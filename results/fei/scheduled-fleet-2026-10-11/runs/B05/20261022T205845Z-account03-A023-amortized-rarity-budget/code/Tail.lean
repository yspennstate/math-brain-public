import Std.Tactic

theorem A023TailNumerator (k : Nat) : 4 < 4^(k+2) := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [Nat.succ_add, Nat.pow_succ]
    omega

#print axioms A023TailNumerator
