## Summary

**Status: PARTIAL.** The architecture is complete. The conjecture now reduces to six precisely stated lemmas, and several branches previously listed as open are closed with explicit constants.

**What is new and proved:**
1. **Level 1 is closed, in both forms.**
   - Log form: H′₁ ≤ 12 (Theorem A). It uses the decoupling bound D₁ with q = 2, which needs no marginal condition, together with the fact that the log form only needs some power decay of φ.
   - Sublevel form: α₁ ≤ 28.1 when c ≤ 1/500 (Theorem A′). Sort rows by norm; the tails' Frobenius mass either passes a 1-marginal test early or decays geometrically, and geometric decay is impossible once the mass exceeds 204ε².
2. **Light-rows Fourier theorem (LF), levels 2 and 3.** For any row set L, if e₃(ν²) ≥ 72ρ_L²e₂(ν²), Theorem D applies with density ≤ 22.2(ν₁ν₂ν₃)^{-1/3}. The level-2 analogue gives α₂.
   - It needs no spectral gap, no leverage bound and no concentration: only first moments over a random partition.
   - The two new tools are an overlap inequality, W_k^{(L)} ≥ e_k − 2(k−1)ρ_L²e_{k−1}, and a marginal bound, αᵢ ≤ |bᵢ|²e_{k−1}/e_k.
   - Heavy rows go on the unconstrained side J, so hub columns count as Fourier directions.
   - Corollary: a no-pivot matrix with no row of norm above μ₀/14.7 (level 3) or μ₀/8.5 (level 2) is closed.
3. **Structure when LF fails (Theorem S).**
   - A heavy row exists.
   - If the light rows carry two directions of size ≥ 17ρ₀, they are rank 2 plus a Frobenius remainder below 13.9ρ₀. That is Frobenius-small, not only operator-small.
   - A Weyl count bounds how many heavy rows there are relative to the light rows' spectrum.
   - With |H| ≤ N₀ heavy rows, the hub block satisfies ‖E_HH‖_F ≤ N₀√(2c), so it is negligible.
   - With exactly one heavy row, the normal form is E = S + R: S is a rank-3 core (the hub plus a spread rank-2 block), and ‖R‖_F < 19.6ρ₀.
4. **Hub reduction at level 2 (Lemma HR).** α₂(Q) ≤ 8K(1 + log₊ 1/(8K)), where K = α₁(Δ) and Δ is the discriminant form. Δ's matrix is exactly −4a(M/a), a Schur complement. With Theorem A′ this closes level 2 for no-pivot matrices with ‖M‖ ≤ ρ₀²/(2c).
5. **A new explicit gap.** In the single-hub normal form the hub row usually lies inside the rank-2 span; call the square coefficient along the hub direction σ.
   - Simplest instance: Q = 4X_hL + 2L² + 2V² + Σdᵢ Xᵢ² with small dᵢ ≠ 0.
   - Every off-diagonal block has rank 2 (20 of 20 random partitions), the Gram matrices of Theorems H and MF are singular, and Proposition 5.4 needs d = 0.
   - The density is bounded numerically (1.45 to 1.67), so this is a gap in the methods, not a counterexample.
   - It would follow from (M-D2): a bounded density for "definite spread rank 2 + small diagonal twist".

**The six missing lemmas:**
- **M-TW:** the twist lemma for |t| ≤ 1/‖R‖_F.
- **M-PEEL:** peeling sub-hubs out of the remainder R.
- **M-DEG:** the degenerate single hub (σ ≠ 0), implied by M-D2.
- **M-2H:** Proposition 5.5 with a small nonzero hub block.
- **M-MH:** many heavy rows.
- **M-BIG2:** at level 2, a hub absorbed by a huge eigen-direction.

**Checks.** The exact overlap identity matches brute force to 6e-15, the marginal bound holds (with equality at k = 1), and the overlap inequality was never violated. For k = 3 at the tested sizes (n up to 22) its right side was negative, so it was never tested in the regime where it bites.

**Most useful next step:** prove M-D2. It is self-contained, nobody else holds it, and it closes the whole σ ≠ 0 case at R = 0.

- num/

---

# REPORT: the level-one node, the light-rows Fourier theorem, and the structure of its failure

