# Ding-Sun condition c:G and Proposition 1.3: rigorous verification spec

Everything below is at kappa = 0. Parameter rectangle (their eq e:numbers):

  alpha in [a_lb, a_ub] = [0.833078599, 0.833078600]
  q     in [q_lb, q_ub] = [0.56394907949, 0.56394908030]
      intermediate points q_lu = 0.56394907950, q_ul = 0.56394908029
  psi   in [p_lb, p_ub] = [2.5763513100, 2.5763513224]
      intermediate points psi_lu = 2.5763513103, psi_ul = 2.5763513221

gamma(q) = sqrt(q/(1-q)); gamma_lb = gamma(q_lb) etc. All endpoint constants must
enter the code as exact rationals (e.g. 833078599/10^9), not floats.

Their proofs are complete analysis except for steps marked [computer-assisted] or
"by a numerical integration package". The full list of numerical obligations:

## Block 1: Proposition p:gardner (their Prop 1.3)

Definitions: P(psi) = int tanh(sqrt(psi) z)^2 phi(z) dz;
R(q, alpha) = alpha int F_q(sqrt(q) z)^2 phi(z) dz, F_q(x) = E(-x/sqrt(1-q))/sqrt(1-q);
G(alpha,q,psi) = -psi(1-q)/2 + int log(2 cosh(sqrt(psi) z)) phi
                 + alpha int log Psi(-gamma(q) z) phi.

(1a) [l:into] With R_trunc(q,alpha) = alpha int_{|z|<=10} F_q(sqrt(q) z)^2 phi:
     R_trunc(q_lb, a_lb) > p_lb; R_trunc(q_lu, a_lb) + T < psi_lu;
     R_trunc(q_ul, a_ub) > p_ul... (their text: part a maps (q_lb,q_lu) into
     (p_lb, p_lu) at alpha=a_lb; part b maps (q_ul,q_ub) into (p_ul,p_ub) at
     alpha=a_ub; each needs the lower corner > and upper corner < checks.)
     T = tail term, their closed form:
     T = (2 a_ub/(1-q_ub)) (Psi(10) + 2 sqrt(q_ub) phi(10)/sqrt(1-q_ub)
         + q_ub (10 phi(10) + Psi(10))/(1-q_ub)), verified T < 1e-20.
     NOTE: R is increasing in q (their l:recursion.monotone, analytic), so corner
     checks suffice.

(1b) [l:at] P'(psi) <= 0.08 for psi in [p_lb, p_ub], via
     P'(psi) <= int 2/cosh(sqrt(p_lb) z)^4 phi - int cosh(2 sqrt(p_ub) z)/cosh(sqrt(p_ub) z)^4 phi.
     (Their monotonicity argument reduces to these two integrals at the corners.)
     And dR/dq <= 12 on the rectangle, via
     R(q_ub, a_ub)/(1-q_ub) + (a_ub/(1-q_ub)^2) int E(xi_ub) E'(xi_ub) zeta_ub phi dz <= 12
     where at kappa=0: xi_{q,z} = -gamma(q) z, zeta_{q,z} = -z/sqrt(q(1-q))... 
     CHECK: xi_{q,z} = (kappa - q^{1/2} z)/sqrt(1-q) = -sqrt(q/(1-q)) z;
     zeta_{q,z} = (kappa - q^{-1/2} z)/sqrt(1-q) = -z/sqrt(q(1-q)).
     xi_ub(z) = max(xi_{q_lb,z}, xi_{q_ub,z}) pointwise (= -gamma_lb z for z>=0,
     -gamma_ub z for z<0); zeta_ub similar. E, E' both increasing so
     E(xi_ub) E'(xi_ub) is the pointwise sup. The integrand E(xi)E'(xi)zeta is
     bounded by evaluating all factors at their sup when the product sign allows;
     DS integrate E(xi_ub)E'(xi_ub) zeta_ub -- since zeta_ub can be negative for
     z > 0... re-derive carefully when implementing; any pointwise upper envelope
     works. Product 0.08 * 12 = 0.96 < 1 gives the AT/contraction condition.

