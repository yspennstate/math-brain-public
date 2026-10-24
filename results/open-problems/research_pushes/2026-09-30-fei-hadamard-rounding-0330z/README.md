# Multilayer Hadamard rounding cost

**Classical FEI: OPEN.** This package quantifies one attempted classicalization of the 2026 quantum FEI counterexample.

- Boolean sign-rounding after a final flat orthogonal/random-sign layer has expected control influence at least `r/(2sqrt(6)) sqrt(L/ln(4L))`
- The estimate is independent of the number of earlier data layers
- Before rounding, exact Booleanity forces a one-hot coefficient vector, whose final-layer probability is explicitly zero or `2L/2^L`
- Any exact conditional-mean Boolean lift of a scalar multiple of the real polynomial requires scaling at most `sqrt(3/L)`

[REPORT.md](REPORT.md) contains all proofs and limits. `python verify.py` reproduces [verification.json](verification.json), using exact integer Walsh and rational-log checks. It neither proves full classical FEI nor rules out other classicalization procedures. [CLAIMS.json](CLAIMS.json) preserves these scopes.
