import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Analysis.SpecialFunctions.Gamma.BohrMollerup
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.MeasureTheory.Integral.Gamma
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Integral.IntegralEqImproper
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.Tactic

/-!
The off-diagonal case of (5.2) in Lemma 5.4 of "Quadratic forms with five large singular values have bounded densities"
(repaired text, sha256 90f859b7): if the characteristic function of `R` satisfies `|φ_R(t)| ≤ (4√2 π e/(L|t|))^{1/2}`
for `t ≠ 0` (Corollary 4.4(c) for a partition with `‖S_{I,J}‖_F ≥ L/4`), then `P(|R - a| < ρ) ≤ c₅₄ √(ρ/L)` with
`c₅₄ = 2 e^{1/4} (√2 π e)^{1/2} Γ(1/4) π^{-1/2} < 19` (`lemma54_fourier`, `c54_lt_19`).

The proof is the paper's: `1{|x| < ρ} ≤ e^{1/4} e^{-x²/(4ρ²)}` (`indicator_le_gauss`), Lemma 2.1(c) at `v = 1/(4ρ²)`,
the hypothesis on `|φ_R|` under the integral (`envelope_rewrite`), and `∫ |t|^{-1/2} e^{-ρ²t²} dt = Γ(1/4) ρ^{-1/2}`.
Lemma 2.1(c), the Gamma integral and the constant `c₅₄` with its certificate are repeated from `FiveS2Fourier.lean`,
`FiveS2Gamma.lean` and `FiveS5.lean`.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

namespace Fourier54

section Fourier

open Complex

/-- `∫ c F = c ∫ F` for complex constants, stated with the instances of `ℂ` so that it rewrites. -/
theorem cintegral_const_mul {α : Type*} [MeasurableSpace α] (μ : Measure α) (c : ℂ) (F : α → ℂ) :
    ∫ x, c * F x ∂μ = c * ∫ x, F x ∂μ := integral_const_mul c F

/-- The characteristic function `φ(t) = ∫ e^{itz} dμ(z)`. -/
noncomputable def chf (μ : Measure ℝ) (t : ℝ) : ℂ := ∫ z, cexp (((t * z : ℝ) : ℂ) * I) ∂μ

