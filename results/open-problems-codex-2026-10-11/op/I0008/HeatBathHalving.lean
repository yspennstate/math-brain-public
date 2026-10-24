import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith

open Finset

-- Finite paired-tail estimate used after rounding integer indices toward zero.
theorem paired_tail_bound (n : ℕ) (W : ℕ → ℝ)
    (he : ∀ j ∈ range n, 2 * W (j + 1) ≤ W (2 * j + 2))
    (ho : ∀ j ∈ range n, 2 * W (j + 1) ≤ W (2 * j + 3)) :
    (∑ j ∈ range n,
      (Real.exp (-W (2 * j + 2) / 2) +
        Real.exp (-W (2 * j + 3) / 2))) ≤
      2 * (∑ j ∈ range n, Real.exp (-W (j + 1))) := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro j hj
  have h1 : Real.exp (-W (2 * j + 2) / 2) ≤
      Real.exp (-W (j + 1)) := by
    apply Real.exp_le_exp.mpr
    linarith [he j hj]
  have h2 : Real.exp (-W (2 * j + 3) / 2) ≤
      Real.exp (-W (j + 1)) := by
    apply Real.exp_le_exp.mpr
    linarith [ho j hj]
  linarith

-- Include 0 and the two indices that round to 0. The rest form paired tails.
theorem two_sided_halving_bound (n : ℕ) (P M : ℕ → ℝ)
    (hp : 0 ≤ P 1) (hm : 0 ≤ M 1)
    (hpe : ∀ j ∈ range n, 2 * P (j + 1) ≤ P (2 * j + 2))
    (hpo : ∀ j ∈ range n, 2 * P (j + 1) ≤ P (2 * j + 3))
    (hme : ∀ j ∈ range n, 2 * M (j + 1) ≤ M (2 * j + 2))
    (hmo : ∀ j ∈ range n, 2 * M (j + 1) ≤ M (2 * j + 3)) :
    1 + Real.exp (-P 1 / 2) + Real.exp (-M 1 / 2) +
      (∑ j ∈ range n,
        (Real.exp (-P (2 * j + 2) / 2) +
          Real.exp (-P (2 * j + 3) / 2))) +
      (∑ j ∈ range n,
        (Real.exp (-M (2 * j + 2) / 2) +
          Real.exp (-M (2 * j + 3) / 2))) ≤
      3 * (1 + (∑ j ∈ range n, Real.exp (-P (j + 1))) +
        (∑ j ∈ range n, Real.exp (-M (j + 1)))) := by
  have h1 : Real.exp (-P 1 / 2) ≤ 1 := by
    apply Real.exp_le_one_iff.mpr
    linarith
  have h2 : Real.exp (-M 1 / 2) ≤ 1 := by
    apply Real.exp_le_one_iff.mpr
    linarith
  have h3 := paired_tail_bound n P hpe hpo
  have h4 := paired_tail_bound n M hme hmo
  have h5 : 0 ≤ ∑ j ∈ range n, Real.exp (-P (j + 1)) :=
    Finset.sum_nonneg fun _ _ => le_of_lt (Real.exp_pos _)
  have h6 : 0 ≤ ∑ j ∈ range n, Real.exp (-M (j + 1)) :=
    Finset.sum_nonneg fun _ _ => le_of_lt (Real.exp_pos _)
  linarith

#print axioms paired_tail_bound
#print axioms two_sided_halving_bound
