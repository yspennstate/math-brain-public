---
name: g0013_every_permutation_n_le_10_proved_exact_certificate_2026_11_08
description: "[VERIFIED] G0013 (A_n) proved for every permutation n <= 10: exact Laguerre certificate, 456,453 classes at n=10, min margin 2.17e-3, public ee5dd5fa, ledger e10e538b"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:30:56+02:00
  status: verified
  evidence: "papers_agent/G0013/sd_exact_n10.verify (VERIFIED) + sd_canon_check_n10.out (0 bad); public commit ee5dd5fa6b66773350c18fe8558d79f9a17bcde1"
---

G0013 (Catalano-Lavenant / Schrott Conj. 1.1, the statement (A_n): the identity is farthest from lambda x lambda among n-point grid permutation measures) is now PROVED for every permutation with n <= 10, in exact rational arithmetic, and public. Extends [[g0013_every_permutation_n_le_9_proved_exact_laguerre_certificate_2026_11_08]] by one n with the same certificate.

n = 10 run (papers_agent/G0013, 8 Nov 02:14-03:00 local): sd_exact_shard.py 10 4 k, four windowless pythonw shards, BelowNormal, EcoQoS throttling turned off with unthrottle.py (without it the shards ran at ~1/3 speed). 456,453 classes = Burnside orbit count of S_10 under the square's 8 symmetries (456,454) less the id/rev class; about 115-175 classes/s over four shards, ~45 min. Exact dual lower bound for W2^2(id) at n=10: 0.1013632915011046. All ok, 0 FAIL; smallest certified margin 2.169456e-3 at 0123456798 (the corner adjacent transposition again; float gap 2.17242e-3, so rounding + excess cost ~3e-6). n^2 * A_n gap = 0.1086 (series 0.1459 ... 0.1145, 0.1086 for n=3..10).

Checks: sd_exact_verify.py 10 4 (every shard ends '# done', every line well formed, no duplicate, count = Burnside, no FAIL, one lower bound) -> VERIFIED; sd_canon_check.py 10 4 (every key canonical under the 8 symmetries and not the id class, so distinct lines = distinct classes) -> 0 bad of 456,453. Burnside formula: (n! + 2 I(n) + 2^m m! + [n mod 4 in {0,1}] 2 (2k)!/k!)/8, m = n//2, k = n//4, I = involutions; gives 1,6,22,114,693,5281,46065,456453 classes for n=3..10 after subtracting 1.

Published: paper Prop. 4.11 now 3 <= n <= 10 (12 pp, 0 Overfull); yspennstate/wasserstein-layered-permutation-copulas ee5dd5fa6b66773350c18fe8558d79f9a17bcde1 ("Every permutation for n at most ten", with the four shard outputs, ~4.8 MB each); ledger open-problems-repo master e10e538bd1447accba11e8416a41ebf5d8c89860 [skip ci]. Status still partial: general n open.

Next size: n = 11 is about 5.0e6 classes (11x), roughly 8-10 h on four workstation shards at this rate; the margin shrinks like ~0.11/n^2 (~9e-4 at n=11), still far above the 2^-40 rounding. This route proves fixed n only; it gives no general-n argument.

