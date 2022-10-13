---
layout: post
title: "Bahasa Rust 5: Result, Option, dan Pattern Matching"
permalink: /Bahasa-Rust-5 
lang: id
date: 2021-02-26 00:54
categories: [rust, programming]
image: /assets/images/rust-5.png
author: "mochidaz"

---


Error handling merupakan salah satu logika penting dalam pemrograman. Error handling merupakan cara untuk memproses suatu logika disaat logika yang lainnya mengalami `error` atau kegagalan. Error handling dapat juga disebut dengan `exception handling`. 
Umumnya, bahasa pemrograman lain memakai sebuah logika bernama `try-catch` untuk melakukan exception handling dimana `try` mencoba untuk menjalankan suatu logika yang berpotensi untuk error, dan `catch` merupakan logika yang menangkap error tersebut, lalu menjalankan logika lainnya bila error yang ditangkap sesuai. 
Rust tidak menggunakan `try-catch`. Rust menggunakan sebuah `enum` bernama `Result<T, E>` dimana T merupakan generic untuk tipe data yang akan di-`wrap` dalam bentuk `Ok(T)` dan E merupakan generic untuk tipe data bentuk error yang akan di-`wrap` dalam bentuk `Err(E)`. Yang kedua adalah `null`. 
Bahasa pemrograman lain umumnya memiliki `null` atau nilai kosong yang benar-benar kosong (Bukan 0, karena 0 merupakan integer). Namun `null reference` dianggap sebagai sesuatu yang buruk dalam Computer Science. Oleh karena itu, Rust tidak memiliki `null`, melainkan sebuah `enum` bernama `Option`. `enum` ini digunakan untuk sesuatu yang memiliki kemungkinan tidak ada atau `None`. 
`enum` ini akan mengembalikan `Some(value)` atau `None`.

Ingat bahwa `T` yang sudah kalian lihat diatas dan akan kalian terus lihat dibawah sini berarti "Type" atau tipe. Biasanya, `T` sangat umum dipakai sebagai perwakilan tipe data generic dimana kita dapat memasukkan apapun kedalam sana. Jangan bingung dengan `T` dibawah. Bila anda melihat sesuatu semacam `Ok(T)`, maka itu berarti didalam `Ok()` kita dapat memasukkan value apapun, dan hanya merupakan sebuah perwakilan dari tipe sebelum kita memasukkan apapun kesana. Mirip seperti variabel pada aljabar (2x + 3y dan semacamnya) sedangkan `E` merupakan perwakilan untuk tipe error.

Omong-omong, perlu diingat bahwa Pattern Matching yang akan dibahas disini merupakan pattern matching dasar untuk menghandle kedua `enum` ini. Detailnya akan dibahas di lain waktu.

## Result<T, E>

Yang pertama adalah `Result<T, E>`. Untuk yang baru saja belajar bahasa Rust, tentu akan kebingungan tentang bagaimana cara melakukan `error handling` di bahasa ini. Jawabannya adalah dengan `enum` berikut. `Result<T, E>` akan mengembalikan success value atau nilai bila sukses dan tidak terjadi error dalam `Ok(T)` dan mengembalikan failure atau kegagalan dalam bentuk `Err(E)`. Dikarenakan mereka merupakan `enum`, kita dapat menggunakan `pattern matching` untuk me-handle error yang dikembalikan:

```rust
use std::fs;
use std::io::{self, prelude::*};

fn main() {
    // Isi dari tes.txt: Halo
    let file = fs::File::open("tes.txt");
    let mut content = String::new();

    let mut file = match file {
       Ok(f) => f,
       Err(e) => panic!("Error terjadi: {}", e)
    };
    file.read_to_string(&mut content);
    
    println!("{}", content);
}
```

Kode diatas merupakan kode untuk membuka dan membaca sebuah file bernama `tes.txt`. Bila file tersebut ada dan dapat dibuka, maka pattern matching diatas, yaitu `match file` akan mengembalikan file tersebut. Karena `std::fs::File::open` mengembalikan sebuah Result, maka pattern matching yang tersedia adalah antara `Ok(T)` atau `Err(E)`. Bila pattern yang ditemukan merupakan `Ok(f)` dimana `f` merupakan nama variabel `T` yang dapat kita ganti dengan apapun, maka kembalikan value yang diwrap didalam `Ok(T)` tersebut, yaitu `f` itu sendiri: `Ok(f) => f`. Sedangkan yang kedua, bila pattern yang ditemukan merupakan `Err(e)` dimana sama seperti `f`, `e` merupakan nama variabel pengganti `E`, maka print errornya dengan macro `panic!` dan `e` merupakan pesan errornya. Selanjutnya adalah `file.read_to_string(&mut content)` yang merupakan sebuah method dari `std::fs::File` dimana dia akan secara langsung memanipulasi `String` yang mutable dengan mengonversi dan mengappend hasil bacaan file dari `std::fs::File` ke sebuah `&mut String` atau mutable string.

