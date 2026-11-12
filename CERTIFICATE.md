# Verification certificate: A272651, lower bounds from sixteen explicit sets

## Claim

For each line below there is a set of N points in the n X n grid, no three on a line; hence a(n) >= N.

n: N = 106: 162, 118: 181, 122: 192, 134: 210, 142: 221, 146: 224, 158: 241, 166: 258, 178: 273, 194: 303, 202: 313,
302: 472, 398: 616, 502: 771, 614: 948, 802: 1226.

No claim of optimality and no claim that these are the best known bounds (see README).

## Evidence

| What | Program | Written by | Covers | Result |
|---|---|---|---|---|
| Producer | `programs/candidate1_death_growth.py` | a Claude agent of the lab, 29-30 Aug 2026 | builds the sets; its own triple check ran for p <= 307 and was skipped for p = 401 | sets in `data/witnesses/` |
| Independent check 1 | `verification/check_no3.py` | the guide (Claude Code), 13 Nov 2026 | all 16 sets: range, distinctness, pairwise distinct reduced directions from every point | 16 x OK |
| Independent check 2 | `verification/check_triples.py` | the guide, 13 Nov 2026 | all 16 sets: cross product over every triple | 16 x OK, 0 collinear triples |
| Third-party sets | `verification/check_third_party.py` | the guide, 13 Nov 2026 | 158 point-set files of the rStation supplement (sha256 704cba3c...1f68) | all valid; best per side in `verification/logs/check_third_party.log` |

The two checkers share no code with the producer and use different methods from each other.

## Replayed for this repository

13 November 2026, Apple Silicon Mac, Python 3:

```
python3 verification/check_no3.py data/witnesses/*.txt       -> verification/logs/check_no3.log        (16 lines OK)
python3 verification/check_triples.py data/witnesses/*.txt   -> verification/logs/check_triples.log    (16 lines OK)
python3 -I verification/check_third_party.py <extracted supplement> -> verification/logs/check_third_party.log
```

## Not covered

- Optimality of any set; only inclusion-maximality follows from the construction, and that was not re-checked here.
- The counts reported without coordinates that we could check: 700 points at side 400 and 1352 at side 800 (rStation
  discussions of October-November 2026), 236 at side 132 (same report), and the sets of arXiv:2606.26399 (about 1.8n points for 82 <= n <= 119).
- Completeness of the prior-art search: larger sets may exist elsewhere.

## Guide's independent check

Both checkers above are the guide's own code and were run by him on 13 November 2026 on all sixteen sets; an earlier
version of check 1 passed on the original files on 13 November 2026 as well. Result: all sixteen sets are valid.

## Verdict

`complete` for the claim as worded (sixteen valid sets, hence sixteen lower bounds).
