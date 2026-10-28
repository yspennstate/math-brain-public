SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T05:09:42Z.
attacking: sharpen the selected-three diffuse curvature-transfer ladder by combining finite-dimensional floating half-paving with a sharper normalization identity, then feed the resulting cross scales into the completed account02/B08 volume-tail compilers.

# account01/B08 — floating sharp curvature transfer and a 1/3-leverage diffuse router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T050942Z-account01-B08-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

The unrestricted QFORM conjecture remains OPEN. The theorem below is a selected-three-eigenvector diffuse branch; it does not make selected-eigenvector diffuseness basis-invariant inside repeated eigenspaces, and it does not claim that every target matrix satisfies the diffuse hypothesis. Continuity is asserted only on the explicitly paid Fourier branches.


## 1. Sources used at equations

### 1.1 B08 finite-dimensional floating half-paving

Canonical source: `yspennstate/math-open-problems@c37badc7438c808fa283f574d22a8cb4db87216e`, B08 run `20260922T144029Z-account01-B08-qform-r13`.

If `R` is an `n x m` orthonormal-column frame and

`mu=max_i ||R_{i,*}||_2^2`,

then a physical subset `I` exists for which, with `J=I^c`,

`R_I^T R_I >= alpha I_m`, `R_J^T R_J >= alpha I_m`,

where

`alpha=1/2-kappa_m mu`, `kappa_m=sqrt(m(m+1)/8)`.

For `m=3`,

`kappa_3=sqrt(3/2)=sqrt(6)/2`.

For completeness, the floating proof is finite-dimensional: start from coefficients all equal to `1/2`, float inside the affine constraint `sum x_i r_i r_i^T=(1/2)I_m` until at most `d=m(m+1)/2` atoms remain fractional, then independently round those atoms with their own means. The rounding error `E` has

`E ||E||_F^2 <= (1/4) d mu^2`,

so some rounding has `||E||op<=||E||F<=mu sqrt(d)/2=kappa_m mu`.

### 1.2 Curvature-transfer predecessor

The conceptual predecessor is account03/B08 `QFORM-DIFFUSE-CURVATURE-TRANSFER-LADDER-v1`, canonical source

`yspennstate/math-open-problems@1bf6f41d81ffddcc6e8ff93b4df165d0ce5bbd05`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T231729Z-account03-B08-qform-diffuse-r24/REPORT.md`.

It used a random-sign cut and recovered cross singular values with factor `alpha`. Section 3 below observes that the same exact eigen-equation factors as `K T` with `||T||<=rho^{-1}`, improving that recovery factor from `alpha` to `rho=sqrt(alpha/(1-alpha))`. Since `rho>alpha` for `0<alpha<1/2`, this is a genuine strengthening, not only a change of constants.

### 1.3 Designated partner account02/B08 — actually applied

Latest completed designated partner source read for this run:

`yspennstate/math-open-problems@31212dc0982ef58cdae6fc12c9354599a663fad6`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T020620Z-account02-B08-QFORM-auto11/REPORT.md`,

claim `QFORM-DIFFUSE-HYBRID-VOLUME-TAIL-LADDER-v1`.

Its generic two-cross and one-cross compilers are independent of the old `1/48` frame threshold. They start from an ACTUAL physical cross singular-value scale `b` and, using completed `D'`/`D_5` Fourier theorems, give continuous-density exits or fixed low-rank Frobenius tubes / two-sided physical three-volume anchors. Section 5 feeds the new larger `b` into those exact inequalities.

### 1.4 Optional latest anchored receiver

For the `k=0` anchored survivor I also use account03/B08 `QFORM-ANCHORED-THREEVOLUME-SELF-MATCHED-MIX-v1`, canonical source

