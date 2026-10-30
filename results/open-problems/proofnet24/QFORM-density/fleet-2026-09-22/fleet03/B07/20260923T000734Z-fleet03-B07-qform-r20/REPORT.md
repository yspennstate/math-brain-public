SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T00:07:34Z.
attacking: all third-compound overlap classes at once — select finitely many disjoint original-coordinate banks by overlap-aware random coloring, then push the one- and two-shared packets down an exact Schur ladder without choosing one tiny minor.

# fleet03/B07 — overlap-aware coordinate-bank selection and the two-pivot Schur rung

**Run:** `20260923T000734Z-fleet03-B07-qform-r20`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Owner control:** revision `2026-09-22.15` at the substantive source refresh  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Outcome:** `ESSENTIAL STRUCTURAL STEP + EXACT SCHUR LEDGER + PARTNER INEQUALITY / FULL TARGET OPEN`.

## 1. Exact target and correction boundary

The target is unchanged. For arbitrary dimension, independent real original coordinates with marginal probability densities at most one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or give a target-valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is introduced. Continuity of the full target is tracked separately.

The current correction ledger was reread. This report does not use law-uniform pointwise quadratic stationary phase, the false arbitrary-joint rank-three coarea inequality, a worst conditional projected-density cap, a fiber-supremum estimate, or the inference that aggregate minor mass contains one dimension-free individual minor. It also does not replace a small nonzero pivot by an exact zero pivot.

The incoming own result is

`yspennstate/math-open-problems@2bfa1a13adc433a23ba60ac2372e33c0c15202f1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T235048Z-fleet03-B07-qform-r20/REPORT.md`.

It proved the scalar shared-minor identity

`W_i(A)=A_ii^2 ||wedge^2 S_i||_F^2`

for every genuine physical scalar pivot and an exact quarter-Riesz transducer for a tiny nonzero scalar square. The first unpaid structural issue was that the total shared third-compound mass can be spread among arbitrarily many physical pivots, so selecting `max_i W_i` loses dimension.

This run removes that dimension loss at the coordinate-selection stage: instead of selecting one pivot, it selects a bounded number of **disjoint original-coordinate banks** depending only on the overlap type of the third minors.

## 2. Total third-compound currency

For `q=0,1,2,3`, define

`E_q(A)=sum_{|I|=|J|=3, |I intersect J|=q} det A[I,J]^2`.          (2.1)

These four nonnegative energies partition the full third compound. Since `A` is symmetric,

`sum_(q=0)^3 E_q(A)
 = ||wedge^3 A||_F^2
 = sum_(i<j<k) lambda_i^2 lambda_j^2 lambda_k^2`,                  (2.2)

where the `lambda_i` are the eigenvalues of `A`. Under the owner hypothesis, at least one triple has all three absolute eigenvalues at least one, so

`sum_q E_q(A) >= 1`.                                                (2.3)

Therefore some overlap class obeys

`E_q(A)>=1/4`.                                                       (2.4)

The question is whether this aggregate can be turned into a fixed finite original-coordinate packet without selecting one small minor. The answer is yes.

## 3. Main selection theorem: four overlap types, finitely many physical banks

### Theorem 3.1 — `QFORM-THIRD-COMPOUND-OVERLAP-COLORING-v1`

For every real matrix `A`, the following statements hold.

### q=0: disjoint row and column triples

There exist six pairwise disjoint sets of original coordinates

`L1,L2,L3,R1,R2,R3`

such that

`P0:=sum_(i_a in La, j_b in Rb)
       det A[{i1,i2,i3},{j1,j2,j3}]^2
     >= E_0(A)/1296`.                                               (3.1)

### q=1: one shared physical coordinate

There exist five pairwise disjoint sets

`H,R1,R2,C1,C2`

such that

`P1:=sum_(h in H, r_a in Ra, c_b in Cb)
       det A[{h,r1,r2},{h,c1,c2}]^2
     >= (4/3125) E_1(A)`.                                          (3.2)

### q=2: two shared physical coordinates

