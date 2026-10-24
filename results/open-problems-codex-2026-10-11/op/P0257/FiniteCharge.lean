import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- The combinatorial incidence argument supplies hlocal and htotal.
-- This theorem checks the finite summation and endpoint-error step only.
theorem finite_charge_bound {α : Type*} [Fintype α]
    (charge score loss : α → ℝ) (L R : ℝ)
    (hlocal : ∀ v, 2 * score v - loss v ≤ charge v)
    (htotal : (∑ v, charge v) = 2 * L)
    (hloss : (∑ v, loss v) ≤ 2 * R) :
    (∑ v, score v) - R ≤ L := by
  have hs : (∑ v, (2 * score v - loss v)) ≤ ∑ v, charge v :=
    Finset.sum_le_sum (fun v _ => hlocal v)
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum, htotal] at hs
  linarith

-- Used in the resampling variance estimate.
theorem square_sum_bound (x y : ℝ) :
    (x + y)^2 ≤ 2 * x^2 + 2 * y^2 := by
  nlinarith [sq_nonneg (x-y)]
