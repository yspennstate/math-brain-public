import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Only exponent algebra, not the stochastic theorem.
theorem critical_rho_positive (a rho : ℝ)
    (ha : 0 < a) (halt : a < 1) (hr : 0 ≤ rho)
    (hc : a * (rho + 1) = 1) : 0 < rho := by
  by_contra h
  have hz : rho = 0 := by linarith
  rw [hz] at hc
  linarith

theorem critical_H_exponent (a rho : ℝ)
    (hc : a * (rho + 1) = 1) :
    (1 - a) * (rho + 1) = rho := by
  nlinarith [hc]

theorem absorption (x b c eta k : ℝ)
    (hx : 0 ≤ x) (hc : 0 ≤ c) (hk : 0 ≤ k)
    (hs : c * eta ≤ 1 / 2)
    (he : x ≤ b + c * (eta * x + k)) :
    x ≤ 2 * (b + c * k) := by
  nlinarith [mul_nonneg hx (sub_nonneg.mpr hs)]
