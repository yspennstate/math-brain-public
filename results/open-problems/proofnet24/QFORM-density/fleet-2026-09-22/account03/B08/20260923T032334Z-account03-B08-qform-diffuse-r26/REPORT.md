SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T03:23:34Z.
attacking: join the diffuse third-volume exit to high-volume-leverage / low-cross-rank survivors quantitatively, retaining the actual full matrix and original-coordinate product structure.

# account03/B08 QFORM r26 — third-volume leverage failure forces an anchored hub or a four-bank low-tail/bicore packet

**Run:** `20260923T032334Z-account03-B08-qform-diffuse-r26`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `NEW TARGET-RELEVANT ROUTING THEOREMS + PAID CONTINUOUS BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction discipline

The target remains unrestricted: independent real ORIGINAL coordinates with one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No Gaussian, moment, compact-support, connected-support, iid, log-concavity, spectral-coordinate independence, pointwise law-uniform Fresnel decay, arbitrary-joint rank-three coarea bound, conditional projection-height moment, one-good-minor principle, or small-random-quadratic-error argument is used.

This run applies the newest required fractional-volume theorem rather than merely citing it. The immutable source is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an ORIGINAL-coordinate cross block `B`, put

`Delta_3(B)=e_3(BB^T)=sum_{|S|=|T|=3} det B[S,T]^2`.

Let `alpha_i` be the row inclusion marginals of the normalized squared-minor law. The source proves that if `1<=q<3/2` and every `alpha_i<=q/2`, then the full ambient quadratic-plus-affine form has a continuous `C_0` density with

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Delta_3(B)^(-1/6)`.      (1.1)

All same-side quadratic terms and outside couplings remain present. By transposing the cross block, the same statement holds if the corresponding column marginals obey the gate.

The immediate B08 predecessor is r25,

`yspennstate/math-open-problems@d30dba6db19d1eceabde6222c84a5b57a85506f0`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T002108Z-account03-B08-qform-diffuse-r25/REPORT.md`.

It proved a one-shot Pluecker transfer for three selected eigenvectors with `|lambda_j|>=L` and maximum selected-frame row leverage at most `1/48`. In its disjoint `q=0` branch there is an actual original-coordinate cross block `B=A[I,J]` satisfying

`Delta_3(B) >= L^6/2304`.                                      (1.2)

The issue left by r25 was how to handle failure of the volume/range diffuseness gate without selecting a single bad minor. This report closes that routing implication.

## 2. The normalized third-volume law

Assume `Delta_3(B)>0`. Give every row triple `S` and column triple `T` probability

`w_{S,T}=det B[S,T]^2 / Delta_3(B)`.                            (2.1)

Define

`alpha_i=P_w(i in S)`,  `beta_j=P_w(j in T)`.                  (2.2)

Then `sum_i alpha_i=sum_j beta_j=3` and `0<=alpha_i,beta_j<=1`.

The important point is that (2.1) aggregates the entire third-minor bank BEFORE any localization or reciprocal payment. This is consistent with the live correction that local collision / one-minor selection can lose a positive power of bank size.

## 3. New leverage-failure lemma: a double-incident anchored third-volume bank

### Lemma 3.1 — `QFORM-VOLUME-BILEVERAGE-ANCHOR-v1`

Fix `1<q<3/2`. Then either

1. one physical side satisfies the fractional-volume gate and (1.1) applies; or
2. there are an original row `i` and original column `j` such that

`Z_ij := sum_{S contains i, T contains j} det B[S,T]^2
       > (q-1) Delta_3(B)`.                                  (3.1)

#### Proof

If all row marginals are at most `q/2`, apply (1.1). If all column marginals are at most `q/2`, transpose `B` and apply (1.1). Otherwise choose `i,j` with

`alpha_i>q/2`, `beta_j>q/2`.

Under the probability law `w`, the union bound gives

`P(i in S and j in T)
 >= alpha_i+beta_j-1
 > q-1`.                                                       (3.2)

Multiplying (3.2) by `Delta_3(B)` gives (3.1). QED.

This is the key new replacement for r25's unresolved leverage failure: failure on BOTH sides creates quantitative third-volume mass incident to one physical row AND one physical column.

## 4. Exact deshearing of the anchored bank

Write the actual cross block around the two anchors as

`B = [[b, r^T], [c, D]]`.                                     (4.1)

The exact physical-coordinate exterior identity proved in account03/B07 r21,

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T004111Z-account03-B07-qform-r21/REPORT.md`,

