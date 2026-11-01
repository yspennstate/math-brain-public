Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: RS-2026-CL-B remains `4/4 -> 4/4`, unchanged count `0 -> 1`; predecessor I0076 remains retired/frozen at positive-route `2/4`. Methods tried: #4 PROVE SOMETHING WEAKER, COMPLETELY; #14 FIND THE GROUP ACTING; #28 REPLACE FOR ALL WITH FOR TYPICAL.**

Problem/source now owned by R15 after the mandatory I0076 rotation: Anastasia Kireeva, Randomstrasse 101, **“Low-degree hardness of finding the largest clique in Erdős–Rényi graph (problems 36-38)”**, posted 5 June 2026; exact active target is the displayed unplanted clique/deficient-set inequality labeled “Conjecture 35”. Canonical claim: `operations/claims/RS-2026-CL-B.md`. Status after this run remains **REFUTED AS PRINTED by the exact k=1 witness; closure audits pending**.

# 1. Continuity and repository recovery

The Burdzy–Scheutzow Problem 7.2 / I0076 predecessor is **not reopened**. It reached the six-unchanged-run CLOSABLE handoff and remains OPEN / PARTIAL / RETIRED-HANDOFF, with the transparent positive-route metric frozen at `2/4`: P1 (shift-coupling/invariant-field compiler) and P2 (full discrete FRW+BRW analogue) are proved; P3 (continuous common-shift/relative-phase obstruction) and P4 (source closure/audits) remain open.

Before new work I recovered the current repository state rather than restarting: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the newest R15 report `runs/R15/20260917_0257Z_clb_constant_shift_a23.md`; the canonical CL-B claim; current implementation manifest `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`; current neighboring Randomstrasse screen from R09; and the newest visible R17 report. Repository search found **no independent CL-B audit verdict yet**. R09 explicitly recognizes CL-B as owned by R15 and leaves it untouched.

# 2. Current source check and exact distinction from the AIM problem

Fresh check on 2026-09-17: the live Randomstrasse page still prints

\[
\mathbb E\max_{S:\,S\text{ is a }k\text{-clique in }G}
\langle1_S,f(G)\rangle
\le
C\,\mathbb E\max_{\substack{|S|=k,\\ |E_G(S)|\le(1-\varepsilon)\binom{k}{2}}}
\langle1_S,f(G)\rangle,
\qquad 0<C<1,
\tag{CL-B}
\]

for every polynomial map `f:{0,1}^{binom(n,2)} -> R^n` of degree `o(log n)`, with `G~G(n,1/2)` and `epsilon>0`. The display still states **no k-range and no centering, norm, mean-zero, or additive normalization on f**.

Live source: https://randomstrasse101.math.ethz.ch/posts/clique-low-degree/

The official AIM 2024 workshop report is materially different. Its null-optimization challenge is to prove that no polynomial of degree `o(log^2 n)` can find a clique of size `0.9 log n`; the workshop then proves only a weaker result for symmetric fixed-degree maps, with an explicit norm scale on the right-hand side. I inspected the report pages containing both statements, not just a search snippet.

AIM report: https://aimath.org/pastworkshops/lowdegreecomplexityrep.pdf

Bounded dated searches for the exact display, `Randomstrasse Conjecture 35` plus clique/low-degree terms, later Kireeva low-degree-clique work, and explicit corrections found no later source that repairs or resolves this exact printed formula. This is bounded negative evidence only, **not** a novelty certificate.

# 3. Retained exact source-level refutation

The frozen source witness from a23 remains

\[
k_n=1,\qquad f_n(G)=\mathbf 1_n.
\]

It is degree zero, hence `o(log n)`. Every singleton is simultaneously a 1-clique and a right-hand feasible set because `binom(1,2)=0`; both maxima are therefore exactly 1 for every graph, so (CL-B) becomes `1 <= C`, impossible for every `0<C<1`.

That source-level proof remains the closure core and its metric remains `4/4`. The purpose of this run is not to count another obligation, but to test the obvious objection that the missing `k` range was merely a harmless typo.

# 4. Method #4 — a complete robustness theorem at the intended logarithmic scale

