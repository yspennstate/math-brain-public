SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T05:47:10.476505Z.
attacking: fractional mixed-order Jensen extension and a simultaneous double-nested determinant router for the actual spectral-gate hybrid, preserving the full matrix and original-coordinate product law.

# fleet02/B08 r22 — mixed-order Jensen and double-nested hybrid router

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ROUTER + TARGET-VALID MECHANISM STRESS FAMILY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains open. Inputs throughout are independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one. The matrix is arbitrary real symmetric with at least three eigenvalues of modulus at least one. No moments, compact support, connected support, iid assumption, Gaussianity, log-concavity, post-rotation independence, law-uniform pointwise stationary phase, arbitrary-joint coarea, worst conditional-density cap, or perturbative deletion of a small quadratic matrix tail is used. Essential boundedness is the target; continuity is asserted only on the Fourier-paid branches.

## 1. Source pins actually used

Fresh owner control was read from `yspennstate/math-research-brain`, revision `2026-09-22.15`, with QFORM as the sole target and no later stop at the control read.

The immediate B08 predecessor is

`yspennstate/math-open-problems@2e8dce7760ed0b7dc1ab1be7b9d82ecc3c7b7df1`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T050537Z-fleet02-B08-qform-diffuse-r21-ead7cd5c/REPORT.md`.

It proves `QFORM-FRACTIONAL-VOLUME-SELF-MATCHED-ROUTER-v1`. If an ORIGINAL-coordinate cross block `B` has

`Z3=e3(B^T B)>=zeta^6`,

then either the full ambient form is paid by the fractional third-volume theorem, or there are a physical row `i` and column `a` with

`Z_ia:=sum_(S contains i,T contains a) det B[S,T]^2 >(38/125) Z3`,        (1.1)

and the remaining obstruction is an anchor star or a conditional residual-volume concentration.

The newest designated partner actually used is fleet03/B08 r27,

`yspennstate/math-open-problems@e76d2e984f81a058590bb143ff21e387fbbeab09`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T042303Z-fleet03-B08-qform-diffuse-r27/REPORT.md`.

For an anchored packet `Z`, anchor-row norm `R`, and normalized anchored third-minor law with residual row marginals `alpha_k`, it constructs a half order-three / half order-two physical-minor law `Omega` with

`kbar=5/2`, `K(Omega)>=2Z/R`, anchor row marginal `1/2`, residual row marginals exactly `alpha_k`.   (1.2)

At the old threshold `max alpha_k<=1/2`, the mixed-order Fourier theorem gives

`||p_Q||inf <=10 sqrt(e) (2Z/R)^(-1/5)`.

The mixed-order Fourier theorem itself is fleet01/B01 at

`yspennstate/math-open-problems@86f318f0826325e6df3504e1e8ec15f4316cc861`.

The required newest-Claude source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

I use its proved Jensen extension D' as the model for the new variable-order argument, and in Section 6 apply its proved mixed-Fresnel hub theorem to an actual exact-target family.

## 2. New analytic lemma: fractional Jensen for a mixed-order minor law

Let `I,J` be disjoint original-coordinate banks, condition all other original coordinates, and put `M=A[I,J]`. Let `Omega` be a probability law on nonzero square physical minors `M[S,T]` of possibly varying order. Define

`alpha_i=P(i in S)`, `beta_j=P(j in T)`,
`kbar=E|S|=sum_i alpha_i=sum_j beta_j`,
`K=exp(E log det(M[S,T])^2 + H(Omega))`.

### Theorem 2.1 — `QFORM-MIXED-ORDER-JENSEN-v1`

Suppose

`q>=1`, `q<kbar/2`, and `alpha_i<=q/2` for every row `i`.                 (2.1)

Then the full ambient quadratic form, retaining arbitrary same-side blocks, conditioned outside couplings and induced affine terms, has a continuous `C0` density satisfying

`boxed:
 ||p_Q||inf <= 2 sqrt(e) [kbar/(kbar-2q)] q^(-1/2) K^(-1/(2kbar)).
`                                                                         (2.2)

### Proof

The decoupling step used in the completed mixed-order theorem gives

`|phi(t)|^2 <= E_W F(W)`,
`F(W)=prod_i |psi_i(2t <r_i,W>)|`,                                      (2.3)

