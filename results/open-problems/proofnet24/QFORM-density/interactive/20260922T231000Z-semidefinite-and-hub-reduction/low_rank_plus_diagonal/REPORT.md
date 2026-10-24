## Summary

Status: **PARTIAL.** Exact rank three is now proved in every configuration except one that we can state precisely: the nearly pure hub whose hub direction leaks onto the light coordinates.

No step uses a pointwise bound on |ψ|. Every Fourier step goes through Lemma 1 (Lᵖ bounds), Theorem F, Theorem D / D₂, or the Fejér form of Esseen.

**The rank-three result**
- **Rank two at level two is complete.** For a coordinate j, the discriminant Δ_s = M′² − a(C′ − s) is a rank-one form with eigenvalue −det(M)·l_j, whatever the hub diagonal a is (Lemma 1.5). This gives α₂ ≤ 88 for every rank-two form with any linear terms. So the tree for exact rank three has depth one, and any c-pivot gives density ≤ 176 c^{−1/2}.
- **Hub normal form.** With no pivot, either every leverage is ≤ 1/2 (density ≤ 12), or there is a null heavy coordinate h (l_h > 1/2, |a_hh| < c). In the basis adapted to h, M = [[p,q,κ],[q,s,0],[κ,0,m]] with κ² ≥ 1 − m², |s| ≥ 1, q² + s² ≥ 1, and the hub direction is r₃ = √l_h e_h + εw with ε² = 1 − l_h.
- **Leak-free hub (ε = 0).** Through GEOM Prop 5.4 it gives density ≤ 278 whenever the linear term lies in range(R). The key identity is D_H = |det M|/(|s|κ²); since |det M| ≥ max(κ, |s|) and |s| ≥ 1, the Prop 5.4 constant stays bounded. With no square along the hub partner (p′ = 0), Theorem H gives ≤ 7.6 with any linear term.
- **Leaking hub (ε > 0), spread light frame.** Theorem D₂ gives |φ(t)| ≤ 41.6/|t| uniformly in ε, because Z₂ ≥ κ²(q² + s²)/256. Theorem F gives the high frequencies. Together: density ≤ 41 + 27 log₊(1/(6ε)), with any linear term.
- **Definite rank three:** ≤ 249 with any linear term. **Definite exact rank r:** ≤ 304 for every r.

**What is still open in exact rank three.** No pivot, M indefinite, a null heavy coordinate h, and one of:
- (O1) small leakage ε > 0, with the level on the two-sheet side or the linear term outside range(R). Here only a logarithmic growth as l_h → 1 is not excluded, and at l_h = 1 the density is bounded when the linear term is in range.
- (O2) ε = 0, a square along the hub partner (p′ ≠ 0), and the linear term outside range(R).
- (O3) a light frame that is not spread, for example leakage concentrated on a few coordinates, or a second heavy row.

For D ≠ 0, diagonal cancellation creates exactly this hub-plus-square configuration, now carrying a diagonal twist. Theorem H, twist_obstruction/ Cor 3.2 and hub_decoupling/ Thm 5.1 all fail on it for the same reason: the hub column lies in the span of the light block's frame.

**Most useful next step.** Prove the leaky form of Prop 5.4's estimate, (LH) in §3.3 below. Equivalently, find any gain over D₂'s 1/|t| decay in the frequency range 1 ≪ |t| ≪ ε⁻². This is the same slice / mixed-norm estimate that hub_decoupling/ calls Ω.

---

# Diagonal plus bounded rank: heavy coordinates, the lower levels, and exact rank three

## 0. Setting, conventions and tools

X = (X_1, …, X_n) has independent coordinates with densities f_i ≤ 1 and characteristic functions ψ_i. Q = XᵀAX + bᵀX + c and φ(t) = E e^{itQ}. For a random variable Z,

- α₁(Z) = sup_{s, u>0} P(|Z − s| ≤ u)/√u,
- α₂(Z) = sup_{s, 0<u≤1} P(|Z − s| ≤ u)/(u(1 + log(1/u))).

