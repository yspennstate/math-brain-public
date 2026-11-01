import Mathlib.Tactic

theorem a052_count (K q R cap : ?) (m : ?) (hK : 0 < K) (hq : 0 < q)
    (hm : q * (m : ?) ? R) (hb : K * R < cap) (hc : cap ? K * q) : m = 0 := by
  by_contra h
  have hn : 1 ? m := Nat.one_le_iff_ne_zero.mpr h
  have hr : (1 : ?) ? (m : ?) := by exact_mod_cast hn
  have hR : q ? R := le_trans (le_mul_of_one_le_right (le_of_lt hq) hr) hm
  have hKR := mul_le_mul_of_nonneg_left hR (le_of_lt hK)
  linarith
