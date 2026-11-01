import Mathlib.Tactic.Linarith

theorem a042_endpoint_error (s e2 e3 : Rat)
    (triple : 3 * e3 <= s * e2) (nonneg : 0 <= s * e2) :
    5 * e3 + 2 * s * e2 <= 4 * s * e2 := by
  linarith
