import Mathlib.Tactic.Ring

-- Uncompiled. This algebraic numerator is only one step in PROOF.md;
-- it does not formalize entropy, logarithmic differentiation or full FEI.
theorem spike_derivative_numerator (t u : Real) :
    (1-t)*(t+u*(1-t))-t*(1-t)*(1-u)=u*(1-t) := by
  ring
