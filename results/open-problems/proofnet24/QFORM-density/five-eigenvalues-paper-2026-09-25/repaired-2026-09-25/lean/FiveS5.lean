import Mathlib.Analysis.SpecialFunctions.Gamma.BohrMollerup
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.InverseDeriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Section 5 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): the constants and the elementary steps.

* Lemma 5.1: `sqrt_add_sub_le` (`√(u+δ) - √u ≤ √δ`) and `square_density_bound`.
* Lemma 5.2: `ellipse_jacobian` and `definite_const`.
* Lemma 5.3: `hyperbola_level`, `hyperbola_jacobian`, `hyperbola_u_norm`, `hyperbola_T1`, `hyperbola_branch_growth`,
  `hyperbola_cutoff`, `hyperbola_seven_halves_log2`, `amgm_inv`, `hyperbola_log_arg`.
* Lemma 5.4: `gamma_three_halves`, `gamma_five_quarters_sq_le`, `gamma_quarter_pow4_le`, `c54_pow4`, `c54_lt_19`
  (the coefficient 19, i.e. repair 20's certificate `2048 e^3 π < 19^4`), `c54_formula`, `lemma54_diag`,
  `log19_lt_three`, `L0_lt_eight`, `layer_cake_switch`.
* Lemma 5.5: `J_product_le`, `J_one_lt`, `J_far_compare`, and the three antiderivatives `deriv_log_branch_plus`,
  `deriv_arcsin_branch`, `deriv_log_branch_minus`.
* Lemma 5.6: `pairhalf_definite_const`, `pairhalf_delta_value`, `pairhalf_total`, `bounded_half_value`,
  `deriv_halfmoment_kernel`, `pairhalf_scaling`.
-/

open Real

namespace QformFiveB

/-! ### Lemma 5.1 -/

/-- `√(u+δ) - √u ≤ √δ` for `u, δ ≥ 0` (the interval length in Lemma 5.1(b)). -/
theorem sqrt_add_sub_le (u δ : ℝ) (hu : 0 ≤ u) (hδ : 0 ≤ δ) : √(u + δ) - √u ≤ √δ := by
  have h : √(u + δ) ≤ √u + √δ := by
    rw [Real.sqrt_le_left (by positivity)]
    have h1 : √u ^ 2 = u := Real.sq_sqrt hu
    have h2 : √δ ^ 2 = δ := Real.sq_sqrt hδ
    nlinarith [Real.sqrt_nonneg u, Real.sqrt_nonneg δ, mul_nonneg (Real.sqrt_nonneg u) (Real.sqrt_nonneg δ)]
  linarith

/-- The density formula of Lemma 5.1 is at most `1/√(|a||z-v|)` when `f ≤ 1`, and the Jacobian factor is
`|a| · √(|z-v|/|a|) = √(|a| |z-v|)`. -/
theorem square_density_bound (a w f1 f2 : ℝ) (ha : 0 < a) (hw : 0 < w) (h1 : f1 ≤ 1) (h2 : f2 ≤ 1) :
    (f1 + f2) / (2 * √(a * w)) ≤ 1 / √(a * w) ∧ a * √(w / a) = √(a * w) := by
  have hs : 0 < √(a * w) := Real.sqrt_pos.mpr (mul_pos ha hw)
  constructor
  · rw [div_le_div_iff₀ (by positivity) hs]
    nlinarith
  · rw [show a * w = a ^ 2 * (w / a) by field_simp, Real.sqrt_mul (by positivity), Real.sqrt_sq ha.le]

/-! ### Lemma 5.2 -/

/-- The Jacobian of `(δ, θ) ↦ (√(δ/μ₁) cos θ, √(δ/μ₂) sin θ)` is `1/(2√(μ₁ μ₂))`. -/
theorem ellipse_jacobian (μ₁ μ₂ δ θ : ℝ) (h1 : 0 < μ₁) (h2 : 0 < μ₂) (hδ : 0 < δ) :
    (cos θ / (2 * √(δ * μ₁))) * (√(δ / μ₂) * cos θ) - (sin θ / (2 * √(δ * μ₂))) * (-(√(δ / μ₁) * sin θ))
      = 1 / (2 * √(μ₁ * μ₂)) := by
  have e1 : √(δ / μ₂) / √(δ * μ₁) = 1 / √(μ₁ * μ₂) := by
    rw [Real.sqrt_div hδ.le, Real.sqrt_mul hδ.le, Real.sqrt_mul h1.le]
    have : 0 < √δ := Real.sqrt_pos.mpr hδ
    have : 0 < √μ₁ := Real.sqrt_pos.mpr h1
    have : 0 < √μ₂ := Real.sqrt_pos.mpr h2
    field_simp
  have e2 : √(δ / μ₁) / √(δ * μ₂) = 1 / √(μ₁ * μ₂) := by
    rw [Real.sqrt_div hδ.le, Real.sqrt_mul hδ.le, Real.sqrt_mul h1.le]
    have : 0 < √δ := Real.sqrt_pos.mpr hδ
    have : 0 < √μ₁ := Real.sqrt_pos.mpr h1
    have : 0 < √μ₂ := Real.sqrt_pos.mpr h2
    field_simp
  have hs : 0 < √(δ * μ₁) := Real.sqrt_pos.mpr (mul_pos hδ h1)
  have hs' : 0 < √(δ * μ₂) := Real.sqrt_pos.mpr (mul_pos hδ h2)
  have key : (cos θ / (2 * √(δ * μ₁))) * (√(δ / μ₂) * cos θ) - (sin θ / (2 * √(δ * μ₂))) * (-(√(δ / μ₁) * sin θ))
      = (cos θ ^ 2 * (√(δ / μ₂) / √(δ * μ₁)) + sin θ ^ 2 * (√(δ / μ₁) / √(δ * μ₂))) / 2 := by
    field_simp
    ring
  rw [key, e1, e2]
  have hc := sin_sq_add_cos_sq θ
  field_simp
  linear_combination (1 : ℝ) * hc

/-- Lemma 5.2: `(1/(2√det B)) ∫_0^{2π} L dθ = π L / √det B`. -/
theorem definite_const (L D : ℝ) (hD : 0 < D) : 1 / (2 * √D) * (2 * π * L) = π * L / √D := by
  have : 0 < √D := Real.sqrt_pos.mpr hD
  field_simp

/-! ### Lemma 5.3 -/

/-- The branch `w = ε√(δ/μ₊) cosh τ e₊ + √(δ/|μ₋|) sinh τ e₋` lies on the level set `q = v + δ`:
in the eigenbasis `q - v = μ₊ x₊² - |μ₋| x₋²`. -/
theorem hyperbola_level (μp μm δ τ ε : ℝ) (hp : 0 < μp) (hm : 0 < μm) (hδ : 0 ≤ δ) (hε : ε ^ 2 = 1) :
    μp * (ε * √(δ / μp) * cosh τ) ^ 2 - μm * (√(δ / μm) * sinh τ) ^ 2 = δ := by
  have h1 : √(δ / μp) ^ 2 = δ / μp := Real.sq_sqrt (div_nonneg hδ hp.le)
  have h2 : √(δ / μm) ^ 2 = δ / μm := Real.sq_sqrt (div_nonneg hδ hm.le)
  have hc := cosh_sq_sub_sinh_sq τ
  have e : μp * (ε * √(δ / μp) * cosh τ) ^ 2 - μm * (√(δ / μm) * sinh τ) ^ 2
      = ε ^ 2 * (μp * √(δ / μp) ^ 2) * cosh τ ^ 2 - (μm * √(δ / μm) ^ 2) * sinh τ ^ 2 := by ring
  rw [e, h1, h2, hε, mul_div_cancel₀ δ hp.ne', mul_div_cancel₀ δ hm.ne']
  linear_combination δ * hc

/-- The Jacobian of `(δ, τ) ↦ (ε√(δ/μ₊) cosh τ, √(δ/μ₋) sinh τ)` has modulus `1/(2√(μ₊ μ₋)) = 1/(2√D)`. -/
theorem hyperbola_jacobian (μp μm δ τ ε : ℝ) (hp : 0 < μp) (hm : 0 < μm) (hδ : 0 < δ) (hε : ε ^ 2 = 1) :
    |(ε * cosh τ / (2 * √(δ * μp))) * (√(δ / μm) * cosh τ)
      - (sinh τ / (2 * √(δ * μm))) * (ε * √(δ / μp) * sinh τ)| = 1 / (2 * √(μp * μm)) := by
  have e1 : √(δ / μm) / √(δ * μp) = 1 / √(μp * μm) := by
    rw [Real.sqrt_div hδ.le, Real.sqrt_mul hδ.le, Real.sqrt_mul hp.le]
    have : 0 < √δ := Real.sqrt_pos.mpr hδ
    have : 0 < √μp := Real.sqrt_pos.mpr hp
    have : 0 < √μm := Real.sqrt_pos.mpr hm
    field_simp
  have e2 : √(δ / μp) / √(δ * μm) = 1 / √(μp * μm) := by
    rw [Real.sqrt_div hδ.le, Real.sqrt_mul hδ.le, Real.sqrt_mul hp.le]
    have : 0 < √δ := Real.sqrt_pos.mpr hδ
    have : 0 < √μp := Real.sqrt_pos.mpr hp
    have : 0 < √μm := Real.sqrt_pos.mpr hm
    field_simp
  have hs : 0 < √(δ * μp) := Real.sqrt_pos.mpr (mul_pos hδ hp)
  have hs' : 0 < √(δ * μm) := Real.sqrt_pos.mpr (mul_pos hδ hm)
  have key : (ε * cosh τ / (2 * √(δ * μp))) * (√(δ / μm) * cosh τ)
      - (sinh τ / (2 * √(δ * μm))) * (ε * √(δ / μp) * sinh τ)
      = ε * (cosh τ ^ 2 * (√(δ / μm) / √(δ * μp)) - sinh τ ^ 2 * (√(δ / μp) / √(δ * μm))) / 2 := by
    field_simp
  rw [key, e1, e2]
  have hc := cosh_sq_sub_sinh_sq τ
  have hε' : |ε| = 1 := by
    have : |ε| ^ 2 = 1 := by rw [sq_abs]; exact hε
    nlinarith [abs_nonneg ε]
  have hsp : 0 < √(μp * μm) := Real.sqrt_pos.mpr (mul_pos hp hm)
  rw [show ε * (cosh τ ^ 2 * (1 / √(μp * μm)) - sinh τ ^ 2 * (1 / √(μp * μm))) / 2
      = ε * ((cosh τ ^ 2 - sinh τ ^ 2) / (2 * √(μp * μm))) by field_simp, hc]
  rw [abs_mul, hε', one_mul, abs_of_pos (by positivity)]

/-- `u = (ε a/2, b/2)` and `u' = (ε a/2, -b/2)` with `a² = δ/μ₊`, `b² = δ/μ₋` both have squared length
`δΛ/4`, `Λ = 1/μ₊ + 1/μ₋`; and `u e^τ + u' e^{-τ}` is the branch point. -/
theorem hyperbola_u_norm (μp μm δ τ ε : ℝ) (hp : 0 < μp) (hm : 0 < μm) (hδ : 0 ≤ δ) (hε : ε ^ 2 = 1) :
    (ε * √(δ / μp) / 2) ^ 2 + (√(δ / μm) / 2) ^ 2 = δ * (1 / μp + 1 / μm) / 4 ∧
    (ε * √(δ / μp) / 2) ^ 2 + (-(√(δ / μm) / 2)) ^ 2 = δ * (1 / μp + 1 / μm) / 4 ∧
    ε * √(δ / μp) / 2 * exp τ + ε * √(δ / μp) / 2 * exp (-τ) = ε * √(δ / μp) * cosh τ ∧
    √(δ / μm) / 2 * exp τ + -(√(δ / μm) / 2) * exp (-τ) = √(δ / μm) * sinh τ := by
  have h1 : √(δ / μp) ^ 2 = δ / μp := Real.sq_sqrt (div_nonneg hδ hp.le)
  have h2 : √(δ / μm) ^ 2 = δ / μm := Real.sq_sqrt (div_nonneg hδ hm.le)
  refine ⟨?_, ?_, ?_, ?_⟩
  · have e : (ε * √(δ / μp) / 2) ^ 2 + (√(δ / μm) / 2) ^ 2 = (ε ^ 2 * √(δ / μp) ^ 2 + √(δ / μm) ^ 2) / 4 := by
      ring
    rw [e, h1, h2, hε]; field_simp
  · have e : (ε * √(δ / μp) / 2) ^ 2 + (-(√(δ / μm) / 2)) ^ 2 = (ε ^ 2 * √(δ / μp) ^ 2 + √(δ / μm) ^ 2) / 4 := by
      ring
    rw [e, h1, h2, hε]; field_simp
  · rw [cosh_eq]; ring
  · rw [sinh_eq]; ring

/-- Lemma 5.3: for `τ ≥ T₁ = (3/4) log 2`, `√2 e^{-τ} ≤ e^{τ}/2`. -/
theorem hyperbola_T1 (τ : ℝ) (hτ : 3 / 4 * log 2 ≤ τ) : √2 * exp (-τ) ≤ exp τ / 2 := by
  have hs2 : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs2p : 0 < √2 := by positivity
  have e : exp (2 * (3 / 4 * log 2)) = 2 * √2 := by
    have e1 : 2 * (3 / 4 * log 2) = log 2 + log (√2) := by
      rw [Real.log_sqrt (by norm_num)]; ring
    rw [e1, exp_add, exp_log (by norm_num), exp_log hs2p]
  have h2 : 2 * √2 ≤ exp τ * exp τ := by
    rw [← exp_add, ← e]
    exact exp_le_exp.mpr (by linarith)
  have hpos : 0 < exp τ := exp_pos τ
  rw [exp_neg, ← div_eq_mul_inv, div_le_iff₀ hpos]
  nlinarith

/-- Lemma 5.3: on `τ ≥ T₁`, with `|u'_i| ≤ √2 |u_i|`, the coordinate `y = u_i e^τ + u'_i e^{-τ}` keeps the
sign of `u_i`, `|u_i|e^τ/2 ≤ |y| ≤ 3|u_i|e^τ/2`, and `|y'| ≥ |u_i|e^τ/2 ≥ |y|/3`. -/
theorem hyperbola_branch_growth (ui ui' τ : ℝ) (hτ : 3 / 4 * log 2 ≤ τ) (hu : |ui'| ≤ √2 * |ui|) :
    |ui| * exp τ / 2 ≤ |ui * exp τ + ui' * exp (-τ)| ∧
    |ui * exp τ + ui' * exp (-τ)| ≤ 3 * (|ui| * exp τ) / 2 ∧
    |ui| * exp τ / 2 ≤ |ui * exp τ - ui' * exp (-τ)| ∧
    |ui * exp τ + ui' * exp (-τ)| / 3 ≤ |ui * exp τ - ui' * exp (-τ)| := by
  have hT := hyperbola_T1 τ hτ
  have he : 0 < exp (-τ) := exp_pos _
  have he' : 0 < exp τ := exp_pos _
  have hsmall : |ui' * exp (-τ)| ≤ |ui| * exp τ / 2 := by
    rw [abs_mul, abs_of_pos he]
    calc |ui'| * exp (-τ) ≤ √2 * |ui| * exp (-τ) := by gcongr
      _ = |ui| * (√2 * exp (-τ)) := by ring
      _ ≤ |ui| * (exp τ / 2) := by gcongr
      _ = |ui| * exp τ / 2 := by ring
  have hbig : |ui * exp τ| = |ui| * exp τ := by rw [abs_mul, abs_of_pos he']
  have t1 := abs_add_le (ui * exp τ) (ui' * exp (-τ))
  have t2 := abs_sub_abs_le_abs_sub (ui * exp τ) (-(ui' * exp (-τ)))
  have t3 := abs_sub_abs_le_abs_sub (ui * exp τ) (ui' * exp (-τ))
  rw [sub_neg_eq_add] at t2
  rw [abs_neg] at t2
  refine ⟨by linarith, by linarith, by linarith, by linarith⟩

/-- Lemma 5.3: the cutoff `T = max{T₁, log(2/|u_i|)}` is at most `(3/4) log 2 + (1/2) log⁺(32/(δΛ))` when
`|u_i| ≥ √(δΛ)/(2√2)`. -/
theorem hyperbola_cutoff (x L : ℝ) (hL : 0 < L) (hx : √L / (2 * √2) ≤ x) :
    max (3 / 4 * log 2) (log (2 / x)) ≤ 3 / 4 * log 2 + 1 / 2 * max 0 (log (32 / L)) := by
  have hsL : 0 < √L := Real.sqrt_pos.mpr hL
  have hs2 : 0 < √2 := by positivity
  have hxpos : 0 < x := lt_of_lt_of_le (by positivity) hx
  have hlog2 : 0 ≤ log 2 := log_nonneg (by norm_num)
  apply max_le
  · have := le_max_left (0 : ℝ) (log (32 / L)); linarith
  · have h1 : 2 / x ≤ 4 * √2 / √L := by
      rw [div_le_div_iff₀ hxpos hsL]
      have := mul_le_mul_of_nonneg_left hx (show (0 : ℝ) ≤ 4 * √2 by positivity)
      have e : 4 * √2 * (√L / (2 * √2)) = 2 * √L := by field_simp; ring
      linarith
    have h2 : log (2 / x) ≤ log (4 * √2 / √L) := log_le_log (by positivity) h1
    have h3 : log (4 * √2 / √L) = 1 / 2 * log (32 / L) := by
      have e : 4 * √2 / √L = √(32 / L) := by
        rw [Real.sqrt_div (by norm_num), show (32 : ℝ) = 4 ^ 2 * 2 by norm_num,
          Real.sqrt_mul (by norm_num), Real.sqrt_sq (by norm_num)]
      rw [e, Real.log_sqrt (by positivity)]; ring
    have h4 := le_max_right (0 : ℝ) (log (32 / L))
    linarith

/-- Lemma 5.3: `6 log 2 + (3/2) log 2 < 6`, so each branch contributes less than `6 + log⁺(32/(δΛ))`. -/
theorem hyperbola_seven_halves_log2 : 6 * log 2 + 3 / 2 * log 2 < 6 := by
  have := log_two_lt_d9; norm_num at this; linarith

/-- The arithmetic-geometric mean step of Lemma 5.3: `Λ = 1/μ₊ + 1/μ₋ ≥ 2/√(μ₊ μ₋) = 2 D^{-1/2}`. -/
theorem amgm_inv (p q : ℝ) (hp : 0 < p) (hq : 0 < q) : 2 / √(p * q) ≤ 1 / p + 1 / q := by
  have ha : 0 < √p := Real.sqrt_pos.mpr hp
  have hb : 0 < √q := Real.sqrt_pos.mpr hq
  have hpa : √p ^ 2 = p := Real.sq_sqrt hp.le
  have hqb : √q ^ 2 = q := Real.sq_sqrt hq.le
  rw [Real.sqrt_mul hp.le, ← hpa, ← hqb]
  rw [Real.sqrt_sq ha.le, Real.sqrt_sq hb.le]
  rw [div_add_div _ _ (by positivity) (by positivity), div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith [sq_nonneg (√p - √q), mul_pos ha hb]

/-- Lemma 5.3: `Λ ≥ 2/√D` turns `32/(δΛ)` into at most `16√D/δ`. -/
theorem hyperbola_log_arg (δ Λ D : ℝ) (hδ : 0 < δ) (hD : 0 < D) (hΛ : 2 / √D ≤ Λ) :
    32 / (δ * Λ) ≤ 16 * √D / δ := by
  have hsD : 0 < √D := Real.sqrt_pos.mpr hD
  have hΛpos : 0 < Λ := lt_of_lt_of_le (by positivity) hΛ
  rw [div_le_div_iff₀ (by positivity) hδ]
  have h := mul_le_mul_of_nonneg_left hΛ (show (0 : ℝ) ≤ 16 * √D * δ by positivity)
  have e : 16 * √D * δ * (2 / √D) = 32 * δ := by field_simp; ring
  nlinarith

/-! ### Lemma 5.4 -/

theorem gamma_three_halves : Gamma (3 / 2) = √π / 2 := by
  have h := Real.Gamma_add_one (show (1 / 2 : ℝ) ≠ 0 by norm_num)
  rw [show (1 / 2 : ℝ) + 1 = 3 / 2 by norm_num, Real.Gamma_one_half_eq] at h
  rw [h]; ring

/-- Log-convexity of `Γ` (Bohr–Mollerup): `Γ(5/4)² ≤ Γ(1) Γ(3/2) = √π/2`. -/
theorem gamma_five_quarters_sq_le : Gamma (5 / 4) ^ 2 ≤ √π / 2 := by
  have h := convexOn_log_Gamma.2 (show (1 : ℝ) ∈ Set.Ioi 0 by norm_num)
    (show (3 / 2 : ℝ) ∈ Set.Ioi 0 by norm_num) (show (0 : ℝ) ≤ 1 / 2 by norm_num)
    (show (0 : ℝ) ≤ 1 / 2 by norm_num) (show (1 / 2 : ℝ) + 1 / 2 = 1 by norm_num)
  have e : (1 / 2 : ℝ) • (1 : ℝ) + (1 / 2 : ℝ) • (3 / 2 : ℝ) = 5 / 4 := by norm_num
  rw [e] at h
  simp only [Function.comp_apply, smul_eq_mul, Real.Gamma_one, log_one, gamma_three_halves] at h
  have hpos : 0 < Gamma (5 / 4) := Real.Gamma_pos_of_pos (by norm_num)
  have hpos2 : 0 < √π / 2 := by positivity
  have h2 : log (Gamma (5 / 4) ^ 2) ≤ log (√π / 2) := by
    rw [log_pow]; push_cast; linarith
  exact (log_le_log_iff (by positivity) hpos2).mp h2

/-- `Γ(1/4) = 4Γ(5/4)` gives `Γ(1/4)^4 ≤ 256 (√π/2)^2 = 64π`. -/
theorem gamma_quarter_pow4_le : Gamma (1 / 4) ^ 4 ≤ 64 * π := by
  have h1 : Gamma (5 / 4) = 1 / 4 * Gamma (1 / 4) := by
    have := Real.Gamma_add_one (show (1 / 4 : ℝ) ≠ 0 by norm_num)
    rwa [show (1 / 4 : ℝ) + 1 = 5 / 4 by norm_num] at this
  have h2 := gamma_five_quarters_sq_le
  rw [h1] at h2
  have hsq : (√π / 2) ^ 2 = π / 4 := by
    rw [div_pow, Real.sq_sqrt pi_pos.le]; norm_num
  have hnn : 0 ≤ (1 / 4 * Gamma (1 / 4)) ^ 2 := sq_nonneg _
  have h3 : ((1 / 4 * Gamma (1 / 4)) ^ 2) ^ 2 ≤ (√π / 2) ^ 2 := pow_le_pow_left₀ hnn h2 2
  rw [hsq] at h3
  have e : ((1 / 4 * Gamma (1 / 4)) ^ 2) ^ 2 = Gamma (1 / 4) ^ 4 / 256 := by ring
  rw [e] at h3
  linarith

/-- The coefficient of Lemma 5.4 at `v = 1/4`: `2 e^{1/4} (√2 π e)^{1/2} Γ(1/4) π^{-1/2}`. -/
noncomputable def c54 : ℝ := 2 * exp (1 / 4) * √(√2 * π * exp 1) * Gamma (1 / 4) / √π

/-- Its fourth power is `32 e³ Γ(1/4)⁴`. -/
theorem c54_pow4 : c54 ^ 4 = 32 * exp 1 ^ 3 * Gamma (1 / 4) ^ 4 := by
  unfold c54
  have hpi : 0 < π := pi_pos
  have hsp : √π ^ 2 = π := Real.sq_sqrt hpi.le
  have hs2 : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hA : 0 ≤ √2 * π * exp 1 := by positivity
  have hsA : √(√2 * π * exp 1) ^ 2 = √2 * π * exp 1 := Real.sq_sqrt hA
  have he4 : exp (1 / 4) ^ 4 = exp 1 := by
    rw [← Real.exp_nat_mul]; norm_num
  have e0 : (2 * exp (1 / 4) * √(√2 * π * exp 1) * Gamma (1 / 4) / √π) ^ 4
      = 2 ^ 4 * exp (1 / 4) ^ 4 * (√(√2 * π * exp 1) ^ 2) ^ 2 * Gamma (1 / 4) ^ 4 / (√π ^ 2) ^ 2 := by
    ring
  rw [e0, he4, hsA, hsp]
  have e1 : (√2 * π * exp 1) ^ 2 = 2 * π ^ 2 * exp 1 ^ 2 := by rw [mul_pow, mul_pow, hs2]
  rw [e1]
  field_simp
  ring

/-- **Lemma 5.4, the constant 19**: `2 e^{1/4} (√2 π e)^{1/2} Γ(1/4) π^{-1/2} < 19`, through
`Γ(1/4)^4 ≤ 64π` and `2048 e³ π < 2048 (68/25)³ (63/20) < 19⁴`. -/
theorem c54_lt_19 : c54 < 19 := by
  apply lt_of_pow_lt_pow_left₀ 4 (by norm_num : (0 : ℝ) ≤ 19)
  rw [c54_pow4]
  have he : exp 1 < 68 / 25 := by have := exp_one_lt_d9; norm_num at this ⊢; linarith
  have hep : 0 < exp 1 := exp_pos 1
  have hpi : π < 63 / 20 := by have := pi_lt_d2; norm_num at this ⊢; linarith
  have hG := gamma_quarter_pow4_le
  have he3 : exp 1 ^ 3 < (68 / 25) ^ 3 := by gcongr
  have he3pos : 0 < exp 1 ^ 3 := by positivity
  calc 32 * exp 1 ^ 3 * Gamma (1 / 4) ^ 4 ≤ 32 * exp 1 ^ 3 * (64 * π) := by gcongr
    _ = 2048 * (exp 1 ^ 3 * π) := by ring
    _ < 2048 * ((68 / 25) ^ 3 * (63 / 20)) := by
        have := mul_lt_mul he3 hpi.le pi_pos (by positivity)
        linarith
    _ < 19 ^ 4 := by norm_num

/-- The display of Lemma 5.4 at `v = 1/4`: `e^{1/4} ρ/(2√(π/4)) (4√2πe/L)^{1/2} Γ(1/4) (1/ρ²)^{1/4}` equals
`c54 √(ρ/L)`; here `(4v/ρ²)^{1/4} = ρ^{-1/2}` at `v = 1/4`. -/
theorem c54_formula (ρ L : ℝ) (hρ : 0 < ρ) (hL : 0 < L) :
    exp (1 / 4) * ρ / (2 * √(π * (1 / 4))) * √(4 * √2 * π * exp 1 / L) * Gamma (1 / 4) * (1 / √ρ)
      = c54 * √(ρ / L) := by
  unfold c54
  obtain ⟨r, hr, rfl⟩ : ∃ r : ℝ, 0 < r ∧ ρ = r ^ 2 :=
    ⟨√ρ, Real.sqrt_pos.mpr hρ, (Real.sq_sqrt hρ.le).symm⟩
  have hpi : 0 < π := pi_pos
  have hsL : 0 < √L := Real.sqrt_pos.mpr hL
  have hsπ : 0 < √π := Real.sqrt_pos.mpr hpi
  have e1 : √(π * (1 / 4)) = √π / 2 := by
    rw [Real.sqrt_mul hpi.le, show (1 / 4 : ℝ) = (1 / 2) ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]; ring
  have e2 : √(4 * √2 * π * exp 1 / L) = 2 * √(√2 * π * exp 1) / √L := by
    rw [Real.sqrt_div (by positivity), show 4 * √2 * π * exp 1 = 2 ^ 2 * (√2 * π * exp 1) by ring,
      Real.sqrt_mul (by norm_num), Real.sqrt_sq (by norm_num)]
  have e3 : √(r ^ 2 / L) = r / √L := by rw [Real.sqrt_div (by positivity), Real.sqrt_sq hr.le]
  rw [e1, e2, e3, Real.sqrt_sq hr.le]
  field_simp

/-- Lemma 5.4, diagonal case: `|S_ii| ≥ L/2` gives `2√(2ρ/|S_ii|) ≤ 4√(ρ/L)`. -/
theorem lemma54_diag (ρ L s : ℝ) (hρ : 0 ≤ ρ) (hL : 0 < L) (hs : L / 2 ≤ s) :
    2 * √(2 * ρ / s) ≤ 4 * √(ρ / L) := by
  have hs0 : 0 < s := by linarith
  have hL' : L ≠ 0 := hL.ne'
  have h1 : 2 * ρ / s ≤ 4 * (ρ / L) := by
    rw [div_le_iff₀ hs0]
    have h := mul_le_mul_of_nonneg_left hs (show (0 : ℝ) ≤ 4 * (ρ / L) by positivity)
    have e : 4 * (ρ / L) * (L / 2) = 2 * ρ := by field_simp; ring
    linarith
  have h4 : √(4 : ℝ) = 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  calc 2 * √(2 * ρ / s) ≤ 2 * √(4 * (ρ / L)) := by gcongr
    _ = 4 * √(ρ / L) := by rw [Real.sqrt_mul (by norm_num) (ρ / L), h4]; ring

/-- `log 19 < 3`, since `19 < 2.7182818283³ < e³`. -/
theorem log19_lt_three : log 19 < 3 := by
  rw [log_lt_iff_lt_exp (by norm_num)]
  have h := exp_one_gt_d9
  have h3 : (2.7182818283 : ℝ) ^ 3 < exp 1 ^ 3 := by gcongr
  have e : exp 1 ^ 3 = exp 3 := by rw [← Real.exp_nat_mul]; norm_num
  calc (19 : ℝ) < 2.7182818283 ^ 3 := by norm_num
    _ < exp 1 ^ 3 := h3
    _ = exp 3 := e

/-- Lemma 5.4: `L₀ = 2 + 2 log 19 < 8`. -/
theorem L0_lt_eight : 2 + 2 * log 19 < 8 := by linarith [log19_lt_three]

/-- Layer cake in Lemma 5.4: `19 e^{-u/2} = 1` at `u₀ = 2 log 19`, so the tail `∫_{u₀}^∞ 19 e^{-u/2} du = 38 e^{-u₀/2}`
equals `2`. -/
theorem layer_cake_switch : 19 * exp (-(2 * log 19) / 2) = 1 ∧ 38 * exp (-(2 * log 19) / 2) = 2 := by
  have e : exp (-(2 * log 19) / 2) = 1 / 19 := by
    rw [show -(2 * log 19) / 2 = -log 19 by ring, exp_neg, exp_log (by norm_num)]; norm_num
  rw [e]; norm_num

/-! ### Lemma 5.5 -/

/-- `(1 + √(1+d))(1 + √(1-d)) ≤ 4` for `0 ≤ d ≤ 1`. -/
theorem J_product_le (d : ℝ) (h0 : 0 ≤ d) (h1 : d ≤ 1) : (1 + √(1 + d)) * (1 + √(1 - d)) ≤ 4 := by
  set a := √(1 + d) with ha
  set b := √(1 - d) with hb
  have ha0 : 0 ≤ a := Real.sqrt_nonneg _
  have hb0 : 0 ≤ b := Real.sqrt_nonneg _
  have ha2 : a ^ 2 = 1 + d := Real.sq_sqrt (by linarith)
  have hb2 : b ^ 2 = 1 - d := Real.sq_sqrt (by linarith)
  have hab : a * b ≤ 1 := by nlinarith [sq_nonneg (a - b)]
  have hsum : a + b ≤ 2 := by nlinarith [sq_nonneg (a - b), sq_nonneg (a + b)]
  nlinarith

/-- `J(1) = π + 2 log(1 + √2) < π + 4 log 2`. -/
theorem J_one_lt : π + 2 * log (1 + √2) < π + 4 * log 2 := by
  have hs : √2 < 3 := by
    rw [show (3 : ℝ) = √9 by rw [show (9 : ℝ) = 3 ^ 2 by norm_num]; exact (Real.sqrt_sq (by norm_num)).symm]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have h : log (1 + √2) < log 4 := log_lt_log (by positivity) (by linarith)
  have e : log 4 = 2 * log 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num, log_pow]; norm_num
  linarith

/-- For `d > 1` and `x ∈ [-1, 1]`, `|x - d| ≥ |x - 1|`, so `J(d) ≤ J(1)`. -/
theorem J_far_compare (d x : ℝ) (hd : 1 < d) (hx1 : -1 ≤ x) (hx2 : x ≤ 1) : |x - 1| ≤ |x - d| := by
  rw [abs_of_nonpos (by linarith), abs_of_neg (by linarith)]
  linarith

/-- The antiderivative of `y^{-1/2}(y+d)^{-1/2}` on `y > 0`: `2 log(√y + √(y+d))`. -/
theorem deriv_log_branch_plus (d y : ℝ) (hd : 0 < d) (hy : 0 < y) :
    HasDerivAt (fun y => 2 * log (√y + √(y + d))) (1 / (√y * √(y + d))) y := by
  have hy' : 0 < y + d := by linarith
  have h1 : HasDerivAt (fun y => √y) (1 / (2 * √y)) y := Real.hasDerivAt_sqrt hy.ne'
  have h2 : HasDerivAt (fun y => √(y + d)) (1 / (2 * √(y + d))) y := by
    have := (Real.hasDerivAt_sqrt hy'.ne').comp y ((hasDerivAt_id y).add_const d)
    simpa using this
  have hs1 : 0 < √y := Real.sqrt_pos.mpr hy
  have hs2 : 0 < √(y + d) := Real.sqrt_pos.mpr hy'
  have hsum : 0 < √y + √(y + d) := by positivity
  have h3 := ((h1.add h2).log hsum.ne').const_mul 2
  simp only [Pi.add_apply] at h3
  convert h3 using 1
  field_simp
  ring

/-- The antiderivative of `x^{-1/2}(d-x)^{-1/2}` on `0 < x < d`: `2 arcsin √(x/d)`. -/
theorem deriv_arcsin_branch (d x : ℝ) (hx : 0 < x) (hxd : x < d) :
    HasDerivAt (fun x => 2 * arcsin (√(x / d))) (1 / (√x * √(d - x))) x := by
  have hd : 0 < d := by linarith
  have hq : 0 < x / d := div_pos hx hd
  have hq1 : x / d < 1 := (div_lt_one hd).mpr hxd
  have hs : 0 < √(x / d) := Real.sqrt_pos.mpr hq
  have hs1 : √(x / d) < 1 := by
    rw [show (1 : ℝ) = √1 by simp]; exact Real.sqrt_lt_sqrt hq.le hq1
  have h1 : HasDerivAt (fun x => √(x / d)) (1 / d / (2 * √(x / d))) x := by
    have := (Real.hasDerivAt_sqrt hq.ne').comp x ((hasDerivAt_id x).div_const d)
    simpa [div_eq_mul_inv, mul_comm] using this
  have h2 := ((Real.hasDerivAt_arcsin (by linarith) hs1.ne).comp x h1).const_mul 2
  convert h2 using 1
  have hsq : √(x / d) ^ 2 = x / d := Real.sq_sqrt hq.le
  have hx' : 0 < √x := Real.sqrt_pos.mpr hx
  have hdx : 0 < d - x := by linarith
  have hdx' : 0 < √(d - x) := Real.sqrt_pos.mpr hdx
  have e1 : √(1 - √(x / d) ^ 2) = √(d - x) / √d := by
    rw [hsq, show 1 - x / d = (d - x) / d by field_simp, Real.sqrt_div hdx.le]
  have e2 : √(x / d) = √x / √d := Real.sqrt_div hx.le d
  have hsd : 0 < √d := Real.sqrt_pos.mpr hd
  have hd2 : √d * √d = d := Real.mul_self_sqrt hd.le
  rw [e1, e2]
  field_simp
  rw [Real.sq_sqrt hd.le]

/-- The antiderivative of `x^{-1/2}(x-d)^{-1/2}` on `x > d > 0`: `2 log(√x + √(x-d))`. -/
theorem deriv_log_branch_minus (d x : ℝ) (hd : 0 < d) (hx : d < x) :
    HasDerivAt (fun x => 2 * log (√x + √(x - d))) (1 / (√x * √(x - d))) x := by
  have hx0 : 0 < x := by linarith
  have hxd : 0 < x - d := by linarith
  have h1 : HasDerivAt (fun x => √x) (1 / (2 * √x)) x := Real.hasDerivAt_sqrt hx0.ne'
  have h2 : HasDerivAt (fun x => √(x - d)) (1 / (2 * √(x - d))) x := by
    have := (Real.hasDerivAt_sqrt hxd.ne').comp x ((hasDerivAt_id x).sub_const d)
    simpa using this
  have hs1 : 0 < √x := Real.sqrt_pos.mpr hx0
  have hs2 : 0 < √(x - d) := Real.sqrt_pos.mpr hxd
  have hsum : 0 < √x + √(x - d) := by positivity
  have h3 := ((h1.add h2).log hsum.ne').const_mul 2
  simp only [Pi.add_apply] at h3
  convert h3 using 1
  field_simp
  ring

/-! ### Lemma 5.6 -/

/-- The definite case of Lemma 5.6: `2√(2π) < 6`. -/
theorem pairhalf_definite_const : 2 * √(2 * π) < 6 := by
  have hpi := pi_lt_d2
  have h : √(2 * π) < 3 := by
    rw [show (3 : ℝ) = √9 by rw [show (9 : ℝ) = 3 ^ 2 by norm_num]; exact (Real.sqrt_sq (by norm_num)).symm]
    exact Real.sqrt_lt_sqrt (by positivity) (by norm_num at hpi ⊢; linarith)
  linarith

/-- At `δ = 1/64`: `4√δ (8 + log(16/δ)) = 4 + 5 log 2`. -/
theorem pairhalf_delta_value : 4 * √(1 / 64 : ℝ) * (8 + log (16 / (1 / 64))) = 4 + 5 * log 2 := by
  have h1 : √(1 / 64 : ℝ) = 1 / 8 := by
    rw [show (1 / 64 : ℝ) = (1 / 8) ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  have h2 : log (16 / (1 / 64) : ℝ) = 10 * log 2 := by
    rw [show (16 / (1 / 64) : ℝ) = 2 ^ 10 by norm_num, log_pow]; norm_num
  rw [h1, h2]; ring

/-- `δ^{-1/2} + (4 + 5 log 2) = 12 + 5 log 2 < 16` at `δ = 1/64`. -/
theorem pairhalf_total : (1 / √(1 / 64 : ℝ)) + (4 + 5 * log 2) < 16 := by
  have h1 : √(1 / 64 : ℝ) = 1 / 8 := by
    rw [show (1 / 64 : ℝ) = (1 / 8) ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  rw [h1]
  have := log_two_lt_d9; norm_num at this ⊢; linarith

/-- (5.1) in Lemma 5.6: `∫_0^∞ min{1, 2M s^{-2}} ds = √(2M) + 2M/√(2M) = 2√(2M)`. -/
theorem bounded_half_value (M : ℝ) (hM : 0 < M) : √(2 * M) + 2 * M / √(2 * M) = 2 * √(2 * M) := by
  have hs : 0 < √(2 * M) := Real.sqrt_pos.mpr (by positivity)
  have h : √(2 * M) * √(2 * M) = 2 * M := Real.mul_self_sqrt (by positivity)
  field_simp
  linarith

/-- The antiderivative behind `∫_{-δ}^{δ} h(y)|y|^{-1/2} dy = 4√δ(8 + log(16/δ))` in Lemma 5.6:
on `y > 0`, `d/dy [2√y (8 + log(16/y))] = y^{-1/2} (6 + log(16/y))`. -/
theorem deriv_halfmoment_kernel (y : ℝ) (hy : 0 < y) :
    HasDerivAt (fun y => 2 * √y * (8 + log (16 / y))) ((6 + log (16 / y)) / √y) y := by
  have h1 : HasDerivAt (fun y => √y) (1 / (2 * √y)) y := Real.hasDerivAt_sqrt hy.ne'
  have h2 : HasDerivAt (fun y => log (16 / y)) (-(1 / y)) y := by
    have hq : HasDerivAt (fun y => 16 / y) (-(16 / y ^ 2)) y := by
      have := (hasDerivAt_inv hy.ne').const_mul 16
      simpa [div_eq_mul_inv] using this
    have := hq.log (by positivity)
    convert this using 1
    field_simp
  have h3 := (h1.const_mul 2).mul (h2.const_add 8)
  convert h3 using 1
  have hs : 0 < √y := Real.sqrt_pos.mpr hy
  field_simp
  rw [Real.sq_sqrt hy.le]
  ring

/-- Lemma 5.6: with `Y = (q - v)/√D` and `b = (a - v)/√D`, `|q - a| = √D |Y - b|`, so
`E|q(W) - a|^{-1/2} = D^{-1/4} E|Y - b|^{-1/2}`. -/
theorem pairhalf_scaling (q a v D : ℝ) (hD : 0 < D) :
    |q - a| = √D * |(q - v) / √D - (a - v) / √D| := by
  have hs : 0 < √D := Real.sqrt_pos.mpr hD
  rw [show (q - v) / √D - (a - v) / √D = (q - a) / √D by ring, abs_div, abs_of_pos hs]
  field_simp

end QformFiveB
