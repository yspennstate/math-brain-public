# FEI for monotone functions: an erasure bound on the down-set, and DNFs of bounded width

24 September 2026. Proved here, for monotone Boolean functions:

- a bound on the restriction step at any coordinate in terms of its influence relative to the variance
  (Theorem 2);
- the Fourier entropy-influence inequality with constant 9.41 for every monotone 2-DNF, with no condition on the
  number of terms or on how often a variable occurs (Corollary 4);
- the inequality with constant at most w + 8.1 for every monotone DNF or CNF of width w, and more generally for
  every class of monotone functions closed under restrictions whose nonconstant members have a minterm or a
  maxterm of size at most w (Theorem 3);
- the influence-entropy bound with influences measured relative to the variance (Corollary 5), and a reduction of FEI for
  monotone functions to monotone functions all of whose influences are small compared with the variance
  (Corollary 6);
- O'Donnell and Tan's strengthened inequality for the same classes, with constant 17.43 for 2-DNFs and at most
  2w + 14.8 in general, and hence FEI for read-once formulas over AND, OR, XOR and threshold gates of any fan-in
  whose inputs are monotone DNFs or CNFs of bounded width (Section 4a);
- H(f) <= (log2 log2 s + 7.85) I(f) for every monotone function computed by a decision tree with s leaves, and
  (log2 L + 7.85) with L the largest least expected depth over restrictions (Section 4b, paper Theorem 1.6); in
  particular (log2 m + 8.85) for monotone DNFs with m terms and (2 log2 s + 7.85) with s the sensitivity;
- a local form of the conjecture, equivalent to it on every restriction-closed class: removing one element of the
  spectral sample raises its weight by at most a bounded factor on logarithmic average (Section 5a, paper
  Proposition 6.3).

FEI for all monotone functions stays open; Section 5 says where the argument stops. Every statement was also
checked numerically, including exhaustively over the 7,828,354 monotone functions of six variables (Section 6).

Notation as in continuations 2026-09-23-readk-dnf and 2026-09-24-monotone. For f: {0,1}^n -> {0,1} put
F = 1 - 2f, chi_T(x) = (-1)^{sum_{i in T} x_i}, P(T) = Fhat(T)^2, H = sum P log2(1/P), I = sum |T| P(T), and
Inf_v = sum_{T ni v} P(T) = Pr[f(x^{v<-1}) != f(x^{v<-0})]. Write q = Pr[f = 0] and m = min(q, 1 - q). For a
coordinate v and T subset of [n] - v, the pair (P(T), P(T + v)) is the pair of weights of T with and without v.
With phi(t) = t log2(1/t) and E(X, Y) = phi(X) + phi(Y) - phi(X + Y),

    B_v = sum_{T not ni v} E(P(T), P(T + v)) = H(1[v in S] | S - v),

where S is the spectral sample, and the restriction step Delta_v = H(F) - (H(F_0) + H(F_1))/2 splits as
Delta_v = B_v + JS_v, with JS_v the Jensen-Shannon divergence of the spectra of the two restrictions
(continuation 2026-09-22-opus-team, F4, Section 0). Since I(F) = Inf_v + (I(F_0) + I(F_1))/2, a class of
functions closed under restrictions in which every nonconstant member has a coordinate with Delta_v <= K Inf_v
satisfies H <= K I, by induction on the number of variables.

## 1. The down-set identity

Let D = {f = 0}, a down-set, and let mu be the uniform measure on D, with characteristic function
mu~(T) = E_mu chi_T. Since F = 2 1_D - 1,

    Fhat(T) = 2 q mu~(T) for T nonempty.                                                          (1.1)

Fix v. For y in {0,1}^{[n]-v} call y blocked if y is in D but y + v is not, and free if y + v is in D. Because D is
a down-set, the fibre of D over y is {y} when y is blocked and {y, y + v} when y is free. Put

    a(T) = |D|^{-1} sum_{y blocked} chi_T(y),        b(T) = 2 |D|^{-1} sum_{y free} chi_T(y)       (T subset [n]-v).

Lemma 1. For T subset of [n] - v,

    mu~(T + v) = a(T),        mu~(T) = a(T) + b(T),

and, with eps = Inf_v/(4q),

    q sum_T a(T)^2 = eps,        q sum_T b(T)^2 = 1 - 2 eps,        0 <= eps <= 1/2.

Proof. On a free fibre x_v takes both values with equal weight, so chi_{T+v} averages to zero there; on a blocked
fibre x_v = 0. This gives the two identities. Let N_B and N_F be the numbers of blocked and free y; then
|D| = N_B + 2 N_F and Inf_v = N_B/2^{n-1}, since the pivotal edges in direction v are exactly the pairs
{y, y + v} with y blocked. Parseval on {0,1}^{n-1} gives sum_T a(T)^2 = 2^{n-1} N_B/|D|^2 and
sum_T b(T)^2 = 2^{n-1} 4 N_F/|D|^2. Multiplying by q = |D|/2^n gives N_B/(2|D|) = eps and
2 N_F/|D| = 1 - 2 eps. []

In words: under the uniform measure on the down-set, a coordinate is a fair coin whenever it is not blocked, and
eps_v is half the probability that it is blocked. By (1.1) and Lemma 1, P(T + v) = 4q^2 a(T)^2 for every T and
P(T) = 4q^2 (a(T) + b(T))^2 for T nonempty. For monotone f, Fhat({v}) = Inf_v, so P({v}) = Inf_v^2.

## 2. The erasure bound

Let Psi(r) = log2(e (r + 2 sqrt(r) + 2)) for r >= 0. It is increasing, and concave because r + 2 sqrt(r) + 2 is
concave and positive. Let c0 = max_{0 < x <= 1} x log2(e/x^2) = 2 e^{-1/2}/ln 2 = 1.75008.

Lemma 2. For every monotone f and every coordinate v with Inf_v > 0,

    B_v <= Inf_v (c0 + Psi(4m/Inf_v - 2)).

Proof. The dual f*(x) = 1 - f(1 - x) is monotone, has the same P (its coefficients are -(-1)^{|T|} Fhat(T)) and
Pr[f* = 0] = 1 - q. So it is enough to prove the bound with q in place of m; note Inf_v <= 2q, so the argument
of Psi is nonnegative. Use E(X, Y) <= Y log2(e (X + Y)/Y), which follows from X log2(1 + Y/X) <= Y log2 e.

The pair T = empty: P({v}) = Inf_v^2 and P(empty) + P({v}) <= 1, so this pair contributes at most
Inf_v^2 log2(e/Inf_v^2) <= c0 Inf_v.

The pairs with T nonempty: if a(T) = 0 the pair contributes 0. Otherwise put s = b(T)/a(T); by homogeneity of E
the pair contributes 4q * q a(T)^2 * psi(s), where psi(s) = E((1 + s)^2, 1) <= log2(e((1 + s)^2 + 1)) <= Psi(s^2).
The weights w_T = q a(T)^2 have total W <= eps, and sum w_T s_T^2 <= q sum_T b(T)^2 = 1 - 2 eps by Lemma 1.
Jensen's inequality for the concave increasing Psi gives

    sum w_T Psi(s_T^2) <= W Psi((1 - 2 eps)/W) <= eps Psi((1 - 2 eps)/eps),

