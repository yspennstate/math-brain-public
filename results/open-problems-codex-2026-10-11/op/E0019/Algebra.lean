import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

def ax (x y : Real) : Real := -x-y
def ay (x y : Real) : Real := x-y
def det2 (u v s t : Real) : Real := u*t-v*s

theorem affine_drift_determinant (x y : Real) :
    det2 (ax x y) (ay x y) (ax (x-1) y) (ay (x-1) y) = 2*y := by
  unfold det2 ax ay
  ring

theorem bracket_vector_first : ax (ax 1 0) (ay 1 0) = 0 := by
  norm_num [ax, ay]

theorem bracket_vector_second : ay (ax 1 0) (ay 1 0) = -2 := by
  norm_num [ax, ay]

theorem difference_bracket_rank : det2 (-1) 1 0 (-2) = 2 := by
  norm_num [det2]

theorem controllability_rank : det2 1 0 (-1) 1 = 1 := by
  norm_num [det2]

theorem source_homogeneous_determinant (a y z : Real) :
    det2 (-a*y+z) (-a*z) (-a*y) (-y-a*z) = a*y^2-y*z-a*z^2 := by
  unfold det2
  ring

theorem critical_exponent_algebra (d k l p : Real) :
    d*k*(p-1)-l*p = (d*k-l)*p-d*k := by
  ring
