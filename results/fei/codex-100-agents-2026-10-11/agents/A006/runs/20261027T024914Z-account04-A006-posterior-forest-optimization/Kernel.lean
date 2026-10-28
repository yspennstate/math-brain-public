import Mathlib

example (a b c t : ?) (ha : 0 ? a) (hb : 0 ? b) (hc : 0 ? c) (ht : 0 ? t) :
 117 * ((a+t/2)+(b+t/2)+(c+t/2)) * (a+b+c+t)^2
 - 242 * ((a+t/2)*(b+t/2)+(a+t/2)*(c+t/2)+(b+t/2)*(c+t/2))*(a+b+c+t)
 + 48*(a+t/2)*(b+t/2)*(c+t/2) ? 0 := by
 have hid : 117 * ((a+t/2)+(b+t/2)+(c+t/2)) * (a+b+c+t)^2
  - 242 * ((a+t/2)*(b+t/2)+(a+t/2)*(c+t/2)+(b+t/2)*(c+t/2))*(a+b+c+t)
  + 48*(a+t/2)*(b+t/2)*(c+t/2)
  = 117*(a^3+b^3+c^3)+109*(a^2*b+a^2*c+b^2*a+b^2*c+c^2*a+c^2*b)
    +24*a*b*c+(335/2:?)*t*(a^2+b^2+c^2)+117*t*(a*b+a*c+b*c)
    +(113/2:?)*t^2*(a+b+c) := by ring
 rw [hid]
 positivity
