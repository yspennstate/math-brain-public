import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/- The three orthogonal two-coordinate components contribute nonnegative
   squared norms a,b,c. This certifies the finite algebra behind the
   neighbor-refresh/BABP Dirichlet comparison, not a stochastic theorem. -/
theorem projectionEnergyComparison (a b c : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) :
    a + b + c ≤ a + b + 2*c ∧ a + b + 2*c ≤ 2*(a+b+c) := by
  constructor <;> linarith

theorem heatKernelExponent (g t : ℝ) :
    -g*t + (g*t/2)/2 = -(3*g/4)*t := by
  ring
