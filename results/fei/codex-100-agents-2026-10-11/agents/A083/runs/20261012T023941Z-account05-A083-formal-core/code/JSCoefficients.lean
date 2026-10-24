import Init.Data.Rat.Lemmas

namespace FEIJS

-- The normalized central-binomial coefficient is oddProduct/evenProduct.
def oddProduct : Nat → Nat
  | 0 => 1
  | n+1 => (2*n+1) * oddProduct n

def evenProduct : Nat → Nat
  | 0 => 1
  | n+1 => (2*n+2) * evenProduct n

def factorial : Nat → Nat
  | 0 => 1
  | n+1 => (n+1) * factorial n

theorem factorial_split (n : Nat) : factorial (2*n) = oddProduct n * evenProduct n := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [show 2*(n+1) = (2*n+1)+1 by omega]
    simp only [factorial, oddProduct, evenProduct, ih]
    have hi : 2*n+1+1 = 2*n+2 := by omega
    rw [hi]
    simp only [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

theorem even_factorial (n : Nat) : evenProduct n = 2^n * factorial n := by
  induction n with
  | zero => decide
  | succ n ih =>
    simp only [evenProduct, factorial, ih, Nat.pow_succ]
    rw [show 2*n+2 = 2*(n+1) by omega]
    simp only [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

theorem odd_pos (n : Nat) : 0 < oddProduct n := by
  induction n with
  | zero => decide
  | succ n ih =>
    exact Nat.mul_pos (by omega) ih

theorem even_pos (n : Nat) : 0 < evenProduct n := by
  induction n with
  | zero => decide
  | succ n ih =>
    exact Nat.mul_pos (by omega) ih

theorem coefficient_cross_comparison (n : Nat) (hn : 1 ≤ n) :
    evenProduct n ≤ (2*n) * oddProduct n := by
  induction n with
  | zero => omega
  | succ n ih =>
    cases n with
    | zero => decide
    | succ m =>
      have h := ih (by omega)
      have step := Nat.mul_le_mul_left (2*(m+1)+2) h
      have lift := Nat.mul_le_mul_left (2*(m+1)+2)
        (Nat.mul_le_mul_right (oddProduct (m+1)) (show 2*(m+1) ≤ 2*(m+1)+1 by omega))
      change (2*(m+1)+2) * evenProduct (m+1) ≤
        (2*(m+1+1)) * ((2*(m+1)+1) * oddProduct (m+1))
      rw [show 2*(m+1+1) = 2*(m+1)+2 by omega]
      exact Nat.le_trans step (by simpa only [Nat.mul_assoc] using lift)

theorem rational_normalized_coefficient (n : Nat) (hn : 1 ≤ n) :
    (1 : Rat) / (2*n : Nat) ≤ (oddProduct n : Rat) / (evenProduct n : Rat) := by
  have ht : 0 < (2*n : Nat) := by omega
  have htq : 0 < ((2*n : Nat) : Rat) := Rat.natCast_pos.mpr ht
  have heq : 0 < (evenProduct n : Rat) := Rat.natCast_pos.mpr (even_pos n)
  have bound : (evenProduct n : Rat) ≤ ((2*n : Nat) : Rat) * (oddProduct n : Rat) := by
    simpa only [Rat.natCast_mul] using
      (Rat.natCast_le_natCast.mpr (coefficient_cross_comparison n hn))
  have h := Rat.mul_le_mul_of_nonneg_right bound
    (Rat.le_of_lt (Rat.inv_pos.mpr htq))
  have cancel : (((2*n : Nat) : Rat) * (oddProduct n : Rat)) *
      ((2*n : Nat) : Rat)⁻¹ = (oddProduct n : Rat) := by
    rw [Rat.mul_comm ((2*n : Nat) : Rat) (oddProduct n : Rat),
      Rat.mul_assoc, Rat.mul_inv_cancel _ (Rat.ne_of_gt htq), Rat.mul_one]
  rw [cancel] at h
  apply Rat.le_of_mul_le_mul_right (c := (evenProduct n : Rat)) _ heq
  rw [Rat.div_mul_cancel (Rat.ne_of_gt heq)]
  simpa only [Rat.div_def, Rat.one_mul, Rat.mul_one, Rat.mul_comm] using h

theorem scalar_series_coefficient (n : Nat) (hn : 1 ≤ n) :
    ((1 : Rat) / (2*n : Nat)) / (2*n-1 : Nat) ≤
      ((oddProduct n : Rat) / (evenProduct n : Rat)) / (2*n-1 : Nat) := by
  have hd : 0 < (2*n-1 : Nat) := by omega
  change ((1 : Rat) / (2*n : Nat)) * ((2*n-1 : Nat) : Rat)⁻¹ ≤
    ((oddProduct n : Rat) / (evenProduct n : Rat)) * ((2*n-1 : Nat) : Rat)⁻¹
  exact Rat.mul_le_mul_of_nonneg_right
    (rational_normalized_coefficient n hn)
    (Rat.le_of_lt (Rat.inv_pos.mpr (Rat.natCast_pos.mpr hd)))

#print axioms coefficient_cross_comparison
#print axioms rational_normalized_coefficient
#print axioms scalar_series_coefficient
#print axioms factorial_split
#print axioms even_factorial

def entropyPartial (t : Rat) : Nat → Rat
  | 0 => 0
  | n+1 => entropyPartial t n +
    (((1 : Rat) / (2*(n+1) : Nat)) / (2*(n+1)-1 : Nat)) * t^(n+1)

def sqrtPartial (t : Rat) : Nat → Rat
  | 0 => 0
  | n+1 => sqrtPartial t n +
    (((oddProduct (n+1) : Rat) / (evenProduct (n+1) : Rat)) /
      (2*(n+1)-1 : Nat)) * t^(n+1)

theorem all_partial_sums (t : Rat) (ht : 0 ≤ t) (N : Nat) :
    entropyPartial t N ≤ sqrtPartial t N := by
  induction N with
  | zero => exact Rat.le_refl
  | succ n ih =>
    have hterm := Rat.mul_le_mul_of_nonneg_right (c := t^(n+1))
      (scalar_series_coefficient (n+1) (by omega)) (Rat.pow_nonneg (n := n+1) ht)
    exact Rat.le_trans (Rat.add_le_add_right.mpr ih) (Rat.add_le_add_left.mpr hterm)

#print axioms all_partial_sums
end FEIJS
