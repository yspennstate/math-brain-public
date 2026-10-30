SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-23T23:46:06Z.
attacking: the fresh all-small-physical-diagonal branch by decomposing the THIRD COMPOUND in operator norm, not Frobenius mass, to force one localized physical overlap-0/1/2/3 currency; pay overlap 0 and 3 and compress overlap 1 through the corrected fleet04/B20 anchored-third-volume theorem.

# fleet03/B20 r42 — local third-compound overlap operator funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: proof closure and keeper  
Status: **NEW TARGET-LEVEL STRUCTURAL CLOSURE + TWO GLOBAL PAYMENTS + DESIGNATED-PARTNER APPLICATION / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved below only in the disjoint-cross branch; not proved in the principal-triple branch or globally.

## 1. Exact target and fresh source boundary

The target is unchanged: for every finite `n`, independent real original-coordinate random variables with probability densities `f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a universally bounded density, or give a valid counterexample.

No Gaussian, log-concave, moment, compact-support, connected-support, iid, centering, diagonal-basis, or post-rotation independence assumption is used. This run does not use law-uniform pointwise decay of one-dimensional quadratic phases, an arbitrary-joint coarea estimate, a conditional-density supremum in place of independence, one-good-minor inversion, or deletion of a small nonzero random quadratic term.


The immediate fresh global input is fleet03/B01 `QFORM-SCALARPIVOT-COMPOUND-OPERATOR-CLOSURE-v1`, canonical source

`yspennstate/math-open-problems@319a41e1179abcd7827abc2a54b117b4d1276dcf`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T233049Z-auto11/REPORT.md`.

It proves, under the full target hypotheses, that any literal diagonal pivot `a=A_ii!=0` gives

`||p_Q||_infinity <137 |a|^(-1/2)`.                              (1.1)

In particular,

`max_i |A_ii|>=1/64  => ||p_Q||_infinity<1096`.                  (1.2)

Thus any state not already paid by (1.2) lies in the literal all-small-diagonal chamber

`max_i |A_ii|<1/64`.                                             (1.3)

Two additional completed receivers are used exactly at their proved scope:

1. fleet03/B06 `QFORM-PHYSICAL-TRIPLE-DETERMINANT-RECEIVER-v1`: a literal physical principal triple `M` gives

   `||p_Q||_infinity<102 |det M|^(-1/3)`.                        (1.4)

2. fleet03/B02 `QFORM-CROSS-E3-MARGINALFREE-L1-v1`: for a literal disjoint original-coordinate cross block `M=A[U,V]`,

   `V_3=e_3(MM^T)>0`

   implies a continuous `C_0` density with

   `||p_Q||_infinity <= C_E3 V_3^(-1/6)`,
   `C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.              (1.5)

The designated partner actually applied below is corrected fleet04/B20 r12,

`yspennstate/math-open-problems@95d5c3b6e8a753f5da44f742f8449d51470f4a11`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T201641Z-fleet04-B20-QFORM-r12/REPORT.md`.

For an anchored literal cross block

`M=[[b,r^T],[c,N]]`,

with full anchored third-volume `J_3`, it proves

`J_3^(1/2) <= |b| E_2(N)^(1/2)+||r||_2||c||_2||N||_F`,           (1.6)

hence

`max{b^2 E_2(N), ||r||_2^2||c||_2^2||N||_F^2} >= J_3/4`.        (1.7)

This is the corrected full-anchor statement; no unsupported bank-restricted equality is used.

## 2. Third compound and localized overlap currencies

Let `T` denote the set of physical 3-subsets of `[n]`. In the canonical original-coordinate triple basis put

`C = wedge^3 A`,
`C_(I,J)=det A[I,J]`, `I,J in T`.                                (2.1)

Because `A` is real symmetric, its singular values are the absolute eigenvalues. Under the target hypothesis,

`||C||_op=s_1(A)s_2(A)s_3(A)>=1`.                                (2.2)

Split `C=C_0+C_1+C_2+C_3`, where `(C_h)_(I,J)=C_(I,J)` when `|I intersect J|=h`, and zero otherwise.

Define four *localized* physical currencies:

`P_3 := max_(I in T) |det A[I,I]|`,                              (2.3)

`J_0 := sum_(I,J in T, I intersect J=empty) det A[I,J]^2`,       (2.4)

`J_1(j) := sum_(I,J in T, I intersect J={j}) det A[I,J]^2`,
`J_1^* := max_j J_1(j)`,                                         (2.5)

`J_2(S) := sum_(I,J in T, I intersect J=S) det A[I,J]^2`,
`J_2^* := max_(|S|=2) J_2(S)`.                                   (2.6)

The point is that `J_1^*` and `J_2^*` are one-anchor and one-pair packets, rather than dimension-growing total overlap masses.

## 3. New operator-overlap lemma

### Lemma 3.1 — `QFORM-C3-LOCAL-OVERLAP-OPERATOR-v1`

