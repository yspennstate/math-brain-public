import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- The scalar interpolation step only; no queueing or probabilistic assertion.
theorem grid_bridge (left mid right eps budget : ℝ)
    (hl : -eps ≤ left) (hr : right ≤ eps)
    (forward_left : left - budget ≤ mid)
    (forward_right : mid - budget ≤ right) :
    -eps - budget ≤ mid ∧ mid ≤ eps + budget := by
  constructor <;> linarith

theorem bridge_with_arrival_budget (left mid right eps ell h a cap : ℝ)
    (hh : 0 ≤ h) (ha : a ≤ cap)
    (hl : -eps ≤ left) (hr : right ≤ eps)
    (forward_left : left - ell - h * a ≤ mid)
    (forward_right : mid - ell - h * a ≤ right) :
    -eps - ell - h * cap ≤ mid ∧ mid ≤ eps + ell + h * cap := by
  have hm : h * a ≤ h * cap := mul_le_mul_of_nonneg_left ha hh
  constructor <;> linarith
