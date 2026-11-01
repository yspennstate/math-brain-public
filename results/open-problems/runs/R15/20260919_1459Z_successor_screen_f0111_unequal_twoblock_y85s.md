Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the fixed four-obligation metric remains `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical positive-route `2/4` is only the frozen handoff value. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, the balanced mixed-sign two-block calculus is extended to every unequal-amplitude two-block direction; the second-contact condition is one exact scalar equation whose derivative has a quadratic numerator, equal partition functions are impossible unless the amplitudes are equal, and a closed monotonicity threshold gives a unique candidate endpoint ratio with its side of `1` determined by the amplitude imbalance. Methods #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**

# R15 retained screen — unequal-amplitude two-block transfer calculus for the quadratic `k=2` Talagrand hazard

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 from PENDING/NOT READY, establish publication novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Required continuity, source fidelity, ownership, and exclusions

I continued from

`runs/R15/20260919_1424Z_successor_screen_f0111_balanced_twoblock_x84r.md`

rather than restarting. Before new mathematics I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the I0076 intake row in `probability_1000_intake_I_20260914/problems.jsonl` and the six-run handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the newest own R15 report above and the latest neighboring CLOSABLE successor reconciliation visible in R20.

The latest neighboring R20 reconciliation checked the complete intervening claim delta and still found `E_READY_SUCCESSOR: 0 -> 0`: the only explicit newly released source was classified HARD, while local CLOSABLE retirements had not become canonical owner-clear releases. Thus there is still no lawful READY+CLOSABLE successor for R15 to claim. I did not steal an owned target, convert a PENDING queue row into READY, or revive an operationally retired source.

### Exact I0076 source rechecked

I reopened Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.

The source notions remain exactly:

- FBM: there exist random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random time `S` at which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2: `X` is FBM and BBM and there exists an arbitrary random time `T` such that the two complete centered half-processes `(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}` are independent. Must `X` be 2BM?

There is no stopping-time assumption on `T`, no deterministic-time substitute, and neither half at `T` is separately assumed Brownian. Problem 7.5 is a different source problem and remains excluded.

The controlling I0076 handoff is unchanged. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but R15 eliminated source-valid independent seam existence. The later Brownian-prefix/BES candidate had exact seam independence but R15 proved it is actually 2BM. Hence no frozen counterexample candidate survives. The positive-route handoff froze at `2/4` after six unchanged runs and operationally retired I0076 from hourly attack.

Fresh dated public searches on 2026-09-19 using the exact paper title, authors, arXiv ID and `Problem 7.2` recovered the original paper/publication and related Brownian-pasting literature but no accessible later primary source explicitly claiming a solution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

### F0111 current-primary-literature check

Fresh 2026-09-19 searches for Talagrand discrete convexity / `k=2` / quadratic majorant recovered:

- Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), which reformulates the discrete Convexity Conjecture via `k`-thresholds and proves substantial classes rather than the full conjecture;
- Chen Li, arXiv:2609.08967 (2026-09-08), resolving the fractional version;
- Jinyoung Park, arXiv:2609.14681 (2026-09-13), giving a dimension-independent comparison explicitly described as progress toward the conjecture;
- Fang--Wang, arXiv:2609.18458 (2026-09-16), which applies Li's method to Talagrand Conjecture 7.8 (and consequently 7.3 and 7.11), not Problem 10.9.

Targeted searches did not retrieve a primary source stating the unequal-amplitude endpoint-transfer formulas below. Negative search evidence does not establish novelty; novelty remains `UNVERIFIED`.

The preceding R15 run used #5/#18/#30. This run uses the distinct triple #11/#20/#24.

---

## 2. Carried `k=2` setup

For the cardinality-two threshold hazard,

`F(t)=F_n(t)=sum_i t_i - log S(t)`,

`S(t)=sum_i exp(t_i)-(n-1)`,                                 (2.1)

for `t in R_+^n`, `n>=2`.

A quadratic nonnegative polynomial is

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,

`A_i,B_ij>=0`.                                                (2.2)

A global quadratic certificate at an interior base `q` means

`P(t)>=F(t)` for every `t>=0`, and `P(q)=F(q)`.               (2.3)

Value contact at an interior point implies gradient contact.

Earlier R15 runs proved that any genuinely isolated first bifurcation must use a mixed-sign direction. The immediately preceding run solved the first symmetric quotient

`h=c 1_J-c 1_K`.

This run removes the equal-amplitude restriction and studies

`h=a 1_J-b 1_K`, `a,b>0`,                                    (2.4)

for disjoint nonempty coordinate blocks `J,K`.

Write

`A=sum_{i in J} exp(q_i)>0`,

`B=sum_{i in K} exp(q_i)>0`,

`C=sum_{i notin J union K} exp(q_i)-(n-1)`.                  (2.5)

Along `q+s h`,

`S(s)=A exp(a s)+B exp(-b s)+C`.                             (2.6)

Introduce the mean and imbalance parameters

`m=(a+b)/2>0`, `d=(a-b)/2`, so `|d|<m`,                     (2.7)

and

`alpha=m/sinh(m)`.                                            (2.8)

---

## 3. Method #11 — dualize the two exponentials into a second-order transfer equation

Set

`U(s)=S(s)-C=A exp((m+d)s)+B exp(-(m-d)s)`.                  (3.1)

Unlike a direct coefficient calculation, `U` is exactly the solution of the constant-coefficient equation

`U''-2d U'-(m^2-d^2)U=0`.                                   (3.2)

