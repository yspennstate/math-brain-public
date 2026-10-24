# W3-04: where the log I in Kelman-Kindler-Lifshitz-Minzer-Safra comes from

Group W3-04, 23 September 2026. The log I factor of Kelman–Kindler–Lifshitz–Minzer–Safra (KKLMS, arXiv:1911.10579v2) is not removed here, nor any power of it, and no new class on which it disappears was found. What is here is a complete map of the paper's proof, a proof that the log is built into the form of their main inequality rather than being a weakness of their parameters, and one modest positive result.

Status of each claim.
- PROVED, Proposition H. In the induction of KKLMS Theorems 5.2 and 6.6, every allowed choice of degrees and thresholds gives a leading constant with ln C1 ≥ ℓ·d·ln(d/d_1). The cost of each degree-reduction level adds up like a harmonic sum, so the scheme can only certify coefficients smaller than (d/d_1)^{-d} as small.
- PROVED, Lemma V and Proposition M. The form of KKLMS Corollary 6.7 is itself essentially sharp. Take f = (1 − Maj_n)/2 with n ≈ k^{4β−5}. Then any inequality of that form with cross-influence coefficient B ≤ b·k^{-β}, β > 3/2, must have leading constant A ≥ k^{(β−3/2−o(1))k}. For KKLMS's own B this reads A ≥ δ^{-(1/16−o(1))d}; they prove δ^{-10^5 d}, so their exponent is right up to a constant. If B ≥ 1/(αd), the inequality says nothing.
- The majority witness is monotone, symmetric, a threshold function, and has all influences O(n^{-1/2}). So none of the suggested classes (monotone, all influences small as in F4, noise-sensitive derivatives as in F5) rescues this inequality form.
- PROVED, Theorem A. KKLMS's per-set charge C|S|log(|S|+1) is needed only on their large-coefficient bucket. There it can be replaced by the minimum of any fixed number of reference-measure charges, in particular exact counting and F5's rank-weighted measure.
- NUMERICAL. With g a band of levels [d/2, d], the threshold drops to β > 1.
- NUMERICAL. KKLMS's bound overcharges on actual functions. On majority, E_μ log2(|S|+1) grows like log2 n (14.6 at n = 100001) while H/I stays at 2.88. On tribes it grows like log w; on recursive majority and on the towers of Numaro's g it grows with the depth.
- NUMERICAL. In every family tested, the influence-weighted tail μ(λ ≥ C) decays exponentially; λ is defined in Section 0.
- Conclusion: no argument that combines per-level inequalities of Corollary 6.7's form with bucket accounting can remove the log. What is missing is an inequality that couples the levels.

## 0. Conventions

KKLMS use f: {0,1}^n → {0,1}, natural logarithms, I_i[f] = ||∂_i f||_2^2 (a quarter of the usual influence), and the cross-influence I[f,g] = Σ_i √(I_i[f]·I_i[g]). Here F = 1 − 2f is ±1-valued, so F̂(S) = −2f̂(S) for S ≠ ∅. H and I are in bits and in the ±1 convention, as in CONTEXT.md.

Two derived quantities are used throughout: the size-biased spectral law μ(S) = |S|F̂(S)^2/I, and the per-element log-coefficient λ(S) = log2(1/F̂(S)^2)/|S|. Fubini gives the identity

  H − F̂(∅)^2 log2(1/F̂(∅)^2) = I·∫_0^∞ μ(λ ≥ C) dC.

So FEI is equivalent to a uniform bound on the integral of the tail μ(λ ≥ C). KKLMS Theorem 1.3 in this language says E_μ λ ≤ K(1 + E_μ log2(|S|+1)).

## 1. Proof map of KKLMS

### 1.1 Tools (Sections 2–3)

