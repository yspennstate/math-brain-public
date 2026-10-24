## Summary

**Status: FALSE as asked, with a PROVED replacement.** No smallness condition on E makes the twist lemma true, because any twist lying along range(P) is fatal however small it is. What is true is a block version: a twist is harmless whenever the coordinates split into two blocks with no coupling between them, whatever the twist does inside each block. It needs no leverage condition, and it has a hub version that extends Theorem H.

**Key new idea.** Plancherel makes the L² norm of a twisted characteristic function blind to the twist. It is bounded by the density of the k-dimensional projection, whatever the phase is. An L¹ bound then follows by Cauchy–Schwarz between two independent blocks. What breaks L¹ is a law made of many narrow, separated bumps: the aligned twist moves each bump's Fourier transform to its own place, so the cancellation between them disappears. The Gaussian model does not show this.

**Next step.** A real-variable lemma for the pair (X_h, L) with a dense remainder, i.e. GEOM Prop 5.4 extended to Q = 2X_hL + cL² + λV² + (dense part not a function of L, V). Or else a proof that the non-aligned coupling of a dense W controls its aligned cross-block part.

---

# Twisted Fresnel integrals: an obstruction and a block lemma

## 0. Setting

X has independent coordinates with densities f_i ≤ 1. P is an n×k matrix of rank k with rows ρ_i, G = PᵀP, and c_i = ρ_iᵀG⁻¹ρ_i are the leverages. Z = PᵀX. For a symmetric E put

- T_E(u) = E exp(i⟨Pu,X⟩ + i XᵀEX),
- J(E) = ∫_{ℝᵏ} |T_E(u)| du.

For a set of coordinates S, write G_S = P_SᵀP_S. Theorem F gives J(D) ≤ (4π)ᵏ det(G)^{-1/2} for every diagonal D when all c_i ≤ 1/2.

## 1. Obstruction

**Gaussian model.** For X ~ N(0, s²I), k = 1 and E = κvvᵀ, one has J = √(2π)/s · (1+4s⁴κ²)^{1/4} ≤ √(2π)/s + 2√(π|κ|), bounded uniformly in s. Large variance is not what inflates J.

**Theorem 1.** Let p = Pe be a unit vector with every p_i ≠ 0, and κ ≠ 0. Put s₀ = 1/(N√(2π)). For every N there are laws with densities ≤ 1 such that

J(κppᵀ) ≥ (1 − 2η)(1+4κ²s₀⁴)^{-1/4} (2πN)ᵏ det(G)^{-1/2},

with η = P(|g| ≥ 10(1+4κ²s₀⁴)^{-1/2}). We have η ≤ 2·10⁻¹² once N⁴ ≥ κ²/π². For the same laws J(0) ≤ (4π)ᵏ det(G)^{-1/2} when c_i ≤ 1/2.

So ‖E‖ ≤ δ, ‖EP‖ ≤ δ, ‖PᵀEP‖ ≤ δ and |θ|‖E‖_F ≤ 1 all fail, for every δ > 0.

*Proof.*
1. **Laws.** Put D = 10√(2π)N/|κ|. Let f_i = N⁻¹ Σ_{q<N} γ_{s₀}(x − a_{iq}) with a_{iq} = qN^{i−1}D/p_i and γ_{s₀} the N(0, s₀²) density. Each bump has height 1. Bumps of one coordinate are at least D apart, so f_i ≤ 1 + 4e^{−D²/8s₀²}. Rescaling X by that factor gives densities ≤ 1 and costs only a factor (1+δ)^{−k}, because the construction works for every κ.
2. **Components.** The law is the mixture, with weights N⁻ⁿ, of Gaussians N(μ_c, s₀²I). The numbers y_c = ⟨p, μ_c⟩ are distinct multiples of D.
3. **Modulus of one component.** Put w = u + 2κy_c e and γ₀ = s₀²/(1+4κ²s₀⁴) ≤ s₀². Then |T_c| = (1+4κ²s₀⁴)^{-1/4} exp(−wᵀMw/2), where M = Pᵀ[s₀²(I − ppᵀ) + γ₀ppᵀ]P. Since γ₀G ≤ M ≤ s₀²G, we get ‖T_c‖₁ ≥ (1+4κ²s₀⁴)^{-1/4}(2πN)ᵏ det(G)^{-1/2}.
4. **Disjoint windows.** Let l(u) = ⟨Pᵀp, u⟩. Since ⟨Pᵀp, e⟩ = 1, we have l(u) = l(w) − 2κy_c. The sets U_c = {|l(u) + 2κy_c| < |κ|D} are disjoint. Under the weight exp(−wᵀMw/2), l(w) has variance at most γ₀⁻¹, so the mass of T_c outside U_c is at most η‖T_c‖₁.
5. **Conclusion.** J ≥ Σ_c N⁻ⁿ(∫_{U_c}|T_c| − ∫_{U_cᶜ}|T_c|) ≥ (1 − 2η) min_c ‖T_c‖₁. ∎

