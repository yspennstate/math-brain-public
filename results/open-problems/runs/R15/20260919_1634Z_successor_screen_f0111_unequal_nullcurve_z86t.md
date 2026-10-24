Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the fixed four-obligation metric remains `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, with the historical positive-route `2/4` only a frozen handoff value. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, the unequal-amplitude two-block Hessian-null mechanism is reduced to one explicit scalar cubic-null curve, quartic local minimality is proved automatically strict, the `C=0` branch is completely excluded, and all positive-weight candidates are classified into three surviving scalar regimes. Methods applied in a new way: #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE, #7 TAKE THE LIMIT.**

# R15 retained screen — exact unequal-amplitude Hessian-null curve for the quadratic `k=2` Talagrand hazard

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 from PENDING/NOT READY, establish publication novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Continuity, source fidelity, ownership, exclusions

I continued from the immediately preceding immutable report

`runs/R15/20260919_1459Z_successor_screen_f0111_unequal_twoblock_y85s.md`

created at commit

`0bd9040070400f9fb16cf4edcd8d3d081b09f18d`,

rather than restarting.

Before new mathematics I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the I0076 history and six-run handoff, the newest R15 report, and the newest neighboring CLOSABLE admission reconciliation available on master.

The newest visible CLOSABLE gate is R06 commit

`502c2216976341d9cdd6285846b9fa74b8b6e692`,

which recovers P0462 as an already retired six-run route and records successor-admission metric `E_ready: 0 -> 0`. It also screens P0367 as an infinite conditional-support theorem, P0469 as HARD, and E0057 as literature-resolved/KNOWN. There is therefore still no lawful free + READY + CLOSABLE + nonretired target for R15. I did not steal an owned target, convert a PENDING row into READY, or revive a retired route.

### Exact I0076 source rechecked

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / *Probability Theory and Related Fields* 160 (2014), 95--126.

Definition 2.1 and Problem 7.2 remain exactly as recorded:

- FBM: there exist random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random time `S` at which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2: `X` is FBM and BBM and there exists an arbitrary random time `T` such that the two complete centered half-processes `(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}` are independent. Must `X` be 2BM?

The source does **not** assume `T` is a stopping time, does not allow deterministic-time independence as a substitute, and does not separately assume either half at `T` is Brownian. Problem 7.5 is a distinct source question and remains excluded.

The controlling I0076 handoff is unchanged. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but R15 eliminated source-valid independent seam existence. The later Brownian-prefix/BES candidate had exact seam independence but R15 proved it is actually 2BM. Hence no frozen counterexample candidate survives. The transparent positive-route count froze at `2/4` after six unchanged runs and I0076 was operationally handed off rather than silently restarted.

Fresh 2026-09-19 public searches using the exact paper title, authors, arXiv ID and `Problem 7.2` recovered the original paper/publication and related Brownian-pasting material, but no accessible later primary source explicitly claiming a solution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

### Retained F0111 literature check

Fresh 2026-09-19 primary-source searches still recover:

- Ascoli--He--Park--Talagrand, arXiv:2608.11183, 2026-08-11: a `k`-threshold reformulation and substantial classes, not the full discrete Convexity Conjecture;
- Chen Li, arXiv:2609.08967, 2026-09-08: the fractional version;
- Jinyoung Park, arXiv:2609.14681, 2026-09-13: a dimension-free comparison explicitly stated as progress toward the conjecture;
- Fang--Wang, arXiv:2609.18458, 2026-09-16: another Talagrand problem, not Problem 10.9.

I found no accessible primary source stating the null-curve calculation below. Negative search evidence does not establish novelty; novelty remains `UNVERIFIED`.

### Section-B method-history constraint

The preceding run used #11/#20/#24. The historical R15/F0111 report

`runs/R15/20260919_0605Z_successor_screen_f0111_onebig_uniform_m76a.md`

explicitly records that **all 30 Section-B moves had already been tried at least once on F0111**. Therefore the literal instruction to choose three globally unused numbers on this retained screen is no longer satisfiable without inventing history. I do not falsely claim unused numbers. I instead use a nonconsecutive triple in genuinely new roles: #18 (signed three-atom cumulant language), #25 (derive the same fifth-order obstruction from the support polynomial and cumulants), and #7 (singular balanced limit). This does not repeat the immediately preceding #11/#20/#24 triple.

The analytic idea was written before code in

`artifacts/R15/f0111_unequal_nullcurve_idea_z86t.md`

at commit `7a3714bc812e6eafbc5b2a04f3650959e98ffeb3`.

---

## 2. Carried `k=2` setup and the remaining local mechanism

For the cardinality-two threshold hazard,

`F(t)=sum_i t_i-log S(t)`,

`S(t)=sum_i exp(t_i)-(n-1)`,                                  (2.1)

and a nonnegative quadratic polynomial

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,

`A_i,B_ij>=0`.                                                 (2.2)

A global certificate at an interior base `q` means

`P(t)>=F(t)` for every `t>=0`, and `P(q)=F(q)`.                (2.3)

Earlier R15 runs proved a first-bifurcation theorem: at a boundary base of the quadratic `C_1` certificate region, every global certificate must either acquire a second global contact or have singular contact Hessian. Subsequent sign-rigidity showed that a genuinely isolated remaining bifurcation must use a mixed-sign direction.

The preceding run treated arbitrary two-block amplitudes for the **second-contact** mechanism. This run treats the parallel **Hessian-null** mechanism for

`h=a 1_J-b 1_K`, `a,b>0`,                                    (2.4)

with disjoint nonempty coordinate blocks `J,K`.

Write

`A=sum_{i in J} exp(q_i)>0`,

`B=sum_{i in K} exp(q_i)>0`,

`C=sum_{i notin J union K} exp(q_i)-(n-1)`,                  (2.5)

so along `q+s h`,

`S(s)=A exp(as)+B exp(-bs)+C`.                               (2.6)

Let

`ell(s)=log S(s)`.                                             (2.7)

Because `q` is interior, small positive and negative `s` are both feasible. If `h` is a null direction of the Hessian of the nonnegative gap

`G=P-F`,                                                        (2.8)

then `s=0` is a two-sided local minimum with

`G''(0)=0`.                                                     (2.9)

Since the restriction of `P` is quadratic and the non-logarithmic part of `F` is linear,

`G^(j)(0)=ell^(j)(0)` for every `j>=3`.                       (2.10)

Hence local minimality forces

`ell'''(0)=0`, `ell''''(0)>=0`;                               (2.11)

