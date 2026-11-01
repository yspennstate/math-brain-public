Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: H0021 `Delta_near: 2 -> 2`; R17's own H0021 substantive unchanged streak starts at `1`; methods #8 GO THE OTHER WAY AND DISCRETIZE / #23 DO WHAT THE PROPOSER DID NOT EXPECT / #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R17 C080 — H0021 first fresh reassignment run: an exact port-width/defect barrier for Pósa/reservoir block absorption

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R17, HARD OUTSIDE.  
Active source: H0021 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, Conjecture 1.4.  
Status after this run: **OPEN / PARTIAL / ACTIVE**.

## 0. Continuity, current source, exclusions, and ownership

This is the first substantive H0021 run after R17's fresh reassignment. I continued from

`runs/R17/20260919_2144Z_g0004_recursive_module_handoff_h0021_c079_f1c7.md`

and from the mandatory inherited H0021 handoff

`runs/R16/2026-09-18T00-46-50Z_h0021-spread-capacity-handoff-h0022_91e4.md`

rather than restarting any of R16's linking-system, fixed-Hamilton-skeleton, or spread-capacity checks.

The predecessor targets stay closed operationally to R17 research:

- binary Chvatal--Sankoff LCS remains handed off at
  `0.792665992 <= gamma_2 <= 0.826275942762282626`, width
  `0.033609950762282626`;
- D0064 remains terminal in R17;
- G0004 was released after its second recovery and third post-recovery no-movement run.

At run start I reread/recovered the required current surfaces: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; the current H0021 claim; the newest R17 report; R16's H0021 handoff and its sharp almost-spanning/subcubic-core reports; the current H-intake identity for arXiv:2608.06358; and the newest neighboring H0022 handoff. The canonical H0021 claim now names **R17** as exclusive owner and preserves `Delta_near=2`.

A fresh bounded 2026-09-19 public-source check recovered arXiv:2608.06358v1 as the current primary paper. The paper still states Conjecture 1.4 explicitly:

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\quad\text{is whp }\mathcal T_{n,\Delta}\text{-universal}
\]

for every fixed `epsilon>0` and integer `Delta>=2`. Exact-title, arXiv-id, author, and Conjecture-1.4 searches did not recover a later primary source claiming the sharp theorem. This is bounded dated evidence, not a global novelty certificate.

The source itself identifies the sharp linking-system statement (Conjecture 1.6) as a possible intermediate step, and explains why its current proof needs a large constant: the raw rooted-linear-forest family has poor spread near `psi=1`, so the authors first manufacture a rich family of flexible prefixes and only then apply the expectation-threshold theorem to the complements.

### Frozen metric

`Delta_near` is the largest `D>=2` for which there is a complete source-matching proof that, for every fixed `epsilon>0`, whp

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\]

contains **every** `n`-vertex tree of maximum degree at most `D`.

Before: `Delta_near=2`.  
After: `Delta_near=2`.

A new architecture obstruction is PARTIAL and does not move this metric. Since R17's H0021 counters were explicitly `NOT STARTED` at reassignment, this run starts the R17 substantive unchanged streak at `1`; it does not inherit R16's already-exhausted streak as though the route were unchanged.

## 1. Inherited facts I used rather than reproved

The following are inherited and are only inputs here.

1. R16 proved sharp-density almost-spanning universality for every fixed maximum degree, leaving an explicit residual of order
   \[
   \Theta\!\left(\frac{n\log\log n}{\log n}\right).
   \]
   For `Delta=3`, its displayed residual coefficient is `(30/c+o(1))` at `p=c log n/n`.
2. For subcubic trees with `L` leaves, suppressing degree-two vertices gives a core with `2L-2` vertices and `2L-3` edges. Uniformly subdivided cubic cores show that the hard structural scale `L=Theta(n loglog n/log n)` is real.
3. The number of low-leaf subcubic homeomorphism types is subexponential: R16 proved
   \[
   N_{n,L}^{(3)}\le16^L {n-2\choose 2L-4}.
   \]
4. R16's final H0021 run proved a **method obstruction**, not a source lower bound: if the completion is supported on one fixed Hamilton cycle cut into `r` blocks, then even random block order/orientation/shift leaves the completion-edge support too small for the source's generic `q`-spread hitting theorem to work in an arbitrarily small `epsilon log n/n` residual layer.
5. That last obstruction did **not** show the actual random completion fails. This run asks that stronger question first, as required by the counterexample-first rule.

## 2. Methods #8 + #23 — discretize the Pósa/reservoir idea and try to break it

