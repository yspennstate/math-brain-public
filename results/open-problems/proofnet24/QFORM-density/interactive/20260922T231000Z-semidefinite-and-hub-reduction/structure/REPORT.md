## Summary

**Status by part**
- **(i) Exact version, PROVED:** f(1) = 2, and 2r ≤ f(r) ≤ 3r in general. f(r) = 2r is still a conjecture; it holds in the two extreme cases we checked.
- **(ii) Robust version, PROVED in Frobenius form:** the exact skeleton identity below gives A = D + R + E with rank R ≤ 4r and ||E||_F ≤ 3(r+1)√κ. The version with only s_{r+1}(A_IJ) ≤ δ and constants free of n is open.
- **(iii) Marginals, PROVED:** α_i ≤ k‖m_i‖²/T_k, and a heavy marginal forces a hub or a pivot. Theorem S also holds: small rows imply Theorem D.
- **(iv) Decomposition, PROVED as a dichotomy:** either Theorem D applies with a universal constant, or the input of Theorem H holds up to a small Frobenius twist. That twisted Theorem H is open, as is the scale caveat in §5.6(4).

**Key new ideas**
1. For a random partition, U^T diag(ξ) R diag(1−ξ) U = −¼ U^T D_ε R D_ε U exactly, because RU = 0. The feared cancellation therefore has a mean that sees only diag(R), plus a Rademacher chaos of variance at most 6η⁴.
2. Volume-sampled skeletons (S,T) satisfy E_w Σ_{l≠m}(A−P)²_lm = (r+1)² V_{r+1}/V_r exactly.
3. Force the hub rows into J. The light rows then have marginals at most 3η²/T_3, so the averaging over random partitions works.
4. Theorem H ignores the hub block and the hub diagonal. After the decomposition, the only non-exact feature is a twist E on the light block with ‖E‖_F ≤ 36√τ₀.

**Most useful next step.** Prove (TH-ε), Theorem H with that twist, in its simplest case: one hub with any diagonal, one spread rank-one direction with |λ| ≥ 1, and a zero-diagonal twist of small Frobenius norm. The canonical case "star + rank one + eps W" with small eps·√n is exactly this.

---

# The structure lemma for matrices without pivots

Setting: X_1, ..., X_n independent with densities at most 1, Q = X^T A X + b^T X + c, A real symmetric. All density and small-ball bounds are uniform in b and c.

## 0. Results

| # | Statement | Status |
|---|---|---|
| 2.1 | All off-diagonal 2×2 minors vanish ⇒ A = D + R, rank R ≤ 2; a star attains 2. So f(1) = 2. | PROVED |
| 2.2 | All off-diagonal (r+1)-minors vanish ⇒ rank R ≤ 3r. Disjoint stars need 2r. So 2r ≤ f(r) ≤ 3r. | PROVED |
| 2.3 | f(r) = 2r (true in the two extreme cases of Remark 2.4). | CONJECTURAL |
| 3.1 | Volume-sampled skeleton identity: the mean squared off-diagonal Schur remainder equals (r+1)² V_{r+1}/V_r exactly. | PROVED |
| 3.2 | V_{r+1} ≤ κV_r ⇒ A = D + R + E, rank R ≤ 4r, E zero-diagonal and supported off 2r rows and columns, ‖E‖_F ≤ 3(r+1)√κ. If T_{r+1}(A_IJ) ≤ δ² for every partition, then every off-diagonal block of E has norm ≤ 6(r+1)δ. | PROVED |
| 3.3 | The same with only s_{r+1}(A_IJ) ≤ δ, constants free of n. | OPEN |
| 4.1–4.3 | Marginal identities; T_k e_{k−1}/k ≤ e_k ≤ T_k e_{k−1}; α_i ≤ k‖m_i‖²/T_k. | PROVED |
| 4.4 | α_i > h forces a row with ‖A_{iJ}‖² > hT_3/3: a hub or a pivot. | PROVED |
| 4.5 | **Theorem S.** ≥ 3 eigenvalues of modulus ≥ 1 and all rows ≤ 1/20 ⇒ with probability ≥ 1/2 a random partition has s_3 ≥ 0.26 and all I-marginals ≤ 0.11; density ≤ 38. No pivot hypothesis is needed. | PROVED |
| 5.1 | **Dichotomy** with hub rows H = {rows ≥ η} and τ₀ ≥ 12η²: either a partition with H ⊂ J has T_3 ≥ τ₀ (Theorem D, density ≤ 13.4 τ₀^{−1/2}); or the light rows agree with one rank-2 matrix up to Frobenius² 144τ₀, off four columns and the diagonal. Levels 1, 2 analogous. | PROVED |
| 5.2 | In the second case the light block is D + (rank ≤ 2) + E with ‖E‖_F < 36√τ₀: Theorem H's input except for E. | PROVED |
| 5.3 | Any number of hubs, A_HH = 0, σ₂(A_{H,L}) > 0: density ≤ 2√π (σ₁σ₂)^{−1/2}, whatever the rest. | PROVED |
| 5.4 | One hub direction, A_HH = 0: P(\|Q−s\| ≤ u) ≤ (4u/σ₁)(1 + log₊(σ₁/(4u))). | PROVED |
| 5.5 | The no-pivot regime reduces to Theorem H plus a small Frobenius twist (TH-ε), plus eigenvalue bookkeeping and a scale caveat. | reduction PROVED; (TH-ε) OPEN |