Cara diatas bisa dibilang lumayan ribet. Dengan menaruh return type `std::io::Result<T>`, maka kode diatas akan lebih pendek. Apa bedanya `Result<T, E>` dan `std::io::Result<T>`? Mereka sama. `std::io::Result<T>` merupakan sebuah `Result<T, E>` yang telah diganti bentuk typenya menjadi `Result<T, Error>` dari library `fs` itu dengan keyword `type`. Error yang dikembalikan merupakan `std::io::Error`, error khusus dari library `io` itu sendiri, untuk error yang terjadi pada proses Input/Output. Begini kira-kira implementasinya:

```rust
use std::fs;
use std::io::{self, prelude::*};

fn main() -> io::Result<()> {
    // Isi dari tes.txt: Halo
    let mut file = fs::File::open("tes.txt")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    println!("{}", content);
    Ok(())
}
```
Dengan menggunakan operator `?`, maka error handling akan semakin lebih mudah dan kode kita terlihat lebih rapi. Namun perlu diingat bahwa operator `?` hanya berlaku untuk fungsi yang mengembalikan `Result`. Lalu, Ok(T) atau Err(E) dibutuhkan sebagai ekspresi untuk pengembalian pada sebuah fungsi yang mengembalikan `Result`. `Ok(())` dibawah adalah untuk mewrap `void`, atau tidak ada value didalam sebuah `Ok(T)`. Pengembalian harus sesuai dengan jenis `T` yang akan dikembalikan dan didefinisikan didalam `Result` pada return type. Seperti yang diatas, karena fungsi diatas mengembalikan `Result<()>` dimana `()` merupakan `empty tuple` yang tidak mengembalikan value apapun, maka kita harus mewrap `empty tuple` juga didalam `Ok(T)`. Rust juga memiliki cara lain untuk error handling seperti dengan menggunakan `expect()`. Method ini akan mengeluarkan pesan yang kita tulis didalam parameternya bila terjadi sebuah error dan tanpa perlu menggunakan return type `enum Result`.

```rust
use std::fs;
use std::io::{self, prelude::*};

fn main() {
    // Isi dari tes.txt: Halo
    let mut file = fs::File::open("tes.txt").expect("Tidak bisa membuka file");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Tidak bisa membaca file");
    println!("{}", content);
}
```

Simpel sekali bukan? Sekarang, kita akan membahas method `unwrap()`.

Method `unwrap()` merupakan sebuah method yang akan mengabaikan error atau sukses dan langsung mengambil value apapun yang diwrap didalam sebuah `Ok(T)` atau `Some(T)` (bagian dari `Option<T>`, akan dibahas nanti).

```rust
use std::fs;
use std::io::{self, prelude::*};

fn read_file(filename: &str) -> io::Result<String> {
    let mut file = fs::File::open(filename)?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn main() {
    // Isi dari tes.txt: Halo
    let content = read_file("tes.txt").unwrap();
    // OUTPUT: Halo
    println!("{}", content);
}
```

Kode diatas adalah contoh penggunaan dari `unwrap()` yaitu disaat kita ingin mengambil value dari "wrapper" sebuah enum. Bila kita tidak menggunakan `unwrap()` pada kode diatas, maka kita harus menggunakan formatting khusus untuk `println!()` yang berupa `{:?}` dan kemudian hasil yang akan dikeluarkan adalah `Ok("Halo\n")` dikarenakan isi file masih diwrap dalam `Ok(T)`.

## Early Return

