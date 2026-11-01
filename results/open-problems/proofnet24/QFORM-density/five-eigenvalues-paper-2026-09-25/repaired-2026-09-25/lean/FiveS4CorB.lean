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
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Corollary 4.4(b) of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), from the bound of Theorem 4.1: if `|φ_Q(t)|² ≤ (√2 π e)² ω(2)^{1/2} E₂^{-1/2} |t|^{-2}` for all
`t ≠ 0` (`ℓ = 2`, `ω(2) = 2`), then `sup_a E|Q - a|^{-1/2} ≤ C₂ E₂^{-1/8}` with `C₂ = 8 e^{1/2} 2^{-1/8} < 12.2`
(`cor44b`), through Lemma 2.3 with `u = β₂ E₂^{-1/4}` and the envelope integral `∫ |t|^{-1/2} min{1, u/|t|} dt = 8√u`,
as in the paper.

Lemma 2.3, the envelope integral and the constants of Corollary 4.4 are repeated from `FiveS2Halfmoment.lean`,
`FiveS2Envelope.lean` and `FiveS4Cor.lean`, so that this file compiles on its own.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

namespace CorB

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

section EnvelopeHalf

open Real

/-- **Lemma 2.3, the envelope integral.** `∫_ℝ |t|^{-1/2} min{1, u/|t|} dt = 8√u`. -/
theorem halfmoment_envelope_integral (u : ℝ) (hu : 0 < u) :
    ∫ t : ℝ, |t| ^ (-(1 / 2 : ℝ)) * min 1 (u / |t|) = 8 * √u := by
  have hsym := integral_comp_abs (f := fun s : ℝ => s ^ (-(1 / 2 : ℝ)) * min 1 (u / s))
  simp only at hsym
  rw [hsym]
  have hg1 : ∀ x ∈ Ioc (0 : ℝ) u, x ^ (-(1 / 2 : ℝ)) * min 1 (u / x) = x ^ (-(1 / 2 : ℝ)) := by
    intro x hx
    have h1 : 1 ≤ u / x := by rw [le_div_iff₀ hx.1]; linarith [hx.2]
    rw [min_eq_left h1, mul_one]
  have hg2 : ∀ x ∈ Ioi u, x ^ (-(1 / 2 : ℝ)) * min 1 (u / x) = u * x ^ (-(3 / 2 : ℝ)) := by
    intro x hx
    have hx0 : 0 < x := lt_trans hu hx
    have h1 : u / x ≤ 1 := by rw [div_le_one hx0]; exact le_of_lt hx
    rw [min_eq_right h1]
    have e : x ^ (-(3 / 2 : ℝ)) = x ^ (-(1 / 2 : ℝ)) * x⁻¹ := by
      rw [show (-(3 / 2 : ℝ)) = -(1 / 2) + -1 by norm_num, rpow_add hx0, rpow_neg_one]
    rw [e]
    field_simp
  have hint1 : IntegrableOn (fun x : ℝ => x ^ (-(1 / 2 : ℝ)) * min 1 (u / x)) (Ioc 0 u) := by
    have h := (intervalIntegrable_iff_integrableOn_Ioc_of_le hu.le).mp
      (intervalIntegral.intervalIntegrable_rpow' (a := 0) (b := u) (by norm_num : (-1 : ℝ) < -(1 / 2)))
    exact IntegrableOn.congr_fun h (fun x hx => (hg1 x hx).symm) measurableSet_Ioc
  have hint2 : IntegrableOn (fun x : ℝ => x ^ (-(1 / 2 : ℝ)) * min 1 (u / x)) (Ioi u) :=
    IntegrableOn.congr_fun (Integrable.const_mul
      (integrableOn_Ioi_rpow_of_lt (by norm_num : -(3 / 2 : ℝ) < -1) hu) u)
      (fun x hx => (hg2 x hx).symm) measurableSet_Ioi
  rw [← Ioc_union_Ioi_eq_Ioi hu.le, setIntegral_union Ioc_disjoint_Ioi_same measurableSet_Ioi hint1 hint2,
    setIntegral_congr_fun measurableSet_Ioc hg1, setIntegral_congr_fun measurableSet_Ioi hg2,
    ← intervalIntegral.integral_of_le hu.le,
    integral_rpow (Or.inl (by norm_num : (-1 : ℝ) < -(1 / 2))), integral_const_mul,
    integral_Ioi_rpow_of_lt (by norm_num : -(3 / 2 : ℝ) < -1) hu,
    zero_rpow (by norm_num : (-(1 / 2 : ℝ) + 1) ≠ 0)]
  have h1 : u ^ (-(1 / 2 : ℝ) + 1) = √u := by
    rw [show (-(1 / 2 : ℝ) + 1) = 1 / 2 by norm_num, sqrt_eq_rpow]
  have h2 : u * u ^ (-(3 / 2 : ℝ) + 1) = √u := by
    rw [show (-(3 / 2 : ℝ) + 1) = -(1 / 2) by norm_num, rpow_neg hu.le, ← sqrt_eq_rpow]
    have hs : 0 < √u := sqrt_pos.mpr hu
    field_simp
    rw [sq_sqrt hu.le]
  have e : u * (-u ^ (-(3 / 2 : ℝ) + 1) / (-(3 / 2 : ℝ) + 1)) = 2 * (u * u ^ (-(3 / 2 : ℝ) + 1)) := by
    ring
  rw [e, h1, h2]
  ring

end EnvelopeHalf

section Constants

open Real

/-- `C_3 = 3√2 e (9/2)^{1/6}`. -/
noncomputable def C3 : ℝ := 3 * √2 * exp 1 * (9 / 2 : ℝ) ^ (1 / 6 : ℝ)

/-- `C_2 = 8 e^{1/2} 2^{-1/8}`. -/
noncomputable def C2 : ℝ := 8 * exp (1 / 2) * (2 : ℝ) ^ (-(1 / 8 : ℝ))

/-- `β_3 = ((√2 π e)^3 ω(3)^{1/2})^{1/2}` with `ω(3) = 27/3! = 9/2`. -/
noncomputable def beta3 : ℝ := √((√2 * π * exp 1) ^ 3 * √(9 / 2))

/-- `β_2 = ((√2 π e)^2 ω(2)^{1/2})^{1/2}` with `ω(2) = 4/2! = 2`. -/
noncomputable def beta2 : ℝ := √((√2 * π * exp 1) ^ 2 * √2)

theorem omega_three_two : (3 : ℝ) ^ 3 / (Nat.factorial 3 : ℝ) = 9 / 2 ∧ (2 : ℝ) ^ 2 / (Nat.factorial 2 : ℝ) = 2 := by
  constructor <;> norm_num [Nat.factorial]

theorem sqrt2_pow_six : √2 ^ 6 = 8 := by
  have h : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  calc √2 ^ 6 = (√2 ^ 2) ^ 3 := by ring
    _ = 8 := by rw [h]; norm_num

theorem C3_pow_six : C3 ^ 6 = 26244 * exp 1 ^ 6 := by
  unfold C3
  have h1 : ((9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6 = 9 / 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  calc (3 * √2 * exp 1 * (9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6
      = 3 ^ 6 * √2 ^ 6 * exp 1 ^ 6 * ((9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6 := by ring
    _ = 26244 * exp 1 ^ 6 := by rw [sqrt2_pow_six, h1]; ring

theorem C2_pow_eight : C2 ^ 8 = 8388608 * exp 1 ^ 4 := by
  unfold C2
  have h1 : ((2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8 = 1 / 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]
    rw [show (-(1 / 8 : ℝ)) * ((8 : ℕ) : ℝ) = -1 by norm_num, Real.rpow_neg_one]; norm_num
  have h2 : exp (1 / 2) ^ 8 = exp 1 ^ 4 := by
    rw [← Real.exp_nat_mul, ← Real.exp_nat_mul]; norm_num
  calc (8 * exp (1 / 2) * (2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8
      = 8 ^ 8 * exp (1 / 2) ^ 8 * ((2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8 := by ring
    _ = 8388608 * exp 1 ^ 4 := by rw [h1, h2]; ring

theorem C3_pos : 0 < C3 := by unfold C3; positivity

theorem C2_pos : 0 < C2 := by unfold C2; positivity

/-- `e < 11/4`. -/
theorem exp_one_lt_eleven_quarters : exp 1 < 11 / 4 := by
  have := exp_one_lt_d9; norm_num at this ⊢; linarith

/-- **Corollary 4.4(a), the constant.** `C_3 < 15`, from `26244 (11/4)^6 < 15^6`. -/
theorem C3_lt_15 : C3 < 15 := by
  apply lt_of_pow_lt_pow_left₀ 6 (by norm_num : (0 : ℝ) ≤ 15)
  rw [C3_pow_six]
  have he := exp_one_lt_eleven_quarters
  have hep : 0 < exp 1 := exp_pos 1
  have h6 : exp 1 ^ 6 < (11 / 4) ^ 6 := by gcongr
  calc 26244 * exp 1 ^ 6 < 26244 * (11 / 4) ^ 6 := by linarith
    _ < 15 ^ 6 := by norm_num

/-- **Corollary 4.4(b), the constant.** `C_2 < 12.2`, from `8388608 (11/4)^4 < (61/5)^8`. -/
theorem C2_lt : C2 < 61 / 5 := by
  apply lt_of_pow_lt_pow_left₀ 8 (by norm_num : (0 : ℝ) ≤ 61 / 5)
  rw [C2_pow_eight]
  have he := exp_one_lt_eleven_quarters
  have hep : 0 < exp 1 := exp_pos 1
  have h4 : exp 1 ^ 4 < (11 / 4) ^ 4 := by gcongr
  calc 8388608 * exp 1 ^ 4 < 8388608 * (11 / 4) ^ 4 := by linarith
    _ < (61 / 5) ^ 8 := by norm_num

/-- **Corollary 4.4(a), the identity.** `3 β_3^{2/3}/π = C_3`: both are positive and have sixth power `26244 e^6`. -/
theorem cor44_a_identity : 3 * beta3 ^ (2 / 3 : ℝ) / π = C3 := by
  have hpi : 0 < π := pi_pos
  have hb0 : 0 ≤ beta3 := Real.sqrt_nonneg _
  have hX : 0 ≤ (√2 * π * exp 1) ^ 3 * √(9 / 2) := by positivity
  have hb2 : beta3 ^ 2 = (√2 * π * exp 1) ^ 3 * √(9 / 2) := Real.sq_sqrt hX
  have hs : √(9 / 2 : ℝ) ^ 2 = 9 / 2 := Real.sq_sqrt (by norm_num)
  have hpow : (beta3 ^ (2 / 3 : ℝ)) ^ 6 = (beta3 ^ 2) ^ 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hb0]
    rw [show (2 / 3 : ℝ) * ((6 : ℕ) : ℝ) = ((4 : ℕ) : ℝ) by norm_num, Real.rpow_natCast]
    ring
  have hL : (3 * beta3 ^ (2 / 3 : ℝ) / π) ^ 6 = 26244 * exp 1 ^ 6 := by
    have e : (3 * beta3 ^ (2 / 3 : ℝ) / π) ^ 6 = 3 ^ 6 * (beta3 ^ (2 / 3 : ℝ)) ^ 6 / π ^ 6 := by ring
    rw [e, hpow, hb2]
    have e2 : ((√2 * π * exp 1) ^ 3 * √(9 / 2)) ^ 2 = √2 ^ 6 * π ^ 6 * exp 1 ^ 6 * √(9 / 2 : ℝ) ^ 2 := by ring
    rw [e2, sqrt2_pow_six, hs]
    field_simp
    ring
  have hLpos : 0 ≤ 3 * beta3 ^ (2 / 3 : ℝ) / π := by positivity
  have := C3_pos
  rw [← C3_pow_six] at hL
  exact (pow_left_inj₀ hLpos this.le (by norm_num : (6 : ℕ) ≠ 0)).mp hL

/-- **Corollary 4.4(b)**, `β_2 = 2^{3/4} π e`: both sides are positive with fourth power `8 π^4 e^4`. -/
theorem cor44_b_beta2 : beta2 = (2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1 := by
  have hpi : 0 < π := pi_pos
  have hX : 0 ≤ (√2 * π * exp 1) ^ 2 * √2 := by positivity
  have hb2 : beta2 ^ 2 = (√2 * π * exp 1) ^ 2 * √2 := Real.sq_sqrt hX
  have hs2 : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have h34 : ((2 : ℝ) ^ (3 / 4 : ℝ)) ^ 4 = 8 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  have hL : beta2 ^ 4 = 8 * π ^ 4 * exp 1 ^ 4 := by
    have e : beta2 ^ 4 = (beta2 ^ 2) ^ 2 := by ring
    rw [e, hb2]
    have e2 : ((√2 * π * exp 1) ^ 2 * √2) ^ 2 = (√2 ^ 2) ^ 3 * π ^ 4 * exp 1 ^ 4 := by ring
    rw [e2, hs2]; norm_num
  have hR : ((2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1) ^ 4 = 8 * π ^ 4 * exp 1 ^ 4 := by
    have e : ((2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1) ^ 4 = ((2 : ℝ) ^ (3 / 4 : ℝ)) ^ 4 * π ^ 4 * exp 1 ^ 4 := by ring
    rw [e, h34]
  rw [← hR] at hL
  exact (pow_left_inj₀ (Real.sqrt_nonneg _) (by positivity) (by norm_num : (4 : ℕ) ≠ 0)).mp hL

/-- **Corollary 4.4(b), the identity.** `8 (β_2/(2π))^{1/2} = C_2`: both are positive with square `64 e 2^{-1/4}`. -/
theorem cor44_b_identity : 8 * √(beta2 / (2 * π)) = C2 := by
  have hpi : 0 < π := pi_pos
  have hq : beta2 / (2 * π) = (2 : ℝ) ^ (-(1 / 4 : ℝ)) * exp 1 := by
    rw [cor44_b_beta2]
    have e : (2 : ℝ) ^ (3 / 4 : ℝ) = 2 * (2 : ℝ) ^ (-(1 / 4 : ℝ)) := by
      rw [show (3 / 4 : ℝ) = 1 + (-(1 / 4)) by norm_num, Real.rpow_add (by norm_num), Real.rpow_one]
    rw [e]; field_simp
  rw [hq]
  unfold C2
  have h1 : √((2 : ℝ) ^ (-(1 / 4 : ℝ)) * exp 1) = (2 : ℝ) ^ (-(1 / 8 : ℝ)) * exp (1 / 2) := by
    rw [Real.sqrt_mul (by positivity), Real.sqrt_eq_rpow, Real.sqrt_eq_rpow, ← Real.rpow_mul (by norm_num),
      ← Real.exp_one_rpow, ← Real.rpow_mul (exp_pos 1).le, Real.exp_one_rpow]
    norm_num
  rw [h1]; ring

end Constants

/-! ### Corollary 4.4 (b) from Theorem 4.1 -/

section Corollary

open Real

/-- **Corollary 4.4(b).** If Theorem 4.1 holds with `ℓ = 2`, that is
`|φ_Q(t)|² ≤ (√2 π e)² ω(2)^{1/2} E₂^{-1/2} |t|^{-2}` for `t ≠ 0` with `ω(2) = 4/2! = 2`, then for every `a`,
`E|Q - a|^{-1/2} ≤ C₂ E₂^{-1/8}` with `C₂ = 8 e^{1/2} 2^{-1/8} < 12.2`: `|φ_Q| ≤ min{1, u/|t|}` with `u = β₂ E₂^{-1/4}`,
and Lemma 2.3 gives `8 √(u/(2π))`. -/
theorem cor44b (μ : Measure ℝ) [IsProbabilityMeasure μ] (E2 : ℝ) (hE : 0 < E2)
    (hdecay : ∀ t : ℝ, t ≠ 0 → ‖chf μ t‖ ^ 2
      ≤ (√2 * π * exp 1) ^ 2 * √2 * E2 ^ (-(1 / 2 : ℝ)) * |t| ^ (-(2 : ℝ)))
    (a : ℝ) :
    ∫⁻ z, (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ)) ∂μ ≤ ENNReal.ofReal (C2 * E2 ^ (-(1 / 8 : ℝ))) := by
  have hb0 : 0 < beta2 := Real.sqrt_pos.2 (by positivity)
  have hb2 : beta2 ^ 2 = (√2 * π * exp 1) ^ 2 * √2 := Real.sq_sqrt (by positivity)
  have hu : 0 < beta2 * E2 ^ (-(1 / 4 : ℝ)) := by positivity
  -- the envelope
  have henv : ∀ t : ℝ, t ≠ 0 → ‖chf μ t‖ ≤ min 1 (beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t|) := by
    intro t ht
    have hat : 0 < |t| := abs_pos.2 ht
    have h1 : (E2 ^ (-(1 / 4 : ℝ))) ^ 2 = E2 ^ (-(1 / 2 : ℝ)) := by
      rw [← Real.rpow_natCast, ← Real.rpow_mul hE.le]
      norm_num
    have h2 : |t| ^ (-(2 : ℝ)) = (|t| ^ 2)⁻¹ := by
      rw [Real.rpow_neg hat.le, Real.rpow_two]
    have key : (beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t|) ^ 2
        = (√2 * π * exp 1) ^ 2 * √2 * E2 ^ (-(1 / 2 : ℝ)) * |t| ^ (-(2 : ℝ)) := by
      rw [div_pow, mul_pow, hb2, h1, h2, div_eq_mul_inv]
    have hb : ‖chf μ t‖ ≤ beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t| := by
      calc ‖chf μ t‖ = √(‖chf μ t‖ ^ 2) := (Real.sqrt_sq (norm_nonneg _)).symm
        _ ≤ √((beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t|) ^ 2) :=
            Real.sqrt_le_sqrt (by rw [key]; exact hdecay t ht)
        _ = beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t| := Real.sqrt_sq (by positivity)
    exact le_min (chf_norm_le_one μ t) hb
  -- the envelope integral
  have hval : ∫ t : ℝ, |t| ^ (-(1 / 2 : ℝ)) * min 1 (beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t|)
      = 8 * √(beta2 * E2 ^ (-(1 / 4 : ℝ))) := halfmoment_envelope_integral _ hu
  have hint : Integrable (fun t : ℝ => |t| ^ (-(1 / 2 : ℝ)) * min 1 (beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t|)) := by
    apply Integrable.of_integral_ne_zero
    rw [hval]
    have : 0 < √(beta2 * E2 ^ (-(1 / 4 : ℝ))) := Real.sqrt_pos.2 hu
    positivity
  have hne : ∀ᵐ t ∂(volume : Measure ℝ), t ≠ 0 := by
    rw [ae_iff]
    simp
  have hK : ∫⁻ t, ENNReal.ofReal (|t| ^ (-(1 / 2 : ℝ)) * ‖chf μ t‖)
      ≤ ENNReal.ofReal (8 * √(beta2 * E2 ^ (-(1 / 4 : ℝ)))) := by
    calc ∫⁻ t, ENNReal.ofReal (|t| ^ (-(1 / 2 : ℝ)) * ‖chf μ t‖)
        ≤ ∫⁻ t, ENNReal.ofReal (|t| ^ (-(1 / 2 : ℝ)) * min 1 (beta2 * E2 ^ (-(1 / 4 : ℝ)) / |t|)) := by
          apply lintegral_mono_ae
          filter_upwards [hne] with t ht
          apply ENNReal.ofReal_le_ofReal
          exact mul_le_mul_of_nonneg_left (henv t ht) (Real.rpow_nonneg (abs_nonneg t) _)
      _ = ENNReal.ofReal (8 * √(beta2 * E2 ^ (-(1 / 4 : ℝ)))) := by
          rw [← ofReal_integral_eq_lintegral_ofReal hint
            (Filter.Eventually.of_forall (fun t => by positivity)), hval]
  -- the constant
  have hs2π : 0 < √(2 * π) := Real.sqrt_pos.2 (by positivity)
  have hc : 1 / √(2 * π) * (8 * √(beta2 * E2 ^ (-(1 / 4 : ℝ)))) = C2 * E2 ^ (-(1 / 8 : ℝ)) := by
    have e1 : √(E2 ^ (-(1 / 4 : ℝ))) = E2 ^ (-(1 / 8 : ℝ)) := by
      rw [Real.sqrt_eq_rpow, ← Real.rpow_mul hE.le]
      norm_num
    rw [← cor44_b_identity, Real.sqrt_mul hb0.le, e1, Real.sqrt_div' _ (by positivity : (0 : ℝ) ≤ 2 * π)]
    field_simp <;> ring
  calc ∫⁻ z, (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ)) ∂μ
      ≤ ENNReal.ofReal (1 / √(2 * π)) * ∫⁻ t, ENNReal.ofReal (|t| ^ (-(1 / 2 : ℝ)) * ‖chf μ t‖) := lemma23 μ a
    _ ≤ ENNReal.ofReal (1 / √(2 * π)) * ENNReal.ofReal (8 * √(beta2 * E2 ^ (-(1 / 4 : ℝ)))) := by
        gcongr
    _ = ENNReal.ofReal (C2 * E2 ^ (-(1 / 8 : ℝ))) := by
        rw [← ENNReal.ofReal_mul (by positivity), hc]

end Corollary

end CorB

end QformFiveB
