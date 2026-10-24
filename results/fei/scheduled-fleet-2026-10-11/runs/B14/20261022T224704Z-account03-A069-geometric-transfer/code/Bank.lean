import Std.Tactic

-- Fortieth-bit units: a single bank of at least25 units pays at most24
-- units of cumulative charges, retaining at least1 unit. The real entropy
-- and child-bank bounds are separate premises, not formalized here.
theorem bank_remainder (bank charges : Nat) (hb : 25 ≤ bank)
    (hc : charges ≤ 24) : charges + 1 ≤ bank := by
  omega
