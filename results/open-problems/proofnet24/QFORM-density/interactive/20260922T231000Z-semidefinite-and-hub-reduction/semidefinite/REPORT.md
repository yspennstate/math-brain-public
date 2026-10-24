# Bounded density for semidefinite quadratic forms in independent variables

## 0. Setting and results

X = (X_1,…,X_n) has independent coordinates; X_i has density f_i ≤ 1 and characteristic function ψ_i. For real symmetric A, b ∈ R^n, c ∈ R:

- Q = XᵀAX + bᵀX + c, and φ(t) = E exp(itQ).
- λ_1(A) ≥ λ_2(A) ≥ … are the eigenvalues; |λ|_(k)(A) is the k-th largest modulus.
- For a random variable Z, L_Z(u) = sup_s P(|Z − s| ≤ u) is its concentration function.
- α_1(Z) = sup_{u>0} L_Z(u)/√u and α_2(Z) = sup_{0<u≤1} L_Z(u)/(u(1 + log(1/u))).
- ‖p_Z‖∞ is the supremum of the density.
- A_IJ is the I×J block of A, s_1(M) ≥ s_2(M) ≥ … are singular values, and e_k is the k-th elementary symmetric polynomial.

**Theorem 1.** Let A be positive semidefinite with λ_3(A) ≥ 1. Then ‖p_Q‖∞ ≤ C_0 = 1.71·10⁴ for every b, c and all independent X_i with densities ≤ 1.
- By scaling, ‖p_Q‖∞ ≤ C_0/λ_3(A) whenever λ_3 > 0.
- The same bound holds for negative semidefinite A: apply the theorem to −Q.
- The rank of A, the dimension n and b are arbitrary; b may point outside the range of A.

**Theorem 2.** Let A be PSD and let b, c, X be as above.
- (a) If λ_1(A) ≥ 1, then L_Q(u) ≤ 45.26 √u for all u > 0.
- (b) If λ_2(A) ≥ 1, then L_Q(u) ≤ 4435 u(1 + log(1/u)) for 0 < u ≤ 1.

**Proposition 3 (decoupling certificate).** Let k ∈ {1,2,3} and let A be PSD with λ_k(A) > 0 and
max_i a_ii ≤ λ_k(A)/γ_k, where γ_1 = 128, γ_2 = 300, γ_3 = 640.
Then some partition [n] = I ∪ J satisfies:
- s_k(A_IJ) ≥ λ_k/4;
- every k-volume marginal of A_IJ on I is at most 64k·max a_ii/λ_k ≤ 1/2.

Consequently, uniformly in b, c, X:
- k = 1: |φ(t)| ≤ 2e^{1/4}(2π)^{1/2}(λ_1|t|)^{-1/2};
- k = 2: |φ(t)| ≤ 8πe^{1/2}(λ_2|t|)^{-1};
- k = 3: ‖p_Q‖∞ ≤ 24√e/λ_3.

**Theorem 4 (indefinite, small |A|-diagonal).** Write |A| = (A²)^{1/2}; its diagonal (|A|)_ii = Σ_m |λ_m| u_m(i)² is at least |a_ii|. Suppose k ∈ {1,2,3} and
max_i (|A|)_ii ≤ |λ|_(k)(A)/γ′_k, where γ′_1 = 130, γ′_2 = 360, γ′_3 = 680.
Then some partition has s_k(A_IJ) ≥ 0.2875|λ|_(k) and all k-volume marginals on I at most 1/2. Hence
- |φ(t)| ≤ e^{k/4}(2π)^{k/2}(0.2875|λ|_(k))^{-k/2}|t|^{-k/2};
- for k = 3, ‖p_Q‖∞ ≤ 34.4/|λ|_(3).

**Corollary 5.** Call a coordinate i *hub-like at level k* for M if (|M|)_ii > |λ|_(k)(M)/γ′_k.
- The conjecture is equivalent to the three no-pivot statements of the reduction theorem (§1.4), restricted to matrices with no c-pivot that have a hub-like coordinate at the relevant level.
- At a hub-like i with |m_ii| < c, both the positive and the negative part of |M|^{1/2} carry weight at least ((|M|)_ii − c)/2.
- The i-th row of M has norm at least (|M|)_ii.

