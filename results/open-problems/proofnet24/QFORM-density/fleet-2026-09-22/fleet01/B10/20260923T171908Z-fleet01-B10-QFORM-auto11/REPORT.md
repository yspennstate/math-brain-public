SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-23T17:19:08Z.
attacking: the punctured near-coloop bordered pair-times-triple packet; test whether the new grouped projected-crossing theorem can spend the hub-containing third-rank currency before the hub is peeled, and derive the exact obstruction if not.

# fleet01/B10 — optimal-scale one-hub crossing packing and reduction to an ultra-coloop collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T171908Z-fleet01-B10-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / NEW_DISJOINT_VOLUME_PACKING / NEW_CONTINUOUS_DENSITY_BRANCH / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
Execution: `scheduled_automation / WITHOUT_VERIFIED_BRAIN`.

The full arbitrary exact-rank-three theorem and the owner-level three-large-eigenvalue conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. This run proves a new product-preserving random-partition lemma that matches, up to a universal factor, the exact scale of the designated fleet02/B10 one-hub crossing currency. Combining the two closes every diffuse-transverse punctured near-coloop state for which `D^2(1-h)` is bounded below. In the current hard chamber this leaves only the much thinner normalized collar

`D^2(1-h)<2^(-12)`, hence `h>4095/4096`,

together with the already-known near-null condition `|a|D<2^(-12)`. The new theorem gives a **continuous** density on the paid branch. It does not prove a uniform estimate in the residual ultra-coloop limit.

## 1. Fresh source state and inherited hard chamber


Work in the exact-rank-three representation

`A=U M U^T`, `U^T U=I_3`,

where `M` is real symmetric, invertible, and all three eigenvalues have absolute value at least one. Put

`D=|det M|>=1`.

The inherited near-coloop state has one ORIGINAL physical row

`u_0=sqrt(h) r`, `||r||=1`,

with leaves

`u_i=t_i r+p_i`, `p_i perpendicular r`.

Parseval gives

`sum_i t_i^2=1-h`,
`sum_i p_i p_i^T=I_2`,
`sum_i t_i p_i=0`.                                                     (1.1)

Write

`delta=1-h`, `tau_i=||p_i||^2`.

The already-paid transverse-heavy branch allows the live hard chamber to assume

`h>63/64`, `tau_i<1/4` for every leaf.                                (1.2)

The preceding B10 work also reduced the punctured near-null branch to

`0<|a|D<2^(-12)`, `a=r^T M r`,                                          (1.3)

and proved disjoint original-coordinate banks carrying the scale-free pair-times-bordered-triple packet

`W_H T_JK>0.05379357`.                                                   (1.4)

That packet retains the hub in the third-rank volume. The immediate preceding two-hub Schur--Fresnel theorem showed why peeling the hub before spending (1.4) loses exactly the relevant third-rank currency.

## 2. Designated partner input: exact one-hub crossing factorization

The newest completed designated fleet02/B10 report used here is

`yspennstate/math-open-problems@144e391e6a0aed00bb8ded766cf5609d88d260b2`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260923T164541Z-fleet02-B10-QFORM-r11/REPORT.md`.

For any partition of the leaves into disjoint ORIGINAL banks `I` and `J`, define

`S_I=sum_(i in I) p_i p_i^T`,
`G_J=sum_(j in J) u_j u_j^T`.

For the one-hub projected-crossing packet, its exact factorization is

`V_3=h (det M)^2 det(S_I) det(G_J)`.                                    (2.1)

Here `V_3` is the aggregate physical three-volume used by the completed one-hub compiler. Crucially, (2.1) contains no near-null scalar `a` or `q`; degeneration is controlled by the product-frame partition itself.

The compatible completed analytic theorem is fleet01/B03

`QFORM-ONE-HUB-ROW-MARGINAL-FREE-2VOLUME-v1`,

canonical source

`yspennstate/math-open-problems@4b7608c198ea570378ae30b5a22d63ba7d387534`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260923T165124Z-fleet01-B03-QFORM-r29/REPORT.md`.

It removes the volume-row-marginal gate and says that whenever `V_3>0`, the full quadratic polynomial has a continuous `C_0` density and

`||p_Q||_infinity <= C_* V_3^(-1/6)`,                                  (2.2)

where

`C_*=3*2^(7/6)*exp(1/3)=9.39913188784886...`.

Arbitrary internal curvature and affine terms in the theorem's stated packet are allowed; no rotated random coordinates are declared independent.

## 3. New five-row disjoint packing identity

The goal is to force `det(S_I)det(G_J)` quantitatively using only (1.1)-(1.2).

Randomly put every leaf into `I` with probability `theta` and into `J` with probability `1-theta`, independently across ORIGINAL coordinates. By two- and three-dimensional Cauchy--Binet,

`det S_I = sum_(a<b, a,b in I) det(p_a,p_b)^2`,                          (3.1)

and

`det G_J = sum_(c<d<e, c,d,e in J) det(u_c,u_d,u_e)^2`.                 (3.2)

Fix a leaf triple `T={c,d,e}`. The transverse two-volume left after deleting those three original coordinates is

