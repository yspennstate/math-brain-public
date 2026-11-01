Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `ROMERO-2025-SPLIT8` has `R_SPLIT8: 0 -> 0`; closure audit gate for the claimed n=8 layer remains `1/2 -> 1/2`; frozen I0056/H_{5,5} width `0 -> 0`; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.**

# R06 — Romero split reliability: the max-minus-three diagonal for every n>=6

Run date: 2026-09-19.
Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
Active canonical claim: `operations/claims/ROMERO-2025-SPLIT8.md`.

## 1. Continuity, metric, and repository state

I continued from

`runs/R06/20260919T0738Z_romero_max2_all_n_bridge_60_a71c.md`

created at commit

`6aecd527341ca0136caab388513cabe1473ce480`.

The fixed claimed finite-layer metric remains

`R_SPLIT8 = 0`,

because the exact n=8 layer `m=14,...,26` is already mathematically candidate-complete. The finite package remains **PARTIAL for the unrestricted Romero/Brown--McMullin source problem** and still has only one qualifying OTHER-task full-proof audit:

`P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF`.

Repository-wide searches still recover no genuinely distinct non-R06/non-P26 second full-proof audit of the exact n=8 package, so its closure gate remains `1/2`.

A new P26 report in the repository independently audited the previous run's all-n max-minus-two theorem:

`P26-AUDIT-R06-ROMERO-MAX2-ALLN-65 = PASS_FULL_MATHEMATICAL_PROOF / CLAIM_SCOPED_UPPER_DIAGONAL / SOURCE_PARTIAL_OPEN / SATYANARAYANA_1992_DEPENDENCY_VERIFIED / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / PRIOR_ART_EXACT_SPECIALIZATION_UNVERIFIED / PENDING_SECOND_DISTINCT_AUDIT`.

That is useful independent confirmation, but it is not the missing second audit of the n=8 finite layer and does not change `R_SPLIT8`.

Before new mathematics I reread/reconciled the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the active Romero claim, the newest own report, and current neighboring/audit evidence. The exact comparison from the preceding R06 creation commit to the then-current master was **83 commits ahead / 0 behind / complete (`too_large=null`)**. It contained the new P26 max-minus-two audit but no second distinct Romero finite-layer audit.

The original R06 predecessor remains frozen:

`Phi_V(H_{5,5}) = sqrt(5)`, interval `[sqrt(5),sqrt(5)]`, width `0`, under the outer-vertex-boundary normalization. The full Lyons--Peres Question 6.20 remains PARTIAL; Haslegrave--Panagiotis DOI `10.1002/rsa.20946` remain prior art for triangular/quadrangular cases and are not relabelled as new.

## 2. Fresh source and prior-art check

Primary source rechecked on 2026-09-19:

Pablo Romero, *Characterization of locally most split reliable graphs*, Theoretical Computer Science 1047 (2025), 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv `2503.15453`.

The current source still states that Brown--McMullin's remaining simple-graph existence/nonexistence cases are open, proves that every local optimum is split-equivalent to the diameter-terminal balloon, and proves nonexistence only for

`n>=7, n <= m <= C(n-3,2)+3`.

Thus the upper diagonal

`m = C(n,2)-3`

is source-unresolved for `n>=8`.

Fresh bounded searches included exact title/arXiv/author/follow-up queries and the phrases

- `split reliability binom(n,2)-3`;
- `uniformly most split reliable dense graph three missing edges`;
- `split reliability complete graph three edges`;
- `split reliability Birnbaum all-terminal`.

They recovered Romero 2025, Brown--McMullin 2023, ordinary two-terminal reliability papers (a different reliability notion), and classical all-terminal reliability/compression literature, but no later primary source stating the theorem below. This is bounded negative evidence only; priority for the exact split theorem remains **UNVERIFIED**.

Three classical all-terminal inputs are used explicitly and credited:

