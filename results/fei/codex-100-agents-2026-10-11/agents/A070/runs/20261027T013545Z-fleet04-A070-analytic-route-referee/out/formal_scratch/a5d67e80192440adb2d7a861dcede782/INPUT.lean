import Mathlib.Tactic.Ring
theorem A070GaussianNorm (a b c d : Int) : (a*c-b*d)^2+(a*d+b*c)^2=(a^2+b^2)*(c^2+d^2) := by ring
