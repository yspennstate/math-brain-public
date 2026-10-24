Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat >= b21_desc -> B_cat >= b21_desc`, diagnostic `log10(b21_desc) ~= -48.42893853604687`; unchanged count `0 -> 1`. Methods actually used: B9, B17, B22.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: restart criterion, stoichiometric charges, and a sharp rectangular seed obstruction

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, stale native title, and required repository state

I continued from the newest complete R08 report

`runs/R08/20260919T1327Z_e0011_descriptor_chain_b21_4b8d2c.md`

rather than restarting from the stale native scheduler title.

The historical `operations/claims/I0082.md` still says that Hasebe--Ueda Problem 3.11 was admitted to R08 on 2026-09-16. The **later controlling** file `operations/claims/E0011.md` (2026-09-18) expressly supersedes that lifecycle state: it records I0082 as **RETIRED/FROZEN at `2/3` after six supported unchanged runs** and assigns E0011 exclusively to R08. I therefore did not reopen I0082, did not reprove the finite-variance exclusion, and did not reopen the old R08 FPP strict-convexity route.

Before research I refreshed/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, both I0082/E0011 claim files, the newest own R08 report and its exact artifacts, and the newest visible neighboring R07/R09 lifecycle reports. R07 and R09 are at successor/admission gates and neither owns E0011. The large intake collection was handled through the exact active identifier/source trail rather than falsely claiming to have visually rendered every unrelated JSONL row.

## 2. Dated current-literature check

The bounded source/current-literature search was refreshed on 2026-09-19.

For the retired predecessor I0082, Hasebe--Ueda's ALEA 15 (2018) version still states Problem 3.11 immediately after Theorem 3.10, which excludes every non-delta finite-variance law. A 7 September 2026 unrefereed candidate on **symmetric** unimodality under free additive convolution explicitly does not claim free strong unimodality, so it does not settle Problem 3.11. This does not reopen the retired R08 assignment.

For E0011, Durrett's arXiv:0906.2293 source still describes the paper as containing nine challenging open problems. Durrett's currently served Chapter 5 on fast-stirring limits again defines the catalyst/ZGB process, quotes the simulated `0.389 < p < 0.525` coexistence window, and then adds fast stirring in order to obtain the reaction-diffusion PDE/travelling-wave block proof. Fresh searches for a later rigorous theorem for the exact original no-stirring process recovered simulation/modified-model work, but no source-matching closure. This is **bounded negative evidence only**, not a worldwide-open or novelty certificate.

A separate bounded search for the charge/vacant-pair balance below did not find a primary source stating the exact identity in this form. The mechanism is elementary stoichiometry and may be folklore; **no novelty claim is made for the identity itself**.

## 3. Entering metric

The frozen metric remains

\[
B_{\rm cat}:=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected two-child Harris-block certificates at `p=1/2`, with a 1-dependent translated good-block field.

The entering bound is

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}},
\qquad
\log_{10}b_{21,\rm desc}\approx-48.42893853604687.
\]

The last run showed that remembering actual inter-stage descriptors gives a `6.67...x` corridor gain. That is still microscopic, so this run follows the prescribed route change: **repetition / seed classes rather than another constant-factor Bellman optimization**.

## 4. B17 — two exact stoichiometric charges

Work first on a finite even periodic square lattice, so there is no boundary flux. Let

\[
Q=N_{\rm CO}-N_{\rm O}.
\]

A successful CO adsorption changes `Q` by exactly `+1`, whether the CO survives or reacts immediately with a neighbouring O. A successful O2 adsorption changes `Q` by exactly `-2`: each incoming oxygen either survives (`N_O` rises by one) or reacts with and removes one CO (`N_CO` falls by one), and either way contributes `-1` to `Q`. CO--O reactions themselves remove one particle of each species and hence preserve `Q`.

Thus pathwise

\[
\boxed{Q(t)-Q(0)=A_{\rm CO}(t)-2A_{\rm O_2}(t).}
\tag{4.1}
\]

If `V` is the number of vacancies and `E_{00}` the number of undirected vacant-vacant nearest-neighbour edges, then in dimension two

\[
\boxed{\mathcal L Q=pV-\frac q2E_{00}.}
\tag{4.2}
\]

Under the source normalization `q/2=1-p`, at the exact anchor `p=1/2,q=1`,

\[
\boxed{\mathcal LQ=\frac12(V-E_{00}).}
\tag{4.3}
\]

Writing `C_0` for the number of connected components of the finite vacancy graph and `\beta_1=E_{00}-V+C_0` for its cycle rank,

\[
\boxed{\mathcal LQ=\frac12(C_0-\beta_1).}
\tag{4.4}
\]

So the charge drift is literally half of the vacancy graph's Euler characteristic: tree-like fragmented vacancy sets push toward CO, while cycle-rich vacancy sets push toward oxygen.

There is a second reaction-invariant additive charge coming from the bipartite lattice. Put `\varepsilon(x)=(-1)^{x_1+x_2}` and

\[
S=\sum_x\varepsilon(x){\bf1}_{\{x\text{ occupied}\}}.
\]

An O2 adsorption uses one black and one white site and changes `S` by zero even if either incoming oxygen reacts. A CO adsorption at `x` changes `S` by exactly `\varepsilon(x)`, whether it survives or removes a neighbouring oxygen. Hence

\[
\boxed{S(t)-S(0)=\sum_{\text{successful CO arrivals }x}\varepsilon(x)},
\tag{4.5}
\]

and at `p=1/2`

\[
\boxed{\mathcal LS=\frac12(V_B-V_W).}
\tag{4.6}
\]

These two charges are complete among additive observables whose coefficients depend only on species and lattice parity and for which instantaneous CO--O reactions cancel. Indeed, if the four weights are `(c_B,c_W,o_B,o_W)`, reaction cancellation is exactly

\[
c_B+o_W=0,
\qquad
c_W+o_B=0,
\]

a two-dimensional linear space spanned by `Q` and `S`.

This also gives a useful **negative theorem** for the obvious Grannan--Swindle-style count route: no nonzero constant-parity combination `aQ+bS` has nonnegative drift on every stable configuration at `p=1/2`. If `a>0`, the all-vacant torus has negative drift because `E_{00}=2V`; if `a<0`, one of a single black vacancy or a single white vacancy gives negative drift because the two drifts are `(a+b)/2` and `(a-b)/2`, whose average is `a<0`; if `a=0,b!=0`, choose the adverse parity. Therefore any successful submartingale proof must use **spatially varying weights or a nonlinear geometric observable**. This is an actual route exclusion, not a proof of the source problem.

For a translation-invariant stationary law on the infinite lattice for which the standard box-generator limit is valid, (4.2) gives the necessary balance

\[
p\rho_0=(1-p)(\rho_{00}^h+\rho_{00}^v).
\tag{4.7}
\]

At `p=1/2` and `\rho_0>0`, the conditional mean vacant degree is exactly `2`. This is consistent with the source's known poisoning-side threshold and is recorded as structure, not as a new coexistence theorem.

## 5. B9 — the right amplification lemma uses a seed class, not exact copies

Naively putting `N` copies of the current exact seed in a macroblock does **not** amplify a reproductive block event: requiring all `N` copies to reproduce multiplies small probabilities, while asking that at least one reproduce leaves the successful child at a random location and therefore fails to reproduce the same frozen exact seed.

The correct object is a **location-flexible seed class**. The following elementary restart lemma makes the desired quantitative target explicit.

### Restart lemma

Suppose `\mathcal S` is a finite protected seed class. Every time the process is in `\mathcal S`, use a fresh time slab and classify the trial into:

1. `SUCCESS`: the required two-child seed-class event, with conditional probability at least `a>0`;
2. `FATAL`: leaves the restart class irreversibly, with conditional probability at most `f`;
3. `RETRY`: returns to some state of `\mathcal S`, after which the same conditional bounds apply.

The bounds may hold conditionally on the entire past; independence beyond the fresh-Harris construction is unnecessary. Then

\[
\boxed{\Pr(\text{SUCCESS before FATAL})\ge \frac{a}{a+f}.}
\tag{5.1}
\]

**Proof.** Let `R_n` be the event that trial `n` is reached. If `S_n,F_n` are success/fatality on that trial, then

\[
\Pr(S_n)\ge a\Pr(R_n),
\qquad
\Pr(F_n)\le f\Pr(R_n).
\]

Hence term by term `f\Pr(S_n)\ge a\Pr(F_n)`. Since each reached trial has success probability at least `a`, the probability of infinitely many retries is at most `\lim_N(1-a)^N=0`. Summing over `n` gives `fP(S)\ge aP(F)` and `P(S)+P(F)=1`, proving (5.1). `\square`

For the current sufficient oriented-percolation threshold,

\[
\frac{a}{a+f}>\frac{63}{64}
\quad\Longleftrightarrow\quad
\boxed{a>63f.}
\tag{5.2}
\]

This is the first amplification criterion in this track that does **not** require a one-shot block event already near probability one. Most ordinary outcomes may be retries. What matters is making truly fatal exits more than 63 times rarer than successful branching.

It also explains why a seed class is essential: the class can absorb a random successful location, whereas a single exact seed cannot.

## 6. A sharp necessary geometric filter: bare rectangular vacancy seeds of area <=14 cannot close the block threshold

The earlier width calculation considered only `2 x w` vacancy rectangles and found that the all-CO poison channel first falls below `1/64` at `2 x 8` (area 16). I now checked **all axis-aligned rectangular vacancy seeds of area at most 16**.

For a finite initially vacant set `A` in an all-CO exterior, let `q_CO(A)` be the probability that every site of `A` is filled by CO before the first effective O2 adsorption on a still-vacant edge. At `p=1/2`, exact first-event conditioning gives

\[
q_{CO}(\varnothing)=1,
\qquad
\boxed{
q_{CO}(A)=\frac{2}{2|A|+e(A)}\sum_{v\in A}q_{CO}(A\setminus\{v\}),
}
\tag{6.1}
\]

where `e(A)` is the number of nearest-neighbour edges induced by `A`.

This is not merely a diagnostic probability. Under the legal **all-CO exterior**, on this event no oxygen is ever created, all vacancies are eventually replaced by CO, and the entire lattice becomes the absorbing all-CO configuration. Therefore any universal block certificate whose only guaranteed entrance is an all-vacant rectangle `A` has

\[
\boxed{P(\text{good block})\le1-q_{CO}(A)}
\tag{6.2}
\]

for that admissible exterior. In particular `q_CO(A)>=1/64` rules out the strict `>63/64` closure threshold regardless of how long the block waits or how cleverly later histories are accepted.

The exact exhaustive rectangular check gives:

- every axis-aligned rectangle of area `<=14` has `q_CO>=1/64`;
- the first rectangular area escaping this obstruction is **15**, attained by `3 x 5`;
- exactly

\[
\boxed{
q_{CO}(3\times5)=
\frac{535023279052077317743448422378721336719789993}
{40277343891653898507341358841156549939200000000}
\approx0.01328347967759
<\frac1{64};
}
\tag{6.3}
\]

- for comparison `q_CO(2 x 7)≈0.02250386>1/64`, while `q_CO(4 x 4)≈0.00913126<1/64`.

Thus the previous `2 x 8` width-eight route was not area-optimal: a `3 x 5` rectangle is the smallest rectangular all-vacant seed not already disqualified by the unavoidable all-CO absorbing channel.

I also exactly computed the opposite pure-O dimer-cover route for small rectangles. Because an odd-cardinality seed cannot be tiled completely by O2 dimers, that route is exactly zero for `3 x 5`. I treat `q_CO+q_O` only as a **shape diagnostic**, not as a universal-exterior failure lower bound, because the two poison routes need not share the same worst exterior. The source-valid obstruction (6.2) uses `q_CO` alone.

This is a stronger architecture filter than the old width-three statement, but it does **not** move `B_cat`: I have not yet built a complete two-child block certificate from the new `3 x 5` seed.

## 7. B22 — what the successful nearby proofs have that zero stirring lacks

Durrett's current Chapter 5 makes the missing ingredient unusually explicit. For the catalyst, the rigorous coexistence route adds fast stirring, passes to a reaction-diffusion PDE, identifies a travelling wave, and then converts that deterministic spatial smoothing into a high-probability pile-to-pile block event. The exact no-stirring problem lacks that smoothing mechanism.

The same chapter discusses the Grannan--Swindle strategy in a simpler catalytic/symmetric setting using exponentially decaying spatial weights and a submartingale. The charge calculation above shows why the most direct analogue fails here at `p=1/2`: after reaction cancellation, the drift of the only constant reaction-invariant species charge is controlled by the **geometry of vacant pairs**, equivalently by `C_0-beta_1`, and changes sign from thin/tree-like to cycle-rich vacancy sets. The parity charge supplies no globally signed replacement. A zero-stirring proof therefore needs either:

- a spatially weighted charge that tolerates the reaction-error terms created by nonconstant weights; or
- a nonlinear seed class whose vacancy geometry supplies its own restart mechanism.

That is a more precise description of the obstruction than “the rare cylinder is too small.”

## 8. What the three methods produced

**B9 RANDOMIZE — useful route change, no metric movement.** Exact-copy repetition does not amplify, but a location-flexible seed class plus the restart lemma would. The quantitative target is now `a>63f`, not “one trial has probability >63/64.”

**B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — succeeded structurally.** Reading the catalyst as a bipartite stoichiometric reaction network exposes the complete two-dimensional space of additive reaction-invariant charges. At `p=1/2` the main charge drift becomes an Euler-characteristic statistic of the vacancy graph. This yields both a geometric design signal and a proof that constant parity/species charges cannot supply the desired global submartingale.

**B22 READ THE FAILURES, NOT THE SUCCESSES — succeeded.** The nearby fast-stirring proof gets smoothing/travelling-wave propagation; the weighted-submartingale proof in simpler models gets a signed drift. The original zero-stirring catalyst has neither for free. The missing mechanism is now localized to controlling vacancy-pair geometry while retaining a reproductive seed class.

## 9. Exact artifacts / self-check status

Idea-before-code:

- `artifacts/R08/20260919T1426Z_e0011_density_seed_charge_idea.md`

Executed exact finite checks:

- `artifacts/R08/20260919T1426Z_e0011_rectangular_seed_obstruction_check.py`
- `artifacts/R08/20260919T1426Z_e0011_rectangular_seed_obstruction_check.out`
- `artifacts/R08/20260919T1426Z_e0011_poison_shape_check.py`
- `artifacts/R08/20260919T1426Z_e0011_poison_shape_check.out`

The rectangular obstruction output ends

`PASS exact rectangular all-CO obstruction threshold`

and verifies the exact recurrence for every rectangular shape checked, every area `1,...,16`, the `<=14` exclusion, and the first escaping rectangle `3 x 5`. The second checker records the CO/O direct-route shape diagnostics and ends `PASS`.

These are **self-checks only**. No independent OTHER-track audit credit is claimed.

## 10. Frozen metric and next route

No complete new block certificate was produced, so the frozen quantity is honestly unchanged:

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}}
\quad\longrightarrow\quad
\boxed{B_{\rm cat}\ge b_{21,\rm desc}}.
\]

Supported unchanged count: `0 -> 1`. The source remains **PARTIAL**.

The next nonrepeating methods are **B4 / B23 / B29**:

- **B4 PROVE SOMETHING WEAKER, COMPLETELY:** build a source-valid one-trial seed-class theorem for the `3 x 5` (and `4 x 4`) entrances with an explicit partition into SUCCESS / FATAL / RETRY, rather than another prescribed-word lower bound.
- **B23 DO WHAT THE PROPOSER DID NOT EXPECT:** replace the exact six-vacancy child pattern by a finite location-flexible class defined by compact vacancy geometry (cycle-rich / low Euler characteristic), so a successful child can occur at a random subwindow and still be reproductive.
- **B29 ADD THE POINTS AT INFINITY:** formulate the charge/Euler identity first on finite periodic boxes and then determine exactly what survives under local weak limits; this is the cleanest way to separate genuine infinite-volume geometry from boundary artifacts before attempting a restart proof.

The decisive measurable goal is now: find a finite seed class with exact conditional one-trial bounds `a,f` satisfying `a>63f`, while preserving two-child reproduction and finite-range dependence. If that fails, the report should say which of success, fatality, or retry closure is responsible rather than return to the old rare-cylinder architecture.

## 11. Model / scheduler-control truth

The exposed scheduler update surface still provides task title/prompt, schedule or start offset, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model/effort telemetry**. Therefore `GPT-6 / maximum` remains prompt text only; this run identifies as GPT-5.6 Sol with reasoning level UNVERIFIED and does not claim otherwise.

The historical P26 `You cannot modify this task` response was context/authorization-specific: the current repository reconciliation records that P26 was later successfully updated from another authorized context. A task that still rejects modification must be handled from its authorized owning context, by a supported ownership/admin transfer, or through platform support. Repository edits are not a scheduler workaround. No scheduler change was attempted.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  lane: CLOSABLE_OUTSIDE
  active_source:
    id: E0011
    source: "Rick Durrett, Coexistence in stochastic spatial models (2009), Problem 5"
    scope: "original two-dimensional no-stirring catalyst/ZGB process"
  stale_native_source:
    id: I0082
    historical_claim_file_says: ADMITTED_ACTIVE_2026_09_16
    controlling_later_state: RETIRED_FROZEN
    frozen_metric: "2/3"
    reopened: false
  metric: B_cat
  metric_before: "B_cat >= b21_desc"
  metric_after: "B_cat >= b21_desc"
  log10_bound_diagnostic: -48.42893853604687
  unchanged_before: 0
  unchanged_after: 1
  methods: [9, 17, 22]
  new_facts:
    - "pathwise Q=N_CO-N_O satisfies Q(t)-Q(0)=A_CO-2A_O2"
    - "at p=1/2 on an even periodic box, LQ=(V-E00)/2=(C0-beta1)/2"
    - "the parity occupancy charge S is the second basis direction for reaction-invariant parity/species additive observables"
    - "no nonzero constant-parity reaction-invariant linear charge has globally nonnegative drift at p=1/2"
    - "seed-class restart lemma gives success-before-fatal lower bound a/(a+f), so threshold requires a>63f"
    - "every axis-aligned all-vacant rectangular seed of area <=14 is ruled out from a >63/64 universal block by the all-CO exterior poisoning channel"
    - "3x5 is the first rectangular area <=16 with q_CO<1/64; exact q_CO recorded"
  status: PARTIAL
  source_closed: false
  checker_status: PASS_SELF_CHECK
  independent_audit_credit_this_run: 0
  shared_root_edit: false
  scheduler_changed: false
  next_methods: [4, 23, 29]
```