**The class.** A = D + RMRᵀ, where R is n × r with orthonormal columns r_1, …, r_r, M is symmetric r × r, and D is diagonal. The form D + Σ λ_k v_k v_kᵀ with orthonormal v_k is the case M = diag(λ); conversely RMRᵀ = Σ λ_k (Ro_k)(Ro_k)ᵀ for an eigenbasis o_k of M.

- The rows of R are ρ_i = Rᵀe_i, and l_i = |ρ_i|² are the leverages (Σ l_i = r).
- Replacing (R, M) by (RO, OᵀMO) with O orthogonal does not change A; this rotation is used freely.
- A c-pivot is a diagonal entry, or a 2 × 2 principal minor, of modulus ≥ c.

**Tools from the record.**
- (T1) Lemma 1 of RESULTS: ∫|ĝ|ᵖ ≤ 4π/√p for |g| ≤ f ≤ 1 and p ≥ 2, twisted transforms included.
- (T2) Theorem F, conditioned form (RESULTS §4, FOURIER §3.1). Suppose on a coordinate set I the quadratic part is Σ_{k≤r} λ_k v_k v_kᵀ plus a matrix diagonal on I. Suppose the rows ρ_i^I = ((v_k)_i)_k have invertible Gram matrix G_I and normalized leverages ρ_iᵀG_I⁻¹ρ_i ≤ 1/2. Then after conditioning on the other coordinates
  |φ(t)| ≤ (4π)^{r/2} |t|^{−r/2} (∏|λ_k| det G_I)^{−1/2}, uniformly in linear terms,
  and for r ≥ 3, ‖p_Q‖ ≤ (4r/(r − 2)) (∏|λ_k| det G_I)^{−1/r}.
- (T3) Theorem D_k (FOURIER §1.2) with k = 2, q = 1. For disjoint I, J, if every 2-volume-sampling marginal of A_IJ on I is ≤ 1/2, then |φ(t)| ≤ e^{1/2} (2π/|t|) e₂(A_IJᵀA_IJ)^{−1/4}, uniformly in linear terms and diagonal blocks.
- (T4) Esseen, Fejér form: sup_s P(|Z − s| ≤ h) ≤ 1.0877 h ∫_{|t|≤1/h} |φ_Z(t)| dt. Here K(x) = (sin(x/2)/(x/2))² ≥ 0.9194 on |x| ≤ 1 and K̂(t) = 2π(1 − |t|)₊.
- (T5) From GEOM: Lemmas 1.2–1.6; the profiles (P1)–(P3) and compositions (C1)–(C6); the decision tree, Theorem 5.1; Proposition 5.4.
- (T6) Theorem H (RESULTS §5) and Theorem C (RESULTS §7).

No argument uses a pointwise bound on |ψ_i|.

## 1. Linear algebra

**Lemma 1.1 (Schur complements).** If A = D + RMRᵀ and a = a_hh ≠ 0, then
A/a = D_{−h} + R_{−h}(M − Mρ_hρ_hᵀM/a)R_{−h}ᵀ,
and likewise for an invertible 2 × 2 block. So "diagonal plus rank ≤ r" is closed under the moves of the tree. For D = 0, a 1 × 1 (resp. 2 × 2) pivot lowers the rank by exactly one (resp. two).

*Proof.* A_{−h,h} = R_{−h}Mρ_h because D is diagonal. The rank statement is Guttman's rank additivity. ∎

**Lemma 1.2 (interlacing).** Let M be r × r symmetric with every eigenvalue of modulus ≥ 1, and let B be a principal k × k block (in some orthonormal basis) with ‖B‖ < 1. Then 2k ≤ r, and M has at least k eigenvalues ≥ 1 and at least k eigenvalues ≤ −1.

*Proof.* Interlacing gives λ_i(M) ≥ λ_i(B) ≥ λ_{i+r−k}(M). Taking i = k gives λ_k(M) > −1, hence λ_k(M) ≥ 1. Taking i = 1 gives λ_{1+r−k}(M) < 1, hence ≤ −1. So k < 1 + r − k. ∎

