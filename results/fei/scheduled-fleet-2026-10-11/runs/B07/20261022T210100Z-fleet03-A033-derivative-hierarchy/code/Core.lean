import Std.Tactic

theorem A033ControllerStep
    (d u u0 u1 b0 b1 v : Int)
    (h : d + u0 + u1 <= u) :
    d + (u0 + b0*v) + (u1 + b1*v) <= u + (b0+b1)*v := by
  simp only [Int.add_mul]
  omega

#print axioms A033ControllerStep
