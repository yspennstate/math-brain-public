SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-24T11:19:49Z.
attacking: the r58 fixed-cross-star / finite-heavy-row obstruction by spending the whole star against the Parseval frame before selecting any reciprocal physical pair, and converting the diffuse remainder into a determinant-squared pair law.

# fleet03/B06 r59 — fixed star -> heavy coefficient, weighted pair law, or finite two-dimensional hub span

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.
Fresh control commit at startup: `729dbb6257ce9c5bd94b7f3bfec5a41171e048be`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **new deterministic product-weight compiler + designated-partner quantitative splice; full QFORM remains OPEN**.

Incoming B06 source: `yspennstate/math-open-problems@b5c6217b1d62e7ae0e8989018953050a5c1b69af`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T102213Z-fleet03-B06-qform-r58/REPORT.md`.

Designated partner source actually used below: fleet04/B06 theorem `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, canonical source `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B06/20260924T001014Z-fleet04-B06-QFORM-r3/REPORT.md`.

The live corrections are retained: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint rank-three coarea, no conditional projection-density cap, no post-rotation independence, and no unrestricted spectral-fiber supremum.

## 1. Live fixed-star packet from r58

After the r57/r58 global-null reduction and the near-coloop peel, the unresolved geometric branch contains a rank-at-most-three physical carrier

`R = U M U^T`, with `U^T U = I_r`, `r<=3`,

inside the complete child matrix `C=D+R`. In r58 alternative (B), some literal original coordinate `q` has an actual complete cross star

`c_j = C_{qj} = u_q^T M u_j  (j != q)`

with

`||c||_2 >= eta`, where `eta=1/96`.                                         (1.1)

Here `u_j=U^T e_j` is the physical row of the rank-three carrier. The issue is that (1.1) does not force any one `|c_j|` to be large: a fixed star can spread over arbitrarily many original coordinates. Selecting the largest coordinate before using product structure would lose dimension.

The purpose of this run is to aggregate the whole star against the complete Parseval frame first.

## 2. The deterministic star/frame trichotomy

The result is more general than the live constants.

### Theorem 2.1 — `QFORM-FIXEDSTAR-PAIRWEIGHT-TRICHOTOMY-v1`

Let `U in R^{n x 3}` have orthonormal columns and write its rows as `u_j in R^3`, so

`sum_j u_j u_j^T = I_3`.                                                   (2.1)

Fix an original coordinate `q` and a nonzero vector `z in R^3`. Put

`c_j = <z,u_j>  (j != q),`

`S = sum_{j != q} c_j^2`,                                                   (2.2)

and suppose `S >= eta^2`.

Let

`H={j != q : ||u_j||^2 > 1/2}`,
`L={1,...,n}\({q} union H)`.                                                (2.3)

Since `sum_j ||u_j||^2=3`, one has `|H|<=5`.

Then at least one of the following alternatives holds.

**(I) Heavy-star coefficient.** There exists `h in H` such that

`|c_h| >= eta/sqrt(10)`.                                                    (2.4)

**(II) Weighted diffuse pair law.** There exists a unit vector `w perpendicular z` for which the two physical coefficient vectors on `L`,

`a_j=<z/||z||,u_j>`, `b_j=<w,u_j>`,

have complete determinant-squared pair mass

`P_L := sum_{j<k, j,k in L} (a_j b_k-a_k b_j)^2`                            (2.5)

satisfying

`boxed: ||z||^2 P_L >= S/4 >= eta^2/4.`                                    (2.6)

**(III) Finite two-dimensional hub span.** The at-most-six literal coordinates

`E={q} union H`                                                             (2.7)

carry spectral leverage

`sum_{j in E} ||u_j||^2 > 1`,                                               (2.8)

and therefore the row span of `{u_j:j in E}` has dimension at least two.

No reciprocal individual coefficient or minor is used in this theorem.

### Proof

Split

`S_H=sum_{j in H} c_j^2`, `S_L=sum_{j in L} c_j^2`, so `S=S_H+S_L`.

If `S_H>=S/2`, then `H` is nonempty and, because `|H|<=5`,

`max_{h in H}|c_h|^2 >= S_H/|H| >= S/10 >= eta^2/10`,                       (2.9)

which is (I).

Assume henceforth `S_H<S/2`. Then

`S_L>S/2`.                                                                  (2.10)

Define the light-frame Gram matrix

`G_L = sum_{j in L} u_j u_j^T`,                                             (2.11)

