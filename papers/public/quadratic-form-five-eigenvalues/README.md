# Quadratic forms with five large singular values have bounded densities

Yitzchak Shmalo

Let $X_1,\dots,X_n$ be independent real random variables with densities bounded by $K$, and let
$Q=X^TAX+b^TX+c$ with $A$ real symmetric. The paper proves that if the fifth singular value of $A$ is at
least $s>0$, then $Q$ has a density bounded by $270K^2/s$, uniformly in $n$, $b$, $c$, the rest of the
spectrum of $A$ and the laws of the $X_i$. Along the way it shows that $s_3(A)\ge1$ gives
$\sup_a\mathbb E|Q-a|^{-1/2}\le 77$ when $K=1$ (Proposition 7.2).

The proof combines a decay estimate for the characteristic function of $Q$ in terms of the crossing volumes
of an off-diagonal block of $A$ (Section 4), a random sign argument that, in the absence of a pivot, turns
$2m-1$ large eigenvalue moduli into $m$ large singular values of such a block (Section 6), and conditioning
on one or two coordinates when $A$ has a large diagonal entry or a large principal $2\times2$ minor
(Section 5).

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/`: numerical checks of the constants and of the main steps. Numbering follows the paper.

| Program | What it checks |
|---|---|
| `constants_exact.py` | every numerical constant in the paper, in 50-digit arithmetic (41 inequalities and identities) |
| `constants_opt.py` | the choice of the pivot thresholds $\eta=1/12$, $\zeta=1/256$ against the branches of the proof |
| `decoupling_check.py` | the sign-decoupling identities behind Lemmas 6.2-6.3 and Proposition 6.4 on random matrices |
| `verify_five.py` | Proposition 6.4 on random pivot-free matrices, a two-star example, and Monte Carlo densities against Theorem 1.1 |

The checks are numerical illustrations; the proofs in the paper do not depend on them except for the
arithmetic of the constants, which `constants_exact.py` verifies.

## Requirements

Python 3.10 or later with `numpy` and `mpmath`. Each program runs on its own, for example

    python code/constants_exact.py

and ends with a line saying that all its checks pass. `decoupling_check.py` and `verify_five.py` take longer than the other two.
