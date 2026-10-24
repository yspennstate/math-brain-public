## Summary

**Status: PARTIAL.** We proved one new complete theorem. It settles the sub-case that none of the three known tools reach. We also give a precise reduction for the rest of the family, and a proof that pointwise Fourier bounds cannot work here.

- **What is proved:** for hub diagonal a = 0 and E acting inside span(w, v) (E = PEP), with arbitrary linear terms b, β, γ, any laws and any n, the density of Q is bounded by an absolute constant.
- **Key new idea:** complete the square, 2xL + σL² = σ(L + x/σ)² − x²/σ, and linearise that square exactly. The hub coordinate then carries a quadratic phase −tx²/σ. As t varies, its twisted characteristic function sweeps a parabola. Lemma S, an elementary 1D Strichartz-type bound, puts it in L⁶ jointly in (t, frequency), for every density ≤ 1. That covers frequencies above 1/|σ|. Below |σ| in scale, a three-event comparison with two Theorem-H forms gives the small-ball bound. A smoothing lemma glues the two halves together at scale |σ|.
- **Obstruction, checked numerically:** for E = σww^T and a suitably chosen hub law, |φ(t₀)| ≈ 1.38 √σ / t₀. So no bound C t^{-3/2} holds on the family, and any proof has to average over t.
  - The Frobenius-split lead is correct for E − PEP. But the in-span part adds nothing to e₃(A_IJᵀA_IJ) for any partition (Prop 7.2), so that split never reaches it.
  - The false twist lemma kills the Theorem-H-with-twist route for the in-span part. Theorem 6.2 does not use it.
  - Nothing here uses the pointwise form of Rudelson–Vershynin, only Lemma 1 (L^p) and Lemma S.
- **Most useful next step:** a twist estimate for twists with **no in-span part**: L¹ at |t| ≤ M/‖E_rest‖_F, and an L^{6/5}(dζ) slice version in the Strichartz range. Cross terms wzᵀ + zwᵀ need particular attention, because the bump-shift mechanism still acts on them. Together with the volume lemma of §8(b), that finishes a = 0.

---

# A hub coordinate against a compressed rank-one term: Strichartz at high frequency, comparison at low frequency

## 0. Setting and results

X_h, X_1, …, X_m are independent with densities ≤ 1. f_h is the density of X_h, ψ_i the characteristic function of X_i, and X' = (X_1, …, X_m).

w, v ∈ R^m are orthonormal with w_i² + v_i² ≤ 2c (c ≤ 1/8). L = ⟨w, X'⟩, V = ⟨v, X'⟩, and P is the orthogonal projection onto span(w, v). The form is

  Q = a X_h² + 2X_h(L + β) + λ(V + γ)² + X'ᵀEX' + bᵀX',

with |λ| ≥ 1, |a| < c, ‖E‖_op ≤ ε ≤ ε₀, and b, β, γ arbitrary. φ(t) = E e^{itQ}.

Split E = PEP + E_rest. The in-span part PEP is the form e_ww L² + 2e_wv LV + e_vv V², with |e_··| ≤ ε.

| # | Statement | Status |
|---|---|---|
| 2.1 | the e_vv, e_wv parts are removed exactly; what remains of PEP is σL² | PROVED |
| 3.1 | Lemma S: ∬\|∫f e^{isx²+iτx}dx\|⁶ ds dτ ≤ 4π³/√3 for every density f ≤ 1 | PROVED |
| 4.1 | ∫_{\|t\|≥T₀}\|φ\| ≤ 308\|λ'\|^{-1/2}\|1−aσ\|^{-1/6}(\|σ\|T₀)^{-1/6}, for E = PEP, any a, b | PROVED |
| 5.1 | sup_s P(\|Q−s\| ≤ δ) ≤ (6.5C_H + 2)δ for δ ≥ \|σ\|, when a = 0, E = PEP, any b | PROVED |
| 6.2 | a = 0, E = PEP, any b, β, γ, laws, m: density ≤ absolute constant | PROVED |
| 7.1 | no bound \|φ(t)\| ≤ Ct^{-3/2} holds on the family (≈ 1.38√(σ/λ)/t for adversarial hub laws) | NUMERICAL (Gaussian limit) |
| 7.2 | the in-span part adds nothing to e₃(A_IJᵀA_IJ) | PROVED (first order) |
| 8.1 | the full family (a = 0) reduces to twist estimates for twists with no in-span part, plus a volume lemma | PARTIAL |

Constants: C₆ = (4π³/√3)^{1/6} = 2.0377 and C_H = 7.56|λ'|^{-1/3}.

## 1. Tools

**Fresnel.** For θ ≠ 0, ε > 0 and A = 1/(4(ε − iθ)),

  exp(iθy² − εy²) = √(A/π) ∫ exp(−Au² + iuy) du,  with |√(A/π)| ≤ (4π|θ|)^{-1/2}.

Hence |E e^{iθY² + iW}| ≤ (4π|θ|)^{-1/2} ∫|E e^{iuY + iW}| du, by dominated convergence as ε → 0.

