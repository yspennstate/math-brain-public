# BT: biased weighted thresholds (ledger items C004, C025)

Route owner: Opus subagent BT-biased-thresholds (workflow claude-51330238), started 2026-10-12.
Everything here is my own working. Statuses follow the campaign rules: PROVED only with a
complete proof below; finite computations are EVIDENCE; KNOWN carries a citation.

## 0. Definitions and the exact target

Inputs y in {0,1}^n with the product law mu = prod Bernoulli(q_i), 0 < q_i < 1.

    sigma_i^2 = 4 q_i (1 - q_i),   phi_i(y_i) = (2 y_i - 1 - (2 q_i - 1)) / sigma_i,
    phi_S = prod_{i in S} phi_i   (orthonormal basis of L^2(mu)).

For f : {0,1}^n -> {-1,1}, write f = sum_S fhat(S) phi_S, P(S) = fhat(S)^2 (sum_S P(S) = 1), and

    E_mu(f)  = sum_{S != empty} P(S) ln( sigma_S^2 / P(S) )      (nats),  sigma_S^2 = prod_{i in S} sigma_i^2,
    H_mu^+(f) = E_mu(f) / ln 2                                     (bits),
    I_mu(f)  = sum_S |S| P(S),   V_mu(f) = Var_mu(f) = sum_{S != empty} P(S),
    Delta_mu(f) = I_mu - V_mu = sum_{|S|>=2} (|S|-1) P(S),
    J(f)     = sum_{|S|>=2} |S| P(S),          so  Delta <= J <= 2 Delta.

A weighted threshold is T(y) = 1[ sum_i w_i y_i >= theta ] with real w, theta, and f = 2T - 1.

**Target (C025).** Is there an absolute C with H_mu^+(f) <= C * Delta_mu(f) for every weighted
threshold f and every product law mu? Equivalently (up to a factor 2) E_mu(f) <= C' J(f).
C004 (paper Theorem bias:strong, constant C_T = 80 + 460/ln 2 < 744) proves it for symmetric
thresholds 1[sum y_i >= t].

This is exactly the "FEI+ for product distributions" inequality of O'Donnell and Tan
(Conjecture 1 of arXiv:1304.1347, ICALP 2013), there written on {-1,1}^n with
sigma_i^2 = 1 - mu_i^2, restricted to the class of weighted thresholds. Known from that paper (KNOWN):
Theorem 1 (composition: if the gate satisfies eta-biased FEI+ with factor C2 and disjoint inner
functions satisfy mu-biased FEI+ with factor C1, the composition satisfies it with max(C1,C2));
Theorem 2 (every F of arity k satisfies mu-biased FEI+ with factor 2^{O(k)}, uniformly in the biases).
So the open part is uniformity in the arity for thresholds with arbitrary weights.

## 1. Basic reductions and identities (PROVED, elementary)

**(R1) Signs of weights.** Replacing y_i by 1 - y_i replaces q_i by 1 - q_i, leaves sigma_i fixed and
replaces phi_i by -phi_i. So P(S) and every quantity above is unchanged, while w_i -> -w_i and
theta -> theta - w_i. Hence WLOG all w_i >= 0, i.e. T is monotone increasing.

**(R2) Output negation** f -> -f changes no P(S). Coordinates with w_i = 0 are irrelevant and every
S containing one has P(S) = 0, so they can be deleted. Deterministic coordinates (q_i in {0,1})
are restrictions and are deleted (the restricted function is again a weighted threshold).

**(R3) The g-representation.** For one coordinate and any h, E[h phi_i | y_{-i}] =
(1-q_i) h(0) phi_i(0) + q_i h(1) phi_i(1) with phi_i(1) = 2(1-q_i)/sigma_i and
phi_i(0) = -2 q_i / sigma_i, hence E[h phi_i | y_{-i}] = (sigma_i/2) (h(1) - h(0)). Iterating over
the coordinates of S,

    fhat(S) = sigma_S g_S,   g_S := 2^{-|S|} E_{mu_{S^c}} [ d_S f ],   d_S f(.) = sum_{z in {0,1}^S} (-1)^{|S|-|z|} f(z, .).

Thus P(S) = sigma_S^2 g_S^2 and

    E_mu(f) = sum_{S != empty} sigma_S^2 g_S^2 ln(1 / g_S^2),

with |g_S| <= 1 for Boolean f (|d_S f| <= 2^{|S|}), so every summand is >= 0. Computationally g is
obtained from f by the butterfly (a, b) -> ((1-q_i) a + q_i b, (b - a)/2) in each coordinate; all
g_S are rational when the q_i are rational, and so are the P(S) (exact arithmetic is possible).