(1c) [c:q.psi.bds] Sign checks (P has analytic tail handling: for P use
     int_{|z|<=10} plus tail 2 e^{-50}; R via (1a) form):
     P(R(q_lb, a_lb)) - q_lb > 0 > P(R(q_lu, a_lb)) - q_lu
     P(R(q_ul, a_ub)) - q_ul > 0 > P(R(q_ub, a_ub)) - q_ub
     (their display has typos "P(R(qul,qubd))"; the intent per the surrounding
     text is as written here, at alpha = a_ub.)
     NOTE composition: R evaluated as interval through (1a)-style truncation,
     then P of that interval.

(1d) [c:gg.bds] G_*(a_ub) <= -psi_ul (1-q_ub)/2 + int log(2cosh(sqrt(p_ub) z)) phi
     + a_ub int log Psi(-gamma(q_ul)... CAREFUL: their display:
     G_*(a_ub) <= -psi_ul(1-q_ub)/2 + int log 2cosh(sqrt(psi_ub) z) phi
                  + alpha int log Psi(kappa - sqrt(q_ul) z / sqrt(1-q_ul)) phi < -1e-12.
     For the log Psi term the alpha multiplying it: log Psi < 0 so use a_lb for
     upper bound... their display just says "alpha"; re-derive the correct corner
     (upper bound on G_* needs: minimize psi(1-q)/2 subtracted... use monotonicity
     of each term in (q,psi) as they argue via stationarity: G_* evaluated with
     psi in [psi_ul, psi_ub], q = q_*(a_ub) in (q_ul, q_ub); each term bounded at
     the appropriate corner). Similarly G_*(a_lb) > +1e-12 with corners flipped.
     Tails: log(2cosh) integrand <= |x| + log 2, log Psi integrand: |log Psi(-gamma z)|
     <= ... handle with explicit tail bounds at |z| >= 10 (log Psi(u) >= -u^2/2 - log 2
     for u... use log Psi(u) >= log phi(u) - log(u + 1/u)-ish for u > 0; simplest:
     |log Psi(u)| <= u^2/2 + log 2 + log(1+|u|) everywhere; Gaussian tail of z^2 phi).

## Block 2: near lambda = 1 (Prop p:HH.PP.near.lambda.one)

(2a) [l:ell.A.large.A.improved] With the explicit |z| >= 9 tails included,
     verify the two positive integral coefficients C1 <= 2.679 and C2 <= 3.17.
     Consequently, for A >= 100,
       1 - ell(A) <= 2.679/A + 3.17/A^2 <= 2.711/A,
     and (log 2.711)/2 + 1/2 <= 0.9987. These are the corrected constants after
     the prefactors and tails are handled rigorously.

(2b) [c:entropy.near.one] iota(100) = 1 - ell(100) > 0.025, via
     ell(100) <= ell_Out(100) = int_{|z|<=9} D_{sqrt(p_lb) z}(100)/(1-q_ub) phi + 1e-15.
     So verify: that integral < 0.975 - 1e-15.

(2c) [p:sqrt] The two-dimensional bound at lambda_lb = 0.975 is
     a_lb sqrt(1+0.975) * { I_pos + I_neg } <= -0.4446, where
     I_pos = int_0^9 int_0^9 log Psi(-u) phi(gamma_ub z + sqrt(1-L_lb) u)/Psi(gamma_lb z) phi(z) du dz
     I_neg = int_{-9}^0 int_0^9 log Psi(c_ub psi_ub z - u) E(gamma_ub z) e^{-u^2 (1-L_lb)/2} phi(z) du dz
     with L_lb = 0.975^2, c_ub = sqrt(1-0.975)/sqrt(1+0.975).
     The certified implementation uses the sign-correct J_pos/J_neg envelopes:
     on the retained rectangles the logarithm is replaced by an upper envelope
     and its positive weight by a lower envelope, while dropping the remaining
     negative mass preserves an upper bound. The accompanying positive linear
     coefficient satisfies
       psi_ub (1-q_lb) / (2(2-0.025)) <= 0.285.

(2d) Assembly inequality (analytic once 2a--2c hold): for iota <= 0.018,
       sqrt(iota)(1.2837 + log(1/iota)/2) - 0.4446 < 0.
     The expression is increasing on this interval because 1.2837 > 1, and
     the certified endpoint value at iota = 0.018 is negative. Thus Block 2
     covers lambda in [0.982,1). The last value-grid cell pins
     lambda_lo(0.99) > 0.982, so the grid and endpoint regions overlap.

## Block 3: grid (Prop p:grid.result)

Shared machinery. tau = (A-1)/(A+1), A(tau) = exp(2 atanh(tau)).
D_H(A) = (A^2-1)(1-m^2)^2 / (sqrt(A^2 + m^2 - A^2 m^2) + 1)^2, m = tanh(H).
ell_In(A) = int_{|z|<=9} D_{sqrt(p_ub) z}(A)/(1-q_lb) phi dz
ell_Out(A) = int_{|z|<=9} D_{sqrt(p_lb) z}(A)/(1-q_ub) phi dz + sgn(A-1) 1e-15
lambda_up(tau) = max(ell_In, ell_Out)(A(tau)), lambda_lo = min(...).
[Verify their l:ell.bounds sandwich: analytic, rests on dD/dpsi sign -- audit.]

Gamma(H,D) = entropy of the 2x2 table (1/4)[(1+m)^2+D, 1-m^2-D; 1-m^2-D, (1-m)^2+D].
H_star >= H_lb = int_{-9}^{9} ent2((1+tanh(sqrt(p_ub) z))/2) phi dz   [ent2 = binary entropy]
frH_ub(A) = -2 H_lb + 1e-15 + int_{-9}^{9} Gamma(sqrt(p_lb) z, D_{sqrt(p_ub) z}(A)) phi dz
[Their envelope: Gamma decreasing in |m| at fixed D (dGamma/dm sign opposite m),
and the D-derivative term handled by their displayed monotonicity; audit signs.]

I_ub(lm_lo, lm_up) = a_lb int_{-9}^{9} int_0^9 log Psi(g_lb - S_ub) d_lb dx dz
  with the d_lb, g_lb, S_ub envelopes as displayed (per sign of z).
  [We may instead use direct interval cells in (z, x); the envelope route
  matches their text; the direct route is self-validating. Prefer direct
  interval evaluation of log Psi(g - S) d(z,x) with lm as an interval and
  the same domain truncations, since the truncation tails are what carry
  the analytic content:
    I(lm) <= (restriction to [-9,9]x[0,9] of negative integrand) always.
  For the LOWER bound I_lb(0): I(0) >= a_ub int_{-9}^{9} log Psi(gamma_ub z) phi
  - 1e-15 (their display; the 1e-15 covers |z|>9: |log Psi(gamma z)| phi tail).]

P_ub(lm_lo, lm_up) = -p_lb (1-q_ub) lm_lo/(1+lm_lo) + I_ub(lm_lo, lm_up) - I_lb(0)
  [CHECK: the first term sign: for lm_lo < 0 the term -psi(1-q) lm/(1+lm) is
  positive and maximized at... their P_ubd display uses lm_lo; for negative
  lambda branch they use QQ anyway. Verify per-branch monotonicity when coding.]

Q_ub adds (0.2)^2/2 - 0.2 sqrt(p_lb) sqrt(1-q_ub) c_lb and uses I_{0.2, ub}.

Part (a) cells: t-vector as printed (transcribe exactly); for each adjacent pair
verify frH_ub(A(tau_inner)) + P_ub(...) < 0 on [0.24, 0.99] branch, and the
QQ analog on the negative branch [-1, -0.18]. Boundary checks:
lambda_up(0.24) < 0.2, lambda_lo(0.99) > 0.982, lambda_lo(-0.18) > -0.125.
ALSO: coverage of lambda in [-0.125, 0]... part (a) covers [0.2, 0.982] and
[lmin, -0.125]; parts (b), (c) cover [-0.125, 0.2] via derivative signs;
near-1 by Block 2. Full covering of [lmin, 1] verified in assembly.

Part (b) cells: derivative envelopes K_{s,ub,i}, K_{s,lb,i} (i = 1,2,3) as
displayed (2D integrals on [0,6.5]x[0,8], [-3.3,0]x[0,1], [-3.3,0]x[0,9] after
changes of variables), plus truncation constants: +3e-6 (upper), -1.1e-7/sqrt(1-L_ub)
(lower) [their l:dII.dlambda.truncate -- ANALYTIC, transcribed constants; audit].
H' bracket: -(1-q_lb) log A(tau_up)/2 <= H'(lm(tau)) <= -(1-q_ub) log A(tau_lo)/2.
P' brackets as displayed. Verify (dPG)_ub < 0 on the positive t-vector (0.06..0.26),
(dPG)_lb > 0 on the negative vector (-0.19..-0.03). Boundary checks:
lambda_lo(0.26) > 0.2, lambda_up(0.06) < 0.05, lambda_up(-0.19) < -0.125,
lambda_lo(-0.03) > -0.03.

Part (c) cells: second-derivative envelopes M_{ub,i}, i = 1..4 (2D integrals over
[0,6.5]x[0,6.5] and [-5,0]x[0,11], [-5,6.5]x[0,11]) + 1e-6 truncation
[l:second.derivative.truncate -- analytic; audit] + L_ub(A_lo, A_ub) (1D integral)
for the H'' term. Verify (d2PG)_ub < 0 on the printed 17-point t-vector
(-0.043..0.078). Boundary: lambda_up(-0.043) < -0.03, lambda_lo(0.078) > 0.05.

Assembly of c:G [analytic, in their text]: PG'' < 0 on [-0.03, 0.05] with
PG(0) = SE(0) = 0, PG'(0)... need PG'(0) = 0: P'(0) = 0 and H'(0) = 0 (A(0)=1,
log A = 0) -- so 0 is a critical point, second derivative negative => strict
local max with PG < 0 on punctured [-0.03, 0.05] MINUS need PG(0) = 0:
P(0) = 0, H(0) = 0 by construction. Then (b): PG' sign opposite lambda on
[-0.125,-0.03] u [0.05, 0.2] extends negativity to those intervals (PG
decreasing away from the max, PG at -0.03/0.05 already < 0). Then (a) covers
[0.2, 0.982] and [lmin, -0.125] directly, Block 2 covers [0.982, 1).
Note SE <= min(PG, QG) and also SE <= PG + A with A <= 0 -- c:G is about
SE_star = H + P + A_inf... their SE(lm) = H + P + A; A <= 0 so SE <= PG;
on the negative branch they need the extra tilt: SE <= QG (with s = 0.2).
For the neighborhood of 0 and the derivative ranges they use SE <= PG. But
c:G requires STRICT negativity of SE_star = SE at alpha_sat for lm not in
{0,1}: on [-0.03, 0.05]\{0}, SE <= PG < 0 strict except 0. OK.
AND for lm in [0.982, 1): Block 2 gives H + P < H(1) + P(1) = -G_*(alpha);
at alpha = alpha_star exactly, G_* = 0, so H + P < 0 strictly and SE <= PG < 0. OK.
At lm = 1: SE(1) = -G_*(alpha_star) = 0 -- consistent with c:G allowing
equality at 1. [c:G states SE_star(lm) < 0 for lm not in {0,1}.]

The final journal Condition 1.2 also requires SE_star''(0) < 0 and
lim_{lm -> 1-} SE_star'(lm) > 0. Here A(0)=A'(0)=0 and A''(0)<=0, so the
certified strict PG'' bound gives SE_star''(0)<0. Ding--Sun's exact endpoint
calculation gives the stronger analytic limit SE_star'(lm)->+infinity.

Source-bound erratum: `verification/dsfun.py` line 1166 has a leading minus in
the prose docstring for I(lm). The correct definition is
I(lm)=+alpha E[log Psi(g)], as in the Ding--Sun source and executable formula
`body = -ALPHA * res`. The frozen proof-source byte is intentionally retained
because its SHA is bound into the Block 3a and 3b/c certificates; this typo does
not affect executable mathematics.

## Order of implementation

1. Core library: certified Gaussian quadrature (acb.integral based) for the
   integrand families: tanh/cosh powers, E(x) (via erfc or their integral trick),
   log Psi, D_H(A), Gamma(H,D), binary entropy; parameter-interval evaluation;
   exact-rational constants; tail bound helpers.
2. Block 1 (p:gardner). Independently valuable: re-derives the parameter
   rectangle rigorously. If any check FAILS, the rectangle itself is suspect --
   escalate carefully (recompute alpha_star to higher precision first with
   nonrigorous numerics to see which side fails).
3. Block 2, then Block 3a, 3b, 3c.
4. Each block emits a machine-readable log of every inequality with its interval.

Audit obligations (analytic steps to re-check while transcribing, since the
whole point is removing trust): l:recursion.monotone, l:intbyparts,
c:gg.decreasing, l:ell.bounds, l:dII.dlambda.truncate, l:second.derivative.truncate,
l:EE (special functions), e:dHH.dlambda derivation, and the sign/envelope
directions flagged above (2c especially).
