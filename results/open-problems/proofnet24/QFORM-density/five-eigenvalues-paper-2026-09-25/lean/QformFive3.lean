import Mathlib.Tactic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.Order.Chebyshev
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.DotProduct
import Mathlib.Data.Matrix.Block
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Real.StarOrdered

/-!
Formal check of Proposition 6.4 of "Quadratic forms with five large eigenvalues have bounded densities",
from the spectral hypothesis to the crossing volume.

The first part repeats QformFive2.lean (Lemma 6.2(a), Lemma 6.3 and the averaging step of the random sign
argument) so that this file compiles on its own.

The second part proves the facts of Lemma 2.5 that the proposition uses, for approximation numbers:
`ApproxGE k σ T` says that every matrix of rank less than `k` is at operator distance at least `σ` from `T`,
which is `s_k(T) ≥ σ` by the characterization `s_k(T) = min {‖T - B‖ : rank B < k}` in the proof of Lemma 2.5.
It proves the compression inequality (`approx_compress`), the Weyl step (`compressed_lower`) and the
inequality `s_m(A_{I,J}) ≥ s_{2m-1}(C)` of Lemma 6.2(b) (`approx_of_dil`), and assembles the proposition for a
symmetric `A` given `2m - 1` orthonormal eigenvectors (`prop64`, `prop64_m3`, `prop64_m2`, `prop64_m1`).

The third part joins both ends to Mathlib's spectral theorem: `k` eigenvalues of modulus at least one give `k`
orthonormal eigenvectors (`eigenframe`), and `s_m(M) ≥ σ` in the approximation-number form gives at least `m`
eigenvalues of `M Mᵀ` that are at least `σ²`, hence `E_m(M) = e_m(M Mᵀ) ≥ σ^{2m}` (`card_eig_of_approx`,
`evol_of_approx`). The theorems `prop64_spectral_m3`, `prop64_spectral_m2` and `prop64_spectral_m1` are
Proposition 6.4 with the paper's definitions and constants: a real symmetric `A` without a pivot and with
`N_A(1) ≥ 2m - 1` has a partition `[n] = I ⊔ J` with `E_m(A_{I,J}) ≥ γ^{2m}`, where `γ = 0.09, 0.237, 0.38`
for `m = 3, 2, 1`.
-/

open Finset BigOperators

namespace QformFive

/-- The sign attached to a Boolean. -/
def sgn (b : Bool) : ℝ := if b then 1 else -1

/-! ## Lemma 6.2(a) -/

/-- Lemma 6.2(a), entrywise: a - eps_i eps_j a is 0 when the signs agree and 2a otherwise. -/
theorem sign_identity (a : ℝ) (b c : Bool) :
    a - sgn b * sgn c * a = 2 * (if b = c then 0 else a) := by
  cases b <;> cases c <;> simp [sgn] <;> ring

/-- Lemma 6.2(a), matrix form: A - D A D = 2 C with D = diag(sgn x) and C the off-diagonal block part. -/
theorem sign_identity_matrix {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (x : Fin n → Bool) :
    A - Matrix.diagonal (fun i => sgn (x i)) * A * Matrix.diagonal (fun i => sgn (x i))
      = (2 : ℝ) • Matrix.of (fun i j => if x i = x j then 0 else A i j) := by
  ext i j
  simp only [Matrix.sub_apply, Matrix.mul_diagonal, Matrix.diagonal_mul, Matrix.smul_apply,
    Matrix.of_apply, smul_eq_mul]
  rw [← sign_identity (A i j) (x i) (x j)]
  ring

/-! ## Moments of independent signs -/

/-- Product formula: summing a product of one-coordinate factors over all sign vectors factorizes. -/
theorem sum_prod_bool {n : ℕ} (f : Fin n → Bool → ℝ) :
    ∑ x : Fin n → Bool, ∏ r, f r (x r) = ∏ r, (f r true + f r false) := by
  rw [← Fintype.prod_sum (fun r b => f r b)]
  refine Finset.prod_congr rfl (fun r _ => ?_)
  simp [Fintype.sum_bool]

/-- The exponent of coordinate r in the product sgn(x i) sgn(x j) sgn(x p) sgn(x q). -/
def mult {n : ℕ} (i j p q r : Fin n) : ℕ :=
  (if i = r then 1 else 0) + (if j = r then 1 else 0) + (if p = r then 1 else 0) + (if q = r then 1 else 0)

theorem prod_mult {n : ℕ} (x : Fin n → Bool) (i j p q : Fin n) :
    ∏ r, sgn (x r) ^ (mult i j p q r) = sgn (x i) * sgn (x j) * sgn (x p) * sgn (x q) := by
  simp only [mult, pow_add, Finset.prod_mul_distrib, Finset.prod_pow_boole, Finset.mem_univ, if_true]

/-- The fourth moment of independent signs: for i ≠ j and p ≠ q, the sum over all 2^n sign vectors of
sgn(x i) sgn(x j) sgn(x p) sgn(x q) is 2^n when {p,q} = {i,j} and 0 otherwise. -/
theorem fourth_moment {n : ℕ} (i j p q : Fin n) (hij : i ≠ j) (hpq : p ≠ q) :
    ∑ x : Fin n → Bool, sgn (x i) * sgn (x j) * sgn (x p) * sgn (x q)
      = if (p = i ∧ q = j) ∨ (p = j ∧ q = i) then (2:ℝ) ^ n else 0 := by
  have hsum : ∑ x : Fin n → Bool, sgn (x i) * sgn (x j) * sgn (x p) * sgn (x q)
      = ∏ r, (1 + (-1 : ℝ) ^ (mult i j p q r)) := by
    calc ∑ x : Fin n → Bool, sgn (x i) * sgn (x j) * sgn (x p) * sgn (x q)
        = ∑ x : Fin n → Bool, ∏ r, sgn (x r) ^ (mult i j p q r) := by
          refine Finset.sum_congr rfl (fun x _ => ?_); rw [prod_mult]
      _ = ∏ r, (sgn true ^ (mult i j p q r) + sgn false ^ (mult i j p q r)) :=
          sum_prod_bool (fun r b => sgn b ^ (mult i j p q r))
      _ = ∏ r, (1 + (-1 : ℝ) ^ (mult i j p q r)) := by
          refine Finset.prod_congr rfl (fun r _ => ?_); simp [sgn]
  rw [hsum]
  by_cases h : (p = i ∧ q = j) ∨ (p = j ∧ q = i)
  · rw [if_pos h]
    have h2 : ∀ r, (1 + (-1 : ℝ) ^ (mult i j p q r)) = 2 := by
      intro r
      have he : mult i j p q r = 2 * ((if i = r then 1 else 0) + (if j = r then 1 else 0)) := by
        rcases h with ⟨hp, hq⟩ | ⟨hp, hq⟩
        · rw [hp, hq]; unfold mult; ring
        · rw [hp, hq]; unfold mult; ring
      rw [he, pow_mul]; norm_num
    rw [Finset.prod_congr rfl (fun r _ => h2 r), Finset.prod_const, Finset.card_univ, Fintype.card_fin]
  · rw [if_neg h]
    push_neg at h
    obtain ⟨h1, h2⟩ := h
    have key : ∃ r, mult i j p q r = 1 := by
      by_cases hpi : p = i
      · refine ⟨q, ?_⟩
        have e1 : i ≠ q := fun e => hpq (hpi.trans e)
        have e2 : j ≠ q := fun e => h1 hpi e.symm
        have e3 : p ≠ q := hpq
        simp [mult, e1, e2, e3]
      · by_cases hpj : p = j
        · refine ⟨q, ?_⟩
          have e1 : i ≠ q := fun e => h2 hpj e.symm
          have e2 : j ≠ q := fun e => hpq (hpj.trans e)
          have e3 : p ≠ q := hpq
          simp [mult, e1, e2, e3]
        · refine ⟨p, ?_⟩
          have e1 : i ≠ p := fun e => hpi e.symm
          have e2 : j ≠ p := fun e => hpj e.symm
          have e3 : q ≠ p := fun e => hpq e.symm
          simp [mult, e1, e2, e3]
    obtain ⟨r, hr⟩ := key
    apply Finset.prod_eq_zero (Finset.mem_univ r)
    rw [hr]; norm_num

/-! ## Lemma 6.3 as an exact finite average -/

/-- The off-diagonal sign chaos with coefficients c. -/
def chaos {n : ℕ} (c : Fin n → Fin n → ℝ) (x : Fin n → Bool) (i j : Fin n) : ℝ :=
  if i ≠ j then c i j * sgn (x i) * sgn (x j) else 0

theorem sum_chaos_pair {n : ℕ} (c : Fin n → Fin n → ℝ) (i j p q : Fin n) :
    ∑ x : Fin n → Bool, chaos c x i j * chaos c x p q
      = if i ≠ j ∧ p ≠ q ∧ ((p = i ∧ q = j) ∨ (p = j ∧ q = i)) then (2:ℝ) ^ n * (c i j * c p q) else 0 := by
  by_cases hij : i ≠ j
  · by_cases hpq : p ≠ q
    · have e : ∀ x : Fin n → Bool, chaos c x i j * chaos c x p q
          = (c i j * c p q) * (sgn (x i) * sgn (x j) * sgn (x p) * sgn (x q)) := by
        intro x; simp only [chaos, if_pos hij, if_pos hpq]; ring
      simp_rw [e, ← Finset.mul_sum, fourth_moment i j p q hij hpq]
      by_cases hpair : (p = i ∧ q = j) ∨ (p = j ∧ q = i)
      · rw [if_pos hpair, if_pos ⟨hij, hpq, hpair⟩]; ring
      · rw [if_neg hpair, if_neg (fun h => hpair h.2.2)]; ring
    · have e : ∀ x : Fin n → Bool, chaos c x i j * chaos c x p q = 0 := by
        intro x; simp only [chaos, if_neg hpq]; ring
      simp_rw [e, Finset.sum_const_zero]
      rw [if_neg (fun h => hpq h.2.1)]
  · have e : ∀ x : Fin n → Bool, chaos c x i j * chaos c x p q = 0 := by
      intro x; simp only [chaos, if_neg hij]; ring
    simp_rw [e, Finset.sum_const_zero]
    rw [if_neg (fun h => hij h.1)]

/-- For i ≠ j, summing the pairing indicator over (p, q) picks out (i, j) and (j, i). -/
theorem sum_pairing {n : ℕ} (c : Fin n → Fin n → ℝ) (i j : Fin n) (hij : i ≠ j) (K : ℝ) :
    ∑ p, ∑ q, (if i ≠ j ∧ p ≠ q ∧ ((p = i ∧ q = j) ∨ (p = j ∧ q = i)) then K * (c i j * c p q) else 0)
      = K * (c i j * (c i j + c j i)) := by
  have hsplit : ∀ p q : Fin n,
      (if i ≠ j ∧ p ≠ q ∧ ((p = i ∧ q = j) ∨ (p = j ∧ q = i)) then K * (c i j * c p q) else 0)
        = (if q = j then (if p = i then K * (c i j * c i j) else 0) else 0)
          + (if q = i then (if p = j then K * (c i j * c j i) else 0) else 0) := by
    intro p q
    by_cases hA : p = i ∧ q = j
    · rw [hA.1, hA.2]; simp [hij, Ne.symm hij]
    · by_cases hB : p = j ∧ q = i
      · rw [hB.1, hB.2]; simp [hij, Ne.symm hij]
      · have hn : ¬((p = i ∧ q = j) ∨ (p = j ∧ q = i)) := by tauto
        rw [if_neg (fun h => hn h.2.2)]
        have t1 : (if q = j then (if p = i then K * (c i j * c i j) else 0) else 0) = 0 := by
          by_cases hq : q = j
          · have hp : p ≠ i := fun hp => hA ⟨hp, hq⟩
            simp [hq, hp]
          · simp [hq]
        have t2 : (if q = i then (if p = j then K * (c i j * c j i) else 0) else 0) = 0 := by
          by_cases hq : q = i
          · have hp : p ≠ j := fun hp => hB ⟨hp, hq⟩
            simp [hq, hp]
          · simp [hq]
        rw [t1, t2]; ring
  simp only [hsplit, Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  ring

/-- Second moment of the sign chaos: the sum over all sign vectors of (sum_{i≠j} c_ij eps_i eps_j)^2
equals 2^n times sum_{i≠j} c_ij (c_ij + c_ji). -/
theorem chaos_second_moment {n : ℕ} (c : Fin n → Fin n → ℝ) :
    ∑ x : Fin n → Bool, (∑ i, ∑ j, chaos c x i j) ^ 2
      = (2:ℝ) ^ n * ∑ i, ∑ j, (if i ≠ j then c i j * (c i j + c j i) else 0) := by
  have expand : ∀ x : Fin n → Bool, (∑ i, ∑ j, chaos c x i j) ^ 2
      = ∑ i, ∑ p, ∑ j, ∑ q, chaos c x i j * chaos c x p q := by
    intro x
    rw [sq, Finset.sum_mul_sum]
    refine Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun p _ => ?_))
    rw [Finset.sum_mul_sum]
  simp_rw [expand]
  -- move the sum over sign vectors to the inside
  have inside : ∑ x : Fin n → Bool, ∑ i, ∑ p, ∑ j, ∑ q, chaos c x i j * chaos c x p q
      = ∑ i, ∑ p, ∑ j, ∑ q, ∑ x : Fin n → Bool, chaos c x i j * chaos c x p q := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl (fun p _ => ?_)
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl (fun j _ => ?_)
    rw [Finset.sum_comm]
  rw [inside]
  simp_rw [sum_chaos_pair]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [Finset.sum_comm, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  by_cases hij : i ≠ j
  · rw [sum_pairing c i j hij, if_pos hij]
  · rw [if_neg hij, mul_zero]
    refine Finset.sum_eq_zero (fun p _ => Finset.sum_eq_zero (fun q _ => ?_))
    rw [if_neg (fun h => hij h.1)]

/-- Reordering a fourfold finite sum. -/
theorem sum_comm4 {α β : Type*} [Fintype α] [Fintype β] (f : α → α → β → β → ℝ) :
    ∑ a, ∑ b, ∑ i, ∑ j, f a b i j = ∑ i, ∑ j, ∑ a, ∑ b, f a b i j := by
  calc ∑ a, ∑ b, ∑ i, ∑ j, f a b i j = ∑ a, ∑ i, ∑ b, ∑ j, f a b i j := by
        refine Finset.sum_congr rfl (fun a _ => ?_); exact Finset.sum_comm
    _ = ∑ i, ∑ a, ∑ b, ∑ j, f a b i j := Finset.sum_comm
    _ = ∑ i, ∑ a, ∑ j, ∑ b, f a b i j := by
        refine Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun a _ => ?_)); exact Finset.sum_comm
    _ = ∑ i, ∑ j, ∑ a, ∑ b, f a b i j := by
        refine Finset.sum_congr rfl (fun i _ => ?_); exact Finset.sum_comm