1. **Dense uniformly least reliable graph.** Petingi--Saccoman--Schoppmann (Networks 27 (1996), 125--131) characterize ULRG in the dense range. Romero's later reliability-bounds paper restates the exact dense form: if

   `e=(n-1)(n-2)/2+r`, `1<=r<n`,

   then the ULRG is `K_{n-1}` plus one extra vertex adjacent to exactly `r` vertices of the clique. At `e=C(n,2)-3`, this is exactly `K_n` with a 3-edge star deleted.

2. **Independent deletions maximize ATR.** Satyanarayana--Schoppmann--Suffel, Networks 22 (1992), 209--216, DOI `10.1002/net.3230220206`: deleting `r` independent edges from `K_n` gives strictly larger all-terminal reliability than any other graph of the same order and size, for `0<p<1`. I use only `r=3`.

3. **Compression monotonicity.** Kelmans and independently Satyanarayana--Schoppmann--Suffel proved that graph compression cannot increase all-terminal reliability. Kahl, Discrete Applied Mathematics 292 (2021), 108--116, DOI `10.1016/j.dam.2020.12.025`, gives the modern compression definition and records this monotonicity.

These are prior tools, not new claims.

## 3. Idea before code: deform the max-minus-two bridge by one missing edge

The previous run proved the whole diagonal

`m=C(n,2)-2`

by rewriting split reliability as the all-terminal Birnbaum importance of the missing terminal edge. The natural deformation is to add **one more missing edge** and ask whether the same importance comparison remains tractable.

Let

`M=C(n,2)`, `m=M-3`,

and fix terminals `s,t`. For any graph `X` in which `st` is absent, the exact bridge remains

`Rel(X+st;p) = Rel(X;p) + p SR_X^{s,t}(p)`.          (1)

Equivalently, `SR_X` is the all-terminal Birnbaum importance of the edge `st` in `X+st`.

This language exposes a finite all-terminal skeleton: once `st` is missing there are only two additional missing edges, so the entire split comparison is controlled by all-terminal reliabilities of complete graphs with two or three deleted edges.

No code was written to discover this reduction.

## 4. Method #25 — count the same thing twice: exactly seven terminal types

First use the terminal-edge swap lemma from the preceding report. If `st` is present and `e` is any missing edge, put

`G' = G-st+e`.

Conditioning on the common edge state proves

`SR_{G'}(p) >= SR_G(p)` for every `p in [0,1]`.

At density `M-3` and `n>=6`, `G'` is still connected (deleting only three edges from `K_n` cannot disconnect it), so an optimum may be assumed to have `st` missing.

Now write the other two missing edges as a two-edge set `P`. Up to relabeling nonterminals and swapping the terminals, there are exactly seven possibilities. I count them in two equivalent ways.

### Direct missing-edge count

With `st` already absent, the two edges of `P` are either adjacent or independent, and their incidences with `s,t` give exactly:

- **A:** `P={su,sv}`; total missing graph is `K_{1,3}` (a 3-star centered at `s`);
- **B:** `P={su,tu}`; total missing graph is `K_3`;
- **C:** `P={su,tv}`, `u!=v`; total missing graph is `P_4`, while `P` is independent;
- **D:** `P={su,uv}`; total missing graph is `P_4`, while `P` is adjacent;
- **E:** `P={su,vw}`; total missing graph is `P_3 union K_2`, while `P` is independent;
- **F:** `P={uv,uw}`; total missing graph is `P_3 union K_2`, while `P` is adjacent;
- **G:** `P={uv,wx}`; total missing graph is `3K_2`.

All displayed nonterminals are distinct unless adjacency is explicitly shown.

### Birnbaum-host count

Adding `st` leaves `K_n-P`. A two-edge deletion set in a complete graph is either adjacent or independent. In the adjacent host there are four orbits for the distinguished edge `st`; in the independent host there are three. Thus the same universe is `4+3=7`.

The two counts agree and no sampled graph universe is being substituted for the source class.

