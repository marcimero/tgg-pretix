# tgg-pretix

Custom pretix-Image für [tickets.thegoatgermany.de](https://tickets.thegoatgermany.de), gebaut von GitHub Actions und gepusht nach `ghcr.io/marcimero/tgg-pretix:latest`. Coolify pullt nur das fertige Image — es wird nichts auf dem Server gebaut.

## Inhalt

- **`plugin/` — pretix-tgg-fonts**: eigene Fonts für Ticket-PDFs und den Shop:
  Inter, Geist, Saira, Saira Condensed, Saira Semi Condensed
  (Google Fonts, [SIL Open Font License 1.1](https://openfontlicense.org/); Condensed/Semi Condensed ohne Kursive — Italic zeigt die aufrechten Schnitte). Global verfügbar, keine Plugin-Aktivierung nötig.
- **[pretix-event-css-js](https://github.com/nicoknoll/pretix-event-css-js)** (PyPI, gepflegt): Code-Editor für eigenes CSS/JS pro Event — beim Event unter *Einstellungen → Plugins* aktivieren, danach erscheint *Einstellungen → Event CSS & JS*.
  (Nicht zu verwechseln mit `pretix-custom-css-js` — das ist verwaist und mit pretix ≥ 2024.7 inkompatibel.)

## Workflow

- Push auf `main` oder manueller Run („Build & Push" → *Run workflow*) baut das Image neu.
- **pretix-Update:** Workflow manuell laufen lassen (zieht das frische `pretix/standalone:stable`), danach in Coolify redeployen.
- Fonts ändern: TTF/WOFF2 in `plugin/pretix_tggfonts/static/pretix_tggfonts/` legen, in `signals.py` registrieren, pushen.
