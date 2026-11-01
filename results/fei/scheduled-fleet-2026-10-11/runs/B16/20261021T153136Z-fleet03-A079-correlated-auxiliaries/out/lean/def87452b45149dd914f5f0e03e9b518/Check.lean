import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Lean

def ternary (i : Fin 3) : Int := if i.val = 0 then 0 else if i.val = 1 then 1 else -1
def sign (i : Fin 2) : Int := if i.val = 0 then 1 else -1

theorem complementary_phase_is_boolean :
    ∀ (a b : Fin 3) (z h : Fin 2),
      ternary a * ternary b = 0 →
      ternary a * ternary a + ternary b * ternary b = 1 →
      (ternary a + sign z * ternary b * sign h = 1 ∨
       ternary a + sign z * ternary b * sign h = -1) := by
  decide

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "complementary_phase_is_boolean")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME complementary_phase_is_boolean: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND complementary_phase_is_boolean: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND complementary_phase_is_boolean: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS complementary_phase_is_boolean: " dependencies)))
