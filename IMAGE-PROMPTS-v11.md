# Southern Point — Photography Prompts (v11)

Reference-matched image-generation prompts for the current site.

## Current status

Three slots are now **filled** with Dj's own AI-generated reference images (cropped, upscaled ~1.6–1.8×, sharpened, and in the technology image's case warm-graded toward the brand palette):

| Slot | File | Prompt below |
|---|---|---|
| Homepage hero, right panel | `assets/images/hero-houston-skyline.jpg` | 1 |
| Government Contracting hero | `assets/images/gc-infrastructure.jpg` | 2 |
| Industries → Technology hero | `assets/images/industry-technology.jpg` | 3 |

`assets/images/industrial-aerial.jpg` (the refinery shot) is in the repo but **not yet placed** — it's the natural fit for prompt 6, the Services hub.

Still open: Industries → Operations (prompt 4), About (prompt 5), Services hub (prompt 6).

Source images came in at 828px wide (phone-screenshot resolution), so they're a little soft at full-bleed desktop widths. Regenerating any of them at 1920px+ and dropping the file in under the same name would sharpen them with no code change.

## Why prompts, not finished images

This sandbox can't run image generation or download stock photography (confirmed blocked at the network level, same as every prior phase). So the path is: paste a prompt below into a free generator, save what you like, and upload the results back into this chat — I'll crop/compress/rename them to the exact slot and wire them into the page.

## Free tools that will run these prompts

- **Bing Image Creator / Microsoft Designer** — designer.microsoft.com — free with a Microsoft account, no card required, generous daily credits. Best all-around option for these.
- **Google ImageFX** — labs.google/fx/tools/image-fx — free with a Google account.
- **Adobe Firefly** — firefly.adobe.com — free tier with monthly credits, commercially safe to use (trained on licensed/public-domain content, matters if this ever gets scrutinized as a real business site).
- **Leonardo.ai** — free daily credits, more control over aspect ratio.

Any of these will work with the prompts as written. If a tool caps aspect ratio, generate the closest option and I'll crop to spec on my end.

## Style anchor (from your 4 reference images)

Your references — a data center/security operations scene, a bridge construction site, an aerial industrial/refinery complex at sunset, and a Houston skyline office interior — set the mood: large-scale, serious, infrastructure-and-enterprise subject matter, shot like real editorial/corporate photography, not stock-photo smiling-at-camera poses. I've carried that mood into every prompt below, but shifted the color grading toward Southern Point's own palette (warm midnight/burgundy/bronze, not the cool blue typical of security/tech stock photography) so whatever comes back sits naturally against the site instead of clashing with it.

Every prompt below already includes a "no text/no logo/no watermark" instruction and a realism instruction — AI generators are prone to inventing garbled signage (like the "InfraLock Systems" / "Desai Construction" labels baked into your reference images) and warped hands/faces, so re-roll a few times per prompt and pick the cleanest result rather than trying to prompt-engineer those artifacts away entirely.

---

## 1. Homepage hero — right panel

- **Slot:** Replaces the current CSS graphic panel in the split-screen hero (`_partials/build_index.py`, `.hero-visual`)
- **Crop needed:** Portrait-leaning, roughly 4:5 to 3:4. Generate at the highest resolution the tool allows; I'll crop to fit.
- **Prompt:**
  > Editorial corporate photograph, wide interior view of a modern high-rise office at dusk, floor-to-ceiling windows overlooking a warmly lit Houston skyline silhouette, a few professionals in soft-focus mid-conversation in the foreground, warm amber and deep burgundy ambient lighting mixed with cool blue dusk light through the windows, shallow depth of field, shot on a full-frame camera with a 35mm lens, photorealistic, high production value, no text, no logos, no signage, no watermark

## 2. Government Contracting — page hero

- **Slot:** `government-contracting/index.html` hero section (currently no image; dark text-only hero)
- **Crop needed:** Wide landscape, roughly 16:9 to 2:1
- **Prompt:**
  > Aerial editorial photograph of a large-scale civil infrastructure construction site at golden hour — a partially completed bridge or highway interchange, heavy equipment and structural steel visible, warm amber and bronze sunset light raking across concrete and steel, dramatic long shadows, slight haze, shot from a drone at a three-quarter angle, photorealistic, serious and monumental in scale, no text, no logos, no signage, no watermark, no visible workers' faces in close-up

## 3. Industries — Technology

- **Slot:** `/industries/technology/` hero or photo section
- **Crop needed:** Landscape, roughly 3:2
- **Prompt:**
  > Editorial photograph inside a modern data center or network operations center, rows of server racks with status LEDs, a technician in the mid-distance reviewing a monitoring dashboard on a large screen, warm amber and bronze accent lighting mixed with cool ambient blue from the equipment (keep the overall grade warm, not cold blue), shallow depth of field, photorealistic, serious and technical mood, no readable text on any screen, no logos, no signage, no watermark

## 4. Industries — Operations

- **Slot:** `/industries/operations/` hero or photo section
- **Crop needed:** Landscape, roughly 3:2
- **Prompt:**
  > Editorial photograph of a large logistics or industrial operations floor, wide shot showing coordinated activity — pallets, conveyor lines, or a control room overlooking a warehouse floor — one or two people in the mid-distance reviewing a clipboard or tablet, warm directional light, slight industrial haze, photorealistic, documentary style not posed, no text, no logos, no signage, no watermark, no visible faces in close-up

## 5. About page

- **Slot:** `/about/` — "who we are" section
- **Crop needed:** Landscape, roughly 3:2 to 16:9
- **Prompt:**
  > Editorial interior photograph of a modern corporate office in Houston, Texas, floor-to-ceiling windows with a recognizable Houston downtown skyline visible outside, warm late-afternoon light, a clean contemporary office interior with dark wood and bronze accents, no people or very soft-focus figures at the far edge of frame, photorealistic, calm and confident mood, no text, no logos, no signage, no watermark

## 6. Services hub

- **Slot:** `/services/` — page intro / hero
- **Crop needed:** Wide landscape, roughly 2:1
- **Prompt:**
  > Wide editorial photograph of a large-scale industrial or infrastructure worksite at sunset, aerial or elevated three-quarter angle, cranes and structural steel silhouetted against a warm amber and burgundy sky, sense of scale and active work in progress, photorealistic, cinematic color grading, no text, no logos, no signage, no watermark, no visible workers' faces in close-up

---

## After you generate

Send back whichever results you like best (doesn't need to be all six — even 2–3 strong ones is enough to start). Tell me which prompt/slot each one is for if it's not obvious, and I'll optimize (compress, correct aspect ratio) and wire them into the actual pages — nothing changes on the live site until then.
