# T228 target 3, step 2: the radial tail t^alpha P_pi(|x| > t) -> c0

claude-b1e26540, 22 Oct 2026 04:1x. Status: draft for review. Uses T3_SETUP.md (Lemma R) and T3_STEP1.md (Theorem 1,
Lemma 1). Hypotheses and notation as in T3_STEP1.md: class (A), s > 0, (S_d) gamma = E log xi < 0, alpha the root of
h(alpha) = E xi^alpha = 1.

## The renewal theorem used
Goldie (1991), Theorem 2.3. Read here in the restatement Jelenkovic-Olvera-Cravioto, "Implicit renewal theory and power
tails on trees", arXiv:1006.3295v5, Theorem 3.1, PDF p.5 (src_goldie/JOC_1006.3295.pdf, sha256 abbfbddf3b348a0c), which
with N = 1 and C_1 = C is Goldie's theorem:
  C >= 0, the law of log C on {C > 0} non-arithmetic; 0 < E C^alpha log C < oo; E C^alpha = 1; E C^beta < oo for some
  0 <= beta < alpha; R >= 0 independent of C with E R^beta < oo for every 0 < beta < alpha; and
      int_0^oo | P(R > t) - P(C R > t) | t^(alpha-1) dt < oo.                                           (G)
  Then P(R > t) ~ H t^(-alpha) with 0 <= H < oo,
      H = (E C^alpha log C)^(-1) int_0^oo v^(alpha-1) [P(R > v) - P(C R > v)] dv.
(Goldie's own page was not read: Project Euclid refuses scripted download. The statement above is JOC's, which they give
as a generalization of Goldie's; for N = 1 nothing else is assumed.)

## Theorem 2 (step 2 of target 3)
Under the hypotheses of Theorem 1 (T3_STEP1.md), with x ~ pi,
    t^alpha P_pi(|x| > t) -> c0 := E[ |Psi(x)|^alpha - |M x|^alpha ] / (alpha m_alpha),   m_alpha := E xi^alpha log xi,
where Psi = M x + R(x) is one fresh step independent of x, the expectation is absolutely convergent, and 0 <= c0 < oo.

Proof. Take R := |x_0| with x_0 ~ pi and C := |M_0 x_0| / |x_0| (pi has a density, so x_0 != 0 a.s.).

Independence and law of C. M_0 is independent of x_0, and by Lemma R the law of |M_0 u| is that of xi for every unit u. So
given x_0, C has the law of xi whatever x_0 is: C is independent of R and C =_d xi.

Hypotheses on C. xi has a density on (0, oo) (X ~ chi2_b has a density and xi^2 is a smooth function of (X, Y) with
nonvanishing derivative in Y when d >= 2, in X when d = 1, away from a null set), so log xi is non-arithmetic. Every
positive moment of xi is finite (Lemma 1), which gives E C^beta < oo and E C^alpha log+ C < oo. E C^alpha = h(alpha) = 1.
h is log-convex with h(0) = h(alpha) = 1 and is not constant (xi is not a.s. 1), so h is strictly convex on [0, alpha]
and h'(alpha) = m_alpha > 0; it is finite by the moment bounds. So 0 < m_alpha < oo.

Moments of R. E R^beta = E_pi |x|^beta < oo for every beta < alpha: Theorem 1 (i).

Condition (G). By stationarity |Psi(x_0)| =_d |x_0| = R, and C R = |M_0 x_0|. For nonnegative U, V on one space,
    int_0^oo |P(U > t) - P(V > t)| t^(alpha-1) dt <= E int_0^oo |1(U > t) - 1(V > t)| t^(alpha-1) dt
                                                  = E |U^alpha - V^alpha| / alpha.
Take U = |Psi(x_0)|, V = |M_0 x_0|; then |U - V| <= |R(x_0)| <= B with B as in T3_STEP1.md (B depends on the step's data
only, not on x_0, and has all moments).
  alpha <= 1: |U^alpha - V^alpha| <= |U - V|^alpha <= B^alpha, finite in mean.
  alpha > 1: |U^alpha - V^alpha| <= alpha |U - V| max(U, V)^(alpha-1) <= alpha B (V + B)^(alpha-1)
             <= alpha 2^((alpha-2)^+) [ B V^(alpha-1) + B^alpha ].
  Condition on x_0 = x. The pair (M_0, B) is independent of x_0, so by Hoelder with exponents alpha and alpha/(alpha-1),
      E[ B |M_0 x|^(alpha-1) ] <= (E B^alpha)^(1/alpha) (E |M_0 x|^alpha)^((alpha-1)/alpha) = (E B^alpha)^(1/alpha) |x|^(alpha-1),
  using E|M_0 x|^alpha = h(alpha) |x|^alpha = |x|^alpha. Integrating, the bound is (E B^alpha)^(1/alpha) E_pi |x|^(alpha-1),
  finite by Theorem 1 (i) since alpha - 1 < alpha.
So E|U^alpha - V^alpha| < oo and (G) holds.

The theorem gives P_pi(|x| > t) ~ H t^(-alpha). Since E|U^alpha - V^alpha| < oo, Fubini applies to the signed integrand:
int_0^oo v^(alpha-1) [1(U > v) - 1(V > v)] dv = (U^alpha - V^alpha)/alpha pointwise, so
    H = E[ |Psi(x_0)|^alpha - |M_0 x_0|^alpha ] / (alpha m_alpha) = c0.
H >= 0 is part of the theorem's conclusion. QED

Note. What is NOT used: nothing about the direction x/|x|, and no matrix renewal theory (Kesten, Alsmeyer-Mentemeier).
The rotation invariance of the data makes the norm a one-dimensional implicit renewal problem exactly. If c0 > 0 (step 3),
then E_pi |x|^alpha = oo, so the moment range in Theorem 1 (i) is sharp.

## What remains
Step 3: c0 > 0. The theorem gives only c0 >= 0, and c0 = 0 is not excluded by anything above. Plan as in T3_SETUP.md:
a scalar lower chain r_{k+1} = (xi_k r_k - B'_k)^+ with iid pairs (Lemma R), started inside the full support of pi
(Theorem 1 (iii)), and a Cramer-Lundberg lower bound for the tilted walk sum log xi_j; compare ABB Proposition 8.1.

## Citation status
- JOC Theorem 3.1, PDF p.5, read on the page (arXiv v5). Goldie 1991 Thm 2.3 itself: not read (download blocked);
  the claim rests on JOC's statement, which is a stated generalization proved in that paper.
- The comparison inequality for (G) is proved above in one line, so Goldie's Lemma 9.4 is not needed.
