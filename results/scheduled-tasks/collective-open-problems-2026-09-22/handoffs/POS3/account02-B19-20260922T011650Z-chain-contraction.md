# POS3 handoff — account02/B19 — autonomous-chain contraction adversary

Run: `20260922T011650Z-account02-B19-pos3-r12`  
Outcome: `CANDIDATE_REFUTED` for fixed-pair chain-contraction lifting; parent POS3 remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical science: `yspennstate/math-open-problems` commit `606c4a6c7a85fe290b0be72862d27678772d97cc`, report blob `14588aa0c8cfb8bff56ebd7d08b3d361f6653a90`. Verifier blob `5ba35878b1c412fb75da40cfeb66bec464e72368`, SHA-256 `cd058d6426bca31e656a044286235e9c860f599bc2a2d724cddb1d2bb29f6cfa`; output blob `8bddad37def4dc7f2e9d372af74bbf4bcccc4bea`, SHA-256 `d80f0e0f5d3a98ec4748c80bd1753bc5b40c56d2dff5dd3bf5ebbd1ecbef6ba1`.

Exact family: `P(m,r)=C_2 ⊔ C_{m+2} ⊔ C_r`, with autonomous top-chain module `M={B3,...,B_{m+2}}`. Contracting `M` gives `Q(r)=C_2 ⊔ C_3 ⊔ C_r`. Under the true uniform law, deleting the third-chain letters leaves a uniform A/B shuffle because each A/B word has the same number of C insertions. Hence

`Pr_P(A1<B1)=2/(m+4)`, while `Pr_Q(A1<B1)=2/5`.

Thus the same outside pair is balanced in the contracted quotient but unbalanced below `1/3` for every `m>=3`. Width is exactly three for `r>=1`, and the incomparability graph is connected. The concrete `m=3,r=1` certificate has `E=168` and all 17 incomparable-pair probabilities were exactly checked; seven are balanced, so this is not a POS3 counterexample.

Source consequence: account04/B19's theorem that a minimal counterexample has no proper autonomous nonchain does **not** permit a uniform fixed-pair contraction induction for the remaining chain-module branch. The missing implication must be a weighted **pair-migration/corridor** lemma: expansion may change the selected pair. In the toy family the migration is visible directly: `Pr(A1<B1)=2/7` but `Pr(A1<B2)=11/21`.

Named other-account input applied: account03/B10 report blob `388ac28e375df4e7a49f72ffbf540f362e03696e` (pinned majority-rank atom). Also used account04/B19 blob `ce30dae79d698103f026d4d871033238489b1fb1` (autonomous-module reduction).

Late compatible dependency consumed after the immutable science report: account01/B10 handoff blob `4ae042e4d6ed4e5b3641567fc30be3c4c92a0f7f` / science report blob `b33f4c52f0da12d8bcb9f30b89c9ceb1a88b3936` refutes choosing a three-chain cover that eliminates nested deleted-chain profiles. This is consistent with the present obstruction: changing cover or preserving a fixed quotient pair cannot remove the context-sensitive corridor weights. The surviving target is a signed/weighted aggregate migration theorem across nested profiles and consecutive strong-majority boundaries.

Ordinal padding `C_s ⊕ P(3,1) ⊕ C_t` preserves all 17 incomparable probabilities exactly, so no finite-size threshold repairs the fixed-pair lift.
