import Mathlib

-- Only the single-split real algebra in the physical ledger, not FEI.
example (h d e0 e1 r0 r1 : Real) :
    h + d + ((r0 - e0) + (r1 - e1)) / 2 =
      h + (d - (e0 + e1) / 2) + (r0 + r1) / 2 := by
  ring
