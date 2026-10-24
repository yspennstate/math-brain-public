## Summary

**Status: PARTIAL.** We proved a loss-free decoupling bound at hubs, but only when the cross block between the two halves has low rank. The canonical case (star + rank one + εW) is still open: there εW couples the two halves, and I reduce that remainder to one stated estimate.

**What the decoupling loses, and where.** The Cauchy–Schwarz step |φ|² ≤ φ_D loses nothing: φ_D is exactly the characteristic function of the doubled form D. Theorem D loses at the next step, where it throws away the phase of the duplicated block. Kwan–Sauermann never throw that phase away. They push the loss to the last step and dilute it by squaring again and again. That dilution cannot help at a hub. Every copy of the hub coincides with its twin on the shared block (Lemma 3.1), so the loss grows with the number of copies and does not shrink as you iterate.

**Key new idea (Theorem 5.1).** Split into a shared block I and a duplicated block H ∪ J0, with H a set of hubs. Keep the phase of J0 and integrate each hub copy exactly, using f_h ≤ 1.
- The shared block's twist is removed by the differencing, so its characteristic function is integrable (Brascamp–Lieb).
- The duplicated block keeps an arbitrary twist, but it is only needed in L², and Plancherel is blind to twists. This is result N3 of twist_obstruction/.
- Young's inequality, in the difference of the two hub frequencies, pairs the two halves.

If A_{IJ0} has rank r, then |φ(t)| ≤ C(2|t|)^{−|H|−r/2}. This holds for arbitrary A_II, A_J0J0, A_HH, hub diagonals and linear terms. One hub with r = 1 gives density ≤ 6(|λ|√(det G_I det G_J))^{−1/3}. With r = 0 the hub alone decays at its true rate 1/|t|, whatever uncoupled forms sit on the two halves. The class is the same as the twist record's hub block lemma (N8), reached by an independent route with no Fresnel step, at the price of a leverage condition on I.

**Also proved.**
- Proposition 4.1: an identity in which the sum of the two hub copies enters through the ambiguity function of the hub law.
- Theorem 6.1: a dense twist is allowed in the cross block, provided a third block carrying the hub row is uncoupled from I. Then |φ| ≲ |t|^{−5/4}, which is integrable.

**Checks.** Every factor of Theorem 5.1 was re-derived. The Monte Carlo run (dense twists of norm 0, 1, 3 inside the halves) stays below the bound at every t tested. It is a weak check: beyond t ≈ 8 the values sit at the Monte Carlo floor, so it could only have failed below t ≈ 8. Nothing uses the pointwise Rudelson–Vershynin bound; only Lᵖ bounds, Plancherel, projection bounds and Brascamp–Lieb.

**Where it stops (canonical case).** εW couples every pair of blocks that carry the hub row.
- The part aligned with the hub partner defeats every Fourier L¹ bound for bumpy laws. It has to go into a real-variable hub step.
- The non-aligned part reduces to the estimate Ω < ∞ in §7.3, a Fourier bound on slices of a product measure. That is conjectural; we have no proof.

**Most useful next step.** Absorb the aligned component into the (X_h, L) block by the change of variables of geometric Proposition 5.4. Then prove Ω < ∞ for |t| ≤ 1/(λ‖εW‖_F); above that, Theorem D already integrates to O(λ^{−1/2}).

---

# Decoupling at hubs: where the square-root loss sits, and a loss-free version

## 0. Setting and summary

X = (X_1, ..., X_n) has independent coordinates with densities f_i ≤ 1 and characteristic functions ψ_i. Q = XᵀAX + bᵀX + c, φ(t) = E exp(itQ). For a set S of coordinates, X_S is the subvector and Ψ_S(η) = ∏_{i∈S} ψ_i(η_i). A hub is a coordinate h. Its row is w = (A_{hj})_{j≠h}, and w_S is its restriction to S; L_S = ⟨w_S, X_S⟩.

**Results.**

