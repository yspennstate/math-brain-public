# Comparator statement audit

Opened [TraceReconstruction.lean](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/TraceReconstruction.lean), lines 9–77.

Words are functions `Fin n → Bool`. A mask retains indices in increasing order; its weight multiplies q for deletions and 1-q for retentions. The observation is only the resulting Boolean list. Summing over masks gives its full distribution, including length.

An estimator assigns each observed sample tuple a nonnegative distribution over all length-n words. Success averages over independent masks. Thus randomized estimators are unrestricted, and the channel supplies ordinary complete traces. The infimum defining sample complexity is over integer sufficient budgets, with infinity for no budget.

The quantitative theorem has the same sequence hypotheses and exponent as the manuscript. The fixed-channel theorem quantifies over every positive polynomial exponent and every fixed success probability in (0,1]. No model or quantifier mismatch was found.

The three comparator theorem bodies contain `sorry`. This file supplies statements, not checked proofs. That observation does not establish a gap in the separate implementation. Neither the implementation nor its comparator check was run here.