**Brascamp–Lieb with the L^p lemma.** Suppose G = Σρ_iρ_iᵀ is invertible and ρ_iᵀG^{-1}ρ_i ≤ 1/2 for all i. Then for all shifts c_i,

  ∫_{R^r} Π_i |ψ_i(⟨ρ_i, z⟩ + c_i)| dz ≤ (4π)^r det(G)^{-1/2}.

This is Theorem F of RESULTS.md. It uses only ∫|ψ|^p ≤ 4π/√p for p ≥ 2.

## 2. The in-span part

**Lemma 2.1.**

  λ(V + γ)² + e_ww L² + 2e_wv LV + e_vv V² = λ'(Ṽ + γ')² + σL² + μL + const,

where
- λ' = λ + e_vv and κ = e_wv/λ';
- Ṽ = V + κL = ⟨v + κw, X'⟩;
- σ = e_ww − e_wv²/λ';
- γ' = λγ/λ' and μ = −2λγκ.

So |λ'| ≥ 1 − ε, and |κ|, |σ| ≤ 2ε.

*Proof.* Complete the square in V, then in Ṽ. The frame (w, ṽ) has Gram matrix [[1, κ], [κ, 1 + κ²]], whose determinant is 1. For ρ_i = (w_i, ṽ_i) one computes ρ_iᵀG^{-1}ρ_i = w_i² + v_i² exactly. ∎

So for E = PEP,

  Q = aX_h² + 2X_h(L + β) + λ'(Ṽ + γ')² + σL² + Z,

where Z is a linear form (plus a constant).

## 3. Lemma S

**Lemma 3.1.** Let f ≤ 1 be a density (or let |F| ≤ f), and g(s, τ) = ∫f(x)e^{isx² + iτx} dx. Then ∬|g|⁶ ≤ 4π³/√3.

*Proof.*
1. g³ is the Fourier transform of the push-forward μ of f⊗f⊗f dx under F(x) = (Σx_i, Σx_i²).
2. det(DF DFᵀ) = 12Σx_i² − 4(Σx_i)² = 12r², where r is the distance from x to the line R(1,1,1).
3. The fibres of F are circles of radius r. By coarea, μ has density m = (1/(2√3))∫₀^{2π} f f f dθ ≤ π/√3.
4. By Plancherel, ∬|g|⁶ = (2π)²∬m² ≤ (2π)²(π/√3)∬m = 4π³/√3. ∎

Direct quadrature gives:
- uniform [0,1]: 59.2;
- two half-intervals 11.5 apart: 15.9;
- ten bumps of width 0.1 spread over [0,20]: 4.8.

## 4. High frequency

**Proposition 4.1.** Let E = PEP, σ ≠ 0, |aσ| < 1, and b arbitrary. Then

  ∫_T^{2T}|φ| ≤ (4π)^{5/6}C₆|λ'|^{-1/2}|1 − aσ|^{-1/6}(|σ|T)^{-1/6} = 16.8|λ'|^{-1/2}|1 − aσ|^{-1/6}(|σ|T)^{-1/6},

and the dyadic sum over both signs of t is at most 308 × the same factor, at T₀.

*Proof.*
1. At X_h = x, write 2x(L + β) + σL² = σ(L + x/σ)² − x²/σ + 2βx. Fresnel with θ = tσ, then Fubini, gives
  |φ(t)| ≤ (4π|tσ|)^{-1/2} ∫dζ |Ψ(ζ)| |g_h(t(a − 1/σ), 2tβ + ζ/σ)|.
2. Fresnel in Ṽ gives |Ψ(ζ)| ≤ (4π|tλ'|)^{-1/2} K(ζ), where K(ζ) = ∫dξ Π_i |ψ_i(ζw_i + ξṽ_i + tb'_i)|. No twist is left.
3. By §1: ‖K‖₁ ≤ (4π)² (det G = 1, leverages ≤ 1/2) and ‖K‖_∞ ≤ 4π. So ‖K‖_{6/5} ≤ (4π)^{11/6}.
4. Apply Hölder with exponents 6 and 6/5 in (t, ζ) ∈ [T, 2T] × R. The map (t, ζ) ↦ (t(a − 1/σ), 2tβ + ζ/σ) has |det| = |1 − aσ|/σ². Lemma S then bounds the L⁶ factor by (σ²/|1 − aσ|)^{1/6}C₆.
5. Collecting the factors: (4πT)^{-1}|σλ'|^{-1/2}σ^{1/3}C₆T^{5/6}(4π)^{11/6}, which is the claim. ∎

## 5. Scales above |σ| (a = 0)

**Proposition 5.1.** Let a = 0 and E = PEP. For all s and all δ ≥ |σ|,

  P(|Q − s| ≤ δ) ≤ (6.5C_H + 2)δ.

