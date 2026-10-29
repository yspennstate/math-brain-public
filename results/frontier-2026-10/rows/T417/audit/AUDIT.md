# T417 second audit (agent B, 18 Oct 2026 04:xx)

Scope: the dossier results of agent A dated 18 Oct 02:xx-04:0x (the exact mean-square map, the secular equation and
stability edge, Lemma A, Lemma B, the upper-bound theorem, the SGD ceiling, and the 04:0x reduction). Read by hand line by line;
numeric checks with my own code (audit_check.py, not hb_ms_*.py), output audit_check_run1.txt.

## Verdict

- Lemma A (ii), the deterministic part: PASS. The sign checks p_h(-q) >= 0 and p_h(q) >= 0, the use of beta = r_1 r_2 <= q^2 < q,
  and the monotonicity of (q + beta)/(q - beta) in beta are all right; 1 - q^2 = 4 sqrt(kappa)/(sqrt(kappa) + 1)^2 is exact.
- Lemma A (i), the noise part: PASS once the input "stable => S < 1" is proved (below). Two small points. The complex case is right
  as written (s > (1 - sqrt beta)^2, 1 - beta <= 2(1 - sqrt beta), and rho_HB >= q^2 >= beta). The real case tacitly takes both roots
  nonnegative. Real roots of one sign that are both negative need s > 1 + beta. With s <= 2B(1 - beta)h_min/tr H that gives
  8 B h_min/tr H > 4 > 1 >= 1 - rho_HB, so the bound holds trivially. Add one line.
- Lemma B: PASS. The column-sum computation reproduces 1 - eta h_j (2 - eta h_j (1 + 1/B) - eta tr H/B), and the l1 contraction
  bounds the radius of the nonnegative block.
- The theorem's three constants (128/3; (64/3) B h_max/tr H; (32/3) sqrt kappa): PASS. Both cases of the min in eta_0 were redone.
- The SGD ceiling 1 - rho_SGD* <= 4 h_min min(B/tr H, 1/h_max): PASS, given "stable => S < 1" at beta = 0.

## The gap, and a proof that closes it

Lemma A (i) and the SGD ceiling both use "mean-square stable => S < 1". The dossier derives S from the secular function at mu = 1
and checks the equivalence on 3,000 points; it does not prove it. A renewal argument proves it, and also proves the dossier's open
claim (1) of 04:0x (the radius is the larger of the block radius and the top real secular root).

Write e_(t+1) = (1 + beta - eta H) e_t - beta e_(t-1) + xi_t, with xi_t = -eta (Hhat_t - H) e_t a martingale difference. For Gaussian
x its conditional covariance is (eta^2/B)(H e e' H + (e'He) H). The diagonal of that covariance depends only on the diagonal
e_j^2, so the diagonals close for ANY start (the dossier needs a diagonal start; it does not). Per mode, with g_j the impulse
response of r^2 - (1 + beta - eta h_j) r + beta,
    a_j(t) = E[det_j(t)^2] + sum_(s<t) g_j(t-1-s)^2 (eta^2/B) (h_j^2 a_j(s) + h_j sum_l h_l a_l(s)),
with every term nonnegative (the cross terms vanish by the martingale property). This is a renewal system a = d + K * a with a
nonnegative matrix kernel. Its summed kernel is Khat = Diag(G_j eta^2 h_j^2/B) + u h', where u_j = G_j eta^2 h_j/B and
    G_j = sum_n g_j(n)^2 = (1 + beta) / ((1 - beta) eta h_j (2(1 + beta) - eta h_j))     (AR(2) variance; check (1): 6.8e-15).
- Necessity. If the map is stable then A = sum_t a(t) is finite and A = D + Khat A, with D > 0 for a start in which every
  coordinate is nonzero. A finite positive solution forces rho(Khat) < 1. For diagonal plus rank-one, rho(Khat) < 1 holds exactly
  when every diagonal entry is < 1 and h'(I - Diag)^(-1) u < 1, and that last sum is S term by term. So stable => S < 1, with the
  brackets positive. Since Khat >= u h' entrywise, this also gives the weaker S_0 = h'u < 1, which is all Lemma A (i) uses.
