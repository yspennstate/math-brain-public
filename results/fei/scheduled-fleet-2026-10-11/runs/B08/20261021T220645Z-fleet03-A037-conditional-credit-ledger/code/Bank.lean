theorem bank_no_reuse (bank debit prior : Nat) (hb : 20 <= bank) (hd : debit <= 12) (hp : prior <= 5) : 3 + debit + prior <= bank := by
  have hh : 3 + debit + prior <= 3 + 12 + 5 := Nat.add_le_add (Nat.add_le_add_left hd 3) hp
  exact Nat.le_trans hh hb
