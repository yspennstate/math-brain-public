# account03/B10 — rank-three coupled case: nonisotropic-pivot closure

**Run:** `account03-B10-20260922T141643Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Rank-three coupled case  
**Classification:** `NEW EXACT-RANK-THREE SUPPORTING THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and corrections

The exact target is unchanged: independent real coordinates have densities bounded by one, and a real symmetric matrix has at least three eigenvalues of modulus at least one. The full arbitrary-matrix conjecture remains open.

This report treats **exact rank three**,

\[
A=U\Lambda U^T,\qquad U^TU=I_3,\qquad |\lambda_1|,|\lambda_2|,|\lambda_3|\ge1.
\]

No spectral rotation of the random vector is made. Every conditioning step is in original coordinates. The argument does not use the refuted law-uniform pointwise Fresnel decay, a receiver-only projection-density surrogate, or a naive fiber supremum. The linear bank used below has a bounded **marginal** density, but the two bank coordinates are allowed to be arbitrarily dependent.

Dependencies used at proof level:

1. account03/B09, `QFORM-SCHUR-RANK2-RECTANGULAR-v1` and its exact-rank-three Pluecker aggregation, `yspennstate/math-open-problems@ad5aac11726332af91f2f2680a10f755e22d08db`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T134741Z-account03-B09-QFORM-r12/REPORT.md`.
2. account03/B16, `QFORM-INDEFINITE-PRODUCT-FRACTIONAL-TRACE-v1`, especially its one-dimensional kernel `J_*` and weak-`L^2` ridge bound, `yspennstate/math-open-problems@1defc84f1bfd79994a103a6d683c887d9dead1e7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/B16-20260922T135620Z-r11/REPORT.md`.
3. compatible account04/B18, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` and `QFORM-SCHUR-PIVOT-SMOOTHING-v1`, `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.
4. The one-dimensional marginal-density theorem of Ball--Rogozin (equivalently the `k=1` case of sharp product marginal bounds): if independent coordinates have densities at most one and `b` is a unit vector, then `sum b_j X_j` has density at most `sqrt(2)`. A source spelling out this exact `sqrt(2)` statement is Rudelson--Vershynin, *Small ball probabilities for linear images of high-dimensional distributions*, Theorem 1.2; the result follows from Rogozin plus Ball's cube-slicing theorem.

The exact designated partner `account04/B10` had no completed current-QFORM handoff visible at the pre-publication refresh. No result is attributed to it. In accordance with the asynchronous instruction, the completed compatible account04/B18 theorem is applied below to an actual physical-triple inequality.

## 2. Rank-three Schur geometry after one physical pivot

Let `u^T` be row `i` of `U` and put

\[
\ell=\|u\|_2^2,\qquad d=u^T\Lambda u=A_{ii}.
\]

Assume for now that `d != 0`. Then `ell>0`. Let `P` be a `3 x 2` matrix whose columns form an orthonormal basis of `u^perp`. For every `k != i`, set

\[
v_k=P^T u_k\in\mathbb R^2,
\]

and let `W` be the matrix with rows `v_k^T`. Since the rows of `U` form a Parseval frame,

\[
W^TW=I_2. \tag{2.1}
\]

Complete the square in the original coordinate `X_i`. The Schur residual on the other physical coordinates is

\[
S=A_{\bar i,\bar i}-A_{\bar i,i}A_{i,\bar i}/d=W M W^T, \tag{2.2}
\]

where

\[
M=P^T\left(\Lambda-\frac{(\Lambda u)(\Lambda u)^T}{d}\right)P
\]

is invertible. The exact determinant identity proved in the B09 source is

\[
|\det M|=|\det\Lambda|\frac{\ell}{|d|}. \tag{2.3}
\]

Moreover the full quadratic form can be written as

\[
Q=d\left(X_i+\frac{A_{i,\bar i}X_{\bar i}}d\right)^2+R,
\qquad R=(W^T X_{\bar i})^T M(W^T X_{\bar i}). \tag{2.4}
\]

The translated `X_i` still has conditional density at most one for every fixed `X_{\bar i}`. Hence the square pushforward gives, for almost every `t`,

\[
p_Q(t)\le |d|^{-1/2}\,\mathbb E|t-R|^{-1/2}. \tag{2.5}
\]

Thus the unpaid problem after a nonisotropic pivot is a uniform fractional trace for the dependent two-dimensional frame projection `W^T X_{\bar i}`.

## 3. Random-shift residual trace lemma

The key point is that near-coloop residual frames can be paid without pretending their two projected coordinates are independent.

### Lemma 3.1 — `QFORM-RANDOM-SHIFT-RESIDUAL-TRACE-v1`

Let `W` be any Parseval two-frame with rows `v_k^T`, and let the physical coordinates `X_k` be independent with densities bounded by one. Choose a row `j` with

\[
q=\|v_j\|_2^2>0.
\]

Let `M` be any invertible symmetric `2 x 2` matrix. Then, with

\[
Z=W^T X,
\]

one has

\[
\sup_t\mathbb E|t-Z^TMZ|^{-1/2}
\le 16\sqrt{15}\,2^{1/4}\,(q|\det M|)^{-1/4}. \tag{3.1}
\]

More generally, if the normalized orthogonal bank below has density cap `K`, the factor `2^{1/4}` in (3.1) is replaced by `K^{1/2}`.

### Proof

Take an orthonormal basis `(e_1,e_2)` of `R^2` with `e_1=v_j/sqrt(q)`. For `k != j`, write

\[
v_k=a_ke_1+b_ke_2.
\]

The Parseval identity gives the exact relations

\[
\sum_{k\ne j}a_k^2=1-q,\qquad
\sum_{k\ne j}b_k^2=1,\qquad
\sum_{k\ne j}a_kb_k=0. \tag{3.2}
\]

Define bank variables

\[
L_1=\sum_{k\ne j}a_kX_k,\qquad L_2=\sum_{k\ne j}b_kX_k.
\]

Then

\[
Z=(\sqrt q\,X_j+L_1)e_1+L_2e_2. \tag{3.3}
\]

The crucial provenance facts are:

* `X_j` is independent of the whole bank `(L_1,L_2)`;
* `L_1` and `L_2` need **not** be independent;
* because the coefficient vector `(b_k)` has Euclidean norm one, Ball--Rogozin gives a marginal density for `L_2` bounded by `K=sqrt(2)`.

Write `M=[[a,b],[b,c]]` in the basis `(e_1,e_2)`.

#### Case 1: `a != 0`

For fixed bank values `(L_1,L_2)=(w,y)`,

\[
Z^TMZ
=a q\left[X_j+\frac{w+(b/a)y}{\sqrt q}\right]^2
+\frac{\det M}{a}y^2. \tag{3.4}
\]

Translation of `X_j` preserves its density cap. Let `J_*` be the cap-one square-root kernel from account03/B16,

\[
J_*(A)=\sup_{0\le f\le1,\ \int f=1}\int f(x)|A-x^2|^{-1/2}dx.
\]

Equation (3.4) yields pointwise in the **entire** bank

\[
\mathbb E_{X_j}|t-Z^TMZ|^{-1/2}
\le |a q|^{-1/2}J_*\!\left(\alpha\pm\delta y^2\right), \tag{3.5}
\]

where `alpha` depends on `t,a,q`, the sign is immaterial, and

\[
\delta=\frac{|\det M|}{a^2 q}. \tag{3.6}
\]

The B16 weak-`L^2` ridge estimate states, for a cap-one density `g`,

\[
\int g(y)J_*(\alpha\pm\delta y^2)dy
\le16\sqrt{15}\,\delta^{-1/4}. \tag{3.7}
\]

If `g` has cap `K`, scale `Y'=K Y`; its density is cap one and the quadratic coefficient becomes `delta/K^2`. Therefore

