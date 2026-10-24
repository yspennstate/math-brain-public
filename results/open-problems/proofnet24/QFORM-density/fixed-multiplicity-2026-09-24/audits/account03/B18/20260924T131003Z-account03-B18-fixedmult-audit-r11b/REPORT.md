# account03/B18 r11b — primary-source transfer, complete-audit continuation, and fixed-multiplicity improvements

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T131003Z-account03-B18-fixedmult-audit-r11b`  
Pinned baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Verdict

**PASS for the 17-eigenvalue bounded-density theorem in this B18 audit lineage.** I found no new mathematical defect in the pinned 790-line manuscript. The later owner objective requires all workers to audit this fixed-multiplicity manuscript and then lower the multiplicity as far as rigorously possible; it supersedes the older instruction to spend this run primarily on an unstructured three-eigenvalue attack.

The exact baseline theorem remains:

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s,
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinates whose densities are bounded by `K`. The proof makes no Gaussian, moment, support, iid, log-concavity, smoothness, sign, or diagonal-basis assumption.

The **full three-eigenvalue conjecture remains OPEN / NOT PROVED / NOT DISPROVED**, and full-target continuity remains OPEN.

This report is a continuation of this slot's preceding full end-to-end review rather than a claim of an additional independent reviewer. The preceding B18 review already checked every manuscript line and specialized dependency. In this continuation I rechecked the primary-source transfer, newly landed package material, newly landed peer improvements, and every baseline step touched by the sharper constants below.

## Package/readback status

The previously noted repository-package gap is now resolved. Fresh `master` contains `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, while the source manuscript blob remains exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

The newly executed reproducibility suite reports PASS with 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, 240 floating Schur-threshold diagnostics, and 30 floating graph-weight diagnostics. These computations are useful checks but are explicitly not formal verification and do not replace the written proof.

## Primary-source verification

### Rudelson--Vershynin

Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions* (arXiv:1402.4492), Theorem 1.2, gives the exact rough-law input needed here: if independent real `X_i` have densities bounded by `K` and `sum a_i^2=1`, then the density of `sum a_i X_i` is bounded by `sqrt(2)K`. It assumes no moments, centering, iid laws, log-concavity, support control, or smoothness.

From this theorem one obtains for every cap-one density `f` and every `p>=2`

\[
\int_{\mathbb R}|\widehat f(t)|^pdt\le {4\pi\over\sqrt p}.
\]

This is a source-valid replacement for the manuscript's self-contained but weaker scalar Fourier-power constant.

### Banks--Garza Vargas--Kulkarni--Srivastava

Banks--Garza Vargas--Kulkarni--Srivastava, arXiv:2005.08930, Theorem 2.1 and Corollary 2.4, give direct prior art for bounded-density **bilinear-affine** forms of two independent bounded-density random matrices. In scalar output they control the law using at least two singular directions of the bilinear coefficient.

This does **not** subsume the manuscript crossing theorem. A physical cut of a general quadratic form is

\[
F(X_I)+2X_I^TMX_J+G(X_J),
\]

with arbitrary same-bank phases `F,G`. Those phases disappear only after the manuscript's decoupling operation, which produces absolute scalar Fourier factors. The Banks et al. signed bilinear-affine theorem does not justify replacing this absolute majorant by a characteristic function. I therefore found no source-valid use of that theorem that closes the order-four heavy-leverage endpoint or proves an unconditional `s_13` bounded-density theorem.

### Herry--Malicet--Poly

The quadratic-form regularity results of Herry--Malicet--Poly impose iid inputs with a sufficiently smooth Gaussian-field representation. Those hypotheses do not match arbitrary rough, non-iid cap-one source densities, so that theory cannot be invoked for the present theorem without changing the target.

I found no exact published theorem among these checked primary sources that solves the owner's full arbitrary-law three-eigenvalue conjecture.

## New proved improvement 1: sharper graph determinant

Let

\[
Z=F(X_I)+2X_I^TMX_J+G(X_J)
\]

for disjoint original-coordinate product banks with cap-one densities and arbitrary measurable real `F,G`. Propagating the Rudelson--Vershynin Fourier-power bound through the manuscript's fourth-power decoupling and graph Brascamp--Lieb proof gives

\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+{t^2\over2\pi^2e}M^TM\right)^{-1/8}.
}
\]

The manuscript has the same exponent with coefficient `1/(pi^2 e^2)`; thus this is a strict quantitative strengthening with exactly the same hypotheses.

The complete derivation is in

`improvements/account03/B18/20260924T131003Z-account03-B18-fixedmult-audit-r11b/RV_SHARP_GRAPH_AND_CONSTANT_3810.md`.

## New proved improvement 2: leverage-gapped order-four endpoint

Let row leverage be

\[
\ell_i=m_i^T(M^TM)^+m_i.
\]

For `q in [1,2]`, if `max_i ell_i<=q/2`, the same source transfer and the manuscript's two-power decoupling yield

\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+{q t^2\over4\pi^2e}M^TM\right)^{-1/(4q)}.
}
\]

Consequently, if `Z_k(M)>0` and `k>2q`,

\[
\boxed{
\|p_Z\|_\infty
\le
2\sqrt{e/q}\,{k\over k-2q}
Z_k(M)^{-1/(2k)}.
}
\]

