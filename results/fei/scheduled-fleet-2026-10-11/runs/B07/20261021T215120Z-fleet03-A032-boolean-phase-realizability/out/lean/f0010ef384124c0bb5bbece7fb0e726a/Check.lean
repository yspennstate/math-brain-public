import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
theorem A032_exact_power_guards :
    (3 : Nat)^5 < 2^8 ∧ 2^14 < 3^9 ∧ 3^9 < 2^16 := by decide

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "A032_exact_power_guards")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME A032_exact_power_guards: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND A032_exact_power_guards: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND A032_exact_power_guards: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS A032_exact_power_guards: " dependencies)))
