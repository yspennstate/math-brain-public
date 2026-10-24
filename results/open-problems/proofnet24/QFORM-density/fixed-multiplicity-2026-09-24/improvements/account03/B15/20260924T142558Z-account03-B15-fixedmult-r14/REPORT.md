# account03/B15 r14 — terminal eight-direction collar collapses to one strong-cross physical pair

Run: `20260924T142558Z-account03-B15-fixedmult-r14`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Status and source inputs

The seventeen-direction baseline has already been independently reconstructed by this slot. The currently stronger nine-direction candidate and its same-constant `C_0` regularity upgrade were recorded in the preceding B15 run. This run changes mechanism and attacks the only open branch in the current multiplicity-eight reduction.

The new argument uses two completed source-pinned inputs.

1. account03/B04, `QFORM-EIGHT-DIRECTION-TERMINAL-OVERLAP1-COLLAR-v1`, source
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T124904Z-account03-B04-fixedmult-audit-r2/REPORT.md`, blob `851e0ae9c78a4d9a49f60a1cc5f0026b734579e6`.
   In its terminal normalized no-pivot branch it proves
   
   `V_2(A)>=kappa^2` and `Xi_2(A)>=(delta_*^2/2)V_2(A)`,
   
   where `eta=1/100`, `kappa=1/6400`, and
   
   `delta_* = 97/100-(297 sqrt(2)+3 sqrt(202))/4000
             =0.854335140191133771...`.

2. account03/B04, `QFORM-EXACT-ZERO-TWO-ANCHOR-AFFINE-RECEIVER-v1`, source
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T134840Z-account03-B04-QFORM-fixedmult-audit-r55/EXACT_ZERO_TWO_ANCHOR.md`, blob `702725a5ead6896d83d9b7fe5e764deae491dd64`.
   If a literal physical pair `H` has `A[H,H]=0` and `C=A[H,H^c]` has row rank two, then
   
   `||p_Q||_infinity <= e sqrt(2 pi) det(CC^T)^(-1/4)`
   
   for arbitrary outside curvature and arbitrary affine terms.

The designated partner account04/B15 same-constant `C_0` compiler is used in Section 5 below at the actual new interval inequality.

The unrestricted three-eigenvalue conjecture remains OPEN. Multiplicity eight also remains OPEN after this report; the gain is a dimension-free structural collapse of its terminal aggregate collar.

## 2. New structural lemma: aggregate two-sided collar forces one strong-cross pair

For every physical two-set `H subset [n]`, define

`G_H := sum_{U subset H^c, |U|=2} det(A[H,U])^2.`                 (2.1)

If

`C_H := A[H,H^c]`,

then Cauchy--Binet gives the exact identity

`G_H = det(C_H C_H^T)`.                                         (2.2)

Recall that the ordered disjoint second volume is

`V_2(A)=sum_{H,U: |H|=|U|=2, H cap U=empty} det(A[H,U])^2`.

Therefore

`sum_H G_H = V_2(A)`.                                           (2.3)

For fixed `H`, let

`Xi_H := sum_{S,T: S,H,T pairwise disjoint, |S|=|T|=2}
                 det(A[S,H])^2 det(A[H,T])^2.`                  (2.4)

Symmetry of `A` gives `det(A[S,H])^2=det(A[H,S])^2`. Dropping only the restriction `S cap T=empty` enlarges the nonnegative sum, hence

`Xi_H <= (sum_{S disjoint H} det(A[H,S])^2)^2 = G_H^2`.          (2.5)

Summing (2.5),

`Xi_2(A)=sum_H Xi_H <= sum_H G_H^2
                        <= (max_H G_H) sum_H G_H
                        = (max_H G_H) V_2(A).`                   (2.6)

As soon as `V_2(A)>0`, this proves the exact ratio inequality

`boxed: max_H det(C_H C_H^T) >= Xi_2(A)/V_2(A).`                 (2.7)

This is the key point: the aggregate collar does not force one *local minor* to be large, but it does force one entire two-row outside cross map to have a dimension-free Gram determinant. No cardinality factor appears.

## 3. Application to the multiplicity-eight terminal collar

Assume the normalized terminal branch of the completed B04 theorem:

- `A=A^T` has no `eta`-pivot;
- `s_8(A)>=1`;
- `V_3(A)<kappa^3`, so the theorem is in its collar alternative.

The cited theorem gives

`Xi_2(A) >= (delta_*^2/2)V_2(A)`                                (3.1)

with `V_2(A)>=kappa^2>0`. Combining (2.7) and (3.1) produces a literal physical pair `H` such that

`boxed: det(C_H C_H^T) >= delta_*^2/2
       =0.36494426588270207... .`                                (3.2)

Equivalently, the product of the two nonzero singular values of the two-row cross map satisfies

`s_1(C_H)s_2(C_H) >= delta_*/sqrt(2)
                  =0.6041061710351104... .`                     (3.3)

Because the ambient branch has no `eta`-pivot, the same pair also obeys

`|A_hh|<eta=0.01` for `h in H`,                                 (3.4)

