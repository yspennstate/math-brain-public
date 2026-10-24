Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 maximum. SUCCESSOR METRIC MOVEMENT: RS-2026-CL-B `0/4 -> 4/4`; predecessor I0076 remains retired/frozen at positive-route `2/4`. Methods tried: #2 ATTACK THE NEGATION FIRST, #12 FIND WHAT IS CONSERVED, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

Problem/source: Anastasia Kireeva, Randomstrasse 101, **“Low-degree hardness of finding the largest clique in Erdős–Rényi graph (problems 36-38)”**, posted 5 June 2026; exact target is the displayed unplanted clique/deficient-set score inequality that the page labels “Conjecture 35”. Queue ID: **RS-2026-CL-B**. Status of the displayed statement after this run: **REFUTED AS PRINTED by owner self-proof; closure audits pending**.

# 1. Rotation continuity: I0076 is not reopened

The previous R15 target, Burdzy–Scheutzow *Forward Brownian Motion* Problem 7.2 / I0076, reached the mandatory six-unchanged-run CLOSABLE handoff and remains **OPEN / PARTIAL / RETIRED-HANDOFF**. Its transparent positive-route metric stays frozen at `2/4`: P1 (shift-coupling/invariant-field compiler) and P2 (full discrete FRW+BRW analogue) are proved; P3 (continuous common-shift relative-phase obstruction) and P4 (source closure/audits) remain open. This run does not create a seventh I0076 lemma.

Required repository continuity was read before dispatch: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest R15 report, current fleet/implementation manifests, current claims for higher-ranked candidates, and the latest neighboring R17 report. Higher-ranked CLOSABLE-looking candidates were either currently owned/reserved, resolved, source-scope held, or broad/not READY. The queue row `RS-2026-CL-B` had no current claim; a repository-wide search found the queue entry but no competing owner.

# 2. Exact source statement and admission

The live Randomstrasse page currently prints the following formulation in its “Unplanted setting”. For `G ~ G(n,1/2)` and `epsilon>0`, for all polynomial functions

\[
f:\{0,1\}^{\binom n2}\to\mathbb R^n
\]

of degree `o(log n)`, it asserts

\[
\mathbb E\max_{S:\,S\text{ is a }k\text{-clique in }G}
\langle \mathbf 1_S,f(G)\rangle
\le
C\,\mathbb E\max_{\substack{|S|=k,\\ |E_G(S)|\le(1-\varepsilon)\binom k2}}
\langle \mathbf 1_S,f(G)\rangle,
\tag{CL-B}
\]

where `0<C<1` is a constant.

The page does not give a range for `k` in this display and does not impose a centering, norm, mean-zero, symmetry, or additive-normalization constraint on `f`. The post title calls the group “problems 36-38” while the displayed box itself is labeled “Conjecture 35”; I therefore identify the source by the formula rather than silently repairing its numbering.

Fresh 2026-09-17 checks:

- the live Randomstrasse page still displays (CL-B) in this form;
- exact-phrase/follow-up searches found no later correction of this display and no source-matching resolution;
- the official AIM report for the December 2024 workshop states a **different** null-optimization challenge: prove that no polynomial of degree `o(log^2 n)` can find a clique of size `0.9 log n` in `G(n,1/2)`, and records only a weaker fixed-degree symmetric correlation result.

Therefore the theorem below refutes **the Randomstrasse displayed formulation as printed**. It does **not** claim to solve the broader AIM null-optimization problem.

A create-only canonical claim was written to `operations/claims/RS-2026-CL-B.md` and read back at commit

`d60ad2919e2051daa44e325eb34cb8ae90855ba8`.

# 3. Frozen candidate and metric

Freeze the family

\[
k_n=1,\qquad f_n(G)=\mathbf 1_n\quad(n\ge2),
\]

and let `epsilon>0` be arbitrary.

The fixed four-obligation metric is:

1. `f_n` is a source-admissible polynomial map;
2. `deg(f_n)=0=o(log n)`;
3. both source maxima in (CL-B) are well-defined and equal to `1` for every graph;
4. (CL-B) fails for every allowed `0<C<1`.

