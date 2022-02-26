---
layout: post
title: "Bahasa Pemrograman Rust 3: Fungsi, Prosedur, dan Return Type"
lang: id
permalink: /id/Bahasa-Rust-3
date: 2021-1-22 23:58
---

![rust]({{site.baseurl}}/images/rust-3.png)

Pada bagian ketiga ini, sesuai judul, kita akan membahas tentang fungsi, prosedur, dan return type atau tipe data yang dikembalikan oleh sebuah fungsi. 
Anda pastinya sudah tidak asing dengan fungsi bila anda telah belajar tentang fungsi pada matematika, atau bahasa pemrograman lain. Benar, fungsi menerima 
parameter, memproses data, kemudian mengembalikannya dengan berupa sebuah nilai tertentu. Lalu, apa bedanya fungsi dan prosedur? Bagaimana cara 
kita mendefinisikan fungsi pada Bahasa Rust? Bagaimana cara kita mendefinisikan return type dan mengembalikan sebuah nilai dari fungsi tersebut? Mari simak baik-baik!

## Statement dan Expression

Sebelum masuk ke pembahasan utama, ada baiknya kita pahami tentang *statement* dan *expression* terlebih dahulu.

*Statement* adalah sebuah pernyataan yang menyatakan sebuah perintah untuk melakukan sesuatu. *Statement* tidak mengembalikan nilai apapun. Ia hanyalah instruksi. 
Contoh dari statement adalah pendeklarasian variabel, pendefinisian fungsi, perintah loop seperti `for` dan `while`, dan semacamnya.

*Expression* adalah sebuah ekspresi yang mengevaluasi sebuah nilai. *Expression* mengembalikan sebuah nilai. Contoh dari *expression* adalah `1 + 1`, `7 - 4`, `5 != 2`, 
dan pernyataan yang aritmatika lainnnya yang juga dapat melibatkan `boolean`.

Rust merupakan `expression-oriented language` atau bahasa berorientasi ekspresi yang berarti hampir semua yang ada di dalamnya berupa ekspresi.

*Expression* dapat berada dalam *statement*. Contohnya adalah dalam pendeklarasian variabel: `let x = 10;`. Disana, `let x =` merupakan sebuah *statement* sedangkan 
*expression* adalah nilai dari variabel itu sendiri: 10.

## Fungsi

Fungsi adalah sebuah "modul" kode yang "mandiri" yang digunakan untuk menyelesaikan tugas khusus. Seperti yang sudah saya jelaskan diatas, fungsi biasanya 
mengambil data tertentu, memprosesnya, kemudian mengembalikan nilai hasil proses tersebut. Fungsi dapat dipanggil dalam fungsi lain dan dapat digunakan berulang 
kali untuk data yang nilainya berbeda. Mendefinisikan fungsi di Rust tidak sulit. Kita menggunakan keyword `fn` untuk mendefinisikan fungsi dalam bahasa ini. Anda 
pasti tidak asing dengan keyword ini karena anda pastinya telah melihat bentuk dari *entry point* Rust yaitu fungsi utama atau *main function*-nya.

```rust
fn main() {
   println!("Hello World!");
}
```

Fungsi diatas adalah fungsi utama, dan tidak mengembalikan maupun menerima nilai apapun. Fungi yang tidak mengembalikan apapun disebut juga dengan `void function`.

### Parameter

Parameter adalah variabel dalam definisi fungsi yang terletak didalam kurung fungsi. Kurang lebih, parameter bertindak seperti *placeholder* yang mewakili sebuah nilai 
yang kemudian ditunjukkan bagaimana ia akan diproses dalam fungsi tersebut. Parameter menerima data yang disebut dengan argumen. Dalam fungsi, kita akan "menjelaskan" 
tentunya dengan algoritma yang kita buat untuk bagaimana sang nilai akan diproses. Dan nilai itu diwakili dengan parameter tersebut, yang nantinya disaat sebuah nilai 
diberikan, sang nilai akan diproses sesuai dengan bagaimana parameter di dalam fungsi tersebut diproses. Untuk mendefinisikan sebuah parameter, tidak seperti C++ yang 
menaruh tipe data dibelakang nama parameter (contoh: `int x`), Rust menaruh tipe data di depan parameter dengan pembatas ":". Seperti ini: `x: i32`.

### Return dan Return Type

Return merupakan sebuah *statement* untuk memerintahkan sebuah fungsi mengembalikan value tertentu, yang tentunya harus sesuai dengan tipe data yang dituliskan pada return type. Return type merupakan jenis tipe data dari nilai yang dikembalikan oleh sang fungsi setelah diproses. Rust menggunakan tanda `->` kemudian menaruh 
nama tipe data yang akan dikembalikan didepan tanda panah tersebut. Bila nilai yang dikembalikan tidak sesuai dengan return type yang dituliskan, maka akan terjadi error.

