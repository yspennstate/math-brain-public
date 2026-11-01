import Mathlib
example (e B x0 x : ℝ) (hB : 4*e ≤ B) (h0 : x0 ≤ 0) (hx : -4*e ≤ x) : 0 ≤ B-x0+x := by linarith
example (B x0 xp xm : ℝ) : x0-(xp+xm)/2 + ((B-x0+xp)+(B-x0+xm))/2 = B := by ring
