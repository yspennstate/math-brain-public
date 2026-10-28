import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
theorem activation_prime_fiber (a b c : Bool)
    (hb : Bool.xor a b = false) (hc : Bool.xor a c = false) : b = c := by
  cases a
  · cases b
    · cases c
      · rfl
      · cases hc
    · cases hb
  · cases b
    · cases hb
    · cases c
      · cases hc
      · rfl

theorem constant_branch_forces_constant {X Y : Type} (A : X → Bool)
    (B : Y → Bool) (x : X)
    (h : ∀ y, Bool.xor (A x) (B y) = false) : ∀ y z, B y = B z := by
  intro y z
  exact activation_prime_fiber (A x) (B y) (B z) (h y) (h z)

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "constant_branch_forces_constant")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME constant_branch_forces_constant: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND constant_branch_forces_constant: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND constant_branch_forces_constant: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS constant_branch_forces_constant: " dependencies)))
