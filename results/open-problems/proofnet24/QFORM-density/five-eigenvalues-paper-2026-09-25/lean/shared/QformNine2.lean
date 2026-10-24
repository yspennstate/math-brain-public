import Mathlib.Tactic
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Gamma.BohrMollerup
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Analysis.Convex.Jensen
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Data.Finset.Powerset

/-!
Second group of formal checks for "Quadratic forms with nine large eigenvalues have bounded densities":
the constant of Lemma 5.4 (through the Gamma function), the monotonicity used in the proof of Theorem 4.1,
the determinant identities of Lemmas 2.8 and 6.2, and Lemma 4.2 (the entropy inequality).
-/

open Real Finset

namespace QformNine

/-! ## Lemma 5.4: the constant 2 e^{1/4} (sqrt2 pi e)^{1/2} Gamma(1/4) pi^{-1/2} < 19 -/

/-- Log-convexity of Gamma between 1 and 3/2: Gamma(5/4) <= sqrt(Gamma(3/2)) = sqrt(sqrt pi / 2). -/
theorem gamma_five_quarters_le : Real.Gamma (5/4) ≤ Real.sqrt (Real.sqrt π / 2) := by
  have h := Real.convexOn_log_Gamma.2 (show (1:ℝ) ∈ Set.Ioi 0 by norm_num)
    (show (3/2:ℝ) ∈ Set.Ioi 0 by norm_num) (show (0:ℝ) ≤ 1/2 by norm_num) (show (0:ℝ) ≤ 1/2 by norm_num)
    (show (1/2:ℝ) + 1/2 = 1 by norm_num)
  simp only [Function.comp_apply, smul_eq_mul] at h
  rw [show (1/2:ℝ) * 1 + 1/2 * (3/2) = 5/4 by norm_num, Real.Gamma_one, Real.log_one] at h
  have hG32 : Real.Gamma (3/2) = Real.sqrt π / 2 := by
    rw [show (3/2:ℝ) = 1/2 + 1 by norm_num, Real.Gamma_add_one (by norm_num), Real.Gamma_one_half_eq]
    ring
  rw [hG32] at h
  have hpos : 0 < Real.Gamma (5/4) := Real.Gamma_pos_of_pos (by norm_num)
  have hq : 0 < Real.sqrt π / 2 := by positivity
  have hlog : Real.log (Real.Gamma (5/4)) ≤ Real.log (Real.sqrt (Real.sqrt π / 2)) := by
    rw [Real.log_sqrt hq.le]; linarith
  exact (Real.log_le_log_iff hpos (Real.sqrt_pos.mpr hq)).mp hlog

/-- Gamma(1/4) = 4 Gamma(5/4) <= 4 sqrt(sqrt pi / 2). -/
theorem gamma_quarter_le : Real.Gamma (1/4) ≤ 4 * Real.sqrt (Real.sqrt π / 2) := by
  have h := Real.Gamma_add_one (s := (1/4:ℝ)) (by norm_num)
  rw [show (1/4:ℝ) + 1 = 5/4 by norm_num] at h
  have := gamma_five_quarters_le
  linarith