where `W` has an original-coordinate product probability density with each coordinate density at most one. Since this is a probability measure,

`E F <= (E F^q)^(1/q)`.                                                  (2.4)

Apply the identical Brascamp--Lieb determinant expansion to `F^q`. The Gaussian determinant/currency part is unchanged. On row `i` the source one-dimensional Fourier lemma is now used at exponent

`p_i=q/alpha_i>=2`.                                                       (2.5)

It gives

`int |psi_i(s)|^(q/alpha_i) ds <=4 pi sqrt(alpha_i/q)`.                  (2.6)

After `s=2t x`, the `alpha_i` factors cancel the BL row entropy exactly as in the `q=1` proof, while the new factors multiply to `q^(-kbar/2)`. The column factors remain bounded by one and contribute the same `e^(kbar/2)`. Thus

`E F^q <= e^(kbar/2)(2pi/|t|)^kbar q^(-kbar/2) K^(-1/2)`.               (2.7)

By (2.3)-(2.4),

`|phi(t)| <= B |t|^(-kbar/(2q))`,
`B=e^(kbar/(4q))(2pi)^(kbar/(2q)) q^(-kbar/(4q)) K^(-1/(4q))`.          (2.8)

Set `a=kbar/(2q)>1`. Since `|phi|<=1`,

`int_R min(1,B|t|^-a) dt = 2a/(a-1) B^(1/a)`,                           (2.9)

and

`B^(1/a)=sqrt(e)(2pi) q^(-1/2) K^(-1/(2kbar))`.                         (2.10)

Fourier inversion yields (2.2). The integrable characteristic function gives a continuous `C0` representative. QED.

For fixed order `kbar=3`, (2.2) is exactly the Claude D' constant after setting `q=2h`; thus the new formula is consistent with the completed source rather than introducing a different normalization.

## 3. Apply the partner construction beyond the one-half marginal wall

In the fleet03/B08 anchored construction (1.2), choose a residual marginal threshold

`h=9/16`, `q=2h=9/8`.                                                   (3.1)

The partner law has `kbar=5/2`; hence `q<5/4=kbar/2`. If every residual anchored marginal is at most `9/16`, Theorem 2.1 and `K>=2Z/R` give

`boxed:
 ||p_Q||inf <= (40/3)sqrt(2e) (2Z/R)^(-1/5).
`                                                                         (3.2)

This strictly enlarges the partner's `1/2` marginal scope. The price is only in the explicit constant.

## 4. New structural theorem: paid, star, or simultaneous double-nested packet

### Theorem 4.1 — `QFORM-FRACTIONAL-MIXED-JENSEN-DOUBLE-NESTED-ROUTER-v1`

Let `B` be any ORIGINAL-coordinate cross block and suppose

`Z3=e3(B^T B)>=zeta^6`.                                                   (4.1)

Then at least one of the following holds.

**PAID.** The full ambient form has a continuous `C0` density and

`boxed: ||p_Q||inf <34.342/zeta.`                                        (4.2)

**STAR.** There is a physical row or column anchor with Euclidean cross-star norm greater than `zeta`.

**DOUBLE-NESTED.** There exist distinct physical rows `i,k` and distinct physical columns `a,b` such that

`boxed:
 sum_(ell,c) det B[{i,k,ell},{a,b,c}]^2 > (19/500) Z3,
`                                                                         (4.3)

where the sum ranges over residual physical row/column indices making a `3x3` minor.

### Proof

Apply the predecessor router. Its fractional branch is already paid by `<18.218/zeta`, hence by (4.2). Otherwise it supplies `i,a` with the anchored packet (1.1).

If either anchor cross-star norm is `>zeta`, the STAR conclusion holds. Assume both are at most `zeta`.

Condition the normalized third-minor law on the anchor event `(i in S,a in T)`. If the maximum conditional residual-row marginal is at most `9/16`, apply (3.2) with `Z=Z_ia` and `R<=zeta`. Since

`2Z/R > 2(38/125) zeta^6/zeta = (76/125) zeta^5`,                         (4.4)

we obtain

