import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

-- The exact add-one Poisson remainder in the half-moment derivative.
theorem annealing_remainder (z x : ℝ) (hz : z ^ 2 = 1 + x) :
    z - 1 - x / 2 = -((z - 1) ^ 2) / 2 := by
  nlinarith

-- A two-outcome conditional likelihood ratio: a,b are its square roots,
-- p and 1-p are probabilities, and m is the square root of its mean M.
theorem conditional_deficit_identity (p a b m : ℝ)
    (hnorm : p * a ^ 2 + (1-p) * b ^ 2 = 1) :
    p * (m*a-m)^2 + (1-p)*(m*b-m)^2
      = 2*m^2*(1-(p*a+(1-p)*b)) := by
  calc
    p * (m*a-m)^2 + (1-p)*(m*b-m)^2 =
        m^2*(p*a^2+(1-p)*b^2-2*(p*a+(1-p)*b)+1) := by ring
    _ = 2*m^2*(1-(p*a+(1-p)*b)) := by rw [hnorm]; ring
