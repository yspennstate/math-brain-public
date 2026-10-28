theorem A080_four_row_witness (s0 s1 : Bool) :
  (((s0,s0) != (s0,!s0)) && ((s0,s0) != (!s1,!s1)) && ((s0,!s0) != (!s1,!s1))) = true
  ? (((s0,s0) != (s0,!s0)) && ((s0,s0) != (s1,!s1)) && ((s0,!s0) != (s1,!s1))) = true := by
  cases s0 <;> cases s1 <;> decide
