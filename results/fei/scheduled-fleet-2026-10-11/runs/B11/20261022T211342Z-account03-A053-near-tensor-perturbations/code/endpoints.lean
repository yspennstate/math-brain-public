import Mathlib
example (p q l : ℝ) (hp : 0 < p) (hQ : 4 * p ≤ q)
    (hL : l < (71 / 2 : ℝ) * p) : l - 9 * q < -(p / 2) := by
  linarith

example (n I a b : ℝ) (hn : 2 ≤ n) (ha : I ≤ n * a)
    (hb : I-a ≤ (n-1)*b) : 2*I ≤ n*(a+b) := by
  have h1 := mul_nonneg (sub_nonneg.mpr hn) (sub_nonneg.mpr ha)
  have h2 := mul_nonneg (by linarith : 0 ≤ n) (sub_nonneg.mpr hb)
  by_contra h
  have hx : n*(a+b)-2*I < 0 := by linarith
  have hm := mul_neg_of_pos_of_neg (by linarith : 0 < n-1) hx
  nlinarith [h1, h2]
