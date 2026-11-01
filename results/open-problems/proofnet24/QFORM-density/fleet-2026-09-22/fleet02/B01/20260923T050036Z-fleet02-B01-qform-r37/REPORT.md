SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T05:00:36Z.
attacking: the new rank-two cross-kernel currency by building a strict-N3 diffuse rank-three family on which every three-coordinate packet has vanishing currency, then routing the same family through joint Fresnel–Brascamp–Lieb before any tiny packet is inverted.

# fleet02/B01 r37 — single cross-kernel currency is not a universal N3 resource

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Classification:** `EXPLICIT STRUCTURAL OBSTRUCTION + SOURCE-VALID PAID TARGET FAMILY / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. What is attacked

The newest completed designated-partner theorem, fleet03/B01 `QFORM-RANK2-CROSS-TRANSVERSE-L4-v1`, assigns to a three-original-coordinate center `I` and disjoint original-product bank `J`, with `K=A_IJ` of rank two,

`Delta=sigma_1(K)sigma_2(K)`,  `d=|z^T A_II z|`,  `z in ker(K^T)`, `|z|=1`,

and proves

`||p_Q||_infinity <= kappa (Delta^2 d)^(-1/5)`,
`kappa=(15/4)6^(2/5)=7.6787719165...`,

when `d>0`, while retaining arbitrary curvature on both active sides and all outside variables. Its stated structural debt is to show that the strict-N3 remainder either has one packet with `Delta^2 d` uniformly positive or else is forced into an already-paid branch.

This run kills the first alternative as a possible universal structural statement. The obstruction is itself safely paid by the newest joint Fresnel–Brascamp–Lieb theorem, so it is not a counterexample to QFORM.

## 2. Diffuse rank-three diagonal-twist family

Split the original coordinates into three disjoint banks `U,V,W`, each of size `m>=3`. Let `u,v,w` be the normalized constant vectors on those banks, extended by zero off their own bank. Thus `u,v,w` are orthonormal. Define

`A_m = u u^T - 2 v v^T + w w^T + m^(-1) I_(3m)`.       (2.1)

The spectrum is explicit:

`1+1/m` on `u`,
`-2+1/m` on `v`,
`1+1/m` on `w`,
`1/m` on the orthogonal complement.                            (2.2)

Hence every `A_m` is in the exact QFORM target: it has three eigenvalues of modulus at least one.

The physical coefficients are also explicit. On the `U` and `W` banks the diagonal is `2/m` and within-bank off-diagonal entries are `1/m`. On the `V` bank the diagonal is `-1/m` and within-bank off-diagonal entries are `-2/m`. Cross-bank entries vanish. Therefore

`max_i |A_ii| = 2/m`,
`max_{i<j} |det A[{i,j},{i,j}]| = 4/m^2`.                       (2.3)

Consequently, for every fixed no-pivot threshold `tau>0`, this family lies in strict N3 for all sufficiently large `m`.

## 3. Every three-coordinate rank-two cross-kernel currency vanishes

Take **any** original-coordinate set `I` with `|I|=3` and **any** disjoint original-coordinate bank `J`. Suppose

`K=A_m[I,J]`

has rank two. Let

`Delta=sigma_1(K)sigma_2(K)`

and let `z` be a unit generator of `ker(K^T)`. Put

`d=|z^T A_m[I,I] z|`.                                           (3.1)

The diagonal twist in (2.1) contributes nothing to the disjoint cross block `K`. A row of `K` belonging to bank `g` has entries `lambda_g/m` only in columns of `J` from that same bank, with `lambda_g in {1,-2,1}`. Thus every row has squared Euclidean norm at most `4/m`, and because there are only three rows,

`||K||_F^2 <= 12/m`.                                            (3.2)

Since `rank K=2`,

`Delta = sigma_1 sigma_2
       <= (sigma_1^2+sigma_2^2)/2
       = ||K||_F^2/2
       <= 6/m`.                                                  (3.3)

Next write

`A_m[I,I]=m^(-1) I_3 + B_0`.                                    (3.4)

The matrix `B_0` is block diagonal according to which of the three banks the coordinates of `I` come from. A block containing `k<=3` coordinates from bank `g` is `(lambda_g/m) 11^T`, whose only nonzero eigenvalue has modulus `|lambda_g|k/m<=6/m`. Hence

`||B_0||_op <= 6/m`,
`d <= ||A_m[I,I]||_op <= 7/m`.                                  (3.5)

Combining (3.3)-(3.5) gives the universal packet estimate

`boxed:  Delta^2 d <= 252/m^3`                                  (3.6)

for **every** three-coordinate / disjoint-bank packet having rank-two cross block.

Therefore

`sup_{|I|=3, J disjoint, rank A_IJ=2} Delta(I,J)^2 d(I,J) -> 0`. (3.7)

So the three-large-eigenvalue hypothesis, even inside strict N3, cannot force one fleet03/B01 cross-kernel packet with universally positive determinant currency.

This refines the older correction `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`: the new statement explicitly includes the transverse kernel-curvature factor `d` introduced by the newest partner theorem and controls *all* disjoint banks `J`, not one prescribed cross bank.

## 4. Actual application of the completed partner theorem

The partner result is not merely cited. Choose

`I={U_1,U_2,V_1}`

and let `J` be all remaining original coordinates. Then `K=A_m[I,J]` has rank two. The two `U` rows are identical on the remaining `m-2` `U` coordinates, and the `V` row is supported on the remaining `m-1` `V` coordinates. Hence the two nonzero eigenvalues of `KK^T` are

`2(m-2)/m^2` and `4(m-1)/m^2`,

so

`Delta^2 = 8(m-2)(m-1)/m^4`.                                   (4.1)

A unit kernel vector is `z=(1,-1,0)/sqrt(2)`, and the exact center block is

`[[2/m,1/m,0],[1/m,2/m,0],[0,0,-1/m]]`,

therefore

`d=1/m`.                                                         (4.2)

The completed fleet03/B01 theorem consequently gives the valid target-family estimate

`||p_Q||_infinity
 < kappa [m^5/(8(m-2)(m-1))]^(1/5)`,                            (4.3)

with `kappa=(15/4)6^(2/5)`. This certificate deteriorates like

`(kappa/8^(1/5)) m^(3/5) = 5.066100... m^(3/5)`,                 (4.4)

although the true target family is uniformly controllable. Because (3.6) holds for every rank-two packet, changing the three-coordinate center cannot repair the single-packet currency on this family.

## 5. The same family is uniformly paid by the newest joint averaged-frequency theorem

Now apply the required newest decoupling/Fresnel–Brascamp–Lieb source at
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Write

`A_m = R Lambda R^T + D`,
`R=[u v w]`, `Lambda=diag(1,-2,1)`, `D=m^(-1)I`.                 (5.1)

Take the theorem's active coordinate set to be all `3m` coordinates. Then

`G=R^T R=I_3`,                                                   (5.2)

and every normalized row leverage is exactly `1/m<=1/2`. Theorem F therefore gives the genuine joint-frequency estimate

`|phi_Q(t)|
 <= (4 pi)^(3/2) 2^(-1/2) |t|^(-3/2)`,                         (5.3)

and Fourier inversion yields

`boxed: ||p_Q||_infinity <= 12 * 2^(-1/3)
                         = 9.5244063118...`                     (5.4)

for **every** independent input family with densities bounded by one, uniformly in `m`.

The diagonal `m^(-1)I` is absorbed as the allowed diagonal oscillatory twist; no perturbative approximation, moment condition, support condition, Gaussian assumption, post-rotation independence, or arbitrary-joint coarea statement is used.

This is exactly the required oscillatory replacement. The scalar phase-aligned-density construction still refutes any law-uniform pointwise `|t|^-1/2` Fresnel bound. Here the integrable `|t|^-3/2` decay is created jointly by the three spread directions through Brascamp–Lieb.

## 6. Structural consequence

The partner's first alternative, “strict N3 forces a three-coordinate rank-two cross-kernel packet with `Delta^2 d >= c`,” is false. The family (2.1) has

`sup packet currency <=252/m^3 ->0`

while its density is uniformly `<9.525` by the source-valid diffuse rank-three theorem.

Thus the structural theorem needed after the new fleet03/B01 analytic receiver must be a **routing theorem**, not a universal single-packet lower bound:

`QFORM-N3-KERNEL-CURRENCY-FAILURE-ROUTING-v1`:
if every three-coordinate rank-two packet has small `Delta^2 d`, prove that the matrix is quantitatively forced into a paid diffuse rank-three/diagonal-twist, volume, hub, grouped-square, ridge, exact-null or physical-pair branch before any reciprocal tiny packet is paid.

The present family supplies an exact model for the diffuse-rank-three exit. It does not prove that every small-currency strict-N3 matrix has such an exit.

## 7. Status and checks

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. This report is a supporting structural obstruction plus a fully paid target-valid stress family. It is not a full candidate and has not received two independent end-to-end reviews.

`CHECK.py` and the actual `CHECK.txt` in this run directory verify the exact spectrum formula, strict-N3 scales, the explicit packet determinant currency, the partner theorem constant, and the Theorem-F constant; the output ends `STATUS=PASS`. The checker is regression evidence only; the proof is Sections 2–5 above.
