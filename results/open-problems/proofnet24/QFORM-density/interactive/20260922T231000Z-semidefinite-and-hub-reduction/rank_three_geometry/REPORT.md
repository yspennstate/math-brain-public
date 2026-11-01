## Summary

**Status: PARTIAL, with the definite case PROVED.**
- **Proved:** definite rank-three forms have density ≤ 82 for every linear and constant term (≤ 12 when the linear part is in the range). So the spherical means of a 3D orthonormal projection satisfy M_{y0}(r) ≤ 6/(πr), uniformly in the centre.
- **Proved:** an indefinite rank-three form with any c-pivot has bounded density on both sides of the level set, for every linear term.
- **Still open:** rank three with no pivot and a row of leverage > 1/2. That row is then a hub, and this is the open configuration of a hub with one square and a rank-two twist. We reduced the light case of it to one named Fourier estimate (TW), which we tested numerically but did not prove.

**Key idea.** Conditioning on one coordinate leaves a rank-two form of an orthonormal 2D projection plus a linear form. For such forms a discriminant identity makes the conditional small-ball bound depend on one unit 1D projection only. This gives α₂ ≤ 87.3 for every rank-two matrix and every linear term, which is the missing (H2) ingredient the earlier record named.

**Pointwise Rudelson–Vershynin:** nothing here uses it. The Fourier steps use only Lemma 1 of RESULTS (the L^p bound) inside Brascamp–Lieb, plus an Esseen inequality proved in §0.

**Most useful next step:** prove (TW), J(τ) ≤ K(1+|τ|), for light orthonormal frames. Then join Proposition 5.3 to GEOM Prop 5.4 across frames where Z has a component in span(V,U).

---

# Rank-three quadratic forms: the convex side by pivots and discriminants

## Results

1. **Theorem 3.1 (PROVED).** Every definite rank-three form has density ≤ 82, for every linear term, constant term and product law. When the linear part lies in the range of A the bound is 12.
2. **Corollary 3.2 (PROVED).** For Y an orthonormal 3D projection of X, the spherical means of the density of Y satisfy M_{y0}(r) ≤ min(2^{3/2}, 6/(πr)), uniformly in y0.
3. **Lemmas 2.2 and 2.3 (PROVED).** For every unit vector w and every linear form L: α₁(σ⟨w,X⟩² + L) ≤ 15.43 |σ|^{-1/2}. For every rank-two symmetric M whose nonzero eigenvalues have modulus ≥ 1, and every linear form L: α₂(XᵀMX + L) ≤ 87.3.
4. **Theorem 4.1 (PROVED).** If a rank-three A with all |eig| ≥ 1 has a c-pivot, the density is bounded for every linear term, on both sides of the level set:
   - |a_ii| ≥ c gives ≤ 57.93 c^{-1/2};
   - an indefinite 2×2 block with |det| = D ≥ c gives ≤ 8.47 D^{-1/2}(5.2 + log₊16√D);
   - a definite 2×2 block gives ≤ π/√c.
5. **Corollary 4.2 (PROVED).** Rank three is open only when A has no c-pivot and some leverage exceeds 1/2. That row is then a hub, and the level set is either on the two-sheet side or there is a linear term outside the range.
6. **Section 5, the hub core.**
   - Localisation to a thin cone around the heavy null direction: PROVED.
   - The twist estimate (TW) implies a bounded density for light orthonormal frames: PROVED, conditional on (TW).
   - An explicit density shows that bounds on the marginals of (Z,V,U) cannot close the core: PROVED.
7. **Section 6 (PROVED).** Every level set of 2tv + u² has an exact fibration by planar conics. The fibres are lines exactly on the one-sheet side (this is Theorem C). On the two-sheet side the fibres through the null axis are hyperbolas, and their integrals decay only like 1/|α|.
8. **Section 7 (NUMERICAL, exact estimators).**
   - Core densities do not grow as the heavy row tends to null: values 1.7–3.6 in every family, including laws built to realise the obstruction of 5.4.
   - J(τ) is flat in τ.

