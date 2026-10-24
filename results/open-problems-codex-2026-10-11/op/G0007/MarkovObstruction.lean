import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

-- Algebraic contradiction from singleton, edge, and three-vertex stationarity.
theorem no_tree_markov_stationary_algebra
    (d v : ℝ) (hd : d ≠ 0)
    (hedge : d * v = d - 1)
    (hpath : d * (2 * v + v ^ 2) = 3 * d - 4) : False := by
  have hv : v = (d - 1) / d := by
    apply (eq_div_iff hd).2
    nlinarith [hedge]
  rw [hv] at hpath
  field_simp at hpath
  nlinarith
