import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic.Linarith

open MeasureTheory

/-- The terminal expectation obstruction. This does not formalize Vitali's theorem. -/
theorem nonnegative_zero_mean_is_zero
    {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) (Z : Ω → ℝ)
    (hi : Integrable Z μ) (hn : ∀ᵐ ω ∂μ, 0 ≤ Z ω)
    (hz : (∫ ω, Z ω ∂μ) = 0) : Z =ᵐ[μ] 0 := by
  exact (integral_eq_zero_iff_of_nonneg_ae hn hi).mp hz

/-- The coefficient obtained by inverting a linear time asymptotic. -/
theorem inverse_log_coefficient (a b c : ℝ) (ha : a ≠ 0) (hc : c = 1 / a) :
    b / a = b * c := by
  rw [hc, div_eq_mul_inv, one_div]

/-- A negative candidate speed cannot equal a nonnegative limiting speed. -/
theorem negative_speed_obstruction (s c : ℝ) (hs : 0 ≤ s) (hc : c < 0) : s ≠ c := by
  intro h
  rw [h] at hs
  linarith
