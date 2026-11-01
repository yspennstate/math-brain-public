import Std.Tactic

-- Integer-scaled conservative booking: source surplus451, charges<320,128.
theorem two_reset_bank (s p1 p2 : Int) (hs : 451 < s)
    (h1 : p1 < 320) (h2 : p2 < 128) : 3 < s-p1-p2 := by
  omega

theorem tail_bound (m : Nat) : 16*m+17 <= 17*2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    simp only [Nat.pow_succ]
    omega
