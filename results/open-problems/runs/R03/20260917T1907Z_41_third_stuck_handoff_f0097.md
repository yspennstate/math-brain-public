Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family or reasoning-effort telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the frozen F0001 full-range metric: `r(10)=222.6104736743168493957921796888577...` remains exact and `r(11)<=523.4894710902614257202829985613411...`; unchanged count `5 -> 6`. This is the THIRD stuck episode after two permitted recoveries, so F0001 is HANDED OFF and R03 ROTATES to HARD OUTSIDE successor F0097. Final recovery methods: #5 ADD A PARAMETER, #25 COUNT THE SAME THING TWICE, #18 SAY IT IN ANOTHER LANGUAGE.**

# R03 run41 — terminal F0001 stuck handoff; final rich-core test fails; rotate to F0097 random k-SAT

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status of old target: **F0001 OPEN / R03 PARTIAL / HANDOFF REQUIRED AND EXECUTED.**  
Successor: **F0097 HARD OUTSIDE / OPEN_CURRENT / claimed by R03 for the next research run.**

No finite checker is manufactured in this run: the final recovery produced no new finite claim and no improved numerical remainder. The substantive work is the source-scale failure analysis and lawful rotation mandated by the owner's stuck policy.

## 1. Continuity, source match, and controls

Before the final recovery I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `QUEUE.md`, and the current new-methods policy `operations/NEW_METHODS_2026-09-16.md`;
- newest complete R03 report `runs/R03/20260917T1805Z_40_stuck_thinking_02.md` and its retained run38/run39 handoff chain;
- newest neighboring R02 successor-admission report `runs/R02/20260917T1718Z_2f6a9c1d.md`;
- targeted intake/attempt/ownership searches for F0001 and the prospective HARD successor F0097.

The connector does not expose all roughly 780 intake rows as a single reliable byte-for-byte read. I therefore used the exact target records, queue state, prior attempts and ownership paths relevant to this handoff, and do not claim a literal visual reread of every JSONL row.

The old outside source remains F0001: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 2.2. For iid uniform Rademacher `B_n`, the retained source-normalized statement is

\[
\Pr(\det B_n=0)=(1+o(1))\,n(n-1)2^{1-n}.
\tag{1.1}
\]

Let `T_n` be the exact union of equal/opposite signed row-pair and column-pair events. The frozen R03 metric is

\[
\boxed{r(n)=2^n\Pr(\det B_n=0,T_n^c),}
\tag{1.2}
\]

and the retained collision-overlap argument makes source closure equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

The current full-range finite envelope remains

\[
r(10)=222.6104736743168493957921796888577\ldots
\]

exactly and

\[
\boxed{
r(11)\le
\frac{32615069759481592686393385491735}
     {62303201039659529147657486336}
=523.4894710902614257202829985613411\ldots .
}
\tag{1.4}
\]

All retained `n>=12` branches remain unchanged.

### Current primary literature, rechecked 2026-09-17

Jain--Sah--Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 2021, still proves the sharp elementary-mechanism asymptotic for finite-support laws **not uniform on their support**. For a law uniform on its support it gives exponential-scale precision and the sharp compressible/low-entropy analysis, not the missing polynomial prefactor. Source: https://arxiv.org/abs/2010.06554.

Song--Wang, arXiv:2607.00495 (1 July 2026), determines growing-corank probabilities for `k=O(sqrt(log n))`; Hunter--Kwan--Sauermann--Sawhney, *On random matrices with large corank*, IMRN 2026 rnag126 (18 June 2026), proves `P(corank >= k)<=exp(-c n k)`. Neither gives the sharp exact-corank-one prefactor. A bounded fresh search did not find an accepted repair of the disputed Irmatov sharp claim or another accepted F0001 resolution. This is dated negative search evidence, not a novelty certificate.

`POSTED.md` does not close or exclude F0001.

## 2. Third-stuck trigger is binding

The preserved unchanged sequence is:

- run36: `0 -> 1`;
- run37: `1 -> 2`;
- run38: `2 -> 3`, mandatory stuck recovery 1;
- run39: `3 -> 4`, action selected by recovery 1;
- run40: `4 -> 5`, mandatory stuck recovery 2;
- **run41: `5 -> 6`, final action fails to move the fixed metric and leaves the same source-scale blocker.**

