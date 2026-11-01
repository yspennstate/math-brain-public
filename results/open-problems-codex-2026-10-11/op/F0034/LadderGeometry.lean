import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/- On a connector's open time interval, it lies strictly between adjacent rails.
   This certifies affine geometry only, not Brownian-net probability statements. -/
theorem ladder_connector_between (h t : ℝ)
    (hlo : h / 3 < t) (hhi : t < 2 * h / 3) :
    7 * h / 9 - 2 * t / 3 < 7 * h / 3 - 3 * t ∧
    7 * h / 3 - 3 * t < 14 * h / 9 - 2 * t / 3 := by
  constructor <;> linarith

theorem ladder_connector_endpoints (h : ℝ) :
    7 * h / 3 - 3 * (h / 3) = 14 * h / 9 - 2 * (h / 3) / 3 ∧
    7 * h / 3 - 3 * (2 * h / 3) = 7 * h / 9 - 2 * (2 * h / 3) / 3 := by
  constructor <;> linarith
