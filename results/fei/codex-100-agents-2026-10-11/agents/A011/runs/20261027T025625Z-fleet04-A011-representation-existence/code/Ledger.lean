import Mathlib.Tactic.Linarith

theorem a011_physical_ledger_step (dparent dinherited dchild reset qloss : Real)
    (hq : qloss = dparent - dinherited)
    (hr : reset = dchild - dinherited) :
    dchild = dparent + reset - qloss := by
  linarith