- Fact 2.4: Σ_{|T|≤v} I_T[f^{≤d}] ≤ 2d^v·||f||^2. This bounds the number of heavy generalized influences.
- Lemma 2.6: E_z I[f_{I→z}, g_{I→z}] ≤ Σ_{i∉I} I_i[f,g].
- Lemma 2.7: E_z ĝ_{restricted}(S)^2 = Σ_{T: T∩I = S} ĝ(T)^2. It links coefficients of restrictions to partial generalized influences. The statement prints J→z where I→z is meant.
- Theorem 2.8 (Bonami): ||h||_q ≤ (q−1)^{deg(h)/2}·||h||_2.
- Lemma 3.3 and Corollary 3.4 (random partitions into m parts, Chernoff plus a union bound). An (α,d)-almost-homogeneous g keeps a fraction (1 − 2m·e^{-ε²αd/(3m)}) of Σ|f̂ĝ| on the sets that meet every part in [(1−2ε)αd', d'], where d' = (1+ε)d/m. The printed lemma omits the factor m; its proof has it.
- Lemma 3.5 (exchanging max and expectation, Bonami at q = 4): E max_i h_i^2 ≤ 3^d·max_i||h_i||·(E Σ_i h_i^2)^{1/2}.
- Lemma 5.1 (two-function version, Hölder pair (4/3, 4)): E(Σ|h'_i|^{4/3}|h_i|^{4/3})^{3/4} ≤ 3^d·max(||h_i||·||h'_i||)^{1/4}·(EΣh'^2·EΣh^2)^{3/8}. It holds with 3^{d/2}.
- Fact 6.2 and Corollary 6.3 (exact partitions): Pr[|S∩I_i| = v for all i] ≥ (16√v)^{-d/v}.

### 1.2 Base cases

- Lemma 4.3 (the KKL step). If deg g ≤ d, then ⟨f,g⟩ ≤ (d/δ)^d·max|f̂ĝ| + 2·3^{d/4}·δ^{1/8}·I[f,g]. Split the sets S into those inside Inf = {i : I_i[f^{≤d}] ≥ δ} (at most d/δ variables) and the rest; the rest is handled by Hölder (4/3, 4), Bonami, and Booleanity, ||∂_i f||_{4/3} ≤ 2I_i^{3/4}.
- Lemma 5.3 is the same statement with (Σ|f̂ĝ|^{4/3})^{3/4} and the factor (d/δ)^{d/4}.

### 1.3 Induction (Theorems 4.1, 5.2, 6.6)

Step from degree d_k to d_{k-1}:
1. Take a partition into m = (1+ε)d_k/d_{k-1} parts (Corollary 3.4) and keep the part g̃ of g on well-spread sets.
2. For each part j, let T_j be the sets T ⊆ I_j with I_{T,I_j}[f] ≥ δ_k||f||^2 or I_{T,I_j}[g̃] ≥ δ_k||g̃||^2. Then |T_j| ≤ 2/δ_k.
3. Bad sets B = {S : S∩I_j ∈ T_j for every j}. Then |B| ≤ (2/δ_k)^m, and term (I) ≤ |B|^{1/4}·(Σ|f̂ĝ|^{4/3})^{3/4}.
4. Every other S has a light part j. Write ⟨f,g̃_j⟩ = E_z⟨f_{J→z}, (g̃_j)_{J→z}⟩ and apply the induction hypothesis at degree d_{k-1}. This produces three terms: (III), the coefficient term, which Lemma 5.1, Lemma 2.7 and lightness bound by 3^{d_k}·δ_k^{1/4}·||f||·||g||; (IV), the cross-influence term, via Lemma 2.6; (V), by Cauchy–Schwarz.
5. Resulting constants: C1(k) = 2^k(2/δ_k)^{(1+ε)d_k/(4d_{k-1})}, C2(k) = 2·C2(k−1), and C3(k) ≥ 2m[C1(k−1)·3^{d_k}·δ_k^{1/4} + C3(k−1)].

How the three versions differ: Theorem 4.1 counts heavy sets only for g and uses a max term, so it needs δ_{j+1} ≈ δ_j^{4d_j/d_{j−1}}; Corollary 4.2 uses 1/ε levels with d_j = d^{j/k}; Corollary 5.4 needs δ ≤ 2^{-16d^ε/ε} and gives δ^{-6d}, and only gives FEI up to poly(log I) because the base case is entered at degree poly(log d).

### 1.4 Section 6 and Corollary 6.7

- Lemma 6.4 and Corollary 6.5 (boosted base case): reduce degree e' = 10^k to 1 in steps of 10 using exact partitions. The cost is (16√e_i)^{10} per step, which is affordable when η ≤ 10^{-320√e'}.
- Theorem 6.6 runs the Theorem 5.2 induction on top of this base at d_1 = e'. Its inductive step is omitted in the paper. In its k = 1 case, the variable splitting x_i → x_{i,1} + … must be read as parity so that f stays Boolean.
- Corollary 6.7 parameters: e' = (1000/α)(log d)^2, d_{i+1} = 2d_i, ε = 1/log d, δ_2 = δ^{1600 d_1}, δ_{i+1} = δ_i^{2(1+ε)^2}. Conclusion, for δ ≤ d^{-96000/√α}:

  ⟨f,g⟩ ≤ δ^{-10^5 d}·||f||^{3/4}·||g||^{3/4}·max_{|S|∼d}|f̂ĝ|^{1/4} + δ^{1/16}·I[f,g] + δ·||f||·||g||.

  The proof actually bounds the second coefficient by δ^{1/32}, not δ^{1/16}; this is harmless.

