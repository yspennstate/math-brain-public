import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Std.Tactic

theorem a035_cleared_cauchy (a b x y : Int) :
    (a*x+b*y)*(a*x+b*y) ≤ (a*a+b*b)*(x*x+y*y) := by
  have hs : 0 ≤ (a*y-b*x)*(a*y-b*x) := by
    by_cases h : 0 ≤ a*y-b*x
    · exact Int.mul_nonneg h h
    · exact Int.mul_nonneg_of_nonpos_of_nonpos (by omega) (by omega)
  have hi : (a*a+b*b)*(x*x+y*y) =
      (a*x+b*y)*(a*x+b*y) + (a*y-b*x)*(a*y-b*x) := by
    simp only [Int.add_mul, Int.mul_add, Int.sub_mul, Int.mul_sub]
    simp only [Int.mul_assoc, Int.mul_left_comm, Int.mul_comm]
    omega
  omega

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "a035_cleared_cauchy")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME a035_cleared_cauchy: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a035_cleared_cauchy: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a035_cleared_cauchy: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS a035_cleared_cauchy: " dependencies)))
