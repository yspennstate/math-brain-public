import Lean.Elab.Tactic.Omega

theorem weak_child_int (p c d q : Int) (hp : 4*p <= d) (hc : c <= p) (hq : q = p+c) : 2*q <= d := by omega
