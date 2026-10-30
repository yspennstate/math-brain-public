SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T00:41:11Z.
attacking: finite-bank overlap receiver and no-pivot residual-bank packet — replace the crude overlapping star-star-core product by a genuinely disjoint four-bank packet using exact anchored-minor deshearing.

# fleet03/B07 QFORM r21 — transverse physical deshearing and a disjoint four-bank replacement for the P packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Run:** `20260923T004111Z-fleet03-B07-qform-r21`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL PACKET / FULL TARGET OPEN`.

## 1. Target and correction boundary

The exact target remains unrestricted: independent real original coordinates with marginal probability densities bounded by one, and a real symmetric matrix `A` with at least three eigenvalues of modulus at least one. The goal is one universal finite essential density bound for `Q=X^TAX`, or a valid target counterexample. The stronger continuous-density request is tracked separately.

No Gaussian, moment, compact-support, connected-support, log-concavity, iid, diagonal-basis, or post-rotation independence hypothesis is used. This run does not use the refuted law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea cap, a worst conditional projection-density bound, or a one-good-minor selector. A small nonzero coefficient is never replaced by zero.

The designated `fleet04/B07` current-QFORM handoff/canonical directory was checked again and was still absent, so no result is fabricated or attributed to it. A compatible completed `fleet04/B18` projection/rearrangement theorem is applied quantitatively in Section 7.

## 2. Source-pinned incoming packet

The fresh physical deshearing input is fleet02/B20 r22,

`yspennstate/math-open-problems@1c1f83fe62149caa8b755ac8d39923214c8b6c39`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260922T233033Z-fleet02-B20-QFORM-r22/REPORT.md`.

Inside the O0 third-compound branch, after a physical row anchor `i` and physical column anchor `a` are selected, the actual cross block has the form

`B = [[b, r^T], [c, D]]`                                                    (2.1)

and the anchored third-minor mass satisfies

`Z := sum_{|J|=|K|=2} det B[{i} union J,{a} union K]^2 > 1/768.`             (2.2)

Here `J` ranges over residual physical row pairs and `K` over residual physical column pairs. The same source proved the coarse inequality

`sqrt(Z) <= |b| sqrt(E_2(D)) + ||c|| ||r|| ||D||_F`,                       (2.3)

which led to the still-unpaid packet

`P: ||c|| ||r|| ||D||_F > 1/(32 sqrt(3))`                                  (2.4)

or the residual second-compound packet `E_2(D)>1/48` (with the high-`E_5` branch already paid).

The current no-pivot reduction uses `tau=1/128`. Fleet01/B09 r19 proves there that

`|b|<1/8`                                                                  (2.5)

for every physical off-diagonal coefficient. The purpose of this run is to sharpen (2.3): when the `E_2(D)` branch does not fire, the mass in (2.4) is not allowed to hide in overlap with the star directions. It must produce a packet on four genuinely disjoint original-coordinate banks.

## 3. Exact anchored-minor tensor identity

Write residual row indices as `j,k` and residual column indices as `p,q`. Define

`C_2(D)_{jk,pq}=D_jp D_kq-D_jq D_kp`                                      (3.1)

and

`G_{jk,pq}
 =-r_p(c_j D_kq-c_k D_jq)
  +r_q(c_j D_kp-c_k D_jp).`                                                (3.2)

Direct expansion of the actual physical `3x3` minor gives

`det B[{i,j,k},{a,p,q}] = b C_2(D)_{jk,pq} + G_{jk,pq}.`                    (3.3)

Thus, if `T` denotes the matrix of anchored `3x3` minors,

`T = b C_2(D) - L_c D iota_r`                                             (3.4)

with the standard exterior convention `iota_r(e_p wedge e_q)=r_p e_q-r_q e_p` and `L_c(w)=c wedge w`; in these conventions `G=-L_cD iota_r`.

The crucial point is that the second term has an exact **transverse** norm, not merely the coarse upper bound in (2.3).

### Theorem 3.1 — `QFORM-ANCHORED-TRANSVERSE-DESHEAR-v1`

Let `C=||c||_2`, `R=||r||_2`. If `C,R>0`, let

`P_c^perp=I-cc^T/C^2`, `P_r^perp=I-rr^T/R^2`.

Then

`boxed:
 ||L_c D iota_r||_HS^2
 = C^2 R^2 ||P_c^perp D P_r^perp||_F^2.
`                                                                               (3.5)

Equivalently,

`boxed:
 sum_{j<k,p<q} G_{jk,pq}^2
 = C^2R^2||D||_F^2
   -C^2||Dr||_2^2
   -R^2||D^T c||_2^2
   +(c^TDr)^2.
