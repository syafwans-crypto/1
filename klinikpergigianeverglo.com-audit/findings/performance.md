# Performance — 35/100 · PROVISIONAL

> **Do not act before re-measuring logged out.** WP Rocket does not optimise for logged-in
> users, so minification, combination and JS-delay are absent from this capture. No CrUX
> field data and no lab run were possible. Treat 35 as unmeasured.

The findings below are **plugin-driven** and will largely persist for public visitors.

## High — vendor libraries for features the page never uses

Loaded by Happy Elementor Addons (free + Pro) and Royal Elementor Addons:

`three.min.js` · `gsap` · `TweenMax` · `ScrollMagic` · `motionpath` · `anime.js` ·
`Chart.js` · `plyr` · `swiper-bundle` · `owl.carousel` · `multiscroll` · `slick` ·
`isotope` · `magnific-popup` · `justifiedGallery` · `twentytwenty` · `datatables` ·
`prism` · `pdfobject` · `circlr` · `select2` · `alpinejs` · `rangeslider` ·
`hover-effect.umd` · **`fullcalendar` + `locales-all.min.js`**

The page uses: a hero, cards, an accordion, a form, a video playlist. `locales-all.min.js`
ships every locale on earth for a calendar that does not exist here.

**Largest single lever available.** Configuration problem, not a code problem. Test on staging.

## High — four Google Font families, all weights

| Family | Weights | Source |
|---|---|---|
| Roboto | 100–900 + all italics | Elementor kit |
| Roboto Slab | 100–900 + all italics | Elementor kit |
| Poppins | 300–800 | custom section 1 |
| Poppins | 400,600,700,800 | custom section 2 (duplicate request) |
| Inter, Cardo | — | theme, self-hosted |

Three independent typography systems; the Elementor pair is almost certainly unused here.

## Medium — unpinned CDN dependency

```html
<script id="alpine-js" src="//unpkg.com/alpinejs?ver=3.22.0"></script>
```
`ver` is a WordPress cache-buster, **not a version pin** — this resolves to `alpinejs`
*latest*. Reliability and supply-chain exposure on a live site. Same pattern for
`cdn.jsdelivr.net` and `cdnjs.cloudflare.com` scripts.

## Medium — competing LCP candidates

Both hero columns declare:
```html
<img fetchpriority="high" … loading="eager" fetchpriority="high" decoding="async">
```
Two high-priority images compete; neither is likely the true LCP element (the H1 text
probably is). Note `fetchpriority` is duplicated on the same tag.

## Medium — oversized images (developer's own to-do)

Source comment: *"NOTA PENJIMATAN TERBESAR … penjimatan boleh capai 80-90%"* — with
`[TUKAR-URL]` markers in four sections. None executed.

- 8 × `Testimoni*.png` @ 1024×1024, displayed small
- `IMG_7124-scaled.jpg` (≤2560px) displayed ~520px
- 10 gallery images at full size, displayed 190–280px
- Floating decorations using `-scaled.png` at 44–90px display
- `IMG_2951-1.png`, `IMG_2953.png` — PNG photographs

## Done well

`content-visibility: auto` + `contain-intrinsic-size` · Font Awesome → inline SVG ·
cache-reusing duplicate URLs · `IntersectionObserver` deferral · `prefers-reduced-motion`
respected · explicit `width`/`height` preventing CLS.
