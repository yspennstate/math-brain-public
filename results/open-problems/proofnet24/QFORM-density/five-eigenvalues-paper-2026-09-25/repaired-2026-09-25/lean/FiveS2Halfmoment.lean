import Mathlib.MeasureTheory.Integral.Gamma
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.MeasureTheory.Integral.IntegralEqImproper
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Measure.CharacteristicFunction.TaylorExpansion
import Mathlib.Tactic

/-!
Lemma 2.3 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): for every real random variable `Z` and every `a`,
`E|Z - a|^{-1/2} ≤ (2π)^{-1/2} ∫ |t|^{-1/2} |φ_Z(t)| dt`, where both sides may be infinite and `|0|^{-1/2} = ∞`.

Both sides live in `[0, ∞]` (lower Lebesgue integrals), so nothing is assumed about integrability. The proof is the
paper's: `|z - a|^{-1/2} = Γ(1/4)^{-1} ∫_0^∞ v^{-3/4} e^{-v(z-a)²} dv` (`halfmoment_rep`, both sides `∞` at `z = a`),
Tonelli, the bound of Lemma 2.1(c) (`inner_z_bound`), Tonelli again, and
`∫_0^∞ v^{-5/4} e^{-t²/(4v)} dv = 4^{1/4} Γ(1/4) |t|^{-1/2}` with `4^{1/4}/(2√π) = 1/√(2π)` (`halfmoment_kernel`).
The envelope consequence `8√(u/(2π))` is `FiveS2Envelope.lean`.

So that the file compiles on its own, the Gamma integrals of `FiveS2Gamma.lean` and Lemma 2.1(c) of
`FiveS2Fourier.lean` are repeated here, with their proofs, in the namespace `QformFiveB.Half`. `chf μ` is shown equal to
Mathlib's `charFun μ` (`chf_eq_charFun`), whose continuity and bound `‖φ‖ ≤ 1` are used.
-/

namespace QformFiveB

namespace Half

section GammaPart

open Real MeasureTheory Set

/-- `(1/z²)^{1/4} = |z|^{-1/2}` for `z ≠ 0`. -/
theorem inv_sq_rpow_quarter (z : ℝ) (hz : z ≠ 0) : (1 / z ^ 2) ^ (1 / 4 : ℝ) = |z| ^ (-(1 / 2 : ℝ)) := by
  have ha : 0 < |z| := abs_pos.mpr hz
  rw [← sq_abs z, one_div, ← Real.rpow_natCast, Real.inv_rpow (by positivity), ← Real.rpow_mul ha.le,
    Real.rpow_neg ha.le]
  norm_num

/-- **Lemma 2.3, the representation.** `∫_0^∞ v^{-3/4} e^{-v z²} dv = Γ(1/4) |z|^{-1/2}` for `z ≠ 0`. -/
theorem halfmoment_gamma_identity (z : ℝ) (hz : z ≠ 0) :
    ∫ v in Ioi (0 : ℝ), v ^ (-(3 / 4 : ℝ)) * exp (-(z ^ 2 * v)) = |z| ^ (-(1 / 2 : ℝ)) * Gamma (1 / 4) := by
  have hz2 : 0 < z ^ 2 := by positivity
  have h := Real.integral_rpow_mul_exp_neg_mul_Ioi (a := 1 / 4) (r := z ^ 2) (by norm_num) hz2
  rw [show (1 / 4 : ℝ) - 1 = -(3 / 4) by norm_num, inv_sq_rpow_quarter z hz] at h
  exact h

/-- `4^{1/4}/(2√π) = 1/√(2π)`, the constant of (2.1). -/
theorem halfmoment_constant : (4 : ℝ) ^ (1 / 4 : ℝ) / (2 * √π) = 1 / √(2 * π) := by
  have h4 : (4 : ℝ) ^ (1 / 4 : ℝ) = √2 := by
    rw [Real.sqrt_eq_rpow, show (4 : ℝ) = 2 ^ (2 : ℝ) by norm_num, ← Real.rpow_mul (by norm_num)]; norm_num
  have hpi : 0 < π := pi_pos
  have hs2 : √2 * √2 = 2 := Real.mul_self_sqrt (by norm_num)
  have hspi : 0 < √π := Real.sqrt_pos.mpr hpi
  rw [h4, Real.sqrt_mul (by norm_num) π]
  field_simp
  linarith [hs2]

