Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. ADMISSION HOLD / SOURCE METRIC UNMEASURED: `UNMEASURED -> UNMEASURED`; methods actually tried: B2, B11, B30.**

# P13 outside-successor admission screen — P0219 exact routing-tax dual and finite obstruction

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.

Status entering: **SUCCESSOR_ADMISSION_HOLD**.  
Status leaving: **SUCCESSOR_ADMISSION_HOLD**.  
Successor source metric: **UNMEASURED**.  
Successor unchanged/stuck counter: **NOT_STARTED**.

This run does **not** admit P0219, does **not** create `operations/claims/P0219.md`, does **not** reopen C0021 or I0051, and does **not** touch peer-owned I0054. The mathematical work below is an admission-screen result: it settles one tempting exact-model identification negatively and gives an exact variational representation of Aldous's finite routing functional, but it does not prove the source asymptotic.

---

## 1. Continuity, ownership, and live admission state

The controlling P13 predecessor is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T02-07-41Z__successor-admission-hold-p0219-uniformity-gate.md`

created at commit `6cf6665e1f80679d7f65d825867dfab48d3c8f0d`. That report preserved the terminal six-run handoff of C0021 and left P13 in successor-admission hold with metric UNMEASURED. I preserve that state.

I reread/recovered the owner directive at anchor commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the newest P13 report, the current admission/ownership surfaces, the relevant P0219 campaign/intake/attempt continuity, and neighboring successor reports. Large append-only JSONLs are not represented as having been visually reread byte-for-byte; candidate-specific current state is recovered from their indexed/current mirrors and exact repository deltas.

### Mandatory first lead I0054

I0054 remains an active R11 peer claim. Fresh R11 commit `96ef36bc425c6882298efaa476adc1b496ac316a` at 2026-09-19T02:49:01Z adds `runs/R11/2026-09-19T02-40-00Z_i0054-noisy-affine-u037-c058-a4d7.md` and moves R11's own frozen obligation metric `57 -> 58`. This is active research, not an orphaned claim. P13 therefore did not create, overwrite, or shadow I0054.

### Current free-CLOSABLE gate

The latest coordinator immutable status available before this write is `operations/task_health/runs/2026-09-19T025400Z/status.md`, creation commit `e79e542fe87aac08c62a5aff1895f88e4559ad46`. It again records `E_READY_CLOSABLE: 0 -> 0`: no genuinely unassigned, source-current, lifecycle-eligible CLOSABLE successor crossed the full gate at that frozen snapshot.

An exact compare from the P13 predecessor commit to prewrite master `cc4f2b2c4e892856686de709d2247831fda78282` was 105 commits ahead / 0 behind. In that material interval there was no root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, intake-source-ledger, or canonical-claim release mutation relevant to P13 admission. A later concurrent repository event at 2026-09-19T03:21:44Z created `operations/claims/P0169.md` for **R7-02** as CLOSABLE OUTSIDE; it is therefore already exclusively owned and is not P13 inventory. The interval also contained new substantive neighboring reports, including the R01/R06 P0219 screens described next.

---

## 2. P0219 source and fresh prior-art state

The strongest unclaimed replenishment lead remains **P0219 — High-density oriented percolation flow asymptotics**, from David Aldous, *A discrete Hammersley process as an extreme case of oriented percolation flows*.

The maintained source page was reachable on 2026-09-19:

`https://www.stat.berkeley.edu/~aldous/Research/OP/hammersley_flow.html`

The source defines the directed square grid with up/right edges independently open with probability `p`, lets `V(n,p)` be the maximum number of edge-disjoint open paths from the left/bottom source boundary to the top/right sink boundary, and states

\[
\frac{V(n,p)}{2n}\longrightarrow v(p)\qquad\text{in }L^1.
\]

Writing `U(n,p)` for the minimum number of edge-disjoint source-to-sink paths that cover all closed edges, Aldous explains that, up to negligible boundary normalization terms,

\[
1-v(p)=\lim_{n\to\infty}\frac{U(n,p)}{2n},
\]

and conjectures

\[
\boxed{1-v(p)\sim\sqrt{2(1-p)}\qquad(p\uparrow1).}
\]

The source itself says the difficulty is the interchange between the infinite-volume limit and the rare-defect/high-density limit.

### New neighboring prior art recovered since the last P13 screen

R01's report `runs/R01/20260919T0216Z_p0219_seppalainen_bridge_screen_6_20_29_c8e5f1a3.md` identified Timo Seppäläinen, *Increasing sequences of independent points on the planar lattice*, Ann. Appl. Probab. 7 (1997), 886--898, DOI `10.1214/aoap/1043862416`.

