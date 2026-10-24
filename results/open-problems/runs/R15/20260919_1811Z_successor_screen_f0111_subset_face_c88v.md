Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the fixed four-obligation metric remains `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, the previous two-coordinate global-face obstruction is extended to every coordinate subset `J`, with a proved sharp-through-cubic rational lower envelope, an all-subset coefficient barrier, and a base-only exact-contact consequence. Methods used in new roles: #3 PROVE SOMETHING STRONGER, #25 COUNT THE SAME THING TWICE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 retained screen — all-subset global face barriers for the `k=2` threshold hazard

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below about Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 to READY, establish novelty, solve Problem 10.9, or satisfy the fleet's independent-audit closure rule.

## 1. Continuity, source fidelity, ownership, and exclusions

I continued from the immediately preceding immutable R15 report

`runs/R15/20260919_1715Z_successor_screen_f0111_graphflow_face_b87u.md`

rather than restarting. Before doing new mathematics I recovered/read the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 six-run handoff, the newest own R15 report, the neighboring R20/F0111 tropical handoff, the I0076 intake/search history, and the newest coordinator status visible on `master` (`operations/task_health/runs/2026-09-19T175900Z/status.md`).

The newest coordinator state still says that admission scarcity is the operational obstruction: five enabled CLOSABLE successor gates have no admitted current target, and **no newly free CLOSABLE successor was admitted** in that run. `QUEUE.md` likewise still separates PENDING candidates from READY dispatch inventory. I therefore did not steal an owned problem, promote a PENDING row, or manufacture a successor claim.

### Exact I0076 source rechecked

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is BBM if the time reversal is FBM;
- `X` is 2BM if there is one random time `S` for which the complete centered future and past are independent **standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM plus existence of an arbitrary random time `T` for which

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent as complete half-processes forces 2BM. The source does **not** assume `T` is a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is separate and excluded.

The controlling I0076 handoff remains unchanged. The source-Theorem-6.1 process supplies FBM, BBM and non-2BM but was eliminated as a source counterexample because it has no source-valid independent real seam. The later Brownian-prefix/BES construction had exact seam independence but was proved to be 2BM. Hence no frozen counterexample candidate survives. The source metric cannot honestly be scored on a current candidate. The historical positive-route handoff value `2/4` remains historical only; I0076 is `OPEN / PARTIAL / RETIRED-HANDOFF`.

Fresh dated web queries used this run included exact-title / exact-problem searches for `"Forward Brownian Motion" "Problem 7.2"`, `Burdzy Scheutzow "Problem 7.2" Brownian`, and later two-sided/forward-Brownian literature. They recovered the original source and related Brownian splitting/pasting material but no accessible later primary source explicitly claiming a resolution of exact Problem 7.2. This is bounded negative evidence, not a worldwide openness certificate.

### Retained F0111 source/current-literature check

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 / F0111. The primary source asks whether there is a universal `gamma>0` such that every cardinality threshold up-class

`A={X subset S: card X >= k}`

belongs to `C_gamma`. I rechecked the primary PDF and current 2026 literature. Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulate the discrete Convexity Conjecture using `k`-thresholds and prove substantial classes; Jinyoung Park, arXiv:2609.14681 (2026-09-13), gives a dimension-free comparison explicitly described as progress toward the conjecture. Neither accessible source claims the exact all-`n,k,q` positive-polynomial Problem 10.9 statement solved. Novelty of the theorem below remains `UNVERIFIED`.

### Section-B methods

The immediately preceding R15 run used #11/#20/#4. Earlier F0111 history has already used all 30 method numbers at least once, so a globally never-before-used triple is impossible without inventing history. This run therefore uses a different triple in genuinely new roles:

- **#3 PROVE SOMETHING STRONGER** — replace the pair-face inequality by a theorem for every coordinate face size `m>=2`;
- **#25 COUNT THE SAME THING TWICE** — prove the one-dimensional lower envelope both through exact derivative-series cancellation and through its Taylor contact, the latter identifying the optimal cubic denominator constant;
- **#30 ONE SCALE / ONE DIRECTION AT A TIME** — restrict a putative global certificate to one arbitrary equal-coordinate face ray and extract a hierarchy of necessary constraints.

The new route was written **before validation/checking** in

`artifacts/R15/f0111_subset_face_idea_c88v.md`

at creation commit `1494f12d03af65cdb344c87d122670f24c61e5fe`, and was read back at that exact commit. No numerical path sampling is used anywhere below.

---

## 2. Carried `k=2` setup

For the cardinality-two threshold class, write

`F_n(t)=sum_{i=1}^n t_i - log(sum_{i=1}^n exp(t_i)-(n-1))`,       (2.1)

for `t in R_+^n`.

A quadratic positive candidate has the form

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,

`A_i>=0`, `B_ij>=0`.                                            (2.2)

The preceding R15 report proved, by taking a two-coordinate equal ray, that every **global** majorant `P>=F_n` must satisfy a nontrivial pair-face condition. It also produced an exact `n=4` local Hessian-null candidate passing positive coefficients, exact contact, full local PSD, cubic nullity and strict quartic positivity while failing that global pair-face test. That example showed that the remaining obstruction is genuinely global.

The question this run is whether the pair ray is exceptional or is the first member of an all-face hierarchy.

---

## 3. Method #3 — a sharp-through-cubic lower envelope on every equal-coordinate face

Fix an arbitrary coordinate subset `J subset [n]` of size

`m=|J|>=2`,                                                     (3.1)

and put `t=s 1_J`, `s>=0`. All inactive coordinates cancel from the denominator in (2.1), giving the exact one-variable hazard

`f_m(s):=F_n(s 1_J)=m s-log(m exp(s)-(m-1)).`                  (3.2)

Let

`N_m=binom(m,2)=m(m-1)/2`,

`c_m=(2m-1)/3`.                                                (3.3)

### R15-F0111-SUBFACE1 — all-face rational lower envelope

For every integer `m>=2` and every `s>=0`,

`boxed: f_m(s) >= N_m s^2/(1+c_m s).`                         (3.4)

Moreover, among lower envelopes with the same quadratic term and form

`N_m s^2/(1+d s)`,                                             (3.5)

the denominator slope must satisfy `d>=c_m`; hence `c_m` is the smallest possible such slope compatible even locally at the origin.

### Proof of the global inequality

Differentiate (3.2):

`f_m'(s)=m(m-1)(1-exp(-s))/(m-(m-1)exp(-s)).`                 (3.6)

