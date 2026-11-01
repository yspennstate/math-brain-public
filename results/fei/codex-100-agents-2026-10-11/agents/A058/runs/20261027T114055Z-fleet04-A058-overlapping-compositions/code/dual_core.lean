theorem a058_liquidation_exchange
    (r gap u l v need : Nat) (hu : l ≤ u) (hv : need ≤ v) :
    r * l + gap * need ≤ r * u + gap * v :=
  Nat.add_le_add (Nat.mul_le_mul_left r hu) (Nat.mul_le_mul_left gap hv)
