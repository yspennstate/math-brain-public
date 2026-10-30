import Lean.Elab.Tactic.Omega

-- Cleared-denominator budget implication only. The entropy bound is a premise.
theorem same_bank_budget (D R E U : Int)
    (hE : 0 <= E) (hR : E <= R)
    (hprofile : 4*D <= 2*R+19*E)
    (hadmit : 6*R <= 4*U+E) :
    R <= U /\ D <= 5*E+U-R := by
  omega
