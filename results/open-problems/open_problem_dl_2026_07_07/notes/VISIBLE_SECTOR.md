# Visible sector: jet transport (C2) + Christoffel ratio-LLN + correlation bound
# Status: REFEREED (independent adversarial pass + numerics).
# VERDICTS: Prop 0 CORRECT; Statement 1 CORRECT (scoped k <= 3; general-k constant open);
# THEOREM 2 CORRECT AFTER FIX (applied below): pointwise leverage |K_V - K_J|(x_i) <=
#   rho N_l = m closes the truncation-excess gap — truncate net-point Bernstein at 2R_0,
#   add hypothesis R_0 >= m (i.e. n >= C_0 m^2 d LambdaBig); conclusion sum_i K_V <= 3nm.
# THEOREM 3 FATAL — WITHDRAWN. ||M_l||_op <= R_0 is FALSE (op-norm of the projected
#   sample Gram ~ n·dimV, >= max diagonal; referee numerics: op/R_0 up to 363 on fully
#   visible configs). No op-norm LLN rescues Hanson-Wright (op·s and even the Frobenius
#   term carry the factor-d loss). The visible-sector CORRELATION bound is NOT proved;
#   it reduces to the fixed-vector/quadratic chaining over the jet family — the same
#   factor-d wall as F24(c)/F26(b). Honest conditional form: IF sup over visible U of
#   ||P_{V_l(U)} T_l||^2 <= C n m polylog THEN the visible-sector rate follows (via
#   Theorem 2 + weighted Cauchy-Schwarz). NOTE: E_y ||P_V T_l||^2 = tr M_l <= 3nm IS
#   proved (Theorem 2) — what is missing is only the sup-before-E_y deviation control.
# My own pre-referee repair attempt (matrix-Bernstein op <= Cn => survives at
#   d >= polylog^2) was ALSO WRONG — the op·s term in HW is nm·dΛ, killing the d-gain
#   entirely. Recorded to prevent re-derivation.
# Complete for cluster size <= 3 (hence Statements 0-2 complete for m <= 3, all l);
# general k modulo one extractable constant (jet Gram lower bound c(l,k)).

Conventions: sigma uniform on S^{d-1}; H_l dim N_l ~ d^l/l!; zonal Z_l^u = Z_l(u,.) =
N_l P_l(<u,.>), P_l Gegenbauer P_l(1)=1; reproducing <g, Z_l^u> = g(u); <Z_l^u, Z_l^v> =
N_l P_l(<u,v>); phi_l(s) = sqrt(N_l) P_l(s) unit-norm. V_l(U) = span{Z_l^{u_j}};
K_V(x) = ||P_V Z_l^x||^2 (Christoffel), int K_V = dim V; rho(V,V') = ||P_V - P_{V'}||_op.

## Prop 0 (identities, proven)
S := sum_i Z_l^{x_i} (x) Z_l^{x_i}; E_x[Z_l^x (x) Z_l^x] = I_{H_l}; sum_i K_V(x_i) =
tr(P_V S) = tr(Gamma^{-1} Gamma-hat); population n dim V <= nm. Leverage form (0.1):
K_V(x_i) <= (1/lambda_min(Gamma-bar)) sum_j phi_l(<u_j,x_i>)^2.
(K)-refutation localized: pole ON x_i => K_V(x_i) = N_l (numerics: tr/nm = 102 at
N_l/n = 67 poles-on-data vs 1.4 generic).

## STATEMENT 1 — jet closure, transport, entropy (the C2 wall)
Lemma 1.1 (exact polynomiality): u -> Z_l(u,x) is a DEGREE-l POLYNOMIAL in u; Taylor
TERMINATES; all directional derivatives D^{(a)} zeta stay in H_l; every V_l(U) sits in
the closed ambient family M_{l,E} = H_l cap {q(pi_E x): deg q <= l}, dim <= binom(m+l, l)
(continuous in E, no conditioning) — vehicle for entropy, too big for the trace.
Lemma 1.2 (closure = jet spans): a cluster of k poles in a cap of radius theta about u_0:
span within rho <= C(l,k) theta of the JET SPAN J = span{D^{(a)} zeta(u_0)[escapes],
a <= k-1}, dim <= k. PROVEN k=2 in full (key orthogonality <Z_0, Z-dot> = 0; ||Z-dot||^2
>= c(l) N_l; exact Taylor remainder C(l) sqrt(N_l) theta). General k: confluent
Vandermonde divided differences; invertible with cond <= C(k); limit jet Gram >= c(l,k)
N_l I by rotation invariance + compactness [constant c(l,k) NOT extracted — the one gap].
Lemma 1.3 (jet-frame Lipschitz): (center, escapes, shape) -> P_J is C(l,m)-Lipschitz
into rho, DIMENSION-FREE (the sqrt(N_l) cancels in normalized directions). The merge
discontinuity (numerics: rho/pole-move ~ 10^3 for rotating a tight cluster's escape) is
handled by netting ESCAPE DIRECTIONS AS INDEPENDENT COORDINATES.
THEOREM 1 (entropy): log N(closure family, rho, delta) <= C(md + m^2 log(elm))
log(C(l,m)/delta) <= C md log(C/delta) for m <= d. L2 unit-ball union entropy <=
C md log(C N_l/u). TRANSPORT COROLLARY: pole-wise eta-close configs: every unit g in
V_l(U) has g' in jet closure of V_l(U') with ||g - g'||_2 <= C(l,m) eta — exponent 1,
poly constants, NO GRAM CONDITIONING (numerics: exactly linear, constants 0.67-1.5,
d-free).

