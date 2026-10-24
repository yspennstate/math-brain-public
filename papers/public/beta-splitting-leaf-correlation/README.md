# Correlation of leaf heights at mesoscopic separation in the critical beta-splitting tree

Yitzchak Shmalo

In the critical beta-splitting random tree on n leaves, closed into a cycle, take a uniformly random leaf and the leaf r places further round the cycle. Aldous and Janson (The critical beta-splitting random tree II: overview and open problems, arXiv:2303.02529, Section 3.9, Open Problem 1) asked for a proof that the correlation of the two leaf heights tends to 1 - α when log r_n / log n tends to α in [0, 1]. The paper proves that, uniformly in 1 ≤ r ≤ n/2, the covariance of the two heights is σ² log(n/r) + O(√log n) and the variance of one height is σ² log n + O(√log n), with σ² = 2ζ(3)/ζ(2)³. So the correlation equals 1 - log r / log n + O((log n)^(-1/2)), which answers the question. The proof uses a potential of each leaf's position in its clade that decreases at rate ζ(2) up to square-integrable errors, and compares the two martingales it produces up to the cut that separates the two leaves.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/checks.py`: the computer checks of Section 6 (exact rational checks of the common-clade chain, the drift and error bounds in double precision, an exact recursion for the mean separation time, the moment of Lemma 4.1 on a grid, and a Monte Carlo simulation of the two lineages). Its output is `code/checks_output.txt`; the script exits with a nonzero code if any check fails.
- `lean/PairIdentities.lean`: Lean 4 / Mathlib proofs of the algebraic identities and inequalities listed in Section 6. The compiler output is `lean/lean_output.txt`.

## Running the checks

```
python code/checks.py
```

Requires Python 3 with NumPy; it runs in under a minute. The simulation uses a fixed seed, so the output is reproduced exactly.