**Notation.**
- X has independent coordinates with densities at most 1. Q = XᵀMX + bᵀX + c₀, with M symmetric and b, c₀ arbitrary.
- α₁, α₂, H′₁, H′₂ are as in GEOM.
- "No c-pivot" means every |mᵢᵢ| < c and every 2×2 principal minor has modulus < c; then every |mᵢⱼ| < ε := √(2c).
- E := M − diag M, rᵢ := |rowᵢ(E)|, μ₀ := 1 − c.
- e_k(B) is e_k of the squared singular values of B, and Z_k = e_k(M_IJ).

By GEOM Theorems 3.1, 5.1 and 5.2, the conjecture is equivalent to three no-pivot statements, each uniform in b and c₀: H′₁ with one large eigenvalue, H′₂ with two, and a bounded density with three.

## 1. Lemma 0 (decay requirements)

**Esseen bound.** For every Z, s and u > 0:
- P(|Z−s| ≤ u) ≤ 1.0877 u ∫_{|t|≤1/u} |φ_Z|.
- Proof: the triangle kernel satisfies (sin(x/2)/(x/2))² = ∫(1−|t|)₊ e^{itx} dt, and it is ≥ 0.91939 on |x| ≤ 1.

**Consequence.** If |φ_Z| ≤ min(1, B|t|^{−b}) with 0 < b < 1, then sup_s P(|Z−s| ≤ u) ≤ 2.18 B u^b/(1−b), and by the layer-cake formula:
- H′₁ ≤ b^{−1}(1 + log₊(2.18B/(1−b))).
- H′₂ ≤ 2.18B/((1−b)(2b−1)) when b > 1/2.

So H′₁ needs any power decay, H′₂ needs decay beyond |t|^{−1/2}, and α₂ follows from decay |t|^{−1}.

## 2. The bound D_k(q), and its case k = 1

Decoupling gives |φ|² ≤ E_W F with F = Π_{i∈I} |ψᵢ(2t(BW)ᵢ)|, where B = M_IJ and W = X_J − X′_J. By Jensen and the Brascamp–Lieb argument of Theorem D (RES §6, FOUR §1.2), whenever max_I αᵢ^{(k)} ≤ q/2 with 1 ≤ q ≤ 2:

  E_W F^q ≤ e^{k/2} (2π/|t|)^k q^{−k/2} Z_k^{−1/2}.   (2.1)

**The case k = 1 in full.**
- Exponents: αᵢ = |aᵢ|²/Z₁ for the rows and 1 − β_j for the columns, where β_j = |col_j|²/Z₁.
- Lieb's Gaussian constant: det(D_J + BᵀD_I B) ≥ Σ_{i,j} b_ij² dᵢ Π_{j′≠j} e_{j′} ≥ Z₁ Π dᵢ^{αᵢ} Π e_j^{1−β_j}. This comes from expanding "diagonal plus positive semidefinite", keeping the |T| = 1 terms, and weighted AM–GM with weights b_ij²/Z₁.
- One-dimensional factors: ∫|ψᵢ(2ts)|^{q/αᵢ} ds ≤ (2|t|)^{−1} 4π (αᵢ/q)^{1/2}, by RES Lemma 1, which needs q/αᵢ ≥ 2.
- Multiplying out: E_W F^q ≤ e^{1/2}(2π/|t|) q^{−1/2} Z₁^{−1/2}.

This yields two bounds:
- (2.2) With q = 2, no marginal condition is needed: |φ| ≤ (π√(2e))^{1/4} Z₁^{−1/8} |t|^{−1/4}.
- (2.3) With q = 1, if all αᵢ ≤ 1/2: |φ| ≤ e^{1/4}(2π)^{1/2} Z₁^{−1/4} |t|^{−1/2}.

Both hold for φ of Q itself, since the bounds are uniform over the conditioned values.

## 3. The level-one node

**Theorem A.** Let c ≤ 1/2 and let M have no c-pivot and an eigenvalue of modulus ≥ 1. Then H′₁(Q) ≤ 12.

*Proof.*
1. ‖E‖ ≥ μ₀, so ‖E‖²_F ≥ μ₀².
2. For a random partition, E‖M_IJ‖²_F = ‖E‖²_F/4. So some partition has Z₁ ≥ 1/16.
3. By (2.2), B ≤ 2.33. Lemma 0 with b = 1/4 gives H′₁ ≤ 4(1 + log(2.9B)) ≤ 11.6. ∎

**Theorem A′.** Let c ≤ 1/500 and let M have no c-pivot and an eigenvalue of modulus ≥ 1. Then α₁(Q) ≤ 28.1.
Consequently, every symmetric N with an eigenvalue of modulus ≥ Λ has α₁ ≤ 1118 Λ^{−1/2}, for all linear terms.

