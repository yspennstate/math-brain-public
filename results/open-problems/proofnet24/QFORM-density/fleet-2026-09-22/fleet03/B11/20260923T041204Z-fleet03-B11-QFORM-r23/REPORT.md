SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T04:12:04Z.
attacking: the near-null one-sign low-cross-rank hub-star residual via a product-preserving heavy-star aggregation inequality.

# fleet03/B11 — scale-sensitive balanced near-rank-one recoloring

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T041204Z-fleet03-B11-QFORM-r23`  
**Assignment:** indefinite signatures `(2,1)` and `(1,2)`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING TARGET-LEVEL PACKET THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the new balanced robust-recolor branch by the Fourier/volume exits below; not claimed for the separate sign-frustrated partner exit. The unrestricted continuous-density conclusion remains open.

## 1. Exact target and correction boundary

The target remains unrestricted: for every dimension, every family of independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or give a genuine counterexample.

This report does not assume Gaussianity, moments, compact or connected support, log-concavity, post-rotation independence, law-uniform pointwise van-der-Corput decay, the refuted arbitrary-joint three-dimensional coarea estimate, a positive worst-fibre conditional-density moment, or perturbative deletion of small coefficients. It retains the current correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`; the argument below is not a small-pivot half-Riesz approximation.

The new point is to splice three already proved ingredients in a regime where their hypotheses become automatic after a **cap-preserving diagonal normalization of original independent coordinates**:

1. fleet01/B08's exact-rank-one recoloring algebra: if `C,D` have `s_2>=c` and the two off-diagonal blocks are exactly rank at most one, then the recolored third exterior volume is at least `(7/2)c^6`;
2. the fractional three-volume theorem: diffuse third-volume marginals imply a continuous density bounded by `[3e/((3-2q)sqrt(q))] Z^(-1/6)`;
3. the square physical rank-three cross-block Fourier theorem: an invertible `3x3` cross block `B` between two three-coordinate product banks gives `||p_Q||_infinity <=3 |det B|^(-1/3)` and a continuous density.

The scale-free perturbation of item 1 is false: fleet01/B08 gives an explicit `R=1/epsilon` family with an arbitrarily thin rank-one tube but recolored `E_3=0`. The theorem below identifies a natural B11 chamber in which that pathology cannot occur: pair-PSD hidden-minority geometry, after normalization, forces every relevant coefficient block to have bounded operator scale.

## 2. Linear-algebra lemma: robust recoloring at controlled scale

For a real matrix `T`, write

`E_3(T)=e_3(T^T T)=||wedge^3 T||_HS^2`.

### Lemma 2.1 — `QFORM-SCALE-SENSITIVE-NEARRANK1-RECOLOR-v1`

Let `C,D,U,V` be real `2x2` matrices and

`M=[[C,U],[V,D]]`.

Assume

` s_2(C)>=c>0,  s_2(D)>=c,`                                      (2.1)

and there are rank-at-most-one matrices `U_0,V_0` with

`||U-U_0||_op<=epsilon,   ||V-V_0||_op<=epsilon`.                (2.2)

Suppose also

`||C||_op,||D||_op,||U_0||_op,||V_0||_op <= L`.                 (2.3)

If

`epsilon <= sqrt(7/2)c^3/(16 L^2)`,                              (2.4)

then

`boxed: E_3(M) >= 7 c^10/(512 L^4).`                             (2.5)

#### Proof

Put

`M_0=[[C,U_0],[V_0,D]]`.

The completed exact-rank-one recoloring lemma of fleet01/B08 gives

`E_3(M_0)>= (7/2)c^6`.                                          (2.6)

Because every block in `M_0` has operator norm at most `L`,

`||M_0||_op<=2L`.                                                (2.7)

Let `s_1>=s_2>=s_3>=s_4` be the singular values of `M_0`. Every triple singular-value product contains a factor at most `s_3`; hence

`E_3(M_0)
 =sum_(i<j<k)(s_i s_j s_k)^2
 <=4(2L)^4 s_3(M_0)^2
 =64 L^4 s_3(M_0)^2`.                                           (2.8)

Combining (2.6)--(2.8),

`s_3(M_0)>= sqrt(7/2)c^3/(8L^2).`                               (2.9)

The perturbation is

`M-M_0=[[0,U-U_0],[V-V_0,0]]`.

