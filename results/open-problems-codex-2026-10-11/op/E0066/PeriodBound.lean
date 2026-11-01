import Mathlib.Data.Fintype.Perm

-- Finite algebraic step used in the three-type period bound.
-- Uses the kernel evaluator; no native_decide and no admitted statements.
theorem perm_fin3_order_bound (p : Equiv.Perm (Fin 3)) :
    p ^ 2 = 1 ∨ p ^ 3 = 1 := by
  revert p
  decide +kernel

theorem perm_fin2_order_bound (p : Equiv.Perm (Fin 2)) :
    p ^ 2 = 1 := by
  revert p
  decide +kernel

#print axioms perm_fin3_order_bound
#print axioms perm_fin2_order_bound
