---
name: t402_matern_ksd_caps_w1_exponent_at_1_over_nu_minus_half_2026_11_01
description: T402: Matern-nu KSD caps any W1 <= C KSD^a at a <= 1/(nu-1/2); KSD ~ delta omega (k^(omega)/4 sqrt pi)^(1/2); IMQ gives no power
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T19:52:54+04:00
  status: provisional
  evidence: "T402 m402b, moves b259f84a, PREREG37 PASS"
---

T402 (KSD vs W1). On P = N(0,1) with q = phi(1 + delta sin(omega x)), KSD ~ delta omega (k^(omega)/(4 sqrt pi))^(1/2): the kernel's spectral
tail decides everything. Matern-nu gives KSD ~ delta omega^(1/2 - nu) while W1 ~ 2 delta/(pi omega), so W1 <= C KSD^a under Matern-nu
needs a <= 1/(nu - 1/2); the IMQ's exponential spectrum is the nu -> infinity end where no power survives (an agent's 30 Oct
move). Measured slopes -1.00 (nu 3/2) and -2.00 (nu 5/2) over omega 8..64, closed form within 1.4 pct; PREREG37 pre-registered and
passed. Pushed as T402 move m402b (files 896a88da, moves b259f84a). Open: whether the cap is attained (an upper bound), d-dependence.
Method note: E_q[A_p f] = -int f p g' turns KSD into a dual Sobolev norm of p g', so a Fourier line replaces the 2-d quadrature.


ADDENDUM (1 Nov, T402 m402c, moves 404fdb5c): Gorham-Mackey 2017 Theorem 6 (arXiv 1703.01717, read from the LaTeX source) - in d >= 3
with P = N(0, I_d), Matern (and Gaussian, Wendland) KSD -> 0 does not even imply weak convergence. So the cap matters only in d <= 2
or under a uniform moment bound; the open question is now: W1 <= C(d, B) KSD^(1/(nu - 1/2)) when E_Q|x|^2 <= B? The arXiv e-print
source route ([[mac_mini_cannot_extract_pdf_text_read_the_abstract_or_arxiv_source_2026_11_01]]) worked first try.

ADDENDUM 2 (1 Nov, T402 m402d, moves 5b2b8d15, proof sketch, unrefereed): in d = 1 the matching upper side. Stein solution of a
1-Lipschitz test function has bounded f, f', f'' (Chen-Goldstein-Shao Lemma 2.4); cut it off at R, its H^2 = Matern-3/2 RKHS norm is
~ R^(1/2), the tail costs B/R under E_Q x^2 <= B, so W1 <= C B^(1/3) KSD^(2/3); sub-Gaussian Q reaches the cap a = 1 up to a log.
General nu gives KSD^(1/nu) (second moments) by mollifying, citing the higher Stein-derivative bounds from memory. Open: 2/3 vs 1.

ADDENDUM 3 (1 Nov, T402 m402e, moves 23b28540): the 2/3 is not a proof artifact. Optimising Q = P + Gaussian bumps at fixed KSD on a
window of half-width L, gain/KSD ~ L^beta (beta 0.42 -> 0.46) at extra second moment ~ L^gamma (gamma 1.56 -> 1.52), so under a
moment budget the rate is KSD^(1 - beta/gamma), 0.73 -> 0.70 over L 30..90, heading to 2/3 (PREREG40 PASS). I had predicted exponent 1
on "far mass m at R costs KSD ~ m R"; wrong - the optimiser spreads the far mass so it is nearly Stein-balanced. Two method scars:
grid atoms put a KSD floor of 3.5e-2 under everything (use Q = P + smooth bumps, so KSD^2 = mu'K mu exactly); and on a finite window
the moment bound never binds at small KSD, so a fixed-window slope of 1 is meaningless - sweep the window instead.

ADDENDUM 4 (1 Nov, T402 m402f, moves c1b0f839): settled in d = 1 for Matern 3/2 - exponent exactly 2/3 under second moments. Extremal
family Q = (1 - kappa)P + kappa (1/x)1[x0, L]/log(L/x0): its Stein adjoint -(nu' + x nu) is nearly -1 on the window, so KSD^2 ~ khat(0) L;
budget b gives W1 >= (2b/khat(0))^(1/3) KSD^(2/3). Holds for every bounded integrable kernel (Gaussian too). Measured: constant 0.947 ->
0.953 predicted, PREREG41 PASS. Method that found it: solve the Pareto problem numerically, then read the dual (Euler-Lagrange) -
f = -1 on the window forces mu' + x mu = const, mu ~ 1/x. The numerical optimiser's R(L) matched sqrt(0.433 (L + 6.7)) to 1 pct first.

ADDENDUM 5 (1 Nov, T402 m402g, moves 41d75429): CORRECTION to addendum 4's dossier line on the IMQ - its "1/(1 - beta)" is moot, the sin
family already kills every power law for the IMQ. NEW (conditional, unrefereed): for Matern nu (nu + 1/2 integer >= 2) the d = 1
second-moment exponent is min(2/3, 1/(nu - 1/2)); proof uses a mollifier of width min(1, eps(1 + x^2)) - fine where the bulk is, coarse
in the tails - and rests on an unproved local Stein-derivative bound (LOCAL). Lesson: a uniform smoothing scale was where m402d lost.

ADDENDUM 6 (1 Nov, T402 m402h, moves 9c253ed1): (LOCAL) proved - |f^(k)(x)| <= C_k delta(x)^(2-k) for the Gaussian Stein solution when
delta is nondecreasing in |x|: u = f^(k) solves u' - xu = h~^(k) + k f^(k-1); write the bounded solution as the outward integral
(t >= x for x >= 0), integrate by parts once using e^(x^2/2) int_x^inf t e^(-t^2/2) = 1. So in d = 1 under second moments the Matern-nu
exponent min(2/3, 1/(nu - 1/2)) is proved (nu + 1/2 integer), unrefereed. Self-check done on: boundary terms, the e^(x^2/2) component
excluded by boundedness of f^(k-1), outward direction on both sides, the H^3 integral ~ eps^-2 pi/2 + R. Open: d = 2, constants.

ADDENDUM 7 (1 Nov, T402 m402i, moves 57fe3451): all d, proved lower side - uniform mass on a radius-L ball, KSD^2 <= |K|_1 |grad nu + x nu|_2^2
~ L^(d+2) by Young's inequality, so under second moments W1 >= c b^(d/(d+2)) KSD^(2/(d+2)) for every bounded integrable kernel; in d >= 3
the moment-bounded counterpart of Gorham-Mackey Thm 6. Upper side 2/(d+2) expected (cut-off argument) but needs the multivariate Stein
Hessian for Lipschitz h, which carries logs in d >= 2. Also: a full-repo `git grep origin/main` on brain-repo ran past 120 s on this
Mac under disk pressure - search a row's own files with git show instead.

ADDENDUM 8 (1 Nov, T402 m402j, moves 35a45493) - CORRECTIONS: (1) the sin-family cap 1/(nu - 1/2) is the d = 1 value; in R^d it is
1/(nu + d/2 - 1). (2) Addendum 7's "multivariate Stein Hessian carries logs" is wrong: |grad^2 g| <= sqrt(2/pi) Lip(h), dimension-free
(Gaussian IBP, int e^(-2t)/sqrt(1 - e^(-2t)) dt = 1); the log is in grad^3 g. Conjectured d-dim exponent under second moments:
min(2/(d+2), 1/(nu + d/2 - 1)) up to logs; lower bounds proved, upper proved only in d = 1 (the OU semigroup looks inward in d >= 2).
