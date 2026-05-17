from flask import Flask, request, render_template
from rembg import remove
from PIL import Image
from werkzeug.utils import secure_filename # TAMBAHAN: Untuk keamanan nama file
import os
import uuid # TAMBAHAN: Untuk membuat ID unik acak

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    hasil_gambar = None
    
    if request.method == 'POST':
        if 'image' not in request.files:
            return "File tidak ditemukan"
            
        data_mentah = request.files['image']
        
        if data_mentah.filename == '':
            return "Belum memilih gambar"
            
        # 1. KEAMANAN: Bersihkan nama file dari karakter jahat/simbol aneh
        nama_asli = secure_filename(data_mentah.filename)
        
        # 2. PRIVASI: Buat kode acak unik agar file tidak saling timpa
        id_unik = uuid.uuid4().hex 
        
        # Pisahkan nama dan ekstensi (misal 'foto.jpg' jadi 'foto' dan '.jpg')
        nama_file, ekstensi = os.path.splitext(nama_asli)
        
        # Gabungkan jadi nama baru (contoh: foto_a1b2c3d4.jpg)
        nama_aman_input = f"{nama_file}_{id_unik}{ekstensi}"
        lokasi_input = os.path.join('static', nama_aman_input)
        
        # simpan file upload
        data_mentah.save(lokasi_input)
        
        # proses remove bg
        input_image = Image.open(lokasi_input)
        output = remove(input_image)
        
        # nama hasil juga dibuat unik
        nama_hasil = f'bg-remove-{id_unik}.png'
        lokasi_output = os.path.join('static', nama_hasil)
        
        # simpan hasil
        output.save(lokasi_output)
        hasil_gambar = nama_hasil
        
    return render_template('index.html', hasil_gambar=hasil_gambar)

if __name__ == '__main__':
    app.run(debug=True)