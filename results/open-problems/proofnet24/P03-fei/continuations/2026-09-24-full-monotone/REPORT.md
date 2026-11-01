# FEI for monotone functions: nearly disjoint DNFs and the clique property (campaign of 24-25 September)

Goal (his 17:02 order): keep working on the full monotone case for 20 hours. The full case contains the
Friedgut-Kalai log^2 n bound for graph properties (best known: log^2 n/(log log n)^2, KKLMS 2020), so the realistic
target is the part of the small-relative-influence regime that the down-set step cannot reach. Main line: monotone
DNF formulas whose terms rarely overlap (a Janson-type condition), with high read and unbounded width. Flagship case:
"G(n, 1/2) contains a k-clique" at the clique number, a monotone graph property whose minterms have C(k,2) ~ 2 log^2 n
edges; the width theorem, the decision-tree theorem and the read-k theorem all give constants that grow with n here
(width 2 log^2 n; log of the expected depth ~ log n; read C(n-2, k-2)).

Literature on the class: Klivans-Lee-Wan (ECCC TR10-023) prove Mansour's conjecture for random DNFs with t terms of
width log t and remark that for poly(n)-size DNFs this gives spectral entropy O(log n) = O(I); O'Donnell-Wright-Zhou
cite this as FEI for random DNFs. It does not cover the clique DNF (n^{Theta(log n)} terms, I ~ log^2 n).

## 1. The block expansion (verified exactly)

f = OR_t [V_t in x], Z = 1 - f, q = E Z. Two terms overlap if their variable sets meet. A block is U = V(J) for a
connected set J of terms; kappa(U) = sum over connected J with V(J) = U of (-1)^{|J|}.

Lemma 1. Z = sum over families of pairwise disjoint blocks of prod kappa(U) x^U (0/1 variables, x^U = prod_{i in U} x_i).
Lemma 2. Zhat(T) = (-1)^{|T|} sum over families F of disjoint blocks, every block meeting T, union containing T, of
q(V(F)) prod_{U in F} kappa(U) 2^{-|U|}, where q(A) = Pr[no term disjoint from A is satisfied].

Proofs: expand prod(1 - x^{V_t}) over subsets J, split J into connected components (they are variable-disjoint), group
components by their unions; for Lemma 2 the blocks not meeting T are exactly the families disjoint from A = V(blocks
meeting T), and their sum is the expansion of the zero indicator of the terms disjoint from A.
Checks: `code/polymer_check.py` (cluster form, 12 random DNFs, error 0), `code/block_formula_check.py` (block form,
pointwise identity and Fourier identity on 10 random DNFs, error 0). For the k-cliques inside K_{k+1},
kappa(E(K_{k+1})) = -C(k,2) (checked k = 3..6; a covering subfamily must miss at least 3 vertices), so dense clique
configurations enter with polynomial, not exponential, multiplicity.

## 2. Cluster coding (proved for the cluster version; block version being written)

Reference measure: choose each cluster/block independently with probability c 2^{-|U|}, then a uniform subset of the
union. With the dense/sparse split (a block is dense for T if |T cap U| >= |U|/beta) and Cauchy-Schwarz over covering
families: H <= h(eps) + eps Lambda + (2 beta + log(1/c)) I + 8(D_sp + O_sp), I >= 4(D - O_I), D_sp <= sigma*_beta D.
All four inequalities checked exactly on 12 DNFs (`code/cluster_bound_check.py`, `logs/cluster_bound_check.log`); the
coding bound itself is 4.1-5.6 I even with heavy overlaps. Consequence: FEI with an absolute constant whenever the
off-diagonal sums O are a small fraction of D (tribes: O = 0).

Obstruction found (17:4x): with clusters of terms, O diverges for cliques - the C(k+1, k) cliques inside one K_{k+1}
generate ~4^{k+1} pairs of covering families, so O ~ lambda n^3/k although K_{k+1} has probability ~lambda/(nk).
Cauchy-Schwarz discards the inclusion-exclusion cancellation. The block (Moebius) grouping restores it (kappa =
-C(k,2) there).

## 3. Plan for the clique theorem

Split Z = Z_1 + Z_2, Z_1 = families of pairwise disjoint single terms (kappa = -1 each), Z_2 = the rest. Z_2 vanishes
unless two overlapping terms are satisfied, so its influence I(Z_2) should be tiny (rare event, bounded |Z_2| via
kappa bounds / independence polynomials at -1). For Z_1 the Cauchy-Schwarz analysis needs only pair sums of single
terms (Janson Delta, theta_t), with no dense-configuration explosion. Reference = mixture of the cluster code and the
trivial code (level + uniform subset, cost ~ |S| log(eN/|S|)); the trivial code pays only on the rare bad sets.

Status log follows below as the work proceeds.

## 4. Vertex coding: FEI for the clique property in the whole subcritical range (18:0x, 24 Sep)

Setting: f a Boolean function of the N = C(n,2) edges of K_n, F = 1 - 2f, S the spectral sample, V(S) the set of
vertices covered by the edges of S, v = |V(S)|, eps = Pr[S nonempty] = 1 - Fhat(empty)^2. "S touches W" (W a vertex
set) means some edge of S has an endpoint in W.

### 4.1 The coding inequality (any function of the edges of K_n)

Proposition 4.1. For every f and every rooted binary tree with leaf set [n] (internal nodes = sets of >= 2 vertices,
each with two children),
    H <= h(eps) + eps log2(e I/eps) + log2(3) T + I log2(e E[C(v,2)] / I),
    T = sum over internal nodes N of Pr[S touches N]   (the root contributes eps).
