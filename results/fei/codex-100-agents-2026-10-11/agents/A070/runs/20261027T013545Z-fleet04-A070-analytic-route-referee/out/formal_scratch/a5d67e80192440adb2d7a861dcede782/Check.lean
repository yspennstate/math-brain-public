import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Mathlib.Tactic.Ring
theorem A070GaussianNorm (a b c d : Int) : (a*c-b*d)^2+(a*d+b*c)^2=(a^2+b^2)*(c^2+d^2) := by ring

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "A070GaussianNorm")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME A070GaussianNorm: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND A070GaussianNorm: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND A070GaussianNorm: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS A070GaussianNorm: " dependencies)))
