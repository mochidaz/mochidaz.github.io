---
layout: post
title: "Bahasa Pemrograman Rust 4: Vector dan Loop"
permalink: /Bahasa-Rust-4
lang: id
date: 2021-02-5 17:56
categories: [rust, programming]
image: /assets/images/rust-4.png
author: "mochidaz"

---

Looping merupakan sebuah logika dimana sebuah _iterator_ akan terus mengulang hingga batas yang ditentukan, atau selamanya. Loop dibagi menjadi for loop dan while loop dimana 
dalam for loop kita dapat menentukan _iterable_ untuk mengulang untuk setiap elemen dalam _iterator_ sedangkan while akan mengulang sampai kondisi terpenuhi. Vector merupakan array dinamis yang _iterable_ atau dapat kita iterasi untuk setiap elemen di dalamnya. Di bagian ke-4 ini kita akan membahas tentang cara-cara looping yang "idiomatic" dan method-methodnya. Untuk for loop tidak akan dibahas secara langsung dan hanya akan masuk ke dalam contoh-contoh disini. While loop dapat dilihat sendiri [disini](https://doc.rust-lang.org/1.2.0/book/while-loops.html).

## Vector

Seperti yang telah dijelaskan di bagian sebelumnya, vector merupakan tipe data heap yang dapat dimanipulasi. Vector memiliki banyak method berguna dan merupakan tipe yang menyimpan generic atau dapat dimasukkan tipe data apapun. Berikut adalah cara-cara untuk membuat vector:

```rust
fn main () {
   let mut vector = Vec::new();
   vector.push("Elemen index 0");
}
``` 

Diatas ini merupakan cara pertama untuk membuat vector dimana method tersebut akan membuat sebuah vector kosong yang tidak akan mengalokasi sampai sebuah atau banyak elemen 
dimasukkan kedalamnya dengan method `push()`. Keyword `mut` tentu akan dibutuhkan agar vector tersebut dapat diubah. Compiler akan menentukan tipe data sendiri dari tipe 
yang di-push ke dalam vector tersebut. Namun untuk lebih spesifiknya, disaat strong typing dibutuhkan, kita dapat dengan dua cara memberikannya tipe.

Cara pertama adalah dengan memberi variabel tersebut tipe dengan cara normal.

```rust
fn main() {
   let mut vector: Vec<i32> = Vec::new(); // Vec<i32>
   vector.push(3); // Sukses
   vector.push("Tiga"); // Error
}
```

Cara kedua adalah dengan syntax khusus Rust bernama `turbofish`.

```rust
fn main() {
   let mut vector = Vec::<i32>::new(); // Sama hasilnya dengan yang diatas (Vec<i32>)
   vector.push(3);
}
```

Kedua cara diatas dikhususkan untuk membuat vector kosong yang akan dimasukkan elemen di lain waktu. Berikut adalah contoh penggunaannya:

```rust
fn main() {
   let mut bilangan_ganjil = Vec::new();
   // Iterasi dari 1 sampai 10
   for i in 1..10 {
       // Bila i mod 2 tidak sama dengan 0 (Ganjil)
       if i % 2 != 0 {
          bilangan_ganjil.push(&i);
       }
   }
   
   // Formatting :? adalah formatting untuk struct (Dengan Debug implemented)
   // OUTPUT: [1,3,5,7,9]
   println!("{:?}", bilangan_ganjil);
}
```

Sudah paham kan penggunaannya? Digunakan ketika kita ingin memasukkan sebuah elemen yang biasanya diproses terlebih dahulu saat runtime.

Sekarang, mari kita lihat pembuatan vector yang kedua: Dengan macro `vec!`.

```rust
fn main() {
   let vector = vec![1,2,3,4,5];
   for i in vector {
   	  // OUTPUT: 12345
      print!("{:?}", i);
   }
}
```

Biasanya macro ini digunakan untuk membuat vector secara instan dengan kapasitas yang pasti. Ada beberapa cara lain yang ekuivalen untuk membuat vector dengan kapasitas pasti seperti:

```rust

fn main() {
   let mut vec = Vec::with_capacity(5);
   for i in 0..5 {
      vec.push(i);
   }
   // OUTPUT: [0, 1, 2, 3, 4]
   println!("{:?}", vec);
}

```

Dengan menggunakan kapasitas pasti, vector akan melakukan alokasi dengan lebih baik.


### Method-method berguna

Berikut adalah method-method yang akan sangat berguna dalam manipulasi vector:

#### is_empty()

Method untuk mengecek apakah sebuah vector kosong atau tidak

```rust
// OUTPUT: Vector kosong
fn main() {
   let mut vec = Vec::new();
   if vec.is_empty() {
      println!("Vector kosong");
   }
   else {
      println!("Vector tidak kosong");
   }
}
```

#### len()

Method untuk mengecek panjang index sebuah vector

```rust
// OUTPUT: Vector kosong
fn main() {
   let mut vec = vec![1,2,3,4];
   // OUTPUT: 4
   println!("{}", vec.len());
}

```

#### capacity()

Method untuk mengecek kapasitas vector

```rust
// OUTPUT: Vector kosong
fn main() {
   let mut vec: Vec<i32> = Vec::with_capacity(10);
   // OUTPUT: 10
   println!("{}", vec.capacity());
}
```

## Loop

Daripada menggunakan `while`, rust memiliki metode yang lebih baik untuk menggantikan `while true` di saat yang memang harus menggunakan loop terus-menerus seperti console application. Yaitu dengan menggunakan `loop {}`.

```rust
use std::io;
use std::io::Write;

fn main() {
   let mut input = String::new();
   loop {
      io::stdin().read_line(&mut input).unwrap();
      println!("Yang anda masukkan adalah: {}", input);
      match io::stdout().flush() {
         Ok(_) => (),
         Err(e) => println!("{}", e),
      };
   }
}
```

Kode diatas merupakan contoh program yang membaca input dan akan terus menerus meminta input dan 
kemudian mengeluarkan outputnya. Memakai `loop {}` lebih efektif dari `while true` untuk beberapa kondisi. 
Contohnya dalam kode berikut:

```rust
let x;
while true { x = 1; break; }
println!("{}", x);
```

Kode diatas akan gagal dalam mengcompile dikarenakan ada kemungkinan variabel `x` tidak diinitialisasi - rust mengharuskan semua kondisi terpenuhi. Sedangkan kode ini:

```rust
let x;
loop { x = 1; break; }
println!("{}", x);
```

Akan bekerja dengan baik dikarenakan tidak memiliki kondisi.


## Idiomatic Iterator

Dengan menggunakan method-method yang akan dijelaskan ini, mengiterasi sebuah Vector akan menjadi lebih simpel daripada menggunakan for loop. Dapat disebut juga dengan "Idiomatic" - yang berarti kode tersebut memiliki sesuatu yang unik dari bahasa yang dipakai. Mari lihat contoh penggunaannya:

```rust
fn main() {
   let mut bilangan = (1..100).collect::<Vec<i32>>();
   let mut bilangan_genap = bilangan.iter()
                            .filter(|x| *x % 2 == 0)
                            .collect::<Vec<_>>();
   println!("{:?}", bilangan_genap);
}
```

Method `iter()` pada `Vec` akan mengembalikan `Iter<'_, T>`, sebuah `trait` iterator yang sangat berguna. Kita akan dapat memanipulasi tiap elemen dalam vector tanpa perlu repot-repot membuat for loop. Berikut adalah contoh menggunakan method `iter()` bersama dengan method-method penting lainnya untuk mengambil bilangan genap, menggantikan kode `for loop` diatas. Mari bahasa method-method lainnya yang terlihat diatas. 
Method .filter() akan memfilter sejumlah elemen berdasarkan kondisi yang diberikan. Contohnya diatas sana ada `|x|`. `||` dengan sebuah variabel didalamnya merupakan closure, atau dapat kita bilang sebagai `lambda function`-nya Rust. Dia akan membuat sebuah fungsi anonim yang langsung diproses kemudian. Variabel `x` disana merupakan "parameter" dari si closure tersebut, yang kemudian diproses setelahnya secara langsung. Variabel `x` mewakili setiap elemen dalam vector `bilangan`. Elemen tersebut kemudian diproses dengan `*x % 2 == 0` yang berarti bila nilai x (setelah direferencing, karena `.iter()` mengiterasi dengan mengambil reference/meminjam elemen dalam vector) mod 2 adalah 0 (Logika sederhana bilangan genap), maka `filter` akan mengembalikan `Iterator` yang hanya berisi nilai-nilai yang telah memenuhi kondisi tadi (`*x % 2 == 0`). Yang terakhkir merupakan method `.collect()`. Method ini merupakan method yang mengumpulkan value dari `Iterator` tadi ke dalam sebuah `Vec<T>`. Method ini membutuhkan type. Maksud dari `Vec<_>` diatas adalah kita membiarkan compiler untuk menentukan tipe generic tersebut (type inference). Dapat dikatakan bahwa 
menggunakan `Vec<_>` seperti mengatakan pada compiler "Aku menggunakan generic `Vec<T>` namun tolong tentukan apa itu `T` untukku". Kadangkala `_` juga disebut dengan "type placeholder". Namun tentunya kalian juga bisa memberi tipe secara langsung ke `Vec<T>` seperti `.collect::<Vec<i32>>()` dengan turbofish, atau `let x: Vec<i32> = ... .collect()` dengan memberi tipe setelah nama variabel karena seperti yang sudah disebutkan bahwa `collect()` membutuhkan tipe.

#### map()

Menggunakan map merupakan salah satu cara untuk memanipulasi elemen di dalam sebuah vector dengan idiomatic. Seperti `filter()`, method ini juga menggunakan `closure`. Berikut adalah contoh penggunaannya:

```rust
fn main() {
   let mut vec = (1..10).collect::<Vec<i32>>();
   let mut vec_kali_3 = vec.iter().map(|x| x * 3).collect::<Vec<_>>();
   // OUTPUT: [3, 6, 9, 12, 15, 18, 21, 24, 27]
   println!("{:?}", vec_kali_3);
}
```

Method `map()` diatas akan mengalikan 3 tiap elemen dalam vector `vec` yang diwakili dengan `x`. Singkatnya, `map()` dapat dengan instan memanipulasi akan seperti apa elemen baru yang akan dimasukkan 
ke dalam sebuah vector baru. Untuk `Result<T, E>` dan `Option<T>`, dengan `map()` kita juga dapat secara langsung me-unwrap() value mereka. Kedua `enum` tersebut akan dibahas di bagian selanjutnyabersamaan dengan pattern matching menggunakan `match`. 

Terima kasih karena telah membaca sampai jumpa di bagian selanjutnya.