This was checked on 20 000 random instances with no violation.

**Lemma 1.3 (heavy directions).** Let A = RMRᵀ have every |eig M| ≥ 1 and no c-pivot (c ≤ 1). Let H = {i : l_i ≥ δ}, so |H| ≤ r/δ, and τ = |H|√(2c). Rotate so that G_H = R_HᵀR_H = diag(g_1 ≥ … ≥ g_r).
- (a) ‖A_HH‖ ≤ τ, and the leading k × k block of M has norm ≤ τ/g_k.
- (b) If τ < 1, then g_k ≤ τ for every k > r/2. So at most ⌊r/2⌋ directions carry more than τ of their mass on H, and M is nearly isotropic on their span.
- (c) If M is definite, then every l_i < c.

*Proof.* No c-pivot gives a_ij² < c + c² ≤ 2c, so ‖A_HH‖_F² ≤ 2c|H|². With R_H = UG_H^{1/2}, A_HH = UG_H^{1/2}MG_H^{1/2}Uᵀ. If g_k > τ, the leading block of M has norm < 1, and Lemma 1.2 applies. For (c), |a_ii| ≥ l_i. ∎

**Lemma 1.4 (hub normal form).** Let M be 3 × 3 symmetric with every |eig| ≥ 1, e_3 a unit vector, and m = e_3ᵀMe_3 with |m| ≤ 1. Rotating in e_3^⊥ so that Me_3 = (κ, 0, m),
M = [[p, q, κ], [q, s, 0], [κ, 0, m]],
and then κ² ≥ 1 − m², q² + s² ≥ 1, |s| ≥ 1, and det M = −s(κ² − mp′) with p′ = p − q²/s.

*Proof.* The first two inequalities are |Me_3|, |Me_2| ≥ 1. For x = (0, κ, −q), Mx = (0, sκ, −mq); the condition |Mx|² ≥ |x|² gives s²κ² ≥ κ² + q²(1 − m²). ∎

**Lemma 1.5 (discriminant).** Fix j and write X′ = X_{−j}. Given X′, Q = aX_j² + 2M′X_j + C′ with a = a_jj, M′ = ⟨α, X′⟩ + m_0 and C′ = X′ᵀBX′ + ⟨β, X′⟩ + c_0, where α = A_{−j,j} and B = A_{−j,−j}. Then Δ_s := M′² − a(C′ − s) has quadratic part N = ααᵀ − aB = −a(A/a).
- (a) Rank 2: N has rank ≤ 1, with nonzero eigenvalue −det(M)·l_j, for every a.
- (b) Rank 3, in a basis with ρ_j = √l_j e_3, c = (M_13, M_23) and P = M_{12,12}: N has rank ≤ 2, and on its range det = l_j·a·det M and trace = l_j(|c|² − M_33 tr P).
- (c) For g(x) = ax² + 2M′x + C′ and any density f ≤ 1: ∫f·1{|g − s| ≤ u} ≤ min(1, 4u/√|Δ_s|), and the density of g(X_j) at s is Σ_{g=s} f/(2√Δ_s).

*Proof.* N = R_{−j}KR_{−j}ᵀ with K = Mρ_jρ_jᵀM − aM. So the nonzero spectrum of N is that of K(I − ρ_jρ_jᵀ). With ρ_j = √l_j e_3, a = l_jM_33 and Ke_3 = 0. The factor I − ρ_jρ_jᵀ = diag(1, 1, 1 − l_j) is the identity on the support of K, so the spectrum is that of l_j(ccᵀ − M_33P); for rank two it is the scalar −l_j det M. The bordered-determinant formula gives det(ccᵀ − M_33P) = M_33 det M. For (c), complete the square, g − s = ay² − Δ_s/a. The inequality √(A + B) − √(A − B) ≤ 2B/√A handles Δ_s > u|a|. The case Δ_s < −u|a| is empty. Otherwise the bound 2√(2u/|a|) ≤ 4u/√|Δ_s| applies, and a = 0 is the linear case. ∎