For

`q_m(s)=N_m s^2/(1+c_m s)`,                                   (3.7)

we have

`q_m'(s)=N_m s(2+c_m s)/(1+c_m s)^2`.                         (3.8)

After dividing by `m(m-1)` and clearing positive denominators, `f_m'(s)>=q_m'(s)` is equivalent to

`2(1+c_m s)^2(1-exp(-s))`
` >= s(2+c_m s)(m-(m-1)exp(-s)).`                             (3.9)

Write the difference in (3.9) as

`D_m(s)=A_m(s)+B_m(s)exp(-s)`.                                (3.10)

With `c_m=(2m-1)/3`, direct expansion gives

`A_m(s)`
`=2 + [2(m-2)/3]s + [(m-2)(2m-1)/9]s^2`.                    (3.11)

The three coefficients are nonnegative for every `m>=2`. Multiply (3.10) by `exp(s)`. The polynomial `B_m(s)` cancels **exactly** the coefficients of `s^0,s^1,s^2` in `A_m(s)exp(s)`. For every `k>=3`, the remaining coefficient of `s^k` is

`2/k!`
` + [2(m-2)/3]/(k-1)!`
` + [(m-2)(2m-1)/9]/(k-2)!`,                                 (3.12)

which is strictly positive. Therefore

`exp(s)D_m(s)>=0` for `s>=0`,                                 (3.13)

with strict inequality for `s>0`. Thus `f_m'>=q_m'`. Since both functions vanish at `s=0`, integration proves (3.4).

### Method #25 — the second count identifies the denominator constant

Taylor expansion at the origin gives

`f_m(s)=N_m s^2-N_m c_m s^3+O(s^4).`                         (3.14)

On the other hand,

`N_m s^2/(1+d s)=N_m s^2-N_m d s^3+O(s^4).`                 (3.15)

If (3.5) is a lower envelope in any punctured right-neighborhood of zero, then `f_m(s)-N_m s^2/(1+d s)>=0` for small positive `s`; (3.14)--(3.15) force

`d>=c_m`.                                                     (3.16)

