import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
theorem A015_incidence_ratio (s k : Nat) (h : s <= k) :
    s * (k + 1) <= (s + 1) * k := by
  simpa [Nat.mul_add, Nat.add_mul, Nat.mul_comm] using
    Nat.add_le_add_left h (s * k)

theorem A015_nonempty_owners (a : List Nat)
    (h : forall x, x in a -> 1 <= x) : a.length <= a.sum := by
  induction a with
  | nil => simp
  | cons x xs ih =>
    have hx : 1 <= x := h x (by simp)
    have hs : forall y, y in xs -> 1 <= y := by
      intro y hy
      exact h y (by simp [hy])
    have hi := ih hs
    simpa [List.length_cons, List.sum_cons, Nat.add_comm] using
      Nat.add_le_add hx hi

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "A015_incidence_ratio")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME A015_incidence_ratio: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND A015_incidence_ratio: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND A015_incidence_ratio: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS A015_incidence_ratio: " dependencies)))
