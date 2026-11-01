import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

-- The finite-memory-4 branch polynomial from the exact orbit matrix.
def memoryFourPolynomial (x l : ℚ) : ℚ :=
  l^3 + (2*x-1)*l^2 + (2*x^2-x)*l - x^3

-- At x=0 the root l=1 is simple: the remaining factor is nonzero there.
theorem memoryFourAtZero (t : ℚ) :
    memoryFourPolynomial 0 (1+t) = t*(1+t)^2 := by
  unfold memoryFourPolynomial
  ring

theorem simpleRootFactor : (1 + (0 : ℚ))^2 = 1 := by
  norm_num

-- Exact residual of the first four terms; divisible by x^5.
theorem memoryFourResidual (x : ℚ) :
    memoryFourPolynomial x (1-x-x^2+x^3) =
      x^5*(x^4-3*x^3+2*x^2+3*x-4) := by
  unfold memoryFourPolynomial
  ring

-- A positive diagonal return count is outweighed by other lengths.
theorem pairedReturnCancellation :
    (945 : ℤ) - 12*105 + 8*15 = -195 := by
  norm_num
