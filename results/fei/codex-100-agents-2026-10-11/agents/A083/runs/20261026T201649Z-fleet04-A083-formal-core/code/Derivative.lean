import Init.Data.Rat.Lemmas

namespace A083Stage21

-- This checks the missing factor in the displayed derivative, not logarithmic
-- differentiation, the real minimizer, or the universal FEI source premise.
theorem derivative_regression :
    (-(1/4 : Rat)/(1/3) + (1/2)/(5/12) = 9/20) ∧
    (((1/12 : Rat)/((1/3)*(5/12))) = 3/5) ∧
    ((9/20 : Rat) ≠ 3/5) ∧
    ((3/4 : Rat)*((1/12)/((1/3)*(5/12))) = 9/20) := by
  decide

end A083Stage21
