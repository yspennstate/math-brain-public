import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Squared denominator comparison: no probability assertions are formalized.
theorem no_cancellation_denominator (r s u v : Real)
    (hr : 0 <= r) (hs : 0 <= s) (hp : 0 <= u*v) :
    (1+r)^2+u^2 <= (1+r+s)^2+(u+v)^2 := by
  have hrs : 0 <= r*s := mul_nonneg hr hs
  nlinarith only [hs, hp, hrs, sq_nonneg s, sq_nonneg v]

-- Positive-part control used by clipping the sum imaginary part.
theorem clipped_excess_control (i g h G R : Real)
    (hi : i=g+h) (hg : abs g <= G) (hh : abs h <= R) (hR : 0 <= R) :
    max (abs i-G) 0 <= R := by
  apply max_le
  . have ht : abs i <= abs g + abs h := by
      rw [hi]
      exact abs_add_le g h
    linarith only [ht, hg, hh]
  . exact hR

-- Exact algebraic certificate underlying the Hellinger split:
-- for t = sqrt(1+k)-1, k=t^2+2t.
theorem small_hellinger_bound (k t : Real)
    (hk : 0 <= k) (hk1 : k <= 1) (ht : 0 <= t)
    (hid : k=t^2+2*t) : k^2 <= 6*t^2 := by
  have ht1 : t <= 1 := by nlinarith only [hk1, hid, sq_nonneg t]
  have ht2 : t^2 <= 1 := by nlinarith only [ht, ht1]
  have hsq : (t+2)^2 <= 6 := by nlinarith only [hk1, hid, ht1]
  have hm := mul_nonneg (sq_nonneg t) (sub_nonneg.mpr hsq)
  nlinarith only [hid, hm]

#print axioms no_cancellation_denominator
#print axioms clipped_excess_control
#print axioms small_hellinger_bound
