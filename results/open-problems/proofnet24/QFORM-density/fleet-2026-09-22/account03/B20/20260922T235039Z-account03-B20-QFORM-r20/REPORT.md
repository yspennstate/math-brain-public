SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-22T23:50:39Z.
attacking: the O0 two-anchor aggregate after exact Schur-compound compression, by removing the nonphysical cross-Schur bank in favor of quantitative original-coordinate compound/star resources.

# account03/B20 QFORM r20 — physical deshearing of the O0 double-anchor packet

Run: `20260922T235039Z-account03-B20-QFORM-r20`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: proof closure and keeper  
Classification: **ESSENTIAL_SUPPORTING_STEP / O0-PHYSICAL-DESHEAR / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Exact target and source frontier

The target is unchanged: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. Continuity is tracked separately.

No Gaussian, moment, log-concavity, compact-support, connected-support, iid, diagonal-basis, post-rotation-independence, or conditional-density-cap assumption is introduced. In particular, the argument below is deterministic matrix algebra on actual original-coordinate coefficient banks. It does not apply a density theorem to a Schur-transformed random vector.

The immediate input is account03/B20 r19,

`yspennstate/math-open-problems@21c78fcc8e4bd9f5c7a872ae3c034b03ca0f88bf`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T224748Z-account03-B20-QFORM-r19/REPORT.md`.

That run consumed account01/B20 r21's source-valid O0 certificate and produced physical row/column anchors with common third-minor mass

`Z_ia > 1/768`.                                                     (1.1)

After physical permutations, write the actual cross block

`B = [[b,r^T],[c,D]]`.                                               (1.2)

If `b!=0`, r19 defines only as a deterministic matrix

`S=D-c r^T/b`                                                       (1.3)

and proves the exact anchored compound identity

`Z_ia=b^2 E_2(S)>1/768`,                                            (1.4)

where

`E_2(M)=sum_{p<q} ||m_p wedge m_q||^2`

for the columns `m_p` of `M`. Thus

`|b| sqrt(E_2(S)) > delta`,  `delta:=1/sqrt(768)=1/(16 sqrt(3))`.    (1.5)

If `b=0`, r19 gave the safe but non-sharp estimate

`Z_ia<=||c||^2 ||r||^2 ||D||_F^2`.

The purpose of this run is to eliminate the nonphysical bank `S` from the first unpaid interface and sharpen the zero-edge branch exactly.

## 2. Main theorem — physical deshearing of the second compound

### Theorem `QFORM-O0-PHYSICAL-DESHEAR-v1`

Let `B` have the block form (1.2).

### (A) Exact zero-anchor identity

If `b=0`, then

`boxed(
 Z_ia = ||c||_2^2 ||r||_2^2 ||P_(c^perp) D P_(r^perp)||_F^2.
)`                                                                  (2.1)

Here `P_(c^perp)` and `P_(r^perp)` are the orthogonal projections perpendicular to `c` and `r`; if either vector is zero, the right side is interpreted as zero. Consequently (1.1) forces `c,r!=0` and

`boxed(
 ||c||_2 ||r||_2 ||P_(c^perp) D P_(r^perp)||_F > delta.
)`                                                                  (2.2)

This is strictly stronger than the previous total-Frobenius estimate: the residual bank must survive after removing **both** star directions.

### (B) Nonzero-anchor deshear inequality

If `b!=0`, put `h=r/b` and `S=D-c h^T`. Then

`boxed(
 sqrt(E_2(S))
 <= sqrt(E_2(D))
  + ||c||_2 sqrt(||h||_2^2||D||_F^2-||D h||_2^2).
)`                                                                  (2.3)

Equivalently,

`boxed(
 |b| sqrt(E_2(S))
 <= |b| sqrt(E_2(D))
  + ||c||_2 ||r||_2 ||D P_(r^perp)||_F.
)`                                                                  (2.4)

Applying the same identity to `S^T=D^T-h c^T` gives the transpose companion

`boxed(
 |b| sqrt(E_2(S))
 <= |b| sqrt(E_2(D))
  + ||c||_2 ||r||_2 ||P_(c^perp)D||_F.
)`                                                                  (2.5)

Combining (1.5), (2.4), and (2.5), every unpaid nonzero-anchor O0 packet obeys the exhaustive quantitative alternative

`P2:`

`boxed( |b| sqrt(E_2(D)) > delta/2 = 1/(32 sqrt(3)). )`              (2.6)

or, if (2.6) fails, **both** transverse physical-star reserves hold:

`boxed(
 ||c|| ||r|| ||D P_(r^perp)||_F > delta/2,
 ||c|| ||r|| ||P_(c^perp)D||_F > delta/2.
)`                                                                  (2.7)

All matrices/vectors in (2.1)--(2.7) are coefficients of the original physical cross block. The projectors are used only to state deterministic Euclidean energies; no projected random coordinates are declared independent.

## 3. Proof

### 3.1 Exterior-square notation

Let `d_p` denote the columns of `D`. Then

`E_2(D)=sum_(p<q) ||d_p wedge d_q||_2^2`.                            (3.1)

For `S=D-c h^T`, the columns are `s_p=d_p-h_p c`, hence

`s_p wedge s_q
 =d_p wedge d_q + c wedge (h_q d_p-h_p d_q)`.                       (3.2)

View the arrays indexed by `p<q` as one Hilbert space. Minkowski gives

`sqrt(E_2(S))
 <= sqrt(E_2(D))
   +[sum_(p<q)||c wedge(h_qd_p-h_pd_q)||^2]^(1/2).`                 (3.3)

Since `||c wedge v||<=||c||||v||`,

`second term <= ||c|| [sum_(p<q)||h_qd_p-h_pd_q||^2]^(1/2).`        (3.4)

The vector-valued Lagrange identity is

`sum_(p<q)||h_qd_p-h_pd_q||^2
 =||h||^2||D||_F^2-||D h||^2`.                                      (3.5)

Equations (3.3)--(3.5) prove (2.3). Because

`||h||^2||D||_F^2-||D h||^2
 =||h||^2 ||D P_(h^perp)||_F^2`,                                   (3.6)

and `h` is parallel to `r`, multiplying by `|b|` proves (2.4). Applying the same argument to the transpose proves (2.5). The dichotomy (2.6)--(2.7) is immediate from the strict lower bound (1.5).

### 3.2 Exact zero-edge identity

Assume `b=0`. Let `L_c:x->c wedge x` and `L_r:y->r wedge y`. The complete anchor-containing third-minor array is exactly the coefficient array of

`L_c D L_r^*`.                                                      (3.7)

Therefore

`Z_ia=||L_c D L_r^*||_HS^2`.                                       (3.8)

The elementary exterior identities are

`L_c^*L_c=||c||^2 P_(c^perp)`,
`L_r^*L_r=||r||^2 P_(r^perp)`.                                      (3.9)

Cyclicity of trace gives

`||L_c D L_r^*||_HS^2`
` =||c||^2||r||^2
   Tr(P_(r^perp) D^T P_(c^perp) D P_(r^perp))`
` =||c||^2||r||^2||P_(c^perp) D P_(r^perp)||_F^2`.                 (3.10)

This proves the exact identity (2.1), and (2.2) follows from (1.1).

## 4. A fully physical disjoint-bank consequence of `P2`

The physical second compound in (2.6) can be split without selecting one small minor. Independently two-color the residual physical rows and columns of `D`. Every squared `2x2` minor has probability `1/4` that its two rows and its two columns are each separated. Therefore there exist deterministic physical bipartitions

`L'=L_1 disjoint_union L_2`, `R'=R_1 disjoint_union R_2`

such that

`M_sep := sum_(j in L1,k in L2,p in R1,q in R2)
             det D[{j,k},{p,q}]^2
        >= E_2(D)/4`.                                               (4.1)

Put `F_pq=||D[L_p,R_q]||_F^2`. For each separated minor,

`det[[x,y],[z,w]]^2 <=2(x^2w^2+y^2z^2)`.

Summing gives

`M_sep <=2(F_11 F_22+F_12 F_21)`.                                  (4.2)

Hence

`max{F_11F_22,F_12F_21}>=E_2(D)/16`,                               (4.3)

or equivalently

`max{
 ||D[L1,R1]||_F ||D[L2,R2]||_F,
 ||D[L1,R2]||_F ||D[L2,R1]||_F
 } >= sqrt(E_2(D))/4`.                                              (4.4)

On branch `P2`, this yields the source-physical three-resource packet

`boxed(
 |b| max_matching
   ||D[bank1]||_F ||D[bank2]||_F
 > delta/8 = 1/(128 sqrt(3)).
)`                                                                  (4.5)

The anchor row/column and the four residual banks are genuine disjoint original-coordinate blocks. Equation (4.5) is an aggregate bank certificate, not a claim that one individual minor is large.

## 5. A physical exterior-energy consequence of the star branch

The first reserve in (2.7) can be written without projectors:

`||r||^2 ||D P_(r^perp)||_F^2
 =sum_(p<q)||r_p d_q-r_q d_p||^2`.                                  (5.1)

Thus the star branch gives

`||c||^2 sum_(p<q)||r_p d_q-r_qd_p||^2 > delta^2/4`.                (5.2)

A random two-coloring of the residual physical columns separates each pair with probability `1/2`; hence some physical column bipartition `R'=R_1 disjoint_union R_2` satisfies

