# Infinity Dental: "Instagram Stories" advertorial (Year End Smile Care)

Live: https://kpinfinitydental.com/year-end-smile-care/ (WordPress page ID 2524, Elementor, template `elementor_canvas`)

A full-screen, tap-through story landing page modelled on the Jüced
"advertorial as Instagram Stories" format: segmented progress bar, back button,
"Terus ke promo" skip, one big CTA per slide, ending in an offer picker and a
booking bottom sheet.

## Slides (12)
1. Hook: "Gosok gigi 2x sehari. Tapi kenapa masih nampak kusam?"
2. Problem: plaque → tartar, a toothbrush can't remove it
3. Agitate: signs people ignore
4. Insight: bersih ≠ putih (scaling / polishing / whitening / fluoride)
5. Reveal: 4-in-1 Smile Care package
6. Compare toggle: RM460 harga biasa → RM300 pakej (auto-animates)
7. Real results: before/after from @kpinfinitydental (whitening 15 min, S22→S14)
8. Clinic visit steps (auto stepper) on the real reception photo
9. Who it's for
10. "Kad semakan": report-card table built from real Google reviews
11. Real Google reviews carousel (from IG/LP, verbatim, shortened)
12. Offer: 4-in-1 RM300 · Smile Assessment from RM50 · Braces from RM200/bln

## Lead capture
- **Tempah slot saya** opens a bottom sheet holding the site's real FluentForm
  (`[fluentform id="3"]`, rendered by an Elementor Shortcode widget with CSS ID
  `ids-form-src`, moved into the sheet by JS). The treatment dropdown is
  pre-selected from the chosen package.
- **WhatsApp kami terus** opens the site's Click to Chat **Greetings Form**
  (keeps the existing CRM / fbp / fbc / gclid flow), with the pre-filled message
  set to the chosen package. Falls back to `wa.me/60182979390` if the plugin is off.
- The floating Click to Chat button is hidden only while the story is open, so it
  never covers the CTA.
- `dataLayer` events: `story_slide`, `story_skip`, `story_pick`,
  `story_book_open`, `story_whatsapp`, `story_form_submit`.
- `#promo` in the URL opens the offer slide directly.

## Background music
- Track: **"The Brave Smile Serenade"** (Magnific music generator, Lyria 3), made for
  a dental "overcoming fear" story ad. Re-cut into a 30.2 s seamless loop
  (0.6 s tail→head crossfade, loudness-normalised, 128 kbps, 473 KB):
  `assets/infinity-story-bg-music.mp3` → WP media ID 2528.
- Starts on the visitor's first tap (browsers block autoplay with sound), fades in,
  loops gaplessly via Web Audio (falls back to `<audio loop>`).
- 🔊/🔇 button in the top bar; the choice is remembered (`localStorage ids_music`).
  Music ducks while the booking sheet is open and pauses when the tab is hidden.
  `dataLayer` event `story_sound` (on/off).

## Files
- `story.src.html`: source (HTML/CSS/JS, `{{A:file}}` asset tokens)
- `build.py`: builds `preview.html` (local), `elementor-html-widget.html`,
  `elementor-data.json` and `infinity-stories-elementor.json`
  (`python3 build.py media-map.json` resolves assets to the WordPress media URLs)
- `assets/`: optimised images. AI images were generated with Magnific; the
  before/after photos and reception photo come from @kpinfinitydental (the
  reception photo was upscaled with Magnific)
- `media-map.json`: asset → WordPress media URL (IDs 2511–2523, music 2528)

## Updating the live page
Edit `story.src.html`, run `python3 build.py media-map.json`, then write
`elementor-data.json` to the page's `_elementor_data` meta and **save the
document through Elementor** (e.g. the MCP `elementor-update-page-settings`
tool) so Elementor's element cache is refreshed.

Generated images are illustrative (disclosed on slide 1 and the offer slide).
Pricing and claims come from the clinic's current ads and Instagram, so confirm
them with the clinic before scaling spend.
