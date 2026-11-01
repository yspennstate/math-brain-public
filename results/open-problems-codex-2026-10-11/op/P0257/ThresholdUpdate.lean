import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- One direction of the Lipschitz inequality for the threshold update.
theorem threshold_update_lipschitz (hx hy dx dy d t : ℝ)
    (hh : hx ≤ hy + d) (hd : dy ≤ dx + d) :
    max hx (t-dx) ≤ max hy (t-dy) + d := by
  apply max_le
  · linarith [le_max_left hy (t-dy)]
  · linarith [le_max_right hy (t-dy)]

-- New shortcuts cannot violate the old height differences.
theorem shortcut_height_bound (hx hy bx byv d : ℝ)
    (hx0 : 0 ≤ hx) (hy0 : 0 ≤ hy)
    (hxb : hx ≤ bx) (hyb : hy ≤ byv)
    (hxy : hx-hy ≤ d) (hyx : hy-hx ≤ d) :
    hx-hy ≤ min d (bx+byv) ∧ hy-hx ≤ min d (bx+byv) := by
  constructor
  · apply le_min hxy
    linarith
  · apply le_min hyx
    linarith
