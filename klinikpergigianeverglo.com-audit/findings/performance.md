# Performance — 65/100 · DIUKUR (bukan lagi anggaran)

**Sumber:** PageSpeed Insights, Mobile, 20 Ogos 2026 4:41 PM GMT+8
Moto G Power teremulasi · Slow 4G throttling · Lighthouse 13.4.1 · Single page session

> **Pembetulan.** Audit asal memberi 35 (provisional) berdasarkan capture logged-in
> yang melangkau WP Rocket. Angka sebenar ialah **65**. Caveat itu betul; anggarannya
> tidak. Semua angka di bawah adalah ukuran sebenar.

## Metrik

| Metrik | Nilai | Sasaran | Status |
|---|---|---|---|
| First Contentful Paint | 2.9s | ≤1.8s | ⚠️ |
| **Largest Contentful Paint** | **8.7s** | ≤2.5s | 🔴 |
| Total Blocking Time | **0ms** | ≤200ms | ✅ |
| Cumulative Layout Shift | 0.116 | <0.1 | ⚠️ |
| Speed Index | 4.1s | ≤3.4s | ⚠️ |

Skor lain: Accessibility 91 · Best Practices 100 · SEO 92 · Agentic Browsing 1/3 🔴

---

## ❌ FINDING DIBATALKAN — "vendor libraries" bukan isu

Audit asal menandakan **High severity** untuk timbunan library Happy Addons / Royal
Addons (three.js, gsap, ScrollMagic, Chart.js, plyr, swiper, owl, multiscroll, slick,
isotope, datatables, prism, fullcalendar + locales-all, dan lain-lain).

**Lighthouse Treemap menunjukkan jumlah JavaScript halaman ini ialah 20.7 KiB:**

| Fail | Saiz | % |
|---|---|---|
| `smush-lazy-load.min.js` | 7.5 KiB | 36% |
| `wpr-beacon.js` | 7.5 KiB | 36% |
| Inline (Rocket, FluentForm, Click-to-Chat, dll.) | 5.7 KiB | 27% |

WP Rocket menangguhkan semua library tersebut sehingga interaksi pengguna — ia tidak
pernah dimuat pada page load. **TBT 0ms** dan **Best Practices 100** mengesahkannya.

**Tindakan: batalkan Fasa 3 item 15.** Mengaudit dan menyahaktifkan widget addon ialah
kerja berisiko regresi untuk faedah sifar. Jangan buat.

---

## 🔴 Isu #1 — Penghantaran gambar (jimat 3,256 KiB)

> Lighthouse Insight: *Improve image delivery — Est savings of 3,256 KiB*

**3.2 megabait.** Ini punca LCP 8.7s dan Speed Index 4.1s. Jurang FCP→LCP sebanyak 5.8
saat mengesahkan elemen terbesar ialah gambar, bukan teks atau JS.

Punca yang telah disahkan dari sumber halaman:
- Gambar hero — `Screenshot-*.png`, **screenshot disimpan sebagai PNG**, format terberat,
  dipaparkan hanya 480×600
- 8 × `Testimoni*.png` @ 1024×1024
- `IMG_7124-scaled.jpg` (≤2560px) dipaparkan ~520px
- 10 gambar galeri saiz penuh, dipaparkan 190–280px
- `IMG_2951-1.png`, `IMG_2953.png` — fotograf dalam format PNG

Ini tepat item `[TUKAR-URL]` yang dev asal tandakan sendiri dan tidak pernah laksanakan.

### Penyelesaian: guna Smush yang sedia terpasang

Tidak perlu menukar URL secara manual satu per satu.

1. Smush → **Bulk Smush** → hidupkan **Resize Full Size Images**, maks ~1920px
2. Smush → **WebP Conversion** → hidupkan
3. Jalankan **Bulk Smush** untuk seluruh Media Library

Screenshot PNG → WebP biasanya susut 85–90%.

### Sebelum bertindak
Buka **Diagnostics → Largest Contentful Paint element** dalam PageSpeed untuk nama
elemen yang tepat. Senarai di atas adalah inferens daripada corak metrik dan sumber
halaman — sahkan dahulu.

---

## 🔴 Isu #2 — Render-blocking (jimat 620ms)

Google Fonts Elementor: **Roboto** dan **Roboto Slab**, 100–900 plus setiap italic
(~36 varian), sedangkan section kustom halaman ini menggunakan Poppins yang dimuat
berasingan, dan tema meng-host Inter/Cardo secara lokal. Tiga sistem tipografi.

Buat **selepas** gambar — 620ms kecil berbanding 3.2 MB.

---

## ⚠️ Isu #3 — Lebih 4 preconnect

> Lighthouse Warning: *More than 4 `preconnect` connections were found*

Punca: `fonts.googleapis.com` dan `fonts.gstatic.com` di-preconnect **dua kali** —
sekali dalam widget CSS pertama (`6da1fece`), sekali lagi dalam widget hero
(`1d9e088a`) — ditambah `dns-prefetch` untuk `cdn.jsdelivr.net`, `unpkg.com` dan
`cdnjs.cloudflare.com`.

Padam dua baris ini dari **widget hero sahaja**:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```
Kekalkan baris `<link href="...Poppins...">` dan blok `<noscript>`.

---

## ⚠️ Isu #4 — CLS 0.116

Sedikit di atas ambang 0.1. Suspek: font swap (Poppins `display=swap`), dan kandungan
yang di-inject JavaScript (26 review, deck testimoni 10 gambar) yang muncul lewat.
Keutamaan rendah — betulkan selepas LCP.

---

## Yang memang berfungsi baik

- **TBT 0ms** — JavaScript langsung tidak menyekat main thread
- **Best Practices 100/100**
- WP Rocket menangguhkan JS dengan berkesan
- `content-visibility: auto` + `contain-intrinsic-size`
- Font Awesome digantikan SVG inline
- `prefers-reduced-motion` dihormati
- `width`/`height` eksplisit pada hampir semua gambar
