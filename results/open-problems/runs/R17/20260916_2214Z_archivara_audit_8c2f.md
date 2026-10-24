Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime and scheduler interface provide no model selector or reasoning-effort selector; I do not claim otherwise. **NO MOVEMENT: certified deterministic interval width `0.033614007999972411... -> 0.033614007999972411...`. Section-B moves tried: 21 (ask who else has this shape), 23 (do what the proposer did not expect), 13 (find what only increases).**

Problem/source: Václav Chvátal and David Sankoff, “Longest common subsequences of two random sequences,” *Journal of Applied Probability* 12(2) (1975), 306–315, DOI `10.2307/3212444`. Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E LCS(X_1^n,Y_1^n)}n
\]
for independent iid fair binary strings.

Run ID: `20260916_2214Z_archivara_audit_8c2f`.

Status of the outside problem: **OPEN**. R17 status: **PARTIAL**. No exact-value closure is claimed.

# 1. Fixed metric

The certified deterministic R17 interval remains
\[
\boxed{
0.792665992
\le \gamma_2
\le
\frac{173228576586520}{209648759000007}
=
0.8262799999999724111889\ldots
}
\]
and therefore
\[
\boxed{
W=U-L
=
\frac{880891882776315417257}
{26206094875000875000000}
=
0.0336140079999724111889\ldots .
}
\]

There is **no movement** in this run.

The source status check on 2026-09-17 (Asia/Jerusalem; 2026-09-16 UTC) still finds the exact binary constant unresolved. Tiskin arXiv:2212.01582 describes the coefficient as “as yet unresolved.” Lember--Sova (first published 18 July 2026, DOI `10.1111/sjos.70086`) work in a pairwise-Markov strongly-related-string model and explicitly call the Chvátal--Sankoff constant unknown. The 2025 ISIT publication of Heineman et al. continues to state the deterministic lower endpoint `0.792665992`.

# 2. Repository continuity