## 1. Notation and standing facts

For a matrix M with singular values s_1 ≥ s_2 ≥ …, write x_j = s_j², e_k = e_k(M^T M), and T_k(M) := Σ_{j≥k} s_j², the mass beyond the best rank-(k−1) approximation.

For a symmetric A:
- ρ(A) := max over disjoint S, T of rank A_ST.
- mr(A) := min over diagonal D of rank(A − D).
- V_k(A) := Σ det(A_ST)² over ordered pairs of disjoint k-sets, with V_0 = 1.

For a uniformly random partition, P(S ⊂ I, T ⊂ J) = 4^{−k}. By Cauchy–Binet, e_k(A_IJ^T A_IJ) = Σ_{S⊂I, T⊂J} det(A_ST)². So E e_k = 4^{−k} V_k.

Cited facts:
- One- and two-dimensional marginals of product densities ≤ 1 have densities ≤ √2 and ≤ 2 (Ball; Livshyts–Paouris–Pivovarov).
- Theorem D / D_k (k = 1, 2, 3): if every volume-sampling I-marginal of A_IJ is ≤ 1/2, then |φ(t)| ≤ B_k|t|^{−k/2} Z^{−1/4} with Z = e_k. For k = 3 this gives ‖p_Q‖ ≤ 6√e Z^{−1/6}. For k = 1, 2 it gives the level-1 and level-2 small-ball statements via Esseen.

## 2. The exact structure lemma

**Theorem 2.1.** If every off-diagonal 2×2 minor of A vanishes, then mr(A) ≤ 2. A star e_h w^T + w e_h^T (w_h = 0, at least two nonzero w_j) has ρ = 1 and mr = 2.

*Proof.* Let G be the support graph of the off-diagonal entries. The hypothesis says a_ik a_jl = a_il a_jk for all distinct i, j, k, l.

(a) Disjoint edges ik, jl span a K_4. The minor on rows {i,j}, columns {k,l} gives a_il a_jk = a_ik a_jl ≠ 0. The minor on rows {i,l}, columns {k,j} gives a_ij a_lk = a_ik a_lj ≠ 0.

(b) If Q spans a complete subgraph with |Q| ≥ 3 and p ∉ Q is adjacent to some q ∈ Q, then for distinct q′, q″ ∈ Q − q the edges pq and q′q″ are disjoint. By (a), p is adjacent to q′ and q″, hence to all of Q.

(c) Suppose G has two disjoint edges. By (a) and (b) their component is a complete graph K_m with m ≥ 4. Any other edge is disjoint from an edge of that component, so by (a) it lies inside it. So G is K_m plus isolated vertices.
- On Q = V(K_m) put c_i = a_ij a_ik / a_jk.
- Changing k to l multiplies c_i by a_il a_jk/(a_jl a_ik) = 1, so c_i is independent of (j,k).
- c_i c_j = a_ij² > 0, so all c_i share one sign σ; put u_i = |c_i|^{1/2}.
- The signs satisfy s_ij s_ik s_jk = σ. Fix q₀, put ε_i = σ s_{iq₀} (ε_{q₀} = 1); then s_ij = σ ε_i ε_j.
- Hence a_ij = σ v_i v_j with v_i = ε_i u_i, and mr ≤ 1.

