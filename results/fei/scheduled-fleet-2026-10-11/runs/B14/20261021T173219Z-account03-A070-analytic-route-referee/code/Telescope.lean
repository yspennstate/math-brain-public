import Std

def debit (f : Nat → Int) : Nat → Int
  | 0 => 0
  | n + 1 => debit f n + (f n - f (n + 1))

theorem telescope (f : Nat → Int) (n : Nat) :
    debit f n = f 0 - f n := by
  induction n with
  | zero => simp [debit]
  | succ n ih =>
    simp only [debit, ih]
    omega
