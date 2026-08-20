# On-Page SEO — 45/100

## Evidence from source

```html
<html lang="en-US">                                    <!-- page is 100% Bahasa Melayu -->
<title>Smile-Planner &#8211; Klinik Pergigian Everglo</title>   <!-- occurrence 1 -->
<title>Smile-Planner &#8211; Klinik Pergigian Everglo</title>   <!-- occurrence 2 -->
<meta name='robots' content='max-image-preview:large' />        <!-- WP default; no SEO plugin -->
<link rel="canonical" href="https://klinikpergigianeverglo.com/smile-planner/" />  <!-- correct -->
<!-- NO <meta name="description"> -->
<!-- NO og:* / twitter:* -->
```

## The page documents its own unshipped plan

Inside the hero widget:

> `WAJIB SET DI PERINGKAT PAGE (RankMath/Yoast/Elementor, bukan dalam widget ni):`
> `- Title tag : Klinik Gigi Bandar Puteri Bangi | Klinik Pergigian Everglo — Scaling, Braces, Whitening & Veneer`
> `- Meta desc : Klinik pergigian di Bandar Puteri Bangi, Kajang. Rawatan gigi teliti & mesra first-timer…`

Neither was set. The copy already exists — it just needs pasting into an SEO plugin.

## Heading inventory

- **H1 × 1** — `Bukan Sekadar Rawat Gigi. "Kami Bantu Anda Senyum Lebih Yakin."` (no keyword)
- **H2 × 17** — including one **completely empty** `<h2></h2>` in the footer
- **H3** — pain cards (4), planner steps (4), treatments (6), doctors (2)
- **H4 × 7** — video playlist titles, nested under `<h2>Playlist</h2>` (skips H3)

## Link inventory (entire page)

| Type | Count | Targets |
|---|---|---|
| Internal | 2 | `/term-of-services/`, `/privacy-policy/` |
| External | 1 | `srsadvertisement.com` (dofollow) |
| On-page anchors | 4 | all `#form` |
| Logo linked? | No | `logo-everglo2.png` is a bare `<img>` |

Template is `elementor_canvas` → no site header, no menu, no site footer. The page is a
crawl dead-end.