\[
\mathbb E J_*(\alpha\pm\delta L_2^2)
\le16\sqrt{15}\,K^{1/2}\delta^{-1/4}. \tag{3.8}
\]

Notice that no conditioning on `L_1` is used in (3.8): `L_1` disappeared into a translation before the bank was averaged. Combining (3.5)--(3.8),

\[
\sup_t\mathbb E|t-Z^TMZ|^{-1/2}
\le16\sqrt{15}\,K^{1/2}(q|\det M|)^{-1/4}. \tag{3.9}
\]

#### Case 2: `a=0`

Invertibility forces `b != 0` and `|det M|=b^2`. For fixed bank,

\[
Z^TMZ=2b\sqrt q\,L_2 X_j+\text{(bank-only term)}.
\]

For every cap-one probability density `f`, the bathtub principle gives

\[
\sup_s\int f(x)|s-\gamma x|^{-1/2}dx
\le2\sqrt2\,|\gamma|^{-1/2}. \tag{3.10}
\]

Thus the inner `X_j` expectation is at most

\[
2|b|^{-1/2}q^{-1/4}|L_2|^{-1/2}.
\]

For a probability density bounded by `K`, another bathtub bound gives

\[
\mathbb E|L_2|^{-1/2}\le2\sqrt{2K}. \tag{3.11}
\]

