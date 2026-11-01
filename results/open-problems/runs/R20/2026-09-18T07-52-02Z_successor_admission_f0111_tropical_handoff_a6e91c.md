Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max=1213`, retirement count `6`; methods #2 ATTACK THE NEGATION FIRST, #14 FIND THE GROUP ACTING, #29 ADD THE POINTS AT INFINITY.**

# R20 successor admission — F0111 ray non-refutation, symmetric reduction, and tropical rigidity handoff

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R20, CLOSABLE OUTSIDE.

All mathematical statements newly derived below are **SELF_CHECK_ONLY**. They are proved on the page, but no independent fleet audit is claimed.

## 1. Continuity, source status, ownership, and exclusions

I did **not** reopen Afonso S. Bandeira, Randomstrasse 2025 Conjecture 26 / intake I0100. Its six-unchanged-run CLOSABLE handoff remains controlling. The historical canonical claim `operations/claims/I0100.md` still records R20 ownership and the exact source normalization; the later immutable R20 handoff records retire active attack after six unchanged runs. Both facts are preserved.

The frozen source metric remains

`p_max = 1213`,

with complete retained exact primal/dual certified prime set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

For prime `p = 1 mod 4`, `G_{p,1}` is the Paley graph induced on the nonzero squares, equivalently the neighbor set of `0`; the target quantity is the source-normalized Lovasz theta of the **complement**,

`T_p = theta(complement G_{p,1})`,

with target `T_p ~ sqrt(p/2)`. This is not Conjecture 27 two-localization, Conjecture 28 degree-four SOS, or Conjecture 29 Paley ETF/RIP. Numerical SDP values remain non-certificates.

Fresh public check on 2026-09-18: the current Jig/Randomstrasse root `https://jig.so/p/7` is still titled “Is the Lovasz theta of the Paley 1-localization asymptotic to sqrt(p/2)?” and still labels the root **Open**. The page records kernel-checked sufficient reductions but does not claim the asymptotic. Therefore I0100 remains `OPEN / PARTIAL / RETIRED-HANDOFF`, and its retirement count stays frozen at `6` rather than increasing during successor screening.

Before new mathematics I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical I0100 claim, newest own R20 reports through

`runs/R20/2026-09-18T07-25-00Z_successor_admission_f0111_gap_cover_c4a91e.md`,

neighboring R15 F0111 work through

`runs/R15/20260918_0612Z_successor_admission_f0111_fkg_sendov_g51a.md`,

and current coordinator state through

`operations/task_health/runs/2026-09-18T055500Z/status.md`.

The coordinator still reports no newly promoted free READY target in its bounded pass. Current queue search also shows that several superficially attractive historical candidates have since been claimed, reserved, or resolved. A direct current fetch of `operations/claims/F0111.md` returned 404, but current admission reports classify F0111 as an active pending lead already under screening, not as READY dispatch inventory. I therefore create no claim.

The admission metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

## 2. F0111 source fidelity and current-literature check

The screening problem is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 (`F0111`). For the threshold up-class

`A_{n,k} = {X subset [n] : |X| >= k}`

and independent coordinates with

`P_t(i in X)=1-exp(-t_i)`,

define

`F_{n,k}(t) = -log P_t(|X|<k)`.

Talagrand's `C_gamma` requirement asks whether one universal `gamma>0` works for every `n,k` so that, for every base point `q>=0`, there exists a multilinear polynomial with nonnegative coefficients and no constant term,

`P(t)=sum_{empty != I subset[n]} beta_I t_I`, `beta_I>=0`,

satisfying

`F_{n,k}(t) <= P(t)` for every `t>=0`,

and

`P(gamma q) <= gamma F_{n,k}(q)`.

I rechecked the primary Talagrand PDF and dated exact-title / `Problem 10.9` / `C_gamma` searches on 2026-09-18. The bounded search recovered the original source and related DeMarco--Kahn and Frankston--Kahn--Park Talagrand-problem literature, but no accessible later theorem explicitly claiming this exact heterogeneous-`q`, positive-multilinear-majorant statement. This is bounded negative evidence, not a novelty certificate or a worldwide openness assertion.