## 5. All-terminal notation for the seven types

Write, as functions of the common edge-operating probability `p`,

- `a = Rel(K_n - P_2^adj)`;
- `i = Rel(K_n - 2K_2)`;
- `S = Rel(K_n - K_{1,3})`;
- `T = Rel(K_n - K_3)`;
- `P = Rel(K_n - P_4)`;
- `Q = Rel(K_n - (P_3 union K_2))`;
- `J = Rel(K_n - 3K_2)`.

Applying (1) gives, for `0<p<1`,

`p SR_A = a-S`,
`p SR_B = a-T`,
`p SR_C = i-P`,
`p SR_D = a-P`,
`p SR_E = i-Q`,
`p SR_F = a-Q`,
`p SR_G = i-J`.                                      (2)

This is the second payoff of method #25: seven split-reliability functions collapse to seven differences of only **two** two-deletion ATR values and **five** three-deletion ATR values.

## 6. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: the exact switch identity

The only obstacle in (2) is that the independent two-edge host has higher all-terminal reliability than the adjacent two-edge host. The required correction is an exact identity.

### Lemma (two-edge switch identity)

Let `q=1-p`. Then

`i-a = q(P-S)`.                                      (3)

### Proof

Label four vertices `0,1,2,3`. Set

`A_2 = K_n-{01,02}`  (adjacent two-edge deletion),

`I_2 = K_n-{01,23}`  (independent two-edge deletion).

The edge `03` is present in both. Condition its random state.

If `03` is operational, contract it. The contracted multigraphs `A_2/03` and `I_2/03` are isomorphic: in each, the merged vertex has one surviving edge to vertex `1`, one surviving edge to vertex `2`, and identical parallel pairs to every other vertex. Hence the conditional connectedness probabilities agree and contribute zero to `Rel(I_2)-Rel(A_2)`.

If `03` fails, then

`A_2-03 = K_n-{01,02,03}`,

a three-star deletion, while

`I_2-03 = K_n-{01,23,03}`

has missing graph a four-vertex path and is isomorphic to `K_n-P_4`.

The failure branch has probability `q`, proving (3). `square`

This identity is exact for every `n` for which the named vertices exist; it is not asymptotic.

## 7. Three classical ATR orderings

For `n>=6` the following inequalities hold for every `p in [0,1]`.

### 7.1 The three-star deletion is uniformly least reliable

At `e=M-3`, the dense Petingi--Saccoman--Schoppmann characterization applies because

`M-3 = (n-1)(n-2)/2 + (n-4)`.

Their ULRG is `K_{n-1}` plus one vertex of degree `n-4`, which is exactly `K_n` with three edges incident to one vertex deleted. Therefore

`S <= T,  S <= P,  S <= Q,  S <= J`.                 (4)

### 7.2 The `P_3 union K_2` deletion is at least as reliable as the `P_4` deletion

Take

`Y = K_n-{01,02,34}`

and compress `Y` from vertex `1` to vertex `4`. Since

`N_Y(1) - N_Y(4) - {4} = {3}`,

the compression removes the present edge `13` and inserts the missing edge `43`. The result is

`K_n-{01,02,13}`,

whose missing graph is `P_4`.

Compression cannot increase all-terminal reliability, so

`P <= Q`.                                             (5)

### 7.3 Three independent deletions maximize reliability

The `r=3` Satyanarayana--Schoppmann--Suffel theorem gives

`P <= J`                                              (6)

(and indeed `J` is strictly above any nonmatching deletion pattern for `0<p<1`).

## 8. The max-minus-three theorem

### Theorem

For every `n>=6`, let `M=C(n,2)`. In the class `T_{n,M-3}` of connected simple two-terminal graphs, the diameter-terminal graph

`A_n = K_n-{st,su,sv}`

with distinct nonterminals `u,v` is uniformly most split reliable:

`SR_{A_n}(p) >= SR_G(p)`

for every `G in T_{n,M-3}` and every `p in [0,1]`.

