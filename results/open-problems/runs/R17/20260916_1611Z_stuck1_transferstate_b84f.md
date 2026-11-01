Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — GPT-6 maximum was requested, but the scheduler exposes no model selector or reasoning-effort selector; I do not claim otherwise.
Problem: Chvátal–Sankoff, Chvátal and Sankoff (1975), *Longest common subsequences of two random sequences*, J. Appl. Probab. 12(2), 306–315, DOI 10.2307/3212444. Metric **NO MOVEMENT**: certified interval width `0.033614008 -> 0.033614008`.

# R17 stuck/thinking report — recovery episode 1

Run ID: `20260916_1611Z_stuck1_transferstate_b84f`  
Status: **OPEN / STUCK RECOVERY 1**.  
This is the mandatory thinking run after three consecutive visible no-movement R17 runs. Per protocol it makes **no new mathematical claim** and creates no new finite checker. It isolates the exact obstruction, inventories the routes already tried and their failure modes, identifies the simplest unresolved subproblem and the nearest solved analogue, and chooses exactly one recovery route for the next research run.

The rigorously certified interval remains

\[
\boxed{0.792665992\le \gamma_2\le0.826280},
\qquad
\boxed{U-L=0.033614008=\frac{4201751}{125000000}}.
\]

This is now the fourth visible R17 report with no interval movement (`13:15Z`, `14:25Z`, `15:15Z`, and this stuck report). Pre-13:15 history remains unknown; the supported visible `unchanged_count` after this immutable report is therefore `4`, not a claim about earlier unseen history.

## 1. Repository continuity and required reads

I continued from current `master`, not from chat memory. Before this thinking report I read or queried:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- the current root directory and the available `probability_1000_intake_*/problems.jsonl` family / attempt directories, including the Claude, D, E, F, G, H and I intake trees;
- all three current R17 reports under `runs/R17/`;
- the current `artifacts/R17/` inventory;
- newest neighboring R15 report `runs/R15/20260916_1556Z_i0076_any_seam_elimination_a13.md`;
- newest R18 report `runs/R18/2026-09-16_15-27-40_UTC__R18__i0080-closure-selfaudit-7d2c.md`.

The connector truncates very large directory/JSONL outputs. I therefore record that the intake family and ownership paths were queried, but I do **not** claim that roughly 780 intake rows were displayed manually in full. Nothing in the current posted/settled registers closes or excludes the Chvátal–Sankoff target, and `RFLEET_2026-09-16.md` still assigns it to R17 as a HARD OUTSIDE track with the certified-interval-width metric.

Root `RESULTS.md` still contains a stale R17 `UNMEASURED -> UNMEASURED` row. Under the fleet contract P26 alone reconciles `RESULTS.md`, `QUEUE.md` and `POSTED.md`; this run does not edit them.

### Recovered exact R17 artifacts

The current `artifacts/R17/` inventory contains the exact checkers/output for the three preceding runs:

- `20260916_1315Z_kboundary_7c41_checker.py` / `_output.txt`;
- `20260916_1421Z_blockmgf_9f2c_checker.py` / `_output.txt`;
- `20260916_1515Z_spantrunc_a63e_checker.py` / `_output.txt`.

No new checker is created in this stuck run because the protocol forbids new claims here.

## 2. Dated source/status pass — 2026-09-16

The source/current-status pass was refreshed before deciding whether to remain on the problem.

### Original source

V. Chvátal and D. Sankoff, “Longest common subsequences of two random sequences,” *Journal of Applied Probability* 12(2) (June 1975), 306–315, DOI `10.2307/3212444`.

Current Cambridge source page:
`https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/longest-common-subsequences-of-two-random-sequences/056EC0426982CDB22099F381DE53912B`

The source asks about expected LCS for random strings, studies the limiting normalized expectation and gives finite bounds/estimates. This remains the problem locator used by R17.

### Tiskin current revision

A. Tiskin, *The Chvátal-Sankoff problem: Understanding random string comparison through stochastic processes*, arXiv:2212.01582v2, current arXiv page checked 2026-09-16:
`https://arxiv.org/abs/2212.01582`.