*Proof.* Set Q₁ = Q − σL² and Q₂ = Q − σ(L + β)², which equals 2X_h(L + β) + λ'(Ṽ + γ')² + Z − 2σβL − σβ². Both are in the Theorem H class: H = {h}, I = X', det G̃ = 1, leverages ≤ 1/2. So both have density ≤ C_H, uniformly in linear terms. Let Λ = √(δ/|σ|) ≥ 1, and split into three events that cover everything:
- **A = {|L| ≤ Λ}.** Here |Q − Q₁| ≤ δ, so the probability is ≤ P(|Q₁ − s| ≤ 2δ) ≤ 4C_Hδ.
- **B = {|L| > Λ, |L + β| ≥ Λ/2}.** Given X' (lossless), Q is affine in X_h with slope 2(L + β). So the probability is ≤ δ/|L + β| ≤ 2δ.
- **C = {|L| > Λ, |L + β| < Λ/2}.** Here |Q − Q₂| < δ/4, so the probability is ≤ 2.5C_Hδ. ∎

Only B uses a = 0. For a ≠ 0, the hub quadratic has its vertex at −(L + β)/a, and there it has a square-root singularity.

## 6. Theorem

**Lemma 6.1 (combination).** Suppose
1. sup_s P(|Q − s| ≤ δ) ≤ Aδ for all δ ≥ η, and
2. ∫_{|t|≥1/(2η)}|φ| ≤ B.

Then ‖p_Q‖_∞ ≤ C_K A + B/(2π).

*Proof.* Take K even Schwartz with 0 ≤ K̂ ≤ 1, K̂ = 1 on [−1/2, 1/2], and supp K̂ ⊂ [−1, 1]. Set C_K = Σ_k (k + 1) sup_{|v|≥k} |K(v)|. Split μ = μ∗K_η + (μ − μ∗K_η):
- μ∗K_η has density ≤ A·C_K, by (i).
- μ − μ∗K_η has integrable Fourier transform φ(1 − K̂(η·)), supported in |t| ≥ 1/(2η). So its density is ≤ B/(2π). ∎

**Theorem 6.2.** Let a = 0, E = PEP with ‖E‖ ≤ ε₀, and let b, β, γ, m and the laws be arbitrary. Then ‖p_Q‖_∞ ≤ C, an absolute constant.

*Proof.* If σ = 0, Theorem H applies directly. Otherwise take η = |σ| in Lemma 6.1: (i) holds by Prop. 5.1, and (ii) holds by Prop. 4.1 with T₀ = 1/(2|σ|). ∎

The two halves meet exactly at scale |σ|. Below |σ|, case B gives only 2√(|σ|δ). Prop. 4.1 started at T₀ = 1 costs |σ|^{-1/6}.

## 7. Obstructions

**Prop 7.1 (numerical).** Take E = σwwᵀ, (L, V) Gaussian N(0, I/12), and λ = 1. Then

  ∫|Ψ_t(2tx)| dx ≈ √(6π)√σ / t.

Choosing the hub law by phase selection gives |φ(t₀)| ≈ 1.38√σ/t₀. Measured: t₀|φ| = 0.453 (σ = 0.1) and 0.212 (σ = 0.02). t₀^{3/2}|φ| = 184 and 86, still growing like √t₀. For the uniform hub law, t₀^{3/2}|φ| stays at 10.6.

Bumpy laws (04_twist_lemma): ∫|E e^{iu⟨v,X⟩ + iκ⟨v,X⟩²}| du = ∞. The mechanism: each bump's transform is shifted by 2κℓ_k, which destroys the product cancellation.

**Prop 7.2.** With h ∈ J, the in-span terms lie in the tangent space of rank-2 matrices at w_I⊗e_h + λv_I⊗v_{J'}. So they add nothing to e₃ (and rank A_IJ ≤ 2 for E = σwwᵀ). The terms z_I w_{J'}ᵀ and the out-of-span part do count.

## 8. Full family (a = 0): what is left

- **(a)** Prop 5.1 holds verbatim once the family without in-span part is bounded, with some constant C_rest.
- **(b)** Prop 4.1 with E_rest needs K_t (now carrying the twist t X'ᵀE_rest X') in L^{6/5}(dζ) for t‖E_rest‖_F ≤ M. Theorem D covers t ≥ M/‖E_rest‖_F, if e₃ ≳ ‖E_rest‖_F² with admissible marginals: heavy rows go to J, and rows whose mass lies in J×J are removed by conditioning. If ‖E_rest‖_F ≳ |σ|, Theorem D alone covers the tail.
- **(c)** C_rest needs an L¹ twist estimate for PSP = 0 at low frequency. The bump shift vanishes when SP = 0, but not for the cross terms wzᵀ + zwᵀ (shift 2zᵀp_k along w). So this remains open.

For a ≠ 0, only case B of Prop 5.1 needs new input.

## 9. Numerics (num/)

- **n1_obstruction.py, n1b_obstruction_tail.py:** Prop 7.1.
- **n2_strichartz_constant.py:** Lemma S.
- **n3_strichartz_windows.py:** window integrals for σ = 0.1.
  - Uniform hub: 2.28, 1.38, 0.70, 0.35, 0.17.
  - Rough hub: 1.25, 0.75, 0.50, 0.31, 0.21.
  - Proven bound: 18.9 down to 7.5.
  - The run reached the 600 s limit after 13 of 15 rows.
