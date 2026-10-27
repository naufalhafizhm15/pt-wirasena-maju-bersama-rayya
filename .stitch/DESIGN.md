# Design System: PT. Wirasena Maju Bersama Rayya — Industrial B2B Supply & Packaging Manufacturing

## 1. Visual Theme & Atmosphere
An architectural, precision-engineered industrial B2B interface with confident asymmetric layouts, technical specification tables, and fluid spring-physics motion (Density: 6, Variance: 6, Motion: 5). The atmosphere is clinical, trustworthy, and modern — like a Japanese-standard manufacturing plant in Cikarang combined with an editorial industrial catalog. Zero "vibe-coded" SaaS clichés.

## 2. Color Palette & Roles
- **Canvas Alabaster** (#F8FAFC) — Primary background surface
- **Pure Studio Surface** (#FFFFFF) — Product showcase and specification table fill
- **Deep Zinc Ink** (#18181B) — Primary typography and structural headers (never pure #000000)
- **Industrial Slate** (#52525B) — Secondary body text, part numbers, and technical descriptions
- **Technical Rule** (#E4E4E7) — 1px structural architectural grid lines and table dividers
- **Wirasena Forest Green** (#2E8540) — Singular calibrated accent (<80% saturation) for primary RFQ actions, active indicators, and industrial badges

## 3. Typography Rules
- **Display / Headlines:** `Outfit` — Track-tight (`-0.025em`), controlled architectural scale, weight-driven hierarchy (`600`–`700`)
- **Body Copy:** `Plus Jakarta Sans` — Relaxed leading (`1.75`), max `65ch` per line, neutral slate tone
- **Monospace / Specs:** `JetBrains Mono` — Mandatory for all part codes, dimensions (`mm`), flute grades (`B/C/CB-Flute`), telephone numbers, NPWP, and catalog indices (`01`–`06`)
- **Banned:** `Inter`, generic system fonts, and serif fonts.

## 4. Component Stylings
- **Buttons:** Tactile `-1px` translate on active state. Solid Wirasena Forest Green (`#2E8540`) or Deep Zinc (`#18181B`) with crisp `6px` architectural corners. No neon outer glows.
- **Product Spec Rows & Asymmetric Zig-Zag Blocks:** Replace generic 3-column equal card grids with 1px architectural grid cells (`border-t border-[#E4E4E7]`) and 2-column asymmetric split showcases featuring studio-white product photography and monospace specification matrices.
- **Inputs / Search:** Label above input, crisp `1px` border (`#D4D4D8`), focus ring in `#2E8540`.

## 5. Layout Principles
- **Asymmetric Split Hero:** Left-aligned editorial typography with inline contextual factory visuals and clean spatial separation (text never overlaps busy photography).
- **No 3-Column Equal Card Rows:** Use architectural index tables, 2-column zig-zag product blocks, and specification matrices.
- **Containment:** Max-width `1360px` centered with `1px` vertical structural hairlines.
- **Mobile-First Collapse (< 768px):** All multi-column grids collapse cleanly into single-column stacks with zero horizontal overflow.

## 6. Motion & Interaction
- **Spring Physics:** `cubic-bezier(0.22, 1, 0.36, 1)` on hover and reveal transitions.
- **Hardware-Accelerated Transforms:** Animate exclusively via `transform` and `opacity`.

## 7. Anti-Patterns (Strictly Banned)
- No emojis anywhere in UI labels or headings
- No `Inter` font
- No pure black (`#000000`)
- No neon or outer glow shadows
- No 3-column equal card layouts
- No overlapping text over busy unmasked photos
- No fabricated metrics or `LABEL // YEAR` AI clichés

