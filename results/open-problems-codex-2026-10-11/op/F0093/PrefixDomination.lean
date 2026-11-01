import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

open scoped BigOperators

-- Positive finite kernels preserve a pointwise domination bound.
-- This is the finite algebra used for the KL averaging bound in Lemma A2.
theorem finite_kernel_domination {ι : Type*} (s : Finset ι)
    (a p b : ι → ℝ) (M : ℝ)
    (ha : ∀ i ∈ s, a i ≤ M * p i)
    (hb : ∀ i ∈ s, 0 ≤ b i) :
    (∑ i ∈ s, a i * b i) ≤ M * (∑ i ∈ s, p i * b i) := by
  classical
  calc
    (∑ i ∈ s, a i * b i) ≤ (∑ i ∈ s, (M * p i) * b i) := by
      exact Finset.sum_le_sum (fun i hi =>
        mul_le_mul_of_nonneg_right (ha i hi) (hb i hi))
    _ = M * (∑ i ∈ s, p i * b i) := by
      simp only [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i hi
      ring
