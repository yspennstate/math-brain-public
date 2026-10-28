import Mathlib.Tactic
-- Only the final ordered-field implication, not the analytic KL/log theorem.
theorem refund_sign (D E J m p : ℝ) (hDE : E ≤ D) (hE : 0 ≤ E)
    (hJ : 0 ≤ J) (hm : m ≤ 1) (hp : 0 ≤ p) :
    -(D - m * E + (1 + p) * J) / 2 ≤ 0 := by
  have h1 : 0 ≤ (1 - m) * E := mul_nonneg (sub_nonneg.mpr hm) hE
  have h2 : 0 ≤ (1 + p) * J := mul_nonneg (by linarith) hJ
  nlinarith
#print axioms refund_sign