Before research I read the required current repository surfaces rather than restarting from chat memory:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R17/20260916_2114Z_lowerprecision_6b2e.md`;
- current `runs/R18/` listing and newest R18 closure report;
- historical/intake search for the binary-LCS target, including the P0283 lineage.

The previous R17 report left two live high-value directions: reproduce the exact Heineman length-21 production certificate on the lower side, or regenerate Lueker's h=8 witness with stronger directed-rounding slack on the upper side. This run did not repeat either unchanged computation. Instead it checked a newly surfaced 2026 lower-bound claim that is now being tracked by a major public constants repository.

# 3. Move 21 — current-status discovery: a new 0.79970* claim exists, but is explicitly unverified

The Davis--Ivanisvili--Tao `optimizationproblems` repository currently lists the binary Chvátal--Sankoff entry as
\[
0.792665992\;(0.79970^*) \le C_{31}\le0.826280,
\]
and its recent-progress section says:

`C31 improved lower bound (unverified): C31 >= 0.79970* by Archivara, 4 Mar 2026.`

The repository's global note says an asterisk marks bounds whose available verification is currently at “minimal levels”; it also warns that listed submissions are not certified by the site for correctness.

The C31 source entry identifies the claim as:

Archivara Agent, *An Improved Lower Bound on the Chvátal--Sankoff Constant for Binary Strings via Monte Carlo Beam Search* (2026),

with public code/data at `spicylemonade/constant`.

This is an important current-status correction relative to earlier R17 source passes: there is now a claimed lower endpoint above Heineman's value, but the tracking site itself explicitly marks it unverified.

Because R17's fixed metric accepts only rigorously certified deterministic endpoints, I audited the actual proof mechanism rather than importing `0.79970`.

# 4. Move 23 — exact audit of the Archivara inference

The public paper/repository defines a beam heuristic \(H_N(X,Y)\) on two independent fair binary strings of length \(N\). The code keeps at most \(W\) frontier pairs \((i,j)\), expands by the next possible `0` and `1` match, and prunes by a deterministic endpoint score. Every output is indeed a valid common subsequence, so pathwise
\[
H_N(X,Y)\le LCS(X,Y).
\]

Consequently the elementary deterministic transfer is valid:
\[
\frac{\mathbf E H_N}{N}
\le
\frac{\mathbf E L_N}{N}
\le
\gamma_2.
\tag{C014.1}
\]
The paper itself states this part correctly.

The public experiment then takes
\[
N=1000,\qquad W=100,\qquad M=1,000,000,
\]
reports empirical normalized mean approximately
\[
\bar Z=0.803417,
\]
and applies Hoeffding with \(\delta=10^{-12}\) to obtain the displayed margin approximately
\[
0.003717.
\]

Hoeffding gives the probabilistic statement
\[
\Pr\left\{
\mathbf E Z
\ge
\bar Z-
\sqrt{\frac{\log(1/\delta)}{2M}}
\right\}
\ge1-\delta
\tag{X014.1}
\]
with respect to the random Monte Carlo sample.

It does **not** imply, for the particular realized sample, the deterministic theorem
\[
\mathbf E Z\ge0.79970.
\tag{X014.2}
\]

## R17-X014 — finite-sample concentration does not certify a deterministic endpoint

**STATUS: PROVED LOGICAL OBSTRUCTION / DOES NOT REFUTE THE OPEN SOURCE PROBLEM.**

For every finite \(M\), consider iid Bernoulli random variables of true mean
\[
p=\frac14.
\]
The realization
\[
Z_1=\cdots=Z_M=1
\]
has strictly positive probability
\[
p^M=4^{-M}>0,
\]
yet its empirical mean is \(1\), far above its true expectation \(1/4\).

Thus no finite observed sample, merely by satisfying a high-confidence concentration interval, logically excludes the exceptional event. A \(1-\delta\) confidence statement is not a probability-one or exact-arithmetic certificate of the unknown expectation.

This does **not** say Hoeffding's inequality is false. It says the inferential level is different:

- valid: “with confidence at least \(1-10^{-12}\), this experiment supports \(\gamma_2\ge0.79970\)” under the sampling assumptions;
- not established by that argument: the deterministic mathematical theorem \(\gamma_2\ge0.79970\).

This distinction exactly matches the owner's standing rule that simulation confidence intervals do not count as deterministic rigorous endpoints.

Therefore the R17 ledger does **not** replace `0.792665992` by `0.79970`.

The public automated peer-review file in the Archivara repository endorses the Monte Carlo/Hoeffding step as “rigorous”; that review does not repair the logical issue above because it uses the same confidence inference rather than a deterministic evaluation of \(\mathbf E H_N\).

# 5. Exact finite audit of the beam component

I did not stop at the inferential objection. I separately checked whether the beam heuristic itself really produces valid common subsequences.

The exact checker exhaustively enumerates all binary input pairs through \(n=7\) for \(W=1,2,3\), comparing the beam score against an independent exact LCS dynamic program. It verifies
\[
0\le H_{n,W}(x,y)\le LCS(x,y)
\]
in **65,532 exact beam/LCS comparisons**.

It also checks 768 exact two-block concatenation cases:
\[
H_{2,W}(x_1,y_1)+H_{2,W}(x_2,y_2)
\le
LCS(x_1x_2,y_1y_2).
\]

Interesting finite evidence, not an asymptotic theorem: the tested \(W=3\) beam agrees with exact LCS on every pair through \(n=7\). At \(n=7\),
\[
\mathbf E H_{7,3}
=
\mathbf E L_7
=
\frac{19339}{4096}.
\]
Dividing by 7 gives only a noncompetitive finite-block lower bound, so this finite computation does **not** move the metric.

The checker contains no Monte Carlo and ends `ALL_EXACT_CHECKS_PASS`.

# 6. Move 13 — a deterministic regenerative compiler for beam-like heuristics

The confidence failure suggests the right repair: convert the heuristic itself into a renewal process whose mean cycle consumption can be certified, rather than estimating a fixed-block expectation from a random sample.

## R17-C015 — safe-exposure regenerative lower-bound compiler

**STATUS: PROVED.**

Let \(X,Y\) be independent iid fair infinite binary streams. Fix an integer reward \(r\ge1\). Suppose an adaptive algorithm \(\mathcal A\), starting from fresh tails, reveals only finitely many coordinates almost surely, outputs a common subsequence of exactly \(r\) symbols, and at termination has exposed prefixes of lengths
\[
C_X,\qquad C_Y.
\]
Assume
\[
\mu_X=\mathbf E C_X<\infty,\qquad
\mu_Y=\mathbf E C_Y<\infty.
\]

After every cycle, discard **all exposed coordinates** and restart \(\mathcal A\) on the two unexposed tails.

Then
\[
\boxed{
\gamma_2
\ge
\frac{r}{\max\{\mu_X,\mu_Y\}}.
}
\tag{C015.1}
\]

### Proof

Because the restart point lies strictly beyond every queried coordinate, deferred decisions for the product iid measure imply that the two unexposed tails are again independent iid fair binary streams, independent of the completed cycle. Hence the successive consumption pairs
\[
(C_{X,j},C_{Y,j}),\qquad j\ge1,
\]
are iid copies of \((C_X,C_Y)\).

Let
\[
S^X_k=\sum_{j=1}^k C_{X,j},
\qquad
S^Y_k=\sum_{j=1}^k C_{Y,j},
\]
and let
\[
K_n=
\max\{k:S^X_k\le n,\ S^Y_k\le n\}.
\]
Concatenating the \(r\)-symbol common subsequence produced in every completed cycle gives pathwise
\[
LCS(X_1^n,Y_1^n)\ge rK_n.
\tag{C015.2}
\]

By the strong law,
\[
\frac{S^X_k}{k}\to\mu_X,
\qquad
\frac{S^Y_k}{k}\to\mu_Y
\quad\text{a.s.}
\]
and therefore the inverse two-coordinate renewal count satisfies
\[
\frac{K_n}{n}
\to
\frac1{\max\{\mu_X,\mu_Y\}}
\quad\text{a.s.}
\]
Each cycle producing \(r\) matches necessarily consumes at least \(r\) coordinates from each stream, so
\[
0\le\frac{rK_n}{n}\le1.
\]
Dominated convergence and (C015.2) yield
\[
\gamma_2
=
\lim_n\frac{\mathbf E L_n}{n}
\ge
\lim_n\frac{r\,\mathbf E K_n}{n}
=
\frac{r}{\max\{\mu_X,\mu_Y\}}.
\]
This proves C015.

### Application to finite-width beam search

A fixed-width, fixed-depth beam cycle fits C015 if the “cycle boundary” is taken beyond **all coordinates inspected while expanding every retained beam state**, not merely beyond the endpoint of the ultimately preferred path. For finite \(W,r\), only finitely many next-occurrence queries are made; each fresh binary search has a geometric tail, so \(C_X,C_Y\) have finite means.

The algorithm is symmetric in the two streams, hence
\[
\mu_X=\mu_Y=: \mu_{W,r}
\]
and
\[
\boxed{
\gamma_2\ge \frac r{\mu_{W,r}}.
}
\tag{C015.3}
\]

This is a deterministic repair path for the beam idea. To beat the retained Heineman endpoint it would suffice to certify
\[
\boxed{
\mu_{W,r}
<
\frac{r}{0.792665992}.
}
\tag{O016}
\]

The new hard object is therefore a **mean exposure** rather than a confidence interval for a heuristic score.

C015 deliberately throws away all revealed-but-unused suffix information at each renewal, so it may lose substantial performance. A sharper version should retain a bounded revealed buffer as a finite Markov state and flush only on buffer overflow. That would give an exact finite-state lower-bound policy; an overflow state is a lower-bound mechanism, not an approximation to the exact LCS process.

This is the next mathematically honest way to exploit the 2026 beam-search idea.

# 7. Why the Monte Carlo data still matter — but only as evidence

The Archivara computation remains useful as **evidence** that a width-100 beam policy has high expected performance. It identifies a promising lower-bound policy family.

What it does not supply is the deterministic expectation needed by (C014.1). Two routes could make it rigorous:

1. compute or rigorously lower-bound \(\mathbf E H_{1000,100}\) by exact state aggregation / interval dynamic programming over the true iid input law; or
2. use C015/C015.3 (or a buffered variant) and rigorously upper-bound the mean exposure \(\mu_{W,r}\).

Either route would convert the heuristic into an admissible deterministic endpoint. Re-running more Monte Carlo trials does not.

# 8. Heineman lower endpoint and Lueker upper endpoint remain as in the prior run

The previous R17 report found that the public Heineman code computes
\[
B(m,S)=\frac{2m}{S+m}
\]
from an integer `min_change` and fixed-point scale, but the public repository does not preserve the exact length-21 production pair \((S,m)\) needed to reconstruct the nine-digit headline independently. This run searched the public repository/history again and found no `0.792665992` production log or preserved length-21 output. The source-published `0.792665992` is therefore retained, with the artifact-reproducibility caveat unchanged.

On the upper side, Lueker's original code landing page remains live. The web reader can enumerate the Java source files and Javadocs, but direct raw `.java` retrieval through the web reader is rejected because of `text/x-java`. That is an access-format limitation, not evidence that the code is unavailable. No new h=8 witness vector was recovered in this run, so C010 is unchanged.

# 9. Current-status conclusions

The deterministic certified interval does **not** adopt the public `0.79970*` claim.

The best status statement I can support is:

\[
\boxed{
0.792665992
\le\gamma_2
\le0.8262799999999724111889\ldots
}
\]

plus a separate probabilistic/unverified item:

\[
\gamma_2\gtrsim0.79970
\quad\text{at the stated Monte Carlo confidence level,}
\]
which is not part of R17's deterministic metric.

This distinction is materially important because a major public constants tracker currently displays both numbers side-by-side with the higher one marked by an asterisk.

# 10. Exact artifacts

Exact self-check:

`artifacts/R17/20260916_2214Z_confidence_regen_8c2f_checker.py`

creation commit:
`8162e0ecc23b834fdab1ccf3550c05868fd39d4a`

Archived output:

`artifacts/R17/20260916_2214Z_confidence_regen_8c2f_checker_output.txt`

creation commit:
`d0dccd42a76be57c2c9ed0f0ebab17f8a9e49c65`

Executed-output SHA-256:
`d17ab38ec50d82e58d52a3f630a9bb8a41910adb0683e17dabe760d4622b44a1`

Both files were read back at their returned commits.

The self-check covers:

- exact positive-probability counterexamples to deterministic finite-sample inference;
- 65,532 exhaustive beam-vs-LCS comparisons;
- 768 exact block-concatenation checks;
- small exact expected-LCS superadditivity regressions.

C015 is a theorem-sized analytic claim; its complete proof is on this page rather than delegated to the checker.

# 11. R18 audit duty

The newest visible R18 report is the already-closed, audit-complete, packaged Hasebe--Ueda--Wang Problem 4.11 result. It contains the distinct earlier R17 audit and the required P26 audit. No newer mathematical R18 package requiring a fresh R17 audit appeared before this report, so I did not manufacture a duplicate audit.

# 12. Model/scheduler control

The model-control situation is still unchanged.

The exposed scheduling interface offers task prompt/title, schedule/timing, enabled state and timing mode. It exposes no model selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` remains a request in prompt text, not a verified runtime setting.

