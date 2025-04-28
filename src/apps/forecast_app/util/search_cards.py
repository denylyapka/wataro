import random

from src.apps.forecast_app.index import CARDS


class Deal:

    @staticmethod
    def get_type_arcana() -> str:
        arcans = ['senior', 'junior']
        arcana = random.choice(arcans)
        return arcana

    @staticmethod
    def get_random_group_cards() -> (str, str):
        arcana_type = Deal.get_type_arcana()

        group_list = []
        if arcana_type == 'senior':
            group_list = ['intelligence', 'morals', 'material']
        if arcana_type == 'junior':
            group_list = ['pentacles', 'cups', 'wands', 'swords']
        random_group = random.choice(group_list)
        return arcana_type, random_group

    @staticmethod
    def get_random_card_one() -> dict:
        arcana_type, random_group = Deal.get_random_group_cards()

        max_counter = 0
        if arcana_type == 'senior':
            max_counter = 6
        if arcana_type == 'junior':
            max_counter = 13

        counter = random.randint(0, max_counter)
        card_name = CARDS["Ryder Waite"]["arcana"][arcana_type][random_group][counter]["name"]
        card_img = CARDS["Ryder Waite"]["arcana"][arcana_type][random_group][counter]["photo"]
        card_data = {"name": card_name, "img": card_img}
        return card_data

    @staticmethod
    def get_random_card_one_with_filters(filters: list) -> dict:
        # print("filters:", filters)
        # print('Deal.get_random_card_one()["name"]:', Deal.get_random_card_one()["name"])
        if Deal.get_random_card_one()["name"] in filters:
            return Deal.get_random_card_one_with_filters(filters)
        if Deal.get_random_card_one()["name"] in filters:
            return Deal.get_random_card_one_with_filters(filters)
        if Deal.get_random_card_one()["name"] in filters:
            return Deal.get_random_card_one_with_filters(filters)
        card_data = Deal.get_random_card_one()
        return card_data

    @staticmethod
    def get_random_3_cards() -> dict:
        data_filters = []

        past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            past = Deal.get_random_card_one()
        data_filters.append(past["name"])

        now = Deal.get_random_card_one()
        if now["name"] in data_filters:
            now = Deal.get_random_card_one()
        if now["name"] in data_filters:
            now = Deal.get_random_card_one()
        if now["name"] in data_filters:
            now = Deal.get_random_card_one()
        data_filters.append(now["name"])

        future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            future = Deal.get_random_card_one()
        data_filters.append(future["name"])

        return {"прошлое": past,
                "настоящее": now,
                "будущее": future}

    @staticmethod
    def get_random_cards_for_moon_3() -> dict:
        data_filters = []

        light_side = Deal.get_random_card_one()
        if light_side["name"] in data_filters:
            light_side = Deal.get_random_card_one()
        if light_side["name"] in data_filters:
            light_side = Deal.get_random_card_one()
        if light_side["name"] in data_filters:
            light_side = Deal.get_random_card_one()
        data_filters.append(light_side["name"])

        dark_side = Deal.get_random_card_one()
        if dark_side["name"] in data_filters:
            dark_side = Deal.get_random_card_one()
        if dark_side["name"] in data_filters:
            dark_side = Deal.get_random_card_one()
        if dark_side["name"] in data_filters:
            dark_side = Deal.get_random_card_one()
        data_filters.append(dark_side["name"])

        terminator = Deal.get_random_card_one()
        if terminator["name"] in data_filters:
            terminator = Deal.get_random_card_one()
        if terminator["name"] in data_filters:
            terminator = Deal.get_random_card_one()
        if terminator["name"] in data_filters:
            terminator = Deal.get_random_card_one()
        data_filters.append(terminator["name"])

        return {"Освещённая сторона": light_side,
                "Тёмная сторона": dark_side,
                "Переходная зона": terminator}

    @staticmethod
    def get_random_cards_for_moon_phases() -> dict:
        data_filters = []

        new_moon = Deal.get_random_card_one()
        if new_moon["name"] in data_filters:
            new_moon = Deal.get_random_card_one()
        if new_moon["name"] in data_filters:
            new_moon = Deal.get_random_card_one()
        if new_moon["name"] in data_filters:
            new_moon = Deal.get_random_card_one()
        data_filters.append(new_moon["name"])

        first_half_half = Deal.get_random_card_one()
        if first_half_half["name"] in data_filters:
            first_half_half = Deal.get_random_card_one()
        if first_half_half["name"] in data_filters:
            first_half_half = Deal.get_random_card_one()
        if first_half_half["name"] in data_filters:
            first_half_half = Deal.get_random_card_one()
        data_filters.append(first_half_half["name"])

        full_moon = Deal.get_random_card_one()
        if full_moon["name"] in data_filters:
            full_moon = Deal.get_random_card_one()
        if full_moon["name"] in data_filters:
            full_moon = Deal.get_random_card_one()
        if full_moon["name"] in data_filters:
            full_moon = Deal.get_random_card_one()
        data_filters.append(full_moon["name"])

        last_half_half = Deal.get_random_card_one()
        if last_half_half["name"] in data_filters:
            last_half_half = Deal.get_random_card_one()
        if last_half_half["name"] in data_filters:
            last_half_half = Deal.get_random_card_one()
        if last_half_half["name"] in data_filters:
            last_half_half = Deal.get_random_card_one()
        data_filters.append(last_half_half["name"])

        return {"Новолуние": new_moon,
                "Первая четверть": first_half_half,
                "Полнолуние": full_moon,
                "Последняя четверть": last_half_half}


    @staticmethod
    def get_random_10_cards() -> dict:
        data_filters = []

        currency_situation = Deal.get_random_card_one()
        if currency_situation["name"] in data_filters:
            currency_situation = Deal.get_random_card_one()
        if currency_situation["name"] in data_filters:
            currency_situation = Deal.get_random_card_one()
        if currency_situation["name"] in data_filters:
            currency_situation = Deal.get_random_card_one()
        data_filters.append(currency_situation["name"])

        troubles = Deal.get_random_card_one()
        if troubles["name"] in data_filters:
            troubles = Deal.get_random_card_one()
        if troubles["name"] in data_filters:
            troubles = Deal.get_random_card_one()
        if troubles["name"] in data_filters:
            troubles = Deal.get_random_card_one()
        data_filters.append(troubles["name"])

        opportunities = Deal.get_random_card_one()
        if opportunities["name"] in data_filters:
            opportunities = Deal.get_random_card_one()
        if opportunities["name"] in data_filters:
            opportunities = Deal.get_random_card_one()
        if opportunities["name"] in data_filters:
            opportunities = Deal.get_random_card_one()
        data_filters.append(opportunities["name"])

        reasons = Deal.get_random_card_one()
        if reasons["name"] in data_filters:
            reasons = Deal.get_random_card_one()
        if reasons["name"] in data_filters:
            reasons = Deal.get_random_card_one()
        if reasons["name"] in data_filters:
            reasons = Deal.get_random_card_one()
        data_filters.append(reasons["name"])

        past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            past = Deal.get_random_card_one()
        data_filters.append(past["name"])

        future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            future = Deal.get_random_card_one()
        data_filters.append(future["name"])

        your_position = Deal.get_random_card_one()
        if your_position["name"] in data_filters:
            your_position = Deal.get_random_card_one()
        if your_position["name"] in data_filters:
            your_position = Deal.get_random_card_one()
        if your_position["name"] in data_filters:
            your_position = Deal.get_random_card_one()
        data_filters.append(your_position["name"])

        env_position = Deal.get_random_card_one()
        if env_position["name"] in data_filters:
            env_position = Deal.get_random_card_one()
        if env_position["name"] in data_filters:
            env_position = Deal.get_random_card_one()
        if env_position["name"] in data_filters:
            env_position = Deal.get_random_card_one()
        data_filters.append(env_position["name"])

        hopes_and_fears = Deal.get_random_card_one()
        if hopes_and_fears["name"] in data_filters:
            hopes_and_fears = Deal.get_random_card_one()
        if hopes_and_fears["name"] in data_filters:
            hopes_and_fears = Deal.get_random_card_one()
        if hopes_and_fears["name"] in data_filters:
            hopes_and_fears = Deal.get_random_card_one()
        data_filters.append(hopes_and_fears["name"])

        issue = Deal.get_random_card_one()
        if issue["name"] in data_filters:
            issue = Deal.get_random_card_one()
        if issue["name"] in data_filters:
            issue = Deal.get_random_card_one()
        if issue["name"] in data_filters:
            issue = Deal.get_random_card_one()
        data_filters.append(issue["name"])

        return {
            "currency_situation": currency_situation,
            "troubles": troubles,
            "opportunities": opportunities,
            "reasons": reasons,
            "past": past,
            "future": future,
            "your_position": your_position,
            "env_position": env_position,
            "hopes_and_fears": hopes_and_fears,
            "issue": issue
        }

    @staticmethod
    def get_6_cards() -> dict:
        data_filters = []

        card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        data_filters.append(card_1["name"])

        card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        data_filters.append(card_2["name"])

        card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        data_filters.append(card_3["name"])

        card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        data_filters.append(card_4["name"])

        card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        data_filters.append(card_5["name"])

        card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        data_filters.append(card_6["name"])

        return {"Текущее состояние отношений": card_1,
                "Главный вопрос или конфликт": card_2,
                "Совет для разрешения": card_3,
                "Влияние внешних факторов": card_4,
                "Энергия, которую нужно отпустить": card_5,
                "Перспективы (6–12 месяцев)": card_6}

    @staticmethod
    def get_6_cards_work() -> dict:
        data_filters = []

        card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        data_filters.append(card_1["name"])

        card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        data_filters.append(card_2["name"])

        card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        data_filters.append(card_3["name"])

        card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        data_filters.append(card_4["name"])

        card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        data_filters.append(card_5["name"])

        card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        data_filters.append(card_6["name"])

        return {"Текущее положение в карьере": card_1,
                "Основное препятствие": card_2,
                "Совет от Высших Сил": card_3,
                "Скрытые возможности": card_4,
                "Энергия, которую нужно развить": card_5,
                "Итоговый прогноз (3–6 месяцев)": card_6}

    @staticmethod
    def get_6_cards_live_energy() -> dict:
        data_filters = []

        card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        if card_1["name"] in data_filters:
            card_1 = Deal.get_random_card_one()
        data_filters.append(card_1["name"])

        card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        if card_2["name"] in data_filters:
            card_2 = Deal.get_random_card_one()
        data_filters.append(card_2["name"])

        card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        if card_3["name"] in data_filters:
            card_3 = Deal.get_random_card_one()
        data_filters.append(card_3["name"])

        card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        if card_4["name"] in data_filters:
            card_4 = Deal.get_random_card_one()
        data_filters.append(card_4["name"])

        card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        if card_5["name"] in data_filters:
            card_5 = Deal.get_random_card_one()
        data_filters.append(card_5["name"])

        card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        if card_6["name"] in data_filters:
            card_6 = Deal.get_random_card_one()
        data_filters.append(card_6["name"])

        return {"Текущее состояние энергии": card_1,
                "Главное препятствие": card_2,
                "Совет для пробуждения": card_3,
                "Скрытый источник энергии": card_4,
                "Энергия, которую нужно отпустить": card_5,
                "Перспективы (3–6 месяцев)": card_6}
