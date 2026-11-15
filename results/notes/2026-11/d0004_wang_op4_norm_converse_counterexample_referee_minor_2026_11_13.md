---
name: d0004_wang_op4_norm_converse_counterexample_referee_minor_2026_11_13
description: "Complete mixability Open Problem 4 (Wang survey): do the Theorem-5 norm inequalities suffice for n-CM? No: convex-order reduction + smooth density counterexample n=3,4, referee MINOR (cite PWW 2012 Thm 3.2b); D0007 proved = our existing repo"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T01:34:32+02:00
  status: verified
  evidence: "D0004AR referee MINOR 13 Nov; own quantile check min slack -1.7e-14; brain 54d1d025"
---

Wang's complete-mixability survey (arXiv 1411.6190), Open Problem 4, asks whether the norm inequalities of its Theorem 5 are sufficient for n-complete mixability. Our D0004A run (Codex, Mac mini 1, 13 Nov 2026) answered the unrestricted converse NO, and the independent referee D0004AR returned MINOR.

- Theorem A: for bounded X with mean mu, the Theorem-5 inequalities for every norm in Definition 5 hold iff X <=cx n mu - (n-1) X (convex order).
- Theorem B: a smooth density counterexample for n = 3 and 4, e.g. f(x) = 1/10 + (27/10)(2x-1)^2 on [0,1] for n = 3. It passes the convex-order test but fails the necessary condition P(1/4 < X < 3/4) >= 1/3 for a 3-CM continuous law with mean 1/2, since that mass is 13/80. My own check, 20,000 quantile atoms in d0004/check/dens.py, gives a minimum slack of -1.7e-14.
- Theorem C: Bernoulli(p) passes iff 1/n <= p <= 1-1/n, and is n-CM iff np is an integer.

What the referee asked for:
- Prop 5 is Puccetti-Wang-Wang 2012, Theorem 3.2(b), in count-vector form, and must be cited as such.
- The n=2 and Bernoulli facts are in Wang-Wang 2011, Prop 2.3, Mao-Wang 2015, Ex 3.1, and Bellini-Karasan-Pinar 2016, Thm 1.
- Index the non-Fatou construction from k >= 1, and fix the reproduction paths.

The new parts are the norm reduction and the explicit regular counterexamples. This is not a full characterization of the extra hypotheses Open Problem 4 asks for.

D0007 (Open Problem 7, the same day) is PROVED with referee MINOR, but it is the same result as our repo complete-mixability-large-n, so it needs no new paper. The claimed counterexample in Yin-Zhu arXiv:1706.05499 is incompatible with it.

Archive: brain 06_math_research/referee_reports/2026-11-13/D0004A, D0004AR, D0007A, D0007AR (commit 54d1d025). Ledger: intake_D rows for D0004 and D0007.

