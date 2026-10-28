import Mathlib.Tactic

theorem A084_row_transfer (b d k l : Real) (hk : 0 <= k)
    (hbd : b <= d) (hl : l <= k*b) : l <= k*d := by
  nlinarith
