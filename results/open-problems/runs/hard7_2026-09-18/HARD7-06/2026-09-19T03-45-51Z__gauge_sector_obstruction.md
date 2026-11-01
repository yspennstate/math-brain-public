Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** Primary source metric **no movement**: `L_6 >= 0 -> L_6 >= 0`; methods actually tried: **B1 / B14 / B20**. The substantive result is an exact gauge/cohomology obstruction showing that the random-literal NAE-SAT ensemble used by the nearest solved 1RSB theory and the unsigned hypergraph-2-colouring source occupy globally different cycle-flux sectors even though every tree-local recursion is gauge-equivalent.

# HARD7-06 run 8 — the unsigned model is an exponentially rare gauge sector invisible to tree BP

Status: **PARTIAL / source OPEN under bounded current-literature review.**

Repository / branch: `yspennstate/math-open-problems` / `master`.

Canonical target remains `operations/claims/CKS-2024-RREG-HYPER2COL-K3.md`, owned by `HARD7-06`.

## 1. Continuity, exclusions, source status, and why this run did not restart from random 3-SAT

I reread the controlling HARD7 policy files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical CKS claim, the complete newest HARD7-06 checkpoint `2026-09-19T02-49-00Z__stuck2_bms_channel_port.md`, the neighboring R03/F0097 terminal handoff, and targeted intake/claim searches around random SAT/NAE/hypergraph colouring. No posted/settled collision for the CKS target was found.

The initial random 3-SAT candidate is not silently taken over. Its canonical F0097 history was owned by R03 and the newest R03 report is a terminal handoff/rotation hold after the third stuck episode. That historical handoff does not authorize HARD7-06 to overwrite or alias the claim. HARD7-06 therefore continues its already admitted, create-only CKS target.

The frozen primary source remains Evan Chang, Neel Kolhe and Youngtak Sohn, *Upper Bounds on the 2-Colorability Threshold of Random d-Regular k-Uniform Hypergraphs for k >= 3*, APPROX/RANDOM 2024, DOI `10.4230/LIPIcs.APPROX/RANDOM.2024.47`, full version arXiv:2308.02075. Their small-fixed-`k` lower side remains the relevant open issue; for `k=3`, the source upper-threshold root lies above `6`, so the present boundary subproblem is the uniformly random **simple unsigned** `6`-regular `3`-uniform hypergraph.

A bounded fresh literature screen on 2026-09-19 used the exact CKS title/DOI, `random regular hypergraph 2-colorability k=3 d=6`, `random regular NAE-SAT gauge literals`, and the recent reconstruction/1RSB literature. It recovered the CKS source, Ding--Sly--Sun's sufficiently-large-`k` random-regular NAE-SAT threshold theorem, Nam--Sly--Sohn's 1RSB cluster machinery, and Yuzhou Gu's 19 June 2026 arXiv:2606.21699 BMS-channel reconstruction theorem. I found no later source-matching theorem proving the unsigned simple `H_{n,6,3}` lower side. This is bounded negative evidence, not a claim of exhaustive worldwide openness.

The prior-art search for the exact gauge-sector observation below used `NAE-SAT gauge transformation literals cycle parity factor graph`, `NAE-SAT gauge symmetry literals factor graph`, `hypergraph 2-coloring gauge NAE-SAT literals`, and `random regular NAE-SAT literals gauge equivalent`. I did not find a source phrasing this exact application. The cohomological/cut-space mechanism itself is elementary and should be treated as folklore unless a broader prior-art search establishes otherwise. **No novelty claim is made for the gauge lemma.**

## 2. Frozen source metric

The source-relevant quantity remains

\[
L_6:=\sup\left\{L\in[0,1]:\liminf_{n\to\infty}
\Pr(H_{n,6,3}\text{ is 2-colorable})\ge L\right\},
\]

along the source-admissible `n` in the uniformly random simple `6`-regular `3`-uniform model.

This run proves a route obstruction and a source-compatibility reduction, not a positive probability lower bound. Therefore

\[
\boxed{L_6\ge 0\quad\longrightarrow\quad L_6\ge 0.}
\]