**Corollary 6.** Semidefinite rank-three forms have density at most C_0/λ_3, with any linear terms. Combined with the one-sheet bound π√2 for indefinite rank-three forms, the rank-three case is open only for indefinite forms on the side where the level sets are two-sheet hyperboloids.

## 1. Tools

**1.1 Conditioning and one coordinate.**
- Conditioning on any set of coordinates is lossless.
- If a_ii = a > 0, then Q = a(X_i − m(X_{-i}))² + R(X_{-i}), with m affine and R quadratic with matrix A/a_ii.
- Given X_{-i}, the variable a(X_i − m)² has density (f_i(m+r) + f_i(m−r))/(2√(aw)) ≤ (aw)^{-1/2} at w > 0, where r = √(w/a).
- Hence
  (1.1) p_Q(y) ≤ a^{-1/2} E|y − R(X_{-i})|^{-1/2}.
  This is a square-root profile with constant K = a^{-1/2} around the random centre ξ = R.

**Schur complements.** If A is PSD with λ_k(A) ≥ 1 and a_ii > 0, then A/a_ii is PSD and λ_{k-1}(A/a_ii) ≥ 1.
- Positivity: yᵀ(A/a_ii)y = min_x (x,y)ᵀA(x,y) ≥ 0.
- For invertible A, (A/a_ii)^{-1} = (A^{-1})_{-i,-i}. The eigenvalues ν_j of A^{-1} satisfy ν_j ≤ 1 for j ≥ n−k+1. By interlacing, the eigenvalues μ_j of the submatrix satisfy 0 < μ_j ≤ ν_j ≤ 1 for the k−1 indices j = n−k+1,…,n−1.
- For singular A, apply this to A + εI and use continuity.

**1.2 Theorem D_k (decoupling with volume sampling; RESULTS Theorem D for k = 3, FOURIER §1.2 with q = 1).**
Let I, J be disjoint, M = A_IJ and Z_k = e_k(MᵀM) = Σ_{|S|=|T|=k} det(M_ST)². Put w_ST = det(M_ST)²/Z_k, α_i = P_w(i ∈ S) and β_j = P_w(j ∈ T).
If α_i ≤ 1/2 for all i ∈ I, then for all b, c, X:
|φ(t)|² ≤ e^{k/2}(2π)^k |t|^{-k} Z_k^{-1/2},
and for k = 3, ‖p_Q‖∞ ≤ 6√e Z_3^{-1/6}.

*Proof.*
1. *Decoupling.* Condition on the coordinates outside I ∪ J. Apply Cauchy–Schwarz in X_I and introduce an independent copy X′_J. This gives
   |φ|² ≤ E_W Π_{i∈I} |ψ_i(2t(MW)_i)|, where W = X_J − X′_J.
   The W_j are independent with densities f_j * f_j(−·) ≤ 1. The blocks A_II, A_JJ and all linear terms drop out.
2. *Brascamp–Lieb.* Use exponents α_i on w ↦ ⟨m_i, w⟩ and 1 − β_j on w ↦ w_j; they sum to |J|. By Lieb's theorem the constant is
   sup_{d>0} (Π d_i^{α_i} Π d_j^{1−β_j} / det(D_J + MᵀD_IM))^{1/2},
   with D_I = diag(α_i d_i) and D_J = diag((1−β_j)d_j).
3. *Determinant.* By the diagonal-plus-PSD expansion and Cauchy–Binet,
   det(D_J + MᵀD_IM) = Σ_{S,T} det(M_ST)² Π_{i∈S} α_i d_i Π_{j∉T}(1−β_j)d_j.
   Weighted AM–GM with weights w_ST gives det ≥ Z_k Π(α_i d_i)^{α_i} Π((1−β_j)d_j)^{1−β_j}. All d's cancel, so the constant is at most Z_k^{-1/2} Π α_i^{-α_i/2} Π(1−β_j)^{-(1−β_j)/2}.
