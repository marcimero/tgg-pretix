# tgg-pretix

Custom pretix-Image für [tickets.thegoatgermany.de](https://tickets.thegoatgermany.de), gebaut von GitHub Actions und gepusht nach `ghcr.io/marcimero/tgg-pretix:latest`. Coolify pullt nur das fertige Image — es wird nichts auf dem Server gebaut.

## Inhalt

- **`plugin/` — pretix-tgg-fonts**: eigene Fonts für Ticket-PDFs und den Shop:
  Inter, Geist, Saira, Saira Condensed, Saira Semi Condensed
  (Google Fonts, [SIL Open Font License 1.1](https://openfontlicense.org/); Condensed/Semi Condensed ohne Kursive — Italic zeigt die aufrechten Schnitte)
- **pretix-custom-css-js**: [Marketplace-Plugin (unofficial)](https://github.com/pretix-unofficial/pretix-custom-css-js) für eigenes CSS/JS pro Event — nach dem Deploy pro Event unter *Einstellungen → Plugins* aktivieren.

## Workflow

- Push auf `main` oder manueller Run („Build & Push" → *Run workflow*) baut das Image neu.
- **pretix-Update:** Workflow manuell laufen lassen (zieht das frische `pretix/standalone:stable`), danach in Coolify redeployen.
- Fonts ändern: TTF/WOFF2 in `plugin/pretix_tggfonts/static/pretix_tggfonts/` legen, in `signals.py` registrieren, pushen.
