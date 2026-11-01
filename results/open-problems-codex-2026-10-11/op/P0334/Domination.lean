import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset

open scoped BigOperators

-- Finite piecewise-constant derivative version of the increasing-envelope step.
-- Ordinary Lean kernel checking only; no sorry, axioms, or native_decide.
theorem weighted_increment_domination {ι : Type*} (s : Finset ι)
    (a b w : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) :
    |∑ i ∈ s, w i * (a i - b i)| ≤ ∑ i ∈ s, w i * |a i - b i| := by
  calc
    |∑ i ∈ s, w i * (a i - b i)|
        ≤ ∑ i ∈ s, |w i * (a i - b i)| := Finset.abs_sum_le_sum_abs _ _
    _ = ∑ i ∈ s, w i * |a i - b i| := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [abs_mul, abs_of_nonneg (hw i hi)]

#print axioms weighted_increment_domination