## 0. Setting and tools

**Setting.** X = (X_1,…,X_n) has independent coordinates with densities f_i ≤ 1. A = RΛRᵀ, where R is n×3 with orthonormal columns and Λ is symmetric 3×3 with eigenvalues of modulus ≥ 1. Rows of R are r^(i) ∈ ℝ³, leverages are l_i = |r^(i)|², and Σ_i r^(i)r^(i)ᵀ = I₃. Put Y = RᵀX.

Since Λ is invertible, every Q = XᵀAX + bᵀX + c can be written

  Q = (Y−y₀)ᵀΛ(Y−y₀) + βZ + c′,  Z = ⟨u,X⟩, |u| = 1, u ⊥ columns of R.  (0.1)

Here βZ is the outside linear term. The diagonal entries are a_ii = r^(i)ᵀΛr^(i).

**Small-ball quantities.** φ_Q(u) = sup_s P(|Q−s| ≤ u); α₁(Q) = sup_{u>0} φ_Q(u)/√u; α₂(Q) = sup_{0<u≤1} φ_Q(u)/(u(1+log(1/u))).

**Tools from the record.**
- **(T1) Theorem F**, with B = 0 and I = [n]. Then G_I = I₃, so if every l_i ≤ 1/2, then |φ_Q(t)| ≤ (4π)^{3/2}|t|^{-3/2}|det Λ|^{-1/2} and ‖p_Q‖ ≤ 12. This holds for every linear term, because linear phases are translations inside Brascamp–Lieb. The only characteristic-function input is Lemma 1 of RESULTS: ∫|ĝ|^p ≤ 4π/√p for |g| ≤ f ≤ 1, p ≥ 2.
- **(T2) GEOM Lemma 1.2.** For g(x) = a(x−m)² + κ and X with density ≤ 1: the density of g(X) is ≤ |a|^{-1/2}|y−κ|^{-1/2}, and P(|g(X)−s| ≤ u) ≤ 4u/√(|a| max(|s−κ|,u)) ≤ 2√(2u/|a|).
- **(T3) GEOM Lemma 1.3.** For ANY density ρ ≤ K on ℝ² and B positive definite, the density of (w−w₀)ᵀB(w−w₀) is ≤ πK/√det B.
- **(T4) GEOM Lemma 1.5.** Schur complements keep the count of eigenvalues of modulus ≥ 1, minus the pivot size.
- **(T5) Layer cake.** sup_s E|Z−s|^{-1/2} ≤ ∫₀^∞ min(1, φ_Z(v^{-2})) dv.
- **(T6) Ball / Livshyts–Paouris–Pivovarov.** k-dimensional orthonormal projections of X have density ≤ 2^{k/2}.
- **(T7)** Conditioning on original coordinates is lossless (Fubini).
- **GEOM (P2), (P3), (C3):** 2×2 pivots and their compositions.

**Esseen inequality with an explicit constant.** Let F(x) = (sin(x/2)/(x/2))² ≥ 0. Its Fourier transform is 2π(1−|t|)₊, and F ≥ F(1) = 0.919395 on [−1,1]. Hence

  P(|Z−s| ≤ h) ≤ F(1)^{-1} E F((Z−s)/h) = F(1)^{-1} ∫(1−|t|)₊ φ_Z(t/h)e^{-its/h} dt ≤ 1.08767 h ∫_{|t|≤1/h} |φ_Z(t)| dt.  (0.2)

## 1. The pivot identity

**Lemma 1.1.** Let h be any coordinate with a := a_hh ≠ 0, and put r = r^(h). Let V_h (3×2) have orthonormal columns spanning r^⊥, and put W = V_hᵀR_{−h}ᵀX_{−h}. Then:

(a) W is an orthonormal 2D projection of X_{−h}: its coefficient matrix M satisfies MMᵀ = I₂.

