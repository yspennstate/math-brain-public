Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat >= b21_desc -> B_cat >= b21_desc`, diagnostic `log10(b21_desc) ~= -48.42893853604687`; unchanged count `1 -> 2`. Methods actually used: B4, B23, B29.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: arbitrary-shape poison obstruction, the thin-strip restart candidate, and a stationary vacancy-degree identity

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, stale native title, and required repository state

I continued from the newest complete R08 report

`runs/R08/20260919T1509Z_e0011_charge_restart_rect15_c41b7e.md`

rather than restarting from the stale native scheduler title.

The historical `operations/claims/I0082.md` still contains its 2026-09-16 admission text for Hasebe--Ueda Problem 3.11. The **later controlling** file `operations/claims/E0011.md` (2026-09-18) explicitly records I0082 as **RETIRED/FROZEN at `2/3` after six supported unchanged runs** and assigns E0011 exclusively to R08. I therefore did not reopen I0082, did not reprove its finite-variance exclusion, and did not reopen the old R08 FPP strict-convexity route.

Before research I refreshed/recovered campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the I0082/E0011 claim files, the newest complete own report and its artifacts, and the newest visible neighboring R07/R09 lifecycle reports. R07 and R09 are at unrelated successor/admission gates and neither owns E0011. The large intake JSONL files are connector-truncated when rendered wholesale; I used exact-ID/source searches and the canonical claim trail rather than falsely claiming a visual read of every unrelated row.

## 2. Dated current-literature check

The bounded source/current-literature check was refreshed on 2026-09-19.

Durrett's 2009 source still describes the paper as containing nine challenging open problems. Durrett's currently served particle-systems Chapter 5 still defines the original catalyst/ZGB process, quotes the simulated coexistence window near `0.389 < p < 0.525`, and then adds **fast stirring** to obtain the reaction-diffusion/travelling-wave route. Recent ZGB work recovered in the bounded search concerns modified models such as CO desorption or reactive sulfur; I found no later primary theorem settling the exact original two-dimensional no-stirring source target. This is **bounded negative evidence only**, not a worldwide-open or novelty certificate.

I also searched for the exact charge/vacancy-pair identities below and did not find a primary source stating them in this form. The underlying stoichiometry and edge-isoperimetric mechanisms are elementary and may be folklore. **No novelty claim is made for those mechanisms.**

## 3. Entering metric

The frozen quantity remains

\[
B_{\rm cat}:=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected two-child Harris-block certificates at `p=1/2`, with finite-range dependence and a written deterministic seed-reproduction implication.

The entering certified bound is

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}},
\qquad
\log_{10} b_{21,\rm desc}\approx -48.42893853604687.
\]

The previous run changed route from rare prescribed cylinders to seed classes and restart amplification. This run follows its prescribed nonrepeating methods B4/B23/B29.

## 4. B4 — remove the rectangle restriction from the all-CO poisoning obstruction

The preceding run proved an exact obstruction only for **rectangular** bare vacancy seeds. The rectangle hypothesis is unnecessary.

Let `A` be any finite set of initially vacant sites in an otherwise all-CO configuration at `p=1/2`. Let `q(A)` be the probability that every site of `A` is filled by CO before the first effective O2 adsorption on a still-vacant nearest-neighbour edge. First-event conditioning gives

\[
q(\varnothing)=1,
\qquad
\boxed{
q(A)=\frac{2}{2|A|+e(A)}\sum_{v\in A} q(A\setminus\{v\}),
}
\tag{4.1}
\]

where `e(A)` is the number of nearest-neighbour edges induced by `A`. On this event no oxygen is ever created, and the process reaches the absorbing all-CO configuration. Thus any universal good-block construction whose only guaranteed entrance is the bare vacancy set `A` has

\[
P(\text{good block})\le 1-q(A)
\tag{4.2}
\]

against this admissible exterior.

### 4.1 A square-lattice edge bound

If `|A|=n` and `A` meets `r` rows and `c` columns, then the number of horizontal induced edges is at most `n-r` and the number of vertical induced edges is at most `n-c`. Since `n\le rc`,

\[
r+c\ge \lceil 2\sqrt n\rceil.
\]

Hence

\[
\boxed{e(A)\le m(n):=2n-\lceil2\sqrt n\rceil.}
\tag{4.3}
\]

This is enough for a geometry-free recursive lower envelope.

### 4.2 Exact recursive lower envelope

For `0\le e\le m(n)` define `L(n,e)` recursively. Put `L(0,0)=1`. If the induced degree sequence of `A` is `d_1,...,d_n`, then

\[
0\le d_i\le4,
\qquad
\sum_i d_i=2e,
\qquad
e(A\setminus\{v_i\})=e-d_i.
\]

Therefore define

\[
\boxed{
L(n,e)=\frac{2}{2n+e}
\min_{\substack{0\le d_i\le4\\
\sum_i d_i=2e\\
0\le e-d_i\le m(n-1)}}
\sum_{i=1}^n L(n-1,e-d_i).
}
\tag{4.4}
\]

The minimization deliberately allows integer degree sequences that need not be graph-realizable. That enlarges the adversarial set and can only make `L` smaller, so it is safe.

**Induction.** Suppose `q(B)\ge L(k,e(B))` for every `|B|=k<n`. Applying (4.1) to `A`, substituting the induction hypothesis for every deletion, and then minimizing over the larger necessary-constraint class in (4.4) gives

\[
q(A)\ge L(n,e(A)).
\tag{4.5}
\]

The exact checker also verifies, for every `n\le15`, that `L(n,e)` is nonincreasing in `e`. Consequently

\[
q(A)\ge L(n,m(n)).
\]

For `n=14`, `m(14)=20` and the exact value is

\[
\boxed{
L(14,20)=
\frac{10200893358654003482591}
{575716442031828197100000}
\approx0.01771860696326969
>
\frac1{64}.
}
\tag{4.6}
\]

Indeed

\[
L(14,20)-\frac1{64}
=
\frac{2410647903813375805807}
{1151432884063656394200000}>0.
\tag{4.7}
\]

Every smaller bare vacancy set is also covered: if `|A|<14`, augment it by sufficiently distant isolated vacant sites to a 14-site set `A'`. The event that **all** sites of `A'` fill with CO before any internal O2 adsorption implies the corresponding event for `A`, so `q(A)\ge q(A')>1/64`.

Therefore:

### Arbitrary-shape seed obstruction

\[
\boxed{
|A|\le14
\quad\Longrightarrow\quad
q(A)>\frac1{64}.
}
\tag{4.8}
\]

Hence **no bare all-vacant seed of at most 14 sites, of any geometry, can support a universal good-block probability strictly greater than `63/64`** against arbitrary exterior states.

This strengthens the preceding rectangle-only theorem. It is also sharp **for this particular direct-poison obstruction**: the explicit `3 x 5` set has 15 sites and

\[
q(3\times5)\approx0.01328347967759<\frac1{64}.
\]

That does **not** mean a 15-site seed yields coexistence; it only means this single unavoidable all-CO channel no longer rules it out.

For reference, the conservative envelope at `n=15` is already below the budget:

\[
L(15,m(15))=
\frac{18662677377032686970336681}
{1552693103756001269342280000}
\approx0.012019553208478372<\frac1{64}.
\tag{4.9}
\]

## 5. B23 — the compact 3x5 seed loses a different test; 2x8 is the first thin restart rectangle passing both

The previous run identified `3 x 5` as the smallest **rectangular area** escaping direct all-CO poison. B23 asks the opposite question: perhaps compactness is dynamically bad.

Start from a fully vacant `h x w` rectangle in an all-CO exterior at `p=1/2`, and evaluate the generator of the vacancy count `V` at time zero.

A CO adsorption at any vacant site changes `V` by `-1`, giving total CO contribution `-hw/2`.

For an O2 adsorption on an internal vacant edge, inspect one endpoint:

- if the endpoint is on the rectangle boundary, it has an outside CO neighbour; the incoming O reacts immediately and leaves the adsorption site vacant again while removing that CO, so its net contribution to `V` is `+1`;
- if the endpoint is strictly interior, it initially has no CO neighbour and the incoming O survives, so its contribution is `-1`.

For `h,w\ge3`, summing these signs over the endpoints of all internal edges gives

\[
\boxed{
\mathcal L V
=-\frac32hw+\frac72(h+w)-8.
}
\tag{5.1}
\]

For a `2 x w` strip, every site is a boundary site, so

\[
\boxed{
\mathcal L V=\frac w2-1.
}
\tag{5.2}
\]

For a `1 x w` strip the drift is `-1/2`.

The formula (5.1) is already `-1/2` at `3 x 3` and decreases as either dimension grows. Therefore among rectangles with both side lengths at least two, **positive initial vacancy drift occurs exactly for `2 x w` strips (or rotations) with `w\ge3`**.

The exact relevant values are

\[
\mathcal LV(3\times5)=-\frac52,
\qquad
\mathcal LV(4\times4)=-4,
\qquad
\mathcal LV(2\times7)=\frac52,
\qquad
\mathcal LV(2\times8)=3.
\tag{5.3}
\]

Combine this with the exact direct-poison probabilities:

\[
q(2\times7)\approx0.02250386288623>\frac1{64},
\]

\[
q(2\times8)\approx0.01245080073227<\frac1{64},
\]

\[
q(3\times5)\approx0.01328347967759<\frac1{64},
\qquad
q(4\times4)\approx0.00913126490994<\frac1{64}.
\]

The exact checker exhausts every axis-aligned rectangle of area at most 16 with both sides at least two and finds

\[
\boxed{
2\times8
\text{ is the unique such rectangle with both }
q<1/64
\text{ and }
\mathcal LV>0.
}
\tag{5.4}
\]

So the direct-poison filter and the local growth-drift filter point in different directions: `3 x 5` is cardinality-efficient, but `2 x 8` is the first rectangle that also has a positive vacancy drift. This makes the thin `2 x 8` strip a more plausible **restart seed-class candidate** than the compact `3 x 5` rectangle.

This is still an architecture result, not a reproductive block certificate. No metric movement is claimed.

## 6. B29 — pass the charge identity to infinite volume by boundary flux, not by pretending an infinite total charge exists

The idea-before-code note initially phrased this through finite tori. The cleaner argument is a Følner-box/boundary-flux proof, which avoids relying on any nontrivial finite-volume stationary law.

Let `\mu` be a translation-invariant stationary law for the infinite source process. For a finite square `\Lambda`, define the **local** charge

\[
Q_\Lambda
=
\sum_{x\in\Lambda}
\left({\bf1}_{\{x=CO\}}-{\bf1}_{\{x=O\}}\right).
\]

For adsorption/reaction events whose entire interaction neighbourhood lies in the interior of `\Lambda`, the same stoichiometric cancellation as in the previous run is exact:

- each successful CO adsorption contributes `+1` to charge;
- each successful O2 adsorption contributes `-2` to charge.

Thus the bulk generator contribution is

\[
p\,V_\Lambda-\frac q2 E_{00,\Lambda},
\]

up to events whose sites or reactions meet a constant-width boundary layer. Rates and charge increments are uniformly bounded, so the expectation of the omitted boundary contribution is `O(|\partial\Lambda|)`.

Stationarity gives `E_\mu[\mathcal L Q_\Lambda]=0`. Divide by `|\Lambda|` and let `\Lambda\uparrow\mathbb Z^2`. The boundary/volume ratio vanishes, yielding

\[
\boxed{
p\rho_0=\frac q2(\rho_{00}^h+\rho_{00}^v).
}
\tag{6.1}
\]

Under the source normalization `q/2=1-p`,

\[
\boxed{
p\rho_0=(1-p)(\rho_{00}^h+\rho_{00}^v).
}
\tag{6.2}
\]

If `\rho_0>0`, the conditional number of vacant nearest neighbours of the origin satisfies

\[
\boxed{
\mathbb E_\mu[\deg_0^{\rm vac}\mid 0\text{ vacant}]
=
\frac{2(\rho_{00}^h+\rho_{00}^v)}{\rho_0}
=
\frac{2p}{1-p}.
}
\tag{6.3}
\]

Since `\deg_0^{\rm vac}\le4`, every translation-invariant stationary law with positive vacancy density must satisfy the structural restriction

\[
\boxed{p\le\frac23.}
\tag{6.4}
\]

At the track's anchor `p=1/2`, the conditional vacant degree is exactly

\[
\boxed{\mathbb E[\deg_0^{\rm vac}\mid 0\text{ vacant}]=2.}
\tag{6.5}
\]

This is source-relevant because any putative non-poisoned stationary coexistence state with vacancies must live on that balance surface. It is not a proof of coexistence, and no novelty is asserted.

## 7. What the three methods produced

**B4 PROVE SOMETHING WEAKER, COMPLETELY — succeeded as an architecture theorem.** The direct all-CO obstruction now applies to **every** bare vacancy seed of cardinality at most 14, not only rectangles. The proof is a recursive exact lower envelope plus a square-lattice edge bound.

**B23 DO WHAT THE PROPOSER DID NOT EXPECT — useful route reversal.** The smallest poison-escaping rectangle (`3 x 5`) has negative initial vacancy drift. Among rectangles of area at most 16, the thin `2 x 8` strip is uniquely able to pass both the direct-poison test and the positive-initial-drift test. This changes the candidate seed geometry for a restart proof.

**B29 ADD THE POINTS AT INFINITY — succeeded structurally after correction.** A local-box boundary-flux argument transfers the finite stoichiometric charge balance to any translation-invariant stationary infinite-volume law, giving conditional vacant degree `2p/(1-p)` and the necessary restriction `p<=2/3` when vacancy density is positive.

## 8. Exact artifacts / self-check status

Idea written before checker code:

- `artifacts/R08/20260919T1530Z_e0011_strip_seed_stationarity_idea.md`

Executed exact finite checker and archived output:

- `artifacts/R08/20260919T1530Z_e0011_seed_cardinality_strip_check.py`
- `artifacts/R08/20260919T1530Z_e0011_seed_cardinality_strip_check.out`

The output ends

`PASS cardinality obstruction and thin-strip classification`.

It exactly verifies the recursive envelope through `n=15`, its monotonicity in edge count, the strict `L(14,m(14))>1/64` inequality, the explicit `3 x 5`, `2 x 7`, `2 x 8`, and `4 x 4` poisoning probabilities, the vacancy-drift values, and the uniqueness of `2 x 8` among rectangles of area at most 16 satisfying both filters.

These are **self-checks only**. No independent OTHER-track audit credit is claimed.

## 9. Frozen metric and next route

No complete new two-child 1-dependent block certificate was produced. Therefore the frozen quantity is honestly unchanged:

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}}
\quad\longrightarrow\quad
\boxed{B_{\rm cat}\ge b_{21,\rm desc}}.
\]

