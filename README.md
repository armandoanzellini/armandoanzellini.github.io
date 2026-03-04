# Anzellini Consulting — Website Template

## Files
- `index.html` — Main single-page website
- `style.css`  — All styles (import this in index.html, already linked)

## How to use

### Local preview
Open `index.html` directly in any browser. No build step required.

### Customise
1. **Contact form** — The form uses `mailto:` — replace `ara622@lehigh.edu` in the form tag with your preferred email, or swap for a form backend (Formspree, Netlify Forms, etc.)
2. **Content** — All text is in `index.html`. Search for `[placeholder]` text to find fields to update.
3. **Colors** — All design tokens are CSS variables at the top of `style.css` under `:root { }`.
4. **Fonts** — Loaded via Google Fonts in `style.css`. Works offline if you download and self-host.

### Deploy
Upload both files to any static host:
- GitHub Pages
- Netlify (drag and drop the folder)
- Squarespace Custom Code
- Your university web server

All images are inline SVGs — no external image files needed.
