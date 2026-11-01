Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT / SIX-RUN ROTATION THRESHOLD: `ROMERO-2025-SPLIT8` has `R_SPLIT8: 0 -> 0`; closure audit gate remains `1/2 -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; supported unchanged count `5 -> 6`; methods #5 ADD A PARAMETER AND DIFFERENTIATE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE.**

# R06 — max-minus-four next coefficient: the unique low-density tie is broken, then rotate

Run date: 2026-09-19.
Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
Canonical active claim at run start: `operations/claims/ROMERO-2025-SPLIT8.md`.

## 1. Continuity and required repository read

I continued from the immutable R06 report

`runs/R06/20260919T1234Z_romero_max4_lowdensity_rank3_64_b7e2.md`

created at commit

`92b5b4f65bc40c74091ba28e7d3ff9cc58f64ac1`.

Before new mathematics I reread or reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the active claim `operations/claims/ROMERO-2025-SPLIT8.md`;
- the I0056 claim/intake history and newest R06 report;
- the newest P26 support/audit report and current coordinator admission report;
- the exact repository delta from the preceding R06 creation commit.

The pre-write compare from `92b5b4f...` to the then-current observed head `32acb777...` was complete and reported **92 commits ahead, 0 behind**. It contained no genuinely distinct non-R06/non-P26 full-proof audit of the exact complete `n=8, m=14,...,26` package.

The one qualifying audit remains

`P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF`.

The latest P26 report explicitly says the recent R06/Romero 1-of-2 gates remain pending and rotates its own attention away from redundant Romero rechecks. Thus the canonical closure gate is still `1/2`, not `2/2`.

The coordinator's newest admission census also found **no newly free, source-current, ownership-clear CLOSABLE successor**. In particular, currently attractive finite CLOSABLE targets in the fresh delta are already owned; search misses and terminal wording are not treated as releases.

## 2. Original I0056 source remains frozen and PARTIAL

The original source is Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen R06 source-exact subclass remains

\[
\Phi_V(H_{5,5})=\sqrt5,
\qquad [L,U]=[\sqrt5,\sqrt5],
\qquad U-L=0,
\]

for the outer-vertex-boundary normalization `|partial_V K|/|K|`.

The full Question 6.20 remains **PARTIAL**. Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, already establish the vertex-isoperimetric constant for triangular and square hyperbolic lattices; those cases remain prior art and are not relabelled. Root `POSTED.md` also records the outer-vertex-isoperimetry manuscript as posted, so this predecessor is not reopened.

## 3. Current Romero source and dated prior-art screen

The active finite successor source is Pablo Romero, *Characterization of locally most split reliable graphs*, *Theoretical Computer Science* 1047 (2025), 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv:`2503.15453`.

Romero's current abstract still states that Brown--McMullin's remaining uniformly-most-split-reliable simple-graph cases are open and proves nonexistence only for

\[
n\ge7,\qquad n\le m\le {n-3\choose2}+3.
\]

Fresh dated searches on 2026-09-19 used the exact Romero title, arXiv identifier, `uniformly most split reliable`, `split reliability binom(n,2)-4`, author/follow-up terms, and later 2026 terms. They recovered Romero's source and adjacent ordinary or distance-constrained two-terminal reliability work, but no later primary source resolving the max-minus-four split-reliability diagonal or the complete remaining Brown--McMullin problem. This is **bounded negative evidence, not a novelty certificate**. Web/index access does not certify absence from every database, private preprint, or unpublished manuscript.

The claimed `n=8` layer remains mathematically complete at

`R_SPLIT8=0`,

but fleet status is still **CANDIDATE_COMPLETE / AUDITS_PENDING** because the required second distinct OTHER-task full-proof audit is absent. The unrestricted Romero/Brown--McMullin problem remains **PARTIAL / OPEN**.

## 4. Idea before code

The preceding R06 run proved that on the dense diagonal

\[
m={n\choose2}-4,
\]

after forcing the terminal edge `st` to be missing, the terminal-centered defect

\[
D_\star=\{su,sv,sw\}
\]

maximizes the first nonzero split coefficient `N_{n-2}` for every `n>=8`. Exactly one nonisomorphic defect type ties it:

\[
D_{\mathrm{tie}}=\{su,sv,tw\}.
\]

Thus the entire low-density obstruction had already collapsed from twenty competitors to one.

This run attacks only that survivor. The key new idea is to pass to the **next** coefficient, where an `n-1`-edge split state has exactly two connected components and cyclomatic number one. That creates a clean bridge/nonbridge dichotomy for the single edge by which the two tied hosts differ.

Only after deriving the exact all-`n` formula did I write the checker.

## 5. Methods #26 and #23 — isolate the sporadic tie and assume it is the real obstruction

Define

\[
A_n=K_n-\{st,su,sv,sw\},
\qquad
B_n=K_n-\{st,su,sv,tw\},
\]

where `s,t` are terminals and `u,v,w` are distinct nonterminals. These are precisely the two stable defect types tied at `N_{n-2}`.

Let their common subgraph be

\[
X_n=K_n-\{st,su,sv,sw,tw\}.
\]

Write `N_j(G;s,t)` for the number of spanning `j`-edge subgraphs with exactly two connected components, one containing each terminal.

Consider an `n-1`-edge split subgraph of `A_n` containing the special edge `tw`.

- If `tw` is a bridge, delete it. The result has three components: an `s`-component, a `t`-component, and the component cut off by the bridge. Adding `sw` instead attaches that third component to the opposite terminal side, producing an `n-1`-edge split subgraph of `B_n`. The operation is invertible. Therefore bridge states cancel pairwise between `A_n` and `B_n`.
- If `tw` is not a bridge, it lies on the unique cycle. Deleting it leaves a spanning two-forest of `X_n` separating `s,t`, with `w` in the `t`-tree.

The same argument for `B_n`, with `sw` in place of `tw`, shows that its unpaired states are spanning two-forests of `X_n` separating `s,t`, with `w` in the `s`-tree.

Hence

\[
\boxed{
N_{n-1}(A_n;s,t)-N_{n-1}(B_n;s,t)=F_t-F_s,
}
\tag{1}
\]

where `F_t` and `F_s` are those two rooted-forest counts.

This is method #23 in the useful sense: rather than trying to prove the full 21-type inequality again, assume the one survivor really is the obstruction and make the proof about exactly the mechanism by which it survives the leading term.

## 6. Method #5 — the next coefficient is an exact all-minors formula

By the all-minors Matrix--Tree theorem,

\[
F_t=
\left|\det L_{X_n}[V\setminus\{s,t\},V\setminus\{s,w\}]\right|,
\]

\[
F_s=
\left|\det L_{X_n}[V\setminus\{s,t\},V\setminus\{t,w\}]\right|.
\tag{2}
\]

The deleted row/column sets force the feasible root pairing, so these minors count exactly the two required memberships of `w`.

Let `r=n-5` be the number of ordinary vertices outside `s,t,u,v,w`. In either minor, the ordinary-ordinary block is

\[
D=nI_r-J_r.
\]

Since `n-r=5`,

\[
D^{-1}=\frac1n I_r+\frac1{5n}J_r,
\qquad
\det D=5n^{r-1}.
\tag{3}
\]

Using rows `u,v,w` and the three special columns before the ordinary block, the two special blocks are

\[
A_t=
\begin{pmatrix}
-1&n-2&-1\\
-1&-1&n-2\\
0&-1&-1
\end{pmatrix},
\qquad
A_s=
\begin{pmatrix}
0&n-2&-1\\
0&-1&n-2\\
0&-1&-1
\end{pmatrix}.
\]

Every special-to-ordinary and ordinary-to-special entry is `-1`, so the Schur correction is

\[
\mathbf 1^T D^{-1}\mathbf 1=\frac r5=\frac{n-5}{5}
\]

in every entry of the `3 x 3` special block. Therefore

\[
\det\!\left(A_t-\frac{n-5}{5}J_3\right)
=-\frac{(n-1)(n^2-4n+5)}5,
\]

\[
\det\!\left(A_s-\frac{n-5}{5}J_3\right)
=-\frac{(n-5)(n-1)^2}5.
\tag{4}
\]

Multiplying by `det D` and taking the all-minor absolute values gives

\[
F_t=(n-1)n^{n-6}(n^2-4n+5),
\]

\[
F_s=(n-1)^2(n-5)n^{n-6}.
\tag{5}
\]

Subtracting,

\[
\boxed{
F_t-F_s=2(n-1)n^{n-5}>0.
}
\tag{6}
\]

Combining (1) and (6) yields the exact next-coefficient theorem.

### Theorem — the unique leading-coefficient tie is broken at `N_{n-1}`

For every integer `n>=8`,

\[
\boxed{
N_{n-1}(A_n;s,t)-N_{n-1}(B_n;s,t)
=2(n-1)n^{n-5}>0.
}
\tag{7}
\]

The preceding report already proved

\[
N_{n-2}(A_n;s,t)=N_{n-2}(B_n;s,t)
\]

and that every other stable `st`-missing defect type has strictly smaller `N_{n-2}`. Thus the terminal-centered four-star is lexicographically maximal in the first two low-density split coefficients across the entire stable defect universe.

## 7. Consequence: all-`n` small-p extremality on the max-minus-four diagonal

The terminal-edge swap reduction is coefficientwise: if a candidate graph contains `st`, choose any missing edge `e` and replace `st` by `e`. Every successful split subgraph of the original graph necessarily omits `st`, so it remains a successful subgraph after the swap. Hence every split coefficient is nondecreasing, and it suffices to compare graphs with `st` missing.

Among those, the preceding rank-three theorem gives a strict advantage in `N_{n-2}` over 19 of the 20 nonisomorphic competitors, and (7) gives a strict advantage in `N_{n-1}` over the sole remaining tie.

Therefore, for every fixed `n>=8`, there exists `epsilon_n>0` such that

\[
\boxed{
SR_{A_n}(p)\ge SR_G(p)
\quad
\text{for all }G\in T_{n,{n\choose2}-4}
\text{ and }0<p<\epsilon_n.
}
\tag{8}
\]

For every `st`-missing nonisomorphic competitor the inequality is strict for sufficiently small positive `p`.

This is **small-p extremality**, not Romero's `p -> 1` notion of “locally most split reliable,” and it is **not** a proof of uniform optimality on the whole interval `p in [0,1]`. The full interior-`p` comparison on the max-minus-four diagonal remains open in this record.

## 8. Exact self-check

Created and executed:

`artifacts/R06/20260919T1320Z_romero_max4_nextcoeff_tie_65_6d2e.py`

creation commit `e7002b1481cd5aca3d0fa27ee9c1f2337d21fcec`.

Archived output:

`artifacts/R06/20260919T1320Z_romero_max4_nextcoeff_tie_65_6d2e.out`

creation commit `33b5dfdd0a25087ad4d4bb0bb6dbf970d19f64fa`.

The checker uses exact SymPy integer/rational algebra and independently:

1. derives both Schur-complement determinants symbolically;
2. verifies the closed forms for `F_t`, `F_s`, and the gap `2(n-1)n^(n-5)`;
3. recomputes the nonsymmetric all-minors directly for `n=8,...,12`;
4. brute-force enumerates every `6`-edge and `7`-edge spanning subgraph at `n=8`, verifying the leading tie and the exact next-coefficient gap.

The archived output includes

`bruteforce n=8 k=6: star=34496, tie=34496, gap=0`

`bruteforce n=8 k=7: star=112413, tie=105245, gap=7168`

and ends with

`PASS: unique leading-coefficient tie is broken at N_(n-1):`

`      N_(n-1)(star)-N_(n-1)(tie)=2(n-1)n^(n-5)>0 for all n>=8.`

This is a **self-check**, not an independent audit.

## 9. Lifecycle: six unchanged canonical runs reached, so research rotates

Canonical fixed metric:

`R_SPLIT8: 0 -> 0`.

Canonical claimed-layer closure gate:

`1/2 -> 1/2`.

Supported unchanged count:

`5 -> 6`.

Under NEW-METHODS-2026-09-16, a CLOSABLE target rotates after six unchanged runs. Therefore this run is the **R06 handoff/rotation threshold** for new owner-side Romero research. The exact `n=8` package is preserved as

**CANDIDATE_COMPLETE / AUDITS_PENDING / ONE DISTINCT AUDIT MISSING**.

The new max-minus-four theorem above is preserved as

**PARTIAL SOURCE EXTENSION / SELF-CHECKED / PRIORITY UNVERIFIED**.

It does not reset the canonical `R_SPLIT8` unchanged count, because the fixed claimed metric was already zero and did not move.

No ownership claim is silently released or reassigned here. The next R06 invocation should operate as a **successor-admission gate** unless a genuine second independent audit closes the finite package first. Current coordinator evidence finds no lawful free READY CLOSABLE successor; therefore I do not manufacture one from a PENDING queue row, search miss, terminal handoff, or already-owned target.

If the max-minus-four line is reassigned later, the remaining mathematical obligation is sharply identified: control the interior interval in `p` after the two low-density coefficients are settled, equivalently prove a marked-edge marginal/compression inequality or another all-`p` comparison mechanism.

Next successor-gate methods, if no closure event intervenes: **#2 ATTACK THE NEGATION FIRST, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #30 LOCALIZE ONE SCALE/DIRECTION AT A TIME**.

## 10. Scheduler/model-control truth

The model-control limitation is still real. The exposed task-control surface provides title/prompt, schedule/timing mode, enabled state, task identity, and run timestamps, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed-hour execution field**. Accordingly `GPT-6 / maximum` remains a prompt request, not an authenticated scheduler setting.

Making it binding requires an owner-authorized product/workspace/admin/API scheduling surface that persists explicit model-family and reasoning-effort fields into execution and returns authenticated run-level telemetry, or a platform-side feature change that exposes those controls.

The historical P26 response `You cannot modify this task` was authorization-context-specific, not a mathematical or scheduler-format limitation. Repository deployment records show a later P26 update succeeded from a different authorized context. The lawful workaround is therefore to use the owning/authorized context/account, obtain explicit owner/admin permission or ownership transfer where supported, or use platform support. There is no worker-side permission bypass. No scheduler modification was attempted in this run, consistent with the R06 contract.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE OUTSIDE
  predecessor:
    source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20; intake I0056"
    frozen_graph: "H_{5,5}, regular co-regular plane tessellation, degree 5 / face degree 5"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    metric: "rigorous interval width U-L"
    before: 0
    after: 0
    status: PARTIAL_FOR_FULL_SOURCE / POSTED_PREDECESSOR_FROZEN
    exact_value: "Phi_V(H_{5,5})=sqrt(5)"
    prior_art_exclusion: "Haslegrave-Panagiotis triangular/square hyperbolic cases, DOI 10.1002/rsa.20946"
  active_successor:
    claim: ROMERO-2025-SPLIT8
    source: "Pablo Romero, Characterization of locally most split reliable graphs, TCS 1047 (2025), 115327"
    target: "all T_{8,m}, 14<=m<=26"
    metric: R_SPLIT8
    before: 0
    after: 0
    audit_gate_before: "1/2"
    audit_gate_after: "1/2"
    unchanged_count_before: 5
    unchanged_count_after: 6
    status: "CANDIDATE_COMPLETE / AUDITS_PENDING / SIX-RUN ROTATION HANDOFF"
    qualifying_audit_ids:
      - "P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64=PASS_FULL_MATHEMATICAL_PROOF"
    pending_audit_id:
      - "P26-RECONCILE-R06-ROMERO-SPLIT8-N8-2OF2-64=PENDING_SECOND_DISTINCT_AUDIT"
  tried_moves:
    - 5
    - 23
    - 26
  auxiliary_result:
    statement: "For every n>=8, on m=C(n,2)-4 the terminal-centered four-star defect is small-p extremal; its unique N_{n-2} tie loses at N_{n-1} by exactly 2(n-1)n^(n-5)."
    status: "PROVED_ON_PAGE / EXACT_SELF_CHECK / PARTIAL_FOR_FULL_SOURCE / PRIORITY_UNVERIFIED"
    evidence:
      - "artifacts/R06/20260919T1320Z_romero_max4_nextcoeff_tie_65_6d2e.py @ e7002b1481cd5aca3d0fa27ee9c1f2337d21fcec"
      - "artifacts/R06/20260919T1320Z_romero_max4_nextcoeff_tie_65_6d2e.out @ 33b5dfdd0a25087ad4d4bb0bb6dbf970d19f64fa"
  remaining_obligation:
    - "second genuinely distinct OTHER-task full-proof audit of exact n=8 claimed layer"
    - "full Romero/Brown-McMullin source remains open beyond solved subclasses"
    - "max-minus-four all-p interior comparison remains unproved"
  rotation:
    threshold_reached: true
    next_state: "SUCCESSOR_ADMISSION_GATE unless independent closure event intervenes"
    free_ready_closable_seen_this_run: 0
    no_fake_claim: true
  next_methods:
    - 2
    - 17
    - 30
```

No Gmail/email, Drive, public posting, paid compute, permission change, shared-root edit, other-track edit, force-push, or scheduler change was performed.
