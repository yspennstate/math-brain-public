# PROB10-07 mathematical idea note — K_{4,n} partition transfer

Model request: GPT-6 maximum. Authenticated runtime model/effort telemetry is unavailable; actual runtime model/effort are therefore **UNVERIFIED** and no selector change is claimed.

Parent target: Grimmett–Winkler pairwise negative correlation for the uniform measure on **all forests** of a finite graph. This note is complementary to P14/HARD10-01: it does not repeat their finite graph-order census, minimal-counterexample fiber classification, or 3-terminal apex analysis.

Current PROB10-07 theorem already proved: the exact source inequality for every `K_{3,n}` by a five-state terminal-partition transfer. This run compares three materially different unexhausted continuations before code.

## Route A — deletion–contraction recurrence in n

Delete/contract one spoke incident to the newest right vertex and try to close a recurrence directly for the three pair-orbit Rayleigh differences. Advantage: source-aligned deletion–contraction. Risk: contraction creates parallel-edge/identified-terminal minors and couples several auxiliary marked polynomials, so a scalar recurrence is unlikely to close.

## Route B — four-terminal partition transfer for K_{4,n}

Process the degree-four side vertices one at a time. Future cycle legality depends only on the connectivity partition of the four fixed terminals, giving exactly Bell(4)=15 states. The unmarked transfer should have form `M=5I+N`, where `N` strictly coarsens partitions and hence `N^4=0`. Therefore total and edge-marked counts are `5^n` times explicit degree-at-most-three polynomials in `n`. Distinct edge pairs again have only three symmetry types: same right vertex, same left vertex, or vertex-disjoint. If the three exact Rayleigh differences factor into polynomials positive for every integer `n>=1`, this proves an infinite 3-connected class strictly larger in terminal width than the previous `K_{3,n}` theorem.

Critical falsification test before promoting anything: derive the 15-state transfer from the forest cycle criterion, compute all three pair-orbit differences exactly, factor them over Q, and inspect every real/integer sign condition. A single negative value is an exact source-model counterexample for that `K_{4,n}` instance and must be reported as such.

## Route C — 3-sum / four-terminal response decomposition

Try to express `K_{4,n}` as repeated gluing of a fixed four-terminal gadget and prove a Rayleigh-preserving response-cone closure. This would be more structural and potentially extend beyond complete bipartite graphs, but the P14 history shows that three-terminal environmental mixtures already create mixed-sign covariance terms. Without a new cone invariant, this route risks reproducing the known obstruction.

## Choice

Pursue **Route B** first because it is exact, finite-dimensional, nonenumerative in `n`, and has an immediate falsification criterion. Only if the exact factorization succeeds will a checker/report be written. The theorem claim, if any, will remain PARTIAL for the universal conjecture and will not alter the historical complete-order metric `9`.