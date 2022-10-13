---
layout: post
title: "Bahasa Pemrograman Rust 9: Generics"
permalink: /Bahasa-Rust-9
lang: id
date: 2022-01-16 02:00
categories: [rust, programming]
image: /assets/images/rust-9.png
author: "mochidaz"

---


Saya sudah pernah menjelaskan tentang generics pada [Bab Result, Option, dan Pattern Matching](https://mochidaz.github.io/id/Bahasa-Rust-5). Dengan generics, kita dapat menuliskan tipe data abstrak dengan _placeholder types_ untuk struct, enum, dan juga fungsi. Kita menggunakan _placeholder types_ daripada mendefinisikan tipe datanya secara eksplisit. Kita dapat menuliskan kode yang bekerja untuk tipe-tipe data yang berbeda sehingga menambah fleksibilitas kode kita. Dengan generics, kita dapat mengurangi duplikasi kode. Ingat bahwa generics tidak memiliki _runtime cost_ - Generics dibuat saat _compile time_ sehingga performa _runtime_ akan tetap sama, dengan saat anda tidak menggunakan generics. Mari kita langsung masuk ke masalah pertama!

Sekarang saya akan membuat sebuah struct bernama `Apalah` yang berisi field `x` dan `y` yang keduanya memiliki tipe `i32`.

```rust
struct Apalah {
	x: i32,
	y: i32,
}
```

Nah, sekarang saya akan coba mencetak kedua field tersebut.

```rust
fn main() {
	let a = Apalah {
		x: 10,
		y: 20,
	};
	
	println!("x = {}, y = {}", a.x, a.y);
}
```

Kode tersebut akan berjalan dengan baik dan akan mencetak kedua field yang bertipe `i32` tersebut. Namun bagaimana bila kita ingin mengisi struct tersebut dengan `f64` misalnya? Tentunya kita tidak boleh melakukan ini:

```rust
struct Apalah {
	x: i32,
	y: i32,
}

struct Apalah {
	x: f64,
	y: f64,
}
```

Sehingga kita akan terpaksa menggunakan nama yang berbeda untuk dua struct yang sama dan hanya dibedakan oleh tipe field.

```rust
struct ApalahI32 {
	x: i32,
	y: i32,
}

struct ApalahF64 {
	x: f64,
	y: f64,
}
```

Terjadi duplikasi kode disini. Kita membuat dua struct sama yang hanya berbeda pada tipe, dengan nama yang berbeda. Karena inilah solusi yang membuat kode lebih fleksibel - generics diperlukan!

Mari kita hapus kedua struct diatas dan mendefinisikan struct `Apalah` lagi, namun kali ini berbeda.

```rust
struct Apalah<T> {
	x: T,
	y: T,
}
```
Nah, seperti yang kalian tahu, `T` merupakan tipe _placeholder_ yang dapat diganti dengan tipe data apapun - compiler yang akan mengurusnya. Dengan `T`, kita akan dapat menggunakan struct `Apalah` untuk tipe data yang berbeda-beda. Mari kita coba.

```rust
fn main() {
	let a = Apalah {
		x: 10,
		y: 20,	
	};
	
	println!("x = {}, y = {}", a.x, a.y);
	
	let b = Apalah {
		x: 10.5,
		y: 15.77,	
	};
	
	println!("x = {}, y = {}", b.x, b.y);
}
```
Daaaan kode akan tercompile dengan baik.

Apa yang terjadi disini? Disini, compiler akan secara otomatis mengisi tipe `T` dengan `i32` disaat kita menggunakan tipe `i32` saat kita membuat variabel bilangan bulat dari struct tersebut, dan juga `f64` bila kita menggunakan desimal! Terima kasih, compiler. Namun, bila kita ingin menggunakan `f32` untuk float misalnya, dan bukan `f64`, kita juga dapat mendefinisikan tipe data kita secara eksplisit pada saat pendeklarasian ataupun assignment seperti ini:

```
let b: Apalah<f32> = Apalah {
	x: 10.5,
	y: 15.77,	
};
```
Sangat berguna, bukan?

Lalu, kenapa kita menggunakan `T`? Dan bukan huruf lain? Sebenarnya, `T` hanyalah sebuah _placeholder_. Seperti sebuah identifier variabel, kalian bisa mengganti `T` dengan apapun sesuka kalian. Namun, `T` merupakan _naming convention_ yang baik untuk generics. `T` merupakan kependekan dari _Type_ atau tipe. Biasanya, _naming convention_ untuk generics setelah `T` dilanjutkan dengan huruf sesudah `T` yaitu `U`. Namun tentu saja penamaan itu relatif.

Menuliskan dua tipe generic berbeda sangat mudah. Hanya tinggal menambah satu huruf yang berbeda seperti ini:

```rust
struct Apalah<T, U> {
	x: T,
	y: U,
}
```
Dan sekarang kita dapat membuat sebuah struct dengan dua tipe generic yang berbeda seperti ini:

```rust
let a = Apalah {
	x: 10,
	y: 15.8,	
};
```
Atau tentu saja misalnya

```rust
let a: Apalah<i32, f32> = Apalah {
	x: 10,
	y: 15.8,	
};
```

Generics juga berlaku untuk enumerasi. Mari sekarang kita bersihkan dan hapus struct `Apalah` kita, dan semua yang ada didalam fungsi `main` dan membuat sebuah enum generic baru.

```rust
enum EnumApalah<T> {
	OpsiA(T),
	OpsiB(T),
	OpsiC,
}
```

Kemudian kita gunakan pattern matching.

```rust
fn main() {
	let apalah = EnumApalah::OpsiA(20);
	let apalah2 = EnumApalah::OpsiB(vec![1,2,3]);
	
	match apalah {
		EnumApalah::OpsiA(a) => {
			println!("OpsiA memiliki {}", a);
		}
		EnumApalah::OpsiB(b) => {
			println!("OpsiB memiliki {}", b);
		}
		EnumApalah::OpsiC => {
			println!("OpsiC tidak ada apa-apa");
		}
 	};
}
```

Dan tentu saja, generic juga bekerja pada tipe yang berupa struct, seperti `apalah2` diatas yang memuat `Vec` atau vektor.

Sekarang kita akan masuk ke fungsi generic. Silahkan untuk clear atau hapus enum yang telah kita buat, dan juga semua yang ada didalam fungsi `main`.

Pembuatan fungsi generic juga mirip dengan struct, yaitu sebagai berikut:

```rust
fn fungsi_apalah<T>(a: T, b: T) -> T {
	a
}
```
Diatas, kita memakai `T` sebagai tipe untuk a dan b, dan juga return typenya. Ini hanyalah sebuah contoh membosankan untuk generic pada fungsi.

Kedua tipe pada parameter fungsi diatas adalah `T` sehingga bila kita memasukkan tipe `i32` misalnya pada parameter `a`, namun memasukkan tipe `f32` pada parameter `b`, maka akan terjadi error.

Sekarang, mari kita masuk pada bagian yang tidak membosankan dan juga bagian menarik utamanya: Trait bounds.

Generics pada Rust adalah trait-based generics yang berarti limitasi atau apa yang bisa kita lakukan dengan generics didasarkan pada traits yang dibatasi olehnya. Bingung? Mari kita lihat sebuah contoh.

Kita ganti `fungsi_apalah` menjadi seperti ini:

```rust
fn fungsi_apalah<T>(a: T, b: T) -> T {
	a + b
}
```
Kira-kira apa yang akan terjadi? Akan terjadi error! Kalau anda memakai `template` pada bahasa C++, maka anda akan langsung bisa menambahkan kedua parameter diatas. Namun, tidak dengan Rust. Generics pada Rust dibatasi, atau diikat oleh trait. Dengan kata lain, kita harus menggunakan trait untuk melakukan operasi tertentu untuk tipe yang ingin kita input.

Untuk pertambahan, Rust menyediakan sebuah trait builtin yaitu `std::ops::Add`. Mari kita tambahkan!

```rust
fn fungsi_apalah<T: std::ops::Add<Output=T>>(a: T, b: T) -> T {
	a + b
}
```

Nah, sekarang mari kita tes.

```rust
fn main() {
	let a = fungsi_apalah(10, 20);
	println!("Hasilnya adalah: {}", a);
}
```

Dan jreng! Sekarang parameter `a` akan dapat ditambahkan dengan parameter `b` dan kita akan mendapat output `Hasilnya adalah: 30`!

Sekarang saya akan menjelaskan tentang trait `Add` diatas. Jadi, untuk menggunakan generics pada Rust untuk suatu tipe, tipe yang akan digunakan harus mengimplementasi trait khusus, dan kemudian kita akan menggunakan trait yang diimplementasi oleh tipe tersebut dalam fungsi kita.

Contohnya, tipe seperti `i32`, `f32`, dan sebagainya telah mengimplementasi trait `Add` sehingga kita dapat menggunakannya pada fungsi generic tersebut. Namun, apa yang akan terjadi bila kita memasukkan tipe yang tidak mengimplementasi `Add` seperti string slice, misalnya? Tentu saja akan terjadi error! Lebih tepatnya seperti ini: `help: the trait `Add` is not implemented for `&str` ` yang berarti trait `Add` tidak diimplementasikan untuk `&str`.

Trait yang digunakan seperti diatas dinamakan juga dengan _constraint_.

Sudah jelaskan? Lalu apa fungsi dari `<Output=T>`? Itu untuk memberitahu Rust bahwa output dari fungsi tersebut adalah `T`, bukan yang lain. Lalu mengapa ini dibutuhkan? Karena bisa saja saat kita menambahkan kedua tipe yang sama, misalnya `T + T`, pertambahan tersebut berujung kepada hasil yang memiliki tipe yang berbeda, misalnya `U` atau `T + U` = `V`. Karena itu, kita harus mendefinisikan tipe `Output` kita.

Sekarang, bagaimana kalau kita juga ingin memakai operator pengurangan pada fungsi kita? Simpel, kita tambahkan _constraint_ lainnya dengan operator `+`. Trait untuk pengurangan adalah `std::ops::Sub`.

```rust
fn fungsi_apalah<T: std::ops::Add<Output=T> + std::ops::Sub<Output=T>>(a: T, b: T) -> T {
	a - b
}
```

Dan sekarang kita bisa melakukan pengurangan dalam fungsi generic kita.

Sekarang, kita akan menambahkan `std::fmt::Debug` agar kita dapat menggunakan `println!` dalam fungsi kita.

```rust
fn fungsi_apalah<T: std::ops::Add<Output=T> + std::ops::Sub<Output=T> + std::fmt::Debug>(a: T, b: T) -> T {
	println!("a memiliki: {:?}", a);
	a - b
}
```
Namun... _constraint_ kita sekarang terlihat sangat berantakan. Oleh karena itu, Rust menyediakan alternatif lain yang berupa keyword `where`.

```rust
fn fungsi_apalah<T>(a: T, b: T) -> T 
where T: std::ops::Add<Output=T> + std::ops::Sub<Output=T> + std::fmt::Debug {
	println!("a memiliki: {:?}", a);
	a - b
}
```
Nah, kode kita sekarang terlihat lebih _readable_. Dan sekarang, kita akan menambah satu parameter lain yang bertipe berbeda. `U` misalnya lalu menambah _constraint_ `Debug`.

```rust
fn fungsi_apalah<T, U>(a: T, b: T, c: U) -> T 
where T: std::ops::Add<Output=T> + std::ops::Sub<Output=T> + std::fmt::Debug,
      U: std::fmt::Debug {
	println!("a memiliki: {:?}", a);
	println!("c memiliki: {:?}", c);
	a - b
}
```

Untuk menambahkan constraint pada tipe lain, cukup dengan menambah koma saja di akhir _constraint_ untuk satu tipe, bukan operator `+`.

```rust
fn main() {
	let a = fungsi_apalah(10, 20, "Halo");
	println!("Hasilnya adalah: {}", a);
}
```

Output dari `println!` kita sekarang akan berupa:

```
a memiliki: 10
c memiliki: "Halo"
Hasilnya adalah: -10
```

Sekarang, kita akan membuat sebuah trait baru dengan satu method bernama `TraitApalah`.

```rust
trait TraitApalah {
	fn apalah(&self, a: &str, b: &str) -> String;
}
```
Nah, sekarang kita akan membuat dua fungsi baru.

```rust
fn sesuatu<T>(x: &T) -> String 
where T: TraitApalah {
	println!("{:?}", x);
	x.apalah("satu", "dua")
}

fn sesuatu2(x: &dyn TraitApalah) -> String {
	println!("{:?}", x);
	x.apalah("satu", "dua")
}
```

Seperti yang kalian lihat, fungsi `sesuatu` merupakan fungsi generic dan `sesuatu2` tidak. Mungkin kalian berpikir untuk apa repot-repot menggunakan generic dan _constraint_ pada fungsi `sesuatu`. Fungsi `sesuatu2` akan lebih simpel. Namun, kalian lihat, kedua fungsi tersebut memiliki error karena mereka memiliki `println!` namun tidak mengimplementasikan `Debug`. Akan ribet untuk memperbaiki itu pada fungsi `sesuatu2`, sedangkan pada fungsi `sesuatu`, kita hanya tinggal menambah _constraint_ `Debug`.

```rust
fn sesuatu<T>(x: &T) -> String 
where T: TraitApalah + std::fmt::Debug {
	println!("{:?}", x);
	x.apalah("satu", "dua")
}

fn sesuatu2(x: &dyn TraitApalah) -> String {
	println!("{:?}", x);
	x.apalah("satu", "dua")
}
```

Dan error pada fungsi `sesuatu` akan hilang.

Sekarang, hapus fungsi `sesuatu2` dan kita buat sebuah struct baru bernama `StructApalah`. Jangan lupa derive `Debug`.

```rust
#[derive(Debug)]
struct StructApalah {
	sesuatu: i32,
}
```

Lalu kita implement `TraitApalah` pada `StructApalah`.

```rust
impl TraitApalah for StructApalah {
	fn apalah(&self, a: &str, b: &str) -> String {
		self.sesuatu.to_string() + "|" + a + "|" + b
	}
}
```

Lalu kita coba gunakan fungsi `sesuatu` pada `StructApalah`.

```rust
fn main() {
    let a = StructApalah {
        sesuatu: 100
    };

    let b = sesuatu(&a);
    println!("{}", b);
}
```
Output yang akan keluar adalah:
```bash
StructApalah { sesuatu: 100 }
100|satu|dua
```

Sekarang, mari kita coba untuk mengimplementasikan `TraitApalah` pada tipe primitif - yaitu `i32`. Benar, kita bisa melakukannya.

```rust
impl TraitApalah for i32 {
	fn apalah(&self, a: &str, b: &str) -> String {
		"i32".to_string() + "|" + a + "|" + b
	}
}
```

Lalu kita coba pakai di fungsi `main`.

```rust
fn main() {
    let a = StructApalah {
        sesuatu: 100
    };

    let b = sesuatu(&a);
    println!("{}", b);
    
    let sebuahi32 = 10;
    let c = sesuatu(&sebuahi32);
    println!("{}", c);
}
```

Kode akan berjalan dengan sempurna. Kita dapat menggunakan fungsi generic `sesuatu` pada kedua tipe berbeda tersebut karena mereka mengimplementasikan `TraitApalah` dan fungsi tersebut memiliki _constraint_ `TraitApalah` juga.

Mungkin implementasi diatas terlihat aneh, namun saya ingin menunjukkan bahwa tipe itu sekarang agaknya tidak relevan dalam _generic programming_ - trait-lah yang bermain peran besar. Itulah yang dimaksud dengan _trait-based generics_.

Sekarang, bersihkan lagi semua yang tadi kita tulis dan kita akan merombak ulang `StructApalah`. Kita akan mempelajari cara untuk menggunakan implementasi pada struct generic. Kita akan membuat sebuah `logger` sederhana sebagai contoh.

```rust
struct StructApalah<T,U> {
	a: T,
	b: U,
}

impl<T,U> StructApalah<T,U>
where T: std::fmt::Debug,
      U: std::fmt::Debug {
	fn log(&self) {
		println!("Logging! a: {:?} b: {:?}", self.a, self.b);
	}
}

```

Kita menggunakan _constraint_ untuk generics pada struct untuk method pada implementasi - dengan `where` juga, seperti pada fungsi.

Mari kita buat sebuah variabel dari `StructApalah` dan kemudian kita gunakan method `log`. Selalu ingat bahwa `a` dan `b` dapat diisi dengan tipe apapun yang mengimplementasi `Debug`.

```rust
fn main() {
	let a = StructApalah {
		a: 20,
		b: vec![0,0,0,0],
	};
	
	a.log();
}
```

Dan kode diatas akan berjalan dengan sempurna dengan output seperti ini:

```bash
Logging! a: 20 b: [0, 0, 0, 0]
```

Demikian akhir dari topik generics kita kali ini, terima kasih banyak sudah membaca, bila ada pertanyaan, silahkan kirim email ke rahmanhakim2435@pm.me :).
