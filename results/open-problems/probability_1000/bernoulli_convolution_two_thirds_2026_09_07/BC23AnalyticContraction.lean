import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SumIntegralComparisons
import Mathlib.Analysis.PSeries
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Analytic core of the two-copy paper, machine-checked

* The series `psi t = ∑_{k≥1} t^(2k)/(2k(2k-1))` of Lemma 6.1 and the two
  inequalities the lemma rests on: `psi (u v) ≤ v^2 psi u` and `v^2 ≤ 2 psi v`,
  hence `psi (u v) ≤ 2 psi u psi v` for |u|,|v| ≤ 1.
* The integral-test bound `∑_{n≥1} n^(-26/25) ≤ 26` that Section 6 uses to reach 209.
-/

open Real Set MeasureTheory

namespace BC23

/-- One term of the series: t^(2(k+1)) / ((2(k+1))(2(k+1)-1)). -/
noncomputable def psiTerm (t : ℝ) (k : ℕ) : ℝ :=
  t ^ (2 * (k + 1)) / (((2 * (k + 1) : ℕ) : ℝ) * ((2 * (k + 1) : ℕ) - 1 : ℝ))

/-- The even convex function of Lemma 6.1, as its positive series. -/
noncomputable def psi (t : ℝ) : ℝ := ∑' k : ℕ, psiTerm t k

lemma denom_pos (k : ℕ) : (0:ℝ) < (((2 * (k + 1) : ℕ) : ℝ) * ((2 * (k + 1) : ℕ) - 1 : ℝ)) := by
  push_cast
  nlinarith [(k.cast_nonneg : (0:ℝ) ≤ k)]

lemma psiTerm_nonneg (t : ℝ) (k : ℕ) : 0 ≤ psiTerm t k := by
  unfold psiTerm
  have h := denom_pos k
  have : 0 ≤ t ^ (2 * (k + 1)) := by
    rw [pow_mul]; positivity
  positivity

lemma pow_two_mul_le_one {t : ℝ} (ht : |t| ≤ 1) (n : ℕ) : t ^ (2 * n) ≤ 1 := by
  rw [pow_mul]
  have h2 : t ^ 2 ≤ 1 := by
    have := abs_le.1 ht
    nlinarith [this.1, this.2]
  exact pow_le_one₀ (by positivity) h2

lemma psiTerm_le {t : ℝ} (ht : |t| ≤ 1) (k : ℕ) : psiTerm t k ≤ 1 / (((k:ℝ) + 1) ^ 2) := by
  unfold psiTerm
  have hd := denom_pos k
  have hnum := pow_two_mul_le_one ht (k + 1)
  have hnum0 : 0 ≤ t ^ (2 * (k + 1)) := by rw [pow_mul]; positivity
  have hden : ((k:ℝ) + 1) ^ 2 ≤ (((2 * (k + 1) : ℕ) : ℝ) * ((2 * (k + 1) : ℕ) - 1 : ℝ)) := by
    push_cast; nlinarith [(k.cast_nonneg : (0:ℝ) ≤ k)]
  calc t ^ (2 * (k + 1)) / (((2 * (k + 1) : ℕ) : ℝ) * ((2 * (k + 1) : ℕ) - 1 : ℝ))
      ≤ 1 / (((2 * (k + 1) : ℕ) : ℝ) * ((2 * (k + 1) : ℕ) - 1 : ℝ)) := by gcongr
    _ ≤ 1 / (((k:ℝ) + 1) ^ 2) := by gcongr

lemma summable_psiTerm {t : ℝ} (ht : |t| ≤ 1) : Summable (psiTerm t) := by
  refine Summable.of_nonneg_of_le (psiTerm_nonneg t) (psiTerm_le ht) ?_
  have h : Summable (fun k : ℕ => 1 / ((k:ℝ) ^ 2)) := by
    simpa using Real.summable_one_div_nat_pow.2 (by norm_num : 1 < 2)
  have := (summable_nat_add_iff 1).2 h
  simpa [Nat.cast_add, Nat.cast_one] using this

/-- Termwise: (uv)^(2n) ≤ v^2 u^(2n) for |v| ≤ 1, n ≥ 1. -/
lemma psiTerm_mul_le {u v : ℝ} (hv : |v| ≤ 1) (k : ℕ) :
    psiTerm (u * v) k ≤ v ^ 2 * psiTerm u k := by
  unfold psiTerm
  have hd := denom_pos k
  rw [mul_pow, ← mul_div_assoc]
  apply div_le_div_of_nonneg_right _ hd.le
  -- u^(2(k+1)) v^(2(k+1)) ≤ v^2 u^(2(k+1)) since v^(2k) ≤ 1
  have hu0 : 0 ≤ u ^ (2 * (k + 1)) := by rw [pow_mul]; positivity
  have hvk : v ^ (2 * k) ≤ 1 := pow_two_mul_le_one hv k
  have hv0 : 0 ≤ v ^ (2 * k) := by rw [pow_mul]; positivity
  have : v ^ (2 * (k + 1)) = v ^ 2 * v ^ (2 * k) := by ring
  rw [this]
  have h2 : 0 ≤ v ^ 2 := by positivity
  nlinarith [mul_nonneg hu0 h2, mul_le_mul_of_nonneg_left hvk (mul_nonneg hu0 h2)]

