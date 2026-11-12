#!/usr/bin/env python3
"""Checker for no-three-in-line point sets in the n X n grid (written by the lab's guide, independent of the search code).

Two input formats:
  ours:        first line "# n=<n> points=<N> ...", then N lines "x y", 0-based;
  plain:       first line "n N", then N lines "x y", 1-based (use --zero for 0-based).
For every point the reduced directions to all later points must be pairwise distinct; exact integer arithmetic.
Prints "OK n N N/n file" per file; exits non-zero on the first failure.
"""
import re, sys
from math import gcd


def read(path, zero):
    text = open(path).read()
    m = re.match(r"#\s*n=(\d+)\s+points=(\d+)", text)
    if m:
        n, N, lo = int(m.group(1)), int(m.group(2)), 0
        vals = [int(t) for line in text.splitlines() if not line.startswith("#") for t in line.split()]
    else:
        toks = [int(t) for t in text.split()]
        n, N, vals, lo = toks[0], toks[1], toks[2:], (0 if zero else 1)
    if len(vals) != 2 * N:
        raise ValueError(f"expected {N} points, found {len(vals) / 2}")
    pts = [(vals[2 * i], vals[2 * i + 1]) for i in range(N)]
    if not all(lo <= x < lo + n and lo <= y < lo + n for x, y in pts):
        raise ValueError("point outside the grid")
    if len(set(pts)) != N:
        raise ValueError("repeated point")
    return n, pts


def no_three(pts):
    for i, (x, y) in enumerate(pts):
        seen = set()
        for u, v in pts[i + 1:]:
            dx, dy = u - x, v - y
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            if (dx, dy) in seen:
                raise ValueError(f"three collinear points through {(x, y)} in direction {(dx, dy)}")
            seen.add((dx, dy))


if __name__ == "__main__":
    zero = "--zero" in sys.argv
    for path in [a for a in sys.argv[1:] if a != "--zero"]:
        try:
            n, pts = read(path, zero)
            no_three(pts)
        except ValueError as e:
            sys.exit(f"FAIL {path}: {e}")
        print("OK", n, len(pts), f"{len(pts) / n:.4f}", path.split("/")[-1])
