# E0065 - regularity thresholds for quadratic stochastic operators (Rozikov, Problem 12)

Date: 2026-09-09. Source: Ganikhodzhaev and Rozikov, "Quadratic stochastic operators: results and open
problems", arXiv 0902.4207 (source_id qso_open_2009), Section 9, PDF p. 7.

## 1. The problem as the source states it

Verbatim (text.txt lines 318-328, display fraction restored):

> 9 Regularity of QSO
> In [17] the authors consider an arbitrary QSO V : S^{m-1} -> S^{m-1} with matrix P = (P_{ij,k}) and
> studied the problem of finding the smallest alpha_m such that the condition P_{ij,k} > alpha_m implies
> the regularity of V.
> Theorem 7. [17] 1) If P_{ij,k} > 1/(2m) then V is regular.
> 2) alpha_2 = (1/2)(3 - sqrt 7).
> Problem 12. Find exact values of alpha_m for any m >= 3.

The operator is the source's eq. (4)-(5): V(x)_k = sum_{i,j=1}^m P_{ij,k} x_i x_j, summed over ALL
ordered pairs, with P_{ij,k} >= 0, P_{ij,k} = P_{ji,k}, sum_k P_{ij,k} = 1. "Regular" is the usual
notion in this literature: every trajectory converges. Reference [17] is Ganikhodzhaev and Sarymsakov,
Dokl. Akad. Nauk UzSSR 1988 no. 11, 5-6, in Russian, two pages; I could not obtain it.

The ledger row transcribes the source faithfully (it writes lambda_m for alpha_m).

## 2. Findings

Throughout, alpha_m = sup { min_{ijk} P_{ij,k} : V is not regular }, which is the same thing as the
smallest alpha such that P_{ij,k} > alpha for all i,j,k forces regularity.

Theorem A (upper bound, all m >= 2). If min P_{ij,k} > ((m+1) - sqrt(m^2+1)) / (2m) then V is regular.
So alpha_m <= ((m+1) - sqrt(m^2+1))/(2m) < 1/(2m). For m = 3 this is (4 - sqrt 10)/6 = 0.13962,
against the source's 1/6 = 0.16667.

Theorem B (lower bound, all m >= 3). For every alpha < (1 - 1/sqrt(m+1)) / (2m) there is a QSO with
min P_{ij,k} = alpha that has a 2-cycle, hence is not regular. So alpha_m >= (1 - 1/sqrt(m+1))/(2m).
For m = 3 this is 1/12 = 0.08333.

Corollary. 1/12 <= alpha_3 <= (4 - sqrt 10)/6, and for every m >= 3

    (1 - 1/sqrt(m+1)) / (2m)  <=  alpha_m  <=  ((m+1) - sqrt(m^2+1)) / (2m),

so 2 m alpha_m -> 1: the source's bound 1/(2m) is asymptotically sharp to first order, and
alpha_m = 1/(2m) - O(m^{-3/2}). The earlier attempt's guess that alpha_m behaves like 0.354/m is wrong.

Theorem C (the m = 2 data point is off by a factor of two). In the source's normalisation (4)-(5),
alpha_2 = (3 - sqrt 7)/4 = 0.08856, not (3 - sqrt 7)/2 = 0.17712. Both halves are proved below; the
algebraic core of the upper half and the explicit m = 3 two-cycle are certified in Lean (U_E0065.lean,
compiled clean, axioms propext / Classical.choice / Quot.sound only).

Remark on the discrepancy. (3 - sqrt 7)/2 is exactly twice the value forced by the source's own
convention. If the intended hypothesis in [17] were "2 P_{ij,k} > alpha", the m = 2 value would read
(3 - sqrt 7)/2, but then the general bound would read 1/m, not 1/(2m); if instead the general bound were
meant as "P_{ij,k} > 1/(4m)", Theorem B refutes it for m >= 4 (the construction has min P = 0.069 > 1/16
at m = 4 with a 2-cycle). No single reading of the coefficients makes both parts of Theorem 7 correct.
Under the literal reading, part 1 is correct and part 2 is not.

## 3. Proofs

### 3.1 The one-step identity

For x, y in the simplex, using P_{ij,k} = P_{ji,k},

    V(x)_k - V(y)_k = sum_i (x_i - y_i) sum_j P_{ij,k} (x_j + y_j) = (A(z)(x - y))_k,   z = x + y,

