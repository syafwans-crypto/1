# Phase 1 — Kod Siap Paste
**Untuk:** `https://klinikpergigianeverglo.com/smile-planner/`
**Masa dianggarkan:** ~3 jam
**Andaian yang perlu disahkan:** lihat ⚠️ di Blok 3

---

## 📍 PETA LOKASI — kod mana masuk di mana

**Amaran penting:** Blok 1, 2 dan 4a **BUKAN** untuk Elementor. Kalau anda paste tag
`<meta>` dalam HTML widget Elementor, ia akan mendarat dalam `<body>`, bukan `<head>` —
dan tag OG dalam `<body>` diabaikan oleh kebanyakan scraper. Preview WhatsApp tetap kosong.

| Blok | Masuk di mana | Bukan di Elementor? |
|---|---|---|
| **1** Title + Meta Desc | Panel plugin SEO (RankMath/Yoast) di sidebar editor halaman | ✅ Bukan |
| **2** OG + Twitter | Tab **Social** plugin SEO, **atau** WPCode → Header | ✅ Bukan |
| **3** JSON-LD | Elementor → widget HTML **hero** | ❌ Ya, dalam Elementor |
| **4a** Bahasa laman | Settings → General → Site Language | ✅ Bukan |
| **4b** Buang `<h2>` kosong | Elementor → widget HTML **footer** | ❌ Ya, dalam Elementor |
| **5** Blok NAP | Elementor → widget HTML **footer** (sama dengan 4b) | ❌ Ya, dalam Elementor |

### Cara cari widget dalam Elementor

Buka halaman dengan Elementor → tekan **Ctrl/Cmd + I** untuk buka **Navigator**.
Atau lebih mudah: scroll ke bahagian yang dimaksudkan, hover pada blok, klik ikon pensil.

### Widget yang anda perlu sentuh — hanya DUA

#### 🔹 Widget HTML HERO — untuk Blok 3
- **ID Elementor:** section `7ee75a92` → column `60d92862` → widget `1d9e088a`
- **Cara kenal:** bahagian paling atas, background biru gelap, headline
  *"Bukan Sekadar Rawat Gigi."* dengan galeri gambar bergerak di sebelah kanan
- **Dalam widget tu, cari:**
  ```
  <!-- JSON-LD SCHEMA "Dentist" — dibaca oleh Google (rich results / local pack) dan
       AI engine seperti ChatGPT, Perplexity & Gemini (GEO). ... -->
  <script type="application/ld+json">
  ```
- **Ganti** dari `<script type="application/ld+json">` sehingga `</script>` — **satu blok
  itu sahaja**. Jangan sentuh CSS, HTML hero, atau script loader background di bawahnya.

> ⚠️ Widget hero ni panjang (~700 baris). Sebelum edit, **salin keseluruhan isi ke
> Notepad** sebagai backup. Kalau tersilap padam satu `</style>`, seluruh hero pecah.

#### 🔹 Widget HTML FOOTER — untuk Blok 4b dan Blok 5
- **ID Elementor:** section `3c275689` → column `2a62ca38` → widget `6082c2ac`
- **Cara kenal:** bahagian paling bawah sekali, background biru cyan, logo putih Everglo,
  link *"Term of conditon | Privacy Policy"*, teks disclaimer TikTok/Google/Facebook
- **Blok 4b** — cari dan padam `<h2 style="margin: 6px 0 0; ...; color: #fff;"></h2>`
  (ia betul-betul di bawah `<img ... alt="Everglo Dental">`)
- **Blok 5** — paste blok NAP selepas `</h2>` yang dipadam tadi, sebelum
  `<p style="margin: 4px 0 0; ...">` yang ada link Term of condition

### Widget yang perlu diperiksa untuk `<title>` bertindih

Kalau selepas pasang plugin SEO `<title>` masih muncul dua kali, salah satu suspek ialah
**WPCode → Global Header** — admin bar tunjuk **1 snippet aktif** di situ. Buka
`wp-admin → Code Snippets → Headers & Footers` dan periksa isi Global Header.

---

## Blok 1 — Title & Meta Description

Pasang **RankMath** atau **Yoast SEO**, buka halaman Smile-Planner → Edit Snippet.

### Title (pilih satu)

**Pilihan A — utama (58 aksara):**
```
Klinik Gigi Bandar Puteri Bangi | Klinik Pergigian Everglo
```

