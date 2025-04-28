from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.apps.forecast_app.gigachat.gigachat_api import send_prompt, get_access_token
from src.apps.forecast_app.util.search_cards import Deal
from src.db_app.main import get_db
from . import crud
from .index import DEALS

templates = Jinja2Templates(directory="src/templates")
router = APIRouter(prefix="/forecast", tags=["Получить предсказание"], include_in_schema=False)

check_list = ["не профессиональный таролог", "мне не удалось", "противоречит моим", "генеративная", "не могу",
              "не являюсь", "не знаю", "профессиональн"]


@router.get("/{id_deal}/{tg_id}")
async def info_forecast_universal(id_deal: int, tg_id: int, r: Request):
    return templates.TemplateResponse("forecast_info.html", {
        "request": r, "id_deal": id_deal, "tg_id": tg_id, "data_deal": DEALS[id_deal]
    })


@router.post("/get_answer")
async def get_answer(body: dict, db: Session = Depends(get_db)):
    print("body:", body)
    tg_id = body["tg_id"]
    crud.Forecast.try_to_edit_status_code(tg_id, db)

    prediction_list = []
    pre_questions = []

    if body["card_deal"] == '0':
        question = body["question"]
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_random_card_one()
        question = question.strip()  # Убираем лишние пробелы

        user_prompt = (
            f'Представь что ты профессиональный таролог и напиши, пожалуйста, предсказание таро ровно на 100 слов '
            f'по карте {card_data["name"]} на вопрос {question}{"?" if "?" not in question else ""}')
        response = send_prompt(user_prompt, get_access_token())
        n = 0
        while n != 3:
            n += 1
            for item in check_list:
                if item in response:
                    response = send_prompt(user_prompt, get_access_token())
                else:
                    break

        prediction_list = [
            {"question": question, "prediction_card": card_data["name"],
             "prediction_answer": response.replace('*', ''), "image": card_data["img"]}
        ]

        # Получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))
    elif body["card_deal"] == '1':
        def process_prediction(card_name, time_period, question_):
            # Создаем prompt
            user_prompt_ = (
                f'Представь что ты профессиональный таролог и напиши, пожалуйста, краткое предсказание таро '
                f'по карте "{card_name}" на вопрос "{question_}{"?" if "?" not in question_ else ""}" в раскладе '
                f'"Триплет" описывая {time_period}.'
            )

            # Получаем ответ
            response_ = send_prompt(user_prompt_, get_access_token())

            # Проверяем наличие запрещенных элементов
            while any(item_ in response_ for item_ in check_list):
                response_ = send_prompt(user_prompt_, get_access_token())

            return response_

        question = body["question"]
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_random_3_cards()
        question = question.strip()  # Убираем лишние пробелы

        # Обрабатываем каждую карту
        response_past = process_prediction(card_data['прошлое']['name'], 'прошлое', question)
        response_now = process_prediction(card_data['настоящее']['name'], 'настоящее', question)
        response_future = process_prediction(card_data['будущее']['name'], 'будущее', question)

        # Формируем итоговый список предсказаний
        prediction_list = [
            {"question": f"{question} (\"Прошлое\")", "prediction_card": card_data["прошлое"]["name"],
             "prediction_answer": response_past.replace('*', ''), "image": card_data["прошлое"]["img"]},
            {"question": f"{question} (\"Настоящее\")", "prediction_card": card_data["настоящее"]["name"],
             "prediction_answer": response_now.replace('*', ''), "image": card_data["настоящее"]["img"]},
            {"question": f"{question} (\"Будущее\")", "prediction_card": card_data["будущее"]["name"],
             "prediction_answer": response_future.replace('*', ''), "image": card_data["будущее"]["img"]}
        ]

        # получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))
    elif body["card_deal"] == '2':
        def process_prediction(card_name, step, question_):
            # Создаем prompt
            user_prompt_ = (
                f'Представь что ты профессиональный таролог и напиши, пожалуйста, краткое предсказание таро '
                f'по карте "{card_name}" на вопрос "{question_}{"?" if "?" not in question_ else ""}" в раскладе '
                f'"Кельтский крест" описывая {step}.'
            )

            # Получаем ответ
            response_ = send_prompt(user_prompt_, get_access_token())

            # Проверяем наличие запрещенных элементов
            while any(item_ in response_ for item_ in check_list):
                response_ = send_prompt(user_prompt_, get_access_token())

            return response_

        question = body["question"]
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_random_10_cards()
        question = question.strip()  # Убираем лишние пробелы

        # Обрабатываем каждую карту
        response_currency_situation = process_prediction(card_data['currency_situation']['name'], 'текущую ситуацию', question)
        response_troubles = process_prediction(card_data['troubles']['name'], 'проблемы', question)
        response_opportunities = process_prediction(card_data['opportunities']['name'], 'возможности', question)
        response_reasons = process_prediction(card_data['reasons']['name'], 'причины', question)
        response_past = process_prediction(card_data['past']['name'], 'прошлое', question)
        response_future = process_prediction(card_data['future']['name'], 'будущее', question)
        response_your_position = process_prediction(card_data['your_position']['name'], 'позицию человека который загадал вопрос', question)
        response_env_position = process_prediction(card_data['env_position']['name'], 'позицию окружающих', question)
        response_hopes_and_fears = process_prediction(card_data['hopes_and_fears']['name'], 'надежды и страхи', question)
        response_issue = process_prediction(card_data['issue']['name'], 'итог', question)

        prediction_list = [
            {"question": f"{question} (\"Текущая ситуация\")",
             "prediction_card": card_data["currency_situation"]["name"],
             "prediction_answer": response_currency_situation.replace('*', ''), "image": card_data["currency_situation"]["img"]},
            {"question": f"{question} (\"Проблемы\")", "prediction_card": card_data["troubles"]["name"],
             "prediction_answer": response_troubles.replace('*', ''), "image": card_data["troubles"]["img"]},
            {"question": f"{question} (\"Возможности\")", "prediction_card": card_data["opportunities"]["name"],
             "prediction_answer": response_opportunities.replace('*', ''), "image": card_data["opportunities"]["img"]},
            {"question": f"{question} (\"Причины\")", "prediction_card": card_data["reasons"]["name"],
             "prediction_answer": response_reasons.replace('*', ''), "image": card_data["reasons"]["img"]},
            {"question": f"{question} (\"Прошлое\")", "prediction_card": card_data["past"]["name"],
             "prediction_answer": response_past.replace('*', ''), "image": card_data["past"]["img"]},
            {"question": f"{question} (\"Будущее\")", "prediction_card": card_data["future"]["name"],
             "prediction_answer": response_future.replace('*', ''), "image": card_data["future"]["img"]},
            {"question": f"{question} (\"Ваша позиция\")", "prediction_card": card_data["your_position"]["name"],
             "prediction_answer": response_your_position.replace('*', ''), "image": card_data["your_position"]["img"]},
            {"question": f"{question} (\"Позиция окружающих\")", "prediction_card": card_data["env_position"]["name"],
             "prediction_answer": response_env_position.replace('*', ''), "image": card_data["env_position"]["img"]},
            {"question": f"{question} (\"Возможности\")", "prediction_card": card_data["hopes_and_fears"]["name"],
             "prediction_answer": response_hopes_and_fears.replace('*', ''), "image": card_data["hopes_and_fears"]["img"]},
            {"question": f"{question} (\"Итог\")", "prediction_card": card_data["issue"]["name"],
             "prediction_answer": response_issue.replace('*', ''), "image": card_data["issue"]["img"]},
        ]

        # получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))
    elif body["card_deal"] == "40" or "42":
        def process_prediction(card_name, time_period, question_):
            # Создаем prompt
            user_prompt_ = (
                f'Представь что ты профессиональный таролог и напиши, пожалуйста, краткое предсказание таро '
                f'по карте "{card_name}" на вопрос "{question_}{"?" if "?" not in question_ else ""}" описывая '
                f'{time_period}.'
            )

            # Получаем ответ
            response_ = send_prompt(user_prompt_, get_access_token())

            # Проверяем наличие запрещенных элементов
            while any(item_ in response_ for item_ in check_list):
                response_ = send_prompt(user_prompt_, get_access_token())

            return response_

        question = body["question"]
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_random_cards_for_moon_phases()
        question = question.strip()  # Убираем лишние пробелы

        response_new_moon = ""
        response_first_half_half = ""
        response_full_moon = ""
        response_second_half_half = ""
        # Обрабатываем каждую карту
        if body["card_deal"] == "40":
            response_new_moon = process_prediction(card_data['Новолуние']['name'], 'Новолуние: Какие новые ритуалы или практики стоит начать?', question)
            response_first_half_half = process_prediction(card_data['Первая четверть']['name'], 'Первая четверть: Какие действия помогут укрепить твою энергию и мотивацию?', question)
            response_full_moon = process_prediction(card_data['Полнолуние']['name'], 'Полнолуние: Какие ритуалы очищения и освобождения будут полезны?', question)
            response_second_half_half = process_prediction(card_data['Последняя четверть']['name'], 'Последняя четверть: Какие практики помогут тебе расслабиться и восстановиться?', question)
        if body["card_deal"] == "42":
            response_new_moon = process_prediction(card_data['Новолуние']['name'], 'Новолуние: Что нужно начать? Какие новые идеи или проекты требуют твоего внимания?', question)
            response_first_half_half = process_prediction(card_data['Первая четверть']['name'], 'Первая четверть: Как продвигается мой путь? Есть ли препятствия, которые нужно преодолеть?', question)
            response_full_moon = process_prediction(card_data['Полнолуние']['name'], 'Полнолуние: Какое освещение приходит в мою жизнь? Какие скрытые истины открываются?', question)
            response_second_half_half = process_prediction(card_data['Последняя четверть']['name'], 'Последняя четверть: Что нужно отпустить? Какие старые привычки или убеждения больше не служат мне?', question)

        # Формируем итоговый список предсказаний
        prediction_list = [
            {"question": f"{question} (\"Новолуние\")", "prediction_card": card_data["Новолуние"]["name"],
             "prediction_answer": response_new_moon.replace('*', ''), "image": card_data["Новолуние"]["img"]},
            {"question": f"{question} (\"Первая четверть\")", "prediction_card": card_data["Первая четверть"]["name"],
             "prediction_answer": response_first_half_half.replace('*', ''), "image": card_data["Первая четверть"]["img"]},
            {"question": f"{question} (\"Полнолуние\")", "prediction_card": card_data["Полнолуние"]["name"],
             "prediction_answer": response_full_moon.replace('*', ''), "image": card_data["Полнолуние"]["img"]},
            {"question": f"{question} (\"Последняя четверть\")", "prediction_card": card_data["Последняя четверть"]["name"],
             "prediction_answer": response_second_half_half.replace('*', ''), "image": card_data["Последняя четверть"]["img"]}
        ]

        # получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))
    elif body["card_deal"] == "41":
        def process_prediction(card_name, time_period, question_):
            # Создаем prompt
            user_prompt_ = (
                f'Представь что ты профессиональный таролог и напиши, пожалуйста, краткое предсказание таро '
                f'по карте "{card_name}" на вопрос "{question_}{"?" if "?" not in question_ else ""}" описывая '
                f'{time_period}.'
            )

            # Получаем ответ
            response_ = send_prompt(user_prompt_, get_access_token())

            # Проверяем наличие запрещенных элементов
            while any(item_ in response_ for item_ in check_list):
                response_ = send_prompt(user_prompt_, get_access_token())

            return response_

        question = body["question"]
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_random_cards_for_moon_3()
        question = question.strip()  # Убираем лишние пробелы

        # Обрабатываем каждую карту
        response_light_side = process_prediction(card_data['Освещённая сторона']['name'], 'Освещённая сторона: Что приносит мне радость и удовлетворение? Какие аспекты моей жизни находятся под благоприятным влиянием Луны?', question)
        response_dark_side = process_prediction(card_data['Тёмная сторона']['name'], 'Тёмная сторона: Какие страхи или сомнения мешают мне двигаться вперёд? Какие аспекты моей жизни нуждаются в проработке?', question)
        response_terminator = process_prediction(card_data['Переходная зона']['name'], 'Переходная зона: Какие изменения происходят в моей жизни? Какие возможности открываются перед мной?', question)

        # Формируем итоговый список предсказаний
        prediction_list = [
            {"question": f"{question} (\"Освещённая сторона\")", "prediction_card": card_data["Освещённая сторона"]["name"],
             "prediction_answer": response_light_side.replace('*', ''), "image": card_data["Освещённая сторона"]["img"]},
            {"question": f"{question} (\"Тёмная сторона\")", "prediction_card": card_data["Тёмная сторона"]["name"],
             "prediction_answer": response_dark_side.replace('*', ''), "image": card_data["Тёмная сторона"]["img"]},
            {"question": f"{question} (\"Переходная зона\")", "prediction_card": card_data["Переходная зона"]["name"],
             "prediction_answer": response_terminator.replace('*', ''), "image": card_data["Переходная зона"]["img"]},
        ]

        # получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))

    response = {
        "prediction_list": prediction_list, "ready_questions_list": pre_questions
    }
    return response


