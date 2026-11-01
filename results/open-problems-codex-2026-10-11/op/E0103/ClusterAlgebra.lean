import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

-- Equal-length intervals add either a whole interval or only the gap.
-- This is the finite algebraic step in the marked void union formula.
theorem equal_interval_increment (ell h : ℝ) :
    (if h ≤ ell then ell + h else 2 * ell) = ell + min h ell := by
  by_cases hh : h ≤ ell
  · simp [hh, min_eq_left hh]
  · have he : ell ≤ h := le_of_lt (lt_of_not_ge hh)
    simp [hh, min_eq_right he]
    ring

-- Equivalence of the cluster-mass and stationary-atom formulas for theta.
theorem cluster_index_identity (p q : ℝ) (hp : 0 ≤ p)
    (hp1 : p < 1) (hq : 0 < q) :
    1 / (1 + p * q / (1 - p)) = (1 - p) / (1 - p + p * q) := by
  have hpden : 1 - p ≠ 0 := by linarith
  have hpq : 0 ≤ p * q := mul_nonneg hp (le_of_lt hq)
  have hd : 0 < 1 - p + p * q := by linarith
  have hdne : 1 - p + p * q ≠ 0 := ne_of_gt hd
  have hj : 0 ≤ p * q / (1 - p) := div_nonneg hpq (by linarith)
  have hs : 1 + p * q / (1 - p) ≠ 0 := by linarith
  field_simp [hpden, hdne, hs]
  <;> ring