/-- Lemma 5.4: the constant of the concentration inequality is less than 19. -/
theorem concentration_constant_lt :
    2 * Real.exp (1/4) * Real.sqrt (Real.sqrt 2 * π * Real.exp 1) * Real.Gamma (1/4) / Real.sqrt π < 19 := by
  set G := Real.Gamma (1/4) with hGdef
  have hG0 : 0 < G := Real.Gamma_pos_of_pos (by norm_num)
  have hG : G ≤ 4 * Real.sqrt (Real.sqrt π / 2) := gamma_quarter_le
  have hsp : 0 < Real.sqrt π := Real.sqrt_pos.mpr Real.pi_pos
  have e4 : Real.exp (1/4) ^ 4 = Real.exp 1 := by rw [← Real.exp_nat_mul]; norm_num
  have s4 : Real.sqrt (Real.sqrt 2 * π * Real.exp 1) ^ 4 = 2 * π^2 * (Real.exp 1)^2 := by
    have h1 : Real.sqrt (Real.sqrt 2 * π * Real.exp 1) ^ 2 = Real.sqrt 2 * π * Real.exp 1 :=
      Real.sq_sqrt (by positivity)
    have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
    calc Real.sqrt (Real.sqrt 2 * π * Real.exp 1) ^ 4
        = (Real.sqrt (Real.sqrt 2 * π * Real.exp 1) ^ 2)^2 := by ring
      _ = (Real.sqrt 2 * π * Real.exp 1)^2 := by rw [h1]
      _ = Real.sqrt 2 ^ 2 * π^2 * (Real.exp 1)^2 := by ring
      _ = 2 * π^2 * (Real.exp 1)^2 := by rw [h2]
  have p4 : Real.sqrt π ^ 4 = π^2 := by
    have h1 : Real.sqrt π ^ 2 = π := Real.sq_sqrt Real.pi_pos.le
    calc Real.sqrt π ^ 4 = (Real.sqrt π ^ 2)^2 := by ring
      _ = π^2 := by rw [h1]
  have G4 : G^4 ≤ 64 * π := by
    have h2 : Real.sqrt (Real.sqrt π / 2) ^ 2 = Real.sqrt π / 2 := Real.sq_sqrt (by positivity)
    have h3 : Real.sqrt π ^ 2 = π := Real.sq_sqrt Real.pi_pos.le
    calc G^4 ≤ (4 * Real.sqrt (Real.sqrt π / 2))^4 := by gcongr
      _ = 256 * (Real.sqrt (Real.sqrt π / 2)^2)^2 := by ring
      _ = 256 * (Real.sqrt π / 2)^2 := by rw [h2]
      _ = 64 * Real.sqrt π ^ 2 := by ring
      _ = 64 * π := by rw [h3]
  set K := 2 * Real.exp (1/4) * Real.sqrt (Real.sqrt 2 * π * Real.exp 1) * G / Real.sqrt π with hK
  have hK0 : 0 ≤ K := by positivity
  have K4 : K^4 = 32 * Real.exp 1 ^ 3 * G^4 := by
    rw [hK, div_pow, mul_pow, mul_pow, mul_pow, e4, s4, p4]
    have : (π:ℝ)^2 ≠ 0 := by positivity
    field_simp
    ring
  have he3 : Real.exp 1 ^ 3 < 2.7182818286 ^ 3 := by gcongr; exact exp_one_lt_d9
  have hpi := pi_lt_d2
  have hprod : Real.exp 1 ^ 3 * π < 2.7182818286 ^ 3 * 3.15 :=
    mul_lt_mul'' he3 hpi (by positivity) Real.pi_pos.le
  have hK4 : K^4 < 19^4 := by
    rw [K4]
    calc 32 * Real.exp 1 ^ 3 * G^4 ≤ 32 * Real.exp 1 ^ 3 * (64 * π) := by gcongr
      _ = 2048 * (Real.exp 1 ^ 3 * π) := by ring
      _ < 2048 * (2.7182818286 ^ 3 * 3.15) := by linarith
      _ < 19^4 := by norm_num
  exact lt_of_pow_lt_pow_left₀ 4 (by norm_num) hK4

/-! ## Theorem 4.1: the monotonicity of the branch constants -/

/-- With omega(m) = m^m/m!, omega(k) <= omega(k+1); this is the step a_{k+1} <= e^{-1/2} a_k. -/
theorem omega_step (k : ℕ) :
    (k:ℝ)^k / (k.factorial:ℝ) ≤ ((k:ℝ)+1)^(k+1) / ((k+1).factorial : ℝ) := by
  rw [Nat.factorial_succ]
  push_cast
  have hk : (0:ℝ) < k.factorial := by exact_mod_cast Nat.factorial_pos k
  rw [div_le_div_iff₀ hk (by positivity)]
  have hp : (k:ℝ)^k ≤ ((k:ℝ)+1)^k := pow_le_pow_left₀ (by positivity) (by linarith) k
  calc (k:ℝ)^k * (((k:ℝ)+1) * k.factorial) ≤ ((k:ℝ)+1)^k * (((k:ℝ)+1) * k.factorial) := by gcongr
    _ = ((k:ℝ)+1)^(k+1) * k.factorial := by ring

