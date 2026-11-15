VERDICT: PARTIAL reduction of the remaining L2-initial-data case to uniform continuity of bounded-start transition laws

The literature has advanced: Yi Han's [arXiv:2611.07310v1](https://arxiv.org/abs/2611.07310),
submitted 5 November 2026, covers every positive Hölder exponent for bounded
initial data, including unbounded diffusion coefficients. It also covers
arbitrary L2 initial data for bounded diffusion. The remaining source-level
corner is unbounded g, initial data in L2 without a spatial bound, and
0<beta<=2/3. See SOLVED_ELSEWHERE.md for exact theorem locations and scope.

PROOF.md gives a sufficient continuity criterion for that corner. Let P_s be
the already unique transition operator from bounded initial functions. If,
for each bounded Lipschitz f, P_s f is uniformly continuous in the L2 distance
on L2 balls, uniformly for s in compact intervals away from zero, then weak
uniqueness extends to every deterministic L2 initial state. The modulus must
be independent of the initial functions' spatial suprema.

The proof establishes positive-time boundedness and the bound
E||U_delta-S_delta u0||_2^2 <= C sqrt(delta) directly from L2 initial data.
It gives explicit comparison bounds (5)-(6), then identifies full path laws
by conditional restart. The root-mean-square exponent 1/4 is sharp already
for constant diffusion.

Checks: the constant-noise variance was derived independently from Fourier
modes and periodized Gaussians. Both give leading constant 1/sqrt(2 pi).
The computation command was:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_heat.py
```

All five comparisons passed; data are in heat_check.csv and full output is
in LOG.md. Peak RSS was 13.89 MiB. The process verified inherited nice=20;
the launcher warning is explained in LOG.md. An initial resource-limit setter
failed before calculation and was removed.

What failed: fixed spatial-cutoff localization at time zero does not extend
to general L2 data. PROOF.md gives an explicit singular initial function with
every fixed cutoff's exit-time infimum equal to zero.

What remains uncertain: the required uniform continuity estimate is unproved.
No uniqueness claim is made for the residual case. The new preprint's theorem
statements were checked, but its entire proof was not independently audited.

Next worker: prove (UC) in PROOF.md, or a bound
|P_s f(v)-P_s f(w)| <= K_(R,a,b,f)||v-w||_2^alpha with any alpha>0,
where K is independent of ||v||_infinity and ||w||_infinity. The reduction
then applies without further initial-time localization.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:19 Asia/Tbilisi.
