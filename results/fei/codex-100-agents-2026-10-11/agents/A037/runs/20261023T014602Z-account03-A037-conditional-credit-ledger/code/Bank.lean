theorem second_reset_bank (bank prior second : Nat) (hb : 24 <= bank) (hp : prior <= 6) (hs : second <= 1) : 17 + prior + second <= bank := by
  have hh : 17 + prior + second <= 17 + 6 + 1 := Nat.add_le_add (Nat.add_le_add_left hp 17) hs
  exact Nat.le_trans hh hb