Before proof: **0/4**. After proof: **4/4**.

# 4. Move #2 — exact counterexample-first proof

For every graph `G` on `[n]` and every singleton `S={v}`,

\[
|E_G(S)|=0,\qquad \binom{|S|}{2}=0.
\]

Thus every singleton is simultaneously

- a `1`-clique, and
- a member of the right-hand feasible family, because
  \[
  0\le(1-\varepsilon)\,0=0
  \]
  for **every** real `epsilon>0`.

For `f_n(G)=\mathbf 1_n`,

\[
\langle\mathbf 1_S,f_n(G)\rangle=1
\]

for every singleton. Hence, pointwise in `G`, both maxima in (CL-B) equal `1`; therefore both expectations equal `1`. The claimed inequality becomes

\[
1\le C,
\]

which is false for every source-allowed `0<C<1`.

Finally, `f_n` has degree zero for every `n`, and

\[
\frac{0}{\log n}=0\to0,
\]

so `deg(f_n)=o(log n)` exactly in the source's asymptotic sense.

Therefore

\[
\boxed{\text{The displayed Randomstrasse conjecture (CL-B) is false as written.}}
\tag{R15-CLB-1}
\]

This is not a numerical or sampled counterexample; it is an exact all-`n` family.

# 5. Move #12 — the missing normalization is structurally fatal

The singleton witness exploits the missing `k` range, but there is a stronger reason the printed universal quantifier over **all** polynomial `f` cannot be right without normalization.

For fixed `k`, define the two pointwise score functionals

\[
L_G(f)=\max_{S\in\mathcal C_k(G)}\langle\mathbf1_S,f(G)\rangle,
\]
\[
R_G(f)=\max_{S\in\mathcal D_{k,\varepsilon}(G)}\langle\mathbf1_S,f(G)\rangle,
\]

whenever the respective feasible families are nonempty. For any real `a`, let

\[
g(G)=f(G)+a\mathbf1_n.
\]

Then `deg(g)=deg(f)` and, because every feasible set has cardinality `k`,

\[
L_G(g)=L_G(f)+ak,\qquad R_G(g)=R_G(f)+ak.
\tag{5.1}
\]

Thus the additive constant direction is a conserved affine direction of both score landscapes. If the source inequality were required for every unnormalized `f`, then on any regime in which the two feasible families are nonempty and the expectations are finite it would imply

\[
\mathbb E L_G(f)+ak
\le
C\bigl(\mathbb E R_G(f)+ak\bigr).
\]

Equivalently,

\[
(1-C)ak\le C\,\mathbb E R_G(f)-\mathbb E L_G(f).
\]

For `0<C<1`, the left-hand side tends to `+infinity` as `a->+infinity`, whereas the right-hand side is independent of `a`. Hence no normalization-free version with the printed quantifiers can hold.

This diagnosis survives any nontrivial fixed `k` regime once feasibility is guaranteed. So the issue is not merely the degenerate choice `k=1`: a corrected conjecture must remove or normalize the additive-constant direction (and also specify the intended `k` regime).

# 6. Move #23 — reverse the anticipated answer and compare to AIM

The queue asked to recover the `k` range and normalization rather than assume the display was complete. The outside AIM workshop report explains why this was necessary. Its actual null-optimization problem is:

> prove that no polynomial of degree `o(log^2 n)` can find a clique of size `0.9 log n` in `G(n,1/2)`.

The report then gives a weaker theorem only for **symmetric fixed-degree** maps, bounding their clique correlation. This is qualitatively compatible with the intended research direction, but it is not (CL-B), and it supplies no missing normalization that can silently be imported into the Randomstrasse display.

So the correct disposition is:

- Randomstrasse displayed inequality: **REFUTED AS PRINTED**;
- likely intended normalized/nondegenerate formulation: **NOT RECOVERED from the display; do not invent it**;
- broader AIM 2024 null-optimization problem: **OPEN / not claimed solved here**.

# 7. Exact self-check artifact

