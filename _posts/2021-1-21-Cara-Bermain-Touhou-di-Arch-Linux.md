---
layout: post
title: "Cara bermain Touhou di Arch Linux dan Turunannya"
date: 2021-1-21 23:37
permalink: /id/Bermain-Touhou-di-Linux
lang: id
---

![touhou]({{site.baseurl}}/images/touhou.png)

Bermain game terutama game Windows di Linux dewasa ini bukanlah lagi sebuah sesuatu yang luar biasa. Dengan banyak usaha dari komunitas open source yang membangun compatibility layer, menjalankan software Windows terutama game menjadi sangatlah mudah. Compatibility layer yang dimaksud tersebut adalah Wine. Wine merupakan software compatibility layer Windows untuk Linux yang dapat dipakai dengan sangat mudah.

#### Touhou Project

Touhou Project merupakan game dojin yang dikembangkan oleh Jun'ya Ota atau yang biasa dikenal dengan sebutan ZUN. Game ini memiliki beberapa versi yaitu versi PC-98, 1st Windows Generation, 2nd Windows Generation, dan 3rd Windows Generation. Game ini sejatinya merupakan game bullet hell dimana kita harus menghindari hujan peluru dari musuh, dengan beberapa spin-off game fighting yang dikembangkan oleh kolaborasi dengan Twilight Frontier. Touhou Project memiliki komunitas yang sangat sangat besar dan telah lama menjadi Internet Culture.

## Menginstall Wine di Arch Linux

Di kebanyakan distro, Wine sudah tersedia di repository utama. Namun, di Arch Linux, kita harus mengaktifkan repository multilib terlebih dahulu. Cara mengaktifkan repository multilib adalah dengan berikut:

1. Jalankan perintah berikut: `sudo <teks editor pilihan anda> /etc/pacman.conf`. Anda bebas memakai text editor manapun yang anda suka. Untuk saya sendiri, text editor yang saya biasa gunakan adalah `vim` sehingga saya akan mengedit file tersebut dengan: `sudo vim /etc/pacman.conf`.

2. Turun kebawah, dan cari baris berikut:
```
#[multilib]
#Include = /etc/pacman.d/mirrorlist
```

3. Uncomment atau hilangkan tanda tagar dari kedua baris tersebut sehingga akan terlihat seperti ini:
```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

4. Jalankan `sudo pacman -Sy` untuk mengupdate repository.

5. Jalankan `sudo pacman -S wine` untuk menginstall wine.

6. Install winetricks dengan: `sudo pacman -S winetricks`

7. Install Microsoft Visual C++ 2015 dengan: `winetricks vcrun2015`

8. Install wine-mono dengan: `sudo pacman -S wine-mono`

9. Install lib32 dari libgnutls dengan: `sudo pacman -S lib32-gnutls`

10. Biasanya setelah semua langkah diatas, Touhou sudah dapat dimainkan. Silahkan coba dengan menjalankan perintah `cd` ke directory dimana Touhou terletak. Contoh: `cd "~/Games/Touhou 10 - Mountain of Faith"` kemudian jalankan dengan `wine Touhou10.exe` atau apapun nama executable dari game Touhou tersebut.

11. Touhou harusnya sudah bisa berjalan. Namun bila ternyata tidak ada suara dan kalian menggunakan pulseaudio dan alsa, maka anda harus menginstall lib32 dari alsa, openal, dan pulseaudio terlebih dahulu dengan perintah berikut: `sudo pacman -S lib32-alsa-plugins lib32-libpulse lib32-openal`.

12. Dengan begini, Touhou termasuk game fightingnya (13.5, 14.5, 15.5 dsb) sudah dapat dijalankan dengan baik.

## Screenshot

### Danmaku

#### Touhou 10: Mountain of Faith

![touhou2]({{site.baseurl}}/images/touhou-mof.png)

#### Touhou 13: Ten Desires

![touhou3]({{site.baseurl}}/images/touhou-td.png)

#### Touhou 14: Double Dealing Character

![touhou4]({{site.baseurl}}/images/touhou-ddc.png)

### Fighting Game

#### Touhou 12.3: Hisoutensoku
![touhou5]({{site.baseurl}}/images/touhou-hisoutensoku.png)

#### Touhou 13.5: Hopeless Masquerade

![touhou6]({{site.baseurl}}/images/touhou-hm.png)

#### Touhou 14.5: Urban Legends in Limbo
![touhou7]({{site.baseurl}}/images/touhou-ulil.png)

#### Touhou 15.5: Antinomy of Common Flowers
![touhou8]({{site.baseurl}}/images/touhou-aocf.jpg)

Terima kasih telah membaca artikel ini. Bila ada pertanyaan, kamu dapat mengirim email ke rahmanhakim2435@pm.me :).
