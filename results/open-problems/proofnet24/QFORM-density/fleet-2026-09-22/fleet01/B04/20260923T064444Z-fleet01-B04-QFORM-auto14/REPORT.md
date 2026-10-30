SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T06:44:44Z.
attacking: rank-two minor-support obstruction via weighted intersecting-family stability, entropy-efficient triangle repair, and the resulting double-heavy Schur currency.

# fleet01/B04 — weighted star/triangle stability for second exterior volume

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15` on fresh `math-research-brain/main`.  
Status: **NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full arbitrary-dimension three-large-eigenvalue conjecture is not proved here. The new square-splice branch proves essential boundedness; continuity is not claimed for it.

## 1. Source-valid analytic input

Let `I,J` be disjoint sets of original independent coordinates and, after conditioning all other original coordinates, write

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`,

where `F,G` contain arbitrary within-bank quadratic and affine terms. For any probability weight `w_{S,T}` on nonzero physical `2x2` minors of `M`, put

`G_2(w)=exp( sum w_{S,T} log det(M_{S,T})^2 + H(w) )`.

The completed designated-partner theorem fleet02/B04, `QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1`, states that if `1<=q<2` and every *row* inclusion marginal of `w` is at most `q/2`, then

`sup_s E |R-s|^(-1/2)
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] G_2(w)^(-1/8).`                 (1.1)

If one further untouched original coordinate `Z` supplies

`Q=a[Z+m]^2+R`, `a!=0`,

then

`||p_Q||_infinity
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] |a|^(-1/2) G_2(w)^(-1/8).`      (1.2)

The source is `yspennstate/math-open-problems@10a74bd7d75466fe46f4ff6ecf3362fba6cb2e5d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T052139Z-fleet02-B04-qform-auto11/REPORT.md`. The proof there retains arbitrary same-bank curvature and uses product-space Fourier/BL/Hausdorff--Young machinery, not law-uniform pointwise Fresnel decay.

The preceding fleet01/B04 run proved the disjointness entropy repair: if `mu` is the canonical squared-minor row-pair marginal, `Z_2=e_2(M^T M)`, and

`delta=P_{S,S' iid mu}(S cap S'=empty)`,

then, when `delta>0`, there is a `q=1` full-minor weight with

`G_2 >= Z_2 sqrt(delta)`.                                      (1.3)

The present run attacks the complementary `delta` small/zero regime.

## 2. New weighted intersecting-family stability lemma

### Lemma `QFORM-WEIGHTED-EDGE-STAR-TRIANGLE-STABILITY-v1`

Let `mu` be any probability measure on the two-element subsets of a finite set, and let `E,F` be iid with law `mu`. Put

`delta=P(E cap F=empty)`.

Then there is either a vertex `v` whose star has `mu`-mass at least

`1-delta-sqrt(2 delta)`,                                         (2.1)

or a three-vertex set `{a,b,c}` whose three internal edges have total `mu`-mass at least

`1-delta-sqrt(2 delta)`.                                         (2.2)

For `delta=0` this recovers the weighted form of the elementary fact that an intersecting family of two-sets is contained in a star or a triangle.

### Proof

For `delta>0`, define for an edge `e`

`d(e)=P(F cap e=empty)`.

Since `E_mu d(E)=delta`, choose `e={a,b}` with `d(e)=c<=delta`. Decompose the mass of edges intersecting `e` as

`z=mu({a,b})`,
`x_j=mu({a,j})`, `y_j=mu({b,j})` for `j notin {a,b}`,
`x=sum_j x_j`, `y=sum_j y_j`.

Thus

`z+x+y=1-c`.                                                     (2.3)

Relabel `a,b` so that `x>=y`. The ordered pairs consisting of `{a,j}` and `{b,k}` with `j!=k` are disjoint, hence

`delta >= 2( x y - sum_j x_j y_j )`.                            (2.4)

Put