and if the fourth derivative vanishes, then also

`ell'''''(0)=0`.                                               (2.12)

These are exact necessary conditions, not numerical diagnostics.

---

## 3. Method #18 — rewrite the line as a signed three-atom cumulant problem

Normalize at `s=0`:

`x=A/S(0)>0`, `y=B/S(0)>0`, `k=C/S(0)`,                      (3.1)

so

`x+y+k=1`.                                                     (3.2)

The number `k` may be negative; this is why the correct language is a **signed** three-atom mass, not a probability distribution:

`nu=x delta_a + y delta_{-b} + k delta_0`.                    (3.3)

Nevertheless derivatives of `ell=log S` are exactly the formal cumulants of this total-mass-one three-atom object.

Introduce

`m=(a+b)/2>0`,

`delta=(a-b)/(a+b) in (-1,1)`,                               (3.4)

and let

`p=ell'(0)=a x-b y`,

`z=p/m-delta`.                                                 (3.5)

Thus

`a=m(1+delta)`, `b=m(1-delta)`, `p=m(delta+z)`.              (3.6)

The two-exponential ODE from the preceding run gives

`ell''(0)=(a-b)p+ab(1-k)-p^2`,                               (3.7)

and differentiating once gives the exact cubic recurrence

`ell'''(0)=(a-b-2p)ell''(0)+ab k p`.                         (3.8)

For unequal amplitudes `delta != 0`, the apparent denominator branch

`delta+3z=0`                                                   (3.9)

cannot satisfy cubic nullity. Indeed then `p=(a-b)/3`, and direct substitution into (3.8) yields

`ell'''(0)=2 m^3 delta(9-delta^2)/27 !=0`.                   (3.10)

Away from that impossible branch, solving `ell'''(0)=0` is exact and gives

`boxed: k = 2 z(1-z^2)/((1-delta^2)(delta+3z)).`             (3.11)

Using `x+y=1-k` and `a x-b y=p`, one then gets

`boxed: x = (delta+z)(1+z)(1+delta+2z)`
`             / [2(1+delta)(delta+3z)],`                     (3.12)

`boxed: y = (delta+z)(1-z)(1-delta-2z)`
`             / [2(1-delta)(delta+3z)].`                     (3.13)

Thus the entire unequal-amplitude two-block cubic-null locus is **one scalar curve in `z`**. The original high-dimensional coefficient problem has disappeared from the derivative compatibility calculation.

