import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- The r^2 coefficient forces exactly two possible quadratic sigma coefficients.
theorem quadratic_sector (a b : ℝ) :
    4 * b ^ 2 + 4 * b * a ^ 2 = 0 ↔ b = 0 ∨ b = -a ^ 2 := by
  constructor
  · intro h
    have hm : b * (b + a ^ 2) = 0 := by nlinarith
    rcases mul_eq_zero.mp hm with hb | hb
    · exact Or.inl hb
    · right
      linarith
  · intro h
    rcases h with hb | hb
    · rw [hb]
      ring
    · rw [hb]
      ring

-- Leading first-difference coefficient of the nonlinear formal PV sector.
theorem nonlinear_recurrence_coefficient (a n : ℝ) :
    -4 * a ^ 2 * n * (n - 1) + 4 * a ^ 2 * (n - 1)
      = -4 * a ^ 2 * (n - 1) ^ 2 := by
  ring

-- Sign used in the stopped discounted power estimate.
theorem discounted_power_sign (k c xpower : ℝ)
    (hkc : k ≤ c) (hx : 0 ≤ xpower) : (k - c) * xpower ≤ 0 := by
  exact mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hkc) hx
