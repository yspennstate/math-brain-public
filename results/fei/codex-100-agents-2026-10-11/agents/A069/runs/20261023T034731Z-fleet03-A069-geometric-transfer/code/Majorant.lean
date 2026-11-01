import Std

theorem width_bound (l : Nat) : 4 ≤ l → 4*l ≤ 2^l := by
  induction l with
  | zero =>
    intro h
    omega
  | succ n ih =>
    intro h
    by_cases hn : 4 ≤ n
    · have hpow : 4 ≤ 2^n := Nat.le_trans (by omega : 4 ≤ 4*n) (ih hn)
      calc
        4*(n+1) = 4*n+4 := by omega
        _ ≤ 2^n+2^n := Nat.add_le_add (ih hn) hpow
        _ = 2^(n+1) := by simp [Nat.pow_succ, Nat.mul_two]
    · have he : n=3 := by omega
      subst n
      decide

theorem bank_units : 1600-1541=59 := by decide
