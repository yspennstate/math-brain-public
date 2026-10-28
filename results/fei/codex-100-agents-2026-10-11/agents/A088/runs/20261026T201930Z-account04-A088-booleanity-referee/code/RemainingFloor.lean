import Mathlib.Tactic
-- Formalized scalar substep only. Not compiled: known Mathlib memory exceeds this stage cap.
theorem remaining_floor (m d : ?) (hm : 4 ? m) (hd : m*d ? 1/64) :
    39/32 ? 2*m - 13/2 - 18*m*d := by
  nlinarith
theorem conditional_ratio_floor : (131:?)/49 < 4 := by norm_num
