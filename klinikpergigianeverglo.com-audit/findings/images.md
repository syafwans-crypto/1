# Images — 48/100

## High — 15 content images with empty `alt`

All are Elementor image widgets with an unfilled Media Library alt field:

1. `logo-everglo2.png` — brand logo (also not linked)
2. `dental-treatment-768x768.png`
3–10. `Testimoni1`, `Testimoni2-1`, `Testimoni3`, `Testimoni4`, `Testimoni5`, `Testimoni6`,
   `Testimoni8`, `Testimoni9-4`
11. `Google-Review-Everglo.png`
12. `Whitening-Promo` · 13. `Composite-Veneer-Promo` · 14. `Brace-Promo` · 15. `Scaling-Promo`

**Items 12–15 matter most** — they are the page's commercial offers, entirely unreadable to
search engines, LLMs and screen-reader users.

## Medium — gallery: one alt string, ten times

All 10 tiles use `alt="Galeri Everglo"`. Give each a distinct description
("Bilik rawatan…", "Kaunter penyambut tetamu…").

## Low — duplicated attributes

```html
<img loading="lazy" src="…" alt="…" width="34" height="34" loading="lazy" decoding="async">
<img fetchpriority="high" … loading="eager" fetchpriority="high" decoding="async">
```
Invalid HTML; first occurrence wins. No ranking impact, but it breaks automated auditing.

## Done well — credit where due

The hero gallery is a **model implementation**:

```html
<img … alt="Pesakit selesai rawatan gigi di Klinik Pergigian Everglo, Bandar Puteri Bangi">
<img … alt="" aria-hidden="true">   <!-- animation duplicate, correctly hidden -->
```

Unique keyword-natural alt text on real images; duplicates correctly marked decorative. The
same correct pattern is used for the insurance-panel marquee. Treatment icons, doctor
portraits, panel logos and video thumbnails all carry meaningful alt text.