**(R4) Monotone identities.** For monotone T and f = 2T - 1 put d_i = T(y_i=1) - T(y_i=0) in {0,1}
and rho_i = E d_i. Then fhat(B u {i}) = sigma_i dhat_i(B) for i notin B, so

    P({i}) = sigma_i^2 rho_i^2,  I_i := sum_{S contains i} P(S) = sigma_i^2 rho_i,
    J_i := sum_{S contains i, |S|>=2} P(S) = sigma_i^2 rho_i (1 - rho_i),  J = sum_i J_i,
    I_i <= V  (since I_i <= sum_{S != empty} P(S)).

For a weighted threshold, d_i = 1[ theta - w_i <= W_{-i} < theta ], W_{-i} = sum_{j != i} w_j y_j.
The singleton terms of E are 2 sigma_i^2 rho_i^2 ln(1/rho_i) <= 2 J_i (using rho ln(1/rho) <= 1-rho),
so only |S| >= 2 matters:  E <= 2J + E_{>=2},  E_{>=2} = sum_{|S|>=2} P(S) ln(sigma_S^2/P(S)).

## 2. First computations (EVIDENCE, float64 unless stated)

Code: code/biased.py (butterfly g-transform, metrics, exact Fraction version, TC of conditional
laws), code/levels.py (functions of group counts, mpmath), code/search_small.py, code/scan_sym.py,
code/scan_random.py. Sanity checks passed: MAJ3 uniform gives H+=2, I=1.5, Var=1, ratio 4;
dictator gives 0/0; AND2 over a bias grid reaches 7.7418 < 2+4/ln2 = 7.77078 (the sharp AND/OR
constant of paper Lemma comp:elementary-gates); exact Fraction Parseval = 1 on a 5-variable LTF;
level code agrees with brute force to 1e-16 on weights (2,2,1,1,1), theta 4.

* Exhaustive monotone LTFs, all coordinates relevant, integer weights <= 9, n <= 5 (data/search_small_n5.json,
  n<=4 in search_small_n4.json), maximizing H+/Delta over the biases by Nelder-Mead on logit(q)
  (|logit| <= 14) from 6-9 starts: the supremum found is 7.77078 for every n, always in a
  degenerate limit where extreme biases reduce the function to AND2/OR2 (e.g. w=(6,5,4,1), theta 6,
  q -> (0,0,1,1)). No interior maximum above it.
* Symmetric thresholds T_{t,m}, m <= 40, every t, common bias p in {0.001,...,0.999} (mpmath with
  adaptive precision, re-run at +40 digits; precision gap 0): best H+/Delta = 7.768 (m=2) decreasing to
  7.732 (m=40), always OR (t=1) at p=0.001. [A first run at fixed 40 digits printed 53236 for m=32:
  that was cancellation (probabilities 1e-96 below the working precision), fixed by working with the
  0/1 function and adaptive precision. Recorded as a numerical trap.]
* Random weighted thresholds n=5..11 (4749 configs, 5 weight laws, extreme biases down to 1e-5, local
  bias optimization; data/scan_random_seed7.json): best 7.7707, again an AND2/OR2 degeneration.

Working conjecture suggested by the data (CONJECTURE, not proved): for every weighted threshold and
every product law, H_mu^+ <= (2 + 4/ln 2) Delta_mu, i.e. the AND/OR constant is the supremum.

## 3. The paper's normalization-credit lemma does NOT extend to weighted thresholds (PROVED)

The symmetric proof (paper Prop. bias:weak) rests on Lemma bias:credit,

    (CR)   V ln(1/V) <= sum_i I_i ln^+(4 rho_i / V) + C I,

whose proof splits ln(1/alpha) = TC(mu_A) + sum_i KL(mu_A^(i) || mu_i) and needs

    (TCB)  alpha * TC(mu_A) <= C' I     (paper eq. bias:eq-4-5, C' = 13/4 for symmetric thresholds),

where A is the minority output event, alpha = mu(A), mu_A = mu( . | A).

**Family.** For s >= 2 let T_s(y_0, y_1..y_s) = 1[ s*y_0 + y_1 + ... + y_s >= s ] = y_0 OR (y_1 AND ... AND y_s),
a weighted threshold with two weights (it is also a read-once formula, so C004 covers its FEI+).
Biases: q_0 = p_h, q_j = p (j >= 1). Put a = p^s, alpha = P(T=1) = p_h + (1-p_h) a, and fix x in (0,1)
by requiring mu_A(y_0 = 0) = x, i.e. (1-p_h) a = x alpha, equivalently p_h = alpha (1-x).

