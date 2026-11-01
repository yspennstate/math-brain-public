Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; post-recovery substantive unchanged count reaches `3`, so the SECOND SECTION-I STUCK TRIGGER is now active; methods #10 DERANDOMIZE / #21 ASK WHO ELSE HAS THIS SHAPE / #26 HUNT THE SPORADIC CASE.**

# R17 C075 — G0004: derandomized contact selection hits the same barrier; a recursive tree-spine family forces a new rate obstruction

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R17, HARD OUTSIDE.  
Status: **OPEN / PARTIAL / STUCK RECOVERY 1/2; SECOND STUCK TRIGGERED FOR NEXT RUN**.

## 0. Continuity, ownership, source, and what was read

The canonical claim `operations/claims/G0004.md` still names **R17** as exclusive owner of Lucas Flammant's finite-graph percolation Conjecture 2.2. The original Chvátal--Sankoff binary-LCS source remains terminally handed off at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626,
\]

and the Rhodes--Vargas D0064 successor remains terminal at `R_class=0/3`. Neither predecessor is reopened.

At run start I reread the required campaign and ownership surfaces:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/G0004.md`;
- newest own report C074 and the preceding G0004 reports C069--C073;
- the R7-02 G0004 failure-kernel / selector screen;
- the canonical G-intake record and current neighboring ownership screens that continue to identify G0004 as R17-owned.

No current root exclusion or ownership record supersedes the claim.

A fresh 2026-09-19 web check of arXiv:2609.03492 and searches by the exact title, `Conjecture 2.2`, `tree`, `d-ary tree`, and the author's name still found the source paper as the current primary item and no later primary source claiming the unrestricted conjecture or the tree-spine rate calculation below. The source still says that the general finite-graph conjecture is open, proves the outer-face planar case with failure at most `2 sqrt(epsilon)`, and notes that replacing connectivity by arbitrary increasing events is false. This is bounded negative evidence, not a global novelty certificate.

The fixed source-wide metric remains

\[
U_F:=\inf\left\{u:\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under all source quantifiers}\right\}.
\]

Before: `U_F=1`. After: `U_F=1`.

The new result below is a lower obstruction on how fast a valid universal modulus could converge. It does not prove the full conjecture and therefore does not move `U_F`.

## 1. Exact failure-kernel setup retained

For each boundary vertex `b`, write

\[
q_b(\omega)=1-\mathbb P(E_b\mid\pi=\omega).
\]

Then `q_b` is decreasing, `0<=q_b<=1`, and

\[
\mathbb E q_b\le\varepsilon.
\]

Let

\[
C_b=\{o\leftrightarrow b\},\qquad
S(\omega)=\{b\in B:C_b(\omega)\},\qquad
N=|S|,
\]

and `C={N>0}`. On `C`,

\[
m(\omega)=\min_{b\in S(\omega)}q_b(\omega),
\]

with `m=0` on `C^c`. The exact failure ratio is

\[
R=\frac{\mathbb E m}{\mathbb P(C)}.
\]

C074 showed that the uniform-contact law differs from the connection-Palm law exactly by the density `M/N`, where `M=E[N|C]`, and established all factorial inequalities

\[
\mathbb E\left[\binom Nk m\right]\le\varepsilon\,\mathbb E\binom Nk,
\qquad k\ge1.
\]

The question this run was whether a deterministic selector or a small non-star connectivity pattern can turn that structure into a source-wide upper bound.

## 2. Method #10 — DERANDOMIZE: exact priority selector, but it collapses to the old `epsilon M` barrier

Fix an arbitrary deterministic total order `prec` of the boundary set `B`. On `C`, let `tau_prec(omega)` be the first boundary vertex in that order that is connected to `o`.

For each `b`, define

\[
D_b=\bigcap_{a\prec b}C_a^c.
\]

The event `D_b` is decreasing. Since `q_b` is decreasing, the product

\[
q_b\,\mathbf 1_{D_b}
\]

is also decreasing. Therefore Harris--FKG against the increasing event `C_b` gives

\[
\begin{aligned}
\mathbb E\big[q_b\mathbf 1_{\{\tau_\prec=b\}}\big]
&=\mathbb E\big[\mathbf 1_{C_b}q_b\mathbf 1_{D_b}\big]\\
&\le \mathbb P(C_b)\,\mathbb E[q_b\mathbf 1_{D_b}]\\
&\le \varepsilon\,\mathbb P(C_b).
\end{aligned}
\tag{2.1}
\]

Summing over `b`,

\[
\boxed{
\mathbb E[q_{\tau_\prec};C]\le\varepsilon\,\mathbb E N.
}
\tag{2.2}
\]

Since `m<=q_{tau_prec}` on `C`, this recovers

\[
R\le\varepsilon\,\mathbb E[N\mid C].
\]

Thus a deterministic first-contact rule by itself does **not** improve the old bounded-contact theorem.

There is also an exact derandomization identity. If `Pi` is a uniform random permutation of `B`, independent of percolation, then conditional on a configuration with `N>0`, the first connected boundary point is uniform on `S`. Hence

\[
\boxed{
\mathbb E_\Pi\left[q_{\tau_\Pi}(\omega)\mid\omega\right]
=\frac1{N(\omega)}\sum_{b\in S(\omega)}q_b(\omega).
}
\tag{2.3}
\]

Consequently some deterministic order has expected selected failure no larger than the uniform-contact average. But applying Harris separately to that order still yields only (2.2). This identifies the precise failure of the derandomization route: **the loss occurs when one sums the marginal connection probabilities `sum_b P(C_b)=E N`; random priorities do not remove that multiplicity.**

Outcome of method #10: useful obstruction diagnosis, no source-metric movement.

## 3. Methods #21 and #26 — branching-process shape and the first genuinely worse-than-star recursive family

The star calculation in C069 gave worst failure of order `epsilon log(1/epsilon)` within stars. The next natural object with the same local `one connected label survives while alternatives are suppressed` mechanism is a rooted branching tree, where that mechanism can repeat at every scale.

This produces a much larger failure probability than the star and a new obstruction on any possible quantitative version of Flammant's conjecture.

### 3.1 Construction

Fix integers `d>=2` and `h>=1`. Let `T_{d,h}` be the complete rooted `d`-ary tree of depth `h`. Let `o` be its root and `B` its `d^h` leaves. Perform Bernoulli bond percolation with the same edge parameter `p` on every edge.

For a leaf `b`, consider its unique root-to-leaf path. At each of the `h` internal vertices on this path there are `d-1` child edges not lying on the path. Call all of these the **sibling edges of b**. There are exactly `(d-1)h` such edges.

Define the decreasing event

\[
D_b=\{\text{every sibling edge of }b\text{ is closed}\},
\]

and take the source event

\[
E_b=D_b^c.
\]

Then `E_b` is increasing and

\[
\mathbb P(E_b)=1-\varepsilon_h,
\qquad
\boxed{\varepsilon_h=(1-p)^{(d-1)h}.}
\tag{3.1}
\]

Equivalently, in the failure-kernel formulation `q_b=1_{D_b}` and `E q_b=epsilon_h` exactly.

### 3.2 Exact characterization of source failure

Let

\[
C_h=\{o\leftrightarrow B\}.
\]

On `C_h`, source failure means that every connected leaf has `E_b=0`, equivalently every connected leaf satisfies `D_b`.

**Claim.** Source failure occurs exactly when the root cluster reaches depth `h` through a single open spine and, at every vertex of that spine, the path edge is open while all `d-1` sibling child edges are closed.

**Proof.** If a connected leaf `b` satisfies `D_b`, then at every ancestor of `b` all sibling child edges are closed. Since the path edges to `b` are open, there is exactly one open child edge at every spine vertex. Therefore no other leaf can be connected to `o`.

Conversely, if a root-to-leaf spine has its path edge open and all sibling child edges closed at every level, the terminal leaf `b` is connected and is the unique connected boundary vertex; moreover `D_b` holds, so `E_b` fails. QED.

For two distinct leaves the corresponding spine events are disjoint: at their first divergence one event requires one child edge open and the other closed, while the other event requires the reverse.

Each fixed leaf-spine event requires exactly `h` specified edges open and `(d-1)h` specified sibling edges closed; all edges below closed sibling edges are unrestricted. Therefore

\[
\boxed{
\mathbb P(\text{source failure})
=d^h p^h(1-p)^{(d-1)h}
=\big(dp(1-p)^{d-1}\big)^h.
}
\tag{3.2}
\]

Since this event is a subset of `C_h`, the exact conditional failure ratio is

\[
R_{d,h,p}
=\frac{\big(dp(1-p)^{d-1}\big)^h}{\mathbb P(C_h)}
\ge \big(dp(1-p)^{d-1}\big)^h.
\tag{3.3}
\]

If `dp>1`, `P(C_h)` is the depth-`h` survival probability of a supercritical `Bin(d,p)` Galton--Watson process and converges to a positive survival probability, so (3.3) has the correct exponential rate, not merely a crude lower bound.

### 3.3 Convert the construction to an epsilon exponent

Assume `dp>1`. Since `p>1/d`, the function `dp(1-p)^{d-1}` lies below one: it is already `(1-1/d)^{d-1}<1` at `p=1/d` and decreases for larger `p`. Define

\[
\alpha(d,p)
:=
\frac{\log\big(dp(1-p)^{d-1}\big)}{(d-1)\log(1-p)}
=1+\frac{\log(dp)}{(d-1)\log(1-p)}.
\tag{3.4}
\]

Then `0<alpha(d,p)<1`, and by (3.1)--(3.3),

\[
\boxed{
R_*(\varepsilon_h)\ge R_{d,h,p}\ge \varepsilon_h^{\alpha(d,p)}.
}
\tag{3.5}
\]

This is already qualitatively worse than the star rate `epsilon log(1/epsilon)`: the recursive branching mechanism amplifies a rare decreasing failure at each level and produces a genuine fractional power.

### 3.4 Universal Hölder obstruction `1-1/e`

Now let `d>=3` and choose

\[
p=\frac e d.
\]

Then `dp=e>1`, and

\[
\alpha_d
=1+\frac{1}{(d-1)\log(1-e/d)}
=1-\frac{1}{(d-1)(-\log(1-e/d))}.
\tag{3.6}
\]

As `d->infinity`,

\[
(d-1)(-\log(1-e/d))\longrightarrow e,
\]

so

\[
\boxed{
\alpha_d\longrightarrow 1-\frac1e.
}
\tag{3.7}
\]

Therefore:

### Theorem 3.1 — rate obstruction for any quantitative form of Flammant 2.2

For every

\[
\beta>1-\frac1e,
\]

the full source failure envelope cannot satisfy

\[
R_*(\varepsilon)=O(\varepsilon^\beta)
\qquad(\varepsilon\downarrow0).
\]

#### Proof

Choose `d` sufficiently large that `alpha_d<beta`. For the depth sequence `h->infinity`, let `epsilon_h` be (3.1) with `p=e/d`. Then `epsilon_h->0`, and (3.5) gives

\[
\frac{R_*(\varepsilon_h)}{\varepsilon_h^\beta}
\ge
\varepsilon_h^{\alpha_d-\beta}
\longrightarrow\infty.
\]

QED.

Equivalently, if the conjecture is ultimately proved with a Hölder-type failure bound

\[
1-\phi(\varepsilon)=O(\varepsilon^\beta),
\]

then necessarily

\[
\boxed{\beta\le1-1/e\approx0.6321.}
\]

No claim is made that `1-1/e` is the true global exponent. It is a rigorous obstruction furnished by this explicit outerplanar tree family. The source's existing outer-face planar upper bound `R<=2 sqrt(epsilon)` has exponent `1/2`, so the present construction leaves a nontrivial exponent window between `1/2` and `1-1/e` even on trees.

For the large-degree scaling `p=c/d` with fixed `c>1`, the same calculation gives

\[
\alpha(c)=1-\frac{\log c}{c}+o_d(1).
\]

Within this scaling, `log(c)/c` is maximized at `c=e`, explaining why `1-1/e` is the natural exponent produced by the recursive one-open-child spine mechanism.

Outcome of methods #21 and #26: **substantial new source-valid lower obstruction, but no upper-bound movement in the fixed metric.**

## 4. Exact checker

The finite combinatorial core of the tree-spine identity was checked with exact rational arithmetic, not simulation:

- script: `artifacts/R17/g0004_tree_spine_exact_check_c075.py`;
- output: `artifacts/R17/g0004_tree_spine_exact_check_c075.out`;
- final output ends `EXACT_TREE_SPINE_CHECK_PASS`.

The checker exhaustively enumerates all edge configurations for three small trees and verifies exactly that every `q_b` has expectation `(1-p)^((d-1)h)` and that the source-failure probability equals `[dp(1-p)^(d-1)]^h`. The final archived output was read after correction of an intermediate transcription typo; all mathematical claims in this report use the corrected exact output.

This checker is a self-check only. The theorem-sized family argument is proved on the page above and is not promoted to independently audited status.

## 5. What this changes about the obstruction

C074 showed that any counterexample must exploit the inverse-contact-size bias `M/N` and can concentrate failure on unusually small-contact configurations. The tree family above shows that this is not merely a pathological distributional possibility: **genuine connectivity can realize the mechanism recursively.**

On a failed tree-spine configuration, `N=1`. On typical supercritical configurations, `N` is exponentially larger in depth. Thus the failure event lives exactly in the extreme lower tail singled out by C074, while each individual boundary failure event still has probability only `epsilon_h`.

This explains why no argument based only on controlling one or finitely many contact moments is likely to recover a near-linear modulus. The adaptive minimum can harvest exponentially many possible spines, while each leaf pays its own exponentially small decreasing-event budget.

At the same time the construction still gives a positive power of `epsilon`, not a constant. So it does **not** refute Flammant's qualitative conjecture.

## 6. Literature-shape check from method #21

The closest proof technology found in the bounded search remains:

- Harris--FKG and the van den Berg--Häggström--Kahn conditional cluster inequalities;
- stopping-set / decision-tree methods used in percolation and OSSS-type arguments;
- the source paper's own left-first depth-first exploration in the planar outer-face case.

The new tree calculation is naturally a Galton--Watson / branching-process object: `P(C_h)` is exactly survival to generation `h` for offspring `Bin(d,p)`, while source failure is the much rarer event that every generation along the surviving lineage has exactly one open child and all siblings closed.

The bounded 2026-09-19 search did not locate a paper applying this exact recursive-spine event to Flammant's Conjecture 2.2 or deriving the exponent `1-1/e`. This is a prior-art search record, not a novelty certificate.

## 7. Section-I status and next required action

The fixed metric has now failed to move in three consecutive substantive post-recovery runs:

- C073: cluster-local linear-modulus theorem, `U_F=1`;
- C074: contact-debiasing / factorial hierarchy / lower-tail reduction, `U_F=1`;
- C075: recursive tree-spine rate obstruction, `U_F=1`.

Therefore the **second Section-I stuck trigger is active**. The next R17 G0004 run must be a thinking-only stuck report, not a fourth ordinary lemma run. Recovery count remains `1/2` until that report chooses exactly one recovery action; that next choice will be recovery `2/2`.

The new blocker is sharper than before:

\[
\boxed{
\text{prove }R_*(\varepsilon)\to0\text{ despite recursive low-contact spine amplification,}
\quad\text{or push the recursive construction to a nonvanishing ratio.}
}
\]

The simplest still-unproved special case is now **arbitrary rooted trees with arbitrary increasing source events**. The present complete `d`-ary construction is an obstruction/lower bound, not an upper theorem for trees.

The nearest solved source-valid regime remains the outer-face planar theorem from Flammant, which includes trees abstractly but uses a planar exploration and yields only `2 sqrt(epsilon)`; the R17 cluster-local theorem gives `1-epsilon` under a strong event-locality hypothesis. What is missing is a tree or general-graph argument that handles arbitrary non-cluster-local events while retaining a dimension-free decay rate.

Fresh Section-B methods reserved for the required stuck-thinking run are:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — target an all-trees theorem before arbitrary graphs;
- **#7 TAKE THE LIMIT** — formulate the recursive extremal problem as an infinite-tree / branching dynamic program;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE** — investigate whether the `1-1/e` exponent is the value of a known branching-selection or entropy variational problem that has an upper-bound theorem.

These differ from #10/#21/#26 and all immediately preceding triples.

## 8. Model/scheduler control status

The exposed scheduler interface still provides title, prompt, schedule, timing mode, and enablement controls but no bindable model-family selector, no reasoning-effort selector, and no authenticated runtime-model telemetry. Therefore the requested `GPT-6 / maximum` remains prompt-only from this surface; this run can only honestly report GPT-5.6 Sol with reasoning UNVERIFIED.

The historical P26 `You cannot modify this task` result is an authorization-context issue. The repository also records that P26 was subsequently updated from another authorized context. The legitimate workaround is the owning/admin-authorized scheduler surface or platform support; task duplication, permission bypass, or repository edits are not substitutes.

No scheduler change was attempted in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R17
  source_id: G0004
  source: "Lucas Flammant, arXiv:2609.03492v2, Conjecture 2.2"
  allocation: HARD_OUTSIDE
  owner: R17
  status_before: OPEN_PARTIAL_STUCK_RECOVERY_1_OF_2
  status_after: OPEN_PARTIAL_SECOND_STUCK_TRIGGERED
  fixed_metric: U_F
  value_before: 1
  value_after: 1
  metric_movement: false
  methods_tried: [10, 21, 26]
  new_results:
    - "Exact deterministic-priority selector lemma; random-order average equals the uniform-contact selector, but one-step Harris still loses E[N]."
    - "Complete d-ary depth-h tree construction with epsilon_h=(1-p)^((d-1)h) and exact source failure [d p (1-p)^(d-1)]^h."
    - "For every beta>1-1/e, R_*(epsilon) is not O(epsilon^beta); hence any Holder-type universal failure modulus must have beta<=1-1/e."
  closure: false
  recovery_count_before: "1/2"
  recovery_count_after: "1/2"
  next_run: "MANDATORY SECTION-I THINKING-ONLY STUCK REPORT; choose recovery 2/2"
  next_methods: [4, 7, 17]
  artifacts:
    - artifacts/R17/g0004_tree_spine_exact_check_c075.py
    - artifacts/R17/g0004_tree_spine_exact_check_c075.out
  predecessor_sources_reopened: false
  shared_root_files_modified: false
  peer_files_modified: false
  scheduler_modified: false
```
