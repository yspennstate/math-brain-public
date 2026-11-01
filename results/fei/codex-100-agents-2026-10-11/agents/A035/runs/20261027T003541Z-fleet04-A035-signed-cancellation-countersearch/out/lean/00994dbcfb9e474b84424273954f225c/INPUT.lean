import Std.Tactic

theorem a035_cleared_cauchy (a b x y : Int) :
    (a*x+b*y)*(a*x+b*y) ≤ (a*a+b*b)*(x*x+y*y) := by
  have hs : 0 ≤ (a*y-b*x)*(a*y-b*x) := by
    by_cases h : 0 ≤ a*y-b*x
    · exact Int.mul_nonneg h h
    · exact Int.mul_nonneg_of_nonpos_of_nonpos (by omega) (by omega)
  have hi : (a*a+b*b)*(x*x+y*y) =
      (a*x+b*y)*(a*x+b*y) + (a*y-b*x)*(a*y-b*x) := by
    simp only [Int.add_mul, Int.mul_add, Int.sub_mul, Int.mul_sub]
    simp only [Int.mul_assoc, Int.mul_left_comm, Int.mul_comm]
    omega
  omega
