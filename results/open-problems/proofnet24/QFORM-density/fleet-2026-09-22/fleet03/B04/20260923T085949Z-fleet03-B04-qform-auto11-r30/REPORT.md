SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T08:59:49Z.
attacking: convert the overlap-one third-compound mass into an original-coordinate scalar pivot plus aggregate residual pair-volume, before any local minor is inverted.

# Overlap-one third-compound compiler to pivot + pair-volume

Run: `20260923T085949Z-fleet03-B04-qform-auto11-r30`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: fleet03/B04, Product Fourier rearrangement  
Status: **SUPPORTING_THEOREM_PROVED / FULL QFORM OPEN**  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The full owner target is unchanged: for every finite `n`, independent real original-coordinate inputs with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite `L^infinity` bound for the density of `Q=X^TAX`, or give a valid counterexample. Continuity is an additional requested conclusion and is tracked separately.

This report uses no Gaussianity, moments, compact support, connected support, log-concavity, post-rotation independence, or law-uniform pointwise quadratic-phase decay. It also does not use the corrected-away unrestricted joint-coarea or positive conditional-projection-moment interfaces. Everything below is performed in original coordinates.

The previous B04 run converted the *disjoint* portion of the third compound into a rank-three physical cut. The present run attacks the next overlap layer: third-order minors whose physical row and column triples intersect in exactly one coordinate.

## 2. Completed peer theorem actually used

The analytic input is fleet01/B01 `QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1`, canonical source

`yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T030821Z-fleet01-B01-qform-auto11/REPORT.md`.

For an arbitrary quadratic polynomial `R` in independent cap-one original coordinates and any disjoint physical cross block `M` inside its coefficient matrix, put

`E2(M)=sum_{|P|=|Q|=2} det(M[P,Q])^2=e_2(M^TM)`.

The peer theorem proves

`sup_s E |R-s|^(-1/2) <= C_E2 E2(M)^(-1/8)`,

with

`C_E2 <= 12*2^(5/6)*e^(5/24)=26.3340461807597...`,

while retaining arbitrary self-quadratic curvature on both banks, arbitrary signs, outside couplings and affine terms. If an independent original-coordinate scalar square `a(Z+ell)^2` is peeled outside `R`, the standard square kernel gives

`||p_Q||_infinity <= C_E2 |a|^(-1/2) E2(M)^(-1/8)`.

This is an essential-boundedness statement; continuity is not asserted by that square-peel interface.

The designated partner `fleet04/B04` had no completed current-QFORM handoff or canonical report visible at startup, so no designated-partner result is fabricated here. The completed fleet01/B01 theorem above is the peer result actually applied at an inequality.

## 3. Overlap-one third-compound slice

Fix an original coordinate `i` with

`a_i:=A_ii != 0`.

Write `K=[n]\\{i}`, `v=A[K,i]`, and let

`S_i := A[K,K] - a_i^(-1) v v^T`                                  (3.1)

be the exact scalar Schur residual. Completing only the physical coordinate `X_i` gives

`Q = a_i ( X_i + a_i^(-1) v^T X_K )^2 + X_K^T S_i X_K`.           (3.2)

Define the overlap-one third-compound slice through `i` by

`Delta_i(A)
 := sum det A[{i} union P, {i} union Q]^2`,                        (3.3)

where the sum is over ordered two-element sets `P,Q subset K` with `P cap Q=empty`.

Equivalently, `Delta_i` is exactly the squared third-minor mass of all ordered physical triples `(I,J)` satisfying `I cap J={i}`.

### Lemma 3.1 — exact Schur factorization

For every disjoint two-sets `P,Q subset K`,

`det A[{i} union P,{i} union Q] = a_i det S_i[P,Q]`.               (3.4)

Hence, if

`D2_disj(S_i):=sum_{P cap Q=empty, |P|=|Q|=2} det S_i[P,Q]^2`,    (3.5)

then

`boxed: Delta_i(A)=a_i^2 D2_disj(S_i).`                            (3.6)

#### Proof

Order the selected rows and columns with `i` first. The corresponding `3x3` matrix is

`[[a_i, v_Q^T],[v_P, A[P,Q]]]`.

