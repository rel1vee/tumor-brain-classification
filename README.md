# Klasifikasi Tumor Otak Berbasis AI 🧠

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Selamat datang di **Klasifikasi Tumor Otak Berbasis AI**, aplikasi berbasis web yang menggunakan model deep learning untuk mendeteksi jenis tumor otak dari citra MRI. Aplikasi ini dirancang untuk memberikan hasil klasifikasi yang cepat, akurat, dan informatif, dengan antarmuka yang elegan dan interaktif.

## 📋 Deskripsi Proyek

Aplikasi ini memungkinkan pengguna untuk mengunggah citra MRI (format JPEG/PNG) dan mendapatkan prediksi jenis tumor otak, seperti **Glioma**, **Meningioma**, **Pituitary Tumor**, atau **No Tumor**, beserta tingkat kepercayaan (confidence score). Hasil ditampilkan dalam kartu modern dengan progress bar visual dan informasi tambahan tentang jenis tumor yang terdeteksi.

**Fitur Utama**:
- **Antarmuka Dua Kolom**: Kolom kiri untuk unggah citra dan pemrosesan, kolom kanan untuk hasil dan informasi tambahan.
- **Progress Bar**: Visualisasi tingkat kepercayaan prediksi.
- **Informasi Tumor**: Deskripsi singkat tentang jenis tumor yang terdeteksi.
- **Desain Elegan**: Menggunakan gradien, bayangan kartu, dan efek hover untuk pengalaman pengguna yang menarik.
- **Error Handling**: Penanganan kesalahan untuk memastikan aplikasi berjalan lancar.

> **Disclaimer**: Aplikasi ini adalah alat bantu diagnosis dan tidak menggantikan penilaian medis profesional. Selalu konsultasikan hasil dengan dokter spesialis.

## 🚀 Cara Penggunaan

1. **Unggah Citra MRI**: Pilih file citra (JPEG/PNG) melalui area unggah di kolom kiri.
2. **Proses Citra**: Klik tombol "Proses Citra" untuk memulai klasifikasi.
3. **Lihat Hasil**: Hasil klasifikasi, tingkat kepercayaan, dan informasi tumor akan ditampilkan di kolom kanan.

## 📂 Struktur Folder

```
your_project_folder/
├── app.py                    # File utama aplikasi Streamlit
├── brain_tumor_model.keras   # Model deep learning untuk klasifikasi
├── requirements.txt          # Daftar dependensi Python
├── README.md                 # Dokumentasi proyek (file ini)
```

## 🛠️ Persyaratan dan Instalasi

### Prasyarat
- Python 3.8 atau lebih tinggi
- Git (untuk mengelola repository)
- Akun GitHub dan Streamlit Cloud untuk deployment

### Dependensi
Dependensi aplikasi tercantum dalam `requirements.txt`:
```
streamlit
tensorflow
pillow
numpy
```

Untuk menginstall dependensi secara lokal:
```bash
pip install -r requirements.txt
```

### Menjalankan Secara Lokal
1. Clone repository:
   ```bash
   git clone <URL_REPOSITORY_ANDA>
   cd your_project_folder
   ```
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```
4. Buka browser di `http://localhost:8501` untuk melihat aplikasi.

## 🌐 Deployment ke Streamlit Cloud

1. **Siapkan Repository GitHub**:
   - Pastikan file `app.py`, `brain_tumor_model.keras`, dan `requirements.txt` ada di direktori proyek.
   - Buat repository GitHub baru dan push file:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin <URL_REPOSITORY_ANDA>
     git push -u origin main
     ```
   - **Catatan**: Jika `brain_tumor_model.keras` >100 MB, gunakan Git LFS atau host model di cloud (lihat bagian di bawah).

2. **Deploy ke Streamlit Cloud**:
   - Login ke [Streamlit Cloud](https://share.streamlit.io/).
   - Klik "New app", pilih repository GitHub Anda, dan set `app.py` sebagai file utama.
   - Klik "Deploy" dan tunggu hingga proses selesai.

3. **Verifikasi Model**:
   - Pastikan `brain_tumor_model.keras` ada di repository dan dapat diakses oleh aplikasi.
   - Jika model tidak ditemukan, periksa nama file (case-sensitive) dan `.gitignore`.

### Menangani Model Berukuran Besar
Jika `brain_tumor_model.keras` terlalu besar untuk GitHub:
- **Gunakan Git LFS**:
  ```bash
  git lfs install
  git lfs track "*.keras"
  git add .gitattributes
  git add brain_tumor_model.keras
  git commit -m "Add model with LFS"
  git push origin main
  ```
- **Host di Cloud**: Unggah model ke Google Drive/Dropbox dengan link publik, lalu ubah kode untuk mengunduh model:
  ```python
  import urllib.request
  model_url = "https://your_storage_link/brain_tumor_model.keras"
  model_path = "brain_tumor_model.keras"
  if not os.path.exists(model_path):
      urllib.request.urlretrieve(model_url, model_path)
  ```

## ⚠️ Catatan Penting
- **Nama File Model**: Pastikan nama file di kode (`brain_tumor_model.keras`) sesuai dengan file di repository (case-sensitive).
- **Kompatibilitas TensorFlow**: Gunakan versi TensorFlow yang kompatibel dengan model Anda (disarankan TensorFlow 2.13.0).
- **Ukuran Citra**: Aplikasi hanya menerima citra JPEG/PNG. Pastikan citra yang diunggah valid.
- **Performa**: Untuk model besar, pertimbangkan konversi ke format TFLite untuk deployment yang lebih ringan.

## 📚 Kontribusi

Kami menyambut kontribusi untuk meningkatkan aplikasi ini! Silakan buat *pull request* atau laporkan *issue* di repository GitHub.

## 🙏 Kredit

- **Streamlit**: Framework untuk antarmuka web interaktif.
- **TensorFlow**: Untuk pelatihan dan inferensi model deep learning.
- **Pillow & NumPy**: Untuk pemrosesan citra dan manipulasi data.

## 📧 Kontak

Untuk pertanyaan atau dukungan, hubungi melalui [GitHub Issues](<URL_REPOSITORY_ANDA>/issues) atau email <your_email@example.com>.

---

⭐ **Jika Anda menyukai proyek ini, beri bintang di GitHub!**