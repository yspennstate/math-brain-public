theorem A080_uniform_budget (H h I k p C : Nat)
    (hH : H <= h + 2 * p * (4 * k + 5))
    (hh : h <= C * I) (hc : 4 * k + 5 <= C * k) :
    H <= C * (I + 2 * k * p) := by
  calc
    H <= h + 2 * p * (4 * k + 5) := hH
    _ <= C * I + 2 * p * (C * k) :=
      Nat.add_le_add hh (Nat.mul_le_mul_left (2 * p) hc)
    _ = C * (I + 2 * k * p) := by
      simp [Nat.mul_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