The fresh route proposed at reassignment was to leave the source's linking-system framework and test a Pósa-rotation / reservoir-absorption architecture. The first issue is how much endpoint flexibility a block must possess before an independent sprinkle can connect all the blocks.

The right finite state is much smaller than a transfer matrix: one supervertex per block, carrying only the set of host vertices to which its unresolved target ports can still move before the final sprinkle.

### Definition 2.1 (pre-sprinkle flexible-port system)

Condition on an arbitrary first-round construction. It outputs `r=r(n)` pairwise vertex-disjoint port sets

\[
P_1,\ldots,P_r\subseteq[n],
\qquad |P_i|\le s.
\]

The sets may be chosen in any adaptive way from all previously exposed randomness, but they are fixed before a fresh independent sprinkle

\[
G_2\sim G(n,p_2)
\]

is exposed.

Define the **port graph** `H` on `[r]` by

\[
ij\in E(H)
\quad\Longleftrightarrow\quad
E_{G_2}(P_i,P_j)\ne\varnothing.
\tag{2.1}
\]

Any block-completion scheme whose inter-block target edges must all be supplied by `G_2` can only connect blocks along edges of `H`. In particular, if every one of the `r` blocks has to participate in one connected target quotient (a path is already enough), then `H` may not have an isolated vertex.

The sets `P_i` are deliberately allowed to encode **all** old-layer Pósa rotations, local switches, orientation choices, or internal block variants. Thus a failure below is not repaired by merely randomising the block order after the sprinkle.

### Lemma 2.2 (exact auxiliary random graph)

Conditional on the first round and the sets `(P_i)`, the edge indicators of `H` are independent. Moreover

\[
\Pr(ij\in E(H)\mid P_1,\ldots,P_r)
=1-(1-p_2)^{|P_i||P_j|}
\le q,
\tag{2.2}
\]

where

\[
q:=1-(1-p_2)^{s^2}\le p_2s^2.
\tag{2.3}
\]

Consequently `H` is stochastically dominated by `G(r,q)`.

#### Proof

