# Referee report: route SEL-selector-interference

Independent referee (Opus), 12 Oct 2026. Full FEI is OPEN; nothing below claims otherwise.
Scope: every claim in CLAIMS.json marked PROVED, REFUTED or KNOWN (SEL-1 ... SEL-15, SEL-K1).
The two CONJECTURE claims (SEL-8', SEL-13) get no verdict here; they were stress-tested only (section 5).

## 0. Method

- Every proof was re-derived from the definitions (section 2, claim by claim). For each step I record what was
  checked and where each hypothesis is used.
- My own code in `referee_code/` (written from scratch; the author's `code/` was read only to learn the index
  convention of the published witness tables) computes Walsh transforms in exact int64 integers, influences as exact
  fractions (disagreement counts), entropies in float64 (evidence), with mpmath interval arithmetic at 60 digits
  (certificates), or as exact rationals where all spectral masses are dyadic.
- Exhaustive tests at total dimension n <= 4 for every inequality; structured, random and adversarial families beyond.
  Every check prints the maximum of (left side - right side) over its instances, so each could have failed.

| script | claims | instances |
|---|---|---|
| check_sel1_2.py | SEL-1, SEL-2 | every Boolean function of 2, 3, 4 variables x every split a (197,136); 33,000 random and low-energy multiplexers, n = 5..8 |
| check_falsifiers.py | SEL-1, SEL-2 | X001 parity lifts, X002 parity splice, X003 sparse activation, X004 overlap |
| check_sel3.py | SEL-3 | bent point flip m = 2..18 (exact Walsh, 50-digit logs), products with a = 2 |
| check_twocell_identity.py | SEL-15, SEL-8, SEL-3 | two-cell reduction identity (3,000 random instances); X009 split of the bent-flip cost |
| check_sel4.py | SEL-4 | M_g identities on 300 balanced g |
| check_sel5_6.py | SEL-5, SEL-5b, SEL-6 | 140 random f (n <= 7), 60 recursive one-bit decompositions, exact spectra of g and g o g |
| check_sel7_14_15.py | SEL-7, SEL-14, SEL-15, SEL-15c | 23,140 exhaustive SEL-7 instances (18,616 balanced two-cell), 49,776 exhaustive sign averages, 1,052 random, 300 members of M_4 |
| check_sel8.py | SEL-8 | Boolean witness r = 1..18 with interval logs; SVD witness (40 digits); real-leaf witness |
| check_sel9_10_11.py | SEL-9, SEL-10, SEL-11 | 2,049,252 exhaustive (every affine partition of F_2^a, a <= 3, every Boolean leaf assignment on 4-a data bits, plus constant leaves at a = 4); 591,364 at 5..7 variables; 9,108 real-leaf; 300 SEL-11; 40 adversarial optimisations |
| check_sel12.py | SEL-12 | 152,940 exhaustive decision-tree instances with delta > 0 (n = 4, all 146 tree partitions at a = 3); 10,186 random; 200 telescoping checks; random recursive constructions |
| stress_sel13.py, probe_2x2*.py, probe_famK_mp.py | SEL-13 (conjecture) | families, 40,000 random multi-scale matrices, high-precision 2x2 search, 60-digit re-evaluation of float optima |

## 1. Verdict summary

| claim | author status | verdict | one-line reason |
|---|---|---|---|
| SEL-1 | PROVED | CONFIRMED | identity + Maassen-Uffink + BR log-Sobolev + subadditivity all re-derived; 230k instances, max violation 9e-16 (float noise); X002 attains it exactly |
| SEL-2 | PROVED | CONFIRMED | h(t)/t nonincreasing; all K values and the crossover 0.30925 recomputed; closure checked on every instance |
| SEL-3 | PROVED | CONFIRMED | closed forms equal exact Walsh entropies to 50 digits (m = 4..18); cost/bound = 0.99999934 at m = 18; products additive. The unboundedness part is already X009 (see remarks) |
| SEL-4 | PROVED | CONFIRMED | reduction re-derived; energy bookkeeping I_sel = (tI(g)+1)/2 >= c(tn+1) needs c <= 1/2 (stated in NOTES, omitted in the CLAIMS line, harmless) |
| SEL-5 | PROVED | CONFIRMED | B_b(b) = f(b), distinct characters; one-bit recursion verified (needs the chi_S G bookkeeping, see remarks) |
| SEL-5b | PROVED | CONFIRMED | definitional: F(x,z) = g_x(x,z) = g~_x(z) is a fresh node |
| SEL-6 | PROVED | CONFIRMED | H(g) = 3, I(g) = 3/2, H(g o g) = 15/2, I(g o g) = 9/4 by exact 16-variable Walsh; composition lemma checked on the full spectrum; H(G) = 57/4 > 27/2 = 4I(G). H > 4I itself is classical (remarks) |
| SEL-7 | PROVED | CONFIRMED | marginals, subadditivity, exact influence identities, closures (iv) and (v) re-derived; 24k instances, all exact identities hold as fractions |
| SEL-8 | REFUTED | CONFIRMED (the refutation stands) | Boolean witness recomputed from its description: r = 9 excess in [1.40285500346969e-5, 1.40285500346970e-5] (60-digit intervals); expansion constant Omega re-derived analytically; SVD witness gap 0.0333249268439756; real-leaf witness 0.0307067 |
| SEL-15 | PROVED | CONFIRMED | (ii) re-derived (simpler route below); two-cell reduction identity verified to 2e-15; 18,616 exhaustive balanced instances max excess 0; corollary algebra checked; 300 M_4 members max H - 4(I-1) = 0 |
| SEL-14 | PROVED | CONFIRMED | averaging + concavity; exact E_eps I_sel = D on every instance. Reads "any Boolean leaves" (orthogonality not needed) |
| SEL-9 | PROVED | CONFIRMED | tensor-power/AEP proof checked line by line; 2.6M Boolean and 9k real instances, adversarial maximum 2.7e-15; ACKSW Theorem 1.6 citation verified; leaf extension not found in the literature I could scan (novelty unverified) |
| SEL-11 | PROVED | CONFIRMED | H(r) identity re-derived; special case of SEL-9; 300 instances |
| SEL-10 | PROVED | CONFIRMED | edge-counting bound I_sel >= (delta/2) sum p_j r_j re-derived (x^i leaves an affine cell iff i occurs in its dual); c_j <= r_j; checked on every Boolean affine instance |
| SEL-12 | PROVED | CONFIRMED | (a) induction on SEL-2; (b) per-node one-bit SEL-1, telescoping of cost and of I_sel verified exactly on 200 random trees; 163k instances, max violation 0 |
| SEL-K1 | KNOWN | CONFIRMED | C012 and X005/C014 in the campaign ledger say exactly this |

No claim was found false and no proof step was found missing. Minor corrections are listed in section 4.

## 2. Claim-by-claim

### SEL-1 (CONFIRMED)

Statement checked: for F(x,y) = g_x(y), x a fresh uniform a-bit block, arbitrary Boolean branches on a common data cube,
cost(F) = H(F) - avg_b H(g_b) = H(S|T) + I(X;Y) <= sum_i h(pi_i) + min{sum_i h(pi_i), (2/ln2) I_sel}, pi_i = Inf_{x_i}(F).

Re-derivation.
- Fhat(S,T) = N^{-1} sum_b chi_S(b) ghat_b(T). Parseval in b gives sum_S Fhat(S,T)^2 = R_T := N^{-1} sum_b ghat_b(T)^2, so
  the data marginal of Fhat^2 equals the data marginal of the channel law P(b,T) = ghat_b(T)^2/N. Chain rule on both
  laws: H(F) = H(R) + H(S|T) and a + avg H(g_b) = H(R) + sum_T R_T H(r_T), i.e. H(R) = avg H(g_b) + I(X;Y) with
  I(X;Y) = a - sum_T R_T H(r_T) (X uniform). Hence (i). In the code R and R' are computed independently (from F and from
  the branches); max |R - R'| = 0 on every instance.
