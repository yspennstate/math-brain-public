import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- The local birth/coalescence detailed-balance identity, for walk rate one.
theorem birth_coalescence_balance (b : ℝ) (h : 1 + b ≠ 0) :
    (b / (1 + b)) * (1 - b / (1 + b)) * b =
      (b / (1 + b)) * (b / (1 + b)) := by
  field_simp
  <;> ring

-- Equal-particle-number moves have equal Bernoulli weights.
theorem jump_weight_balance (p : ℝ) : p * (1 - p) = (1 - p) * p := by
  ring

-- Local flip identity for the constrained Ising process.
theorem constrained_flip_balance (p : ℝ) :
    (1 - p) * p = p * (1 - p) := by
  ring

-- The isolated-pair escape identity after the first-step Green identity.
theorem escape_green_identity (g h : ℝ) (hg : g ≠ 0) (heq : g = 1 + h) :
    1 - h / g = 1 / g := by
  field_simp
  <;> rw [heq]
  <;> ring