The HARD-target policy permits at most two stuck recoveries. Therefore this is the **third stuck episode** in the policy sense: R03 must hand off F0001 now. A third thinking recovery or another local F0001 lemma would violate the owner instruction.

## 3. Final recovery target: rich Schur cores

Put `d=n-1`, `m=d-1`. Retained C295/C296 reduce source closure to the binary count

\[
\boxed{N_d^\circ=o\!\left(d^2 2^{d^2-d-1}\right),}
\tag{BLOCK}
\]

where `N_d^circ` counts singular binary `d x d` matrices with no zero row/column and with `J-2B` invertible. Outside a source-normalized negligible sector, the surviving matrices have real corank one and both left/right null vectors have almost full support and almost all absolute coordinate magnitudes distinct.

Fix a distinguished invertible binary `m x m` minor `C` and write

\[
B=\begin{pmatrix}C&a\\ b^T&c\end{pmatrix}.
\]

Then

\[
\det B=0 \iff c=b^TC^{-1}a.
\tag{3.1}
\]

Let `I_circ(C)` count pairs `(a,b) in {0,1}^m x {0,1}^m` for which the scalar in (3.1) lies in `{0,1}` and all retained collision/pivot/two-sided null-profile filters hold, and let

\[
\rho_\circ(C)=2^{-2m}I_\circ(C).
\tag{3.2}
\]

The source-scale aggregate asks for average incidence density essentially

\[
\boxed{\mathbb E_C\rho_\circ(C)=o(d^2 2^{-d})}
\tag{3.3}
\]

(up to the already-retained invertibility/cofactor normalization). Run40 selected a final attempt to trade unusually large `rho_circ(C)` for scarcity of cores.

## 4. Method #5 — add the richness parameter: exact layer-cake formulation, but no tail theorem

Define

\[
H(t)=\#\{C\in\{0,1\}^{m\times m}: C\text{ invertible},\ \rho_\circ(C)\ge t\}.
\tag{4.1}
\]

Since `0<=rho_circ<=1`, the exact layer-cake identity is

\[
\sum_C\rho_\circ(C)=\int_0^1 H(t)\,dt.
\tag{4.2}
\]

Equivalently a dyadic decomposition bounds it by a constant multiple of

\[
\sum_{j\ge0}2^{-j}H(2^{-j}).
\tag{4.3}
\]

This makes the required theorem completely explicit: one needs a scarcity estimate for rich binary inverse cores that remains nontrivial all the way down to

\[
t\asymp \operatorname{poly}(d)2^{-d}.
\tag{4.4}
\]

Checked bilinear/inverse Littlewood--Offord machinery becomes structural at polynomial concentration scales; it does not presently supply a core count at the exponentially smaller threshold (4.4). Introducing `t` therefore diagnoses the missing scale but does not move (BLOCK).

**Outcome #5: failed at the exact endpoint; no metric movement.**

## 5. Method #25 — count the same object twice: the double count collapses to retained cofactor bookkeeping

Summing the incidence count over cores gives

\[
\sum_C I_\circ(C),
\tag{5.1}
\]

which is exactly the number of collision/pivot-filtered singular bordered binary matrices together with a **distinguished invertible `(d-1)x(d-1)` minor** in the chosen position. Removing the distinguished-minor mark weights an exact-corank-one matrix by the number of its nonzero cofactors. If `u,v` are left/right null vectors, `adj(B)=\gamma vu^T`, so this multiplicity is the product of the support sizes of `u` and `v`; on the retained dense sector it is `(1-o(1))d^2`.

But this is precisely the mechanism already used in the retained cofactor comparison C280/C295/C296. The new double count does **not** create an additional entropy factor: it returns the same source-equivalent weighted count from the opposite direction.

**Outcome #25: exact but tautological relative to retained C280/C296; no metric movement.**

## 6. Method #18 — incidence graph and high moments: a concrete rank obstruction

For each invertible core `C`, form the bipartite graph `G_C` with left and right vertex classes `{0,1}^m`; connect `a` to `b` when

\[
b^TC^{-1}a\in\{0,1\}
\tag{6.1}
\]

