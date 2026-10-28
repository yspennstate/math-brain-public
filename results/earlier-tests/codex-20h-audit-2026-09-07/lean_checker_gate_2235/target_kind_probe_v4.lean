import Lean
theorem ProbeClosed : True := by trivial
def ProbeValue : Nat := 7
theorem ProbeAdmitted : False := by sorry
axiom ProbeAxiom : False
namespace Receipt
 theorem Named : True := by trivial
end Receipt
open Lean Elab Command in
run_cmd do
  for name in [``ProbeClosed, ``ProbeValue, ``ProbeAdmitted, ``ProbeAxiom, ``Receipt.Named] do
    let ci ← getConstInfo name
    let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
    logInfo m!"TARGET_KIND {name}: theorem={toString isTheorem}"
#print axioms ProbeClosed
#print axioms ProbeValue
#print axioms ProbeAdmitted
#print axioms ProbeAxiom
#print axioms Receipt.Named
