SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-24T05:45:42Z.
attacking: the fleet04/B20 r13 strong-anchor-edge leaf; convert its literal edge into a quantitatively indefinite physical pair and route any disjoint post-puncture third cross singular through the completed pair+third-cross receiver.

# fleet03/B20 r48 — strong double-anchor edge gives L-infinity or a punctured rank-two system

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW ENDPOINT BRANCH CLOSURE / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution memory: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native learned-memory ingestion.  
Continuity: **not proved on the new paid branch**; the result below gives an essentially bounded density.

All coordinates below are literal ORIGINAL coordinates. No random variable is rotated. No Gaussian, log-concave, moment, compact-support, connected-support or iid hypothesis is added. No nonzero coefficient tail is deleted.

## 1. Fresh source-pinned proof graph


The newest fleet03/B19 compiler used for global context is r50:

`yspennstate/math-open-problems@f3a0b13c6d73bb3ec94be4ad5fc293c60ab7da3f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260924T050225Z-fleet03-B19-QFORM-r50/REPORT.md`.

It leaves a robust literal rank-two light-light cross with full-law `H_(1/4)` smoothing, or a fixed physical hub-star. It explicitly does not yet upgrade the fractional estimate to an endpoint density bound.

The designated partner source is fleet04/B20 r13:

`yspennstate/math-open-problems@d2560a041fd91c05d7fddf50f5b5414ecd2680a2`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260924T051424Z-fleet04-B20-QFORM-r13/REPORT.md`.

In its exact localized child-window scope, after the scalar-pivot exit is excluded it has two original physical anchors `i,j`. It proves the exhaustive double-anchor refinement. With

`rho_0=2.157910236855737e-5`,
`a_0=rho_0/512=4.2146684313588616e-8`,
`beta_0=sqrt(3)/(128 sqrt(96))`,

one has the child off-diagonal star `||C_{-j,j}||>a_0`, and either

`|A_ij| >= beta_0/sqrt(2) = 1/1024`,                              (1.1)

or a quantitatively transverse rank-two double-anchor block, or an aligned two-star collar. The present run closes (1.1) whenever the already-live all-small-physical-diagonal gate is active, except for a punctured rank-two survivor.

The endpoint receiver is this slot's completed r47 theorem:

`yspennstate/math-open-problems@fb3a649f17234d139f1731e78557d2e7b1cdd187`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T044648Z-fleet03-B20-QFORM-auto11-r47/REPORT.md`.

Its theorem `QFORM-INDEFINITE-PAIR-THIRDCROSS-QUARTER-SMOOTHING-v1` says: if two original coordinates form an invertible indefinite principal pair `B`, with

`D=|det B|`, `kappa=s_min(B)`,

and after deleting those coordinates there are disjoint original-coordinate sets `L,M` with

`s_3(A[L,M]) >= sigma`,

then the FULL ambient quadratic law has an essentially bounded density and

`||p_Q||_infinity <= C_pc D^(-1/3) kappa^(-1/6) sigma^(-1/6)`,    (1.2)

where

`C_pc=3(6B_1)^(2/3)=35.72978950364268...`,
`B_1=(2+sqrt(pi))(4e)^(1/4)`.

The receiver retains arbitrary same-bank curvature, affine terms, outside couplings, signs and additional spectrum.

## 2. First essential implication: the r13 strong edge is quantitatively indefinite

Work in the normalized target scale `s_3(A)>=1`. Consider the partner r13 strong-edge leaf (1.1) after the child scalar-pivot branch is excluded. In the current all-small-diagonal chamber assume

`|A_ii| <= 1/64`,                                                 (2.1)

and the r13 pivot failure gives the sharper second-anchor bound

`|A_jj| < a_0`.                                                   (2.2)

Write

`a=A_ii`, `c=A_jj`, `d=A_ij`,
`B=[[a,d],[d,c]]`.                                                (2.3)

Set

`A_0=1/64`, `C_0=a_0`, `d_0=1/1024`.                             (2.4)

Then

`d^2-ac >= d^2-|ac| >= d_0^2-A_0 C_0 =: D_0`.                   (2.5)

Numerically

`D_0 = 9.530157744638501e-7 >0`.                                 (2.6)

Therefore `det B=ac-d^2<0`: the literal physical pair is invertible and indefinite, and

`D=|det B| >= D_0`.                                               (2.7)

This already converts the partner's geometric strong-edge leaf into the sign structure required by the r47 endpoint receiver. It remains to obtain a dimension-free lower bound on `kappa=s_min(B)` without silently assuming `|d|` is near its threshold.

## 3. Uniform lower bound for the pair's smaller singular value

For an invertible `2x2` matrix, the product of singular values is `D`, hence

`kappa=D/s_max(B)`.                                               (3.1)

Put `t=|d|>=d_0`. From (2.1)-(2.2),

`D >= t^2-A_0 C_0`,                                              (3.2)

while

`s_max(B) <= ||B||_F <= sqrt(A_0^2+C_0^2+2t^2)`.                 (3.3)

Thus

`kappa >= g(t):=(t^2-A_0 C_0)/sqrt(A_0^2+C_0^2+2t^2)`.           (3.4)