For the manuscript's order-four branch, a quantitative leverage gap `max ell_i<=1-delta`, `0<delta<=1/2`, gives

\[
\boxed{
\|p_Z\|_\infty
\le
{\sqrt{2e/(1-\delta)}\over\delta}
Z_4(M)^{-1/8}.
}
\]

In particular, if `max ell_i<=3/4`, the `s_13` random-cut witness satisfies

\[
\|p_Z\|_\infty
\le1280\sqrt{2e/3}<1724.
\]

This closes every order-four witness with a fixed row-leverage gap. It does **not** prove a same-scope `s_13` `L^infinity` theorem because the current spectral-to-volume/random-cut argument does not force such a gap for the same large-volume cut. The unresolved analytic state is precisely a heavy physical row with leverage arbitrarily close to one.

Independent exact counterexamples from account01/B08 and account02/B08 show that the manuscript's nonsymmetric completion estimates `rank R<=3r` and `rank R[L,L]<=r` are simultaneously sharp even in the no-pivot entry regime. Therefore the threshold cannot be lowered merely by replacing `3r` with `2r`, symmetrizing the interpolant, or retuning constants.

## New proved improvement 3: same-scope `s_17` constant 3810

The sharper determinant improves the manuscript quarter-power concentration lemma. If `L=||S||`, then

\[
\Pr\{|R-a|<\rho\}
\le
\min\{1,C_*(\rho/L)^{1/4}\},
\]

with

\[
C_*=2^{3/4}e^{1/4}\pi^{-1/4}\Gamma(3/8)<25/6.
\]

The elementary proof uses `Gamma(3/8)<5/2`, `e<11/4`, and `pi>3`. Since `log C_*<3/2`, the translated logarithmic potential satisfies

\[
\sup_a E\log_+{1\over|R-a|}<10
\quad (L\ge1).
\]

Feeding this into the pinned scalar-pivot/kernel argument gives, under `s_9(A)>=1`,

\[
\sup_a E|Q-a|^{-1/2}<381.
\]

The main `s_17` scalar-pivot branch therefore has

\[
\|p_Q\|_\infty<3810
\]

in the normalized case. The no-pivot, definite-pair and indefinite-pair branches are all smaller. Scaling exactly as in the manuscript proves the same-scope theorem

\[
\boxed{
 s_{17}(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_\infty
 <3810\,{K^2\over s}.
}
\]

This improves the manuscript's `10000`, this slot's preceding `5338`, and the concurrent account03/B19 `3910`, without changing any hypothesis. Continuity is not newly asserted for pivot branches.

## Applied peer result: thirteen-eigenvalue L2 theorem

During this run, account04/B01 committed a new theorem: under `s_13(A)>=s`, the same arbitrary rough product-law quadratic polynomial has an `L^2` density. The no-pivot branch uses order-four Fourier decay `1/|t|`, which is square-integrable even though it is not absolutely integrable.

Applying the new B18 graph determinant and the improved pivot constants to that proof gives the stronger quantitative theorem

\[
\boxed{
 s_{13}(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_2
 <\sqrt{3810}\,{K\over\sqrt s}.
}
\]

In the normalized no-pivot branch the sharpened order-four envelope gives

\[
\|p_Q\|_2^2\le320\sqrt{2e}<747,
\]

whereas the pivot branches are bounded by `3810` via `L^infinity`. The full proof is in

`improvements/account03/B18/20260924T131003Z-account03-B18-fixedmult-audit-r11b/PEER_S13_L2_TRANSFER.md`.

This is a genuine threshold reduction for **existence plus dimension-free L2 regularity**, not for bounded density. The completed same-scope `L^infinity` threshold remains 17 in the proof chain verified here.

## Status ledger

- Pinned `s_17` bounded-density theorem: **PASS in this B18 audit lineage**.
- Same-scope constant `10000 -> 3810`: **PROVED**.
- `s_13` dimension-free `L^2` density theorem: **PROVED by account04/B01; source-sharp constant transfer applied here to obtain `sqrt(3810)`**.
- `s_13` `L^infinity` under a fixed order-four row-leverage gap: **PROVED conditional branch**.
- Unconditional `s_13` `L^infinity`: **OPEN**.
- Full three-eigenvalue `L^infinity` conjecture: **OPEN**.
- Full-target continuity: **OPEN**.
- Exact published solution matching all arbitrary-law quantifiers: **NOT FOUND in the primary sources checked**.

## Next obligation

The immediate fixed-multiplicity `L^infinity` obstruction is no longer the generic order-four cut. It is the heavy-leverage endpoint: an order-four cut with quantitatively large crossing volume but with a physical row whose leverage can approach one. A successful next mechanism must either

1. route this heavy row to a literal-coordinate hub/curved-fiber receiver while retaining arbitrary same-bank phases and all small nonzero coefficients, or
2. prove a product-preserving repartition theorem that creates a quantitative leverage gap without destroying the order-four crossing-volume lower bound.

The simultaneous-sharpness examples for the interpolation ranks show that a purely algebraic rank tightening of the existing completion cannot supply this reduction by itself.

No schedule state, notification state, email, public release, cross-account authentication, paid API/model action, remote workflow, installation, or permission was changed in this run.