Proof. H(S) = H(V(S)) + H(S | V(S)). Code V(S): one bit for "S empty"; otherwise, at every internal node that
V(S) meets, record which of its two children V(S) meets (3 possibilities); this determines V(S). Whether a node is
met is determined by the symbols above it, so H(V(S)) <= h(eps) + log2(3) T. Given V(S) with v vertices, record |S|
(entropy <= eps log2(e E[|S| given S nonempty]) = eps log2(eI/eps), geometric maximum entropy) and then S as one of
C(C(v,2), |S|) sets: log2 C(M, s) <= s log2(eM/s); Jensen with weights P(S)|S|/I gives
sum P(S)|S| log2(e C(v,2)/|S|) <= I log2(e E[C(v,2)]/I).  []
Checked exactly (all intermediate forms) on 17 functions of 4-6 vertices: code/vertex_coding_check.py.

### 4.2 Two Parseval-Harris lemmas (any monotone f of the edges)

For W a vertex set write G - W for G with every edge at W deleted, and E_W for the edges at W.

Lemma 4.2. Pr[S touches W] = E Var(F | edges off E_W) <= 4 Pr[f(G - W) = 0] Pr[some minterm touching W is in G].
Proof. The Parseval identity sum_{S meets A} Fhat(S)^2 = E Var(F | x off A). On a fibre where f(G - W) = 1, f = 1 by
monotonicity and the variance is 0; otherwise the variance is 4p(1-p) <= 4p with p = Pr[f = 1 | fibre]. So the sum
is <= 4 Pr[f(G) = 1, f(G - W) = 0] <= 4 Pr[{minterm touching W present} and {f(G - W) = 0}], an increasing event and
a decreasing one; Harris.  []

Lemma 4.3. For vertices u != w let A = E_u - uw, B = E_w - uw, and a, b, c, g0 the indicators that G contains a
minterm touching u but not w, w but not u, both, neither. Then
    Pr[u, w both in V(S)] <= Pr[uw in S] + 8 (E[ab] + E[c]) Pr[g0 = 0].
Proof. Pr[S meets A and B] = ||(I - E_A)(I - E_B) F||^2. Condition on the edges off A u B (they include uw). If
g0 = 1 then f = 1 on the fibre. Otherwise f = 1 - (1-a)(1-b)(1-c) there, a depends on A, b on B, so
(I - E_A)(I - E_B) f = -(a - E_A a)(b - E_B b) + (I - E_A)(I - E_B)[(1-a)(1-b)c]; the operator is a contraction and
Var_A(a) <= E_A a, so the fibre average of the square is <= 2 E_A a E_B b + 2 E c. Multiply by 4 (F = 1 - 2f); Harris
with the decreasing event {g0 = 0}.  []
Checked exactly for k-cliques on 4-6 vertices (max ratios 0.995 and 0.350).

### 4.3 The clique property

f = f_{n,k} = [G contains K_k], m = C(k,2), lambda = C(n,k) 2^{-m}, q = Pr[f = 0]. Janson quantities:
    t_j = C(k,j) C(n-k,k-j) 2^{-(m - C(j,2))},   eta = sum_{j=2}^{k-1} t_j,   Delta = lambda eta
(eta = expected number of other k-cliques sharing an edge with a given present one). For n' vertices,
Pr[G(n',1/2) has no K_k] <= exp(-mu(n') + Delta/2), mu(n') = C(n',k) 2^{-m} (Janson).

Theorem 4.4. For every Lambda > 0, uniformly over k with lambda_{n,k} <= Lambda,
    H(f_{n,k}) <= ( 2 log2 3 + log2(e (5 + 4 lambda)) + o(1) ) I(f_{n,k})     as n -> infinity.
So the k-clique properties with lambda <= Lambda (the window around the clique number and the whole subcritical
range, k up to n) satisfy FEI with one constant; 7.78 + o(1) for lambda <= 1, 6.93 + o(1) as lambda -> 0.
[Superseded by section 8: coding V(S) directly instead of along the tree removes the 2 log2 3 - 2, giving
2 + log2(e(5 + 4 lambda)), 6.61 at lambda <= 1. The tree proof below stays as written; it is still valid.]

Proof. (a) Range of k. lambda_{n,k} <= Lambda forces k >= k_1(n), and k_1(n) >= 2 log2 n - 2 log2 log2 n - O(1) -> inf
(lambda increases in k up to about log2 n, so for n > Lambda every admissible k lies past the maximum). From
(n/k)^k <= C(n,k) <= Lambda 2^m:  k log2(n/k) <= log2 C(n,k) <= m + log2 Lambda.
(b) eta -> 0 uniformly. For j >= k/2 put i = k - j: m - C(j,2) = i(2k-i-1)/2 >= i(3k/2 - 1)/2, so
t_{k-i} <= (sqrt2 k n 2^{-3k/4})^i =: y^i, and y is decreasing in k with y(k_1) = O(k_1^{5/2}/sqrt n) -> 0. For
2 <= j <= k/2: C(n-k,k-j) C(k,j)/C(n,k) <= C(k,j) (k/(n-k+1))^j, so t_j <= lambda (k^2 2^{(j-1)/2}/(n-k+1))^j / j!;
if k <= 3 log2 n this is <= Lambda z^j with z = k^2 2^{k/4}/(n-k+1) = O(k^2 n^{-1/4}); if k > 3 log2 n use
t_j <= 2^k (n 2^{-(k+1)/2})^{k-j} <= (2 n^{-1/4})^k. Hence eta <= y/(1-y) + 2 Lambda z^2 + k (2n^{-1/4})^k -> 0.
(c) Influence. e = ab is pivotal iff G - e has no K_k (event D) and some K containing e has K - e present (A_K).
Given A_K the other edges are fair coins and D is an intersection of decreasing events {L not present}, L not
containing e, of conditional probability 1 - 2^{-(m - C(j,2))}, j = |L cap K|; Harris gives
Pr[D given A_K] >= exp(-(lambda + eta)(1 + 2^{2-k})). The pairs: sum_{K != K'} Pr[A_K and A_K' and D] <= mu_e eta Pr[D]
<= mu_e eta (mu_e = C(n-2,k-2) 2^{-(m-1)}). Bonferroni:
    I = N Pr[e pivotal] >= 2 lambda m [exp(-(lambda + eta)(1 + 2^{2-k})) - eta/2] = 2 lambda m e^{-lambda} (1 - o(1)).