Since `a_i!=0`, its determinant is `a_i` times the determinant of the `2x2` Schur complement

`A[P,Q]-a_i^(-1)v_P v_Q^T=S_i[P,Q]`.

Squaring and summing gives (3.6). QED.

The identity is scale-correct: `Delta_i` is homogeneous of degree six in `A`.

## 4. Random-cut compiler for the residual pair volume

Independently assign every residual physical coordinate in `K` to `L` or `R` with probability `1/2`. For a realized cut define

`M_{L,R}:=S_i[L,R]`.

Its complete physical pair volume is

`E2(M_{L,R})
 = sum_{P subset L,Q subset R, |P|=|Q|=2} det S_i[P,Q]^2`.         (4.1)

A fixed ordered disjoint pair `(P,Q)` survives the oriented cut precisely when every coordinate of `P` lands in `L` and every coordinate of `Q` lands in `R`, an event of probability `2^-4=1/16`. Overlapping pairs cannot occur in (4.1). Therefore

`boxed: E_{L|R} E2(M_{L,R}) = D2_disj(S_i)/16.`                   (4.2)

Consequently some actual original-coordinate cut satisfies

`E2(M_{L,R}) >= D2_disj(S_i)/16
               =Delta_i(A)/(16 a_i^2).`                            (4.3)

This is the key aggregate-before-inversion step. No individual `2x2` minor is selected or inverted.

## 5. Main theorem

### Theorem 5.1 — `QFORM-OVERLAP1-PIVOT-PAIRVOLUME-v1`

Let `A` be any real symmetric matrix, let the original-coordinate inputs be independent with densities bounded by one, and fix a physical coordinate `i` for which `a_i=A_ii!=0` and `Delta_i(A)>0`. Then `Q=X^TAX` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_ov1 ( |a_i|^2 Delta_i(A) )^(-1/8),
`                                                                      (5.1)

where

`C_ov1 = sqrt(2) C_E2
       <=12*2^(4/3)*e^(5/24)
       =37.2419652609898... .`                                      (5.2)

#### Proof

Use the cut furnished by (4.3). In the completed-square representation (3.2), the square variable is the original independent coordinate `X_i`; its shift may depend arbitrarily on every residual variable. Inside the exact residual `X_K^T S_i X_K`, the chosen `L|R` is a cut into disjoint sets of original independent coordinates, and its cross block is `M_{L,R}`. Thus the physical-square lift of the completed fleet01/B01 theorem applies literally:

`||p_Q||_infinity
 <= C_E2 |a_i|^(-1/2) E2(M_{L,R})^(-1/8)`                         (5.3)

`<= C_E2 |a_i|^(-1/2)
   [Delta_i(A)/(16 a_i^2)]^(-1/8)`                                (5.4)

`= sqrt(2) C_E2 |a_i|^(-1/4) Delta_i(A)^(-1/8)`                   (5.5)

`= sqrt(2) C_E2 (|a_i|^2 Delta_i(A))^(-1/8).`                     (5.6)

This proves (5.1). QED.

The certificate

`H_i^(ov1):=|A_ii|^2 Delta_i(A)`                                  (5.7)

is homogeneous of degree eight, so `(H_i^(ov1))^(-1/8)` has exactly the density scaling `A -> cA`.

### Corollary 5.2 — exact decomposition of the overlap-one layer

Let

`D1(A):=sum_{|I|=|J|=3, |I cap J|=1} det A[I,J]^2`.               (5.8)

Then

`boxed: D1(A)=sum_i Delta_i(A).`                                   (5.9)

Indeed every pair `(I,J)` with one-point intersection has a unique shared coordinate. Thus Theorem 5.1 converts any overlap-one mass carried by a nonzero physical diagonal pivot into a quantitative product-space density bound.

### Corollary 5.3 — finite-hub overlap routing

Suppose `H` is a set of at most `h` physical coordinates such that

`sum_{i in H} Delta_i(A) >= theta D1(A)`

and `|A_ii|>=alpha>0` for every `i in H`. If `D1(A)>0`, then some `i in H` obeys

`|A_ii|^2 Delta_i(A) >= alpha^2 theta D1(A)/h`,

and therefore

`boxed:
 ||p_Q||_infinity
 <= C_ov1 [alpha^2 theta D1(A)/h]^(-1/8).
