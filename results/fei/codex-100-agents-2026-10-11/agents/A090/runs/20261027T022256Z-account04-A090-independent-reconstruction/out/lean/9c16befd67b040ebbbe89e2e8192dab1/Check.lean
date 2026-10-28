import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Mathlib

open scoped BigOperators

/-- Finite active-floor tangent certificate, on positive reference atoms.
Zero-reference/zero-true atoms are handled separately in the prose proof. -/
theorem floor_tangent {n : ℕ} (p x y : Fin n → ℝ) (k : ℝ)
    (hx : ∀ i, 0 < x i)
    (hsum : (∑ i, (y i - x i)) = 0)
    (hactive : ∀ i, p i = k⁻¹ * x i ∨
      (p i ≤ k⁻¹ * x i ∧ x i ≤ y i)) :
    (∑ i, p i * (y i - x i) / x i) ≤ 0 := by
  calc
    (∑ i, p i * (y i - x i) / x i) ≤
        ∑ i, k⁻¹ * (y i - x i) := by
      apply Finset.sum_le_sum
      intro i _
      apply (div_le_iff₀ (hx i)).2
      rcases hactive i with h | ⟨h, hy⟩
      · rw [h]
        ring_nf
      · have hd : 0 ≤ y i - x i := sub_nonneg.mpr hy
        have hmul := mul_le_mul_of_nonneg_right h hd
        nlinarith only [hmul]
    _ = 0 := by rw [← Finset.mul_sum, hsum, mul_zero]

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "floor_tangent")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME floor_tangent: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND floor_tangent: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND floor_tangent: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS floor_tangent: " dependencies)))
