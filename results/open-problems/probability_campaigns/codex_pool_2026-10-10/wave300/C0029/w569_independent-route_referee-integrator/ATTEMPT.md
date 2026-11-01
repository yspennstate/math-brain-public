# C0029 independent route (recorded before reading w567's ATTEMPT.md)

Target: for an n by n matrix B of independent uniform signs, show P(s_min(B) <= t/sqrt(n)) <= t + C exp(-c n), with constants C,c>0 independent of n,t. Current global openness: UNKNOWN. The 2025 Sah–Sahasrabudhe–Sawhney result gives (1+O((log n)^(-1/16)))t plus an exponential remainder, which does not settle the exact coefficient.

## Route: heat-flow interpolation

Let G have independent standard normal entries and set M_s=sqrt(1-s) B+sqrt(s) G, 0<=s<=1, with independent B,G. A tempting route is to compare the distribution functions F_s(t)=P(s_min(M_s)<=t/sqrt(n)) along s and use the Gaussian exact hard-edge law. The replacement would have to separate the Bernoulli singular atom from the continuous part and control the total change to within the positive Gaussian margin t-F_G(t) (asymptotically t^3/3 for small t). A uniform monotone comparison is false:

* At n=1 and t=1/2, F_0(t)=0, whereas F_1(t)=P(|G|<=1/2)>0.
* At n=2 and t=0, F_0(0)=1/2: after fixing the first sign row, exactly two of the four second rows are parallel to it. For every s>0, M_s has a joint density on R^4, and the determinant-zero set has Lebesgue measure zero, so F_s(0)=0.

Thus interpolation can move the event in opposite directions at different thresholds. This refutes the naive monotonicity step, not the conjecture. An independent route would require a threshold-dependent differential comparison of the continuous part plus explicit control of the singular atom. I have no such estimate.

The hardest open piece for this route is an upper bound on the Bernoulli-to-Gaussian CDF error that fits under the Gaussian deficit from t in the intermediate small-ball window. The 2025 multiplicative error alone is too large there. No parent-problem solution claimed.

Sources: Spielman–Teng, ICM 2002, Conjecture 2, https://cs-www.cs.yale.edu/homes/spielman/PAPERS/icm.pdf ; Sah–Sahasrabudhe–Sawhney, GAFA 2025, Theorem 1.1, https://doi.org/10.1007/s00039-025-00707-z ; Tao–Vu, GAFA 2010, https://arxiv.org/abs/0903.0614 .
