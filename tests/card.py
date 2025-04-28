import random

from src.apps.forecast_app.index import CARDS as cards_data


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
        card_name = cards_data["Ryder Waite"]["arcana"][arcana_type][random_group][counter]["name"]
        card_img = cards_data["Ryder Waite"]["arcana"][arcana_type][random_group][counter]["photo"]
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
            print("block repeat")
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            print("block repeat x2")
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            print("block repeat x3")
            past = Deal.get_random_card_one()
        data_filters.append(past["name"])

        now = Deal.get_random_card_one()
        if now["name"] in data_filters:
            print("block repeat")
            now = Deal.get_random_card_one()
        if now["name"] in data_filters:
            print("block repeat x2")
            now = Deal.get_random_card_one()
        if now["name"] in data_filters:
            print("block repeat x3")
            now = Deal.get_random_card_one()
        data_filters.append(now["name"])

        future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            print("block repeat")
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            print("block repeat x2")
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            print("block repeat x3")
            future = Deal.get_random_card_one()
        data_filters.append(future["name"])

        return {"прошлое": past,
                "настоящее": now,
                "будущее": future}

    @staticmethod
    def get_random_10_cards() -> dict:
        data_filters = []

        currency_situation = Deal.get_random_card_one()
        if currency_situation["name"] in data_filters:
            print("block repeat")
            currency_situation = Deal.get_random_card_one()
        if currency_situation["name"] in data_filters:
            print("block repeat x2")
            currency_situation = Deal.get_random_card_one()
        if currency_situation["name"] in data_filters:
            print("block repeat x3")
            currency_situation = Deal.get_random_card_one()
        data_filters.append(currency_situation["name"])

        troubles = Deal.get_random_card_one()
        if troubles["name"] in data_filters:
            print("block repeat")
            troubles = Deal.get_random_card_one()
        if troubles["name"] in data_filters:
            print("block repeat x2")
            troubles = Deal.get_random_card_one()
        if troubles["name"] in data_filters:
            print("block repeat x3")
            troubles = Deal.get_random_card_one()
        data_filters.append(troubles["name"])

        opportunities = Deal.get_random_card_one()
        if opportunities["name"] in data_filters:
            print("block repeat")
            opportunities = Deal.get_random_card_one()
        if opportunities["name"] in data_filters:
            print("block repeat x2")
            opportunities = Deal.get_random_card_one()
        if opportunities["name"] in data_filters:
            print("block repeat x3")
            opportunities = Deal.get_random_card_one()
        data_filters.append(opportunities["name"])

        reasons = Deal.get_random_card_one()
        if reasons["name"] in data_filters:
            print("block repeat")
            reasons = Deal.get_random_card_one()
        if reasons["name"] in data_filters:
            print("block repeat x2")
            reasons = Deal.get_random_card_one()
        if reasons["name"] in data_filters:
            print("block repeat x3")
            reasons = Deal.get_random_card_one()
        data_filters.append(reasons["name"])

        past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            print("block repeat")
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            print("block repeat x2")
            past = Deal.get_random_card_one()
        if past["name"] in data_filters:
            print("block repeat x3")
            past = Deal.get_random_card_one()
        data_filters.append(past["name"])

        future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            print("block repeat")
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            print("block repeat x2")
            future = Deal.get_random_card_one()
        if future["name"] in data_filters:
            print("block repeat x3")
            future = Deal.get_random_card_one()
        data_filters.append(future["name"])

        your_position = Deal.get_random_card_one()
        if your_position["name"] in data_filters:
            print("block repeat")
            your_position = Deal.get_random_card_one()
        if your_position["name"] in data_filters:
            print("block repeat x2")
            your_position = Deal.get_random_card_one()
        if your_position["name"] in data_filters:
            print("block repeat x3")
            your_position = Deal.get_random_card_one()
        data_filters.append(your_position["name"])

        env_position = Deal.get_random_card_one()
        if env_position["name"] in data_filters:
            print("block repeat")
            env_position = Deal.get_random_card_one()
        if env_position["name"] in data_filters:
            print("block repeat x2")
            env_position = Deal.get_random_card_one()
        if env_position["name"] in data_filters:
            print("block repeat x3")
            env_position = Deal.get_random_card_one()
        data_filters.append(env_position["name"])

        hopes_and_fears = Deal.get_random_card_one()
        if hopes_and_fears["name"] in data_filters:
            print("block repeat")
            hopes_and_fears = Deal.get_random_card_one()
        if hopes_and_fears["name"] in data_filters:
            print("block repeat x2")
            hopes_and_fears = Deal.get_random_card_one()
        if hopes_and_fears["name"] in data_filters:
            print("block repeat x3")
            hopes_and_fears = Deal.get_random_card_one()
        data_filters.append(hopes_and_fears["name"])

        issue = Deal.get_random_card_one()
        if issue["name"] in data_filters:
            print("block repeat")
            issue = Deal.get_random_card_one()
        if issue["name"] in data_filters:
            print("block repeat x2")
            issue = Deal.get_random_card_one()
        if issue["name"] in data_filters:
            print("block repeat x3")
            issue = Deal.get_random_card_one()
        data_filters.append(issue["name"])

        print(data_filters)

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