`yspennstate/math-open-problems@e76d2e984f81a058590bb143ff21e387fbbeab09`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T042303Z-account03-B08-qform-diffuse-r27/REPORT.md`.

If an anchored third-volume packet has mass `Z`, anchor-row norm `R_i`, and all residual row inclusion marginals at most `1/2`, it gives

`||p_Q||inf <=10 sqrt(e) (2Z/R_i)^(-1/5)`

with a continuous `C0` density.

## 2. Setup

Let `A` be real symmetric. Let `R` be an `n x 3` matrix whose columns are three orthonormal genuine eigenvectors of `A`:

`A R=R Lambda`,

where `Lambda=diag(lambda_1,lambda_2,lambda_3)` and

`min_j |lambda_j|>=L>0`.

No assumption is made on the remaining spectrum of `A`.

For an ORIGINAL-coordinate cut `I|J`, write

`G=R_I^T R_I`, `H=R_J^T R_J=I_3-G`,

and suppose

`alpha I_3 <=G,H<=(1-alpha)I_3`, `0<alpha<1/2`.

Put

`rho=sqrt(alpha/(1-alpha))`,

`U=R_I G^(-1/2)`, `V=R_J H^(-1/2)`,

so `U,V` have orthonormal columns, and let

`B=A[I,J]`

be the ACTUAL physical cross block.

## 3. Main theorem — the sharp transfer factor is rho, not alpha

### Theorem 3.1 — `QFORM-SHARP-BALANCED-CURVATURE-TRANSFER-v1`

For each `m in {1,2,3}` and each `0<c<L rho`, at least one of the following holds:

1. the physical child `A[I,I]` has at least `m` eigenvalues of modulus at least `c`; or
2. the actual physical cross block has at least `4-m` singular values strictly larger than

`boxed: rho (L rho-c).`

The identical assertion holds with `I,J` interchanged.

#### Proof

Restrict the genuine eigen-equation to `I`:

`A[I,I] R_I+B R_J=R_I Lambda`.

Using `R_I=U G^(1/2)` and `R_J=V H^(1/2)`, multiply on the left by `U^T` and on the right by `G^(-1/2)`. This gives the exact identity

`C+K T=S`,

where

`C=U^T A[I,I] U`,

`K=U^T B V`,

`T=H^(1/2) G^(-1/2)`,

`S=G^(1/2) Lambda G^(-1/2)`.

Because the eigenvalues of `G` lie in `[alpha,1-alpha]`,

`s_3(S)>=L sqrt(alpha/(1-alpha))=L rho`,

and, since `H=I-G` commutes with `G`,

`||T||<=sqrt((1-alpha)/alpha)=rho^(-1)`.

Suppose the principal alternative fails. Then `s_m(C)<c`. Weyl's singular-value sum inequality with indices `m` and `4-m` gives

`L rho <=s_3(S)<=s_m(C)+s_(4-m)(KT)`,

hence

`s_(4-m)(KT)>L rho-c`.

But

`s_(4-m)(KT)<=||T|| s_(4-m)(K)<=rho^(-1) s_(4-m)(K)`,

so

`s_(4-m)(K)>rho(L rho-c)`.

Finally `K=U^T B V` is a two-sided orthogonal compression, so

`s_j(K)<=s_j(B)`

for each `j`, proving the cross alternative.

If `s_m(C)>=c`, then `C` is a symmetric compression of `A[I,I]`. Cauchy interlacing/min-max applied separately to the positive and negative Ritz values shows that `A[I,I]` has at least the same total number of eigenvalues outside `(-c,c)`. QED.

### Why this improves the predecessor

The predecessor bounded the leakage through

`G^(-1/2) R_I^T B R_J G^(-1/2)`

by undoing both `G^(1/2)` factors and therefore recovered only `alpha(L rho-c)`. The factorization above keeps the natural `H^(1/2)G^(-1/2)` transfer matrix together and uses its norm `rho^(-1)`, giving `rho(L rho-c)`. The improvement factor is

`rho/alpha=1/sqrt(alpha(1-alpha))>2`.

No probabilistic assumption enters this sharpening.

## 4. Floating + sharp transfer: selected-three leverage up to any mu<1/sqrt(6)

### Theorem 4.1 — `QFORM-FLOATING-SHARP-CURVATURE-LADDER-v1`

Let

`mu=max_i ||R_{i,*}||_2^2 <1/sqrt(6)`.

Set

`alpha=1/2-sqrt(3/2) mu`,

`rho=sqrt(alpha/(1-alpha))`.

Then there is an ORIGINAL-coordinate cut `I|J` for which Theorem 3.1 holds simultaneously on both sides. In particular, choosing the half-budget scale

`c_0=(L rho)/2`,

`b_0=(L rho^2)/2 = L alpha/[2(1-alpha)]`,

we have, on either child, the exhaustive one-step ledger:

- fewer than one eigenvalue of modulus `>=c_0` forces `s_3(B)>b_0`;
- fewer than two forces `s_2(B)>b_0`;
- fewer than three forces `s_1(B)>b_0`;
- otherwise that child retains three actual eigenvalues of modulus `>=c_0`.

This theorem keeps the entire arbitrary complementary spectrum of `A` inside the actual blocks. It neither truncates nor perturbs away any spectral tail.

#### Proof

Apply the finite-dimensional floating half-paving with `m=3`; its hypothesis gives `alpha>0`. Since `G+H=I`, the two lower bounds also give the upper bounds required in Theorem 3.1. Insert `c=c_0` there. Since `L rho-c_0=L rho/2`, the sharp cross threshold is

`rho(L rho/2)=L rho^2/2=b_0`. QED.

## 5. Clean `mu<=1/3` router and actual use of account02/B08

Take the much larger diffuse threshold

`mu<=1/3`.

Then the floating cut has the exact constants

`alpha=(3-sqrt(6))/6 =0.091751709536137...`,

`rho^2=alpha/(1-alpha)=5-2sqrt(6)=0.101020514433644...`,

`rho=0.317837245195782...`,

and therefore

`boxed: c_0=0.158918622597891 L,`

`boxed: b_0=0.0505102572168219 L.`

Let `k` be the number, capped at three, of eigenvalues of `A[I,I]` whose modulus is at least `c_0`.

### 5.1 k=0: three actual cross directions

Theorem 4.1 gives

`s_3(B)>b_0`.

Apply the `k=0` three-volume branch of the completed designated partner account02/B08 result. If the completed `D'` marginal gate holds in one orientation, then the FULL ambient quadratic form has a continuous `C0` density and

