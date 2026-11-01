# T228 target 3, step 3: the tail constant is strictly positive

claude-b1e26540, 22 Oct 2026 04:3x. Status: draft for review. Uses T3_SETUP.md (Lemma R), T3_STEP1.md (Lemma 1, Lemma 3,
Theorem 1) and T3_STEP2.md (Theorem 2). Hypotheses and notation as in T3_STEP1.md: class (A), s > 0, (S_d), alpha the
root of h(alpha) = E xi^alpha = 1, B the step bound with |R(x)| <= B.

## Theorem 3
Under the hypotheses of Theorem 1, liminf_{t -> oo} t^alpha P_pi(|x| > t) > 0. Hence the constant of Theorem 2 satisfies
c0 > 0, so P_pi(|x| > t) ~ c0 t^(-alpha) with 0 < c0 < oo, and E_pi |x|^alpha = oo.

ABB (arXiv 2102.02299) prove the analogous statement, Proposition 8.1, by optional sampling for the backward composition
Psi_1 o ... o Psi_n. In R^d that route bounds the remainder by operator norms ||M_1 ... M_(k-1)||, whose sum is not a
Goldie perpetuity. The proof below runs the chain forward, where Lemma R makes the radial bound a scalar recursion with iid
coefficients, and replaces optional sampling by a last-exit decomposition of pi.

## Four ingredients

(I) Radial lower bound. Fix x_0 = y and run x_j = Psi_j(x_(j-1)). Put u_(j-1) = x_(j-1)/|x_(j-1)| (u = e_1 if x = 0),
xi_j = |M_j u_(j-1)|, and B_j the bound of step j (a function of the |a_i| and eps_i of step j only). Rotating every a_i
of step j maps the pair (|M_j u|, B_j) for direction u to the pair for any other direction, so given the past the pair has
one fixed law: (xi_j, B_j) are iid, independent of y, with xi_j =_d xi (Lemma R). Within a pair they are dependent. Since
|Psi_j(x)| >= |M_j x| - B_j = xi_j |x| - B_j and xi_j >= 0, induction gives, with r_j = |x_j|, S_j = sum_(i<=j) log xi_i,
    r_j >= e^(S_j) r_0 - W_j,    W_j = sum_(i<=j) e^(S_j - S_i) B_i = e^(S_j) sum_(i<=j) e^(-S_i) B_i.          (3.1)

(II) The tilted walk. Let Q make the pairs iid with law xi^alpha dP (a probability law since E xi^alpha = 1). Then on the
sigma-field F_n of the first n pairs dQ/dP = e^(alpha S_n), so for a stopping time tau of the pairs and G in F_tau,
    P(tau < oo, G) = E_Q[ e^(-alpha S_tau) ; tau < oo, G ].                                                    (3.2)
Under Q, X = log xi has mean E xi^alpha log xi = m_alpha in (0, oo) (T3_STEP2.md), so S_n -> oo Q-a.s. For 0 < theta < alpha,
    E_Q e^(-theta X) = E xi^(alpha - theta) = h(alpha - theta) < 1                                             (3.3)
by Lemma 1. Three consequences:
 (a) p_+ := Q(S_j > 0 for all j >= 1) > 0. Pick L with Q(inf_(j>=0) S_j > -L) >= 1/2 (S_n -> oo) and delta > 0 with
     q := Q(X > delta) > 0 (E_Q X > 0). With m > L/delta, on {X_1, ..., X_m > delta} we have S_j > 0 for j <= m and S_m > L,
     and the walk after m is independent with infimum above -L with probability >= 1/2. So p_+ >= q^m / 2.
 (b) Overshoot. Let tau_u = inf{n : S_n > u} and O_u = S_(tau_u) - u (finite Q-a.s.). Let U = sum_(n>=0) Q(S_n in .).
     By (3.3) and Chernoff, U((-oo, 1]) <= e^theta / (1 - h(alpha - theta)) =: C_U. For any a, every visit to [a, a+1]
     after the first lies within 1 of it, so U([a, a+1]) <= C_U. Dropping the condition that the maximum before n stays
     below u,
         Q(O_u > z) <= sum_(n>=1) E_Q[ 1{S_(n-1) <= u} Fbar(u + z - S_(n-1)) ] <= C_U sum_(k>=0) Fbar(z + k)
                    <= C_U ( Fbar(z) + int_z^oo Fbar ),    Fbar(v) = Q(X > v),
     uniformly in u >= 0, and the right side tends to 0 as z -> oo because E_Q X^+ < oo.
 (c) V := sum_(i>=1) e^(-S_i) B_i. For 0 < theta < min(alpha, 1), using that B_i is independent of S_(i-1),
         E_Q V^theta <= sum_i E_Q[e^(-theta S_(i-1))] E_Q[xi_i^(-theta) B_i^theta] = E[xi^(alpha-theta) B^theta] / (1 - h(alpha-theta)) < oo
     (Hoelder; B and xi have every positive moment). So Q(V > v) <= v^(-theta) E_Q V^theta -> 0.

