from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Pengguna(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nama_pengguna = db.Column(db.String(150), unique=True, nullable=False)
    kata_sandi = db.Column(db.String(200), nullable=False)

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(150), nullable=False)
    kelas = db.Column(db.String(50), nullable=False)
    matkul = db.Column(db.String(150), nullable=False)
    NIM = db.Column(db.Integer, nullable=False)