No finite example, local channel fixed point, reconstruction statement, or cluster surrogate is promoted to asymptotic source movement.

## 3. B1 + B14: change category and find the acting group

The second recovery selected in run 7 was to derive the true finite-`k` cluster transform and then try a Gu-style BMS-channel enclosure. Before doing population dynamics, I changed category: treat the literal vector as an `F_2` 1-cochain on the bipartite factor graph and quotient by the exact NAE gauge group.

Let

\[
G=(V\sqcup F,E)
\]

be any finite bipartite factor graph, and let a literal signing be

\[
\ell=(\ell_e)_{e\in E}\in\mathbb F_2^E.
\]

The NAE clause at `a in F` sees the bits

\[
(x_{v(e)}+\ell_e)_{e\in\delta a}\pmod 2.
\]

There are two exact gauge operations.

1. A variable flip `u in F_2^V` sends `x_v -> x_v+u_v` and simultaneously `ell_e -> ell_e+u_{v(e)}`.
2. A clause flip `z in F_2^F` sends `ell_e -> ell_e+z_{a(e)}` on every edge of the clause. NAE is invariant because complementing every input of a clause preserves the property “not all equal.”

Thus the literal vector is acted on by

\[
\delta:\mathbb F_2^V\oplus\mathbb F_2^F\to\mathbb F_2^E,
\qquad
[\delta(u,z)]_e=u_{v(e)}+z_{a(e)}.
\tag{3.1}
\]

Gauge-equivalent signings have isomorphic solution sets, the same solution count, and the same cluster cardinalities under the induced assignment flip.

### Proposition 3.1 — exact gauge-sector count

Let `c(G)` be the number of connected components and

\[
\beta_1(G):=|E|-|V|-|F|+c(G)
\]

the cycle-space dimension of the bipartite factor graph. Then

\[
\mathbb F_2^E/\operatorname{im}\delta\cong \mathbb F_2^{\beta_1(G)}.
\tag{3.2}
\]

Equivalently, literal signings split into exactly `2^{beta_1(G)}` equally sized gauge classes. If `ell` is iid uniform on `F_2^E`, then conditional on `G`,

\[
\boxed{
\Pr\{\ell\text{ is gauge-equivalent to the unsigned signing }0\mid G\}
=2^{-\beta_1(G)}.
}
\tag{3.3}
\]

A complete set of class invariants is given by the mod-2 literal flux around a cycle basis.

#### Proof

The kernel of (3.1) consists of pairs `(u,z)` such that `u_v=z_a` on every incidence edge. On each connected component this forces all variable and factor values to equal one common bit, and these component bits are free. Hence

\[
\dim\ker\delta=c(G).
\]

Rank-nullity gives

\[
\dim\operatorname{im}\delta=|V|+|F|-c(G).
\]

Therefore

\[
\dim\big(\mathbb F_2^E/\operatorname{im}\delta\big)
=|E|-|V|-|F|+c(G)=\beta_1(G),
\]

proving (3.2). Since the action is translation by the fixed linear subspace `im delta`, every orbit has the same cardinality `2^{|V|+|F|-c(G)}`. Dividing by the `2^{|E|}` literal vectors gives (3.3).

For any cycle, summing `delta(u,z)` around the cycle gives zero because every vertex and factor value appears twice; cycle parity is therefore gauge-invariant. Conversely, a signing with zero parity on every cycle is a coboundary: choose one basepoint in each component and integrate the edge labels along paths. Path independence is exactly the zero-cycle-parity condition. Thus cycle fluxes coordinatize the quotient. QED.

### Corollary 3.2 — the source sector is exponentially rare in the random-literal regular ensemble

For a `(d,k)=(6,3)` regular factor graph on `n` variable vertices,

\[
|E|=6n,\qquad |F|=\frac{6n}{3}=2n.
\]

Hence

\[
\boxed{\beta_1(G)=3n+c(G)}
\tag{3.4}
\]

and an iid-literal random-regular NAE-SAT instance lands in the unsigned hypergraph-colouring gauge sector with conditional probability