These identities were checked on 3000 random instances, largest relative error 2·10⁻¹³.

**Lemma 1.6 (diagonal cancellation).** Let A = D + RMRᵀ have no c-pivot. Then ‖R_HMR_Hᵀ + D_H‖ ≤ τ. By Weyl's inequality, at most r coordinates of H have |D_hh| > τ. For these, ρ_hᵀMρ_h ≈ −D_hh and ρ_hᵀMρ_{h′} ≈ 0 (h ≠ h′), within τ. ∎

Each such h is a hub: small diagonal, large row. The smallest example is A = D + λvvᵀ with v = (e_h + w)/√2 and D = −diag(λvvᵀ). Then
A = (λ/2)(e_hwᵀ + we_hᵀ) + (λ/2)(wwᵀ − diag(wwᵀ)),
a star whose light block carries a square along the hub partner and a diagonal twist.

## 2. The lower levels are complete

**Proposition 2.1 (level one, rank one).** If Q = μ⟨u, X⟩² + ⟨b, X⟩ + c with |u| = 1, then α₁(Q) ≤ 15.5 |μ|^{−1/2}.

*Proof.* If some u_k² > 1/2, GEOM Lemma 1.2(ii) in X_k gives P ≤ 4√(e/|μ|). Otherwise (T2) with r = 1 gives |φ| ≤ (4π/(|t||μ|))^{1/2}, and (T4) gives 15.43|μ|^{−1/2}√h. ∎

**Proposition 2.2 (level two, rank two, every configuration).** If A = RMRᵀ has rank two and |det M| ≥ 1, then α₂(Q) ≤ 88 for every b and c.

*Proof.*
- If every l_i ≤ 1/2: (T2) gives |φ| ≤ 4π/|t|, and (T4) gives 27.4h(1 + log(1/h)).
- If some l_j > 1/2: Lemma 1.5(c) gives P(|Q − s| ≤ u) ≤ E min(1, 4u/√|Δ_s|). By Lemma 1.5(a), Δ_s = μ⟨v, X′⟩² + (linear) with |μ| = |det M| l_j ≥ 1/2, whatever a_jj is. So a₁ := α₁(Δ_s) ≤ 22 by Proposition 2.1, and
  ∫₀¹ P(|Δ_s| < 16u²/θ²) dθ ≤ ∫₀¹ min(1, 4a₁u/θ) dθ = 4a₁u(1 + log(1/(4a₁u))) ≤ 88u(1 + log(1/u)). ∎

*Remarks.* The hub diagonal never enters, and linear terms outside range(R) are allowed; the same identity is Lemma X′ of rank_three_geometry/. The density analogue fails. There p_Q(s) ≤ E[Δ_s^{−1/2}; Δ_s > 0], where Δ_s has rank two with small eigenvalue ≈ a det M/κ². This is only a pivot bound, and at a = 0, E|M′|^{−1} = ∞.

**Theorem 2.3 (the tree for exact rank three).** Let A = RMRᵀ have rank three and every |eig M| ≥ 1. If A has a c-pivot, then ‖p_Q‖ ≤ 176 c^{−1/2} for every b and c.

*Proof.*
- A definite 2 × 2 pivot gives ≤ πc^{−1/2} by GEOM Lemma 1.3.
- An indefinite 2 × 2 pivot B gives a type-2 profile with constant K₂ = D^{−1/2}(5.2 + log₊16√D) ≤ 8.4c^{−1/2}. Its centre has the rank-one matrix A/B, with an eigenvalue of modulus ≥ 1 (Lemma 1.1, GEOM 1.5). Proposition 2.1 and (C3) then give ≤ 72c^{−1/2}.
- A 1 × 1 pivot gives a type-1 profile with constant |a|^{−1/2}. Its centre has rank two and |det| ≥ 1, so Proposition 2.2 applies, and (C1) gives ≤ 8c^{−1/2}√(88(1 + log 88)) ≤ 176c^{−1/2}. ∎