`sum_(a<b, a,b notin T) det(p_a,p_b)^2`
` = det(sum_(i notin T) p_i p_i^T)`
` = det(I_2-S_T)`,                                                       (3.3)

where

`S_T=sum_(i in T)p_i p_i^T`.

Because `S_T` is positive semidefinite and, by (1.2),

`tr S_T=sum_(i in T)tau_i<3/4`,

we get the sharper two-dimensional determinant bound

`det(I_2-S_T)=1-tr S_T+det S_T>1/4`.                                    (3.4)

This is stronger than merely bounding both eigenvalues of `I-S_T` below by `1/4`; the exact determinant identity keeps the positive `det S_T` term.

A disjoint pair `{a,b}` and triple `T` contribute simultaneously to `(det S_I)(det G_J)` precisely when the pair lands in `I` and the triple lands in `J`. The probability is

`theta^2(1-theta)^3`.                                                     (3.5)

Therefore, expanding (3.1)-(3.2), discarding only impossible overlapping pair/triple terms, and then using (3.3)-(3.4),

`E[det S_I det G_J]`
` = theta^2(1-theta)^3 sum_T det(u_T)^2 det(I_2-S_T)`
` > (1/4) theta^2(1-theta)^3 sum_T det(u_T)^2`.                         (3.6)

The final triple sum is again Cauchy--Binet:

`sum_T det(u_T)^2=det(sum_i u_i u_i^T)`
` =det(I-h rr^T)=1-h=delta`.                                            (3.7)

The probability factor is maximized at `theta=2/5`, because

`d/dtheta [2 log theta+3 log(1-theta)]=2/theta-3/(1-theta)`,

so the critical point is `theta=2/5`. Then

`theta^2(1-theta)^3=(2/5)^2(3/5)^3=108/3125`.                          (3.8)

Combining (3.6)-(3.8), some deterministic ORIGINAL-coordinate split satisfies

`boxed: det S_I det G_J > (27/3125)(1-h).`                              (3.9)

No local minor is selected; the statement is an aggregate bank theorem. Every use of independence remains attached to literal original-coordinate banks.

### General form

The same proof gives, whenever `max_i tau_i<=eta<1/3`,

`sup_(I disjoint J, I union J=leaves) det S_I det G_J`
` >= (108/3125)(1-3 eta)(1-h)`.                                        (3.10)

For the live `eta<1/4` chamber, (3.9) is the clean specialization.

## 4. The scale is optimal up to a universal factor

There is also a matching upper bound for every partition. Since

`0<=S_I<=I_2`,

we have

`det S_I<=1`.                                                           (4.1)

Likewise

`0<=G_J<=G_L:=sum_i u_i u_i^T=I-h rr^T`.

For `h<1`, conjugating by `G_L^(-1/2)` gives a positive semidefinite contraction, hence

`det G_J<=det G_L=1-h`.                                                  (4.2)

(The singular endpoint follows by continuity.) Thus for **every** split,

`det S_I det G_J <=1-h`.                                                (4.3)

Applying the designated-partner identity (2.1) gives the two-sided structural scale

`boxed:`
`(27/3125) h D^2(1-h) < sup_(I,J) V_3(I,J) <= h D^2(1-h)`.              (4.4)

This is an important mechanism diagnosis. Within this one-hub projected-crossing architecture, no better partition argument can remove the factor `D^2(1-h)`: the coloop degeneration is genuine for this compiler, not an artifact of the random split. The lower bound is within the universal factor `3125/27<116` of the best possible scale.

## 5. Actual inequality-level application of the designated partner result

Insert (3.9) into fleet02/B10's exact factorization (2.1). For the deterministic split furnished above,

`boxed: V_3 > (27/3125) h D^2(1-h).`                                    (5.1)

This is the required direct application of the designated partner result to an actual inequality.

Now apply the completed row-marginal-free one-hub theorem (2.2): every punctured diffuse-transverse state `0<h<1` in (1.2) has a continuous `C_0` density satisfying

`boxed:`
`||p_Q||_infinity`
` < C_* [(27/3125) h D^2(1-h)]^(-1/6).`                                (5.2)

The estimate is independent of the near-null Rayleigh scalar `a`. Thus the partner's observation that near-nullness itself does not degrade the one-hub crossing currency is now converted into a uniform deterministic partition theorem.

### Universal payment outside the ultra-coloop scale

In the inherited hard chamber `h>63/64`. If

`D^2(1-h)>=2^(-12)`,                                                     (5.3)

then (5.1) gives

`V_3 > (27/3125)(63/64)2^(-12)`
` =1701/819200000`.                                                      (5.4)

Hence

`||p_Q||_infinity`
` < C_* (819200000/1701)^(1/6)`
` =83.2150762187...`.                                                    (5.5)

Therefore

`boxed: D^2(1-h)>=2^(-12)  ==>  ||p_Q||_infinity<83.216`,                (5.6)

and the density is continuous and vanishes at infinity.

This closes an actual previously-unpaid punctured near-coloop branch. No moment, support, log-concavity, Gaussianity, iid law, or diagonal-basis assumption enters.

