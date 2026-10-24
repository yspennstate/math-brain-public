import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic

/-!
Fourth group of formal checks for "Quadratic forms with nine large eigenvalues have bounded densities":
the integral identities used in Lemmas 2.2, 2.3, 5.5 and Proposition 7.2.
-/

open Real MeasureTheory Set

namespace QformNine

/-- Lemma 2.2: for a > 0 and p > 1, the integral of t^{-p} over (a, infinity) is a^{1-p}/(p-1). -/
theorem envelope_tail (a p : ℝ) (ha : 0 < a) (hp : 1 < p) :
    ∫ t in Ioi a, t ^ (-p) = a ^ (1 - p) / (p - 1) := by
  rw [integral_Ioi_rpow_of_lt (by linarith) ha, show -p + 1 = 1 - p by ring]
  have h1 : (1 - p) ≠ 0 := by linarith
  have h2 : (p - 1) ≠ 0 := by linarith
  field_simp
  ring

/-- Lemma 2.3: the integral of t^{-1/2} over (0, u) is 2 sqrt u. -/
theorem halfmoment_core (u : ℝ) (hu : 0 < u) :
    ∫ t in (0:ℝ)..u, t ^ (-(1/2:ℝ)) = 2 * Real.sqrt u := by
  rw [integral_rpow (Or.inl (by norm_num))]
  rw [show -(1/2:ℝ) + 1 = 1/2 by norm_num, Real.zero_rpow (by norm_num), Real.sqrt_eq_rpow]
  ring

/-- Lemma 2.3: the integral of t^{-3/2} over (u, infinity) is 2 u^{-1/2}. -/
theorem halfmoment_tail (u : ℝ) (hu : 0 < u) :
    ∫ t in Ioi u, t ^ (-(3/2:ℝ)) = 2 * u ^ (-(1/2:ℝ)) := by
  rw [integral_Ioi_rpow_of_lt (by norm_num) hu, show -(3/2:ℝ) + 1 = -(1/2) by norm_num]
  ring

/-- Lemma 2.3: 2 (2 sqrt u) + 2 u (2 u^{-1/2}) = 8 sqrt u, the integral of |t|^{-1/2} min(1, u/|t|). -/
theorem halfmoment_total (u : ℝ) (hu : 0 < u) :
    2 * (2 * Real.sqrt u) + 2 * u * (2 * u ^ (-(1/2:ℝ))) = 8 * Real.sqrt u := by
  have h : u * u ^ (-(1/2:ℝ)) = Real.sqrt u := by
    have hs : 0 < Real.sqrt u := Real.sqrt_pos.mpr hu
    rw [Real.rpow_neg hu.le, ← Real.sqrt_eq_rpow]
    calc u * (Real.sqrt u)⁻¹ = Real.sqrt u * Real.sqrt u * (Real.sqrt u)⁻¹ := by
          rw [Real.mul_self_sqrt hu.le]
      _ = Real.sqrt u := by field_simp
  calc 2 * (2 * Real.sqrt u) + 2 * u * (2 * u ^ (-(1/2:ℝ)))
      = 4 * Real.sqrt u + 4 * (u * u ^ (-(1/2:ℝ))) := by ring
    _ = 8 * Real.sqrt u := by rw [h]; ring

/-- Lemmas 5.5 and 7.2: the integral of x^{-1/2} over (0, 1) is 2, so that of |x|^{-1/2} over (-1, 1) is 4. -/
theorem int_inv_sqrt : ∫ x in (0:ℝ)..1, x ^ (-(1/2:ℝ)) = 2 := by
  rw [integral_rpow (Or.inl (by norm_num))]
  rw [show -(1/2:ℝ) + 1 = 1/2 by norm_num, Real.zero_rpow (by norm_num), Real.one_rpow]
  norm_num

/-- Lemma 2.3: Gamma representation, int_0^infinity v^{1/4 - 1} e^{-z^2 v} dv = |z|^{-1/2} Gamma(1/4) for z != 0. -/
theorem gamma_rep (z : ℝ) (hz : z ≠ 0) :
    ∫ v in Ioi (0:ℝ), v ^ ((1/4:ℝ) - 1) * Real.exp (-(z^2 * v)) = |z| ^ (-(1/2:ℝ)) * Real.Gamma (1/4) := by
  have hz2 : 0 < z^2 := by positivity
  rw [Real.integral_rpow_mul_exp_neg_mul_Ioi (by norm_num) hz2]
  congr 1
  have habs : 0 ≤ |z| := abs_nonneg z
  rw [← sq_abs z, one_div, ← Real.rpow_natCast, ← Real.rpow_neg habs, ← Real.rpow_mul habs]
  norm_num

end QformNine