- (ii) first bound: with u_T(b) = ghat_b(T)/sqrt(N R_T) (a unit vector) and W the orthogonal Walsh matrix (entries
  +-N^{-1/2}), Fhat(S,T) = sqrt(R_T) (W u_T)(S), so nu_T = (W u_T)^2 is the conditional law of S given T. Maassen-Uffink
  (H. Maassen, J. B. M. Uffink, Phys. Rev. Lett. 60 (1988) 1103) gives H(r_T) + H(nu_T) >= -2 log2 max|W_ij| = a.
  Average over T ~ R: I(X;Y) <= H(S|T).
- (ii) second bound: BR eq. (5). I re-derived its normalisation: the two-point Gross inequality in natural units is
  Ent(g^2) <= (1/2) E[(g(x) - g(x^i))^2] per coordinate (equivalently 2 E(D_i g)^2), it tensorises, and with
  g = |v_D| (v_D(x) = ghat_x(D)), q(D) Ent(w_D) = Ent(v_D^2), the reverse triangle inequality and Parseval in y give
  (ln 2) I(X;D) <= (1/2) sum_i E_x E_y (F(x,y) - F(x^i,y))^2 = 2 I_sel.
- (iii) H(S|T) <= H(S) <= sum_i H(1[i in S]) (S is a function of its indicator vector) and P[i in S] = Inf_{x_i}(F)
  because F is Boolean; Jensen for the last step.