4. *L^p bounds.* For p ≥ 2, ∫|ψ|^p ≤ 4π/√p (Rogozin and Ball; RESULTS Lemma 1). This gives ‖|ψ_i(2t·)|‖_{1/α_i} ≤ ((2|t|)^{-1}4π α_i^{1/2})^{α_i}. The factors α_i^{α_i/2} cancel, and Π(1−β)^{-(1−β)/2} ≤ e^{k/2}.
5. *Density for k = 3.* ‖p_Q‖ ≤ (2π)^{-1}∫min(1, B|t|^{-3/2}) = (3/π)B^{2/3}, with B = (2π)^{3/2}e^{3/4}Z_3^{-1/4}. ∎

**1.3 Lemma 1.1 (Fejér kernel).**
L_Z(u) ≤ (u/(2 sin²1)) ∫_{|t|≤2/u} |φ_Z| ≤ 0.70615 u ∫_{|t|≤2/u} |φ_Z|.

*Proof.* The kernel (sin x/x)² is at least sin²1 on [−1,1], and its Fourier transform is π(1 − |τ|/2)_+. ∎

Consequences:
- If |φ_Z| ≤ B|t|^{-1/2}, then α_1 ≤ 3.9946 B.
- If |φ_Z| ≤ min(1, B/|t|) with B ≥ 2, then α_2 ≤ 1.4123 B.

**1.4 Lemma 1.2 (compositions; GEOM §3.1).** Suppose p_Q(y) ≤ K E|y − ξ|^{-1/2}.
- **(C5)** α_1(Q) ≤ 4K.
- **(C2)** If α_1(ξ) ≤ K′, then α_2(Q) ≤ 4√2 K max(K′, 1).
  This uses ∫_{−u}^{u}|y + d|^{-1/2} dy ≤ 4√2 u max(|d|, u)^{-1/2} and a layer-cake bound.
- **(C1)** If α_2(ξ) ≤ K′ with K′ ≥ 1, then ‖p_Q‖ ≤ 3K(K′(3 + log K′))^{1/2}.
  This uses sup_s E|s − ξ|^{-1/2} ≤ V + K′(3 + 2 log V)/V with V = (K′(3 + log K′))^{1/2}.

**Reduction (GEOM Theorems 5.1–5.2).** The conjecture is equivalent to the following bounds, uniform in linear terms, for matrices with no c-pivot:
- α_1 ≤ H_1 when |λ|_(1) ≥ 1;
- α_2 ≤ H_2 (or its integrability form) when |λ|_(2) ≥ 1;
- ‖p‖ ≤ H_3 when |λ|_(3) ≥ 1.

For PSD matrices only 1×1 pivots matter: m_ii < c forces every 2×2 principal minor into [0, c²).

## 2. The Gram picture and the partition identity

Let A be PSD of rank r and set B = UΛ^{1/2} (an n×r matrix). Then
- A = BBᵀ and BᵀB = Λ = diag(λ_m);
- the rows b_i of B satisfy |b_i|² = a_ii.

Rows of A may be huge, since (A²)_ii ≤ λ_1 a_ii, but the rows of B are controlled by the diagonal alone. This is the only use of semidefiniteness.

Take independent uniform signs ε_i and set I = {ε = +1}, J = {ε = −1}. Define
- N = (1/2)Σ_i ε_i b_i b_iᵀ;
- H_I = Λ/2 + N and H_J = Λ/2 − N, so that H_I + H_J = Λ;
- then A_IJ = B_I B_Jᵀ.

**Lemma 2.1.** For every g:
- ⟨B_I g, A_IJ B_J g⟩ = |Λg|²/4 − |Ng|²;
- (gᵀH_Ig)(gᵀH_Jg) ≤ (gᵀΛg/2)².

*Proof.* The left side is gᵀH_IH_Jg. The cross terms (1/2)(gᵀNΛg − gᵀΛNg) cancel, since both equal (Λg)·(Ng). The second claim is AM–GM. ∎