Exact rank three therefore reduces to its no-pivot leaf, and the tree has depth one.

## 3. Exact rank three without a pivot

**Theorem 3.1.** Let A = RMRᵀ have rank three, every |eig M| ≥ 1, and no c-pivot with c ≤ 1/100. Let b and c be arbitrary.
- (a) If max l_i ≤ 1/2, then ‖p_Q‖ ≤ 12 (T2 with I = [n], G = I).
- (b) If M is definite, then every l_i < c, so (a) applies. With the tree at c = 1/2, **every definite rank-three form has density ≤ 249, for every linear term.**
- (c) Otherwise fix h with l := l_h > 1/2. Then |a_hh| < c.
  - Rotate so that ρ_h = √l e_3. Then m := M_33 = a_hh/l satisfies |m| < 1/50. The vectors r_1, r_2 vanish at h, and r_3 = √l e_h + εw with ε = √(1 − l). Here w is a unit vector on L = [n] ∖ {h}, orthogonal to r_1 and r_2.
  - With Lemma 1.4, Q = F(S_1, S_2, Z) + ⟨b, X⟩ + c, where F(y) = yᵀMy, S_k = ⟨r_k, X⟩, W = ⟨w, X_L⟩ and Z = √l X_h + εW. The vectors (r_1, r_2, w) form an orthonormal frame on L with leverages λ_i.

  In this setting:
  - (c1) If max λ_i ≤ 1/2, then ‖p_Q‖ ≤ 12(|det M|ε²)^{−1/3}.
  - (c2) If max λ_i ≤ 1/50, then ‖p_Q‖ ≤ 41 + 27 log₊(1/(6ε)), for every linear term.
  - (c3) If ε = 0 (e_h ∈ range R) and b ∈ range(R), then ‖p_Q‖ ≤ 278.
  - (c4) If ε = 0, p′ = 0 and max λ_i ≤ 1/2, then ‖p_Q‖ ≤ 7.6, for every linear term.
  - (c5) If b ∈ range(R), then p_Q(y) ≤ π√2 on the one-sheet side (Theorem C). Here F is indefinite, since |m| < 1.

*Proof.*

(c1) Condition on X_h. The form on L has frame [r_1, r_2, εw], with G_L = diag(1, 1, ε²) and normalized leverages λ_i; apply (T2).

(c2)
1. Split L into I and L ∖ I at random, and set J = {h} ∪ (L ∖ I). Let Γ denote the Gram matrix of (r_1, r_2, w) on each part. By matrix Chernoff, as in GEOM Prop 4.2 (3e^{−0.0767·50} per part), Γ_I, Γ_{L∖I} ≥ I/4 with probability ≥ 0.87.
2. Then G_I = DΓ_ID ≥ Π₁₂/4, where D = diag(1, 1, ε), and G_J ≥ diag(1/4, 1/4, l) ≥ I/4.
3. For N = G_I^{1/2}MG_J^{1/2}:
   NᵀN ≥ ¼ G_J^{1/2}MΠ₁₂MG_J^{1/2}.
   Since e₂ is monotone, Z₂ = e₂(A_IJᵀA_IJ) ≥ (1/16) det(XG_JXᵀ) ≥ det(XXᵀ)/256, where X is the first two rows of M. And det(XXᵀ) ≥ κ²(q² + s²) ≥ 1 − m².
4. The left singular vectors lie in range(R_I), where coordinate i has leverage ρ̂_iᵀΓ_I⁻¹ρ̂_i ≤ 4λ_i. So every 2-marginal is ≤ 0.16.
5. (T3) gives |φ| ≤ 41.6/|t|. Theorem F on L gives |φ| ≤ 44.6ε⁻¹|t|^{−3/2}.
6. Integrating min(1, 41.6/|t|, 44.6ε⁻¹|t|^{−3/2}), and using (c1) when ε ≥ 1/6, gives the bound.

