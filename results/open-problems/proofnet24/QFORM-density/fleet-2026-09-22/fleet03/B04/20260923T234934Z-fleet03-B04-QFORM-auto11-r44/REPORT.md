SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T23:49:34Z.
attacking: heavy-carrier two-core plus diffuse-bank square or projected-crossing routing with explicit product-Fourier constants.

# fleet03/B04 r44 — delete the physical heavy set, renormalize the residual frame, and repave

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / STRICT HEAVY-CARRIER ENLARGEMENT / DESIGNATED-PARTNER RESULT APPLIED / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: continuous `C_0` density on the paid cross-volume branch below; the full target continuity statement remains OPEN.

The unrestricted conjecture is not proved here. The new point is a product-coordinate compiler for a low-rank coefficient carrier whose *individual* physical leverage gate has failed: delete only the finitely many genuinely heavy original rows, renormalize the residual Parseval frame, and pave that residual frame. If the deleted rows do not capture too much of any carrier direction, this recovers a target-scale literal original-coordinate cross block and the existing product-Fourier `E_3` theorem pays the whole ambient quadratic form. If the repaving fails, one gets a quantitative finite physical hub that captures a definite amount of an actual carrier direction.

No random variable is rotated and then declared independent. No law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea lemma, moment/support/log-concavity assumption, or deletion of a nonzero random quadratic error is used.

## 1. Fresh sources and correction boundary


The analytic receiver is the completed same-slot theorem