the last step because W -> W Psi(c/W) is nondecreasing (its derivative is Psi(y) - y Psi'(y) >= Psi(0) > 0 at
y = c/W, by concavity). Since (1 - 2 eps)/eps = 4q/Inf_v - 2 and 4q eps = Inf_v, the nonempty pairs contribute at
most Inf_v Psi(4q/Inf_v - 2). []

The logarithm in Lemma 2 cannot be removed: in the monotone flip example of F4 (Proposition 6.1),
F_n = Maj_n(y) OR (z AND [y = y*]), one has m ~ 1/2, Inf_z = 2^{-n} and B_z >= ((n - 3 log2(n + 1))/2) Inf_z
for n >= 11 (paper, Remark 5.1; F4 states n - 3 log2 n, but its last step gives 4^n u^2 >= 2^n/((n-1)(n+1)^2),
not 2^n/n^3), while log2(4m/Inf_z) < n + 1. What is new is that the logarithm is of the influence relative to m, not of the influence
itself (compare F4, Lemma 1.2, which has log2(e/Inf_v)).

For the Jensen-Shannon part we use JS_v <= (2/ln 2) sum_T min(Fhat(T)^2, Fhat(T+v)^2) <= (2/ln 2) Inf_v
(F4, Lemma 1.1(c)). A direct proof: with u = Fhat(T), w = Fhat(T + v), |w| <= |u| and r = w/u, the pair
contributes (u^2 + w^2)(1 - h((1 + t)/2)) with t = 2r/(1 + r^2), and the series
1 - h((1 + t)/2) = (1/ln 2) sum_{k>=1} t^{2k}/(2k(2k - 1)) turns the claim (1 + r^2)(1 - h) <= (2/ln 2) r^2 into
sum_{k>=2} (4/(k(2k - 1))) s^{k-2} y^2 <= 1, where y = 1/(1 + r^2) is in [1/2, 1] and s = 4(y - y^2) is in [0, 1];
bounding s^{k-2} by s for k >= 3 and using sum_{k>=1} 1/(k(2k - 1)) = 2 ln 2 leaves
(2/3) y^2 + 16(2 ln 2 - 7/6)(y^3 - y^4) <= 1, and the left side is at most 0.806 on [1/2, 1].

Theorem 2 (the restriction step). For every monotone f and every coordinate v with Inf_v > 0,

    Delta_v <= Inf_v (2/ln 2 + c0 + Psi(4m/Inf_v - 2)).

Here 2/ln 2 + c0 = 4.6355. So any coordinate with Inf_v >= tau m has Delta_v <= (4.6355 + Psi(4/tau - 2)) Inf_v:
for tau = 2/3 the constant is 9.401, for tau = 1 it is 8.85, for tau = 2 (the largest possible) it is 7.08.

## 3. Short certificates

Lemma 3. Let f be monotone and let M be a minterm of f with |M| = k >= 1. Then some v in M has
Inf_v >= 4q/(2^{k+1} - 2), that is eps_v >= 1/(2^{k+1} - 2). The same holds with a maxterm and 1 - q.

Proof. If k = 1, M = {v} and f = x_v OR g with g not depending on x_v, so Inf_v = Pr[g = 0] = 2q. Let k >= 2,
M = {v_1, ..., v_k}, and delta = max_j eps_{v_j}. Under mu, the conditional probability that x_{v_j} = 1 given
the other coordinates is 1/2 on free fibres and 0 on blocked ones, and the blocked fibres have probability
2 eps_{v_j}. Hence p_j = mu(x_{v_2} = ... = x_{v_j} = 1) satisfies p_1 = 1 and p_{j+1} >= (p_j - 2 delta)/2,
so p_k >= 2^{1-k} - delta (2 - 2^{2-k}). If x_{v_2} = ... = x_{v_k} = 1 then v_1 is blocked, because adding v_1
completes M. So 2 delta >= 2 eps_{v_1} >= p_k, which gives delta >= 1/(2^{k+1} - 2). For a maxterm apply this
to f*. []

For k = 2 this is the statement that every edge u w of a monotone 2-DNF has an endpoint with eps >= 1/6: the
probability rho_u = 1/2 - eps_u that u is present blocks w, so eps_w >= (1/2 - eps_u)/2.

Theorem 3. Let C be a class of monotone functions closed under restrictions, such that every nonconstant member
has a minterm or a maxterm of size at most w. Then every f in C satisfies

    H(f) <= c_w I(f),    c_w = 2/ln 2 + c0 + Psi(2^{w+1} - 4) <= w + 8.1.

Proof. By Lemma 3 a nonconstant f in C has a coordinate with Inf_v >= 4m/(2^{w+1} - 2); Theorem 2 then gives
Delta_v <= c_w Inf_v, since Psi is increasing. Induct on the number of variables. []

The values are c_1 = 7.078, c_2 = 9.400, c_3 = 10.466, c_4 = 11.421, c_5 = 12.354, c_10 = 17.139, and
c_w - w decreases to 2/ln 2 + c0 + 1 + log2 e = 7.078 as w grows.

Corollary 4. Every monotone 2-DNF, f(x) = OR_{u in U} x_u OR OR_{uw in E} x_u x_w for a graph (V, E) and a set
U of vertices, satisfies H(f) <= 9.41 I(f). The same holds for monotone 2-CNFs, that is for the indicator that
the set of ones is a vertex cover of a graph.

The class is closed under restrictions: x_v = 0 deletes v, and x_v = 1 turns the neighbours of v into singleton
terms. For a monotone 2-DNF with no singleton terms, 1 - f is the indicator that the set of ones is independent,
mu is the uniform independent set of the graph (the hard-core model at fugacity 1), eps_v is half the
probability that v has an occupied neighbour, and Lemma 1 reads E|S|/(4q) = sum_v eps_v. The previous bound for
this class was the read-k theorem with k the maximum degree, (30 + 5.6 log2 k) I (continuation
2026-09-23-readk-dnf, Theorem 2.5).

Other members of the classes in Theorem 3: monotone DNFs whose terms have at most w variables and monotone CNFs
whose clauses have at most w variables, with any number of terms and any number of occurrences of a variable;
disjunctions of such a DNF with such a CNF on disjoint variables.

## 4. The influence-entropy bound with relative influences

Corollary 5. For every monotone f,

    H(f) <= sum_v Inf_v (4.6355 + Psi(4m/Inf_v - 2)).