is

`T = b C_2(D) - L_c D iota_r`,                                (4.2)

where `T` is precisely the tensor of `3x3` minors incident to the anchor row/column. Hence

`||T||_HS^2=Z_ij`,
`||C_2(D)||_HS^2=E_2(D)`,                                    (4.3)

and the transverse term has the exact norm

`G:=||L_cD iota_r||_HS
  =||c|| ||r|| ||P_c^perp D P_r^perp||_F`.                    (4.4)

The triangle inequality in (4.2) gives

`sqrt(Z_ij) <= |b| sqrt(E_2(D)) + G`.                          (4.5)

Therefore at least one of

`|b| sqrt(E_2(D)) > (1/2)sqrt((q-1)Delta_3(B))`,              (4.6)

or

`G > (1/2)sqrt((q-1)Delta_3(B))`                              (4.7)

holds.

No physical pair determinant is inverted. Alternative (4.6) is kept as an aggregate anchored-bilinear-times-second-volume resource.

## 5. Transverse branch -> four disjoint original-coordinate banks

In alternative (4.7), independently two-color the residual physical rows and columns. The B07 r21 calculation gives a coloring for which the split transverse tensor has squared norm at least `G^2/4`. Expanding that split tensor into its four star-star-core pieces and using the triangle inequality, one piece has norm at least `G/8`. Thus there are four mutually disjoint original-coordinate banks with

`C R F
 := ||c_L|| ||r_R|| ||D[L',R']||_F
 > G/8
 > (1/16)sqrt((q-1)Delta_3(B))`.                              (5.1)

The two anchor coordinates are outside all four banks. This is a product-provenance statement, not a spectral-coordinate statement.

Combining Sections 3-5 gives:

### Theorem 5.1 — `QFORM-THIRD-VOLUME-TO-HUB-OR-T4-v1`

For every actual original-coordinate cross block `B` with `Delta_3(B)>0` and every `1<q<3/2`, one of the following holds:

**A. Fractional-volume exit.** The full ambient quadratic form has a continuous density obeying (1.1).

**B. Anchored second-volume hub.** There exist physical anchors such that

`|b| sqrt(E_2(D)) > (1/2)sqrt((q-1)Delta_3(B))`.              (5.2)

**C. Disjoint four-bank packet.** Four mutually disjoint original-coordinate banks satisfy

`C R F > (1/16)sqrt((q-1)Delta_3(B))`.                        (5.3)

The theorem retains every other entry and every other spectral direction of the ambient matrix.

## 6. Explicit diffuse q=0 corollary: the old leverage gate disappears

Now apply Theorem 5.1 to the r25 diffuse `q=0` packet (1.2), taking

`q=4/3`.                                                       (6.1)

The fractional-volume constant is

`[3e/((3-2q)sqrt(q))] 2304^(1/6)
 =76.9983411472... <77`.                                      (6.2)

Thus the following exhaustive alternative holds.

### Corollary 6.1 — `QFORM-DIFFUSE-Q0-ROUTER-v1`

If the selected three-eigenvector frame has maximum row leverage `<=1/48` and r25 lands in its disjoint `q=0` packet, then at least one of:

**A. Paid continuous branch**

`||p_Q||_infinity <77/L`,                                    (6.3)

and `p_Q` has a continuous `C_0` representative;

**B. Anchored hub / residual-second-volume branch**

`|b| sqrt(E_2(D)) > L^3/(96sqrt(3))`;                        (6.4)

**C. Four-bank branch**

`C R F > L^3/(768sqrt(3))`.                                  (6.5)

Indeed `(q-1)Delta_3 >= L^6/6912`, whose square root is `L^3/(48sqrt(3))`; (6.4) and (6.5) follow from the factors `1/2` and `1/16` above.

This is stronger than r25's `range(B)` leverage gate. Even if `B` has full range projection and hence range leverage one, the third-volume law either pays analytically or forces one of the concrete physical packets (6.4)-(6.5).

## 7. The four-bank branch enters the existing low-tail/bicore compiler

The newest completed account03/B07 r22 source is

`yspennstate/math-open-problems@ac54330d3df42a48098ef7c704ac268382accd7c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T030701Z-account03-B07-qform-r22/REPORT.md`.

