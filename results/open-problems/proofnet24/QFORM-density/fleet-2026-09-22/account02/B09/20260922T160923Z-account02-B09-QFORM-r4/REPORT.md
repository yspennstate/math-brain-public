# account02/B09 — stable-rank random Schur cut for the bilinear block mechanism

**Run:** `20260922T160923Z-account02-B09-QFORM-r4`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** Bilinear block mechanism  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full target OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The sole target is the full arbitrary-product-law statement: for every dimension, independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite `C` such that

`P{X^T A X in L} <= C |L|`

for every interval `L`, or produce a genuine counterexample. No moment, support, sign, post-rotation independence, or small-tail assumption is introduced here.

At the start of this run the first unpaid B09 implication was to aggregate bilinear curvature **before** paying a reciprocal local determinant or scalar-coordinate cost. The newest owner continuation `QFORM-PROOF-FIRST-20260922T161801Z` specifically prioritizes an exhaustive product-preserving ridge-or-grouped-coordinate reduction. This run proves one quantitative branch of that reduction:

> `QFORM-PIVOT-OFFDIAG-STABLERANK-v1`: once a genuine physical square pivot exists, sufficiently large off-diagonal stable rank of its physical Schur complement forces a source-valid ridge certificate after one random coordinate cut, with no fixed-minor selection and a direct linear small-ball bound.

Combined with the completed `1/39` spectral-window/heavy-coordinate dichotomy, this closes the target branch in which a heavy coordinate is diagonal-dominant and its Schur complement has off-diagonal stable rank at least `24`. The residual is now the complementary heavy-bank / low-stable-rank routing problem.

## 2. Source-pinned completed inputs actually applied

### Named partner account03/B09

The latest complete partner result used here is

- repository/commit: `yspennstate/math-open-problems@62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T155042Z-qform12/REPORT.md`;
- theorem: `QFORM-PIVOT-RIDGE-BILINEAR-v1`.

For a genuine original-coordinate pivot `a=A_kk!=0`, let `S` be its scalar Schur complement, take a physical residual cross block `N=S[I,J]`, and for `gamma>0`, `1<=q<=2` put

`K=N N^T (gamma^2 I+N N^T)^(-1)`, `theta=tr K`, `D=det(I+N N^T/gamma^2)`.

If `max_i K_ii<=q/2` and `theta>q`, then `Q=X^TAX` has a bounded density. For every

`r in (max(1,2q/theta),2)`, `p=r/(r-1)`, `beta=theta/(2q)`,

the partner proves

`||p_Q||_inf <= |a|^(-1/2) P_r (2pi)^(-1/2) C_r^(r/2)
                 [2 t0 beta r/(beta r-1)]^(1/2)`,                 (2.1)

where

`P_r=1+(1-r/2)^(-1/r)`,
`C_r=r^(1/(2r))/p^(1/(2p))`,
`t0=[pi e sqrt(2/q)/(2 gamma)] D^(-1/(2theta))`.

This is an actual inequality used below, not merely a citation. Its proof completes the genuine physical square, applies a ridge Fourier envelope to the residual, then uses inverse Hausdorff--Young and a square-potential estimate. It does not incur a square-root small-ball exponent loss.

### Spectral-window / heavy-coordinate reduction

I also use the completed source-pinned consequence