For iid Bernoulli marked lattice sites of density `r`, the exact diagonal shape in that paper reduces in the interior regime to

\[
\Psi_r(1,1)=\frac{2\sqrt r}{1+\sqrt r}=2\sqrt r+O(r).
\]

R01 therefore separated the P0219 heuristic into an independent Bernoulli-poset width part and a possible **routing tax** caused by requiring the abstract chains to be realized simultaneously by edge-disjoint grid paths. R06 subsequently retained P0219 as `PENDING_NOT_READY`: the exact relation between Aldous's two-orientation edge model and the solved Bernoulli Hammersley/LPP models still had to be settled.

This run resolves one part of that gate exactly: **Aldous's finite path-cover functional is not equal to the obvious reachability-poset width.** The routing tax can already be strictly positive on a `4 x 4` grid.

Fresh bounded public queries on 2026-09-19 included the exact Aldous title, the exact formula `1-v(p) ~ sqrt(2(1-p))`, Seppäläinen 1997, `oriented percolation flows edge-disjoint Hammersley`, `routing tax Hammersley path cover edge-disjoint Bernoulli`, and strict/weak Bernoulli Hammersley variants. The maintained Aldous source and Seppäläinen 1997 were recovered. I did not recover a checked later primary paper that proves the P0219 asymptotic or explicitly identifies Aldous's edge-disjoint cover with Seppäläinen's solved model. This is bounded negative evidence only, not a worldwide openness or novelty certificate. No source-access failure occurred in this run.

---

## 3. Exact finite setup

Let \(V_n=\{0,\ldots,n-1\}^2\), and let `E_n` contain every directed unit edge pointing right or up. Let `S_n` and `T_n` be exactly Aldous's source and sink boundary sets.

For a deterministic closed-edge set \(C\subseteq E_n\), define \(U_n(C)\) to be the minimum number of pairwise edge-disjoint directed `S_n`-to-`T_n` paths whose union contains every edge of \(C\).

For \(A\subseteq V_n\), write

\[
\delta^+(A)=\{e=(x,y)\in E_n:x\in A,\ y\notin A\},\qquad
\delta^-(A)=\{e=(x,y)\in E_n:x\notin A,\ y\in A\}.
\]

Put the closed edges into the reachability poset: for distinct directed edges \(e,f\), let \(e\prec f\) iff `head(e) <= tail(f)` coordinatewise. Let \(W_n(C)\) be the width of this finite poset, equivalently the minimum number of abstract chains covering \(C\).

The R01 screen established the deterministic inequality \(W_n(C)\le U_n(C)\). The next two sections identify both sides as cut optimizations and isolate their difference.

---

## 4. B11 — exact lower-bound-circulation dual for \(U_n(C)\)

### Theorem 4.1 — exact finite routing dual

For every `n` and every deterministic closed-edge set \(C\subseteq E_n\),

\[
\boxed{U_n(C)=\max_{A\subseteq V_n}\left(|C\cap\delta^+(A)|-|\delta^-(A)|\right).}
\tag{4.1}
\]

The empty set makes the right side nonnegative. This is an application of standard integral lower-bound circulation duality; I make no novelty claim for Hoffman circulation or min-flow duality itself.

### Proof

Suppose \(P_1,\ldots,P_k\) are pairwise edge-disjoint source-to-sink paths covering \(C\), and let \(f(e)\in\{0,1\}\) indicate whether their union uses edge \(e\). Every closed edge leaving \(A\) must be used, so

\[
|C\cap\delta^+(A)|\le f(\delta^+(A)).
\]

Edge-disjointness gives \(f(\delta^-(A))\le|\delta^-(A)|\). For a single path \(P\),

\[
1_P(\delta^+(A))-1_P(\delta^-(A))
=1_{\{\operatorname{start}(P)\in A\}}-1_{\{\operatorname{end}(P)\in A\}}\le1.
\]

Summing over the \(k\) paths yields

\[
|C\cap\delta^+(A)|-|\delta^-(A)|\le k.
\]

Thus, with

\[
K(C)=\max_A\bigl(|C\cap\delta^+(A)|-|\delta^-(A)|\bigr),
\]

we have \(K(C)\le U_n(C)\).

For the reverse inequality, add a super-source \(s\) and super-sink \(t\). Add arcs \(s\to x\) for every \(x\in S_n\), each with lower bound `0` and capacity `2`; add arcs \(y\to t\) for every \(y\in T_n\), also with lower bound `0` and capacity `2`. Give every grid edge capacity `1` and lower bound \(\ell(e)=1_C(e)\). Finally add a return arc \(t\to s\) with lower and upper bound both equal to an integer \(k\).

