# The Fourier entropy-influence inequality for read-k DNF formulas and for regular functions

Status (end of 23 Sep, paper in paper/). PROVED, with explicit constants (FEI H <= C I; FEI+ H^+ <= C'(I - Var)):
- read-k DNF and CNF formulas: C = min(2.89 + 9.9k, 30 + 5.6 log2 k), C' = min(22 + 28k, 88 + 16.4 log2 k)
  (sections 1-2, 6, 19); the log k dependence matches the min-entropy bound of ACKSW;
- regular (2-monotone) functions, which contain all linear threshold functions: C = 15.1, C' = 60 (sections 3, 6);
  FEI for linear threshold functions was stated as open by Chakraborty et al. (random LTFs, 2018);
- monotone functions whose desirability preorder has width w: C = 15.1 + log2 w (section 15);
- Boolean functions of m regular functions with unrelated orders (e.g. intersections of m halfspaces):
  C = 16.5 + 8.4 ln m, C' = 66 + 31 ln m (section 8);
- unions and intersections of regular functions in which every variable is relevant to at most k of them:
  C = min(3.9 + 21.2k, 54 + 12.8 log2 k), C' = min(24 + 66k, 186 + 46.2 log2 k) (sections 13, 14, 20);
  contains the first two classes up to constants;
- AND, OR, XOR of any fan-in under every product measure: the biased FEI+ with the sharp constant 2 + 4 log2 e
  (XOR 2 log2 e) (section 12);
- hence, by O'Donnell-Tan's composition theorem, FEI for read-once formulas whose leaves are in these classes on
  disjoint variable sets and whose gates have bounded arity, or are in these classes with balanced inputs (e.g.
  iterated majorities of any odd fan-ins, constant 66).
OPEN: a k-independent constant for read-k DNFs (= FEI for all DNFs; section 19 resolves O(log k) with a
rooted-animal reference, no cover lemma needed; section 20 does the same for unions of regular functions);
biased FEI+ for threshold functions (conjectured sharp constant 2 + 4 log2 e, numerically supported with 50-digit
rechecks, section 12) which would give all read-once threshold formulas; the full conjecture. Numerically the true
constants for all these classes are about 4.

For read-k DNFs the min-entropy inequality H_inf <= O(log k) I was proved by Arunachalam, Chakraborty, Koucky,
Saurabh and de Wolf (STACS 2020), improving Shalev's result for regular read-k DNFs; Mansour's conjecture for read-k
DNFs is due to Klivans, Lee and Wan (2010). The Shannon-entropy inequality for read-k DNFs was open.

## 0. Notation

x is uniform on {0,1}^n and chi_S(x) = (-1)^{sum_{i in S} x_i}. For f: {0,1}^n -> {0,1} let g = 1 - 2f. The
spectral sample S has Pr[S = A] = P(A) = ghat(A)^2; H = H(f) = H(S) in bits, I = I(f) = E|S| = sum_i Inf_i with
Inf_i = Pr[f(x) != f(x + e_i)], and Var = 1 - P(empty) = 4 p_0 (1 - p_0), p_0 = Pr[f = 0].

A DNF formula is f = OR_{t=1}^m T_t, where T_t is satisfied exactly when x restricted to V_t equals a fixed a_t
(a conjunction of literals on the variable set V_t, V_t nonempty). It is read-k if every variable lies in at most k
of the sets V_t. No minimality or irredundancy is assumed. mu = sum_t 2^{-|V_t|}.

## 1. Two lemmas

Lemma 1 (path lemma). p_0 mu <= (k/4) I. More precisely, p_0 mu <= (1/2) sum_j Inf_j sum_{t : j in V_t} 1/|V_t|.

Proof. For a pair (x, t) with f(x) = 0, change the coordinates of V_t at which x differs from a_t one at a time, in
a fixed order of V_t. f is 0 at the start and 1 at the end, so there is a first edge (x', x' + e_j) of the path with
f(x') = 0 and f(x' + e_j) = 1, and j lies in V_t. Given this edge and t, the point x agrees with x' outside the
coordinates of V_t that precede j in the order, so at most 2^{p-1} pairs (x, t) are sent to it, where p is the
position of j. Summing 2^{-|V_t|} over pairs, each boundary edge in direction j receives at most
sum_{t : j in V_t} 2^{p_t(j) - 1 - |V_t|} <= k_j / 2. There are 2^{n-1} I boundary edges, so
2^n p_0 mu <= (k/2) 2^{n-1} I. Averaging the bound over uniformly random orders of each V_t replaces 2^{p-1} by
(2^{|V_t|} - 1)/|V_t| and gives the refined form. []

Lemma 2 (density of the spectral sample in a witnessing term). Fix i with Inf_i > 0 and let t_1, ..., t_r
(r <= k) be the terms whose variable set contains i. Let nu_i be the law of S \ {i} given i in S. For beta > 1,

    nu_i( for every s: |(T + i) cap V_{t_s}| < |V_{t_s}|/beta ) <= r max_s Pr[ Bin(|V_{t_s}| - 1, 1/2) < |V_{t_s}|/beta - 1 ].

Proof. D_i g(x) := (g(x^{i<-0}) - g(x^{i<-1}))/2 = f(x^{i<-1}) - f(x^{i<-0}) takes values in {-1, 0, 1}, and
ghat(T + i) is the T-coefficient of D_i g, so nu_i(T) = (D_i g)^(T)^2 / Inf_i. If i is pivotal at x, some term
is satisfied at exactly one of x^{i<-0}, x^{i<-1}; it must contain i, so x lies in one of the subcubes
C_s = {x : x = a_{t_s} on V_{t_s} \ {i}}. Let A_s be the pivotal points whose first such s is s. Then
D_i g = sum_s D_i g 1_{A_s}, and since A_s lies in C_s, writing x = (y, z) with y = x restricted to V_{t_s} \ {i},
    D_i g 1_{A_s} (y, z) = 1[y = a_{t_s}] Psi_s(z),   Psi_s(z) = (D_i g 1_{A_s})(a_{t_s}, z).
The factors depend on disjoint coordinates, so the squared Fourier coefficients of this piece do not depend on
T cap (V_{t_s} \ {i}): under its normalised spectral law that set is uniform over the subsets of V_{t_s} \ {i}, and
independent of the rest. By Cauchy-Schwarz, (sum_s c_s)^2 <= r sum_s c_s^2, hence for every event F,
nu_i(F) <= r max_s nu_{i,s}(F), where nu_{i,s} is the normalised spectral law of the s-th piece. The stated event is
contained, for each s, in {|T cap (V_{t_s} \ {i})| < |V_{t_s}|/beta - 1}. []

## 2. The theorem

Theorem 1. Let f be computed by a read-k DNF formula. For every beta > 2,

    H(f) <= [ 2.886 + k ( 2 + 2 beta + 2 C_beta ) ] I(f),   C_beta = sup_{m >= 1} m Pr[ Bin(m-1, 1/2) < m/beta - 1 ].

With beta = 3, C_3 = 0.9490...: H(f) <= (2.886 + 9.898 k) I(f). The same bound holds for read-k CNF formulas.

Proof. Reference measure. For a set U of terms let V(U) be the union of their variable sets, and let
q(U) = prod_{t in U} pi_t prod_{t not in U} (1 - pi_t) with pi_t = 2^{-|V_t|}. Put Q(empty) = 1 - Var and, for
A nonempty, Q(A) = Var Q_1(A) with Q_1(A) = sum_U q(U) 2^{-|V(U)|} [A subset of V(U)]. The total mass of Q is at
most 1, and Q(A) > 0 whenever P(A) > 0, because a variable that occurs in no term is irrelevant. Gibbs' inequality:

    H <= h(Var) + sum_{A != empty} P(A) log2(1/Q_1(A)).

If U covers A, then Q_1(A) >= q(U) 2^{-|V(U)|}, so log2(1/Q_1(A)) <= Lambda + 2 sum_{t in U} |V_t|, where
Lambda = sum_t log2(1/(1 - pi_t)) <= 2 mu (pi_t <= 1/2 and log2(1/(1-x)) <= 2x on [0, 1/2] by convexity).

The cover. For nonempty A let D(A) be the set of terms with |A cap V_t| >= |V_t|/beta. Call i in A sparse if no
member of D(A) contains it, and cover each sparse i by a smallest term containing it, of size w_i. Then
sum_{t in D(A)} |V_t| <= beta sum_{t in D(A)} |A cap V_t| <= beta k |A|, and

    sum_{A != empty} P(A) log2(1/Q_1(A)) <= Var Lambda + 2 beta k I + 2 sum_i w_i Inf_i nu_i(i sparse).

Lemma 2 gives w_i nu_i(i sparse) <= k max_s w_i tau(|V_{t_s}|) <= k max_s |V_{t_s}| tau(|V_{t_s}|) <= k C_beta,
with tau(m) = Pr[Bin(m-1,1/2) < m/beta - 1], because w_i <= |V_{t_s}| for every s.

The vacuum term. By Lemma 1, Var Lambda <= 4 p_0 * 2 mu <= 2 k I.

The empty set. Let alpha = min(p_0, 1 - p_0); then Var = 4 alpha (1 - alpha) lies in [2 alpha, 4 alpha]. The
edge-isoperimetric inequality gives I >= 2 alpha log2(1/alpha), and I >= Var >= 2 alpha. Hence
h(Var) <= Var log2(1/Var) + Var log2 e <= 4 alpha (log2(1/alpha) - 1) + 5.771 alpha <= 2 I + 1.771 alpha <= 2.886 I.

For CNF formulas apply the theorem to the dual function x -> 1 - f(1 - x), whose spectral law is that of f. []

Remarks. (1) The refined form of Lemma 1 improves the vacuum term to (4/ln 2) max_j (sum_{t containing j} 1/|V_t|) I,
which is small when all terms are long. (2) For monotone formulas the activation probabilities
u_t / Pr[no other term satisfied], with Harris' inequality in place of Lemma 1, also give a bound, of order k^2. (3) Where the
constant is lost: the vacuum term and the Cauchy-Schwarz step each cost a factor k, and the cover double-counts
variables lying in several dense terms. Numerically H/I and the best Gibbs bound over activation constants do not
grow with k, but the step "activate every dense term" does genuinely cost Theta(k) I (section 16: x0 & OR_k has k
dense terms through x0 while one term covers S), so an O(log k) proof must pick a minimal cover.

## 3. Regular functions

Theorem 2. Let f be a regular (2-monotone) Boolean function: after negating some inputs f is monotone and its
coordinates are totally preordered by desirability (i >= j iff f(x^{i=1,j=0}) >= f(x^{i=0,j=1}) for all x). Then
H(f) <= 15.1 I(f), with the level-entropy bound H(|S|) <= 3.8854 I proved in the paper (Lemma 1.5); a level-entropy
bound H(|S|) <= 3 I would give 14.22.

Proof. Order the coordinates by decreasing desirability and let U_i be the predecessors of i. For every assignment
z outside U_i + {i}, the points y in {0,1}^{U_i} at which i is pivotal form an antichain: if y < y' both had i
pivotal, pick j in U_i with y_j = 0 < y'_j; then f(y', x_i = 0) >= f(y + e_j, x_i = 0) >= f(y, x_i = 1) = 1 by
monotonicity and j >= i, so i is not pivotal at y'. This is the only property of threshold functions used in F5's
Lemma 2 (Sperner's theorem on the noised coordinates), and the rest of F5's proof applies unchanged. []

Regular functions include all threshold functions and, from nine variables on, functions that are not threshold
functions; they are the up-sets generated by shifted families.

## 4. Scope

Neither theorem proves FEI in general. The known proofs for classes now use three unrelated mechanisms: a rank order
with Littlewood-Offord (threshold and regular functions), composition (read-once formulas), and witness activation
(read-k DNFs, Theorem 1). Recursive ternary majority defeats every rank order; star functions of expander graphs, which
are read-twice DNFs, defeat every coordinate hierarchy; majority defeats the witness method, since each variable lies
in exponentially many minterms whose contributions to the derivative superpose coherently.

## 5. Numerical checks

Code in code/, logs in logs/. All spectra are exact (Walsh-Hadamard transform of the full truth table).
- readk_linear.py: 192 random read-k DNFs (k <= 5, n <= 16, monotone and non-monotone, not made irredundant):
  Lemma 1 holds with p_0 mu / ((k/4) I) <= 0.47 and the refined form <= 0.61; Lemma 2's ratio <= 1 (equality when
  i lies in one term, as the proof predicts); the pieces' spectral marginal on V_t \ {i} is uniform to 0.0; the Gibbs
  bound is at most 4.52 I.