and the retained source filters hold. Then `rho_circ(C)` is the filtered edge density. Source closure requires a theorem saying that the **average edge density over binary inverse cores** is exponentially sparse, while cores with larger edge density are correspondingly rare.

I tested the most direct moment route. Ignore filters only to obtain an upper-bound obstruction. Fix `a` and one target value `t`. If `q` cube points `b^{(1)},...,b^{(q)}` all satisfy

\[
(b^{(j)})^TC^{-1}a=t,
\]

then for `j>=2`

\[
(b^{(j)}-b^{(1)})^TC^{-1}a=0.
\tag{6.2}
\]

If the difference vectors span rank `r`, multiplication by `C^{-T}` preserves that rank, so the admissible `a` lie in a codimension-`r` real linear subspace. Projection onto free coordinates gives the general cube bound

\[
\#\bigl(\{0,1\}^m\cap L\bigr)\le2^{m-r}.
\tag{6.3}
\]

However `r<=q-1`. Consequently a `q`-th-moment argument based only on this rank information yields at most a factor

\[
2^{-r/q}\ge 2^{-(q-1)/q},
\tag{6.4}
\]

which is only constant-scale after taking the `q`-th root. Taking `q` of order `m` does not help: even maximal `r=m` gives `2^{-m/q}=Theta(1)`. Thus generic high-moment/rank information cannot generate the missing `2^{-m}`-scale incidence density.

This is a concrete obstruction, not another renamed coupling lemma: the moment method loses the desired exponential factor exactly when the root is taken.

**Outcome #18: failed; the same rich-core counting theorem remains missing.**

## 7. Terminal F0001 handoff

### (a) Exact blocking statement

\[
\boxed{N_d^\circ=o\!\left(d^2 2^{d^2-d-1}\right).}
\]

### (b) Routes tried and why they stop

Run40 contains the consolidated A--L failure map: bounded circuits, fixed-prime incidence/CRT, false left-right independence, nonuniform JSS deformation, one-sided inverse LO/cube sections, threshold/Schlaefli deficits, binary-pivot equivalence, higher-corank theorems, exponential-rate estimates, counting inverse LO as a black box, full/distinct row-column fibers, and bilinear Schur cores. This run adds the terminal failures above: dyadic richness exposes but does not bridge the exponential scale; the natural double count is already the cofactor identity; and generic moment-rank estimates lose the exponential gain under the moment root.

### (c) What a proof still needs

A future F0001 owner needs a **matrix-level counting theorem** of the following form: rich two-sided bilinear incidence forces a structural certificate whose number of realizable binary inverse cores is exponentially smaller, with a quantitative tail valid down to edge density `poly(d)2^{-d}`. Pointwise anticoncentration at polynomial scale is not enough.

### (d) Simplest special case still unproved

Count exact-corank-one binary matrices for which both left and right null vectors have full support and pairwise-distinct absolute coordinate magnitudes. Run39 gives only

\[
|S_d|=O(2^{d^2}d^{-3/2}),
\]

while source-scale closure even for this class requires

\[
|S_d|=o(d^2 2^{d^2-d-1}).
\]

The gap is still exponential, about `2^d/d^(7/2)`.

### (e) Nearest solved problem and what it has that F0001 lacks

Jain--Sah--Sawhney's sharp theorem for **non-uniform** finite-support entry laws is the nearest source-level analogue. Its bulk analysis has a strict law-dependent entropy/norm gap; that gap becomes equality for the uniform Rademacher law. Higher-corank work supplies strong suppression away from corank one, but F0001's entire difficulty is the dense exact-corank-one uniform endpoint.

**Handoff verdict:** F0001 is **OPEN**, R03's work is **PARTIAL**, and the target is handed off after exhausting the allowed recovery budget. The frozen metric and all certificates are preserved; nothing is relabeled as solved or retired mathematically. R03 must not return to F0001 unless explicitly reassigned with a fresh route.

## 8. HARD OUTSIDE rotation: F0097 random k-SAT

The current queue has no newly certified generic READY rows, so I screened a source already identified by R02 as current-open, HARD, and unsuitable only for R02's CLOSABLE lane.