Also I <= N mu_e = 2 lambda m.
(d) The tree term. Balanced tree; a node N at depth l has w <= n/2^l + 1 vertices. Lemma 4.2 with
Pr[clique touching N] <= lambda - mu(n-w) <= lambda k w/(n-k+1) and Pr[G - N clique-free] <=
exp(-lambda + lambda k w/(n-k+1) + lambda eta/2). Levels with 2^l < L k (L = sqrt k) cost at most 2 L k eps <= 8 L k
lambda (eps <= 4(1-q) <= 4 lambda): o(I). The internal nodes of one level are disjoint, so a level with 2^l >= L k
costs <= 4 lambda k (n/(n-k+1)) e^{-lambda} e^{lambda theta + lambda eta/2}, theta = (n/L + k)/(n-k+1) -> 0, and
there are <= log2(n/(Lk)) + 2 of them. With (a): T/I <= 4 (log2(n/k) + 2)/(k-1) (1 + o(1)) + o(1)
<= 2x + o(1), x = log2 C(n,k)/m (for k > n/log n both sides are o(1); for k > n/2 use lambda - mu <= lambda and
n - 1 internal nodes).
(e) The small terms A = h(eps) + eps log2(eI/eps). If lambda >= 1/4, A = O(log I) = o(I) because I -> inf. If
lambda < 1/4: eps <= 4 lambda and x -> x log2(e/x) + x log2(eI/x) increases for x <= min(1, sqrt I), so
A/I <= (2 e^lambda/m)(1 + o(1)) log2(e^2 m/(8 lambda)) = 2 e^lambda (1 - x) + O(log m/m), since
log2(1/lambda) = m(1 - x). Together with (d): A/I + T/I <= 2 + 2(e^lambda - 1) log2(1/lambda)/m + o(1) = 2 + o(1),
and T/I <= 2 + o(1). Therefore A/I + log2(3) T/I <= 2 log2 3 + o(1).
(f) The pair term. E[C(v,2)] = (1/2) sum_{u != w} Pr[u, w in V(S)] <= I + R/2 by Lemma 4.3, where for cliques c
forces uw into the clique:
    sum_{u != w} E[c] <= n(n-1) C(n-2,k-2) 2^{-m} = 2 lambda m,
    sum_{u != w} E[ab] <= lambda^2 k^2 + lambda sum_j (k-j)^2 t_j <= lambda^2 k^2 + lambda k^2 eta
(pairs of cliques sharing at most one vertex give at most [C(n-2,k-1) 2^{-m}]^2 per ordered pair; a pair sharing
j >= 2 vertices is counted (k-j)^2 times), and Pr[g0 = 0] <= exp(-lambda + 2 lambda k/(n-k+1) + lambda eta/2). So
R/(2I) <= 4 (1 + o(1)) (lambda k/(k-1) + 1 + k eta/(k-1)) = 4(1 + lambda) + o(1), and
log2(e E[C(v,2)]/I) <= log2(e (5 + 4 lambda)) + o(1).  []

Why the clique case works: the spectral sample lives on about k vertices and carries about m/2 edges, so the vertex
set costs about k log2(n/k) ~ m bits (the tree) and the edges inside cost O(1) each (the density E C(v,2) = O(I)).
The width theorem gives (m + 8.1) here, a factor of about 2 log2^2 n; the down-set step and the cluster coding both
lose on the dense clique configurations; the vertex coding never looks at them.

### 4.4 Finite n (the rigorous bound evaluated, mpmath 60 digits): code/clique_vertex_bound.py, logs/clique_vertex_bound.log

The script evaluates every inequality above as written (Janson, with the second form exp(-mu^2/(2 Delta)) when
Delta >= mu; Harris lower bound for q; second-moment and Bonferroni lower bounds for Pr[e pivotal]) and prints the
bound B(n,k) >= H/I. For all 2 <= k <= n <= 6 it lies above the exact ratio (exact H/I from 2.90 to 4.08; bound
8.5 to 252). For n = 2^e, 12 <= e <= 37, and lambda in [2^-12, 11]: B <= 10.0 at every (n,k) printed
(2^17, k = 28, lambda 1.04: B = 7.86, asymptotic 7.81; 2^24, k = 41, lambda 0.70: 7.49; 2^33, k = 58, lambda 1.58:
8.11 against 8.11). At the three larger lambda in that range B is 10.9 (2^22, lambda 25.9), 12.0 (2^31, lambda 61.2)
and 25.7 (2^15, lambda 30.9). [An earlier line here said "B <= 12 from 2^12 on at every lambda <= 64"; the 2^15 row
contradicts it.] Below 2^12 and at lambda above about 2 the Janson factor exp(Delta/2) and the pivotal lower bound are
too weak and B is large or not finite; those are finitely many functions.
Far subcritical (18:4x): for n = 2^16, 2^20, 2^30, 2^40 and every k with 2^-3600 <= lambda <= 1, A/I + T/I <= 1.97
and B <= 2 log2 3 + log2(e(5 + 4 lambda)), confirming the trade-off of step (e).
Three script bugs, all caught by a printed cross-check: (1) log(1 - 2^-m) underflows to 0 at 60 digits when m > 200
(then T = 0 and I_lo > I_up; the first table was wrong and is discarded); fixed with log1p. (2) 1 - q_lo cancels to 0
when lambda < 2^-200 (then eps_up = 0 and A = T = 0, a bound that was too optimistic); fixed with expm1. (3) A was
bounded with max(0, eps log2(eI)), dropping a negative term worth -eps log2(1/lambda): valid but a factor 2 loose,
which made B exceed the asymptotic value far below the threshold (7.41 at 2^20, k = 95) and looked like a failure of
step (e); it was the script. Now A uses x log2(e I_up/x) with x = min(eps_up, I_up).

