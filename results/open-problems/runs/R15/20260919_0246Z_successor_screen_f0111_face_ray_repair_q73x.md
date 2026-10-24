Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; there is no surviving frozen counterexample candidate, so the original four-obligation candidate metric is not presently scoreable. The handoff's post-switch `2/4` positive-route value remains frozen and is not a live-candidate score. `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: on Talagrand F0111, a new exact coordinate-face ray gate **refutes the previous curvature-sparing quadratic contact even though it passes positivity, exact value/gradient contact, and the complete local SDP/Hessian gate**; a one-parameter `theta=4/5` redistribution repairs that failure mode while preserving strict local PSD and additionally certifies every two-small-coordinate face plus the entire previously failing homogeneous small-coordinate ray. Methods #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #19 MAKE IT AN ALGORITHM, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# R15 retained screen — the global face-ray obstruction and a curvature-budget repair

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All Talagrand mathematics below is **SELF_CHECK_ONLY**. Nothing here reopens Burdzy–Scheutzow Problem 7.2 after its mandatory six-run handoff, promotes F0111 from `PENDING / NOT READY`, claims publication novelty, or satisfies the fleet closure/audit standard.

## 1. Continuity, source fidelity, exclusions, and admission

I continued from the newest complete own report

`runs/R15/20260919_0227Z_successor_screen_f0111_rankone_sdp_z72w.md`

rather than restarting. Before new mathematics I recovered the campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the current coordinator/task-health admission evidence, the I0076 six-run handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

and the newest visible neighboring Burdzy--Scheutzow track state (I0077 remains separately owned by R07).

The current strict admission evidence still says

`E_READY_CLOSABLE: 0 -> 0`.

No free source-current ownership-clear CLOSABLE successor was admitted. I therefore created no claim and edited no shared root.

I rechecked the primary Burdzy--Scheutzow PDF itself. Definition 2.1 says that FBM means existence of random origins tending to `-infinity` from each of which the complete centered future is standard Brownian; BBM is the time-reversal notion; 2BM requires one random origin whose centered future and centered past are **independent standard Brownian motions**. Problem 7.2 assumes FBM + BBM and merely independence of the two complete centered half-paths at an arbitrary random time `T`. It does **not** assume that `T` is a stopping time and does not separately assume that either seam half is Brownian. Problem 7.5 remains distinct and excluded.

The controlling six-run handoff is unchanged. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES candidate had FBM, BBM and an exact independent seam but was proved actually to be 2BM. There is no live frozen candidate on which a third or fourth source obligation can honestly be scored, so I do not manufacture a seventh I0076 lemma.

Fresh dated public-web searches on 2026-09-19 recovered the original Problem 7.2 source/citation trail but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only.

## 2. Carried retained screen: heterogeneous `k=2`

For Talagrand's cardinality-two threshold,

`F(t)=F_{n,2}(t)=sum_i t_i - log S(t)`,
`S(t)=sum_i exp(t_i)-(n-1)`.                                  (2.1)

At an interior base `q`, write

`r_i=exp(q_i)/S(q)`,
`z_i=q_i r_i`,
`m_i=q_i(1-r_i)`,
`D=sum_i m_i=<q,grad F(q)>`,
`W=D-F(q)`.                                                    (2.2)

The carried quadratic contact equations are

`a_i + sum_{j!=i} e_ij = m_i`,                                (2.3)
`sum_{i<j} e_ij = W`,                                         (2.4)

with all contact masses nonnegative. In normalized coordinates `t_i=q_i x_i`, any global quadratic exact-contact majorant must also pass

`M_ii=d_i:=q_i^2 r_i(1-r_i)`,
`M_ij=e_ij-z_i z_j`,
`M >= 0`.                                                      (2.5)

The preceding run killed the rank-one point of this cone and then isolated a different **curvature-sparing** contact on the two-level family

`q^(epsilon)=(epsilon,...,epsilon,b,b)`,
`m=14`, `b=log 2`.                                             (2.6)

For the fourteen small coordinates and two big coordinates it sets

