# Smile Upgrade Planner 2026 — Elementor Template (pixel-faithful)

Elementor page template for the "Smile Upgrade Planner 2026" landing page
(Klinik Pergigian Everglo), converted from the Claude Design source so it
renders **identically** to the original design.

`preview.png` shows the rendered output.

## Approach — why this looks exactly like the design

Elementor's free widgets can't reproduce the design's exact CSS (gradients,
badges, floating cards, custom spacing), so instead of rebuilding it widget by
widget, this template keeps each design section's **original HTML + inline CSS
intact inside Elementor HTML widgets**. The result is pixel-for-pixel the same
as Claude Design, while every section remains a separate, rearrangeable
Elementor block.

- **Fonts**: Poppins + Roboto load from Google Fonts (CDN).
- **Icons**: Font Awesome 6.5 loads from CDN.
- **Brand colors**: promoted to `:root` CSS variables (`--blue`, `--navy`, …).
- **The 5 photos** that were embedded in the design with no public URL
  (hero, 2 social-proof photos, clinic interior, Dr. Farah) are inlined as
  optimized **data-URI JPEGs** — so the file is fully self-contained and needs
  **no media upload**. Originals are in `assets/` for reference.

## How to import

1. WordPress admin → **Templates → Saved Templates**.
2. Click **Import Templates** (top of the page).
3. Upload `smile-planner-elementor.json`.
4. Edit any page with Elementor → folder icon → **My Templates** → insert it.

> If import times out, it's a server (LiteSpeed/PHP) limit, not the file.
> This version is structurally light (17 HTML-widget sections, ~50 elements
> vs. 179 before) so it imports far faster than a full native-widget rebuild.
> If it still stalls, raise PHP `max_execution_time`/memory or ask your host
> to increase the LiteSpeed connection timeout.

## What still needs the live site

These reference the live `klinikpergigianeverglo.com` URLs and appear blank
only in an offline preview — they load normally once the page is on your site:

- Partner/panel logo marquee
- Clinic gallery (9 photos)
- YouTube video testimonials
- Footer logo

## Lead form

The lead section keeps the `[fluentform id="3"]` shortcode inline. It renders
your real FluentForm once the FluentForm plugin is active.
