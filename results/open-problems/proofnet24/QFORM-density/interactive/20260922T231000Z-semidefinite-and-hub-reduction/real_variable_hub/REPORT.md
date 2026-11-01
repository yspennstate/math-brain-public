## Summary

We did not reach the full target. The canonical family is not proved: what is proved is the interval-hub case (hub density supported in an interval) with a diagonal twist and any linear terms. With a dense remainder, the problem reduces to one precisely stated Fourier estimate, which is still open.

**What is proved:**
- **Step (1), linear terms outside span(w,v):** closed for interval hub laws. So is the whole of any E except its non-aligned dense part: the compression onto span(w,v) and the diagonal.
- **The degenerate-hub milestone** `4X_hL + 2L^2 + 2V^2 + Σd_iX_i^2 + ⟨b,X⟩`, with the hub uniform on an interval: density ≤ 8.99. Theorem H and Prop 5.4 each miss this case.
- **Dense E:** proved only as a reduction. Everything follows from one open estimate, TL_⊥ (Section 4 below).
- **General hub laws:** the method gives C(1 + log M), where M unit intervals cover the hub's support. A uniform bound needs one more estimate, CSP_gen (Section 5).
- **Hub diagonal a ≠ 0:** argument written out, constants not computed.

**Key new idea.** Condition on X' (lossless), keep L as a real variable, and use Fourier only after L is frozen. Once L = ℓ is fixed, every term Theorem H would have to linearise along the hub direction (κL^2, L·V, L·⟨r,X'⟩) is a constant, a shift of the square's centre, or a linear term. None of them enters the frequency integral, where they would be the aligned twists that twist_obstruction/ shows are fatal.

**Checks.** Every constant in Lemma 2 and Theorem A was checked a second way; details are under the report's Section 8. The fibre estimator matches an independent estimator to about 1%. Nothing grows numerically: the dense family's peak density falls as eps grows, and the hub profile g(x) is unimodal, which suggests the log M loss belongs to the method.

**Most useful next step.** Prove TL_⊥, starting with the rank-two case R_⊥ = ε(pq^T + qp^T), p, q ⊥ span(w, ṽ). A Cauchy-Schwarz across a random split of the support of R_⊥, using N3 and N9 of twist_obstruction/, looks like the way in.

---

# Hubs with a remainder: freezing the hub projection

## Setting