(b) Q = a(X_h−m)² + R_h, with m affine in X_{−h} and

  R_h = (W−w₀)ᵀS′(W−w₀) + β′Z′ + c″,  S′ = V_hᵀ(Λ − Λrrᵀ Λ/a)V_h.

  Here Z′ is a unit linear form of X_{−h}, and β′ = 0 whenever β = 0.

(c) The eigenvalues of S′ are the two nonzero eigenvalues of A/a_hh, so both have modulus ≥ 1.

(d) For every s, p_Q(s) ≤ |a|^{-1/2} E|s−R_h|^{-1/2}.

*Proof.* Write Y = rX_h + Y′ with Y′ = R_{−h}ᵀX_{−h}, and D = Y′ − y₀. Then

  Q = aX_h² + 2X_h(rᵀΛD + βu_h/2) + DᵀΛD + β⟨u_{−h},X_{−h}⟩ + c′.

Completing the square gives R_h = DᵀSD − (βu_h/a) rᵀΛD − β²u_h²/(4a) + β⟨u_{−h},X_{−h}⟩ + c′, with S = Λ − Λrrᵀ Λ/a.

- Sr = 0 and S is symmetric, so S = ΠSΠ (Π the projection onto r^⊥). Hence DᵀSD = (W−w₀)ᵀS′(W−w₀).
- The remaining terms are a linear form of X_{−h} plus a constant. Its component in the span of the rows of M is absorbed into w₀, since S′ is invertible by (c). The rest is β′Z′. If β = 0, no linear term arises outside W.
- For (a): MMᵀ = V_hᵀ(I − rrᵀ)V_h = I₂.
- For (c): the quadratic part of R_h is the Schur complement A/a_hh = MᵀS′M. It has rank two and at least two eigenvalues of modulus ≥ 1 by (T4).
- For (d): apply (T2) conditionally on X_{−h}, then (T7). ∎

No leverage condition enters. The identities were checked symbolically (check_identities.py). The resulting exact estimator matches direct histograms of Q to 1–2% (§7).

## 2. Small-ball bounds with arbitrary linear terms

**Lemma 2.2.** Let Z₂ = ⟨z,X⟩ with |z| = 1, let Ξ be any linear form, and A > 0. Then for all λ, z₀, s and v > 0,

  P(|A(Z₂−z₀)² + λΞ − s| ≤ v) ≤ 15.43 √(v/A).

*Proof.*
- **Light case: all z_i² ≤ 1/2.** Apply the Fresnel linearisation (RESULTS (3.1)) to the square; the linear terms go into the phase. This gives |φ(t)| ≤ (4π|t|A)^{-1/2} ∫du Π_i |ψ_i(uz_i + b_i)| for some shifts b_i. Hölder with weights c_i = z_i² (Σ c_i = 1) and Lemma 1 bound the integral by Π_i(|z_i|^{-1}·4π|z_i|)^{c_i} = 4π. So |φ(t)| ≤ √(4π/(A|t|)), and (0.2) gives the bound 4·1.08767·√(4π)·√(v/A) = 15.43√(v/A).
- **Heavy case: some z_k² > 1/2.** Given X_{−k}, the form is a quadratic in X_k with leading coefficient ≥ A/2. (T2) gives ≤ 4√(v/A). ∎

**Lemma 2.3.** Let W = MX with MMᵀ = I₂; write w^(i) for the columns of M. Let S be symmetric 2×2 with |det S| ≥ 1, of any signature, and L any linear form. Then for 0 < u ≤ 1,

  sup_s P(|(W−w₀)ᵀS(W−w₀) + L − s| ≤ u) ≤ 87.3 u(1+log(1/u)).

*Proof.*

**(a) Light case: all |w^(i)|² ≤ 1/2.** Apply Fresnel to both squares and geometric Brascamp–Lieb with c_i = |w^(i)|² (Σ c_i = 2); linear terms are shifts. This gives |φ(t)| ≤ (4π)²/(4π|t|√|det S|) ≤ 4π/|t|. By (0.2), the probability is ≤ 27.34 u(1+log(1/u)).