- unif_control.py: negative controls for the uniformity check: the whole derivative deviates by 0.80 and a piece
  with one outside point added by 0.012, so the check can fail.
- readk_check.py, termref.py, stars.py: tribes, star functions of random regular and circulant graphs (n <= 25), and
  random monotone read-2..5 DNFs: H/I between 3.0 and 4.5; the term reference is within 0.1 to 1 of H/I.
- verify_f5.py: F5's lemmas and Theorem 2 on 590 random threshold functions and 440 random regular functions
  (n <= 13); every pivotal set is an antichain in the predecessor cube, and all lemma ratios are below 0.70.

## 6. The strengthened inequality (FEI+) and composition

Notation: H^+(f) = sum_{A nonempty} P(A) log2(1/P(A)); W(f) = sum_{|A|>=2} P(A); J(f) = sum_{|A|>=2} |A| P(A)
= sum_i Var(D_i g). Since |A| <= 2(|A|-1) for |A| >= 2, J <= 2 (I - Var), so it suffices to bound H^+ by C J.

Lemma A (every Boolean function). P({i}) log2(1/P({i})) <= (2/ln 2) Var(D_i g).
Proof: b = |E D_i g| <= E|D_i g| = Inf_i, Var(D_i g) = Inf_i - b^2 >= b - b^2, and b^2 ln(1/b) <= b - b^2
because ln(1/b) <= 1/b - 1. Sharp: f = x_1 AND NOT(x_2 ... x_w), i = 1, ratio -> 2/ln 2.

Lemma B (every Boolean function). W log2(1/W) <= 8 J.
Proof, alpha = min(Pr[f=1], Pr[f=0]). Facts: J >= sum_i Inf_i (1 - Inf_i); W <= J/2 and W <= Var <= 4 alpha;
Inf_i <= 2 alpha, so W_1 <= 2 alpha I and J >= (1 - 2 alpha) I; I >= 2 alpha log2(1/alpha).
- alpha <= 1/4: J >= I/2 >= alpha log(1/alpha) >= (W/4) log(1/W)-type bound, <= 4J (or <= 1.7 J if 4 alpha > 1/e).
- alpha > 1/4 and J >= 0.024: <= 3.2 J (split at W = 0.012).
- alpha > 1/4 and J < 0.024: a unique coordinate i* has Inf > 1 - 2 delta and ghat(i*)^2 > 1 - 3 delta. Write
  g = A + chi_{i*} B (A = E_{i*} g, B = D_{i*} g), D = 1 - B in {0,1,2}, E = {D != 0} of density eta < 3 delta.
  W <= ||A||^2 + Var(B) <= 4 eta, and J >= sum_T |T| Dhat(T)^2 >= (1/4) I(1_E) >= (eta/2) log2(1/eta) by edge
  isoperimetry, so W log(1/W) <= 4 eta log(1/eta) <= 8 J.
Numerically the worst ratio W log(1/W) / J over all functions of <= 4 variables, random functions up to 10
variables and perturbed dictators is 1.59 (logs/feiplus_lemmas.log).

Reduction. For any Q >= 0 with sum_{|A|>=2} Q(A) <= 1: H^+(f) <= (2/ln 2 + 8) J + sum_{|A|>=2} P(A) log2(1/Q(A)).

Read-k DNF (Q = the term-activation reference Q_1, beta = 3):
- vacuum W Lambda <= 2 W mu <= 4k J (if p_0 >= 1/4: mu <= kI and W I <= 1.5 J; if p_0 < 1/4: W <= 4 p_0, J >= I/2);
- dense cover 2 beta k J;
- sparse elements: w_i nu_i(E_i \ {empty}) <= max(log2 k + 2, 2k C_beta) nu_i(T nonempty), using
  nu_i(empty) <= sum_{s containing i} 2^{-(|V_s|-1)} (Cauchy-Schwarz on the witness pieces) <= 1/2 when every term
  through i has >= log2 k + 2 variables.
Total: H^+ <= (10.9 + 14k) J <= (22 + 28k)(I - Var).

Regular functions (monotone, ordered by desirability): Inf is nonincreasing along the order (Inf_i - Inf_j =
E_z[f(1,0,z) - f(0,1,z)] >= 0 for i < j), nu_i(empty) = Inf_i, and sum_i Inf_i^2 <= 1 forces i <= 3 when Inf_i > 1/2.
Hence sum_{|A|>=2} P(A) sum_{i in A} ln+(i/|A|) <= 2 L_1 J, and the rank reference Q(A) = 2^{-(|A|-1)} pi_{|A|}(A)
gives H^+ <= (2/ln 2 + 9 + log2(ea/(a-1)) + 2 a L_1 / ln 2) J < 30 J at a = 1.1087, i.e. FEI+ with C = 60.

Composition corollary. O'Donnell-Tan (arXiv 1304.1347): Theorem 1 (FEI+ composes: gates need the biased form for the
biases of their inputs, inputs need the form for the measure they see), Theorem 2 (every gate of arity a satisfies
biased FEI+ with 2^{O(a)}), Proposition 2.1 (uniform FEI+ with C implies FEI with max(C, 1/ln 2)). Inputs of the
formula read uniform variables, so uniform FEI+ for them suffices: read-once formulas of arity <= a over read-k
DNF/CNF formulas and regular functions on disjoint variable sets satisfy H <= max(22 + 28k, 60, C_a) I.
Open: biased FEI+ for read-k DNFs / regular functions (would allow them as gates).

Numerical audit of every proof component (logs/feiplus_readk.log, logs/feiplus_regular.log): read-k, k <= 6:
true FEI+ ratio <= 6.35, reduced Gibbs <= 3.64 J, vacuum <= 1.1 J (bound 4k), dense <= 8.3 J at k=6 (bound 18),
sparse <= 0.27 J, nu_i(empty)/bound <= 0.875 (bound 1). Regular/LTF (320 functions, n <= 12): influence order never
violated, rank term <= 0.32 J (bound 8.30), reduced Gibbs <= 2.62 J (bound 19.07), FEI+ ratio <= 6.11.
Compositions (AND/OR/XOR/MAJ3 of LTF and read-2 leaves): FEI+ ratio <= 6.38, H/I <= 3.65.

## 7. Toward O(log k)

In the Theorem 1 proof, the k-dependence enters through (i) the vacuum term, (ii) Cauchy-Schwarz on the <= k
witness pieces, (iii) the dense cover. (i) becomes O(1) with activation probability 2^{-|V_t|}/k (paying log k per
term of a minimal cover, <= log k per element); (ii) becomes O(log k) by splitting on whether the smallest term
through i has fewer than C log(k+1) variables (or, equivalently, via Donsker-Varadhan with D(nu_i || M_i) <= log r,
since nu_i <= r M_i pointwise for the uniform mixture M_i of the pieces). (iii) is the obstruction: when many
dense terms share a core (sunflowers with sparse petals), sum_{t in cover} |V_t| can be ~k |S| even for the
cheapest cover, and every per-element charging scheme tried fails on such configurations. The overlap-aware
sequential reference (activate terms in order with probability 2^{-|V_t \ W|}/k, W = current union) costs
<= |U| log k + 3 |V(U)| + O(vacuum) for any cover U, so O(log k) would follow from E_P[Phi(S)] <= C I with
Phi(S) = min |V(U)| over covers U of S. Numerically (logs/phicover.log, logs/kgrowth*.log): E[Phi]/I <= 2.6 on
sunflowers, hyperstars, Fano, threshold-2 and random read-k with k <= 10; the Gibbs bound with the best c in
pi_t = c 2^{-|V_t|} stays <= 4.45 I (k <= 16 on x0 AND OR_k, k <= 10 random). A proof of E[Phi] = O(I) (or
O(log k) I) is open; the coherent superposition of witness pieces can differ wildly from their mixture (e.g. for
x_c AND OR of petals, nu_c puts mass ~1 on T = empty while the mixture spreads over prefixes), so Donsker-Varadhan
alone is too lossy for non-local costs.

## 8. Boolean functions of several regular functions (arbitrary orders)

Theorem. If h_1, ..., h_m are regular (each with its own desirability order and orientation; e.g. halfspaces with
unrelated weight vectors) and F: {0,1}^m -> {0,1} is arbitrary, then f = F(h_1, ..., h_m) satisfies
H(f) <= (16.5 + 8.4 ln m) I(f). In particular FEI holds, with constant O(log m), for intersections of m halfspaces.
(The earlier corollary needed compatible orders.)

Proof. If i is pivotal for f at x it is pivotal for some h_l. Split D_i g into pieces d_{i,l} by the least such l;
the support of d_{i,l} lies in the pivotal set of i for h_l, which is an antichain in every subcube spanned by the
predecessors U_i^l of i in the l-th order. So the noise lemma and the rank-tail lemma hold piece by piece:
nu_{i,l}(F_l > u) <= min(1, B e^{-u/2}) with F_l = ln(r_l(i)/(|T cap U_i^l| + 1)), hence
E_{nu_{i,l}} e^{lambda F_l} <= B^{2 lambda}/(1 - 2 lambda). Cauchy-Schwarz gives nu_i <= sum_l nu_{i,l} (pointwise),
so for G = min_l F_l: E_{nu_i} G <= (1/lambda) ln E_{nu_i} e^{lambda G} <= (1/lambda) ln sum_l E e^{lambda F_l}
<= 4 ln m + 4 ln 2 + 2 ln B < 4 ln m + 4.93 at lambda = 1/4. Multi-order rank reference
theta_k(i) = max_l min(1, (k/r_l(i))^a): sum_i theta_k(i) <= m k a/(a-1), so ln Z_k <= k(1 + ln m + ln(a/(a-1))).
With the level entropy H(|S|) <= 3.886 I: H <= [3.886 + (1 + ln(a/(a-1)) + 4.93 a + (1 + 4a) ln m)/ln 2] I, a = 1.2.

Numerics (logs/multiorder.log): AND/OR/XOR/MAJ of 2-4 LTFs with random or opposite weight orders, n <= 12:
H/I <= 3.86; E sum min_l ln+(r_l(i)/|S|) <= 0.233 I (bound 4 ln m + 4.93); per-piece tail E F_l <= 0.737 (bound L_1 =
4.151).

FEI+ for functions of m regular functions: H^+ <= (33 + 15.3 ln m) J <= (66 + 31 ln m)(I - Var). New ingredient: if
nu_i(empty) > 1/2 then Inf_i(f) > 1/2, so some h_l has Inf_i(h_l) > 1/(2m); influences of a regular function do not
increase along its order and their squares sum to <= 1, so r_l(i) < 4m^2 and the rank cost is < 2 ln(2m) pointwise.
Hence the composition corollary also allows inputs that are Boolean functions of m regular functions (e.g. polytopes
with m facets). Numerics (logs/multiorder_plus.log): non-singleton rank term <= 0.124 J (bound 8 ln m + 9.86),
FEI+ ratio <= 5.68 for functions of 2-4 LTFs.

## 9. Toward biased FEI+ (gates of unbounded fan-in) - numerical findings, no proof

Goal: biased FEI+ for LTFs/regular functions (and read-k DNFs) with a constant independent of the biases and the
fan-in; with O'Donnell-Tan this would give FEI for read-once formulas whose GATES are threshold functions of any
fan-in (read-once threshold formulas, e.g. MAJ_101 o MAJ_101), which O'Donnell-Tan's 2^{O(arity)} does not cover.
- Adversarial bias search (logs/bfp_ltf.log): sup of H^mu[f^{>=1}] / (Inf^mu - Var^mu) over LTFs is 7.771, the same
  value as for read-k DNFs (logs/bfp_adv.log) - apparently the extreme-bias limit of a 2-input AND.
