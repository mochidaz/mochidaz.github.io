---
layout: title
title: "Bahasa Pemrograman Rust 7: Struct, Trait, dan Implementasi"
permalink: /id/Bahasa-Rust-7 
lang: id
layout: post
date: 2022-01-15
---

![rust]({{site.baseurl}}/images/rust-7.png)

Di artikel kali ini, kita akan membahas tentang structs, traits, dan implementasi. Pertama-tama, kita harus mengetahui terlebih dahulu secara umum tentang struct.

Struct merepresentasikan tipe data kompleks yang kita definisikan sendiri. Struct dapat berisi banyak field atau tidak berisi field sama sekali. Rust memiliki method yang dapat diimplementasikan pada sebuah struct, namun Rust tidak memiliki inheritance. Untuk mencapat _polymorphism_, Rust menggunakan trait.

## Struct

Untuk mendefinisikan sebuah struct, kita menggunakan keyword `struct`.

```rust
//main.rs
struct TipeSaya {
	field_a: i32,
	field_b: i32,
}
```
Tidak seperti bahasa C, Rust tidak mengharuskan kita menaruh titik koma setelah kita mendefinisikan sebuah struct. _Naming Convention_ untuk struct pada Rust adalah dengan _PascalCase_ untuk nama struct dan _snake_case_ untuk nama field.

Sekarang, kita akan membuat sebuah variabel baru dari struct tersebut.

```rust
//main.rs
fn main() {
	let tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
	};
}
```
Dengan begini kita telah membuat sebuah struct baru `tipe_saya` dengan `field_a` yang bernilai 10 dan `field_b` yang bernilai 20. Sekarang kita akan coba untuk mengubah `field_a` menjadi 30.

```rust
//main.rs
fn main() {
	let tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
	};
	tipe_saya.field_a = 30;
}
```
Lalu apakah yang akan terjadi? Akan terjadi error pada kode ini. Seperti yang kalian tahu, seluruh variabel pada bahasa Rust itu _Immutable_ atau tidak dapat diubah secara default sehingga field dalam variabel `tipe_saya` tidak dapat diubah. Hal ini tentu dapat diatasi dengan keyword yang telah kita pelajari: Keyword `mut`.

```rust
//main.rs
fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
	};
	tipe_saya.field_a = 30;
}
```
Daaaaan, kode akan ter-compile.

Sekarang, kita akan membuat sebuah file baru bernama `apalah.rs`. 

Didalam `apalah.rs`, saya akan mendefinisikan sebuah struct baru yang bernama `TipeApalah`.

```rust
//apalah.rs
struct TipeApalah {
	hitung: i32,
	bil_bulat: i32,
	bool_apalah: bool,
}
```
Sekarang, kita akan memanggil struct ini di file `main.rs` kita dengan menggunakan `mod` dan `use`.

```rust
//main.rs
mod apalah;
use apalah::TipeApalah;
```
Untuk membuat sebuah module, kita harus menaruh `mod <nama_file>` pada file `main.rs` project kita dan kemudian menggunakan keyword `use` untuk menggunakan fungsi, variabel static/constant, trait, atau struct didalam file tersebut. Untuk langsung memanggil semuanya tanpa menuliskan secara eksplisit, kita dapat menuliskan sebagai berikut: `use nama_file::*;`. Biasanya `mod` dan `use` digunakan di bagian paling atas file. Namun, `mod` dan `use` juga dapat digunakan untuk scope khusus seperti didalam sebuah fungsi.

Sekarang, kita akan coba membuat sebuah variabel dari `TipeApalah`.

```rust
//main.rs
fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
	};
	tipe_saya.field_a = 30;
	
	let tipe_apalah = TipeApalah {
		hitung: 0,
		bil_bulat: 100,
		bool_apalah: false,
	};
}
```
Kira-kira apa yang akan terjadi pada kode diatas? Kode tersebut akan mengalami error!

Mengapa begitu? Itu dikarenakan struct dan field didalam struct tersebut berstatus _private_. Untuk mengatasi hal ini, kita harus menggunakan sebuah keyword bernama `pub` pada saat pendefinisian struct dan juga untuk setiap field didalam struct.

```rust
//apalah.rs
pub struct TipeApalah {
	pub hitung: i32,
	pub bil_bulat: i32,
	pub bool_apalah: bool,
}
```