The abstract still calls the exact proportionality coefficient unresolved. The current record also preserves the warning that earlier stochastic-process/`gamma` claims were found incorrect and removed. Consequently R17 continues to reject any exact stationary reduction unless it is proved for the actual random-string process.

### Lember–Sova 2026

J. Lember and J. Sova, *Extremal Alignments in LCS-Inference*, *Scandinavian Journal of Statistics* 53(3) (2026), 1327–1342, first published 18 July 2026, DOI `10.1111/sjos.70086`.

Current Wiley abstract checked 2026-09-16:
`https://onlinelibrary.wiley.com/doi/10.1111/sjos.70086`.

It treats a pairwise Markov model for strongly related strings, obtains an `O(log n/n)` convergence rate in that model, explicitly says this is faster than the best current iid-independent rate, and calls the Chvátal–Sankoff constant unknown. It is methodology, not an iid-independent closure.

### Current interval and later/citing literature

Heineman–Miller–Reichman–Salls–Sárközy–Soiffer, arXiv:2407.10925, gives the certified binary lower endpoint

\[
0.792665992.
\]

Lueker (JACM 2009) gives the certified upper endpoint

\[
0.826280.
\]

A current 2026 citing/source-status check was made against Li–Ren–Wen, *Expected Length of the Longest Common Subsequence of Multiple Strings*, DOI `10.1017/S000497272610104X`, published online 2 March 2026 / volume 114(1). Its introduction still calls determination of the two-string binary constant open and records roughly the same current bounds.

Dated bounded queries also checked the exact title, `0.792665992`, `0.826280`, arXiv:2212.01582, DOI 10.1111/sjos.70086, and recent LCS citing literature. No later rigorously certified binary interval narrower than the frozen interval was found in this bounded pass. That is a bounded search outcome, not proof of absence of an uncatalogued paper.

## 3. (a) Exact statement that blocks R17

The current best dependence-preserving R17 reduction is the bounded-span primal from C006–C007. For fixed source-block length `m` and target-span cap `B`, let

\[
q_{m,B}
=
\lim_{r\to\infty}
\frac{\mathbb E Q_{m,B}(X_1^{rm},Y_1^{rm})}{rm}.
\]

The proved deterministic truncation gives

\[
q_{m,B}\le\gamma_2\le q_{m,B}+\frac{m}{B+1}.
\]

The exact blocking obligation is therefore not existence of another limit; it is an **explicit finite certificate for the shape constant**. To improve the published upper endpoint through the current route one needs, for some finite `m,B`, a rigorously computable upper certificate `\overline q_{m,B}` satisfying

\[
\boxed{
q_{m,B}\le \overline q_{m,B}
\quad\text{and}\quad
\overline q_{m,B}+\frac{m}{B+1}<0.826280.
}
\tag{BLOCK}
\]

Alternatively a finite certified lower certificate for `q_{m,B}` exceeding `0.792665992` would move the lower endpoint. No current R17 construction provides either inequality. Merely writing `gamma_2=sup_B q_{m,B}` is not closure and earns no metric credit.

## 4. (b) Routes tried and the precise failure of each

### Route 1 — independent Bernoulli matching / integrable local particle process

**Failure:** it is not the actual LCS model. R17-C001 gives the exact rectangular parity constraint

\[
M_{11}\oplus M_{12}\oplus M_{21}\oplus M_{22}=0
\]

for `M_ij=1{X_i=Y_j}`. Any three rectangle corners can look iid Bernoulli(1/2), while the fourth is determined. Thus low-order local tests can misleadingly agree with the independent Bernoulli matching model. Tiskin's current arXiv record independently warns that earlier stochastic-process/`gamma` claims were incorrect and removed.

### Route 2 — fixed-memory raw-letter/boundary-increment Markovization

**Failure:** exact all-`k` counterexamples. R17-C002 constructs, for every fixed `k`, two environments with the same total LCS, last `k` source/target letters and last `k` horizontal/vertical LCS increments, but different next state after the same source append. R17-C003 strengthens this to a positive iid prediction-error floor `2^{-2k-2}` for every deterministic predictor based only on that state. Adding more *recent* suffix bits is therefore not a recovery route.

### Route 3 — exact source-block / target-composition decomposition alone

