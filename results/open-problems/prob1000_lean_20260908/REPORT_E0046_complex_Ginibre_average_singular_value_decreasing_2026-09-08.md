# The expected average singular value of a complex Ginibre matrix decreases in the dimension

Proved independently 2026-09-08 (the complex half of the conjecture); found the same evening to have been
settled in the literature in 2026, see Prior art. Ledger id E0046. Source: Bandeira, *Ten
lectures and forty-two open problems in the mathematics of data science* (2015), Open Problem 1.2,
attributed there to Bandeira, Kennedy and Singer [BKS13a].

## The problem as the source states it

> Open Problem 1.2 (Monotonicity of singular values [BKS13a]). Consider the setting above but with
> p = n, then X in R^{n x n} is a matrix with iid N(0,1) entries. Let sigma_i(X/sqrt n) denote the
> i-th singular value of X/sqrt n, and define alpha_R(n) := E[(1/n) sum_i sigma_i(X/sqrt n)] as the
> expected value of the average singular value of X/sqrt n. The conjecture is that, for every n >= 1,
> alpha_R(n+1) >= alpha_R(n). Moreover, for the analogous quantity alpha_C(n) defined over the
> complex numbers, meaning simply that each entry of X is an iid complex valued standard gaussian
> CN(0,1), the reverse inequality is conjectured for all n >= 1: alpha_C(n+1) <= alpha_C(n).

Both sequences tend to 8/(3 pi) = 0.84883, the first absolute moment of the quarter-circle law.

## Theorem

For every n >= 1, alpha_C(n+1) < alpha_C(n). The real case is not treated here.

## Proof

**1. An exact formula.** For X with iid CN(0,1) entries (E|X_ij|^2 = 1), W = X X^* is a complex
Wishart matrix in the square case, and its eigenvalues form the Laguerre unitary ensemble with weight
e^{-x} on (0, infinity). Its one-point density is the Christoffel-Darboux sum
rho_n(x) = e^{-x} sum_{k=0}^{n-1} L_k(x)^2, with L_k the Laguerre polynomials (Mehta, Ch. 19). Since
sigma_i(X/sqrt n) = sqrt(lambda_i(W))/sqrt n,

    alpha_C(n) = n^{-3/2} E tr W^{1/2} = n^{-3/2} sum_{k=0}^{n-1} a_k,     a_k := integral_0^infinity x^{1/2} e^{-x} L_k(x)^2 dx.

**2. A closed form for a_k.** From the Laguerre generating function sum_k L_k(x) t^k = (1-t)^{-1}
exp(-xt/(1-t)) and the Mellin transform of e^{-cx},

    sum_{m,n} t^m u^n integral x^{1/2} e^{-x} L_m L_n dx = Gamma(3/2) (1-t)^{1/2} (1-u)^{1/2} (1-tu)^{-3/2},

and reading the diagonal coefficient,

    a_k = Gamma(3/2) r_k,     r_k = sum_{m=0}^{k} (3/2)_m / m! . C(1/2, k-m)^2,

with (3/2)_m the rising factorial and C(1/2, j) the binomial coefficient of (1+x)^{1/2}. So
r_0 = 1, r_1 = 7/4, r_2 = 145/64, r_3 = 687/256, r_4 = 49881/16384, and a 30-digit quadrature of the
defining integral agrees with each of these (e0046.py, e0046b.py).

**3. The recurrence.** Write S_n := sum_{k<n} r_k, so alpha_C(n) = Gamma(3/2) S_n / n^{3/2}. The
generating function of r_k is R(t) = (1-t)^{-3/2} Q(t) with Q(t) = sum_j C(1/2,j)^2 t^j =
2F1(-1/2, -1/2; 1; t), which satisfies the hypergeometric equation t(1-t) Q'' + Q' - Q/4 = 0.
Substituting Q = (1-t)^{3/2} R and clearing the common factor gives

    t (1-t)^2 R'' + (1-t)(3t-1) R' + (4t-7)/4 . R = 0,

and since sum_{n>=0} S_n t^n = t R(t)/(1-t), the same substitution gives

    t^2 (1-t)^2 S'' + t (1-t)(3t+1) S' + (4t^2 - 3t + 4)/4 . S = 0.

Reading off coefficients (e0046e.py, symbolic, and checked exactly on the rationals r_0..r_24):

    (k+1)^2 r_{k+1} = (2k^2 + 2k + 7/4) r_k - k^2 r_{k-1},
    n^2 S_{n+1}     = (2n^2 + 3/4) S_n - n^2 S_{n-1},          n >= 1,   S_1 = 1, S_2 = 11/4.

**4. The ratio recursion.** Put rho_n := S_{n+1}/S_n > 0. Dividing the S-recurrence by n^2 S_n,

    rho_n = 2 + 3/(4 n^2) - 1/rho_{n-1},     rho_1 = 11/4.

The claim alpha_C(n+1) < alpha_C(n) is S_{n+1}/S_n < ((n+1)/n)^{3/2}, i.e. rho_n < f(n) with
f(n) := (1 + 1/n)^{3/2}.

