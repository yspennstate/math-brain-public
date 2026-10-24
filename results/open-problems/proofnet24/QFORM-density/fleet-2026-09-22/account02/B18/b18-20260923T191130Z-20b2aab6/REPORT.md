# account02/B18 — equal-spectrum null-hub rigidity and the low-hub-leverage stress family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `b18-20260923T191130Z-20b2aab6`  
Status: **PROVED SUPPORTING TARGET-LEVEL SUBCLASS CLOSURE + TARGET-VALID COMPILER STRESS; FULL QFORM OPEN**.  
Continuity: only where inherited from the cited partner theorem; no global continuity claim.

## First unpaid implication

The genuinely new remaining interface isolated here is **not** the tiny-edge heavy collar at condition number one and moderate hub leverage: that collar is empty. The equal-magnitude exact-rank-three null-hub sector with hub range leverage `h>=1/5` is uniformly paid below by an explicit constant.

What remains even inside the condition-number-one null-hub model is the **low hub range leverage `h -> 0` sector**. An explicit exact target family below simultaneously has spectrum `{-1,1,1}`, a null physical hub, a transverse-heavy leaf `q_i -> 1`, a nonzero physical hub edge `g_i -> 0`, zero distinguished physical diagonal, and vanishing residual nonplanar leakage. Thus the `h>=1/5` hypothesis in the closure is a real geometric boundary for the present compiler, not merely a loose estimate. The family is **not** a QFORM counterexample.

The unrestricted owner target, arbitrary independent one-dimensional densities bounded by one and arbitrary symmetric `A` with at least three eigenvalues of modulus at least one, remains OPEN.

---

## 1. Setup: exact null-hub normal form

Use the completed exact null-hub normal form

`Q = 2 (X_0 + ell . X_L)(g . X_L) + d (beta . X_L)^2`,  
`||beta||_2=1`, `beta . g=0`, `gamma=||g||_2>0`.

Write `n=g/gamma`. Decompose the deterministic twist coefficient as

`ell = a n + b beta + kappa e`,

where `e` is a unit vector orthogonal to both `n,beta` when `kappa>0` (and can be chosen arbitrarily in that orthogonal complement when `kappa=0`). Set

`s = sqrt(1+kappa^2)`, `p=(e_0+kappa e)/s`.

Then `p,n,beta` are deterministic orthonormal vectors in the physical coordinate space, and on their span the quadratic matrix is represented by

`M = [[0, s gamma, 0],
      [s gamma, 2a gamma, b gamma],
      [0, b gamma, d]]`.                                      (1)

No random-coordinate rotation is being made: this is only coefficient-space algebra for the physical matrix. The original random variables remain the independent coordinates `X_j`.

For a leaf `i` put

`x_i=n_i`, `y_i=beta_i`, `z_i=e_i`,
`q_i=x_i^2+y_i^2`.

The physical hub edge and leaf diagonal are

`g_i=A_{0i}=gamma x_i`,
`A_{ii}=2 kappa gamma z_i x_i + y_i^2`.                        (2)

---

## 2. New rigidity theorem at exact condition number one

### Theorem `QFORM-EQUAL-SPECTRUM-NULLHUB-RIGIDITY-v1`

Assume the exact-rank-three physical matrix has a nonzero null hub `A_{00}=0`, and after multiplying `A` by `-1` if necessary its three nonzero eigenvalues are exactly

`{-1,1,1}`.

Then in the null-hub normal form above one necessarily has

`d=1`, `a=0`, `b=0`, `s gamma=1`.                              (3)

Equivalently,

`ell = kappa e`, `gamma=(1+kappa^2)^(-1/2)`,

and

`A = p n^T + n p^T + beta beta^T`,                             (4)

where

`p = gamma e_0 + sqrt(1-gamma^2) e`

is unit and orthogonal to `n,beta`.

In particular the hub range leverage is exactly

`h = ||P_range(A)e_0||^2 = gamma^2`,                            (5)

and for every original-coordinate leaf

`A_{ii}=2 sqrt(1-h) z_i x_i + y_i^2`,
`g_i=sqrt(h) x_i`,
`q_i=x_i^2+y_i^2`.                                             (6)

### Proof

For (1), the three elementary spectral invariants under the target spectrum `{-1,1,1}` are

`tr M = 1`, `det M = -1`, `e_2(M)=-1`.

They give

`2a gamma + d = 1`,                                           (7)
`d (s gamma)^2 = 1`,                                          (8)
`-(s gamma)^2 + 2a gamma d - b^2 gamma^2 = -1`.              (9)