**Lemma 2.2.** Let K be a set of k indices with λ_m ≥ θ on K, and put S_K = Σ_{m∈K} |Ne_m|²/λ_m².
- If S_K ≤ 1/8, then s_k(A_IJ) ≥ θ/4.
- If max a_ii ≤ c, then E S_K ≤ kc/(4θ), so P(S_K > 1/8) ≤ 2kc/θ.

*Proof.*
1. For g in G = span{e_m : m ∈ K}, Cauchy–Schwarz gives |Ng| ≤ |Λg| S_K^{1/2}. Lemma 2.1 then gives ⟨B_I g, A_IJ B_J g⟩ ≥ |Λg|²/8 > 0, so B_J is injective on G.
2. For x = B_J g, |A_IJ x|/|x| ≥ (|Λg|²/8)/(gᵀΛg/2) ≥ θ/4. Courant–Fischer gives s_k(A_IJ) ≥ θ/4.
3. For the expectation, E|Ne_m|² = (1/4)Σ_i b_i(m)²|b_i|² ≤ (c/4)λ_m. Then apply Markov's inequality. ∎

No other eigenvalue enters, and there is no dimension factor.

## 3. Marginals are ridge leverages

Let M be a matrix, σ_m the eigenvalues of G = MMᵀ with orthonormal eigenvectors u_m, and k ≤ rank M. Then
α_i = Σ_m p_m u_m(i)², where p_m = σ_m e_{k-1}(σ_{-m})/e_k(σ).

**Lemma 3.1.** For every m, p_m ≤ min(1, kσ_m/σ_k). Hence, for every 0 < κ ≤ σ_k/k,
α_i ≤ 2 m_iᵀ(MᵀM + κ)^{-1} m_i, where m_i is the i-th row of M.

*Proof.*
1. p_m ≤ 1 because e_k(σ) = σ_m e_{k-1}(σ_{-m}) + e_k(σ_{-m}).
2. For μ ≥ 0, e_k(μ) ≥ (μ_(k)/k) e_{k-1}(μ): add to each (k−1)-set a top-k index outside it; each k-set is hit at most k times. This gives p_m ≤ kσ_m/σ_k when m is not among the top k.
3. min(1, x) ≤ 2x/(1 + x); then apply push-through. ∎

**Lemma 3.2.** For M = A_IJ and i ∈ I,
m_iᵀ(MᵀM + κ)^{-1}m_i = b_iᵀH_J(H_IH_J + κ)^{-1}b_i ≤ b_iᵀ(H_I + κΛ^{-1})^{-1}b_i.

*Proof.* First, (B_JH_IB_Jᵀ + κ)B_J = B_J(H_IH_J + κ), which gives the equality. Then use H_J ≤ Λ, hence H_J^{-1} ≥ Λ^{-1}. For singular H_J, argue by continuity. ∎

## 4. Proof of Proposition 3

Let K_b be the top k indices and K_s the rest, so λ_m ≤ λ_k on K_s. Put
- κ = λ_k²/(16k) and ρ = κ/λ_k = λ_k/(16k);
- l_i = |Λ_b^{-1/2} b_i^b|², which satisfies l_i ≤ a_ii/λ_k and Σ_i l_i = k.

Consider three events:
- (S): S_{K_b} ≤ 1/8;
- (E1): ‖Λ_b^{-1/2}N_bbΛ_b^{-1/2}‖_F² ≤ 1/64;
- (E2): (2/ρ)‖N_sbΛ_b^{-1/2}‖_F² ≤ 1/8.

**Lemma 4.1.** [[P, R], [Rᵀ, T]] ≥ [[P − 2RT^{-1}Rᵀ, 0], [0, T/2]] for T > 0.
The quadratic form of the difference is 2|T^{-1/2}Rᵀx + T^{1/2}y/2|².

