---
layout: post
title: "Bahasa Pemrograman Rust 8: Enumerasi"
permalink: /Bahasa-Rust-8
lang: id
date: 2022-01-16 01:00
categories: [rust, programming]
image: /assets/images/rust-8.png
author: "mochidaz"

---


Kita sudah pernah membahas tentang enum di [Bab Result, Option, dan Pattern Matching](https://mochidaz.github.io/id/Bahasa-Rust-5). Namun, kita belum membahasnya lebih dalam lagi. Artikel kali ini akan lebih pendek dari artikel-artikel sebelumnya, namun sangatlah berguna. Artikel kali ini akan menyambung dengan artikel selanjutnya yaitu tentang generics. Karena itu, bacalah artikel ini dengan baik!

Enum merupakan fitur yang sangat berguna pada Rust. Untuk mendefinisikan sebuah enum, cukup gunakan keyword `enum` diikuti dengan nama enum kita. Seperti struct, _naming convention_ untuk enum adalah dengan PascalCase, dan itu juga berlaku untuk setiap enumerasi didalamnya.

Untuk contoh yang lebih detail, saya akan gunakan contoh tentang tipe pembayaran misalnya.

```rust
enum Pembayaran {
	Cash,
	KartuKredit,
	KartuDebit,
}
```
Lalu kita akan menggunakan pattern matching untuk enum kita ini.

```rust
fn main() {
	let pembayaran = Pembayaran::Cash;
	
	match pembayaran {
		Pembayaran::Cash => {
			println!("Membayar dengan cash!");
		}
		Pembayaran::KartuKredit => {
			println!("Membayar dengan Kartu Kredit!);
		}
		Pembayaran::KartuDebit => {
			println!("Membayar dengan Kartu Debit!");
		}
	}
}
```

`match` akan mencocokkan dengan variabel `pembayaran`, enumerasi mana yang dimiliki oleh `pembayaran` yang dalam kasus ini adalah `Pembayaran::Cash`. Saat pattern matching, kita diharuskan untuk menuliskan semua enumerasi kita. Semua kondisi yang memungkinkan harus terpenuhi. Bila tidak, akan terjadi error seperti berikut:

```rust
match pembayaran {
	Pembayaran::Cash => {
		println!("Membayar dengan cash!");
	}
	Pembayaran::KartuKredit => {
		println!("Membayar dengan Kartu Kredit!);
	}
}
```
Akan terjadi error pada kode diatas karena `Pembayaran::KartuDebit` tidak terpenuhi. Kita juga dapat menggunakan tanda underscore `_` untuk meng-cover sisa dari enumerasi seperti ini misalnya.

```rust
match pembayaran {
	Pembayaran::Cash => {
		println!("Membayar dengan cash!");
	}
	_ => {
		println!("Membayar dengan kartu!");
	}
}
```

Tanda `_` diatas akan meng-cover kedua kemungkinan yaitu `Pembayaran::KartuKredit` dan `Pembayaran::KartuDebit`.

Sekarang kita akan membahas tentang fitur yang akan menjadi fitur favorit kita tentang enum. Yaitu mengasosiasikan data pada enumerasi!

Sekarang kita akan mengganti enum pembayaran menjadi seperti ini:

```rust
enum Pembayaran {
	Cash(f64),
	KartuKredit(String, f64),
	KartuDebit,
}
```

Lalu kita akan membuat sebuah struct baru yang bernama `DataDebit` untuk data pada `KartuDebit`.

```rust
struct DataDebit {
	nomor_kartu: String,
	jumlah: f64,
}
```

Sekarang, ganti `KartuDebit` menjadi seperti ini:

```rust
enum Pembayaran {
	Cash(f64),
	KartuKredit(String, f64),
	KartuDebit(DataDebit),
}
```

Hebat, bukan? Kita juga dapat menggunakan tipe kita sendiri untuk `enum`. Lalu bagaimana cara kerjanya? Mari kita lihat!

Sekarang, kita akan mengganti nama variabel `pembayaran` ke `cash`, kemudian menambah value, lalu membuat dua variabel lainnya untuk dua enumerasi lainnya dengan satu variabel dari struct `DataDebit`.

```rust
fn main() {
	let cash = Pembayaran::Cash(20000.0);
	let kredit = Pembayaran::KartuKredit("12345".to_string(), 100000.0);
	
	let data_debit = DataDebit {
		nomor_kartu: "11111".to_string(),
		jumlah: 200000.0,
	};
	
	let debit = Pembayaran::KartuDebit(data_debit);
	
	...
```

Sekarang, kita buat fungsi baru untuk pattern matching. Pindahkan saja pattern matching pada fungsi `main` tadi kesini, kemudian ganti menjadi seperti ini:

```rust
fn bayar(metode: Pembayaran) {
	match metode {
		Pembayaran::Cash(jumlah) => {
			println!("Membayar dengan cash dengan jumlah: {}", jumlah);
		}
		Pembayaran::KartuKredit(no_kartu, _) => {
			println!("Membayar dengan kartu kredit bernomor {}", no_kartu);
		}
		Pembayaran::KartuDebit(data) => {
			println!("Membayar dengan kartu debit bernomor {} dan berjumlah {}", data.nomor_kartu, data.jumlah);
		}
	}
}
```

Kalian lihat. Kita tinggal memberi variabel baru didalam setiap enumerasi seperti `jumlah` pada `Pembayaran::Cash`. Setiap variabel menandai data yang dimiliki enum tersebut. Nama yang digunakan bebas. Kalian akan dapat menggunakannya didalam block enumerasi kalian seperti diatas. Lalu apa fungsi dari `_` pada `Pembayaran::KartuKredit`? Itu adalah tanda untuk memberitahu compiler bahwa kita tidak akan menggunakan data tersebut didalam block enumerasi pada pattern matching kita. Kita juga dapat menamai data yang tidak akan dipakai dengan menggunakan prefix `_` juga seperti `_jumlah`. Namun untuk sekarang, saya lebih memilih menggunakan hanya underscore saja.

Mari kita panggil fungsi diatas dalam fungsi `main` kita.

```rust
fn main() {
	let cash = Pembayaran::Cash(20000.0);
	let kredit = Pembayaran::KartuKredit("12345".to_string(), 100000.0);
	
	let data_debit = DataDebit {
		nomor_kartu: "11111".to_string(),
		jumlah: 200000.0,
	};
	
	let debit = Pembayaran::KartuDebit(data_debit);
	
	bayar(cash);
	bayar(kredit);
	bayar(debit);
}
```

Dan bingo! Anda akan melihat output seperti ini:

```bash
Membayar dengan cash dengan jumlah: 20000
Membayar dengan kartu kredit bernomor 12345
Membayar dengan kartu debit bernomor 11111 dan berjumlah 200000
```

Dengan begitu, materi enumerasi kali ini selesai.

Terima kasih telah membaca, bila ada pertanyaan, silahkan untuk mengirim email pada rahmanhakim2435@pm.me :).