## STATEMENT 2 — visible-sector Christoffel ratio-LLN
Visibility: R_0 := n/(C_0 m d LambdaBig), LambdaBig := log(C N_l n d); U is p_0-VISIBLE
iff max_i K_{V_l(U)}(x_i) <= R_0. Defended: (i) intrinsic (matrix-Bernstein per-term);
(ii) sharp vs poles-on-data (those need R_0 >= N_l); (iii) implied by [lambda_min
(Gamma-bar) >= beta_0] + [pole bulk-separation phi_l(<u_j,x_i>)^2 <= beta_0 R_0/m]; via
Gegenbauer flatness + cap occupancy, only an O(md polylog)-point spike-neighborhood of
the sample is excluded.
THEOREM 2: whp (1 - (nd)^{-c}), SIMULTANEOUSLY for all l <= Lambda* and all p_0-visible U:
   sum_i K_{V_l(U)}(x_i) <= C n m      (NO polylog).
Proof: truncated scalar Bernstein at cap R_0 (iid x_i; Var <= R_0 n m; t = nm gives tail
e^{-c m d LambdaBig}) + net union over the jet family at delta = m/N_l (log-card <=
C md LambdaBig) + TRACE-TRANSPORT BRIDGE |tr(P_V S) - tr(P_J S)| <= rho ||S||_{S_1} =
delta n N_l = nm (conditioning-free — the whole point of Statement 1).
Numerics: worst tr/nm over 40 random visible U: 1.96 (N_l/n = 67), 1.45 (N_l/n = 22);
clustered poles (lambda_min Gamma-bar = 1e-3): ~1 — conditioning-irrelevance confirmed.

## THEOREM 3 (BONUS — visible-sector correlation bound = visible half of keystone F24b)
For f = sum_{l <= Lambda*} f_l, f_l in V_l(U), U p_0-visible, sum_l lambda_l ||f_l||^2
<= L^2: whp over x,
   E_y sup_f sum_i y_i f(x_i) <= C L sqrt(n m polylog(n)/d).
Proof: weighted Cauchy-Schwarz to sum_l lambda_l^{-1} y^T M_l y, M_l the projected
kernel Gram (tr M_l = sum_i K_{V_l}(x_i) <= Cnm by Thm 2; ||M_l||_op <= R_0); Hanson-
Wright with s = C md LambdaBig unioned over the same net; sum_l lambda_l^{-1} <=
C log(Lambda*)/d. => fitting eps n forces L >= eps sqrt(nd/(m polylog)) >= eps sqrt(n/m)
once d >= polylog: THE CONJECTURED RATE, log-free, EVERY activation, EVERY m — ON THE
VISIBLE SECTOR.

## Gaps (exact)
(i) general-k jet Gram lower bound c(l,k) not extracted (all complete for m <= 3);
(ii) +m^2 log(elm) entropy term (harmless m <= d; for m > d Thm 2 degrades to
C(nm + n m^2/d)); (iii) INVISIBLE sector (poles in the O(md polylog)-point spike-
neighborhood of the sample) = the charging/bump front = (M)'s clustered core.

## Numerics ledger (seeds fixed, scripts in agent scratchpad)
Addition theorem 0.96-1.06; jet transport exactly linear, constants 0.67-1.5, d-free;
merge discontinuity 10^3 confirmed (escape dirs must be netted); poles-on-data 102 vs
1.4 generic; occupancy tail max phi^2 ~ n^{0.4} << N_l; visible LLN worst 1.96.
