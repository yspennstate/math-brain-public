import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Algebraic core of the deterministic-centering argument.
-- The probabilistic concentration theorem is proved on paper, not formalized here.
theorem separated_centers_disjoint (a s l e : ℝ)
    (hgap : e ≤ |a - l|)
    (hsa : |s - a| < e / 3)
    (hsl : |s - l| < e / 3)
    (he : 0 < e) : False := by
  have ht := abs_sub_le a s l
  rw [abs_sub_comm a s] at ht
  linarith

theorem center_bound (a s l e : ℝ)
    (hsa : |s - a| ≤ e / 2)
    (hsl : |s - l| ≤ e / 2) : |a - l| ≤ e := by
  have ht := abs_sub_le a s l
  rw [abs_sub_comm a s] at ht
  linarith
