## Summary

**Status.** The naive extension is FALSE: for two hubs, any hub block with negative determinant can carry an unbounded density (Theorem 1). Three positive theorems are PROVED: private leaves with any hub block, one hub diagonal with no hub-hub coupling, and Schur-matched leaves with small weight plus a third structure. The general positive-definite block is CONJECTURAL; we reduced it to one open maximal inequality.

**Key new idea.** After conditioning on the leaves, the remainder r can be any function correlated with the hub coefficient c. So the only general bound is p_Q(s) ≤ E_c sup_t p_{q_c}(t). With B = 0 this is Prop 5.5. With det B < 0, a quadratic remainder (R = LᵀB⁻¹L) can put every logarithmic singularity at the same level. Each positive result avoids the supremum in one of three ways:
- the level does not depend on the centre (Theorems 2 and 4);
- the critical set is a coordinate line (Theorem 3);
- or, in the counterexample, the singularities are made to coincide on purpose.

No step uses a pointwise bound on characteristic functions; there is no Fourier input anywhere. The bound √(2π)/σ_min for two hubs with any hub block (audit/, finding 3) is Theorem 2 below at k = 2, with the same constant.

**Next step.** Prove the elliptic maximal inequality for product densities (Proposition 7), then its hyperbolic analogue. With Lemma 5, that would show a pair of hubs with any hub block, inside a matrix with three large eigenvalues, has a bounded density. When the remainder carries a square transverse to the hub partners (and no twist on the other coordinates), the maximal inequality is not needed: single_hub_core/, Theorem 6.1 bounds the density by 11.5 (s₁s₂)^{-2/5}|λ|^{-1/5} for every hub block, through Plancherel in the two-dimensional hub partner. More generally single_hub_core/, Theorem 6.4 needs of the remainder only a polynomial profile mu(I) <= K|I|^b (any b > 0) of its frozen slices on intervals, and with a third hub (Theorem 6.3) nothing at all.

---

# Groups of hubs with a nonzero hub block

## Summary

