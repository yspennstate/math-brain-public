import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Exact algebra behind radial rigidity; q is the squared norm of Q(d).
theorem radial_midpoint_rigidity (e q b h : ℝ) (he : 0 < e) (hq : 0 ≤ q)
    (hminus : h - 2 * e * b + e ^ 2 * q ≤ h)
    (hplus : h + 2 * e * b + e ^ 2 * q ≤ h) : q = 0 := by
  have hs : 0 < e ^ 2 := by
    simpa only [pow_two] using mul_pos he he
  nlinarith

#print axioms radial_midpoint_rigidity
