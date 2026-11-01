import Mathlib.Tactic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.Order.Chebyshev
import Mathlib.LinearAlgebra.Matrix.Defs
import Mathlib.Data.Matrix.Mul

/-!
The off-diagonal case of Lemma 5.4 of "Quadratic forms with five large singular values have bounded densities"
(repaired text, sha256 90f859b7): if every `|S_ii| < L/2`, where `L = ‖S‖`, then some partition `[n] = I ⊔ J` has
`‖S_{I,J}‖_F ≥ L/4`.

The paper argues with operator norms (`‖O‖ ≥ ‖S‖ - max |S_ii|` and `‖O‖_F ≥ ‖O‖` for the off-diagonal part `O`). Here
the same bound comes from one eigenvector: if `S v = λ v` with `‖v‖ = 1`, then `(O v)_i = (λ - S_ii) v_i`, so
`‖O‖_F² ≥ ‖O v‖² = ∑_i (λ - S_ii)² v_i² ≥ (|λ| - d)²` whenever `|S_ii| ≤ d ≤ |λ|`; for symmetric `S` one may take
`|λ| = L`.

* `offdiag_row`: `∑_{j ≠ i} S_ij v_j = (λ - S_ii) v_i`.
* `offdiag_sq_ge`: `∑_{i ≠ j} S_ij² ≥ (|λ| - d)²`.
* `count_quarter`: for `i ≠ j`, exactly a quarter of the `2^n` partitions put `i` in `I` and `j` in `J`
  (flipping the label of `i` or of `j` permutes the four classes).
* `sum_over_partitions`: summed over all partitions, `∑_{i ∈ I, j ∈ J} f_ij` totals `2^n/4 · ∑_{i ≠ j} f_ij`.
* `exists_partition`: some partition has `∑_{i ∈ I, j ∈ J} f_ij ≥ (1/4) ∑_{i ≠ j} f_ij`.
* `lemma54_partition`: with `|λ| = L` and `|S_ii| ≤ L/2`, some partition has `‖S_{I,J}‖_F² ≥ L²/16`, i.e.
  `‖S_{I,J}‖_F ≥ L/4` (`lemma54_partition_frob`).
-/

open Finset Matrix

namespace QformFiveB

section Frobenius

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- `∑_j O_ij v_j = (λ - S_ii) v_i` for the off-diagonal part `O` of `S` when `S v = λ v`. -/
theorem offdiag_row (S : Matrix n n ℝ) (v : n → ℝ) (lam : ℝ) (hv : S *ᵥ v = lam • v) (i : n) :
    ∑ j, (if i = j then 0 else S i j) * v j = (lam - S i i) * v i := by
  have hrow : ∑ j, S i j * v j = lam * v i := by
    have := congrFun hv i
    simpa [Matrix.mulVec, dotProduct] using this
  have hsplit : ∑ j, S i j * v j
      = ∑ j, (if i = j then 0 else S i j) * v j + ∑ j, (if i = j then S i j * v j else 0) := by
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun j _ => ?_)
    by_cases h : i = j
    · simp [h]
    · simp [h]
  have hdiag : ∑ j, (if i = j then S i j * v j else 0) = S i i * v i := by
    rw [Finset.sum_ite_eq]
    simp
  linarith [hsplit, hdiag, hrow]

/-- **The off-diagonal Frobenius bound.** If `S v = λ v`, `∑ v_i² = 1` and `|S_ii| ≤ d ≤ |λ|`, then
`∑_{i ≠ j} S_ij² ≥ (|λ| - d)²`. -/
theorem offdiag_sq_ge (S : Matrix n n ℝ) (v : n → ℝ) (lam d : ℝ) (hv : S *ᵥ v = lam • v)
    (hnorm : ∑ i, v i ^ 2 = 1) (hd : ∀ i, |S i i| ≤ d) (hdl : d ≤ |lam|) :
    (|lam| - d) ^ 2 ≤ ∑ i, ∑ j, (if i = j then 0 else S i j ^ 2) := by
  have hcs : ∀ i, ((lam - S i i) * v i) ^ 2 ≤ ∑ j, (if i = j then 0 else S i j ^ 2) := by
    intro i
    rw [← offdiag_row S v lam hv i]
    calc (∑ j, (if i = j then 0 else S i j) * v j) ^ 2
        ≤ (∑ j, (if i = j then 0 else S i j) ^ 2) * ∑ j, v j ^ 2 :=
          Finset.sum_mul_sq_le_sq_mul_sq _ _ _
      _ = ∑ j, (if i = j then 0 else S i j ^ 2) := by
          rw [hnorm, mul_one]
          refine Finset.sum_congr rfl (fun j _ => ?_)
          split_ifs <;> simp
  have hlow : ∀ i, (|lam| - d) ^ 2 * v i ^ 2 ≤ ((lam - S i i) * v i) ^ 2 := by
    intro i
    have h1 : 0 ≤ |lam| - d := by linarith
    have h2 : |lam| - d ≤ |lam - S i i| := by
      have := abs_sub_abs_le_abs_sub lam (S i i)
      linarith [hd i]
    have h3 : (|lam| - d) ^ 2 ≤ (lam - S i i) ^ 2 := by
      rw [← sq_abs (lam - S i i)]
      exact pow_le_pow_left₀ h1 h2 2
    rw [mul_pow]
    exact mul_le_mul_of_nonneg_right h3 (sq_nonneg _)
  calc (|lam| - d) ^ 2 = ∑ i, (|lam| - d) ^ 2 * v i ^ 2 := by
        rw [← Finset.mul_sum, hnorm, mul_one]
    _ ≤ ∑ i, ((lam - S i i) * v i) ^ 2 := Finset.sum_le_sum (fun i _ => hlow i)
    _ ≤ ∑ i, ∑ j, (if i = j then 0 else S i j ^ 2) := Finset.sum_le_sum (fun i _ => hcs i)

