# SEO Audit — klinikpergigianeverglo.com/smile-planner/

**Date:** 2026-08-20
**Scope:** Single URL, supplied HTML source
**Business type detected:** Local Service — brick-and-mortar dental clinic (Dentist), Bandar Puteri Bangi / Kajang, Selangor, Malaysia. YMYL health content.
**SEO Health Score: 53 / 100**

---

## Important caveats on this audit

**1. The HTML supplied is a logged-in admin preview, not the public page.**
Evidence: `body class="... logged-in admin-bar"`, the full `#wpadminbar` markup, and
`_wp_http_referer` = `/smile-planner/?preview_id=2090&preview_nonce=…&preview=true`.

Consequences:
- Admin-only assets (Elementor `dev-tools`, `app-loader`, `finder`, `web-cli`, `notes`,
  `admin-bar`, `wp-api`, backbone/marionette, WPCode admin bar) are present here but will
  **not** load for public visitors. They are excluded from the findings below.
- **WP Rocket does not optimise pages for logged-in users.** The public page is likely
  minified/combined and may delay JS. Therefore all **Performance findings are provisional**
  and must be re-verified on a logged-out render or via PageSpeed Insights.

**2. Not assessed** (no network access from the audit environment; the site is blocked by
this environment's egress policy): robots.txt, XML sitemap, HTTP status/redirects, security
headers, Core Web Vitals field data (CrUX), indexation status (GSC), backlinks, SERP
positions, rendered-DOM verification, screenshots. These are marked "Not assessed" rather
than estimated.

**3. Scope.** One URL only. No crawl was possible, so site-wide issues (duplicate titles
across pages, orphan pages, sitemap coverage) are out of scope.

---

## Executive summary

The page is genuinely well-built in places — the hero image alt text is descriptive and
correctly distinguishes decorative duplicates (`alt="" aria-hidden="true"`), `content-visibility: auto`
is used properly, Font Awesome webfonts were replaced with inline SVG, and there is a
detailed `Dentist` JSON-LD block with services, hours and service areas. Someone competent
worked on this.

The problem is that the page's own source code documents an SEO plan that was never
executed. Inside the hero widget there is a comment reading:

> `WAJIB SET DI PERINGKAT PAGE (RankMath/Yoast/Elementor, bukan dalam widget ni):`
> `- Title tag : Klinik Gigi Bandar Puteri Bangi | Klinik Pergigian Everglo — Scaling, Braces, Whitening & Veneer`
> `- Meta desc : Klinik pergigian di Bandar Puteri Bangi, Kajang…`

Neither was ever set. The page ships with the WordPress default title
`Smile-Planner – Klinik Pergigian Everglo` and **no meta description at all**. The same
pattern repeats: `[TUKAR-URL]` image-resizing to-dos left unactioned in four separate
sections. The build was finished; the SEO checklist was not.

### Top 5 critical / high-severity issues

1. **No meta description** anywhere in `<head>`. Google will scrape arbitrary body text.
2. **Duplicate `<title>` tags** — the tag appears twice, and the title itself is a slug
   artefact (`Smile-Planner`) carrying no keyword or location.
3. **`<html lang="en-US">` on a page written entirely in Bahasa Melayu.** The language
   declaration contradicts the content.
4. **Almost no internal links** — 2 outbound internal links on the entire page
   (T&C, Privacy). Six treatments are named; none link anywhere. The logo is not a link.
5. **NAP conflict inside the page itself** — JSON-LD says `Bandar Bukit Mahkota`, the FAQ
   and hero say `Bandar Puteri Bangi`. Address and phone appear nowhere in visible page
   text except buried in a collapsed FAQ answer.

### Top 5 quick wins (under an hour each)

1. Set the title + meta description already written in the source comment.
2. Change site/page language to `ms_MY` (fixes `lang` attribute).
3. Add Open Graph + Twitter Card tags — this page's traffic is Meta/TikTok/WhatsApp ads,
   and link previews currently have nothing to render.
4. Fill the 15 empty `alt` attributes, especially the four promo images.
5. Add `sameAs` (Facebook, Instagram, TikTok, Google Maps) to the existing JSON-LD.

---

## Category scores

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 58 | 12.76 |
| Content Quality | 23% | 62 | 14.26 |
| On-Page SEO | 20% | 45 | 9.00 |
| Schema / Structured Data | 10% | 55 | 5.50 |
| Performance (CWV) | 10% | 35 *(provisional)* | 3.50 |
| AI Search Readiness | 10% | 55 | 5.50 |
| Images | 5% | 48 | 2.40 |
| **Total** | | | **52.92 → 53** |

Because the Performance component is provisional (see caveat 1), the true total could move
roughly ±4 points once a logged-out render is measured.

---

## 1. On-Page SEO — 45/100

### Critical: no meta description
There is no `<meta name="description">` in `<head>`. No SEO plugin (Yoast / RankMath / SEOPress)
is emitting meta output — the only robots directive is WordPress's default
`<meta name='robots' content='max-image-preview:large' />`. Use the description already
drafted in the hero comment.

### Critical: duplicate `<title>` tag
`<title>Smile-Planner &#8211; Klinik Pergigian Everglo</title>` appears **twice** — once
immediately after the `<style>` block near the top of `<head>`, and again after the WordPress
preview script. Duplicate title elements are invalid HTML; browsers and parsers take the
first and discard the rest, but it signals a template/plugin conflict worth tracing.

The title content is also weak: "Smile-Planner" is a URL slug rendered as a title, with no
service keyword and no location. Recommended (from the source comment, lightly trimmed to
fit ~60 chars):
`Klinik Gigi Bandar Puteri Bangi | Everglo — Braces, Scaling, Veneer`

### High: H1 contains no target keyword
The single H1 is:
`Bukan Sekadar Rawat Gigi. "Kami Bantu Anda Senyum Lebih Yakin."`

Emotionally strong, semantically empty. The keywords sit directly above it in a `<p class="evg-eyebrow">`
("Klinik Pergigian Everglo @ Bandar Puteri Bangi, Kajang"). Work location + primary service
into the H1 itself, or promote the eyebrow's content into it.

Heading structure is otherwise sound — exactly one H1, then H2 section heads, H3 card titles.
Two defects:
- The footer contains an **empty `<h2></h2>`** (`<h2 style="margin: 6px 0 0; …; color: #fff;"></h2>`).
  Delete it.
- The video playlist widget emits `<h4>` tab titles under an `<h2>Playlist</h2>`, skipping H3.
  Cosmetic; low priority.

### High: internal linking is effectively absent
The entire page links to exactly **two** internal URLs — `/term-of-services/` and
`/privacy-policy/` — plus one external dofollow link to `srsadvertisement.com` (the agency).
Every call-to-action is an on-page `#form` anchor.

The page names six treatments (Braces, Scaling & Polishing, Whitening, Crown & Bridge,
Denture, Consultation) and the site is known to have at least `/veneers/` and `/landing-page/`.
None are linked. The Everglo logo image is not wrapped in an `<a>` — there is no link home.

This page is built on the `elementor_canvas` template (`page-template-elementor_canvas`),
which strips the site header and footer, so there is **no navigation whatsoever**. Combined
with the lack of body links, the page is a crawl dead-end: link equity flows in and stops.

### Medium: URL slug
`/smile-planner/` is an English slug on a Malay page targeting Malay-language local queries.
Changing it now costs a redirect and risks the existing (recent) indexation. Recommendation:
**keep the URL**, fix the title/meta/H1 instead. Revisit only if the page is rebuilt.

### Not assessed
Canonical is correctly self-referencing (`https://klinikpergigianeverglo.com/smile-planner/`) ✓.
Indexability looks fine (no `noindex`), but actual index status requires Search Console.

---

## 2. Technical SEO — 58/100

### High: wrong language declaration
`<html lang="en-US">` while 100% of visible copy is Bahasa Melayu. Fix via WordPress
Settings → Site Language → `Bahasa Melayu`, or filter `language_attributes()`. This affects
screen readers, translation behaviour, and how search engines and LLMs classify the page.

### Medium: duplicate `<meta name="viewport">`
Two viewport tags are emitted:
`width=device-width, initial-scale=1` (WordPress/theme) and
`width=device-width, initial-scale=1.0, viewport-fit=cover` (Elementor, later in `<head>`).
Harmless in practice, but indicates two systems fighting over the same tag.

### Medium: key content is injected by JavaScript and absent from raw HTML
Two of the page's strongest trust assets are **not in the HTML source**:
- The **26 Google reviews** (names, dates, full review text) are held in a JS array and
  injected into `#tc` only when an `IntersectionObserver` fires with `rootMargin: '600px 0px'`.
- The **10-image testimonial deck** (`#evgDeck`) is likewise built only on intersection.

Googlebot renders JavaScript and will very likely pick these up. But crawlers that do not
execute JS — including most LLM retrieval crawlers — will see empty containers. See §6.

### Medium: no breadcrumbs
No breadcrumb trail and no `BreadcrumbList` schema. On a canvas-template page with no
navigation, breadcrumbs would be the only orientation signal for users and crawlers.

### Low: content protection plugin
`wccp_free` (WP Content Copy Protection / no right-click) is active. It does not block
Googlebot, but it degrades UX (blocked selection/copy) for legitimate visitors wanting to
copy the clinic address or phone number.

### Not assessed
robots.txt, XML sitemap presence and coverage, HTTP status codes, redirect chains, HSTS and
security headers, mobile usability testing, JS-rendered DOM verification.

### Non-SEO note worth raising
The admin bar shows a **Novamira MCP plugin with "AI Abilities: On"**, and the plugin's own
confirmation dialog reads *"This looks like a production site. AI Abilities are intended for
staging or development sites."* A plugin exposing write-capable AI abilities on a live
clinic site handling patient enquiry data deserves a deliberate decision rather than being
left on by default. Also visible: **26 pending plugin updates** and **53 comments in
moderation** (almost certainly spam — comments should be disabled on a brochure site).

---

## 3. Content Quality & E-E-A-T — 62/100

### What works
- Substantial, original, non-templated Malay copy that speaks to real patient anxieties
  ("takut sakit, takut kena judge, risau kos rawatan").
- **Named practitioners with bios** — Dr. Farah Fatah (Pengarah & Doktor Gigi, ~10 years)
  and Dr. Najmina. Named humans are a strong E-E-A-T signal.
- 26 verbatim Google reviews with reviewer names and recency.
- 9 genuine FAQs answering real pre-visit objections, present in raw HTML inside `<details>`.
- Appropriate medical hedging: *"Cadangan rawatan bergantung kepada pemeriksaan doktor."*

### High: YMYL page with no professional credentials
This is health content. Neither doctor lists a qualification (BDS/DDS) or, more importantly
for Malaysia, a **Malaysian Dental Council (MDC) registration number**. There are no links to
individual practitioner bio pages, no `Person` schema, and no "medically reviewed by" line.
For a YMYL query set, this is the single biggest content-side gap.

### High: no visible NAP block
The clinic's address appears **only inside a collapsed FAQ answer**. The phone number appears
only inside the WhatsApp widget's JSON config (`601162649191`) — not as readable text.
Opening hours appear only in JSON-LD. There is no Google Maps embed and no directions link.

For a brick-and-mortar local business, address + phone + hours should be visible text in the
footer of every page.

### Medium: testimonials are images of text
The eight `Testimoni*.png` images and the ten-image `#evgDeck` are screenshots of written
testimonials. That text is invisible to search engines and to AI systems. The 26 HTML
reviews partially compensate — but those are JS-injected (§2).

### Medium: treatment descriptions are one line each
Each of the six treatments gets a single sentence ("Untuk bantu susunan gigi yang tidak
teratur."). There is no depth on process, duration, aftercare, or indicative pricing —
the questions patients actually search. This is thin for the commercial intent it targets.

### Low: promotional claims carry no terms
Four "Promo Bulan Ini" images (Whitening, Composite Veneer, Braces, Scaling) are pure images
with empty alt text. Offer terms, validity dates and pricing are unreadable to crawlers and
to screen-reader users, and unindexable as content.

---

## 4. Schema / Structured Data — 55/100

One JSON-LD block, `@type: Dentist`. It is more thorough than most clinic sites — services
as `MedicalProcedure`, `openingHoursSpecification`, `areaServed`, `paymentAccepted`,
`knowsLanguage`, and a smart `alternateName` array capturing real misspellings
("Everglow Dental") observed in Search Console.

### High: address inside schema contradicts the page
```
schema  : "streetAddress": "8, Jalan Puteri 2A/3, Bandar Bukit Mahkota"
FAQ     : "No 8 (GF), Jalan Puteri 2A/3, Bandar Puteri Bangi, 43000 Kajang, Selangor"
hero    : "Klinik Pergigian Everglo @ Bandar Puteri Bangi, Kajang"
```
`Bandar Bukit Mahkota` vs `Bandar Puteri Bangi`. These are adjacent localities, so both may
be loosely true — but structured data, on-page text and the Google Business Profile must
state **one** identical address. NAP inconsistency directly suppresses map-pack ranking.

### High: self-serving `aggregateRating`
```json
"aggregateRating": { "ratingValue": "5.0", "reviewCount": "381" }
```
Google has not shown review rich results for self-serving `LocalBusiness`/`Organization`
markup since 2019, and marking up a rating the business asserts about itself, without
corresponding `Review` items, falls foul of the structured-data guidelines. The rating is
almost certainly real (it matches the on-page Google Reviews badge) — but the markup will
not earn stars and carries a non-zero spam-flag risk.

Options, in order of preference: (a) remove `aggregateRating`; (b) keep it but add individual
`Review` objects for reviews actually displayed on the page; (c) rely on the Google Business
Profile, which is where these reviews legitimately live and already surfaces them.

### Medium: `FAQPage` schema missing despite nine real FAQs
The FAQs are already marked up semantically with `<details>/<summary>`. Adding `FAQPage`
JSON-LD is near-zero effort.

Be realistic about the payoff: since August 2023 Google restricts **FAQ rich results** to
authoritative government and health *institutional* sites, so a private clinic should not
expect star-style SERP expansion. The value here is **machine extraction** — ChatGPT,
Perplexity and AI Overviews parse `FAQPage` reliably. Worth doing for GEO, not for stars.

### Medium: no `VideoObject` for seven embedded videos
Seven YouTube videos (braces comparison, crowns, veneers, dentures, root canal) are embedded
via the Elementor playlist. No `VideoObject` markup, so no video rich results and no
key-moments eligibility.

### Medium: no `sameAs`
The source comment even says *"Pilihan: tambah link Facebook/Instagram/Google Maps dalam sameAs"*
— never done. The clinic has an active TikTok (`@klinikpergigianeverglo`), Facebook and
Instagram presence. `sameAs` is the primary mechanism for consolidating a brand entity in
Google's Knowledge Graph and in LLM entity resolution. Cheapest high-value schema fix available.

### Low: schema describes the org, not this page
`"url"` points at the homepage `/`, not this URL. There is no `@id`, no `WebPage` node, and
no `Service` node for the "Smile Upgrade Planner" the page is actually about. Consider a
`@graph` with `WebPage` → `about` → `Dentist`, plus `geo` coordinates and `priceRange`.

---

## 5. Performance — 35/100 *(provisional — see caveat 1)*

**Re-verify logged out before acting.** WP Rocket is installed and does not optimise for
logged-in users, so minification, combination and JS-delay are all bypassed in this capture.

That said, the following are plugin-driven and will largely persist for public visitors.

### High: vendor libraries loaded for features the page never uses
The Happy Elementor Addons (free + Pro) and Royal Elementor Addons stacks load, on every
page load, a library set including:

`three.min.js`, `gsap` + `TweenMax` + `ScrollMagic` + `motionpath`, `anime.js`, `Chart.js`,
`plyr`, `swiper-bundle`, `owl.carousel`, `multiscroll`, `slick`, `isotope`, `magnific-popup`,
`justifiedGallery`, `twentytwenty`, `datatables`, `prism`, `pdfobject`, `circlr`, `select2`,
`alpinejs`, `rangeslider`, `hover-effect.umd`, and **`fullcalendar` plus `locales-all.min.js`**.

This page uses a hero, cards, an accordion, a form and a video playlist. Essentially none of
the above is required. `locales-all.min.js` alone ships every locale on earth for a calendar
that does not exist on this page. This is the largest single performance lever available and
it is a plugin-configuration problem, not a code problem.

### High: four Google Font families, all weights
```
Roboto        : 100–900 + every italic  (Elementor kit)
Roboto Slab   : 100–900 + every italic  (Elementor kit)
Poppins       : 300–800                 (custom section 1)
Poppins       : 400,600,700,800         (custom section 2 — duplicate request)
```
plus locally hosted `Inter` and `Cardo` from the Twenty Twenty-Four theme. That is three
independent typography systems. The Elementor Roboto/Roboto Slab requests pull ~36 variants
and are almost certainly unused by these custom-HTML sections. Disable Elementor's Google
Fonts or pin to the weights actually used.

### Medium: unpinned third-party CDN dependency
`<script id="alpine-js" src="//unpkg.com/alpinejs?ver=3.22.0">` — the `ver` query string is a
WordPress cache-buster, **not** a version pin. This resolves to whatever `alpinejs` latest is
today. An unpinned, unversioned script from a third-party CDN on a production site is both a
reliability risk (a breaking release breaks the page) and a supply-chain exposure. Pin a
version or self-host. Same pattern applies to `cdn.jsdelivr.net` and `cdnjs.cloudflare.com`
dependencies loaded here.

### Medium: competing LCP candidates
Both hero columns declare a high-priority first image:
```html
<img fetchpriority="high" … loading="eager" fetchpriority="high" decoding="async">
```
Two `fetchpriority="high"` images compete for the same bandwidth, and neither is likely the
true LCP element (the H1 text probably is). Additionally the hero *background* is deliberately
deferred until after `window.load` and then faded in — which is good for LCP but produces a
visible late repaint.

Note the duplicated attributes: `fetchpriority` appears twice on the same tag, and
`loading="eager"` sits alongside it. Browsers honour the first and ignore the rest.

### Medium: oversized images (developer's own to-do, never actioned)
Four separate source comments flag this, e.g.:
> `NOTA PENJIMATAN TERBESAR (perlu buat manual dalam WordPress): … 10 gambar testimoni … dipaparkan hanya 210x210px … penjimatan boleh capai 80-90%`

Confirmed instances:
- 8 × `Testimoni*.png` at 1024×1024 for small display
- `IMG_7124-scaled.jpg` (WordPress `-scaled` = up to 2560px) displayed at ~520px
- 10 gallery images at full size, displayed ~190–280px
- Floating decorations (`*-scaled.png`) displayed at 44–90px
- `IMG_2951-1.png`, `IMG_2953.png` — PNG photographs, the heaviest possible format choice

Every `[TUKAR-URL]` marker in the source is an unexecuted resize.

### What is done well
`content-visibility: auto` with `contain-intrinsic-size` on most sections; Font Awesome
webfont replaced by inline SVG (saves ~250KB per the comments); marquee/deck duplicates reuse
identical URLs to hit cache; `IntersectionObserver` deferral of heavy sections;
`prefers-reduced-motion` respected throughout. This is thoughtful work.

### Not assessed
LCP / INP / CLS — no field data (CrUX) and no lab run possible. Do not treat 35 as measured.

---

## 6. AI Search Readiness (GEO) — 55/100

### What works
- `Dentist` schema with a rich natural-language `description` — highly extractable.
- `alternateName` covering misspellings ("Everglow Dental", "Everglo Dental Clinic") helps
  entity resolution when users ask an LLM about the clinic by an approximate name.
- Nine FAQs in raw HTML — directly citable Q&A passages.
- Explicit service list, service areas, payment methods, languages — exactly the attribute
  set an LLM needs to answer "is there a dentist near Bangi that takes Atome?"

### High: the review corpus is invisible to non-rendering crawlers
The 26 Google reviews are the page's richest citable content and they exist only in a
JavaScript array until an `IntersectionObserver` fires. GPTBot, PerplexityBot, ClaudeBot and
similar retrieval crawlers generally do **not** execute JavaScript. To them this section is
an empty `<div id="tc">`.

Fix: server-render the reviews into the HTML (they are static strings — there is no reason
for them to be JS-injected), and keep the observer only for the animation.

### Medium: no `FAQPage` / `Speakable` / `Review` markup
Covered in §4. For GEO specifically, `FAQPage` is the highest-value addition.

### Medium: no `sameAs`, no author entities
Without `sameAs`, an LLM cannot reliably connect this site to the clinic's TikTok/Facebook/
Instagram/Google Maps presence. Without `Person` schema for Dr. Farah and Dr. Najmina, the
practitioners are strings, not entities.

### Not assessed
`llms.txt` presence, AI crawler access in robots.txt (GPTBot/CCBot/PerplexityBot rules), and
actual citation rates in ChatGPT/Perplexity — all require network access.

---

## 7. Images — 48/100

### High: 15 content images with empty `alt`
All are Elementor image widgets where the Media Library alt field was never filled:

| Image | Note |
|---|---|
| `logo-everglo2.png` | brand logo — also not linked |
| `dental-treatment-768x768.png` | section illustration |
| `Testimoni1/2-1/3/4/5/6/8/9-4` (8 images) | testimonial screenshots |
| `Google-Review-Everglo.png` | review badge |
| `Whitening-Promo`, `Composite-Veneer-Promo`, `Brace-Promo`, `Scaling-Promo` | **offer content** |

The four promo images matter most: they are the page's commercial offers, and they are
entirely unreadable to search engines, LLMs and screen-reader users.

### Medium: gallery uses one duplicated alt string
All 10 gallery tiles carry the identical `alt="Galeri Everglo"`. Ten identical alts provide
no differentiation. Describe each: *"Bilik rawatan Klinik Pergigian Everglo"*,
*"Kaunter penyambut tetamu"*, etc.

### Low: duplicated HTML attributes
Many `<img>` tags repeat attributes, e.g.
`<img loading="lazy" src="…" alt="…" width="34" height="34" loading="lazy" decoding="async">`
and the hero's doubled `fetchpriority="high"`. Invalid HTML; the first occurrence wins.
No ranking impact, but it will confuse future maintenance and any automated auditing.

### What is done well — genuinely
The hero gallery is a model implementation: unique, descriptive, keyword-natural alt text on
the four real images ("Pesakit selesai rawatan gigi di Klinik Pergigian Everglo, Bandar
Puteri Bangi"), with the animation duplicates correctly marked `alt="" aria-hidden="true"`.
The same correct pattern is used for the insurance-panel marquee. Explicit `width`/`height`
on nearly every image prevents CLS. Treatment icons, doctor portraits and panel logos all
carry meaningful alt text.

---

## 8. Additional finding: corrupted video playlist configuration

The Elementor video-playlist widget's `data-settings` attribute contains malformed entries.
Markdown link syntax has leaked into the stored values:

```
"youtube_url":"https:\/\/[www.youtube.com\/watch?v=uIINNNuKXOg"      ← stray "["
"title":"Crown](https:\/\/www.youtube.com\/watch?v=uIINNNuKXOg"       ← markdown fragment as title
"title":"Gigi) Jonggang  - Cabut Atau Tidak"                          ← orphaned ")"
```

Someone pasted Markdown-formatted links into the widget's title/URL fields. The **rendered**
output is currently fine — the visible tabs show correct titles and the
`data-video-url` attributes are clean — so this is not user-facing today. But the stored
config now holds roughly double the intended entries (7 videos, ~13 config objects), it bloats
the DOM, and **re-saving the widget in Elementor may propagate the corruption to the front
end**. Repair the fields before anyone next edits that widget.

---

## Conversion notes (outside SEO scope, but visible)

- The lead form requires **Email**, on a page whose entire CTA language is WhatsApp-first
  ("Boleh WhatsApp kami dahulu"). For this audience, a required email field is friction.
  Consider making it optional.
- Submit button reads "Submit Form" — a generic English label in an otherwise Malay page.
- Address and phone are not clickable/visible anywhere as text (§3).