Its squared operator is block diagonal, so exactly

`||M-M_0||_op=max{||U-U_0||_op,||V-V_0||_op}<=epsilon`.          (2.10)

By singular-value perturbation and (2.4),

`s_3(M)>= sqrt(7/2)c^3/(16L^2)`.                                (2.11)

The block `C` is an orthogonal row/column compression of `M`, so

`s_2(M)>=s_2(C)>=c`; hence also `s_1(M)>=c`.                     (2.12)

One term in `E_3(M)` is therefore enough:

`E_3(M)
 >=(s_1(M)s_2(M)s_3(M))^2
 >=c^4 * [(7/2)c^6/(256L^4)]
 =7c^10/(512L^4).`                                               (2.13)

This proves the lemma. QED.

The exponent `c^10 L^-4` is not claimed sharp. What matters is that the perturbation scale is **relative to the rank-one core scale**. This is exactly what the scale-free B08 counterexample shows is necessary.

## 3. Hidden-minority pair-PSD normalization supplies the missing scale bound

Let `S` be eight ORIGINAL coordinates. Assume, after possibly replacing the whole quadratic form by its negative, that

`a_r=A_rr>=m>0  for every r in S`,                               (3.1)

and every physical `2x2` principal block on `S` is positive semidefinite:

`A_rr A_ss-A_rs^2>=0`.                                           (3.2)

Define normalized coefficients

`rho_rs=A_rs/sqrt(a_r a_s)`.                                     (3.3)

Then `|rho_rs|<=1`.

There are two preliminary exits which use no recoloring.

- If some `rho_rs=0`, that physical pair is positive definite with determinant at least `m^2`; the definite-pair theorem gives `||p_Q||_infinity<=pi/m`.
- If some triangle has nonzero edge-sign product `-1`, the completed sign-frustrated physical-triangle theorem from the designated partner fleet04/B11, spliced with the definite-pair complement, gives `||p_Q||_infinity<=4pi/m`. The actual partner inequality used is displayed in Section 6 below.

Thus in the unpaid pair-PSD packet every edge is nonzero and every triangle has positive sign product. This forces a global sign gauge: fix one vertex `r_0`, set `sigma_r=sign(rho_(r_0 r))`, and use the triangle `(r_0,r,s)` to obtain

`sign(rho_rs)=sigma_r sigma_s`.                                  (3.4)

Replacing each source variable `X_r` by `sigma_r X_r` preserves independence and all density caps. After that physical sign change,

`0<rho_rs<=1` throughout the packet.                              (3.5)

In particular every normalized `2x2` coefficient block has Frobenius, hence operator, norm at most `2`.

This is precisely the scale control missing from the B08 scale-free near-rank-one tube: the huge `R=1/epsilon` core cannot occur after pair-PSD normalization.

## 4. Main packet theorem

Partition the eight coordinates into four disjoint two-coordinate packets

`S=I_+ disjoint_union I_- disjoint_union J_+ disjoint_union J_-`.

After the global sign gauge of Section 3, let `R=(rho_rs)_(r,s in S)` be the normalized physical matrix and define

`C=R[I_+,I_-],   D=R[J_+,J_-],`
`U=R[I_+,J_-],   V=R[J_+,I_-].`                                  (4.1)

### Theorem 4.1 — `QFORM-HIDDEN-MINORITY-ROBUST-RECOLOR-PACKET-v1`

Under (3.1)--(3.2), suppose

`s_2(C)>=c>0,   s_2(D)>=c`,                                      (4.2)

and `U,V` are each within operator distance at most `epsilon` of a rank-at-most-one `2x2` matrix. If

`epsilon <= c^3/80`,                                             (4.3)

then one of the following holds:

1. a zero edge or sign-frustrated triangle already yields

`||p_Q||_infinity <=4pi/m`;                                      (4.4)

2. the balanced packet has a bounded **continuous** density and

`boxed: ||p_Q||_infinity
 <= C_packet /(m c^(5/3)),`                                      (4.5)

where

`C_packet=(9sqrt(3)e/2)(41472/7)^(1/6)
         =90.1246891247... .`                                    (4.6)

All coefficients, spectrum and couplings outside these eight original coordinates are arbitrary.

#### Proof of the balanced branch

By (3.5), `||C||,||D||,||U||,||V||<=2`. Since a rank-one approximant can be chosen within `epsilon`, and (4.2) plus the entry cap imply `c<=2`, condition (4.3) gives `epsilon<=1/10`. Thus we may take