For different unordered pairs `{i,j}`, the sets of physical sprinkle edges `P_i x P_j` are disjoint because the port sets are pairwise disjoint. Hence the superedge events are independent. Formula (2.2) is exact, and monotonicity in `|P_i||P_j|` gives the domination. The last inequality is the union bound (or Bernoulli's inequality). `QED`.

This is the promised discretisation: after the old layer is frozen, a very broad class of block-rotation completions has a one-parameter obstruction, `q r`.

## 3. Actual failure theorem, stronger than the old q-spread obstruction

### Theorem 3.1 (zero-defect port-width barrier)

Under Definition 2.1, suppose

\[
q r\le \log r-\omega(1).
\tag{3.1}
\]

Then, uniformly over every first-round construction and every resulting family of pairwise disjoint port sets of size at most `s`, with conditional probability `1-o(1)` the port graph `H` has an isolated vertex.

Therefore **no** completion architecture of this type can realise a connected spanning quotient on all `r` blocks.

#### Proof

It is enough by stochastic domination to prove the isolated-vertex statement for `J\sim G(r,q)`. Let `I` be the number of isolated vertices. Then

\[
\mu:=\mathbb E I=r(1-q)^{r-1}.
\tag{3.2}
\]

Under (3.1), `q=o(1)` and

\[
\mu=\exp\{\log r-(1+o(1))qr\}\to\infty.
\tag{3.3}
\]

For distinct vertices `u,v`,

\[
\Pr(u,v\text{ both isolated})=(1-q)^{2r-3},
\]

whereas

\[
\Pr(u\text{ isolated})^2=(1-q)^{2r-2}.
\]

Thus

\[
\frac{\operatorname{Var} I}{\mu^2}
\le \frac1\mu+\frac{q}{1-q}=o(1).
\tag{3.4}
\]

Chebyshev gives `I>0` whp. Having an isolated vertex is a decreasing graph property, so the stochastic domination transfers the conclusion from `J` to `H`. `QED`.

### Corollary 3.2 (critical path-block scale)

Let

\[
r=\frac nk,
\qquad
p_2=\delta\frac{\log n}{n},
\]

where `delta>0` is fixed and

\[
k=(\kappa+o(1))\frac{\log n}{\log\log n}
\]

for a fixed `kappa>0`. If for some fixed `eta>0`

\[
s^2\le (1-\eta)\frac{k}{\delta},
\tag{3.5}
\]

then the port graph has an isolated block whp. In particular a zero-defect block architecture at the source scale requires

\[
\boxed{
s=\Omega\!\left(\sqrt{\frac{k}{\delta}}\right)
=\Omega\!\left(\sqrt{\frac{\log n}{\delta\log\log n}}\right).
}
\tag{3.6}
\]

#### Proof

By (2.3),

\[
qr\le p_2s^2\frac nk
\le (1-\eta)\log n.
\]

Since `log r=log n-o(log n)`, this is at most `log r-Theta(log n)`, so Theorem 3.1 applies. `QED`.

This is a genuine strengthening of R16's fixed-cycle calculation. The old argument said that a **generic spread theorem cannot certify** a two-port fixed-skeleton completion at coefficient `epsilon`. Corollary 3.2 says that, in the natural independent-sprinkle version, the completion itself actually fails whp: after all permutations and orientations are allowed, an isolated superblock remains unless the old layer supplies enough endpoint flexibility.

## 4. A sharper tradeoff when an absorber is allowed to discard exceptional blocks

The zero-defect condition is intentionally severe. A reservoir architecture is allowed to repair some exceptional blocks. The same calculation gives the exact scale it must beat.

### Theorem 4.1 (port width versus exceptional-block budget)

Keep Definition 2.1. Let `t=t(r)` be the maximum number of blocks that a later absorber is allowed to remove from the port-graph completion. Put

\[
\mu=r(1-q)^{r-1}.
\]

If

\[
\mu/t\longrightarrow\infty,
\tag{4.1}
\]

(with the convention that `t=0` is Theorem 3.1), then whp `H` has more than `t` isolated vertices. Hence no scheme which must connect all but at most `t` blocks through sprinkle edges can succeed.

A convenient sufficient condition is

\[
q r\le \log\frac rt-\omega(1).
\tag{4.2}
\]

#### Proof

The second-moment computation (3.4) gives

\[
I=(1+o_{\Pr}(1))\mu
\]

for `G(r,q)` whenever `mu->infinity` and `q=o(1)`. If `mu/t->infinity`, then `I>t` whp. Stochastic domination transfers the same lower bound on isolated-block count to `H`. For (4.2),

\[
\mu/t
=\frac rt\exp(-(1+o(1))qr)\to\infty.
\]
`QED`.

### Source-scale interpretation

Again take

\[
r=n/k,\qquad
p_2=\delta\log n/n,\qquad
k=(\kappa+o(1))\log n/\log\log n.
\]

Suppose a block architecture is allowed to mark at most

\[
t=\Theta(r/k)
\]

blocks exceptional. This is the block-count scale corresponding to an `Theta(n/k)` **vertex** repair budget if an exceptional whole `k`-block must be rerouted.

Then

\[
\log(r/t)=\log k+O(1)=(1+o(1))\log\log n.
\]

Since

\[
p_2 r=(\delta/\kappa+o(1))\log\log n,
\]

Theorem 4.1 shows that if

\[
s^2 < (1-o(1))\frac{\kappa}{\delta},
\tag{4.3}
\]

there are whp too many isolated blocks for such an absorber.

Thus an `Theta(n/k)` repair window changes the design requirement dramatically:

\[
\boxed{
\text{zero exceptional blocks: }s\gtrsim\sqrt{k/\delta};
\qquad
\Theta(r/k)\text{ exceptional blocks: }s\gtrsim\sqrt{\kappa/\delta}.
}
\tag{4.4}
\]

If the sprinkle receives only `delta=Theta(epsilon)` of the sharp-density budget, then a realistic residual architecture therefore needs at least **order `epsilon^{-1/2}` endpoint choices per critical block**, unless it has a cheaper repair operation than discarding/rerouting a whole block.

This last qualification matters. I am **not** claiming every absorber pays `k` vertices per bad block. A more local switch could cost only `O(1)` vertices. The theorem is stated in the correct invariant form—the exceptional-block budget `t`—and the conversion to a vertex budget is only for architectures whose repair really replaces a whole path gadget.

## 5. Method #28 — why “typical order” does and does not help

The reassignment plan proposed replacing the simultaneous `for all` burden by a typical-embedding statement and then recovering universality through compression. The port graph shows exactly where that can matter.

For equal port-set sizes `|P_i|=s`, conditional on the first round the port graph is **exactly**

\[
G\!\left(r,1-(1-p_2)^{s^2}\right).
\]

Therefore randomising the order/orientation of the path blocks after the sprinkle cannot defeat Theorem 3.1: if the port graph has an isolated supervertex, **every** ordering fails simultaneously. This directly stress-tests the “typical” relaxation rather than only one fixed permutation.

On the other hand, the obstruction is close to the correct coarse scale. The classical Hamiltonicity threshold for `G(r,q)` is

\[
q=\frac{\log r+\log\log r+\omega(1)}{r}.
\]

So in the abstract supergraph model, once old-layer rotations/switches make the port sets large enough that `q r` crosses `log r+loglog r`, a typical port graph is Hamiltonian and a quotient **path** no longer faces a supergraph-level obstruction. This does not solve H0021—the candidate-port realisations must be compatible with the same embedded target paths and must remain vertex-disjoint—but it identifies a sharp design target instead of another vague “add flexibility” instruction.

The source paper itself points in the same qualitative direction from a different method: near `psi=1`, fixed rooted paths have poor spread, so it manufactures many well-spread prefixes whose other endpoints remain flexible. The new calculation here says how much flexibility a completely different block/sprinkle architecture must buy before it can even clear the isolated-block barrier.

## 6. Application to the inherited stress tree

R16's terminal H0021 report used a subcubic stress family `T_{r,k}` consisting of `r` disjoint `k`-vertex paths, with a residual matching that joins designated internal ports of consecutive target paths. Contracting the path blocks gives a path on `r` supervertices.

Consider any two-round completion architecture of the following broad form:

1. before `G_2` is exposed, it embeds or otherwise fixes `r` disjoint path gadgets;
2. for gadget `i`, **all** images to which its unresolved residual target ports can be moved using only old-layer switches lie in a fixed set `P_i` of size at most `s`;
3. all residual edges between different gadgets must come from the independent `G_2` sprinkle;
4. at most `t` gadgets may be sent to a separate exceptional repair routine.

Then Theorem 4.1 applies verbatim. This includes arbitrary post-sprinkle permutation of the blocks and arbitrary use of their already-generated local orientation states: all such choices are already subsumed into `P_i`.

In particular:

- **bounded-port, zero-defect** versions of the fixed-backbone idea are genuinely impossible at sharp density, not merely beyond the reach of the generic spread theorem;
- an `Theta(n/k)` whole-block absorber can in principle lower the required port multiplicity from `Theta(sqrt k)` to `Theta(epsilon^{-1/2})`;
- therefore the next constructive question is very concrete: can one expose the main skeleton while retaining `C(epsilon)` mutually compatible endpoint images per critical chain, with `C(epsilon)` at least a constant multiple of `epsilon^{-1/2}`, and can the exceptional blocks be repaired without consuming more than the inherited `Theta(n/k)` window?

That is a materially different target from “prove an optimal linking system.” It asks only for enough local endpoint multiplicity to make the quotient graph cross its own sparse connectivity threshold.

## 7. What this run does **not** prove

The result is an architecture theorem, not a theorem about the source random graph property.

It does **not** prove or refute Conjecture 1.4, does not prove `Delta_near>=3`, and does not show that every Pósa-rotation or absorption proof must literally have disjoint pre-sprinkle port sets. A successful proof may use overlapping/global switchers, expose edges adaptively rather than in two independent rounds, or repair isolated blocks locally at cost `O(1)` rather than reroute a whole `k`-block.

These escape routes are exactly why the honest source metric remains

\[
\boxed{\Delta_{\rm near}=2.}
\]

No finite enumerative claim was introduced in this run, so I did not spend the run manufacturing an exact-arithmetic checker. The finite identity (2.2) is proved symbolically from disjoint independent edge sets; the theorem-sized probabilistic claims are proved on the page.

## 8. Method outcomes and next route

### #8 GO THE OTHER WAY AND DISCRETIZE — **success**

The Pósa/reservoir completion question collapses, after conditioning on the old layer, to a supergraph on `r` blocks. Its edge probability is exactly controlled by the port-set sizes. This removes all irrelevant internal path detail from the first obstruction.

### #23 DO WHAT THE PROPOSER DID NOT EXPECT — **success as a refutation of the naive fresh route**

Rather than try to prove that bounded local endpoint flexibility suffices, the run shows it actually fails in an independent sprinkle. The failure is an honest isolated-superblock event and persists after arbitrary block permutation/orientation.

### #28 REPLACE FOR ALL WITH FOR TYPICAL — **mixed, but quantitatively informative**

Typicality cannot help below the isolated-block threshold because one isolated block defeats every ordering. Above the corresponding supergraph Hamiltonicity scale, typical order is no longer the obstruction. Thus the route survives only if the first round creates enough endpoint multiplicity.

The unused H0021 Section-B numbers after this run are

`{14,15,16,17,26,29}`.

For the next substantive H0021 run I reserve **#15 BREAK THE SYMMETRY ON PURPOSE / #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE / #29 ADD THE POINTS AT INFINITY**. The intended target is to build or rule out an `epsilon`-dependent switcher that gives each critical chain `Theta(epsilon^{-1/2})` compatible endpoint images while preserving disjointness, using the global reservoir rather than internal block chords. If that route does not move `Delta_near`, the run will say so plainly rather than add another certificate-only commit.

## 9. Prior-art / neighboring-source note

The current primary H0021 source already explains that the sharp problem is entangled with optimal-depth linking systems and that its own spread improvement works by preserving flexible prefix endpoints. I therefore do **not** claim the general principle “endpoint flexibility helps” as novel.

The specific port-graph/exception-budget calculation above is a new R17 derivation relative to the inherited repository state. R16's previous H0021 result was a support/spread-capacity obstruction for a fixed Hamilton skeleton; it explicitly stopped short of proving that the actual randomized completion fails. Theorem 3.1 fills exactly that gap for the independent-sprinkle bounded-port architecture.

The neighboring H0022 line from the same source was also read: R16 eventually handed it off after its own two recoveries, with an exact positive Newton-overlap expansion and a second-moment obstruction. I did not import H0022 as a solved black box or alter its files.

## 10. Model / scheduler-control truth

This runtime identifies the model as **GPT-5.6 Sol**. No authenticated reasoning-effort field is exposed to this report, so the reasoning level is recorded as **UNVERIFIED**, not “maximum.”

The scheduler/control surface available in this environment still exposes prompt/title/schedule/timing/enablement operations but no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-model/applied-effort telemetry. Thus `GPT-6 / maximum` remains prompt text only from this surface. Enforcing it would require an owner-authorized product/API/admin surface that actually exposes those controls and execution attestation.

The historical P26 `You cannot modify this task` incident remains authorization-context-specific; the root ledger records that P26 later accepted its full update in another authorized context. The legitimate remedy is the owning/admin-authorized context or platform support, not duplication, permission bypass, or a repository edit masquerading as scheduler control.

No scheduler, permission, workflow, email, Drive, purchase, public posting, shared-root ledger, peer file, or canonical claim was modified in this run.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R17
  allocation: HARD_OUTSIDE
  active_source:
    id: H0021
    statement: Cohen_Antonir_Lichev_Zhukovskii_Conjecture_1_4
    source: arXiv_2608_06358v1
    canonical_owner: R17
    status: OPEN_PARTIAL_ACTIVE
  predecessor_targets:
    binary_LCS: HANDED_OFF_FROZEN
    D0064: TERMINAL_FROZEN
    G0004: HANDED_OFF_RELEASED
  metric:
    name: Delta_near
    before: 2
    after: 2
    movement: none
  r17_h0021_substantive_unchanged_streak:
    before: NOT_STARTED
    after: 1
  section_B_methods: [8, 23, 28]
  mathematical_progress:
    theorem: PRE_SPRINKLE_PORT_GRAPH_IS_DOMINATED_BY_G_r_q
    zero_defect_barrier: qr_below_log_r_forces_isolated_block_whp
    defect_tradeoff: expected_isolated_blocks_vs_exception_budget_t
    sharp_scale_zero_defect: s_squared_order_k_over_delta
    sharp_scale_block_repair_window: s_squared_order_kappa_over_delta
  source_metric_moved: false
  new_finite_checker: none_no_new_finite_enumerative_claim
  new_audit: none
  closure_claim: false
  shared_roots_edited: false
  peer_files_edited: false
  canonical_claim_edited: false
  scheduler_or_permission_edits: false
  email_or_drive_used: false
```

**Bottom line:** R17 did not move the source metric, but it converted the fresh Pósa/reservoir idea into a quantitative theorem: after the old layer is frozen, a block completion fed by an independent `delta log n/n` sprinkle needs enough endpoint multiplicity to clear an isolated-superblock threshold. With no exceptions this means `s=Omega(sqrt(k/delta))`; with an `Theta(r/k)` whole-block repair allowance it means `s=Omega(delta^{-1/2})`. The next constructive route is therefore to manufacture `epsilon`-dependent compatible endpoint multiplicity, not to repeat fixed-skeleton spread checks.