@router.post("/add_question")
async def add_question(body: dict, db: Session = Depends(get_db)):
    print("body (add_question):", body)
    tg_id = body["tg_id"]
    crud.Forecast.try_to_edit_status_code(tg_id, db)

    question = body["question"]
    crud.create_request_history(tg_id=tg_id, question=question, db=db)

    # Основной блок кода
    card_data = Deal.get_random_card_one()
    question = question.strip()  # Убираем лишние пробелы

    user_prompt = (
        f'Представь что ты профессиональный таролог и напиши, пожалуйста, предсказание таро ровно на 100 слов '
        f'по карте {card_data["name"]} на вопрос {question}{"?" if "?" not in question else ""}')
    response = send_prompt(user_prompt, get_access_token())
    n = 0
    while n != 3:
        n += 1
        for item in check_list:
            if item in response:
                response = send_prompt(user_prompt, get_access_token())
            else:
                pass

    prediction_list = [
        {"question": question, "prediction_card": card_data["name"],
         "prediction_answer": response, "image": card_data["img"]}
    ]

    response = {
        "prediction_list": prediction_list
    }
    return response


@router.post("/get_answer_with_data")
async def get_answer_with_data(body: dict, db: Session = Depends(get_db)):
    print("body:", body)
    tg_id = body["tg_id"]
    crud.Forecast.try_to_edit_status_code(tg_id, db)

    prediction_list = []
    pre_questions = []

    if body["card_deal"] == '10':
        def process_prediction(card_name, time_period, question_):
            # Создаем prompt
            user_prompt_ = (
                f'Представь что ты профессиональный таролог и напиши, пожалуйста, краткое предсказание таро '
                f'по карте "{card_name}" на вопрос "{question_}{"?" if "?" not in question_ else ""}" '
                f'описывая {time_period}.'
            )

            # Получаем ответ
            response_ = send_prompt(user_prompt_, get_access_token())

            # Проверяем наличие запрещенных элементов
            while any(item_ in response_ for item_ in check_list):
                response_ = send_prompt(user_prompt_, get_access_token())

            return response_

        question = f"Любовный расклад по данным:\n\n" \
                   f"Возраст: {body['age']}\n" \
                   f"Текущее положение: {body['workNow']}\n" \
                   f"Пол: {body['paul']}\n" \
                   f"Цель: {body['direction']}"
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_6_cards()
        question = question.strip()  # Убираем лишние пробелы

        # Обрабатываем каждую карту
        response_1 = process_prediction(card_data['Текущее состояние отношений']['name'], 'Текущее состояние отношений', question)
        response_2 = process_prediction(card_data['Главный вопрос или конфликт']['name'], 'Главный вопрос или конфликт', question)
        response_3 = process_prediction(card_data['Совет для разрешения']['name'], 'Совет для разрешения', question)
        response_4 = process_prediction(card_data['Влияние внешних факторов']['name'], 'Влияние внешних факторов', question)
        response_5 = process_prediction(card_data['Энергия, которую нужно отпустить']['name'], 'Энергия, которую нужно отпустить', question)
        response_6 = process_prediction(card_data['Перспективы (6–12 месяцев)']['name'], 'Перспективы (6–12 месяцев)', question)

        # Формируем итоговый список предсказаний
        prediction_list = [
            {"question": "(\"Текущее состояние отношений\")", "prediction_card": card_data["Текущее состояние отношений"]["name"],
             "prediction_answer": response_1.replace('*', ''), "image": card_data["Текущее состояние отношений"]["img"]},
            {"question": "(\"Главный вопрос или конфликт\")", "prediction_card": card_data["Главный вопрос или конфликт"]["name"],
             "prediction_answer": response_2.replace('*', ''), "image": card_data["Главный вопрос или конфликт"]["img"]},
            {"question": "(\"Совет для разрешения\")", "prediction_card": card_data["Совет для разрешения"]["name"],
             "prediction_answer": response_3.replace('*', ''), "image": card_data["Совет для разрешения"]["img"]},
            {"question": "(\"Влияние внешних факторов\")", "prediction_card": card_data["Влияние внешних факторов"]["name"],
             "prediction_answer": response_4.replace('*', ''), "image": card_data["Влияние внешних факторов"]["img"]},
            {"question": "(\"Энергия, которую нужно отпустить\")", "prediction_card": card_data["Энергия, которую нужно отпустить"]["name"],
             "prediction_answer": response_5.replace('*', ''), "image": card_data["Энергия, которую нужно отпустить"]["img"]},
            {"question": "(\"Перспективы (6–12 месяцев)\")", "prediction_card": card_data["Перспективы (6–12 месяцев)"]["name"],
             "prediction_answer": response_6.replace('*', ''), "image": card_data["Перспективы (6–12 месяцев)"]["img"]}
        ]

        # получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))
    elif body["card_deal"] == '20':
        def process_prediction(card_name, time_period, question_):
            # Создаем prompt
            user_prompt_ = (
                f'Представь что ты профессиональный таролог и напиши, пожалуйста, краткое предсказание таро '
                f'по карте "{card_name}" на вопрос "{question_}{"?" if "?" not in question_ else ""}" '
                f'описывая {time_period}.'
            )

            # Получаем ответ
            response_ = send_prompt(user_prompt_, get_access_token())

            # Проверяем наличие запрещенных элементов
            while any(item_ in response_ for item_ in check_list):
                response_ = send_prompt(user_prompt_, get_access_token())

            return response_

        question = f"Расклад по карьере по данным:\n\n" \
                   f"Возраст: {body['age']}\n" \
                   f"Текущее положение: {body['workNow']}\n" \
                   f"Пол: {body['paul']}\n" \
                   f"Цель: {body['direction']}"
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_6_cards_work()
        question = question.strip()  # Убираем лишние пробелы

        # Обрабатываем каждую карту
        response_1 = process_prediction(card_data['Текущее положение в карьере']['name'], 'Текущее положение в карьере', question)
        response_2 = process_prediction(card_data['Основное препятствие']['name'], 'Основное препятствие', question)
        response_3 = process_prediction(card_data['Совет от Высших Сил']['name'], 'Совет от Высших Сил', question)
        response_4 = process_prediction(card_data['Скрытые возможности']['name'], 'Скрытые возможности', question)
        response_5 = process_prediction(card_data['Энергия, которую нужно развить']['name'], 'Энергия, которую нужно развить', question)
        response_6 = process_prediction(card_data['Итоговый прогноз (3–6 месяцев)']['name'], 'Итоговый прогноз (3–6 месяцев)', question)

        # Формируем итоговый список предсказаний
        prediction_list = [
            {"question": "(\"Текущее положение в карьере\")", "prediction_card": card_data["Текущее положение в карьере"]["name"],
             "prediction_answer": response_1.replace('*', ''), "image": card_data["Текущее положение в карьере"]["img"]},
            {"question": "(\"Основное препятствие\")", "prediction_card": card_data["Основное препятствие"]["name"],
             "prediction_answer": response_2.replace('*', ''), "image": card_data["Основное препятствие"]["img"]},
            {"question": "(\"Совет от Высших Сил\")", "prediction_card": card_data["Совет от Высших Сил"]["name"],
             "prediction_answer": response_3.replace('*', ''), "image": card_data["Совет от Высших Сил"]["img"]},
            {"question": "(\"Скрытые возможности\")", "prediction_card": card_data["Скрытые возможности"]["name"],
             "prediction_answer": response_4.replace('*', ''), "image": card_data["Скрытые возможности"]["img"]},
            {"question": "(\"Энергия, которую нужно развить\")", "prediction_card": card_data["Энергия, которую нужно развить"]["name"],
             "prediction_answer": response_5.replace('*', ''), "image": card_data["Энергия, которую нужно развить"]["img"]},
            {"question": "(\"Итоговый прогноз (3–6 месяцев)\")", "prediction_card": card_data["Итоговый прогноз (3–6 месяцев)"]["name"],
             "prediction_answer": response_6.replace('*', ''), "image": card_data["Итоговый прогноз (3–6 месяцев)"]["img"]}
        ]

        # получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))
    elif body["card_deal"] == '30':
        def process_prediction(card_name, time_period, question_):
            # Создаем prompt
            user_prompt_ = (
                f'Представь что ты профессиональный таролог и напиши, пожалуйста, краткое предсказание таро '
                f'по карте "{card_name}" на вопрос "{question_}{"?" if "?" not in question_ else ""}" '
                f'описывая {time_period}.'
            )

            # Получаем ответ
            response_ = send_prompt(user_prompt_, get_access_token())

            # Проверяем наличие запрещенных элементов
            while any(item_ in response_ for item_ in check_list):
                response_ = send_prompt(user_prompt_, get_access_token())

            return response_

        question = f"Расклад 'Поиск жизненной энергии' по данным:\n\n" \
                   f"Возраст: {body['age']}\n" \
                   f"Текущее положение: {body['workNow']}\n" \
                   f"Пол: {body['paul']}\n" \
                   f"Цель: {body['direction']}"
        crud.create_request_history(tg_id=tg_id, question=question, db=db)

        # Основной блок кода
        card_data = Deal.get_6_cards_live_energy()
        question = question.strip()  # Убираем лишние пробелы

        # Обрабатываем каждую карту
        response_1 = process_prediction(card_data['Текущее состояние энергии']['name'], 'Текущее состояние энергии', question)
        response_2 = process_prediction(card_data['Главное препятствие']['name'], 'Главное препятствие', question)
        response_3 = process_prediction(card_data['Совет для пробуждения']['name'], 'Совет для пробуждения', question)
        response_4 = process_prediction(card_data['Скрытый источник энергии']['name'], 'Скрытый источник энергии', question)
        response_5 = process_prediction(card_data['Энергия, которую нужно отпустить']['name'], 'Энергия, которую нужно отпустить', question)
        response_6 = process_prediction(card_data['Перспективы (3–6 месяцев)']['name'], 'Перспективы (3–6 месяцев)', question)

        # Формируем итоговый список предсказаний
        prediction_list = [
            {"question": "(\"Текущее состояние энергии\")", "prediction_card": card_data["Текущее состояние энергии"]["name"],
             "prediction_answer": response_1.replace('*', ''), "image": card_data["Текущее состояние энергии"]["img"]},
            {"question": "(\"Главное препятствие\")", "prediction_card": card_data["Главное препятствие"]["name"],
             "prediction_answer": response_2.replace('*', ''), "image": card_data["Главное препятствие"]["img"]},
            {"question": "(\"Совет для пробуждения\")", "prediction_card": card_data["Совет для пробуждения"]["name"],
             "prediction_answer": response_3.replace('*', ''), "image": card_data["Совет для пробуждения"]["img"]},
            {"question": "(\"Скрытый источник энергии\")", "prediction_card": card_data["Скрытый источник энергии"]["name"],
             "prediction_answer": response_4.replace('*', ''), "image": card_data["Скрытый источник энергии"]["img"]},
            {"question": "(\"Энергия, которую нужно отпустить\")", "prediction_card": card_data["Энергия, которую нужно отпустить"]["name"],
             "prediction_answer": response_5.replace('*', ''), "image": card_data["Энергия, которую нужно отпустить"]["img"]},
            {"question": "(\"Перспективы (3–6 месяцев)\")", "prediction_card": card_data["Перспективы (3–6 месяцев)"]["name"],
             "prediction_answer": response_6.replace('*', ''), "image": card_data["Перспективы (3–6 месяцев)"]["img"]}
        ]

        # получение доп вопросов
        user_prompt = f'Составь 1 дополнительный вопрос (без описания) к раскладу ' \
                      f'{DEALS[int(body["card_deal"])]["name"]}.'
        pre_questions.append(send_prompt(user_prompt, get_access_token()))

    response = {
        "prediction_list": prediction_list, "ready_questions_list": pre_questions
    }
    return response