# FEI: the L1 form, the support form and the chain flow (an agent, 9-10 Nov 2026)

Status of every line: PROVED means a short proof is written here and the statement passed check_p.py on all
4-variable functions and a 6-variable sample; OPEN means not proved by anyone. Nothing here bounds the FEI constant.

Notation. g_S = D_S f, a function of the coordinates outside S, values in 2^(1-|S|) Z, |g_S| <= 1.
mu(S) = (E g_S)^2 = fhat(S)^2, up(S) = E g_S^2, alpha(S) = E|g_S| (abs1 in STATE.md), p(S) = P[g_S != 0].
A = sum mu log(1/up), A1 = sum mu log(1/alpha), Gamma = sum mu log(alpha/|fhat|), P = sum mu log(1/p),
Q = sum mu log(up/alpha^2), B = sum mu log(up/mu). Logs base 2.

## 1. Exact identities and two-sided bounds (PROVED)

(a) H = 2 A1 + 2 Gamma.            (b) A1 = (A + Q)/2, A1 <= A <= 2 A1 (from up <= alpha <= sqrt(up)).
(c) B = Q + 2 Gamma <= A + 2 Gamma (FEIB01 found the second form; it is up <= alpha, alpha >= up termwise).
(d) P <= Q <= P + (I - Var):  (E|g|)^2 <= p E g^2 (Cauchy-Schwarz on the support) and E g^2 <= E|g|,
    E|g| >= 2^(1-|S|) p (granularity).  Also P <= A <= P + 2(I - Var).
So  2P + 2 Gamma <= H <= 2P + 2 Gamma + 2(I - Var)  (A1 <= P + I - Var directly from granularity; FEIB08), and
    FEI  <=>  A1 <= C I and Gamma <= C I  <=>  P <= C I and Gamma <= C I.
P-conjecture in words: for a spectral sample S, the restriction of f to S (outside fixed at random) has full degree
|S| with probability at least 2^(-C|S|) on log-average. Gamma-conjecture: the top coefficient of that restriction
keeps a sign bias 2^(-C|S|) on log-average. A1 >= Var log(1/max_i Inf_i), so A1 <= C I already contains KKL.
On the 4-variable balanced record (H 3, I 1.5): A1 1.5, P 1, Gamma 0, so the record is all containment.

(e) Isoperimetric step: 2 p(S) log(1/p(S)) <= sum_{j not in S} p(S + j).
    Proof: the support of g_S has density p; its edge boundary is at least |supp| log(1/p) (edge-isoperimetric
    inequality on the cube); a boundary edge in direction j is a point where D_j g_S != 0.
(f) Level form: B <= sum_d W_d log(M_d / W_d), W_d the level-d weight, M_d = sum_{|S|=d} up(S) = E C(|U|,d).
    (Jensen inside each level.) With Theorem 1: H <= 2I + 2 sum_d W_d log(E C(|U|,d)/W_d).
    Gives H = O(I) when |U| is sub-exponential at scale I; gives sqrt(n) (the truth) for majority; loses a
    log I on tribes (the Poisson number of tribes hit). Literature check owed: Keller-Mossel-Schlank 2012.

## 2. The chain flow (PROVED identities)

Draw S from mu and order it uniformly at random; R_j = its first j elements. Flow through a set R of size r:
    m(R) = sum_{S contains R} mu(S) / C(|S|, r),      sum over all R of m(R) = I + 1.
Telescoping log(1/alpha(S)) along the chain:
    A1 = sum_{R nonempty} m(R) * (1/|R|) sum_{s in R} log( alpha(R - s) / alpha(R) ),
so A1 / I is the m-average of the mean cost of the last step into R. A1 <= C I says the expensive steps
(alpha drops by 2^(-t), t large) carry at most a C/t share of the flow.

Generalized Talagrand bound (PROVED, constant 1): with L(R) = ln( ||g_R||_2 / ||g_R||_1 ),
    m(R) <= up(R) * min(1, r! / L(R)^r).
Proof: 1/C(k+r,r) = r int_0^1 t^k (1-t)^(r-1) dt, so m(R) = r int_0^1 ||T_sqrt(t) g_R||^2 (1-t)^(r-1) dt;
Bonami gives ||T_sqrt(t) g||_2 <= ||g||_(1+t); interpolation gives ||g||_(1+t)^2 <= ||g||_2^2 exp(-L(1-t)).
r = 1 is Talagrand's inequality: sum_{S contains i} mu(S)/|S| <= 2 Inf_i / ln(1/Inf_i).
Hypercontractive size statement (same proof): sum_{S contains R, |S - R| <= k} mu(S) <= rho^(-2k) ||g_R||_(1+rho^2)^2,
so a peaked derivative (L large) has almost all of its supersets at distance >= c L above R.

Level-1 theorem (PROVED): E_S log(1/min_{i in S} Inf_i) <= C I. Proof: P[S contains i, |S| <= k] <= 3^k Inf_i^(3/2);
sets with |S| >= (1/4) log_3(1/Inf_i) pay for themselves; the rest cost sum_i Inf_i^(5/4) log(1/Inf_i) = O(I).
This works because the budget at level 1 is sum_i up(i) = I.

## 3. Where the proof of A1 <= C I stops (OPEN)

At level r >= 2 the same accounting needs a budget for the sets R of size r. The candidates:
  sum_{|R|=r} up(R) = E C(|U|, r)    too large (exponential moments of |U|; majority has n^(r-1/2));
  sum_R m(R) = I + 1                  exact, but m(R) is the flow itself, so nothing is gained;
  u1(R) = sum_{S contains R} mu(S)/C(|S|-1, r-1), sum_{|R|=r} u1(R) = E[|U|; |U| >= r]/r, total about I ln(deg):
        (this harmonic sum is NOT the source of the log in KKLMS Theorem 1.3; FEIB08 traced that log to their
        Corollary 6.7 / eq. (16).)
Fixed level (PROVED by FEIB09, re-derived by hand and checked by code/check_feib09.py on all n=4 functions and 9,003
n=6 ones): with A_r = E_S log(1/max_{R in S, |R|=r} up(R)) (A_r = 0 on |S| < r),
    A_1 <= 3.520226 I,   A_r <= r A_1 + I/ln 2,   A_2 <= 6.1033 I,   A_3 <= 7.872677 I.
The product reference measure costs the factor r. No summable per-level budget exists: AND_(2r) forces the level-r
increment to be at least 1/(2r) of I.
What is needed is a cross-subsidy rule: each U pays w(U,S) >= 0 to its subsets, sum_{S in U} w(U,S) <= C|U|, and
    mu(S) log(1/alpha(S)) <= C|S| mu(S) + sum_{U contains S} mu(U) w(U,S).
