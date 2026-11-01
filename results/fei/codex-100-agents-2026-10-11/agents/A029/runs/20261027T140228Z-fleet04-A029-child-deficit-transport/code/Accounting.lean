import Lean.Elab.Tactic.Omega

-- This is only doubled integer accounting, not Fourier analysis or the rank theorem.
theorem child_payment (u old parent child0 child1 fee : Int)
    (ledger : 2 * parent = child0 + child1 + 2 * fee)
    (paid : parent + old <= u) :
    child0 + child1 + 2 * fee + 2 * old <= 2 * u := by
  omega