Suppose `q` and `q+h` are two distinct interior contacts of the same global quadratic certificate. Normalize

`x=S(0)>0`, `r=S(1)/S(0)>0`, `k=C/S(0)`.                    (3.3)

Then

`U(0)=x(1-k)`, `U(1)=x(r-k)`.                                (3.4)

Since `A,B>0`, the endpoint ratio of `U` is a strict convex combination of the two exponential multipliers:

`exp(-b) < (r-k)/(1-k) < exp(a)`.                            (3.5)

In particular `k<1` and `r-k>0`.

Solving (3.2) from its endpoint values gives the exact transfer formulas

`U'(0)/x`
`=d(1-k)+alpha[exp(-d)(r-k)-(1-k)cosh(m)]`,                  (3.6)

`U'(1)/x`
`=d(r-k)+alpha[(r-k)cosh(m)-exp(d)(1-k)]`.                   (3.7)

Let `ell(s)=log S(s)`. The restriction of `P` to the line is quadratic, so two value-and-gradient contacts force the certificate-independent Hermite identity

`ell'(0)+ell'(1)=2 log r`.                                   (3.8)

Combining (3.6)--(3.8) yields the exact scalar second-contact equation

`H_{m,d,k}(r)=0`,                                             (3.9)

where

`H_{m,d,k}(r)`
`=d(1-k)+alpha[exp(-d)(r-k)-(1-k)cosh(m)]`
` + {d(r-k)+alpha[(r-k)cosh(m)-exp(d)(1-k)]}/r`
` -2 log r`.                                                  (3.10)

Thus every unequal-amplitude two-block second contact is reduced from a high-dimensional polynomial search to one scalar endpoint ratio `r`, subject to the strict feasibility interval (3.5).

### Derivative normal form

Define

`P0=alpha exp(-d)>0`,                                         (3.11)

`beta=d k+alpha[exp(d)(1-k)+k cosh(m)]`.                     (3.12)

Exact differentiation of (3.10) gives

`H'(r)=P0-2/r+beta/r^2`
`     =(P0 r^2-2r+beta)/r^2`.                                (3.13)

Hence for each fixed `(m,d,k)`, `H` has at most two critical points and therefore at most three distinct positive roots. Combining with (3.5), at most three endpoint partition ratios can even pass the certificate-independent two-contact test.

---

## 4. Method #20 — find why the balanced equal-partition shortcut fails

In the balanced preceding run, `r=1` was always a Hermite root and required its own global segment analysis. In the unequal-amplitude family the exact evaluation is

`H_{m,d,k}(1)`
`=2(1-k)[d-m sinh(d)/sinh(m)]`.                              (4.1)

Because

`x -> sinh(x)/x`