Successor: **F0097 — random `k`-SAT satisfiability threshold for every fixed `k`.**

Outside source: Alan Frieze, *Random Structures and Algorithms*, ICM 2014 lecture/slides. The source's random-`k`-SAT section says: finding `c_k` for fixed `k=O(1)` is a major open problem, and its open-problems section asks for the precise satisfiability threshold for random `k`-SAT. Primary PDF: https://www.math.cmu.edu/~af1p/ICM.pdf, especially the random-`k`-SAT slides around PDF page 349 / internal page 348.

Fresh current-status check: Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, Combinatorics, Probability and Computing 35 (2026), published online 27 March 2026, states that the satisfiability threshold is known precisely for `k=2` and for `k>=k_0` with `k_0` an undetermined large constant; for `3<=k<k_0`, even existence of a uniform satisfiability threshold remains open. Thus the small-fixed-`k` source content is still current-open in this bounded 2026-09-17 check.

Prior work is not reset: intake attempt `F0097-A001` already records the Ding--Sly--Sun sufficiently-large-`k` theorem and that their argument uses largeness of `k` essentially throughout. R02's newest screen likewise classified F0097 as `OPEN_CURRENT / HARD / NOT CLAIMED`.

Ownership search found no existing canonical `operations/claims/F0097.md`; fetching that path returned 404 before the write. I therefore created the required create-only ownership claim for R03 at commit `2db7c06e830b25b376e7d29d5933ee28d7e795dc`. `POSTED.md` does not exclude F0097.

No F0097 theorem is attempted in this handoff run. The next R03 run must define its own fixed source-valid metric before research. Because this is a new problem, it must begin with a counterexample/refutation search and preserve F0097-A001 rather than re-deriving it. Planned next Section-B triple: **#2 ATTACK THE NEGATION FIRST, #6 DEFORM TO A SOLVED POINT, #27 SWAP THE QUANTIFIERS.**

## 9. Model / scheduler escalation

The requested runtime setting is still not enforceable from the exposed scheduler surface. The available controls expose task title/prompt, schedule/timing, enablement and notifications, but no model-family or reasoning-effort field and no authenticated per-run applied-model telemetry. Therefore `GPT-6 / maximum` remains prompt text only here.

Historical `You cannot modify this task` responses such as P26 are authorization/workspace-context boundaries. The lawful workaround is an owning/admin-authorized product context; enforcing GPT-6/maximum additionally requires that product/backend surface to expose explicit model and reasoning controls, or a platform-side change/support intervention. No scheduler or permission change was made in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R03
  lane: HARD_OUTSIDE
  old_target:
    source: "F0001 / Vu Conjecture 2.2 / iid uniform Rademacher singularity"
    source_status: OPEN
    run_status: PARTIAL_HANDOFF
    metric: "r(n)=2^n P(det B_n=0, T_n^c)"
    before_n11_upper: "523.4894710902614257202829985613411..."
    after_n11_upper: "523.4894710902614257202829985613411..."
    movement: NO_MOVEMENT
    unchanged_count_before: 5
    unchanged_count_after: 6
    stuck_recoveries_used: 2
    terminal_stuck_episode: 3
    handoff: true
  methods: [5, 25, 18]
  final_recovery:
    richness_parameter: "layer-cake tail needed down to poly(d) 2^-d; unavailable"
    double_count: "collapses to retained cofactor-weighted singular-matrix count"
    moment_rank: "q-fold rank bound loses exponential gain after q-th root"
  new_F0001_theorem_claims: 0
  new_finite_claims: 0
  checker: none
  successor:
    id: F0097
    source: "Alan Frieze ICM 2014 / random k-SAT"
    lane: HARD_OUTSIDE
    status: OPEN_CURRENT
    prior_attempt_preserved: F0097-A001
    claim_commit: 2db7c06e830b25b376e7d29d5933ee28d7e795dc
    research_started: false
    next_methods: [2, 6, 27]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  workflow_execution: false
  scheduler_modified: false
```

## 11. Delivery discipline

This immutable report is the only R03 run report for the invocation. Apart from the create-only successor ownership claim required for lawful rotation, no shared root, peer-track file, email, Drive item, public post, purchase, permission, workflow or scheduler state is modified.