Early return merupakan sebuah kondisi dimana kita menggunakan keyword `return` untuk mengembalikan suatu value sebelum seluruh kode dalam fungsi tersebut diproses. Biasanya early return digabungkan dengan pattern matching untuk mengembalikan sebuah `Err(E)` di sebuah fungsi yang memiliki return type `Result<T, E>`.
```rust
use std::fs;
use std::io::{self, prelude::*};

fn read_file(filename: &str) -> io::Result<String> {
    let file = fs::File::open(filename);
    let mut content = String::new();

    let mut file = match file {
	Ok(f) => f,
	Err(e) => return Err(e)
    };
    file.read_to_string(&mut content)?;
    
    Ok(content)
}

fn main() {
    // Isi dari tes.txt: Halo
    let content = read_file("tes.txt").unwrap();
    println!("{}", content);
}
``` 

Kode diatas akan langsung mengembalikan `Err(E)` bila ada masalah dengan file `tes.txt`dan program akan terhenti ketika kita mencapai `unwrap()`. Kita juga dapat me-handlenya lagi dengan pattern matching seperti berikut:

```rust
use std::fs;
use std::io::{self, prelude::*};

fn read_file(filename: &str) -> io::Result<String> {
    let file = fs::File::open(filename);
    let mut content = String::new();

    let mut file = match file {
	Ok(f) => f,
	Err(e) => return Err(e)
    };
    file.read_to_string(&mut content)?;
    
    Ok(content)
}

fn main() {
    // Isi dari tes.txt: Halo
    let content = read_file("tes.txt");
    match content {
        Ok(f) => println!("Success! Content: {}", f),
        Err(e) => println!("Failed! Error: {}", e)
    }
}
```

Kode diatas akan mengeluarkan output "Success! Content: \<Konten File>" bila berhasil dan "Failed! Error: \<Jenis Error>" bila gagal.

## `Option<T>`

Yang kedua adalah `Option<T>`. Enum ini merupakan `enum` yang sangat berguna bila ada dua kemungkinan kondisi dimana dalam satu kondisi value berhasil ditemukan dan dalam kondisi lain value tidak ada (None). Untuk lebih jelasnya, mari kita bahas lewat contoh.

```rust
fn count_word(sentence: String, word: &str) -> Option<i32> {
    let mut count = 0;
    let vec = sentence.split(" ").map(|s| s.to_string()).collect::<Vec<String>>();

    for i in vec {
        if i == word {
            count += 1;
        }
    }
    if count == 0 {
        None
    }
    else {
        Some(count)
    }
}

fn main() {
    let sentence = String::from("Aku sedang coding bahasa Rust dan bahasa Rust ini sangat keren");
    let count = count_word(sentence, "Rust");
    match count {
        None => println!("Tidak ditemukan kata tersebut di kalimat tersebut"),
        Some(value) => println!("Ditemukan {} kata tersebut di kalimat tersebut", value)
    };
}
```

Kode diatas dapat menghitung ada berapa kata spesifik di dalam sebuah kalimat. Bila tidak ditemukan, maka kita akan mengembalikan `None`. Bila ditemukan, maka `Some(count)` dimana count adalah hasil penghitungan jumlah kata di dalam kalimat tersebutlah yang akan dikembalikan. Sama seperti `Ok(T)`, `Some(T)` mewrap value. Kita dapat mengambil value tersebut dengan pattern matching seperti diatas maupun method `unwrap()`. Kita juga dapat mengatur default value dengan `unwrap_or(T)` dimana bila `None` ditemukan, maka value secara otomatis akan berubah menjadi si T yang kita berikan. Contoh:

```rust
fn default_example(opt: Option<&str>) {
    println!("{}", opt.unwrap_or("Ini adalah value default"));
}

fn main() {
    default_example(Some("Test"));
    default_example(None);
}
```

Pada baris pertama fungsi `main()`, `default_example()` akan mengeluarkan output "Test" dikarenakan `Option<&str>` pada parameter `default_example()` memiliki value. Sedangkan pada baris kedua, yaitu `default_example(None)`, output yang akan dikeluarkan adalah "Ini adalah value default" dikarenakan `Option<&str>` pada parameter fungsi itu mengembalikan `None` dan tidak memiliki value sehingga `unwrap_or(T)` secara otomatis akan mengambil value yang dipass pada parameternya sebagai argumen dan untuk kasus disini, itu adalah "Ini adalah value default".

Terima kasih telah membaca, nantikan artikel selanjutnya.

Bila anda melihat sebuah kesalahan atau typo atau kata-kata yang agak kurang jelas, boleh kontak saya di email rahmanhakim2435@pm.me atau dm Instagram rahmanhakim2435_. Begitu juga bila anda ingin bertanya, jangan ragu untuk mengirim pesan pada email atau dm Instagram!