To make it enforceable, the product/API must expose model and reasoning controls for scheduled tasks, or the task must be managed in an owning workspace/admin surface that exposes those controls.

The historical P26 `"You cannot modify this task"` response is ownership/context-specific; repository records also show a later authorized context that could update P26. The legitimate workaround is the owning account/workspace or platform support. It is not permission bypass, schedule duplication, or another unauthorized task.

No scheduler change was attempted.

# 13. Claim ledger

Retained:
- R17-C001 through R17-C010 at their previous stated scopes.
- R17-C011 lower-endpoint artifact reconstruction, conditional exactly as stated.
- R17-C013 fair-binary specialization of the corrected Lember--Sova/Undrits entropy theorem.

New:
- **R17-X014: PROVED LOGICAL OBSTRUCTION** — a finite Monte Carlo/Hoeffding confidence interval does not by itself certify a deterministic lower endpoint for the unknown expectation.
- **R17-C015: PROVED** — safe-exposure regenerative compiler
  \[
  \gamma_2\ge r/\max(\mu_X,\mu_Y).
  \]
- **R17-O016: OPEN** — find finite \(W,r\) and a rigorous mean-exposure certificate
  \[
  \mu_{W,r}<r/0.792665992,
  \]
  or implement a bounded revealed-buffer finite-state policy that certifies a stronger lower endpoint.