- Biased tools that DO go through: Lemma A (singletons) verbatim with sigma weights; the path lemma under product
  measures (p_0 * sum_t Pr[t sat] <= (k/4) Inf^mu, because each boundary-edge charge is mu(y) q_j(1-q_j) = mu(y)
  sigma_j^2/4); a biased Sperner/Littlewood-Offord bound mu(antichain) <= (2/sqrt(pi)) (sum_j sigma_j^2/2)^{-1/2}
  via the coupling X_j = B_j C_j (B_j ~ Bern(2 min(p_j,1-p_j)), C_j fair), which gives the noise/rank-tail lemma
  with MASS rank M_j = sum of 2 min(p,1-p) over predecessors.
- What FAILS (logs/bfp_gibbs.log): the sigma-weighted mass-rank reference Q(S) ~ sigma_S^2 prod theta: its Gibbs
  bound reaches 23 J where H^+ is 3.9 J; the excess is W log(1/W), uncompensated because when heavy coordinates are
  nearly frozen the light ones get small mass rank and full weight, so the reference overweights pairs that the
  spectrum never uses (a light coordinate is pivotal only when a heavy one flips).
- Candidate biased Lemma B (logs/bfp_lemmaB.log): W log(1/W) <= C J + sum_{|S|>=2} P(S) log(1/sigma_S^2) holds with
  C <= 1.78 on random functions, LTFs and read-2 DNFs under adversarial biases. If true in general it pays the
  non-singleton mass with the sigma weights; the remaining difficulty is that the same sigma-weight budget is then
  not available for the reference, which must still handle frozen heavy coordinates.

## 10. Exact verification of constants (logs/constants_exact.log)

Every numerical constant used in the proofs was re-checked with exact rational arithmetic or 40-digit mpmath:
C_3 = 13*299/4096 (exact, m <= 3000, Chernoff tail beyond), the slopes 9.898, 13.8 <= 14, the exponential-moment
identity B^{2 lambda}/(1 - 2 lambda), the case constants of the non-singleton-mass lemma (0.316, 3.2, 12 delta < 1/e),
and the final constants 15.1, 16.5 + 8.4 ln m, 30, 33 + 15.3 ln m. The check caught one rounding slip: with the
rounded level-entropy constant 3.886 the regular-function constant is 15.1002 > 15.1; the exact constant of the
level-entropy lemma is 3.88539, and with it the constant is 15.0996. The paper now states 2.8854 and 3.8854.

## 11. Gates of unbounded fan-in with balanced inputs

In O'Donnell-Tan's Theorem 1 a gate needs the strengthened inequality only for the product measure given by the
biases of ITS inputs. If every input of a gate is balanced, that measure is uniform, and the uniform FEI+ theorems
above apply to the gate with no arity restriction. Majority of an odd number of independent balanced bits is balanced,
so iterated majorities MAJ_{r_1} o ... o MAJ_{r_d} with arbitrary odd fan-ins satisfy FEI with constant 66 (60 for
the regular gates, 50 for the variables as read-1 DNFs), independent of the fan-ins; O'Donnell-Tan's bounded-arity
theorem gives 2^{O(r)} here. The same holds for read-once formulas of balanced weighted majorities (sgn(w.y), no
ties) and, generally, for any gate from our classes whose inputs are balanced. Numerics (logs/recmaj_k.log):
MAJ_a o MAJ_b for (a,b) up to (7,3), (3,7), (5,5): H/I <= 2.72, FEI+ ratio <= 4.0; weighted MAJ_5 o MAJ_3: FEI+ <= 4.25.

## 12. AND, OR and XOR gates of any fan-in under any product measure (proved)

Lemma (paper, Lemma 4.5). OR_m and AND_m satisfy the mu-biased strengthened inequality with C = 2 + 4 log2(e) =
7.7708 for every m and every product measure, and XOR_m with C = 2 log2(e). The constant 2 + 4 log2(e) is sharp
(OR_2 with both input probabilities -> 0).

The whole proof is one inequality: for a_1..a_m in (0,1], Z = prod a_j,
    Phi = sum_j (a_j - Z) ln(1/a_j)  <=  2 R,   R = sum_j (1 - a_j) - 1 + Z.
Appending b changes Phi by (1-b) Z ln(1/Z) + b ln(1/b) (1-Z) and R by (1-b)(1-Z); t ln(1/t) <= 1-t gives the
induction step. For OR (a_j = Pr[input j false]) the left side of the biased inequality is 2(I-Var) + 8 Z Phi / ln 2
and I - Var = 4 Z R; for XOR (a_j = nu_j^2) it is Phi / ln 2 and I - Var = R.

What it adds (corrected in the 10:5x audit): AND_m, OR_m, XOR_m are read-once trees of fan-in-2 gates, so
O'Donnell-Tan's bounded-arity theorem ALREADY covers them as gates, with their unspecified constant C_2. The lemma's
contribution is the explicit sharp constant 2 + 4 log2(e), which makes the corollary's constant explicit for
formulas over AND/OR/XOR gates: e.g. unions and intersections of any number of halfspaces on disjoint variable sets
satisfy FEI with constant 66 (not max(66, C_2)). It is not a new class of gates.

Checks (logs/andor_biased.log): Phi <= 2R on 200,000 random inputs, every float-flagged case re-decided in 60-digit
arithmetic (max exact Phi/R = 1.99999998, no violation); closed forms equal brute-force biased spectra to 5e-15;
the OR_m search maximum 7.770797 in floats is 7.770775 exactly, below 7.770780; negative control: Phi/R = 1.9999 at
a = (1-1e-4, 1-1e-4), so 2 cannot be lowered.

Threshold functions and read-k DNFs as gates (numerics, logs/bfp_ltf_exact.log, logs/bfp_adv_exact.log): the float
bias searches of section 9 reported 7.7709 and 7.7708, above 2 + 4 log2(e). Replaying them and recomputing the top
instances in 50-digit arithmetic, every one is BELOW the bound (LTFs: 7.770775 at best, 5.6e-6 under; read-k DNFs:
7.770762, 1.8e-5 under); the float excess was rounding at biases |mu| up to tanh(7). So the AND_2 extreme-bias
limit is the largest value found for LTFs and read-k DNFs under any product measure. Conjecture (numerical only):
every threshold function satisfies the biased inequality with C = 2 + 4 log2(e). With O'Donnell-Tan this would
give FEI for all read-once threshold formulas. Moderate-bias check (logs/bfp_moderate.log): with |mu_j| <= 0.5,
0.8, 0.95 the largest LTF ratios found were 6.93, 7.38, 7.70, and the unweighted-rank Gibbs bound stayed at 5.4-5.8 J.

Related literature checked 23 Sep: Kelman-Kindler-Lifshitz-Minzer-Safra's general bound is
H <= K(sum_A |A| log(|A|+1) P(A) + I) (a factor logarithmic in the LEVEL), not a factor log(1+I); Han (Combinatorica
2025) H = O(I + sum_i Inf_i log(1/Inf_i)); Gonzalez-MacManus-Pereyra (arXiv 2606.00246, 2026) FEI for delta-tribes
and separation-property classes. None covers read-k DNFs, threshold functions or unbounded AND/OR gates over them.

## 13. Read-k unions of regular functions (proved; paper Section 4, Theorem 4.1)

If h_1..h_m are regular (e.g. threshold functions) and every variable is relevant to at most k of them, then
h_1 v ... v h_m and h_1 ^ ... ^ h_m satisfy H <= (3.9 + 21.2k) I, independent of m. Contains the read-k DNF theorem
(terms are threshold functions) and the regular theorem (m = 1) up to constants; new: unions/intersections of
halfspaces with bounded overlap, read-k DNFs whose terms are threshold functions.

Proof = the read-k machinery with three substitutions:
- Path lemma for ANY union with read-k supports: p0 sum_l Pr[h_l = 1] <= (k/4) I, by resampling R_l (the
  resampled h_l is independent of x, and each single-coordinate resample flips 0 -> 1 with probability Inf_j/4).
- Activation of h_l with probability pi_l = min(Pr[h_l=1], 1/2); vacuum eps*Lambda <= 2k I.
- Witness filling: instead of the uniform fill of a term, a level inequality for functions supported on the
  pivotal set of h_l (measure Inf_j(h_l) <= 2 Pr[h_l = 1]): nu(|T cap R| <= l) <= alpha (2e ln(1/alpha)/l)^l
  (Holder + hypercontractivity), so a rarely true h_l is filled by about log(1/pi_l)/beta of its variables.
- Within an activated h_l: a Bernoulli product rank reference with a level parameter kappa_l = |A cap R_l|, and the
  per-piece rank tail from the multi-order theorem.
Constants: a = 1.44, beta = 5; K = max_l 5(l+1) phi_l(2^{-5l-4}) = 0.6624 (l = 1); coefficient of k
2 + 5 + 4.273 + 8.624 + 1.855*0.6624 = 21.125 (logs/union_constants.log, 30-digit, the monotonicity in lambda and
the maximum at l = 1 checked explicitly for l <= 399).

Numerics with the paper's parameters (logs/unionltf.log, logs/unionltf_rare.log), 75 formulas, k <= 4, up to 12
threshold functions, n <= 14: H/I <= 4.0; path-lemma ratio <= 0.955; per-piece E F <= 0.730 (bound L1 = 4.151);
level-tail quantity <= 0.293 (bound K = 0.662; it is identically 0 unless some h_l is rarely true - the rare family
was built to exercise it); the proof's bound from the choice L_A lies in [H, 37 I].

## 14. The strengthened inequality for read-k unions (proved; paper Theorem 5.4(d))

H^+ <= (11.9 + 33k) J, hence FEI+ with C = 24 + 66k, so read-k unions/intersections of regular functions can be
leaves of the composition corollary with a constant free of m. Proof: Proposition 5.3 with the union reference;
vacuum W*Lambda <= 4k J exactly as for read-k DNFs (path lemma for unions + Lemma 5.2's general facts W <= J/2,
J >= I/2 when p0 < 1/4); per coordinate E[G_j 1(T != 0)] <= 2k(a L1/ln2 + c2 K) nu_j(T != 0): either
nu_j(T != 0) >= 1/2, or Inf_j(f) > 1/2, some h_l has Inf_j(h_l) > 1/(2k), so r_l(j) < 4k^2 and Pr[h_l = 1] > 1/(4k)
and G_j = O(log k) pointwise.
Checks (logs/unionplus.log): 51 formulas; H+/J <= 3.95; W*Lambda/(kJ) <= 1.91 (proof 4); per-coordinate ratio/k
<= 1.28 (proof 19.70); the second case nu_j(0) > 1/2 was forced with dictator-like families (30 occurrences; the
first, random family never produced it) and the ratio there is 0, within the pointwise bound.
The corollary now states its constant as the largest of C_a and the Theorem 1.3 constants of the classes that occur.

## 15. Monotone functions of small desirability width (paper Remark 3.9)

The regular proof uses the order only through the antichain lemma (needs every coordinate of U_i to be at least as
desirable as i) and through sum_s theta_k(s) <= k a/(a-1). For a monotone f whose desirability preorder (refined
inside equivalence classes) has width w, take U_i = coordinates above i and r(i) = |U_i| + 1: Dilworth gives w chains,
the p-th element of a chain has r >= p, so sum theta <= w k a/(a-1), and H <= (15.1 + log2 w) I. Example: monotone
functions invariant under S_{n1} x ... x S_{nw} (OWZ proved FEI for these with a w-dependent constant).
Check (logs/widthcheck.log): 34 monotone block-symmetric functions (w <= 4 blocks, n <= 13): exact desirability
preorder, measured width <= number of blocks in every case, H/I <= 3.66, rank-reference Gibbs bound with poset ranks
>= H and <= 3.88 I, i.e. at least 11.26 below 15.1 + log2 w.

## 16. Where the k in the read-k theorem comes from (numerics, logs/densecount.log)

The number of dense terms through an element, E_{nu_i} #{t through i : |S cap V_t| >= |V_t|/3}, grows LINEARLY in k:
exactly k for x0 & OR_k (every 2-term through x0 is half filled by S = {x0}), ~0.8k for sunflowers and random read-k
DNFs, k for at-least-2-of-n. So the step "activate every dense term" genuinely costs Theta(k) I - not slack in the
estimate - while a minimal cover needs one term. An O(log k) proof must choose a minimal cover (e.g. the sequential
activation reference: activate t with probability min(2^{-|V_t minus B|}, 1/(2k)) given the union B so far, which
costs 3|V(U)| + |U| log 2k + O(I)) and prove a cover lemma E[|V(U(S))| + |U(S)|] <= C I; numerically
E[min union cover] <= 2.6 I. Not proved.