Talagrand is the rule w(U,{i}) = 1. A pointwise rule in U cannot work (AND: U = [n] would owe (3/2)^n), so the
rule must use the local data of f around S (the derivative's peakedness L(S) and the sizes of the supersets).
Granularity loses 2^r if one converts L1 influences of g_R to L2 ones termwise; working with a fixed p-norm
(4/3 or 3/2) instead of L1 avoids that: with beta(R) = ||g_R||_p, the p-chain cost is within a factor p of A1 and
    P[V contains s, |V| <= k | U contains R] <= rho^(-2k) exp(-2 L_p(R + s)) P[V contains s | U contains R].

## 3b. The label-time flow and "the tail pays" (9 Nov 23:5x; idea, partly proved, NOT yet checked numerically)

Give each element of S ~ mu an independent uniform label; R_t = the elements with label < t. Then
    P[R_t = R] = t^|R| F_R(1 - t),   F_R(u) = sum_V ghat_R(V)^2 u^|V| = <g_R, T_u g_R>.
PROVED (level inequality + Cauchy-Schwarz on the support): sum_{|V| <= k} ghat_R(V)^2 <= 3^k ||g_R||_{4/3}^2
<= 3^k up(R) p(R)^(1/2). In words: given U contains R, U has at least c log(1/p(R)) further elements except with
probability p(R)^(1/4). So a prefix R with a sparse derivative is always followed by a long tail, and the tail
could pay for log(1/p(R)): cost of the prefix <= C |S - R|.
Conjecture T (to test first on the census): E log(1/p(R_t)) <= C_t I for t = 1/2, and the relative form for the
increments R_t -> R_(1+t)/2 with the same C; summing the geometric series of remaining sizes would give P <= 2 C I.
Where the proof of T stops: the bad event {|S - R| <= k} has flow sum_{|V|<=k} ghat_R(V)^2 (1-t)^|V|, to be compared
with the flow F_R(1-t) through R, not with up(R). A lower bound on F_R(u) = <g_R, T_u g_R> is needed. For g_R of one
sign F_R(u) >= (E|g_R|)^2 and reverse hypercontractivity applies; for a signed g_R the loss is the noisy cancellation
ratio <|g|, T_u |g|> / <g, T_u g>, whose u = 0 value is exactly the Gamma term (alpha/|fhat|)^2. So the two halves
meet again here: containment along the flow is provable up to a noisy version of Gamma.
Caution: for f with every D_S f of one sign (read-once formulas are in this class), alpha = |fhat| and A1 = H/2
identically, so the L1 form gives nothing new there; H <= 2I + 2P still holds and FEI on that class is P <= C I.
CORRECTION (10 Nov, FEIB12 and FEIB13): this holds for the NONEMPTY derivatives only. For a biased f the empty set
contributes Gamma = b^2 log2(1/|b|) with b = fhat(empty) (at most I/(2 ln 2)). AND_2: mu(empty) = 1/4, H = 2, P = 1/2,
I = 1, Var = 3/4, 2P + 2(I - Var) = 3/2, and the missing half bit is the empty term (Gamma = 1/4 bit).
The exponential-moment shortcut sum_S mu(S) 2^(-C|S|)/p(S) <= K is false on tribes (it needs 2^(-C) of order 1/w).

## 4. Exact potential formulas over the (E, D) tree (PROVED, for the record)

For any functional N with N(f) = 1 on Boolean f and N(c) = |c| on constants (L1, Lp, L-infinity norms all qualify),
unrolling coordinates in any order:
    H/2 = sum over tree nodes g of  ||E g||_2^2 log(N(g)/N(E g)) + ||D g||_2^2 log(N(g)/N(D g)),   I = sum ||D g||_2^2.
Different N move the cost between nodes; the entropy chain rule is N = the L2 norm (node cost (||g||^2/2) h(split);
FEIB08). With N = L-infinity the
root and the first D-steps cost nothing; the cost sits where averaging kills the sup norm. No N makes every node
locally payable: with N = L1 the constant node a + b x, |b| <= |a|, costs b^2 log(|a|/|b|) against a payment b^2,
and the Boolean root costs h(Inf_i) against Inf_i. That is the potential problem FEIB06 is searching.

## 5. The cancellation half B, the superset coupling, the noise form (10 Nov 00:3x-00:5x; hand-derived, numerics owed)

Coupling nu: draw S ~ mu, then U ~ mu conditioned on U containing S. nu(S,U) = mu(S) mu(U) / up(S) on S in U.
w(S) = mu(S)/up(S) = P[U = S | U contains S] = (E g_S)^2 / E g_S^2.   Z_U = sum_{S in U} w(S).

(a) PROVED (one line each).  E_{U~mu} Z_U = 1 (Kraft), so nu is a probability and its U-marginal is mu Z.
    A = D(nu || mu x mu)   (the density is 1[S in U]/up(S)).
    B = E_nu log(1/w(S)) = H_nu(S | U) - D(mu Z || mu),   hence B <= H_nu(S | U) <= H.
    B is 2-homogeneous on real f and is 0 exactly when the spectral support is an antichain.
(b) PROVED. Recursion f = E + x_n D:  B(f) = B(E) + B(D) + sum_T Ehat(T)^2 log(1 + up_D(T)/up_E(T)).
    Unrolled in any order of the coordinates:
        B = E_S sum_{k not in S} log( 1 / (1 - pi_k(S)) ),   pi_k(S) = P[k in U | U_{>k} = S_{>k}, U_{<k} contains S_{<k}].
    Only absences cost. With the conditioning U_{>k} = S_{>k} alone this sum is the entropy chain rule's absence
    part and is at most I/ln 2; the extra "U_{<k} contains S_{<k}" is the whole difficulty. The node a + b x costs
    a^2 log(1 + b^2/a^2) <= b^2/ln 2, so (unlike section 4) the T = empty term of every node is locally payable.
(c) PROVED. Noise form. Thin U by keeping each element with probability rho = 1 - u: the thinned law is
    tau_rho(S) = rho^|S| <g_S, T_u g_S>, the averaged spectral measure of a rho-random restriction. Put
        Phi(u) = E_{S~mu} log( 1 / <g_S, T_u g_S> ),      Phi(0) = H,  Phi(1) = A,  Phi decreasing.
    Gibbs: H <= Phi(u) + I log(1/(1-u)).  So for any fixed u < 1:  FEI  <=>  Phi(u) <= C I.
    Containment is the endpoint u = 1; the cancellation half is the statement that <g_S, T_u g_S> is not much smaller
    than E g_S^2 on log-average. Log-convexity in t = ln(1/u) gives only
    Phi(u) <= A + ln(1/u) E_nu |U - S| / ln 2, and E_nu |U - S| is of order n on majority (I is sqrt n): too weak.
(d) Necessary Renyi form (Jensen on A = E_S log(1/P_U[U contains S])):  containment A <= C I implies
        WC:   P_{S,U iid mu}[S in U] = sum_S mu(S) up(S) = E_x sum_S fhat(S)^2 (D_S f(x))^2  >=  2^(-C I).
    WC is implied by Fourier min-entropy-influence (max mu >= 2^(-C I)) and is weaker; it is trivial unless f is
    nearly balanced. Section 3's fixed-level theorem should give 2^(-C I^2). OPEN; a natural first target.
(e) Sparse-set split, PROVED: S pays for itself when |S| >= log(1/p(S))/K, so
        P <= K I + sum_{S: p(S) < 2^(-K|S|)} mu(S) log(1/p(S)),   and mu(S) <= p(S) up(S) <= p(S)^2.
    The level inequality sum_{|V|<=k} ghat_S(V)^2 <= 3^k p(S)^(1/2) up(S) says a sparse S has w(S) <= p(S)^(1/2) and
    all but a p^(1/4) share of its supersets at distance >= c log(1/p(S)).
(f) Three shortcuts that are FALSE (do not retry):
    - sum over sparse S of p(S)^(2-eps) <= C I: on majority the pairs alone give n (mu <= p^2 loses everything
      there; the weight must stay mu). On tribes it holds once K >= 6.
    - B <= C E_nu |S| log(e|U|/|S|) <= C' I: the first inequality is true (count subsets of U) but the right side is
      not O(I): f = MUX(AND_L(y); a random g on k bits; parity on 2^L k bits) has it of order k L against I ~ 1.5 k.
    - E_nu |U| <= C I (majority, as in (c)).
(g) Axiomatic question (round 3, FEIB10): for a probability mu on finite sets with
        (C)  mu{U contains R, |U - R| <= k} <= 3^k 2^|R| up(R)^(3/2)   for all R, k
    (what granularity and the level inequality give for derivatives), does E log(1/up(S)) <= C E|S| follow?
    By hand on two-scale measures: every R is rare (N_R <= (3/2)^(I-r)) or common (N_R >= N 9^-(I-r) 4^-r); "only the
    empty set is common" is impossible once log(1/up(S))/|S| exceeds about 3.2; uniform I-subsets and product
    structures violate (C). Neither a proof nor a counter-measure.

STATUS of section 5 (10 Nov): the identities of (a)-(e) are CHECKED by code/check_sec5.py on all 65,536 functions
of 4 variables and on AND_2..16, MAJ_3..15, tribes (width 2, 3, 4, up to 16 variables), address functions k = 1, 2, 3:
up = E g^2, Kraft, B = E_nu log(1/w), Phi monotone, the Gibbs bound; errors <= 7e-16, no violation.
Tables: code/check_sec5_census4.txt, code/check_sec5_fam16.txt. The recursion of (b) is not coded yet.


6. What the section-5 routes can and cannot do (10 Nov, by hand; numerics where stated)
=======================================================================================

(a) Conjecture W of FEIB13 item 3 is FALSE for every absolute c. On tribes with s tribes of width w, delta = 2^-w,
    a set S touching k tribes has
        mu(S) = 4 (1-delta)^(2(s-k)) delta^(2k),      up(S) = 4 delta^k 2^-|S| (1-delta)^(s-k),
    so  W_c = sum_{S nonempty} mu(S) c^-|S| / up(S) = (1 - delta + delta((1+2/c)^w - 1))^s - (1-delta)^s.
    At s = 2^w ln 2 this is about exp(ln 2 (1+2/c)^w), doubly exponential in w, against K^(I/Var) = K^(O(w)).
    CHECKED against the table (TRIBES_3x5, c = 2: 1.815).
    The theta-variant
        W_theta,c(f) = sum_S mu(S) c^-|S| up(S)^-theta          (S = empty included; it contributes mu(empty))
    on tribes equals 4^(1-theta) [ ((1-delta)^(2-theta) + delta^(2-theta)((1 + 2^theta/c)^w - 1))^s - (1-delta)^((2-theta)s) ]
    plus mu(empty), and stays bounded exactly when
        1 + 2^theta / c <= 2^(1-theta)          (theta = 1/2: c >= 3.42;  theta = 3/4: c >= 8.9;  theta = 1: never).
    AND_n gives the same condition. Majority is harmless for every theta <= 1 (up(S) ~ n^(-1/2)/|S|, so the sum is
    of order n^(theta/2)).
    W_theta,c is multiplicative under XOR of functions on disjoint variables, and by Jensen
        W_theta,c(f) <= K^I(f)   implies   A <= (log2 K + log2 c) I / theta.
    So one may ask (W_theta): W_theta,c(f) <= K^I(f) for all Boolean f, some theta in (0,1), c, K absolute; a tail
    bound P_mu[ up(S) < c^(-|S|/theta) 2^-t ] <= K^I 2^(-theta t).

(a') W_theta is FALSE for every theta > 0, c, K: containment has no exponential moment.
    AND of s disjoint copies of g (f = -1 iff all copies are -1), beta = P[g = -1], S touching the copies in K, k = |K|:
        mu_f(S) = 4 beta^(2(s-k)) prod_{j in K} mu_g(S_j)/4,     up_f(S) = 4 beta^(s-k) prod_{j in K} up_g(S_j)/4,
        W(f) = (1 - 2 beta^s)^2 + 4^(1-theta) [ (beta^(2-theta) + 4^(theta-1) W0(g))^s - beta^((2-theta)s) ],
    W0(g) = sum over nonempty S of mu_g c^-|S| up_g^-theta. As s grows I(f) = s beta^(s-1) I(g) -> 0, so W(f) <= K^I(f)
    for all s forces beta^(2-theta) + 4^(theta-1) W0(g) <= beta, i.e. (using g and -g)
        (N)   W0(g) <= 4^(1-theta) min over b in {beta, 1-beta} of b (1 - b^(1-theta)),
    and (N) implies W(g) <= 1. So the K-form for all f, the form "W <= 1" for all f and (N) for all g are equivalent.
    (N) for the dictator is the tribes condition above. But majority violates (N) for large n: its level-1 part alone is
        W0(MAJ_n) >= (1/c) (2/pi) (pi n/2)^(theta/2)  -> infinity
    (up(i) = Inf_i ~ n^(-1/2), with only O(1) of |S| to pay for it). Hence AND_s o MAJ_n breaks every (theta, c, K).
    What this says about any proof of containment: log(1/up(S)) is NOT bounded by C|S| set by set, not even in an
    exponential-moment sense; on majority the cost (1/2) log n sits on bounded levels and is paid by the heavy tail of
    |S| (E|S| ~ sqrt n). Containment is a budget statement, as in Talagrand's inequality
    sum_i mu(i) log(1/Inf_i) <= C I, where S pays with the mass above it: mu(S) log(1/up(S)) <~ up(S).
    (N) does hold with bounded c on tribes of every size (theta = 1/2: sup c* = 5.63 at width 4, s = 53) and on all
    4-variable functions (c* = 4.63): code/check_wstar.py; small cases do not see the majority effect.
    First order in theta, (N) is the AND-closed normalisation of containment:
        (C1)  A + kappa(b) Var <= C I,   kappa(b) = 2 + b log2(1/b)/(1-b),  b = max(beta, 1-beta),  3 <= kappa < 3.443,
    equivalent to containment up to the constant (Var <= I). It gives lower bounds for the containment constant:
        A(AND_s o g)/I  ->  A(g)/I(g) + [4 beta^2 log2(1/beta) + 8 beta (1-beta)] / I(g)     (s -> infinity),
    = 3 for g a dictator (AND_n), 3.434 for g = OR_2, 3.537 for g = OR_3, 3.530 for OR_4. So c_A >= 3.537 (not 3);
    tribes with s chosen freely give about 3.81 (width 3, s = 18, from the theta = 0.02 row of check_wstar_tribes.txt).
    The same computation for H:  H(AND_s o g)/I -> H(g)/I(g) + [8 beta^2 log2(1/beta) + 8 beta(1-beta)]/I(g);
    dictator 4, OR_2 5.37, OR_3 5.70, OR_4 5.65; for balanced g the gain is 4/I(g) (hand-computed, to check by code).

(b) A reference measure on the sets S themselves is FEI. If pi is a sub-probability on sets with
    E_S log(1/pi(S)) <= C I then H <= E_S log(1/pi(S)) <= C I by Gibbs. So any proof of containment by
    "up(S) >= pi(S) 2^(-C|S|)" must use a pi that is NOT summable to 1: sum_S up(S) = E 2^|U|. FEIB09's fixed-level
    pi lives on sets of bounded size; a uniform-in-level proof needs references on proper subsets R(S) of S (or on
    pairs (R, k) as in axiom (C)). FEIB13 item 4 read with pi on S is the full conjecture.

(c) Local polynomial form. For x in the cube and a set S put
        a_x(S) = sum_{T in S} (-1)^|S-T| f(x^T)  =  (-2)^|S| D_S f(x)        (x^T = x with T flipped),
    the top coefficient of the restriction of f to the subcube x + span(S), an integer. Then
        up(S) = 4^-|S| E_x a_x(S)^2,     p(S) = P_x[ f restricted to x + span(S) has full degree |S| ],
        fhat(S) = (-2)^-|S| E_x a_x(S),
    so P = E_S log(1/P_x[full degree on x + span(S)]) and Gamma is the sign cancellation of the top coefficients.
    If a_x(S) != 0 then the restriction depends on every coordinate of S, and S meets every certificate of every
    point y of the subcube (a certificate of y disjoint from S fixes f on all of y + span(S) = the subcube).
    Containment in this language: a spectral sample S is, with probability 2^(-O(|S|)) on the log-average over S,
    a set on which a random subcube restriction of f has full degree.

(d) Elementary: mu(S) <= p(S) up(S) <= p(S)^2;  mu(S) <= 4^(|S|-1) up(S)^2 (integrality of a_x);  mu(i) <= Inf_i^2.

(e) WC. RECALLED (Kelman-Kindler-Lifshitz-Minzer-Safra; to confirm from the paper): the spectrum of a function of
    constant variance sits, up to a small mass, on 2^(O(I log I)) characters, so WC >= sum mu^2 >= 2^(-O(I log I));
    target (b) of FEIB11 is then known and the open part of WC is the removal of log I. The fixed-level theorem gives
    only log(1/WC) = O(I^2) (condition on |S|, |U| <= 2I).

(f) Not a counter-measure: mass on the empty set, on one set U_0 of size m (mass eta = r/m) and on the r-subsets of
    U_0 (total mass 1/2). Axiom (C) holds only when log(m/r) <= about 2 r log a (a = the constant of (C)), which
    caps A/I at (2/3) log a.

(g) Small influences are no loss (FEIB07, re-derived): the XOR of 4d disjoint copies of a d-variable f keeps H/I
    and B/I and has every influence below I/sqrt(n) once I(f) >= 1/2. A theorem for functions with all influences
    <= I/sqrt(n) is the full conjecture.

(h) Noise-weighted containment, recursion (hand-derived, NOT checked): for real g and
        A_rho(g) = sum_V rho^(2|V|) ghat(V)^2 log( ||g||^2 / ||D_V g||^2 ),
        A_rho(g) = sum_i rho^2 int_0^1 dt [ ||T_(rho sqrt t) D_i g||^2 log(||g||^2/||D_i g||^2) + A_(rho sqrt t)(D_i g) ].
    No induction hypothesis found for it.

(i) Symmetric functions are done (FEIB02, round 2; proofs in codex/workers/FEIB02/PROOFS.md, not yet refereed
    here): B <= 3.459354 I and Gamma <= (8/5) I for every symmetric Boolean f; majority has B/I -> 2/ln 2, so the
    route H <= 2B + 2I cannot give a symmetric constant below about 7.77. FEIB07: the coding route gives
    B <= sum_i h2(Inf_i) (an influence-log bound, not O(I)); disjoint-term DNF has B <= (1 + 4c/w_min) I.
    FEIB06: no local entropy potential certifies B <= C I under a universal root budget.

## 7. The restriction step, the erasure form and the good-coordinate form (10 Nov 01:1x-01:5x; hand-derived; numeric check = code/check_erasure.py)

Notation: U ~ mu the spectral sample. For a coordinate i write f = f0 + x_i f1 (f0 = E_i f, f1 = D_i f), and for
T not containing i: a_T = fhat(T), b_T = fhat(T + i). The two restrictions f(i -> +-1) = f0 +- f1 have spectra
(a_T +- b_T)^2, and their half-half mixture is a_T^2 + b_T^2 = the law of U - i.

(a) P <= B. By Cauchy-Schwarz mu(S) = (E g_S)^2 <= p(S) up(S), so w(S) = mu(S)/up(S) <= p(S) and
    P = E log(1/p) <= E log(1/w) = B. So FEI <=> B <= C I, and containment P <= C I is a consequence of it;
    B - P = E_S log( E[X^2 | X != 0] / (E[X | X != 0])^2 ), X = D_S f.

(b) The one-coordinate step (exact). Put
        D_i(f) := H(f) - (1/2) H(f(i->+1)) - (1/2) H(f(i->-1)).
    Then D_i(f) = E_i(f) + J_i(f), where
        E_i(f) := H( 1[i in U] | U - i ) = sum_T (a^2+b^2) h( b^2/(a^2+b^2) )          (erasure entropy of i)
        J_i(f) := JSD( spectrum of f(i->+1), spectrum of f(i->-1) )
                = sum_T (a^2+b^2) [ 1 - h( (1+t)/2 ) ],   t = 2ab/(a^2+b^2).
    Proof: H(U) = H(U - i) + H(1[i in U] | U - i), and H(U - i) is the entropy of the mixture.
    Edge form: D_i(f) = sum_T phi(a_T, b_T), phi(a,b) = eta(a^2) + eta(b^2) - eta((a+b)^2)/2 - eta((a-b)^2)/2,
    eta(x) = x log2(1/x); phi is homogeneous of degree 2.
    J is cheap: 1 - h((1+t)/2) <= t^2, so the T-term is <= 4a^2b^2/(a^2+b^2) <= 4 min(a^2,b^2); the sharp constant
    is sup_theta [1 - h((1+sin 2theta)/2)]/sin^2(theta) = 2/ln 2 (theta -> 0). So
        0 <= J_i(f) <= (2/ln 2) Inf_i(f)          [an earlier note of mine said 2 Inf_i; that is wrong for b << a]
    and sum_i J_i <= (2/ln 2) I.

(c) Exact path formula. Influences average over restrictions: I(f) = Inf_i(f) + average of I(f(i->+-1)).
    Hence for ANY decision tree that queries coordinates (adaptive order allowed) down to constants,
        H(f) = E_path sum_k D_{i_k}(f_{k-1}),       I(f) = E_path sum_k Inf_{i_k}(f_{k-1}),
    f_k = f restricted by the first k answers. With a uniformly random order (independent uniform labels, restrict
    in decreasing label order): H(f) = int_0^1 E[ Psi(f_rho_p) ] dp/p, Psi := sum_i D_i, rho_p = random restriction
    keeping each coordinate alive with probability p.

(d) Erasure form of FEI. H^-(f) := sum_i E_i(f) = sum_i H(1[i in U] | U - i) <= H(f) (Han). Conversely, if
    H^-(g) <= C I(g) for all Boolean g then Psi(g) <= (C + 2/ln 2) I(g) for all g, and the random-order path
    formula gives H(f) <= (C + 2/ln 2) I(f). So
        FEI  <=>  sum_i H( 1[i in U] | U - i ) <= C I(f)  for all Boolean f.
    (Also Psi <= H + (2/ln 2) I pointwise.)

(e) Down-ratio form. E_i = sum_T [ a^2 log(1 + b^2/a^2) + b^2 log(1 + a^2/b^2) ]; the first sum is <= Inf_i/ln 2.
    With G(f) := E_U sum_{i in U} log2( 1 + mu(U - i)/mu(U) ):   G <= H^- <= G + I/ln 2. So
        FEI  <=>  E_U sum_{i in U} log2( 1 + mu(U - i)/mu(U) ) <= C E|U|.
    In words: for a typical spectral set U and typical i in U, the lower neighbour U - i is not much heavier than U
    (in the log mean). Only edges with a heavy lower end and a light upper end cost anything:
    cost = light * log(heavy/light). The pair (fhat(U - i), fhat(U)) is (mean, level-one coefficient at i) of the
    Boolean function f * chi_(U - i).

(f) Divergence form, one coordinate. Let nu_i = b^2/Inf_i (spectral law of D_i f) and lam_i = a^2/(1 - Inf_i)
    (spectral law of E_i f), both on subsets not containing i. Then
        sum_T b^2 log(a^2/b^2) = Inf_i [ log((1 - Inf_i)/Inf_i) - KL(nu_i || lam_i) ],
    in the extended-real sense only. CORRECTED (referee FEIB17, 10 Nov): this raw divergence does not give E_i; it
    can be infinite while E_i/Inf_i is finite and large (one missing coefficient of a is enough). The exact form
    uses the mixture m = a^2 + b^2 (a probability law dominating nu_i):
        G_i := sum_T b^2 log2(1 + a^2/b^2) = Inf_i [ log2(1/Inf_i) - KL(nu_i || m) ],   G_i <= E_i <= G_i + Inf_i/ln 2.
    Coordinate i is cheap exactly when KL(nu_i || m) >= log2(1/Inf_i) - C: the spectrum of the derivative sits
    where the whole spectrum is thin.

(g) Good-coordinate form (existence). If FEI holds with constant C then every nonconstant Boolean g has a
    coordinate i with Inf_i > 0 and D_i(g) <= (C + 2/ln 2) Inf_i(g) (pigeonhole on Psi <= (C + 2/ln 2) I).
    Conversely if every nonconstant Boolean g has a coordinate with D_i(g) <= C' Inf_i(g), query that coordinate
    first and recurse: the path formula gives H <= C' I. So
        FEI  <=>  exists C: every nonconstant Boolean g has a coordinate i with
                  H( 1[i in U] | U - i ) <= C Inf_i(g),  i.e.  KL(nu_i || a^2 + b^2) >= log2(1/Inf_i) - C.
    Trivially E_i <= h(Inf_i) <= Inf_i log2(e/Inf_i), so any coordinate with Inf_i >= 2^-C is good.
    Consequence: if f* maximises H/I among n-variable functions (value C_n) then for EVERY i
        D_i(f*) >= C_(n-1) Inf_i(f*)     [H(f*) <= D_i + C_(n-1)(I - Inf_i) and H(f*) = C_n I >= C_(n-1) I],
    hence Inf_i(f*) <= 2^(3/ln 2 - C_(n-1)) for every i. So if C_n were unbounded, the maximisers f*_n would have
    every influence tending to 0 and no cheap coordinate. (Not true of an arbitrary sequence of counterexamples:
    XOR with a fresh dictator adds a coordinate with D_i = 0. Corrected after the referee, FEIB17.)

(h) What is false. The per-coordinate statement E_i <= C Inf_i for every i: take h bent on k variables y, a point
    y*, and f(x_i, y) = h(y) for y != y*, f(x_i, y*) = x_i. Then D_i f = 1[y = y*], b_T^2 = 4^-k for all T,
    a_T^2 ~ 2^-k, E_i ~ k 2^-k = k Inf_i. (The other coordinates pay: I ~ k/2.) The local statement at a fixed T
    is false too (biased majority at T = empty).
    Examples by hand: odd or even functions (majority): E_i = 0 for all i (the parity of |U - i| decides i in U);
    bent: Psi = 2n = 4I; address: Psi = 2a; AND_n: D_i = O(2^-n); tribes: D_i = O(Inf_i).

(i) Open, to test first: is the coordinate of maximal influence always good? Is the best coordinate ratio
    min_i D_i/Inf_i bounded on the census, and where is it largest?

## 8. Round 3 of the Codex workers (FEIB10-13), digest (reports read 10 Nov; proofs of FEIB13 read in full)

FEIB10: containment does not follow from the hypercontractive size axiom alone (explicit non-Boolean measure with
  A/I ~ s/3; it violates f^2 = 1). Boolean spectra obey mu{U >= R, |U - R| <= k} <= 3^k 2^(|R|-1) up(R)^(3/2).
  Any proof must use f^2 = 1 beyond size statements.
FEIB11: log2(1/WC) <= 16 I^2 + 13 I; raw linear WC constant >= 2 log2(8/3) on address functions; n = 5 NPN census
  max log2(1/WC)/I = 1.2491; linear WC proved for monotone, symmetric, read-once bounded gate, degree d.
  npn5.txt = the 616,126 five-variable NPN representatives (kept local).
FEIB12: noise identities proved; median shortcut false; F_S(u)/up(S) >= w + (1-w) u^(m/(1-w)); degree d:
  H, B, Phi(u) <= [2(d-1) + 1/ln 2] I; no fixed nonnegative combination of the five root-zero features is a
  universal local certificate.
FEIB13: P <= A <= P + 2(I - Var); mu(S) <= p(S)^2; T_t <= P + (1-t) I; F_R(u) <= up(R) p(R)^((1-u)/(1+u));
  equal-width tribes: P <= 2I, A <= 4I - 2Var, H <= 6I; W (theta = 1) false on balanced tribes; thinned reference
  laws cost between H and H + I log(1/rho) (so equivalent to FEI); budget with cutoff M = ceil(2I) passed
  numerics, proof open.
Self-composition note: H(f o g) = H(f) + I(f) H(g), I(f o g) = I(f) I(g) for balanced g, so the record 6.5218 is
  H(g)/(I(g) - 1); the AND-of-copies gain 4/I(g) does not beat it when H/I >= 4.

## 9. What the erasure form says and does not say (10 Nov 02:21)

(a) The local constant. R := sup_f min_i D_i(f)/Inf_i(f) (min over coordinates f depends on). Then
  C* <= R <= C* + 2/ln 2, where C* = sup H/I: the left by induction along the tree that always queries a best
  coordinate, the right because sum_i D_i = H^- + J <= H + (2/ln 2) I. So FEI <=> R finite, and R >= 6.5218.
  Numerics so far: 4.8677 for n <= 5, 5.997 on tribes 2x7. Search for large min_i D_i/Inf_i: code/hill_rho.py
  (running on Mac mini 2, n = 6..10).

(b) Pair form of one step. Write u = f(x_i = +1), v = f(x_i = -1), f0 = (u+v)/2, f1 = (u-v)/2. Both take values in
  {-1,0,1}, with complementary supports: f1 lives on the boundary set B_i (measure Inf_i = delta), f0 off it.
  a = f0hat(T), b = f1hat(T). In operator terms b = P uhat, a = (1-P) uhat with P = multiplication by 1_B, a
  projection whose matrix in the character basis has constant diagonal delta. Up to an additive (log2 3 + 1/ln 2) delta,
     E_i = sum_T b_T^2 log2(1 + uhat(T)^2/b_T^2) = delta [ log2((1+delta)/delta) - KL(nu_1 || q) ],
  nu_1 = b^2/delta, q = (uhat^2 + b^2)/(1 + delta), mu_u = uhat^2. (CORRECTED after the referee: the reference law
  must be the mixture q; the raw KL(nu_1 || mu_u) can be infinite. The additive constant improves to
  log2((3 + sqrt 5)/2) + 1/ln 2.) So coordinate i is good exactly when the spectrum of the derivative D_i f is
  nearly singular to the spectrum of the restriction: KL(nu_1 || q) >= log2(1/delta) - C. Sufficient: a set Q of
  characters with sum_{T in Q} b_T^2 >= delta (1 - c/log(1/delta)) and mu_u(Q) <= C delta. For tribes Q = sets that
  meet the rest of i's tribe. If u is a character (low entropy) the coordinate is good with E_i about 2 delta: P is
  generic against the character basis, so b is spread while uhat is not. A bad coordinate needs uhat spread over
  the support of b (the bent case).

(c) FALSE: "the coordinate of largest influence is good". Take b the bent inner product on m variables, x_j =
  Maj_r(z_j) on disjoint blocks, and f = b(x(z)) except on the event x(z) = x*, where f = x_i (a fresh variable).
  Inf_i = 2^-m; a block variable has influence about (1/2) sqrt(2/(pi r)), below 2^-m once r > 4^m/(2 pi). Every
  character T in the support has f0hat(T)^2/f1hat(T)^2 = (2^(m/2) +- 1)^2, so E_i/Inf_i = m + O(1): the unique
  coordinate of largest influence is as bad as one likes. (Exact by the product formula; n = m r + 1 is beyond a
  truth-table check. Exact block sizes from the referee FEIB17: with x* the all-zero point m = 2, 4, 6 need
  r = 7, 53, 695; with x* the all-one point r = 3, 33, 613; E_i/Inf_i = 2.6725, 5.2244, 7.3868.) The block
  coordinates are good, so this is no threat to FEI. Goodness is
  not a matter of the size of the influence.

(d) Edge-law form. On edges e = (T, T+i) of the subset lattice put P(e) = mu(T+i)/I (pick U with weight |U| mu(U),
  remove a uniform element) and Q(e) = (mu(T) + mu(T+i))/n (pick S from mu, toggle a uniform coordinate). Then
     G = I [ log2(n/I) - KL(P || Q) ]   exactly,
  so FEI <=> KL(P || Q) >= log2(n/I) - C: the down-edge law of the spectral sample is nearly singular to its
  up-edge law. In words: removing an element from a spectral sample rarely makes the set much more likely,
     E_U sum_{i in U} log2^+( mu(U - i)/mu(U) ) <= C E|U|.
  For a sparse product measure every removal gains the factor (1-p)/p; that is the model obstruction (a heuristic,
  not a classification), and Boolean spectra must be shown to avoid it. For a symmetric function the ratio is
  (W_(k-1)/W_k)(n-k+1)/k. CORRECTED after the referee: consecutive low levels CAN both carry comparable weight
  (a threshold at n/2 + sqrt(n)/4 has W_0 = 0.142, W_1 = 0.500 at n = 16384); the steep singleton edges then cost
  about W_1 log n, paid for by the influence of order sqrt n.

(e) What a proof must use. FEI fails for complex unimodular functions: f = prod_j (cos t + i sin t x_j) has a
  product spectrum with p = sin^2 t, entropy n h(p) against influence n p. So |f| = 1 is not enough; the proof has
  to use that f is real, that is, that D_i f takes values in {-1,0,1} and is supported on a set of measure Inf_i
  (the KKL input). The bound E_i <= h(Inf_i) alone loses a logarithm: on tribes the greedy tree that queries a
  largest-influence variable pays w/2 per unit of influence, and
     K(f) := integral_0^1 E_rho sum_{i alive} h(Inf_i(f_rho)) dp/p   (an upper bound for H - (2/ln 2) I)
  is about w I on tribes of width w. The true E_i is small there because i is recognisable from U - i.

## 10. Edge entropy, the vertex form and witnesses (10 Nov 02:32)

(a) Edge entropy. H^- = sum over edges {T, T+i} of the subset cube of Phi(mu(T), mu(T+i)),
  Phi(p, q) = (p+q) h(p/(p+q)), symmetric in the two ends; I = sum over edges of mu(top end). Since H^- <= H and
  C* <= sup H^-/I + 2/ln 2 (one coordinate has E_i <= (H^-/I) Inf_i; then the tree induction of section 7),
     sup H^-/I  <=  C*  <=  sup H^-/I + 2.886,
  so FEI is exactly the statement that the edge entropy of a Boolean spectrum is O(I), and sup H^-/I >= 3.63.
  Only steep edges matter: an edge with mu(top) >= 2^-c mu(bottom) costs at most (c + 1 + 1/ln 2) mu(top)
  (corrected after the referee; c + 1 bounds the G summand alone; the sharp constant is log2(1+2^c) + 2^c log2(1+2^-c)).

(b) Vertex form. For T with fhat(T) != 0 put g_T = f chi_T (Boolean, mean fhat(T), level-one coefficients
  fhat(T+i), i not in T, and fhat(T-i), i in T) and rho_i(T) = (fhat(T+i)/fhat(T))^2. Then
     G = E_{T~mu} sum_{i not in T} rho_i(T) log2(1 + 1/rho_i(T)),
  and FEI <=> G <= C I. Bad vertices have many small up-ratios (the sparse product picture: n ratios of size I/n);
  good ones have O(1) up-neighbours of comparable mass. Jensen gives G <= I log2(1 + E_mu[up]/I), up(T) the number
  of up-neighbours in the support; so a spectrum whose support has average up-degree O(I) satisfies FEI.

(c) Witnesses. For any statistic s_i of U - i,  E_i = H(1[i in U] | U - i) <= H(1[i in U] | s_i(U - i)).
  So FEI follows from: statistics s_i with sum_i H(1[i in U] | s_i(U - i)) <= C I. Tribes: s_i = whether U - i
  meets the tribe of i. Odd or even functions: the parity of |U - i| (cost 0). Linear statistics of U are the
  natural family: for a probability law pi on {-1,1}^n, T -> E_{z~pi} chi_T(z); parity of |T cap P| is a point mass,
  "T misses N" is the uniform law on the subcube of N. On the function side sum_T fhat(T)^2 chi_T(z) = E_x f(x)f(xz),
  the autocorrelation, so a witness separates the autocorrelation of D_i f from that of f.

(d) Block witness (PROVED, two-cell bound). For N not containing i let I_N = P[U meets N] = E_x Var_{x_N} f and
  eta = P[i in U, U misses N] = E[(E[D_i f | x outside N])^2]. With s_i = 1[U - i meets N],
     E_i <= I_N h((Inf_i - eta)/I_N) + h(eta)  <=  Inf_i log2(e max(I_N, Inf_i)/Inf_i) + eta log2(e/eta).
  (Two cells: the cell "meets N" has mass I_N and holds Inf_i - eta of the event; p h(q/p) is increasing in p and
  h(x) <= x log2(e/x).)
  So i is good whenever some block N has block influence I_N <= C Inf_i and resampling N destroys the pivotality
  of i: eta <= Inf_i/log(1/Inf_i). Tribes: N = the rest of the tribe. Majority has no such block (it needs
  |N| >= log^2 n, where I_N is about (2 sqrt 2/pi) sqrt(|N|/n), so I_N/Inf_i is of order sqrt|N|; corrected after
  the referee); it is good through parity. Compositions need both kinds. The referee (FEIB17 REFEREE.md (h)) also
  gives the form  E_i <= delta log2(e (I_N + eta)/delta) + eta log2(e/eta),  delta = Inf_i, valid with no side condition.

(e) Caveat on H^- (10 Nov 02:5x). The bracket in (a) is a statement about suprema only. Function by function
  H <= H^- + (2/ln 2) I is FALSE: for an odd (or even) f the parity of |U - i| decides whether i is in U, so
  E_i = 0 for every i and H^- = 0, while H can be of order I (majority). The induction of section 7 uses E_i of
  the restricted functions, which are no longer odd. What does hold for each f: H^- <= H (Han's inequality).

## 11. Threshold functions by the good-coordinate route (10 Nov 03:0x-04:0x; PROVED, a second proof, not a new class)

STATUS OF THE CLASS (corrected 10 Nov 04:0x). FEI for linear threshold functions f = sgn(w.x - theta) is NOT
open for us: it was proved here on 22-23 Sep 2026 by a different argument (rank-weighted entropy,
Erdos-Littlewood-Offord, OWZ Theorem 5: H <= 14.22 I; brain memory
fei_holds_for_linear_threshold_functions_rank_argument_2026_09_23, files in open-problems-repo
proofnet24/P03-fei/continuations/2026-09-22-opus-team/F5-monotone/, second reading in
.../2026-09-24-full-monotone/referee_F5_ltf.md), and worker FEIB14 cites the October 2026 preprint for
H^- <= H < 8.937 I on the class. The first version of this section called the class open after reading only the
outside literature (Chakraborty, Karmalkar, Kundu, Lokam, Saurabh, arXiv 1903.11635, 2019: "it is still not known
whether it holds for the class of Linear Threshold Functions") and without recalling the brain. What this section
adds is therefore not a theorem about a new class. It is (1) a complete second proof by the erasure /
good-coordinate method of section 7, which shows the method closes end to end on a full restriction-closed class;
(2) two tools that do not depend on thresholds: the anti-concentration comparison of Lemma A in (i) and the
conditioning on the refreshed set in (k). The constant obtained this way is worse than 14.22 (it is an explicit
absolute constant, not optimised); numerics say the true value on the class is below 4.
The class is closed under restrictions, so the good-coordinate induction of section 7 runs inside it.

Setting. w_1 >= w_j >= 0 for all j, no ties (w.x != theta on the cube). Write x = (x_1, y), s = w'.y - theta with
w' = (w_2..w_n), and S = {y : |s| < w_1} (a slab). Then
   D_1 f = 1_S,     E_1 f = sgn(s) 1_{S^c},     Inf_1 = P[S] =: delta,
and if delta = 0 then f is constant (a pivotal point for j gives one for 1 because w_j <= w_1).
Level weights on the n-1 remaining variables: A_k = W^k(E_1 f), B_k = W^k(1_S); sum A_k = 1 - delta,
sum B_k = delta, B_0 = delta^2.

(a) Level witness (PROVED; instance of 10(c) with s_1(T) = |T|).
     E_1 <= L_1 := H(1[1 in U] | |U - 1|) = sum_k Phi(A_k, B_k),   Phi(p, q) = (p+q) h(q/(p+q)).

(b) Conditional theorem (PROVED). If every non-constant threshold function has L_1 <= c Inf_1 at its coordinate
  of largest weight, then H(f) <= (c + 2/ln 2) I(f) for every threshold function.
  Proof. D_1 = E_1 + J_1 <= (c + 2/ln 2) Inf_1 (section 7), H(f) = D_1 + (H(f_+) + H(f_-))/2,
  I(f) = Inf_1 + (I(f_+) + I(f_-))/2, and f_+, f_- are threshold functions on n-1 variables; induct on n.

(c) Two-sequence lemma (PROVED). Let A_k, B_k >= 0 (k = 0..m), delta = sum B_k > 0, and suppose
     A_{>=K} B_{<=K} <= M delta^2     for every K >= 0      (tails of A against heads of B).
  Then  sum_k Phi(A_k, B_k) <= (1/ln 2 + 4 + 2 log2(1 + 2M)) delta.
  Proof. Phi(A, B) <= B/ln 2 + g(A, B) with g(a, b) = b log2(1 + a/b), since A log2(1 + B/A) <= B/ln 2.
  g is concave and 1-homogeneous, hence superadditive: sum over a set G of g(A_k, B_k) <= g(A_G, B_G); and g is
  increasing in each argument. Put beta_k = B_{<=k}/delta and G_j = {k : 2^(-j-1) < beta_k <= 2^(-j)}, j >= 0
  (levels with beta_k = 0 have B_k = 0 and contribute nothing). For k_j = min G_j the hypothesis gives
  A_{G_j} <= A_{>=k_j} <= M delta / beta_{k_j} <= 2^(j+1) M delta [corrected 22:2x, referee FEIB18: <= not <, so M = 0 is covered], and B_{G_j} <= 2^(-j) delta. So
     sum_{k in G_j} g <= 2^(-j) delta log2(1 + 2^(2j+1) M) <= 2^(-j) delta (2j + log2(1 + 2M)),
  and sum_j 2^(-j) = 2, sum_j j 2^(-j) = 2.
  For a threshold function the case K = 0 is free: A_{>=0} B_0 <= delta^2. [added 22:2x, referee FEIB18: the K = 0
  hypothesis is needed for general sequences (A_0 = N, B_0 = 1, all else 0 meets every K >= 1 case with M = 0 while
  Phi(N, 1) is unbounded); a product bound proved only for K >= 1 is used with max(M, 1).]

(d) So FEI for threshold functions, with constant 3/ln 2 + 4 + 2 log2(1 + 2M) (about 11.5 at M = 1), follows from

  PRODUCT INEQUALITY (PROVED 10 Nov 04:0x, by (e) and (k)).  There is an absolute M such that for every
  threshold function, at its largest weight, and
  every K >= 1:      W^{>=K}(E_1 f) * W^{<=K}(1_S) <= M Inf_1^2.

  In words: the slab indicator has little weight below any level above which the rest of f still has weight.
  Examples by hand: AND (delta = 2^-(n-1), both factors binomial sums times delta^2: product <= delta^2);
  majority (B_{<=K} about delta^2 sqrt K, A_{>=K} about K^(-1/2)).

(e) Noise form (PROVED reduction). For any g and rho in (0, 1), since Stab_rho(g) = sum rho^|T| ghat(T)^2:
     W^{<=K}(g) <= rho^(-K) Stab_rho(g),     W^{>=K}(g) <= (1 - rho^K)^(-1) (E g^2 - Stab_rho(g)).
  Take rho = 1 - 1/K for K >= 2 (1/4 <= rho^K <= 1/e) and rho = 1/2 for K = 1. With y, z rho-correlated:
  Stab_rho(1_S) = P[y in S, z in S] =: Stay.  E f0^2 - Stab_rho(f0) = P[y not in S, z in S] + 2 Cross for
  f0 = E_1 f, where Cross = P[s(y) >= w_1, s(z) <= -w_1] + P[the reverse]. The first term is at most delta and
  Stay <= delta. So for every K >= 1
     A_{>=K} B_{<=K} <= (4/(1 - 1/e)) (delta + 2 Cross) Stay <= 6.33 (1 + 2 M_cs) delta^2 =: M delta^2
  once

  CROSS-STAY INEQUALITY (PROVED 10 Nov 04:0x, see (k)).   Cross_rho * Stay_rho <= M_cs delta^2   for all rho in [0, 1),

  for the slab S = {|w'.x - theta| < w_1} with all weights of w' at most w_1 (the two noise rates may differ by
  a constant factor). [corrected 22:2x, referee FEIB18: the next sentence is FALSE as stated - X, Y independent, t = 0,
  eps -> 0 gives Cross Stay/delta^2 = (1 - delta)^2/2 -> 1/2, not 1/pi; nothing in the proof uses it.] Gaussian model
  (X, Y rho-correlated normals, slab of half-width eps at height t): the product is delta^2/pi to first order, for every rho and t: Cross is about sqrt(1-rho^2) e^(-t^2/2)/pi, Stay is
  about delta * 2 eps/sqrt(2 pi (1 - rho^2)). The inequality is scale-free, a local-time statement.

(f) How Cross-Stay is proved (the proof is (i)-(k)). The first plan was a Harnack inequality for the noise
  process started inside the slab; it was not needed. What works: write the rho-correlated pair as "refresh a
  random set T of coordinates". Given T and the unrefreshed part, s(y) and s(z) are the same constant plus two
  independent copies of a symmetric sum over T with steps at most w_1. Crossing needs that sum to land beyond
  the slab on the far side; a symmetric sum with steps at most a that reaches beyond a window of half-width a
  also puts comparable mass in the window (Lemmas A and B). So Cross is paid for by delta itself, and Stay by
  delta times the anti-concentration of the refreshed sum; the two losses, 1 + sigma_T/w_1 and w_1/sigma_T,
  cancel. The hypothesis "largest weight = half-width of the slab" enters exactly in Lemma A.

(g) Numerics (code/ltf_level.py, code/ltf_product.py; laptop, exact Walsh transform; n = 14, 18, 20; weight
  families gauss, unif, geometric ratios 1.15-2, a few heavy weights, majority, 1..n, Fibonacci, powers
  0.5-3; thresholds 0 to 3 standard deviations). CHECKED on these only:
     largest weight:  L_1/Inf_1 <= 2.73,  E_1/Inf_1 <= 2.68 (tends to 2 for AND-like thresholds);
     M = max_{K>=1} A_{>=K} B_{<=K}/delta^2 <= 0.74 (attained at K = 1 for thresholds up to 1.5 sd, K = 3-4 at 2.5 sd);
     other coordinates can be bad: max_i E_i/Inf_i reaches 6.76, so the choice of coordinate matters;
     H/I <= 3.9 on all functions tried.
  With c = 2.73 the conditional theorem would give H <= 5.62 I for threshold functions. Not checked: adversarial
  weights (owed: a search over integer weights maximising L_1/Inf_1 and M).
  Large n (code/ltf_cross.py, joint law of (s(y), s(z)) by dynamic programming, n up to 401, twelve values of rho
  from 0 to 1 - 2^-11; results code/ltf_out/cross_families_20261110.txt): R(rho) = Cross Stay/delta^2 <= 0.4609 on
  22 cases (majority, random integer weights, a few heavy weights, geometric, 1..n, squares; thresholds 0-3 sd).
  The Gaussian value is 1/pi = 0.318.
  Lemma checks (exact enumeration, code/lemmaA_check.py 600 weight sets, n <= 13, seven weight kinds, closed
  windows, candidates aligned to the atoms): max of the Lemma A ratio = 1.0000 against the proved 2 (attained
  with five unit weights, a = 1.25, c = 0.25, alpha = 1); max of the Lemma B ratio = 0.4551 against 16/3.
  code/ol_check.py (integer weights, n <= 30, 4000 sets): one-layer ratio <= 0.9375, tail ratio <= 0.4571.
  code/hazard.py (open windows, a up to 5 max w): tail ratio <= 0.6509. So both lemma constants look like they
  could be 1 and about 2/3; nothing depends on that.

(h) OPEN after the proof. (1) The method on a wider restriction-closed class: what replaced "f restricted to x_1"
  here was a pair (1_S, sgn(s) 1_{S^c}) with a one-dimensional statistic s behind both; the level witness worked
  because low-level weight of 1_S and high-level weight of the rest cannot both be large. Candidates, in order:
  functions of two linear forms (intersections of two halfspaces; the statistic is two-dimensional and the slab
  becomes a union of strips), degree-2 thresholds, monotone functions (the known hard case: brain memory
  fei_monotone_case_open_three_failed_routes_exact_data_2026_09_24). (2) The general form of the criterion.
  For any Boolean f and any i, D_i f = (f_+ - f_-)/2 and E_i f = (f_+ + f_-)/2 have disjoint supports, so
  Stay_rho(i) = P[y, z both i-pivotal] and Cross_rho(i) = P[E_i f(y) = -E_i f(z) != 0] are defined, and steps
  (a), (c), (e) use nothing about thresholds (B_0 = (E D_i f)^2 <= Inf_i^2 always). So:
     if Cross_rho(i) Stay_rho(i) <= M Inf_i^2 for all rho, then D_i f <= C(M) Inf_i.
  With noise on ALL coordinates this cannot be the general statement: for tribes of width w, at rho = 1 - 1/w,
  Cross is of order 1 and Stay of order delta (computed by hand 10 Nov, NOT run), so the product is delta, not
  delta^2, at every coordinate; the level witness loses a factor log n there. LOCAL FORM (derived 10 Nov 04:0x,
  NOT checked numerically): fix N in [n] - i, count levels inside N only (statistic |T n N| in 10(c)) and apply
  noise to the coordinates of N only. Then (a), (c), (e) go through with one change: K = 0 is no longer free, it
  asks B^N_0 = E[(P[i pivotal | coordinates off N])^2] <= M Inf_i^2. So a coordinate i is good as soon as there
  is N with
     (L0)  E[(P[i pivotal | x off N])^2] <= M Inf_i^2,        (L1)  Cross^N_rho(i) Stay^N_rho(i) <= M Inf_i^2 all rho.
  N empty kills Cross and fails (L0); N = everything gives (L0) for free and is the threshold case. Tribes: N =
  the tribe of i gives Cross^N = 0 and (L0) with M = 1/P[no other tribe true]. Compositions f = F(g(x_i, x_N),
  x_rest): Cross^N Stay^N/Inf_i^2 for f equals Cross Stay/Inf_i^2 for g (the chance that F depends on g cancels),
  and (L0) asks that g have influence of order 1 in F. So (L0)+(L1) holds for thresholds, tribes and one level of
  composition; whether some pair (i, N) always exists is a strengthening of the good-coordinate conjecture, to
  be TESTED on the extremal functions of sections 2 and 9 before anything is built on it (exhaustive over N for
  n <= 10).
  TESTED 10 Nov 04:1x (code/local_cs.py): a pair (i, N) does NOT always exist with a bounded constant. On
  AND_w o MAJ_3 the best single-set value grows like log w (section 12(a)); the tribe computation above (order 1
  times delta, a log n loss for the level witness) is confirmed by the same script. What replaces it is the
  filtration witness of section 12.
  (3) Sharpening the constant on thresholds is not a priority (sup H/I looks like 4).

(i) LEMMA A (PROVED; anti-concentration comparison at the scale of the largest step). Let R = sum_j w_j eps_j with
  independent uniform signs and weights 0 < w_j <= a. Then for all 0 <= c <= alpha,
        P[alpha <= R <= alpha + a]  <=  2 P[c - a <= R <= c + a].
  In words: an interval of length a further out than c carries at most twice the mass of the window of
  half-width a centred at c. Closed intervals are needed (R = a eps, c = 0 fails for open windows).
  Proof, by induction on the number n of steps; write W_x = [x - a, x + a] and J = [alpha, alpha + a].
  n = 0: R = 0 lies in J only if alpha = 0, then c = 0 and 0 is in W_0.
  Step: R = R' + w eps, 0 < w <= a. Then P[R in J] = (P[R' in J - w] + P[R' in J + w])/2 and
  P[R in W_c] = (P[R' in W_{c-w}] + P[R' in W_{c+w}])/2. It suffices to show
     (+)  P[R' in J + w] <= 2 P[R' in W_{c+w}]      and      (-)  P[R' in J - w] <= 2 P[R' in W_{c-w}].
  (+) is the induction hypothesis with centre c + w and left end alpha + w >= c + w.
  (-) If c >= w it is the induction hypothesis with centre c - w >= 0 and left end alpha - w >= c - w.
      If c < w put e = w - c in (0, a] and beta = alpha - w >= -e. By symmetry of R',
      P[R' in W_{c-w}] = P[R' in W_e]. Three cases for the interval [beta, beta + a]:
      beta >= e: induction hypothesis with centre e and left end beta.
      e - a <= beta < e: [beta, beta + a] is inside W_e.
      -e <= beta < e - a: split [beta, beta + a] = [beta, e - a) u [e - a, beta + a]. The second piece is inside
        W_e (beta + a < e + a). The mirror image of the first piece is (a - e, -beta], which is inside W_e
        because a - e >= e - a and -beta <= e; R' is symmetric, so the first piece has mass at most P[R' in W_e].
        Together at most 2 P[R' in W_e].
  Remark: the proof uses only that each step is symmetric and bounded by a (condition on |step|), so it holds
  for any independent symmetric summands with |X_j| <= a.

(j) LEMMA B (PROVED; the tail beyond a window is paid for by the window). With R as in (i), sigma^2 = sum w_j^2,
  and t >= 0:
        P[R > t + a]  <=  (16/3) (1 + sigma/a) P[|R - t| <= a].
  Proof. Let L = a + 2 sigma. (1) Let tau be the first k with S_k > t + a (partial sums in a fixed order); then
  S_tau <= t + 2a, and R > t + a + L forces R - S_tau > 2 sigma, which given the past up to tau has probability at
  most 1/8 (Chebyshev and symmetry). By Levy's inequality P[tau < infinity] <= 2 P[R > t + a]. So
  P[R > t + a + L] <= (1/4) P[R > t + a], hence P[R > t + a] <= (4/3) P[t + a < R <= t + a + L].
  (2) (t + a, t + a + L] is covered by ceil(L/a) <= 2 + 2 sigma/a closed intervals of length a with left ends
  >= t; each has mass <= 2 P[|R - t| <= a] by Lemma A with c = t. Multiply out.

(k) CROSS-STAY (PROVED) and the theorem. Setting of this section; sigma^2 = sum_{j>=2} w_j^2. Realise the
  rho-correlated pair (y, z) as: T = a random set containing each j >= 2 independently with probability 1 - rho,
  independent of y; z_j = y_j off T, z_j fresh on T. Given T and the coordinates of y off T,
        s(y) = A + U,   s(z) = A + V,   A = sum_{j not in T} w_j y_j - theta,
  with U, V independent copies of the symmetric sum over T, steps at most w_1, sigma_T^2 = sum_{j in T} w_j^2.
  No ties means s never equals +-w_1, so U has no atom at +-w_1 +- A and closed and open windows agree.
  Cross. Given (T, A = al): Cross = 2 P[U >= w_1 - al] P[U >= w_1 + al] <= 2 P[U > w_1 + |al|]
        <= (32/3) (1 + sigma_T/w_1) P[|U - |al|| <= w_1]                    (Lemma B, a = w_1, t = |al|)
        = (32/3) (1 + sigma_T/w_1) P[y in S | T, A = al]                    (symmetry of U).
  Average over A, then over T; T is independent of y, so P[y in S | T] = delta and
        Cross <= (32/3) delta E[1 + sigma_T/w_1] <= (32/3) delta (1 + x),     x := sqrt((1 - rho)) sigma/w_1.
  Stay. Given (T, y): P[z in S] = P[|A + V| < w_1] <= Q_T := sup over intervals of length 2 w_1 of the mass of V.
  Q_T depends on T only, so Stay <= delta E[min(1, Q_T)]. Kolmogorov-Rogozin (lambda_j = w_j, each step has
  concentration 1/2 at that scale): Q_T <= K_0 w_1/sigma_T with K_0 absolute. Chernoff for sigma_T^2 (a sum of
  independent terms in [0, w_1^2] with mean x^2 w_1^2): P[sigma_T^2 <= x^2 w_1^2/2] <= exp(-x^2/8). So
        Stay <= delta (exp(-x^2/8) + min(1, sqrt(2) K_0/x)).
  Product. Cross Stay <= (32/3) sup_{x >= 0} (1 + x)(exp(-x^2/8) + min(1, sqrt(2) K_0/x)) delta^2 =: M_cs delta^2,
  finite and absolute. (Numerically the truth is M_cs <= 0.46, see (g).)

  THEOREM (second proof). H(f) <= C I(f) for every linear threshold function, C = 3/ln 2 + 4 + 2 log2(1 + 2M),
  M = 6.33 (1 + 2 M_cs). Chain: (k) => (e) => product inequality => (c) with (a) gives L_1 <= c Inf_1 at the
  largest weight => (b). Every step is written above; the only quoted results are Levy's inequality, the
  Kolmogorov-Rogozin inequality, a Chernoff bound, and section 7 (D_i = E_i + J_i, J_i <= (2/ln 2) Inf_i).
  Audit state: steps (a)-(e), (i)-(k) re-derived once after writing (10 Nov 04:0x); Lemmas A, B checked by exact
  enumeration; NOT yet read by a second reader (owed: Codex referee FEIB18), NOT compared line by line with the
  September rank proof.

## 12. The filtration witness (10 Nov 04:1x-04:4x; (b)-(f) PROVED, (g) proved and checked, universality OPEN)

Notation of section 7: for a coordinate i, g = E_i f, h = D_i f (disjoint supports, values in {-1, 0, 1},
E h^2 = Inf_i =: delta, E g^2 = 1 - delta), p(T) = fhat(T)^2 and q(T) = fhat(T + i)^2 for T not containing i,
E_i = sum_T Phi(p(T), q(T)), Phi(p, q) = eta(p) + eta(q) - eta(p + q) = (p + q) h(q/(p + q)).
Phi is concave, homogeneous of degree 1, increasing in each argument, hence superadditive.

(a) The single-set witness is not universal (code/local_cs.py, exhaustive over i and N).
  L^N_i = H(1[i in U] | |(U - i) n N|), minimised over (i, N), per unit of Inf_i, against min_i E_i/Inf_i:
     AND_w o MAJ_3, w = 2..6:   1.8048  2.5431  3.1378  3.6808  4.2013     against   1.8048  2.1827  2.1455  2.0438  1.9570
     TRIBES_2x8  4.1111 against 3.6068;    OR_AND_OR_16  4.6889 against 3.3170.
  The gap on AND_w o MAJ_3 grows by about 0.55 per unit of w. Reason: the count inside the block of i cannot see
  whether the other blocks are empty, and the count over everything mixes the block with the rest.
  A two-count labelling (|T n mates|, [T n rest is empty]) is exact (= E_i) on AND_w o MAJ_r and on tribes and
  within 0.016 on OR-AND-OR at n = 8, 12, 16 (code/local_cs2.py). A labelling per family is not a theorem.

(b) Definition. Fix i and an ordering pi = (j_1, ..., j_m) of the other m = n - 1 coordinates. Label a set T
  (not containing i) by lab(T) = max{k : j_k in T}, and 0 for the empty set. Put
        A_k = sum_{lab(T) = k} p(T),      B_k = sum_{lab(T) = k} q(T),      L^pi_i := sum_{k=0}^m Phi(A_k, B_k).
  Then L^pi_i = H(1[i in U] | lab(U - i)) >= H(1[i in U] | U - i) = E_i, because lab(U - i) is a function of
  U - i. Martingale form: with F_k generated by x_{j_1}, ..., x_{j_k},
        A_k = E (E[g | F_k] - E[g | F_{k-1}])^2,   B_k = E (E[h | F_k] - E[h | F_{k-1}])^2,   A_0 = (E g)^2,  B_0 = (E h)^2.
  So the witness reveals the other coordinates one at a time and compares, step by step, how much of g and how
  much of h each step explains. The level witness of 11(a) and the single-set witness of (a) are coarser
  statistics of the same kind; all three are limits of the weighted count sum_{j in T} lambda_j (equal weights;
  0/1 weights; weights growing fast along pi). [corrected 22:2x, referee FEIB19: not literally - superincreasing weights
  make the weighted sum injective, so its conditional entropy is E_i for every such weight vector; L^pi_i is the
  further coarse-graining to the last revealed position. The definition and the martingale identity are unaffected.]

(c) Trivial bound. By superadditivity sum_k Phi(A_k, B_k) <= Phi(sum A_k, sum B_k) = h(delta). So for every f, i
  and pi:  E_i <= L^pi_i <= h(Inf_i) <= Inf_i log2(e/Inf_i). Every coordinate is good up to log(1/Inf_i); summed
  along a decision tree this is the influence-log bound H <= C sum_i h(Inf_i) (Keller, Mossel and Schlank).
  The whole question is the removal of that logarithm at one coordinate.

(d) Computation. With the zeta transforms a(R) = sum_{T in R} p(T), b(R) = sum_{T in R} q(T) over subsets R of
  the other coordinates, an ordering is a maximal chain empty = R_0 < R_1 < ... < R_m and A_k = a(R_k) - a(R_{k-1}),
  B_k = b(R_k) - b(R_{k-1}). The minimum over all m! orderings is a shortest path:
        best(empty) = Phi(a(empty), b(empty)),   best(R) = min_{j in R} best(R - j) + Phi(a(R) - a(R - j), b(R) - b(R - j)).
  Cost m 2^m per coordinate (code/filt_cs.py; batched in code/hill_filt.py, the two agree to 15 digits).

(e) Sufficient condition. The two-sequence lemma 11(c) applies to any index set, so
        A_{>=K} B_{<=K} <= M delta^2 for all K >= 1   implies   L^pi_i <= (1/ln 2 + 4 + 2 log2(1 + 2 max(M, 1))) delta
  (K = 0 is free: B_0 = (E h)^2 <= delta^2). Here A_{>=K} = E Var(g | F_{K-1}) and B_{<=K} = E (E[h | F_K])^2.
  Pair form, exact (no noise constant as in 11(e)): let y, y' agree on the first K revealed coordinates and be
  independent on the rest. Then B_{<=K} = E h(y) h(y') =: Stay_K <= P[i pivotal at both], and with y, y' sharing
  the first K - 1 coordinates A_{>=K} = P[i pivotal at y, not at y'] + 2 Cross_{K-1},
  Cross = P[g(y) = -g(y') != 0]. Since the first term is at most delta and Stay <= delta, the condition is
        Cross_{K-1} Stay_K <= M' delta^2       for every K.
  In words: i is good along pi if, at every stage, either the value of f is already settled up to probability
  delta (given what has been revealed), or the revealed coordinates still say little about whether i is pivotal.
  Thresholds: decreasing weight order from the largest weight gives a product of order (w_1/sigma)^2, by hand.
  Tribes: the other tribes first, the mates of i last: after the other tribes f is settled unless none fired,
  and then only the tribe of i matters.

(f) Why a random ordering is not enough (hand estimate, NOT run; [22:2x, referee FEIB19: GAP - 'Stay is about
  delta^(2-t)' drops the other tribes; no uniform proof; nothing depends on it]). For tribes of width w and a uniformly random
  pi, after a fraction t of the coordinates Stay is about delta^(2 - t) while Cross stays of order 1, so
  L^pi_i/delta is of order log(1/delta) = w. The ordering has to depend on i: mates last.

(g) Composition formula (PROVED, checked to 3e-16 on 400 random pairs, code/comp_check.py). Let
  f(x_B, z) = F(g(x_B), z) = F_0(z) + g(x_B) F_1(z) with g Boolean on the block B and i in B. Then
        Inf_i(f) = Inf_i(g) ||F_1||^2,
        E_i(f) = ||F_1||^2 [ E_i(g) - Phi(ghat(0)^2, ghat(i)^2) ]
                 + sum_{T2} Phi( (F_0hat + ghat(0) F_1hat)(T2)^2 ,  ghat(i)^2 F_1hat(T2)^2 ).
  Proof: fhat(T1 u T2) = [T1 empty] F_0hat(T2) + ghat(T1) F_1hat(T2); for T1 nonempty the pair (T1, T1 + i)
  scales by F_1hat(T2)^2 and Phi is homogeneous; T1 empty is the last sum. The last sum is the erasure term of F
  at the slot of g, for an input of mean ghat(0), with the slot's variance 1 - ghat(0)^2 replaced by the smaller
  ghat(i)^2; with t = ghat(i)^2/(1 - ghat(0)^2) <= 1, the last sum DIVIDED BY t is at least the biased erasure term
  (Phi(p, t q)/t decreases in t), while the last sum itself is at most it [corrected 22:2x, referee FEIB19:
  F(u, z) = u, g = AND_2 gives last sum Phi(1/4, 1/4) = 1/2 < h(1/4)]; the excess is where
  a composition can lose. The same splitting holds for the filtration witness when pi reveals z before B.
  (O'Donnell and Tan prove a composition theorem for the conjecture itself; this is the one-coordinate version.)

(h) Numbers (code/filt_cs.py; F = min over i and pi of L^pi_i/Inf_i; minE = min_i E_i/Inf_i <= F; M = the
  constant of (e) along the best ordering).
     F = minE:  AND_n (2.2922, 2.1048, 2.0341, 2.0105 at n = 6, 8, 10, 12); every tribes function to n = 12
        (TRIBES_2x2..2x6: 1.7817, 2.3160, 3.0428, 3.3892, 3.5417; 3x2..3x4: 2.6220, 2.5474, 2.4282; 4x2, 4x3: 2.6246,
        2.6135); bent (2.0000); OR-AND-OR at n = 8, 12 (3.3047, 3.4145).
     MAJ_n, n = 3..11: 1.0000, 1.5204, 1.7848, 1.9578, 2.0844 (minE = 0; M 0.50..0.75). MAJ_3 o MAJ_3: 1.9024.
     AND_w o MAJ_3, w = 2, 3, 4: 2.8048, 3.1827, 3.1455, which is minE + 1.0000 each time (compare (a)).
     AND_2 o MAJ_5: 3.1591 (minE 1.6387). XOR_w o MAJ_3: 1.0000. XOR_2 o MAJ_5: 1.5204.
     Bent with one point flipped, 2k = 4..12 variables: 0.8908, 1.6993, 1.9285, 1.9831, 1.9959 at the best
        coordinate; the worst coordinate grows (2.95, 5.35, 7.43, 9.44, 11.44), so the choice of i matters.
     Address functions: 0 (a data coordinate has E_i = 0); M is 1, 3, 7 there and plays no role.
     PM(K33) host (9 variables):  minE 2.6293,  F 2.9132,  M 1.115.
     PM(K33) lift with nine coins (18 variables, the record 6.5218 as H/(I - 1)): minE 2.6305, F 2.8455 at a grid
        coordinate; at a coin coordinate the witness is 8.52.
     Random functions, n = 8 (40, half of them sparse): minE <= 1.1759, F <= 1.7862, M <= 0.544.
     The ten bests of the first hill search (objective min_i D_i/Inf_i, n = 6..10): F <= 3.3892.
     Sup of F over everything above: 3.5417 (tribes 2 x 6). M <= 0.82 on the families, 1.115 on the PM host.
  Search (code/hill_filt.py, maximise F by single and double flips with restarts; Mac mini 2, n = 8, 9, 10,
  ten processes, four hours from 04:23): after ten minutes the best is 3.4544 (n = 10, from a tribes start,
  minE 3.3602). A 40 s run at n = 6 gave 3.0897.

(i) FILTRATION WITNESS CONJECTURE (FWC; OPEN).  There is an absolute c such that every non-constant Boolean f
  has a coordinate i and an ordering pi of the others with L^pi_i <= c Inf_i.
  FWC implies FEI with constant c + 2/ln 2 (section 7: D_i = E_i + J_i <= L^pi_i + (2/ln 2) Inf_i, and the class
  of all Boolean functions is closed under restriction). FEI is equivalent to the same statement with E_i in
  place of L^pi_i, so FWC is a strengthening; nothing above says it is true beyond the cases run. What would
  refute it: a family in which, for every coordinate and every order of revealing the others, D_i f becomes
  predictable while E_i f is still undetermined with probability far above Inf_i. Tribes-like and PM-like
  functions are not such a family. What is proved: thresholds (section 11, with pi = decreasing weights).
  [corrected 22:2x, referee FEIB19: section 11 proves the degree-count (level) witness, not this maximum-position
  one; the filtration statement for thresholds needs the separate deterministic-tail argument in FEIB19 PROOFS.md.]

(j) OPEN. (1) A rule for (i, pi) on a general function: "farthest first, nearest last" needs a notion of
  distance from i; candidates: order by the correlation of pivotality (j early when revealing x_j changes
  P[i pivotal] little), or by the greedy path of (d). (2) FWC on restriction-closed classes: read-once formulas
  (by (g)), monotone functions, functions of two linear forms. (3) Adaptive filtrations: let the next revealed
  coordinate depend on the values seen (a decision tree on the other coordinates); the labels are then not
  functions of U - i alone, so the inequality E_i <= L needs a different proof; not done. (4) A search for a
  counterexample family beyond n = 10 (structured: overlapping-term DNFs, projective-plane functions, linear
  changes of variables of the extremal functions).

(k) Larger structured functions (10 Nov 05:00; code/filt_big.py, tables code/big_out/; exact minimum over
  orderings, coordinate 0 of functions with a transitive symmetry group, n up to 25; minM = the minimum over
  orderings of max_K A_{>=K} B_{<=K} / Inf_i^2, a bottleneck path).
     perfect matching on K_{n,n}, n = 3, 4, 5:  F 2.9132, 3.7775, 4.2019;  minE 2.6293, 3.1810, 3.2970;  minM 1.105, 1.342, 1.266
     plane DNFs PG(2,q), q = 2, 3, 4:           F 2.3213, 3.1602, 3.9884;  minE 0, 0.7276, 1.8219;       minM 0.903, 1.201, 1.553
     perfect matching on K6 4.1253; difference-set DNF {0,1,3,7} mod 21 4.1125; four-cycle in K45 4.0415;
     triangle, K4, bipartite on K6, K7: 3.83 to 4.04; tribes at n = 15..21 again F = minE (at most 3.5916).
  Sup of F over everything run: 4.2019 (perfect matching on K55). Sup of minM: 1.553 (PG(2,4)).
  CAVEAT, and it limits what these numbers show. The trivial bound of (c) is h(Inf_i)/Inf_i, and a balanced
  transitive function on n <= 25 variables has Inf_i >= 0.04. For the functions with the largest F the witness
  is within 10 to 20 percent of the trivial bound: perfect matching K55 4.20 against 4.69 (Inf 0.100), K6
  triangle 4.03 against 4.53, K6 bipartite 4.00 against 4.63, C4 in K45 4.04 against 4.80. Where Inf_i is small
  the witness is far below it (max degree <= 2 on K7: 2.48 against 13.96 at Inf 0.00017; tribes 2 x 10: 3.57
  against 6.15), but those are tribes-like or rare-event functions. So the tables do not test FWC in the regime
  that matters (balanced, overlapping structure, Inf_i -> 0); they show no counterexample at n <= 25 and nothing
  more. The growth of F along K33, K44, K55 and along the planes is the trivial bound growing as Inf_i falls.
  (script for the comparison: scratch triv.py; the column is F / (h(Inf)/Inf).)
  The minimum-certificate rule of (j)(1) (code/rule_cs.py: outside the certificate first, mates last): equal to
  the optimum on AND, majority, tribes 2 x k, bent; 1.94 times the optimum on XOR o MAJ_3. Not a rule to prove from.

(l) The condition of (e) in terms of the spectral sample and of resampling (10 Nov 05:17; PROVED identities).
  Write U for the spectral sample, delta = Inf_i = P[i in U]. For a set R of other coordinates let x^R be x with
  the coordinates of R resampled, and
        W(R) := P[i in U, U n R empty]      = E h(x) h(x^R)              (pivotality of i survives resampling R),
        V(R) := P[i not in U, U n R nonempty] = E Var(g | x off R) = E g^2 - E g(x) g(x^R)   (block influence of R on g).
  W decreases in R from delta to fhat(i)^2; V increases from 0 to Var g. For the ordering pi and K >= 1, with
  R = the coordinates revealed after stage K and R+ = R plus the coordinate revealed at stage K:
        B_{<=K} = W(R),      A_{>=K} = V(R+).
  So the sufficient condition of (e) reads:   W(R) V(R+) <= M delta^2   along the chain of final segments of pi.
  (1) Sub-chain lemma. W and V are monotone, so it is enough to have nested sets R_1 < R_2 < ... < R_J = all
      with V(R_1) <= M delta and W(R_j) V(R_{j+1}) <= M delta^2; any ordering that refines the chain (R_1 revealed
      last) then satisfies (e) with the same M. A halving chain is the canonical form:
      W(R_j) <= 2^-j delta and V(R_j) <= M 2^(j-1) delta, j up to log2(1/delta).
  (2) In words: i is good if resampling a set R that changes the value of f with probability p (in units of
      delta) destroys the pivotality of i except with probability M/p. With miss(R) = W(R)/delta =
      P[U n R empty | i in U] and tau(R) = V(R)/delta the condition is miss(R) tau(R+) <= M.
  (3) Monotone f: put L = {f = 0 for both values of x_i}, H = {f = 1 for both}, D = {i pivotal}; L is a
      down-set, H an up-set, D lies between, P[D] = delta. Then W(R) = P[x in D, x^R in D] and
      V(R) = P[x in D, x^R not in D] + 4 P[x in L, x^R in H] (g is +1 on H, -1 on L, 0 on D; the second term is
      twice the probability that x and x^R lie on opposite sides). The first part is at most delta, so the condition is
            P[stay in D] * P[jump over D] <= M' P[D]^2
      for the resampling chain of R. One-dimensional picture (thresholds): D is a band of width d in a density
      rho, the chain moves a distance s: stay = delta d/s, jump = s rho, product = delta^2. Tribes with R = the
      other tribes moves along D and fails; R = mates moves across D.
  (4) Sanity check that Booleanness is used. For a product measure on sets (inclusion probabilities p_j, all
      small; the squared spectrum of prod (sqrt(1-p_j) + sqrt(p_j) x_j), not Boolean, the standard real-valued
      violation of the conjecture) and any i and R: W(R) V(R) is about p_i e^-s (1 - e^-s) with s = sum of p_j
      over R, which is of order p_i, not p_i^2, at s = 1. The condition fails for every ordering, as it must.
  (5) Union bound: V(R) <= sum_{j in R} Inf_j. For a coordinate i of maximal influence the condition follows
      from miss(first r coordinates of the chain) <= M/(r + 1) for r <= Var(g)/delta. This is sufficient and far
      from necessary: for majority miss is about r^(-1/2) and V(R) is about sqrt(r) delta, not r delta.
  (6) The same two quantities give a criterion for one function without restrictions (chain rule in a fixed
      order sigma, the two-sequence lemma at each step): if for each k there is a chain of subsets R of
      {sigma_1..sigma_(k-1)} with P[sigma_k in U, U n R empty] P[sigma_k not in U, U n R+ nonempty] <=
      M Inf_{sigma_k}^2, then H(f) <= c(M) I(f). Here U n R looks only at earlier coordinates, so a coordinate
      early in sigma has few sets to use; the last coordinate has all of them.

(m) Percolation as a test of (l) (heuristic from the arm estimates of Garban, Pete and Schramm; NOT a proof here,
  and the literature on the conjecture for percolation is not yet checked). Crossing of an L x L piece of the
  triangular lattice, i in the bulk, R = B(i, r) minus i. W(R) = P[i pivotal for x and for x^R] is of order
  alpha_4(r, L) alpha_4(r)^2 (four arms from radius r to L once, from 1 to r in two independent
  configurations), and V(R) <= P[U meets B(i, r)], of order alpha_4(r, L). With delta of order alpha_4(L) and
  quasi-multiplicativity, W(B(r)) V(B(2r)) is of order delta^2 at every scale: the chain of balls is a halving
  chain. So the filtration witness, with the order "farthest site first", should give E_i <= C Inf_i at every
  bulk site: a balanced function with overlapping, long-range structure and Inf_i -> 0 on which the condition
  holds for a reason (quasi-multiplicativity) unlike both the tribes reason and the threshold reason.
  The entropy itself: a quad-tree code (for each non-empty square, which of its four quarters are non-empty)
  gives H(U) <= log2(15) * sum over dyadic r of E #{r-squares met by U} <= C sum_r (L/r)^2 alpha_4(r, L)
  <= C' L^2 alpha_4(L), of the order of I, because alpha_4(r) >= r^(-2+eta). So the conjecture should hold for
  percolation crossings; whether this is written somewhere is to be checked before it is called anything.
  The tree code is not universal: H(U) <= sum over nodes v of a binary tree on the coordinates of
  P[U meets S_v] H(children pattern | U meets S_v) for every tree, but on the plane DNF PG(2,q) in the sparse
  regime every tree pays about log q per element (lines are spread across any hierarchy), while the ordering
  "the lines through i, one after another" keeps the filtration witness at (2 + o(1)) Inf_i there (A_k/B_k =
  1 + q 2^(t-1-r) for the point of rank r on the t-th line; only the last log q lines pay, log q each).
  (The PG(2,q) estimate is a hand computation, not run; the exact values at q = 2, 3, 4 are in (k).)
  Use of (l) for computation: W and V are expectations of products over a pair (x, x^R), so they can be
  estimated by sampling for functions of any size, and by superadditivity of Phi a coarse chain
  R_1 < ... < R_J gives the upper bound  E_i <= sum_j Phi(V(R_{j+1}) - V(R_j), W(R_j) - W(R_{j+1}))  (plus the
  two end cells). This is the test at small Inf_i that exact enumeration cannot reach (code/mc_chain.py).

(n) What a counterexample to FWC must look like, after (l), (m): a Boolean function in which, for every
  coordinate i, the companions of i in the spectral sample cannot be captured by sets of small block influence:
  delocalised samples (given i in U, the rest of U spread over a pool much larger than U) of moderate size.
  Level inequalities force |U - i| >= c log(1/delta) given i in U; product-like spreading with |U| below
  I log(1/delta) would violate the condition, and is what Booleanness has to exclude. Thresholds are delocalised
  but with |U| of order n; tribes, percolation and sparse designs are localised.

### 12(o) Sampling at small influence, and why the nested witness fails on overlapping DNFs (10 Nov 05:47)

Status of this subsection: the tables are measurements (code/mc_chain.py, 1,048,576 samples unless marked); the
analysis of the DNF case is a heuristic computation, not a proof. The test that would confirm or kill it is named
at the end.

Tables. L/Inf is the coarse chain bound of 12(l) (an upper bound for E_i/Inf_i), "trivial" is h(Inf)/Inf, M is the
largest W(R_j) V(R_{j+1}) / Inf^2 along the chain.

    family                         Inf       L/Inf    trivial   ratio    M
    run of 6 ones,  n = 89         0.0418    3.289    5.994     0.549    1.18
    run of 8 ones,  n = 355        0.0138    3.021    7.610     0.397    1.22
    run of 10 ones, n = 1420       0.0044    2.837    9.276     0.306    1.39
    run of 12 ones, n = 5678       0.0013    2.803   11.020     0.254    1.16
    run of 14 ones, n = 22713      0.0004    2.471   12.715     0.194    0.56   (524,288 samples)
    majority, n = 1001             0.0252    3.501    6.732     0.520    0.98
    hex crossing 12 x 12           0.0591    4.10     5.48      0.749    1.16   (262,144 samples)
    hex crossing 16 x 16           0.0425    4.270    5.967     0.716    1.15
    hex crossing 24 x 24           0.0264    4.440    6.669     0.666    1.17
    hex crossing 32 x 32           0.0190    4.530    7.189     0.630    1.17   (added 10 Nov 06:30)
    hex crossing 48 x 48           0.0115    4.688    7.918     0.592    1.36   (524,288 samples; added 06:30)
    hex crossing 64 x 64           0.0080    4.665    8.405     0.555    1.24   (524,288 samples; added 10 Nov 08:40)
    hex crossing 96 x 96           0.0048    4.831    9.134     0.529    1.46   (262,144 samples; added 10 Nov 08:40)
    majority, n = 10001            0.0082    3.688    8.359     0.441    1.23   (524,288 samples; added 06:30)
    tribes, 186 ANDs of width 8    0.0038    1.999    9.467     0.211    1.27   (added 06:30)
    tribes, 728 ANDs of width 10   0.0009    2.023   11.495     0.176    0.55   (added 06:30)
    at least 10 of 640 ANDs w 6    0.0039    2.358    9.425     0.250    1.29   (added 06:30)
    at least 10 of 2560 ANDs w 8   0.0010    2.031   11.375     0.179    0.85   (added 06:30)
    at least 10 of 10240 ANDs w 10 0.0002    1.938   13.500     0.144    0.42   (524,288 samples; added 06:30)
    random DNF w 9,  n 250,  m 355     0.0417    5.290    5.995     0.882    3.19
    random DNF w 10, n 500,  m 710     0.0245    5.858    6.779     0.864    4.04
    random DNF w 10, n 300,  m 710     0.0340    5.681    6.298     0.902    4.03
    random DNF w 11, n 600,  m 1420    0.0195    6.362    7.106     0.895    5.79
    random DNF w 12, n 2000, m 2839    0.0076    6.848    8.471     0.808    8.30
    random DNF w 12, n 1000, m 2839    0.0124    6.986    7.769     0.899    9.28
    random DNF w 13, n 4000, m 5678    0.0041    7.406    9.387     0.789   11.07   (524,288 samples)

Reading. (1) Localised families: flat or falling while the trivial bound doubles. (2) Hex: M stays at 1.15 to 1.17
but L/Inf creeps up 0.17 per step; larger boards (32 to 96) are still running, and the ball chain is not optimised.
(Added 06:30: boards 32 and 48 give 4.53 and 4.69, about 0.27 per doubling of the side from 16 to 48 against 1.2 per
doubling for the trivial bound; boards 64 and 96 still running. [Added 10 Nov 08:40: boards 64 and 96 finished,
4.665 and 4.831. From side 16 to side 96 the coarse chain bound rises 0.56 over 2.58 doublings, 0.22 per doubling,
against 1.22 per doubling for the trivial bound; the step 48 to 64 is flat within sampling error (the Inf estimates
carry a relative error of 1.5 to 3 percent, files code/mc_out/hex_64_s1.json, hex_96_s1.json). Inf falls as
side^-1.22 (the four-arm exponent 5/4), so the creep is about 0.18 log2(1/Inf): slow, not visibly bounded, and a
property of this coarse ball chain as long as no finer chain is tried.] Tribes and thresholds of disjoint ANDs sit at 2, as
the private-term lemma 12(q) says they must; majority creeps 3.50 to 3.69 from n = 1001 to 10001 with this coarse
chain, although 11 proves the nested witness is bounded on thresholds (measured L_1/Inf_1 <= 2.73 there), so a
creep in this column is a property of the coarse chain and not evidence about E_i.)
(3) Random monotone DNFs in which every variable lies in many terms (i = the variable of largest degree D; chain =
breadth-first order in the term hypergraph): L/Inf rises with the width and M rises roughly like D/3. Three other
chains on the w = 9 instance (65,536 samples each; mates of i term by term 5.44, the mates last 5.11, a uniformly
random order 5.48, against 5.25 for breadth-first at that sample size) do no better.

Why (heuristic). Write a monotone DNF, in 0/1 values with x_i in {0,1}, as

    f = 1 - N (1 - B x_i),     N = [no term avoiding i is satisfied],   B = [some term through i has all its mates on].

Then, up to the common factor from the 0/1 convention, h = N B / 2 and g = (1 - N) + h, so for T nonempty

    g^(T) = h^(T) - N^(T),     E_i = sum_T Phi( (h^(T) - N^(T))^2 , h^(T)^2 ).

A set T contributes a full bit per unit of h-mass when N^(T) is negligible against h^(T), about
h^2 log(N^2 / h^2) when N^(T) dominates, and by Jensen never more than log(1/Inf) on average. Take the locally
tree-like case: i lies in D terms t_1..t_D of width w that share only i, every mate lies in about D other terms,
and those share nothing else nearby. On T = S + R with S a subset of the mates of one t and R outside,
h^(T)^2 is about 4^{-(w-1)} N_t^(R)^2 for every S (the AND of the mates is flat on its 2^{w-1} sets), while
sum_R N^(S + R)^2 is about rho^{|S|} with rho about D 2^{-w} (the mates in S must be pivotal for N through |S|
different terms). So N dominates only for |S| <= k_0, k_0 about 2w / (w - log2 D), and the sets with |S| <= k_0
carry a fraction about C(w-1, <= k_0) 2^{-(w-1)} of the h-mass. Estimate:

    E_i / Inf_i  is about  2 + O( C(w-1, <= k_0) 2^{-(w-1)} w ),   bounded when D <= 2^{w/3}, say.

(For the instances above this gives about 3.1 at w = 9, D = 24 and about 2.3 at w = 12, D = 35.)

The nested witness sees only K(U) = the last revealed element of U - i. Given i in U, U - i is a uniform subset S
of the mates of one of the D terms, plus an independent "noise" set R drawn from the spectrum of N restricted;
R is empty with probability c bounded away from 0 and 1 for a balanced f. Two kinds of order:
  (a) mates revealed last: K is the top element of S, a single mate z, with B-mass about Inf 2^{-r} / D for the
      r-th mate of its block; the same event without i has mass about Inf (z is in U through one of its other
      terms, whose remaining variables were revealed earlier). Cost: sum_r 2^{-r} log2(2^r D) = log2 D + 2 per unit.
  (b) mates revealed first: the mate events become cheap (mass about Inf^2 without i), but with probability 1 - c
      the last element is a noise element, where i in U and i not in U are in ratio about Inf: cost about
      (1 - c) log2(1/Inf) per unit.
So for every order of these two kinds L / Inf is about min( log2 D + 2 , (1 - c) log2(1/Inf) ), unbounded when D
grows with w. Check against the table: w 12, D about 35: log2 D + 2 = 7.1, measured 6.85 to 6.99; w 9, D 24:
6.6 against a trivial bound of 6.0, measured 5.1 to 5.5.

Consequences, if the heuristic is right.
- FWC as stated in 12 (one nested filtration, conditioning on the last revealed element only) is FALSE on regular,
  locally tree-like monotone DNFs with D -> infinity, D <= 2^{w/3}: every coordinate looks like the root, every
  order pays log D or (1 - c) log(1/Inf), while E_i / Inf_i stays bounded. FEI is not threatened by this family;
  the witness is too coarse for it. FWC remains proved on the classes of 12(i) and FEIB19.
- What separates the two cases is the SECOND element: given i in U the last two revealed elements of U - i are two
  mates of one term (probability 1 - w 2^{-(w-1)}), and without i that event has mass about Inf^2. So the natural
  refinement is the r-witness

      L^{pi,r}_i = H( 1[i in U] | the last r revealed elements of U - i ),   E_i <= L^{pi,r}_i <= L^{pi,1}_i = L^pi_i,

  whose atom masses are again resampling correlations, now of derivatives of order <= r:
  P[i in U, k_1..k_r in U, U misses R] = E D_{k_1}..D_{k_r} h(x) . D_{k_1}..D_{k_r} h(x^R).
  For the tree-like DNF r = k_0 + 1 should suffice (r = 3 for D <= 2^{w/3}; r <= 5 for any linear hypergraph,
  where D <= 2^{w/2}). r = infinity is E_i itself, so "FWC_r for some fixed r" is a ladder between the nested
  witness and FEI. Whether a fixed r can work for all Boolean functions is open; DNFs whose terms share many
  variables (D near 2^w) push k_0 up, so a fixed r is doubtful in general and the useful statement may have to
  let the window grow with the local structure.

Tests owed before any of this is repeated as a result.
  T1. The two-level tree model f = [x_i and OR_t AND_{j in t} z_j] or OR_j [z_j and Q_j(y)], Q_j an OR of D - 1
      disjoint ANDs of width w - 1 on fresh variables. Its spectrum is a tensor product over the D blocks, so
      E_i can be evaluated to any accuracy by importance sampling over T with exact p(T), q(T) (proposal: mixture
      of the spectrum of N and of "one active block"). Compare with the chain bound of mc_chain on the same
      function for orders (a) and (b), and with the r = 2, 3 witnesses. Prediction: E_i/Inf about 2 to 3,
      order (a) about log2 D + 2.
  T2. A lower bound L^pi_i / Inf_i >= c log D over ALL orders pi and all i for a D-regular linear hypergraph DNF
      (the two kinds of order above are not all orders).
  T3. Percolation: is the creep of L/Inf on hex the chain (balls) or the function? Larger boards, and the r = 2
      witness there.

### 12(p) Test T1 run: the tree model confirms 12(o) for the orders tested (10 Nov 06:05)

Status: measurements with an exact model (code/tree_dnf.py, self-test passes: the block formulas against a
13-variable truth table to 1e-9, importance sampling against exact enumeration on four small cases, the r = 1, 2, 3
witnesses against the truth table, grouped against direct evaluation). Not a proof of anything; the orders tested
are "mates revealed last" only (block by block, and round robin over the blocks).

The model. Root x; D blocks of L = w - 1 mates z; each mate z carries Q_z = an OR of D - 1 disjoint ANDs of
width L on fresh variables;  f = [x and OR_t AND_{z in t} z] or OR_z [z and Q_z].  With N_t = prod_{z in t}(1 - z Q_z),
A_t = prod_{z in t} z, N = prod_t N_t, M = prod_t (1 - A_t) N_t the +-1 function has E_x f = N + M - 1 and
D_x f = N - M up to sign, both tensor products over the blocks, so every Fourier weight is a product of block
coefficients that depend only on how many mates of the block are in each of four states. E_root is a sum of
Phi over type tuples and is estimated by importance sampling with exact summands; the witnesses are closed forms
in the block resampling moments (80-digit decimals).

    w    D     P[N=1]   Inf_root    E_root/Inf        L1/Inf (block, robin)   L2/Inf           L3/Inf          log2 D + 2
    10   8     0.612    8.93e-3     2.260 +- 0.004    6.59   6.42             3.21   3.11      2.64   2.64     5.00
    12   16    0.525    3.93e-3     2.127 +- 0.004    7.68   7.39             3.43   3.17      2.45   2.44     6.00
    14   30    0.502    1.79e-3     2.051 +- 0.004    8.64   8.28             3.56   3.13      2.33   2.29     6.91
    16   55    0.507    8.40e-4     2.023 +- 0.004    9.56   9.15             3.62   3.06      2.26   2.19     7.78
    20   196   0.5003   1.86e-4     1.997 +- 0.006    11.49  10.99            3.87   3.00      2.24   2.12     9.61
    24   712   0.4996   4.24e-5     1.995 +- 0.010    13.42  12.86            4.12   2.96      2.25   2.08     11.48
    unbalanced (f is 1 with probability near 1):
    6    4     0.395    3.73e-2     3.330 +- 0.002    5.55   5.46             4.23   4.23      3.94   3.95     4.00
    8    8     0.220    1.10e-2     2.855 +- 0.002    6.64   6.42             4.63   4.49      3.73   3.74     5.00
    9    24    0.0002   1.35e-5     2.703 +- 0.002    7.30   7.12             6.85   6.52      -      -        6.58

(L^r = H(1[root in U] | the last r revealed elements of U among the mates); L^1 is the nested witness of 12.
Balanced rows take D^2 L 2^-L about 1.4, the largest D for which the model is not almost constant. Widths 20
and 24 used 100,000 and 40,000 samples.)

Correction to the reading below (10 Nov 06:15): the root is not the only coordinate. A leaf of this model lies in
one term whose other variables lie in no other term, and such a coordinate is good for the nested witness with
ratio tending to 2 (12(q)). So this family does NOT refute FWC, which only needs one coordinate; what the table
shows is that a root-like coordinate (every mate in D other terms) is bad for window 1 under the orders tested.
The family that would refute FWC is a regular DNF with no private term, where every coordinate is root-like.

Second correction (10 Nov 06:48, from Codex worker FEIB20's all-order table, 12(r)): "under the orders tested" matters
for the root too. The table below is for orders that reveal the mates last. In the "clause" order (each mate
followed at once by the leaves of its own clauses) the root's nested witness is 4.22, 4.82, 5.18, 5.42 at
w 10, 12, 14, 16, against 6.6 to 9.6 for leaves first; the increments shrink (0.59, 0.36, 0.24). So even for the
root the growth like log2 D is a property of mates-last orders (proved for those by FEIB21, 12(s)), not of window 1.

What it shows.
- E_root/Inf falls to 2 along the balanced rows, as the heuristic of 12(o) said (2 + a small term).
- The nested witness with the mates last rises by about 1 per row, i.e. like log2 D + 1.4 to 1.8. So for these
  orders the nested witness is unbounded on this family while E_root/Inf is bounded. (Orders that reveal mates
  before leaves are not covered by tree_dnf.py; 12(o) predicts (1 - c) log2(1/Inf) for them. T2 is still owed.)
- Conditioning on the last TWO revealed mates is enough here: L2/Inf stays near 3.1 in round-robin order
  (3.11, 3.17, 3.13, 3.06) and L3/Inf falls toward E (2.64 -> 2.19). In block order L2 creeps (3.21 -> 3.62):
  with one block revealed after another the last two elements are more often in different blocks.
- The unbalanced row w 9, D 24 (the function is almost constant, every mate is in a satisfied term with
  probability 0.09) needs more than two: L2 6.5 to 6.8. That is k_0 of 12(o) growing as D 2^-w grows.

The down-ratio form 7(e), one coordinate at a time, in divergence language (a restatement, nothing new). With g = E_i f,
h = D_i f, delta = Inf_i, nu_h(T) = h^(T)^2 / delta, and mu_-i(T) = g^(T)^2 + h^(T)^2 the law of U - i,

    delta [ log2(1/delta) - D(nu_h || mu_-i) ]  <=  E_i  <=  delta [ log2(1/delta) - D(nu_h || mu_-i) + 1/ln 2 ],

because Phi(p, q) = q log2((p+q)/q) + p log2(1 + q/p), the first sum is delta [log2(1/delta) - D], and
0 <= p log2(1 + q/p) <= q / ln 2. So i is a good coordinate with constant C exactly when

    D( nu_h || mu_-i )  >=  log2(1/Inf_i) - C     (up to the additive 1.4427),

i.e. the normalised spectrum of the derivative sits on a part of the spectrum of weight about Inf_i: for T drawn
from nu_h the ratio g^(T)^2 / h^(T)^2 is typically O(1), although its nu_h-average is (1 - delta)/delta. The
largest possible value of D is log2(1/delta) (nu_h <= mu_-i / delta), so the statement is "D within a constant of
its maximum". Every witness is a statistic S of T and data processing gives D(S nu_h || S mu_-i) <= D, which is
the inequality L >= E_i again. In this language the tree-DNF finding reads: the statistic "last revealed element"
loses log D of the divergence, "last two" loses O(1).

With 7(b)-(c) (J_i <= (2/ln 2) Inf_i and the exact path formula) this gives, along any decision tree that
queries i_v at node v,  H(f) <= sum_v P[v] ( E_{i_v}(f_v) + (2/ln 2) Inf_{i_v}(f_v) ),  I(f) = sum_v P[v] Inf_{i_v}(f_v):
the divergence bound is needed only on average over a tree, and a node with a coordinate of influence >= c costs
at most h2(c)/c per unit. The open case is restrictions all of whose influences are small.

Where this leaves section 12. The ladder L^1 >= L^2 >= ... >= E_i is the right family of witnesses; L^1 (FWC as
stated) is too coarse for overlapping DNFs under the orders tested; the open statement worth attacking is
"some fixed window r, or a window chosen from the local structure, gives D(S nu_h || S mu_-i) >= log2(1/Inf_i) - C
for some i", together with T2 (all orders) to settle whether FWC with r = 1 is really false.
(Added 06:48: read this paragraph with 12(q)-(s). The tree family has a good leaf, the root is much better under
clause order, and FEIB21 proves the erasure ratio itself tends to 2 at every coordinate of a sparse linear DNF.
"Too coarse" above is a statement about mates-last orders only.)

### 12(q) A private term gives a good coordinate, so the tree model does not refute FWC (10 Nov 06:15)

Status: proved here (short computation, checked line by line; first written by Codex worker FEIB20 and re-derived).
An elementary lemma; not claimed as new.

Lemma (private AND). Let f be Boolean (+-1) and suppose the variables i and B (|B| = k) enter f only through
a = AND(x_i, x_B), i.e. f = A(v) + c(v) a with v the other variables, a in {0, 1}, c in {0, +2, -2}. Put
delta = Inf_i = 2^-k P[c != 0]. Then for the order that reveals v first and B last,

    2 (1 - 2^-k)  <=  E_i / delta  <=  L_i / delta  <=  2 (1 - 2^-k) + 2^-k log2( e 2^k / delta ).

Proof. a = 2^-(k+1) sum over S in B + i of chi_S. So for V in v and S in B: the coefficient of f on V + S + i is
c^(V) 2^-(k+1) for every S; on V + S it is the same number when S is non-empty and A^(V) + c^(V) 2^-(k+1) when S is
empty. Write p_V = c^(V)^2 4^-(k+1); sum_V p_V 2^k = delta. Every T = V + S with S non-empty has g^(T)^2 = h^(T)^2 =
p_V and Phi(p, p) = 2p, which gives 2 (2^k - 1) sum_V p_V = 2 (1 - 2^-k) delta in E_i. In the witness the atom
"last revealed element is the r-th variable of B" has h-mass and g-mass both 2^(r-1) sum_V p_V, again 2 per unit,
with the same total. The remaining atoms (S empty) carry h-mass 2^-k delta and total mass at most 1; Phi is concave
and homogeneous, hence superadditive, so their sum is at most Phi(1, 2^-k delta) <= 2^-k delta log2(e 2^k / delta),
using Phi(q, p) <= p log2( e (p + q) / p ).  QED

Since delta = 2^-k P[c != 0], the last term is 2^-k ( 2k + 1.45 + log2(1 / P[c != 0]) ): the ratio tends to 2 as k
grows unless the private term is pivotal with probability below about 2^(-2^k).

Consequences.
- Every leaf of the tree model of 12(p) is such a coordinate (its clause is private), so min over i of the nested
  witness is about 2 there. 12(o) spoke of regular, locally tree-like DNFs where every coordinate looks like the
  root; the tree model is not one of them, and FWC is not refuted by it. The correction is also inside 12(p).
- The same computation works for any private gadget whose Fourier coefficients at S + i and S agree in modulus
  for non-empty S; AND and OR have this property, a parity gadget has it trivially.
- The family to test is a DNF with no private term in which every variable lies in D terms: random regular DNFs
  (the rdnf rows of 12(o): 6.85 to 6.99 at w 12, D about 35 for four kinds of order, against a predicted E/Inf of
  about 2.3), and structured ones (lines of a plane, D parallel classes). In the sparse regime (f almost constant)
  revealing the variables of i's own terms FIRST looks good: given that the last element j lies on a line through
  i, the set U - i lies inside that line, and the other lines through j contribute only the singleton {j}. In the
  balanced regime the noise part of U - i spoils that order (12(o), kind (b)). FEIB20 is on the question over all
  orders; T2 stands as stated but for leafless families only.

### 12(r) All orders on the tree model, and planes with no private term (10 Nov 06:49)

Sources: Codex worker FEIB20 (codex/workers/FEIB20: REPORT, RESULTS, PROOF, MOMENTS, nested.py; PROOF.md read line
by line, it is the lemma of 12(q) plus an exact leaf influence), my code/guard_order.py and code/leafless.py.
Every number is bits per unit influence.

(1) Leaf theorem (FEIB20, proved; the lemma of 12(q) with the influence made explicit). On the tree model with
D >= 2, L = w - 1 >= 2 and D^2 L 2^-L <= 2, a terminal leaf i with the other L - 1 leaves of its clause revealed last has

    2 (1 - 2^-(L-1))  <=  E_i / Inf_i  <=  L_i / Inf_i  <=  2 + 2^-(L-1) (2L - 2 + 4 log2 e)  <  6,

because Inf_leaf >= 2^-(L+1) e^-3 there. So min over i and orders of the nested witness tends to 2 on this family.

(2) Nested witness, six orders, all variables in the order (FEIB20, closed-form resampling moments, checked against
exact truth tables at n = 13 and 25 and re-run with 70-digit decimals):

    w   D   coordinate   leaves first   mates first   clause   block    random   private last
    10   8  root          6.572          5.539         4.222    6.894    6.295       -
    10   8  mate          5.195          4.996         4.998    5.236    3.957       -
    10   8  leaf          6.576          6.078         6.153    7.043    4.990     2.052
    12  16  root          7.652          6.492         4.816    8.075    7.451       -
    12  16  mate          6.157          6.036         6.047    6.182    4.885       -
    12  16  leaf          8.368          7.914         7.955    9.036    6.932     2.016
    14  30  root          8.616          7.115         5.178    9.096    8.412       -
    14  30  mate          6.829          6.749         6.758    6.844    4.884       -
    14  30  leaf          9.699          9.200         9.223   10.516    6.249     2.004
    16  55  root          9.556          7.559         5.419   10.067    9.307       -
    16  55  mate          7.315          7.262         7.267    7.324    5.007       -
    16  55  leaf         10.738         10.111        10.122   11.672    9.415     2.001

    E/Inf (Monte Carlo, 400,000 samples): root 2.267, 2.124, 2.048, 2.032; mate 2.180, 2.080, 2.031, 2.021.

    Orders: "clause" = each mate followed at once by the leaves of its own clauses; "block" = a block's leaves,
    then its mates; "private last" = clause order with the target leaf's clause-mates moved to the end.
    Small exact cases: n = 13 (w 3, D 2): min_i E/Inf 2.2360, exact minimum over all orders 2.3602 (a mate);
    n = 17: hill search 2.7172 (root; an upper bound only).

    Reading. For the root the clause order is far better than any order I had tried and its increments shrink
    (0.59, 0.36, 0.24 per row, while log2 D rises by about 0.9 per row). Whether it is bounded is not known; four
    rows do not decide it. Why it helps (heuristic): with the root absent from U, a mate in U nearly always brings
    leaves of its own clauses with it, so the label "this mate, and nothing revealed after it" carries little mass
    from the root-absent part; in mates-last orders that label carries almost all of it.

(3) Guarded orders do not beat clause order (mine, code/guard_order.py on FEIB20's moments). Order: unguarded
leaves, then all mates, then the first gam leaves of every clause. The root's witness moves monotonically from the
leaves-first value to the mates-first value: w 10: 6.57 (gam 0), 6.41 (2), 5.96 (4), 5.67 (6), 5.54 (9);
w 12: 7.65, 7.62, 7.14, 6.75, 6.49 (gam 11). Nothing below mates first; the gain of clause order comes from
putting each mate next to its own leaves, not from guarding.

(4) Planes with no private term, exact minimum over all orders (mine, code/leafless.py on filt_big.run). Points of
Z_p^2, terms = the lines of D parallel classes, so every variable lies in D terms of width p, two terms share at
most one point, and the translations act transitively. minE = E_i/Inf_i, F = min over all orders of the nested
witness (subset dynamic programme, exact).

    family       n    mean      Inf       minE     F        F - minE
    AG2_3 D2      9    -        -        2.6293   2.9132    0.284
    AG2_3 D3      9    -        -        2.1015   2.9436    0.842
    AG2_3 D4      9    -        -        1.8943   3.2072    1.313      (all four classes: the affine plane of 12(g))
    AG2_5 D2     25   +0.4900   0.0852   3.1042   3.6753    0.571
    AG2_5 D3     25   +0.3199   0.1031   3.2429   4.1612    0.918
    AG2_5 D4     25   +0.1816   0.1140   2.8775   4.1887    1.311      (added 06:55)
    AG2_5 D5     25   +0.0664   0.1204   2.2003   3.9666    1.766      (added 06:55)
    AG2_5 D6     25   -0.0314   0.1240   1.5496   3.8489    2.299      (added 07:12; all six classes: the affine plane of order 5)

    (AG2_3 D2 is the 3 x 3 grid with rows and columns as terms; its two values equal the PM(K33) values recorded
    in 12(g). The perfect-matching function of K33 and "some row or some column of the 3 x 3 grid is all ones" are
    different functions; I have not explained the agreement and do not lean on it.)

    Reading. On leafless planes the gap F - minE grows with the number of classes through a point (0.28, 0.84, 1.31
    at n = 9; 0.57, 0.92, 1.31, 1.77, 2.30 at n = 25), which is the direction 12(o) predicted, but the numbers are small
    and n is small. F itself is not monotone in D at n = 25 (3.68, 4.16, 4.19, 3.97, 3.85): it peaks near the classes
    count where the function is closest to balanced-with-small-terms and falls as minE falls. Nothing here refutes
    FWC and nothing proves it. The largest F in any exact run is still 4.2019 (perfect matchings of K55, 12(g));
    AG2_5 D4 at 4.1887 is just under it.

### 12(s) Sparse linear DNFs: the erasure ratio tends to 2 at every coordinate (10 Nov 06:49; Codex worker FEIB21)

Source: codex/workers/FEIB21 (REPORT, RESULTS, BELIEF, PROOFS.md sections 1-13). I read PROOFS.md whole and checked
section 12 line by line (steps 1-4 below are my restatement; I found no gap). Sections 2-8 I read but did not
re-derive every constant. Not claimed as new: FEIB21's literature note finds min-entropy results for read-k DNFs
(Shalev; Arunachalam, Chakraborty, Koucky, Saurabh, de Wolf), Shannon entropy for read-k decision trees (Wan,
Wright, Wu) and the general bound with a logarithmic loss (Kelman, Kindler, Lifshitz, Minzer, Safra), none of which
is this statement; a proper search is still owed before the word new is used.

Theorem (LIN). Let f be a monotone DNF, every term of width w, two terms sharing at most one variable, every
variable in at most D terms. L = w - 1, a = 2^-L, i a variable in d >= 1 terms. For 1 <= k <= L put

    gamma_k = a sum_{j<k} C(L, j),      theta = 1 - L (D-1) a - (d-1) a / 2,
    alpha_k = C(L, k) 2^(C(k,2) - 2k) ((D-1) a)^k / (1 - k (D-1) a / 2),
    eps = min(1, d gamma_k),            kappa = alpha_k / (a theta).

If theta > 0, k (D-1) a < 2 and d a <= 1/4, then

    | E_i / Inf_i - 2 |  <=  2 eps + (8 / ln 2) sqrt(kappa) + eps log2( e [3 + 8 / (eps d a theta)] )
                              + d a log2( e [1 + (d a)^-2] ).

Corollary. For fixed epsilon > 0 and D <= 2^((1 - epsilon)(w - 1)), E_i / Inf_i = 2 + o(1) as w grows, uniformly
in the number of terms and in the coordinate (take k > 1/epsilon). Example values of the bound: w 32, D = d = 9848,
k = 3: error 0.1998; w 256, D = 2^191, k = 6: 4.8e-8.

Proof in four steps. N = indicator that no term avoiding i is satisfied; A_t = AND of the L mates of i in its
t-th term (the d mate sets are disjoint). Then h = D_i f = N 1[some A_t], g = E_i f = N + M - 1 with M = N prod (1 - A_t),
so g^ = 2 N^ - h^ off the empty set.
 1. Inf_i / E[N] lies in [d a theta, d a]. Harris (increasing against decreasing events) and Bonferroni.
 2. Split the pivotal points by the first satisfied A_t: h = sum h_t with disjoint supports and h_t = A_t Psi_t.
    The squared spectrum of h_t is uniform over the subsets of the t-th mate set, so all but gamma_k of its mass
    sits on Omega = {sets with at least k mates of some term through i}; Cauchy-Schwarz over the d pieces gives
    h-mass outside Omega at most d gamma_k Inf_i.
 3. For k mates J of one term through i no other term contains two of them, so N = R prod_{j in J} (1 - z_j Q_j)
    and || D_J N ||^2 = 4^-k P[R, all Q_j]. Choosing one residual term per j, the k terms are distinct and pairwise
    share at most one variable, so P[all Q_j] <= (D-1)^k 2^C(k,2) a^k. Summing: N-mass on Omega <= kappa Inf_i.
 4. On Omega, Phi(g^2, h^2) differs from 2 h^2 by at most (4/ln 2) |h^| |g^ + h^| = (8/ln 2) |h^| |N^|;
    Cauchy-Schwarz with 2 and 3. Off Omega use Phi(P, Q) <= Q log2(e (1 + P/Q)) on the eps Inf_i of h-mass.

What the proof uses, in general form (my reading; this is the part to carry to other classes). Write f_0 for the
restriction x_i = 0 (here 2N - 1). For ANY Boolean f, coordinate i and family Omega of non-empty sets,

    | E_i - 2 Inf_i |  <=  2 eps Inf_i + (8/ln 2) sqrt( Inf_i W_Omega(f_0) / 4 ) + eps Inf_i log2( e [3 + 2 / (eps Inf_i)] ) + empty-set term,

where eps Inf_i is the mass of (D_i f)^2 outside Omega and W_Omega(f_0) the Fourier weight of f_0 on Omega. So i is
good as soon as the derivative's spectrum sits, up to a fraction 1/log(1/Inf_i), on a family of sets where the
restriction f_0 has weight O(Inf_i). In (LIN) Omega is "many variables of one certificate": the derivative is a sum
of sub-cube indicators (certificates of codimension L), whose spectra are spread over all subsets of the fixed
variables, while f_0 hardly depends jointly on k variables of one certificate. (The constants in this display are
as I transcribed them from step 4 with A replaced by 1/4 of the weight of f_0; re-derive before quoting.)

Other results of FEIB21 (proved there; read, constants not re-derived):
- Tree model, balanced (lambda = D^2 L 2^-L in a compact interval): E_root/Inf = 2 + O(sqrt(L/D) + L^2/D) with an
  explicit finite bound (E); the same for monotone uniform DNFs with a forest incidence graph (section 3).
- Mates-last orders: one-mate witness = log2 D + O(1) (section 5; this proves the growth seen in 12(p));
  two-mate witness bounded, limsup <= 5 log2 5 + 7 lambda/16 (section 6); the sharper limit 2 + 7 lambda/16 is
  heuristic. Large rows by the compressed evaluator: w 32, D 9848: L1 16.66, L2 2.90; w 240: L1 119.2, L2 2.68.
- Unbalanced scaling D^2 2^-L -> c: E_root/Inf -> 2 but for every fixed r every MATE order has
  r-window witness >= (1/8) P[Poisson(c/4) >= r] log2 D (section 8). Arbitrary interleavings of leaves and mates
  are not covered (and 12(r)(2) shows interleaving matters). w 40: L1 22.1, L2 13.6, L3 7.5; w 80: 42.1, 24.3, 11.9.
- The whole mate neighbourhood U intersect {mates of the root} as statistic has ratio -> 2 in both scalings
  (section 7). A fixed neighbourhood fails on the PM tower: keeping the bottom k levels gives the exact formula
  (PMB) with an extra term d_k [(t - k) log2(1/a0) + ...] growing in the depth t; k about 2 log t / log(1/a0)
  levels suffice. The optimised one-element filtration stays bounded there (12(i): 4.863 at depth 20).
- The coordinate of largest influence need not be good (section 11): a bent function on k bits with one value
  replaced by a fresh root x has E_root/Inf = k + log2 e + o(1); composing the other inputs with balanced MAJ3
  towers of depth k + 1 makes the root the unique maximum. This agrees with 10 (largest influence can be bad) and
  gives a cleaner example. A full 19-variable table: root 2.672, minimum over coordinates 0.834.
- Exact minimum of any r-window over all orders by a subset recurrence (section 9, window_search.py); finite scan
  through dimension 22: largest optimised L2 minimum 3.2195 (cyclic run-of-five on 9 variables).

Why (LIN) is not yet FEI for a class. The good-coordinate route needs a good coordinate in every restriction.
Restrictions of a linear monotone DNF are linear monotone DNFs but the widths become mixed and the bound
D <= 2^((1-epsilon)(w_min - 1)) can fail after terms shrink. FEIB21's proposed next lemma (BELIEF.md): pick a
variable of a SHORTEST term, split the derivative by the first witnessing term, show the pieces from much wider
terms are negligible, and prove (LIN) for the truncated family. Two easy ends of that lemma (mine, 06:49):
 - a term of width 1 (f = y OR r): g^ = h^ on every non-empty set, so E_y/Inf_y = 2 (1 - A) + Phi((1-A)^2, A^2)/A
   with A = P[r = 0], which is at most about 3 for every A. A variable alone in a term is always good.
 - a coordinate of influence >= c is good with h2(c)/c (7).
 The open middle is a shortest term of width between 2 and about log2 D.

### 12(t) Critical percolation: a bulk site is a good coordinate; a fixed block is not a witness (10 Nov 07:08; Codex worker FEIB22)

Source: codex/workers/FEIB22 (REPORT, ARGUMENT, RESULTS, METHODS). I read REPORT and ARGUMENT whole and checked the
argument step by step; it uses only standard arm estimates (Garban, Pete, Schramm, The Fourier spectrum of critical
percolation: quasi-multiplicativity, the bulk pivotal comparison, and P[U meets B] <= 4 alpha_4(B, Q)). It has had
no referee other than me.

Statement. f = left-right crossing of the L x L rhombus of the triangular lattice at p = 1/2, i a site in a fixed
compact part of the interior, delta = Inf_i, a(r) = alpha_4(1, r), R_r = B(i, r) - {i}. With W(R) = P[i in U, U misses R]
and V(R) = P[i not in U, U meets R] (12(l)):

    W(R_r) <= C delta a(r),      V(R_r) <= C delta / a(r)        for r_0 <= r <= cL.

 - W: write W(R_r) = P[i pivotal in x and in x'], x and x' equal outside B(i, r) and independent inside. Both need
   four arms from scale 1 to r/2 (independent copies: a(r/2)^2) and the shared outside needs four arms from 2r to
   the board scale: W <= a(r/2)^2 alpha_4(2r, L) <= C a(r) alpha_4(L) <= C delta a(r).
 - V: V(R_r) <= P[U meets B(i, r)] <= C alpha_4(r, L) <= C delta / a(r).
 So along radii in bounded ratio W(R_r) V(R_r') <= C delta^2, the last jump (r comparable to L, W <= C delta^2) and the
 empty label (q = delta^2) included, and the two-sequence lemma 11(c) gives

    E_i / Inf_i  <=  nested ball witness / Inf_i  <=  C,   uniformly in L.

 A direct sum agrees: a shell costs at most C delta a(r) (1 + log(1/a(r))), summable over dyadic r because a(r) decays
 polynomially. No numerical constant is extracted.

Fixed blocks fail (FEIB22, proved; three lines). B a fixed set of b sites near i, q_0 = P[i in U, U misses B] =
E_y[(E_{x_B} D_i f)^2]. D_i f is 0/1, so its average over x_B is a multiple of 2^-b, hence q_0 >= 2^-b delta, while
p_0 >= 1 - C_B delta. So H(1[i in U] | U cap B) / delta >= 2^-b log2(1/delta) - O_B(1): every fixed block witness
grows like log L. The same three lines hold for ANY monotone function and any block B of b coordinates whose
influences are O(delta): a block witness needs b growing with log log(1/delta) at least. (Mine: this is the
block-side analogue of FEIB21's fixed-window failure in 12(s).)

Numbers (centre site; nested = the mc_chain ball chain; exact for L <= 5, Monte Carlo with 1 s.e. about 0.01 above):

    L    Inf       nested/Inf   two-hit shells/Inf   block r=1   block r=2   E_i/Inf (exact)
    3    0.3203    2.163        1.784                2.074       1.488       1.488
    4    0.1860    3.013        2.662                3.349       2.646       2.108
    5    0.1714    3.122        2.784                3.486       2.556       2.001
    8    0.0931    3.764        3.416                3.959       3.679         -
    12   0.0589    4.085        3.737                4.223       3.911         -
    16   0.0425    4.248        3.897                4.392       4.023         -
    24   0.0262    4.459        4.115                4.580       4.147         -

    Exact optimum over all orders (subset shortest path), centre site: L 3: 1.963 (E/Inf 1.488); L 4: 2.841 (2.108);
    L 5: 3.043 (2.001). Resampling product max_j W(R_j) V(R_j+1) / Inf^2: 1.17, 1.16, 1.16, 1.18 at L 8-24 (flat).

Reading. The slow rise of the nested column that 12(o) recorded (hex 32/48: 4.53/4.69) is a bounded witness
creeping, not a logarithm: the product W V / delta^2 is flat at 1.17 and the argument above bounds the witness.
This is the third proved mechanism for a good coordinate, after comparability (thresholds, 11) and separation
(12(s)); like thresholds it goes through the two-sequence lemma, with geometric scales as the chain.

What it does not give. The good-coordinate route needs every restriction, and restricted crossings lose the
geometry. For the crossing itself FEI needs no route (my remark, 07:08; a sketch, and surely known to the
percolation people - check before quoting): code U by a quadtree. H(U) <= sum over dyadic boxes B of
P[U meets B] * (4 bits for which children are met) <= C sum_r (L/r)^2 alpha_4(r, L), and since alpha_4(1, r) >= r^(-2+eps)
the sum is dominated by r = 1, where it is L^2 alpha_4(L), comparable to I(f) (boundary boxes by the half-plane
three-arm bound). The form of this argument is worth keeping: FEI holds for f whenever some bounded-branching
hierarchy of blocks has E[number of blocks met by U] <= C E|U|.

### 12(u) A hidden coordinate in a monotone function; the largest influence can be bad for monotone f too (10 Nov 07:08; mine)

f(x, y) = MAJ_k(y) OR (x AND [y >= y0]), k odd, y0 a point of weight (k-1)/2. f is monotone, x lies in exactly one
term, of width (k+1)/2, the width of every term of MAJ_k. D_x f = 1[y = y0]: Inf_x = 2^-k and (D_x f)^ is flat,
+-2^-k. E_x f = MAJ_k + 1[y = y0], whose squared coefficients on odd sets of middle size are about 2^-k / k. So
almost all of the derivative's mass sits where the average's spectrum is 2^k / k times larger, and

    E_x / Inf_x  ~  k / 2  =  (1/2) log2(1 / Inf_x)

(the half because MAJ_k has no weight on even sets, where the two spectra agree and Phi = 2q). Exact (code/mono_hidden.py):

    k     n    H/I      Inf_x       E_x/Inf_x    E_y/Inf_y (y in y0 / not)
    5     6    1.955    3.1e-02     4.243        0.326 / 0.386
    9    10    2.153    2.0e-03     5.783        0.041 / 0.042
    13   14    2.304    1.2e-04     7.483        0.0040 / 0.0041
    17   18    2.399    7.6e-06     9.270        0.0004 / 0.0004

    (increments per two steps of k: 0.72, 0.75, 0.79, 0.84, 0.86, 0.89, 0.90, tending to 1.)

Facts read off this.
 1. For majority itself E_i = 0 at every coordinate: E_i f is an odd function of the other k - 1 variables and
    D_i f (the middle slice) is even, so their supports are disjoint and 1[i in U] is a function of |U - i| mod 2.
    The y columns above are small for that reason. E_i can be zero; it is not bounded below by 2 Inf_i.
 2. "Every variable of a shortest term is good" is false for monotone DNFs (x is in a shortest term). FEIB21's
    proposed lemma (12(s), end) must choose the variable, or restrict the class (here terms share many variables).
 3. The largest-influence rule fails for monotone functions as well. Replace each y_j by a balanced monotone
    function phi of m fresh variables (MAJ_m, m about 4^k). With S = union of S_j and T(S) = {j : S_j nonempty},
    (D_x F)^(S) = +-2^-k prod_{j in T} phi^(S_j) and (E_x F)^(S) = (MAJ_k^(T) +- 2^-k) prod_{j in T} phi^(S_j): the
    ratio at S is the ratio at T(S), Phi is homogeneous and sum over non-empty S_j of phi^(S_j)^2 = 1, so E_x and
    Inf_x are unchanged, exactly. The new variables have influence at most 0.63 Inf(phi) < 2^-k. So x is the unique
    coordinate of largest influence, in a monotone function on about k 4^k variables, with E_x/Inf_x ~ k/2, about
    (1/4) log2 n. (FEIB21's example in 12(s) was not monotone.) [Attribution, added 10 Nov 07:59: this is not
    new here. The same composition, Maj_5(y) OR (z AND [y = y*]) with each y_j replaced by Maj_109, is Prop 7.2
    of the 24 Sep 2026 paper FEI_monotone_width; memories fei_most_influential_coordinate_fails_by_composition_2026_09_24
    and fei_monotone_downset_bounded_width_dnf_2026_09_24. See 12(v).] The composition identity is exact; the base rows
    are the table above. Checked exactly (07:14, code/mono_hidden_comp.py): with phi = MAJ_3, E_x/Inf_x = 3.523112,
    4.242673, 4.988771 at k = 3, 5, 7 (n = 10, 16, 22), the base values to six places, also with phi = MAJ_5 at
    k = 3; a block variable has influence Inf_y(f) times the influence of one variable of phi (0.625 x 0.5 at
    k = 3, m = 3). "0.63 Inf(phi)" above means: at most max_j Inf_{y_j}(f) times the influence of a single
    variable of phi, which is below 2^-k once m is of order 4^k / k.
 4. Why extreme hiding is expensive (heuristic, the direction I want to make precise). E_i / Inf_i near log(1/delta)
    forces the normalised spectrum of E_i f to charge the support of (D_i f)^ almost fully. D_i f lives on a set of
    density delta, so |(D_i f)^| <= delta everywhere and its normalised spectrum has min-entropy at least log(1/delta).
    So the average E_i f must itself have a spread spectrum, entropy of order log(1/delta), on functions whose total
    influence is then large (majority: sqrt k; bent: k/2). The cost delta log(1/delta) of such a node is small against
    the influence of the function it sits in. This is where an averaged statement can hold although no rule for a
    single coordinate does.

The accounting that 4 points at (exact, from 7(c)). H(f) = (1/2) H(f_0) + (1/2) H(f_1) + J_i + E_i and
I(f) = (1/2) I(f_0) + (1/2) I(f_1) + Inf_i, so for ANY decision tree that reads every variable on every path

    H(f) = sum over nodes v of P(v) (E + J)(v),      I(f) = sum over nodes v of P(v) Inf(v),

with J <= (2/ln 2) Inf (7(b)). FEI with constant C + 2/ln 2 follows for f from ONE tree whose nodes satisfy
sum_v P(v) E(v) <= C sum_v P(v) Inf(v). Not every node has to be good: a bad node may be paid for by the influence
read elsewhere in the tree. Also min_i E_i/Inf_i <= (sum E_i)/(sum Inf_i) <= H/I, so
sup_f min_i E_i/Inf_i <= sup_f H/I. [CORRECTED 10 Nov 08:17, after FEIB23 section G and FEIB24 section 1: the
first text here said the two suprema are equal. What the reductions give is the bracket
C* - 2/ln 2 <= G* <= A* <= C*, with G* = sup min_i E_i/Inf_i, A* = sup (sum_i E_i)/I, C* = sup H/I; the tree
induction returns C* <= G* + 2/ln 2 only, because of the J terms. Boundedness of the three is equivalent;
equality of the constants is not proved. The lower bound carried to G* is 6.5218 - 2.8854 = 3.636. The
statement 9(a), for the full step cost D_i = E_i + J_i, is correct as written.] Briefs FEIB23-25 are written on
this averaged form.


### 12(v) (10 Nov 07:35-07:59) The step bound is relative to the variance, for every Boolean f; a bad pendant vertex; the random-restriction form

Read first: the brain already held most of the monotone side of this (memory
fei_monotone_downset_bounded_width_dnf_2026_09_24, paper FEI_monotone_width of 24 Sep 2026: step bound
Delta_v <= Inf_v (4.6355 + Psi(4m/Inf_v - 2)) for monotone f through the uniform measure on the zero set, m =
min(P[f=0], P[f=1]); H <= (w + 8.1) I for monotone width-w DNFs and CNFs, 9.41 for 2-DNFs; the failure of the
largest-influence rule by composition, which is fact 3 of 12(u)). What this subsection adds is items 1-3 (no
monotonicity is used anywhere), the example of item 4 and the forms of items 5-7.

 1. Relative step bound (proved here; all Boolean f). With delta = Inf_i, g = E_i f, h = D_i f,

        E_i + J_i <= delta (6.94 + log2(1 + Var(f)/delta)).

    Proof. E_i = sum_T Phi(ghat(T)^2, hhat(T)^2) and Phi is concave and homogeneous, hence superadditive
    (sum_T Phi(p_T, q_T) <= Phi(sum p_T, sum q_T); the first text said "subadditive", the wrong word for the
    inequality used) and increasing in each argument. Split off T = empty: E_i <= Phi(ghat(0)^2, hhat(0)^2) + Phi(A, B) with
    A = sum_{T nonempty} ghat(T)^2 = Var(g) <= Var(f) and B <= delta. Phi(V, delta) = V log2(1 + delta/V) +
    delta log2(1 + V/delta) <= delta/ln 2 + delta log2(1 + V/delta). For the first term |hhat(0)| <= E|h| = delta,
    so it is at most Phi(1, delta^2) <= delta^2/ln 2 + delta^2 log2(1 + delta^-2) <= 1.4427 delta + 1.1610 delta
    (max of x log2(1 + x^-2) on (0,1] is 1.160998, at x^-2 = 3.92; my first note had 1.06, wrong). J_i <=
    (2/ln 2) delta by 7(b). Total constant 1.4427 + 2.6037 + 2.8854 = 6.94.  []
    Referee (Codex worker FEIB28, 10 Nov 09:1x): correct. The empty pair has the shorter estimate
    Phi(p, q) <= 2 sqrt(pq) <= 2 delta (h2(x) <= 2 sqrt(x(1-x))), which gives the same statement with
    2 + 3/ln 2 = 6.3281 in place of 6.94. Every 6.94 below and in 12(w) may be read as 6.33.
    This is the single-set witness with the set N = everything, coarsened to "is U - i empty": the log(1/Inf) of
    the trivial bound E_i <= h2(Inf_i) becomes log(Var/Inf). Checked (code/relative_step.py, seed 1): 160 random
    functions of four biases, n = 4..10, and 622 random DNFs; the left side is at most 0.65 of the right.

 2. Short-term lemma for arbitrary DNFs (proved here; literals of any sign). If f is not constant and t is a
    conjunction of k literals with t <= f, some variable v of t has Inf_v >= 2 P[f = 0] / (2^k - 1).
    Proof. Order the variables of t as v_1..v_k. For x with f(x) = 0 flip, in this order, the variables on which x
    disagrees with t; the end point satisfies t, so some step is an edge (y, y + v_j) with f(y) = 0, f(y + v_j) = 1.
    Given that edge, x agrees with y off v_1..v_{j-1}, so at most 2^(j-1) points x use it. Hence
    P[f = 0] <= sum_j 2^(j-1) Inf_{v_j} / 2 <= (2^k - 1)/2 max_j Inf_{v_j}.  []
    Sharp for a single literal. Checked on every term of the 622 random DNFs: the smallest ratio is 1.0000.
    (24 Sep Lemma 3 is the monotone case, with 1/(2^(k+1) - 2) in its normalisation.)

 3. Consequences, for classes of ALL Boolean functions (no monotonicity).
    (a) If a class is closed under restrictions and every non-constant member has a coordinate with
        Inf_v >= kappa Var(f), then H <= (6.94 + log2(1 + 1/kappa)) I on the class (tree accounting of 12(u)).
    (b) Every DNF or CNF of width w: Var <= 4 P[f=0], so kappa = 1/(2(2^w - 1)) and H <= (w + 7.94) I.
        Measured on the 622 random DNFs: H is at most 0.44 of this bound (largest H/I 4.02).
    (c) Every DNF with m terms: take a shortest term, width k, and the variable v of item 2, so that
        Var/Inf_v <= 4 P[f=0] P[f=1] (2^k - 1) / (2 P[f=0]) = 2 P[f=1] (2^k - 1). If 2^k <= 2m this is below 4m;
        otherwise P[f=1] <= m 2^-k and it is at most 2m. A restriction has at most m terms, so (a) applies with
        kappa = 1/(4m): H <= (6.94 + log2(1 + 4m)) I.
        (The first text said "if 2^k <= 2m use (b)". That step was wrong: a shortest term of width k does not
        make the DNF of width k, e.g. x_1 OR (x_2 AND x_3 AND x_4). The bound is unchanged. Referee FEIB28.)
    (d) Decision trees: by the O'Donnell-Saks-Schramm-Servedio inequality max_v Inf_v >= Var / (expected depth),
        and a tree with s leaves has expected depth at most log2 s under every restriction. So
        H <= (6.94 + log2(1 + log2 s)) I for s-leaf decision trees, and H <= (6.94 + log2(1 + d)) I for depth d.
    (e) Where the conjecture lives: if H(f) > C I(f) with C > 6.94, then SOME restriction of f is non-constant
        with every influence below Var / (2^(C - 6.94) - 1) (the contrapositive of (a)). Families with all
        influences small against the variance, which motivate this: balanced tribes, majority, graph properties,
        percolation, the PM(K33) towers.
        (The first text called the open case "all influences small against the variance, hereditarily". That
        is not what the contrapositive gives and cannot hold on every restriction: a minimal non-constant
        restriction is a dictator, with influence equal to the variance. The list is a motivation, not a
        characterization. Referee FEIB28.)
    Status: 1 and 2 proved and re-derived once; (a)-(e) follow in two lines each. The monotone versions are the
    24 Sep results. Item 1 refines the step of Han's theorem (arXiv:2312.08271, Theorem 1:
    Ent(f) <= (1/ln 2)(3 I + sum_k I_k ln(4/I_k)), proved by adding the coordinates one at a time in a fixed
    order with loss I_k log(4/I_k) per step; no statement there is relative to the variance or adaptive, and it
    has no corollary on DNFs or decision trees - theorem list read 10 Nov 08:14). See 12(w) for the fixed-order
    form of item 1. Whether the non-monotone statements (b)-(d) are in the literature is NOT yet checked (owed:
    Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf arXiv:1809.09819, Wan-Wright-Wu arXiv:1312.3003,
    Gopalan-Servedio-Tal-Wigderson on sensitivity, Chakraborty-Kulkarni-Lokam-Saurabh); do not call them new before.
    First look (10 Nov 08:0x, abstracts and two web searches only): Wan-Wright-Wu (arXiv:1312.3003) have
    H <= 12 d Inf for a decision tree of expected depth d when Inf >= 1, and 9k Inf for read-k trees, both linear
    where (d) is logarithmic but hereditary; Arunachalam et al. have the min-entropy form for read-k DNFs and
    H <= 2 aUC^xor; the searches returned nothing on bounded width with unbounded read. The theorem statements of
    those papers are still unread, so the status stays "not known to be new".
    Second look (10 Nov 11:00-11:04, theorem lists read through ar5iv.labs.arxiv.org/html/1806.03646 and
    ar5iv.labs.arxiv.org/html/1911.10579, first 100,000 characters of each):
      - Shalev (arXiv:1806.03646) Theorem 6/24: H <= (4 log L + 11) Var + 10 I for L the spectral l1-norm, hence
        (4 log s + 21) I for s-leaf trees and (4 d + 21) I for depth d. Item (d) has log2(1 + log2 s) and
        log2(1 + d) in place of log s and d. That paper states no Shannon-entropy bound for width-w or m-term DNFs
        (its DNF results are min-entropy, regular read-k). Its Theorem 9/31: O(sqrt k) I for read-k trees.
      - Kelman, Kindler, Lifshitz, Minzer and Safra (arXiv:1911.10579) Theorem 1.3:
        H[f^{<=D}] <= K sum_{|S|<=D} |S| log(|S|+1) fhat(S)^2 + K I, K an absolute constant. For degree d this is
        H <= K (1 + log(d+1)) I, so the depth-d form of (d) is known up to the constant (here the constant on
        log2(1+d) is 1 and the additive one is 6.94). The s-leaf, width-w and m-term forms do not follow from
        Theorem 1.3 as stated (it needs E|U| log|U| against I, not a degree bound).
      Verdict for now: (a) with its hereditary hypothesis and the explicit constants are ours to state; the
      logarithmic dependence on depth is theirs. Wan-Wright-Wu and Chakraborty-Kulkarni-Lokam-Saurabh theorem
      statements are still unread.

 4. A bad pendant vertex in a 2-DNF (exact; code/graph_pendant.py). Graph functions f_G = 1[the set of ones is not
    independent] are the monotone 2-DNFs. Take the clique on y_0..y_k with a pendant vertex x on y_0:
    f = Thr_2(y) OR (x AND y_0), n = k + 2.

         k   n   Inf_x      E_x/Inf_x  E_y0/Inf_y0  E_y1/Inf_y1  H/I     log2 k
         2   4   1.250e-01  3.5231     0.7046       1.1744       1.8991  1.000
         3   5   6.250e-02  4.3352     2.0839       1.9101       2.4980  1.585
         4   6   3.125e-02  4.7142     2.5879       2.4214       2.9696  2.000
         6   8   7.812e-03  5.0634     2.6441       2.4546       3.4456  2.585
         8  10   1.953e-03  5.3209     2.3694       2.2262       3.6190  3.000
        10  12   4.883e-04  5.5437     2.1861       2.0721       3.6859  3.322
        12  14   1.221e-04  5.7394     2.0977       1.9999       3.7175  3.585
        14  16   3.052e-05  5.9124     2.0592       1.9717       3.7371  3.807
        16  18   7.629e-06  6.0665     2.0425       1.9625       3.7521  4.000
        18  20   1.907e-06  6.2052     2.0345       1.9605       3.7647  4.170

    By hand: D_x f is the indicator of the single point (y_0 = 1, the other y zero), so hhat(T)^2 = 4^-(k+1) for
    every T, while ghat(T) = 2^-(k+1) (2(k + 2 - 2|T|) -+ 1): ghat^2/hhat^2 is about 4 (k + 2 - 2|T|)^2, of order 4k
    on a typical T, and E_x/Inf_x = log2 k + O(1) (measured difference 2.3 falling to 2.0). Here Var/Inf_x is
    about 4k (exactly (4k+6)(1 - (2k+3)/2^(k+2)), referee FEIB28; the order follows from summing ghat(T)^2 above:
    2^-(k+1) times 4 E(k + 2 - 2|T|)^2 = 4(k+2) 2^-(k+1) up to the +-1; this line said "about 2k" until 10 Nov
    10:00, which was wrong), so the logarithm of item 1 is attained inside the 2-DNFs: the pendant x has a term to itself
    ({x, y_0}) and is still bad, because its only mate is shared (12(q) needs the whole term private). The good
    endpoint of the edge is y_0, as item 2 says it must be (Inf_y0 >= (2/3) P[f=0]).
    In general, for a graph G and T a set of vertices put lambda_u = -1 on T and +1 off T and let Z_G(lambda) be
    the independence polynomial. Then fhat(T) and fhat(T + v) are proportional to Z_{G-v} + Z_{G-N[v]} and
    Z_{G-v} - Z_{G-N[v]} (the deletion recursion Z_G = Z_{G-v} + lambda_v Z_{G-N[v]}), so v is bad exactly when the
    occupation ratio Z_{G-N[v]}/Z_{G-v} is near 1 at typical signed activities.
    Correction (referee FEIB28): this holds for NONEMPTY T only. The sign function is 1 - 2 [independent], so
    with X = Z_{G-v}, Y = Z_{G-N[v]} at T = empty: fhat(empty) = 1 - 2^(1-n) (X + Y) and
    fhat({v}) = -2^(1-n) (X - Y) up to a global sign; they are not proportional to X + Y and X - Y there
    (k = 2: the coefficients are 1/8 and -1/8, squared ratio 1, while X = 4, Y = 3 would give 49).
    The asymptotic E_x/Inf_x = log2 k + O(1) stands: the empty atom has mass 2^-(k+1) and is set aside;
    Jensen gives the upper bound and the binomial small-ball estimate P(|2(k+2-2|T|) -+ 1| <= t sqrt k) <=
    C (t + k^-1/2) bounds the negative part of the logarithm, which gives the lower bound.

 5. Random-order form of the tree identity (proved; checked to machine zero on six random 4-variable functions,
    code/rand_restrict_identity.py). With EE(g) = sum_i E_i(g), JJ(g) = sum_i J_i(g) and rho a p-random restriction,

        H(f) = sum_{m=1..n} (1/m) E_{rho with m free variables} [EE(f_rho) + JJ(f_rho)]
             = integral_0^1 E_rho [EE(f_rho) + JJ(f_rho)] dp/p,        I(f) = integral_0^1 E_rho I(f_rho) dp/p.

    (Average the tree identity over uniformly random query orders; integral_0^1 P[Bin(n,p) = m] dp/p = 1/m.)
    JJ <= 2.89 I and EE <= H (Han). Bootstrap: on a restriction-closed class, if E_rho EE(f_rho) <= L p I(f) for all
    p <= p0, then C*(class) <= L + 2.89/p0. So FEI is a statement about the edge entropy of p-random restrictions
    for small constant p. Parity lifts (f o XOR_k) keep their structure under such restrictions, so "restrictions
    simplify" cannot be the whole proof; for width-w DNFs it would be a switching statement at pivotal points.

 6. Granularity (proved; checked, ratio at most 1.0000 with equality cases). For every S,
    fhat(S)^2 <= 4^(|S|-1) M(S)^2, M(S) = sum of fhat(S')^2 over S' containing S: the top coefficient of a Boolean
    function of d bits is a multiple of 2^(1-d), so |fhat(S)| <= E_rho |f_rho^(S)| <= 2^(|S|-1) E_rho f_rho^(S)^2.
    |S| = 1 is fhat(i)^2 <= Inf_i^2. Alone it only gives bounds exponential in the degree.

 7. Angle form. With (f_0hat(T), f_1hat(T)) = r_T (cos theta_T, sin theta_T) for the two restrictions at x_i and
    nu = (mu_0 + mu_1)/2: beta_T = sin^2(theta_T - pi/4) = (f_0hat - f_1hat)^2 / (2 (f_0hat^2 + f_1hat^2)),
    Inf_i = E_nu beta, E_i = E_nu h2(beta). A coordinate is bad when beta is small but nowhere zero on nu-typical
    T (the two restrictions have nearly equal coefficients everywhere); it is good when beta is 0 or of order 1.

 8. A bound that does not help: delta log2(1/delta) <= 2 I(D_i f) by the edge-isoperimetric inequality, so
    E_i <= 2 I(D_i f) + 1.44 Inf_i, and along a tree H <= E[|U|(|U| - 1)] + 4.33 I. This is the trivial bound again.


### 12(w) (10 Nov 08:17-08:27) Round 7 read; the bracket for the good-coordinate constant; the fixed-order form of the step bound; where the step bound cannot be enough

 1. Corrections made inside the entries they correct (10 Nov 08:17): 12(u) no longer says
    sup min_i E_i/Inf_i = C*; the bracket is C* - 2/ln 2 <= G* <= A* <= C* (G* = sup_f min_i E_i/Inf_i,
    A* = sup_f sum_i E_i / I, C* = sup_f H/I). 12(v) item 1 says "superadditive". 12(v) status names Han's theorem.

 2. Fixed-order form of the step bound (proved; checked, code/han_refine.py). For any order k_1, ..., k_n of the
    variables, V_j = {k_j, ..., k_n}, and W_j = sum of fhat(S)^2 over the sets S that MEET V_j:

        H(f) <= 6.94 I(f) + sum_j Inf_{k_j} log2(1 + W_j / Inf_{k_j}),      W_j <= min(Var f, sum_{k in V_j} Inf_k).

    Proof. Tree identity in the fixed order: H(f) = sum_j E_rho[(E + J)_{k_j}(f_rho)], rho a uniform assignment
    of k_1..k_{j-1}. Item 1 of 12(v) at each node, then Jensen for (a, b) -> a log2(1 + b/a) (concave, being the
    perspective of log2(1 + b)): E_rho Inf_{k_j}(f_rho) = Inf_{k_j}(f) and E_rho Var(f_rho) = W_j.  []
    (My first note had W_j as the mass of the nonempty sets INSIDE V_j; that is wrong, the restriction averages
    fold every S onto its trace on V_j.)
    Against Han (arXiv:2312.08271: H <= 6.33 I + sum_k I_k log2(1/I_k)): log2(1 + W/I_k) <= log2(1/I_k) + 1, so
    this is never more than 1.61 I worse and it gains where W_j is small against 1: biased functions, and the
    tail of an order with decreasing influences. Consequences: H <= (6.94 + log2(n + 1)) I always (T_j <=
    (n - j + 1) Inf_{k_j} in decreasing order; a bound of this shape is folklore); and FEI with constant
    6.94 + log2(1 + K) for every f whose influences, sorted decreasingly, have tails sum_{k >= j} Inf_k <=
    K Inf_j (geometric decay; no restriction-closure is needed, unlike 12(v)(a)). No gain when the influences
    are equal. Measured (seed 1; orders natural, decreasing influence, increasing influence, random): H is at
    most 0.458 of the right side on 160 random functions, 0.463 on 192 random DNFs, 0.346 on tribes 4x3, MAJ11
    and three thresholds with geometric weights; never above 1. Against Han's right side ours is 1.02-1.04
    times as large at the median and at most 1.25 times (the smallest ratio was not recorded): on these
    families it is NOT an improvement in size, only in shape (it sees the variance). Treat it as a remark.
    Priority (referee FEIB28, who opened the papers; I have not read this one myself): Keller, Mossel and
    Schlank (arXiv:1105.2651, Claim 4.1) have H <= sum_i h2(Inf_i), hence H <= I/ln 2 + sum_k I_k log2(1/I_k),
    which is stronger than Han's constants; Han's second version acknowledges earlier related work, and the
    2025 strengthening by Li and Han (arXiv:2512.03117) was withdrawn for this reason. The restriction-tree
    induction is published in Gopalan-Mehta-P. (arXiv:2606.00246v2, as cited by the referee). The W_j-shaped
    bound was not found in the papers opened; nothing more than that is claimed for it.

 3. Where the step bound cannot be enough (by hand). Tribes of width w with about 2^w ln 2 blocks: every influence is
    delta ~ 2^-w up to a factor w, Var is of order 1, so the step bound charges delta (w + O(1)) at the root.
    Querying inside one tribe: after j ones (probability 2^-j) the next variable of the tribe has influence
    2^j delta and variance over influence 2^(w-j), so the tribe is charged delta sum_j (w - j) = delta w^2 / 2
    against its influence w delta. By symmetry every first query is charged the same, while the true H/I of
    tribes is bounded. By Talagrand's inequality all influences <= delta forces I >= c Var log(1/delta).
    In supersolution language: Psi = C I + Theta with Theta = sum_j Inf_j log2(1/Inf_j) satisfies
    Psi(g) - avg Psi(g_b) >= (E + J)_i(g) at every node (the bound of Keller-Mossel-Schlank and Han, any
    order; C = 3/ln 2 is enough); FEI needs a Theta that is O(I). The step envelope of 12(v) item 1 by itself
    can overcharge: tribes and the pendant example of 12(v) item 4 have similar (Var, influence) at the queried
    node, with true costs O(delta) and delta log(Var/delta).
    Corrections (referee FEIB28, 10 Nov 09:1x), three statements of the first text withdrawn:
    (i) "No tree does better by symmetry at the root" - symmetry equates the first queries only; nothing is
        proved about adaptive continuations. NOT PROVED.
    (ii) "the functions on which the step bound loses the factor log(Var/delta) are exactly those where
        Talagrand's inequality is tight" - WRONG. Odd majority: Var = 1, delta ~ sqrt(2/(pi n)), I = n delta; the
        step bound loses log2(1/delta) at every coordinate while I / (Var log(1/delta)) tends to infinity.
    (iii) "no functional built from the pair (Var, influences) alone can work" - NOT PROVED; no class of
        potentials was fixed and no matching pair of functions was exhibited. What stands is the sentence
        above about the envelope of item 1.

 4. What the exact step cost is (two-sided inequalities, not an identity; by hand, then checked in
    code/step_info.py, see 12(x)). With p_T = ghat(T)^2,
    q_T = hhat(T)^2, rho_h = q/delta the law of U - i given i in U:

        delta E_{rho_h}[log2(p/q)]_+  <=  E_i  <=  delta (1/ln 2 + 1) + delta E_{rho_h}[log2(p/q)]_+ .

    (sum_T p log2(1 + q/p) <= delta/ln 2 and log2(1 + x) <= 1 + [log2 x]_+.) So i is good exactly when, given
    i in U, the rest U - i falls where ghat(T)^2 <= 2^K hhat(T)^2 on a log-average; and since g and h have
    disjoint supports as functions (h = +-1 on the sensitive set B_i of measure delta, g = +-1 off it, g h = 0),
    |hhat(T)| <= delta everywhere. In the form with the two restrictions: ghat = (f_0hat + f_1hat)/2,
    hhat = (f_0 1_B)^ ; the coordinate is bad when the spectrum of f_0 restricted to B_i sits on sets T where
    f_0 and f_1 have nearly equal coefficients. The single-set and filtration witnesses of sections 10-12 are
    coarsenings of the statistic T; the exact statement has no coarsening.

 5. Scale form of the chain rule (Shannon only; no Boolean input). Give the coordinates independent uniform
    times and reveal U in that order: H(U) = integral_0^1 a(p) dp, a(p) = sum_i E_{R p-random, i not in R}
    H(1[i in U] | U cap R). a is non-increasing, a(0) = sum_i h2(Inf_i), a(1) = sum_i E_i. So
    sum_i E_i <= H <= sum_i h2(Inf_i), and FEI asks that a drop from its trivial value to O(I) on a set of
    scales p of measure bounded below. The joint law of (U cap R, 1[i in U]) is the average over restrictions of
    the spectra of f_rho on R + i, and conditional entropy is concave in the joint law, which is 12(v) item 5
    seen from the other side (the gap is the JJ term).
    Two precisions (referee FEIB28): in the i-th summand R is a p-random subset of the coordinates other than
    i. The concavity gap is a conditional mutual information, J_full - J_marginal for the mixture, not JJ
    itself in general. And a drop of a(p) on a set of scales of positive measure is necessary for FEI, not
    sufficient: the remaining scales must be bounded too.

 6. Transitive functions. If a transitive group of coordinate permutations fixes f, all E_i/Inf_i are equal, so
    min_i E_i/Inf_i = sum_i E_i / I <= H/I: for such f the good-coordinate statement is ONE inequality,
    E_1 <= C Inf_1. It follows from FEI and is weaker than FEI for transitive functions (their restrictions are
    not transitive). Use: (i) a search over cyclically invariant functions for large E_1/Inf_1 is a search for
    lower bounds on G* and A* in a space of 2^(orbits) functions (the best explicit min_i E_i/Inf_i so far is
    3.7137, FEIB24; the transferred bound is 3.636. Since 10 Nov 09:1x: worker FEIB26 reports towers of the
    9-variable transitive PM(K33) function with E_1/Inf_1 above four, limit about 4.474 - see 12(y) item 4 for
    the formula and the state of my check); (ii) a proof of the one-coordinate inequality for graph
    properties or for all transitive functions would be a new unconditional statement. Not searched yet.

 7. Round 7 proofs, state of the reading (10 Nov 08:05-08:15, first read; a line-by-line verdict is owed for the
    parts marked unread):
      FEIB24 PROOFS 1 (the bracket), 2 (parity leakage E_i <= h2(even spectral mass)), 3-5 (charging theorem for
        the hidden-coordinate family, sum_i E_i <= 2 I, and <= 5 I after disjoint balanced odd monotone
        substitutions): read, no gap found. Sections 6, 7, 9: unread.
      FEIB23 PROOFS D (bias bound), F (the family TD(w, Q)), G (the bracket): read, no gap found; the end of C
        read; A, B and the start of C unread.
      FEIB25 PROOFS and PAPER: unread (fixed-level impossibility, A_1 and A_2 bounds, the deduction
        sum_i E_i <= C E[|U| log2(|U| + 1)] from arXiv:1911.10579).
    TD(w, Q) (lines over F_Q on w columns, Q = 2^k, w = k + 2 ceil(log2 k) + 1): the expected number of
    satisfied terms is Q^2 2^-w = 2^k / (2 k^2), which grows, so the function is far from balanced
    (P[f = 0] about exp(-2^k/(2k^2)) if the terms were independent; two lines share at most one point, so
    Janson's inequality applies and this is the right order). Heuristic only: in that regime the spectrum
    should look like that of a biased tribes function, whose H/I is 4 + O(1/w); if so the family is a place
    where the certificates fail, not where FEI fails. Not computed beyond n = 25.


### 12(x) (10 Nov 08:55) Exact forms of the step cost; FEI as a divergence from the product measure; the cyclic search so far

Notation as in section 7: f = g + x_i h, g = E_i f, h = D_i f (functions of the other n - 1 variables),
p_T = ghat(T)^2, q_T = hhat(T)^2, delta = Inf_i = sum_T q_T, rho_g = p/(1 - delta), rho_h = q/delta, nu = p + q
(the law of U - i), a = f0hat(T), b = f1hat(T) for the two restrictions f_0 = g + h, f_1 = g - h.
E_i = H(1[i in U] | U - i) = sum_T Phi(p_T, q_T).

All of (A)-(D) are exact identities or inequalities, PROVED (each is two lines) and CHECKED NUMERICALLY:
`python step_info.py 1` in code/ (1193 (function, coordinate) pairs, random functions and random DNFs at
n = 5..8; largest residual 2.1e-15; the sandwich (C) never violated).

 (A) Information form.
       E_i = h2(delta) - I(1[i in U]; U - i) = h2(delta) - (1 - delta) D(rho_g || nu) - delta D(rho_h || nu).
     Since nu >= delta rho_h, D(rho_h || nu) <= log2(1/delta), and
       E_i / delta = log2(1/delta) - D(rho_h || nu) + r,   0 <= r <= 1/ln 2
     (delta (log2(1/delta) - D(rho_h || nu)) = sum_T q log2(1 + p/q) and delta r = sum_T p log2(1 + q/p)).
     A coordinate is good (E_i <= C Inf_i) exactly when D(rho_h || nu) >= log2(1/delta) - C': the part of the
     spectral sample outside i must tell, up to a likelihood ratio of order 1/delta, whether i is in the sample.
     A coordinate is bad when rho_g is about as large as rho_h on most of the rho_h mass (p_T about q_T / delta).

 (B) Angle form. With m_T = (a^2 + b^2)/2, s_T = 2ab/(a^2 + b^2), c_T = (a^2 - b^2)/(a^2 + b^2) (s^2 + c^2 = 1):
       E_i = sum_T m_T h2((1 + s_T)/2),   J_i = sum_T m_T (1 - h2((1 + c_T)/2)),   Inf_i = (1/2) sum_T m_T (1 - s_T).
     Proof: ghat = (a + b)/2, hhat = (a - b)/2, so p + q = m and p/(p + q) = (1 + s)/2; and
     H(nu) - H(a^2)/2 - H(b^2)/2 = sum_T m [1 - h2(a^2/(2m))].
     The cost E_i + J_i is even in s; the influence is not. Multiplying f by x_i sends b to -b: E_i and J_i are
     unchanged and Inf_i becomes 1 - Inf_i. (This is the parity leakage of FEIB24 seen per frequency: mass with
     a = -b costs influence and no entropy.)

 (C) Sandwich.
       delta E_{rho_h}[log2(p/q)]_+  <=  E_i  <=  delta (1/ln 2 + 1) + delta E_{rho_h}[log2(p/q)]_+ .
     Proof: Phi(p, q) = p log2(1 + q/p) + q log2(1 + p/q); the first term is in [0, q/ln 2]; and
     [log2 r]_+ <= log2(1 + r) <= 1 + [log2 r]_+.

 (D) Real-space constraints. g h = 0 and g^2 + h^2 = 1 pointwise: h = f_0 1_B and g = f_0 1_{B^c}, where B is the
     set of points of the (n - 1)-cube at which coordinate i is pivotal (measure delta). In Fourier space
     ghat * hhat = 0 (ghat is orthogonal to every translate of hhat) and ghat * ghat + hhat * hhat = delta_empty.
     So the good-coordinate statement reads: for every Boolean function there is a direction i such that the
     function cut to its sensitive set B_i and the function cut to the complement have spectra that are far from
     proportional, in the sense of (A).

 (E) FEI as a divergence from the product measure (exact; a restatement, recorded because it names the object).
     Let X = (1[i in U])_i and pi_f the product measure on subsets with the same marginals, pi_f = prod Bern(Inf_i).
     Then
       H(mu_f) = sum_i h2(Inf_i) - D(mu_f || pi_f),
     so H <= sum_i h2(Inf_i) <= sum_i Inf_i log2(1/Inf_i) + I/ln 2 with no work (this bound is Claim 4.1 of
     Keller-Mossel-Schlank, arXiv:1105.2651, as reported by the referee FEIB28), and
       FEI  <=>  D(mu_f || pi_f) >= sum_i Inf_i log2(1/Inf_i) - C I   for every Boolean f.
     The erasure form is the same with the dual total correlation added:
       sum_i E_i = sum_i h2(Inf_i) - TC(X) - DTC(X),   TC = D(mu_f || pi_f),   DTC = H(X) - sum_i H(X_i | X_-i) >= 0,
     and the equivalence of section 7 says the DTC term may be added or dropped at the price of 2/ln 2 in the
     constant. In words: FEI says the spectral sample of a Boolean function is as far from independent as its
     marginals allow, up to O(I) bits. A linear test function sees only the marginals, so any proof through the
     Donsker-Varadhan form D >= E_mu[phi] - log E_pi[e^phi] needs phi that reads the joint position of the sample.
     HEURISTIC, not proved: the size of the sample is not enough. Under rho_h the sample has at least about
     0.2 log2(1/delta) points with high probability (level inequality for h, which is supported on a set of
     measure delta), while under nu the size has mean at most I; but the upper tail of |U| for Boolean f can be as
     heavy as I/k, so the statistic |U - i| separates rho_h from nu only up to log2(log(1/delta)/I) bits, not
     log2(1/delta).

 Where the rho_h mass sits (step_info.py table; buckets of log2(p/q)):

     function, coordinate      Inf      E/Inf   J/Inf   E_rho_h[log2(p/q)]_+   mass at p <= q   largest bucket hit
     tribes 3 x 3              0.1914   2.547   2.165   0.646                  0.750            (4, 8]: 0.059
     tribes 4 x 3              0.1675   2.428   2.080   0.477                  0.750            (4, 8]: 0.083
     tribes 3 x 4              0.1099   2.614   2.108   0.681                  0.875            (4, 8]: 0.125
     tribes 2 x 6              0.0308   2.292   2.028   0.309                  0.969            (8, inf): 0.031
     majority 9, 11, 13        0.27..   0       0       0                      1.000            -
     pendant(k), small coord,  2^-(k+1) 2.454, 2.178, 2.060, 2.019            0.938 .. 0.999   one bucket, mass 2^-(k+1)
       k = 3, 5, 7, 9
     random, n = 12            0.5088   1.082   0.855   0.232                  0.823            (4, 8]: 0.006

   (pendant(k): x_1 unless x_2..x_{k+1} are all ones, then x_1 AND x_{k+2}. Its small coordinates are GOOD: the
   ratio tends to 2. This is not the pendant graph of 12(v) item 4.) In every row 75 to 99.9 percent of the rho_h
   mass sits where p <= q and the rest is in one or two buckets (tribes 3 x 3 also has 0.191 in (1, 2],
   tribes 4 x 3 has 0.167 in (0, 1]).

 Cyclic search (12(w) item 6), state at 08:53. Objective G = E_1/Inf_1 over cyclically invariant functions
 (code/cyc_hill.py; Mac mini 2). The bar is 3.7137 (best explicit min_i E_i/Inf_i, FEIB24).

     n    start     best G    H/I      I      state
     14   random    2.9121    3.3413   2.98   finished (1500 sweeps), frozen
     14   tribes 3  3.0576    3.6997   2.05   finished, frozen at a local optimum next to the start
     15   tribes 3  3.1500    3.8066   2.02   running, frozen
     16   random    2.4730    2.8584   4.75   running (sweep 140)
     16   tribes 4  3.0435    3.5303   2.92   running, frozen
     18   tribes 4  2.9033    3.4911   3.27   running (sweep 8)

 Nothing is near the bar. The structured starts sit in local optima at this temperature; the two hotter runs
 (archived as hot_run1, hot_run2) lost the structure. The record functions for H/I are towers, and a tower of a
 transitive base is transitive, so the next search is over towers (worker FEIB26, task 2), not over single-level
 cyclic functions.

 Hill search over the filtration ratios (Mac mini 2, ended): best rhoF 3.5932 (n = 10, seed 39, rhoE 3.1805),
 3.4189 (n = 8, seed 34), 3.4101 (n = 9, seed 36); best gap 1.8463 (n = 9, seed 41, rhoE 0). Files code/hill_out/.

### 12(y) (10 Nov 09:00-09:22) The step cost as a log-average of one ratio; what coarse statistics see; a maximally bad coordinate; transitive towers reach 4.475; round 8 so far

 Corrections from the referee (worker FEIB28) to 12(v), 12(w) and 12(x)(E) are written inside those entries.

 1. One ratio decides whether a coordinate is good. Fix i, delta = Inf_i, and for T not containing i write
    a = f_0hat(T), b = f_1hat(T) for the coefficients of the two restrictions x_i = +1, -1. Then
    p_T = ghat(T)^2 = (a+b)^2/4, q_T = hhat(T)^2 = (a-b)^2/4, nu_T = p_T + q_T = (a^2+b^2)/2, rho_h = q/delta, and

        rho_h(T) / nu(T) = (a-b)^2 / (2 delta (a^2+b^2)),
        log2(1/delta) - D(rho_h || nu) = E_{T ~ rho_h} [ log2( 2 (a^2+b^2) / (a-b)^2 ) ]  =: Lam_i  (>= 0),

    and by 12(x)(A)  Lam_i <= E_i/Inf_i <= Lam_i + 1/ln 2. So: draw T from the spectrum of the derivative
    D_i f; the coordinate is good exactly when the two restrictions' coefficients at T are not nearly equal, on
    a log-average. FEI is equivalent to: every Boolean f has a coordinate with Lam_i <= C
    (sup_f min_i Lam_i lies in [C* - 3/ln 2, C*]).
    A single event is not enough in general: for a set A of frequencies, data processing gives
        Lam_i <= (1 - rho_h(A)) log2(1/delta) + rho_h(A) log2(nu(A)/delta) + 1,
    so an event with nu(A) <= C delta proves the coordinate good only if rho_h(A^c) log2(1/delta) = O(1).

 2. What coarse statistics recover (code/sep_stat.py, seed 1; exact transforms). For a statistic s(T) the
    deficit_s = log2(1/delta) - D(s(rho_h) || s(nu)) is an upper bound for Lam_i. Statistics tried: |T|; the
    number of low-influence coordinates in T; the projections of T on the low- and high-influence coordinates;
    the projection on the best 1..4 coordinates found greedily.
      majority-like coordinates (the y-coordinates of the 12(u) family): |T| is sharp (full 0.066, size 0.088).
      tribes 3x3, 4x3, 3x4, 2x6: full 1.28-1.56; four greedy coordinates 1.50-1.74; |T| 2.2-2.8. The witness is
        the projection on the coordinate's own clause, as in 12(d); the size loses a bit.
      pendant graph, clique vertices: |T| is within 0.1 of full (1.15-1.6).
      bad coordinates stay bad under every statistic, as they must: 12(u) hidden coordinate full 3.77, 4.56,
        5.40 at k = 7, 9, 11; pendant vertex 3.77, 4.11, 4.31 at k = 6, 9, 11.
    Conclusion: no one of these statistics is sharp on all the families; the right statistic depends on the
    function (size for threshold-like, the clause projection for DNF-like). Nothing here is a proof.

 3. A coordinate can be as bad as the trivial bound allows (worker FEIB27, PROOFS section 1, read in full; my
    sep_stat run computed the same family independently). b = the quadratic bent function on k (even) variables,
    f(x, y) = b(y) except that x flips the value at one point y_0. Then Inf_x = 2^-k, hhat(T)^2 = 4^-k for every
    T, and p_T/q_T takes the two values (2^(k/2) -+ 1)^2, so
        E_x/Inf_x = k + log2(e) - o(1)     (9.4286, 11.4392, 13.4418 at k = 8, 10, 12),
    against the trivial E_i <= h2(Inf_i) = Inf_i (log2(1/Inf_i) + log2(e) - o(1)). The other coordinates have
    ratio about 2, so the minimum stays 2; with several hidden coordinates all of them are equally bad (9.3764
    with four at k = 8) and the bent coordinates still pay. Consequence (FEIB27): no per-coordinate bound
    E_i <= sum_k c_k t_k(f, i) with terms t_k <= Inf_i exists, for any fixed dictionary of such terms; a proof
    must choose the coordinate. 12(u) is the monotone instance with growth (1/2) log2(1/Inf).

 4. Transitive towers (worker FEIB26; formula re-derived and values recomputed by me, code/tower_audit.py).
    For f = F(psi, ..., psi) with the same psi in each of the k blocks, i in block 1, c = psihat(empty),
    t = 1 - c^2, a = psihat({i})^2, K_A(c) = sum_{B >= A} Fhat(B) c^{|B - A|}:
        mu_f(S) = K_A(c)^2 prod_{j in A} mu_psi(S_j)          (A = the blocks S meets),
        E_i(f)   = sum_{A' <= {2..k}} t^{|A'|} [ Phi(K_{A'}^2, K_{A'+1}^2 a) + K_{A'+1}^2 (E_i(psi) - Phi(c^2, a)) ],
        Inf_i(f) = Inf_i(psi) sum_{A'} t^{|A'|} K_{A'+1}^2 .
    (Phi is homogeneous of degree one, so the blocks other than block 1 sum out; the empty pair of psi is the only
    pair that changes shape.) Checked against a direct transform on six random pairs (F on 3 or 4 variables, psi on
    3): worst error 6e-17.
    F = "the chosen edges of K_{3,3} contain a perfect matching" (9 variables, transitive, mean 0.0352,
    E_i/Inf_i = 2.6293). Self-towers F^(r), all coordinates equivalent, so G = E_1/Inf_1 = sum_i E_i / I:
        depth  1        2        3        4        5        6        7        8
        G      2.6293   4.0481   4.4168   4.4713   4.47500  4.47419  4.47415  4.47415
    My values agree with the worker's (4.048135961762, 4.474995805835, limit 4.474150253077) to twelve digits.
    The mean drifts to 1 (0.035, 0.105, 0.243, 0.491, 0.823, 0.992, ...), so deep levels are nearly constant
    functions with tiny influences; the ratio converges all the same.
    So  G* >= 4.47499  and  A* >= 4.47499  (depth five, 59,049 variables), up from 3.7137. The bracket of 12(w)
    item 1 with C* >= 6.5218 gave only G* >= 3.636. Since G* <= C*, a transitive tower above 6.5218 would raise
    the lower bound for the FEI constant itself; none is known. The worker also proves that the limit exists for
    every transitive base and gives a tail bound; that part I have read but not re-derived.
    Next: search over transitive bases (cyclically invariant F on 9-15 variables) for the largest tower value;
    the recursion costs 3^k per level, so each candidate is cheap.
    UPDATE (10 Nov 09:40-10:00): the best explicit value is 4.50505, not 4.47499. Replacing a gate F by -F sends
    K_A to -K_A, so the only change in the recursion is the sign of the level mean c; a tower of -f is therefore
    not the tower of f, and the gate signs are a free choice at every level. With M = F above and N = -M
    (worker FEIB26's final report): seven gates N, M, N, M, N, M, N from the bottom (4,782,969 variables) give
    4.50504996749762 < G < 4.50504996749764 (its interval certificate); my float recursion gives 4.50504996749320
    (code/sym_enum.py, pattern "mp", depth 7). The four period-two sign patterns of this base (code/sym_deep.py,
    depth cap 512): f,f,... 4.474995805836 (depth 5); -f,-f,... 4.501652448360 (depth 6); -f,f,-f,...
    4.505049967493 (depth 7); f,-f,f,... 4.485667289781 (depth 6). So G* >= 4.50504 and A* >= 4.50504.
    The worker's census of all transitive functions through seven variables has best self-tower limit 4.13707
    (its figure). Exhaustive enumeration of all 2^25 functions invariant under Aut(K_{3,3}) on the nine edges,
    under the four patterns, is running (code/sym_enum.py); results go into 12(z).

 5. Round 8, state at 09:22 (workers FEIB26, FEIB27, FEIB28 on Mac mini 1, still running).
    FEIB28 (referee): report read in full. FEIB23 A-G, FEIB24 1-10, FEIB25 1-9 and its paper: every proof
    confirmed (remaining gaps are only that the 8-variable and full monotone censuses were not rerun
    independently; FEIB25 section 5 is conditional on Corollary 6.7 of Kelman et al. and is not a new FEI class).
    This closes the reading owed in 12(w) item 7. On 12(v)/12(w): items 1, 2, 3(a), 3(b), 3(d), 5 of 12(v) and
    items 2, 4, 5, 6 of 12(w) confirmed; the errors found are corrected in place (3(c) proof, 3(e) wording, the
    empty-set case of item 4, three statements of 12(w) item 3, priority in 12(w) item 2).
    FEIB27 (which local terms could pay for a step): besides item 3, it proves that every term of the brief's
    dictionary except Inf_i and B_i = sum_{S containing i, |S| >= 2} mu(S) sums to O(Var), so cannot bound
    sum_i E_i (tribes with m = (ln 2) 2^w clauses of width w has sum_i E_i growing like I); that
    sum_S mu(S) log2(1+|S|) is O(I) (my brief said otherwise; wrong); and, on an OR of disjoint 2-clauses (five clauses: settled 22:3x
    by code/or2_check.py, D_i/Inf_i = 5.7825 at k = 5 clauses and 6.0037 at k = 8; its PROOFS' "eight" is a slip),
    that (E_i + J_i)/Inf_i = 5.7825 at every coordinate while each of its eight potentials has drop at most its
    budget times Inf_i, so within that span the zero potential is optimal on that function. Its section 5 agrees
    with the referee: a bad coordinate does not exclude a best-coordinate supersolution.
    The one direction it leaves standing, as a question only: sum_i E_i <= C (I - W_1), W_1 = sum_i fhat({i})^2.

### 12(z) (10 Nov 10:05-10:33) K33 enumeration complete in the pp pattern; power form refuted; the predictor (pseudo-likelihood) form; the tilted-excess identity; FEIB27's verdicts

Notation as in 12(y): mu(S) = fhat(S)^2, U ~ mu, I = E|U|, Q(T,i) = mu(T+i)/I on pairs with i not in T,
L = E_Q log2(1 + mu(T)/mu(T+i)) = sum_i Inf_i Lam_i / I, and FEI <=> L <= C.
up_lam(T) = sum_{U >= T} mu(U) lam^|U-T| = ||T_sqrt(lam) D_T f||^2; up_1 = up, up_0 = mu.

1. Exhaustive K33 enumeration, pp pattern: DONE (computed exactly by code/sym_enum.py, float64; four lanes of
   8,388,608 functions; all 2^25 functions invariant under the 72-element group of K33 acting on its 9 edges).
   The largest self-tower limit of min_i E_i/Inf_i is 4.474995805836, attained only by PM(K33) and its three
   relatives (function numbers 33546240, 33552384, 31102532, 31364804). Next: 4.392562759838 (8191, 2451899),
   4.367309548521, 4.363110902692. Depth-one maximum 2.673971278743 (19229115, 16779263; PM(K33) has 2.629252962712).
   Chains (pp): cube groups q3v and k24 (8 variables, 2^21 functions each) best tower 3.958574785035, depth-one
   3.042836845650; s3ws3 (9 variables) 3.385374328825 and 2.844174435061; s2ws5 (10 variables) 3.791693271987 and
   3.389192093442 (biased functions; their towers fall). So within these groups nothing beats PM(K33), and the best
   explicit value stays the alternating tower's 4.50505 (12(y) item 4 UPDATE). The mm, mp, pm patterns are running.

2. Power form refuted (code/power_form.py). S_i = sum_{U containing i} |fhat(U)||fhat(U-i)|. A bound
   sum_i S_i <= C I would imply FEI, since log2(1+x) <= (2/(e ln 2)) sqrt(x). For f = F(psi,...,psi), psi balanced,
   r_i = S_i/Inf_i obeys r(f) = r_i(psi) + (|psihat({i})|/Inf_i(psi)) r_b(F), and |psihat({i})| = Inf_i(psi) for
   monotone psi. On a balanced monotone 4-variable base composed with itself the formula holds to rounding and
   sum_i S_i / I doubles (0.666667 -> 1.333333). So r grows linearly in depth: no Cauchy-Schwarz / L1-L2 route can
   prove FEI. The logarithm is essential.

3. The predictor form (PROVED, two lines). For ANY p_i(T) >= 0 put
       K = (1/I) sum_i sum_{T without i} (mu(T) + mu(T+i)) p_i(T).
   Then  L <= log2 K + E_Q log2(1/p_i(T)),  with equality at p_i(T) = mu(T+i)/(mu(T)+mu(T+i)).
   Proof: R(T,i) = (mu(T)+mu(T+i)) p_i(T)/(K I) is a probability law on pairs; Gibbs' inequality E_Q log(Q/R) >= 0.
   So FEI <=> there are predictors of a deleted element of the spectral sample whose total predicted count is at
   most K E|U| and whose log-loss is at most C per element. This is a pseudo-likelihood statement: FEI asks for a
   bounded-cost conditional model of one element given the rest, not for a model of the whole sample.
   Sufficient special case (closure maps): a map N on sets with E|N(U)| <= K E|U| and
   E sum_{i in U} 1[i not in N(U-i)] log(1/Inf_i) <= C E|U| gives FEI (predictor (Inf_i + 1[i in N(T)])/2). Tribes:
   N = the tribe-mates of T. Majority needs a soft predictor (density |T|/n), so hard closure maps are not enough.

4. Predictors from noisy derivative norms. r = up_lam(T+i)/up_lam(T); "ratio" p = min(1,r), "thin"
   p = (1-lam) r/(1+(1-lam) r), "lrat" p = lam r (always <= 1, since up_lam(T) >= lam up_lam(T+i)).
   MEASURED (code/predictor.py, exact transforms, float64; code/predictor_out.txt), bound against exact L:
   AND n=14 1.004 vs 1.0031; tribes 2x6 2.358 vs 2.3516; tribes 3x4 1.44 vs 1.3903; PM(K33) 1.789 vs 1.6733;
   address k=3 0.76 vs 0.6000; random n=10 0.72 vs 0.55; MAJ3 of MAJ3 0.54 vs 0. Majority (exact L = 0), by the
   closed form of its spectrum (code/predictor_sym.py, log domain): best overhead 0.22, 0.29, 0.37, 0.97, 1.45, 1.72
   bits at n = 5, 9, 13, 51, 201, 801 (thin, lam = 0.1) - increments shrinking. HEURISTIC: with W_k ~ k^(-3/2) the
   predictor is about (k+1)/((1-lam) n) and the cost is (1/I) sum_k k^(-1/2) log(n/k) -> 2 nats, so the overhead
   converges to a constant of a few bits. No family tried breaks the predictor.
   For lrat: sum_{i not in T} p_i(T) = m_lam(T) := E|U-T| for U drawn from supersets of T with weight
   mu(U) lam^|U-T|, so  K <= 1 + E_{T~mu} m_lam(T) / I,  and
   cost = log2(1/lam) + (1/I) E_{U~mu} sum_{i in U} [log2 up_lam(U-i) - log2 up_lam(U)].
   Composition law (PROVED): for f = F(psi,...,psi), psi balanced, T with blocks T_j and J = {j : T_j nonempty},
       up_lam^f(T) = up_theta^F(J) prod_{j in J} up_lam^psi(T_j),   theta = up_lam^psi(empty) = sum_S mu_psi(S) lam^|S|.
   The tilt contracts up the tower (theta <= lam W-weighted), which is why towers stay bounded: an element whose
   deletion empties l nested blocks costs about l log(1/W_1(psi)) + log(1/lam) and has frequency (W_1/I)^l.

5. The tilted-excess identity (PROVED). d/d(ln lam) ln up_lam(T) = m_lam(T), and up_0 = mu. Hence
       B := E_mu log2(up(S)/mu(S)) = (1/ln 2) int_0^1 E_{T~mu} m_t(T) dt/t,
   and with Lemma 2 (H <= E_mu log2(1/up_lam) + I log2(1/(1-lam)); (1-lam)^|S| up_lam(S) is a probability law) and
   the granularity bound A := E_mu log2(1/up) <= H/2 + I (for S nonempty mu(S) <= 4^(|S|-1) up(S)^2, as D_S f is a
   multiple of 2^(1-|S|); for S empty up = 1):
       H/2 <= I (1 + log2(1/(1-lam))) + (1/ln 2) int_lam^1 E_{T~mu} m_t(T) dt/t        for every lam in (0,1).
   So FEI <=> int_{1/2}^1 E_{T~mu} m_t(T) dt <= C I. In words: draw T from the spectral sample, then redraw a
   superset with penalty t per extra element; the expected number of extra elements, integrated over t in [1/2,1],
   is O(E|T|). NECESSARY for FEI: E_{T~mu} m_t(T) <= C_t I for each fixed t < 1 (m_t is nondecreasing in t).
   SUFFICIENT: E_mu m_t <= C I (1-t)^(-a) with a < 1. Values: AND and random functions t/(1+t); majority about
   t/(1-t) until 1-t ~ |T|/n (the log singularity integrates to |T| log(n/|T|), which averages to O(I)).
   A measure (not a Boolean spectrum) built from "all I/2-subsets of sets of size sI" would have
   E m_t / I ~ s at 1-t ~ (ln s)/s, a log^2 divergence; Boolean-ness has to forbid rich containment of typical
   small sets in many much larger ones. This is the same wall as B <= C I (largest B/I seen 1.5108), seen as a
   statement about one tilted resampling step. No novelty claimed; not yet checked against the literature.

6. FEIB27 (round 8, ended; REPORT read). (a) PROVED there: E_i <= B_i [2 + log2 e + log2(1 + A_i/B_i)] with
   B_i = Inf_i - fhat({i})^2, A_i = Var - Inf_i. (b) Every local (per-coordinate) bound in its dictionary is
   refuted by the hidden-bent family (ratio k + log2 e). (c) Summed bounds: everything except Inf_i and B_i sums to
   O(Var) and fails on tribes; the surviving SUMMED candidate is the B-direction
       sum_i E_i <= C (I - W_1),   census optimum C about 4.094 (33.6 million functions, 172.6 million coordinates).
   (d) The best-coordinate candidate min_i E_{rho_h}[log2(p/q)]_+ <= 2 is unbroken (largest seen 1.863061). The
   half-mass candidates at p <= q and p <= 4q are DISPROVED (the latter by a transitive function: OR of nine
   disjoint pairs plus the two transversal clauses, mass 429970409/859963392 < 1/2). (e) The witness for the
   supersolution obstruction is the OR of EIGHT disjoint 2-clauses (ratio 6.0037460565590882514); this settles the
   five-versus-eight question of 12(y). (f) Correction to my brief, already noted in 12(y): sum_S mu(S) log2(1+|S|)
   is O(I).
   My check of the B-direction on a near-dictator (f = x_1 except on an AND-set of measure eps, where f = +1):
   sum_i E_i about 2 eps k, I - W_1 about eps k: ratio about 2. A counterexample would need level-1 weight spread
   over many coordinates with I - W_1 small, which KKL/FKN-type facts forbid.

7. Targets for round 9: (i) the B-direction, prove or break; (ii) adversarial search against the predictor bound
   and the necessary condition E_mu m_t <= C_t I; (iii) monotone good coordinate (for monotone f: h = 1_B and, for
   T nonempty, ghat = a - b, hhat = -(a + b) with a, b the transforms of the up-set forced to +1 and the down-set
   forced to -1).

### 12(aa) (10 Nov 10:45-10:58) Thinning reading of the predictor; fixed-t form; four dead ends; the A functional

Notation as in 12(z): mu(S) = fhat(S)^2, U ~ mu, I = E|U|, up_t(T) = sum_{U >= T} mu(U) t^|U-T|, up = up_1,
m_t(T) = t sum_{i not in T} up_t(T+i)/up_t(T), H = A + B with A = E_mu log2(1/up(S)), B = E_mu log2(up(S)/mu(S)).

1. **Thinning.** nu_t(T) = (1-t)^|T| up_t(T) is the law of U after each element is deleted independently with
   probability t. The "thin" predictor of 12(z) item 4 is nu_t's own conditional law of one more element.
   m_t(T) = sum_{U >= T} |U-T| mu(U) t^|U-T| / up_t(T) is the posterior mean number of deleted elements given the
   thinned sample T. Averaged over thinned samples it is exact:
       E_{T ~ nu_t} m_t(T) = t sum_T sum_{i not in T} (1-t)^|T| up_t(T+i) = (t/(1-t)) E_{nu_t}|T| = t I.
   FEI (12(z) item 5) asks for the same posterior mean averaged over unthinned samples T ~ mu, integrated over
   t in (1/2, 1), to be O(I).

2. **Fixed-t form.** For any fixed t in (0,1):  FEI  <=>  E_{S ~ mu} log2(1/up_t(S)) <= C_t I.
   (=>) up_t >= mu, so the left side is at most H. (<=) Gibbs against nu_t: H <= E_mu log2(1/nu_t(S))
   = E_mu log2(1/up_t(S)) + I log2(1/(1-t)). Since up_t(S) = ||T_sqrt(t) D_S f||^2, FEI says that the noisy derivative
   along a mu-typical set S has norm at least 2^(-C|S|) on average in the logarithm. Unconditionally
   D(mu || nu_t) <= I log2(1/(1-t)), so the cross-entropy against the thinned law is H up to O(I): this form is
   H again, with the tilt as a free parameter. It is a restatement.

3. **Dead ends, so they are not tried again.**
   (a) Change of measure mu(T)/nu_t(T) <= (1-t)^(-|T|) gives E_mu m_t <= (1-t)^(-d) t I for degree-d functions only.
   (b) Jensen in the tilt, up_t(S) >= up_1(S) t^(m_1(S)), needs E_mu m_1, which is of order n for majority.
   (c) The crude bound E_mu m_t <= t E[|U| (1+t)^(|U|-1)] is an exponential moment of |U|.
   (d) AM-GM on up(T+i)/up(T) leads back to the power form, refuted in 12(z) item 2.

4. **The A functional.** A <= H, A <= H/2 + I (granularity: mu(S) <= 4^(|S|-1) up(S)^2), A <= B + 2I - 2Var.
   So "A <= C I" follows from FEI. It is not an easier statement in general:
   - if the spectrum sits on one level then up = mu on the support and A = H; so "A <= C I" contains FEI for
     functions with homogeneous spectrum (example: f = x1 x2 if x2 = x3 else x2 x4, four coefficients 1/2 on
     level 2, A = H = I = 2);
   - level-one part is unconditional: fhat(i)^2 <= Inf_i^2 gives sum_i fhat(i)^2 log2(1/Inf_i) <= I/(e ln 2);
   - higher levels by granularity alone need E 5^|U|, an exponential moment.
   Tower law (from the composition law of 12(z) at t = 1, theta = 1 for balanced psi):
       A(F(psi,...,psi)) = A(F) + I(F) A(psi),   so the tower limit of A/I is A(psi)/(I(psi) - 1),
   the same shape as for H. Checked exactly (code/a_form.py, a_form_out.txt): maj3(maj3) 3.125 = 1.25 + 1.5 x 1.25;
   maj3(hom) 4.25.
   Measured split of H/I into A/I + B/I (computed exactly by code/a_form.py):
       majority 3, 5, 9, 13:  A/I 0.833, 0.966, 0.976, 0.937;  B/I 0.500, 0.807, 1.161, 1.365
       AND 4: 1.94 + 1.46;  tribes 3x4: 2.04 + 1.08;  PM(K33): 2.09 + 1.15.   AND_n: A/I -> 3, B/I -> 1 (closed form).
   Reading: on majority A/I stays near 1 and the growth of H/I is all in B; on AND, tribes and PM(K33) A carries
   two thirds. The two halves are hard on different families (A on antichain-like spectra, B on nested ones).

5. Search added: code/ov_hill.py (truth-table hill-climb against the thinning predictor: objectives overhead,
   full bound, E_mu m_t / I, exact L), two lanes at n = 11 on Mac mini 2 from 10:54. A bounded "mt" at fixed t is
   necessary for FEI; an unbounded one found by search would be a counterexample candidate and gets recomputed
   independently before anything is said about it.

### 12(bb) (10 Nov 11:10-11:15) Round 9, first two reports: the B-direction is FEI again; the thinning predictor holds

Workers FEIB29 and FEIB30 (Mac mini 1, Codex) finished 13:05-13:07 Mac clock. Both REPORT.md files read whole.

1. **B-direction (FEIB29): equivalent to FEI, so not an easier target.** The proof, re-derived here:
   multiplying f by a character chi_R translates the spectrum by R, so every E_i is unchanged, while
   Inf_i(chi_R f) = 1 - Inf_i(f) for i in R. Hence min_R I(chi_R f) = sum_i min(p_i, 1 - p_i), p_i = Inf_i. Since
   |fhat({i})| <= p_i, B_i = p_i - fhat({i})^2 >= p_i(1 - p_i) >= (1/2) min(p_i, 1 - p_i). So
       sum_i E_i(f) = sum_i E_i(chi_R f) <= K_E I(chi_R f) <= 2 K_E (I - W_1),
   and the converse is I - W_1 <= I. (The comparison min_R I(chi_R f) <= 2(I - W_1) is Lemma 2.2 of the symmetric-FEI
   paper, arXiv:2610.16069; no novelty.) Consequences recorded:
   - FEI <=> sum_i E_i <= C sum_i min(Inf_i, 1 - Inf_i): the erasure form is invariant under character translation,
     and only the translation-invariant part of the influence pays.
   - Near a dictator the constant does not improve: the supremum of sum E_i / (I - W_1) at distance delta tends to
     K_E as delta -> 0 (worker's proof by rare activation of a tensor power; PROOFS.md, not re-derived by me).
   - The census value 4.094 was only a census value: the worker reports 4.1601 on a stored 14-variable read-once
     formula and 4.50523 on the depth-six alternating PM(K33) tower (its numbers, interval-certified by its own
     scripts; the tower figure matches the 4.50505 of 12(z) item 1 in the other denominator; not recomputed here).
   - Proved by the worker for classes (constants loose, all by known theorems): symmetric (24.08), read-once with
     gate arity k, depth-d trees 4(d-1) + 2/ln 2.
   Verdict: the "surviving summed candidate" of 12(z) item 6 is FEI itself up to a factor 2. Closed as a separate lead.

2. **Thinning predictor (FEIB30): conjecture P unbroken; overhead is at most about 2.5 bits everywhere tested.**
   - Overhead = D_KL(Q || R) exactly, with R(T,i) = (mu(T) + mu(T+i)) p_i(T) / (I K). (Q is the size-biased law:
     draw U with probability |U| mu(U)/I, delete a uniform element. The prose of my brief said "draw U from mu"; the
     displayed formula Q(T,i) = mu(T+i)/I, used in 12(z) and in all code, is the right one.)
   - The composition law of 12(z) holds for balanced inner functions only. For biased inner functions (AND, tribes,
     PM(K33)) the outer polynomial is re-expanded at the inner mean. The worker's recurrence does this; my
     code/predictor.py compose() is used on balanced inner gates only, so no figure of 12(z)/12(aa) changes, but the
     statement there needed the word "balanced" (it has it in 12(aa) item 4).
   - Majority: under the size-biased spectrum |U|/n tends to the arcsine law; thin predictor's limit overhead is
     2.0007, 2.0074, 2.0520 bits at lam = 0.1, 0.25, 0.5 (proved formulas, numerically evaluated; L = 0 since
     majority is odd, so every E_i vanishes). My "two nats" heuristic was wrong; it is two bits.
   - Fixed balanced self-towers: overhead converges (proved, constants depend on the base). Depth-six values at
     lam 0.1: PM(K33) 0.012, tribes 0.003, AND/OR 0.003, MAJ3 0.48. On every hard example (large L) the thin
     predictor is within 0.1 bit of exact; the overhead is largest where L = 0.
   - Search: 525 hill-climbs, n = 8..12, largest overhead 1.198; largest full bound in the whole pool 3.3804 bits
     (PM(K33) depth five), where L = 3.2320.
   Reading: P (sup_f Ov < infinity) is plausible with a constant near 2 bits. P is not FEI: it says the thinning
   predictor is nearly optimal, so FEI <=> its cost is bounded:
       FEI  <=>  E_{S ~ size-biased mu} avg_{i in S} log2(1 + up_t(S-i) / ((1-t) up_t(S))) <= C     (given P).
   My two n = 11 lanes on Mac mini 2 duplicate this search; they run to their cap and are read once.

3. **One identity from the afternoon's own work (exact, three lines).** Let Q(T,i) = mu(T+i)/I and pi its T-marginal.
   Then
       E_Q log2( mu(T) / mu(T+i) ) = H_Q(i | T) - log2 I - D(pi || mu).
   Proof: E_Q log(1/mu(T+i)) = H(size-biased mu) + D(size-biased || mu) and D(size-biased || mu) = E log|S| - log I;
   E_Q log(1/mu(T)) = H(pi) + D(pi || mu); and H(size-biased) + E log|S| = H_Q(T,i) = H(pi) + H_Q(i|T).
   FEI is the statement E_Q [log2(mu(T)/mu(T+i))]_+ <= C (the positive part, within one bit of L). The signed
   version is weaker (D(pi || mu) is infinite for majority). What is missing is the part
   E_Q [log2(mu(T+i)/mu(T))]_+ : mass-increasing up-moves, weighted by the upper mass.
   Checked exactly (code/q_identity.py, q_identity_out.txt): the two sides agree to 1e-15 on AND 4, AND 8,
   tribes 2x3, tribes 3x4, PM(K33). Values (positive part down / positive part up / signed), bits per unit of I:
   AND 4: 0.702 / 0 / 0.702; tribes 3x4: 0.477 / 0 / 0.477; tribes 2x3: 0.693 / 0.477 / 0.216;
   PM(K33): 1.342 / 1.320 / 0.022. On PM(K33) the two parts nearly cancel: H_Q(i|T) = 2.587, log2 I = 1.003,
   D(pi || mu) = 1.562.
   Status: identity only; no bound follows yet.
   Addendum (10 Nov 20:1x, an agent; NEXT (4)(a) closed, negative). The up-move part is not a target on its
   own. It is finite exactly when supp(mu) is closed under deleting one element (U in supp, i in U => U - i in supp),
   and the same condition decides whether D(pi || mu) is finite. For an odd f (f(-x) = -f(x)) the spectrum sits on odd
   sets, so mu(U - i) = 0 for every U in supp: every move is an up-move, the up part and D(pi || mu) are both +infinity,
   and every E_i = 0. Majority on three bits already shows it: mu({1}) = mu({2}) = mu({3}) = mu({1,2,3}) = 1/4.
   Subtracting the two infinite terms first gives nothing new: on an up-move the combined integrand
   [log2(mu(T+i)/mu(T))]_+ - log2(pi(T)/mu(T)) equals log2 I + log2 Q(i|T), on a down-move it equals
   log2(I mu(T) / sum_j mu(T+j)), and putting these into the identity returns E_Q [log2(mu(T)/mu(T+i))]_+ term by
   term. So item 3 is a rewriting of the positive part, and any bound has to be on the down part directly.

### 12(cc) (10 Nov 20:4x-20:5x, an agent; NEXT (4)(c)) Power weights die for every a != 0, monotone f included

FEIB31 (PROOFS.md (5.3)) asks whether some a gives a universal C with

    sum_i Inf_i^a E_i <= C sum_i Inf_i^(a+1)                                   (W_a)

on monotone f, rules out a < 0 (layered hidden bits) and a > 1 (one hidden bit, balanced-majority substitution), and
leaves 0 <= a <= 1 open. The interval (0, 1] is ruled out too: substitute tribes, not majority.

1. **Biased substitution lemma (exact; the same identity is FEIB26 PROOFS section 2, "Unbalanced-inner composition", workers_r8/FEIB26).** Let f be Boolean on (x, y_1..y_k) and F = f(x, phi(z^1), ..., phi(z^k)) with
   phi monotone on fresh blocks, p = P(phi = 1), mu = 2p - 1. Writing y_j = mu + sum_{B != 0} phihat(B) chi_B(z^j),
   Fhat(S) = gtilde(A) prod_{j in A} phihat(S_j) with A the set of blocks S meets and gtilde(A) = sum_{A' >= A}
   fhat(A') mu^|A' - A|; summing prod phihat(S_j)^2 over the S with block set A gives (1 - mu^2)^|A|. Since
   Phi(a, b) = (a + b) h2(b / (a + b)) is homogeneous, E_x(F) and Inf_x(F) are E_x and Inf_x of f computed in the
   p-biased orthonormal basis on y (x uniform). Balanced phi (mu = 0) is 12(u) item 2. A leaf v of block j has
   Inf_v(F) = P_p(y_j pivotal for f) Inf_v(phi). Checked against full truth tables (19 variables, k = 3, tribes
   (2,2), (2,3), (3,2)): E_x, Inf_x and a leaf influence agree to 12 digits (code/wa_tribes.py, wa_tribes2.py).
2. **No-go for 0 < a <= 1.** Take f_k = MAJ_k(y) OR (x AND [y >= y0]) of 12(u), ratio r_k = E_x/Inf_x unbounded in k
   (FEIB31 Sections 4-5; 3.523, 4.989, 6.618, 8.369 at k = 3, 7, 11, 15). Substitute Ben-Or-Linial tribes of width w,
   s = round(2^w ln 2) terms: p_w -> 1/2, every leaf influence is 2^-(w-1)(1 - 2^-w)^(s-1) <= 2^-(w-1), and the
   leaf count is w s < w 2^w. The leaves' share of the right side is at most
   k w 2^w 2^(-(w-1)(1+a)) = 2^(1+a) k w 2^(-a w) -> 0 for every a > 0, while E_x(F), Inf_x(F) -> E_x, Inf_x of f_k by
   item 1 and continuity in p. The left side is at least Inf_x(F)^a E_x(F) (all terms are nonnegative). So the
   quotient in (W_a) tends to r_k as w -> infinity; then let k -> infinity. Majority substitution fails for a <= 1
   only because MAJ_m spreads influence with total sqrt(m); tribes keeps the total at O(w) = O(log n).
   Numbers (lower bound on the quotient, code/wa_tribes_out.txt): k = 15, r = 8.3685: a = 0.25 gives 8.21 at w = 128,
   a = 0.1 gives 8.3685 at w = 512, a = 0.05 gives 3.95 at w = 512; at a = 0 the bound falls with w (0.0096 at
   k = 3, w = 48), as it must, since the leaves' share there is k s w 2^-(w-1) ~ k w ln 2, growing.
3. **Reading.** Among power weights Inf_i^(1+a) only a = 0 survives, and (W_0) is A* < infinity, FEI within 2/ln 2
   (12(w) item 1). [corrected 21:3x, see 12(dd): this holds only for g(Inf_i) with g(t) log(1/t) -> 0] Any weighted good-coordinate statement has to use weights that are not a function of Inf_i alone
   (the hidden coordinate's influence is the same in f_k and in F, while the base influences can be made as small and
   as numerous as we like at bounded total). Status: proved here, exact checks above; no referee yet.

### 12(dd) (10 Nov 21:3x, an agent; NEXT (4)(c)) Where the tribes no-go stops: Talagrand's weight

12(cc) item 3 said more than item 2 proves. Take a general positive continuous weight g on (0, 1] and

    sum_i g(Inf_i) E_i <= C sum_i g(Inf_i) Inf_i.                                (W_g)

1. **The no-go reaches every g with g(t) log(1/t) -> 0 as t -> 0.** Same construction as 12(cc) item 2. As w -> infinity
   a leaf of block j has influence P_j 2^-w (1 + o(1)), with P_j = P(y_j pivotal for f_k) at p = 1/2, and there are
   w 2^w ln 2 (1 + o(1)) leaves per block, so the leaves' weighted total is ln 2 * w * sum_j P_j g(P_j 2^-w) (1 + o(1)).
   This tends to 0 exactly when w g(c 2^-w) -> 0, i.e. g(t) = o(1/log(1/t)), and then the quotient tends to r_k.
   Power weights (a > 0) are the case g(t) = t^a.
2. **It stops at g(t) = 1/log(1/t), and must.** Talagrand's inequality Var f <= C sum_i Inf_i / (1 + log(1/Inf_i))
   makes the right side of (W_g) at least c Var(F) for every g >= 1/(1 + log(1/t)), however the influences are spread, so
   no substitution can make the hidden coordinate dominate. Checked (code/wg_tribes.py, g = log2(1/t)^-b, w up to 2^40):
   b = 2 reaches r_k (4.2427 at k = 5, 5.7834 at k = 9), b = 1.5 approaches it slowly (4.2408, 5.6563 at w = 2^40), b = 1
   stays flat (0.0206 at k = 5, 0.0007 at k = 9, every w), b = 0.5 tends to 0.
3. **What is still open.** (W_g) for g between Talagrand's weight and the constant (g(t) = log(1/t)^-b, 0 <= b <= 1;
   b = 0 is A*). Elementary upper bound, for the record: E_i <= Inf_i (log2(1/Inf_i) + 1/ln 2) (Jensen on the c_T log((a_T +
   c_T)/c_T) part of Phi), so the left side of (W_g) at b = 1 is at most (1/ln 2) I. A counterexample at b = 1 needs many hidden
   coordinates with E_i/Inf_i of order log(1/Inf_i) and total influence large against the rest's Talagrand sum; none known.
   Status: items 1-2 proved here (item 2 is Talagrand plus the arithmetic), exact checks above; no referee yet.
4. **Why the open window is hard.** (i) For transitive f every Inf_i is equal, so every (W_g) says exactly G(f) <= C: any
   weighted statement of this kind implies sup over transitive f of G(f) < infinity (which FEI implies, and nothing weaker
   is known to). Weights help only on nontransitive f. (ii) For b <= 1 substitution never lowers the right side: a tribes
   block under y_j contributes about ln 2 * w^(1-b) * Inf_{y_j}, at least ln 2 * Inf_{y_j} against Inf_{y_j}/log(1/Inf_{y_j})
   before. So a counterexample at 0 < b <= 1 must come from the base function itself, not from dilution, and the
   reduction trick of 12(cc) has nothing more to give. Next useful move: a direct construction with many hidden
   coordinates carrying most of the influence, or a proof of (W_g) at b = 1 from the tree accounting of 12(u) item 5.
5. **A necessary shape for a counterexample at b = 1** (heuristic accounting, not a theorem). Call coordinates with
   E_i >= theta Inf_i L_i (L_i = log2(1/Inf_i), theta fixed) heavy. For the quotient to be large, the heavy coordinates'
   Talagrand sum, about I_heavy/L, must dominate the whole right side, which Talagrand keeps >= c Var; so I_heavy >~ L. If
   FEI holds (A* < infinity), sum E_i >= theta L I_heavy forces I_heavy <= (A*/theta) I / L, so I >~ L^2: the rest of the
   function must carry influence of order L^2 at Talagrand cost below I_heavy/L, i.e. at leaf influences far below the
   heavy ones (L_rest >~ L^3). FEI neither rules this out nor produces it; this is a different question from A*.
   Small-function scan (code/wq_scan.py, g = (1 + log2(1/t))^-b): all 65,536 functions on 4 variables, max Q0 = 2.7042,
   max Q1 = 2.6725, max Q1/Q0 = 1.359; random monotone n = 6, 8, 10: max Q1 3.0581-3.1064, always below max Q0
   (3.0310-3.1611). Nothing in small f makes the Talagrand weight worse than the plain A* quotient.

### 12(ee) (10 Nov 21:5x, an agent; NEXT (5)) The two unread papers for 11's items 3(b)-(d), read

Wan, Wright and Wu (arXiv:1312.3003, ar5iv theorem list read): Theorem 1.1 H <= 9k I for read-k decision trees; Theorem 1.2
H <= 12 d I for expected depth d when I >= 1 (Appendix E: the I >= 1 hypothesis is needed unless FEI is proved); Theorem 1.6 a
ternary protocol of length min{(2k+2) I, 4 I + 2 d}; Theorems 1.3/1.12-1.13 a protocol proof of O'Donnell-Tan's composition
theorem. Chakraborty, Kulkarni, Lokam and Saurabh (ECCC TR13-052, full text read): Theorem 4.13 H <= 2 d(f), d(f) the minimum
average depth; H = O(log L) for L-leaf trees (their (7)), with the remark that O(log #DNF terms) would give Mansour's
conjecture; Corollary 4.4 H = O(D(f)), O(deg f); Theorem 5.5 balanced LTFs; Corollary 5.14 H <= 10 I for read-once formulas.
Neither paper has a width-w or m-term DNF bound of the form H <= c(w) I, nor a bound multiplicative in I with log log s or
log(1 + d). Verdict for 11 item 3: (b) width-w DNF H <= (w + 7.94) I and (c) m-term DNF H <= (6.94 + log2(1 + 4m)) I are not in
these papers or in Shalev / KKLMS (read 10 Nov 11:0x); (d) depth form is KKLMS Theorem 1.3 up to the constant; the s-leaf
form (6.94 + log2(1 + log2 s)) I is incomparable to CKLS's additive O(log s) and stronger when I << log s / log log s. Still
owed before calling (b)-(c) new: Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf arXiv:1809.09819 theorem statements (only
the abstract has been read) and a search for "entropy influence DNF width". Note (c) gives O(log^2 m) for m-term DNFs via
I = O(log m), not Mansour's O(log m).

### 12(ff) (10 Nov 22:0x, an agent; closes NEXT (5)) The last paper for 11 item 3, and the prior work on Talagrand's weight

1. **Arunachalam, Chakraborty, Koucky, Saurabh, de Wolf, arXiv:1809.09819** ("Improved bounds on Fourier entropy and
   min-entropy"). Statements, from the abstract: H_inf <= 2 C_min^xor(f); H_inf <= 2 log(||fhat||_{1,eps}/(1-eps)), so FMEI
   holds for read-k DNF with k constant; H <= 2 aUC^xor(f) (average unambiguous parity certificate complexity, improving
   CKLS); and the weak form H <= C min{C^0(f), C^1(f)} already implies Mansour's conjecture.
   Against 11 item 3: aUC^xor does not give (b). For tribes of width w a 0-input needs a certificate touching every block,
   and P[f = 0] is about 1/2, so aUC^xor is of order 2^w while (b) gives O(w I) = O(w^2). Their weak form, specialised to
   a width-w DNF (C^1 <= w), asks H <= C w. (b) is the influence-weighted relative of it: H <= (C^1 + 7.94) I. That does
   not reach their question, since I can be as large as about w.
2. **Lecomte and Tan, arXiv:2109.04525** (FOCS 2021): Fourier concentration of size-s DNF on s^{O(log log k)}
   coefficients, k the read number. A concentration statement with no entropy-influence bound. It does not contain (b) or (c).
3. **The prior work on Talagrand's weight (bears on 12(dd)).** Keller, Mossel and Schlank, Discrete Math. 312 (2012)
   3364-3372 ("A note on the entropy/influence conjecture"), and Han, arXiv:2312.08271: H(f) <= c1 I + c2 sum_k
   Inf_k log(1/Inf_k). Our elementary bound E_i <= Inf_i (log2(1/Inf_i) + 1/ln 2) (12(dd) item 3) is the per-coordinate
   E-version of this. Summed, it gives sum_i E_i <= sum_i Inf_i log2(1/Inf_i) + I/ln 2, so it reproduces their theorem for
   A = sum_i E_i in place of H. The weighted statement (W_g) at b = 1 differs from theirs: both sides carry the weight.
   Its left side is at most (1/ln 2) I, which is not small against the right side sum_i Inf_i/(1 + log(1/Inf_i)).
   12(dd) item 3 stands as the open window.
4. **Verdict for 11 item 3.** None of the six papers now read (Wan-Wright-Wu, CKLS, ACKSW, Lecomte-Tan,
   Keller-Mossel-Schlank, Han) states (b) H <= (w + 7.94) I for width-w DNF/CNF or (c) H <= (6.94 + log2(1 + 4m)) I
   for m-term DNF. As stated bounds, they may be called new, cited against CKLS Cor 4.4 / Th 4.13 and ACKSW's min{C^0, C^1}
   question. Both are short consequences of the kappa-Var route in 11. Status: proved here, no referee. The depth form
   of (d) remains KKLMS.

### 12(gg) (10 Nov 22:1x, an agent; NEXT (4)(c)) Slowly varying weights are no easier than the unweighted statement

Notation as in 12(dd): Q_g(f) = sum_i g(Inf_i) E_i / sum_i g(Inf_i) Inf_i and C_g = sup_f Q_g(f); G(f) = sum_i E_i / I.

1. **Composition with balanced inner function (exact).** Let psi on n bits be balanced (psihat(empty) = 0) and F on m bits, and
   put h = F(psi(x^1), ..., psi(x^m)) on disjoint blocks. Then hhat(S_1, ..., S_m) = Fhat(T) prod_{j in T} psihat(S_j) with
   T = {j : S_j nonempty}, and for the coordinate (j, i)
       Inf_(j,i)(h) = Inf_j(F) Inf_i(psi),
       E_(j,i)(h)   = Inf_j(F) E_i(psi) + sum_{T not containing j} Phi(Fhat(T)^2, Fhat(T + j)^2 psihat({i})^2).
   Proof: pairs (S_j, S_j + i) with both nonempty keep T and, by homogeneity of Phi and sum_{S nonempty} psihat(S)^2 = 1 on
   the other blocks, give Inf_j(F) E_i(psi). The pair (empty, {i}) is the only one that moves T, and gives the sum. (This is
   FEIB26 PROOFS section 1 with the T-term written out.) Checked to 0 error, code/maj_comp_check.py (three psi, F = Maj_3, Maj_5).
2. **For F = Maj_m the extra term vanishes.** Majority (m odd) has Fourier weight only on odd sets, so Fhat(T) Fhat(T + j) = 0
   and Phi(.,.) = 0 in every term. Hence E_(j,i) = tau_m E_i(psi) and Inf_(j,i) = tau_m Inf_i(psi), with
   tau_m = Inf_j(Maj_m) ~ sqrt(2/(pi m)), and G(Maj_m o psi) = G(psi) exactly.
3. **Theorem.** If g > 0 is slowly varying at 0 (g(c t)/g(t) -> 1 as t -> 0 for each c > 0), then C_g >= G(psi) for every
   balanced psi. Proof: by 2, Q_g(Maj_m o psi) = sum_i g(tau_m Inf_i) E_i / sum_i g(tau_m Inf_i) Inf_i over the finitely many
   i with Inf_i > 0. Dividing by g(tau_m), each ratio g(tau_m Inf_i)/g(tau_m) -> 1 as m -> infinity, so Q_g -> G(psi).
   Numerically, psi = (x1 AND x2) XOR x3 has G = 1 and Q_1(psi) = 0.6667. Then Q_1(Maj_3 o psi) = 0.8000 and
   Q_1(Maj_5 o psi) = 0.8285, rising toward 1 at the slow log rate.
4. **The weight question for g = g(Inf_i) is settled up to regular variation.** Let g be regularly varying at 0 with index
   alpha. If alpha > 0, then g(t) log(1/t) -> 0 and 12(dd) item 1 gives C_g = infinity. If alpha = 0, g is slowly varying,
   which includes every log(1/t)^-b and the constant; then C_g >= sup over balanced psi of G(psi). So a weight built from Inf_i
   alone either makes the statement false or makes it at least as strong as the unweighted good-coordinate bound (for
   balanced functions). It never gives an easier route. The open window of 12(dd) item 3 is closed in this sense. Whether
   C_1 = sup G is open, as is the case of g that is not regularly varying, which is not worth pursuing.
   Data: agent's n=6 monotone census has sup Q_1 = 2.9733 < sup Q_0 = 3.0310 (finite n, consistent with 3: the
   lift needs m -> infinity). n=7 (all 2,414,682,040,998 monotone functions, leaders recomputed independently; results/q7
   and merged7_full.txt in fei_solve_agent_2026_11_10): sup Q_0 = 3.164564560463, sup Q_1/2 = 3.124590660064,
   sup Q_1 = 3.082273853464, all at one function (f1 fca8f0a0cc880000, f0 0; H 3.8716, I 1.1094). The gap
   sup Q_0 - sup Q_1 is 0.058 at n=6 and 0.082 at n=7, so it does not close at small n; the lift in 3 uses n*m variables
   (m -> infinity), far beyond any census, and that is what makes the weights equal in the limit.
   max(Q_1 - Q_0) = 0.1177 (n=6), 0.1223 (n=7). [added 22:5x]
   Lift seen directly (agent, results/maj3_lift.txt): balanced monotone psi on 3-4 variables are odd except table
   eac8, and odd functions have E_i = 0 everywhere. For eac8: Q_0 1.268273, Q_1 1.201205; on Maj_3 o eac8 (12 variables)
   Q_0 1.268273 unchanged, as item 2 says, and Q_1 1.219496 (Q_1 - Q_0 from -0.0671 to -0.0488). [added 23:1x] Status: 1-3 proved here, exact checks above, no referee.

### 12(hh) (10 Nov 23:1x, an agent) 12(gg) reaches balanced functions only; the biased case keeps the empty pair

1. **Data (agent, n=6 monotone, exhaustive).** sup G over all f is 3.030964 (mean -0.78125); over balanced f 1.784288;
   over |fhat(empty)| <= 1/8 it is 2.012892. So at small n the balanced class sits far below the overall sup (balanced
   monotone functions on few variables are close to odd ones, and odd functions have E_i = 0).
2. **Biased composition (derivation, same steps as 12(gg) item 1).** For psi with mean mu, sigma^2 = 1 - mu^2, expand F in
   the mu-biased basis, u_j = (psi(x^j) - mu)/sigma. Then hhat(S_1..S_m) = F^mu(T) prod_{j in T} psihat(S_j)/sigma and
       Inf_(j,i)(h) = Inf^mu_j(F) Inf_i(psi) / sigma^2,
       E_(j,i)(h)   = Inf^mu_j(F) E'_i(psi) / sigma^2 + sum_{T not containing j} Phi(F^mu(T)^2, F^mu(T + j)^2 psihat({i})^2 / sigma^2),
   where E'_i(psi) = E_i(psi) - Phi(mu^2, psihat({i})^2) is E_i without the empty pair. Two differences from the balanced
   case: the empty pair of psi is lost, and under bias Maj_m has even-level weight, so the extra term does not vanish.
   Checked to 5.6e-17 on every (j, i), code/biased_comp_check.py (psi = the n=6 leader, mu = -0.78125, F = Maj_3,
   18 variables). There E'/I(psi) = 2.094317, so the empty pairs carry 31 pct of the leader's E, and yet
   G(Maj_3 o psi) = 3.072379 > G(psi) = 3.030964: under bias the extra term more than pays back the lost pair.
3. **Balancing by a multiplexer loses the same pair (checked, code/balance_mux_check.py).** h(x, x', z) = psi(x) if z = 0,
   else -psi(x') (or the dual -psi(-x'), which keeps monotonicity; identical numbers). On the overall leader: G 3.030964
   -> 1.607585; the x coordinates alone give 2.721111 and z adds E 0.390 on Inf 0.805. [corrected 23:1x: an earlier line
   here read 2.721 as E'/I and the empty pairs as 10 pct of E; E'/I is 2.094 (item 2), and the mux keeps part of each
   empty pair through the pairs (z, z + i).] On the balanced leader the mux gives 1.835044 (up from 1.784288, the x part unchanged); near
   balanced 2.012892 -> 2.020421.
4. **Reading.** For a biased function the pair (empty, {i}) contributes Phi(mu^2, fhat(i)^2), which for mu near 1 is about
   fhat(i)^2 log(1/fhat(i)^2): the Talagrand weight of 12(dd) again, now as the one Fourier pair that no composition or
   balancing step carries over intact (item 2 shows composition replaces it with the extra term, which can be larger).
   So the 12(gg) closure covers sup over balanced psi; whether the weighted constant C_1
   reaches the overall sup G needs either the biased extra term of item 2 (a mu-biased outer function whose extra term
   vanishes) or a direct construction. Next check: item 2 numerically, then search outer F with mu-biased spectrum
   supported where F^mu(T) F^mu(T + j) = 0.