On this curve the second and fourth log derivatives factor as

`ell''(0)=m^2 Q_delta(z)`,                                    (3.14)

where

`Q_delta(z)=((delta+z)(1-z^2))/(delta+3z)`,                  (3.15)

and

`ell''''(0)=m^4 R_delta(z)`,                                  (3.16)

with

`R_delta(z)`
`= -2 (delta+z)(1-z^2)`
`    * [delta^2 z+3 delta z^2+delta+3 z^3]`
`    / (delta+3z)^2`.                                         (3.17)

Equations (3.11)--(3.17) are identities, not asymptotics.

---

## 4. Method #25 — count the fifth derivative twice and force strict quartic positivity

The local condition in (2.11) only says `R_delta(z)>=0`. The key new rigidity is that for unequal amplitudes equality is impossible.

Let `Y=lambda-p` on the three support points `lambda in {a,-b,0}` and write central moments

`mu_j = integral Y^j d nu`.                                   (4.1)

Then

`kappa_2=mu_2=ell''(0)`,

`kappa_3=mu_3=ell'''(0)`,

`kappa_4=mu_4-3mu_2^2=ell''''(0)`,

`kappa_5=mu_5-10mu_3 mu_2=ell'''''(0)`.                      (4.2)

### First count: the cubic support polynomial

The three centered support points are

`a-p`, `-b-p`, `-p`.                                          (4.3)

Their sum is

`sigma_1=a-b-3p`.                                              (4.4)

Their monic cubic support polynomial is

`Y^3-sigma_1 Y^2+sigma_2 Y-sigma_3=0`.                       (4.5)

Average (4.5) under `nu`. Since `mu_1=0` and cubic nullity gives `mu_3=0`,

`sigma_3=-sigma_1 mu_2`.                                      (4.6)

Multiply (4.5) by `Y^2` and average again. Using (4.6) and `mu_3=0`,

`mu_5=sigma_1(mu_4-mu_2^2)`.                                 (4.7)

Therefore on every cubic-null point,

`boxed: kappa_5 = (a-b-3p)(kappa_4+2 kappa_2^2).`            (4.8)

This is the same fifth-order quantity obtained from differentiating `log S`, but the support-polynomial count exposes its factorization.

### Second count: prove the remaining factors cannot vanish

At a cubic-null point, `kappa_2` cannot vanish. If `kappa_2=0`, (3.8) and `kappa_3=0` imply

`ab k p=0`.                                                    (4.9)

Because `ab>0`, either `k=0` or `p=0`.

- If `k=0`, then `x+y=1` with `x,y>0`; the ordinary two-point variance is
  `kappa_2=xy(a+b)^2>0`, contradiction.
- If `p=0`, (3.7) gives
  `kappa_2=ab(1-k)=ab(x+y)>0`, contradiction.

Hence

`kappa_2 !=0`.                                                 (4.10)

Also

`a-b-3p = -m(delta+3z)`.                                      (4.11)

For unequal amplitudes, the only way this factor could vanish is the branch already excluded by (3.10). Thus it too is nonzero on the cubic-null curve.

Now suppose local minimality had `kappa_4=0`. Equation (4.8) would give

`kappa_5=2(a-b-3p)kappa_2^2 !=0`,                            (4.12)

contradicting the necessary odd-order condition (2.12). Therefore every genuine unequal-amplitude Hessian-null direction satisfies the **strict** inequality

`boxed: R_delta(z)>0.`                                        (4.13)

This removes the entire fourth-order equality boundary without any numerical search.

---

## 5. Exact positive-weight regime classification

The factorized formulas also give a complete scalar sign chart. Because reversing the line sends `(delta,z)` to `(-delta,-z)`, it suffices to display `0<delta<1`.

From (3.12)--(3.13), the condition `x>0,y>0` holds exactly on four open `z` intervals:

1. `z<-1`;
2. `-(1+delta)/2 < z < -delta`;
3. `-delta/3 < z < (1-delta)/2`;
4. `z>1`.

Define

`N_delta(z)=delta^2 z+3 delta z^2+delta+3z^3`.                (5.1)

It has the useful form

`N_delta(z)=[(delta+3z)^3+delta(9-delta^2)]/9`,              (5.2)

so

`N_delta'(z)=(delta+3z)^2>=0`.                               (5.3)

On interval 3, `Q_delta(z)>0`, `delta+3z>0`, and `N_delta(z)>0`, hence (3.17) gives

