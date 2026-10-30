# FEI campaign in the brain

Written by fei_brain_ingest.py (claude-51330238). Sources: brain_workers/FEI100_20261011 (the Codex fleet and the Opus stream leads of claude-2d8060eb) and fei_opus_2026_10_11 (the supplementary Opus workflow). Full FEI stays OPEN unless a complete proof passes the campaign's B18/B19 reviews and B20 synthesis; a status below is its author's own label until a referee confirms it.

## Counts

- files carried: 21317; left on this computer (binary or over 2 MB): 1293
- fleet runs with a REPORT.md (finished or in progress): 506; claims recorded: 1119

## Claims by status

### PROVED (85)
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse]
-   [fleet/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse]
-   [fleet/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse]
-   [fleet/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse]
-   [fleet/claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion]
-   [fleet/claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion]
-   [fleet/claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion]
-   [fleet/claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion]
-   [fleet/claude/B07/runs/20261011T230024Z-claude-B07-two-address-census]
-   [fleet/claude/B07/runs/20261011T230024Z-claude-B07-two-address-census]
-   [fleet/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring]
-   [fleet/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring]
-   [fleet/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring]
-   [fleet/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring]
-   [fleet/claude/B12/runs/20261011T225832Z-claude-B12-erasure-ledger-depth]
-   [fleet/claude/B12/runs/20261011T225832Z-claude-B12-erasure-ledger-depth]
-   [fleet/claude/B12/runs/20261011T225832Z-claude-B12-erasure-ledger-depth]
-   [fleet/claude/B16/runs/20261011T225600Z-claude-B16-retained-kl-sandwich]
-   [fleet/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge]
-   [fleet/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge]
-   [fleet/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]
-   [fleet/claude/B19/runs/20261011T224700Z-claude-B19-paper-audit-rankcode]
-   [fleet/claude/B19/runs/20261011T224700Z-claude-B19-paper-audit-rankcode]
-   [fleet/claude/B20/runs/20261011T225100Z-claude-B20-erasure-activation-transfer]
-   [fleet/claude/B20/runs/20261011T225100Z-claude-B20-erasure-activation-transfer]
-   [fleet/claude/B20/runs/20261011T225100Z-claude-B20-erasure-activation-transfer]
-   [fleet/claude/B20/runs/20261011T225100Z-claude-B20-erasure-activation-transfer]
- For a row g_T(x) = E_y[f(y,x) chi_T(y)] (|A| = 2) whose normalized squared Walsh law is product: g_T = chi_{D1} phi(x_R) with phi full-support on R (r = |R|); |phihat(U)| = kappa prod_{i in U xor U*} p_i/q_i (coprime p_i >= q_i >= 1); nu = 2^{r+1} kappa is an integer divisible by prod q_i; with nu' = nu / prod q_i: w_T = nu'^2 4^{-(r+1)} prod_i (p_i^2+q_i^2) and log2(1/w_T) + H(q_T) = 2 - 2 log2 n  [opus/A2-two-addresses]
- Lemma 3 for k spectral addresses: rows take values in 2^{1-k} Z, the minimal Walsh coefficient of a product row is nu 2^{1-k-r} with prod q_i | nu, w_T = nu'^2 4^{1-k-r} prod (p_i^2+q_i^2) and log2(1/w_T) + H(q_T) = 2(k-1) - 2 log2 nu' + sum_i Ft(p_i,q_i), nu' = nu/prod q_i.  [opus/A2-two-addresses]
- Every f in K2 satisfies H(f) <= 4 I(f).  [opus/A2-two-addresses]
- Every f in K2 satisfies H(f) <= c* I(f) with c* = 16/3 - (3/2) log2 3 = 2.9558895822...; equality for the 3-variable AND (f = -1 iff y1 = y2 = x = -1, H = 4 - (9/8) log2 3, I = 3/4). Hence the optimal constant on K2 is c*, refuting any constant below c* (in particular 2 and 40/17).  [opus/A2-two-addresses]
- Signed-character selectors with any number of address coordinates: if f(y,x) = s(x) chi_{tau(x)}(y) and every row s 1_{tau = T} has a product squared Walsh law, then H(f) <= 4 (I(f) - Inf_y(f)) <= 4 I(f); the constant 4 is sharp (addressing functions y_x: H = 2a, I = 1 + a/2).  [opus/A2-two-addresses]
- Let C_k be the optimal constant for Boolean f with an address set of size <= k and all conditional laws product. C_k is nondecreasing, K_k contains every Boolean function on k+1 variables (a law on one bit is product), hence sup_k C_k = C_FEI. C_0 = C_1 = 2 (known), C_2 = 16/3 - (3/2) log2 3 = H/I(AND_3) (A2-T-S).  [opus/A2-two-addresses]
- For any f = 2T-1, any product law and any linear order of coordinates: E_mu(f) = sum_i sigma_i^2 [rho_i^2 ln(1/rho_i^2) + sum_{nonempty B subset U_i} phi_{sigma_B^2}(ehat_i(B)^2)] and Delta_mu(f) = sum_i sigma_i^2 I_mu(e_i), e_i = E[d_i | y_{U_i}].  [opus/BT-biased-thresholds]
- For increasing T with alpha = mu(T=1): ln(1/alpha) = sum_i c_i ln(1/q_i) - DTC(mu_A), c_i = q_i rho_i/alpha, hence alpha ln(1/alpha) <= sum_i q_i ln(1/q_i) rho_i. (The p-biased inequality is the classical biased edge-isoperimetric inequality, KNOWN; the identity is an elementary entropy proof.)  [opus/BT-biased-thresholds]
- Antichains in a product law with marginals r_j have measure <= (2 sum_j min(r_j,1-r_j))^{-1/2}; for regular monotone T, E_{nu_i} ln^+(Lambda_i/(|B cap U_i|+1)) <= 3 + ln 4, Lambda_i = sum_{j<i} sigma_j^2.  [opus/BT-biased-thresholds]
- For every regular monotone T (every weighted threshold) and every product law with 0 < q_i < 1: E_mu(f) <= Var(f) ln(1/Var(f)) + A_0 I_mu(f), A_0 = 2 + ln 7 + (6/5)(3 + ln 4) < 9.21 nats.  [opus/BT-biased-thresholds]
- Corrected FEI+ under a bias floor: for 0 < delta <= 1/2, every regular monotone T (every weighted threshold) and every product law with all q_i in [delta, 1-delta], H_mu^+(f) <= (2 K_delta/ln 2) Delta_mu(f), K_delta = max(2 A_delta/(delta(1-delta)), 8 A_delta + 18.5), A_delta = A_0 + max(1.661, ln(1/delta)/(1-delta)); constant O(delta^{-1} log(e/delta)), uniform in arity and weights.  [opus/BT-biased-thresholds]
- A096 stage 2 (H2 <= 3.0484 I, B_1 <= 7.540 I) confirmed by an independent referee pass; superseded as a constant by L2-T3 (B_1 <= 3.5777 I).  [opus/L2-level-two]
- B13's sandwich G <= B <= G + log(e) I re-derived; Lemma 1 summed with a_{j,i} is the same bound pushed forward to levels (data processing). J_i <= B_i taken from B13, not re-derived.  [opus/L2-level-two]
- For every multiplexer with a fresh uniform selector block and arbitrary Boolean branches on a common data cube: cost(F) = H(S|T) + I(X;Y) and cost(F) <= sum_i h(pi_i) + min{ sum_i h(pi_i), (2/ln2) I_sel } <= a min{2h(I_sel/a), h(I_sel/a) + (2/ln2) I_sel/a}.  [opus/SEL-selector-interference]
- If I_sel(F) >= c a (0 < c <= 1) and H(g_b) <= C I(g_b) for all branches, then H(F) <= max{C, K(c)} I(F) with K(c) = min{2h(c)/c, h(c)/c + 2/ln2}. K(1/2) = 4 (C035), K(c) < 2/c for c != 1/2, K(c) = log2(1/c) + log2 e + 2/ln2 + o(1) as c -> 0 (K(0.1) = 7.575, K(0.01) = 10.965).  [opus/SEL-selector-interference]
- For the bent point-flip multiplexer F_m = Mux_z(b, b - 2*1_{t=0}) on m+1 bits (m even), delta = Inf_z = 2^-m and cost(F_m) = delta(log2(1/delta) + 3/ln2) + O(m delta^2) (exact closed forms in NOTES). Products of a independent copies attain the SEL-1 bound asymptotically for every a. Hence no inequality cost(F) <= K I_sel(F) with an absolute K holds.  [opus/SEL-selector-interference]
- Let Kopt(c) be the sup of H/I over one-node fresh-selector multiplexers with I_sel >= c a and branches of zero entropy. Then sup{H(g)/I(g): I(g) >= 2c n(g)} <= Kopt(c) <= K(c) for 0 < c <= 1/2, and sup_{c>0} Kopt(c) = C_FEI. An energy-uniform closure constant that stays bounded as c -> 0 is equivalent to full FEI.  [opus/SEL-selector-interference]
- If selector coordinates may occur in the branches and orthogonality is imposed on the branches as functions of all variables, then every Boolean f on n bits is a single node: f(x) = B_x(x) with B_b = f(b)(-1)^{|S_b|} chi_{S_b}, S_b = {i: b_i = -1}; the branches are pairwise orthogonal signed characters (H = 0). Also every f is a recursive one-bit orthogonal multiplexer with character leaves via F   [opus/SEL-selector-interference]
- The orthogonal-neighbour closure constant max(4, C_leaf) fails under reuse: g(x0..x3) = x2 if x2 = x3, x0 if (x2,x3) = (1,-1), x1 if (x2,x3) = (-1,1) is balanced with H(g) = 3, I(g) = 3/2 (exact), and G = g o (g o g) on 64 variables has H(G) = 57/4 > 4 I(G) = 27/2, H/I = 38/9, by the balanced composition identities H(f o g) = H(f) + I(f)H(g), I(f o g) = I(f)I(g).  [opus/SEL-selector-interference]
- With orthogonality and branch FEI hypotheses imposed on the effective branches g_b restricted to x = b, a reuse node is exactly a fresh-selector node with those branches, so C035 applies verbatim.  [opus/SEL-selector-interference]
- For any partition of the selector cube and pairwise orthogonal Boolean leaves (overlapping Fourier supports allowed): S-marginal of Fhat^2 is sum_k ahat_k^2, T-marginal is sum_k p_k Ghat_k^2, H(F) <= 2H(p) + sum_k p_k [H(q_k) + H(G_k)], I_sel = (1/4) sum_k I(h_k). If H(h_k) <= C_s I(h_k) and H(G_k) <= C_g I(G_k) then H(F) <= max{C_s + 6, C_g} I(F); strong form max{max(C_s,4) + 2, C_g}(I(F) - 1) fo  [opus/SEL-selector-interference]
- Balanced two-cell selectors with orthogonal leaves: for balanced h on the selector cube and Boolean G_1 orthogonal to G_2 on a common data cube (shared variables and overlapping Fourier supports allowed), F = ((1+h)/2)G_1 + ((1-h)/2)G_2 satisfies H(F) <= 2 + H(h)/2 + (H(G_1)+H(G_2))/2 and I(F) = I(h)/2 + (I(G_1)+I(G_2))/2. Corollary (SEL-15c): for C >= 4, the smallest class containing a base class  [opus/SEL-selector-interference]
- For any partition and any Boolean (or real unit) leaves, with independent uniform signs eps_k: E_eps H(sum_k eps_k a_k G_k) <= H(p) + sum_k p_k [H(q_k) + H(G_k)], E_eps I_sel = D = (1/4) sum_k I(h_k). Hence some re-signing of the leaves satisfies H <= max{C_s + 4, C_g} I whenever cells and leaves are FEI-good: all interference losses in this report are sign-alignment effects.  [opus/SEL-selector-interference]
- Joint-strategy candidate C1 holds: for every partition of F_2^a into affine subspaces (codims c_j, p_j = 2^-c_j) and real leaves g_j with E g_j^2 = l_j, sum p_j l_j = 1, w_j = p_j l_j, Lambda_j = ghat_j^2/l_j: H(Fhat^2) <= H(w) + sum_j w_j c_j + sum_j w_j H(Lambda_j). For Boolean leaves: H(F) <= 2 sum_j p_j c_j + sum_j p_j H(g_j). Proof by tensor powers and the AEP (the method of Arunachalam-Chakr  [opus/SEL-selector-interference]
- Joint-strategy C2 made unconditional: affine partition of a fresh selector block, Boolean leaves with <g_j, g_l> <= 1 - delta for adjacent distinct cells: I_sel >= (delta/2) sum p_j r_j and H(F) <= max{4/delta, C} I(F) (strong: max{4/delta, C_g}(I(F)-1) for balanced leaves). The recursive class (fresh blocks, affine cells, copies inside cells, shared data, regular base leaves) satisfies H <= max{4  [opus/SEL-selector-interference]
- Reverse uncertainty: for a real function Psi constant on the cells of an affine partition of F_2^a with E Psi^2 = 1, cell weights w_j = p_j v_j^2 and point law r = Psi^2/N: H(Psihat^2) + H(r) <= a + 2H(w) (Maassen-Uffink gives >= a).  [opus/SEL-selector-interference]
- (a) Recursive fresh-selector multiplexers whose every node has energy fraction >= c, from leaves with H <= C_leaf I, satisfy H <= max{C_leaf, K(c)} I. (b) For cells given by a coordinate decision tree with adjacent-cell leaf correlation <= 1 - delta: cost(F) <= K(delta/2) I_sel(F), so H(F) <= max{C, K(delta/2)} I(F), K(delta/2) = log2(1/delta) + O(1) (K(1/2) = 4 at delta = 1).  [opus/SEL-selector-interference]
- Constant sandwich: with C_FEI = sup H/I, K_E = sup B/I, K_L = sup L/I, K_loc = sup_f min_{i:Inf_i>0} B_i/Inf_i, K_Delta = sup_f min_i Delta_i H/Inf_i: K_loc <= K_E <= C_FEI <= K_Delta <= K_loc + 2/ln2 and K_L <= K_E <= K_L + log2 e.  [opus/U-universal]
- Profile of an extremizer of c_n = max H/I on n bits: ratio-critical; all Inf_i <= 1/2; Delta_i H >= c Inf_i and B_i >= (c-2/ln2) Inf_i for every i; DTC <= sum_i JS_i <= (2/ln2) J; H(S_A|S_{A^c}) >= (c-2/ln2) I_A for every block; Inf_i <= Var 2^{6.0782-c}; deg f >= 1 + cI/2; random-order erasure profile (c-2/ln2) I <= beta(t) <= (c-2/ln2) I + (2/ln2) I/t; random restrictions at density t have expec  [opus/U-universal]
- FEI holds iff there is A < infinity with H(f) <= A (I(f) + DTC(f)) for all Boolean f (DTC = H - B, dual total correlation of the spectral sample).  [opus/U-universal]
- FEI iff there is K such that every ratio-critical f with all Inf_i <= 1/2 has a coordinate with H(S_i|S_{-i}) <= K Inf_i.  [opus/U-universal]
- C019's stopping-tree hypothesis and C024's linear path-cost payment are each FEI-equivalent (constants shift by at most 2/ln2 resp. 3 and 1 nat units); their local form is (LDI).  [opus/U-universal]
- Meta-obstruction: Slote (arXiv:2608.01424) gives quantum Boolean functions (Hermitian unitaries) of Pauli degree d with exp(Theta(d^2)) equal-magnitude Pauli terms, so H/I = Theta(d). Hence any argument whose steps all remain valid for quantum Boolean functions (Parseval, hypercontractivity, LSI, KKL/Talagrand/Friedgut-type estimates, operator Booleanity A^2 = I) cannot prove FEI or any bound H <=  [opus/U-universal]
- For every Boolean f and nonempty S: |fhat(S)| <= 2^{|S|-1} I_S(f), where I_S(f) = sum_{T superset of S} fhat(T)^2 = E[(d_S f)^2]; equivalently p_S <= 4^{|S|-1} pi(S)^2. (d_S f takes values in 2^{1-|S|} Z because it is 2^{-|S|} times a sum of 2^{|S|} signs.)  [opus/U-universal]
- Theorem G: for every Boolean f, H(f) <= 2(I(f) - Var(f)) + 2 U(f) - (1-Var) log2(1/(1-Var)) <= 2 I(f) + 2 U(f), where U(f) = sum_S p_S log2(pi(S)/p_S) and pi(S) = sum_{T superset of S} p_T. Also U <= H, so FEI holds iff sup U/I < infinity, with C_FEI <= 2 + 2 sup(U/I) and sup(U/I) >= (6.4548-2)/2 by Hod.  [opus/U-universal]
- Level-only universal bounds: H <= 2(I-Var) + 2H(W) + 2 sum_{k>=1} W_k log2 E[binom(|S|,k)] (W_k = P(|S| = k); equal to Theorem G for symmetric functions); and, tensor-stable, H <= 2(I-Var) + 2 inf_{lambda>0} [log2 E(1+lambda)^{|S|} - I log2 lambda] (lambda = 1: H <= 2I + 2 log2 E 2^{|S|}).  [opus/U-universal]
- For read-once compositions f = g(h_1..h_k) with independent inner functions: U(f) = U(P_g^mu) + sum_j P(j in J) U(q_j), parallel to H(f) = H(P_g^mu) + sum_j P(j in J) H(q_j), I(f) = sum_j P(j in J) E_{q_j}|T|.  [opus/U-universal]
- Exact restriction identity: Delta_i U = sum_{T not containing i} m_T [ s_T log2(r_T/s_T) + (1-s_T) log2(1/(1-s_T)) + D2((1+eta_T)/2 || (1+x_T)/2) ], with m_T = fhat(T)^2 + fhat(T+i)^2, s_T = fhat(T+i)^2/m_T, r_T = pi(T+i)/pi(T), eta_T and x_T the restriction asymmetries of the T-coefficient and of the T-upper-set mass. Equivalently Delta_i U = B_i - Gamma_i + K_i with K_i = U(law of S minus i) - a  [opus/U-universal]
- If for all Boolean f, sum_i Delta_i U(f) <= a I(f) + b U(f) with b < 1, then U <= (a/(1-b)) I and H <= (2 + 2a/(1-b)) I for all f.  [opus/U-universal]
- Random-restriction entropy inequality: for every Boolean f and t in (0,1], H(f) <= (1/t) E[H(f_{J,X})] + (2/ln2)((1-t)/t) I(f), with J a Binomial(t) live set and X uniform on its complement; more precisely the deficit c I - H is a supermartingale up to (2/ln2)(1-t) I under random restriction.  [opus/U-universal]
- If f = OR of gates h_l that are mutually exclusive (at most one true at each input), then fhat(A) = sum_l hhat_l(A) for every nonempty A; hence every nonempty Fourier set of f lies inside the relevant set R_l of a single gate.  [opus/W-witness-cost]
- For the paper's queue law with any root odds rho_l > 0 (paper: rho_l = lambda*pi_l), Q(A) >= 2^{-Lambda} * sum over gates l with A subset R_l of rho_l * [1/(s(s+1))] * [prod_{j in A} theta^l_s(j)/Z^l_s] * 1/2, s=|A|: distinct single-root witnesses are disjoint runs and their probabilities add.  [opus/W-witness-cost]
- Exact spectrum of selector trees f(x,y)=g_{leaf(x)}(y) with regular leaves on disjoint data blocks: block sets T u B (B nonempty in supp g_i, T subset path(i)) have fhat = 2^{-c_i} sigma(T) ghat_i(B); for read-once control trees the sets inside the control coordinates are exactly S u {v}, S subset anc(v), with |fhat| = 2^{-d_v}|m_+(v)-m_-(v)|; Inf_{x(v)}(f) = P(reach v)(1 - m_+ m_-)/2; I(f) = sum_  [opus/W-witness-cost]
- Let K be the class of selector trees with regular leaves on pairwise disjoint fresh data blocks, where either all leaf means are equal (any decision tree; contains addressing C009 and every subcube selector with balanced regular leaves) or the control tree is read-once (arbitrary leaf biases; contains decision lists x1?g1:(x2?g2:...) with regular outputs). With gates h_i = [x in C_i] AND [g_i = 1]  [opus/W-witness-cost]
- The minimum-witness variational bound (W) of Prop. joint-witness (C008) is not linear in I on the read-once part of K: for F_{D,w} (root x_0; plus side complete read-once depth-D tree with OR_w leaves, minus side with AND_w leaves, fresh blocks), for every lambda > 0 and D >= 4, RHS(W) >= (1-2*2^{-w})^2 (D/2 + 2) (the large-lambda case handled separately: the root normalizer 2^D log(1+t) dominates  [opus/W-witness-cost]
- Direct spectral FEI on K: H(f) <= (C_reg + log2 e) I(f) < 10.38 I(f) for every f in K.  [opus/W-witness-cost]
- Term decision lists f = tau_1 ? g_1 : (tau_2 ? g_2 : ... : g_{m+1}) with read-once terms (conjunctions of fresh disjoint blocks of arbitrary widths w_k >= 1, arbitrary length m) and regular outputs on fresh blocks with one common mean mu in (-1,1): with the unfolded-path gates h_{j,t} = [x in C_{j,t}] AND [g_j = 1] and the 'deficit order' inside each gate (true block first, then the false prefixes  [opus/W-witness-cost]
- Owner mass lemma: if f^{-1}(b) is partitioned into subcubes C_l with fixed-coordinate sets V_l and probabilities p_l, then |fhat(A)| <= 2 sum_{l: A subset V_l} p_l for every nonempty A.  [opus/W-witness-cost]
- Reduction to the rank term: for every nonconstant f, every subcube partition {C_l} of a level set f^{-1}(b) (e.g. the b-leaves of any decision tree) and every choice of orders r_l, the paper's queue law over the gates 1_{C_l} gives H(f) <= [8 + 3 log2 e + 2 log2(3ea/(a-1))] I(f) + 2a R(f) (= 23.55 I + 2.4 R at a = 6/5), where R(f) = sum_A fhat(A)^2 E_{l ~ w_A}[sum_{x in A} log2+(r_l(x)/|A|)] and w  [opus/W-witness-cost]
- Mixture-of-orders refinement of W-P121: giving each cell C_l copies (l,c) with orders r_{l,c} and gate-dependent root odds p_l*gamma_{l,c} (sum_c gamma_{l,c} = 1) yields H(f) <= 23.55 I(f) + 2a R_mix(f), R_mix = sum_A fhat(A)^2 E_{l ~ w_A}[min_c((1/a) log2(1/gamma_{l,c}) + sum_{x in A} log2+(r_{l,c}(x)/|A|))]. This repairs the block-structure loss of a single order per cell (one bit instead of log  [opus/W-witness-cost]

### REFUTED (5)
- Attempted shortcut: a single Lagrange multiplier on sum w_T = 1 with per-row suprema certifies H <= c* I in the E_*-empty scenario. It does not: the bound is +0.0218 (tiny rows exploit free weights); a direct heavy-row argument (Section 5.2) is needed.  [opus/A2-two-addresses]
- Attempted shortcut: in scenario B one may keep only the weights of even-class rows (dropping their unfair-coordinate and nu' structure). The resulting bound is +0.0295 (the Gibbs gap 2 delta log2(1+2^{-c/delta})) for every rho >= 3, so it cannot certify c*; the envelopes of Section 5.4 are required.  [opus/A2-two-addresses]
- There is an absolute C such that V ln(1/V) <= sum_i I_i ln^+(4 rho_i/V) + C I for every weighted threshold under every product law (the extension of the paper's Lemma bias:credit).  [opus/BT-biased-thresholds]
- alpha * TC(mu_A) <= C I for the minority event A of every weighted threshold under every product law (the extension of paper eq. bias:eq-4-5).  [opus/BT-biased-thresholds]
- T1-sharp: for pairwise orthogonal leaves H(F) <= H(p) + sum_k p_k [H(q_k) + H(G_k)] (C010 identity as an upper bound). False for real orthonormal leaves (3-variable example, excess 0.0307 bits) and for Boolean leaves: selector of 9 bits, A_2 = one point, A_1 = rest, G_2 = 1 - 2*1[y=(+1,+1,-1,+1)], G_1 = -y_2 (1 - 2*1[y=(+1,-1,+1,-1)]) (orthogonal, all 16 Fourier sets shared): excess in [1.40285500  [opus/SEL-selector-interference]

### KNOWN (4)
- The target inequality is Conjecture 1 (FEI+ for product distributions) of O'Donnell-Tan, arXiv:1304.1347, restricted to weighted thresholds; their Theorem 2 proves it for every gate of arity k with factor 2^{O(k)}, and Theorem 1 gives constant-preserving composition.  [opus/BT-biased-thresholds]
- Copy-or-orthogonal nodes with arbitrary cells are FEI-complete (two-cell selector M_g with orthogonal dictator leaves; paper 'Unrestricted selectors', ledger C012); copy-or-anticopy point cells are FEI-complete (signed dictator, X005/C014). These fix the boundary of SEL-7 and SEL-10.  [opus/SEL-selector-interference]
- Tensor reformulation: if H <= C I + Psi with Psi(f^{(x)t})/t -> 0 (e.g. o(n), o(deg), o(I)), then H <= C I; same for B and L.  [opus/U-universal]
- Best universal bounds in the literature: H <= sum_i h(Inf_i) (Keller-Mossel-Schlank arXiv:1105.2651; Han arXiv:2312.08271); H[f^{<=D}] <= K sum_{|S|<=D} |S| log(|S|+1) fhat(S)^2 + K I (Kelman-Kindler-Lifshitz-Minzer-Safra arXiv:1911.10579v2, Thm 1.3); H <= 2 aUC_parity (Arunachalam et al. arXiv:1809.09819); H <= 2(deg-1) (granularity). Classes: plateaued functions sharp constant 4 (Potapov arXiv:2  [opus/U-universal]

### CONDITIONAL (3)
-   [fleet/claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion]
-   [fleet/claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]

### PARTIAL (2)
- C025: H_mu^+ <= C (I_mu - Var_mu) uniformly for all weighted thresholds and all product laws.  [opus/BT-biased-thresholds]
- Same as W-T111 but with arbitrary output means (term decision lists in general).  [opus/W-witness-cost]

### EVIDENCE (24)
-   [fleet/claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion]
-   [fleet/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring]
-   [fleet/claude/B16/runs/20261011T225600Z-claude-B16-retained-kl-sandwich]
-   [fleet/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]
- Exhaustive enumeration of K2 for n <= 6 (n <= 4 all functions and address sets; n = 5, 6 with the address pair fixed, all product rows, symmetry reduction only by x-translations, x-permutations and negation) gives max H/I = c* = 2.955889582 (AND_3); 1,564,928 K2 functions at n = 5 with a fixed address pair.  [opus/A2-two-addresses]
- The arithmetic relaxation of K2 (row types constrained only by Lemmas 3, 5, 6) has supremum c* in every searched parameter range; next-best scenario rho = 3 (2.914374), then rho = 2 (2.786517); E_* empty scenario 2.505329. All relaxation constraints and the inequality chain H - c*I <= Phi <= 0 were checked on about 98,000 sampled K2 functions with |C| = 3, 4.  [opus/A2-two-addresses]
- Three addresses, n = 5 (|C| = 2): exhaustive search (2,634,528 functions after reducing the x = 0 fiber by y-translations, y-permutations and negation) gives max H/I = 3.402475551 = H/I(AND_4), equal to the maximum over all 4-variable Boolean functions. Conjecture (open): C_3 = H/I(AND_4).  [opus/A2-two-addresses]
- With exact level normalizers the paper's (level-independent) reference gives a Gibbs bound of about 1.3 I on T_s, while the paper's estimate ln Z_k <= k + 4m gives 5.15-5.62 I growing with s: the loss on T_s is in the normalizer estimate.  [opus/BT-biased-thresholds]
- On alternating AND/OR trees (fan-in 2, depth to 22; AND2/OR3 to 12): B/I -> 3.6557, H/I -> about 5.345; sum_i H(S_i | |S - i|)/I grows by 1.00 per two levels (order log log(1/eps), a second level-statistic obstruction besides O5); every fixed-height witness has excess (kappa_h + o(1)) eps_i log2(1/eps_i) with kappa_h = 0.495, 0.162, 0.045, 0.009 at h = 1, 3, 5, 7, and the excess falls below I once  [opus/L2-level-two]
- Brute force on 43 functions (n = 6 to 16; 34 structured, 9 generic). (i) The pair (pattern of S - i on the first class of equal co-occurrence P(S contains i, j) that it meets, |S - i|) is an exact witness on 27 of the 28 structured functions outside the X-family; the exception (AND/OR depth 4, +0.0037 I) is an ordering effect, since co-occurrence is not monotone in tree distance (0.0663, 0.0221, 0  [opus/L2-level-two]
- An unpredictable coordinate need not have a subcube pivotal set. For F(y, t) = g(y) (-1)^{t 1_A(y)}, g bent on m bits, A a uniformly random set of 2^{m/2} points: B_t/eps_t - log2(1/eps_t) = 0.121, 0.264, 0.323, 0.352, 0.370, 0.379 and u_t = B_t/h2(eps_t) = 0.798 ... 0.907 at m = 10, ..., 20 (heuristic limit of the offset log2 e - 1.05 = 0.39, so u_t -> 1), while I(1_{A_t}) is 1.97 to 2.00 times t  [opus/L2-level-two]
- On the selector functions of sections 5c-5d the payment of L2-SB is loose: B_Y / 2 I_X = 0.019, 0.0011, 0.0001 on X009 (m = 6, 10, 14), 0.026 and 0.0031 on cube selectors, 0.020 and 0.0070 on random-set selectors, 0.37, 0.28, 0.26 on the many-selector functions (dependent selectors: H(S_Y) = 5.18, 4.07, 3.65 against sum_Y h2 = 6.49, 4.35, 4.05), 0 on the address functions (B_Y = 0 although H(S_Y)   [opus/L2-level-two]
- On K-partite polynomials the largest H/I found, exhaustively on the shapes (1,1,1), (2,1,1), (3,1,1), (2,2,1), (1,1,1,1), on random members and in a greedy search, is that of one monomial with a variable in each block (the AND of K bits up to sign): 2 at K = 2, c* = 2.9559 at K = 3, 3.4025 at K = 4, against the bounds 2, 4, 6. Simulated annealing on shapes up to (4,4,4) and (3,3,3,3), restarted fr  [opus/L2-level-two]
- Theorem G is tight: equality for all addressing functions tested and 2-bit bent; ratio H/(2(I-Var)+2U) -> 1 on point defects and reaches 0.986 on near-extremal read-once AND/OR formulas with H/I = 5.91 (U/I = 2.06), so on the extremal family C_FEI is governed by sup U/I.  [opus/U-universal]
- U is immune to the sparse-activation local-log obstruction: on X003 (k=4..10) Delta_y U/Inf_y = 3.69, 4.10, 4.25, 4.30 while Delta_y H/Inf_y = 8.33..14.33 grows like k; on X009 (m=4..12) 3.57..4.31 vs 8.0..16.3; on X002 -> 3.0.  [opus/U-universal]
- The universal local form 'Delta_i U <= K Inf_i for every coordinate i' is not supported: annealing over selector pairs gives max Delta_y U/Inf_y = 4.78, 5.11, 5.48, 6.15 at n = 6, 7, 8, 9, dominated by the KL asymmetry term.  [opus/U-universal]
- Exhaustive n <= 4: max H/I = 3.4025, max B/I = 2.7042, K_loc >= 2.6725, K_Delta >= 4.8677, max U/I = 1.465, max G/I = 2.75, Theorem G holds with minimum slack 0.  [opus/U-universal]
- On 300 random selector trees (read-once and general trees, regular leaves, up to 16 variables) the queue-law code lengths satisfy minW/I <= 6.17, witness-sum/I <= 6.17, owner-coded/I <= 4.97, H/I <= 3.40; in particular nothing near the proved 17.  [opus/W-witness-cost]
- The C008 rank term is order-sensitive on term decision lists: with the natural path order, m = 2^w terms of width w have rank-term/I growing about linearly in w (0.30, 0.77, 1.39, 2.11, 2.88, 3.73 for w = 2..7); with the length (=deficit) order it stays <= 0.56 up to w = 10 and the total stays near 8.5-8.9 I. With mixed widths (one narrow top block before about 10*2^W wide terms of negligible infl  [opus/W-witness-cost]
- Decision-tree witness code and rank term: all f with n <= 4 (222 NPN classes for n=4, best of 24 ordered reduced trees and f, -f): witness-sum code/I <= 6.06, min-witness <= 6.17. Majority (sequential tree, n = 3..13): witness-sum code/I falls 4.06 -> 3.88 while min-witness rises 4.69 -> 6.55; R/I = 0.43 -> 0.76 (n <= 11; heuristic limit 2 e^{-1/2}/ln 2 = 1.75). Read-once AND/OR formulas (short-ci  [opus/W-witness-cost]
- On Wan-Wright-Wu's bad tree (l dummy levels above copies of MAJ_5, l = 0..6) the path-order rank term grows (R/I 0.58 -> 1.89, code/I 4.04 -> 6.46) while the adapted-order rank term is exactly constant (R/I = 0.428): the reduction with adapted orders is immune to the dummy-level obstruction that costs their protocol 2l characters. Random read-k trees (k <= 8): R/I <= 0.62 (path), <= 0.37 (adapted)  [opus/W-witness-cost]
- On read-once AND/OR formulas with left-to-right short-circuit cells, the rank term of W-P121 grows with formula depth while H/I saturates: AND-OR trees depth 1..12 have H/I = 2.00 ... 5.29 (levelling near 5.3) but R_path/I = 0.25 ... 2.85 and R_mix/I (path and reversed orders) = 0.63 ... 2.39, rising about 0.2 per level; a near-balanced AND2/OR3 control shows the same (d=5: H/I 4.53, R_path/I 1.63  [opus/W-witness-cost]

### CONJECTURE (6)
- sup over weighted thresholds and product laws of H_mu^+/Delta_mu equals the AND/OR constant 2 + 4/ln 2 = 7.7708.  [opus/BT-biased-thresholds]
- (LCR) sum_k W_k ln(1/W_k) <= sum_k sum_i W_k pi_i^(k) ln^+(4 pi_i^(k)/sigma_i^2) + C I for every weighted threshold and product law, pi_i^(k) = inclusion probability of i in the level-k spectral sample. PROVED: (LCR) implies E <= (C + 1 + ln 11 + (6/5)(3 + ln 4)) I uniformly; for symmetric thresholds (LCR) follows from the paper's credit lemma by convexity.  [opus/BT-biased-thresholds]
- For pairwise orthogonal Boolean leaves and any partition, H(F) <= H(p) + sum_k p_k [H(q_k) + H(G_k)] + kappa B with B = sum_k p_k(1-p_k) and an absolute kappa; this would give the constant-preserving strong closure max{C_s, 4 + kappa, C_g}(I(F)-1).  [opus/SEL-selector-interference]
- Schmidt-entropy defect: for every real matrix M with ||M||_F = 1 and every SVD M = sum_k sigma_k u_k v_k^T (s_k = sigma_k^2), H(|M|^2) <= H(s) + sum_k s_k [H(u_k^2) + H(v_k^2)] + kappa_0 sum_k s_k (1 - s_k), kappa_0 = 0.756151564 (numerical supremum, attained in the limit M_t = [[t,1],[t^2(1-eta),t]], t -> 0, eta = 4.5911). Implies SEL-8' with kappa = kappa_0 for every partition and every orthonor  [opus/SEL-selector-interference]
- GU: sum_i Delta_i U(f) <= K I(f) for all Boolean f (K about 3.1); weaker GU': sum_i Delta_i U <= a I + b U with b < 1. Either implies U <= K' I by restriction induction (K' = a/(1-b)) and hence FEI with C <= 2 + 2K'.  [opus/U-universal]
- There is an absolute K such that every nonconstant Boolean f has a subcube partition of f^{-1}(1) or f^{-1}(-1) (e.g. the leaves of a decision tree) and orders with R(f) <= K I(f). By W-P121 this implies FEI with C = 23.55 + 2.4 K. Read with R_mix (W-P123) in place of R.  [opus/W-witness-cost]

### OPEN_TARGET (1)
-   [fleet/agents/A079/runs/20261011T224806Z-fleet05-A079-correlated-auxiliaries]

### A042_FULL_NARROW_INDEPENDENT_ACCEPTANCE_CONSUMED_LOCALLY; ORIGINAL_UNCHANGED (1)
-   [fleet/agents/A044/runs/20261014T055346Z-fleet05-A044-non-symmetric-gate-classes]

### A045_INDEPENDENT_REVIEW_CONSUMED_LOCAL_RECORD_PENDING_SUPERVISOR_ADOPTION (1)
-   [fleet/agents/A041/runs/20261014T083216Z-fleet05-A041-weighted-threshold-fei]

### A055_PHYSICAL_GEOMETRY_SCOPED_REVIEW_HOLDS; BUNDLED_TRANSFER_NOT_AUDITED (1)
-   [fleet/agents/A055/runs/20261014T064016Z-fleet05-A055-extremal-obstruction-referee]

### A055_SCOPED_ALGEBRA_REVIEW_HOLDS; FULL_CHAIN_INDEPENDENCE_NOT_CLAIMED (1)
-   [fleet/agents/A055/runs/20261014T033719Z-fleet05-A055-extremal-obstruction-referee]

### A088_INDEPENDENT_ACCEPTANCE_RECEIPT_CONSUMED_PENDING_B20 (1)
-   [fleet/agents/A070/runs/20261014T034205Z-fleet05-A070-analytic-route-referee]

### ACCEPTED_LOCAL_INDEPENDENT_REVIEW (5)
-   [fleet/agents/A057/runs/20261012T003930Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261012T003930Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261012T003930Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A058/runs/20261012T020138Z-fleet05-A058-overlapping-compositions]
-   [fleet/agents/A058/runs/20261013T234047Z-fleet05-A058-overlapping-compositions]

### ANALYTICALLY_PROVED_AUTHOR_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A010/runs/20261011T225444Z-fleet05-A010-universal-residual-falsifier]

### ANALYTICALLY_PROVED_CERTIFIED_SMALL_CASES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A006/runs/20261011T231903Z-fleet05-A006-posterior-forest-optimization]

### ANALYTICALLY_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW (3)
-   [fleet/agents/A009/runs/20261013T235139Z-fleet05-A009-fractional-incidence-optimization]
-   [fleet/agents/A010/runs/20261014T001430Z-fleet05-A010-universal-residual-falsifier]
-   [fleet/agents/A010/runs/20261014T031741Z-fleet05-A010-universal-residual-falsifier]

### ANALYTICALLY_PROVED_EXACT_BOOLEAN_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A008/runs/20261014T050954Z-fleet05-A008-gate-label-compression]

### ANALYTICALLY_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A009/runs/20261014T054349Z-fleet05-A009-fractional-incidence-optimization]

### ANALYTICALLY_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A008/runs/20261013T222820Z-fleet05-A008-gate-label-compression]
-   [fleet/agents/A008/runs/20261014T021605Z-fleet05-A008-gate-label-compression]

### ANALYTICALLY_PROVED_EXACT_COMBINATORIAL_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A006/runs/20261013T214427Z-fleet05-A006-posterior-forest-optimization]

### ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED (2)
-   [fleet/agents/A092/runs/20261011T221121Z-fleet05-A092-counterexample-referee]
-   [fleet/agents/A092/runs/20261012T004903Z-fleet05-A092-counterexample-referee]

### ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED_CORE_ONLY (3)
-   [fleet/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A091/runs/20261011T234101Z-fleet05-A091-composition-referee]
-   [fleet/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority]

### ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED_LOCALLY (6)
-   [fleet/agents/A007/runs/20261011T234502Z-fleet05-A007-root-normalization]
-   [fleet/agents/A094/runs/20261011T224936Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261011T224936Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A095/runs/20261011T231526Z-fleet05-A095-restricted-result-extraction]
-   [fleet/agents/A095/runs/20261011T231526Z-fleet05-A095-restricted-result-extraction]
-   [fleet/agents/A095/runs/20261013T213857Z-fleet05-A095-restricted-result-extraction]

### ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED_LOCALLY_BY_A039 (2)
-   [fleet/agents/A039/runs/20261011T223903Z-fleet05-A039-projection-under-restrictions]
-   [fleet/agents/A039/runs/20261011T223903Z-fleet05-A039-projection-under-restrictions]

### ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED_LOCALLY_BY_A040 (1)
-   [fleet/agents/A040/runs/20261013T212401Z-fleet05-A040-credit-insufficiency-tests]

### ANALYTICALLY_PROVED_LOCALLY_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A036/runs/20261011T214139Z-fleet05-A036-reference-law-divergence]

### ANALYTICALLY_PROVED_LOCAL_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A036/runs/20261011T232800Z-fleet05-A036-reference-law-divergence]

### ANALYTICALLY_PROVED_NARROW_ROUTE_OBSTRUCTION_AND_ONE_USE_FIXTURE_PAYMENT_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A094/runs/20261014T061347Z-fleet05-A094-proof-chain-challenger]

### ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW (9)
-   [fleet/agents/A006/runs/20261011T210855Z-fleet05-A006-posterior-forest-optimization]
-   [fleet/agents/A046/runs/20261011T214251Z-fleet05-A046-current-candidate-intake]
-   [fleet/agents/A092/runs/20261011T221121Z-fleet05-A092-counterexample-referee]
-   [fleet/agents/A094/runs/20261011T224936Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261012T044109Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261014T001244Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A096/runs/20261011T215017Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A096/runs/20261011T215017Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A096/runs/20261011T234252Z-fleet05-A096-live-gap-ledger]

### ANALYTICALLY_PROVED_SCOPED_CORRECTION_DIAGNOSTIC_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A100/runs/20261011T231552Z-fleet05-A100-release-and-continuation-ledger]

### ANALYTICALLY_PROVED_SHARP_STRESS_FAMILY_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A094/runs/20261014T031253Z-fleet05-A094-proof-chain-challenger]

### ANALYTIC_ALL_GRAPH_OPTIMIZATION_PROVED_EXACT_FINITE_COSTS_CERTIFIED_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A009/runs/20261014T024630Z-fleet05-A009-fractional-incidence-optimization]

### ANALYTIC_AND_EXACT_CERTIFICATE_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A001/runs/20261011T231625Z-fleet05-A001-quantifier-audit]

### ANALYTIC_ARBITRARY_GRAPH_MASS_PROVED_EXACT_FINITE_COST_CERTIFIED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A006/runs/20261014T011124Z-fleet05-A006-posterior-forest-optimization]

### ANALYTIC_MEAN_ONLY_VARIANCE_ALLOCATION_REFUTATION_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A045/runs/20261014T063646Z-fleet05-A045-biased-realizability-referee]

### ANALYTIC_MECHANISM_REFUTATION_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A045/runs/20261013T212421Z-fleet05-A045-biased-realizability-referee]

### ANALYTIC_PROOF_AND_EXACT_CENSUS_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A043/runs/20261011T221757Z-fleet05-A043-prime-gate-decomposition]

### ANALYTIC_PROOF_COMPLETE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A001/runs/20261011T210330Z-fleet05-A001-quantifier-audit]

### ANALYTIC_PROOF_EXACT_CHECKS; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A042/runs/20261013T221414Z-fleet05-A042-bias-endpoint-certificates]

### AUTHOR_PROVED_ALL_DIMENSION_ALL_ADMISSIBLE_WORDS_REVIEW_PENDING_FULL_FEI_OPEN (1)
-   [fleet/agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge]

### AUTHOR_PROVED_AND_EXACTLY_REPLAYED_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A051/runs/20261013T215311Z-fleet05-A051-near-extremizer-definition]

### AUTHOR_PROVED_AND_EXACT_CERTIFICATES; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A006/runs/20261014T074929Z-fleet05-A006-posterior-forest-optimization]

### AUTHOR_PROVED_AT_SCOPED_DOMAINS_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A060/runs/20261013T212522Z-fleet05-A060-composition-sharpness]

### AUTHOR_PROVED_AT_STATED_SCOPE_PENDING_INDEPENDENT_REVIEW (6)
-   [fleet/agents/A025/runs/20261012T045020Z-fleet05-A025-rare-event-counterfamily]
-   [fleet/agents/A025/runs/20261014T002956Z-fleet05-A025-rare-event-counterfamily]
-   [fleet/agents/A025/runs/20261014T032227Z-fleet05-A025-rare-event-counterfamily]
-   [fleet/agents/A025/runs/20261014T062819Z-fleet05-A025-rare-event-counterfamily]
-   [fleet/agents/A035/runs/20261013T212341Z-fleet05-A035-signed-cancellation-countersearch]
-   [fleet/agents/A068/runs/20261014T023317Z-fleet05-A068-antichain-beyond-one-order]

### AUTHOR_PROVED_AT_STATED_SCOPE_WITH_EXACT_SIGN_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A035/runs/20261014T003450Z-fleet05-A035-signed-cancellation-countersearch]

### AUTHOR_PROVED_CONDITIONAL_COMPLETE_REFERENCE_INTERFACE_PENDING_REVIEW (1)
-   [fleet/agents/A018/runs/20261014T051305Z-fleet05-A018-shared-data-collision-law]

### AUTHOR_PROVED_CONDITIONAL_REFERENCE_INTERFACE_REPAIR_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A011/runs/20261014T074949Z-fleet05-A011-representation-existence]

### AUTHOR_PROVED_EXACTLY_CERTIFIED_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A037/runs/20261014T043944Z-fleet05-A037-conditional-credit-ledger]
-   [fleet/agents/A037/runs/20261014T111143Z-fleet05-A037-conditional-credit-ledger]

### AUTHOR_PROVED_EXACTLY_CERTIFIED_SCOPED_APPLICATION_PENDING_REVIEW (1)
-   [fleet/agents/A097/runs/20261012T005449Z-fleet05-A097-cross-route-transfer]

### AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW (8)
-   [fleet/agents/A007/runs/20261011T215236Z-fleet05-A007-root-normalization]
-   [fleet/agents/A007/runs/20261011T234502Z-fleet05-A007-root-normalization]
-   [fleet/agents/A007/runs/20261013T220854Z-fleet05-A007-root-normalization]
-   [fleet/agents/A007/runs/20261014T014217Z-fleet05-A007-root-normalization]
-   [fleet/agents/A007/runs/20261014T043228Z-fleet05-A007-root-normalization]
-   [fleet/agents/A007/runs/20261014T100124Z-fleet05-A007-root-normalization]
-   [fleet/agents/A008/runs/20261011T221357Z-fleet05-A008-gate-label-compression]
-   [fleet/agents/A009/runs/20261012T031835Z-fleet05-A009-fractional-incidence-optimization]

### AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW (9)
-   [fleet/agents/A037/runs/20261011T220010Z-fleet05-A037-conditional-credit-ledger]
-   [fleet/agents/A037/runs/20261011T220010Z-fleet05-A037-conditional-credit-ledger]
-   [fleet/agents/A039/runs/20261011T223903Z-fleet05-A039-projection-under-restrictions]
-   [fleet/agents/A039/runs/20261013T235428Z-fleet05-A039-projection-under-restrictions]
-   [fleet/agents/A039/runs/20261014T025407Z-fleet05-A039-projection-under-restrictions]
-   [fleet/agents/A039/runs/20261014T055326Z-fleet05-A039-projection-under-restrictions]
-   [fleet/agents/A063/runs/20261011T222159Z-fleet05-A063-information-revelation]
-   [fleet/agents/A063/runs/20261014T052608Z-fleet05-A063-information-revelation]
-   [fleet/agents/A097/runs/20261011T221240Z-fleet05-A097-cross-route-transfer]

### AUTHOR_PROVED_EXACT_CERTIFICATE; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A042/runs/20261012T002547Z-fleet05-A042-bias-endpoint-certificates]

### AUTHOR_PROVED_EXACT_CERTIFICATES_PASSED_PENDING_INDEPENDENT_REVIEW (5)
-   [fleet/agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A070/runs/20261013T212602Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261014T005025Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261014T034205Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee]

### AUTHOR_PROVED_EXACT_CERTIFICATES_PASS_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A054/runs/20261013T235828Z-fleet05-A054-connectedness-alternatives]

### AUTHOR_PROVED_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A080/runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard]

### AUTHOR_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_REVIEW (10)
-   [fleet/agents/A077/runs/20261011T220936Z-fleet05-A077-sparse-defect-towers]
-   [fleet/agents/A077/runs/20261012T004059Z-fleet05-A077-sparse-defect-towers]
-   [fleet/agents/A077/runs/20261013T222235Z-fleet05-A077-sparse-defect-towers]
-   [fleet/agents/A077/runs/20261014T020716Z-fleet05-A077-sparse-defect-towers]
-   [fleet/agents/A077/runs/20261014T045011Z-fleet05-A077-sparse-defect-towers]
-   [fleet/agents/A078/runs/20261011T222503Z-fleet05-A078-coding-and-padding]
-   [fleet/agents/A078/runs/20261012T023229Z-fleet05-A078-coding-and-padding]
-   [fleet/agents/A078/runs/20261013T234208Z-fleet05-A078-coding-and-padding]
-   [fleet/agents/A078/runs/20261014T023613Z-fleet05-A078-coding-and-padding]
-   [fleet/agents/A078/runs/20261014T053454Z-fleet05-A078-coding-and-padding]

### AUTHOR_PROVED_EXACT_CHECKS_PASSED_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A068/runs/20261011T222313Z-fleet05-A068-antichain-beyond-one-order]
-   [fleet/agents/A069/runs/20261014T030208Z-fleet05-A069-geometric-transfer]

### AUTHOR_PROVED_EXACT_INTERFACE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A018/runs/20261013T222945Z-fleet05-A018-shared-data-collision-law]

### AUTHOR_PROVED_EXACT_N4_CENSUS_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/claude/B08/runs/20261011T225000Z-claude-B08-tc-restriction-ledger]

### AUTHOR_PROVED_EXACT_VALIDATION_PASSED_PENDING_INDEPENDENT_REVIEW (3)
-   [fleet/agents/A054/runs/20261011T224200Z-fleet05-A054-connectedness-alternatives]
-   [fleet/agents/A067/runs/20261014T020120Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261014T044841Z-fleet05-A067-hypercontractive-refinement]

### AUTHOR_PROVED_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A054/runs/20261014T025808Z-fleet05-A054-connectedness-alternatives]
-   [fleet/agents/A054/runs/20261014T055856Z-fleet05-A054-connectedness-alternatives]

### AUTHOR_PROVED_FINITE_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A072/runs/20261014T124911Z-fleet05-A072-exact-walsh-engine]

### AUTHOR_PROVED_GUARDED_GROWING_EDIT_AND_RECURSIVE_CLOSURE_PENDING_REVIEW (1)
-   [fleet/agents/A022/runs/20261014T043413Z-fleet05-A022-one-point-surgery]

### AUTHOR_PROVED_INDEPENDENTLY_REVIEWED_LOCAL_RECEIPT (2)
-   [fleet/agents/A067/runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement]

### AUTHOR_PROVED_INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A072/runs/20261014T020611Z-fleet05-A072-exact-walsh-engine]

### AUTHOR_PROVED_MECHANISM_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A090/runs/20261014T010003Z-fleet05-A090-independent-reconstruction]

### AUTHOR_PROVED_NARROW_COMB_INTERFACE_EXTENSION_PENDING_REVIEW (1)
-   [fleet/agents/A011/runs/20261013T214448Z-fleet05-A011-representation-existence]

### AUTHOR_PROVED_NARROW_CONTINUUM_ADMISSION_REFINEMENT_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A012/runs/20261014T043333Z-fleet05-A012-sparse-activation-accounting]
-   [fleet/agents/A013/runs/20261014T051241Z-fleet05-A013-representation-stability]

### AUTHOR_PROVED_NARROW_FINITE_COUNTEREXAMPLES_AND_CENSUS_INDEPENDENT_REVIEW_PENDING_FULL_FEI_OPEN (1)
-   [fleet/agents/A071/runs/20261014T090502Z-fleet05-A071-search-space-design]

### AUTHOR_PROVED_NARROW_INTERFACE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A012/runs/20261013T220914Z-fleet05-A012-sparse-activation-accounting]

### AUTHOR_PROVED_NARROW_NECESSARY_CONDITION_EXACT_REPLAY_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A051/runs/20261014T085227Z-fleet05-A051-near-extremizer-definition]

### AUTHOR_PROVED_NARROW_PACKET_EXTENSION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A013/runs/20261014T021710Z-fleet05-A013-representation-stability]

### AUTHOR_PROVED_NARROW_PACKET_REFINEMENT_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A012/runs/20261014T101345Z-fleet05-A012-sparse-activation-accounting]

### AUTHOR_PROVED_NARROW_PACKET_REFINEMENT_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A012/runs/20261014T014452Z-fleet05-A012-sparse-activation-accounting]

### AUTHOR_PROVED_NARROW_PACKET_REPAIR_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A013/runs/20261014T051241Z-fleet05-A013-representation-stability]

### AUTHOR_PROVED_NARROW_REFERENCE_CONTINUATION_PENDING_REVIEW (1)
-   [fleet/agents/A086/runs/20261014T042208Z-fleet05-A086-joint-code-referee]

### AUTHOR_PROVED_NARROW_REFERENCE_OWNERSHIP_CONTINUATION_PENDING_REVIEW (1)
-   [fleet/agents/A011/runs/20261014T011235Z-fleet05-A011-representation-existence]

### AUTHOR_PROVED_NARROW_REFERENCE_REPAIR_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A011/runs/20261014T035454Z-fleet05-A011-representation-existence]
-   [fleet/agents/A031/runs/20261014T011913Z-fleet05-A031-convolution-identity]

### AUTHOR_PROVED_NARROW_REFINEMENT_EXACTLY_REPLAYED_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A051/runs/20261014T012634Z-fleet05-A051-near-extremizer-definition]

### AUTHOR_PROVED_NARROW_REFINEMENT_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A055/runs/20261014T004129Z-fleet05-A055-extremal-obstruction-referee]

### AUTHOR_PROVED_NARROW_ROUTE_REPAIR_PENDING_INDEPENDENT_REVIEW (3)
-   [fleet/agents/A031/runs/20261013T215020Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261014T075717Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261014T075717Z-fleet05-A031-convolution-identity]

### AUTHOR_PROVED_NARROW_TRANSPORT_EXACTLY_REPLAYED_PENDING_INDEPENDENT_AGENT_REVIEW (1)
-   [fleet/agents/A051/runs/20261014T041948Z-fleet05-A051-near-extremizer-definition]

### AUTHOR_PROVED_NEW_HISTORY_PENDING_INDEPENDENT_REVIEW; LEGACY_SCOPED_REVIEWS_PRESERVED (1)
-   [fleet/agents/A095/runs/20261014T074829Z-fleet05-A095-restricted-result-extraction]

### AUTHOR_PROVED_NEW_SUPPORT_COMPLETION_PENDING_INDEPENDENT_REVIEW; PRIOR_CLAUSES_SCOPED_REVIEWED (1)
-   [fleet/agents/A095/runs/20261014T034647Z-fleet05-A095-restricted-result-extraction]

### AUTHOR_PROVED_PENDING_FULL_INDEPENDENT_REVIEW; B05_R_EQUALS_2K_SUBCLAIM_ACCEPTED_BY_A001 (1)
-   [fleet/agents/A001/runs/20261011T231625Z-fleet05-A001-quantifier-audit]

### AUTHOR_PROVED_PENDING_FULL_REVIEW; EXCHANGEABLE_OPTIMUM_SLICE_INDEPENDENTLY_ACCEPTED_BY_A001 (1)
-   [fleet/agents/A001/runs/20261013T213937Z-fleet05-A001-quantifier-audit]

### AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (95)
-   [fleet/agents/A003/runs/20261011T221324Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A003/runs/20261011T221324Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A003/runs/20261012T005637Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A003/runs/20261012T005637Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A011/runs/20261011T213831Z-fleet05-A011-representation-existence]
-   [fleet/agents/A012/runs/20261011T215648Z-fleet05-A012-sparse-activation-accounting]
-   [fleet/agents/A013/runs/20261011T221511Z-fleet05-A013-representation-stability]
-   [fleet/agents/A013/runs/20261012T010150Z-fleet05-A013-representation-stability]
-   [fleet/agents/A014/runs/20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read]
-   [fleet/agents/A014/runs/20261013T235200Z-fleet05-A014-overlap-beyond-worst-case-read]
-   [fleet/agents/A014/runs/20261014T024736Z-fleet05-A014-overlap-beyond-worst-case-read]
-   [fleet/agents/A014/runs/20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read]
-   [fleet/agents/A017/runs/20261011T215725Z-fleet05-A017-recursive-addressing]
-   [fleet/agents/A017/runs/20261011T234546Z-fleet05-A017-recursive-addressing]
-   [fleet/agents/A022/runs/20261011T215800Z-fleet05-A022-one-point-surgery]
-   [fleet/agents/A025/runs/20261011T225648Z-fleet05-A025-rare-event-counterfamily]
-   [fleet/agents/A030/runs/20261011T225732Z-fleet05-A030-restriction-plateau-tests]
-   [fleet/agents/A030/runs/20261013T212321Z-fleet05-A030-restriction-plateau-tests]
-   [fleet/agents/A030/runs/20261014T003426Z-fleet05-A030-restriction-plateau-tests]
-   [fleet/agents/A031/runs/20261011T214115Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261011T214115Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261011T232738Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261011T232738Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A034/runs/20261011T223816Z-fleet05-A034-phase-energy-transfer]
-   [fleet/agents/A040/runs/20261011T225840Z-fleet05-A040-credit-insufficiency-tests]
-   [fleet/agents/A041/runs/20261011T214208Z-fleet05-A041-weighted-threshold-fei]
-   [fleet/agents/A041/runs/20261011T214208Z-fleet05-A041-weighted-threshold-fei]
-   [fleet/agents/A042/runs/20261011T220136Z-fleet05-A042-bias-endpoint-certificates]
-   [fleet/agents/A048/runs/20261011T221822Z-fleet05-A048-tensor-stress]
-   [fleet/agents/A051/runs/20261011T214321Z-fleet05-A051-near-extremizer-definition]
-   [fleet/agents/A051/runs/20261011T214321Z-fleet05-A051-near-extremizer-definition]
-   [fleet/agents/A052/runs/20261011T220243Z-fleet05-A052-critical-source-structure]
-   [fleet/agents/A052/runs/20261012T003906Z-fleet05-A052-critical-source-structure]
-   [fleet/agents/A055/runs/20261013T212502Z-fleet05-A055-extremal-obstruction-referee]
-   [fleet/agents/A060/runs/20261011T230152Z-fleet05-A060-composition-sharpness]
-   [fleet/agents/A061/runs/20261011T214516Z-fleet05-A061-entropy-process]
-   [fleet/agents/A061/runs/20261011T214516Z-fleet05-A061-entropy-process]
-   [fleet/agents/A061/runs/20261011T233210Z-fleet05-A061-entropy-process]
-   [fleet/agents/A061/runs/20261013T215821Z-fleet05-A061-entropy-process]
-   [fleet/agents/A062/runs/20261011T220423Z-fleet05-A062-influence-compensator]
-   [fleet/agents/A062/runs/20261011T220423Z-fleet05-A062-influence-compensator]
-   [fleet/agents/A062/runs/20261012T003951Z-fleet05-A062-influence-compensator]
-   [fleet/agents/A062/runs/20261013T221705Z-fleet05-A062-influence-compensator]
-   [fleet/agents/A062/runs/20261014T015800Z-fleet05-A062-influence-compensator]
-   [fleet/agents/A062/runs/20261014T044820Z-fleet05-A062-influence-compensator]
-   [fleet/agents/A062/runs/20261014T124831Z-fleet05-A062-influence-compensator]
-   [fleet/agents/A065/runs/20261014T033844Z-fleet05-A065-stopping-rule-falsifier]
-   [fleet/agents/A066/runs/20261011T214539Z-fleet05-A066-semigroup-dissipation]
-   [fleet/agents/A066/runs/20261011T214539Z-fleet05-A066-semigroup-dissipation]
-   [fleet/agents/A066/runs/20261011T233317Z-fleet05-A066-semigroup-dissipation]
-   [fleet/agents/A066/runs/20261011T233317Z-fleet05-A066-semigroup-dissipation]
-   [fleet/agents/A066/runs/20261013T215841Z-fleet05-A066-semigroup-dissipation]
-   [fleet/agents/A066/runs/20261013T215841Z-fleet05-A066-semigroup-dissipation]
-   [fleet/agents/A067/runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261012T004014Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A069/runs/20261011T224507Z-fleet05-A069-geometric-transfer]
-   [fleet/agents/A069/runs/20261012T043929Z-fleet05-A069-geometric-transfer]
-   [fleet/agents/A069/runs/20261014T000110Z-fleet05-A069-geometric-transfer]
-   [fleet/agents/A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A076/runs/20261011T214703Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261011T214703Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261011T233829Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261011T233829Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261013T220051Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261013T220051Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261014T013416Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261014T013416Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261014T042128Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261014T042128Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261014T091637Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A076/runs/20261014T091637Z-fleet05-A076-threshold-and-tribes-controls]
-   [fleet/agents/A079/runs/20261012T044009Z-fleet05-A079-correlated-auxiliaries]
-   [fleet/agents/A079/runs/20261014T000722Z-fleet05-A079-correlated-auxiliaries]
-   [fleet/agents/A080/runs/20261011T231244Z-fleet05-A080-universal-counterexample-standard]
-   [fleet/agents/A080/runs/20261014T074729Z-fleet05-A080-universal-counterexample-standard]
-   [fleet/agents/A086/runs/20261011T234041Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261013T220217Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261014T013711Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A089/runs/20261011T224857Z-fleet05-A089-repair-specialist]
-   [fleet/agents/A089/runs/20261012T044049Z-fleet05-A089-repair-specialist]
-   [fleet/agents/A089/runs/20261014T000812Z-fleet05-A089-repair-specialist]
-   [fleet/agents/A090/runs/20261013T213537Z-fleet05-A090-independent-reconstruction]
-   [fleet/agents/A092/runs/20261013T222550Z-fleet05-A092-counterexample-referee]
-   [fleet/agents/A095/runs/20261011T231526Z-fleet05-A095-restricted-result-extraction]
-   [fleet/agents/A095/runs/20261011T231526Z-fleet05-A095-restricted-result-extraction]
-   [fleet/agents/A095/runs/20261013T213857Z-fleet05-A095-restricted-result-extraction]
-   [fleet/agents/A095/runs/20261014T010024Z-fleet05-A095-restricted-result-extraction]
-   [fleet/claude/B09/runs/20261011T225000Z-claude-B09-sharp-uniform-endpoint-tax]
-   [fleet/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich]
-   [fleet/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich]
-   [fleet/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich]
-   [fleet/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich]
-   [fleet/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich]
-   [fleet/claude/B14/runs/20261011T224500Z-claude-B14-granularity-neutralization]

### AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW_WITH_SCOPED_REVIEWED_DEPENDENCY (2)
-   [fleet/agents/A030/runs/20261014T032502Z-fleet05-A030-restriction-plateau-tests]
-   [fleet/agents/A030/runs/20261014T062839Z-fleet05-A030-restriction-plateau-tests]

### AUTHOR_PROVED_RATIONAL_INTERVAL_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A008/runs/20261012T005959Z-fleet05-A008-gate-label-compression]

### AUTHOR_PROVED_REFORMULATION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/claude/B08/runs/20261011T225000Z-claude-B08-tc-restriction-ledger]

### AUTHOR_PROVED_REPAIR_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A011/runs/20261011T232009Z-fleet05-A011-representation-existence]
-   [fleet/agents/A012/runs/20261011T234525Z-fleet05-A012-sparse-activation-accounting]

### AUTHOR_PROVED_RESTRICTED_CONTINUUM_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A084/runs/20261014T000747Z-fleet05-A084-continuum-parameters]

### AUTHOR_PROVED_REVIEW_PENDING (2)
-   [fleet/agents/A017/runs/20261013T220934Z-fleet05-A017-recursive-addressing]
-   [fleet/agents/A050/runs/20261011T230000Z-fleet05-A050-repair-with-scope]

### AUTHOR_PROVED_ROOT_DENSITY_HIGH_INFLUENCE_EXTENSION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A022/runs/20261014T103056Z-fleet05-A022-one-point-surgery]

### AUTHOR_PROVED_SCOPED; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A052/runs/20261014T124751Z-fleet05-A052-critical-source-structure]

### AUTHOR_PROVED_SCOPED_ANALYTIC_PLUS_EXACT_CERTIFICATE_REVIEW_PENDING (1)
-   [fleet/agents/A075/runs/20261013T212622Z-fleet05-A075-search-to-theorem-bridge]

### AUTHOR_PROVED_SCOPED_APPLICATION_PENDING_INDEPENDENT_REVIEW (3)
-   [fleet/agents/A041/runs/20261011T232825Z-fleet05-A041-weighted-threshold-fei]
-   [fleet/agents/A052/runs/20261013T221539Z-fleet05-A052-critical-source-structure]
-   [fleet/agents/A052/runs/20261014T015635Z-fleet05-A052-critical-source-structure]

### AUTHOR_PROVED_SCOPED_AUDIT_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A038/runs/20261011T221733Z-fleet05-A038-occupancy-term-audit]

### AUTHOR_PROVED_SCOPED_BOOLEAN_OBSTRUCTION_AND_PAID_CONTROL_PENDING_REVIEW (1)
-   [fleet/agents/A018/runs/20261014T022025Z-fleet05-A018-shared-data-collision-law]

### AUTHOR_PROVED_SCOPED_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A022/runs/20261011T234607Z-fleet05-A022-one-point-surgery]

### AUTHOR_PROVED_SCOPED_CONSEQUENCE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A033/runs/20261011T221704Z-fleet05-A033-derivative-hierarchy]

### AUTHOR_PROVED_SCOPED_CONTINUATION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A041/runs/20261013T215146Z-fleet05-A041-weighted-threshold-fei]

### AUTHOR_PROVED_SCOPED_CONTINUATION_REVIEW_PENDING (3)
-   [fleet/agents/A017/runs/20261014T014813Z-fleet05-A017-recursive-addressing]
-   [fleet/agents/A017/runs/20261014T043353Z-fleet05-A017-recursive-addressing]
-   [fleet/agents/A017/runs/20261014T102650Z-fleet05-A017-recursive-addressing]

### AUTHOR_PROVED_SCOPED_CONTROLLER_EXTENSION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A022/runs/20261014T014918Z-fleet05-A022-one-point-surgery]

### AUTHOR_PROVED_SCOPED_CRITICAL_CLASS_REFEREE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A055/runs/20261014T064016Z-fleet05-A055-extremal-obstruction-referee]

### AUTHOR_PROVED_SCOPED_DIAGNOSTIC_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A015/runs/20261011T225533Z-fleet05-A015-minterm-barrier-analysis]

### AUTHOR_PROVED_SCOPED_EXTENSION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A022/runs/20261013T220954Z-fleet05-A022-one-point-surgery]

### AUTHOR_PROVED_SCOPED_HEREDITARY_REPAIR_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A035/runs/20261014T063030Z-fleet05-A035-signed-cancellation-countersearch]

### AUTHOR_PROVED_SCOPED_INTERFACE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A013/runs/20261013T222840Z-fleet05-A013-representation-stability]

### AUTHOR_PROVED_SCOPED_LEAD_TARGET_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A038/runs/20261012T012321Z-fleet05-A038-occupancy-term-audit]

### AUTHOR_PROVED_SCOPED_LEMMA_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A090/runs/20261014T034626Z-fleet05-A090-independent-reconstruction]

### AUTHOR_PROVED_SCOPED_MECHANISM_DIAGNOSTIC_REVIEW_PENDING (1)
-   [fleet/agents/A015/runs/20261012T044229Z-fleet05-A015-minterm-barrier-analysis]

### AUTHOR_PROVED_SCOPED_NONFLAT_RESERVE_AND_RECURSIVE_TRANSPORT_PENDING_REVIEW (1)
-   [fleet/agents/A097/runs/20261014T021008Z-fleet05-A097-cross-route-transfer]

### AUTHOR_PROVED_SCOPED_PACKET_EXTENSION_PENDING_REVIEW (1)
-   [fleet/agents/A040/runs/20261013T212401Z-fleet05-A040-credit-insufficiency-tests]

### AUTHOR_PROVED_SCOPED_PARAMETERIZED_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN (1)
-   [fleet/agents/A075/runs/20261014T074708Z-fleet05-A075-search-to-theorem-bridge]

### AUTHOR_PROVED_SCOPED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A029/runs/20261011T223746Z-fleet05-A029-child-deficit-transport]

### AUTHOR_PROVED_SCOPED_PHYSICAL_REPAIR_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN (1)
-   [fleet/agents/A089/runs/20261014T061326Z-fleet05-A089-repair-specialist]

### AUTHOR_PROVED_SCOPED_PRESCRIBED_REFERENCE_AND_DESTROYED_EDGE_PAYMENT_PENDING_REVIEW (1)
-   [fleet/agents/A097/runs/20261014T050248Z-fleet05-A097-cross-route-transfer]

### AUTHOR_PROVED_SCOPED_RECONSTRUCTION_REVIEW_PENDING (1)
-   [fleet/agents/A075/runs/20261011T231030Z-fleet05-A075-search-to-theorem-bridge]

### AUTHOR_PROVED_SCOPED_REFERENCE_CONTINUATION_PENDING_REVIEW (1)
-   [fleet/agents/A041/runs/20261014T083216Z-fleet05-A041-weighted-threshold-fei]

### AUTHOR_PROVED_SCOPED_REFERENCE_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A041/runs/20261014T012508Z-fleet05-A041-weighted-threshold-fei]

### AUTHOR_PROVED_SCOPED_REFINEMENT_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A099/runs/20261012T044129Z-fleet05-A099-candidate-assembly]

### AUTHOR_PROVED_SCOPED_REPAIR_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN (1)
-   [fleet/agents/A089/runs/20261014T030932Z-fleet05-A089-repair-specialist]

### AUTHOR_PROVED_SCOPED_RIGIDITY_AND_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A055/runs/20261014T033719Z-fleet05-A055-extremal-obstruction-referee]

### AUTHOR_PROVED_SCOPED_STRUCTURAL_APPLICATION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A052/runs/20261014T044609Z-fleet05-A052-critical-source-structure]

### AUTHOR_PROVED_SCOPED_TRACE_AND_EXACT_REFUTATION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A035/runs/20261014T032607Z-fleet05-A035-signed-cancellation-countersearch]

### AUTHOR_PROVED_SCOPED_TRANSFER_AND_BOOLEAN_BOUNDARY_PENDING_REVIEW (2)
-   [fleet/agents/A097/runs/20261013T222610Z-fleet05-A097-cross-route-transfer]
-   [fleet/agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly]

### AUTHOR_PROVED_SCOPE_PRESERVING_QUANTITATIVE_REFINEMENT_REVIEW_PENDING_FEI_OPEN (1)
-   [fleet/agents/A071/runs/20261014T042108Z-fleet05-A071-search-space-design]

### AUTHOR_PROVED_SOURCE_BOUND_LOCAL_PHYSICAL_PAYMENT_REVIEW_PENDING (1)
-   [fleet/agents/A084/runs/20261014T061132Z-fleet05-A084-continuum-parameters]

### AUTHOR_PROVED_SOURCE_BOUND_PREFIX_COMPLETION_INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A084/runs/20261014T030826Z-fleet05-A084-continuum-parameters]

### AUTHOR_PROVED_SOURCE_COMPLETE_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A029/runs/20261012T033113Z-fleet05-A029-child-deficit-transport]
-   [fleet/agents/A029/runs/20261013T235347Z-fleet05-A029-child-deficit-transport]

### AUTHOR_PROVED_TARGET_COMPLETE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A084/runs/20261012T044029Z-fleet05-A084-continuum-parameters]

### AUTHOR_PROVED_UNIVERSAL_REDUCTION_REVIEW_PENDING_FULL_FEI_OPEN (1)
-   [fleet/agents/A075/runs/20261014T005346Z-fleet05-A075-search-to-theorem-bridge]

### AUTHOR_PROVED_WITH_EXACT_ENDPOINT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A034/runs/20261014T055220Z-fleet05-A034-phase-energy-transfer]

### BASELINE_EXTENSION_PROVED_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A004/runs/20261012T030039Z-fleet05-A004-constant-and-unit-ledger]

### BASELINE_PROVED_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A004/runs/20261011T223224Z-fleet05-A004-constant-and-unit-ledger]

### BASELINE_REPRODUCED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A016/runs/20261011T213934Z-fleet05-A016-addressing-benchmark]

### CANDIDATE (20)
- KKLMS Theorem 1.3 transfers to +-1 functions with constant at most 4K (their influence is a probability of change), so every fixed level of B is O(I) with an unspecified constant; sum to level D is O(D log D) I.  [opus/L2-level-two]
- Lemma 1: B^(i)_j <= phi(a_{j,i}, d_{j,i}) <= d log(e(a+d)/d) <= psi(d_{j,i}). Summed over j: B_i = H(S_i | S - i) <= H(S_i | |S - i|).  [opus/L2-level-two]
- Lemma 2: d_0 <= eps^2; d_1 <= 2 eps^2 ln(2/eps) (two proofs: Hoeffding MGF with conditional Jensen, and entropy via the at-most-two-to-one map x -> D_i f(x) x); d_j <= eps^{2-2/q} (q-1)^j for every q >= 2 (Bonami); d_j <= eps.  [opus/L2-level-two]
- Theorem 3: B_{k-1} <= b_k I for every Boolean f, with b_1 = 2/(sqrt(e) ln 2) = 1.750078 exactly, b_k <= 2k log e for all k >= 2, and certified b_2 <= 3.5777, b_3 <= 7.3278, b_4 <= 10.1773, b_5 <= 13.0437, b_6 <= 15.9174, b_7 <= 18.795, b_8 <= 21.6747, b_9 <= 24.5559, b_10 <= 27.4379.  [opus/L2-level-two]
- Corollary 4: B_{<D} <= log(e) D(D+1) I for every D >= 1; certified partial sums 5.3278 (D=2), 12.6556 (D=3), 35.8766 (D=5), 144.2575 (D=10).  [opus/L2-level-two]
- Theorem 5 (localization): for 0 <= c < 1/2, sum_i sum_{j <= c ln(1/eps_i)} B^(i)_j <= C(c) I with C(c) finite; certified C(0.2) <= 1.7501, C(0.3) <= 4.0782, C(0.4) <= 13.8404, C(0.45) <= 46.9287.  [opus/L2-level-two]
- The threshold 1/2 in Theorem 5 is exact for the Bonami bound: for c >= 1/2 the bound of Lemma 2 at level floor(cL) does not decay, by ln(1+s) >= 2s/(2+s).  [opus/L2-level-two]
- No level inequality for {0,+-1} functions raises the threshold 1/2. Proposition 6: the level law of a Hamming slice 1{|y| = t} on N bits, rescaled by N, converges to the arcsine law on [1/2 - sqrt(rho(1-rho)), 1/2 + sqrt(rho(1-rho))] when t/N -> rho (moment method on the Krawtchouk Jacobi matrix). Corollary 7: for every c > 1/2 the derivatives of f = 1 - 2 1{#(-1) <= rho N} (rho near 1/2) keep a f  [opus/L2-level-two]
- Reduction: B <= (log(e/tau) + C(c)) I + B_gap(tau, c), B_gap = sum over i with eps_i < tau of the direction-i edges at levels j > c ln(1/eps_i); for fixed tau in (0,1) and c < 1/2, FEI is equivalent to B_gap(tau, c) = O(I).  [opus/L2-level-two]
- x0 times bent: B_k/I ~ 1.128/sqrt(k); f-independent per-level constants must have a divergent sum, so B20 must couple levels.  [opus/L2-level-two]
- Hamming balls: level-local budgets (B_r paid by level-r quantities) fail at every level r (B_0/Var ~ log n).  [opus/L2-level-two]
- Product references fail: Phi/I = a - 1 + O(1) on AND tensor powers while H/I < 4; majority shows the cancellation.  [opus/L2-level-two]
- Charging every edge to its upper endpoint loses a factor k+1.  [opus/L2-level-two]
- Level coarse-graining cannot prove B20: B <= K I is sum_i I(S_i; S - i) >= sum_i h2(eps_i) - K I, but on balanced tribes sum_i H(S_i | |S - i|)/I = log(1/eps) + 1.34 + o(1) while B/I -> 2; the size of S - i carries about 0.1 eps_i bits about S_i.  [opus/L2-level-two]
- On tribes one block is enough: with W_i = S cap (block(i) - i), B_i <= H(S_i | W_i) and sum_i H(S_i | W_i) <= (2 + O(w 2^-w)) I on balanced tribes (closed form; equals brute force to ten digits on six small cases).  [opus/L2-level-two]
- Lemma R: for a read-once formula over arbitrary gates, B_i = H(S_i | S - i) = H(S_i | tau, A) = phi(mu^2, fhat(i)^2) + sum_t alpha_t sum_{A nonempty} phi(P_t(A), P_t(A + c_t) rho_{>t}), where tau is the deepest path node whose subtree meets S - i and A the off-path children of v_tau that S meets. Corollary R1: the branch witness (tau, A) is exact; the height-s witness S cap (sub(v_s) - i) exceeds   [opus/L2-level-two]
- Corollary R2: if every gate of a read-once formula is an AND, an OR or a parity of literals (any fan-in), then B_i = H(S_i | tau_i), tau_i the height of the lowest ancestor of i whose subtree meets S - i. The gate laws have product form, so P_t(A + c_t)/P_t(A) does not depend on A and the cells of Lemma R merge without loss (1-homogeneity of phi). With majority gates it fails.  [opus/L2-level-two]
- Pivotal faces (elementary). With A_i the pivotal set of i and s(x) the sensitivity: (P1) an {i,j}-face is odd exactly when i is pivotal at one end of it and not the other, I(1_{A_i}) = sum_j P(E_ij) and P(E_ij) = 4 P(E_ij, A_i, A_j); (P2) Harper's inequality gives E[s - 1 | A_i] >= (1/2) log2(1/eps_i) (equality for AND_n) and h2(eps_i) <= eps_i log2 e + I(1_{A_i})/2; (P3) any set C of coordinates   [opus/L2-level-two]
- Blocks with signed-character fibers (elementary). If every fiber of F over an address block X is a signed character, F(x, y) = s(x) chi_{tau(x)}(y), then sum_{t in Y} B_t <= H(S_Y) = H(tau(X)) <= 2 I_X, with equality throughout for AND2^N = prod_k (-1)^{t_k (1 - y_k)} (Y the t bits). For any split, B_X = sum_T R_T B(nu_T) with R_T = P(S_Y = T) and nu_T the normalized spectral law of the slice F_T(  [opus/L2-level-two]
- K-partite polynomials (elementary). If [n] splits into K blocks and every monomial of the GF(2) polynomial of f = (-1)^P uses at most one variable of each block (the blocks properly colour the graph joining two coordinates that share a monomial), then B <= H <= sum_k H(S_{X_k}) <= 2 sum_k I_{X_{-k}} = 2 (K - 1) I. Every block then has signed-character fibers, and this is exactly the class on which  [opus/L2-level-two]

### CERTIFIED (14)
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse]
-   [fleet/claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion]
-   [fleet/claude/B07/runs/20261011T230024Z-claude-B07-two-address-census]
-   [fleet/claude/B07/runs/20261011T230024Z-claude-B07-two-address-census]
-   [fleet/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring]
-   [fleet/claude/B12/runs/20261011T225832Z-claude-B12-erasure-ledger-depth]
-   [fleet/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge]
-   [fleet/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge]
-   [fleet/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]
-   [fleet/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit]
-   [fleet/claude/B19/runs/20261011T224700Z-claude-B19-paper-audit-rankcode]

### CERTIFIED_AUTHOR_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard]

### CERTIFIED_FINITE_COMPUTATION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/claude/B06/runs/20261011T223800Z-claude-B06-block-tree-reductions]

### CERTIFIED_LOCALLY_REVIEW_PENDING (COMPUTER-ASSISTED: MPMATH INTERVAL ARITHMETIC) (1)
-   [fleet/claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax]

### CHECKED_EVIDENCE (1)
-   [fleet/claude/B19/runs/20261011T224700Z-claude-B19-paper-audit-rankcode]

### CORRECTED_SUBCLAIM_ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A046/runs/20261011T232847Z-fleet05-A046-current-candidate-intake]

### CORRECTED_VALID_CLAUSES_INDEPENDENTLY_RECONSTRUCTED; EXTRA_COUPLED_ASSERTION_WITHDRAWN (1)
-   [fleet/agents/A034/runs/20261014T055220Z-fleet05-A034-phase-energy-transfer]

### ERROR_V1_REMAINDER_SIGN_ACCEPTANCE_WITHDRAWN (1)
-   [fleet/agents/A087/runs/20261012T004155Z-fleet05-A087-restriction-referee]

### EXACTLY_CERTIFIED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A032/runs/20261011T234647Z-fleet05-A032-boolean-phase-realizability]

### EXACTLY_CERTIFIED_SCOPED_ADAPTER_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A081/runs/20261014T013521Z-fleet05-A081-dependency-certificates]

### EXACTLY_VALIDATED_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (4)
-   [fleet/agents/A081/runs/20261013T220111Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261014T013521Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261014T042148Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261014T092812Z-fleet05-A081-dependency-certificates]

### EXACT_BOOLEAN_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A068/runs/20261013T234128Z-fleet05-A068-antichain-beyond-one-order]

### EXACT_BOOLEAN_SCOPE_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A088/runs/20261012T024518Z-fleet05-A088-booleanity-referee]

### EXACT_COUNTEREXAMPLE_AND_SCOPED_REPAIR_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A085/runs/20261013T213517Z-fleet05-A085-certificate-adversary]

### EXACT_FINITE_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A051/runs/20261011T233123Z-fleet05-A051-near-extremizer-definition]

### EXACT_FINITE_CERTIFICATE_COMPLETE_PENDING_INDEPENDENT_REVIEW; PRIOR_SCOPES_PRESERVED (1)
-   [fleet/agents/A023/runs/20261014T051414Z-fleet05-A023-amortized-rarity-budget]

### EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (6)
-   [fleet/agents/A071/runs/20261011T214639Z-fleet05-A071-search-space-design]
-   [fleet/agents/A071/runs/20261011T233808Z-fleet05-A071-search-space-design]
-   [fleet/agents/A072/runs/20261012T004036Z-fleet05-A072-exact-walsh-engine]
-   [fleet/agents/A073/runs/20261011T222436Z-fleet05-A073-certified-logarithms]
-   [fleet/agents/A074/runs/20261011T224717Z-fleet05-A074-independent-reproducer]
-   [fleet/claude/B15/runs/20261011T225100Z-claude-B15-erasure-countersearch]

### EXACT_FINITE_HISTORY_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A081/runs/20261014T092812Z-fleet05-A081-dependency-certificates]

### EXACT_LOCAL_LEDGER_TEST_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A081/runs/20261014T042148Z-fleet05-A081-dependency-certificates]

### EXACT_V1_STATEMENT_HOLDS; ERRONEOUS_ADDITIONAL_REPORT_SIGNS_EXCLUDED (1)
-   [fleet/agents/A023/runs/20261012T010933Z-fleet05-A023-amortized-rarity-budget]

### EXHAUSTIVE_FLOAT64_WITH_CLOSED_FORM_MAXIMA (1)
-   [fleet/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich]

### EXISTING_INTERFACE_SCOPE_OBJECTION_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A048/runs/20261014T022727Z-fleet05-A048-tensor-stress]

### EXISTING_INTERFACE_WIDTH_PAYMENT_CLOSED_AUTHOR_PROVED_REVIEW_PENDING (1)
-   [fleet/agents/A046/runs/20261014T041928Z-fleet05-A046-current-candidate-intake]

### EXISTING_REFUTATION_EXTRACTED_AND_CHECKED_LOCAL_REVIEW_PENDING (1)
-   [fleet/agents/A049/runs/20261011T224133Z-fleet05-A049-minimal-falsifier-extraction]

### EXISTING_REPAIR_ADMISSION_AND_TERMINAL_SCOPE_AUDIT_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A048/runs/20261014T052201Z-fleet05-A048-tensor-stress]

### EXISTING_SCOPE_OBJECTION_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A048/runs/20261013T234007Z-fleet05-A048-tensor-stress]

### FINITE_ALGEBRAIC_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A072/runs/20261011T220909Z-fleet05-A072-exact-walsh-engine]

### FINITE_CERTIFICATE_AND_ANALYTIC_BOUNDARY_PROOF_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A043/runs/20261012T012726Z-fleet05-A043-prime-gate-decomposition]

### FINITE_CERTIFIED_AUTHOR_PENDING_INDEPENDENT_REVIEW (3)
-   [fleet/agents/A010/runs/20261011T225444Z-fleet05-A010-universal-residual-falsifier]
-   [fleet/agents/A010/runs/20261012T044209Z-fleet05-A010-universal-residual-falsifier]
-   [fleet/agents/A010/runs/20261012T044209Z-fleet05-A010-universal-residual-falsifier]

### FINITE_COUNTEREXAMPLE_CERTIFIED_WITH_INDEPENDENT_REPAIR (2)
-   [fleet/agents/A073/runs/20261011T222436Z-fleet05-A073-certified-logarithms]
-   [fleet/agents/A074/runs/20261011T224717Z-fleet05-A074-independent-reproducer]

### FINITE_DOMAIN_EXACT_CERTIFICATE_AND_LEDGER_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A004/runs/20261014T054158Z-fleet05-A004-constant-and-unit-ledger]

### FINITE_EXISTING_HELPER_VERIFICATION_COMPLETE_LOCAL_REVIEW_PENDING (1)
-   [fleet/agents/A049/runs/20261013T235808Z-fleet05-A049-minimal-falsifier-extraction]

### FINITE_GUARDED_REPAIR_PROVED_WITH_EXACT_CERTIFICATES_REVIEW_PENDING (1)
-   [fleet/agents/A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine]

### FINITE_REFINEMENT_CERTIFIED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A032/runs/20261013T221334Z-fleet05-A032-boolean-phase-realizability]

### FOCUSED_INTERFACE_EXTENSION_PROVED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A056/runs/20261011T233147Z-fleet05-A056-balanced-composition]

### FORMAL_CLAIM_INDEPENDENTLY_ACCEPTED_AUXILIARY_SOURCE_CORRECTED_LOCAL_ADOPTION_PENDING (1)
-   [fleet/agents/A008/runs/20261014T021605Z-fleet05-A008-gate-label-compression]

### FORMAL_CLAIM_INDEPENDENTLY_ACCEPTED_LOCALLY_AUXILIARY_SOURCE_ERROR_RECORDED_ADOPTION_PENDING (1)
-   [fleet/agents/A006/runs/20261014T011124Z-fleet05-A006-posterior-forest-optimization]

### FULL_EXACT_LOCAL_CLAIM_INDEPENDENTLY_REVIEWED_LOCAL_RECORD_PENDING_SUPERVISOR_ADOPTION (1)
-   [fleet/agents/A045/runs/20261014T063646Z-fleet05-A045-biased-realizability-referee]

### FULL_NARROW_OBSTRUCTION_INDEPENDENTLY_RECONSTRUCTED_LOCALLY; ORIGINAL_UNCHANGED (1)
-   [fleet/agents/A042/runs/20261014T112104Z-fleet05-A042-bias-endpoint-certificates]

### GAP_AT_STATED_BOUNDARY_LOCAL_REVIEW_PENDING_B20 (1)
-   [fleet/agents/A070/runs/20261013T212602Z-fleet05-A070-analytic-route-referee]

### GAP_SCOPE_UNQUALIFIED_BLOCK_TREE_BUDGET; SINGLETON_COMPONENT_VALID (1)
-   [fleet/agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement]

### GLOBAL_UPPER_THEOREM_AND_PAIR_TRIPLE_LEDGER_INDEPENDENTLY_REVIEWED_LOCALLY; OTHER_BUNDLED_CLAUSES_NOT_REVIEWED_HERE; ORIGINAL_UNCHANGED (1)
-   [fleet/agents/A044/runs/20261014T055346Z-fleet05-A044-non-symmetric-gate-classes]

### HOLDS_SOURCE_BOUND_INDEPENDENT_RECONSTRUCTION_BY_A087 (1)
-   [fleet/agents/A087/runs/20261013T222530Z-fleet05-A087-restriction-referee]

### INDEPENDENTLY_ACCEPTED (6)
-   [fleet/agents/A072/runs/20261014T044904Z-fleet05-A072-exact-walsh-engine]
-   [fleet/agents/A072/runs/20261014T124911Z-fleet05-A072-exact-walsh-engine]
-   [fleet/agents/A074/runs/20261014T030615Z-fleet05-A074-independent-reproducer]
-   [fleet/agents/A074/runs/20261014T060751Z-fleet05-A074-independent-reproducer]
-   [fleet/agents/A080/runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard]
-   [fleet/agents/A080/runs/20261014T074729Z-fleet05-A080-universal-counterexample-standard]

### INDEPENDENTLY_ACCEPTED_AT_ENTIRE_ORIGINAL_SCOPE_BY_A081 (2)
-   [fleet/agents/A081/runs/20261014T092812Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261014T092812Z-fleet05-A081-dependency-certificates]

### INDEPENDENTLY_ACCEPTED_AT_ENTIRE_STATED_SCOPE_BY_A081 (1)
-   [fleet/agents/A081/runs/20261014T042148Z-fleet05-A081-dependency-certificates]

### INDEPENDENTLY_ACCEPTED_AT_EXACT_STATED_SCOPE (1)
-   [fleet/agents/A057/runs/20261014T124811Z-fleet05-A057-coherent-restriction-remainder]

### INDEPENDENTLY_ACCEPTED_AT_EXPLICIT_ORIGINAL_SCOPE_BY_A100 (2)
-   [fleet/agents/A100/runs/20261014T010218Z-fleet05-A100-release-and-continuation-ledger]
-   [fleet/agents/A100/runs/20261014T010218Z-fleet05-A100-release-and-continuation-ledger]

### INDEPENDENTLY_ACCEPTED_AT_FULL_ORIGINAL_SCOPE_BY_A090_LOCAL_ADOPTION_PENDING (2)
-   [fleet/agents/A081/runs/20261014T092812Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A090/runs/20261014T074809Z-fleet05-A090-independent-reconstruction]

### INDEPENDENTLY_ACCEPTED_AT_FULL_ORIGINAL_SCOPE_BY_A100 (1)
-   [fleet/agents/A100/runs/20261014T034838Z-fleet05-A100-release-and-continuation-ledger]

### INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A066 (1)
-   [fleet/agents/A066/runs/20261014T042048Z-fleet05-A066-semigroup-dissipation]

### INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A073_AND_A001_LOCAL_ADOPTION_PENDING (3)
-   [fleet/agents/A001/runs/20261014T011101Z-fleet05-A001-quantifier-audit]
-   [fleet/agents/A081/runs/20261014T013521Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A096/runs/20261014T013836Z-fleet05-A096-live-gap-ledger]

### INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A073_LOCAL_ADOPTION_PENDING (6)
-   [fleet/agents/A073/runs/20261014T023508Z-fleet05-A073-certified-logarithms]
-   [fleet/agents/A073/runs/20261014T053433Z-fleet05-A073-certified-logarithms]
-   [fleet/agents/A085/runs/20261014T074749Z-fleet05-A085-certificate-adversary]
-   [fleet/agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A096_LOCAL_ADOPTION_PENDING (2)
-   [fleet/agents/A090/runs/20261014T074809Z-fleet05-A090-independent-reconstruction]
-   [fleet/agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger]

### INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A098_LOCAL_ADOPTION_PENDING (4)
-   [fleet/agents/A001/runs/20261014T035113Z-fleet05-A001-quantifier-audit]
-   [fleet/agents/A098/runs/20261014T024504Z-fleet05-A098-resource-reallocation]
-   [fleet/agents/A098/runs/20261014T054007Z-fleet05-A098-resource-reallocation]
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]

### INDEPENDENTLY_ACCEPTED_AT_STATED_FINITE_SCOPE_BY_A073 (1)
-   [fleet/agents/A073/runs/20261013T234148Z-fleet05-A073-certified-logarithms]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE (7)
-   [fleet/agents/A048/runs/20261014T022727Z-fleet05-A048-tensor-stress]
-   [fleet/agents/A048/runs/20261014T052201Z-fleet05-A048-tensor-stress]
-   [fleet/agents/A057/runs/20261014T044759Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A092/runs/20261013T222550Z-fleet05-A092-counterexample-referee]
-   [fleet/agents/A092/runs/20261014T020903Z-fleet05-A092-counterexample-referee]
-   [fleet/agents/A092/runs/20261014T020903Z-fleet05-A092-counterexample-referee]
-   [fleet/agents/A092/runs/20261014T045641Z-fleet05-A092-counterexample-referee]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_A075_LOCAL_RECORD (2)
-   [fleet/agents/A075/runs/20261014T005346Z-fleet05-A075-search-to-theorem-bridge]
-   [fleet/agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A018 (3)
-   [fleet/agents/A018/runs/20261012T010436Z-fleet05-A018-shared-data-collision-law]
-   [fleet/agents/A018/runs/20261012T010436Z-fleet05-A018-shared-data-collision-law]
-   [fleet/agents/A018/runs/20261012T010436Z-fleet05-A018-shared-data-collision-law]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A047 (3)
-   [fleet/agents/A047/runs/20261014T015314Z-fleet05-A047-boundary-search]
-   [fleet/agents/A047/runs/20261014T044331Z-fleet05-A047-boundary-search]
-   [fleet/agents/A047/runs/20261014T124731Z-fleet05-A047-boundary-search]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A050 (1)
-   [fleet/agents/A050/runs/20261014T063752Z-fleet05-A050-repair-with-scope]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A066 (1)
-   [fleet/agents/A066/runs/20261014T012949Z-fleet05-A066-semigroup-dissipation]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A067_LOCAL_RECEIPT (5)
-   [fleet/agents/A067/runs/20261014T020120Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261014T020120Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261014T044841Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261014T044841Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261014T044841Z-fleet05-A067-hypercontractive-refinement]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A073 (1)
-   [fleet/agents/A073/runs/20261013T234148Z-fleet05-A073-certified-logarithms]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A081 (3)
-   [fleet/agents/A081/runs/20261013T220111Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261013T220111Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261014T013521Z-fleet05-A081-dependency-certificates]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A087 (25)
-   [fleet/agents/A027/runs/20261011T234627Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261011T234627Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261013T221314Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261013T221314Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T015108Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T015108Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T043519Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T043519Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T104101Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T104101Z-fleet05-A027-block-selection]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261012T004155Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261012T004155Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261012T004155Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261014T020842Z-fleet05-A087-restriction-referee]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A090 (4)
-   [fleet/agents/A090/runs/20261011T231429Z-fleet05-A090-independent-reconstruction]
-   [fleet/agents/A090/runs/20261011T231429Z-fleet05-A090-independent-reconstruction]
-   [fleet/agents/A090/runs/20261013T213537Z-fleet05-A090-independent-reconstruction]
-   [fleet/agents/A096/runs/20261011T234252Z-fleet05-A096-live-gap-ledger]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A096 (1)
-   [fleet/agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A098 (2)
-   [fleet/agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A098/runs/20261012T024601Z-fleet05-A098-resource-reallocation]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A098_AND_A085_LOCAL_ADOPTION_PENDING (1)
-   [fleet/agents/A085/runs/20261014T034606Z-fleet05-A085-certificate-adversary]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A100 (1)
-   [fleet/agents/A100/runs/20261013T213917Z-fleet05-A100-release-and-continuation-ledger]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL (2)
-   [fleet/agents/A060/runs/20261013T212522Z-fleet05-A060-composition-sharpness]
-   [fleet/agents/A060/runs/20261013T212522Z-fleet05-A060-composition-sharpness]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING (4)
-   [fleet/agents/A028/runs/20261011T221633Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A028/runs/20261011T221633Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A028/runs/20261011T221633Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A028/runs/20261011T221633Z-fleet05-A028-stopping-tree-payment]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT (12)
-   [fleet/agents/A067/runs/20261012T004014Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261012T004014Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261012T004014Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A067/runs/20261014T044841Z-fleet05-A067-hypercontractive-refinement]
-   [fleet/agents/A088/runs/20261013T234248Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261014T024038Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261014T024038Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_REVIEW (3)
-   [fleet/agents/A074/runs/20261012T043949Z-fleet05-A074-independent-reproducer]
-   [fleet/agents/A074/runs/20261012T043949Z-fleet05-A074-independent-reproducer]
-   [fleet/agents/A074/runs/20261014T000656Z-fleet05-A074-independent-reproducer]

### INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_REVIEW_RECORD (1)
-   [fleet/agents/A046/runs/20261013T215251Z-fleet05-A046-current-candidate-intake]

### INDEPENDENTLY_ACCEPTED_AT_UNCHANGED_SCOPE_A071_LOCAL_RECORD (1)
-   [fleet/agents/A071/runs/20261014T042108Z-fleet05-A071-search-space-design]

### INDEPENDENTLY_ACCEPTED_AT_UNCHANGED_SCOPE_A071_LOCAL_RECORD_FULL_FEI_OPEN (1)
-   [fleet/agents/A071/runs/20261014T090502Z-fleet05-A071-search-space-design]

### INDEPENDENTLY_ACCEPTED_BY_A067_RECEIPT_CONSUMED_PENDING_B20 (2)
-   [fleet/agents/A070/runs/20261014T005025Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261014T005025Z-fleet05-A070-analytic-route-referee]

### INDEPENDENTLY_ACCEPTED_BY_A070_AT_FULL_SCOPE_PENDING_B20 (1)
-   [fleet/agents/A070/runs/20261014T034205Z-fleet05-A070-analytic-route-referee]

### INDEPENDENTLY_ACCEPTED_BY_A070_AT_SCOPE_PENDING_B20 (1)
-   [fleet/agents/A070/runs/20261014T005025Z-fleet05-A070-analytic-route-referee]

### INDEPENDENTLY_ACCEPTED_BY_A082_LOCAL_ADOPTION_PENDING (3)
-   [fleet/agents/A081/runs/20261014T092812Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A082/runs/20261014T045125Z-fleet05-A082-finite-inequalities]
-   [fleet/agents/A082/runs/20261014T045125Z-fleet05-A082-finite-inequalities]

### INDEPENDENTLY_ACCEPTED_LOCAL (1)
-   [fleet/agents/A013/runs/20261012T010150Z-fleet05-A013-representation-stability]

### INDEPENDENTLY_ACCEPTED_LOCALLY; UNIVERSAL_EXTENSION_OPEN (1)
-   [fleet/agents/A006/runs/20261014T074929Z-fleet05-A006-posterior-forest-optimization]

### INDEPENDENTLY_ACCEPTED_LOCALLY; UNIVERSAL_OPEN (1)
-   [fleet/agents/A010/runs/20261014T062324Z-fleet05-A010-universal-residual-falsifier]

### INDEPENDENTLY_ACCEPTED_LOCALLY_BY_A010; REGISTRY_ADOPTION_UNVERIFIED (1)
-   [fleet/agents/A010/runs/20261014T031741Z-fleet05-A010-universal-residual-falsifier]

### INDEPENDENTLY_ACCEPTED_LOCAL_ADOPTION_PENDING (2)
-   [fleet/agents/A012/runs/20261014T014452Z-fleet05-A012-sparse-activation-accounting]
-   [fleet/agents/A013/runs/20261013T222840Z-fleet05-A013-representation-stability]

### INDEPENDENTLY_ACCEPTED_LOCAL_BY_A004_AT_FULL_SOURCE_SCOPE_ADOPTION_PENDING (1)
-   [fleet/agents/A004/runs/20261014T024610Z-fleet05-A004-constant-and-unit-ledger]

### INDEPENDENTLY_ACCEPTED_LOCAL_BY_A004_NEW_POINT_BOUND_SOURCE_ADOPTION_PENDING (1)
-   [fleet/agents/A004/runs/20261014T054158Z-fleet05-A004-constant-and-unit-ledger]

### INDEPENDENTLY_ACCEPTED_LOCAL_ONE_REVIEW_AT_STATED_SCOPE (2)
-   [fleet/agents/A004/runs/20261013T235034Z-fleet05-A004-constant-and-unit-ledger]
-   [fleet/agents/A004/runs/20261013T235034Z-fleet05-A004-constant-and-unit-ledger]

### INDEPENDENTLY_ACCEPTED_LOCAL_RECEIPT_PENDING_B20 (6)
-   [fleet/agents/A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee]
-   [fleet/agents/A070/runs/20261013T212602Z-fleet05-A070-analytic-route-referee]

### INDEPENDENTLY_ACCEPTED_LOW_INFLUENCE_FRAGMENT_BY_A081 (1)
-   [fleet/agents/A081/runs/20261013T220111Z-fleet05-A081-dependency-certificates]

### INDEPENDENTLY_ACCEPTED_SOURCE_THEOREM_UPSTREAM_ID_AND_PACKAGE_PENDING (1)
-   [fleet/agents/A070/runs/20261013T212602Z-fleet05-A070-analytic-route-referee]

### INDEPENDENTLY_RECONSTRUCTED_ACCEPTED_LOCALLY (1)
-   [fleet/agents/A007/runs/20261011T234502Z-fleet05-A007-root-normalization]

### INDEPENDENTLY_RECONSTRUCTED_ACCEPTED_LOCALLY_ADOPTION_PENDING (1)
-   [fleet/agents/A008/runs/20261012T005959Z-fleet05-A008-gate-label-compression]

### INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE (1)
-   [fleet/agents/A063/runs/20261011T222159Z-fleet05-A063-information-revelation]

### INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION (24)
-   [fleet/agents/A031/runs/20261011T232738Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261011T232738Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261011T232738Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261011T232738Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261013T215020Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261013T215020Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A031/runs/20261014T011913Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A035/runs/20261013T212341Z-fleet05-A035-signed-cancellation-countersearch]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261012T024518Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261012T024518Z-fleet05-A088-booleanity-referee]
-   [fleet/agents/A088/runs/20261012T024518Z-fleet05-A088-booleanity-referee]

### INDEPENDENTLY_RECONSTRUCTED_AT_EXACT_A005_STATEMENT_SCOPE (2)
-   [fleet/agents/A002/runs/20261014T013942Z-fleet05-A002-hardness-preserving-transformations]
-   [fleet/agents/A005/runs/20261014T031720Z-fleet05-A005-noncircular-endpoint-referee]

### INDEPENDENTLY_RECONSTRUCTED_AT_EXACT_STATEMENT_SCOPE (2)
-   [fleet/agents/A005/runs/20261014T031720Z-fleet05-A005-noncircular-endpoint-referee]
-   [fleet/agents/A005/runs/20261014T061827Z-fleet05-A005-noncircular-endpoint-referee]

### INDEPENDENTLY_RECONSTRUCTED_AT_FULL_STATED_SCOPE_LOCAL (3)
-   [fleet/agents/A011/runs/20261014T074949Z-fleet05-A011-representation-existence]
-   [fleet/agents/A086/runs/20261014T013711Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261014T042208Z-fleet05-A086-joint-code-referee]

### INDEPENDENTLY_RECONSTRUCTED_AT_FULL_STATED_SCOPE_LOCALLY (9)
-   [fleet/agents/A086/runs/20261014T042208Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261014T093519Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261014T093519Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261014T093519Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A094/runs/20261014T031253Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261014T031253Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261014T061347Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261014T061347Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A095/runs/20261014T034647Z-fleet05-A095-restricted-result-extraction]

### INDEPENDENTLY_RECONSTRUCTED_AT_ORIGINAL_SCOPE_LOCAL_ADOPTION_PENDING (2)
-   [fleet/agents/A009/runs/20261014T024630Z-fleet05-A009-fractional-incidence-optimization]
-   [fleet/agents/A015/runs/20261012T044229Z-fleet05-A015-minterm-barrier-analysis]

### INDEPENDENTLY_RECONSTRUCTED_AT_SCOPED_APPLICATION_STATEMENT (1)
-   [fleet/agents/A002/runs/20261014T043038Z-fleet05-A002-hardness-preserving-transformations]

### INDEPENDENTLY_RECONSTRUCTED_AT_SCOPE_BY_A068_REGISTRY_ADOPTION_PENDING (1)
-   [fleet/agents/A068/runs/20261014T023317Z-fleet05-A068-antichain-beyond-one-order]

### INDEPENDENTLY_RECONSTRUCTED_AT_SOURCE_SCOPE (1)
-   [fleet/agents/A093/runs/20261014T053944Z-fleet05-A093-literature-and-priority]

### INDEPENDENTLY_RECONSTRUCTED_AT_STATED_ANALYTIC_SCOPE_BY_A055 (1)
-   [fleet/agents/A055/runs/20261014T004129Z-fleet05-A055-extremal-obstruction-referee]

### INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE (8)
-   [fleet/agents/A002/runs/20261013T220534Z-fleet05-A002-hardness-preserving-transformations]
-   [fleet/agents/A005/runs/20261012T044149Z-fleet05-A005-noncircular-endpoint-referee]
-   [fleet/agents/A005/runs/20261012T044149Z-fleet05-A005-noncircular-endpoint-referee]
-   [fleet/agents/A079/runs/20261012T044009Z-fleet05-A079-correlated-auxiliaries]
-   [fleet/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates]

### INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL (4)
-   [fleet/agents/A032/runs/20261014T043539Z-fleet05-A032-boolean-phase-realizability]
-   [fleet/agents/A032/runs/20261014T105923Z-fleet05-A032-boolean-phase-realizability]
-   [fleet/agents/A086/runs/20261013T220217Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261013T220217Z-fleet05-A086-joint-code-referee]

### INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING (11)
-   [fleet/agents/A006/runs/20261011T231903Z-fleet05-A006-posterior-forest-optimization]
-   [fleet/agents/A006/runs/20261013T214427Z-fleet05-A006-posterior-forest-optimization]
-   [fleet/agents/A007/runs/20261013T220854Z-fleet05-A007-root-normalization]
-   [fleet/agents/A007/runs/20261014T043228Z-fleet05-A007-root-normalization]
-   [fleet/agents/A008/runs/20261013T222820Z-fleet05-A008-gate-label-compression]
-   [fleet/agents/A008/runs/20261013T222820Z-fleet05-A008-gate-label-compression]
-   [fleet/agents/A008/runs/20261014T021605Z-fleet05-A008-gate-label-compression]
-   [fleet/agents/A008/runs/20261014T050954Z-fleet05-A008-gate-label-compression]
-   [fleet/agents/A009/runs/20261013T235139Z-fleet05-A009-fractional-incidence-optimization]
-   [fleet/agents/A015/runs/20261014T001450Z-fleet05-A015-minterm-barrier-analysis]
-   [fleet/agents/A015/runs/20261014T031846Z-fleet05-A015-minterm-barrier-analysis]

### INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_REVIEW_RECORD (1)
-   [fleet/agents/A082/runs/20261012T004123Z-fleet05-A082-finite-inequalities]

### INDEPENDENTLY_RECONSTRUCTED_BY_A032_PENDING_REGISTRY_ADOPTION (1)
-   [fleet/agents/A079/runs/20261014T060856Z-fleet05-A079-correlated-auxiliaries]

### INDEPENDENTLY_RECONSTRUCTED_BY_A034_PENDING_REGISTRY_ADOPTION (1)
-   [fleet/agents/A034/runs/20261014T055220Z-fleet05-A034-phase-energy-transfer]

### INDEPENDENTLY_RECONSTRUCTED_BY_A079_PENDING_REGISTRY_ADOPTION (1)
-   [fleet/agents/A079/runs/20261014T060856Z-fleet05-A079-correlated-auxiliaries]

### INDEPENDENTLY_RECONSTRUCTED_DOWNSTREAM_SCOPE_LOCAL_ADOPTION_PENDING (2)
-   [fleet/agents/A007/runs/20261014T100124Z-fleet05-A007-root-normalization]
-   [fleet/agents/A015/runs/20261014T062347Z-fleet05-A015-minterm-barrier-analysis]

### INDEPENDENTLY_RECONSTRUCTED_FORMAL_SCOPE_LOCAL_ADOPTION_PENDING (1)
-   [fleet/agents/A007/runs/20261014T014217Z-fleet05-A007-root-normalization]

### INDEPENDENTLY_RECONSTRUCTED_FULL_NARROW_SCOPE_LOCALLY; ORIGINAL_UNCHANGED (1)
-   [fleet/agents/A042/runs/20261014T044053Z-fleet05-A042-bias-endpoint-certificates]

### INDEPENDENTLY_RECONSTRUCTED_FULL_STATED_FINITE_INTERFACE_HOLDS_BY_A061 (1)
-   [fleet/agents/A061/runs/20261014T085352Z-fleet05-A061-entropy-process]

### INDEPENDENTLY_RECONSTRUCTED_FULL_STATED_NARROW_SCOPE_LOCALLY; ORIGINAL_SOURCE_UNCHANGED (1)
-   [fleet/agents/A043/runs/20261014T052009Z-fleet05-A043-prime-gate-decomposition]

### INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE_BY_A087 (4)
-   [fleet/agents/A064/runs/20261014T060409Z-fleet05-A064-global-debt-potential]
-   [fleet/agents/A087/runs/20261014T045317Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261014T045317Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261014T045317Z-fleet05-A087-restriction-referee]

### INDEPENDENTLY_RECONSTRUCTED_HOLDS_BY_A064 (2)
-   [fleet/agents/A064/runs/20261013T235917Z-fleet05-A064-global-debt-potential]
-   [fleet/agents/A064/runs/20261014T030103Z-fleet05-A064-global-debt-potential]

### INDEPENDENTLY_RECONSTRUCTED_LOCALLY_AT_FULL_STATED_NARROW_SCOPE; ORIGINAL_SOURCE_UNCHANGED (1)
-   [fleet/agents/A043/runs/20261014T022706Z-fleet05-A043-prime-gate-decomposition]

### INDEPENDENTLY_RECONSTRUCTED_LOCALLY_BY_A010; REGISTRY_ADOPTION_UNVERIFIED (1)
-   [fleet/agents/A010/runs/20261014T001430Z-fleet05-A010-universal-residual-falsifier]

### INDEPENDENTLY_RECONSTRUCTED_LOCAL_BY_A003_ADOPTION_PENDING (2)
-   [fleet/agents/A003/runs/20261014T050612Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A004/runs/20261014T054158Z-fleet05-A004-constant-and-unit-ledger]

### INDEPENDENTLY_RECONSTRUCTED_PENDING_REGISTRY_ADOPTION (1)
-   [fleet/agents/A079/runs/20261014T030635Z-fleet05-A079-correlated-auxiliaries]

### INDEPENDENTLY_REVIEWED_ACCEPTED_AT_STATED_SCOPE (11)
-   [fleet/agents/A057/runs/20261013T221645Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261014T015740Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A060/runs/20261014T033739Z-fleet05-A060-composition-sharpness]
-   [fleet/agents/A091/runs/20261011T214848Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261011T214848Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261013T220323Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T013816Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T042228Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T042228Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T042228Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T094139Z-fleet05-A091-composition-referee]

### INDEPENDENTLY_REVIEWED_AT_CAP_AND_COHERENT_SCOPE (1)
-   [fleet/agents/A057/runs/20261014T015740Z-fleet05-A057-coherent-restriction-remainder]

### INDEPENDENTLY_REVIEWED_AT_EXACT_SCOPE_LOCAL_RECORD_PENDING_SUPERVISOR_ADOPTION (1)
-   [fleet/agents/A045/runs/20261014T033253Z-fleet05-A045-biased-realizability-referee]

### INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE (14)
-   [fleet/agents/A042/runs/20261012T002547Z-fleet05-A042-bias-endpoint-certificates]
-   [fleet/agents/A045/runs/20261013T212421Z-fleet05-A045-biased-realizability-referee]
-   [fleet/agents/A085/runs/20261011T231324Z-fleet05-A085-certificate-adversary]
-   [fleet/agents/A085/runs/20261011T231324Z-fleet05-A085-certificate-adversary]
-   [fleet/agents/A085/runs/20261011T231324Z-fleet05-A085-certificate-adversary]
-   [fleet/agents/A085/runs/20261013T213517Z-fleet05-A085-certificate-adversary]
-   [fleet/agents/A086/runs/20261011T214823Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261011T214823Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261011T214823Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261011T234041Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261011T234041Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261011T234041Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261011T234041Z-fleet05-A086-joint-code-referee]
-   [fleet/agents/A086/runs/20261011T234041Z-fleet05-A086-joint-code-referee]

### INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE_LOCALLY (6)
-   [fleet/agents/A081/runs/20261014T013521Z-fleet05-A081-dependency-certificates]
-   [fleet/agents/A094/runs/20261012T044109Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261012T044109Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261012T044109Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261014T001244Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261014T001244Z-fleet05-A094-proof-chain-challenger]

### INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE_LOCAL_RECORD_PENDING_SUPERVISOR_ADOPTION (4)
-   [fleet/agents/A041/runs/20261013T215146Z-fleet05-A041-weighted-threshold-fei]
-   [fleet/agents/A041/runs/20261014T012508Z-fleet05-A041-weighted-threshold-fei]
-   [fleet/agents/A042/runs/20261013T221414Z-fleet05-A042-bias-endpoint-certificates]
-   [fleet/agents/A045/runs/20261014T004049Z-fleet05-A045-biased-realizability-referee]

### INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE_PENDING_REGISTRY_ADOPTION (2)
-   [fleet/agents/A055/runs/20261011T230118Z-fleet05-A055-extremal-obstruction-referee]
-   [fleet/agents/A055/runs/20261013T212502Z-fleet05-A055-extremal-obstruction-referee]

### INDEPENDENTLY_REVIEWED_HOLDS_AT_STATED_FIRST_QUERY_SCOPE_FULL_FEI_OPEN (1)
-   [fleet/agents/A075/runs/20261014T074708Z-fleet05-A075-search-to-theorem-bridge]

### INDEPENDENTLY_REVIEWED_LOCALLY_ACCEPT_AT_STATED_SCOPE (2)
-   [fleet/agents/A023/runs/20261011T221608Z-fleet05-A023-amortized-rarity-budget]
-   [fleet/agents/A023/runs/20261011T221608Z-fleet05-A023-amortized-rarity-budget]

### INDEPENDENTLY_REVIEWED_LOCALLY_BY_A039 (3)
-   [fleet/agents/A038/runs/20261014T051947Z-fleet05-A038-occupancy-term-audit]
-   [fleet/agents/A039/runs/20261014T025407Z-fleet05-A039-projection-under-restrictions]
-   [fleet/agents/A039/runs/20261014T055326Z-fleet05-A039-projection-under-restrictions]

### INDEPENDENTLY_REVIEWED_LOCALLY_PENDING_SHARED_ADOPTION (2)
-   [fleet/agents/A037/runs/20261014T043944Z-fleet05-A037-conditional-credit-ledger]
-   [fleet/agents/A037/runs/20261014T043944Z-fleet05-A037-conditional-credit-ledger]

### INDEPENDENTLY_REVIEWED_LOCAL_ACCEPTANCE (1)
-   [fleet/agents/A080/runs/20261013T212642Z-fleet05-A080-universal-counterexample-standard]

### INDEPENDENT_A018_AND_A020_HOLDS_AT_FULL_STATED_SCOPE; SHARED_ADOPTION_PENDING (1)
-   [fleet/agents/A019/runs/20261014T055119Z-fleet05-A019-orthogonality-extensions]

### INDEPENDENT_A018_HOLDS_AT_STATED_SCOPE; SHARED_ADOPTION_PENDING (1)
-   [fleet/agents/A018/runs/20261014T051305Z-fleet05-A018-shared-data-collision-law]

### INDEPENDENT_A018_HOLDS_AT_STATED_SCOPE; SUPERVISOR_ADOPTION_PENDING (2)
-   [fleet/agents/A018/runs/20261013T222945Z-fleet05-A018-shared-data-collision-law]
-   [fleet/agents/A018/runs/20261014T022025Z-fleet05-A018-shared-data-collision-law]

### INDEPENDENT_ACCEPTANCE_BY_A075_CONSUMED_WITH_SOURCE_PROVENANCE (1)
-   [fleet/agents/A084/runs/20261014T030826Z-fleet05-A084-continuum-parameters]

### INDEPENDENT_NEW_CONTROLLER_CLAUSE_AND_GLOBAL_ASSEMBLY_HOLDS_BY_A061 (1)
-   [fleet/agents/A061/runs/20261014T042028Z-fleet05-A061-entropy-process]

### INDEPENDENT_RECONSTRUCTION_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION (2)
-   [fleet/agents/A033/runs/20261011T221704Z-fleet05-A033-derivative-hierarchy]
-   [fleet/agents/A033/runs/20261011T221704Z-fleet05-A033-derivative-hierarchy]

### INDEPENDENT_REVIEW_A064_RECEIPT_CONSUMED_AT_EXACT_SCOPE (2)
-   [fleet/agents/A087/runs/20261014T020842Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261014T045317Z-fleet05-A087-restriction-referee]

### INDEPENDENT_REVIEW_CONSUMED_LOCAL_RECORD_PENDING_SUPERVISOR_ADOPTION (2)
-   [fleet/agents/A041/runs/20261014T012508Z-fleet05-A041-weighted-threshold-fei]
-   [fleet/agents/A045/runs/20261014T033253Z-fleet05-A045-biased-realizability-referee]

### INDEPENDENT_REVIEW_HOLDS (5)
-   [fleet/agents/A040/runs/20261014T033148Z-fleet05-A040-credit-insufficiency-tests]
-   [fleet/agents/A040/runs/20261014T063453Z-fleet05-A040-credit-insufficiency-tests]
-   [fleet/agents/A046/runs/20261014T041928Z-fleet05-A046-current-candidate-intake]
-   [fleet/agents/A046/runs/20261014T083236Z-fleet05-A046-current-candidate-intake]
-   [fleet/agents/A046/runs/20261014T083236Z-fleet05-A046-current-candidate-intake]

### INDEPENDENT_REVIEW_HOLDS_AT_SCOPE (2)
-   [fleet/claude/B19/runs/20261011T224700Z-claude-B19-paper-audit-rankcode]
-   [fleet/claude/B19/runs/20261011T224700Z-claude-B19-paper-audit-rankcode]

### INDEPENDENT_REVIEW_HOLDS_SEPARATOR_EXTENSION_ONLY (1)
-   [fleet/agents/A040/runs/20261014T003941Z-fleet05-A040-credit-insufficiency-tests]

### INDEPENDENT_REVIEW_SCOPE_CLARIFICATION_REQUIRED (1)
-   [fleet/agents/A088/runs/20261012T024518Z-fleet05-A088-booleanity-referee]

### INDEPENDENT_SCOPED_ACCEPTANCE_WHOLE_BLOCK_ONLY_OTHER_CLAUSES_PENDING (1)
-   [fleet/agents/A029/runs/20261014T025327Z-fleet05-A029-child-deficit-transport]

### INDEPENDENT_SCOPED_BANK_ACCEPTANCE_OTHER_CLAUSES_PENDING (1)
-   [fleet/agents/A029/runs/20261014T055200Z-fleet05-A029-child-deficit-transport]

### INFLUENCE_ONLY_REFERENCE_SLICE_INDEPENDENTLY_ACCEPTED_BY_A098; BUNDLED_OTHER_CLAUSES_PENDING_FULL_REVIEW (2)
-   [fleet/agents/A001/runs/20261014T011101Z-fleet05-A001-quantifier-audit]
-   [fleet/agents/A098/runs/20261013T235014Z-fleet05-A098-resource-reallocation]

### KERNEL_CHECKED_LOCAL_CORE_ANALYTIC_FAMILY_EXACT_FINITE_CERTIFICATES_PENDING_REVIEW (1)
-   [fleet/agents/A083/runs/20261013T234228Z-fleet05-A083-formal-core]

### KERNEL_CHECKED_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A083/runs/20261011T222842Z-fleet05-A083-formal-core]
-   [fleet/agents/A083/runs/20261012T023941Z-fleet05-A083-formal-core]

### LOCAL_CERTIFICATE_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A081/runs/20261011T214745Z-fleet05-A081-dependency-certificates]

### LOCAL_CERTIFICATE_COMPLETE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates]

### LOCAL_CORE_KERNEL_CHECKED_ANALYTIC_FAMILY_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A083/runs/20261014T023633Z-fleet05-A083-formal-core]

### LOCAL_EXACT_CERTIFICATE_AND_PROOF_REVIEW_PENDING (1)
-   [fleet/agents/A071/runs/20261013T215901Z-fleet05-A071-search-space-design]

### LOCAL_EXACT_CERTIFICATE_AND_SCOPED_PROOF_REVIEW_PENDING (1)
-   [fleet/agents/A071/runs/20261014T013355Z-fleet05-A071-search-space-design]

### LOCAL_RATIONAL_CORE_KERNEL_CHECKED_ANALYTIC_CRITERION_PROVED_EXACT_CONDITIONAL_PAYMENT_PENDING_REVIEW (1)
-   [fleet/agents/A083/runs/20261014T053514Z-fleet05-A083-formal-core]

### MAIN_INEQUALITY_INDEPENDENTLY_REVIEWED_LOCALLY; BUNDLED_BOUNDARY_REVIEW_REMAINS_PENDING (1)
-   [fleet/agents/A044/runs/20261013T235618Z-fleet05-A044-non-symmetric-gate-classes]

### MULTIPLE_INDEPENDENT_FULL_SCOPED_ACCEPTANCES_A099_A073_A001_NO_UNIVERSAL_PAYMENT (2)
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### NARROW_ADMISSION_AND_IMPOSSIBILITY_CERTIFIED_PENDING_REVIEW (1)
-   [fleet/agents/A032/runs/20261014T015128Z-fleet05-A032-boolean-phase-realizability]

### NARROW_AUTHOR_PROVED_PENDING_EXTERNAL_REVIEW (1)
-   [fleet/agents/A034/runs/20261014T025347Z-fleet05-A034-phase-energy-transfer]

### NARROW_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A079/runs/20261014T030635Z-fleet05-A079-correlated-auxiliaries]

### NARROW_CERTIFICATE_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A073/runs/20261014T053433Z-fleet05-A073-certified-logarithms]
-   [fleet/agents/A085/runs/20261014T034606Z-fleet05-A085-certificate-adversary]

### NARROW_COMPLETE_REFERENCE_PAYMENT_PROVED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A047/runs/20261014T124731Z-fleet05-A047-boundary-search]

### NARROW_CONDITIONAL_INTERFACE_AUTHOR_PROVED_PENDING_REVIEW (1)
-   [fleet/agents/A066/runs/20261014T042048Z-fleet05-A066-semigroup-dissipation]

### NARROW_DIAGNOSTIC_PROOF_AND_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A002/runs/20261014T100104Z-fleet05-A002-hardness-preserving-transformations]

### NARROW_EXISTING_INTERFACE_CONTINUATION_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A040/runs/20261014T063453Z-fleet05-A040-credit-insufficiency-tests]

### NARROW_EXISTING_INTERFACE_MIXED_HISTORY_CONTINUATION_AUTHOR_PROVED_REVIEW_PENDING (1)
-   [fleet/agents/A046/runs/20261014T083236Z-fleet05-A046-current-candidate-intake]

### NARROW_EXISTING_SEPARATOR_INTERFACE_REFINEMENT_PROVED_REVIEW_PENDING (1)
-   [fleet/agents/A046/runs/20261014T012528Z-fleet05-A046-current-candidate-intake]

### NARROW_HISTORY_INTERFACE_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A066/runs/20261014T090057Z-fleet05-A066-semigroup-dissipation]

### NARROW_LOCAL_CERTIFICATE_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A085/runs/20261014T074749Z-fleet05-A085-certificate-adversary]

### NARROW_PACKET_CLOSURES_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A068/runs/20261014T052938Z-fleet05-A068-antichain-beyond-one-order]

### NARROW_PAID_FRAGMENT_VERIFICATION_PROVED_PENDING_REVIEW (1)
-   [fleet/agents/A066/runs/20261014T012949Z-fleet05-A066-semigroup-dissipation]

### NARROW_PRODUCT_EXTENSION_PROVED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A047/runs/20261014T015314Z-fleet05-A047-boundary-search]

### NARROW_SCOPED_TRANSFER_AUTHOR_PROVED_EXACT_CHECKS_PASS_PENDING_REVIEW (1)
-   [fleet/agents/A069/runs/20261014T060600Z-fleet05-A069-geometric-transfer]

### NARROW_SCOPE_AUDIT_PROVED_AND_CERTIFIED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A047/runs/20261014T044331Z-fleet05-A047-boundary-search]

### NARROW_SCOPE_CERTIFICATE_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A085/runs/20261014T005642Z-fleet05-A085-certificate-adversary]

### NARROW_SCOPE_REPAIR_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A050/runs/20261014T063752Z-fleet05-A050-repair-with-scope]

### NARROW_TERMINAL_ENDPOINT_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A079/runs/20261014T060856Z-fleet05-A079-correlated-auxiliaries]

### NEW_OVERLAP_CLASSIFICATION_CENSUS_AND_LOSS_INDEPENDENTLY_RECONSTRUCTED_LOCALLY; OWN_MUX_DEPENDENCY_NOT_REACCEPTED; ORIGINAL_UNCHANGED (1)
-   [fleet/agents/A044/runs/20261014T025427Z-fleet05-A044-non-symmetric-gate-classes]

### NEW_SHARED_SELECTOR_APPLICATION_SLICE_INDEPENDENTLY_ACCEPTED_BY_A099_OLDER_BUNDLED_CLAUSES_UNAUDITED (2)
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### NUMERICAL_EVIDENCE_FLOAT64 (1)
-   [fleet/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich]

### ONE_INDEPENDENT_FULL_SCOPED_ACCEPTANCE_A094_SECOND_PENDING (2)
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### ONE_INDEPENDENT_FULL_SCOPED_ACCEPTANCE_A099_SECOND_PENDING (1)
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### ONE_INDEPENDENT_SCOPED_ACCEPTANCE_A099_SECOND_AUDIT_PENDING (1)
-   [fleet/agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly]

### ONE_INDEPENDENT_SCOPED_ACCEPTANCE_FULL_CHAIN_AND_SECOND_AUDIT_PENDING (3)
-   [fleet/agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### OPEN (5)
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization]
-   [fleet/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse]
-   [fleet/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport]
-   [fleet/claude/B20/runs/20261011T225100Z-claude-B20-erasure-activation-transfer]

### ORIGINAL_AUTHOR_PROVED_WITH_LOCAL_INDEPENDENT_PARTIAL_REVIEW (2)
-   [fleet/agents/A012/runs/20261013T220914Z-fleet05-A012-sparse-activation-accounting]
-   [fleet/agents/A012/runs/20261014T014452Z-fleet05-A012-sparse-activation-accounting]

### PARTIALLY_INDEPENDENTLY_RECONSTRUCTED_AT_EXPLICIT_TRANSPORT_SCOPE (1)
-   [fleet/agents/A095/runs/20261014T074829Z-fleet05-A095-restricted-result-extraction]

### PARTIALLY_INDEPENDENTLY_RECONSTRUCTED_FULL_RECORD_NOT_ACCEPTED (2)
-   [fleet/agents/A031/runs/20261014T075717Z-fleet05-A031-convolution-identity]
-   [fleet/agents/A035/runs/20261014T032607Z-fleet05-A035-signed-cancellation-countersearch]

### PARTIALLY_INDEPENDENTLY_RECONSTRUCTED_LOCAL (2)
-   [fleet/agents/A013/runs/20261014T021710Z-fleet05-A013-representation-stability]
-   [fleet/agents/A086/runs/20261014T013711Z-fleet05-A086-joint-code-referee]

### PARTIALLY_INDEPENDENTLY_RECONSTRUCTED_NEW_APPLICATION_LOCAL (1)
-   [fleet/agents/A086/runs/20261014T013711Z-fleet05-A086-joint-code-referee]

### PARTIALLY_INDEPENDENTLY_REVIEWED_AT_EXPLICIT_SCOPE_LOCALLY (2)
-   [fleet/agents/A094/runs/20261012T044109Z-fleet05-A094-proof-chain-challenger]
-   [fleet/agents/A094/runs/20261012T044109Z-fleet05-A094-proof-chain-challenger]

### PARTIALLY_INDEPENDENTLY_REVIEWED_LOCAL (1)
-   [fleet/agents/A012/runs/20261011T234525Z-fleet05-A012-sparse-activation-accounting]

### PARTIALLY_RECONSTRUCTED_AT_EXPLICIT_DEPENDENCY_SCOPE_LOCALLY (1)
-   [fleet/agents/A094/runs/20261014T031253Z-fleet05-A094-proof-chain-challenger]

### PARTIALLY_RECONSTRUCTED_LOCAL_NEW_TWO_BIT_CLAUSES_ONLY (2)
-   [fleet/agents/A012/runs/20261014T043333Z-fleet05-A012-sparse-activation-accounting]
-   [fleet/agents/A013/runs/20261014T021710Z-fleet05-A013-representation-stability]

### PARTIALLY_REVIEWED_AT_EXPLICIT_ONE_NODE_SCOPE_LOCALLY (1)
-   [fleet/agents/A094/runs/20261014T001244Z-fleet05-A094-proof-chain-challenger]

### PARTIALLY_REVIEWED_NOT_BLANKET_ACCEPTED (1)
-   [fleet/agents/A086/runs/20261011T214823Z-fleet05-A086-joint-code-referee]

### PARTIAL_A016_FORCED_SUPPORT_REFUND_DIVERGENCE_ELIGIBILITY_HOLDS; OTHER_SOURCE_CLAUSES_NOT_ACCEPTED_BY_THIS_REVIEW (1)
-   [fleet/agents/A016/runs/20261014T075009Z-fleet05-A016-addressing-benchmark]

### PARTIAL_A020_REFERENCE_AND_BALANCED_REPAIR_HOLDS; OTHER_SOURCE_CLAUSES_NOT_ACCEPTED_BY_THIS_REVIEW (1)
-   [fleet/agents/A020/runs/20261014T062539Z-fleet05-A020-selector-boundary-tests]

### PARTIAL_ACCEPTANCE_COUPLED_CLAUSE_GAP (1)
-   [fleet/agents/A032/runs/20261014T043539Z-fleet05-A032-boolean-phase-realizability]

### PARTIAL_FINE_PROFILE_INDEPENDENT_A018_HOLDS; OTHER_SOURCE_CLAUSES_NOT_REVIEWED_HERE (1)
-   [fleet/agents/A018/runs/20261014T051305Z-fleet05-A018-shared-data-collision-law]

### PARTIAL_INDEPENDENT_ACCEPTANCE_PAIRED_ROW_SLICE; OTHER_BUNDLED_CLAUSES_REVIEW_PENDING (1)
-   [fleet/agents/A046/runs/20261014T012528Z-fleet05-A046-current-candidate-intake]

### PARTIAL_INDEPENDENT_REVIEW_FULL_ACCEPTANCE_PENDING (1)
-   [fleet/agents/A098/runs/20261011T223200Z-fleet05-A098-resource-reallocation]

### PARTIAL_INDEPENDENT_REVIEW_FULL_BUNDLE_PENDING (3)
-   [fleet/agents/A022/runs/20261014T014918Z-fleet05-A022-one-point-surgery]
-   [fleet/agents/A022/runs/20261014T043413Z-fleet05-A022-one-point-surgery]
-   [fleet/agents/A022/runs/20261014T103056Z-fleet05-A022-one-point-surgery]

### PARTIAL_INDEPENDENT_REVIEW_FULL_TRANSFER_COROLLARY_PENDING (1)
-   [fleet/agents/A100/runs/20261013T213917Z-fleet05-A100-release-and-continuation-ledger]

### PARTIAL_INDEPENDENT_REVIEW_HOLDS; FULL_V2_REVIEW_PENDING (1)
-   [fleet/agents/A024/runs/20261014T055140Z-fleet05-A024-biased-child-stability]

### PARTIAL_REVIEW_ADDITIONAL_V2_LIFT_HOLDS_BY_A087 (1)
-   [fleet/agents/A087/runs/20261014T020842Z-fleet05-A087-restriction-referee]

### PARTIAL_SCOPE_SINGLETON_TREE_ONLY_BLOCK_SCOPE_REFUTED (1)
-   [fleet/agents/A100/runs/20261013T213917Z-fleet05-A100-release-and-continuation-ledger]

### PRICE_VERIFIED_LOCALLY_FULL_CHAIN_INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A056/runs/20261013T215801Z-fleet05-A056-balanced-composition]

### PROVED; SOURCE_DOCUMENT_INDEPENDENTLY_ACCEPTED_LOCALLY (1)
-   [fleet/agents/A006/runs/20261014T074929Z-fleet05-A006-posterior-forest-optimization]

### PROVED_ANALYTICALLY_AND_EXACT_FINITE_CERTIFICATES; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A010/runs/20261014T062324Z-fleet05-A010-universal-residual-falsifier]

### PROVED_AND_CERTIFIED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A047/runs/20261012T003641Z-fleet05-A047-boundary-search]

### PROVED_AT_SCOPE_INDEPENDENT_A070_RECONSTRUCTION_REGISTRY_ADOPTION_PENDING (1)
-   [fleet/agents/A068/runs/20261013T234128Z-fleet05-A068-antichain-beyond-one-order]

### PROVED_AT_STATED_SCOPE_A020_INDEPENDENT_REVIEW_WITH_ACCEPTED_DEPENDENCY (1)
-   [fleet/agents/A020/runs/20261014T002716Z-fleet05-A020-selector-boundary-tests]

### PROVED_AT_STATED_SCOPE_INDEPENDENT_EXTENSION_REVIEW_PENDING (1)
-   [fleet/agents/A019/runs/20261012T031916Z-fleet05-A019-orthogonality-extensions]

### PROVED_AT_STATED_SCOPE_INDEPENDENT_REVIEW_PENDING (3)
-   [fleet/agents/A019/runs/20261011T223425Z-fleet05-A019-orthogonality-extensions]
-   [fleet/agents/A019/runs/20261013T235305Z-fleet05-A019-orthogonality-extensions]
-   [fleet/agents/A020/runs/20261014T002716Z-fleet05-A020-selector-boundary-tests]

### PROVED_AUTHOR_INDEPENDENT_REVIEW_PENDING (4)
-   [fleet/claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt]
-   [fleet/claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt]
-   [fleet/claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt]
-   [fleet/claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt]

### PROVED_AUTHOR_NO_NOVELTY_CLAIM (1)
-   [fleet/claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt]

### PROVED_AUTHOR_REVIEW_PENDING (1)
-   [fleet/agents/A080/runs/20261013T212642Z-fleet05-A080-universal-counterexample-standard]

### PROVED_BY_EXACT_FINITE_CERTIFICATE_PENDING_REVIEW (1)
-   [fleet/agents/A064/runs/20261014T060409Z-fleet05-A064-global-debt-potential]

### PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW (70)
-   [fleet/agents/A021/runs/20261011T214020Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A021/runs/20261011T214020Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A021/runs/20261011T232653Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A021/runs/20261011T232653Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A021/runs/20261013T214613Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A021/runs/20261014T011316Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A021/runs/20261014T011316Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A023/runs/20261011T221608Z-fleet05-A023-amortized-rarity-budget]
-   [fleet/agents/A023/runs/20261012T010933Z-fleet05-A023-amortized-rarity-budget]
-   [fleet/agents/A023/runs/20261013T223305Z-fleet05-A023-amortized-rarity-budget]
-   [fleet/agents/A023/runs/20261013T223305Z-fleet05-A023-amortized-rarity-budget]
-   [fleet/agents/A023/runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget]
-   [fleet/agents/A023/runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget]
-   [fleet/agents/A024/runs/20261011T223622Z-fleet05-A024-biased-child-stability]
-   [fleet/agents/A024/runs/20261014T025222Z-fleet05-A024-biased-child-stability]
-   [fleet/agents/A024/runs/20261014T055140Z-fleet05-A024-biased-child-stability]
-   [fleet/agents/A025/runs/20261014T032227Z-fleet05-A025-rare-event-counterfamily]
-   [fleet/agents/A026/runs/20261011T214052Z-fleet05-A026-good-coordinate-erasure]
-   [fleet/agents/A026/runs/20261011T214052Z-fleet05-A026-good-coordinate-erasure]
-   [fleet/agents/A026/runs/20261011T232716Z-fleet05-A026-good-coordinate-erasure]
-   [fleet/agents/A027/runs/20261011T215911Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261011T215911Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261011T234627Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261013T221314Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T015108Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T043519Z-fleet05-A027-block-selection]
-   [fleet/agents/A027/runs/20261014T104101Z-fleet05-A027-block-selection]
-   [fleet/agents/A028/runs/20261011T221633Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A028/runs/20261012T011208Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A028/runs/20261013T223410Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A028/runs/20261014T022306Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A028/runs/20261014T051435Z-fleet05-A028-stopping-tree-payment]
-   [fleet/agents/A035/runs/20261011T225802Z-fleet05-A035-signed-cancellation-countersearch]
-   [fleet/agents/A035/runs/20261011T225802Z-fleet05-A035-signed-cancellation-countersearch]
-   [fleet/agents/A038/runs/20261013T223535Z-fleet05-A038-occupancy-term-audit]
-   [fleet/agents/A038/runs/20261013T223535Z-fleet05-A038-occupancy-term-audit]
-   [fleet/agents/A038/runs/20261014T022516Z-fleet05-A038-occupancy-term-audit]
-   [fleet/agents/A038/runs/20261014T051947Z-fleet05-A038-occupancy-term-audit]
-   [fleet/agents/A056/runs/20261011T214407Z-fleet05-A056-balanced-composition]
-   [fleet/agents/A056/runs/20261011T214407Z-fleet05-A056-balanced-composition]
-   [fleet/agents/A056/runs/20261013T215801Z-fleet05-A056-balanced-composition]
-   [fleet/agents/A056/runs/20261014T012909Z-fleet05-A056-balanced-composition]
-   [fleet/agents/A056/runs/20261014T042008Z-fleet05-A056-balanced-composition]
-   [fleet/agents/A056/runs/20261014T085332Z-fleet05-A056-balanced-composition]
-   [fleet/agents/A057/runs/20261013T221645Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261014T015740Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261014T044759Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261014T124811Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A059/runs/20261013T235852Z-fleet05-A059-decomposition-depth]
-   [fleet/agents/A059/runs/20261014T025828Z-fleet05-A059-decomposition-depth]
-   [fleet/agents/A060/runs/20261014T004659Z-fleet05-A060-composition-sharpness]
-   [fleet/agents/A060/runs/20261014T004659Z-fleet05-A060-composition-sharpness]
-   [fleet/agents/A060/runs/20261014T033739Z-fleet05-A060-composition-sharpness]
-   [fleet/agents/A064/runs/20261011T224431Z-fleet05-A064-global-debt-potential]
-   [fleet/agents/A064/runs/20261013T235917Z-fleet05-A064-global-debt-potential]
-   [fleet/agents/A064/runs/20261014T030103Z-fleet05-A064-global-debt-potential]
-   [fleet/agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A087/runs/20261014T020842Z-fleet05-A087-restriction-referee]
-   [fleet/agents/A091/runs/20261011T214848Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T013816Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T042228Z-fleet05-A091-composition-referee]
-   [fleet/agents/A091/runs/20261014T094139Z-fleet05-A091-composition-referee]
-   [fleet/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport]
-   [fleet/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport]
-   [fleet/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport]
-   [fleet/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport]
-   [fleet/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport]
-   [fleet/claude/B06/runs/20261011T223800Z-claude-B06-block-tree-reductions]
-   [fleet/claude/B06/runs/20261011T223800Z-claude-B06-block-tree-reductions]
-   [fleet/claude/B06/runs/20261011T223800Z-claude-B06-block-tree-reductions]

### PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW (FORMULA AND ROOT BOUND); CERTIFIED_EXACT_FINITE (LEDGERS) (1)
-   [fleet/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport]

### PROVED_LOCALLY_REVIEW_PENDING (8)
-   [fleet/agents/A020/runs/20261011T225608Z-fleet05-A020-selector-boundary-tests]
-   [fleet/agents/A020/runs/20261012T044635Z-fleet05-A020-selector-boundary-tests]
-   [fleet/agents/A020/runs/20261012T044635Z-fleet05-A020-selector-boundary-tests]
-   [fleet/agents/A021/runs/20261014T035704Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A021/runs/20261014T075029Z-fleet05-A021-rare-core-asymptotics]
-   [fleet/agents/A047/runs/20261011T220210Z-fleet05-A047-boundary-search]
-   [fleet/agents/A049/runs/20261014T025532Z-fleet05-A049-minimal-falsifier-extraction]
-   [fleet/agents/A049/runs/20261014T055836Z-fleet05-A049-minimal-falsifier-extraction]

### PROVED_LOCAL_INDEPENDENT_REVIEW_PENDING (2)
-   [fleet/agents/A032/runs/20261014T105923Z-fleet05-A032-boolean-phase-realizability]
-   [fleet/agents/A058/runs/20261011T222138Z-fleet05-A058-overlapping-compositions]

### PROVED_LOCAL_PENDING_INDEPENDENT_REVIEW (3)
-   [fleet/agents/A082/runs/20261011T221008Z-fleet05-A082-finite-inequalities]
-   [fleet/agents/A082/runs/20261011T221008Z-fleet05-A082-finite-inequalities]
-   [fleet/agents/A082/runs/20261012T004123Z-fleet05-A082-finite-inequalities]

### PROVED_LOCAL_PENDING_REVIEW (1)
-   [fleet/claude/B15/runs/20261011T225100Z-claude-B15-erasure-countersearch]

### PROVED_NARROW_ENVELOPE_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A040/runs/20261014T033148Z-fleet05-A040-credit-insufficiency-tests]

### PROVED_NARROW_SCOPE_EXPLORATION_NOT_PROPOSED_FOR_ADOPTION_REVIEW_CAP (1)
-   [fleet/agents/A044/runs/20261011T223925Z-fleet05-A044-non-symmetric-gate-classes]

### PROVED_PENDING_INDEPENDENT_REVIEW (5)
-   [fleet/agents/A057/runs/20261011T220314Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261011T220314Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A057/runs/20261012T003930Z-fleet05-A057-coherent-restriction-remainder]
-   [fleet/agents/A059/runs/20261011T224320Z-fleet05-A059-decomposition-depth]
-   [fleet/agents/A087/runs/20261013T222530Z-fleet05-A087-restriction-referee]

### PROVED_STANDARD_SYMMETRY_RECONSTRUCTION_PENDING_REVIEW (1)
-   [fleet/agents/A087/runs/20261012T004155Z-fleet05-A087-restriction-referee]

### PROVED_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A032/runs/20261011T215947Z-fleet05-A032-boolean-phase-realizability]

### REFUTED_REMAINDER_COMPONENT_OLD_ACCEPTANCES_RETRACTED (1)
-   [fleet/agents/A100/runs/20261013T213917Z-fleet05-A100-release-and-continuation-ledger]

### REFUTED_V1; A023_PRIOR_REVIEW_RETRACTED (1)
-   [fleet/agents/A023/runs/20261012T010933Z-fleet05-A023-amortized-rarity-budget]

### REPAIRED_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A070/runs/20261013T212602Z-fleet05-A070-analytic-route-referee]

### REPAIR_AND_OBSTRUCTION_PROVED_LOCAL_REVIEW_PENDING (1)
-   [fleet/agents/A058/runs/20261012T020138Z-fleet05-A058-overlapping-compositions]

### RESTRICTED_CERTIFICATE_CHECKED_REVIEW_PENDING_FULL_MAP_OPEN (1)
-   [fleet/agents/A084/runs/20261011T224831Z-fleet05-A084-continuum-parameters]

### SCOPED_ANALYTIC_JENSEN_REFINEMENT_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A100/runs/20261014T034838Z-fleet05-A100-release-and-continuation-ledger]

### SCOPED_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A036/runs/20261014T083156Z-fleet05-A036-reference-law-divergence]

### SCOPED_APPLICATION_A020_INDEPENDENT_ACCEPTANCE_WITH_ACCEPTED_DEPENDENCY (1)
-   [fleet/agents/A020/runs/20261014T032122Z-fleet05-A020-selector-boundary-tests]

### SCOPED_APPLICATION_AUTHOR_PROVED_INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A019/runs/20261014T025011Z-fleet05-A019-orthogonality-extensions]

### SCOPED_AUTHOR_PROOF_AND_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A026/runs/20261014T075434Z-fleet05-A026-good-coordinate-erasure]

### SCOPED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW (7)
-   [fleet/agents/A003/runs/20261013T222630Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A003/runs/20261013T222630Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A003/runs/20261014T021415Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A003/runs/20261014T050612Z-fleet05-A003-minimal-target-formulation]
-   [fleet/agents/A026/runs/20261013T214810Z-fleet05-A026-good-coordinate-erasure]
-   [fleet/agents/A026/runs/20261014T011337Z-fleet05-A026-good-coordinate-erasure]
-   [fleet/agents/A026/runs/20261014T040156Z-fleet05-A026-good-coordinate-erasure]

### SCOPED_CALIBRATION_AND_DIAGNOSTIC_FALSIFIER_REVIEW_PENDING (1)
-   [fleet/agents/A020/runs/20261014T032122Z-fleet05-A020-selector-boundary-tests]

### SCOPED_CONDITIONAL_REFERENCE_AUDIT_PROVED_PENDING_INDEPENDENT_REVIEW (5)
-   [fleet/agents/A096/runs/20261014T013836Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### SCOPED_CONTINUATION_PROVED_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger]
-   [fleet/agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger]

### SCOPED_CONTINUUM_RECONSTRUCTION_ONLY_FULL_CHAIN_NOT_INDEPENDENTLY_ACCEPTED (1)
-   [fleet/agents/A012/runs/20261014T101345Z-fleet05-A012-sparse-activation-accounting]

### SCOPED_CONVERSION_PROVED_AND_CERTIFIED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A047/runs/20261013T221434Z-fleet05-A047-boundary-search]

### SCOPED_DEPENDENCY_CONTINUATION_AUTHOR_PROVED_PENDING_REVIEW (1)
-   [fleet/agents/A016/runs/20261014T075009Z-fleet05-A016-addressing-benchmark]

### SCOPED_EXACT_HISTORY_CERTIFICATE_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A001/runs/20261014T074909Z-fleet05-A001-quantifier-audit]

### SCOPED_EXISTING_PAYMENT_VERIFICATION_PROVED_LOCALLY_PENDING_REVIEW (1)
-   [fleet/agents/A048/runs/20261012T013822Z-fleet05-A048-tensor-stress]

### SCOPED_EXPLICIT_FAMILY_LEMMA_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A073/runs/20261014T023508Z-fleet05-A073-certified-logarithms]

### SCOPED_INDEPENDENT_ACTIVATION_REPAIR_PROVED_LOCAL_REVIEW_PENDING (1)
-   [fleet/agents/A058/runs/20261014T052501Z-fleet05-A058-overlapping-compositions]

### SCOPED_INDEPENDENT_REVIEW_COMPLETE_LOCALLY (1)
-   [fleet/agents/A009/runs/20261012T031835Z-fleet05-A009-fractional-incidence-optimization]

### SCOPED_INTERFACE_AND_EXACT_OBSTRUCTION_PROVED_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A004/runs/20261014T024610Z-fleet05-A004-constant-and-unit-ledger]

### SCOPED_LEMMA_ACCEPTED_LOCAL; REMAINDER_NOT_REVIEWED_HERE (2)
-   [fleet/agents/A058/runs/20261014T052501Z-fleet05-A058-overlapping-compositions]
-   [fleet/agents/A058/runs/20261014T052501Z-fleet05-A058-overlapping-compositions]

### SCOPED_LIVE_MECHANISM_REPAIR_REFUTATION_AUTHOR_PROVED_PENDING_REVIEW (1)
-   [fleet/agents/A016/runs/20261013T214508Z-fleet05-A016-addressing-benchmark]

### SCOPED_MECHANISM_APPLICATION_AUTHOR_PROVED_PENDING_REVIEW (1)
-   [fleet/agents/A016/runs/20261014T011255Z-fleet05-A016-addressing-benchmark]

### SCOPED_MECHANISM_CALIBRATION_AUTHOR_PROVED_PENDING_REVIEW (1)
-   [fleet/agents/A016/runs/20261011T232501Z-fleet05-A016-addressing-benchmark]

### SCOPED_MECHANISM_FALSIFIER_AUTHOR_PROVED_INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A020/runs/20261014T062539Z-fleet05-A020-selector-boundary-tests]

### SCOPED_MECHANISM_OBSTRUCTION_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A001/runs/20261013T213937Z-fleet05-A001-quantifier-audit]

### SCOPED_MECHANISM_REFUTATION_AUTHOR_PROVED_PENDING_REVIEW (1)
-   [fleet/agents/A016/runs/20261014T035514Z-fleet05-A016-addressing-benchmark]

### SCOPED_NEW_PROFILE_RECONSTRUCTION_ONLY_FULL_CHAIN_NOT_INDEPENDENTLY_ACCEPTED (2)
-   [fleet/agents/A012/runs/20261014T043333Z-fleet05-A012-sparse-activation-accounting]
-   [fleet/agents/A013/runs/20261014T051241Z-fleet05-A013-representation-stability]

### SCOPED_NORMALIZED_REFERENCE_OBSTRUCTION_PROVED_PENDING_INDEPENDENT_REVIEW (3)
-   [fleet/agents/A001/runs/20261014T011101Z-fleet05-A001-quantifier-audit]
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### SCOPED_NORM_REPAIR_AND_BOUNDARY_PROVED_LOCAL_REVIEW_PENDING (1)
-   [fleet/agents/A058/runs/20261014T022937Z-fleet05-A058-overlapping-compositions]

### SCOPED_QUADRATIC_REFERENCE_REPAIR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A045/runs/20261014T033253Z-fleet05-A045-biased-realizability-referee]

### SCOPED_RECONSTRUCTION_EXACTLY_CERTIFIED_PENDING_EXTERNAL_REVIEW (1)
-   [fleet/agents/A081/runs/20261013T220111Z-fleet05-A081-dependency-certificates]

### SCOPED_RECONSTRUCTION_HOLDS_LOCAL_RECORD_PENDING_SUPERVISOR_ADOPTION (1)
-   [fleet/agents/A041/runs/20261014T083216Z-fleet05-A041-weighted-threshold-fei]

### SCOPED_REFEREE_RECONSTRUCTION_COMPLETE_PENDING_REVIEW_OF_AUDIT (1)
-   [fleet/agents/A045/runs/20261011T225924Z-fleet05-A045-biased-realizability-referee]

### SCOPED_REFERENCE_ADMISSION_REPAIR_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A045/runs/20261014T004049Z-fleet05-A045-biased-realizability-referee]

### SCOPED_REFERENCE_APPLICATION_AUTHOR_PROVED_INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A019/runs/20261014T055119Z-fleet05-A019-orthogonality-extensions]

### SCOPED_REFERENCE_AUDIT_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger]

### SCOPED_REFINEMENT_AUTHOR_PROVED_WITH_EXACT_ENDPOINT_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A033/runs/20261014T051927Z-fleet05-A033-derivative-hierarchy]

### SCOPED_REFUTATION_CERTIFIED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A005/runs/20261011T225209Z-fleet05-A005-noncircular-endpoint-referee]

### SCOPED_REPAIR_AUTHOR_PROVED_REVIEW_PENDING (1)
-   [fleet/agents/A050/runs/20261013T212442Z-fleet05-A050-repair-with-scope]

### SCOPED_REPAIR_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A050/runs/20261014T004109Z-fleet05-A050-repair-with-scope]

### SCOPED_REPAIR_PROVED_LOCAL_REVIEW_PENDING (1)
-   [fleet/agents/A058/runs/20261013T234047Z-fleet05-A058-overlapping-compositions]

### SCOPED_REVIEW_HOLDS_FULL_CHAIN_CONDITIONAL_AUTHOR_CONFLICT (1)
-   [fleet/agents/A061/runs/20261014T012929Z-fleet05-A061-entropy-process]

### SCOPED_ROOT_REFERENCE_LEDGER_PROVED_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A001/runs/20261014T035113Z-fleet05-A001-quantifier-audit]

### SCOPED_SIGNED_REFERENCE_REPAIR_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING (1)
-   [fleet/agents/A050/runs/20261014T033613Z-fleet05-A050-repair-with-scope]

### SECTION1_INDEPENDENTLY_ACCEPTED_ONLY_REMAINDER_OUTSIDE_REVIEW (1)
-   [fleet/agents/A056/runs/20261014T042008Z-fleet05-A056-balanced-composition]

### SOURCE_BOUND_AUDIT_COMPLETE_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A001/runs/20261011T210330Z-fleet05-A001-quantifier-audit]

### SOURCE_COMPLETE_ALL_BIAS_COHERENT_PRIME_BOUND; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A043/runs/20261014T052009Z-fleet05-A043-prime-gate-decomposition]

### SOURCE_COMPLETE_ANALYTIC_ARBITRARY_ARITY_CLASS_AND_EXACT_CENSUS_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A043/runs/20261014T022706Z-fleet05-A043-prime-gate-decomposition]

### SOURCE_COMPLETE_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A055/runs/20261013T212502Z-fleet05-A055-extremal-obstruction-referee]

### SOURCE_COMPLETE_ANALYTIC_PROOF_AND_EXACT_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A043/runs/20261013T233947Z-fleet05-A043-prime-gate-decomposition]

### SOURCE_COMPLETE_ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW (7)
-   [fleet/agents/A051/runs/20261011T233123Z-fleet05-A051-near-extremizer-definition]
-   [fleet/agents/A053/runs/20261011T221934Z-fleet05-A053-near-tensor-perturbations]
-   [fleet/agents/A053/runs/20261012T014744Z-fleet05-A053-near-tensor-perturbations]
-   [fleet/agents/A053/runs/20261013T234027Z-fleet05-A053-near-tensor-perturbations]
-   [fleet/agents/A053/runs/20261014T022917Z-fleet05-A053-near-tensor-perturbations]
-   [fleet/agents/A053/runs/20261014T052310Z-fleet05-A053-near-tensor-perturbations]
-   [fleet/agents/A055/runs/20261011T230118Z-fleet05-A055-extremal-obstruction-referee]

### SOURCE_COMPLETE_BASELINE_RECONSTRUCTION_INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A018/runs/20261011T221538Z-fleet05-A018-shared-data-collision-law]

### SOURCE_COMPLETE_ENDPOINT_MECHANISM_OBSTRUCTION_AND_SYMBOLIC_CERTIFICATES; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A042/runs/20261014T112104Z-fleet05-A042-bias-endpoint-certificates]

### SOURCE_COMPLETE_LOCAL_COFACTOR_MECHANISM_AND_CONGESTION_OBSTRUCTION; INDEPENDENT_REVIEW_PENDING; UNIVERSAL_SUMMED_PAYMENT_OPEN (1)
-   [fleet/agents/A044/runs/20261014T055346Z-fleet05-A044-non-symmetric-gate-classes]

### SOURCE_COMPLETE_LOCAL_NARROW_REPAIR; INDEPENDENT_REVIEW_PENDING; NO_NEW_BROAD_CANDIDATE (1)
-   [fleet/agents/A044/runs/20261013T235618Z-fleet05-A044-non-symmetric-gate-classes]

### SOURCE_COMPLETE_NARROW_ENDPOINT_REPAIR; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A042/runs/20261014T044053Z-fleet05-A042-bias-endpoint-certificates]

### SOURCE_COMPLETE_NARROW_MECHANISM_OBSTRUCTION_AND_SHARP_SLICE_REPAIR; INDEPENDENT_REVIEW_PENDING (1)
-   [fleet/agents/A044/runs/20261014T025427Z-fleet05-A044-non-symmetric-gate-classes]

### SOURCE_COMPLETE_NARROW_REPAIR_AND_EXACT_CHECKS_PENDING_REVIEW (1)
-   [fleet/agents/A042/runs/20261014T015254Z-fleet05-A042-bias-endpoint-certificates]

### SOURCE_COMPLETE_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A002/runs/20261011T215124Z-fleet05-A002-hardness-preserving-transformations]
-   [fleet/agents/A002/runs/20261011T215124Z-fleet05-A002-hardness-preserving-transformations]

### SOURCE_COMPLETE_PENDING_REVIEW (2)
-   [fleet/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority]
-   [fleet/agents/A093/runs/20261014T024314Z-fleet05-A093-literature-and-priority]

### SOURCE_COMPLETE_SCOPED_COROLLARY_PENDING_INDEPENDENT_REVIEW (2)
-   [fleet/agents/A005/runs/20261012T044149Z-fleet05-A005-noncircular-endpoint-referee]
-   [fleet/agents/A005/runs/20261014T001325Z-fleet05-A005-noncircular-endpoint-referee]

### SOURCE_COMPLETE_SCOPED_ENDPOINT_APPLICATION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A005/runs/20261014T031720Z-fleet05-A005-noncircular-endpoint-referee]

### SOURCE_COMPLETE_SCOPED_ENDPOINT_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A005/runs/20261014T061827Z-fleet05-A005-noncircular-endpoint-referee]

### SOURCE_COMPLETE_SCOPED_EXTENSION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A002/runs/20261013T220534Z-fleet05-A002-hardness-preserving-transformations]

### SOURCE_COMPLETE_SCOPED_EXTENSION_PENDING_REVIEW (2)
-   [fleet/agents/A002/runs/20261011T234442Z-fleet05-A002-hardness-preserving-transformations]
-   [fleet/agents/A002/runs/20261011T234442Z-fleet05-A002-hardness-preserving-transformations]

### SOURCE_COMPLETE_SCOPED_HARDENING_EXTENSION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A002/runs/20261014T043038Z-fleet05-A002-hardness-preserving-transformations]

### SOURCE_COMPLETE_SCOPED_QUANTIFIER_EXTENSION_PENDING_INDEPENDENT_REVIEW (1)
-   [fleet/agents/A002/runs/20261014T013942Z-fleet05-A002-hardness-preserving-transformations]

### STAGE4_EXTENSION_ACCEPTED_LOCAL_INDEPENDENT_REVIEW; EARLIER_BUNDLE_NOT_REVIEWED_HERE (2)
-   [fleet/agents/A058/runs/20261014T022937Z-fleet05-A058-overlapping-compositions]
-   [fleet/agents/A058/runs/20261014T022937Z-fleet05-A058-overlapping-compositions]

### TWO_INDEPENDENT_FULL_SCOPED_ACCEPTANCES_A098_A099_HEREDITARY_TRANSPORT_OPEN (1)
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### TWO_INDEPENDENT_FULL_SCOPED_ACCEPTANCES_A098_A100_REMAINDER_ONLY (1)
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### TWO_INDEPENDENT_SCOPED_ACCEPTANCES_A096_A099 (3)
-   [fleet/agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly]
-   [fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly]

### TWO_WHOLE_INDEPENDENT_RECONSTRUCTIONS_OBSERVED_LOCAL_ADOPTION_PENDING (1)
-   [fleet/agents/A008/runs/20261014T050954Z-fleet05-A008-gate-label-compression]

### V1_INDEPENDENTLY_ACCEPTED; V2_ALL_ORDER_EXTENSION_PROVED_LOCALLY_PENDING_REVIEW (1)
-   [fleet/agents/A059/runs/20261014T060348Z-fleet05-A059-decomposition-depth]

### WHOLE_INDEPENDENT_RECONSTRUCTION_BY_A009_LOCAL_ADOPTION_PENDING (1)
-   [fleet/agents/A009/runs/20261014T054349Z-fleet05-A009-fractional-incidence-optimization]

## Newest fleet runs

- 10-14 16:06  fleet/agents/A052/runs/20261014T124751Z-fleet05-A052-critical-source-structure
- 10-14 16:06  fleet/agents/A072/runs/20261014T124911Z-fleet05-A072-exact-walsh-engine
- 10-14 16:04  fleet/agents/A047/runs/20261014T124731Z-fleet05-A047-boundary-search
- 10-14 16:04  fleet/agents/A057/runs/20261014T124811Z-fleet05-A057-coherent-restriction-remainder
- 10-14 16:04  fleet/agents/A062/runs/20261014T124831Z-fleet05-A062-influence-compensator
- 10-14 14:30  fleet/agents/A042/runs/20261014T112104Z-fleet05-A042-bias-endpoint-certificates
- 10-14 14:19  fleet/agents/A037/runs/20261014T111143Z-fleet05-A037-conditional-credit-ledger
- 10-14 14:10  fleet/agents/A032/runs/20261014T105923Z-fleet05-A032-boolean-phase-realizability
- 10-14 13:55  fleet/agents/A017/runs/20261014T102650Z-fleet05-A017-recursive-addressing
- 10-14 13:49  fleet/agents/A027/runs/20261014T104101Z-fleet05-A027-block-selection
- 10-14 13:39  fleet/agents/A022/runs/20261014T103056Z-fleet05-A022-one-point-surgery
- 10-14 13:26  fleet/agents/A012/runs/20261014T101345Z-fleet05-A012-sparse-activation-accounting
- 10-14 13:14  fleet/agents/A002/runs/20261014T100104Z-fleet05-A002-hardness-preserving-transformations
- 10-14 13:13  fleet/agents/A007/runs/20261014T100124Z-fleet05-A007-root-normalization
- 10-14 13:00  fleet/agents/A091/runs/20261014T094139Z-fleet05-A091-composition-referee
- 10-14 13:00  fleet/agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger
- 10-14 12:48  fleet/agents/A086/runs/20261014T093519Z-fleet05-A086-joint-code-referee
- 10-14 12:40  fleet/agents/A081/runs/20261014T092812Z-fleet05-A081-dependency-certificates
- 10-14 12:34  fleet/agents/A076/runs/20261014T091637Z-fleet05-A076-threshold-and-tribes-controls
- 10-14 12:24  fleet/agents/A056/runs/20261014T085332Z-fleet05-A056-balanced-composition
- 10-14 12:14  fleet/agents/A071/runs/20261014T090502Z-fleet05-A071-search-space-design
- 10-14 12:14  fleet/agents/A066/runs/20261014T090057Z-fleet05-A066-semigroup-dissipation
- 10-14 12:03  fleet/agents/A061/runs/20261014T085352Z-fleet05-A061-entropy-process
- 10-14 12:00  fleet/agents/A051/runs/20261014T085227Z-fleet05-A051-near-extremizer-definition
- 10-14 11:51  fleet/agents/A036/runs/20261014T083156Z-fleet05-A036-reference-law-divergence
- 10-14 11:48  fleet/agents/A041/runs/20261014T083216Z-fleet05-A041-weighted-threshold-fei
- 10-14 11:47  fleet/agents/A046/runs/20261014T083236Z-fleet05-A046-current-candidate-intake
- 10-14 11:14  fleet/agents/A011/runs/20261014T074949Z-fleet05-A011-representation-existence
- 10-14 11:11  fleet/agents/A031/runs/20261014T040733Z-fleet05-A031-convolution-identity
- 10-14 11:11  fleet/agents/A031/runs/20261014T075717Z-fleet05-A031-convolution-identity
- 10-14 11:09  fleet/agents/A016/runs/20261014T075009Z-fleet05-A016-addressing-benchmark
- 10-14 11:08  fleet/agents/A026/runs/20261014T075434Z-fleet05-A026-good-coordinate-erasure
- 10-14 11:08  fleet/agents/A095/runs/20261014T074829Z-fleet05-A095-restricted-result-extraction
- 10-14 11:07  fleet/agents/A075/runs/20261014T074708Z-fleet05-A075-search-to-theorem-bridge
- 10-14 11:06  fleet/agents/A021/runs/20261014T075029Z-fleet05-A021-rare-core-asymptotics
- 10-14 11:04  fleet/agents/A006/runs/20261014T074929Z-fleet05-A006-posterior-forest-optimization
- 10-14 11:01  fleet/agents/A001/runs/20261014T074909Z-fleet05-A001-quantifier-audit
- 10-14 11:00  fleet/agents/A026/runs/20261014T040156Z-fleet05-A026-good-coordinate-erasure
- 10-14 10:57  fleet/agents/A085/runs/20261014T074749Z-fleet05-A085-certificate-adversary
- 10-14 10:55  fleet/agents/A080/runs/20261014T074729Z-fleet05-A080-universal-counterexample-standard
- 10-14 10:54  fleet/agents/A090/runs/20261014T074809Z-fleet05-A090-independent-reconstruction
- 10-14 10:54  fleet/agents/A095/runs/20261014T034647Z-fleet05-A095-restricted-result-extraction
- 10-14 10:52  fleet/agents/A021/runs/20261014T035704Z-fleet05-A021-rare-core-asymptotics
- 10-14 10:52  fleet/agents/A016/runs/20261014T035514Z-fleet05-A016-addressing-benchmark
- 10-14 09:54  fleet/agents/A050/runs/20261014T063752Z-fleet05-A050-repair-with-scope
- 10-14 09:54  fleet/agents/A045/runs/20261014T063646Z-fleet05-A045-biased-realizability-referee
- 10-14 09:53  fleet/agents/A055/runs/20261014T064016Z-fleet05-A055-extremal-obstruction-referee
- 10-14 09:51  fleet/agents/A035/runs/20261014T063030Z-fleet05-A035-signed-cancellation-countersearch
- 10-14 09:50  fleet/agents/A040/runs/20261014T063453Z-fleet05-A040-credit-insufficiency-tests
- 10-14 09:45  fleet/agents/A030/runs/20261014T062839Z-fleet05-A030-restriction-plateau-tests
- 10-14 09:43  fleet/agents/A025/runs/20261014T062819Z-fleet05-A025-rare-event-counterfamily
- 10-14 09:41  fleet/agents/A005/runs/20261014T061827Z-fleet05-A005-noncircular-endpoint-referee
- 10-14 09:40  fleet/agents/A015/runs/20261014T062347Z-fleet05-A015-minterm-barrier-analysis
- 10-14 09:37  fleet/agents/A020/runs/20261014T062539Z-fleet05-A020-selector-boundary-tests
- 10-14 09:36  fleet/agents/A089/runs/20261014T061326Z-fleet05-A089-repair-specialist
- 10-14 09:35  fleet/agents/A099/runs/20261014T061720Z-fleet05-A099-candidate-assembly
- 10-14 09:34  fleet/agents/A010/runs/20261014T062324Z-fleet05-A010-universal-residual-falsifier
- 10-14 09:32  fleet/agents/A094/runs/20261014T061347Z-fleet05-A094-proof-chain-challenger
- 10-14 09:28  fleet/agents/A064/runs/20261014T060409Z-fleet05-A064-global-debt-potential
- 10-14 09:26  fleet/agents/A079/runs/20261014T060856Z-fleet05-A079-correlated-auxiliaries
- 10-14 09:25  fleet/agents/A084/runs/20261014T061132Z-fleet05-A084-continuum-parameters
- 10-14 09:23  fleet/agents/A059/runs/20261014T060348Z-fleet05-A059-decomposition-depth
- 10-14 09:22  fleet/agents/A069/runs/20261014T060600Z-fleet05-A069-geometric-transfer
- 10-14 09:22  fleet/agents/A074/runs/20261014T060751Z-fleet05-A074-independent-reproducer
- 10-14 09:17  fleet/agents/A054/runs/20261014T055856Z-fleet05-A054-connectedness-alternatives
- 10-14 09:14  fleet/agents/A049/runs/20261014T055836Z-fleet05-A049-minimal-falsifier-extraction
- 10-14 09:12  fleet/agents/A039/runs/20261014T055326Z-fleet05-A039-projection-under-restrictions
- 10-14 09:10  fleet/agents/A024/runs/20261014T055140Z-fleet05-A024-biased-child-stability
- 10-14 09:09  fleet/agents/A019/runs/20261014T055119Z-fleet05-A019-orthogonality-extensions
- 10-14 09:05  fleet/agents/A029/runs/20261014T055200Z-fleet05-A029-child-deficit-transport
- 10-14 09:02  fleet/agents/A034/runs/20261014T055220Z-fleet05-A034-phase-energy-transfer
- 10-14 09:02  fleet/agents/A009/runs/20261014T054349Z-fleet05-A009-fractional-incidence-optimization
- 10-14 09:01  fleet/agents/A068/runs/20261014T052938Z-fleet05-A068-antichain-beyond-one-order
- 10-14 09:01  fleet/agents/A044/runs/20261014T055346Z-fleet05-A044-non-symmetric-gate-classes
- 10-14 08:56  fleet/agents/A014/runs/20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read
- 10-14 08:55  fleet/agents/A083/runs/20261014T053514Z-fleet05-A083-formal-core
- 10-14 08:52  fleet/agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee
- 10-14 08:51  fleet/agents/A098/runs/20261014T054007Z-fleet05-A098-resource-reallocation
- 10-14 08:50  fleet/agents/A004/runs/20261014T054158Z-fleet05-A004-constant-and-unit-ledger
- 10-14 08:49  fleet/agents/A058/runs/20261014T052501Z-fleet05-A058-overlapping-compositions
- 10-14 08:49  fleet/agents/A078/runs/20261014T053454Z-fleet05-A078-coding-and-padding
- 10-14 08:49  fleet/agents/A093/runs/20261014T053944Z-fleet05-A093-literature-and-priority
- 10-14 08:43  fleet/agents/A073/runs/20261014T053433Z-fleet05-A073-certified-logarithms
- 10-14 08:42  fleet/agents/A053/runs/20261014T052310Z-fleet05-A053-near-tensor-perturbations
- 10-14 08:40  fleet/agents/A043/runs/20261014T052009Z-fleet05-A043-prime-gate-decomposition
- 10-14 08:38  fleet/agents/A033/runs/20261014T051927Z-fleet05-A033-derivative-hierarchy
- 10-14 08:37  fleet/agents/A048/runs/20261014T052201Z-fleet05-A048-tensor-stress
- 10-14 08:34  fleet/agents/A028/runs/20261014T051435Z-fleet05-A028-stopping-tree-payment
- 10-14 08:34  fleet/agents/A063/runs/20261014T052608Z-fleet05-A063-information-revelation
- 10-14 08:32  fleet/agents/A038/runs/20261014T051947Z-fleet05-A038-occupancy-term-audit
- 10-14 08:32  fleet/agents/A018/runs/20261014T051305Z-fleet05-A018-shared-data-collision-law
- 10-14 08:28  fleet/agents/A013/runs/20261014T051241Z-fleet05-A013-representation-stability
- 10-14 08:23  fleet/agents/A097/runs/20261014T050248Z-fleet05-A097-cross-route-transfer
- 10-14 08:22  fleet/agents/A023/runs/20261014T051414Z-fleet05-A023-amortized-rarity-budget
- 10-14 08:22  fleet/agents/A008/runs/20261014T050954Z-fleet05-A008-gate-label-compression
- 10-14 08:19  fleet/agents/A092/runs/20261014T045641Z-fleet05-A092-counterexample-referee
- 10-14 08:19  fleet/agents/A057/runs/20261014T044759Z-fleet05-A057-coherent-restriction-remainder
- 10-14 08:18  fleet/agents/A003/runs/20261014T050612Z-fleet05-A003-minimal-target-formulation
- 10-14 08:15  fleet/agents/A077/runs/20261014T045011Z-fleet05-A077-sparse-defect-towers
- 10-14 08:13  fleet/agents/A087/runs/20261014T045317Z-fleet05-A087-restriction-referee
- 10-14 08:12  fleet/agents/A067/runs/20261014T044841Z-fleet05-A067-hypercontractive-refinement
- 10-14 08:09  fleet/agents/A062/runs/20261014T044820Z-fleet05-A062-influence-compensator
- 10-14 08:08  fleet/agents/A091/runs/20261014T042228Z-fleet05-A091-composition-referee
- 10-14 08:07  fleet/agents/A072/runs/20261014T044904Z-fleet05-A072-exact-walsh-engine
- 10-14 08:02  fleet/agents/A082/runs/20261014T045125Z-fleet05-A082-finite-inequalities
- 10-14 08:00  fleet/agents/A052/runs/20261014T044609Z-fleet05-A052-critical-source-structure
- 10-14 07:55  fleet/agents/A047/runs/20261014T044331Z-fleet05-A047-boundary-search
- 10-14 07:50  fleet/agents/A032/runs/20261014T043539Z-fleet05-A032-boolean-phase-realizability
- 10-14 07:50  fleet/agents/A002/runs/20261014T043038Z-fleet05-A002-hardness-preserving-transformations
- 10-14 07:48  fleet/agents/A012/runs/20261014T043333Z-fleet05-A012-sparse-activation-accounting
- 10-14 07:47  fleet/agents/A007/runs/20261014T043228Z-fleet05-A007-root-normalization
- 10-14 07:47  fleet/agents/A042/runs/20261014T044053Z-fleet05-A042-bias-endpoint-certificates
- 10-14 07:46  fleet/agents/A037/runs/20261014T043944Z-fleet05-A037-conditional-credit-ledger
- 10-14 07:45  fleet/agents/A017/runs/20261014T043353Z-fleet05-A017-recursive-addressing
- 10-14 07:45  fleet/agents/A022/runs/20261014T043413Z-fleet05-A022-one-point-surgery
- 10-14 07:42  fleet/agents/A027/runs/20261014T043519Z-fleet05-A027-block-selection
- 10-14 07:39  fleet/agents/A056/runs/20261014T042008Z-fleet05-A056-balanced-composition
- 10-14 07:38  fleet/agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger
- 10-14 07:33  fleet/agents/A076/runs/20261014T042128Z-fleet05-A076-threshold-and-tribes-controls
- 10-14 07:33  fleet/agents/A066/runs/20261014T042048Z-fleet05-A066-semigroup-dissipation
- 10-14 07:32  fleet/agents/A086/runs/20261014T042208Z-fleet05-A086-joint-code-referee
- 10-14 07:32  fleet/agents/A051/runs/20261014T041948Z-fleet05-A051-near-extremizer-definition
- 10-14 07:31  fleet/agents/A071/runs/20261014T042108Z-fleet05-A071-search-space-design
- 10-14 07:31  fleet/agents/A081/runs/20261014T042148Z-fleet05-A081-dependency-certificates
- 10-14 07:29  fleet/agents/A046/runs/20261014T041928Z-fleet05-A046-current-candidate-intake
- 10-14 07:27  fleet/agents/A061/runs/20261014T042028Z-fleet05-A061-entropy-process
- 10-14 07:12  fleet/agents/A011/runs/20261014T035454Z-fleet05-A011-representation-existence
- 10-14 07:11  fleet/agents/A001/runs/20261014T035113Z-fleet05-A001-quantifier-audit
- 10-14 07:11  fleet/agents/A100/runs/20261014T034838Z-fleet05-A100-release-and-continuation-ledger
- 10-14 07:06  fleet/agents/A050/runs/20261014T033613Z-fleet05-A050-repair-with-scope
- 10-14 07:03  fleet/agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge
- 10-14 06:58  fleet/agents/A080/runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard
- 10-14 06:54  fleet/agents/A085/runs/20261014T034606Z-fleet05-A085-certificate-adversary
- 10-14 06:54  fleet/agents/A070/runs/20261014T034205Z-fleet05-A070-analytic-route-referee
- 10-14 06:53  fleet/agents/A090/runs/20261014T034626Z-fleet05-A090-independent-reconstruction
- 10-14 06:51  fleet/agents/A060/runs/20261014T033739Z-fleet05-A060-composition-sharpness
- 10-14 06:49  fleet/agents/A055/runs/20261014T033719Z-fleet05-A055-extremal-obstruction-referee
- 10-14 06:46  fleet/agents/A079/runs/20261014T030635Z-fleet05-A079-correlated-auxiliaries
- 10-14 06:45  fleet/agents/A065/runs/20261014T033844Z-fleet05-A065-stopping-rule-falsifier
- 10-14 06:44  fleet/agents/A040/runs/20261014T033148Z-fleet05-A040-credit-insufficiency-tests
- 10-14 06:43  fleet/agents/A010/runs/20261014T031741Z-fleet05-A010-universal-residual-falsifier
- 10-14 06:41  fleet/agents/A035/runs/20261014T032607Z-fleet05-A035-signed-cancellation-countersearch
- 10-14 06:41  fleet/agents/A045/runs/20261014T033253Z-fleet05-A045-biased-realizability-referee
- 10-14 06:40  fleet/agents/A005/runs/20261014T031720Z-fleet05-A005-noncircular-endpoint-referee
- 10-14 06:36  fleet/agents/A015/runs/20261014T031846Z-fleet05-A015-minterm-barrier-analysis
- 10-14 06:36  fleet/agents/A030/runs/20261014T032502Z-fleet05-A030-restriction-plateau-tests
- 10-14 06:34  fleet/agents/A025/runs/20261014T032227Z-fleet05-A025-rare-event-counterfamily
- 10-14 06:32  fleet/agents/A020/runs/20261014T032122Z-fleet05-A020-selector-boundary-tests
- 10-14 06:30  fleet/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly
- 10-14 06:29  fleet/agents/A094/runs/20261014T031253Z-fleet05-A094-proof-chain-challenger
- 10-14 06:25  fleet/agents/A084/runs/20261014T030826Z-fleet05-A084-continuum-parameters
- 10-14 06:24  fleet/agents/A089/runs/20261014T030932Z-fleet05-A089-repair-specialist
- 10-14 06:20  fleet/agents/A059/runs/20261014T025828Z-fleet05-A059-decomposition-depth
- 10-14 06:18  fleet/agents/A074/runs/20261014T030615Z-fleet05-A074-independent-reproducer
- 10-14 06:18  fleet/agents/A039/runs/20261014T025407Z-fleet05-A039-projection-under-restrictions
- 10-14 06:16  fleet/agents/A064/runs/20261014T030103Z-fleet05-A064-global-debt-potential
- 10-14 06:16  fleet/agents/A069/runs/20261014T030208Z-fleet05-A069-geometric-transfer
- 10-14 06:12  fleet/agents/A054/runs/20261014T025808Z-fleet05-A054-connectedness-alternatives
- 10-14 06:11  fleet/agents/A049/runs/20261014T025532Z-fleet05-A049-minimal-falsifier-extraction
- 10-14 06:06  fleet/agents/A029/runs/20261014T025327Z-fleet05-A029-child-deficit-transport
- 10-14 06:04  fleet/agents/A044/runs/20261014T025427Z-fleet05-A044-non-symmetric-gate-classes
- 10-14 06:04  fleet/agents/A034/runs/20261014T025347Z-fleet05-A034-phase-energy-transfer
- 10-14 06:03  fleet/agents/A009/runs/20261014T024630Z-fleet05-A009-fractional-incidence-optimization
- 10-14 06:01  fleet/agents/A024/runs/20261014T025222Z-fleet05-A024-biased-child-stability
- 10-14 05:58  fleet/agents/A019/runs/20261014T025011Z-fleet05-A019-orthogonality-extensions
- 10-14 05:58  fleet/agents/A014/runs/20261014T024736Z-fleet05-A014-overlap-beyond-worst-case-read
- 10-14 05:55  fleet/agents/A004/runs/20261014T024610Z-fleet05-A004-constant-and-unit-ledger
- 10-14 05:53  fleet/agents/A098/runs/20261014T024504Z-fleet05-A098-resource-reallocation
- 10-14 05:51  fleet/agents/A093/runs/20261014T024314Z-fleet05-A093-literature-and-priority
- 10-14 05:51  fleet/agents/A068/runs/20261014T023317Z-fleet05-A068-antichain-beyond-one-order
- 10-14 05:51  fleet/agents/A083/runs/20261014T023633Z-fleet05-A083-formal-core
- 10-14 05:50  fleet/agents/A043/runs/20261014T022706Z-fleet05-A043-prime-gate-decomposition
- 10-14 05:50  fleet/agents/A088/runs/20261014T024038Z-fleet05-A088-booleanity-referee
- 10-14 05:49  fleet/agents/A078/runs/20261014T023613Z-fleet05-A078-coding-and-padding
- 10-14 05:46  fleet/agents/A058/runs/20261014T022937Z-fleet05-A058-overlapping-compositions
- 10-14 05:44  fleet/agents/A073/runs/20261014T023508Z-fleet05-A073-certified-logarithms
- 10-14 05:44  fleet/agents/A038/runs/20261014T022516Z-fleet05-A038-occupancy-term-audit
- 10-14 05:43  fleet/agents/A053/runs/20261014T022917Z-fleet05-A053-near-tensor-perturbations
- 10-14 05:39  fleet/agents/A018/runs/20261014T022025Z-fleet05-A018-shared-data-collision-law
- 10-14 05:39  fleet/agents/A048/runs/20261014T022727Z-fleet05-A048-tensor-stress
- 10-14 05:35  fleet/agents/A013/runs/20261014T021710Z-fleet05-A013-representation-stability
- 10-14 05:35  fleet/agents/A023/runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget
- 10-14 05:34  fleet/agents/A028/runs/20261014T022306Z-fleet05-A028-stopping-tree-payment
- 10-14 05:28  fleet/agents/A087/runs/20261014T020842Z-fleet05-A087-restriction-referee
- 10-14 05:27  fleet/agents/A003/runs/20261014T021415Z-fleet05-A003-minimal-target-formulation
- 10-14 05:26  fleet/agents/A008/runs/20261014T021605Z-fleet05-A008-gate-label-compression
- 10-14 05:26  fleet/agents/A097/runs/20261014T021008Z-fleet05-A097-cross-route-transfer
- 10-14 05:23  fleet/agents/A017/runs/20261014T014813Z-fleet05-A017-recursive-addressing
- 10-14 05:22  fleet/agents/A077/runs/20261014T020716Z-fleet05-A077-sparse-defect-towers
- 10-14 05:19  fleet/agents/A022/runs/20261014T014918Z-fleet05-A022-one-point-surgery
- 10-14 05:18  fleet/agents/A067/runs/20261014T020120Z-fleet05-A067-hypercontractive-refinement
- 10-14 05:18  fleet/agents/A092/runs/20261014T020903Z-fleet05-A092-counterexample-referee
- 10-14 05:16  fleet/agents/A072/runs/20261014T020611Z-fleet05-A072-exact-walsh-engine
- 10-14 05:14  fleet/agents/A057/runs/20261014T015740Z-fleet05-A057-coherent-restriction-remainder
- 10-14 05:13  fleet/agents/A047/runs/20261014T015314Z-fleet05-A047-boundary-search
- 10-14 05:08  fleet/agents/A032/runs/20261014T015128Z-fleet05-A032-boolean-phase-realizability
- 10-14 05:07  fleet/agents/A062/runs/20261014T015800Z-fleet05-A062-influence-compensator
- 10-14 05:06  fleet/agents/A052/runs/20261014T015635Z-fleet05-A052-critical-source-structure
- 10-14 05:06  fleet/agents/A027/runs/20261014T015108Z-fleet05-A027-block-selection
- 10-14 05:05  fleet/agents/A012/runs/20261014T014452Z-fleet05-A012-sparse-activation-accounting
- 10-14 05:00  fleet/agents/A042/runs/20261014T015254Z-fleet05-A042-bias-endpoint-certificates
- 10-14 04:57  fleet/agents/A007/runs/20261014T014217Z-fleet05-A007-root-normalization
- 10-14 04:54  fleet/agents/A091/runs/20261014T013816Z-fleet05-A091-composition-referee
- 10-14 04:54  fleet/agents/A002/runs/20261014T013942Z-fleet05-A002-hardness-preserving-transformations
- 10-14 04:50  fleet/agents/A076/runs/20261014T013416Z-fleet05-A076-threshold-and-tribes-controls
- 10-14 04:50  fleet/agents/A086/runs/20261014T013711Z-fleet05-A086-joint-code-referee
- 10-14 04:50  fleet/agents/A056/runs/20261014T012909Z-fleet05-A056-balanced-composition
- 10-14 04:49  fleet/agents/A071/runs/20261014T013355Z-fleet05-A071-search-space-design
- 10-14 04:49  fleet/agents/A096/runs/20261014T013836Z-fleet05-A096-live-gap-ledger
- 10-14 04:46  fleet/agents/A081/runs/20261014T013521Z-fleet05-A081-dependency-certificates
- 10-14 04:43  fleet/agents/A066/runs/20261014T012949Z-fleet05-A066-semigroup-dissipation
- 10-14 04:41  fleet/agents/A041/runs/20261014T012508Z-fleet05-A041-weighted-threshold-fei
- 10-14 04:37  fleet/agents/A051/runs/20261014T012634Z-fleet05-A051-near-extremizer-definition
- 10-14 04:37  fleet/agents/A061/runs/20261014T012929Z-fleet05-A061-entropy-process
- 10-14 04:36  fleet/agents/A011/runs/20261014T011235Z-fleet05-A011-representation-existence
- 10-14 04:36  fleet/agents/A046/runs/20261014T012528Z-fleet05-A046-current-candidate-intake
- 10-14 04:33  fleet/agents/A031/runs/20261014T011913Z-fleet05-A031-convolution-identity
- 10-14 04:33  fleet/agents/A016/runs/20261014T011255Z-fleet05-A016-addressing-benchmark
- 10-14 04:30  fleet/agents/A021/runs/20261014T011316Z-fleet05-A021-rare-core-asymptotics
- 10-14 04:28  fleet/agents/A001/runs/20261014T011101Z-fleet05-A001-quantifier-audit
- 10-14 04:27  fleet/agents/A026/runs/20261014T011337Z-fleet05-A026-good-coordinate-erasure
- 10-14 04:25  fleet/agents/A006/runs/20261014T011124Z-fleet05-A006-posterior-forest-optimization
- 10-14 04:24  fleet/agents/A100/runs/20261014T010218Z-fleet05-A100-release-and-continuation-ledger
- 10-14 04:24  fleet/agents/A075/runs/20261014T005346Z-fleet05-A075-search-to-theorem-bridge
- 10-14 04:21  fleet/agents/A095/runs/20261014T010024Z-fleet05-A095-restricted-result-extraction
- 10-14 04:18  fleet/agents/A090/runs/20261014T010003Z-fleet05-A090-independent-reconstruction
- 10-14 04:12  fleet/agents/A050/runs/20261014T004109Z-fleet05-A050-repair-with-scope
- 10-14 04:12  fleet/agents/A085/runs/20261014T005642Z-fleet05-A085-certificate-adversary
- 10-14 04:11  fleet/agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard
- 10-14 04:10  fleet/agents/A060/runs/20261014T004659Z-fleet05-A060-composition-sharpness
- 10-14 04:09  fleet/agents/A045/runs/20261014T004049Z-fleet05-A045-biased-realizability-referee
- 10-14 04:09  fleet/agents/A070/runs/20261014T005025Z-fleet05-A070-analytic-route-referee
- 10-14 04:00  fleet/agents/A040/runs/20261014T003941Z-fleet05-A040-credit-insufficiency-tests
- 10-14 03:59  fleet/agents/A035/runs/20261014T003450Z-fleet05-A035-signed-cancellation-countersearch
- 10-14 03:57  fleet/agents/A055/runs/20261014T004129Z-fleet05-A055-extremal-obstruction-referee
- 10-14 03:55  fleet/agents/A025/runs/20261014T002956Z-fleet05-A025-rare-event-counterfamily
- 10-14 03:55  fleet/agents/A030/runs/20261014T003426Z-fleet05-A030-restriction-plateau-tests
- 10-14 03:47  fleet/agents/A005/runs/20261014T001325Z-fleet05-A005-noncircular-endpoint-referee
- 10-14 03:43  fleet/agents/A020/runs/20261014T002716Z-fleet05-A020-selector-boundary-tests
- 10-14 03:41  fleet/agents/A010/runs/20261014T001430Z-fleet05-A010-universal-residual-falsifier
- 10-14 03:39  fleet/agents/A094/runs/20261014T001244Z-fleet05-A094-proof-chain-challenger
- 10-14 03:39  fleet/agents/A015/runs/20261014T001450Z-fleet05-A015-minterm-barrier-analysis
- 10-14 03:39  fleet/agents/A084/runs/20261014T000747Z-fleet05-A084-continuum-parameters
- 10-14 03:38  fleet/agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly
- 10-14 03:33  fleet/agents/A079/runs/20261014T000722Z-fleet05-A079-correlated-auxiliaries
- 10-14 03:32  fleet/agents/A064/runs/20261013T235917Z-fleet05-A064-global-debt-potential
- 10-14 03:28  fleet/agents/A074/runs/20261014T000656Z-fleet05-A074-independent-reproducer
- 10-14 03:19  fleet/agents/A089/runs/20261014T000812Z-fleet05-A089-repair-specialist
- 10-14 03:11  fleet/agents/A059/runs/20261013T235852Z-fleet05-A059-decomposition-depth
- 10-14 03:11  fleet/agents/A049/runs/20261013T235808Z-fleet05-A049-minimal-falsifier-extraction
- 10-14 03:11  fleet/agents/A054/runs/20261013T235828Z-fleet05-A054-connectedness-alternatives
- 10-14 03:10  fleet/agents/A044/runs/20261013T235618Z-fleet05-A044-non-symmetric-gate-classes
- 10-14 03:09  fleet/agents/A069/runs/20261014T000110Z-fleet05-A069-geometric-transfer
- 10-14 03:06  fleet/agents/A009/runs/20261013T235139Z-fleet05-A009-fractional-incidence-optimization
- 10-14 03:05  fleet/agents/A019/runs/20261013T235305Z-fleet05-A019-orthogonality-extensions
- 10-14 03:05  fleet/agents/A039/runs/20261013T235428Z-fleet05-A039-projection-under-restrictions
- 10-14 03:02  fleet/agents/A029/runs/20261013T235347Z-fleet05-A029-child-deficit-transport
- 10-14 03:00  fleet/agents/A004/runs/20261013T235034Z-fleet05-A004-constant-and-unit-ledger
- 10-14 02:57  fleet/agents/A098/runs/20261013T235014Z-fleet05-A098-resource-reallocation
- 10-14 02:57  fleet/agents/A014/runs/20261013T235200Z-fleet05-A014-overlap-beyond-worst-case-read
- 10-14 02:57  fleet/agents/A029/runs/20261012T033113Z-fleet05-A029-child-deficit-transport
- 10-14 02:56  fleet/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority
- 10-14 02:55  fleet/agents/A019/runs/20261012T031916Z-fleet05-A019-orthogonality-extensions
- 10-14 02:53  fleet/agents/A043/runs/20261013T233947Z-fleet05-A043-prime-gate-decomposition
- 10-14 02:52  fleet/agents/A073/runs/20261013T234148Z-fleet05-A073-certified-logarithms
- 10-14 02:52  fleet/agents/A088/runs/20261013T234248Z-fleet05-A088-booleanity-referee
- 10-14 02:52  fleet/agents/A078/runs/20261013T234208Z-fleet05-A078-coding-and-padding
- 10-14 02:51  fleet/agents/A083/runs/20261013T234228Z-fleet05-A083-formal-core
- 10-14 02:51  fleet/agents/A058/runs/20261013T234047Z-fleet05-A058-overlapping-compositions
- 10-14 02:49  fleet/agents/A068/runs/20261013T234128Z-fleet05-A068-antichain-beyond-one-order
- 10-14 02:49  fleet/agents/A053/runs/20261013T234027Z-fleet05-A053-near-tensor-perturbations
- 10-14 02:49  fleet/agents/A048/runs/20261013T234007Z-fleet05-A048-tensor-stress
- 10-14 02:46  fleet/agents/A078/runs/20261012T023229Z-fleet05-A078-coding-and-padding
- 10-14 01:47  fleet/agents/A013/runs/20261013T222840Z-fleet05-A013-representation-stability
- 10-14 01:46  fleet/agents/A018/runs/20261013T222945Z-fleet05-A018-shared-data-collision-law
- 10-14 01:43  fleet/agents/A038/runs/20261013T223535Z-fleet05-A038-occupancy-term-audit
- 10-14 01:43  fleet/agents/A028/runs/20261013T223410Z-fleet05-A028-stopping-tree-payment
- 10-14 01:43  fleet/agents/A023/runs/20261013T223305Z-fleet05-A023-amortized-rarity-budget
- 10-14 01:40  fleet/agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement
- 10-14 01:36  fleet/agents/A087/runs/20261013T222530Z-fleet05-A087-restriction-referee
- 10-14 01:36  fleet/agents/A077/runs/20261013T222235Z-fleet05-A077-sparse-defect-towers
- 10-14 01:36  fleet/agents/A008/runs/20261013T222820Z-fleet05-A008-gate-label-compression
- 10-14 01:36  fleet/agents/A097/runs/20261013T222610Z-fleet05-A097-cross-route-transfer
- 10-14 01:33  fleet/agents/A003/runs/20261013T222630Z-fleet05-A003-minimal-target-formulation
- 10-14 01:32  fleet/agents/A092/runs/20261013T222550Z-fleet05-A092-counterexample-referee
- 10-14 01:32  fleet/agents/A057/runs/20261013T221645Z-fleet05-A057-coherent-restriction-remainder
- 10-14 01:27  fleet/agents/A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine
- 10-14 01:27  fleet/agents/A007/runs/20261013T220854Z-fleet05-A007-root-normalization
- 10-14 01:26  fleet/agents/A047/runs/20261013T221434Z-fleet05-A047-boundary-search
- 10-14 01:25  fleet/agents/A017/runs/20261013T220934Z-fleet05-A017-recursive-addressing
- 10-14 01:24  fleet/agents/A052/runs/20261013T221539Z-fleet05-A052-critical-source-structure
- 10-14 01:24  fleet/agents/A062/runs/20261013T221705Z-fleet05-A062-influence-compensator
- 10-14 01:21  fleet/agents/A032/runs/20261013T221334Z-fleet05-A032-boolean-phase-realizability
- 10-14 01:21  fleet/agents/A022/runs/20261013T220954Z-fleet05-A022-one-point-surgery
- 10-14 01:21  fleet/agents/A042/runs/20261013T221414Z-fleet05-A042-bias-endpoint-certificates
- 10-14 01:19  fleet/agents/A027/runs/20261013T221314Z-fleet05-A027-block-selection
- 10-14 01:15  fleet/agents/A002/runs/20261013T220534Z-fleet05-A002-hardness-preserving-transformations
- 10-14 01:15  fleet/agents/A012/runs/20261013T220914Z-fleet05-A012-sparse-activation-accounting
- 10-14 01:14  fleet/agents/A091/runs/20261013T220323Z-fleet05-A091-composition-referee
- 10-14 01:13  fleet/agents/A081/runs/20261013T220111Z-fleet05-A081-dependency-certificates

## What the agents say they learned (last lines of each LEARNED.md)

- fleet/agents/A001: Fixed-degree KL guard: coarse-graining each residual atom |T|<=L separately and all larger atoms into one tail preserves the full normalizer but loses mu_tail*D(conditional tail). For n>=max(6,2L+2),  / Shared-core quotient guard: for edited bent core and Q_r product AND2 signs, delta=2^-d,alpha=2^-r,w=4^(1-r),selector e=delta/2,core a=1/2+delta(1-alpha). Binary partner quotient loses e D0/2 with D0> / Neutral padded AND3 continuation: six-bit b positive when first three bits zero,c origin flip,I(b)=I(c)=3/4,delta1/64. With actual balanced Maj3 unlocked encoder, fixed full encoder erasure is NOT aut
- fleet/agents/A002: Stage5: deterministic parity-check greedy tags avoiding XOR sums of<=b-1 previous columns (including standard tag basis) yield distance>b with r=ceil(2b log2(2D)) when r<=D. For a one-point edit p=2^- / The seed-independent growing cutoff q(N)=max(1,floor(cube_root(N))) also retains the full universal optimal FEI constant with fixed rare/weak/mean/collision thresholds, because b_t/q(N_t)->infinity fo / Stage6 durable: Omega_ij=sum_T q_T[H(XZ)+H(ZX)-H(ZZ)-H(XX)] for actual Boolean quartets; physical query marginals are uniform and common retained q cancels. Row (3,-3,-2,-2) margin omega+2d=(29+18log2
- fleet/agents/A003: A003 stage3: Once-sliced odd majority has mean +/-rho, singleton and each influence rho, and B_i<=2rho. The zero-sum boundary derivative gives t c_t+(2r-t)c_(t+2)=0; even/odd derivative energies rho/2 / A003 stage4: A004 independently accepts both stage3 claims at original abstract scope. A026 signed shift kappa=log2(32/27) is closed at source scope. Shadow bank under interleaved actual queries obeys / A003 stage5: Distinguish A096 discarded mask-only KL L_d (~d delta) from retained seed shadow Q (~2delta), and from partner deletion M=downward erasure. On b=-1+2point and constant other child, actual
- fleet/agents/A004: Source hash convention: A003 hashes sorted compact JSON of statement and hypotheses, not the statement UTF8 alone. Recompute using source code; preserve both the historical hash and any explicitly lab / Stage 4: A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 independently accepted by A004 at full source scope. At one seed row, partner deletion L=M_z and unlocked shadow Q=B_z differ exactly by C_up in [0,de / Stage 5 durable facts: A003-RETAINED-POINT-SHADOW-SHARP-ALLOWANCE@1 accepted by A004 for the new all-d positive point bound; A003 independent acceptance of A004 prior criterion consumed. A0=2/ln2-2 bi
- fleet/agents/A005: Stage3 corrected-price transport: for every fixed seed with H-CI>0, Q_C=min_i[B_i+max(-sigma_i,0)]/Inf_i is preserved in the point-edit full-support limit. Dummy corrected prices grow like delta(seed) / Stage4 logarithmic code admission: D=tn tensor data bits plus r=min{s:2^s-s-1>=D} tags, distinct weight>=2 labels, gives distance3 with H=tHseed and I=tIseed+at most r. One-point flip makes negative c / Stage5 durable facts: Complete Gibbs surplus G_A+lambda I_A-J_A-|A|r=KI_A-L_A exactly, so lambda tuning cannot create payment. Signed physical interaction Omega_(A,B) has sharp absolute bound2min(|A|,
- fleet/agents/A006: Stage 3 durable interface: For fixed ownership tau, incoming Laplacian minors rooted at exactly one vertex per source SCC give attached-forest polynomial T(x), weighted by root pi. Exact actual-run B  / Stage 4: For any graph prime table with both endpoint orders, t(singleton)=1/4 and t(pair)=1/6. Every inclusion-maximal matching M in G[A] leaves independent unmatched U, so choosing a neighbor for ea / Stage6: Full partition star differs from matching-star when hub owner is an edge OUTSIDE the present leaf set. For k>=1, W_hub+B=lambda_B[(k-1)!/(3*8^k*k*(k+1)) + k!/(16*8^k*(k+1)*(k+2))*sum_outside l
- fleet/agents/A007: - Exact distributed multiplier per old forest is a marked exponential coefficient: c>=2 uses pi_a(l) z f_l' and (u+1)_(c-2)u!/prod pi; c=1 uses u!prod f. Actual TREE components are required. This does / - One-control susceptibility t_l=(s_l+1)^(gamma(s_l+1))/(s_l^(gamma*s_l)(kappa_l+1)^gamma) determines the root mean. Owned-size proportions cannot replace this tilt: supports {0,1,4},{2,3,4,5}, T={0,1 / - Same overlapping record has J=16*2^(-6/5)+8*(4/9)^(6/5)>8 and one-core Dprime/(pD)=97/98. Preserve that signed normalizer, all other spectral sectors and inherited pR_g; one refund is not universal 
- fleet/agents/A008: Stage 3 durable fact: actual conditioned partition-forest mass Q_tau=product_used(lambda*t)/D times N_s(T), where monomial h has N_s weight product_u[product_j h_j!/((c_u+1)(c_u+2)binom(s_u+c_u-1,c_u) / Stage 4 correction: size-one probability 1/2 is not full singleton t. Width-two two-order t=1/4, pair t=1/6; common-first t_common=1/[2(1+a)], t_private=a/[2(1+a)], a=2^-6/5. Prior formal mass theorem / Stage5 durable diagnostic: connected graph edges h-x_i, h-y, y-z has I=5/4+m2^(-m-1), P({z})=1/16. Uniform lambda1/(m+1) yields full C_part/I>(1/24)log2(m+1) and R/I>(1/24)log2(m+1)-log2(72). SAME-pri
- fleet/agents/A009: Stage3: both endpoint orders in width-two edge gates make theta=1 and exact t(singleton)=1/4, t(pair)=1/6. Matching actual-run multiplicity pays complete K_n nonempty cost <=185I/6 for all n>=4, despi / Stage4: complete star mass is multiaffine in global lambda; c_e=lambda_e d_e W/W averaged over actual P. All edge c_e>0 from monotone singleton spectra. With >=2 edges, degree>=3 restriction forces C> / 2026-10-14T06:02:16.180341+00:00 | Arbitrary-core/private-leaf payment: weights private 1/(2m_i), core 1/[2max(d_i,d_j)] are globally feasible. Private-only selected traces still pay ALL core absent r
- fleet/agents/A010: 2026-10-14: For graph positive edge prime tables with one full order, every independent selected set has exact surrogate mass W_A=product_j[(1/4)sum_incident lambda_e r_e(j)^(-6/5)]; all root choices  / 2026-10-14 stage4: Width-two positive edge primes with BOTH orders satisfy Q_part(A)<=W_B(A)/D<=72^|A|Q_part(A). This controls negative residual credit by log2(72)I. Uniform max-read weights can fail  / 2026-10-14 stage5 durable: a full-support star spectral sector forces every prime edge used; its root-law gradient contribution is D/prod lambda, so the uncapped simplex tangent gap diverges at ALL fe
- fleet/agents/A011: Subprobability physical inheritance must retain massM: R_b=M(2r*pi_b)/Z_b, Zsum2M. The exact query ledger includes log(Z_b/M), notlogZ_b alone. Product-compatible zero true fibers retain off-support i / Stress: bent_k times signedAND3, one dummy and selector, bent edit point weightk/2, k even>=2. Source c=k+4,S4=k-1; rootCE=c+B, rootI=Ig-t, margin>=k-1-(k+12)t>0. Weak dummy query cost/influence>k/2+5 / 1,097,416 exact checks:4240 all-small Boolean point roots/12720 supplied references;3 direct weak queries;6 two-query histories/24 leaves;432 subprobability queries;64 combined terminal-model cases. T
- fleet/agents/A012: * 64 SLSQP conditional-mean starts are floating evidence only. Best rounded ratio3.87321 at theta155/256 is an actual one-row controller profile. No proof that arbitrary extremizers have one changed r / * Exact stage checks257212 assertions: continuum5953, actual/debt243506, independent positive-log/coverage/nonmember7710, original-source-cert43. All jobs under55 seconds, max actual dimension12. Sour / 2026-10-14 stage6 durable: For G=c(s), H=c(s)(1-2 1_W(s)1_E(V)) on<=3 shared bits, arbitrary common private event, exact B=2(d-m theta^2/8)+sum Phi((a-theta b)^2,(theta b)^2), all realtheta satisfy B<
- fleet/agents/A013: Stage 3 constant boundary: removing a last satisfied literal yields a constant-true gate and hence a constant child; use the vacuum reference. Density doubles per removed literal, but density-one is n / Stage4: Exact conserved mux ownership B=2(d*-delta)+B_C makes three-bit arbitrary-private payment B<4d* rigorous for d*<=1/32 (B/d*<29/8) or d*>=1/6 (log2(5/4)<1/3). Remaining arbitrary-private band i / Stage5: Pure3-bit shared phase versus two-row arbitrary private-event edits (events may correlate) has exact selector d=(p+q)/8,shared minority delta=(p²+q²)/8 and B=2(d-delta)+sumPhi((chat-k)²,k²),k=
- fleet/agents/A014: Stage 3 durable obstruction: for disjoint equal-width positive clauses p=2^-w,c=(1-p)^(m-1), local conditioned derivative residual is zero but bad off-clause degree mass=I(1-c). Thus conditioned Fouri / Stage 4: C=h_x(Y)k_x(Z), nested blockers on disjoint private cubes. Physical Ix=A0-A1, private I=sum_i[b_i I(1-2h_i)+a_i I(1-2k_i)]/2. Normalized blocker entropy = weighted terminal blocker entropies  / Stage 5: exact component spectra make stage-4 row mixture equal actual row law. Empty reference mass q_e=(A0^2+A1^2)/(4s)>=s/2; actual blocker spectrum <=2Q_C. Complete normalized output reference exc
- fleet/agents/A015: Full-support tail CLOSED by A007-RETAINED-OWNERSHIP-TAIL-AND-ROOT-BUDGET@1, reconstructed downstream by A015 with own upstream-envelope authorship disclosed: multinomial*A<=1, finite-N label depletion / Arbitrary-support tail transplant is false even on exact singleton primes of OR_n: ownership forced, H=log|T|, normalized nonempty spectral mean >=.5logceil(n/2); positive full-set n8192 contradicts t / On SAME OR_n activated prime table, beta1/n: root credit2^(s-1) and s! actual chronological stars give J1=s!/n^s*2^(-(s-1)/5). Exact conditioned selected Q_star=s!/[24D'n^s s^2(s+1)] [alpha/(4(1+alpha
- fleet/agents/A016: For any fixed normalized finite-CE Q, both children may inherit its coordinate marginal; average child spectrum equals erased parent spectrum, giving exact CE_parent=avgCE_child+sum P log(Qmarg/Q), no / A020 opposite-means fixture: Qh=(Ph+point_q)/2, QF gate uniform with data(Qh*Ps+point_empty)/2. Query q then v0 with SAME marginals. Fresh-to-inherited conversion E<delta^2 explicitly retained. J<35/1 / After all v erasures, actual q0,v=0 has core+1, I_F=3/4, CE=5-[5log2(9+delta)+3log2(1+delta)]/8>3 for k>=6 (577^5*65^3<2^64). This is a terminal reference-eligibility failure, not FEI or an unpayable 
- fleet/agents/A017: 2026-10-14 stage5 (run 20261014T043353Z-fleet05-A017-recursive-addressing): Closed saved all-weak rank-two coset-minus-one collapse in original coordinates; parity extends adaptive zero K4 bill thro / Stage5 structural lesson: At D5 with seven edits, odd pivotal-edge parity makes polar influence either1/16 or at least3/16. All weak rows force Qw constant on E; alternating rank then equals2, E is a  / 2026-10-14 10:26 UTC stage6 20261014T102650Z-fleet05-A017-recursive-addressing: Exact durable facts: every BooleanD<=5 phase has K4-good maximum-influence coordinate; max1/16 implies five-edge bound
- fleet/agents/A018: Do not identify posterior KL refund with a change of data prior. CE_separate-CE_joint=E_R log(qjoint/qseparate) is signed. Actual core references refund TC. Eligible UNIFORM references for private poi / A019-INTERNAL-PIVOTAL-EDIT-ACCOUNT@1 independently HOLDS in full. The effective edit is empty when a shared edge is unchanged, so2kappa-J=-J then, not0. General signed W and complete terminals must re / Validation18690 exact checks:534 complete-reference cases (128 non-flat), two signed prior choices, old eleven-bit control,528 ownership cases and analytic/profile checks. Source-author checkers were 
- fleet/agents/A019: For a=g,b=g*(-1)^1_E, 2I((a-b)/2)-(Ia+Ib)/2=P_in-P_out, the original core pivotal energies inside/outside E. Crossing edges cancel exactly. Half-private holds iff P_in<=P_out; independent edit regions / ## Private query empty-row repair, 2026-10-14T06:11:46.573283+00:00 / For gate F=1 at x0 and h*s at x1 with nonlinear two-bit s (mean+-1/2), Psi activation profile has phi(beta)=Psi(beta/2), phi second derivative=(1/4)log2(beta^2/(4-beta^2)). Its negative is even decrea
- fleet/agents/A020: - Actual query erasure B=(1+a)/2*h2(a/(1+a))<delta/2, hence K1 good. All core and full activation references are rate4 eligible. An untouched averaged private half-slack>=1 pays one insertion<5/8 leav / - Exact entropy/reference insertion needs full terminal CE and both posterior refunds. A reference-only ghost budget on a vanishing true row can cause a fixed lost refund even when actual entropy quer / - Next must preserve this incoming reference and booked debit through a second v query. Resetting to a newly selected child mixture or exact spectrum changes the task.
- fleet/agents/A021: Stage5: For nested point selectors of widths r,s and three balanced cores z*b,z*b_u,z*b_v from any even-m bent seed (m>=4), actual terminal decrement D=mV+L+3cV+E, |E|<=8c sqrt(delta)V uniformly in wi / Stage6 flatness-free refund: same two distinct point edits to ANY Boolean seed on m>=1 bits give D<=Rstar+(11/2+3c)IC<Rstar+10IC, all positive widths. DO NOT extend the old lower bound Rstar<=D to non / Stage6 owner completion: On A025 quadratic-bent conditional two-edit family (even m>=4), ANY common activation width k>=0,p=2^-k, original fair nested controls, query x first. Exact Rroot=p(3m+2+3k)de
- fleet/agents/A022: Stage4 one-point arbitrary-controller transport: F=b(x)(1-2*1_(x=v)*A(z)), quadratic paired bent k=2m>=4 and arbitrary independent indicator A. Expose first bit of every pair, then STOP. Surviving per / Stage5 growing edit theorem: k=2m>=4 paired quadratic bent, q distinct vertices, arbitrary possibly dependent A_j independent of data. General q<=2^(m-2): H<=K I_data+2^-k sum H(1-2A_j), K=max(4+2c,[4 / Stage6 root density: arbitrary Boolean seed b, distinct data vertex flips with dependent indicators on independent controls. Exact controller spectral marginal R=(1-qdelta)point_empty+delta sum ahat_j
- fleet/agents/A023: 2026-10-13: For A=X(U OR V) OR WUV with one fair X and disjoint point blocks, balanced core, beta=q+r-qr, eta=pqr, pi=(beta+eta)/2, e=beta-eta, d_X=e/2 and Jrem=(J(WUV)+J(U OR V))/2. The difference in / 2026-10-14: For arbitrary G,H sharing a data cube and one fresh point block alpha=2^-s, original gamma=P(G!=H) stays fixed through all live histories. Sum of actual erasure costs is <=2(1-2alpha)I_S+4 / 2026-10-14 stage5: For nested point blocks and three shared cores, the actual source outer product includes inner-control influence I_B. Nested reserves are R_data=2a(1-a)[(1-b)I01+bI02]+2ab(1-b)I12 a
- fleet/agents/A024: Complete controller prefix bad bill is r sum_liftedbad p q_w+I(h)/2 sum_liftedbad p d_w, with actual terminal t H(h),t I(h),t Q(h). A bound on controller own bad q does not bound its lifted bad pivot  / K7 scope repair: fixed five-bit modules give every controller query influence>=13/512 and every terminal core query>=1/16. Integer 13^13*499^499>2^4517 implies h2(13/512)<7*13/512; all controller-firs / A046@2 rare-row constant/nonconstant moments and B/d<1781/480 when e<=1/8 independently HOLDS without repair. eta<=8e^2/25 uses compatible point geometry; neither its whole reserve nor arbitrary-contr
- fleet/agents/A025: 2026-10-14: For arbitrary Boolean G,H and a fresh j-bit point-switch, gamma=P(G!=H)>0, B/d<=2+log2(e)/sqrt(e gamma); gamma>=1/4 guarantees strict K=4 goodness uniformly in selector depth. For A=WUV OR / 2026-10-14 stage4: A023 v3 additional whole-block theorem independently accepted at exactly that scope: H-H_T<=(11/2)I_S+2alpha(1-alpha)I(GH), E_B<=(5/2)I_S+R, with full terminal entropy and physical  / 2026-10-14 stage5: for quadratic bent b_m, cores zb and two distinct flips at (y=0,x=0),(y=e0,x=0), pi=(1/2,1/4,1/4), the unresolved x query has d=2^-m/2, symmetric bank release=3d/2, true B/d>=3/2+m/
- fleet/agents/A026: - Common-dyadic integer interval sums exactly reproduce repeated Fraction sums and cut the guarded checker runtime; preserve partial certified rows and freeze any continuation. / Stage5: B_z<=h2(delta)<=I(g+g-). W=Var(h)I(g+g-) funds all encoder shadow charges under arbitrary fixed-partition interleaving: Q+G+L+EWleaf=Wroot. Actual exclusive pivotal account X is conserved; W<= / Stage6: V=Var(h)h2(delta) is a nonnegative mixed-query shadow reserve: encoder drop gamma^2 h2(delta), data drop Var(h) I(disagreement;query). Q+G_H+L_H+EVleaf=Vroot; every difference from stage5 boun
- fleet/agents/A027: For the exact arbitrary-controller activation remainder R(p,d), p<=1/2, R_dd=16p[ln(1-2d)-(1-p)ln(2d)-p ln(1-2pd)+p ln(p)]/ln2. The bracket decreases in p throughout d<=d_star=(1-1/sqrt2)/2, and its p / Actual core-only leaves with negative probabilities<=d_star give Pi_H(F)-pPi_H(u)<=0 by one endpoint Jensen refund; controller Hplus remains in terminal entropy. Parent bias<=d_star/2 ensures every fi / Sharpness: at p1/2 and d_star<d<1/2 curvature is negative. Distinct dyadic nested negative sets on a common finite core are actual nonconstant Boolean sibling witnesses to any band extension. Fixed se
- fleet/agents/A028: * R is a nonnegative supermartingale under arbitrary physical control/data interleaving: controller release=(p0-p1)^2 I(GH)/2, data release=2p(1-p)Inf_i(GH)<=2actual Inf_data(F). One stopped-tree Rroo / * Exact AND2 guard: a=(-1,1),G=(1,1),H=(-1,1), p1/2; rootH2, branch/query-child entropy0; datareleaseR1/2 and actual queryI1/2. Bare-release residual fails by3/2; any added local data price in that ru / * A023 point-block theorem already has scoped A025/A029 acceptance; A056 structural history/KL closure releases zero controller KL, not a paid entropy bank. NEXT actual non-flat data residual with car
- fleet/agents/A029: - Primary stage2 pilot caught original-coordinate/local-index confusion in influence vectors; corrected before full search. Physical coordinate labels must be translated to the ordered free-variable i / 2026-10-14 stage4: A023@3 arbitrary-shared-data whole-point-block clause independently HOLDS; other bundled clauses excluded. Two nested blocks f=g0+A(g1+B(g2-g1)-g0), a,b, terminal weights(1-a,a(1-b) / 2026-10-14 stage5: A023 stage5 independently accepts our stage4 nested owner/signed algebra only. Sharp all-dimensional two-point-block DATA reserve conversion: Rdata<=kappa Rstar,kappa=(2-a-b)/(1-ab)
- fleet/agents/A030: Two-dictator wrapper F_h=((1+h)/2)y0+((1-h)/2)y1 obeys H(F)=H(h)/2+A(Eh), I(F)=1+I(h)/2, where A is even, decreases from2 to0 and is4-Lipschitz. For any prescribed adaptive controls-first tree, [Q_C(h / For F=C_h*u+(1-C_h)*v on three independent blocks, delta=(1-Eu*Ev)/2 and H(F)=delta H(h)+qH(u)+(1-q)H(v)+B(Eh;Eu,Ev), with B(+-1)=0 and |partial_b B|<22delta. Thus any control reveal after partial ind / For independent cores selected by finite label kappa, actual controller boundary reserve has unique mean-only harmonic extension P=sum_e product_j(1+e_j m_j)/2*r_e, using one common own-history contro
- fleet/agents/A031: Private derivative support e_i=2q_j[1+(1-q_k)(1-q_l)]/8; own retained-frequency hit mass1-2q_j has equal signed endpoints and logprice1. Thus M_i<=3e_i and allshared cost<=4(2+log2euler)I_private, giv / Local child trace sufficiency survives restrictions; OWNER ADMISSION does not. From widths(1,L,L), X1=0 leaves a_a=a_c=-1/2,a_ac=-(1-2^-L)/2, I_private=L2^-L/2, M_shared>=(1-2^-L)^2/2. Fresh child pri / A035 review of prior three-state tribes record is PARTIAL sections1-4 only; activation and quantitative degree corollary not accepted by that receipt. Incoming-reference delta-minus-K ledger in its ne
- fleet/agents/A032: - Existing45088-row catalogue has144 odd-mixed rows, norms1 or5; four-data common odd-mask covers would need totalnorm64 but can reach at most20. Finite exclusion depends on existing completeness, not / - Independent n4 audit covers32768 global-sign representatives,5280 admissions, exact physical edges and118 log signatures. NEXT must move to multiple-nonfair/nonproduct complete-core admission/paymen / 2026-10-14 stage6 durable result: A nonzero ternary integer row with product squared spectrum has dyadic squared norm whose reduced odd numerator is1 modulo4. Primitive coprime pair norms have odd par
- fleet/agents/A033: - A031 v1 anchor and no-go claims independently reconstructed using physical multiplication isometry; reviews locally saved pending adoption. A033's class consequence is pending A088/A094 review. No n / - Fixed signed-order G_(K,w) no-go imported from curated route-map section 3. Fixed atom-cap cyclic no-go is distinct and only available as an audited summary; original definition/family/checker still / 2026-10-14T05:38:39.163838+00:00 - Exact endpoint: any integer height-two coordinate-product Fourier row with exactly2 nonfair marginals has at least2 fair marginals. Remove deterministic characters, 
- fleet/agents/A034: 2026-10-14: A079 independently accepted original affine quadratic-row theorem without repair (run20261012T044009Z). For two-address product rows with odd shared M, primitive Walsh scale is1 and all pa / 2026-10-14 stage5 CORRECTION: gcd_J D_J|3t was not proved; sum_J(t+4t_J)=0. Use A034 odd-mask v2 only: per-row D_J|(t+4t_J) and concentrated D|3t remain accepted. The standalone extra coupled statemen / 2026-10-14 stage5 ALL-PRODUCT RESULT: For an integer height-two product row reduced to N nonfair/m fair coordinates, primitive scale is a power of two and oddpart(k)>=5^N, while k<=4*2^(N+m). For N>=4
- fleet/agents/A035: 2026-10-14 stage3 durable fact: point-flipping a shared parity destroys disjoint Fourier rows. Exact ledger B=pi beta+I_Pbar(selector;branch|retained row)+(B-Bbar); only the middle term is necessarily / 2026-10-14 stage4: for shared-phase point surgery, signed core ratio ell has<=4 types; other free selector-frequency presence collapses likelihood to1/(10d) or1/(26d). Otherwise preserve counts A,B1 a / 2026-10-14 stage5: PRIVATE DATA EXPOSURE is not spectral conditioning. Incoming rbar=(r0+r1)/2, mubar=sum_s d_s/(2d)*mu_s. Parent spectral-collapse delta and physical-child K are distinct nonnegative 
- fleet/agents/A036: Actual full-support all-zero physical point flips preserve the addressing completed slope via the reusable bound |T_b-T_c|<=h2(rho)+n rho+rho/ln2, rho=(||b||1+||c||1)^2||b-c||2<=1/2. The l1 price is e / Exact outputs: rational log/exponential intervals, outward rational-grid serialization. Family spectra and squared correlations can be rational even when amplitude coordinates contain radicals; factor / Stage3 owned occupancy history: reached F=-1 on x0,a1, v_n on x1,b1, + otherwise, v_n a rare point defect. Original completed max-entropy nonempty reference retained through a then data; ALL n>=2 have
- fleet/agents/A037: - A fixed epsilon root-reference ratio bound survives every common joint stochastic history. Conditional references differ by at most2epsilon, regardless of depth. Total outcome KL and rootKL each dif / - The intermediate conversion diagnostic is not a prior exercised reset. An actual booked debit needs the original bank reduced explicitly; hypothetical favorable root credit does not prove upstream/c / - Independent checker imports no peer code. 2,750 exact likelihood/interval checks in0.1716114s, <50MB estimated. Complete canonical signs are certified, decimal displays only explanatory.
- fleet/agents/A038: - Genuine actual child S4=4I-H is certified individually positive. D+<mean S4/8; withdrawing once preserves both terminal entropies and at least 7/8 of that dedicated surplus. This is conditional owne / - Prior A038 reset/occupancy certificate independently accepted by A039 without repair; observed source-bound review retained. A039 full continuation is consumed at named identity scope, not newly acc / - Exact Fraction log intervals may serialize beyond Python integer-string limits: persist outward denominator-10^30 enclosures, keep full exact arithmetic for signs and preserve failed serialization r
- fleet/agents/A039: Source-owned occupancy root bank A=D(P||M) transports exactly as A=E_erasure+O_outcome+mean inherited child KL under the same physical coherent kernel; retain normalized child references, do not creat / ### Stage5 durable facts: final-frontier conversion / For a fixed inherited root occupancy reference, two physical queries obey A=E_tot+O_tot+K_end and final D=TC_end-K_end-E_tot=O_tot+TC_end-A. Convert once at final frontier; do not spend a first-fronti
- fleet/agents/A040: A046-SEPARATOR-LAYER-CUTOFF-RESERVE@1 independently HOLDS. V_j is exactly the physical expected sum of eligible future face costs; expected drift c_j for j<=m,0 for j>m. It is an M-unit reserve, not r / ## Stage 5: arbitrary-bias rare rows survive core-data exposure / A046 v2 full exact claim independently HOLDS. For a=1-Eg arbitrary[0,2], nonconstant moments are 2a eta-a^2eta^2,-a^2eta e,2a e-a^2e^2. With rho=2^-(j-1),d=rho a e/2, qstar=2a eta-a^2eta^2-rho a^2eta 
- fleet/agents/A041: * Old majority control has reverse K_B=P_mixed; max Z1/2, C_star=E_mixed, KLln2 and positive taxln2/4 cancel exactly. / * A one-bit physical direction ALWAYS gives K=P_mixed, even for arbitrary Boolean branches. This is a complete owner identity, not an entropy theorem. On recovered OR-AND guards it keeps C_star<=E_mix / * Do not apply mean-only pair funding or conditional-Boolean assumptions to the selected reference. Ordinary KL needs the harmonic factor under degree tilt. First open line is selected C_star or signe
- fleet/agents/A042: Stage4: exact slack S=4D-2R-E_single=sum_i v_i[2(d_i-|c_i|)+2|c_i|(1-|c_i|)-h(|c_i|)]. Here d_i=E Di^2 and d_i-|c_i|=2min(P(Di=1),P(Di=-1)). For prime mask33152 with first-three fair biases, D=(5+14z- / Stage5 coherent-face: prime56067 in rare coordinates x=1-b,y=1-c is f=-1+2z+2xy-2z[ax+(1-a)y]. Le=4alpha q(2-alpha-q), Ld=4(1-alpha)q(1+alpha-q); exact D=Le e(1-e)+Ld d(1-d)+(uw/4)(d-e)^2+4ed(1-e)(1-d / Stage6 rare-selector: for band/parity family n=16r^2, selector eps<=1/2, m=2eps*a, V=4(1-eps)+eps*E Zg^2-m^2, exact pair residual=choose(n,2)h(m)/4 versus kappa bill=choose(n,2)kappa(m)V/4. Bill/D>=ep
- fleet/agents/A043: - Next obstruction: prime56067 positive on A={Y1=1,Y2=1,Z=1},B={Y1=0,Y3=1,Z=1},C={Y2=0,Y3=0}. Net delta loss=-2v1*p2*p3*p4*(1-p4), uniform-1/8; component deltas5/16,5/16,1/4, actual3/4. Agreeing share / - Deterministic endpoint checking: remove zero-coefficient entries before comparing rational-log dictionaries. Preserve the true analytic contraction instead of treating a zero dictionary key as mathe / 2026-10-14 stage5: For reflected prime56067, Delta=B+2T and E_ge2=ln4*Delta+G with G=2T A(q)+2Tx A(alpha)+2Ty A(1-alpha)+(uw/4)h(d-e)<=6T. Universal signed singleton reserve yields E<=(6+ln4)Delta, he
- fleet/agents/A044: Sharp unequal-mean mux: K(q)=2+2[1+g(max(q,1-q))]/ln2, g(t)=t ln(1/t)/(1-t); sup_q K(q)=2+4/ln2. Mean geometry v0+v1>=d(2-d), d=|m1-m0|, pays d^2 ln(4/d^2)<=2(v0+v1). Fixed-q extremizers approach oppo / Stage4 shared-guard lesson (actual prime56067): events a=b=z=1, a=0,c=z=1, b=c=0 are exclusive. Delta-sum componentDelta=-2v_a p_b p_c p_z(1-p_z). On p_a=p_z=1/2,p_b=p_c=1-e,r=1-e: Delta=2re(1+2re),L= / Stage5 integer profile: Z_S=(1/2)sum_b(-1)^(|S|-|b|)f(b,x_notS) is integer; E Z_S=2^(|S|-1)c_S,Var Z_S=4^(|S|-1)/v_S sum_{T strictly containing S}P(T). Integer Z^2>=|Z| gives h(EZ)<=2VarZ even if |EZ|
- fleet/agents/A045: Stage 3 durable facts: Mixed spectral conditioning need not preserve Boolean admission at inherited physical biases (biased one-bit marginal (0,1); fair AND4 split2+2 marginal (0,1/3,1/3,1/3)). A join / Stage4 durable facts: Count-tail g_j physical derivatives have disjoint supports at each edge, even under unequal biases. Thus I(sum alpha_j g_j)=sum alpha_j^2 I(g_j), although their function values/F / Stage5 durable facts: A044 integer mixed physical profile has mean2^(|S|-1)c_S and variance4^(|S|-1)strict_mass/v_S; entire local claim including degree3 constant2+6/ln2 and genuine disjoint closure i
- fleet/agents/A046: Stage 4: For any point switch G+A_j(H-G) with disagreement gamma>=2^-D, possible strict K4-bad queries have j<=ceil(log2(D+1))+2. For WUV OR S(U OR V) with balanced g, D=min(R,T)+1 suffices. Vj=2^-j[M / Stage 5 durable: A040 independently accepted A046 v1 without repair; original V envelope still has log-width obstruction. For balanced compatible overlap, eta<=8e^2/25; separating full constant row gi / 2026-10-14 stage 6: With WUV controls unexposed, arbitrary conditional core bias gives theta=eta/e<=1/5. If a e<=1/16 every separator layer is K4-good (1251/320); otherwise every j>=4 is good (53/16).
- fleet/agents/A047: Stage4 durable repair: Under product biases, spectral deletion r_i=4p_i(1-p_i) times consumed physical i-influence. One coordinate-product deletion reference gives H(D|S)+E KL=sum a_i h2(r_i/a_i), no  / Stage5: Inherited same-kernel child reference likelihood is 2q_B(b)*p_e/q_e. On identical erased supports, child conditional spectator matching is equivalent to constancy on each branch-support graph  / Stage6: Fixed-reference full liability is A+[D-4R]_+, not conditional KL alone. If root CE<=M and root/frontier H>=h*, it is <=M-h* and can be booked once from actually unused certified final S4. For 
- fleet/agents/A048: A050 active deletion entropy e=H(D|S)<=a h2(R/a), including normalized reference/KL, zero-reservoir and conversion clauses, independently accepted unchanged. Shared-core data is admitted for this zero / ## Stage5: exact conditional-k activation admission and arbitrary terminal (20261014T052201Z) / For nonconstant controller activation 1+A(g(U,Z)-1) resolving both outcomes, hereditary controller-independent k(Z-frequency|U-frequency) exists iff E_Ug is constant in Z. Pure-Z mass beta copies as (
- fleet/agents/A049: - Local block checks now close the lead-assigned finite domain. The updated unpaid cost is reference injection/reset on actual descendants with one prescribed root witness and terminal entropy; next e / 2026-10-14T03:12:19.948864+00:00 | Essential fixed-prefix compression: an arbitrary k-bit core with r fixed prefix queries essential in every reached cell satisfies sum queried influences >= (2^r-1)*2 / 2026-10-14T06:16:33.030451+00:00 | Core-data common-factor audit: for F=y*(1+a*(1-z)*(g-1)), alpha=Pr(g=-1)>0, contracted inactive duplicate labels give kappa=1/2, d=alpha/2; before parity kappa=alpha
- fleet/agents/A050: Stage3 certificate lesson: indexed parity k=2 has j_k=1 and zero injection, so use k>=3 to test that obstruction. Exact r=2,k=3 joint confirms positive injection with 2 retained terminal entropy bits. / Stage4 durable repair: actual p_v(c,u,z)=pbar_v(c,u)k(z|u) and complete q_v=qbar_v k with one hereditary normalized k preserve every controller entropy/physical-influence/Bayes-erasure/outcome/signed- / Stage5 durable repair: after erasure and SAME normalized physical channel, full-support r=p_e/q_e can vanish. On occupied branch/T row m=E_Qr, ell=r/m; inherited spectator KL<=min(log max ell,log E_Q 
- fleet/agents/A051: - Universal entropy edit bound: H(f^E)-H(f)>=4E[1_E f G_f]-(8/ln2)|E|/2^n, G_f=sum ahat log2(ahat^2)chi. Proof: -t^2log2(t^2)+3t^2/ln2 convex on[-1,1], including zero, then Parseval. Influence edit ex / - Finite epsilon-extremality gives sum_E fG <=(K/2)signed_boundary+(2/ln2)|E|+2^n epsilon/4. Exact critical selected witness has fG+K pivotal_degree<=Kn/2+2/ln2 pointwise. Near-extremality must specif / - Stage6 140390 exact assertions across all278 tables n0..3 and65808 ordered edit pairs PASS, with6014 separate-representation checks. A052 compatible Gibbs sections1--3 independently hold; no fresh i
- fleet/agents/A052: Stage4: signed pair collision equals singleton collisions plus P=sum4(alpha delta+beta gamma)^2/q minus two nonnegative exact weighted-Cauchy merging refunds. P<=2 I_pair and C_k>=2 beta_k give C_pair / Stage5: genuine physical ratio criticality forces every influence<exp(3)2^-R, because R*d<=L<=h2(d)+(2/ln2)d. Exact singleton Gibbs bank includes minority KL and recentring slack. Actual conditional i / Stage6 durable restriction (2026-10-14): for K>=0, W(E)=W(E+)+W(E-)-K e(E+,E-); all signed cuts iff both induced-sign capacity-K/2 flows have divergence>=fG-lambda+(K/2)p. Use the complete parent G, n
- fleet/agents/A053: Packed new singleton rows have mass4p-8sp^2, with B=J=1 per normalized row; occupied rows contain minority4sp^2<=4p/(n+1). Consequently L_i<16p,V_i<19p and V_pair<54p, uniformly in n>=3. Physical indi / At K>=8 a violating one-point distance-three near-code root has D+S_i<0 at this max-influence coordinate, so average actual-child deficit>D_root>0. No such source is a least-dimensional K-violation or / A052 weak-critical Gibbs bank@1 independently accepted at complete analytic scope; no source counts adopted. The outstanding interface is actual distance-two signed-row payment after the paid query, p
- fleet/agents/A054: 2026-10-14 durable extension: For any component with physical A-projection measure mu and mass p, every partial Fourier row is supported in that projection. Its normalized Fourier entropy and its phys / 2026-10-14 / 20261014T025808Z-fleet05-A054-connectedness-alternatives: Exact natural sign/raw correction T(p)=h((1-2p)^2)-4h(p^2)-8ln2 p(1-p), with T''=16ln(2p/|1-2p|). T+(8/e)p ln p is convex, so i / 2026-10-14 / 20261014T055856Z-fleet05-A054-connectedness-alternatives: Actual connected-component fiber information W_A=sum_k E_Y m_ky log2(1/m_ky)=Q_A+pH(L|Y,U) satisfies EA(g)>=W_A/2 because actua
- fleet/agents/A055: Stage3 durable facts: singleton paired row c=4e(1-e), phase Fourier TV=e in [c/4,c/2]; 2 beta<=C<=4 beta; L<=h2(C/2)+C. On a least-dimensional K-violator, actual S=-E D_K(child)>=0 and O=Inf-beta>=0 g / Stage4 durable: T=sum O_i+sum both pair merging refunds. T=0 iff Boolean f constant: zero O makes squared Fourier magnitudes downward-monotone; zero refunds plus monotonicity force every face determin / Stage5 durable: two tags U(0,0)=-1,U(0,1)=h^m,U(1,w)=1 connect both signs, H(U)=mH(h)/4+O(1), I(U)=mI(h)/4+1,c=(3-Eh^m)/4. Rare r=ceil4log2(m+1) activation+2dummies+one inactive adjacent flip keeps bo
- fleet/agents/A056: Compatible mux reference controller query: erasureKL0 because Q/P is constant across controller subsets inside each exclusive data fiber; shared-only fibers Q=P. Projected reference outcome probabilit / ## Stage6: fixed original phase owners under private restrictions / For G=1+A_r(u-1), empty-calibrated Ru and a=2^-r, calibrating all shared-only rows leaves Q(U!=empty,T!=empty)=a^2 Ru(T), exact debt a(1-a)Du. Reference-only remaining-private owner fibers must use pa
- fleet/agents/A057: Stage4 durable fact: Current R=sum q_j log2(1/q_j)Var(u_j) is a supermartingale under arbitrary physical controller/data interleaving in exclusive independent-core models. Data drop=r(q_j)beta^2; cont / Stage5: Two-event shared-bit priority is paid on EVERY physical controller order with arbitrary disjoint-core data interruptions at8+2/ln2 after fine R release. Before X, same-orientation empty X ampl / Stage6 durable fact: For F=(1-Y)G+Y[A u+(1-A)H], H=exclusive disjoint-core mixture with residual probability e selecting SAME G, queried point probability q<=1/2, full B_A<=(12-4q)d<=12d. The key comp
- fleet/agents/A058: Stage 3 durable fact: hereditary l1<=1 shared conditional means are equivalent to every fully private-fixed Boolean shared slice being a signed character (Parseval + l1/l2 equality). Thus G=epsilon(X) / Stage4: slice-wise shared Fourier l1<=L is equivalent to hereditary conditional-private-mean l1<=L (restriction contraction + convexity). Coherent corrections obey |Dprivate|<=2L InfF, |Dshared|<=min( / Stage5: for independent point activations of two quadratic phases sharing S, common coefficients are delta+p(uhat-delta). At shared queries Cauchy-Schwarz on actual coherent rows prices D by (2+2sqrt2
- fleet/agents/A059: Interleaved stopping (A059 stage2): U=sum q[H(core)-eta(mean^2)] is a controller-query martingale. R=sum q log2(1/q)Var(core) has exact data loss q log2(1/q)beta^2 and controller release sum q Var D_2 / 2026-10-14T03:20:23.485714+00:00: Reused fallback F=A u+(1-A)G does not need independent children. Fine release is qVar(u)+[eta(1-q)-eta(1-2q)/2]Vbar. Exact B=qVar(u)+(q-2q^2)(Var(G)+(m-n)^2)+Var(G)Ph / 2026-10-14T06:23:55.166588+00:00: For independent earlier Boolean event blocks, failure guard E has normalized squared Fourier nonempty block probability p_i. If J is last nonempty block, t_J=product 
- fleet/agents/A060: - Shortest next mechanism: current biased packet debt and common reserve on two distinct activated cores sharing a control, retaining both terminal core entropies. A strict relative cap discount based / 2026-10-14 signed DATA sharpness: F=b_r+(y-1)1[z=0], paired quadratic bent even r>=4, q=2^-r. U_drop=0,R_drop=qr,Inf_y=q. Signed residual E obeys (19/6)q/ln2 <=3/ln2-E/q <=8q/((1-4q)ln2). Therefore A0 / 2026-10-14 03:37 UTC (20261014T033739Z-fleet05-A060-composition-sharpness): Point activation q=2^-r,m=Eu,a=1-m,z=qa,V=1-m² has exact D=2qV+2(q-2q²)a²+Ppair(z). Coarse releaseqV gives ratio2+(1/q-4)z
- fleet/agents/A061: Stage4: A005 signed-child eligibility is verified at new-implication scope. For arbitrary fixed violating seed, every fresh point-edit query has sigma=-(delta(seed)+delta(edited child))/2 -> -delta(se / Stage5 reviewed A064 repeated fallback: for F=A*u+(1-A)G with u independent of actual same G on both children, d=p(1-Eu*EG), and B-kappa=Bprofile+(c-k)W. Bound c<=2p, k>=0 and amplitude Phi(a²,b²)<=2| / Stage6: matched occupancy entropy H(M)=h2(z)+zlog(c)-sum dlog(theta)-sum(z-d)log(1-theta) avoids costly per-atom interval logs while preserving all atoms for reference reach. Coherent-kernel erasure/B
- fleet/agents/A062: Given prescribed nonnegative priced seed/profile reserves, R=t*r_seed+r_M transports them through finite adaptive interleavings at max prices, provided w waits until the seed tree reaches its zero-res / Shared-core data invalidate the independent-core proxy (1-Eu Ev)/2. For u negative{0},v negative{0,2} on3bits, querybit0 gives actualt1/8,childt1/4,0, but proxy5/16 and childmean1/4: false release1/16 / A030 independent-block mismatch transport independently HOLDS at its stated scope: actual mismatch=(1-mn)/2, untouched mean fixed, own-history controller reserve unchanged and harmonic under one-block
- fleet/agents/A063: 2026-10-14: For a fixed two-query canonical block, R_i_then_j=I(S_j;X_i|S_remaining). Deleted first spectral bit and later physical outcome contribute no extra information conditional on the correct h / Actual B05 family r=2k, d=2^-3k: both selector/one-control orders have strictly positive refund <16d^2 for all even k>=4. Every nonempty residual spectral packet contributes exactly zero; only [[1+C,C / Exact interval arithmetic lesson: bound denominator growth by outward endpoint rounding (here denominator2^384); leave kernel probabilities exact. A giant Fraction serialization failure is not a check
- fleet/agents/A064: For ordered disjoint point-priority controllers, Q=sum q*r+sum phi(q)Var transports C-priced own-history core reserves through arbitrary data interleaving: data priceC+11/2, control price11, root extr / On the actual essential-exposed priority fixture F=-1 on x=0,a=1, v on x=1,b=1, +1 otherwise, all256 three-bit v and all3 chosen next data queries certify W=[D_a]_++mean[D_b]_+<half the SAME mean actu / Exact support witness: core mask235,data bit0 has7/32 product-reference mass on source-zero erasure fibers in both actual a children; grandchild conditional KL>1.062 and>0.290, yet the complete signed
- fleet/agents/A065: Stage20261014T033844Z:225 exact reserve intervals on15 fixed families;54,431 main assertions including60 raw Boolean replay trees. B05k6 I=883/262144,H/I in[3.7381271477,3.7381271478]. At C=6.5218 gre / Greedy overlapping ratio intervals are ties only after exact prime-log-vector equality. Reuse the rigorous interval kernel; raw polynomial replay checks the compressed representation but shares the ke / Current frontier: actual non-point/overlapping controller reveal during partial core exposure, with both child continuation reserves and one unused physical influence account. A062 fixed-core preserva
- fleet/agents/A066: 2026-10-14T01:29:49Z stage: Actual bent single-child point edit F=g-(1-z)1_0 has query d=2^-2m, I=m+(2m+1)d and paid rate>2 for allm>=2 (>2.17 at m2), tending to2 above. Selected M_z^+/d is within8*2^ / 2026-10-14T04:20:48Z stage: In F=b+1_zero(q-1), arbitrary q, all nonempty residual control cells share uniform bent-core laws. Only empty-control cell loses KL, exactly delta*qhat(i)^2*D0. Jensen give / 2026-10-14 stage6: For any core b and F=b+1_zero(q-b(0)), complete control price M_i(F)<=delta M_i(q)+delta d beta_i^2+(2/(e ln2))Inf_i(F). Carry G=delta H_bits(q), R=delta d Var(q): control drops G>=
- fleet/agents/A067: Two fixed subcube controllers yield at most four compatible or five incompatible complete nonempty frequency cells. Every occupied row is flat within a cell; log2 cell size<=2 conditional mean degree, / ### 2026-10-14 stage5 04:48 UTC: final Boolean flag replaces edit ownership / For every Boolean F and block Z, alpha=P_spectral(S_Z nonempty)<=Var(F); h2(alpha)<=2I(F). Split Var at1/2, otherwise use minority bias p, Var=4p(1-p), monotone t log(e/t), and set isoperimetry I>=2p 
- fleet/agents/A068: 2026-10-13T23:48:53.298275+00:00 | For odd q>=5 cyclic quadratic-controlled majority, padded N>=2q and any point edit, R_delta=(1-2^-N)R0+2^-N U_N has Gamma<=Creg Ix(G)+2Iz(G)-(287/1920)Ix(Fq). Balanc / 2026-10-14T02:52:53.279655+00:00 | Unate two-face reserve: Inf_j(h)-2 sum_S_supset_ij hhat(S)^2 = E[d_jh(i+)d_jh(i-)]>=0. An invertible disjoint parity-star substitution y_j=x_j product_leaves x_i pre / 2026-10-14T06:05:32.764070+00:00 | Actual identification closures: a2=sigma*a1 makes each tag-merging packet carry the same phase; signed averaging conserves every control entropy/rank term. Node entr
- fleet/agents/A069: Control subsets form three visible singleton cells and two flat nonempty-Z cells with fixed u membership. Normalized weights1/4,1/4,1/16,7/20,7/80 absorb singleton costs and u-membership into2degree.  / Physical Y query carries R_Y by frequency marginalization to SAME Rprime for all cores/both children. Full reference decrement equals expected conditional core-reference cost plus binary JS of actual  / Maj3,y0,-y0,-Maj3 on one 3-bit tree with Kraft sum13/16 are genuinely nonfactorizing four branches paid by common K3; resulting family H<(28/5)I for all private widths. No universal source reference o
- fleet/agents/A070: - Fully exposed boundary t>=4: q1 flips c+,u+; q2 flips c+,V-all+ (|V|=t); h point mask on |Y|=t; g=q1*h and finalq2*h. Gamma(g)<=7I(g), Ig=1+2t2^-t, Iq=1+t2^-t, If=(3t+1)2^-t, R_I=2-2^-t. Ancestral[7 / - Norm-one real guard: g=sqrt(2)1{x+}, q single flip atx-,z1=z2+ gives gq=g, Ig=If=1/2,Iq=3/4,theta1/4. Boolean K=M=1 edge factor5/3 fails5/4>5/6. The discrete actual-pivot comparison is indispensable / - A088 stage4 independent acceptance of own prior signed-conversion audit consumed, no self-review. Historical cyclic-law certificates still unrecovered/unreplayed and excluded from dependencies.
- fleet/agents/A071: 2026-10-14T01:50:32.003212+00:00 | Mixed signs matter: on actualg3=h(h((-h(h^6))^6)^6) as defined explicitly in stage4 PROOF, all64 independent signs are exactly10 orbits under48 matched-pair automorp / 2026-10-14T04:33:11.804565+00:00 | A075 all-word output-entropy payment independently reconstructed: D=Qh2(p)-h2(pout)>=0, DeltaPsi=D/(QI), Delta(H/I)=C/(QI), C=H_p(gate)-Qh2(4p(1-p)); retained core H / 2026-10-14T09:16:06.929562+00:00 | Full-terminal affordability and unused-owner availability differ even in J(g6^6): every selected-block restrictionH/I<4.2, while selected-only mean fullreveal rate c
- fleet/agents/A072: 2026-10-14 stage5: A080-REPEATED-ESCAPE-RETURN-NOGROWTH@1 independently HOLDS: mu=Var/I contracts<=2/3 at common h, never increases at J;8mu per common step and225/44 mu per full escape sum to1731/44  / 2026-10-14 stage5 boundary sign audit: All8 frozen physical queries have Delta H(F)>4 Inf(F), even the6 with negative Delta C. Positive Delta C occurs only in J block0 (i=0 and2). These are true-decre / 2026-10-14 stage6: For checked full slacks S_parent,S0,S1 and signed query excess e, B=(S0+S1)/2=S_parent+e. Transport each incoming label a as a*S_child/B and new label e likewise; old conditional ex
- fleet/agents/A073: A073 stage20261013: exact E(f5) in (2.695887520153100810486497662748,2.695887520153100810486497662749), min coordinates0,1,3; E(f6) in (2.944495303871858585073528591901,2.94449530387185858507352859190 / Stage20261014: A096 single-spectator ownership@1 independently HOLDS: parity duplication embeds p, adds sum_J e, removes sum_J M; dropping partner loses original M_i, retaining partner preserves KL ex / Stage20261014T053433: A085 quadratic remainder@1 independently HOLDS, including platform/formula-specific first falsezero104 and squared-atom underflow538. For p_sigma=(1+sigma*t)/2, x_sigma=(delta-si
- fleet/agents/A074: 2026-10-14T06:22:24.416232+00:00 stage5: J=-h(x xor1) has negative-weight counts[0,4,10,18,15,6,1],sigma=4p-10p^2+18p^3-19p^4+10p^5-2p^6 and3p<sigma<4p on0<p<=1/16. All arbitrary cores escape finitely / Exact bitset characters versus binary-polynomial occupied blocks are independent of FWHT. Symbolic Phi(x,0)=0 and power-of-two logs prevent exact dummy identities from becoming nonzero-width interval  / Actual J on six copies of6-bit core negative on(0, 1, 2),physical block0 queriesi0/i2 both haveDeltaC>0 andDeltaH>4Inf; i2 child biases3/32 and0 with exact constantH=I=0. Full signed physical identity
- fleet/agents/A075: 2026-10-14 stage3 20261014T005346Z durable: For every actual Boolean g and delta,eta>0, finite oriented disjoint f6 composition produces p_min<=delta,I<=eta,E>=E(g)-kappa, kappa<0.914. Moderate contin / 2026-10-14 stage4 20261014T034311Z durable: Ordinary OUTPUT entropy potential Psi=h2(p_min)/I differs from squared-spectrum H/I. Indicator-plus-complement entropy tensorization gives h2(output)<=Qh2(i / 2026-10-14T08:07:15.271814+00:00 For g_n negative on{0,1,2}, p=3/2^n, S4(g_n)/p->s=6log3-8/3-4loge>0. J=-h flip0 selected q0=4p-14p2+18p3-10p4+2p5. Complete selected-block full curvature D/p2->32+16lo
- fleet/agents/A076: Stage4 durable fact: for arbitrary shared-data mux F=(G+H)/2+z(G-H)/2, D_i=B_i(F)-[B_i(G)+B_i(H)]/2 has |D_i|<=1. A hereditary H relevant-influence gap eta permits H-relevant-first adaptive queries wi / Stage5 durable facts (bits): private query i absent from branch H in F=mux_z(G,H) has A_i=B_i(F)-B_i(G)/4>=0 and A_i<=d+Phi(4delta-d,d)/2<=4delta, d=Inf_i(G),delta=Pr(G!=H)=Inf_z(F), d<=2delta. Scalar / Stage6 durable facts: phase-point F=H(s)[1+point(s)(V-1)] with k-bit quadratic bent H, epsilon2^-k, has exact H(F)=epsilon H(V)+k+k epsilon(1-mu^2)+J(mu), |J prime|<=40epsilon; I(F)=k/2+k epsilon(1-mu
- fleet/agents/A077: A076 stage5 private query admission retains a quarter: 0<=B_i(mux)-B_i(private core)/4<=4delta; scoped local/antichain theorem independently HOLDS. Its four-delta allowance cannot be reset at each lay / If eligibility is absorbing and a marked private query releases at least gamma of eligible mismatch mass, M=(4/gamma)delta*1_eligible pays all repeated remainders by its stopped telescope. In the actu / Every adaptive fresh-coordinate stopped tree on that family, with arbitrary selector timing, satisfies B_T+E K_leaf<=10P_data+22Inf_z(root). Terminal H is the exact actual core law, not K_leaf; both i
- fleet/agents/A078: Stage3 durable obstruction: G=1-2 indicator{s=0,x=0}, H=quadratic bent on even k shared bits, F=mux_z(G,H). Actual Inf_x=2^(-k-1); exact D=(2^k-1)S(-a,a;b)+S(1-a,a;b), a=2^-k,b=2^(-k/2). D/Inf>=k-4, Q / Stage4: For any fresh point activation and any actual finite interleaved tree, active weight w*p_remaining=p0*pi projects to one core tree. Its paired-quarter bill is bounded below by p0L_shadow-6P_da / Stage5: Nonnegative-mean core g, point activation V with p=2^-r,c=1-Eg: all core directions costp q_g(v), any nonzero control displacement costpc, no folding improvement. Exact minimum M(V)=p[T_c(g)+r
- fleet/agents/A079: - For ACTUAL Boolean g(z,y), fair-product positive frequency branches yield0,+/-1 partial rows, raw magnitudes powers2 and dyadic branch norms. Both positive norms must be1/2. H=1+(m0+m1)/2<=2I, arbit / - Exact four-bit nonflat nonproduct witness raw Walsh[-8,0,0,0,4,4,-4,4,8,0,0,0,4,4,-4,4], frequency bit2 branches fair counts1 and3, masses1/2, H3,I3/2. Two-unused-address embedding has conditional e / - First unpaid step: a nonfair branch has an odd norm factor, so probability need not be1/2; preserve h2(q), both whole conditional spectra, actual partial-row heights, signed address gap and one unus
- fleet/agents/A080: A074 independently accepted A080 g3 rare-core obstruction@1 unchanged (503 exact checks; source run20261014T030615Z). New potential mu=Var/I never increases under identical disjoint substitution of an / Named common policy costs<=8mu per step; each full J=-h(x xor1) escape from p<=1/16 costs<=225mu_start/44 in H/I. At most one episode per preceding common count, so every strategy with any number of e / 2026-10-14 stage5: For every fixed delta,eta>0, sup H/I on actual p_min<=delta,I<=eta equals unrestricted sup exactly. Tensor t=ceil(k^2/I(g)) then private point activation2^-k retains H/I >=R(g)/(1+2
- fleet/agents/A081: Stage 4 refund-contract facts: full row KL equals coarse KL plus nonnegative conditional W; coarse retained price equals full retained price plus influence-weighted W. Complete reference-only cells ca / Stage 5 reserve-availability facts: A090 arbitrary-gate signed refund partition v1 independently accepted at entire original scope. Keeping gate residual mask plus bent Fourier sign preserves full KL; / Stage 6 phase/history facts: physical child amplitudes are a_T+epsilon*a_(T+j), so complete parent squared law alone cannot transport an actual labeled child; neutral nine-bit F and translate y0 share
- fleet/agents/A082: Exact E*(5)=K5=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89), with 640 three-vertex path extremizers. Independently reproduced the full covering scan without FWHT. Covering influence-order and an / The physical affine-support projection bridge is parameterized: a certified r-junta constant extends to affine Fourier dimension<=r and disjoint products at every restriction. For r=5 it gives H<=(K5+ / Stage 20261014T045125Z: The exact loss-only bank threshold five is a policy obstruction, not an FEI lower bound: point-sign roots already obey H<=4I. Arbitrary signed-core amplitudes plus gate mask fo
- fleet/agents/A083: C024 conditioning identity matters: actual AND2 sign [1,1,1,-1] has coherent H(Pi|root Fourier label)=1/2, but terminal residual spectrum is empty and H(Pi|it)=3/2. Its r-fold product has reset gap r  / 2026-10-14 durable fact: On F_m shared AND priority gate after querying u, the essential u=0 and u=1 leaves number m+2 and m+3. Physical surviving-v probabilities are t/2 and 3t/4; equal-leaf referenc / 2026-10-14 durable stage5: Under domination rather than equal erased support, inherited conditional matching iff p_e/q_e (including0) is constant on branch-support graph components formed on FULL q_e 
- fleet/agents/A084: Stage3: For positive signed packets, c=m^2, u=U/D and lambda=D/q, the boundary slope A=sum D log2(u/c) controls ALL t>=0: G(t)=product(t+u)^lambda has G'(t)>=1, hence A>=0 implies R(t)>=0. Negative A  / Stage4 durable: Finite arbitrarily long common-sign matching-gate trajectories have a uniformly bounded FULL normalized entropy correction, not just rare tail: [-2074/105,248/3]. Scalar L(v)=q h2(v)+v / Stage5 durable: Holding other output laws fixed, C_j(x)=sum ell((a+xd)^2)+(1-x^2)sum ell(d^2)+q x^2log2(x^2), up to affine terms. Thus C_j second derivative=-2L_j(x), L=sum d^2log2((a+xd)^2/(x^2d^2)).
- fleet/agents/A085: A073 F_d, even d>=2: delta=2^-d, sign weights(1+-sqrt(delta))/2. Complete binary quotient retains mu=(1/2,1/2),r=(1-delta/2,delta/2). Conditional gap D0 satisfies (24/169)delta<D0<(15/16)delta by stro / ## 2026-10-14T07:59:20.483764+00:00 — Canonical inherited-quotient owner / On four-bit priority gate, b then y only at b=1, old actual mean-child S4=3 partitions into consumed-influence1 and finalS4=2. Canonical c root ~0.793; C=-log2(1-4c/15)/2. Complete mean inherited b-ch
- fleet/agents/A086: 2026-10-14T01:52:17.205110+00:00 20261014T013711Z-fleet05-A086-joint-code-referee: Every shared-only atom must be calibrated individually to remove posterior mismatch; off-target reference fibers ne / 2026-10-14T04:32:58.365181+00:00 20261014T042208Z-fleet05-A086-joint-code-referee: For any point edit, data marginal is P_g-rho*g(ystar)*ghat(T)*chi_T(ystar)+rho*2^-m; unsigned mixture admission mus / Stage6 durable facts: arbitrary-core point edit admits prescribed Rdag=(R+6pt U)/(1+6pt), CE<=2c+15(C+E+J), conditional rate4C0+15, not same-rate recursion. Incoming mass M survives R_b=M(2r*pi_b)/Z_b
- fleet/agents/A087: - A030 conditional non-point binary transfer v1 HOLDS: H(F)=delta H(h)+qH(u)+pH(v)+B(b;m,n), delta=(1-mn)/2. Exact mean correction B has Lipschitz bound22delta; controller physical influence=delta I_i / - A064 independently accepted our stage4 owned-controller geometry. Byte-identical exact_statement receipt keeps our correct original raw hash even though reviewer-copy recorded hash differs. This is  / - A038/A039 exposed opposite-priority fixture has kappa0 but positive product-reference reset. One small-fixture occupancy release funds either that debit or occupancy-to-product conversion, not both.
- fleet/agents/A088: Stage3 durable facts: Sparse fibers a_x<=1/4 imply per-core-edge mask mismatch p<=1/2, so Boolean final pivot probability p or 1-p dominates p. This pays one combined-mask core reserve; separate-event / Stage4: Two globally fixed subcube controllers admit a common complete four-cell compatible/five-cell incompatible Fourier reference; log-cardinality<=2conditional mean degree, so accessK<19/2 (<9 com / Stage5: Universal Boolean spectral flag h2(alpha)<=2I is sharp at full-block point signs and uses minority-set bias/boundary, not mere normalized Fourier mass. A067 no-cap four-branch final-reference 
- fleet/agents/A089: 2026-10-14T00:24:49.297122+00:00 Signed composition reserve R(t)=sum Phi(U,tD)-qPhi(m^2,t) has sharp bias-only positivity criterion L=sum Dlog2(U/D)-qlog2(m^2)>=0; active zero U gives L=-infinity; m=0 / 2026-10-14T03:23:00.811619+00:00 Finite moderate duration does not pay a uniform entropy bill; Q>=19/16 permits the one-use potential Delta=1/I-1/I_next. Ordinary matching steps have -1<=C/Q<=2, hence / 2026-10-14T06:38:57.769571+00:00 A075 independently accepted A089 stage4 full fixed-policy bill at unchanged scope. Physical DeltaH(F)=q_j DeltaH(core)+DeltaC; rate excess includes both terms. Unused 
- fleet/agents/A090: Stage 3: For normalized derivative/reference rows, degree coarsening loses exactly sum_i eps_i sum_t mu_bar_i(t) KL(mu_i(.|t)||r_i(.|t)); M_degree-M equals this nonnegative loss. For actual OR of m=2^ / Stage 4 durable fact: for F=b_d+1[y=0](g-1), even d>=4, any Boolean gate g, complete gate-query likelihood depends only on residual gate mask V and bent Fourier sign sigma_R. Forgetting sigma loses on / Stage 5 durable fact: A001 four-cell quotient for a bent core point-attached to r two-bit gate products jointly pays selector M_C+L_C beyond J with extra E<rw delta(d+2r+1)/2<=5/8<3a/2, one named owne
- fleet/agents/A091: Stage20261014T042228Z proof checkpoint: actual later-test B query before a point A is settled has original fine kappa=(1-a)q Var(v); repeated u has no query erasure. Residual is three nonnegative mean / Stage20261014T042228Z: A087 owned controller reveal v1 and A059 interrupted priority payment v1 independently accepted at full source scope. The source repeated-fallback erasure formula is exact with  / Stage6: A059 priority v2 independently accepted at original raw hash c7b765fc00fead608b436d82fdc93d9913fd59f353572d346be700fffb8fb0c3. Product failure spectrum has last-nonempty-block logarithmic mome
- fleet/agents/A092: A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 independently accepted: half-output-conditional bank pays positive scalar tax by I(Pi;Y)/2<=I_phys/2; lambda<1/2 fails on essential biased point-defect computing t / Stage4: A083@1 accepted: retained root-to-terminal bank loses r bits on disjoint AND signs, H=2r,I=r; local Lean scope is rational row transport only. A050@1 accepted: e=H(S intersect Q|S)<=I_A h2(R/I / Stage5: A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1 accepted unchanged: hereditary shared conditional spectral kernel with matched references transports quotient prices exactly and retains spectator entro
- fleet/agents/A093: 2026-10-13T23:57:21.757439+00:00 | GMP26 v1/v2: true decrement = E_i+R_i, R_i>=0 and <=4I_i by the binary-entropy series. Two-bit AND has Delta=2, E=1, R=1, I_i=1/2, refuting same-K replacement at K=2 / 2026-10-14T02:52:37.482116+00:00 | Source repair: V=sum|a²-b²|, D=sum(a-b)²=4Iquery. Correct h<=2sqrt gives E<=V/2; refund R<=D implies Delta<=V/2+4I. GMP semi-separated ternary Prop6.1 V<=4D survives / 2026-10-14T05:50:45.020838+00:00 | GMP wrong-variable scope: OR of k AND3 blocks, boundary deletion minus child, epsilon8^-k. I_z=epsilon; nonempty coefficient abs=2epsilon7^j with j missed blocks. Tr
- fleet/agents/A094: - Physical restriction with same incoming Q requires normalized inherited children R_b=2r*pi_b/Z_b. Complete debt satisfies Dparent-avgDchild=L_j-avglog2Z_b>=0; complete CE additionally retains the ac / - A paid root does not imply influence-priced inherited child references: exact source-cost1 character plus dummy/point-control family has root price12, but inherited negative reference vacuum<1/3 for / - This fixture is repaired by charging its whole retained-core ledger ONCE: CEroot<=1+10(n+1)2^-n<=(34/3)Inf_active. Whole independent terminal CE stays outside the account. No new descendant bank is 
- fleet/agents/A095: 2026-10-14: For Boolean G(s,X),H(s,Y), t>=2 shared bits and disjoint private cubes, sign folding gives d*=min(d,1-d) without changing spectra or entropy increment. Shared conditional means imply each  / 2026-10-14 stage4: A094 sharp all-location padded quadratic point-selector price C_pt=(16/29)[8-(180log2(3)+300log2(5))/256] independently HOLDS, including destroyed-edge debit, all-dimensional tail a / 2026-10-14 stage5: Through any finite adaptive core-only tree on a point-selector, Pi_M=Pi_g+delta(t_a-2j_a) and mean remaining I=Ig-Pi_g+delta[n+1-t_a-2(j-j_a)]. A094 posterior transport retains actu
- fleet/agents/A096: ## Stage5 non-flat loss and real child surplus / For F=b+1_0(g-1), arbitrary actual b(0)=1, delta=2^-d, retaining (residual gate mask V,bhat(T)) preserves full gate-row KL. Mask-only loss L_i=delta*a_i^2*D(U||q_i), q_i=((bhat(T)+delta(a0-1))^2+delta / Stage6 durable facts: For every Boolean P and normalized finite-cost Q, BOTH physical children can use marginal Q_-j. Exactly CE(P,Q)=B_j+meanCE_child+[D(P||Q)-D(P_-j||Q_-j)], last term nonnegative co
- fleet/agents/A097: Stage5: A09420261014T031253Z independently accepts A097 padded-bank/full terminal-activation chain. Its all-vertex bent proof means do not repeat moved-point bent work. New negative-cell floor for g=1 / Calibrated common-vacuum collapse pays full CE<=c+10(C+E+J), C2ptb,E2pta,J2rpt. Owned certificate S_K+(K-10)C-(K+10)E+(K-10)J retains erased edges. Since E<=I_g/2, c<=C0I_g yields paid rate2C0+10. Sou / Boolean active restrictions keep the negative-cell family but do NOT automatically transport an arbitrary incoming reference or remaining bank. Next must construct actual descendant Q/normalizers and 
- fleet/agents/A098: Stage3: For the permutation orbit of any fixed squared Boolean spectrum, inf_Q(subprobability) max_pi CE(P_pi,Q)=H(barP)=H(degree)+E log2 binom(n,degree). Q may be label-dependent; the average law is  / Stage4: A073-NONZERO-ERASURE-BINARY-REMAINDER@1 independently holds for all even d>=2. On bent core with one vertex replaced by a two-bit AND-sign gate, complete pair rows have e=delta/2 and binary la / Stage5: A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1 independently holds at full scope. Negative-cell point edits admit actual nonnegative three-component marginal; empty-calibrated floor retains same-refer
- fleet/agents/A099: Negative-cell supplied-reference floor: for g=1-2 A_a with b dummies edited at a negative full data point under r fresh point controls, CE_F<=c+10(C+E+J), I_F=I_g+C-E+J, E/I_g<=1/2. A source certifica / For arbitrary core point attachment, the sufficient statistic (gate mask, actual signed core amplitude) preserves full derivative-row KL; mask-only quotient losses fit 2 I_Y+2/(e ln2) I_X, or I_Y/2 wh / For the A073 positive-erasure bent-core/two-bit gate family, weighted Jensen gives R(delta)=(1+delta-3delta^2/4)/(1+delta^2/4), each loss/e<1/8 and summed loss<delta^2/(2 ln2), also a dedicated twenti
- fleet/agents/A100: New A100 Jensen refinement, pending external review: sign weights (1+sigma sqrt(delta))/2 give D0<=log2[(1+delta-3delta^2/4)/(1+delta^2/4)]. R increases to77/65, and77^4<2*65^4 gives L/e<1/8. R<1+delt / A008 auxiliary t=1/2 singleton substitution is false; both endpoint orders give t=1/4. Formal determinant/queue operator retains t and is unchanged. In an e+1-singleton forced assignment, the old subs / A097 padded zero-point17/8 bank and A086 unpadded price-two bank have A094 full original-scope reviews. Arbitrary-location/destroyed-edge sharp price is a distinct pending A094 theorem. A095 v3 new ap
- fleet/claude/B02: - Tribes closed forms worth reusing: P(A) = 4 q^{2(m-k)} 4^{-wk}, I = 2mw q^{m-1} 2^{-w}, E k = 4m q^m 2^{-w}, / H = -P0 log P0 - 2v(1 + m log q) + 2 E k (w + log q). H/I -> 4 at m = 2^w. / - Tool note: long shell heredocs failed to parse; writing files in chunks under 4 KB worked.
- fleet/claude/B03: read-once AND/OR constant must respect. / - The harness refuses REPORT.md from a subagent; return the report text in the structured output and let the / coordinator save it.
- fleet/claude/B04: - Charging the boundary at every node of a fixed order costs the second moment sum C(|S|,2)fhat^2. Adaptivity or the exact B_W (parity / KL credit) is the only way forward on this route. / - Process: the harness refused REPORT.md from this Claude subagent ("subagents should return findings as text"); the report text went into the structured output for the coordinator to persist. Plan fo / - Codex checks this stage: A016, A017, A018, A019 all hold at their stated scope; A017 and A018 are baseline reconstructions, A019 is a narrow genuine extension.
- fleet/claude/B05: - Tooling: this Bash wrapper fails on heredocs that contain apostrophes (unexpected EOF); use the Write tool for files. / Directory listings of the big campaign folders can exceed 60 s; read targeted paths. memok.py gates heavy jobs on / commit free memory as well as physical; a lean array layout kept the n = 19 run far under the 300 MB line.
- fleet/claude/B06: - In this harness a subagent cannot write REPORT.md (the Write tool refuses report files). Return the report text in the structured / output, save the JSON records, and name the blocker in PROGRESS.json. / - Long bash heredocs with nested quotes failed to parse; write code files with the Write tool and keep shell commands short.
- fleet/claude/B07: - Entropy inequalities H <= c I with c = a + b log2 3 can be decided exactly by integer powers; floats only rank. / - Process: a float illustration built a 16384 x 16384 dense matrix (several GB). Use FWHT; size memory before running. / - The subagent harness refused REPORT.md (Write tool). Put report content in the StructuredOutput and JSON records.
- fleet/claude/B08: - Process: one diagnostic compared 64*B with an unscaled I*log2(e) and reported 64,832 false violations; keep one / scale per comparison and re-derive any surprising violation before reporting it. / - The Write tool refuses a file named REPORT.md from a subagent; the protocol file was staged in scratch and copied.
- fleet/claude/B09: - The tax is per revealed bit and independent of I. It can never pay a deficit; it has to BE paid by delta. Do not present it as progress on charging M. / - Process scars: (1) a coarse-grid scalar minimiser missed a minimiser narrower than the grid step (p = 2^-30); merge a fine local grid around the expected minimiser. (2) I multiplied the case count i / - The A043 composition identity holds with unequal child biases: the composed spectral law factorises as S ~ g^2, then T_i ~ f_i^2/v_i on nonempty sets.
- fleet/claude/B10: - My first PASS covered beta from 0.2897, which is p = 0.0816, not 0.08: a coverage gap that a green PASS hid. / Recompute the coordinate change at the seam before trusting a cover. / - mpmath iv has no asin; parametrize boxes by the angle instead of by p.
- fleet/claude/B11: - For n<=6 the point defect maximizes both H/I and the block-descent constant phi; do not search small n for descent obstructions. / - The fibrewise log-Sobolev bound allows any recentring per fibre; the conditional majority is optimal and gives the Bayes error beta_A. / - The descent constant obeys M_n <= max_m K_desc(m), so it must eventually exceed C_*; the interesting question is boundedness.
- fleet/claude/B12: - A058's private anchors make every outer label visible in the physical support, so overlapping shared gates cost nothing extra; the collision problem starts only when an anchor is shared. / - Exact checks of entropy identities: Walsh coefficients are integers over 2^n, so every entropy is a rational combination of logs of primes; compare the vectors. 6,468 identities ran in seconds. / - Practicalities: heredoc scripts with many quotes broke the Bash tool's parser here; write scripts with the Write tool. Python launched from Git Bash gets /c/ paths converted only when they are argum
- fleet/claude/B14: .md files from a subagent. Write a scratchpad .txt with Write, then cp. / - Timing: the first stream notes landed three minutes late because the derivation came first. Write the skeleton in the / first ten minutes next time.
- fleet/claude/B15: - Symmetric functions never beat K* (n<=14): symmetry is the wrong search family for this lemma. / - Tooling: truth tables for n>=6 exceed int64; build the +-1 vector from Python ints. Dump search JSON before certification so a certifier crash does not lose the run. / - The subagent harness refuses report .md files; persist JSON (CLAIMS, PROGRESS, PACKET_DELTA) and return the report in the StructuredOutput.
- fleet/claude/B16: - Negative controls matter: wrong constants (B - Q <= 0.5M/ln2, JS <= M/ln2, Delta - Q <= 2M/ln2) trip at n = 3, 4; one control I labelled false (B >= Q + 0.01M) was in fact true, which is how the sha / - The subagent harness refuses a Write of a file named REPORT.md; record the protocol report in CLAIMS.json proof_source and in the StructuredOutput, and name the blocker in PROGRESS.json. / - A Bash heredoc that contains an apostrophe inside double-quoted Python strings failed to parse in this shell wrapper; write scripts with the Write tool.
- fleet/claude/B17: almost flat (2.697 at n=15). A high H/I is not evidence of a high selection constant. / - The harness refuses REPORT.md from a subagent. The report text has to travel in the final / structured answer.
- fleet/claude/B18: - A C005 induction with a good-coordinate constant K proves FEI with K+2/ln2, so any known lower bound on the FEI constant is also a lower bound (minus 2/ln2) on every universal good-coordinate consta / - Exact zero deviations in float checks on small Boolean functions are expected (dyadic Walsh coefficients give identical floating terms); confirm nontriviality and use rational-log rechecks for anyth / - The harness refuses REPORT.md writes from a subagent; put the report text in the structured return and record the blocker in PROGRESS.json.
- fleet/claude/B19: 2026-10-11: Section 8's shared-data proposition places no hypothesis on F (any coordinate split is a selector block), so it is the block-restriction identity; the content is in the orthogonality corol / 2026-10-11: Theorem A's single-order rank code fails on XOR of disjoint AND_L blocks: any order pays about (L-1) ln 2 nats per Fourier element against true entropy under 4 bits per unit influence. A p / 2026-10-11: A heredoc of Python source with many quotes failed inside bash -c ("unexpected EOF"); write scripts with the Write tool. The harness refuses REPORT.md from a subagent; put the report in th
- fleet/claude/B20: - A minimum over coordinates of B_i/Inf_i is bounded by H/I (mediant, then B <= H by the chain rule). On a family with known H/I it is never an independent falsifier. / - Two streams' constants that look inconsistent can be one extremizer under two definitions: B13's 4.8677 and A082's 2.6725 differ by 4 J_i = 8 - (5/2) log2 5 at the 3-bit point function. / - Tooling: write long .md files with a PowerShell single-quoted here-string and WriteAllText; Bash heredocs containing apostrophes fail, and the Write tool refuses report files here.

## Not in git (binary, over 2 MB or flagged by the secret scan)

Binary and flagged files of the fleet and the Opus routes, and the computed arrays of TRIO_1011, are also assets of this repo's release fei-campaign-binaries-2026-10 (manifest in its notes), marked [release] below. TRIO_1011's downloaded papers and raw API responses stay on the laptop only. Text over 2 MB in finished fleet runs is on math-open-problems through the fleet sync.

- ~/brain_workers/FEI100_20261011/agents/A026/runs/20261011T214052Z-fleet05-A026-good-coordinate-erasure/out/gray_selections.bin (32906 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A029/runs/20261014T055200Z-fleet05-A029-child-deficit-transport/REVIEW_A028.md (2927 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A053/runs/20261014T052310Z-fleet05-A053-near-tensor-perturbations/REVIEW_A052.md (2976 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A071/runs/20261014T042108Z-fleet05-A071-search-space-design/out/FROZEN_SPEC.json (2314 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates/out/source_snapshots/MU1988_page1.png (360175 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates/out/source_snapshots/MU1988_page2.png (566369 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A081/runs/20261011T234021Z-fleet05-A081-dependency-certificates/out/source_snapshots/MU1988_pdf.pdf (554646 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A082/runs/20261011T221008Z-fleet05-A082-finite-inequalities/out/selection_n1.bin (2 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A082/runs/20261011T221008Z-fleet05-A082-finite-inequalities/out/selection_n2.bin (8 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A082/runs/20261011T221008Z-fleet05-A082-finite-inequalities/out/selection_n3.bin (128 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A082/runs/20261011T221008Z-fleet05-A082-finite-inequalities/out/selection_n4.bin (32768 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A084/runs/20261012T044029Z-fleet05-A084-continuum-parameters/out/SIGN_MAP.png (80565 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A084/runs/20261012T044029Z-fleet05-A084-continuum-parameters/out/SIGN_MAP.svg (67674 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A091/runs/20261011T234101Z-fleet05-A091-composition-referee/out/MU-page1.png (277491 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A091/runs/20261011T234101Z-fleet05-A091-composition-referee/out/MU-page2.png (433947 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A091/runs/20261011T234101Z-fleet05-A091-composition-referee/out/maassen_uffink_1988.pdf (554646 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/out/ckls_rev1.pdf (683360 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/out/ckls_rev2.pdf (844697 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/out/gps_v4.pdf (1103984 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/out/maassen_uffink_1988.pdf (554646 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/out/mu_page1.png (360175 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/out/mu_page2.png (566369 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/out/odonnell_tan.pdf (373967 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/chang25.pdf (383981 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/ckkls18.pdf (227003 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/ckls_corrected.pdf (844697 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/fangwang26.pdf (2055963 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/gmp26.pdf (554711 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/gmp26_v1.pdf (538520 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/gmp_page16.png (81619 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/han25.pdf (369433 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/kms12.pdf (177512 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/owz11.pdf (406363 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A093/runs/20261013T234909Z-fleet05-A093-literature-and-priority/out/potapov26.pdf (319037 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261011T225112Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.pdf (290128 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261012T044129Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.pdf (332387 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.pdf (54721 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.pdf (400836 bytes) [release]
- ~/brain_workers/FEI100_20261011/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich/out/n4_minD.npy (524416 bytes) [release]
- ~/brain_workers/FEI100_20261011/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich/out/n4_minL.npy (524416 bytes) [release]
- ~/brain_workers/FEI100_20261011/claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich/out/n4_ratio.npy (524416 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-1_n1024.npz (1828 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-1_n16384.npz (24601 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-1_n262144.npz (417396 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-1_n4096.npz (5832 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-1_n65536.npz (100813 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-2_n1024.npz (3165 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-2_n16384.npz (58921 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-2_n4096.npz (13585 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H-2_n65536.npz (242611 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H0_n1024.npz (1460 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H0_n16384.npz (16943 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H0_n262144.npz (293093 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H0_n4096.npz (4052 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H0_n65536.npz (70465 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H1_n1024.npz (1296 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H1_n16384.npz (12707 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H1_n4096.npz (3215 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H1_n65536.npz (54164 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H2_n1024.npz (1272 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H2_n16384.npz (10887 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H2_n4096.npz (2770 bytes) [release]
- ~/brain_workers/TRIO_1011/op/F0131/experiments/H2_n65536.npz (45141 bytes) [release]
- ~/fei_opus_2026_10_11/A2-two-addresses/data/prod3_wide.pkl (291137 bytes) [release]
- ~/brain_workers/FEI100_20261011/agents/A009/runs/20261014T054349Z-fleet05-A009-fractional-incidence-optimization/out/CHECK.json (2659058 bytes)
- ~/brain_workers/FEI100_20261011/agents/A014/runs/20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read/code/.keep (1 bytes)
- ~/brain_workers/FEI100_20261011/agents/A014/runs/20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read/out/.keep (1 bytes)
- ~/brain_workers/FEI100_20261011/agents/A022/runs/20261011T234607Z-fleet05-A022-one-point-surgery/out/full_r0_patterns.jsonl (3115340 bytes)
- ~/brain_workers/FEI100_20261011/agents/A022/runs/20261011T234607Z-fleet05-A022-one-point-surgery/out/full_r2_patterns.jsonl (3229122 bytes)
- ~/brain_workers/FEI100_20261011/agents/A022/runs/20261011T234607Z-fleet05-A022-one-point-surgery/out/full_r4_patterns.jsonl (3288315 bytes)
- ~/brain_workers/FEI100_20261011/agents/A022/runs/20261013T220954Z-fleet05-A022-one-point-surgery/out/full_CASES.jsonl (3012244 bytes)
- ~/brain_workers/FEI100_20261011/agents/A022/runs/20261014T014918Z-fleet05-A022-one-point-surgery/out/full_CASES.jsonl (3611812 bytes)
- ~/brain_workers/FEI100_20261011/agents/A023/runs/20261014T051414Z-fleet05-A023-amortized-rarity-budget/out/results.json (6579625 bytes)
- ~/brain_workers/FEI100_20261011/agents/A023/runs/20261014T051414Z-fleet05-A023-amortized-rarity-budget/out/rows.jsonl (4296876 bytes)
- ~/brain_workers/FEI100_20261011/agents/A032/runs/20261011T234647Z-fleet05-A032-boolean-phase-realizability/out/mixed_slices_m4.json (8195116 bytes)
- ~/brain_workers/FEI100_20261011/agents/A039/runs/20261014T055326Z-fleet05-A039-projection-under-restrictions/out/MIXED_CHECK.json (2423422 bytes)
- ~/brain_workers/FEI100_20261011/agents/A061/runs/20261014T085352Z-fleet05-A061-entropy-process/out/EXHAUSTIVE_CHECK.json (9842811 bytes)
- ~/brain_workers/FEI100_20261011/agents/A065/runs/20261014T033844Z-fleet05-A065-stopping-rule-falsifier/out/VALIDATION.json (2562347 bytes)
- ~/brain_workers/FEI100_20261011/agents/A071/runs/20261014T013355Z-fleet05-A071-search-space-design/out/big/cases_partial.json (32890647 bytes)
- ~/brain_workers/FEI100_20261011/agents/A071/runs/20261014T013355Z-fleet05-A071-search-space-design/out/big/results.json (32949050 bytes)
- ~/brain_workers/FEI100_20261011/agents/A076/runs/20261014T013416Z-fleet05-A076-threshold-and-tribes-controls/out/FULL_LEDGERS.json (6785281 bytes)
- ~/brain_workers/FEI100_20261011/agents/A076/runs/20261014T042128Z-fleet05-A076-threshold-and-tribes-controls/out/FULL_LEDGERS.json (3443331 bytes)
- ~/brain_workers/FEI100_20261011/agents/A081/runs/20261013T220111Z-fleet05-A081-dependency-certificates/out/source_snapshots/A064_stage2_marker (27 bytes)
- ~/brain_workers/FEI100_20261011/agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger/out/REPORT_SOURCE_BUNDLE.txt (2883280 bytes)
- ~/brain_workers/FEI100_20261011/agents/A096/runs/20261014T013836Z-fleet05-A096-live-gap-ledger/out/REPORT_SOURCE_BUNDLE.txt (3944457 bytes)
- ~/brain_workers/FEI100_20261011/agents/A096/runs/20261014T013836Z-fleet05-A096-live-gap-ledger/out/SOURCE_LEDGER.json (2779947 bytes)
- ~/brain_workers/FEI100_20261011/agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger/out/REPORT_SOURCE_BUNDLE.txt (4904444 bytes)
- ~/brain_workers/FEI100_20261011/agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger/out/SOURCE_LEDGER.json (3882594 bytes)
- ~/brain_workers/FEI100_20261011/agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger/out/REPORT_SOURCE_BUNDLE.txt (5932824 bytes)
- ~/brain_workers/FEI100_20261011/agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger/out/SOURCE_LEDGER.json (5255615 bytes)
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261011T225112Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.aux (2924 bytes)
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261012T044129Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.aux (4243 bytes)
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.aux (4096 bytes)
- ~/brain_workers/FEI100_20261011/agents/A099/runs/20261014T031358Z-fleet05-A099-candidate-assembly/out/CANDIDATE_MANUSCRIPT.aux (7189 bytes)
- ~/brain_workers/FEI100_20261011/agents/A100/runs/20261014T034838Z-fleet05-A100-release-and-continuation-ledger/out/CLAIM_CENSUS.json (2510964 bytes)
- ~/brain_workers/FEI100_20261011/claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B07/runs/20261011T230024Z-claude-B07-two-address-census/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B08/runs/20261011T225000Z-claude-B08-tc-restriction-ledger/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B09/runs/20261011T225000Z-claude-B09-sharp-uniform-endpoint-tax/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B14/runs/20261011T224500Z-claude-B14-granularity-neutralization/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B15/runs/20261011T225100Z-claude-B15-erasure-countersearch/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B16/runs/20261011T225600Z-claude-B16-retained-kl-sandwich/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge/out/census_n4.stdout (4514 bytes)
- ~/brain_workers/FEI100_20261011/claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge/out/search_n56.stdout (6656 bytes)
- ~/brain_workers/FEI100_20261011/claude/B18/.current_run (101 bytes)
- ~/brain_workers/FEI100_20261011/claude/B18/runs/20261011T222429Z-claude-B18-proof-audit/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B19/runs/20261011T224700Z-claude-B19-paper-audit-rankcode/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/claude/B20/runs/20261011T225100Z-claude-B20-erasure-activation-transfer/.final (0 bytes)
- ~/brain_workers/FEI100_20261011/fei100.py.bak_acctend_1014 (19773 bytes)
- ~/brain_workers/FEI100_20261011/fei100.py.bak_linetop_1014 (20398 bytes)
- ~/brain_workers/FEI100_20261011/state.json.bak_acctend_1014 (68841 bytes)
- ~/brain_workers/FEI100_20261011/state.json.bak_linetop_1014 (68850 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/1708.03643.response (722401 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/2408.08457.response (265498 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/2408.12995.response (632616 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/2606.32024.response (473098 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/2609.15388.response (549084 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/arxiv.response (143532 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/arxiv_chemical.response (58833 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/arxiv_cost_exact.response (37478 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/arxiv_hex.response (2509 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/arxiv_target.response (217717 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/crossref.response (653715 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/crossref_source.response (29715 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/crossref_target.response (83213 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/github.response (5919 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/openalex_doi.response (20163 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/random_turn_hex.response (443079 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/semantic_source.response (28753 bytes)
- ~/brain_workers/TRIO_1011/op/C0020/source_pdf.pdf (1522266 bytes)
- ~/brain_workers/TRIO_1011/op/C0021/arxiv.xml (37546 bytes)
- ~/brain_workers/TRIO_1011/op/C0021/github_visualizer.json (2738 bytes)
- ~/brain_workers/TRIO_1011/op/C0021/source.pdf (1522266 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/1811.07038.pdf (465682 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/2010.01261.pdf (1110817 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/2408.14389.pdf (562624 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/arxiv.xml (5553 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/arxiv_broad.xml (30556 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/arxiv_invertibility.xml (26398 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/arxiv_jain.xml (90075 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/original.pdf (552011 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/second_cook.pdf (655974 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/second_inhomogeneous_search.xml (38320 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/second_jain.pdf (549508 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/second_taovu.pdf (282229 bytes)
- ~/brain_workers/TRIO_1011/op/C0031/survey.pdf (1157091 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/2009.09141.pdf (1696243 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/2412.13751.pdf (758423 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/Crossref_4.raw (172597 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/GitHub_6.raw (55 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/GitHub_7.raw (55 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/arxiv_0.raw (4813 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/arxiv_1.raw (53621 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/followup_3.raw (196880 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/followup_4.raw (8421 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/followup_5.raw (6513 bytes)
- ~/brain_workers/TRIO_1011/op/C0036/lyons2014.pdf (390464 bytes)
- ~/brain_workers/TRIO_1011/op/C0057/budd.pdf (702597 bytes)
- ~/brain_workers/TRIO_1011/op/C0057/conditioned.pdf (394430 bytes)
- ~/brain_workers/TRIO_1011/op/C0057/dichotomy.pdf (617198 bytes)
- ~/brain_workers/TRIO_1011/op/C0057/markov_pdf.pdf (1364490 bytes)
- ~/brain_workers/TRIO_1011/op/C0057/simple_pdf.pdf (1428946 bytes)
- ~/brain_workers/TRIO_1011/op/C0057/source.pdf (4911737 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/1506.01590.pdf (702597 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/1602.01328.pdf (1515343 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/1704.05297.pdf (1688676 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/1910.09623.pdf (10369198 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/1912.08790.pdf (980105 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/2304.01167.pdf (1571674 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/2311.08571.pdf (1592727 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/2411.05541.pdf (626651 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/2412.02666.pdf (1207834 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/2603.13642.pdf (617198 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/2604.24180.pdf (5489650 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/peccot.pdf (4911737 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/second_1102.2950.pdf (3106520 bytes)
- ~/brain_workers/TRIO_1011/op/C0059/second_math_0110296.pdf (378272 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/arxiv.xml (2668 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/arxiv_exact.xml (71690 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/arxiv_gasket.xml (743 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/arxiv_general.xml (184872 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/arxiv_positive.xml (203833 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/arxiv_prevost.xml (26862 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/fpp2023.pdf (1499575 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/geometry.pdf (1530546 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/signclusters.pdf (478709 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/source.pdf (1007278 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/sznitman2012.pdf (461105 bytes)
- ~/brain_workers/TRIO_1011/op/C0060/zeroone2026.pdf (463624 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/arxiv.response (31537 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/arxiv_clisby.response (801 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/arxiv_recent.response (100250 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/crossref.response (116749 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/crossref_source.response (17552 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/crossref_targeted.response (211456 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/github.response (281 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/graham.pdf (163564 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/hypercube.pdf (556982 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/openalex.response (609 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/openalex_citing_attempt.response (609 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/openalex_clisby.response (609 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/openalex_graham.response (609 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/openalex_source.response (609 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/openalex_source_doi.response (609 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/semantic_citing.response (123630 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/semantic_scholar.response (174 bytes)
- ~/brain_workers/TRIO_1011/op/C0097/source.pdf (873839 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/apollonian.pdf (1959086 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/arxiv.xml (122753 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/arxiv_convergence.pdf (419145 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/arxiv_fractions.xml (50344 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/arxiv_identity_dirichlet.xml (772 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/arxiv_identity_recent.xml (49176 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/arxiv_target.xml (115434 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/citation_leads.xml (4830 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/dimensional.pdf (1543264 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/ellipse.pdf (1177360 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/height_distribution.pdf (166684 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/source.pdf (2156680 bytes)
- ~/brain_workers/TRIO_1011/op/C0100/stability.pdf (577008 bytes)
- ~/brain_workers/TRIO_1011/op/C0101/apollonian.pdf (1125764 bytes)
- ~/brain_workers/TRIO_1011/op/C0101/f_lattice.pdf (5528023 bytes)
- ~/brain_workers/TRIO_1011/op/C0101/solitons.pdf (1099872 bytes)
- ~/brain_workers/TRIO_1011/op/C0101/source.pdf (2156680 bytes)
- ~/brain_workers/TRIO_1011/op/C0109/arxiv.xml (64478 bytes)
- ~/brain_workers/TRIO_1011/op/C0109/jalowy_w1.json (4293485 bytes)
- ~/brain_workers/TRIO_1011/op/C0109/source.pdf (2769596 bytes)
- ~/brain_workers/TRIO_1011/op/C0119/graham.pdf (209405 bytes)
- ~/brain_workers/TRIO_1011/op/C0119/source_pdf.pdf (586944 bytes)
- ~/brain_workers/TRIO_1011/op/C0119/surface_growth.pdf (288876 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/arxiv_velocity.xml (11822 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/arxiv_zeroone.xml (5171 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/paper_counterexample.pdf (309812 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/paper_exchangeable.pdf (301664 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/paper_mob.pdf (402504 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/paper_zeroone.pdf (231984 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/paper_zeroone_published.pdf (1165 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/source.pdf (489643 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/zerner2002.pdf (1163 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/zerner_correct_pdf.pdf (1159 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/zerner_download.pdf (1164 bytes)
- ~/brain_workers/TRIO_1011/op/C0133/zerner_euclid_modern.pdf (1055 bytes)
- ~/brain_workers/TRIO_1011/op/C0159/bell_pdf.pdf (521691 bytes)
- ~/brain_workers/TRIO_1011/op/C0159/source.pdf (1165 bytes)
- ~/brain_workers/TRIO_1011/op/C0160/source.pdf (1162 bytes)
- ~/brain_workers/TRIO_1011/op/C0160/subgroup_html.txt (692581 bytes)
- ~/brain_workers/TRIO_1011/op/C0160/subgroup_pdf.pdf (410805 bytes)
- ~/brain_workers/TRIO_1011/op/C0160/survey.pdf (649606 bytes)
- ~/brain_workers/TRIO_1011/op/C0160/survey_euclid_alt.txt (1163 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/arxiv.response (3760 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/arxiv_https.response (3722 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/crossref.response (159251 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/crossref_resolution.response (9789 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/crossref_source.response (12751 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/github.response (55 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/journal_pdf.response (3038 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/openalex.response (54 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/openalex_citing_source.response (44 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/openalex_resolution.response (44 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/openalex_retry_source.response (44 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/openalex_source.response (61 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/openalex_source_doi.response (44 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/resolution_pdf.pdf (324474 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/resolution_publisher.response (3038 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/semantic_resolution.response (27 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/semantic_scholar.response (45 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/semantic_source.response (940 bytes)
- ~/brain_workers/TRIO_1011/op/D0019/source.pdf (468241 bytes)
- ~/brain_workers/TRIO_1011/op/D0024/quenched_1804.06148.pdf (596751 bytes)
- ~/brain_workers/TRIO_1011/op/D0024/search_semantic_bulk.txt (586922 bytes)
- ~/brain_workers/TRIO_1011/op/D0024/source.pdf (164945 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/arxiv.response (4224 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/arxiv_exact_recent.response (12001 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/arxiv_facilitated.response (190110 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/arxiv_fredrickson.response (126705 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/arxiv_mathpr_recent.response (210535 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/arxiv_title.response (2605 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/crossref.response (189937 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/crossref_recent.response (425894 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/crossref_source.response (97840 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/cutoff.pdf (648070 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/front_pdf.pdf (651188 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/github.response (151619 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/github_fredrickson.response (10988 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/kcm_book.pdf (1878067 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/recent_hierarchy.pdf (913001 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/recent_thermodynamic.pdf (1492923 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/source.pdf (532424 bytes)
- ~/brain_workers/TRIO_1011/op/D0026/spectral_note.pdf (197291 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_exp_title.response (774 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_fa_title.response (2735 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_fredrickson.response (141195 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_gap_title.response (19639 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_html.response (804067 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_http.response (4224 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_https.response (136937 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_kcm.response (84458 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/arxiv_since_source.response (66990 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/cmrt_correct.pdf (493960 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/crossref.response (127881 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/crossref_exp.response (7400 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/crossref_precise.response (155252 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/crossref_source_title.response (52988 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/fa2013_correct.pdf (264820 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/fa_2013_pdf.pdf (2104916 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/github.response (108329 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/github_precise.response (10988 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/mountford_valle_html.response (3038 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/openalex.response (33 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/openalex_citing_source_attempt.response (33 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/openalex_source.response (33 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/openalex_source_lookup.response (33 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/oriented_2026.pdf (301380 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/semanticscholar.response (16 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/semanticscholar_citations.response (26 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/source.pdf (532424 bytes)
- ~/brain_workers/TRIO_1011/op/D0027/spectral_pdf.pdf (185462 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/arxiv.response (3802 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/arxiv_corners.response (63551 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/arxiv_laguerre.response (29796 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/arxiv_nested.response (782 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/bead.pdf (389861 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/beta_jacobi.pdf (262425 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/crossref.response (170457 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/crossref_corners.response (102459 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/dumitriu_edelman.pdf (223103 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/edelman_sutton.pdf (451734 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/github.response (55 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/jacobi_arxiv.response (1099383 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/jacobi_mit_second.response (262425 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/killip_nenciu.pdf (355494 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/second_crossref.response (23884 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/source.pdf (276733 bytes)
- ~/brain_workers/TRIO_1011/op/D0040/sutton_doi.response (3038 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/CIK.pdf (387098 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/CV.pdf (404167 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/CV_search.xml (3108 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/KRV.pdf (540784 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/arxiv.xml (63763 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/arxiv_critical.xml (31436 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/arxiv_exotic.xml (23549 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/arxiv_exotic_math.xml (17698 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/arxiv_higher.xml (45965 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/arxiv_nonregular.xml (12318 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/arxiv_virag.xml (1786 bytes)
- ~/brain_workers/TRIO_1011/op/D0043/source.pdf (276733 bytes)
- ~/brain_workers/TRIO_1011/op/D0047/dumaz_malvy.pdf (2129509 bytes)
- ~/brain_workers/TRIO_1011/op/D0047/rumanov.pdf (214453 bytes)
- ~/brain_workers/TRIO_1011/op/D0047/sine_operator.pdf (902714 bytes)
- ~/brain_workers/TRIO_1011/op/D0047/source.pdf (276733 bytes)
- ~/brain_workers/TRIO_1011/op/D0047/valko_virag.pdf (580762 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/arxiv.response (124634 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/arxiv_boundary.response (788 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/arxiv_kpz.response (13629 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/arxiv_targeted.response (191593 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/crossref.response (202520 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/crossref_source.response (47219 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/environment.pdf (1671988 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/extremal.pdf (296815 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/github_retry.response (55 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/gps.pdf (1434844 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/hmp.pdf (326501 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/kpz.pdf (655661 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/openalex_citations.response (610 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/openalex_correct_citations.response (610 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/openalex_correct_source.response (610 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/openalex_retry.response (610 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/openalex_search.response (610 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/openalex_source.response (610 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/response_calculus.pdf (456636 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/semantic.response (174 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/semantic_source.response (174 bytes)
- ~/brain_workers/TRIO_1011/op/D0051/source.pdf (2634164 bytes)
- ~/brain_workers/TRIO_1011/op/D0056/arxiv.xml (20454 bytes)
- ~/brain_workers/TRIO_1011/op/D0056/source.pdf (245224 bytes)
- ~/brain_workers/TRIO_1011/op/D0056/stable.pdf (297385 bytes)
- ~/brain_workers/TRIO_1011/op/D0056/sustainability.pdf (469768 bytes)
- ~/brain_workers/TRIO_1011/op/D0064/allez.pdf (330749 bytes)
- ~/brain_workers/TRIO_1011/op/D0064/freezing.pdf (521724 bytes)
- ~/brain_workers/TRIO_1011/op/D0064/shamov.pdf (422865 bytes)
- ~/brain_workers/TRIO_1011/op/D0064/source_curl.pdf (2860332 bytes)
- ~/brain_workers/TRIO_1011/op/D0064/uniqueness_supercritical.pdf (573492 bytes)
- ~/brain_workers/TRIO_1011/op/D0093/arxiv_http.xml (27850 bytes)
- ~/brain_workers/TRIO_1011/op/D0093/rolla.pdf (969581 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/arxiv.response (14 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/crossref.response (268443 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/crossref_active.response (100900 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/crossref_diffusive.response (0 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/github.response (28175 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/openalex.response (610 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/semantic.response (174 bytes)
- ~/brain_workers/TRIO_1011/op/D0097/source.pdf (969581 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/arxiv.xml (35244 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/arxiv_exclusion.xml (4784 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/arxiv_target.xml (34108 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/asymmetric.pdf (744541 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/comparison.pdf (150067 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/interface.pdf (975783 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/slow.xml (3162 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/source.pdf (502730 bytes)
- ~/brain_workers/TRIO_1011/op/E0007/voter.xml (6676 bytes)
- ~/brain_workers/TRIO_1011/op/E0012/allelopathy.pdf (1259994 bytes)
- ~/brain_workers/TRIO_1011/op/E0012/journal_retry.pdf (1425055 bytes)
- ~/brain_workers/TRIO_1011/op/E0012/source.pdf (502730 bytes)
- ~/brain_workers/TRIO_1011/op/E0019/fast2022.pdf (320654 bytes)
- ~/brain_workers/TRIO_1011/op/E0019/feller2023.pdf (466094 bytes)
- ~/brain_workers/TRIO_1011/op/E0019/linear2024.pdf (603538 bytes)
- ~/brain_workers/TRIO_1011/op/E0019/one_dim_2025.pdf (521338 bytes)
- ~/brain_workers/TRIO_1011/op/E0019/singular2020.pdf (459834 bytes)
- ~/brain_workers/TRIO_1011/op/E0019/source.pdf (952986 bytes)
- ~/brain_workers/TRIO_1011/op/E0019/torus2017.pdf (268736 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/arxiv_search_html.raw (191542 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/bhp2023_pdf.raw (505316 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/bhp2025_pdf.raw (405434 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/bhp2026_pdf.raw (484615 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/concentration_pdf.raw (453059 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/crossref.raw (268151 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/crossref_kakutani.raw (7347 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/crossref_math.raw (345373 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/crossref_phrase.raw (106646 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/github.raw (55 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/github_phrase.raw (30485 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/kanda_original.pdf (972513 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/li_pdf.raw (208620 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_absolute_H.raw (524904 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_citations.raw (383 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_phrase.raw (1023342 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_published.raw (10228 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_published_citations.raw (38521 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_search.raw (1253030 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_source.raw (92098 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/openalex_symmetric_H.raw (519849 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/published_metadata.raw (14307 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/semantic_citations.raw (7819 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/source_pdf.pdf (295535 bytes)
- ~/brain_workers/TRIO_1011/op/E0024/two_theorems_pdf.raw (279145 bytes)
- ~/brain_workers/TRIO_1011/op/E0025/concentration_2023_pdf.pdf (453059 bytes)
- ~/brain_workers/TRIO_1011/op/E0025/diffusions_2021_pdf.pdf (208620 bytes)
- ~/brain_workers/TRIO_1011/op/E0025/survey.pdf (295535 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/bhp_survey_pdf.pdf (405434 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/concentration_pdf.pdf (453059 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/diffusion_pdf.pdf (208620 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/ekfr_original.pdf (260046 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/oa_title.json (2160385 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/rao_actual.pdf (325626 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/rao_pdf.json (9595498 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/rao_pdf.pdf (9595498 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/s2_bulk.json (465029 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/source_pdf.pdf (295535 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/sum_pdf.pdf (216431 bytes)
- ~/brain_workers/TRIO_1011/op/E0027/transforms_pdf.pdf (279145 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/arxiv.response (45185 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/arxiv_https.response (45185 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/citing_W1544252356_1.response (114643 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/citing_W2081343974_1.response (447100 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/citing_W2081343974_2.response (456520 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/citing_W2081343974_3.response (146534 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/crossref_0.response (76753 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/crossref_1.response (105276 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/crossref_2.response (135540 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/degenerate2026.response (9447 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/github_0.response (55 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/gz2012.pdf (146266 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/gz2025.response (7898 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/openalex_0.response (453416 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/openalex_1.response (466072 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/openalex_2.response (491154 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/regularity2011.pdf (230968 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/saburov2015.pdf (1052 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/semantic_1.response (21194 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/source.pdf (165225 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/source_lookup.response (148518 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/springer2026.response (3038 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/target_openalex_0.response (411131 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/target_openalex_1.response (341615 bytes)
- ~/brain_workers/TRIO_1011/op/E0062/target_openalex_2.response (394276 bytes)
- ~/brain_workers/TRIO_1011/op/E0066/abdulghafor2016.pdf (0 bytes)
- ~/brain_workers/TRIO_1011/op/E0066/arxiv.xml (14586 bytes)
- ~/brain_workers/TRIO_1011/op/E0066/regular.pdf (156958 bytes)
- ~/brain_workers/TRIO_1011/op/E0066/saburov2016.pdf (14371 bytes)
- ~/brain_workers/TRIO_1011/op/E0066/source.pdf (165225 bytes)
- ~/brain_workers/TRIO_1011/op/E0072/cancelation_norm.pdf (297868 bytes)
- ~/brain_workers/TRIO_1011/op/E0072/source.pdf (370230 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/arxiv.response (15468 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/arxiv_https.response (99941 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/arxiv_pitman_tang.response (2381 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/arxiv_targeted.response (38034 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/crossref.response (89730 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/crossref_2012.response (14264 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/crossref_extremal.response (214119 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/crossref_targeted.response (95995 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/paper_1602.06512.response (150052 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/paper_2410.13426.response (120473 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/paper_2601.16580.response (1255481 bytes)
- ~/brain_workers/TRIO_1011/op/E0081/second_arxiv_firstpassage.response (3601 bytes)