`D=xy-sum_j x_jy_j <= delta/2=:d`.

If `y<=2 sqrt(d)=sqrt(2delta)`, then the star at `a` has mass

`z+x=1-c-y >=1-delta-sqrt(2delta)`,

and we are done.

Assume now `y>2sqrt(d)`. Choose `j_0` maximizing `x_j`. Since

`D=sum_j y_j(x-x_j) >= y(x-x_{j_0})`,

we have

`x-x_{j_0} <= d/y < sqrt(d)/2`.                                 (2.5)

Also

`x_{j_0} >= x-sqrt(d)/2 >= y-sqrt(d)/2 >3sqrt(d)/2`.             (2.6)

For every `j!=j_0`, `x-x_j>=x_{j_0}`; therefore

`D >= x_{j_0} sum_{j!=j_0}y_j
   =x_{j_0}(y-y_{j_0})`,

and so

`y-y_{j_0} <= d/x_{j_0} < 2sqrt(d)/3`.                           (2.7)

The triangle `{a,b,j_0}` consequently has mass

`z+x_{j_0}+y_{j_0}
 =1-c-(x-x_{j_0})-(y-y_{j_0})
 >=1-delta-(7/6)sqrt(d)
 >=1-delta-sqrt(2delta)`,                                       (2.8)

because `d=delta/2` and `7/6<=2`. The case `delta=0` follows by the same decomposition with `D=0`, or by taking a limit. QED.

## 3. Canonical second-volume interpretation

For each physical row pair `S`, define its aggregated squared-minor weight

`W_S=sum_{|T|=2} det(M_{S,T})^2`.

Cauchy--Binet gives

`Z_2=e_2(M^T M)=sum_{|S|=2}W_S`.                                (3.1)

Let

`mu(S)=W_S/Z_2`,
`alpha_i=P_mu(i in S)`.                                         (3.2)

The lemma therefore says that when the determinant-weighted disjointness `delta` is small, either one original physical row carries almost all of the second exterior volume, or three original physical rows carry almost all of it. In the triangle alternative,

`mu(ab)+mu(ac)+mu(bc)
 = e_2(M[{a,b,c},J]^T M[{a,b,c},J])/Z_2`.                       (3.3)

This is an aggregate statement; no reciprocal tiny local minor is selected.

## 4. New non-hub compiler with an explicit universal constant

### Theorem `QFORM-E2-NONHUB-COMPILER-v1`

In the setting of Section 1, assume `Z_2>0` and

`alpha_*:=max_i alpha_i <=3/4`.                                  (4.1)

Then

`sup_s E|R-s|^(-1/2) <= C_* Z_2^(-1/8)`,                         (4.2)

and, for the untouched scalar square `Q=a[Z+m]^2+R`,

`||p_Q||_infinity <= C_* |a|^(-1/2) Z_2^(-1/8)`,                 (4.3)

where

`delta_0=1/625`,
`eta_0=1/625+sqrt(2)/25`,
`r_0=1/4-eta_0`,                                                 (4.4)

and

`C_* = max{
  4sqrt(2e) 25^(1/8),
  6sqrt(2e)(3/4)^(1/4) [3r_0]^(-1/8)
}`

satisfies

`C_*=13.949982726975489... <13.95`.                              (4.5)

The density conclusion in (4.3) is essential boundedness; continuity is not asserted.

### Proof

If `delta>=delta_0`, use the previous disjointness entropy repair (1.3):

`G_2>=Z_2 sqrt(delta)>=Z_2/25`.

Apply the partner theorem with `q=1`:

`sup_s E|R-s|^(-1/2)
 <=4sqrt(2e)(Z_2/25)^(-1/8)
 =4sqrt(2e)25^(1/8)Z_2^(-1/8)`.                                 (4.6)

Now suppose `delta<delta_0`. The stability lemma gives a star or triangle of mass at least `1-eta_0`. The star alternative is impossible if its mass exceeds `3/4`; since

