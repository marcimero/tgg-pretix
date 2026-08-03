# Custom pretix image for The GOAT Germany.
# Built by GitHub Actions (.github/workflows/build.yml) and pushed to GHCR;
# Coolify only pulls and runs the finished image — no builds on the server.
#
# Contains pretix-tgg-fonts (plugin/): Inter, Geist, Saira (+Condensed/Semi
# Condensed) for PDFs and shop, plus custom shop CSS via html_head.
# (The marketplace plugin pretix-custom-css-js is abandoned and incompatible
# with pretix >= 2024.7 — its sass signals were removed upstream.)
FROM pretix/standalone:stable

USER root
COPY plugin /tgg-plugin
RUN pip3 install /tgg-plugin

USER pretixuser
RUN cd /pretix/src && make production
