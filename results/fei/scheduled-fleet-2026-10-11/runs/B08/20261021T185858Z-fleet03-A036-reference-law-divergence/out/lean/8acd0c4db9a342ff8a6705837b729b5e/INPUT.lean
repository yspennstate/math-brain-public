import Lean.Elab.Tactic.Omega
 theorem signedRecovery (a d r w s ce i : Int)
 (hs : 0 <= s) (hid : s - (a + d - 4*r + w) = 4*i-ce-w) :
 max (a+d-4*r+w) 0 <= s ? ce+w <= 4*i := by
 omega
#print axioms signedRecovery
