import Mathlib.Tactic
namespace A059
-- Conditional lower price of compulsory liquidation: no entropy theorem imported.
theorem mandatory_frozen_price (r e x0 x1 c0 c1 : ℚ)
    (h0 : 0 ≤ x0) (h1 : 0 ≤ x1) (hc0 : r ≤ c0) (hc1 : r ≤ c1)
    (hr : 0 ≤ r) (he : e ≤ x0+x1) :
    r*e ≤ c0*x0+c1*x1 := by
  nlinarith
end A059
