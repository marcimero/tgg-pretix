# Custom pretix image for The GOAT Germany.
# Built by GitHub Actions (.github/workflows/build.yml) and pushed to GHCR;
# Coolify only pulls and runs the finished image — no builds on the server.
#
# Contains:
#   - pretix-tgg-fonts (plugin/): Inter, Geist, Saira (+Condensed/Semi
#     Condensed) for ticket PDFs and the shop
#   - pretix-event-css-js (PyPI, maintained): UI code editor for custom
#     CSS/JS per event. (Not pretix-custom-css-js — that one is abandoned
#     and incompatible with pretix >= 2024.7.)
FROM pretix/standalone:stable

USER root
COPY plugin /tgg-plugin
RUN pip3 install /tgg-plugin pretix-event-css-js

USER pretixuser
RUN cd /pretix/src && make production
