# Schema / Structured Data — 55/100

One JSON-LD block: `@type: Dentist`. Better than most clinic sites — `MedicalProcedure`
services, `openingHoursSpecification`, `areaServed`, `paymentAccepted`, `knowsLanguage`, and
an `alternateName` array capturing real Search Console misspellings ("Everglow Dental").

## High — address contradicts the page

```
JSON-LD : "streetAddress": "8, Jalan Puteri 2A/3, Bandar Bukit Mahkota"
FAQ     : "No 8 (GF), Jalan Puteri 2A/3, Bandar Puteri Bangi, 43000 Kajang, Selangor"
Hero    : "Klinik Pergigian Everglo @ Bandar Puteri Bangi, Kajang"
```

Adjacent localities — but schema, on-page text and the GBP must state **one** identical
address. NAP inconsistency directly suppresses map-pack ranking.

## High — self-serving aggregateRating

```json
"aggregateRating": { "@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "381" }
```

Google has not shown review rich results for self-serving `LocalBusiness` markup since 2019,
and a business-asserted rating with no `Review` objects conflicts with the guidelines. The
rating is almost certainly real — it just won't earn stars, and carries some spam-flag risk.

Options: (a) remove it; (b) add `Review` objects for reviews shown on-page; (c) let the
Google Business Profile carry it, which is where these reviews legitimately live.

## Medium — missing markup

| Missing | Note |
|---|---|
| `FAQPage` | 9 FAQs already in `<details>`. **Realistic expectation:** since Aug 2023 Google limits FAQ rich results to authoritative gov/health institutional sites — a private clinic won't get stars. Value here is LLM extraction (GEO). |
| `VideoObject` | 7 YouTube videos embedded, zero markup |
| `sameAs` | Source comment suggests it; never added. Cheapest high-value fix. |
| `Person` | Both doctors are strings, not entities |

## Low — describes the org, not the page

`"url"` → homepage, not this URL. No `@id`, no `WebPage` node, no `Service` node for the
"Smile Upgrade Planner". No `geo`, no `priceRange`.
Suggested: `@graph` with `WebPage` → `about` → `Dentist`.
