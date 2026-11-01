import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- Only the scalar gap identity is formalized; no Markov-chain formalization
-- or claim about the complete open problem is made by this file.
theorem w335_gap_identity (n a alpha : ℝ)
    (hn : n - 1 ≠ 0) (ha : 1 + (n - 1) * a ≠ 0) :
    alpha * ((1 - a) / (1 + (n - 1) * a) + 1 / (n - 1)) =
      alpha * n / ((n - 1) * (1 + (n - 1) * a)) := by
  field_simp [hn, ha]
  <;> ring