**Pilihan B — kalau nak tekan servis (61 aksara):**
```
Klinik Gigi Bangi & Kajang | Braces, Scaling & Veneer — Everglo
```

Saya cadang **A**. Nama penuh jenama tolong Google padankan dengan Google Business
Profile, dan "Klinik Gigi Bandar Puteri Bangi" itulah query sebenar dalam GSC.

### Meta Description (152 aksara)
```
Klinik pergigian di Bandar Puteri Bangi, Kajang. Scaling, tampalan, cabut gigi, braces, gigi palsu, whitening & veneer. Mesra first-timer. Book hari ini.
```

### Sekali gus — buang `<title>` bertindih
Selepas plugin SEO aktif, buka **View Source** dan cari `<title`. Kalau masih muncul
**dua kali**, puncanya theme/Elementor yang emit sendiri. Periksa ikut turutan ini:
1. Elementor → Settings → Features → cuba matikan mana-mana "SEO"/"meta" toggle
2. Theme Twenty Twenty-Four `functions.php` atau child theme — cari `wp_title` / `<title>`
3. WPCode → Global Header snippet (ada 1 snippet aktif) — periksa isinya

---

## Blok 2 — Open Graph & Twitter Card

Ini yang paling cepat bagi pulangan: **semua trafik anda datang dari iklan Meta, TikTok
dan link WhatsApp**. Sekarang bila orang share link ni, preview kosong.

Kalau guna RankMath/Yoast, isi terus dalam tab **Social** (lagi selamat — plugin akan
handle escaping). Kalau nak manual, masuk ikut **WPCode → Header**:

```html
<meta property="og:type" content="website" />
<meta property="og:locale" content="ms_MY" />
<meta property="og:site_name" content="Klinik Pergigian Everglo" />
<meta property="og:title" content="Klinik Gigi Bandar Puteri Bangi | Klinik Pergigian Everglo" />
<meta property="og:description" content="Klinik pergigian di Bandar Puteri Bangi, Kajang. Scaling, tampalan, cabut gigi, braces, gigi palsu, whitening &amp; veneer. Mesra first-timer." />
<meta property="og:url" content="https://klinikpergigianeverglo.com/smile-planner/" />
<meta property="og:image" content="https://klinikpergigianeverglo.com/wp-content/uploads/2024/09/IMG_2951.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="Klinik Pergigian Everglo, Bandar Puteri Bangi" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Klinik Gigi Bandar Puteri Bangi | Klinik Pergigian Everglo" />
<meta name="twitter:description" content="Scaling, tampalan, cabut gigi, braces, gigi palsu, whitening &amp; veneer. Mesra first-timer." />
<meta name="twitter:image" content="https://klinikpergigianeverglo.com/wp-content/uploads/2024/09/IMG_2951.png" />
```

⚠️ **`og:image` perlu ditukar.** `IMG_2951.png` bukan 1200×630 dan ia PNG (berat).
Buat satu imej 1200×630 JPG/WebP khas untuk share preview, upload, dan ganti URL di
**tiga tempat** di atas (`og:image`, `twitter:image`). Kalau saiz tak padan, WhatsApp
dan Facebook akan crop sesuka hati.

---

## Blok 3 — JSON-LD yang dibetulkan

**Ganti sepenuhnya** blok `<script type="application/ld+json">` sedia ada dalam widget
HTML hero. Jangan tambah blok kedua — nanti jadi dua entiti.

### ⚠️ Tiga perkara WAJIB disahkan dahulu

| Baris | Isu | Tindakan |
|---|---|---|
| `streetAddress` | JSON-LD asal tulis **Bandar Bukit Mahkota**, FAQ & hero tulis **Bandar Puteri Bangi** | Buka Google Business Profile, salin alamat **verbatim**. Saya guna versi FAQ sebagai default sebab 2 daripada 3 sumber di halaman bersetuju — tapi **GBP yang menentukan**. |
| `sameAs` | Placeholder | Isi URL sebenar Facebook, Instagram, TikTok, Google Maps |
| `geo` | Placeholder | Ambil dari Google Maps: klik kanan pada pin → koordinat |

### `aggregateRating` — saya buang

Rating 5.0/381 tu memang betul, tapi **self-serving markup**: Google tak papar review
rich result untuk `LocalBusiness` sejak 2019, dan rating yang perniagaan isytihar sendiri
tanpa objek `Review` melanggar garis panduan structured data. Review sebenar anda sudah
hidup di Google Business Profile — biar ia kekal di sana.