**Exact facts.** mu_A = x * delta_{(0,1,...,1)} + (1-x) * ( delta_{y_0=1} (x) Bern(p)^{(x)s} ) (disjoint supports), so
    TC(mu_A) = s * [ h(x + (1-x) p) - (1-x) h(p) ]          (h = natural binary entropy).
rho_0 = 1 - a, rho_j = (1-p_h) p^{s-1} = x alpha / p, I_0 = 4 p_h (1-p_h)(1-a) <= 4 alpha (1-x),
I_j = 4 (1-p) x alpha, I = I_0 + s I_1 <= 4 alpha (1 - x + s x), V = 4 alpha (1 - alpha),
ln(1/alpha) = s ln(1/p) - ln(1/x) + ln(1/(1-p_h)) >= s ln(1/p) - ln(1/x).

**Proposition 3.1 (credit failure).** If p <= x <= 1/2 and alpha <= 1/2, then
    V ln(1/V) - sum_i I_i ln^+(4 rho_i/V)  >=  4 alpha [ (s-1) x ln(1/x) - ln 4 - alpha ln(1/alpha) - 2 alpha (1 + s x) ].
With x = 1/s this gives  [V ln(1/V) - sum_i I_i ln^+(4 rho_i/V)] / I  >=  ((s-1)/(2s)) ln s - ln 2 - delta_s,
delta_s = (alpha ln(1/alpha) + 4 alpha)/2, and alpha <= s p^s is astronomically small for p = 1/(50 s).
Hence no absolute C makes (CR) true for weighted thresholds.

*Proof.* (i) V ln(1/V) = 4 alpha (1-alpha) ln(1/(4 alpha (1-alpha))) >= 4 alpha (1-alpha) (L - ln 4), L = ln(1/alpha).
(ii) 4 rho_0 / V = (1-a)/(alpha(1-alpha)) <= 1/(alpha (1-alpha)), and ln(1/(1-alpha)) <= 2 alpha for alpha <= 1/2, so the
heavy credit is <= I_0 (L + 2 alpha) <= 4 alpha (1-x)(L + 2 alpha).
(iii) 4 rho_j / V = x/(p (1-alpha)) >= 1 (as x >= p), so each light credit is
I_j ln(x/(p(1-alpha))) <= 4 (1-p) x alpha (ln(x/p) + 2 alpha).
(iv) Subtract, use L >= s ln(1/p) - ln(1/x):
4 alpha [ (1-alpha)(L - ln 4) - (1-x)(L + 2 alpha) - s(1-p) x (ln(x/p) + 2 alpha) ]
>= 4 alpha [ x L - alpha L - ln 4 - 2 alpha (1-x) - s (1-p) x ln(x/p) - 2 alpha s x ]
>= 4 alpha [ x (s ln(1/p) - ln(1/x)) - s x (ln(1/p) - ln(1/x)) + s p x ln(x/p) - ln 4 - alpha L - 2 alpha (1 + s x) ],
and s p x ln(x/p) >= 0, which is the display. For x = 1/s divide by I <= 4 alpha (2 - 1/s) <= 8 alpha. QED.

**Proposition 3.2 (TC failure).** In the same family, alpha TC(mu_A)/I >= s [h(x + (1-x)p) - (1-x) h(p)] / (4 (1 - x + s x)).
For x = 1/s and p -> 0 this tends to s h(1/s)/8 = (ln s + (s-1) ln(s/(s-1)))/8 -> infinity. So (TCB) fails.
*Proof.* The formula for TC is the exact mixture computation above; divide by I <= 4 alpha (1 - x + s x). QED.

**Exact check (EVIDENCE, but exact rationals).** code/verify_credit_cex.py computes all P(S) exactly with Fractions
(Parseval = 1 exactly) for s = 4, 8, 10 with x = 1/s, p = x/50:
(V ln(1/V) - credit)/I = -0.1874, 0.236581, 0.365572 and H+/Delta = 2.1026, 2.04953, 2.03994.
code/credit_counterexample.py (mpmath, 60 digits) continues: s = 16, 32, 64, 128 give
(V ln(1/V) - credit)/I = 0.629, 1.0028, 1.3653, 1.7211 (growth (ln 2)/2 per doubling of s, as predicted) and
alpha TC/I = 0.471, 0.553, 0.637, 0.722 (growth (ln 2)/8 per doubling).