Dan bingo! Semua akan berjalan dengan lancar. Hal ini juga berlaku pada fungsi dan method.

Sekarang kita akan coba membuat method untuk struct `TipeApalah`.

Untuk membuat method, kita menggunakan keyword `impl` yang berarti _implement_ atau implementasikan diikuti dengan nama struct kita. Pertama-tama, saya akan membuat sebuah method bernama `new()` yang akan digunakan untuk membuat variabel dari struct `TipeApalah` tanpa harus mengetik panjang-panjang.

```rust
//apalah.rs
impl TipeApalah {
	pub fn new(x: i32) -> Self {
		Self {
			hitung: 0,
			bil_bulat: x,
			bool_apalah: true,
		}
	}
}
```

Pada kode diatas, kita menggunakan `Self` sebagai return type kita yang berarti, return type kita adalah tipe yang kita implementasikan - yang dalam kasus ini adalah struct `TipeApalah` kita. Ingat bahwa kita langsung mengembalikan struct `TipeApalah` baru kita sehingga kita tidak perlu menaruh titik koma di akhir.

Method diatas dapat kita panggil dengan cara berikut:

```rust
//main.rs
fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
	};
	tipe_saya.field_a = 30;
	
	let tipe_apalah = TipeApalah {
		hitung: 0,
		bil_bulat: 100,
		bool_apalah: false,
	};
	
	let tipe_apalah2 = TipeApalah::new(20);
}
```

Menggunakan operator `::` kita memanggil method `new` kita. Kita memasukkan angka 20 kedalam method `new` yang nantinya akan di-assign kepada field `bil_bulat` didalam struct `TipeApalah`. Kalian juga dapat membuat parameter lain, untuk memberi nilai kepada `hitung`. Namun pada kasus ini, sebagai contoh, saya akan membiarkan `hitung` dan `bool_apalah` untuk dibuat secara otomatis didalam method `new()`.

Sekarang, mari kita coba membuat satu method lagi yang berbeda dari method `new()` ini.

```rust
//apalah.rs
impl TipeApalah {
	pub fn new(x: i32) -> Self {
		Self {
			hitung: 0,
			bil_bulat: x,
			bool_apalah: true,
		}
	}
	
	pub fn lebih_dari(&self, x: i32) -> bool {
		self.bil_bulat > x 
	}
}
```

Disini kita menggunakan "self" juga, yang diawali dengan tanda ampersand (&). Namun, seperti yang kalian lihat, `self` disini berbeda. Disini, kita tidak memakai huruf S kapital, dan juga memakainnya pada parameter. `self` disini menunjuk pada data didalam struct, sedangkan `Self` dengan S kapital menunjuk kepada tipe.

Dengan menggunakan `self`, kita dapat menggunakan field struct kita di dalam method.

Sekarang mari kita panggil method kedua kita ini.

```rust
//main.rs
fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
	};
	tipe_saya.field_a = 30;
	
	let tipe_apalah = TipeApalah {
		hitung: 0,
		bil_bulat: 100,
		bool_apalah: false,
	};
	
	let tipe_apalah2 = TipeApalah::new(20);
	
	let check = tipe_apalah2.lebih_dari(30);
}
```
Nah, lihat perbedaannya? Pada `tipe_apalah2`, kita memakai `::` untuk memanggil method `new()` sedangkan pada `check`, kita memakai `.` untuk memanggil method `bil_bulat()`. Yang membuatnya berbeda adalah dari `&self` di parameter. Bila kita tidak memakai `&self` pada parameter method kita, kita memakai operator `::` untuk memanggilnya. Namun bila kita memakai `&self`, kita memakai dot operator/`.` untuk memanggilnya.

Omong-omong, kita juga dapat menjadikan struct lainnya sebagai field pada struct kita.

Nah, sekarang kita akan membuat satu method lagi untuk `TipeApalah`.