`                                                                               (3.6)

If `c=0` or `r=0`, both sides of (3.5) are zero by convention.

#### Proof

The adjoint identities on exterior powers are

`iota_r iota_r^* = R^2 I-r r^T`,
`L_c^* L_c = C^2 I-c c^T`.                                                       (3.7)

Therefore

`||L_c D iota_r||_HS^2
 =tr[(C^2I-cc^T)D(R^2I-rr^T)D^T]`.                                              (3.8)

Expanding the trace gives (3.6). Factoring out `C^2R^2` gives (3.5). QED.

### Meaning

The old product `CR||D||_F` can be large merely because `D` is aligned with one of the two star directions. Equation (3.5) shows that the part which actually creates the anchored determinant tensor is instead

`CR ||P_c^perp D P_r^perp||_F`.                                                  (3.9)

Thus the difficult packet carries a third direction simultaneously transverse to both stars. This is a strictly stronger structural statement than the coarse packet P.

## 4. No-pivot consequence: either residual E2 or a transverse reserve

By the reverse triangle inequality applied to (3.4),

`||L_cD iota_r||_HS >= sqrt(Z)-|b|sqrt(E_2(D)).`                              (4.1)

Assume the no-pivot bound (2.5) and suppose the residual `E_2` packet does **not** fire:

`E_2(D) <= 1/48.`                                                             (4.2)

Since

`sqrt(Z)>1/sqrt(768)=1/(16sqrt(3))`

and

`|b|sqrt(E_2(D)) < (1/8)(1/sqrt(48))=1/(32sqrt(3)),`                          (4.3)

we obtain

`boxed:
 ||L_cD iota_r||_HS > 1/(32sqrt(3)),
`                                                                                 (4.4)

hence

`boxed:
 C^2R^2||P_c^perp D P_r^perp||_F^2 > 1/3072.
`                                                                                 (4.5)

This is already a dimension-free replacement for the old `P` branch: the core norm is forced **after removing both star directions**.

## 5. Random physical coloring turns the transverse reserve into four disjoint banks

Independently two-color every residual row and every residual column. Write the row partition as

`L_0 disjoint_union L_1`

and the column partition as

`R_0 disjoint_union R_1`.

For a fixed coloring define the split transverse packet

`G_split
 = sum_{j in L_0,k in L_1,p in R_0,q in R_1} G_{jk,pq}^2.`                   (5.1)

Every unordered residual row pair is split with probability `1/2`; independently every unordered residual column pair is split with probability `1/2`. Therefore

`E G_split = (1/4)||L_cD iota_r||_HS^2.`                                     (5.2)

Together with (4.4)-(4.5), some deterministic physical coloring satisfies

`boxed: G_split > 1/12288.`                                                   (5.3)

No spectral or input-coordinate rotation is used: `L_0,L_1,R_0,R_1` are literal disjoint sets of original coordinates.

Now expand (3.2) on the split packet as four tensors:

`G=A_1+A_2+A_3+A_4`,                                                         (5.4)

where their squared `ell_2` norms factor exactly as

`||A_1||_2^2 = ||c_{L_0}||^2 ||r_{R_0}||^2 ||D[L_1,R_1]||_F^2`,
`||A_2||_2^2 = ||c_{L_1}||^2 ||r_{R_0}||^2 ||D[L_0,R_1]||_F^2`,
`||A_3||_2^2 = ||c_{L_0}||^2 ||r_{R_1}||^2 ||D[L_1,R_0]||_F^2`,
`||A_4||_2^2 = ||c_{L_1}||^2 ||r_{R_1}||^2 ||D[L_0,R_0]||_F^2`.             (5.5)

Since `||G||_2 <= sum_s ||A_s||_2`, at least one of the four terms has squared norm greater than `G_split/16`. Thus:

### Theorem 5.1 — `QFORM-O0-DISJOINT-STAR-STAR-CORE-v1`

Under (2.2), the no-pivot bound `|b|<1/8`, and `E_2(D)<=1/48`, there are physical two-colorings and `epsilon,eta in {0,1}` such that

`boxed:
 ||c_{L_epsilon}||_2^2
 ||r_{R_eta}||_2^2
 ||D[L_{1-epsilon},R_{1-eta}]||_F^2
 > 1/196608
 =1/(3*2^16).
`                                                                               (5.6)

Equivalently,

`boxed:
 ||c_{L_epsilon}||
 ||r_{R_eta}||
 ||D[L_{1-epsilon},R_{1-eta}]||_F
 >1/(256sqrt(3)).