Supported unchanged count: `1 -> 2`. The source remains **PARTIAL**.

This is not yet a formal stuck run; one more supported unchanged run would make the count three and trigger the full section-I stuck protocol.

The next nonrepeating methods are **B3 / B15 / B19**:

- **B3 PROVE SOMETHING STRONGER:** do not merely get one successful strip event; construct a finite **location-flexible `2 x 8` strip seed class** whose SUCCESS output lies in the same class, so restart amplification can actually iterate.
- **B15 BREAK THE SYMMETRY ON PURPOSE:** orient the strip and its protected halo toward the two desired forward children instead of insisting on a symmetric compact seed. The positive vacancy drift is a boundary phenomenon and should be exploited rather than averaged away.
- **B19 MAKE IT AN ALGORITHM:** build the exact finite SUCCESS / FATAL / RETRY automaton for the oriented strip plus a minimal halo, and compute rigorous conditional lower/upper bounds `a,f`. The decisive target is still `a>63f`; if that inequality cannot be achieved, identify exactly which absorbing/fatal class prevents it.

## 10. Model / scheduler-control truth

The exposed scheduler update surface still provides task title/prompt, schedule or start offset, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model/effort telemetry**. Therefore `GPT-6 / maximum` remains prompt text only; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED and does not claim otherwise.