/-- psi (u v) ≤ v^2 psi u for |u|, |v| ≤ 1. -/
theorem psi_mul_le {u v : ℝ} (hu : |u| ≤ 1) (hv : |v| ≤ 1) : psi (u * v) ≤ v ^ 2 * psi u := by
  unfold psi
  rw [← tsum_mul_left]
  have huv : |u * v| ≤ 1 := by
    rw [abs_mul]; exact mul_le_one₀ hu (abs_nonneg v) hv
  refine Summable.tsum_le_tsum (fun k => psiTerm_mul_le hv k) (summable_psiTerm huv) ?_
  exact (summable_psiTerm hu).mul_left _

/-- v^2 ≤ 2 psi v for |v| ≤ 1: the first term of the series is v^2/2 and every term is nonnegative. -/
theorem sq_le_two_psi {v : ℝ} (hv : |v| ≤ 1) : v ^ 2 ≤ 2 * psi v := by
  unfold psi
  have hfirst : psiTerm v 0 = v ^ 2 / 2 := by
    unfold psiTerm; norm_num
  have hle : psiTerm v 0 ≤ ∑' k, psiTerm v k :=
    (summable_psiTerm hv).le_tsum 0 (fun j _ => psiTerm_nonneg v j)
  rw [hfirst] at hle
  linarith

/-- Lemma 6.1's analytic core: psi (u v) ≤ 2 psi u psi v for |u|, |v| ≤ 1. -/
theorem psi_prod_le {u v : ℝ} (hu : |u| ≤ 1) (hv : |v| ≤ 1) : psi (u * v) ≤ 2 * psi u * psi v := by
  have h1 := psi_mul_le hu hv
  have h2 := sq_le_two_psi hv
  have hpsi_u : 0 ≤ psi u := tsum_nonneg (psiTerm_nonneg u)
  calc psi (u * v) ≤ v ^ 2 * psi u := h1
    _ ≤ (2 * psi v) * psi u := by gcongr
    _ = 2 * psi u * psi v := by ring

/-- The integral test: ∑_{n ≥ 0} n^(-26/25) ≤ 26 (the n = 0 term is 0, n = 1 gives 1, the tail is ≤ ∫_1^∞ = 25). -/
theorem tail_sum_le : ∑' n : ℕ, ((n:ℝ) ^ (-(26:ℝ)/25)) ≤ 26 := by
  set f : ℝ → ℝ := fun x => x ^ (-(26:ℝ)/25) with hf
  have h21 : ((2:ℕ) - 1 : ℝ) = 1 := by norm_num
  have hanti : AntitoneOn f (Ici ((2:ℕ) - 1 : ℝ)) := by
    rw [h21]
    intro x hx y hy hxy
    simp only [hf]
    have hx1 : (1:ℝ) ≤ x := hx
    exact Real.rpow_le_rpow_of_nonpos (by linarith) hxy (by norm_num)
  have hint : IntegrableOn f (Ioi ((2:ℕ) - 1 : ℝ)) := by
    rw [h21]
    exact integrableOn_Ioi_rpow_of_lt (by norm_num : (-(26:ℝ)/25) < -1) (by norm_num : (0:ℝ) < 1)
  have hnn : ∀ t ∈ Ioi ((2:ℕ) - 1 : ℝ), 0 ≤ f t := by
    rw [h21]
    intro t ht; simp only [hf]; have : (1:ℝ) < t := ht
    positivity
  have h := AntitoneOn.abs_tsum_sub_sum_range_le_integral (f := f) (N := 2) (by norm_num) hanti hint hnn
  have hI : ∫ x in Ioi ((2:ℕ) - 1 : ℝ), f x = 25 := by
    rw [h21]
    simp only [hf]
    rw [integral_Ioi_rpow_of_lt (by norm_num : (-(26:ℝ)/25) < -1) (by norm_num : (0:ℝ) < 1)]
    norm_num
  have hsum : ∑ n ∈ Finset.range 2, f n = 1 := by
    simp [hf, Finset.sum_range_succ]
  rw [hI, hsum] at h
  have := (abs_le.1 h).2
  simp only [hf] at this ⊢
  linarith