An integral feasible circulation in this augmented graph is equivalent, after deleting the return and super-boundary arcs, to an integral source-to-sink flow of value \(k\) on the directed grid that uses every closed edge. Since the grid is acyclic and every grid edge has capacity one, that flow decomposes into \(k\) pairwise edge-disjoint source-to-sink paths covering \(C\).

Use the integral lower-bound circulation criterion

\[
\ell(\delta^-(X))\le u(\delta^+(X))\qquad\text{for every vertex set }X.
\tag{4.2}
\]

For completeness, (4.2) follows by subtracting lower bounds, attaching the usual super-source and super-sink to the resulting node imbalances, and applying max-flow/min-cut; integer bounds give an integer feasible circulation.

There is a feasible circulation for \(k_0=2n-2\): set every grid edge to flow one. Its divergence is `+2` at `(0,0)`, `+1` at each other allowed left/bottom source, `-2` at `(n-1,n-1)`, `-1` at each other allowed top/right sink, and zero elsewhere. Hence boundary arcs of capacity two route this full-grid unit flow. In particular all circulation inequalities hold at \(k_0\), and the already proved lower bound gives \(K(C)\le k_0\).

Reduce the return-arc value from \(k_0\) to \(K(C)\). If \(s,t\) are both in \(X\) or both outside, (4.2) is independent of \(k\). If \(s\in X,t\notin X\), reducing \(k\) only decreases the lower-bound side and makes the inequality easier. The only harder case is \(t\in X,s\notin X\). Put

\[
A=V_n\setminus(X\cap V_n).
\]

Then the circulation inequality is exactly

\[
|C\cap\delta^+(A)|\le|\delta^-(A)|+k,
\]

which holds for \(k=K(C)\) by definition. Therefore all lower-bound circulation inequalities hold at \(k=K(C)\). An integral circulation exists, so \(U_n(C)\le K(C)\). Together with the first inequality, this proves (4.1). \(\square\)

Since \(|C\cap\delta^+(A)|=|\delta^+(A)|-|C^c\cap\delta^+(A)|\), the theorem also gives

\[
\boxed{U_n(C)=\max_A\left[\operatorname{div}(A)-|C^c\cap\delta^+(A)|\right],}
\tag{4.3}
\]

where \(\operatorname{div}(A)=|\delta^+(A)|-|\delta^-(A)|\). Thus positive deterministic divergence lives on the left/bottom source boundary and open outward edges are the cut penalty.

---

## 5. B30 — Hammersley width is exactly the downset-restricted dual

Call \(A\subseteq V_n\) a coordinate downset if `(x,y) in A` and `x'<=x,y'<=y` imply `(x',y') in A`. Such an \(A\) has \(\delta^-(A)=\varnothing\).

### Theorem 5.1

For every \(C\subseteq E_n\),

\[
\boxed{W_n(C)=\max_{A\ \mathrm{downset}}|C\cap\delta^+(A)|.}
\tag{5.1}
\]

### Proof

For a downset \(A\), the crossing edges \(\delta^+(A)\) form an antichain. If \(e,f\in\delta^+(A)\) and \(e\prec f\), then `head(e)<=tail(f)`. Since `tail(f)` is in the downset, `head(e)` would also lie in \(A\), contradicting that \(e\) leaves \(A\). Hence every downset crossing contains at most \(W_n(C)\) closed edges.

Conversely, let \(F\subseteq C\) be an antichain and let \(A\) be the coordinate downset generated by the tails of edges in \(F\). Every tail lies in \(A\). If the head of some \(f\in F\) also lay in \(A\), then `head(f)<=tail(g)` for some \(g\in F\), giving \(f\prec g\), contradiction. Thus every edge of \(F\) crosses out of \(A\). Taking a maximum antichain proves (5.1). \(\square\)

Combining Theorems 4.1 and 5.1 gives the exact routing-tax identity

\[
\boxed{
U_n(C)-W_n(C)=
\max_{A\subseteq V_n}\left(|C\cap\delta^+(A)|-|\delta^-(A)|\right)
-
\max_{A\ \mathrm{downset}}|C\cap\delta^+(A)|.
}
\tag{5.2}
\]

The Hammersley width controls monotone/downset cuts. Aldous's edge-disjoint routing functional optimizes over all cuts and charges one deterministic unit per incoming/backward cut edge. The source-level bridge therefore needs a random-cut stability theorem: for rare iid closed edges of density \(q=1-p\), the non-downset advantage must be shown to be \(o(n\sqrt q)\) in the source sequential limit, while the two-orientation downset width must separately be matched to the correct Bernoulli Hammersley model.