/-- The Gaussian Fourier integral with `b = 1/(4v)`: `∫ e^{ixt} e^{-t²/(4v)} dt = 2√(πv) e^{-v x²}`. -/
theorem gauss_fourier (v : ℝ) (hv : 0 < v) (x : ℝ) :
    ∫ t : ℝ, cexp (((x * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ)
      = ((2 * Real.sqrt (Real.pi * v) : ℝ) : ℂ) * ((Real.exp (-(v * x ^ 2)) : ℝ) : ℂ) := by
  have hb : 0 < (((1 / (4 * v) : ℝ)) : ℂ).re := by rw [ofReal_re]; positivity
  have h := fourierIntegral_gaussian hb (x : ℂ)
  have hcongr : (fun t : ℝ => cexp (((x * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ))
      = fun t : ℝ => cexp (I * (x : ℂ) * t) * cexp (-(((1 / (4 * v) : ℝ)) : ℂ) * t ^ 2) := by
    funext t
    rw [ofReal_exp]
    congr 1
    · congr 1; push_cast; ring
    · congr 1; push_cast; ring
  rw [hcongr, h]
  have hv' : (v : ℂ) ≠ 0 := by exact_mod_cast hv.ne'
  congr 1
  · have h1 : (Real.pi : ℂ) / (((1 / (4 * v) : ℝ)) : ℂ) = ((4 * Real.pi * v : ℝ) : ℂ) := by
      push_cast
      rw [div_div_eq_mul_div, div_one]
      ring
    rw [h1, show (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) by norm_num, ← ofReal_cpow (by positivity),
      ← Real.sqrt_eq_rpow]
    congr 1
    rw [show (4 : ℝ) * Real.pi * v = 2 ^ 2 * (Real.pi * v) by ring, Real.sqrt_mul (by positivity),
      Real.sqrt_sq (by norm_num)]
  · rw [ofReal_exp]
    congr 1
    push_cast
    field_simp
    try ring

/-- **Lemma 2.1(c).** `E e^{-v(Z-a)²} = (2√(πv))^{-1} ∫ e^{-t²/(4v)} e^{-ita} φ_Z(t) dt`. -/
theorem lemma21c (μ : Measure ℝ) [IsProbabilityMeasure μ] (a v : ℝ) (hv : 0 < v) :
    ((∫ z, Real.exp (-(v * (z - a) ^ 2)) ∂μ : ℝ) : ℂ)
      = ((1 / (2 * Real.sqrt (Real.pi * v)) : ℝ) : ℂ) *
        ∫ t : ℝ, ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ) * cexp (-(((t * a : ℝ) : ℂ) * I)) * chf μ t := by
  have hc : (2 * Real.sqrt (Real.pi * v)) ≠ 0 := by positivity
  have hpt : ∀ z : ℝ, ((Real.exp (-(v * (z - a) ^ 2)) : ℝ) : ℂ)
      = ((1 / (2 * Real.sqrt (Real.pi * v)) : ℝ) : ℂ) *
        ∫ t : ℝ, cexp ((((z - a) * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ) := by
    intro z
    rw [gauss_fourier v hv (z - a), ← mul_assoc, ← ofReal_mul, one_div_mul_cancel hc, ofReal_one, one_mul]
  have hint : Integrable (Function.uncurry fun (z t : ℝ) =>
      cexp ((((z - a) * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ)) (μ.prod volume) := by
    have hg : Integrable (fun p : ℝ × ℝ => Real.exp (-(1 / (4 * v)) * p.2 ^ 2)) (μ.prod volume) :=
      (integrable_exp_neg_mul_sq (by positivity : (0 : ℝ) < 1 / (4 * v))).comp_snd μ
    refine hg.mono' ?_ ?_
    · exact Continuous.aestronglyMeasurable (by fun_prop)
    · refine Filter.Eventually.of_forall (fun p => ?_)
      rcases p with ⟨z, t⟩
      simp only [Function.uncurry_apply_pair]
      rw [norm_mul, norm_exp_ofReal_mul_I, one_mul, Complex.norm_of_nonneg (Real.exp_pos _).le]
  rw [← integral_complex_ofReal]
  simp_rw [hpt]
  rw [cintegral_const_mul, integral_integral_swap hint]
  congr 1
  refine integral_congr_ae (Filter.Eventually.of_forall (fun t => ?_))
  have hsplit : ∀ z : ℝ, cexp ((((z - a) * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ)
      = (((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ) * cexp (-(((t * a : ℝ) : ℂ) * I))) *
        cexp (((t * z : ℝ) : ℂ) * I) := by
    intro z
    have e : cexp ((((z - a) * t : ℝ) : ℂ) * I)
        = cexp (-(((t * a : ℝ) : ℂ) * I)) * cexp (((t * z : ℝ) : ℂ) * I) := by
      rw [← Complex.exp_add]
      congr 1
      push_cast
      ring
    rw [e]
    ring
  simp only [hsplit]
  rw [cintegral_const_mul]
  rfl

/-- **Lemma 2.1(c), the bound used later.** `E e^{-v(Z-a)²} ≤ (2√(πv))^{-1} ∫ e^{-t²/(4v)} |φ_Z(t)| dt`. -/
theorem lemma21c_bound (μ : Measure ℝ) [IsProbabilityMeasure μ] (a v : ℝ) (hv : 0 < v) :
    ∫ z, Real.exp (-(v * (z - a) ^ 2)) ∂μ
      ≤ (1 / (2 * Real.sqrt (Real.pi * v))) * ∫ t : ℝ, Real.exp (-(1 / (4 * v)) * t ^ 2) * ‖chf μ t‖ := by
  have h := congrArg (fun w : ℂ => ‖w‖) (lemma21c μ a v hv)
  simp only at h
  have hE : 0 ≤ ∫ z, Real.exp (-(v * (z - a) ^ 2)) ∂μ := integral_nonneg (fun z => (Real.exp_pos _).le)
  have hc : 0 ≤ 1 / (2 * Real.sqrt (Real.pi * v)) := by positivity
  rw [Complex.norm_of_nonneg hE, norm_mul, Complex.norm_of_nonneg hc] at h
  rw [h]
  gcongr
  refine (norm_integral_le_integral_norm _).trans (le_of_eq ?_)
  congr 1
  funext t
  have hphase : ‖cexp (-(((t * a : ℝ) : ℂ) * I))‖ = 1 := by
    rw [← neg_mul, ← ofReal_neg, norm_exp_ofReal_mul_I]
  rw [norm_mul, norm_mul, Complex.norm_of_nonneg (Real.exp_pos _).le, hphase, mul_one]

end Fourier

section Constants

open Real

/-- **Lemma 5.4, the integral.** `∫_ℝ |t|^{-1/2} e^{-w t²} dt = Γ(1/4) w^{-1/4}` for `w > 0`. -/
theorem concentration_gamma_integral (w : ℝ) (hw : 0 < w) :
    ∫ t : ℝ, |t| ^ (-(1 / 2 : ℝ)) * exp (-w * |t| ^ (2 : ℝ)) = Gamma (1 / 4) * w ^ (-(1 / 4 : ℝ)) := by
  have h := integral_comp_abs (f := fun y : ℝ => y ^ (-(1 / 2 : ℝ)) * exp (-w * y ^ (2 : ℝ)))
  simp only at h
  rw [h, integral_rpow_mul_exp_neg_mul_rpow (p := 2) (q := -(1 / 2)) (b := w) (by norm_num) (by norm_num) hw,
    show (-(-(1 / 2 : ℝ) + 1) / 2) = -(1 / 4) by norm_num, show ((-(1 / 2 : ℝ) + 1) / 2) = 1 / 4 by norm_num]
  ring

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

end Constants

/-! ### The off-diagonal case of (5.2) -/

/-- `1{|z - a| < ρ} ≤ e^{1/4} e^{-(z - a)²/(4ρ²)}`. -/
theorem indicator_le_gauss (a ρ z : ℝ) (hρ : 0 < ρ) :
    (Ioo (a - ρ) (a + ρ)).indicator (fun _ => (1 : ℝ≥0∞)) z
      ≤ ENNReal.ofReal (Real.exp (1 / 4) * Real.exp (-(1 / (4 * ρ ^ 2) * (z - a) ^ 2))) := by
  by_cases hz : z ∈ Ioo (a - ρ) (a + ρ)
  · rw [indicator_of_mem hz, ← ENNReal.ofReal_one]
    apply ENNReal.ofReal_le_ofReal
    rw [← Real.exp_add]
    apply Real.one_le_exp
    have h1 : |z - a| < ρ := abs_lt.2 ⟨by linarith [hz.1], by linarith [hz.2]⟩
    have h2 : (z - a) ^ 2 < ρ ^ 2 := by
      rw [← sq_abs]
      exact pow_lt_pow_left₀ h1 (abs_nonneg _) (by norm_num)
    have h3 : 1 / (4 * ρ ^ 2) * (z - a) ^ 2 ≤ 1 / 4 := by
      rw [div_mul_eq_mul_div, one_mul, div_le_div_iff₀ (by positivity) (by norm_num)]
      linarith
    linarith
  · rw [indicator_of_notMem hz]
    exact zero_le _

/-- For `t ≠ 0` and at `t = 0` alike: `e^{-ρ²t²} (C/(L|t|))^{1/2} = (C/L)^{1/2} |t|^{-1/2} e^{-ρ²|t|²}`. -/
theorem envelope_rewrite (C L ρ t : ℝ) (hC : 0 ≤ C) (hL : 0 < L) :
    Real.exp (-(ρ ^ 2) * t ^ 2) * Real.sqrt (C / (L * |t|))
      = Real.sqrt (C / L) * (|t| ^ (-(1 / 2 : ℝ)) * Real.exp (-(ρ ^ 2) * |t| ^ (2 : ℝ))) := by
  rcases eq_or_ne t 0 with rfl | ht
  · rw [abs_zero, Real.zero_rpow (by norm_num : (-(1 / 2 : ℝ)) ≠ 0)]
    simp
  · have hat : 0 < |t| := abs_pos.2 ht
    rw [Real.rpow_two, sq_abs, show C / (L * |t|) = C / L / |t| by rw [div_div],
      Real.sqrt_div (div_nonneg hC hL.le) |t|, Real.rpow_neg (abs_nonneg t), ← Real.sqrt_eq_rpow]
    ring

/-- **Lemma 5.4, the off-diagonal case of (5.2).** If `|φ_R(t)| ≤ (4√2 π e/(L|t|))^{1/2}` for all `t ≠ 0` (Corollary
4.4(c) with `‖S_{I,J}‖_F ≥ L/4`), then `P(|R - a| < ρ) ≤ c₅₄ √(ρ/L)` with `c₅₄ < 19`, by
`1{|x| < ρ} ≤ e^{1/4} e^{-x²/(4ρ²)}` and Lemma 2.1(c). -/
theorem lemma54_fourier (μ : Measure ℝ) [IsProbabilityMeasure μ] (L : ℝ) (hL : 0 < L)
    (hφ : ∀ t : ℝ, t ≠ 0 → ‖chf μ t‖ ≤ Real.sqrt (4 * Real.sqrt 2 * Real.pi * Real.exp 1 / (L * |t|)))
    (a ρ : ℝ) (hρ : 0 < ρ) :
    μ (Ioo (a - ρ) (a + ρ)) ≤ ENNReal.ofReal (c54 * Real.sqrt (ρ / L)) := by
  have hC0 : 0 < 4 * Real.sqrt 2 * Real.pi * Real.exp 1 := by positivity
  have hv0 : 0 < 1 / (4 * ρ ^ 2) := by positivity
  -- the indicator bound
  have hint1 : Integrable (fun z => Real.exp (1 / 4) * Real.exp (-(1 / (4 * ρ ^ 2) * (z - a) ^ 2))) μ := by
    refine Integrable.mono' (integrable_const (Real.exp (1 / 4)))
      (by fun_prop : Measurable fun z => Real.exp (1 / 4) * Real.exp (-(1 / (4 * ρ ^ 2) * (z - a) ^ 2))).aestronglyMeasurable
      (Filter.Eventually.of_forall (fun z => ?_))
    rw [Real.norm_eq_abs, abs_of_pos (by positivity)]
    have h1 : Real.exp (-(1 / (4 * ρ ^ 2) * (z - a) ^ 2)) ≤ 1 := Real.exp_le_one_iff.2 (by
      have : 0 ≤ 1 / (4 * ρ ^ 2) * (z - a) ^ 2 := by positivity
      linarith)
    have h2 : 0 < Real.exp (1 / 4) := Real.exp_pos _
    nlinarith
  have step1 : μ (Ioo (a - ρ) (a + ρ))
      ≤ ENNReal.ofReal (Real.exp (1 / 4) * ∫ z, Real.exp (-(1 / (4 * ρ ^ 2) * (z - a) ^ 2)) ∂μ) := by
    rw [← integral_const_mul, ofReal_integral_eq_lintegral_ofReal hint1
      (Filter.Eventually.of_forall (fun z => by positivity)), ← one_mul (μ (Ioo (a - ρ) (a + ρ))),
      ← lintegral_indicator_const measurableSet_Ioo]
    exact lintegral_mono (fun z => indicator_le_gauss a ρ z hρ)
  -- Lemma 2.1(c)
  have h21 := lemma21c_bound μ a (1 / (4 * ρ ^ 2)) hv0
  have e4v : 1 / (4 * (1 / (4 * ρ ^ 2))) = ρ ^ 2 := by
    field_simp <;> ring
  -- the Fourier integral
  have hG : ∫ t : ℝ, |t| ^ (-(1 / 2 : ℝ)) * Real.exp (-(ρ ^ 2) * |t| ^ (2 : ℝ))
      = Real.Gamma (1 / 4) * (ρ ^ 2) ^ (-(1 / 4 : ℝ)) := concentration_gamma_integral (ρ ^ 2) (by positivity)
  have hGpos : 0 < Real.Gamma (1 / 4) * (ρ ^ 2) ^ (-(1 / 4 : ℝ)) :=
    mul_pos (Real.Gamma_pos_of_pos (by norm_num)) (Real.rpow_pos_of_pos (by positivity) _)
  have hGint : Integrable (fun t : ℝ => |t| ^ (-(1 / 2 : ℝ)) * Real.exp (-(ρ ^ 2) * |t| ^ (2 : ℝ))) :=
    Integrable.of_integral_ne_zero (by rw [hG]; exact hGpos.ne')
  have hne : ∀ᵐ t ∂(volume : Measure ℝ), t ≠ 0 := by
    rw [ae_iff]
    simp
  have step3 : ∫ t : ℝ, Real.exp (-(1 / (4 * (1 / (4 * ρ ^ 2)))) * t ^ 2) * ‖chf μ t‖
      ≤ Real.sqrt (4 * Real.sqrt 2 * Real.pi * Real.exp 1 / L)
          * (Real.Gamma (1 / 4) * (ρ ^ 2) ^ (-(1 / 4 : ℝ))) := by
    rw [e4v, ← hG, ← integral_const_mul]
    refine integral_mono_of_nonneg (Filter.Eventually.of_forall (fun t => by positivity))
      (hGint.const_mul _) ?_
    filter_upwards [hne] with t ht
    rw [← envelope_rewrite _ L ρ t hC0.le hL]
    exact mul_le_mul_of_nonneg_left (hφ t ht) (Real.exp_pos _).le
  -- the constant
  have hsπ : 0 < Real.sqrt Real.pi := Real.sqrt_pos.2 Real.pi_pos
  have hsρ : 0 < Real.sqrt ρ := Real.sqrt_pos.2 hρ
  have hA : Real.sqrt (Real.pi * (1 / (4 * ρ ^ 2))) = Real.sqrt Real.pi / (2 * ρ) := by
    rw [show Real.pi * (1 / (4 * ρ ^ 2)) = (Real.sqrt Real.pi / (2 * ρ)) ^ 2 by
      rw [div_pow, Real.sq_sqrt Real.pi_pos.le]
      field_simp <;> ring, Real.sqrt_sq (by positivity)]
  have hB : (ρ ^ 2) ^ (-(1 / 4 : ℝ)) = 1 / Real.sqrt ρ := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hρ.le, show ((2 : ℕ) : ℝ) * (-(1 / 4 : ℝ)) = -(1 / 2) by norm_num,
      Real.rpow_neg hρ.le, ← Real.sqrt_eq_rpow, one_div]
  have hD : Real.sqrt (Real.pi * (1 / 4)) = Real.sqrt Real.pi / 2 := by
    rw [Real.sqrt_mul Real.pi_pos.le, show (1 / 4 : ℝ) = (1 / 2) ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
    ring
  calc μ (Ioo (a - ρ) (a + ρ))
      ≤ ENNReal.ofReal (Real.exp (1 / 4) * ∫ z, Real.exp (-(1 / (4 * ρ ^ 2) * (z - a) ^ 2)) ∂μ) := step1
    _ ≤ ENNReal.ofReal (Real.exp (1 / 4) * ((1 / (2 * Real.sqrt (Real.pi * (1 / (4 * ρ ^ 2))))) *
          (Real.sqrt (4 * Real.sqrt 2 * Real.pi * Real.exp 1 / L)
            * (Real.Gamma (1 / 4) * (ρ ^ 2) ^ (-(1 / 4 : ℝ)))))) := by
        apply ENNReal.ofReal_le_ofReal
        apply mul_le_mul_of_nonneg_left _ (Real.exp_pos _).le
        exact h21.trans (mul_le_mul_of_nonneg_left step3 (by positivity))
    _ = ENNReal.ofReal (c54 * Real.sqrt (ρ / L)) := by
        congr 1
        rw [← c54_formula ρ L hρ hL, hA, hB, hD]
        field_simp <;> ring

end Fourier54

end QformFiveB
