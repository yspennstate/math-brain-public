import Mathlib

theorem perturbation_square (x y : ℝ) : (x+y)^2 ≤ 2*x^2+2*y^2 := by
  nlinarith [sq_nonneg (x-y)]

theorem joint_sector_budget (jr jm j c d : ℝ)
    (hr : 0 ≤ jr) (hd : 0 ≤ d) (hcd : c ≤ d)
    (hj : jr+jm ≤ j) : c*jr+d*jm ≤ d*j := by
  have h1 : c*jr ≤ d*jr := mul_le_mul_of_nonneg_right hcd hr
  have h2 : d*(jr+jm) ≤ d*j := mul_le_mul_of_nonneg_left hj hd
  nlinarith

#print axioms perturbation_square
#print axioms joint_sector_budget
