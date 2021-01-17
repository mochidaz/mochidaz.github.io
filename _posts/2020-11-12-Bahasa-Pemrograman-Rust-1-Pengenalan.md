---
layout: post
title: "Bahasa Pemrograman Rust 1: Perkenalan, Instalasi, dan Cargo"
categories: [cerita]
date: 2020-11-11 14:41:20
permalink: /id/Bahasa-Rust-1
---

![rust]({{ site.baseurl }}/images/rust-1.png)

### Pengenalan

Bahasa Pemrograman Rust merupakan bahasa yang diciptakan oleh Graydon Hoare pada 2014 lalu. Bahasa berkembang dengan sangat cepat. Rust merupakan bahasa yang menyediakan memory safety atau keamanan memory tanpa perlu mengalokasikannya secara manual seperti dengan malloc() pada bahasa C. Rust memiliki masa depan yang cerah sebagai sebuah bahasa pemrograman. Bahasa low level yang dapat digunakan untuk embedded system, yang menyediakan memory safety, bagaimana tidak akan populer. Beberapa perusahaan mulai menulis ulang project mereka yang awalnya ditulis dalam bahasa seperti C++ ke Rust. Firefox juga akan mengimprovisasi Gecko dengan quantum yang ditulis dalam bahasa Rust.

### Instalasi

Menginstall rust cukup mudah. Bila anda memakai Linux, anda dapat menginstall rustup dengan package manager anda.

#### Debian/Ubuntu
```
$ sudo apt install rustup
```

#### Red Hat/Fedora/OpenSUSE
```
$ sudo dnf install rustup
```

#### Arch/Manjaro
```
$ sudo pacman -S rustup
```

#### Instalasi dengan Curl
```
$ curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

#### Instalasi dalam Windows

Untuk instalasi dengan windows, anda dapat melihat instruksi disini.

<https://forge.rust-lang.org/infra/other-installation-methods.html>

#### Menginstall toolchain dan mengatur default toolchain

Rust memiliki tiga channel toolchain yaitu stable, beta, dan nightly. Fitur-fitur yang belum stabil hanya tersedia di nightly rust. Namun, untuk sekarang, kita pakai channel stable terlebih dahulu. Untuk menginstall toolchain, run perintah berikut:

```
$ rustup install stable
```

Bila anda ingin menginstall beta atau nightly toolchain, ganti stable menjadi toolchain yang anda inginkan.

Sekarang, untuk mengatur default toolchain, jalankan perintah berikut:

```
$ rustup default stable
```

Lakukan hal yang sama yaitu mengganti stable dengan channel yang anda inginkan bila anda ingin menggunakan channel lain sebagai default toolchain.

Anda akan dapat memakai cargo dan rustc setelah melakukan semua diatas.

### Cargo

Cargo adalah package manager rust sekaligus project manager. Dengan cargo, dependency yang ditulis dalam file khusus bernama Cargo.toml akan diinstall, kemudian program dicompile dan dirun. File executable akan disimpan dalam folder khusus didalamnya. Cargo sudah datang bersama rustup, rustc, dan toolchain lainnya. Bila semua sudah siap, mari kita buat project baru.

```
$ cargo new helloworld
```

Dengan command diatas, cargo akan membuat sebuah project bernama helloworld. Anda dapat mengganti nama helloworld dengan apapun sesuai nama project anda. Mari kita lihat struktur project rust.

```
├── Cargo.toml
└── src
    └── main.rs
```
  
Sebelum project di-build atau di-run, seperti inilah struktur project rust. `Cargo.toml` memuat manifest sebuah project seperti nama project, author, versi, dan edisi. `Cargo.toml` jugalah tempat kita menulis dependency project kita. Selanjutnya, `src` adalah folder untuk source file. Di dalam folder itulah kita membuat file-file yang akan kita tuliskan source code didalamnya seperti `main.rs` yang merupakan main file dimana entry point terletak. Sekarang mari lihat isi file main.rs, yang berisi hello world program secara otomatis.

```
fn main() {
    println!("Hello, world!");
}
```

Kira-kira begitulah entry point rust. Namun, kali ini akan membahas tentang cargo terlebih dahulu. Untuk pemrogramannya, akan kita bahas di post berikutnya. Baik, sekarang mari lanjutkan ke command cargo berikutnya.

Untuk build sebuah project dan menginstall dependency yang dibutuhkan secara otomatis, kita harus menjalankan sebuah command cargo, yaitu

```
$ cargo build
```

Dengan menjalankan perintah ini, maka program akan dicompile secara otomatis. Sekarang, mari kita jalankan.

Sudah menjalankan? Sekarang struktur project akan berubah menjadi seperti ini

```
├── Cargo.lock
├── Cargo.toml
├── src
│   └── main.rs
└── target
    ├── CACHEDIR.TAG
    └── debug
        ├── build
        ├── deps
        │   ├── helloworld-2b5eaaa0d7f413f8
        │   └── helloworld-2b5eaaa0d7f413f8.d
        ├── examples
        ├── helloworld
        ├── helloworld.d
        └── incremental
            └── helloworld-1wkj4tbmbf4ld
                ├── s-fszg58f8sz-1k6u8ve-1oa8bie7cqsss
                │   ├── 1dqgm8rogc77u7hp.o
                │   ├── 1lbiykn7to4xjn8o.o
                │   ├── 1xt5ymq0w7pid6v2.o
                │   ├── 2bk3804w6neb0cj4.o
                │   ├── 2dsc7rk80ct1rqsz.o
                │   ├── 32j4umd5agl7q4ck.o
                │   ├── 43kc0tbeopmdjeu9.o
                │   ├── dep-graph.bin
                │   ├── query-cache.bin
                │   ├── work-products.bin
                │   └── x8t9z996m5lb9b8.o
                └── s-fszg58f8sz-1k6u8ve.lock
```

File binary terletak dalam `target/debug/helloworld` yang dapat dijalankan dengan `target/debug/helloworld` bila posisi anda sekarang dalam root directory.

```
Hello, world!
```

Bila anda ingin langsung menjalankan program tanpa perlu menngeksekusi binary nya secara manual, jalankan lah perintah berikut

```
$ cargo run
```

Perintah ini akan menjalankan program secara langsung, setelah membuild program.

### Install Package

Untuk menginstall sebuah package, umumnya kita harus menuliskan nama package dan versinya di `Cargo.toml` dan saat proses build, cargo akan otomatis menginstallnya untuk kita. Contohnya, bila kita menggunakan package scraper pada project kita, maka kita harus menulis scraper di dependencies seperti ini:

```
[package]
name = "helloworld"
version = "0.1.0"
authors = ["Nama Author <email_author@mail.com>"]
edition = "2018"

[dependencies]
scraper = "0.12.0"

```

Bila anda tidak tahu versi berapa yang terakhir rilis, anda dapat menulisnya dengan `scraper = "*"`.

Namun, kita bisa menginstall package cargo secara manual dengan command berikut

```
$ cargo install <nama package>
```

Misalnya seperti diatas, kita ingin menginstall scraper, maka kita hanya tinggal menjalankan

```
$ cargo install scraper
```

Kira-kira untuk pengenalan dasar dari cargo sudah cukup sampai disini. Sampai jumpa di post selanjutnya!
