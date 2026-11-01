# W-witness-cost: the joint witness cost of the queue law beyond addressing

Route: W-witness-cost (campaign ledger items C008, C009, C020). Working notes, 12 Oct 2026.
Full FEI remains OPEN. Nothing here claims otherwise.

Reading order (sections were appended as the work went): 0-8 (framework, class K, Theorem 5.1, obstruction N1,
direct FEI, attempts), 11 (term decision lists, Theorem 11.1, Corollary 11.2), 12 (reduction to the rank term,
Proposition 12.1, evidence, refinement), 13 (summary and next step), then 12.4 (read-once formulas at large depth),
then 9 (counterexample checks). Numerical tables: data/tables.json. Claims ledger: CLAIMS.json.

Conventions: log = log base 2, ln = natural log. Uniform cube, Boolean outputs in {-1,1},
p(A) = fhat(A)^2, H(f) = sum_A p(A) log(1/p(A)), I(f) = sum_A |A| p(A), v = Var(f) = sum_{A != empty} p(A).
For a subprobability "mass vector" m (nonnegative, finite total) write Hm(m) = sum m_k log(1/m_k) (no normalization).

## 0. Sources read

- CLAIMS.md C008, C009, C020 (and C001-C003, C010-C014, C035 for scope).
- baseline/current-threshold-paper.tex, Section "Read-k unions of structured gates": queue reference
  (lines 822-860), witness run and cost (862-941), averaging (943-1020), "A bound retaining the joint
  witness cost" (Prop. joint-witness, 1184-1295), "The addressing benchmark" (1297-1335), "Scope of the
  refinement" (1337-1346).
- REPORT.md "Main route I: complete joint descriptions" (three improvements: all witnesses, correlated
  assignments, scale mixtures) and SEED_LEMMAS.md section 2 (mixtures of complete reference laws).
- COUNTEREXAMPLES.md X001-X013 (all read; applicability recorded in section 9 below).
- Fleet state at start (00:1x 12 Oct): B02 joint-coding agents A006-A010 had produced no report yet.

## 1. The objects (restated exactly, from the paper)

Union representation. f = h_1 OR ... OR h_N (true = +1), each gate h_l a Boolean function of at most M
regular functions h_{l,r}; R_l = relevant set of h_l; d(j) = number of gates containing coordinate j.
p_l = P[h_l = 1], pi_l = min(p_l, 1/2). Each regular inner function carries a fixed desirability order;
r_{l,r}(j) = rank of j. For s >= 1 and j in R_l:
  theta^l_s(j) = max_{r: j in supp h_{l,r}} min{1, (s / r_{l,r}(j))^a},   a > 1 (paper: a = 6/5),
  Z^l_s = e_s(theta^l_s) (elementary symmetric polynomial), Z^l_s <= (e M a/(a-1))^s.

Queue law Q_{1,lambda} (paper). Independently make gate l a root with probability lambda pi_l/(1+lambda pi_l).
Process each queued occurrence of a gate l: (i) s >= 1 w.p. 1/(s(s+1)); fail if s > |R_l|; else choose an
s-subset B of R_l w.p. prod_{j in B} theta^l_s(j) / Z^l_s. (ii) c >= 0 w.p. 1/((c+1)(c+2)); a uniform
multiset of c elements of B; for each occurrence of j choose uniformly one of the d(j) gates containing j and
append it. Output the union of the selected subsets when the queue empties. Q_{1,lambda}(A) = probability of a
successful finite run with output A. Sum_A Q_{1,lambda}(A) <= 1.

Witness cost (Prop. joint-witness). For an assignment tau (A partitioned into A_l, s_l = |A_l|, used gates F),
a directed spanning forest T on F whose roots are one representative per source strongly connected
component of the incidence digraph, attachments j_e, child counts c_l:
  C_lambda(A; tau, T) = sum_{roots r} log(1/(lambda pi_r)) + sum_{edges e} log d(j_e)
     + sum_{l in F} [ log(s_l(s_l+1)) + log Z^l_{s_l} - sum_{j in A_l} log theta^l_{s_l}(j) ]
     + sum_{l in F} [ log((c_l+1)(c_l+2)) + log binom(s_l+c_l-1, c_l) ],
and log(1/Q_{1,lambda}(A)) <= Lambda_lambda + C_lambda(A; tau, T), Lambda_lambda = sum_l log(1 + lambda pi_l).
Hence (Gibbs with Q(empty) = 1-v, Q(A) = v Q_{1,lambda}(A)):
  H(f) <= h(v) + v Lambda_lambda + sum_{A != empty} p(A) min_{tau,T} C_lambda(A; tau, T).        (W)

C020 asks for an absolute C with RHS(W) <= C I(f) on a new class, all terms kept.

## 2. Sharpest version attacked

(T1, positive) Find a class K, strictly beyond addressing (C009), beyond C001-C003 and C035, and a
representation of each f in K for which the COMPLETE right side of a valid queue-law bound is <= C I(f) with
C absolute (no dependence on N, k, depth, n, biases).

(T2, negative) Decide whether the paper's law with ONE global root-odds parameter lambda (and the
scale-mixture repair of SEED_LEMMAS section 2) can achieve T1 on such a class when only minimum-cost
witnesses are used; if not, identify the missing ingredient exactly.

Status of both: see sections 4-8 below and CLAIMS.json.

## 3. Two elementary lemmas about the queue law

**Lemma 3.1 (mutually exclusive unions).** Suppose f = h_1 OR ... OR h_N and at every input at most one
h_l equals 1. Then for every A != empty, fhat(A) = sum_l hhat_l(A). In particular fhat(A) != 0 implies
A subset of R_l for some l (indeed for some l with hhat_l(A) != 0).
*Proof.* Pointwise (1+f)/2 = sum_l (1+h_l)/2 by exclusivity. Take the coefficient of chi_A, A nonempty:
fhat(A)/2 = sum_l hhat_l(A)/2. A coefficient hhat_l(A) vanishes if A contains a coordinate irrelevant to h_l. QED