/-- Section 6, the constant chain: if j_0 ≤ c := log(9/8), 0 ≤ j_n, and j_n ≤ 2 n^(-13/25) for n ≥ 1,
    then 2 ∑ j_n^2 ≤ 2 c^2 + 8 ∑_{n≥1} n^(-26/25) < 209. -/
theorem entropy_constant_chain (j : ℕ → ℝ) (hnn : ∀ n, 0 ≤ j n)
    (hj0 : j 0 ≤ Real.log (9/8))
    (hjn : ∀ n : ℕ, 1 ≤ n → j n ≤ 2 * (n:ℝ) ^ (-(13:ℝ)/25)) :
    ∑' n : ℕ, 2 * (j n) ^ 2 < 209 := by
  have c_pos : 0 < Real.log (9/8) := Real.log_pos (by norm_num)
  have c_lt : Real.log (9/8) < 1/8 := by
    have h := Real.log_lt_sub_one_of_pos (by norm_num : (0:ℝ) < 9/8) (by norm_num : (9/8:ℝ) ≠ 1)
    linarith
  -- dominating sequence g: g 0 = 2 c^2, g n = 8 n^(-26/25) for n ≥ 1
  set g : ℕ → ℝ := fun n => if n = 0 then 2 * (Real.log (9/8)) ^ 2 else 8 * (n:ℝ) ^ (-(26:ℝ)/25) with hg
  have hle : ∀ n, 2 * (j n) ^ 2 ≤ g n := by
    intro n
    by_cases h0 : n = 0
    · subst h0; simp only [hg, if_true]
      have := hnn 0
      nlinarith [hj0, this]
    · simp only [hg, h0, if_false]
      have hn1 : 1 ≤ n := Nat.one_le_iff_ne_zero.2 h0
      have hb := hjn n hn1
      have hpos : (0:ℝ) < n := by exact_mod_cast hn1
      have hsq : (j n) ^ 2 ≤ (2 * (n:ℝ) ^ (-(13:ℝ)/25)) ^ 2 := by
        have := hnn n
        exact pow_le_pow_left₀ this hb 2
      have hrp : ((n:ℝ) ^ (-(13:ℝ)/25)) ^ 2 = (n:ℝ) ^ (-(26:ℝ)/25) := by
        rw [← Real.rpow_natCast, ← Real.rpow_mul hpos.le]; norm_num
      calc 2 * (j n) ^ 2 ≤ 2 * (2 * (n:ℝ) ^ (-(13:ℝ)/25)) ^ 2 := by gcongr
        _ = 8 * ((n:ℝ) ^ (-(13:ℝ)/25)) ^ 2 := by ring
        _ = 8 * (n:ℝ) ^ (-(26:ℝ)/25) := by rw [hrp]
  -- g is summable and its sum is 2 c^2 + 8 ∑ n^(-26/25) ≤ 2 c^2 + 208
  have htail : Summable (fun n : ℕ => (n:ℝ) ^ (-(26:ℝ)/25)) := by
    have := Real.summable_nat_rpow_inv.2 (by norm_num : (1:ℝ) < 26/25)
    refine this.congr ?_
    intro n; rw [← Real.rpow_neg (Nat.cast_nonneg n)]; norm_num
  have hg_eq : g = (fun n : ℕ => (if n = 0 then 2 * (Real.log (9/8)) ^ 2 else 0) + 8 * (n:ℝ) ^ (-(26:ℝ)/25)) := by
    funext n; simp only [hg]; split_ifs with h0
    · subst h0; simp
    · simp
  have hsum_g : Summable g := by
    rw [hg_eq]
    exact (summable_of_ne_finset_zero (s := {0}) (by intro n hn; simp at hn; simp [hn])).add (htail.mul_left 8)
  have hg_val : ∑' n, g n ≤ 2 * (Real.log (9/8)) ^ 2 + 8 * 26 := by
    rw [hg_eq, Summable.tsum_add (summable_of_ne_finset_zero (s := {0}) (by intro n hn; simp at hn; simp [hn])) (htail.mul_left 8)]
    rw [tsum_eq_single 0 (by intro n hn; simp [hn]), tsum_mul_left]
    simp only [if_true]
    have := tail_sum_le
    nlinarith [this]
  have hsum_j : Summable (fun n => 2 * (j n) ^ 2) :=
    Summable.of_nonneg_of_le (fun n => by positivity) hle hsum_g
  calc ∑' n, 2 * (j n) ^ 2 ≤ ∑' n, g n := Summable.tsum_le_tsum hle hsum_j hsum_g
    _ ≤ 2 * (Real.log (9/8)) ^ 2 + 8 * 26 := hg_val
    _ < 209 := by nlinarith [c_pos, c_lt]


