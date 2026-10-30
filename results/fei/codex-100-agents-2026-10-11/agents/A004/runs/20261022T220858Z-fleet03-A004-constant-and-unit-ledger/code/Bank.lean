import Mathlib

-- Scalar consequence of the reference telescope, not the KL or log theorem.
example (A H E W L : ℚ) (hp : W + L ≤ H + E) (hb : H + E ≤ A) :
    0 ≤ A - W - L := by
  linarith