The historical P26 `You cannot modify this task` result was context/authorization-specific: the repository reconciliation records that P26 was later successfully updated from another authorized context. A task that still rejects modification must be handled from its authorized owning context, by a supported ownership/admin transfer, or through platform support. Repository edits are not a scheduler workaround. No scheduler change was attempted.

## 11. Structured ledger delta

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
    controlling_later_state: RETIRED_FROZEN
    frozen_metric: "2/3"
    reopened: false
  metric: B_cat
  metric_before: "B_cat >= b21_desc"
  metric_after: "B_cat >= b21_desc"
  log10_bound_diagnostic: -48.42893853604687
  unchanged_before: 1
  unchanged_after: 2
  methods: [4, 23, 29]
  new_facts:
    - "Every bare vacancy seed A subset Z^2 with |A|<=14 has an all-CO direct-poison probability q(A)>1/64 under a legal all-CO exterior."
    - "The exact recursive lower envelope gives L(14,20)=10200893358654003482591/575716442031828197100000>1/64."
    - "Among axis-aligned rectangles of area <=16 with both sides >=2, 2x8 is uniquely both below the 1/64 direct-poison threshold and of positive initial vacancy drift."
    - "For any translation-invariant stationary law with positive vacancy density, E[deg_vac(0)|0 vacant]=2p/(1-p), hence p<=2/3; at p=1/2 the conditional degree is exactly 2."
  exact_artifacts:
    - artifacts/R08/20260919T1530Z_e0011_seed_cardinality_strip_check.py
    - artifacts/R08/20260919T1530Z_e0011_seed_cardinality_strip_check.out
  self_check_only: true
  source_status: PARTIAL
  next_methods: [3, 15, 19]
  next_unchanged_triggers_stuck_protocol: true
```