Because (8) implies `d>0` and `(s gamma)^2=1/d`, substitute (7)-(8) into (9):

`b^2 gamma^2
 = 1 - 1/d + d - d^2
 = -((d-1)^2(d+1))/d <= 0`.                                   (10)

The left side is nonnegative, so equality forces `d=1` and `b=0`. Then (8) gives `s gamma=1`, and (7) gives `a=0`. This proves (3). Formula (4) follows because `u=e_0+ell=s p` and `g=gamma n` with `s gamma=1`. Since the active range is `span{p,n,beta}` and `<e_0,p>=gamma`, (5) follows. Equation (6) is (2) with `kappa gamma=sqrt(1-h)`.

This rigidity is purely deterministic matrix algebra; it uses no distributional assumption.

---

## 3. New tiny-edge exclusion in the moderate-hub sector

### Theorem `QFORM-EQUAL-SPECTRUM-TINYEDGE-HEAVY-EXCLUSION-v1`

Under the hypotheses of the rigidity theorem, assume

`h >= 1/5`, `|A_{ii}| < 1/64`, and `|g_i| < 1/64`              (11)

for an original-coordinate leaf `i`. Then

`q_i < 5/4096 + (1+2 sqrt(5))/64
     = 0.08672282742186843... < 1/2`.                          (12)

Consequently, in the exact-spectrum `{-1,1,1}` null-hub model with `h>=1/5`, a transverse-heavy leaf `q_i>1/2` and a small physical diagonal `|A_{ii}|<1/64` **cannot** lie in the punctured tiny-edge state `0<|g_i|<1/64` (nor at `g_i=0`).

### Proof

From `g_i=sqrt(h)x_i` and `h>=1/5`, (11) gives

`|x_i| < sqrt(5)/64`.                                         (13)

From (6), `|z_i|<=1` and `sqrt(1-h)<=1`,

`y_i^2
 <= |A_{ii}| + 2 sqrt(1-h)|z_i x_i|
 < 1/64 + 2 sqrt(5)/64`.                                     (14)

Therefore

`q_i=x_i^2+y_i^2
 < 5/4096 + (1+2 sqrt(5))/64 < 1/2`,

as claimed.

This is the exact missing deterministic implication for the condition-number-one version of the live heavy punctured collar.

---

## 4. Transfer to a whole-line density bound on a genuine target subclass

### Theorem `QFORM-EQUAL-SPECTRUM-NULLHUB-MODERATEH-CLOSURE-v1`

Let `X_1,...,X_n` be arbitrary independent random variables with one-dimensional probability densities bounded by one. Let `A` be symmetric of exact rank three, with nonzero spectrum `{-1,1,1}` (up to global sign). Suppose an **original physical coordinate** `0` satisfies

`A_{00}=0`, `h=||P_range(A)e_0||^2 >= 1/5`.                   (15)

Then `Q=X^TAX` has an essential density and

`||p_Q||_infinity <= 1024`.                                  (16)

No moment, support, log-concavity, smoothness, iid, symmetry, diagonal-basis, or post-rotation independence assumption is used.

### Proof by source-valid branches

**Branch A: a nonzero physical diagonal is not tiny.** If some original coordinate `k` has

`|A_{kk}| >= 1/64`,

apply the completed scalar-square/Schur-half-Riesz estimate from account02/B18:

`||p_Q||_infinity <= 128 [c_k |det M| |A_{kk}|]^(-1/4)`,       (17)

where `c_k` is the physical spectral-row leverage. Here `|det M|=1`, and since the coefficient-space matrix has operator norm one,

`|A_{kk}| <= c_k`.

Hence `c_k |A_{kk}| >= (1/64)^2=1/4096`, and

`||p_Q||_infinity <= 128 * 4096^(1/4) = 1024`.                (18)

This branch is completely in original coordinates.

**Branch B: all physical diagonals are tiny and all residual transverse leverages are diffuse.** Assume now `|A_{kk}|<1/64` for every leaf. If

`max_i q_i <= 1/2`,

apply the completed designated-partner account03/B18 `QFORM-SCHUR-NULLHUB-TRANSVERSE-COMPILER-v1` (r28). Its exact determinant currency is `h |pdet A|`; here `|pdet A|=1`, so

`||p_Q||_infinity
 <= 3*2^(4/3) h^(-1/3)
 <= 3*2^(4/3)5^(1/3)
 = 12.9266081401913...`.                                     (19)

