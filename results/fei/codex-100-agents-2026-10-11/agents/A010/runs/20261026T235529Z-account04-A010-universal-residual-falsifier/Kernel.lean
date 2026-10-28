import Init

-- Nonempty union forces at least one active mask. The weighted integer
-- numerator of each such tuple dominates its unweighted numerator.
theorem A010_weighted_tuple (k m : Nat) (h : 1 <= k) : m <= k * m :=
  calc
    m = 1 * m := (Nat.one_mul m).symm
    _ <= k * m := Nat.mul_le_mul_right m h

-- This kernel alone does not formalize the sampler, spectral identities,
-- sector assignment or all-parameter entropy estimate.