**What this does and does not say.** It refutes the extension of Lemma bias:credit and of eq. (bias:eq-4-5) to weighted
thresholds; it does not refute FEI+ for them (T_s has H+/Delta ~ 2). The loss is in the product-form credit:
under mu_A the s light coordinates are critical together (a block), each is charged ln(1/pi_l), pi_l = x, i.e. s ln(1/x)
in total, while the event "the block is the spectral sample" costs only ln(1/x). In the Gibbs bound with the paper's
reference the loss is the step ln Z_k <= k + 4m: at level k = s the exact normalizer is about (8e/s)^s, i.e. it carries a
credit -s ln s that the paper's bound discards. With exact per-level normalizers the paper's reference does give
O(1) per unit influence on T_s (numerically about 1.3 I for s = 4..12; section 7). So the obstruction is to the bookkeeping
(level entropy + normalizer + per-coordinate credit), not to the reference measure itself.

Wider scans (EVIDENCE): random weighted thresholds n <= 10 (19,737 configs, local bias optimization) gave
max alpha TC/I = 0.302 and max (V ln(1/V) - credit)/I = 0.418; exchangeable 2-3 group thresholds with up to 160
coordinates (317k configs, code/group_credit.py) gave alpha TC/I <= 0.281 and credit excess <= 0.84 (the last is the
AND_k limit q -> 1, where the excess/I tends to 1). The failure needs the block structure plus x of order 1/s and p << x,
which random search does not find; it is invisible below s ~ 8.

## 4. Tools valid for every product law (PROVED)

Notation: phi_s(x) = x ln(s/x) (phi_s(0)=0); phi_s >= 0 on [0,s], its maximum is s/e, it is increasing on [0,s/e]
and subadditive. A monotone T is *regular* if some linear order 1,...,n of the coordinates has, for i<j and all y,
T(y^{i<-1,j<-0}) >= T(y^{i<-0,j<-1}). Weighted thresholds with w_1 >= ... >= w_n >= 0 are regular (after R1).
U_i = {1,...,i-1}, Lambda_i = sum_{j<i} sigma_j^2.

**Lemma 4.1 (least-element decomposition; any T).** For f = 2T-1 put d_i = T(y_i=1)-T(y_i=0) and
e_i = E[d_i | y_{U_i}] (a function of the coordinates before i). Then

    E_mu(f) = sum_i sigma_i^2 [ rhohat_i^2 ln(1/rhohat_i^2) + sum_{B subset U_i, B nonempty} phi_{sigma_B^2}(ehat_i(B)^2) ],
    Delta_mu(f) = sum_i sigma_i^2 I_mu(e_i),     I_mu(e) := sum_B |B| ehat(B)^2,

where rhohat_i = E d_i (= rho_i for monotone T).
*Proof.* Every nonempty S has a unique last element i, S = B u {i} with B subset U_i. By (R3)/(R4) fhat(S) = sigma_i dhat_i(B),
and for B subset U_i, dhat_i(B) = E[d_i phi_B] = E[e_i phi_B] = ehat_i(B). So P(S) = sigma_i^2 ehat_i(B)^2 and
ln(sigma_S^2/P(S)) = ln(sigma_B^2/ehat_i(B)^2). Summing gives the first identity; |S| - 1 = |B| gives the second. QED.
(Checked numerically to 2e-15 on 400 random thresholds, code/verify_tools.py.)

**Lemma 4.2 (DTC identity and biased edge isoperimetry; any increasing T).** Let A = {T=1}, alpha = mu(A) > 0, Y ~ mu_A
and c_i = mu_A(Y_i = 1 and i pivotal at Y) = q_i rho_i / alpha. Then

    ln(1/alpha) = sum_i c_i ln(1/q_i) - DTC(mu_A),     DTC(Y) := H(Y) - sum_i H(Y_i | Y_{-i}) >= 0,

hence alpha ln(1/alpha) <= sum_i q_i ln(1/q_i) rho_i.
*Proof.* H(mu_A) = -ln(1/alpha) + sum_i [b_i ln(1/q_i) + (1-b_i) ln(1/(1-q_i))], b_i = mu_A(Y_i = 1). Given Y_{-i} = z:
if (z,0) and (z,1) are both in A then Y_i ~ Bern(q_i); if only (z,1) is in A (i pivotal) then Y_i = 1; (z,0) in A with
(z,1) not in A is impossible. Since mu_A(i pivotal at Y_{-i}) = q_i rho_i/alpha = c_i, H(Y_i|Y_{-i}) = (1-c_i) h(q_i) and
b_i = c_i + (1-c_i) q_i. A direct computation gives b ln(1/q) + (1-b) ln(1/(1-q)) - (1-c) h(q) = c ln(1/q).
DTC >= 0 because H(Y) = sum_i H(Y_i | Y_<i) >= sum_i H(Y_i | Y_{-i}). QED.
Status: the p-biased case, alpha ln(1/alpha) <= p ln(1/p) sum_i rho_i, is the classical edge-isoperimetric inequality for
increasing sets of the biased cube (KNOWN); the exact identity with DTC is an elementary entropy proof of it.
Checked to 3e-15 (code/verify_tools.py).