### 1.5 Section 7

- Theorem 1.3. Buckets S_{d,k} = {|S| = d : 2^{-C(k+1)d·log(d+1)}√var < |f̂(S)| ≤ 2^{-Ckd·log(d+1)}√var}. For k ≥ 1, apply Corollary 6.7 with δ = 2^{-32k}·d^{-10^5} and I[f,g] ≤ √(2d)·I; the bucket mass is ≤ 2^{-k}d^{-10}·O(I), so these buckets contribute O(C·I) entropy in total. Bucket 0 is charged 2Cd·log(d+1) + log(1/var) per unit mass.
- Theorem 1.1: the same with log(1+Ĩ), δ = 2^{-256k}d^{-10^5}Ĩ^{-16} and D = 10Ĩ.
- Theorem 1.2: from Theorem 1.3 with D = 2Ĩ/η and Markov's inequality.
- Corollary 7.1 (Bourgain–Kalai type) follows from Theorem 1.1.

### 1.6 Exactly where the log enters

- (a) In Corollary 6.7, through the constraint δ ≤ d^{-O(1)}, from two sides. The Chernoff step needs d_{j−1} ≳ log(ratio)/ε², with ε ≈ 1/(number of levels) = 1/log d, so that (1+ε)^{2k} stays bounded; this forces e' ≈ log² d, and then the boosted base needs η ≤ 10^{-O(√e')} = d^{-O(1)}. Each level pays 6^{d_{j+1}}·δ_j^{ε/2} in C3, with ln(1/δ_j) ≈ 800 d_j·ln(1/δ); so ε·ln(1/δ) ≳ 1, again ln(1/δ) ≳ log d.
- (b) In Theorem 1.3: the first term δ^{-Θ(d)} forces bucket thresholds 2^{-Θ(d log d)}, and bucket 0 is charged d·log d.
- (c) In the accounting: I[f,g] ≤ √(2d)·I independently forces B, hence δ, to be polynomially small in d.
- (d) In Theorems 1.1 and 1.2 through D ∝ Ĩ.

## 2. The obstruction

### 2.1 Proposition H (harmonic accumulation, PROVED)

Statement. Let 1 ≤ d_1 < … < d_K = d, let ℓ, s > 0, and let c_1 ≥ 0 and δ_j ∈ (0,1) satisfy, for 2 ≤ j ≤ K: (a) c_j ≥ s·m_j·ln(1/δ_j) with m_j ≥ d_j/d_{j−1}; (b) s·ln(1/δ_j) ≥ c_{j−1} + ℓ(d_j − d_{j−1}). Then c_K ≥ d·(c_1/d_1 + ℓ·ln(d/d_1)).

Proof. From (a) and (b), c_j ≥ (d_j/d_{j−1})·(c_{j−1} + ℓ(d_j − d_{j−1})). Divide by d_j and use x − 1 ≥ ln x: c_j/d_j ≥ c_{j−1}/d_{j−1} + ℓ·ln(d_j/d_{j−1}). Summing over j gives the claim. ∎

Why the hypotheses hold in KKLMS: c_j = ln C1(j), s = 1/4, and m_j is the number of parts, which must be at least d_j/d_{j−1} for homogeneous g. (b) holds because C3 multiplies ||f||·||g|| and must be below 1 for the inequality to say anything; the (III) contribution m·C1(j−1)·3^{D}·δ_j^{1/4} is part of C3, and the degree D of z ↦ ĝ_{J→z}(S) is at least d_j − d_{j−1}.