/-- **Lemma 2.3, after the exchange.** `∫_0^∞ v^{-5/4} e^{-t²/(4v)} dv = 4^{1/4} Γ(1/4) |t|^{-1/2}` for `t ≠ 0`, by the
substitution `v = 1/x`. -/
theorem halfmoment_gamma_identity2 (t : ℝ) (ht : t ≠ 0) :
    ∫ v in Ioi (0 : ℝ), v ^ (-(5 / 4 : ℝ)) * exp (-(t ^ 2 / (4 * v)))
      = (4 : ℝ) ^ (1 / 4 : ℝ) * Gamma (1 / 4) * |t| ^ (-(1 / 2 : ℝ)) := by
  have key := integral_comp_rpow_Ioi (fun y : ℝ => y ^ (-(5 / 4 : ℝ)) * exp (-(t ^ 2 / (4 * y))))
    (p := -1) (by norm_num)
  simp only [smul_eq_mul] at key
  rw [← key]
  have hcongr : ∀ x ∈ Ioi (0 : ℝ),
      |(-1 : ℝ)| * x ^ ((-1 : ℝ) - 1) * ((x ^ (-1 : ℝ)) ^ (-(5 / 4 : ℝ)) * exp (-(t ^ 2 / (4 * x ^ (-1 : ℝ)))))
        = x ^ ((1 / 4 : ℝ) - 1) * exp (-((t ^ 2 / 4) * x)) := by
    intro x hx
    have hx0 : 0 < x := hx
    rw [abs_neg, abs_one, one_mul, ← Real.rpow_mul hx0.le, Real.rpow_neg_one]
    have e1 : x ^ ((-1 : ℝ) - 1) * x ^ ((-1 : ℝ) * (-(5 / 4 : ℝ))) = x ^ ((1 / 4 : ℝ) - 1) := by
      rw [← Real.rpow_add hx0]; norm_num
    have e2 : t ^ 2 / (4 * x⁻¹) = t ^ 2 / 4 * x := by field_simp
    rw [e2, ← e1]; ring
  rw [setIntegral_congr_fun measurableSet_Ioi hcongr]
  have ht2 : 0 < t ^ 2 / 4 := by positivity
  rw [Real.integral_rpow_mul_exp_neg_mul_Ioi (by norm_num) ht2]
  have hq : (1 / (t ^ 2 / 4)) ^ (1 / 4 : ℝ) = (4 : ℝ) ^ (1 / 4 : ℝ) * |t| ^ (-(1 / 2 : ℝ)) := by
    rw [show 1 / (t ^ 2 / 4) = 4 * (1 / t ^ 2) by field_simp, Real.mul_rpow (by norm_num) (by positivity),
      inv_sq_rpow_quarter t ht]
  rw [hq]; ring

/-- **Lemma 5.4, the integral.** `∫_ℝ |t|^{-1/2} e^{-w t²} dt = Γ(1/4) w^{-1/4}` for `w > 0`. -/
theorem concentration_gamma_integral (w : ℝ) (hw : 0 < w) :
    ∫ t : ℝ, |t| ^ (-(1 / 2 : ℝ)) * exp (-w * |t| ^ (2 : ℝ)) = Gamma (1 / 4) * w ^ (-(1 / 4 : ℝ)) := by
  have h := integral_comp_abs (f := fun y : ℝ => y ^ (-(1 / 2 : ℝ)) * exp (-w * y ^ (2 : ℝ)))
  simp only at h
  rw [h, integral_rpow_mul_exp_neg_mul_rpow (p := 2) (q := -(1 / 2)) (b := w) (by norm_num) (by norm_num) hw,
    show (-(-(1 / 2 : ℝ) + 1) / 2) = -(1 / 4) by norm_num, show ((-(1 / 2 : ℝ) + 1) / 2) = 1 / 4 by norm_num]
  ring