Let H be a set of k = |H| ≥ 2 coordinates and B = A_HH the hub block. Let A = A_{H,H^c} be the hub rows, with singular values s₁ ≥ … ≥ s_k > 0. Write X' = X_{H^c}, L = AX' + β_H, and R(X') for all terms not involving X_H. Then

  Q = X_Hᵀ B X_H + 2 X_Hᵀ L + R(X').

GEOM Prop. 5.5 gives ‖p_Q‖ ≤ ½ + 8/(s₁s₂) for k = 2, B = 0 and every R.

| # | Statement | Status |
|---|---|---|
| Thm 1 | k = 2 and any hub block with det B < 0, including zero hub diagonals with an arbitrarily small hub-hub coupling. The remainder R = LᵀB⁻¹L gives P(\|Q\| ≤ ε) ≥ c ε log(1/ε), so there is no bounded density. The full matrix has rank two, no pivot, and small entries when the hub rows are spread. | PROVED (the extension is FALSE) |
| Thm 2 | Leaves J coupled only to the hubs: ‖p_Q‖ ≤ C_k / s_k(A_HJ) for every hub block, everything else arbitrary. C₂ = √(2π), C₃ = 1.71. Nearly attained. | PROVED |
| Thm 3 | k = 2, B = diag(a, 0), every remainder: ‖p_Q‖ ≤ 1 + 9.52 s₁^{−1/2} s₂^{−1}. | PROVED |
| Thm 4 | Schur-matched leaves plus an independent part W. The logarithm has weight ≤ 2√\|det B\| /(s₁s₂). For definite B the density is ≤ 2π√det B /(s₁s₂). For indefinite B it is bounded once a third large eigenvalue lies off the leaves. | PROVED |
| Lem 5 | Any quadratic ζ with quadratic part S: P(\|ζ − s\| ≤ ρ) ≤ 4 (ρ/‖S‖)^{1/4}. | PROVED |
| Conj 6 | k = 2: bounded whatever the remainder iff det B ≥ 0. For det B < 0, a log profile of weight O(√\|det B\|) around the Schur centre. k ≥ 3 with rank B ≠ 2: bounded. | CONJECTURAL, NUMERICAL |
| Prop 7 | det B > 0 case of Conj 6 ⇐ an elliptic maximal inequality for products. One-coordinate reductions lose exactly log(1/det B). | reduction PROVED, inequality OPEN |

**Structural point.** Given X', we have Q = q_c(X_H) + r, with q_c(x) = xᵀBx + cᵀx, c = 2L and r = R(X'). Since r may be any function of X' correlated with c, the general bound is p_Q(s) ≤ E_c sup_t p_{q_c}(t).
- For B = 0 the supremum is 1/|c|_∞, which is integrable in dimension two.
- For B ≠ 0 there is a critical point x₀(c) = −B⁻¹c/2.
- If det B < 0, sup_t p_{q_c} = ∞ whenever the product density is positive near x₀(c). Theorem 1 shows a quadratic remainder can put all these singularities at one level.
- If det B > 0, the supremum is finite but its expectation is a maximal function.

## 1. Tools

X has independent coordinates with densities f_i ≤ 1.

- **(F1)** Ball's bound with Rogozin's inequality: ⟨v, X_J⟩ has density ≤ √2 / |v|.
- **(F2)** If M is k × m of rank k with singular values s_j, then MX' has density ≤ 2^{k/2} / ∏ s_j. For k = 2:
  - L has density ≤ 2/(s₁s₂);
  - c has density ≤ K := 1/(2s₁s₂);
  - c₂ has density ≤ K₂ := 1/(√2 s₂), because a hub row has norm ≥ s₂.
- **(F3)** Bathtub: if 0 ≤ g ≤ 1, ∫g ≤ 1 and w is radially decreasing about a point, then ∫gw ≤ ∫ of w over the ball of volume 1 centred there.
- **(F4)** GEOM Lemma 1.4 and its proof. Let Y = (Y₁, Y₂) have independent densities g_i ≤ 1, and let B be indefinite with det B = −D, eigenvalues μ₊ > 0 > μ₋, and Λ = 1/μ₊ + 1/|μ₋|. Then
  p_{YᵀBY}(δ) = (2√D)⁻¹ Σ_{ε=±} ∫ g(y_ε(t)) dt,  where y_ε(t) = u_ε eᵗ + v_ε e^{−t} and |u_ε| = |v_ε| = ρ₀ = ½√(|δ|Λ).
  The vectors u_ε, v_ε depend only on (B, δ). For T ≥ T₁ = ¾ log 2, the tail satisfies ∫_T^∞ g(y_ε(t)) dt ≤ 3 log(1 + 1/m), with m ≥ ρ₀ e^T /(2√2); the same holds for t ≤ −T. This uses only g_i ≤ 1 and ∫g_i ≤ 1, so it holds uniformly under translations of Y.
- **(F5)** GEOM Lemma 1.3: if Y ∈ ℝ² has any density ≤ κ and B is definite, then p_{YᵀBY} ≤ πκ/√det B.

**Completing the square (B invertible).**
  Q = YᵀBY + ξ,  with Y = X_H + Z, Z = B⁻¹L and ξ = R(X') − LᵀB⁻¹L.   (1.1)
- Given X', Y has independent coordinates with densities f_h(· − Z_h) ≤ 1.
- ξ is quadratic in X' with matrix A/B (the Schur complement).
- Z has density ≤ |det B| · 2^{k/2} / ∏ s_j.

## 2. Theorem 1 (counterexample)

**Theorem 1.** Let k = 2, det B = −D < 0, A of rank two, and R = LᵀB⁻¹L. Then Q = YᵀBY. If ρ_Y(0) > 0 (for example uniform laws on [−½, ½] with β_H = 0), there are c₀, r₁ > 0 such that for 0 < ε ≤ r₁²:
  P(|Q| ≤ ε) ≥ (2c₀/√D) · ε · (1 + log(r₁²/ε)).
So Q has no bounded density.

*Proof.*
1. Here ξ ≡ 0 in (1.1).
2. ρ_Y = f_H ∗ law(Z) is the convolution of an L¹ function with a bounded density, hence uniformly continuous.
3. For uniform laws, AX' has a log-concave density that is positive on the interior of A[−½, ½]^m, and that interior contains a neighbourhood of 0. So ρ_Y(0) > 0.
4. Take c₀ > 0 with ρ_Y ≥ c₀ on |y| ≤ r₀. In the eigenbasis, yᵀBy = μ₊u² − |μ₋|v². Put a = √μ₊ u − √|μ₋| v and b = √μ₊ u + √|μ₋| v. Then yᵀBy = ab and da db = 2√D du dv.
5. If |a|, |b| ≤ r₁ := r₀/√Λ, then |y| ≤ r₀. Hence
  P(|Q| ≤ ε) ≥ (c₀/(2√D)) · |{|ab| ≤ ε, |a|, |b| ≤ r₁}| = (c₀/(2√D)) · 4ε(1 + log(r₁²/ε)). ∎

**The matrix.** M = GᵀBG with G = [I₂  B⁻¹A], so M has rank two. Its nonzero eigenvalues are those of B + AAᵀB⁻¹; for B = diag(b, −b) and AAᵀ = σ²I they are ±(b + σ²/b). Let a_j be the columns of A with |a_j| ≤ η, and suppose ‖B‖ < c and η²‖B⁻¹‖ < c/4. Then:
- remainder diagonals are ≤ η²‖B⁻¹‖;
- leaf–leaf 2×2 minors are det(B⁻¹) det[a_j a_l]² ≤ η⁴‖B⁻¹‖²;
- hub–leaf minors b_hh a_jᵀB⁻¹a_j − A_hj² are < c.

So M has no c-pivot. This needs spread hub rows, with about m ≳ σ²‖B⁻¹‖/c leaves. The example has exactly two large eigenvalues, so it is consistent with the conjecture (which needs three). What it rules out is any statement that a hub pair has a bounded density whatever the remainder.

**Remarks.**
- (i) det B < 0 includes B = [[0, e], [e, 0]] for every e ≠ 0. So Prop 5.5 is sharp in requiring A_HH = 0 exactly.
- (ii) The weight is small: ρ_Y(0) ≤ ‖ρ_Z‖ ≤ 2D/(s₁s₂). Theorem 4(b) gives the matching upper bound.
- (iii) In RESULTS Theorem H this is a rank-two A_JJ lying in the span of the hub rows, so det G̃ = 0 there.
- (iv) With det B > 0 the same remainder gives a density ≤ 2π√D/(s₁s₂).

**Numerics** (exact conditional sublevel estimator, §6; m = 80 leaves, 1.2·10⁶ samples). Values are P(|Q| ≤ ε)/(2ε) for ε = 10⁻¹, …, 10⁻⁷.

| B | values | fitted slope in log(1/ε) | predicted ρ_Y(0)/√D |
|---|---|---|---|
| diag(.2, −.2) | 1.20 2.02 2.86 3.69 4.50 5.31 6.18 | 0.359 | 0.362 |
| diag(.05, −.05) | … 1.67 | 0.089 | 0.092 |
| [[0, .2], [.2, 0]] | 1.20 2.03 2.83 3.63 | ≈ 0.35 | 0.364 |
| 0.2 I (control) | flat ≈ 0.57 = (π/b)ρ_Y(0)/2 | — | — |

## 3. Theorem 2 (private leaves)

**Theorem 2.** Let the coordinates split as H ∪ J ∪ K with |H| = k ≥ 2, and suppose the matrix of Q vanishes on J×J and J×K. Linear terms on J, and all other blocks, are arbitrary. If s_k(A_HJ) ≥ σ, then
  ‖p_Q‖ ≤ C_k/σ,  C_k = (√2/2) ∫_{|x| ≤ r_k} dx/|x|,  where V_k r_k^k = 1.
So C₂ = √(2π) = 2.507 and C₃ = 1.710.

*Proof.*
1. Condition on X_K. Then Q = ⟨v(X_H), X_J⟩ + g(X_H), with v(x) = 2A_HJᵀx + b_J.
2. Given X_H = x, (F1) gives a conditional density ≤ √2/|v(x)|.
3. Let P be the projection onto range(A_HJᵀ). Then |v(x)| ≥ |Pv(x)| = |2A_HJᵀ(x − x_b)| ≥ 2σ|x − x_b|, where x_b = −(AAᵀ)⁻¹A b_J / 2.
4. By Fubini and (F3), p_Q(s) ≤ (√2/(2σ)) ∫ f_H(x)/|x − x_b| dx ≤ C_k/σ. ∎

No smallness, leverage or eigenvalue condition is needed, and k ≥ 2 is essential. For comparison, Theorem H allows a diagonal on the leaves but needs leverages ≤ ½. Numerically the bound is nearly attained: 2.375 and 2.398 against 2.507. The gap is exactly the cube-versus-disk loss (3.526 vs 3.545) and the Gaussian-versus-Ball loss (1.382 vs 1.414).

## 4. Theorem 3 (one hub diagonal, no hub-hub coupling, every remainder)

**Theorem 3.** For k = 2, B = diag(a, 0) with any a ≠ 0, and every R:
  ‖p_Q‖ ≤ 1 + 16√(KK₂) = 1 + 9.514 s₁^{−1/2} s₂^{−1}.

*Proof.*
1. Given X', p(t) = |c₂|⁻¹ ∫ f₁(x₁) f₂((t − g(x₁))/c₂) dx₁, where g(x₁) = a x₁² + c₁x₁.
2. Let x₁* = −c₁/(2a). Off the window |x₁ − x₁*| ≤ ω, each of the two branches x₁ ↦ x₂ is monotone with |dx₂/dx₁| ≥ 2|a|ω/|c₂|. So the branches contribute at most 1/(|a|ω).
3. Hence sup_t p ≤ 2/λ + m₁(x₁*, λ/(2|a|))/|c₂|, with λ = 2|a|ω and m₁ the f₁-mass of the window. Also sup_t p ≤ 1/|c₂|.
4. The critical line moves at speed 1/(2|a|) in c₁, so ∫ m₁(−c₁/(2a), λ/(2|a|)) dc₁ = ∫ f₁(x) |{c₁ : |2ax + c₁| ≤ λ}| dx = 2λ, for every a.
5. Take λ = θ|c₂|^{1/2} on |c₂| ≤ 1. Then E[2/λ] ≤ 8K₂/θ and E[m₁/|c₂|] ≤ 8θK; on |c₂| > 1 the bound is 1.
6. Put θ = √(K₂/K), and use p_Q(s) ≤ E_c sup_t p. ∎

Numerics with the adversarial remainder R = L₁²/a: 2.65 (a = 1), 1.79 (a = .2), 0.60 (a = .02); bound 10.5. What makes this case provable is that the critical set is a coordinate line, so the window does not depend on t. Any block with b₁₂ ≠ 0 and b₂₂ = 0 has det < 0 and falls under Theorem 1.

## 5. Lemma 5 and Theorem 4

**Lemma 5.** Let ζ = ZᵀSZ + bᵀZ + c₀, with λ = ‖S‖. Then P(|ζ − s| ≤ ρ) ≤ 4(ρ/λ)^{1/4}. If λ ≥ 1, then E log₊ 1/|ζ − s| ≤ 4 log 4 + 4 ≤ 9.55.

*Proof.*
- **Case 1: some |s_ii| ≥ λ/2.** Condition on the other coordinates. GEOM Lemma 1.2(ii) gives ≤ 2√(2ρ/|s_ii|) ≤ 4√(ρ/λ).
- **Case 2: all |s_ii| < λ/2.** Then ‖S_off‖ > λ/2.
  1. A random subset I has E[2u_IᵀS_IJ u_J] = ½ uᵀS_off u. So some I has ‖S_IJ‖ ≥ ‖S_off‖/2 > λ/4.
  2. Cauchy–Schwarz in Z_I, with Z_J2 an independent copy of Z_J, gives P ≤ P(|2Z_IᵀS_IJ W + h| ≤ 2ρ)^{1/2}, where W = Z_J − Z_J2 has independent densities ≤ 1.
  3. (F1) and P(|S_IJ W| ≤ t) ≤ 2√2 t/‖S_IJ‖ give P ≤ (4√2)^{1/2}(ρ/‖S_IJ‖)^{1/4} ≤ 3.37(ρ/λ)^{1/4}.
- **The logarithm.** E log₊ 1/|ζ − s| = ∫₀^∞ P(|ζ − s| ≤ e^{−τ}) dτ ≤ ∫₀^∞ min(1, 4e^{−τ/4}) dτ. ∎

**Theorem 4.** Take H = {h₁, h₂}, D = |det B|, and s₁, s₂ the singular values of A_HJ. Suppose
  Q = (X_H + Z)ᵀB(X_H + Z) + W,  with Z = B⁻¹(A_HJ X_J + g(X_K)) and W = W(X_K),
where g is affine and W is quadratic, both arbitrary. (This allows arbitrary hub–K couplings and anything on K.) Then:
- **(a)** If B is definite: ‖p_Q‖ ≤ 2π√D/(s₁s₂).
- **(b)** If B is indefinite and D ≤ 4: p_Q(s) ≤ (2√D/(s₁s₂)) · [7.04 + 2 log₊(2√2 s₁s₂/D) + E log₊ 1/|s − W|].
- **(c)** If moreover ‖A_KK − A_KH B⁻¹ A_HK‖ ≥ 1 (true whenever the H ∪ K block has three eigenvalues of modulus ≥ 1): ‖p_Q‖ ≤ (2√D/(s₁s₂)) · (16.6 + 2 log₊(2√2 s₁s₂/D)).

*Proof.* Condition on X_K; then the level is fixed. Z has density ≤ κ_Z := 2D/(s₁s₂), and Y = X_H + Z has density ≤ κ_Z.
- **(a)** Apply (F5).
- **(b)**
  1. For each value of Z, apply (F4) with the same curves y_ε(t). Split each branch at |t| = T₂.
  2. The tails are ≤ 3 log(1 + 1/m) uniformly in Z.
  3. The middle part, averaged at the fixed level, is ≤ 2T₂ κ_Z (Tonelli).
  4. Choose e^{T₂} = max(e^{T₁}, 2√2 M/ρ₀) with M = 1/κ_Z. This gives
   p ≤ (κ_Z/√D) · [7.04 + 2 log₊(4√2/κ_Z) + log₊ 1/(Λ|δ|)].
  5. The bracket times κ is increasing in κ, and Λ ≥ 1 when D ≤ 4. Average over X_K.
- **(c)** Apply Lemma 5. ∎

Theorem 1 is the case W = constant of (b). The logarithm is real, but its weight tends to zero with the hub block. Numerics: adding 4X_k² to the Theorem 1 example gives a flat 0.73; adding 4X_k² − 4Y_k² gives 0.61.

## 6. Conjectures, reduction, generalisations, numerics

**Conjecture 6.**
- (i) For k = 2 and det B ≥ 0: bounded whatever the remainder, uniformly in B.
- (ii) For det B < 0: p_Q(s) ≤ C + C√|det B| · E log₊ 1/|s − ξ|. Hence α₂ ≤ C, and the density is bounded when the full matrix has three large eigenvalues (then ‖A/B‖ ≥ 1 and Lemma 5 applies).
- (iii) For k ≥ 3 with rank B ≠ 2: bounded.

**Proposition 7.** Let M_B f(x) := sup_t p_{(X_H − x)ᵀB(X_H − x)}(t) (the ellipse means). Then p_Q(s) ≤ E M_B f_H(x₀), where x₀ = −B⁻¹c/2 has density ≤ 2D/(s₁s₂). So Conjecture 6(i) for definite B follows from the elliptic maximal inequality ∫ρ M_B f ≤ Φ(‖ρ‖_∞ / det B), for every product f and every probability density ρ.
- All examples satisfy the weak-L² form C√(‖ρ‖/det B).
- Bounding f₁f₂ ≤ f_i on the arcs where x_i moves fast gives M_B f(x₀) ≤ (C/√D)(M f₁ + M f₂), with 1D Hardy–Littlewood maximal functions M. Averaging against a density of height ~|b| costs exactly log(1/|b|), and this is sharp for f₁ = 1_[0,1]. So the product structure must be used in both coordinates at once.

**Generalisations.**
- **Non-orthogonal rows:** nothing uses orthogonality; only singular values enter.
- **Overlap with the remainder's eigenvectors:**
  - none gives Theorem 2;
  - exact matching gives Theorem 1 (and Theorem 4 once a third structure is present);
  - partial overlap is covered by Theorem H, with det G̃^{−1/2}.
  Numerically, R = t·LᵀB⁻¹L is bounded for t ≠ 1 (t = .99: 3.35; t = .9: 2.66; t = 0: 2.41) and diverges only at t = 1. A third direction on the leaves, V₃ ⊥ the hub rows, is bounded (1.88, 1.37, 0.89 for λ = .25, 1, 4).
- **Hub plus a hub-like structure in the remainder:** this is a hub pair with block [[a_hh, a_hk], [a_hk, a_kk]], and the sign of its determinant decides:
  - zero diagonals with a_hk ≠ 0 fall under Theorem 1;
  - a_hk = 0 with one zero diagonal falls under Theorem 3.

**Estimator.** Given X' and X_{h₁}, Q is a 1D quadratic in X_{h₂}. So P(|Q − s| ≤ ε | ·) is the measure of at most two explicit intervals, computed exactly. The estimator is unbiased and lies in [0, 1]. Hub laws were uniform or spread (5 and 7 intervals over ±8 and ±12). Runs were BelowNormal and under 10 minutes each.

**Adversarial check of 6(i).** Sup density for R = 0 / half Schur / full Schur:

| B | uniform hubs | spread hubs |
|---|---|---|
| diag(.2, .2) | 2.40 / 1.95 / 1.08 | 0.10 / 0.10 / 0.10 |
| diag(.2, .0002) | 2.41 / 0.06 / 0.02 | 0.12 / 0.02 / 0.01 |
| rotated rank one | 2.41 / 2.36 / 2.05 | 0.11 / 0.11 / 0.12 |
| near rank one | 2.44 / 0.20 / 0.06 | 0.11 / 0.06 / 0.03 |

The definite case b·I stays at 0.09–0.29 for b = .2, .05, .01 and t ∈ [0, 2]. There is no growth anywhere.

**Audit.**
- Every constant was recomputed.
- The Theorem 1 slopes match the prediction to within 1–3%.
- Theorem 2 sits below its bound by exactly the two explained losses.
- Theorem 3 was tested with the adversarial remainder.
- In Theorem 4, the (F4) tails are uniform under translation and the fixed-level averaging is legitimate.
- The strongest threat to Conjecture 6(i) would be product sets built like Besicovitch–Rado–Kinney sets in each coordinate. The check that would settle it: maximise ∫ρ M_B f over product sets with ρ of height h, and see whether it grows faster than h^{1/2} as h → 0.
