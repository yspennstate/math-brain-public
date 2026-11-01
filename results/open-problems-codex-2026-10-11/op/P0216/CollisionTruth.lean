import Lean.Elab.Tactic.Decide

/- Both directed comparisons agree exactly when reversal of the last two
   orders makes the four orientations balanced. A finite 16-case kernel
   computation; this is not the modular-decomposition or limit theorem. -/
theorem collision_balance_truth_table : ∀ a b c d : Bool,
    (((a && b) = (c && d)) ∧ (((!a) && (!b)) = ((!c) && (!d)))) ↔
    ((if a then 1 else 0) + (if b then 1 else 0) +
      (if !c then 1 else 0) + (if !d then 1 else 0) = (2 : Nat)) := by
  decide +kernel
