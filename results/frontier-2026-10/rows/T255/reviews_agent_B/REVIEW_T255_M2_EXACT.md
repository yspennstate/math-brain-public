# Independent audit: T255 M2_EXACT.md, sections 2, 4 and 9

Reviewer: agent B (interactive Claude session), 17 Oct 2026 20:28-20:35. Requested by agent Q on topic
t255-audit. I did not open or run any of the author's scripts. Text audited: rows/T255/M2_EXACT.md (sha256 in the receipt).

## What I checked against

The paper itself. I took the LaTeX source of arXiv 2306.17759 (e-print of Dec 2023, main.tex lines 640-690, and line 455
for Sigma_lin = V^{ad}V^{bw} + V^{aw}V^{bd}). gen_paper.py codes Theorem 4.2's drift b(V) and diffusion
Sigma = gamma^2(2-gamma^2) Sigma_lin + gamma^4 tau0^-2 A straight from that text, in upper-triangle coordinates. It computes
the generator drift(F) = grad F . b + (1/2) Hess F : Sigma and the quadratic-variation rate grad F^T Sigma grad F of any
rational F symbolically in the entries, evaluated at 60 digits. Nothing passes through the author's noise representation,
so this is the check the text lists as weak point (b), done exactly instead of by Monte Carlo.

## Results (checks.json, checks2.json)

- Section 1, the noise representation. The covariance of the upper entries of L dGamma L^T (dGamma = sqrt(c) dH +
  k(dN K + K dN^T)) equals the paper's Sigma entry for entry: max relative gap 6e-61 over m = 2, 3, 4, random PD V and
  gamma^2, tau0. The simplified drift (V|W|^2/m^2 + (v(VD)^T + (VD)v^T)/(2m)) equals the paper's b to 4e-61. So weak point
  (b) is closed exactly. As a by-product, gamma^4 tau0^-2 A is the covariance of the dN part, so A is positive semidefinite,
  and Sigma >= c Sigma_lin is positive definite on the PD cone (c > 0). That is the nondegeneracy section 9(2) uses.
- Section 2, PD preservation. The drift and QV rate of log det V stay bounded as the smallest eigenvalue goes to 1e-4,
  1e-12, 1e-30: m = 3 drift -5.37, -5.37, -5.32 and QV 6.3, 5.9, 6.1; m = 4 likewise. This is consistent with the claim that
  no inverse is left. It is numerical, not symbolic, but the bounded-coefficient argument then goes through.
- Section 4, m = 2. Drift kappa w^3 and QV 2cw^2 + gamma^4 w^4/tau0^2, both to 2e-59 on 40 random V. The scale exponent is
  kappa/(4k^2) = 1/(4 gamma^2). S = 1^T V 1 has drift (gamma^2 w^2/(4tau0^2)) S to 2e-58 and QV <= 1.9 ((1+w)S)^2. The Feller
  analysis is right: s(inf) < inf iff gamma^2 < 1/2, and v(inf) < inf on that whole range. One small wording point: at
  gamma^2 = 1/6 exactly, the inner integral diverges like log y (line 70 says it converges), but the product with s' is
  still O(y^-3 log y), so v(inf) < inf and nothing changes. The exit-probability formula is correct given s(0+) finite and 0
  natural. The theorem "global PD solution iff gamma^2 >= 1/2" for m = 2 follows.
- Section 9, Lemma A, at a = 1e12, m = 3, 4, 5, 6, gamma^2 = 0.5 and 1:
  (i) the drift of log a per unit u equals alpha_m = (f - B^2/2) m^2/(m-1)^2 to every printed digit; 2f/B^2 =
      (m^2-m-1)/(2gamma^2(m-1)); the QV rate is bounded (0.03-0.44).
  (ii) the drift of log Phi_S per unit u equals mu_S = (gamma^2/m^2)(gamma^2 - m(m-2)/(m-1)) exactly for every random shape.
      Uniformity holds: the gap is O(|w|) (m = 3, gamma^2 = 0.5: 7.2e-3, 3.0e-4, 4.7e-5 at |w| = 1e-1, 1e-2, 1e-3; m = 4..6
      similar) and O(Phi_S) (1.5e-2, 2.4e-3, 1.6e-4 at Phi_S = 1e-1, 1e-2, 1e-3, worst over six shapes including nearly
      rank-one and nearly rank-(m-2) transverse blocks with eigenvalue ratio 1e-18). The QV rate is constant at the corner.
      At a = 50 the c-noise moves the rate the helpful way (m = 3: -0.0562 against -0.0556).
  (iii) with X = 0 the drift of |w|^2 over |w|^2 per unit u tends to -2 kappa, kappa = gamma^2(m-2)/(2m(m-1)) (m = 3:
      -0.0833338 at |w| = 1e-5 against -0.0833333), and the QV of |w|^2 is zero (1e-58), as stated.
- The proof of the theorem, read line by line.
  (1) With Phi_S < delta < 1, Phi_S <= Phi_S^p, and with delta <= 1/(2C) the |w| bound becomes -kappa|w|^2 + C Phi_S^p. With
  M p |mu_S| >= 4C, drift(Y) <= -(q alpha/2) a^-q - kappa|w|^2 - C Phi_S^p <= 0 on D. On exit Y >= y_0, so
  P(tau < inf) <= Y(V_0)/y_0. On {tau = inf}, log a grows linearly in u and t = int du/|W|^2 converges. Correct.
  (2) Sigma is analytic and positive definite on the open PD cone, so its square root is locally Lipschitz and the solution
  is pathwise unique up to explosion. Section 2 says it does not leave the cone first. The support theorem for a
  nondegenerate diffusion localised to compact subsets of the cone gives positive probability of following a PD path into
  the ball around V* = lambda e1e1^T + eta I. There Y < y_0/2 once lambda > 4^{1/q} lambda_1 and (m-1)eta/lambda is small, so
  the strong Markov step gives P(explode) >= (1/2) P(V_T in the ball) > 0. Correct.

## Verdict

PASS for section 4 (m = 2: explosion with positive probability iff gamma^2 < 1/2, else a global PD solution) and for
section 9's theorem (m >= 3, every gamma^2 in (0, 1], tau0 > 0: explosion with positive probability from every PD V_0, and
probability tending to 1 at the corner), with section 2 as its input. Lemma A is the theorem's only computed input. I
re-derived it from the paper's coefficients, not the author's representation, exactly at w = 0 and with O(|w|), O(Phi_S)
uniformity checked numerically for m = 3..6. A symbolic proof of the uniformity for general m is still argument, not
computation, as the text says. That is the residual weak point (a), and it is mild: the gap shrinks linearly in every case
tried, including degenerate shapes. Scope: correctness only. Novelty against the literature after 2306.17759 is not
judged. Corollary 4.3 (with MLP blocks) is not covered, as the text says.