*Proof.* Sort r₁ ≥ r₂ ≥ …; put S_k = Σ_{j≥k} r_j², L_k = {k+1, …, n} and T_k = {1, …, k}.
1. **Test.** Suppose S_{k+1} ≥ 8r_{k+1}². Split L_k by fair coins and put J = [n] ∖ I. Some outcome has e₁(E_IJ) ≥ S_{k+1}/4 ≥ 2r_{k+1}². Every row of E_IJ has norm ≤ r_{k+1}, so all 1-marginals are ≤ 1/2. Then (2.3) and Esseen give α₁ ≤ 14.0 e₁(E_IJ)^{−1/4}.
2. **Failures force geometric decay.** If the test fails for j < k, then S_{j+2} < (7/8)S_{j+1}, so S_{k+1} < (7/8)^k S₁.
3. **A block bound that always holds.** S₁ ≤ k(k−1)ε² + 2S_{k+1}.
4. **Contradiction.** At k = 11 steps 2 and 3 give S₁ ≤ 110ε² + 0.461S₁, so S₁ ≤ 204ε² = 408c < μ₀². This is impossible.
5. **Conclusion.** So the test holds at some k ≤ 10, where S_{k+1} ≥ S₁/4. Step 1 then gives α₁ ≤ 28 S₁^{−1/4} ≤ 28.1.
6. **General N.** Scale to N/Λ. If it has a c-pivot, the level-one certificate gives 50c^{−1/2} = 1118; otherwise use the above. ∎

## 4. Marginals are controlled by row norms

**Lemma M.** For any matrix B with rows bᵢ and squared singular values a₁ ≥ a₂ ≥ …:

  αᵢ^{(k)} ≤ |bᵢ|² e_{k−1}(a)/e_k(a) ≤ k|bᵢ|²/a_k.

*Proof.*
1. αᵢ = 1 − e_k(BᵀB − bᵢbᵢᵀ)/e_k(BᵀB).
2. The map t ↦ e_k(A + tbbᵀ) is affine, because det(x − A − tbbᵀ) = det(x − A)(1 − t bᵀ(x−A)^{−1}b). Its slope is Σ_j (v_jᵀb)² e_{k−1}(a_{−j}).
3. So αᵢ = Σ_j (v_jᵀbᵢ)² e_{k−1}(a_{−j})/e_k(a) ≤ |bᵢ|² e_{k−1}(a)/e_k(a).
4. For the second inequality, assign to each (k−1)-set P a top-k index outside it. Each k-set arises at most k times, so a_k e_{k−1}(a) ≤ k e_k(a). ∎

**Lemma M′ (multi-scale form).** For every K ≥ k:

  αᵢ ≤ Σ_{j≤K} u_j(i)² + (k/a_k) |rowᵢ(B − B_K)|²,

where B_K is the best rank-K approximation. The proof uses p_j ≤ 1 for every j, and p_j ≤ k a_j/a_k for j outside the top k.

## 5. The overlap inequality

**Lemma O.** Let E be symmetric with zero diagonal, L ⊂ [n], B₀ = E_{L,[n]} with singular values ν, and ρ_L = max_{i∈L} rᵢ. Let W_k^{(L)} = Σ det(E_ST)² over S ⊂ L, T ⊂ [n], |S| = |T| = k, with S and T disjoint. Then

  W_k^{(L)} ≥ e_k(ν²) − 2(k−1) ρ_L² e_{k−1}(ν²).

*Proof.*
1. The overlap mass is at most Σ_{i∈L} Φᵢ, where Φᵢ = Σ_{S,T∋i} det(E_ST)².
2. Use the SVD B₀ = Σ ν_r a_r b_rᵀ and Cauchy–Binet. Then Φᵢ = Σ_{R,R′} ν_R ν_{R′} F_{RR′}(α) F_{RR′}(β), with α_r = a_r(i), β_r = b_r(i), and F_{RR′}(x) = δ_{RR′} − det((I − xxᵀ)_{R,R′}).
3. The values of F:
   - F_RR = |x_R|²;
   - F = ±x_r x_{r′} (with a sign depending only on R, R′) when |R ∩ R′| = k−1;
   - F = 0 when |R ∩ R′| ≤ k−2.
4. Since Σ_r ν_r α_r β_r = E_ii = 0, this becomes
   Φᵢ = Σ_R ν_R² Σ_{r≠r′∈R} α_r² β_{r′}² + Σ_{|Q|=k−1} ν_Q² (Σ_{r∈Q} ν_r α_r β_r)².
