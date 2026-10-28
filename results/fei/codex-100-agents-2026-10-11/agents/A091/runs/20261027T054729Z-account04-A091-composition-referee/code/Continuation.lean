import Mathlib.Tactic

theorem a091_feasible_continuation (A I p D q : ℝ)
    (hA : 0 < A) (hJ : 0 < I - p) (hq : q ≤ 1) :
    0 ≤ A * I - D - q * A * (I - p) ↔
      q ≤ min 1 ((A * I - D) / (A * (I - p))) := by
  have hden : 0 < A * (I - p) := mul_pos hA hJ
  constructor
  · intro h
    apply le_min hq
    apply (le_div_iff₀ hden).2
    nlinarith
  · intro h
    have hm := (le_div_iff₀ hden).mp (le_min_iff.mp h).2
    nlinarith

#print axioms a091_feasible_continuation
