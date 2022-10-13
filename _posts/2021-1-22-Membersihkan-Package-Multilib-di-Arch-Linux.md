---
layout: post
title: "Membersihkan Wine dan Package Multilib di Arch Linux"
permalink: /Membersihkan-Wine-dan-Package-Multilib
lang: id
date: 2021-1-22 03:16
categories: [linux]
image: /assets/images/rika-drinks-wine.jpg
author: "mochidaz"

---

Apa kamu telah bosan dengan Wine, ingin menghapus package tertentu seperti Visual C++ atau memang ingin menghapus seluruhnya dikarenakan ukurannya, library-library nya, dan package-packagenya yang sangat besar? Apa kamu ingin membersihkan library-library multilib (lib32) yang tidak kamu butuhkan lagi namun sangat banyak dan menyebalkan hingga bersih? Simak artikel ini!

## Membersihkan Wine

Bila kamu ingin menghapus Wine secara total, maka kamu harus membersihkan package seperti Mono, Gecko, Visual C++, dan sebagainya terlebih dahulu. Namun, dengan menggunakan metode yang akan saya jelaskan ini, kamu yang tidak ingin menghapus wine, hanya package wine tertentu juga dapat melakukannya dengan cara disini yaitu dengan menggunakan builtin uninstallernya. Wine memiliki builtin uninstaller yang dapat kamu gunakan untuk menghapus package-package yang tidak kamu butuhkan lagi. Cara untuk membuka wine uninstaller sangatlah mudah. Run saja command `wine uninstaller` atau `wine64 uninstaller` kemudian kamu dapat melihat menu GUI terbuka. 

![wine-un](images/wine-uninstaller.png)

Disana, kamu dapat melihat package-package seperti Microsoft Visual C++, Wine-Mono, dan Gecko. Kamu tinggal memencet package yang ingin kamu remove, kemudian klik tombol remove. Package tersebut akan segera dihapus. Bila kamu masih ingin menggunakan wine dan hanya menghapus package tertentu, maka langkah diatas sudah cukup. Bila ingin sepenuhnya menghapus wine, jalankan perintah-perintah berikut:

```
# Skip ini bila kamu sudah menghapus wine
$ sudo pacman -R wine && sudo pacman -R $(pacman -Qdtq)

# Menghapus sisa-sisa

$ rm -r .wine
$ rm .config/menus/applications-merged/wine*
$ rm -r .local/share/applications/wine
$ rm .local/share/desktop-directories/wine*
$ rm .local/share/icons/????_*.xpm
```

Dengan begini, seharusnya wine dan sisa-sisanya sudah sepenuhnya hilang.

## Membersihkan Package Multilib

Package multilib diawali dengan prefix `lib32-`. Package-package ini merupakan software-software 32-bit yang dapat digunakan untuk menjalankan dan membangung aplikasi 32-bit di 64-bit. Library multilib terletak di `/usr/lib32`. Lalu, bagaimanakah cara kita menghapus semua library di multilib dengan aman? Yaitu dengan menjalankan perintah berikut: 

```
$ sudo pacman -R `LANG=C pacman -Sl multilib | grep installed | cut -d ' ' -f 2`
```
Nantinya, lib32 yang berasal dari multilib akan teruninstall sedangkan yang berguna seperti `lib32-gcc-libs` akan tetap tersimpan.

Sekalian saja, untuk membersihkan package-package lain yang tidak dipakai lagi, run perintah berikut: `pacman -R $(pacman -Qdtq)` yang akan menghapus semua package yang tidak diperlukan lagi.

Terima kasih telah membaca, nantikan artikel-artikel selanjutnya :).