`1-eta_0>3/4`,

we may take a triangle `{a,b,c}` with total mass `tau>=1-eta_0`.

For each triangle edge, e.g. `{a,b}`,

`mu(ab)=tau-[mu(ac)+mu(bc)]
       >=tau-alpha_c
       >=1-eta_0-3/4
       =r_0`.                                                     (4.7)

Thus all three aggregated row-pair weights satisfy

`W_ab,W_ac,W_bc >=r_0 Z_2`.                                     (4.8)

Assign row-pair weight `1/3` to each of these three edges, and inside each chosen row pair retain the canonical conditional distribution over column pairs,

`w(T|S)=det(M_{S,T})^2/W_S`.                                    (4.9)

Every row marginal is exactly `2/3`, so the partner theorem applies with `q=4/3`. The chain rule for entropy gives exactly

`G_2(w)
 =3(W_ab W_ac W_bc)^(1/3)
 >=3r_0 Z_2`.                                                    (4.10)

Therefore

`sup_s E|R-s|^(-1/2)
 <=6sqrt(2e)(3/4)^(1/4)(3r_0 Z_2)^(-1/8)`,                      (4.11)

which is the second constant in (4.5). Combining (4.6) and (4.11) proves (4.2), and the partner square peel proves (4.3). QED.

### Symmetric orientation consequence

The two-bank polynomial is symmetric under swapping `I,J` and replacing `M` by `M^T`. Hence the same theorem holds using canonical *column* marginals. Consequently, if the certificate (4.3) is not available from either orientation, then there must exist a physical row `i` and physical column `j` with

`alpha_i>3/4`, `beta_j>3/4`.                                    (4.12)

This is substantially sharper than the preceding `small delta => pair/hub concentration` frontier: every non-hub and every triangle-type obstruction is now analytically paid.

## 5. Exact double-heavy Schur currency

Let `(S,T)` be a full physical `2x2` minor drawn from the canonical squared-minor law. Under (4.12), the union bound gives

`P(i in S and j in T)>1/2`.                                     (5.1)

Equivalently, if

`Z_{ij}=sum_{S contains i, T contains j} det(M_{S,T})^2`,

then

`Z_{ij}>Z_2/2`.                                                  (5.2)

Write the matrix around this physical row/column as

`M=[[a,r^T],[c,N]]`,                                             (5.3)

where `a=M_{ij}`.

If `a!=0`, define the scalar Schur complement matrix

`S_c=N-c r^T/a`.

For every remaining row `u` and column `v`,

`det [[a,r_v],[c_u,N_uv]] = a (S_c)_{uv}`.

Summing squares gives the exact identity

`boxed: Z_{ij}=a^2 ||S_c||_F^2`.                                (5.4)

Hence every unpaid double-heavy nonzero-edge packet satisfies

`boxed: a^2 ||S_c||_F^2 > Z_2/2`.                               (5.5)

If instead `a=0`, each such minor determinant equals `-c_u r_v`, so

`boxed: Z_{ij}=||c||_2^2 ||r||_2^2 > Z_2/2`.                    (5.6)

Thus the only survivor of the new non-hub compiler is no longer an amorphous near-coloop: it has an explicit original-coordinate double-heavy row/column with either Schur-Frobenius currency (5.5) or a zero-edge two-arm hub currency (5.6). No individual Schur entry is asserted large; the statement remains aggregate and dimension-free.

## 6. Genuinely rotated indefinite target example

Let

`R0=[[1,0],[0,sqrt(2)],[1/sqrt(2),1]]`

and let

`V=[[cos(pi/8),-sin(pi/8)],[sin(pi/8),cos(pi/8)]]`,
`M=R0 V`.

Every physical entry of `M` is nonzero. Right multiplication by `V` is part of the coefficient matrix, not a rotation of the random variables. The squared physical `2x2` minors are unchanged and equal

