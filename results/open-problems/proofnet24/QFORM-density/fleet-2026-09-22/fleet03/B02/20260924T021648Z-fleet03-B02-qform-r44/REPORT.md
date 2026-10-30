SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-24T02:16:48Z.
attacking: the ultra-near-rank-two physical crossing left by the low-E3 funnel; subtract its symmetric crossing, force the third spectral credit into a literal secondary physical cut or a large diagonal, and spend the secondary cut by the marginal-free E3 Fourier theorem.

# fleet03/B02 r44 — rank-two subtraction forces a secondary physical Fourier cut

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Run: `20260924T021648Z-fleet03-B02-qform-r44`  
Status: **NEW SUPPORTING STRUCTURAL/FOURIER COMPILER / FULL QFORM OPEN / FULL CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

The exact owner target remains unchanged: independent ORIGINAL real coordinates with one-dimensional densities bounded by one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence hypothesis is used.


## 1. Source-pinned inputs

### 1.1 Live ultra-near-rank-two packet

The freshest source-valid low-E3 funnel used here is fleet01/B02 r42:

- `yspennstate/math-open-problems@434d3ab3168164b38fdba61456e35e747a67bea3` (repository snapshot containing the report);
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T012005Z-fleet01-B02-qform-auto11-r42/REPORT.md`.

For a literal disjoint physical cross block `M=A[R,C]` with `E2(M)>4/9`, either the marginal-free physical-E3 theorem pays when `E3(M)>=2^-18`, or a low-E3 survivor has one of two forms. The genuinely rank-two branch satisfies

`x1*x2 > 247/576`,                                                (1.1)

`T2:=sum_(k>=3) xk < 9/1011712`,                                 (1.2)

where `x1>=x2>=...` are the squared singular values of `M`. Thus

`dist_F(M,{rank<=2}) < 0.002982585`.                              (1.3)

The complementary small-`x2` branch was already placed inside the existing giant-near-rank-one packet. This run attacks the rank-two branch without deleting the tail in (1.2).

### 1.2 Marginal-free physical E3 Fourier receiver

The completed whole-cross theorem, recorded in fleet02/B02's latest B02 compiler, gives for every literal original-coordinate cross block `N` with

`Z3:=E3(N)=e3(NN^T)>0`

a continuous `C0` density and

`||p_Q||_infinity <= C3 Z3^(-1/6)`,                              (1.4)

`int_R |phi_Q(t)|dt <= 2*pi*C3*Z3^(-1/6)`,                       (1.5)

with

`C3=10.3450832321475...`.                                        (1.6)

One source snapshot containing the theorem and its aggregate use is

`yspennstate/math-open-problems@434d3ab3168164b38fdba61456e35e747a67bea3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260924T011009Z-fleet02-B02-qform-auto11/REPORT.md`.

The same proof yields the uniform three-credit crossing tail

`|phi_Q(t)| <= min{1,
 4*sqrt(e)*pi^(3/2)*Z3^(-1/4)*|t|^(-3/2)}`.                      (1.7)

This is a physical three-crossing estimate, not the refuted scalar pointwise Fresnel estimate.

### 1.3 Designated partner fleet04/B02

The designated partner's zero-diagonal physical-triple theorem is pinned at

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`.

On its exact overlap, for a nonsingular physical zero-diagonal principal triple `H0`,

`L:=int_R |phi_Q(t)|^2 dt
 <= 6*pi*2^(2/3)*|det H0|^(-1/3)`.                               (1.8)

The partner's strong-cut report is