**Lemma 3.2 (sum over single-root witnesses).** Fix any union representation and any root odds
rho_l > 0 (the paper takes rho_l = lambda pi_l; the proof below is the paper's, unchanged). Let O(A) be the
set of gates l with A subset of R_l. Then, with s = |A| and Lambda_rho = sum_l log(1+rho_l),
  Q(A) >= 2^{-Lambda_rho} * sum_{l in O(A)} rho_l * [1/(s(s+1))] * [prod_{j in A} theta^l_s(j) / Z^l_s] * (1/2).
*Proof.* For l in O(A) let E_l be the event: the root set is exactly {l}; the (only) occurrence of l draws
s = |A| (allowed since s <= |R_l|) and then B = A; then draws c = 0. On E_l the queue empties and the output
is A, so E_l is a successful finite run with output A. P(root set = {l}) = (rho_l/(1+rho_l)) prod_{l'!=l}
1/(1+rho_l') = rho_l 2^{-Lambda_rho}; the other three factors are the stated choice probabilities. The events
E_l for distinct l have distinct root sets, hence are disjoint, and Q(A) >= sum_l P(E_l). QED

Taking only the largest term recovers the paper's single-root witness cost
  log(1/(rho_l)) + log(s(s+1)) + log Z^l_s - sum_{j in A} log theta^l_s(j) + log 2,
which is C_lambda(A; tau, T) with F = {l}, no edges, c_l = 0, rho_l = lambda pi_l.
(Remark: gate-dependent odds rho_l are a harmless generalization of C008: the root step is still independent
Bernoulli, the proof of Prop. joint-witness is word for word the same. They are not needed for Theorem 5.1.)

## 4. The class K (selector trees with regular leaves) and its exact spectrum

Coordinates split into control X and data Y, disjoint. T is a decision tree on X: each internal node v carries a
label x(v) in X and two children (taken when x(v) = +1, -1); no label repeats along a root-to-leaf path.
Leaf i has cell C_i (the subcube of x following the path), codimension c_i = number of internal nodes on the
path, p_i = 2^{-c_i}. Each leaf carries a REGULAR Boolean function g_i of y (paper's sense: unate with a total
desirability order; constants and all LTFs included), mean mu_i, Var_i = 1 - mu_i^2, P_i = P(g_i = 1) = (1+mu_i)/2.
Hypothesis (DS): for i != i', the nonempty Fourier supports of g_i and g_i' are disjoint. f(x,y) = g_{i(x)}(y).
CORRECTION (self-audit, same day): for UNATE leaves (DS) is the same as disjoint relevant data blocks. Indeed a unate g
has |ghat({j})| = Inf_j(g) > 0 for every relevant j (after orienting j increasing, d_j g >= 0, so
ghat({j}) = E d_j g = E|d_j g| = Inf_j). If j were relevant to two leaves, {j} would lie in both supports. So for
regular leaves K is exactly: selector trees whose leaves are regular functions on pairwise disjoint fresh data blocks.
(Proposition 4.1 (i)-(v) are stated under (DS) because their proofs only use (DS).)

K_EM: (DS) and all mu_i equal (any tree shape). K_RO: (DS) and the tree read-once: the labels x(v) are
pairwise distinct over all internal nodes (arbitrary means). K = K_EM union K_RO.

Examples. Addressing f(a,y) = y_a is in K_EM (complete oblivious tree on the address bits, leaves y_u, mu = 0);
so are all subcube selectors with balanced regular DS leaves. K_RO contains decision lists
x_1 ? g_1 : (x_2 ? g_2 : ...) with regular outputs of arbitrary bias, and read-once trees of any shape.

For a node v write anc(v) for the strict ancestors, d_v = |anc(v)| + 1, P(reach v) = 2^{-(d_v-1)},
m_+(v), m_-(v) for the mean of f given that v is reached and x(v) = +1 (resp. -1), m(v) = (m_+ + m_-)/2,
Delta_v = |m_+(v) - m_-(v)|/2, w_v = P(reach v) Delta_v^2.

**Proposition 4.1 (exact spectrum).** (i) For every decision tree and arbitrary leaf functions,
fhat(T u B) = sum_i 1hat_{C_i}(T) ghat_i(B) for T subset X, B subset Y, where 1hat_{C_i}(T) = 2^{-c_i} sigma_i(T)
(a sign) if T is a subset of the path variables of i, and 0 otherwise.
(ii) Under (DS): if B != empty and ghat_i(B) != 0 then fhat(T u B) = 1hat_{C_i}(T) ghat_i(B), and the spectral
mass of the "block" of leaf i is W_i = sum_{T, B != empty} fhat(T u B)^2 = p_i Var_i, uniformly spread over T
(each T subset of path(i) carries the fraction 2^{-c_i}).
(iii) The sets inside X ("phi-sets") have fhat(T) = phihat(T), phi(x) = mu_{i(x)}. Under K_EM, phi is constant.
Under K_RO, phihat(T) != 0 forces T = S u {v} with v the deepest node of T and S subset anc(v), and then
|phihat(T)| = 2^{-d_v} |m_+(v) - m_-(v)|; the 2^{d_v - 1} sets of node v carry total mass w_v.
(iv) Under K_RO: Inf_{x(v)}(f) = P(reach v) (1 - m_+(v) m_-(v))/2 >= P(reach v) Delta_v.
(v) I(f) = I_X^blk + I_Y + I^phi with I_X^blk = sum_i p_i Var_i c_i/2, I_Y = sum_i p_i I(g_i),
I^phi = sum_v w_v (d_v+1)/2 (the last term absent under K_EM), and the control influence
I_X(f) = sum_{u in X} Inf_u(f) = I_X^blk + I^phi.

*Proof.* (i) f = sum_i 1_{C_i}(x) g_i(y), with 1_{C_i} = prod_{u on path} (1 + s_u x_u)/2. (ii) Under (DS) only the
leaf whose support contains B contributes; Parseval for 1_{C_i} gives sum_T 1hat_{C_i}(T)^2 = p_i, and
sum_{B != empty} ghat_i(B)^2 = Var_i. (iii) phihat(T) = sum_i mu_i 1hat_{C_i}(T). Nonzero terms need T inside a
path, so T is a chain; let v be its deepest node. Under read-once labels, a leaf's path contains x(v) iff the leaf
lies below v, and then contains all of anc(v) u {v} with the same signs on anc(v). Splitting the leaves below v
by the sign at v gives phihat(T) = sigma(S) 2^{-d_v} (m_+(v) - m_-(v)) because
sum_{i below v, sign +} mu_i 2^{-c_i} = 2^{-d_v} m_+(v). There are 2^{d_v-1} choices of S; the total mass is
2^{d_v-1} 4^{-d_v} (m_+ - m_-)^2 = w_v. (iv) Inf_{x(v)}(f) = sum_{A containing x(v)} fhat(A)^2. By (ii)-(iii) this is
w_v + (1/2) sum_{v' strictly below v} w_{v'} + (1/2) sum_{i below v} p_i Var_i. The plus-subtree function L (as a
selector tree with root at the plus child) has 1 - m_+^2 = Var(L) = sum of the same two kinds of masses
rescaled by 2/P(reach v), and likewise for the minus side; together with the algebraic identity
(1 - m_+ m_-)/2 = ((m_+ - m_-)/2)^2 + (1 - m_+^2)/4 + (1 - m_-^2)/4 this gives the formula. Finally
1 - ab >= |a - b| for a, b in [-1,1] (it equals (1-a)(1+b) or (1+a)(1-b)), so (1 - m_+ m_-)/2 >= Delta_v.
(v) Sum |A| fhat(A)^2 using (ii)-(iii): a block set has |T| + |B| with T uniform on subsets of path(i)
(mean c_i/2) and sum_B |B| ghat_i(B)^2 = I(g_i); a phi-set of node v has size 1 + |S|, mean (d_v + 1)/2. QED

Exact checks (code/test_spectrum.py, integer Walsh transforms, Fractions): 400 random instances (200 read-once,
200 general trees; leaves = constants, AND_w, OR_w, random LTFs on fresh blocks; up to 15 variables): the
formula (i), the phi-set structure (iii), the influence formula (iv) and the decomposition (v) hold exactly.
(By the correction above, fresh blocks are the general case for regular leaves.)
Negative controls (same code): replacing the influence formula by (1 + m_+ m_-)/2 trips the test on 21/30 random
read-once instances; dropping the sign sigma(T) in (i) trips it on 27/30 (the non-trips are coincidences, e.g.
m_+ m_- = 0 or all-positive signs). Coverage: 51/60 read-once instances have nonzero phi-sets; 11/60 general trees
repeat a variable across paths.

## 5. Theorem W1: the paper's queue law has complete expected code length <= 17 I on K

Representation. For f in K let G = {i : g_i is not identically -1}. Gates h_i = kappa_i AND [g_i = 1], i in G,
kappa_i = 1[x in C_i]. They are mutually exclusive and their union is f. Each gate is a Boolean function of M <= 2
regular functions: kappa_i (a conjunction of c_i literals; all its coordinates are equally desirable, so we fix the
path order, root first, as its desirability order: rank r_kappa = depth position) and g_i (any fixed desirability
order). R_i = path variables of i u relevant variables of g_i (every path variable is relevant to h_i because
g_i is not identically -1). The law is the paper's Q_{1,lambda} with lambda = 1 and a = 6/5; pi_i = min(p_i P_i, 1/2).

**Theorem 5.1.** For every f in K, with this representation,
  H(f) <= h(v) + v Lambda_1 + sum_{A != empty} fhat(A)^2 log(1/Q_{1,1}(A)) <= 17 I(f).
More precisely the right side is at most
  h(v) + (log e + 2) v + [log2(6 e a/(a-1)) + max(2 + a + (log e)/e, 2 + a (1 + ln 2)/ln 2)] I(f),
which at a = 6/5 is <= 2I + 3.443 I + (6.613 + 4.932) I < 16.99 I.
Under K_EM the bound uses only one (minimum-cost, single-root) witness per Fourier set. Under K_RO the phi-sets
use the sum over single-root witnesses (Lemma 3.2); Section 6 proves that the minimum-witness version is false.

*Proof.* Gibbs (paper eq:gibbs) with Q(empty) = 1-v, Q(A) = v Q_{1,1}(A) gives the first inequality. By
Proposition 4.1 every nonempty support set is a block set or (under K_RO) a phi-set. Exclusivity gives
Lambda_1 = sum_{i in G} log(1+pi_i) <= log e sum_i P(h_i = 1) = log e P(f = 1) <= log e.

Block sets. A = T u B with B != empty, ghat_i(B) != 0, T subset path(i); then i in G and A subset R_i.
Lemma 3.2 with the single gate i gives, with s = |A|,
  log(1/Q(A)) <= Lambda_1 + log(1/pi_i) + [log(s(s+1)) + 1] + log Z^i_s + a sum_{j in A} log+(r(j)/s).
Phi-sets (K_RO). A = T = S u {v}. Every leaf l below v with l in G has T subset R_l, and for each such l the
coordinates of T sit at the same path positions 1..d_v (they lie on the root-to-v path), so
prod_{j in T} theta^l_s(j) = Theta_v(T) := prod_{j in T} min(1, (s/r_v(j))^a) does not depend on l. With
Z^l_s <= (e M a/(a-1))^s, M = 2 (paper eq. union:normalizer; it holds for any M inner functions),
  log(1/Q(T)) <= Lambda_1 + log(1/ sum_{l in G, below v} pi_l) + [log(s(s+1)) + 1] + s log(2ea/(a-1))
                + a sum_{j in T} log+(r_v(j)/s).
We now average each bracket against p(A) = fhat(A)^2 and use the notation of Proposition 4.1.

(a) Rarity of block sets. log(1/pi_i) <= 1 if pi_i = 1/2, else = c_i + log(1/P_i); in all cases
log(1/pi_i) <= 1 + c_i + log(1/P_i). The block of leaf i has mass W_i = p_i Var_i. W_i c_i = 2 p_i Var_i c_i/2.
Claim A: for Boolean g with P = P(g=1) in (0,1), 4P(1-P) log(1/P) <= 2 I(g). Proof: q = min(P, 1-P); the
edge-isoperimetric inequality I(g) >= 2q log(1/q) (paper, proof of lem:levelentropy). If P <= 1/2:
4P(1-P)log(1/P) <= 4P log(1/P) = 2(2q log(1/q)) <= 2I(g). If P > 1/2: log(1/P) <= 1 and 4P(1-P) <= 4q, while
2I(g) >= 4q log(1/q) >= 4q since q <= 1/2. So W_i log(1/P_i) = p_i 4P_i(1-P_i) log(1/P_i) <= 2 p_i I(g_i).
Total: sum_i W_i log(1/pi_i) <= v_blk + 2 I_X^blk + 2 I_Y, v_blk = sum_i W_i.

(b) Rarity of phi-sets. If some pi_l = 1/2 below v, the sum is >= 1/2 and the log is <= 1. Otherwise
sum_{l below v} pi_l = sum_{l below v} p_l P_l = P(reach v)(1 + m(v))/2 (leaves with g == -1 have P = 0), so the
log equals (d_v - 1) + log(2/(1+m(v))). Since m_+, m_- >= -1, Delta_v <= 1 + m(v), and log(2/(1+m)) <= 1 + log(1/Delta_v)
(w_v > 0 forces Delta_v > 0). Both cases give <= d_v + log(1/Delta_v). Now w_v d_v = 2 I^phi_v - w_v and
w_v log(1/Delta_v) = P(reach v) Delta_v^2 log(1/Delta_v) <= ((log e)/e) P(reach v) Delta_v <= ((log e)/e) Inf_{x(v)}(f)
by Prop 4.1(iv) and max_{0<x<=1} x log(1/x) = (log e)/e. Total: <= 2 I^phi - v_phi + ((log e)/e) I_X(f).

(c) Size, child-count and normalizer. log(s(s+1)) <= s log 3 (s(s+1) <= 3^s for s >= 1), and
log Z_s <= s log(2ea/(a-1)). Total over all sets: v + log2(6ea/(a-1)) I(f).

(d) Rank. Block T-part: the elements of T have distinct path ranks <= c_i, so
sum_{j in T} log+(r(j)/s) <= sum_{j in T} log+(r(j)/|T|) <= psi_{c_i}(|T|), psi_c(t) = t log(c/t) (psi_c(0) = 0),
because each term is <= log(c_i/|T|). Given B, T is uniform on subsets of path(i), |T| ~ Bin(c_i, 1/2); psi_c is
concave on [0, c], so E psi_{c_i}(|T|) <= psi_{c_i}(c_i/2) = c_i/2. Contribution <= a I_X^blk.
Block B-part: for j in B with predecessor set U_j in g_i's order, s >= |B| >= |B cap U_j| + 1 and
r(j) = |U_j| + 1, so log+(r(j)/s) <= log(r(j)/(|B cap U_j| + 1)) = F_j(B minus j)/ln 2 >= 0 (F_j as in the
paper's lem:ranktail). Summing, sum_B ghat_i(B)^2 sum_{j in B} F_j(B minus j) = sum_j Inf_j(g_i) E_{nu_j} F_j
<= L_* I(g_i), L_* = 1 + ln 2, by lem:ranktail applied to d_j g_i in the monotone orientation (its support is an
antichain on every fiber of U_j by lem:pivotal-antichain). Each B is paired with every T with total weight p_i,
so the contribution is <= a (L_*/ln 2) I_Y.
Phi-sets: the elements of T have distinct ranks <= d_v, so the rank sum is <= psi_{d_v}(s); s = 1 + Bin(d_v - 1, 1/2)
has mean (d_v + 1)/2 and Jensen gives E psi_{d_v}(s) <= ((d_v+1)/2) log(2 d_v/(d_v+1)) <= (d_v+1)/2.
Contribution <= a I^phi.

Adding: H(f) <= h(v) + v log e + [v_blk + 2I_X^blk + 2I_Y] + [2I^phi - v_phi + ((log e)/e) I_X]
              + [v + log2(6ea/(a-1)) I] + [a I_X + a (L_*/ln 2) I_Y].
Use v_blk - v_phi + v <= 2v, I = I_X + I_Y, h(v) <= 2I (paper: h_2(v) <= 2I + (log e - 2) v), v <= I.
The coefficient of I_X is 2 + a + (log e)/e = 3.731 and of I_Y is 2 + a(1 + ln 2)/ln 2 = 4.932 (a = 6/5);
log2(36 e) = 6.613; log e + 2 = 3.443. Total < 2 + 3.443 + 6.613 + 4.932 = 16.988. QED

Remarks. (1) Nothing in the proof uses k, N, the depth, the number of data coordinates or the biases.
(2) Under K_EM no phi-sets exist, every set has a unique owner gate, and the minimum-cost witness suffices; the
addressing benchmark C009 is the special case (complete tree, leaves y_u). (3) The proof never uses forests,
attachments or child labels: on K the whole joint description is "one gate, one subset". The difficulty sits in
the root term, i.e. in which gate is named, and in the subset/rank term inside that gate.
(4) Corollary (FEI on K): H(f) <= 17 I(f) for every f in K. For fresh data blocks this class is a read-once
composition of multiplexer gates with LTF leaves, so FEI with SOME constant may already follow from
O'Donnell-Tan composition (ICALP 2013) plus Theorem A of the manuscript, if the multiplexer's biased FEI+
constant is established; I have not verified that the MUX constant is in the literature. K_EM with balanced leaves
is covered for FEI by the selector identities C010/C011 (any subcube partition, disjoint leaf supports). So the
NEW content of Theorem 5.1 is the witness-route bound, not FEI on K. A direct spectral computation (section 7)
gives a smaller FEI constant on K.

## 6. Proposition N1: the minimum-witness bound (W) is NOT linear in I on K_RO, for every lambda

Family. D >= 1, w >= 2, delta = 2^{-w}. F = F_{D,w}: root query x_0; the plus side is a complete read-once tree
of depth D on fresh control variables whose 2^D leaves carry OR_w on fresh disjoint blocks; the minus side is
the same with AND_w (true iff all w inputs are +1; OR_w false iff all are -1). F is in K_RO (fresh blocks, so DS;
OR and AND are regular). All 2^{D+1} cells have codimension D+1.

Exact data (Prop 4.1): m_+(x_0) = 1 - 2 delta, m_-(x_0) = -(1 - 2 delta); every other internal node has equal means
on both sides, so the only phi-set is {x_0}, with fhat({x_0})^2 = (1-2delta)^2. E F = 0, v = 1.
  I(F) = (1 - 2delta)^2 + 2 delta (1-delta)(D+1) + 2 w delta
(Prop 4.1(v): Var(OR_w) = Var(AND_w) = 4 delta(1-delta), I(OR_w) = I(AND_w) = 2 w delta).

**Proposition 6.1.** In the cell-and-leaf representation (gates h_i = kappa_i AND [g_i = 1]), for every lambda > 0
and D >= 4, the right side of (W) satisfies
  RHS_lambda(F) >= (1 - 2 delta)^2 (D/2 + 2).
The same lower bound holds for the scale-mixture bound of SEED_LEMMAS section 2 (any weights w_j, any lambda_j),
and for the complemented representation (gates kappa_i AND [g_i = -1], i.e. the paper's intersection form).
With w = ceil(log2 D) and D >= 16: I(F) <= 4 while RHS >= (49/64)(D/2 + 2), so RHS/I -> infinity linearly in D.
On the other hand, for the same law Q_{1,1}, log(1/Q_{1,1}({x_0})) < 7.3 bits for every D, and Theorem 5.1 gives
H(F) <= h(v) + v Lambda_1 + sum_A p(A) log(1/Q_{1,1}(A)) <= 17 I(F).

*Proof.* A = {x_0} lies in every R_i. Any witness for A has tau(x_0) = l for one gate l, F = {l}, one root, no
edges, c_l = 0, so C_lambda(A; tau, T) = log(1/(lambda pi_l)) + log 2 + log Z^l_1 - log theta^l_1(x_0) + log 2
>= log(1/(lambda pi_l)) + 2, because Z^l_1 = sum_{j in R_l} theta^l_1(j) >= theta^l_1(x_0). Every gate has
pi_l = 2^{-(D+1)} P_l <= 2^{-(D+1)} (1-delta). Hence min_{tau,T} C_lambda(A) >= D + 3 + log(1/(1-delta)) - log lambda.
For t < 1 (t defined next) all other terms of (W) are nonnegative; h(v) = 0, v = 1, and Lambda_lambda >= 2^D log(1 + lambda (1-delta) 2^{-(D+1)})
(the plus-side gates alone). Put t = lambda (1-delta) 2^{-(D+1)}. Then
  RHS_lambda >= (1-2delta)^2 (2 - log t) + 2^D log(1 + t).
If t >= 1 (CORRECTED in self-audit: here other sets' root terms log(1/(lambda pi_r)) can be negative, so "all other
terms are nonnegative" fails): every witness of every set A has at most |A| roots, each costing >= -log t, and all
other cost terms are >= 0 (log Z - sum log theta >= 0, and the size and child-count terms are >= 0), so
min C_lambda(A) >= -|A| log(1+t); summing, sum_A p(A) min C_lambda(A) >= -I(F) log(1+t), and
RHS >= (2^D - I(F)) log(1+t) >= 2^D - D/2 - 5/2 (since I(F) <= 1 + (D+1)/2 + 2w 2^{-w} <= D/2 + 5/2), which is
>= D/2 + 2 for D >= 4.
If 2^{-D/2} <= t < 1: log(1+t) >= t (concavity of log(1+t) on [0,1]), so RHS >= 2^D t >= 2^{D/2}.
If t < 2^{-D/2}: -log t > D/2, so RHS > (1-2delta)^2 (2 + D/2).
For D >= 4, 2^{D/2} >= D/2 + 2 and 2^D - D/2 - 5/2 >= D/2 + 2, which gives the claim.
Mixtures: the bracket for A = {x_0} is Lambda_{lambda_j} + C_{lambda_j}(A) + log(1/w_j) >= 2^D log(1+t_j) + 2 - log t_j,
and the same three cases give >= D/2 + 2 times fhat({x_0})^2 = (1-2delta)^2. Every other set's bracket is >= 0 when
w <= 2^D - D - 1: then every support set has |A| <= D + 1 + w <= 2^D, and for t_j >= 1 the bracket is
>= 2^D log(1+t_j) - |A| log(1+t_j) >= 0, while for t_j < 1 all its terms are >= 0. (For the asymptotic statement
w = ceil(log2 D) satisfies this.)
Complement: the gates kappa_i AND [g_i = -1] have pi'_l = 2^{-(D+1)} P(g_l = -1) <= 2^{-(D+1)}(1-delta) as well, and
{x_0} is again in every gate's support; the argument is identical.
Asymptotics: with delta <= 1/D and w delta <= (log D + 1)/D,
I(F) <= 1 + 2(D+1)/D + 2(log D + 1)/D <= 3.75 for D >= 16, and (1-2delta)^2 >= (7/8)^2.
Witness sum: by Lemma 3.2 with all 2^{D+1} gates,
Q_{1,1}({x_0}) >= 2^{-Lambda_1} (sum_l pi_l) (1/2)(1/Z_1)(1/2) with sum_l pi_l = 1/2, Lambda_1 <= (log e)/2 and
Z_1 = sum_{r=1}^{D+1} r^{-6/5} + sum_{r=1}^{w} r^{-6/5} < 2 zeta(6/5) < 11.19; so log(1/Q) < 0.722 + 1 + 2 + 3.485 < 7.21. QED

Evidence (code/n1_analytic.py, floating point, cross-checked against the generic code code/queue_cost.py on
D = 3, 4, 5 to all printed digits; the root normalizer is evaluated with log1p - a first run without it lost
2^{-53}-size terms and produced a spurious "optimal lambda" at D = 64):

 D   w   I(F)     H/I    minW/I (lambda=1)  min over lambda of minW/I  sumW/I (lambda=1)
 8   3   3.2813   3.076    5.985               5.899 (lambda = 2)          4.580
 16  4   3.2578   2.968    8.458               8.372 (lambda = 2)          4.676
 32  5   3.1895   2.861   13.564              13.476 (lambda = 2)          4.733
 64  6   3.1255   2.783   23.994              23.905 (lambda = 2)          4.770
 96  7   2.5822   2.491   40.957              40.849 (lambda = 2)          4.927
 128 7   3.0783   2.734   45.093              45.003 (lambda = 2)          4.797

(minW = h(v) + v Lambda + sum p(A) min single-root cost; for this family every other set has a unique owner gate,
so multi-gate forests cannot help any set except {x_0}, and for {x_0} a forest is impossible. sumW = the same law
with Lemma 3.2's sum.)

Interpretation for C020. The paper's law itself is efficient on K; the variational inequality of
Prop. joint-witness, which keeps one witness per Fourier set, is not. On K_RO a Fourier set can be described
from many gates at once (here {x_0} from all 2^{D+1} leaves), each individually rare (D+1 bits of rarity), but
jointly carrying probability 1/2. Any approach that bounds -log Q(A) by the cheapest witness pays the rarity of
the gate it names; the missing ingredient is witness multiplicity (equivalently: gate-dependent root odds, i.e.
an entropy code for the OWNER of the set instead of a per-gate rarity charge). A global lambda cannot repair this:
lambda large enough to make one rare root cheap makes Lambda_lambda of order 2^{D/2}.

## 7. Direct spectral FEI on K, and finite evidence

**Corollary 7.1.** For f in K, exactly
  H(f) = (1-v) log(1/(1-v)) + sum_i p_i [2 c_i Var_i + H+(g_i)] + sum_v w_v [2(d_v - 1) + 2 log(1/Delta_v)]
(H+(g) = sum_{B != empty} ghat(B)^2 log(1/ghat(B)^2); the last sum is absent under K_EM), and hence
  H(f) <= (C_reg + log e) I(f) < 10.38 I(f).
*Proof.* Proposition 4.1: each block set of leaf i has mass 4^{-c_i} ghat_i(B)^2 (2^{c_i} choices of T); each phi-set
of node v has mass w_v / 2^{d_v - 1} and log(2^{d_v-1}/w_v) = 2(d_v - 1) + 2 log(1/Delta_v). Then
p_i 2 c_i Var_i = 4 (p_i Var_i c_i/2); H+(g_i) <= H(g_i) <= C_reg D(g_i) <= C_reg I(g_i) (Theorem A);
w_v 2(d_v - 1) <= 4 w_v (d_v+1)/2; 2 w_v log(1/Delta_v) <= (2 log e/e) P(reach v) Delta_v <= 1.062 Inf_{x(v)}(f);
(1-v) log(1/(1-v)) <= v log e <= I log e. Collect with max(4 + 1.062, C_reg) = C_reg. QED
Status: PROVED. For fresh-block read-once trees FEI with some constant very likely follows from read-once
composition; K_EM with balanced leaves is inside C010/C011. The point of this corollary is only the explicit constant.

Evidence on random instances (code/run_costs.py random 7 300; up to 16 variables; floating point):
max over instances of  H/I = 3.40,  minW/I = 6.17 (read-once) / 5.80 (general trees),
witness-sum/I = 6.17 / 5.80,  owner-coded/I = 4.97 / 4.89. ("general trees" have unequal means and are outside K;
the small random trees do not exhibit the full-FEI difficulty of that wider class.)

## 8. Attempts log (what was tried, what failed, why)

A1. Minimum single-root witness with the paper's global lambda on K_RO: FAILS. Witness: Proposition 6.1 (family
    F_{D,w}). The failing set is {x_0}: every gate contains it, every gate is 2^{-(D+1)}-rare.
A2. Gate-dependent root odds rho_l = Omega_l / v (Omega_l = spectral mass assigned to owner l), minimum witness:
    WORKS on K (same proof as Theorem 5.1, root cost becomes the owner entropy Hm(Omega) <= 2I + 1.062 I_X + ...);
    evidence: owner-coded/I <= 4.97 on the random sample. Not needed once A3 is available.
A3. The paper's law with lambda = 1, summing single-root witnesses (Lemma 3.2): WORKS; Theorem 5.1.
A4. Extending K_RO to non-read-once control trees with unequal leaf means: BLOCKED, and necessarily so: constant
    leaves are regular, and a decision tree with constant leaves of arbitrary signs is an arbitrary Boolean function
    of x. The block part of the proof works for every tree; only the phi-part (the real-valued mean function
    phi = mu_{leaf(x)}) needs structure. Any extension must say what controls phi.
A5. Shared-data leaves with disjoint Fourier supports: VACUOUS for unate leaves (Section 4 correction).
A6. Read-once formulas over bounded fan-in gates (a target example): the C008 law needs gates that are Boolean
    combinations of at most M regular functions. A read-once formula of depth >= 3 (e.g. AND of ORs of terms) is not a
    union of such gates with bounded M and bounded label cost: either M grows with the clause width, or the
    distributed form has unbounded overlap. A law that recursively generates gate subsets (a hierarchical queue)
    would just re-encode the O'Donnell-Tan composition structure. Not pursued as a C008 statement.
A7. Decision lists with TERM tests (read-once conjunctions on disjoint blocks): the unfolded tree repeats the later
    blocks across the failure positions of earlier terms (not read-once) and the means are unequal, so it is outside
    K. Section 11: equal output means PROVED (Theorem 11.1, 27 I; Corollary 11.2 for term-test trees); arbitrary
    means PARTIAL (rank term of phi-sets with long continuations); the rank term, not the root term, is the concern.
A8. Decision-tree cells for ARBITRARY f (section 12): root term <= half the entropy (Lemma 12.0), reduction to the
    rank functional R (Prop 12.1). Exhaustive n <= 4 and several families bounded; read-once AND/OR formulas show R/I
    rising with depth while H/I saturates (12.4) - the first candidate obstruction.

## 11. Term decision lists: the root term is fine, the RANK term depends on the order chosen inside each gate

Class TDL. f = tau_1 ? g_1 : (tau_2 ? g_2 : ... : g_{m+1}), tau_k = conjunction of the w_k literals of a fresh block X_k
(orient literals so tau_k = AND), q_k = 2^{-w_k}, outputs g_j regular on fresh blocks Y_j. E_j = {tau_1..tau_{j-1}
false, tau_j true}, P(reach j) = prod_{k<j}(1-q_k). (Read-once term DLs; with w_k = 1 this is in K_RO.)

Representation: the UNFOLDED tree. Test the literals of tau_k in a fixed order; the first failure at position t_k
sends the path to block k+1. A gate = one unfolded path pi = (t_1, ..., t_{j-1}) to output j, h_pi = [cell(pi)] AND
[g_j = 1], cell probability p_pi = prod_{k<j} 2^{-t_k} * q_j. Mutually exclusive, M = 2. The unfolded tree repeats
the variables of block k+1 below each of the w_k failure positions of block k, so TDL is not in K.

Exact spectrum (proof as in Prop. 4.1, with 1_{E_j} = prod_{k<j}(1 - tau_k) tau_j; for S subset X_k:
tauhat_k(S) = q_k sigma(S), (1-tau_k)^(empty) = 1-q_k, (1-tau_k)^(S) = -q_k sigma(S) for S nonempty):
 - block sets of output j: T u B, T = union_{k<=j} S_k, mass prod_{k<j} a_k(S_k)^2 * q_j^2 * ghat_j(B)^2 with
   a_k(empty)^2 = (1-q_k)^2, a_k(S)^2 = q_k^2; total P(E_j) Var_j. Given output j: S_j uniform on all subsets of X_j;
   for k < j independently S_k = empty w.p. 1 - q_k, else uniform nonempty ("rare blocks").
 - phi-sets with top block K: mass w_K = P(reach K) q_K (1-q_K) (mu_K - m_{>K})^2, m_{>K} = E[f | tau_1..tau_K false];
   S_K uniform nonempty, S_k (k<K) as above.
 (Checked exactly: code/validate_termdl.py builds the unfolded tree, takes the integer Walsh transform and matches v
 and I(f) of this law to all digits on three mixed instances; code/exact_tdl_deficit.py replays 58 more.)

Root term (witness sum over owner paths; PROVED in the notes below, same pattern as Theorem 5.1(a),(b)).
For a block set of output j the owners are the unfolded paths to j with t_k >= max S_k (positions 1-indexed,
max(empty) = 0); sum_{owners} p_pi = q_j prod_{k<j} P(t_k >= max S_k), P(t >= 0) = 1 - q, P(t >= m) = 2^{1-m} - q >= 2^{-m}.
So log(1/sum pi) <= w_j + log(1/P_j) + sum_{k<j, S_k empty} log(1/(1-q_k)) + sum_{k<j, S_k nonempty} max S_k (+1 cap).
Against the influence of the same sets, E|T| = w_j/2 + sum_{k<j} q_k E[|S| : S unif. nonempty in X_k] with
E[|S| | nonempty] = (w/2) 2^w/(2^w - 1) >= max(1, w/2): the true block costs w_j vs w_j/2; an empty false block costs
(1-q) log(1/(1-q)) <= q log e vs q E|S| >= q; a rare block costs q E[max S] <= q w vs q w/2; and
P(E_j) Var_j log(1/P_j) <= 2 P(E_j) I(g_j) (Claim A). Phi-sets (written out): the owners of a phi-set with top
block K are the paths to K with block K full and the paths to J > K with t_K >= M_K := max S_K; with P := P(g_K = 1) and
rho := P(f = 1 | tau_1..tau_K false), their pi-sum is prod_{k<K} P(t_k >= M_k) * [q_K P + P(t_K >= M_K) rho]
>= prod_{k<K} P(t_k >= M_k) * 2^{-w_K} max(P, rho) (because P(t_K >= M_K) >= 2^{-M_K} >= q_K). So the root cost is at most
the block-set cost of the blocks k < K plus w_K + log(1/max(P, rho)). The mass of the phi-sets of K is
w_K = P(reach K) q_K (1-q_K) 4 (P - rho)^2 (since mu_K - m_{>K} = 2(P - rho)), and E|S_K| = e_{w_K} >= w_K/2 pays the w_K.
For the logarithm: (P - rho)^2 log(1/max(P,rho)) <= |P - rho| max(P,rho) log(1/max(P,rho)) <= |P - rho| (log e)/e, while the
total influence of block K's variables is P(reach K) w_K q_K (1 - mu_K m_{>K}) = P(reach K) w_K q_K 2[P(1-rho) + (1-P)rho]
>= 2 P(reach K) w_K q_K |P - rho| (P(1-rho) + (1-P)rho - |P - rho| = 2 min(P,rho)(1 - max(P,rho)) >= 0). Hence the logarithm
costs at most (2 log e/e) Inf(X_K) <= 1.07 Inf(X_K), and the phi-set root term is <= C (influence) with C absolute.
(So the root term is PROVED for all sets of every term DL; only the phi-set RANK term below is open.)

Rank term (EVIDENCE). Inside an owner gate the rank weights theta_s(j) = min(1,(s/r)^a) depend on the order fixed for
that gate. Two orders were compared (code/termdl.py, Monte Carlo over the exact spectral law, Jensen over owners,
which is a valid upper bound for log(1/Q) by Lemma 3.2):
 natural: blocks in list order;  sorted: the true block X_j first, then the false prefixes by decreasing length t_k.
Families TD1 (m = 2^w terms of width w, dictator outputs, dictator default) and TD2 (same, default -1):
  w      2     3     4     5     6     7     8     9     10
  TD2 natural rank/I  0.30  0.77  1.39  2.11  2.88  3.73   -     -     -
  TD2 sorted  rank/I  0.14  0.27  0.36  0.43  0.49  0.50  0.51  0.56  0.55
  TD2 sorted total/I  8.88  9.07  8.90  8.72  8.70  8.67  8.71  8.79  8.52
  (root/I stays 1.65-1.93 throughout; TD1 is similar: natural rank/I 0.18 -> 3.45 for w = 2..7, sorted 0.08 -> 0.48.)
Mechanism of the natural-order loss: a typical output j ~ 2^w has ~1 rare block among j-1 ~ 2^w false blocks, with
~w/2 elements sitting at path rank ~2(k-1) + w; each element pays a log(rank/s) ~ a(w - log w): the block's LOCATION
(~w bits of information, needed once) is charged once PER ELEMENT, giving order w^2 against influence order w -
the within-gate analogue of the repeated-label warning X012. Sorting by prefix length puts the rare block (prefix
length ~ max S_k ~ w) ahead of the typical prefixes (length ~ 2), so its elements get rank O(w).
Random stress test (3,759 random TDLs, m <= 150, widths 1..7, outputs dict/AND/OR/constants, 300 Monte Carlo sets
each): worst sorted total/I = 11.22, worst natural total/I = 11.48 (random lists do not reach the natural order's
bad regime m ~ 2^w, w large).
Caveat found while designing the proof: with UNEQUAL widths, decreasing length is the wrong key (a list with ~2^W
false blocks of width W >> w ahead of a rare width-w block puts ~2^{W-w} long prefixes first). The key that matches
the posterior odds that a prefix is a rare block is the DEFICIT w_k - t_k (closeness to a full prefix); for equal
widths the two keys coincide.

### 11.1 Theorem (equal-mean term decision lists): complete code length <= 27 I

Setting: TDL as above with arbitrary widths w_k >= 1 and arbitrary length m >= 1, and all outputs regular on fresh
blocks with ONE common mean mu in (-1,1). Gates: every unfolded path (j; t_1..t_{j-1}), t_k in [1, w_k], with
h_{j,t} = [x in C_{j,t}] AND [g_j = 1]; p_{j,t} = q_j prod_{k<j} 2^{-t_k} (q_{m+1} := 1), so
pi_{j,t} = p_{j,t} P(g_j = 1) <= 1/2 (no cap). ORDER of the conjunction kappa_{j,t} ("deficit order"): first the w_j
variables of the true block X_j (none if j = m+1), then the false prefixes (x_{k,1..t_k}), k < j, as contiguous
segments sorted by increasing deficit d_k = w_k - t_k, ties by increasing k. Law: the paper's Q_{1,1}, a = 6/5.

Claim: H(f) <= h(v) + v Lambda_1 + sum_A fhat(A)^2 log(1/Q_{1,1}(A)) <= 27 I(f).

Proof. (1) Spectrum. f = mu + sum_j (g_j - mu) 1_{E_j}; the second sum has no constant part, and for T inside the
control blocks (B = empty) fhat(T) = mu sum_j 1hat_{E_j}(T) = mu 1hat_{cube}(T) = 0. So every nonempty support set is a
block set T u B of a unique output j (leaf supports disjoint: fresh blocks), fhat(T u B) = 1hat_{E_j}(T) ghat_j(B),
with the law of T given j described above (independent S_k; k<j: empty w.p. 1-q_k else uniform nonempty;
S_j uniform). Mass of output j: P(E_j) Var_j. Influence:
I(f) = I_true + I_rare + I_Y, I_true = sum_j P(E_j) Var_j w_j/2, I_rare = sum_j P(E_j) Var_j sum_{k<j} q_k e_{w_k},
I_Y = sum_j P(E_j) I(g_j), e_w = E|S| for S uniform nonempty = (w/2) 2^w/(2^w - 1) >= max(1, w/2).
(2) Witness sum and Jensen. For A = T u B of output j the owner gates are the t with t_k >= M_k := max S_k
(1-indexed; M_k = 0 if S_k empty). By Lemma 3.2 and convexity of 2^x (weights w_t proportional to pi_{j,t}),
  log(1/Q(A)) <= Lambda_1 + log(1/sum_owners pi) + 1 + log(s(s+1)) + s log(2ea/(a-1)) + E_w[a sum_{x in A} log+(r_t(x)/s)],
using Z <= (2ea/(a-1))^s (M = 2). Under w the t_k are independent, P(t_k = t) proportional to 2^{-t} on [max(M_k,1), w_k].
Lambda_1 <= log e * P(f = 1) <= log e (exclusivity).
(3) Root. sum_owners pi = P_j q_j prod_{k<j} P(t >= M_k), P(t >= 0) = 1 - q_k, P(t >= M) = 2^{1-M} - q_k >= 2^{-M}.
Per unit mass of output j: E log(1/sum pi) <= w_j + log(1/P_j) + sum_{k<j} [ (1-q_k) log(1/(1-q_k)) + q_k E(M_k | nonempty) ]
<= w_j + log(1/P_j) + sum_{k<j} q_k (log e + w_k) <= 2 (w_j/2) + log(1/P_j) + (log e + 2) sum_{k<j} q_k e_{w_k}.
Var_j log(1/P_j) <= 2 I(g_j) (Claim A of Theorem 5.1). Total root <= 2 I_true + 2 I_Y + (log e + 2) I_rare.
(4) Size, child count, normalizer: v + log2(6ea/(a-1)) I.
(5) Rank. True block: ranks <= w_j, so <= a E psi_{w_j}(|S_j|) <= a w_j/2 per unit mass (S_j uniform): a I_true.
Data: as in Theorem 5.1(d): a (1 + ln 2)/ln 2 * I_Y.
Rare blocks. Let R = {k < j : S_k nonempty}, v in R, x in S_v. Its rank is at most w_j + sum_{u before v} t_u + w_v, and
"u before v" implies d_u <= d_v. For u not in R: E[t_u 1(d_u <= d)] <= 2^{d+2} q_u w_u (if w_u - d >= 2:
sum_{t >= w_u - d} t 2^{-t}/(1-q_u) <= w_u 2^{1-(w_u-d)} * 2; otherwise E t_u <= min(w_u, 4) <= 2 w_u <= 2^{d+2-w_u} w_u).
Under w, d_v = w_v - t_v ranges over [0, w_v - M_v] with probability proportional to 2^{d}, so E 2^{d_v} <= 2^{w_v - M_v + 1};
t_u and t_v are independent. For u in R \ {v}: E t_u <= w_u. Hence
  E_w[r(x)] <= W_R + 2^{w_v - M_v + 3} Lambda_j,  W_R := w_j + sum_{u in R} w_u,  Lambda_j := sum_{u<j} q_u w_u.
log+(r/s) <= log(1 + r/s) and Jensen give per element a log(1 + E_w r / s)
  <= a [ log(1 + W_R/s) + (w_v - M_v + 3) + log(1 + Lambda_j/s) ]   (log(1 + 2^c y) <= c + log(1+y), c >= 0).
Sum over the rare elements, with X := |S_j| + sum_{u in R} |S_u| <= s and Y := sum_{u in R} |S_u| <= X:
 (P1) sum_{v in R} |S_v| log(1 + W_R/s) <= X log(1 + W_R/X); x log(1 + c/x) is concave, and E[X | j, R] >= W_R/2, so
      E[...| j, R] <= log 3 * E[X | j, R].
 (P2a) E[|S_v| (w_v - M_v)] <= w_v + 1 for S_v uniform nonempty (given w_v - M_v = k, E|S_v| = 1 + (w_v - k - 1)/2
      <= (w_v+1)/2, and sum_k k P(w_v - M_v = k) <= 2^{w_v}/(2^{w_v} - 1) <= 2), and w + 1 <= 4 e_w, 3 E|S_v| = 3 e_{w_v}:
      total <= 7 E Y.
 (P2b) sum_{v in R} |S_v| log(1 + Lambda_j/s) <= Y log(1 + Lambda_j/Y), concave in Y, and E[Y | j] = sum_{u<j} q_u e_{w_u}
      >= Lambda_j/2, so <= log 3 * E[Y | j].
Total rare rank <= a [ log 3 (E|S_j| + E Y) + 7 E Y + log 3 E Y ] per unit mass.
(6) Sum, with h(v) <= 2I and v <= I: the coefficient of I_true is 2 + a(1 + log 3) = 5.102, of I_rare is
log e + 2 + a(2 log 3 + 7) = 15.647, of I_Y is 2 + a(1 + ln 2)/ln 2 = 4.932; plus log2(36 e) = 6.613 on all of I, plus
2 + (log e + 1) for h(v) and the v-terms. Total < 2 + 2.443 + 6.613 + 15.647 = 26.71 < 27. QED

Scope remarks. Unequal output means create phi-sets (top block K), whose owners include paths that run past K
through false blocks to a later true output J; the owner's true block X_J and the continuation's false prefixes then
compete with S_K for ranks. With the deficit order and ties to earlier blocks I have a case analysis indicating
these costs are paid by the influence of the continuation blocks, but no complete proof (PARTIAL; evidence above:
equal widths with adversarial outputs <= 12.6 I; mixed widths with a narrow top block before ~10*2^W negligible wide
terms: length order grows like W, deficit order like log W, i.e. the TRUE-BLOCK-FIRST convention fails there and a
gate needs a second copy with the true block last). The equal-mean theorem needs no such case.

Exact replay of Theorem 11.1 (code/exact_tdl_deficit.py): 58 random equal-mean term DLs (m <= 3, widths <= 3, outputs
all dictators / all AND_u / all OR_u, <= 15 variables), exact Walsh spectrum, exact sum over ALL single-root witnesses
with exact normalizers: Gibbs sanity (code >= H) holds on all; worst code/I = 5.44 (deficit order) and 5.44 (natural
order). Room to fail: these sizes cannot separate the orders or show asymptotic growth; they only check the
implementation and that nothing is off by a large factor. The asymptotic content is the proof and the Monte Carlo.

### 11.2 Corollary (equal-mean term-test decision trees)
Let each internal node v of a decision tree test a term tau_v (conjunction of the literals of a block X_v of width
w_v >= 1), the blocks along any root-to-leaf path being pairwise disjoint (a block may recur on different paths), and
let the leaves carry regular functions on fresh disjoint data blocks, all with one mean mu in (-1,1). Unfold every term
test literal by literal; gates = unfolded paths AND [leaf = 1]; order: the full blocks of the nodes passed on the TRUE
branch first (in path order), then the false prefixes by increasing deficit, ties to earlier nodes. Then the paper's
Q_{1,1} has complete code length <= 27 I(f).
Proof: identical to 11.1 with "the true block X_j" replaced by the union of the true blocks on the path to the leaf
(L_true := sum of their widths, uniform subset law on these L_true variables, so E psi_{L_true} <= L_true/2 and
log(1/sum pi) charges L_true), the false nodes on the path playing the role of k < j (their S_v are empty w.p. 1 - q_v,
else uniform nonempty, independent), W_R := L_true + sum_{u in R} w_u, Lambda := sum_{false u on the path} q_u w_u, and
mu-constant phi giving no phi-sets (same argument: phihat(T) = mu 1hat_cube(T) = 0 for T nonempty). The spectral
product formula needs only that the blocks along each path are distinct. With all widths 1 this is K_EM (any decision
tree), and with a caterpillar shape it is 11.1.

## 12. A general reduction: for subcube partitions the root term is at most half the entropy

**Lemma 12.0 (owner mass).** Let f be nonconstant and let f^{-1}(b) (b = 1 or -1) be partitioned into subcubes C_l
(e.g. the b-leaves of any decision tree for f), p_l = P(C_l), V_l = the fixed coordinates of C_l. For every nonempty A,
  |fhat(A)| <= 2 sum_{l : A subset V_l} p_l.
*Proof.* b f = -1 + 2 sum_l 1_{C_l} pointwise; for A nonempty fhat(A) = 2b sum_l 1hat_{C_l}(A), and
|1hat_{C_l}(A)| = p_l if A subset V_l and 0 otherwise. QED (Checked exactly on all instances of code/rank_term.py.)

**Proposition 12.1 (reduction to the rank term).** Let f be nonconstant, let {C_l} partition f^{-1}(b) into subcubes,
each of codimension >= 1, and fix for every l any total order r_l of V_l. Use the paper's law Q_{1,1} on the gates
h_l = 1_{C_l} (each a conjunction: one regular inner function, M = 1, any order is a desirability order), a > 1.
For nonempty A let w_A be the law on {l : A subset V_l} proportional to p_l, and put
  R(f) := sum_{A != empty} fhat(A)^2 E_{l ~ w_A} [ sum_{x in A} log+( r_l(x) / |A| ) ].
Then
  H(f) <= [8 + 3 log e + 2 log2(3 e a/(a-1))] I(f) + 2a R(f)     (= 23.55 I + 2.4 R at a = 6/5).
*Proof.* The gates are mutually exclusive (Lemma 3.1 applies to f or -f) and pi_l = p_l <= 1/2. By Lemma 3.2 and the
convexity of 2^y (Jensen with weights w_A),
  log(1/Q(A)) <= Lambda + log(1/sum_{l : A subset V_l} p_l) + log(s(s+1)) + 1 + s log(ea/(a-1)) + a E_{w_A}[sum_{x in A} log+(r_l(x)/s)],
with Z_l <= (ea/(a-1))^s (M = 1) and s = |A|. Lemma 12.0 gives log(1/sum p_l) <= 1 + (1/2) log(1/fhat(A)^2).
Lambda <= log e. With H+ := sum_{A != empty} fhat(A)^2 log(1/fhat(A)^2) and Gibbs,
  H+ <= H <= h(v) + v(log e + 2) + (1/2) H+ + log2(3ea/(a-1)) I + a R,
hence H+ <= 2h(v) + 2v(log e + 2) + 2 log2(3ea/(a-1)) I + 2aR, and H = H+ + (1-v) log(1/(1-v)) <= H+ + v log e.
Use h(v) <= 2I and v <= I. QED

Consequences.
 (a) FEI would follow from: every nonconstant f (or -f) has a subcube partition of a level set with orders such that
     R(f) <= K I(f); then H <= (23.55 + 2.4K) I. Roots, labels, attachments, normalization and sizes are all
     absorbed; on subcube partitions the WHOLE difficulty of the queue route is the rank term R.
 (b) R is a "relative position" functional: a Fourier set pays log(position/|A|) per element inside the subcubes that
     contain it, averaged over those subcubes with weights p_l. Dummy coordinates placed last cost nothing, so the
     Wan-Wright-Wu "bad tree" (dummy levels above copies of T', their Figure 2) costs nothing here, while their
     path protocol pays 2 bits per dummy level.
 (c) With minterm partitions R(f) ~ sum fhat^2 |A| log(n/|A|) (the classical weak bound); the content is in choosing
     coarse partitions (decision trees) and good orders.
Prior art. Decision-tree path coding for FEI is Wan-Wright-Wu (arXiv:1312.3003): their protocol names a path containing
S by left/right bits and then sends membership bits along it, with length 4 Inf + 2 Cov[T]; it gives 9k for read-k
trees and 12 d for expected depth d, and they observe that natural improvements would give full FEI. Proposition 12.1
differs in the accounting (path never named: witness sums plus Lemma 12.0 make the root cost <= half the entropy;
membership bits replaced by the rank code). I have not found Lemma 12.0's use as a half-entropy root bound in the
literature, but have not searched beyond WWW and the campaign sources; treat novelty as unverified.

Evidence (code/rank_term.py incl. its 'maj' mode, code/dt_code_exhaustive.py; the majority code lengths were an inline
run of code/queue_cost.code_lengths on the sequential tree; exact spectra):
 - all f with n <= 4 (222 NPN classes for n = 4; min over the 24 variable orders of the reduced ordered tree and over
   f, -f): witness-sum code/I <= 4.96 (n=2), 5.70 (n=3), 6.06 (n=4); min-witness 5.01, 5.80, 6.17; max H/I 3.40;
   the worst case is the point function (AND).
 - majority MAJ_n, sequential tree: witness-sum code/I = 4.06, 4.04, 4.00, 3.95, 3.91, 3.88 (n = 3..13, decreasing),
   min-witness 4.69 -> 6.55 (increasing), R/I = 0.43, 0.58, 0.66, 0.72, 0.76 (n = 3..11). With the level law
   W_k proportional to k^{-3/2} and uniform sets within a level, R/I tends to the finite constant
   E[(log2(1/u) - log2 e)^+], u ~ Beta(1/2,1), = 2 e^{-1/2}/ln 2 = 1.75 (heuristic limit, not proved).
 - read-once AND/OR formulas through short-circuit trees: AND-OR trees depth 1..4: witness-sum code/I = 5.01, 4.91,
   5.98, 6.14; R/I with path order 0.25, 0.49, 0.64, 0.97, with spectrally adapted orders (per gate: decreasing
   owner-weighted membership mass divided by set size) 0.25, 0.29, 0.48, 0.55; 150 random read-once formulas (4-12
   literals): code/I <= 7.59, min over b of R/I <= 1.47.
 Open: whether R/I stays bounded for AND-OR trees; depths 5-12 with the canonical orders are in 12.4 (it rises).

Literature checked for section 12 (12 Oct 2026): Wan-Wright-Wu arXiv:1312.3003, Sections 1-2 read (protocol: random path
chosen in proportion to the subtrees' spectral weights, one bit per path step plus one membership bit per step; Lemma 1.7
length 4 Inf + 2 Cov[T]); O'Donnell-Tan arXiv:1304.1347 (composition); Gonzalez-MacManus-Pereyra arXiv:2606.00246
(stopping binary trees; tribes, symmetric, read-k decision trees with constant linear in k); the arXiv full-text listing
for "Fourier entropy influence" through Sep 2026 (Potapov 2609.21563 plateaued; Shmalo 2609.15388 percolation; Slote
2608.01424 quantum FEI false; Li-Han 2512.03117; Chang 2511.07739; Kelman-Kindler-Lifshitz-Minzer-Safra 1911.10579).
None states Lemma 12.0's half-entropy root bound or a relative-rank functional. The general web-search tool was
unavailable (session budget exhausted), so the check is limited to arXiv listings and the papers named.
 - Wan-Wright-Wu's bad tree (their Fig. 2): l dummy levels (a complete tree on l irrelevant variables) above copies of
   the sequential MAJ_5 tree, l = 0..6: H/I = 1.774 throughout; path order R/I = 0.58, 0.84, 1.07, 1.30, 1.51, 1.71,
   1.89 and code/I 4.04 -> 6.46 (grows like log l); ADAPTED order R/I = 0.428 for every l (dummies have zero membership
   weight and go last). Their protocol pays 2l extra characters here.
 - Random read-k trees (n = 11, depth 7, 25 per k): max R/I path order 0.33, 0.62, 0.54, 0.48, 0.48, 0.47 and adapted
   0.24, 0.26, 0.29, 0.31, 0.37, 0.36 for k = 1, 2, 3, 4, 6, 8; code/I <= 6.15. Random trees do not stress the bound.

Where one order per cell must lose (caveat to W-CJ122). The rank code charges elements independently given |A|. If a
cell owns sets of two kinds, "a subset of block B1" and "a subset of block B2", the true information is one bit, but
any single order puts one block second and charges each of its elements about log(|B1|/|B2|). This is exactly the
mixed-width term-DL failure of section 11 (the owner's true block X_J vs the narrow top block S_K).
Refinement (PROVED, same proof as 12.1 with gate-dependent root odds, Lemma 3.2 remark): give each cell C_l several
copies (l,c) with orders r_{l,c} and root odds rho_{l,c} = p_l gamma_{l,c}, sum_c gamma_{l,c} = 1. Then Lambda <= log e and
  H(f) <= 23.55 I(f) + 2a R_mix(f),  R_mix := sum_A fhat(A)^2 E_{l ~ w_A}[ min_c ( (1/a) log(1/gamma_{l,c}) + sum_{x in A} log+(r_{l,c}(x)/|A|) ) ].
(Proof: restrict the witness sum for A, inside each cell l, to the best copy c; the extra root factor gamma_{l,c} adds
log(1/gamma) inside the Jensen average; everything else is unchanged.) With two copies (B1 first / B2 first) the
block example costs 1 bit. W-CJ122 should be read with R_mix in place of R.

## 13. Summary for the fleet (C020)

What is now proved (all with complete proofs above):
 1. K (selector trees with regular leaves on fresh blocks; equal means with ANY tree, or arbitrary means with a
    read-once tree) has complete queue-law code length <= 17 I with the paper's law Q_{1,1} (Theorem 5.1). K contains
    addressing (C009) and is not covered by C001-C003 (unbounded overlap k and M-independence) or C035 (arbitrary bias,
    arbitrary tree shape, low-energy selectors).
 2. Equal-mean term decision lists and, more generally, equal-mean term-test decision trees: <= 27 I (11.1, 11.2).
 3. The minimum-witness variational bound (W) of C008 is NOT linear in I on K (Prop 6.1): >= (D/2+2)(1-2^{1-w})^2 with
    I <= 3.75, for every lambda, with scale mixtures, and for the complemented representation. The law itself is fine.
 4. On every subcube partition of a level set (in particular every decision tree), the root term of the witness sum is
    at most half the entropy, so H <= 23.55 I + 2.4 R (Prop 12.1), and with mixtures of orders R can be replaced by R_mix
    (W-P123). The queue route on such partitions is exactly the problem of bounding the relative-rank functional R.
Ingredients the route needs, each with its witness:
 (i)  witness multiplicity / owner coding (N1, F_{D,w}); a minimum single witness pays the rarity of one named gate.
 (ii) gate orders adapted to the sets the gate owns (term DLs: the natural path order loses order w on m = 2^w terms;
      Wan-Wright-Wu's bad tree: path order loses log l, adapted order nothing).
 (iii) more than one order per gate when its owned sets are block-structured (mixed-width term DLs; W-P123 repairs it).
Not touched: forests/attachments for non-exclusive unions (read-k unions of C003). My classes never need them.

Most promising next step for the fleet: attack W-CJ122 (with R_mix) head-on, in this order:
 (a) try to REFUTE it: look for a family where every decision tree and every bounded mixture of orders leaves
     R_mix/I unbounded (candidates: functions whose cells must own block-structured set families with unboundedly
     many block types, e.g. compositions where each subformula's spectrum must be located inside long cells);
     code/dt_code_exhaustive.py, code/rank_term.py and code/random_R.py compute R and the exact code for n <= 16;
 (b) if no refutation appears, PROVE R_mix <= K I on a class where FEI is open, starting with monotone DNFs of bounded
     width through their minterm-ordered decision trees, and on read-k trees aiming at K = O(log(k+1)) (C021), using
     adapted orders (zero-membership variables last) which already neutralize the Cov[T] obstruction of Wan-Wright-Wu.
The single concrete first task (UPDATED after 12.4): decide W-CJ122 on read-once AND/OR formulas. With the two
canonical orders the rank term already outgrows the entropy (R_path/I 0.25 -> 2.85 over depth 1..12 while H/I levels
near 5.3). The owner-weighted membership masses that define the adapted order factorize over the formula, so the
adapted order is computable at large depth with the samplers of code/andor_sampler.py and code/andor_k.py. If R/I
still grows with adapted orders, the paper's rank law is the bottleneck and the next ingredient is a hierarchical
subset code inside each gate (choose the subformula parts first, then elements within each part); if it stays
bounded, proving it would be the first witness-route proof covering unbounded alternation depth.

### 12.4 Read-once AND/OR formulas at large depth: the rank term outgrows the entropy (EVIDENCE, candidate obstruction)
Exact-law Monte Carlo (code/andor_sampler.py fan-in 2, code/andor_k.py any fan-in): A ~ fhat^2 sampled from the product
structure, owner cells sampled from "x uniform given f = 1 and A all queried by the left-to-right short-circuit
evaluation" (a recursive exact conditional sampler), influences and coefficients exact. Validated against the exact
truth-table values at depths 1-4 (R_path/I 0.248, 0.482, 0.646, 0.954 vs exact 0.250, 0.490, 0.644, 0.967).
AND-OR tree (fan-in 2, alternating, AND on top), depth d = 1..12 (n = 2^d):
  H/I      2.00 2.23 3.62 3.66 4.58 4.52 5.05 5.02 5.13 5.31 5.28 5.29
  R_path/I 0.25 0.51 0.64 0.97 1.09 1.54 1.64 2.08 1.99 2.56 2.38 2.85
  R_mix/I  0.63 0.69 0.69 0.79 0.89 1.0-1.2 1.2-1.3 1.3-1.6 1.52 2.01 1.84 2.39   (two orders: path, reversed)
  root/I (witness sum, exact owner mass) 1.50 1.34 1.77 1.55 1.94 1.70 2.02 1.82 (d <= 8), always below the half-entropy
  bound of Lemma 12.0; the Jensen step costs little (true-sum rank equivalent 0.93 vs 0.97 at d = 4, 1.94 vs 2.08 at d = 8).
  (This tree drifts to a rare-event function: P(f = 1) -> 0, v = 0.003 at d = 12.)
Balanced control (alternating AND of 2 / OR of 3; near-balanced at odd depth): d = 5: P(f=1) = 0.50, H/I = 4.53,
R_path/I = 1.63, R_mix/I = 1.24; d = 7: P(f=1) = 0.76, H/I = 5.48, R_path/I = 2.51, R_mix/I = 1.94.
Reading. H/I levels off near 5.3 (FEI holds for read-once formulas; the brain's computer-assisted read-once constant
is about 6.46, Hod's lower bound about 6.45), while R/I keeps rising by about 0.2 per level with both canonical orders,
also in the near-balanced control. If this continues, the C008 law on short-circuit cells with one or two fixed orders
per cell gives only H <= O(depth) I on read-once formulas. Adapted orders halve R at depth <= 4 (section 12 evidence)
but cannot be computed at large depth by the present code. Mechanism (heuristic): a Fourier set of a read-once formula
is a union of parts living in different subformulas, which the owner cell visits in evaluation order interleaved with
many unused variables; the rank code charges every element its global position, i.e. it re-pays the location of each
subformula part per element instead of once per part. This is the within-gate analogue of the repeated-label warning
X012, one level up: the rank weights theta have no notion of the formula's hierarchy.
Status: EVIDENCE only (finite depth, Monte Carlo, two canonical orders). It does not refute W-CJ122 (other trees and
orders are not excluded) but it marks read-once formulas as the place where the conjecture, in its rank-code form, is
most likely to fail, and suggests the next ingredient: a hierarchical subset code inside a gate (choose the subformula
parts first, then elements within each part), which is no longer the paper's rank law.

## 9. Mandatory counterexample checks (X001-X013), for Theorems 5.1, 11.1, Proposition 12.1 (placed at the end)

- X001 (parity lift): not used. The theorems are class results proved by an explicit code; no local erasure quantity
  is used as a certificate. The parity lift of an f in K is not in K in general; nothing is claimed for it.
- X002 (selector synergy): the splice g_0/g_1 uses quadratic (bent-type) leaves, which are not unate, so not in K.
- X003 (sparse bent perturbations): its children use quadratic bent cores b, b' (not unate), so the family is not in K
  and nothing here pays its local logarithm.
- X011, C013 (rare activation): F = 1 + A_r(g - 1) with a REGULAR core g on fresh variables is in K_RO (the AND of
  the r activation bits unfolds into a read-once caterpillar; the off-branches carry the constant leaf +1), so
  Theorem 5.1 bounds it by 17 I uniformly in r. X011 is not contradicted: its cores are arbitrary, while K needs
  regular cores. N1 (Prop 6.1) is the witness-route analogue of X003: a rare object (each gate) forced into the cost
  by the minimum-witness accounting, repaired by witness sums.
- X004 (overlapping leaf supports): excluded by hypothesis; for unate leaves (DS) is automatic (section 4 correction).
- X005 / C014 (signed constant leaves, shared leaves): constant leaves ARE allowed in K, which is exactly why K
  requires equal means or a read-once tree: a complete oblivious tree with constant leaves of arbitrary signs is an
  arbitrary Boolean function (K_EM forces equal signs, K_RO forbids repeated labels). Shared balanced leaves g(u) y
  violate (DS).
- X006 (real amplitudes): every object is a genuine Boolean function; all spectra in the proofs are exact Boolean
  spectra (Prop 4.1, section 11), checked by integer Walsh transforms.
- X007 (shared-variable products): not used (all products in section 4 and 11 are over disjoint variable blocks).
- X008 (two spectral addresses), X009, X010 (approximate independence, reveal policy): not used.
- X012 (addressing calibration): K_EM contains addressing; Theorem 5.1 charges its label once per set (one root,
  one subset), consistent with X012; Theorem 5.1's constant 17 is weaker than the paper's tailored < 10.
- X013 (coherent superposition): no coherent-sum entropy inequality is used; coherent sums are computed exactly
  (Lemma 3.1, Prop 4.1, Lemma 12.0). Lemma 12.0 is an L1-type bound on a coherent sum (|sum| <= sum |.|), not an
  entropy bound.
Structural order tried at large depth (code/cert_order.py): inside each owner cell put the evaluation-certificate
variables (those whose values propagate to the root's value) first, then the rest, both in query order, and use the
cells of the RARER level set. AND-OR tree depth 1..12:
  R_path/I        0.24 0.50 0.65 0.97 1.10 1.50 1.60 2.07 2.08 2.51 2.42 2.81
  R_cert-first/I  0.24 0.34 0.54 0.72 0.89 1.11 1.25 1.47 1.55 1.75 1.75 1.89
The certificate-first order removes about a third of the rank term but the growth persists (about 0.15 per level, maybe
slowing), while H/I levels near 5.3. Best evidence so far that a single fixed order per cell loses a factor growing
with alternation depth on read-once formulas; it is not a proof (adapted per-cell orders at large depth and other
trees remain untested).
