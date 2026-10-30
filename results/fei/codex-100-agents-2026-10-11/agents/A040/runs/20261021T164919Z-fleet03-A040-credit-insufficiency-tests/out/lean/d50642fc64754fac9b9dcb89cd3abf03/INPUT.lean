import Mathlib

theorem inherited_core_release (alpha a0 a1 a m jd e ig t : ?)
    (ha : (a0+a1)/2=a) :
    alpha * (a*m*jd+a*e*m*(m-1)/2+m*e*ig) -
    alpha * (((a0+a1)/2)*m*jd+((a0+a1)/2)*e*m*(m-1)/2+m*e*(ig-t))
    = alpha*m*e*t := by
  rw [ha]
  ring

#print axioms inherited_core_release