- `yspennstate/math-open-problems@9c497213db0174f64450be250a62c5a97deb1ddf`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T155815Z-qform-r11b/ADDENDUM.md`,
- based on account03/B04 `QFORM-SPECTRAL-WINDOW-1OVER39-v1` at `yspennstate/math-open-problems@093c15486c794a2e8b23978ca7b289feabf999a7`.

For every target matrix `A`, either the full quadratic form already has a continuous density with

`||p_Q||_inf < 35.27`,                                               (2.2)

or there is an original coordinate `i` such that, writing `a=A_ii` and `b=A[i,i^c]`,

`max(|a|, ||b||_2) >= 1/312`.                                      (2.3)

The source proof preserves arbitrary smaller spectral directions and original-coordinate product provenance.

Live corrections consumed include the failures of law-uniform pointwise Fresnel decay, spectral-fiber suprema, post-rotation independence, a cross minor alone, transformed conditional density caps, one physical rank-two Schur extraction, and a local-good-block/rank-three-cut dichotomy. The newest correction `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1` also rules out direct averaging of two-pivot certificates against same-sign Pluecker weight. None of those refuted statements is used below.

## 3. Main theorem: off-diagonal Schur stable rank produces a ridge cut

### Theorem 3.1 — `QFORM-PIVOT-OFFDIAG-STABLERANK-v1`

Let `A` be any real symmetric matrix and let `k` be an original physical coordinate with

`a=A_kk != 0`.

Write the scalar Schur complement after completing that physical square as

`S=A_{-k,-k}-A_{-k,k}A_{k,-k}/a`.

Let

`s=||S||_op`,
`S^o=S-diag(S)`,
`rho=||S^o||_F^2/s^2`,                                             (3.1)

assuming `s>0`. If

`rho >= 24`,                                                       (3.2)

then for every independent cap-one product input law `Q=X^TAX` has an essentially bounded density satisfying

`boxed: ||p_Q||_inf <= C0 / sqrt(|a| s)`,                         (3.3)

where

`C0 = 3 [1+4^(2/3)] sqrt(e/2)
      [(3/2)^(1/3)/3^(1/6)]^(3/4)
    = 11.8757032583... < 11.876.`                                  (3.4)

Consequently every interval `L` obeys

`P{Q in L} <= 11.876 (|a|s)^(-1/2) |L|`.                         (3.5)

No rank restriction is imposed on `S`; arbitrary diagonal/self-block curvature and arbitrary additional spectral directions remain present. Continuity is not claimed by this endpoint.

### Proof

Choose a fair random physical coordinate cut `P | P^c` of the residual coordinates and set

`N=S[P,P^c]`.

Every unordered off-diagonal pair `{i,j}` is separated by the cut with probability `1/2`, and when it is separated exactly one copy of `S_ij` occurs in the rectangular matrix `N`. Therefore

`E_P ||N||_F^2
 = (1/2) sum_{i<j} S_ij^2
 = (1/4) ||S^o||_F^2.                                             (3.6)

Hence some deterministic physical cut satisfies

`||N||_F^2 >= rho s^2/4`.                                         (3.7)

Because `N` is a compression of `S`,

`||N||_op <= s`.                                                   (3.8)

Apply the named partner theorem (2.1) with

`gamma=s`, `q=2`.

The leverage gate is automatic: `0<=K<=I`, so `max_i K_ii<=1=q/2`. If `sigma_j` are the singular values of `N`, then

`theta
 = sum_j sigma_j^2/(s^2+sigma_j^2)
 >= ||N||_F^2/(s^2+||N||_op^2)
 >= rho/8
 >= 3`.                                                           (3.9)

Thus the partner threshold `theta>q=2` holds without selecting any individual singular value or determinant packet.

Take `r=3/2`, `p=3`. Then `beta=theta/4>=3/4`, so

`beta r >= 9/8`,
`beta r/(beta r-1) <= 9`.                                         (3.10)

Also `D>=1`, hence

`t0 <= pi e/(2s)`.                                                 (3.11)

Substitution of (3.10)--(3.11) into (2.1) gives

`||p_Q||_inf
 <= |a|^(-1/2) P_r (2pi)^(-1/2) C_r^(3/4)
    sqrt(9 pi e/s)
 = C0 / sqrt(|a|s)`,                                               (3.12)

with `C0` exactly as in (3.4). This proves the theorem. The conditioning/product provenance is entirely that of the partner theorem; the only new operation is a deterministic original-coordinate cut selected from (3.6).

## 4. Target-level branch closed: diagonal-heavy coordinate plus high Schur stable rank

### Corollary 4.1 — `QFORM-WINDOW39-DIAGHEAVY-STABLERANK-v1`

Assume now that `A` satisfies the full target spectral hypothesis. If the spectral-window branch (2.2) does not already apply, let `i` satisfy the heavy-coordinate conclusion (2.3). Suppose this coordinate is diagonal-dominant in the weak sense

`|a| >= ||b||_2`,                                                 (4.1)

and the scalar Schur complement `S` at `i` satisfies

`||S-diag(S)||_F^2 >= 24 ||S||_op^2`.                            (4.2)

Then

`boxed: ||p_Q||_inf < 340`.                                       (4.3)

### Proof

From (2.3) and (4.1),

`|a| >= 1/312`.                                                    (4.4)

Write

`A=L diag(a,S) L^T`,
`L=[[1,0],[b/a,I]]`.                                               (4.5)

Let `t=||b||_2/|a|<=1`. The nontrivial two-dimensional singular block of `L` gives

`||L||^2 <= (3+sqrt(5))/2`.                                       (4.6)

Since the third singular value of `A` is at least one under the target hypothesis and

`s_3(A) <= ||L||^2 s_3(diag(a,S))`,                               (4.7)

we obtain

`s_3(diag(a,S)) >= cS := 2/(3+sqrt(5))`.                          (4.8)

Only one singular value of `diag(a,S)` comes from the scalar block `a`. Therefore at least two singular values of `S` are at least `cS`; in particular

`s=||S||_op >= cS`.                                                (4.9)

Theorem 3.1 and (4.4),(4.9) yield

`||p_Q||_inf
 <= C0 sqrt(312/cS)
 =339.4097192265... <340`.                                        (4.10)

