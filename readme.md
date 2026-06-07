# Salt Level Checker

A web-based salinity checker that determines whether a water sample's salt concentration is safe or too high.

## What it does

Enter a salt level in **parts per million (ppm)**. The app instantly shows:
- An animated gauge showing where the value sits on a 0–2000 ppm scale
- A **SAFE** result (green) for values at or below 1,000 ppm
- A **HIGH** alert (red) for values above 1,000 ppm
- Status LEDs and a glowing result card that reflect the reading

## Files

| File | Description |
|------|-------------|
| `index.html` | The complete web app — all HTML, CSS, and JS in one file, no build step needed |
| `salt-level-checker.py` | The original Python/tkinter desktop app this was converted from |

## Running locally

Just open `index.html` in any browser — no server or dependencies required.

## Deploying

This is a static site. It can be deployed to:
- **Netlify** — drag the folder into [app.netlify.com](https://app.netlify.com) or connect this GitHub repo
- **GitHub Pages** — enable Pages in your repo settings, set source to `main` / `/(root)`
- Any static hosting service

## Threshold

Safe limit is set at **≤ 1,000 ppm**. This mirrors the original Python app's logic.