(d) Otherwise the edges pairwise intersect, so they form a star or a triangle. A star gives A − diag A = e_h w^T + w e_h^T, of rank 2. A triangle is a 3×3 block B, and B − λ_min(B) I is singular.

Lower bound: if a star's off-diagonal part were that of σuu^T, then u_h u_{l1} ≠ 0 and u_h u_{l2} ≠ 0 would force a_{l1l2} ≠ 0. ∎

**Theorem 2.2.** mr(A) ≤ 3ρ(A). Moreover f(r) ≥ 2r.

*Proof.* Lower bound: ρ and mr are additive over direct sums, so r disjoint stars give ρ = r and mr = 2r.

Upper bound. Let s = ρ(A). Choose disjoint s-sets S, T with A_ST invertible; put C = A_ST^{−1}, K = S ∪ T, L = the rest. For l ∈ L put y_l = A_{l,S}^T, x_l = A_{l,T}^T, n_l = (y_l, x_l).

(i) For l ≠ m in L, the vanishing (s+1)-minor on (S+l, T+m) gives det(A_ST)(a_lm − x_l^T C y_m) = 0. So off-diag(A_LL) = off-diag(P) with P = XCY^T.

(ii) By symmetry a_lm = x_m^T C y_l. So the nondegenerate skew form ω(n, n′) = x^T C y′ − x′^T C y vanishes on all pairs n_l, n_m. The span U of the n_l is isotropic, so dim U ≤ s, i.e. rank N ≤ s with N = [Y, X].

(iii) P − P^T is skew with zero off-diagonal part, so P is symmetric. Let D vanish on K and equal diag(A_LL) − diag(P) on L. Row l of A − D is (y_l, x_l, x_l^T C Y^T), a linear image of n_l. These rows span at most s dimensions, and the K-rows add at most 2s. ∎

**Remark 2.4 (evidence for f(r) = 2r).** Write N = Z W^T with W (2s × p) a basis of U. Then A − D = diag(I, Z) G diag(I, Z^T), where G = [[A_KK − D_K, W], [W^T, E]] and E = W_x^T C W_y.

Assume L contains two disjoint sets on each of which Z has rank p. Then the remaining minor conditions say: every off-diagonal block of G has rank ≤ s, with the last p indices usable on both sides.
- If p = s and E is invertible, the Schur complement makes A_KK − W E^{−1} W^T diagonal, so mr = s.
- If p = s and E = 0, then rank W_{K1} + rank W_{K2} = s for every partition of K. So the nonzero rows of W are independent: there are exactly s hubs R. Elimination shows A_{K−R,K−R} is diagonal, and then mr ≤ 2s.

The intermediate cases are not settled.

## 3. The robust structure lemma

**Theorem 3.1 (skeleton identity).** For disjoint r-sets S, T with det A_ST ≠ 0, let P^{ST} = A_{·,T} A_ST^{−1} A_{S,·}. Then

Σ_{(S,T)} (det A_ST² / V_r) · Σ_{l,m ∉ S∪T, l≠m} (A − P^{ST})_lm² = (r+1)² V_{r+1}/V_r.

The same holds with S restricted to a row set L (and V replaced by V^L).

*Proof.* det A_{S+l,T+m} = det(A_ST)(A − P)_lm. The map (S, T, l, m) ↦ (S+l, T+m, marked l, marked m) is a bijection onto disjoint (r+1)-pairs with one marked element on each side, and each such pair carries (r+1)² markings. ∎

**Corollary 3.2.** Suppose V_{r+1} ≤ κV_r. Then there are disjoint r-sets S, T such that, with L = [n] − (S ∪ T),

A = D + R + E, rank R ≤ 4r, E supported on L × L with zero diagonal, ‖E‖_F ≤ 3(r+1)√κ.

