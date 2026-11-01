import Mathlib.Data.Fintype.Card
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.Tactic.Linarith

-- Finite algebraic core of the Perron-flow path product optimization.
-- The graph compression and probabilistic theorem are proved in ATTEMPT.md.
theorem flow_prod_bound {I : Type*} [Fintype I] (t : I -> Real)
    (h0 : forall i, 0 <= t i) (h1 : forall i, t i <= 1) :
    Finset.univ.prod (fun i => t i * (1 - t i)) <=
      (1 / 4 : Real) ^ Fintype.card I := by
  calc
    Finset.univ.prod (fun i => t i * (1 - t i)) <=
        Finset.univ.prod (fun _i : I => (1 / 4 : Real)) := by
      apply Finset.prod_le_prod
      . intro i hi
        exact mul_nonneg (h0 i) (sub_nonneg.mpr (h1 i))
      . intro i hi
        nlinarith [sq_nonneg (t i - 1 / 2)]
    _ = (1 / 4 : Real) ^ Fintype.card I := by simp
