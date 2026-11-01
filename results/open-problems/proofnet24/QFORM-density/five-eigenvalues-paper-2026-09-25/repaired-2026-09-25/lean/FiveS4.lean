import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Analysis.Convex.Jensen
import Mathlib.Data.Finset.Powerset
import Mathlib.Tactic

/-!
Section 4 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), the finite part.

* `esymm_le`: `m! e_m(α) ≤ (Σ α)^m` for nonnegative `α` (used in the proof of Lemma 4.2).
* `entropy_bound`: Lemma 4.2, `H(w) + Σ_i α_i log α_i ≤ log ω(m)` for a probability distribution `w` on the
  `m`-subsets of a finite set, with `α_i = Σ_{T ∋ i} w_T` and `0 log 0 = 0` (Mathlib's `log 0 = 0`).
* `hub_selection`: the stopping procedure in the proof of Theorem 4.1: a set `H` with `|H| ≤ ℓ`,
  `F(H) ≥ 2^{-|H|} F(∅)`, and, when `|H| < ℓ`, `F(H ∪ {j}) ≤ F(H)/2` for every `j ∉ H`.
* `omega_le_succ`, `decay_const_le`, `decay_const_ratio`: `a_k ≤ a_0` (in squared form, with the sharper factor
  `e^{-k}`) and `π^ℓ e^{ℓ/2} (2e)^{ℓ/2} = (√2 π e)^ℓ`, the last lines of the proof of Theorem 4.1.
* `step5_log_identity`, `hub_constant`: the algebra of Steps 4 and 5 of Lemma 4.3.
-/

open Finset Real

namespace QformFiveB

/-- `ω(m) = m^m / m!`; Lean's `0^0 = 1` gives `ω(0) = 1`, as in the paper. -/
noncomputable def omega (m : ℕ) : ℝ := (m : ℝ) ^ m / (m.factorial : ℝ)

theorem omega_zero : omega 0 = 1 := by simp [omega]

theorem omega_pos (m : ℕ) : 0 < omega m := by
  unfold omega
  rcases Nat.eq_zero_or_pos m with h | h
  · subst h; simp
  · exact div_pos (pow_pos (by exact_mod_cast h) m) (by exact_mod_cast Nat.factorial_pos m)

/-- `ω(m) ≤ ω(m+1)`: `ω(m+1)/ω(m) = ((m+1)/m)^m ≥ 1` (proof of Theorem 4.1). -/
theorem omega_le_succ (m : ℕ) : omega m ≤ omega (m + 1) := by
  unfold omega
  have hf : ((m + 1).factorial : ℝ) = ((m : ℝ) + 1) * (m.factorial : ℝ) := by
    rw [Nat.factorial_succ]; push_cast; ring
  have hm1 : (0 : ℝ) < (m : ℝ) + 1 := by positivity
  have hfac : (0 : ℝ) < (m.factorial : ℝ) := by exact_mod_cast Nat.factorial_pos m
  have e : ((((m + 1 : ℕ) : ℝ)) ^ (m + 1)) / ((m + 1).factorial : ℝ)
      = ((m : ℝ) + 1) ^ m / (m.factorial : ℝ) := by
    rw [hf]; push_cast
    field_simp
    ring
  rw [e]
  gcongr
  linarith

theorem omega_mono {j k : ℕ} (h : j ≤ k) : omega j ≤ omega k := by
  induction h with
  | refl => exact le_refl _
  | step _ ih => exact ih.trans (omega_le_succ _)

/-- `S^{n+1} + (n+1) x S^n ≤ (S+x)^{n+1}` for `S, x ≥ 0`. -/
theorem pow_succ_ge (S x : ℝ) (hS : 0 ≤ S) (hx : 0 ≤ x) (n : ℕ) :
    S ^ (n + 1) + ((n : ℝ) + 1) * x * S ^ n ≤ (S + x) ^ (n + 1) := by
  induction n with
  | zero => simp
  | succ k ih =>
    have key : (S + x) * (S ^ (k + 1) + ((k : ℝ) + 1) * x * S ^ k)
        = S ^ (k + 1 + 1) + (((k + 1 : ℕ) : ℝ) + 1) * x * S ^ (k + 1)
          + ((k : ℝ) + 1) * x ^ 2 * S ^ k := by
      push_cast; ring
    have hk : 0 ≤ ((k : ℝ) + 1) * x ^ 2 * S ^ k := by positivity
    have hSx : 0 ≤ S + x := by linarith
    calc S ^ (k + 1 + 1) + (((k + 1 : ℕ) : ℝ) + 1) * x * S ^ (k + 1)
        ≤ (S + x) * (S ^ (k + 1) + ((k : ℝ) + 1) * x * S ^ k) := by rw [key]; linarith
      _ ≤ (S + x) * (S + x) ^ (k + 1) := mul_le_mul_of_nonneg_left ih hSx
      _ = (S + x) ^ (k + 1 + 1) := by ring

/-- `m! e_m(α) ≤ (Σ_i α_i)^m` for nonnegative `α`: in `(Σ α)^m` each product over an `m`-set occurs `m!`
times and every other term is nonnegative (proof of Lemma 4.2). -/
theorem esymm_le {ι : Type*} [DecidableEq ι] (α : ι → ℝ) (s : Finset ι) (hα : ∀ i ∈ s, 0 ≤ α i) (m : ℕ) :
    (m.factorial : ℝ) * ∑ T ∈ s.powersetCard m, ∏ i ∈ T, α i ≤ (∑ i ∈ s, α i) ^ m := by
  induction s using Finset.induction_on generalizing m with
  | empty =>
    cases m with
    | zero => simp
    | succ n => rw [Finset.powersetCard_eq_empty.mpr (by simp)]; simp
  | insert a s ha ih =>
    have hα' : ∀ i ∈ s, 0 ≤ α i := fun i hi => hα i (mem_insert_of_mem hi)
    have haα : 0 ≤ α a := hα a (mem_insert_self a s)
    have hS : 0 ≤ ∑ i ∈ s, α i := sum_nonneg hα'
    cases m with
    | zero => simp
    | succ n =>
      have hdisj : Disjoint (s.powersetCard (n + 1)) ((s.powersetCard n).image (insert a)) := by
        rw [disjoint_left]
        intro T hT hT'
        rcases mem_image.mp hT' with ⟨U, _, rfl⟩
        exact ha ((mem_powersetCard.mp hT).1 (mem_insert_self a U))
      have hinj : ∀ T ∈ s.powersetCard n, ∀ T' ∈ s.powersetCard n, insert a T = insert a T' → T = T' := by
        intro T hT T' hT' h
        have h1 : a ∉ T := fun h' => ha ((mem_powersetCard.mp hT).1 h')
        have h2 : a ∉ T' := fun h' => ha ((mem_powersetCard.mp hT').1 h')
        have h3 := congrArg (fun U => U.erase a) h
        simpa [erase_insert h1, erase_insert h2] using h3
      have hprod : ∀ T ∈ s.powersetCard n, ∏ i ∈ insert a T, α i = α a * ∏ i ∈ T, α i := by
        intro T hT
        have : a ∉ T := fun h => ha ((mem_powersetCard.mp hT).1 h)
        exact prod_insert this
      rw [powersetCard_succ_insert ha, sum_union hdisj, sum_image hinj, sum_congr rfl hprod, ← mul_sum,
        sum_insert ha]
      have e1 := ih hα' (n + 1)
      have e0 := ih hα' n
      have hfac : ((n + 1).factorial : ℝ) = ((n : ℝ) + 1) * (n.factorial : ℝ) := by
        rw [Nat.factorial_succ]; push_cast; ring
      have hb := pow_succ_ge (∑ i ∈ s, α i) (α a) hS haα n
      have hc : 0 ≤ ((n : ℝ) + 1) * α a := by positivity
      have e0' := mul_le_mul_of_nonneg_left e0 hc
      calc ((n + 1).factorial : ℝ) * (∑ T ∈ s.powersetCard (n + 1), ∏ i ∈ T, α i
              + α a * ∑ T ∈ s.powersetCard n, ∏ i ∈ T, α i)
          = ((n + 1).factorial : ℝ) * ∑ T ∈ s.powersetCard (n + 1), ∏ i ∈ T, α i
            + ((n : ℝ) + 1) * α a * ((n.factorial : ℝ) * ∑ T ∈ s.powersetCard n, ∏ i ∈ T, α i) := by
              rw [hfac]; ring
        _ ≤ (∑ i ∈ s, α i) ^ (n + 1) + ((n : ℝ) + 1) * α a * (∑ i ∈ s, α i) ^ n := by linarith
        _ ≤ (∑ i ∈ s, α i + α a) ^ (n + 1) := hb
        _ = (α a + ∑ i ∈ s, α i) ^ (n + 1) := by ring

/-- Swapping the two sums over incidences `i ∈ T`, for `T` running over `m`-subsets of `s`. -/
theorem sum_incidence {ι : Type*} [DecidableEq ι] (s : Finset ι) (m : ℕ) (g : ι → Finset ι → ℝ) :
    ∑ i ∈ s, ∑ T ∈ s.powersetCard m with i ∈ T, g i T = ∑ T ∈ s.powersetCard m, ∑ i ∈ T, g i T := by
  simp_rw [sum_filter]
  rw [sum_comm]
  apply sum_congr rfl
  intro T hT
  rw [← sum_filter]
  congr 1
  ext i
  simp only [mem_filter]
  constructor
  · rintro ⟨_, h⟩; exact h
  · intro h; exact ⟨(mem_powersetCard.mp hT).1 h, h⟩

/-- **Lemma 4.2.** For a probability distribution `w` on the `m`-subsets of a finite set `s`, with marginals
`α_i = Σ_{T ∋ i} w_T` and `H(w) = -Σ_T w_T log w_T` (`0 log 0 = 0`), `H(w) + Σ_i α_i log α_i ≤ log ω(m)`. -/
theorem entropy_bound {ι : Type*} [DecidableEq ι] (s : Finset ι) (m : ℕ)
    (w : Finset ι → ℝ) (hw0 : ∀ T ∈ s.powersetCard m, 0 ≤ w T)
    (hw1 : ∑ T ∈ s.powersetCard m, w T = 1) :
    -(∑ T ∈ s.powersetCard m, w T * log (w T))
      + ∑ i ∈ s, (∑ T ∈ s.powersetCard m with i ∈ T, w T)
          * log (∑ T ∈ s.powersetCard m with i ∈ T, w T)
      ≤ log (omega m) := by
  set P := s.powersetCard m with hP
  set α : ι → ℝ := fun i => ∑ T ∈ P with i ∈ T, w T with hαdef
  have hα0 : ∀ i, 0 ≤ α i := fun i => sum_nonneg (fun T hT => hw0 T (mem_filter.mp hT).1)
  have hαw : ∀ T ∈ P, ∀ i ∈ T, w T ≤ α i := by
    intro T hT i hi
    exact single_le_sum (f := w) (fun U hU => hw0 U (mem_filter.mp hU).1) (mem_filter.mpr ⟨hT, hi⟩)
  -- the Jensen points
  set p : Finset ι → ℝ := fun T => if 0 < w T then (∏ i ∈ T, α i) / w T else 1 with hpdef
  have hprodpos : ∀ T ∈ P, 0 < w T → 0 < ∏ i ∈ T, α i := by
    intro T hT hwT
    exact prod_pos (fun i hi => lt_of_lt_of_le hwT (hαw T hT i hi))
  have hp_pos : ∀ T ∈ P, 0 < p T := by
    intro T hT
    by_cases hwT : 0 < w T
    · simp only [hpdef, if_pos hwT]; exact div_pos (hprodpos T hT hwT) hwT
    · simp only [hpdef, if_neg hwT]; exact one_pos
  have hwp : ∀ T ∈ P, w T * p T ≤ ∏ i ∈ T, α i := by
    intro T hT
    by_cases hwT : 0 < w T
    · simp only [hpdef, if_pos hwT]
      rw [mul_div_cancel₀ _ hwT.ne']
    · have hw0' : w T = 0 := le_antisymm (not_lt.mp hwT) (hw0 T hT)
      rw [hw0', zero_mul]
      exact prod_nonneg (fun i _ => hα0 i)
  have hwlog : ∀ T ∈ P, w T * (∑ i ∈ T, log (α i)) - w T * log (w T) = w T * log (p T) := by
    intro T hT
    by_cases hwT : 0 < w T
    · simp only [hpdef, if_pos hwT]
      have hne : ∀ i ∈ T, α i ≠ 0 := fun i hi => (lt_of_lt_of_le hwT (hαw T hT i hi)).ne'
      rw [log_div (hprodpos T hT hwT).ne' hwT.ne', log_prod hne]
      ring
    · have hw0' : w T = 0 := le_antisymm (not_lt.mp hwT) (hw0 T hT)
      rw [hw0']; ring
  -- rewrite the left side as a Jensen sum
  have hleft : -(∑ T ∈ P, w T * log (w T)) + ∑ i ∈ s, α i * log (α i) = ∑ T ∈ P, w T * log (p T) := by
    have hsw : ∑ i ∈ s, α i * log (α i) = ∑ T ∈ P, w T * ∑ i ∈ T, log (α i) := by
      have h1 : ∀ i ∈ s, α i * log (α i) = ∑ T ∈ P with i ∈ T, w T * log (α i) := by
        intro i _; simp only [hαdef]; rw [sum_mul]
      rw [sum_congr rfl h1, sum_incidence s m (fun i T => w T * log (α i))]
      apply sum_congr rfl; intro T _; rw [mul_sum]
    rw [hsw, ← sum_congr rfl hwlog, sum_sub_distrib]
    ring
  -- Jensen for the concave logarithm
  have hjensen := (strictConcaveOn_log_Ioi.concaveOn).le_map_sum (t := P) (w := w) (p := p) hw0 hw1
    (fun T hT => (hp_pos T hT : 0 < p T))
  simp only [smul_eq_mul] at hjensen
  -- the Jensen sum is positive and at most e_m(α)
  have hsumpos : 0 < ∑ T ∈ P, w T * p T := by
    have hex : ∃ T ∈ P, 0 < w T := by
      by_contra hcon
      push_neg at hcon
      have : ∑ T ∈ P, w T ≤ 0 := sum_nonpos hcon
      linarith
    obtain ⟨T, hT, hwT⟩ := hex
    exact sum_pos' (fun U hU => mul_nonneg (hw0 U hU) (hp_pos U hU).le)
      ⟨T, hT, mul_pos hwT (hp_pos T hT)⟩
  have hle_e : ∑ T ∈ P, w T * p T ≤ ∑ T ∈ P, ∏ i ∈ T, α i := sum_le_sum hwp
  -- Σ α = m
  have hsumα : ∑ i ∈ s, α i = m := by
    have := sum_incidence s m (fun _ T => w T)
    simp only at this
    simp only [hαdef]
    rw [this]
    have h2 : ∀ T ∈ P, ∑ _i ∈ T, w T = (m : ℝ) * w T := by
      intro T hT
      rw [sum_const, (mem_powersetCard.mp hT).2, nsmul_eq_mul]
    rw [sum_congr rfl h2, ← mul_sum, hw1, mul_one]
  -- e_m(α) ≤ ω(m)
  have hE : ∑ T ∈ P, ∏ i ∈ T, α i ≤ omega m := by
    have h := esymm_le α s (fun i _ => hα0 i) m
    rw [hsumα] at h
    unfold omega
    rw [le_div_iff₀ (by exact_mod_cast Nat.factorial_pos m)]
    linarith
  calc -(∑ T ∈ P, w T * log (w T)) + ∑ i ∈ s, α i * log (α i)
      = ∑ T ∈ P, w T * log (p T) := hleft
    _ ≤ log (∑ T ∈ P, w T * p T) := hjensen
    _ ≤ log (omega m) := log_le_log hsumpos (hle_e.trans hE)

/-- **The stopping procedure of Theorem 4.1.** For any `F` on finite sets with `F(∅) > 0` and any `ℓ`, there is
`H ⊆ I` with `|H| ≤ ℓ`, `2^{-|H|} F(∅) ≤ F(H)`, and, if `|H| < ℓ`, `F(H ∪ {j}) ≤ F(H)/2` for all `j ∈ I \ H`. -/
theorem hub_selection {ι : Type*} [DecidableEq ι] (I : Finset ι) (F : Finset ι → ℝ) (ℓ : ℕ) :
    ∃ H ⊆ I, H.card ≤ ℓ ∧ (2 : ℝ)⁻¹ ^ H.card * F ∅ ≤ F H ∧
      (H.card < ℓ → ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2) := by
  have aux : ∀ d : ℕ, ∀ H ⊆ I, H.card + d = ℓ → (2 : ℝ)⁻¹ ^ H.card * F ∅ ≤ F H →
      ∃ H' ⊆ I, H'.card ≤ ℓ ∧ (2 : ℝ)⁻¹ ^ H'.card * F ∅ ≤ F H' ∧
        (H'.card < ℓ → ∀ j ∈ I \ H', F (insert j H') ≤ F H' / 2) := by
    intro d
    induction d with
    | zero =>
      intro H hHI hcard hF
      refine ⟨H, hHI, by omega, hF, fun h => absurd h (by omega)⟩
    | succ d ih =>
      intro H hHI hcard hF
      by_cases hall : ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2
      · exact ⟨H, hHI, by omega, hF, fun _ => hall⟩
      · push_neg at hall
        obtain ⟨j, hj, hjF⟩ := hall
        have hjI : j ∈ I := (mem_sdiff.mp hj).1
        have hjH : j ∉ H := (mem_sdiff.mp hj).2
        have hcard' : (insert j H).card = H.card + 1 := card_insert_of_notMem hjH
        apply ih (insert j H) (insert_subset hjI hHI) (by omega)
        rw [hcard', pow_succ]
        have : (2 : ℝ)⁻¹ ^ H.card * F ∅ * 2⁻¹ ≤ F H / 2 := by
          have := mul_le_mul_of_nonneg_right hF (by norm_num : (0 : ℝ) ≤ 2⁻¹)
          linarith [show F H / 2 = F H * 2⁻¹ by ring]
        calc (2 : ℝ)⁻¹ ^ H.card * 2⁻¹ * F ∅ = (2 : ℝ)⁻¹ ^ H.card * F ∅ * 2⁻¹ := by ring
          _ ≤ F H / 2 := this
          _ ≤ F (insert j H) := hjF.le
  exact aux ℓ ∅ (empty_subset I) (by simp) (by simp)

/-- **The constant of Theorem 4.1.** With `a_k² = (2e)^{ℓ-k} ω(ℓ-k) 2^k` (write `j = ℓ - k`),
`e^k a_k² ≤ a_0²`; in particular `a_k ≤ a_0`. -/
theorem decay_const_ratio (j k : ℕ) :
    exp 1 ^ k * ((2 * exp 1) ^ j * omega j * 2 ^ k) ≤ (2 * exp 1) ^ (j + k) * omega (j + k) := by
  have hω := omega_mono (Nat.le_add_right j k)
  have h0 : 0 ≤ (2 * exp 1) ^ j := by positivity
  calc exp 1 ^ k * ((2 * exp 1) ^ j * omega j * 2 ^ k)
      = (2 * exp 1) ^ j * (2 * exp 1) ^ k * omega j := by rw [mul_pow]; ring
    _ ≤ (2 * exp 1) ^ j * (2 * exp 1) ^ k * omega (j + k) := by
        apply mul_le_mul_of_nonneg_left hω; positivity
    _ = (2 * exp 1) ^ (j + k) * omega (j + k) := by rw [pow_add]

theorem decay_const_le (j k : ℕ) :
    (2 * exp 1) ^ j * omega j * 2 ^ k ≤ (2 * exp 1) ^ (j + k) * omega (j + k) := by
  have h := decay_const_ratio j k
  have h1 : 1 ≤ exp 1 ^ k := one_le_pow₀ (by linarith [add_one_le_exp (1 : ℝ)])
  have h2 : 0 ≤ (2 * exp 1) ^ j * omega j * 2 ^ k := by
    have := omega_pos j; positivity
  nlinarith

/-- `π^ℓ e^{ℓ/2} (2e)^{ℓ/2} = (√2 π e)^ℓ`, written with square roots. -/
theorem decay_const_identity (ℓ : ℕ) :
    π ^ ℓ * (√(exp 1)) ^ ℓ * (√(2 * exp 1)) ^ ℓ = (√2 * π * exp 1) ^ ℓ := by
  have he : 0 ≤ exp 1 := (exp_pos 1).le
  have h : π * √(exp 1) * √(2 * exp 1) = √2 * π * exp 1 := by
    rw [Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]
    have : √(exp 1) * √(exp 1) = exp 1 := Real.mul_self_sqrt he
    calc π * √(exp 1) * (√2 * √(exp 1)) = √2 * π * (√(exp 1) * √(exp 1)) := by ring
      _ = √2 * π * exp 1 := by rw [this]
  rw [← mul_pow, ← mul_pow, h]

/-- **Step 5 of Lemma 4.3, logarithmic form.** For a probability vector `w` and `c > 0`,
`Σ_T w_T log(c w_T) = log c + Σ_T w_T log w_T`; with `c = Θ(H) Z_H` and `θ(T') = Z_H w_{T'}` this is
`Π (Θ(H) θ(T'))^{-w/2} = (Θ(H) Z_H)^{-1/2} e^{H(w)/2}`. -/
theorem step5_log_identity {κ : Type*} (P : Finset κ) (w : κ → ℝ) (c : ℝ) (hc : 0 < c)
    (hw0 : ∀ T ∈ P, 0 ≤ w T) (hw1 : ∑ T ∈ P, w T = 1) :
    ∑ T ∈ P, w T * log (c * w T) = log c + ∑ T ∈ P, w T * log (w T) := by
  have h : ∀ T ∈ P, w T * log (c * w T) = w T * log c + w T * log (w T) := by
    intro T hT
    rcases (hw0 T hT).lt_or_eq with hpos | hzero
    · rw [log_mul hc.ne' hpos.ne']; ring
    · rw [← hzero]; simp
  rw [sum_congr rfl h, sum_add_distrib, ← sum_mul, hw1, one_mul]

/-- **Step 4 of Lemma 4.3, the constant.** With Lemma 3.3 at `p = 1/α ≥ 2`, the inner integral
`(2|t|)^{-1} ∫ |ψ|^{1/α}` is at most `(2|t|)^{-1} · 2π√(2e)/√(1/α) = π√(2eα)/|t|`. -/
theorem hub_constant (t α : ℝ) (ht : 0 < t) (hα : 0 < α) :
    (2 * t)⁻¹ * (2 * π * √(2 * exp 1) / √(1 / α)) = π * √(2 * exp 1 * α) / t := by
  have hsα : √(1 / α) = (√α)⁻¹ := by rw [one_div, Real.sqrt_inv]
  have h2 : √(2 * exp 1 * α) = √(2 * exp 1) * √α :=
    Real.sqrt_mul (by positivity) α
  rw [hsα, h2]
  have hsa : 0 < √α := Real.sqrt_pos.mpr hα
  field_simp

end QformFiveB