Consequence. Certifying that coefficients of size τ carry little mass needs C1·τ^s ≤ 1, that is, |f̂| ≤ (d/d_1)^{-(ℓ/2s)d}. Replacing the Hölder pair (4/3, 4) by (r, 2r/(2−r)) gives ℓ/s = r·ln((3r−2)/(2−r))/(2(r−1)) ≥ 2, with limit 2 as r → 1, so no Hölder pair helps. The certifiable threshold is |f̂| ≤ (d/d_1)^{-d}, which means λ ≥ 2·log2(d/d_1). The tax per level is proportional to the relative degree increase, and the multiplicative bad-set count |B| ≤ ∏|T_j| makes those taxes add up as a harmonic sum.

### 2.2 Lemma V (PROVED)

Statement. Let f be Boolean and g = Σ_{S∈𝒮} f̂(S)χ_S with every |S| ≥ αd. Then I[f,g] ≥ I[g] ≥ αd·⟨f,g⟩.

Proof. I_i[g] ≤ I_i[f], so √(I_i[f]I_i[g]) ≥ I_i[g]. Also ⟨f,g⟩ = ||g||^2 and Σ_i I_i[g] = Σ_{𝒮}|S|f̂(S)^2 ≥ αd||g||^2. ∎

So any Corollary-6.7-type bound with B ≥ 1/(αd) is automatically satisfied and says nothing.

### 2.3 Proposition M (PROVED; exact checks in logs/check_propM_bounds.log)

Setup. n = 2m+1 and k = 2j+1 are odd with 3 ≤ k ≤ n. Let f = (1 − Maj_n)/2 and g = f^{=k}. Suppose

  (∗) ⟨f,g⟩ ≤ A·||f||^{3/4}·||g||^{3/4}·max_{|S|=k}|f̂ĝ|^{1/4} + B·I[f,g] + C·||f||·||g||

holds for this pair, with B ≤ k^{-5/4}·n^{-1/4}/(4√6) and C ≤ k^{-3/4}/14.

Conclusion. A ≥ 2^{-11/8}·(6k^{3/2})^{-5/8}·((n−1)/(k−1))^{(k−1)/4}.

Hence, if (∗) holds for all Boolean f and all k-homogeneous g with B = b·k^{-β} (β > 3/2) and C ≤ k^{-3/4}/14, then log2 A ≥ (β − 3/2)(k−1)·log2 k − O_{b,β}(k). For this, take n the largest odd integer ≤ (4√6·b)^{-4}·k^{4β−5}.

Proof. Write M = |M̂aj(S)| for |S| = k, which equals 4^{-m}·C(2m,m)·C(m,j)/C(2m,2j) (F4 Proposition 6.1; checked against the Walsh transform for n ≤ 17), and W = C(n,k)·M^2. The facts used:
- (B1) C(m,j)^2 ≤ C(2m,2j) ≤ (1 + √(2πj))·C(m,j)^2. Vandermonde's identity gives C(2m,2j) = Σ_t C(m,j+t)C(m,j−t); the ratio of the t-th term to C(m,j)^2 is ∏_{s≤t}[(m−j−s+1)/(m−j+s)]·[(j−s+1)/(j+s)] ≤ e^{-t²/(2j)}; summing and comparing with a Gaussian integral gives the upper bound.
- (B2) 4^{-m}·C(2m,m) ∈ [1/(2√m), 1/√(πm)]. Hence M ≤ 1/(√(πm)·C(m,j)) ≤ (j/m)^j.
- (B3) W = [(2m+1)/k]·[4^{-m}C(2m,m)]^2·C(m,j)^2/C(2m,2j) ≥ 1/(2k(1 + √(π(k−1)))) ≥ 1/(6k^{3/2}).
- (B4) I(Maj_n) = n·4^{-m}·C(2m,m) ≤ √n.

Each term of (∗) for this pair: ⟨f,g⟩ = ||g||^2 = W/4 and ||f||^2 = 1/2; max|f̂ĝ|^{1/4} = (M/2)^{1/2}; I[f,g] = √(I(Maj_n)·kW)/4. By (B3) and (B4), the hypotheses on B and C make each of the last two terms at most W/16. Hence A·2^{-3/8}·(W/4)^{3/8}·(M/2)^{1/2} ≥ W/8, which gives A ≥ 2^{-11/8}·W^{5/8}·M^{-1/2}. Now use (B2) and (B3). ∎

