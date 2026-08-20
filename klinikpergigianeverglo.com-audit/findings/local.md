# Local SEO — brick-and-mortar dental clinic

Business type: **Dentist**, single location, Bandar Puteri Bangi / Kajang, Selangor.

## Critical — NAP is inconsistent *within the page itself*

| Source | Locality stated |
|---|---|
| JSON-LD `streetAddress` | Bandar **Bukit Mahkota** |
| FAQ answer | Bandar **Puteri Bangi** |
| Hero eyebrow | Bandar **Puteri Bangi** |

Postcode/city agree (43000 Kajang, Selangor) and the phone is consistent
(`+60-11-6264-9191` ≡ WhatsApp `601162649191`). But the locality mismatch alone is enough to
weaken entity matching. Pick whichever exactly matches the **Google Business Profile** and
propagate everywhere.

## High — no visible NAP anywhere on the page

- Address appears **only** inside a collapsed `<details>` FAQ answer
- Phone appears **only** inside the WhatsApp widget's JSON config — never as readable text
- Opening hours appear **only** in JSON-LD
- No Google Maps embed, no directions link

For a local business this should be visible text in the footer of every page.

## Medium — no `sameAs` to consolidate the local entity

The clinic has an active TikTok (`@klinikpergigianeverglo`), Facebook and Instagram presence
plus a Google Maps listing. None are declared.

## Medium — no `geo` coordinates, no `priceRange`

Both are standard `LocalBusiness` properties and both are absent.

## Strengths

- `areaServed` is well chosen: Bandar Puteri Bangi, Bangi, Kajang, Bandar Seri Putra,
  Bukit Mahkota, Nilai, Semenyih
- `openingHoursSpecification` covers all 7 days (Mon–Fri 09:00–18:00, Sat–Sun 09:00–17:00),
  matching the reviews that praise public-holiday opening
- `paymentAccepted` lists locally relevant methods (Atome, Grab PayLater, panel insurance)
- 26 real Google reviews on-page (though JS-injected — see `geo.md`)

## Not assessed

Google Business Profile completeness · citation consistency across Malaysian directories ·
map-pack position · review velocity — all require network access.
