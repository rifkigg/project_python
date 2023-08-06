ulang = 'y'
while ulang == 'y':
    print("""
    ============================
        Daftar Program Mtk
    
        1. Segitiga
        2. Persegi
        3. Persegi Panjang
        4. lingkaran
    ============================
        """)
    pesan = int(input("Masukkan No : "))

    if pesan == 1:
        print("""
        =========================
            Ingin Mencari Apa?

            a. Luas
            b. Keliling
        =========================
            """)
        rumus = str(input("Masukkan huruf : "))
        if rumus == "a":
            alas = float(input("Ukuran alas : "))
            tinggi = float(input("Ukuran tinggi : "))
            luas_segitiga = (alas * tinggi)/2
            print("Luas Segitiga : ",luas_segitiga)
        else:
            sisi1 = float(input("Masukkan ukuran sisi 1 : "))
            sisi2 = float(input("Masukkan ukuran sisi 2 : "))
            sisi3 = float(input("Masukkan ukuran sisi 3 : "))
            keliling_segitiga = (sisi1 + sisi2 + sisi3)
            print(keliling_segitiga)
    elif pesan == 2:
        print("""
        =========================
            Ingin Mencari Apa?

            a. Luas
            b. Keliling
        =========================
            """)
        rumus = str(input("Masukkan huruf : "))
        if rumus == "a":
            sisi = float(input("Masukkan ukuran sisi : "))
            luas_persegi = (sisi * sisi)
            print("Luas persegi : ")
        else:
            sisi = float(input("Masukkan ukuran sisi : "))
            keliling_persegi = (sisi * 4)
            print("Keliling persegi : ",keliling_persegi)
    elif pesan == 3:
        print("""
        =========================
            Ingin Mencari Apa?

            a. Luas
            b. Keliling
        =========================
            """)
        rumus = str(input("Masukkan huruf : "))
        if rumus == "a":
            panjang = float(input("Masukkan ukuran panjang : "))
            lebar = float(input("Masukkan ukuran lebar : "))
            luas_persegi_panjang = (panjang * lebar)
            print("Luas pesegi panjang : ",luas_persegi_panjang)
        else:
            panjang = float(input("Masukkan ukuran panjang : "))
            lebar = float(input("Masukkan ukuran lebar : "))
            keliling_persegi_panjang = (panjang*lebar)*2
            print("Keliling persegi panjang : ",keliling_persegi_panjang)
    else:
        print("""
        =========================
            Ingin Mencari Apa?

            a. Luas
            b. Keliling
        =========================
            """)
        rumus = str(input("Masukkan huruf : "))
        if rumus == "a":
            r = float(input("Masukkan ukuran jari jari : "))
            luas_lingkaran = 3.14 * r**2
            print("Luas lingkaran : ",luas_lingkaran)
        else:
            d = float(input("Masukkan ukuran diameter : "))
            keliling_lingkaran = 3.14 * d 
            print("Keliling lingkaran : ",keliling_lingkaran)
    ulang = input("Ingin menghitung lagi? (y/n) : ")




