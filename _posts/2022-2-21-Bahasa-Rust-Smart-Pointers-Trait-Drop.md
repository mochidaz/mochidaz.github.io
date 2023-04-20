---
title: "Bahasa Pemrograman Rust: Smart Pointers - Trait Drop"
layout: post
tags: rust programming coding
lang: id
date: 2022-2-21
permalink: /Bahasa-Rust-SP-Drop
categories: [rust, programming]
image: /assets/images/drop.png
author: "mochidaz"
---


Seperti yang telah kita ketahui, _smart pointer_ adalah sebuah tipe yang mengimplementasikan trait `Deref` dan `Drop`. Kita sudah membahas tentang `Deref` di artikel sebelumnya. Kali ini, kita akan membahas tentang `Drop`.

# Tentang `Drop`

Trait `Drop` dapat diimplementasikan pada tipe apapun, dan hampir akan selalu digunakan ketika kita mengimplementasikan sebuah _smart pointer_. Trait `Drop` adalah sebuah trait yang membuat kita dapat mengatur atau mengkustomisasi apa yang akan terjadi bila sebuah nilai keluar dari _scope_-nya (_out of scope_). Mari kita ambil `Box<T>` sebagai contoh. Implementasi kustom tentang apa yang akan terjadi ketika sebuah nilai keluar dari _scope-nya_ pada `Box<T>` adalah, ia akan mendealokasikan nilai yang ia tunjuk pada heap. 

Sekarang, mari kita gunakan _constraint_ trait `Debug` pada _smart pointer_ `Kotak<T>` kita kemarin dan semua implementasinya agar kita dapat menampilkan value `T` pada _smart pointer_ `Kotak<T>` kita.

```rust
use std::ops::Deref;

struct Kotak<T: std::fmt::Debug>(T);

impl<T> Kotak<T>
    where T: std::fmt::Debug {
    fn new(x: T) -> Self {
        Self(x)
    }
}

impl<T> Deref for Kotak<T>
    where T: std::fmt::Debug {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}
```

Lalu kita implementasikan `Drop` pada `Kotak<T>` kita.

```rust
impl<T> Drop for Kotak<T>
    where T: std::fmt::Debug {
    fn drop(&mut self) {
        println!("Dropping Kotak yang memiliki data {:?}!", self.0);
    }
}
```

Kita hanya akan menggunakan macro `println!` untuk sekarang, karena sekarang kita hanya akan berfokus pada bagaimana trait `Drop` bekerja, dan tidak pada implementasi kustom aslinya seperti mendealokasikan nilai di heap. Sekarang, mari kita lihat fungsi `main` kita.

```rust
fn main() {
	let x = Kotak::new(20);
	{
		let y = Kotak::new("Halo");
	}	
}
```

Bila kita compile lalu kita jalankan kode kita, maka kita akan menerima output seperti ini:

```
Dropping Kotak yang memiliki data "Halo"!
Dropping Kotak yang memiliki data 20!
```

Lihat, begitu variabel `Kotak<T>` kita menyentuh akhir dari _scope_, maka apa yang ada di dalam method `drop` kita akan terpanggil. Diatas, variabel `x` akan di-drop ketika ia menyentuh akhir dari _scope_ `main` sehingga fungsi `y` akan lebih dahulu di-drop. Karena itulah output `Dropping Kotak yang memiliki data "Halo"!` keluar lebih dahulu. Selalu ingat bahwa trait `Drop` ini digunakan untuk mengkustomisasi apa yang akan dilakukan ketika data kita di-drop, bukan kita harus mengimplementasikan trait `Drop` terlebih dahulu baru data kita dapat di-drop. Rust akan secara otomatis men-drop nilai yang sudah mencapai akhir _scope_.

# Early Drop

Ada kalanya kita ingin men-drop nilai kita lebih dahulu sebelum mencapai akhri _scope_, seperti saat kita menggunakan _lock_ atau _Mutex_. Rust melarang kita untuk memanggil method `drop` secara langsung dari value. Kita harus menggunakan fungsi `drop` dari `std::mem::drop`. Kita tidak perlu menggunakan `use` untuk memanggil fungsi tersebut. Seperti `Vec`, fungsi itu sudah tersedia didalam _prelude_.

```rust
fn main() {
	let x = Kotak::new(20);
	drop(x);
	{
		let y = Kotak::new("Halo");
	}	
}
```

Dan output yang akan dikeluarkan adalah:

```
Dropping Kotak yang memiliki data 20!
Dropping Kotak yang memiliki data "Halo"!
```

Variabel `x` akan di-drop terlebih dahulu.

Terima kasih telah membaca :).
