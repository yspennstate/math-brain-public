import Lean.Elab.Tactic.Omega

theorem whole_sign_gate (d gain : Int) (h : gain = -d) : gain <= 0 <-> 0 <= d := by
  omega
