import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Mathlib.Tactic

theorem a011_same_bank
    (c C0 Ig Ifull bill : ℝ)
    (hC : 0 ≤ C0) (hI : 0 ≤ Ig)
    (hc : c ≤ C0 * Ig)
    (hf : (3 / 4 : ℝ) * Ig ≤ Ifull)
    (hb : bill ≤ (3 / 2 : ℝ) * c + (41 / 4 : ℝ) * Ig) :
    (4 * C0 + 15) * Ifull - bill ≥ ((3 / 2 : ℝ) * C0 + 1) * Ig := by
  have hK : 0 ≤ 4 * C0 + 15 := by positivity
  have hm := mul_le_mul_of_nonneg_left hf hK
  nlinarith

theorem a011_dyadic_polynomial_step (q : ℝ) (hq : 2 ≤ q) :
    (q+1)^2 + 15*(q+1) + 7 ≤ 2*(q^2 + 15*q + 7) := by
  nlinarith [sq_nonneg (q-2)]

theorem a011_js_algebra (u v : ℝ) :
    (u^2-v^2)^2 ≤ 2*(u^2+v^2)*(u-v)^2 := by
  nlinarith [sq_nonneg ((u-v)^2)]

#print axioms a011_same_bank
#print axioms a011_dyadic_polynomial_step
#print axioms a011_js_algebra

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "a011_same_bank")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME a011_same_bank: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a011_same_bank: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND a011_same_bank: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS a011_same_bank: " dependencies)))