`QFORM-CROSS-E3-OPTIMAL-THRESHOLD-v1`,

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T215155Z-fleet03-B04-QFORM-auto11-r42/REPORT.md`.

For every literal original-coordinate cross block `M`, it proves

`||p_Q||_infinity <= C_* E_3(M)^(-1/6)`,                       (1.1)

with a continuous `C_0` density, where

`C_*=8.45302122552817687470491804598...`.                     (1.2)

The theorem retains arbitrary same-bank quadratic terms and affine terms produced by conditioning outside the selected banks.

The live rank-five source used for the numerical application below is fleet01/B20's actual physical approximant branch, read from

`yspennstate/math-open-problems@af30108d1fd48a138ef13c683d397a74f8e0228e:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260923T165154Z-fleet01-B20-QFORM-auto11/REPORT.md`.

It supplies an original-coordinate symmetric `S_0` satisfying

`rank(S_0)<=5`,

`s_3(S_0)>1597/2000`,

`||A-S_0||_op<403/2000`.                                      (1.3)

Its earlier direct paving paid the case `max_i (P_{S_0})_{ii}<=1/25` and left the physical-heavy-carrier outcome.

The newer assembly sources were also refreshed. Fleet03/B19 r44 isolates an all-coordinate-essential threshold-Schur core, and fleet03/B20 r41 reduces the non-annular source to a finite threshold carrier with retained coefficient error. Those Schur operators are not silently treated as actual random quadratic coefficients here; realizing them product-safely remains part of the live glue.

## 2. Residual paving after deleting a physical hub

Let

`S=U Lambda U^T`                                                (2.1)

be a real symmetric matrix of rank `r<=R`, where `U^T U=I_r`. Write the physical rows of `U` as `u_i^T`, and let

`ell_i=||u_i||_2^2`.                                            (2.2)

Choose any physical index set `H`, let `L=H^c`, and define

`G=U_L^T U_L=I_r-U_H^T U_H`,

`beta=max_{i in L} ell_i`.                                      (2.3)

### Theorem 2.1 — `QFORM-RESIDUAL-PAVING-AFTER-HUB-DELETION-v1`

Assume

`G >= gamma I_r`, `gamma>0`, and `R beta < gamma`.              (2.4)

Put

`g=(1-sqrt(R beta/gamma))/2 >0`.                               (2.5)

Then there is a partition of the ORIGINAL residual coordinates

`L=I disjoint_union J`                                          (2.6)

for which

`s_k(S[I,J]) >= g gamma s_k(S), 1<=k<=r`.                      (2.7)

Consequently, if `A=S+E`, `||E||_op<=delta`, `s_3(S)>=sigma`, and

`m:=g gamma sigma-delta>0`,                                    (2.8)

then the full ambient quadratic form on independent cap-one inputs satisfies

`boxed: ||p_{X^T A X}||_infinity <= C_*/m`,                    (2.9)

and its density is continuous and vanishes at infinity.

#### Proof

Because `G>=gamma I`, define the renormalized residual frame

`V=U_L G^(-1/2)`.                                               (2.10)

Then `V^T V=I_r`. Its physical row `v_i^T=u_i^T G^(-1/2)` obeys

`||v_i||^2 <= ell_i/gamma <= beta/gamma`.                       (2.11)

Choose independent Rademacher signs `epsilon_i` on `L`, put `I={i:epsilon_i=1}`, and set

`F=V_I^T V_I`.

Since `sum_i v_i v_i^T=I_r`,

`F-(1/2)I_r=(1/2) sum_{i in L} epsilon_i v_i v_i^T`.            (2.12)

Independence and cancellation of cross terms give the exact second-moment identity

`E ||F-(1/2)I_r||_F^2
 =(1/4) sum_i ||v_i v_i^T||_F^2
 =(1/4) sum_i ||v_i||^4
 <=(1/4)(beta/gamma) sum_i ||v_i||^2
 =(r beta)/(4 gamma)
 <=R beta/(4 gamma)`.                                           (2.13)

Hence some deterministic physical partition satisfies

`||F-(1/2)I_r||_op
 <=(1/2)sqrt(R beta/gamma)`,                                    (2.14)

so

`g I_r <=F<= (1-g)I_r`,
`g I_r <=I_r-F<= (1-g)I_r`.                                    (2.15)

Now write

`B=G^(1/2) Lambda G^(1/2)`.                                    (2.16)

Since the smallest singular value of `G^(1/2)` is at least `sqrt(gamma)`, the product singular-value inequality gives

`s_k(B)>=gamma s_k(Lambda)=gamma s_k(S)`.                       (2.17)

Take polar decompositions

`V_I=Q_I F^(1/2)`,
`V_J=Q_J (I-F)^(1/2)`,                                         (2.18)

where `Q_I,Q_J` have orthonormal columns. The cross block is

`S[I,J]=Q_I F^(1/2) B (I-F)^(1/2) Q_J^T`.                      (2.19)

Both square-root factors in (2.19) have smallest singular value at least `sqrt(g)`. Therefore

`s_k(S[I,J])>=g s_k(B)>=g gamma s_k(S)`,                        (2.20)

proving (2.7).

For `M=A[I,J]`, coordinate compression of `E` has operator norm at most `delta`, so Weyl's singular-value inequality gives

`s_3(M)>=g gamma sigma-delta=m`.                                (2.21)

The third compound satisfies

`E_3(M)=sum_{a<b<c}s_a(M)^2s_b(M)^2s_c(M)^2 >=s_3(M)^6>=m^6`. (2.22)

Condition on the original coordinates in `H`. The remaining `I` and `J` variables retain independence and their one-dimensional density caps; every coupling to `H` becomes an allowed affine term. Apply (1.1) to the literal cross block `M` and (2.22):

`||p_{Q|X_H}||_infinity<=C_*/m`.                               (2.23)

The source theorem has the same `L^1` characteristic-function envelope uniformly in the induced affine terms, so averaging over `X_H` yields (2.9) and a `C_0` density. QED.

This is a product-space paving theorem: the only randomization is a deterministic-existence proof for a partition of original coordinate indices.

## 3. Heavy-set dichotomy

Fix a leverage threshold `tau>0` and choose

`H={i:ell_i>tau}`.                                              (3.1)

Then

`|H| tau < sum_{i in H}ell_i <=r<=R`,                           (3.2)

so `|H|<R/tau`, while every residual row has `beta<=tau`.

For any `gamma in (R tau,1)`, exactly one of the following holds:

1. `G>=gamma I`, and Theorem 2.1 applies with `beta<=tau`;
2. there is a unit vector `z in R^r` such that

   `||U_H z||^2>1-gamma`.                                       (3.3)

Indeed, if `lambda_min(G)<gamma`, take a minimizing unit vector `z`; since `U^T U=I`,

`||U_Hz||^2=1-z^T G z>1-gamma`.                                (3.4)

Thus failure of the product-Fourier exit does not merely say "some leverage is large": a bounded set of literal physical coordinates captures a definite fraction of an actual carrier-range direction.

## 4. Spend the live rank-five carrier inequality

Apply Section 3 to the source (1.3) with

`R=5`, `tau=1/25`, `gamma=19/20`.                              (4.1)

Then `|H|<125`, hence

`boxed: |H|<=124.`                                              (4.2)

If `G>=19I/20`, then

`g=(1-sqrt((1/5)/(19/20)))/2
  =1/2-1/sqrt(19)`.                                             (4.3)

Using the safe source values in (1.3),

`m
 >(19/20)(1/2-1/sqrt(19))(1597/2000)-403/2000
 =14223/80000 -1597 sqrt(19)/40000`.                            (4.4)

This is strictly larger than `3/800`. Indeed (4.4) minus `3/800` is positive exactly when

`13923>3194 sqrt(19)`,                                          (4.5)

and

`13923^2=193849929 >193831084=19*3194^2`.                      (4.6)

Therefore the full ambient form is paid by

`boxed:
 ||p_Q||_infinity
 < (800/3) C_*
 =2254.1389934741805... <2255`,                                 (4.7)

with a continuous `C_0` density. Using the actual margin in (4.4), rather than only `m>3/800`, gives

`C_*/m =2249.065294606407...`.                                  (4.8)

If this payment does not apply, then the same physical heavy set, still of size at most `124`, obeys

`boxed: there exists unit z with ||U_H z||^2>1/20.`             (4.9)

So the fleet01/B20 physical-heavy-carrier survivor has been sharpened:

`QFORM-R5-HEAVYSET-DELETE-OR-CROSS-E3-v1` — either the formerly heavy rank-five carrier is already paid continuously by `<2255`, or at most 124 heavy original coordinates collectively contain more than five percent of one genuine carrier direction.

This is a strict enlargement of the old `max_i ell_i<=1/25` paving region: individual leverage may exceed `1/25` and the new branch can still pay as long as the total carrier operator captured by those heavy rows stays below `1/20`.

The statement does **not** yet pay the complementary concentrated-hub case (4.9), and it does not identify the latest threshold-Schur matrix with a random quadratic coefficient. Those are the remaining bridges.

## 5. Explicit genuinely rotated indefinite example beyond the old leverage gate

This example makes the strict enlargement concrete.

Let physical rows be indexed by `x in F_2^7`, so `N=128`. Start with the three orthonormal Walsh columns

`U0(x)=128^(-1/2) (1, (-1)^(x_1), (-1)^(x_2))`.                (5.1)

The rows at `x=0` and `x=e_3` are identical. Let `theta` satisfy

`sin(2 theta)=3/4`,                                              (5.2)

and apply the `2x2` orthogonal matrix

`[[cos theta, sin theta],[-sin theta,cos theta]]`

to **these two coefficient rows only**, producing a new `128x3` matrix `U`. This is a construction of the coefficient matrix; no random variable is rotated. We still have `U^T U=I_3`.

The physical leverages are exactly

`ell_0=21/512>1/25`,
`ell_{e_3}=3/512`,
`ell_x=3/128` for all other `x`.                                (5.3)

Hence the old `1/25` maximum-leverage gate fails, while the heavy set is exactly `H={0}`. On its complement,

`G=I-u_0u_0^T`,
`lambda_min(G)=1-21/512=491/512`.                               (5.4)

Moreover the largest residual leverage is `beta=3/128`. With `R=3`, Theorem 2.1 gives

`g=1/2-3/sqrt(491)`.                                            (5.5)

Define the genuinely rotated indefinite carrier

`S_*=U diag(2,3/2,-3/2) U^T`                                   (5.6)

and add a dense retained perturbation

`E_*=J_128/2560`, `||E_*||_op=1/20`,
`A_*=S_*+E_*`.                                                   (5.7)

The nonzero carrier eigenvalues are `2,3/2,-3/2`; by Weyl, `A_*` has two positive eigenvalues at least `1.45` and one negative eigenvalue at most `-1.45`, so it satisfies the exact owner spectral hypothesis.

For the residual paving,

`m_*=(491/512)(1/2-3/sqrt(491))(3/2)-1/20
    =1473/2048 -9 sqrt(491)/1024 -1/20
    =0.47448566576616890095...`.                                (5.8)

Therefore every admissible independent cap-one product law satisfies

`boxed:
 ||p_{X^T A_* X}||_infinity
 <= C_*/m_*
 =17.815124534644861... <17.82.`                                (5.9)

The density is continuous and vanishes at infinity. A deterministic matrix check verifies `U^TU=I`, the three leverage values, `lambda_min(G)=491/512`, the target spectrum, and the numerical constant. No Monte Carlo histogram is used.

## 6. Designated partner fleet04/B04 applied at an actual inequality

The completed designated-partner report is

`yspennstate/math-open-problems@3224f273e92d97a8bff7424e9b1191c1e49d0611:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260923T214340Z-fleet04-B04-QFORM-r1/REPORT.md`.

It supplies a literal cross block `M=A[I,J]`, fixed physical row `i`, fixed physical column `j`, and separated anchored third-volume

`J_3^sep(i,j)>delta_p`,

`delta_p=47045881/(12*10^18)`.                                  (6.1)

Every summand is incident to the same row `i`, hence the full incident currency satisfies

`J_i>=J_3^sep(i,j)>delta_p`.                                    (6.2)

Applying the completed incident-third-volume product-Fourier receiver at this actual inequality gives

`boxed:
 ||p_Q||_infinity
 <3*2^(4/3) delta_p^(-1/6)
 =602.011132419117836... <602.012`,                              (6.3)

with a continuous `C_0` density. This is an equation-level application of the designated partner result; it is included here as the required partner consumption, not claimed as a new result of r44.

## 7. Current proof-graph consequence and next edge

The full QFORM conjecture remains OPEN, and full-target continuity remains OPEN separately.

This run removes one avoidable feature of the heavy-carrier frontier: a single physical leverage just above `1/25` is not by itself an obstruction. One may delete the entire bounded heavy set, renormalize the residual frame, and recover a literal cross-`E_3` payment unless that bounded set captures a definite amount of some carrier direction.

The newest B19/B20 source has compressed the global remaining problem further to an all-coordinate-essential threshold-Schur core / source-realization problem. The precise nonduplicate B04 continuation is therefore

`QFORM-ESSENTIAL-SCHUR-SOURCE-REALIZATION-OR-RESIDUAL-PAVING-v1`:

realize the live strong finite threshold carrier as an actual original-coordinate coefficient carrier with a retained operator collar; then apply Theorem 2.1. If the residual paving fails, use the resulting bounded physical hub concentration together with the existing rank-two half-Riesz / square-bank / incident-volume receivers. The Schur operator itself must not be substituted for an actual product-law quadratic coefficient without this realization step.

No scheduler state, task identity, email, notification, public release, paid model/API call, or cross-account authentication is changed by this report.
