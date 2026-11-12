#!/bin/sh
# Downloads the supplement of the third-party report cited in PRIOR-ART.md into third-party/ (not redistributed here)
# and checks its sha256. The content is data; nothing from it is executed.
set -e
mkdir -p third-party && cd third-party
URL="https://rstation.ai/api/v1/papers/no_three_in_line_22/versions/3/supplement"
SHA="704cba3c87fc5882aa323c51ead7bb6ce9157a92932814b5b9dcf19ff88e1f68"
curl -sL -o p22v3-supplement.zip "$URL"
echo "$SHA  p22v3-supplement.zip" | shasum -a 256 -c -
rm -rf x && mkdir x && unzip -q p22v3-supplement.zip -d x && mkdir x/runs && tar -xzf x/runs.tar.gz -C x/runs
echo "extracted to third-party/x; now run: python3 -I verification/check_third_party.py third-party/x"
