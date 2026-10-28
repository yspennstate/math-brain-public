import Mathlib

-- Intended scalar nonnegativity component only; NOT compiled this stage.
example (p C x : ℝ) (hp : 0 ≤ p) (hC : 4 ≤ C) (hx : -4*p ≤ x) :
    0 ≤ p*C+x := by
  nlinarith
