import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
-- Finite sign case of A080's last cut. Bool complement encodes sign change.
theorem a071_four_rows (s t : Bool) :
    (((s,s) ≠ (s,!s)) ∧ ((s,s) ≠ (!t,!t)) ∧ ((s,!s) ≠ (!t,!t))) ∨
    (((s,s) ≠ (s,!s)) ∧ ((s,s) ≠ (t,!t)) ∧ ((s,!s) ≠ (t,!t))) := by
  cases s <;> cases t <;> decide

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "a071_four_rows")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME a071_four_rows: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a071_four_rows: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a071_four_rows: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS a071_four_rows: " dependencies)))
