import Init

-- Integer allocation sanity only. The logarithmic dominance and Fourier
-- transport arguments are not formalized by this statement.
theorem fresh_reset_allocation (old fresh inf : Nat)
    (hOld : old <= 3 * inf) (hReset : fresh <= old + 3 * inf) :
    fresh + inf <= 7 * inf := by
  have h : fresh <= 3 * inf + 3 * inf :=
    Nat.le_trans hReset (Nat.add_le_add_right hOld (3 * inf))
  calc
    fresh + inf <= (3 * inf + 3 * inf) + inf := Nat.add_le_add_right h inf
    _ = (3 + 3) * inf + 1 * inf := by rw [Nat.add_mul, Nat.one_mul]
    _ = ((3 + 3) + 1) * inf := (Nat.add_mul (3 + 3) 1 inf).symm
    _ = 7 * inf := rfl