For every real symmetric `A`,

`boxed:
 ||wedge^3 A||_op
 <= P_3 + 3 sqrt(J_2^*) + 3 sqrt(J_1^*) + sqrt(J_0).}`            (3.1)

Consequently, under `s_3(A)>=1`, at least one of

`P_3>=1/4`,                                                       (3.2)
`J_2^*>=1/144`,                                                   (3.3)
`J_1^*>=1/144`,                                                   (3.4)
`J_0>=1/16`                                                       (3.5)

must hold.

### Proof

The `h=3` component is diagonal in the physical triple basis, hence

`||C_3||_op=P_3`.                                                 (3.6)

The disjoint component satisfies the Hilbert--Schmidt bound

`||C_0||_op<=||C_0||_F=sqrt(J_0)`.                               (3.7)

For `h=2`, for every physical pair `S` let `P_S` be the orthogonal projection of `ell_2(T)` onto triples containing `S`, and let `K_S` be the matrix whose `(I,J)` entry is `C_(I,J)` exactly when `I intersect J=S`. Then

`C_2=sum_(|S|=2) K_S`,
`K_S=K_S P_S=P_S K_S`,
`||K_S||_op<=||K_S||_F=sqrt(J_2(S))<=sqrt(J_2^*)`.               (3.8)

For `x in ell_2(T)`, a fixed output triple `I` receives contributions only from the three pairs `S subset I`. Pointwise Cauchy--Schwarz therefore gives

`||C_2 x||_2^2
 <=3 sum_S ||K_S P_S x||_2^2
 <=3 J_2^* sum_S ||P_S x||_2^2`.                                 (3.9)

Every physical triple contains exactly three pairs, so

`sum_S ||P_S x||_2^2=3||x||_2^2`.                               (3.10)

Thus

`||C_2||_op<=3 sqrt(J_2^*)`.                                     (3.11)

The `h=1` proof is identical. For each singleton `j`, project onto triples containing `j`. Every triple contains exactly three singletons, so

`||C_1||_op<=3 sqrt(J_1^*)`.                                     (3.12)

The triangle inequality for `C=C_0+C_1+C_2+C_3` proves (3.1). Combining (2.2) and (3.1), if all four terms on the right were strictly less than `1/4`, their sum would be less than one. Hence at least one of (3.2)--(3.5) holds. QED.

### Why this is different from the existing third-compound mass split

The completed B07 overlap-role work uses the Frobenius identity `sum_h W_h=e_3(A^2)` and then colors an active *global* overlap packet. Lemma 3.1 instead starts from the operator norm of `wedge^3 A` and uses the finite overlap multiplicity of the triple basis. It forces overlap-one mass onto one literal physical anchor or overlap-two mass onto one literal physical pair with dimension-free constants. No largest tiny determinant is selected.

## 4. Two branches pay immediately

### 4.1 Principal triple

If (3.2) holds, the physical-triple receiver (1.4) gives

`||p_Q||_infinity
 <102 (1/4)^(-1/3)
 =102*4^(1/3)
 =161.9149073007...<161.915`.                                    (4.1)

This is essential boundedness; continuity is not claimed from this receiver.

### 4.2 Disjoint third compound

Suppose (3.5) holds. Independently color every physical coordinate `U` or `V` with probability `1/2`. For every ordered disjoint triple pair `(I,J)`, the event `I subset U`, `J subset V` has probability `2^(-6)=1/64`. Therefore some literal disjoint original-coordinate cut has

`e_3(A[U,V]A[U,V]^T)
 >=J_0/64
 >=1/1024`.                                                       (4.2)

Apply (1.5): the full ambient law has a continuous `C_0` density and

`||p_Q||_infinity
 <= C_E3 (1024)^(1/6)
 =24 exp(1/3)
 =33.4946982021...<33.495`.                                      (4.3)

No same-bank terms or extra spectrum are removed.

## 5. Fresh small-diagonal synthesis

Combine Lemma 3.1 with the fresh B01 theorem (1.2). Every target state is now either already paid by (1.2), (4.1), or (4.3), or it satisfies simultaneously

`max_i |A_ii|<1/64`                                               (5.1)

and one of the two localized overlap packets

`J_2(S)>=1/144` for one physical pair `S`,                        (5.2)

or

`J_1(j)>=1/144` for one physical anchor `j`.                      (5.3)

Thus the entire all-small-diagonal branch no longer needs a global/diffuse third-compound packet: every unpaid state has a fixed physical one-anchor or two-anchor packet.

The overlap-two quantity in (5.2) is exactly the physical overlap-two exterior-star currency `W_2(S)` used by the scalar-pivot W2 receiver. In particular, if one of the two shared diagonal pivots is `a!=0`, the completed determinant-free W2 theorem gives the valid scale

`||p_Q||_infinity
 <=77.022 |a|^(-1/4) J_2(S)^(-1/8)
 <=143.355 |a|^(-1/4)`.                                         (5.4)