(III) Last-exit decomposition. Let x_0 ~ pi, A Borel, D Borel with A cap D empty, sigma_A = inf{k >= 1 : x_k in A},
sigma_D likewise. For N >= 1 split {x_N in D} by the last time in [0, N-1] at which the chain is in A (the events are
disjoint for different times) and use stationarity:
    pi(D) = P_pi(x_N in D) >= sum_(k=1)^N P_pi(x_0 in A, x_1, ..., x_(k-1) not in A, x_k in D)
          -> int_A pi(dx) E_x[ #{ k < sigma_A : x_k in D } ] >= int_A pi(dx) P_x(sigma_D < sigma_A).              (3.4)
No recurrence theorem is used; only stationarity of pi.

(IV) Leaving the ball. Lemma 3 with R = 4K: for |x| <= K and Borel E, P(x, E) >= eps_(4K) Leb(E cap B_(4K)).

## Proof of Theorem 3
Fix K and z (chosen below) and let t > 4K. Take A = B_K = {|x| <= K}, D = {|x| > t}, and the annulus
G_K = {2K <= |y| <= 4K}, which misses A.

Step 1: from y in G_K. Put u = log(t/K), tau = tau_u, and
    F = {S_j > 0 for 1 <= j <= tau} cap {V <= K/2} cap {O_u <= z}  (on {tau < oo}).
Let F' be F with V replaced by its partial sum V_tau = sum_(i<=tau) e^(-S_i) B_i; then F' is in F_tau and contains F.
On F', by (3.1) with r_0 = |y| >= 2K, for 1 <= j <= tau:
    r_j >= e^(S_j) (2K - K/2) = (3K/2) e^(S_j) > 3K/2,
so the chain does not return to B_K before tau, and at j = tau, r_tau >= (3K/2) e^(S_tau) > (3K/2)(t/K) > t. So sigma_D <= tau < sigma_A.
By (3.2), S_tau <= u + z on F', and (a)-(c):
    P_y(sigma_D < sigma_A) >= P(tau < oo, F') >= e^(-alpha(u+z)) Q(F') >= e^(-alpha(u+z)) Q(F)
                           >= (K/t)^alpha e^(-alpha z) [ p_+ - Q(V > K/2) - sup_(u>=0) Q(O_u > z) ].
Choose z and then K so that the bracket is at least p_+/2 (possible by (b) and (c)).

Step 2: from x in B_K. One step lands in G_K with probability at least eps_(4K) Leb(G_K) by (IV), without visiting B_K, so by
the Markov property at time 1,
    P_x(sigma_D < sigma_A) >= eps_(4K) Leb(G_K) (p_+/2) e^(-alpha z) K^alpha t^(-alpha).

Step 3. By (3.4) and pi(B_K) > 0 (Theorem 1 (iii)),
    pi(|x| > t) >= pi(B_K) eps_(4K) Leb(G_K) (p_+/2) e^(-alpha z) K^alpha t^(-alpha)     for all t > 4K.
So liminf t^alpha pi(|x| > t) > 0. Theorem 2 gives the limit c0, so c0 > 0. If E_pi|x|^alpha were finite, then
t^alpha P(|x| > t) <= E[|x|^alpha ; |x| > t] -> 0, contradicting c0 > 0. QED

## Remarks
- No renewal theorem, no non-arithmetic condition and no Cramer-Lundberg asymptotic is used here; the lower bound needs only
  m_alpha > 0, h < 1 on (0, alpha) (Lemma 1) and the one-step minorization (Lemma 3). Non-arithmeticity enters only
  through Theorem 2, for the existence of the limit.
- The dependence between xi_j and B_j inside a pair is harmless: (3.1) is pathwise, Q tilts the pair's joint law, and (c)
  only uses that B_i is independent of the earlier pairs.
- The same proof gives, for any start y with |y| large, P_y(sup_j |x_j| > t) >= c (|y|/t)^alpha.

## Target 3 as it now stands (steps 1-3, all drafts for review)
For the class-(A) single-index SGD chain in R^d with Gaussian data, s > 0 and gamma = E log xi < 0: a unique stationary law
pi with full support and E_pi |x|^p < oo exactly for p < alpha, and
    P_pi(|x| > t) ~ c0 t^(-alpha),   c0 = E[ |Psi(x)|^alpha - |Mx|^alpha ] / (alpha E xi^alpha log xi) in (0, oo),
alpha the positive root of E xi^alpha = 1, xi^2 = (1 - cX)^2 + c^2 X Y, X ~ chi2_b, Y ~ chi2_(d-1).
Citations: Hairer-Mattingly Theorem 1.2 (step 1, read on the page, arXiv 0810.2777v1); Goldie through JOC Theorem 3.1
(step 2, read). Step 3 cites nothing.