If T_{r+1}(A_IJ) ≤ δ² for every partition, then κ = 4δ², and every off-diagonal block of E has norm ≤ ‖E‖_F ≤ 6(r+1)δ.

*Proof.*
- Some skeleton has F := offdiag(A_LL − P) with ‖F‖_F² ≤ (r+1)²κ.
- The column spaces of P, P^T and P_sym lie in col(N), since P = X(CY^T) and P^T = Y(C^TX^T).
- P − P^T = F^T − F, so ‖P_sym − P‖_F ≤ ‖F‖_F.
- Let P_r be the rank-r eigen-truncation of P_sym. Since P has rank ≤ r, ‖P_sym − P_r‖_F ≤ ‖F‖_F.
- Put R = [[A_KK, A_KL], [A_LK, P_r]]. Its rows in L span col(N), of dimension ≤ 2r, so rank R ≤ 4r.
- E = F + offdiag(P − P_r), so ‖E‖_F ≤ 3‖F‖_F.
- For the partition form: e_{r+1} ≤ T_{r+1} e_r ≤ δ² e_r for every partition (Lemma 4.2); averaging gives V_{r+1} ≤ 4δ²V_r. ∎

**Remark 3.3.** With only s_{r+1} ≤ δ one gets T_{r+1} ≤ nδ², hence ‖E‖_F ≤ 6(r+1)√n δ. A maximal-volume skeleton controls the remainder entrywise by (r+1)δ, but its operator norm only up to a factor of order √(r|L_1|). A dimension-free operator-norm version is open.

## 4. Volume-sampling marginals

**Lemma 4.1.** Let G = MM^T and let m_i be the rows of M.
- (a) 1 − α_i^{(k)} = e_k(G_{−i,−i}) / e_k(G).
- (b) α_i e_k(G) = Σ_{S′ ⊂ I−i, |S′| = k−1} det G_{S′S′} · dist²(m_i, span m_{S′}) ≤ ‖m_i‖² e_{k−1}(G).
- (c) α_i = Σ_m p_m u_m(i)².

*Proof.* By Cauchy–Binet, Σ_T det(M_ST)² = det G_SS. Then apply Gram–Schmidt for S = S′ + i. ∎

**Lemma 4.2.** (1/k) T_k e_{k−1} ≤ e_k ≤ T_k e_{k−1}. Hence e_k ≥ T_k T_{k−1} ⋯ T_1 / k! ≥ T_k^k / k!.

*Proof.* e_k = (1/k) Σ_{|B|=k−1} Π_B x · Σ_{j∉B} x_j, and Σ_{j∉B} x_j ≥ T_k. For the upper bound, A ↦ (A − max A, max A) is injective and max A ≥ k. ∎

**Proposition 4.3.** α_i^{(k)} ≤ k‖m_i‖² / T_k(M). This is sharper than using s_k²: dense noise makes T_k large.

**Corollary 4.4.** Let M = A_IJ with A symmetric. If α_i > h, then:
- ‖A_{iJ}‖² > hT_3/3, and removing row i destroys more than a fraction h of the 3-volume.
- If |a_ii| < c, then either some |a_ij|² ≥ 2c, giving a 2×2 pivot with |det| ≥ 2c − c² ≥ c; or row i has more than hT_3/(6c) entries of modulus < √(2c), i.e. it is a hub.
- At most ⌊3/h⌋ indices have α_i > h.

**Theorem 4.5 (Theorem S).** Let A have at least three eigenvalues of modulus ≥ 1 and all rows ‖Ae_i‖ ≤ η ≤ 1/20. Then with probability ≥ 1/2 a random partition has s_3(A_IJ) ≥ 0.26 and α_i ≤ 0.11 for all i ∈ I. Hence ‖p_Q‖ ≤ 6√e/0.26 ≤ 38. With one or two large eigenvalues the same holds for s_1, s_2, giving the level-1 and level-2 statements. No pivot hypothesis is needed, since |a_ii| ≤ η.

*Proof.* Let AU = UΛ with U orthonormal and |λ_k| ≥ 1. Put u(i) = U^T e_i, l_i = |u(i)|², R = A − UΛU^T (so RU = 0 and U^T R = 0).