### 4.5 What is not covered

The supercritical side lambda -> inf (k below the clique number, f nearly always 1). There the bound of 4.3 grows like
log2 lambda, and not because of the estimates: in the Janson regime the spectral sample of 1 - f is a union of about
Poisson(lambda) pieces of independent cliques, so E C(v,2) ~ lambda^2 k^2/2 while I ~ lambda k^2/4. Coding S inside
V(S) as an arbitrary edge set pays log2 lambda per edge; a coding that names the piece of each vertex (log2 lambda per
vertex, not per edge) would fix it. Not done yet.

## 5. Paper (18:4x)

paper/fei_clique.tex / .pdf (9 pages; copy in Downloads/FEI_clique_property): "The Fourier entropy-influence inequality
for the clique property". Contents: Proposition 2.1 (vertex coding), Lemmas 3.1-3.2 (Parseval-Harris), Section 4 for
copies of any graph Gamma (Lemma 4.1 influence, 4.2 tree, 4.3 pairs, Theorem 4.4: constant
2 log2 3 + log2(e(1 + 4 rho (1 + lambda))), rho = C(s,2)/m, when s -> inf, s/n -> 0, lambda <= Lambda, eta -> 0),
Section 5 for cliques (Lemma 5.1: the admissible k form {k_1..n}, eta -> 0 uniformly; Theorem 1.1 including
k > n/log n), Remarks: finite-n table, the characterization for graph properties (FEI iff E[v log2(n/v)] = O(I) and
H(S | V(S)) = O(I), from H >= E log2 C(n,v) by vertex symmetry), the supercritical heuristic, why coordinates fail.
Exact check at n <= 7 (code/clique_n7_check.py, logs/clique_n7_check.log, logs/clique_small_n_check.log): every
inequality holds for all 2 <= k <= n <= 7; exact H/I from 2.90 to 4.35 (triangles on 7 vertices); Prop. 2.1 at most
6.78 I; Lemma 3.1 ratio at most 1 (= Pr[f=0] at the root), Lemma 3.2 ratio at most 0.39.

## 6. Where the monotone case stands after the clique result (19:0x)

Proved classes of monotone functions, with the mechanism behind each (see also continuation 2026-09-24-monotone,
section 1, for the list with references):
- symmetric functions; read-once formulas; delta-tribes: exact product or symmetric structure.
- bounded width (w + 8.1), s-leaf decision trees, m-term DNFs: the down-set restriction step, which is O(Inf_v)
  when the relative influence Inf_v / min(q, 1 - q) is bounded below and loses log(min(q, 1 - q)/Inf_v) otherwise.
- regular functions (15.1), hence every monotone threshold function (F5's 14.22 is a second proof, read in
  referee_F5_ltf.md): a reference measure ordered by desirability, because derivatives are localised on the more
  desirable coordinates.
- the clique property below its threshold, and copies of any dense Gamma with rare overlaps (this campaign, 6.61 at
  lambda <= 1 after section 8; 7.78 with the tree): a hierarchy on the VERTICES plus an arbitrary edge set inside the covered vertex set. No ordering of
  the edges works here (the spectral sample is spread over a random clique), and every single edge has relative
  influence of order (log n/n)^2, so neither of the two previous mechanisms applies. It is the first proved case in
  the "transitive" corner the other methods leave out: all edges are equivalent and the desirability preorder is
  far from total.

Reformulation for graph properties (paper, Remark 6.2): FEI on a class of graph properties holds iff
E[v log2(n/v)] = O(I) (vertex part; symmetry makes it necessary, since H >= E log2 C(n, v)) and
H(S | V(S)) = O(I) (inside part; implied by E C(v,2) = O(I)). For cliques below the threshold both hold. For
stars (maximum-degree properties) the vertex part holds because the star sizes are heavy-tailed like majority's
levels, and the inside part holds because a star is determined by its centre, but E C(v,2) = O(I) fails, so the
inside part needs a better code than Jensen there.

Open, in the order I would attack them:
1. Clique property with k and lambda both growing (k below the clique number by more than a constant). For fixed k
   the width theorem gives C(k,2) + 8.1. In the Janson regime (lambda up to about n^2/k^4) the spectral sample is a
   union of about Poisson(lambda) clique pieces, and the vertex coding pays log2 lambda per edge; naming each
   vertex's piece would cost log2 lambda per vertex instead. The difficulty is to define the pieces from the
   Fourier side: same-component probabilities of S have no Parseval handle I can find, and the union bound over
   paths inside one clique diverges like (k/2)^r. The block (Moebius) expansion of section 1 is the natural tool;
   the obstruction is bounding kappa(U) for dense blocks (Euler characteristics of clique-free complexes).
   Beyond the Janson regime the conditioned graph is a lower-tail large deviation object for clique counts.