`                                                                      (5.10)

This is a direct bridge from a finite overlap hub to an already-paid Fourier/Riesz endpoint. The remaining hard overlap-one configuration is now specifically one in which the third-minor mass is either spread over many shared coordinates or is carried by shared coordinates with very small/zero physical diagonal pivots.

## 6. Genuinely rotated indefinite target family

The theorem is non-vacuous in the exact three-large-eigenvalue regime even when every nonseparable physical coefficient vanishes with dimension.

Let `m=2p>=4` and define the `m x m` matrix

`S_m = [[0, p^(-1) J_p],[p^(-1) J_p,0]]`,                         (6.1)

where `J_p` is the all-ones `p x p` matrix. Set

`A_m = [1] direct_sum S_m`.                                        (6.2)

Then

`spec(A_m)={1,1,-1,0,...,0}`,                                     (6.3)

so `A_m` is a genuine target with exactly three nonzero eigenvalues, all of modulus one, and it is indefinite. It is not diagonal in the independent coordinates: every coordinate in the first residual bank couples to every coordinate in the second residual bank. Every nonzero residual physical coefficient is

`1/p=2/m -> 0`.                                                    (6.4)

Take the singleton coordinate as the pivot. Then `a_0=1` and the Schur residual is exactly `S_m`. A nonzero residual `2x2` minor must use one row from each bank and one column from each bank; its determinant has absolute value `p^(-2)`. Requiring the row and column pairs to be physically disjoint leaves

`[p(p-1)]^2`

ordered choices. Hence

`boxed:
 Delta_0(A_m)=D2_disj(S_m)
 = [p(p-1)]^2 p^(-4)
 = (1-1/p)^2
 = (1-2/m)^2.
`                                                                      (6.5)

Theorem 5.1 therefore gives, for every admissible product input law,

`boxed:
 ||p_{X^T A_m X}||_infinity
 <= C_ov1 (1-2/m)^(-1/4).
`                                                                      (6.6)

Numerically,

- `m=4`: bound `44.2884100651...`;
- `m=6`: bound `41.2150096084...`;
- `m=10`: bound `39.3785838610...`;
- `m -> infinity`: bound `37.2419652610...`.

The specialized grouped-bank theorem is sharper on this family; the point of (6.6) is different: it recovers a dimension-free estimate **solely from the overlap-one third-compound currency**, despite every nonseparable physical coefficient tending to zero.

Regularity for Theorem 5.1 and (6.6): absolute continuity and essential boundedness are proved; continuity is **not** claimed for arbitrary merely measurable input densities because the square shift in (3.2) depends on the residual variables.

## 7. What changed in the full proof graph

The preceding B04 run left an overlap/triple-hub residue after paying a large disjoint third-compound portion. This run pays a substantial part of the next overlap layer:

- disjoint third-volume -> previous B04 rank-three random-cut Fourier gate;
- one-point-overlap third-volume + nonzero physical pivot -> Theorem 5.1 here;
- a finite set of nonzero-diagonal overlap hubs -> Corollary 5.3.

The first unpaid implication for this pathway is now sharper:

`QFORM-OVERLAP1-SMALLDIAG-OR-OVERLAP2-ROUTING-v1`:

starting from the bare three-large-eigenvalue hypothesis and the failure of the disjoint-third-volume Fourier exit, route the remaining third-compound mass either

1. into Theorem 5.1 with dimension-free control of `|A_ii|^2 Delta_i`;
2. into a zero/near-zero physical-pivot mechanism that uses the overlap-one minor packet without an inverse `A_ii`; or
3. into the intersection-two / principal-third-minor layers and then an already-paid pair, star, grouped, ridge or local-3block endpoint.

The bare spectral hypothesis has **not** been shown here to force alternative 1, so the full QFORM conjecture remains OPEN. No full-solution claim or end-to-end review claim is made.

## 8. Finite checks

The companion `CHECKS.json` records the constant arithmetic, exact spectra, exact overlap currency formula and numerical bounds for `m=4,6,10`. These checks are supplementary; the proof above is algebraic.