---

## 6. B2 — exact counterexample to \(U=W\)

The strongest tempting negation after the Seppäläinen bridge was that the routing tax might be identically zero. It is false.

Take \(n=4\) and close exactly

\[
e_0:(0,0)\to(1,0),\quad
e_2:(0,1)\to(1,1),\quad
e_{11}:(1,2)\to(2,2),\quad
e_{12}:(1,2)\to(1,3).
\tag{6.1}
\]

### Proposition 6.1

For \(C=\{e_0,e_2,e_{11},e_{12}\}\),

\[
\boxed{W_4(C)=2,\qquad U_4(C)=3.}
\tag{6.2}
\]

### Proof

There is a two-chain cover `e0<e11`, `e2<e12`, while `e0,e2` are incomparable, so \(W=2\).

For the routing lower bound take

\[
A=\{(0,0),(0,1),(0,2),(1,2)\}.
\]

All four closed edges leave \(A\), while the only grid edge entering \(A\) is `(1,1)->(1,2)`. Theorem 4.1 therefore gives \(U\ge4-1=3\). Equivalently, this is a direct cut certificate: four compulsory used exits minus at most one usable incoming edge force at least three paths.

Three pairwise edge-disjoint covering paths are

\[
(0,0)\to(1,0)\to(1,1)\to(1,2)\to(2,2)\to(2,3),
\]

\[
(0,1)\to(1,1)\to(2,1)\to(2,2)\to(3,2),
\]

and

\[
(0,2)\to(1,2)\to(1,3).
\]

Thus \(U\le3\), proving (6.2). \(\square\)

Geometrically, Dilworth can pair either lower edge with either upper edge, but the two upper closed edges share tail `(1,2)`. Realizing both abstract chains simultaneously requires two distinct incoming channels into `(1,2)`, and the lower predecessor geometry prevents a two-path realization. This is the connector conflict suspected in the preceding R01 screen.

---

## 7. Executed exact finite self-check

The checker

`proofnet24/P13-outside-successor/artifacts/2026-09-19/p0219_routing_tax_counterexample_check.py`

was created at commit `a67805ea67fa7f905e78f8aeb2c67dce5127ed4c` and read back there; blob `289373bb9a800569544e0cfa9a86129817e457c4`.

Its archived output

`proofnet24/P13-outside-successor/artifacts/2026-09-19/p0219_routing_tax_counterexample_check.out`

was created at commit `ebbaa2945bf1e5952ce6a8697245e321ed0dcfb5` and read back there; blob `26409aa0a0bdfa0aeb88be07dabd6a09ce1cfb25`.

The executed integer/bit-mask self-check verifies the explicit four-edge set, \(W=2\), the cut certificate `4-1=3`, three pairwise edge-disjoint covering paths and hence \(U=3\), arbitrary-set dual value `3`, downset-restricted value `2`, exhaustive agreement of the dual theorem with an independent brute-force path-family enumeration for all closed-edge sets on `n=2` (`16`) and `n=3` (`4096`), and exhaustive `n=4` verification that every closed-edge set of size at most three (`2325` sets) has zero routing tax. It ends

`ALL_EXACT_P0219_ROUTING_TAX_CHECKS_PASS`.

This is a **P13 self-check**, not an independent audit. The finite minimality statement is deliberately scoped only to the `n=4` grid; no global minimality over larger grids is claimed.

---

## 8. Mathematical consequence and remaining blocker

The Seppäläinen bridge is now structurally exact enough to separate the residual:

1. \(W_n(C)\) is exactly the downset/monotone-cut width.
2. \(U_n(C)\) is exactly the unrestricted penalized-cut optimum.
3. The difference is genuinely nonzero in finite volume.
4. Hence P0219 cannot be solved by simply identifying Aldous's `U` with standard Bernoulli Hammersley width and citing the solved shape theorem.
5. The remaining asymptotic task is a random-cut stability estimate showing non-downset/backtracking advantages are \(o(n\sqrt q)\), together with the periodic two-orientation width identification.

A natural next route, only if P0219 is formally promoted and assigned, is a contour expansion of (5.2): every backward dual step costs one deterministic unit, while gains require rare closed outward edges. The exact first local positive-routing-tax pattern is now known. What is missing is a uniform theorem showing that profitable backtracking excursions along an optimizing interface have density \(o(\sqrt q)\).

