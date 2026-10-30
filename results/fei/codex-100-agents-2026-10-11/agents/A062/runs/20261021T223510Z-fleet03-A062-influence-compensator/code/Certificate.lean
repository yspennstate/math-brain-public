theorem paired_reserve_reset (debt child : Nat) (h : debt + child <= 363) :
    debt + child - 384 = 0 := by
  exact Nat.sub_eq_zero_of_le (Nat.le_trans h (by decide))

theorem width_threshold (k c : Nat) (h : 5*c < 2*k) : 0 < 2*k-5*c := by
  exact Nat.sub_pos_of_lt h
