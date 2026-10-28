import Lean
import Mathlib.Tactic.NormNum
theorem MathlibChecked : (2 : Rat)^3 = 8 := by norm_num

open Lean Elab Command in
run_cmd do
  let ci ← getConstInfo ``MathlibChecked
  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false
  logInfo m!"TARGET_KIND MathlibChecked: theorem={toString isTheorem}"
#print axioms MathlibChecked