Kalau tetap nak simpan, syaratnya: tambah objek `Review` untuk review yang **betul-betul
dipaparkan** di halaman (26 review Google tu ada — tapi kena server-render dulu, itu Fasa 2).

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://klinikpergigianeverglo.com/smile-planner/#webpage",
      "url": "https://klinikpergigianeverglo.com/smile-planner/",
      "name": "Smile Upgrade Planner | Klinik Pergigian Everglo",
      "inLanguage": "ms-MY",
      "description": "Smile Upgrade Planner — pemeriksaan gigi dan cadangan rawatan yang sesuai di Klinik Pergigian Everglo, Bandar Puteri Bangi, Kajang.",
      "about": { "@id": "https://klinikpergigianeverglo.com/#dentist" },
      "isPartOf": { "@id": "https://klinikpergigianeverglo.com/#website" }
    },
    {
      "@type": "WebSite",
      "@id": "https://klinikpergigianeverglo.com/#website",
      "url": "https://klinikpergigianeverglo.com/",
      "name": "Klinik Pergigian Everglo",
      "inLanguage": "ms-MY"
    },
    {
      "@type": "Dentist",
      "@id": "https://klinikpergigianeverglo.com/#dentist",
      "name": "Klinik Pergigian Everglo @ Bandar Puteri Bangi",
      "alternateName": [
        "Klinik Pergigian Everglo",
        "Everglo Dental",
        "Everglo Dental Clinic",
        "Everglow Dental",
        "Klinik Gigi Everglo"
      ],
      "description": "Klinik gigi di Bandar Puteri Bangi, Kajang. Rawatan pergigian teliti dan mesra first-timer: pemeriksaan gigi, scaling & polishing, tampalan, cabut gigi, braces (pendakap gigi), gigi palsu (denture), teeth whitening, crown & bridge dan veneer. Mesra kanak-kanak.",
      "url": "https://klinikpergigianeverglo.com/",
      "image": [
        "https://klinikpergigianeverglo.com/wp-content/uploads/2024/09/IMG_2951.png",
        "https://klinikpergigianeverglo.com/wp-content/uploads/2024/09/IMG_7124-scaled.jpg"
      ],
      "logo": "https://klinikpergigianeverglo.com/wp-content/uploads/2026/07/logo-everglo2.png",
      "telephone": "+60-11-6264-9191",
      "priceRange": "$$",
      "currenciesAccepted": "MYR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "No 8 (GF), Jalan Puteri 2A/3, Bandar Puteri Bangi",
        "addressLocality": "Kajang",
        "addressRegion": "Selangor",
        "postalCode": "43000",
        "addressCountry": "MY"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "GANTI_LATITUDE",
        "longitude": "GANTI_LONGITUDE"
      },
      "hasMap": "GANTI_URL_GOOGLE_MAPS",
      "sameAs": [
        "GANTI_URL_FACEBOOK",
        "GANTI_URL_INSTAGRAM",
        "https://www.tiktok.com/@klinikpergigianeverglo",
        "GANTI_URL_GOOGLE_MAPS"
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "18:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Saturday", "Sunday"],
          "opens": "09:00",
          "closes": "17:00"
        }
      ],
      "areaServed": [
        { "@type": "City", "name": "Bandar Puteri Bangi" },
        { "@type": "City", "name": "Bangi" },
        { "@type": "City", "name": "Kajang" },
        { "@type": "City", "name": "Bandar Seri Putra" },
        { "@type": "City", "name": "Bukit Mahkota" },
        { "@type": "City", "name": "Nilai" },
        { "@type": "City", "name": "Semenyih" }
      ],
      "availableService": [
        { "@type": "MedicalProcedure", "name": "Pemeriksaan Gigi (Dental Check-up)" },
        { "@type": "MedicalProcedure", "name": "Scaling & Polishing" },
        { "@type": "MedicalProcedure", "name": "Tampalan Gigi (Filling)" },
        { "@type": "MedicalProcedure", "name": "Cabut Gigi (Extraction)" },
        { "@type": "MedicalProcedure", "name": "Braces / Pendakap Gigi" },
        { "@type": "MedicalProcedure", "name": "Gigi Palsu / Denture" },
        { "@type": "MedicalProcedure", "name": "Teeth Whitening" },
        { "@type": "MedicalProcedure", "name": "Crown & Bridge" },
        { "@type": "MedicalProcedure", "name": "Veneer Gigi" }
      ],
      "employee": [
        { "@id": "https://klinikpergigianeverglo.com/#dr-farah" },
        { "@id": "https://klinikpergigianeverglo.com/#dr-najmina" }
      ],
      "paymentAccepted": "Cash, Credit Card, Debit Card, Atome, Grab PayLater, Insurans Panel",
      "knowsLanguage": ["ms", "en"]
    },
    {
      "@type": "Person",
      "@id": "https://klinikpergigianeverglo.com/#dr-farah",
      "name": "Dr. Farah Fatah",
      "jobTitle": "Pengarah & Doktor Gigi",
      "image": "https://klinikpergigianeverglo.com/wp-content/uploads/2024/09/Dr.-Farah-1.png",
      "worksFor": { "@id": "https://klinikpergigianeverglo.com/#dentist" },
      "description": "Pengasas Klinik Pergigian Everglo dengan pengalaman hampir 10 tahun dalam rawatan pergigian am dan kosmetik.",
      "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "Malaysian Dental Council Registration",
        "identifier": "GANTI_NO_PENDAFTARAN_MDC"
      }
    },
    {
      "@type": "Person",
      "@id": "https://klinikpergigianeverglo.com/#dr-najmina",
      "name": "Dr. Najmina",
      "jobTitle": "Doktor Gigi",
      "image": "https://klinikpergigianeverglo.com/wp-content/uploads/2026/07/Dr.-Najmina.png",
      "worksFor": { "@id": "https://klinikpergigianeverglo.com/#dentist" },
      "description": "Doktor gigi berpengalaman dalam rawatan pergigian am dan kosmetik untuk semua peringkat umur.",
      "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "Malaysian Dental Council Registration",
        "identifier": "GANTI_NO_PENDAFTARAN_MDC"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://klinikpergigianeverglo.com/smile-planner/#faq",
      "isPartOf": { "@id": "https://klinikpergigianeverglo.com/smile-planner/#webpage" },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Adakah saya perlu membuat temujanji?",
          "acceptedAnswer": { "@type": "Answer", "text": "Ya, adalah dinasihatkan untuk membuat temu janji untuk mengelakkan masa menunggu yang lebih lama." }
        },
        {
          "@type": "Question",
          "name": "Adakah saya mendapat panggilan setelah membuat temu janji dalam talian?",
          "acceptedAnswer": { "@type": "Answer", "text": "Ya, kami akan menghubungi anda dan jadualkan temu janji mengikut keselesaan anda. Penyambut tetamu akan membimbing anda melalui proses tersebut." }
        },
        {
          "@type": "Question",
          "name": "Saya takut dengan doktor gigi. Bolehkah anda membantu saya?",
          "acceptedAnswer": { "@type": "Answer", "text": "Kami adalah doktor berpengalaman dan profesional, kami menyediakan pesakit dengan penjagaan yang terbaik sepanjang lawatan mereka. Setelah kebimbangan pergigian anda diuruskan, barulah kami akan meneruskan prosedur rawatan." }
        },
        {
          "@type": "Question",
          "name": "Saya mempunyai banyak pertanyaan. Boleh saya tanya dalam talian?",
          "acceptedAnswer": { "@type": "Answer", "text": "Jangan ragu untuk berjalan masuk bila-bila masa. Muatkan kami dengan semua keraguan dan kebimbangan anda mengenai rawatan pergigian. Kami membangunkan hubungan Pesakit – Doktor dan menjamin kepuasan anda." }
        },
        {
          "@type": "Question",
          "name": "Adakah saya akan mengalami sakit semasa prosedur rawatan?",
          "acceptedAnswer": { "@type": "Answer", "text": "Matlamat kami adalah untuk menyediakan penjagaan pergigian dengan profesionalisme yang terbaik dan keselesaan pesakit adalah keutamaan kami. Kami memberi jaminan bahawa rawatan anda akan menjadi pengalaman yang tidak menyakitkan dan selesa." }
        },
        {
          "@type": "Question",
          "name": "Adakah anda menerima perlindungan insurans?",
          "acceptedAnswer": { "@type": "Answer", "text": "Ya, kami terima. Kami mempunyai beberapa perlindungan insurans yang tersedia di klinik pergigian kami." }
        },
        {
          "@type": "Question",
          "name": "Adakah anda menerima kad kredit / debit?",
          "acceptedAnswer": { "@type": "Answer", "text": "Ya, boleh." }
        },
        {
          "@type": "Question",
          "name": "Bolehkah saya membuat pembayaran secara ansuran?",
          "acceptedAnswer": { "@type": "Answer", "text": "Jika anda mempunyai kad kredit MAYBANK, ya ansuran boleh. Kami juga menyediakan Atome dan Grab PayLater." }
        },
        {
          "@type": "Question",
          "name": "Di mana saya boleh mencari Klinik Everglo?",
          "acceptedAnswer": { "@type": "Answer", "text": "Kami berada di Bandar Puteri Bangi, berdekatan Lotus's Bandar Puteri Bangi. No 8 (GF), Jalan Puteri 2A/3, Bandar Puteri Bangi, 43000 Kajang, Selangor. Anda juga boleh menggunakan Google Maps atau Waze untuk mencari kami." }
        }
      ]
    }
  ]
}
</script>
```

**Nota tentang FAQPage:** jangan harap bintang di SERP. Sejak Ogos 2023 Google hadkan
FAQ rich result kepada laman kerajaan dan institusi kesihatan sahaja. Nilai sebenar
markup ni ialah **pengekstrakan oleh AI** — ChatGPT, Perplexity dan AI Overviews baca
`FAQPage` dengan baik. Ia untuk GEO, bukan untuk bintang.

### Sahkan selepas paste
Google Rich Results Test → https://search.google.com/test/rich-results
Schema validator → https://validator.schema.org/

---

## Blok 4 — Dua pembetulan sebaris

### 4a. Bahasa laman
`Settings → General → Site Language` → **Bahasa Melayu**

Ini betulkan `<html lang="en-US">` yang sekarang mengisytihar halaman ni Bahasa Inggeris
walaupun 100% kandungan Bahasa Melayu.

Kalau tukar site language menyusahkan wp-admin anda, guna cara ini dalam
child theme `functions.php` (halaman ini sahaja):
```php
add_filter( 'language_attributes', function ( $output ) {
    if ( is_page( 2090 ) ) {
        return 'lang="ms-MY"';
    }
    return $output;
} );
```

### 4b. Buang `<h2>` kosong di footer
Dalam widget HTML footer, cari dan **padam** baris ini:
```html
<h2 style="margin: 6px 0 0; font-family: var(--font-display); font-weight: 700; font-size: clamp(1.4rem,3vw,1.7rem); color: #fff;"></h2>
```

---

## Blok 5 — Blok NAP (Nama, Alamat, Telefon)

Sekarang alamat klinik **hanya wujud dalam jawapan FAQ yang tertutup**, dan nombor
telefon **langsung tiada sebagai teks** — ia hanya dalam konfigurasi JSON widget
WhatsApp. Untuk perniagaan setempat, ini kena nampak.

Tambah dalam widget HTML footer, sebelum baris hak cipta:

```html
<div style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px 28px; margin:18px 0 0; font-family:var(--font-body); font-size:0.95rem; color:rgba(255,255,255,0.92);">
  <span itemscope itemtype="https://schema.org/PostalAddress">
    📍 No 8 (GF), Jalan Puteri 2A/3, Bandar Puteri Bangi, 43000 Kajang, Selangor
  </span>
  <a href="tel:+60116264919" style="color:#fff; text-decoration:none; font-weight:600;">
    📞 011-6264 9191
  </a>
  <span>🕐 Isnin–Jumaat 9pg–6ptg · Sabtu–Ahad 9pg–5ptg</span>
  <a href="GANTI_URL_GOOGLE_MAPS" style="color:#fff; text-decoration:none; font-weight:600;">
    🗺️ Dapatkan Arah
  </a>
</div>
```

⚠️ Perhatikan `tel:+60116264919` — sahkan digit penuh nombor tu. Schema asal tulis
`+60-11-6264-9191` (12 digit selepas kod negara), widget WhatsApp pula `601162649191`.
Kira semula dan pastikan kedua-duanya padan.

---

## Senarai semak sebelum tutup Fasa 1

- [ ] Title muncul **sekali sahaja** dalam view-source
- [ ] Meta description wujud dan bawah 160 aksara
- [ ] `<html lang="ms-MY">`
- [ ] Rich Results Test lulus tanpa error
- [ ] Alamat dalam JSON-LD = alamat Google Business Profile, **verbatim**
- [ ] Share link ke WhatsApp — preview papar tajuk, deskripsi dan imej
- [ ] `<h2>` kosong sudah tiada
- [ ] Blok NAB nampak di footer, nombor telefon boleh diklik
- [ ] Submit URL ke Search Console → Request Indexing
