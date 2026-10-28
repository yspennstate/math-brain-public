theorem calibration_mass (k b c r : Nat) : k * b + k * c + r = k * (b + c) + r := by
  rw [Nat.mul_add]