`e_ss=z_s^2`,
`e_sb=z_s z_b`,
`e_bb=W-C(14,2)z_s^2-28 z_s z_b`,                             (2.7)

and obtains singleton masses from (2.3). The previous report proved that, for sufficiently small positive `epsilon`, all coefficients are positive and the Hessian gate (2.5) is **strictly** positive definite. Global majorization was left open.

This run tests exactly that remaining claim.

---

## 3. Method #19 — turn global verification into a gate cascade

The local SDP gate is not the last gate. A global positive quadratic majorant must remain a majorant after arbitrary coordinates are set to zero.

### Lemma R15-F0111-FACE-RAY

Suppose a positive quadratic polynomial

`P(t)=sum_i alpha_i t_i + sum_{i<j} beta_ij t_i t_j`

globally majorizes `F_{n,2}`. Suppose a coordinate subset `A` of size `m` has common singleton coefficient `alpha` and common within-`A` pair coefficient `beta`. Then for every `x>=0`,

`m alpha x + C(m,2) beta x^2`
` >= m x - log(1+m(exp(x)-1))`.                               (3.1)

Equivalently, every such global majorant must satisfy the exact one-dimensional gate

`beta >= B_m(alpha)`,

where

`B_m(alpha):=sup_{x>0}`
` [m x-log(1+m(exp(x)-1))-m alpha x] / [C(m,2)x^2]`.          (3.2)

**Proof.** Set every coordinate outside `A` equal to zero and every coordinate in `A` equal to `x`. The restriction of `F_{n,2}` is exactly `F_{m,2}(x 1_m)`, while the restriction of `P` is the left side of (3.1). QED.

This gives a useful gate cascade for candidate quadratic contacts:

1. nonnegative contact masses and exact value/gradient contact;
2. the local Hessian/SDP gate `M>=0`;
3. coordinate-face ray gates such as (3.1);
4. only after those survive, genuinely asymmetric multi-coordinate directions.

The previous curvature-sparing point passes gates 1 and 2. It fails gate 3.

---

## 4. Method #16 — exact refutation on the `m=14` small-coordinate face

For the curvature-sparing contact (2.7), as `epsilon ->0+`,

`S(q^(epsilon)) ->3`,
`r_s ->1/3`, `r_b ->2/3`,
`z_s/epsilon ->1/3`, `z_b ->2b/3`.                            (4.1)

Its coefficients on a small coordinate and small-small pair therefore satisfy

`alpha_s(epsilon) -> alpha_*:=2/3-(4/9)b`,
`beta_ss(epsilon) -> 1/9`.                                    (4.2)

Choose the exact ray point

`x=log(4/3)`.                                                  (4.3)

For fourteen active small coordinates,

`F_{14,2}(x 1_14)=14x-log(17/3)`.                             (4.4)

The limiting polynomial-minus-target gap is

