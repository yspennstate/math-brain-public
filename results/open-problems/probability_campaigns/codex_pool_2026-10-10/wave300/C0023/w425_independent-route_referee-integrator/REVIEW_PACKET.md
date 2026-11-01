# C0023 referee packet — w425, 2026-10-10

## Source/status gate

The dated `problems.jsonl:23` intake gives the nearest-neighbour Bernoulli bond target from Garban--Steif XI.1 p.136. Its open label is historical. The pinned [Anthropic formalization](https://github.com/anthropics/formal-math/tree/795efb86f191735c5481675763537cfb4ff37e55/percolation) defines the intended Z^d bond law in `Challenge.lean` and states `percolation_continuity (d) (2≤d)`. `Solution.lean` bridges that exact proposition by `Iff.rfl` to `Percolation.Continuity.CSH.percolationContinuity_allDimensions`. `AUDIT.md` records a clean solution build, two expected `sorry` placeholders only in the comparator statement file, main-theorem axioms `[propext, Classical.choice, Quot.sound]`, and comparator/nanoda acceptance. I inspected those files and the recorded receipt, but did not independently rebuild or audit the entire proof.

The newer [OpenAI comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/CriticalPercolation.lean) asserts a broader quasi-transitive critical nonpercolation theorem, with a [scope note](https://github.com/openai/math/blob/main/lean/docs/213.md) that includes Z³ bond/site. I have not checked that solution or its receipt. **Verdict: FIX** the historical open-status field to `claimed_solved_pending_independent_formal_audit`. No peer partial lemma proves C0023. An independent statement/axiom audit and rebuild should decide retirement.

## w423 verdicts

**L1 KEEP.** For a finite increasing Bernoulli event A, Russo differentiation gives `f'(p)=Σ_e P(e pivotal)`. Pivotality is independent of its own edge, and an open pivotal forces A, so `E[N_open-pivotal 1_A]=p f'(p)`. Division by `f(p)>0` and integration give the conditional bridge identity and the exact probability ratio. No independence among pivotal indicators is assumed.

**L2 KEEP, conditional criterion only.** A bounded subsequence of `∫_a^{p_c} λ_n(s)/s ds`, with `theta(p_c)>0`, gives `P_a(A_{n_k})≥theta(p_c)e^{-M}>0`; decreasing-event convergence forces `theta(a)>0`, contradicting `a<p_c`. The load bound is unproved on Z^d.

**L3 KEEP, special graph.** In block n, `m_n=n²2^{n+1}` disjoint length-`n+1` paths give `h_n(p)=1-(1-p^{n+1})^{m_n}`. At `p=1/2`, failure is at most `e^{-n²}`; for `p<1/2`, `h_n(p)≤n²(2p)^{n+1}→0`. The conditional single-open-path probability is at most `n²e^{-n²+1/4}/(1-e^{-1})`, yielding bounded exponential moments of endpoint open-pivotal count. The fixed backward-interval integral still diverges. I rederived the block formula, moment bound, and Borel–Cantelli uniqueness argument. The graph is locally finite but nontransitive with unbounded terminal degrees. The endpoint estimate does not transfer to Z^d.

**L4 KEEP, quenched fragility only.** Given Bernoulli(p_c) lattice bonds and independent q-retention, the annealed retained law is Bernoulli(p_c q). For each rational q<1 it is subcritical, so no infinite retained component almost surely. Fubini produces a full-measure set of base configurations for each rational q; intersect them countably and dominate any real q<1 by a rational r with q<r<1. Each hypothetical infinite component of a base configuration therefore has quenched retention threshold 1. This proves a conditional fragility statement, not that no critical infinite component exists. The missing geometric claim is that a hypothetical critical component would percolate under some q<1; no such claim is proved. Root-specific thresholds within a fixed connected component agree for q>0 by finite-path connection and FKG (or finite energy), so the author's parenthetical is valid.

**w423 six-concept bundle: KEEP as draft with a status FIX.** The pivotal identity, interval criterion, endpoint counterexample, refuted endpoint shortcut, quenched fragility and resilience-gap concepts track L1–L4 and label the unproved step. Its six relations use allowed types; `endpoint-counterexample refutes endpoint-shortcut` is supported by L3, and the other links describe this specific route. The source license starts with accepted `owner-own-work`. Before ingestion, change the now-stale `pending w425` review markers to reflect the scoped checks above, and attach the newer formal-claim status to any C0023 target card. No concept should become a theorem merely from this review.

## w424 verdicts

**Abstract h_n obstruction KEEP.** `h_n(p)=min(1,(2p)^n)` is continuous and nondecreasing in p, decreases in n, tends to zero for `p<1/2`, and equals one at `p=1/2`. It refutes an inference from those soft properties alone; it is not a percolation example.

**Varying-generation tree KEEP, special case.** With `b_k=8` at powers of two and `2` otherwise, `M_n=E Z_n=(2p)^n4^{1+floor(log2 n)}`. At `p=1/2`, the fresh-edge conditional binomial law gives `Q_n=E Z_n²/M_n²=Q_{n-1}+1/(b_n M_{n-1})`. The block `2^j≤k<2^{j+1}` contributes `1/(8·2^j)`, so `Q_n≤5/4` and Cauchy–Schwarz yields `P(Z_n>0)≥4/5`. Below `1/2`, `M_n≤4n²(2p)^n→0`. Thus this bounded-degree nontransitive tree has a critical jump. I independently recalculated the recurrence and sum.

**Finite-scale window KEEP.** Every open pivotal of the n-generation survival event lies on any chosen open root-to-generation-n path, hence at most n. Russo's formula gives `f_n'(p)≤n/p`, and integrating from `p_n=1/2-δ_n` yields `f_n(1/2)-f_n(p_n)≤δ_n n/p_n`. This does not provide one fixed subcritical p uniformly across n.

**w424 draft bundle: KEEP the three concepts in their stated draft scope; FIX status context before ingestion.** Its dyadic tree, narrow-window, and fixed-backward-interval statements match the checked calculations. Its four relations use allowed types and two point to the exact C0023 logical ID confirmed by read-only `CARD_EVIDENCE.json`. The quoted C0023 target card still says `current status no_resolution_found_in_documented_search as of 2026-09-07`; the later formal solved claim must be attached or the card will continue to mislead recall. The entries say `not independently reviewed`; my checks cover the tree/window arithmetic, but no second independent account has checked every bundle phrase or the formal target. Keep them as concepts until that review. The `file:///C:/...` own-work source URLs need a publication-safe locator before the public brain release.

## Own route and next referee

`ATTEMPT.md` records my stopping-cluster relay approach before either peer proof was opened. The elementary union bound loses `|A|`; removing that factor requires a selected-relay conditional estimate, which simple product independence does not provide. It is a draft partial lemma. w428 should audit it before promotion. I have not sent a mesh request because this worker's explicit forbidden-actions block bars chat/mesh sends.

NEXT: Independent rebuild/statement-fidelity audit of the pinned formal theorem, with attention to the conditioned-slack induction and comparator trust boundary; then decide C0023 retirement.