The argument runs in four steps.
1. *Singular value.* Under (S), s_k ≥ λ_k/4. So κ ≤ s_k²/k, and α_i ≤ 2b_iᵀ(H_I + κΛ^{-1})^{-1}b_i.
2. *Lower bound.* Since κΛ^{-1} ≥ 0 ⊕ ρI_s and (H_I)_bs = N_bs, Lemma 4.1 gives
   H_I + κΛ^{-1} ≥ [Λ_b/2 + N_bb − (2/ρ)N_bsN_sb] ⊕ (ρ/2)I_s ≥ Λ_b/4 ⊕ (ρ/2)I_s
   under (E1) and (E2).
3. *Marginals.* α_i ≤ 8l_i + (4/ρ)|b_i^s|² ≤ 64k a_ii/λ_k ≤ 64k/γ_k ≤ 1/2.
4. *Probabilities.* The failure probabilities are:
   - P(not S) ≤ 2kc/λ_k;
   - P(not E1) ≤ 64·(1/4)Σ l_i² ≤ 16kc/λ_k;
   - P(not E2) ≤ 8·(2/ρ)(ck/4) = 64k²c/λ_k.

   The total, (18k + 64k²)c/λ_k, is at most 0.641, 0.973 and 0.984 for k = 1, 2, 3.

Hence a good partition exists. For it, Z_k ≥ (λ_k/4)^{2k}, and Theorem D_k gives the stated bounds. ∎

The small block may be of any dimension, with eigenvalues up to λ_k. It enters only through the ridge ρ, so no separate high-rank case is needed.

## 5. Proof of Theorems 1 and 2

Use pivot thresholds c_1 = 1/128, c_2 = 1/300 and c_3 = 1/640.

**Level 1** (λ_1 ≥ 1).
- If some a_ii ≥ c_1: (1.1) and (C5) give α_1 ≤ 4c_1^{-1/2} = 45.26.
- Otherwise Proposition 3 gives B_1 = 6.437, and Lemma 1.1 gives α_1 ≤ 25.71.
- So α_1 ≤ 45.26. This is Theorem 2(a).

**Level 2** (λ_2 ≥ 1).
- If some a_ii ≥ c_2: the centre has a PSD matrix with λ_1 ≥ 1, so α_1(ξ) ≤ 45.26 by level 1. Then (C2) gives α_2 ≤ 4√2 c_2^{-1/2}·45.26 = 4434.05.
- Otherwise B_2 = 8πe^{1/2} = 41.44, and α_2 ≤ 58.52.
- This is Theorem 2(b).

**Level 3** (λ_3 ≥ 1).
- If some a_ii ≥ c_3: level 2 applies to the centre, and (C1) gives ‖p_Q‖ ≤ 3c_3^{-1/2}(4434.05·(3 + log 4434.05))^{1/2} = 17061.
- Otherwise ‖p_Q‖ ≤ 24√e = 39.6.
- This is Theorem 1. ∎

**Which step uses which result:**
- profiles and Schur complements: §1.1;
- leaves: Lemmas 2.1–2.2, 3.1–3.2 and 4.1, the second-moment events, and Theorem D_k with q = 1;
- Fourier decay to concentration: Lemma 1.1;
- the tree: (C5), (C2), (C1).

No 2×2 pivots, hub propositions or Fresnel linearisation are used.

The rank-two PSD case with linear terms outside the range (GEOM §4) is level 2 here.

## 6. Proof of Theorem 4 and Corollary 5

Write A = BSBᵀ with B = U|Λ|^{1/2} and S = sign(Λ). Then |b_i|² = (|A|)_ii =: d_i, H_I = |Λ|/2 + N, and A_IJ = B_I S B_Jᵀ. Split g = g_+ + g_- by sign.

**Lemma 6.1.**
- (a) ⟨B_I Sg, A_IJ B_J g⟩ = |Λg|²/4 − (g_-ᵀ|Λ|Ng_+ + g_+ᵀ|Λ|Ng_-) − (SNSg)·(Ng).
- (b) |B_I Sg|² + |B_J g|² = gᵀ|Λ|g − 4g_+ᵀNg_-.

*Proof.* Use SH_IS = |Λ|/2 + SNS, S commuting with |Λ|, and Sg = g_+ − g_-. ∎

