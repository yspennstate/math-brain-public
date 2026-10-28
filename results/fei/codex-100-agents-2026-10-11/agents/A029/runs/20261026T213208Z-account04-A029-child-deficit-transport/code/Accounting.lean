import Lean.Elab.Tactic.Omega

-- Only the doubled integer child-affordability algebra is formalized here.
-- KL bounds, real-valued physical weights and FEI are not asserted in Lean.
theorem child_affordability (c0 c1 s0 s1 r a : Int) :
    (c0 - s0) + (c1 - s1) <= 2 * (r + a) ↔
    c0 + c1 <= 2 * (r + a) + s0 + s1 := by
  omega

theorem replace_children (d0 d1 s0 s1 b0 b1 : Int)
    (h0 : d0 + s0 = b0) (h1 : d1 + s1 = b1) :
    (d0 + s0) + (d1 + s1) = b0 + b1 := by
  rw [h0, h1]