end GammaPart

section FourierPart

open Complex MeasureTheory

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

end FourierPart

section HalfMomentPart

open MeasureTheory Set

/-- The paper's `φ_Z` is Mathlib's characteristic function. -/
theorem chf_eq_charFun (μ : Measure ℝ) (t : ℝ) : chf μ t = charFun μ t := by
  rw [charFun_apply_real]
  unfold chf
  congr 1
  funext z
  rw [Complex.ofReal_mul]

theorem chf_continuous (μ : Measure ℝ) [IsProbabilityMeasure μ] : Continuous (chf μ) := by
  have h : chf μ = charFun μ := funext (chf_eq_charFun μ)
  rw [h]
  exact continuous_charFun

theorem chf_norm_le_one (μ : Measure ℝ) [IsProbabilityMeasure μ] (t : ℝ) : ‖chf μ t‖ ≤ 1 := by
  rw [chf_eq_charFun]
  exact norm_charFun_le_one t

theorem ofReal_mul_ofReal {p q : ℝ} (hp : 0 ≤ p) :
    ENNReal.ofReal p * ENNReal.ofReal q = ENNReal.ofReal (p * q) := (ENNReal.ofReal_mul hp).symm

/-- `∫_0^∞ v^{-3/4} dv = ∞`. -/
theorem lintegral_rpow_three_quarters_top :
    ∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ))) = ⊤ := by
  have hnot : ¬ IntegrableOn (fun v : ℝ => v ^ (-(3 / 4 : ℝ))) (Ioi 1) := by
    rw [integrableOn_Ioi_rpow_iff (by norm_num : (0 : ℝ) < 1)]
    norm_num
  have hmeas : AEStronglyMeasurable (fun v : ℝ => v ^ (-(3 / 4 : ℝ))) (volume.restrict (Ioi 1)) :=
    (by fun_prop : Measurable fun v : ℝ => v ^ (-(3 / 4 : ℝ))).aestronglyMeasurable
  have h0 : 0 ≤ᵐ[volume.restrict (Ioi (1 : ℝ))] fun v : ℝ => v ^ (-(3 / 4 : ℝ)) :=
    (ae_restrict_iff' measurableSet_Ioi).mpr
      (Filter.Eventually.of_forall (fun v hv => (Real.rpow_pos_of_pos (lt_trans zero_lt_one hv) _).le))
  have htop1 : ∫⁻ v in Ioi (1 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ))) = ⊤ := by
    by_contra hne
    exact hnot ⟨hmeas, (hasFiniteIntegral_iff_ofReal h0).mpr (lt_top_iff_ne_top.mpr hne)⟩
  apply eq_top_iff.mpr
  rw [← htop1]
  exact lintegral_mono_set (Ioi_subset_Ioi zero_le_one)

