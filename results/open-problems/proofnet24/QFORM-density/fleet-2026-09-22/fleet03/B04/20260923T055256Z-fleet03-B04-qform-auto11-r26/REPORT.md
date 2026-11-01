SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T05:52:56Z.
attacking: three-sample minor-overlap entropy conditioning for product-Fourier half-Riesz smoothing, with an exact physical-star obstruction when the overlap event has zero probability.

# fleet03/B04 r26 — minor-overlap entropy gate and exact star obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15`  
Assignment: Product Fourier rearrangement  
Execution status: `WITHOUT_VERIFIED_BRAIN`  
Full conjecture: `OPEN`  
New branch regularity: absolute continuity + essential boundedness; continuity is **not** claimed for arbitrary merely measurable input densities.

## 1. Target and first unpaid implication

The target remains: for every finite `n`, independent real ORIGINAL coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal finite bound on the density of `X^T A X`, or give a valid counterexample.

The preceding B04 work left a low-cross-rank/high-leverage structural debt. A very fresh same-path peer result, fleet02/B04's `QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1`, shows that a physical cross packet can be paid once one has *some* probability weight on its nonzero physical `2x2` minors with bounded row marginals. Its first unpaid implication was exactly a fractional-matching-or-hub alternative.

This run closes that qualitative alternative and gives a quantitative product-space certificate. The mechanism is to sample several physical minors from the canonical squared-minor law, condition on their having no common physical row, and use the conditional first marginal as the entropy-efficient weight. No local minor is selected and no reciprocal of a tiny matrix entry is taken.

## 2. Source-pinned analytic input actually applied

Fresh completed peer theorem applied at the final inequality:

- `yspennstate/math-open-problems@04297a630381fcfcf429b4c5ec560886bebacb39`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T052139Z-fleet02-B04-qform-auto11/REPORT.md`
- theorem `QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1`.

Its exact scope is as follows. For disjoint ORIGINAL-coordinate banks `I,J`, after conditioning any other original coordinates, write

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`,

where `F,G` may contain arbitrary within-bank quadratic and affine terms. If `w` is any probability law on nonzero physical `2x2` minors `M_{S,T}`, with row inclusion marginals `alpha_i`, and

`G_2(w)=exp( sum w_{S,T} log det(M_{S,T})^2 + H(w) )`,

then for `1<=q<2`, whenever `max_i alpha_i<=q/2`,

`sup_s E|R-s|^(-1/2)
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] G_2(w)^(-1/8).`                 (2.1)

If a further untouched original coordinate `Z`, independent of the residual variables and with density cap one, appears as

`Q=a[Z+m]^2+R`,

with arbitrary measurable residual-dependent shift `m`, then

`||p_Q||_infinity
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] |a|^(-1/2) G_2(w)^(-1/8).`   (2.2)

The designated partner is `fleet04/B04`. A fresh lookup before this run found only current QFORM login/start evidence and no completed current-QFORM canonical report or shared handoff. I therefore do not fabricate a designated-partner theorem; the completed peer theorem above is the result actually consumed at equations.

## 3. Canonical two-volume law

Let `M` be any real physical cross block between two disjoint original-coordinate banks, and assume

`Z_2 := sum_{|S|=|T|=2} det(M_{S,T})^2 >0`.                       (3.1)

For every nonzero physical `2x2` minor `z=(S,T)` put

`d_z=det(M_{S,T})^2`,
`nu_z=d_z/Z_2`.                                                    (3.2)

Thus `nu` is the canonical squared-minor probability law. If `z_1,...,z_k` are iid with law `nu`, write `S_l` for the physical row pair of `z_l` and define

`delta_k^r = P( S_1 cap ... cap S_k = emptyset )`.               (3.3)

There is an analogous column quantity `delta_k^c` obtained from the `T_l`.

The key point is that the empty-common-intersection event is symmetric in the `k` iid samples. Conditioning on it creates exactly the marginal cap needed by the product-Fourier theorem.

## 4. General k-sample overlap-entropy theorem

### Theorem 4.1 — `QFORM-KSAMPLE-MINOR-OVERLAP-ENTROPY-v1`

Assume `k>=2` and `delta_k^r>0`. Let

`q_k=2(k-1)/k`.                                                    (4.1)

Then for every residual `R` in the scope of (2.1),

`boxed:
 sup_s E|R-s|^(-1/2)
 <= C_k Z_2^(-1/8) (delta_k^r)^(-1/(8k)),
`
where

`C_k = 4 sqrt(2e) q_k^(-1/4)/(2-q_k)
     = 2k sqrt(2e) [k/(2(k-1))]^(1/4).`                           (4.2)

The same conclusion holds with `delta_k^c` in place of `delta_k^r` by transposing the physical cross block. Hence one may use the larger of the two probabilities.

If an untouched original-coordinate scalar square is available as in (2.2), then

`boxed:
 ||p_Q||_infinity
 <= C_k |a|^(-1/2) Z_2^(-1/8)
       max(delta_k^r,delta_k^c)^(-1/(8k)).
}`                                                                  (4.3)

