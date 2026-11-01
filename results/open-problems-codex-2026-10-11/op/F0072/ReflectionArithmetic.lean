import Mathlib.Data.Nat.Basic

/- Cross multiplication for the rational reflection comparison:
   11/24 < (11/16)^2. This is not a counterexample to F0072,
   only to one proposed auxiliary inequality. -/
theorem reflection_comparison_cross_products :
    (11 : Nat) * 256 < 121 * 24 := by
  decide +kernel
