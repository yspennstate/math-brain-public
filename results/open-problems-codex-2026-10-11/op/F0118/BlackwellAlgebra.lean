import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace F0118Second

theorem branch_ratio_identity (a h k beta c : ℝ) :
    (a * (beta + 2*c)) * (k*c^2) -
      (a*c) * (h*c + k*c^2) =
      a*c^2 * (k*beta-h+k*c) := by ring

theorem informative_mass_identity (a h k beta c s : ℝ) :
    c*(a*beta+2*h*c+2*a*c+2*k*c^2) +
      (2*s-4*c)*(a*c+2*k*c^2) =
      c*(a*(beta+2*s)+(2*h-2*a+4*s*k)*c-6*k*c^2) := by ring

theorem low_tail_derivative_certificate (a h k c s v : ℝ) :
    (a+2*k*c) - v*(a-h-2*k*s+6*k*c) =
      (1-v)*(a+2*k*c) + v*(h+2*k*(s-2*c)) := by ring

theorem high_tail_derivative_certificate (a h k c : ℝ) :
    2*a*(a+2*k*c) - a*(2*h+2*a+4*k*c) = -2*a*h := by ring

end F0118Second