Hence this case is at most

\[
4\sqrt2 K^{1/2}(q|\det M|)^{-1/4},
\]

which is smaller than (3.9). Taking `K<=sqrt(2)` proves (3.1). QED.

### Why this lemma matters

The correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` rules out replacing a dependent projected pair by a bounded conditional-density surrogate. Lemma 3.1 does not do that. The potentially dependent `L_1` is frozen only long enough to translate the genuinely independent physical variable `X_j`; the only projection theorem used later is a one-dimensional **marginal** cap for `L_2`.

## 4. Main theorem: every nonisotropic physical pivot is uniformly paid

### Theorem 4.1 — `QFORM-RANK3-NONISOTROPIC-PIVOT-v1`

Let

\[
A=U\Lambda U^T,\quad U^TU=I_3,
\]

have exact rank three and `|lambda_r|>=1`. Let row `u_i` have leverage `ell_i>0` and diagonal quadratic coefficient

\[
d_i=u_i^T\Lambda u_i\ne0.
\]

Then for independent input coordinates with densities bounded by one,

\[
\boxed{
\|p_{X^TAX}\|_\infty
<97\,[|d_i|\,\ell_i\,|\det\Lambda|]^{-1/4}.
} \tag{4.1}
\]

Only an essentially bounded density is claimed; continuity is not proved by this theorem.

### Proof

Use the pivot geometry of Section 2 and the residual two-frame `W`.

Let `q_max=max_j ||v_j||^2`.

#### Branch A: `q_max >= 1/3`

Choose `j` attaining `q=q_max`. Lemma 3.1 and (2.3)--(2.5) give

\[
\begin{aligned}
\|p_Q\|_\infty
&\le16\sqrt{15}\,2^{1/4}q^{-1/4}|d|^{-1/2}|\det M|^{-1/4}\\
&=16\sqrt{15}\,2^{1/4}q^{-1/4}
   [|d|\ell|\det\Lambda|]^{-1/4}\\
&\le16\sqrt{15}\,6^{1/4}
   [|d|\ell|\det\Lambda|]^{-1/4}.
\end{aligned} \tag{4.2}
\]

Numerically `16 sqrt(15) 6^(1/4)=96.9847442244...<97`.

#### Branch B: `q_max < 1/3`

Use the completed B09 Pluecker-Schur theorem. For its residual Pluecker mass `R_2`,

\[
R_2\ge1-\sum_jq_j^2
\ge1-q_{max}\sum_jq_j
=1-2q_{max}>1/3, \tag{4.3}
\]

because a Parseval two-frame has `sum q_j=2`. B09 therefore gives

\[
\|p_Q\|_\infty
\le\frac{16\sqrt2}{3^{1/4}}
 [|d|\ell|\det\Lambda|]^{-1/4} R_2^{-1/8}
<19.724[|d|\ell|\det\Lambda|]^{-1/4}, \tag{4.4}
\]

again below the constant in (4.1).

The two branches are exhaustive, proving (4.1). QED.

### Interpretation

Before this run the exact-rank-three Schur/Pluecker route had two endpoint obstructions after choosing a nonzero pivot: small `d`, and collapse of disjoint residual Pluecker mass `R_2` through a near-coloop. Theorem 4.1 removes the second obstruction entirely. **Once a physical pivot has `d_i != 0`, residual frame concentration no longer causes a separate loss.** The surviving difficulty is the quantitative isotropic-pivot regime itself.

## 5. Completed account04 mathematics applied to an actual inequality

The completed compatible account04/B18 theorem gives a sharper payment whenever a concrete physical triple has definite Schur complement. In the notation above, choose two residual physical rows `j,k` with Pluecker weight

\[
w_{jk}=\det(W_{\{j,k\}})^2>0.
\]

If `W_{\{j,k\}} M W_{\{j,k\}}^T` is definite, the physical principal triple `B_{ijk}` has

\[
|\det B_{ijk}|=|\det\Lambda|\,\ell_i\,w_{jk}. \tag{5.1}
\]

Applying account04/B18 exactly as stated gives

\[
\boxed{
\|p_Q\|_\infty
\le2\sqrt\pi\,[|d_i|\ell_i|\det\Lambda|w_{jk}]^{-1/4}.
} \tag{5.2}
\]

This is an actual inequality, not a citation-only dependency. It can be much sharper than (4.1) when one physical residual basis has substantial Pluecker weight. It is not by itself dimension-free because `w_{jk}` may be arbitrarily small; Theorem 4.1 is precisely the aggregate replacement for that single-minor loss.

The exact assigned partner `account04/B10` had no completed QFORM artifact visible, so (5.2) is explicitly labeled a compatible-partner application rather than an assigned-partner result.

## 6. Exact-rank-three definite signature is now fully bounded

A useful target-level corollary follows by combining Theorem 4.1 with the completed diffuse-range theorem at `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Assume all three nonzero eigenvalues of exact-rank-three `A` have the same sign. If every row leverage satisfies `ell_i<=1/32`, the diffuse-range theorem gives the continuous-density bound

