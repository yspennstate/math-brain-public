# Review: T325 DOSSIER, sections MEASUREMENT, RATE and SPURIOUS MINIMA (agent B, 17 Oct 23:2x)

Read against DOSSIER.md as of 17 Oct and the author's outputs (gap_rate_out.txt, gd_steps3_out.txt). Same model family as the
author (agent A), so a consistency audit, not distinct-account admission. Numerical checks use my own code
(t325_indep.py, own quadrature on the MP density, nothing imported from the row's scripts).

## RATE, noiseless half: PASS (by hand)
- MP_q with mean 1 and variance q is the free Poisson law of rate 1/q and jump size q. Its Jacobi parameters are
  alpha_0 = rate * jump = 1, alpha_n = (rate + 1) * jump = 1 + q (n >= 1), beta_n = rate * jump^2 = q, as the dossier recalls.
- The recurrence for orthonormal p_k at s = 0 is sqrt(q) p_{k+1}(0) = -alpha_k p_k(0) - sqrt(q) p_{k-1}(0), with p_0 = 1 and
  p_1(0) = -1/sqrt(q). If p_k(0) = (-1)^k q^(-k/2) and p_{k-1}(0) = (-1)^(k-1) q^(-(k-1)/2), then
  alpha_k p_k + sqrt(q) p_{k-1} = (-1)^k [(1 + q) q^(-k/2) - q^(1 - k/2)] = (-1)^k q^(-k/2), so p_{k+1}(0) = (-1)^(k+1) q^(-(k+1)/2).
  Christoffel: R*_L = 1 / sum_{k<=L} p_k(0)^2 = 1 / sum_{k<=L} q^(-k). Correct.
- Real roots in the support: K_L(s, 0) as a polynomial in s is a multiple of the degree-L orthogonal polynomial of the measure
  s dMP_q, which is positive on [a, b] because 0 < a; so its zeros are real, simple and inside (a, b). The dossier says "recalled";
  this is the standard fact and it applies (0 lies below the support since q < 1).
- Minor: the dossier's "R*_L ~ (1 - q) q^L" is right for fixed q as L -> infinity; the exact form (1 - q) q^L / (1 - q^(L+1))
  is the one to quote.

## RATE, noisy half
The pointwise optimum of P^2 + lam (1 - P)^2 / s is P = lam / (s + lam), with value lam / (s + lam), so the ridge floor is
int lam / (s + lam) dMP_q with lam = sigma^2 q: checked by hand. The Theta(rho^(-2L)) rate is the Bernstein-ellipse rate for
weighted L^2 approximation of a function analytic off the ridge pole s = -lam; the claim is measured, labelled as measured, and
the label is right (no proof is claimed).

## FULL MATRICES and the two L = 6 sections: reasoning checked, numbers not re-run
- The symmetrisation argument is right. The signed permutations of R^d form the hyperoctahedral group, whose defining
  representation is irreducible, so its commutant is the scalars. The averaged risk is invariant under conjugating every G_l by
  the group, so its gradient at a group-fixed point lies in the fixed subspace (the scalar layers); with the scalar gradient zero
  the scalar point is critical in all 64 directions. This is why the unsymmetrised first try had gradient 1.3e-2 there.
- The L = 6 reading is the right one and is stated with the right caution: the full-matrix ends below the scalar minima lose on
  fresh S, and the gap shrinks roughly like 1/M with the sample. Note the same applies to the TRAINING polynomial floor
  (0.0802762 at M = 90 against 0.0816349 on fresh S), so "below the floor" comparisons should always use one spectrum.
- A lead the dossier's last finding opens (untested here). Every end layer is c_l times an orthogonal matrix. For even d a scaled
  rotation c(cos t I + sin t J) with J^2 = -I acts as the complex number c e^{it} on any subspace where S commutes with J. Two
  layers with conjugate angles would then realise exactly the complex-conjugate step pair that MEASUREMENT's repair (i) asks for.
  S does not commute with a fixed J, so this is only approximate, but it suggests route (i) of the last section in a sharper
  form: restrict to G_l = a_l I + b_l J_l with J_l antisymmetric orthogonal, compute the population risk exactly over Wishart S
  (rotation invariant, so the risk depends only on the relative position of the J_l), and see whether it goes below the best
  real-step minimum. If it does, the trained transformer can beat real-step GD with label noise, which reverses the reading of
  FULL MATRICES at L >= 6.
  Caveat against the lead, by free probability: for Wishart S and any fixed J, S is asymptotically free from J as d grows,
  so with tau(J) = 0, tau(J^2) = -1 the alternating moment gives tau(J S J S) -> tau(J^2) tau(S)^2 = -tau(S)^2. The rotation
  then does not act as a complex scalar on S's spectrum; at large d its effect averages out, and the complex-step mechanism
  (if real) is a small-d effect. So the test should be run at d = 4 and d = 8 side by side: a gain that shrinks with d is
  this effect, a gain that persists is something else.

## Numerical checks (t325_indep.py)
Own quadrature (Gauss-Legendre, 4000 nodes, after s = c - r cos t, which makes the MP density smooth); output in
t325_indep.jsonl. Mass, mean and variance of MP_q come back as 1, 1, q to 3e-13.
- Noiseless floor, least squares over every P of degree L with P(0) = 1, against 1/sum_{k<=L} q^(-k):
  q = 0.25, L = 1, 2, 3, 4, 6: 0.2, 0.0476190, 0.0117647, 0.00293255, 1.8312e-4, agreeing with the formula to 1e-13.
  q = 0.5: 1/3, 1/7, 1/15, 1/31, 1/127, likewise. PASS.
- Ridge floor at sigma^2 = 0.25 (lam = q/4): 0.0751838136 (q = 0.25) and 0.1753905297 (q = 0.5). The closed form
  lam m(-lam), with m the MP Stieltjes transform, gives the same to 30 digits (mpmath). The row's gap_rate_out.txt prints
  both these values ("ridge on these nodes") and a second pair from its ridge_floor() helper, 0.07518518 and 0.17540188,
  which are off by 1.4e-6 and 1.1e-5. The DOSSIER quotes the helper's pair (line 95). FIX: quote 0.075184 and 0.17539.
  The gaps of the L = 6 real-step value to ridge stay 3.3% and 5.2% after the fix (5.235% against 5.228% for q = 0.5).
- q = 0.5, L = 6, repeated step: the bounded scalar search gives step 0.600369, value 0.1845717382, matching the row's
  polished 0.184571738 at 0.6004. The 6 x 6 Hessian at that point (central differences, h = 1e-5) has least eigenvalue
  2.1e-3 > 0, so it is a strict local minimum in all six steps, not only along the diagonal. The best of 40 random L-BFGS-B
  starts in [0, 2.06]^6 is 0.1845717393, the same point to 1e-9. That is evidence for "global among real steps", not a proof.
