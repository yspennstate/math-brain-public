import Mathlib.Tactic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.Order.Chebyshev

/-!
Formal checks of the random sign argument of Section 6 of "Quadratic forms with five large
eigenvalues have bounded densities": Lemma 6.2(a) (the identity A - DAD = 2C), the fourth moment of
independent signs, the second moment of the sign chaos in Lemma 6.3 (as an exact finite average over
all 2^n sign vectors), the Frobenius form of Lemma 6.3 and its bound 2 a^2 (sum |phi_i|^2)^2, and the
averaging step of Proposition 6.4. Sign vectors are functions Fin n -> Bool, read through sgn.
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

end QformFive
