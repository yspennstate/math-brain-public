import Mathlib.Data.Nat.Basic

/- Cross multiplication for 3/4 < (33/38)^2 in the corrected
   three-site lattice contact calculation. -/
theorem corrected_reflection_comparison_cross_products :
    (3 : Nat) * 1444 < 1089 * 4 := by
  decide +kernel
