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
`const`, anda harus mendefinisikan tipe datanya secara eksplisit, sedangkan `let` tidak perlu karena compiler akan menentukannya sendiri. 
Namun, keyword `let` meiliki tipe data default. Bila anda me-assign sebuah nilai integer contohnya kepada variabel yang dideklarasikan dengan
keyword `let`, maka integer tersebut otomatis akan menjadi 32 bit integer (i32). Bila anda ingin memakai 8 bit integer, maka anda harus 
menuliskannya secara eksplisit. Hal ini juga berlaku pada nilai float.

```
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


```
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
| :---     |    :----:                              |
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
