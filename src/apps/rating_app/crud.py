from sqlalchemy.orm import Session

from src.db_app import models


class Rating:
    @staticmethod
    def get_rating_data(tg_id: int, db: Session):
        pre_rating_data = []
        for item in db.query(models.ReferalShip).filter().all():
            if item.code != "ok":
                continue
            try:
                username = (db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == item.tg_id_master).first()).username
            except:
                username = "none"
            data = {"name": "@" + username,
                    "friend_tg_id": item.tg_id_friend,
                    "tg_id": item.tg_id_master}
            if data not in pre_rating_data:
                pre_rating_data.append(data)
        print("pre_rating_data:", pre_rating_data)

        # Результирующий список
        result = []

        for item in pre_rating_data:
            found = next((x for x in result if x['name'] == item['name'] and x['tg_id'] == item['tg_id']), None)

            if found:
                found['quantity'] += 1
            else:
                result.append({
                    'name': item['name'],
                    'quantity': 1,
                    'tg_id': item['tg_id']
                })

        print("result:", result)

        # Сортируем список по значению ключа 'quantity' в порядке убывания
        sorted_data = sorted(result, key=lambda x: x['quantity'], reverse=True)

        # Добавляем параметр "number" начиная с единицы
        for i, item in enumerate(sorted_data):
            item["number"] = i + 1

        your_place = 0
        for item in sorted_data:
            your_place += 1
            if int(item["tg_id"]) == tg_id:
                break
        if str(f"'tg_id': {tg_id}") not in str(sorted_data):
            your_place = 0
        print("sorted_data", sorted_data)
        return sorted_data, your_place

    @staticmethod
    def referal_reg(tg_id_master: int, tg_id_friend: int, code: str, db: Session):
        check_1 = db.query(models.ReferalShip).filter(
            models.ReferalShip.tg_id_master == tg_id_master,
            models.ReferalShip.tg_id_friend == tg_id_friend,
        ).first()
        if check_1:
            return
        if tg_id_friend == tg_id_master:
            return
        db_user = models.ReferalShip(
            tg_id_master=tg_id_master,
            tg_id_friend=tg_id_friend,
            code=code
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return "ok"


class UserData:
    @staticmethod
    def get_username(tg_id: int, db: Session) -> str:
        for item in db.query(models.AccountMetricsData).filter().all():
            if item.tg_id == tg_id:
                print(item.tg_id)
                return item.username