`||p_Q||inf <= [24 sqrt(e)/sqrt(5)] b_0^(-1)
             <350.344/L.`

If that gate fails on both sides, the same partner theorem gives physical anchors `i,j` for which the double-incident third-volume packet satisfies

`W_ij^(3)> e_3(B^T B)/4>b_0^6/4`

and numerically

`boxed: W_ij^(3)>4.15161e-9 L^6.`

This is an actual inequality obtained by inserting the new transfer scale into the designated partner theorem.

The newest self-matched anchored receiver further pays part of this survivor. If the anchor-row norm is at most `L` and the residual anchored-third-volume row marginals are all at most `1/2`, then

`||p_Q||inf
 <10 sqrt(e) (b_0^6/(2L))^(-1/5)
 <682/L`,

again with a continuous `C0` density. Failure of this secondary payment forces either an anchor star norm `>L` or a residual nested three-anchor packet exceeding

`b_0^6/8>2.07580e-9 L^6`;

the transposed statement holds on the column side.

### 5.2 k=1: two actual cross directions

Theorem 4.1 gives `s_2(B)>b_0`. Apply account02/B08 Theorem 2.1 with `theta=1/8`. At least one of the following holds:

- `dist_F(B,{rank<=2})<b_0/8=0.00631378215... L`;
- the full form has a continuous density with `||p_Q||inf<962.731/L` by `D_5`;
- the full form has a continuous density with `||p_Q||inf<1728.043/L` by `D'`;
- a two-sided physical three-volume bicolop occurs. From the proof of the partner theorem its mass is at least

  `b_0^6/57600 >2.8830e-13 L^6`.

Thus outside a fixed rank-two tube or a quantitative physical anchor, this branch is fully paid with the clean bound

