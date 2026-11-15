---
name: t022_fpp_geodesic_coalescence_tail_0p67_median_k1p46_2026_11_02
description: T022 planar FPP Exp(1): geodesic merge tail r^-0.67 (KPZ 2/3), median merge distance ~k^1.46; coalescence at the integrable rate
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T09:29:26+04:00
  status: provisional
  evidence: "brain-repo 06_math_research/frontier/rows/T022/moves.jsonl 82dd880d"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T022 (no bigeodesics in general planar FPP), first move m022a (moves.jsonl 82dd880d, 2 Nov). Exponential(1) edge weights on Z^2, the Dijkstra geodesic tree to a far target, starts k apart at x = n/4. P(merge distance > r) at k 1 falls as r^-0.679 +- 0.013 (n 2048, 200 fields) and r^-0.665 +- 0.007 (n 1024, 400 fields), which is KPZ's 2/3. The median merge distance grows like k^1.46 +- 0.03 and k^1.41 +- 0.01 over k 4-64; the exponent is near 1.6 at small k and bent down by the box at k 64. So coalescence runs at the integrable rate in a non-integrable model: the input the Basu-Hoffman-Sly style argument needs looks true, and what is missing is a proof of it. Errors come from a bootstrap over whole fields. Scar: starts placed on the box wall merge along it (median 0); start inside the box. PREREG102 2/3, with (b) the mean ratio per doubling a MISS at k 32 and 64. Code: scratchpad t022/coal.c, stats.py, boot.py (pushed as t022_* in the row folder).


Related: the same FPP model on T006 gave chi 0.31 and xi 0.67, consistent with these exponents [[t006_fpp_chi_0p31_xi_0p67_kpz_relation_holds_2026_11_02]].

Addendum (2 Nov, m022b, moves.jsonl 7ccfd48d): Uniform(0,1) weights give the same exponents, a tail slope of -0.670 +- 0.011 and a median exponent of 1.459 +- 0.025, so this is not an Exp artifact. At n 4096 (Exp, 50 fields) the local median exponents sit flat at 1.52-1.59 and the fit gives 1.551 +- 0.050. The k^1.46 in the slug is a box-cap underestimate; the large-box value is consistent with 3/2. PREREG103 2/3.