is strictly increasing for `x>0`, the bracket in (4.1) has exactly the sign of `d` when `|d|<m`. Since `1-k>0`,

`sign H(1)=sign d`.                                           (4.2)

Therefore

`boxed: H(1)=0 iff d=0 iff a=b.`                              (4.3)

So **an unequal-amplitude two-block second contact can never have equal endpoint partition functions**:

`a != b  =>  S(q+h) != S(q)`.                                (4.4)

This identifies exactly why the preceding reflection/equal-partition algorithm does not extend: its anchor root disappears immediately when the positive and negative amplitudes separate.

---

## 5. Method #24 — extremize the derivative and get a sharp monotonicity threshold

The quadratic numerator in (3.13) is controlled by the product `P0 beta`. Define

`L(m,d)=d+alpha[cosh(m)-exp(d)]`.                             (5.1)

A direct identity gives

`P0 beta=alpha^2+k alpha exp(-d)L(m,d)`.                     (5.2)

The function `d -> L(m,d)` satisfies

`L(m,-m)=L(m,m)=0`,

`partial_d^2 L(m,d)=-alpha exp(d)<0`.                         (5.3)

Hence strict concavity implies

`L(m,d)>0` for every `|d|<m`.                                (5.4)

Also `0<alpha<1`. Define the exact threshold

`Kappa(m,d)`
`=(1-alpha^2)/(alpha exp(-d)L(m,d))>0`.                       (5.5)

If

`k>=Kappa(m,d)`,                                               (5.6)

then `P0 beta>=1`. The discriminant of the numerator in (3.13) is

`4(1-P0 beta)<=0`,                                             (5.7)

so `H` is strictly increasing on `(0,infinity)` (in the equality case its derivative vanishes at only one isolated point). Moreover (5.6) implies `beta>0`, so

`H(r)->-infinity` as `r->0+`,

`H(r)->+infinity` as `r->infinity`.                           (5.8)

Thus there is exactly one positive Hermite-compatible endpoint ratio `r_*`. Equation (4.2) locates it without solving it:

`d>0 (a>b)  =>  r_*<1`,

`d<0 (a<b)  =>  r_*>1`.                                      (5.9)

Finally, when `d=0`, (5.5) reduces exactly to the balanced threshold from the preceding run:

`Kappa(m,0)`
`= [((sinh m)/m)^2-1]/[cosh m-1]`.                           (5.10)

So the new transfer calculus genuinely extends, rather than replaces, the balanced theorem.

### What this does and does not prove

This run does **not** eliminate every unequal-amplitude two-block second contact. Outside the monotonicity region (5.6), equation (3.9) can have up to three positive roots, and even inside (5.6) the unique root still has to be confronted with the strict feasibility interval (3.5), endpoint curvature, and the full global-majorant condition.

What is new and exact is:

1. arbitrary amplitudes `(a,b)` have a one-dimensional endpoint equation;
2. its derivative complexity is only quadratic;
3. equal partition functions are rigorously impossible unless `a=b`;
4. an explicit threshold gives uniqueness and determines which side of `1` the sole candidate lies on.

The next useful attack is to combine (3.5) and endpoint nonnegative-gap curvature with the unique-root regime, then treat the complementary discriminant-positive regime; in parallel, derive the unequal-amplitude Hessian-null equation from the same transfer system. A stronger eventual goal is a compression theorem reducing a general mixed-sign extremizer to a two-level displacement.

---

## 6. Exact finite-core validation

Only after the analytic route was found, I added one small symbolic checker for the finite algebraic identities used above:

- `artifacts/R15/f0111_unequal_twoblock_symbolic_y85s.py`
- `artifacts/R15/f0111_unequal_twoblock_symbolic_y85s.out`

The checker uses exact SymPy simplification, no floating-point path sampling. It verifies the ODE, both endpoint transfer identities, the derivative normal form, (4.1), the factorization (5.2), the endpoint/concavity identities for `L`, and the balanced specialization (5.10). The executed archived output ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

This is a self-check, not an independent audit.

---

## 7. Model / scheduler-control truth