1. Weyl differencing |φ|² ≤ φ_D is exact on its right side: φ_D is the characteristic function of the doubled form D. At a hub, Theorem D loses at the next step, where it removes the phase exp(it(q_J(X_J) − q_J(X'_J))) (Section 2).
2. The Kwan–Sauermann scheme does not avoid the loss. It carries the loss to the last step and dilutes it by repeated squaring. At a hub the loss is proportional to the number of hub copies, so the dilution does not remove it (Lemma 3.1).
3. Theorem 5.1 (loss-free decoupling at hubs). Suppose the coordinates split into a shared block I and a duplicated block H ∪ J0, with H a set of hubs, and the cross block A_{IJ0} has rank r. Then |φ(t)| ≤ C(2|t|)^{−|H|−r/2} with an explicit C, whatever A_II, A_{J0J0}, A_HH and the linear terms are. Dense twists are allowed inside both blocks. Each hub counts with full weight |t|^{−1} and each cross direction with |t|^{−1/2}; for one hub and r = 1 the density is at most 6(|λ|(det G_I det G_J)^{1/2})^{−1/3}.
   - Differencing removes the twist of the shared block, whose characteristic function is then in L¹ (Brascamp–Lieb).
   - The duplicated block keeps its phase and is paid for only in L², which no twist can inflate (Plancherel).
   - Young's inequality, in the difference of the two hub frequencies, pairs the two.
4. Proposition 4.1: an identity in which the sum of the two hub copies enters through the ambiguity function of the hub law. Theorem 6.1: a dense cross block is allowed if a third block carrying the hub row is uncoupled from the shared block; then |φ| ≤ C|t|^{−5/4}.
5. The canonical case star + rank one + εW is not settled: there εW always couples the shared and duplicated blocks. Section 7 isolates the two parts of that coupling.
   - The part aligned with the hub partner defeats every Fourier L¹ argument for bumpy laws and must be treated in physical space.
   - The non-aligned part reduces to a precise open estimate.

**Status labels.** Lemma 2.1, Lemma 3.1, Proposition 4.1, Theorems 5.1 and 6.1: PROVED. Section 7: the obstruction is PROVED to be present in the method (7.2); the missing estimate is CONJECTURAL (7.3).

## 1. Tools

**(T1)** (Lemma 1 of the record.) If |g| ≤ f ≤ 1, f a probability density, and p ≥ 2, then ∫|ĝ|^p ≤ 4π/√p.

**(T2)** (Ball; Livshyts–Paouris–Pivovarov.) If P is n × k of rank k, the density of PᵀX is at most 2^{k/2} det(PᵀP)^{−1/2}. (PᵀX = G^{1/2}Y with G = PᵀP, where Y is the coordinates of X in an orthonormal basis of the column space; Y has density ≤ 2^{k/2}.)

**(T3)** (Frame Brascamp–Lieb, as in Theorem F.) Let ρ_i ∈ R^k (i ∈ S) be the rows of an |S| × k matrix Q_S, with G = Q_SᵀQ_S invertible and leverages c_i = ρ_iᵀG^{−1}ρ_i ≤ 1/2. Then for every β ∈ R^S,

  ∫_{R^k} ∏_{i∈S} |ψ_i(⟨ρ_i, v⟩ + β_i)| dv ≤ (4π)^k det(G)^{−1/2}.

*Proof.* Put v = G^{−1/2}v'. Then ⟨ρ_i, v⟩ = √c_i ⟨u_i, v'⟩ with unit vectors u_i and Σ c_i u_i u_iᵀ = I. Rows with c_i = 0 contribute factors ≤ 1. The geometric Brascamp–Lieb inequality (Ball, Barthe) is invariant under translating each argument, so the integral is at most

  ∏_i (c_i^{−1/2} ∫|ψ_i|^{1/c_i})^{c_i}.

(T1) with p = 1/c_i ≥ 2 bounds each factor by (4π)^{c_i}, and Σ c_i = k. ∎

**(T4)** (Plancherel for twisted characteristic functions.) Let P be n × k of rank k and Φ any real measurable function of X. Then

  ∫_{R^k} |E exp(i⟨Pu, X⟩ + iΦ(X))|² du ≤ (2π)^k 2^{k/2} det(PᵀP)^{−1/2}.

*Proof.* The map u ↦ E exp(i⟨u, PᵀX⟩ + iΦ(X)) is the Fourier transform of the complex measure m(z)dz = E[e^{iΦ(X)}; PᵀX ∈ dz], and |m| ≤ p_{PᵀX}. By Plancherel the integral equals (2π)^k‖m‖₂² ≤ (2π)^k ‖p‖_∞ ∫p, and (T2) bounds ‖p‖_∞. No condition on Φ is needed. (This is the L² twist lemma of the twist record.) ∎

## 2. Where the loss sits

**Lemma 2.1.** For a split [n] = I ∪ J, let X'_J be an independent copy of X_J. Put D = Q(X_I, X_J) − Q(X_I, X'_J), q_J(x) = xᵀA_JJ x + b_Jᵀx and Φ_J(t; x_I) = E exp(itQ(x_I, X_J)). Then

  |φ(t)|² ≤ E_{X_I}|Φ_J(t; X_I)|² = φ_D(t) = E[exp(it(q_J(X_J) − q_J(X'_J))) Ψ_I(2t A_IJ(X_J − X'_J))].

*Proof.* φ = E_{X_I}Φ_J and Cauchy–Schwarz give the inequality, and E|Φ_J|² = E exp(itD) by independence. In D the block A_II and the coefficient b_I cancel, leaving D = 2X_IᵀA_IJ(X_J − X'_J) + q_J(X_J) − q_J(X'_J); take the expectation over X_I first. ∎

Theorem D bounds φ_D by E|Ψ_I(2tA_IJ W)| with W = X_J − X'_J, i.e. it discards the phase of q_J. At a hub this is where the loss occurs, not in the Cauchy–Schwarz step.

Heuristically, take Q = 2X_hL + λV² with h ∈ J. Then D = [2X_hL + λV²] − [2X'_hL' + λV'²], where L' = L_I + L'_J and V' = V_I + V'_J. This form has two hubs and a rank-two part, so its characteristic function should decay like |t|^{−3} (= |φ|² for the true decay |t|^{−3/2}). The phase-free bound sees only the rank-two cross block and gives |t|^{−2}, i.e. |φ| ≲ |t|^{−1}, which is not integrable. Theorem 5.1 turns this into a proof.

## 3. The Kwan–Sauermann scheme and its continuous translation

**3.1. The mechanism** (arXiv 2312.13826, Section 3). Let X = Σ ξ_i a_i ∈ R^r with Rademacher ξ_i and t disjoint bases among the a_i, and let Z be a quadric on a (d+1)-dimensional affine subspace W. Then P(X ∈ Z) ≤ 2^{dr+1} t^{−(r−d)/2}, the rate of a d-dimensional subspace. The proof is an induction on d.
- Reducible quadrics and cylinders are handled directly.
- Otherwise, for x ≠ y, (Z − x) ∩ (Z − y) is a quadric on a d-dimensional affine subspace. With X = X_I + X_J,

  P(X ∈ Z)² ≤ P(X_J ∈ (Z − X_I) ∩ (Z − X'_I), X_I ≠ X'_I) + P(X ∈ Z) P(X'_I = X_I).

- The main term is nonzero only if X_I − X'_I lies in the linear space parallel to W (probability t^{−(r−d−1)/2}). Then X_J must lie in a quadric of one dimension less (probability t^{−(r−d+1)/2} by induction). The product is (t^{−(r−d)/2})²: no loss.

The quadratic equation is never dropped. Each differencing turns it into one linear equation on X_I − X'_I and a quadric of one dimension less.

**3.2. Unbounded rank** (Section 4 there). Let f(k, s) be the supremum of P(Q = 0, Mξ = w) over M of robust rank k, with Q nondegenerate modulo (M, M)-perturbations (A and A + LM + MᵀR define the same quadric on {Mx = w}). The recursion is

  f(k,s)² ≲ s^{−k/2} f(k+1, s) + (degenerate terms of order s^{−(k+2)/2}).

After m steps, dropping the quadratic equation (f(m) ≤ s^{−m/2}) costs s^{1/2} at level m, hence s^{1/2^{m+1}} at level 0. The loss is carried to the end and diluted, and m ~ log log s makes it O(1).

**3.3. Translation.** The events become joint densities p_{(Q, MX)}(z, w). The differencing identity is

  E_{X_I}[p_{(Q,MX)|X_I}(z, w)²] = density of (Q(X_I,X_J), MX, D, M_J(X_J − X'_J)) at (z, w, 0, 0),

with D linear in X_I given (X_J, X'_J).

The (M, M)-perturbation lemma is exact in physical space: on the slice {MX = w}, a twist of the form LM + MᵀR is a linear term. It has no Fourier counterpart. In Fourier L¹ bounds a twist component along the integrated directions is not harmless (Section 7.2).

In Fourier form, dropping the quadratic equation at the end costs one factor |t| in φ_{D_m}, i.e. |t|^{2^{−m}} in |φ|. The dilution would work if every intermediate step were lossless.

**Lemma 3.1 (hub copies coincide on shared blocks).** Let D_0 = Q and D_j = D_{j−1}(X_{S_j}, X_{T_j}) − D_{j−1}(X_{S_j}, X''_{T_j}), with S_j shared, T_j duplicated, and every copy of the hub h kept in T_j. The 2^m copies h^σ (σ ∈ {0,1}^m) in D_m have coefficient rows on S_m that depend only on (σ_1, ..., σ_{m−1}), up to sign.

*Proof.* The two copies created at step m from a copy h^τ are h^τ (in T_m) and its duplicate (in T''_m). Their rows on S_m are the row of h^τ restricted to S_m, with signs + and −, because S_m is not duplicated. ∎

*Consequence.* A bound that removes the phase of the last duplicated block sees each pair only through its difference: at most 2^{m−1} hub directions out of 2^m copies. Each hub copy is worth |t|^{−1} in φ_{D_m}, so the loss is |t|^{2^{m−1}} in φ_{D_m}, i.e. |t|^{1/2} in |φ|, for every m. The dilution of 3.2 removes a loss of one unit, but the hub loss grows with the number of copies. What removes it is to integrate both copies exactly and keep the phase of the duplicated block (Sections 4 and 5).

**3.4. The "Fourier-space decoupling" remark.** Kwan–Sauermann note that decoupling in Fourier space can lose less. That happens when the decoupled bound has Gaussian form exp(−ct²s²), where a square root only changes c. For densities ≤ 1 the decay after decoupling is polynomial. It comes from the density of W = X_J − X'_J near 0, and a square root halves the exponent. So the remark gives nothing here.

## 4. The hub-integrated identity

**Proposition 4.1.** Let h have A_hh = a, row w and linear coefficient b_h. Let I, J0 partition the other coordinates, with I shared and J = {h} ∪ J0 duplicated. Put
- σ = X_h − X'_h and μ = (X_h + X'_h)/2;
- W0 = X_J0 − X'_J0 and U0 = X_J0 + X'_J0;
- Δ = ⟨w_J0, W0⟩ and Σ = ⟨w_J0, U0⟩;
- M = A_{IJ0} and q0(x) = xᵀA_{J0J0}x + b_J0ᵀx;
- F_σ(μ) = f_h(μ + σ/2) f_h(μ − σ/2) and F̂_σ(s) = ∫F_σ(μ)e^{isμ}dμ (the ambiguity function of f_h).

Then

  φ_D(t) = E_{X_J0, X'_J0}[e^{it(q0(X_J0) − q0(X'_J0))} ∫dσ e^{itσ(Σ + b_h)} Ψ_I(2t(σw_I + MW0)) F̂_σ(2t(Δ + aσ))],

and consequently

  |φ(t)|² ≤ ∫dσ E_{W0}[|Ψ_I(2t(σw_I + MW0))| |F̂_σ(2t(Δ + aσ))|].  (4.1)

Moreover |F̂_σ| ≤ g_h(σ) := (f_h ∗ f̃_h)(σ) ≤ 1, ∫g_h = 1, and ∫|F̂_σ(s)|²ds ≤ 2π g_h(σ).

*Proof.* With X_h = μ + σ/2 and X'_h = μ − σ/2 (Jacobian 1),

  D = 2σL_I + 2μΔ + σΣ + b_hσ + 2aμσ + 2X_IᵀMW0 + q0(X_J0) − q0(X'_J0),

since 2X_h(L_I + L_J0) − 2X'_h(L_I + L'_J0) = 2σL_I + 2μΔ + σΣ and a(X_h² − X'_h²) = 2aμσ. The expectation over X_I gives Ψ_I(2t(σw_I + MW0)); the one over μ gives F̂_σ(2t(Δ + aσ)). In (4.1) the absolute values remove every phase. What remains depends on (X_J0, X'_J0) only through W0, whose coordinates are independent with densities g_j = f_j ∗ f̃_j ≤ 1.

For the bounds: |F̂_σ| ≤ ∫F_σ = g_h(σ) ≤ ‖f_h‖_∞ = 1. Plancherel and F_σ ≤ 1 give ∫|F̂_σ|² = 2π‖F_σ‖₂² ≤ 2π g_h(σ). ∎

Neither A_II nor A_{J0J0} appears in (4.1), and the hub is seen twice:
- the difference σ through its bounded density (the Theorem H mechanism, robust to rough hub laws);
- the sum through F̂_σ, which is controlled only in L². For the uniform law F_σ is an interval indicator and F̂_σ is not integrable.

## 5. Loss-free decoupling at hubs

**Theorem 5.1.** Let H be a set of coordinates, let I and J0 be disjoint sets of coordinates disjoint from H, and let K be the rest. For h ∈ H let w^(h) be the row of h. Suppose

  A_{IJ0} = Σ_{k=1}^r λ_k a_k b_kᵀ  (a_k ∈ R^I, b_k ∈ R^{J0}, λ_k ≠ 0, r ≥ 0).

Put Q_I = [w_I^(h) (h ∈ H), a_1, ..., a_r], an |I| × (|H| + r) matrix, and G_I = Q_IᵀQ_I. Put Q_J = [w_J0^(h) (h ∈ H), b_1, ..., b_r] and G_J = Q_JᵀQ_J. Assume G_I and G_J are invertible and every row of Q_I has leverage ≤ 1/2. Then for every t ≠ 0,

  |φ(t)|² ≤ (2|t|)^{−2|H|−r} (2π)^{|H|} (4π)^{|H|+r} 2^{(|H|+r)/2} (|λ_1⋯λ_r| (det G_I det G_J)^{1/2})^{−1},

for all blocks A_HH, A_II, A_{J0J0}, all blocks involving K, and all linear and constant terms.

**Corollary 5.2.**
- One hub and r = 1: ‖p_Q‖_∞ ≤ 6(|λ_1|(det G_I det G_J)^{1/2})^{−1/3}.
- One hub and r = 0: |φ(t)| ≤ (2|t|)^{−1}(8√2 π²)^{1/2}(|w_I|²|w_J0|²)^{−1/4}. The hub decays at its true rate |t|^{−1}, whatever quadratic forms sit inside I and inside J0, provided they are not coupled.

*Proof.*

*Step 0 (conditioning).* Given X_K the form is a quadratic polynomial in the other coordinates with the same blocks A_HH, A_{H, I∪J0}, A_II, A_{IJ0}, A_{J0J0}; only linear and constant terms change. Since |φ(t)| ≤ E_{X_K}|E[e^{itQ} | X_K]|, it suffices to treat K empty, with arbitrary linear terms.

*Step 1 (differencing).* Lemma 2.1 with I shared and J = H ∪ J0 duplicated gives |φ(t)|² ≤ φ_D(t) = E_{X_I}|Φ_J(t; X_I)|².

*Step 2 (integrating the hubs).* For fixed x_I write

  Q = x_HᵀA_HH x_H + 2⟨x_H, l_I + W_J0ᵀX_J0⟩ + ⟨β, x_H⟩ + X_J0ᵀB X_J0 + ⟨2A_{J0I}x_I + b_J0, X_J0⟩ + κ(x_I),

where B = A_{J0J0}, l_I = (⟨w_I^(h), x_I⟩)_h, W_J0 is the J0 × H matrix with columns w_J0^(h), and κ collects the terms in x_I only. Define 𝒜(η) = E exp(i⟨η, X_J0⟩ + itX_J0ᵀB X_J0) for η ∈ R^{J0}. Then

  Φ_J(t; x_I) = e^{itκ(x_I)} ∫_{R^H} ∏_h f_h(x_h) e^{it(x_HᵀA_HH x_H + ⟨β, x_H⟩)} e^{2it⟨x_H, l_I⟩} 𝒜(2tW_J0 x_H + τ(x_I)) dx_H,  τ(x_I) = 2tA_{J0I}x_I + t b_J0.

Expand |Φ_J|² as a double integral over (x_H, x'_H), take the expectation over X_I inside (Fubini: bounded integrand, integrable weight), and substitute y = 2tx_H, y' = 2tx'_H. This gives

  φ_D(t) = (2|t|)^{−2|H|} ∫∫ ∏_h f_h(y_h/2t) f_h(y'_h/2t) e^{iθ(y,y')} F(y, y') dy dy',
  F(y, y') = E_{X_I}[e^{i⟨y − y', L_I^H⟩} 𝒜(W_J0 y + τ(X_I)) conj 𝒜(W_J0 y' + τ(X_I))],

with L_I^H = (⟨w_I^(h), X_I⟩)_{h∈H} and θ a real phase. Since f_h ≤ 1 and φ_D ≥ 0,

  |φ(t)|² ≤ (2|t|)^{−2|H|} ∫∫|F(y, y')| dy dy'.  (5.1)

The block A_HH and the hub linear terms went into θ.

*Step 3 (the shared block enters through a low-dimensional projection).* Put Z = (⟨a_k, X_I⟩)_{k≤r}. Then τ(X_I) = 2tΣλ_k Z_k b_k + t b_J0 depends on X_I only through Z. Let B(y, ζ) = 𝒜(W_J0 y + Σζ_k b_k + t b_J0), and let p(l, z) be the density of (L_I^H, Z) = Q_IᵀX_I, which exists because Q_I has full column rank. With p̂_z(s) = ∫e^{i⟨s,l⟩}p(l, z)dl,

  F(y, y') = ∫_{R^r} p̂_z(y − y') B(y, 2tΛz) conj B(y', 2tΛz) dz,  Λ = diag(λ_k).

*Step 4 (Young).* For k, g ≥ 0, ∫∫k(y − y')g(y)g(y') = ⟨g, k ∗ g⟩ ≤ ‖k‖₁‖g‖₂². Hence

  ∫∫|F| ≤ ∫‖p̂_z‖₁ ‖B(·, 2tΛz)‖₂² dz ≤ sup_z‖p̂_z‖₁ · (2|t|)^{−r}|det Λ|^{−1} · ∫_{R^{|H|+r}} |B|².

*Step 5a (shared side, L¹).* Fourier inversion in z gives p̂_z(s) = (2π)^{−r}∫_{R^r} Ψ_I(Q_I(s, u)) e^{−i⟨u,z⟩} du. By (T3) this is integrable and the inversion is legitimate, and

  sup_z‖p̂_z‖₁ ≤ (2π)^{−r}∫|Ψ_I(Q_I v)| dv ≤ (2π)^{−r}(4π)^{|H|+r} det(G_I)^{−1/2}.

The twist A_II was removed by the differencing, so this concerns only a projection of the product measure on I.

*Step 5b (duplicated side, L²).* B(y, ζ) = E exp(i⟨Q_J(y, ζ), X_J0⟩ + it(X_J0ᵀB X_J0 + ⟨b_J0, X_J0⟩)), so by (T4)

  ∫|B|² ≤ (2π)^{|H|+r} 2^{(|H|+r)/2} det(G_J)^{−1/2},

whatever B = A_{J0J0} is.

*Step 6.* Insert Steps 4–5 into (5.1). For |H| = r = 1 this gives |φ(t)| ≤ K(2|t|)^{−3/2} with K = 8π^{3/2}X^{−1/2} and X = |λ_1|(det G_I det G_J)^{1/2}. Since ∫min(1, C|t|^{−3/2}) = 6C^{2/3},

  ‖p_Q‖_∞ ≤ (2π)^{−1}∫|φ| ≤ (3/(2π))K^{2/3} = 6X^{−1/3}. ∎

**Remarks.**
1. Theorem H needs the block of the hub partners to be low rank plus diagonal. Theorem 5.1 needs only the cross block between the halves to be of low rank; inside each half the form is arbitrary. This is the class of the twist record's hub block lemma (N8), which is proved there by Fresnel linearisation and Plancherel and needs no leverage condition. The proof here has no Fresnel step and needs leverages ≤ 1/2 on the shared half only.
2. This is the continuous form of "keep the quadratic equation". The duplicated half is never replaced by its modulus: its phase stays inside 𝒜 and is paid for in L². The shared half supplies an L¹ kernel in y − y', and each hub copy contributes (2|t|)^{−1}.
3. Numerical check (check_thm51.py): one hub, r = 1, 8 + 8 coordinates, uniform laws, and dense twists of operator norm 0, 1 and 3 inside each half. The Monte Carlo |φ(t)| lies below the bound for t = 2, ..., 64, by a factor ≥ 3 for t ≤ 8. Beyond t = 8 the values are at the Monte Carlo floor (5·10⁻⁴), so the check had no room to fail there.

## 6. The sum copy in L²: dense cross blocks

**Theorem 6.1.** Let h be a hub with row w and any diagonal a, and let I, J_V, J_L be disjoint sets of the other coordinates (the rest conditioned on). Suppose A_{IJ_L} = 0. Let

  Z_h = |w_I|² ‖P_{w_I⊥} A_{IJ_V}‖_F²,

the sum of the squared 2 × 2 minors of [w_I | A_{IJ_V}] that contain the column w_I. Let α_i be the volume-sampling marginals of these minors on I, and assume α_i ≤ 1/2. Then

  |φ(t)|² ≤ (4π)² e^{1/2} (2|t|)^{−2} Z_h^{−1/2} · 2^{1/4}|w_{J_L}|^{−1/2} (π/|t|)^{1/2},

so |φ(t)| ≤ C|t|^{−5/4} and the density is bounded. The blocks A_II, A_{J_VJ_V}, A_{J_VJ_L}, A_{J_LJ_L} and A_{IJ_V} are arbitrary: a dense twist is allowed everywhere except between I and J_L.

*Proof.* Apply (4.1) with J0 = J_V ∪ J_L. Since A_{IJ_L} = 0, Ψ_I depends only on (σ, W_V). Fix (σ, W_V) and let x_L = ⟨w_{J_L}, W_L⟩, whose density is ≤ √2/|w_{J_L}| by (T2). By Cauchy–Schwarz,

  E_{W_L}|F̂_σ(2t(x_L + const))| ≤ ‖p_{x_L}‖₂ (2|t|)^{−1/2}‖F̂_σ‖₂ ≤ (√2/|w_{J_L}|)^{1/2}(π/|t|)^{1/2}.

What remains is R(t) = ∫dσ E_{W_V}|Ψ_I(2t(σw_I + A_{IJ_V}W_V))|, a Brascamp–Lieb integral over (σ, W_V) in which σ carries Lebesgue measure. By Lieb's theorem it suffices to test centred Gaussians, with weights d_i on the rows and e_j on the coordinates of W_V.
- Cauchy–Binet, keeping only the terms whose I-rows form a 2 × 2 minor containing w_I, and weighted AM–GM with volume-sampling weights give det ≥ Z_h ∏d_i^{α_i} ∏e_j^{1−β_j}. Here β_j is the probability that the minor uses column j, so Σβ_j = 1.
- All Gaussian parameters cancel as in Theorem D, and (T1) gives R(t) ≤ (4π)²(2|t|)^{−2} Z_h^{−1/2} ∏(1−β_j)^{−(1−β_j)/2} ≤ (4π)² e^{1/2}(2|t|)^{−2} Z_h^{−1/2}.

When a ≠ 0 the argument of F̂_σ is shifted by aσ, which the L² bound does not see. ∎

**Remark.** Treating |F̂_σ(2tΔ)| as a function in L²(R²) (exponent 1/2) makes the Brascamp–Lieb constant infinite for total ψ-exponent 2 whenever the ψ-rows span only the directions σ and ⟨v, W0⟩. On their common kernel V0 (dimension m − 1), the Bennett–Carbery–Christ–Tao condition requires m − 1 ≤ Σ(1 − β_j) + 1/2 = m − 3/2. So L²(R²) counts σ twice. The right norm is the mixed norm sup_σ‖F̂_σ(2t·)‖₂, for which the count on V0 is exactly balanced, and the proof above is a proof of the mixed-norm inequality in the uncoupled case.

## 7. What does not transfer: the dense coupling between the halves

**7.1. The canonical family.** For Q = 2X_hL + λV² + εX'ᵀWX' with W dense, every set carrying a fixed fraction of |w|² is coupled to every other such set by εW. So A_{IJ0} = λv_I v_J0ᵀ + εW_{IJ0} has full rank for every split, and neither Theorem 5.1 nor Theorem 6.1 applies. (If ‖εW_{IJ}‖_F ≳ 1 for some split, Theorem D applies; the open case is ‖εW‖_F ≲ 1.) The coupling enters Theorem 5.1 through τ(X_I) = 2tA_{J0I}X_I, which is then of high rank.

**7.2. The aligned component.** The part θL_I L_J0 of the coupling, from θL² with θ ~ ε wᵀWw, shifts the hub frequency: F contains 𝒜((y + 2tθL_I)w_J0 + ...), and is no longer of the form ∫p̂_z(y − y')G_z(y) conj G_z(y') dz.

Undoing the shift turns the sum factor of Proposition 4.1 into the ambiguity function of f_h along a tilted line: A_f(σ ∓ κs, s) = A_{Uf}(σ, s), with U the Fresnel propagator at time κ = θ/(2t). (A chirp e^{−iκξ²/2} on f̂ multiplies f̂(ξ + s/2) conj f̂(ξ − s/2) by e^{−iκξs}.) Its L² norm along the line is at most (2π)^{1/2}‖Uf‖₄². That is bounded for the uniform law but not for densities ≤ 1 in general: sets of many narrow pieces arranged as a zone plate focus under U. This matches the twist record's counterexample for rank-one twists along an integrated direction (laws made of narrow bumps).

On average over t it is controlled by the one-dimensional Strichartz estimate ‖U_κ f‖_{L⁸_κL⁴_x} ≲ ‖f‖₂ (Hölder with exponents 8 and 8/7 against |t|^{−5/4}); this is a sketch only. In physical space the component is harmless, since the block of (X_h, L) is [[a, 1], [1, θ]], of determinant of order one. It belongs in a real-variable hub step (the change of variables of geometric Proposition 5.4), not in a Fourier bound.

**7.3. The non-aligned component (missing estimate, CONJECTURAL).** Let E: R^I → R^{J0} satisfy Ew_I = 0, Eᵀw_J0 = 0 and ‖E‖ ≤ ε, i.e. no component along the hub partner on either side. Repeat Steps 3–4 of Theorem 5.1 with τ = 2t(λV_I v_J0 + EX_I), conditioning on (V_I, τ). This gives

  ∫∫|F| ≤ (2|t||λ|)^{−1}(2π)² 2 det(G_J)^{−1/2} Ω,  Ω = ∫dτ sup_z ‖∫e^{isl} p(l, z, τ) dl‖_{L¹(ds)},

where p is the joint density of (L_I, V_I, 2tEX_I). If EX_I were independent of (L_I, V_I), Ω would equal sup_z‖p̂_z‖₁ and Theorem 5.1 would extend. For a product measure, orthogonal linear forms are uncorrelated but not independent, and Ω is a Fourier bound on slices of a product measure. This is the form open case (a) takes on the decoupling side: a slice-Fourier (mixed-norm) estimate, uniform in the dimension of EX_I. It is the analogue of the Kwan–Sauermann robust-rank inheritance, and we have no proof.

## 8. Next step

1. Split the dense coupling into its aligned and non-aligned parts.
2. Absorb the aligned part into the (X_h, L) block by the real-variable change of variables of geometric Proposition 5.4.
3. For the non-aligned part, either prove Ω < ∞ for |t| ≤ 1/(λ‖εW‖_F), or extend the twist record's coupling-gain lemma to small non-aligned couplings. Above that range, Theorem D already integrates to O(λ^{−1/2}).

Theorem 5.1 then covers the rest of the canonical case, for every hub diagonal.

---
