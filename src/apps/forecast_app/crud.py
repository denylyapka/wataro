from sqlalchemy.orm import Session

from src.db_app import models


def create_data_about_user_card_deal(tg_id: int, question: str, card_deal: str, db: Session):
    db_user = models.CardDeal(tg_id=tg_id, question=question, card_deal=card_deal)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_question_and_card_deal(tg_id: int, db: Session):
    question = ''
    for item in db.query(models.CardDeal).filter(models.CardDeal.tg_id == tg_id).all():
        question = item.question
    db.query(models.CardDeal).filter(models.CardDeal.tg_id == tg_id).delete()
    db.commit()
    return question

def create_request_history(tg_id: int, question: str, db: Session):
    db_user = models.RequestHistory(tg_id=tg_id, question=question)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


class Forecast:
    @staticmethod
    def get_data_question(tg_id: int, db: Session):
        question = ""
        card_deal = ""
        for item in db.query(models.CardDeal).filter(models.CardDeal.tg_id == tg_id).all():
            question = item.question
            card_deal = item.card_deal
        db.query(models.CardDeal).filter(models.CardDeal.tg_id == tg_id).delete()
        db.commit()
        return question, card_deal

    @staticmethod
    def try_to_edit_status_code(tg_id: int, db: Session):
        user_check = db.query(models.ReferalShip).filter(models.ReferalShip.tg_id_friend == tg_id).first()
        if not user_check:
            return
        if user_check.code == "code":
            user_check.code = "ok"
            db.commit()