There exist four pairwise disjoint sets

`H1,H2,R,C`

such that

`P2:=sum_(h1 in H1,h2 in H2,r in R,c in C)
       det A[{h1,h2,r},{h1,h2,c}]^2
     >= E_2(A)/128`.                                                (3.3)

### q=3: principal triples

There exist three pairwise disjoint sets

`H1,H2,H3`

such that

`P3:=sum_(h_a in Ha)
       det A[{h1,h2,h3},{h1,h2,h3}]^2
     >= (2/9) E_3(A)`.                                              (3.4)

Consequently, under the owner spectral hypothesis, **at least one** of the following source-valid packets exists:

`P0 >= 1/5184`,
`P1 >= 1/3125`,
`P2 >= 1/512`,
`P3 >= 1/18`.                                                        (3.5)

Every bank in the applicable packet consists of original physical coordinates. Conditioning on all coordinates outside their union therefore preserves product independence inside the active banks and adds only affine terms to the active quadratic form.

### Proof

Color the original coordinates independently; then average the relevant squared-minor sum.

For `q=0`, use six colors `L1,L2,L3,R1,R2,R3`. A fixed ordered pair `(I,J)` of disjoint triples is accepted exactly when the three members of `I` receive the three `L` colors and the three members of `J` receive the three `R` colors. Its probability is

`(3!)(3!)/6^6 = 1/1296`.                                           (3.6)

Thus the expected accepted mass is `E_0/1296`, so one coloring attains at least this value.

For `q=1`, use five colors `H,R1,R2,C1,C2`. For a fixed pair of triples with unique common coordinate `h`, the common coordinate lands in `H` with probability `1/5`; the two row-only coordinates split between `R1,R2` with probability `2/25`; and the two column-only coordinates split between `C1,C2` with the same probability. Hence

`Pr(accepted)=(1/5)(2/25)(2/25)=4/3125`.                            (3.7)

For `q=2`, use four colors `H1,H2,R,C`. The two common coordinates split between `H1,H2` with probability `2/16`; the row-only and column-only coordinates land in `R` and `C` with probability `1/4` each. Thus

`Pr(accepted)=(2/16)(1/4)(1/4)=1/128`.                              (3.8)

For `q=3`, use three colors `H1,H2,H3`; a principal triple is rainbow with probability

`3!/3^3=2/9`.                                                        (3.9)

Taking expectations proves (3.1)--(3.4), and (2.4) gives (3.5). QED.

The `q=0` packet recovers the earlier six-bank rainbow third-compound mechanism. The gain here is that **all four overlap classes now have one finite-bank selection theorem with no dimension-dependent coordinate choice.**

## 4. The second rung of the Schur-compound ladder

The preceding run handled one shared coordinate. The two-shared packet has an equally exact pair-pivot identity.

Fix a physical pair `H={h1,h2}` and define

`W_H^(2)(A)
 :=sum_(r,c notin H)
   det A[H union {r}, H union {c}]^2`.                               (4.1)

### Theorem 4.1 — `QFORM-SHARED2-PAIR-SCHUR-COMPOUND-v1`

Let

`B_H=A[H,H]`                                                        (4.2)

and suppose `det B_H !=0`. Write the matrix in the physical block order `H | H^c` as

`A=[[B_H,E^T],[E,C]]`,                                               (4.3)

and let

`S_H=C-E B_H^(-1) E^T`                                              (4.4)

be the exact two-coordinate Schur complement. Then

`boxed: W_H^(2)(A)=det(B_H)^2 ||S_H||_F^2.`                          (4.5)

Moreover the global two-shared ledger is

`boxed: sum_(|H|=2) W_H^(2)(A)=E_2(A)+3E_3(A).`                      (4.6)

If `A` satisfies `s_3(A)>=1`, every invertible physical pair also satisfies

`boxed: ||S_H||_op >=1.`                                            (4.7)

### Proof

For `r,c notin H`, the block determinant formula gives exactly

`det A[H union {r},H union {c}]
 =det(B_H) S_H[r,c]`.                                                (4.8)