Evidence: all 65,536 functions of 4 variables with a = 1, 2, 3 (and n = 2, 3): 197,136 instances; 33,000 random/biased/
low-energy multiplexers at n = 5..8. Max of each (lhs - rhs): IXY - HST 4.4e-16, IXY - (2/ln2) I_sel 0, HST - sum h 8.9e-16,
cost - bound 8.9e-16. The bound is attained: ratio 1.000 on small cases and exactly on the X002 parity splice
(cost = 2 = bound for m = 3..11, check_falsifiers.py). Consistent with the independent Codex validation A020
(run 20261011T225608Z) of the a h(s/a) + (2/ln2)s form.

### SEL-2 (CONFIRMED)

h is concave with h(0) = 0, so h(t)/t (a chord slope from the origin) is nonincreasing on (0,1]. With c' = I_sel/a >= c,
SEL-1 gives cost <= a min{2h(c'), h(c') + (2/ln2) c'} = I_sel min{2h(c')/c', h(c')/c' + 2/ln2} <= K(c) I_sel; adding
avg H(g_b) <= C I_data gives the closure. Recomputed: K(1/2) = 4, K(0.25) = 6.1305, K(0.1) = 7.5753, K(0.01) = 10.9647,
K(0.001) = 14.2931; crossover h(c)/c = 2/ln2 at c* = 0.3092494; K(c) < 2/c iff h(c) < 1 iff c != 1/2 (and K(c) <= 2h(c)/c).
Asymptotics: h(c)/c = log2(1/c) + log2 e + O(c). Evidence: H(F) - max{C, K(I_sel/a)} I(F) <= 0 on all 230k instances
(C = max_b H(g_b)/I(g_b)).

### SEL-3 (CONFIRMED)

