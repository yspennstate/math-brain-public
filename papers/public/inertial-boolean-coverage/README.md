# First-order coverage asymptotics for the inertial Boolean model

Yitzchak Shmalo, 16 November 2026. Zenodo: https://doi.org/10.5281/zenodo.24271165

Points of a homogeneous Poisson process in R^d move along straight lines with independent random velocities V, and each carries a closed ball of radius r. Let C(LK) be the first time at which the region swept by the balls contains the dilated compact set LK. Konstantopoulos (arXiv:1407.6834, Open problem 1) asked for the asymptotics of this coverage time in the inertial case; the Brownian case was treated by Peres, Sinclair, Sousi and Stauffer (PTRF 156, 2013). Put a = lambda * omega_{d-1} * r^{d-1} * E|V|, where omega_j is the volume of the unit ball of R^j. If d >= 2, the mean speed is finite and positive, and K has nonempty interior, then C(LK)/log L tends to d/a almost surely and in L^1, with no other assumption on the velocities; for targets of Minkowski dimension alpha > 1 the limit is alpha/a. Under the tail condition (log h) E[|V|; |V| > h] -> 0 the limit alpha/a holds for every alpha and every d >= 1. In dimension one the condition cannot be dropped: for one speed law with finite mean, C([0,L])/log log L converges in law to an exponential variable.

## Files

- `main.tex`, `main.pdf`: the paper.
- `CREDITS.md`: which statements are known, adapted or new, and whose work they rest on.
- `checks/point_law_check.py`: simulates the probability that a point of the plane is still uncovered at time t and compares it with exp(-lambda(pi r^2 + 2 r t)) from Lemma 2.1. Needs Python 3 and NumPy; runs in under a minute. Its output is in `checks/output.txt`.

## License

The paper is licensed CC BY 4.0 and the code MIT.
