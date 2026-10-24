# QFORM B17 — exact 3 sqrt(2) ceiling for every finite collinear-heavy fragmentation

Run: `QFORM-B17-20260922T233857Z-r11`

Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL_QFORM_OPEN / CONTINUITY_SEPARATE / WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form conjecture is **not** proved here. The result closes the remaining 1.16% gap in the entire collinear-heavy witness architecture isolated in the preceding B17 run: no finite number of macroscopic independent cap-one physical coordinates sharing one minority-sign spectral direction can beat the diffuse `3 sqrt(2)` obstruction.

## 1. Dependency: exact branch extremization

The preceding account01/B17 theorem at

`yspennstate/math-open-problems`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/QFORM-B17-20260922T225652Z/REPORT.md`

proves the following exact global-output reduction. For any finite real vector `a=(a_1,...,a_r)` with

`sum_i a_i^2=1`,

arbitrary independent real `X_i` with densities at most one, and independent standard Gaussians `G_1,G_2`, put

`T_a = G_1^2 + G_2^2 - 12 (sum_i a_i X_i)^2`.

If `U_i` are iid `Unif[-1/2,1/2]`, then

`||p_{T_a}||_infinity <= (1/2) F(a)`,

where

`F(a) := E exp[-6 (sum_i a_i U_i)^2]`,

and equality at output zero is attained when every heavy law is the centered unit interval. In physical variance-`1/12` normalization the exact branch constant is

`C(a)=6 F(a)`.

The previous run bounded `C(a)` by `3 sqrt(2)(pi/3)^(1/4)`. The theorem below improves this to the exact sharp ceiling `3 sqrt(2)`.

## 2. External sinc input

Let `sinc(u)=sin(u)/u`, with the continuous value one at zero. König and Koldobsky, *On the maximal perimeter of sections of the cube*, Advances in Mathematics 346 (2019), 773–804, DOI `10.1016/j.aim.2019.02.017`, Proposition 7, prove for Ball's normalized sinc-integral function that for every `p>=9/4`,

`f(p) <= sqrt(3/pi)`.

With their normalization this is exactly

`boxed( integral_R |sinc(u)|^p du <= sqrt(6 pi / p),   p>=9/4. )`       (2.1)

This asymptotically sharp refinement of Ball's basic sinc bound is the missing constant needed below.

## 3. Main theorem

**Theorem (QFORM-COLLINEAR-FRAGMENT-SHARP-3SQRT2-v1).** For every finite real vector `a=(a_i)` satisfying `sum a_i^2=1`,

`boxed( F(a)=E exp[-6(sum_i a_iU_i)^2] <= 1/sqrt(2). )`                 (3.1)

Consequently the exact branch constant satisfies

`boxed( C(a) <= 3 sqrt(2). )`                                          (3.2)

Moreover

`sup_{r>=1, sum a_i^2=1} C(a) = 3 sqrt(2)`.

The supremum is approached by the equal-weight vectors `a_i=1/sqrt(r)` as `r->infinity`, by the already proved Gaussian endpoint / CLT limit.

### Proof of (3.1)

Zero coefficients may be discarded. By Fourier inversion,

`e^{-6x^2} = (24 pi)^(-1/2) integral_R e^{-t^2/24} e^{itx} dt`.

Since `E exp(i t a_i U_i)=sinc(a_i t/2)`, Fubini gives

`F(a) = (24 pi)^(-1/2) integral_R e^{-t^2/24} prod_i sinc(a_i t/2) dt`.       (3.3)

We split according to the largest leverage.

### Case I: every `a_i^2 <= 8/9`

Set

`p_0=2`, `p_i=2/a_i^2`.

Then `p_i>=9/4` and

`1/p_0 + sum_i 1/p_i = 1/2 + (1/2)sum_i a_i^2 = 1`.

Apply Hölder to the absolute value of (3.3). The Gaussian factor satisfies

`||e^{-t^2/24}||_2 = (12 pi)^(1/4)`.                                  (3.4)

For each sinc factor, after `u=a_i t/2`, (2.1) gives

`||sinc(a_i t/2)||_{p_i}^{p_i}`
` = (2/|a_i|) integral_R |sinc(u)|^{p_i} du`
` <= (2/|a_i|) sqrt(6 pi/p_i)`
` = 2 sqrt(3 pi)`.                                                     (3.5)

Therefore

`integral_R e^{-t^2/24} prod_i |sinc(a_i t/2)| dt`
` <= (12 pi)^(1/4) prod_i [2 sqrt(3 pi)]^(1/p_i)`
` = (12 pi)^(1/4) [2 sqrt(3 pi)]^(1/2)`
` = sqrt(12 pi)`.                                                      (3.6)

Insert (3.6) into (3.3):

`F(a) <= sqrt(12 pi)/sqrt(24 pi) = 1/sqrt(2)`.

This is the exact cancellation that the cruder Ball bound missed.

### Case II: one coefficient has `a_1^2 > 8/9`

There can be at most one such coefficient. Put `a=|a_1|` and

`R=sum_{i>=2} a_i U_i`.

Conditioning on `R`,

`F(a_1,...,a_r)= E_R integral_{-1/2}^{1/2} exp[-6(a u+R)^2] du`.

For fixed `a`, the displayed integral is the convolution of two symmetric decreasing functions evaluated at `R`; hence it is maximized at `R=0`. Thus

`F(a_1,...,a_r) <= H(a):=integral_{-1/2}^{1/2} e^{-6a^2u^2}du`.          (3.7)

The function `H(a)` is strictly decreasing for `a>0`. Since `a>sqrt(8/9)=2sqrt(2)/3`,

`F(a_1,...,a_r) < H(2sqrt(2)/3)`
` = [3 sqrt(pi)/(4 sqrt(3))] erf(2/sqrt(3))`.                          (3.8)

For completeness, this is strictly less than `1/sqrt(2)` by an entirely elementary rational certificate. The alternating series

`erf(x)=(2/sqrt(pi)) sum_{k>=0} (-1)^k x^(2k+1)/(k!(2k+1))`

has decreasing terms at `x=2/sqrt(3)`. Truncating after the positive `k=4` term gives an upper bound and yields

`H(2sqrt(2)/3) < 52933/76545 = 0.6915278594...`,

while exactly

`1/2 - (52933/76545)^2 = 255332047/11718274050 > 0`.

Hence `H(2sqrt(2)/3)<1/sqrt(2)`, proving (3.1) also in Case II.

The two cases exhaust all finite leverage vectors, proving (3.1) and therefore (3.2).

Finally, for equal weights `a_i=1/sqrt(r)`, the preceding B17 report proved

`C_r -> 3 sqrt(2)`

(and in fact `C_r=3sqrt(2)[1-3/(80r)-173/(17920r^2)+O(r^-3)]`). Hence the supremum over the entire finite collinear-heavy architecture is exactly `3sqrt(2)`. QED.

## 4. Source-valid finite target matrices

The branch has exact original-coordinate provenance. For integers `m,r>=1`, take a physical-to-spectral frame with

- `m` rows `e_1/sqrt(m)`,
- `m` rows `e_2/sqrt(m)`,
- heavy rows `a_i e_3`, `i=1,...,r`.

Because `sum a_i^2=1`,

`R^T R=I_3`.

Therefore

`A=R diag(1,1,-1)R^T`

has nonzero spectrum exactly `{1,1,-1}` at every finite `m`. Centered unit intervals in the two positive banks converge to the Gaussian coordinates used in `T_a`, while the heavy coordinates remain exact cap-one physical variables. Thus this theorem is a sharp restriction on an actual target-admissible witness family, not on an artificial post-rotation product model.

## 5. Application of the newest source: the formerly unpaid two-sheet side

The newest Claude source `COUNTEREXAMPLE_SEARCH.md` at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

proves its Theorem C: for exact rank three of signature `(+,+,-)`, the one-sheet side `s>=0` satisfies a dimension-free bound `p(s)<=pi sqrt(2)`, while it explicitly leaves the two-sheet side `s<0` unpaid in general.

The present branch theorem hits exactly that source-identified gap for the collinear-heavy architecture. The preceding exact shell rearrangement gives, for every `r>0`,

`p_{T_a}(-r^2)`
` <= (1/2) E exp[-sqrt(12) r |sum_i a_iU_i| - 6(sum_i a_iU_i)^2]`
` <= (1/2)F(a)`
` <= 1/(2sqrt(2))`.                                                    (5.1)

Hence in physical normalization

`boxed( sup_{s<0} p_Q(s) <= 3sqrt(2) )`                                (5.2)

for every limiting member of this source-valid branch. Together with Theorem C's independently proved one-sheet control, this shows that the exact-rank-three convex/two-sheet escape mechanism described in the newest source cannot occur through arbitrary finite fragmentation confined to a single minority-sign spectral direction. The full two-sheet problem for genuinely non-collinear product projections remains open.

## 6. Designated partner result applied

The completed designated partner account02/B17 result

`yspennstate/math-open-problems@50913ed00c5943aaf2772473cbf17ddcb5bed090:proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T204449Z-account02-B17-QFORM-r19/REPORT.md`

proves that for `delta>0`

`G_1^2+G_2^2-G_3^2-delta G_4^2`

has exact global density peak

`1/[2sqrt(2(1+delta))]`.

Apply that theorem to the equal-weight endpoint of the present sharp hierarchy. Appending a fourth **independent diffuse minority-sign bank** of eigenvalue `-delta` gives exact source-valid finite matrices with nonzero spectrum `{1,1,-1,-delta}` and

`boxed( lim_{r->infinity} C_{r,delta} = 3sqrt(2)/sqrt(1+delta) < 3sqrt(2). )`   (6.1)

For every finite `r`, convolution with the independent fourth-mode contribution also gives the unconditional branch bound

`C_{r,delta} <= C_r <= 3sqrt(2)`.                                      (6.2)

Thus the present exact `3sqrt(2)` ceiling and the partner's exact fourth-mode formula together show that a fixed independent Gaussianized minority-sign spectral tail not only fails to beat the barrier; it opens a strict asymptotic gap `(1+delta)^(-1/2)` at the only sharp endpoint of this entire collinear family.

## 7. Consequence for the witness search

The following source-valid mechanisms are now excluded as ways to force a universal constant above `3sqrt(2)`:

1. any finite number of macroscopic independent cap-one physical coordinates sharing one minority-sign spectral direction, with arbitrary translations or fragmented supports;
2. every output location in that architecture, including the two-sheet side;
3. the diffuse limit of arbitrary finite collinear fragmentation;
4. appending a fixed independent Gaussianized minority-sign spectral mode.

A witness above `3sqrt(2)`, if one exists, must therefore exploit a mechanism outside this architecture: genuinely non-collinear heavy rows spanning multiple spectral directions, a coupled tail sharing physical coordinates, a finite/mesoscopic non-Gaussian overshoot, or a different off-center geometry.

## 8. Full-target status

- Full QFORM universal bound: `OPEN / NOT PROVED`.
- Universal sharp constant: not proved to equal `3sqrt(2)`.
- Full continuity statement: separately open.
- No use is made of the refuted arbitrary-joint coarea bound, post-rotation independence, law-uniform pointwise stationary phase, worst conditional-density moments, fiber suprema, or universal physical-minor extraction.
- The only new external analytic input is the exact sinc-moment inequality (2.1), with its published `p>=9/4` scope retained.

The accompanying checker records the exact heavy-case rational certificate and numerical constants only; the proof above is analytic.