end Frobenius

section Partition

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Flip the label of one coordinate. -/
def flip (k : n) (x : n → Bool) : n → Bool := Function.update x k (!x k)

theorem flip_involutive (k : n) : Function.Involutive (flip k) := by
  intro x
  simp only [flip, Function.update_idem, Function.update_self, Bool.not_not, Function.update_eq_self]

/-- The number of labellings with `x i = a` and `x j = b` does not depend on `a`. -/
theorem count_flip_first (i j : n) (hij : i ≠ j) (a b : Bool) :
    (∑ x : n → Bool, if x i = a ∧ x j = b then (1 : ℝ) else 0)
      = ∑ x : n → Bool, if x i = !a ∧ x j = b then (1 : ℝ) else 0 := by
  refine Fintype.sum_equiv (Function.Involutive.toPerm (flip i) (flip_involutive i)) _ _ (fun x => ?_)
  simp only [Function.Involutive.coe_toPerm, flip, Function.update_self,
    Function.update_of_ne (Ne.symm hij)]
  cases x i <;> cases a <;> simp

/-- The number of labellings with `x i = a` and `x j = b` does not depend on `b`. -/
theorem count_flip_second (i j : n) (hij : i ≠ j) (a b : Bool) :
    (∑ x : n → Bool, if x i = a ∧ x j = b then (1 : ℝ) else 0)
      = ∑ x : n → Bool, if x i = a ∧ x j = !b then (1 : ℝ) else 0 := by
  refine Fintype.sum_equiv (Function.Involutive.toPerm (flip j) (flip_involutive j)) _ _ (fun x => ?_)
  simp only [Function.Involutive.coe_toPerm, flip, Function.update_self, Function.update_of_ne hij]
  cases x j <;> cases b <;> simp

/-- **A quarter of the partitions.** For `i ≠ j`, `4 · #{x : x_i = 1, x_j = 0} = 2^n`. -/
theorem count_quarter (i j : n) (hij : i ≠ j) :
    4 * (∑ x : n → Bool, if x i = true ∧ x j = false then (1 : ℝ) else 0)
      = 2 ^ Fintype.card n := by
  set c := ∑ x : n → Bool, if x i = true ∧ x j = false then (1 : ℝ) else 0 with hc
  have h1 : (∑ x : n → Bool, if x i = false ∧ x j = false then (1 : ℝ) else 0) = c := by
    rw [hc, count_flip_first i j hij true false]; rfl
  have h2 : (∑ x : n → Bool, if x i = true ∧ x j = true then (1 : ℝ) else 0) = c := by
    rw [hc, count_flip_second i j hij true false]; rfl
  have h3 : (∑ x : n → Bool, if x i = false ∧ x j = true then (1 : ℝ) else 0) = c := by
    rw [← h1, count_flip_second i j hij false false]; rfl
  have htot : ∑ x : n → Bool, ((if x i = true ∧ x j = false then (1 : ℝ) else 0)
      + (if x i = false ∧ x j = false then (1 : ℝ) else 0)
      + (if x i = true ∧ x j = true then (1 : ℝ) else 0)
      + (if x i = false ∧ x j = true then (1 : ℝ) else 0)) = 2 ^ Fintype.card n := by
    have hone : ∀ x : n → Bool, ((if x i = true ∧ x j = false then (1 : ℝ) else 0)
        + (if x i = false ∧ x j = false then (1 : ℝ) else 0)
        + (if x i = true ∧ x j = true then (1 : ℝ) else 0)
        + (if x i = false ∧ x j = true then (1 : ℝ) else 0)) = 1 := by
      intro x
      cases x i <;> cases x j <;> simp
    rw [Finset.sum_congr rfl (fun x _ => hone x), Finset.sum_const, Finset.card_univ, Fintype.card_pi,
      Finset.prod_const, Finset.card_univ, Fintype.card_bool, nsmul_eq_mul, mul_one]
    push_cast
    ring
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.sum_add_distrib, h1, h2, h3] at htot
  linarith

