import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

open scoped BigOperators

theorem c0059_type2_partial_mass (n : ℕ) :
    (∑ k ∈ Finset.range n, (1 : ℚ) / (4 * ((k : ℚ) + 1)^2 - 1)) =
      (n : ℚ) / (2 * (n : ℚ) + 1) := by
  induction n with
  | zero => norm_num
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    push_cast
    have h1 : (2 * (n : ℚ) + 1) ≠ 0 := by positivity
    have h2 : (2 * (n : ℚ) + 3) ≠ 0 := by positivity
    have h3 : 4 * ((n : ℚ) + 1)^2 - 1 ≠ 0 := by
      have h : 4 * ((n : ℚ) + 1)^2 - 1 = (2 * n + 1) * (2 * n + 3) := by ring
      rw [h]
      exact mul_ne_zero h1 h2
    field_simp
    <;> ring