The point of keeping the `t` dependence is that replacing the numerator at `d_0` while allowing the denominator to grow would be invalid. Instead differentiate exactly. For `t>0`,

`g'(t)
 = [2t(A_0^2+C_0^2+2t^2)-2t(t^2-A_0C_0)]
   /(A_0^2+C_0^2+2t^2)^(3/2)
 = 2t(A_0^2+C_0^2+t^2+A_0C_0)
   /(A_0^2+C_0^2+2t^2)^(3/2) >0`.                               (3.5)

Therefore the worst case is exactly the threshold `t=d_0` and

`kappa >= kappa_0:=D_0/F_0`,                                     (3.6)

where

`F_0=sqrt(A_0^2+C_0^2+2d_0^2)
   =0.015685916410416986...`,                                    (3.7)

so

`boxed: kappa >= kappa_0
 =6.075614261408114e-5.`                                         (3.8)

No dimension enters this estimate.

## 4. Endpoint payment or punctured rank-two system

### Theorem 4.1 — `QFORM-R13-STRONGEDGE-TO-LINF-OR-PUNCTURED-R2-v1`

Under the exact-target hypotheses, suppose the fleet04/B20 r13 strong-anchor-edge leaf occurs at target scale one, the all-small-diagonal envelope (2.1) holds at the first anchor, and the r13 scalar-pivot exit has failed at the child anchor so that (2.2) holds. Then exactly one of the following source-valid alternatives holds.

**Endpoint branch.** There exist disjoint original-coordinate sets `L,M` in the complement of `{i,j}` such that

`s_3(A[L,M]) >= 2^-16`.                                          (4.1)

Then the FULL ambient law of `Q=X^TAX` has an essentially bounded density and

`boxed: ||p_Q||_infinity <116273.`                               (4.2)

**Punctured-rank-two branch.** For every pair of disjoint original-coordinate sets `L,M` in the complement of `{i,j}`,

`boxed: s_3(A[L,M]) < 2^-16.`                                    (4.3)

#### Proof

Sections 2-3 give an original-coordinate invertible indefinite pair with

`D>=D_0`, `kappa>=kappa_0`.                                      (4.4)

If (4.1) occurs, apply the completed r47 theorem (1.2) with `sigma=2^-16`. The numerical bound is

`C_pc D_0^(-1/3) kappa_0^(-1/6) (2^-16)^(-1/6)
 =116272.95703803611... <116273`.                                (4.5)

All coefficients outside the selected pair and all same-bank quadratic terms are retained by the source theorem. If (4.1) fails for every disjoint remaining `L,M`, (4.3) is exactly its negation. QED.

This is a genuine endpoint closure of the r13 strong-edge alternative, not a fractional-concentration estimate. It also routes its sole unpaid survivor into the same punctured-rank-two geometry isolated independently by r47 from much larger entry-heavy edges.

## 5. Why this is useful in the current full-target proof graph

The partner r13 localized-window leaf previously ended at

`strong edge OR transverse double anchor OR aligned two-star collar`.

The first alternative is now replaced, in the still-unpaid all-small-diagonal chamber, by

`essential L-infinity payment <116273 OR punctured rank-two cross system`.

Thus a strong double-anchor edge can no longer coexist with a disjoint post-puncture third cross singular at scale `2^-16`.

The new implication is compatible with the fresh fleet03/B19 r50 frontier: both now expose finite physical hubs/stars together with rank-two physical crossing structure. What is *not* proved is that an arbitrary `l2` hub star contains one coefficient as large as `1/1024`; that would be dimension-dependent and is not asserted.

The first remaining implication on this partner leaf is therefore narrowed to

`QFORM-R13-TRANSVERSE/ALIGNED-OR-PUNCTURED-R2-PAYMENT-v1`:

> pay the transverse double-anchor and aligned two-star alternatives, and glue the new punctured-rank-two survivor into a bounded-rank physical carrier or force a disjoint third cross singular that returns to Theorem 4.1/r47.

At the fresher r50 global leaf, the distinct endpoint debt remains `H_(1/4)+diffuse-third-source OR hubstar -> L-infinity`; this run does not rename that separate debt as solved.

## 6. Integrity and continuity

This argument uses no law-uniform pointwise quadratic-phase decay, generic interpolation from a Frostman estimate, arbitrary-joint coarea, conditional projection-density moment, post-rotation independence, interval extremality, one-good-minor extraction, or Monte Carlo proof. Repeated eigenvalues are harmless. The r47 endpoint receiver proves only essential boundedness, so continuity on the new branch is **not proved**.

Full unrestricted QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full universal continuous-density conclusion: **OPEN**.

## 7. Numerical constants

`rho_0 = 2.157910236855737e-5`  
`a_0 = rho_0/512 = 4.2146684313588616e-8`  
`d_0 = 1/1024 = 9.765625e-4`  
`D_0 = d_0^2-(1/64)a_0 = 9.530157744638501e-7`  
`F_0 = sqrt((1/64)^2+a_0^2+2d_0^2) = 0.015685916410416986`  
`kappa_0 = D_0/F_0 = 6.075614261408114e-5`  
`B_1 = 6.850346732237482`  
`C_pc = 35.72978950364268`  
`endpoint bound at sigma=2^-16 = 116272.95703803611`.
