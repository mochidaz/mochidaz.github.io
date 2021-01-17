---
layout: post
title: "Bahasa Pemrograman Rust 2: Variabel, Mutability, dan Tipe Data"
categories: [cerita]
date: 2021-1-16 19:19
permalink: /id/Bahasa-Rust-2
---

![rust]({{ site.baseurl }}/images/rust-2.png)

## Variabel
Pada bahasa Rust, kita dapat mendeklarasikan variabel dengan tiga keyword berikut: `const`, `static`, dan `let`.
Variabel `const` tidak akan dapat diubah atau immutable. Variabel `static` dapat diubah, namun membutuhkan keyword `unsafe`
karena operasi ini tidak aman bagi memory. Untuk `let`, `let` merupakan keyword paling umum untuk mendefinisikan variabel
dalam Rust. Tidak seperti `static` dan `const`, `let` **TIDAK DAPAT**	 digunakan diluar fungsi. Bila anda menggunakan `static` maupun
`const`, anda harus mendefinisikan tipe datanya secara eksplisit, sedangkan `let` tidak perlu karena compiler akan menentukannya sendiri. Namun untuk contoh di artikel ini di bagian bawah, saya akan terus mendefinisikan tipe datanya secara eksplisit untuk memperjelas. 
Keyword `let` memliki tipe data default. Bila anda me-assign sebuah nilai integer contohnya kepada variabel yang dideklarasikan dengan
keyword `let`, maka integer tersebut otomatis akan menjadi 32 bit integer (i32). Bila anda ingin memakai 8 bit integer, maka anda harus 
menuliskannya secara eksplisit. Hal ini juga berlaku pada nilai float.

```rust
const FOO: i8 = 10;
static BAR: i8 = 1;

fn main() {
  // i32
  let baz = 3;
  // i8
  let qux: i8 = 4;
}
```


## Mutability
Berikutnya adalah mutability, atau bisa tidaknya variabel tersebut diubah nilainya. Secara default, variabel dalam rust semuanya 
immutable atau tidak dapat diubah. Untuk membuat sebuah variabel mutable atau dapat diubah, diperlukan sebuah keyword yang bernama `mut`. `mut` memungkinkan kita 
untuk re-assign atau memberikan nilai kembali pada suatu variabel. Bila anda mengubah nilai dari suatu variabel tanpa keyword `mut`, maka akan terjadi error.


```rust
fn main() {
  let mut x = 10;
  // Output: 10
  println!("{}", x);
  x = 5;
  // Output: 5
  println!("{}", x);
}
```

## Tipe Data dalam Bahasa Rust

### Primitive Type

| Tipe Data| Nama Tipe                              |
|-------   |-------------------------------------   |
| `i8`     | 8-bit Integer                          |
| `i16`    |   16-bit Integer                       |
| `i32`    | 32-bit Integer                         |
| `i64`    | 64-bit Integer                         |
| `i128`   | 128-bit Integer                        |
| `u8`     | 8-bit Unsigned Integer                 |
| `u16`    | 16-bit Unsigned Integer                |
| `u32`    | 32-bit Unsigned Integer                |
| `u64`    | 64-bit Unsigned Integer                |
| `u128`   | 128-bit Unsigned Integer               |
| `f32`    | 32-bit Floating Point                  |
| `f64`    | 64-bit Floating Point                  |
| `f128`   | 128-bit Float                          |
| `str`    | String Slices                          |
| `bool`   | Boolean                                |
| `char`   | Character                              |
| `array`  | Array dengan ukuran tetap              |
| `usize`  | Unsigned Integer dengan ukuran Pointer |
| `tuple`  | Tuple                                  |
| `slice`  | Slice                                  |
| `isize`  | Signed Integer dengan ukuran Pointer   |

#### Penggunaan

###### Integer

Integer merupakan tipe data bilangan bulat dengan rentang tertentu yang memiliki batas. Berikut adalah rentang minimal dan maksimal dari setiap X-bit signed integer.

| Tipe Integer    | Nilai Minimum        | Nilai Maksimum      |
| --------------  | :-------------:      | :--------------:    |
| 8-bit Integer   | -128                 | 127                 |
| 16-bit Integer  | -32768               | 32767               |
| 32-bit Integer  | -2147483648          | 2147483647          |
| 64-bit Integer  | -9223372036854775808 | 9223372036854775807 |
| 128-bit Integer | −2^127               | 2^127 - 1           |

Saya menuliskan 128-bit Integer dalam bentuk pangkatnya dikarenakan nilainya sangatlah besar. Untuk penggunaan, gunakan Integer untuk menyetor bilangan bulat tanpa koma, dan pakai tipe Integer seefektif mungkin dengan memperhatikan batas jarak yang tertera diatas.


