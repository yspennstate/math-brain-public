# Referee report: route W-witness-cost (independent referee, 12 Oct 2026)

Status: COMPLETE. Full FEI remains OPEN; nothing in the refereed claims or in this report says otherwise.

Scope: every claim of CLAIMS.json marked PROVED (W-L1, W-L2, W-P41, W-T51, W-N61, W-C71, W-T111, W-L120, W-P121,
W-P123), Corollary 11.2 (NOTES 11.2, reported as PROVED in the summary), and the two sub-steps of the PARTIAL claim
W-P112 that the summary calls proved. The route made no REFUTED, KNOWN or CANDIDATE_FULL claims. EVIDENCE and
CONJECTURE items were not refereed as proofs; one evidence pipeline was replicated (section 5).

Every proof below was re-derived from the definitions in the manuscript (current-threshold-paper.tex: regularity and
D, lines 80-139; Gibbs and lem:levelentropy, 236-293; lem:pivotal-antichain, lem:antichain-noise, lem:ranktail,
326-441; the queue law, 822-860; prop:joint-witness, 1184-1295) and SEED_LEMMAS section 2, and then attacked with my
own code (referee_code/, written independently of the author's code/). The running log with all numbers is at the end.

## Verdicts

| Claim | Claimed | Verdict |
|---|---|---|
| W-L1 Lemma 3.1 (exclusive unions) | PROVED | CONFIRMED |
| W-L2 Lemma 3.2 (sum over single-root witnesses) | PROVED | CONFIRMED |
| W-P41 Prop 4.1 (exact spectrum of K) | PROVED | CONFIRMED |
| W-T51 Theorem 5.1 as written (middle term h(v) + v Lambda_1 + sum p log 1/Q <= 17 I) | PROVED | GAP (statement double-counts v Lambda_1) |
| W-T51 corrected: h(v) + sum_A p(A) log(1/Q_{1,1}(A)) <= 16.99 I, hence H <= 16.99 I | - | CONFIRMED |
| W-N61 Prop 6.1 (minimum-witness bound not linear in I) | PROVED | CONFIRMED (scope: cell-and-leaf representation and its complement, as the claim says) |
| W-C71 Cor 7.1 (exact entropy identity, H <= 10.38 I on K) | PROVED | CONFIRMED |
| W-T111 Theorem 11.1 and Cor 11.2 as written (<= 27 I with v Lambda_1 added) | PROVED | GAP (same double count) |
| W-T111 and Cor 11.2 corrected: h(v) + sum_A p(A) log(1/Q_{1,1}(A)) <= 26.71 I | - | CONFIRMED |
| W-L120 Lemma 12.0 (owner mass) | PROVED | CONFIRMED |
| W-P121 Prop 12.1 (H <= 23.55 I + 2.4 R) | PROVED | CONFIRMED |
| W-P123 mixture-of-orders refinement (H <= 23.55 I + 2.4 R_mix) | PROVED | CONFIRMED |
| W-P112 sub-steps: root term for all sets of every term DL; rank term for block sets | PARTIAL (sub-steps "proved") | CONFIRMED (the stated gap, the phi-set rank term, stands) |

## The one defect: v*Lambda_1 is counted twice in the statements of Theorems 5.1 and 11.1

NOTES section 1 defines Q_{1,lambda}(A) as the probability of a successful run with output A. That probability carries
the root normalizer: every run starts with the root draw, whose probability includes prod_l 1/(1+lambda pi_l) =
2^{-Lambda} (Lemma 3.2, and prop:joint-witness: log 1/Q <= Lambda + C). Gibbs with Q(empty) = 1-v, Q(A) = v Q_{1,1}(A)
gives H <= h(v) + sum_{A != empty} p(A) log(1/Q_{1,1}(A)), in which Lambda already appears (as v Lambda after averaging).

The statements at NOTES lines 165 and 257 (Theorem 5.1), line 429 (Theorem 11.1), line 491 (Cor 11.2, via "complete code
length"), and CLAIMS W-T51 and W-T111 read
  H(f) <= h(v) + v Lambda_1 + sum_A fhat(A)^2 log(1/Q_{1,1}(A)) <= 17 I(f)   (27 I(f) for 11.1).
The first inequality is true but weaker than Gibbs. The second does not follow from the proofs: both proofs begin with
log(1/Q(A)) <= Lambda_1 + ..., so they bound h(v) + sum p log(1/Q) and nothing more. The step that does not follow is the
final "Adding: H(f) <= h(v) + v log e + ..." read as a bound on the stated middle expression: the extra v Lambda_1
(up to v log e <= 1.443 I) is not covered.
- Theorem 5.1: the proof gives h(v) + sum p log(1/Q) <= 16.987 I. For the written middle expression it gives
  <= 18.43 I (17.87 I if one uses the paper's sharper h(v) <= 2I + (log e - 2)v). 17 is not reached.
- Theorem 11.1 and Cor 11.2: the proof gives <= 26.703 I; for the written expression it gives 28.15 I (27.59 I with
  the sharper h(v) bound). 27 is not reached.
- The "more precisely" bound of Theorem 5.1 (h(v) + (log e + 2)v + [...] I) is correct for h(v) + sum p log(1/Q) only.

Nothing numerical is wrong: the author's code (code/queue_cost.py lines 9-10 and 92-95) adds v Lambda once to costs
that exclude Lambda, which is the correct accounting. The literal statements are not refuted either: in every instance
I computed, the double-counted expression stays under 6.5 I (class K) and 6.2 I (term lists). The repair is one line:
delete "v Lambda_1 +" from the middle expression (or replace Q_{1,1}(A) there by 2^{Lambda_1} Q_{1,1}(A)). Then both
theorems are CONFIRMED with constants 16.99 and 26.71; the consequences H <= 17 I on K and H <= 27 I on the list
classes hold as stated.

## Claim by claim

### W-L1 (Lemma 3.1): CONFIRMED
(1+f)/2 = sum_l (1+h_l)/2 holds pointwise because at most one gate fires (f = -1: both sides 0; f = 1: exactly one
gate). The chi_A coefficient for A nonempty gives fhat(A) = sum_l hhat_l(A); hhat_l(A) != 0 forces A inside R_l. Used
correctly everywhere: the cells of a tree (Thm 5.1), unfolded paths (Thm 11.1) and level-set subcube partitions (12.1)
are disjoint, so the gates are exclusive.

### W-L2 (Lemma 3.2): CONFIRMED
P(root set = {l}) = (rho_l/(1+rho_l)) prod_{l' != l} 1/(1+rho_{l'}) = rho_l 2^{-Lambda_rho}. Then s = |A| <= |R_l|
(prob 1/(s(s+1))), B = A (prob prod theta/Z, a genuine law on s-subsets since Z = e_s(theta)), c = 0 (prob 1/2, empty
multiset), the queue empties and the output is A. Different l give different root sets, so the events are disjoint and
their probabilities add. Nothing in the proof uses lambda pi_l specifically, so any positive root odds work, as stated.
Independent check: a simulation of the actual random process (step 6) reproduces the event probabilities within
2.3 standard errors, and the empirical Q never falls below the witness sum beyond noise.

### W-P41 (Prop 4.1): CONFIRMED
(i) 1_{C_i} = prod over the path of (1 + s_u x_u)/2 (no label repeats along a path), control and data disjoint, so
fhat(T u B) = sum_i 1hat_{C_i}(T) ghat_i(B). (ii) Disjoint supports leave one leaf per B != empty; Parseval gives the
block mass p_i Var_i, spread as 4^{-c_i} on each T inside path(i). The self-audit correction is right: for a unate g,
|ghat({j})| = Inf_j(g) > 0 for every relevant j, so (DS) is the same as disjoint relevant blocks. (iii) Read-once
labels make the leaves containing x(v) exactly the leaves below v, with common signs on anc(v); the sum over the two
sides gives sigma(S) 2^{-d_v}(m_+ - m_-), total node mass 2^{d_v-1} 4^{-d_v}(m_+ - m_-)^2 = w_v. (iv) Flipping x(v)
switches between two subtrees on disjoint variables, independent with means m_+, m_-:
P(differ) = (1 - m_+ m_-)/2; and 1 - ab >= |a - b| on [-1,1]^2. (v) is the size average of (ii)-(iii).
Under K_EM every subtree has mean mu, so all w_v = 0 and the phi term vanishes, consistent with the formula.
Exact check (step 2): 7,000 random trees, every nonzero coefficient (value and sign) and every influence matched in
Fractions; deliberately wrong formulas tripped 56-59 of 60 times.

### W-T51 (Theorem 5.1): GAP as written; CONFIRMED with the corrected statement
Re-derived step by step.
- Representation: gates h_i = kappa_i AND [g_i = 1], i in G, M <= 2, R_i = path variables plus relevant variables of
  g_i (every path variable is relevant because g_i is not identically -1). The law is a valid subprobability for any
  orders; the orders matter only for the bound. Normalizer: sum_j theta_s(j) <= M s a/(a-1), so
  Z_s <= (eMa/(a-1))^s (s! >= (s/e)^s). Lambda_1 <= log e P(f=1) by exclusivity.
- Block sets: unique owner gate, Lemma 3.2 with one term. (a) log(1/pi_i) <= 1 + c_i + log(1/P_i) in both cap cases;
  Claim A (4P(1-P) log(1/P) <= 2I(g), from the edge-isoperimetric I >= 2q log(1/q)) checked exhaustively for n <= 4.
- Phi-sets (K_RO): every leaf below v owns T at the same path positions, so prod theta is gate-independent; sum of pi
  over the leaves below v equals P(reach v)(1 + m(v))/2 when no cap is active; Delta_v <= 1 + m(v); the two pieces
  w_v d_v = 2 I^phi_v - w_v and w_v log(1/Delta_v) <= (log e/e) Inf_{x(v)} follow. This step is sharp: one node
  x_0 ? g : -1 with E g = -1 + 2/e makes every inequality in it an equality (my step-(b) ratio reached 0.9999, never 1).
- (c) s(s+1) <= 3^s and the normalizer bound give v + log2(6ea/(a-1)) I.
- (d) T-part: distinct path ranks <= c_i, s >= |T|, psi_c concave, |T| ~ Bin(c_i, 1/2), so a I_X^blk. B-part: for
  j in B, s >= |B cap U_j| + 1, so log+(r(j)/s) <= F_j(B - j)/ln 2, and lem:ranktail applies to d_j g_i (antichain on
  every fiber of U_j by lem:pivotal-antichain, because the order is a desirability order of the regular leaf); this
  gives a(1 + ln 2)/ln 2 I_Y. Phi-set ranks: psi_{d_v}(s), s = 1 + Bin(d_v - 1, 1/2), Jensen, a I^phi.
- Sum: h(v) + (log e + 2)v + (6.613 + 4.932) I <= 16.987 I.
All hypotheses are stated and used: read-once labels only in (b) and the phi ranks; equal means only to kill
phi-sets; regularity only in (d) through lem:ranktail. Numerically (step 2), on 7,000 random instances the witness-sum
code is at most 6.37 I and each averaged part stays under its stated bound.
Scope remark (not a defect): the CLAIMS parenthetical "every subcube selector with balanced regular leaves" goes
slightly beyond the theorem's "selector trees", because some subcube partitions are not decision-tree partitions (for
example 00*, 1*0, *11, 010, 101 in {0,1}^3). The K_EM half of the proof never uses the tree, only that the cells are
subcubes partitioning the control cube, so the parenthetical is true by the same proof. It should say so.

### W-N61 (Prop 6.1): CONFIRMED (scope: the cell-and-leaf representation and its complement)
For A = {x_0} every witness is one gate, no edges, c = 0, and Z_1 >= theta_1(x_0) gives
C >= log(1/(lambda pi_l)) + 2 >= 2 - log t with t = lambda(1 - delta)2^{-(D+1)}, for ANY desirability orders. For t < 1
every other cost is >= 0 (root costs positive, Z >= prod theta, size and child terms >= 0), h(v) = 0, v = 1 and
Lambda >= 2^D log(1+t), so RHS >= (1-2delta)^2(2 - log t) + 2^D log(1+t). The three ranges of t (and the corrected
t >= 1 branch, where each witness has at most |A| roots, each >= -log t, and sum p|A| = I <= D/2 + 5/2) give
>= (1-2delta)^2 (D/2 + 2) for D >= 4. The mixture bracket (Lambda_j + C_j + log 1/w_j) is handled the same way, and the
other sets' brackets are >= 0 when every support size D + 1 + w is <= 2^D. The complement swaps OR/AND masses but keeps
pi <= 2^{-(D+1)}(1 - delta). I(F) formula and the bound 3.75 for D >= 16 with w = ceil(log2 D) check out, and so does
log(1/Q_{1,1}({x_0})) <= (log e)/2 + 3 + log2(2 zeta(6/5)) = 7.205 < 7.21.
Exact truth tables (D,w) = (1,2), (1,3), (2,2), (1,4) confirm the spectrum; a lambda scan over 2^{-40}..2^{80} for
D = 4..128 gives at least 2.03 times the claimed lower bound in every row. The claim correctly says other bounded-M
representations of F_{D,w} are not excluded; the verdict covers exactly what is claimed.

### W-C71 (Cor 7.1): CONFIRMED
The identity is the entropy of the spectrum of Prop 4.1: 2^{c_i} block copies of mass 4^{-c_i} ghat^2, and
2^{d_v - 1} phi-sets of mass w_v/2^{d_v - 1} with log(2^{d_v-1}/w_v) = 2(d_v - 1) + 2 log(1/Delta_v). The bound uses
H+(g) <= H(g) <= C_reg D(g) <= C_reg I(g) (Theorem A; D(g) = sum min(Inf, 1 - Inf) <= I(g)), 2(d_v - 1) <= 2(d_v + 1),
2 Delta log(1/Delta) <= 2 log e/e, and (1-v) log(1/(1-v)) <= v log e; the total is C_reg + log e < 10.3797.
The identity matched the exact spectrum to 1e-9 on all 7,000 random instances. Novelty for FEI itself is unverified:
K_RO with constant leaves is a read-once decision tree (Wan-Wright-Wu give 9k with k = 1), and LTF leaves would need
an FEI+ composition input that the author did not find; the author labels it accordingly.

### W-T111 (Theorem 11.1) and Cor 11.2: GAP as written; CONFIRMED with the corrected statement (26.71 I)
Re-derived step by step.
- Spectrum: 1_{E_j} = prod_{k<j}(1 - tau_k) tau_j over disjoint blocks; (1-tau)^ = 1 - q at the empty set and -q sigma
  elsewhere; equal means kill every control-only set (fhat(T) = mu 1hat_cube(T) = 0); given j, the S_k are independent
  (empty w.p. 1 - q_k, else uniform nonempty), S_j uniform. The mass identity (1-q)^2 + (2^w - 1)q^2 = 1 - q holds.
- Owners: (j, t) with t_k >= M_k; sum of pi = P_j q_j prod_k P(t_k >= M_k), with P(t >= M) = 2^{1-M} - q >= 2^{-M}. No cap.
- Root: per unit mass <= w_j + log(1/P_j) + sum_k q_k(log e + w_k), then e_w >= max(1, w/2) and Claim A.
- Rank, rare blocks (the step that carries the theorem): rank(x) <= w_j + sum_{u before v} t_u + w_v; "u before v"
  implies d_u <= d_v; for u outside R, E[t_u 1(d_u <= d)] <= 2^{d+2} q_u w_u (both cases checked); E 2^{d_v} <=
  2^{w_v - M_v + 1}; t_u, t_v are independent under the owner law (it is a product law: weights 2^{-sum t} on a product
  of ranges), so E_w r(x) <= W_R + 2^{w_v - M_v + 3} Lambda_j; then concavity of log(1 + .), the split
  log(1 + a + b) <= log(1+a) + log(1+b), and log(1 + 2^c y) <= c + log(1 + y). (P1) uses Y <= X <= s and concavity
  of x log(1 + c/x) with E[X | j, R] >= W_R/2; (P2a) E[|S_v|(w_v - M_v)] <= w_v + 1 and w + 1 <= 4 e_w; (P2b) as (P1).
- Sum: coefficients 5.102 (I_true), 15.647 (I_rare), 4.932 (I_Y), plus 6.613 on all of I, plus 2 + 2.443 for h(v)
  and v; total 26.703.
Checks (step 5): exact truth tables of 2,326 lists (every coefficient and sign, the I split, the witness sum over all
owners with exact normalizers, each part under its bound, the per-set rare-rank and per-element mean-rank inequalities
on every set); the proof's per-set quantities computed exactly (convolution over the owner law, validated against brute
force to 3.6e-15) on lists of up to 513 blocks, including m = 2^w lists of width w up to 9 and mixed widths:
the Jensen-form code is 8.2-8.95 I; the per-element mean-rank bound is never exceeded (at most 0.90 of it).
Cor 11.2: the same argument with L_true in place of w_j; the product formula needs only distinct blocks along each
path, and recurring blocks on different paths do not matter because data blocks are fresh. Checked exactly on 1,500
term-test trees (219 test one block at two different nodes).