Row facts:
- ‖Ae_i‖² ≥ ‖Λu(i)‖² ≥ l_i.
- Ae_i = UΛu(i) + Re_i with Re_i ⊥ range U, so ‖Re_i‖ ≤ η and |R_ii| ≤ η.

The identity. With ε = ±1, ξ = (1+ε)/2, Δ = U^T D_ε U and Φ = U_I^T A_IJ U_J:

4Φ = (I+Δ)Λ(I−Δ) − T_0 − T_1, T_0 = Σ_i R_ii u(i)u(i)^T, T_1 = Σ_{i≠j} ε_iε_j R_ij u(i)u(j)^T.

This follows from U^T diag(ξ) R diag(1−ξ) U = ¼ U^T(I + D_ε)R(I − D_ε)U = −¼ U^T D_ε R D_ε U, using RU = 0 and U^T R = 0.

Moments:
- E‖Δ‖_F² = Σ l_i² ≤ 3η².
- E‖T_1‖_F² ≤ 2Σ_{i≠j} R_ij² l_i l_j ≤ 2 (max l) Σ_i l_i ‖Re_i‖² ≤ 6η⁴. Only the pairings (i,j) and (j,i) survive, and (u(i)·u(j))² ≤ l_i l_j.
- ‖T_0‖ ≤ max_i |R_ii| ≤ η.

By Markov, ‖Δ‖_F² ≤ 12η² and ‖T_1‖_F² ≤ 24η⁴ hold together with probability ≥ 1/2. On that event:
- s_3(4Φ) ≥ (1 − 2√3 η)² − η − 2√6 η² ≥ 0.621.
- ‖U_I‖² ≤ (1 + ‖Δ‖)/2 ≤ 0.5866, and likewise for U_J.
- s_3(A_IJ) ≥ 0.155/0.5866 ≥ 0.264.
- α_i ≤ 3η²/s_3² ≤ 0.108, and Z ≥ s_3⁶. ∎

**Remarks.**
1. The row-norm hypothesis is not scale-invariant. Normalize so that the third largest |λ| is 1 (free, since p_Q(s) = p_{Q/μ}(s/μ)/μ) and take U to be the top three eigenvectors, so ‖R‖ ≤ 1. The same proof gives s_3(4Φ) ≥ (1 − 2√(3l))² − d − 2√(6l) with probability ≥ 1/2, where l = max l_i and d = max |R_ii|. The marginal bound in that regime is not proved (§5.6).
2. This answers (iii): if no partition has s_3 ≥ 0.26 with all marginals ≤ 0.11, then some row has norm > 1/20, which by Corollary 4.4 is a hub or a pivot.

## 5. The decomposition

### 5.1 The dichotomy

Let H = {i : ‖Ae_i‖ ≥ η} and L = [n] − H. For any partition with I ⊂ L and H ⊂ J, every I-row satisfies ‖A_{iJ}‖ < η, so α_i^{(k)} ≤ kη²/T_k. Write V_k^L for the volume sum restricted to pairs with S ⊂ L.

**Theorem 5.1.** Let k ∈ {1, 2, 3} and τ₀ ≥ 4kη². Exactly one of the following holds.

(G2) Some partition with I ⊂ L and H ⊂ J has T_k(A_IJ) ≥ τ₀. Then all I-marginals are ≤ 1/4 and Z ≥ τ₀^k/k!, so Theorem D_k applies. For k = 3, ‖p_Q‖ ≤ 6√e (6/τ₀³)^{1/6} ≤ 13.4 τ₀^{−1/2}.

(G3) Every such partition has T_k < τ₀. Then V_k^L ≤ 2^{k+1} τ₀ V_{k−1}^L. Moreover there are disjoint (k−1)-sets S ⊂ L and T with

Σ_{l ∈ L−K, m ∉ K ∪ {l}} (A − P)_lm² ≤ k² 2^{k+1} τ₀ (= 144τ₀ for k = 3), where K = S ∪ T.

The hub columns are included in this sum; the hub block A_HH is free.