**5. The elementary inequality.** For 0 <= x <= 1,

    (1+x)^{3/2} + (1-x)^{3/2} >= 2 + (3/4) x^2,     with equality only at x = 0.               (*)

Proof: put u = sqrt(1+x), v = sqrt(1-x), s = u + v. Then u^2 + v^2 = 2, uv = (s^2 - 2)/2,
x^2 = 1 - u^2 v^2, and the left side is u^3 + v^3 = s(u^2 - uv + v^2) = 3s - s^3/2. So
(*) reads 3s - s^3/2 - 2 - (3/4)(1 - (s^2-2)^2/4) >= 0, and the left side factors as
(s - 2)^2 (3 s^2 + 4 s - 8)/16. Since s^2 = 2 + 2uv >= 2, the second factor is at least
6 + 4 sqrt 2 - 8 > 0, and (*) follows, with equality iff s = 2 iff x = 0.

**6. Induction.** rho_1 = 11/4 < 2^{3/2} = f(1). Suppose rho_{n-1} < f(n-1), n >= 2. Since
rho -> 2 + 3/(4n^2) - 1/rho is increasing,

    rho_n < 2 + 3/(4n^2) - 1/f(n-1) = 2 + 3/(4n^2) - (1 - 1/n)^{3/2} < (1 + 1/n)^{3/2} = f(n),

the last step being (*) at x = 1/n, where it is strict. Hence rho_n < f(n) for all n >= 1, which is
the theorem.

## Remarks

* The inequality is tight to second order: rho_n = 3/(2n) + 3/(8n^2) + O(n^{-3}) on both sides,
  and numerically the margin f(n) - rho_n is about 0.18/n^3 (n = 10: 1.8e-4; n = 20: 2.6e-5;
  n = 40: 3.1e-6). That is why no bound on the finite-n quarter-circle correction could have
  proved it; the recursion for the ratio is what makes the second-order terms cancel exactly.
* The proof gives the same for any weight: the argument only used that S_n satisfies an
  n^2 S_{n+1} = (2n^2 + c) S_n - n^2 S_{n-1} recurrence with c <= 3/4 and rho_1 <= 2^{3/2}.
* The real case, alpha_R increasing, is Bandeira's other half and is not touched: the Laguerre
  orthogonal ensemble's one-point function is a sum of squares of Laguerre polynomials plus a
  boundary term, and its half-integer moment does not reduce to a two-term recurrence in the same
  way. Numerically alpha_R(n) is increasing: alpha_R(1) = sqrt(2/pi) = 0.79788, alpha_R(2) = 0.81020 (exact
  quadrature of the 2 x 2 real Wishart density), and Monte Carlo (e0046r.py, 2e6/n^2 samples each)
  gives 0.818, 0.824, 0.831, 0.835, 0.839, 0.842, 0.846 (+- 0.0004) at n = 3, 4, 6, 8, 12, 20, 40, rising
  toward 0.84883. The two sequences approach the same limit from opposite sides, as the conjecture says.

## Checks

* a_k by 30-digit quadrature vs the closed form: exact agreement k = 0..8.
* Both recurrences: derived symbolically from the two ODEs and verified exactly on the rational
  values for k <= 22 (e0046e.py).
* alpha_C(n) for n = 1..40 decreasing, converging to 0.84890 at n = 40 against the limit 0.84883
  (e0046.py); alpha_C(1) = sqrt(pi)/2, the mean of a Rayleigh variable, as it must.
* Lean 4 (Prob1000/E0046.lean): the inequality (*) in the algebraic form with u, v, and the
  induction from the ratio recursion to rho_n <= f(n), certified; the recurrences themselves enter
  as hypotheses (they are the symbolic computation above).

## Prior art (checked after the proof, the same evening)

Both halves of the conjecture were settled in 2026, and the intake's status search of 2026-09-08 missed
them. Ondrej Hutnik, *The average singular value of a real square Gaussian random matrix strictly
increases with dimension*, arXiv:2608.12151 (12 August 2026), proves alpha_R(N+1) - alpha_R(N) >
1/(1000 N^2) and cites, for the complex half, his companion preprint *The average singular value of a
complex Gaussian random matrix strictly decreases with dimension* (2026), which builds on the
recurrence of L. D. Abreu, *A recurrence relation for the average singular value of a complex Gaussian
random matrix*, Complex Anal. Oper. Theory 20 (2026) 159. Abreu's 2016 preprint arXiv:1606.00494
claiming the complex decrease was withdrawn in 2023 (its Lemma 1 was wrong); his 2026 note reduces
the complex claim to R(d) < 0 for a difference of two Laguerre integrals and calls that inequality
still open at the time of writing.

So the theorem above is a rediscovery. What may still be of use is the route: a two-term recurrence for
the PARTIAL SUMS S_n rather than for alpha itself, which turns the claim into the ratio recursion
rho_n = 2 + 3/(4n^2) - 1/rho_{n-1} and a one-line induction from the inequality (*). Whether Hutnik's
argument is the same in substance I have not checked; his real-case paper describes "a delicate
analysis argument starting from the recurrence relation". The Lean file certifies the induction and
the inequality; the recurrence is a symbolic computation.