There is a second issue in the printed display: for `k>=2`, either feasible family can be empty on rare graphs, and the source does not state a convention for `max emptyset`. Thus the literal expression is not globally defined for such `k` unless one supplies a repair.

The following theorem shows that **even the natural intended-scale repair does not rescue the multiplicative gap**.

## R15-CLB-2 — logarithmic-scale constant-vector obstruction

Fix

\[
k_n=\lfloor0.9\log_2 n\rfloor,
\qquad \varepsilon=\tfrac14,
\qquad f_n(G)=\mathbf1_n.
\]

For empty feasible families, use the natural nonnegative-score convention that the corresponding maximum is zero. More generally, the same conclusion holds under any repair whose value on an empty family is `O(k_n)`.

Let `L_n(G)` and `R_n(G)` be the two score maxima. On a graph for which the relevant feasible family is nonempty, the constant vector gives exactly

\[
L_n(G)=k_n,\qquad R_n(G)=k_n.
\]

For the left side, the standard random-clique facts recalled by the live source are already enough: the maximum clique has size approximately `2 log_2 n` with high probability, and even the elementary greedy algorithm finds a clique of size approximately `log_2 n` with high probability. Hence

\[
\Pr(\omega(G)\ge k_n)\to1.
\tag{4.1}
\]

For the right side, fix one deterministic set `S_0` of size `k_n` and put

\[
m_n=\binom{k_n}{2},\qquad X_n=|E_G(S_0)|\sim\mathrm{Bin}(m_n,1/2).
\]

The deficient threshold for `epsilon=1/4` is `3m_n/4`. Hoeffding gives

\[
\Pr(X_n>3m_n/4)
=\Pr(X_n-m_n/2>m_n/4)
\le \exp(-m_n/8)\to0.
\tag{4.2}
\]

Therefore a right-hand feasible set exists with probability tending to one. Under zero-on-empty,

\[
\frac{\mathbb E L_n}{k_n}
=\Pr(\omega(G)\ge k_n)\to1,
\]

and

\[
\frac{\mathbb E R_n}{k_n}
\ge \Pr(X_n\le3m_n/4)\to1,
\]

while always `R_n<=k_n`; hence

\[
\frac{\mathbb E R_n}{k_n}\to1.
\]

Consequently

\[
\boxed{\frac{\mathbb E L_n}{\mathbb E R_n}\to1.}
\tag{4.3}
\]

For every fixed `0<C<1`, (4.3) violates (CL-B) for all sufficiently large `n`.

If the empty-family repair is merely bounded by `M k_n` in absolute value, the exceptional events in (4.1)-(4.2) have probability `o(1)`, so the same normalized expectation limits and conclusion hold.

**Outcome of method #4: successful strengthening, but no metric movement.** The printed formula is not only killed by `k=1`; after supplying a harmless empty-family convention it still fails at the AIM-motivated logarithmic clique scale for the same degree-zero constant vector.

# 5. Method #14 — complement symmetry gives an exact finite nondegenerate diagnostic

There is also an exact `k=2` sanity version once the same zero-on-empty convention is imposed. Take `epsilon=1/2`, `k=2`, and `f=1_n`.

The left feasible family is nonempty iff `G` has an edge. The right feasible family requires at most `(1-epsilon) binom(2,2)=1/2` edges, hence is nonempty iff `G` has a nonedge. Therefore

\[
L_n(G)=2\mathbf1\{G\text{ has an edge}\},
\qquad
R_n(G)=2\mathbf1\{G\text{ has a nonedge}\}.
\]

The complement involution `G -> \bar G` preserves `G(n,1/2)` and swaps the two events. Thus, with `N=binom(n,2)`, exactly

\[
\mathbb E L_n
=\mathbb E R_n
=2(1-2^{-N}).
\tag{5.1}
\]

So the factor `C<1` already fails exactly at every finite `n>=2` under this repaired nondegenerate interpretation.

This is not needed for the source-level k=1 refutation and I do not count it as a new metric obligation. Its role is diagnostic: merely inserting `k>=2` does not fix the display.

# 6. Method #28 — what survives after replacing universal syntax by the intended typical regime

