# Action Plan — klinikpergigianeverglo.com/smile-planner/

Priority order. Effort is for one competent WordPress/Elementor editor.

---

## Phase 1 — Critical fixes (Week 1)

| # | Action | Effort | Why |
|---|---|---|---|
| 1 | Install and configure an SEO plugin (RankMath or Yoast); set the **title** and **meta description** already drafted in the hero widget comment | 30 min | No meta description exists; title is a slug artefact |
| 2 | Trace and remove the **duplicate `<title>` tag** (theme vs plugin conflict) | 30 min | Invalid HTML, signals a template conflict |
| 3 | Set WordPress site language to **Bahasa Melayu** so `<html lang>` stops claiming `en-US` | 5 min | Language declaration contradicts all content |
| 4 | Resolve the **NAP conflict**: pick one address (`Bandar Puteri Bangi` vs `Bandar Bukit Mahkota`), match it exactly to the Google Business Profile, update JSON-LD + FAQ text | 45 min | NAP inconsistency directly suppresses map-pack ranking |
| 5 | Add a **visible NAP block** — address, phone (`tel:` link), opening hours, Google Maps link — to the page footer | 1 hr | Local business with no visible contact details |

**Verify after Phase 1:** Rich Results Test, Search Console URL Inspection, and view-source
confirmation of a single title + present meta description.

---

## Phase 2 — High-impact improvements (Weeks 2–3)

| # | Action | Effort | Why |
|---|---|---|---|
| 6 | Add **Open Graph + Twitter Card** tags (title, description, 1200×630 image) | 30 min | All traffic is Meta/TikTok/WhatsApp ads; previews currently render nothing |
| 7 | Add **internal links**: logo → home, each of the 6 treatment cards → its treatment page, plus a related-services block | 2 hrs | Page is a crawl dead-end with 2 internal links total |
| 8 | Fill the **15 empty alt attributes**, prioritising the 4 promo images; give the 10 gallery images distinct alts | 1 hr | Offer content is invisible to search, AI and screen readers |
| 9 | Add **`sameAs`** (Facebook, Instagram, TikTok, Google Maps) to the JSON-LD | 15 min | Cheapest entity-consolidation win available |
| 10 | Decide on **`aggregateRating`**: remove it, or add real `Review` objects for reviews shown on-page | 45 min | Self-serving rating earns no stars and carries spam-flag risk |
| 11 | Rework the **H1** to carry location + primary service | 20 min | Current H1 has no keyword |
| 12 | Delete the **empty `<h2>`** in the footer | 5 min | Malformed heading |
| 13 | **Server-render the 26 Google reviews** into HTML; keep IntersectionObserver for animation only | 2 hrs | Best content on the page is invisible to non-rendering / LLM crawlers |

---

## Phase 1.5 — Gambar (buat SELEPAS Fasa 1, sebelum apa-apa lagi)

Ditambah 20 Ogos 2026 selepas pengukuran PageSpeed sebenar. **LCP 8.7s** dengan
**3,256 KiB penjimatan gambar** tersedia. Ini kerja berimpak tertinggi yang tinggal.

| # | Action | Effort | Why |
|---|---|---|---|
| 13a | Sahkan elemen LCP: PageSpeed → **Diagnostics → Largest Contentful Paint element** | 5 min | Jangan tukar 8 fail sebelum tahu yang mana satu |
| 13b | Smush → **Bulk Smush** → hidupkan **Resize Full Size Images** (maks ~1920px) | 10 min | Fail 2560px dipaparkan 520px |
| 13c | Smush → **WebP Conversion** → hidupkan | 10 min | Screenshot PNG susut 85–90% |
| 13d | Jalankan **Bulk Smush** seluruh Media Library | 30 min tunggu | 3.2 MB |
| 13e | Padam 2 baris `preconnect` berganda dari widget hero | 5 min | Amaran Lighthouse >4 preconnect |
| 13f | Ukur semula PageSpeed; sasaran LCP <2.5s | 5 min | Sahkan |

