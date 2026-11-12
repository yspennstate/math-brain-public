# Moments of level widths in conditioned Galton–Watson trees

Companion material for the paper of the same title (Y. Shmalo, October 2026). [Read the paper](paper/main.pdf).

Let T_n be a conditioned Galton–Watson tree, or more generally a simply generated tree, with n vertices, and let
l_k(T_n) be the number of its vertices at distance k from the root. Conjecture 21.1 of S. Janson, *Simply generated
trees, conditioned Galton–Watson trees, random allocations and condensation*, Probab. Surveys 9 (2012), states that
E l_k(T_n)^r → E l_k(T̂)^r for every integer r ≥ 1 and every k ≥ 1, where T̂ is the local limit of T_n, and that the
same holds for real r > 0. The paper shows that if the offspring distribution ξ is critical and E ξ^(r+1) < ∞ for a
real r ≥ 1, then the variables l_k(T_n)^r, n ≥ 1, are uniformly integrable for every k, so that
E l_k(T_n)^r → E Z_k^(r+1), where Z_k is the size of generation k of the unconditioned process. Together with the
cases that follow from Fatou's lemma, this proves the conjecture for every integer r ≥ 1, and for every real r > 0
except when 0 < r < 1 and ξ is critical with infinite variance and E ξ^(r+1) < ∞.

The proof writes the law of the first k generations of T_n as a density with respect to the unconditioned tree,
using Dwass's formula, and bounds that density with the local limit theorem: by a constant times the number of
vertices at depth k while the first k generations hold at most half of the n vertices, and by n^(3/2) times a negative
power of that number otherwise, an event whose contribution is controlled by the moment of order r + 1.

## Contents

- `paper/` the LaTeX source and the compiled PDF.
- `code/checks.py` checks of the identities and inequalities used in the proof, for five critical offspring laws:
  the formula of Lemma 2.1 for the law of the first k generations of T_n against exact enumeration of all trees with
  at most 12 vertices (k = 1, 2, 3; 35,302 comparisons), Dwass's formula for the law of the total size, and the
  conditional moment bounds of Lemma 2.3. It uses only the Python standard library, in exact rational arithmetic
  except for the moments of order 1/2, 3/2 and 5/2 in Lemma 2.3, which are checked in floating point.
  `code/checks.out` is its output.

The proof rests on the local limit theorem and uniform integrability; it has not been formalized.

## Running the checks

    python code/checks.py

Python 3.8 or later. The script runs in under a minute and ends with `ALL CHECKS PASS`.
