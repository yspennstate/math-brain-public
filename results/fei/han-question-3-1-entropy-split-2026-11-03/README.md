# The entropy split on read-once formulas

For a Boolean function f with Fourier expansion f = sum f^(S) chi_S and a coordinate k, write H(f) for the Fourier
entropy, I_k(f) for the influence, and

    D_k(f) = H(f) - (H(f_+) + H(f_-))/2,

where f_+ and f_- are the restrictions x_k = +1 and x_k = -1. With h(x) = x ln(1/x) and

    Phi(l, m) = h(l) + h(m) - [h((sqrt l + sqrt m)^2) + h((sqrt l - sqrt m)^2)]/2,

one has D_k(f) = sum over S not containing k of Phi(f^(S)^2, f^(S+k)^2). Phi is symmetric and homogeneous of degree one.

The alternating read-once trees on which Han's Question 3.1 (arXiv:2312.08271) fails, with sum |f^(S) f^(S+k)| / I_k
growing like the depth (paper and code: https://github.com/yspennstate/han-question-read-once-formulas), keep the
ratio D_k / I_k bounded. The files here prove and check:

- `q31_tree_entropy.py`: Phi, the integer Walsh-Hadamard transform and the exact block recursion for D_k on uniform
  alternating trees, compared with truth tables.
- `q31_readonce_general.py`, `q31_readonce_check.py`: on a general read-once formula (pushed to a NAND tree) the
  siblings of the path from x_k to the root enter only through P, the product of their probabilities of -1:

      D' = P[D - Phi(c0^2, I^2) + Phi(4 mu^2, I^2)] - P^2 Phi(4 mu^2, I^2) + Phi(c0'^2, I'^2),  c0' = -1 + 2 mu P,  I' = I P.

  Exact against truth tables on 60 random trees with unequal children (463 coordinates, error 2.6e-15).
- `q31_lemma_a_analytic.py`: for 0 < t <= 1, t(4 ln 2 + ln(1/t)) <= Phi(1, t) <= t(3 + ln(1/t)), from the power
  series of (1+b)^2 ln(1+b) + (1-b)^2 ln(1-b), whose coefficients past the first are negative.
- `q31_readonce_bound.py`: with Psi(c0, I) = Phi(c0^2, I^2)/I the recursion telescopes,

      D_k/I_k = sum_l (I_l - I_{l+1}) Phi(4 mu_l^2, I_l^2) / I_l^2 + Psi(c0_L, I_L),

  and the upper bound of the lemma, compared with the integral of 3 + ln 4 + 2 ln(1/x) from I_L to 1, gives

      D_k / I_k <= 5 + ln 4 - I_L (2 + ln 4) < 5 + ln 4 = 6.386 nats

  for every read-once formula and every coordinate. The identity is checked on 240 random sequences at 400 digits
  and the bound on 323 truth-table coordinates (largest ratio 4.42).
- `q31_readonce_pi2.py`, `q31_readonce_beam.py`: with mu = 1/2 and P close to 1 the sum tends to
  the integral of Phi(1, x^2)/x^2 over (0, 1), which equals pi^2/2 = 4.9348; a beam search over P sequences finds
  nothing larger. Whether pi^2/2 is the supremum over read-once formulas is open.
- `q31_readonce_gain_scan.py`: a bound on each step of the recursion separately, of order (1 - P) I, is false; only
  the telescoped sum is bounded.

So on read-once formulas the induction inequality of arXiv:2606.00246 (eq. (21)) holds with K = 5 + ln 4 while the
inequality (3.18) of Han's question fails. Each script runs with Python 3, NumPy and mpmath; the `.out` files are
their outputs.