`L=3`                                                            (4.7)

in Lemma 2.1. Moreover

`1/80 < sqrt(7/2)/144`,                                          (4.8)

so (4.3) implies the required perturbation condition (2.4) with `L=3`. Therefore for the recolored normalized cross block

`M=[[C,U],[V,D]]`                                                 (4.9)

between

`K=I_+ union J_+,  Lbank=I_- union J_-`,                         (4.10)

we have

`Z:=E_3(M)>= 7 c^10/41472`.                                      (4.11)

Now condition on every original coordinate outside `S`. For each `r in S` make the **coordinatewise** change of random variable

`Z_r=sqrt(a_r/m) X_r`.                                           (4.12)

Because `a_r>=m`, the transformed density is

`p_(Z_r)(z)=sqrt(m/a_r) f_r(sqrt(m/a_r)z)<=1`.                   (4.13)

Thus the transformed variables remain independent cap-one ORIGINAL product coordinates. This is not a spectral rotation. In the transformed quadratic polynomial the normalized eight-coordinate block is multiplied by `m`; in particular the recolored cross block is exactly

`m M`.                                                           (4.14)

All outside terms have become arbitrary deterministic affine terms under the conditioning, which both analytic inputs below allow.

Give the normalized third minors of `M` the usual squared-volume sampling law and let `alpha_i,beta_j` be row and column inclusion marginals.

**Diffuse-volume case.** If one orientation has all row marginals at most `2/3`, apply the fractional three-volume theorem with `q=4/3` to `mM`. If instead the column marginals are good, apply it to `(mM)^T`. Because

`E_3(mM)=m^6 Z`,                                                 (4.15)

we obtain a continuous density and

`||p_Q||_infinity
 <=(9sqrt(3)e/2)m^-1 Z^-1/6
 <=C_packet/(m c^(5/3)).`                                       (4.16)

**Concentrated-volume case.** Otherwise some row and some column have marginals greater than `2/3`. For the squared-minor sampling law,

`P(i in row triple and j in column triple)>1/3`.                 (4.17)

Hence the sum `W_ij` of squared `3x3` minors incident to that row and column obeys

`W_ij>Z/3`.                                                       (4.18)

Because `M` is only `4x4`, exactly

`binom(3,2)^2=9`                                                  (4.19)

such minors occur. Therefore at least one physical `3x3` cross subblock `B` satisfies

`|det B|^2>Z/27`.                                                 (4.20)

For the scaled variables its cross block is `mB`, so the completed square rank-three physical cross-block Fourier theorem gives a continuous density with

`||p_Q||_infinity
 <=3 |det(mB)|^-1/3
 <3sqrt(3)m^-1 Z^-1/6
 <=22.1033468473... /(m c^(5/3)).`                               (4.21)

This is smaller than the diffuse bound (4.16). Thus (4.5) holds in both cases. Averaging over the conditioned outside coordinates preserves the same essential bound; the cited Fourier theorems already give the full ambient continuous representative in this original-coordinate setting. QED.

## 5. Why this is a genuine advance over the thin-tube obstruction

Fleet01/B08 exhibited a target-valid family for which a cross block is `O(epsilon)`-close in Frobenius norm to rank one while the rank-one core has size `R=1/epsilon`; after recoloring, the two off-diagonal blocks multiply to the identity and the third exterior volume vanishes exactly. Therefore no theorem of the form

`dist(B,rank1)<=epsilon and child curvature>=c  => E_3>=F(c,epsilon)>0`

can hold without a scale parameter.

The pair-PSD hidden-minority chamber supplies that scale parameter for free after diagonal normalization. Every normalized coefficient satisfies `|rho_rs|<=1`, so all `2x2` blocks have operator norm at most `2`. Lemma 2.1 then turns the near-rank-one tube into the explicit positive third-volume floor (4.11). The apparent perturbation obstruction is therefore not present inside this normalized physical chamber.

This is not a small-coefficient perturbation of the random quadratic form. Every coefficient in the actual form is retained. The perturbation is used only in a deterministic singular-value/exterior-volume inequality for the actual coefficient block, after which a theorem for that actual block is applied.

## 6. Designated partner applied at an actual inequality