`yspennstate/math-open-problems@674f13a108a33176aafffe8f9b6d44ec3a89f03a`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260923T151038Z-fleet04-B02-QFORM-r1/REPORT.md`.

It constructs an actual physical cut `M` with `||M||_F^2>11907/16384` and leaves, among its explicit survivors, near-rank-one/two physical-cross states. Section 5 below applies the present theorem to that same partner survivor and applies (1.8) to the new secondary Fourier cut.

## 2. The deterministic third-credit extraction

Let `R,C` be disjoint sets of original coordinates and put

`M=A[R,C]`.                                                       (2.1)

Let `sigma_1(M)>=sigma_2(M)>=...` be its singular values. Define the symmetric crossing operator `B` on the full physical coordinate space by

`B[R,C]=M`, `B[C,R]=M^T`,                                        (2.2)

and all other entries of `B` equal to zero. Put

`K=A-B`.                                                          (2.3)

Then `K[R,C]=K[C,R]=0`, while `diag K=diag A`.

### Lemma 2.1 — spectral credit left after removing one physical crossing

Assume the target spectral hypothesis `s3(A)>=1`. If

`sigma_2(M) <= 1-alpha`,                                          (2.4)

for some `alpha in (0,1]`, then

`boxed: ||K||_op >= alpha.`                                      (2.5)

#### Proof

The nonzero singular values of the symmetric matrix `B` are

`sigma_1(M), sigma_1(M), sigma_2(M), sigma_2(M), ...`;             (2.6)

therefore

`s3(B)=sigma_2(M)`.                                               (2.7)

The singular-value Weyl inequality gives

`s3(A)=s3(B+K) <= s3(B)+s1(K)`.                                  (2.8)

Since `s3(A)>=1`, equations (2.4),(2.7),(2.8) imply (2.5). QED.

This step is purely deterministic. The singular vectors of `M` are used only to identify singular values of the coefficient matrix `B`; no random coordinate is rotated or declared independent.

## 3. Large diagonal or a literal secondary physical cut

Fix `beta in (0,1)`. Suppose first that

`max_i |A_ii| < beta*alpha`.                                     (3.1)

Let

`D=diag(K)=diag(A)`, `H=K-D`.                                    (3.2)

Then `H` is symmetric and zero diagonal. By (2.5),(3.1),

`||H||_op >= ||K||_op-||D||_op
             > (1-beta)alpha`,                                   (3.3)

and hence

`||H||_F^2 > (1-beta)^2 alpha^2`.                                (3.4)

Independently color every original physical coordinate into `J` or `J^c` with probability `1/2`. Since `H` is zero diagonal,

`E ||H[J,J^c]||_F^2 = (1/4)||H||_F^2.                            (3.5)

The important support fact is exact: `B` is supported only on `R x C` and `C x R`, whereas `H[R,C]=H[C,R]=0`. Thus on every cut the two rectangular matrices `B[J,J^c]` and `H[J,J^c]` have disjoint entry support, so

`||A[J,J^c]||_F^2
 =||B[J,J^c]||_F^2+||H[J,J^c]||_F^2
 >=||H[J,J^c]||_F^2`.                                           (3.6)

Consequently some deterministic original-coordinate cut has

`boxed:
 E_N:=||N||_F^2
 >= ((1-beta)^2 alpha^2)/4,
 N:=A[J,J^c].}`                                                   (3.7)

There is no category/dimension loss and no cancellation payment: the removed primary crossing and the residual off-diagonal matrix occupy disjoint physical coefficient entries.

We have therefore proved:

### Theorem 3.1 — `QFORM-R2-SUBTRACTION-SECONDARY-CUT-v1`

Let `A` satisfy `s3(A)>=1`, and let `M=A[R,C]` be any literal physical cross block with `sigma_2(M)<=1-alpha`. For every `beta in (0,1)`, at least one of the following holds:

1. **physical diagonal:** some `i` has `|A_ii|>=beta*alpha`;
2. **secondary physical cut:** there is a literal original-coordinate cut `N=A[J,J^c]` satisfying (3.7).

This theorem does not assert that a large diagonal alone closes QFORM. It identifies where the third spectral credit must go after a rank-two crossing has absorbed at most `sigma_2(M)` of the third singular direction.

## 4. Spend the secondary cut by integrated Fourier

Let `0<theta<=1/2`, and let `y1>=y2>=...` be the squared singular values of the secondary physical cut `N`. Put

`E_N=sum yj`, `T_N=sum_(j>=3) yj`.                                (4.1)

The elementary exterior-volume funnel used in r43 says that if neither

`y2 < theta E_N`                                                  (4.2)

nor

`T_N < theta E_N`                                                 (4.3)

holds, then

`E3(N)>=theta^3 E_N^3`.                                          (4.4)

Applying (1.4)-(1.5) and then (3.7) gives the genuine Fourier-`L1` exit

