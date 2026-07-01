# Smile Upgrade Planner 2026 — Elementor Template

Elementor-editable version of the "Smile Upgrade Planner 2026" landing page
for Klinik Pergigian Everglo, converted from the Claude Design source file
(`templates/smile-planner/SmilePlanner.dc.html`).

## What's here

- `smile-planner-elementor.json` — an Elementor **page template** (16 sections,
  179 elements) built entirely from native **free** Elementor widgets:
  heading, text-editor, button, icon-list, icon-box, image, image-gallery,
  video, testimonial, accordion, shortcode. No Elementor Pro required.
- `assets/` — 5 images that were embedded directly in the design file (no
  public URL): `hero.jpg`, `social-proof-1.jpg`, `social-proof-2.jpg`,
  `clinic-experience.jpg`, `dr-farah.png`.

## How to import

1. In WordPress, go to **Templates → Saved Templates → Import Templates**
   (or, when editing/creating a page, open Elementor and use
   **Folder icon → Import Template**).
2. Upload `smile-planner-elementor.json`.
3. Insert the imported template into a new/existing page.

## After import — fix the 5 placeholder images

The JSON references these under a placeholder path
(`REPLACE_WITH_YOUR_SITE/wp-content/uploads/smile-planner/...`) because the
original design file embedded them as inline data with no public URL.
Elementor template exports never embed binary images either way — they
always point at Media Library URLs — so this step is normal for any
imported template with foreign images, not specific to this conversion:

1. Upload the 5 files in `assets/` to your WordPress Media Library.
2. In Elementor, click each broken image (Hero, the 2 social-proof photos,
   the Clinic Experience photo, Dr. Farah's photo) and reselect it from the
   Media Library.

All other images (clinic gallery, partner logos, footer logo) already point
at the live `klinikpergigianeverglo.com` URLs from the original design and
need no changes.

## Fonts & colors

The template uses **Poppins** (headings) and **Roboto** (body) with inline
typography settings matching the brand palette:

| Token  | Hex       | Token  | Hex       |
|--------|-----------|--------|-----------|
| Navy   | `#0F2F44` | Mint   | `#7EDDD3` |
| Blue   | `#0EA5C6` | Grey   | `#F6FAFB` |
| Sky    | `#EAF9FC` | CTA    | `#FF6B5A` |

Elementor will auto-load Poppins/Roboto from Google Fonts — no extra font
setup needed.

## Known simplifications vs. the original design

Elementor's free widgets don't support arbitrary CSS, so a few visual
details from the original HTML were adapted rather than pixel-matched
(everything below is freely re-editable after import):

- The rotating logo **marquee** is a static 4-up image gallery instead of
  an animated strip.
- The two floating badges over the hero photo ("5.0 Google rating",
  "Mesra first-timer") are a stacked icon-list under the image rather than
  absolutely-positioned overlays.
- The numbered "1–4" Smile Upgrade Planner steps use plain numerals in the
  heading text instead of custom number badges.
- The `[fluentform id="3"]` lead form is inserted via Elementor's
  **Shortcode** widget, unchanged — it will render your real FluentForm
  once the plugin is active.
