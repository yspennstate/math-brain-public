import Std.Tactic.Omega

-- After multiplying all rational edge probabilities by a common denominator,
-- this is the scalar crossing-flux funding step. It is not an entropy theorem.
theorem fluxBudget (i g r : Nat) (h : 2 * g ≤ r) :
    4 * i + 8 * g ≤ 4 * (i + r) := by
  omega