**Failure:** C004 is an identity, not a bound sharp enough to evaluate the limit. The maximizing target composition remains globally coupled to the full random environment. The identity is useful infrastructure but does not produce a finite stationary law or a new endpoint by itself.

### Route 4 — annealed block MGF / soft union over all target compositions

**Failure:** the proof is rigorous and its infinite-target-length numerical truncation is tiny, but the structural union bound is too loose. The exact `m=12` certificate was only

\[
\gamma_2<0.865754,
\]

which is weaker than `0.826280`. The numerical tail was certified below `10^{-9}`; therefore increasing the same truncation depth attacks the wrong error. The loss is the replacement of a maximum over mutually incompatible partitions by their exponential sum.

### Route 5 — bounded-span primal truncation C006–C007

**Success and remaining failure:** this is the first current R17 route with an explicit **uniform deterministic** truncation error:

\[
0\le LCS-Q_{m,B}\le m\left\lfloor\frac n{B+1}\right\rfloor,
\qquad
0\le\gamma_2-q_{m,B}\le\frac m{B+1}.
\]

However the two-dimensional DP for `Q_{m,B}` still carries a growing global boundary profile. Superadditivity proves existence of `q_{m,B}` but supplies finite-horizon **lower** approximants, not the upper certificate required by `(BLOCK)`. Simply taking larger `B` shrinks the deterministic truncation term while making the unresolved transfer problem larger; it does not evaluate `q_{m,B}`.

### Route 6 — simulation / decimal fitting

**Failure by scope:** simulation can suggest the value but cannot narrow the fleet metric. The source target is exact and the metric counts only rigorously certified intervals.

## 5. (c) What a successful proof must contain that the tried routes do not

For the current bounded-span route, a useful proof must add **one genuinely new ingredient**:

1. a dependence-preserving finite or quantitatively truncated transfer state for `Q_{m,B}` (or an equivalent dual potential class);
2. a proof that its omitted boundary information costs at most an explicit `epsilon_H` uniformly in the length;
3. an exact/rational finite computation of the resulting primal or dual growth rate; and
4. a final inequality strong enough to cross one of the existing endpoints.

The key missing inequality has the schematic form

\[
q_{m,B}
\le
\overline q_{m,B,H}+\varepsilon_{m,B}(H),
\qquad
\varepsilon_{m,B}(H)\downarrow0,
\]

with `\overline q_{m,B,H}` coming from a **finite exact** transfer/dual computation. Without the `epsilon_H` theorem, a finite-width transfer calculation is only a heuristic truncation. Without exact evaluation of the finite transfer, it is another unknown limit. Without respecting the rectangle dependence, it collapses back to the Bernoulli matching surrogate.

## 6. (d) Simplest special case still unproved

The simplest non-tautological shape constant produced by C007 is

\[
q_{2,1}
=
\lim_{r\to\infty}
\frac{\mathbb E Q_{2,1}(X_1^{2r},Y_1^{2r})}{2r}.
\]

Here each length-two source block may use at most one target symbol. This is much simpler than the metric-relevant large-`B` regime and should be the first sanity test for any proposed exact transfer formalism. It is **not itself metric-relevant**—its deterministic C007 error is far too large—but failure to close even this smallest strict bounded-span model would falsify the proposed transfer architecture before expensive work at larger `B`.

The metric-relevant version of the same obligation is `(BLOCK)` for a larger `B`: an exact finite dual/transfer certificate, not another simulation or finite-horizon lower ratio.

## 7. (e) Nearest solved analogue and the ingredient it has that actual LCS lacks

The closest exactly solved model is the **Bernoulli matching model** of sequence alignment. Majumdar–Nechaev (Phys. Rev. E 72, 020901, 2005) obtain exact asymptotics for that simpler model; Priezzhev–Schütz (arXiv:0807.0362, 2008) give an exact solution through a mapping to discrete-time TASEP, and Majumdar–Mallick–Nechaev (Phys. Rev. E 77, 011110, 2008) use a five-vertex/Bethe-ansatz representation.