so `0<=G_L<=I_3`. Let `e_1=z/||z||` and extend it to an orthonormal basis `(e_1,e_2,e_3)`. In this basis write

`G_L = [[a,b^T],[b,C]]`,                                                     (2.12)

where `a=e_1^T G_L e_1=S_L/||z||^2`.

If `tr G_L<2`, then, using (2.1),

`sum_{j in E}||u_j||^2 = 3-tr G_L >1`.                                      (2.13)

Since any rank-one positive contraction has trace at most one, the rows indexed by `E` cannot span only one spectral direction. This proves (III).

It remains to assume

`tr G_L>=2`.                                                                (2.14)

Because `0<=G_L<=I`, one has `G_L^2<=G_L`. Taking the `(1,1)` entry gives

`a^2+||b||^2 <= a`, hence `||b||^2<=a(1-a)`.                                (2.15)

The positive semidefinite Schur numerator

`K=a C-bb^T`                                                                (2.16)

has trace

`tr K = a tr C-||b||^2
      >= a(tr C-1+a)
      = a(tr G_L-1)
      >= a`.                                                                (2.17)

Since `K` is a `2x2` positive semidefinite matrix, its largest eigenvalue is at least `tr K/2>=a/2`. Choose a unit `w in e_1^perp` attaining that eigenvalue. Then the Gram determinant of the two coefficient vectors `(a_j)_{j in L}` and `(b_j)_{j in L}` is

`det [[sum a_j^2, sum a_j b_j],[sum a_j b_j,sum b_j^2]]
 = a w^T C w-(b.w)^2
 >= a/2.`                                                                   (2.18)

Cauchy-Binet identifies this determinant exactly with the complete pair mass `P_L` in (2.5). Hence

`P_L >= a/2 = S_L/(2||z||^2) > S/(4||z||^2)`,                               (2.19)

which is (II). QED.

### Live numerical specialization

For the r58 fixed star `eta=1/96`, alternative (II) gives the explicit product currency

`boxed: ||z||^2 P_L >= 1/36864.`                                            (2.20)

This is the relevant aggregate-before-inversion statement. A star of fixed l2 size cannot simultaneously avoid every heavy coordinate, avoid every finite two-dimensional hub packet, and have vanishing complete light-bank pair area after the natural `||z||^2` normalization.

## 3. Why this is a curved-fiber replacement rather than a coordinate maximum

The quantity `P_L` is the Cauchy-Binet mass of the complete original-coordinate pair law. If one normalized the weights

`mu({j,k}) = (a_jb_k-a_kb_j)^2/P_L`,                                        (3.1)

then `mu` is a genuine probability law on light-bank physical pairs. The theorem first obtains the total mass `P_L`; it does not choose a pair and pay its reciprocal determinant.

This avoids exactly the dimension loss in the correction `QFORM-FIBER-SUP-DIMENSION-LOSS`: many individually tiny pair minors may carry a fixed total curved area.

## 4. Scaled product-Fourier consequence and actual fleet04/B06 splice

The designated fleet04/B06 theorem proves the following for an orthonormal physical two-frame with row leverage at most `1/2`: the joint density of the two linear statistics is at most four, and after the tangential output shear the off-fold quadratic section obeys

`||g_r||_infinity <= 4/(|lambda| r)`.                                       (4.1)

Apply that result to the actual weighted pair from Theorem 2.1 as follows.

Let `F_L` be the `|L| x 2` matrix with rows `(a_j,b_j)`. Its Gram matrix is

`G_2=F_L^T F_L`, with `det G_2=P_L`.                                         (4.2)

Assume the whitened physical two-frame

`W=F_L G_2^{-1/2}`                                                          (4.3)

satisfies the genuine partner gate

`max_{j in L} ||W_{j,*}||^2 <= 1/2`.                                        (4.4)

Then `(W^T X_L)` has joint density at most four by fleet04/B06's product-Fourier/BL input. Transforming back through `G_2^{1/2}` gives the actual unwhitened statistics `(A,B)=F_L^T X_L` the joint-density cap

`boxed: ||p_{A,B}||_infinity <= 4/sqrt(P_L).`                                (4.5)

Now consider exactly the partner's tangential curved statistic

`Y=lambda(B-b_0)^2 + beta(alpha A+gamma B+B_R)+c`,                           (4.6)

