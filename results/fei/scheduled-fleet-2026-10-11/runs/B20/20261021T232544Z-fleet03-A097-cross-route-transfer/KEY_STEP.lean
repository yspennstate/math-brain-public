-- Proposed key reserve algebra. NOT COMPILED: memok admission exited 1.
import Mathlib
theorem original_reserve_one_control
    (C I E X e : ℝ) (hC : 0 ≤ C) (hI : 0 ≤ I)
    (hE : E ≤ I / 4) (hX : 0 ≤ X) (he : 0 ≤ e)
    (hIe : 4 * e ≤ I) :
    12 * e ≤ (2*C+10)*(I+X-E) - (C*I+10*(X+E)) - 8*e := by
  have hCX : 0 ≤ C * X := mul_nonneg hC hX
  have hCI : 0 ≤ C * I := mul_nonneg hC hI
  have hCE : C * E ≤ C * (I / 4) := mul_le_mul_of_nonneg_left hE hC
  nlinarith