The carried-forward exact formula is, with `y_i=exp(t_i)-1` and `Z_j(y)=sum_{r=0}^j e_r(y)`, 

`F_{n,k}(t)=sum_i t_i-log Z_{k-1}(y)`.

Previous R20 work also established the threshold-gap calculus and then proved that the tempting route “certify every gap independently and compose” is impossible already at the first gap. This run does not rederive that work.

---

## 3. Method #2 — ATTACK THE NEGATION FIRST: the most immediate ray obstruction vanishes for `k=2`

Any source-valid certificate at base `q` necessarily implies

`F_{n,k}(gamma q) <= P(gamma q) <= gamma F_{n,k}(q)`.       (3.1)

Therefore a single `q` violating

`F_{n,k}(gamma q) <= gamma F_{n,k}(q)`                      (3.2)

would refute membership in `C_gamma` before any coefficient search. I attacked this necessary condition first.

For `k=2` there is an exact no-refutation theorem.

### R20-F0111-RAY2 — radial sublinearity for the two-threshold hazard

For every `n>=2`, every `t>=0`, and every `0<=lambda<=1`,

`F_{n,2}(lambda t) <= lambda F_{n,2}(t)`.                   (3.3)

#### Proof

For `k=2`,

`F_{n,2}(t)=sum_i t_i-log(1+sum_i(exp(t_i)-1)).`             (3.4)

Put `x_i=exp(t_i)-1>=0` and

`f_lambda(x)=(1+x)^lambda-1`.

For `0<=lambda<=1`, `f_lambda` is nonnegative, increasing, concave and satisfies `f_lambda(0)=0`. Any such concave function is subadditive: for `x,y>=0`, concavity gives

`f_lambda(x) >= [x/(x+y)] f_lambda(x+y)`,

`f_lambda(y) >= [y/(x+y)] f_lambda(x+y)`,

so `f_lambda(x)+f_lambda(y)>=f_lambda(x+y)`. Iteration yields

`sum_i f_lambda(x_i) >= f_lambda(sum_i x_i)`.

Equivalently,

`1+sum_i((1+x_i)^lambda-1) >= (1+sum_i x_i)^lambda`.        (3.5)

Taking logarithms and substituting `1+x_i=exp(t_i)` into (3.4) gives exactly (3.3). QED.

Thus the strongest zero-cost necessary test (3.2) cannot refute the `k=2` threshold problem for any candidate `gamma` in `(0,1]`. This does **not** prove `C_gamma`: it only removes a natural negation route.

---

## 4. Method #14 — FIND THE GROUP ACTING: homogeneous base points reduce exactly to elementary-symmetric certificates

Fix `n,k`, a homogeneous base point

`q=M 1_n`, `M>0`,

and suppose `P` is any source-valid positive multilinear certificate at this base.

### R20-F0111-SYM1 — exact `S_n` symmetrization

There is a certificate with the same budget of the form

`P_bar(t)=sum_{r=1}^n c_r e_r(t)`, `c_r>=0`.                (4.1)

#### Proof

Define

`P_bar(t)=(1/n!) sum_{sigma in S_n} P(t_sigma)`.

Because `F_{n,k}` is permutation-invariant,

`F_{n,k}(t)=F_{n,k}(t_sigma)<=P(t_sigma)`

for every permutation, so averaging preserves the global majorant. Averaging preserves multilinearity and nonnegative coefficients. Since `q` is fixed by every permutation,

`P_bar(gamma q)=P(gamma q)`,

so the budget is unchanged. Every symmetric multilinear polynomial is a linear combination of the elementary symmetric polynomials `e_r`, and coefficient positivity gives `c_r>=0`. QED.

This is more than a cosmetic reduction: all homogeneous-base obstruction or construction searches may be done in the `n` nonnegative coefficients `(c_1,...,c_n)`, rather than the full `2^n-1` coefficient cone.

A carried-forward degree-drop bound also gives the exact symmetric global linear envelope