Equivalently define the homogeneous overlap volume

`Omega_k^r
 = sum_{z_1,...,z_k: S_1 cap ... cap S_k=emptyset}
     product_{l=1}^k d_{z_l}
 = Z_2^k delta_k^r`.                                               (4.4)

Then the half-Riesz estimate reads simply

`sup_s E|R-s|^(-1/2) <= C_k (Omega_k^r)^(-1/(8k))`,               (4.5)

and similarly for columns.

### Proof

Let `C` be the event in (3.3), let

`mu = nu^k( . | C )`,                                             (4.6)

and let `w` be the first marginal of `mu`. Symmetry of `C` makes all `k` marginals equal to `w`.

For each physical row `i`, on `C` it is impossible that all `k` sampled row pairs contain `i`. Therefore

`sum_{l=1}^k 1_{i in S_l} <= k-1` on `C`.

Taking conditional expectation and using symmetry gives

`alpha_i(w)=P_mu(i in S_1) <= (k-1)/k=q_k/2`.                    (4.7)

This is exactly the row-marginal hypothesis of (2.1).

Next, because `mu=nu^k 1_C/delta_k^r`,

`D(mu || nu^k)=log(1/delta_k^r)`.                                (4.8)

Since all marginals of `mu` are `w`, the exact relative-entropy decomposition is

`D(mu || nu^k)
 = D(mu || w^k) + k D(w||nu)
 >= k D(w||nu)`.                                                  (4.9)

Consequently

`D(w||nu) <= (1/k) log(1/delta_k^r)`.                            (4.10)

But by `d_z=Z_2 nu_z`,

`log G_2(w)
 = sum_z w_z log d_z + H(w)
 = log Z_2 - D(w||nu)`.                                          (4.11)

Combining (4.10) and (4.11),

`G_2(w) >= Z_2 (delta_k^r)^(1/k)`.                               (4.12)

Apply the completed peer theorem (2.1) with `q=q_k`; (4.2) follows. Equation (4.3) follows from the dependence-safe scalar-square peel (2.2). Applying the same argument to `M^T` yields the column version. QED.

This proof is entirely in product/original-coordinate space. It uses neither pointwise quadratic-phase decay nor independence after spectral rotation.

## 5. The first new endpoint: three samples

At `k=3`,

`q_3=4/3`,
`C_3=6*3^(1/4)*sqrt(e)=13.019035313822702...`.                   (5.1)

Thus if

`delta_3 = max(delta_3^r,delta_3^c)>0`,

then

`boxed:
 sup_s E|R-s|^(-1/2)
 <=6*3^(1/4)*sqrt(e) Z_2^(-1/8) delta_3^(-1/24).
}`                                                                  (5.2)

With the outer original square,

`boxed:
 ||p_Q||_infinity
 <=6*3^(1/4)*sqrt(e)
   |a|^(-1/2) Z_2^(-1/8) delta_3^(-1/24).
}`                                                                  (5.3)

The exponent `1/24` is deliberately mild: a highly concentrated canonical minor law pays only a twenty-fourth-root penalty before the argument reaches the exact hub residue below.

For computational use there is also an exact one-line formula. Let

`r_S=P_nu(row pair=S)`,
`alpha_i=P_nu(i in row pair)`.

Inclusion-exclusion over the events that row `i` belongs to all three samples gives

`boxed:
 delta_3^r = 1 - sum_i alpha_i^3 + sum_{|S|=2} r_S^3.
}`                                                                  (5.4)

Indeed two distinct common rows can occur only when all three sampled row pairs equal that same pair; there are no triple-row intersections because every `S` has size two.

## 6. Exact zero event = physical star

### Proposition 6.1 — `QFORM-THREE-MINOR-STAR-DICHOTOMY-v1`

For the row support family

`F_r={S: there exists T with det(M_{S,T})!=0}`,                    (6.1)

one has

`delta_3^r=0`

if and only if there is a physical row `i_*` contained in every `S in F_r`. In that case

`rank(M_{I\{i_*},J}) <=1`,                                      (6.2)

and therefore `rank(M)<=2`.

The analogous statement holds for columns.

### Proof

The `if` direction is immediate: if every supported row pair contains `i_*`, then every triple of sampled row pairs has nonempty common intersection.

Conversely assume `delta_3^r=0`. Since every supported minor has positive `nu`-mass, every ordered triple of supported row pairs has nonempty common intersection. In particular every two supported row pairs intersect (repeat one of them as the third sample).

If the support contains only one row pair, it is a star. Otherwise choose distinct supported pairs

`{a,b}` and `{a,c}`.

If some supported pair `G` did not contain `a`, pairwise intersection would force `G={b,c}`. But then

`{a,b} cap {a,c} cap {b,c}=emptyset`,

contradicting `delta_3^r=0`. Hence every supported row pair contains `a`, proving the star claim.

Every physical `2x2` minor of the matrix obtained by deleting row `a` is then zero, so that deleted-row matrix has rank at most one. Restoring one row raises rank by at most one, proving (6.2). QED.

