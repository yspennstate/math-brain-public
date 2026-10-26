# Ding-Sun at general margin: a lemma-by-lemma audit

Audit of the probabilistic body of Ding and Sun, "Capacity lower bound
for the Ising perceptron" (arXiv:1809.07742), for the question: which
statements and proofs run at general margin kappa unchanged, which need
bounded changes, and which rest on kappa = 0 facts.  This file covers
Sections 2 through 7 of their paper in full, one entry per numbered
statement, plus entries for the assembled proofs of Theorem 1.4 and
Proposition 1.3 at the end of Section 7.  The NEXT section at the end
maps Sections 8-10 (their Condition 1.2 verification apparatus) onto
the margin program's certification plan.

Provenance and conventions.  The audit was done against the arXiv v1
LaTeX source (e-print, fetched 2026-07-17, file lbd.tex, 6299 lines).
Statement and equation numbers were reconstructed mechanically from the
source (shared theorem counter per section; globally sequential display
numbers) and validated against two independent anchors: the S_star
definition is display (48), cited by their Condition 1.2, and the
H_star display is (34), matching the reference "(34)-(48)" in
paper/lower_bound_section.tex.  Line numbers below refer to lbd.tex.
Notation: Psi is the complementary normal CDF (their bPhi), E(x) =
phi(x)/Psi(x) the inverse Mills ratio (their script E; M(x) in this
repo's notes), F_q(x) = E((kappa-x)/sqrt(1-q))/sqrt(1-q),
xi_{q,z} = (kappa - q^{1/2} z)/sqrt(1-q), and (q_star, psi_star) the RS
fixed point at (kappa, alpha).  "AT condition" means their display (5)
(equivalently (14), (15)): sup_q d/dq P(R_kappa(q, alpha)) < 1 on a
rectangle (q_lb, q_ub) x (a_lb, a_ub) containing the fixed point.

Their own declaration (Remark 1.5): "Although our main result is for
kappa = 0, this assumption is used only in a few steps which will be
explicitly indicated.  Otherwise we write most steps of the proof for
general kappa in R, assuming only that we have a fixed point
q_star = P(R_kappa(q_star, alpha)) such that condition (5) is satisfied
for a range (q_lb, q_ub) containing q_star."  A mechanical sweep of the
source for kappa = 0 confirms this: in the entire probabilistic body
(Sections 2-7) the assumption is invoked explicitly exactly once, at
line 4628 in the proof of Theorem 1.4 (the endpoint package for
S(lambda); see the Section 7 block below).  Sections 8-10 (the
numerical verification of Condition 1.2) fix kappa = 0 at the outset
(line 4654).  The audit below tests the declaration proof by proof; it
holds up, with the qualifications recorded here, the most important
being a hidden symmetry use in Lemma 7.3 that the sweep cannot see
because the kappa never gets set to zero: it enters through a
reflection that is measure-preserving only at kappa = 0.

## Section 1 statements (context for the audit)

Not part of the per-lemma audit proper, but fixed here since every
later entry refers to them.  Theorem 1.1 (t:main) and Theorem 1.4
(t:second) are stated at kappa = 0; Condition 1.2 (c:G) is the
hypothesis S_star(lambda) < 0 off {0, 1} for S_star = S_{0, alpha_star}
of display (48); Proposition 1.3 (p:gardner) is the kappa = 0
fixed-point package (existence, uniqueness, AT bound, G_star crossing)
proved by the computer-assisted block in Section 7.  The reduction of
Theorem 1.1 to Theorem 1.4 (lines 461-512) is the Paley-Zygmund step;
it manipulates only the conditional moments supplied by Theorem 1.4 and
carries no kappa of its own, so it transfers verbatim once a
general-kappa Theorem 1.4 exists.  The kappa-analogs of Condition 1.2
and Proposition 1.3 are precisely what this repo supplies: the
certified fixed point, uniqueness rectangle, AT contraction, and
G crossing at seven margins, and the float diagnostics for
S_{kappa, alpha_star} (ds_condition.py; certification of the univariate
condition is mapped but not yet run).

## Remark 2.1 (r:fixed.pt.adjusted), lines 569-592

- What it says: restates the standing assumption in the N vs N_all
  notation: a fixed point q_star = P(R_{kall}(q_star, a_all)) with the
  AT bound (14) on (q_lb, q_ub), and asserts by continuity that for
  small delta the rescaled parameters kappa = kall (N_all/N)^{1/2},
  alpha = M/N admit a nearby fixed point q_1 = q_star + o(1) with the
  AT bound (15) on the same interval.
- kappa-dependence: EXPLICIT (kall appears in every display).
- Verdict: BOUNDED CHANGES.  At kall = 0 the rescaling fixes kappa =
  kall = 0, so the continuity step perturbs alpha alone.  At kall != 0
  the rescaling perturbs the margin too: kappa - kall = kall x
  O(hat-alpha(delta)).  The continuity argument must therefore be run
  in the two parameters (kappa, alpha) jointly.  The mechanism is
  unchanged - existence by the intermediate value theorem plus
  uniqueness and stability from the contraction - but the hypothesis
  consumed is strictly stronger than the pointwise kappa = 0 statement:
  the AT contraction must hold on a rectangle with positive kappa-width
  around (kall, a_all).
- Certified inputs consumed: exactly the slab certificates of this
  repo, which prove contraction, fixed-point existence and uniqueness,
  and the G crossing over (kappa, alpha, q) boxes of kappa-width 5e-4
  (results/certified_intervals*.csv, kappa in [-0.65, 0.19]), plus the
  located alpha_star(kappa) intervals.  This entry is the cleanest
  example of the general pattern: the margin paper's rectangle-form
  certificates are the exact shape of hypothesis their general-kappa
  program asks for, whereas a point certificate at a single kappa would
  not suffice.

## Remark 2.2 (r:tap), lines 616-622

- What it says: informal summary of the state-evolution inputs from
  Bayati-Montanari and Bolthausen: (a) l2-Cauchy property of the TAP
  iterates n^(t), m^(t) for large t; (b) empirical profiles of h^(s)
  and H^(s) approach N(0, q_1) and N(0, psi_0); (c) the Gram matrices
  of the iterates converge to nondegenerate limits.
- kappa-dependence: EXPLICIT through the nonlinearity F = F_{q_1}
  (kappa sits inside the Mills argument); the row field h remains
  centered at every kappa (the margin shifts the law of n = F(h) and of
  the conditional overshoot nu, not of h).
- Verdict: VERBATIM, with one point to keep in view.  The cited results
  ([BM11, Lemma 1] and Bolthausen's iterative construction) are generic
  in the nonlinearity: they require Lipschitz continuity and moment
  growth, and F_q is Lipschitz with constant 1/(1-q) at every kappa
  since E' lies in (0,1) (their Lemma 10.1(b), stated for all real
  arguments).  Item (b) with the general-kappa state evolution
  q_{s+1} = P(R_kappa(q_s, alpha)) initialized at the certified fixed
  point stays at the fixed point for all s.  Item (a), the Cauchy
  property, is where the AT contraction (15) enters; at general kappa
  it is available as a certified input rather than from their
  Lemma 7.5.  DS state the summary informally and cite the formal
  statements per use (see the entries for Lemma 2.9 and Lemma 4.5);
  each such use audited below is nonlinearity-generic.
- Certified inputs consumed: the fixed point (q_star, psi_star) at
  (kappa, alpha) and the AT contraction on the rectangle.

## Proposition 2.3 (p:kr), lines 626-640

- What it says: for small delta there is a column split
  G = (E, hat-E) with hat-N/N <= delta/exp(1/delta^{2/3}) and
  t(delta) such that with probability at least 1/10 there exists
  hat-J in {-1,+1}^{hat-N} with
  (E m + hat-E hat-J)/N^{1/2} >= (kappa + 2 delta^{1/2}) 1_M
  coordinatewise, where m = m^(t) is the TAP magnetization (display
  (18)).
- kappa-dependence: EXPLICIT.  The proof (lines 1160-1384) targets
  T_s = N^{1/2} kappa + (M delta)^{1/2} (1 + 2^{-s}); the margin rides
  through the whole stage construction as an additive shift of the
  target vector and never interacts with the mechanism.
- Verdict: VERBATIM.  The stagewise weighted-majority argument (their
  adaptation of Kim-Roche) uses only: the base case (Lemma 2.9, general
  kappa), symmetry of the Gaussian disorder entries hat-g (disorder
  symmetry, not margin symmetry - it survives at every kappa), the mgf
  bound (58), and the deficit induction (56).  Two kappa-independent
  frictions, present already at kappa = 0 and repairable by adjusting
  constants: (i) the closing argument (lines 1377-1383) states the
  final entry bound without the N^{1/2} kappa shift, which must be
  carried along (it is, trivially, since the deficit vector is defined
  relative to T_s); (ii) as written the endgame delivers margin
  kappa + c(alpha) delta^{1/2} with c(alpha) of order alpha^{1/2},
  which for alpha near 0.83 is smaller than the 2 delta^{1/2} claimed
  in (18).  The cushion constant is consumed downstream only through
  "some positive multiple of delta^{1/2} exceeding the dkappa
  perturbation" ((19), (20), Lemma 2.4), so renaming the constant
  closes it at every kappa equally.  Neither friction involves the
  margin.
- Certified inputs consumed: none beyond Lemma 2.9's inputs.

## Lemma 2.4 (l:kr), lines 644-657

- What it says: for any y > kappa the equation h + (1-q) F_q(h) = y has
  a unique solution h in R (the function L_q maps R strictly
  increasingly onto (kappa, infinity)).
- kappa-dependence: EXPLICIT; the statement and proof are already
  written at general kappa.
- Verdict: VERBATIM.  The proof consumes only all-real-argument facts
  about E from Lemma 10.1: E(x) > max(0, x), E(x) - x of order 1/x at
  +infinity, E' in (0, 1).  Lemma 10.1 is stated and proved for all
  x in R, so the shifted argument (kappa - h)/sqrt(1-q) costs nothing.
- Certified inputs consumed: none (analytic).

## Remark 2.5 (r:cst), lines 698-708

- What it says: defines the cst convention (F-measurable, stochastically
  bounded prefactors).
- kappa-dependence: NONE.
- Verdict: VERBATIM.
- Certified inputs consumed: none.

## Definition 2.6 (d:cube, restrictions in discrete cube), lines 746-765

- What it says: defines the slice H (spin configurations J whose
  projection onto the span of the TAP iterates is within O(1/N) of m,
  displays (27)-(28)) and the refined slice H_eps (per-bin conditional
  magnetization within 2 eps of its target).
- kappa-dependence: NONE in the defining displays (the definition acts
  on the prior side; kappa enters only through the conditioned data m,
  H^(s) themselves).
- Verdict: VERBATIM.
- Certified inputs consumed: none directly; the limit theory of #H_eps
  (Section 6) is prior-side and consumes (q_star, psi_star) only.

## Definition 2.7 (d:profile, profile truncation), lines 769-814

- What it says: defines the basic satisfiability event S_{J,delta,t} =
  {(E J + hat-E hat-J)/N^{1/2} >= kappa 1_M + dkappa} (display (29))
  and its profile-truncated refinement S_{J,delta,t,eps}: a 20th-moment
  bound on nu against the conditional law phi_{xi_mu}, and a two-way
  equidistribution of (Psi(h_mu/sqrt(q)), Psi(nu_mu)/Psi(xi_mu)) at
  resolution eps.
- kappa-dependence: EXPLICIT.  kappa sits in the event itself and in
  xi = (kappa 1_M - h)/sqrt(1-q) (display (30)); the informal target
  density is (1/sqrt(q)) phi(h/sqrt(q)) phi_{xi_{q,z}}(nu), whose
  nu-conditional is the shifted (asymmetric, at kappa != 0) Mills law.
- Verdict: VERBATIM.  A definition; nothing to prove.  Two checks worth
  recording: the parenthetical claim that S_{J,delta,t} implies
  G J_all / sqrt(N_all) >= kall 1_M holds for every sign of kall
  (multiply by (N/N_all)^{1/2} > 0 and use dkappa >= 0 and the exact
  rescaling kappa = kall (N_all/N)^{1/2}); and the moment functional in
  part (ii) integrates an even power against phi_xi, well-defined at
  every xi.
- Certified inputs consumed: none directly; every later use consumes
  the fixed point through the limit law of (h, nu).

## Remark 2.8 (r:cond), lines 1082-1100

- What it says: the conditioning scheme: conditional on F = sigma(DATA),
  the matrix E is Gaussian subject to the linear constraints (49)-(50);
  the calculation is reorganized so that E is an unconditioned Gaussian
  independent of the background field, with the constraints reimposed
  through the change of measure of Section 3.
- kappa-dependence: NONE in the mechanism (Gaussian conditioning on
  linear constraints).  kappa enters only through the values of the
  conditioned data (h, n, m, H, dkappa) appearing on the right sides of
  (49)-(50).
- Verdict: VERBATIM.
- Certified inputs consumed: none.

## Lemma 2.9 (l:kr.base.case), lines 1105-1153

- What it says: for any delta there is t(delta) with
  || (delta^{1/2} + kappa - E m / N^{1/2})_+ ||_2 <= M^{1/2} /
  exp(c/delta) whp, c > 0 depending only on kappa for alpha in the
  rectangle (display (51)).
- kappa-dependence: EXPLICIT; the constant c and the threshold both
  carry kappa, and the statement is written that way.
- Verdict: VERBATIM.  The proof has three inputs, each checked at
  general kappa.  (i) The rewrite (52) of E m / N^{1/2} as
  L_q(h^(t)) + (1-q)(n^(t-1) - n^(t)) is algebra on the TAP equations.
  (ii) The Cauchy property (53) of n^(t) is the state-evolution input
  (Remark 2.2(a)); at general kappa it rests on the certified AT
  contraction.  (iii) The tail step: L_q(h) <= kappa + delta^{1/2}
  forces h <= -c'/delta^{1/2} because L_q(h) - kappa is of order 1/|h|
  as h -> -infinity - this asymptotic comes from E(x) - x of order 1/x
  at +infinity (Lemma 10.1, all-real), with c' now kappa-dependent, and
  the Gaussian tail bound for sqrt(q_1) Z below -c'/delta^{1/2} is
  margin-free.  The transfer of the tail bound to the empirical profile
  cites [BM11, Lemma 1(c)], which is generic in the (Lipschitz,
  kappa-carrying) nonlinearity.  The test function h^2 1{h <= -c} needs
  the standard pseudo-Lipschitz mollification at every kappa alike.
- Certified inputs consumed: fixed point and AT contraction at
  (kappa, alpha); nothing else.

## Corollary 2.10 (c:kr), lines 1386-1460

- What it says: ||n - n^(t)||_2 + ||h - h^(t)||_2 <= N^{1/2} /
  exp(1/delta^{1/3}), i.e. the perturbed fixed-point pair (20)-(21) is
  close to the t-th TAP iterate.
- kappa-dependence: EXPLICIT (the inversion runs through L_q, whose
  derivative bound uses the Mills expansion at the shifted argument).
- Verdict: VERBATIM.  The proof combines: the union bound (61) over
  hat-J (disorder-only); the rearrangement (62) of the fixed-point
  equation; and the inversion step, which needs a lower bound on
  dL_q/dh on the region h >= -c/delta^{1/2} guaranteed by
  L_q(h) >= (kappa + delta^{1/2}) 1_M.  The displayed derivative (63)
  has a typo - dL_q/dh = 1 - E'((kappa-h)/sqrt(1-q)), not 1 - E(...) -
  and the stated asymptotic 1/h^2 is the correct one for 1 - E'.  The
  typo is kappa-independent, and the corrected computation runs at
  every kappa from Lemma 10.1's all-real expansions.
- Certified inputs consumed: same as Lemma 2.9.

## Lemma 3.1 (l:extra.orth, subspace decompositions), lines 1576-1621

- What it says: the orthogonal decompositions V_row + V_adm + V_col =
  V_RC and V_row + V_prf + V_col = V_RCP of the relevant subspaces of
  R^{M x N} (and the one-replica versions).
- kappa-dependence: NONE.  Pure linear algebra on spans of rank-one
  matrices built from the conditioned data and the direction vectors
  v, w.
- Verdict: VERBATIM.
- Certified inputs consumed: none.

## Proposition 3.2 (p:tilt, change of measure formula), lines 1633-1679

- What it says: for any tilt T in V_RC and any E_{row,prf}-measurable
  event B, P(B | E_RC) equals the tilted-measure factorization
  (S|CR): tilted probability given rows, times the ratio of admissible
  densities (and the one-replica version (S1|CR)).
- kappa-dependence: NONE.  Gaussian change of measure plus the
  orthogonality of Lemma 3.1; the Radon-Nikodym factor cancels between
  numerator and denominator because T lies in V_RC.
- Verdict: VERBATIM.  Valid for every tilt T in V_RC; the specific tilt
  chosen later (display (71)) carries the kappa-dependent data, but
  this proposition is indifferent to the choice.
- Certified inputs consumed: none.

## Proposition 4.1 (p:adm), lines 1763-1857

- What it says: with the tilt T of (71)-(72), the admissible densities
  satisfy (A1|R): 1/p_adm1(E_adm1) = exp{N psi (1-q)/2 + O(cst)}, the
  two-replica version (A|R) with the extra factor
  exp{N psi (1-q) c_lambda^2 / 2}, and the non-asymptotic bound (73).
- kappa-dependence: NONE in the displays or proof mechanism.  The
  computation is a product of one-dimensional Gaussian densities
  phi((v, y^(s)) - (T, V^(s))); kappa is inside the conditioned data
  (y^(s), and n through T) but the proof never opens those objects.
- Verdict: VERBATIM.  The proof consumes: the restriction bounds of
  Definition 2.6, and the nondegeneracy of the change-of-basis matrix
  Xi, which is a forward reference to Corollary 5.3 (c:Xi.nondegenerate)
  - an item for the Section 5 audit; its role here is
  kappa-transparent.
- Certified inputs consumed: (q_star, psi_star) values only, through
  the limits of bq, bpsi.

## Proposition 4.2 (p:basic.sat.giv.row), lines 1880-1985

- What it says: (S1|R): tilted probability of S_J given rows equals
  exp{(1_M, log Psi(xi^J))} with xi^J the shifted Mills argument vector
  (75), up to 1 - o_N(1) for the eps-refined event; and (S|R): the pair
  probability is the integral (76) of exp{(1_M, log Psi((xi^K - lambda
  nu)/sqrt(1-lambda^2)))} against the conditional law of nu.
- kappa-dependence: EXPLICIT.  kappa 1_M sits inside xi^J (75) and
  inside the algebra (the rotation of E j to a fixed shift plus E v).
- Verdict: VERBATIM.  Checked line by line: the decomposition of J
  along the basis, the cancellation T v = -zeta^J making nu = (E-T) v
  standard Gaussian, and the orthant identity P(E v >= xi^J) =
  prod_mu Psi(xi^J_mu) are exact for arbitrary real xi^J - no symmetry
  of xi is used anywhere.  The o_N(1) for the eps-event is a law of
  large numbers for independent coordinates whose moment control is
  display (82), proved for both signs of xi separately (see Lemma 4.5).
  This proposition is the single place where the margin enters the
  moment computation, and it enters as a pure shift.
- Certified inputs consumed: none beyond the conditioned data; the
  limit versions consume the fixed point through Corollary 4.3.

## Corollary 4.3 (c:PP), lines 1989-1991 (proof 2322-2348)

- What it says: the limits (P1|R) and (P|R-LD) hold: the normalized log
  of the one-replica ratio converges to P_star, and the pair ratio is
  asymptotically bounded by 2 P_star + P(lambda), uniformly in lambda.
- kappa-dependence: EXPLICIT through xi_{q,z} in P_star (35) and
  I(lambda) (43).
- Verdict: VERBATIM.  The proof is: combine Propositions 4.1 and 4.2,
  then apply Lemma 4.5 to pass to the limit law (z, nu) with nu drawn
  from phi_{xi_{q,z}}; for lambda near 1 use the trivial bound (73).
  Each step is kappa-transparent given Lemma 4.5.  The limit constants
  P_star, P(lambda) are exactly the general-kappa displays (35), (44);
  their finiteness and the endpoint identities P(0) = 0, P(1) = -P_star
  are consumed later (the first is an exact cancellation valid at every
  kappa - checked directly: I(0) = a_all int log Psi(xi) phi dz =
  P_star - psi(1-q)/2; the second is a Section 8 item, see NEXT).
- Certified inputs consumed: (q_star, psi_star) at (kappa, alpha); the
  evaluation of P_star and P(lambda) at the certified points is what
  ds_condition.py computes in float.

## Corollary 4.4 (c:PP.small.lm), lines 1996-2034 (proof 2353-2544)

- What it says: the sharp small-lambda estimate (P|R-CLT): the log of
  the pair ratio equals N rho lambda^2 / 2 + O(cst(1 + N |lambda|^3)),
  with limsup rho <= P''(0) = 2 psi_star (1 - q_star) + I''(0)
  (display (77)).
- kappa-dependence: EXPLICIT.  The Taylor coefficients are Mills-family
  functionals of xi at the shifted argument: first derivative
  (E(xi^K), nu), second derivative -(E(xi^K), xi^K) - (E'(xi^K), nu^2)
  (displays (86)-(87)).
- Verdict: VERBATIM, with the one downstream caveat recorded here.  The
  proof consumes: the truncated-Gaussian identities int nu phi_xi = E(xi)
  and int nu^2 phi_xi = 1 + xi E(xi), and the Mills identity
  E'(x) = E(x)(E(x) - x) - all pointwise in xi, no symmetry; the exact
  first-order cancellation between (85) and the Taylor expansion, which
  reduces to ||E(xi)||^2 = N (1-q) psi - definitionally true since
  zeta = E(xi) = sqrt(1-q) n and psi = ||n||^2/N, and in the limit it
  is the fixed-point equation psi = R_kappa(q, alpha), i.e. the
  certified input (this is the general-kappa surviving identity
  alpha E[N^2] = psi_0 already noted in NOTES.md section 8); the
  concentration of tP(. | rows, S_J) on S_{J,eps}, an LLN for
  independent coordinates with moment control (82), kappa-uniform; and
  Lemma 4.5 for the limit rho -> P''(0).  Caveat: the corollary's
  usefulness downstream (Section 7, line 4613) requires
  P''(0) + H''(0) < 0, which DS verify numerically at kappa = 0
  (Proposition 9.1(c)).  At kappa != 0 this is a new numerical
  obligation of exactly the univariate species this repo's machinery
  certifies; the float scans (the degenerate maximum of
  S_{kappa, alpha_star} at lambda = 0 in ds_condition.py) are the
  uncertified version of it.
- Certified inputs consumed: fixed point identity psi_star =
  R_kappa(q_star, alpha) (for the cancellation); at certification time,
  a certified bound P''(0) + H''(0) < 0 at each margin.

## Lemma 4.5 (lem-CLT-approximation), lines 2102-2316

- What it says: for test functions f_1, f_2 on R^6 with fifth-power
  growth, the empirical inner products over the M coordinates of
  (xi^J, xi^K, zeta^J, zeta^K, h, nu) can be exchanged for their values
  at the approximating vectors (displays (79), (80)), and converge to
  the integral against phi(z) dz phi_{xi_{q,z}}(nu) dnu at the fixed
  point.
- kappa-dependence: EXPLICIT, and handled with visible care: the moment
  bound (82), int nu^20 phi_xi(nu) dnu <= O(1 + xi^21), is proved by
  separate arguments for xi >= 0 (Mills bound E(xi) <= xi
  substituted into the exponential-tilt representation) and xi <= 0
  (phi_xi <= 2 phi).  The proof is therefore already written for the
  asymmetric law that a nonzero margin produces - this display is the
  paper's own certificate that the nu-marginal analysis does not lean
  on the kappa = 0 symmetry.
- Verdict: VERBATIM.  Inputs checked: interpolation plus Cauchy-Schwarz
  (kappa-free), Definition 2.7 parts (ii)-(iii) (general kappa),
  [BM11, Lemma 1(c)] for the empirical moments of the iterates
  (nonlinearity-generic; F_q Lipschitz at every kappa), Corollary 2.10
  for X^apx vs X^(t) (general kappa, above), and the truncation
  R -> infinity argument (kappa-free given (82)).  The limit
  I_bq -> I_q_star as t up, delta down consumes continuity of the
  fixed point in the parameters, i.e. the certified rectangle.
- Certified inputs consumed: fixed point and its rectangle stability.

## Proposition 5.1 (p:adm.clt), lines 2561-2598 (proof 3037-3160)

- What it says: the admissible conditional densities are of constant
  order: (A1|RB1): 1/cst <= tp_{adm1|row,bsat1}(barE_adm1 | barE_row)
  <= cst for any J in H; and (A|RB-CLT): the pair version
  tp_{adm|row,bsat} <= cst uniformly over (J,K) in H(lm) for
  lmin <= lm <= lmbig, any constant lmbig < 1.  (Both displays carry
  tags, not numbers.)
- kappa-dependence: EXPLICIT through the conditioned thresholds.  By
  Proposition 4.2 the one-replica law of E_adm1 given (rows, sat_J) is
  that of a = C^T(nu - zeta^J) with nu a standard Gaussian in R^M
  conditioned coordinatewise to nu >= xi^J (display (75), kappa
  inside); the pair law is a_{lm,nu} = C^T(lm nu + sqrt(1-lm^2) om -
  zeta^K) with om conditioned to om >= xi^{K,lm,nu} =
  (xi^K - lm nu)/sqrt(1-lm^2) (displays (108)-(109)).
- Verdict: VERBATIM.  Upper bounds: Corollary 5.6 for the
  sat_J-version, transferred to bsat1 by tP(sat_J | rows) =
  (1 - o(1)) tP(bsat1 | rows) from Proposition 4.2; the pair bound
  reruns the Lemma 5.5 / Corollary 5.6 argument for the shifted
  threshold field xi^{K,lm,nu}, whose bounded-window coordinate
  fraction comes from the eps-profile control of nu (Definition
  2.7(iii)) together with the bounded-cube fraction for xi^K; the
  window constants absorb kappa, and 1/sqrt(1-lm^2) <= cst on
  lm <= lmbig.  Lower bound (one-replica only): the event psat1 with
  properties (i)-(ii) (lines 3084-3098) is asserted rather than
  constructed in detail; its ingredients are the profile law of large
  numbers whose moment input is display (82), proved for both signs of
  xi separately in Lemma 4.5, so the assertion consumes nothing
  kappa = 0.  No symmetry of the nu-law is used anywhere in the proof:
  the conditioning nu >= xi is handled for arbitrary real threshold
  vectors throughout.
- Certified inputs consumed: none beyond those of Lemmas 5.2-5.7
  (the fixed point enters through the limit laws).

## Lemma 5.2 (lem-CLT-empirical), lines 2630-2797

- What it says: for any cube A_gamma in R^t of side gamma within
  distance 1/gamma of the origin, at least a 1/cst_gamma fraction of
  the M rows of h(1:t) (respectively the N rows of H(1:t)) lie in
  A_gamma, with high probability (displays (95)-(96)).
- kappa-dependence: EXPLICIT in one step: the final column H^(t+1)
  passes through the perturbed fixed-point equation (20)-(21), so the
  proof must show the solution vector n = F_q applied to the perturbed
  field stays far from the span of the earlier iterates (display
  (99)); the map F_q o L_q^{-1} and its domain threshold
  kappa + delta^{1/2} carry the margin.
- Verdict: VERBATIM, with two kappa-independent write-up frictions
  recorded.  Inputs: [BM11, Lemma 1(a)] for the conditional
  representation of h^(s+1) (nonlinearity-generic; F_q is Lipschitz
  with constant 1/(1-q) at every kappa since E' lies in (0,1),
  Lemma 10.1); [BM11, Lemma 1(c)] for the norm bound (97); [BM11,
  Lemma 1(g)] for ||m^(s),perp|| >= N^{1/2}/cst (needs F_q genuinely
  nonlinear, true at every kappa since E' is strictly increasing); and
  the dkappa smoothing, where dkappa is uniform on
  [0, delta/exp(1/delta^2)]^M (line 667), margin-free in law, and the
  equation n_mu = F_q o L_q^{-1}(u_mu - dkappa_mu) decouples
  coordinatewise.  The frictions, both present already at kappa = 0:
  (i) the claimed uniform lower bound |(F_q o L_q^{-1})'(x)| >= 1/cst
  on all of x >= kappa + delta^{1/2} (line 2705) fails as
  x -> infinity, where E' -> 0 faster than any polynomial and the
  composite derivative with it; the repair is to run the density and
  covering bound only over the at-least-N/2 coordinates whose field
  value lies in a bounded window (available from (97)), bounding the
  remaining coordinates' contribution by 1 -- the count still wins.
  (ii) the covering count for (99) (line 2715) mixes the normalized
  and unnormalized scalings of the slab S; the direct volume
  computation (per-coordinate density <= cst, volume of the slab
  <= c^M gamma'^{M-t+1} (N^{1/2} cst)^{t-1} once the unit-ball volume
  is accounted) yields the normalized conclusion (99) as stated.
  Neither friction involves the margin: the ranges shift with kappa
  but the decay mechanism and the repair are identical at kappa = 0.
- Certified inputs consumed: fixed point and AT rectangle (through the
  state-evolution citations).

## Corollary 5.3 (c:Xi.nondegenerate), lines 2801-2823

- What it says: the M x t matrix bN of display (26) (columns
  n/sqrt(N psi), n^(t-1)/sqrt(N psi_{t-1}), ..., n^(1)/sqrt(N psi_1))
  has all singular values in [1/cst, cst]; hence so does the QR
  change-of-basis matrix Xi.  Forward-cited by Proposition 4.1 and by
  the basis construction of Section 2 (line 741).
- kappa-dependence: NONE in the mechanism (linear algebra plus a
  two-case norm bound); kappa lives inside the column vectors.
- Verdict: VERBATIM.  Inputs: [BM11, Lemma 1(a),(g)] for the submatrix
  bN(2:t) (nonlinearity-generic), display (99) from Lemma 5.2 for the
  distance of the new column from the span, and (97) for the omitted
  upper bound.  The two-case split on the first coordinate of the test
  vector is scale bookkeeping only.
- Certified inputs consumed: same as Lemma 5.2.

## Lemma 5.4 (l:chf.decay), lines 2827-2882

- What it says: for phi_xi the standard Gaussian conditioned to be at
  least xi: (a) |chf(tau)| <= exp(-var_xi tau^2/4) for |tau| small
  enough, where var_xi = 1 + E(xi)(xi - E(xi)); (b) |chf(tau)| <=
  max{1, exp(-tau^2/2) + 2 E(xi)/|tau|} for all real tau.
- kappa-dependence: EXPLICIT in scope: the lemma is stated and proved
  for every real threshold xi, which is exactly what a nonzero margin
  requires -- the thresholds later fed in are xi^J (75) and
  xi^{K,lm,nu} (109), asymmetric fields when kappa is not 0.
- Verdict: VERBATIM.  Checked step by step, since this was flagged as
  a likely pressure point.  Part (a) is the Taylor expansion of the
  centered characteristic function; var_xi is the truncated-Gaussian
  variance, which is positive and at most 1 for every real xi, and the
  "small enough" threshold depends on the third absolute moment,
  uniform over the window |xi| <= cst in which the part is later
  applied.  Part (b) is Cauchy's theorem on the rectangle
  {Re z >= xi, 0 <= Im z <= tau}, giving Psi(xi) - Psi(xi - i tau) =
  i phi(xi) int_0^tau exp(i xi u + u^2/2) du; the substitution
  u = tau - ubar/tau bounds the modulus by 2 phi(xi) e^{tau^2/2}/tau,
  and dividing by Psi(xi) e^{tau^2/2} yields the E(xi)/tau term.
  Every step is pointwise in xi.  The only symmetry used is
  |chf(-tau)| = |chf(tau)| (conjugation in the tau variable), which
  says nothing about the law of xi or z.  No kappa = 0 constant, no
  sign restriction on xi, no reflection of the cavity variable.
- Certified inputs consumed: none (analytic).

## Lemma 5.5 (l:gradient.bd), lines 2903-2965

- What it says: the density pp of barE_adm1 given (rows, sat_J)
  satisfies |grad pp| <= cst uniformly on R^t.
- kappa-dependence: EXPLICIT through xi^J inside the product
  characteristic function (102).
- Verdict: VERBATIM, with one kappa-independent display friction.  The
  proof: the factorization (102) (Gaussian algebra, exact for
  arbitrary real xi^J); the coordinate-fraction estimates (103)-(104)
  from Lemma 5.2 plus Corollary 5.3 (rows of bN in prescribed cubes;
  the rows lie near the closed positive orthant since every
  n^(s) = F_q(h^(s)) is a positive vector); then Lemma 5.4(a) on the
  (103)-coordinates for |s| <= N^{1/2} and Lemma 5.4(b) on the
  (104)-coordinates for |s| >= N^{1/2}; Fourier inversion closes.  The
  friction: as printed, (103) records only the upper half
  |(e_mu)^T C s|/|s| <= (1/cst)/N^{1/2} of what the stated conclusion
  |pp-hat(s)| <= exp(-|s|^2/cst) consumes; the Taylor factors help
  only if the same positive fraction of coordinates also satisfies
  |tau_mu| >= |s|/(cst N^{1/2}), a two-sided comparability.  The
  two-sided version does follow from Lemma 5.2: center the cube at a
  point a in a compact subset of the open positive orthant with
  |(a, s'')| in a fixed window for the given unit direction
  s'' = Xi^{-1}s/|Xi^{-1}s| (a linear functional cannot vanish
  identically on an open full-dimensional set, and compactness in s''
  makes the window uniform over directions); the rider
  |xi^J_mu| <= cst holds on such cubes because the h-preimage of a
  compact subset of the open orthant is bounded, the bound absorbing
  kappa.  Same gap and same repair at kappa = 0; no margin content.
- Certified inputs consumed: same as Lemma 5.2.

## Corollary 5.6 (c:adm.density.largerevt), lines 2968-3035

- What it says: 1/cst <= pp(barE_adm1) <= cst for the sat_J-conditioned
  density evaluated at the conditioned value.
- kappa-dependence: EXPLICIT through the truncated-Gaussian moments of
  nu conditioned to nu >= xi^J.
- Verdict: VERBATIM.  The centering: E nu = E(xi^J) coordinatewise
  (truncated-Gaussian mean, every real xi), and the chain
  zeta^J/(1 + O(1/N)) = sqrt(1-q) n = sqrt(1-q) F_q(h) = E(xi)
  (displays (2), (21), (27), (30)) plus Lemma 4.5 give
  ||E a||_inf <= cst/N^{1/2} -- the same general-kappa cancellation as
  the first-order step of Corollary 4.4.  The covariance: C^T D C with
  D = diag(var_{xi^J_mu}); nondegeneracy via D >= gamma(Id - I_gamma)
  and the entrywise smallness of bN^T I_gamma bN as gamma -> 0 by
  [BM11, Lemma 1(c)] -- the flagged coordinates are those with
  xi^J_mu large positive (var_xi -> 0 only as xi -> +infinity), a set
  of vanishing Gaussian mass at every kappa.  The central limit
  theorem plus the Lemma 5.5 gradient bound convert the ball average
  to the point value (105).  The variance profile var_xi is not
  symmetric in xi at kappa != 0 and none of the displays ask it to be.
- Certified inputs consumed: fixed point (through Lemma 4.5's limit).

## Lemma 5.7 (l:adm.mgf), lines 3180-3218

- What it says: the normalized cumulant generating function of the
  t-th coordinate of b_{lm,nu} (display (110)) converges:
  B_{lm,nu}(N^{1/2} s)/N -> BB(lm, s) of display (45), uniformly over
  nu in the support of the conditioned measure, in the iterated limit.
  This is the source of the convexity of BB(lm, .) in s (line 985) and
  of the cumulant interpretation behind A(lm) = inf_s BB(lm, s).
- kappa-dependence: EXPLICIT.  The exact finite-N formula is the
  exponential-tilt identity for the truncated Gaussian,
  E exp(u om_mu) = e^{u^2/2} Psi(xi_mu - u)/Psi(xi_mu), applied at the
  shifted thresholds xi^{K,lm,nu}_mu; the identity holds for all real
  xi and u, and these are the same phi_xi integrals audited in
  Lemma 4.5.
- Verdict: VERBATIM, with one kappa-independent typo.  The three terms
  of the finite-N formula (lines 3197-3214): the linear term through
  (c^(t), zeta^J); s^2/2 from ||c^(t)|| = 1; and the
  (1_M, log Psi ratio) term, whose limit is the (80) functional of
  Lemma 4.5 with a quadratically growing test function.  Uniformity
  over nu comes from the eps-profile restriction (Definition 2.7(iii)).
  The typo: line 3215 states (c^(t), zeta^J) = (1 - o(1)) N^{1/2}
  psi(1-q); the correct value is N^{1/2}(psi(1-q))^{1/2}, from
  c^(t) = n/sqrt(N psi) (display (24)) and zeta^J = (1 + o(1))
  sqrt(1-q) n (display (30)), so the inner product is
  sqrt(1-q)||n||^2/sqrt(N psi).  The square-root value is also the one
  that matches the linear coefficient -psi^{1/2} sqrt(1-q)
  sqrt((1-lm)/(1+lm)) s of BB in display (45); checked both by direct
  computation and by that matching, so the error does not propagate.
  Convexity of BB(lm, .) is inherited from convexity of cumulant
  generating functions under pointwise limits, at every kappa; this is
  what the A(lm) <= 0, A(0) = 0 endpoint chain (lines 975-985)
  consumes.
- Certified inputs consumed: fixed point (the limit is evaluated at
  (q_star, psi_star)).

## Proposition 5.8 (unlabeled), lines 3223-3329

- What it says: (A|RB-LD): limsup (log tp_{adm|row,bsat})/N <= A(lm) =
  inf_s BB(lm, s) in the iterated limit, uniformly over
  lmin <= lm <= lmbig for any constant lmbig < 1.
- kappa-dependence: EXPLICIT through the same conditioned fields as
  Lemma 5.7.
- Verdict: VERBATIM.  The steps: the convolution representation (111);
  discarding ||om^a||_inf >= (N log N)^{1/2} (112); the
  shift-monotonicity step -- for nonnegative u the truncated-Gaussian
  density ratio f(w)/f(w + u') <= 1 + o(1) on the retained range,
  because w >= xi implies w + u' >= xi.  This last is an order
  property of one-sided conditioning, valid for arbitrary real xi, not
  a symmetry; the proof restricts to u >= 0 precisely because the
  nu-law is one-sidedly supported, which is the paper's own handling
  of the asymmetry a margin produces.  Then the ball average is
  bounded by P(|b_{lm,nu,t}| <= O(1)/N^{1/2}), estimated by the
  two-sided Chernoff bound N^{O(1)} inf_{|s| <= log N}
  E exp(N^{1/2} s b_t) and closed by Lemma 5.7 with convexity of
  BB(lm, .).
- Certified inputs consumed: those of Lemma 5.7.

## Proposition 6.1 (p:count), lines 3338-3588

- What it says: (H): #H_eps/(1 - o(1)) = #H = exp{O(cst)} N^{-t}
  exp{(1_N, log 2 cosh(H)) - (H, m)}; as a consequence the limit (34)
  (the definition of H_star) holds.
- kappa-dependence: NONE in the mechanism.  Entirely prior-side: the
  uniform measure on {-1,+1}^N tilted by the field H (display (113));
  kappa reaches the statement only through the conditioned data
  H = H^(t).
- Verdict: VERBATIM.  Inputs checked: the sandwich (117) from
  Definition 2.6 via (115)-(116); the [BM11, Lemma 1(a),(g)]
  nondegeneracy of the Gram-Schmidt matrix for (25); the
  triangular-array local central limit theorem of [Borovkov 2017,
  Thm 3.1] for the 2t-dimensional lattice variable y_J, an external
  citation generic in the summands, whose four conditions are verified
  in-proof: the covariance lower bound uses Lemma 5.2 (H-side, (96))
  plus the nonlinearity of tanh (the full-rank block argument, lines
  3546-3573), the almost-sure and max-covariance bounds come from
  (97)-(118), and the nonlattice condition (120) again uses the
  empirical spread from Lemma 5.2 -- here the relevant rows involve
  the H-coordinates, which spread over all of R^t with no orthant
  constraint, so the cube-positioning has no direction obstruction.
  Nothing consumed is specific to kappa = 0.
- Certified inputs consumed: (q_star, psi_star), through the limit
  (34) only.

## Proposition 6.2 (p:cube.moderate), lines 3590-3681

- What it says: (H2-CLT): #H_eps(lm)/(#H_eps)^2 is at most (up to
  constants) #H(lm)/(#H)^2 = exp{-N lm^2/(2 sigma^2) + O(N lm^3)} for
  small lm, with sigma^2 = ||1 - m^2||^2/(N (1-q)^2) (display (121)).
- kappa-dependence: NONE in the mechanism (pair tilt (122), overlap
  tilt (123), local central limit theorem, quadratic expansion of the
  cumulant generating function).
- Verdict: VERBATIM.  The block-diagonality of Lambda''(0) (line 3664)
  is exact: J and K are independent and centered under the pair tilt,
  so all cross-covariances with the overlap coordinate vanish.  The
  inverse-function step for z_lm needs Lambda'' nondegenerate, i.e.
  order-N singular values for the A-blocks and N sigma^2 with sigma^2
  of constant order; the empirical limit of sigma^2 is
  E[(1 - tanh^2(psi^{1/2} Z))^2]/(1-q)^2 > 0 at every kappa.  The
  consistency fact (153), 1/sigma^2 -> -H''(0), is proved in the
  flowing text (lines 4152-4161) by [BM11, Lemma 1(c)] and is consumed
  by the CLT regime of Theorem 1.4's proof.
- Certified inputs consumed: (q_star, psi_star).

## Lemma 6.3 (l:algebra), lines 3761-3845

- What it says: the algebra of the pair-empirical-measure
  parametrization: properties of B_H(A), S_H(A), D_H(A) -- the
  H -> -H identities (133), strict monotonicity in A, boundary values
  (134)-(135), D_H(1) = 0 with D_H'(1) = (1-m^2)^2/2, and the
  conjugate-root analysis making (B, D) = (B_H(A), D_H(A)) the unique
  pair with P_{H,D} = Q_{A,B} a valid measure.
- kappa-dependence: NONE.  Pure algebra in (H, A) with H ranging over
  all of R.
- Verdict: VERBATIM.  The flag raised in the previous NEXT section on
  this lemma's symmetries resolves as follows: display (133),
  S_H(A) = S_{-H}(A) and D_H(A) = D_{-H}(A), is an algebraic identity
  proved pointwise (B_H(A) = 1/B_{-H}(A), lines 3796-3800).  It is a
  symmetry in the prior field variable H, not a measure-preservation
  claim; the only measure it is ever paired with is the z-Gaussian in
  ell(A) and frH(A) (displays (38), (138)), that is the prior field
  H = psi^{1/2} z, which is exactly N(0, psi) at every kappa (the
  margin moves the row-side laws of n and nu, never the centered
  fields h and H; see the Remark 2.2 entry).  The derivative values
  were spot-checked: (137) at Delta(1) = 1 gives D_H'(1) =
  (1-m^2)^2/2 as stated.
- Certified inputs consumed: none (analytic).

## Proposition 6.4 (p:cube.ld), lines 3860-3994

- What it says: (H2-LD): limsup (log #H_eps(lm))/N <= 2 H_star + H(lm)
  in the iterated limit, uniformly over lmin <= lm <= lmbig for any
  constant lmbig < 1.
- kappa-dependence: NONE in the mechanism (coordinatewise product tilt
  (139) with B_i = B_{H_i}(A), the Markov bound (142), and an entropy
  identity).
- Verdict: VERBATIM.  The Radon-Nikodym constancy over H_eps(lm) uses
  the limits (140)-(141), both [BM11, Lemma 1(c)] plus Definition
  2.6/2.7 facts; the pointwise identity Gamma(H, D_H(A)) =
  log(B + 1/B + 2/A) - tanh(H) log B - (1 - tanh(H)^2 - D_H(A))
  (log A)/2 (lines 3964-3978) is algebra from (131)-(132).  The
  endpoint evaluations in the flowing text (lines 4010-4023), H(0) =
  frH(1) = 0 and H(1) = frH(infinity) = -H_star, the derivative
  formulas (152) with the concavity of H(lm), and (153) are all
  prior-side and hold at every kappa with (q, psi) = (q_star,
  psi_star).  In particular the H-side endpoint identities needed by
  Theorem 1.4's endpoint package are not kappa = 0-specific; only the
  P- and A-side limits at lm -> 1 need the Section 8 apparatus.
- Certified inputs consumed: (q_star, psi_star).

## Lemma 7.1 (l:intbyparts), lines 4187-4218

- What it says: at the fixed point, I = alpha int E(xi_{q,z})
  zeta_{q,z} phi(z) dz = psi (1 - q), with zeta_{q,z} =
  (kappa - q^{-1/2} z)/sqrt(1-q).
- kappa-dependence: EXPLICIT.
- Verdict: VERBATIM.  Re-derived independently for this audit: writing
  zeta = xi - z sqrt(1-q)/q^{1/2}, Stein's identity plus
  E' = E(E - x) gives I = alpha E[E(xi)^2] = psi(1-q) using only
  psi = R_kappa(q, alpha).  Their route (differentiate, integrate by
  parts, solve for I) is the same computation rearranged.
- Certified inputs consumed: the fixed point at (kappa, alpha).

### Corollary 7.2 (c:gg.decreasing), lines 4220-4257

- What it says: G_star(alpha) is decreasing on (a_lb, a_ub); the proof
  shows (q_star, psi_star) is a stationary point of G (displays
  (156)-(157)) so dG_star/dalpha = int log Psi(xi_{q,z}) phi(z) dz < 0.
- kappa-dependence: EXPLICIT.
- Verdict: VERBATIM.  The two stationarity computations carry kappa
  through and are the same identities as NOTES.md section 2 (this
  repo's Lemma 1-2, verified there symbolically and numerically along
  the continuation).  Note the corollary presumes the fixed point
  exists and is differentiable in alpha on the rectangle - at general
  kappa that is again the certified rectangle plus the contraction.
- Certified inputs consumed: fixed point, uniqueness rectangle.

### Lemma 7.3 (l:recursion.monotone), lines 4259-4308

- What it says: P and R(., alpha) are nondecreasing (P' >= 0 and
  dR/dq >= 0).
- kappa-dependence: HIDDEN, and this is the audit's principal finding.
  The displays carry kappa throughout, but the positivity proof for the
  cross term of dR/dq (display (158)) pairs z with its reflection
  zbar = 2 kappa q^{1/2} - z and groups both terms under a single
  factor phi(z) dz.  That grouping is a change of variables only when
  the reflection preserves the Gaussian measure, i.e. only at
  kappa = 0 (where zbar = -z and phi(-z) = phi(z)).  This is precisely
  the u -> -u symmetry of the kappa = 0 cavity law, used silently: for
  kappa != 0, phi(zbar) != phi(z) and the displayed regrouping of the
  second term of (158) into
  int_{z <= q^{1/2} kappa} (EE'(xi_{q,z}) - EE'(xi_{q,zbar}))
  zeta_{q,z} phi(z) dz is not equal to the integral it came from.
  Separately, the stated reflection identity (display (159)) has a sign
  error: xi_{q,zbar} - xi_{q,z} = -2 q zeta_{q,z}, not +2 q zeta_{q,z}
  (checked directly, including at kappa = 0); with the corrected sign
  the monotonicity argument does close at kappa = 0.  Both claims were
  also confirmed numerically (q = 0.6, grid quadrature): at kappa = 0
  the original cross term, their regrouped form, and the
  measure-carrying pairing agree to ten digits, while at kappa = 0.3
  the regrouped form gives 2.03420 against the true 2.06053, and at
  kappa = -0.4 it gives 0.70091 against 0.68748; the pairing that
  carries phi(zbar) reproduces the true value exactly in all cases.
  The cross term itself remained positive at all three margins tested,
  consistent with the repair below.
- Verdict: OBSTRUCTION as written at kappa != 0 (for the dR/dq half;
  the P' >= 0 half is prior-side and verbatim).  The conclusion is
  nonetheless true at every kappa, and this repo already holds the
  repair: the integration-by-parts identity dR/dq =
  alpha E[E'(u)^2 + 2 E(u)^2 E'(u)]/(1-q)^2 (NOTES.md section 5,
  verified symbolically and against finite differences to 1e-15) has a
  manifestly positive integrand with no reflection step.  A
  general-kappa write-up should simply substitute that identity for
  their reflection argument.  Correction to the repo's own notes:
  NOTES.md refers to this statement as "Ding-Sun's Lemma 7.2"; in the
  arXiv v1 numbering it is Lemma 7.3 (7.2 is the corollary on G_star),
  and the accurate description is not "stated at kappa = 0" but
  "stated at general kappa with a kappa = 0-only proof step".
- Certified inputs consumed: none needed once the replacement identity
  is used; the identity itself should be added to the certified battery
  if Lemma 7.3 is consumed quantitatively anywhere (their Lemma 7.5
  uses dR/dq bounds; the margin program replaces that whole block with
  slab certificates, so nothing downstream of the obstruction survives
  into the ported proof).

### Proof of Theorem 1.4, the kappa = 0 step (line 4628)

- What it says: "For kall = 0 and all a_all in (a_lb, a_ub), we have by
  exact calculation ... S(0) = S'(0) = 0, S(1) = -G_star(a_all), and
  S'(lambda) -> infinity as lambda -> 1 (the last claim can be seen
  from Proposition 8.4)."  This is the only explicitly flagged kappa = 0
  invocation in Sections 2-7, exactly as Remark 1.5 promised.
- Audit of the four endpoint facts at general kappa: S(0) = 0
  decomposes as H(0) = 0 (prior-side: the D = 0 entropy integral equals
  2 H_star using only q = P(psi); checked directly), P(0) = 0 (exact
  cancellation, every kappa; checked directly), A(0) = 0 (convexity of
  B(0, .) plus the s-derivative identity at s = 0, which is again the
  fixed point psi = R_kappa - their own display below (45) already
  cites (3) for it).  S'(0) = 0: H'(0) = 0 prior-side; P'(0) =
  -psi(1-q) + I'(0) with I'(0) = alpha E[E(xi)^2] = psi(1-q) - the
  fixed point again; A'(0) = 0 from A <= 0 = A(0).  So S(0) = S'(0) = 0
  transfer to every kappa given the certified fixed point - these are
  the six endpoint identities ds_condition.py verifies to 1e-12 at the
  certified margins.  S(1) = -G_star and S'(lambda) -> infinity near
  lambda = 1 rest on the Section 8 analysis (Propositions 8.1, 8.4,
  Corollary 8.3), which fixes kappa = 0 at line 4654; these are genuine
  open obligations of the port (the float curves at the five margins
  match the expected endpoint behavior, which is evidence, not proof).
  The remaining numerical citation at line 4635, P''(0) + H''(0) < 0
  (Proposition 9.1(c)), is likewise kappa = 0 and becomes a certified
  obligation per margin.

## Lemma 7.4 (l:into), lines 4311-4359 [computer-assisted]

- What it says: R(., alpha) maps the reference q-interval inward for
  every alpha in (albd, aubd), with numerical endpoint bounds.
- kappa-dependence: the statement is the kappa = 0 instance; the
  interval endpoints are kappa = 0 decimals.
- Verdict: REPLACED BY CERTIFICATION.  This is the existence clause
  of the margin program's Condition 1 package: the per-slab
  endpoint-inward sweeps certify it at every kappa in the strip
  (1680 slabs), and the located thin rectangles carry it at each
  certified margin.
- Certified inputs consumed: the slab existence certificates.

## Lemma 7.5 (l:at), lines 4361-4429 [computer-assisted]

- What it says: sup over the rectangle G of dP(R(q, alpha))/dq is at
  most 0.96 - the uniform contraction.
- kappa-dependence: kappa = 0 rectangle and constant.
- Verdict: REPLACED BY CERTIFICATION.  The per-slab contraction
  products certify the same clause at every strip kappa (worst
  0.958 across the lane's thin rectangles; margins 0.049-0.198 on
  the contraction lane), through the collapsed dR/dq identity that
  also repairs Lemma 7.3's general-kappa proof.
- Certified inputs consumed: slab contraction certificates; the
  thin-rectangle lane summary.

## Corollary 7.6 (c:q.psi.bds), lines 4431-4462 [computer-assisted]

- What it says: for each alpha in the window there is a unique fixed
  point (q_star, psi_star) inside the reference box.
- kappa-dependence: kappa = 0 box.
- Verdict: REPLACED BY CERTIFICATION.  Uniqueness at general kappa
  is carried per slab by Banach on the certified rectangles and,
  independently on the positive lane, by Nakajima's theorem under a
  certified premise.
- Certified inputs consumed: located fixed-point intervals; the
  uniqueness certificates of both lanes.

## Corollary 7.7 (c:gg.bds), lines 4464-4520 [computer-assisted]

- What it says: G_star(albd) > 0 > G_star(aubd), so alpha_star lies
  inside the window.
- kappa-dependence: kappa = 0 endpoints.
- Verdict: REPLACED BY CERTIFICATION.  The certified G-sign
  crossings at located boxes carry this clause per slab and, deep,
  at each certified margin (alpha_star width ~2e-6).
- Certified inputs consumed: per-slab G crossings; deep alpha_star
  enclosures.

## Assembled proofs of Theorem 1.4 and Proposition 1.3 (Section 7 close)

- What they do: assemble the audited pieces plus the computer-assisted
  block into the capacity lower bound at kappa = 0; the CLT-regime
  bookkeeping is displays (161)-(165), and the single explicitly
  kappa = 0 step is at source line 4628 (the endpoint package
  S(1) = -G_star with the S' divergence near lambda = 1, resting on
  their Section 8).
- Verdict: BOUNDED CHANGES, conditional on Section 8's endpoint
  package at general kappa (see NEXT); every other consumed piece is
  audited VERBATIM above or replaced by the margin certificates.

## Section 8 (Quantitative estimates of limiting exponents, lines 4652-4993)

Their Section 8 opens by fixing kappa = 0 outright (line 4654), so
every statement here is FORMALLY kappa = 0; the audit question is
which proofs are structurally margin-generic.  Notation: their
S(lm) = H(lm) + P(lm) + A(lm) is the pair-overlap exponent, and the
window constants (albd, aubd, qlbd, qubd, psilbd, psiubd) are their
certified kappa = 0 ranges.

- Preamble, displays e:II.repeat through e:def.HH.pair.repeat
  (4655-4695).  Definitional.  At general kappa the Phi arguments
  acquire the margin shift and the nu-marginal becomes asymmetric --
  exactly the kernels the DS-condition port (dsfun_kappa.py)
  implements.  The quoted identities P(0) = A(0) = 0, P(1) = -P_star,
  A <= 0, H(0) = 0, H(1) = -H_star are inherited from Sections 3-6,
  all audited VERBATIM at general kappa.  Verdict: BOUNDED CHANGES
  (definitional insertion of the margin, no proof content).

- Lemma l:ell.A.large.A.improved (4711, computer-assisted):
  1 - ell(A) <= 1.78/A + 4.3/A^2.  Proof anatomy: (i) the exact
  algebra e_H(A) = A(1-m^2)/(Delta+1) and the sandwich
  1 <= Delta <= A giving e_H <= sqrt(1-m^2) + |m|/A -- margin-free,
  VERBATIM; (ii) monotonicity of the integrand in psi (both signs
  worked out) -- generic calculus, VERBATIM; (iii) the final display
  bounding 1 - ell(A) by (2/(A(1-qubd))) times a truncated Gaussian
  integral, evaluated numerically to get 1.78 and 4.3.  The two
  constants are explicit functionals of (qubd, psilbd, psiubd), so at
  each of our margins they are re-derived by two arb integrals over
  the certified (q, psi) enclosure plus the phi-tail beyond the
  truncation.  Verdict: analytic skeleton VERBATIM; constants
  REPLACED BY CERTIFICATION per margin.

- Corollary c:entropy.near.one (4773): H(lm) - H(1) <=
  0.81 iota + (iota/2) log(1/iota) for iota <= 0.025.  Consumes the
  lemma, the numeric threshold iota(100) > 0.025, and the prior-side
  derivative identity e:dHH.dlambda (kappa-free given (q, psi)).
  The constant 0.81 = log(1.83)/2 + 1/2 and the 0.025 threshold
  become per-margin outputs of the same certified quantities.
  Verdict: VERBATIM structure, per-margin constants.

- Proposition p:sqrt (4802): (P(lm) - P(1))/iota^{1/2} <=
  0.285 iota^{1/2} - 0.45.  Three ingredients.  (i) e:pos.sqrt is
  monotone bounding of the explicit middle term by window constants
  -- VERBATIM with per-margin constants.  (ii) The change of
  variables and the z >= 0 / z <= 0 case split with log bPhi
  monotone: at general kappa the split point moves to the (certified)
  kappa-shifted crossing of the Phi argument -- BOUNDED CHANGES, the
  same species as the port's R1a tail split at the certified xi = 1
  crossing, already implemented and tested there.  (iii) The final
  two double integrals over [0,9]^2 and [-9,0]x[0,9] evaluated to
  -0.45 -- REPLACED BY CERTIFICATION per margin.  The qualitative
  conclusion that S'(lm) -> infinity as lm -> 1 (consumed at line
  4632) survives at a margin iff the certified sqrt-coefficient
  stays strictly negative there; it is a one-parameter family of
  certified double integrals, well inside the port's machinery.

- Proposition p:HH.PP.near.lambda.one (4703, proof at 4886):
  combination arithmetic of the corollary and p:sqrt; negativity for
  iota <= 0.02 is a two-line calculation from the constants.
  Verdict: VERBATIM structure; the threshold is recomputed per
  margin from the certified constants.

- Lemma l:ell.bounds (4904): ell(A) sandwiched by ell_In, ell_Out
  with gap <= 1.4e-11.  Proof: dD/dpsi sign analysis and the clean
  special-function fact |x tanh'(x)| <= 2^{-1/2} (proved by convexity
  of cosh x - sqrt2 x) -- all VERBATIM at any kappa.  The gap
  constants scale linearly with the width of the (q, psi) enclosure:
  theirs is ~1e-12 wide at kappa = 0; ours at the seven margins is
  set by the deep alpha location (tol 2e-6) and the fixed-point
  enclosures, giving sandwich gaps ~1e-6 rather than 1e-11.
  OBLIGATION (quantitative, not structural): verify Section 9's
  slack budget absorbs the wider sandwich at each margin -- this is
  a per-margin inequality check inside the port, not new mathematics.

- The endpoint package consumed at lines 4628-4635 decomposes as:
  (1) S(0) = S'(0) = 0: from P(0) = A(0) = H(0) = 0 and the
  stationarity identities; at general kappa these are the assembly
  identities verified symbolically in this repo (sympy battery items
  17-19, stationarity_psi/q and dRdq assembly) on top of audited
  Sections 3-4.  VERBATIM (verified).
  (2) S(1) = -G_star: their exact calculation at kappa = 0; the
  lm -> 1 limit computation redone with the kappa-shifted kernel is
  mechanical (dominated convergence to the diagonal), and for the
  second-moment argument only S(1) <= -c < 0 is consumed, which is
  also available as a certified bound.  BOUNDED CHANGES (with the
  certified-inequality fallback).
  (3) S'(lm) -> infinity at 1: from p:sqrt, see above.
  (4) S''(0) <= P''(0) + H''(0): from A <= 0 = A(0), A'(0) = 0
  (audited Section 3 discussion, general kappa) -- a maximum at 0
  forces A''(0) <= 0.  VERBATIM.
  (5) P''(0) + H''(0) < 0: their Proposition p:grid.result(c);
  REPLACED BY CERTIFICATION per margin through the port.

Section 9 head (p:grid.result, 5018): parts (a), (b), (c) are the
grid-certified negativity, first-derivative sign, and
second-derivative negativity of the pair exponent over the lambda
ranges; the consequence S(lm) <= 0 with equality only at 0 and 1 is
the full Condition c:G.  At the seven margins this proposition is
wholesale REPLACED BY CERTIFICATION: the DS-condition port
(ds_condition.py + dsfun_kappa.py, currently gated 19/19 and
awaiting the A06 re-audit) evaluates the same PG/QG bounds with arb
over the certified (q, psi, alpha) enclosures.  Their Sections 9.1-9.3
(function-value, first-derivative, second-derivative grid bounds)
and Section 10 (special-function estimates; the Mills family our
lem:mills strengthens) exist to make their grid rigorous at
kappa = 0 and are not consumed once the port's certificates replace
the grid wholesale.

## Tally for Sections 2-7

Sections 2-4: 15 VERBATIM, 1 BOUNDED CHANGES (Remark 2.1,
two-parameter perturbation consuming the slab rectangles), 0
OBSTRUCTION.  Section 5: 8 VERBATIM.  Section 6: 4 VERBATIM.
Section 7: 7.1 and 7.2 VERBATIM; 7.3 OBSTRUCTION as written
(kappa = 0 reflection in the dR/dq half; conclusion true, repaired
by the margin paper's Lemma on dR/dq - verified against the source
by the parent session, including the shared theorem counter and the
verbatim change of variables); 7.4-7.7 REPLACED BY CERTIFICATION;
assembled proofs BOUNDED CHANGES pending the Section 8 endpoint
package.  Section 8: preamble BOUNDED (definitional); analytic
skeletons of all five statements VERBATIM at general kappa; the
five numeric steps REPLACED BY CERTIFICATION per margin; endpoint
package decomposed 2 VERBATIM (verified symbolically), 1 BOUNDED
(S(1), with certified-inequality fallback), 2 CERTIFICATION; one
quantitative obligation (Section 9 slack vs our wider enclosures).
Section 9 head: p:grid.result wholesale REPLACED BY CERTIFICATION.  The chf-decay entry (Lemma 5.4) was independently
spot-checked against the source by the parent session and stands.

## Tally for Sections 2-4 (superseded above; kept for history)

Seventeen numbered statements audited: fifteen VERBATIM, one BOUNDED
CHANGES (Remark 2.1: the continuity step becomes a two-parameter
perturbation and consumes rectangle-form certificates), zero
obstructions inside Sections 2-4.  The two kappa = 0-specific defects
found live outside: the hidden reflection in Lemma 7.3 (obstruction as
written, repair in hand) and the Section 8-9 endpoint and
second-derivative package invoked at line 4628 and 4635 (open numerical
obligations at kappa != 0, of the univariate species this repo's
certification machinery handles).  Typos found, all kappa-independent:
the derivative display (63) (E for E'), the reflection identity (159)
(sign), and the cushion-constant bookkeeping in Proposition 2.3's
endgame.  No statement in Sections 2-4 cites an external a priori bound
proved only at kappa = 0: the Kim-Roche adaptation is self-contained
(Proposition 2.3), the state-evolution citations are
nonlinearity-generic, the Mills-family bounds (Lemma 10.1) are stated
for all real arguments, and the two-sided capacity bound of
Kim-Roche/Talagrand quoted in their introduction is never consumed by
the proof of Theorem 1.1 or 1.4.

## NEXT

Sections 2-8 are audited above (2-4, 5, 6, 7 with the 7.3 repair, 8
with the endpoint-package decomposition), and the Section 9 head
(p:grid.result) is dispositioned as wholesale replacement by the
port's certificates.  Remaining, in dependency order:

1. The port's acceptance: the A06 re-audit verdict on dsfun_kappa.py
   (sha 3E48F9B2...6866, gated 19/19, gitignored UNACCEPTED until the
   verdict lands).  Everything Section 8-9 needs numerically routes
   through it.
2. The Section 9 slack-budget check at the seven margins: our
   (q, psi) enclosures are ~1e-6 wide against DS's ~1e-12, so the
   l:ell.bounds sandwich gap grows accordingly; verify per margin
   that the PG/QG negativity margins absorb it (an inequality check
   inside the port, no new mathematics).
3. DONE (paper Lemma lem:S1, 07-17): the lm -> 1 dominated-
   convergence computation at general kappa is written out in the
   lower-bound section - single lambda-free integrable majorant,
   |log Psi(M(z))| <= C_s(1+z^2) with M affine in |z| - and passed
   a hostile-referee audit on six attack points (verdict: no
   substantive defect; two citation-precision fixes applied: the
   lambda-up-to-1 limit convention now stated, and the Mills
   parenthetical corrected to E' in (0,1) plus E(0) = sqrt(2/pi)).
   The referee also verified H(1) = -H_star's chain by hand at
   general kappa and found no hidden kappa = 0 dependence.
4. The per-margin certified constants for Section 8's five numeric
   steps (1.78/4.3, iota(100) > 0.025, 0.285, -0.45, and the
   combination threshold 0.02), emitted by the port at each of the
   seven margins once accepted.
5. The Nakajima-Sun sharp-threshold transfer on the positive side
   (independent cross-check; unchanged status).