*Proof.* (G2) follows from Proposition 4.3 and Lemma 4.2. For (G3), e_k ≤ T_k e_{k−1} ≤ τ₀ e_{k−1} for every such partition. For S ⊂ L, P(S ⊂ I, T ⊂ J) = 2^{−k−|T∩L|} ∈ [4^{−k}, 2^{−k}]. So 4^{−k} V_k^L ≤ E e_k ≤ τ₀ E e_{k−1} ≤ τ₀ 2^{1−k} V_{k−1}^L. Then apply the row-restricted Theorem 3.1. ∎

**Corollary 5.2.** In (G3) with k = 3 and L′ = L − K,

A_{L′L′} = D + λ₁v₁v₁^T + λ₂v₂v₂^T + E, E symmetric with zero diagonal, ‖E‖_F < 36√τ₀.

A_HH, A_{H,L′} and the four coordinates K are unconstrained. For example, η = 1/400 and τ₀ = 12η² give density ≤ 1550 in (G2) and ‖E‖_F < 0.32 in (G3).

### 5.2 What the downstream results need

| result | needs | delivered by |
|---|---|---|
| Theorem D / D_k | a partition with Z ≥ Z₀ and I-marginals ≤ 1/2 | (G2); Theorem S when there are no hub rows |
| Theorem H | A_II = D + Σ λ_j v_j v_j^T **exactly**; leverages of ρ̃_i = ((v_j)_i, a_ih) ≤ 1/2; A_HH, A_HJ, A_IJ, A_JJ arbitrary | (G3) + Corollary 5.2, except that E ≠ 0. Coordinates with v_j(i)² > l₀ (fewer than 2/l₀) go to J. |
| Prop 5.3 / GEOM 5.5 | σ₂(A_{H,L}) ≥ σ and A_HH = 0 | N_B ≥ 2 in (5.1) |
| Prop 5.4 / GEOM 5.3 | one hub direction and A_HH = 0 | N_B = 1 |
| GEOM 5.4 | one hub coordinate plus one rank-one direction | the E = 0, r = 1 case of (G3) |

### 5.3 Hubs with zero hub block

**Proposition 5.3.** If A_HH = 0 (H of any size) and B = A_{H,L} has σ₂ > 0, then ‖p_Q‖ ≤ 2√π (σ₁σ₂)^{−1/2}, whatever A_LL, b and c are.

*Proof.* Given X_L, Q = ⟨c, X_H⟩ + q with c = 2BX_L + b_H, so the conditional density is ≤ √2/|c| (Ball). The projection of c onto the top two left singular directions is (2σ₁Z₁ + β₁, 2σ₂Z₂ + β₂). Z is a two-dimensional marginal, of density ≤ 2, so this vector has density ≤ K = 1/(2σ₁σ₂). The bathtub principle gives E|Y|^{−1} ≤ 2√(πK). ∎

For two hubs this sharpens GEOM 5.5, from 1/2 + 8σ^{−2} to about 3.55/σ.

**Proposition 5.4.** If A_HH = 0, then P(|Q − s| ≤ u) ≤ (4u/σ₁)(1 + log₊(σ₁/(4u))), so α₂ ≤ (4/σ₁)(1 + log₊(σ₁/4)).

*Proof.* The conditional small-ball probability is ≤ min(1, 2√2 u/|c|), and |c| ≥ |2σ₁⟨b₁, X_L⟩ + β|, which has density ≤ 1/(√2 σ₁). Apply the bathtub principle on the line. ∎

### 5.4 The reduction

For a no-pivot matrix with at least three eigenvalues of modulus ≥ 1, either (G2) gives a universal density bound, or (G3) holds. In (G3), after conditioning on the four coordinates K (lossless),

Q = X_H^T A_HH X_H + 2X_H^T A_{H,L′} X_{L′} + X_{L′}^T (D + Σ_{j≤2} λ_j v_j v_j^T + E) X_{L′} + linear terms.

Theorem H bounds this form when E = 0, for any hub block and any hub diagonal. It needs the decay exponent |H_used| + r/2 > 1 and a well-conditioned G̃.

