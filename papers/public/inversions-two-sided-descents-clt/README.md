# A joint central limit theorem for inversions and two-sided descents

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

Let π be a uniform random permutation of n elements, let I(π) be its number of inversions and let T(π) = D(π) + D(π⁻¹) be the number of descents of π plus the number of descents of π⁻¹. The paper shows that I and T, centred and scaled by their standard deviations, converge jointly to a pair of independent standard normal variables, with the Wasserstein distance of every unit linear combination to the standard normal law at most a constant times n^(-1/2). The same holds with T replaced by any statistic that adds a fixed function over all windows of k consecutive positions of π and of π⁻¹, provided its variance grows linearly, and the triple (I, D(π), D(π⁻¹)), standardized in the same way, converges to a standard normal vector in R³. Exactly, Cov(I, T) = (n-1)/2. The proof replaces I by its Hoeffding projection on the point process that generates π and applies Chatterjee's normal approximation by interaction graphs, as Chatterjee and Diaconis did for T alone.

This answers the question raised by P. Dörr (arXiv:2404.06598, Section 5) of the joint asymptotic normality of T with the inversion count.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/enumerate.py`: checks the exact covariance and variance formulas used in the paper (Var I, Var D, Cov(D(π), D(π⁻¹)), Cov(I, D), Cov(I, T), Var T) by enumerating all permutations of n elements for n = 2, ..., 8, in exact rational arithmetic. Run `python code/enumerate.py`; it needs only the Python standard library and takes under a minute.
- `SHA256SUMS`: sha256 of each file above.