`                                                                               (5.7)

The three factors live on **four mutually disjoint original-coordinate banks**: the two star pieces use `L_epsilon` and `R_eta`, while the core block uses their complementary row and column banks. The outer row/column anchors `i,a` are disjoint from all four.

This is the main new structural result of the run.

## 6. Consequence for the current N3 O0 packet

Fleet02/B20 r22 left, after its D5-paid branch, the three physical possibilities

`H: |b|>1/8`,
`P: ||c||||r||||D||_F>1/(32sqrt(3))`,
`R: E_2(D)>1/48 and E_5(D)<1/1024`.                                         (6.1)

Inside the sufficient no-pivot class `N3(1/128)`, fleet01/B09 r19 makes `H` impossible. Theorems 3.1 and 5.1 now sharpen the remaining bookkeeping:

* if `E_2(D)>1/48`, retain `R` exactly;
* otherwise the anchored determinant mass forces the disjoint four-bank packet (5.6)-(5.7).

Hence the overlapping packet `P` need no longer be the first receiver datum. It can be replaced by

`T4: there exist four disjoint original-coordinate banks with
     ||c_L|| ||r_R|| ||D[L',R']||_F >1/(256sqrt(3)).`                      (6.2)

The inherited `E_5(D)<1/1024` remains available on every still-unpaid state after D5 has been removed.

This is a strict structural gain: in `P`, the stars and the core can reuse the same physical coordinates, while `T4` explicitly separates the star supports from the core supports before any reciprocal analytic estimate is attempted.

The latest reviewed fleet01/B20 trichotomy can still be applied unchanged to the sibling `R` branch: small `E_3(D)` gives the rank-two tube `dist_F(D,rank<=2)<3/128`; a diffuse third-volume branch is paid by reviewed D'; otherwise it yields a nested anchored packet. The new `T4` branch is a different, product-provenance-friendly endpoint for what used to be the coarse `P` branch.

## 7. Completed fleet04 result applied to an actual inequality

The designated `fleet04/B07` has no completed current-QFORM artifact, so none is invented. I use the compatible completed fleet04/B18 sharp projection/rearrangement input, canonical source

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

Its sharp one-dimensional product-projection consequence, already used source-validly in B07 r19, is

`||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`                              (7.1)

for an original-coordinate coefficient bank `u`.

Take the actual `T4` term in (5.7) and abbreviate

`C_*=||c_{L_epsilon}||`,
`R_*=||r_{R_eta}||`,
`F_*=||D[L_{1-epsilon},R_{1-eta}]||_F`.

Then

`C_* R_* F_* >1/(256sqrt(3)).`                                            (7.2)

The two star banks are disjoint, so the corresponding scalar projections are genuinely independent. Applying (7.1) to both gives the actual joint-density inequality

`boxed:
 ||p_(c_L^T X_L, r_R^T X_R)||_infinity
 <= 2/(C_*R_*)
 < 512sqrt(3) F_*.
`                                                                            (7.3)

This is not promoted to a generic indefinite quadratic receiver: the live correction says that a bounded projected joint density alone is insufficient. It is useful only when the quadratic geometry supplies the proper anchor interface.

For example, on the already proved B07 r19 **exact zero two-anchor block** endpoint, arbitrary outside quadratic curvature is permitted and the coefficient-plane theorem gives

`||p_Q||_infinity <=2 sqrt(K)`                                             (7.4)

when the two star coefficient forms have joint cap `K`. If in addition `F_*<=1`, (7.3) gives `K<512sqrt(3)`, hence the complete continuous-density bound

`boxed:
 ||p_Q||_infinity < 2 sqrt(512sqrt(3))
                   =59.5587109825... .
`                                                                            (7.5)

Likewise, still under `F_*<=1`, (7.2) implies

`max(C_*,R_*) > 1/(16*3^(1/4)).`                                          (7.6)

If the corresponding physical anchor has an **exact zero** diagonal, the completed fleet04/B18/B07-r19 zero-pivot half-Riesz splice gives

`boxed:
 H_(1/2) < 2^(19/4) 3^(1/8)
          =30.8697161588... .
`                                                                            (7.7)

These are genuine equation-level uses of the completed fleet04 mathematics. They are deliberately scoped; neither (7.3) nor a tiny nonzero pivot is silently treated as an exact-zero theorem.

## 8. Exact checks

`CHECKS.py` in this run directory performs integer-arithmetic verification of:

1. the coordinate expansion (3.3) on multiple random integer matrices;
2. the exact transverse norm identity (3.6);
3. the constants
   `1/768 -> 1/3072 -> 1/12288 -> 1/196608`;
4. `1/sqrt(196608)=1/(256sqrt(3))`;
5. the numerical constants in (7.5)-(7.7).

The recorded output ends `STATUS=PASS`. The computation checks identities/constants only; the analytic proof is the argument above.

## 9. First unpaid implication

The first new receiver is

`QFORM-N3-DISJOINT-STAR-STAR-CORE-PAYMENT-v1`:

starting from the exact `T4` packet (5.7), preserve its four disjoint original-coordinate banks and prove a dimension-free density/half-Riesz payment while retaining arbitrary remaining same-side curvature and the small-but-nonzero outer two-anchor block; or force one of the already-paid exact-zero, physical-pair, two-pivot, ridge, D'/volume, grouped-square, or hyperbolic-convolution exits.

A natural next split is now source-valid: if the complementary core block has controlled Frobenius norm, (7.3) makes the two star coefficient forms quantitatively spread; if its Frobenius norm is large, spend that **disjoint** core bank before touching the stars. This is materially stronger than the prior overlapping `P` datum.

The sibling `R` branch remains under `QFORM-R22-RANK2-OR-NESTED-ANCHOR-PAYMENT-v1` from fleet01/B20.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full continuity remains OPEN.** Continuity is proved only on scoped paid endpoints such as (7.5), not on `T4` in general.