Sekarang, mari kita langsung lanjutkan ke contoh sederhana dan penggunaan dengan lebih mendetail.

Dibawah ini adalah sebuah fungsi yang dapat menambahkan dua 32-bit integer kemudian mengembalikan sebuah value, yaitu hasilnya.

```rust
fn add(x: i32, y: i32) -> i32 {
   x + y
} 
```

`-> i32` diatas merupakan return typenya yang merupakan 32-bit integer. `x: i32, y:i32` merupakan parameter yang melambangkan bahwa nilai yang akan diberikan kepada fungsi tersebut 
adalah 32-bit integer dan nilai tersebut diwakili dengan variabel `x` dan `y` yang sebenarnya dapat dengan bebas kita namakan apapun seperti variabel pada umumnya. Lalu yang terakhir, 
`x + y` dibawah merupakan sebuah *expression*, yang menjadi nilai yang dikembalikan atau direturn. Dalam bahasa Rust, kita dapat mengembalikan nilai dari sebuah fungsi dengan dua cara: 
Menggunakan keyword `return`, atau menaruh sebuah *expression* di paling akhir baris fungsi TANPA TITIK KOMA. Keduanya sama saja, namun menggunakan `return` dianggap sebagai gaya penulisan yang buruk 
atau *bad style*. Mengapa begitu? Karena Rust merupakan *expression-oriented language*. Untuk menekankan bahwa Rust merupakan *expression-oriented language*, hal semacam itu dilakukan. 
Bila kita ingin mengembalikan nilai dengan gaya seperti itu, JANGAN taruh titik koma di akhir baris karena *expression* tersebut akan berubah menjadi *statement*. Gunakan `return` hanya pada saat anda ingin melakukan _early return_ atau mengembalikan nilai lebih awal. _Early return_ akan dibahas pada bab _Result, Option, dan Pattern Matching_. 

Fungsi membutuhkan variabel saat dipanggil, untuk menyimpan nilai yang dikembalikan di dalam variabel tersebut.

```rust
fn add(x: i32, y: i32) -> i32 {
   x + y
}

fn main() {
  let a = 10;
  let b = 20;
  // Menyimpan nilai yang dikembalikan oleh fungsi ke variabel hasil
  let hasil = add(a, b);
  
  // OUTPUT: 30
  println!("{}", hasil); 
}
```

## Prosedur

Sebenarnya mungkin semua `void function` juga dapat disebut sebagai prosedur dikarenakan prosedur pada dasarnya adalah fungsi, namun tidak mengembalikan apapun. 
Namun, saya akan menanamkan pemahaman prosedur dan pengertiannya secara lebih dalam untuk apa prosedur tersebut digunakan.

Prosedur hanya mengeksekusi sebuah perintah. Prosedur tidak membutuhkan variabel dan dapat secara begitu saja dipanggil dikarenakan prosedur hanya untuk mengeksekusi 
perintah tertentu dan tidak mengembalikan apapun. Nilai yang biasanya dimasukkan ke dalam parameter prosedur adalah berupa `reference` yang akan kita bahas nanti. Dengan 
reference, nilai tidak menjadi terpisah dengan variabel asli diluar fungsi namun nilai yang dimasukkan akan ikut berubah secara langsung. Seperti ini contohnya:

```rust
fn add_five(x: &mut i32) {
   *x += 5;
}

fn main() {
   let mut a = 10;
   add_five(&mut a);
   // OUTPUT: 15
   println!("{}", a);
}
```

Nah, prosedur `add_five` diatas berfungsi untuk menambahkan 5 ke suatu variabel 32 bit integer. Misalnya kita membuat sebuah fungsi hanya untuk hal seperti diatas, nantinya malah 
lebih panjang dan terlihat lebih "ribet". Kita tidak akan membutuhkan variabel `a` lagi setelah kita mendeklarasi sebuah variabel yang memuat nilai return dari fungsi yang menambah 5 
variabel a diatas. Hal itu akan memakan lebih banyak memory. Oleh karena itu, dengan prosedur, variabel `a` dapat digunakan berkali-kali dan diubah-ubah nilainya. Bagi yang tidak tahu, 
tanda bintang `*` diatas merupakan pointer untuk de-reference sebuah reference, yang artinya, ia mengubah alamat memory yang menunjuk pada suatu nilai menjadi nilai yang ditunjuk kembali.

Kita juga dapat menggunakan prosedur untuk membuat "printer" atau sesuatu yang mem-print output khusus untuk aplikasi command line seperti berikut: 

```rust
fn print_selamat_datang(nama: &str) {
   println!("SELAMAT DATANG");
   println!("      DI      ");
   println!("APLIKASI SAYA,");
   println!("Pak/Bu {}", nama);
}

fn main() {
   let nama = "Rahman";
   print_selamat_datang(nama);
}
```

Kira-kira untuk pembahasan Fungsi, Prosedur, dan Return Type cukup sampai disini. Nantikan artikel berikutnya :).
