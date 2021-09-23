---
layout: post
title: "Bahasa Pemrograman Rust 6: Memahami Ownership dan Borrowing - Bagian 1"
tags: rust programming coding
lang: id
date: 2021-09-21
permalink: /id/Bahasa-Rust-6
---

![rust]({{ site.baseurl }}/images/rust-6.png)

Kali ini kita masuk ke topik yang lumayan ribet dan membingungkan bagi siapapun yang baru saja belajar Rust, entah itu seorang programmer yang berpengalaman maupun tidak. Topik ini merupakan hal yang membuat Rust unik - yang membuat Rust adalah Rust. Benar, kita akan membahas tentang Ownership, fitur terunik bahasa Rust yang menjamin keamanan memory tanpa penggunaan garbage collector. Di artikel ini, kita akan membahas tentang ownership dan borrowing, juga tipe _stack_ dan tipe _heap_.

Ownership dan Borrowing akan sangat sangat membingungkan pemula, namun sangatlah penting dan vital karena ownership merupakan fitur utama bahasa ini. Dalam bahasa lain, masalah memory dapat menyebabkan kesalahan data dan crash pada program - dan Rust, Rust menekankan keamanan memory atau _memory safety_ terlebih dahulu. Sekarang, mari kita lihat sebuah _error_ yang sangat membuat pusing para pemula dalam bahasa Rust.

```rust
fn main() {
    let x = "Ini adalah variabel".to_string();
    let y = x;
    println!("{}", x);
}
```
Dalam kode diatas, kita me-assign variabel `x` pada `y`, lalu memasukkan `x` kedalam macro `println!`. Lalu apakah yang akan terjadi? Benar, error berikut akan terjadi:
```sh
error[E0382]: borrow of moved value: `x`
 --> struct.rs:4:20
  |
2 |     let x = "Ini adalah variabel".to_string();
  |         - move occurs because `x` has type `String`, which does not implement the `Copy` trait
3 |     let y = x;
  |             - value moved here
4 |     println!("{}", x);
  |                    ^ value borrowed here after move

```
Untuk mengetahui apa yang terjadi disini, kita harus mengetahui beda dari tipe _stack_ dan _heap_.

## Tipe _stack_
Variabel _stack_ dibuat untuk pembuatan dan pengambilan memori yang cepat. Memori secara otomatis diambil kembali oleh program setelah si variabel keluar dari scope. Tipe _stack_ merupakan tipe default dalam Rust. _stack_ mencakup tipe-tipe primitif, yang memiliki ukuran yang telah ditetapkan atau _fixed size_ dimana compiler dapat mengetahui ukuran memori yang tepat pada saat _compile time_ seperti berikut:

```rust
let int: i32 = 10;
let float: f32 = 5.5;
let boolean: bool = true;
let ch: char = 'a';
```
Mengapa _string_ tidak termasuk kedalam _stack_? Karena _string_ merupakan sebuah koleksi/_collection_ dari `u8`.

Lalu mengapa dipanggil dengan "_stack_"? Ketika anda membuat variabel baru, variabel tersebut akan dialokasi diatas variabel _stack_ sebelumnya, seperti menumpuk kertas. Ketika sebuah variabel tidak dibutuhkan kembali, maka si variabel akan disingkirkan dari tumpukan tersebut jadi memory dapat diambil kembali pada penggunaan selanjutnya. Memori yang dialokasikan untuk variabel-variabel _stack_ benar-benar disamping satu sama lain sehingga itulah yang membuat _stack_ benar-benar cepat - si program tidak butuh untuk mencari dimana variabel selanjutnya harus berada dalam memori karena ia hanya menaruh/mengalokasikan si variabel _stack_ diatas variabel _stack_ sebelumnya dan membuatnya mudah diakses. Karena itulah ukuran dari _stack_ harus diketahui dan _fixed_. Variabel _stack_ tidak dapat tumbuh atau _grow_ karena tidak ada tempat di dalam _stack_ tersebut - yang ukurannya telah ditetapkan.

Lalu dimana bagian memory managementnya disini? Ini adalah tentang si kurung kurawal/_curly bracket_ yang merupakan penentu _scope_ dalam bahasa Rust. Mari kita lihat contohnya.
```rust
fn main() {
    let x = 10;
    if x == 5 {
        let y = 20;
        println!("{}", y);
    }
    println!("{}", y);
}
```
Kode diatas akan mengalami error dikarenakan oleh penggunaan variabel `y` diluar _scope_ `if` statement. Sejauh ini, konsep ini merupakan hal yang biasa di bahasa pemrograman lainnya juga. Disaat variabel yang berada di dalam _scope_ menemukan akhir dari kurung kurawal, maka "PUFF", si variabel akan hilang seperti asap dan memori akan dibebaskan dan diambil kembali. Hal ini juga berlaku pada prosedur dan fungsi, juga pada setiap segala sesuatu yang memiliki kurung kurawal.

