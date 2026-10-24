import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open scoped BigOperators

theorem c0059_pair_variance {α : Type*} (s : Finset α) (u : α → ℚ) :
    (∑ i ∈ s, ∑ j ∈ s, (u i - u j)^2) =
      2 * (s.card : ℚ) * (∑ i ∈ s, (u i)^2) -
        2 * (∑ i ∈ s, u i)^2 := by
  simp_rw [sub_sq]
  simp only [Finset.sum_sub_distrib, Finset.sum_add_distrib,
    ← Finset.sum_mul, ← Finset.mul_sum, Finset.sum_const, nsmul_eq_mul]
  ring

theorem c0059_star_mesh_identity {α : Type*} (s : Finset α)
    (u : α → ℚ) (z : ℚ) :
    (s.card : ℚ) * (∑ i ∈ s, (u i - z)^2) =
      (1 / 2 : ℚ) * (∑ i ∈ s, ∑ j ∈ s, (u i - u j)^2) +
        ((∑ i ∈ s, u i) - (s.card : ℚ) * z)^2 := by
  rw [c0059_pair_variance]
  simp_rw [sub_sq]
  simp only [Finset.sum_sub_distrib, Finset.sum_add_distrib,
    ← Finset.sum_mul, ← Finset.mul_sum, Finset.sum_const, nsmul_eq_mul]
  ring
