import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

-- Algebraic generator check. This does not formalize the infinite process.
theorem covariance_identity (a b c d k u v : ℝ) :
    (a * (1-b) * c - b*c*(1-d) - k*(u+v)*b*c)
      - c*(a*(1-b)-b*(1-c)-k*u*b)
      - b*(b*(1-c)-c*(1-d)-k*v*c)
      = b*(1-c)*(c-b) := by
  ring

theorem density_from_balance (r k : ℝ) (hr : r ≠ 0)
    (h : r*(1-r) = k*r) : r = 1-k := by
  have h' : r*(1-r) = r*k := by simpa [mul_comm] using h
  have hc : 1-r = k := mul_left_cancel₀ hr h'
  linarith

theorem strictly_positive_density_requires_small_k (r k : ℝ)
    (hr : 0 < r) (hk : 0 < k) (h : r*(1-r) = k*r) :
    k < 1 ∧ r < 1 := by
  have he : r = 1-k := density_from_balance r k (ne_of_gt hr) h
  constructor <;> linarith

theorem telescope_boundary (x y r : ℝ) :
    (x-r) + (y-x) + (r-y) = 0 := by ring

theorem no10_is_ordered (a b : Bool) :
    ((a && !b) = false) → (a = true → b = true) := by
  cases a <;> cases b <;> decide +kernel
