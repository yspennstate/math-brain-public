# T390 review: the next-order coefficient (agent C, 4 Nov 2026)

The check scripts and their outputs named below are in audit_C/.

Source: T390_weight_are_asymptotic.md in this folder. Check: t390_check.py ->
t390_check.json (mpmath, 40 digits). No conflict: no file in the package names this reviewer.

Model as written in the source: 1/2 N(-m,1) + 1/2 N(m,1), known means and unit variance, weight w = e^eta/(e^eta+e^-eta)
at eta = 0, the plain (noise-free) Hyvarinen estimator against maximum likelihood. (The board text says "variance-2"; the
source uses unit variance, and this review checks the source.)

## Verdict

ACCEPT the leading term ARE(m) ~ sqrt(2 pi) e^(-m^2/2)/m. REVISE "c about 2.5" to the exact value

    ARE(m) = sqrt(2 pi) e^(-m^2/2)/m (1 - c/m^2 + O(m^-4)),   c = 4/3 + pi^2/8 = 2.5670338834...

The board's review lead is right.

## Derivation

Because p(x) = phi(x) e^(-m^2/2) cosh(m x) exactly, the substitution y = m x gives, with eps = 1/m^2 and no approximation,

    H = phi(0) e^(-m^2/2) m   A,   A = int sech^3 y e^(-eps y^2/2) dy
    V = phi(0) e^(-m^2/2) m^3 B,   B = int sech^3 y (tanh y + eps y)^2 e^(-eps y^2/2) dy
    ARE / leading term = A^2 / (2 pi B I),   with 1 - I = O(e^(-m^2/2)).

At eps = 0, A = pi/2 and B = pi/8, which gives the leading term. To first order in eps,
ratio = 1 + 2 dA/A0 - dB/B0, with dA = -(eps/2) J3 and dB = eps(2 int y tanh sech^3 - (1/2)(J3 - J5)), where
J3 = int y^2 sech^3 and J5 = int y^2 sech^5. Integrating by parts, int y tanh sech^3 = (1/3) int sech^3 = pi/6. So

    c = 8/3 - (2/pi) J3 + (4/pi) J5.

With J3 = pi^3/8 - pi and J5 = 3 pi^3/32 - 5 pi/6 (found with mpmath.identify, and the identity holds to 40 digits),
c = 8/3 - pi^2/4 + 2 + 3 pi^2/8 - 10/3 = 4/3 + pi^2/8.

## Numbers, two independent paths

The exact ratio was computed two ways: from the y-form above, and by integrating in x with the source's own g, d_eta l and
p. The two agree to every printed digit for m <= 8. They also reproduce the source's table: 0.396, 0.626, 0.772, 0.858,
0.905, 0.933, 0.961.

m^2 (1 - ratio) for m = 4, 5, 6, 8, 10, 15, 20, 40, 100 is 2.269, 2.369, 2.427, 2.486, 2.515, 2.544, 2.554, 2.5637,
2.5665. That approaches 2.56703 from below, and the gap shrinks like 1/m^2. The source's "about 2.5" was read from m <= 8,
where the m^-4 term still pulls it down.

## Not checked here

The second half of the brief is not covered here: rigour of the sandwich asymptotics (regularity, exchange of derivative and
integral), the noisy (denoising) section, the k-component conjecture, and the prior-art comparison with 2210.00726 and
Chen-Kontonis-Shah. The original catalog row stays open. No novelty certification and no change to the solved count.

## Part 2 (12:4x): the noise table, checked independently