2. The vertex part E[v log(n/v)] = O(I) for all monotone graph properties. It is necessary for FEI and is the
   heart of the Friedgut-Kalai log^2 n question; a block KKL inequality for vertex stars would give it, but the
   block version of KKL fails without symmetry (an AND whose only relevant coordinate lies in the block), so it
   would have to use the vertex symmetry.
3. The averaged erasure sum_v B_v <= K I for all monotone f (equivalent to FEI on the monotone class). With E_v f
   and D_v f the non-pivotal and pivotal parts at v (disjoint supports), B_v <= sum_T Dhat_v(T)^2
   log2(e (1 + Ehat_v(T)^2/Dhat_v(T)^2)); FEI needs |Ehat_v| <= C |Dhat_v| on most of the spectral mass of D_v f,
   an alignment statement that second moments cannot see (majority: supports disjoint, B_v = 0).

## 7. Hypergraphs (19:1x-19:3x)

The vertex coding and Lemmas 3.1, 4.1, 4.2 carry over to r-uniform hypergraphs verbatim (C(v,r) inside). The pair
lemma becomes an r-set lemma with a sum over the families of subsets that cover [r] (the product of projections
(1 - E_{A_i}) kills every product of the a_J that does not cover [r]); exact check for r = 3, n <= 6, k = 4, 5:
code/hyper_check.py, logs/hyper_check.log (exact / before-Harris ratio at most 0.92; H/I 3.60 to 4.01; coding bound
at most 6.75 I). A full theorem for complete r-graphs at the threshold was drafted and withdrawn before it shipped:
its bound on t-tuples of copies added copies one at a time and charged each new copy only for its overlap with ONE
earlier copy, but a copy overlapping several earlier ones has fewer new hyperedges than that (three k-cliques each
missing a different vertex of a K_{k+1} cover every pair of the fourth). What is missing is a bound on the t-th
factorial moments of the clique count for t < 2^r in the window, the classical computation for r = 2 [BE76] that I
did not carry out for r >= 3. The paper keeps only a remark (Remark 6.3). For r = 2 the pair lemma involves only
pairs of copies, so Theorem 1.1 is unaffected.

## 8. The tree was not needed: direct coding of V(S), constant 2 + log2(e(5 + 4 lambda)) (19:2x-19:3x)

H(V(S)) <= H(v) + E log2 C(n, v): code the size v, then V(S) as one of the C(n, v) sets of that size. For a graph
property this is an equality (V(S) given v is uniform by vertex symmetry), so the vertex cost of the vertex coding
has no slack at all; the binary tree cost log2(3) per touched node on top of it. With Lemma 3.1 at single vertices,
E v <= 4 lambda k e^{-lambda}(1 + o(1)), and log2 C(n, v) <= v log2(en/2), the vertex term is
V/I <= 4 log2(en/2)/(k - 1) (1 + o(1)) <= 2x + 4 log2(ek/2)/(k - 1) + o(1) = 2x + o(1), and the trade-off with the
small terms A (which gains the harmless H(v) part eps log2(e E v/eps) = o(I)) gives A/I + V/I <= 2 + o(1). New
theorem: H <= (2 + log2(e(5 + 4 lambda)) + o(1)) I for the clique property, uniformly for lambda <= Lambda:
6.61 at lambda <= 1, 5.76 as lambda -> 0 (was 7.78 and 6.93). General Theorem 4.4:
2 + log2(e(1 + 4 rho(1 + lambda))) under s log s = o(m) (automatic for dense patterns).
The characterization for graph properties becomes exact: FEI on a class of graph properties iff
E log2 C(n, v) = O(I) and H(S | V(S)) = O(I).
Numbers (code/clique_vertex_bound.py now evaluates both codings; logs/clique_vertex_bound.log): for n = 2^12..2^37
and lambda in [2^-12, 11] the direct bound is <= 8.8 (was 10.0 with the tree); 2^33, k = 58, lambda 1.576: 6.93
against the limit 6.94; far below the threshold (n = 2^16..2^40, lambda down to 2^-3600) A/I + V/I <= 2.14 and B
exceeds the limit by <= 0.16 (logs/clique_direct_checks.log). For n <= 6 the tree variant is better; both are valid.
Exact n <= 7 (logs/clique_small_n_check.log): the direct right-hand side of Proposition 2.1 is 5.24 I to 6.47 I,
every H/I from 2.90 to 4.35 lies below it, and the rigorous B lies above it.

## 9. Notes toward general graph properties (19:3x)

(a) The vertex part is a KKL statement about vertex stars. For a graph property, E v = n Pr[S touches u] with
Pr[S touches u] = E_y Var(g_y), where g_y is f as a function of the star of u with the other edges fixed to y, and
sum_{e at u} Inf_e(f) = E_y I(g_y). Talagrand/KKL on each fibre: I(g_y) >= c Var(g_y) log(1/delta_y), delta_y the
largest influence of a star edge on g_y. So if delta_y <= n^-alpha on the fibres carrying the star variance,
E v <= 2I/(c alpha log n) and E log2 C(n, v) <= E v log2(en/2) = O(I): the vertex part holds. For the clique
property g_y is an OR of ANDs of width k - 1 over the (k-1)-cliques of G - u, typical delta_y ~ k^2/n^2, which is an
alternative proof of its vertex part. What breaks it: fibres on which one star edge nearly decides f (maximum degree
properties: a neighbour w of degree D - 1 makes uw a dictator on the fibre). There every pivotal event is of that
type and the bound gives nothing, though the vertex part probably still holds because v is heavy-tailed there and
log2 C(n,v) is much less than v log2 n for large v.