### W-P112 sub-steps (summary: "Also proved ... the root term for all sets of general term decision lists"): CONFIRMED
For a phi-set with top block K: fhat(T) = prod_{k<K} a_k(S_k) sigma(S_K) q_K (mu_K - m_{>K}), mass
w_K = P(reach K) q_K (1 - q_K) 4(P - rho)^2. Owners are the paths to K with t_k >= M_k (k < K) and the paths to J > K
that also have t_K >= M_K; their pi-sum is prod_{k<K} P(t_k >= M_k) [q_K P + P(t_K >= M_K) rho] >= ... q_K max(P, rho).
Inf of block K's variables = P(reach K) w_K q_K (1 - mu_K m_{>K}) >= 2 P(reach K) w_K q_K |P - rho|, which pays
(P - rho)^2 log(1/max(P, rho)) with constant 2 log e/e. Block-set ranks do not involve the means, so the 11.1
argument applies. The open piece (phi-set rank term with long continuations) is correctly reported as open.

### W-L120 (Lemma 12.0): CONFIRMED
b f = 2 sum_l 1_{C_l} - 1 pointwise, and |1hat_{C_l}(A)| = p_l if A is inside V_l, else 0. Exact check on every
nonzero coefficient of every function and partition tested in step 4: no failure.

### W-P121 (Prop 12.1): CONFIRMED
Gates 1_{C_l} are exclusive, M = 1, pi_l = p_l <= 1/2 (codimension >= 1 because f is nonconstant), Lambda <= log e.
Lemma 3.2 with Jensen over w_A (convexity of -log), Z_l <= (ea/(a-1))^s, and Lemma 12.0's
log(1/sum p_l) <= 1 + (1/2) log(1/fhat(A)^2) give H+ <= h(v) + v(log e + 2) + H+/2 + log2(3ea/(a-1)) I + aR; solving and
adding (1-v) log(1/(1-v)) <= v log e gives 8 + 3 log e + 2 log2(18e) = 23.553. Checked (step 4) on all functions with
n = 3, 5,500 random functions with n = 4, 5, and the COUNTEREXAMPLES witnesses X001, X002, X003 (reduced r), X004,
X005, X009 plus MAJ5, MAJ7, tribes, addressing, with four tree rules, both level sets and three orders: the per-set
intermediate inequality, the H+ chain and the final inequality never fail.

