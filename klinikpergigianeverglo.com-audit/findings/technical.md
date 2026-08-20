# Technical SEO — 58/100

## Capture caveat

`_wp_http_referer` = `/smile-planner/?preview_id=2090&preview_nonce=…&preview=true` and
`body class="… logged-in admin-bar"`. This is an **admin preview**, so:

- Admin-only assets present here will not load publicly: Elementor `dev-tools`,
  `app-loader`, `finder`, `web-cli`, `notes`, `admin-bar`, `wp-api`, backbone/marionette,
  WPCode admin bar.
- **WP Rocket skips logged-in users** — the public page is probably minified/combined.

## Findings

| Severity | Finding |
|---|---|
| High | `<html lang="en-US">` on Malay content |
| Medium | Reviews + testimonial deck are JS-injected, absent from raw HTML |
| Medium | Duplicate `<meta name="viewport">` (theme + Elementor) |
| Medium | No breadcrumbs, no `BreadcrumbList` |
| Low | `wccp_free` copy-protection blocks selecting the clinic's address/phone |

## Not assessed (no network access)

robots.txt · XML sitemap · HTTP status & redirects · security headers · mobile usability
· rendered-DOM verification · CrUX field data · Search Console indexation

## Non-SEO observations from the admin bar

- **Novamira MCP — "AI Abilities: On"** on a production site. The plugin's own dialog warns:
  *"This looks like a production site. AI Abilities are intended for staging or development
  sites."* Worth a deliberate decision, not a default.
- **26 pending plugin updates.**
- **53 comments in moderation** — near-certainly spam; comments should be off on a brochure site.
