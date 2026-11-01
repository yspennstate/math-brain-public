import Lean

theorem A074_transport_numerator (s d e t : Int) :
    t * (s + e) - (d + e) * t = t * (s - d) := by
  simp only [Int.mul_add, Int.add_mul, Int.mul_sub, Int.mul_comm d t, Int.mul_comm e t]
  omega