Checks. All of (B1)–(B4) were verified exactly for every odd n ≤ 801 and every odd k ≤ n, and at selected levels for n up to 10^6 + 1. The closed form lies below the exact forced constant: log2 values 17.5 against 51.3 at k = 129, and 1737 against 2111 at k = 1025.

KKLMS's own parameters. B = δ^{1/16}, C = δ, δ ≤ d^{-96000}. Then Proposition M gives A ≥ δ^{-(1/16−o(1))d}.

Forced log2 A/(k log2 k) (logs/majority_shape_test.log, exact majority formulas, best n = k^C over a grid of C):

| g | β | k or d = 9 / 17 | 33 / 65 | 129 / 257 | 513 / 1025 | 2049 |
|---|---|---|---|---|---|---|
| level k | 2 | 0.155 | 0.285 | 0.294 | 0.288 | 0.282 |
| level k | 3 | 1.153 | 1.286 | 1.294 | 1.288 | 1.282 |
| band [d/2, d] (NUMERICAL) | 1.1 | says nothing | says nothing | 0.044 | 0.040 | — |
| band [d/2, d] | 1.25 | 0.036 | 0.097 | 0.098 | 0.093 | — |
| band [d/2, d] | 1.5 | 0.146 | 0.168 | 0.162 | 0.155 | — |
| band [d/2, d] | 2 | 0.410 | 0.422 | 0.413 | 0.406 | — |

For the level-k rows the column headers refer to k = 9, 33, 129, 513, 2049; for the band rows to d = 17, 65, 257, 1025. In KKLMS's regime (β = 6000) the ratio is ≥ 1.78 already with C ≤ 8, and grows with C.

### 2.4 Consequence for any route of KKLMS type

KKLMS's accounting uses I[f,g] ≤ √(2d)·I; for the second term to sum to O(I) against entropy weights ≥ d, it needs β > 5/2, and Proposition M then forces A ≥ d^{(1−o(1))d}, which means a per-element charge of at least about 2·log2 d - the same form as Theorem 1.3. Cauchy–Schwarz over the levels needs only β > 3/2, but the band version (numerical) still forces A ≥ d^{0.15d}. B ≈ 1/d is informative, by Lemma V, only at levels that carry a constant fraction of f's influence. Therefore per-level inequalities with a cross-influence second term cannot remove the log. This holds on monotone functions, threshold functions, symmetric functions, and functions with all influences small, because Maj_n belongs to all of these classes.

## 3. What the log costs on actual functions (NUMERICAL, logs/family_survey.log)

K13 = E_μ log2(|S|+1). Theorem 1.3 reads H ≤ K(1 + K13)·I. Towers and the tails of recursive majority are Monte Carlo estimates.

| function | n | H/I | K13 | μ(λ≥4) | μ(λ≥8) | μ(λ≥12) | μ(λ≥16) |
|---|---|---|---|---|---|---|---|
| majority | 1001 | 2.844 | 8.08 | 0.261 | 0.068 | 0 | 0 |
| majority | 100001 | 2.882 | 14.62 | 0.259 | 0.066 | 0.017 | 0.0047 |
| tribes w = 6 | 264 | 3.922 | 2.58 | 0.230 | 0.017 | 0 | 0 |
| tribes w = 14 | 158984 | 4.000 | 3.59 | 0.325 | 0.0059 | 8.6e-4 | 6.2e-5 |
| recursive majority, depth 4 | 81 | 3.210 | 3.09 | 0.215 | 0.062 | 0 | 0 |
| recursive majority, depth 10 | 59049 | 3.931 | 6.51 | 0.363 | 0.0039 | 0.0012 | 9.9e-4 |
| Numaro g | 18 | 3.323 | 1.82 | 0.241 | 1.1e-3 | 6.7e-5 | 6.7e-5 |
| tower of g, depth 2 | 324 | 4.953 | 2.71 | 0.764 | 0.049 | 1.1e-4 | 3.2e-5 |
| tower of g, depth 4 | 104976 | 6.145 | 4.65 | 0.998 | 0.053 | 0.0052 | 0.0024 |
| bent + flip, m = 18 | 19 | 2.000 | 3.36 | 0.0064 | 1.4e-4 | 7.6e-6 | 7.6e-6 |
| majority 18 + one-point flip | 19 | 2.399 | 2.94 | 0.301 | 2.3e-7 | 5.4e-9 | 5.4e-9 |