Proof. Han's telescoping (arXiv:2312.08271, (3.4)) writes H(f) = sum_k E Delta_k(f_x), where f_x fixes the
coordinates after k to x and Delta_k is its restriction step at k; each f_x is monotone. By Theorem 2,
Delta_k(f_x) <= G(Inf_k(f_x), m(f_x)) + 4.6355 Inf_k(f_x) with G(x, m) = x Psi(4m/x - 2), the perspective of the
concave Psi composed with an affine map, hence jointly concave, and increasing in m. Jensen's inequality,
E Inf_k(f_x) = Inf_k(f) and E m(f_x) <= m(f) give the claim. []

Since Psi(r) <= log2(e(r + 2)) + 1, this is H <= 7.1 I + sum_v Inf_v log2(4m/Inf_v). For balanced functions it is
no better than H <= sum_v h(Inf_v) = O(I + sum_v Inf_v log(1/Inf_v)), which is just subadditivity of entropy
(Keller, Mossel and Schlank, Discrete Math. 312 (2012), Claim 4.1; Han, Combinatorica 2025, reproved it with other
constants). For biased functions it is stronger by up to I log2(1/m). For AND_n, for instance, all influences equal
2m and the bound is 8.08 I, while the absolute-influence form carries a factor n. (Both papers of this problem had
credited that bound to Han alone; the citations now name Keller, Mossel and Schlank.)

## 4a. The strengthened inequality and composition (added 24 September, later)

O'Donnell and Tan's strengthened inequality is H+(f) = sum_{A nonempty} P(A) log2(1/P(A)) <= C (I(f) - Var(f)); it is
preserved under disjoint composition when the gates satisfy its biased form.

Lemma 5.1 (exact, every Boolean function). With a_T = Fhat(T), d_T = Fhat(T + v), D_v F = (F(x^{v<-0}) - F(x^{v<-1}))/2
and J(a, d) = phi(a^2 + d^2) - (phi((a+d)^2) + phi((a-d)^2))/2:

    Delta+_v := H+(f) - (H+(f_0) + H+(f_1))/2 = phi(d_empty^2) + sum_{T nonempty} (E(a_T^2, d_T^2) + J(a_T, d_T)),
    (I - Var)(f) = Var(D_v F) + ((I - Var)(f_0) + (I - Var)(f_1))/2.

So a restriction-closed class in which every nonconstant member has a coordinate with Delta+_v <= C Var(D_v F)
satisfies the strengthened inequality with C.

Lemma 5.2 (every monotone f, every v). Delta+_v <= Var(D_v F) (4/ln 2 + log2(e(1 + 1/Inf_v))), in particular
<= 8.80 Var(D_v F) when Inf_v >= 1/2 (near-dictator coordinates). Proof: phi(Inf^2) <= (2/ln 2) Inf (1 - Inf); the J
terms are at most (2/ln 2) M with M = sum_{T nonempty} min(a_T^2, d_T^2) <= Var(D_v F); the E terms are at most
M log2(eS/M) <= Var(D_v F) log2(e(1 + 1/Inf_v)) by the log-sum inequality, because the nonempty a-mass is at most
1 - Inf_v and the nonempty d-mass equals Var(D_v F) = Inf_v(1 - Inf_v).

Paper Theorem 1.8. Every class as in Theorem 3 satisfies H+ <= C+_w (I - Var) with
C+_w = max(8.80, 2(1.0615 + 2/ln 2 + Psi(2^{w+1} - 4))): C+_1 = 12.78, C+_2 = 17.43, C+_3 = 19.56, C+_w <= 2w + 14.8.
Proof: at the coordinate of Lemma 3, either Inf_v >= 1/2 (Lemma 5.2) or Delta+_v <= phi(Inf_v^2) + Inf_v Psi(...) +
JS_v with phi(x^2) <= 1.0615 x and Var(D_v F) >= Inf_v/2.