`F_{n,k}(t) <= [(n-k+1)/n] sum_i t_i`.                      (4.2)

It is asymptotically sharp on the homogeneous high-activity ray but is strictly too expensive for the finite-base Talagrand budget; the next section identifies exactly what every certificate must approach at infinity.

---

## 5. Method #29 — ADD THE POINTS AT INFINITY: unique tropical first-order certificate

Fix integers `2<=k<=n` and write

`m=n-k+1`.

The projective high-activity limit of the threshold hazard is explicit.

### R20-F0111-TROP1 — tropical limit

For every fixed `x in R_+^n`, with coordinates sorted as

`x_(1)>=x_(2)>=...>=x_(n)`, 

we have

`lim_{M->infinity} F_{n,k}(M x)/M
 = Phi_{n,k}(x)
 = sum_i x_i-sum_{j=1}^{k-1}x_(j)
 = sum_{j=k}^n x_(j).`                                     (5.1)

#### Proof

From the exact formula,

`F_{n,k}(Mx)=M sum_i x_i-log Z_{k-1}(exp(Mx)-1)`.

`Z_{k-1}` is a finite sum of monomials of degrees at most `k-1`. Its largest exponential rate is obtained by selecting the `k-1` largest coordinates (zero coordinates cause no problem), hence

`(1/M)log Z_{k-1}(exp(Mx)-1) -> sum_{j=1}^{k-1}x_(j)`.

Subtracting proves (5.1). QED.

The crucial rigidity statement follows.

### R20-F0111-TROP2 — any homogeneous high-activity certificate has one unique first-order projective limit

Fix `gamma>0`. Suppose there is an unbounded sequence `M_l -> infinity` and, for each `M=M_l`, a source-valid certificate at homogeneous base `M 1_n`. By the exact symmetrization above write it as

`P_M(t)=sum_{r=1}^n c_{r,M} e_r(t)`, `c_{r,M}>=0`.          (5.2)

Then along a subsequence the rescaled coefficients

`a_{r,M}:=M^(r-1)c_{r,M}`

converge, and every such subsequential limit is forced to be

`a_1=m/n`, `a_r=0` for every `r>=2`.                        (5.3)

Equivalently, the unique first-order projective certificate is

`Q_infinity(x)=(m/n) sum_i x_i`.                            (5.4)

#### Proof

At the scaled homogeneous base,

`P_M(gamma M 1_n)
 = sum_r c_{r,M} binom(n,r)(gamma M)^r
 <= gamma F_{n,k}(M1_n)`.

Divide by `M`:

`sum_r binom(n,r) gamma^r a_{r,M}
 <= gamma F_{n,k}(M1_n)/M`.                                 (5.5)

The right side tends `gamma m`, because

`F_{n,k}(M1_n)=mM-log binom(n,k-1)+o(1)`.                   (5.6)

All terms on the left of (5.5) are nonnegative, so every `a_{r,M}` is bounded. Pass to a convergent subsequence and call the limits `a_r>=0`.

For fixed `x>=0`, global majorization gives

`F_{n,k}(Mx)/M <= P_M(Mx)/M
                = sum_r a_{r,M} e_r(x)`.

Using (5.1) and passing to the subsequence,

`Phi_{n,k}(x) <= Q(x):=sum_r a_r e_r(x)`.                   (5.7)

The budget limit from (5.5) is

`sum_r binom(n,r) gamma^r a_r <= gamma m`.                  (5.8)

Now evaluate (5.7) at `x=lambda 1_n`, `lambda>0`. Since

`Phi_{n,k}(lambda 1_n)=m lambda`,

we have

`sum_r a_r binom(n,r) lambda^r >= m lambda`.

Divide by `lambda` and let `lambda downarrow 0` to obtain

`n a_1 >= m`.                                                (5.9)

But the `r=1` term in (5.8) is already `gamma n a_1>=gamma m`. Since all remaining terms are nonnegative and their total must be at most `gamma m`, equality is forced throughout:

`a_1=m/n`, and `a_r=0` for `r>=2`.

This proves (5.3)--(5.4). QED.

Finally, (5.4) really does dominate the tropical target:

`sum of the m smallest coordinates <= (m/n) sum of all n coordinates`,

because the average of the `m` smallest numbers is at most the overall average. Equality for `2<=k<=n` occurs only on the diagonal `x_1=...=x_n`.

### Interpretation

This kills another natural counterexample route. A homogeneous high-activity obstruction cannot appear at first projective order: the source budget and global majorization force exactly the same unique linear tropical envelope, and that envelope is valid. Any genuine obstruction (or any proof of the source conjecture) must therefore live in at least one of:

1. the **second-order boundary layer near the projective diagonal**;
2. genuinely heterogeneous multiscale base points not seen by homogeneous compactification;
3. a mixed-degree positive certificate whose higher-degree coefficients vanish at first order but repair the finite-activity budget.

This is a strict narrowing of the mathematical search space, not a closure result.

---

## 6. Stuck/handoff report for F0111 screening

F0111 has now consumed repeated successor-screening runs without becoming a genuinely CLOSABLE target. Under the owner protocol I stop spending R20 runs on further F0111 lemmas after this report unless it is later reassigned with a fresh route.

### (a) Exact blocking statement

A source closure still requires one universal constant `gamma>0` such that

`for every n,k,q>=0 there exists P_q(t)=sum_{I!=empty} beta_I(q)t_I, beta_I(q)>=0,`

with

`F_{n,k}(t)<=P_q(t) for all t>=0`

and

`P_q(gamma q)<=gamma F_{n,k}(q)`.                            (6.1)

No route so far supplies the required `q`-adaptive **mixed-degree** envelope with a uniform budget.

### (b) Routes tried and precise failure modes

- **Pure degree `k` / Harris--FKG envelope:** `F_{n,k}<=e_k(t)` is global and exact enough near zero, but its budget overpays by powers of a large activity on dense rays.
- **Degree-drop / saturation envelopes:** exact lower-degree majorants match saturated faces, but every single pure degree-drop choice fails on a `k-1` heavy plus light-tail multiscale base.
- **Linear fractional-cover gap envelopes:** exact and optimizable, but they overpay the small-activity order `epsilon^j` by an order-`epsilon` cost.
- **Tangent majorant family:** gives legitimate positive mixed-degree global envelopes, but one-scale tangents spill superlinear mass into the heavy coordinates and miss the source budget.
- **Independent gap certification:** impossible already for `D_1`; axis restrictions force singleton coefficients whose budget is too large at an interior base.
- **Isolated first-gap insertion certification:** no uniform standalone certificate scale; the outer insertion kernel must share slack with the inner gap rather than pay for it independently.
- **Symmetric/orbit dual negation routes (neighboring R15):** no source refutation; current one-orbit families are too weak.
- **Direct radial necessary condition (this run):** for `k=2`, `F(lambda t)<=lambda F(t)` holds identically for `0<=lambda<=1`, so the easiest budget obstruction cannot occur.
- **Homogeneous first-order infinity obstruction (this run):** impossible; the unique projective limit is the valid linear envelope `(n-k+1)/n sum t_i`.

### (c) What a proof needs that no tried route contains

It needs a **single positive multilinear construction that changes effective degree with the saturation pattern of `q` while preserving the budget through the outer threshold-hazard cancellation**. In particular it cannot pay for every adjacent gap separately, and it cannot be merely a convex mixture of whole global degree-drop majorants whose scaled costs are all above the target.

### (d) Simplest source-relevant special case still unproved here

`k=2`, `n>=3`, arbitrary heterogeneous positive base `q`.

The `n=2,k=2` all-elements/two-variable kernel is already handled by Talagrand's source theorem, while arbitrary heterogeneous `n>=3` still contains the first genuinely many-coordinate budget interaction.

### (e) Nearest solved source case and missing ingredient

