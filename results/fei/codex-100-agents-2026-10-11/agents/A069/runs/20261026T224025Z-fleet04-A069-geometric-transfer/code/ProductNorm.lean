import Std.Tactic.Omega

-- Exact Gaussian-integer numerator step used in DERIVATION Section 2.
theorem gaussian_integer_product_norm (a b m : Int) :
    (m*a-b)*(m*a-b)+(a+m*b)*(a+m*b) =
      (m*m+1)*(a*a+b*b) := by
  simp only [Int.mul_sub, Int.sub_mul, Int.mul_add, Int.add_mul, Int.one_mul]
  simp only [Int.mul_comm, Int.mul_left_comm, Int.mul_assoc]
  omega