`||p_Q||inf
 < (40/3)sqrt(2e)(125/76)^(1/5) zeta^-1
 =34.3415789778... zeta^-1`.                                            (4.5)

The same argument applies after transposing `B` if the conditional residual-column marginals are all at most `9/16`.

If neither orientation pays, choose a residual row `k` and residual column `b` whose conditional inclusion probabilities are each `>9/16`. They are events under the SAME anchored determinant law, so the union bound gives

`P(k in S, b in T | i in S,a in T) > 2(9/16)-1=1/8`.                    (4.6)

Multiplying by the anchored currency and using (1.1),

`sum_(ell,c) det B[{i,k,ell},{a,b,c}]^2
 > Z_ia/8
 > (38/125)(1/8) Z3
 = (19/500) Z3`.                                                         (4.7)

This is (4.3). QED.

The key improvement is that the old survivor had a row nested packet and a column nested packet separately. The new Jensen room forces them to intersect quantitatively unless a star is already large. No reciprocal minor has been selected.

## 5. Feed the theorem back into the actual spectral gate

Use the B08 actual-spectral-gate scale

`beta=(3L/16)sqrt(3/5)=0.145236875482778...L`.                            (5.1)

All preceding low-rank-tube and D5 alternatives remain unchanged. On the third-volume branches, Theorem 4.1 gives the following sharper residual classification.

### k=0 actual child count

Take `zeta_0=beta`. Then the new paid branch is

`||p_Q||inf <236.453/L`,                                                  (5.2)

or there is a star of norm `>zeta_0`, or a fixed double-nested packet of mass

`>3.56652259827e-7 L^6`, equivalently sixth-root scale `>0.08421203521 L`. (5.3)

The previous `<126/L` exit is retained where it applies; (5.2) is the additional payment that removes all no-star single-sided nested states.

### k=1 actual child count

After the existing genuine rank-two Frobenius tube and the completed D5 `<335/L` branch, the cross-volume scale is

`zeta_1=beta/14400^(1/6)=0.0294453337964...L`.                            (5.4)

The remaining cross-volume state is therefore paid by

`||p_Q||inf <1166.283/L`,                                                 (5.5)

or has a star `>zeta_1`, or a double-nested packet of mass

`>2.47675180435e-11 L^6`, sixth-root scale `>0.01707315362 L`.            (5.6)

### k=2 actual child count

After the existing genuine rank-one/rank-two tubes and D5 branches, the final third-volume scale is

`zeta_2=(beta/120)/225^(1/6)=0.000490755563273...L`.                     (5.7)

The remaining cross-volume state is paid by

`||p_Q||inf <69976.953/L`,                                                (5.8)

or has a star `>zeta_2`, or a double-nested packet of mass

`>5.30853867531e-22 L^6`, sixth-root scale `>0.000284552560327 L`.       (5.9)

The constants are intentionally explicit rather than cosmetically optimized. The conceptual change is the structural survivor: every no-star third-volume branch now has two fixed physical row anchors and two fixed physical column anchors carrying a positive dimension-free fraction of its entire third exterior energy.

## 6. Required e5f result applied to an actual target family

The large-star alternative is not itself evidence of failure. The required e5f source proves a mixed-Fresnel hub theorem. Here is a direct exact-target application.

Let `g,r` be orthogonal coefficient vectors on a leaf bank, with

`||g||_2=G>=1`, `||r||_2=1`, and `r_j^2+(g_j/G)^2<=1/2` for every leaf.    (6.1)

For `|lambda|>=1`, consider

`Q=2 X_0 <g,X_L> + lambda <r,X_L>^2`.                                    (6.2)

Its symmetric matrix has nonzero spectrum

`{+G,-G,lambda}`,                                                         (6.3)

so it is an exact instance of the target. The e5f mixed-hub/Fresnel theorem applies with one physical hub and one Fresnel square. The leaf feature Gram matrix is `diag(1,G^2)` after ordering the square/star features, and (6.1) is exactly its normalized leverage gate. Therefore

`|phi_Q(t)| <= 4 pi^(3/2) |lambda|^(-1/2) G^(-1) |t|^(-3/2)`,             (6.4)

hence

`boxed:
 ||p_Q||inf <= 3*4^(2/3) |lambda|^(-1/3) G^(-2/3)
              <= 7.559526300.
`                                                                         (6.5)

