import Mathlib.Tactic

theorem interaction_bank_drop
    (r t b iw ih d iw0 iw1 : ℝ)
    (hw : iw = d + (iw0 + iw1) / 2) :
    5 * (r * (1-r) * iw + t * (1-t) * ih) -
    (5 * (r * (1-r) * iw0 + (t+b/2) * (1-(t+b/2)) * ih) +
     5 * (r * (1-r) * iw1 + (t-b/2) * (1-(t-b/2)) * ih)) / 2 =
    5 * (r * (1-r) * d + b^2 * ih / 4) := by
  rw [hw]
  ring