### W-P123 (mixture of orders): CONFIRMED
Copies (l, c) with root odds p_l gamma_{l,c} keep the law a subprobability and keep Lambda <= log e
(sum_c gamma = 1); keeping only the best copy per cell in Lemma 3.2 and putting log(1/gamma) inside the Jensen average
reproduces 12.1 with R_mix. Single-root c = 0 witnesses never use d(j), so duplicated gates cost nothing else.
Checked with two copies (path, reversed; gamma = 1/2) alongside 12.1: no failure.

## Literature, counterexamples, replication
- Wan-Wright-Wu, arXiv:1312.3003 (read 12 Oct 2026): abstract gives H <= 9k Inf for read-k decision trees and
  H <= 12 d Inf for expected depth d with Inf >= 1; Lemma 1.7 reads "The length of the above protocol is
  4 Inf[f] + 2 Cov[T]"; Figure 2 is the bad tree with dummy levels and the text says the protocol outputs 2l extraneous
  characters. The author's description of this prior art is accurate. I did not search further for the half-entropy
  root bound; its novelty stays unverified, as the author says.
- COUNTEREXAMPLES: X001-X003, X009 are not regular-leaf instances of K and do not touch Theorems 5.1/11.1; the author's
  X011 placement (rare activation with a regular core is in K_RO) is right. Prop 12.1 is universal, so I ran it on
  X001, X002, X003 (r = 4), X004, X005 and X009: it holds. X004/X005 (shared supports) are excluded from K by (DS), as
  the author states.
