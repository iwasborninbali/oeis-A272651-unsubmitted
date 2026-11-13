# OEIS A272651: verified lower bounds for large grids (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 14 Nov 2026).

- [A272651](https://oeis.org/A272651), sixteen explicit sets above 3(p-1) for n = 2p, 106 <= n <= 802: **verified** (2026-11-13: literature check: superseded for n <= 302; repository built). Certificate: complete.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

[A272651](https://oeis.org/A272651): a(n) is the maximal number of points of the n X n square grid such that no three lie
on a line (offset 1). The entry lists a(n) = 2n for the n where a 2n-point set is known and says nothing about larger grids.
A point set with N points and no three in a line in the n X n grid proves a(n) >= N, and also a(m) >= N for every m > n
(the set fits in the larger grid).

## Result

Sixteen explicit point sets for n = 2p (p prime), each larger than the classical Hall-Jackson-Sudbery-Wild set of 3(p-1)
points that they start from:

| n | points (a(n) >= ) | HJSW 3(p-1) | best set with public coordinates that we verified, at a side <= n | status of our bound |
|---:|---:|---:|---:|---|
| 106 | 162 | 156 | 188 (side 104) | superseded |
| 118 | 181 | 174 | 204 (side 112) | superseded |
| 122 | 192 | 180 | 216 (side 120) | superseded |
| 134 | 210 | 198 | 232 (side 128) | superseded |
| 142 | 221 | 210 | 252 (side 140) | superseded |
| 146 | 224 | 216 | 260 (side 144) | superseded |
| 158 | 241 | 234 | 280 (side 156) | superseded |
| 166 | 258 | 246 | 296 (side 164) | superseded |
| 178 | 273 | 264 | 316 (side 176) | superseded |
| 194 | 303 | 288 | 344 (side 192) | superseded |
| 202 | 313 | 300 | 360 (side 200) | superseded |
| 302 | 472 | 450 | 528 (side 300) | superseded |
| 398 | 616 | 594 | 528 (side 300) | best verified set known to us |
| 502 | 771 | 750 | 528 (side 300) | best verified set known to us |
| 614 | 948 | 918 | 528 (side 300) | best verified set known to us |
| 802 | 1226 | 1200 | 528 (side 300) | best verified set known to us; a larger count is reported without checked coordinates (see below) |

**What this is and is not.** For n <= 302 our sets are not the best known: sets with about 1.8n points were published in
2026 for 82 <= n <= 300 (see [PRIOR-ART.md](PRIOR-ART.md)), and we verified the public coordinates ourselves. For n = 398, 502
and 614 ours are the largest sets with checkable coordinates that we know of. Reports without coordinates that we could
check give 700 points at side 400 and 1352 at side 800; if confirmed, they supersede our bounds at 398 (from side 400 on)
and 802. None of these bounds is claimed to be optimal, and the trivial upper bound is 2n.

**What would change in the entry.** Nothing is submitted. The entry could gain a link to a table of verified lower bounds
for the sizes where 2n points are not known. As it stands, such a table would be mostly other people's results, so the
decision is open (see the registry record).

## How it was obtained

`programs/candidate1_death_growth.py` (29-30 August 2026): start from the Hall-Jackson-Sudbery-Wild set in the 2p X 2p
window (points of the hyperbola xy = 1 mod p, four copies minus the middle block: 3(p-1) points, no three in a line), mark
every free cell that is not on a line through two chosen points as live, and repeatedly add the live cell that kills the
fewest other live cells (ties by a seeded random choice) until no live cell remains. The sets are therefore inclusion-maximal.

## Verification

Every set was checked for range, distinctness and collinearity by two programs that do not share code with the search
program: `verification/check_no3.py` (distinct reduced directions from every point) and `verification/check_triples.py`
(cross product over all triples). Both pass on all sixteen sets. The public third-party sets quoted in the table were checked
with the same checker. Not verified: the reported counts at sides 400 and 800 and the 1.8n sets of the June 2026 preprint
(no coordinates). Details: [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Hall, Jackson, Sudbery and Wild (1975) for the seed construction; Zhang, Zhuang, Wang and Kaplan (arXiv:2606.26399) and a
public report by the agent kiro_conic on the rStation platform (October 2026) for the larger sets at n <= 300. See
[PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

```sh
python3 verification/check_no3.py data/witnesses/*.txt        # 16 lines "OK n N N/n file", about 1 s
python3 verification/check_triples.py data/witnesses/*.txt    # 16 lines "OK ... collinear triples: 0", about 5 min
sh verification/fetch_third_party.sh                          # downloads the third-party supplement, checks its sha256
python3 -I verification/check_third_party.py third-party/x    # "point sets checked: 158, all valid" and the best set per side
python3 programs/candidate1_death_growth.py run 53 1          # regenerates the n = 106 set (seed 0)
```

Expected outputs are in `verification/logs/`.

## Provenance

Witnesses and the search program come from the lab's private research repository `moves`, folder
`research/work/proba/` (commit 888601fe8325eda27c5cb2ab818f24cb30cdcc14, 30 August 2026); the files in `data/witnesses/`
are the same point lists with a uniform header.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (Claude Code as the lab's guide; the search
program was written by a Claude agent of the lab). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
