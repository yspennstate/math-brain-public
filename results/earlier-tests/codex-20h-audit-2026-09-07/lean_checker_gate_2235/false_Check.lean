import Lean
theorem Incorrect : (1 : Nat) = 2 := by rfl

open Lean Elab Command in
run_cmd do
  let ci ← getConstInfo ``Incorrect
  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
  logInfo m!"TARGET_KIND Incorrect: theorem={toString isTheorem}"
#print axioms Incorrect