`H_0`
` =14 alpha_* x + (91/9)x^2 - [14x-log(17/3)]`
` =-(14/3)x -(56/9)(log2)x +(91/9)x^2 + log(17/3).           (4.5)

### Exact sign certificate

I wrote and executed

`artifacts/R15/f0111_face_ray_checker_q73x.py`

and archived its output at

`artifacts/R15/f0111_face_ray_checker_q73x.out`.

The checker uses the positive atanh series

`log y = 2 sum_{k>=0} z^(2k+1)/(2k+1)`,
`z=(y-1)/(y+1)`,                                              (4.6)

with a rational geometric tail bound. Four retained terms already give the rigorous upper bound

`H_0 <`
` -224692498610469256178897`
` /23828794566053057595000000`
` <0`.                                                        (4.7)

The archived output ends `ALL_EXACT_CHECKS_PASS`.

By continuity in `epsilon`, for every sufficiently small positive `epsilon`, the **actual interior** curvature-sparing contact satisfies

`P_epsilon(x,...,x,0,0) < F_{16,2}(x,...,x,0,0)`.            (4.8)

### Theorem R15-F0111-SDP-NOT-SUFFICIENT

There exist fully interior heterogeneous bases at which a positive quadratic polynomial has exact value and gradient contact with `F_{n,2}` and passes the complete local Hessian/SDP gate **strictly**, yet is not a global majorant.

The family above gives such examples for `n=16` and sufficiently small `epsilon>0`.

This is qualitatively stronger than the preceding rank-one no-go: the new counterexample survives every zeroth-, first-, and second-order contact test before failing on a genuine many-coordinate global direction.

---

## 5. The same curvature-matching strategy fails in arbitrarily high dimension

The `m=14` example is not sporadic. Keep two big coordinates equal to `b=log2`, use `m` small coordinates, retain the unmodified curvature-sparing rule `e_ss=z_s^2`, and test the small homogeneous face at

`x=4/m`.                                                        (5.1)

First let `epsilon ->0+`, then `m->infinity`. From (4.2),

`m alpha_* x ->4 alpha_*`,
`C(m,2)(1/9)x^2 ->8/9`,                                      (5.2)

while

`F_{m,2}((4/m)1_m)`
` =4-log(1+m(exp(4/m)-1)) ->4-log5`.                         (5.3)

Hence the limiting gap is

`H_infty = log5 -4/9 -(16/9)log2`.                            (5.4)

It is strictly negative. Indeed `H_infty<0` is equivalent to

`5^9 < e^4 2^16`.                                             (5.5)

The exact checker certifies

`e^4 > 103/3 >30`,
`5^9=1953125 <1966080=30*2^16`.                              (5.6)

Therefore the unmodified `e_ss=z_s^2` curvature-matching architecture fails the global face-ray gate for **all sufficiently large `m`**, at sufficiently small positive `epsilon` for each such `m`.

The lesson is structural: matching the mixed Hessian entry `z_s^2` edge-by-edge is locally natural but globally underprices the coherent motion of many tiny coordinates.

---

## 6. A repaired contact: spend a controlled fraction of diagonal curvature

The failure itself suggests the repair. The small-coordinate diagonal curvature is

`d_s=epsilon^2 r_s(1-r_s)`.                                  (6.1)

For a parameter `0<theta<1`, modify only the small-small pair masses to

`e_ss^(theta)=z_s^2+theta d_s`,                               (6.2)

keep

`e_sb=z_s z_b`,                                               (6.3)

and restore the exact pair budget by

`e_bb^(theta)`
` =W-C(m,2)e_ss^(theta)-2m e_sb`.                             (6.4)

Singleton masses are again defined from the exact degree equations (2.3).

I freeze

`theta=4/5`.                                                   (6.5)

### 6.1 Exact contact, positivity, and strict local PSD survive

The value/gradient contact equations hold identically by construction. At fixed `m=14`, the change in total pair mass relative to the preceding candidate is only `O(epsilon^2)`. Thus the limiting singleton and big-big masses are unchanged and remain strictly positive; consequently all coefficients stay positive for sufficiently small `epsilon`.

The Hessian has an especially simple block form. Inside the small orbit,

`M_ii=d_s`,
`M_ij=theta d_s` for `i!=j`.                                  (6.6)

Its eigenvalues are

`d_s(1-theta)` with multiplicity `m-1`,
`d_s(1+(m-1)theta)` on the all-ones vector,                    (6.7)

both strictly positive for `theta=4/5`. The small-big Hessian entries remain exactly zero because `e_sb=z_s z_b`. The big `2x2` block changes from the preceding strictly-positive block by only `O(epsilon^2)`, and its singular-limit smaller eigenvalue remains the strictly positive quantity proved in the preceding report. Hence the whole Hessian is strictly positive definite for sufficiently small `epsilon`.

So the repair remains inside the local spectrahedral contact cone.

### 6.2 Every two-small-coordinate face is now globally certified

The limiting small-small quadratic coefficient is

`beta_ss -> 1/9 +(4/5)(2/9)=13/45`,                           (6.8)

while the limiting singleton coefficient remains

`alpha_* =2/3-(4/9)log2`.                                    (6.9)

Therefore

`2 alpha_* +13/45 = (73-40 log2)/45 >1`,                    (6.10)

because `log2<7/10`. The checker certifies this last elementary bound by the exact Taylor inequality

`e^(7/10) > 12013/6000 >2`.                                  (6.11)

By continuity, for all sufficiently small positive `epsilon`, the actual two-small-coordinate coefficients `A=B=alpha_s(epsilon)`, `C=beta_ss(epsilon)` obey

`A+B+C>1`.                                                     (6.12)

The following elementary global lemma then applies.

### Lemma R15-F0111-PAIR-CONE

For all `u,v>=0`,

`Phi(u,v):=F_{2,2}(u,v) <= min(u,v,uv)`.                     (6.13)

Consequently every positive bilinear polynomial

`A u+B v+Cuv`

with `A+B+C>=1` globally majorizes `Phi`.

**Proof.** The bounds `Phi<=u` and `Phi<=v` follow immediately from the failure probability. To prove `Phi<=uv`, if `u>=1` then `Phi<=v<=uv`. If `0<=u<=1`,

`(1-e^-u)(1-e^-v) <= u(1-e^-v) <= 1-e^(-uv)`,               (6.14)

where the last inequality is concavity of `s ->1-e^(-sv)` on `[0,1]`. This is equivalent to `Phi<=uv`.

If `u,v<=1`, divide `Au+Bv+Cuv` by `uv`; it is at least `A+B+C`. If, say, `u>=1` and `u>=v`, divide by `v`; the result is at least `A+B+C`. The remaining cases are symmetric. Thus the polynomial dominates `min(u,v,uv)` whenever `A+B+C>=1`. QED.

Hence the repaired contact passes **every coordinate face consisting of two small coordinates**, globally, not merely near the base.

### 6.3 The entire previously failing fourteen-small homogeneous ray is repaired

The repair also passes the whole ray which killed the preceding candidate. Because

`alpha_* >7/20`,
`13/45 >19/100`,                                             (6.15)

for sufficiently small `epsilon` we may use the uniform bounds

`alpha_s>=7/20`, `beta_ss>=19/100`.                           (6.16)

Put `y=14x`. Along the all-small homogeneous ray,

`P(x) >= (7/20)y +(13/28)(19/100)y^2`.                       (6.17)

Also `exp(x)-1>=x`, so

`F_{14,2}(x1_14)`
` <= y-log(1+y)`
` <= y-2y/(2+y),`                                             (6.18)

where `log(1+y)>=2y/(2+y)` follows by differentiating the difference.

Therefore

`P-F >= 2y/(2+y) -(13/20)y +(247/2800)y^2`.                 (6.19)

After dividing by `y>0` and multiplying by `2+y`, positivity reduces to a quadratic with leading coefficient `247/2800` and discriminant

`-44551/1960000 <0`.                                         (6.20)

This exact discriminant is independently checked in the archived artifact. Equality holds at `y=0`, so (6.19) is nonnegative for every `y>=0`.

Thus the `theta=4/5` repair passes the **entire all-small homogeneous ray for all `x>=0`**, whereas the previous `theta=0` contact failed at the explicit point `x=log(4/3)`.

### What is still missing

I do **not** claim the repaired polynomial is a global majorant. Remaining possible failures include asymmetric motions of three or more small coordinates, mixed small/big faces, and full-dimensional directions. The result is instead a materially stronger candidate together with several exact global gates it survives.

---

## 7. Method #22 — current literature and what the failure changes

I reran current source/literature searches dated 2026-09-19. The August 11, 2026 Ascoli--He--Park--Talagrand paper `arXiv:2608.11183` reformulates Talagrand's discrete convexity conjecture through `k`-thresholds and proves substantial graph-property special cases; current seminar descriptions still present the discrete analogue as open and list further open problems. I found no accessible source in this bounded search that states the exact quadratic face-ray gate, the SDP-passing/global-failing contact above, or the `theta` repair. This is **not** a novelty certificate. The local SDP, fractional-graph contact cone, and convexity tools are standard enough that publication novelty remains `UNVERIFIED`.

The important failure-reading conclusion is methodological: a candidate cannot be promoted because it satisfies exact contact plus the Hessian gate. Many-coordinate faces can accumulate `O(m^2)` pair interactions and expose deficits invisible in every fixed local direction. Any continuation of the quadratic route should therefore use the gate cascade in Section 3 before investing in more elaborate local SDP optimization.

## 8. Exact checker / artifact receipt

Created and executed:

`artifacts/R15/f0111_face_ray_checker_q73x.py`

Archived output:

`artifacts/R15/f0111_face_ray_checker_q73x.out`

The output contains exact rational intervals/certificates for the `m=14` no-go, the repair-ray discriminant, `log2<7/10`, and the large-`m` asymptotic sign, and ends

`ALL_EXACT_CHECKS_PASS`.

Artifact commits:

- checker source: `6c019b26700d4fc35029df64e555a6a3c4539969`;
- output archive: `d1c41bc586a71e7727dd16ab897965b5bf42b380`.

The output was read back at the exact archive commit before this report was written.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  native_source:
    id: I0076
    citation: Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.2
    metric: four source-matching obligations on one frozen counterexample candidate
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_handoff_positive_route: "2/4 frozen; not a live-candidate score"
    status: OPEN / PARTIAL / RETIRED-HANDOFF
    unchanged_count: 6_FROZEN_AT_HANDOFF
    remaining_obligation: "future reassignment would need either a new source-valid frozen candidate or a proof of the common re-rooting relative-phase gate H"
    evidence:
      - runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md
    audits: []
  successor_admission:
    E_READY_CLOSABLE_before: 0
    E_READY_CLOSABLE_after: 0
    action: no claim created
  retained_screen:
    id: F0111
    source: Talagrand Definition 10.1 / Problem 10.9
    status: PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED
    metric_before: "previous curvature-sparing quadratic contact passed positivity + exact contact + strict local SDP; global majorization unknown"
    metric_after: "theta=0 contact REFUTED globally by exact 14-small face ray; theta=4/5 repair passes positivity + exact contact + strict local SDP + every two-small face + entire 14-small homogeneous ray; full global majorization still unknown"
    tried_moves: [16, 19, 22]
    remaining_obligation: "prove or refute global majorization for a repaired spectrahedral contact, next testing asymmetric small-coordinate and mixed small/big faces"
    evidence:
      - runs/R15/20260919_0227Z_successor_screen_f0111_rankone_sdp_z72w.md
      - artifacts/R15/f0111_face_ray_checker_q73x.py
      - artifacts/R15/f0111_face_ray_checker_q73x.out
    audits: []
```

## 10. Next genuinely different methods

The next useful triple is

- **#11 DUALIZE**: derive dual separating measures for the remaining asymmetric face inequalities rather than sampling them;
- **#18 SAY IT IN ANOTHER LANGUAGE**: interpret the repaired pair masses as a fractional random graph/contact law and ask for a stochastic domination statement implying global majorization;
- **#24 FIND THE EXTREMAL OBJECT**: optimize the global deficit over a symmetry quotient to identify whether the next worst direction is a two-level asymmetric small face or a mixed small/big face.

I would not return to another rank-one ansatz or another purely local Hessian optimization.

## 11. Model / scheduler / permission boundary

The scheduler limitation remains unchanged. The exposed task surface provides title/prompt, schedule or relative start, timing mode and enabled state, but **no binding model-family selector, no reasoning-effort selector, no authenticated per-run model/effort attestation, and no guaranteed hour-long execution control**. GPT-6/maximum therefore remains prompt-only here.

The historical P26 `You cannot modify this task` response was authorization-context-specific: the operative repository records that another authorized P/C context subsequently succeeded in updating P26. The legitimate remedy is an owning/authorized owner-admin product/API surface exposing model/reasoning controls, not task duplication or permission bypass. No scheduler or permission change was attempted in this run.
