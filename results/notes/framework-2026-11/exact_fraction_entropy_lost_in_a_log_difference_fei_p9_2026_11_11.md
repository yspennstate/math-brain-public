---
name: exact_fraction_entropy_lost_in_a_log_difference_fei_p9_2026_11_11
description: "[VERIFIED] FEI table erratic at large k though arithmetic was exact? log2(num)-log2(den) cancels when a2/d2~1e17; use log1p"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T07:22:37+02:00
  status: provisional
  evidence: ""
---

An "exact" Fraction computation of an entropy term can still be wrong at the last float step. FEI P9's
forced_exact.py kept every coefficient exact but took a^2*log2((a^2+d^2)/a^2) as log2(numerator)-log2(denominator):
with a^2/d^2 near 1e17 (k >= ~121) the two logs (each > 1000) differ by < 1e-17, the term rounds away and is then
multiplied by the large weight a^2. Paper rows 121-141 were off by up to 2.5 and the Remark's "ratio falls from
k=133 to 135" was the artefact; with only that log replaced by log1p the same code gave 45.276 / 50.138 at k=121/133,
matching an independent exact double sum (referee notes 06_math_research/lean_checks_agent/p9_referee, 18d60c0c).
The naive float form r2*log2((r2+1)/r2) has the same flaw once r2 > 1e16 (it returns 0 instead of 1/ln 2).

**Why:** a table that jumps around non-monotonically at large k, or a lone spike (k=59 in the P=1/2 column), is the
signature; the theorem was fine, only the numbers were wrong.

**How to apply:** for p*log((p+q)/p) with p >> q use q/p via log1p (log1p(q/p)/ln 2), never a difference of two
large logs; check a table at large k against a second implementation before quoting it. Related [[fei_p8_hidden_coordinates_posted_2026_11_11]].

