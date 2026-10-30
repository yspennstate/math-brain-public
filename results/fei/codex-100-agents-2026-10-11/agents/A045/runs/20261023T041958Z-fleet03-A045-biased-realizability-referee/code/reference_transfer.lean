import Mathlib

-- UNCOMPILED: formal compute admission refused; not a certificate.
-- Scalar kernel after the two KL bounds have been proved mathematically.
example (kf kt af at : ℝ) (hf : 0 ≤ kf) (ht : 0 ≤ kt)
    (hfb : kf ≤ af) (htb : kt ≤ at) : -af ≤ kt-kf ∧ kt-kf ≤ at := by
  constructor <;> linarith
