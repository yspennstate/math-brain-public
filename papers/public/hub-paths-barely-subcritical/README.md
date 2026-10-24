# Hub paths and the largest component of the barely subcritical configuration model

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in [paper/main.tex](paper/main.tex)).

For the configuration model with a degree sequence whose third moment converges, write eps_n = 1 - nu_n, where
nu_n = sum d_i(d_i - 1) / sum d_i tends to one from below. In his Saint-Flour notes (Open Problem 4.13), van der Hofstad
asked to show that in the barely subcritical regime (eps_n -> 0, n eps_n^3 -> infinity) the largest component has order

    max{ d_max / eps_n ,  eps_n^(-2) log(n eps_n^3) },

and predicted that it has size (d_max / eps_n)(1 + o_P(1)) when eps_n tends to zero sufficiently slowly.

The paper shows that neither statement holds in this generality. The degree sequences have vertices of degree one and
three and a polynomial number of hubs of a large common degree d, few enough that they contribute nothing to the
third moment in the limit. Paths of K hubs joined by direct edges then appear, and the component of such a path is a
tree with about K d / eps_n vertices.

- K = 2: L_1 >= (2 - eta) d_max / eps_n with high probability, for eps_n tending to zero as slowly as we like.
- K growing like sqrt(log n): L_1 >= c sqrt(log n) max{d_max / eps_n, eps_n^(-2) log(n eps_n^3)} with high probability.

In every example the degree of a uniform vertex converges in law to a variable on {1, 3} with all three moments
converging, and n eps_n^3 -> infinity. The order of L_1 in these examples is not determined.

## Code

[code/checks.py](code/checks.py) checks the exact identities used in the proof (the excess identity ell eps = 4y and the
compensated drift), the integrality and the conditions of the main theorem for both families at concrete parameters,
and the inequality Y^2 <= 2Y + D_0 together with the first two moment formulas by enumerating all 945 matchings of a
small degree sequence. Output: [code/checks_output.txt](code/checks_output.txt). The proofs do not depend on these
computations.

    python code/checks.py      # needs sympy

SHA-256 sums of the files are in [SHA256SUMS.txt](SHA256SUMS.txt).