- Sufficiency. The kernel decays geometrically, so rho(Khat(z)) is continuous and increasing in z past 1. S < 1 then gives
  rho(Khat(r)) < 1 for some r > 1, a(t) r^t is summable, and the map is stable (realizable second moments span R^(3d), since
  each mode's 2x2 PSD cone spans R^3). So the stability edge S = 1 of the dossier is a theorem, not only a check.
- The top eigenvalue is real (the dossier's claim (1)). The generating function sum_t a(t) z^t has nonnegative coefficients, so
  by Pringsheim its first singularity lies on the positive axis. By Perron-Frobenius rho(Khat(z)) increases in z there, so the
  radius is max(block radius, the mu* > block radius with rho(Khat(1/mu*)) = 1), which is the secular root. Check (3): at 4,000
  random points (d 1-11, B 1-1000, beta up to 0.999) the radius was a real positive eigenvalue every time. The argument is
  written in sketch form. The fine points (singularities of d(z) from the deterministic part, and the realizable starts exciting
  every pole) are standard, but they have not been written out.

Check (2): of 1,569 stable random points, none had S_0 >= 1.

## What this leaves for the lower bound

With claim (1) proved, the 04:0x route to rho_HB <= 1 - delta/4 for the explicit choice needs only the scalar inequality
R(delta, s, mu') <= 2 on the scanned domain. The dossier scans sup R from 1.684 to 1.90. That is still numerical; an interval or
hand bound on p(mu) finishes it.

## The matching lower bound, proved (04:4x; lower_proof_check.py, lower_proof_check_run1.txt)

Theorem. Let delta = min(1, 2/sqrt(kappa), B h_min/tr H), beta = (1 - delta/2)^2 and eta = delta^2/(4 h_min). Then rho_HB <= 1 - delta/4.
With the SGD ceiling, the tuned speedup satisfies
    (1/16) min(max(1, B h_max/tr H), sqrt kappa)  <=  S(B)  <=  (128/3) min(max(1, B h_max/tr H), sqrt kappa)
(the upper constant is the dossier's 128/3 in the first regime; in the other two it is 64/3 and 32/3). This is the
dossier's open statement S(B) = Theta(min(max(1, B h_max/tr H), sqrt kappa)), with explicit constants. The only change to
the dossier's choice is the cap delta <= 1, which matters only when kappa < 4.

Proof. Fix a mode and write x = eta h, in [delta^2/4, delta^2 kappa/4], a subset of [delta^2/4, 1]. The diagonal noise
eps = eta^2 h^2/B satisfies eps <= x eta tr H/B <= x delta/4. Every mode's roots are complex or double, with |r|^2 = beta,
because x >= (1 - sqrt beta)^2 = delta^2/4. The three eigenvalues of the noiseless block are r_1^2, r_2^2 and beta, so its
radius is beta < mu_0 = 1 - delta/4.
(i) The block determinant factors exactly as p_0(mu) = (mu - beta)((mu + beta)^2 - mu k^2), with k = 1 + beta - x. Its (1,1)
cofactor is mu(mu + beta), so p(mu) = p_0(mu) - eps mu(mu + beta). Put Q = p_0/(mu(mu + beta)). Then
R = x delta/(Q - eps), and the per-mode resolvent of the squared impulse response is sum_n g(n)^2 mu^-(n+1) = 1/Q(mu).
(ii) For mu >= beta, Q is increasing: (mu - beta)/mu increases, and d/dmu [(mu + beta) - mu k^2/(mu + beta)]
= 1 - beta k^2/(mu + beta)^2 >= 1 - 4 beta^2/(mu + beta)^2 >= 0, since k^2 <= 4 beta. Both factors are nonnegative.
(iii) R < 4 holds exactly when Q > delta x/2. At mu_0 this reads (3 - delta) F_0 > 2x(1 - delta/4)(a - delta/4), where
a = 1 + beta and F_0 = (1 - delta/4)(2ax - x^2 - a delta^2/4) + delta^2/16 (identity checked symbolically). The difference
is a concave quadratic in x, with x^2 coefficient proportional to -(4 - delta)(3 - delta). At x = delta^2/4, after
multiplying by 16(1 - delta/4), it is -delta^2(delta^3 - 9 delta^2 + 26 delta - 22) > 0 on (0, 1]. At x = 1 it is a degree-6
polynomial with no root in [0, 1] and positive at delta = 1/2. So R < 4 on the whole mode range, for every mu >= mu_0.
(iv) Summed over modes, the secular function is sum_j (eta/B) h_j R_j/delta < 4 eta tr H/(B delta) <= 1, because
eta tr H/B <= delta/4. With p_j > 0 on [mu_0, inf), the summed renewal kernel Khat(1/mu_0) = Diag(eps_j/Q_j) + u h' has
spectral radius < 1. Multiply the renewal equation a = d + K * a by mu_0^-t. The deterministic part decays like beta^t
(times a polynomial) and beta < mu_0, so it stays summable, and iterating with nonnegative terms gives
sum_t a(t) mu_0^-t <= (I - Khat(1/mu_0))^-1 sum_t d(t) mu_0^-t < inf. The realizable starts span R^(3d), and
|x_t| <= sqrt(a_t a_(t-1)), c_t = a_(t-1). So ||M^t|| = O(mu_0^t) and rho_HB <= mu_0.
(v) The speedup: 1 - rho_HB >= delta/4, and 1 - rho_SGD* <= 4 h_min min(B/tr H, 1/h_max). Write b = B h_min/tr H.
If B h_max/tr H <= 1, then b <= 1/kappa, delta = b and the ratio is >= 1/16. Otherwise the ratio is
>= min(kappa, 2 sqrt kappa, kappa b)/16 >= min(sqrt kappa, B h_max/tr H)/16.   []

This step does not need the Pringsheim sketch above; it uses only the renewal equation, which is exact. Numerics (3,000 random
spectra over four decades, B up to 1e4, d up to 24): min (1 - rho_HB)/delta = 0.334 (theorem 0.25); min speedup over
min(max(1, B h_max/tr H), sqrt kappa), against the SGD ceiling, = 0.0835 (theorem 1/16).

Scope: Gaussian x with diagonal H, batch B, last-iterate mean-square rate (spectral radius). Not covered: non-Gaussian fourth
moments (the dossier's failure point), and the risk curve's transient on power-law spectra (Target 1's exponent statement).