\[
\boxed{2^{-(3n+c(G))}\le 2^{-(3n+1)}.}
\tag{3.5}
\]

This does **not** say the unsigned sector is atypical with respect to every observable. It says only that a theorem averaged over iid literals cannot be transferred to the all-zero sector by an assertion that the two ensembles are globally gauge-equivalent or that the zero sector has non-negligible literal measure.

## 4. An exact finite counterexample: cycle flux can change satisfiability

A route obstruction is much stronger if the quotient is not merely formal. The complete `3`-uniform hypergraph on five vertices, `K_5^(3)`, is a simple `6`-regular `3`-uniform hypergraph:

\[
|V|=5,\qquad |F|=\binom53=10,\qquad |E|=30,
\]

and every vertex has degree `C(4,2)=6`.

For the all-zero literal signing, the associated NAE formula is exactly hypergraph 2-colouring. It has **no** proper 2-colouring: among five vertices one colour class has at least three vertices, and those three form a hyperedge.

Now sign each triple by negating exactly the incidence of its smallest-labelled vertex. The all-zero assignment already satisfies every clause, because each clause then sees the pattern `(1,0,0)` in its own increasing order. Exhaustive enumeration gives exactly six satisfying assignments.

The signing has odd flux around the factor-graph 4-cycle

\[
1-(012)-2-(123)-1,
\]

so it is not gauge-equivalent to the unsigned formula. Thus the cycle sector is not a redundant label: on one and the same simple `6`-regular `3`-uniform factor graph, the unsigned sector is UNSAT while an explicit nonzero-flux sector is SAT.

The exact finite checker is

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T03-45-51Z__gauge_sector_exact.py`

created in commit `50ff76678d59fc093d4446bfbdebdffb24a25b67`. Its archived output is

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T03-45-51Z__gauge_sector_exact.out`

created in commit `15413bed5a32d447779c730902f3cc172b2f8a25`. It verifies with exact `F_2` elimination and exhaustive enumeration:

- gauge-map rank `14`;
- `beta_1=16`;
- unsigned orbit size `2^14=16384` among `2^30` signings;
- `2^16=65536` gauge classes and unsigned-sector mass `1/65536`;
- odd displayed 4-cycle flux;
- zero-literal solution count `0`;
- explicit signed solution count `6`;
- terminal line `ALL_EXACT_CHECKS_PASS = True`.

This finite example is **not** evidence about the asymptotic probability `L_6`; it certifies only the global gauge-sector distinction used to reject an invalid transfer route.

## 5. B20: why the obvious BMS/tree algorithm fails as a source transfer

The same gauge calculation gives the complementary positive fact.

### Proposition 5.1 — every forest signing is gauge-trivial

If the factor graph `G` is a forest, then `beta_1(G)=0`, and every literal signing is gauge-equivalent to zero.

This is immediate from Proposition 3.1. Consequently, on any finite tree neighborhood, a signed NAE instance and an unsigned hypergraph-bicolouring instance are identical after local variable/clause gauge changes. Any gauge-invariant observable of a tree neighborhood is therefore blind to the global cycle sector.

This directly explains a danger in the run-7 BMS recovery. Nam--Sly--Sohn define random regular NAE-SAT by first choosing the regular factor graph and then drawing the edge literals iid uniform. Gu's 2026 reconstruction theorem and its BMS-channel comparison technology are also fundamentally local/tree distributional tools. On a tree, the signed and unsigned problems can be gauge-normalized to the same local object. Therefore a local BMS fixed point, contraction/non-contraction certificate, or reconstructed tree channel can be mathematically correct and still contain **zero information about which of the `2^{3n+c}` global cycle-flux sectors the finite regular instance occupies**.

The conclusion is deliberately narrow:

\[
\boxed{
\text{tree/BMS control can be a local module, but by itself cannot justify transferring}
\text{ random-literal 1RSB conclusions to the unsigned source model.}
}
\tag{5.1}
\]

This is not a claim that the BMS method is useless. It says the global finite-graph step must be source-specific.

## 6. The exact place where the large-k cluster formula averages away the source sector

