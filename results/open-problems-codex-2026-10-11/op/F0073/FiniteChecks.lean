import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

-- Euler cancellation for two free vertices and a grounded boundary.
theorem edge_euler_cancellation (x y a b c : Real) :
    x * (a + b) + y * (-b + c) = x * a + (x - y) * b + y * c := by
  ring

-- Effective-resistance Cauchy-Schwarz on the path 0--x--y.
theorem grounded_path_resistance (x y : Real) :
    y ^ 2 <= 2 * (x ^ 2 + (x - y) ^ 2) := by
  nlinarith [sq_nonneg (2 * x - y)]

-- Gaussian edge lattice inequality: ordered pairings minimize energy.
theorem gaussian_edge_monge (a b c d : Real) (hab : a <= b) (hcd : c <= d) :
    (a-c)^2 + (b-d)^2 <= (a-d)^2 + (b-c)^2 := by
  nlinarith [mul_nonneg (sub_nonneg.mpr hab) (sub_nonneg.mpr hcd)]
