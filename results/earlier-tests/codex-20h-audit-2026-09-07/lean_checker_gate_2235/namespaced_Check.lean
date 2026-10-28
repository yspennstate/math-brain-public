import Lean
namespace Receipt
theorem Named : True := by trivial
end Receipt

open Lean Elab Command in
run_cmd do
  let ci ← getConstInfo ``Receipt.Named
  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
  logInfo m!"TARGET_KIND Receipt.Named: theorem={toString isTheorem}"
#print axioms Receipt.Named
