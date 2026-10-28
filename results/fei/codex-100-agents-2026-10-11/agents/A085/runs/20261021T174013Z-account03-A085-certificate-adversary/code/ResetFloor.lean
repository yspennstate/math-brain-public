import Std

-- Integer-scaled final inequality only. Analytic logarithm bounds are not formalized here.
theorem reset_floor (scale q gain : Int)
    (hq : 8 * q <= scale) (hg : gain <= 2 * q) :
    3 * scale <= 4 * (scale - gain) := by
  omega

#print axioms reset_floor
