---
title: "Menulis dan Membaca Format File Binary Custom"
layout: post
tags: c++ programming coding
lang: id
date: 2024-6-27
permalink: /Custom-Binary-Format
categories: [rust, programming]
image: /assets/images/binary-file.png
author: "mochidaz"
---

Apakah kalian pernah bertanya-tanya, bagaimana format file dibedakan satu dengan yang lain? Apa sih isi dari suatu file sebenarnya? Lalu apakah bisa kita membuat format file sendiri? Di artikel ini, kita akan membahas cara untuk menulis format file milik kita sendiri.

## Apa itu File Binary?

Sebelum kita membuat file binary, tentunya kita harus tahu terlebih dahulu apa itu file binary. File binary adalah file mentah yang berisi data dalam bentuk biner, yaitu data yang direpresentasikan dalam bentuk angka-angka biner. File binary biasanya digunakan untuk menyimpan data yang tidak bisa dibaca oleh manusia, seperti data gambar, data audio, dan sebagainya.

File binary bisa berisi data dalam berbagai format, seperti format BMP untuk gambar, format WAV untuk audio, dan sebagainya. Setiap format file binary memiliki struktur data yang berbeda-beda, tergantung pada jenis data yang disimpan di dalamnya.

## Bagaimana File/File Binary Dibaca?

File pada dasarnya adalah kumpulan data yang tersimpan dalam media penyimpanan. Membaca file melibatkan interpretasi data yang terkandung di dalamnya, yang bisa berupa teks, gambar, audio, video, dan lainnya. Proses ini dimulai dengan memeriksa header file, yang menyediakan informasi penting seperti tipe file, ukuran, dan atribut lainnya yang diperlukan untuk menguraikan isi file.

Khusus untuk file binary, pembacaannya dilakukan dengan membaca byte-byte yang ada dalam file tersebut. Setiap byte diinterpretasikan sesuai dengan format data yang diinginkan. Misalnya, untuk membaca file gambar BMP, kita perlu memahami struktur byte sebagai bagian dari header file BMP, data gambar, dan sebagainya. Karena itulah, implementasi struktur data pada file bisa berbeda antara aplikasi, sehingga satu aplikasi bisa berhasil membaca suatu file dengan benar sementara yang lain membaca file tersebut dengan lebih "aneh", atau bahkan sama sekali tidak bisa membacanya.

Kadangkala, suatu aplikasi juga memiliki file khusus miliknya sendiri, yang berisi data dalam format tertentu yang hanya bisa dibaca oleh aplikasi tersebut. Contohnya adalah file Adobe Photoshop PSD, yang berisi data gambar dalam format khusus yang hanya bisa dibaca oleh Adobe Photoshop. Dalam kasus ini, hanya Adobe Photoshop yang bisa membaca dan menulis file PSD tersebut, karena logika pembacaan dan penulisan file PSD hanya dimiliki oleh Adobe Photoshop.

## Mengapa Dalam Bentuk Binary?

Ada beberapa alasan mengapa kita menggunakan format file binary. Pertama, file binary lebih efisien dalam hal ukuran dan performa. Yang kedua, bila kita tidak ingin file kita diubah atau dibaca oleh orang lain, file binary adalah pilihan yang baik karena tidak bisa dibaca oleh manusia. Bila seseorang ingin membaca file binary kita, mereka harus tahu struktur data file kita seperti apa, dan bagaimana cara membacanya.

## Membuat Format File Sendiri

Untuk membuat format file sendiri, kita perlu menentukan format data yang akan disimpan di dalam file tersebut. Format data ini bisa berupa header file, data, dan sebagainya. Setelah kita menentukan format data, kita bisa menulis program yang akan menulis data ke dalam file tersebut sesuai dengan format yang telah ditentukan.

Sekarang, kita akan menggunakan bahasa pemrograman C++ untuk membuat format file binary sederhana. Kita akan membuat format file yang berisi sebuah data integer dan sebuah data string. Berikut adalah struktur direktori dari proyek kita:

```
.
├── src/
│   ├── format.cpp
│   ├── format.h
│   └── main.cpp
└── CMakeLists.txt
```

Isi dari file `CMakeLists.txt` adalah sebagai berikut:

```cmake
cmake_minimum_required(VERSION 3.10)

project(custom_bin_format)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(custom_bin_format
        src/main.cpp
        src/format.cpp
        src/format.h
)
```

Pertama-tama, dalam file `format.h`, kita akan mendefinisikan struktur data yang akan disimpan di dalam file tersebut. Simpel saja, kita akan menaruh data integer di `data1` dan data string di `data2`. Berikut adalah isi dari file `format.h`:

```cpp
#include <string>
#include <vector>

struct MyFormat {
    int data1;
    std::string data2;

    std::string to_string() const;
};

void write_to_file(const std::string &file_name, std::vector<MyFormat> &data);

std::vector<MyFormat> read_from_file(const std::string &file_name);
```

Disini kita mendefinisikan struktur data `MyFormat` yang berisi dua data, yaitu `data1` bertipe `int` dan `data2` bertipe `std::string`. Kita juga mendefinisikan dua fungsi, yaitu `write_to_file` untuk menulis data ke dalam file, dan `read_from_file` untuk membaca data dari file. Fungsi `to_string` digunakan untuk representasi `MyFormat` dalam bentuk string.

Selanjutnya, kita akan menulis implementasi dari struktur data dan fungsi-fungsi tersebut di dalam file `format.cpp`. Pertama-tama, kita implementasikan fungsi `to_string` dan `write_to_file`.

