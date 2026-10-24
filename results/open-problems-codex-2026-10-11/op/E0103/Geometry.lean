import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Exact endpoint criterion used to count grains spanning [0,L].
theorem spans_closed_interval (a ell L : ℝ) (hL : 0 ≤ L) :
    (∀ x : ℝ, 0 ≤ x → x ≤ L → a ≤ x ∧ x ≤ a + ell) ↔
      (L - ell ≤ a ∧ a ≤ 0) := by
  constructor
  · intro h
    have h0 := h 0 (by linarith) hL
    have h1 := h L hL (by linarith)
    constructor <;> linarith
  · rintro ⟨hleft, hright⟩ x hx0 hxL
    constructor <;> linarith

-- The marked hit sets are disjoint when their initial-position
-- influence intervals are separated by more than twice the radius.
theorem disjoint_influence_intervals (a b x R : ℝ)
    (hsep : 2 * R < b - a)
    (hxa : x ≤ a + R) (hxb : b - R ≤ x) : False := by
  linarith

-- Length of the initial-position set of long grains that intersect
-- but fail to span the target: (ell+L) - (ell-L) = 2L.
theorem nonspanning_length (ell L : ℝ) :
    (ell + L) - (ell - L) = 2 * L := by
  linarith
