from xmlrpc.client import boolean
from app import db
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Contests(db.Model):
    c_id: int
    name: str
    description: str
    language: str
    created_by: str
    created_on: datetime
    start_date: datetime
    end_date: datetime
    c_status: bool
    p_point: int
    v_point: int


    c_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(4), nullable=False)
    created_by = db.Column(db.String(75), nullable=False)
    created_on = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    c_status = db.Column(db.Boolean, nullable=False)
    p_point = db.Column(db.Integer, nullable=False)
    v_point = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Contest {}>'.format(self.c_id)