/-- `|z - a|^{-1/2} ≤ Γ(1/4)^{-1} ∫_0^∞ v^{-3/4} e^{-v (z-a)²} dv` in `[0, ∞]`, with equality; at `z = a` both sides are
`∞`. -/
theorem halfmoment_rep (a z : ℝ) :
    (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ))
      ≤ ENNReal.ofReal (1 / Real.Gamma (1 / 4)) *
        ∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v))) := by
  have hG : 0 < Real.Gamma (1 / 4) := Real.Gamma_pos_of_pos (by norm_num)
  have hc : ENNReal.ofReal (1 / Real.Gamma (1 / 4)) ≠ 0 := (ENNReal.ofReal_pos.mpr (by positivity)).ne'
  by_cases hz : z = a
  · subst hz
    have e : ∀ v : ℝ, v ^ (-(3 / 4 : ℝ)) * Real.exp (-((0 : ℝ) ^ 2 * v)) = v ^ (-(3 / 4 : ℝ)) := by
      intro v
      simp
    simp only [sub_self, abs_zero, ENNReal.ofReal_zero, e]
    rw [ENNReal.zero_rpow_of_neg (by norm_num), lintegral_rpow_three_quarters_top, ENNReal.mul_top hc]
  · have hza : z - a ≠ 0 := sub_ne_zero.mpr hz
    have hpos : 0 < |z - a| := abs_pos.mpr hza
    have hb : 0 < (z - a) ^ 2 := by positivity
    have hint : IntegrableOn (fun v : ℝ => v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v))) (Ioi 0) := by
      have h := integrableOn_rpow_mul_exp_neg_mul_rpow (s := -(3 / 4 : ℝ)) (p := 1) (b := (z - a) ^ 2)
        (by norm_num) le_rfl hb
      refine IntegrableOn.congr_fun h (fun v _ => ?_) measurableSet_Ioi
      simp only [Real.rpow_one, neg_mul]
    have h0 : 0 ≤ᵐ[volume.restrict (Ioi (0 : ℝ))]
        fun v : ℝ => v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v)) :=
      (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall
        (fun v hv => mul_nonneg (Real.rpow_nonneg (le_of_lt hv) _) (Real.exp_pos _).le))
    rw [← ofReal_integral_eq_lintegral_ofReal hint h0, halfmoment_gamma_identity (z - a) hza,
      ENNReal.ofReal_rpow_of_pos hpos, ofReal_mul_ofReal (by positivity)]
    apply le_of_eq
    congr 1
    field_simp