\[
\|p_Q\|_\infty<27. \tag{6.1}
\]

Otherwise choose `i` with `ell_i>1/32`. Definite signature and `min|lambda_r|>=1` imply

\[
|d_i|=|u_i^T\Lambda u_i|\ge\ell_i,
\qquad |\det\Lambda|\ge1. \tag{6.2}
\]

Theorem 4.1 yields

\[
\|p_Q\|_\infty<97\ell_i^{-1/2}<97\sqrt{32}<549. \tag{6.3}
\]

Therefore:

### Corollary 6.1

Every **exact-rank-three definite** quadratic form with all three nonzero eigenvalues of magnitude at least one, in arbitrary orientation and with arbitrary independent cap-one coordinate densities, has an essentially bounded density satisfying

\[
\boxed{\|p_Q\|_\infty<549.} \tag{6.4}
\]

This is substantially weaker than the diagonal constant `pi` but it is orientation-free. The argument establishes continuity only in the diffuse branch (6.1); no global continuous representative is claimed for the heavy-row branch.

## 7. Remaining exact-rank-three implication

The full exact-rank-three problem is now concentrated on **indefinite isotropic-pivot geometry**. Theorem 4.1 is useful whenever a row satisfies a quantitative lower bound on

\[
|d_i|\ell_i|\det\Lambda|.
\]

But for signatures `(2,1)` or `(1,2)`, rows can lie on or near the isotropic cone `u^T Lambda u=0`. In the extreme case every physical diagonal coefficient may vanish. A universal theorem must therefore prove one of the following without rotating away product independence:

1. a dimension-free lower/mixture payment over the nonzero `d_i` values, or
2. a genuinely hyperbolic two-coordinate/bank mechanism for the all-near-isotropic frame.

The present proof shows that **near-coloop residual concentration is no longer an independent obstruction once `d_i != 0`**. This is the first unpaid implication for the next B10 run.

## 8. Verification and status

Exact numerical diagnostics on random orthonormal `n x 3` frames checked to machine precision:

* `W^T W=I_2`;
* the Schur factorization `S=WMW^T`;
* `|det M|=|det Lambda| ell/|d|`;
* the constants `16 sqrt(15) 6^(1/4)=96.98474422447792` and the small-`q` B09 branch constant `19.723992269660204`.

These diagnostics are not proof certificates; Sections 2--6 are analytic.

Status:

* `QFORM-RANDOM-SHIFT-RESIDUAL-TRACE-v1`: **PROVED supporting lemma**.
* `QFORM-RANK3-NONISOTROPIC-PIVOT-v1`: **PROVED exact-rank-three supporting theorem**.
* exact-rank-three definite signature: **PROVED essentially bounded density, universal constant `<549`**.
* continuity for that entire definite branch: **NOT PROVED** (only the diffuse subbranch is continuous by the cited theorem).
* exact-rank-three indefinite signature: **OPEN** in the all-near-isotropic-pivot regime.
* full arbitrary-matrix QFORM conjecture: **OPEN / NOT PROVED**.
