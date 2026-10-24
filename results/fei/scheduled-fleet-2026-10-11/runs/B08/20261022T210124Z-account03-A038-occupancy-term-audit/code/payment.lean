import Mathlib

-- Source-side eligibility is not a second owner. The information quantities and
-- all Boolean/Fourier hypotheses are supplied separately in ANALYTIC_PROOF.md.
example (A D R S Sroot : ℝ) (h : S - D + 4*R = Sroot) :
    S - (A + max (D-4*R) 0) = min (S-A) (Sroot-A) := by
  simp only [max_def, min_def]
  split_ifs <;> linarith

example (A S Sroot : ℝ) (ha : A < 53/32) (hs : 2 ≤ S)
    (hr : 2 ≤ Sroot) :
    11/32 < S - (A + max (S-Sroot) 0) := by
  simp only [max_def]
  split_ifs <;> linarith
