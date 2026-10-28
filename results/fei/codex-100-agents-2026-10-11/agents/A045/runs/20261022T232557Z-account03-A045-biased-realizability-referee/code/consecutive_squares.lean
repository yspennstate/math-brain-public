import Mathlib

-- UNCOMPILED: compute admission refused the formal run; this is not a certificate.
example (a b n : ℤ) (ha : 1 ≤ a) (hb : 0 ≤ b)
    (hlo : (a - 1) * (a - 1) < n) (hhi : n < a * a) : b * b ≠ n := by
  intro heq
  by_cases hba : b < a
  · have hle : b ≤ a - 1 := by omega
    have hprod := mul_nonneg (sub_nonneg.mpr hle)
      (show 0 ≤ a - 1 + b by omega)
    nlinarith
  · have hge : a ≤ b := by omega
    have hprod := mul_nonneg (sub_nonneg.mpr hge)
      (show 0 ≤ b + a by omega)
    nlinarith
