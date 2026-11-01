/-
F0029 (Jarai, Conjecture 3.7, d = 3): the two arithmetic steps of the scaling relation
between the toppling-probability exponent eta and the avalanche-size exponent.

Step (iii): with R = n^(1/(3-eta)), the two error terms  R^(-(1-eps))  and  R^(2-eta+eps)/n
coincide, both equal to n^(-(1-eps)/(3-eta)).  Hence  nu(|Av| >= n) <= 2 n^(-(1-eps)/(3-eta)).

Step (i): with M = R^(3-delta), delta = 13 eps, the main term R^((3-delta)(2/3-eps)) beats the
subtracted term R^(2-delta+eps) because the first exponent is strictly larger (for 0 < eps < 1/10).
-/
import Mathlib

open Real

/-- Step (iii): equality of the two terms after the choice R = n^(1/(3-η)). -/
theorem F0029_step_iii (n η ε : ℝ) (hn : 0 < n) (hη : η < 3) :
    (n ^ (1 / (3 - η))) ^ (-(1 - ε)) + (n ^ (1 / (3 - η))) ^ (2 - η + ε) / n
      = 2 * n ^ (-(1 - ε) / (3 - η)) := by
  have h3 : (3 - η) ≠ 0 := by linarith
  rw [← Real.rpow_mul hn.le, ← Real.rpow_mul hn.le, ← Real.rpow_sub_one hn.ne']
  have e1 : 1 / (3 - η) * (-(1 - ε)) = -(1 - ε) / (3 - η) := by field_simp
  have e2 : 1 / (3 - η) * (2 - η + ε) - 1 = -(1 - ε) / (3 - η) := by field_simp; ring
  rw [e1, e2]; ring

/-- Step (i): the exponent comparison with δ = 13 ε. -/
theorem F0029_step_i (ε : ℝ) (h0 : 0 < ε) (h1 : ε < 1 / 10) :
    2 - 13 * ε + ε < (3 - 13 * ε) * (2 / 3 - ε) := by
  nlinarith

#print axioms F0029_step_iii
#print axioms F0029_step_i
