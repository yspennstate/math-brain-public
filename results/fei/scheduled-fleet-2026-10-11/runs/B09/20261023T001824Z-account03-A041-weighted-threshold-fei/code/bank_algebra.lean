import Mathlib

-- Uncompiled statement: memory admission failed. This is only the scalar
-- consequence of the analytically proved projection and degree inequalities.
example (i p j m d : ℝ) (hp : p ≤ i / 2) (hj : p + j = i)
    (hm : m ≤ j / 2) (hd : d = j - m) : i / 4 ≤ d := by
  linarith