**(b) Heavy case: |w^(j)|² > 1/2 for some j.** Set ŵ = w^(j)/|w^(j)| and e ⊥ ŵ, both unit in ℝ². Define:
- T = ⟨ŵ, W−w₀⟩ = |w|X_j + c, with c a linear form of X_{−j};
- Z₂ = ⟨e, W⟩, a unit linear form of X_{−j}, since Σ_{i≠j}(e·w^(i))² = eᵀ(I − w^(j)w^(j)ᵀ)e = 1;
- L = ℓ_jX_j + L′.

Given X_{−j}, the form is ax² + 2Mx + C in x = X_j, with a = S_tt|w|². Its discriminant satisfies

  D′ := M² − a(C−s) = −|w|² det S · (Z₂−z₀)² + |w|ℓ_jS_te(Z₂−z₀) + S_tt|w|(ℓ_jc − |w|L′) + const.

The c² and c(Z₂−z₀) terms cancel; this was verified symbolically. Completing the square in Z₂, D′ = A′(Z₂−z₁)² + λΞ + B, with |A′| = |w|²|det S| ≥ 1/2 and Ξ a linear form of X_{−j}.

Since |a||s − κ_crit| = |D′|, (T2) gives P(· | X_{−j}) ≤ min(1, 4u/√|D′|); for a = 0 the bound is directly u/|M|. Averaging over X_{−j} and using Lemma 2.2 with a₁ := α₁(D′) ≤ 21.82:

  P ≤ ∫₀¹ P(|D′| < 16u²/θ²) dθ ≤ ∫₀¹ min(1, 4ua₁/θ) dθ ≤ 4a₁u(1+log(1/u)). ∎

**Corollary 2.4.** Under Lemma 2.3, sup_s E|s − ((W−w₀)ᵀS(W−w₀)+L)|^{-1/2} ≤ 1 + ∫₁^∞ min(1, 87.3 v^{-2}(1+2 log v)) dv = 57.93, by (T5).

Every rank-two symmetric M with nonzero eigenvalues of modulus ≥ 1 has this form, since XᵀMX = WᵀSW with W an orthonormal 2D projection. So Lemma 2.3 is (H2) for all rank-two matrices, uniformly in linear terms.

## 3. Definite forms

**Theorem 3.1.** Let Λ be definite (all eigenvalues ≥ 1, or all ≤ −1). Then ‖p_Q‖_∞ ≤ 82 for every b and c, and ‖p_Q‖_∞ ≤ 12 if β = 0.

*Proof.*
- If max l_i ≤ 1/2, (T1) gives ≤ 12.
- Otherwise pick h with l_h > 1/2. Since Λ is definite, |a_hh| ≥ l_h > 1/2. Lemma 1.1(d) and Corollary 2.4 give p_Q ≤ √2·57.93 < 82.
- If β = 0, R_h = (W−w₀)ᵀS′(W−w₀) with S′ definite and det S′ ≥ 1. By (T3) with K = 2 from (T6), R_h has density ≤ 2π, so E|s−R_h|^{-1/2} ≤ 2√(2·2π) = 4√π. Hence p_Q ≤ 4√(2π) = 10.03. ∎

**Corollary 3.2.** By coarea, p_{|Y−y₀|²}(r²) = 2πr M_{y₀}(r). So M_{y₀}(r) ≤ 12/(2πr) = 6/(πr); trivially M ≤ ‖ρ_Y‖ ≤ 2^{3/2}.

Only the product structure is used, through (T1), (T2) and (T6). This is consistent with the thin-shell counterexample for general bounded 3D densities.

## 4. Indefinite forms

**Theorem 4.1.** Let A = RΛRᵀ have all |eig| ≥ 1, of any signature, and let b be arbitrary.

(i) If |a_ii| ≥ c for some i, then ‖p_Q‖ ≤ 57.93 c^{-1/2}. This follows from Lemma 1.1, which needs no leverage condition, and Corollary 2.4.

(ii) If a 2×2 principal block B = A_{ij} is definite with det B ≥ c, then ‖p_Q‖ ≤ π/√c, by GEOM (P3).