Therefore the new three-sample gate gives an exact qualitative resolution of the peer worker's `fractional-matching-or-hub` debt:

- if either row or column two-minor support is not a star, a concrete entropy-efficient Fourier weight exists automatically and (5.2) pays it;
- if both are stars, there exist physical `i_*,j_*` such that deleting `i_*` leaves row rank at most one and deleting `j_*` leaves column rank at most one. This is an explicit double-hub/low-cross-rank residue for the grouped-star and pair mechanisms.

In particular every physical cross block of rank at least three automatically has both `delta_3^r>0` and `delta_3^c>0`.

## 7. Genuinely rotated indefinite target example where two samples fail but three succeed

Let

`M_0=[[1,0],[0,1],[1,1]]`

and let

`V=[[cos(pi/8),-sin(pi/8)],[sin(pi/8),cos(pi/8)]]`,
`M=M_0 V`.                                                         (7.1)

This is a fixed coefficient rotation, not a rotation of the random inputs. All six physical entries of `M` are nonzero. Right multiplication by `V` preserves every absolute `2x2` minor and the singular values.

The three physical row-pair minors have squared determinants

`d_12=d_13=d_23=1`,                                               (7.2)

so

`Z_2=3`.                                                          (7.3)

The canonical row-pair law is uniform on the three edges of a triangle. Any two triangle edges intersect, hence

`delta_2^r=0`;                                                     (7.4)

the two-sample/disjoint-pair entropy gate is completely unavailable. But three sampled edges have empty common intersection exactly when all three are distinct. Therefore

`delta_3^r=6/27=2/9`,
`Omega_3^r=Z_2^3 delta_3^r=6`.                                   (7.5)

Let `Z,X_1,X_2,X_3,Y_1,Y_2` be arbitrary independent cap-one real inputs and put

`Q_*=Z^2+2 X^T M Y`.                                              (7.6)

Its symmetric coefficient matrix is

`A_*=[1] direct_sum [[0,M],[M^T,0]]`.

Since `M^T M` has exact eigenvalues `3` and `1`,

`spec(A_*)={sqrt(3),1,1,0,-1,-sqrt(3)}`.                         (7.7)

Thus `A_*` is genuinely rotated and indefinite, and it has five eigenvalues of modulus at least one. The target hypotheses are satisfied with room to spare.

Apply (5.3) with `a=1` and `Omega_3^r=6`:

`boxed:
 ||p_(Q_*)||_infinity
 <=6*3^(1/4)*sqrt(e)*6^(-1/24)
 =12.082473081510534... .
}`                                                                  (7.8)

This bound holds for every admissible product input law. It is a new explicit estimate in a physical configuration where the simpler two-minor-disjointness construction has zero probability.

No continuity claim is made in this branch; the result is absolute continuity with an essentially bounded density.

## 8. What this advances, and what remains unpaid

This run is not a full solution. It does, however, close a previously explicit qualitative combinatorial debt: entropy-efficient minor weights do not need to be guessed or optimized globally. Three iid canonical minors either generate one automatically, with a quantitative overlap-volume certificate, or the physical support is an exact star.

The next B04 implication is now narrower:

`QFORM-DOUBLE-STAR-LOW-CROSSRANK-TO-PAID-HUB-v1`:

> In the remaining full-target structural branch, if the relevant physical two-volume is concentrated on a row star and a column star (equivalently the three-sample overlap probabilities vanish on both sides), combine the resulting rank-one-deletion geometry with the existing grouped-square, pair-log, true-pair Schur, or mixed-hub endpoints without paying a vanishing individual coefficient.

For quantitative near-stars, optimize over `k` in (4.3): larger `k` makes `delta_k` increase toward one while the prefactor grows only linearly and the overlap penalty exponent falls as `1/(8k)`. That provides a continuous bridge from diffuse minor support to the exact-star residue.

The full QFORM conjecture remains OPEN; two independent end-to-end reviews of a full candidate are therefore not yet applicable.

## 9. Corrections explicitly respected

This proof does not use any of the following corrected-away premises:

- law-uniform pointwise van-der-Corput/Fresnel decay;
- independence after diagonalizing or rotating the random coordinates;
- arbitrary-joint three-dimensional coarea bounds;
- positive conditional projection-density moments;
- naive fiber-sup dimension-free integration;
- existence of one uniformly good local minor;
- a universal single-pivot Schur rank-two extraction.

All matrix rotations in the explicit example are rotations of the deterministic coefficient block only; the random inputs remain the original independent coordinates.

## 10. Designated partner status

Designated partner `fleet04/B04`: fresh repository search showed current QFORM login/start records but no completed current-QFORM canonical report or shared handoff. No partner theorem is invented. The completed peer actually applied is fleet02/B04 at commit `04297a630381fcfcf429b4c5ec560886bebacb39`.

## 11. Status

`SUPPORTING THEOREM PROVED / EXPLICIT TARGET-VALID ESTIMATE / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.
