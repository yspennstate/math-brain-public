import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- Conditional algebraic step in geometric uncrossing; geometry is proved in ATTEMPT.md.
theorem uncross_sum (old1 old2 new1 new2 a b c d : ℝ)
    (h1 : old1 = a + b) (h2 : old2 = c + d)
    (h3 : new1 < a + d) (h4 : new2 < c + b) :
    new1 + new2 < old1 + old2 := by
  linarith

-- Rational certificate for the capped-cost counterexample coordinates.
def sqdist (x y u v : ℚ) : ℚ := (x-u)^2 + (y-v)^2
example : sqdist (-1/10) 0 (1/10) 0 = 1/25 := by norm_num [sqdist]
example : sqdist 0 (-10) 0 10 = 400 := by norm_num [sqdist]
example : sqdist (-1/10) 0 0 10 = 10001/100 := by norm_num [sqdist]
example : sqdist 0 (-10) (1/10) 0 = 10001/100 := by norm_num [sqdist]
example : (10001/100 : ℚ) > 1 := by norm_num
example : (1/5 : ℚ) + 1 < 1 + 1 := by norm_num