(b) The inside part has a structural obstacle, not a technical one: the Jensen bound through E C(v,2) is only right
when the spectral sample is dense in its vertex set. Examples where FEI is plausible but Jensen loses a growing
factor: dominating sets of size t ~ log2 n (spectral sample inside a complete bipartite graph between a t-set and
about t log n other vertices: Jensen loses log log n; coding the t-set first costs t log2 v bits and then every
edge is one of t choices), maximum degree (stars: the centre determines everything), and cliques below the clique
number (union of about lambda pieces: Jensen loses log2 lambda per edge). In each case the right inside code names a
small structure first (the t-set, the centre, the partition into pieces) and then pays O(1) per edge; what is
missing is a Fourier-side handle on that structure. For pieces the natural candidate, the connected components of
S, has none: Pr[u, w in one component of S] is an intersection over all cuts, the union bound over paths inside one
piece diverges like (k/2)^r, and a single fixed cut gives back Pr[S touches u].

(c) Biased measures. The vertex coding works verbatim under mu_p (Parseval, Harris, Janson all hold), with the
spectral influence sigma^2 I_p in place of I. For cliques in G(n,p) at the threshold the same estimates should give
(a heuristic reading of the proof, not checked line by line)
Ent_p <= (log2(1/p)(1 + o(1)) + O(1)) sigma^2 I_p, the form of the p-biased conjecture of Keller, Mossel and Schlank
(Ent_p <= c p log(1/p) I_p), for every p, including p -> 0 slowly (p = 1/log n), where their Claim 2.5 gives only
log n. Not written up; for polynomially small p Claim 2.5 already suffices.

## 10. Where the clique proof stops above the threshold, and why (19:5x)

(a) The Janson window is thin. Pr[no K_k] = e^{-lambda(1+o(1))} needs lambda eta -> 0. The two ends of eta are
t_2 ~ lambda k^4/(2 n^2) and t_{k-1} = k(n-k) 2^{-(k-1)} ~ k^3 lambda^{2/k}/(e^2 n), so the window is roughly
lambda << n/k^3. Since lambda grows by a factor of about n per step down in k near the clique number, this covers at
most the one value of k just below the threshold. In the window I expect every estimate of sections 4 and 8 to go
through with the same o(1) terms (not checked line by line). The vertex coding then gives (2 + log2(e(5 + 4 lambda)) + o(1)) I, which is log2 lambda too
much: the sample is a union of about lambda clique pieces, and Jensen over all pairs of V(S) charges log2 lambda per edge.

(b) Beyond the window the sample is governed by the lower tail of the clique count. Janson gives only
Pr[no K_k] <= exp(-mu^2/(2 Delta)). For k -> inf nothing is known about the structure of G(n,1/2) conditioned on
having no K_k, so no estimate of E v, E C(v,2) or of the pieces is available. This is a probabilistic obstruction,
not a coding one.

(c) What the width paper gives here. Its Corollary 5 holds for every monotone f:
H <= sum_v Inf_v (4.6355 + Psi(4 min(q,1-q)/Inf_v - 2)). For the clique property Inf_e/q = pi/(1 - pi/2), with
pi = Pr[e completes a K_k | G - e has none]. So FEI holds with a constant that depends only on a lower bound for
pi (4.64 + Psi(4/pi - 4)). In the Janson window pi ~ mu_e = 2 lambda m/N, which costs log2(N/(lambda m)) per unit of
influence. The vertex coding loses log2 lambda and the down-set step loses log2(N/(lambda m)); they add up to about
2 log2(n/k), so in the middle of the range neither method has a constant. In the deep lower-tail regime, FEI for cliques
follows from pi >= c, a statement about the conditioned graph that I cannot prove. For k = 3, where the conditioned
graph is nearly bipartite (Erdos-Kleitman-Rothschild), pi is about 1/2, but fixed k is already covered by the width theorem.

(d) A spectral-side handle on the pieces would still close the window part. The natural local criterion is
"u, w have many common S-neighbours". By Parseval, Pr[{uz, zw} in S] = E[(D_{uz} D_{zw} F)^2], so E codeg_S(u,w) is
computable. Inside a piece a pair has about k/4 common neighbours. A cross-piece pair has almost none, but for
lambda >> n/k the cross-piece cherries dominate the EXPECTED codegree, so Markov's inequality on E codeg does not
separate the two kinds of pair; a second-moment estimate precise to 1 + O(1/k) would. Not pursued: the window it
would cover is the one value of k in (a).

## 11. Biased measures: the clique property in G(n,p) (20:0x-20:3x)

Everything in sections 4 and 8 holds under mu_p, 0 < p <= 1/2, with the spectral influence I_s = 4p(1-p) I_p in place
of I. The coding concerns an arbitrary random set, the two Parseval identities hold for any product measure, and Harris
and Janson hold under mu_p. The changes: lambda = |K| p^m, eta weighted by p^{|E(L) - E(K)|}, and
sum_e mu_e = lambda m/p, so 4(1-p) lambda m [exp(-lambda/(1-p^m) - 2 eta) - eta/2] <= I_s <= 4(1-p) lambda m exp(...).
With ell = log2(1/p) we have log2(1/lambda) = m(ell - x), and the trade-off becomes
A/I + V/I <= ell (1 + theta)/(1 - p) + o(1), where theta = O(s/n + eta + 2^-m).

Paper Theorem 6.3: for every Lambda and delta there are k_0 and n_0 such that
H_p <= [(1+delta) log2(1/p)/(1-p) + log2(e(1 + 2(1+lambda)/(1-p))) + delta] I_s
for all n >= n_0, k >= k_0 and p <= 1/2 with lambda <= Lambda. In the Keller-Mossel-Schlank normalisation this is
H_p <= 4[(1+delta) log2(1/p) + log2(e(3 + 2 lambda)) + delta] p I_p.

