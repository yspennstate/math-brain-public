import Std.Tactic

-- In quarter-bit units, three charges of at most one unit leave one unit
-- unused from a single four-unit terminal bank. The entropy inequalities
-- and the identification of this bank are separate mathematical premises.
theorem quarter_bank (a b c : Nat) (ha : a ≤ 1) (hb : b ≤ 1)
    (hc : c ≤ 1) : a + b + c + 1 ≤ 4 := by
  omega
