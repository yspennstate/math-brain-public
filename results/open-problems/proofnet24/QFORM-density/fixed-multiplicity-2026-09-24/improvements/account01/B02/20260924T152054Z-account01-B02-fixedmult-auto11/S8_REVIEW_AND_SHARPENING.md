# account01/B02 — independent reconstruction of the multiplicity-eight candidate, with a constant sharpening

Run: `20260924T152054Z-account01-B02-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **ONE INDEPENDENT COMPLETE PASS REVIEW OF AN `s_8` CANDIDATE; SECOND INDEPENDENT COMPLETE REVIEW STILL REQUIRED.**

## 1. Statement independently reconstructed

For arbitrary independent real coordinate densities `0<=f_i<=K`, arbitrary real symmetric `A`, arbitrary `b,c`, and `s_8(A)>=s>0`, the current candidate proof yields an essentially bounded density for

\[
 Q=X^TAX+b^TX+c.
\]

Keeping the exact third-volume receiver constant rather than rounding it to 15 gives the slightly sharper safe estimate

\[
 \boxed{\|p_Q\|_\infty<2371\,K^2/s.}
\]

Global continuity is **not** claimed. The no-pivot branches used below are continuous `C_0`; the scalar/pair-pivot branches establish absolute continuity and an essential bound.

The candidate was first assembled in account03/B07 commit `58fed0bc6bd949dd0a37cb462bfe38e77eda81c0`, using the terminal-collar, robust-anchor, incident-volume and one-high-leverage results listed below. This B02 report is an independent reconstruction/review, not authorship credit for the threshold.

## 2. Dependencies checked in this run

I checked the mathematical content needed from the following exact sources rather than relying on their status labels:

1. Current self-contained nine-eigenvalue paper `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`: grouped product-Fourier compiler, marginal-free `E_3` density receiver, five-eigenvalue full half-potential, scalar/definite/indefinite pivot estimates, Schur counts and scaling.
2. Eight-direction terminal collar `5dc3b183bf69c8ab69f725c4464d5073f5c803cd`: under `s_8>=1` and no old `eta=1/100` pivot, either `V_3>=kappa^3`, or good order-two seeds create two large completed diagonals and a two-sided collar; here `kappa=1/6400`.
3. Robust physical two-anchor extraction `0408c579bcda638e72c010ff99892a22b9049796`: in the small-`V_3` collar there is a literal two-coordinate anchor `H`, complement `L`, crossing `C=A[H,L]`, with
   \[
   g:=\det(CC^T)\ge d_0:=\delta_*^2/2=0.3649442658827020\ldots,
   \]
   where
   \[
   \delta_*={97\over100}-{297\sqrt2+3\sqrt{202}\over4000}.
   \]
4. Product-safe disjoint incident third-volume receiver `d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f`.
5. Zero/one-high leverage closure `74542593cca87e76d83b07f98e2c895f76b90796`.
6. Final two-high exclusion / assembly `58fed0bc6bd949dd0a37cb462bfe38e77eda81c0`.

All probabilistic conditioning remains on literal original coordinates. Orthogonal projections below are deterministic row-space devices only.

## 3. Independent proof reconstruction

Normalize `K=s=1`. Use the older collar pivot threshold

\[
 \eta={1\over100},\qquad \kappa={1\over6400}.
\]

A pivot is either `|A_ii|>=eta` or a principal two-coordinate determinant of modulus at least `eta`.

### 3.1 Scalar pivot

Suppose `|A_ii|>=eta`. Completing the square in the literal original coordinate gives

\[
 \|p_Q\|_\infty
 \le \eta^{-1/2}\sup_a\E|R-a|^{-1/2}.
\]

The scalar Schur complement retains at least seven unit spectral directions because `s_8(A)>=1`. In particular it has at least five, so Proposition 8.3 of the audited nine-eigenvalue paper applies. Its exact bound is

\[
 H_5\le \max\{70,16p^{-1/4},1+d^{-1/2}(J_0+2L_0)\},
\]
with `d=3/40`, `p=1/400`. Numerically this maximum is `<99`, and the coarser source-valid `<115` is already sufficient. Thus

\[
 \|p_Q\|_\infty<990
\]
(using the exact displayed maximum), certainly `<2371`.

No independence between the completed square and the Schur remainder is asserted; the estimate is the conditional density domination proved in the current paper.

### 3.2 Principal two-coordinate pivot

If a principal pair has determinant modulus `D>=eta=1/100`, then:

- if definite, conditioning on the complement and the exact two-dimensional Jacobian gives
  \[
  \|p_Q\|_\infty\le \pi/\sqrt D<32;
  \]
- if indefinite, its two-coordinate Schur complement retains at least six unit spectral directions, hence at least one. The audited hyperbolic-pair envelope and quarter-power logarithmic potential give
  \[
  \|p_Q\|_\infty
   \le 10(6+\log16+L_0)+1/e
   <193.
  \]

Thus every old-pivot branch is paid well below the eventual no-pivot constant.

### 3.3 No pivot: large disjoint third volume

Assume no old `eta` pivot. The terminal-collar theorem first proves

\[
 V_2(A)\ge\kappa^2.
\]

If

\[
 V_3(A)\ge\kappa^3,
\]
then a fair literal coordinate cut contains a physical crossing block `M` with

\[
 Z_3(M)\ge4^{-3}\kappa^3.
\]

The independently audited marginal-free third-volume receiver gives

\[
 \|p_Q\|_\infty
 \le C_3 Z_3(M)^{-1/6},
 \qquad C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots .
\]

Since `(4^{-3} kappa^3)^(-1/6)=160`,

\[
 \boxed{\|p_Q\|_\infty<160C_3
 =2370.93402605488\ldots<2371.}
\]

This branch has an integrable characteristic function and therefore a continuous `C_0` density.

### 3.4 No pivot: small third volume forces a robust physical two-anchor

Now assume `V_3<kappa^3`. The terminal-collar argument samples invertible disjoint two-seeds by determinant-squared weight. Since

\[
 \E\|F_B\|_F^2\le9V_3/V_2<9\kappa,
\]
seeds with `||F_B||_F^2<=18 kappa` carry at least half the order-two volume. For each good seed the completion has

\[
 \|E\|\le\sqrt{18\kappa}=:{\varepsilon_*},
 \quad \rank R\le6,
 \quad \rank R[L,L]\le2.
\]

From `s_8(A)>=1`, rank shift forces two completed diagonal coordinates with modulus at least `1-epsilon_*`. On their literal two-set `H`, the interpolation block is quantitatively invertible:

\[
 |\det P_B[H,H]|\ge\delta_*>0.
\]

Writing `P_B[H,H]=A[H,T]B^{-1}A[S,H]`, determinant multiplication gives a two-sided collar. Summing the selected good seeds and then aggregating by the anchor `H` yields a literal two-coordinate anchor with

\[
 C=A[H,H^c],\qquad
 g=\det(CC^T)\ge d_0=\delta_*^2/2.
\]

I checked the aggregation step: `sum_H det(C_HC_H^T)=V_2`, the assigned good-seed mass is at least `V_2/2`, and the collar product is bounded above by the square of the complete anchor two-volume, yielding exactly `g>=delta_*^2/2`.

### 3.5 Leverage decomposition and disjoint incident third volume

Let

\[
 Q_C=C^T(CC^T)^{-1}C,
 \qquad q_i=(Q_C)_{ii},
 \qquad P=I-Q_C,
\]
so `Q_C` is a rank-two orthogonal projection and `sum_i q_i=2`.

For each complement row `d_i` of `D=A[H^c,H^c]`, put `r_i=d_iP`. The exact Cauchy–Binet/leverage identity is

\[
 W_i
 =g\bigl((1-q_i)\|r_i\|_2^2-r_{ii}^2\bigr),
\]
where `W_i` is the sum of squared literal anchored `3x3` minors whose row coordinate `i` is excluded from the three column coordinates. These are product-usable disjoint incident minors.

Define the high-leverage set

\[
 J=\{i:q_i>2/3\}.
\]
Since the leverage scores sum to two, `|J|<=2`.

If `|J|<=1`, define the leverage-corrected diagonal coefficients on low-leverage rows by

\[
 \lambda_i={r_{ii}\over1-q_i},
\]
set the high-row coefficient to zero, and let `E` contain the corresponding residual rows. Then

\[
 \|E\|_F^2\le{3W_{\rm dis}\over g}.
\]

If `W_dis<=g/48`, then `||E||_F<=1/4`. The remainder decomposes as `A=D_0+R+E` with

\[
 \rank R\le4+|J|\le5,
 \qquad \rank R[U,U]\le2
\]
for the low-leverage set `U`. Rank perturbation from `s_8(A)>=1` forces at least three low coordinates with `|lambda_i|>=3/4`. On any three of them,

\[
 |R_{ii}|>0.74,
 \qquad |R_{ij}|<\sqrt{\eta+\eta^2}+1/4<0.351.
\]

Thus the `3x3` restricted block is strictly row-diagonally dominant and invertible, contradicting `rank R[U,U]<=2`. Therefore

\[
 W_{\rm dis}>g/48.
\]

A fair cut of the four distinct coordinates in every incident minor preserves at least `1/16` of this volume. The grouped product-Fourier receiver then yields

\[
 \|p_Q\|_\infty
 <3\,2^{5/6}e^{2/3}(g/48)^{-1/6}
 \le23.479.
\]

This branch is continuous `C_0`.

### 3.6 The apparent two-high survivor is impossible

It remains only to show that `|J|=2` cannot occur in the robust no-pivot collar.

For physical complement columns `a<b`, define the determinantal weights

\[
 w_{ab}={\det(C_{\{a,b\}})^2\over g}.
\]

Cauchy–Binet and the rank-two determinantal inclusion identity give

\[
 \sum_{a<b}w_{ab}=1,
 \qquad q_i=\sum_{b\ne i}w_{ib}.
\]

If two distinct coordinates `i,j` both have leverage `>2/3`, inclusion–exclusion under this probability law forces

\[
 w_{ij}\ge q_i+q_j-1>1/3,
\]
so

\[
 \det(C_{\{i,j\}})^2>g/3.
\]

But every entry of this literal `2x2` cross minor is an off-diagonal coefficient of the original no-pivot matrix, hence

\[
 |A_{uv}|^2<\eta+\eta^2={101\over10000}.
\]

Therefore

\[
 |\det C_{\{i,j\}}|
 \le2(\eta+\eta^2)={101\over5000},
\quad
 \det(C_{\{i,j\}})^2<0.00040804.
\]

On the other hand `delta_*>4/5`, so

\[
 g/3\ge\delta_*^2/6>8/75>0.1,
\]
a contradiction. Hence

\[
 \boxed{|J|\le1.}
\]

The preceding incident-volume closure therefore pays every small-`V_3` robust-anchor state. This closes the no-pivot case.

### 3.7 Scaling

For general `K,s`, set `Y=KX` and

\[
 \widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

Then `s_8(A/s)>=1` and `Q=(s/K^2)\widetilde Q`, so density scaling turns the normalized `<2371` bound into

\[
 \boxed{\|p_Q\|_\infty<2371K^2/s.}
\]

Every original input hypothesis is preserved.

## 4. Independent-review verdict for multiplicity eight

**PASS as a candidate proof in this B02 reconstruction.** I found no mathematical gap in the dependency chain above and no use of post-rotation independence, moments, bounded support, Gaussianity, log-concavity, connected support, exact rank, or a law-uniform pointwise quadratic oscillatory estimate.

However, under the owner protocol this is **only one independent complete review** of the newly assembled `s_8` theorem. The account03/B07 source is an authoring/assembly report and is not counted as an independent review. I have not verified a second genuinely separate complete reconstruction of the whole `s_8` chain after its assembly. Therefore:

- multiplicity 8: **CANDIDATE + ONE INDEPENDENT COMPLETE PASS REVIEW; NOT YET INDEPENDENTLY VALIDATED**;
- multiplicity 9 / constant 400: separately has two complete PASS reviews after the accompanying B02 audit and account01/B20 review;
- multiplicity 7: **GAP / NOT PROVED**;
- multiplicity 3: **OPEN**.

## 5. Why this run does not lower to seven

The known `s_7` no-pivot reductions retain either a paid `V_3` branch or an invertible-seed overlap-one packet together with nested literal physical stars. They do not yet supply a dependence-safe receiver for a same-index overlapping third minor. The obstruction is structural: the shared original coordinate cannot simultaneously be placed in two independent banks. Conditioning it away leaves only an order-two crossing, while duplicating it without a valid decoupling argument invents independence. The existing multi-deletion/star rigidity does not prove that the three stars form a nondegenerate physical third compound.

Thus no complete `s_7` proof follows from the currently checked identities. The first missing implication remains a product-preserving analytic receiver that spends the overlap-one/shared-coordinate currency while retaining the nested star information, or an alternative structural conversion to already-paid disjoint `E_3` currency.

MODEL: GPT-5.6 Sol. Effort/reasoning telemetry: UNKNOWN / not exposed.