(c3) Divide by κ and apply GEOM Prop 5.4 with a = m/κ, λ = s/κ and σ_F = p′/κ.
1. By Lemma 1.4, D_H = |1 − mp′/κ²| = |det M|/(|s|κ²) > 0. So ‖p_Q‖ ≤ 1/κ + 4Ψ(D_H)/√(κ|s|).
2. Use |det M| ≥ ‖M‖ ≥ max(κ, |s|), |s| ≥ 1 and κ ≥ 0.99.
   - Definite branch: 2√(2π)|s|^{−1/4}|det M|^{−1/4} ≤ 5.02.
   - Hyperbolic branch, D ≥ 1: K ≤ 18.7, so Ψ ≤ 69.
   - Hyperbolic branch, D < 1: log(1/D) ≤ 2 log|det M|, and the term is ≤ 33.9 · sup_{x≥1} x^{−1/4}√(3.89 + log x) ≤ 67.
3. Hence ‖p_Q‖ ≤ 278.

(c4) Theorem H with the single hub h and A_LL = λŝŝᵀ, where λ = (s² + q²)/s and ŝ ∝ r_2 + (q/s)r_1. The hub column is A_Lh = κr_1, and det G̃ = κ²s²/(s² + q²). This gives |φ| ≤ (4π)^{3/2}(2κ)⁻¹|s|^{−1/2}|t|^{−3/2}, and the density is ≤ (3/π)K^{2/3} ≤ 7.6. ∎

**3.2 What remains of exact rank three.** Theorems 2.3 and 3.1 cover every exact rank-three form with universal constants, except in the following configuration. There is no c-pivot, M is indefinite, a coordinate h has l_h > 1/2, and in the normal form of 3.1(c) one of the following holds.
- (O1) 0 < ε is small, and the level lies on the two-sheet side or b ∉ range(R). For a spread light frame the density is at most 41 + 27 log₊(1/(6ε)). So only a logarithmic growth as l_h → 1 is not excluded, and it disappears at l_h = 1 when b is in range, by (c3).
- (O2) ε = 0, p′ ≠ 0 (a square along the hub partner), and b ∉ range(R).
- (O3) The light frame is not spread. This includes leakage concentrated on a set T of light coordinates. Conditioning on X_T removes that leakage and keeps the new linear terms in range, but it costs the mass of r_1, r_2 on T, and it returns to (O1) with a smaller ε.

**3.3 Why the tools stop, and the missing estimate.**
- **Theorem H, 04 Cor 3.2, 10 Thm 5.1.** Each needs the hub row to be independent of the Fresnel (or cross-block) directions. In exact rank r, A_Ih = R_IMρ_h ∈ range(R_I), so G̃ (or Q_I) is singular exactly when p′ ≠ 0 or ε > 0.
- **Fourier with absolute values.** Write φ = C_t ∫ e^{−iuᵀM⁻¹u/(4t)} ∏ψ_i(⟨ρ_i, u⟩ + tb_i) du. Along the hub direction the phase coefficient is (M⁻¹)₃₃/(4t) = −p′/(4tκ²) (at m = 0; checked numerically).
  - If p′ = 0, the u₃-integral is a Fourier inversion, bounded by 2πf_h ≤ 2π. This is Theorem H.
  - If p′ ≠ 0, it is a Schrödinger evolution of f_h, which is of size ≍ (|t|/|p′|)^{1/2} on resonant sets. Absolute-value bounds then give only |t|^{−1}.
- **Decoupling.** It gives C/|t| (c2), which is how the log bound arises.
- **Prop 5.4 with leakage, a twist or an outside term.** Its change of variables needs a bound on the mixed norm ∫ sup_σ ρ_{S_1S_2W}(σ, w) dw. This is unbounded for non-spread projections: if (X_1 ± X_2)/√2 are built from combs of N teeth, the difference set has measure ≈ √2 N.
- **The missing estimate (LH), sufficient for (O1) with m = 0 and b in range:**
  sup_{f ≤ 1, ∫f = 1} E[ f(A(S_1, S_2) − εW) · 1{|S_1| < 1}/|S_1| ] ≤ C, uniformly in ε,
  for spread orthonormal (S_1, S_2, W), where A(σ) = (y − p′σ_1² − sσ_2² − ℓ·σ)/(2κσ_1). At ε = 0 this is the content of the proof of Prop 5.4.