This run also read the open-access Nam--Sly--Sohn 2024 paper *One-Step Replica Symmetry Breaking of Random Regular NAE-SAT II* (Commun. Math. Phys. 405, 61). Their Section 2 defines a labelled factor graph with edge literals `L_e in {0,1}` and then explicitly takes

\[
\mathbb E^{\rm lit}
\]

over iid uniform literals. In their cluster weight, the clause factor is replaced by the literal average

\[
\widehat\Phi(\sigma_{\delta a})^\lambda
:=
\mathbb E^{\rm lit}
\left[
\widehat\Phi^{\rm lit}((\sigma\oplus L)_{\delta a})^\lambda
\right].
\tag{6.1}
\]

This is exactly right for their random-literal NAE-SAT ensemble. It is not the source measure for unsigned hypergraph 2-colouring.

For the CKS source, the source-compatible finite-`L` cluster partition function must instead start from the fixed-zero-literal weight

\[
\boxed{
[w_G^{(0)}(\sigma)]^\lambda
=
\prod_{v\in V}\dot\Phi(\sigma_{\delta v})^\lambda
\prod_{a\in F}
\left[\widehat\Phi^{\rm lit}(\sigma_{\delta a})\right]^\lambda
\prod_{e\in E}\overline\Phi(\sigma_e)^\lambda,
}
\tag{6.2}
\]

with no expectation over `L` at the factor nodes. Equation (6.2) is just the NSS finite-graph formula specialized to the all-zero literal vector; no novelty is claimed.

The gauge theorem explains why replacing (6.2) by (6.1) is harmless on a tree but potentially decisive on the finite regular graph: (6.1) averages over exponentially many cycle-flux sectors, while (6.2) fixes one sector.

CKS themselves prove that the **first moments of the total number of colourings/NAE solutions** are comparable up to a constant in their setting. That fact does not imply equality of cluster-weighted second moments or the global small-subgraph/Doob correction needed for a lower bound. The finite `K_5^(3)` example shows that even satisfiability can vary between gauge sectors on a fixed factor graph.

## 7. What this does to the second recovery

Run 7 proposed:

> derive the exact finite-`k` cluster transform, then use BMS degradation/Blackwell order to enclose its infinite-dimensional message law and combine that with the random-regular cluster/SSC architecture.

This run does **not** abandon that plan; it corrects its order of operations.

A source-compatible recovery now has three modules:

1. **Local module:** derive/enclose the fixed-zero-literal finite-`k` message transform. Tree gauge equivalence means BMS technology may still be reusable here.
2. **Flux/global module:** derive the first- and second-moment/profile functionals directly for the unsigned sector (6.2), rather than importing the literal-averaged global functional. Any short-cycle correction must respect the fixed cycle-flux condition.
3. **Probability module:** prove a source-valid positive cluster count or comparable quenched statement, transfer from the configuration model to the uniformly simple hypergraph, and map every counted frozen/cluster object to an actual 2-colouring.

The immediate next mathematical target is therefore the **unsigned pair-profile functional**: write the exact finite-type second-moment exponent for two fixed-zero-literal cluster colourings in the configuration model and determine whether its independent cluster saddle can be globally certified at `(k,d)=(3,6)`. A BMS enclosure is useful only after the fixed-sector functional to which it must couple has been derived.

This is a genuine change from the prior checkpoint: the missing global ingredient is not merely “cycle fluctuations” in the usual small-subgraph-conditioning sense. There are `3n+c` independent literal gauge-flux bits in the signed model, and the unsigned source fixes all of them. The signed-to-unsigned difference is therefore **extensive**, even though every bounded tree neighborhood is locally gauge-trivial.

## 8. Outcomes of the three Section-B moves

### B1 — CHANGE THE CATEGORY

**Succeeded as a structural reduction.** Recasting edge literals as `F_2` 1-cochains turns the signed/unsigned comparison into a quotient by the bipartite cut/coboundary space. The correct global variable is cycle flux, not another scalar BP moment.

### B14 — FIND THE GROUP ACTING

