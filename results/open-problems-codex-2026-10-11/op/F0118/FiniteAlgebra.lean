import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.SplitIfs
import Lean.Elab.Tactic.Omega

open scoped BigOperators

namespace F0118

def integerSign (z : ℤ) : ℤ := if z < 0 then -1 else if z = 0 then 0 else 1

-- The exact discrete second difference used in the star-TV derivative proof.
theorem sign_second_difference (z : ℤ) :
    integerSign (z + 1) + integerSign (z - 1) - 2 * integerSign z =
      (if z = -1 then 1 else if z = 1 then -1 else 0) := by
  unfold integerSign
  split_ifs <;> omega

theorem idempotent_real (x : ℝ) (h : x * x = x) : x = 0 ∨ x = 1 := by
  have hprod : x * (x - 1) = 0 := by
    calc
      x * (x - 1) = x * x - x := by ring
      _ = 0 := by rw [h]; ring
  rcases mul_eq_zero.mp hprod with hz | ho
  · exact Or.inl hz
  · exact Or.inr (sub_eq_zero.mp ho)

theorem mixed_ratio_identity (l c q : ℝ) :
    (l^2 * (l + 2*c)) * (c^2 * (3*l + q*c)) -
      (l^2 * c) * (c * (l^2 + 3*l*c + q*c^2)) =
      l^2 * c^2 * (2*l^2 + (q+3)*l*c + q*c^2) := by
  ring

theorem depth_two_derivative_numerator_pos (a t : ℝ)
    (ha : 0 < a) (ht : 0 ≤ t) :
    0 < 2*a^2 * ((a^3+6*a^2+18*a+6)*t^2 +
      (4*a^3+22*a^2+2*a)*t + 4*a^3+20*a^2+22*a+6) := by
  positivity

-- Once cross terms vanish, any stochastic row is deterministic.
theorem row_entry_zero_or_one {α : Type*} [Fintype α] [DecidableEq α]
    (a : α → ℝ) (hsum : ∑ j, a j = 1)
    (hcross : ∀ i j, i ≠ j → a i * a j = 0) (i : α) :
    a i = 0 ∨ a i = 1 := by
  apply idempotent_real
  calc
    a i * a i = ∑ j, a i * a j := by
      symm
      apply Finset.sum_eq_single i
      · intro j _ hji
        exact hcross i j (Ne.symm hji)
      · intro hi
        exact False.elim (hi (Finset.mem_univ i))
    _ = a i * (∑ j, a j) := by rw [Finset.mul_sum]
    _ = a i := by rw [hsum, mul_one]

end F0118
