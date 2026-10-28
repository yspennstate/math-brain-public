import Lean
theorem Checked : True := by trivial

open Lean Elab Command in
run_cmd do
  let ci ← getConstInfo ``Checked
  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
  logInfo m!"TARGET_KIND Checked: theorem={toString isTheorem}"
#print axioms Checked
