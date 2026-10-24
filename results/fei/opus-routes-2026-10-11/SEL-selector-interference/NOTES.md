# SEL: selector interference beyond the orthogonal-neighbour multiplexer closure

Route SEL-selector-interference (ledger C010-C014, C026, C029, C035). Opus worker, 12 Oct 2026.
Full FEI remains OPEN. Nothing here claims otherwise.

Conventions. Boolean outputs are +-1, uniform measure, p(S)=fhat(S)^2, H in bits (log = log2, ln natural),
I = sum_S |S| p(S). h(t) = binary entropy in bits. Characters chi_S. For a block A of coordinates,
I_A = sum_{i in A} Inf_i. "KNOWN" marks a statement already in the literature or in the campaign baseline,
with the source; "PROVED" marks a complete proof written here (novelty not verified unless stated).

## 0. Setting and notation

Multiplexer node (paper `sec:shared-multiplexers`). Selector x in {-1,1}^a uniform, data y in {-1,1}^n uniform and
independent, branches g_b (b in {-1,1}^a) arbitrary Boolean functions of y, F(x,y)=g_x(y), N=2^a.
Spectral sample of F: (S,T), S a set of selector coordinates, T a set of data coordinates, law Fhat(S,T)^2.

- R_T = N^{-1} sum_b ghat_b(T)^2 (the T-marginal), u_T(b)=ghat_b(T)/sqrt(N R_T), r_T(b) = u_T(b)^2,
  nu_T(S) = ((W u_T)(S))^2 with W the orthogonal Walsh-Hadamard matrix (entries +-N^{-1/2}).
  One checks Fhat(S,T) = sqrt(R_T) (W u_T)(S), so nu_T is the conditional law of S given T.
- Gram matrix Gamma_{bb'} = E_y[g_b g_b'].
- pi_i = Inf_{x_i}(F) = N^{-1} sum_b P[g_b != g_{b^(i)}] = N^{-1} sum_b (1-Gamma_{b,b^(i)})/2; I_sel = sum_i pi_i.
- cost(F) := H(F) - N^{-1} sum_b H(g_b)  (the selector cost); I_data = N^{-1} sum_b I(g_b), I(F) = I_sel + I_data.
- X uniform on {-1,1}^a and, given X=b, Y ~ ghat_b^2: the "channel" law P(b,T) = ghat_b(T)^2/N.
  I(X;Y) = sum_T R_T (a - H(r_T)).

Cell selectors (paper `sec:selectors`). Partition A_1..A_m of the selector cube, a_k = 1_{A_k}, p_k = E a_k,
h_k = 2a_k - 1, q_k = ahat_k^2/p_k, D = sum_k sum_S |S| ahat_k(S)^2 = (1/4) sum_k I(h_k), leaves G_k on the data cube,
F = sum_k a_k(x) G_k(y). This is the multiplexer with g_b = G_{L(b)}, L the cell label. For an affine cell A_k
(coset of a linear subspace of F_2^a of codimension c_k), ahat_k is +-p_k on the dual subspace V_k^perp
(2^{c_k} sets) and 0 elsewhere; p_k = 2^{-c_k}; r_k = number of coordinates occurring in V_k^perp (>= c_k).

## 1. Targets (sharpest exact versions attacked)

T-LE (low energy, arbitrary branches). Bound cost(F) by the selector influences alone, sharply as I_sel/a -> 0;
decide whether any linear credit cost <= K I_sel or any energy-uniform ratio closure can hold without more structure.

T-RE (reuse of selector coordinates). Does the orthogonal-neighbour closure survive when selector coordinates also
occur in the branches?

T-CO (copy-or-orthogonal: the structured low-energy regime). Branches equal inside cells, pairwise orthogonal across
cells, Fourier supports may overlap. Closure with an explicit constant from FEI bounds for the cell indicators.

T-C1 (joint_strategy.md candidate C1, "explicitly unproved" there). Affine partition, arbitrary Boolean leaves:
H(F) <= 2 sum_j p_j c_j + sum_j p_j H(G_j)?  and its consequence C2 (correlation-gap closure).

## 2. Summary of outcomes (details and proofs in sections 3-8)

| id | status | statement (short) |
|---|---|---|
| SEL-1 | PROVED (from KNOWN parts) | cost <= sum_i h(pi_i) + min{ sum_i h(pi_i), (2/ln2) I_sel }  (all multiplexers) |
| SEL-2 | PROVED | energy fraction I_sel >= c a  =>  H(F) <= max{C, K(c)} I(F), K(c)=min{2h(c)/c, h(c)/c+2/ln2} ~ log2(1/c); improves C035's 2/c for every c != 1/2 |
| SEL-3 | PROVED | bent point-flip: cost/delta = log2(1/delta)+3/ln2+o(1); SEL-1 asymptotically attained; no linear credit cost <= K I_sel |
| SEL-4 | PROVED | sup_c (energy-uniform closure constant) = C_FEI: low-energy closure without structure is exactly FEI |
| SEL-5 | PROVED | reuse: every Boolean f is ONE orthogonal-branch node with reused selector and signed-character branches |
| SEL-6 | PROVED | explicit exact violation of max(4,C_leaf) under reuse: G=g o g o g, H=57/4 > 4I=27/2 |
| SEL-7 | PROVED | copy-or-orthogonal cells: H(F) <= 2H(p)+sum p_k[H(q_k)+H(G_k)], closure max{C_s+6, C_g} (low energy allowed) |
| SEL-8 | REFUTED | T1-sharp (C010 formula as an upper bound for orthogonal leaves): false for real leaves and for Boolean leaves (13-variable witness, excess 1.40286e-5, interval-certified) |
| SEL-8' | CONJECTURE | orthogonal leaves: excess over the C010 formula <= kappa sum_k p_k(1-p_k) |
| SEL-9 | PROVED | C1 for every affine partition and arbitrary (even real unit-norm) leaves, by tensor-power/AEP (ACKSW method) |
| SEL-10 | PROVED | C2 unconditional: affine cells + correlation gap delta across cell boundaries => H(F) <= max{4/delta, C} I(F); recursive version |
| SEL-11 | PROVED | per-T reverse uncertainty for cell-constant functions on affine partitions: H(Psihat^2)+H(|Psi|^2/N) <= a + 2H(w) |
| SEL-12 | PROVED | recursive nodes with energy fraction >= c close with K(c); decision-tree cells with gap delta close with K(delta/2) ~ log2(1/delta) |
| SEL-13 | CONJECTURE (EVIDENCE) | Schmidt-entropy defect: H(|M|^2) <= H(s)+sum s_k[H(u_k^2)+H(v_k^2)]+kappa_0 sum s_k(1-s_k), kappa_0 = 0.75615 numerically sharp; implies SEL-8' |
| SEL-14 | PROVED | the C010 formula holds on average over leaf signs for ANY leaves; interference losses are sign-alignment effects |
| SEL-15 | PROVED | balanced two-cell cut + orthogonal shared leaves: C010 value is an upper bound; recursion with cuts FROM the class closes with C = 4 (from dictators) |