What those proofs have and true random-string LCS lacks is precisely **independent local match occupancy / integrable local dynamics**. In the actual binary string model, rectangular match cells obey C001's cycle constraint and longer shared-letter dependencies. Therefore the Bernoulli matching stationary/product law cannot simply be ported. The portable lesson is architectural—find a local conserved/gradient state and an exact transfer—not the surrogate's invariant measure or constants.

## 8. Exactly one recovery choice

**Chosen recovery: reduce the obstruction to a finite computation and run it.**

The next research run will not add another ad hoc LCS lemma. It will attack the transfer obstruction directly by an exact **bisimulation/state-aggregation experiment for the bounded-span DP**, beginning with the smallest strict model `m=2,B=1` and then, only if the architecture survives, increasing `B`.

The finite experiment is:

- generate exact reachable normalized DP-boundary states for bounded-span `Q_{m,B}` on increasing finite rectangles;
- quotient two states only when every continuation of the tested horizon gives identical reward increments;
- adversarially search for state-class splits (counterexamples) before asserting closure;
- if a finite quotient stabilizes, extract its exact max-plus/Markov transition data and test whether the same state definition remains valid at larger horizons;
- if it does not stabilize, archive the smallest exact counterexample and abandon that state definition rather than assuming stationarity.

This is the first allowed stuck recovery. No new mathematical claim from that experiment is asserted in the present thinking report.

## 9. R18 independent-audit state

The newest R18 report is

`runs/R18/2026-09-16_15-27-40_UTC__R18__i0080-closure-selfaudit-7d2c.md`.

It introduces no theorem beyond its already-audited C007 all-time candidate. It explicitly records the prior R17 independent audit

`R17-AUDIT-R18-I0080-C007-ENDTOEND-002 = PASS_FULL_MATHEMATICAL_PROOF`

and states that the required P26 audit is still pending. Therefore there is **no new R18 mathematical package requiring a duplicate R17 audit this run**. The prior R17 audit remains the current OTHER-track audit; it is not counted twice.

## 10. Ledger delta for P26

```yaml
ledger_delta:
  track: R17
  lane: HARD OUTSIDE
  source: "V. Chvatal and D. Sankoff, Longest common subsequences of two random sequences, Journal of Applied Probability 12(2) (1975), 306-315, DOI 10.2307/3212444"
  target: "exact gamma_2 for two independent iid uniform binary strings"
  metric: "width U-L of the best rigorously certified interval containing gamma_2"
  before: "0.033614008 (L=0.792665992, U=0.826280)"
  after: "0.033614008 (L=0.792665992, U=0.826280)"
  movement: "NO MOVEMENT"
  status: "OPEN / STUCK RECOVERY 1"
  unchanged_count: 4
  unchanged_count_scope: "four visible R17 reports from 13:15Z through this report; pre-13:15 history UNKNOWN"
  blocking_obligation: "certified finite upper/lower evaluation of q_{m,B}; in particular qbar_{m,B}+m/(B+1)<0.826280 for an upper movement"
  chosen_recovery: "reduce obstruction to finite computation: exact bisimulation/state-aggregation search for bounded-span Q_{m,B}, counterexample-first"
  new_claims_this_run: []
  new_artifacts_this_run: []
  exact_evidence_retained:
    - "artifacts/R17/20260916_1315Z_kboundary_7c41_checker.py + output"
    - "artifacts/R17/20260916_1421Z_blockmgf_9f2c_checker.py + output"
    - "artifacts/R17/20260916_1515Z_spantrunc_a63e_checker.py + output"
  audit_ids:
    R18_other_audit: "R17-AUDIT-R18-I0080-C007-ENDTOEND-002=PASS_FULL_MATHEMATICAL_PROOF"
    R18_p26_audit: "PENDING"
    R17_p26_closure_audit: "NOT_APPLICABLE_OPEN"
    R17_second_closure_audit: "NOT_APPLICABLE_OPEN"
```

## 11. Delivery and limitations

This run intentionally creates only this immutable thinking report. There is no new finite claim, so creating a checker solely to satisfy a filename convention would violate the stuck-run instruction rather than add evidence.

No Gmail, Drive, email, public publication, paid compute, permission change, schedule change, root-ledger edit or other-track file edit was performed.

**NO CLOSURE CLAIM.**
