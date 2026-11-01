Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations remain `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical positive-route `2/4` is only the frozen handoff value. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, I prove that every coordinatewise-comparable second contact and every one-sign Hessian-null direction collapses to the already identified exceptional subset-flat case; hence every genuinely isolated first bifurcation must be mixed-sign. Methods #3 PROVE SOMETHING STRONGER, #25 COUNT THE SAME THING TWICE, #26 HUNT THE SPORADIC CASE.**

# R15 retained screen — sign-definite bifurcation rigidity for the quadratic `k=2` Talagrand hazard

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 from PENDING/NOT READY, establish publication novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Required repository recovery, ownership, source fidelity, and exclusions

I continued from

`runs/R15/20260919_1158Z_successor_screen_f0111_subset_bifurcation_v82m.md`

rather than restarting. Before new mathematics I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the I0076 six-run handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

the newest own report above, the neighboring R20 F0111 handoff, and current successor-gate evidence. The newest neighboring gate report I could recover in this run was

`runs/R02/20260919T1208Z_successor_gate_kressner_owned_p0157_reassigned_3_6_11_3f7c9a12.md`.

Its changed-claims reconciliation found no canonical release into the CLOSABLE pool: the newly READY+CLOSABLE item it saw was claimed at creation, and the other relevant reassignment was HARD. I therefore found no lawful free READY+CLOSABLE successor for R15 and created no successor claim.

### I0076 source rechecked exactly

I re-opened Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), including Definition 2.1 and the page containing Problem 7.2.

The exact source notions are:

- FBM: there are random origins `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random origin `S` for which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2: `X` is FBM and BBM and there exists an arbitrary random time `T` such that the two complete centered half-processes `(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}` are independent. Must `X` be 2BM?

There is no stopping-time hypothesis on `T`, no deterministic-time substitute, and neither half at `T` is separately assumed Brownian. Problem 7.5 is a different problem and remains excluded.

The controlling I0076 handoff remains unchanged. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but R15 eliminated source-valid independent seam existence; the later Brownian-prefix/BES candidate has exact seam independence but R15 proved it is actually 2BM. Thus no frozen counterexample candidate survives and the source metric cannot honestly be advanced by scoring obligations on a nonexistent candidate.

Fresh public searches dated 2026-09-19 used the exact title/arXiv ID, author names, `Problem 7.2`, and resolution/citation terms. They recovered the original paper and related references but no accessible later primary source explicitly claiming a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

### F0111 source and current literature rechecked

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9. The original source was rechecked, along with fresh 2026-09-19 searches for `Problem 10.9`, `discrete convexity`, `k-threshold`, and the current 2026 papers.

The current primary items recovered were:

- Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulating the discrete Convexity Conjecture via `k`-thresholds and proving substantial classes;
- Chen Li, arXiv:2609.08967 (2026-09-08), resolving the **fractional** version;
- Jinyoung Park, arXiv:2609.14681 (2026-09-13), obtaining a dimension-independent bound **toward** the conjecture;
- Fang--Wang, arXiv:2609.18458 (2026-09-16), a note using Li's method to answer a different Talagrand problem.

None of the retrieved primary statements claims Talagrand's exact Problem 10.9 or the quadratic contact/bifurcation theorems below. Negative search evidence does not certify novelty; novelty remains `UNVERIFIED`.

The preceding R15 run used #5/#18/#30. The full 30-move inventory has already been exhausted over the longer F0111 screening history, so this run uses a nonconsecutive fresh triple relative to the immediately preceding run: #3/#25/#26.

## 2. Carried setup and the previous first-bifurcation reduction

For the cardinality-two threshold hazard, write

`F(t)=F_n(t)=sum_i t_i - log S(t)`,

`S(t)=sum_i exp(t_i)-(n-1)`,                                 (2.1)

for `t in R_+^n`, `n>=2`.

A quadratic positive polynomial is

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,

with `A_i,B_ij>=0`.                                          (2.2)

A global quadratic certificate at an interior base `q` means

`P(t)>=F(t)` for all `t>=0`, and `P(q)=F(q)`.                (2.3)

Because `q` is interior and `P-F>=0`, value contact implies gradient contact there.

The previous R15 runs established the following package, used here without re-derivation.

1. The interior quadratic `gamma=1` certificate-base set is relatively closed.
2. If a boundary certificate has only zeros `{0,q}` and `Hess(P-F)(q)` is positive definite, it can be strictified and continued, so every boundary certificate must display at least one of:
   - a singular contact Hessian; or
   - another global contact point.
