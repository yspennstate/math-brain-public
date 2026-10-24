import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith

open Finset

-- The configuration set is finite here. The countable version in ATTEMPT.md
-- follows by increasing finite subsets and monotone convergence.
theorem partition_comparison {α : Type*} (s : Finset α)
    (H K : α → ℝ) (D : ℝ)
    (h : ∀ x ∈ s, |H x - K x| ≤ D) :
    (∑ x ∈ s, Real.exp (-H x)) ≤
      Real.exp D * (∑ x ∈ s, Real.exp (-K x)) := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro x hx
  have hlow := (abs_le.mp (h x hx)).1
  calc
    Real.exp (-H x) ≤ Real.exp (D + -K x) := by
      apply Real.exp_le_exp.mpr
      linarith
    _ = Real.exp D * Real.exp (-K x) := Real.exp_add D (-K x)

theorem reverse_partition_comparison {α : Type*} (s : Finset α)
    (H K : α → ℝ) (D : ℝ)
    (h : ∀ x ∈ s, |H x - K x| ≤ D) :
    (∑ x ∈ s, Real.exp (-K x)) ≤
      Real.exp D * (∑ x ∈ s, Real.exp (-H x)) := by
  apply partition_comparison s K H D
  intro x hx
  rw [abs_sub_comm]
  exact h x hx

#print axioms partition_comparison
#print axioms reverse_partition_comparison