5. Sum over i ∈ L. Use Σ_r ν_r² a_r(i)² = rᵢ² ≤ ρ_L² and Σ_{i∈L} b_r(i)² ≤ 1 in the first term, and Cauchy–Schwarz in the second. Each term is at most (k−1) ρ_L² e_{k−1}. ∎

A single hub makes the inequality an equality, with W₂ = 0.

## 6. Theorem LF (light-rows Fourier)

**Theorem LF.**
- **(a)** If e₃(ν²) ≥ 72ρ_L² e₂(ν²), there are disjoint I ⊂ L and J with Z₃ ≥ e₃/128 and every 3-marginal on I at most 1/2. Hence ‖p_Q‖ ≤ 22.2 (ν₁ν₂ν₃)^{−1/3} for all b, c₀. It suffices that ν₃ ≥ 14.7 ρ_L.
- **(b)** If e₂(ν²) ≥ 36ρ_L² e₁(ν²), there is a partition with Z₂ ≥ e₂/32 and 2-marginals ≤ 1/2. Hence |φ| ≤ 24.6(ν₁ν₂)^{−1/2}/|t|, α₂ is bounded, and H′₂ ≤ 3α₂.

*Proof of (a).*
1. Coins on L; I is the coin-1 set, J = [n] ∖ I. Each disjoint pair (S, T) has probability ≥ 2^{−6}, and meeting pairs have probability 0.
2. So E e₃(B) ≥ 2^{−6}(e₃ − 4ρ_L² e₂) by Lemma O, and E e₂(B) ≤ e₂/4.
3. Hence E[e₃(B) − 2ρ_L² e₂(B)] ≥ 2^{−6}(e₃ − 36ρ_L² e₂) ≥ 2^{−7}e₃.
4. Take an outcome achieving this. Lemma M gives marginals ≤ 1/2, and Theorem D gives 6√e (2⁷/e₃)^{1/6} ≤ 22.2 e₃^{−1/6}.

*Proof of (b).* The same with k = 2, then (2.1) with q = 1. ∎

**Corollary (no hub).** Take L = [n], so ν = |μ|.
- Three large eigenvalues and every row of E at most μ₃/14.7 ⇒ Theorem D applies.
- Two large eigenvalues and every row at most μ₂/8.5 ⇒ α₂ is bounded.

Only the ratio e₃/e₂ enters, so Wigner blocks with large rows are covered too.

## 7. Structure when LF fails

**Theorem S.** Let ρ₀ ≤ μ₀/17, H = {rᵢ > ρ₀}, L the rest, T = Σ_{j≥3} ν_j². Suppose LF(a) fails for every row set. Then:
- **(a)** Some row has norm greater than μ₀/14.7.
- **(b)** If ν₂ ≥ 17ρ₀, then T < 192ρ₀².
- **(c)** μ²_{j+|H|} ≤ ν_j² for all j, by Weyl applied to E² = E_Lᵀ E_L + E_Hᵀ E_H.
- **(d)** ‖E_HH‖²_F ≤ |H|² ε².

*Proof of (b).* Write y = ν², K = 72ρ₀², t for the tail values and m = y₂. Failure means e₃ < K e₂.
- **If T ≤ y₂:** from y₁y₂T < K(y₁y₂ + (y₁+y₂)T + T²/2) we get T < K + (5/8)T, so T < 8K/3.
- **If T > y₂:** split e₃ − K e₂ = y₁y₂(T−K) + (y₁+y₂)(e₂(t) − KT) + (e₃(t) − K e₂(t)). Use e₂(t) ≥ T(T−m)/2 and e₃(t) ≥ T(T−m)(T−2m)/6. In each of the sub-cases T < 2m, 2m ≤ T < 4m and T ≥ 4m this gives e₃ > K e₂, a contradiction. ∎

**Corollary S1 (one heavy row, ρ₀ = μ₀/100).** Let Π be the projection onto the two leading left singular vectors p₁, p₂ of E_{L,·}. Put S = [[ΠE_LLΠ, ΠE_Lh], [E_hLΠ, 0]] and R = E − S. Then:
- S has rank ≤ 3;
- ‖R‖²_F ≤ 2T, so ‖R‖_F < 19.6ρ₀;
- S has three eigenvalues of modulus ≥ 0.8μ₀;
- each coordinate has leverage ≤ 2ρ₀²/μ₀² in span(p₁, p₂).

## 8. Level two at a hub