*Remarks.*
- Small leverages do not help: p = (1,…,1)/√n gives the same bound.
- With complex weights g_i = e^{iκp_i²x²}f_i, the same bound holds for the zero-diagonal twist κ(ppᵀ − diag p_i²).
- The hub version holds too: p = w/|w| lies in the range of Theorem H's frame [V, A_{MH}].

## 2. The L² norm does not see the twist

**Lemma 2.** For any real function φ of X,

∫|E e^{i⟨u,Z⟩ + iφ(X)}|² du ≤ (2π)ᵏ ‖p_Z‖_∞ ≤ (2π)ᵏ 2^{k/2} det(G)^{-1/2}.

*Proof.* The function is the Fourier transform of m(z) = E[e^{iφ} | Z = z] p_Z(z), and |m| ≤ p_Z. Apply Plancherel. For the density bound write Z = G^{1/2}Y, where Y is an orthogonal k-dimensional projection of X; Ball and Livshyts–Paouris–Pivovarov give p_Y ≤ 2^{k/2}. ∎

## 3. Block lemma

**Theorem 3.** Let [n] = K ∪ I ∪ J with G_K and G_I invertible and E_KI = 0. Then

J(E) ≤ (2π)ᵏ 2^{k/2} (det G_K det G_I)^{-1/4},

for arbitrary E_KK, E_II, E_KJ, E_IJ, E_JJ and any extra phase ψ(X_J). No leverage condition is needed.

*Proof.* Condition on X_J. The phase then splits into a function of X_K plus a function of X_I, because the K–I term vanishes. By independence the conditional expectation is a product A_K(u)·A_I(u). Apply Cauchy–Schwarz in u, then Lemma 2 to each block. ∎

*Remarks.*
- A random split of a spread frame has G_K ≈ G_I ≈ G/2.
- Twists that look coupled can sometimes be uncoupled by a better split. For v = (1,1,1,1)/2 and w = (1,−1,1,−1)/2, 2κ⟨v,X⟩⟨w,X⟩ = κ((X₁+X₃)² − (X₂+X₄)²)/2, so K = {1,3}, I = {2,4} gives J ≤ 4π.

**Corollary 3.1 (Theorem F with a two-block remainder).** Let A = Σ_{k≤3} λ_k v_kv_kᵀ + B with B_KI = 0. Then

- |φ_Q(t)| ≤ (2π)^{3/2} |λ₁λ₂λ₃|^{-1/2} (det G_K det G_I)^{-1/4} |t|^{-3/2},
- ‖p_Q‖_∞ ≤ 6 |λ₁λ₂λ₃|^{-1/3} (det G_K det G_I)^{-1/6}.

*Proof.* Fresnel-linearize the three squares, then apply Theorem 3 with E = tB. ∎

**Corollary 3.2 (Theorem H with a two-block remainder).** Split the coordinates as H ∪ K ∪ I ∪ J and let A_MM = Σ_{k≤r} λ_k v_kv_kᵀ + B on M = K ∪ I, with B_KI = 0. Rows are ρ̃_i = ((v_k)_i, A_ih), m = r + |H|, and G̃_K, G̃_I must be invertible. Then

|φ_Q(t)| ≤ (2|t|)^{−|H|} Π_k (4π|tλ_k|)^{-1/2} (2π)^m 2^{m/2} (det G̃_K det G̃_I)^{-1/4},

