# Reference measures for the Fourier entropy-influence inequality

Group W2-C, 23 September 2026. FEI is neither proved nor refuted here.

Proved.
1. No level-wise product reference can prove FEI. This class contains product measures, every conditional Bernoulli law on each level, F5's rank-weighted measure for every ordering and exponent, and every influence-weighted product. On depth-d recursive ternary majority every such reference costs at least (d − 1)·I bits, while H = 4(I − 1) (Theorem 1; the exact optimum is tabulated to d = 10).
2. Count-splitting tree references reveal the spectral sample by splitting |S| down a tree over the coordinates. They are exact precisely for count-Markov spectral laws. Every symmetric function is count-Markov along every tree, the class is closed under read-once composition, and AND, OR and XOR gates can be binarized without loss. Every such reference costs at most H(|S|) + E log C(n,|S|) (Theorem 2).
3. The information a restricted block R carries about the rest of the spectral sample is at most (2/ln 2)·Inf(R). Consequently FEI is equivalent to a block-erasure inequality: K_b ≤ C_FEI ≤ K_b + 2/ln 2 (Lemma 3, Theorem 4).
4. Any adaptive single-coordinate exploration of S gives a valid reference with rank costs. This is F5's Lemma 6 with adaptivity (Proposition 5).
5. A fixed reference cannot serve a random relabelling of a function: its average cost is at least E log C(n,|S|) (Lemma 6).

Numerical. The optimal binary count-splitting tree was computed exactly by a subset dynamic programme. It costs H to within 4e-15 bits on majority, tribes, recursive majority, addressing and AND/OR chains, and within 1.3e-5 bits on F4's monotone flip family. Other losses: at most 0.012 bits on bent-plus-flip, 0.07–0.16 bits on threshold functions, and 0.11–0.16 bits (0.056–0.078·I) on Numaro's g and its restrictions. Samples tested: all 65,536 functions of four variables, 100,000 random functions of five, 20,000 of six, and adversarial searches at six to eight variables. On these the best count-splitting cost divided by I never exceeds the sample's largest H/I, and the loss over H never exceeds 1.39 bits (0.36·I). The only structural loss found is on mixtures of incompatible hierarchies: a multiplexer between recursive majority and a scrambled copy loses 0.25 bits; four scrambled copies lose 0.39 bits.

Conjectural. A single tree fails on such mixtures as the depth grows, with loss of order d·I. So a universal reference must mix count-splitting trees over restricted blocks, and Lemma 3 controls the price of that. The erasure term of Theorem 4 is what remains unpaid.

Refuted. Level-wise product references (Theorem 1). Hit-only trees as the best hierarchical family: count-splitting beats them on every tested function, and they lose 0.83·I on majority at n = 17, with the loss still growing. Single-coordinate adaptive exploration with rank costs: a heuristic lower bound of order d·log(4/3)·I on recursive majority (Section 5).

## 0. Notation

f: {−1,1}^n → {−1,1}. The spectral sample S has Pr[S = A] = f̂(A)², so H(f) = H(S), I(f) = E|S| and Inf_i = Pr[i ∈ S]. Logarithms are base 2 unless written ln.

For a block B of coordinates, c_B = |S ∩ B|. For J disjoint from R = [n] ∖ J and z ∈ {−1,1}^R, f_{J|z} is the restriction to J.

A reference is any probability Q on subsets of [n]. Gibbs' inequality gives H(f) ≤ E log 1/Q(S), with equality iff Q = P on the support.

## 1. Level-wise product references cannot prove FEI

A level-wise product reference has the form Q(S) = ρ(|S|) ∏_{i∈S} w_{|S|,i} / e_{|S|}(w_{|S|}), with any law ρ on levels and any positive weights (e_k is the elementary symmetric polynomial). Product measures and F5's Lemma 6 measure are special cases, for every ordering and every exponent.

Theorem 1 (proved). Let g_d = Maj3^{∘d}, n = 3^d, I = (3/2)^d. Every level-wise product reference satisfies E log 1/Q(S) ≥ H(|S|) + E log C(n,|S|) ≥ (d − 1)·I, while H(g_d) = 4(I − 1).

