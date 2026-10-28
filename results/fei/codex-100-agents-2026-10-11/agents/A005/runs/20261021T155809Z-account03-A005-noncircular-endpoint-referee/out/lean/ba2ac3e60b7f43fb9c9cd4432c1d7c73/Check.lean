import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Analysis.SpecialFunctions.Log.Basic

theorem whole_sign_sum (H q b : Real) :
    (H + q + b) + (H + q - b) = 2 * H + 2 * q := by ring

theorem refund_error_upper (u I : Real) (hu : 0 < u) (hu1 : u <= 1)
    (hI : 1 - u <= I) :
    1 - u + u * Real.log u <= I ^ 2 := by
  have hlog : Real.log u <= u - 1 := Real.log_le_sub_one_of_pos hu
  have hm : u * Real.log u <= u * (u - 1) := mul_le_mul_of_nonneg_left hlog (le_of_lt hu)
  have hpos : 0 <= 1 - u := by linarith
  have hIp : 0 <= I := le_trans hpos hI
  nlinarith [sq_nonneg (I - (1-u))]

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "refund_error_upper")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME refund_error_upper: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND refund_error_upper: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND refund_error_upper: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS refund_error_upper: " dependencies)))