/-! ## Lemmas 2.8 and 6.2: determinant identities -/

/-- Lemma 6.2: the bordered determinant, det [[B, u], [v, a]] = det B * det(a - v B^{-1} u). -/
theorem bordered_det {r : ℕ} (B : Matrix (Fin r) (Fin r) ℝ) [Invertible B]
    (u : Matrix (Fin r) (Fin 1) ℝ) (v : Matrix (Fin 1) (Fin r) ℝ) (a : Matrix (Fin 1) (Fin 1) ℝ) :
    (Matrix.fromBlocks B u v a).det = B.det * (a - v * ⅟B * u).det :=
  Matrix.det_fromBlocks₁₁ B u v a

/-- Lemma 2.8(b): for rows N (independent) and T, the Gram determinant of the stacked rows factors as
det(N N^T) * det(C C^T) with C = T (1 - Pi), Pi = N^T (N N^T)^{-1} N. -/
theorem gram_factor {k l d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ) (T : Matrix (Fin l) (Fin d) ℝ)
    [Invertible (N * N.transpose)] :
    (Matrix.fromBlocks (N * N.transpose) (N * T.transpose) (T * N.transpose) (T * T.transpose)).det
      = (N * N.transpose).det *
        ((T * ((1 : Matrix (Fin d) (Fin d) ℝ) - N.transpose * ⅟(N * N.transpose) * N)) *
          (T * ((1 : Matrix (Fin d) (Fin d) ℝ) - N.transpose * ⅟(N * N.transpose) * N)).transpose).det := by
  rw [Matrix.det_fromBlocks₁₁]
  congr 2
  have hGsymm : (N * N.transpose).transpose = N * N.transpose := by
    rw [Matrix.transpose_mul, Matrix.transpose_transpose]
  have hinvsymm : (⅟(N * N.transpose)).transpose = ⅟(N * N.transpose) := by
    have h1 : (N * N.transpose) * (⅟(N * N.transpose)).transpose = 1 := by
      have h0 := congrArg Matrix.transpose (invOf_mul_self (N * N.transpose))
      rw [Matrix.transpose_mul, Matrix.transpose_one, hGsymm] at h0
      exact h0
    calc (⅟(N * N.transpose)).transpose
        = ⅟(N * N.transpose) * ((N * N.transpose) * (⅟(N * N.transpose)).transpose) := by
          rw [← Matrix.mul_assoc, invOf_mul_self, Matrix.one_mul]
      _ = ⅟(N * N.transpose) := by rw [h1, Matrix.mul_one]
  have hPiT : (N.transpose * ⅟(N * N.transpose) * N).transpose = N.transpose * ⅟(N * N.transpose) * N := by
    rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose, hinvsymm, Matrix.mul_assoc]
  have hPi2 : (N.transpose * ⅟(N * N.transpose) * N) * (N.transpose * ⅟(N * N.transpose) * N)
      = N.transpose * ⅟(N * N.transpose) * N := by
    calc (N.transpose * ⅟(N * N.transpose) * N) * (N.transpose * ⅟(N * N.transpose) * N)
        = N.transpose * ⅟(N * N.transpose) * (N * N.transpose) * ⅟(N * N.transpose) * N := by
          simp only [Matrix.mul_assoc]
      _ = N.transpose * ⅟(N * N.transpose) * N := by
          rw [Matrix.mul_assoc N.transpose (⅟(N * N.transpose)) (N * N.transpose), invOf_mul_self,
            Matrix.mul_one]
  rw [Matrix.transpose_mul, Matrix.transpose_sub, Matrix.transpose_one, hPiT]
  have hidem : (1 - N.transpose * ⅟(N * N.transpose) * N) * (1 - N.transpose * ⅟(N * N.transpose) * N)
      = 1 - N.transpose * ⅟(N * N.transpose) * N := by
    rw [Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one, Matrix.one_mul, hPi2]
    abel
  calc T * T.transpose - T * N.transpose * ⅟(N * N.transpose) * (N * T.transpose)
      = T * (1 - N.transpose * ⅟(N * N.transpose) * N) * T.transpose := by
        rw [Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one]
        simp only [Matrix.mul_assoc]
    _ = T * ((1 - N.transpose * ⅟(N * N.transpose) * N) * (1 - N.transpose * ⅟(N * N.transpose) * N))
          * T.transpose := by rw [hidem]
    _ = T * (1 - N.transpose * ⅟(N * N.transpose) * N)
          * ((1 - N.transpose * ⅟(N * N.transpose) * N) * T.transpose) := by
        simp only [Matrix.mul_assoc]