Corollary 6.4: their Conjecture 1.6 holds for the clique property for every k >= 3, p <= 1/2 and lambda <= Lambda
(bounded k and bounded n come from their Claim 2.5). Moreover limsup H_p/(p log2(1/p) I_p) <= 4 as p -> 0 and k -> inf.
The dictator's ratio h(4p(1-p))/(p log2(1/p)) tends to 4, so 4 is the best possible constant.

Lemma 6.2 (eta -> 0 uniformly): eta increases in p. At p = 1/2, use Lemma 5.1. Otherwise k < k_1(n) = O(log n), and
at p_k we get y = Lambda^{3/(2k)} k^{5/2} n^{-1/2} and z = k^{3/2} (en)^{1/2}/(Lambda^{1/(2k)}(n-k+1)).

Numbers: code/clique_biased.py.
- logs/clique_biased_exact_n6.log: n <= 6, p in {0.5, 0.3, 0.1, 0.03}. All lemmas hold, with ratios at most 1 and 0.38.
  H_p/(p log2(1/p) I_p) is 4.02-4.08 at p = 0.03 and 4.45-4.63 at p = 0.1. Six cases are skipped because they
  underflow double precision.
- logs/clique_biased_scan.log: large n. At p = 1/2 it reproduces the published rows. At p = 2^-16, n = 2^40, k = 6:
  B = 19.79, limit 19.03, KMS form 4.95.
- n = 7 is running (logs/clique_biased_exact_n7.log).

Where this is new: k -> inf together with p -> 0, for example p = 1/log n. There KMS Claim 2.5 loses a factor of
order k. For fixed k their claim already gives the biased form, and at p = 1/2 this is Theorem 1.1. For any FIXED
function the ratio tends to 4 as p -> 0 (dictator, AND_m, disjoint ORs of ANDs), so the content is uniformity in n and
k, not the value 4.

Also changed in the paper: the proof of Lemma 3.1 now calls the conditional probability r, since p is now the edge
probability; the funding section carries the Google Cloud line (owner rule of 09-20). The paper is 12 pages.

## 12. Below the clique number: a constant of order log k from the width paper (20:3x-21:0x)

Every monotone graph property has equal edge influences I/N. So the width paper's per-coordinate bound (its
Corollary 1.4, H <= sum_v Inf_v (4.6355 + Psi(4 mu/Inf_v - 2))) combines with the edge-isoperimetric inequality
I >= 2 mu log2(1/mu) to give, for EVERY monotone graph property (paper Proposition 6.1):
    H <= (4.6355 + Psi(2N/log2(1/mu) - 2)) I,   mu = min(Pr[f=0], Pr[f=1]).
For cliques, Janson in both forms gives ln(1/q) >= lambda/(2 max(1, eta)), so
    H/I <= 4.6355 + Psi(4 ln2 * N max(1,eta)/lambda - 2)    (Corollary 6.2, all n and k).
For k <= (2 - delta) log2 n the term t_2 dominates eta: t_j/t_2 <= (5/j!) z^{j-2} with
z = k^2 2^{k/2}/(n-k+1) <= sqrt2 k^2 n^{-delta/2}, and t_2 -> inf. Then N eta/lambda = (1 + o(1)) 2 C(k,2)^2, so
    H <= (4.6355 + Psi(8 ln2 C(k,2)^2) + o(1)) I <= (8.96 + 2 log2 C(k,2) + o(1)) I,   about 4 log2 k + 7.
The loss is log2(N/log2(1/q)). The true lower-tail exponent is at most (1 + o(1)) N/(k-1) (a (k-1)-partite graph has
no K_k), so this route cannot lose less than log2(k-1): it cannot give FEI, only the log k shape. The width constant
C(k,2) + 8.1 is better for k <= 4 and worse from k = 5 on.

Numbers (code/clique_downset_bound.py, logs/clique_downset_bound.log): D(n,k) is within 0.08 of
8.55 + 2 log2 C(k,2) for 6 <= k <= k_1 - 3, and within 0.35 for k <= 5. At n = 2^12, 2^16, 2^20, 2^24, 2^32, 2^40,
over every k from 3 to k_1 (the first k with lambda <= 11), the best of this bound, the vertex-coding B(n,k) and the
width bound is at most 23.2, 25.0, 31.7, 33.7, 38.4 and 34.0. The maximum sits at k_1 - 1 or k_1 - 2, where lambda is
between Lambda and about n^{1.3}. There e^{lambda eta/2} spoils Janson, and D loses about log2(N/lambda). At n = 2^20,
k = 33 (lambda 627, lambda eta 5.5) the vertex coding still works: B = 31.7. At n = 2^40, k = 71 (lambda 8.6e4,
lambda eta 0.006) it gives B = 20.9.

Picture of the clique property after today:
- k >= k_1: constant 2 + log2(e(5 + 4 lambda)), Theorem 1.1.
- k <= (2 - delta) log2 n: constant 8.96 + 2 log2 C(k,2), Corollary 6.2.
- In between, one or two values of k get bounds of order log n.
- G(n,p): the biased form with constant tending to 4 (section 11).
Paper: 13 pages. The old heuristic remark "Below the clique number" moved into the new section 6 as Remark 6.3.

## 13. Local properties: any increasing property of k-vertex induced graphs, Janson-free (21:0x-21:3x)