#print axioms BC23.psi_prod_le
#print axioms BC23.tail_sum_le
#print axioms BC23.entropy_constant_chain

-- ===== appended: contraction to geometric decay (BC23Contraction) =====
/-!
# From a uniform L² contraction to geometric decay of the fibre deficits

Let `j n = E psi(u_n)` be the fibre deficit and `e n = E[u_n^2]` the second moment of the
bias.  The two pointwise inequalities `t^2 ≤ 2 psi t` and `psi t ≤ t^2 psi 1` (|t| ≤ 1)
integrate to `e n ≤ 2 j n` and `j n ≤ psi 1 * e n`.  If the signed three-preimage average
contracts uniformly, `e (n+1) ≤ (1 - κ) e n`, then `j (n+1) ≤ ρ j n` with
`ρ = 2 psi 1 (1 - κ)`, and `ρ < 1` gives summability with the explicit bound
`∑ j n ≤ j 0 / (1 - ρ)`.  Since `psi 1 = ∑ 1/(2k(2k-1)) = log 2`, the threshold is
`κ > 1 - 1/(2 log 2) ≈ 0.279`; the measured values of κ are 0.71 to 0.98.
The contraction hypothesis itself is the open statement; nothing here proves it.
-/



/-- `psi t ≤ t^2 psi 1` for |t| ≤ 1: the series is termwise dominated. -/
theorem psi_le_sq_mul {t : ℝ} (ht : |t| ≤ 1) : psi t ≤ t ^ 2 * psi 1 := by
  have h := psi_mul_le (u := 1) (v := t) (by simp) ht
  simpa using h

/-- Geometric decay of the deficits from a uniform L² contraction of the bias. -/
theorem summable_of_L2_contraction (j e : ℕ → ℝ) (κ : ℝ)
    (hκ1 : 1 - κ ≥ 0)
    (hρ : 2 * psi 1 * (1 - κ) < 1)
    (hnn : ∀ n, 0 ≤ j n)
    (hje : ∀ n, j n ≤ psi 1 * e n)
    (hej : ∀ n, e n ≤ 2 * j n)
    (hcon : ∀ n, e (n + 1) ≤ (1 - κ) * e n) :
    Summable j ∧ ∑' n, j n ≤ j 0 / (1 - 2 * psi 1 * (1 - κ)) := by
  set ρ := 2 * psi 1 * (1 - κ) with hρdef
  have hpsi1 : 0 ≤ psi 1 := by
    unfold psi
    exact tsum_nonneg (fun k => psiTerm_nonneg 1 k)
  have hρ0 : 0 ≤ ρ := by rw [hρdef]; positivity
  -- one step: j (n+1) ≤ ρ j n
  have hstep : ∀ n, j (n + 1) ≤ ρ * j n := by
    intro n
    have h1 := hje (n + 1)
    have h2 := hcon n
    have h3 := hej n
    have h4 : psi 1 * e (n + 1) ≤ psi 1 * ((1 - κ) * e n) := by gcongr
    have h5 : (1 - κ) * e n ≤ (1 - κ) * (2 * j n) := by gcongr
    have h6 : psi 1 * ((1 - κ) * e n) ≤ psi 1 * ((1 - κ) * (2 * j n)) := by gcongr
    calc j (n + 1) ≤ psi 1 * e (n + 1) := h1
      _ ≤ psi 1 * ((1 - κ) * e n) := h4
      _ ≤ psi 1 * ((1 - κ) * (2 * j n)) := h6
      _ = ρ * j n := by rw [hρdef]; ring
  -- iterate: j n ≤ ρ^n j 0
  have hgeom : ∀ n, j n ≤ ρ ^ n * j 0 := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      calc j (n + 1) ≤ ρ * j n := hstep n
        _ ≤ ρ * (ρ ^ n * j 0) := by gcongr
        _ = ρ ^ (n + 1) * j 0 := by ring
  have hρ1 : ρ < 1 := hρ
  have hsg : Summable (fun n : ℕ => ρ ^ n * j 0) :=
    (summable_geometric_of_lt_one hρ0 hρ1).mul_right (j 0)
  have hsum : Summable j :=
    Summable.of_nonneg_of_le hnn hgeom hsg
  refine ⟨hsum, ?_⟩
  have htsum : ∑' n, ρ ^ n * j 0 = j 0 / (1 - ρ) := by
    rw [tsum_mul_right, tsum_geometric_of_lt_one hρ0 hρ1]
    field_simp
  calc ∑' n, j n ≤ ∑' n, ρ ^ n * j 0 := hsum.tsum_le_tsum hgeom hsg
    _ = j 0 / (1 - ρ) := htsum

end BC23

#print axioms BC23.psi_le_sq_mul
#print axioms BC23.summable_of_L2_contraction
