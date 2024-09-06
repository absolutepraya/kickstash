# KickStash

URL to deployed app via PWS:
(Soon)

## Pertanyaan dan Jawaban

1. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

    ***Jawab***:
    *(belum dijawab)*

2. Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

    ***Jawab***:  
    *(belum dijawab)*

3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak!

    ***Jawab***:  
    Beberapa fungsi `git` yang paling penting dalam pengembangan perangkat lunak adalah sebagai berikut.
    - **Version Control**:  
    Git mencatat setiap perubahan pada kode, memungkinkan developer untuk melihat riwayat pengeditan, siapa yang mengubah apa, dan kapan perubahan tersebut dilakukan.
    - **Collaboration**:  
    Git memfasilitasi kolaborasi tim dengan memungkinkan banyak developer bekerja pada proyek yang sama tanpa mengganggu pekerjaan satu sama lain. Ini dilakukan dengan menggunakan `branching` dan `merging`.
    - **Backup**:  
    Git memungkinkan developer untuk kembali ke versi sebelumnya dari kode jika terjadi kesalahan, dengan memanfaatkan fitur seperti `commit`, `reset`, dan `checkout`.
    - **Code Review**:  
    Git memungkinkan developer untuk melakukan *code review* dengan mudah, memungkinkan mereka untuk memberikan masukan dan saran kepada rekan tim mereka.
    - **Deployment**:  
    Git memungkinkan developer untuk melakukan *deployment* kode ke server produksi dengan mudah, dengan memanfaatkan fitur seperti `push` dan `pull`.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    ***Jawab***:  
    Ada beberapa alasan yang mungkin mendasarinya, di antaranya:
    - **Struktur**:  
    Django mengikuti pola MVT (Model-View-Template) yang membantu pemula memahami pentingnya arsitektur yang terstruktur dalam pengembangan aplikasi web.
    - **Fitur Bawaan**:  
    Django dilengkapi dengan banyak fitur bawaan, seperti autentikasi, pengelolaan database, dan manajemen admin, sehingga pemula dapat fokus pada belajar konsep dasar.
    - **Keamanan**:  
    Django memiliki mekanisme keamanan bawaan seperti perlindungan terhadap CSRF, SQL injection, dan XSS.
    - **Skalabilitas**:  
    Django dirancang untuk menangani aplikasi web yang kompleks dan besar, sehingga pemula dapat mempelajari cara mengelola aplikasi yang berkembang.
    - **ORM Bawaan**:  
    Django menyediakan *ORM* bawaan yang memungkinkan developer untuk berinteraksi dengan database tanpa menulis SQL mentah.

5. Mengapa model pada Django disebut sebagai *ORM*?

    ***Jawab***:  
    Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena mereka menghubungkan struktur objek dalam kode Python dengan tabel-tabel dalam database relasional. Dengan menggunakan model Django, developer dapat berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis SQL mentah.

## Checklist Tugas

* [X] Membuat sebuah proyek Django baru.
* [X] Membuat aplikasi dengan nama `main` pada proyek tersebut.
* [X] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
* [X] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
  * `name`
  * `price`
  * `description`
* [X] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
* [X] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
* [X] Melakukan *deployment* ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
* [X] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di- *deploy* , serta jawaban dari beberapa pertanyaan berikut.
  * Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
  * Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
  * Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
  * Menurut Anda, dari semua framework yang ada, mengapa framework
    Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  * Mengapa model pada Django disebut sebagai *ORM*?