Paper Theorem 6.1. Let B be an increasing property of graphs on [k] whose minimal elements have no isolated vertex,
and let f = [some k-set W has G[W] in B]. Define pi = Pr[G(k,1/2) in B], lambda = C(n,k) pi, and
iota = I(B)/pi (the relative influence). Let pi_j = Pr[B | a fixed j-set's edges all present] and
eta = sum_j C(k,j) C(n-k,k-j) pi_j. If lambda <= Lambda, eta -> 0 and log k = o(log n), then
    H <= (2 + log2(e(1 + 4(1+lambda) k^2/iota)) + o(1)) I <= (2 + log2(e(1 + 2(1+lambda) k/log2(n/k))) + o(1)) I.

Two new ingredients:
(1) The edge-isoperimetric inequality gives iota >= 2 log2(1/pi) = 2 log2(C(n,k)/lambda). Equality holds for the
    subcube, i.e. the clique. So the clique property is the extremal local property, and its constant 5 + 4 lambda
    comes back exactly.
(2) Every probability of {f = 0} enters as a ratio, and the Harris inequality controls the ratios, so Janson is not
    needed:
    - Pr[f(G - U) = 0] <= q exp(|U| lambda k/(n(1-pi))).
    - I >= q lambda iota (e^{-2 eta} - eta(1+theta)/2), by conditioning on the configuration inside W and splitting
      the other k-sets into near (sharing >= 2 vertices) and far ones.
    q cancels in V/I and in E C(v,2)/I. The A-term trade-off is the same as before, with log2 C(n,k) in place of m.

The theorem requires eta -> 0, and that must be checked for each B. For cliques this is Lemma 5.1. The crude bound
pi_j <= pi 2^{C(j,2)} gives eta <= lambda sum_j rho_j 2^{C(j,2)}, which is fine for j = 2 but too weak near j = k.
Quasi-cliques ("at least alpha C(k,2) edges") fail the spanning hypothesis whenever D <= C(k-1,2), since a minimal
element can then have an isolated vertex, so they are not an example as stated. Spanning examples: "K_k minus at most
t edges" with t <= k - 2, and "k vertices inducing minimum degree >= d". Their eta has not been checked. No example
beyond cliques is claimed in the paper.

Also changed: \label{sec:clique} was added. The abstract and introduction mention the extension. The paper is
15 pages.

## 14. Theorem 6.1 for every k, and t-defective cliques (21:1x-21:4x)

Hypothesis change: "log k = o(log n)" became "k log k = o(log(1/pi))". This is automatic for dense B (log(1/pi) of
order k^2), and it covers ALL k in the clique range. With it, Theorem 6.1 reproves Theorem 1.1 without Janson, including
k > n/log n. The facts the proof needs follow from the new hypothesis:
- lambda k/n -> 0 and lambda k^4/n^2 -> 0. If k > n^{1/3}, then log2 C(n,k) <= k(2 log2 k + log2 e) = o(L), which
  forces log2(1/lambda) >= L/2 with L/log2 n -> inf.
- k log2(en/2) <= L + log2 lambda + k log2(ek/2), used for V/I.

Corollary 6.2: t-defective cliques, i.e. every vertex misses at most t others; these are the (t+1)-plexes of Seidman and
Foster 1978. Uniformly over t <= t_n with t_n log log n = o(log n), and uniformly in k with lambda^(t) <= Lambda:
H <= (2 + log2(e(5 + 4 lambda)) + o(1)) I, the clique constant.
- B = complements of max degree <= t. There are N <= (1 + k^t)^k of them, so log2(1/pi) >= m - k log2(1 + k^t)
  = m(1 - o(1)).
- eta -> 0 holds as in Lemma 5.1:
  - For j <= k/2, pi_j <= 2^{C(j,2)} pi.
  - For j = k-i, pi_{k-i} <= 2^{-i(2k-i-1)/2} (1 + k^t)^i, because the graph is determined by the other i vertices'
    neighbourhoods. The base kn(1+k^t) 2^{-(3k-2)/4} is <= 2(1+k^t) k^{5/2} Lambda^{3/(2k)} n^{-1/2} by (rangek).
  - Separate bounds cover k > 3 log2 n.
New citation: SF78 (J. Math. Sociol. 6 (1978) 139-154). The paper is still 15 pages.

## 15. Local properties under mu_p (21:2x-21:4x)

Paper Lemma 8.5 is the biased edge-isoperimetric inequality for increasing sets: p I_p(A) >= mu log_p(mu), with equality
on subcubes. Proof: induct on the last coordinate, where A_0 is contained in A_1 with measures a <= b. The two-point
function D(a,b) = (1-p)phi(a) + p phi(b) + p(b-a) - phi((1-p)a + pb) satisfies D(a,a) = 0 and
dD/db = p log_p(pb/((1-p)a+pb)) >= 0. code/biased_isoperimetry_check.py (logs/biased_isoperimetry_check.log) tests it
directly: all 168 up-sets for m <= 4, 20000 random up-sets each for m = 5 and 6, at 8 values of p, and the two-point
inequality on a 400x400 grid. The minimum difference is -9e-16, which is rounding.

Remark 8.6: Theorem 6.1 holds under mu_p. The hypothesis becomes k log k + k log2(1/p) = o(log2(1/pi)), and the bound
becomes H_p <= [(1+o(1)) log2(1/p)/(1-p) + log2(e(1 + (1+lambda)k^2/(p(1-p)iota))) + o(1)] I_s. Lemma 8.5 gives
p iota >= log2(1/pi)/log2(1/p). For cliques p iota = m, which recovers Theorem 8.1. So every dense rare local property
of G(n,p) at its threshold satisfies the Keller-Mossel-Schlank form, with a constant tending to 4 as p -> 0. The paper
is 16 pages.
