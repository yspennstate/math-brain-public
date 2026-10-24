import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

-- The diagonal computations in the two Darboux products.
theorem first_factor_diagonal (A Ai u : ℝ) :
    Ai + A * (1-u) = A + Ai - A*u := by ring

theorem swapped_factor_diagonal (A Ai u theta : ℝ) :
    Ai + A * (1-theta*u) = A + Ai - (A*theta)*u := by ring

-- Multiply the eigenvalue/gap identity by theta to avoid divisions.
theorem first_mode_gap (p q theta : ℝ) :
    theta - (theta*(1-p-q+q*theta)+p) =
      (1-theta)*(q*theta-p) := by ring

-- C_22(1)-W_1, with both sides multiplied by theta^2, p=q*r.
theorem remaining_spectral_mass (q r theta : ℝ) :
    (1-theta)*q^2*r*(1-r)*theta^2 -
      q^2*r*(1-theta)*(theta^2-r) =
    q^2*r^2*(1-theta)*(1-theta^2) := by ring
