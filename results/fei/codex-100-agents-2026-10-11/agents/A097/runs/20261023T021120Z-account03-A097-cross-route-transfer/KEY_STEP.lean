import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- Only the nonempty-atom cancellation in DERIVATION section1 is formalized.
-- Positivity/support and the Boolean physical-tree theorem are prose proofs.
theorem canonical_nonempty_cancel (a x q w : ℝ)
    (ha : a ≠ 0) (hq : 1 - q ≠ 0) :
    (1-w) * (a*x) / (a*(1-q)) = (1-w)*x/(1-q) := by
  field_simp [ha, hq] <;> ring

theorem vacuum_complement (a q : ℝ) :
    1 - (1 - a*(1-q)) = a*(1-q) := by
  ring
