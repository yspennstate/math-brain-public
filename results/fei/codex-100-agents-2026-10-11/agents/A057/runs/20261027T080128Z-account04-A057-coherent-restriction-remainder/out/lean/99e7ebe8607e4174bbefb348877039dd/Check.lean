import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000
def wave (den k : Nat) : Nat :=
  8 * min (k % den) (den - k % den) +
  4 * min ((2*k) % den) (den - (2*k) % den) +
  2 * min ((4*k) % den) (den - (4*k) % den) +
  min ((8*k) % den) (den - (8*k) % den)
theorem a057_boundary_vertices :
  ? i j : Fin 17, wave 32 (i.val+j.val) ?
    wave 16 i.val + wave 16 j.val + 8*((i.val-j.val)+(j.val-i.val)) := by decide

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "a057_boundary_vertices")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME a057_boundary_vertices: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a057_boundary_vertices: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a057_boundary_vertices: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS a057_boundary_vertices: " dependencies)))
