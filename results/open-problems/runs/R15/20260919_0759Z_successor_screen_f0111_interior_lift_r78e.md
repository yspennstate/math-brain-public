Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations remain `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical positive-route `2/4` is only the frozen handoff value, not a live-candidate score. RETAINED-SCREEN MOVEMENT: the Talagrand F0111 `theta=4/5` boundary-limit quadratic from the preceding run now lifts to a genuine fully interior positive exact-contact global majorant: for every fixed `m>=0` there exists `epsilon_m>0` such that every `0<epsilon<epsilon_m` works at the heterogeneous base `(epsilon,...,epsilon,log 2,log 2)`. Methods #6 DEFORM TO A SOLVED POINT, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY.**

# R15 retained screen — lifting the `k=2` boundary majorant to genuine interior bases

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All Talagrand mathematics below is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen Burdzy–Scheutzow Problem 7.2, promote F0111 from successor-screen status, establish publication novelty, settle Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Continuity, source fidelity, exclusions, and current admission state

I continued from the newest own report

`runs/R15/20260919_0723Z_successor_screen_f0111_twobig_limit_n77b.md`

rather than restarting. Before new mathematics I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the I0076 six-run handoff, the newest R15 report, the retained F0111 proof chain, and the newest coordinator/task-health evidence.

The newest coordinator report available at the start of this run is

`operations/task_health/runs/2026-09-19T075800Z/status.md`.

It records several admitted CLOSABLE assignments, but they are already attached to native slots; the remaining successor gates explicitly have no admitted successor. I found no release or ownership transfer to R15. I therefore created no successor claim and edited no shared root.

### Exact Burdzy–Scheutzow source, checked again

The primary *Forward Brownian Motion* source, arXiv:1302.6958, Definition 2.1 and Problem 7.2, still says:

- FBM: random origins `S_n -> -infinity` from which the complete centered future is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random origin `S` at which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2 assumes FBM + BBM and existence of an arbitrary random time `T` at which the two complete centered half-processes are independent.

There is **no stopping-time assumption on `T`**, and neither seam half at `T` is separately assumed Brownian. Problem 7.5 is a different question and remains excluded.

The controlling six-run handoff remains valid. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved actually to be 2BM. Hence there is still no surviving frozen counterexample candidate on which the original four-obligation metric can honestly move.

Fresh public searches dated 2026-09-19 used the exact title, arXiv identifier, `Problem 7.2`, later-author terms and citation terms. They recovered the original source and citation trail but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a global openness certificate.

For the retained Talagrand screen, the current primary-literature pass again recovered Ascoli–He–Park–Talagrand, arXiv:2608.11183 (submitted 2026-08-11), which reformulates the broader discrete convexity conjecture via `k`-thresholds and proves substantial graph classes, but does not claim the full conjecture. The exact Problem 10.9 source scope therefore remains distinct. Search failure for the theorem below is not a novelty certificate.

## 2. Carried theorem and the precise missing step

For cardinality two write

`F_n(t)=sum_i t_i - log(1+sum_i(exp(t_i)-1))`.                (2.1)

The preceding report proved the following global **boundary-limit** theorem. Put `b=log 2` and, for `m>=0`,

`X=sum_{i=1}^m x_i`, `Q=sum_{1<=i<j<=m} x_i x_j`,            (2.2)

and define

`alpha = 2/3 -(4/9)b`,
`beta_s = 13/45`,
`a = 5/3 - log(3)/b`,
`c = 2/9`,
`beta = [log(3) -(4/3)b]/b^2`.                               (2.3)

Then

`P_0(x,y,z)`
` = alpha X + beta_s Q`
`   + a(y+z) + beta yz + c X(y+z)`                           (2.4)

satisfies

`P_0(t) >= F_{m+2}(t)` for every `t>=0`.                     (2.5)

Moreover `P_0` has value and first-order contact at the boundary point

`q_0=(0,...,0,b,b)`.                                         (2.6)

The explicit unresolved obligation recorded in that report was to lift (2.5) to the actual positive-`epsilon` repaired exact-contact family. Mere coefficientwise continuity was insufficient because the domain is the noncompact orthant.

This run closes exactly that gap for every fixed `m`.

## 3. Method #6 — deform the interior family to the solved boundary point

Fix an arbitrary integer `m>=0`, put `n=m+2`, and for `epsilon>0` define

`q_e=(epsilon,...,epsilon,b,b)`, `b=log 2`,                  (3.1)

with `m` small coordinates. Let

`S_e=3+m(exp(epsilon)-1)`,
`r_s=exp(epsilon)/S_e`, `r_b=2/S_e`,                         (3.2)

`z_s=epsilon r_s`, `z_b=b r_b`,
`d_s=epsilon^2 r_s(1-r_s)`.                                  (3.3)

At the base `q_e`, let

`D_e=m epsilon(1-r_s)+2b(1-r_b)`,
`W_e=D_e-F_n(q_e)`.                                          (3.4)

Freeze the repair parameter

`theta=4/5`                                                   (3.5)

and define pair contact masses

`e_ss=z_s^2 +(4/5)d_s`,
`e_sb=z_s z_b`,
`e_bb=W_e-C(m,2)e_ss-2m e_sb`.                               (3.6)

Define singleton contact masses from the exact degree equations

`a_s=epsilon(1-r_s)-(m-1)e_ss-2e_sb`,
`a_b=b(1-r_b)-m e_sb-e_bb`.                                  (3.7)

The corresponding quadratic coefficients are

`alpha_s(e)=a_s/epsilon`,
`beta_ss(e)=e_ss/epsilon^2`,
`alpha_b(e)=a_b/b`,
`beta_bb(e)=e_bb/b^2`,
`c_e=e_sb/(epsilon b)`.                                      (3.8)

Thus

`P_e(x,y,z)`
` =alpha_s(e) X + beta_ss(e) Q`
`  +alpha_b(e)(y+z)+beta_bb(e)yz+c_e X(y+z)`.                (3.9)

By construction of the masses,

`P_e(q_e)=F_n(q_e)`,
`grad P_e(q_e)=grad F_n(q_e)`.                               (3.10)

This is exact, not asymptotic.

As `epsilon ->0+`,

`r_s ->1/3`, `r_b ->2/3`,                                   (3.11)

and direct substitution gives

`alpha_s(e)->alpha`,
`beta_ss(e)->beta_s`,
`alpha_b(e)->a`,
`beta_bb(e)->beta`,
`c_e->c`.                                                    (3.12)

The limits are all strictly positive. In particular `a>0` is exactly

`5 log2 > 3 log3`, i.e. `32>27`,                             (3.13)

and `beta>0` follows from `3^3>2^4`. Therefore for this fixed `m` all coefficients of `P_e` are strictly positive once `epsilon` is sufficiently small.

So `P_e` is a genuine positive multilinear quadratic exact-contact candidate at a **fully interior** base. The only issue is global majorization.

## 4. First new lemma — the boundary gap has exactly two zeros

Put

`G_0=P_0-F_n`.                                               (4.1)

The carried theorem says `G_0>=0`. I now need the stronger fact

`{t>=0:G_0(t)=0}={0,q_0}`.                                  (4.2)

### Proof of (4.2)

The carried pair-smoothing theorem says that in any symmetric coordinate orbit whose within-orbit quadratic coefficient exceeds `1/6`, a fixed-total minimum of `P-F` can occur only after equalizing positive coordinates or deleting coordinates. Here

`beta_s=13/45>1/6`, `beta>1/6`,                              (4.3)

where the second strict inequality was certified exactly in the previous finite core.

Suppose `G_0(t)=0`. Since `G_0>=0`, this point is a minimizer on the compact product of the fixed-total small and big simplices. Pair smoothing therefore forces:

- all positive small coordinates to be equal;
- the two big coordinates either to be equal or one of them to be zero.

The carried branch theorems then make the equality cases explicit.

**No big coordinate.** The small-face cone proof used the strict rational interior pair

`alpha_0=179/500`, `beta_0=36/125`,                           (4.4)

with

`(1-alpha_0)^2-4alpha_0 beta_0=-63/250000<0`,                (4.5)

and the exact strict coefficient inequalities `alpha>alpha_0`, `beta_s>beta_0`. Hence every nonzero small vector has `G_0>0`.

**Exactly one big coordinate.** If there is no positive small coordinate, `F_n=0` and the polynomial equals `a y>0`. With one positive small coordinate, the carried rational mixed-face theorem lies strictly below the limiting coefficients:

`alpha>16/45`, `a>2/25`, `c=2/9>21/100`,                    (4.6)

so every genuinely mixed point has strict positive slack, while axes again have positive singleton cost. For at least two positive small coordinates, the carried Bernoulli-KL proof has strict `K(s)>0` on the only dangerous KL branch; off that branch the strict small-face gap already supplies strict positivity. Thus no one-big point is a zero except the origin, where the big coordinate is also zero.

**Two equal positive big coordinates.** Write the positive-small support size as `r`. For `r>=2`, the preceding run decomposed the exact reduced gap as

`G_r(s,y)>=h(y)+L(s,y)`,                                     (4.7)

with `h>=0` and `L(s,y)>0` whenever `s>0`. For `r=1` its separate term `L_1(s,y)` is also strictly positive for `s>0`. For `r=0`, the gap is exactly `h(y)`. The proof of the preceding run gives

`h(0)=h(b)=0`,                                                (4.8)

`h(y)>0` for every `y>=0`, `y notin {0,b}`.                  (4.9)

Hence the two-big branch has equality only at the origin and at `y=b`, i.e. at `q_0`.

These exhaust the pair-smoothed minima. Therefore (4.2) holds. QED.

This exact zero-set classification is the key extra information that plain coefficient convergence lacked.

## 5. Method #13 — a coercive monovariant prevents failures from escaping to infinity

The second missing ingredient is uniform control of the noncompact orthant.

Because all five limiting coefficient types in (2.3) are positive, choose constants `u,v>0` and `epsilon_1>0` such that for every `0<epsilon<epsilon_1`,

- every singleton coefficient of `P_e` is at least `u`;
- every pair coefficient of `P_e` is at least `v`.             (5.1)

For an arbitrary `t>=0`, put

`X=sum_i t_i`, `M=max_i t_i`, `B=X-M`,
`Q_all=sum_{i<j}t_i t_j`.                                    (5.2)

The cardinality-two hazard obeys

`F_n(t)<=B`,                                                  (5.3)

because

`1+sum_i(exp(t_i)-1)>=exp(M)`.                               (5.4)

On the polynomial side,

`P_e(t)>=uX+v Q_all`,                                        (5.5)

and the pairs involving a maximizing coordinate alone give

`Q_all>=M B`.                                                (5.6)

Consequently

`G_e(t):=P_e(t)-F_n(t)`
` >=uM+B(u-1+vM)`.                                           (5.7)

In particular, once

`M >= R_0:=(1-u)/v`,                                         (5.8)

(the case `u>=1` is easier), the bracket in (5.7) is nonnegative and

`G_e(t)>=uM>0`.                                              (5.9)

So a prospective negative point cannot run away to infinity as `epsilon ->0`. Every failure would have to remain in one fixed compact box depending only on `m,u,v`, not on `epsilon`.

This is the monotone quantity of the run: after the largest coordinate crosses `R_0`, the pair mass `MB` makes the gap irreversibly positive.

## 6. Uniform control near the origin

The other boundary zero, the origin, is also harmless uniformly in `epsilon`.

Let `p_i=1-exp(-t_i)` and let `zeta` be the probability that at least two coordinates are selected. By the union bound over pairs,

`zeta <= sum_{i<j}p_i p_j <= Q_all <=X^2/2`.                 (6.1)

For `X<=1`, this gives `zeta<=1/2`, and hence

`F_n(t)=-log(1-zeta)<=2zeta<=X^2`.                           (6.2)

Together with `P_e>=uX`,

`G_e(t)>=uX-X^2`.                                            (6.3)

Thus whenever

`0<X<=delta_0:=min(1,u/2)`,                                  (6.4)

we have

`G_e(t)>=(u/2)X>0`.                                          (6.5)

So no negative points can collapse into the origin either.

## 7. Method #29 — compactify the last hole and use strong convexity at `q_0`

It remains to control a neighborhood of the second boundary zero `q_0` and then the compact middle region.

### 7.1 The Hessian at the boundary contact is strictly positive definite

At `q_0`, the hazard weights are

`r_s=1/3`, `r_b=2/3`.                                       (7.1)

For `G_0=P_0-F_n`, the small-small Hessian block has

`diag=2/9`, `offdiag=beta_s-1/9=8/45`.                       (7.2)

Its eigenvalues are

`2/45` on the small-orbit transverse space,                  (7.3)

and

`2/9 +(m-1)8/45` on the all-ones direction.                 (7.4)

The small-big entries vanish exactly because

`c-r_s r_b=2/9-2/9=0`.                                      (7.5)

The big `2x2` block has diagonal `2/9` and off-diagonal `beta-4/9`, hence eigenvalues

`beta-2/9`, `2/3-beta`.                                      (7.6)

The preceding exact checker certified `beta>2/9`. Also

`a=1/3-beta b>0`                                             (7.7)

by `32>27`, and `b>1/2`; therefore

`beta<1/(3b)<2/3`.                                           (7.8)

Thus every eigenvalue in (7.3)--(7.6) is strictly positive. The Hessian of `G_0` at `q_0` is positive definite for every fixed `m` (with absent blocks ignored for `m=0,1`).

By smooth dependence on `(epsilon,t)`, there are `rho>0`, `lambda>0`, and `epsilon_2>0` such that, for every `0<epsilon<epsilon_2`,

`nabla^2 G_e(t) >= lambda I`                                 (7.9)

throughout a fixed Euclidean ball `B(q_0,rho)`. For smaller `epsilon` we also have `q_e in B(q_0,rho/4)`.

Using the exact contact equations (3.10), strong convexity yields

`G_e(t)>= (lambda/2)||t-q_e||^2`                             (7.10)

for every nonnegative `t` in a sufficiently smaller fixed ball around `q_0`. Hence the positive-`epsilon` perturbation cannot open a negative crater near the boundary contact.

### 7.2 The compact middle region

By Section 5, any negative point lies in the compact box

`K={t>=0:max_i t_i<=R_0}`.                                   (7.11)

Remove from `K` the uniform origin neighborhood in Section 6 and the fixed `q_0` neighborhood in Section 7.1. The remainder `K_mid` is compact.

By the zero-set theorem (4.2),

`G_0>0` on `K_mid`.                                          (7.12)

Therefore

`eta:=min_{K_mid}G_0>0`.                                     (7.13)

The coefficients of `P_e` converge to those of `P_0`, so `G_e->G_0` uniformly on `K_mid`. Hence for all sufficiently small positive `epsilon`,

`G_e>=eta/2>0` on `K_mid`.                                   (7.14)

Sections 5, 6, 7.1 and 7.2 cover the entire nonnegative orthant.

## 8. New theorem — fully interior exact-contact global majorants

### Theorem R15-F0111-K2-INTERIOR-LIFT

For every fixed integer `m>=0`, there exists `epsilon_m>0` such that, for every

`0<epsilon<epsilon_m`,                                       (8.1)

the `theta=4/5` repaired polynomial `P_e` in (3.9) has all coefficients strictly positive and satisfies

`P_e(t)>=F_{m+2}(t)` for every `t in R_+^(m+2)`,             (8.2)

with exact value and gradient contact at the fully interior heterogeneous base

`q_e=(epsilon,...,epsilon,log2,log2)`.                       (8.3)

**Proof.** Positivity and contact are Section 3. The boundary theorem and exact boundary zero set are Sections 2 and 4. Uniform coercivity at infinity is Section 5, the origin is Section 6, the moving exact-contact point is protected by uniform strong convexity in Section 7.1, and uniform convergence closes the remaining compact middle region in Section 7.2. QED.

### Interpretation in Talagrand's language

At each base covered by the theorem, `P_e` is a positive multilinear polynomial with no constant term, globally majorizes the cardinality-two hazard, and satisfies exact contact `P_e(q_e)=F(q_e)`. Therefore these specific bases satisfy the `gamma=1` certificate requirement appearing in Talagrand's Definition 10.1.

This is substantially stronger than the preceding boundary-limit statement: the certificate now lives at a genuinely interior heterogeneous base and is an actual global majorant, not a limit object.

It is still **not** Talagrand Problem 10.9. The source asks for one universal `gamma>0` covering every base and every cardinality threshold. Here:

- only `k=2` is treated;
- the bases have the two-level form `(epsilon^m,b,b)` with `b=log2`;
- `epsilon_m` may depend on `m`;
- no claim is made for arbitrary heterogeneous bases or `k>=3`.

Status therefore remains `PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED`.

## 9. Why no new checker was created

The movement in this run is a theorem-sized compactness/coercivity argument, not a finite enumeration. The only finite transcendental signs imported into the proof are already certified by earlier exact-rational artifacts, especially:

- `beta>2/9` and the two-big limiting finite core in `artifacts/R15/f0111_twobig_limit_checker_n77b.py/.out`;
- the strict small-face cone discriminant in `artifacts/R15/f0111_smallface_cone_y74c.py/.out`;
- the strict one-big scalar margins in `artifacts/R15/f0111_onebig_uniform_checker_m76a.py/.out`.

A new grid sampler would not certify the noncompact global statement and would violate the run's idea-first rule. The new proof is on the page.

## 10. Current literature and novelty status

Dated 2026-09-19 searches included:

- `Burdzy Scheutzow Forward Brownian Motion Problem 7.2 arXiv 1302.6958` and later-author/citation variants;
- `Talagrand Problem 10.9 Are Many Small Sets Explicitly Small`;
- Ascoli–He–Park–Talagrand `k`-threshold work, arXiv:2608.11183.

The Brownian search recovered the original source and citation trail, but no accessible later primary source explicitly claiming resolution of exact Problem 7.2. The Talagrand search recovered the August 11, 2026 reformulation and substantial special classes, not a full resolution of Problem 10.9. I found no accessible source in this bounded search stating Theorem R15-F0111-K2-INTERIOR-LIFT.

That absence is not a novelty certificate. The new proof is built from elementary compactness, coercivity, pair smoothing and a carried explicit polynomial, so **publication novelty remains UNVERIFIED**.

## 11. Model / scheduler control

The operative implementation evidence remains unchanged on model control. The exposed scheduler surface provides task identity/title, prompt, schedule/timing, enabled state and notification-related controls, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution field. Therefore `GPT-6 / maximum` remains prompt text only in this run.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in an unauthorized context. The boundary was not bypassed; repository continuity records later successful modification only from an authorized P/C context. A genuine GPT-6/maximum guarantee would require an owning/authorized or owner/admin product/backend/API surface that actually persists those routing fields and attests them after execution.

No scheduler, permission, email, Drive, public-posting, purchase, or shared-root change was attempted.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  native_source:
    id: I0076
    citation: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
    metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_handoff_positive_route: "2/4 frozen; not a live-candidate score"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    unchanged_count: "6_FROZEN_AT_HANDOFF"
    remaining_obligation: "requires a genuinely new surviving source-valid candidate or a complete implication proof; retirement remains controlling"
  successor_admission:
    claim_created: false
    reason: "newly admitted closable work found in current coordinator state is already owned; remaining gates have no admitted successor"
  retained_screen:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9"
    status: "PENDING / NOT READY / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
    movement: true
    before: "dimension-free k=2 boundary-limit global quadratic majorant at (0^m,log2,log2)"
    after: "for every fixed m, genuine positive-epsilon fully interior global positive quadratic exact-contact majorants at (epsilon^m,log2,log2) for all sufficiently small epsilon"
    theorem_id: R15-F0111-K2-INTERIOR-LIFT
    remaining_obligation: "arbitrary heterogeneous k=2 bases and then k>=3 / universal source gamma; obtain independent audits before any closure or publication claim"
  methods_this_run:
    - "#6 DEFORM TO A POINT YOU CAN SOLVE"
    - "#13 FIND WHAT ONLY INCREASES"
    - "#29 ADD THE POINTS AT INFINITY"
  evidence:
    - "runs/R15/20260919_0723Z_successor_screen_f0111_twobig_limit_n77b.md"
    - "runs/R15/20260919_0605Z_successor_screen_f0111_onebig_uniform_m76a.md"
    - "runs/R15/20260919_0455Z_successor_screen_f0111_orbit_smoothing_k75v.md"
    - "runs/R15/20260919_0358Z_successor_screen_f0111_smallface_cone_y74c.md"
    - "artifacts/R15/f0111_twobig_limit_checker_n77b.out: ALL_EXACT_CHECKS_PASS"
  audits: []
```

## 13. Next research move

The positive-epsilon compactness gap that blocked the preceding run is now gone. Repeating another continuity or local-SDP lemma would be low value.

The next useful attack should leave the two-level family. A natural target is to deform the two equal large coordinates independently,

`(epsilon^m,b-delta,b+delta)`,                                (13.1)

and determine whether the interior global certificate persists through a nontrivial open set of genuinely three-level bases. If that works, the correct next invariant is the geometry of the open certificate region in hazard space, not another special ray.

Suggested next Section-B moves: **#1 CHANGE THE CATEGORY, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS**.