The completed designated partner fleet04/B11 result is `QFORM-SIGN-FRUSTRATED-NEAR-NULL-TRIANGLE-v1` from

`yspennstate/math-open-problems@572f6cd066c9cdef7b5a509917b4dcd79cea2fda`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T021512Z-fleet04-B11-sign-frustrated-triangle-r4/REPORT.md`.

For a sign-frustrated physical triple with positive diagonals `a_r`, `m=min a_r`, and normalized edges within `eta<1/2` of a frustrated sign pattern, it gives

`||p_Q||_infinity <=6sqrt(pi)/[m(1-2eta)]`.                      (6.1)

Apply this to the present pair-PSD packet. For a sign-frustrated triangle put

`d_rs=1-rho_rs^2`.

If some `d_rs>=1/16`, the definite physical-pair theorem gives

`||p_Q||_infinity<=4pi/m`.                                      (6.2)

If every `d_rs<1/16`, then

`|rho_rs|>sqrt(15)/4`,
`eta_0=1-sqrt(15)/4`,                                            (6.3)

and the partner theorem gives the actual inequality

`||p_Q||_infinity
 <=6sqrt(pi)/[m(sqrt(15)/2-1)]
 =11.3559184890.../m
 <4pi/m`.                                                         (6.4)

Thus the partner result removes the entire sign-frustrated complement **before** the scale-sensitive balanced recoloring argument is invoked. This is what licenses the global sign gauge (3.4) in the remaining branch.

## 7. Rank-two logarithmic control and the role of the third direction

The mandatory opposite-sign rank-two control is unchanged. For independent

`X,Y ~ Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|))`,   `0<|t|<1/2`,                       (7.1)

so rank two genuinely has a logarithmically unbounded density.

The new packet theorem identifies a separate, product-preserving way the third direction removes that endpoint. In the balanced near-rank-one chamber, two child rank-two resources survive. Recoloring turns them, despite the near-rank-one outer coupling, into a quantitative **third exterior volume**. If that volume is diffuse, the fractional three-volume Fourier exponent is strictly integrable (`q=4/3` gives time exponent `9/8>1`). If the volume concentrates, a single physical `3x3` cross block appears and gives the rank-three Fourier tail `|t|^-3/2`, again integrable. The rank-two endpoint would only supply `|t|^-1`.

So here the third direction is not postulated in rotated eigen-coordinates: it is constructed from actual original-coordinate product banks and paid either by distributed third-volume or by a literal three-by-three physical cross determinant.

## 8. What remains

The full conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**.

The new theorem pays a scale-sensitive portion of the prior B11 obstruction `QFORM-HIDDEN-MINORITY-BALANCED-NEAR-RANKONE-AGGREGATION-v1`. What remains is the **structural extraction** problem under only the three-large-eigenvalue hypothesis:

- force a fixed-scale eight-coordinate packet with the two child `s_2` bounds and the normalized near-rank-one outer blocks required by Theorem 4.1; or
- route failure of that packet into an already-paid ridge/diffuse/cross-volume, scalar-pivot, null-pivot, sign-frustrated, definite-pair, or grouped-coordinate branch.

The theorem allows arbitrary additional spectrum and arbitrary outside couplings once the packet is present. It does not assert that such a packet is automatic. In high-cardinality bank examples, fixed packets can still be tiny; aggregation before reciprocal-minor payment remains necessary.

Continuity is proved in the new balanced robust-recolor branch through the two Fourier exits. Continuity is **not** newly proved for the partner sign-frustrated branch or for the unrestricted target.

## 9. Source pins

- designated partner fleet04/B11: `yspennstate/math-open-problems@572f6cd066c9cdef7b5a509917b4dcd79cea2fda`, path above;
- exact-rank-one recoloring and its scale-free obstruction: fleet01/B08 report present at `yspennstate/math-open-problems@81d042c1d5c1c0e4c861ab9f55c3d4564b05323d`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260923T033753Z-fleet01-B08-QFORM-auto11/REPORT.md`;
- fractional three-volume theorem: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`;
- square rank-three physical cross-block Fourier theorem: fleet02/B02 report present at `yspennstate/math-open-problems@81d042c1d5c1c0e4c861ab9f55c3d4564b05323d`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/B02-20260922T120900Z-qform-r11/REPORT.md`.

No full-solution claim is made. Independent end-to-end reviews of a hypothetical full solution are not applicable because the full theorem remains open.
