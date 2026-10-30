import Std.Tactic.Omega
theorem A017_critical_counts (R A D : Nat) (hR : R = A + 12) (hE : R + A + 2*D <= 12) : R = 12 ? A = 0 ? D = 0 := by omega