/-- For `v > 0`: `∫ v^{-3/4} e^{-v(z-a)²} dμ(z) ≤ v^{-3/4} ∫ (2√(πv))^{-1} e^{-t²/(4v)} |φ(t)| dt`, by Lemma 2.1(c). -/
theorem inner_z_bound (μ : Measure ℝ) [IsProbabilityMeasure μ] (a v : ℝ) (hv : 0 < v) :
    ∫⁻ z, ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v))) ∂μ
      ≤ ∫⁻ t, ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) *
          ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2))) *
          ENNReal.ofReal ‖chf μ t‖ := by
  have hv34 : 0 ≤ v ^ (-(3 / 4 : ℝ)) := Real.rpow_nonneg hv.le _
  have hchf : Measurable (chf μ) := (chf_continuous μ).measurable
  have e1 : ∀ z, ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v)))
      = ENNReal.ofReal (v ^ (-(3 / 4 : ℝ))) * ENNReal.ofReal (Real.exp (-(v * (z - a) ^ 2))) := by
    intro z
    rw [ofReal_mul_ofReal hv34, mul_comm ((z - a) ^ 2) v]
  have e2 : ∀ t, ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) *
        ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2))) * ENNReal.ofReal ‖chf μ t‖
      = ENNReal.ofReal (v ^ (-(3 / 4 : ℝ))) * ENNReal.ofReal ((1 / (2 * Real.sqrt (Real.pi * v))) *
          (Real.exp (-(1 / (4 * v)) * t ^ 2) * ‖chf μ t‖)) := by
    intro t
    have hq : 0 ≤ v ^ (-(3 / 4 : ℝ)) * ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2)) := by
      positivity
    rw [ofReal_mul_ofReal hq, ofReal_mul_ofReal hv34]
    congr 1
    ring
  simp_rw [e1, e2]
  rw [lintegral_const_mul _ (by fun_prop), lintegral_const_mul _ (by fun_prop)]
  refine mul_le_mul_left' ?_ _
  have hbd : ∀ z : ℝ, ‖Real.exp (-(v * (z - a) ^ 2))‖ ≤ 1 := by
    intro z
    rw [Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
    exact Real.exp_le_one_iff.mpr (by have := mul_nonneg hv.le (sq_nonneg (z - a)); linarith)
  have hintz : Integrable (fun z : ℝ => Real.exp (-(v * (z - a) ^ 2))) μ :=
    (integrable_const (1 : ℝ)).mono' (by fun_prop : Measurable _).aestronglyMeasurable
      (Filter.Eventually.of_forall hbd)
  have hb : (0 : ℝ) < 1 / (4 * v) := by positivity
  have hintt : Integrable (fun t : ℝ => (1 / (2 * Real.sqrt (Real.pi * v))) *
      (Real.exp (-(1 / (4 * v)) * t ^ 2) * ‖chf μ t‖)) := by
    refine ((integrable_exp_neg_mul_sq hb).const_mul (1 / (2 * Real.sqrt (Real.pi * v)))).mono'
      (by fun_prop : Measurable _).aestronglyMeasurable (Filter.Eventually.of_forall (fun t => ?_))
    have hn := chf_norm_le_one μ t
    have he := Real.exp_pos (-(1 / (4 * v)) * t ^ 2)
    have hc : 0 < 1 / (2 * Real.sqrt (Real.pi * v)) := by positivity
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    have : Real.exp (-(1 / (4 * v)) * t ^ 2) * ‖chf μ t‖ ≤ Real.exp (-(1 / (4 * v)) * t ^ 2) := by
      nlinarith [norm_nonneg (chf μ t)]
    exact mul_le_mul_of_nonneg_left this hc.le
  rw [← ofReal_integral_eq_lintegral_ofReal hintz (Filter.Eventually.of_forall (fun z => (Real.exp_pos _).le)),
    ← ofReal_integral_eq_lintegral_ofReal hintt (Filter.Eventually.of_forall (fun t => by positivity))]
  apply ENNReal.ofReal_le_ofReal
  rw [integral_const_mul]
  exact lemma21c_bound μ a v hv

/-- The kernel: for `t ≠ 0`, `∫_0^∞ v^{-3/4} (2√(πv))^{-1} e^{-t²/(4v)} dv = Γ(1/4) |t|^{-1/2} / √(2π)`. -/
theorem halfmoment_kernel (t : ℝ) (ht : t ≠ 0) :
    ∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) *
        ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2)))
      = ENNReal.ofReal (Real.Gamma (1 / 4) * (1 / Real.sqrt (2 * Real.pi)) * |t| ^ (-(1 / 2 : ℝ))) := by
  have hcongr : ∀ v ∈ Ioi (0 : ℝ), v ^ (-(3 / 4 : ℝ)) *
        ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2))
      = 1 / (2 * Real.sqrt Real.pi) * (v ^ (-(5 / 4 : ℝ)) * Real.exp (-(t ^ 2 / (4 * v)))) := by
    intro v hv
    have hv0 : 0 < v := hv
    have hs : 0 < Real.sqrt v := Real.sqrt_pos.mpr hv0
    have hp : 0 < Real.sqrt Real.pi := Real.sqrt_pos.mpr Real.pi_pos
    have e5 : v ^ (-(5 / 4 : ℝ)) = v ^ (-(3 / 4 : ℝ)) / Real.sqrt v := by
      rw [Real.sqrt_eq_rpow, ← Real.rpow_sub hv0]
      norm_num
    have ee : -(1 / (4 * v)) * t ^ 2 = -(t ^ 2 / (4 * v)) := by ring
    rw [Real.sqrt_mul Real.pi_pos.le, e5, ee]
    field_simp
  have hEq : ∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) *
        ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2)))
      = ∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (1 / (2 * Real.sqrt Real.pi) *
          (v ^ (-(5 / 4 : ℝ)) * Real.exp (-(t ^ 2 / (4 * v))))) :=
    setLIntegral_congr_fun measurableSet_Ioi (fun v hv => by rw [hcongr v hv])
  have ht2 : 0 < t ^ 2 / 4 := by positivity
  have hint : IntegrableOn (fun v : ℝ => v ^ (-(5 / 4 : ℝ)) * Real.exp (-(t ^ 2 / (4 * v)))) (Ioi 0) := by
    rw [← integrableOn_Ioi_comp_rpow_iff _ (by norm_num : (-1 : ℝ) ≠ 0)]
    have h := integrableOn_rpow_mul_exp_neg_mul_rpow (s := -(3 / 4 : ℝ)) (p := 1) (b := t ^ 2 / 4)
      (by norm_num) le_rfl ht2
    refine IntegrableOn.congr_fun h (fun x hx => ?_) measurableSet_Ioi
    have hx0 : 0 < x := hx
    simp only [smul_eq_mul]
    rw [abs_neg, abs_one, one_mul, ← Real.rpow_mul hx0.le, Real.rpow_neg_one, Real.rpow_one]
    have e1 : x ^ ((-1 : ℝ) - 1) * x ^ ((-1 : ℝ) * (-(5 / 4 : ℝ))) = x ^ (-(3 / 4 : ℝ)) := by
      rw [← Real.rpow_add hx0]; norm_num
    have e2 : t ^ 2 / (4 * x⁻¹) = t ^ 2 / 4 * x := by field_simp
    rw [e2, ← e1]
    ring_nf
  have hint' : IntegrableOn (fun v : ℝ => 1 / (2 * Real.sqrt Real.pi) *
      (v ^ (-(5 / 4 : ℝ)) * Real.exp (-(t ^ 2 / (4 * v))))) (Ioi 0) := hint.const_mul _
  have h0 : 0 ≤ᵐ[volume.restrict (Ioi (0 : ℝ))] fun v : ℝ => 1 / (2 * Real.sqrt Real.pi) *
      (v ^ (-(5 / 4 : ℝ)) * Real.exp (-(t ^ 2 / (4 * v)))) :=
    (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall
      (fun v hv => by have := Real.rpow_nonneg (le_of_lt hv) (-(5 / 4 : ℝ)); positivity))
  rw [hEq, ← ofReal_integral_eq_lintegral_ofReal hint' h0, integral_const_mul,
    halfmoment_gamma_identity2 t ht]
  congr 1
  have hc := halfmoment_constant
  have hp : 0 < Real.sqrt Real.pi := Real.sqrt_pos.mpr Real.pi_pos
  calc 1 / (2 * Real.sqrt Real.pi) * ((4 : ℝ) ^ (1 / 4 : ℝ) * Real.Gamma (1 / 4) * |t| ^ (-(1 / 2 : ℝ)))
      = (4 : ℝ) ^ (1 / 4 : ℝ) / (2 * Real.sqrt Real.pi) * Real.Gamma (1 / 4) * |t| ^ (-(1 / 2 : ℝ)) := by
        field_simp
    _ = Real.Gamma (1 / 4) * (1 / Real.sqrt (2 * Real.pi)) * |t| ^ (-(1 / 2 : ℝ)) := by
        rw [hc]; ring