3. If `q,t` are two distinct interior contacts and `h=t-q`, then the coefficient-free Hermite condition holds:

`2(F(t)-F(q))=<h,grad F(t)+grad F(q)>`,                       (2.4)

or equivalently

`integral_0^1 s(1-s) D_h^3F(q+s h) ds=0`.                   (2.5)

4. If `h!=0` is a null direction of `Hess(P-F)(q)`, then

`D_h^3F(q)=0`, `D_h^4F(q)<=0`.                               (2.6)

5. For a subset-constant direction `h=c 1_J`, writing

`A_J=sum_{i in J} exp(q_i)`,

`C_J=sum_{i notin J} exp(q_i)-(n-1)`,                        (2.7)

an additional contact or a null-Hessian direction is impossible unless `C_J=0`; in that exceptional case the relevant internal pair coefficients vanish and the **entire feasible subset line is contact**. The alternative null-cubic case `C_J=A_J` is excluded by a positive fourth derivative.

The previous cursor proposed attacking two-block directions. The stronger route below first proves that *all sign-definite directions*, not only one-block directions, already collapse to the exceptional subset-flat case.

## 3. Method #3 — prove something stronger: comparable second contacts are rigid

### Theorem R15-F0111-COMPARABLE-CONTACT-RIGIDITY

Let `P>=F` be a nonnegative quadratic global certificate. Suppose `q,t in (0,infinity)^n` are two distinct contacts of the same `P` and are coordinatewise comparable. Then, after possibly swapping `q` and `t`, there is a nonempty subset `J` and a scalar `L>0` such that

`t-q=L 1_J`,                                                  (3.1)

and necessarily

`sum_{i notin J} exp(q_i)-(n-1)=0`.                           (3.2)

Consequently the second contact is not isolated: every feasible point on the line `q+s L 1_J` is a contact. In particular, **no isolated additional contact can have a one-sign displacement**.

### Proof

Assume `q<=t` coordinatewise and put

`h=t-q>=0`, `h!=0`.                                           (3.3)

Let

`S_s=S(q+s h)`, `ell(s)=log S_s`, `L=ell(1)-ell(0)`.         (3.4)

Since some coordinate increases strictly, `S_1>S_0`, so `L>0`.

At both interior contacts the gradients of `P` and `F` agree. For every coordinate `i`,

`partial_i P(t)-partial_iP(q)=sum_{j!=i}B_ij h_j>=0`.        (3.5)

Now

`partial_iF(x)=1-exp(x_i)/S(x)`.                              (3.6)

Thus (3.5) gives

`exp(t_i)/S_1 <= exp(q_i)/S_0`,                               (3.7)

and therefore

`0<=h_i<=L` for every `i`.                                    (3.8)

The two-contact Hermite identity (2.4) can be written entirely in terms of `ell`. Since

`F(q+s h)=sum_i(q_i+s h_i)-ell(s)`,                           (3.9)

(2.4) is exactly

`ell'(0)+ell'(1)=2L`.                                         (3.10)

The remainder of the proof turns (3.10) into a positive sum with completely classified equality.

## 4. Method #25 — count the same endpoint identity twice

Let

`a_i=exp(q_i)`, `C=n-1`,

`b_i=a_i/S_0>0`, `c=C/S_0>0`,

`d_i=L-h_i in [0,L]`.                                        (4.1)

Normalize the partition function by the chord joining its endpoint logarithms:

`M(s)=exp(-Ls) S_s/S_0`

`    =sum_i b_i exp(-d_i s)-c exp(-Ls)`.                      (4.2)

By definition of `L`,

`M(0)=M(1)=1`.                                                (4.3)

First use (4.3) itself. Subtracting the two endpoint values gives

`sum_i b_i(1-exp(-d_i))=c(1-exp(-L))`.                        (4.4)

Second differentiate (4.2) at both endpoints:

`M'(0)+M'(1)`
`=cL(1+exp(-L))-sum_i b_i d_i(1+exp(-d_i))`.                 (4.5)

Use (4.4) to eliminate `c`. With

`g(x)=x coth(x/2)` for `x>0`, and `g(0)=2`,                  (4.6)

we obtain the exact positive-sum identity

`M'(0)+M'(1)`
`=sum_i b_i(1-exp(-d_i)) [ g(L)-g(d_i) ]`.                   (4.7)

But `M'(0)=ell'(0)-L` and `M'(1)=ell'(1)-L`, so the Hermite equality (3.10) is exactly

`M'(0)+M'(1)=0`.                                              (4.8)

The key monotonicity is elementary:

