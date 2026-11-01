import Lean
axiom Unsupported : False
theorem Dependent : False := Unsupported

open Lean Elab Command in
run_cmd do
  let ci ← getConstInfo ``Dependent
  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
  logInfo m!"TARGET_KIND Dependent: theorem={toString isTheorem}"
#print axioms Dependent
