# Prior art for lower bounds on A272651 at large n

Searched 13 November 2026 (ChatGPT literature search for the lab, then re-read and re-checked by the guide).

## In the OEIS

`https://oeis.org/search?q=id:A272651&fmt=text` (13 Nov 2026): terms a(1)..a(47+) equal to 2n; comment by Donghwi Park
(20 Jun 2026): a(n) = 2n for all 1 < n <= 66, and 2n-point sets known for n = 68, 70. No lower bounds for larger n in the entry.
A000769 (number of 2n-point solutions up to symmetry) carries the reference list.

## Literature and public tables

| Source | What it establishes | Checked by us |
|---|---|---|
| R. R. Hall, T. H. Jackson, A. Sudbery, K. Wild, Some advances in the no-three-in-line problem, J. Combin. Theory Ser. A 18 (1975), 336-341 | sets of 3(p-1) points in the 2p X 2p grid, p prime; (3/2 - o(1)) n in general | construction re-implemented in `programs/candidate1_death_growth.py`; sets pass the checkers |
| A. Flammenkamp, Progress in the no-three-in-line problem (web page and database) | 2n-point sets for all n up to the high 70s with a few gaps (state of autumn 2026: the page should be read for the current list) | not re-checked here |
| L. Zhang, X. Zhuang, T. Wang, N. Kaplan, Geometry-Aware MCTS for Extremal Problems in Combinatorial Geometry, arXiv:2606.26399 (June 2026) | reports sets of "roughly 1.8n" points for 82 <= n <= 119 (an example with 216 points at n = 119) | abstract and text read; no coordinates available to check |
| kiro_conic (an AI agent), "Explicit quarter-turn no-three-in-line sets with at least 1.8n points for sixteen grid sizes 100 <= n <= 200", rStation paper 22, version 3, 9 Oct 2026, https://rstation.ai/problems/no_three_in_line/papers/22/v3 | explicit sets with coordinates: 184 at n = 100 up to 360 at n = 200, and run outputs up to 528 at n = 300 | **all 158 point-set files verified** with our checker (`verification/logs/check_third_party.log`) |
| rStation discussions, 7 Oct and 5 Nov 2026 | counts 700 at side 400 and 1352 (and 1350) at side 800 from search logs | not verified: no coordinates checked |

rStation is a platform where AI agents post results; it is not a refereed source. It is credited here because the coordinates are
public and pass our check. The supplement is not redistributed: `verification/fetch_third_party.sh` downloads it and checks its sha256.

## Who was first

- Our sets date from 29-30 August 2026 (private repository; not published at the time).
- The 1.8n sets of Zhang et al. (June 2026) precede ours for 82 <= n <= 119, and the rStation sets (October 2026) are larger than
  ours at every side up to 300. So for n <= 302 our sets add nothing to what is known.
- For n = 398, 502, 614 we found no larger set with checkable coordinates; for n = 802 a larger count is reported but unverified.

To be repeated before any submission: OEIS entry, arXiv listing for "no-three-in-line", Flammenkamp's page, the rStation problem page.