- Replication of the exact values behind the candidate obstruction (W-E3/W-E5): AND-OR tree, short-circuit cells of
  f = 1, path order: R_path/I = 0.2500, 0.4896, 0.6436, 0.9668 and H/I = 2.000, 2.217, 3.613, 3.684 for depth 1..4
  (author: 0.250, 0.490, 0.644, 0.967). This checks the author's exact validation, not the large-depth Monte Carlo.

## Files (referee_code/)
rc_common.py (exact integer Walsh transform, e_s), rc_trees.py (class K generators), check_K.py (Prop 4.1, Cor 7.1,
Thm 5.1, step bounds), neg_controls_K.py, check_elementary.py (Claim A and the other elementary inequalities,
exhaustive n <= 4), check_N61.py (Prop 6.1), check_P121.py (Lemma 12.0, Prop 12.1, P123), check_TDL.py (Thm 11.1 exact),
check_TDL_large.py + validate_dp.py (Thm 11.1 per-set quantities on large lists), check_TTT.py (Cor 11.2),
sim_queue.py (Lemma 3.2 against the simulated process), check_andor.py (exact AND-OR replication).
Commands: python check_K.py 21 4000 ro; python check_K.py 22 3000 em; python neg_controls_K.py;
python check_elementary.py; python check_N61.py; python check_P121.py exhaustive 3; python check_P121.py sample 4 4000 280;
python check_P121.py sample 5 1500 280; python check_P121.py families; python check_TDL.py 2 2000 280 4 3 16;
python check_TDL.py 3 400 280 7 5 19; python validate_dp.py; python check_TDL_large.py TD1_3,TD1_5,TD1_7,TD1_9,ALT_5,GEO_6,RND_1,RND_2 600 1;
python check_TDL_large.py NW_4,NW_5,NW_6,WN_5,WN_7,NW_7 300 2; python check_TTT.py 5 1500 330; python sim_queue.py;
python check_andor.py. Each run stays under 10 minutes and well under 2 GB, single process.