with A_HH, everything touching J, B_KK and B_II arbitrary.

For one hub and one square this gives ‖p_Q‖_∞ ≤ 3·2^{2/3}|λ|^{-1/3}(det G̃_K det G̃_I)^{-1/6}, about 7.6|λ|^{-1/3} for a balanced split. So star + rank one + εW is bounded for every ε whenever W_KI = 0 on a split where both halves see v and w: block-diagonal or banded W, for instance. The compression of W along the hub direction then lies inside the blocks and is harmless.

## 4. Couplings that help

**Proposition 4.** Suppose E_KI = Σ_{l≤r} σ_l a_l b_lᵀ with σ_l > 0, a_l orthonormal, and Gram[P_K, a], Gram[P_I, b] invertible. Then

J ≤ (2π)^{k+r/2} 2^{(k+r)/2} (det Gram[P_K,a] · det Gram[P_I,b])^{-1/4} Π_l (2σ_l)^{-1/2}.

*Proof.* The coupling shifts the K-frequency by Σ ω_l a_l, where ω_l = 2σ_l⟨b_l, X_I⟩. Write T as an integral over ω, apply Cauchy–Schwarz in ω and then in u, and use Lemma 2 in k + r dimensions on each side. ∎

So large non-aligned couplings help. Aligned couplings make the Gram matrix singular; that is exactly the case of Theorem 1.

## 5. Consequence for star + rank one + εW

- **|t| ≥ 1/(ε‖W‖_F).** With the hub in J, Theorem D suffices, subject to its I-marginal condition.
- **|t| below that.** The obstruction is the aligned cross-block coupling P̃_KᵀW_{KI}P̃_I. Its component along the hub direction, from the L² term cL², cannot be Fresnel-linearized. Linearizing the pair (X_h, L) with matrix [[a_hh, 1], [1, c]] leaves the hub coordinate alone on one direction (leverage exactly 1), and in any split one half sees only one direction.
- **What this means.** A bound in terms of norms of E cannot close this case. What remains possible is either:
  - letting the non-aligned bulk of W control the aligned part. Heuristically it does: at the positions the construction of Theorem 1 needs, a dense W shifts each bump off the frame and kills it. For generic W, |wᵀWw| is of order n^{-1/2} while ‖Ww‖ is of order 1; or
  - a real-variable step for the pair (X_h, L).

## 6. Numerics

All values are exact up to quadrature: for Gaussian-mixture laws every twisted characteristic function is a finite sum of explicit complex Gaussians (gmix.py, which matches 2D quadrature to 1e-14).

- **Theorem 1** (n = 2, κ = 1, separation factor 8): J(κvvᵀ) = 12.57, 25.11, 37.65, 50.20, 75.30 for N = 2, 4, 6, 8, 12, i.e. J/2πN = 1.000 to 0.999. J(0) ≤ 2π for the same laws, and the maximum density is 1.000000. The window lower bound from the proof is within 0.2% of the exact value and does not depend on κ (31.3, 62.7, 125.3, 250.6 for N = 5, 10, 20, 40). With n = 4 (leverages 1/4) J/2πN ≈ 1.
- **Theorem 3** (n = 4, same laws): the aligned twist gives 12.57, 18.83, 25.10 for N = 2, 3, 4. The same twist cut into two blocks gives 0.79, 0.24, 0.10, against the bound 4π. Adding a non-aligned coupling σ = 0.1, 1, 10 keeps J ≤ 0.79.
- **Other twists** on these laws, which are tuned against aligned twists only (so this is not an adversarial test): the zero-diagonal twist, a dense twist with zero compression, and the cross twist all give J ≤ 2.1.

## 7. Status

- **PROVED:** Theorem 1, Lemma 2, Theorem 3, Corollaries 3.1–3.2, Proposition 4.
- **FALSE:** the twist lemma under any size condition on E.
- **CONJECTURAL:**
  - PᵀEP = 0 suffices, under a spreading condition;
  - small non-aligned couplings are harmless;
  - for dense generic W, the non-aligned coupling dominates the aligned cross-block part.
