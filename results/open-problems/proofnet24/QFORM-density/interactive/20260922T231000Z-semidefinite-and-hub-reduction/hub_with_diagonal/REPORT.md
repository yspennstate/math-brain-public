## Summary

**Status: PARTIAL.**
- **Proved:** the composition lemma for a general remainder, reduced to one hypothesis (SQ). Its sharp form, with the random centre tracked, is Theorems 3.3-3.4. Also proved: an unconditional class where the dense twist sits on the hub's leaves (Theorem 5.1), and several a-free transfers.
- **No counterexample:** the numerics are flat in a.
- **Open:** a twist that touches the coordinates of the transverse square. That is the canonical star + rank one + eps W with W acting on supp(v).

**Key new idea.** The level set {Q = s} is the family of lines tangent to the parabola r = s + t^2/a in the (t, R)-plane; at a = 0 it is a pencil. Assume R has a square-root profile around a centre C along L. Then the whole effect of a is one negative quarter moment, E|(L + beta)^2 - a(C - s)|^{-1/4}. This can fail only when the centre is aligned with the parabola, which happens only when the hub block is nearly rank one. There the hub's own square takes over with the small constant |a|^{1/2}.

**Most useful next step.** Prove a square-root-profile lemma for a rank-one square with a small dense twist on its own coordinates. Theorems 3.3-3.4 then settle every small hub diagonal.

No step uses a pointwise bound on characteristic functions. Examples 4.2 and 4.3 agree with finding 3 of audit/.

---

# One hub with a small nonzero diagonal and a general remainder

**Setting.** X_h and X' = (X_i)_{i≠h} are independent. Every coordinate has density ≤ 1, and f_h is the density of X_h.