**Lemma 4.3 (paper lem:pivotal-antichain, KNOWN).** For regular T, on every fiber fixing the coordinates outside
U_i u {i}, the support of d_i is an antichain of {0,1}^{U_i}.

**Lemma 4.4 (antichains under product laws).** Let nu be a product law on {0,1}^m with marginals r_j and
m_j = min(r_j, 1-r_j). Every antichain Aset satisfies nu(Aset) <= E[(F+1)^{-1/2}] <= (2 sum_j m_j)^{-1/2}, where F is a sum
of independent Bernoulli(2 m_j). Also nu(Aset) <= max(r_j, 1-r_j) for every single j.
*Proof.* Realize Y_j as its more likely value with probability 1-2m_j and as a fair bit otherwise (this is the law of Y_j).
Conditional on the set F of fair coordinates and on all other values, Y_F is uniform on {0,1}^F and the fiber of Aset is
an antichain there, of density at most c_|F| <= (|F|+1)^{-1/2} (Sperner; paper lem:antichain-density). Average and use
E[1/(F+1)] = int_0^1 prod_j (1 - p_j + p_j s) ds <= 1/E F with Cauchy-Schwarz. For the last claim condition on all
coordinates except j: the fiber is an antichain of {0,1}, i.e. at most one point. QED.