X_h and X' = (X_i)_{i≠h} are independent, each coordinate with density ≤ 1. L = ⟨w,X'⟩ and V = ⟨v,X'⟩, with w, v orthonormal and leverages c_i = w_i^2 + v_i^2 ≤ 1/2. The family is

  Q = aX_h^2 + 2X_h(σL + β) + F(X'),  F = λV^2 + m(L)V + q(L) + T,

where:
- |λ| ≥ 1;
- m is affine and q is quadratic, so every quadratic in (L,V) with V^2-coefficient λ is allowed, in particular the compression PEP of E onto span(w,v);
- T is the rest. In the canonical family, T = X'^T E' X' + ⟨b,X'⟩ with E' = E − PEP.

| Result | Status |
|---|---|
| Lemma 1: exact reduction of p_Q to the joint law of (L,F), any remainder | PROVED |
| Lemma 2: Fourier bound at frozen L (aligned terms never enter the frequency integral) | PROVED |
| Theorem A: a = 0, f_h ≤ 1_J with J an interval of length D, T separable (any diagonal matrix, any linear term): ‖p_Q‖ ≤ 1/2 + σ^{-1}(1.54 + 21.9 D^{1/2}|λ|^{-1/2}) | PROVED |
| Corollary: 4X_hL + 2L^2 + 2V^2 + Σd_iX_i^2 + ⟨b,X⟩ with interval hub law: ≤ 8.99 | PROVED |
| Theorem B: dense E reduces to the non-aligned twist lemma TL_⊥ | PROVED (reduction) |
| Proposition C: general hub law, bound C(1 + log M); uniform bound follows from CSP_gen | PROVED / estimate stated |
| Proposition D: a ≠ 0 with \|1 − a q''/2\| ≥ c | PARTIAL |
| Block freezing; parabola lemma in three sub-cases; failure of the mixed-norm route | PROVED |
| Numerics | NUMERICAL |

## 1. Exact reduction

**Lemma 1.** For any measurable F and t = σL + β,

  p_Q(s) = E k_L(F),  k_ℓ(φ) = Σ over x with ax^2 + 2tx = s − φ of f_h(x)/(2|ax + t|).

Roots with |ax + t| ≥ 1 contribute at most 1 in total. For a = 0 they contribute at most 1/2, so

  p_Q(s) ≤ 1/2 + I(s),  I(s) = E[1{|t| < 1}(2|t|)^{-1} f_h((s − F)/(2t))].

*Proof.* Given X', Q is a one-variable function of X_h; change variables on each monotone branch, then Fubini. □

## 2. Fourier analysis at frozen L

Write F = F(L; X') with F(ℓ; X') = λ(V + γ(ℓ))^2 + c(ℓ) + T(ℓ; X'). Here γ and c are continuous, and T(ℓ; X') = Σ_i φ_i(X_i; ℓ) + ⟨b(ℓ), X'⟩ is separable for each ℓ and continuous in ℓ.

**Lemma 2.** For bounded Ψ ∈ L^1(R), continuous off a null set,

  |E[Ψ(L) e^{−iτF(L;X')}]| ≤ ‖Ψ‖_1 · min(√2, 4√π |τλ|^{-1/2}).

*Proof.*
1. Let η_δ be the centred Gaussian of variance δ^2. By continuity in ℓ and dominated convergence, E[Ψ(L)e^{−iτF(L;X')}] = lim_δ ∫ Ψ(ℓ_0) E[η_δ(L − ℓ_0) e^{−iτF(ℓ_0;X')}] dℓ_0.
2. For fixed ℓ_0, Fourier inversion of η_δ (with |η̂_δ| ≤ 1) bounds the inner expectation by (1/2π)∫ |E e^{iξL − iτF(ℓ_0;X')}| dξ. Because ℓ_0 is a constant, no function of L appears in the exponent except ξL.
3. Fresnel linearisation of the single square (RESULTS.md (3.1); the centre contributes a unimodular phase) bounds the integrand by (4π|τλ|)^{-1/2} ∫ |E e^{iξL + iuV − iτT(ℓ_0;X')}| du.
4. The last expectation factorises as Π_i ĝ_i(ξw_i + uv_i − τb_i), with g_i = f_i e^{−iτφ_i} and |g_i| = f_i. The frame ρ_i = (w_i, v_i) is tight with c_i ≤ 1/2.
5. Geometric Brascamp-Lieb, applied to the translated functions F_i(y) = |ĝ_i(|ρ_i|y − τb_i)|^{1/c_i}, together with Lemma 1 of RESULTS.md (∫|ĝ|^p ≤ 4π/√p for p = 1/c_i ≥ 2), gives ∫∫ Π|ĝ_i| ≤ (4π)^2.
6. Total: (1/2π)(4π|τλ|)^{-1/2}·16π^2 = 4√π |τλ|^{-1/2}, times ‖Ψ‖_1. The trivial bound is E|Ψ(L)| ≤ √2‖Ψ‖_1. □

Frozen L removes from the frequency integral exactly the terms (κL^2, LV, L⟨r,X'⟩) that Theorem H must linearise along the hub direction. As twists in that integral they would be aligned, and the aligned-twist counterexamples show the twist lemma is false for them.

## 3. Theorem A (interval hub law)

**Theorem A.** Let a = 0, f_h ≤ 1_J with J an interval of length D, and let F be as in Section 2 with T separable. Then

  ‖p_Q‖_∞ ≤ 1/2 + σ^{-1}(1.54 + 21.9 D^{1/2}|λ|^{-1/2}).

*Proof.*
1. With c_J the midpoint of J, f_h((s − F)/(2t)) ≤ 1{|F − c_*(L)| ≤ u(L)/2}, where u = 2|t|D and c_* = s − 2t c_J.
2. The Fejér kernel Φ_u(y) = (sin(y/u)/(y/u))^2 satisfies Φ_u ≥ 0.9195 on |y| ≤ u/2, and its Fourier transform is π u (1 − u|τ|/2)_+.
3. Truncate to |t| ≥ δ_0 so that Fubini applies, and remove the truncation by monotone convergence at the end. Then I ≤ (1.088/2π)∫ dτ E[Ψ_τ(L) e^{−iτF}], with H = (2|t|)^{-1}1{δ_0 ≤ |t| < 1} and Ψ_τ = H·Φ̂_{u}(τ)·e^{iτc_*}.
4. Since dℓ = dt/σ, ‖Ψ_τ‖_1 = (πD/σ)∫_{|t|<1}(1 − |t|D|τ|)_+ dt ≤ (π/σ)·min(2D, 1/|τ|).
5. Lemma 2 gives I ≤ (0.544/σ)∫ min(2D, |τ|^{-1}) · min(√2, 4√π|τλ|^{-1/2}) dτ.
6. Split at |τ| = 1/(2D): the inner part equals 2√2 and the outer part is ≤ 16√(2π) D^{1/2}|λ|^{-1/2}. □

**Corollaries.**
1. The degenerate-hub form 4X_hL + 2L^2 + 2V^2 + Σd_iX_i^2 + ⟨b,X⟩ has σ = 2, λ = 2. Theorem H fails for it (the frame (w_i, v_i, 2w_i) is singular) and so does Prop 5.4 (the diagonal twist). With an interval hub law (D = 1) its density is ≤ 8.99.
2. Take the canonical family with E replaced by its compression onto span(w,v) plus any diagonal matrix, and with arbitrary b (components outside span(w,v) included). For interval hub laws it is bounded with constants independent of n, ε and E.

## 4. Theorem B (dense E reduces to a non-aligned twist lemma)

**The decomposition.**
- Keep diag(E) in the separable part and decompose only E_off relative to w: E_off = κww^T + (wr^T + rw^T) + E_w, with r = E_off w − κw ⊥ w and E_w = P_w^⊥ E_off P_w^⊥.
- This is an identity of quadratic forms: X'^T E_off X' = κL^2 + 2L⟨r,X'⟩ + X'^T E_w X'. At frozen L = ℓ the first term is a constant and the second is linear.
- Let R = λvv^T + E_w, so that Rw = 0. Let ṽ be its top unit eigenvector, with eigenvalue λ̃ ≥ λ − ‖E‖; then ṽ ⊥ w and |ṽ − v| ≲ ‖E‖/λ.
- Write R = λ̃ṽṽ^T + R_⊥, with R_⊥w = R_⊥ṽ = 0.

**(TL_⊥), the missing estimate.** There is C_⊥ such that

  ∫∫ |E exp(iξ⟨w,X⟩ + iu⟨ṽ,X⟩ + iτX^T R_⊥ X + iΣ_i φ_i(X_i))| dξ du ≤ C_⊥,

for every product law with densities ≤ 1, every spread orthonormal frame (w, ṽ) with leverages ≤ 1/2, all separable phases φ_i, all τ, and every symmetric R_⊥ that annihilates span(w, ṽ) with ‖R_⊥‖ ≤ 1/2.

**Theorem B.** Assume TL_⊥. Then Theorem A holds for the full canonical family: a = 0, any E with ‖E‖ ≤ 1/4, any b, interval hub law. The constant 4√π in Lemma 2 becomes C_⊥/(2π√(4π)), and λ becomes λ̃.

*Proof.* This is Lemma 2 verbatim with the frame (w, ṽ). The ṽ-square is linearised, and the linear term along ṽ becomes a shift of the centre. What remains in the frequency integral is R_⊥ together with the separable phases. □

Why TL_⊥ is a reasonable target:
- By hypothesis it excludes the only known obstructions to twist lemmas, the aligned twists (R p ≠ 0 for some p in the frame span), which the counterexamples with bumpy laws require.
- It is trivial for Gaussian X.
- It is exactly the "small non-aligned coupling" statement left open in twist_obstruction/. The reduction shows that the aligned part of a dense twist never needs a Fourier treatment.

## 5. General hub laws

**Proposition C.** Suppose supp f_h is covered by M unit intervals. Then ‖p_Q‖ ≤ C(1 + log M).

*Proof.*
1. The kernel is dominated by (2|t|)^{-1}Σ_{m≤M} 1_{s−2tJ_m}.
2. Lemma 2 with Fejér domination gives, for each frozen ℓ and each interval S of length u, the conditional bound ν_ℓ(S) ≤ 21.9|λ|^{-1/2}u^{1/2}. Call this CSP (conditional square-root profile).
3. Hence ∫ν_ℓ k_ℓ ≤ min(√2/(2|t|), 21.9 M |λ|^{-1/2}(2|t|)^{-1/2}). Integrating over |t| < 1 gives O(1 + log M). □

**CSP_gen, the missing estimate for general hub laws.** For a.e. ℓ and every measurable set S,

  ν_ℓ(S) ≤ K|λ|^{-1/2}|S|^{1/2},

where ν_ℓ is the conditional law of λ(V+γ)^2 + T at L = ℓ. This is a uniform weak-L^2 bound.
- With CSP_gen, the bathtub principle (the kernel is ≤ (2|t|)^{-1} with mass 1) gives I ≤ 2√2 K|λ|^{-1/2}/σ for every hub law.
- Lemma 2 only gives |ν̂_ℓ(τ)| ≲ |τ|^{-1/2}. That yields the interval form of CSP, not the weak-L^2 form.
- An equivalent formulation: a parabola lemma for the fixed-hub forms Q_x with a separable twist. The naive Fourier proof fails because the twist changes along the curve.

## 6. Proposition D (a ≠ 0, PARTIAL)

**Kernel bounds.**
- Recentre J at 0; this moves a term linear in L into q.
- Then k_ℓ(φ) ≤ |a|^{-1/2}|φ − φ_c(ℓ)|^{-1/2}, with φ_c = s' + t^2/a.
- The level sets of k_ℓ are at most four intervals, with |{k_ℓ > μ}| ≤ min(2|t| + |a|, 2/μ, 4/(|a|μ^2)).
- sup k_ℓ ≤ 1/(2 max(0, |t| − |a|/2)).

**Region |t| ≥ |a|/2.** A layer-cake argument with CSP gives an integrable bound; the only logarithm appears near |t| = |a|/2 and is integrable.

**Region |t| < |a|/2.** This region has measure ≤ √2|a|/σ; it is where the hub's own critical point lies inside J.
1. The contribution is ≤ |a|^{-1/2} E[|R_a − s|^{-1/2}; |t| < |a|/2], where R_a = F − t^2/a is a rank-two form in (L,V) plus T. Its (L,V) matrix has determinant ≈ −λ(1 − a q''/2)/a.
2. Theorem F with r = 2 gives α_2(R_a) ≲ |a|^{1/2}|λ|^{-1/2}(1 − a q''/2)^{-1/2}.
3. The layer cake, combined with the probability of the region, gives O(|a|^{1/4} log^{1/2}(1/|a|)).

The non-degeneracy |1 − a q''/2| ≥ c is exactly D_H > 0 of Prop 5.4.

## 7. Elementary real-variable facts

**(a) Block freezing (PROVED).**
- Split the non-hub coordinates as K ∪ I. Suppose every term of F that involves X_I is of Prop 5.4 form in (L_I, V_I), with coefficients depending on X_K.
- Then conditioning on X_K reduces to Prop 5.4 on I, with ρ_{L_I V_I} ≤ 2/√(det Gram_I).
- This covers arbitrary E_KK, arbitrary b_K, and couplings E_KI whose row space lies in span(w_I, v_I).

**(b) Parabola lemma (sub-cases PROVED).** The claim: p of λ(V+γ)^2 + μY is ≤ C(|λμ|)^{-1/2}, for orthonormal v, y. It holds:
- (i) if some |v_i| ≥ c. Conditioning on X_{-i} leaves a one-variable quadratic whose critical value is μ⟨y_{-i} − (y_i/v_i)v_{-i}, X_{-i}⟩. That coefficient vector has norm |μ|(v_i^2 + y_i^2)^{1/2}/|v_i|, which gives the constant 2^{7/4}c^{-1}.
- (ii) if v and y have disjoint supports;
- (iii) if y_I = αv_I exactly on some block I;
- (iv) for spread frames, by Fourier: ∫∫Π|ψ_i(uv_i + τy_i)| ≤ (4π)^2 gives ∫|τ|^{-1/2}J(τ)dτ < ∞.

**(c) The mixed-norm route fails.**
- The parabola density is ≤ |λ|^{-1/2}∫ sup_v ρ_{VY}(v,y)|s − μy|^{-1/2} dy, and the same L^1_y L^∞_v mixed norm controls the definite rank-two form with a twist.
- That mixed norm is infinite for two coordinates with spread sets (difference sets, V, Y = (X_1 ± X_2)/√2), even though the parabola lemma holds there by (b)(i).
- By the Darmois-Skitovich theorem, spread projections of a non-Gaussian product are never independent, so no linear re-coordinatisation decouples V from (L,T).

**(d) Reduction to small ‖E_off‖_F (checked).**
- Put the hub in J and take a random split. Then A_IJ has two singular values of order one, and Σ_{k≥3} s_k^2 ≥ ‖E_IJ‖_F^2 − 4‖E‖^2, with E‖E_IJ‖_F^2 = ‖E_off‖_F^2/4.
- So Theorem D applies once ‖E_off‖_F ≥ η_0 ≫ ‖E‖.
- The diagonal of E is invisible to A_IJ and must be kept separable.
- The suggestion that the twist is then small in L^2 is false for spread laws, whose variances are unbounded.

## 8. Numerics

**Estimator.** fibre_density.py implements the partition-of-unity fibre identity p(s) = Σ_i E[Σ_r f_i(r)|∂_iQ|/|∇Q|^2]. It is exact-conditional, unbiased and bin-free. Against the independent hub-conditional estimator:

| s-grid point | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| fibre estimator | 0.559 | 1.169 | 1.411 | 1.006 |
| hub-conditional | 0.552 | 1.183 | 1.420 | 1.010 |

**Degenerate hub, 48 leaves, interval hub (t1).**

| configuration | peak density |
|---|---|
| no twist | 1.64 |
| diagonal twist \|d_i\| ≈ 0.1 | 1.46 |
| plus an orthogonal linear term of norm 1 | 0.85 |
| spread or bumpy laws | ≤ 0.07 |

The proven bound is 8.99.

**Hub profile (t2a).** g(x) = p_{Q_x}(0) is unimodal:

| x | 0 | ±1 | ±2 | ±3 |
|---|---|---|---|---|
| g(x) | ≈ 1.5 | 0.34 | 0.17 | 0.11 |

So the bathtub-worst hub law is the interval around 0, which is why the log M loss looks like a limitation of the method.

**Dense family (t2b).** Q = 2X_h(L + 0.2) + V^2 + εX'^T W X' + b_⊥U, with ‖W‖ = 1 and zero diagonal.

| laws | b_⊥ | ε = 0 | ε = 0.2 | ε = 0.5 |
|---|---|---|---|---|
| uniform | 0 | 3.45 | 2.19 | 1.43 |
| uniform | 1 | 1.15 | 1.12 | 0.98 |
| 3-tooth comb | 0 | 0.85 | 0.39 | 0.21 |

Nothing grows. The twist and the orthogonal linear terms lower the density, consistent with their entering only through a Fourier factor they can shrink.

**Constants.**
- The Fejér minimum 0.9194 and its transform π(1 − ω/2) were confirmed by quadrature.
- The Lemma 2 constant was recomputed: (1/2π)(4π)^{-1/2}·16π^2 = 7.0898 = 4√π.
- In Theorem A's integral the inner part equals 2√2 exactly. The outer part evaluates numerically to 16.7, below the analytic bound 40.1, so the stated constant is valid but not sharp.

## 9. What remains

1. TL_⊥ (Section 4): the only input still needed for the canonical dense family with a = 0 and interval hub laws.
2. CSP_gen (Section 5): the weak-L^2 conditional bound needed for general hub laws; the interval form is proved.
3. Explicit constants for Proposition D.