Q = a X_h² + 2 X_h t + R(X'),  t = L + β,  L = ⟨w, X'⟩,  R = X'^T M X' + b^T X' + const,  A = [[a, w^T],[w, M]].

**Inputs used.**
- A linear form ⟨θ, X⟩ has density ≤ √2/|θ| (Ball).
- k-dimensional marginals have density ≤ 2^{k/2} (Livshyts-Paouris-Pivovarov).
- Lemmas 1.2(ii), 1.3, 1.4 and 1.6 of the geometric report.
- α₁(Z) = sup_{s,u} P(|Z−s| ≤ u)/√u.
- No pointwise bound on characteristic functions is used.

**Answer to the question.** The property of R needed jointly with L has two parts:
1. a square-root profile of R around a random centre C, uniformly along L (hypothesis SQ);
2. a negative quarter moment of the single quadratic Δ_C = (L+β)² − a(C − s).

At a = 0 the second part is automatic. For a ≠ 0 it fails only if the centre is aligned with the parabola C = s + t²/a, which forces the hub block to be nearly rank one. There the hub's own square Z²/a (Z = aX_h + t) takes over with constant |a|^{1/2}, and level-1 randomness in the independent part of the centre removes the remaining logarithm. No hypothesis on the marginal law of R suffices, even at a = 0 (Example 4.2).

## 1. Exact identities

**1.1 Two ways of conditioning.** Given X', Q = g(X_h) with g(x) = ax² + 2xt + R. Put u = ax + t. Then ax² + 2xt = (u² − t²)/a, so the roots of g = s are u = ±√Δ with Δ = t² + a(s − R), x_± = (u_± − t)/a, and |g′(x_±)| = 2|u_±|. Hence

 p_Q(s) = E[Σ_± f_h(x_±)/(2√Δ); Δ > 0].

Here Δ = a(s − κ), where κ = R − t²/a is the random centre of the square-root singularity. Δ is a quadratic in X' with matrix ww^T − aM.

Given X_h = x instead, Q = ax² + Y_x with Y_x = R + 2xt, and p_Q(s) = ∫ f_h(x) p_{Y_x}(s − ax²) dx. Since Y_x + ax² = R + 2x(L + β + ax/2), a nonzero diagonal amounts to a zero diagonal with the x-dependent offset β + ax/2. So zero-diagonal bounds that are uniform in the offset *inside* the x-integral transfer at once.

**1.2 The split.** Roots with |ax + t| ≥ 1 contribute at most 1. So p_Q ≤ 1 + T(s), where

 T(s) = ∫ K_s dμ_{t,R},  K_s(t, r) = Σ_{x: ax²+2xt+r=s, |ax+t|<1} f_h(x)/(2|ax+t|).

**1.3 Tangent lines.** Consider the map (u, x) ↦ (t, r) = (u − ax, s + ax² − 2xu). Its Jacobian determinant is −2u, and at every image point x is a root with ax + t = u. So, when (t, R) has a density ρ,

 T(s) = ∫ f_h(x) [∫_{−1}^{1} ρ(u − ax, s + ax² − 2xu) du] dx.

For fixed x the segment passes through (−ax, s + ax²), which lies on Γ_s = {r = s + t²/a}, and has slope −2x = 2t/a there. So it is tangent to Γ_s. The full line carries the X-ray p_{Y_x}(s − ax²).
- At a = 0 the lines form the pencil through (0, s).
- For a ≠ 0 they form the tangent family of Γ_s.
- In the coordinates (t, κ = r − t²/a) they become horizontal translates of one parabola.

**Lemma 1.4 (kernel masses).** Let 0 ≤ f_h ≤ 1 with ∫f_h = 1.
- (i) ∫∫ K_s = 2.
- (ii) For fixed t and every φ ≥ 0, ∫ K_s(t, r)φ(r) dr = ∫ f_h(x) 1{|ax+t|<1} φ(s − ax² − 2xt) dx.
- (iii) For fixed r, with σ = s − r, ∫ K_s dt = ∫ f_h(x) 1{|ax²+σ| < 2|x|} dx/(2|x|) ≤ log(1 + (1+√(1+|aσ|))/(2|σ|)) ≤ log 2.5 + log₊(1/|σ|) for |a| ≤ 1.

*Proof.* (ii): at fixed t substitute r = s − ax² − 2xt, with |dr/dx| = 2|ax+t|. (iii): at fixed r, t = (σ − ax²)/(2x), |dt/dx| = |σ+ax²|/(2x²) and ax + t = (ax²+σ)/(2x), so the weight times the Jacobian is f_h(x)/(2|x|). The support lies in |x| > x_* = |σ|/(1+√(1+|aσ|)), and the bathtub principle gives log(1 + 1/(2x_*)). ∎

Numerically, bound (iii) is attained (ratio 1.00). So the logarithmic profile of the hub does not depend on a.

## 2. Regularity routes, uniform in a

**Proposition 2.1.** If (L, R) has a bounded joint density, then p_Q ≤ 1 + 2‖ρ_{L,R}‖_∞ for all a and β. This follows from Lemma 1.4(i).

**Proposition 2.2.** If the conditional density of L given R is at most κ₀, then for |a| ≤ 1

 p_Q ≤ 1 + κ₀(log 2.5 + 2 + 2 log₊ α₁(R)).

This is Lemma 1.4(iii) followed by Lemma 1.6. It is a type-2 profile around the centre R, independent of a.

Neither hypothesis holds in the configuration of Prop. 5.4, where the joint density has a square-root singularity along r = F_c(ℓ).

## 3. Square-root profiles and the random centre

**Hypothesis (SQ).** For every φ ≥ 0,

 E φ(L, R) ≤ K E[∫ φ(L, r)|r − C|^{-1/2} dr]

for a random centre C defined jointly with L.
- Typical source: R = λ(V − D)² + C, where V has conditional density ≤ κ_V given (L, D, C). Then K = κ_V|λ|^{-1/2}.
- Lebesgue variant: ρ_{L,R|Ξ} ≤ K′|r − C(ℓ, Ξ)|^{-1/2} with Ξ independent of L. Typical source: (L, V) with joint density ≤ K₂, which gives K′ = K₂|λ|^{-1/2}.

**Lemma 3.1 (reduction to the centre).** Under SQ, T ≤ K·N_a(s) with

 N_a(s) = E[1{|aX_h+t|<1}|s − aX_h² − 2X_h t − C|^{-1/2}].

*Proof.* Apply SQ to φ = K_s, then use Lemma 1.4(ii). ∎

So level 3 for Q becomes a level-2 question about the hub with remainder C.

**Lemma 3.2 (one-dimensional kernel).** Let Δ = t² + aσ. Then

 J_a(t, σ) := sup_{0≤f≤1, ∫f=1} ∫ f(x)|σ − ax² − 2xt|^{-1/2} dx ≤ 9.05|Δ|^{-1/4},  and J₀ ≤ 2|t|^{-1/2}.

*Proof.* Write φ(x) = −a(x + t/a)² + Δ/a. By Lemma 1.2(ii), |{|φ| < ε}| ≤ min(2√(2ε/|a|), 4ε/√max(|Δ|, |a|ε)). By the bathtub principle, J_a ≤ ∫₀^∞ min(1, m(λ^{-2})) dλ.
- If |Δ| ≥ a²/16: cut at λ₁ = 2|Δ|^{-1/4}; this gives 4|Δ|^{-1/4}.
- Otherwise: cutting at 2√2/√|a| and √(|a|/|Δ|) gives |a|^{-1/2}(4 + 2√2 + √2 log(a²/(8|Δ|))). Since log y ≤ (4/e)y^{1/4}, this is ≤ 9.04|Δ|^{-1/4}. ∎

Numerically (exact level-set measure, 3000 cases) the worst ratio is 0.32. The supremum can exceed J₀ by a factor √2 as a → 0: the second root x = −2t/a is a second tangent point.

**Theorem 3.3 (composition).** Under SQ,

 p_Q(s) ≤ 1 + 9.05 K E|Δ_C|^{-1/4},  Δ_C = (L+β)² + a(s − C).

Suppose C = σ_c t² + φ₁t + φ₀ + C′, with σ_c, φ₁, φ₀ constants and the conditional density of t given C′ at most D. Put D_H = 1 − aσ_c. Then

 p_Q ≤ 1 + 25.6 K D^{1/2}|D_H|^{-1/4}.

*Proof.* Given C′, Δ_C is a quadratic in t with leading coefficient D_H. Factor it into two linear factors and apply Cauchy-Schwarz: E|t−m−r|^{-1/4}|t−m+r|^{-1/4} ≤ sup_c E|t−c|^{-1/2} ≤ 2√2 D^{1/2}. ∎

At a = 0 the bound is finite for every centre whatsoever.

**Theorem 3.4 (integrating t first).** Under the same hypotheses,

 p_Q ≤ 1 + K D|σ_c|^{-1/2}(11.4 + 1.42 log₊|σ_c| + 1.42 min{2 log₊ α₁(C′), log₊(8|σ_c|/|D_H|)}).

*Proof.* Condition on (X_h, C′). Then N_a ≤ D·E I(X_h, C′) with I(x, c′) = ∫_{|ax+τ|<1}|h(τ)|^{-1/2} dτ, where h(τ) = s − ax² − 2xτ − σ_cτ² − φ₁τ − φ₀ − c′. The function h is quadratic with critical value h_c = s − c′ − q_c(x), where q_c has leading coefficient −D_H/σ_c.
- (I1), from the curvature: I ≤ |σ_c|^{-1/2}(5.66 + 1.42 log₊(|σ_c|/|h_c|)).
- (I2), from the slope: on the slab h′ = −(2xD_H + φ₁) ± 2|σ_c|. Outside E₀ = {|2xD_H + φ₁| ≤ 4|σ_c|} this gives I ≤ 2.83|σ_c|^{-1/2}.
- Finally E log₊(1/|h_c|) ≤ 2 + 2 log₊ min(α₁(C′), α₁(q_c(X_h))), and α₁(q_c(X_h)) ≤ 2√2(|σ_c|/|D_H|)^{1/2}. ∎

Numerically, (I1) has worst ratio 0.76.

**Reading of 3.3-3.4.**
- Genuine hub (|D_H| ≥ 1/2): p_Q ≤ 1 + 30.5 K D^{1/2}. The diagonal a is harmless.
- Degenerate end (σ_c ≈ 1/a): p_Q ≤ 1 + K D|a|^{1/2}(C + 1.42 log(1/|a|) + 1.42 min{2 log α₁(C′), log(8/(|a|D_H))}). The only thing needed of the centre is level-1 randomness of C′. Without it the growth is log(1/D_H), and this is attained (Example 4.3).

**Corollary 3.5 (Prop. 5.4 with an arbitrary coupling to further coordinates).** Let (L, V) be linear forms on the coordinates P = supp w ∪ supp v, with joint density ≤ K₂, and let Ξ = X_{P^c}. Let R be any quadratic polynomial in (L, V, Ξ) with V²-coefficient λ ≠ 0. Completing the square in V gives R = λ(V − D(L,Ξ))² + σ_c L² + c₁(Ξ)L + c₀(Ξ), with σ_c deterministic.
- Given Ξ, this is Prop. 5.4's configuration, which is uniform in the affine parts. So Prop. 5.4's bound holds with D_H = |1 − aσ_c|.
- The t-first argument (with D replaced by 1 and K by K₂|λ|^{-1/2}) adds T ≤ K₂|λ|^{-1/2}|σ_c|^{-1/2}(11.4 + 1.42 log₊|σ_c| + 1.42 min{2 sup_x log₊ α₁(S_x), log₊(8|σ_c|/|D_H|)}).
- Here S_x(Ξ) = c₀(Ξ) − (x + c₁(Ξ)/2)²/σ_c is the critical value of R + 2xL over (L, V), that is, the Schur-complement form in the independent coordinates Ξ.
- So the degenerate regime is uniform in D_H once that form has a level-1 bound.
- Scope: linear terms on P must lie in span(w, v).

## 4. The hub block, and why the hypotheses must be joint

**Lemma 4.1 (dichotomy).** Let B = [[a, W],[W, m]] with W ≥ 1, |a| < c ≤ 1/8 and σ = m/W².
- If both eigenvalues of B have modulus ≥ 1, then |σ| < 4 and D_H = |1 − aσ| ≥ 1 − 4c ≥ 1/2.
- If D_H ≤ 1/2, the small eigenvalue has modulus ≤ 2|a|W²/(W² − 2a²). Then B is a rank-one piece (a, w)(a, w)^T/a: a spread square, not a hub.

*Proof.* If |σ| ≥ 4, the smaller eigenvalue has modulus ≤ 2(1 + c|σ|)/(|σ| − c). This is decreasing in |σ| and equals 0.77 at |σ| = 4. ∎

**Example 4.2 (marginal hypotheses never suffice, even at a = 0).** Let Y be an extra independent coordinate and R = 2YL + c. Then R is itself a hub (bounded α₁ and level 2), and L is spread. Yet at a = β = 0, Q = 2(X_h + Y)L + c has an unbounded (logarithmic) density. Here A has only the nonzero eigenvalues ±√2·W, because the two hub rows are parallel.

**Example 4.3 (no transfer without D_H; the logarithm is sharp).** Let R = t²/a₀ + λV², with V independent and λa₀ < 0.
- At a = 0: p_Q ≤ C|λ|^{-1/2} E|t|^{-1/2}.
- At a = a₀: Q = Z²/a₀ + λV² is hyperbolic in the independent pair (Z, V). Its density is ~ ρ_Z(0)ρ_V(0)(|a₀|/|λ|)^{1/2} log(1/|s|), which is unbounded.
- Here A has only two large eigenvalues.

Numerics: a = 0.2, λ = −1, sums of 30 uniforms. The form is σt² + λV² + λ₂U² with D_H = 1 − aσ.

| D_H | 1 | 0.3 | 0.1 | 0.03 | 0.01 | 0.003 |
|---|---|---|---|---|---|---|
| λ₂ = 0 (two large eigenvalues) | 3.67 | 4.62 | 5.35 | 6.22 | 6.98 | 7.93 |
| λ₂ = +1 (three large eigenvalues) | 2.69 | 2.34 | 2.20 | 2.13 | 2.08 | 2.13 |
| λ₂ = −1 (three large eigenvalues) | 2.32 | 2.52 | 2.43 | 2.34 | 2.33 | 2.36 |

The λ₂ = 0 row grows by 0.72 per unit of log(1/D_H); the prediction is 0.85. The other two rows stay bounded.

Adding centre randomness εY to the λ₂ = 0 case cuts the growth off as Theorem 3.4 predicts:

| ε | 0 | 1e−3 | 1e−2 | 1e−1 | 1 |
|---|---|---|---|---|---|
| D_H = 0.1 | 5.29 | 5.05 | 4.37 | 2.52 | 0.82 |
| D_H = 0.003 | 8.06 | 6.23 | 4.32 | 2.41 | 0.81 |

The two rows merge once ε exceeds the D_H scale.

## 5. An unconditional class

**Theorem 5.1.** Split the leaves into disjoint sets S and T. Let V = ⟨v, X_S⟩, L = ⟨w, X_T⟩, and

 Q = aX_h² + 2X_h(L+β) + λ(V − D)² + C,

where D is any function of X_T and C is any quadratic polynomial in X_T with matrix M_C. A dense twist on the hub's leaves is allowed. Then:
- (a) if a = 0: ‖p_Q‖_∞ ≤ 9.51|λ|^{-1/2}|v|^{-1}|w|^{-1/2};
- (b) for every a: ‖p_Q‖_∞ ≤ 25.6|λ|^{-1/2}|v|^{-1} α₁(Δ_C)^{1/2}, with Δ_C = (L+β)² − aC;
- (c) if |w| = 1, max|w_i| ≤ 1/16 and |a|‖M_C‖ ≤ 1/16: ‖p_Q‖_∞ ≤ 118|λ|^{-1/2}|v|^{-1}.

All bounds are uniform in β, in the linear terms on T, and in the v-component of the linear terms on S.

*Proof.*
1. Condition on (X_T, X_h), which is lossless. Then Q = λ(V − D)² + Z with Z fixed and V of density ≤ √2/|v|. So p_Q(s) ≤ (√2/|v|)|λ|^{-1/2} E|s − aX_h² − 2X_h t − C|^{-1/2}.
2. Lemma 3.2 (which does not use the slab) and E|Z′|^{-1/4} ≤ 2α₁^{1/2} give (b).
3. For (a), use J₀ ≤ 2|t|^{-1/2} and E|t|^{-1/2} ≤ 2√2(√2/|w|)^{1/2}.
4. For (c), write N = ww^T − aM_C and choose a balanced split T = I ∪ J. Then ‖N_IJ‖_F ≥ |w_I||w_J| − |a|‖M_C‖ ≥ 0.437, row norms are ≤ 0.125, and the k = 1 marginals are ≤ 0.08.
5. Theorem D with k = 1, q = 1 then gives |φ_{Δ_C}(τ)| ≤ (2πe^{1/2}/|τ|)^{1/2} Z₁^{-1/4}.
6. Esseen with constant 1.0877 gives α₁ ≤ 21.2. ∎

Scope: this does not cover linear terms on S orthogonal to v, or a twist that touches S.

Numerics (30 + 30 leaves, a = 0 and ±0.05, both signs of λ):
- twist on T only: 2.13-2.14 at ε = 0.3, 1.06-1.08 at ε = 1;
- twist on all leaves (not covered): 1.82-1.87 and 0.76-0.80.

## 6. Bipartite leaves

**Proposition 6.1.** Suppose M_GG = 0. Put η = 2M_{Gc}X_c + b_G, let η_⊥ be its part orthogonal to w_G, and let σ_G = max over unit e ⊥ w_G of |M_{cG} e|. Then for every a, β, M_cc and w_c,

 ‖p_Q‖ ≤ (√2/|w_G|) E arcsinh(|w_G|/|η_⊥|) ≤ (√2/|w_G|)(1 + log(1 + 2|w_G|) + log₊(√2/σ_G)).

*Proof.* Given X_c and X_h = x, Q is affine in X_G with coefficient 2xw_G + η. Apply the bathtub principle in x. Then use arcsinh z ≤ log(1 + 2z), and note that ⟨e, η⟩ is a linear form in X_c with coefficient 2M_{cG} e. ∎

## 7. The Fourier route does not see the diagonal

**Proposition 7.1.** |φ_Q(τ)| ≤ ∫ f_h(x)|E e^{iτ(R + 2xL)}| dx, which does not depend on a. Hence

 ‖p_Q‖ ≤ (1/2π) ∫ min{1, ∫ f_h |E e^{iτ(R+2xL)}| dx} dτ.

- The first step of Theorem H is exactly this inequality. So every zero-diagonal estimate proved through it holds for every hub diagonal.
- The route is not blind to the curvature μ of R along w. For R = λV² + μL², the tilt integral inflates to (4π|μ|)^{1/2}|τ|^{-1/2}. The bound then fails logarithmically for every a, although the density is bounded.
- The real-variable route sees only the product aμ, through D_H.

## 8. Numerics

The estimator is the exact conditional formula above: Monte Carlo over X' with a sum over the roots, 2e5-6e5 samples per point.

Star + rank one + twist (60 leaves, ‖W‖ = 1, uniform laws), max_s p_Q for a = 0, .02, .1, .3, −.1, −.3:

| λ | ε | β | a = 0 | .02 | .1 | .3 | −.1 | −.3 |
|---|---|---|---|---|---|---|---|---|
| +1 | 0 | 0 | 3.55 | 3.59 | 3.51 | 3.47 | 3.62 | 3.62 |
| +1 | 0.2 | 0 | 2.16 | 2.18 | 2.16 | 2.14 | 2.18 | 2.16 |
| +1 | 0 | 0.4 | 2.05 | 2.05 | 2.06 | 2.06 | 2.05 | 2.04 |
| +1 | 0.2 | 0.4 | 1.49 | 1.51 | 1.50 | 1.50 | 1.56 | 1.51 |
| −1 | 0 | 0 | 3.58 | 3.60 | 3.59 | 3.65 | 3.57 | 3.44 |
| −1 | 0.2 | 0 | 2.18 | 2.18 | 2.19 | 2.61 | 2.18 | 2.15 |
| −1 | 0 | 0.4 | 2.06 | 2.07 | 2.06 | 2.05 | 2.05 | 2.07 |
| −1 | 0.2 | 0.4 | 1.51 | 1.52 | 1.50 | 1.50 | 1.51 | 1.50 |

The 2.61 is a single heavy-tail excursion: the estimator's variance is logarithmically infinite.

Other runs:
- Curvature μ along w (D_H from 0.4 to 1.6): 3.00-3.56 without twist, 2.00-2.18 with ε = 0.2.
- Spread laws, including a spread hub law with the slab placed on the hub's mass, only lower the density (≤ 0.09).

Bounds against the true maximum, in a model where SQ holds exactly (all bounds hold, crude by factors 5-20):

| (a, σ_c, D_H) | true max | Theorem 3.3 | Theorem 3.4 |
|---|---|---|---|
| (0.1, 0, 1) | 3.63 | 41.3 | n/a |
| (0.1, 3, 0.7) | 3.93 | 45.1 | 21.3 |
| (0.2, 4.95, 0.01) | 7.07 | 128.8 | 23.4 |
| (0.2, 4.95, 0.01) with centre noise | 1.70 | 43.8 | 17.1 |

## 9. What is open

The general remainder is reduced to SQ.
- Theorem 5.1 supplies SQ when the transverse square has its own coordinates.
- Corollary 3.5 supplies it when R sees the hub's coordinates only through (L, V).
- It is open when a dense twist touches supp(v), which is the canonical star + rank one + εW. It is also open with linear terms there orthogonal to v.

Given SQ, Theorems 3.3-3.4 settle every small hub diagonal, uniformly in the genuine-hub regime and at cost |a|^{1/2}·log at the degenerate end.

The next step is a square-root-profile lemma for Y = λ⟨v, X⟩² + εX^TWX + ⟨ℓ, X⟩ on the same coordinates. Equivalently, in the Fourier route: the twist bound for ∫∫|E e^{iuV + iyL + iτεX^TWX}| du dy, which Proposition 7.1 carries to every hub diagonal.
