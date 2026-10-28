import Lean
theorem Admitted : False := by sorry

open Lean Elab Command in
run_cmd do
  let ci ← getConstInfo ``Admitted
  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
  logInfo m!"TARGET_KIND Admitted: theorem={toString isTheorem}"
#print axioms Admitted
