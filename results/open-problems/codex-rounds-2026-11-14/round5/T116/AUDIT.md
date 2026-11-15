# Final transfer and testing audit

New beyond round 4: the implementation's final argument differs from the manuscript's posterior-factorization route. [Testing.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/TraceReconstruction/Testing.lean), lines 76–121, supplies an injective family with distance to one reference bounded by sqrt(mgN^(-d))+2mgE. Lines 164–201 imply s<=2^(-g)+epsilon. PROOF.md checks this inequality twice, including success below 1/2. These are existing claims, not a new lower bound.

[Restoration.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/TraceReconstruction/Restoration.lean), lines 24–35, transfers auxiliary Hellinger and simulation bounds to m complete traces. Lines 95–137 use extra deletion probability (q-r)/(1-r) and a common per-sample kernel. The total deletion probability is q. The padding law in Testing.lean is independent and common to both hypotheses.

This audit verifies the final elementary inference conditional on the family estimate. It does not verify that the construction satisfies that estimate. No Lean checker, accepted-axiom inspection, or dependency-closure audit was performed. Sources remain on moving main; the attempted pinned URL failed.
