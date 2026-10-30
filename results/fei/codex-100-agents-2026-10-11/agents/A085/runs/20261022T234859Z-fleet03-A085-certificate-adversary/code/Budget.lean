import Std

-- Integer-scaled induction step for the 61/4 reserve only.
-- This source does not formalize logarithms, source references or Boolean functions.
theorem reserve_increment (p d : Int) (hp : 4 <= p)
    (hold : 61 + 19 * (d - 1) <= 20 * p) :
    61 + 19 * d <= 20 * (2 * p) := by
  omega

#print axioms reserve_increment