## 4. Fixed r, and D ≠ 0

**Theorem 4.1 (definite, any r).** Let A = RΛRᵀ with all λ_k ≥ 1 (or all ≤ −1) and r ≥ 3. Then ‖p_Q‖ ≤ 304 for every b, c, n and r.

*Proof.* Use 1 × 1 pivots at threshold 1/2 (a_ii ≥ l_i); PSD Schur complements are PSD of rank one lower with all nonzero eigenvalues ≥ 1 (GEOM 1.5).
- Level 1: the pivot gives α₁ ≤ 4; otherwise (T2) gives α₁ ≤ 15.5.
- Level 2: (C2) gives 124; otherwise (T2) gives 27.4.
- Level 3: (C1) gives 8√2 √(124(1 + log 124)) = 304; otherwise (T2) gives ≤ 12. ∎

**Theorem 4.2 (exact rank r, all nonzero |eig| ≥ 1).**
- Let H = {l ≥ 1/4}. If λ_max(G_H) ≤ 1/2, then ‖p_Q‖ ≤ 8r/(r − 2) ≤ 24 for every linear term. (Condition on X_H; then G_L ≥ I/2, leverages are < 1/2 and det G_L ≥ 2^{−r}.)
- Otherwise, without pivots, Lemma 1.3 leaves at most ⌊r/2⌋ nearly isotropic hub directions.
- For r ≥ 4, the pivot branches need level two at rank r − 1 and level one at rank r − 2 with any linear terms. The light cases follow from (T2). The heavy null case reduces by Lemma 1.5 to α₁ of a discriminant with one large eigenvalue; a sketch via D₁ exists (PARTIAL).

**Remark 4.3 (D ≠ 0).**
- In the regime where the |A|-diagonal is small (spread), semidefinite/ Theorem 4 and structure/ Theorem S apply to D + RMRᵀ directly, since decoupling does not see D.
- Diagonal cancellation (Lemma 1.6) creates hubs whose light block carries a square along the partner plus a diagonal twist Σd_iX_i². This is (O2) with the outside linear term replaced by the twist. Prop 5.4 does not allow the twist, and Theorem H does not allow a partner that is also a square direction. Theorem H does cover the twist when that square is absent.

## 5. Numerics

The checks are Python with numpy, in `num/`, each run under 10 minutes at BelowNormal priority.
- The discriminant identities (errors ≤ 2·10⁻¹³); the identities (M⁻¹)₃₃ = −p′/κ² and (M⁻¹)₂₂ = 1/s at M_33 = 0 (error 5·10⁻¹⁰); interlacing (no violation in 20 000 instances).
- `hub_leak.py`: a fibre estimator for Q = 2κS_1(√l X_h + εW) + pS_1² + sS_2² + m₀Z² with n = 40 and uniform or comb hub laws. The peak density does not grow as ε ↓ 0: for example 2.86, 2.95, 2.95, 2.93 and 3.59, 3.63, 3.66, 3.88 at ε = 0, 0.05, 0.2, 0.5. These test matrices were not normalized to |eig| ≥ 1; the check concerns only the dependence on ε.

## 6. Status

| Result | Status |
|---|---|
| Lemmas 1.1–1.6 | PROVED |
| Propositions 2.1–2.2, Theorem 2.3 | PROVED |
| Theorem 3.1 (a), (b), (c1), (c2), (c3), (c4), (c5) | PROVED (c5 is Theorem C) |
| Theorem 4.1 | PROVED |
| Theorem 4.2, first part | PROVED |
| Theorem 4.2, pivot branches for r ≥ 4 | PARTIAL |
| (O1)–(O3), estimate (LH) | OPEN |
| Density flat in ε for the leaking hub | NUMERICAL |