Its proof depends only on a four-bank product lower bound `CRF>kappa`, so repeating its algebra with

`kappa=L^3/(768sqrt(3))`                                      (7.1)

gives the following scaled statement. For any `Lambda>0` and `0<theta<=1/2`, either

1. `CR>Lambda`; or
2. the singular-value tail `T=sum_{nu>=3}s_nu(M)^2` of the core block satisfies `T<theta F^2`; or
3. the full ambient density is continuous and

`||p_Q||_infinity
 < (9sqrt(3)e/2)(6/theta^2)^(1/6) Lambda/kappa`;              (7.2)

or
4. there are matched left/right singular-core projections of rank `<225/theta`, with operator remainder at most `sqrt(T)/15`, and original physical row and column core norms each greater than

`sqrt(theta/450) kappa/Lambda`.                               (7.3)

For a concrete scale-compatible collar take

`Lambda=L^2`, `theta=1/16`.                                  (7.4)

Then alternative 2 is the genuine rank-two Frobenius tube

`dist_F(M,{rank<=2})=sqrt(T)<F/4`.                            (7.5)

Alternative 3 is completely paid with

`||p_Q||_infinity
 < 10368 e *1536^(1/6) / L
 =95731.45794099.../L
 <95732/L`,                                                   (7.6)

again with continuity. Alternative 4 has rank `<3600`, operator remainder `<=sqrt(T)/15`, and physical selected-core row/column norms each exceeding

`L/(46080sqrt(6))
 =8.8595549e-6 L`.                                           (7.7)

Thus the r25 diffuse `q=0` class has now been joined quantitatively to exactly the current B08 obligation: paid diffuse volume, or a physical hub/second-volume resource, or a large-star / rank-two-tube / bounded-rank two-sided-core survivor.

## 8. Completed account04 result applied at an actual inequality

The designated `account04/B08` current-QFORM handoff/canonical directory was checked fresh and remains absent, so no partner theorem is fabricated.

A compatible completed account04 theorem is account04/B18's sharp product-projection transfer, canonical report

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`,
with scientific source recorded in the shared proof graph at commit `ce50e74f705c49f66524aa6565d4aa4a9be88061`.

Its one-dimensional consequence for an original-coordinate coefficient bank `u` is

`||p_{u^T X}||_infinity <= sqrt(2)/||u||_2`.                  (8.1)

The two star banks in (6.5) are disjoint, so the star projections are genuinely independent. On the large-star alternative `CR>L^2` from Section 7, (8.1) gives the ACTUAL inequality

`||p_{(c_L^T X_L, r_R^T X_R)}||_infinity
 <= 2/(CR)
 < 2/L^2`.                                                    (8.2)

Equation (8.2) is deliberately recorded as a resource, not falsely promoted to a generic indefinite quadratic pushforward bound; the correction ledger forbids that shortcut. It is the product-linear input for the remaining hub/star receiver.

## 9. Checks

`CHECKS.py` and the actual captured `CHECKS.txt` are stored beside this report. They verify the exact q=4/3 arithmetic, the `77/L` paid constant, the anchored thresholds, the four-bank scale, the `theta=1/16` low-tail ratio/rank, the `95732/L` paid constant, and the physical-core row scale. Output begins `QFORM_B08_R26_CHECK_PASS`.

These finite calculations check constants only; the proofs are Sections 3-8.

## 10. What remains

The full QFORM conjecture remains **OPEN / not proved / not disproved**. The full continuous-density statement also remains open. Continuity is proved here only on the fractional-volume exit and the B07 diffuse-tail paid subbranch.

For B08, the first remaining implications are now sharply separated:

1. consume the anchored resource `|b|sqrt(E_2(D))>L^3/(96sqrt(3))` without replacing a small nonzero anchor by zero and without selecting one tiny residual minor;
2. pay the four-bank large-star branch using its original-coordinate product provenance plus a valid curved kernel (not just the joint cap (8.2));
3. pay the rank-two Frobenius tube or route the two-sided bounded-rank core into an already-valid finite-core/grouped-coordinate receiver;
4. separately consume r25's `q=1,q=2,q=3` overlap packets.

No assertion here closes those branches. The substantive gain is that the diffuse disjoint-third-volume branch no longer stops at a range-leverage failure: every such failure now produces explicit dimension-free physical currency that enters the existing low-rank/hub proof tree.