Squaring and summing proves (4.5).

For (4.6), an ordered pair of triples `(I,J)` with overlap two has exactly one two-set `H=I intersect J` and is therefore counted once. A principal triple `I=J` has three two-subsets and is counted three times. No other overlap class is counted.

For (4.7), set

`D=diag(0_(2x2),S_H)`.                                               (4.9)

Then

`A-D=[I_2; E B_H^(-1)] B_H [I_2, B_H^(-1)E^T]`,                    (4.10)

which has rank at most two. By the Eckart--Young characterization of the third singular value,

`s_3(A)<=||D||_op=||S_H||_op`.                                      (4.11)

Thus `s_3(A)>=1` implies (4.7). QED.

Equation (4.5) is the exact analogue one exterior degree lower than the preceding scalar identity

`shared-one third compound -> A_ii^2 * second compound(S_i)`.        (4.12)

The new rung is

`shared-two third compound -> det(A[H,H])^2 * first compound(S_H)`. (4.13)

Three shared coordinates are simply principal determinants. This gives an exact **overlap-Schur ladder** rather than a best-minor selection.

## 5. Banked form of the Schur ladder

The selection theorem and Schur identities combine without selecting a pivot.

On the `q=1` packet (3.2), split the shared bank into exact-zero and genuine scalar pivots. Then exactly

`P1 = P1_zero
    +sum_(h in H: A_hh !=0) A_hh^2
       sum_(r1 in R1,r2 in R2,c1 in C1,c2 in C2)
         det S_h[{r1,r2},{c1,c2}]^2`.                                (5.1)

Therefore, if `P1>=1/3125`, either the exact-zero part has mass at least `1/6250`, or the genuine scalar-Schur weighted packet has mass at least `1/6250`.

On the `q=2` packet (3.3), split the shared physical pairs according to whether their `2x2` principal block is singular. Then exactly

`P2 = P2_singular
    +sum_(h1 in H1,h2 in H2: det B_H !=0)
       det(B_H)^2
       sum_(r in R,c in C) S_H[r,c]^2`.                              (5.2)

Hence, if `P2>=1/512`, either the singular-pair packet has mass at least `1/1024`, or the genuine pair-Schur weighted first-compound packet has mass at least `1/1024`.

The important point is that neither (5.1) nor (5.2) takes a maximum over `h` or `H`. The entire determinant weight survives the conditioning ledger. A future analytic receiver may average or group these packets, but it need not pay the reciprocal of one dimension-dependent local minor.

## 6. Completed fleet04 input applied to the tiny-pivot receiver

The designated `fleet04/B07` still has no completed current-QFORM artifact at the fresh lookup, so no result is fabricated for that slot. The compatible completed fleet04 result actually used is fleet04/B18:

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

Its sharp product-projection consequence says that for a nonzero original-coordinate coefficient vector `u`,

`||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`.                        (6.1)

Here is an actual downstream inequality for the new Schur ladder. Suppose a genuine scalar-pivot term in (5.1) reaches the already-isolated tiny-pivot chamber

`F=d[X+m(Y)]^2+H(Y),  d!=0`,                                        (6.2)

and the exact inner Schur remainder has a physical zero-self row with off-diagonal coefficient vector `u`, `eta=||u||_2>0`. Write

`H=2 X_j (u^T Z+b)+G(Z)`.                                           (6.3)

By (6.1), the random coefficient `L=u^T Z+b` has density cap at most `sqrt(2)/eta`. Integrating the clean scalar `X_j` first and then applying the one-dimensional half-Riesz bathtub bound gives

`boxed: H_(1/2)(H) <= 2^(11/4) eta^(-1/2).`                         (6.4)

The completed own theorem `QFORM-SQUARE-HALFRIESZ-QUARTERROOT-v1` from the preceding B07 run then yields

`boxed:
 H_(1/2)(F)
 <= 4 |d|^(-1/4) [2^(11/4) eta^(-1/2)]^(1/2)
 =2^(27/8) (|d| eta)^(-1/4)
 <10.375 (|d| eta)^(-1/4).
`                                                                       (6.5)