K13 grows by about 3.3 per decade of n on majority, by about log2 w on tribes, by log2(3/2) per level on recursive majority, and by about log2 I(g) per level on the towers; H/I stays bounded in every case. On majority the tail is μ(λ ≥ C) ≈ 2^{-C/2}. On the towers λ concentrates near 6.52. Open question (not a conjecture that can be supported in general): is μ(λ ≥ C) ≤ K·2^{-cC} for every Boolean f? FEI needs only a uniformly integrable tail. Multi-scale symmetric functions may give polynomial tails; this was not tested.

## 4. Theorem A (PROVED, as a modification of the last step of KKLMS §7.1)

Statement. For the constants of KKLMS Theorem 1.3 there is K such that, for every Boolean F, every a > 1, and any choice of orderings r_d (one per level):

  H(F) ≤ K·I(F) + Σ_{S≠∅} F̂(S)^2·min{ K|S|·log2(|S|+1), log2 C(n,|S|), |S|·log2(ea/(a−1)) + a·log2(e)·Σ_{i∈S} ln+(r_{|S|}(i)/|S|) }.

Proof.
1. Buckets k ≥ 1 contribute O(I), exactly as in KKLMS.
2. On bucket 0 at level d, call it B_d, with mass P_d: every coefficient there exceeds τ_d = 2^{-2Cd·log(d+1)}·var, so |B_d| ≤ 2^{2Cd·log(d+1)}.
3. Apply Gibbs' inequality against ν_d = (1/3)(uniform on B_d + uniform on level d + π_d), where π_d is F5's rank-weighted measure. By F5 Lemma 6, ln Z_d ≤ d·ln(ea/(a−1)). This gives Σ_{B_d} p·log(1/p) ≤ P_d·log(1/P_d) + P_d·log 3 + Σ_{B_d} p·min(the three charges).
4. Finally, Σ_d P_d·log(1/P_d) ≤ I + var·log(1/var) = O(I), by Gibbs against 2^{-d} and edge isoperimetry. ∎

What it does. On majority the counting charge is the exact conditional entropy (CNT/I = 2.87 at n = 100001), so Theorem A turns KKLMS's K·I·log n into K'·I for majority. The rank charge recovers F5's bound for threshold functions. At n ≤ 20 all charges are within constant factors of H/I (logs/theoremA_charges.log), and the per-level Gibbs check passes on every family. Tribes, recursive majority and the towers need a hierarchical reference measure, which is W2-C's topic; FEI is already known for them by composition.

## 5. What a log-free proof would need

1. Bad sets counted jointly rather than as a product ∏|T_j|, or a degree reduction whose Bonami cost does not scale with the degree of the complement. Proposition H covers every scheme that has both features.
2. A second term that adds up across levels, instead of I[f,g] (Proposition M, Lemma V). The natural target is the global statement Σ_d d·(mass at level d with λ ≥ C) ≤ ψ(C)·I with ∫ψ < ∞, which is FEI itself.
3. F5's mechanism (Littlewood–Offord plus a reference measure, no hypercontractivity) escapes both obstructions. Theorem A is where it plugs into KKLMS.

## 6. Files

Everything is in continuations/2026-09-22-opus-team/W3-04-kklms/. Code: code/fei_core.py (exact Walsh transform and the families; bent-plus-flip uses F4's convention, since flipping a different point multiplies by a character and changes I); code/majority_exact.py (shape test); code/check_propM_bounds.py (exact checks of (B1)–(B4)); code/family_survey.py (Section 3 table); code/theoremA_charges.py (Section 4 check); code/sanity.py (reproduces H and I of Numaro's g, 6.7766053090 and 261/128, maj17, tribes, bent+flip and recursive majority). Logs: logs/*.log. Paper: src/kklms_1911.10579.pdf and its text extractions src/kklms.txt and src/kklms_mu.txt.