```rust
//apalah.rs
impl TipeApalah {
	pub fn new(x: i32) -> Self {
		Self {
			hitung: 0,
			bil_bulat: x,
			bool_apalah: true,
		}
	}
	
	pub fn lebih_dari(&self, x: i32) -> bool {
		self.bil_bulat > x 
	}
	
	pub fn tambah_satu(&mut self) {
		self.hitung += 1
	}
}
```
Lihat perbedaannya? Kita memakai keyword `mut` setelah tanda ampersand untuk membuat field menjadi mutable. Setelahnya, kita dapat memanipulasi field tersebut dengan method. Sekarang, saya akan ubah variabel `tipe_apalah` menjadi mutable dan kemudian memanggil method `tambah_satu`.

```rust
//main.rs
fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
	};
	tipe_saya.field_a = 30;
	
	let mut tipe_apalah = TipeApalah {
		hitung: 0,
		bil_bulat: 100,
		bool_apalah: false,
	};
	
	let tipe_apalah2 = TipeApalah::new(20);
	
	let check = tipe_apalah2.lebih_dari(30);
	
	tipe_apalah.tambah_satu();
}
```

Sekarang field `hitung` dalam `tipe_apalah` memiliki nilai 1.

Sekarang, kita akan membahas tentang trait.

Trait digunakan untuk mencapai _polymorphism_ dalam Rust. Dengan trait, kita dapat mendefinisikan _shared behavior_ untuk tipe-tipe yang berbeda. _Shared behaviour_ berarti kita membagi fungsionalitas sebuah tipe kepada tipe lainnya.

Membuat sebuah trait hampir mirip dengan membuat implementasi, hanya saja kita tidak menuliskan `body` untuk method didalamnya. Sekarang, saya akan membuat sebuah trait bernama `TraitApalah` di file `apalah.rs`.

```rust
//apalah.rs
pub trait TraitApalah {
	fn is_valid(&self) -> bool;
}
```

Nah, sekarang kita sudah membuat trait kita. Ingat bahwa seperti struct, kita juga harus menggunakan keyword `pub` agar kita dapat mengakses trait tersebut di file lain, seperti struct namun kita tidak harus menuliskan `pub` untuk setiap method didalamnya. Kita tidak menuliskan `method body`, melainkan nama method, parameter `&self`, dan return type secara langsung dan diakhiri dengan titik koma untuk setiap method. Parameter `&self` diatas akan menunjuk pada setiap field dalam tipe yang diimplementasikan.

Mari kita coba implementasikan `TraitApalah` pada `TipeApalah`. 
```rust
//apalah.rs
pub struct TipeApalah {
	pub hitung: i32,
	pub bil_bulat: i32,
	pub bool_apalah: bool,
}

impl TraitApalah for TipeApalah {
	fn is_valid(&self) -> bool {
		self.bool_apalah
	}
}
```

Kita menggunakan keyword `for` untuk implementasi trait, lalu mengimplementasikan method abstrak yang berada dalam trait tersebut didalamnya. Disini sebagai contoh, saya akan mengecek apalah field `bool_apalah` true atau false pada method `is_valid()`.

Nah, kalian pasti berpikir "Lalu buat apa?" "Kenapa repot-repot bikin trait? Kan bisa langsung aja didalem implementasi structnya?". Ok, mari kita lihat contoh simpelnya. Sekarang, kita akan implementasikan dulu trait `TraitApalah` pada `TipeSaya` juga.

Pertama-tama, kita akan menambahkan field bertipe boolean untuk `TipeSaya` juga sehingga `main.rs` akan menjadi begini:

```rust
//main.rs
mod apalah;
use apalah::TipeApalah;

struct TipeSaya {
	field_a: i32,
	field_b: i32,
	field_c: bool,
}

fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
		field_c: true,
	};
	tipe_saya.field_a = 30;
	
	let mut tipe_apalah = TipeApalah {
		hitung: 0,
		bil_bulat: 100,
		bool_apalah: false,
	};
	
	let tipe_apalah2 = TipeApalah::new(20);
	
	let check = tipe_apalah2.lebih_dari(30);
	
	tipe_apalah.tambah_satu();
}
```
Lalu kita akan mengimplementasikan `TraitApalah` pada `TipeSaya` juga. Jangan lupa untuk memanggil `TraitApalah` dengan `use` juga.

```rust
//main.rs
mod apalah;
use apalah::{TipeApalah, TraitApalah};
```
Lalu kita implementasikan seperti tadi.