Paper Corollary 1.9. For a read-once formula over AND, OR, XOR and threshold gates of any fan-in whose inputs are monotone
DNFs or CNFs of width at most w on disjoint variables: H <= max(C+_w, 760) I, and H <= C+_w I with only AND, OR and
XOR gates (O'Donnell-Tan Theorem 1; gate constants 2 + 4 log2 e and 760 from continuation 2026-09-23-readk-dnf). For
example the conjunction of any number of monotone 2-DNFs on disjoint variables, a DNF of unbounded width, has
H <= 17.43 I; Theorem 3 alone gives 2k + 8.1 for k conjuncts.

The biased form for bounded-width DNFs themselves, which would let them serve as gates, does not follow the same way:
under a product measure with small input biases q the down-set BOUND leaves an unpaid log(1/q) on a large matching.
The step itself is fine there (`code/biased_matching.py`, `logs/biased_matching.log`): for a perfect matching of k
pairs, all biases q and k = round(ln 2/q^2) so the output is balanced, the biased spectral sample is a product over
the pairs, and at every input the erasure term H(1[v in S] | S - v) is o(Inf~_v) as q -> 0 (it is about
(q/2)(4 log2(1/q) + O(1)) Inf~_v): every pair of weights (P(T), P(T + v)) is lopsided, with ratio about q^3 when v's
partner is outside T and about 1/q when it is inside. So the credit Inf~_v log2(1/sigma_v^2) is not even needed, and
rho_v = (B~_v - Inf~_v log2(1/sigma_v^2))/Inf~_v = -(log2(1/q) - 2) + o(1) (q = 0.001: -7.94, k = 693,147). The
exact product formula matches brute force on (q, k) = (0.3, 3), (0.2, 4), (0.1, 5) to all printed digits. What fails is
the second-moment estimate of Lemma 2, which cannot see lopsided pairs; a sharper erasure bound (a biased version of
the local form R <= K I, with the credit) is what the biased conjecture needs, not a different induction.

The induction itself goes through numerically (`code/biased_induction.py`, `code/biased_induction2.py`, logs beside
them). With L(G) = sum_{A nonempty} P_mu(A) log2(sigma_A^2/P_mu(A)) and R(G) = I_mu - Var_mu, restricting coordinate v
to b with probability mu(y_v = b), the biased form follows on a restriction-closed class of gates if every
nonconstant gate has a coordinate with L(G) - E_b L(G_b) <= C (R(G) - E_b R(G_b)). Over fourteen graph gates on up to
six inputs (edge, paths, cycles, stars, triangle, K4, K2,3, K3,3, matchings) with 261 bias vectors each, the largest
value of min_v of that ratio is 7.7702, attained by a single edge with both biases near 1 - the AND constant
2 + 4 log2 e = 7.7708 - and every other graph stays below 6.87. On random monotone 2- and 3-DNF gates with 6 to 8
inputs and random biases the largest value is 6.67, and 6.87 after a coordinate-wise local search on the biases of
the twelve worst cases. Conjecture: every monotone DNF gate of width 2 (and 3) has, under every product measure, a
coordinate at which the biased step is at most 2 + 4 log2 e times the decrease of I - Var. This would give FEI for
read-once formulas whose gates are arbitrary monotone 2-DNFs (graph gates) with inputs of any bias. Which
coordinate (`code/biased_which_v.py`, 400 random graph gates on 3-6 inputs, random biases): restricting the v that
maximises R(G) - E_b R(G_b) = sum_{T nonempty} P_mu(T + v) - the biased Var(D_v F), the analogue of the most
influential coordinate - gives worst ratio 7.765, the same as the best coordinate; the most pivotal coordinate and the
highest-degree vertex give 7.767; the input of largest bias fails (8.105). So a proof should restrict a coordinate of
largest biased Var(D_v F) and bound its erasure term with the credit, using that the weight pairs are lopsided.
Numerically the loss is not real (`code/biased_gate.py`, `code/biased_gate2.py`): every monotone 2-DNF gate tested
(paths, cycles, stars, triangle, K4, K2,3, matchings; equal biases from 1e-6 to 1 - 1e-6 and 300 random bias vectors
each) and 120 random monotone 2- and 3-DNF gates on up to 10 inputs with a local search on the biases never exceed
2 + 4 log2 e = 7.7708, the sharp AND2/OR2 constant, which they approach only at extreme biases (7.77071). Conjecture:
monotone DNFs of bounded width satisfy the biased strengthened inequality with the sharp constant 2 + 4 log2 e under
every product measure; with the uniform theorem this would give FEI for read-once formulas over bounded-width monotone
DNF gates of any depth. The same holds over ALL monotone functions of at most five variables (`code/biased_all.py`,
309 product measures each, then a local search on the biases of the 30 best pairs): float values up to 7.7713 appeared
only at biases near 1e-7, and 60-digit recomputation (`code/biased_mp.py`) puts every one of them below
2 + 4 log2 e by 2e-6 to 4e-6 (`logs/biased_all.log`, `logs/biased_mp.log`). For a 2-DNF gate the uniform measure on the zeros under a product measure is the hard-core
model with activities q_v/(1 - q_v), so a proof amounts to a spectral-entropy estimate for the hard-core model at
every activity.

## 4b. Decision trees (added 24 September, noon)

In Theorem 3 the large relative influence comes from a short minterm. The theorem of O'Donnell, Saks, Schramm and
Servedio (FOCS 2005) gives another source: for a decision tree T computing g, Var(G) <= sum_i delta_i Inf_i(g), where
delta_i is the probability that T reads coordinate i on a uniform input, and sum_i delta_i is the expected depth. So
a monotone g with a tree of expected depth at most L has a coordinate with Inf_v >= Var(G)/L >= 2m/L.

Let L(f) be the largest, over the restrictions g of f, of the least expected depth of a decision tree for g. In a
tree whose paths read distinct coordinates a leaf at depth k is reached with probability 2^-k, so the expected depth
is the entropy of the leaf reached; restricting a tree does not add leaves; hence L(f) <= log2 s for a tree with s
leaves. Also L(f) <= the depth of any tree for f, and L(f) <= the zero-error randomized query complexity.

Paper Theorem 1.6. Every nonconstant monotone f has H(f) <= (4.6355 + Psi(2L(f) - 2)) I(f) <= (log2 L(f) + 7.85) I(f);
a monotone function computed by a decision tree with s >= 2 leaves has H <= (log2 log2 s + 7.85) I. Proof: at each
restriction the OSSS coordinate has 4m/Inf_v - 2 <= 2L - 2, then Theorem 2 and the induction. The strengthened
inequality holds with max(8.80, 2(1.0615 + 2/ln 2 + Psi(2L - 2))) <= 2 log2 L + 14.33 (paper Theorem 1.8), so leaves
with small trees can enter the composition corollary.

For comparison, Wan, Wright and Wu (ITCS 2014) prove H <= 12 d I for every Boolean function with I >= 1 computed by a
tree of expected depth d. For monotone functions the factor d becomes log2 L, with L a maximum over restrictions. With
D(f) <= C_0(f) C_1(f) (Buhrman and de Wolf's survey), a monotone function whose minterms have at most w_1 elements
and whose maxterms at most w_0 has H <= (log2(w_0 w_1) + 7.85) I: logarithmic in the widths, where Theorem 3 is
linear in the smaller one (Theorem 3 is still the better of the two when w_0 = w_1 <= 5). For monotone f the
certificate complexity equals the sensitivity s(f) (Nisan; in Buhrman and de Wolf's survey), and sensitivity does not
grow under restriction, so every nonconstant monotone f has H <= (2 log2 s(f) + 7.85) I; with bs(f) <= 2 deg(f)^2
(Nisan-Szegedy) and s = bs for monotone f, a monotone function of Fourier degree k has L(f) <= 4k^4 and
H <= (4 log2 k + 9.85) I (paper Corollary 1.7(d)). And a monotone DNF with m
terms (or CNF with m clauses) is evaluated term by term with at most two new reads per term in expectation, and its
restrictions have at most m terms, so L(f) <= 2m and H <= (log2 m + 8.85) I - for monotone formulas better than the
read-k theorem's (30 + 5.6 log2 m) I for m-term DNFs. These are paper Corollary 1.7 (a)-(c). Checked
(`code/mterm_check.py`, `logs/mterm_check.log`): on 400 random monotone DNFs (n <= 10, m <= 29) the hereditary
expected depth L(f) <= 2m held with largest ratio 0.992 (a single long term nearly attains it), and H/I stayed
below 0.43 of log2 m + 8.85.

Checked (`code/dt_check.py`, `logs/dt_check.log`): the least expected depth E*, least number of leaves s*, least
depth D* and L(f), by dynamic programming over the 3^n subcubes, for all nonconstant monotone functions with n <= 5
and 145 random monotone DNFs on 8 to 10 variables. The OSSS bound max_v Inf_v >= Var/E* held everywhere, with
equality for 87 of the 7,579 functions of five variables (the conjunction among them); E* <= log2 s* and E* <= D*
everywhere; H/I stayed below 0.44 of the bound of paper Theorem 1.6. The constants (`code/local_form_check.py`,
`logs/local_form_check.log`): over L >= 1, max (c(L) - log2 L) = 7.8497 and max (C+(L) - 2 log2 L) = 14.3223.

Mixed classes (paper Remark 3.2). The induction needs a short minterm only where no other bound is available: if
B inside C are restriction-closed monotone classes, H <= C_B I on B, and every nonconstant member of C outside B has
a minterm or maxterm of size <= w, then H <= max(c_w, C_B) I on C. With B the monotone regular functions (15.1,
continuation 2026-09-23-readk-dnf) and C the functions g OR h, g in B and h a monotone width-w DNF on the SAME
variables or not: every restriction is in B (h killed), constant, or has a term of h as an implicant. So for
instance Maj_n(x) OR (the edge indicator of any graph G on [n]) has H <= 15.1 I - a non-disjoint combination that
neither theorem nor the composition theorem covers alone.

## 4c. Product measures with biases in [eps, 1 - eps] (PROVED 24 September, afternoon; paper Theorem 1.10, Section 6)

Theorem 1.10. Let 0 < eps <= 1/2 and mu a product measure with every bias in [eps, 1 - eps]. Every f in a class as in
Theorem 3 (restriction-closed, monotone, a minterm or maxterm of size <= w) satisfies the biased strengthened inequality
    sum_{A nonempty} P_mu(A) log2(sigma_A^2 / P_mu(A)) <= (14.24 + 2w log2(1/eps)) (I_mu - Var_mu).
So in the composition corollary a bounded-width monotone DNF/CNF gate may have inputs of any bias in [eps, 1 - eps].
At eps = 1/2 the constant 14.24 + 2w matches the uniform C+_w <= 2w + 14.8.

Proof (paper Section 6). Lemma 6.1: the biased restriction step of L = sum P log2(sigma^2/P) is
d_empty^2 log2(sigma^2/d_empty^2) + sum_{T nonempty}(E(a^2, d^2) + J_q(a, d)) - log2(1/sigma^2) sum_{T nonempty} d^2, and the step of
R = I - Var is sum_{T nonempty} d^2. Lemma 6.2 (log-Sobolev, see (C3) below): J_q <= (c(q)/ln 2) d^2 with
c(q) <= 2 + ln(1/sigma^2), so the credit pays for J up to (2/ln 2). Lemma 6.3: biased down-set - under mu conditioned on
the zero set, x_v is 0 over blocked y and Bernoulli(q) over free y; d_T = -2 mu(D) tau alpha(T), a_T = 2 mu(D)(alpha +
gamma)(T); Parseval under mu' gives the second moments; Inf~_v = sigma^2 pi, d_empty^2 = sigma^2 pi^2 (pi = Pr[v pivotal]);
Jensen gives erasure <= Inf~_v log2(e(1 + 2(1-q)/q + 2(1-theta)/(q theta))), theta = mu_D(v blocked). Lemma 6.4: a minterm
of size k with biases >= eps has a coordinate with theta >= eps^(k-1)(1-eps). Then two cases: pi <= 1/2 (constant
2*1.0615 + 2 log2(9e) + 2/ln 2 + 2k log2(1/eps) = 14.2336 + 2k log2(1/eps)), and pi > 1/2 (the near-dictator log-sum
argument with Var((1-q)F_0 + qF_1) <= 4(1 - pi): 4/ln 2 + log2(9e/2) + log2(1/eps) = 9.3834 + log2(1/eps)). Maxterms by
duality under the reflected measure. The credit (the sigma_A^2 factors) is essential: for a dictator under bias,
H+ = sigma^2 log2(1/sigma^2) > 0 = I - Var, while the credited form gives 0 <= 0.

Checks (`code/biased_downset.py`, `code/biased_theorem_check.py`, logs beside them): the biased identities to 3e-13;
the erasure bound on 985 (gate, coordinate, bias) cases at <= 0.774 of itself; the minterm lemma with margin >= 1.21;
and the final step inequality at the minterm-lemma coordinate on 393 random DNF gates with biases in [eps, 1-eps]
(eps from 0.02 to 0.5) at <= 0.41 of the claimed constant.

## 5. What remains

Corollary 6. Let tau in (0, 2]. Suppose every monotone g with Inf_v(g) < tau m(g) for all v has a coordinate
with Delta_v <= K Inf_v. Then every monotone f satisfies H(f) <= max(K, 4.6355 + Psi(4/tau - 2)) I(f). In
particular, if some monotone f has H(f) > C I(f) with C > 7.08, then a restriction g of f has
H(g) - C I(g) >= H(f) - C I(f) and every influence of g is below 2^{9.08 - C} m(g): exponentially small in C
compared with its variance. (Proof as F4, Theorem 2.1 and Corollary 2.2, with Theorem 2 in place of F4,
Lemma 1.2: at the end of the descent Psi(4m/Inf_v - 2) > C - 4.6355 at every coordinate, and
Psi(r) <= log2(2e(r + 2)).)

This is where the method stops. When every influence is small compared with the variance, eps_v is small at
every coordinate, the free fibres carry almost all of the down-set, and Lemma 2 is only as good as subadditivity.
Majority shows that the free and blocked parts can still be perfectly aligned: for odd n, a(T) = 0 when |T| is
odd and a(T) + b(T) = 0 when |T| is even and nonempty, so B_v = 0 although eps_v ~ n^{-1/2}. Balanced tribes
and monotone graph properties live in this regime, and FEI there contains the log^2 n influence bound for graph
properties (continuation 2026-09-24-monotone, Section 1).

Three precise statements the data supports (24 September, afternoon):

(C1) IS FALSE (24 September, 16:4x; paper Proposition 7.2, `code/c1_refute.py`, `logs/c1_refute.log`). Replace every
y_j in the Remark 7.1 function g_n (Remark 6.1 in the older numbering used elsewhere in this report) = Maj_n(y) OR (z AND [y = y*]) by a majority of k new variables. The inner functions
are balanced, so the spectral sample of the composition is that of g_n with each y_j replaced by an independent
spectral sample of Maj_k; Inf_z and Delta_z do not change (the H(Maj_k) terms cancel because
Inf_{y_j}(g) = (Inf_{y_j}(g_0) + Inf_{y_j}(g_1))/2), while each inner variable has influence Inf_{y_j}(g_n) Inf(Maj_k).
For k >= 109 (n = 5, 546 variables) z is the unique most influential coordinate and Delta_z/Inf_z = 6.6596 > 6.0037;
the least k for n = 3, 5, 7, 9, 11, 13 is 17, 109, 1071, 12659, 162355, 2176477 and the ratio is 5.92, 6.66, 7.42,
8.22, 9.06, 9.93, unbounded like (n - 3 log2 n)/2 by Remark 7.1. Brute force on the 10- and 16-variable compositions
(k = 3) matches the identities to 4e-16. The example was already in the failed-routes list of the 24 Sep 02:36
continuation (route 2); the n <= 6 exhaustive check could not see it because it needs hundreds of variables.
Stronger (`code/log_sharp.py`, `logs/log_sharp.log`): with a threshold [|y| >= k] in place of Maj_n and y* of weight
k - 1, 2^n Mhat(T) = 2 K_{k-1}(|T| - 1; n - 1) (Krawtchouk; exact big-integer sums, mpmath per pair, checked against
brute force at n = 5, 9, 13) and for the best k, n = 21, 31, 41, 61, 81: Delta_z/Inf_z = 20.64, 29.85, 39.39, 58.79,
78.41 against log2(4m/Inf_z) = 20.62, 30.17, 41.09, 60.29, 80.58; Theorem 1.3's bound is 6.1-8.3 above. So the
logarithm of Theorem 1.3 is attained with coefficient 1 (numerically; Remark 7.1 proves 1/2), and after composition
this happens at the unique most influential coordinate. Consequence: no rule that picks the coordinate by the size of
its influence (absolute or relative to m; composition with balanced functions leaves m unchanged) can work. The
averaged form (section 5a) needs no choice; max sum_v B_v / I is 3.03 over all monotone n = 6 and 3.61 on everything
computed (matching8). The original (C1) text follows as the record of what was conjectured.

(C1, as stated earlier - refuted above) The most influential coordinates work (uniform measure). For monotone f, every coordinate v* of largest influence
has Delta_{v*} <= K Inf_{v*} with K about 6 (`code/maxinf_step_all.py` takes the WORST coordinate among ties; the first
run, `code/maxinf_step.py`, took the best, and both give the same maxima): over all 7,828,354 monotone functions of six variables and the
families (matching8 6.004, tribes 4.5-4.7, K6-triangle 4.83, majority 0) the ratio at v* is at most 6.004, and its
worst case equals the worst case of rho_0 = min_v Delta_v/Inf_v in each reported row (n <= 5, the first 200,000
functions of n = 6, each family; `code/maxinf_step.py`, `logs/maxinf_step.log`). (C1) implies FEI for monotone
functions with constant K; Lemma 2 proves it only when Inf_{v*} is a fixed fraction of m.
For perfect matchings the ratio is exact at every size (`code/matching_c1.py`, `logs/matching_c1.log`; the spectrum of
an OR of independent parts factorises, H(M_k) = -8p^k + 4k p^(k-1) H_edge - phi(4 (9/16)^k) + phi((2p^k - 1)^2) with
p = 3/4, checked against brute force for k <= 8): Delta_v/Inf_v = 4.00, 3.25, 4.15, 5.39, 5.78, 5.94, 6.00, 6.0037 for
k = 1..8, then decreasing to 5.7353 as k -> oo. So the 8-edge matching is the worst matching, and any constant in (C1)
is at least 6.0037. An annealing search maximising the ratio at the worst most influential coordinate
(`code/adv_c1.py`, `logs/adv_c1.log`) found 5.713 at n = 8, 5.532 at n = 10 and 5.347 at n = 12 - nothing near the matching's 6.0037. Over disjunctions of k <= 40
disjoint copies of every monotone function of at most four variables (exact, same product formula;
`code/or_copies_c1.py`, `logs/or_copies_c1.log`), the largest ratio is 6.00375, attained by AND_2 at k = 8 - the
matching again (conjunctions are covered by duality). So K = 6.0037 is the natural conjecture for (C1).

(C2) The biased step for graph gates (Section 4a): at the coordinate of largest biased Var(D_v F), the biased step is at
most 2 + 4 log2 e times the decrease of I - Var (worst 7.765 over 400 random graph gates; 6.87 off single edges).

(C3) PROVED 24 Sep 14:1x (paper Lemma 6.4): the credit pays for the Jensen-Shannon part exactly. The one-pair Jensen
gap below is Ent_nu(g^2) on the two-point space nu = (1-q, q) with g = (|a - t d|, |a + d/t|), and d^2 = q(1-q)(w-u)^2 >=
Var_nu(g); the two-point logarithmic Sobolev inequality with the optimal constant of Diaconis and Saloff-Coste (Ann.
Appl. Probab. 6 (1996), Theorem A.1) gives J_q <= c(q) d^2 (nats), c(q) = ln((1-q)/q)/(1-2q), best possible for a single
pair; and with x = |1 - 2q|, c(q) = 2 sum x^(2k)/(2k+1) <= 2 + sum_{k>=1} x^(2k)/k = 2 + ln(1/(4q(1-q))) termwise. The
numerical sup of Phi_q below IS c(q) (2.7465 at q = 0.1, 2.1182 at 0.3, 2 + (8/3)(1/2 - q)^2 near 1/2). At q = 1/2 this is
Gross's two-point inequality, and Lemma 2.1 of the paper now has that one-line proof (Ent(g^2) <= (1/2)(|u+w| - |u-w|)^2
= 2 min(u^2, w^2)) in place of the series argument. Numerical record (`code/js_biased.py`): With t = sqrt(q/(1-q)), the biased
restriction's Jensen gap for one pair, J_q(a, d) = phi(a^2 + d^2) - (1-q) phi((a - t d)^2) - q phi((a + d/t)^2), is
homogeneous of degree 2, and numerically J_q(a, d) <= d^2 (log2(1/sigma^2) + 2/ln 2) for every q and all a, d, with
equality only in the limit q = 1/2, |a/d| -> oo (the uniform bound of Lemma 2.1). In closed form, with p = sin^2(psi)
the mixing probability of the two restricted coefficients: KL(Bern(p) || Bern(q)) <= BC(Bern(p), Bern(1-q))^2
(2 + ln(1/(4q(1-q)))) in nats, BC the Bhattacharyya coefficient. If (C3) holds, the biased step at v is at most
[phi(d_empty^2) - d_empty^2 log2(1/sigma_v^2)] + sum_{T nonempty} E(a_T^2, d_T^2) + (2/ln 2) sum_{T nonempty} d_T^2, so (C2)
reduces to an erasure bound with no credit left - which for the balanced matching holds because every pair is
lopsided, and which the second-moment argument of Lemma 2 cannot give. Status of (C3): in (p, q) form it reads
D(p || q) <= (2 + ln(1/(4q(1-q)))) (1 - BC(p, q)^2), a sharpened relative of the Yang-Barron bound
D <= (2 + log sup(P/Q)) H^2 (which loses a factor 2 on the logarithm here); it holds on a 4001 x 800 grid in (p, q)
with equality only at p = q (`code/c3_reduce.py`, `logs/c3_reduce.log`). The easy proof - compare derivatives in the
angle psi with p = sin^2 psi from psi = gamma, q = sin^2 gamma - does NOT work: the two one-variable inequalities it
needs fail at extreme parameters (a = tan gamma = 1e-4, x = tan psi/tan gamma ~ 5e7; and a = 16.6, x = 0.019), so a proof
must use the integrated form. The margin of (C3), 2 + ln(1/(4q(1-q))) - sup_s Phi_q(s) in nats with s = a/d, is 0.614
for small q (q = 1e-8 to 1e-4), 0.54 at q = 0.01, 0.28 at 0.1, 0.056 at 0.3, and near q = 1/2 it is (4/3)(1/2 - q)^2 to
leading order (60-digit values 0.00334 at q = 0.45, 1.33e-4 at 0.49, 1.33e-6 at 0.499, 1.33e-8 at 0.4999; the sup sits
at s ~ 1/(1/2 - q)); double-precision runs show spurious negative margins at |s| ~ 1e7 from cancellation
(`code/c3_margin.py`, `code/c3_mp.py`, logs beside them). A proof has to be exact to second order around the
uniform case q = 1/2, where (C3) is Lemma 2.1's bound J <= (2/ln 2) d^2.

## 5a. A local form of the conjecture (added 24 September, noon)

Put R(f) = sum over S with P(S) > 0 of P(S) sum_{v in S} log2+ (P(S - v)/P(S)), with log2+ t = max(log2 t, 0). For
every Boolean function (paper Proposition 6.3)

    R(f) <= sum_v B_v <= min(H(f), R(f) + log2(2e) I(f)).

The bound by H is the chain rule (conditioning on more coordinates lowers entropy); the two bounds by R come from
Y log2+(X/Y) <= E(X, Y) <= Y (log2(2e) + log2+(X/Y)). With Delta_v = B_v + JS_v and JS_v <= (2/ln 2) Inf_v, on every
restriction-closed class H <= C I implies R <= C I, and R <= K I implies H <= (K + 5.33) I. So the conjecture, for
all functions or on any restriction-closed class, is equivalent to a statement about one step of the spectral
sample: removing one element of S raises its weight by at most a bounded factor, on average in the logarithm. For
monotone f the ratio at S = T + v with T nonempty is (1 + b(T)/a(T))^2, and Lemma 2 bounds its logarithmic average
with the second moments of a and b alone; the alignment of Section 5 is what a sharper bound would have to use.

Numerically (`code/local_form_check.py`, `logs/local_form_check.log`) the two inequalities hold on all monotone
functions of at most five variables and on 20,000 random functions of 3 to 8 variables. R is much smaller than H:
over monotone functions of five variables max R/I = 1.18 against max H/I = 3.62, and over the random functions
max R/I = 1.06 against max H/I = 3.84. Over all 7,828,354 monotone functions of six variables max R/I = 1.34 against
max H/I = 3.74 (`code/r_survey.py`, `logs/r_survey.log`). Families: majority has R = 0 exactly (every pair has one
zero weight); tribes 3x3 to 4x4 have R/I <= 0.68; threshold functions 1.16-1.24; the Remark 6.1 functions g_n have
R/I -> 0; 'K6 contains a triangle' 1.63 (H/I 3.99); perfect matchings are the largest, R/I 1.25, 1.79, 1.85, 1.81
for 4, 6, 8, 10 edges (H/I up to 4.52). Lexicographic threshold functions [x >= t as a binary number], Hod's family
for lower bounds on the FEI constant, over 150-400 thresholds for each n = 10, 12, 14, 16: max R/I 1.10-1.11 (at
t/N near 0.834) while max H/I is 3.90-3.98 (`code/lex_check.py`, `logs/lex_check.log`). So on everything tested
R/I < 1.9 while H/I reaches 4.5: the one-step quantity is small, and the conjecture in this form asks for a
constant near 2. A simulated-annealing search over monotone functions (moves keep monotonicity; starts from threshold,
random 2/3-DNF and tribes-like functions; `code/adv_local.py`, `logs/adv_local.log`) maximising R/I found 1.754 at
n = 10, 1.415 at n = 12 and 1.388 at n = 14 - all below the matchings - and, maximising H/I, 3.84 at n = 10 and 4.02 at
n = 12. For a perfect matching the value is explained exactly: removing v from S changes the weight only if
v is the one element of S on its edge, and then by the factor 9, so the bulk of R/I is (2/3) log2 9 / (4/3) = 1.58;
the rest comes from S = {v}, whose removal lands on the large weight P(empty set).

## 5c. Where the monotone case stands (24 September, evening)

Equivalent forms, on any class closed under restrictions (monotone functions are one): (i) H <= C I; (ii) every
nonconstant member has a coordinate with Delta_v <= K Inf_v; (iii) the averaged erasure sum_v B_v <= K I (paper
Prop 7.4: sum_v B_v <= H, and B_v <= K Inf_v at some v gives (ii) with K + 2/ln 2); (iv) R <= K I; (v) for every
down-set D with uniform measure mu_D, the distribution pi_D(T) = (|D|/2^n)(E_{mu_D} chi_T)^2 has entropy at most
C E_{pi_D}|T| (for q <= 1/2, P(T) = 4q pi_D(T) on nonempty T, and the log(1/q) difference is absorbed by edge
isoperimetry I >= 2q log2(1/q)); (vi) a block version: if every nonconstant member has a nonempty block W with
H(S cap W | S minus W) <= K E|S cap W|, then H <= (K + 2/ln 2) I - the block Jensen-Shannon term is
(1/ln 2) sum_T Ent_x(g_T^2), g_T(x) = sum_U Fhat(T + U) chi_U(x) on the W-cube, and Gross's inequality on that cube
bounds it by (2/ln 2) E|S cap W|, which contains Lemma 2.1 as |W| = 1. Tribes pass (vi) with W = one tribe. Blocks
never beat single coordinates for the erasure: by the chain rule H(S cap W | S - W) >= sum_{v in W} B_v, so the block
ratio is at least min_{v in W} B_v/Inf_v. Measured on minterm and maxterm blocks (`code/block_minterm.py`,
`logs/block_minterm.log`): all monotone n <= 5, matchings to 8 edges, tribes, K5/K6 triangle, majority to 13 variables,
random 2- to 5-DNFs on 14 variables - the best block ratio is 1.28-3.68, always at or above the best coordinate
(majority: blocks 1.28-1.83, coordinates 0). So blocks are a proof device only.

A per-pair lemma for the biased step (numerical, `code/pair_credit.py`, `logs/pair_credit.log`): with s = a/d and
sigma^2 = 4q(1-q), E(a^2, d^2) + J_q(a, d) - log2(1/sigma^2) d^2 <= d^2 (C0 + log2(1 + sigma^2 s^2)) for every q, sup
C0 = 4.79880 (limit q -> 0 at s ~ 0.862/sqrt q; 4.32809 = log2 e + 2/ln 2 at q = 1/2), 80-digit arithmetic. In angle
form (q = sin^2 beta, d^2/(a^2 + d^2) = sin^2 psi) the left side is (a^2 + d^2)(h(sin^2 psi) + D(sin^2(beta + psi) ||
sin^2 beta) - sin^2 psi log2 csc^2 2 beta). It lets the credit pay the Jensen-Shannon part and normalise the erasure at
once; with the biased down-set of Lemma 6.3 (Jensen with weights d_T^2 and sigma^2 sum(a^2)/rho <= 16 + 16/theta when
pi <= 1/2) the pi <= 1/2 case of Theorem 1.10 would cost at most 2.12 + C0 + log2(17 + 16/theta) <= 12.6 + (w - 1)
log2(1/eta), against 14.24 + 2w log2(1/eta) now; the pi > 1/2 case was not redone. Not in the paper: no proof of the
pair inequality written yet, and it leaves the eta -> 0 problem where it was.

What cannot work, with the example that kills it:
- choosing v by the size of its influence, absolute or relative (Prop 7.2; balanced composition leaves m unchanged);
- choosing v from (Inf_v, eta_v) alone, at a maximal element of the desirability order, by shifting to a regular
  function (continuation 2026-09-24-monotone, routes 1-3);
- any step bound using only the second moments of the blocked and free parts: Theorem 1.3 is attained (Remark 7.1),
  so the small-relative-influence regime needs the alignment of Remark 7.3 (majority: exact parity; tribes: the pairs
  meeting v's own tribe have equal weights and the rest carry a 2^{1-w} fraction);
- the averaged half-moment sum_v sum_T |Fhat(T) Fhat(T + v)| <= K I (which would give (iv) via log2 x <= (2/ln 2) sqrt x):
  false for g = Maj_n(y) OR OR_{y* in L} (z_{y*} AND [y = y*]), L the layer of weight (n-1)/2 with one fresh z per point;
  each z contributes 2^{-n} ||Ahat||_1 (A = (1 - 2 Maj_n) - 1_L) and there are C(n, (n-1)/2) of them. Exact
  (`code/layer_lookup.py`, `logs/layer_lookup.log`; brute force agrees at 6 and 15 variables): the z half-moment is
  0.75, 3.72, 307.6, 3.6e6, 1.8e12 times I at n = 7, 15, 31, 61, 101. The log form is fine there: the summed erasure
  over the z is 0.73-0.94 I (B_z/Inf_z ~ n, both parities costly because 1_L breaks majority's parity), and H/I is
  4.13, 4.20, 4.24, 4.27 at n = 101, 201, 401, 801, increments shrinking by ~0.64 per doubling (limit about 4.32, below
  the 4.52 of the 10-edge matching); majority itself 2.73, 2.78, 2.82, 2.84 (`code/sym_limit.py`, `logs/sym_limit.log`).

Why the full case is hard: (v) and (iii) restricted to transitive functions are (ii) at any coordinate, and FEI for
monotone graph properties gives total influence Omega(log^2 n) (Friedgut-Kalai), where the best known bound is
log^2 n/(log log n)^2 (Kelman-Kindler-Lifshitz-Minzer-Safra 2020). In the orbit picture the step for a graph property
is bounded only if adding an edge to a typical spectral sample rarely creates new vertices, which is the content of
that bound. The biased small-eta problem for graph gates has the same shape: combining each pair's erasure and
Jensen-Shannon parts with the credit turns the pair ratio a^2/d^2 into sigma^2 a^2/d^2 = 4(1-q)^2(1 + gamma/alpha)^2,
whose second moment is again ~1/theta (theta = blocking probability under mu_D); the matching at small bias beats it by
exact cancellation gamma = -alpha on the sets that meet v's partner, which a second-moment argument cannot see.

## 5b. Lean (added 24 September, afternoon)

`lean/FEIMonoPsi.lean` checks, in Lean 4 (v4.33.1) with Mathlib (revision 0df444a360ea, tag v4.33.1), the scalar core of
Lemma 2: with
Psi(r) = log(r + 2 sqrt r + 2) (the paper's Psi is log2 e + Psi/ln 2, an increasing affine image): X log(1 + Y/X) <= Y
(ent_le, which gives E(X, Y) <= Y log(e(X+Y)/Y)); (1 + s)^2 + 1 <= s^2 + 2|s| + 2 (sq_bound, which with sqrt(s^2) = |s|
gives psi(s) <= Psi(s^2)); Psi concave and nondecreasing on [0, oo) with Psi(0) > 0 (Psi_concave, Psi_mono,
Psi_zero_pos); g(z)/z nonincreasing for g concave on [0, oo) with g(0) >= 0 (ratio_anti); and the Jensen step
(jensen_chain): weights w >= 0 with 0 < sum w <= eps and sum w s^2 <= c give sum w Psi(s^2) <= eps Psi(c/eps).
`lean/FEIMonoRec.lean` checks the arithmetic of Lemma 3: p(1) = 1 and p(j+1) >= (p(j) - 2 delta)/2 give
2^(k-1) p(k) >= 1 - delta (2^k - 2), and with p(k) <= 2 delta, delta (2^(k+1) - 2) >= 1. Both files: lake env lean exit 0,
no warnings, #print axioms lists only propext, Classical.choice, Quot.sound (`lean/*.check.txt`). The Fourier and
probabilistic parts (the down-set identity, the pair decomposition) are checked numerically, not in Lean.

## 6. Numerical checks

- `code/downset_check.py`: Lemma 1 and the first, cruder form of Lemma 2, B_v <= c0 Inf_v + log2(5e)(4m - Inf_v),
  at every coordinate of every monotone function with n <= 6 (`logs/downset_n1_6.log`): identity error at most
  7.2e-16, largest ratio of the two sides 0.489 (at n = 5 and 6), no violation.
- `code/relhan_check.py`: Theorem 2 at every coordinate and Corollary 5 for every monotone function with n <= 6
  (`logs/relhan_n1_6.log`): the largest ratio of Delta_v to the bound of Theorem 2 is 0.688 and of H to the bound
  of Corollary 5 is 0.528, both over the 7,828,354 functions of six variables.
- `code/width_check2.py`: Theorem 2 and Lemma 3 on complete, complete bipartite, crown, Paley, random regular and
  complete multipartite graphs up to 16 vertices, random monotone DNFs of width 3 and 4 with up to 120 terms, and
  random monotone CNFs (`logs/width_check2.log`): the largest ratio of Delta_v to the bound of Theorem 2 is 0.68,
  the chosen coordinate uses at most 0.59 of c_k, and Lemma 3's lower bound on eps holds on every row.
- `code/width_check.py`, `code/gdnf_battery.py`: 2-DNFs of paths, cycles, stars, grids, hypercubes, the Petersen
  graph, matchings and G(n, p) up to 20 vertices, the same with singleton terms, and random DNFs of width 3 and 4
  up to 20 variables (`logs/width_check.log`, `logs/battery1.log`). The cruder form of Lemma 2 holds at every
  vertex; the smallest relative influence of the most influential vertex over the width-2 functions is exactly 2/3,
  attained by perfect matchings, as Lemma 3 predicts. The largest H/I in these families is 4.52 (a perfect
  matching of 10 edges; the matching limit is about 4.87), and rho_0 = min_v Delta_v/Inf_v is at most 6.00.
- `code/adversary.py`: simulated annealing over monotone functions of 8 and 10 variables, moves that keep
  monotonicity, maximising the ratio of Delta_v (or B_v) to its bound in Theorem 2 (or Lemma 2): the largest
  ratios found are 0.651 and 0.579 (`logs/adversary.log`).
- `code/avg_step.py`: the averaged step sum_v Delta_v/I over all monotone functions with n <= 6 (maximum 5.302,
  at x3 x4 (x0 OR x2)(x1 OR x5); `logs/avg_n1_5.log`, `logs/avg_n6.log`).
- `code/dt_check.py`: decision-tree complexities by dynamic programming over subcubes and the OSSS influence bound
  (`logs/dt_check.log`; Section 4b).
- `code/local_form_check.py`, `code/r_survey.py`: the constants of Theorem 1.6 and the inequalities of Proposition 6.3
  (`logs/local_form_check.log`, `logs/r_survey.log`; Section 5a).
- `code/biased_matching.py`, `code/biased_step.py`, `code/biased_induction.py`, `code/biased_induction2.py`,
  `code/biased_which_v.py`: the biased restriction step (Section 4a).
- `lean/FEIMonoPsi.lean`, `lean/FEIMonoRec.lean`: Lean checks (Section 5b).
- `paper/fei_monotone_width.tex`, `.pdf`: the same results written as a short paper.