## Tipe _heap_
Tipe _heap_ merupakan tipe yang fleksibel - ukurannya dapat berubah-ubah, memori yang dapat hidup diluar _scope_ yang membuatnya. Memori ini akan diambil kembali secara otomatis ketika _OWNER_-nya keluar dari _scope_. Tipe kompleks adalah merupakan tipe yang termasuk kedalam _heap_, contohnya _Vector_, _String_, _HashMap_, dan sebagainya. Kita juga dapat mengalokasikan tipe _stack_ pada _heap_ dengan menggunakan `Box<T>`. Berikut adalah contoh tipe data yang berada pada _heap_.
```rust
let vector: Vec<i32> = vec![10,30,20,25];
let string: String = "Aku string".to_string();
let boxed_i32: Box<i32> = Box::new(50);
```

## Perbedaan

```rust
let a = 10;
let b = a;
println!("{} {}", a, b);
```

Potongan kode diatas memuat sebuah tipe primitif yaitu `a` yang bertipe `i32` kita assign pada variabel `b`, kemudian kita _print_ menggunakan macro `println!`. Kode tersebut akan berjalan dengan baik, tanpa _error_. Sekarang, mari kita lihat contoh berikutnya - contoh yang akan menjawab _error_ di bagian paling atas.

```rust
let a = String::from("Halo");
let b = a;
println!("{} {}", a, b);
```

Kode diatas memuat sebuah tipe kompleks yaitu `a` yang bertipe `String`. Seperti pada potongan kode yang memuat `stack`, kita me-assign variabel `a` ke `b`. Segalanya terlihat sama. Namun, mengapa terjadi _error_? Nah, disini terlihat perbedaan bagaimana Rust mengatur _stack_ dan _heap_ dengan jelas. Variabel _stack_ - para tipe primitif akan di-copy, karena mengcopy variabel _stack_ itu "murah". Tipe-tipe primitif memiliki trait `Copy` yang memungkinkan itu terjadi sedangkan tipe kompleks - Rust memindahkan (_move_) _ownership_ dan tidak mengimplementasikan trait `Copy`.

## Ownership dan Borrowing

Sekarang, kalian sudah tahu kan beda dari _stack_ dan _heap_? Oke, jadi simpelnya, _ownership_ itu seperti ini:

- Data di-assign kepada sebuah variabel.
- Si variabel menjadi _owner_ atau pemilik dari data tersebut.
- Hanya dapat ada satu pemilik dalam satu waktu.
- Ketika si pemilik keluar dari _scope_, maka data tersebut akan hilang dari memori.

Sekarang, lihatlah potongan kode berikut:
```rust
let a = String::from("Halo");
let b = a;
println!("{} {}", a, b);
```
Kode diatas merupakan kode yang akan _error_, seperti yang telah kalian lihat. Lalu, bila kita ingin me-assign variabel `a` kepada variabel `b` - atau untuk variabel `b` mengambil data variabel `a`, bagaimana kita melakukannya? Ada dua cara untuk melakukannya.

Cara pertama adalah dengan menggunakan method `clone()`.
```rust
let a = String::from("Halo");
let b = a.clone();
println!("{} {}", a, b);
```
`clone()` akan membuat data baru yang sama - yang dialokasikan di _heap_ dan kemudian me-assignnya pada variabel baru, yang dalam kasus diatas, pada variabel `b`. Method `.clone()` membuat sebuah "kopi" dari si memori. Jadi, kedua variabel tersebut merupakan variabel yang benar-benar berbeda. Namun, _cloning_ relatif "mahal" pada _heap_.

Yang kedua adalah dengan "meminjam" atau "_borrow_" si _ownership_ sebagai sebuah _reference_.

```rust
let a = String::from("Halo");
let b = &a;
println!("{} {}", a, b)
```

Pada bahasa lain, dua variabel dapat menunjuk kepada memori yang sama sehingga, bila satu variabel diubah, maka variabel lain juga akan ikut terubah. Hal ini dapat mengakibatkan masalah _parallel_ dan _concurrency_ seperti _race conditions_. Masalah seperti ini bukanlah masalah bagi Rust.

Sekarang, kita akan menggali lebih dalam tentang _borrowing_.