`boxed:
 ||p_Q||_infinity
 <= [2 C3 theta^(-1/2)]/[(1-beta)alpha],}`                        (4.5)

`boxed:
 int_R |phi_Q(t)|dt
 <= [4 pi C3 theta^(-1/2)]/[(1-beta)alpha].}`                     (4.6)

The density on this exit is continuous and vanishes at infinity.

Thus Theorem 3.1 sharpens to an exhaustive four-way compiler:

### Theorem 4.1 — `QFORM-R2-SUBTRACTION-FOURIER-FUNNEL-v1`

Under the hypotheses of Theorem 3.1, for every `beta in (0,1)` and `theta in (0,1/2]`, at least one holds:

1. `max_i |A_ii|>=beta alpha`;
2. a secondary literal physical cut `N` satisfies `y2<theta E_N`;
3. a secondary literal physical cut `N` satisfies `T_N<theta E_N`;
4. the full ambient QFORM law has genuine Fourier `L1` and obeys (4.5)-(4.6).

No nonzero tail is deleted in alternatives 2-3. They are coefficient-geometry packets for the next receiver.

### Concrete target-scale constants

Take

`alpha=1/2`, `beta=1/4`, `theta=1/4`.                              (4.7)

Then a primary physical crossing with

`sigma_2(M)<=1/2`                                                  (4.8)

forces either

`boxed: max_i |A_ii|>=1/8,}`                                     (4.9)

or a secondary physical cut with

`boxed: E_N>=9/256=0.03515625.}`                                 (4.10)

If that secondary cut is outside its two low-rank tubes, then

`E3(N)>= (1/4)^3(9/256)^3
       =729/2^30
       =6.789341568946838e-7`,                                   (4.11)

and the full law has

`boxed: ||p_Q||_infinity <=110.347554477,}`                       (4.12)

`boxed: int_R |phi_Q(t)|dt <=693.334132969.}`                    (4.13)

These constants are not optimized; their role is to make the new spectral-to-physical implication fully quantitative and dimension-free.

## 5. Designated fleet04/B02 applied to actual inequalities

### 5.1 Apply the partner strong-cut survivor

The fleet04/B02 strong-cut theorem supplies an actual literal cross block `M` with

`||M||_F^2>11907/16384`,                                         (5.1)

and explicitly leaves near-rank-one/two physical-cross survivors when its D5 / optimized-HY exits do not fire.

On any such survivor for which the actual second singular value obeys

`sigma_2(M)<=1/2`,                                                (5.2)

Theorem 4.1 applies to that **same physical M** and gives the concrete exhaustive alternatives (4.9), a secondary low-rank physical cut with energy at least `9/256`, or the full Fourier payment (4.12)-(4.13). This converts the partner's low-rank survivor into a new third-spectral-credit packet; it is not a citation-only dependency.

The remaining partner subcase `sigma_2(M)>1/2` is a balanced robust two-mode crossing and is not claimed paid here.

### 5.2 New hybrid with the partner L2 theorem

On the overlap where the designated partner's zero-diagonal physical triple `H0` exists, combine its actual inequality (1.8) with the secondary-cut tail. From (1.7),(4.4),

`|phi_Q(t)| <= K |t|^(-3/2)`,                                    (5.3)

with

`K=4 sqrt(e) pi^(3/2) theta^(-3/4) E_N^(-3/4)`.                  (5.4)

For every `T>0`, Cauchy-Schwarz below `T` and direct integration above `T` give

`int |phi_Q|
 <= sqrt(2L) T^(1/2) + 4K T^(-1/2)`.                             (5.5)

Optimizing in `T` yields

`int |phi_Q| <=4 sqrt(K) (2L)^(1/4)`.                             (5.6)

Using (1.8), dividing by `2*pi`, and simplifying gives the new partner hybrid

`boxed:
 ||p_Q||_infinity
 <=2^(8/3) 3^(1/4) e^(1/4)
   |det H0|^(-1/12)
   theta^(-3/8) E_N^(-3/8).}`                                    (5.7)

At the concrete scale (4.7),(4.10),

`boxed:
 ||p_Q||_infinity
 <=63.331843800 |det H0|^(-1/12).}`                               (5.8)