Because the metric moved, I ran a small exact-arithmetic self-check only after the idea/proof was fixed. It is explicitly labeled a **self-check, not the theorem proof**.

Checker:

`artifacts/R15/20260917_0257Z_clb_constant_vector_exact_check.py`

read back at commit

`b840cd3c34a6351fd4d4ebc4bb234331490fd6e0`.

Executed output:

`artifacts/R15/20260917_0257Z_clb_constant_vector_exact_check_output.txt`

read back at commit

`f2614b0c1d44e3a31fcb07c69425ace35454e23c`.

The exact run uses `epsilon=1/3`, `C=999/1000`, and verifies the frozen `k=1` witness for every `n=2,...,50`; all checks pass. The all-`n`, all-`epsilon`, all-`C<1` proof is the argument in Section 4, not the finite run.

# 8. Closure status and audits

The source statement is mathematically refuted as printed by the on-page proof, but **R15 does not call the task CLOSED yet**. Fleet closure still requires two independent audits by other tasks, one supplied by P26 and a second by another independent track. No audit IDs exist yet, so none is invented.

A paper folder is therefore **not** created in this run. If the two audits pass, the appropriate deliverable should be a very short correction/note that states the exact printed formula, the constant-vector counterexample, and the additive-shift obstruction, while explicitly separating it from the broader AIM problem.

# 9. Neighbor R17 audit duty

The newest visible R17 report remains **OPEN / PARTIAL** on the Chvátal–Sankoff constant. It has genuine interval-width movement via an improved exact upper endpoint, but it is not a source-closure package. Therefore the instruction “audit R17 when a package is ready” is not triggered and no R17 audit verdict is manufactured.

# 10. Model / scheduler / permission status

The requested GPT-6 / maximum setting is still not verifiable or settable through the exposed task-control interface. The available controls expose prompt/title/schedule/timing/enabled state, but no authenticated model selector, reasoning-effort selector, or completed-run model telemetry. This report therefore records the actual model metadata available to this run as **GPT-5.6 Sol / reasoning UNVERIFIED**.

To make GPT-6/maximum enforceable would require an owner/product scheduler surface that persists model and reasoning fields and exposes authenticated run metadata, or platform support that changes the runtime assignment.

The historical P26 `"You cannot modify this task"` failure remains an authorization/context boundary. The legitimate workaround is the owning authorized context/account, an owner/admin permission change, or platform support; creating a duplicate schedule or bypassing permissions is not authorized. No scheduler change was attempted here.

# 11. Structured ledger delta

```yaml
ledger_delta:
  source: >-
    Anastasia Kireeva, Randomstrasse 101, 2026-06-05,
    displayed unplanted clique/deficient-set low-degree score conjecture
    (queue ID RS-2026-CL-B)
  target: >-
    Decide the displayed inequality exactly as printed, without importing an
    unstated k-range or normalization.
  predecessor:
    id: I0076
    status: RETIRED-HANDOFF_OPEN_PARTIAL
    metric: "positive-route gates frozen at 2/4 after six unchanged runs"
  metric: >-
    Number of four source-witness obligations proved for the frozen family
    k_n=1, f_n(G)=1_n.
  before: "0/4"
  after: "4/4"
  status: "REFUTED_AS_PRINTED_SELF_PROOF; CLOSURE_AUDITS_PENDING"
  unchanged_count: 0
  tried_moves: [2, 12, 23]
  remaining_obligation: >-
    Obtain independent P26 and second-track audits; do not claim the broader
    AIM 2024 null-optimization problem or invent a corrected normalization.
  evidence:
    claim_commit: d60ad2919e2051daa44e325eb34cb8ae90855ba8
    checker_commit: b840cd3c34a6351fd4d4ebc4bb234331490fd6e0
    checker_output_commit: f2614b0c1d44e3a31fcb07c69425ace35454e23c
    theorem: R15-CLB-1
  audit_ids: []
```

No root `RESULTS.md`, `QUEUE.md` or `POSTED.md` edit was made; P26 remains the shared-ledger writer. No email, Gmail, Drive, public posting, purchase, permission change, or scheduler change was made.
