#!/usr/bin/env python3
"""Checks every point-set file found under a directory (format "n N", then N lines "x y", 1-based) with check_no3.no_three
and prints the largest verified set per n. Files that are not point sets (logs, tables) are skipped and counted.
Usage: python3 -I check_third_party.py DIR"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_no3 import no_three

best, checked, skipped = {}, 0, 0
for root, _, files in os.walk(sys.argv[1]):
    for f in sorted(files):
        path = os.path.join(root, f)
        try:
            toks = [int(t) for t in open(path, errors="replace").read().split()]
            n, N, vals = toks[0], toks[1], toks[2:]
            if len(vals) != 2 * N or N < 3:
                raise ValueError
        except (ValueError, IndexError):
            skipped += 1
            continue
        pts = [(vals[2 * i], vals[2 * i + 1]) for i in range(N)]
        if len(set(pts)) != N or not all(1 <= x <= n and 1 <= y <= n for x, y in pts):
            sys.exit(f"FAIL {path}: bad points")
        try:
            no_three(pts)
        except ValueError as e:
            sys.exit(f"FAIL {path}: {e}")
        checked += 1
        if N > best.get(n, (0, ""))[0]:
            best[n] = (N, os.path.relpath(path, sys.argv[1]))
print(f"point sets checked: {checked}, all valid; other files skipped: {skipped}")
for n in sorted(best):
    print(n, best[n][0], f"{best[n][0] / n:.4f}", best[n][1])