This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The exposed scheduler/action schema in this run still offers task title/prompt, schedule or relative start, timing mode, enabled state and ordinary update controls. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution field**. Thus `GPT-6 / maximum` remains a prompt request on this surface rather than an enforceable scheduler setting.

The operative implementation record still documents the P26 ID `6aa7b43682948191b697d72fec69d539` returning `You cannot modify this task` from one authorization context. Repository continuity also records later successful access from an authorized P/C context. The lawful workaround is therefore the owning/authorized workspace/account/API/admin surface for that same task, or platform support if that context still denies access — not a permission bypass, identity substitution, or duplicate schedule. Enforcing GPT-6/maximum additionally requires a product/backend/API surface that actually exposes and persists those routing fields.

No scheduler, permission, email, Drive, public-posting, purchase, or notification mutation was made.

---

## ledger_delta

```yaml
ledger_delta:
  track: R15
  actual_model: GPT-5.6 Sol
  reasoning: UNVERIFIED
  lane: CLOSABLE_OUTSIDE
  native_source:
    source: Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2
    intake: I0076
    source_status: OPEN_PARTIAL_RETIRED_HANDOFF
    fixed_metric_name: four source-matching obligations for one frozen counterexample candidate
    metric_before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    metric_after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_positive_route_handoff: 2/4
    unchanged_count: PRESERVED_AFTER_SIX_RUN_HANDOFF
  successor_gate:
    name: E_READY_SUCCESSOR
    before: 0
    after: 0
    movement: NO_MOVEMENT
    evidence: runs/R20/2026-09-19T14-52-30Z_terminal_wait_campbell_hard_release_p0169_p0458_nonrelease_5e2a91.md
  retained_screen:
    source: Michel Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9 / F0111
    status: SELF_CHECK_ONLY_NOT_CLAIMED
    new_result: unequal-amplitude two-block second-contact transfer reduction and monotonicity threshold
    checked_family: h = a 1_J - b 1_K, a,b>0
    exact_scalar_equation: H_{m,d,k}(r)=0
    exact_root_bound: at_most_3_positive_roots_for_fixed_m_d_k
    equal_partition_rigidity: r=1 iff a=b for Hermite compatibility
    monotonicity_threshold: k >= Kappa(m,d) gives exactly one positive root
  tried_moves:
    - 11 DUALIZE
    - 20 FIND_WHY_THE_ALGORITHM_FAILS
    - 24 FIND_THE_EXTREMAL_OBJECT
  checker:
    source: artifacts/R15/f0111_unequal_twoblock_symbolic_y85s.py
    source_commit: d778d170def8895ee4e7cd8ac797411088fa5ed9
    output: artifacts/R15/f0111_unequal_twoblock_symbolic_y85s.out
    output_commit: f2074c222cd4090cc42dde5eed435fdfd1ab117d
    result: ALL_EXACT_SYMBOLIC_CHECKS_PASS
    audit_class: SELF_CHECK_ONLY
  remaining_obligation: >-
    Do not reopen I0076 absent explicit reassignment. If no owner-clear READY CLOSABLE
    successor appears, continue only the retained NOT-CLAIMED screen: combine the unequal
    two-block scalar equation with feasibility and endpoint curvature, classify the unequal
    Hessian-null branch, and seek a compression theorem from general mixed-sign directions
    to a two-level extremizer. Do not call F0111 solved or novel without full source scope,
    current-priority verification, and two independent audits.
  evidence:
    - runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md
    - runs/R15/20260919_1424Z_successor_screen_f0111_balanced_twoblock_x84r.md
    - runs/R20/2026-09-19T14-52-30Z_terminal_wait_campbell_hard_release_p0169_p0458_nonrelease_5e2a91.md
    - operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md
    - artifacts/R15/f0111_unequal_twoblock_symbolic_y85s.py
    - artifacts/R15/f0111_unequal_twoblock_symbolic_y85s.out
    - Burdzy--Scheutzow arXiv:1302.6958v4 source checked 2026-09-19
    - Ascoli--He--Park--Talagrand arXiv:2608.11183 checked 2026-09-19
    - Park arXiv:2609.14681 checked 2026-09-19
    - Fang--Wang arXiv:2609.18458 checked 2026-09-19
  audit_ids: []
```
