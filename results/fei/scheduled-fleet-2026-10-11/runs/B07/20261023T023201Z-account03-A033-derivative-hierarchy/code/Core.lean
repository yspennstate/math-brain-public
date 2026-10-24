import Std.Tactic

-- Intended arithmetic guard only. No compilation claimed: memory admission held.
theorem A033SecondResetPowerGuard :
    (448 : Nat)^40 * 7^15 > 2^8 * 361^40 * 8^15 := by
  decide

#print axioms A033SecondResetPowerGuard