The public `0.79970*` claim is classified **UNVERIFIED / CONFIDENCE-LEVEL EVIDENCE**, not `REFUTED`; the source problem remains OPEN.

# 14. Next attack

The next lower-side attack should not run more Monte Carlo. It should compile the beam idea into a deterministic finite-state or regenerative certificate.

The most promising concrete version is a **bounded revealed-buffer beam**: keep the true already-exposed suffix bits and relative beam frontier as the Markov state up to a buffer cap \(K\); on overflow, flush to a fresh exposure boundary. This is a genuine finite-state lower-bound policy, not a truncation of the true LCS process. Every transition probability is dyadic and can in principle be handled in exact arithmetic. Its stationary reward/consumption ratio would be a deterministic lower endpoint.

If that policy fails to exceed `0.792665992`, preserve the exact obstruction and return to regenerating Lueker h=8 for a meaningful upper improvement.

# 15. Structured ledger_delta

```yaml
ledger_delta:
  track: R17
  source:
    authors: "Václav Chvátal; David Sankoff"
    year: 1975
    target: "exact binary Chvátal-Sankoff constant gamma_2"
  metric:
    name: "width U-L of the rigorously certified deterministic interval containing gamma_2"
    before_exact: "880891882776315417257/26206094875000875000000"
    before_decimal: "0.0336140079999724111889..."
    after_exact: "880891882776315417257/26206094875000875000000"
    after_decimal: "0.0336140079999724111889..."
    movement: "none"
  endpoints:
    lower_certified: "0.792665992"
    upper_certified: "173228576586520/209648759000007"
    excluded_from_metric:
      - "0.79970* Archivara Monte Carlo/Hoeffding claim; public tracker marks unverified and the supplied argument is confidence-level, not deterministic"
  status: PARTIAL
  source_problem_status: OPEN
  unchanged_count_since_last_metric_move: 2
  methods_this_run: [21, 23, 13]
  exact_evidence:
    - "artifacts/R17/20260916_2214Z_confidence_regen_8c2f_checker.py @ 8162e0ecc23b834fdab1ccf3550c05868fd39d4a"
    - "artifacts/R17/20260916_2214Z_confidence_regen_8c2f_checker_output.txt @ d0dccd42a76be57c2c9ed0f0ebab17f8a9e49c65"
    - "output sha256 d17ab38ec50d82e58d52a3f630a9bb8a41910adb0683e17dabe760d4622b44a1"
  audit_ids:
    - "no new R18 audit required; newest R18 package already audit-complete"
  open_obligation:
    - "deterministically evaluate or upper-bound mean exposure of a regenerated/buffered beam policy strongly enough to exceed lower endpoint 0.792665992"
```

No Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler modification, shared-root edit, or peer-file edit was made.