/-! ## Lemma 4.2: the entropy inequality -/

/-- (S + a)^(k+1) >= S^(k+1) + (k+1) a S^k for S, a >= 0. -/
theorem pow_succ_ge (S a : ℝ) (hS : 0 ≤ S) (ha : 0 ≤ a) :
    ∀ k : ℕ, S^(k+1) + (k+1) * a * S^k ≤ (S + a)^(k+1) := by
  intro k
  induction k with
  | zero => simp
  | succ k ih =>
    have h1 : 0 ≤ S^k := pow_nonneg hS k
    have h2 : 0 ≤ S + a := by linarith
    push_cast at ih ⊢
    calc S^(k+2) + (k+1+1) * a * S^(k+1)
        ≤ (S + a) * (S^(k+1) + (k+1) * a * S^k) := by
          have hnn : 0 ≤ (k+1:ℝ) * a * a * S^k := by positivity
          have expand : (S + a) * (S^(k+1) + (k+1) * a * S^k)
              = S^(k+2) + (k+1+1) * a * S^(k+1) + (k+1) * a * a * S^k := by ring
          linarith [expand, hnn]
      _ ≤ (S + a) * (S + a)^(k+1) := by gcongr
      _ = (S + a)^(k+2) := by ring

/-- m! e_m(a) <= (sum of a)^m for nonnegative a, where e_m is the m-th elementary symmetric function
(the sum over m-subsets of the products). -/
theorem factorial_mul_esymm_le {ι : Type*} [DecidableEq ι] (s : Finset ι) (a : ι → ℝ)
    (ha : ∀ i ∈ s, 0 ≤ a i) :
    ∀ m : ℕ, (m.factorial : ℝ) * ∑ T ∈ s.powersetCard m, ∏ i ∈ T, a i ≤ (∑ i ∈ s, a i) ^ m := by
  induction s using Finset.induction_on with
  | empty =>
    intro m
    cases m with
    | zero => simp
    | succ k =>
      rw [Finset.powersetCard_eq_empty.mpr (by simp)]
      simp
  | insert j s hj ih =>
    intro m
    have ha' : ∀ i ∈ s, 0 ≤ a i := fun i hi => ha i (Finset.mem_insert_of_mem hi)
    have haj : 0 ≤ a j := ha j (Finset.mem_insert_self j s)
    have hS : 0 ≤ ∑ i ∈ s, a i := Finset.sum_nonneg ha'
    have IH := ih ha'
    cases m with
    | zero => simp
    | succ k =>
      rw [Finset.powersetCard_succ_insert hj, Finset.sum_union]
      · rw [Finset.sum_image]
        · have hins : ∀ T ∈ s.powersetCard k, ∏ i ∈ insert j T, a i = a j * ∏ i ∈ T, a i := by
            intro T hT
            have hjT : j ∉ T := fun h => hj ((Finset.mem_powersetCard.mp hT).1 h)
            exact Finset.prod_insert hjT
          rw [Finset.sum_congr rfl hins, ← Finset.mul_sum, Finset.sum_insert hj]
          have h1 := IH (k+1)
          have h2 := IH k
          have hb := pow_succ_ge (∑ i ∈ s, a i) (a j) hS haj k
          have hfac : ((k+1).factorial : ℝ) = (k+1) * (k.factorial : ℝ) := by
            rw [Nat.factorial_succ]; push_cast; ring
          have hE : 0 ≤ ∑ T ∈ s.powersetCard k, ∏ i ∈ T, a i :=
            Finset.sum_nonneg (fun T hT => Finset.prod_nonneg (fun i hi =>
              ha' i ((Finset.mem_powersetCard.mp hT).1 hi)))
          rw [add_comm (a j) (∑ i ∈ s, a i)]
          calc ((k+1).factorial : ℝ) * (∑ T ∈ s.powersetCard (k+1), ∏ i ∈ T, a i
                + a j * ∑ T ∈ s.powersetCard k, ∏ i ∈ T, a i)
              = ((k+1).factorial : ℝ) * ∑ T ∈ s.powersetCard (k+1), ∏ i ∈ T, a i
                + (k+1) * a j * ((k.factorial : ℝ) * ∑ T ∈ s.powersetCard k, ∏ i ∈ T, a i) := by
                rw [hfac]; ring
            _ ≤ (∑ i ∈ s, a i)^(k+1) + (k+1) * a j * (∑ i ∈ s, a i)^k := by
                have : 0 ≤ ((k:ℝ)+1) * a j := by positivity
                gcongr
            _ ≤ ((∑ i ∈ s, a i) + a j)^(k+1) := hb
        · intro T hT U hU hTU
          have hjT : j ∉ T := fun h => hj ((Finset.mem_powersetCard.mp (Finset.mem_coe.mp hT)).1 h)
          have hjU : j ∉ U := fun h => hj ((Finset.mem_powersetCard.mp (Finset.mem_coe.mp hU)).1 h)
          have := congrArg (fun X => X.erase j) hTU
          simpa [Finset.erase_insert hjT, Finset.erase_insert hjU] using this
      · rw [Finset.disjoint_left]
        intro T hT hT'
        obtain ⟨U, _, rfl⟩ := Finset.mem_image.mp hT'
        exact hj ((Finset.mem_powersetCard.mp hT).1 (Finset.mem_insert_self j U))

/-- Lemma 4.2. Let w be a probability distribution on the m-subsets of s and alpha_i = sum of w_T over T
containing i. Then H(w) + sum_i alpha_i log alpha_i <= log(m^m/m!). -/
theorem entropy_lemma {ι : Type*} [DecidableEq ι] (s : Finset ι) (m : ℕ) (hm : 1 ≤ m)
    (w : Finset ι → ℝ) (hw0 : ∀ T ∈ s.powersetCard m, 0 ≤ w T)
    (hw1 : ∑ T ∈ s.powersetCard m, w T = 1) :
    -(∑ T ∈ s.powersetCard m, w T * Real.log (w T)) +
      ∑ i ∈ s, (∑ T ∈ (s.powersetCard m).filter (fun T => i ∈ T), w T) *
        Real.log (∑ T ∈ (s.powersetCard m).filter (fun T => i ∈ T), w T)
      ≤ Real.log ((m:ℝ)^m / (m.factorial : ℝ)) := by
  set P := s.powersetCard m with hP
  set α : ι → ℝ := fun i => ∑ T ∈ P.filter (fun T => i ∈ T), w T with hα
  have hα0 : ∀ i, 0 ≤ α i := fun i => Finset.sum_nonneg (fun T hT => hw0 T (Finset.mem_filter.mp hT).1)
  -- alpha_i >= w_T whenever i in T
  have hαge : ∀ T ∈ P, ∀ i ∈ T, w T ≤ α i := by
    intro T hT i hi
    exact Finset.single_le_sum (f := w) (fun U hU => hw0 U (Finset.mem_filter.mp hU).1)
      (Finset.mem_filter.mpr ⟨hT, hi⟩)
  -- exchange of sums: sum_i alpha_i log alpha_i = sum_T w_T sum_{i in T} log alpha_i
  have hmem : ∀ i T, (i ∈ s ∧ T ∈ P.filter (fun T => i ∈ T)) ↔ (i ∈ T ∧ T ∈ P) := by
    intro i T
    constructor
    · rintro ⟨_, hT⟩
      exact ⟨(Finset.mem_filter.mp hT).2, (Finset.mem_filter.mp hT).1⟩
    · rintro ⟨hiT, hTP⟩
      exact ⟨(Finset.mem_powersetCard.mp hTP).1 hiT, Finset.mem_filter.mpr ⟨hTP, hiT⟩⟩
  have hswap : ∑ i ∈ s, α i * Real.log (α i) = ∑ T ∈ P, w T * ∑ i ∈ T, Real.log (α i) := by
    calc ∑ i ∈ s, α i * Real.log (α i)
        = ∑ i ∈ s, ∑ T ∈ P.filter (fun T => i ∈ T), w T * Real.log (α i) := by
          refine Finset.sum_congr rfl (fun i _ => ?_)
          rw [Finset.sum_mul]
      _ = ∑ T ∈ P, ∑ i ∈ T, w T * Real.log (α i) := Finset.sum_comm' hmem
      _ = ∑ T ∈ P, w T * ∑ i ∈ T, Real.log (α i) := by
          refine Finset.sum_congr rfl (fun T _ => ?_)
          rw [Finset.mul_sum]
  -- sum_i alpha_i = m
  have hsumα : ∑ i ∈ s, α i = m := by
    have : ∑ i ∈ s, α i = ∑ T ∈ P, w T * (T.card : ℝ) := by
      calc ∑ i ∈ s, α i = ∑ i ∈ s, ∑ T ∈ P.filter (fun T => i ∈ T), w T := rfl
        _ = ∑ T ∈ P, ∑ i ∈ T, w T := Finset.sum_comm' hmem
        _ = ∑ T ∈ P, w T * (T.card : ℝ) := by
            refine Finset.sum_congr rfl (fun T _ => ?_)
            rw [Finset.sum_const, nsmul_eq_mul, mul_comm]
    rw [this]
    have hc : ∀ T ∈ P, w T * (T.card : ℝ) = w T * m := by
      intro T hT; rw [(Finset.mem_powersetCard.mp hT).2]
    rw [Finset.sum_congr rfl hc, ← Finset.sum_mul, hw1, one_mul]
  -- the left side as a Jensen sum over sets with positive weight
  set Q := P.filter (fun T => 0 < w T) with hQ
  have hzero : ∀ T ∈ P, T ∉ Q → w T = 0 := by
    intro T hT hTQ
    have := hw0 T hT
    by_contra hne
    exact hTQ (Finset.mem_filter.mpr ⟨hT, lt_of_le_of_ne this (Ne.symm hne)⟩)
  have hQsub : Q ⊆ P := Finset.filter_subset _ _
  have hsplit : ∀ f : Finset ι → ℝ, (∀ T ∈ P, w T = 0 → f T = 0) → ∑ T ∈ P, f T = ∑ T ∈ Q, f T := by
    intro f hf
    rw [← Finset.sum_subset hQsub (fun T hT hTQ => hf T hT (hzero T hT hTQ))]
  have hLHS : -(∑ T ∈ P, w T * Real.log (w T)) + ∑ i ∈ s, α i * Real.log (α i)
      = ∑ T ∈ Q, w T * Real.log ((∏ i ∈ T, α i) / w T) := by
    rw [hswap, ← Finset.sum_neg_distrib, ← Finset.sum_add_distrib]
    rw [hsplit _ (fun T hT h0 => by simp [h0])]
    refine Finset.sum_congr rfl (fun T hT => ?_)
    have hwT : 0 < w T := (Finset.mem_filter.mp hT).2
    have hTP : T ∈ P := (Finset.mem_filter.mp hT).1
    have hpos : ∀ i ∈ T, 0 < α i := fun i hi => lt_of_lt_of_le hwT (hαge T hTP i hi)
    rw [Real.log_div (Finset.prod_ne_zero_iff.mpr (fun i hi => (hpos i hi).ne')) hwT.ne',
      Real.log_prod (fun i hi => (hpos i hi).ne')]
    ring
  rw [hLHS]
  -- Jensen for the concave logarithm
  have hwQ1 : ∑ T ∈ Q, w T = 1 := by rw [← hsplit w (fun T hT h0 => h0), hw1]
  have hJ := (StrictConcaveOn.concaveOn strictConcaveOn_log_Ioi).le_map_sum
    (t := Q) (w := w) (p := fun T => (∏ i ∈ T, α i) / w T)
    (fun T hT => ((Finset.mem_filter.mp hT).2).le) hwQ1
    (fun T hT => by
      have hwT : 0 < w T := (Finset.mem_filter.mp hT).2
      have hTP : T ∈ P := (Finset.mem_filter.mp hT).1
      exact Set.mem_Ioi.mpr (div_pos (Finset.prod_pos (fun i hi =>
        lt_of_lt_of_le hwT (hαge T hTP i hi))) hwT))
  simp only [smul_eq_mul] at hJ
  have hsimp : ∑ T ∈ Q, w T * ((∏ i ∈ T, α i) / w T) = ∑ T ∈ Q, ∏ i ∈ T, α i := by
    refine Finset.sum_congr rfl (fun T hT => ?_)
    have hwT : 0 < w T := (Finset.mem_filter.mp hT).2
    field_simp
  rw [hsimp] at hJ
  refine le_trans hJ ?_
  -- sum over Q of the products <= e_m(alpha) <= m^m/m!
  have hQpos : 0 < ∑ T ∈ Q, ∏ i ∈ T, α i := by
    have hne : Q.Nonempty := by
      by_contra hemp
      rw [Finset.not_nonempty_iff_eq_empty.mp hemp, Finset.sum_empty] at hwQ1
      norm_num at hwQ1
    obtain ⟨T0, hT0⟩ := hne
    have hwT : 0 < w T0 := (Finset.mem_filter.mp hT0).2
    have hTP : T0 ∈ P := (Finset.mem_filter.mp hT0).1
    exact lt_of_lt_of_le (Finset.prod_pos (fun i hi => lt_of_lt_of_le hwT (hαge T0 hTP i hi)))
      (Finset.single_le_sum (f := fun T => ∏ i ∈ T, α i)
        (fun T hT => Finset.prod_nonneg (fun i hi => hα0 i)) hT0)
  apply Real.log_le_log hQpos
  have hQle : ∑ T ∈ Q, ∏ i ∈ T, α i ≤ ∑ T ∈ P, ∏ i ∈ T, α i :=
    Finset.sum_le_sum_of_subset_of_nonneg hQsub (fun T _ _ => Finset.prod_nonneg (fun i _ => hα0 i))
  have hE := factorial_mul_esymm_le s α (fun i _ => hα0 i) m
  rw [hsumα] at hE
  have hfpos : (0:ℝ) < m.factorial := by exact_mod_cast Nat.factorial_pos m
  rw [le_div_iff₀ hfpos]
  calc (∑ T ∈ Q, ∏ i ∈ T, α i) * m.factorial ≤ (∑ T ∈ P, ∏ i ∈ T, α i) * m.factorial := by gcongr
    _ = m.factorial * ∑ T ∈ P, ∏ i ∈ T, α i := by ring
    _ ≤ (m:ℝ)^m := hE

end QformNine