This is a real application of the owner-required source to the present hybrid geometry: a physical star plus a compatible diffuse child square is already paid without any moment or support assumptions. Thus the unpaid STAR case in Theorem 4.1 must involve incompatibility with such a diffuse child feature, or additional arbitrary curvature that destroys this simple low-rank compression.

## 7. Source-valid stress family: double-nested volume does not imply one local minor

The new double-nested packet must remain aggregated. For each integer `m>=1`, define `(m+2)x3` Parseval frames `U,V` by

`u_1=e1`, `u_2=e2`, `u_ell=e3/sqrt(m)` for `ell>=3`,
`v_1=e1`, `v_2=e3`, `v_c=e2/sqrt(m)` for `c>=3`.                          (7.1)

Then `U^T U=V^T V=I_3`. Put

`M_m=U V^T`,
`A_m=[[0,M_m],[M_m^T,0]]`.                                                (7.2)

The three nonzero singular values of `M_m` are all one, hence `A_m` has six nonzero eigenvalues, three `+1` and three `-1`. It is a valid target matrix.

Fix rows `1,2` and columns `1,2`. The anchor `2x2` block is

`[[1,0],[0,0]]`, so its determinant is exactly zero.                       (7.3)

For every residual row `ell` and residual column `c`, because `M_m[S,T]=U_S V_T^T` on a `3x3` selection,

`det M_m[{1,2,ell},{1,2,c}] = -1/m`.                                     (7.4)

There are `m^2` such minors, so

`sum_(ell,c) det^2 =1`, while `max_(ell,c)|det|=1/m ->0`.                 (7.5)

Therefore even a unit double-nested packet does NOT force a dimension-free single `3x3` minor, and does NOT force the fixed `2x2` anchor pair to be invertible. Any next step that replaces (4.3) by one local reciprocal determinant is false.

This family is not a QFORM counterexample. In physical coordinates

`Q_m=2X_1Y_1 + 2X_2(m^-1/2 sum_{c>=3}Y_c)
     +2(m^-1/2 sum_{ell>=3}X_ell)Y_2`,                                  (7.6)

and the three displayed blocks use disjoint original coordinates. The normalized sums have one-dimensional density at most `sqrt(2)`. Applying the e5f independent-block `L^3` proposition to the three blocks (rescaling the two projected factors by their density cap) gives

`||p_Q||inf <= (1/(2pi))[6pi * (6pi sqrt(2))^2]^(1/3)
             =3*2^(1/3)
             =3.7797631497...`.                                         (7.7)

Thus (7.1)-(7.7) is a source-valid obstruction to a *mechanism*, not to the conjecture: the correct receiver must keep the determinant packet or exploit grouped stars/independent blocks.

## 8. Remaining implication

The first unpaid B08 implication is now

`QFORM-DIFFUSE-DOUBLE-NESTED-OR-STAR-PAYMENT-v1`:

starting from the actual spectral gate, pay either (a) a large physical star that is not already covered by the mixed-Fresnel hub geometry, or (b) the fixed two-row/two-column double-nested packet (4.3), while retaining arbitrary same-bank quadratic curvature, full complementary spectrum and original-coordinate product provenance. The stress family proves that one-good-minor or invertible-anchor-pair extraction cannot be the general receiver. The genuine rank-one/rank-two cross tubes in the `k=1,2` child branches remain parallel unpaid states.

The next plausible aggregate object is the two-anchor compound law itself: mix its order-three packet with a compatible residual order-two law under Theorem 2.1, or route failure of that compatibility to a grouped-star/low-rank compression theorem. This changes the missing step from two unrelated one-sided nested packets to one simultaneous physical four-anchor state.

## 9. Checks and review status

`CHECKS.py` and actual output `CHECKS.txt` beside this report verify the mixed-Jensen constants, all three actual-gate scales, the Parseval/spectrum/minor identities in the stress family, and the explicit mixed-Fresnel target family. The output ends

`QFORM_B08_R22_CHECK_PASS`.

These are finite checks, not independent proof review. The new theorem is a source-pinned supporting argument supplied in this run; independent review is pending. Full QFORM and global continuity remain OPEN.