/-- Frobenius form of Lemma 6.3: with Q_x(a,b) = sum_{i≠j} eps_i eps_j o_ij phi_i(a) phi_j(b), the sum over
all sign vectors of ||Q_x||_F^2 equals 2^n sum_{i≠j} o_ij (o_ij |phi_i|^2 |phi_j|^2 + o_ji (phi_i.phi_j)^2). -/
theorem frobenius_moment {n k : ℕ} (o : Fin n → Fin n → ℝ) (φ : Fin n → Fin k → ℝ) :
    ∑ x : Fin n → Bool, ∑ a, ∑ b,
        (∑ i, ∑ j, chaos (fun i j => o i j * φ i a * φ j b) x i j) ^ 2
      = (2:ℝ) ^ n * ∑ i, ∑ j, (if i ≠ j then
          o i j * (o i j * (∑ a, φ i a ^ 2) * (∑ b, φ j b ^ 2)
                   + o j i * (∑ a, φ i a * φ j a) ^ 2) else 0) := by
  have step1 : ∑ x : Fin n → Bool, ∑ a, ∑ b,
        (∑ i, ∑ j, chaos (fun i j => o i j * φ i a * φ j b) x i j) ^ 2
      = ∑ a, ∑ b, ∑ x : Fin n → Bool,
        (∑ i, ∑ j, chaos (fun i j => o i j * φ i a * φ j b) x i j) ^ 2 := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl (fun a _ => ?_)
    rw [Finset.sum_comm]
  rw [step1]
  simp_rw [chaos_second_moment]
  simp_rw [← Finset.mul_sum]
  congr 1
  rw [sum_comm4 (fun a b i j => (if i ≠ j then (o i j * φ i a * φ j b) *
      ((o i j * φ i a * φ j b) + (o j i * φ j a * φ i b)) else 0))]
  refine Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => ?_))
  by_cases hij : i ≠ j
  · simp only [if_pos hij]
    have e1 : ∑ a, ∑ b, (o i j * φ i a * φ j b) * (o i j * φ i a * φ j b)
        = o i j * (o i j * (∑ a, φ i a ^ 2) * (∑ b, φ j b ^ 2)) := by
      rw [show o i j * (o i j * (∑ a, φ i a ^ 2) * (∑ b, φ j b ^ 2))
          = (∑ a, o i j * φ i a ^ 2) * (∑ b, o i j * φ j b ^ 2) by
            rw [← Finset.mul_sum, ← Finset.mul_sum]; ring]
      rw [Finset.sum_mul_sum]
      refine Finset.sum_congr rfl (fun a _ => Finset.sum_congr rfl (fun b _ => ?_)); ring
    have e2 : ∑ a, ∑ b, (o i j * φ i a * φ j b) * (o j i * φ j a * φ i b)
        = o i j * (o j i * (∑ a, φ i a * φ j a) ^ 2) := by
      rw [show o i j * (o j i * (∑ a, φ i a * φ j a) ^ 2)
          = (∑ a, o i j * o j i * (φ i a * φ j a)) * (∑ b, φ i b * φ j b) by
            rw [← Finset.mul_sum, sq]; ring]
      rw [Finset.sum_mul_sum]
      refine Finset.sum_congr rfl (fun a _ => Finset.sum_congr rfl (fun b _ => ?_)); ring
    calc ∑ a, ∑ b, (o i j * φ i a * φ j b) * ((o i j * φ i a * φ j b) + (o j i * φ j a * φ i b))
        = ∑ a, ∑ b, ((o i j * φ i a * φ j b) * (o i j * φ i a * φ j b)
            + (o i j * φ i a * φ j b) * (o j i * φ j a * φ i b)) := by
          refine Finset.sum_congr rfl (fun a _ => Finset.sum_congr rfl (fun b _ => ?_)); ring
      _ = o i j * (o i j * (∑ a, φ i a ^ 2) * (∑ b, φ j b ^ 2) + o j i * (∑ a, φ i a * φ j a) ^ 2) := by
          simp_rw [Finset.sum_add_distrib]; rw [e1, e2]; ring
  · simp only [if_neg hij, Finset.sum_const_zero]

/-- The bound of Lemma 6.3: for symmetric o with |o_ij| <= a, the right side above is at most
2 a^2 (sum_i |phi_i|^2)^2 (before the factor 2^n). -/
theorem frobenius_bound {n k : ℕ} (o : Fin n → Fin n → ℝ) (φ : Fin n → Fin k → ℝ) (a : ℝ)
    (hsym : ∀ i j, o j i = o i j) (hbd : ∀ i j, i ≠ j → |o i j| ≤ a) :
    (∑ i, ∑ j, (if i ≠ j then
          o i j * (o i j * (∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2)
                   + o j i * (∑ c, φ i c * φ j c) ^ 2) else 0))
      ≤ 2 * a ^ 2 * (∑ i, ∑ c, φ i c ^ 2) ^ 2 := by
  have hu0 : ∀ i, 0 ≤ ∑ c, φ i c ^ 2 := fun i => Finset.sum_nonneg (fun c _ => sq_nonneg _)
  have hcs : ∀ i j, (∑ c, φ i c * φ j c) ^ 2 ≤ (∑ c, φ i c ^ 2) * (∑ c, φ j c ^ 2) :=
    fun i j => Finset.sum_mul_sq_le_sq_mul_sq Finset.univ (φ i) (φ j)
  have term : ∀ i j, i ≠ j →
      o i j * (o i j * (∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2) + o j i * (∑ c, φ i c * φ j c) ^ 2)
        ≤ 2 * a ^ 2 * ((∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2)) := by
    intro i j hij
    rw [hsym i j]
    have hab := hbd i j hij
    have ha0 : 0 ≤ a := le_trans (abs_nonneg _) hab
    have ha : o i j ^ 2 ≤ a ^ 2 := by
      rw [← sq_abs]; exact pow_le_pow_left₀ (abs_nonneg _) hab 2
    have huu : 0 ≤ (∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2) := mul_nonneg (hu0 i) (hu0 j)
    have hc := hcs i j
    calc o i j * (o i j * (∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2) + o i j * (∑ c, φ i c * φ j c) ^ 2)
        = o i j ^ 2 * ((∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2) + (∑ c, φ i c * φ j c) ^ 2) := by ring
      _ ≤ a ^ 2 * ((∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2) + (∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2)) := by
          apply mul_le_mul ha (by linarith) (by positivity) (by positivity)
      _ = 2 * a ^ 2 * ((∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2)) := by ring
  calc (∑ i, ∑ j, (if i ≠ j then
          o i j * (o i j * (∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2)
                   + o j i * (∑ c, φ i c * φ j c) ^ 2) else 0))
      ≤ ∑ i, ∑ j, 2 * a ^ 2 * ((∑ c, φ i c ^ 2) * (∑ d, φ j d ^ 2)) := by
        apply Finset.sum_le_sum; intro i _
        apply Finset.sum_le_sum; intro j _
        by_cases hij : i ≠ j
        · rw [if_pos hij]; exact term i j hij
        · rw [if_neg hij]
          exact mul_nonneg (mul_nonneg (by norm_num) (sq_nonneg a)) (mul_nonneg (hu0 i) (hu0 j))
    _ = 2 * a ^ 2 * (∑ i, ∑ c, φ i c ^ 2) ^ 2 := by
        rw [sq (∑ i, ∑ c, φ i c ^ 2), Finset.sum_mul_sum, Finset.mul_sum]
        refine Finset.sum_congr rfl (fun i _ => ?_)
        rw [Finset.mul_sum]