This is deliberately **not** promoted to a universal payment as `a->0`: the remaining uniform-in-small-pivot endpoint is genuine.

## 6. Designated fleet04/B20 result applied to the one-anchor branch

Assume (5.3). Randomly color every coordinate other than `j` into two disjoint literal banks `R,C` with probability `1/2` each. A determinant term in `J_1(j)` has two row-only and two column-only coordinates; it survives with the row-only pair in `R` and column-only pair in `C` with probability `1/16`. Hence there is one physical split for which

`J_sep
 :=sum_(P subset R, Q subset C, |P|=|Q|=2)
      det A[{j} union P,{j} union Q]^2
 >=J_1(j)/16
 >=1/2304`.                                                       (6.1)

Order the corresponding anchored literal block as

`M=A[{j} union R,{j} union C]
  =[[b,r^T],[c,N]]`,                                              (6.2)

where

`b=A_jj`, `r=A[j,C]`, `c=A[R,j]`, `N=A[R,C]`.                    (6.3)

Because `R` and `C` are disjoint, the full anchored third-volume of this rectangular block is exactly `J_sep`. Apply the corrected designated partner fleet04/B20 r12 inequality (1.7) **at this actual packet**:

`max{ b^2 E_2(N), ||r||_2^2||c||_2^2||N||_F^2 }
 >= J_sep/4
 >=1/9216`.                                                       (6.4)

Inside the unpaid small-diagonal chamber (5.1), `|b|<1/64`. Therefore (6.4) sharpens to the explicit source-valid alternative

`boxed: E_2(N)>4/9`,                                              (6.5)

or

`boxed: ||r||_2 ||c||_2 ||N||_F >=1/96`.                         (6.6)

All banks in (6.2)--(6.6) are literal original-coordinate banks; no rotated random coordinate is called independent. The arbitrary self blocks on `R` and `C`, all outside couplings, all signs, affine terms and extra spectrum are retained.

This is the required actual application of a completed fleet04/B20 result to a new inequality.

## 7. Current compact end-to-end compiler

Under the bare full target hypothesis `s_3(A)>=1`, at least one of the following now holds:

1. **macroscopic physical diagonal:** `max_i|A_ii|>=1/64`, paid by B01 with `||p_Q||_infinity<1096`;
2. **macroscopic physical principal triple:** a literal triple has `|det|>=1/4`, paid with `||p_Q||_infinity<161.915`;
3. **disjoint physical E3 crossing:** a literal disjoint cross block has `E_3>=1/1024`, paid continuously with `||p_Q||_infinity<33.495`;
4. **localized overlap-two star:** one literal physical pair `S` has `J_2(S)>=1/144`, while both physical diagonals are `<1/64` in magnitude;
5. **localized overlap-one anchor:** one literal anchor `j` and disjoint physical banks `R,C` satisfy either `E_2(A[R,C])>4/9` or the two-star packet (6.6), while `|A_jj|<1/64`.

The first three are full-law payments. The last two are the entire remaining output of this compiler.

This is a substantially smaller closure interface than the global overlap-mass branch: the remaining analytic debt is now tied to one physical pair or one physical anchor, with fixed aggregate currency and no dimension dependence.

## 8. First remaining implication

The first remaining implication is

`QFORM-SMALLDIAG-LOCAL-OVERLAP12-PAYMENT-v1`:

> uniformly pay either (i) a physical pair `S` with `J_2(S)>=1/144` and both shared physical diagonals `<1/64`, including the exact-zero/small-pivot limit, or (ii) the one-anchor packet (6.5)/(6.6), while retaining arbitrary same-bank quadratic curvature, all outside couplings, signs, affine terms, fragmented/unbounded cap-one laws and arbitrary additional spectrum.

A valid route may use averaged Fourier / fractional-Riesz / direct small-ball methods, but may not replace (6.5) by one good `2x2` minor or treat the bounded projection density of any derived coordinate as a curved-pushforward bound.

The full unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity also remains open.

## 9. Verification

A finite regression checker was run on 200 random symmetric matrices of dimensions 5--8, each rescaled to `s_3(A)=1`. It directly formed `wedge^3 A`, the four overlap components, and the localized `J_1^*,J_2^*` stars. Results:

`max ||C_1||_op/(3 sqrt(J_1^*)) =0.37340708296177255`,
`max ||C_2||_op/(3 sqrt(J_2^*)) =0.4738281548218091`,
`min [P_3+3sqrt(J_2^*)+3sqrt(J_1^*)+sqrt(J_0)-||wedge^3 A||_op]
 =1.90878755454123`,
`violations=0`.

This computation is regression evidence only. The proof is the analytic finite-overlap argument in Section 3.

Exact numerical constants independently checked:

`102*4^(1/3)=161.91490730075634`,
`24*exp(1/3)=33.49469820206615`,
`4096/9216=4/9`,
`sqrt(1/9216)=1/96`.
