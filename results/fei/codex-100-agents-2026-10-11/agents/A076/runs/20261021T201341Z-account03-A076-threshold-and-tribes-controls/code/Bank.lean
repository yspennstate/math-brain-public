import Std
theorem point_bank_release (m a : Int) :
  2 * (1-m*m) - ((1-(m+a)*(m+a))+(1-(m-a)*(m-a))) = 2*a*a := by
  simp only [Int.add_mul, Int.mul_add, Int.sub_mul, Int.mul_sub, Int.mul_assoc]
  omega