`R_delta(z)<0`.                                                (5.4)

Thus interval 3 is completely impossible for a Hessian-null local minimum.

On interval 2, `Q_delta(z)>0` and `delta+3z<0`, so `R_delta(z)` has the same sign as `N_delta(z)`. At the endpoints,

`N_delta(-(1+delta)/2)=-(1-delta)^2(delta+3)/8<0`,            (5.5)

`N_delta(-delta)=delta(1-delta^2)>0`.                         (5.6)

By monotonicity there is one root

`z_*(delta) = -[delta + (delta(9-delta^2))^(1/3)]/3`,         (5.7)

and strict quartic positivity keeps only

`z_*(delta)<z<-delta`.                                        (5.8)

The two outer intervals automatically have `R_delta(z)>0`: `N_delta(z)<0` for `z<-1` and `N_delta(z)>0` for `z>1`.

Therefore, after choosing the orientation `delta>0`, every unequal-amplitude two-block Hessian-null candidate is confined to exactly three scalar regimes:

`boxed: z<-1,  or  z_*(delta)<z<-delta,  or  z>1.`            (5.9)

The middle regime has `k=C/S(0)>0`. Both outer regimes have `k<0`. So the null mechanism has split cleanly into one positive-stationary-remainder strip and two negative-remainder tails.

### Complete elimination at `C=0`

If `C=0`, then `k=0`. Equation (3.11) gives

`z in {0,-1,1}`.                                               (5.10)

But `z=1` makes `y=0` in (3.13) and `z=-1` makes `x=0` in (3.12), contradicting `A,B>0`. Hence only `z=0` remains. Yet (3.17) gives the exact value

`R_delta(0)=-2`.                                               (5.11)

This contradicts local minimality. Thus

`boxed: for a!=b and C=0, no two-block Hessian-null direction exists.` (5.12)

The preceding balanced calculation already excluded the `a=b,C=0` case, so **no two-block Hessian-null mechanism of any amplitude ratio exists when `C=0`**.

---

## 6. Method #7 — the singular balanced limit recovers both old branches

The formulas have a nonuniform limit at `delta=0`, and that nonuniformity is informative rather than a defect.

For fixed nonzero `z`, letting `delta->0` in (3.11) and (3.17) gives

`k -> 2(1-z^2)/3`,                                             (6.1)

`R_delta(z) -> (2/3) z^2(z^2-1)`.                            (6.2)

Thus strict local admissibility becomes `|z|>1`, which is exactly the **negative-`C` balanced branch** from the earlier R15 calculation.

The positive-`C` balanced branch lives in the singular scale `z=t delta`. Taking `delta->0` with fixed `t` gives

`k -> 2t/(1+3t)`,                                              (6.3)

`R_delta(t delta) -> -2(t+1)/(1+3t)^2`.                      (6.4)

For `t<-1`, (6.4) is positive and (6.3) lies in `(2/3,1)`. Since `k=C/S(0)` and `1-k=(A+B)/S(0)`,

`k>2/3  <=>  C>2(A+B)`,                                       (6.5)

which is exactly the old **positive-`C` balanced branch**.

At the exceptional balanced point `delta=z=0`, direct differentiation gives the previously obtained

`ell''''(0)=m^4(1-k)(3k-2)`.                                  (6.6)

Thus the strict positive branch is `k>2/3`, while the equality `k=2/3` was already excluded by the sixth-order calculation in the balanced run.

So the new unequal-amplitude curve does not merely coexist with the old balanced theorem: its regular and singular `delta->0` limits recover the old negative- and positive-`C` branches respectively.

---

## 7. Exact symbolic validation

Only after the analytic route was written down, I added a small exact SymPy self-check:

- source: `artifacts/R15/f0111_unequal_nullcurve_symbolic_z86t.py` @ `d1506179fc3e9822002c2012f7c3a0041db24a14`;
- archived executed output: `artifacts/R15/f0111_unequal_nullcurve_symbolic_z86t.out` @ `d93dd25ab15ab934c29b3223e3e410044f8fcb22`.

It verifies exactly, without floating-point sampling:

- `x+y+k=1` and the mean formula;
- the second-cumulant factor `Q_delta`;
- exact cubic nullity on (3.11);
- the fourth-cumulant factor `R_delta`;
- the fifth-order support recurrence (4.8);
- the nonzero formula on the excluded `delta+3z=0` branch;
- `R_delta(0)=-2` for `C=0`;
- the regular balanced specializations (6.1)--(6.2);
- the singular blow-up limits (6.3)--(6.4).