`W_12=2`, `W_13=1`, `W_23=1`,                                  (6.1)

so

`Z_2=4`,
`(alpha_1,alpha_2,alpha_3)=(3/4,3/4,1/2)`,
`delta=0`.                                                       (6.2)

For independent cap-one variables `Z,X_1,X_2,X_3,Y_1,Y_2`, set

`Q_*=Z^2+2X^T M Y`.                                              (6.3)

Since

`R0^T R0=[[3/2,1/sqrt(2)],[1/sqrt(2),3]]`,

its eigenvalues are

`(9+sqrt(17))/4`, `(9-sqrt(17))/4`,                              (6.4)

both strictly larger than one. Therefore the exact spectrum of the symmetric matrix of `Q_*` is

`{1,
  +/-sqrt((9+sqrt(17))/4),
  +/-sqrt((9-sqrt(17))/4),
  0}`,                                                           (6.5)

and the two positive singular values are approximately `1.8112913643` and `1.1041845831`. Thus this is a genuinely rotated indefinite target-valid form with five eigenvalues of modulus at least one.

Because `delta=0`, the new stability mechanism recognizes the three-row triangle exactly. Put weight `1/3` on each of its three physical minors. Then every row marginal is `2/3`, `q=4/3`, and

`G_2=3(2*1*1)^(1/3)=3*2^(1/3)`.                                (6.6)

The partner theorem gives the all-input-law estimate

`boxed:
 ||p_(Q_*)||_infinity
 <=6sqrt(2e)(3/4)^(1/4)[3*2^(1/3)]^(-1/8)
 =11.025434960874854... .`                                      (6.7)

For comparison, the unmodified canonical minor law first becomes admissible at `q=3/2`, giving `14.173330427618081...`. The triangle reweight therefore improves the direct canonical certificate on this same rotated indefinite matrix.

In fact the uniform triangle weight is the global optimum of the partner certificate on this three-edge support. For `4/3<=q<=3/2`, admissibility forces each edge weight at least `1-q/2`; the entropy maximizer is

`w_12=q-1`, `w_13=w_23=1-q/2`.                                  (6.8)

Writing `B(q)` for the partner bound, one obtains

`d/dq log B(q)
 =-1/(4q)+1/(2-q)-(1/8)log((2-q)/(q-1))`,                        (6.9)

whose derivative is strictly positive and which is already positive at `q=4/3`. For `q>=3/2`, the canonical determinant currency is constant and the prefactor increases. Thus `q=4/3` and (6.7) are optimal inside this entropy-weighted rank-two compiler.

## 7. What remains unpaid

The new first gap is

`QFORM-E2-DOUBLEHEAVY-HUB-SCHUR-ROUTING-v1`:

> Starting from the full three-large-eigenvalue hypothesis and a scalar-square/E2 packet not already paid by the non-hub compiler, consume the forced double-heavy currency
> `a^2||S_c||_F^2>Z_2/2` when `a!=0`, or `||c||^2||r||^2>Z_2/2` when `a=0`, through an existing grouped-coordinate/mixed-hub/ridge/pair-log mechanism without selecting a reciprocal tiny entry. The separate zero/near-zero *outer scalar square* branch also remains open.

This run does not show that the bare global spectral hypothesis automatically supplies an outer scalar square with target-scale `|a|^4 Z_2`, so it does not close QFORM. It does remove the triangle/non-hub ambiguity from the previous B04 small-disjointness frontier and replaces it by a concrete double-heavy Schur/hub certificate.

## 8. Corrections respected

No law-uniform pointwise quadratic-phase decay is used. No spectral rotation of the random inputs is used. No arbitrary-joint coarea bound, conditional projection-density positive moment, naive fiber supremum, or uniformly good local minor is assumed. The fixed `V` in Section 6 is part of the physical coefficient matrix. Numerical values only evaluate exact formulas; no histogram is used as evidence.