> **(TH-ε)** Theorem H stays true, with constants depending on its data and on ε₀, when the light block carries a symmetric zero-diagonal twist E with ‖E‖_F ≤ ε₀.

"Star + rank one + eps W" with small eps·√n is exactly (G3), with ‖E‖_F = eps·√n; numerically T_3 is about 0.06 eps²n. With large eps·√n it is (G2). After the decomposition, both open configurations, a hub with a dense remainder and a hub with a nonzero diagonal, become instances of (TH-ε), since Theorem H is indifferent to the hub block.

### 5.5 Eigenvalue bookkeeping

Weyl's inequality gives, for t ∈ (0,1),

N_A(1) ≤ N_{A_HH}(1−t) + N_{A_LL}(1−t) + 2N_B(t). (5.1)

With t = 1/4:
- N_{A_LL}(3/4) ≥ 3: Theorem S applies to (4/3)A_LL.
- N_B ≥ 2: two hub directions (Proposition 5.3 when A_HH = 0).
- N_B = 1: the hub direction must be completed by a large eigenvalue of A_LL or of A_HH.

Two warnings.
- A hub coupled along the spread direction adds no eigenvalue pair. Indeed e_h w^T + w e_h^T + σww^T = σ(w + e_h/σ)(w + e_h/σ)^T − e_h e_h^T/σ has eigenvalues (σ ± √(σ²+4))/2, only one of modulus ≥ 1 when σ is near 1. In Theorem H this shows up as a singular G̃, so the count must be done on the core span(e_h, w_h, v_j).
- A_HH carries large eigenvalues only if |H| is at least about (3/4)/√(2c). If it carries three, condition on X_L and use induction on n (same constant, since conditioning is lossless).

### 5.6 Not proved

1. (TH-ε).
2. f(r) = 2r in general.
3. A dimension-free operator-norm robust lemma.
4. **The scale caveat.** If every row has norm ≥ η (for instance 10³ × spread rank 2 + spread rank 1 with moderate n), then H = [n] and (G3) says nothing, although Theorem D applies. The leverage variant of Theorem S proves s_3 in this regime. The missing piece is a partition-independent heaviness that controls the marginals when some singular values dwarf s_3: in α_i ≤ Σ_m min(1, 3s_m²/T_3) u_m(i)², the large directions should enter only through their leverage. Adaptive η, whose (G2) constant improves as η grows, handles dense matrices but not widely separated eigenvalues.
5. A hub block carrying one or two large eigenvalues, weakly coupled to a light block carrying the rest.

## 6. Numerical checks (scripts in the folder)

**check_thmS.py**
- Marginal formula against brute force: error 1.4e-15.
- α_i / (3‖m_i‖²/T_3) ≤ 0.50.
- The identity 4Φ = …: error 1.1e-15.
- Theorem S on n = 200 and 800, 40 partitions each, with four remainders: none; dense Wigner with rows up to 0.56; a diagonal-cancelling remainder; eigenvalues (1, 40, −3) with rows up to 8.8. Median s_3 was 0.45–0.63 (minimum 0.37); every run's largest I-marginal was ≤ 0.19.

**check_dichotomy.py**
- Skeleton identity: 10.771342625751851 on both sides (n = 8, two rows barred from S).
- Over 2000 random spectra, the largest e_3/(e_2T_3) was 1.000 (bound: ≤ 1) and the smallest e_3/(T_3T_2T_1/6) was 1.05 (bound: ≥ 1).
- Star + rank one + eps W with the hub forced into J: median T_3 = 0.0054, 0.06, 0.53 at eps·√n = 0.3, 1, 3; median largest I-marginal 0.07–0.32.
- In this family the eigenvalues sit at 1, so the printed count of eigenvalues ≥ 1 read 1–2. This does not affect the check.

## 7. Next step

Prove (TH-ε) for one hub (any diagonal), one spread rank-one direction with |λ| ≥ 1, and a zero-diagonal leaf twist E with ‖E‖_F ≤ ε₀ and light rows. A natural route: keep the Fresnel and hub variables of Theorem H, and decouple exp(itX^T E X) against the same Brascamp–Lieb data. E has small Frobenius norm, so its decoupled blocks have small volume in every direction.