where A(z)_{ki} = sum_j P_{ij,k} z_j has column sums sum_j z_j = 2. Let M = A(z)/2, column stochastic.
For a sum-zero vector v, ||M v||_1 <= delta(M) ||v||_1 with the Dobrushin coefficient
delta(M) = max_{i,i'} (1/2) ||M_{.i} - M_{.i'}||_1. Column i of M is the mixture sum_j (z_j/2) P_{ij,.},
and columns i and i' share the summand P_{ii',.}, with weights z_{i'}/2 and z_i/2 respectively.
Bounding delta(M) by 1 - m alpha without using the shared summand gives the source's 1/(2m).

### 3.2 Theorem A

Every V maps the simplex into D = { x : x_i >= alpha for all i }, because V(x)_k >= alpha (sum x_i)^2.
Take x, y in D, so z_i >= 2 alpha. Let w = min(z_i, z_{i'})/2 >= alpha. Subtract w P_{ii',.} from both
columns i and i': what remains are two non-negative vectors mu, nu of equal mass 1 - w whose every
entry is at least alpha (1 - w) (each remaining summand has entries >= alpha times its weight). Hence
(1/2)||mu - nu||_1 = (1 - w) - sum_k min(mu_k, nu_k) <= (1 - w)(1 - m alpha), and

    ||V(x) - V(y)||_1 <= 2 (1 - alpha)(1 - m alpha) ||x - y||_1     for x, y in D.

If kappa = 2(1 - alpha)(1 - m alpha) < 1, V is a contraction of the closed set D into itself, so it has a
unique fixed point p in D, every trajectory started in D converges to p, and every trajectory enters D
after one step. Every fixed point lies in V(S), a subset of D, so p is the only fixed point in the
simplex. kappa < 1 is 2 m alpha^2 - 2(m+1) alpha + 1 > 0, i.e. alpha > ((m+1) - sqrt(m^2+1))/(2m)
(the smaller root; the larger root exceeds 1/m).

### 3.3 Theorem B: the swap construction

Fix m >= 3 and 0 < alpha < 1/(2m). Let sigma be the transposition (1 2). Put

    P_{22,1} = P_{2j,1} = 1 - (m-1) alpha   (j = 3..m),
    P_{11,2} = P_{1j,2} = 1 - (m-1) alpha   (j = 3..m),
    P_{12,k} = P_{jj',k} = alpha + (1 - m alpha)/(m-2)   for k, j, j' in {3..m},
    every other coefficient = alpha.

Each (i,j) row sums to 1, all entries are >= alpha with equality attained, so min P = alpha (as
alpha <= 1/m). Writing s = x_3 + ... + x_m,

    V(x)_1 = alpha + (1 - m alpha)(x_2^2 + 2 x_2 s),    V(x)_2 = alpha + (1 - m alpha)(x_1^2 + 2 x_1 s),

and V commutes with sigma and with every permutation of {3..m}. A point with V(x) = sigma x and
x_1 != x_2 is a 2-cycle (V^2 x = sigma V x = sigma sigma x = x). Take x_3 = ... = x_m = s/(m-2); then
V(x)_k = x_k for k >= 3 holds automatically (those coordinates are equal by symmetry and sum to
1 - x_1 - x_2), and V(x) = sigma x says that x_1 and x_2 are both roots of

    (1 - m alpha) t^2 + (2 (1 - m alpha) s - 1) t + alpha = 0.

Sum of roots = 1 - s forces s = m alpha/(1 - m alpha), the product is alpha/(1 - m alpha), and the
discriminant is

    4 m (m+1) alpha^2 - 4 (m+1) alpha + 1,

positive exactly when alpha < (1 - 1/sqrt(m+1))/(2m) (or alpha above the larger root, which is > 1/(2m)).
For such alpha the roots are real, distinct and positive (positive sum (1 - 2 m alpha)/(1 - m alpha) and
positive product), s is in (0,1), so x is an interior point of the simplex and {x, sigma x} is a 2-cycle.

For m = 3 the coefficients are P_{22,1} = P_{23,1} = P_{11,2} = P_{13,2} = P_{12,3} = P_{33,3} = 1 - 2 alpha,
all others alpha; the 2-cycle is

    x_{1,2} = ((1 - 6 alpha) +- sqrt(48 alpha^2 - 16 alpha + 1)) / (2 (1 - 3 alpha)),   x_3 = 3 alpha/(1 - 3 alpha),

and 48 alpha^2 - 16 alpha + 1 = (12 alpha - 1)(4 alpha - 1) > 0 iff alpha < 1/12. At alpha = 1/12 the two
roots merge into the fixed point (1/3, 1/3, 1/3), where the Jacobian on the tangent plane has eigenvalues
-1 and 0: a period-doubling of the uniform fixed point. Numerically the 2-cycle is attracting below
1/12 (supercritical), and just above 1/12 random orbits converge to the fixed point.

Where the construction came from: a numerical search (m3_local.py) over all m = 3 operators for the
largest alpha at which some fixed point has a tangent-plane eigenvalue of modulus 1 returned exactly this
operator at alpha = 1/12 (eigenvalue -1), a rotation-type operator at alpha = 0.048 (complex pair), and
nothing better. The lumped construction (state 1 against a block of m-1 identical states, which reduces
to the m = 2 map, lumped_bound.py) gives only ((m+1) - sqrt(m^2+m+1))/(2m) = 0.0657 at m = 3.

### 3.4 Theorem C: m = 2

On S^1 the operator is the quadratic f(p) = a p^2 + 2 b p (1-p) + c (1-p)^2 with a = P_{11,1},
b = P_{12,1}, c = P_{22,1}, and P_{ij,k} > alpha means a, b, c in (alpha, 1 - alpha).

Two classical facts about interval maps. (i) A continuous self-map of an interval has every orbit
convergent iff it has no periodic point of period 2 (Coppel 1955). (ii) A real quadratic polynomial is
affinely conjugate to z^2 + c; it has a real 2-cycle iff c < -3/4 iff its alpha-fixed point has
multiplier < -1; and the 2-cycle lies in every invariant interval containing that fixed point (on an
invariant J = [u, v] around a fixed point with multiplier < -1, f^2(u) >= u while f^2(x) < x just left of
the fixed point, so f^2 has a fixed point in [u, p), which cannot be the other fixed point beta because
J lies in [-beta, beta] and beta is the larger fixed point). Degenerate (affine) f with slope -1 forces
a = 0, so it does not occur for alpha > 0. Hence, for alpha > 0,

    V on S^1 is not regular  iff  some fixed point p in [0,1] has f'(p) < -1.

Lower half. a = b = alpha, c = 1 - alpha. The resultant of f(p) - p and f'(p) + 1 in p is
(2 alpha - 1)(8 alpha^2 - 12 alpha + 1) (m2_sympy.py), so f'(p) < -1 exactly for alpha < (3 - sqrt 7)/4,
and then a 2-cycle exists. Directly: at alpha = 0.08 the orbit settles on {0.2250, 0.5845}.

Upper half (certified as m2_slope_bound). With s = a p + b q, t = b p + c q, q = 1 - p: the fixed
point equation is p = s p + t q and f'(p) = 2(s - t) = 2(s - p)/q. So f'(p) <= -1 gives s <= (3p-1)/2 and
then t = p(1-s)/q >= 3p/2. The shared coefficient b satisfies (t - (1-alpha) q)/p <= b <= (s - alpha p)/q,
which after substituting the two bounds reads (1 - alpha) >= (4 - 2 alpha) p q; and b in [alpha, 1-alpha]
confines p to [(2 alpha + 1)/3, 2(1 - alpha)/3], on which p q >= (2 alpha + 1)(2 - 2 alpha)/9. Together
9 >= 4 (2 - alpha)(2 alpha + 1), i.e. 8 alpha^2 - 12 alpha + 1 >= 0, i.e. alpha <= (3 - sqrt 7)/4.

So alpha_2 = (3 - sqrt 7)/4 in the convention of eq. (4). I also checked the reading in which the
coefficient of x_1 x_2 itself (2b) is what is bounded below: that gives 1 - 2/sqrt 5 = 0.1056, not
(3 - sqrt 7)/2 either.

## 4. What is not done

* alpha_3 is bracketed, 1/12 <= alpha_3 <= (4 - sqrt 10)/6, not computed. Closing the gap needs either a
  better global argument (a metric adapted to the shared summand, or contraction of V^2) or a
  non-regular operator with min P above 1/12 arising from a global mechanism (a saddle-node 2-cycle away
  from the fixed point, or an invariant curve). A Newton search for 2-cycles in 1500 random m = 3
  operators with min P in (1/12, 0.1396) found none (verify_iter.py), which is weak evidence that the
  truth is at the lower end.
* Whether the swap construction is the extremal local mechanism for every m >= 3 is only checked
  numerically at m = 3; for m >= 4 the fixed point of the construction is not uniform and other
  arrangements of the bystander mass may do slightly better.
* Reference [17] itself was not seen; the factor-two discrepancy is stated against the survey's printed
  convention, which is the only one available to me.
* The two interval-map facts in 3.4 are quoted, not re-proved.

## 5. Checks

* m2_calibrate.py (L-BFGS-B over all a, b, c) and m2_sympy.py (exact resultant) independently give
  (3 - sqrt 7)/4 = 0.0885621722 for the m = 2 threshold. verify_all.py: 40,000 random operators with
  min P > (3 - sqrt 7)/4 have every fixed point with f'(p) >= -0.9507 > -1. m2_probe.py: the extremal
  family a = b = alpha, c = 1 - alpha has f'(p) = -1.023 at alpha = 0.08 (orbit on a 2-cycle) and
  f'(p) = -0.970, -0.917, -0.839, -0.786 at alpha = 0.10, 0.12, 0.15, 0.17 with convergent orbits: the
  printed value (3 - sqrt 7)/2 = 0.177 would require non-regular operators with min P near 0.177.
* m3_local.py (SLSQP, random restarts, bisection in alpha; output in m3_local_output.txt) finds the
  period-doubling threshold at m = 3 in [0.08333, 0.08334] with exactly the swap operator; the
  Neimark-Sacker threshold at 0.048.
* verify_all.py: for (m, alpha) = (3, 0.08), (3, 0.083), (4, 0.066), (4, 0.069), (5, 0.058) the explicit
  point satisfies V(x) = sigma x to machine precision, and fsolve on V^2(x) = x from 300 random starts
  finds exactly the two points of that 2-cycle and nothing else.
* verify_iter.py (renormalised iteration, since sum V(x) = (sum x)^2 amplifies rounding
  double-exponentially over 20,000 steps): below the threshold orbits land on the 2-cycle, just above it
  (3, 0.0834) and (4, 0.0692) they converge to the fixed point; 300 random m = 3 operators with
  min P = 0.14, just above the new upper bound, converge to a fixed point.
* Lean 4 / Mathlib (lean_compile_output.txt): U_E0065.lean certifies m2_slope_bound (the inequality of
  3.4), m3_two_cycle_identity (V(x) = sigma x for the stated sum, product and x_3) and
  m3_two_cycle_exists (distinct positive roots for 0 < alpha < 1/12). One compile, no errors, only
  deprecation warnings; every theorem depends on propext, Classical.choice, Quot.sound only.

## 6. Prior art

WebSearch (the session budget ran out after these): "quadratic stochastic operator" regularity threshold
"1/(2m)"; Ganikhodzhaev Sarymsakov "simple criterion for regularity"; "results and open problems"
Problem 12 regularity alpha_m; "(3-sqrt7)/2" quadratic stochastic operator; Saburov positive
coefficients regular; the 2011 IDAQP survey (Ganikhodzhaev, Mukhamedov, Rozikov); Lyubich's book.
Fetched: Zada and Shah, "On dynamics of quadratic stochastic operators: a survey", Surveys in Math.
and its Appl. 12 (2017), which restates Theorem 7 verbatim and lists alpha_m for m >= 3 as open;
Mukhamedov and Saburov, arXiv 1111.3101 (Volterra case only); arXiv API listings for "quadratic
stochastic operator" + regular (seven papers, none on coefficient lower bounds). Nothing later gives a
value or a bound for m >= 3, and nothing questions the m = 2 value. Saburov, "On regularity of
diagonally positive quadratic doubly stochastic operators" (Results Math. 2017), is about the doubly
stochastic class under a different hypothesis. Search phrase that found the 2017 survey: "quadratic
stochastic operators" "results and open problems" Problem 12.

## 7. The strongest case that I am wrong

The m = 2 correction contradicts a printed theorem, so it deserves the most suspicion. It would fail if
"regular" in [17] meant something other than convergence of every trajectory, or if [17] bounds a
differently normalised coefficient. Against this: the survey's eq. (4) is explicit; the l1 argument
reproduces part 1 under that convention exactly; and (3 - sqrt 7)/2 is not the threshold under the
natural alternative normalisation either. The confirming check is the absence of non-regular operators
with min P in (0.0886, 0.177): the certified inequality rules out the only mechanism (a fixed point with
multiplier below -1), the 40,000-sample search agrees, and the extremal family itself converges at
alpha = 0.10, 0.12, 0.15, 0.17.

For Theorem A the risk is the mass bookkeeping in 3.2 (that mu and nu have equal mass and entries at
least alpha times that mass). The random test in verify_all.py (ratio 1.108 observed against the bound
1.26 at m = 3, alpha = 0.1; 0.780 against 1.08 at m = 4) never violated the bound, and 300 random
operators at alpha = 0.14 all converged. For Theorem B the risk would be an algebra slip in the roots;
the Lean identity plus the fsolve-found period-2 points at five (m, alpha) pairs close that.