`g'(x)=(sinh x-x)/(2 sinh^2(x/2))>0` for every `x>0`.         (4.9)

Therefore each summand in (4.7) is nonnegative, and it is strictly positive whenever

`0<d_i<L`.                                                    (4.10)

Equality in (4.8) forces every `d_i` to lie in `{0,L}`. Equivalently,

`h_i=L-d_i in {0,L}` for every `i`.                           (4.11)

Since `h!=0`, there is a nonempty subset `J` with

`h=L 1_J`.                                                    (4.12)

The previous subset-direction theorem now applies. It says this second contact is impossible unless `C_J=0`, and when `C_J=0` the whole feasible line is contact and all internal `B_ij` on `J` vanish. This proves the theorem when `q<=t`. If `t<=q`, swap the endpoint names and apply the same argument. QED.

### What is genuinely stronger here

The previous run only classified displacements which were *assumed in advance* to have equal nonzero coordinates on one subset. The theorem above starts with an **arbitrary heterogeneous vector `h>=0`** and proves, from global majorization plus the endpoint contact equations alone, that it must collapse to exactly that subset-constant form.

Thus an isolated second-contact bifurcation, if one exists, must join **incomparable** points: its displacement must contain at least one positive and at least one negative coordinate.

## 5. Method #26 — hunt the sporadic equality case for Hessian nullity

The second first-bifurcation mechanism also has a complete sign-definite classification.

### Theorem R15-F0111-ONESIGN-NULL-RIGIDITY

Let `P>=F` be a nonnegative quadratic global certificate with an interior contact `q`. Suppose `h!=0` is a null vector of the positive semidefinite contact Hessian

`Hess(P-F)(q) h=0`,                                           (5.1)

and all coordinates of `h` have the same weak sign. Then, after replacing `h` by `-h` if needed, there is a nonempty subset `J` and `m>0` such that

`h=m 1_J`.                                                    (5.2)

The previous subset-null classification then implies that the only possible case is the exceptional flat hypersurface

`sum_{i notin J}exp(q_i)-(n-1)=0`,                            (5.3)

and in that case the whole feasible subset line is contact. Hence **no isolated Hessian-singularity bifurcation can have a one-sign null vector**.

### Proof

Assume `h>=0`. Put

`r_i=exp(q_i)/S(q)>0`,

`m=sum_i r_i h_i`.                                            (5.4)

Since `h` is nonzero and all `r_i>0`, `m>0`.

The `i`-th component of the null-Hessian equation is, after cancellation of the rank-one terms,

`sum_{j!=i} B_ij h_j = r_i(m-h_i)`.                           (5.5)

The left side is nonnegative because `B_ij,h_j>=0`. Hence

`0<=h_i<=m` for every `i`.                                    (5.6)

Set

`x_i=h_i/m in [0,1]`.                                         (5.7)

By the definition of `m`,

`sum_i r_i x_i=1`.                                            (5.8)

The carried local null condition (2.6) requires `D_h^3F(q)=0`. With

`M_k=sum_i r_i h_i^k`,                                        (5.9)

we have

`D_h^3F(q)=-(M_3-3M_1M_2+2M_1^3)`.                          (5.10)

Since `M_1=m`, substitute `h_i=m x_i` and use (5.8):

`M_3-3mM_2+2m^3`
`=m^3 sum_i r_i (x_i^3-3x_i^2+2x_i)`
`=m^3 sum_i r_i x_i(1-x_i)(2-x_i)`.                          (5.11)

Every summand is nonnegative on `[0,1]`, and because every `r_i>0`, equality occurs only when

`x_i in {0,1}` for every `i`.                                 (5.12)

The required cubic equality therefore forces

`h=m 1_J`                                                     (5.13)

for a nonempty subset `J`. The previous subset-null theorem now applies. Its cubic alternatives were `C_J=0` or `C_J=A_J`; the latter has

`D_h^4F(q)=m^4/8>0`,                                         (5.14)

contradicting the necessary local condition `D_h^4F(q)<=0`. Thus only `C_J=0` survives, and there the internal pair coefficients vanish and the whole feasible subset line is contact. This proves the claim for `h>=0`. If `h<=0`, replace `h` by `-h`; kernel membership is unchanged and the cubic-zero condition is sign-insensitive at zero. QED.

## 6. New first-bifurcation normal form

Combining Sections 3--5 with the previous first-bifurcation theorem gives a substantially smaller obstruction class.

### Corollary R15-F0111-MIXEDSIGN-FIRST-BIFURCATION

