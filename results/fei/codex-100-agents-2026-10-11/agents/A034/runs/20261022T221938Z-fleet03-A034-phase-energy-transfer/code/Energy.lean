import Lean.Elab.Tactic.Omega

theorem A034_energy (a b c : Int) (h : 3*c <= a+b) : a+b <= 3*(a+b-2*c) := by omega