## 17. Symmetric gates under i.i.d. bias (numerics, logs/symbiased.log) and literature corrections

For a symmetric gate with i.i.d. inputs the biased coefficient on a set of size s is sigma^s a_s with
a_s = 2^{-s} E_{c~Bin(r-s,p)} [sum_j C(s,j)(-1)^{s-j} G(c+j)] (an average of s-th finite differences of the weight
profile), so the biased FEI+ ratio is computable exactly. In 80-digit arithmetic over every symmetric function with
r <= 8 and every threshold with r <= 30, at 15 biases from 1e-8 to 1 - 1e-8, the maximum ratio is 7.7707801 < 2 + 4 log2 e
= 7.7707802, attained only by AND2/OR2 at extreme bias. So LTFs, read-k DNFs and symmetric functions share the extremal
constant. A proof for symmetric gates would give FEI for iterated compositions of symmetric gates of unbounded arity
(OWZ's noise-sensitivity lemma for symmetric derivatives transfers to i.i.d. bias via unimodality of Poisson-binomial
laws; the missing piece is paying W log(1/W), which needs the negative part of sum_s s W_s log(eA/s), A = r sigma^2 -
it balances at leading order in the rare-threshold example p = r^{-1/2}, t = r/2, but a general argument is open).
Corrections from the audit: OWZ Theorem 2 already gives FEI for d-part-symmetric functions with 12.04 + log2 d (all
functions), better than Remark 3.9 on that family; OWZ Theorem 5 is the level-entropy bound H(|S|) <= 3 I for every
Boolean function, so Theorem 1.2's constant is 14.22 with it (the paper keeps its self-contained 15.1 and says so).

## 18. Symmetric gates: the precise missing inequality (reduction, not proved)

Setting: G: {0..r} -> {+1,-1} a weight profile, inputs i.i.d. with P(y_j = 1) = p, sigma^2 = 4p(1-p), A = r sigma^2.
All sets of size s carry the same biased coefficient sigma^s a_s, with a_s = 2^{-s} E_{c ~ Bin(r-s,p)} [Delta^s G(c)];
W_s = C(r,s) sigma^{2s} a_s^2 is the level weight, eps = sum_{s>=1} W_s, I = sum_s s W_s, J = sum_{s>=2} s W_s.
The biased strengthened inequality H^+_sigma = sum_{s>=1} W_s log2(1/a_s^2) <= C J splits as:
  singletons: <= (2/ln 2) J  (Lemma A, general);
  non-singletons: sum_{s>=2} W_s [ log2(C(r,s) sigma^{2s}) + log2(1/W_s) ]
     <= J + W log2(1/W) + sum_{s>=2} s W_s log2(e A / s)      (W = sum_{s>=2} W_s; Gibbs on levels >= 2 vs 2^{-(s-1)}).
So everything reduces to the BIASED UNCERTAINTY INEQUALITY
     W log2(1/W) + sum_{s>=2} s W_s log2(e A / s)  <=  C' J,
in which the second term is negative for levels above eA and must pay for W log(1/W) when the non-singleton mass W is
small. Uniform measure (p = 1/2): W log(1/W) <= 8 J (paper Lemma 5.2) and the second term is O(I) by noise sensitivity
of symmetric derivatives (OWZ Theorem 6), so this is OWZ's argument. Under bias, W log(1/W) is NOT bounded by C J
(threshold r/2 of r with p = r^{-1/2}: W log(1/W) / J ~ (log r)/2) but the levels then sit at s ~ r/2 >> eA ~ 4 sqrt(r),
and the negative term -(r/4) log r W cancels it at leading order. Numerics (logs/slicespec.log, the threshold case, where
the derivative is one slice indicator with Krawtchouk coefficients): the per-unit non-singleton cost stays <= 4.41
(r <= 60, all t, p from 1e-5 to 0.5); the rank-tail form of biased noise sensitivity holds with constant 1.44 for A > 1;
at extreme bias the spectral level does NOT reach log(1/pi) (ratio 0.06), so any proof must use the negative term.

## 19. Logarithmic dependence on k for read-k DNFs (PROVED 23 Sep, paper Theorem 2.5 / Thm 1.1)

Result: for every read-k DNF or CNF formula, H(f) <= min(2.89 + 9.9k, 30 + 5.6 log2 k) I(f), and
H^+(f) <= min(10.9 + 14k, 44 + 8.2 log2 k) J(f), i.e. FEI+ with C = min(22 + 28k, 88 + 16.4 log2 k).
Optimising beta per k gives FEI constant < 20 + 4.44 log2 k for k <= 10^6 (logs/animalconst2.log).
The dependence on k now matches the O(log k) min-entropy bound of Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf.

Where the factor k came from in Theorem 2.3: the product reference activates every term of the cover (cost |V_t| per
term), and the dense terms through one variable can number k, so sum_{t dense}|V_t| ~ beta k |S|. Numerically this is
not real (logs/mincover.log, denseunion.log, designdnf.log): the smallest union of terms covering S has
E|V(U)| ~ 1.2-2.5 I for k <= 10, even on shared-core designs built to force Theta(k) (every cover of a set containing
all private points uses every term), while the sum over dense terms grows like 1.5k I.

