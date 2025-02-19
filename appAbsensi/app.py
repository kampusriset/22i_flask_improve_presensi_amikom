from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, Pengguna, Mahasiswa

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/absensi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi ekstensi
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'masuk'  # redirect jika belum login

@login_manager.user_loader
def load_user(user_id):
    return Pengguna.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('masuk'))

# ======== Routes Autentikasi ========

@app.route('/daftar', methods=['GET', 'POST'])
def daftar():
    if request.method == 'POST':
        nama_pengguna = request.form.get('username')
        kata_sandi = request.form.get('password')
        # Cek apakah nama_pengguna sudah digunakan
        if Pengguna.query.filter_by(nama_pengguna=nama_pengguna).first():
            flash('Nama pengguna sudah digunakan', 'danger')
            return redirect(url_for('daftar'))
        hashed_password = bcrypt.generate_password_hash(kata_sandi).decode('utf-8')
        pengguna_baru = Pengguna(nama_pengguna=nama_pengguna, kata_sandi=hashed_password)
        db.session.add(pengguna_baru)
        db.session.commit()
        flash('Registrasi berhasil, silakan masuk!', 'success')
        return redirect(url_for('masuk'))
    return render_template('daftar.html')

@app.route('/masuk', methods=['GET', 'POST'])
def masuk():
    if request.method == 'POST':
        nama_pengguna = request.form.get('username')
        kata_sandi = request.form.get('password')
        pengguna = Pengguna.query.filter_by(nama_pengguna=nama_pengguna).first()
        if pengguna and bcrypt.check_password_hash(pengguna.kata_sandi, kata_sandi):
            login_user(pengguna)
            flash('Masuk berhasil', 'success')
            return redirect(url_for('beranda'))
        else:
            flash('Nama pengguna atau kata sandi salah', 'danger')
    return render_template('masuk.html')

@app.route('/keluar')
@login_required
def keluar():
    logout_user()
    flash('Anda telah keluar', 'info')
    return redirect(url_for('masuk'))

@app.route('/ganti_password', methods=['GET', 'POST'])
@login_required
def ganti_password():
    if request.method == 'POST':
        kata_sandi_sekarang = request.form.get('current_password')
        kata_sandi_baru = request.form.get('new_password')
        if bcrypt.check_password_hash(current_user.kata_sandi, kata_sandi_sekarang):
            current_user.kata_sandi = bcrypt.generate_password_hash(kata_sandi_baru).decode('utf-8')
            db.session.commit()
            flash('Kata sandi berhasil diubah', 'success')
            return redirect(url_for('beranda'))
        else:
            flash('Kata sandi saat ini salah', 'danger')
    return render_template('ganti_password.html')

# ======== Routes Beranda & CRUD Mahasiswa ========

@app.route('/beranda')
@login_required
def beranda():
    # Ambil parameter pencarian dari URL (misal: ?keyword=...)
    keyword = request.args.get('keyword', '')
    if keyword:
        # Filter data mahasiswa berdasarkan nama (case-insensitive)
        daftar_mahasiswa = Mahasiswa.query.filter(Mahasiswa.nama.ilike(f'%{keyword}%')).all()
    else:
        daftar_mahasiswa = Mahasiswa.query.all()
    return render_template('beranda.html', mahasiswa=daftar_mahasiswa, keyword=keyword)


@app.route('/mahasiswa/tambah', methods=['GET', 'POST'])
@login_required
def tambah_mahasiswa():
    if request.method == 'POST':
        nama = request.form.get('nama')
        kelas = request.form.get('kelas')
        matkul = request.form.get('matkul')
        NIM = request.form.get('NIM')
        mahasiswa_baru = Mahasiswa(nama=nama, kelas=kelas, matkul=matkul, NIM=NIM)
        db.session.add(mahasiswa_baru)
        db.session.commit()
        flash('Data mahasiswa berhasil ditambahkan', 'success')
        return redirect(url_for('beranda'))
    return render_template('tambah_mahasiswa.html')

@app.route('/mahasiswa/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_mahasiswa(id):
    mahasiswa = Mahasiswa.query.get_or_404(id)
    if request.method == 'POST':
        mahasiswa.nama = request.form.get('nama')
        mahasiswa.kelas = request.form.get('kelas')
        mahasiswa.matkul = request.form.get('matkul')
        mahasiswa.NIM = request.form.get('NIM')
        db.session.commit()
        flash('Data mahasiswa berhasil diperbarui', 'success')
        return redirect(url_for('beranda'))
    return render_template('edit_mahasiswa.html', mahasiswa=mahasiswa)

@app.route('/mahasiswa/hapus/<int:id>', methods=['GET'])
@login_required
def hapus_mahasiswa(id):
    mahasiswa = Mahasiswa.query.get_or_404(id)
    db.session.delete(mahasiswa)
    db.session.commit()
    flash('Data mahasiswa berhasil dihapus', 'success')
    return redirect(url_for('beranda'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Membuat tabel jika belum ada
    app.run(debug=True)