This is a new equation-level application of the designated fleet04/B02 `L2` theorem. Continuity on this overlap comes from the secondary physical-E3 Fourier `L1` exit, not from the partner `L2` estimate alone.

## 6. Apply to the freshest ultra-near-rank-two packet

Return to the fleet01/B02 r42 live packet (1.1)-(1.2). Its nonzero tail remains in the true matrix throughout this argument.

Split only by the actual second singular value of the same physical cross block:

### Case A: `sigma_2(M)>1/2`

This is now a quantitatively balanced robust two-mode crossing. Together with (1.1), it remains a dedicated rank-two core packet. No Fourier `L1` claim is made here.

### Case B: `sigma_2(M)<=1/2`

Theorem 4.1 gives, with no use of the tiny-tail deletion,

1. a physical diagonal `|A_ii|>=1/8`; or
2. a secondary physical cut `N` with `||N||_F^2>=9/256` lying in a genuine near-rank-one/two tube; or
3. a continuous-density Fourier exit with (4.12)-(4.13).

Thus the first unpaid interface from r42 is narrowed from

> robust ultra-near-rank-two crossing + unspecified third curvature

to

> balanced rank-two core (`sigma_2>1/2`), or a large physical diagonal (`>=1/8`), or **two simultaneous literal low-rank physical crossings at fixed scale**.

The third spectral direction can no longer remain an unspecified diffuse coefficient cloud in the `sigma_2<=1/2`, small-diagonal subcase: random-cut aggregation forces a fixed-energy actual physical cut before any minor inversion.

This is correction-safe because the cut is made in the ORIGINAL coordinates and because the primary crossing and residual coefficient supports are disjoint after the exact subtraction (2.2)-(2.3).

## 7. Deterministic checks

The constants were independently recomputed:

- `(1-beta)^2 alpha^2/4 = 9/256 = 0.03515625` at `(alpha,beta)=(1/2,1/4)`;
- `theta^3 E_N^3 >=729/2^30=6.789341568946838e-7` at `theta=1/4`;
- (4.12) evaluates to `110.34755447624...` using `C3=10.3450832321475`;
- (4.13) evaluates to `693.33413296831...`;
- (5.8) has coefficient `63.33184379940...`.

A seeded finite regression tested the deterministic Weyl/subtraction and max-cut lower bounds on 500 constructed symmetric matrices of dimensions 6 through 10 with zero physical diagonal, literal primary `R-C` crossings having `sigma_2 in [0.15,0.45]`, and independently generated residual symmetric coefficients with the `R-C` support removed. Every retained matrix was scaled in the residual until `s3(A)>=1`. There were zero violations of `||A-B||_op>=1-sigma_2`; the minimum observed slack was about `0.44565`. Exhaustive cuts for these small dimensions had zero violations of (3.7); the smallest observed ratio of best-cut energy to the rigorous floor was about `42.13`. These computations are corroborative only; the proof is (2.8) plus the exact random-cut expectation (3.5)-(3.6).

## 8. Status and next implication

`QFORM-R2-SUBTRACTION-SECONDARY-CUT-v1`: **PROVED supporting structural lemma**.

`QFORM-R2-SUBTRACTION-FOURIER-FUNNEL-v1`: **PROVED supporting integrated-Fourier compiler**, conditional only on the already completed marginal-free physical-E3 receiver in its stated scope.

Full unrestricted QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

Full-target continuity: **OPEN**. Continuity is proved only on the physical-E3 exit above.

Target-wide universal unweighted `int |phi_Q|`: **OPEN / not refuted**.

The next B02 implication is `QFORM-COUPLED-TWO-LOWRANK-CUTS-OR-LARGE-DIAGONAL-L1-v1`: on the r42 ultra-rank-two survivor, pay the balanced `sigma_2>1/2` core, or combine the fixed-energy secondary low-rank cut with the primary robust two-mode crossing before selecting a tiny physical minor; separately route the `|A_ii|>=1/8` branch through a product-preserving pivot/kernel-curvature receiver. The nonzero transverse tails remain part of the actual quadratic form throughout.

No task identity, schedule, cadence, enabled/paused state, notification, email, Drive, permission, public-release, paid-model/API, installation, or cross-account-authentication state is changed by this report.