At the natural reciprocal scale `eta>=|d|^(-1)`, this is a universal `H_(1/2)<10.375`. This improves the previous `12.158` composite constant while retaining the genuine nonzero square and all curvature in `G`. No projected joint-density cap is used; the original product provenance is retained through the scalar linear projection.

At the same exact scope, direct square convolution also gives

`||p_F||_infinity <= |d|^(-1/2) H_(1/2)(H)
 <=2^(11/4)(|d| eta)^(-1/2)`.                                      (6.6)

Thus the new banked scalar-Schur route has a quantitatively paid receiver whenever it reaches a reciprocal-scale exact-zero row inside the Schur remainder.

## 7. Compatibility with concurrent physical packets and a barrier

Two concurrent results fit the present reduction.

First, fleet03/B20 proved `QFORM-O0-PHYSICAL-DESHEAR-v1` at

`yspennstate/math-open-problems@6b53c8f8d5612c67942c34caafba8e543ed0f0bb`.

It converts the O0 anchored Schur second compound into original-coordinate second-compound or exterior-star bank certificates. This is precisely the kind of analytic receiver required by the `q=0` packet here; no probabilistic theorem is applied to a nonphysical Schur-transformed random vector.

Second, fleet03/B16 proved the cap-only nonzero-pivot barrier at

`yspennstate/math-open-problems@588e9ff712ec9233ce2698b6d477f957af299b24`.

A bounded two-dimensional joint density, even with bounded coordinate marginals, is insufficient for the remaining indefinite nonlinear pushforward. Therefore (5.1)--(5.2) must retain the actual original-product/Schur provenance. The overlap-coloring theorem does exactly that: its banks are subsets of the original independent coordinates, not arbitrary projected coordinates.

## 8. Exact checks

`check_overlap_schur.py` uses only the Python standard library and exact `Fraction` arithmetic. It verifies

`p0=1/1296, p1=4/3125, p2=1/128, p3=2/9`,

and the dominant-class packet constants

`1/5184, 1/3125, 1/512, 1/18`.

For an explicit symmetric integer `5x5` matrix it checks (4.5) for all ten physical pairs, with exact rational arithmetic. It also obtains

`E0=0, E1=200, E2=1880, E3=1380`,

and verifies

`sum_H W_H^(2)=6020=E2+3E3`.                                      (8.1)

`CHECKS.txt` records `STATUS=PASS`. These computations verify finite identities and constants only; they are not numerical evidence for the universal conjecture.

## 9. What is now reduced and what remains unpaid

The coordinate-minor selection debt is now substantially sharper. Under the bare three-large-eigenvalue hypothesis, one does **not** need to choose one principal or cross minor. One can always select a bounded collection of disjoint original-coordinate banks carrying one of the four fixed packets (3.5). The one- and two-shared packets then descend through the exact scalar/pair Schur ladder (5.1)--(5.2) while preserving their determinant weights.

The first unpaid B07 implication is now

`QFORM-FINITE-BANK-OVERLAP-RECEIVER-v1`:

> Prove a dimension-free analytic payment for each of the four packet types in (3.5), using the exact-zero/genuine-Schur splits (5.1)--(5.2) and the already completed product-preserving half-Riesz, ridge, physical-deshear, rank-one triangular, and bordered-hub mechanisms. No receiver may collapse the state to a bounded projected joint-density cap or select one dimension-dependent minor.

More concretely, the remaining difficult pieces are: the fully curved disjoint `q=0` receiver not already routed by physical deshearing; the aggregate exact-zero/shared-one receiver when mass is spread over many hubs; the singular-pair and weighted pair-Schur `q=2` receiver; and the aggregate principal-triple `q=3` bordered receiver. These are now four finite overlap geometries rather than an unrestricted coordinate-minor search.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** The full continuity conclusion also remains OPEN. Continuity is established only in the already-completed scoped branches whose characteristic functions or coefficient-plane densities are integrable.
