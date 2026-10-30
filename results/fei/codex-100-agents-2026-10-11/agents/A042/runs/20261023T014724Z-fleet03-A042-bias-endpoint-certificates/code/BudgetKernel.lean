import Lean.Elab.Tactic.Omega

theorem endpoint_scale_budget (D R : Int) :
    4 * (2 * D - R) + 3 * (D - R) = 11 * D - 7 * R := by
  omega