Thus the constant in the global bound (3.4) is not an arbitrary convenient choice: it is the smallest denominator slope allowed by the exact cubic term.

For `m=2`, (3.4) becomes exactly the previous R15 bound

`2s-log(2exp(s)-1) >= s^2/(1+s)`.                             (3.17)

---

## 4. Method #30 — every coordinate subset imposes a global certificate barrier

For the same `J`, define the aggregate coefficients

`A_J=sum_{i in J} A_i`,

`B_J=sum_{i<j, i,j in J} B_ij`.                               (4.1)

Restriction of the global majorant to the equal ray gives

`A_J s+B_J s^2 >= f_m(s)`.                                   (4.2)

By (3.4), for every `s>0`,

`A_J+B_J s >= N_m s/(1+c_m s)`.                              (4.3)

### R15-F0111-SUBFACE2 — all-subset coefficient inequality

Every nonnegative quadratic global majorant `P>=F_n` satisfies, for every `J` with `|J|=m>=2`,

`boxed:`

`A_J >= [3/(2m-1)] (sqrt(N_m)-sqrt(B_J))_+^2,`               (4.4)

where `x_+=max(x,0)`.

### Proof

Rearrange (4.3):

`A_J >= N_m s/(1+c_m s)-B_J s`.                              (4.5)

Take the supremum over `s>=0`. If `B_J>=N_m`, the right derivative at zero is nonpositive and the supremum is zero. If `0<B_J<N_m`, the maximizer satisfies

`1+c_m s=sqrt(N_m/B_J)`,                                     (4.6)

and substitution yields

`sup_{s>=0}[N_m s/(1+c_m s)-B_Js]`
`=(sqrt(N_m)-sqrt(B_J))^2/c_m`.                              (4.7)

The same formula holds at `B_J=0` by taking `s->infinity`. Since `1/c_m=3/(2m-1)`, this is (4.4). QED.

### Block-symmetric form

If on the face `J` the coefficients are block-constant,

`A_i=alpha` for `i in J`,

`B_ij=beta` for distinct `i,j in J`,                          (4.8)

then `A_J=m alpha` and `B_J=N_m beta`, so (4.4) becomes

`boxed:`

`alpha >= [3(m-1)/(2(2m-1))](1-sqrt(beta))_+^2.`             (4.9)

For `m=2`, the prefactor is `1/2`, exactly the old pair-face condition. As `m->infinity` it increases to `3/4`. Thus larger coordinate faces impose strictly stronger per-coordinate singleton budgets on a symmetric block than the pair test alone.

This is a genuine hierarchy of **global** conditions; it does not follow merely from Hessian PSD at a contact point.

---

## 5. Exact-contact consequence: a base-only necessary face inequality

Suppose now that the global certificate is exact at an interior base `q>0`. Put

`r_i=exp(q_i)/(sum_l exp(q_l)-(n-1))`,                        (5.1)

so exact gradient contact gives

`A_i+sum_{j!=i}B_ij q_j=1-r_i`.                              (5.2)

For a fixed `J`, write

`x_J=sum_{i in J}r_i`,

`q_* = min_{i in J}q_i`.                                     (5.3)

Summing (5.2) over `i in J`, every internal edge contributes `B_ij(q_i+q_j)>=2q_*B_ij`, while every edge from `J` to its complement contributes a nonnegative amount. Hence

`A_J <= m-x_J-2q_*B_J`.                                     (5.4)

Combine this with (4.4). Since the actual value `B_J>=0` is unknown, compatibility requires

`m-x_J >= min_{B>=0}`
`{2q_*B + [3/(2m-1)](sqrt(N_m)-sqrt(B))_+^2}.`               (5.5)

The minimum occurs in `0<=B<=N_m`. Setting `y=sqrt(B)` gives a convex quadratic, whose minimizer is

`y_*=[d sqrt(N_m)]/(2q_*+d)`,

`d=3/(2m-1)`.                                                (5.6)

Substitution gives the following entirely base-level obstruction.

### R15-F0111-SUBFACE3 — base-only exact-contact test

For every interior exact-contact base and every `J`, `|J|=m>=2`,

`boxed:`

`m-x_J >= [3m(m-1)q_*]/[3+2(2m-1)q_*].`                     (5.7)

Equivalently,

`x_J <= m-[3m(m-1)q_*]/[3+2(2m-1)q_*].`                     (5.8)

