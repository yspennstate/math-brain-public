import Lean
def Number : Nat := 7

open Lean Elab Command in
run_cmd do
  let ci ← getConstInfo ``Number
  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
  logInfo m!"TARGET_KIND Number: theorem={toString isTheorem}"
#print axioms Number
