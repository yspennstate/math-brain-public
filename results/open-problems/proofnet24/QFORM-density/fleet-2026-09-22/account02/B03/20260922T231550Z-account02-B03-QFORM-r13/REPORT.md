# B03 decoupled-time report: overlap-one minor bank and a sharp pivot-E3 obstruction

Run: `20260922T231550Z-account02-B03-QFORM-r13`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: **Decoupled time integral**  
Status: **ESSENTIAL_STEP_APPLIED + REFUTED_INTERMEDIATE_STRUCTURAL_GATE / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target remains: independent real coordinates with densities at most one, symmetric `A`, and at least three eigenvalues of `A` having magnitude at least one; prove one universal essential-density bound for `X^T A X`, or give a genuine target counterexample. No moment, support, diagonal-basis, or post-rotation independence hypothesis is added.

## 1. Sources actually used

Fresh brain control at the beginning of the run was `yspennstate/math-research-brain@78f318e2c65263b0de840aaf014f28f4d6ef0f20`, OWNER CONTROL revision `2026-09-22.15`; a later refresh observed main `15158a63bfe014b1a4053dcd8229e2e6258253cd` with the same QFORM-only programme and no applicable stop.

The designated partner result actually applied is account03/B03 run `20260922T225606Z-account03-B03-QFORM-r21`, canonical mathematics

`yspennstate/math-open-problems@bbf30c1b2b9495570c8ef2a3f0436c94062892a`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T225606Z-account03-B03-QFORM-r21/REPORT.md`.

Its theorem `QFORM-PIVOT-EK-AGGREGATE-HALF-RIESZ-v1` says: after a nonzero original-coordinate scalar pivot `d`, if a Schur-residual original-coordinate cross block `B` has

`E_k(B)=e_k(BB^T)>0`, `k>=3`,

then

`||p_Q||_infinity <= C_k |d|^(-1/2) E_k(B)^(-1/(4k))`,

`C_k = sqrt(e)/(2k) Beta(1/(4k),(k-2)/(8k))`.

For `k=3`, `C_3=9.84065586492201854...`. Its proof starts from an independent-copy / regularized-determinant estimate and never makes sums and differences of a coordinate pair independent.

This run also obeys the later proof-first continuation and applies the newest source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

from `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially the proved D' extension and Theorem F in `FOURIER_ROUTE_REPORT.md` / `RESULTS.md`.

Corrections retained include the false law-uniform pointwise Fresnel decay, false conditional sum/difference density cap, false arbitrary-joint rank-three coarea gate, false positive conditional projection-density moments, and false universal single local/cross-rank-three extraction. None is used below.

## 2. New theorem: convert residual E_k into an original-matrix overlap-one bank

Fix an original coordinate `i` with `d=A_ii != 0`. Let

`S=A_{-i,-i}-A_{-i,i} A_{i,-i}/d`

be its Schur complement. For `k>=3`, define the original-matrix overlap-one bank

`M_{i,k}(A)`
` := sum |det A[{i} union I, {i} union J]|^2`,

where the sum is over ordered disjoint `k`-subsets `I,J` of the coordinates other than `i`.

### Theorem `QFORM-OVERLAP-ONE-MINORBANK-TRANSDUCER-v1`

If `M_{i,k}(A)>0`, then

`||p_Q||_infinity`
` <= sqrt(2) C_k |d|^{-(k-1)/(2k)} M_{i,k}(A)^(-1/(4k)).`       (2.1)

For `k=3`,

`||p_Q||_infinity`
` <= 13.9167889868 |d|^(-1/3) M_{i,3}(A)^(-1/12).`             (2.2)

### Proof

For every disjoint `I,J`, the block determinant identity gives exactly

`det A[{i} union I,{i} union J] = d det S[I,J]`.                (2.3)

Randomly put each residual original coordinate into `L` or `R`, independently with probability `1/2`. For `B=S[L,R]`, Cauchy--Binet gives

`E_k(B)=sum_{I subset L,J subset R,|I|=|J|=k} det S[I,J]^2`.

Every ordered disjoint pair `(I,J)` is captured with probability `2^(-2k)`. Hence

`E E_k(S[L,R])`
` = 2^(-2k) |d|^(-2) M_{i,k}(A)`.                              (2.4)

Some deterministic cut therefore has at least the right side of (2.4). Insert that cut into the partner theorem:

`E_k^(-1/(4k))`
` <= sqrt(2) |d|^(1/(2k)) M_{i,k}^(-1/(4k))`,

which gives (2.1), and (2.2) is `k=3`. The homogeneity is exact: under `A -> rho A`, the right side scales as `|rho|^(-1)`. QED.

This removes a residual-Schur bookkeeping layer: the partner's decoupled-time certificate can now be sought directly as a positive original-matrix bank of `(k+1)x(k+1)` minors whose row and column index sets overlap only at the physical pivot.

## 3. Exact target witness where the newest D' theorem strictly extends the old D / D5 / pivot-E3 gates

Define the real `5x3` frame

`U_j = (1/sqrt(5), sqrt(2/5) cos(2 pi j/5), sqrt(2/5) sin(2 pi j/5))`,
`j=0,...,4`.

Elementary roots-of-unity identities give

`U^T U=I_3`, and every row leverage is `||U_j||^2=3/5`.

Set

`A_0 = [[0_5,U],[U^T,0_3]]`.

Its characteristic polynomial is

`z^2 (z-1)^3 (z+1)^3`,

