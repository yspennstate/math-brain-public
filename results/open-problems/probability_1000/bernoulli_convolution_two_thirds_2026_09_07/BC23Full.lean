import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Field.GeomSum
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Int.GCD
import Mathlib.Algebra.Prime.Defs
import Mathlib.RingTheory.Int.Basic
import Mathlib.Tactic.NormNum.Prime
import Mathlib.Tactic.Common
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The exact full-period average, assembled

Combines three checked ingredients:
* `eq_zero_of_S_eq_zero` - the frequencies `2^i 3^(K-i)` admit no `{0, +-1, +-2}` relation (3-adic);
* `sum_e_period` - character orthogonality over a full period;
* `prod_one_add_cos` - the three-term expansion of a product of `1 + cos` factors.
-/

open Finset Complex

namespace BC23


noncomputable def ee (t : ℝ) : ℂ := Complex.exp (2 * Real.pi * Complex.I * t)

lemma ee_add (s t : ℝ) : ee (s + t) = ee s * ee t := by
  unfold ee
  rw [← Complex.exp_add]
  push_cast
  ring_nf

lemma ee_int (n : ℤ) : ee (n : ℝ) = 1 := by
  unfold ee
  have : (2 * Real.pi * Complex.I * (n : ℝ)) = (n : ℂ) * (2 * Real.pi * Complex.I) := by
    push_cast; ring
  rw [this, Complex.exp_int_mul_two_pi_mul_I]

/-- `e (k * m / N)` as a power of the primitive root `e (m / N)`. -/
lemma ee_pow (m : ℝ) (k : ℕ) : ee (k * m) = (ee m) ^ k := by
  induction k with
  | zero => simp [ee]
  | succ k ih =>
    have hstep : ((k : ℝ) + 1) * m = (k : ℝ) * m + m := by ring
    push_cast
    rw [hstep, ee_add, ih, pow_succ]