`boxed(
 ||c||^2 sum_(p in R1,q in R2)||r_p d_q-r_qd_p||^2
 > delta^2/8 = 1/6144.
)`                                                                  (5.3)

The transpose companion supplies a physical row bipartition with the analogous bound

`boxed(
 ||r||^2 sum_(j in L1,k in L2)||c_j D_(k,*)-c_k D_(j,*)||^2
 >1/6144.
)`                                                                  (5.4)

These are exterior-star bank certificates in original coordinates. They retain the cancellation geometry that was lost in the coarse r19 bound `||c||||r||||D||_F>delta/2`.

## 6. Designated partner account04/B20 applied at its exact downstream scope

The newest completed designated partner remains account04/B20 r3,

`yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`,

theorem `QFORM-CROSS-DOMINATED-SECOND-SCHUR-CLOSURE-v1`.

Its source-valid scope is an already-selected physical outer pivot `|a|>=tau>=1/4` and exact second-Schur row `(d,c_*)` with

`max{|d|,||c_*||}>tau/9`.

On the cross-dominated side `||c_*||>|d|`, the same actual inequality immediately gives

`||c_*||>tau/9`,

so the partner theorem applies and yields

`boxed( ||p_Q||_infinity <5262. )`                                  (6.1)

The complementary diagonal-dominated side is already paid in the same source-valid reduction. Therefore the physical packets (4.5)/(5.3)/(5.4) should not be routed back into that already-closed localized state: any such localization exits immediately through (6.1) or its diagonal companion. No partner hypothesis is extended to the upstream O0 banks themselves.

