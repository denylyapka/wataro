from src.db_app import models

from sqlalchemy.orm import Session


class CreateUser:
    @staticmethod
    def auto_create_user(data: dict, db: Session):
        db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == data["tg_id"]).delete()
        print("data:", data)
        db_user = models.AccountMetricsData(tg_id=data["tg_id"], username=data["username"], name=data["fullname"])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def auto_check_user(tg_id: int, db: Session):
        user_data = db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == tg_id).first()
        return user_data

    @staticmethod
    def get_name(tg_id: int, db: Session):
        user_data = db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == tg_id).first()
        return f"{user_data.name}" if user_data is not None else tg_id

    @staticmethod
    def get_username(tg_id: int, db: Session):
        user_data = db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == tg_id).first()
        return f"@{user_data.username}" if user_data is not None else ""

    @staticmethod
    def get_letter(tg_id: int, db: Session):
        user_data = db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == tg_id).first()
        return str(user_data.name)[:1] if user_data is not None else "?"

    @staticmethod
    def recreate_user(tg_id: int, paul: str, device: str, db: Session):
        user_data = db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == tg_id).first()
        print("paul:", paul)
        print("device:", device)
        if paul != "choice_paul":
            user_data.paul = paul
        if device != "choice_device":
            user_data.device = device
        db.commit()

    @staticmethod
    def get_paul(tg_id: int, db: Session):
        user_data = db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == tg_id).first()
        return str(user_data.paul) if user_data.paul is not None else "Выберите пол"

    @staticmethod
    def get_device(tg_id: int, db: Session):
        user_data = db.query(models.AccountMetricsData).filter(models.AccountMetricsData.tg_id == tg_id).first()
        return str(user_data.device) if user_data.device is not None else "Выберите устройство"


class SubCheck:
    @staticmethod
    def add_user(tg_id: int, flag: str, db: Session):
        user_data = db.query(models.SubsCheckUser_2).filter(models.SubsCheckUser_2.tg_id == tg_id).first()
        if user_data is None:
            db_user = models.SubsCheckUser_2(tg_id=tg_id, flag=flag)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return
        user_data.flag = flag
        db.commit()

    @staticmethod
    def rem_user(tg_id: int, db: Session):
        user_data = db.query(models.SubsCheckUser_2).filter(models.SubsCheckUser_2.tg_id == tg_id).first()
        user_data.flag = "left"
        db.commit()

    @staticmethod
    def check_def(tg_id: int, db: Session):
        user_data = db.query(models.SubsCheckUser_2).filter(models.SubsCheckUser_2.tg_id == tg_id).first()

        if user_data is None:
            return {"code": 304, "status": "Not sub", "message": "Подпишитесь на канал, чтобы продолжить",
                    "link": "https://t.me/+mI53wHAz7u0zNjY6"}

        if user_data.flag == "left":
            return {"code": 304, "status": "Not sub", "message": "Подпишитесь на канал, чтобы продолжить",
                    "link": "https://t.me/+mI53wHAz7u0zNjY6"}
        return {"code": 200, "status": "Have sub", "message": "Начать",
                "link": f"/choicer/{tg_id}"}
