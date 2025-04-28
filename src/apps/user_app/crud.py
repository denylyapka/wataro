from src.db_app import models

from sqlalchemy.orm import Session


class CreateUser:
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