so it is a genuine target matrix, in fact with six eigenvalues of magnitude one. Take the natural cross cut with the five-row bank on the constrained side and the three-row bank on the other side. Then

`Z=e_3(U^T U)=1`, and every volume-sampling row marginal is exactly `3/5`.

The newest Claude D' theorem permits any marginal threshold `h<3/4`. Choosing `h=3/5` gives the actual target-level inequality

`||p_{X^T A_0 X}||_infinity`
` <= 6 sqrt(e) (6/5)^(-1/2) (3/5)^(-1)`
` = 10 sqrt(5e/6)`
` = 15.0506971833506914...`.                                  (3.1)

This is a genuine enlargement of the three specific gates being compared here:

* old Theorem D requires all constrained-side marginals `<=1/2`. Any disjoint rank-three cross cut in eight coordinates has constrained side size at most five, while its marginals sum to three; therefore its maximum marginal is at least `3/5>1/2`. So no rank-three cut of this matrix can satisfy the old-D marginal gate;
* D5 requires two disjoint sides of size at least five, impossible in eight coordinates;
* every physical diagonal of `A_0` is zero, so the partner scalar-pivot theorem cannot start.

Other already-proved mechanisms may also control this matrix; the point is only that D' covers an exact target instance beyond these three gates, and its relaxed exponent is therefore not formal slack.

## 4. Exact source-valid obstruction to a universal pivot-E3 structural reduction

Let `H_8` be the Sylvester Walsh matrix and let `R` be its first three columns divided by `sqrt(8)`. Put

`P=RR^T`,

so `P` is a rank-three orthogonal projection and every diagonal entry is `3/8`. For `0<t<=1/2`, define

`A_t=t I_8+(1-t)P`.                                            (4.1)

The spectrum is

`1,1,1,t,t,t,t,t`,

so every `A_t` is a genuine target matrix. Every physical scalar pivot is

`d=(3+5t)/8`.                                                  (4.2)

For one pivot, the exact symbolic checker enumerates every ordered residual cut (three states per one of seven coordinates: unused / left / right), computes `E_3` by exact determinants, and proves that

`d^6 E_3(S[L,R]) / F(t)` belongs to `{0,1/4,1/2,1}`            (4.3)

for every cut, where

`F(t)=t^2(1-t)^6(5t+3)^4/2^20`.                               (4.4)

Equality occurs. Walsh translation symmetry makes all eight pivots permutation-equivalent. Therefore

`max_{physical pivots i, residual cuts L,R} |d_i|^6 E_3(B_i[L,R]) = F(t) -> 0`. (4.5)

Consequently the bare three-large-eigenvalue hypothesis does **not** imply any positive universal lower bound on the partner theorem's homogeneous pivot-E3 certificate. Even the best bound obtainable from that theorem on this family is

`C_3 F(t)^(-1/12)`
` ~ 21.6620864982538225 t^(-1/6)`,                             (4.6)

which diverges as `t -> 0`.

The new original-matrix bank from Section 2 also collapses explicitly:

`M_{i,3}(A_t)=7 t^2(1-t)^6/128`                               (4.7)

for every pivot `i`; the random-cut transducer (2.2) therefore also scales as `t^(-1/6)`.

This is a counterexample only to the proposed **structural proof gate** `three large eigenvalues => uniformly positive pivot-E3 certificate`; it is not a counterexample to QFORM.

## 5. The same adversary is uniformly controlled by the newest Fresnel theorem

The obstruction (4.1) simultaneously identifies the needed complementary branch. Write

`A_t = t I_8 + (1-t) R R^T`.

The first term is diagonal in the original product coordinates. The three rank directions have coefficient `1-t`, and their row leverage is `3/8<=1/2`. Thus the newest completed Theorem F applies with `G=I_3` and yields

`||p_{X^T A_t X}||_infinity <= 12/(1-t) <= 24`                (5.1)

uniformly for `0<t<=1/2` and for every independent cap-one input law.

So the source-valid lesson is exact: aggregate pivot/collision certificates are powerful once present, but they cannot be the sole structural branch. The near-rank-three diagonal-tail regime can make every pivot-E3 bank vanish while a dependence-safe, original-coordinate Fresnel/Brascamp--Lieb estimate remains uniformly strong.

## 6. First unpaid implication

A viable full proof now needs an exhaustive product-preserving structural alternative that pays **either**

1. a diffuse/diagonal-plus-low-rank Fresnel certificate such as Theorem F/D', including the `A_t` boundary family above; **or**
2. a localized/pivot branch with positive overlap-one bank `M_{i,3}` (or a stronger already-paid physical pair/ridge certificate); **or**
3. a grouped/ridge mechanism for the known collinear-bank and hybrid families that evade both local certificates.

What is now rigorously unavailable is the shortcut asserting that branch 2 alone follows from `s_3(A)>=1` at a universal scale. The exact obstruction occurs already in fixed dimension eight and has a uniformly bounded output density by branch 1.

## 7. Exact computation and status

`check_symbolic.py` performs only exact SymPy algebra. It verifies the Parseval frame, the target spectra, the complete `3^7` residual-cut certificate set, the exact maximum (4.4), the overlap-one bank (4.7), and the constants. Saved output ends `STATUS=PASS`.

The computation is a finite exact certificate for the cut enumeration; the transducer theorem and D' application are analytic. No numerical histogram is used as proof.

Full QFORM remains **OPEN**. Essential boundedness is proved only in the stated new branches; continuity is not claimed here. No scheduler/task, notification, email, permission, public-release, paid-model/API/Codex, or cross-account action was performed.
