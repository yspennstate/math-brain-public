Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `ROMERO-2025-SPLIT8` has `R_SPLIT8: 0 -> 0`; closure audit gate remains `1/2 -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; supported unchanged count `4 -> 5`; methods #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS.**

# R06 — max-minus-four: uniform low-density extremality by a rank-three forest determinant

Run date: 2026-09-19.
Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
Active canonical successor claim: `operations/claims/ROMERO-2025-SPLIT8.md`.

## 1. Continuity and required repository read

I continued from the immutable STUCK1 report

`runs/R06/20260919T1126Z_romero_stuck1_marked_importance_63_c2f7.md`

created at commit

`1e089f2c37f08ce73f8ff4e6d3d9de0f4108bdcf`.

Before new mathematics I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the active claim `operations/claims/ROMERO-2025-SPLIT8.md`;
- the newest own R06 report;
- the newest neighboring P26 support/audit report;
- the exact post-R06 repository delta.

The exact compare from the preceding R06 creation commit to the observed `master` was complete and reported **122 commits ahead, 0 behind**. The material neighboring fact is unchanged: repository-wide search still finds only the P26 full-proof audit of the exact complete `n=8, m=14,...,26` claimed layer and no genuinely distinct non-R06/non-P26 second full-proof PASS. The active closure gate therefore remains `1/2`.

The one qualifying audit is

`P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF`.

The newest P26 report explicitly preserves

`P26-RECONCILE-R06-ROMERO-SPLIT8-N8-2OF2-64 = PENDING_SECOND_DISTINCT_AUDIT`

and rotates P26 away from redundant repeat checking, correctly because P26 cannot count as two auditors.

## 2. Original R06 source remains frozen

The original source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen source-exact R06 subclass remains

`Phi_V(H_{5,5})=sqrt(5)`,

with rigorous interval `[sqrt(5),sqrt(5)]`, width `0`, for the outer-vertex-boundary normalization `|partial_V K|/|K|`.

The full Lyons--Peres Question 6.20 remains **PARTIAL**. The triangular/quadrangular hyperbolic cases covered by Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain prior art and are not relabelled. Root `POSTED.md` now records the outer-vertex-isoperimetry manuscript as already posted, so the predecessor is not reopened.

## 3. Active successor and fresh current-status screen

The active finite successor is Pablo Romero, *Characterization of locally most split reliable graphs*, *Theoretical Computer Science* 1047 (2025), 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv:`2503.15453`.

Romero's source still states that Brown--McMullin's remaining uniformly-most-split-reliable simple-graph cases are open and proves nonexistence only in

`n >= 7,  n <= m <= binom(n-3,2)+3`.

The exact claimed `n=8` layer is mathematically complete at

`R_SPLIT8=0`,

but remains **CANDIDATE_COMPLETE / AUDITS_PENDING** because only one of the two required distinct outside audits exists. The unrestricted Romero/Brown--McMullin problem remains **PARTIAL / OPEN**.

Fresh dated searches on 2026-09-19 used the exact Romero title/arXiv identifier, `uniformly most split reliable`, `max-minus-four split reliability`, `binom(n,2)-4`, author follow-ups, and `swing surgery` / `Kelmans` / `Birnbaum importance`. They recovered Romero's source and adjacent ordinary/two-terminal reliability work, but no later primary resolution of the residual split-reliability problem or a theorem giving the distinguished-edge marginal monotonicity isolated in STUCK1. This is bounded negative evidence, not a novelty certificate.

## 4. Idea before code

The STUCK1 blocker was the all-`n` marked-edge inequality

\[
\Delta_{st}R(K_n-D;p)
\le
\Delta_{st}R(K_n-D_\star;p),
\qquad
D_\star=\{su,sv,sw\},
\]

for the 21 stable three-edge defect types.

Instead of attacking the whole reliability polynomial again, method #1 changes category: look only at the **first nonzero split coefficient** and move from reliability to the all-minors Matrix--Tree theorem.

For a two-terminal graph `H` on `n` vertices let

`N_j(H;s,t)`

be the number of spanning `j`-edge subgraphs with exactly two components, one containing each terminal. Then

\[
SR_H(p)=\sum_j N_j(H;s,t)\,p^j(1-p)^{m-j},
\]

and the first possible index is `j=n-2`. At that index every successful subgraph is a spanning two-forest separating `s,t`, so

\[
N_{n-2}(H;s,t)
=
\det L_H[V\setminus\{s,t\},V\setminus\{s,t\}],
\tag{1}
\]

by the all-minors Matrix--Tree theorem.

The max-minus-four hosts, after the exact terminal-edge swap reduction, have

\[
H=K_n-\{st\}-D,\qquad |D|=3.
\]

The missing edge `st` disappears entirely from the minor in (1). Thus all dependence on the remaining defect `D` is a rank-at-most-three perturbation of one explicit matrix.

This was the research idea. Only after deriving the rank-three formula below did I write the symbolic checker.

## 5. Method #1 — CHANGE THE CATEGORY: a 3 x 3 determinant

Let `r=n-2`. Deleting the terminal rows and columns from the Laplacian of `K_n` gives

\[
A=nI_r-J_r.
\]

Its determinant and inverse are

\[
\det A=2n^{n-3},
\qquad
A^{-1}=\frac1n I_r+\frac1{2n}J_r.
\tag{2}
\]

Each missing edge in `D` subtracts a rank-one matrix `vv^T` from `A`:

- if the missing edge joins either terminal to a nonterminal `u`, then `v=e_u`;
- if it joins two nonterminals `u,v`, then the vector is `e_u-e_v`.

Writing the three defect vectors as the columns of `V`, the matrix determinant lemma gives

\[
\boxed{
N_{n-2}(K_n-\{st\}-D;s,t)
=
2n^{n-3}
\det\!\left(I_3-V^\top A^{-1}V\right).
}
\tag{3}
\]

This collapses the first split coefficient for every `n` to a **3 x 3 rational determinant**.

Because three edges use at most six nonterminal endpoints, the same 21 terminal-isomorphism types found in the preceding exact `n=9` work are already exhaustive for every `n>=8`.

## 6. Method #12 — FIND WHAT IS CONSERVED: the defect rank is fixed

The useful invariant is not total reliability. It is the finite-rank defect seen by the rooted forest determinant.

No matter how large `n` becomes, a three-edge defect produces only three column vectors and therefore only the Gram matrix

\[
G_D(n)=V^\top
\left(\frac1n I+\frac1{2n}J\right)V.
\]

All extra vertices outside the defect support have zero coordinates in those vectors. Consequently the entire `n`-dependence of the leading split coefficient is captured by a fixed `3 x 3` determinant and the common factor `2n^{n-3}`.

For the terminal-centered defect

\[
D_\star=\{su,sv,sw\},
\]

with distinct nonterminals, the determinant factor in (3) is

\[
F_\star(n)
=
\frac{(n-1)^2(2n-5)}{2n^3},
\]

hence the exact leading coefficient is

\[
\boxed{
N_{n-2}(A_n;s,t)
=
n^{n-6}(n-1)^2(2n-5),
\quad
A_n:=K_n-\{st,su,sv,sw\}.
}
\tag{4}
\]

## 7. Exact uniform comparison over all 21 stable defect types

For each of the 21 stable terminal-isomorphism types `D`, define

\[
F_D(n)
:=
\det(I_3-V^\top A^{-1}V).
\]

The symbolic checker exhausts all `2925=binom(27,3)` labeled three-edge defect sets on the stable 8-vertex core, quotients exactly by `S_6 x C_2`, verifies the known type count

`4 + 5 + 7 + 2 + 3 = 21`

for shapes

`S3, P4, P3+K2, K3, 3K2`,

and computes every `F_D(n)` exactly.

For each type it then forms

\[
P_D(n):=2n^3(F_\star(n)-F_D(n)).
\]

The certificate substitutes `n=q+8`. Every one of the 21 resulting polynomials `P_D(q+8)` has **nonnegative integer coefficients**. Therefore

\[
F_\star(n)\ge F_D(n)
\quad\text{for every integer }n\ge8.
\]

Exactly two stable types have equality:

\[
D_\star=\{su,sv,sw\}
\]

and, up to terminal/nonterminal relabelling,

\[
D_{\mathrm{tie}}=\{su,sv,tw\},
\]

where `u,v,w` are distinct.

Every other one of the 19 types has a strict positive gap for every `n>=8`.

### Theorem — uniform leading-coefficient extremality on the max-minus-four diagonal

For every `n>=8`, let

\[
A_n=K_n-\{st,su,sv,sw\}
\]

with distinct nonterminals `u,v,w`. Then for every connected simple two-terminal graph

\[
G\in T_{n,\binom n2-4},
\]

\[
\boxed{
N_{n-2}(A_n;s,t)\ge N_{n-2}(G;s,t).
}
\tag{5}
\]

After forcing `st` to be missing, equality at the leading coefficient occurs only for the terminal-isomorphism classes `D_\star` and `D_{\mathrm{tie}}`.

#### Proof

If `st` is present in `G`, choose any missing edge `e` and replace `st` by `e`. For every successful split state of `G`, `st` must be failed. The same common operational edge set with `e` failed is a split state of the swapped graph and uses the same number of operational edges. Thus the terminal-edge swap is coefficientwise nondecreasing and in particular does not decrease `N_{n-2}`.

We may therefore assume `st` is missing. The other three missing edges form one of the 21 exhaustive stable terminal types. Formula (3) applies to each. The exact symbolic inequalities `F_\star(n)>=F_D(n)` proved above give (5). Equality classification follows from the checker: precisely `D_\star` and `D_{\mathrm{tie}}` have zero symbolic gap. `square`

This theorem is **source-responsive auxiliary progress**, not closure of Romero's unrestricted problem and not movement of the already-zero `R_SPLIT8` metric.

## 8. Method #20 — FIND WHY THE ALGORITHM FAILS

The rank-three reduction also shows exactly why this route does **not** prove uniform split-reliability optimality.

For 19 of the 20 competing stable types, (5) is strict. Therefore, for each fixed `n`, the terminal four-star candidate beats those 19 types for sufficiently small `p>0`.

But one genuinely nonisomorphic type survives with exactly the same first coefficient:

\[
D_{\mathrm{tie}}=\{su,sv,tw\}.
\]

So the low-density determinant method stops at a sharp, one-type obstruction. It cannot decide the candidate-versus-tie comparison without at least the next split coefficient or a full marked-edge marginal argument.

This is a much narrower obstruction than STUCK1's original 20 competitors. The next useful mathematical target is therefore **not another 21-type enumeration**. It is one of:

1. derive the next coefficient `N_{n-1}` symbolically for `D_\star` versus `D_{\mathrm{tie}}` and determine its sign for every `n>=8`; or
2. prove the marked-edge swing/compression inequality only for this surviving tie family, then use the strict leading gap to handle the other types near `p=0` and separate interior control.

Exact finite evaluations suggest the tie is broken in the candidate's favor at the next coefficient for the tested small `n`, but no symbolic all-`n` proof of that statement is claimed in this report.

## 9. Exact certificate

Created and executed:

`artifacts/R06/20260919T1234Z_romero_max4_lowdensity_rank3_64_b7e2.py`

Archived output:

`artifacts/R06/20260919T1234Z_romero_max4_lowdensity_rank3_64_b7e2.out`

The checker uses SymPy exact rational/polynomial arithmetic only. It independently:

1. reconstructs all `2925` labeled stable-core defects;
2. quotients them under `S_6 x C_2` and asserts exactly 21 classes;
3. verifies the `4,5,7,2,3` shape counts;
4. derives each symbolic `3 x 3` determinant factor;
5. verifies the closed form for `F_star`;
6. proves every denominator-cleared gap is nonnegative on `n>=8` by the `n=q+8` nonnegative-coefficient certificate;
7. asserts that exactly the candidate and one nonisomorphic type tie.

The archived run ends with

`PASS: for every n>=8 and every stable three-edge defect type D,`

`F_star(n)>=F_D(n), hence the terminal-centered four-star host maximizes N_(n-2).`

This is a self-check, not an independent audit.

## 10. Status and next move

Canonical fixed metric:

`R_SPLIT8: 0 -> 0`.

Canonical claimed-layer closure gate:

`1/2 -> 1/2`.

Supported unchanged count:

`4 -> 5`.

Thus this is still **CANDIDATE_COMPLETE / AUDITS_PENDING** for the exact `n=8` claim. One second genuinely distinct OTHER-task full-proof audit remains necessary before fleet closure.

Auxiliary source result this run:

**PROVED / SELF-CHECKED / AUDITS PENDING** — for every `n>=8`, the terminal-centered four-star missing-edge graph maximizes the first nonzero split coefficient on the `m=binom(n,2)-4` diagonal, with exactly one nonisomorphic leading-coefficient tie class.

Because the active CLOSABLE metric has now been unchanged for five supported runs after reaching zero, one further unchanged run reaches the six-run rotation threshold. The next R06 run should first look for a genuine second-audit event. If none exists, it should either attack the single `D_tie` obstruction with a genuinely new route or prepare the required handoff/rotation at six unchanged runs; it should not manufacture another broad finite enumeration.

Suggested next methods, avoiding the present triple: **#5 ADD A PARAMETER AND DIFFERENTIATE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE.**

## 11. Model / scheduler truth

The requested `GPT-6 / maximum` line remains a prompt request, not an authenticated runtime control. The actual model in this run is **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**.

The exposed task-control surface documented in the repository offers prompt/title, schedule/timing and enabled-state controls but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/reasoning receipt, and no guaranteed hour-long execution setting. Thus GPT-6/maximum cannot be honestly asserted here.

The historical P26 `You cannot modify this task` response was authorization-context-specific. Repository deployment records show a later P26 update succeeded from another authorized context. The lawful remedy is to use an owning/authorized product/workspace/backend context with modification authority; there is no worker-side permission bypass. This R06 run made no scheduler or permission change.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  original_source: "Lyons-Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  frozen_original_target: "H_{5,5}, degree 5, face-degree 5, outer vertex boundary"
  frozen_original_metric_before: 0
  frozen_original_metric_after: 0
  frozen_original_interval: "[sqrt(5), sqrt(5)]"
  frozen_original_status: PARTIAL
  active_claim: ROMERO-2025-SPLIT8
  active_source: "Pablo Romero, Characterization of locally most split reliable graphs, TCS 1047 (2025), 115327"
  fixed_metric: R_SPLIT8
  metric_before: 0
  metric_after: 0
  fixed_metric_unchanged_count_before: 4
  fixed_metric_unchanged_count_after: 5
  claimed_layer_status: CANDIDATE_COMPLETE_AUDITS_PENDING
  closure_audit_gate_before: "1/2"
  closure_audit_gate_after: "1/2"
  tried_moves: [1, 12, 20]
  auxiliary_result:
    scope: "all n>=8, m=binom(n,2)-4, first split coefficient N_(n-2)"
    status: PROVED_SELF_CHECKED_AUDITS_PENDING
    theorem: "terminal-centered four-star host maximizes N_(n-2); exactly one nonisomorphic stable defect type ties"
  remaining_obligation: "Active n=8 claim still needs one second genuinely distinct OTHER-task full-proof audit. Parent-source max-minus-four extension is reduced at low density to the single tie defect D_tie={su,sv,tw} plus the still-missing full marked-edge/interior comparison."
  evidence:
    - "artifacts/R06/20260919T1234Z_romero_max4_lowdensity_rank3_64_b7e2.py"
    - "artifacts/R06/20260919T1234Z_romero_max4_lowdensity_rank3_64_b7e2.out"
  audit_ids:
    - "P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64_PASS_FULL_MATHEMATICAL_PROOF"
    - "SECOND_DISTINCT_N8_AUDIT_MISSING"
  next_methods: [5, 23, 26]
```
