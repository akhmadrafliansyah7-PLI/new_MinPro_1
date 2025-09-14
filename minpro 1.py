# Nama	: Akhmad Rafliansyah
# Prodi	: Sistem Informasi
# kelas	: B
# NIM   : 2509116045
# menu utama
jadwal_matkul = []
while True:
    print("=== menu ===")
    print("-CREAT")
    print("-READ")
    print("-LOGOUT")

    pilih = input("pilih menu: ")
# menu CREAT
    if pilih == "CREAT":    
        while True:
            jawab = input("apakah anda ingin menambahkan jadwal matkul? (yes/no):")
# menambahkan jadwal matkul  
            if jawab == "yes":
                nama_matkul = input("masukan nama matkul:")
                hari = input("masukan hari:")
                jam = input("masukan jam:")
                nama_gedung = input("masukan nama gedung:")
            
                jadwal_matkul.append([nama_matkul, hari, jam, nama_gedung])

                print("data berhasil di tambahkan")

            elif jawab == "no":
                print("penambahan jadwal matkul selesai")
                break
            else:
                print("jawaban tidak valid silahkan jawab yes/no")

# menu READ          
    elif pilih == "READ":
            if not jadwal_matkul:
               print("jadwal matkul belum di tambahkan.")
# menampilkan semua jadwal matkul
            else:
                print("==daftar jadwal matkul==")
                for matkul in jadwal_matkul:
                    print("nama matkul  :", matkul[0])
                    print("hari         :", matkul[1])
                    print("jam          :", matkul[2])
                    print("nama gedung  :", matkul[3])
                    print()

    elif pilih == "LOGOUT":
        print("anda berhasil keluar. program selesai")
        break

    else:
        print("pilihan tidak valid")