Check: t390_noise_check.py -> t390_noise_check.json (scipy quad, nested, rel tol 1e-10). Definitions used:
psi = s g + g' for the smoothed model, u(x0) = E_z psi(x0 + sigma z), V = E_p0 u^2, V_s = E_p_sigma psi^2, I the clean
Fisher information. Integrating the noise out of the DSM gradient gives the same u as integrating it out of the explicit
gradient (Stein's lemma on z), so V <= V_s by total variance and H^2/(V_s I) is a valid lower bound, as the source says.

| m | sigma | ARE here | source | H^2/(V_s I) here | source |
|---|---|---|---|---|---|
| 3 | 0 | 0.0072 | 0.0072 | 0.0072 | 0.0072 |
| 3 | 1.5 | 0.8418 | 0.842 | 0.1823 | 0.182 |
| 3 | 3 | 0.9682 | 0.968 | 0.3318 | 0.332 |
| 3 | 6 | 0.9159 | 0.916 | 0.1857 | 0.186 |
| 5 | 2.5 | 0.8863 | 0.886 | 0.1306 | 0.131 |
| 5 | 5 | 0.9906 | 0.991 | 0.3311 | 0.331 |
| 5 | 10 | 0.9667 | 0.967 | 0.1872 | 0.187 |

Every entry matches to the printed digits. Verdict ACCEPT the table, with two wording fixes:
- "loose by a factor of about 3" holds only at sigma = m (2.9, 3.0). At sigma = m/2 the factor is 4.6 and 6.8, at
  sigma = 2m 4.9 and 5.2.
- The effective-separation sentence fits H^2/(V_s I_s), the smoothed model's own ARE (0.639 at m = 3, sigma = 3, which is
  the clean ARE at m' = 3/sqrt(10)), not the lower-bound column, which divides by the clean I.
The limit m' = m/sqrt(1 + c^2 m^2) -> 1/c is right. Still not checked: sandwich regularity, the k-component conjecture,
prior art.

## Part 3 (12:5x): regularity, and the m^-4 term

Sandwich regularity (noise-free estimator). For this model s_eta(x) = -x + m tanh(m x + eta), so every eta-derivative of
the per-sample loss l = s^2/2 + s' is a polynomial in x of degree at most 2 times bounded functions of (m x + eta)
(tanh, sech^2 and their derivatives). On any compact eta-interval the first three derivatives are dominated by
C(1 + x^2), which has every moment under the Gaussian mixture. The population loss is E l = E(s_eta - s_0)^2/2 + const,
and s_eta = s_0 a.e. forces eta = eta0 because tanh is injective, so the minimiser is unique. H = E g^2 > 0. These are
the hypotheses of the standard M-estimator theorem (van der Vaart, Asymptotic Statistics, Thm 5.23 with 5.7 for
consistency on a compact parameter set; the exchange of derivative and expectation follows from the same domination).
So sqrt(n)(eta_hat - eta0) -> N(0, V/H^2) holds as the source uses it. ACCEPT, with the compact-set (or local) condition
written in.

Exchange in the m-expansion. A(eps) and B(eps) are integrals of y^k sech^3 y times e^(-eps y^2/2) and polynomials in eps.
Since |y|^k sech^3 y is integrable for every k, Taylor's theorem with dominated convergence gives the expansion to any
order with an O(eps^(K+1)) remainder; the correction from I is O(e^(-m^2/2)/m). Carried one order further
(t390_second_order.py -> .json, 40 digits):

    ARE(m) = sqrt(2 pi) e^(-m^2/2)/m (1 - c/m^2 + d/m^4 + O(m^-6)),
    c = 4/3 + pi^2/8 = 2.56703...,   d = 58/9 - pi^2/2 + 5 pi^4/128 = 5.31468...

d was found by PSLQ (relation 1152 d = 7424 - 576 pi^2 + 45 pi^4, the same with zeta(3) and log 2 added to the basis)
and holds to 40 digits. Check against the exact ratio: m^6 (ratio - 1 + c/m^2 - d/m^4) is -9.784, -9.912, -9.944,
-9.953, -9.955 at m = 10, 20, 40, 100, 200, so the remainder is O(m^-6) as claimed. This also accounts for the source's
"about 2.5": at m = 5 the d-term moves m^2(1 - ratio) by d/m^2 = 0.21.

Still open in T390: the k-component conjecture and the prior-art comparison.