**Alat sudah terpasang** — Smush sudah aktif di laman anda. Tak perlu tukar URL manual.

---

## ❌ DIBATALKAN — Fasa 3 item 15 (audit addon Elementor)

Lighthouse Treemap menunjukkan jumlah JavaScript halaman ialah **20.7 KiB**. WP Rocket
menangguhkan three.js, gsap, fullcalendar, Chart.js dan seluruh timbunan addon sehingga
interaksi pengguna — ia tidak pernah dimuat pada page load. **TBT 0ms** mengesahkannya.

Finding asal menandakannya High severity. Ia salah. Kerja berisiko regresi untuk faedah
sifar. **Jangan buat.**

---

## Phase 3 — Content, performance & authority (Month 2)

| # | Action | Effort | Why |
|---|---|---|---|
| 14 | Add **practitioner credentials** — qualifications and MDC registration numbers for Dr. Farah Fatah and Dr. Najmina; link to individual bio pages; add `Person` schema | 3 hrs | Largest E-E-A-T gap on a YMYL health page |
| 15 | ~~Audit the Elementor addon library load~~ — **DIBATALKAN**, lihat Fasa 1.5 | — | Jumlah JS ialah 20.7 KiB; WP Rocket sudah menangguhkan semuanya |
| 16 | Cut to **one font system**; disable Elementor's Roboto / Roboto Slab (all-weight) requests | 1 hr | 3 typography systems, ~36 unused font variants |
| 17 | ~~Execute every `[TUKAR-URL]` to-do~~ — **dinaikkan ke Fasa 1.5**, guna Smush | — | LCP 8.7s menjadikannya kritikal, bukan Bulan 2 |
| 18 | **Pin or self-host** `unpkg.com/alpinejs` and the other unversioned CDN scripts | 1 hr | Unpinned production dependency: reliability + supply-chain risk |
| 19 | Add **`FAQPage`** JSON-LD (expect AI/GEO benefit, not rich-result stars) | 45 min | LLM extraction |
| 20 | Add **`VideoObject`** schema for the 7 YouTube videos | 1 hr | No video rich-result eligibility today |
| 21 | **Expand the 6 treatment descriptions** — process, duration, aftercare, indicative pricing | 6 hrs | One sentence each is thin for commercial intent |
| 22 | Repair the **corrupted video-playlist widget config** (markdown syntax in title/URL fields) before anyone edits it | 1 hr | Re-saving may push the corruption live |
| 23 | Replace image-based testimonials with **real HTML text** | 3 hrs | Text in images is unindexable |

---

## Phase 4 — Monitoring & iteration (Ongoing)

| # | Action | Cadence |
|---|---|---|
| 24 | ✅ **SELESAI 20 Ogos** — Performance 65, LCP 8.7s, TBT 0ms, CLS 0.116. Ukur semula selepas Fasa 1.5 | Bulanan |
| 25 | Verify robots.txt, XML sitemap inclusion, and indexation of `/smile-planner/` in Search Console | Once, then monthly |
| 26 | Confirm AI crawler access (GPTBot, PerplexityBot, ClaudeBot) in robots.txt; consider `llms.txt` | Once |
| 27 | Track map-pack position for "klinik gigi bandar puteri bangi" and variants after the NAP fix | Weekly for 6 weeks |
| 28 | Clear the **53 comments in moderation** and disable comments site-wide | Once |
| 29 | Review the **Novamira MCP "AI Abilities: On"** setting on this production site; apply the 26 pending plugin updates | Once, then monthly |

---

## Sequencing note (dikemas kini 20 Ogos)

Items 1–5 murah dan membuka jalan untuk semua yang lain — buat dahulu.

Kemudian **Fasa 1.5 (gambar)**. Selepas pengukuran sebenar, ini isu teknikal terbesar
yang tinggal: 3,256 KiB dan LCP 8.7s. Ia juga antara yang paling mudah, sebab Smush
sudah terpasang.

Item 15 asalnya dilabel "highest-value performance task". Itu **salah** — ia dibatalkan.