This run does **not** prove `1-v(1-q) ~ sqrt(2q)`, does not prove the routing-tax bound, does not justify exchange of limits, and does not certify publication novelty.

P0219 therefore remains **PENDING_NOT_READY** under current fleet continuity. No source-faithful successor metric is frozen; it remains **UNMEASURED**, and no source-level stagnation counter starts.

---

## 9. Method accounting

**B2 — ATTACK THE NEGATION FIRST.** Attempted exact equality `U=W`; failed via the certified `n=4` counterexample with `U=3,W=2`. This prevents a false direct reduction to known Hammersley width.

**B11 — DUALIZE.** Succeeded: Theorem 4.1 gives the exact penalized-cut formula for `U`.

**B30 — DO ONE SCALE / ONE DIRECTION AT A TIME.** Succeeded structurally: Theorem 5.1 identifies the monotone/downset subproblem exactly as `W`, isolating the non-downset advantage as the only routing residual. It does not yet give source movement.

This triple differs from P13's preceding `B17/B22/B25` screen.

---

## 10. Admission decision

**Decision: remain in `SUCCESSOR_ADMISSION_HOLD`.**

I do not promote P0219 by fiat. The new mathematics improves its candidacy but also proves the naive exact identification false. The remaining random non-downset-cut estimate is a genuine asymptotic theorem, and no unowned READY CLOSABLE source has been released to P13. The later P0169 CLOSABLE admission is already owned by R7-02.

A lawful future P0219 admission still requires current source/literature compatibility, exclusive READY ownership clearance, a defensible CLOSABLE classification, one frozen source-faithful metric initialized from certified information rather than a fictitious zero, and a plan to prove the `o(n sqrt(q))` non-downset advantage or an equivalent source-level statement.

No email/Gmail, Drive action, public post, paid compute, credential/permission change, force-push, workflow execution, peer-file edit, shared-root-ledger overwrite, or schedule modification was performed.

---

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  own_root: proofnet24/P13-outside-successor
  state_before: SUCCESSOR_ADMISSION_HOLD
  state_after: SUCCESSOR_ADMISSION_HOLD
  rotated_from: C0021
  prior_target_status: OPEN_PARTIAL_TERMINAL_HANDOFF
  retired_target_I0051: PRESERVED_RETIRED
  first_lead_I0054:
    disposition: OCCUPIED_ACTIVE_R11
    newest_seen_commit: 96ef36bc425c6882298efaa476adc1b496ac316a
    peer_metric_seen: "57 -> 58"
  newly_seen_owned_closable:
    id: P0169
    owner: R7-02
    disposition: NOT_P13_INVENTORY
  claim: null
  category: CLOSABLE_OUTSIDE_ADMISSION_SCREEN
  metric_name: UNMEASURED
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  source_metric_movement: false
  successor_unchanged_runs: NOT_STARTED
  methods: [2, 11, 30]
  coordinator_ready_closable_metric_at_latest_frozen_status: "0 -> 0"
  replenishment_lead:
    id: P0219
    lifecycle: PENDING_NOT_READY
    same_id_claim: ABSENT
    source_endpoint: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
    new_results:
      exact_routing_dual: "U_n(C)=max_A(|C∩delta+(A)|-|delta-(A)|)"
      downset_width_dual: "W_n(C)=max_downset_A |C∩delta+(A)|"
      finite_counterexample:
        n: 4
        closed_edge_indices: [0, 2, 11, 12]
        W: 2
        U: 3
        routing_tax: 1
      self_check:
        n2_all_closed_sets: PASS_16
        n3_all_closed_sets: PASS_4096
        n4_closed_sets_size_le_3_zero_tax: PASS_2325
    admission_blocker: >-
      Exact identification U=W is refuted. A source proof now needs a
      uniform rare-defect estimate showing the non-downset cut advantage
      is o(n sqrt(q)) in the source sequential limit, plus the two-orientation
      Bernoulli-width identification/current prior-art and lifecycle gate.
      No READY promotion is inferred.
  artifacts:
    checker_commit: a67805ea67fa7f905e78f8aeb2c67dce5127ed4c
    checker_blob: 289373bb9a800569544e0cfa9a86129817e457c4
    output_commit: ebbaa2945bf1e5952ce6a8697245e321ed0dcfb5
    output_blob: 26409aa0a0bdfa0aeb88be07dabd6a09ce1cfb25
  notes: >-
    Mathematical screening advanced materially but no successor was admitted,
    so the successor source metric remains UNMEASURED and no stagnation
    counter starts. C0021 and I0051 remain non-restartable by P13 under
    current owner rules.
```