For the Romero/Brown--McMullin open source, the new content begins at every `n>=8`.

### Proof

By the terminal-edge swap reduction, it is enough to compare A with the seven terminal-missing types in Section 4.

For the three types whose two-edge host is adjacent, equations (2) and (4) give immediately

`p(SR_A-SR_B) = T-S >=0`,

`p(SR_A-SR_D) = P-S >=0`,

`p(SR_A-SR_F) = Q-S >=0`.                            (7)

For type C, use the switch identity (3):

`p(SR_A-SR_C)`
`= (a-S)-(i-P)`
`= (P-S)-(i-a)`
`= (P-S)-q(P-S)`
`= p(P-S) >=0`.                                      (8)

Thus `SR_A-SR_C=P-S>=0` for `p>0`.

For type E,

`p(SR_A-SR_E)`
`= (Q-S)-(i-a)`
`= (Q-S)-q(P-S)`
`= (Q-P)+p(P-S) >=0`,                                (9)

using (4) and (5).

For type G,

`p(SR_A-SR_G)`
`= (J-S)-(i-a)`
`= (J-P)+p(P-S) >=0`,                                (10)

using (4) and (6).

Therefore A weakly dominates every terminal-missing type for every `0<p<1`, and the initial terminal-edge swap extends this to every graph in `T_{n,M-3}`.

At `p=0` and `p=1`, all these connected `n>=6` graphs have split reliability zero, so the weak inequality extends to the closed interval `[0,1]`. `square`

### Source consequence

Combining this theorem with the previous run gives two complete infinite positive diagonals in the source-open simple-graph region:

`m=C(n,2)-2` and `m=C(n,2)-3`, for every `n>=8`.

The unrestricted Romero/Brown--McMullin problem remains **PARTIAL / OPEN**.

## 9. Method #18 — SAY IT IN ANOTHER LANGUAGE: Birnbaum importance was the missing coordinate

The key conceptual change is that split reliability of `G` with `st` absent is exactly the all-terminal Birnbaum importance of `st` in `G+st`:

`SR_G^{s,t}(p) = [Rel(G+st;p)-Rel(G;p)]/p`.

For max-minus-three, the seven graph types are therefore not seven unrelated split polynomials. They are seven **marginal all-terminal reliability losses** produced by deleting the distinguished edge `st` from a host with two missing edges.

In this coordinate system:

- Petingi's dense ULRG theorem controls the three-edge lower endpoint;
- the Satyanarayana--Schoppmann--Suffel matching theorem controls the upper endpoint;
- compression orders the single intermediate pair that is needed;
- the switch identity (3) exactly accounts for the change from an adjacent to an independent two-edge host.

That combination is what closes the entire diagonal. The earlier finite n=8 coefficient enumeration was not needed for this theorem.

## 10. Exactness / audit status

There is **no essential finite computational core** in the theorem. The proof is a universal graph-type classification, one exact conditioning identity, one explicit compression, and cited all-terminal extremal theorems. I therefore did not manufacture a sampled checker and do not use the existing n=8 enumeration as proof of the all-n statement.

Current status:

- canonical fixed n=8 layer: `PROVED_CANDIDATE_LAYER / SOURCE_PARTIAL_OPEN / AUDIT_GATE_1_OF_2`;
- all-n max-minus-two auxiliary theorem: `PROVED_CANDIDATE / P26_AUDIT_PASS / SECOND_DISTINCT_AUDIT_MISSING`;
- all-n max-minus-three theorem in this report: `PROVED_CANDIDATE / SOURCE_PARTIAL_OPEN / AUDITS_0_OF_2 / PRIORITY_UNVERIFIED`.

Nothing is called fleet-closed here. The next independent audit must verify, in particular, the seven-type exhaustion, identity (3), the direction of compression in (5), and the precise dense ULRG specialization in (4).

## 11. Method outcomes and next route

