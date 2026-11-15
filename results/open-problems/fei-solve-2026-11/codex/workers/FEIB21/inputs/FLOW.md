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
  A_{G_j} <= A_{>=k_j} <= M delta / beta_{k_j} < 2^(j+1) M delta, and B_{G_j} <= 2^(-j) delta. So
     sum_{k in G_j} g <= 2^(-j) delta log2(1 + 2^(2j+1) M) <= 2^(-j) delta (2j + log2(1 + 2M)),
  and sum_j 2^(-j) = 2, sum_j j 2^(-j) = 2.
  For a threshold function the case K = 0 is free: A_{>=0} B_0 <= delta^2.

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
  a constant factor). Gaussian model (X, Y rho-correlated normals, slab of half-width eps at height t): the
  product is delta^2/pi to first order, for every rho and t: Cross is about sqrt(1-rho^2) e^(-t^2/2)/pi, Stay is
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
  0/1 weights; weights growing fast along pi).

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

(f) Why a random ordering is not enough (hand estimate, NOT run). For tribes of width w and a uniformly random
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
  ghat(i)^2; since Phi(p, t q)/t decreases in t it is at least the biased erasure term, and the excess is where
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
    random DNF w 9,  n 250,  m 355     0.0417    5.290    5.995     0.882    3.19
    random DNF w 10, n 500,  m 710     0.0245    5.858    6.779     0.864    4.04
    random DNF w 10, n 300,  m 710     0.0340    5.681    6.298     0.902    4.03
    random DNF w 11, n 600,  m 1420    0.0195    6.362    7.106     0.895    5.79
    random DNF w 12, n 2000, m 2839    0.0076    6.848    8.471     0.808    8.30
    random DNF w 12, n 1000, m 2839    0.0124    6.986    7.769     0.899    9.28
    random DNF w 13, n 4000, m 5678    0.0041    7.406    9.387     0.789   11.07   (524,288 samples)

Reading. (1) Localised families: flat or falling while the trivial bound doubles. (2) Hex: M stays at 1.15 to 1.17
but L/Inf creeps up 0.17 per step; larger boards (32 to 96) are still running, and the ball chain is not optimised.
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
    unbalanced (f is 1 with probability near 1):
    6    4     0.395    3.73e-2     3.330 +- 0.002    5.55   5.46             4.23   4.23      3.94   3.95     4.00
    8    8     0.220    1.10e-2     2.855 +- 0.002    6.64   6.42             4.63   4.49      3.73   3.74     5.00
    9    24    0.0002   1.35e-5     2.703 +- 0.002    7.30   7.12             6.85   6.52      -      -        6.58

(L^r = H(1[root in U] | the last r revealed elements of U among the mates); L^1 is the nested witness of 12.
Balanced rows take D^2 L 2^-L about 1.4, the largest D for which the model is not almost constant. Widths 20
(D 196) and 24 (D 712) are running.)

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