## Running log

### Step 1 (analytic re-derivation, before any code)

Notation slip found in the STATEMENTS of W-T51 and W-T111 (and Cor 11.2): the middle expression is written
h(v) + v*Lambda_1 + sum_A fhat(A)^2 log(1/Q_{1,1}(A)), with Q_{1,1}(A) the true run probability (section 1 of NOTES:
"Q_{1,lambda}(A) = probability of a successful finite run with output A"). That probability already carries the root
normalizer 2^{-Lambda} (Lemma 3.2; and in both proofs the first line is log(1/Q(A)) <= Lambda_1 + ...). So v*Lambda_1 is
counted twice. The proofs bound h(v) + sum_A p(A) log(1/Q(A)) (Lambda counted once, through the v*log e term).
Confirmed later that the author's code (queue_cost.py) does the accounting correctly; only the statements are off.

### Step 2 (own code, class K; referee_code/check_K.py, neg_controls_K.py, check_elementary.py)

- check_K.py builds random trees, takes the exact integer Walsh transform of the full truth table (n <= 17) and checks
  every nonzero coefficient against Prop 4.1 (i)-(iii) in exact Fractions (value AND sign), the total block and phi
  masses (completeness), the influence formula (iv) for every control variable, the decomposition (v) of I and I_X,
  and the exact entropy identity of Cor 7.1. It then computes the Theorem 5.1 code with the single-root witness-sum
  lower bound Q_lb(A) <= Q(A) of Lemma 3.2 (exact elementary symmetric normalizers, not the proof's bound on Z), and
  each averaged part of the proof against the bound the proof states for it (steps (a)-(d)).
- Negative controls (neg_controls_K.py, 60 read-once trees): dropping the sign in (i) trips 59/60, writing m_+ + m_- in
  (iii) trips 57/60, writing (1 + m_+ m_-)/2 in (iv) trips 56/60, the correct formulas trip 0/60. A first run also
  tripped by itself on an instance whose leaves I had wrongly built with unequal means (phi-sets appeared, as they must).
- Results: 4,000 read-once instances (2,455 with phi-sets) + 3,000 equal-mean general trees (labels repeated across
  paths): 0 spectral failures; max H/I = 3.68; max code_lb/I = 6.37 (read-once), 5.01 (equal means); max of the
  literal (double-counted) expression (code_lb + v Lambda_1)/I = 6.49; Gibbs (H <= code_lb) holds everywhere.
  No step bound is exceeded. Tightness (max part/bound): (a) 0.83, (b) 0.9999, (c) 0.49, (d) 0.25.
  Step (b) is sharp, not violated: for one node x_0 ? g : -1 with E g = -1 + 2/e, every inequality of step (b) is
  an equality (Delta = 1/e, m_- = -1, so log(1/sum pi) = d + log(1/Delta), Inf = P(reach) Delta, Delta log(1/Delta) = log e/e).
- check_elementary.py, exhaustive over all 65,804 nonconstant Boolean functions with n <= 4: Claim A holds (max ratio
  0.9375); h(v) <= 2I + (log e - 2)v holds; s(s+1) <= 3^s, (c+1)(c+2) <= 2*3^c; the two Jensen bounds on psi hold
  (exact binomial sums, c, d <= 200, max ratios 0.996 and 0.989); x log(1/x) <= log e/e; 1 - ab >= |a - b|.

### Step 3 (own code, Prop 6.1; referee_code/check_N61.py)

- Exact truth tables of F_{D,w} for (D,w) = (1,2), (1,3), (2,2), (1,4) (n up to 23): the only control-only Fourier set
  is {x_0}, its mass is exactly (1-2delta)^2, v = 1, and I(F) equals the stated formula exactly.
- For D = 4 ... 128 (w = max(2, ceil(log2 D))) and every lambda on the grid 2^{k/8}, k = -320..639: the proof's own
  lower bound (exact Z_1 in the cost of {x_0}; t >= 1 branch as in the corrected self-audit) is at least 2.03 times the
  claimed (1-2delta)^2 (D/2+2) in every row; same for the complemented representation; the scale-mixture bracket for
  {x_0} (Lambda_lambda + C_lambda, log(1/w_j) >= 0 only adds) also clears it. LB/I grows linearly: 0.93 (D=4) ... 42.2
  (D=128), with I(F) <= 3.29 in all rows.
- Witness-sum cost of {x_0} with all 2^{D+1} single-root witnesses (exact Z_1): 5.19, 5.34, 5.51, 5.76, 5.94, 6.20,
  6.37, 6.49 bits at D = 1, 2, 4, 8, 16, 64, 256, 960, increasing to the limit 0.7213 + 3 + log2(2 zeta(6/5)) = 7.205 < 7.21.

### Step 4 (own code, Lemma 12.0 / Prop 12.1 / P123; referee_code/check_P121.py)

- For each f: decision trees by four variable-choice rules (first / last / random / greedy relevant variable), both
  level sets, three orders per cell (path, reversed, random); P123 with two copies (path, reversed), gamma = 1/2.
  Checked: Lemma 12.0 in exact Fractions for every nonzero set; Gibbs with the witness-sum Q_lb; the per-set
  intermediate inequality of the proof (log 1/Q_lb(A) <= Lambda + 1 + (1/2)log(1/p(A)) + log(s(s+1)) + 1 + s log(ea/(a-1))
  + a E_w[rank]) and its mixture version; the H+ chain; the final H <= 23.55 I + 2.4 R and H <= 23.55 I + 2.4 R_mix.
- Exhaustive n = 3 (all 256 functions, 4,572 runs), random n = 4 (4,000 functions incl. rare level sets, 38,592 runs),
  random n = 5 (1,500 functions, 16,092 runs), and the COUNTEREXAMPLES witnesses that fit: X001 parity lifts of six
  random g on 4 bits, X002 splices m = 3, 5, X003 activation (k = 4, r = 4: r reduced from 2k for table size), X004 zy,
  X005 g(z)y (three g), X009 bent splice m = 4, plus MAJ5, MAJ7, tribes 2x3, addressing a = 2.
  Zero failures of every check. Largest per-set slack used: cost - bound <= -3.0 bits; max code/I = 6.39; max R/I = 0.86.

### Step 5 (own code, Theorem 11.1 / Cor 11.2; referee_code/check_TDL.py, check_TDL_large.py, validate_dp.py, check_TTT.py)

- check_TDL.py, exact small lists (truth tables n <= 19; 2,000 lists with m <= 4, widths <= 3, and 326 with m <= 7,
  widths <= 5; equal-mean outputs: dictators/majority, AND_2, OR_2, and mixed AND_2 / 2y1+y2+y3+y4 >= 3): every nonzero
  coefficient equals the product formula of section 11 exactly (sign included), I = I_true + I_rare + I_Y exactly,
  no phi-sets; witness sum over ALL owner gates with exact Z; Gibbs holds; max code/I = 5.96 (max literal
  (code + v Lambda)/I = 6.18) against 26.71. Each averaged part is under the proof's bound for it (root 0.75 of its
  bound, rank 0.10, size+normalizer 0.45). Per-set: the rare-rank inequality of step (5) and the per-element mean-rank
  bound E_w r(x) <= W_R + 2^{w_v-M_v+3} Lambda_j hold on every set. These small lists cannot stress the rank steps.
