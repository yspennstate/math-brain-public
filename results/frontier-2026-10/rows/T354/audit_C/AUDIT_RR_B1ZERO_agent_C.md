# T354 random-reshuffling remainder lemma, beta1 = 0, eps = 0, audit 2 (agent C, 20 Oct 2026 03:39)

Object: the lemma "Rigorous remainder, reshuffling, beta1 = 0, eps = 0" in agent_B/NOTE.md and its code remainder_rr.py.
Audit 1 is agent A's (audit_A/AUDIT_RR_agent_A.md). This one re-derives the algebra line by line.

Verdict: CONFIRMED. Every step re-derived. The combinatorial identities agree with a brute force over all permutations to
1e-16, and the exact roots lie inside all three enclosures.

## Re-derived

- Stationary v. With the step frozen and bias correction gone, v_k = sum_j d beta2^j g^2_{k-j}, and sum_j d beta2^j = 1. So
  y = v_k/V = 1 + (d/V) sum_j beta2^j Z_{k-j}. Correct.
- Current-epoch bound. Lags 0..p are distinct samples. sum beta^j Z_j = beta^p sum Z_j + sum (beta^j - beta^p) Z_j. The first
  sum is over a subset of the Z_i and lies in [-Smax, Smax], because the negative Z_i sum to -Smax. The second has
  coefficients in [0, 1 - beta^p], so it is at most (1 - beta^p) sum|Z_i|. Correct, though loose.
- Earlier-epoch bound. Epoch m starts at lag s = p + 1 + (m-1)n and carries a permutation of all Z_i. Subtracting
  beta^(s+n-1) sum Z = 0 leaves coefficients in [0, beta^s (1 - beta^(n-1))], so the sum is at most
  beta^s (1 - beta^(n-1)) Smax, and Smax = sum|Z|/2. Summing over m gives beta^(p+1)/(1 - beta^n) times that, which is the
  code's `full`. Correct. Brute force at n = 6: the max over all permutations is 0.245 against the bound 0.360.
- Taylor expansion. phi = y^(-1/2), with phi' (1) = -1/2, phi''(1)/2 = 3/8 and phi''' = -(15/8) y^(-7/2). The Lagrange term
  is therefore (5/16) xi^(-7/2) |y-1|^3 <= (5/16) eps^3 (1 - eps)^(-7/2), with xi >= 1 - eps. The bound is per position p,
  and E|g r| <= max|g| times the p-average. Correct.
- First order. E[g_a Z_a] = C. For a != b without replacement, E[g_a Z_b] = (sum g sum Z - n C)/(n(n-1)) = -C/(n-1). Across
  epochs the term is 0, because the permutations are independent and E Z = 0. So E[g(y-1)] = d K C/V, with K equal to
  kfactor.K_rr at beta1 = 0. Correct.
- Second order. Split y - 1 = (d/V)(A + B), with A the current epoch and B = sum_m B_m. Then:
  - E[g A B_m] = 0 and E[g B_m B_m'] = 0 (independence, E B_m = 0).
  - E[g B^2] = f' E[B^2], with 0 <= E[B^2] <= full^2. This gives X and the bracket [0, x ef_max^2] in the code (sign by f' = x).
  - E[g A^2] = M00 + 2 s1 M0l + s2 Mjj + (s1^2 - s2) Mjl, with s1 and s2 the sums of beta^j and beta^(2j) over j = 1..p.
  Brute force over all 720 permutations at n = 6, random g, beta 0.8, every p: max difference 1.2e-16 (first order) and
  2.4e-17 (second order) (rr_b10_algebra_check.py, rr_b10_algebra_check.txt). Correct.
- Model constants. m3 = (729 - 9)/10 = 72 and V0 = 9, so x0 = d K 72/18. Correct.

## Roots (rr_b10_exact_roots.txt, the epoch-factorization route of AUDIT_RR_MOM_EPS at beta1 = 0, eps = 0)

| beta2 | exact x*/x0 | enclosure | note's second-order centre |
|---|---|---|---|
| 0.9999 | 0.999872 | [0.99982, 0.99992] | 0.99987 |
| 0.999 | 0.998725 | [0.99348, 1.00391] | 0.99869 |
| 0.995 | 0.993690 | [0.83118, 1.15518] | 0.99290 |

These match audit 1's Laplace-route values to all six digits. The centre misses by -3.5e-5 and -7.9e-4, which is -35 d^2 and
-32 d^2. That is the third-order term, consistent with audit 1's "-33 d^2".

## Not covered

Zeros outside [0, 3 x0] (the lemma's stated scope). Bisection plus a 600-point grid scan is used to locate the crossing; it is a
numerical scan, not a proof of monotonicity. Also not covered: other models, and novelty.

With audit 1, this lemma has two independent audits.
