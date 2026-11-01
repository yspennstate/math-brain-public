# T228 target 3 (class A in R^d): setup and route

claude-b1e26540, 22 Oct 2026 02:4x. A setup note, not a claim. Numbers: t3_numcheck.py / t3_numcheck_run1.txt.

## Model
a_i ~ N(0, I_d), y_i = sigma(a_i.x*) + eps_i, eps_i ~ N(0, s^2), sigma(z) = z + phi(z) with phi as in class (A).
Psi(x) = x - c sum_{i<=b} sigma'(z_i)(sigma(z_i) - y_i) a_i, z_i = a_i.x, c = eta/b. Then Psi(x) = M x + R(x) with
M = I - c sum a_i a_i^T and R(x) = -c sum [z_i phi'(z_i) + (1+phi'(z_i))(phi(z_i) - y_i)] a_i, so
|R(x)| <= B := c sum |a_i| (C1 + C2 |y_i|) <= c sum |a_i| (C1' + C2(|x*||a_i| + |eps_i|)) =: B'.
B' depends on (a_i, eps_i) only through |a_i| and eps_i; all its moments are finite.

## Why neither theorem used for targets 1-2 applies
- Mirek, PTRF 2011, Assumption 1.6 (H1): M must take values in G = R_+^* x K, K a closed subgroup of O(d)
  (similarities). For d >= 2, M = I - c sum a a^T is symmetric with eigenvalues 1 - c lambda_j that differ a.s.,
  so it is not a similarity. Theorem 1.8 does not apply. (Read in w688_target1/sources/Mirek_0907.2261_selected.txt.)
- ABB (2102.02299) is a theorem on the real line.
- GSZ's d-dimensional linear result goes through Alsmeyer-Mentemeier / Kesten for AFFINE recursions only.

## Route: reduce the norm to Goldie's scalar implicit renewal theorem
Lemma R (rotation invariance). For every unit vector u, |M u| has the law of
    xi := sqrt((1 - cX)^2 + c^2 X Y),   X ~ chi2_b, Y ~ chi2_{d-1} independent
(write a_i = (a_i.u) u + a_i^perp; sum (a_i.u) a_i^perp is N(0, X I_{d-1}) given X). The pair (|M u|, (|a_i|, eps_i)_i)
also has a joint law that does not depend on u (O(d) acts on the a_i jointly and fixes |a_i|). Since M_k is independent
of F_k, the pair (xi_k, B'_k) := (|M_k u_k|, B'_k) with u_k = x_k/|x_k| (any fixed u on x_k = 0) is independent of F_k with
a fixed law: the pairs are iid. Consequences:
  (a) log|M_n...M_1 u| = sum log xi_j exactly; the top Lyapunov exponent is gamma = E log xi.
  (b) h(s) = lim (E||M_n...M_1||^s)^(1/n) = E xi^s (GSZ's formula, here with a one-line proof).
  (c) E xi^2 = 1 - 2 eta + eta^2 (b+d+1)/b, so alpha < 2 iff eta > 2b/(b+d+1) (d=1: the dossier's 2b/(b+2)).
      Checked by Monte Carlo at three (d,b,eta); quantiles of |M u| agree across three directions and the formula.
  (d) A nonempty alpha<2 window exists for every (d,b): at eta0 = 2b/(b+d+1), h(2)=1 and strict Jensen gives
      gamma < 0; continuity keeps gamma < 0 and h(2) > 1 on (eta0, eta0 + delta). The window shrinks with d:
      gamma > 0 already at eta = 0.3 for d=10, b=1 (threshold 0.167), so (S_d): E log xi < 0 is a real restriction.

Goldie 1991 (Ann. Appl. Probab. 1, 126-166), Theorem 2.3, applied to R = |x| under pi and M := xi_0 (independent of x_0
by Lemma R): needs E xi^alpha = 1, E xi^alpha log+ xi < oo, log xi non-arithmetic (xi has a density), and
    int_0^oo |P(|Psi(x)| > t) - P(xi |x| > t)| t^(alpha-1) dt  <=  E | |Psi(x)|^alpha - |M x|^alpha | / alpha  <  oo.
For alpha <= 1 the right side is <= E B^alpha. For alpha > 1 it is <= C E[B (|Mx| + B)^(alpha-1)]; condition on x and use
Hoelder with E|Mu|^alpha = 1 for every u: bounded by C (E B^alpha)^(1/alpha) E|x|^(alpha-1) + C E B^alpha, finite once
E_pi |x|^p < oo for p < alpha (drift below). Then t^alpha P_pi(|x| > t) -> c0 = E[|Psi(x)|^alpha - |Mx|^alpha]/(alpha m_alpha),
m_alpha = E xi^alpha log xi, with c0 >= 0.

## Steps left (what a worker must write)
1. Existence/uniqueness of pi. Drift: E|Psi(x)|^p <= E(xi|x| + B)^p <= h(p)|x|^p + C, h(p) < 1 for 0 < p < alpha.
   Minorization differs from d = 1: given the a_i, the label noise moves Psi(x) only inside span{a_1..a_b}, rank
   b < d possible. Use the k-step kernel with kb >= d (noise directions from k steps, carried by the intermediate M's,
   span R^d a.s.) to get a k-step small set; then positive Harris recurrence and aperiodicity.
2. Goldie as above, with each hypothesis checked on the page of the source (Goldie 1991 Thm 2.3 and Lemma 9.x).
3. c0 > 0. The hard step; Goldie gives only c0 >= 0. Candidate: the scalar lower chain r_{k+1} = (xi_k r_k - B'_k)^+
   (iid pairs by Lemma R) satisfies r_k <= |x_k| when r_0 <= |x_0|; with pi of full support (the Gaussian noise),
   a first-passage / Cramer-Lundberg argument for the random walk sum log xi_j (exponential tilt by alpha) gives
   liminf t^alpha P_pi(|x| > t) > 0. Compare ABB Proposition 8.1 (sources/ABB_2102.02299_selected.txt) before writing.
4. Direction (bonus): with x* = 0 everything is O(d)-equivariant and the tail direction is uniform on S^(d-1). For
   x* != 0 conjecture the same; Goldie does not give it.
5. Novelty search before any claim: the radial reduction is natural for rotation-invariant data and may be known
   (GSZ compute h(s) this way for the linear model; search 2021-2026 for nonlinear d-dimensional SGD tails).
