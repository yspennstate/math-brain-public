import Std.Tactic

-- N times the two probabilities in PROOF equations(1)--(2), for h2.
theorem paired_error_cancel (n a e d q : Int)
    (repair : n - a ≤ 4 * (d - e))
    (first : a - 4 * e ≤ 2 * q) : n - 4 * d ≤ 2 * q := by
  omega
