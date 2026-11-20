#!/usr/bin/env python3
"""Build the Infinity Dental "Instagram Stories" landing page.

Outputs (next to this file):
  preview.html               local preview (assets/ paths + a mock booking form)
  elementor-html-widget.html the fragment that goes into ONE Elementor HTML widget
  infinity-stories-elementor.json  importable Elementor template (HTML + Shortcode widgets)

Usage:
  python3 build.py                     # assets resolved to ./assets/
  python3 build.py media-map.json      # assets resolved to WordPress media URLs
media-map.json maps asset file name -> absolute URL (written by the upload step).
"""
import json, re, sys, uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = (HERE / "story.src.html").read_text(encoding="utf-8")
FORM_SHORTCODE = '[fluentform id="3"]'

mapping = {}
if len(sys.argv) > 1:
    mapping = json.loads(Path(sys.argv[1]).read_text())


def resolve(html, base_map):
    def rep(m):
        name = m.group(1)
        if base_map is None:
            return f"assets/{name}"
        if name not in base_map:
            sys.exit(f"missing media URL for {name}")
        return base_map[name]
    return re.sub(r"\{\{A:([^}]+)\}\}", rep, html)


MOCK_FORM = """
<div id="ids-form-src" style="display:none">
  <form class="frm-fluent-form" onsubmit="event.preventDefault();alert('Preview sahaja: borang sebenar FluentForm akan dipaparkan di WordPress.')" style="display:grid;gap:10px">
    <input placeholder="First Name" style="padding:12px;border:1px solid #cdb97f;border-radius:8px">
    <input placeholder="Nombor Whatsapp" style="padding:12px;border:1px solid #cdb97f;border-radius:8px">
    <select style="padding:12px;border:1px solid #cdb97f;border-radius:8px">
      <option>- Select -</option><option>Year End Smile Care</option><option>Scalling and polishing</option>
      <option>Whitening</option><option>Braces</option><option>Clear Aligners</option><option>Comprehensive Smile Assesment</option>
    </select>
    <button class="ff-btn-submit" type="submit">Submit Form</button>
  </form>
</div>
"""

# 1) local preview
preview = resolve(SRC, None).replace("<!--FORM PREVIEW-->", MOCK_FORM)
(HERE / "preview.html").write_text(preview, encoding="utf-8")

# 2) widget fragment (only what is between the APP markers)
m = re.search(r"<!--APP START-->(.*)<!--APP END-->", SRC, re.S)
fragment = m.group(1).strip()
widget = resolve(fragment, mapping if mapping else None)
(HERE / "elementor-html-widget.html").write_text(widget, encoding="utf-8")


# 3) Elementor template: container > [HTML widget, Shortcode widget (#ids-form-src)]
def eid():
    return uuid.uuid4().hex[:7]


zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
elementor_data = [{
    "id": eid(), "elType": "container", "isInner": False,
    "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero,
                 "background_background": "classic", "background_color": "#0F0B07"},
    "elements": [
        {"id": eid(), "elType": "widget", "widgetType": "html", "elements": [],
         "settings": {"html": widget}},
        {"id": eid(), "elType": "widget", "widgetType": "shortcode", "elements": [],
         "settings": {"shortcode": FORM_SHORTCODE, "_element_id": "ids-form-src"}},
    ],
}]
(HERE / "elementor-data.json").write_text(json.dumps(elementor_data, ensure_ascii=False), encoding="utf-8")
template = {"version": "0.4", "title": "Infinity Dental – Year End Smile Story", "type": "page",
            "page_settings": {"template": "elementor_canvas", "hide_title": "yes"},
            "content": elementor_data}
(HERE / "infinity-stories-elementor.json").write_text(json.dumps(template, ensure_ascii=False, indent=1), encoding="utf-8")
print("built:", "preview.html", "elementor-html-widget.html", "elementor-data.json", "infinity-stories-elementor.json",
      "| widget bytes:", len(widget.encode()))
