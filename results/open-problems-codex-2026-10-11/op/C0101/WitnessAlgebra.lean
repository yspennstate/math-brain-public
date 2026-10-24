import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/- These lemmas check the algebra used in ATTEMPT.md, not the infinite-lattice
   least-action or classification arguments. No sorry and no native_decide. -/

def binomQuad (a x : ℚ) : ℚ := a * x * (x - 1) / 2

theorem binom_second_difference (a x : ℚ) :
    binomQuad a (x + 1) + binomQuad a (x - 1) - 2 * binomQuad a x = a := by
  unfold binomQuad
  ring

theorem mixed_second_difference (a x y : ℚ) :
    a * (x + 1) * y + a * (x - 1) * y - 2 * (a * x * y) = 0 := by
  ring

def witness3 (a b c u v w x y z : ℚ) : ℚ :=
  binomQuad a x + binomQuad b y + binomQuad c z +
  u*x*y + v*x*z + w*y*z

theorem witness3_laplacian (a b c u v w x y z : ℚ) :
    witness3 a b c u v w (x+1) y z +
    witness3 a b c u v w (x-1) y z +
    witness3 a b c u v w x (y+1) z +
    witness3 a b c u v w x (y-1) z +
    witness3 a b c u v w x y (z+1) +
    witness3 a b c u v w x y (z-1) -
    6 * witness3 a b c u v w x y z = a+b+c := by
  unfold witness3 binomQuad
  ring

theorem witness3_linear_error (a b c u v w x y z : ℚ) :
    witness3 a b c u v w x y z =
    (a*x*x+b*y*y+c*z*z+2*u*x*y+2*v*x*z+2*w*y*z)/2 -
    (a*x+b*y+c*z)/2 := by
  unfold witness3 binomQuad
  ring

theorem zero_diagonal_psd_entry (u : ℚ)
    (hplus : 0 ≤ 2*u) (hminus : 0 ≤ -2*u) : u = 0 := by
  linarith
