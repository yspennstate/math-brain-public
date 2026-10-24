import Mathlib

/-!
F0019 (Zygouras, Question 2): the load-bearing convex-analysis step of the large-beta bound.

If p is convex on [0, ∞) and p(t) ≤ m·t for every t ≥ 0, then every secant slope of p over
[0, ∞) is at most m. Applied to p = f + λ (the annealed-normalised free energy of the directed
polymer, which is convex) with m = the ground-state energy per step (so that p(β) ≤ m β by
bounding the polymer measure's mean energy by the maximal path energy), this gives
p'(β±) ≤ m for every β ≥ 0, hence f'(β±) ≤ m − λ'(β), which is negative once λ'(β) > m.
-/

theorem secant_le_of_convexOn_le_linear (p : ℝ → ℝ) (m : ℝ)
    (hp : ConvexOn ℝ (Set.Ici 0) p) (hle : ∀ t : ℝ, 0 ≤ t → p t ≤ m * t)
    {a b : ℝ} (ha : 0 ≤ a) (hab : a < b) :
    (p b - p a) / (b - a) ≤ m := by
  by_contra hcon
  push_neg at hcon
  set s := (p b - p a) / (b - a) with hs
  have hsm : 0 < s - m := sub_pos.mpr hcon
  set c := m * a - p a with hc
  set t := max (b + 1) (a + 2 * c / (s - m)) with ht
  have htb : b < t := lt_of_lt_of_le (by linarith) (le_max_left _ _)
  have hta : a < t := lt_trans hab htb
  have ht0 : 0 ≤ t := le_trans ha hta.le
  have hb0 : 0 ≤ b := le_trans ha hab.le
  have hsec : (p b - p a) / (b - a) ≤ (p t - p a) / (t - a) :=
    hp.secant_mono (Set.mem_Ici.mpr ha) (Set.mem_Ici.mpr hb0) (Set.mem_Ici.mpr ht0)
      (ne_of_gt hab) (ne_of_gt hta) htb.le
  have hpt : p t ≤ m * t := hle t ht0
  have hpos : 0 < t - a := sub_pos.mpr hta
  have hne : t - a ≠ 0 := hpos.ne'
  have h1 : (p t - p a) / (t - a) ≤ m + c / (t - a) := by
    have h0 : (p t - p a) / (t - a) ≤ (m * t - p a) / (t - a) :=
      div_le_div_of_nonneg_right (by linarith) hpos.le
    have h0' : (m * t - p a) / (t - a) = m + (m * a - p a) / (t - a) := by
      field_simp
      ring
    rw [hc]
    linarith
  have h2 : c / (t - a) ≤ (s - m) / 2 := by
    have hta' : a + 2 * c / (s - m) ≤ t := le_max_right _ _
    have h3' : 2 * c / (s - m) ≤ t - a := by linarith
    have h3 : 2 * c ≤ (t - a) * (s - m) := (div_le_iff₀ hsm).mp h3'
    rw [div_le_iff₀ hpos]
    have h4 : (s - m) / 2 * (t - a) = (t - a) * (s - m) / 2 := by ring
    rw [h4]
    linarith
  have h5 : s ≤ m + (s - m) / 2 := by
    calc s = (p b - p a) / (b - a) := hs
      _ ≤ (p t - p a) / (t - a) := hsec
      _ ≤ m + c / (t - a) := h1
      _ ≤ m + (s - m) / 2 := by linarith
  linarith

#print axioms secant_le_of_convexOn_le_linear