The AIM report and the blog both frame the meaningful regime as `k` of order `log n` in a typical `G(n,1/2)`. R15-CLB-2 works exactly in that regime. The obstruction is therefore the **lack of normalization of f**, not just the degenerate source syntax.

The a23 affine calculation already showed the structural reason. For fixed k, adding `a 1_n` to f preserves degree and shifts each nonempty-family score by `ak`. R15-CLB-2 now shows that, in the intended typical regime where both families are nonempty with probability tending to one, that affine direction asymptotically forces the ratio of the two constant-vector scores to one. Any corrected `C<1` theorem therefore has to quotient out or normalize this direction (for example by a norm/centering condition) in addition to stating the intended k-scale.

This dovetails with the AIM workshop's weaker theorem, whose right-hand side explicitly contains an `L2` norm factor. I do **not** infer the intended corrected conjecture from that fact; the corrected statement remains to be supplied by the source authors.

# 7. Audits and closure status

Repository-wide searches this run found no P26 or second-track PASS/FAIL audit for RS-2026-CL-B. The mathematical source display remains **REFUTED AS PRINTED by owner self-proof**, but fleet closure remains pending the required two independent OTHER-task audits. No audit ID is invented and no paper folder is created.

The latest visible R17 report has genuine further interval-width movement on the Chvátal-Sankoff constant but still labels the source OPEN and the track PARTIAL. It is not a source-closure package, so R15's independent-audit duty is not triggered.

# 8. Model / scheduler / permission status

The requested `GPT-6 / maximum` setting is still not enforceable through the exposed scheduler interface. The actual controls available to this worker expose task prompt/title/schedule/timing/enabled state, but **no model selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. The repository implementation manifest records the same limitation. A verifiable GPT-6/maximum deployment would require an owner/product surface that persists those fields and returns authenticated run metadata, or platform support.

The historical P26 `You cannot modify this task` response was an authorization/context boundary, not a mathematical issue. Repository records also show that a different authorized context later succeeded in updating P26. The legitimate remedy for any future denial is the owning authorized context, permission/admin change, or platform support; duplicating a task or bypassing permissions is not authorized. No scheduler change was attempted here.

# 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: >-
    Anastasia Kireeva, Randomstrasse 101, 2026-06-05,
    displayed unplanted clique/deficient-set low-degree score conjecture
    (RS-2026-CL-B)
  target: >-
    Decide the displayed inequality as printed; after the exact k=1 refutation,
    test whether restoring the intended logarithmic k-scale rescues it.
  predecessor:
    id: I0076
    status: RETIRED-HANDOFF_OPEN_PARTIAL
    metric: "positive-route gates frozen at 2/4 after six unchanged runs"
  metric: >-
    Number of four source-witness obligations proved for frozen source-exact
    family k_n=1, f_n(G)=1_n.
  before: "4/4"
  after: "4/4"
  unchanged_count_before: 0
  unchanged_count_after: 1
  status: >-
    REFUTED_AS_PRINTED_SELF_PROOF; strengthened by R15-CLB-2 showing failure
    at k=floor(0.9 log_2 n) under any O(k)-bounded empty-family repair;
    CLOSURE_AUDITS_PENDING
  tried_moves: [4, 14, 28]
  remaining_obligation: >-
    Obtain independent P26 and second-track audits of the exact printed-source
    refutation. Do not claim the broader AIM null-optimization problem and do
    not invent a corrected normalization.
  evidence:
    prior_claim_commit: d60ad2919e2051daa44e325eb34cb8ae90855ba8
    prior_source_refutation_report: runs/R15/20260917_0257Z_clb_constant_shift_a23.md
    prior_exact_checker_commit: b840cd3c34a6351fd4d4ebc4bb234331490fd6e0
    prior_exact_output_commit: f2614b0c1d44e3a31fcb07c69425ace35454e23c
    new_theorem: R15-CLB-2
    finite_diagnostic: equation (5.1), complement symmetry at k=2 under zero-empty repair
  audit_ids: []
```

No new checker was manufactured because the fixed metric did not move and the new strengthening is an analytic theorem with its proof on the page. No email, Gmail, Drive, public posting, purchase, shared-root edit, permission change, or scheduler change was made.