#!/usr/bin/env python3
"""Second check, different method: brute force over all triples with the cross product (slow; use for the smaller sets).
Usage: check_triples.py FILE...   (files in the format "# n=<n> points=<N>", 0-based "x y")"""
import re, sys
from itertools import combinations

for path in sys.argv[1:]:
    text = open(path).read()
    n, N = map(int, re.match(r"#\s*n=(\d+)\s+points=(\d+)", text).groups())
    pts = [tuple(map(int, l.split())) for l in text.splitlines() if l.strip() and not l.startswith("#")]
    assert len(pts) == N == len(set(pts)) and all(0 <= x < n and 0 <= y < n for x, y in pts), path
    bad = sum(1 for a, b, c in combinations(pts, 3)
              if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]))
    print("OK" if bad == 0 else "FAIL", n, N, "collinear triples:", bad, path.split("/")[-1])
    if bad:
        sys.exit(1)
