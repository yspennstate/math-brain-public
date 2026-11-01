theorem reserve_max_sum (a b c d : Nat) :
    Nat.max (a+c) (b+d) <= Nat.max a b + Nat.max c d := by
  apply Nat.max_le.mpr
  constructor
  · exact Nat.add_le_add (Nat.le_max_left a b) (Nat.le_max_left c d)
  · exact Nat.add_le_add (Nat.le_max_right a b) (Nat.le_max_right c d)

#print axioms reserve_max_sum
