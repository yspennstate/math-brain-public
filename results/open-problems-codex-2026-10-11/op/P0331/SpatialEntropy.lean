import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith

open scoped BigOperators

-- Finite algebraic core of spatial entropy localization and Pinsker averaging.
theorem sum_pinsker_budget
    (m : ℕ) (t D : Fin m → ℝ) (B h : ℝ)
    (hpinsker : ∀ j, 2 * (t j)^2 ≤ D j)
    (hbudget : (∑ j, D j) ≤ B + h) :
    2 * (∑ j, (t j)^2) ≤ B + h := by
  calc
    2 * (∑ j, (t j)^2) = ∑ j, 2 * (t j)^2 := by
      rw [Finset.mul_sum]
    _ ≤ ∑ j, D j := Finset.sum_le_sum (fun j _ => hpinsker j)
    _ ≤ B + h := hbudget

-- The self-shell term and the periodic background correction both matter.
theorem periodic_smearing_stability
    (A A' I J K N F S : ℝ)
    (hN : 0 ≤ N)
    (hpair : A' ≤ A + 2 * K * N)
    (hself : I ≤ J)
    (hF : F = A / 2)
    (hS : S = (A' + N * I) / 2)
    (hpos : 0 ≤ S) :
    -(J / 2 + K) * N ≤ F := by
  nlinarith

-- Exact division by the number of cells; h is the canonical count correction.
theorem cell_entropy_budget
    (m beta C N h Dloc Dglob : ℝ)
    (hm : 0 < m)
    (hsub : m * Dloc ≤ Dglob)
    (hbudget : Dglob ≤ C * beta * N + h) :
    Dloc ≤ (C * beta * N + h) / m := by
  apply (le_div_iff₀ hm).2
  nlinarith