Two steps, in order of discovery:
1. Vacuum. Joint activation weight lam^{|U|} 2^{-|V(U)|}: sum_U lam^|U| 2^{-|V(U)|} = E_x (1+lam)^{N'(x)} (N' = number
   of terms whose variables are all 1), and Finner's inequality for read-k families gives
   log E(1+lam)^{N'} <= ((1+lam)^k - 1) mu / k. With lam = 1/k and the path lemma, Var * vacuum <= (e-1) log2 e I = 2.48 I
   (was 2k I). Joint activation alone still pays |V(U)| for the union of the dense terms (still ~k).
   Numerically the joint reference already gave bound/I ~ 4.2-5.6 flat in k (logs/jointref.log), and the
   unconditional theorem it gives is only ~(2+eps)k + O(log k) (logs/newconst_fast.log).
2. Rooted animals (the proof). Reference = output law of a random procedure: (a) roots R, each term independently with
   probability lam pi_t/(1+lam pi_t), lam = 1/k; (b) queue: for each processed term u, c_u ~ 1/((c+1)(c+2)), a uniform
   multiset of c_u variables of V_u, and for each a uniform term through it (prob >= 1/k); (c) s ~ 1/(s(s+1)) and a
   uniform s-subset of V(U). For S: dense terms D(S) (>= 1/beta of the term in S), a MINIMAL subfamily U_d covering the
   non-sparse elements (|U_d| <= #non-sparse), a smallest term t_i for each sparse element; U = U_d u {t_i}, |U| <= |S|;
   components of the overlap graph on U, one root each (roots pairwise disjoint), BFS trees. Costs: roots
   sum(log k + |V_r|) <= |R| log k + beta s + W; children c_u log k and multisets via log-sum over
   V_tot <= beta k s + W; subset log C(|V(U)|, s) <= s log(e beta k) + ...; all logarithmic in k except the roots, which
   are disjoint. Per set: log(1/Q1(S)) <= Lambda_lam + s K1 + kappa W, K1 = log k + beta + 7.055 + log(beta k+1) + log(beta k).
   Sparse: E W <= M_beta(k) I with M_beta(k) = sup_w min(w, k T_beta(w)) <= max(1/D_beta, 1 + ln k/D_beta) (Chernoff),
   i.e. the Cauchy-Schwarz factor k of the witness lemma costs only log k because the tail is exponential.
   Constant: 11.384 + beta + log k + log(beta k+1) + log(beta k) + kappa M_beta(k); beta = 8 gives 30 + 5.6 log2 k.
Checks: exact evaluation of the run-probability bound on 28 random read-k formulas (k <= 10, n = 12, 14): bound/I in
[4.5, 8.4], always >= H/I, run probabilities sum <= 0.12 (logs/animalref.log). Per-set audit (logs/animalaudit.log):
24 fresh formulas incl. shared-core designs and non-monotone terms, 4.25 million sets, min of s K1 + kappa W - L_run
= 7.38 >= 0, |U| <= |S| asserted on every set, H <= bound on every formula.
Open: a k-independent constant = FEI for all DNFs (a DNF with m terms is read-m). On graph DNFs
OR_{uv in E}(x_u and x_v) of random k-regular graphs, H/I ~ 3.9-4.4 and DECREASES with k (logs/graphdnf.log), while
the product reference's vacuum grows ~0.55k: the gap between the method and the truth is still there.
The same device may take Theorem 4.1 (unions of regular functions) from 3.9 + 21.2k to O(log k); not done.

## 20. Logarithmic dependence on k for unions of regular functions (PROVED 23 Sep, paper Theorem 4.5)

Result: if h_1..h_m are regular and every variable is relevant to at most k of them, the union and the intersection
satisfy H <= min(3.9 + 21.2k, 54 + 12.8 log2 k) I and H^+ <= min(11.9 + 33k, 93 + 23.1 log2 k) J
(FEI+ constant min(24 + 66k, 186 + 46.2 log2 k)). Contains section 19 up to constants (terms are LTFs) and the regular
theorem (k = 1). Optimising (a, beta) per k: < 61 for k <= 10, < 108 for k <= 1000 (logs/unionconst.log).

Reference = output law of: (a) roots, each l with prob lam pi_l/(1+lam pi_l), lam = 1/k, pi_l = min(Pr[h_l=1],1/2);
(b) queue: for each l, s ~ 1/(s(s+1)), an s-subset B_l of R_l from the LEVEL-NORMALISED rank law
theta_s(i) = min(1,(s/r_l(i))^a) / e_s(theta_s) (log e_s <= s log(ea/(a-1))), then c children through a multiset of
elements of B_l and an index among <= k functions; (c) output the union of the B_l.
Run for A: tau(j) = argmin_l G_j(l), G_j(l) = (a/ln2) F^j_l + log(1/pi_l)[l not dense] (as in Thm 4.1, c_2 = 1);
A_l = tau^-1(l); DIGRAPH l -> l' iff A_l meets R_l'; one root per INITIAL strongly connected component; BFS forest.
Key facts: (1) roots have pairwise disjoint A cap R_r (an element in two roots' supports forces an edge into an
initial component from outside, or two roots in one component); so dense roots cost <= beta |A| and non-dense roots
are charged to their tau-preimages; (2) level-normalising the rank law at |A_l| instead of kappa_l = |A cap R_l|
removes the double-counted Bernoulli normalisation; the price is sum_l |A_l| log(kappa_l/|A_l|) <= |A| log k by the
log-sum inequality (sum_l kappa_l <= k|A|); (3) E_nu G_j via tails: nu_j <= sum_s nu_{j,s}; F has tail B e^{-v/2}
(multi-order proof), non-density has tail g(b) <= 2^{-4.04 - 0.44 b} at beta = 10 (level lemma; the log of
2^{0.44b} phi_l(2^{1-b}) decreases on each (10(l+1),10(l+2)], left-end values -4.6, -4.04, -4.26, -4.56, ...), so
the Cauchy-Schwarz factor k costs only log k: E G <= (4a/ln2)(ln(2kB)+1) + (2/gamma)(log2 k + log2 e).
Per set: log(1/Q1(A)) <= Lam + |A|((1+a) log k + beta + 9.77) + sum_j G_j. Vacuum (log e) I by the union path lemma.
A scar from the derivation: int_0^inf min(1, M 2^{-gam v}) dv = (ln M + 1)/(gam ln 2) only for M >= 1; for M < 1
it is M/(gam ln2), and using the first form made C(1) negative-ish (39.8 instead of 53.7). Use log2^+.
Checks (logs/unionanimal.log, beta = 10): 13 random read-k unions of threshold functions, k <= 5, n = 10, 12:
bound/I 4.9-7.9 (>= H asserted), Kraft <= 0.17, per-set inequality slack >= 13.9 on every set.

## 21. The biased form is a statement about expected mixed derivatives (identity proved; theorems still open)

Identity (checked to 3e-16 on 40 random functions, logs/uform.log). For g = 1 - 2f on {0,1}^n and any product
measure mu (q_j = mu(x_j = 1), sigma_j^2 = 4 q_j (1 - q_j)):
    P_mu(A) = sigma_A^2 4^{-|A|} (E_{x outside A} d_A g)^2,   d_A g = sum_{y subset A} (-1)^{|A minus y|} g(1_y, x_{-A}).
Proof: E_{x_j}[h(x_j) phi_j(x_j)] = (sigma_j/2)(h(1) - h(0)) coordinate by coordinate. Consequences:
- log(sigma_A^2 / P_mu(A)) = log(4^{|A|} / (E d_A g)^2) >= 0 for every set; the left side of the biased inequality is
  sum_A P_mu(A) log(1/u_A) with u_A = P_mu(A)/sigma_A^2 = (E d_A g / 2^{|A|})^2 in [0,1]. There is no counting in it:
  the sigma factor absorbs "which set", and what remains is the size of an expected mixed derivative.
- u_A depends only on the biases OUTSIDE A.
- Monotone DNF: E d_A f = F(A) = E[c(A; T(x))] with T(x) = terms whose part outside A is satisfied and
  c = sum_{nonempty J subset T} (-1)^{|J|+1} 1[union of traces = A] (0 as soon as some term is satisfied outside A).
  So biased FEI+ for monotone DNFs <=> sum_A P_mu(A) log(1/F(A)^2) <= C'(I - Var) (the 2(|A|-1) part is exact).
  The same formula holds for the uniform measure, so Theorem 5.4(a) says sum P log(1/F_unif^2) = O(log k)(I - Var).
- Symmetric gate, i.i.d. bias: u_s = 4^{1-s} (E_{c ~ Bin(r-s,p)} Delta^s G(c))^2; for Thr_{t,r} the expected difference
  is +-(backward difference of order s-1 of the Bin(r-s,p) pmf at t-1). The report's section 18 inequality is this
  written as level entropy + log(C(r,s) sigma^{2s}); in the u-form the level entropy never appears.
- Chain rule: LHS^+ = H(S) - P(0)log(1/P(0)) - sum_i Inf_i log(1/sigma_i^2) <= sum_i sigma_i^2 rho_i log(e/rho_i),
  rho_i = mu(i pivotal). Frozen coordinates (small sigma) cost nothing here; the difficulty is small rho_i, exactly as
  small influences in the uniform case. (Not enough for FEI+: a dictator gets sigma^2 log e against 0.)
Where cover references break (the concrete obstruction): OR_m with q -> 1. Var = 4(1-q)^m, the spectrum sits on
A = [m] with log(sigma_A^2/P) = 2m - 2, but a term-activation reference puts mass ~ lam m (1-q) on singletons and
the Gibbs normalisation Var log(Q(nonempty)/Var) costs Var (m-1) log(1/(1-q)) >> I - Var = 4(m-1)(1-q)^m. The spectrum
here is that of ONE rare clause (all inputs false), not of m terms; any working reference must put total mass ~Var on
nonempty sets and then include each variable with probability ~1 (the sigma gains of the later elements repay the
first element's log(1/Var)). A read-k DNF with frequently satisfied terms mixes the term regime and this clause regime.
Rare-literal regime (every literal true with probability <= 1/2): the biased down-set isoperimetry from entropy
tensorisation, p0 log(1/p0) <= (1/4) sum_i Inf_i log(1/(1-q_i))/q_i <= (1/2) I_mu, is as good as the uniform one, and
Inf_i <= 2 p0 when p0 is small; so the normalisation is paid when p0 < 1/4. For p0 >= 1/4 one needs Q(|A|>=2) <= C J
for the reference (then W log(Q/W) <= (C/2 + 0.531) J); the A-driven BFS reference (roots with prob lam pi_t, children
only through elements already in A with prob pi_{V_t minus B}/(2k), inclusion of each new variable with prob 1 - pi_j)
pays each element's rarity once, which fixes the multiplicity problem of independent activation (the star with a rare
centre charges (m-1) log(1/pi_c) otherwise). Not finished: Q(|A|>=2) <= C J is not proved.
Random-restriction view (for the record): with q_j <= 1/2, x = z AND b (z uniform, b_j ~ Bern(2 q_j)) reproduces the
identity above and gives P_mu(A) <= 2^{|A|} E_b P_unif(A; g_b); the Jensen gap (E_b w)^2 vs E_b w^2 (sign changes
of the restricted coefficients) is what prevents a direct transfer from the uniform theorems.

## 22. The martingale (first-element) form of the biased inequality; a reference that looked bounded and is not

Exact identity (any Boolean f, any product measure, any fixed order of the coordinates). Group the nonempty sets by
their first element i, A = {i} u B with B among the later coordinates, and let psi_i(x_{>i}) = E_{x_{<i}}[f(x^{i<-1}) -
f(x^{i<-0})] (for monotone f: the probability that i is pivotal given the later coordinates). Then
P_mu({i} u B) = sigma_i^2 psi_i~(B)^2, and
    LHS+ = sum_i sigma_i^2 sum_B psi_i~(B)^2 log(sigma_B^2 / psi_i~(B)^2),
    I - Var = sum_i sigma_i^2 I_mu(psi_i),      J = sum_i sigma_i^2 (I_mu(psi_i) + Var_mu(psi_i)).
(psi_i phi_i is the i-th reverse martingale difference of f.) For a regular f in desirability order, psi_i is bounded by
the biased Littlewood-Offord constant of the predecessors, ~ (sigma^2-mass of the predecessors)^{-1/2}; psi_1 is Boolean.
First-element reference (logs/firstel.log, firstel2.log): Q(A) = V_i R_i(B), V_i = sigma_i^2 E psi_i^2 (exact),
R_i(empty) = 1 - omega_i (exact), and for B != empty a sigma-weighted mass-rank law over the later coordinates at level |B|.
No normalisation is lost (Q sums to Var). Adversarial search over 1,500 LTFs (n <= 7, biases to 1 - 1e-6), plus families
up to n = 9: the Gibbs bound stays <= 15.9 J (true LHS+ <= 3.89 J, the AND_2 extreme). BUT it is not bounded:
F = 1[3y1 + 2y2 + y3 >= 4] with y2 frozen at 1 - eps gives Bd/J = 4.2, 5.1, 6.0, 7.5, 8.9 at eps = 1e-2, 1e-4, 1e-6, 1e-9,
1e-12 (logs/firstel_probe.log) while LHS+/J stays 3.11: growth ~ (1/4) log(1/eps). Mechanism: given first element 1, the
non-singleton part is caused by the rare flip of the frozen successor 2 (B = {2} and {2,3}, each ~ eps/4), but the level-1
reference is dominated by the active successor 3 (Z_1 ~ 1), so the sigma-gain of the frozen element does not repay
log(1/omega_1). A slow logarithm fooled a 1,500-instance adversarial search: probe the one-parameter limits, not only the
random ones. What fixes this instance: choose the successor that carries the variance with probability proportional to
its influence on psi_i (cost log(I(psi)/Inf_j(psi)) + log(sigma_j^2), which cancels log(E psi^2 / Var psi) up to O(1));
what remains unproved is the combination of that choice with the rank structure (small relative perturbations of a
fractional psi_i need active predecessors, which also make V_i small by the rank tail). Not finished.

## 23. Unions of Boolean functions of M regular functions (PROVED 23 Sep, paper Theorem 4.6)

If every h_l is a Boolean function of at most M regular functions (orders arbitrary) and every variable is relevant to
at most k of the h_l, the union and the intersection satisfy H <= (54 + 12.8 log2 k + 6.8 log2 M) I and
H+ <= (93 + 23.1 log2 k + 12.6 log2 M) J. Example: unions of polytopes with M facets, each variable in <= k of them.
Proof = Theorem 4.5 with (i) theta^l_s(i) = max over the M orders (log Z <= s log(eMa/(a-1))), (ii) F^j_l = min over the
orders, (iii) the piece d_s split further by the least regular function for which j is pivotal (<= M pieces, rank tail
M B e^{-v/2}); the level lemma and the union path lemma are unchanged (they hold for arbitrary h_l). Constant
53.7 + 12.75 log k + (1 + 4a) log M; for H+ the second case uses Inf_j(h_{l,r}) > 1/(2kM), r < 4k^2 M^2.
Check (logs/unionmulti.log): 22 random read-k unions of intersections of 2-3 threshold functions, k <= 3, n = 10, 12:
bound/I 4.1-7.2 (>= H asserted), Kraft <= 0.151, per-set inequality with the extra log M holds on every set, slack >= 13.6.
Literature note (23 Sep): CKLS16 proves FEI for read-once formulas over AND/OR/XOR/NOT (not "bounded arity"); the paper's
introduction now says so.

## 24. Read-k unions of arbitrary w-juntas; a hybrid reference for biased threshold functions (evidence only)

Corollary of Theorem 4.6 (in the paper after it): a function of w variables is a function of its w dictators, which are
regular, so read-k unions of ARBITRARY functions of <= w variables satisfy H <= (54 + 12.8 log2 k + 6.8 log2 w) I.
Check (logs/unionjunta.log): 15 read-k unions of random truth tables on <= 5 variables, k <= 3, n = 10, 12: bound/I
4.0-7.5 (>= H asserted), Kraft <= 0.203, per-set slack >= 14.77 including the log w term.

Hybrid first-element reference (hybrid.py): as in section 22 but for B != empty a mixture over kappa of product laws
over the successors with inclusion r_j = min(1/2, max(sigma_j^2 theta_kappa(M_j), c Inf_j(psi_i)/Var(psi_i))), c = 1/2.
The influence branch lets a frozen successor that carries the variance of psi_i be included with probability ~1/2, so
its sigma-gain repays log(1/omega_i). Results: the probe of section 22 is FLAT (3.71 J at eps = 1e-2 ... 1e-12, true
3.11 J); four other frozen families flat at <= 4.10 J; lexicographic weights with frozen coordinates, majority-7 with a
frozen input, frozen predecessors + active successors: flat, <= 4.14 J; i.i.d. thresholds t/n (n = 5, 7) at extreme
bias: flat where float64 is reliable (the p -> 1 side loses precision beyond 1e-6; by the symmetry t <-> n+1-t, p <-> 1-p
it duplicates the reliable side); two adversarial searches (2,000 LTFs, biases to 1 - 1e-8): max 6.11 J (true <= 3.89 J).
Exact rewriting used for any proof: Bd = sum_i P({i}) log(sigma_i^2/P({i})) [<= (2/ln2) J, Lemma A]
+ sum_i sigma_i^2 K_i, K_i = sum_{B != empty} psi_i~(B)^2 log(sigma_B^2 / (Var(psi_i) R'_i(B))). What a proof still
needs: the per-first-element term Var(psi_i) log(1/Var(psi_i)) is repaid by gains of frozen successors (numerically),
but for late first elements with smooth fractional psi_i (many active predecessors) it must be charged across first
elements through the biased Littlewood-Offord bound psi_i <= B / sqrt(M_i); that lemma is not proved. So: a candidate
reference with strong evidence, not a theorem.

## 25. Threshold gates with inputs of equal bias (PROVED 23 Sep, paper Theorem thm:threshold) and the credit mechanism

Theorem. For every r, every 1 <= t <= r and every q in (0,1), the symmetric threshold T_{t,r} satisfies, under the
product measure with all biases equal to q,
    sum_{A != empty} P(A) ln(sigma_A^2 / P(A)) <= 11.49 I      (nats),
and hence the biased strengthened inequality (O'Donnell-Tan) with C = 66.4 (bits, right side I - Var). With the
composition theorem this gives FEI with constant 66.4 for iterated threshold functions T_{t1,r1} o ... o T_{td,rd}
with arbitrary thresholds and fan-ins (the bias drifts from level to level; O'Donnell-Tan's own bound is 2^{O(r)}),
and for read-once formulas whose threshold gates have inputs of equal bias.

Proof, in four pieces.
1. Symmetry: P(A) = W_k / C(r,k), so the left side is sum_k W_k ln(1/W_k) + sum_k W_k ln(C(r,k) sigma^{2k}); the level
   entropy costs V ln(1/V) + I, and C(r,k) <= (er/k)^k leaves sum_k k W_k ln(Lambda/k), Lambda = r sigma^2.
2. Rank tail (Lemma thr-rank): sum_k k W_k ln+(Lambda/k) <= 4.85 I. The derivative of T is the indicator of a level
   set (an antichain); resampled coordinates are written z = u AND b (q <= 1/2) or u OR b, so the free coordinates are
   uniform bits and Sperner applies; the number of free coordinates is Bin(r-1, 2 eta min(q,1-q)), whose mean is at
   least eta Lambda / 2. This is the uniform rank tail with |R| replaced by the sigma^2-mass of R.
3. Credit (Lemma thr-credit): V ln(1/V) <= I ln+(4 rho/V) + 4.64 I. Chain rule for relative entropy:
   ln(1/alpha) = D(mu_A || mu) = TC(mu_A) + sum_j D(mu_A^(j) || mu_j). The marginal terms are bounded for ANY monotone
   function under ANY product measure: alpha D(mu_A^(j) || mu_j) <= (Inf_j/4)(1 + ln(1 + rho_j/alpha)). The total
   correlation is bounded by the tilt R to mean t: TC <= D(mu_A || R) <= ln(1/R(N=t)) <= (1/2) ln(8v), v = t(r-t)/r,
   and the same tilt gives I/alpha >= 4 v R(N=t) >= sqrt(2v); so alpha TC <= (2/e) I.
4. Assembly: if 4m <= Lambda (m = I/V) the rank tail pays; otherwise ln(Lambda/k) = -ln(4m/Lambda) + ln(4m/k) and the
   negative part is exactly the credit. Total 2 + 4.85 + 4.64 < 11.49. For 2 <= t <= r-1 the pivotal probability is an
   interior binomial value, rho <= 1/2, so J >= I/2 and I - V >= I/4; t in {1, r} is Lemma andor.
Exact checks (logs/thr_check.log, 50 digits, all r <= 12, all t, 22 biases incl. 1e-30 and 1 - 1e-30, plus 150 random
13 <= r <= 40): left side / I <= 2.94 (bound 11.49); rank ratio <= 1.14 (4.85); credit quantity <= 0.68 (4.64);
alpha TC / I <= 0.25 (2/e); marginal bound ratio <= 0.99 (1); chain identity to 1e-49; rho <= 1/2 for interior t; the
largest ratio to I - V is 7.7708 bits = 2 + 4 log e, attained by OR_2 as q -> 0.

Where this stops, measured.
- The credit inequality V ln(1/V) <= sum_i Inf_i ln+(c rho_i / V) + C I is FALSE for general Boolean functions: the
  disjunction of s disjoint pairs with every bias s^-2 gives ratios 0.52, 1.08, 1.47, 1.56, 1.64 for s = 2..6
  (logs/isoper3.log); the reason is the total correlation of mu_A (which pair fired), ~ ln s, against I/alpha ~ 8.
  For all functions with n <= 5 (logs/isoper2.log, isoper_adv_r1/r2.log) the ratio stays <= 1.25, for threshold
  functions with n <= 12 <= 1.43 (logs/isoper_ltf.log), and alpha TC(mu_A) <= 0.24 I on 3,000 linear threshold
  functions with n <= 13 and biases down to 1e-12 (logs/tc_test.log). So for all LTFs under all product measures the
  missing pieces are: (a) the TC lemma alpha TC <= C I for LTFs (the tilt bound TC <= ln(Chernoff/alpha) holds for any
  LTF; what is missing is the anti-concentration of w.x at theta under the tilt, relative to I/alpha); (b) the
  sigma^2-rank tail for regular functions (sketch: antichain lemma + z AND b, rank r_sigma(i) = sum_{j<=i} sigma_j^2);
  (c) the J-version (near-dictator regime), since the biased strengthened inequality has I - Var on the right.
- Thresholds under arbitrary product measures: section 26 (paper Proposition prop:thr-general) proves the weak form
  (I on the right) with constant 26.3 nats; the strengthened form (I - Var on the right) does not follow from it in the
  regime where the other inputs are nearly deterministic and one input carries almost all of the influence.

Lean. lean/FEIAndOr.lean checks, in Lean 4 (v4.33.1) with Mathlib, the core inequality of Lemma andor:
for a_1..a_m in (0,1], Z = prod a_j: sum_j (a_j - Z) ln(1/a_j) <= 2 (sum_j (1 - a_j) - 1 + Z) (theorem
FEIAndOr.Phi_le_two_R, with Phi_eq identifying Phi with the sum); lean.exe exit 0, no sorry (lean/FEIAndOr.check.txt).
lean/FEISubadd.lean checks the subadditivity bound used in section 27: with phi s x = x log(s/x), for s > 0 and
a^2, b^2 <= s, phi s ((a+b)^2) <= 2 phi s (a^2) + 2 phi s (b^2) + 2 a^2 + 2 b^2 (theorem FEISubadd.subadd); lean.exe
exit 0 with no warnings, and #print axioms lists only propext, Classical.choice, Quot.sound (lean/FEISubadd.check.txt).

## 26. Threshold gates under arbitrary product measures; read-once formulas of depth d (PROVED 23 Sep, paper Proposition prop:thr-general, Lemma lem:weak-compose, Corollary cor:depth)

Proposition. For every r, every 1 <= t <= r and every product measure mu on {0,1}^r with biases q_j in (0,1),
    sum_{A != empty} P_mu(A) ln(sigma_A^2 / P_mu(A)) <= 26.3 I_mu(T_{t,r})      (nats),
with I_mu, not I_mu - Var_mu, on the right (the weak biased form).

Proof, in three pieces (notation: sigma_j^2 = 4 q_j (1 - q_j), Lambda = sum_j sigma_j^2, rho_j = mu(N_{-j} = t-1),
Inf_j = sigma_j^2 rho_j, V = Var, m = I/V, pi_j = Inf_j / V).
1. Gibbs on each level k against the weights prod_{j in A} theta_k(j), theta_k(j) = max(sigma_j^2 min(1, k/Lambda), 4 pi_j).
   Then sum_j theta_k(j) <= k + 4m, so ln Z_k <= k + 4m, and ln(sigma_j^2 / theta_k(j)) <= ln+(Lambda/k) - ln+(4 rho_j / V)
   (min(a, b) <= a - (-b)^+ for a >= 0). With the level entropy V ln(1/V) + I this gives
   LHS <= V ln(1/V) + 6I + sum_j I'_j - sum_j Inf_j ln+(4 rho_j / V),   I'_j = sum_{A containing j} P(A) ln+(Lambda/|A|).
2. Rank terms, one coordinate at a time: I'_j = Inf_j E_{nu_j} ln+(Lambda/(|T|+1)), nu_j(T) = P(T + {j}) / Inf_j. The
   Sperner argument of Lemma thr-rank runs unchanged except that a resampled coordinate i is free with probability
   2 eta min(q_i, 1-q_i) >= eta sigma_i^2 / 2, so the number F of free coordinates is a sum of independent indicators
   with mean >= eta Lambda / 4 (Lambda > 2), and E[1/(F+1)] <= 1/E F for such sums. Hence
   nu_j(|T| <= K) <= 3 sqrt(12/pi) (K/Lambda)^{1/2} and sum_j I'_j <= (2 ln(3 sqrt(12/pi)) + 2) I < 5.54 I.
3. Credit: V ln(1/V) <= sum_j Inf_j ln+(4 rho_j / V) + 14.7 I. The marginal bound of section 25 holds as stated. When
   alpha < 1/4, after negating all inputs, A = {N >= t} with t > E_mu N: otherwise Hoeffding's comparison with the
   binomial (Ann. Math. Statist. 1956, Theorem 4) and the binomial median (Kaas-Buhrman 1980) give mu(A) >= 1/2. Tilt
   to R with dR/dmu proportional to exp(lambda N), E_R N = t: TC(mu_A) <= ln(1/R(N=t)); t is a mode of N under R
   (Darroch 1964); Stein's identity E_R[(y_j - R_j(1)) h(N)] = R_j(1) R_j(0) E_R[h(N_{-j}+1) - h(N_{-j})] with
   h = 1[. >= t] gives I/alpha >= 4 E_R (N-t)^+ = 2 E_R |N-t| >= 2v / sqrt(1+3v), v = Var_R N (fourth moment
   <= v + 3v^2 and Hoelder). For v <= 1/2: R(N=t) >= 1 - v and alpha TC <= (ln 2) sqrt(2.5) I < 1.1 I. For v > 1/2:
   Chebyshev at radius ceil(2 sqrt v) gives R(N=t) >= 3/(4(4 sqrt v + 3)) and alpha TC <= psi(v) I with
   psi(v) = ln((16 sqrt v + 12)/3) sqrt(1+3v)/(2v), decreasing on [1/2, oo), psi(1/2) = 3.242. So 4 alpha TC <= 13 I,
   and 1 + ln 2 + 13 < 14.7.
Total 6 + 5.54 + 14.7 < 26.3 (26.3 / ln 2 < 38 in bits).

Lemma (weak composition). F = G(f_1, ..., f_k) on disjoint variables, mu the product measure with mu(y_i = 1) =
Pr[f_i = 1]. If sum_{A != empty} P_mu(A) log(sigma_A^2 / P_mu(A)) <= C I_mu(G) and H+(f_i) <= D I(f_i) for all i, then
H+(F) <= (C + D) I(F). From the exact recursion of the O'Donnell-Tan composition formula,
    H+(F) = sum_{A != empty} P_mu(A) log(sigma_A^2 / P_mu(A)) + sum_i (Inf_i^mu(G) / sigma_i^2) H+(f_i),
    I(F)  = sum_i (Inf_i^mu(G) / sigma_i^2) I(f_i),
and Inf_i^mu(G) = (Inf_i^mu(G) / sigma_i^2) Var(f_i) <= (Inf_i^mu(G) / sigma_i^2) I(f_i). The recursion is checked
exactly (40 digits) on three compositions in logs/compose_check.log (both sides agree to every printed digit).

Corollary. If f is computed by a read-once formula of depth d over AND, OR, XOR and threshold gates T_{t,r} of any fan-in,
with negations, then H(f) <= (38 d + log e) I(f). Every gate satisfies the weak form with C = 38 under every product
measure (the proposition; Lemma andor for AND/OR/XOR), a literal has H+ = 0, and H(f) <= H+(f) + Var(f) log e.
O'Donnell-Tan Theorem 3 gives a constant 2^{O(k)} for gates of arity at most k, independent of the depth; here the
constant is linear in the depth and independent of the fan-ins. When the inputs of every threshold gate have a common
bias, section 25 and the O'Donnell-Tan composition theorem give 66.4 with no dependence on d.

Checks (50 digits, random threshold gates with unequal biases, biases down to 1e-14 and up to 1 - 1e-14).
logs/thr_general_proof.log audits each piece of the proof: the per-level Gibbs bound, evaluated exactly, is never below
the left side; rank sum / I <= 0.78 (bound 5.54); Gibbs bound / I <= 2.09; left side / I <= 2.03 (bound 26.3); credit
quantity / I <= 0.12 (bound 14.7); alpha TC / I <= 0.17 (bound 3.25). logs/thr_general.log (1,200 gates, r <= 9) looks
at the strengthened form: left side / (I - V) <= 7.771 bits (= 2 + 4 log e, the AND_2 limit as both biases tend to 1);
left side / I <= 2.08; the J-form credit ratio (W ln(1/W) - sum_i J_i ln+(4 J_i / (sigma_i^2 W))) / J <= 0.156. So the
strengthened biased form for thresholds under arbitrary product measures holds with room to spare in every computed
case; the proof of the proposition does not give it, because I_mu - Var_mu can be much smaller than I_mu when the other
inputs are nearly deterministic and one input carries almost all of the influence.

## 27. The strengthened biased inequality for all threshold gates; FEI for read-once threshold formulas of any depth (PROVED 23 Sep, paper Theorem thm:thr-strong, Corollary cor:thr-formula)

Theorem. For every r, every 1 <= t <= r and every product measure mu on {0,1}^r,
    sum_{A != empty} P_mu(A) ln(sigma_A^2 / P_mu(A)) <= 263 J <= 526 (I_mu - Var_mu)      (nats),
J = sum_{|A|>=2} |A| P_mu(A); in bits the constant is 760. With the O'Donnell-Tan composition theorem:
H(f) <= 760 I(f) for every read-once formula over threshold gates T_{t,r} (and XOR gates) of any fan-in and any
depth, negations allowed. Corollary cor:depth (38d + log e) is smaller for d <= 19.

Proof. Notation of section 26; J_j = sigma_j^2 rho_j (1 - rho_j), so J = sum_j J_j (the derivative d_j has mean
rho_j and P(B + {j}) = sigma_j^2 d_j~(B)^2), I - V >= J/2, and the singletons contribute
sum_j 2 sigma_j^2 rho_j^2 ln(1/rho_j) <= 2J.
Case A, every rho_j <= 9/10: J >= I/10 and Proposition prop:thr-general gives 26.3 I <= 263 J.
Case B, rho_{j0} = max_j rho_j = 1 - eps with eps < 1/10 (after negating, q = q_{j0} <= 1/2). The other inputs are
nearly deterministic: resampling every coordinate (the Sperner argument with eta = 1) gives
mu(N' = k) <= (2/(pi L'))^{1/2}, L' = sum_{i != j0} min(q_i, 1-q_i); this forces the likely configuration of the others
to sit at N' = t-1, then eps >= L'(1 - L') forces L' <= 1.128 eps and Lambda' <= 4.51 eps. Up-type coordinates
(likely 0) have rho_i in [0.44, 1 - eps], so J_i >= 0.9 eps sigma_i^2; down-type ones have rho_i in [0.887 q, 0.56],
so J_i >= 0.49 q sigma_i^2. Sets containing j0: Gibbs per level against sigma_B^2 with e_k <= Lambda'^k <= (5.02 U_d)^k
gives <= 2.5 J_{j0}. Sets avoiding j0: T = u + y_{j0}(1 - u - v) with u, v the up/down deviation events, so the
coefficient is 2(1-q) u~(A) - 2q v~(A); |u~|, |v~| <= sigma_A/2, and |u~(A)| <= L_U sigma_A for A inside the
down-types (E[u | y_D] <= P(Z_U >= 1)), likewise for v; a subadditivity bound for x ln(s/x), the log-sum inequality
on four families (lambda = 1, 4 L_U^2, q^2, 4 q^2 L_D^2) and the sigma^2-masses (Lambda_U(e^{Lambda'} - 1),
(Lambda_D^2/2) e^{Lambda_D}) give 22.3 eps Lambda_U + 2.0 q Lambda_D <= 24.9 J_U + 4.1 J_D. Total <= 26.9 J.

Audit (logs/caseB_check.log, 50 digits, 1,600 thresholds with r <= 10, half built to land in case B; 824 case B,
776 case A): L'/eps <= 1.046 (proof 1.128); Lambda'/eps <= 4.06 (4.51); likely configuration at t-1 in every case-B
instance; sets containing j0 <= 1.568 J_{j0} (2.5); J_U ratio >= 0.904 (0.9); J_D ratio >= 0.502 (0.49); sets avoiding
j0 at most 5.9 pct of the bound used for them; left side <= 2.69 J in case B (26.9) and <= 2.03 I in case A (26.3).
logs/thm513_constants.log recomputes the 35 numerical constants of the proof from the inequalities that define them
(0 failures). The subadditivity bound for phi_s is checked in Lean (lean/FEISubadd.lean, section 25).
The true constant is far below the proof's: the largest ratio of the two sides found for thresholds under product
measures is 2 + 4 log e = 7.7708 bits (logs/thr_general.log), attained by OR_2 / AND_2 at extreme bias.

Two exact identities found on the way (checked, not used in the final proof).
- Per-coordinate form. Assigning each A with |A| >= 2 to a uniformly chosen element gives
  sum_{|A|>=2} P(A) ln(sigma_A^2/P(A)) = sum_j sigma_j^2 Psi(d_j),  Psi(d) = sum_{B != empty} (d~(B)^2/(|B|+1)) ln(sigma_B^2/d~(B)^2)
  (logs/slice_damped.log: agreement to 1e-41 on three thresholds). So the strengthened form for thresholds follows from
  the damped slice inequality Psi(d) <= C Var(d) for d = 1[N = s]; numerically Psi/Var <= 2.12 on 1,200 random slices
  (logs/slice_damped.log) and <= 1.35 on a two-route adversarial family (logs/slice_adv.log). The plain Gibbs bound
  with reference sigma_B^2 gives <= 1.11 Var when rho >= 1/2 but fails (13.6) when rho < 1/2 (logs/slice_simple.log).
- Potential form of the composition. With Phi(f) = Var(f) ln(1/Var(f)), if every gate satisfies
  LHS_G <= C (I_mu - V) + K [sum_i Inf_i ln(1/sigma_i^2) - V ln(1/V)] then H+(f) <= C (I(f) - Var(f)) - K Phi(f) for every
  read-once formula over those gates (the bracket telescopes to -Phi(f) at the root). Numerically the best K is about
  1/4 for thresholds (worst ratio 4.48 nats against 5.39 at K = 0; logs/tel_potential.log).

Weighted thresholds (logs/ltf_chernoff.log, 3,000 LTFs with n <= 12, weights in {1,2,3}, powers of two up to 2^6, or
exponential; biases down to 1e-8 and up to 1 - 1e-8): alpha TC(mu_A) <= 0.313 I, but the tilt bound
alpha ln(chi*/alpha) (chi* = Chernoff bound) reaches 1,866 I on an event of probability ~1e-16 whose mass sits on a
single configuration. So for LTFs the total correlation needs a reference measure other than the exponential tilt;
the lattice structure (Darroch: the integer mean is a mode, R(N = t) >= c/sqrt(1+v)) is what makes the tilt work for
symmetric thresholds.

## 28. Weighted thresholds under product measures: reductions tested (23 Sep, evening; numerics, no new theorem)

The missing piece for linear threshold gates is the total-correlation lemma alpha TC(mu_A) <= C I (section 25) or a
route around it. Two inductions fail, the damped distinguished-element route survives only for symmetric
thresholds, and two division rules (items 4 and 5) locate what a working rule for weighted thresholds needs.

1. One-coordinate induction (FAILS). For every set A and coordinate j, exactly,
       TC(mu_A) = lam TC(mu_{A_1}) + (1 - lam) TC(mu_{A_0}) + sum_{k != j} I_A(x_j ; x_k),   lam = q_j alpha_1 / alpha,
   and I(A) = Inf_j + q_j I(A_1) + (1 - q_j) I(A_0); restrictions of threshold sets are threshold sets, so the lemma
   would follow by induction from the one-step inequality alpha sum_k I_A(x_j; x_k) <= C Inf_j for some j. On 5,000
   random instances (n <= 8, biases down to 1e-12; logs/tc_pairwise_s2.log) the best coordinate gives at most 0.76
   and the identity holds to 1e-44. But for A = x_1 OR (x_2 AND ... AND x_{m+1}) (weights (m, 1, ..., 1),
   threshold m) with q_1 = q^m, so that both branches are equally likely, every coordinate gives exactly (m/2) ln 2 in
   the limit q -> 0 (logs/tc_pair_family.log: 0.693, 1.040, 1.386, 1.733, 2.079, 2.426 for m = 2..7), while
   alpha TC / I stays below 0.31. The induction charges the m ln 2 of total correlation, which is shared by m + 1
   coordinates, to one of them.
   Precision note: at 30 digits a set of measure 1 - 2e-35 is invisible and gave a spurious ratio of 331; every run
   here uses 40 more digits than the smallest cell probability needs.
2. Chain rule per coordinate (FAILS). TC = sum_k I_A(x_(k); x_(<k)) in any order, and one could ask for
   I_A(x_(k); x_(<k)) <= C (m_k - q_k) with m_k = mu_A(x_k = 1). If x_k is forced (m_k(context) = 1) in contexts of
   mu_A-probability p and irrelevant otherwise, then I_A ~ p ln(1/p) while m_k - q_k ~ p. This happens already for
   x_1 OR (x_2 AND x_3) with the conjunction rare; there the total is paid by m_1 - q_1 ~ 1, so any proof must move
   charge between coordinates. logs: tc_chain.py (small search, best ordering over all n! orders up to 4.9).
3. Distinguished element with damping (SURVIVES for symmetric thresholds, FAILS per coordinate for weighted ones).
   The identity sum_{|A|>=2} P(A) ln(sigma_A^2/P(A)) = sum_j sigma_j^2 Psi(d_j) of section 27 holds for every Boolean
   function (checked to 2e-45 on 1,500 random linear threshold functions with n <= 9; logs/slab_damped_s2.log), and it
   needs no total-correlation lemma: if Psi(d_j) <= C Var(d_j) for every j, the strengthened biased inequality follows
   with constant 2(2 + C) nats. For a threshold of unit weights d_j = 1[N_{-j} = t-1] is a slice, and the coefficient
   on a set B of size b is exactly
       d~(B)^2 = (sigma_B^2 / 4^b) (backward difference of order b of the pmf of the count outside B, at s)^2,
   so Psi(d) = sum_B (sigma_B^2 a_B^2 / (b+1)) ln(1/a_B^2) with a_B = |difference| / 2^b in [0, 1]. For equal biases
   the ratio Psi/Var at the centre of the slice is 0.79, 1.06, 1.27, 1.43, 1.55, 1.65, 1.73 for m = 4, ..., 256 (the
   increments shrink by about 0.8 per doubling; logs/slice_scaling.log), tail slices sit at 2.05 to 2.43 and decrease
   with m, and for q = 0.1 the centre reaches 1.92 at m = 256. Whether the ratio stays bounded is not proved; the
   heuristic reason to expect it is that the level weight of a slice sits at levels comparable to its variance, where
   the damped per-level entropy is O(1). For weighted thresholds the derivative of a heavy
   input can be a threshold of the light inputs: for f = 1[m x_0 + N >= m/2], d_0 = 1[N < m/2] and Psi/Var = 1.81,
   2.51, 3.29, 4.12 for m = 8, 32, 128, 512 (logs/slab_threshold_deriv.log), growing like 0.6 ln m because the level-1
   coefficients of a threshold function are of order v^{-1/2}. The whole function is still fine (the light inputs
   carry J of order sqrt(v)); on 1,500 random linear threshold functions (n <= 9, logs/slab_damped_s2.log) and in 60
   hill-climbing searches on the whole-function ratio (n <= 8, logs/ltf_ratio_adv.log) the left side of the
   strengthened inequality never exceeds 7.7708 bits times I - Var, the AND_2 value 2 + 4 log e, which the searches
   reach; and Psi/Var <= 2.15 (random) and <= 2.37 (40 hill-climbed slabs, logs/slab_adv_s7.log). So for weighted thresholds a proof has to assign each set to its
   elements by weight (the heavy input's level-1 sets belong to the light inputs), and the credit problem of
   section 26 comes back for any assignment without damping.
4. Assignment to the lightest elements (FAILS the other way; logs/ltf_lightest_assign.log). Giving each set A with
   |A| >= 2 to its lightest elements (ties split equally; for equal weights this is item 3) and comparing each
   coordinate's charge with its budget K_j = sum over the sets it owns of share * |A| * P(A) (these budgets sum to J):
   the heavy-plus-light family is fixed (1.38, 1.46, 1.51 at m = 4, 6, 8), but random threshold functions reach 48.8
   (weights (4,1,1,8,2,2), biases down to 5e-9). A lone lightest input owns its sets undamped, and its derivative can be
   a rare low-level event, so ln(1/rho) returns - the credit problem of section 26. Equal division fails for heavy
   inputs and single ownership fails for light ones.
   Proportional shares do not interpolate between the two (logs/ltf_weighted_assign.log, logs/heavy_light_rules.log):
   with shares proportional to w_j^{-gamma}, a coordinate's ratio is a weighted average of the per-set ratios
   ln(sigma_A^2/P(A))/|A| over the sets it shares in, so shares move budget between sets but cannot take the high-ratio
   sets out of the heavy input's average. In the heavy-plus-light family the heavy input reads 1.81, 2.51, 3.29, 4.12 at
   m = 8, 32, 128, 512 for gamma = 0, and 4.12 at m = 512 for gamma = 1 and 2 as well (exact by level, Parseval exact;
   the light inputs stay at 1.8 to 1.9); on random threshold functions with n <= 7 every weight rule stays small
   (2.01, 2.10, 2.67 for gamma = 0, 1, 2) and a rule by pivotal probability reaches 6.72. A working rule has to depend on
   the set, giving the level-two sets {heavy, light} wholly to the light input while keeping each light input's own sets
   damped; whether such a rule exists is a flow feasibility question for every threshold function.
5. The best division (numerics; logs/ltf_best_assign.log, logs/ltf_best_assign_n8.log, logs/general_best_assign.log).
   Dividing each set A (|A| >= 2) among its elements by any shares x_{A,j} and asking for
   sum_A x_{A,j} (e_A - C b_A) <= 0 for every j, e_A = P(A) ln(sigma_A^2/P(A)), b_A = |A| P(A), is a linear programme; by
   duality it is feasible iff a Hall-type condition holds for every set U of coordinates (the bad sets inside U are paid
   by the slack of the good sets meeting U), and U = everything is the global inequality sum e_A <= C J. The least
   feasible C (bisection over LPs, moderate biases) is at most 1.836 over 234 random linear threshold functions with
   n <= 7 and 1.835 over a second run with n <= 8 (that run predates the gap tracking, so only its maximum is quoted),
   against 1.38 and 1.46 for the heavy-plus-light family at m = 4, 6.
   It is NOT always the global ratio: the largest gap is 0.559 (n = 5, least C 1.279 against a global 0.720). For
   tribes the least C reaches 1.151 against a global 0.697. With the heavy-plus-light family computed exactly
   (item 4: the lightest-elements division holds every coordinate at 1.88 at m = 512 where the equal division gives the
   heavy input 4.12), the evidence is that a bounded division exists for threshold functions; an explicit rule is missing.
6. The whole-function ratio with one heavy input and many light ones (logs/two_class_ltf.log, logs/two_class_ltf_m32.log;
   80 + 7(m + 1) digits, enough for cell probabilities down to (1e-6)^(m+1)). Every linear threshold function with one input of bias q0 and m inputs of a common bias
   q has the form f = x_0 T_a + (1 - x_0) T_b with T_c = 1[N >= c], a < b, and its biased spectrum is exact by level:
   f~(B) = s^k (q0 D_k(a) + (1 - q0) D_k(b)) and f~(B + {0}) = s0 s^k (D_k(a) - D_k(b)) for |B| = k, with D_k(c) the k-th
   alternating difference of the tail of Bin(m - k, q) at c. Over q, q0 in {1e-6, 1e-3, 0.05, 0.3, 0.5, 0.7, 0.95, 0.999,
   1 - 1e-6} and all pairs a < b from ten thresholds around the mean and at the ends, the strengthened ratio stays below
   2 + 4 log2 e for m = 1, 2, 4, 8, 16, 32; the maximum is always the conjunction or disjunction corner (a = m, b = m + 1
   near bias 1, or a = 0, b = 1 near bias 0) and decreases slowly with m: 7.7707773 at m = 1, 7.7707629 at m = 16,
   7.7707475 at m = 32, against 7.7707802. The controls AND_2 and OR_2 at biases 1e-6 give 7.7707773.

## 29. The damped slice inequality: what is proved, what is open, and the conjunction limit (23 Sep, evening)

Setting: d = 1[N = s], N the number of ones among m independent inputs of biases q_i, rho = P(N = s),
Lambda = sum_i 4 q_i (1 - q_i), Psi(d) = sum_{B != empty} (d~(B)^2/(|B|+1)) ln(sigma_B^2/d~(B)^2). If Psi(d_j) <= C Var(d_j)
for every derivative of a threshold gate, the gate satisfies the strengthened biased inequality with 2(2 + C)/ln 2 bits
(section 28, item 3).

Exact formula (proved; checked to 2e-43 on 400 instances, logs/slice_bounds_check.log). d~(B)^2 = prod_{i in B}
q_i (1 - q_i) * (Delta_B)^2, where Delta_B is the backward difference of order |B| at s of the pmf of the number of ones
outside B; its generating function is (1 - z)^|B| prod_{i not in B} (1 - q_i + q_i z).

The constant is at least ln 4 + 2 = 3.386. For the conjunction (s = m) of m inputs of bias q,
Psi/Var = E[(b ln 4 + 2 (m - b) ln(1/q)) / (b + 1); b >= 1] / (1 - q^m) with b ~ Bin(m, 1 - q), which tends to
ln 4 + 2 q ln(1/q)/(1 - q) as m(1 - q) -> infinity: 2.7726 at q = 1/2, 3.2828 at q = 0.9, 3.3763 at q = 0.99, and
ln 4 + 2 as q -> 1 (exact values 3.3424 at m = 4096, q = 0.99). The random searches of section 28 (at most 9 inputs)
never reach m(1 - q) large, which is why they stayed below 2.4. Scanning every s for m in {16, 64, 160} and equal biases
q in {0.5, 0.8, 0.9}, and for m in {16, 64} at q = 0.95, 0.98, 0.99 (logs/slice_highbias.log,
logs/slice_highbias2.log), the largest ratio is the conjunction whenever m(1 - q) >= 3 and approaches that limit from
below; when m(1 - q) is small another slice can be largest (s = 60 at m = 64, q = 0.99, ratio 1.72), always far below
2 + ln 4. Both scans ran at a fixed 60 digits; Parseval certifies their coefficients in aggregate (the sum of
d~(B)^2 over B != empty against Var(d) agrees to a relative 4.6e-55 or better at m = 64, every s, all six biases;
logs/slice_parseval_check.log). With unequal biases (300 random bias vectors, every s, m <= 8; logs/slice_unequal_ratio.log) the largest
ratio is 2.255. Conjecture: Psi(d) < (2 + ln 4) Var(d) for every
slice under every product measure; this would give threshold gates the strengthened inequality with 2(4 + ln 4)/ln 2
< 15.6 bits.

Proved: the conjunction, with the sharp constant (logs/conj_bound_check.log). For d = y_1 ... y_m under any product
measure, Psi(d) < (2 + ln 4) Var(d), and 2 + ln 4 is the supremum. Proof. d~(B)^2 = prod_{i in B} q_i (1 - q_i)
prod_{i not in B} q_i^2 = rho P_w(B), with rho = prod q_i and P_w the product measure on subsets that includes i with
probability w_i = 1 - q_i; ln(sigma_B^2/d~(B)^2) = |B| ln 4 + 2 sum_{i not in B} ln(1/q_i); and Var(d) = rho P_w(B != empty).
So Psi/Var = E_w[(|B| ln 4 + 2 sum_{i not in B} ln(1/q_i))/(|B| + 1) | B != empty]. The first part is below ln 4. For the
second, E[1(i not in B) 1(B != empty)/(|B| + 1)] = q_i E[g(B - {i})] with g(S) = 1(S != empty)/(|S| + 1), q ln(1/q) <= 1 - q,
and sum_i w_i E[g(B - {i})] = E[sum_{i in B} g(B - {i})] = P(|B| >= 2), so the second part is at most
2 P(|B| >= 2)/P(B != empty) < 2. Equality is approached when every q_i -> 1 and m (1 - q_i) -> infinity (the equal-bias
limit ln 4 + 2 q ln(1/q)/(1 - q) above). Checked on 300 random unequal-bias conjunctions with m <= 12: the formula agrees
with the direct transform to 1e-60, Psi/Var <= 2.20, and the intermediate bound is never below Psi/Var (slack exactly 0
at m = 1, where both sides equal (ln 4)/2).

Proved: near-deterministic slices. If rho >= 1/2, then Lambda <= 930 Var(d) and Psi(d) <= 7.04 Var(d).
Proof. Resampling every input as in Lemma thr-rank (eta = 1) gives rho <= max_k P(N = k) <= (2/(pi L))^{1/2}, L = sum_i
min(q_i, 1 - q_i), so L <= 8/pi < 2.547. If the likely configuration has exactly s ones, then N != s whenever exactly one
input deviates, so 1 - rho >= L prod_i (1 - min(q_i, 1 - q_i)) >= L e^{-1.5 L} >= 0.0219 L; otherwise N = s needs a
deviation and 1 - rho >= prod_i (1 - min(q_i, 1 - q_i)) >= e^{-1.5 L} > 0.0219 >= 0.0086 L. Either way
Lambda <= 4L <= 465 (1 - rho) <= 930 Var(d). Gibbs on each level against sigma_B^2 with e_k <= Lambda^k/k! and
x ln(a/x) <= a/e gives Psi(d) <= ln(930) Var(d) + (1/e) sum_k Var^k/(k+1)! <= (6.835 + 0.2) Var(d). Checked on 86
instances: Lambda/Var <= 8.6, Psi/Var <= 1.03.

Proved: the bulk. If rho < 1/2, then Psi(d) <= rho (7.35 + 5.35 ln(1/rho)/sqrt(Lambda)).
Proof. Per-level Gibbs: Psi <= sum_b (W_b/(b+1)) (b ln(e Lambda/b) + ln(1/W_b)). With nu the spectral law of d
(nu(T) = d~(T)^2/rho, W_b = rho nu_b), the rank tail of Lemma thr-rank, nu(|T| <= K) <= 3 sqrt(6/pi) (K/Lambda)^{1/2} for
K >= 1 (valid for any Lambda here, since the free count has mean eta Lambda/2 at least), gives
sum_b W_b ln+(e Lambda/b) <= rho (1 + ln 2 + 4.85) and E_nu[1/(|T|+1); T != empty] <= 1.22 * 3 sqrt(6/pi)/sqrt(Lambda) < 5.06/sqrt(Lambda) (1.22 bounds sum_{K>=1} K^{1/2}/((K+1)(K+2)));
sum_b (nu_b/(b+1)) ln(1/nu_b) <= 2 ln(3)/3 + (zeta(3) - 1)/e < 0.81 for any law on b >= 1. Checked on 314 instances
(the observed value is at most 0.13 of the bound).

Open: the tail. When ln(1/rho) is large compared with sqrt(Lambda) the bulk bound is useless, and per-level Gibbs
over the whole level is too lossy when the weight of a level sits on inputs with small sigma^2 (the D-inputs of the
second case of Theorem thr-strong). The exact formula shows why the tail is benign (in the far upper tail the spectral
weight sits at levels b >= s - O(sqrt(s lambda)), where ln e_b and ln(1/rho) cancel to about b ln 4), but a proof needs
either pointwise caps as in Theorem thr-strong or a tilted version of the rank tail.

A tool for the tail (exact; logs/slice_tilt_identity.log, relative error below 1e-57 on 10 tail slices). Let R be the
exponential tilt of mu with E_R N = s (biases q^R_i = q_i u/(1 - q_i + q_i u)). On the slice dR/dmu = kappa is constant,
and expanding y_i - q_i = (y_i - q^R_i) + (q^R_i - q_i) gives
    d~_mu(B) = kappa^{-1} sum_{T subset of B} alpha_T beta_{B minus T} d~_R(T),
    alpha_i = sqrt(q^R_i (1 - q^R_i)/(q_i (1 - q_i))),  beta_i = (q^R_i - q_i)/sqrt(q_i (1 - q_i)),
so the tail spectrum under mu is a binomial transform of the bulk spectrum under R, where the rank tail applies. The
term T = empty alone gives d~_mu(B) ~ rho beta_B, a spectral law close to the product measure with inclusion
probabilities w_i = beta_i^2/(1 + beta_i^2), and a damped ratio close to E[L(B)/(|B| + 1)] with
L(B) = sum_{i in B} ln(sigma_i^2/(w_i (1 - w_i))) + sum_{i not in B} 2 ln(1/(1 - w_i)); for the conjunction this is exactly
ln 4 + 2 q ln(1/q)/(1 - q). The leading term carries 18 to 47 pct of the spectrum at tilts u between 2.4 and 14 and almost
none near the bulk (u near 1), so it describes only the far tail; a proof has to control the cross terms T != empty,
which is where the rank tail under R would enter.
Where 2 + ln 4 comes from (not a proof). The leading term is exact when the tilt sends every input to q^R_i = 1, the
conjunction, where R is a point mass and every cross term vanishes. There w_i = 1 - q_i, an included input contributes
ln(sigma_i^2/(w_i (1 - w_i))) = ln 4 exactly, and an excluded one contributes 2 ln(1/q_i) with probability q_i against a
share 1 - q_i of the damping denominator; sup_q 2 q ln(1/q)/(1 - q) = 2 (as q -> 1) gives ln 4 + 2. When q^R_i < 1 the
factor sigma_i^2/(w_i (1 - w_i)) = 4 (q_i (1 - q_i) + D_i^2)^2 / D_i^2 with D_i = q^R_i - q_i exceeds 4, so a general tail
slice can stay below 2 + ln 4 only through the cross terms T != empty; the computed slices do.