Proof.
- Setup. With θ_k = ln w_k, the cost is E[−log ρ(|S|)] + Σ_k P_k Φ_k(θ_k), where Φ_k(θ) = (1/ln 2)·E[ln e_k(e^θ) − Σ_{i∈S} θ_i | |S| = k].
- Convexity. ln e_k(e^θ) is a log-sum-exp of linear forms, so Φ_k is convex.
- Symmetry. The automorphism group of g_d (the ternary-tree automorphisms) preserves the law of S and acts transitively on the leaves. Averaging θ over the group therefore does not increase Φ_k, and it yields constant weights, i.e. the uniform law on k-sets, of cost log C(n,k). The ρ term is at least H(|S|) by Gibbs.
- Size of |S|. S is the leaf set of a Galton–Watson tree of depth d whose offspring is 1 with probability 3/4 and 3 with probability 1/4 (mean m = 3/2, variance 3/4). So |S| = (3/2)^d·W_d with E W_d = 1, and E[|S| log(n/|S|)] = I·(d − E[W_d log W_d]).
- Second moment. E W_d² = 1 + (3/4)(m^d − 1)/(m^{d+1}(m − 1)) ≤ 2. By Jensen under the size-biased law, E[W log W] ≤ log E W² ≤ 1. Since log C(n,k) ≥ k·log(n/k), the cost is at least (d − 1)·I.
- Entropy. H = 4(I − 1): two bits for each of the 2(I − 1) expected internal nodes of the tree. □

Exact optimum divided by I (`code/recmaj_levelwise.py`), for d = 2..10: 2.7123, 3.8934, 4.9544, 5.9587, 6.9395, 7.9130, 8.8870, 9.8645, 10.8462. Over the same range H/I goes from 2.2222 to 3.9306. The d = 2 value agrees with an independent optimizer run on the actual spectrum (`logs/run_families.log`).

## 2. Count-splitting tree references

Construction. Take a tree T whose leaves are the coordinates. (1) Draw c_root = |S| from its true law. (2) At each internal node v, draw the children's counts from their true conditional law given c_v. (3) Leaf counts are 0 or 1 and determine S. The expected cost is