This test is weaker than retaining the actual `B_J`, but it removes the polynomial coefficients completely. A candidate base that violates (5.7) cannot admit any nonnegative quadratic global majorant exact there.

---

## 6. What moved, what did not, and the next route

The native Burdzy--Scheutzow problem did **not** move. It remains operationally handed off after six unchanged substantive runs, and no source result is claimed.

The retained Talagrand screen did move mathematically. Before this run, the global-face obstruction had been proved only on `m=2` coordinate faces. After this run:

1. the ray lower bound exists for **every integer `m>=2`**;
2. its denominator slope `(2m-1)/3` is forced by the cubic expansion within this rational family;
3. every coordinate subset supplies the coefficient barrier (4.4);
4. exact contact supplies the coefficient-free base test (5.7).

This matters because the preceding run proved that local Hessian-null/graph-flow feasibility is too weak: when both sign blocks have at least two vertices, the bare nonnegative null-row equations are automatically solvable. The all-subset inequalities now give a family of genuinely global constraints that can be combined with those flows simultaneously.

The next useful attack is therefore **not** another one-dimensional derivative order. It is to impose (4.4) on every subset of a mixed-sign block-symmetric Hessian-null candidate and ask whether the graph-flow degrees can satisfy the complete face hierarchy at once. A successful compression theorem would show that one face becomes extremal; a failure would identify the first configuration requiring a genuinely nonsymmetric global obstruction.

No numerical path samples were used, and I did not manufacture a checker merely to certify a theorem whose proof is analytic and parameter-uniform. The finite-core requirement is therefore not applicable in this run; the theorem-sized claims are proved on the page.

---

## 7. Model/scheduler control status

The exposed scheduler/task interface still has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution control. `GPT-6 / maximum` is therefore prompt text only in this environment; I do not claim it was enforced.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context. The current root `RESULTS.md` records that a later authorized P/C context successfully updated P26. The lawful workaround for an edit-denied task is therefore to operate from the owning/authorized account/workspace/API/admin context, not to duplicate the task or bypass permissions. A genuine GPT-6/maximum guarantee additionally requires a product/backend/API surface that exposes, persists and attests those routing fields.

No scheduler, permission, Gmail, email, Drive, public-posting, or shared-root change was attempted in this run.

---

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2 / I0076"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE; historical positive-route handoff 2/4"
  native_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE; historical positive-route handoff 2/4"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "PRESERVED_AFTER_SIX_RUN_HANDOFF"
  successor_gate:
    free_ready_closable_before: 0
    free_ready_closable_after: 0
    status: "NO LAWFUL FREE SUCCESSOR FOUND"
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9 / F0111; k=2 only"
    status: "PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
    secondary_metric: "coordinate-face sizes covered by proved global rational barrier"
    secondary_before: "m=2 only"
    secondary_after: "all integers m>=2"
    new_claims:
      - "R15-F0111-SUBFACE1: f_m(s) >= binom(m,2)s^2/(1+(2m-1)s/3), with cubic-sharp denominator slope"
      - "R15-F0111-SUBFACE2: A_J >= 3/(2m-1) (sqrt(binomial(m,2))-sqrt(B_J))_+^2 for every coordinate subset J"
      - "R15-F0111-SUBFACE3: exact-contact base test m-x_J >= 3m(m-1)q_min/[3+2(2m-1)q_min]"
  tried_moves: [3, 25, 30]
  preceding_moves: [11, 20, 4]
  remaining_obligation: "For I0076: a new source-valid frozen candidate or full source-level implication proof. For retained F0111: combine all-subset global barriers with mixed-sign null-flow/PSD/contact constraints; arbitrary k and the universal-gamma source problem remain open."
  evidence:
    - "runs/R15/20260919_1715Z_successor_screen_f0111_graphflow_face_b87u.md"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "artifacts/R15/f0111_subset_face_idea_c88v.md @ 1494f12d03af65cdb344c87d122670f24c61e5fe"
    - "Burdzy--Scheutzow primary PDF, Definition 2.1 and Problem 7.2, rechecked 2026-09-19"
    - "Talagrand primary PDF, Problem 10.9, rechecked 2026-09-19"
    - "Ascoli--He--Park--Talagrand arXiv:2608.11183 and Park arXiv:2609.14681, checked 2026-09-19"
  audits: []
  closure: false
```