/-- Orthogonality: the sum of `e (k m / N)` over a full period is `N` or `0`. -/
theorem sum_e_period (N : ℕ) (hN : 0 < N) (m : ℤ) :
    (∑ k ∈ range N, ee ((k : ℝ) * (m : ℝ) / (N : ℝ)))
      = if (N : ℤ) ∣ m then (N : ℂ) else 0 := by
  have hNne : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hN.ne'
  set z : ℂ := ee ((m : ℝ) / (N : ℝ)) with hz
  have hterm : ∀ k ∈ range N, ee ((k : ℝ) * (m : ℝ) / (N : ℝ)) = z ^ k := by
    intro k _
    have : (k : ℝ) * (m : ℝ) / (N : ℝ) = (k : ℝ) * ((m : ℝ) / (N : ℝ)) := by
      field_simp
    rw [this, hz, ee_pow]
  rw [Finset.sum_congr rfl hterm]
  by_cases hdvd : (N : ℤ) ∣ m
  · have hz1 : z = 1 := by
      obtain ⟨c, hc⟩ := hdvd
      have : (m : ℝ) / (N : ℝ) = (c : ℝ) := by
        rw [hc]; push_cast; field_simp
      rw [hz, this, ee_int]
    simp [hz1, hdvd]
  · have hzN : z ^ N = 1 := by
      rw [hz, ← ee_pow]
      have : (N : ℝ) * ((m : ℝ) / (N : ℝ)) = (m : ℝ) := by field_simp
      rw [this, ee_int]
    have hzne : z ≠ 1 := by
      intro h1
      apply hdvd
      rw [hz] at h1
      unfold ee at h1
      obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp h1
      have hpi : (2 : ℂ) * (Real.pi : ℂ) * Complex.I ≠ 0 := by
        have h1' : (Real.pi : ℂ) ≠ 0 := by
          exact_mod_cast Real.pi_ne_zero
        simp [h1', Complex.I_ne_zero]
      have hreal : (m : ℝ) / (N : ℝ) = (n : ℝ) := by
        field_simp at hn
        exact_mod_cast hn
      have hm : (m : ℝ) = (N : ℝ) * (n : ℝ) := by
        field_simp at hreal
        linarith
      exact ⟨n, by exact_mod_cast hm⟩
    have := geom_sum_eq hzne N
    rw [this, hzN]
    simp [hdvd]




/-- The coefficients we allow: `{0, ±1, ±2}`. -/
def Small (e : ℤ) : Prop := e = 0 ∨ e = 1 ∨ e = -1 ∨ e = 2 ∨ e = -2

lemma Small.eq_zero_of_three_dvd {e : ℤ} (h : Small e) (h3 : (3 : ℤ) ∣ e) : e = 0 := by
  rcases h with h | h | h | h | h <;> subst h
  · rfl
  all_goals (exfalso; omega)

/-- The weighted sum whose vanishing we study. -/
def S (eps : ℕ → ℤ) (K : ℕ) : ℤ := ∑ i ∈ range (K + 1), eps i * 2 ^ i * 3 ^ (K - i)

lemma S_zero (eps : ℕ → ℤ) : S eps 0 = eps 0 := by
  simp [S]

lemma S_succ (eps : ℕ → ℤ) (K : ℕ) :
    S eps (K + 1) = 3 * S eps K + eps (K + 1) * 2 ^ (K + 1) := by
  have hterm : ∀ i ∈ range (K + 1),
      eps i * 2 ^ i * 3 ^ (K + 1 - i) = 3 * (eps i * 2 ^ i * 3 ^ (K - i)) := by
    intro i hi
    have hiK : i ≤ K := Nat.lt_succ_iff.mp (mem_range.mp hi)
    have hsub : K + 1 - i = (K - i) + 1 := by omega
    rw [hsub]
    ring
  calc S eps (K + 1)
      = (∑ i ∈ range (K + 1), eps i * 2 ^ i * 3 ^ (K + 1 - i))
          + eps (K + 1) * 2 ^ (K + 1) * 3 ^ (K + 1 - (K + 1)) := by
        rw [S, Finset.sum_range_succ]
    _ = (∑ i ∈ range (K + 1), 3 * (eps i * 2 ^ i * 3 ^ (K - i)))
          + eps (K + 1) * 2 ^ (K + 1) := by
        rw [Finset.sum_congr rfl hterm]; simp
    _ = 3 * S eps K + eps (K + 1) * 2 ^ (K + 1) := by
        rw [S, Finset.mul_sum]

theorem eq_zero_of_S_eq_zero (eps : ℕ → ℤ) (hs : ∀ i, Small (eps i)) :
    ∀ K, S eps K = 0 → ∀ i, i ≤ K → eps i = 0 := by
  intro K
  induction K with
  | zero =>
    intro h i hi
    have : i = 0 := Nat.le_zero.mp hi
    subst this
    rwa [S_zero] at h
  | succ K ih =>
    intro h i hi
    have hsplit : (0 : ℤ) = 3 * S eps K + eps (K + 1) * 2 ^ (K + 1) := by
      rw [← h, S_succ]
    have h3 : (3 : ℤ) ∣ eps (K + 1) * 2 ^ (K + 1) := ⟨-S eps K, by linarith⟩
    have hp : Prime (3 : ℤ) := Int.prime_iff_natAbs_prime.mpr (by norm_num)
    have hnot : ¬ ((3 : ℤ) ∣ (2 : ℤ) ^ (K + 1)) := by
      intro hd
      have h23 : (3 : ℤ) ∣ (2 : ℤ) := hp.dvd_of_dvd_pow hd
      norm_num at h23
    have hdvd : (3 : ℤ) ∣ eps (K + 1) := by
      rcases hp.dvd_mul.mp h3 with hgood | hbad
      · exact hgood
      · exact absurd hbad hnot
    have htop : eps (K + 1) = 0 := (hs (K + 1)).eq_zero_of_three_dvd hdvd
    have hrest : S eps K = 0 := by
      rw [htop] at hsplit
      simp at hsplit
      linarith
    rcases Nat.lt_or_ge i (K + 1) with hlt | hge
    · exact ih hrest i (Nat.lt_succ_iff.mp hlt)
    · have : i = K + 1 := le_antisymm hi hge
      rw [this]
      exact htop



/-- ee 0 = 1. -/
lemma ee_zero : ee 0 = 1 := by simp [ee]

/-- `1 + cos θ` as the three characters `1`, `e(θ)/2`, `e(-θ)/2`. -/
lemma one_add_cos (t : ℝ) :
    (1 : ℂ) + Real.cos (2 * Real.pi * t) = 1 + ee t / 2 + ee (-t) / 2 := by
  unfold ee
  set w : ℂ := ((2 * Real.pi * t : ℝ) : ℂ) with hw
  have h2 : 2 * Complex.cos w = Complex.exp (w * Complex.I) + Complex.exp (-w * Complex.I) :=
    Complex.two_cos w
  have hcast : ((Real.cos (2 * Real.pi * t) : ℝ) : ℂ) = Complex.cos w := by
    rw [hw, Complex.ofReal_cos]
  have hL : (2 : ℂ) * Real.pi * Complex.I * (t : ℝ) = w * Complex.I := by
    rw [hw]; push_cast; ring
  have hR : (2 : ℂ) * Real.pi * Complex.I * ((-t : ℝ) : ℂ) = -w * Complex.I := by
    rw [hw]; push_cast; ring
  rw [hcast, hL, hR]
  linear_combination h2 / 2

/-- The three-term expansion of a product of `1 + cos` factors, as a sum over sign patterns. -/
theorem prod_one_add_cos (K : ℕ) (θ : Fin (K + 1) → ℝ) :
    (∏ i, ((1 : ℂ) + Real.cos (2 * Real.pi * θ i)))
      = ∑ s ∈ Fintype.piFinset (fun _ : Fin (K + 1) => ({-1, 0, 1} : Finset ℤ)),
          ∏ i, (if s i = 0 then (1 : ℂ) else ee ((s i : ℝ) * θ i) / 2) := by
  have hfac : ∀ i : Fin (K + 1),
      ((1 : ℂ) + Real.cos (2 * Real.pi * θ i))
        = ∑ j ∈ ({-1, 0, 1} : Finset ℤ), (if j = 0 then (1 : ℂ) else ee ((j : ℝ) * θ i) / 2) := by
    intro i
    have hm : ((-1 : ℤ) : ℝ) * θ i = -θ i := by push_cast; ring
    have hp : ((1 : ℤ) : ℝ) * θ i = θ i := by push_cast; ring
    rw [show ({-1, 0, 1} : Finset ℤ) = insert (-1 : ℤ) (insert (0 : ℤ) {(1 : ℤ)}) from rfl,
      Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton]
    simp only [if_neg (by decide : (-1 : ℤ) ≠ 0), if_neg (by decide : (1 : ℤ) ≠ 0),
      if_pos]
    rw [one_add_cos (θ i), hm, hp]
    ring
  rw [Finset.prod_congr rfl (fun i _ => hfac i)]
  exact Finset.prod_univ_sum _ _



/-- `ee` turns a finite sum into a product. -/
lemma ee_sum {ι : Type*} (t : Finset ι) (a : ι → ℝ) :
    ee (∑ i ∈ t, a i) = ∏ i ∈ t, ee (a i) := by
  classical
  induction t using Finset.induction_on with
  | empty => simp [ee_zero]
  | insert i t hi ih =>
    rw [Finset.sum_insert hi, Finset.prod_insert hi, ee_add, ih]

/-- One character term of the expansion, factored into its weight and a single exponential. -/
lemma term_factor (K : ℕ) (θ : Fin (K + 1) → ℝ) (s : Fin (K + 1) → ℤ) :
    (∏ i, (if s i = 0 then (1 : ℂ) else ee ((s i : ℝ) * θ i) / 2))
      = (∏ i, (if s i = 0 then (1 : ℂ) else 1 / 2)) * ee (∑ i, (s i : ℝ) * θ i) := by
  rw [ee_sum, ← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl ?_
  intro i _
  by_cases h : s i = 0
  · simp [h, ee_zero]
  · simp [h]
    ring


/-- **The exact full-period average.**  If the frequencies admit no nontrivial `{0, ±1}` relation
modulo `N`, then averaging `∏ (1 + cos)` over a full period gives exactly `1`. -/
theorem period_average (K N : ℕ) (hN : 0 < N) (n : Fin (K + 1) → ℤ)
    (hdis : ∀ s : Fin (K + 1) → ℤ, (∀ i, s i = -1 ∨ s i = 0 ∨ s i = 1) →
      ((N : ℤ) ∣ ∑ i, s i * n i) → ∀ i, s i = 0) :
    (∑ k ∈ range N, ∏ i, ((1 : ℂ) + Real.cos (2 * Real.pi * ((k : ℝ) * (n i : ℝ) / (N : ℝ)))))
      = (N : ℂ) := by
  classical
  have hNne : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hN.ne'
  -- expand each factor into three characters
  have hexp : ∀ k : ℕ,
      (∏ i, ((1 : ℂ) + Real.cos (2 * Real.pi * ((k : ℝ) * (n i : ℝ) / (N : ℝ)))))
        = ∑ s ∈ Fintype.piFinset (fun _ : Fin (K + 1) => ({-1, 0, 1} : Finset ℤ)),
            (∏ i, (if s i = 0 then (1 : ℂ) else 1 / 2))
              * ee ((k : ℝ) * ((∑ i, s i * n i : ℤ) : ℝ) / (N : ℝ)) := by
    intro k
    rw [prod_one_add_cos K (fun i => (k : ℝ) * (n i : ℝ) / (N : ℝ))]
    refine Finset.sum_congr rfl ?_
    intro s _
    rw [term_factor]
    congr 1
    have h1 : (∑ i, (s i : ℝ) * ((k : ℝ) * (n i : ℝ) / (N : ℝ)))
        = ((k : ℝ) / (N : ℝ)) * ∑ i, ((s i : ℝ) * (n i : ℝ)) := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl ?_
      intro i _
      field_simp
    have h2 : ((∑ i, s i * n i : ℤ) : ℝ) = ∑ i, ((s i : ℝ) * (n i : ℝ)) := by
      push_cast
      rfl
    rw [h1, h2]
    field_simp
  rw [Finset.sum_congr rfl (fun k _ => hexp k), Finset.sum_comm]
  -- orthogonality kills every nonzero sign pattern
  have hone : ∀ s ∈ Fintype.piFinset (fun _ : Fin (K + 1) => ({-1, 0, 1} : Finset ℤ)),
      (∑ k ∈ range N, (∏ i, (if s i = 0 then (1 : ℂ) else 1 / 2))
          * ee ((k : ℝ) * ((∑ i, s i * n i : ℤ) : ℝ) / (N : ℝ)))
        = if (∀ i, s i = 0) then (N : ℂ) else 0 := by
    intro s hs
    rw [← Finset.mul_sum, sum_e_period N hN (∑ i, s i * n i)]
    have hsmall : ∀ i, s i = -1 ∨ s i = 0 ∨ s i = 1 := by
      intro i
      have := Fintype.mem_piFinset.mp hs i
      simpa using this
    by_cases hz : ∀ i, s i = 0
    · have hzero : (∑ i, s i * n i) = 0 := by
        refine Finset.sum_eq_zero ?_
        intro i _
        rw [hz i]; ring
      simp [hz, hzero]
    · have hnd : ¬ ((N : ℤ) ∣ ∑ i, s i * n i) := fun hd => hz (hdis s hsmall hd)
      simp [hnd, hz]
  rw [Finset.sum_congr rfl hone]
  -- only the zero pattern remains
  have hzmem : (0 : Fin (K + 1) → ℤ)
      ∈ Fintype.piFinset (fun _ : Fin (K + 1) => ({-1, 0, 1} : Finset ℤ)) := by
    rw [Fintype.mem_piFinset]
    intro i
    simp
  have hpred : ∀ x : Fin (K + 1) → ℤ, (∀ i, x i = 0) ↔ x = 0 := by
    intro x
    constructor
    · intro h; funext i; exact h i
    · intro h i; rw [h]; rfl
  simp only [hpred]
  rw [Finset.sum_ite_eq' _ (0 : Fin (K + 1) → ℤ) (fun _ => (N : ℂ))]
  simp [hzmem]

end BC23

#print axioms BC23.period_average
#print axioms BC23.eq_zero_of_S_eq_zero
#print axioms BC23.sum_e_period
#print axioms BC23.prod_one_add_cos