## 6. Exact description of the remaining ultra-coloop survivor

After (5.6), the still-unpaid part of the present B10 hard chamber may be restricted to

`D^2(1-h)<2^(-12)`.                                                      (6.1)

Since `D>=1`, this immediately strengthens the geometric hub condition to

`1-h<2^(-12)`,

hence

`boxed: h>4095/4096`.                                                    (6.2)

Together with the earlier punctured near-null reduction (1.3), the survivor has the simultaneous normalized smallness

`|a|D<2^(-12)`,
`D^2(1-h)<2^(-12)`.                                                      (6.3)

There is also a useful deterministic coefficient consequence. From (1.1),

`sum_i ||M(t_i r)||^2 = ||Mr||^2 sum_i t_i^2`
` =||Mr||^2(1-h)`.                                                       (6.4)

All singular values of `M` are at least one, so `||M||_op<=D`; hence

`boxed: sum_i ||M(t_i r)||^2 <=D^2(1-h)<2^(-12).`                       (6.5)

Thus, in coefficient space, the entire longitudinal leaf bank is `M`-weighted Frobenius-small while the previous run still supplies the order-one product-preserving certificate

`W_H T_JK>0.05379357`.                                                   (6.6)

Equation (6.5) is **not** used as a probabilistic perturbation estimate: arbitrary cap-one input laws can have unbounded support, so small deterministic coefficients do not imply a small random quadratic error. It is recorded only as exact geometry for the next phase-retaining receiver.

## 7. Why this does not yet spend the bordered packet

The new one-hub compiler necessarily uses a full three-dimensional **leaf-only** Gram on its column bank. Its exact currency has the unavoidable upper bound

`V_3<=hD^2(1-h)`.                                                        (7.1)

By contrast, the prior scale-free packet (6.6) uses bordered triples containing the hub. Therefore in the survivor (6.1), every one-hub projected-crossing currency is small even though the hub-containing bordered-triple currency remains order one. This proves that the two currencies are genuinely different, not merely differently normalized versions of the same quantity.

Accordingly, repeatedly optimizing the one-hub split cannot finish the limit `h->1`. The mechanism must now change while staying on the same target: retain the hub phase long enough to spend the bordered triple packet before converting to a leaf-only full-rank Gram.

## 8. First unpaid implication after this run

The first unpaid B10 implication is now

`QFORM-ULTRACOLOOP-PHASE-RETAINING-BORDERED-RECEIVER-v1`:

> In the exact-rank-three hard chamber with `tau_i<1/4`, `|a|D<2^(-12)`, and `D^2(1-h)<2^(-12)`, use the already-proved disjoint original-coordinate packet `W_H T_JK>0.05379357` to obtain a universal linear small-ball or `L^1_t` estimate **before** the hub-containing third-rank phase is converted into a leaf-only Gram. Arbitrary within-bank curvature, longitudinal leakage, fragmented/unbounded cap-one laws, and both indefinite signs must remain allowed.

The exact endpoint `h=1` and the punctured branch cannot be joined merely by continuity of random outputs. The source-valid route should instead combine the order-one bordered packet (6.6) with a Fresnel/Plancherel step whose constants are stable under the deterministic coefficient geometry (6.3)-(6.5). The fleet02/B10 discriminant calculation also shows that hub-first absolute negative-half-power integration can lose a logarithm as the near-null scalar tends to zero, so that route remains excluded.

## 9. Scope and regularity

- New packing theorem (3.9)/(4.4): **proved supporting structural theorem**.
- New density theorem (5.2): **proved supporting analytic consequence**, conditional only on the already-isolated transverse-diffuse hub geometry; density is continuous `C_0`.
- Universal branch (5.6): **closed**, with explicit bound `<83.216`.
- Remaining ultra-coloop branch (6.1)-(6.6): **OPEN**.
- Arbitrary exact-rank-three theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, or post-rotation-independence assumption has been added.

## 10. Source ledger

Fresh control before publication:

Designated fleet02/B10 result actually applied:
`yspennstate/math-open-problems@144e391e6a0aed00bb8ded766cf5609d88d260b2`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260923T164541Z-fleet02-B10-QFORM-r11/REPORT.md`.

Row-marginal-free analytic compiler:
`yspennstate/math-open-problems@4b7608c198ea570378ae30b5a22d63ba7d387534`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260923T165124Z-fleet01-B03-QFORM-r29/REPORT.md`.

Immediate B10 predecessors:
`yspennstate/math-open-problems@79295a936c9f88cf9356c6ed5d52090fa1cedc37`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B10/20260923T152129Z-fleet01-B10-QFORM-auto11/REPORT.md`,
and
`yspennstate/math-open-problems@591cf390780c8acf7e3dfac2ea7195ba56552276`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B10/20260923T160221Z-fleet01-B10-QFORM-auto11/REPORT.md`.

Newest Claude continuation checked but not used as a proved missing bridge:
`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`,
`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md` and associated single-hub notes; its `(SP)` remains proposed/open.

Repository transport is not native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