```rust
//main.rs
struct TipeSaya {
	field_a: i32,
	field_b: i32,
	field_c: bool,
}

impl TraitApalah for TipeSaya {
	fn is_valid(&self) -> bool {
		self.field_c
	}
}
```
Dan sekarang, saya akan membuat sebuah fungsi baru.

```rust
//main.rs

fn print_jika_valid(check: &dyn TraitApalah) {
	if check.is_valid() {
		println!("Valid!");
	}
}

```
Lihat, fungsi diatas tidak menerima sebuah struct - melainkan sebuah trait! Kita menggunakan keyword `dyn` dengan didahului oleh ampersand untuk menggunakan trait sebagai tipe pada parameter, atau menggunakan trait sebagai return type.

Dengan begini, fungsi diatas dapat digunakan untuk kedua struct kita, yaitu `TipeSaya` dan `TipeApalah`! Sekarang, `main.rs` kita akan terlihat seperti ini:

```rust
//main.rs
mod apalah;
use apalah::{TipeApalah, TraitApalah};

struct TipeSaya {
	field_a: i32,
	field_b: i32,
	field_c: bool,
}

impl TraitApalah for TipeSaya {
	fn is_valid(&self) -> bool {
		self.field_c
	}
}

fn print_jika_valid(check: &dyn TraitApalah) {
	if check.is_valid() {
		println!("Valid!");
	}
}

fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
		field_c: true,
	};
	tipe_saya.field_a = 30;
	
	let mut tipe_apalah = TipeApalah {
		hitung: 0,
		bil_bulat: 100,
		bool_apalah: false,
	};
	
	let tipe_apalah2 = TipeApalah::new(20);
	
	let check = tipe_apalah2.lebih_dari(30);
	
	tipe_apalah.tambah_satu();
	
	print_jika_valid(tipe_saya);
	print_jika_valid(tipe_apalah);
}
```

Sekarang kita akan membahas tentang trait-trait built-in rust yang sangat berguna, dan juga menggunakan macro `derive`.

Kita dapat mengimplementasikan trait `Default` untuk membuat default value untuk struct kita seperti ini:

```
//main.rs
impl Default for TipeSaya {
	fn default() -> Self {
		Self {
			field_a: 0,
			field_b: 0,
			field_c: true,
		}
	}
}
```
Nah, sekarang mari kita coba menggunakan macro `println!` untuk tipe-tipe yang telah kita buat. Untuk mencetak sebuah struct, kita membutuhkan formatter yang berbeda pada `println!`, yaitu yang berupa `{:?}` seperti: `println!("{:?}", vec![1,2,3])`. Namun, walaupun begitu, macro `println!` kita tidak akan langsung bekerja. Akan terjadi error bila kita langsung saja menaruh sebuah struct di dalam macro `println!`. Untuk mengatasinya, struct kita harus mengimplementasikan trait `Debug`. Mengimplementasikan setiap trait secara manual pasti akan sangat membosankan. Jadi, kita dapat mengimplementasikan banyak trait dengan macro `derive`!

```rust
//main.rs

#[derive(Debug)]
struct TipeSaya {
	field_a: i32,
	field_b: i32,
	field_c: bool,
}
```
Dan sekarang, kita akan dapat mencetak `TipeSaya`.

```rust
//main.rs
fn main() {
	let mut tipe_saya = TipeSaya {
		field_a: 10,
		field_b: 20,
		field_c: true,
	};
	tipe_saya.field_a = 30;
	
	let mut tipe_apalah = TipeApalah {
		hitung: 0,
		bil_bulat: 100,
		bool_apalah: false,
	};
	
	let tipe_apalah2 = TipeApalah::new(20);
	
	let check = tipe_apalah2.lebih_dari(30);
	
	tipe_apalah.tambah_satu();
	
	print_jika_valid(tipe_saya);
	print_jika_valid(tipe_apalah);
	
	println!("{:?}", tipe_saya);
}
```

Lakukanlah hal yang sama untuk `TipeApalah` dan `TipeApalah` juga akan dapat dicetak.

Lebih detailnya tentang trait, akan kita bahas di artikel selanjutnya - tentang generics.

Terima kasih telah membaca artikel ini, silahkan kirim email ke rahmanhakim2435@pm.me bila ada pertanyaan dan tunggu update berikutnya ya! :).