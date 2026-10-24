import Mathlib.MeasureTheory.Integral.Gamma
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.MeasureTheory.Integral.IntegralEqImproper
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
The Gamma-function integrals behind Lemmas 2.3 and 5.4 of "Quadratic forms with five large singular values have
bounded densities" (repaired text, sha256 90f859b7).

* `halfmoment_gamma_identity`: `∫_0^∞ v^{-3/4} e^{-v z²} dv = Γ(1/4) |z|^{-1/2}` for `z ≠ 0` (the representation of
  `|z|^{-1/2}` that opens the proof of Lemma 2.3).
* `halfmoment_gamma_identity2`: `∫_0^∞ v^{-5/4} e^{-t²/(4v)} dv = 4^{1/4} Γ(1/4) |t|^{-1/2}` for `t ≠ 0` (the integral
  after the exchange in Lemma 2.3).
* `halfmoment_constant`: `4^{1/4}/(2√π) = 1/√(2π)`.
* `concentration_gamma_integral`: `∫_ℝ |t|^{-1/2} e^{-w t²} dt = Γ(1/4) w^{-1/4}` for `w > 0` (Lemma 5.4; at
  `w = ρ²/(4v)` it is the factor `Γ(1/4)(4v/ρ²)^{1/4}` of the displayed bound).
-/

open Real MeasureTheory Set

namespace QformFiveB

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

end QformFiveB