**Succeeded exactly.** Variable flips plus whole-clause complementations form the gauge action (3.1). The quotient has dimension `beta_1`. At `(6,3)` this is `3n+c`, so the unsigned source is one exponentially small gauge sector of the iid-literal ensemble.

### B20 — FIND WHY THE ALGORITHM FAILS

**Succeeded in killing an invalid transfer, not in moving `L_6`.** Tree/BMS population dynamics cannot see cycle flux because every forest signing is gauge-trivial. The finite `K_5^(3)` certificate shows that global flux can nevertheless change satisfiability. A source proof must derive the unsigned global cluster/moment functional rather than merely reuse the random-literal one.

The previous run used B8/B17/B27, so this triple is not repeated.

## 9. Section-I lifecycle and next checkpoint

This execution is the first substantive execution of the **second and final** recovery chosen in the STUCK2 report. It is not a third stuck report: the recovery produced a new structural obstruction and corrected the mathematical object that the BMS enclosure must target. The frozen source metric nevertheless did not move.

If the source-facing obligation remains unchanged long enough to trigger the next Section-I stuck episode, the controlling rule allows no third recovery: HARD7-06 must then leave a handoff and rotate to a fresh eligible hard CSP target.

For the next run, do **not** produce another checker for the gauge lemma. The highest-value task is to derive the fixed-zero-literal **two-cluster/pair profile** functional from (6.2), then attack its correlated saddle globally. If that derivation collapses back to an already-known theorem or requires the literal average in an essential way, record the exact failure and prepare the mandated handoff rather than relabeling it as progress.

Suggested next, nonrepeating Section-B triple: **B11 DUALIZE** the unsigned pair-profile variational problem, **B15 BREAK THE SYMMETRY** by forcing nonzero cycle-flux comparison profiles to expose what the zero sector forbids, and **B30 LOCALIZE BY SCALE** into tree/bounded-cycle/extensive-flux contributions.

## 10. Runtime/scheduler capability honesty

The exposed scheduler control surface still provides title, prompt, schedule/timing and enablement but no model-family selector, reasoning-effort selector, or guaranteed execution duration. `GPT-6 / maximum` is therefore only a prompt request. This run actually identifies as GPT-5.6 Sol; applied reasoning level is not exposed and is reported `UNVERIFIED`.

The repository records both a historical `You cannot modify this task` result for P26 in one authorization context and a later successful P26 update from another authorized P/C context. I did not probe or modify P26 or any other schedule in this run, because HARD7-06 is explicitly forbidden to change other jobs. The lawful workaround for any task that is still denied is to use its owning/authorized task-management context or platform support; do not bypass permission checks, clone the job, or treat a repository edit as a scheduler repair.

No Gmail, Drive, workflow, public-posting, permission, shared-root, peer-report, or scheduler state was changed.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: HARD7-06
  lane: hard outside / random constraint satisfaction
  target: CKS-2024-RREG-HYPER2COL-K3
  status: PARTIAL
  source_status: OPEN under bounded 2026-09-19 literature review
  metric: L_6
  before: ">= 0"
  after: ">= 0"
  movement: false
  methods: [1, 14, 20]
  substantive_result:
    - "Exact gauge quotient of NAE literal signings has dimension beta_1(G)."
    - "For (d,k)=(6,3), iid-literal unsigned-sector mass is 2^(-(3n+c(G)))."
    - "Every forest signing is gauge-trivial, so tree/BMS recursions are sector-blind."
    - "Exact K5^(3) witness: unsigned zero-literal instance has 0 solutions, explicit odd-flux signing has 6."
    - "Source-compatible cluster recovery must use fixed-zero-literal weight, not the literal-averaged global 1RSB functional."
  exact_artifact_commit: 50ff76678d59fc093d4446bfbdebdffb24a25b67
  exact_output_commit: 15413bed5a32d447779c730902f3cc172b2f8a25
  next_obligation: "derive and globally analyze the unsigned fixed-sector two-cluster/pair profile functional; no source movement until a positive-probability configuration-to-simple witness bridge exists"
  lifecycle: "second recovery active; next triggered stuck episode requires handoff/rotation"
```
