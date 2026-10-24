import Mathlib.Tactic

theorem a011_same_bank
    (c C0 Ig Ifull bill : ℝ)
    (hC : 0 ≤ C0) (hI : 0 ≤ Ig)
    (hc : c ≤ C0 * Ig)
    (hf : (3 / 4 : ℝ) * Ig ≤ Ifull)
    (hb : bill ≤ (3 / 2 : ℝ) * c + (41 / 4 : ℝ) * Ig) :
    (4 * C0 + 15) * Ifull - bill ≥ ((3 / 2 : ℝ) * C0 + 1) * Ig := by
  have hK : 0 ≤ 4 * C0 + 15 := by positivity
  have hm := mul_le_mul_of_nonneg_left hf hK
  nlinarith

theorem a011_dyadic_polynomial_step (q : ℝ) (hq : 2 ≤ q) :
    (q+1)^2 + 15*(q+1) + 7 ≤ 2*(q^2 + 15*q + 7) := by
  nlinarith [sq_nonneg (q-2)]

theorem a011_js_algebra (u v : ℝ) :
    (u^2-v^2)^2 ≤ 2*(u^2+v^2)*(u-v)^2 := by
  nlinarith [sq_nonneg ((u-v)^2)]

#print axioms a011_same_bank
#print axioms a011_dyadic_polynomial_step
#print axioms a011_js_algebra
