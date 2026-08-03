# Custom pretix image for The GOAT Germany.
# Built by GitHub Actions (.github/workflows/build.yml) and pushed to GHCR;
# Coolify only pulls and runs the finished image — no builds on the server.
#
# Contains:
#   - pretix-tgg-fonts (plugin/): Inter, Geist, Saira (+Condensed/Semi Condensed)
#   - pretix-custom-css-js: custom CSS/JS per event (marketplace, unofficial)
FROM pretix/standalone:stable

USER root
COPY plugin /tgg-plugin
# --no-build-isolation: pretix-custom-css-js imports django in its setup.py
# (compilemessages via gettext), so the build must see the image's Python env.
RUN apt-get update \
    && apt-get install -y --no-install-recommends gettext \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --no-build-isolation /tgg-plugin \
        "git+https://github.com/pretix-unofficial/pretix-custom-css-js.git"

USER pretixuser
RUN cd /pretix/src && make production
