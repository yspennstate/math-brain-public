# Negative edge correlation for weighted spanning forests of complete graphs

Yitzchak Shmalo

Let $P_t$ be the arboreal gas on the complete graph $K_n$, the probability measure on acyclic
edge sets $F$ proportional to $t^{|F|}$. The paper proves that for every $n$ and every $t>0$,
any two distinct edges $e,f$ satisfy

$$P_t(e,f\in F) < P_t(e\in F)\,P_t(f\in F).$$

The case $t=1$ (the uniform random forest) is due to Gupta. Edges that share a vertex are handled
through the real-rootedness of a vertex's degree polynomial. Disjoint edges are handled by a
Riccati equation for a ratio of forest counts and a barrier argument.

## Contents

- `paper/forests_kn.tex`, `paper/forests_kn.pdf`: the paper.
- `code/check_c017.py`: symbolic check (sympy) of the polynomial identities used in the
  barrier argument, and of the ordering of the relevant roots for n = 7, ..., 40.
- `code/kn_exact_certificate.py`: an independent exact check of the same algebra with
  python-flint integer polynomials, including the base cases n = 4, 5, 6.
- `code/brute_kn.py`: exact enumeration of forests of K_n for n = 3, ..., 7, comparing both
  sides of the inequality as polynomials in t.

Requirements: Python 3, `sympy`, `python-flint`, `psutil`. Each script prints `ALL OK` or `PASS`.
