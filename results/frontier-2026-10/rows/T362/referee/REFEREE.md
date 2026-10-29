# T362 referee report: the two-curvature instance (agent C, 18 Oct 2026, 20:4x)

Read: DOSSIER.md sections 13:48, 15:15 (bias lemma, lower-bound proposition) and 15:21 (variance lemma, upper-bound theorem),
by agent A. Every step was re-derived by hand; the one extension below was also checked numerically (lb_all_steps.py,
lb_all_steps_out.txt).

## Verdict
ACCEPT the four statements as written, with one gap closed here: the Theta claim needs the lower bound over every constant step,
and the proposition proves it only for g L n1 <= 1/2. The extension below covers every step with 0 < g L <= 1 once
K >= n1 (Lam - ln Lam)/2, which sits inside the theorem's own regime (K >> n1 ln T). Steps with g L in (1, 2) remain uncovered.

## Checks, step by step
- Instance. F(x) = (mu/2) x^2 exactly (the linear parts cancel), x* = 0, mu = L n1/n, G* = s when n1 <= n/2 (a flat gradient is
  s n1/n2 <= s), sigma*^2 = s^2 n1/n2. Correct.
- Epoch map. X -> r^(n1) X + sum_i c_i r^(q_i), c_i = g s (stiff) or -g s n1/n2 (flat), q_i = number of stiff steps after i;
  q uniform on 0..n1-1 for a stiff step and on 0..n1 for a flat one. E B as written. B is independent of X (fresh permutation),
  so E X_(k+1) = A E X_k + E B with A deterministic. Correct.
- Bias lemma. The pair count (k+1 pairs (q, p) with q + p = k, q < n1, p < n1 - q) is right; phi is the weighted mean of
  2(k+1)/(n1+1) under non-increasing weights r^k (needs 0 <= r <= 1, i.e. g L <= 1); the antisymmetric pairing gives phi <= 1;
  phi >= r^(n1-1) from sum (k+1) r^k >= r^(n1-1) n1(n1+1)/2 and S <= n1. Correct.
- Lower-bound proposition. A^K >= e^(-2 g mu T) uses ln(1 - x) >= -2x for x <= 1/2 (here x = g L <= 1/(2 n1)); both cases and the
  constant 1/512 check: case 2 gives (mu/2) (G* (Lam - ln Lam)/(16 mu T))^2 = G*^2 (Lam - ln Lam)^2/(512 mu T^2). Correct.
- Variance lemma. sum c_i = 0 so B = sum c_i (r^q - 1); Bernoulli and e^(-x) <= 1 - x + x^2/2 give 0 <= e_q <= (n1 g L)^2/2;
  sum |c_i| = 2 g s n1, so |E2| <= g^3 s L^2 n1^3; the stiff q's sum to a constant and the flat part is the Mann-Whitney count W
  with Var W = n1 n2 (n+1)/12. Correct.
- Upper-bound theorem. g L n1 = Lam/K; E X_K <= G* (1 + Lam/2)/(mu T) and E X_K >= 0, so squaring is legitimate;
  1 - A^2 >= 1 - e^(-2 g L n1) >= g L n1 for 2 g L n1 <= 1; (n+1)/n2 <= 3 for n >= 2; L n1^2 = mu n n1. Both terms and the
  ratio 4 Lam n1 (1/2 + Lam sqrt(n1)/K)^2/K reproduce. Correct.

## Extension: the lower bound for every step 0 < g L <= 1
Take g L n1 > 1/2 and g L <= 1, so 0 <= r < 1. phi is a weighted mean of 2(k+1)/(n1+1), k = 0..n1-1, hence phi >= 2/(n1+1)
(equality at r = 0), and m >= g G*/(n1+1). A^K = r^(n1 K) <= e^(-g L n1 K) <= e^(-K/2) <= 1/2 for K >= 2. With X0 >= 0,
    E X_K >= (1 - A^K) m >= g G*/(2(n1+1)) > G*/(4 L n1 (n1+1)) >= G*/(8 L n1^2),
so E F(x_K) - F* >= (mu/2)(E X_K)^2 >= G*^2 mu/(128 L^2 n1^4) = G*^2/(128 mu n^2 n1^2)   (L = mu n/n1).
This is >= G*^2 (Lam - ln Lam)^2/(512 mu T^2) exactly when K >= n1 (Lam - ln Lam)/2. Together with the proposition:

    for X0 > 0 on the bias side, Lam - ln Lam >= 2 ln 2 and K >= max(2, n1 (Lam - ln Lam)/2), every constant step with
    0 < g <= 1/L has E F(x_K) - F* >= G*^2 (Lam - ln Lam)^2/(512 mu T^2).

With the upper-bound theorem, the optimal last-iterate error over steps g <= 1/L is Theta(G*^2 ln^2(mu T X0/G*)/(mu T^2)) on this
instance. Numerical check (exact E X_K, steps on a linear grid over (0, 1/L] plus a log grid down to g L = 1e-6, nine instances
including two with K below the sufficient K): the minimum over all steps is 123-171 times the bound; over g L n1 > 1/2 it is at
least 1.1e4 times the bound; the minimiser sits at g mu T/Lam = 1.05-1.09; the minimum of (mu/2)(E X_K)^2 is 1.26-1.46 of
G*^2 Lam^2/(8 mu T^2) (Lam here from X0, not ln T).

## Remarks for the row
1. Steps with 1 < g L < 2 (r negative, every stiff step overshoots) are not covered by either side. Most RR analyses restrict to
   g <= 1/(L n) or g <= 1/L, so the Theta statement should name the range g <= 1/L.
2. The step in the upper bound uses X0, G* and mu; that is fine for the optimal-step error but should be said where the
   statement is quoted ("tuned step").
3. The lower bound uses only (E X_K)^2; it is a bias statement, and the variance term never helps it. The worst-case-over-X0
   reading in the 15:15 section stands: with X0 on the other side the tuned step cancels the bias.
4. The kappa^0 conclusion is for this two-curvature family in units of G*. Li's kappa^3 is not contradicted, only not attained here;
   whether some convex 1-D instance attains a positive kappa power is still the open part of the row.