```rust
fn main() {
	let a: i8 = 127;
	let b: i16 = 32767;
	let c: i32 = 2147483647;
	
	// Dan seterusnya
}
```

Contoh penggunaan pada aritmatika:

```rust
fn main() {
	let x = 42;
	let y = 200;
	// OUTPUT: 242
	println!("{}", x + y);
}
```

Untuk `unsigned integer`, `itype`, dan `utype` tidak akan dibahas disini, dikarenakan topik-topik tersebut merupakan topik yang lebih tinggi lagi.

###### Float

`Float` atau `Floating Point` merupakan tipe data yang menyimpan bilangan desimal.

```rust
fn main() {
	let x: f32 = 252.25;
	let y: f64 = 200.42;
}
```

`Float` juga dapat diimplementasikan untuk bilangan bulat, namun membutuhkan titik dan 0 dibelakangnya.

```rust
fn main() {
	let x: f32 = 3.0;
}
```

##### Char

`Char` merupakan tipe data karakter yang hanya memuat satu buah karakter dengan besar 4-bit. Pendeklarasian `char` menggunakan tanda petik satu quote karena dua petik digunakan untuk `string slice`.

```rust
fn main() {
	let x: char = 'a';
}
```

##### String Slice

`String Slice` (`str`) merupakan satu dari dua tipe `string` utama dimana yang satunya lagi merupakan tipe `String` yang bukan merupakan tipe primitif. Tipe `str` selalu dalam kondisi `borrowed` yang nanti akan dibahas di bab `Ownership`. `String Slice` tersimpan dalam `stack` memory.

```rust
fn main() {
	let x: &str = "Tipe String Slice";
}
```

##### Boolean

`Boolean` merupakan tipe data yang hanya menyimpan salah satu dari dua buah value yakni `true` atau `false`.

```rust
fn main() {
	let x: bool = true;
	let y: bool = false;
}
```

##### Array

`Array` memiliki ukuran tetap di memori. Cara pendeklarasiannya adalah sebagai berikut: `let nama: [tipe; ukuran] = [elm1, elm2, elm3]`.

```rust
fn main() {
	let array: [i32; 3] = [0, 1, 2];
}
```

##### Tuple

`Tuple` merupakan tipe yang heterogen. Ia dapat menyimpan banyak tipe data berbeda didalamnya. Elemen dalam tuple dapat diakses dengan menggunakan tanda titik setelah nama variabel tuple tersebut kemudian menuliskan index dari elemen tersebut.

```rust
fn main() {
	let tuple = ("Saya tuple", 22, [2,3,4], 24.5);
	let elemen_pertama = tuple.0;
	// OUTPUT: Saya tuple
	println!("{}", elemen_pertama);
}
```

##### Slice

`Slice` berukuran dinamis, sebuah koleksi dari elemen. `Slice` biasanya digunakan untuk mengambil sejumlah potongan dari dalam `array`.

```rust
fn main() {
	let array: [&str; 5] = ["hai", "hoi", "halo", "hey", "hoi"];
	let slice = &array[0..3];
	
	// OUTPUT: hai hoi halo
	for i in slice {
		print!("{} ", i);
	}
}
```

`Slice` diatas mengambil elemen ke-0 sampai elemen ke-2 `array` tersebut. Bila anda tidak tahu, tanda `&` diatas merupakan tanda `reference` yang akan dibahas nanti.


### Beberapa Tipe Non-Primitif

###### String

`String` merupakan tipe heap dinamis seperti `Vec`. Pendeklarasian `String` dapat dilakukan dengan beberapa cara.

```rust
fn main() {
	let a: String = String::from("Aku adalah String");
	let b: String = "Aku adalah String".to_string();
	let c: String = "Aku adalah String".into();
	let mut d: String = String::new();
	
	d.push_str("Aku adalah String");
}
```

###### Vec (Vector)

`Vec` merupakan tipe data `vector` atau `array dinamis` yang tersimpan dalam memory `heap`. Vector dapat kita gunakan untuk menyimpan tipe data apapun termasuk User-defined data types atau tipe data yang kita definisikan sendiri. Pendeklarasian `Vec` untuk memasukkan value secara langsung menggunakan sebuah `macro` yang bernama `vec!` sedangkan secara tidak langsung, kita menggunakan method `push()` yang akan memasukkan value kedalam `vector` tersebut. Menggunakan `push()` membutuhkan variabel untuk `mutable` atau dapat dirubah. 

```rust
fn main() {
	// Dengan macro
	let x: Vec<i32> = vec![224, 215, 364, 241];
	// Dengan push()
	let mut y: Vec<i32> = Vec::new();
	
	y.push(123);
}
```