(iii) If B is indefinite with |det B| = D ≥ c, then ‖p_Q‖ ≤ 8.47 D^{-1/2}(5.2 + log₊16√D). Proof: GEOM (P2) gives a logarithmic profile around κ(X_{−ij}). This centre has matrix A/B, which has rank one and eigenvalue |σ| ≥ 1 by (T4), so κ = σ⟨n,X⟩² + (linear form). Lemma 2.2 gives α₁(κ) ≤ 15.43, and (C3) gives K(3 + 2 log 15.43). ∎

**Corollary 4.2 (reduction for rank three).** Fix c ≤ 1/2.
- If A has a c-pivot, the density is bounded (Theorem 4.1).
- If A has no c-pivot and all l_i ≤ 1/2, the density is ≤ 12 (T1).
- In the remaining case, some l_h > 1/2 while |a_hh| < c and |a_hj| < √(2c) for all j (from |det A_{hj}| < c). Yet Σ_j a_hj² = r^(h)ᵀΛ²r^(h) ≥ l_h ≥ 1/2. So row h of A has norm ≥ 1/√2 and only small entries: **a hub**.
- In that case, Theorem C still bounds the one-sheet side when β = 0.

Rank three is therefore open exactly for no-pivot matrices with a hub, and there only on the two-sheet side or when β ≠ 0.

## 5. The hub core

**5.1 Normal form.** Let r̂ = r^(h)/|r^(h)| and l = l_h. Complete r̂ to an orthonormal frame (r̂, e₂, e₃) and set T = ⟨r̂, Y−y₀⟩, W = (⟨e₂, Y−y₀⟩, ⟨e₃, Y−y₀⟩). Then:
- T = √l·X_h + εZ₀ − t₀, with ε = √(1−l) and Z₀ = ⟨R_{−h}r̂, X_{−h}⟩/ε a unit linear form;
- (Z₀, W) is an orthonormal 3D projection of X_{−h}, since (R_{−h}r̂)ᵀR_{−h}e_k = r̂ᵀ(I−rrᵀ)e_k = 0, and it is independent of X_h;
- Q = Λ̃₁₁T² + 2T⟨b,W⟩ + WᵀΛ̃_⊥⊥W + βZ + c′.

For β = 0, the discriminant of Q as a quadratic in X_h is D = l(Λ̃₁₁s − WᵀNW), with N = Λ̃₁₁Λ̃_⊥⊥ − bbᵀ. The Z₀-terms cancel, and det N = Λ̃₁₁ det Λ; both facts were checked symbolically. So the pivot bound p ≤ E|D(W)|^{-1/2} holds for every Λ̃₁₁, but it is infinite at the hub Λ̃₁₁ = 0.

In the no-pivot regime every j ≠ h has small weight in the hub partner V (from a_hj) and in the remaining square U (from a_jj). So (V, U) is light; only Z₀ may carry heavy coordinates. For Λ = diag(1,1,−1) and Λ̃₁₁ = 0 the normalised form is

  Q = 2(T)(V−v₀) + (U−u₀)².

- For ε = 0, β = 0 this is GEOM Prop 5.4 (bounded).
- For ε > 0 the extra term 2εZ₀V is a rank-two twist that involves the hub partner V and a new direction Z₀. This is the canonical open configuration, a hub coupled to a dense remainder, in rank three.

**Lemma 5.2 (localisation).** In the exact null case, p(s) = E[f_h(x*)/(2√l|b||V′|)]. The contribution of {|V′| ≥ κ|W−w₀|} is at most

  E[1/(2√l|b|κ|W−w₀|)] ≤ 2√(2π)/(2κ√l|b|) ≤ 2.51/(κ√l|b|),

using E|W−w₀|^{-1} ≤ 2√(2π) for a density ≤ 2. On the two-sheet level set the complement lies inside a cone of angle about 2κ around the heavy null T-axis. That is where the whole difficulty sits: along this ray the level set is nearly the plane {V = v₀}, which contains the heavy direction.

