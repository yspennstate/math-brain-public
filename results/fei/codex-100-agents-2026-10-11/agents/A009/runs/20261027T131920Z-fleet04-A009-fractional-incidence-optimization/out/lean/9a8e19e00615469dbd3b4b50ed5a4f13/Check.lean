import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
-- A finite boundary check only, not the continuous score certificate.
theorem triangle_grid :
    forall a b c : Fin 5,
      a.val + b.val <= 4 ->
      a.val + c.val <= 4 ->
      b.val + c.val <= 4 ->
      6*a.val*b.val*c.val <=
        4*(a.val*b.val+a.val*c.val+b.val*c.val) := by
  decide

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "triangle_grid")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME triangle_grid: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND triangle_grid: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND triangle_grid: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS triangle_grid: " dependencies)))
