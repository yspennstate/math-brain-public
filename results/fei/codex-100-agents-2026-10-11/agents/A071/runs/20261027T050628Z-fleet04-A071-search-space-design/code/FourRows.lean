-- Finite sign case of A080's last cut. Bool complement encodes sign change.
theorem a071_four_rows (s t : Bool) :
    (((s,s) ≠ (s,!s)) ∧ ((s,s) ≠ (!t,!t)) ∧ ((s,!s) ≠ (!t,!t))) ∨
    (((s,s) ≠ (s,!s)) ∧ ((s,s) ≠ (t,!t)) ∧ ((s,!s) ≠ (t,!t))) := by
  cases s <;> cases t <;> decide