Thus this whole target branch is closed by an actual `O(|L|)` interval estimate, with arbitrary signs, arbitrary extra eigenvalues, and no local determinant selection.

## 5. Diffuse stress family and direct partner application

For a concrete diffuse target family, let `m>=16` be a power of two and let `H_m` be a normalized Walsh-Hadamard matrix. Let

`B_m=H_m diag(1,...,1,0,...,0) H_m^T`

with twelve ones. Then `B_m` is a rank-twelve orthogonal projection, `||B_m||_op=1`, `||B_m||_F^2=12`, and every physical entry has modulus at most `12/m`.

Set

`A_m = [1] direct_sum [[0,B_m],[B_m,0]]`.                          (5.1)

Its nonzero spectrum consists of the pivot eigenvalue `1`, twelve `+1` values, and twelve `-1` values, so it lies well inside the exact target while every physical cross coefficient tends to zero with `m`.

At the singleton pivot, `a=1` and

`S=[[0,B_m],[B_m,0]]`, `s=1`, `||S^o||_F^2=24`,                  (5.2)

so Theorem 3.1 gives the uniform bound `<11.876`.

Using the natural left/right cut is even stronger and directly applies the named partner inequality. There `N=B_m`, `gamma=1`, `q=2`,

`theta=6`, `D=2^12`.                                              (5.3)

Taking `r=3/2` in (2.1) gives the exact numerical bound

`boxed: ||p_Q||_inf <= 3.7554271113...`.                          (5.4)

Thus the partner theorem is quantitatively active on a genuinely diffuse family for which selecting one physical coefficient would lose a factor growing with `m`.

## 6. Decisive method counterexample: one heavy row plus its own square is not enough

A tempting next bridge from the heavy-coordinate dichotomy would be: use a nonzero pivot square together with one heavy off-diagonal coefficient, allowing arbitrary residual curvature on that same coefficient-side bank. That statement is false even in two variables.

Let `U,X` be independent `Uniform[-1/2,1/2]`, both with density cap one, and take

`T=U^2+X^2+2UX=(U+X)^2`.                                         (6.1)

The sum `Y=U+X` has triangular density

`g(y)=1-|y|`, `|y|<=1`.

Hence for `0<t<1`,

`p_T(t)=[g(sqrt(t))+g(-sqrt(t))]/(2sqrt(t))
       =t^(-1/2)-1`,                                              (6.2)

which is unbounded at zero.

So a single heavy bilinear row cannot simply be absorbed by the **same** square pivot in the presence of arbitrary same-bank quadratic structure. This is a method counterexample, not a counterexample to QFORM: the matrix in (6.1) has spectrum `{2,0}` and therefore lacks the required three large eigenvalues. Any heavy-off-diagonal routing must preserve a genuinely independent third smoother or use a grouped hyperbolic/ridge mechanism.

This correction is recorded as `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`.

## 7. Conditional end-to-end proof and sharpened first unpaid implication

The current proof skeleton is now:

1. If the `|lambda|>=1/39` spectral projection has maximum physical leverage at most `1/32`, the completed source theorem gives `||p_Q||_inf<35.27`.
2. Otherwise, a physical coordinate has `max(|a|,||b||_2)>=1/312`.
3. If such a coordinate is diagonal-dominant and its Schur complement has off-diagonal stable rank at least `24`, Corollary 4.1 gives `||p_Q||_inf<340`.
4. The remaining matrices have either a genuinely off-diagonal-heavy coordinate, or every usable diagonal-heavy pivot has Schur off-diagonal stable rank `<24`.

The first unpaid implication is therefore

> **`QFORM-HEAVYBANK-OR-LOWSTABLERANK-ROUTING-v1` (OPEN).** Starting from branch 4, aggregate original coordinates so that either (i) an independent grouped square/hyperbolic smoother pays the off-diagonal-heavy row, or (ii) low Schur off-diagonal stable rank is converted into a bounded-dimensional grouped-coordinate structure that can be sent to an already proved bilinear/square theorem, all before paying a reciprocal tiny local minor.

The two-variable counterexample in Section 6 is a mandatory control: the independent third smoothing resource cannot be silently merged into the same pivot bank. The singleton-plus-two-banks family and the newest Pluecker/pivot-support correction are also mandatory controls against fixed-local-packet routing.

No full-solution claim is made.

## 8. Exact computation used

Only elementary constant evaluation was used. The exact code and captured output are stored beside this report as `check_constants.py` and `check_constants.out`. They verify

`C0=11.875703258329660`,
`cS=0.381966011250105`,
`C0 sqrt(312/cS)=339.409719226565187`,
`partner Walsh-family bound=3.755427111260472`.

No numerical simulation or histogram is used as mathematical evidence.
