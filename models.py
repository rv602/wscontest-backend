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
    name = db.Column(db.String(190), nullable=False)
    description = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(4), nullable=False)
    created_by = db.Column(db.String(190), nullable=False)
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

@dataclass
class ContestAdmin(db.Model):
    c_id: int
    user_name: str

    c_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(190), nullable=False)

    def __repr__(self):
        return '<ContestAdmin {}>'.format(self.user_name)

@dataclass
class UnlistedUser(db.Model):
    c_id: int
    user_name: str

    c_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(190), nullable=False)

    def __repr__(self):
        return '<UnlistedUser {}>'.format(self.user_name)

@dataclass
class IndexPages(db.Model):
    idpb: int
    index_name: str
    index_page: str
    icode: int

    idpb = db.Column(db.Integer, primary_key=True)
    index_name = db.Column(db.String(256), nullable=False)
    index_page = db.Column(db.String(256), nullable=False)
    icode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<IndexPages {}>'.format(self.index_name)

@dataclass
class ContestBooks(db.Model):
    id: int
    c_id: int
    idbp: int
    validator: str
    proofreader: str
    validate_time: datetime
    proofread_time: datetime
    v_revision_id: int
    p_revision_id: int


    id = db.Column(db.Integer, primary_key=True)
    c_id = db.Column(db.Integer, nullable=False)
    idbp = db.Column(db.Integer, nullable=False)
    validator = db.Column(db.String(190), nullable=False)
    proofreader = db.Column(db.String(190), nullable=False)
    validate_time = db.Column(db.DateTime, nullable=False)
    proofread_time = db.Column(db.DateTime, nullable=False)
    v_revision_id = db.Column(db.Integer, nullable=False)
    p_revision_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<ContestBooks {}>'.format(self.id)