**Proposition 5.3 (the twist estimate gives a bounded density).** Setting:
- X_h has density ≤ 1 and is independent of X_L;
- (Z, V, U) is an orthonormal 3D projection of X_L whose rows all have squared norm ≤ 1/2 (a light frame);
- 0 < ε ≤ 1/√2 and l = 1−ε²;
- Q = 2(√l X_h + εZ − t₀)(V−v₀) + (U−u₀)² + (any linear form of X).

Assume

  (TW)  J(τ) := sup_θ ∫∫_{ℝ²} |E exp(i(yV + uU + ⟨θ,X_L⟩ + τZV))| dy du ≤ K(1+|τ|).

Then ‖p_Q‖ ≤ 28.7 + 0.39K.

*Proof.*

(i) **Hub step.** Integrate X_h first, then substitute y = 2t√l x and use f_h ≤ 1:

  |φ(t)| ≤ (2|t|√l)^{-1} ∫ dy |E_L e^{iy(V−v₀) + itΦ}|,  Φ = 2(εZ − t₀)(V−v₀) + (U−u₀)².

(ii) **Fresnel on (U−u₀)².** The remaining linear terms become the shift of y, θ, and the Z-frequency −2tεv₀. This gives ∫dy |…| ≤ (4π|t|)^{-1/2} J(2tε).

(iii) **Cap for large t.** Given X_h, the quadratic part in X_L is M̂Λ_εM̂ᵀ, with Λ_ε having eigenvalues ±ε and 1. Theorem F gives |φ(t)| ≤ (4π)^{3/2} ε^{-1}|t|^{-3/2}.

(iv) **Integrate in t.** Use |φ| ≤ 1 on |t| ≤ 1, bound (ii) on 1 ≤ |t| ≤ ε^{-2}, and bound (iii) beyond:

  ‖p_Q‖ ≤ (2π)^{-1}[2 + (12/(4√(π/2)))K + 4(4π)^{3/2}]. ∎

Any growth of J up to linear in τ is affordable. For Gaussian coordinates J(τ) is exactly constant: 2π/σ² for all τ.

This reduction is complete only for orthonormal light frames. Conditioning on heavy coordinates of Z (which is lossless) yields frames in which Z has a component along (V, U):
- in the exactly degenerate case this is again GEOM Prop 5.4;
- in between, the Fourier route loses about log(ε′/ε″), where ε″ is the distance of Z from span(V, U). This interpolation is the remaining gap in the reduction.

**Proposition 5.4 (marginal bounds cannot close the core).** Fix s = −1, X_h uniform on [−½,½], and κ = ε. For k ≥ k₀, set ρ = κ on the block

  B_k = {v ∈ [2^{-k-1}, 2^{-k}], u ∈ [0,1], |z + (1+u²)/(2εv)| ≤ √l/(2ε)},

and complete ρ to a probability density elsewhere. Then:
- ρ ≤ 1;
- the (V,U) marginal equals √l ≤ 2 on the blocks;
- the (Z,V) marginal is ≤ ε, and the (Z,U) marginal is ≤ 4^{1−k₀}ε;
- the V-marginal is √l ≤ √2, and the U- and Z-marginals are small;
- ZV has a bounded density (≤ √l·ε·2^{1−k₀}).

Yet on each B_k the root satisfies x* = −εδ′/√l ∈ [−½,½], and 1/(2√l V) ≥ 2^k/(2√l). So the density of 2(√l X_h + εZ)V + U² at −1 is at least Σ_{k≥k₀} 1/4 = ∞. Any proof of the core must therefore use the linear dependence T − √l X_h = εZ on independent coordinates, not only bounds on marginals. For the same reason the weaker hypothesis "T|(V,U) has density ≤ K" is not enough: T = t*(W) + Unif[0,1/K] gives E[K/(2|V|)] = ∞.

## 6. Fibrations of the two-sheet hyperboloid