`|det A[H,H]|<eta`,                                              (3.5)

and the manuscript's no-pivot entry estimate gives

`|A_{h_1h_2}|<sqrt(eta^2+eta)=sqrt(0.0101)`.

Thus

`boxed: ||A[H,H]||_op
       <= eta+sqrt(eta^2+eta)
       <0.110499.`                                               (3.6)

So the entire unresolved eight-direction collar can be rephrased without any aggregate reciprocal-minor payment:

> either the already-paid `V_3` branch holds, or there exists one literal physical pair whose self-curvature has operator norm below `0.111` while its outside cross map has two-dimensional Gram determinant at least `0.3649`.

This is strictly stronger operational information than merely retaining the scalar currencies `Omega_1` and `Xi_2`.

## 4. Exact-zero subchamber closes with a universal height below 8.77

Suppose the pair `H` furnished by (3.2) additionally lies in the exact-zero self-curvature chamber

`A[H,H]=0`.                                                     (4.1)

The completed exact-zero two-anchor receiver applies with `G=C_H C_H^T`. From (3.2),

`||p_Q||_infinity
 <= e sqrt(2 pi) det(G)^(-1/4)
 <= e sqrt(2 pi) (2/delta_*^2)^(1/4)`.

Numerically,

`boxed: ||p_Q||_infinity <= 8.766532.`                           (4.2)

This retains arbitrary outside quadratic curvature, arbitrary affine terms, arbitrary dimension and arbitrary independent cap-one rough coordinate laws.

It is useful to record the underlying affine-coefficient regularity as well. With

`L(Y)=C_H Y+b_H/2`,

its two-dimensional density satisfies

`||p_L||_infinity <= e/sqrt(det G)
                   <= e sqrt(2)/delta_*
                   =4.499676... .`                              (4.3)

Consequently the elementary inverse-radius splitting in the exact-zero proof gives

`E |L|^(-1) <= 2 sqrt(2 pi ||p_L||_infinity)
             <10.63434.`                                        (4.4)

Equations (4.3)--(4.4) are uniform in support location and require no moments. They are the quantitative regularity resource that survives in the exact-zero endpoint.

## 5. Designated partner applied to the actual new inequality

For the homogeneous specialization `b=c=0`, equation (4.2) pays the interval inequality

`P{X^T A X in I} <= M_0 |I|`,

where

`M_0 := e sqrt(2 pi) (2/delta_*^2)^(1/4) < 8.766532.`             (5.1)

The ambient `s_8(A)>=1` hypothesis implies `rank(A)>=8`. The completed account04/B15 Theorem 6.1 (`20260923T221909Z-account04-B15-ruled-trace-c0-r8`) says that for a fixed homogeneous rank-at-least-three target instance, any separately paid interval estimate `M|I|` upgrades to a canonical `C_0` representative with *the identical height*.

Applying that partner theorem to (5.1) gives the concrete same-constant conclusion

`boxed: p_{X^TAX} in C_0(R),
        ||p_{X^TAX}||_infinity < 8.766532`                       (5.2)

throughout the exact-zero terminal-pair subchamber.

For arbitrary affine `b,c`, the completed affine fixed-instance regularity theorem previously recorded by account03/B15 supplies `C_0` at fixed `A`; combining it with the interval domination (4.2) again leaves the same pointwise height. This affine regularity statement is logically separate from the designated partner's homogeneous theorem and is not attributed to it.

## 6. What remains open at multiplicity eight

The new reduction removes the dimension-dependent local-minor selection issue from the terminal collar. The remaining endpoint is now sharply localized:

- a literal physical pair `H` has strong two-dimensional outside cross Gram (3.2);
- its self block `B=A[H,H]` is uniformly small in operator norm (3.6) and has `|det B|<0.01`;
- if `B=0`, the theorem is paid with height `<8.77`;
- if `B` is nonzero, completing the square in the pair creates the moving critical value governed by the Schur complement. A naive perturbation from `B=0` is not legitimate for arbitrary remotely translated cap-one laws, and the already-recorded B15 perturbation barrier forbids assuming such uniform continuity.

Thus the next proof obligation is no longer an aggregate `Xi_2` receiver. It is the more concrete **strong-cross / weak-self two-anchor receiver**:

> uniformly bound the output density when one physical two-coordinate block satisfies `||B||_op<0.111`, its outside cross map `C` satisfies `det(CC^T)>=0.3649`, and the full matrix retains the six Schur spectral directions forced by `s_8(A)>=1` whenever `B` is invertible.

The correct route must use those ingredients jointly; paying `1/sqrt(|det B|)` first loses the endpoint as `det B ->0`.

## 7. Exact scope

This report proves the structural certificate (2.7), its terminal numerical specialization (3.2)--(3.6), and the exact-zero height/regularity closure (4.2), (5.2). It does **not** prove multiplicity eight in the nonzero weak-self chamber. The nine-direction bounded-density candidate and the unrestricted three-eigenvalue conjecture remain separate; the full three-eigenvalue target is still OPEN.