## 3. Low-energy collision credit for arbitrary branches (T-LE)

### 3.1 Theorem SEL-1 (PROVED; assembled from KNOWN pieces)

For every multiplexer F(x,y)=g_x(y) with fresh uniform selector block x in {-1,1}^a and arbitrary Boolean branches
on a common data cube:

    (i)   cost(F) = H(S|T) + I(X;Y)                                   [identity]
    (ii)  I(X;Y) <= min{ H(S|T), (2/ln2) I_sel }
    (iii) H(S|T) <= sum_{i=1}^a h(pi_i) <= a h(I_sel/a)
    hence cost(F) <= sum_i h(pi_i) + min{ sum_i h(pi_i), (2/ln2) I_sel }.

Proof. (i) Chain rule for the spectral law: H(F) = H(T) + H(S|T), and H(T)=H(R). The channel law P(b,T)=ghat_b(T)^2/N
has entropy a + N^{-1} sum_b H(g_b), T-marginal R (Parseval in x: sum_S Fhat(S,T)^2 = N^{-1} sum_b ghat_b(T)^2) and
conditional b-law r_T. So a + avg H(g_b) = H(R) + sum_T R_T H(r_T), i.e. H(R) = avg H(g_b) + I(X;Y). Substitute.
This is the paper's eq. (shared-data-collision) and BR eq. (4) rearranged (KNOWN).
(ii, first bound) Maassen-Uffink entropic uncertainty (Maassen and Uffink, Phys. Rev. Lett. 60 (1988) 1103; KNOWN):
for a unitary U and a unit vector u, H(|u|^2) + H(|Uu|^2) >= -2 log max_{ij}|U_ij|. For W, max|W_ij| = N^{-1/2}, so
a - H(r_T) <= H(nu_T) for each T with R_T>0; average with weights R_T.
(ii, second bound) BR Theorem (sources/BLOCK_RESTRICTION_IDENTITY, eq. (5)): I(X;D) <= (2/ln2) I_A with A the selector
block; its proof is the cube log-Sobolev inequality (Gross 1975). KNOWN in the campaign.
(iii) H(S|T) <= H(S) <= sum_i H(1[i in S]) = sum_i h(P[i in S]) and P[i in S] = Inf_{x_i}(F) = pi_i because F is
Boolean. Concavity of h gives the last inequality. QED.

Remarks. (a) For a=1 the bound reads cost <= h(delta) + min{h(delta), (2/ln2)delta}, delta = Inf_z; the
h(delta)+(2/ln2)delta part is the math-brain draft card "sharp additive constant in the split profile" (KNOWN draft).
(b) At pi_i = 1/2 for all i the bound is 2a, the paper's eq. (shared-data-upper); SEL-1 is never weaker than 2a,
because 2 sum h(pi_i) <= 2a.
(c) EVIDENCE: code/test_lowenergy.py checks (i), (ii), (iii) and both final bounds on all 65,536 functions of 4 bits
for every split a=1,2,3 and on random low-energy multiplexers up to 7 bits: no violation; the 2 sum h bound is attained
(ratio 1.0) at a=1,2,3.

### 3.2 Corollary SEL-2: closure with logarithmic dependence on the energy fraction (PROVED)

Let c in (0,1] and suppose I_sel(F) >= c a and H(g_b) <= C I(g_b) for every b. Put
K(c) = min{ 2h(c)/c, h(c)/c + 2/ln2 }. Then

    H(F) <= max{C, K(c)} I(F).

