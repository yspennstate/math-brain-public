import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Mathlib.Tactic

theorem fallback_variance_ownership (p n z : ℝ)
    (hp : 0 ≤ p) (hp' : p ≤ 1) (hn : -1 ≤ n) (hn' : n ≤ 1) :
    (1-p)*(1-z^2) ≤ 1-(p*n+(1-p)*z)^2 := by
  have hv : 0 ≤ 1-n^2 := by nlinarith
  have ht : 0 ≤ p*(1-n^2) := mul_nonneg hp hv
  have hs : 0 ≤ p*(1-p)*(n-z)^2 :=
    mul_nonneg (mul_nonneg hp (by linarith)) (sq_nonneg (n-z))
  have he : 1-(p*n+(1-p)*z)^2-(1-p)*(1-z^2) =
      p*(1-n^2)+p*(1-p)*(n-z)^2 := by ring
  linarith

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "fallback_variance_ownership")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME fallback_variance_ownership: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND fallback_variance_ownership: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND fallback_variance_ownership: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS fallback_variance_ownership: " dependencies)))