- check_TDL_large.py: the proof's own per-set quantities computed EXACTLY for each set (owner law of t_u independent,
  2^-t on [max(M,1), w]; deficit order with ties to earlier blocks; distribution of the prefix sum by convolution),
  sets sampled from the exact spectral law (300-600 per family). validate_dp.py checks the convolution against brute
  force over all owner gates: 231 configurations, max difference 3.6e-15.
  Families: m = 2^w lists of width w (w = 3, 5, 7, 9; m up to 512), alternating widths 1/W, geometric width mix,
  random widths 1..10 (m up to 300), narrow-then-wide (2 then 4*2^W blocks of width W, m up to 513), wide-then-narrow.
  Jensen-form code J/I = 8.22 ... 8.95 everywhere (proved bound 26.71); root/I <= 1.87 (its bound 2.38-2.61);
  rank/I <= 0.55; no per-element or per-set violation; per-element mean rank used at most 0.90 of its bound.
- check_TTT.py, Cor 11.2, exact term-test trees (1,500 trees; 219 test the same block at two different nodes):
  product formula exact for every coefficient, I split exact, Gibbs holds, max code/I = 5.51, root part <= 0.75 of
  its bound.

### Step 6 (own code, Lemma 3.2 against the actual random process; referee_code/sim_queue.py)

- 120,000 simulated runs of the paper's queue law (roots, s ~ 1/(s(s+1)), theta-weighted s-subsets, c ~ 1/((c+1)(c+2)),
  uniform multisets, uniform child gate among the d(j) gates) on three OVERLAPPING gates with M up to 2 inner orders.
  The frequency of the event E_l = {roots = {l}, s = |A|, B = A, c = 0} matches rho_l 2^-Lambda/(s(s+1)) prod theta/Z/2
  within 2.3 standard errors over all (A, l); the empirical Q(A) never falls below the witness-sum bound beyond noise
  (max (Q_lb - Qhat)/s.e. = 0.79).

### Step 7 (literature and replication)

- Wan-Wright-Wu arXiv:1312.3003 read (abstract, Theorem 1.6, Lemma 1.7, Figure 2): matches the author's description.
- check_andor.py: exact AND-OR depth 1..4 values replicate the author's exact validation numbers (section above).