For q = 2tv + u², any density ρ on ℝ³, any s, and any β ∈ ℝ:

  p_q(s) = ½ ∫dα ∫dv ρ( (s−β²)/(2v) − αβ − α²v/2, v, β + αv ).

*Proof.* Coarea gives p = ∫∫ ρ((s−u²)/(2v), v, u) du dv/(2|v|). At fixed v ≠ 0, substitute u = β + αv, so du = |v| dα. ∎

**Consequences.**
- The fibre for fixed α is a conic in the plane {u = β + αv}. It is a line exactly when β² = s.
- On the one-sheet side (s > 0), take β = √s and Λ = diag(1,1,−1), so that t, v = (y₁±y₃)/√2, u = y₂ are orthonormal coordinates. The arc-length factor is 1 + α²/2 and each line integral is ≤ 2. This gives ½∫2/(1+α²/2) dα = π√2, which is Theorem C.
- On the two-sheet side no real β gives lines. With β = 0 the fibres are hyperbolas in the pencil of planes through the null t-axis. In the core, T|(V,U) has density ≤ l^{-1/2}, so each fibre integral is ≤ √(2/l)/√(1+α²). The α-integral diverges logarithmically as the planes approach {v = 0}, the tangent plane of the cone along the heavy null ray. That is the hub logarithm.
- Conditioning on one coordinate, as the assignment suggested, is exactly the pivot of §1. It turns the two-sheet problem into the 2D Lemma 2.3, and it fails only when every conditioned row is null.

## 7. Numerics

All estimators are exact conditional formulas averaged by Monte Carlo, not histograms, and all scripts are in the folder. Each run was under 10 minutes, one process at a time, at below-normal priority.

- **Identities** (check_identities.py): the discriminant identity with an outside linear term, the Z₀-cancellation, and det N = Λ̃₁₁ det Λ all verified symbolically.
- **Estimator validation** (check_pivot_outside.py): definite and (2,1) forms, heavy row spacelike or timelike, β ∈ {0, 1, 5}. The estimator matches histograms of 2·10⁶ samples to 1–2%. sup_s p decreases with β: 1.60, 1.48, 1.00, 0.43, 0.20 for β = 0, 0.3, 1, 3, 10.
- **Hub core** (hub_two_sheet.py): Q = 2TV + U², n = 41, l from 0.5 to 1, families 'rand' and 'shared' (a = 0.6, 0.9), with uniform and spread laws.
  - two-sheet sup: 3.55 → 3.19 for uniform laws as ε goes from 0.71 to 0;
  - one-sheet sup: 4.10 → 3.61;
  - flat in ε, and flat for Λ̃₁₁ ∈ {±0.05, 0.2}.
- **Adversarial core** (core_adversarial.py): big-jump pairs enter Z as a(X+X′) and V as a(X−X′), at scales R = 10, 100, 1000, with the centre scanned on [−120, 120]. The sup is 1.727, 1.738, 1.748 and 1.780 for ε = 0.1, 0.032, 0.01 and 0, with the peak at the vertex. There is no trace of the mechanism of 5.4.
- **Twist integral** (twist_J2.py, with a τ-adaptive y-window). Corrected J at τ = 0, 3, 10, 30:
  - m = 60 random frame: 72.1, 71.9, 71.5, 68.9;
  - m = 60 shared block: 71.5, 71.5, 71.0, 68.9;
  - m = 12 random frame: 68.3, 68.1, 67.7, 66.6.

  These are flat, as the Gaussian value 24π = 75.4 predicts. An earlier fixed-grid run seemed to show a decrease at τ = 100; that was an artifact of the grid.

## 8. What remains

- **Named estimate (TW):** J(τ) ≤ K(1+|τ|) for light orthonormal frames, uniformly over the linear frequency θ. It is exact for Gaussian coordinates, holds numerically, and is sufficient by Proposition 5.3.
- **Unwritten step:** joining Proposition 5.3 to GEOM Prop 5.4 across frames in which Z has a component in span(V, U).
- Together these would settle rank three in every configuration, including outside linear terms.