```rust
fn main() {
  let int: i32 = 10;
  let boxed_int: Box<i32> = Box::new(10);
}
```
Diatas sini kita dapat melihat kedua variabel `int` dan `boxed_int` dimana `int` merupakan tipe primitif yang berada pada _stack_ dan `boxed_int` merupakan tipe integer yang dialokasikan pada _heap_ (_heap allocated integer_). Sekarang kita akan mencoba membuat _procedure_ sederhana.
```rust
fn main() {
  let int: i32 = 10;
  let boxed_int: Box<i32> = Box::new(10);

  stack_proc(int);
  println!("{}", int);
}

fn stack_proc(x: i32) {   
  println!("{}", x)
}
```
Diatas sini ada sebuah prosedur yang akan mem-print si variabel `int`. Kode diatas akan berjalan dengan sempurna. Kita masih akan tetap bisa menggunakan macro `println!` pada variabel `int` bahkan setelah prosedur tersebut dipanggil. Hal ini menandakan bahwa Rust akan meng-kopi si variabel `int` yang merupakan sebuah tipe primitif kepada parameter `x` pada prosedur `stack_proc` yang kemudian membuat variabel `int` dan parameter `x` menunjuk pada memori yang berbeda - tumpukan memori baru ditambahkan kepada _stack_. Hal ini dapat dibuktikan lebih jelas dengan mengubah nilai `x`.
```rust
fn main() {
  let int: i32 = 10;
  let boxed_int: Box<i32> = Box::new(10);

  stack_proc(int);
  println!("{}", int);
}

// Jangan lupa keyword mut untuk mutability
fn stack_proc(mut x: i32) {   
  x += 10;
  println!("{}", x)
}
```
Output yang dikeluarkan oleh si prosedur dan macro `println!` yang mem-print langsung variabel `int` akan berbeda - karena mereka menunjuk pada memori yang berbeda. Sekarang, kita akan melakukan hal yang sama pada tipe kompleks.

```rust
fn main() {
  let int: i32 = 10;
  let boxed_int: Box<i32> = Box::new(10);

  stack_proc(int);
  println!("{}", int);
  
  heap_proc(boxed_int);
  println!("{}", boxed_int);
}

// Jangan lupa keyword mut untuk mutability
fn stack_proc(mut x: i32) {   
  x += 10;
  println!("{}", x)
}

fn heap_proc(y: Box<i32>) {
  println!("{}", y)
}
```
Apa yang akan terjadi dengan kode diatas? Yap, seperti yang sudah kalian duga, akan terjadi error pada kode diatas. Seperti yang kalian tahu, Rust akan membersihkan memori yang telah keluar dari _scope_ dan tipe-tipe kompleks akan memindahkan _ownership_, bukan mengkopi memori. Jadi setelah variabel kompleks kalian, yang dalam kasus diatas, adalah `boxed_int` keluar dari scope prosedur `heap_proc`, memori akan dibersihkan sehingga si variabel `boxed_int` kalian tidak lagi memiliki _ownership_ kepada memori tersebut. Memori yang telah kalian pindahkan kepada parameter `y` pada prosedur `heap_proc` diatas akan lenyap seperti abu setelah menemui akhir dari _scope_ prosedur tersebut sehingga disaat variabel `boxed_int` digunakan oleh macro `println!` setelah prosedur `heap_proc` dipanggil, Rust sudah membersihkan memori `boxed_int` tersebut yang membuatnya tidak memiliki _ownership_ lagi. Tentunya seperti sebelumnya, kalian bisa menggunakan `clone()` sebelum memasukkannya ke dalam parameter. Namun, seperti yang kalian tahu, `clone()` mahal pada memori. Dan itu juga bukan merupakan solusi yang efektif. Apa yang harus kita lakukan? Benar, kita harus "meminjam" _ownership_ dari memori tersebut!

```rust
fn main() {
  let int: i32 = 10;
  let boxed_int: Box<i32> = Box::new(10);

  stack_proc(int);
  println!("{}", int);
  
  heap_proc(&boxed_int);
  println!("{}", boxed_int);
}

// Jangan lupa keyword mut untuk mutability
fn stack_proc(mut x: i32) {   
  x += 10;
  println!("{}", x)
}

fn heap_proc(y: &Box<i32>) {
  println!("{}", y)
}
```
Seperti yang kalian lihat, bila kita ingin mem- _borrow_ atau meminjam _ownership_, kita harus menggunakan tanda `&`. Bila dalam parameter, maka kita harus menggunakannya didepan tipe parameter tersebut seperti yang kalian lihat diatas, kemudian mem-pass argumen/variabel dengan tanda yang sama kedalam parameter tersebut. Kemudian semuanya akan berjalan dengan baik. Dengan _borrow_, dalam kasus diatas, si parameter `y` akan menjadi pemilik atau _owner_ dari memori yang dialokasikan. Namun, itu hanya sementara. Ketika parameter `y` menemukan akhir dari _scope_ nya, maka _ownership_ akan dikembalikan kepada pemilik aslinya yang dalam kasus diatas, variabel `boxed_i32` lalu anda bisa memakai kembali `boxed_i32` sekehendak hati anda.

Kesimpulannya adalah, tipe primitif yang dialokasikan pada _stack_ mengimplementasikan `trait` `Copy` dan akan meng-kopi variabel karena operasi biaya memori yang digunakan "murah" sedangkan tipe kompleks akan memindahkan _ownership_. Hanya bisa ada satu _owner_ dalam satu waktu.

Terima kasih banyak karena telah membaca, nantikan part selanjutnya dari pembahasan Ownership dan Borrowing yang memang topik yang agak sulit.
