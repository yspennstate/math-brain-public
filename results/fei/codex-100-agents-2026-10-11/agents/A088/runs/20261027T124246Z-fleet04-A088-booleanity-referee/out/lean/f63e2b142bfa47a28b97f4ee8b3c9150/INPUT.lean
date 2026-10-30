theorem A088_sector_bank (source spent terminal : Nat)
    (h : source = spent + terminal) : spent ? source := by
  rw [h]
  exact Nat.le_add_right spent terminal
