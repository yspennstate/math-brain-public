import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Lean

theorem profile_tail_bound (m : Nat) : 8 * m + 25 ≤ 25 * 2 ^ m := by
  induction m with
  | zero => decide
  | succ m ih =>
      calc
        8 * (m + 1) + 25 ≤ (25 * 2 ^ m) * 2 := by omega
        _ = 25 * 2 ^ (m + 1) := by rw [Nat.pow_succ, Nat.mul_assoc]

theorem one_bank_transport (rootI leafI spentI rootCE leafCE release : Int)
    (hi : rootI = leafI + spentI) (hc : rootCE = leafCE + release) :
    leafI - leafCE = rootI - rootCE - spentI + release := by
  omega

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "profile_tail_bound")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME profile_tail_bound: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND profile_tail_bound: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND profile_tail_bound: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS profile_tail_bound: " dependencies)))
