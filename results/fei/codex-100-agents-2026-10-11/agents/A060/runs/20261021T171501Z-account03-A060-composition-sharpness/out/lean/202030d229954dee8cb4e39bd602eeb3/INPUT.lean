import Lean

def geom (b : Int) : Nat → Int
  | 0 => 0
  | n + 1 => b ^ n + geom b n

theorem guard_geometric (b : Int) (n : Nat) :
    (b - 1) * geom b n = b ^ n - 1 := by
  induction n with
  | zero => simp [geom]
  | succ n ih =>
    rw [geom, Int.mul_add, ih, pow_succ]
    simp only [Int.sub_mul, Int.one_mul]
    rw [Int.mul_comm b (b ^ n)]
    omega