```cpp
#include <fstream>
#include <vector>

#include "format.h"

std::string MyFormat::to_string() const {
    return std::to_string(data1) + " " + data2;
}

void write_to_file(const std::string &file_name, std::vector<MyFormat> &data) {
    std::ofstream file(file_name, std::ios::binary);
    for (const MyFormat &format : data) {
        file.write(reinterpret_cast<const char *>(&format.data1), sizeof(format.data1));
        size_t size = format.data2.size();
        file.write(reinterpret_cast<const char *>(&size), sizeof(size));
        file.write(format.data2.c_str(), size);
    }
}
```

Disini, kita melakukan `serialization` terhadap data `MyFormat` ke dalam bentuk bytes. Untuk mengubah sebuah tipe data ke dalam bentuk bytes, kita dapat menggunakan `reinterpret_cast`. Seperti biasa, kita membuka file terlebih dahulu dengan `std::ofstream`. Namun, kali ini kita menggunakan mode `std::ios::binary` untuk membuka file dalam mode binary. Setelah itu, kita menulis data integer `data1` ke dalam file. Selanjutnya, kita menulis ukuran string `data2` ke dalam file. Terakhir, kita menulis string `data2` ke dalam file.

Mengapa kita perlu menulis ukuran string `data2` ke dalam file? Karena kita perlu mengetahui berapa panjang string `data2` ketika kita membaca file tersebut. Dengan menulis ukuran string `data2` ke dalam file, kita bisa mengetahui berapa panjang string `data2` ketika kita melakukan `deserialization` atau membaca file tersebut.

Selanjutnya, kita akan menulis implementasi fungsi `read_from_file` di dalam file `format.cpp`.

```cpp
std::vector<MyFormat> read_from_file(const std::string &file_name) {
    std::ifstream file(file_name, std::ios::binary);
    std::vector<MyFormat> result;
    while (true) {
        MyFormat format;
        file.read(reinterpret_cast<char *>(&format.data1), sizeof(format.data1));
        if (file.eof()) {
            break;
        }
        size_t size;
        file.read(reinterpret_cast<char *>(&size), sizeof(size));
        format.data2.resize(size);
        file.read(&format.data2[0], size);
        result.push_back(format);
    }

    return result;
}
```

Disini, kita melakukan `deserialization` terhadap data `MyFormat` dari file. Kita membuka file dengan mode `std::ios::binary` menggunakan `std::ifstream`. Selanjutnya, kita membaca data integer `data1` dari file. Kita menggunakan `file.eof()` untuk mengecek apakah kita sudah mencapai akhir file atau belum. Jika kita sudah mencapai akhir file, kita keluar dari loop. Selanjutnya, kita membaca ukuran string `data2` dari file. Kita alokasikan memori untuk string `data2` menggunakan `resize`. Terakhir, kita membaca string `data2` dari file dan memasukkannya ke dalam `vector` `result`.

Setelah kita menulis implementasi fungsi-fungsi tersebut, kita bisa menggunakan fungsi-fungsi tersebut di dalam file `main.cpp`.

```cpp
#include "format.h"
#include <iostream>

int main() {
    std::vector<MyFormat> data = {
        {1, "<Oh Yeah!>"},
        {2, "<Very good!>"},
        {3, "Furudo Erika is the best detective!"},
    };

    write_to_file("data.dat", data);
    // kode selanjutnya
```

Potongan kode di atas adalah bagaimana kita bisa menulis data ke dalam file dengan format binary yang kita buat sendiri. Kita membuat sebuah `vector` `data` yang berisi tiga data `MyFormat`. Setelah itu, kita menulis data tersebut ke dalam file `data.dat` menggunakan fungsi `write_to_file`.

Sekarang, karena kita sudah menulis data ke dalam file, kita bisa membaca data tersebut dari file. Berikut adalah potongan kode yang menunjukkan bagaimana kita bisa membaca data dari file.

```cpp
    // kode sebelumnya
    std::vector<MyFormat> read_data = read_from_file("data.dat");

    for (const MyFormat &format : read_data) {
        std::cout << format.to_string() << std::endl;
    }

    return 0;
}
```

Kode di atas akan membaca data dari file `data.dat` yang telah kita tulis sebelumnya. Kita menggunakan fungsi `read_from_file` untuk membaca data dari file tersebut. Setelah itu, kita menampilkan data yang telah kita baca ke layar.

Ini adalah kode lengkap dari `main.cpp`:

```cpp
#include "format.h"
#include <iostream>

int main() {
    std::vector<MyFormat> data = {
        {1, "<Oh Yeah!>"},
        {2, "<Very good!>"},
        {3, "Furudo Erika is the best detective!"},
    };

    write_to_file("data.dat", data);

    std::vector<MyFormat> read_data = read_from_file("data.dat");

    for (const MyFormat &format : read_data) {
        std::cout << format.to_string() << std::endl;
    }

    return 0;
}
```

Sekarang, kita akan compile dan run program kita. Pertama-tama, lakukan konfigurasi CMake dengan command berikut:

```bash
cmake -S . -B build/
```

Setelah itu, compile program kita dengan command berikut:

```bash
cmake --build build/
```

Terakhir, run program kita dengan command berikut:

```bash
./build/custom_bin_format
```

Dan kita akan mendapatkan output berikut:

```
1 <Oh Yeah!>
2 <Very good!>
3 Furudo Erika is the best detective!
```

Menulis dan membaca file dengan format binary sendiri sukses! Sekarang, cobalah untuk membuat format file binary yang lebih kompleks dan coba implementasikan sendiri. Selamat mencoba!