/-! ## The averaging step of Proposition 6.4 -/

/-- Some sign vector does at least as well as the average over all 2^n sign vectors. -/
theorem exists_le_average {n : ℕ} (F : (Fin n → Bool) → ℝ) :
    ∃ x, F x ≤ (∑ y, F y) / (2:ℝ) ^ n := by
  have hcard : (Finset.univ : Finset (Fin n → Bool)).card = 2 ^ n := by
    simp [Finset.card_univ, Fintype.card_fun, Fintype.card_bool, Fintype.card_fin]
  have hpos : (0:ℝ) < (2:ℝ) ^ n := by positivity
  have H : ∑ y, F y ≤ ∑ _y : Fin n → Bool, (∑ z, F z) / (2:ℝ) ^ n := by
    rw [Finset.sum_const, hcard, nsmul_eq_mul]
    push_cast
    rw [mul_div_cancel₀ _ hpos.ne']
  obtain ⟨x, -, hx⟩ := Finset.exists_le_of_sum_le Finset.univ_nonempty H
  exact ⟨x, hx⟩

/-- Proposition 6.4, the choice of signs: some x has sum_{a,b} Q_x(a,b)^2 <= 2 a^2 (sum_i |phi_i|^2)^2. -/
theorem exists_good_signs {n k : ℕ} (o : Fin n → Fin n → ℝ) (φ : Fin n → Fin k → ℝ) (a : ℝ)
    (hsym : ∀ i j, o j i = o i j) (hbd : ∀ i j, i ≠ j → |o i j| ≤ a) :
    ∃ x : Fin n → Bool, ∑ c, ∑ d,
        (∑ i, ∑ j, chaos (fun i j => o i j * φ i c * φ j d) x i j) ^ 2
      ≤ 2 * a ^ 2 * (∑ i, ∑ c, φ i c ^ 2) ^ 2 := by
  obtain ⟨x, hx⟩ := exists_le_average (fun x => ∑ c, ∑ d,
      (∑ i, ∑ j, chaos (fun i j => o i j * φ i c * φ j d) x i j) ^ 2)
  refine ⟨x, hx.trans ?_⟩
  rw [frobenius_moment o φ, mul_div_cancel_left₀ _ (by positivity)]
  exact frobenius_bound o φ a hsym hbd

/-! ## Euclidean norms of real vectors -/

open Matrix

section Norms

variable {ι κ μ : Type*} [Fintype ι] [Fintype κ] [Fintype μ]

/-- The squared Euclidean norm. -/
def nsq (v : ι → ℝ) : ℝ := v ⬝ᵥ v

/-- The Euclidean norm. -/
noncomputable def nrm (v : ι → ℝ) : ℝ := Real.sqrt (nsq v)

theorem nsq_nonneg (v : ι → ℝ) : 0 ≤ nsq v :=
  Finset.sum_nonneg (fun i _ => mul_self_nonneg (v i))

theorem nrm_nonneg (v : ι → ℝ) : 0 ≤ nrm v := Real.sqrt_nonneg _

theorem nsq_zero : nsq (0 : ι → ℝ) = 0 := by simp [nsq]

theorem nrm_sq (v : ι → ℝ) : nrm v ^ 2 = nsq v := Real.sq_sqrt (nsq_nonneg v)

theorem nrm_pos {v : ι → ℝ} (hv : v ≠ 0) : 0 < nrm v := by
  apply Real.sqrt_pos.mpr
  rcases (nsq_nonneg v).lt_or_eq with h | h
  · exact h
  · exact absurd (dotProduct_self_eq_zero.mp h.symm) hv

/-- Cauchy-Schwarz. -/
theorem dot_le_nrm (u v : ι → ℝ) : u ⬝ᵥ v ≤ nrm u * nrm v := by
  have hcs : (u ⬝ᵥ v) ^ 2 ≤ nsq u * nsq v := by
    have h := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ u v
    simpa [nsq, dotProduct, sq] using h
  have h2 : (u ⬝ᵥ v) ^ 2 ≤ (nrm u * nrm v) ^ 2 := by
    rw [mul_pow, nrm_sq, nrm_sq]; exact hcs
  have h0 : 0 ≤ nrm u * nrm v := mul_nonneg (nrm_nonneg u) (nrm_nonneg v)
  nlinarith [h2, h0]

theorem nsq_add (u v : ι → ℝ) : nsq (u + v) = nsq u + 2 * (u ⬝ᵥ v) + nsq v := by
  simp only [nsq, add_dotProduct, dotProduct_add, dotProduct_comm v u]; ring

/-- The triangle inequality. -/
theorem nrm_add_le (u v : ι → ℝ) : nrm (u + v) ≤ nrm u + nrm v := by
  have key : nsq (u + v) ≤ (nrm u + nrm v) ^ 2 := by
    rw [nsq_add, add_sq, nrm_sq, nrm_sq]
    nlinarith [dot_le_nrm u v]
  calc nrm (u + v) = Real.sqrt (nsq (u + v)) := rfl
    _ ≤ Real.sqrt ((nrm u + nrm v) ^ 2) := Real.sqrt_le_sqrt key
    _ = nrm u + nrm v := Real.sqrt_sq (add_nonneg (nrm_nonneg u) (nrm_nonneg v))

/-- The reverse triangle inequality for a difference of three vectors. -/
theorem nrm_sub_sub_ge (a b c : ι → ℝ) : nrm a - nrm b - nrm c ≤ nrm (a - b - c) := by
  have h1 := nrm_add_le (a - b - c) b
  have h2 := nrm_add_le (a - b - c + b) c
  have e : a - b - c + b + c = a := by abel
  rw [e] at h2
  linarith

theorem nsq_smul (c : ℝ) (v : ι → ℝ) : nsq (c • v) = c ^ 2 * nsq v := by
  simp only [nsq, smul_dotProduct, dotProduct_smul, smul_eq_mul]; ring

theorem nrm_smul (c : ℝ) (v : ι → ℝ) : nrm (c • v) = |c| * nrm v := by
  rw [nrm, nsq_smul, Real.sqrt_mul (sq_nonneg c), Real.sqrt_sq_eq_abs]; rfl

/-- From a bound on squared norms to a bound on norms. -/
theorem nrm_le_of_nsq_le {u : ι → ℝ} {v : κ → ℝ} {c : ℝ} (hc : 0 ≤ c) (h : nsq u ≤ c ^ 2 * nsq v) :
    nrm u ≤ c * nrm v := by
  calc nrm u = Real.sqrt (nsq u) := rfl
    _ ≤ Real.sqrt (c ^ 2 * nsq v) := Real.sqrt_le_sqrt h
    _ = c * nrm v := by rw [Real.sqrt_mul (sq_nonneg c), Real.sqrt_sq hc]; rfl

theorem nrm_ge_of_nsq_ge {u : ι → ℝ} {v : κ → ℝ} {c : ℝ} (hc : 0 ≤ c) (h : c ^ 2 * nsq u ≤ nsq v) :
    c * nrm u ≤ nrm v := by
  calc c * nrm u = Real.sqrt (c ^ 2 * nsq u) := by
        rw [Real.sqrt_mul (sq_nonneg c), Real.sqrt_sq hc]; rfl
    _ ≤ Real.sqrt (nsq v) := Real.sqrt_le_sqrt h
    _ = nrm v := rfl

/-! ## Operator bounds -/

/-- The squared Frobenius norm. -/
def frob (Q : Matrix κ μ ℝ) : ℝ := ∑ c, ∑ d, Q c d ^ 2

/-- The operator norm is at most the Frobenius norm. -/
theorem nsq_mulVec_le (Q : Matrix κ μ ℝ) (v : μ → ℝ) : nsq (Q *ᵥ v) ≤ frob Q * nsq v := by
  have h : ∀ c, (Q *ᵥ v) c * (Q *ᵥ v) c ≤ (∑ d, Q c d ^ 2) * nsq v := by
    intro c
    have hc := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ (fun d => Q c d) v
    have e1 : (Q *ᵥ v) c = ∑ d, Q c d * v d := rfl
    have e2 : nsq v = ∑ d, v d ^ 2 := by simp [nsq, dotProduct, sq]
    rw [e1, e2, ← sq]; exact hc
  calc nsq (Q *ᵥ v) = ∑ c, (Q *ᵥ v) c * (Q *ᵥ v) c := rfl
    _ ≤ ∑ c, (∑ d, Q c d ^ 2) * nsq v := Finset.sum_le_sum (fun c _ => h c)
    _ = frob Q * nsq v := by rw [frob, Finset.sum_mul]

/-- A diagonal matrix with entries of modulus at most δ has operator norm at most δ. -/
theorem nrm_diagonal_mulVec_le [DecidableEq ι] (d : ι → ℝ) (δ : ℝ) (hδ : 0 ≤ δ) (hd : ∀ i, |d i| ≤ δ)
    (w : ι → ℝ) : nrm (diagonal d *ᵥ w) ≤ δ * nrm w := by
  apply nrm_le_of_nsq_le hδ
  have h : ∀ i, (diagonal d *ᵥ w) i * (diagonal d *ᵥ w) i ≤ δ ^ 2 * (w i * w i) := by
    intro i
    rw [mulVec_diagonal]
    have h1 : d i ^ 2 ≤ δ ^ 2 := by
      rw [← sq_abs]; exact pow_le_pow_left₀ (abs_nonneg _) (hd i) 2
    nlinarith [mul_self_nonneg (w i)]
  calc nsq (diagonal d *ᵥ w) = ∑ i, (diagonal d *ᵥ w) i * (diagonal d *ᵥ w) i := rfl
    _ ≤ ∑ i, δ ^ 2 * (w i * w i) := Finset.sum_le_sum (fun i _ => h i)
    _ = δ ^ 2 * nsq w := by rw [← Finset.mul_sum]; rfl

/-- A matrix with orthonormal columns preserves norms. -/
theorem nsq_mulVec_orth [DecidableEq κ] (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (v : κ → ℝ) :
    nsq (Φ *ᵥ v) = nsq v := by
  unfold nsq
  rw [dotProduct_mulVec, ← mulVec_transpose, mulVec_mulVec, hΦ, one_mulVec]

theorem nrm_mulVec_orth [DecidableEq κ] (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (v : κ → ℝ) :
    nrm (Φ *ᵥ v) = nrm v := by
  rw [nrm, nsq_mulVec_orth Φ hΦ v]; rfl

/-- Bessel's inequality: the transpose of a matrix with orthonormal columns does not increase norms. -/
theorem nrm_transpose_mulVec_le [DecidableEq κ] (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (u : ι → ℝ) :
    nrm (Φᵀ *ᵥ u) ≤ nrm u := by
  have h1 : nsq (Φ *ᵥ (Φᵀ *ᵥ u)) = nsq (Φᵀ *ᵥ u) := nsq_mulVec_orth Φ hΦ _
  have h2 : u ⬝ᵥ (Φ *ᵥ (Φᵀ *ᵥ u)) = nsq (Φᵀ *ᵥ u) := by
    rw [dotProduct_mulVec, ← mulVec_transpose, nsq]
  have h3 : 0 ≤ nsq (u - Φ *ᵥ (Φᵀ *ᵥ u)) := nsq_nonneg _
  have h4 : nsq (u - Φ *ᵥ (Φᵀ *ᵥ u))
      = nsq u - 2 * (u ⬝ᵥ (Φ *ᵥ (Φᵀ *ᵥ u))) + nsq (Φ *ᵥ (Φᵀ *ᵥ u)) := by
    simp only [nsq, sub_dotProduct, dotProduct_sub, dotProduct_comm (Φ *ᵥ (Φᵀ *ᵥ u)) u]; ring
  have h5 : nsq (Φᵀ *ᵥ u) ≤ nsq u := by linarith
  exact Real.sqrt_le_sqrt h5

end Norms

/-! ## Rank -/

section Rank

variable {κ μ : Type*} [Fintype κ] [Fintype μ]

/-- The rank of a sum is at most the sum of the ranks. -/
theorem rank_add_le' (A B : Matrix μ κ ℝ) : (A + B).rank ≤ A.rank + B.rank := by
  unfold Matrix.rank
  rw [Matrix.mulVecLin_add]
  exact (Submodule.finrank_mono (LinearMap.range_add_le _ _)).trans
    (Submodule.finrank_add_le_finrank_add_finrank _ _)

/-- A matrix of rank less than the number of its columns has a nonzero kernel vector. -/
theorem exists_ker (R : Matrix μ κ ℝ) (h : R.rank < Fintype.card κ) :
    ∃ v : κ → ℝ, v ≠ 0 ∧ R *ᵥ v = 0 := by
  have hrn := LinearMap.finrank_range_add_finrank_ker (Matrix.mulVecLin R)
  rw [Module.finrank_fintype_fun_eq_card] at hrn
  have hr : R.rank = Module.finrank ℝ (LinearMap.range R.mulVecLin) := rfl
  have hpos : 0 < Module.finrank ℝ (LinearMap.ker R.mulVecLin) := by omega
  have hne : LinearMap.ker R.mulVecLin ≠ ⊥ := by
    intro hb
    rw [hb, finrank_bot] at hpos
    exact lt_irrefl _ hpos
  obtain ⟨v, hv, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hne
  exact ⟨v, hv0, by simpa using hv⟩

end Rank

/-! ## Approximation numbers

For σ ≥ 0, `ApproxGE k σ T` says that every matrix of rank less than `k` is at operator-norm distance at
least σ from `T`: for each such `R` some nonzero vector `v` has `‖(T - R) v‖ ≥ σ ‖v‖`. The distance from `T`
to the matrices of rank less than `k` is the `k`-th singular value of `T` (Lemma 2.5 of the paper, the
characterization `s_k(T) = min {‖T - B‖ : rank B < k}`), so `ApproxGE k σ T` is `s_k(T) ≥ σ`. -/

section Approx

variable {ι κ μ : Type*} [Fintype ι] [Fintype κ] [Fintype μ]

def ApproxGE (k : ℕ) (σ : ℝ) (T : Matrix μ κ ℝ) : Prop :=
  ∀ R : Matrix μ κ ℝ, R.rank < k → ∃ v : κ → ℝ, v ≠ 0 ∧ σ * nrm v ≤ nrm ((T - R) *ᵥ v)

theorem ApproxGE.mono {k : ℕ} {σ σ' : ℝ} {T : Matrix μ κ ℝ} (h : ApproxGE k σ T) (hσ : σ' ≤ σ) :
    ApproxGE k σ' T := by
  intro R hR
  obtain ⟨v, hv0, hv⟩ := h R hR
  exact ⟨v, hv0, le_trans (mul_le_mul_of_nonneg_right hσ (nrm_nonneg v)) hv⟩

/-- A square matrix that stretches every vector by at least σ has k-th approximation number at least σ,
k being its size. -/
theorem approx_of_lower (T : Matrix κ κ ℝ) (σ : ℝ) (h : ∀ v, σ * nrm v ≤ nrm (T *ᵥ v)) :
    ApproxGE (Fintype.card κ) σ T := by
  intro R hR
  obtain ⟨v, hv0, hRv⟩ := exists_ker R hR
  refine ⟨v, hv0, ?_⟩
  rw [sub_mulVec, hRv, sub_zero]
  exact h v

/-- Lemma 2.5, the compression inequality in the form used: if `Φ` has orthonormal columns and the
compression `Φᵀ C Φ` stretches every vector by at least σ, then `s_k(C) ≥ σ` with `k` the number of
columns of `Φ`. -/
theorem approx_compress [DecidableEq κ] (C : Matrix ι ι ℝ) (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (σ : ℝ)
    (h : ∀ v, σ * nrm v ≤ nrm ((Φᵀ * C * Φ) *ᵥ v)) : ApproxGE (Fintype.card κ) σ C := by
  intro R hR
  have hR' : (Φᵀ * R * Φ).rank < Fintype.card κ :=
    lt_of_le_of_lt ((rank_mul_le_left _ _).trans (rank_mul_le_right _ _)) hR
  obtain ⟨v, hv0, hRv⟩ := exists_ker (Φᵀ * R * Φ) hR'
  have hn : nrm (Φ *ᵥ v) = nrm v := nrm_mulVec_orth Φ hΦ v
  refine ⟨Φ *ᵥ v, ?_, ?_⟩
  · intro h0
    have h1 : nrm v = 0 := by rw [← hn, h0]; simp [nrm, nsq]
    exact (ne_of_gt (nrm_pos hv0)) h1
  · have key : Φᵀ *ᵥ ((C - R) *ᵥ (Φ *ᵥ v)) = (Φᵀ * C * Φ) *ᵥ v := by
      rw [mulVec_mulVec, mulVec_mulVec, Matrix.mul_sub, Matrix.sub_mul, sub_mulVec, hRv, sub_zero]
    calc σ * nrm (Φ *ᵥ v) = σ * nrm v := by rw [hn]
      _ ≤ nrm ((Φᵀ * C * Φ) *ᵥ v) := h v
      _ = nrm (Φᵀ *ᵥ ((C - R) *ᵥ (Φ *ᵥ v))) := by rw [key]
      _ ≤ nrm ((C - R) *ᵥ (Φ *ᵥ v)) := nrm_transpose_mulVec_le Φ hΦ _

/-- Approximation numbers do not change when rows and columns are renamed by the same bijection. -/
theorem approx_submatrix {ι' : Type*} [Fintype ι'] (T : Matrix ι ι ℝ) (e : ι' ≃ ι) (k : ℕ) (σ : ℝ)
    (h : ApproxGE k σ T) : ApproxGE k σ (T.submatrix e e) := by
  intro R hR
  have hR' : (R.submatrix e.symm e.symm).rank < k := by rw [Matrix.rank_submatrix]; exact hR
  obtain ⟨v, hv0, hv⟩ := h _ hR'
  have hnsq : ∀ w : ι → ℝ, nsq (w ∘ e) = nsq w := by
    intro w
    simp only [nsq, dotProduct, Function.comp_apply]
    exact Equiv.sum_comp e (fun i => w i * w i)
  have hnrm : ∀ w : ι → ℝ, nrm (w ∘ e) = nrm w := by
    intro w; rw [nrm, hnsq]; rfl
  refine ⟨v ∘ e, ?_, ?_⟩
  · intro h0
    apply hv0
    funext i
    have := congrFun h0 (e.symm i)
    simpa using this
  · have e1 : T.submatrix e e - R = (T - R.submatrix e.symm e.symm).submatrix e e := by
      ext i j; simp
    have e2 : (T - R.submatrix e.symm e.symm).submatrix e e *ᵥ (v ∘ e)
        = ((T - R.submatrix e.symm e.symm) *ᵥ v) ∘ e := by
      rw [submatrix_mulVec_equiv]
      have hv' : (v ∘ e) ∘ e.symm = v := by funext i; simp
      rw [hv']
    rw [e1, e2, hnrm, hnrm]
    exact hv

end Approx

/-! ## The symmetric dilation and Lemma 6.2(b) -/

section Dilation

variable {I J : Type*} [Fintype I] [Fintype J]

/-- The symmetric dilation `[[0, M], [Mᵀ, 0]]` of a rectangular matrix. -/
def dil (M : Matrix I J ℝ) : Matrix (I ⊕ J) (I ⊕ J) ℝ := Matrix.fromBlocks 0 M Mᵀ 0

/-- Inclusion of the first summand. -/
def incl1 (I J : Type*) [DecidableEq I] [DecidableEq J] : Matrix (I ⊕ J) I ℝ :=
  Matrix.of fun a i => if a = Sum.inl i then 1 else 0

/-- Inclusion of the second summand. -/
def incl2 (I J : Type*) [DecidableEq I] [DecidableEq J] : Matrix (I ⊕ J) J ℝ :=
  Matrix.of fun a j => if a = Sum.inr j then 1 else 0

theorem dil_eq [DecidableEq I] [DecidableEq J] (R : Matrix I J ℝ) :
    dil R = incl1 I J * R * (incl2 I J)ᵀ + incl2 I J * Rᵀ * (incl1 I J)ᵀ := by
  ext a b
  rcases a with i | j <;> rcases b with i' | j' <;>
    simp [dil, incl1, incl2, Matrix.mul_apply, ite_mul, mul_ite, Finset.sum_ite_eq, Finset.sum_ite_eq']

/-- The dilation of `R` has rank at most twice the rank of `R`. -/
theorem rank_dil_le [DecidableEq I] [DecidableEq J] (R : Matrix I J ℝ) : (dil R).rank ≤ 2 * R.rank := by
  rw [dil_eq]
  have h1 : (incl1 I J * R * (incl2 I J)ᵀ).rank ≤ R.rank :=
    (Matrix.rank_mul_le_left _ _).trans (Matrix.rank_mul_le_right _ _)
  have h2 : (incl2 I J * Rᵀ * (incl1 I J)ᵀ).rank ≤ R.rank := by
    have h := (Matrix.rank_mul_le_left (incl2 I J * Rᵀ) (incl1 I J)ᵀ).trans
      (Matrix.rank_mul_le_right (incl2 I J) Rᵀ)
    rw [Matrix.rank_transpose] at h
    exact h
  have h3 := rank_add_le' (incl1 I J * R * (incl2 I J)ᵀ) (incl2 I J * Rᵀ * (incl1 I J)ᵀ)
  omega

theorem dil_sub (M R : Matrix I J ℝ) : dil M - dil R = dil (M - R) := by
  ext a b
  rcases a with i | j <;> rcases b with i' | j' <;> simp [dil]

theorem dil_mulVec (M : Matrix I J ℝ) (w : I ⊕ J → ℝ) :
    dil M *ᵥ w = Sum.elim (M *ᵥ (w ∘ Sum.inr)) (Mᵀ *ᵥ (w ∘ Sum.inl)) := by
  rw [dil, Matrix.fromBlocks_mulVec]
  simp

theorem nsq_sum (w : I ⊕ J → ℝ) : nsq w = nsq (w ∘ Sum.inl) + nsq (w ∘ Sum.inr) := by
  simp [nsq, dotProduct, Fintype.sum_sum_type]

theorem nsq_elim (u : I → ℝ) (v : J → ℝ) : nsq (Sum.elim u v) = nsq u + nsq v := by
  simp [nsq, dotProduct, Fintype.sum_sum_type]

/-- A vector stretched by the transpose gives a vector stretched by the matrix itself. -/
theorem transpose_stretch (N : Matrix I J ℝ) (σ : ℝ) (hσ : 0 < σ) (u : I → ℝ) (hu : u ≠ 0)
    (h : σ * nrm u ≤ nrm (Nᵀ *ᵥ u)) : ∃ v : J → ℝ, v ≠ 0 ∧ σ * nrm v ≤ nrm (N *ᵥ v) := by
  have hu0 : 0 < nrm u := nrm_pos hu
  have hv0 : 0 < nrm (Nᵀ *ᵥ u) := lt_of_lt_of_le (mul_pos hσ hu0) h
  have hvne : Nᵀ *ᵥ u ≠ 0 := by
    intro h0
    rw [h0] at hv0
    simp [nrm, nsq] at hv0
  refine ⟨Nᵀ *ᵥ u, hvne, ?_⟩
  have e : nsq (Nᵀ *ᵥ u) = u ⬝ᵥ (N *ᵥ (Nᵀ *ᵥ u)) := by
    rw [dotProduct_mulVec, ← mulVec_transpose, nsq]
  have key : nrm (Nᵀ *ᵥ u) ^ 2 ≤ nrm u * nrm (N *ᵥ (Nᵀ *ᵥ u)) := by
    rw [nrm_sq, e]; exact dot_le_nrm u _
  have h4 : σ * nrm (Nᵀ *ᵥ u) * nrm u ≤ nrm (N *ᵥ (Nᵀ *ᵥ u)) * nrm u := by
    nlinarith [h, key, nrm_nonneg (Nᵀ *ᵥ u)]
  exact le_of_mul_le_mul_right h4 hu0

/-- Lemma 6.2(b) in the direction used: `s_m(M) ≥ s_{2m-1}` of its symmetric dilation. -/
theorem approx_of_dil [DecidableEq I] [DecidableEq J] (M : Matrix I J ℝ) (m : ℕ) (σ : ℝ) (hσ : 0 < σ)
    (h : ApproxGE (2 * m - 1) σ (dil M)) : ApproxGE m σ M := by
  intro R hR
  have hrank : (dil R).rank < 2 * m - 1 := by
    have := rank_dil_le R; omega
  obtain ⟨w, hw0, hw⟩ := h (dil R) hrank
  rw [dil_sub, dil_mulVec] at hw
  have hsq : σ ^ 2 * (nsq (w ∘ Sum.inl) + nsq (w ∘ Sum.inr))
      ≤ nsq ((M - R) *ᵥ (w ∘ Sum.inr)) + nsq ((M - R)ᵀ *ᵥ (w ∘ Sum.inl)) := by
    have h0 : 0 ≤ σ * nrm w := mul_nonneg hσ.le (nrm_nonneg w)
    have h1 := pow_le_pow_left₀ h0 hw 2
    rw [mul_pow, nrm_sq, nrm_sq, nsq_elim, nsq_sum] at h1
    exact h1
  have hwsplit : w ∘ Sum.inl ≠ 0 ∨ w ∘ Sum.inr ≠ 0 := by
    by_contra hc
    push_neg at hc
    apply hw0
    funext a
    rcases a with i | j
    · exact congrFun hc.1 i
    · exact congrFun hc.2 j
  by_cases hA : w ∘ Sum.inr ≠ 0 ∧ σ ^ 2 * nsq (w ∘ Sum.inr) ≤ nsq ((M - R) *ᵥ (w ∘ Sum.inr))
  · exact ⟨w ∘ Sum.inr, hA.1, nrm_ge_of_nsq_ge hσ.le hA.2⟩
  · have hB : σ ^ 2 * nsq (w ∘ Sum.inl) ≤ nsq ((M - R)ᵀ *ᵥ (w ∘ Sum.inl)) := by
      by_cases hz : w ∘ Sum.inr = 0
      · rw [hz] at hsq
        simp only [mulVec_zero, nsq_zero, add_zero, zero_add] at hsq
        linarith
      · have hlt : nsq ((M - R) *ᵥ (w ∘ Sum.inr)) < σ ^ 2 * nsq (w ∘ Sum.inr) := by
          by_contra hc
          exact hA ⟨hz, not_lt.mp hc⟩
        linarith
    have hl : w ∘ Sum.inl ≠ 0 := by
      intro hl0
      rcases hwsplit with h1 | h2
      · exact h1 hl0
      · have hlt : nsq ((M - R) *ᵥ (w ∘ Sum.inr)) < σ ^ 2 * nsq (w ∘ Sum.inr) := by
          by_contra hc
          exact hA ⟨h2, not_lt.mp hc⟩
        rw [hl0] at hsq
        simp only [mulVec_zero, nsq_zero, add_zero, zero_add] at hsq
        linarith
    exact transpose_stretch (M - R) σ hσ (w ∘ Sum.inl) hl (nrm_ge_of_nsq_ge hσ.le hB)

end Dilation

/-! ## Proposition 6.4 -/

/-- The off-diagonal block part `C` of `A` for the partition `{x = true}`, `{x = false}`. -/
def offBlock {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (x : Fin n → Bool) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun i j => if x i = x j then 0 else A i j

/-- The compressed sign chaos `Q_ε` of Lemma 6.3, with `o = A` off the diagonal and `φ_i` the rows of `Φ`. -/
def chaosMat {n k : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (Φ : Matrix (Fin n) (Fin k) ℝ) (x : Fin n → Bool) :
    Matrix (Fin k) (Fin k) ℝ :=
  Matrix.of fun c d => ∑ i, ∑ j, chaos (fun i j => A i j * Φ i c * Φ j d) x i j

theorem sgn_mul_self (b : Bool) : sgn b * sgn b = 1 := by cases b <;> simp [sgn]

theorem triple_apply {n k : ℕ} (Φ : Matrix (Fin n) (Fin k) ℝ) (B : Matrix (Fin n) (Fin n) ℝ) (c d : Fin k) :
    (Φᵀ * B * Φ) c d = ∑ i, ∑ j, Φ i c * B i j * Φ j d := by
  simp only [Matrix.mul_apply, Matrix.transpose_apply, Finset.sum_mul]
  rw [Finset.sum_comm]

theorem entry_split {n : ℕ} (f : Fin n → Fin n → ℝ) :
    ∑ i, ∑ j, f i j = ∑ i, f i i + ∑ i, ∑ j, (if i ≠ j then f i j else 0) := by
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  have h : ∀ j, f i j = (if i = j then f i j else 0) + (if i ≠ j then f i j else 0) := by
    intro j; by_cases hij : i = j <;> simp [hij]
  rw [Finset.sum_congr rfl (fun j _ => h j), Finset.sum_add_distrib]
  congr 1
  simp

/-- The identity of Proposition 6.4: `2 Φᵀ C Φ = Φᵀ A Φ - Φᵀ Δ Φ - Q_ε`, entrywise over all `n`. -/
theorem compressed_identity {n k : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (Φ : Matrix (Fin n) (Fin k) ℝ)
    (x : Fin n → Bool) :
    (2:ℝ) • (Φᵀ * offBlock A x * Φ)
      = Φᵀ * A * Φ - Φᵀ * diagonal (fun i => A i i) * Φ - chaosMat A Φ x := by
  ext c d
  simp only [Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul, chaosMat, Matrix.of_apply]
  rw [triple_apply, triple_apply, triple_apply]
  have hsplit : ∑ i, ∑ j, Φ i c * (sgn (x i) * sgn (x j) * A i j) * Φ j d
      = ∑ i, Φ i c * (sgn (x i) * sgn (x i) * A i i) * Φ i d
        + ∑ i, ∑ j, (if i ≠ j then Φ i c * (sgn (x i) * sgn (x j) * A i j) * Φ j d else 0) :=
    entry_split (fun i j => Φ i c * (sgn (x i) * sgn (x j) * A i j) * Φ j d)
  have hdiagsum : ∑ i, ∑ j, Φ i c * diagonal (fun i => A i i) i j * Φ j d
      = ∑ i, Φ i c * A i i * Φ i d := by
    refine Finset.sum_congr rfl (fun i _ => ?_)
    simp [diagonal_apply, mul_ite, ite_mul, Finset.sum_ite_eq]
  have hA : ∑ i, ∑ j, Φ i c * A i j * Φ j d
      = 2 * ∑ i, ∑ j, Φ i c * offBlock A x i j * Φ j d
        + ∑ i, ∑ j, Φ i c * (sgn (x i) * sgn (x j) * A i j) * Φ j d := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun j _ => ?_)
    have e := sign_identity (A i j) (x i) (x j)
    simp only [offBlock, Matrix.of_apply]
    linear_combination (Φ i c * Φ j d) * e
  have hdiag2 : ∑ i, Φ i c * (sgn (x i) * sgn (x i) * A i i) * Φ i d = ∑ i, Φ i c * A i i * Φ i d := by
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [sgn_mul_self]; ring
  have hoffd : ∑ i, ∑ j, (if i ≠ j then Φ i c * (sgn (x i) * sgn (x j) * A i j) * Φ j d else 0)
      = ∑ i, ∑ j, chaos (fun i j => A i j * Φ i c * Φ j d) x i j := by
    refine Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => ?_))
    unfold chaos
    dsimp only
    split_ifs <;> ring
  rw [hsplit, hdiag2, hoffd] at hA
  rw [hdiagsum]
  linarith

/-- The lower bound of Proposition 6.4 before the dilation step: for some signs, the compression of the
off-diagonal block part stretches every vector by at least `(1 - δ - √2 a k)/2`. Hypotheses: `A` symmetric,
`Φ` has orthonormal columns spanning eigenvectors with eigenvalues `λ_c` of modulus at least one
(`A Φ = Φ diag λ`), off-diagonal entries at most `a`, diagonal entries at most `δ` in modulus. -/
theorem compressed_lower {n k : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hsym : ∀ i j, A j i = A i j)
    (Φ : Matrix (Fin n) (Fin k) ℝ) (hΦ : Φᵀ * Φ = 1) (lam : Fin k → ℝ)
    (hEig : A * Φ = Φ * diagonal lam) (hlam : ∀ c, 1 ≤ |lam c|)
    (a δ : ℝ) (ha : 0 ≤ a) (hδ : 0 ≤ δ)
    (hoff : ∀ i j, i ≠ j → |A i j| ≤ a) (hdiag : ∀ i, |A i i| ≤ δ) :
    ∃ x : Fin n → Bool, ∀ v : Fin k → ℝ,
      (1 - δ - Real.sqrt 2 * a * k) * nrm v ≤ 2 * nrm ((Φᵀ * offBlock A x * Φ) *ᵥ v) := by
  obtain ⟨x, hx⟩ := exists_good_signs A Φ a hsym hoff
  refine ⟨x, fun v => ?_⟩
  have htr : ∑ i, ∑ c, Φ i c ^ 2 = (k:ℝ) := by
    rw [Finset.sum_comm]
    have hcol : ∀ c, ∑ i, Φ i c ^ 2 = 1 := by
      intro c
      have h := congrFun (congrFun hΦ c) c
      simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.one_apply_eq] at h
      simpa [sq] using h
    simp [hcol]
  have hfrob : frob (chaosMat A Φ x) ≤ 2 * a ^ 2 * (k:ℝ) ^ 2 := by
    rw [htr] at hx
    exact hx
  have hΛ : Φᵀ * A * Φ = diagonal lam := by
    rw [Matrix.mul_assoc, hEig, ← Matrix.mul_assoc, hΦ, Matrix.one_mul]
  have hid := compressed_identity A Φ x
  rw [hΛ] at hid
  have hvec : (2:ℝ) • ((Φᵀ * offBlock A x * Φ) *ᵥ v)
      = diagonal lam *ᵥ v - (Φᵀ * diagonal (fun i => A i i) * Φ) *ᵥ v - chaosMat A Φ x *ᵥ v := by
    rw [← smul_mulVec, hid, sub_mulVec, sub_mulVec]
  have h2 : nrm ((2:ℝ) • ((Φᵀ * offBlock A x * Φ) *ᵥ v))
      = 2 * nrm ((Φᵀ * offBlock A x * Φ) *ᵥ v) := by
    rw [nrm_smul]; norm_num
  have b1 : nrm v ≤ nrm (diagonal lam *ᵥ v) := by
    apply Real.sqrt_le_sqrt
    simp only [nsq, dotProduct]
    apply Finset.sum_le_sum
    intro c _
    rw [mulVec_diagonal]
    have h1 : 1 ≤ lam c ^ 2 := by
      have h := hlam c
      rw [← sq_abs]; nlinarith
    nlinarith [mul_self_nonneg (v c)]
  have b2 : nrm ((Φᵀ * diagonal (fun i => A i i) * Φ) *ᵥ v) ≤ δ * nrm v := by
    rw [← mulVec_mulVec, ← mulVec_mulVec]
    calc nrm (Φᵀ *ᵥ (diagonal (fun i => A i i) *ᵥ (Φ *ᵥ v)))
        ≤ nrm (diagonal (fun i => A i i) *ᵥ (Φ *ᵥ v)) := nrm_transpose_mulVec_le Φ hΦ _
      _ ≤ δ * nrm (Φ *ᵥ v) := nrm_diagonal_mulVec_le _ δ hδ hdiag _
      _ = δ * nrm v := by rw [nrm_mulVec_orth Φ hΦ]
  have b3 : nrm (chaosMat A Φ x *ᵥ v) ≤ Real.sqrt 2 * a * k * nrm v := by
    have hc : 0 ≤ Real.sqrt 2 * a * k :=
      mul_nonneg (mul_nonneg (Real.sqrt_nonneg 2) ha) (Nat.cast_nonneg k)
    apply nrm_le_of_nsq_le hc
    have hsq : (Real.sqrt 2 * a * k) ^ 2 = 2 * a ^ 2 * (k:ℝ) ^ 2 := by
      rw [mul_pow, mul_pow, Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)]
    rw [hsq]
    exact (nsq_mulVec_le _ v).trans (mul_le_mul_of_nonneg_right hfrob (nsq_nonneg v))
  have tri := nrm_sub_sub_ge (diagonal lam *ᵥ v) ((Φᵀ * diagonal (fun i => A i i) * Φ) *ᵥ v)
    (chaosMat A Φ x *ᵥ v)
  rw [← hvec, h2] at tri
  nlinarith [b1, b2, b3, tri]

/-- Proposition 6.4 for the full off-diagonal block part: `s_k(C) ≥ (1 - δ - √2 a k)/2`. -/
theorem prop64_offBlock {n k : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hsym : ∀ i j, A j i = A i j)
    (Φ : Matrix (Fin n) (Fin k) ℝ) (hΦ : Φᵀ * Φ = 1) (lam : Fin k → ℝ)
    (hEig : A * Φ = Φ * diagonal lam) (hlam : ∀ c, 1 ≤ |lam c|)
    (a δ : ℝ) (ha : 0 ≤ a) (hδ : 0 ≤ δ)
    (hoff : ∀ i j, i ≠ j → |A i j| ≤ a) (hdiag : ∀ i, |A i i| ≤ δ) :
    ∃ x : Fin n → Bool, ApproxGE k ((1 - δ - Real.sqrt 2 * a * k) / 2) (offBlock A x) := by
  obtain ⟨x, hx⟩ := compressed_lower A hsym Φ hΦ lam hEig hlam a δ ha hδ hoff hdiag
  refine ⟨x, ?_⟩
  have h := approx_compress (offBlock A x) Φ hΦ ((1 - δ - Real.sqrt 2 * a * k) / 2)
    (fun v => by have := hx v; linarith)
  rw [Fintype.card_fin] at h
  exact h

/-- After renaming the coordinates so that `{x = true}` comes first, the off-diagonal block part is the
symmetric dilation of `A_{I,J}`. -/
theorem offBlock_submatrix {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hsym : ∀ i j, A j i = A i j)
    (x : Fin n → Bool) :
    (offBlock A x).submatrix (Equiv.sumCompl (fun i => x i = true)) (Equiv.sumCompl (fun i => x i = true))
      = dil (A.submatrix (Subtype.val : {i // x i = true} → Fin n)
          (Subtype.val : {j // ¬ x j = true} → Fin n)) := by
  ext a b
  rcases a with ⟨i, hi⟩ | ⟨j, hj⟩ <;> rcases b with ⟨i', hi'⟩ | ⟨j', hj'⟩
  · simp [offBlock, dil, hi, hi']
  · have hj2 : x j' = false := by simpa using hj'
    simp [offBlock, dil, hi, hj2]
  · have hj2 : x j = false := by simpa using hj
    simp [offBlock, dil, hj2, hi']
    exact hsym i' j
  · have hj2 : x j = false := by simpa using hj
    have hj3 : x j' = false := by simpa using hj'
    simp [offBlock, dil, hj2, hj3]

/-- Proposition 6.4 (spectral part complete): if `A` is symmetric with `2m - 1` orthonormal eigenvectors whose
eigenvalues have modulus at least one, off-diagonal entries at most `a` and diagonal entries at most `δ` in
modulus, and `1 - δ - √2 a (2m - 1) > 0`, then for some partition `[n] = I ⊔ J`,
`s_m(A_{I,J}) ≥ (1 - δ - √2 a (2m - 1))/2`. -/
theorem prop64 {n m : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hsym : ∀ i j, A j i = A i j)
    (Φ : Matrix (Fin n) (Fin (2 * m - 1)) ℝ) (hΦ : Φᵀ * Φ = 1) (lam : Fin (2 * m - 1) → ℝ)
    (hEig : A * Φ = Φ * diagonal lam) (hlam : ∀ c, 1 ≤ |lam c|)
    (a δ : ℝ) (ha : 0 ≤ a) (hδ : 0 ≤ δ)
    (hoff : ∀ i j, i ≠ j → |A i j| ≤ a) (hdiag : ∀ i, |A i i| ≤ δ)
    (hpos : 0 < 1 - δ - Real.sqrt 2 * a * ((2 * m - 1 : ℕ) : ℝ)) :
    ∃ x : Fin n → Bool, ApproxGE m ((1 - δ - Real.sqrt 2 * a * ((2 * m - 1 : ℕ) : ℝ)) / 2)
      (A.submatrix (Subtype.val : {i // x i = true} → Fin n) (Subtype.val : {j // ¬ x j = true} → Fin n)) := by
  obtain ⟨x, hx⟩ := prop64_offBlock A hsym Φ hΦ lam hEig hlam a δ ha hδ hoff hdiag
  refine ⟨x, ?_⟩
  have h1 := approx_submatrix (offBlock A x) (Equiv.sumCompl (fun i => x i = true)) _ _ hx
  rw [offBlock_submatrix A hsym x] at h1
  exact approx_of_dil _ m _ (by linarith) h1

/-- Without a pivot (Definition 6.1, η = 1/12, ζ = 1/256) every off-diagonal entry is below 5/48. -/
theorem nopivot_entries {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ)
    (hd : ∀ i, |A i i| < 1 / 12) (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256)
    (i j : Fin n) (hij : i ≠ j) : |A i j| ≤ 5 / 48 := by
  have h1 := hd i
  have h2 := hd j
  have h3 := hp i j hij
  have hprod : A i i * A j j ≤ 1 / 144 := by
    have e : |A i i * A j j| = |A i i| * |A j j| := abs_mul _ _
    have h4 : |A i i| * |A j j| ≤ 1 / 12 * (1 / 12) :=
      mul_le_mul h1.le h2.le (abs_nonneg _) (by norm_num)
    have h5 := le_abs_self (A i i * A j j)
    linarith
  have hsq : A i j ^ 2 ≤ (5 / 48) ^ 2 := by
    have h6 := neg_le_abs (A i i * A j j - A i j ^ 2)
    nlinarith
  rw [abs_le]
  constructor <;> nlinarith [hsq]

theorem sqrt_two_lt' : Real.sqrt 2 < 1.4143 := by
  rw [Real.sqrt_lt' (by norm_num)]; norm_num

/-- Proposition 6.4 with the paper's constants, `m = 3`: without a pivot and with five orthonormal
eigenvectors of eigenvalue modulus at least one, some `A_{I,J}` has `s_3(A_{I,J}) ≥ γ_3 > 0.09`. -/
theorem prop64_m3 {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hsym : ∀ i j, A j i = A i j)
    (Φ : Matrix (Fin n) (Fin 5) ℝ) (hΦ : Φᵀ * Φ = 1) (lam : Fin 5 → ℝ)
    (hEig : A * Φ = Φ * diagonal lam) (hlam : ∀ c, 1 ≤ |lam c|)
    (hd : ∀ i, |A i i| < 1 / 12) (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256) :
    ∃ x : Fin n → Bool, ApproxGE 3 (9 / 100)
      (A.submatrix (Subtype.val : {i // x i = true} → Fin n) (Subtype.val : {j // ¬ x j = true} → Fin n)) := by
  have hs := sqrt_two_lt'
  have hpos : 0 < 1 - 1 / 12 - Real.sqrt 2 * (5 / 48) * ((2 * 3 - 1 : ℕ) : ℝ) := by
    norm_num; nlinarith
  obtain ⟨x, hx⟩ := prop64 (m := 3) A hsym Φ hΦ lam hEig hlam (5 / 48) (1 / 12) (by norm_num) (by norm_num)
    (nopivot_entries A hd hp) (fun i => (hd i).le) hpos
  refine ⟨x, hx.mono ?_⟩
  norm_num; nlinarith

/-- Proposition 6.4 with the paper's constants, `m = 2`: three eigenvectors give `s_2(A_{I,J}) ≥ γ_2 > 0.237`. -/
theorem prop64_m2 {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hsym : ∀ i j, A j i = A i j)
    (Φ : Matrix (Fin n) (Fin 3) ℝ) (hΦ : Φᵀ * Φ = 1) (lam : Fin 3 → ℝ)
    (hEig : A * Φ = Φ * diagonal lam) (hlam : ∀ c, 1 ≤ |lam c|)
    (hd : ∀ i, |A i i| < 1 / 12) (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256) :
    ∃ x : Fin n → Bool, ApproxGE 2 (237 / 1000)
      (A.submatrix (Subtype.val : {i // x i = true} → Fin n) (Subtype.val : {j // ¬ x j = true} → Fin n)) := by
  have hs := sqrt_two_lt'
  have hpos : 0 < 1 - 1 / 12 - Real.sqrt 2 * (5 / 48) * ((2 * 2 - 1 : ℕ) : ℝ) := by
    norm_num; nlinarith
  obtain ⟨x, hx⟩ := prop64 (m := 2) A hsym Φ hΦ lam hEig hlam (5 / 48) (1 / 12) (by norm_num) (by norm_num)
    (nopivot_entries A hd hp) (fun i => (hd i).le) hpos
  refine ⟨x, hx.mono ?_⟩
  norm_num; nlinarith

/-- Proposition 6.4 with the paper's constants, `m = 1`: one eigenvector gives `s_1(A_{I,J}) ≥ γ_1 > 0.38`. -/
theorem prop64_m1 {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hsym : ∀ i j, A j i = A i j)
    (Φ : Matrix (Fin n) (Fin 1) ℝ) (hΦ : Φᵀ * Φ = 1) (lam : Fin 1 → ℝ)
    (hEig : A * Φ = Φ * diagonal lam) (hlam : ∀ c, 1 ≤ |lam c|)
    (hd : ∀ i, |A i i| < 1 / 12) (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256) :
    ∃ x : Fin n → Bool, ApproxGE 1 (38 / 100)
      (A.submatrix (Subtype.val : {i // x i = true} → Fin n) (Subtype.val : {j // ¬ x j = true} → Fin n)) := by
  have hs := sqrt_two_lt'
  have hpos : 0 < 1 - 1 / 12 - Real.sqrt 2 * (5 / 48) * ((2 * 1 - 1 : ℕ) : ℝ) := by
    norm_num; nlinarith
  obtain ⟨x, hx⟩ := prop64 (m := 1) A hsym Φ hΦ lam hEig hlam (5 / 48) (1 / 12) (by norm_num) (by norm_num)
    (nopivot_entries A hd hp) (fun i => (hd i).le) hpos
  refine ⟨x, hx.mono ?_⟩
  norm_num; nlinarith


/-! ## From the spectral theorem to the crossing volume

Proposition 6.4 of "Quadratic forms with five large eigenvalues have bounded densities" from the spectral
hypothesis to the crossing volume, using Mathlib's spectral theorem for Hermitian matrices.

* `eigenframe`: a real symmetric matrix with at least `k` eigenvalues (with multiplicity) of modulus at
  least `t` has `k` orthonormal eigenvectors with such eigenvalues. This is the first step of the proof
  of Proposition 6.4 (`N_A(1) ≥ 2m - 1`, that is `s_{2m-1}(A) ≥ 1`).
* `card_eig_of_approx`: if every matrix of rank less than `m` is at operator distance at least `σ > 0`
  from `N`, then `Nᵀ N` has at least `m` eigenvalues at least `σ²`; this is the direction of the
  characterization in Lemma 2.5 that the proof needs, `s_m ≥ σ`.
* `esym_lower`: the elementary symmetric function `e_m` of nonnegative numbers, `m` of which are at least
  `c ≥ 0`, is at least `c^m` (the last line of the proof of Proposition 6.4).
* `prop64_spectral`: Proposition 6.4 for `m = 3, 2, 1` with the paper's definitions: if `A` has no pivot
  and at least `2m - 1` eigenvalues of modulus at least one, then some partition `[n] = I ⊔ J` has
  `E_m(A_{I,J}) = e_m(A_{I,J} A_{I,J}ᵀ) ≥ γ^{2m}` with `γ = 0.09, 0.237, 0.38`.
-/


section Spectral

variable {n : Type*} [Fintype n] [DecidableEq n]

theorem real_star_eq_transpose (M : Matrix n n ℝ) : star M = Mᵀ := by
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_eq_transpose_of_trivial]

/-- The eigenvector matrix of a real symmetric matrix is orthogonal. -/
theorem eigU_orth (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ * (hA.eigenvectorUnitary : Matrix n n ℝ) = 1 := by
  have h := Unitary.coe_star_mul_self hA.eigenvectorUnitary
  rw [real_star_eq_transpose] at h
  exact h

theorem eigU_orth' (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ) * (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ = 1 := by
  have h := Unitary.coe_mul_star_self hA.eigenvectorUnitary
  rw [Unitary.coe_star, real_star_eq_transpose] at h
  exact h

/-- The spectral theorem in the form `A U = U diag(λ)`. -/
theorem eigU_eigen (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    A * (hA.eigenvectorUnitary : Matrix n n ℝ)
      = (hA.eigenvectorUnitary : Matrix n n ℝ) * diagonal hA.eigenvalues := by
  ext i j
  have h := congrFun (hA.mulVec_eigenvectorBasis j) i
  simp only [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul] at h
  rw [Matrix.mul_diagonal, Matrix.mul_apply]
  simp only [IsHermitian.eigenvectorUnitary_apply]
  rw [h, mul_comm]

/-- The first step of Proposition 6.4: `k` eigenvalues of modulus at least `t` give `k` orthonormal
eigenvectors. -/
theorem eigenframe (A : Matrix n n ℝ) (hA : A.IsHermitian) (k : ℕ) (t : ℝ)
    (hk : k ≤ Fintype.card {j // t ≤ |hA.eigenvalues j|}) :
    ∃ (Φ : Matrix n (Fin k) ℝ) (lam : Fin k → ℝ),
      Φᵀ * Φ = 1 ∧ A * Φ = Φ * diagonal lam ∧ ∀ c, t ≤ |lam c| := by
  obtain ⟨f⟩ : Nonempty (Fin k ↪ {j // t ≤ |hA.eigenvalues j|}) :=
    Function.Embedding.nonempty_of_card_le (by simpa using hk)
  obtain ⟨emb, hemb, hS⟩ : ∃ emb : Fin k → n, Function.Injective emb ∧ ∀ c, t ≤ |hA.eigenvalues (emb c)| :=
    ⟨fun c => (f c).val, Subtype.val_injective.comp f.injective, fun c => (f c).property⟩
  refine ⟨(hA.eigenvectorUnitary : Matrix n n ℝ).submatrix id emb, hA.eigenvalues ∘ emb, ?_, ?_, ?_⟩
  · ext c d
    have h := congrFun (congrFun (eigU_orth A hA) (emb c)) (emb d)
    simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.submatrix_apply, id_eq] at h ⊢
    rw [h]
    simp [Matrix.one_apply, hemb.eq_iff]
  · ext i c
    have h := congrFun (congrFun (eigU_eigen A hA) i) (emb c)
    rw [Matrix.mul_diagonal, Matrix.mul_apply] at h
    rw [Matrix.mul_diagonal, Matrix.mul_apply]
    simp only [Matrix.submatrix_apply, id_eq, Function.comp_apply]
    exact h
  · intro c
    exact hS c

/-- The direction of the characterization in Lemma 2.5 used by Proposition 6.4: if every matrix of rank less
than `m` is at operator distance at least `σ > 0` from `N`, then `Nᵀ N` has at least `m` eigenvalues, counted
with multiplicity, that are at least `σ²`. -/
theorem card_eig_of_approx {I J : Type*} [Fintype I] [Fintype J] [DecidableEq I] (N : Matrix J I ℝ)
    (hG : (Nᵀ * N).IsHermitian) (m : ℕ) (σ : ℝ) (hσ : 0 < σ) (h : ApproxGE m σ N) :
    m ≤ Fintype.card {i // σ ^ 2 ≤ hG.eigenvalues i} := by
  by_contra hlt
  push_neg at hlt
  obtain ⟨U, hUU, hUU', hGU⟩ : ∃ U : Matrix I I ℝ,
      Uᵀ * U = 1 ∧ U * Uᵀ = 1 ∧ (Nᵀ * N) * U = U * diagonal hG.eigenvalues :=
    ⟨_, eigU_orth _ hG, eigU_orth' _ hG, eigU_eigen _ hG⟩
  obtain ⟨μ, hμ⟩ : ∃ μ : I → ℝ, μ = hG.eigenvalues := ⟨_, rfl⟩
  rw [← hμ] at hGU hlt
  obtain ⟨s, hs⟩ : ∃ s : I → ℝ, s = fun i => if σ ^ 2 ≤ μ i then 1 else 0 := ⟨_, rfl⟩
  have hrankP : (U * diagonal s * Uᵀ).rank < m := by
    have h1 : (U * diagonal s * Uᵀ).rank ≤ (diagonal s).rank :=
      (rank_mul_le_left _ _).trans (rank_mul_le_right _ _)
    have h2 : (diagonal s).rank = Fintype.card {i // s i ≠ 0} := Matrix.rank_diagonal s
    have h3 : Fintype.card {i // s i ≠ 0} = Fintype.card {i // σ ^ 2 ≤ μ i} := by
      apply Fintype.card_congr
      refine Equiv.subtypeEquivRight (fun i => ?_)
      rw [hs]
      by_cases hi : σ ^ 2 ≤ μ i <;> simp [hi]
    omega
  obtain ⟨v, hv0, hv⟩ := h (N * (U * diagonal s * Uᵀ)) (lt_of_le_of_lt (rank_mul_le_right _ _) hrankP)
  obtain ⟨y, hy⟩ : ∃ y : I → ℝ, y = Uᵀ *ᵥ v := ⟨_, rfl⟩
  obtain ⟨z, hz⟩ : ∃ z : I → ℝ, z = diagonal (fun i => 1 - s i) *ᵥ y := ⟨_, rfl⟩
  have hvU : U *ᵥ y = v := by rw [hy, mulVec_mulVec, hUU', one_mulVec]
  have hmat : N - N * (U * diagonal s * Uᵀ) = N * U * diagonal (fun i => 1 - s i) * Uᵀ := by
    have hd : diagonal (fun i => 1 - s i) = 1 - diagonal s := by
      ext i j
      by_cases hij : i = j
      · subst hij; simp
      · simp [Matrix.one_apply, hij]
    rw [hd, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one]
    simp only [Matrix.mul_assoc, hUU', Matrix.mul_one]
  have hvec : (N - N * (U * diagonal s * Uᵀ)) *ᵥ v = N *ᵥ (U *ᵥ z) := by
    rw [hmat, ← mulVec_mulVec, ← mulVec_mulVec, ← mulVec_mulVec, ← hy, ← hz]
  have hB : nsq (N *ᵥ (U *ᵥ z)) = ∑ i, μ i * (z i * z i) := by
    rw [nsq, dotProduct_mulVec, ← mulVec_transpose, mulVec_mulVec, mulVec_mulVec, hGU,
      ← mulVec_mulVec, dotProduct_mulVec, ← mulVec_transpose, mulVec_mulVec, hUU, one_mulVec]
    simp only [dotProduct, mulVec_diagonal]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    ring
  have hC : nsq v = ∑ i, y i * y i := by
    calc nsq v = nsq (U *ᵥ y) := by rw [hvU]
      _ = nsq y := nsq_mulVec_orth U hUU y
      _ = ∑ i, y i * y i := rfl
  have hzi : ∀ i, z i = (1 - s i) * y i := by
    intro i; rw [hz, mulVec_diagonal]
  have hterm : ∀ i, 0 ≤ σ ^ 2 * (y i * y i) - μ i * (z i * z i) := by
    intro i
    rw [hzi i, hs]
    by_cases hi : σ ^ 2 ≤ μ i
    · simp only [if_pos hi]
      nlinarith [mul_self_nonneg (y i), sq_nonneg σ]
    · simp only [if_neg hi]
      push_neg at hi
      nlinarith [mul_nonneg (sub_nonneg.mpr hi.le) (mul_self_nonneg (y i))]
  have hy0 : y ≠ 0 := by
    intro h0
    apply hv0
    rw [← hvU, h0, mulVec_zero]
  obtain ⟨j0, hj0⟩ : ∃ j, y j ≠ 0 := by
    by_contra hc
    push_neg at hc
    exact hy0 (funext hc)
  have hpos : 0 < σ ^ 2 * (y j0 * y j0) - μ j0 * (z j0 * z j0) := by
    rw [hzi j0, hs]
    have hyy : 0 < y j0 * y j0 := mul_self_pos.mpr hj0
    by_cases hi : σ ^ 2 ≤ μ j0
    · simp only [if_pos hi]
      nlinarith [pow_pos hσ 2]
    · simp only [if_neg hi]
      push_neg at hi
      nlinarith [mul_pos (sub_pos.mpr hi) hyy]
  have hsum : 0 < ∑ i, (σ ^ 2 * (y i * y i) - μ i * (z i * z i)) :=
    Finset.sum_pos' (fun i _ => hterm i) ⟨j0, Finset.mem_univ _, hpos⟩
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum] at hsum
  have hsq : σ ^ 2 * nsq v ≤ nsq ((N - N * (U * diagonal s * Uᵀ)) *ᵥ v) := by
    have h0 : 0 ≤ σ * nrm v := mul_nonneg hσ.le (nrm_nonneg v)
    have h1 := pow_le_pow_left₀ h0 hv 2
    rw [mul_pow, nrm_sq, nrm_sq] at h1
    exact h1
  rw [hvec, hB, hC] at hsq
  linarith

/-- `e_m` of nonnegative numbers of which at least `m` are at least `c ≥ 0` is at least `c^m`. -/
theorem esym_lower {ι : Type*} [Fintype ι] [DecidableEq ι] (μ : ι → ℝ) (m : ℕ) (c : ℝ) (hc : 0 ≤ c)
    (hμ : ∀ i, 0 ≤ μ i) (hcard : m ≤ Fintype.card {i // c ≤ μ i}) :
    c ^ m ≤ ∑ t ∈ Finset.univ.powersetCard m, ∏ i ∈ t, μ i := by
  have hc' : m ≤ (Finset.univ.filter (fun i => c ≤ μ i)).card := by
    rw [Fintype.card_subtype] at hcard; exact hcard
  obtain ⟨T, hTS, hTc⟩ := Finset.exists_subset_card_eq hc'
  have hT : T ∈ Finset.univ.powersetCard m :=
    Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, hTc⟩
  calc c ^ m = ∏ _i ∈ T, c := by rw [Finset.prod_const, hTc]
    _ ≤ ∏ i ∈ T, μ i :=
        Finset.prod_le_prod (fun _ _ => hc) (fun i hi => (Finset.mem_filter.mp (hTS hi)).2)
    _ ≤ ∑ t ∈ Finset.univ.powersetCard m, ∏ i ∈ t, μ i :=
        Finset.single_le_sum (f := fun t => ∏ i ∈ t, μ i)
          (fun t _ => Finset.prod_nonneg (fun i _ => hμ i)) hT

end Spectral

/-! ## Proposition 6.4 with the paper's definitions -/

/-- The block `A_{I,J}` for the partition `I = {x = true}`, `J = {x = false}`. -/
def blk {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (x : Fin n → Bool) :
    Matrix {i // x i = true} {j // ¬ x j = true} ℝ :=
  A.submatrix Subtype.val Subtype.val

/-- `E_m(M) = e_m(M Mᵀ)`, the `m`-th elementary symmetric function of the eigenvalues of `M Mᵀ`. -/
noncomputable def Evol {I J : Type*} [Fintype I] [Fintype J] [DecidableEq I] (M : Matrix I J ℝ)
    (hG : (M * Mᵀ).IsHermitian) (m : ℕ) : ℝ :=
  ∑ t ∈ Finset.univ.powersetCard m, ∏ i ∈ t, hG.eigenvalues i

theorem approx_transpose {I J : Type*} [Fintype I] [Fintype J] (M : Matrix I J ℝ) (m : ℕ) (σ : ℝ)
    (hσ : 0 < σ) (h : ApproxGE m σ M) : ApproxGE m σ Mᵀ := by
  intro R hR
  have hR' : Rᵀ.rank < m := by rw [Matrix.rank_transpose]; exact hR
  obtain ⟨v, hv0, hv⟩ := h Rᵀ hR'
  have e : M - Rᵀ = (Mᵀ - R)ᵀ := by rw [Matrix.transpose_sub, Matrix.transpose_transpose]
  rw [e] at hv
  exact transpose_stretch (Mᵀ - R) σ hσ v hv0 hv

/-- From `s_m(M) ≥ σ` in the approximation-number form to `E_m(M) ≥ σ^{2m}`. -/
theorem evol_of_approx {I J : Type*} [Fintype I] [Fintype J] [DecidableEq I] (M : Matrix I J ℝ)
    (hG : (M * Mᵀ).IsHermitian) (m : ℕ) (σ : ℝ) (hσ : 0 < σ) (h : ApproxGE m σ M) :
    σ ^ (2 * m) ≤ Evol M hG m := by
  have hcard : m ≤ Fintype.card {i // σ ^ 2 ≤ hG.eigenvalues i} :=
    card_eig_of_approx (N := Mᵀ) hG m σ hσ (approx_transpose M m σ hσ h)
  have hpsd : (M * Mᵀ).PosSemidef := by
    have := Matrix.posSemidef_self_mul_conjTranspose M
    rwa [Matrix.conjTranspose_eq_transpose_of_trivial] at this
  have hnn : ∀ i, 0 ≤ hG.eigenvalues i := fun i => hpsd.eigenvalues_nonneg i
  rw [pow_mul]
  exact esym_lower hG.eigenvalues m (σ ^ 2) (sq_nonneg σ) hnn hcard

/-- Proposition 6.4, `m = 3`, from the spectral hypothesis: if `A` is real symmetric with no pivot and at
least five eigenvalues of modulus at least one, then for some partition `E_3(A_{I,J}) ≥ 0.09^6`. -/
theorem prop64_spectral_m3 {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hA : A.IsHermitian)
    (h5 : 5 ≤ Fintype.card {j // 1 ≤ |hA.eigenvalues j|})
    (hd : ∀ i, |A i i| < 1 / 12) (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256) :
    ∃ x : Fin n → Bool, ApproxGE 3 (9 / 100) (blk A x) ∧
      ∀ hG : (blk A x * (blk A x)ᵀ).IsHermitian, (9 / 100 : ℝ) ^ 6 ≤ Evol (blk A x) hG 3 := by
  have hsym : ∀ i j, A j i = A i j := fun i j => by simpa using hA.apply i j
  obtain ⟨Φ, lam, hΦ, hEig, hlam⟩ := eigenframe A hA 5 1 h5
  obtain ⟨x, hx⟩ := prop64_m3 A hsym Φ hΦ lam hEig hlam hd hp
  refine ⟨x, hx, fun hG => ?_⟩
  have := evol_of_approx (blk A x) hG 3 (9 / 100) (by norm_num) hx
  simpa using this

/-- Proposition 6.4, `m = 2`: three eigenvalues of modulus at least one give `E_2(A_{I,J}) ≥ 0.237^4`. -/
theorem prop64_spectral_m2 {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hA : A.IsHermitian)
    (h3 : 3 ≤ Fintype.card {j // 1 ≤ |hA.eigenvalues j|})
    (hd : ∀ i, |A i i| < 1 / 12) (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256) :
    ∃ x : Fin n → Bool, ApproxGE 2 (237 / 1000) (blk A x) ∧
      ∀ hG : (blk A x * (blk A x)ᵀ).IsHermitian, (237 / 1000 : ℝ) ^ 4 ≤ Evol (blk A x) hG 2 := by
  have hsym : ∀ i j, A j i = A i j := fun i j => by simpa using hA.apply i j
  obtain ⟨Φ, lam, hΦ, hEig, hlam⟩ := eigenframe A hA 3 1 h3
  obtain ⟨x, hx⟩ := prop64_m2 A hsym Φ hΦ lam hEig hlam hd hp
  refine ⟨x, hx, fun hG => ?_⟩
  have := evol_of_approx (blk A x) hG 2 (237 / 1000) (by norm_num) hx
  simpa using this

/-- Proposition 6.4, `m = 1`: one eigenvalue of modulus at least one gives `E_1(A_{I,J}) ≥ 0.38^2`. -/
theorem prop64_spectral_m1 {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ) (hA : A.IsHermitian)
    (h1 : 1 ≤ Fintype.card {j // 1 ≤ |hA.eigenvalues j|})
    (hd : ∀ i, |A i i| < 1 / 12) (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256) :
    ∃ x : Fin n → Bool, ApproxGE 1 (38 / 100) (blk A x) ∧
      ∀ hG : (blk A x * (blk A x)ᵀ).IsHermitian, (38 / 100 : ℝ) ^ 2 ≤ Evol (blk A x) hG 1 := by
  have hsym : ∀ i j, A j i = A i j := fun i j => by simpa using hA.apply i j
  obtain ⟨Φ, lam, hΦ, hEig, hlam⟩ := eigenframe A hA 1 1 h1
  obtain ⟨x, hx⟩ := prop64_m1 A hsym Φ hΦ lam hEig hlam hd hp
  refine ⟨x, hx, fun hG => ?_⟩
  have := evol_of_approx (blk A x) hG 1 (38 / 100) (by norm_num) hx
  simpa using this

end QformFive
