# The layer distribution of the random recursive tree and the minimum of the Poisson-weighted infinite tree

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in [paper/main.tex](paper/main.tex)).

The layer of a vertex of a tree is the number of rounds of leaf removal after which the vertex is a leaf. Stepanyants,
Krapivsky, Hartle and Krioukov (arXiv:2608.04303) showed that the limiting proportion of vertices at layer at least k
in a random recursive tree is

    lbar_k = int_0^inf s_k(y) e^(-y) dy,   s_0 = 1,   s_i(y) = 1 - exp(-int_0^y s_(i-1)),

proved e^(-k) <~ lbar_k <~ e^(-k/e), and conjectured (their Conjecture 1) that the proportion l_k at layer exactly k is
exp[-k/e - (3/(2e)) log k - O(1)].

The paper proves this with a limit in place of the O(1):

- lbar_k e^(k/e) k^(3/(2e)) -> C_* in (0, inf), and l_k e^(k/e) k^(3/(2e)) -> (1 - e^(-1/e)) C_*.

The recursion is the distribution function of the minimal position M_k in generation k of the Poisson-weighted
infinite tree, so lbar_k = E exp(-M_k); the asymptotics then follow from Addario-Berry and Ford (Ann. Appl. Probab. 2013)
and Aidekon (Ann. Probab. 2013) on that branching random walk.

It also proves the layer half of their Conjecture 2: in every finite tree the largest layer is floor(diameter / 2), and
for the random recursive tree on n vertices the largest layer is e log n - (3/2) log log n + O_P(1). The statement about
the largest rank is not treated.

## Code

[code/checks.py](code/checks.py) (Python 3, numpy) checks the deterministic description of the layer and the identity
max layer = floor(diam/2) on all 46,234 recursive trees with at most nine vertices, integrates the recursion (with the
exact values lbar_1 = 1/2 and lbar_2 = 3 - e as controls), compares it with a direct simulation of the Poisson-weighted
infinite tree, and compares it with layer counts in random recursive trees of size 200,000. Its output is in
[code/checks_output.txt](code/checks_output.txt). These computations are not used in the proofs.

SHA256SUMS.txt lists the hashes of the files.
