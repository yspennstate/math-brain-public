import Lean.Elab.Tactic.Omega

theorem a008_accounting (C D B Z : Int)
    (h : C = D - B + Z) (hB : 0 <= B) (hZ : Z <= 0) : C <= D := by
  omega