where `B_R` is measurable in a disjoint original-coordinate bank. Repeating the partner's exact completion of the square and determinant-one output shear changes no density norm. Restricting to the true shifted off-fold set `|B-b_*|>r` has at most two inverse branches, each with Jacobian at least `2|lambda|r`. Therefore the actual inequality is

`boxed: ||g_r||_infinity <= 4/(|lambda| r sqrt(P_L)).`                       (4.7)

This is not a new assumption about independence: independence is used only between the original light bank `L` and the source-disjoint bank of `B_R`.

Combining (4.7) with the weighted star output (2.6) gives

`||g_r||_infinity
 <= 8 ||z||/(|lambda| r sqrt(S))
 <= 8 ||z||/(|lambda| r eta).`                                              (4.8)

At the live values `eta=1/96`, `r=1/64`,

`boxed: ||g_{1/64}||_infinity <= 49152 ||z||/|lambda|.`                      (4.9)

The numerical constant is not the point; (4.7) is the partner-backed inequality that spends the **aggregate pair area** rather than a selected minor.

If the whitened gate (4.4) fails, the obstruction is again finite: because `W` has two orthonormal columns,

`sum_{j in L} ||W_{j,*}||^2=2`,                                             (4.10)

so there are at most three coordinates with whitened leverage strictly greater than `1/2`. Thus the weighted pair branch itself either pays the curved off-fold section by (4.7), or emits at most three additional literal pair-heavy coordinates.

## 5. Resulting compiler for the r58 fixed-star branch

The r58 fixed-star certificate `||c||_2>=1/96` now has the following dimension-free compiler.

1. **Heavy-star branch:** among the at-most-five carrier-heavy coordinates there is a literal cross coefficient

`|C_{qh}| >= 1/(96 sqrt(10)).`                                              (5.1)

This is a genuine finite physical pair and may be routed to the existing pair-log / physical-pivot receivers when the accompanying curvature gate is present.

2. **Diffuse weighted-pair branch:** the complete light-bank pair law satisfies

`||z||^2 P_L >= 1/36864`.                                                    (5.2)

If its whitened leverage is diffuse, fleet04/B06 gives the explicit off-fold estimate (4.7). If not, at most three new literal pair-heavy coordinates remain.

3. **Finite hub-span branch:** at most six literal coordinates carry leverage trace greater than one and hence span at least two spectral directions. This is substantially stronger than a bare list of large coordinates: the packet is certified to carry genuinely two-dimensional spectral geometry.

The unresolved issue is now precise. A full scalar payment still needs one of:

- a dependence-safe receiver that combines (5.1) with the retained third spectral scale;
- a scale-compensating lower bound on `|lambda|/||z||` in the weighted-pair geometry of (4.8); or
- a finite-dimensional theorem that consumes the at-most-six two-dimensional hub-span packet (plus at most three pair-heavy rows) while retaining the complete diagonal phase.

No claim is made that (5.1), (5.2), or (2.8) alone closes the full scalar law.

## 6. Diagnostic computation

A fixed-seed numerical diagnostic generated 20,000 random Parseval `n x 3` frames, random distinguished coordinates, and random `z`. For every sample with nonzero star, it checked the three branches exactly as stated. In the weighted-pair branch it diagonalized the `2x2` Schur numerator `aC-bb^T` and verified

`P_L >= S/(4||z||^2)`.

No violation occurred. Among 10,018 samples entering the weighted-pair branch, the smallest observed ratio

`P_L / [S/(4||z||^2)]`

was approximately `1.5127460598`.

This computation is only a sanity check; the proof is the exact contraction inequality `G_L^2<=G_L`, the `2x2` trace bound, and Cauchy-Binet.

## 7. Status

New proved claims:

- `QFORM-FIXEDSTAR-PAIRWEIGHT-TRICHOTOMY-v1`.
- `QFORM-SCALED-TANGENTIAL-OFFFOLD-v1`, equation (4.7), obtained by applying the completed designated fleet04/B06 theorem after exact whitening/Jacobian scaling.

The full quadratic-form bounded-density conjecture is **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity is also **OPEN**. The partner-backed two-output off-fold branch has the continuity stated in its source; the deterministic compiler itself is not a scalar continuity theorem.

Next B06 debt: `QFORM-FINITE9-HUB-OR-SCALECOMPENSATED-CROSS-CURVATURE-v1`: consume the finite six-hub/two-spectral-direction packet plus the at-most-three pair-heavy rows, or prove that the weighted-pair curvature coefficient automatically compensates the `||z||` factor in (4.8), while retaining the full coordinate-separable diagonal phase.
