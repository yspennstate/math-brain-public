theorem A080_budget (a b u v K c : Nat)
    (ha : a <= K * u) (hb : b <= K * v) :
    a + b + c <= K * (u + v) + c := by
  calc
    a + b + c <= (K * u + K * v) + c :=
      Nat.add_le_add_right (Nat.add_le_add ha hb) c
    _ = K * (u + v) + c := by rw [Nat.mul_add]
