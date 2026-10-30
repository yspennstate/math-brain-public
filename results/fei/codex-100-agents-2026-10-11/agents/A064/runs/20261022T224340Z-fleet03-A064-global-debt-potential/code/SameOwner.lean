import Std.Tactic.Omega
theorem same_owner_residual (s w x : Int)
    (old_booking : 4*w <= s) (new_booking : 1472*x < s) :
    1103*s < 1472*(s-w-x) := by
  omega
