# T392 one-dimensional CFG results (DOSSIER.md, 18 Oct 20:38 and 19 Oct 05:39), audit 1 (agent C, 20 Oct 2026 02:17)

Objects: the setting, Proposition 1 (both samplers dominate p_c, the leakage brackets), Proposition 2 (the DDIM limit law is
free of m), Proposition 3 (the DDPM leakage exponent is 1/8), the tilted-law asymptotics, and the numbers in both tables.

Verdict: Propositions 1 and 2 CONFIRMED. Proposition 3 CONFIRMED in substance. Its lower bound has a gap as written ("Chebyshev on
the martingale keeps half the tube's Q-mass"); a repair is given below. Four tilted-law leakages in the 18 Oct table are a few
per cent off (grid resolution at y = 0), and one DDIM leakage differs from the text. None of this changes a conclusion.

## Re-derived

- Setting. Under the OU flow, N(mu, 1) stays at variance 1, so p_t is a mixture of N(+-a_t, 1). The scores are -(y-a) and
  -y + a tanh(a y). The guided score is -y + w a + (1-w) a tanh(a y). The reverse SDE drift is y + 2 s_w, which is the
  drift written. The probability flow is y + s_w, and with da = a ds this gives dy/da = w + (1-w) tanh(a y). All correct.
- Prop 1(a). b_w - b_1 = 2(w-1) a (1 - tanh(a y)) lies in [0, 4(w-1) a]. The outer drifts -y + 2a and -y + 2(2w-1)a are the exact
  reverse SDEs of the Gaussian families N(a_t, 1) and N((2w-1) a_t, 1). The drifts are ordered everywhere and the noise is additive,
  so the pathwise comparison theorem holds with one Brownian motion. Correct.
- Prop 1(b). dy/da lies in [1, 2w-1], and in [w, 2w-1] while y < 0. y is increasing, so once it reaches 0 it stays there. A path
  that ends below 0 was below 0 throughout, so it started below -w m/2. The bracket follows. Correct.
- Tilted law on y < 0. Put u = m|y|/2. The mass is (2/m) e^{-m^2/8} C(w), with C(w) = int_0^inf cosh^{1-w}(u) e^{-w u} du. The
  normaliser is 2^{w-1} sqrt(2 pi)(1 + o(1)). So the leak is (2/m) e^{-m^2/8} C(w) 2^{1-w} / sqrt(2 pi): exponent 1/8, with a
  w-dependent constant times 1/m. That is the dossier's statement. A fine log-space trapezoid matches this asymptotic to within
  0.1-0.9 per cent at m 8 and 16 for w 2 and 4 (audit_C/tilted_fine.txt).
- Prop 2. z = y - a gives dz/da = (w-1)(1 - tanh(a y)) >= 0. y >= y0 + a, so a y >= a^2/2 once a >= 2|y0|, and
  1 - tanh(x) <= 2 e^{-2x}. The tail bound holds. The flow ODE contains no m: m only sets where it is stopped. So endpoint - m/2
  -> z_inf. In law the error is controlled by the tail bound plus P(|y0| > m/4) = O(e^{-m^2/32}). Correct.

## Independent numbers (audit_C/indep_check.py, indep_check.txt)

Different method: adaptive ODE per start point (rtol 1e-10), Gauss-Hermite with 200 nodes for z_inf, bisection on the monotone
start-to-end map for the DDIM leakage, and quadrature or a 7e6-point log-space trapezoid for the tilted law.

| quantity | dossier | independent |
|---|---|---|
| z_inf mean/var, w 1.5 / 2 / 4 / 8 | 0.383/0.649, 0.649/0.518, 1.363/0.340, 2.264/0.250 | 0.3827/0.6486, 0.6491/0.5178, 1.3633/0.3395, 2.2643/0.2499 |
| DDIM leak w 1.5 m 2 | 5.2e-2 | 5.157e-2 |
| DDIM leak w 2 m 2 | 9.2e-3 (text) / 9.6e-3 (table) | 9.169e-3: the text is right, the table's quantile map is 4 per cent high |
| DDIM leak w 2 m 4; w 8 m 2 | 0; 0 | 6.25e-9; 1.59e-45 (below what 2e5 quantiles resolve; "0" means < 5e-6) |
| tilted mean/var given y > 0 (4 rows) | 1.395/0.608, 2.085/0.851, 1.771/0.487, 2.174/0.754 | 1.393/0.610, 2.084/0.852, 1.771/0.487, 2.174/0.754 |
| tilted leak w2 m2, w2 m4, w8 m2, w8 m4 | 6.1e-2, 6.1e-3, 5.4e-4, 2.2e-5 | 5.97e-2, 5.80e-3, 4.93e-4, 2.66e-5 |

The tilted leakages differ by 2 to 17 per cent. At w 8, m 4 the law's mass on y < 0 lies within about 1/((2w-1) m/2) = 0.033 of 0,
which is under two cells of cfg1d.py's 0.02 grid. Every bracket of Proposition 1 contains the independent DDIM value. I did not
re-run the DDPM Fokker-Planck solves; the m = 16 row of the 19 Oct table is consistent with its own column (log P / m^2 = -0.164
recomputed from -6.85 and log Phi(-8)).

## Proposition 3: the gap and a repair

Gap. Under Q the event E (tube plus descent) has probability about e^{-m^2/8}. Chebyshev on the martingale
M = int Delta/sqrt2 dB is an UNCONDITIONAL bound, P_Q(|M| > k) <= E[M^2]/k^2, and cannot keep half of an exponentially
small event. Jensen under Q conditioned on E has the same problem, because M is not centred under the conditioned law.

Repair: make M bounded pathwise on E. Write M by Ito with G(s, y) = int_c^y Delta/2 dy', which is
G = (w-1)[a (y - c) - log cosh(a y) + log cosh(a c)]. Then M = G(T, Y_T) - G(0, Y_0) - int [d_s G + (Delta/2) b_Q + d_y Delta / 2] ds.
On the tube y >= c/2, from a = K/c on, Delta <= 4(w-1) a e^{-a c}, |d_y Delta| <= 2(w-1) a^2 sech^2(a c/2), and b_Q = O(a). With
ds = da/a every ds-integrand integrates to O((w-1)/c^2). The time before a = K/c must not be put inside the tube: it lasts about T,
and a pathwise constraint over it would cost e^{-O(T)}. Instead, start at a = K/c by the Markov property. In the variable a, the
reverse SDE (ds = da/a, start N(0,1) at a -> 0) contains no m, so P_w(|Y| <= 1 at a = K/c) is a constant independent of m. From
that point the tube and the Girsanov bound run on a in [K/c, m/2], a horizon of log(m c / 2K). At the end,
y in [0, c] and a = m/2 give G = (w-1)[-a c + log cosh(a c) + O(1)] = O(w-1). So |M| <= C(w, c, K) on E, and
  P_w(E) >= e^{-C - (1/4) sup_E int Delta^2} Q(E),
with no probabilistic step left. The rest of the sketch then holds as written. The tube runs only for a in [K/c, m/2], a time of
log(m c / 2K). Holding y = c costs c^2/4 per unit time against the Q-optimal path y = 0, so O(c^2 log m), and the descent costs
O(c m). This gives log P_DDPM(y < 0) >= -m^2/8 - O(m). The upper bound -m^2/8 + O(log m) is Prop 1(a). The exponent 1/8 for
every w stands. The O(m) remainder is crude: the data show a power of m.

One more check of the reading. The Q-optimal leaking path is y = 0 exactly. With delta = y - a an OU fluctuation started stationary,
the most likely path to delta_T = -m/2 is the time reverse of relaxation, delta(s) = -(m/2) e^{-(T-s)} = -a(s). So y = a + delta = 0.
Correct.

## Not covered

The DDPM Fokker-Planck numerics (not re-run), d > 1, the polynomial prefactor, literature and novelty.