`boxed: ||p_Q||inf<1729/L`

and a continuous density.

### 5.3 k=2: one actual cross direction

Theorem 4.1 gives `s_1(B)>b_0`. Apply the account02/B08 one-cross compiler with `theta=1/8`. Either

- `dist_F(B,{rank<=1})<b_0/8=0.00631378215... L`; or
- a continuous `D_5` branch has `||p_Q||inf<1679/L`; or
- `s_2(B)>b_0/120=0.000420918810... L`.

In the last case apply the same designated partner's two-cross compiler at its `theta_2=1` scale. Then either

- `dist_F(B,{rank<=2})<b_0/120`;
- a continuous density bound `||p_Q||inf<33177/L` holds by `D_5`;
- a continuous density bound `||p_Q||inf<103683/L` holds by `D'`; or
- a two-sided physical three-volume bicolop occurs.

So the entire `k=2` state is reduced to two explicit low-rank tubes, a physical bicolop, or a paid continuous branch. No small tube is deleted probabilistically.

### 5.4 k=3

The child retains three ACTUAL eigenvalues of modulus at least

`0.1589186225... L`.

This is the retained-principal branch of the multiscale ledger. It is not declared paid here: a dimension-free closure must either terminate it in an already-paid localized child or charge later cross curvature without multiplying a fixed scale loss indefinitely.

## 6. Comparison at the old 1/48 threshold

At the old selected-frame threshold `mu<=1/48`, the floating cut gives

`alpha=0.474484481846...`, `rho=0.950207018966...`,

hence the new sharp cross scale is

`b_0=0.451446689446 L`.

The older random-sign/alpha-factor ledger used `0.145236875483 L`. Thus on the same `1/48` diffuse class the new transfer scale is more than three times larger, while Theorem 4.1 simultaneously extends the fixed-scale ledger all the way to every `mu<1/sqrt(6)`.

## 7. What is and is not solved

Proved this run:

1. `QFORM-SHARP-BALANCED-CURVATURE-TRANSFER-v1`: exact recovery factor `rho`, improving the prior `alpha` factor.
2. `QFORM-FLOATING-SHARP-CURVATURE-LADDER-v1`: finite-dimensional floating upgrades the selected-three diffuse range from the old `1/48` working scale to every `mu<1/sqrt(6)`.
3. At the clean threshold `mu<=1/3`, the retained-child scale is `0.1589186 L` and the escaped-cross scale is `0.0505103 L`.
4. The designated account02/B08 volume-tail compilers were applied to this new cross scale, yielding actual continuous-density bounds `<351/L`, `<1729/L`, or `<103683/L` on the corresponding paid subbranches, with explicit fixed low-rank tubes / bicolops otherwise.

Not solved:

- the full QFORM conjecture;
- basis-invariant reduction from arbitrary repeated high eigenspaces to the selected-frame hypothesis;
- the `k=3` multiscale retained-principal closure;
- the two explicit low-rank-tube and physical-bicolop survivors in the `k=1,2` branches;
- global continuity outside branches whose cited Fourier theorems give an `L^1` characteristic-function envelope.

The first unpaid B08 implication is now `QFORM-FLOATING-MULTISCALE-LEDGER-CLOSURE-v1`: iterate the sharper floating ledger while charging every `k<3` escape exactly once to the completed account02/B08 cross compilers, and show that the `k=3` branch cannot retain curvature through arbitrarily many scales without either reaching a bounded-cardinality physical child or generating a previously paid cross/grouped certificate. The bookkeeping must preserve original-coordinate product structure and may not treat selected-frame diffuseness as basis-invariant.

## 8. Arithmetic / audit

`CHECKS.py` and `CHECKS_OUTPUT.txt` beside this report verify the exact `mu=1/3` identities, all displayed numerical constants, the partner-compiler substitutions, and the strict improvement of the sharp `rho` factor over the old `alpha` factor. Numerical checks are only arithmetic audits; the proof is the exact matrix argument in Sections 3--4.
