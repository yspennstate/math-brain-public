# Every xi-quadratic stochastic operator converges to the empty body, quadratically

Settled 2026-09-09. Ledger id E0063 (intake E, source `qso_open_2009`, Rozikov's Problem 10).

## The problem as the source states it

Rozikov, *Quadratic stochastic operators: results and open problems* (arXiv:0902.4207), Section 7.
With E_0 = E cup {0} = {0, 1, ..., m}, a set F of "females", its complement M of "males" and 0 the
"empty body", an F-QSO has coefficients

    P_{ij,k} = 1 if k = 0 and (i, j in F cup {0} or i, j in M cup {0});
             = 0 if k != 0 and the same;
             >= 0 if i in F, j in M, for every k.                                           (12)

> Theorem 5 [39]. Any F-QSO has a unique fixed point (1, 0, ..., 0) (with m zeros). Besides, for
> any x_0 in S^m, the trajectory {x(n)} tends to this fixed point exponentially rapidly.
> Problem 10. Consider a partition xi = {E_1, ..., E_q} of E, i.e. E = E_1 cup ... cup E_q,
> E_i cap E_j = empty, i != j. Assume P_{ij,k} = 0 if i, j in E_p, for p = 1, ..., q. Call the
> corresponding operator a xi-QSO. Is an analogue of Theorem 5 true for any xi-QSO?

[39] is Rozikov and Zhamilov, Math. Notes 83 (2008) 554-559. The displayed condition is the
second line of (12) with the two classes replaced by the q blocks; the corresponding operator keeps
the rest of (12): a same-block pair, or any pair containing the empty body, produces the empty body
(P_{ij,0} = 1), and a cross-block pair has arbitrary coefficients. (If pairs containing 0 were left
unconstrained, (1, 0, ..., 0) would not even be a fixed point in general, since V(e_0) = (P_{00,k})_k;
so this is the only reading under which the question makes sense.)

## Theorem

Let V be a xi-QSO with q blocks. Write x_0 for the empty-body mass and y = 1 - x_0. Then for every
x in S^m,

    1 - V(x)_0  <=  (1 - 1/q) (1 - x_0)^2.                                                     (*)

Consequently: e_0 = (1, 0, ..., 0) is the unique fixed point of V; along every trajectory
y_{n+1} <= (1 - 1/q) y_n^2, so y_n <= (1 - 1/q)^n y_0 (exponential convergence, as in Theorem 5)
and in fact y_n -> 0 quadratically (y_{n+1} <= y_n^2). So the analogue of Theorem 5 holds for every
xi-QSO, with a sharper rate; the F-QSO case is q = 2, where the constant is 1/2.

## Proof

Let e_p = sum_{i in E_p} x_i be the mass of block p, so x_0 + sum_p e_p = 1. The empty-body mass
after one step is

    V(x)_0 = sum_{i,j in E_0} P_{ij,0} x_i x_j
           >= x_0^2 + 2 x_0 (1 - x_0) + sum_p e_p^2,

the three terms being the pair (0,0), the pairs (0,i) and (i,0) with i in E, and the same-block pairs,
each of which produces 0 with probability one; cross-block pairs contribute a nonnegative amount that
is dropped. By Cauchy-Schwarz, sum_p e_p^2 >= (sum_p e_p)^2 / q = (1 - x_0)^2 / q. Hence

    1 - V(x)_0 <= 1 - x_0^2 - 2 x_0 (1 - x_0) - (1 - x_0)^2/q = (1 - x_0)^2 - (1 - x_0)^2/q,

which is (*). At a fixed point y <= (1 - 1/q) y^2 <= (1 - 1/q) y (as y <= 1), so y = 0: the fixed point
is e_0, and V(e_0) = e_0 because P_{00,0} = 1. Along a trajectory, y_{n+1} <= (1 - 1/q) y_n^2 <=
(1 - 1/q) y_n gives y_n <= (1 - 1/q)^n y_0.

## Remarks

* The bound is sharp: (*) is an equality exactly when the q block masses are equal (the
  Cauchy-Schwarz case) and no cross-block pair produces the empty body (P_{ij,0} = 0 for i, j in
  different blocks), so the constant 1 - 1/q cannot be improved as a function of the block masses.
  At the other extreme, all mass in one block sends everything to the empty body in one step.
* Nothing about the cross-block coefficients matters. The obstruction the ledger's first attempt
  recorded ("cross-block pairs may have arbitrary P_{ij,k}, so mass produced at states other than 0
  is uncontrolled and can be recycled") is real but irrelevant: the empty body absorbs at least a
  fixed fraction of the square of the off-empty mass at every step, whatever the cross-block pairs do.
* The convergence is quadratic, which is stronger than Theorem 5's "exponentially rapidly" even for
  q = 2.

## Checks

* 300 random xi-QSOs (m from 3 to 8, q from 2 to 5, Dirichlet cross-block rows of three
  concentrations), 20 random starting points each: the ratio (1 - V(x)_0) / ((1 - 1/q)(1 - x_0)^2)
  has maximum 0.9926 over the 6,000 evaluations, and the same ratio along 60-step trajectories,
  with 1 - x_0 computed as the off-empty mass, never exceeds 1; every trajectory's off-empty mass
  reaches zero (e0063.py). Two floating-point traps met on the way, both worth knowing for any QSO
  computation: V is homogeneous of degree two, so an unrenormalised iteration squares any rounding
  error in the total mass and collapses to the zero vector after x_0 has reached 1; and 1 - x_0 loses
  all precision once x_0 is within 1e-16 of 1, so the off-empty mass must be summed directly.
* Lean 4 (Prob1000/E0063.lean): the one-step inequality (*) from the mass lower bound and
  Cauchy-Schwarz (Mathlib's `sq_sum_le_card_mul_sum_sq`), the iteration bound y_n <= c^n y_0, and
  the fixed-point conclusion, on standard axioms.

## Prior art

Rozikov's own later work on xi^(s)- and xi^(as)-QSOs (Mukhamedov, Saburov, Jamilov and others,
2013-2020) uses a different notion: a partition of the set of coupled pairs, on the two-dimensional
simplex, classified into 20 and 18 conjugacy classes. Problem 10 in its literal form (blocks of
individuals, empty body absorbing same-block pairs, any m and q) was not found addressed. The
argument is the natural extension of what [39] must do for two classes and its novelty is small;
what is on record is that the question was posed as open in 2009 and has a one-line affirmative
answer with a sharper rate.
