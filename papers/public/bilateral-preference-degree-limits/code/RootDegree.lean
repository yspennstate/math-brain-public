import Mathlib.Data.Nat.Choose.Central
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum.NatFactorial

/-!
Exact identities used in the paper on the root degree of the bilateral preference graph.

* `beta_constant`: `C(a+b, a) a! b! / (a+b+1)! = 1/(a+b+1)`. With `a = k-1` and `b = n-k-2` this is
  `C(n-3, k-1) B(k, n-k-1) = 1/(n-2)`, the constant in the covariance lemma.
* `central_identity`, `mean_constants_agree`: for every `m`, with `k = m+1`,
  `k C(2k,k)/4^k = (2k-1) C(2k-2,k-1)/2^(2k-1)`. The left side is the limiting mean `mu_k` of the
  unreciprocated count when `n-1-k = k` is fixed, the right side the constant `c_k` in the fixed-`k`
  mean degree of Dabirian and Subramanian.
* `mu_small`, `mu_closed_small`: the gamma-moment sum for `mu_r` and the closed form `r C(2r,r)/4^r`
  agree for `r = 1, ..., 6`.
* `M2_small`, `values_small`: the second moment `M_{2,r}`, the variance `nu_r = mu_r + M_{2,r} - mu_r^2`
  and the squared upper endpoint `mu_r^2/nu_r` of the standardized limit for `r = 1, 2`.
-/

namespace RootDegree

open Nat

theorem beta_constant (a b : ℕ) :
    (Nat.choose (a + b) a : ℚ) * (a ! : ℚ) * (b ! : ℚ) / ((a + b + 1)! : ℚ) = 1 / ((a : ℚ) + b + 1) := by
  have h : (Nat.choose (a + b) a : ℚ) * (a ! : ℚ) * (b ! : ℚ) = ((a + b)! : ℚ) := by
    have := Nat.choose_mul_factorial_mul_factorial (Nat.le_add_right a b)
    rw [Nat.add_sub_cancel_left] at this
    exact_mod_cast this
  have h1 : ((a + b)! : ℚ) ≠ 0 := by exact_mod_cast (Nat.factorial_pos (a + b)).ne'
  have h2 : (a : ℚ) + b + 1 ≠ 0 := by positivity
  rw [h, Nat.factorial_succ]
  push_cast
  field_simp

theorem central_identity (m : ℕ) :
    (m + 1) * Nat.choose (2 * (m + 1)) (m + 1) = 2 * (2 * m + 1) * Nat.choose (2 * m) m := by
  have h := Nat.succ_mul_centralBinom_succ m
  rwa [Nat.centralBinom_eq_two_mul_choose, Nat.centralBinom_eq_two_mul_choose] at h

theorem mean_constants_agree (m : ℕ) :
    ((m : ℚ) + 1) * (Nat.choose (2 * (m + 1)) (m + 1) : ℚ) / 4 ^ (m + 1)
      = (2 * (m : ℚ) + 1) * (Nat.choose (2 * m) m : ℚ) / 2 ^ (2 * m + 1) := by
  have h : ((m : ℚ) + 1) * (Nat.choose (2 * (m + 1)) (m + 1) : ℚ)
      = 2 * (2 * (m : ℚ) + 1) * (Nat.choose (2 * m) m : ℚ) := by
    exact_mod_cast central_identity m
  have h4 : (4 : ℚ) ^ (m + 1) = 2 * 2 ^ (2 * m + 1) := by
    rw [show (4 : ℚ) = 2 ^ 2 by norm_num, ← pow_mul, show 2 * (m + 1) = (2 * m + 1) + 1 by ring, pow_succ]
    ring
  rw [h, h4]
  field_simp

/-- The gamma-moment sum: `mu_r = sum_{l<r} (r-l) (r-1+l)! / (l! (r-1)! 2^(r+l))`. -/
def muSum (r : ℕ) : ℚ :=
  ∑ l ∈ Finset.range r, ((r - l : ℕ) : ℚ) * ((r - 1 + l)! : ℚ) / ((l ! : ℚ) * ((r - 1)! : ℚ) * 2 ^ (r + l))

/-- The closed form `r C(2r, r) / 4^r`. -/
def muClosed (r : ℕ) : ℚ := r * (Nat.centralBinom r : ℚ) / 4 ^ r

/-- The second moment `M_{2,r} = E Lambda_r(A_r)^2`. -/
def M2 (r : ℕ) : ℚ :=
  (∑ l ∈ Finset.range r, ∑ m ∈ Finset.range r,
      ((r - l : ℕ) : ℚ) * ((r - m : ℕ) : ℚ) * ((r + l + m - 1)! : ℚ) / ((l ! : ℚ) * (m ! : ℚ) * 3 ^ (r + l + m)))
    / ((r - 1)! : ℚ)

theorem centralBinom_small :
    Nat.centralBinom 1 = 2 ∧ Nat.centralBinom 2 = 6 ∧ Nat.centralBinom 3 = 20 ∧
      Nat.centralBinom 4 = 70 ∧ Nat.centralBinom 5 = 252 ∧ Nat.centralBinom 6 = 924 := by
  decide

theorem mu_small :
    muSum 1 = 1 / 2 ∧ muSum 2 = 3 / 4 ∧ muSum 3 = 15 / 16 ∧ muSum 4 = 35 / 32 ∧
      muSum 5 = 315 / 256 ∧ muSum 6 = 693 / 512 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp only [muSum, Finset.sum_range_succ, Finset.sum_range_zero] <;> norm_num [Nat.factorial]

theorem mu_closed_small :
    muClosed 1 = 1 / 2 ∧ muClosed 2 = 3 / 4 ∧ muClosed 3 = 15 / 16 ∧ muClosed 4 = 35 / 32 ∧
      muClosed 5 = 315 / 256 ∧ muClosed 6 = 693 / 512 := by
  obtain ⟨c1, c2, c3, c4, c5, c6⟩ := centralBinom_small
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> simp only [muClosed, c1, c2, c3, c4, c5, c6] <;> norm_num

theorem M2_small : M2 1 = 1 / 3 ∧ M2 2 = 22 / 27 := by
  refine ⟨?_, ?_⟩ <;>
    simp only [M2, Finset.sum_range_succ, Finset.sum_range_zero] <;> norm_num [Nat.factorial]

theorem values_small :
    muSum 1 + M2 1 - muSum 1 ^ 2 = 7 / 12 ∧
      muSum 1 ^ 2 / (muSum 1 + M2 1 - muSum 1 ^ 2) = 3 / 7 ∧
      muSum 2 + M2 2 - muSum 2 ^ 2 = 433 / 432 ∧
      muSum 2 ^ 2 / (muSum 2 + M2 2 - muSum 2 ^ 2) = 243 / 433 := by
  obtain ⟨h1, h2, -, -, -, -⟩ := mu_small
  obtain ⟨k1, k2⟩ := M2_small
  rw [h1, h2, k1, k2]
  norm_num

end RootDegree

#print axioms RootDegree.beta_constant
#print axioms RootDegree.central_identity
#print axioms RootDegree.mean_constants_agree
#print axioms RootDegree.centralBinom_small
#print axioms RootDegree.mu_small
#print axioms RootDegree.mu_closed_small
#print axioms RootDegree.M2_small
#print axioms RootDegree.values_small
