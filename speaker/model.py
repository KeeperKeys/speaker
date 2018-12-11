from db import BaseModel, db


class User(BaseModel):
    __tablename__ = 'user'

    name = db.Column(db.String)
