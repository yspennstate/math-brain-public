import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.Tactic

/-!
Lemma 2.1(c) of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): for every real random variable `Z` with law `μ`, every `a ∈ ℝ` and every `v > 0`,
`E e^{-v(Z-a)²} = (2√(πv))^{-1} ∫ e^{-t²/(4v)} e^{-ita} φ_Z(t) dt`.

* `gauss_fourier`: `∫ e^{ixt} e^{-t²/(4v)} dt = 2√(πv) e^{-v x²}`, from Mathlib's `fourierIntegral_gaussian`.
* `lemma21c`: the identity, by the Gaussian integral at `x = z - a` and Fubini; the integrand on `μ ⊗ dt` has modulus
  `e^{-t²/(4v)}`, which is integrable.
* `lemma21c_bound`: `E e^{-v(Z-a)²} ≤ (2√(πv))^{-1} ∫ e^{-t²/(4v)} |φ_Z(t)| dt`, the form used in Lemmas 2.3 and 5.4.

`chf μ t = ∫ e^{itz} dμ(z)` is the characteristic function `φ_Z` of the paper.
-/

open Complex MeasureTheory

namespace QformFiveB

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

end QformFiveB
