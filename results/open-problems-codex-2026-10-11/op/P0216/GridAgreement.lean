import Lean.Elab.Tactic.Omega

/- A deterministic part of the grid proof. An order-reflecting embedding
   on distinct bins has the same strict comparisons in both samples.
   No probability or asymptotic claim is formalized here. -/
theorem compare_of_distinct_bins
    (r s x y u v : Nat) (hne : r ≠ s)
    (hxy : r < s → x < y) (hyx : s < r → y < x)
    (huv : r < s → u < v) (hvu : s < r → v < u) :
    (x < y ↔ u < v) := by
  by_cases h : r < s
  · constructor
    · intro _; exact huv h
    · intro _; exact hxy h
  · have h' : s < r := by omega
    have hy := hyx h'
    have hv := hvu h'
    constructor <;> intro hbad <;> omega

theorem induced_order_agreement
    (x y u v x' y' u' v' : Nat)
    (hx : x < y ↔ u < v) (hy : x' < y' ↔ u' < v') :
    ((x < y ∧ x' < y') ↔ (u < v ∧ u' < v')) := by
  constructor
  · intro h
    exact ⟨hx.mp h.1, hy.mp h.2⟩
  · intro h
    exact ⟨hx.mpr h.1, hy.mpr h.2⟩