CS_T(f) = H(|S|) + Σ_v [H(children's counts) − H(c_v)].

Hit-only references are the same construction with every count replaced by min(c, 1).

Theorem 2 (proved).
- (i) H ≤ CS_T ≤ H(|S|) + E log C(n,|S|) for every T.
- (ii) CS_T = H iff for every internal v, S ∩ B_v is conditionally independent of S ∖ B_v given c_v ("T-count-Markov").
- (iii) An exchangeable spectral law, in particular that of any symmetric f, is T-count-Markov for every T.
- (iv) Let F = G(f_1, …, f_k) on disjoint blocks, and let T have a node whose subtrees T_j are trees on the blocks, with each f_j T_j-count-Markov. Then F is T-count-Markov. If G is AND, OR or XOR (with any negations), that node can be replaced by any binary tree over its inputs without losing exactness.

Proof. (i) CS_T is the minimum of the cross-entropy over all node laws; choosing hypergeometric node laws telescopes to Q(S) = P(|S|)/C(n,|S|), which gives the upper bound. (ii) Compare Q_T with the chain rule for P over the tree, node by node. (iii) Given c and S ∖ B_v, every c-subset of B_v has the same probability. (iv) By the composition identity, P(S) = Ĝ_μ(U)² ∏_{j∈U} f̂_j(S_j)²/V_j, so S_j enters only through 1[S_j ≠ ∅] and f̂_j(S_j)², and c_j determines the first. For AND, Ĝ_μ(U) = −2 ∏_{i∉U} p_i ∏_{i∈U} σ_i when U ≠ ∅, so the gate law is a product measure on nonempty U. For XOR it is a product measure everywhere. □

Checks (`logs/test_countsplit.log`): majority is exact along balanced, caterpillar and random trees; depth-2 recursive majority is exact along its natural ternary tree and along its natural binarization, while the hit-only reference loses 1.72 bits there; tribes 3×4 is exact. Conditional Bernoulli laws, and hence F5's reference, are caterpillar count-splitting references whose node laws also depend on k.

## 3. Numerics

Both dynamic programmes agree with brute force over all 15, 105 and 945 binary trees at n = 4, 5, 6 to within 2e-15. In the table, CS is the optimal count-splitting tree, HIT the optimal hit-only tree, LW the optimal level-wise product reference, and F5 is F5's reference ordered by influence with the best exponent. All costs are divided by I.

| function | n | H/I | CS/I | CS − H (bits) | HIT/I | LW/I | F5/I |
|---|---|---|---|---|---|---|---|
| majority | 13 | 2.3024 | 2.3024 | 4e-15 | 3.0859 | 2.3024 | 2.4672 |
| tribes w4 s3 | 12 | 3.4272 | 3.4272 | 0 | 3.4272 | 4.3676 | 4.6097 |
| rec. majority d2 | 9 | 2.2222 | 2.2222 | 0 | 2.9875 | 2.7123 | 2.8770 |
| addressing k3 | 11 | 2.4000 | 2.4000 | 0 | 2.4000 | 2.6488 | 3.0609 |
| AND/OR chain | 12 | 2.3771 | 2.3771 | 1e-15 | 2.3771 | 2.4014 | 2.4796 |
| Maj13 + flip (F4 6.1) | 14 | 2.3036 | 2.3036 | 7.4e-8 | 3.0864 | 2.3036 | 2.5947 |
| bent + flip, m = 6 | 7 | 2.0779 | 2.0819 | 0.0116 | 2.0885 | 2.0871 | 2.2883 |
| LTF, Gaussian weights | 12 | 2.4477 | 2.5129 | 0.1635 | 3.0037 | | |
| LTF, weights i^(−1/2) | 14 | 2.3779 | 2.4254 | 0.1287 | 3.0318 | | |
| Numaro g, core + 5 coins | 14 | 3.2857 | 3.3440 | 0.1181 | 3.3855 | | |
| Numaro g (hit-optimal tree) | 18 | 3.3234 | 3.4012 | 0.1586 | 3.4356 | 3.3998 | 3.9481 |
| mux(recmaj, scrambled copy) | 10 | 2.3608 | 2.4629 | 0.2473 | 3.0734 | 2.6865 | 3.0177 |
| 2 address bits, 4 scrambled copies | 11 | 2.4535 | 2.6047 | 0.3934 | 3.1175 | | |

For Numaro's g at n = 18 the exact dynamic programme is too large, so the tree is the hit-optimal one; 70 random leaf swaps found no improvement. On majority the hit-only loss, (HIT − H)/I, is 0.58 at n = 5 and rises steadily to 0.83 at n = 17; count-splitting is exact there.

| sample | max H/I | max CS/I | max CS − H | max (CS − H)/I |
|---|---|---|---|---|
| all functions, n = 4 | 3.40248 | 3.40248 | 0.6887 bits | 0.3444 |
| 100,000 random, n = 5 | 3.62374 | 3.62374 | 0.6876 | 0.2755 |
| 20,000 random, n = 6 | 3.73976 | 3.73976 | 0.6930 | 0.2431 |
| hill climbing, n = 6 / 7 / 8 | | 3.6628 / 3.7664 / 2.6298 | 1.019 / 1.389 / 1.199 | 0.360 / 0.328 / 0.255 |

On every function in the three samples, count-splitting was at least as good as the best hit-only tree. When the climb maximizes CS/I it ends on AND-type functions, where CS = H. The n = 8 climb for CS/I was short and did not reach AND_8.

## 4. The price of latent structure

Lemma 3 (proved). H(f) = E_z H(f_{J|z}) + I(z; S_J) + H(S ∩ R | S_J), and I(z; S_J) ≤ (2/ln 2)·Σ_{t∈R} Inf_t(f).

Proof. Mixture: by Parseval in z, the law of S_J is the average over z of the spectral laws of f_{J|z}; the identity follows from the chain rule and the entropy-of-a-mixture formula. One coordinate at a time: reveal z coordinate by coordinate; each step's information is the Jensen–Shannon divergence of two mixtures, and JS is jointly convex (it is the perspective of a convex function), so it is at most the average over z_{>t} of the JS of the two coordinate-t restrictions of g = f_{J∪{t} | z_{<t}, z_{>t}}. Bound per coordinate: F4 Lemma 1.1(b,c) bounds that JS by (2/ln 2)·η_t(g) ≤ (2/ln 2)·Inf_t(g), and E Inf_t(g) = Inf_t(f). Sum over t ∈ R. □

Numerical check (2,092 cases: every function of three variables with every block, and random, biased and threshold functions up to n = 8): the largest ratio of I(z; S_J) to the bound is 0.831. The mixture identity was checked by two independent routes, the marginal of the full spectrum against the average of the restricted spectra, which agree exactly.

Theorem 4 (proved). Let K_b = sup_f min_R H(S ∩ R | S ∖ R)/Inf(R), over blocks R containing a relevant coordinate. Then K_b ≤ C_FEI ≤ K_b + 2/ln 2.

Proof. Taking R = [n] gives K_b ≤ C_FEI. For the other direction, induct on the number of relevant variables with C = K_b + 2/ln 2, using Lemma 3 and E_z I(f_{J|z}) = I(f) − Inf(R). □

Blocks versus single coordinates on the towers of g. Restricting a whole sub-tower G_{k−1} that feeds input j of the top gate lowers the entropy by Δ_j(g) + Inf_j(g)·H(G_{k−1}). The block ratio, [Δ_j(g) + Inf_j(g)·H(G_{k−1})] / [Inf_j(g)·I(G_{k−1})], tends to 6.5218, below the single-coordinate limit 7.1116 from F4. For such deep blocks, data processing gives I(z; S_J) equal to the JS of the single coordinate x_j in g(G_{k−1}, …, x_j, …, G_{k−1}).

Lemma 6 (proved). For any fixed Q, E_π E_{P_{f∘π}} log 1/Q ≥ E_{P_f} log C(n,|S|). This follows from Jensen, because averaging Q over relabellings gives Q(level)/C(n, |S|).

Mixtures of hierarchies. For the multiplexer x_0 ? g_d(y) : g_d(πy), the marginal of S on y is exactly (P_g + P_{g∘π})/2. Conjecture: for random π, min_T CS_T/I → ∞, at a rate of order d; what is proved is only that each fixed tree is bad for most π (Lemma 6). Remedy: restricting x_0 first (cost at most 2.885·Inf_{x_0}) and then using one tree per branch removes this loss. At d = 2 the loss is small because the exchangeable reference is already within 0.49·I of H (the three random scramblings tried each disagree with g on a fraction 0.171875 of inputs and share 27 spectral sets with it).

## 5. Adaptive single-coordinate exploration

Proposition 5 (proved). Reveal k = |S|, then query coordinates one at a time in any adaptive order, and stop once k members have been found. Use the membership probability q_s = min(1/2, (k/s)^a) at step s. Then for every a > 1:

H(S) ≤ H(|S|) + E|S|·[1 + (2/ln 2)(2^{1/a}/2 + 2^{1/a−1}/(a − 1))] + a·E Σ_{i∈S} log⁺(pos(i)/|S|).

Heuristic failure on recursive majority (not proved). An empty subtree of height h absorbs about 2^h queries before its posterior probability of being hit becomes small. Summed over the hit nodes, the query count reaches about 2^d while |S| is about (3/2)^d. So a constant fraction of the members pay about d·log(4/3) bits each. Tree references avoid this because they can ask whether a whole block is empty.

## 6. Where general functions resist

Count-splitting gives H ≤ H(|S|) + Σ_v H(c_{v1} | c_v), and H(|S|) ≤ 3I by O'Donnell–Wright–Zhou. A node's term exceeds what its influence pays only where count-Markov fails; in every family tested, this happened only when a hierarchy is selected by other coordinates, and Lemma 3 prices restricting the selecting coordinates. What remains unpaid is the erasure term H(S ∩ R | S ∖ R) of the selecting block, which is F4's B_i when R is a single coordinate; by Theorem 4 this term is all of FEI, up to 2/ln 2. A proof would need, in place of Littlewood–Offord, a bound on each node's count-split entropy in terms of the influence of its block, for a tree chosen after the selecting blocks are restricted. For threshold functions F5's rank argument supplies such a bound (F5's result is under audit). For symmetric functions and read-once formulas the reference is exact. For general functions no rule for choosing the tree is known; numerically, a good tree exists for every function tested up to 18 variables.

## 7. Files (under `W2-C-reference-measures/`)

Code (`code/`): `wlib.py` (spectra, families, hit-only tree DP in 3^n, level-wise optimizer, F5 cost); `countsplit.py` (count-splitting cost along a given tree); `csdp.py` (exact optimal count-splitting tree, 5^n); `test_wlib.py`, `test_countsplit.py`, `test_csdp.py` (checks against brute force); `run_families.py`, `run_cs_families.py` (the families table); `exhaustive_small.py`, `adversarial_cs.py` (the small-n sweeps and hill climbing); `g18_cs.py` (Numaro's g); `recmaj_levelwise.py` (the Theorem 1 table); `check_block_lemma.py`, `check_mixture.py` (Lemma 3 checks).

Logs (`logs/`): one log per script, plus `run_families.json`, `run_cs_families.json` and `g18_cs.json`.

A precision note: F4's monotone flip family is represented by the count-splitting tree to within 1.3e-5 bits at n = 10 and 7.4e-8 bits at n = 14, not exactly.