/-- Summed over all partitions, the mass `∑_{i ∈ I, j ∈ J} f_ij` totals `2^n/4 · ∑_{i ≠ j} f_ij`. -/
theorem sum_over_partitions (f : n → n → ℝ) :
    ∑ x : n → Bool, ∑ i, ∑ j, (if x i = true ∧ x j = false then f i j else 0)
      = 2 ^ Fintype.card n / 4 * ∑ i, ∑ j, (if i = j then 0 else f i j) := by
  rw [Finset.sum_comm, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [Finset.sum_comm, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  by_cases hij : i = j
  · subst hij
    simp
  · have hq := count_quarter i j hij
    have hsplit : ∀ x : n → Bool, (if x i = true ∧ x j = false then f i j else 0)
        = f i j * (if x i = true ∧ x j = false then (1 : ℝ) else 0) := by
      intro x
      split_ifs <;> simp
    rw [Finset.sum_congr rfl (fun x _ => hsplit x), ← Finset.mul_sum, if_neg hij, ← hq]
    ring

/-- **Some partition carries a quarter of the off-diagonal mass.** -/
theorem exists_partition (f : n → n → ℝ) :
    ∃ x : n → Bool, (1 / 4) * ∑ i, ∑ j, (if i = j then 0 else f i j)
      ≤ ∑ i, ∑ j, (if x i = true ∧ x j = false then f i j else 0) := by
  by_contra h
  push Not at h
  have hlt := Finset.sum_lt_sum_of_nonempty (s := (univ : Finset (n → Bool))) univ_nonempty
    (fun x _ => h x)
  rw [sum_over_partitions, Finset.sum_const, Finset.card_univ, Fintype.card_pi, Finset.prod_const,
    Finset.card_univ, Fintype.card_bool, nsmul_eq_mul] at hlt
  push_cast at hlt
  linarith

/-- **Lemma 5.4, the partition step.** If `S v = λ v` with `∑ v_i² = 1`, `|λ| = L` and `|S_ii| ≤ L/2` for all `i`, some
partition `x` has `∑_{i ∈ I, j ∈ J} S_ij² ≥ L²/16`. -/
theorem lemma54_partition (S : Matrix n n ℝ) (v : n → ℝ) (lam L : ℝ) (hv : S *ᵥ v = lam • v)
    (hnorm : ∑ i, v i ^ 2 = 1) (hL : |lam| = L) (hd : ∀ i, |S i i| ≤ L / 2) :
    ∃ x : n → Bool, L ^ 2 / 16 ≤ ∑ i, ∑ j, (if x i = true ∧ x j = false then S i j ^ 2 else 0) := by
  have hL0 : 0 ≤ L := by rw [← hL]; exact abs_nonneg _
  have hoff := offdiag_sq_ge S v lam (L / 2) hv hnorm hd (by rw [hL]; linarith)
  rw [hL] at hoff
  obtain ⟨x, hx⟩ := exists_partition (fun i j => S i j ^ 2)
  refine ⟨x, ?_⟩
  have e : (L - L / 2) ^ 2 = L ^ 2 / 4 := by ring
  rw [e] at hoff
  simp only at hx
  linarith

/-- The same in Frobenius-norm form: `‖S_{I,J}‖_F ≥ L/4`. -/
theorem lemma54_partition_frob (S : Matrix n n ℝ) (v : n → ℝ) (lam L : ℝ) (hv : S *ᵥ v = lam • v)
    (hnorm : ∑ i, v i ^ 2 = 1) (hL : |lam| = L) (hd : ∀ i, |S i i| ≤ L / 2) :
    ∃ x : n → Bool, L / 4 ≤ Real.sqrt (∑ i, ∑ j, (if x i = true ∧ x j = false then S i j ^ 2 else 0)) := by
  obtain ⟨x, hx⟩ := lemma54_partition S v lam L hv hnorm hL hd
  refine ⟨x, ?_⟩
  have hL0 : 0 ≤ L := by rw [← hL]; exact abs_nonneg _
  rw [show L / 4 = Real.sqrt ((L / 4) ^ 2) by rw [Real.sqrt_sq (by linarith)]]
  exact Real.sqrt_le_sqrt (by nlinarith [hx])

end Partition

end QformFiveB