This branch has a continuous `C_0` density by the partner theorem. The theorem acts on the original-coordinate product amplitude and does not assert independence after coefficient-space rotation.

**Branch C: a transverse-heavy residual leaf exists.** Suppose some original leaf has `q_i>1/2`. By the tiny-edge exclusion theorem and `|A_{ii}|<1/64`, necessarily

`|g_i| >= 1/64`.                                              (20)

Now apply the completed corrected account04/B18 r4 physical-pair/Schur result. In its notation, the target determinant currency satisfies

`h D q_i > (1/5)(1)(1/2)=1/10`,

while `|A_{ii}|<1/64` and (20) imply the physical pair singular-value lower bound used there. Its explicit conclusion is

`||p_Q||_infinity < 64.17958261516226`.                       (21)

Thus all branches are paid, and the coarse uniform constant `1024` in (16) follows.

### Scope boundary

This is a **subclass theorem**, not the full owner target: it assumes exact rank three, exact equal-magnitude nonzero spectrum, an original physical null hub, and `h>=1/5`. Arbitrary eigenvalue ratios, arbitrary extra spectrum, and the low-hub-leverage `h<1/5` sector remain outside this closure.

The latest account03/B18 r32 source-separated theorem was checked but is not silently applied here: generic rigid twists `ell=kappa e` need not satisfy its literal original-coordinate partition/alignment hypothesis. The compatible r28 theorem is the correct partner transfer for Branch B.

---

## 5. Target-valid low-hub-leverage stress family

The preceding `h>=1/5` threshold cannot simply be discarded by the same edge argument. Here is an exact target family entering the simultaneous degeneracy as `h->0`.

Fix `0<eta<1/64`, set

`c=sqrt(1-eta^2)`, `kappa=c/eta`, `gamma=eta`.                 (22)

Choose a distinguished leaf row of an orthonormal three-frame `(n,beta,e)` by

`z=-eta`,
`x=sqrt(1-eta^4-eta^6)-c eta`,
`y=sqrt(2 c eta x)`.                                         (23)

For small `eta` this has `x>0`, and exactly

`x^2+y^2+z^2 = 1-eta^6`.                                    (24)

Indeed `x` is the positive root of

`x^2+2c eta x+eta^2 = 1-eta^6`.                              (25)

Complete this row to orthonormal columns `n,beta,e`. One concrete diffuse completion is as follows. Let

`G=I_3-r r^T`, `r=(x,y,z)`.

Then `G` is positive definite with eigenvalues `1,1,eta^6`. For any Hadamard order `m`, let `W` be the first three normalized Hadamard columns, so `W^T W=I_3` and every row has squared norm `3/m`. Put the remaining frame matrix

`R_res = W G^(1/2)`.                                         (26)

Then `R_res^T R_res=G`; adding the distinguished row `r` gives three orthonormal columns. Every diffuse residual row `r_j` satisfies

`||r_j||^2 <= 3/m`.                                          (27)

Now define, in genuine physical/original coordinates,

`u=e_0+kappa e`, `g=eta n`, `d=1`,
`A = u g^T + g u^T + beta beta^T`.                           (28)

Since

`p=eta u=eta e_0+c e`

is unit and orthogonal to `n,beta`, (28) becomes exactly

`A = p n^T+n p^T+beta beta^T`.                               (29)

Therefore for **every** `eta,m`

`spec_nonzero(A)={-1,1,1}`.                                  (30)

This is a genuine owner-target matrix; no rotated-coordinate independence is being asserted.

For the distinguished leaf `*`, equations (23)-(25) give

`A_** = 2 kappa z (eta x)+y^2
      = -2c eta x+2c eta x=0`,                               (31)

`g_* = eta x ->0`,                                           (32)

`q_* = x^2+y^2 = 1-eta^2-eta^6 ->1`,                         (33)

while the hub range leverage is

`h=eta^2 ->0`.                                                (34)

Thus the exact heavy tiny-edge state is genuinely realizable once hub leverage is allowed to vanish.

Moreover, after deleting the distinguished leaf, the nonplanar part of the twist also degenerates. By the Gram-determinant/Schur-complement identity,

`dist(e_-*, span{n_-*,beta_-*})^2
 = det Gram(n_-*,beta_-*,e_-*) / det Gram(n_-*,beta_-*)
 = eta^6/(eta^2+eta^6)
 = eta^4/(1+eta^4)`.                                         (35)

Hence the residual nonplanar twist size is

