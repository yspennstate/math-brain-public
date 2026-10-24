import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

def criticalV (x : ℝ) : ℝ :=
  (2/5)*x^4 - (16/15)*x^3 + (2/5)*x^2 + (8/5)*x

def criticalW (x : ℝ) : ℝ :=
  (1/20)*x^4 - (4/15)*x^3 + (1/5)*x^2 + (8/5)*x

theorem critical_potential_rescaling (x : ℝ) :
    criticalW (2*x) = 2*criticalV x := by
  unfold criticalW criticalV
  ring

theorem tail_power_separation (c C y : ℝ) (hy : 0 < y)
    (h : C < c*y^3) : C*y^4 < c*y^7 := by
  calc
    C*y^4 < (c*y^3)*y^4 := mul_lt_mul_of_pos_right h (pow_pos hy 4)
    _ = c*y^7 := by ring

theorem exotic_k1_exponents : (3/2 : ℚ) - 1/3 = 7/6 := by ring