**Lemma 6.2.** Let K be a set of k indices with |λ| ≥ θ on K, and put Ñ = |Λ_K|^{-1/2}N_KK|Λ_K|^{-1/2}. Suppose
- (S1) Σ_K |Ne_m|²/λ_m² ≤ η², and
- (S2) ‖Ñ‖ ≤ η′.

Then s_k ≥ θ(1/4 − η − 2η²)/(1/2 + η′).

*Proof.*
1. In 6.1(a), the cross terms are at most η|Λg|² and the last term is at most 2η²|Λg|².
2. In 6.1(b), |4g_+ᵀNg_-| ≤ 2η′gᵀ|Λ|g.
3. Apply Courant–Fischer with the test vectors B_I Sg. ∎

The expectations are as before: both are at most kc/(4θ).

**Proof of Theorem 4.** Take K to be the top k indices by modulus, η = 1/16 and η′ = 1/8. Then τ = s_k lower bound = 0.2875θ.
- Lemma 3.2 carries over through (Sb_i)ᵀ(SH_IS + κ|Λ|^{-1})^{-1}(Sb_i) = b_iᵀ(H_I + κ|Λ|^{-1})^{-1}b_i.
- With κ = τ²/k, the ridge on the rest is ρ = 0.08266θ/k.
- Step 2 of §4, with (E2), gives α_i ≤ 48.39k d_i/θ.
- The failure probability is (80k + 48.39k²)c/θ < 1 at the stated γ′_k. ∎

**Proof of Corollary 5.** Without a hub-like coordinate, Theorem 4 and Lemma 1.1 give α_1 ≤ 23.98, α_2 ≤ 50.89 and ‖p‖ ≤ 34.41. These are the leaf hypotheses of GEOM 5.1; GEOM 5.2 gives the equivalence. For a hub-like coordinate:
- d_i ± m_ii = 2|b_i^±|²;
- (M²)_ii ≥ d_i² by Cauchy–Schwarz. ∎

**Remarks.**
- A PSD row can be huge without being hub-like.
- The star 2X_h⟨w, X⟩ has (|M|)_hh = 1, so it is hub-like, and decoupling loses half of its decay.
- Hubs coupled to general remainders are hub-like. Every other no-pivot configuration is covered by Theorem 4.

## 7. Numerical checks (numpy/scipy)

- The identities of Lemmas 2.1 and 6.1 hold to 10⁻¹³ and 10⁻¹⁶.
- The marginal formula agrees with brute-force enumeration of all k×k minors to 10⁻¹¹.
- Lemmas 3.1, 3.2, 6.2 and the |Λ| version are never violated in 57 + 72 cases.
- Negative controls fail as they should: the identity without |Ng|² fails in 72/72 cases, the factor-2-free Lemma 3.1 in 177/216, p_m ≤ σ_m/σ_k in 60/216, θ/1.2 in place of θ/4 in 84/84, and Λ/4 in the monotonicity in 207/216.
- The variant κ = σ_k survives random tests but fails on a targeted example (α = 0.2126 > 0.1651). There the proved bound holds (0.4252), and α = 3ε²/(1 + 3ε²).
- Chain check at n = 1024 with flat eigenvectors: whenever S, E1, E2 held, the conclusions held, and the means match the exact second-moment formulas.
- Density peaks of PSD forms with λ_3 = 1 are at most 2.83; the Gaussian value is about 2.90. The cases tested: a heavy coordinate plus a linear term outside the range, eigenvalues (50,1,1), and X_1² plus a spread rank-two part; uniform and spread laws.
- All constants were recomputed independently.

## 8. What remains

The open part is Corollary 5's class: no-pivot matrices with a hub-like coordinate. The proposed next step is to put the hub-like set on the J side and integrate it against its densities (each hub then gains a full |t|^{-1}). The quantity to control for the light rows is λ_min(|Λ_K|^{-1/2} Σ_{i∉H*} b_i^K b_i^{Kᵀ} |Λ_K|^{-1/2}).