**Lemma 4.5 (biased rank lemma).** For regular T and rho_i > 0, let nu_i(B) = dhat_i(B)^2/rho_i on subsets of [n]\{i}.
Then E_{nu_i} ln^+( Lambda_i / (|B cap U_i| + 1) ) <= L_0 := 3 + ln 4.
*Proof.* Let Y ~ mu and let Y' resample each coordinate of U_i independently with probability t (fresh from mu).
Orthonormality gives E[d_i(Y) d_i(Y')] = sum_B dhat_i(B)^2 (1-t)^{|B cap U_i|} = rho_i E_{nu_i}(1-t)^kappa, kappa = |B cap U_i|,
and E[d_i(Y) d_i(Y')] <= rho_i sup_y P(d_i(Y') = 1 | Y = y). Given y, each j in U_i is fair-activated independently with
probability 2 t m_j (fair-bit representation of the fresh sample). Conditional on the activated set F and on all other
values, Y'_F is uniform and the support of d_i is an antichain there (Lemma 4.3, then fix U_i \ F). As in Lemma 4.4 the
conditional probability is <= E(|F|+1)^{-1/2} <= (2 t sum_{j in U_i} m_j)^{-1/2} <= (2/(t Lambda_i))^{1/2}, because
m_j >= q_j(1-q_j) = sigma_j^2/4. So E_{nu_i}(1-t)^kappa <= (2/(t Lambda_i))^{1/2}. For real K > 1 put t = 1/(2K):
nu_i(kappa + 1 < K) <= (1-t)^{-(K-1)} E(1-t)^kappa <= e^{1/2} (4K/Lambda_i)^{1/2}, using
-(K-1) ln(1 - 1/(2K)) <= (K-1)/(2K-1) <= 1/2; for K <= 1 the event is empty. Hence
E ln^+(Lambda_i/(kappa+1)) = int_0^inf nu_i(kappa + 1 < Lambda_i e^{-u}) du <= int_0^inf min(1, 2 sqrt(e) e^{-u/2}) du
= 2 ln(2 sqrt e) + 2 = 3 + ln 4. QED. (Numerically the functional never exceeded 0.68 on 400 random thresholds.)

## 5. The weak bound up to the normalization term (PROVED)

**Theorem 5.1.** For every regular monotone T (in particular every weighted threshold), f = 2T-1, and every product
law with 0 < q_i < 1,

    E_mu(f) <= V ln(1/V) + A_0 I_mu(f),    A_0 = 2 + ln 7 + (6/5)(3 + ln 4) < 9.21 (nats),    V = Var_mu f.

*Proof.* For k >= 1 let theta_k(i) = sigma_i^2 min(1, (k/Lambda_i)^a) with a = 6/5 (theta_k(i) = sigma_i^2 if Lambda_i = 0),
Q_k(S) = prod_{i in S} theta_k(i) / Z_k on k-sets, Z_k = e_k(theta_k). Gibbs on level k, with W_k = sum_{|S|=k} P(S):

    sum_{|S|=k} P(S) ln(sigma_S^2/P(S)) <= W_k ln(1/W_k) + W_k ln Z_k + a sum_{|S|=k} P(S) sum_{i in S} ln^+(Lambda_i/k).

Normalizer: h(x) = min(1,(k/x)^a) is nonincreasing and sigma_i^2 <= 1, so sigma_i^2 h(Lambda_i) <= int_{Lambda_i}^{Lambda_{i+1}} h(x-1) dx
and sum_i theta_k(i) <= int_{-1}^inf h = 1 + k + k/(a-1) <= 7k for a = 6/5, k >= 1; thus Z_k <= (7k)^k/k! <= (7e)^k.
Rank: for S = B u {i}, |S| >= |B cap U_i| + 1, so sum_S P(S) sum_{i in S} ln^+(Lambda_i/|S|) <= sum_i I_i E_{nu_i} ln^+(Lambda_i/(|B cap U_i|+1))
<= L_0 I (Lemma 4.5). Levels: sum_k W_k ln(1/W_k) = V ln(1/V) + V H(lambda), lambda_k = W_k/V is a law on {1,2,...} with
mean m = I/V, so H(lambda) <= 1 + ln m <= m and the sum is <= V ln(1/V) + I. Adding: E <= V ln(1/V) + (2 + ln 7 + (6/5) L_0) I. QED.
(Numerically (E - V ln(1/V))/I <= 1.66 on 400 random thresholds.)

**Corollary 5.2 (bias floor).** If every q_i lies in [delta, 1-delta], 0 < delta <= 1/2, then for every regular monotone T

    V ln(1/V) <= max(1.661, ln(1/delta)/(1-delta)) I,     E_mu(f) <= A_delta I_mu(f),   A_delta = A_0 + max(1.661, ln(1/delta)/(1-delta)).

*Proof.* Let alpha be the smaller output probability. If alpha >= 1/20 then V >= 0.19 and V ln(1/V) <= ln(1/0.19) V <= 1.661 I
(Poincare: V <= I). Otherwise pass if needed to the dual T*(y) = 1 - T(1-y) (biases 1-q_i, the same rho_i, I, V) so that the
minority event is increasing; V <= 4 alpha < 1/e gives V ln(1/V) <= 4 alpha ln(1/alpha) <= 4 sum_i q_i rho_i ln(1/q_i)
(Lemma 4.2) = sum_i I_i ln(1/q_i)/(1-q_i), and q -> ln(1/q)/(1-q) is decreasing (ln x <= x-1). QED.

The term V ln(1/V) is not O(I) uniformly in the biases (AND_k under p: ratio ~ ln(1/p)); section 3 shows that the
per-coordinate credit of the symmetric proof cannot pay for it for weighted thresholds.

## 6. Full corrected FEI+ under a bias floor (PROVED)

**Theorem 6.1.** Let 0 < delta <= 1/2. For every regular monotone T (every weighted threshold, after R1) and every product
law with all q_i in [delta, 1-delta],

    E_mu(f) <= K_delta J(f) <= 2 K_delta Delta_mu(f),     K_delta = max( 2 A_delta/(delta(1-delta)), 8 A_delta + 18.5 ),

so H_mu^+(f) <= (2 K_delta / ln 2) Delta_mu(f) = O(delta^{-1} log(e/delta)) Delta_mu(f), uniformly in arity and weights.

*Proof.* Put eta = delta(1-delta)/2.
Case A: every rho_i <= 1 - eta. Then J_i = sigma_i^2 rho_i (1-rho_i) >= eta I_i, so E <= A_delta I <= (A_delta/eta) J.
Case B: some coordinate, call it 0, has rho_0 = 1 - eps with eps < eta. Write u = T(y_0 = 0) and v = 1 - T(y_0 = 1) as
functions of the other coordinates; uv = 0, u is increasing, v is decreasing, T = u + y_0 (1 - u - v), d_0 = 1 - u - v.
(i) For j != 0, j is pivotal at y only if d_0 vanishes at y^{j<-0} or at y^{j<-1}; hence
rho_j <= eps/(1-q_j) + eps/q_j = eps/(q_j(1-q_j)) < 1/2 and J_j >= I_j/2.
(ii) Coefficients: for nonempty B not containing 0, fhat(B) = 2(1-q_0) uhat(B) - 2 q_0 vhat(B) = (1-q_0) Uhat(B) - q_0 Vhat'(B),
with U = 2u-1, V' = 2v-1; for S = {0} u B with B nonempty, fhat(S) = sigma_0 dhat_0(B) = -sigma_0 (uhat(B) + vhat(B)).
For 0/1 functions |uhat(B)| <= sigma_B/2 (integrate one coordinate of B and use E|phi_j| = sigma_j), so every squared
quantity used below is at most sigma_B^2.
(iii) Paper inequality bias:eq-5-9 (valid when a^2, b^2 <= s): phi_s((a +- b)^2) <= 2 phi_s(a^2) + 2 phi_s(b^2) + 2a^2 + 2b^2; and
phi_s(lambda^2 x) = lambda^2 phi_s(x) + lambda^2 x ln(1/lambda^2) with lambda^2 ln(1/lambda^2) <= 2 lambda/e for 0 <= lambda <= 1.
Sets containing 0 with |S| >= 2: sigma_0^2 sum_{B nonempty} phi(dhat_0(B)^2) <= sigma_0^2 [ (1/2)(E(U) + E(V')) + (ln 2 + 1/2)(Var U + Var V') ],
using phi_s(Uhat^2/4) = phi_s(Uhat^2)/4 + (ln 4/4) Uhat^2; with sigma_0^2 <= 4(1-q_0) and sigma_0^2 <= 4 q_0 this is
<= 2(1-q_0) E(U) + 2 q_0 E(V') + 4(ln 2 + 1/2)[(1-q_0) Var U + q_0 Var V'].
Sets avoiding 0 with |B| >= 2: <= 2(1-q_0) E(U) + 2 q_0 E(V') + 2(2/e + 1)[(1-q_0) Var U + q_0 Var V'].
So E_{>=2}(f) <= 4[(1-q_0) E(U) + q_0 E(V')] + 8.25[(1-q_0) Var U + q_0 Var V'].
(iv) u = T|_{y_0=0} and 1 - v = T|_{y_0=1} are regular monotone with biases in [delta, 1-delta]; E, I and Var are invariant
under negation, so Corollary 5.2 gives E(U) <= A_delta I(U) and E(V') <= A_delta I(V'); also Var <= I.
(v) For j != 0, d_j T = (1-y_0) d_j u - y_0 d_j v, so I_j(f) = sigma_j^2 [(1-q_0) E(d_j u)^2 + q_0 E(d_j v)^2] and
sum_{j != 0} I_j(f) = (1-q_0) I(U) + q_0 I(V').
Hence E_{>=2}(f) <= (4 A_delta + 8.25) sum_{j != 0} I_j(f) <= 2(4 A_delta + 8.25) J by (i), and the singletons contribute
at most 2J (R4). So E <= (8 A_delta + 18.5) J. In both cases the claim holds, and J <= 2 Delta. QED.

Remarks. (a) The bias floor is used only in the normalization (Corollary 5.2, factor log(1/delta)), in the case split
(eta ~ delta) and in (i). (b) The theorem covers all regular monotone functions, not only thresholds. (c) At delta = 1/2
it reproves uniform-measure FEI+ for regular functions, with a worse constant than the paper's Theorem A.

## 7. Toward uniformity: level-conditioned references (EVIDENCE + a precise target)

Section 3 shows that a credit depending on the coordinate alone (4 pi_i, pi_i = I_i/V) overcharges a block of coordinates
that enter the spectral sample together. Two repairs were tested with exact normalizers e_k(theta) (code/gibbs_bound.py,
code/gibbs_ld.py; each quantity is an upper bound for E by Gibbs, a = 6/5):

* paper reference theta_k(i) = max(sigma_i^2 min(1,(k/Lambda_i)^a), 4 pi_i) with exact Z_k: on T_s (x = 1/s, p = x/50)
  B/I = 1.351, 1.286, 1.238 for s = 4, 8, 12, while the paper's normalizer bound ln Z_k <= k + 4m gives 5.15, 5.44, 5.62
  (growing); 195 random thresholds with local bias optimization gave at most 2.45 (exact Z_k) and 5.83 (paper's bound);
* level-dependent credit theta_k(i) = max(sigma_i^2 min(1,(k/Lambda_i)^a), 4 pi_i^(k)), pi_i^(k) the inclusion probability
  of i inside level k: on T_s, B/I = 0.631, 0.671, 0.683 against the true E/I = 0.622, 0.662, 0.674 (almost exact); on the
  three-class thresholds OR(y_0, AND(s lights, [Z >= t])) = 1[W y_0 + L + cZ >= s + ct] (s = 4..10, N = 5..8 fair z's)
  level-dependent B/I = 1.16 to 1.42, paper reference 1.83 to 2.07, true E/I = 0.77 to 0.98.

The level-dependent reference reduces the uniform weak bound to one inequality, the replacement of Lemma bias:credit
this route needs (OPEN target; it holds on T_s, and for symmetric thresholds it follows from the paper's credit lemma
by convexity of x ln x, since the level-wise credits dominate the global ones):

    (LCR)   sum_k W_k ln(1/W_k)  <=  sum_k sum_i W_k pi_i^(k) ln^+( 4 pi_i^(k) / sigma_i^2 )  +  C I.

Numerical test of (LCR) itself (code/scan_lcr.py, 2277 random weighted thresholds n <= 10 with extreme biases and local
maximization of the excess): max [sum_k W_k ln(1/W_k) - level-wise credits]/I = 0.744 (an OR-like threshold under moderate
biases); on T_s the excess is negative (-0.77, -0.73, -0.71 for s = 4, 8, 12). So (LCR) held with C = 0.75 in every test.

Given (LCR), Gibbs with theta_k(i) = max(sigma_i^2 min(1,(k/Lambda_i)^a), 4 pi_i^(k)) (whose sum is at most 7k + 4k) and Lemma 4.5
give E <= (C + 1 + ln 11 + (6/5) L_0) I for every weighted threshold and every product law. [Proof: sum_i theta_k(i) <= 11k,
so Z_k <= (11e)^k; the cost of i in S is <= a ln^+(Lambda_i/k) - ln^+(4 pi_i^(k)/sigma_i^2), and the level-k mass containing i
is W_k pi_i^(k); then Lemma 4.5 and (LCR).] The strong form then still needs a uniform near-dictator analysis (Theorem 6.1, Case B, uses the
bias floor in (i) and in the case split).

## 8. Summary and the next step

Proved here: the reductions and g-representation (section 1); the failure of the symmetric proof's credit lemma and of
its total-correlation step for weighted thresholds (Propositions 3.1, 3.2, on T_s = y_0 OR AND_s); the least-element
decomposition, the DTC identity, product-law antichain bound and biased rank lemma (section 4); the weak bound
E <= V ln(1/V) + 9.21 I for all regular monotone functions under all product laws (Theorem 5.1); full corrected FEI+
with constant O(delta^{-1} log(e/delta)) for all regular monotone functions (every weighted threshold) when all biases lie
in [delta, 1-delta] (Theorem 6.1).

Evidence: no weighted threshold found with H+/Delta above the AND/OR constant 2 + 4/ln 2 = 7.7708 (exhaustive n <= 5 with
optimized biases, 4749 random n <= 11, symmetric m <= 40, two-weight groups up to 12 + 12 coordinates with optimized biases).

Not proved: uniformity in the biases. The missing pieces are exactly (1) a normalization credit that survives blocks,
for which (LCR) of section 7 is the precise candidate, and (2) a near-dictator analysis without the bias floor
(Theorem 6.1, Case B (i) and the case split).

Next step for the fleet: prove (LCR) for weighted thresholds (or find a weighted threshold violating it); T_s and the
three-class family are mandatory test cases for any proposed credit. A natural first case is two distinct weights.

## 9. Verification log

* code/verify_tools.py (400 random thresholds, random biases): Lemma 4.1 identities and the DTC identity hold to 3e-15;
  rank functional <= 0.68 (bound 3 + ln 4 = 4.39); (E - V ln(1/V))/I <= 1.66 (bound 9.21).
* code/verify_caseB.py (1500 random thresholds, every coordinate as the pivot, 9135 cases, biases down to ~1e-5):
  the Case B inequality E_{>=2}(f) <= 4[(1-q_0)E(U) + q_0 E(V')] + 8.25[(1-q_0)Var U + q_0 Var V'] never failed (it is a
  deterministic inequality, valid for every coordinate, not only near-dictators); the identity
  sum_{j != 0} I_j(f) = (1-q_0) I(U) + q_0 I(V') holds to 9e-16; rho_j <= eps/(q_j(1-q_j)) never failed.
* code/verify_credit_cex.py: exact Fraction spectra of T_s (s = 4, 8, 10), Parseval exactly 1, credit excess and H+/Delta as in section 3.