Proof. t -> h(t)/t is nonincreasing on (0,1] (h concave, h(0)=0: h(t)/t is the slope of a chord from the origin).
With c' = I_sel/a >= c, SEL-1 gives cost <= a min{2h(c'), h(c') + (2/ln2)c'} = I_sel min{2h(c')/c', h(c')/c' + 2/ln2}
<= K(c) I_sel. Then H(F) = avg H(g_b) + cost <= C I_data + K(c) I_sel <= max{C,K(c)} I(F). QED.

Comparison with C035. K(1/2) = min{4, 2+2/ln2} = 4: the orthogonal-neighbour constant. Since h <= 1, 2h(c)/c <= 2/c with
equality only at c=1/2, so K(c) improves C035's general constant 2/c for every c != 1/2. As c -> 0,
K(c) = log2(1/c) + log2 e + 2/ln2 + o(1): logarithmic instead of linear in 1/c. Values (2/c in brackets):
K(0.25) = 6.130 [8], K(0.1) = 7.575 [20], K(0.01) = 10.965 [200], K(0.001) = 14.293 [2000].
The second expression in the minimum is the smaller one exactly when h(c)/c > 2/ln2, i.e. for c below 0.3092.

### 3.3 Proposition SEL-3: sharpness; no linear selector credit (PROVED)

For even m let b be the quadratic bent function b(t) = (-1)^{t_1t_2 + t_3t_4 + ... + t_{m-1}t_m} (t in F_2^m, b(0)=1),
b' = b - 2*1_{t=0}, F_m = Mux_z(b,b'), eps = 2^{-m/2}, delta = eps^2 = Inf_z(F_m). Exact closed forms:

    H(F_m) = (1-delta)[ m - (1-eps)log(1-eps) - (1+eps)log(1+eps) ] + 2 m delta,
    H(b) = m,   H(b') = m - [ (1+eps)(1-2eps)^2 log(1-2eps) + (1-eps)(1+2eps)^2 log(1+2eps) ].

Derivation. bhat(S) = eps s_S with s_S in {+-1}; sum_S bhat(S) = b(0) = 1 gives #{s_S=+1} = (eps^{-2}+eps^{-1})/2,
#{s_S=-1} = (eps^{-2}-eps^{-1})/2. bhat'(S) = eps s_S - 2eps^2. Fhat(empty_z,S) = bhat(S) - eps^2 and
Fhat({z},S) = eps^2. Summing p log(1/p) over the two sign classes gives the formulas. Expanding
(1-x)ln(1-x)+(1+x)ln(1+x) = x^2 + O(x^4) and (1+x)(1-2x)^2ln(1-2x)+(1-x)(1+2x)^2 ln(1+2x) = 8x^2 + O(x^4):

    H(F_m) = m + delta(m - 1/ln2) + O(m delta^2),  H(b') = m - 8delta/ln2 + O(delta^2),
    cost(F_m) = delta (m + 3/ln2) + O(m delta^2) = delta(log2(1/delta) + 3/ln2) + O(m delta^2).

The SEL-1 bound h(delta) + (2/ln2)delta = delta(log2(1/delta) + 3/ln2) + O(delta^2), so cost/bound -> 1.
EVIDENCE (code/bent_flip.py, exact Walsh integers): cost/delta = 8.030014, 10.255970, ..., 22.328068 for m=4,...,18
against m+3/ln2 = 8.328, ..., 22.328085; the closed forms reproduce these to 1e-15.
For an a-bit selector take the product F = prod_{i<=a} F_m(z_i, y^{(i)}) on disjoint data blocks: it is a
multiplexer in z with branches prod_i g^{(i)}_{z_i}, cost and every pi_i are additive/unchanged, so the bound of
SEL-1 is attained asymptotically for every a. Consequently no inequality cost(F) <= K I_sel(F) with an absolute K
holds: cost/I_sel = log2(1/delta) + 3/ln2 + o(1) is unbounded. Any linear credit must carry log2(1/pi).

### 3.4 Proposition SEL-4: energy-uniform closure as c -> 0 is exactly FEI (PROVED)

Let Kopt(c) be the supremum of H(F)/I(F) over one-node fresh-selector multiplexers with I_sel >= c a whose branches
all have H(g_b)=0 (dictators, constants). Let D(s) = sup{ H(g)/I(g) : g nonconstant Boolean on n variables with
I(g) >= s n }. For 0 < c <= 1/2:

    D(2c) <= Kopt(c) <= K(c),   and   sup_{c>0} Kopt(c) = C_FEI.

Proof. Upper bound: SEL-2 with C = 0. Lower bound: for g with I(g) >= 2cn, let g_t = z prod_{r<=t} g(x^{(r)})
(balanced, tn+1 variables, H(g_t) = tH(g), I(g_t) = tI(g)+1) and M_{g_t} = ((1+g_t)/2) y_1 + ((1-g_t)/2) y_2 with
selector block = the tn+1 inputs of g_t and branches y_1, y_2. Inf_{x_j}(M_g) = Inf_j(g) P[y_1 != y_2] = Inf_j(g)/2, so
I_sel = (tI(g)+1)/2 >= c(tn+1) (using I(g) >= 2cn and c <= 1/2). The exact identities C012 give
H(M_{g_t})/I(M_{g_t}) = (2 + tH(g)/2)/(3/2 + tI(g)/2) -> H(g)/I(g). Finally every nonconstant g on its relevant
variables has I(g) >= s n for s = I(g)/n > 0, so sup_c D(2c) = C_FEI; and Kopt(c) <= C_FEI since every F is Boolean. QED.

Interpretation. Low selector energy (fraction c) is the multiplexer image of low influence density I(g)/n.
The level bound gives D(s) <= O(log(1/s)), matching K(c). Making K independent of c without structural hypotheses is
literally FEI, so "low-energy collision credits" must use structure (sections 5-6). The orthogonal-neighbour theorem
sits at c = 1/2.

### 3.5 Corollary SEL-12: recursive multiplexers with small node energy; decision-tree cells with a gap (PROVED)

(a) Recursive version of SEL-2. Build functions from leaves with H <= C_leaf I by nodes F = g_x(y) with a fresh
selector block of a_v bits whose energy fraction is at least c (I_sel >= c a_v at every node; branches may share
data). Then every function built satisfies H(F) <= max{C_leaf, K(c)} I(F), K as in SEL-2 (K(c) = log2(1/c) + O(1)).
Proof: induction on the construction; at a node the branches satisfy H <= C' I with C' = max{C_leaf, K(c)}, and SEL-2
gives max{C', K(c_v)} = C' since K is nonincreasing.

(b) Decision-tree cells with a correlation gap. Let the cells be the leaves of a coordinate decision tree on the
selector block, with Boolean leaves G_j such that <G_j, G_l> <= 1 - delta whenever cells j != l are adjacent. At an
internal node v querying x_i, the subtrees F_+, F_- are one-bit branches and
    pi_v := Inf_{x_i}(F_v) = E_{x'}[(1 - <G_{J(+,x')}, G_{J(-,x')}>)/2] >= delta/2,
because the two leaves reached from x' are distinct adjacent cells. The selector cost telescopes over the tree,
cost(F) = sum_v P(v) [H(F_v) - (H(F_{v+}) + H(F_{v-}))/2], and I_sel(F) = sum_v P(v) pi_v (on each path a variable is
queried at most once, so the events are disjoint). SEL-1 with a = 1 at each node gives
    cost(F) <= sum_v P(v) [h(pi_v) + min{h(pi_v), (2/ln2) pi_v}] <= K(delta/2) I_sel(F),
hence H(F) <= max{C, K(delta/2)} I(F) when H(G_j) <= C I(G_j). K(delta/2) = log2(1/delta) + O(1), improving SEL-10's
4/delta for tree partitions; at delta = 1 it is K(1/2) = 4, the orthogonal case.
For parity decision trees the same telescoping holds after a linear change of selector coordinates, but influences in
the original coordinates are not preserved, so only SEL-10's 4/delta is proved there (log(1/delta) is CONJECTURE).

## 4. Reuse of selector coordinates (T-RE)

### 4.1 Theorem SEL-5 (PROVED): with reuse, one orthogonal node represents every Boolean function

Let f:{-1,1}^n -> {-1,1} be arbitrary. For b in {-1,1}^n put S_b = {i : b_i = -1} and
B_b(x) = f(b) (-1)^{|S_b|} chi_{S_b}(x). Then

    (i) B_b(b) = f(b) for every b, so f(x) = B_x(x): f is the node "select branch number x, evaluated at x";
    (ii) E_x[B_b B_b'] = 0 for all b != b' (distinct characters), in particular for neighbours;
    (iii) each branch is a signed character: H(B_b) = 0 <= C I(B_b) for every C >= 0.

Proof. chi_{S_b}(b) = prod_{i in S_b} b_i = (-1)^{|S_b|}, so B_b(b) = f(b). S_b != S_b' for b != b'. QED.

One-bit recursive version. For any v and any Boolean F, F = Mux_v(F|_{v=+1}, -v F|_{v=-1}) with branches
orthogonal on the full cube (E[-v F_+ F_-] = -E[v]E[F_+F_-] = 0, F_+- not depending on v). Iterating on functions
chi_S G (G on variables disjoint from S) reaches signed-character leaves after |vars| steps, so every Boolean function
is a recursive one-bit orthogonal multiplexer with character leaves once the selector may reappear in a branch.

### 4.2 Corollary SEL-6 (PROVED): exact violation of the orthogonal-neighbour constant under reuse

If cor:orthogonal-multiplexers held with "orthogonal" read for the branches as functions of all variables (selector
included), SEL-5 with C=0 would give H(f) <= 4 I(f) for every Boolean f. This is false. Exact witness:

    g(x_0,x_1,x_2,x_3) = x_2 if x_2 = x_3;  x_0 if (x_2,x_3) = (1,-1);  x_1 if (x_2,x_3) = (-1,1),
    ghat: 1/2 on {2},{3}; +-1/4 on {0},{1},{0,2},{1,2},{0,3},{1,3},{0,2,3},{1,2,3}  (g = (x_2+x_3)/2
    + x_0 1[x_2=1,x_3=-1] + x_1 1[x_2=-1,x_3=1]),  balanced,  H(g) = 3,  I(g) = 3/2.

Balanced composition lemma (KNOWN, standard; e.g. O'Donnell-Tan, ICALP 2013): for balanced g on disjoint blocks,
the spectral law of f o g is T ~ fhat^2 followed by independent S_i ~ ghat^2 (i in T); since ghat(empty)=0 the
union determines (T,(S_i)), so H(f o g) = H(f) + I(f)H(g), I(f o g) = I(f)I(g), and E[f o g] = fhat(empty).
Hence G = g o (g o g) on 64 variables is balanced with

    H(G) = 3 + (3/2)(3 + (3/2)3) = 57/4,   I(G) = 27/8,   H(G)/I(G) = 38/9 > 4,   4 I(G) = 27/2 < 57/4.

All quantities are exact rationals (g's masses are 1/4 and 1/16). code/witness_ratio.py recomputes ghat, H(g), I(g)
and checks H(g o g) = 15/2, I(g o g) = 9/4 by a 16-variable Walsh transform with interval logarithms.
The same g gives the composition sequence H/I = 6(1-(2/3)^k): 2, 10/3, 38/9, ... -> 6 = H(g)/(I(g)-1).

### 4.3 Remark SEL-5b: the right formulation (PROVED, elementary)

If orthogonality and the branch FEI hypothesis are imposed on the effective branches g~_b = g_b|_{x=b} (functions of
the non-selector variables), a reuse node is literally the fresh node with branches g~_b, and C035 applies verbatim.
So "reuse" splits exactly: hypotheses on effective branches -> C035; hypotheses on full branches -> every Boolean
function (SEL-5), hence FEI with the same constant, and the constant 4 is false (SEL-6).

## 5. Copy-or-orthogonal cells (T-CO)

### 5.1 Theorem SEL-7 (PROVED): pairwise orthogonal leaves with arbitrary cells

Let {A_k} be any partition of the selector cube, G_k Boolean on the data cube with E[G_k G_l] = 0 for k != l
(Fourier supports may overlap), F = sum_k a_k(x)G_k(y). Then:

    (i)  S-marginal of Fhat^2:  mu(S) = sum_k ahat_k(S)^2;   T-marginal:  R(T) = sum_k p_k Ghat_k(T)^2;
    (ii) H(F) <= H(mu) + H(R) <= 2H(p) + sum_k p_k [H(q_k) + H(G_k)];
    (iii) I_sel(F) = D = (1/4) sum_k I(h_k),  I_data(F) = sum_k p_k I(G_k);
    (iv) if H(h_k) <= C_s I(h_k) and H(G_k) <= C_g I(G_k) for all k:  H(F) <= max{C_s + 6, C_g} I(F);
    (v)  strong form: if Hplus(h_k) <= C_s (I(h_k) - Var(h_k)) and the leaves are balanced with
         H(G_k) <= C_g (I(G_k) - 1):  H(F) <= max{max(C_s,4) + 2, C_g} (I(F) - 1).

Proof. Fhat(S,T) = sum_k ahat_k(S) Ghat_k(T). (i) sum_T Fhat(S,T)^2 = sum_{k,l} ahat_k(S)ahat_l(S) E[G_kG_l]
= sum_k ahat_k(S)^2 (Parseval in y, orthonormal leaves); sum_S Fhat(S,T)^2 = sum_{k,l} Ghat_k(T)Ghat_l(T) E[a_k a_l]
= sum_k p_k Ghat_k(T)^2 (disjoint cells). (ii) subadditivity H(S,T) <= H(S)+H(T); mu is the S-marginal of the law
ahat_k(S)^2 on pairs (k,S), whose entropy is H(p) + sum p_k H(q_k); R is the T-marginal of p_k Ghat_k(T)^2, entropy
H(p) + sum p_k H(G_k). (iii) I_sel = sum_S |S| mu(S) = sum_k sum_{S != empty} |S| hhat_k(S)^2/4. I_data: condition on x.
(iv) Paper identity H(p) + sum p_k H(q_k) = (1/4) sum_k Hplus(h_k) + R(p) with R(p) <= 2H(p) <= 4D, and H(p) <= 2D
(edge isoperimetry I(h_k) >= 2 p_k log(1/p_k), paper). So H(F) <= C_s D + 4D + 2D + C_g I_data.
(v) Paper: (1/4) sum Hplus(h_k) <= C_s (D - B), R(p) <= 4B, 0 <= B <= D; so the selector part is <= max(C_s,4) D + 2D.
Balanced leaves make F balanced and I(F) - 1 = D + sum p_k (I(G_k) - 1). QED.

What it covers. Copies inside cells are free: the energy D = (1/4) sum I(h_k) can be arbitrarily small relative to a
(e.g. two cells cut by a threshold function; cells = Hamming balls). It extends C010/C026 from Fourier-disjoint to
orthogonal leaves (shared variables AND shared spectra, e.g. the Maj3 pair of C035, or G_k = f chi_{U_k}).
Recursive version: leaves built recursively in the class, cells from a fixed class with ordinary constant C_s
(e.g. regular cells, C_s = C_reg via thm:A and D_char <= I): the constant max{C_s+6, C_base} is preserved at
every depth; with regular cells and regular base leaves it is C_reg + 6 < 14.937.
Boundary: the cell hypothesis cannot be dropped (C012: M_g has two cells, orthogonal dictator leaves, and is
FEI-complete). KNOWN.

### 5.2 SEL-8: T1-sharp is FALSE, even for Boolean leaves (REFUTED, exact witness)

Candidate T1-sharp. Under the hypotheses of SEL-7, H(F) <= H(p) + sum_k p_k [H(q_k) + H(G_k)] (the Fourier-disjoint
identity C010 used as an upper bound). It would have made the strong closure constant-preserving (C026 with
Fourier-disjointness replaced by orthogonality).

History of the attempt (kept). Random tests (code/t1_orthogonal.py, 4,000 instances, a <= 4, n <= 5, three orthogonal
leaf families incl. bent*chi_U) and hill climbing over orthogonal Boolean pairs (t1sharp_attack.py, n <= 6) found
only equality cases. A one-line proof via a general SVD-entropy lemma was refuted first:
"H(|M|^2) <= H(sigma^2) + sum_k sigma_k^2 [H(u_k^2)+H(v_k^2)] for every real matrix and SVD" fails for
M = [[2,-1],[-1,-1]] (gap 0.0333 bits; code/svd_witness.py); it holds on Hadamard-degenerate SVDs (Maassen-Uffink).

Two-cell reduction (PROVED). For two cells (h, -h), p = (p_1,p_2), write the T-conditional coefficient vector of the
cell label as c(T) = (sqrt(p_1) Ghat_1(T), sqrt(p_2) Ghat_2(T))/sqrt(R_T) = (cos t, sin t) and sin^2 alpha = p_1.
Then the mass of nu_T off the empty set is m_T = cos^2(t + alpha), H(nu_T) = h(m_T) + m_T Hhat (Hhat the entropy of
the normalised nonempty spectrum of h), sum_k p_k H(q_k) = h(p_1) + 2 p_1 p_2 Hhat, and sum_T R_T m_T = 2p_1p_2.
So the Hhat terms cancel and two-cell T1-sharp is equivalent to
    sum_T R_T [ h(cos^2(t_T + alpha)) - h(cos^2 t_T) ] <= h(p_1),
a statement about the leaf pair and p only (the cell function h drops out). Orthonormality of the leaves says exactly
that the law of c(T) (T ~ R) has second-moment matrix diag(p).

Real-leaf refutation (PROVED). The moment problem has first-order violations: with atoms near e_1 and e_2, the excess
is 2 w_1 t f'(alpha) + O(t^2 log 1/t), f(t) = h(cos^2 t), f'(alpha) = -2 sqrt(p_1p_2) log2(p_1/p_2) != 0 for p_1 != 1/2.
Explicit 3-variable real example (code/t1sharp_real_witness.py): selector x in {+-1}^2, A_1 = {(1,1)}, A_2 = rest,
G_1 = cos e - sin e y, G_2 = sin e + cos e y (orthonormal, not Boolean); at e = 0.05 H(F) - bound = +0.0307 bits.
LP over all laws (code/t1_relaxed_lp*.py): the real-leaf two-cell excess is at most about 1.18 p_1 p_2 (p_1 down to
1e-6), i.e. O(B), B = sum_k p_k(1-p_k).

Boolean refutation (PROVED; exact Walsh integers, 50-digit interval logarithms, code/t1sharp_boolean_witness.py).
Expanding at p_2 = eps -> 0: excess = eps Omega + O(eps^2 log 1/eps) with
    Omega(G_1,G_2) = 4H(V) - 4 sum_T Ghat_1(T) Vhat(T) log2(1/Ghat_1(T)^2) + H(G_1) - H(G_2) - 4,  V = (G_1-G_2)/2
(unnormalised entropies). Omega = 0 whenever G_1 or G_2 is a character or the supports are disjoint; an exhaustive
scan over 2,500 random G_1 on 4 bits and all G_2 orthogonal to each (code/t1sharp_omega.py) gives max Omega = 0.04266:
    G_2 = 1 - 2*1[y = (+1,+1,-1,+1)]                (a constant with one point flipped),
    G_1 = -y_2 * (1 - 2*1[y = (+1,-1,+1,-1)])       (a negated dictator with one point flipped),
E[G_1] = 1/8, E[G_2] = 7/8, E[G_1 G_2] = 0, both supports are all 16 sets. With an r-bit selector, A_2 = one point,
A_1 = the rest (13 variables at r = 9):
    r = 9:  H(F) - [H(p) + sum_k p_k (H(q_k)+H(G_k))] in [1.4028550034696e-5, 1.4028550034697e-5]  > 0,
    r = 10: 2.2432e-5,  r = 14: 2.4988e-6,  excess/p_2 -> 0.0409... (r = 14) -> Omega.
So T1-sharp is REFUTED for Boolean leaves. The excess is of order p_2 = O(B), far below SEL-7's extra H(p) ~ p_2 log(1/p_2).

SEL-8' (CONJECTURE). For pairwise orthogonal Boolean leaves and any partition,
    H(F) <= H(p) + sum_k p_k [H(q_k) + H(G_k)] + kappa * B,   B = sum_k p_k (1 - p_k),
with an absolute kappa. It gives the strong closure max{C_s, 4 + kappa, C_g}(I(F)-1), which is constant-preserving
whenever the cell indicators satisfy the strong (biased) bound with the class constant itself (compare SEL-15c, which
proves this for balanced two-cell cuts). Evidence: two-cell real-leaf LP excess <= 0.59 B; three-cell real-leaf LP over
sampled directions (code/t1_relaxed_lp3.py, 8 partitions of F_2^3) excess <= 0.047 B; Boolean witness family
excess/B -> 0.021.

### 5.2b SEL-15: where the C010 formula does hold as an upper bound (PROVED)

(i) Affine partitions, arbitrary leaves: SEL-9 is exactly H(F) <= H(p) + sum_j p_j [H(q_j) + H(g_j)], because for an
affine cell H(q_j) = c_j and H(p) = sum_j p_j c_j. No orthogonality needed.
(ii) Balanced two-cell partitions, orthogonal leaves. Let h be balanced on the selector cube, A_+- = {h = +-1},
G_1 ⊥ G_2 Boolean on a common data cube. Then
    H(F) <= 2 + H(h)/2 + (H(G_1) + H(G_2))/2,     I(F) = I(h)/2 + (I(G_1) + I(G_2))/2,
the right side being the C010 value (equality when the leaves are Fourier-disjoint; for dictator leaves it is C012).
Proof. From 5.2 (two-cell reduction) with p = (1/2,1/2): Hhat = H(h) (hhat(empty) = 0), sum_k p_k H(q_k) = 1 + H(h)/2,
and H(F) = H(p) + sum_k p_k H(G_k) + sum_T R_T [h(m_T) - h(c_1(T)^2)] + H(h)/2 <= 1 + avg H(G) + 1 + H(h)/2,
since h(m_T) <= 1 and h(c_1^2) >= 0. Influence: SEL-7(iii). QED.
(iii) Unbalanced two-cell partitions: false (SEL-8 witness, p_2 = 2^-9).

Corollary SEL-15c (constant-preserving recursion with cuts from the class; PROVED). Let C >= 4 and let M_C be the
smallest class containing a base class of balanced functions with H <= C (I - 1) and closed under
F(x,y) = ((1+h(x))/2) G_1(y) + ((1-h(x))/2) G_2(y) with h, G_1, G_2 in M_C, G_1 ⊥ G_2, and the variables of h disjoint
from those of G_1, G_2 (G_1, G_2 may share variables). Every F in M_C is balanced and H(F) <= C (I(F) - 1).
Proof: by (ii), H(F) <= 2 + (C/2)(I(h) - 1) + C(avg I(G) - 1) = C(I(F) - 1) + 2 - C/2 <= C(I(F) - 1); E F = 0.
Contrast: C026 needs Fourier-disjoint leaves and an external cell class; C012 says arbitrary balanced cuts are
FEI-complete; here the cut must come from the class, and that is exactly what makes the recursion close. With the base
class "balanced regular functions" one may take C = max(4, strong regular constant) (the paper's strong estimate for
character multiples / regular functions, 4 C_reg < 35.746, is the available value). With the base class {dictators}
(H = 0 = 4(I-1)) the constant is exactly 4: M_4 contains the one-bit fresh-selector recursion of C035 (h a dictator)
and replaces the selector bit by any balanced member of the class ("soft selectors"); addressing attains equality.
EVIDENCE (code/m4_class.py): 341 random members of M_4 up to 13 variables: max H - 4(I-1) = 0 (equality cases),
max H - [2 + H(h)/2 + avg H(G)] = 9e-16.

### 5.2c SEL-14: the C010 formula holds on average over leaf signs, for ANY leaves (PROVED)

For any partition, any leaves (no orthogonality), and independent uniform signs eps_k, the functions
F_eps = sum_k eps_k a_k(x) G_k(y) satisfy
    E_eps H(F_eps) <= H(p) + sum_k p_k [H(q_k) + H(G_k)],   E_eps I_sel(F_eps) = D,   I_data(F_eps) = sum_k p_k I(G_k).
Proof. E_eps Fhat_eps(S,T)^2 = sum_k ahat_k(S)^2 Ghat_k(T)^2 (cross terms vanish), the (S,T)-marginal of the law
ahat_k(S)^2 Ghat_k(T)^2 on (k,S,T); concavity of H. For the influence, a cube edge inside a cell contributes 0 and an
edge between cells j != l contributes (1 - eps_j eps_l <G_j,G_l>)/2, of mean 1/2. QED.
So every bad interference effect in this report (signed dictators, T1-sharp failures, X013) is a sign-alignment effect:
for every partition with FEI-good cells and FEI-good leaves, some re-signing of the leaves satisfies
H(F_eps) <= max{C_s + 4, C_g} I(F_eps) (average of cor:selector-full). This is the real-variable "dephasing" analogue of
the averaging identity behind SEL-13 (E_eps H(|sum_k eps_k sigma_k u_k v_k^T|^2) <= H(s) + sum_k s_k[H(u_k^2)+H(v_k^2)]).

### 5.3 SEL-13: a general matrix form (CONJECTURE, strong EVIDENCE) that would imply SEL-8'

Per-T reformulation (PROVED). With c_k(T) = sqrt(p_k) Ghat_k(T)/sqrt(R_T) and phi_k = ahat_k/sqrt(p_k),
H(F) - [H(p) + sum_k p_k (H(q_k)+H(G_k))] = E_{T~R} Phi(c(T)),
Phi(c) = H(|sum_k c_k phi_k|^2) - H(c^2) - sum_k c_k^2 H(phi_k^2), and E[c c^T] = diag(p) is exactly the orthonormality
of the leaves. Equivalently, Fhat = sum_k sqrt(p_k) phi_k Ghat_k^T is a singular value decomposition (orthonormal
phi_k because the cells are disjoint, orthonormal Ghat_k because the leaves are orthonormal).

Conjecture SEL-13 (Schmidt-entropy defect). For every real matrix M with ||M||_F = 1 and every singular value
decomposition M = sum_k sigma_k u_k v_k^T, s_k = sigma_k^2,
    H(|M|^2) <= H(s) + sum_k s_k [H(u_k^2) + H(v_k^2)] + kappa_0 sum_k s_k (1 - s_k),
with kappa_0 = 0.756151564 (numerical supremum). Without the last term it is false (M = [[2,-1],[-1,-1]]); with
2H(s) in place of H(s) + kappa_0 B it is just subadditivity (that is SEL-7's proof).
Evidence: 60,000 random matrices up to 6 x 6 and Nelder-Mead from 300 starts in shapes 2x2 ... 4x4
(code/svd_entropy2.py, svd_entropy3.py) never exceed gap/B = 0.7561; every optimiser run converges to a near-rank-one
2x2 limit; degenerate singular values with rotated bases (svd_entropy4.py) give at most 0.318. The supremum is located
analytically-numerically (code/svd_defect_limit.py, svd_defect_eta*.py, 80-digit arithmetic): for
M_t = [[t, 1], [t^2 (1-eta), t]], t -> 0, the ratio gap/B tends to a function of eta alone (independent of the
other scalings tested), maximal at eta = 4.5911 with value 0.756151563992684.
SEL-13 implies SEL-8' with kappa = kappa_0 for every partition and every orthonormal family of leaves (real or
Boolean), hence the strong orthogonal-leaf closure max{C_s, 4 + kappa_0, C_g} (I(F) - 1) with 4 + kappa_0 < 4.757.
It is also the matrix version of the coherent-superposition obligation C034: X013's real vectors violate the
per-instance coherent-sum bound, but placed as the right factors of a matrix with orthonormal left factors they give
gap 0 (left factors e_1, e_2) or -2 bits (left factors (e_1 +- e_2)/sqrt2). Literature: in quantum-information terms
M is a bipartite pure state measured in product bases; the known entropic uncertainty relations with memory
(Berta et al. 2010) are lower bounds; no upper bound of this form was found (no web search was possible in this
session after the first two checks, so novelty is unverified).

## 6. Affine partitions with arbitrary leaves: C1 and C2 (T-C1)

### 6.1 Theorem SEL-9 (PROVED): C1 holds for every affine partition and arbitrary leaves

Let {A_j} be a partition of F_2^a into affine subspaces of codimension c_j (p_j = 2^{-c_j}), and let g_j be real
functions on the data cube with E g_j^2 = l_j, sum_j p_j l_j = 1 (Boolean leaves: l_j = 1). Put w_j = p_j l_j and
Lambda_j = ghat_j^2 / l_j. Then F = sum_j 1_{A_j}(x) g_j(y) satisfies

    H(Fhat^2) <= H(w) + sum_j w_j c_j + sum_j w_j H(Lambda_j).

For Boolean leaves w = p and H(p) = sum p_j c_j, which is C1:  H(F) <= 2 sum_j p_j c_j + sum_j p_j H(g_j).
For constant leaves (empty data cube) this is SEL-11; for constant +-1 leaves it is the theorem
H(fhat^2) <= 2 aUC^xor(f) of Arunachalam, Chakraborty, Koucky, Saurabh, de Wolf, "Improved bounds on Fourier entropy
and Min-entropy" (arXiv:1809.09819, Theorem 1.6; KNOWN). The proof below is their tensor-power/AEP argument, extended
to leaves; the extension to arbitrary leaves is not stated there (novelty unverified).

Proof. Drop the j with l_j = 0. Fix eps > 0 and k >= 1. The tensor power F^{(k)}(x^1..x^k,y^1..y^k) = prod_i F(x^i,y^i)
has spectral law (Fhat^2)^{tensor k}, so H(F^{(k)}) = k H(F). Expand F^{(k)} = sum_{J in [m]^k} 1_{A_J}(x) G_J(y) with
A_J = A_{j_1} x ... x A_{j_k} (affine, codim c_J = sum_i c_{j_i}, dual subspace V_J^perp of size 2^{c_J}),
G_J = tensor_i g_{j_i}, p_J = prod p_{j_i}, w_J = p_J ||G_J||^2 = prod_i w_{j_i}, Lambda_J = tensor_i Lambda_{j_i}.
Typical labels: Jtyp = { J : -log w_J <= k(H(w)+eps), c_J <= k(sum_j w_j c_j + eps),
sum_i H(Lambda_{j_i}) <= k(sum_j w_j H(Lambda_j) + eps) }. By the weak law of large numbers for i.i.d. labels with law
w (finite alphabet), w^{tensor k}(Jtyp^c) =: alpha_k -> 0, and |Jtyp| <= 2^{k(H(w)+eps)}.
Typical data sets: Ttyp(J) = { T : -log Lambda_J(T) <= sum_i H(Lambda_{j_i}) + k eps }; |Ttyp(J)| <= 2^{sum_i H(Lambda_{j_i}) + k eps}
and, by Chebyshev, Lambda_J(Ttyp(J)^c) <= s^2/(k eps^2), where s^2 = max_j Var_{T~Lambda_j}(log Lambda_j(T)) < infinity.
Approximant: Ftil = sum_{J in Jtyp} 1_{A_J}(x) Gtil_J(y), Gtil_J = Fourier truncation of G_J to Ttyp(J). Since
1hat_{A_J} vanishes off V_J^perp, Ftil is Fourier-supported in B_k = union_{J in Jtyp} V_J^perp x Ttyp(J), and
log|B_k| <= k[ H(w) + sum_j w_j c_j + sum_j w_j H(Lambda_j) + 4 eps ].
Error: functions 1_{A_J}(x)u(y) with distinct J are orthogonal (disjoint x-supports), so
||F^{(k)} - Ftil||^2 = sum_{J notin Jtyp} w_J + sum_{J in Jtyp} p_J ||G_J - Gtil_J||^2 <= alpha_k + s^2/(k eps^2) =: beta_k -> 0.
The spectral mass of F^{(k)} outside B_k is ||Proj_{B_k^c}(F^{(k)} - Ftil)||^2 <= beta_k. For a law P on a finite set
Omega and B with P(B^c) = beta: H(P) <= h(beta) + log|B| + beta log|Omega|. With |Omega| = 2^{k(a+n)}:
k H(F) <= 1 + log|B_k| + beta_k k (a+n). Divide by k, let k -> infinity, then eps -> 0. QED.

Remarks. (a) The same proof gives, for any partition into cells whose indicator spectra have supports of size s_j:
H(F) <= H(w) + sum_j w_j log2 s_j + sum_j w_j H(Lambda_j). Affine cells minimise s_j (s_j >= 1/p_j always).
(b) For non-affine cells the x-side must be truncated too and the cross terms no longer vanish unless the leaves are
orthogonal; even then the truncated leaves lose orthogonality. That is exactly why T1-sharp (5.2) is still open.
(c) EVIDENCE: code/affine_c1.py: 2,100 random affine partitions of F_2^3 and F_2^4 (729 irreducible: no hyperplane
splits them, so they are not parity decision trees), random/coherent/near-copy leaves: no violation of C1 or SEL-11.
(d) For parity-decision-tree partitions C1 also follows from the one-bit bound H(Mux) <= 2 + avg H by induction after
a linear change of selector coordinates at each node (entropy is invariant under invertible linear maps of the
selector block, which permute characters). The AEP proof covers the irreducible partitions.

### 6.2 SEL-11 (PROVED): reverse uncertainty on affine partitions

For a real cell-constant Psi = sum_j v_j 1_{A_j} on an affine partition, E Psi^2 = 1, w_j = p_j v_j^2, and the point
law r(x) = Psi(x)^2/N: H(r) = H(w) + sum_j w_j (a - c_j), so SEL-9 with constant leaves reads

    H(Psihat^2) + H(r) <= a + 2 H(w),

a reverse form of Maassen-Uffink (H(Psihat^2) + H(r) >= a) for functions measurable with respect to an affine partition.

### 6.3 Corollary SEL-10 (PROVED): correlation-gap closure for affine cells (C2 made unconditional)

Let F = sum_j 1_{A_j}(x) g_j(y) with an affine partition of a fresh selector block, Boolean leaves, and
<g_j, g_l> <= 1 - delta whenever j != l and some cube edge joins A_j and A_l. Then
I_sel >= (delta/2) sum_j p_j r_j >= (delta/2) sum_j p_j c_j, and SEL-9 gives

    H(F) <= max{4/delta, C} I(F)        if H(g_j) <= C I(g_j) for all j;
    H(F) <= max{4/delta, C_g}(I(F) - 1)  if the leaves are balanced with H(g_j) <= C_g (I(g_j) - 1).

Proof. Inf_{x_i}(F) = E_x[(1 - <g_{J(x)}, g_{J(x^i)}>)/2] >= (delta/2) P[J(x) != J(x^i)], and
sum_i P[J(x) != J(x^i)] = sum_j p_j r_j (x^i leaves an affine cell iff e_i is not in its direction space iff i occurs
in its dual subspace); c_j <= r_j. Then H(F) <= 2 sum p_j c_j + sum p_j H(g_j) <= (4/delta) I_sel + C I_data.
The strong form uses I(F) - 1 = I_sel + sum p_j (I(g_j) - 1). QED.
Recursive version: building functions by nodes of this kind (fresh selector block, affine partition, branches
previously built, data shared, copies inside cells allowed) from regular leaves preserves max{4/delta, C_reg}.
Selector energy may be far below the selector dimension (copies inside cells), so this is beyond C035's
uniform-energy hypothesis; it contains C035 (point cells, delta = 1) and C011 (Fourier-disjoint leaves, delta = 1).
Necessity: delta = 0 with point cells is the signed-dictator encoding (X005, FEI-complete); non-affine cells with
delta = 1 contain M_g (C012, FEI-complete). Between them, SEL-7 covers FEI-good non-affine cells with delta = 1.

## 7a. Second-path audit of the proved statements (EVIDENCE for proofs that are analytic)

code/audit_closures.py re-derives every closure on random instances by a different path (exact rational
coordinate influences from the integer Walsh transform, entropies from the full spectrum):
- SEL-7: 400 instances; exact identities I_sel = (1/4) sum_k I(h_k), I_data = sum_k p_k I(G_k) hold as Fractions;
  H(F) <= max(C_s+6, C_g) I(F) with C_s, C_g the actual maximal ratios: no failure.
- SEL-10: 352 affine-partition instances with near-copy leaves: I_sel >= (delta/2) sum p_j r_j and
  H(F) <= max(4/delta, C) I(F): no failure.
- SEL-12(b): 199 random decision-tree partitions: cost <= K(delta/2) I_sel: no failure.
- SEL-2: 342 random low-energy multiplexers: H(F) <= max(C, K(I_sel/a)) I(F): no failure.
- SEL-9 weighted real-leaf form (code/affine_c1_real.py, 450 instances, real leaves of random norms): max excess 9e-16.

Structural remark for whoever attacks SEL-8' / SEL-13. In the two-cell moment problem the optimal laws found by the LP
put NO mass at the minor vertex: for p_1 = 0.001 the optimiser uses an atom of weight 0.978 at angle 0.0046 from the
major vertex and an atom of weight 0.022 at angle -0.213 on the other side. A dual certificate must therefore control
f(tau+alpha) - f(alpha) - f(tau) on a whole neighbourhood of the major vertex (curvature f''(alpha) ~ 2log2(1/alpha^2)
against the entropy cost tau^2 log(1/tau^2)), not only first-order terms at the vertices. Per-instance quadratic
certificates Phi(c) <= c^T Gamma c + kappa (1 - sum c_k^4) cannot work in general: near e_k the linear term of Phi is
2 sum_l A_kl c_k c_l with A_kl = sum_x v_k(x) v_l(x) log2(1/v_k(x)^2), and A is not symmetric; the diagonal of the dual
multiplier must carry the asymmetry at cost O(s_k).

## 7. Failed attempts and dead ends (kept with their witnesses)

- A linear low-energy credit cost <= K I_sel: dead by SEL-3 (bent point-flip, ratio log2(1/delta)+3/ln2).
- An energy-uniform ratio closure independent of the fraction c without structure: equivalent to FEI (SEL-4).
- Per-T coherent-sum bound "H(nu_T) <= H(w(T)) + sum_j w_j(T) H(q_j)" for general cells: false per T (two balanced
  cells, anti-aligned leaves at T give H(nu_T) = H(h) > 2 + H(h)/2 once H(h) > 4); only averaged statements can hold.
- The general SVD-entropy lemma behind a one-line proof of T1-sharp: REFUTED by M = [[2,-1],[-1,-1]] (5.2).
- Pointwise Gibbs-type proof of SEL-11 via Aβ log(β^2/A^2) <= kappa(β^2 - Aβ): fails for small β of sign opposite
  to A; the AEP proof replaces it.
- Small explicit functions with H > 4I: none on <= 4 variables (max 3.4025, AND_4), lexicographic functions up to
  11 variables stay below 3.951, tribes/AND-OR compositions below 3.69; composition of the 4-bit g above is the
  smallest exact witness found (64 variables). (The balanced 6-bit hill-climb optimum has H/(I-1) = 6.27895,
  O'Donnell-Tan's 6.278944 value, code/search_strong.py; its plain ratio is only 2.41.)
- T1-sharp (C010 formula as an upper bound for orthogonal leaves): refuted for real and for Boolean leaves (5.2).
  Random search and hill climbing at n <= 6 missed it; the witness came from the p_2 -> 0 expansion (Omega), which
  is the lesson: search the asymptotic regime the moment analysis points to, not uniform random instances.
- General SVD-entropy lemma without defect: refuted (5.2); with defect kappa_0 B it is SEL-13 (open).

## 8. Next step for the fleet

Prove SEL-13 (Schmidt-entropy defect): H(|M|^2) <= H(s) + sum_k s_k [H(u_k^2)+H(v_k^2)] + kappa sum_k s_k(1-s_k) for
every real matrix and SVD, with any absolute kappa (numerically kappa_0 = 0.75615 is sharp, at the near-rank-one 2x2
limit [[t,1],[t^2(1-eta),t]], eta = 4.591). It is a self-contained matrix inequality, it implies SEL-8' and hence the
constant-preserving orthogonal-leaf selector closure max{C_s, 4.757, C_g}(I-1) for arbitrary FEI-good cells (C026
with Fourier-disjointness replaced by orthogonality; with cells drawn from the class itself), and it is the correct
replacement of the refuted coherent-sum bound C034. A first milestone is the two-cell case, which reduces to the
one-angle moment inequality E[f(t+alpha) - f(t)] <= f(alpha) + kappa' p_1 p_2 (E[cos^2 t] = p_1, E[sin 2t] = 0,
f(t) = h(cos^2 t)); the LP gives kappa' = 1.175, and a dual certificate (lambda(alpha), nu(alpha)) checked by interval
arithmetic on a compact alpha-range plus an alpha -> 0 expansion would make it a theorem.