The archived execution ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

This is a self-check, not an independent audit.

---

## 8. What moved and what remains

This run does **not** move the native I0076 source metric and does **not** solve Talagrand Problem 10.9.

The retained-screen movement is exact:

1. the unequal-amplitude two-block Hessian-null problem is scalarized completely by `(delta,z)`;
2. cubic nullity gives explicit `k,x,y` formulas;
3. local quartic nonnegativity is upgraded to **strict** quartic positivity;
4. `C=0` is ruled out completely;
5. positive weights plus quartic positivity leave exactly three scalar regimes after orientation;
6. the balanced positive- and negative-`C` branches are recovered as singular and regular limits.

The highest-value next attack is no longer to differentiate `S` again. It is to use the **nonnegative coefficient / graph-flow part of the exact-contact Hessian equation** to test the three surviving regimes in (5.9). If that kills all three, every two-block Hessian-null bifurcation is eliminated. In parallel, the second-global-contact mechanism from the preceding report still survives in part of parameter space. Beyond two blocks, the strategic goal remains a compression theorem reducing a general mixed-sign extremal direction to a two-level displacement.

No closure label is changed.

---

## 9. Model and scheduler-control truth

This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning remains **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The currently exposed task-update surface still offers title/prompt, schedule or relative start, timing mode, enabled state and ordinary update controls. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed hour-long execution field**. Therefore GPT-6/maximum remains prompt text rather than an enforceable scheduler routing setting in this interface.

The repository records that P26 task ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context, while `RESULTS.md` records that a later authorized P/C context succeeded in updating P26. The lawful workaround for an edit-denied task is therefore the owning/authorized product or admin/API context, not duplication or permission bypass. Actual GPT-6/maximum enforcement would additionally require a product/backend/API surface that exposes and persists model-family and reasoning-effort routing fields. No scheduler or permission change was attempted in this run.

---

```yaml
ledger_delta:
  worker: R15
  source:
    id: I0076
    title: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2"
    source_url: "https://arxiv.org/abs/1302.6958"
    exact_scope: "FBM + BBM + independence of complete centered forward/backward half-processes at an arbitrary random T; decide whether 2BM follows"
    excluded: "Problem 7.5; deterministic-time substitutes; stopping-time strengthening; posted/settled work"
  native_metric:
    name: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_frozen_positive_route: "2/4"
    movement: NO_MOVEMENT
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    unchanged_count: "FROZEN_AFTER_SIX_UNCHANGED_RUNS"
  successor_gate:
    before: 0
    after: 0
    unit: "free READY+CLOSABLE successors"
    evidence: "R06 gate commit 502c2216976341d9cdd6285846b9fa74b8b6e692"
  tried_moves:
    - "#18 SAY IT IN ANOTHER LANGUAGE — signed three-atom cumulant representation"
    - "#25 COUNT THE SAME THING TWICE — support-polynomial fifth moment versus cumulant derivative"
    - "#7 TAKE THE LIMIT — regular and singular delta->0 recovery of balanced branches"
    history_note: "all 30 Section-B moves were already exhausted on R15/F0111 by the 20260919_0605Z report; these are new applications, not falsely claimed unused numbers"
  retained_screen:
    id: F0111
    source: "Talagrand Problem 10.9"
    disposition: "PENDING / NOT READY / SELF_CHECK_ONLY / NOT CLAIMED"
    movement:
      - "explicit unequal-amplitude cubic-null curve k(delta,z), x(delta,z), y(delta,z)"
      - "strict fourth-order positivity for every genuine unequal-amplitude Hessian-null direction"
      - "complete exclusion of C=0 two-block Hessian-null mechanism"
      - "positive-weight candidates reduced to three scalar z-regimes after orientation"
      - "balanced positive/negative C branches recovered as singular/regular limits"
  remaining_obligation: "use nonnegative coefficient / graph-flow constraints to eliminate or realize the three surviving null regimes; separately continue second-contact obstruction; no general mixed-sign compression theorem yet"
  evidence:
    idea_commit: 7a3714bc812e6eafbc5b2a04f3650959e98ffeb3
    checker_commit: d1506179fc3e9822002c2012f7c3a0041db24a14
    checker_output_commit: d93dd25ab15ab934c29b3223e3e410044f8fcb22
    checker_result: ALL_EXACT_SYMBOLIC_CHECKS_PASS
  audits: []
  closure_claim: false
```