Re-derived: bhat(S) = eps s_S, sum_S bhat(S) = b(0) = 1 fixes the sign counts; 1_{t=0} has all coefficients eps^2;
F = b - 1_{t=0} + z 1_{t=0} gives Fhat(empty_z, S) = bhat(S) - eps^2, Fhat({z}, S) = eps^2; total masses sum to 1;
the three closed forms follow; the expansions (1-x)ln(1-x) + (1+x)ln(1+x) = x^2 + O(x^4) and
(1+x)(1-2x)^2 ln(1-2x) + (1-x)(1+2x)^2 ln(1+2x) = 8x^2 + O(x^4) are correct (I expanded the second to second order).
Evidence (check_sel3.py, exact Walsh, 50-digit logarithms): closed forms agree with the Walsh entropies to < 5e-50 for
m = 4..18 (at m = 2 the closed form for H(b') has 0 log 0, a convention issue only). cost/delta = 8.030013847, 10.255970235,
12.310194289, 14.323620862, 16.326969583, 18.327806271, 20.328015412, 22.328067695 for m = 4..18 (author's table
reproduced); m + 3/ln2 = 22.328085 at m = 18; cost/(SEL-1 bound) = 0.96957, 0.99411, ..., 0.99999934. Products with a = 2:
cost(prod) = 2 cost(F_m) to 1e-15 and each selector influence = 2^-m.
Remark (attribution): the conclusion "no cost <= K I_sel with absolute K" already follows from X009 (RIG sections 2-3):
for a one-bit selector H(S|T) = B_t, and X009 gives B_t/delta = log2(1/delta) + 1/ln2 + O(delta). I checked the split:
H(S|T)/delta = 17.442640 vs m + 1/ln2 = 17.442695 and I(X;Y)/delta = 2.885375 vs 2/ln2 = 2.885390 at m = 16. What SEL-3
adds is that both pieces of SEL-1 are attained simultaneously (the constant 3/ln2 is sharp). Cite X009.

### SEL-4 (CONFIRMED)

Upper bound: SEL-2 with C = 0. Lower bound: for g with I(g) >= 2cn, g_t = z prod_r g(x^(r)) has H = tH(g), I = tI(g)+1;
M_{g_t} has dictator branches (H = 0), its selector block is the tn+1 inputs of g_t, and Inf_{x_j}(M) = Inf_j(g_t) P[y_1 != y_2]
= Inf_j(g_t)/2, so I_sel = (tI(g)+1)/2 >= c(tn+1) because tI(g) >= 2ctn and 1/2 >= c. Ratio (2 + tH/2)/(3/2 + tI/2) -> H/I.
sup_c: c = I(g)/(2n) <= 1/2 works for each nonconstant g. The equivalence with full FEI is then immediate in both directions.
check_sel4.py verifies H(M_g) = 2 + H(g)/2 (to 9e-16), I(M_g) = 1 + I(g)/2 and I_sel = I(g)/2 (exact) on 300 balanced g.
The CLAIMS line omits "0 < c <= 1/2"; for c > 1/2 the set {I(g) >= 2cn} is empty (I(g) <= n), so nothing breaks.

### SEL-5 (CONFIRMED) and SEL-5b (CONFIRMED)

chi_{S_b}(b) = (-1)^{|S_b|}, so B_b(b) = f(b); b -> S_b is injective, so the branches are distinct characters, Gram matrix
2^n I (checked exactly on 140 random f, n <= 7). One-bit recursion: Mux_v(F|_{v=+1}, -v F|_{v=-1}) reproduces F and
E[-v F_+ F_-] = 0. Note for the record: the iteration must be run on the factor G of chi_S G (split on a relevant variable
of G, the second branch becomes chi_{S u {v}} (-G_-)); splitting again on v itself loops. With that bookkeeping every node is
exact and full-cube orthogonal and every leaf is a signed character (60 random f, n <= 6). SEL-5b: F(x,z) = g_x(x,z) =
g~_x(z) is literally a fresh-selector node with branches g~_b, so C035 applies when its hypotheses are put on g~_b.

### SEL-6 (CONFIRMED)

Exact: ghat = 1/2 on {2},{3}; 1/4 on {0},{1},{0,2},{1,3}; -1/4 on {1,2},{0,3},{0,2,3},{1,2,3}; E g = 0; H(g) = 3, I(g) = 3/2.
g o g built as a 16-variable truth table: H = 15/2 and I = 9/4 exactly (all coefficients are powers of two, so H is computed as
an exact rational); its full spectral multiset equals the one predicted by the balanced composition lemma. The lemma (also
the baseline's comp:identities with uniform measure; O'Donnell-Tan, ICALP 2013) then gives H(G) = 57/4 = 3 + (3/2)(15/2)
= 15/2 + (9/4)3, I(G) = 27/8, 4I(G) = 27/2 < 57/4, H/I = 38/9; the sequence H/I = 2, 10/3, 38/9, 130/27, ... = 6(1-(2/3)^k).
The logical step is right: a reuse-node closure with constant max(4, C_leaf) plus SEL-5 (C_leaf = 0) would give
H(f) <= 4 I(f) for every Boolean f.
Remark: that some Boolean f has H > 4I is classical (O'Donnell-Tan's composition lower bound about 6.278; Hod 2017,
arXiv:1711.00762, above 6.45; both cited in ACKSW section 1.1), so the failure of constant 4 under reuse was already implied;
SEL-6 supplies a small exact witness.

### SEL-7 (CONFIRMED)

Fhat(S,T) = sum_k ahat_k(S) Ghat_k(T). S-marginal: sum_T Ghat_k Ghat_l = E[G_k G_l] = delta_kl (orthonormal leaves used here).
T-marginal: sum_S ahat_k ahat_l = E[a_k a_l] = p_k delta_kl (disjoint cells; no leaf hypothesis). Subadditivity plus
"marginal entropy <= joint entropy" for the laws ahat_k(S)^2 on (k,S) and p_k Ghat_k(T)^2 on (k,T) give (ii). (iii): Boolean F,
so I_sel = sum_S |S| mu(S); ahat_k(S) = hhat_k(S)/2 off the empty set. (iv): I re-derived the paper identity
H(p) + sum p_k H(q_k) = (1/4) sum H+(h_k) + R(p) (empty-set terms give 2 sum p_k^2 log(1/p_k); nonempty terms give
(1/4)H+(h_k) + (1/2)Var(h_k) = (1/4)H+(h_k) + 2p_k(1-p_k)); with H+ <= H <= C_s I, R(p) <= 4D and H(p) <= 2D
(edge isoperimetry I(h_k) >= 2 p_k log2(1/p_k)) the selector part is <= (C_s + 6) D. (v): (1/4) sum H+ <= C_s(D - B),
R <= 4B, 0 <= B <= D, plus H(p) <= 2D; balanced leaves give I(F) - 1 = D + sum p_k (I(G_k) - 1) with each I(G_k) - 1 >= 0.
Evidence: exhaustive at n <= 4 (every function whose distinct branches are pairwise orthogonal is an instance with cells =
equal-branch classes): 23,140 instances; random: 1,052 instances with orthogonal families built by half-flips, bent leaves,
bent times characters (balanced), the Maj3 pair of the paper, cells random / Hamming-ball / point / balanced. Identities (i)
max error 0, (iii) exact as fractions on every instance, (ii) and closures (iv), (v) max excess 0 (equality cases).
The recursion statement follows by induction (leaves in the class, fresh selector, orthogonality at every node).

### SEL-8 (CONFIRMED: the refutation stands)

T1-sharp (the C010 value as an upper bound for pairwise orthogonal leaves) is false.
- Boolean witness, rebuilt from its verbal description with 0-based data coordinates (my tables coincide with the
  author's stored ones): E[G1] = 1/8, E[G2] = 7/8, E[G1 G2] = 0, both supports all 16 sets. A_2 = {x = (1,...,1)},
  p_2 = 2^-r. Exact Walsh integers of F on r + 4 variables, exact rational cell spectra, mpmath intervals at 60 digits:
  r = 9: excess in [1.40285500346969e-5, 1.40285500346970e-5] (13 variables). Also r = 10: 2.24317e-5, r = 14: 2.49882e-6,
  r = 18: 1.62207e-7; the excess is negative for r <= 8, so the witness needs p_2 <= 2^-9.
- Expansion. I derived it independently: with V = (G1 - G2)/2 and eps = p_2, Fhat(empty,T) = G1hat - 2 eps Vhat and
  Fhat(S,T) = -2 eps Vhat for S != empty; using ||V||^2 = 1/2 and <G1,V> = 1/2 (orthogonality) and
  |G1hat| >= 1/8 on its support, excess = eps [4H(V) - 4 sum_T G1hat Vhat log2(1/G1hat^2) + H(G1) - H(G2) - 4]
  + O(eps^2 log(1/eps)). This is the author's Omega. For the witness Omega = 0.0426594; excess/p_2 = 0.03676, 0.04094,
  0.04252 at r = 12, 14, 18, converging to it.
- SVD-lemma witness M = [[2,-1],[-1,-1]]/sqrt7 (distinct singular values, so the SVD is unique up to signs):
  H(|M|^2) - [H(s) + sum s_k(H(u_k^2) + H(v_k^2))] = 0.0333249268439756 (40-digit mpmath).
- Real-leaf witness (2 selector bits, A_1 = {(1,1)}, G1 = cos e - sin e y, G2 = sin e + cos e y, e = 0.05):
  ||F||^2 = 1, excess = 0.0307067 bits.

### SEL-15 (CONFIRMED)

(ii) A shorter route that I checked: H(F) = H(R) + sum_T R_T H(nu_T); with p = (1/2,1/2) and hhat(empty) = 0,
nu_T puts mass 1 - m_T on the empty set and spreads m_T proportionally to hhat^2, so H(nu_T) = h(m_T) + m_T H(h) <= 1 + m_T H(h);
sum_T R_T m_T = p_1 p_2 E[(G1 - G2)^2] = (1 - <G1,G2>)/2 = 1/2 (orthogonality used exactly here); H(R) <= H(p) + avg H(G)
= 1 + avg H(G). Total <= 2 + H(h)/2 + avg H(G). Influence: I_sel = (I(h) + I(-h))/4 = I(h)/2.
The general two-cell reduction of NOTES 5.2 (on which SEL-8's analysis also rests) was verified as an identity on 3,000
random instances with unbalanced p: max |difference| = 2.2e-15, and the direct off-empty mass of nu_T equals cos^2(t+alpha)
to 6e-16.
Corollary SEL-15c: 2 + (C/2)(I(h) - 1) + (C/2)(I(G1) + I(G2) - 2) = C(I(F) - 1) + 2 - C/2 <= C(I(F) - 1) iff C >= 4; members are
balanced by induction. Evidence: 18,616 exhaustive balanced two-cell instances (n <= 4): max excess 0, influence identity exact;
300 random members of M_4 built from signed dictators (orthogonal pairs from disjoint supports and from Mux_h'(A,B), Mux_h'(A,-B)),
up to 16 variables: max H - 4(I - 1) = 0 (addressing-type equality cases).

### SEL-14 (CONFIRMED)

E_eps Fhat_eps(S,T)^2 = sum_k ahat_k(S)^2 Ghat_k(T)^2 (cross terms carry eps_k eps_l, mean 0); concavity of entropy and
"marginal <= joint" for the law on (k,S,T). Influence: an edge between cells j != l contributes (1 - eps_j eps_l <G_j,G_l>)/2,
mean 1/2; and D = (1/4) sum_k I(h_k) = (1/2) sum_i P[J(x) != J(x^i)] (each crossing edge leaves exactly two cells). The
existence of a good re-signing follows from E[H - K I] <= 0. Evidence: exact E_eps I_sel = D on every instance (49,776
exhaustive at n <= 4 plus random), max E_eps H - C010 value = 8.9e-16. Wording: "any leaves" should read "any Boolean leaves
(no orthogonality needed)"; for real leaves the entropy part holds with w_k = p_k ||G_k||^2 in place of p_k, the influence
identity needs Boolean leaves.

### SEL-9 (CONFIRMED)

Checked line by line: (1) F^(k) = prod_i F(x^i,y^i) has spectral law (Fhat^2)^{tensor k}; (2) the expansion over labels
J in [m]^k with A_J a product of affine cells (affine, codimension sum c_{j_i}, indicator Fourier support exactly V_J^perp of
size 2^{c_J}); (3) the three typicality conditions hold with w^{tensor k}-probability -> 1 by the weak law (finite alphabet),
|Jtyp| <= 2^{k(H(w)+eps)}; (4) |Ttyp(J)| <= 2^{sum_i H(Lambda_{j_i}) + k eps} and Chebyshev for the sum of independent
-log Lambda_{j_i}(T_i) gives Lambda_J(Ttyp^c) <= s^2/(k eps^2), s^2 finite by finite support; (5) 1_{A_J}(x) u(y) for distinct J
are orthogonal (disjoint x-supports), so ||F^(k) - Ftil||^2 = sum_{J not typical} w_J + sum_{J typical} w_J Lambda_J(Ttyp^c)
<= alpha_k + s^2/(k eps^2) (uses ||G_J||^2 = prod l_{j_i} and p_J ||G_J||^2 = w_J); (6) Ftil is supported in B_k, so the
mass of F^(k) off B_k is at most beta_k; (7) H(P) <= h(beta) + log|B| + beta log|Omega| with |Omega| = 2^{k(a+n)}; divide by k.
No step uses Booleanity of the leaves; labels with l_j = 0 are dropped consistently.
Literature: ACKSW, "Improved bounds on Fourier entropy and Min-entropy", arXiv:1809.09819v2 (ACM ToCT 13(4), 2021),
Theorem 1.6: "Let f be any Boolean function. Then H(fhat^2) <= 2 aUC^xor(f)", with the tensorisation/AEP proof outlined on p. 6
(read 12 Oct 2026 from the arXiv PDF). The constant +-1-leaf case of SEL-9 is exactly that bound for a given monochromatic
affine partition. I found no statement of the leaf extension in ACKSW's introduction or in an arXiv title/abstract listing of
"Fourier entropy" papers (export.arxiv.org query, 12 Oct 2026); a full literature search was not possible (the session's web
search budget was exhausted), so novelty remains unverified, as the author says.
Evidence: exhaustive over all 912 affine partitions of F_2^3 (280 not splittable by any hyperplane), all 11 of F_2^2, both of
F_2^1, every Boolean leaf assignment on 4-a data bits: 2,049,252 instances, max H(F) - [2 sum p c + sum p H(g)] = 0 (equality
cases); 591,364 more at 5..7 variables (random partitions of F_2^4, F_2^5, 79 pct of the F_2^4 ones irreducible); 9,108 real-leaf
instances of random norms (max excess 0, mass normalisation to 7e-16); 40 Powell maximisations of the real-leaf gap on
irreducible partitions: best 2.7e-15.

### SEL-11 (CONFIRMED)

r(x) = v_j^2/N on A_j, |A_j| = 2^{a-c_j}: H(r) = sum_j w_j (a - log2(v_j^2)) = H(w) + sum_j w_j (a - c_j) using
log2(v_j^2) = log2 w_j + c_j. Adding SEL-9 with constant leaves (H(Lambda_j) = 0) gives a + 2H(w). Evidence: 300 random
real cell-constant functions on random affine partitions of F_2^4, F_2^5: identity error 1.6e-15, max of
H(Psihat^2) + H(r) - a - 2H(w) = -1.4e-5.

### SEL-10 (CONFIRMED)

Inf_{x_i}(F) = E_x[(1 - <g_{J(x)}, g_{J(x^i)}>)/2] >= (delta/2) P[J(x) != J(x^i)] (adjacent distinct cells only);
x + e_i stays in an affine cell iff e_i is in its direction space iff i occurs in no element of the dual subspace, so
sum_i P[J(x) != J(x^i)] = sum_j p_j r_j; c_j <= r_j because a c_j-dimensional subspace needs at least c_j coordinates. With
SEL-9 (Boolean leaves) H(F) <= 2 sum p_j c_j + sum p_j H(g_j) <= (4/delta) I_sel + C I_data; the strong form uses
I(F) - 1 = I_sel + sum p_j (I(g_j) - 1). Evidence: on every Boolean affine instance above with delta > 0: max of
(delta/2) sum p_j r_j - I_sel = 0, max of H - max(4/delta, C) I = -1.1, strong form (balanced leaves) max 0.
"Contains C035 and C011 at delta = 1" is correct (point cells with orthogonal neighbours; Fourier-disjoint balanced leaves are
orthogonal).

### SEL-12 (CONFIRMED)

(a) Induction: branches previously built satisfy H <= C' I with C' = max{C_leaf, K(c)}; SEL-2 at the node gives
max{C', K(c)} = C'. (b) At a node v querying x_i (never re-queried below v), F_v = Mux_{x_i}(F_{v+}, F_{v-}) with branches on the
cube of the unqueried selector bits and the data, so SEL-1 with a = 1 applies; for each x' the two leaves reached are distinct
adjacent cells, so pi_v >= delta/2; cost telescopes (cost = sum_v P(v) cost_v) and I_sel = sum_v P(v) pi_v (flipping x_i changes
the path only at the unique node querying i). Both telescoping identities were verified on 200 random trees (failures 0).
Evidence: exhaustive over all 2, 8 and 146 decision-tree partitions for a = 1, 2, 3 and all Boolean leaves on 4-a data bits
(152,940 instances with delta > 0) and 10,186 random instances at a = 3..5: max of cost - K(delta/2) I_sel = 0 (equality at
a = 1 with Fourier-disjoint leaves) and of H - max(C, K(delta/2)) I = 0. Random recursive constructions for (a): max of
H - max(C_leaf, K(c_min)) I = -2.4.

### SEL-K1 (CONFIRMED as KNOWN)

C012 (CLAIMS.md: M_g with two cells and orthogonal dictator leaves; tensoring gives the optimal constant C_FEI) and
X005/C014 (COUNTEREXAMPLES.md: singleton cells with leaves g(u)y, i.e. copies or anticopies of one dictator, represent any g
with H(F) = H(g), I(F) = I(g) + 1) say exactly what SEL-K1 cites. They mark the boundary correctly: M_g violates the
"cells from an FEI-good class" hypothesis of SEL-7/SEL-15c (its cell indicator is an arbitrary g), and X005 is delta = 0 in SEL-10.

## 3. Mandatory falsifiers replayed (check_falsifiers.py and the scripts above)

- X001 parity lift (selector z): cost = 0 (spectra are signed relabelings), SEL-1 and SEL-2 hold.
- X002 parity splice: cost = 2 = SEL-1 bound exactly for m = 3, 5, 7, 9, 11 (h(1/2) + min{1, (2/ln2)(1/2)} = 2).
- X003 sparse activation splice (k = 4, r = 8 and k = 6, r = 12): cost/bound = 0.508, 0.464; SEL-2 holds.
- X004 F = zy: cost 0; SEL-7 does not apply (leaves y, -y are not orthogonal), consistent.
- X009 bent point flip: SEL-3 above; cost = B_t + JS term, both attained.
- X013 coherent orthogonal vectors: as real leaves of a one-bit affine selector they give H(F) = 4.5 <= 6 = SEL-9 bound, so no
  conflict with SEL-9's real-leaf form; the T1-sharp failure of SEL-8 is the Boolean realisation of the same phenomenon.
- Overlapping supports with orthogonality (Maj3 pair, bent times characters, half-flip families): SEL-7, SEL-14, SEL-15 hold.

## 4. Points for the author (none changes a verdict)

1. SEL-3: cite X009 (RIG sections 2-3) for the unboundedness of cost/I_sel; state the new content as sharpness of SEL-1.
2. SEL-4: put "0 < c <= 1/2" into the CLAIMS line (it is in NOTES).
3. SEL-14: "any leaves" -> "any Boolean leaves (orthogonality not required)".
4. SEL-6: say that H > 4I for some Boolean f is classical (O'Donnell-Tan; Hod), the claim being the explicit small witness.
5. SEL-8: the Omega expansion is stated without derivation in NOTES; the derivation sketched in section 2 above (single-point
   cell, uses ||V||^2 = 1/2, <G1,V> = 1/2 and the granularity |G1hat| >= 2^{1-n}) should be added.
6. SEL-5: record the chi_S G bookkeeping of the one-bit recursion (splitting on the new character variable loops).
7. SEL-9: novelty of the leaf extension is unverified (my scan found nothing, but it was not a full search).

## 5. Conjectures stress-tested (no verdict)

SEL-13 (Schmidt-entropy defect, kappa_0 = 0.756151564). stress_sel13.py and probe_2x2*.py:
- The author's family [[t,1],[t^2(1-eta),t]] at eta = 4.59112: ratio gap/B = 0.75335 (t = 1e-2), 0.75611 (1e-3), 0.756151018 (1e-4),
  0.756151563912 (1e-6) in 50-digit arithmetic, converging to kappa_0 from below.
- K x K generalisation M = [[1, t b^T], [t a, t^2(a b^T - X)]] (Schur complement -t^2 X), Nelder-Mead over (a, b, X):
  best 0.7565 (K = 2), 0.7551 (K = 3), 0.7520 (K = 4) at t = 1e-2 in float64; 40,000 random multi-scale matrices up to 5 x 5:
  max 0.7531.
- Precision warning: float64 manufactures ratios above kappa_0 at extreme scales. A float64 Nelder-Mead over 2 x 2 matrices
  reported 0.8419 at a point whose 50-digit value is 0.7547; the K = 2 family optimum 0.7565012 (float64) is 0.7558393 at
  60 digits (probe_famK_mp.py; the four best K = 2 and K = 3 candidates all fall below kappa_0 at 60 digits); a 30-digit search
  reported 0.75622 at a point whose 60-digit value is 0.756151068. Every value above kappa_0 that I found disappeared at
  higher precision. So the evidence is consistent with
  kappa_0 being the supremum (approached, not attained), but anyone extending the numerics must evaluate candidate maxima at
  60+ digits.
SEL-8' was not tested beyond the SEL-8 witness family (excess/B -> Omega/2 ~ 0.021, as the author reports).

## 6. Reproduction

From `referee_code/`: `python check_sel1_2.py`, `check_falsifiers.py`, `check_sel3.py`, `check_twocell_identity.py`,
`check_sel4.py`, `check_sel5_6.py`, `check_sel7_14_15.py` (and `--m4only`), `check_sel8.py`, `check_sel9_10_11.py`,
`check_sel12.py`, `stress_sel13.py`, `probe_2x2.py`, `probe_2x2_mp.py`, `probe_famK_mp.py`. Each runs in a single process in under about
ten minutes on this laptop and uses well under 2 GB. Libraries: `rlib.py` (Walsh, entropy, influence), `affine.py`
(enumeration of affine partitions of F_2^a).