**#6 DEFORM TO A POINT YOU CAN SOLVE — SUCCESS.** Adding one missing edge to the previous `M-2` theorem remains tractable and yields the full `M-3` diagonal.

**#18 SAY IT IN ANOTHER LANGUAGE — SUCCESS.** Birnbaum importance turns the split problem into marginal all-terminal reliability and reveals the relevant classical machinery.

**#25 COUNT THE SAME THING TWICE — SUCCESS.** Direct terminal-incidence classification and host-orbit classification independently give the same seven cases; the bridge then collapses them to two two-edge and five three-edge ATR values.

The next nonrepeating route, if no second audit lands first, should test the `M-4` diagonal without assuming the same argument automatically generalizes. A suitable next triple is **#5 ADD A PARAMETER**, **#12 FIND WHAT IS CONSERVED**, **#27 SWAP THE QUANTIFIERS**. The concrete obstruction is whether the all-terminal marginal loss

`Rel(K_n-P)-Rel(K_n-(P union {st}))`

is maximized when `P` is a star of size three at `s`; the `M-3` proof shows exactly which discrete-convexity statement would be needed rather than merely another finite enumeration.

## 12. Model / scheduler-control truth

Actual runtime available to this report is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The current operative implementation manifest still records that the scheduling surface exposes task identity/title, prompt, schedule/start configuration, timing mode and enabled state, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution control**. A real fix requires platform/backend fields for model and effort plus trustworthy per-run attestation.

The historical P26 update that returned `You cannot modify this task` remains an authorization-context boundary. The lawful remedy is the task's owning/authorized workspace/API/admin context, authorized ownership repair/transfer, or platform support for that same task — not cloning the task, substituting identity, or bypassing permissions. No scheduler or permission mutation was attempted in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  source: "Pablo Romero, Characterization of locally most split reliable graphs, TCS 1047 (2025), 115327"
  canonical_claim: ROMERO-2025-SPLIT8
  metric_name: "R_SPLIT8 = number of unresolved m in the claimed n=8 first unresolved layer"
  metric_before: 0
  metric_after: 0
  movement: NO_FIXED_METRIC_MOVEMENT
  unchanged_count_before: 1
  unchanged_count_after: 2
  canonical_status: "PROVED_CANDIDATE_LAYER / SOURCE_PARTIAL_OPEN / AUDIT_GATE_1_OF_2"
  tried_moves: [6, 18, 25]
  predecessor_report: "runs/R06/20260919T0738Z_romero_max2_all_n_bridge_60_a71c.md"
  predecessor_commit: "6aecd527341ca0136caab388513cabe1473ce480"
  repository_compare_ahead_by: 83
  repository_compare_behind_by: 0
  repository_compare_complete: true
  audit_ids:
    - "P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64_PASS_FULL_MATHEMATICAL_PROOF"
    - "SECOND_DISTINCT_N8_AUDIT_MISSING"
    - "P26-AUDIT-R06-ROMERO-MAX2-ALLN-65_PASS_FULL_MATHEMATICAL_PROOF"
  new_source_extension:
    statement: "For every n>=6, K_n-{st,su,sv} is uniformly most split reliable in T_{n,C(n,2)-3}."
    source_new_content_begins: "n>=8"
    proof_type: "analytic Birnbaum/all-terminal bridge; no essential finite core"
    audits: "0/2"
    priority: UNVERIFIED
  remaining_obligation: "obtain a second distinct audit for the canonical n=8 package; audit the new max-minus-three theorem; continue source-level progress without declaring the unrestricted problem solved"
  frozen_predecessor_I0056:
    graph_class: "regular co-regular plane tessellation H_{5,5}"
    normalization: "outer vertex boundary"
    interval: "[sqrt(5),sqrt(5)]"
    width_before: 0
    width_after: 0
    full_source_status: PARTIAL
  shared_root_edits: none
  peer_edits: none
  scheduler_changes: none
```

End of immutable R06 run report.