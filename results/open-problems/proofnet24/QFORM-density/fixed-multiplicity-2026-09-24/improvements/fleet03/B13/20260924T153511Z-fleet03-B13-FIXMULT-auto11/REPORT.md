SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-24T15:35:11Z.
attacking: full B13 audit of the current nine-eigenvalue source, then a retuned multiplicity-eight proof with explicit constants and an extremal-product geometric formulation.

# fleet03/B13 auto11 — complete pair audit and candidate multiplicity-eight bound below 349

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Execution label: **WITHOUT_VERIFIED_BRAIN**.

## 0. Result and review status

Pinned source audited in full: `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.

Verdict on that 955-line source: **PASS**. I found no fatal mathematical defect. I checked the theorem/scaling, Fourier/Riesz normalization, heat-flow Brascamp--Lieb proof, product projection, scalar Fourier powers, decoupling, determinant estimate, grouped mollified-`L^2` compiler, entropy step, Schur counts, nonsymmetric interpolation and both rank bounds, scalar/definite/indefinite pivots, full pair half potential, no-pivot spectral-to-volume conversion, final assembly, and overlap-tail theorem.

The already assembled `s_8` chain has two later independent complete PASS reports visible in the repository: fleet03/B08 at `2bf752b5944536f51357d3d3b8b17212a297c7a6` and fleet03/B18 at `d4eee5296bcc7fea885435e9cee72379d0e902eb`. I independently rederived the structural inequalities used below.

**New candidate in this run:**

\[
\boxed{
s_8(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}<349\,{K^2\over s}
}
\tag{0.1}
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary affine `b,c`, and arbitrary independent real coordinate densities bounded by `K`. No support, moment, iid, Gaussian, log-concavity, sign or diagonal-basis hypothesis is added.

The **new constant-349 retune requires two independent end-to-end reviews before promotion**. The unrestricted three-large-eigenvalue conjecture remains open. Global continuity is not proved; the no-pivot Fourier branches below are `C_0`, while the pivot assembly gives essential boundedness.

The current objective names `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json` under the pinned nine-400 subdirectory, but at the pinned source commit that directory contains only `paper.tex` and `NINE_400_AND_OVERLAP.md`. This is a package/reproducibility discrepancy, not a proof gap, because the specialized mathematics is self-contained in `paper.tex`.

## 1. B13 hyperbolic check

The source hyperbolic proof is correct for both signs and arbitrary rough independent cap-one laws. It actually proves before its final relaxation that each branch integral is at most

\[
{15\over2}\log2+\log_+{32\over |z-v|\Lambda}.
\]

Therefore the source envelope can harmlessly be sharpened to

\[
 p_q(z)\le D^{-1/2}\left({15\over2}\log2+
 \log_+{16\sqrt D\over|z-v|}\right),
\tag{1.1}
\]

using `Lambda>=2/sqrt(D)`. No random coordinate is rotated and the exceptional critical level is handled in the same nonnegative-test-function/Tonelli formulation as the source. This sharpening is not needed for (0.1).

## 2. Retuned five-direction full half potential

For the inner `s_5` receiver use

\[
 d={11\over40},\qquad p={9\over1000},\qquad
 h={107\over1000},\qquad \kappa_5=h^2.
\tag{2.1}
\]

In the inner no-pivot state,

\[
 |A_{ij}|<\sqrt{p+d^2}=\sqrt{677/8000}<291/1000.
\]

The order-two spectral-to-volume proof has only interpolation orders `r=0,1`. At `r=1` its restricted diagonal-dominance margin is

\[
1-d-{291\over1000}-4h={3\over500}>0,
\tag{2.2}
\]

while `d+h<1` pays `r=0`. Hence `s_5(A)>=1` and no inner pivot imply `V_2>=kappa_5^2`, so a fair physical cut has `Z_2>=kappa_5^2/16`.

The audited order-two half-potential constant is `C_2=8 sqrt(e) 2^{-1/8}`. Using

\[
e<{68\over25},\qquad 2^{-1/8}<{23\over25}
\]

(the latter is `25^8<2*23^8`), the no-pivot half potential is bounded by

\[
C_2\sqrt{2/h}<{105\over2}.
\tag{2.3}
\]

Indeed the square of the displayed rational majorant is

\[
{36835328\over13375}<{11025\over4}.
\]

For an inner pair pivot, the source full-pair theorem gives

\[
16p^{-1/4}<{105\over2},
\]

because

\[
{9\over1000}-\left({32\over105}\right)^4
={363037\over972405000}>0.
\]

For an inner scalar pivot the source gives

\[
1+d^{-1/2}(J_0+2L_0),\qquad
J_0=\pi+4\log2,\quad L_0=4+4\log5.
\]

The elementary bounds

\[
\pi<{22\over7},\quad \log2<{347\over500},\quad
\log5<{161\over100}
\]

give `J_0+2L_0<23449/875<27`. The logarithm bounds are certified by positive exponential Taylor partial sums:

\[
\sum_{k=0}^4{(347/500)^k\over k!}-2
={289173281\over1500000000000}>0,
\]

\[
\sum_{k=0}^7{(161/100)^k\over k!}-5
={11628664174467\over8000000000000000}>0.
\]

Finally

\[
1+{27\over\sqrt{11/40}}<{105\over2}
\]

because, after subtracting one and squaring, the exact margin is `59/44>0`.

Thus

\[
\boxed{
s_5(A)\ge1\implies
\sup_a\mathbb E|X^TAX+b^TX+c-a|^{-1/2}<{105\over2}.
}
\tag{2.4}
\]

All coordinates remain the original independent coordinates and all affine terms are retained.

## 3. Retuned eight-direction no-pivot collar

Use outer parameters

\[
\eta={1\over44},\qquad \kappa={1\over138}.
\tag{3.1}
\]

No outer pivot means

\[
|A_{ii}|<\eta,\qquad |A_{ij}|^2<\eta^2+\eta={45\over1936},
\qquad |A_{ij}|<a={3\sqrt5\over44}.
\tag{3.2}
\]

First `V_1>=kappa`: otherwise `||A||<eta+sqrt(kappa)<1`. Next `V_2>=kappa V_1`. If not, the order-one completion has `||E||<2sqrt(kappa)<2/11`, global rank at most three and restricted complement rank at most one. Rank perturbation from `s_8(A)>=1` forces two complement diagonal defects. Since `sqrt5<9/4`,

\[
|R_{ii}|>1-{2\over11}-{1\over44}={35\over44},
\qquad |R_{ij}|<{27\over176}+{2\over11}={59\over176},
\]

contradicting restricted rank one. Therefore

\[
V_2\ge\kappa V_1\ge\kappa^2.
\tag{3.3}
\]

If `V_3>=kappa^3`, Section 5 pays the density directly. Otherwise `V_3/V_2<kappa`. Determinant-squared sampling of order-two seeds and Markov retain at least half of `V_2` on seeds whose completion error obeys

\[
\varepsilon\le\sqrt{18\kappa}=\sqrt{3/23}.
\]

For each good seed, global rank at most six forces two complement diagonal defects. Their physical two-set `H` has interpolation collar determinant

\[
|\det P_B[H,H]|\ge
\delta=(1-\varepsilon-\eta)^2-(a+\varepsilon)^2.
\tag{3.4}
\]

We certify `delta>23/200`. Use

\[
{559\over250}<\sqrt5<{22361\over10000},\qquad
\sqrt{3/23}<{903\over2500}.
\]

Then

\[
1-\eta-a-2\varepsilon>{45061\over440000},
\qquad
1-\eta+a>{12427\over11000},
\]

so

\[
\delta>{559973047\over4840000000}
>{23\over200}.
\tag{3.5}
\]

The robust-anchor aggregation in the reviewed `s_8` chain therefore gives one literal two-set `H` with

\[
C=A[H,H^c],\qquad
 g:=\det(CC^T)>{\delta^2\over2}>{529\over80000}.
\tag{3.6}
\]

## 4. Retuned leverage closure

Let

\[
Q_C=C^T(CC^T)^{-1}C,\qquad q_i=(Q_C)_{ii},\qquad
w_{ij}={\det(C_{\{i,j\}})^2\over g}.
\]

Cauchy--Binet gives `sum w_ij=1` and the rank-two determinantal marginal identity gives

\[
q_i=\sum_{j\ne i}w_{ij}.
\tag{4.1}
\]

If two indices had `q_i,q_j>2/3`, then `w_ij>1/3` and hence

\[
\det(C_{\{i,j\}})^2>{g\over3}>{529\over240000}.
\]

But every entry of that physical cross minor is off-diagonal, so (3.2) gives

\[
\det(C_{\{i,j\}})^2<4(45/1936)^2={2025\over937024}.
\]

This is impossible because

\[
{529\over240000}-{2025\over937024}
={151339\over3513840000}>0.
\tag{4.2}
\]

Thus at most one complement coordinate has leverage above `2/3`.

For the low-leverage coordinates, the reviewed anchored-minor completion gives

\[
\|E\|_F^2\le {3W_{\rm dis}\over g},
\tag{4.3}
\]

with global remainder rank at most five and restricted low-low rank at most two. Suppose `W_dis<=g/75`. Then `||E||_F<=1/5`. Rank perturbation forces three low diagonal coefficients of modulus at least `4/5`. On those coordinates

\[
|R_{ii}|>{4\over5}-{1\over44}={171\over220},
\]

whereas

\[
\sum_{j\ne i}|R_{ij}|
<2\left({27\over176}+{1\over5}\right)
={311\over440}.
\]

The row-dominance margin is exactly `31/440>0`, contradicting restricted rank two. Hence

\[
\boxed{W_{\rm dis}>{g\over75}>{529\over6000000}>{1\over12000}.}
\tag{4.4}
\]

The existing product-coordinate-safe incident receiver gives

\[
\|p_Q\|_\infty\le
3\,2^{5/6}e^{2/3}W_{\rm dis}^{-1/6}<60,
\tag{4.5}
\]

because `2^(5/6)<2`, `e^(2/3)<2`, and `12000<5^6`. This terminal branch has an integrable Fourier majorant and a continuous `C_0` density.

## 5. Large-third-volume branch

If `V_3>=kappa^3`, a fair literal coordinate cut has `Z_3>=kappa^3/64`. The audited marginal-free order-three receiver gives

\[
\|p_Q\|_\infty\le 2C_3\sqrt{138},\qquad
C_3=3\sqrt2\,e\,(9/2)^{1/6}.
\]

Use

\[
\sqrt2<{99\over70},\quad e<{68\over25},\quad
(9/2)^{1/6}<{9\over7},\quad \sqrt{138}<{47\over4}.
\]

The cube-root bound is equivalent to `2*9^6-9*7^6=4041>0`; the square-root bounds are immediate. The exponential-series bound `e<68/25` follows by summing through degree six and bounding the tail beginning at `1/7!` by a geometric series with ratio `1/8`.

Therefore

\[
2C_3\sqrt{138}
<{2135727\over6125}=348.6901224\ldots<349.
\tag{5.1}
\]

This branch also has a continuous `C_0` density.

## 6. Pivot branches and complete assembly

Normalize first to density cap one and spectral scale one.

**Scalar pivot.** If `|A_ii|>=eta=1/44`, its Schur complement retains at least seven unit spectral directions, hence satisfies (2.4). The square profile gives

\[
\|p_Q\|_\infty<{105\over2}\sqrt{44}<349,
\]

because `349^2-44(105/2)^2=526>0`.

**Definite pair pivot.** Direct conditioning gives

\[
\|p_Q\|_\infty\le\pi\sqrt{44}<28.
\]

**Indefinite pair pivot.** The Schur complement retains at least six unit directions, so the source quarter-power logarithmic-potential estimate applies. Even retaining the source's relaxed coefficient `6`,

\[
\|p_Q\|_\infty
\le\sqrt{44}(6+\log16+L_0)+1/e<138
\]

using `sqrt44<7`, `log16<14/5`, `L_0<54/5`, and `1/e<1/2`.

**No pivot.** Sections 3--5 are exhaustive: either `V_3>=kappa^3`, yielding `<349`, or the collar branch yields `<60`.

Thus

\[
\boxed{s_8(A)\ge1\implies
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}<349.}
\tag{6.1}
\]

For general `K,s`, put `Y=KX` and normalize `A` by `s` exactly as in the pinned manuscript. Since `Q=(s/K^2)\widetilde Q`, density scaling proves the candidate theorem (0.1).

## 7. Designated fleet04/B13 result applied to the actual sublevel inequality

Fleet04/B13 proved the optimizer-free extremal-product identity (source commit `d1764f29884bf14ce505d36668105edfcaf8315e`): for every nonnegative slab kernel, the supremum over arbitrary cap-one probability densities equals the supremum over unit-measure product indicators, with bounded finite-union strict witnesses available by approximation and with no interval-extremality conclusion.

Applying that theorem to (6.1), for every real symmetric `A` with `s_8(A)>=1`, every affine `b,c`, and every interval `J`,

\[
\boxed{
\sup_{|E_i|=1}
\left|\left\{x\in\prod_iE_i:
 x^TAx+b^Tx+c\in J\right\}\right|<349|J|.
}
\tag{7.1}
\]

The identical supremum over arbitrary cap-one independent product densities is `<349|J|`. This is an actual geometric sublevel-set inequality and does not assume any `E_i` is an interval, centered, bounded in diameter, or has a bounded fragment count.

## 8. Dependency/review gate

Inputs retained with their original hypotheses:

- self-contained nine-eigenvalue analytic source: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- eight-direction terminal-collar skeleton: fleet03/B04 `5dc3b183bf69c8ab69f725c4464d5073f5c803cd`, rederived above at new parameters;
- reviewed robust-anchor and incident-volume chain: fleet03/B08 `2bf752b5944536f51357d3d3b8b17212a297c7a6` and fleet03/B18 `d4eee5296bcc7fea885435e9cee72379d0e902eb`;
- optimizer-free extremal-product reduction: fleet04/B13 `d1764f29884bf14ce505d36668105edfcaf8315e`.

The `<349` retune is **CANDIDATE_S8_349_PENDING_TWO_END_TO_END_REVIEWS**. Reviewers should specifically check the retuned five-direction constants, the outer `eta=1/44`, `kappa=1/138` collar, the exact `delta>23/200` certificate, the generalized `W_dis>g/75` one-high completion, and the full pivot assembly.

The next multiplicity target after validation is `s_7`. The unrestricted three-eigenvalue conjecture remains **OPEN / not proved / not disproved**.
