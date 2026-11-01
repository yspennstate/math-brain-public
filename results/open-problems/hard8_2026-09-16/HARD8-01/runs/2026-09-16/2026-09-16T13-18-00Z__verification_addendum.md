# HARD8-01 checkpoint 8 — verification addendum

**Date:** 2026-09-16 UTC  
**Status:** unrestricted Černý conjecture remains **OPEN**.

This append-only note records actual GitHub creation receipts, exact-SHA readbacks, the deterministic finite execution, and one terminology clarification for checkpoint 8.

## 1. Mathematical report

Path:

`hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T13-02-47Z__report.md`

Creation commit:

`11d189e07b71b72b47c2a39b243bedadf2ec0986`

Exact-commit readback at that SHA succeeded. Returned content blob SHA:

`fadec862dc85217feebfdde004350fa655d09cba`

Therefore the mathematical report is **VERIFIED as delivered**.

### Terminology clarification

In the lead-in to Lemma 2 / Theorem 3, the report says that for every nonterminal permutation orbit one chooses an outgoing singular letter “lying on a directed arborescence of the orbit-transfer condensation toward C.” The proof needs, and should be read as using, a **directed shortest-path forest in the orbit-transfer digraph itself**: for each orbit vertex outside the terminal SCC `C`, choose the first edge on a shortest directed path to `C`. Distance to `C` strictly decreases along chosen edges, so this is acyclic and can be processed child-before-parent. The theorem and proof are unchanged; this note removes the imprecision between orbit vertices and condensation vertices without overwriting the archived report.

## 2. Exact verifier artifact

Path:

`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T13-02-47Z__terminal_scc_reduction_verifier.py`

Creation commit:

`c33bff64d6189a2fe87e844bd75d65f67cc6d004`

Exact-commit readback succeeded. Returned blob SHA:

`4ae3735e5e6a04e1098e371d5481932d4a479d81`

The verifier is standard-library Python and uses only exact finite permutations, bit-mask subset BFS, graph SCC computation, and integer arithmetic. It uses no randomness, floating point, external SAT/SMT solver, heuristic acceptance, or timeout-as-proof.

## 3. Exact output artifact

Path:

`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T13-02-47Z__terminal_scc_reduction_output.txt`

Creation commit:

`23e109926d76bc5dc29a7a0bcd3b6854bb903b2f`

Exact-commit readback succeeded. Returned blob SHA:

`53c68ceb6b51a5ccc54a6d677c9576a6b9b74cd3`

The executed output was:

```text
AUTOMATA_CHECKED 98280
SYNCHRONIZING 95232
THEOREM_CASES_VERIFIED 95232
MAX_RESET_THRESHOLD 9
SINK_SCC_SIZE_DISTRIBUTION [(1, 39360), (2, 39506), (3, 14760), (4, 1606)]
ORBIT_TRANSFER_STRONGLY_CONNECTED 76176
PROPER_TERMINAL_CORES 19056
SINGLETON_TERMINAL_CORES 9408
MIN_BOUND_SLACK 0
MAX_BOUND_SLACK 3
ALL_CHECKS_PASSED
```

The exhaustive family consists of all 98,280 four-state SI automata with one arbitrary permutation letter and an arbitrary nonempty subset of the 12 simple idempotents. The 95,232 synchronizing instances all passed the unique-terminal-SCC, invariant-core, core-synchronization, and triangular-cleanup inequalities.

## 4. Scope / review requirement

The new result is a reduction theorem for SI automata, not a proof of the unrestricted Černý conjecture. It shows that any SI counterexample reduces to an invariant terminal orbit-SCC core which is itself a counterexample, so a smallest SI counterexample must have strongly connected orbit-transfer digraph. The genuinely hard remaining SI cores are the transitive branch and multi-orbit strongly connected transfer cores.

The symbolic proof is self-reviewed only; independent mathematical review is still required before treating it as established literature.