At a genuinely isolated boundary phenomenon for the quadratic `k=2`, `gamma=1` certificate region:

1. every displacement from the base contact to a second isolated interior contact must have **mixed signs**;
2. every null vector of a singular contact Hessian must have **mixed signs**.

Any sign-definite candidate mechanism is impossible unless it lands on an exceptional subset hypersurface (5.3), where it degenerates into a continuum of contacts rather than an isolated first bifurcation.

This removes a large cone of possible directions without assuming symmetry. The next useful reduction is no longer an arbitrary two-block search; it is specifically the **mixed-sign two-block** family

`h=c_1 1_J-c_2 1_{J^c}`, `c_1,c_2>0`,                        (6.1)

followed, if necessary, by a sign-pattern extremal argument showing that a general mixed-sign obstruction may be compressed to two levels.

That is a materially sharper cursor than the previous run's unrestricted two-block suggestion.

## 7. Why no checker was manufactured

No finite arithmetic claim is introduced in this run. The new movement consists of all-parameter analytic identities, equality cases, and sign arguments. A grid or floating-point sample would not certify either theorem and would violate the instruction to use checking only after an idea worth checking exists. The relevant exact identities are proved symbolically on the page.

## 8. Status and scope discipline

Nothing here resolves Burdzy--Scheutzow Problem 7.2. Its fixed source metric does not move because there is no surviving frozen counterexample candidate; the source remains `OPEN / PARTIAL / RETIRED-HANDOFF` under this worker's protocol.

Nothing here resolves Talagrand Problem 10.9. The result concerns only the retained `k=2` quadratic `gamma=1` contact program and remains `SELF_CHECK_ONLY / NOT CLAIMED / PENDING`. The source asks for a universal statement across the full threshold family, and the current 2026 literature still presents the broader discrete convexity program as incomplete.

## 9. Model/scheduler and denied-task boundary

The implementation status is unchanged. The exposed scheduler/task surface records prompt/title, schedule/timing, enabled state and notification controls, but it exposes no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution setting. Therefore `GPT-6 / maximum` remains a prompt request only, and this report honestly records the actual available identity as GPT-5.6 Sol with reasoning `UNVERIFIED`.

The historical P26 scheduler ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context. That boundary was not bypassed and no duplicate schedule was created. Later repository evidence records that P26 could be updated from a different authorized P/C context. Thus the workaround is an actually authorized owner/admin context; it is not permission circumvention. Enforcing a model/reasoning choice itself still requires a product/backend/API surface that exposes and persists those routing fields.

No scheduler change, email, Drive write, public posting, purchase, permission change, or shared-root edit was attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R15
  lane: CLOSABLE_OUTSIDE
  native_source:
    id: I0076
    source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
    fixed_metric: "number of four source-matching obligations proved for one frozen counterexample candidate: FBM, BBM, source seam independence at an arbitrary random time, failure of 2BM"
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_handoff_value: "2/4 positive-route gates; not a live frozen-candidate score"
    status: OPEN_PARTIAL_RETIRED_HANDOFF
    unchanged_count: "frozen at mandatory six-run rotation"
  retained_screen:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    admission: PENDING_NOT_READY_NOT_CLAIMED
    before: "subset-constant second-contact/null directions classified"
    after: "all coordinatewise-comparable second contacts and all one-sign Hessian-null directions classified; isolated first bifurcations forced mixed-sign"
    status: SELF_CHECK_ONLY_PARTIAL
  tried_moves:
    - 3
    - 25
    - 26
  remaining_obligation: "No free READY+CLOSABLE successor is available; for retained F0111, classify mixed-sign first-bifurcation directions, starting with the two-block family and preserving source scope."
  evidence:
    - R15-F0111-COMPARABLE-CONTACT-RIGIDITY
    - R15-F0111-ONESIGN-NULL-RIGIDITY
    - R15-F0111-MIXEDSIGN-FIRST-BIFURCATION
  audits: []
  closure_claimed: false
```

## 11. Next three methods if this retained screen remains the only lawful work

The next nonconsecutive triple should be:

- **#14 FIND THE GROUP ACTING**: quotient a mixed-sign direction by permutations within its positive and negative level sets;
- **#24 FIND THE EXTREMAL OBJECT**: for fixed positive/negative masses, show the Hermite/null obstruction is extremized by a two-level displacement if possible;
- **#11 DUALIZE**: combine the mixed-sign moment conditions with the weighted-graph contact equations to seek a separating inequality.

If a free source-valid READY+CLOSABLE successor is admitted before the next invocation, the worker should claim that source create-only instead of continuing F0111.