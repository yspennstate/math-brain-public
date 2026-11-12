# Two giant boxes in random allocations

Companion material for the paper of the same title (Y. Shmalo, October 2026). [Read the paper](paper/main.pdf).

Throw m balls into n boxes so that an allocation (y_1, ..., y_n) has probability proportional to
w_{y_1} w_{y_2} ... w_{y_n}, for a weight sequence (w_k). This is the balls-in-boxes model of S. Janson,
*Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probab. Surveys 9
(2012). When m/n → λ > ν, where ν is determined by the weights, about (λ − ν)n balls condense into boxes whose
sizes tend to infinity. For weights w_k ~ c k^(−β) with β > 2 they all go into one box: Y_(1) = (λ − ν)n + o_p(n)
and Y_(2) = o_p(n). Problems 19.42 and 19.43 of the survey (18.41 and 18.42 in the arXiv version) ask whether the
same holds for every nonincreasing weight sequence, and for every weight sequence with w_{k+1}/w_k → ∞. The paper
answers both questions in the negative.

- Theorem 1.1. Let d_0 = 0, let d_j = j^3 when j ≥ 1 is a power of two and d_j = j otherwise, and let
  w_k = exp(d_0 + ... + d_{k−1}). Then w_{k+1}/w_k ≥ e^k for k ≥ 1, and P(Y_(2) ≤ m/8) ≤ exp(−m^3/256) whenever
  m ≥ 64 is a power of two, n ≥ 2 and log(m + n) ≤ m^2/256.
- Theorem 1.2. There are nonincreasing weights, with radius of convergence 1 and 0 < ν < 0.7, such that for every
  λ > ν, along pairs (m_r, n_r) with m_r/n_r → λ, with probability tending to one each of the two largest boxes
  contains at least (λ − ν)n/13 balls.
- Corollary 1.3. For both weight sequences and infinitely many n, the simply generated random tree with n nodes has
  two nodes of outdegree of order n with probability tending to one.

In Theorem 1.1 a box of size y gains the factor e^{j^3} for every power of two j < y. For m = 2^{i+1}, the
allocation with two boxes of sizes 2^i + 1 and 2^i − 1 has at least e^{m^3/128} times the weight of any allocation
in which at most one box exceeds m/8 (Lemma 2.2), and this outweighs the at most (m + n)^m allocations. The weights
of Theorem 1.2 are constant on the dyadic blocks [2^j, 2^{j+1}): w_k = e^{−g(j)}, where g(j) = 3j except that at
each of a sparse sequence of cliffs J_1 < J_2 < ... it jumps to 6J_r + 4 and stays there until 3j catches up. When
the excess is comparable to the block of a cliff, it is cheaper to share it between two boxes below the block than
to put it into one box above it.

## Contents

- `paper/` the LaTeX source and the compiled PDF.
- `code/checks.py` checks of the lemmas and of both theorems. For the weights of Theorem 1.1: Lemma 2.1 for every
  y ≤ 4096, the exact maxima behind Lemma 2.2 for m = 8, 16, ..., 8192 by dynamic programming, and the exact
  log P(Y_(2) ≤ m/8) against the bound in the proof for eight pairs (m, n) with m ≤ 256. For the weights of
  Theorem 1.2: Lemma 3.1 on 36 cliff sequences, ν and σ², the pair count in the proof of Lemma 4.2, Lemma 4.1
  against exact probabilities in 120 cases, and the law of Y_(2) at the cliffs J = 8, 9, 10, for allocations and
  for trees with up to 4,092 nodes. Five negative controls (weights without the spikes, twice; weights without the
  cliffs; a cliff spacing that breaks Lemma 3.1; Lemma 4.1 without its truncation) are asserted to fail. It uses
  only the Python standard library; the arithmetic checks are exact, and the probabilities are computed from
  generating functions in double precision, as sums of positive terms where they are compared with a bound.
  `code/checks.out` is its output. In part B3 the script's B and N(s) are the H and κ(s) of the paper.

The proofs have not been formalized.

## Running the checks

    python code/checks.py

Python 3.8 or later. The script runs in under half an hour and ends with `ALL CHECKS PASS`.
