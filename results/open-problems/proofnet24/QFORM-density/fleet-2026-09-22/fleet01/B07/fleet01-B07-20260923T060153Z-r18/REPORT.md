SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T06:01:53Z.
attacking: coordinate-minor selection via determinant-weighted Schur aggregation; seek a dimension-free receiver for the current rank-two-tube residual without selecting one tiny pivot.

# fleet01/B07 r18 — anchored volume ratios control the global rank tail

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / aggregate-before-inversion  
Status: `ESSENTIAL_STEP_APPLIED / NEW ANCHORED RANK-TAIL RATIO / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. The new result is a deterministic identity/inequality which turns *anchored determinant mass* into a global low-rank conclusion without reciprocating one coordinate minor. It applies directly to the physical bi-anchor survivor produced in fleet01/B07 r17 and has an exact-rank-three endpoint that is paid by the designated partner fleet02/B07 cross-fiber theorem.

## 1. Sources and live scope


The current B07 input is the preceding fleet01/B07 r17 bundle

`yspennstate/math-open-problems@abbd51dd7e691844aa6bfa3d34410af4b23f1cda`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T053559Z-r17/REPORT.md`.

On its unpaid physical bi-coloop branch, for a physical cross block `M`,

`Z=E3(M)`, `F=||M||_F`,

there are actual original-coordinate anchors `(i,j)` with

`H3^(i,j)>Z/2`,                                                   (1.1)

and the designated partner's live lower bound gives

`Z >= (theta^2/6) F^6`.                                          (1.2)

If the D5 exit also fails, the current fifth-volume resource is

`E5(M) < [theta^6/(120*3072^2)] F^10`.                            (1.3)

The concrete collar is `theta=1/16`, with the inherited scale relation `F>kappa/Lambda`, `kappa=1/(256 sqrt(3))`, `Lambda=1` after the preceding large-star exit fails.

The **designated partner fleet02/B07 theorem actually applied below** is `QFORM-CROSS-FIBER-PLANCHEREL-v1`, canonical source

`yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.

For a physical cross block of exact rank `r>=3`, with nonzero singular-value product `D`, it gives a continuous density for the full ambient quadratic form and

`||p_Q||_infinity <= e r/(r-2) D^(-1/r)`.                        (1.4)

All self blocks, outside couplings, affine terms, signs and additional ambient variables are retained.

## 2. Anchored determinant volumes

Fix a physical row `i` and physical column `j`. For each integer `q>=1`, define

`H_q^(i,j)(M)
 = sum_{|R|=|C|=q, i in R, j in C} det(M[R,C])^2`.               (2.1)

Let the squared singular values of `M` be

`lambda_1>=lambda_2>=...>=0`,

and define the global squared Frobenius rank-`q` tail

`T_q(M)=sum_{m>q} lambda_m
       =dist_F(M,{rank<=q})^2`.                                  (2.2)

The important point is that `H_q^(i,j)` is a *sum* of squared physical minors. No individual determinant lower bound is assumed.

## 3. Main theorem: anchored volume-ranktail ratio

### Theorem 3.1 — `QFORM-ANCHORED-VOLUME-RANKTAIL-RATIO-v1`

For every real matrix `M`, every fixed physical anchors `(i,j)`, and every `q>=1`,

`boxed: T_q(M) H_q^(i,j)(M) <= q^2 H_(q+1)^(i,j)(M).`            (3.1)

In particular, whenever `H_q^(i,j)>0`,

`boxed: T_q(M) <= q^2 H_(q+1)^(i,j)/H_q^(i,j).`                 (3.2)

There is also a determinant-weighted Schur-mixture form. Give each invertible anchored `q x q` pivot `B=M[R,C]` weight

`nu(R,C)=det(B)^2/H_q^(i,j)`.                                   (3.3)

Let `S_(R,C)` be its exact rectangular Schur complement in the full matrix. Then

`E_nu ||S_(R,C)||_F^2 <= q^2 H_(q+1)^(i,j)/H_q^(i,j)`.          (3.4)

Consequently at least half of the *determinant mass*, not merely half of the pivot count, lies on pivots satisfying

`||S_(R,C)||_F^2 <= 2q^2 H_(q+1)^(i,j)/H_q^(i,j)`.              (3.5)

Thus a small anchored next-order volume produces a whole determinant-weighted family of low-residual pivots before any reciprocal inversion.

### Proof

Take an anchored invertible `q x q` pivot `B=M[R,C]`. Permute physical rows and columns only for notation, and write

`M = [[B,E],[F,G]]`.                                             (3.6)

Its exact rectangular Schur complement is

`S=G-F B^(-1) E`.                                                (3.7)

Define

`M_B = [[B,E],[F,F B^(-1) E]]
     = [[I],[F B^(-1)]] [B,E]`.                                 (3.8)

Hence `rank(M_B)<=q`, while `M-M_B` vanishes outside the lower-right block and equals `S` there. Therefore

`T_q(M)=dist_F(M,{rank<=q})^2 <= ||S||_F^2`.                    (3.9)

For every row `r` outside `R` and column `c` outside `C`, the one-row/one-column block determinant identity gives

`det M[R union {r}, C union {c}]
 = det(B) S_(r,c)`.                                              (3.10)

Squaring and summing yields the exact extension identity

`det(B)^2 ||S||_F^2
 = sum_{r notin R, c notin C}
   det M[R union {r},C union {c}]^2`.                            (3.11)

Multiply (3.9) by `det(B)^2` and sum over all anchored invertible `q x q` pivots. Zero pivots carry zero weight, so the left side is exactly

`T_q(M) H_q^(i,j)`.                                              (3.12)

On the right, fix an anchored `(q+1) x (q+1)` minor. It can arise only by deleting one of its `q` non-anchor rows and one of its `q` non-anchor columns, hence from at most `q^2` anchored `q x q` pivots. Therefore the total right side of (3.11), after summing pivots, is at most

`q^2 H_(q+1)^(i,j)`.                                            (3.13)

This proves (3.1)-(3.2). Dividing (3.11) by `H_q^(i,j)` before summing proves (3.4), and Markov's inequality gives (3.5). QED.

No spectral-coordinate random variables appear in the proof; all determinant weights remain in original physical coordinates.

## 4. Exact endpoint: anchored fourth volume zero forces global rank three

Take `q=3`. If

`H_3^(i,j)>0`, `H_4^(i,j)=0`,                                   (4.1)

then (3.2) gives `T_3(M)=0`. Thus `rank(M)<=3`; the positive anchored third minor gives `rank(M)>=3`, so

`rank(M)=3` exactly.                                             (4.2)

Now apply the designated partner fleet02/B07 theorem (1.4) with `r=3`. Since in exact rank three

`D^2=E3(M)=Z`,                                                   (4.3)

we obtain the full ambient continuous-density estimate

`boxed: ||p_Q||_infinity <= 3e Z^(-1/6).`                       (4.4)

This is an actual partner application to an inequality, not merely a citation. On the live branch (1.2),

`||p_Q||_infinity
 <=3e (6/theta^2)^(1/6) F^(-1)`.                               (4.5)

If the inherited `F>kappa/Lambda` scale relation is also in force,

`||p_Q||_infinity
 <3e (6/theta^2)^(1/6) Lambda/kappa`.                           (4.6)

At `theta=1/16`, `kappa=1/(256sqrt(3))`, `Lambda=1`, the numerical cap in (4.6) is `<12282.352`. The constant is not optimized; the structural endpoint is what matters. Continuity is proved on this endpoint by the partner theorem.

More generally, `H_q>0` and `H_(q+1)=0` force `rank(M)=q`; for `q>=3` the same partner theorem pays the exact-rank endpoint.

## 5. Quantitative live application: same-anchor rank-three-or-four tube

The r17 bi-anchor branch gives, from (1.1)-(1.2),

`H3^(i,j) > (theta^2/12) F^6`.                                  (5.1)

Also

`H5^(i,j) <= E5(M)
 < [theta^6/(120*3072^2)] F^10`.                                (5.2)

Set

`eta = theta^2/(2304 sqrt(10))`.                                (5.3)

There are two cases.

### Case A: small anchored fourth volume

If

`H4^(i,j) <= eta F^2 H3^(i,j)`,                                 (5.4)

then Theorem 3.1 with `q=3` gives

`T3(M) <=9 eta F^2
       = [theta^2/(256 sqrt(10))] F^2`.                          (5.5)

### Case B: large anchored fourth volume

If (5.4) fails, then Theorem 3.1 with `q=4`, (5.1), and (5.2) give

`T4(M)
 <=16 H5/H4
 <16 [theta^6/(120*3072^2)]F^10
     / [eta F^2 (theta^2/12)F^6]
 = [theta^2/(256 sqrt(10))] F^2`.                               (5.6)

Thus, on every surviving r17 bi-anchor + D5-small branch,

`boxed:
 either dist_F(M,{rank<=3}) < theta/(16*10^(1/4)) F,
 or     dist_F(M,{rank<=4}) < theta/(16*10^(1/4)) F.
}`                                                               (5.7)

At `theta=1/16`, the relative Frobenius tube radius is

`1/(256*10^(1/4)) = 0.0021966458015...`.                        (5.8)

Relative to the partner core scale `a=theta F/sqrt(12)`, this is

`sqrt(12)/(16*10^(1/4)) = 0.1217504683...` times `a`.            (5.9)

This does **not** claim a stronger numerical rank-four tube than every existing global D5 estimate. Its new content is that the *same actual physical bi-anchor* `(i,j)` and the observable anchored ratio `H4/H3` decide whether the entire cross block is close to rank three or rank four, and (3.4)-(3.5) preserve a determinant-weighted family of physical pivots through the reduction.

## 6. Why this is useful for the assignment

The old obstruction was that a constant aggregate determinant bank may be spread over arbitrarily many individually tiny physical minors. Theorem 3.1 never chooses a minor with a reciprocal cost. Instead it attaches to each pivot its natural weight `det(B)^2`, proves an exact Schur-extension identity, and averages the residual before inversion. In the small-ratio case at least half of the *actual determinant currency* sits on small-residual Schur pivots. In the zero-ratio endpoint the whole matrix is forced to exact rank `q`, so the partner aggregate cross-fiber theorem becomes available without any minor selection at all.

The first unpaid implication is now:

`QFORM-SAME-ANCHOR-RANK34-TUBE-RECEIVER-v1` — use the determinant-weighted Schur family (3.5), together with the same physical bi-anchor and the existing rank-two affine / translated-kernel receivers, to absorb a **small but nonzero** rank-three or rank-four tail while retaining arbitrary same-bank quadratic curvature and all original-coordinate product provenance. The exact-rank-three endpoint is paid by (4.4); the quantitative nonzero-tail receiver is still open.

No global continuity claim is made. The full QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`.

## 7. Checks

A seeded finite regression checked (3.1) on 226 nontrivial anchored instances from integer matrices of sizes `4x4`, `5x6`, `6x5`, and `7x7`, for all tested `q<=3`; no violation occurred. The largest finite ratio `T_q H_q/(q^2 H_(q+1))` observed was `0.8199823698599092`. This is only a regression check; the proof is Section 3.

The live constants were independently evaluated as

`eta = 5.361391974840595e-7`,
`theta^2/(256 sqrt(10)) = 4.825252777356535e-6`,
`theta/(16*10^(1/4)) = 0.002196645801524801`,
`tube/a = 0.12175046830316208`,
`partner exact-rank-3 cap after F>kappa = 12282.351780476876`.