`kappa_perp
 = kappa * eta^2/sqrt(1+eta^4)
 = c eta/sqrt(1+eta^4) ->0`.                                 (36)

At the same time the planar gap is

`1-q_* = eta^2+eta^6 ->0`.                                   (37)

So the physical-pair receiver (`sigma_min ~ eta`), the prior planar-gap receiver, and the prior nonplanar-leakage receiver can all deteriorate simultaneously on exact target matrices.

The diffuse completion also removes a large-diagonal escape: for each non-distinguished residual leaf,

`|A_{jj}|=|2c e_j n_j+beta_j^2|
 <= e_j^2+n_j^2+beta_j^2
 <= 3/m`.                                                     (38)

Thus choosing `m>192` makes every residual diagonal `<1/64`, while the hub and distinguished diagonals are exactly zero. More generally every residual-residual physical entry is bounded by the product of the corresponding active-row norms, hence is `O(1/m)`, and every distinguished-residual entry is `O(m^(-1/2))`; fixed pair-minor no-pivot thresholds can therefore also be forced by taking `m` large after `eta` is fixed.

This family is a **counterexample to the shortcut** “exact condition-number-one spectrum plus null hub automatically prevents the simultaneous tiny-edge/heavy/low-leakage geometry.” It is **not** a counterexample to QFORM.

---

## 6. Required pinned result applied to a real inequality

The pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` `COUNTEREXAMPLE_SEARCH.md` proves the ruled one-sheet theorem for exact rank-three signature `(2+,1-)`: if the nonzero eigenvalue moduli are at least one, then on the one-sheet sign

`p_Q(t) <= pi sqrt(2)` a.e.                                   (39)

(with the sign reversed after replacing `A` by `-A`).

Applying it literally to the stress family (29)-(30) gives

`p_{Q_eta,m}(t) <= pi sqrt(2)` for a.e. `t>=0`.                (40)

Thus the stress family does not challenge the already-paid one-sheet side. Any difficulty it exposes is specifically the minority-sign/two-sheet side and the product-provenance-preserving compilation needed there.

The pinned `RESULTS.md` / `FOURIER_ROUTE_REPORT.md` were also reread. Their arbitrary-joint three-dimensional coarea shortcut is explicitly false, while Theorems F/D are product-amplitude Fourier statements. None of the new arguments above replaces the product law by an arbitrary bounded joint density.

---

## 7. Primary-source transfer audit

The only external projection theorem needed by the partner route is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1. Its hypothesis is a genuine product probability density

`f(x)=prod_i f_i(x_i)`

with bounded one-dimensional probability densities. For cap-one factors, every `k`-dimensional orthogonal marginal is bounded by

`2^(k/2)`.                                                    (41)

No moments, compact support, log-concavity, smoothness, iid, symmetry, or centering are assumed. The theorem bounds the **joint marginal density**; it does **not** make projected coordinates independent. In this report, independence is invoked only for disjoint original-coordinate sources in previously completed theorems that explicitly require it.

The latest account03/B18 r32 theorem has a stronger source-separation hypothesis: a literal original-coordinate partition `L=J disjoint_union K` with `g_K=beta_K=0` and `ell_J` aligned with `span{g_J,beta_J}`. The general rigid twist `ell=kappa e` above is orthogonal in coefficient space but need not satisfy this source partition, so r32 is not promoted to the general branch.

The newest interactive projection-only counterexample was also noted: even an independent hub plus all low-dimensional projection caps for an otherwise arbitrary dependent light triple does not prove the leakage endpoint. That is consistent with the present proof, which uses the actual original-coordinate product provenance only through already completed source-matching theorems.

---

## 8. Exact next debt

`QFORM-EQUAL-SPECTRUM-LOWHUB-TWOSHEET-v1`:

starting from the exact target representation

`A=p n^T+n p^T+beta beta^T`,
`p=eta e_0+sqrt(1-eta^2)e`,

with `eta ->0`, prove a whole-line universal bound by spending the original-coordinate product structure **before** converting the residual triple to generic projection caps. The explicit family (22)-(38) is the stress test. It has one-sheet density already bounded by `pi sqrt(2)`, but simultaneously defeats the present fixed physical-pair, planar-gap, nonplanar-leakage, and hub-leverage certificates.

Beyond this condition-number-one model, the full owner target still requires handling arbitrary nonzero eigenvalue ratios and arbitrary extra spectrum. Search misses are not novelty evidence; no counterexample to full QFORM is claimed.
