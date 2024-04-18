from database.extensions import db


def db_save(obj):
    db.session.add(obj)
    db.session.commit()