**Lemma HR.** For any M and coordinate h, write a = m_hh, m = M_{h,−h}, and Q = aX_h² + ℓX_h + q₀ with ℓ = 2⟨m, X′⟩ + b_h. Set Δ_s = ℓ² + 4a(s − q₀). Its matrix is 4(mmᵀ − aM_{−h,−h}) = −4a(M/a). If sup_s α₁(Δ_s) ≤ K, then

  P(|Q−s| ≤ u) ≤ 8Ku(1 + log₊ 1/(8Ku)).

*Proof.*
1. GEOM Lemma 1.2(ii), with |a||s−κ| = |Δ_s|/4, bounds the conditional probability by min(1, 8u|Δ_s|^{−1/2}).
2. Integrate: E min(1, 8u|Δ|^{−1/2}) ≤ ∫₀¹ min(1, 8Ku/λ) dλ. ∎

**Corollary HR.** Let c ≤ 1/500, M no c-pivot with two eigenvalues of modulus ≥ 1, and ‖M‖ ≤ ρ₀²/(2c) with ρ₀ = μ₀/8.5. Then α₂ ≤ 1.1e5.

*Proof.*
1. Either LF(b) applies, or there is a row with |m| > ρ₀.
2. In the second case ‖N‖ ≥ 4(|m|² − |a|‖M′‖) ≥ 2ρ₀².
3. Theorem A′ gives K ≤ 6.8e3, and Lemma HR finishes. ∎

**Where this stops.** Schur complements at a level-two node can have norm of order ‖A‖²/c. A hub row nearly parallel to a huge spread eigen-direction is absorbed by it. The density can still be small: for hub + Λvvᵀ with m parallel to v and a = |m|²/Λ, Q equals ΛW² + Z². The uniform statement is M-BIG2; Lemma M′ is the natural tool.

## 9. A single-hub configuration outside every proved theorem

**Normal form.** In the basis (e_h, ŵ, v), the core is [[a, κ, 0], [κ, α, β], [0, β, γ]]. Completing the square:

  Q = aX_h² + 2κX_hL + σL² + γṼ² + Xᵀ(D + R)X + linear,  with σ = α − β²/γ.

**What is proved in this form:**
- σ = 0, R = 0 (any diagonal D): Theorem H applies.
- D = 0, R = 0 (any σ): GEOM Proposition 5.4 applies.

**Why σ ≠ 0 escapes.** The hub column lies in the span of the Fresnel directions, so the Gram matrices of Theorems H and MF are singular. Absolute-value Fourier gives only |t|^{−3/2}(1 + |tσ|)^{1/2}, because of twist inflation along the hub tilt.

**Simplest instance:** Q = 4X_hL + 2L² + 2V² + Σdᵢ Xᵢ² with 0 < |dᵢ| < c.
- Core eigenvalues 1−√5, 2 and 1+√5; no pivot.
- Every M_IJ has rank 2: with h ∈ J, M_IJ = w_I(2e_h + 2w_{J′})ᵀ + 2v_I v_{J′}ᵀ. So D and all its variants are blind.
- Theorem F fails, because h has leverage 1.
- Theorem MF fails: its Gram matrix Γ = [[4, 2, 0], [2, 1, 0], [0, 0, 1]] is singular.
- Proposition 5.4 needs d = 0.
- Conditioning on X_h leaves a definite spread rank-2 form plus a diagonal twist, which reduces this case to M-D2.
- Numerically (n = 60, uniform laws) the density is 1.67, 1.65 and 1.45 for d = 0, ±0.02 and ±0.1.

## 10. What remains

The one-hub normal form is exact up to a remainder R that is small in Frobenius norm.
- **Tail range |t| ≥ 1/‖R‖_F:** Theorem D works exactly when no row of R carries more than about a third of ‖R‖²_F. The 3-marginal of row i is then about lev_i(top two) + |rowᵢ(R)|²/‖R‖²_F, by Lemma M′.
- **Missing, beyond that:** M-TW, M-PEEL, M-DEG (via M-D2), M-2H, M-MH and M-BIG2. Everything else in the tree is proved.

## 11. Numerics (scripts in num/, BelowNormal, each under a minute)

- **Φᵢ identity:** matches brute force to 6e-15 on 40 cases.
- **Lemma M:** worst ratio of true marginal to bound 1.0000000000000009.
- **Lemma O:** never violated in 63 cases, at n = 12 and n = 22.
- **Degenerate example of §9:** every random partition gives rank-2 blocks, and the density is bounded, as reported above.