Talagrand's all-elements endpoint (`k=n`) and the two-variable kernel theorem have explicit positive multilinear coefficients with a uniform source budget. The threshold problem lacks a composition rule that keeps those local coefficients budget-tight when many overlapping potential `k`-sets share coordinates. Disjoint-block composition from the source does not address this overlap.

**Handoff disposition:** `F0111 = OPEN-looking / HARD / HANDOFF_AFTER_REPEATED_SCREEN / NOT_CLOSABLE_READY / NOT_CLAIMED`.

---

## 7. Admission conclusion

No candidate checked this run crossed all required gates simultaneously:

1. exact outside source and source-matching scope;
2. current-open status after later-literature check;
3. genuinely CLOSABLE full-source metric rather than a finite decoration;
4. no canonical owner/reservation/active admission conflict.

Therefore

`E_ready: 0 -> 0`.

I created **no successor claim** and **no decorative exact checker**. The new claims in Sections 3--5 are theorem-sized analytic statements with complete proofs on the page, not finite claims; they remain SELF_CHECK_ONLY pending any future independent audit.

The next admission-search moves, on a **different candidate**, are:

- **#6 DEFORM TO A POINT YOU CAN SOLVE**;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE**;
- **#30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME**.

## 8. Model/scheduler control status

The limitation is still real in the interface exposed to this worker. The task-management surface provides task title/prompt, schedule/timing mode, enabled state, and task ID; it provides **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed hour-long runtime field**. Hence GPT-6/maximum can only be requested in prompt text here, not enforced or authenticated by this worker.

The historical P26 response `You cannot modify this task` was **authorization-context-specific**, not a permanent global fact: current repository reconciliation records a later successful P26 prompt update from an authorized context. The lawful workaround is therefore to use the owning/admin-authorized context, a supported ownership-transfer/admin surface, or platform support. It is not to duplicate the task or bypass permissions. This R20 run made no scheduler change.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  lane: CLOSABLE_OUTSIDE
  source:
    retired_handoff: "Afonso S. Bandeira, Randomstrasse 2025, Conjecture 26 / intake I0100"
    successor_probe: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9 / F0111"
  metric:
    name: E_ready
    before: 0
    after: 0
  retired_source_metric:
    name: p_max
    value: 1213
    covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
    retirement_count: 6
  status: SUCCESSOR_ADMISSION_REQUIRED
  unchanged_count: UNKNOWN
  methods_actually_tried: [2,14,29]
  candidate_probe:
    id: F0111
    disposition: HANDOFF_HARD_NOT_CLOSABLE_READY_NOT_CLAIMED
    claim_created: false
  substantive_movement:
    - "proved exact radial sublinearity F_{n,2}(lambda t) <= lambda F_{n,2}(t) for 0<=lambda<=1, eliminating the easiest necessary-condition refutation"
    - "proved exact S_n symmetrization of every homogeneous-base positive multilinear certificate"
    - "proved tropical limit Phi_{n,k}=sum of n-k+1 smallest coordinates and uniqueness of the first-order homogeneous certificate (n-k+1)/n * sum_i x_i"
    - "handed off F0111 after repeated HARD-leaning screens; no further R20 screening lemmas without reassignment"
  remaining_obligation: "find a current-open, source-exact, ownership-clear, genuinely CLOSABLE outside successor and create a claim only after every admission gate passes"
  evidence:
    - "operations/claims/I0100.md"
    - "runs/R20/2026-09-18T07-25-00Z_successor_admission_f0111_gap_cover_c4a91e.md"
    - "runs/R15/20260918_0612Z_successor_admission_f0111_fkg_sendov_g51a.md"
    - "operations/task_health/runs/2026-09-18T055500Z/status.md"
    - "operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md"
    - "current Jig Randomstrasse Conjecture 26 root checked 2026-09-18"
    - "Talagrand STOC 2010 Problem 10.9 primary PDF checked 2026-09-18"
  audit_ids: []
  next_methods: [6,17,30]
```

**NO I0100 CLOSURE CLAIM. NO F0111 CLAIM. R20 remains `SUCCESSOR_ADMISSION_REQUIRED`.**