## 7. What this changes and the next unpaid implication

The key correction-safe gain is that the first O0 interface no longer needs the nonphysical rectangular Schur bank `S` as a probabilistic object.

Every unpaid two-anchor O0 state now has one of the following **original-coordinate** certificates:

1. `b=0`: the exact doubly-transverse identity (2.1), with product lower bound (2.2);
2. `b!=0`, physical second-compound branch: (2.6), and therefore the disjoint physical edge-plus-two-bank packet (4.5);
3. `b!=0`, shear-created branch: both one-sided transverse star reserves (2.7), hence the physical exterior-star packets (5.3) and (5.4).

This cleanly separates genuine physical second-compound mass from second-compound mass manufactured by the rank-one shear. In particular it prevents a future proof from applying an independence-sensitive density theorem directly to `S`.

The first unpaid synthesis implication is now

`QFORM-O0-PHYSICAL-PACKET-PAYMENT-v1`:

pay either the edge-plus-two-disjoint-bank packet (4.5) or the doubly/one-sided transverse star packets (2.2), (5.3), (5.4), while retaining arbitrary same-side quadratic blocks and all additional spectrum. A promising compatible mechanism is the existing weighted Schur-flag/product-projection machinery, but any use of the projectors in (2.1)/(2.7) must be through joint marginal-density bounds, not fictitious independence of projected coordinates.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This run proves a structural theorem and no new full-target continuity statement.
