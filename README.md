## Mini Project DDP 1
## Tema  : Pengelolaan Jadwal Matkul Prodi Sistem Informasi Kelas B
## Nama  : Akhmad Rafliansyah
## prodi : Sistem Informasi
## kelas : B
## NIM   : 2509116045


![Flowchart](flowchart_minpro_new.png)

**Penjelasan Flowchart:**
1. Program dimulai dari **START**
2. User akan melihat beberapa menu pilihan yaitu **CREAT**, **READ**, **LOGOUT**.
3. User akan memilih 1 dari 4 pilihan
4. Jika user memilih **CREAT** maka akan ada 2 pilihan yaitu ingin menambahkan data baru atau tidak. jika user memilih tidak maka user akan langsung menuju menu utama lagi. jika user memilih ingin menambahkan data baru maka user harus menginput **nama matkul, hari, jam, dan nama gedung**. setelah itu sistem akan menyimpan data ke dalam daftar dan akan mendapatkan pesan yaitu **"data berhasil di tambahkan"**. alur berlanjut user akan mendapatkan dua pilihan lagi yaitu ingin menambahkan data lagi atau tidak. jika user memilih ingin menambahkan data lagi maka user akan kembali menginput data. jika user memilih tidak maka akan mendapatkan pesan **"penambahan data jadwal matkul selesai"**. selanjutnya user kembali menuju menu utama.
5. jika user memilih **READ** maka akan ada pertanyaan **"apakah user telah menambahkan data jadwal matkul kedalam daftar?"**. jika user belum menambahkan data jadwal matkul maka user akan mendapatkan pesan **"jadwal matkul belum ditambahkan"** dan user akan langsung menuju menu utama. jika user sudah menambahkan data jadwal matkul maka sistem akan menampilkan daftar jadwal matkul yang sudah di tambahkan. selanjutnya user akan kembali menuju menu utama.
6. jika user memilih **LOGOUT** maka user akan mendapatkan pesan **"anda berhasil keluar, program selesai"** dan program akan langsung berhenti/**END**.

**penjelasan output pada terminal program pytho dengan memperlihatkan semua kondisi:**

1.**Kondisi pertama**

![Output](Screenshot%20(32).png)

Kondisi pertama ini adalah bagian menu utama yang memiliki tiga pilihan yaitu **CREAT**, **READ**, **LOGOUT**. user bisa memilih salah satu dari ketiga pilihan

2.**kondisi kedua**
   
![Output](Screenshot%20(33).png)

Di kondisi kedua, user memilih **CREAT** pada bagian pilih menu maka akan menampilkan pertanyaan **"apakah anda ingin menambahkan jadwal matkul? (yes/no)"**. di kondisi ini user memberikan jawaban **yes** maka user akan menambahkan data jadwal matkul berupa **nama matkul, hari, jam, dan nama gedung lalu jika sudah user akan mendapatkan pesan yaitu **"data berhasil di tambahkan"**.

3.**Kondisi ketiga**

![Output](Screenshot%20(34).png)

Di kondisi ketiga ini, ini merupakan jawaban kedua dari kondisi kedua ketika user tidak memilih **yes** tetapi memilih **no** maka user akan mendapatkan pesan yaitu **"penambahan jadwal matkul selesai"** yang artinya menu **CREAT** berakhir dan user di arahkan ke menu pilihan utama lagi.

4.**kondisi keempat**

![Output](Screenshot%20(36).png)

Di kondisi keempat, ketika user memilih **CREAT** dan muncul pertanyaan **"apakah anda ingin menambahkan jadwal matkul? (yes/no)"** tetapi mengosongkan/menjawab selain yes/no. dalam gambar user mengisi jawaban kosong maka user akan mendapatkan pesan yaitu **"jawaban tidak valid silahkan silahkan isi yes/no"** dan akan langsung di suruh mengisi jawaban yaitu yes/no. kondisi ini juga berlaku ketika user mengisi selain yes/no.

5.**kondisi kelima**

![Output](Screenshot%20(35).png)

Di kondisi kelima, user memilih **READ** di salah satu pilihan yang ada di menu utama. terlihat ketika user memilih **READ** maka akan menampilkan data jadwal matkul. kondisi ini berlaku jika user sebelumnya sudah membuat atau menambahkan data jadwal matkul.

6.**kondisi keenam**

![Output](Screenshot%20(37).png)

Di kondisi keenam, user memilih **READ** di salah satu pilihan yang ada di menu utama. terlihat ketika user memilih **READ** user mendapatkan pesan yaitu **"jadwal matkul belum di tambahkan**. ini terjadi karena user sebelumnya belum membuat atau menambahkan data jadwal matkul.

7.**kondisi ketujuh**

![Output](Screenshot%20(38).png)

Di kondisi ketujuh, user memilih **LOGOUT** di salah satu pilihan yang ada di menu. terlihat ketika user memilih **LOGOUT** user mendapatkan pesan yaitu **"anda berhasil keluar, progam selesai**. ini meruapakan kondisi ketika user ingin keluar atau mengakhiri sebuah program. ketika user memilih **LOGOUT** maka otomatis program berhenti atau selesai.

8.**kondisi kedelapan**

![Output](Screenshot%20(39).png)

Di kondisi ke delapan, dalam gambar user mengosongkan jawaban maka user mendapatkan pesan **"pilihan tidak valid"** dan user di suruh untuk memilih salah satu dari tiga pilihan menu utama. kondisi ini juga berlaku ketika user mengisi bukan dari salah satu dari 3 pilihan menu utama.






   
   