/-- **Lemma 2.3.** For every real random variable `Z` with law `μ` and every `a`,
`E|Z - a|^{-1/2} ≤ (2π)^{-1/2} ∫ |t|^{-1/2} |φ_Z(t)| dt`, both sides in `[0, ∞]`, with `|0|^{-1/2} = ∞` on the left. -/
theorem lemma23 (μ : Measure ℝ) [IsProbabilityMeasure μ] (a : ℝ) :
    ∫⁻ z, (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ)) ∂μ
      ≤ ENNReal.ofReal (1 / Real.sqrt (2 * Real.pi)) *
        ∫⁻ t, ENNReal.ofReal (|t| ^ (-(1 / 2 : ℝ)) * ‖chf μ t‖) := by
  have hG : 0 < Real.Gamma (1 / 4) := Real.Gamma_pos_of_pos (by norm_num)
  have hchf : Measurable (chf μ) := (chf_continuous μ).measurable
  have hFm : Measurable (Function.uncurry fun (z v : ℝ) =>
      ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v)))) := by fun_prop
  have hFz : Measurable (fun z : ℝ => ∫⁻ v in Ioi (0 : ℝ),
      ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v)))) := hFm.lintegral_prod_right'
  have hHm : Measurable (Function.uncurry fun (v t : ℝ) =>
      ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) *
        ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2))) *
      ENNReal.ofReal ‖chf μ t‖) := by fun_prop
  have hae : ∀ᵐ t ∂(volume : Measure ℝ), t ≠ 0 := by
    rw [ae_iff]; simp
  calc ∫⁻ z, (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ)) ∂μ
      ≤ ∫⁻ z, ENNReal.ofReal (1 / Real.Gamma (1 / 4)) *
          (∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v)))) ∂μ :=
        lintegral_mono (fun z => halfmoment_rep a z)
    _ = ENNReal.ofReal (1 / Real.Gamma (1 / 4)) *
          ∫⁻ z, (∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v)))) ∂μ :=
        lintegral_const_mul _ hFz
    _ = ENNReal.ofReal (1 / Real.Gamma (1 / 4)) *
          ∫⁻ v in Ioi (0 : ℝ), (∫⁻ z, ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) * Real.exp (-((z - a) ^ 2 * v))) ∂μ) := by
        rw [lintegral_lintegral_swap hFm.aemeasurable]
    _ ≤ ENNReal.ofReal (1 / Real.Gamma (1 / 4)) *
          ∫⁻ v in Ioi (0 : ℝ), ∫⁻ t, ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) *
            ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2))) *
            ENNReal.ofReal ‖chf μ t‖ := by
        exact mul_le_mul_left' (setLIntegral_mono' measurableSet_Ioi (fun v hv => inner_z_bound μ a v hv)) _
    _ = ENNReal.ofReal (1 / Real.Gamma (1 / 4)) *
          ∫⁻ t, ∫⁻ v in Ioi (0 : ℝ), ENNReal.ofReal (v ^ (-(3 / 4 : ℝ)) *
            ((1 / (2 * Real.sqrt (Real.pi * v))) * Real.exp (-(1 / (4 * v)) * t ^ 2))) *
            ENNReal.ofReal ‖chf μ t‖ := by
        rw [lintegral_lintegral_swap hHm.aemeasurable]
    _ = ENNReal.ofReal (1 / Real.Gamma (1 / 4)) *
          ∫⁻ t, ENNReal.ofReal (Real.Gamma (1 / 4) * (1 / Real.sqrt (2 * Real.pi)) * |t| ^ (-(1 / 2 : ℝ))) *
            ENNReal.ofReal ‖chf μ t‖ := by
        congr 1
        refine lintegral_congr_ae (hae.mono (fun t ht => ?_))
        dsimp only
        rw [lintegral_mul_const _ (by fun_prop), halfmoment_kernel t ht]
    _ = ENNReal.ofReal (1 / Real.sqrt (2 * Real.pi)) *
          ∫⁻ t, ENNReal.ofReal (|t| ^ (-(1 / 2 : ℝ)) * ‖chf μ t‖) := by
        have hsq : 0 < Real.sqrt (2 * Real.pi) := Real.sqrt_pos.mpr (by positivity)
        have e : ∀ t : ℝ, ENNReal.ofReal (Real.Gamma (1 / 4) * (1 / Real.sqrt (2 * Real.pi)) * |t| ^ (-(1 / 2 : ℝ))) *
              ENNReal.ofReal ‖chf μ t‖
            = ENNReal.ofReal (Real.Gamma (1 / 4)) * (ENNReal.ofReal (1 / Real.sqrt (2 * Real.pi)) *
                ENNReal.ofReal (|t| ^ (-(1 / 2 : ℝ)) * ‖chf μ t‖)) := by
          intro t
          have h1 : 0 ≤ Real.Gamma (1 / 4) * (1 / Real.sqrt (2 * Real.pi)) * |t| ^ (-(1 / 2 : ℝ)) := by
            have := Real.rpow_nonneg (abs_nonneg t) (-(1 / 2 : ℝ)); positivity
          have h2 : 0 ≤ 1 / Real.sqrt (2 * Real.pi) := by positivity
          rw [ofReal_mul_ofReal h1, ofReal_mul_ofReal h2, ofReal_mul_ofReal hG.le]
          congr 1
          ring
        simp_rw [e]
        rw [lintegral_const_mul _ (by fun_prop), lintegral_const_mul _ (by fun_prop), ← mul_assoc,
          ofReal_mul_ofReal (by positivity), one_div_mul_cancel hG.ne', ENNReal.ofReal_one, one_mul]

end HalfMomentPart


end Half

end QformFiveB
