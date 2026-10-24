import Mathlib.Tactic
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Gamma.BohrMollerup
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Analysis.Convex.Jensen
import Mathlib.LinearAlgebra.Matrix.Gershgorin
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.Rank

/-!
Formal checks for "Quadratic forms with nine large eigenvalues have bounded densities".
Each theorem names the statement of the paper it checks. The analytic theorems of the paper
(Fourier inversion, Brascamp-Lieb, Theorem 4.1) are not formalized here; what is checked is every
numerical constant, every elementary inequality used in a proof, and the finite linear-algebraic
and combinatorial steps.
-/

open Real

namespace QformNine

/-! ## Constants of Sections 6 and 7: eta = 3/40, zeta = 1/400, kappa = 4/625 -/

/-- (6.2): with no pivot, a_ij^2 < eta^2 + zeta = 13/1600, and sqrt(13/1600) < 1/11. -/
theorem small_entry_bound : (3/40 : ℝ)^2 + 1/400 = 13/1600 ∧ Real.sqrt (13/1600 : ℝ) < 1/11 := by
  refine ⟨by norm_num, ?_⟩
  rw [Real.sqrt_lt' (by norm_num)]
  norm_num

/-- sqrt(kappa) = 2/25. -/
theorem sqrt_kappa : Real.sqrt (4/625 : ℝ) = 2/25 := by
  rw [show (4/625 : ℝ) = (2/25)^2 by norm_num]
  exact Real.sqrt_sq (by norm_num)

/-- eta^{-1/2} = sqrt(40/3) < 3.6515, zeta^{-1/2} = 20 and zeta^{-1/4} = sqrt 20 < 4.4722. -/
theorem pivot_scales :
    ((3:ℝ)/40) ^ (-(1:ℝ)/2) = Real.sqrt (40/3) ∧ Real.sqrt (40/3 : ℝ) < 3.6515 ∧
    ((1:ℝ)/400) ^ (-(1:ℝ)/2) = 20 ∧ ((1:ℝ)/400) ^ (-(1:ℝ)/4) = Real.sqrt 20 ∧
    Real.sqrt (20:ℝ) < 4.4722 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [show ((3:ℝ)/40) = ((40:ℝ)/3)^(-(1:ℝ)) by norm_num [Real.rpow_neg_one],
      ← Real.rpow_mul (by norm_num), Real.sqrt_eq_rpow]
    norm_num
  · rw [Real.sqrt_lt' (by norm_num)]; norm_num
  · rw [show ((1:ℝ)/400) = (20:ℝ)^(-(2:ℝ)) by norm_num [Real.rpow_neg, Real.rpow_two]]
    rw [← Real.rpow_mul (by norm_num)]
    norm_num
  · rw [show ((1:ℝ)/400) = (20:ℝ)^(-(2:ℝ)) by norm_num [Real.rpow_neg, Real.rpow_two]]
    rw [← Real.rpow_mul (by norm_num), Real.sqrt_eq_rpow]
    norm_num
  · rw [Real.sqrt_lt' (by norm_num)]; norm_num

/-- Proposition 6.4, the case r = 0: eta + sqrt(kappa) < 1. -/
theorem prop_volume_r0 : (3/40 : ℝ) + Real.sqrt (4/625) < 1 := by
  rw [sqrt_kappa]; norm_num

/-- Proposition 6.4: (r+1) sqrt(kappa) <= 6/25 for r <= 2, and the margins of the contradiction. -/
theorem prop_volume_margins (r : ℕ) (hr : r ≤ 2) :
    ((r:ℝ) + 1) * Real.sqrt (4/625) ≤ 6/25 ∧ (1:ℝ) - 6/25 - 3/40 = 137/200 ∧
    (1/11 : ℝ) + 6/25 < 1/3 ∧ (2:ℝ) * (1/3) < 137/200 := by
  rw [sqrt_kappa]
  have : (r:ℝ) ≤ 2 := by exact_mod_cast hr
  refine ⟨by nlinarith, by norm_num, by norm_num, by norm_num⟩

/-- Proposition 6.4, last step (with Lemma 2.7): a matrix of size r+1 <= 3 whose diagonal entries have
modulus at least 1 - eps - 3/40 and whose off-diagonal entries have modulus less than 1/11 + eps,
0 <= eps <= 6/25, is invertible. -/
theorem prop_volume_core (r : ℕ) (hr : r ≤ 2) (R : Matrix (Fin (r+1)) (Fin (r+1)) ℝ) (ε : ℝ)
    (hε0 : 0 ≤ ε) (hε : ε ≤ 6/25)
    (hdiag : ∀ i, 1 - ε - 3/40 ≤ |R i i|) (hoff : ∀ i j, i ≠ j → |R i j| < 1/11 + ε) :
    R.det ≠ 0 := by
  apply det_ne_zero_of_sum_row_lt_diag
  intro k
  have hcard : (Finset.univ.erase k).card = r := by
    rw [Finset.card_erase_of_mem (Finset.mem_univ k), Finset.card_univ, Fintype.card_fin]
    omega
  have hr' : (r:ℝ) ≤ 2 := by exact_mod_cast hr
  calc ∑ j ∈ Finset.univ.erase k, ‖R k j‖
      ≤ ∑ j ∈ Finset.univ.erase k, (1/11 + ε) := by
        apply Finset.sum_le_sum
        intro j hj
        have hjk : k ≠ j := fun h => (Finset.mem_erase.mp hj).1 h.symm
        rw [Real.norm_eq_abs]
        exact (hoff k j hjk).le
    _ = (r:ℝ) * (1/11 + ε) := by rw [Finset.sum_const, hcard, nsmul_eq_mul]
    _ ≤ 2 * (1/11 + ε) := by nlinarith
    _ < 1 - ε - 3/40 := by linarith
    _ ≤ ‖R k k‖ := by rw [Real.norm_eq_abs]; exact hdiag k

/-- Proposition 6.4, first step: if V_0 = 1, V_i >= 0 and V_k < kappa^k, then some r < k has
V_r > 0 and V_{r+1} < kappa V_r. -/
theorem telescoping (V : ℕ → ℝ) (hV0 : V 0 = 1) (κ : ℝ) (hκ : 0 < κ) (k : ℕ)
    (hk : V k < κ ^ k) : ∃ r < k, 0 < V r ∧ V (r+1) < κ * V r := by
  by_contra h
  push_neg at h
  have key : ∀ r ≤ k, κ ^ r ≤ V r := by
    intro r
    induction r with
    | zero => intro _; simp [hV0]
    | succ m ih =>
      intro hm
      have h1 := ih (by omega)
      have hpos : 0 < V m := lt_of_lt_of_le (pow_pos hκ m) h1
      have h2 := h m (by omega) hpos
      calc κ ^ (m+1) = κ * κ ^ m := by ring
        _ ≤ κ * V m := by gcongr
        _ ≤ V (m+1) := h2
  linarith [key k le_rfl]

/-- Proposition 7.1: (kappa^3/64)^{-1/6} = 25 and (kappa^2/16)^{-1/8} = 5. -/
theorem volume_scales :
    ((4/625:ℝ)^3/64) ^ (-(1:ℝ)/6) = 25 ∧ ((4/625:ℝ)^2/16) ^ (-(1:ℝ)/8) = 5 := by
  constructor
  · rw [show ((4/625:ℝ)^3/64) = (25:ℝ)^(-(6:ℝ)) by norm_num [Real.rpow_neg, Real.rpow_natCast]]
    rw [← Real.rpow_mul (by norm_num)]
    norm_num
  · rw [show ((4/625:ℝ)^2/16) = (5:ℝ)^(-(8:ℝ)) by norm_num [Real.rpow_neg, Real.rpow_natCast]]
    rw [← Real.rpow_mul (by norm_num)]
    norm_num

/-! ## Elementary inequalities used in the proofs -/

/-- Lemma 3.2: beta log(1/beta) <= 1 - beta for beta > 0. -/
theorem mul_log_inv_le (β : ℝ) (hβ : 0 < β) : β * Real.log (1/β) ≤ 1 - β := by
  have h := Real.log_le_sub_one_of_pos (show 0 < 1/β by positivity)
  calc β * Real.log (1/β) ≤ β * (1/β - 1) := by gcongr
    _ = 1 - β := by field_simp

/-- Lemma 5.1: sqrt(u + d) - sqrt u <= sqrt d. -/
theorem sqrt_add_sub_le (u d : ℝ) (hu : 0 ≤ u) (hd : 0 ≤ d) :
    Real.sqrt (u + d) - Real.sqrt u ≤ Real.sqrt d := by
  have hs : u + d ≤ (Real.sqrt u + Real.sqrt d)^2 := by
    have h1 := Real.sq_sqrt hu
    have h2 := Real.sq_sqrt hd
    nlinarith [Real.sqrt_nonneg u, Real.sqrt_nonneg d, mul_nonneg (Real.sqrt_nonneg u) (Real.sqrt_nonneg d)]
  have h3 := Real.sqrt_le_sqrt hs
  rw [Real.sqrt_sq (by positivity)] at h3
  linarith

/-- Theorem 1.1, indefinite pair: D^{-1/2} log D <= 2/e, in the form log D <= (2/e) sqrt D. -/
theorem log_le_two_div_e_mul_sqrt (D : ℝ) (hD : 0 < D) :
    Real.log D ≤ 2 / Real.exp 1 * Real.sqrt D := by
  have hxpos : 0 < Real.sqrt D := Real.sqrt_pos.mpr hD
  have hlog : Real.log D = 2 * Real.log (Real.sqrt D) := by
    rw [Real.log_sqrt hD.le]; ring
  have key : Real.log (Real.sqrt D) ≤ Real.sqrt D / Real.exp 1 := by
    have h := Real.log_le_sub_one_of_pos (show 0 < Real.sqrt D / Real.exp 1 by positivity)
    rw [Real.log_div hxpos.ne' (Real.exp_pos 1).ne', Real.log_exp] at h
    linarith
  rw [hlog]
  have : 2 / Real.exp 1 * Real.sqrt D = 2 * (Real.sqrt D / Real.exp 1) := by ring
  rw [this]
  linarith

/-- The value 2/e is attained at D = e^2, so the supremum used in the proof of Theorem 1.1 equals 2/e. -/
theorem log_div_sqrt_at_e_sq : Real.log (Real.exp 2) / Real.sqrt (Real.exp 2) = 2 / Real.exp 1 := by
  rw [Real.log_exp, show Real.exp 2 = (Real.exp 1)^2 by rw [← Real.exp_nat_mul]; norm_num,
    Real.sqrt_sq (Real.exp_pos 1).le]

/-- log+ is subadditive on products. -/
theorem logp_mul_le (x y : ℝ) (hx : 0 < x) (hy : 0 < y) :
    max 0 (Real.log (x*y)) ≤ max 0 (Real.log x) + max 0 (Real.log y) := by
  rw [Real.log_mul hx.ne' hy.ne']
  have ha := le_max_left 0 (Real.log x)
  have ha' := le_max_right 0 (Real.log x)
  have hb := le_max_left 0 (Real.log y)
  have hb' := le_max_right 0 (Real.log y)
  exact max_le (by linarith) (by linarith)

/-- Theorem 1.1, indefinite pair: log+(16 sqrt D) <= log 16 + (1/2) log+ D. -/
theorem logp_sixteen_sqrt (D : ℝ) (hD : 0 < D) :
    max 0 (Real.log (16 * Real.sqrt D)) ≤ Real.log 16 + (1/2) * max 0 (Real.log D) := by
  have hs : 0 < Real.sqrt D := Real.sqrt_pos.mpr hD
  rw [Real.log_mul (by norm_num) hs.ne', Real.log_sqrt hD.le]
  have h16 : 0 ≤ Real.log 16 := Real.log_nonneg (by norm_num)
  have hm := le_max_left 0 (Real.log D)
  have hm' := le_max_right 0 (Real.log D)
  apply max_le <;> nlinarith

/-- Lemma 5.3: 1/a + 1/b >= 2/sqrt(ab). -/
theorem recip_sum_ge (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    2 / Real.sqrt (a*b) ≤ 1/a + 1/b := by
  set p := Real.sqrt a with hp
  set q := Real.sqrt b with hq
  have hp0 : 0 < p := Real.sqrt_pos.mpr ha
  have hq0 : 0 < q := Real.sqrt_pos.mpr hb
  have hpa : p^2 = a := Real.sq_sqrt ha.le
  have hqb : q^2 = b := Real.sq_sqrt hb.le
  have hab : Real.sqrt (a*b) = p*q := Real.sqrt_mul ha.le b
  rw [hab, ← hpa, ← hqb]
  have e : (1/p - 1/q)^2 = 1/p^2 + 1/q^2 - 2/(p*q) := by field_simp; ring
  nlinarith [sq_nonneg (1/p - 1/q)]

/-- Lemma 5.3: the cutoff T_1 = (3/4) log 2 satisfies exp(2 T_1) = 2 sqrt 2. -/
theorem hyperbola_cutoff : Real.exp (2 * ((3/4) * Real.log 2)) = 2 * Real.sqrt 2 := by
  rw [show 2 * ((3/4) * Real.log 2) = (3/2) * Real.log 2 by ring,
    show (3/2) * Real.log 2 = Real.log 2 * (3/2) by ring, ← Real.rpow_def_of_pos (by norm_num)]
  rw [show (3/2 : ℝ) = 1 + 1/2 by norm_num, Real.rpow_add (by norm_num), Real.rpow_one,
    Real.sqrt_eq_rpow]

/-- Lemma 5.3: the per-branch constant (15/2) log 2 < 6, and log(1 + 1/m) <= log 2 for m >= 1. -/
theorem hyperbola_constants (m : ℝ) (hm : 1 ≤ m) :
    (15/2) * Real.log 2 < 6 ∧ Real.log (1 + 1/m) ≤ Real.log 2 := by
  constructor
  · have := log_two_lt_d9; norm_num at this; linarith
  · apply Real.log_le_log (by positivity)
    have : 1/m ≤ 1 := by rw [div_le_one (by linarith)]; exact hm
    linarith

/-- Lemma 3.3: for p >= 2, m = floor(p/2) satisfies m >= 1 and m >= p/4, and then
2 pi sqrt e / sqrt(2m) <= 2 pi sqrt(2e) / sqrt p. -/
theorem fpower_floor (p : ℝ) (hp : 2 ≤ p) :
    (1:ℝ) ≤ ⌊p/2⌋ ∧ p/4 ≤ (⌊p/2⌋ : ℝ) ∧
    2 * π * Real.sqrt (Real.exp 1) / Real.sqrt (2 * ⌊p/2⌋) ≤ 2 * π * Real.sqrt (2 * Real.exp 1) / Real.sqrt p := by
  have h1 : (1:ℤ) ≤ ⌊p/2⌋ := by rw [Int.le_floor]; push_cast; linarith
  have h1' : (1:ℝ) ≤ ⌊p/2⌋ := by exact_mod_cast h1
  have h2 : p/2 - 1 < ⌊p/2⌋ := by have := Int.sub_one_lt_floor (p/2); linarith
  have h4 : p/4 ≤ (⌊p/2⌋ : ℝ) := by
    by_cases h : 4 ≤ p
    · linarith
    · linarith
  refine ⟨h1', h4, ?_⟩
  set m : ℝ := ((⌊p/2⌋ : ℤ) : ℝ) with hmdef
  have hpp : 0 < p := by linarith
  have hm0 : 0 < m := by linarith
  -- sqrt(2m) >= sqrt(p/2) and sqrt(2e) = sqrt 2 sqrt e
  have hs1 : Real.sqrt (p/2) ≤ Real.sqrt (2*m) := Real.sqrt_le_sqrt (by linarith)
  have hs2 : Real.sqrt (p/2) * Real.sqrt 2 = Real.sqrt p := by
    rw [← Real.sqrt_mul (by positivity)]; congr 1; ring
  have hs3 : Real.sqrt (2 * Real.exp 1) = Real.sqrt 2 * Real.sqrt (Real.exp 1) := Real.sqrt_mul (by norm_num) _
  rw [hs3, ← hs2]
  have hq : 0 < Real.sqrt (p/2) := Real.sqrt_pos.mpr (by positivity)
  have hq2 : 0 < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hA : 0 ≤ 2 * π * Real.sqrt (Real.exp 1) := by positivity
  rw [show 2 * π * (Real.sqrt 2 * Real.sqrt (Real.exp 1)) / (Real.sqrt (p/2) * Real.sqrt 2)
      = 2 * π * Real.sqrt (Real.exp 1) / Real.sqrt (p/2) by field_simp]
  exact div_le_div_of_nonneg_left hA hq hs1

/-- Lemma 2.3: 4^{1/4}/(2 sqrt pi) = 1/sqrt(2 pi). -/
theorem halfmoment_constant : (4:ℝ)^((1:ℝ)/4) / (2 * Real.sqrt π) = 1 / Real.sqrt (2 * π) := by
  have h4 : (4:ℝ)^((1:ℝ)/4) = Real.sqrt 2 := by
    rw [show (4:ℝ) = 2^(2:ℝ) by norm_num, ← Real.rpow_mul (by norm_num), Real.sqrt_eq_rpow]; norm_num
  rw [h4, Real.sqrt_mul (by norm_num)]
  have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  have hpi : 0 < Real.sqrt π := Real.sqrt_pos.mpr Real.pi_pos
  have hs : 0 < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  field_simp
  nlinarith [h2]

/-- Lemma 2.2: 2a + 2 a^p a^{1-p}/(p-1) = 2ap/(p-1). -/
theorem envelope_integral (a p : ℝ) (ha : 0 < a) (hp : 1 < p) :
    2*a + 2 * a^p * (a^(1-p) / (p-1)) = 2*a*p/(p-1) := by
  have h : a^p * a^(1-p) = a := by rw [← Real.rpow_add ha]; simp
  have hp1 : p - 1 ≠ 0 := by linarith
  field_simp
  rw [h]
  ring

/-! ## The constants of Corollary 4.4, Lemmas 5.4-5.6 and Section 7 -/

/-- Corollary 4.4(a): C_3 = 3 sqrt 2 e (9/2)^{1/6} < 15. -/
theorem C3_lt : 3 * Real.sqrt 2 * Real.exp 1 * (9/2 : ℝ) ^ ((1:ℝ)/6) < 15 := by
  set x := (9/2 : ℝ) ^ ((1:ℝ)/6) with hx
  have hx6 : x ^ 6 = 9/2 := by
    rw [hx, ← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  have hs6 : Real.sqrt 2 ^ 6 = 8 := by
    have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
    calc Real.sqrt 2 ^ 6 = (Real.sqrt 2 ^ 2)^3 := by ring
      _ = 8 := by rw [h2]; norm_num
  have hC6 : (3 * Real.sqrt 2 * Real.exp 1 * x)^6 = 26244 * Real.exp 1 ^ 6 := by
    rw [mul_pow, mul_pow, mul_pow, hs6, hx6]; ring
  have he6 : Real.exp 1 ^ 6 < 2.7182818286 ^ 6 := by
    gcongr; exact exp_one_lt_d9
  have hlt : (3 * Real.sqrt 2 * Real.exp 1 * x)^6 < 15^6 := by
    rw [hC6]; nlinarith [he6]
  have hpos : 0 ≤ 3 * Real.sqrt 2 * Real.exp 1 * x := by positivity
  exact lt_of_pow_lt_pow_left₀ 6 (by norm_num) hlt

/-- Corollary 4.4(b): C_2 = 8 e^{1/2} 2^{-1/8} < 12.2. -/
theorem C2_lt : 8 * Real.sqrt (Real.exp 1) * (2:ℝ) ^ (-(1:ℝ)/8) < 12.2 := by
  set y := (2:ℝ) ^ (-(1:ℝ)/8) with hy
  have hy8 : y ^ 8 = 1/2 := by
    rw [hy, ← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num [Real.rpow_neg_one]
  have hse : Real.sqrt (Real.exp 1) ^ 8 = Real.exp 1 ^ 4 := by
    have h2 : Real.sqrt (Real.exp 1) ^ 2 = Real.exp 1 := Real.sq_sqrt (Real.exp_pos 1).le
    calc Real.sqrt (Real.exp 1) ^ 8 = (Real.sqrt (Real.exp 1) ^ 2)^4 := by ring
      _ = Real.exp 1 ^ 4 := by rw [h2]
  have hC8 : (8 * Real.sqrt (Real.exp 1) * y)^8 = 8388608 * Real.exp 1 ^ 4 := by
    rw [mul_pow, mul_pow, hse, hy8]; ring
  have he4 : Real.exp 1 ^ 4 < 2.7182818286 ^ 4 := by
    gcongr; exact exp_one_lt_d9
  have hlt : (8 * Real.sqrt (Real.exp 1) * y)^8 < (12.2:ℝ)^8 := by
    rw [hC8]; nlinarith [he4]
  have hpos : 0 ≤ 8 * Real.sqrt (Real.exp 1) * y := by positivity
  exact lt_of_pow_lt_pow_left₀ 8 (by norm_num) hlt

/-- Proposition 7.1: 25 C_3 < 375 and 5 C_2 < 61. -/
theorem nopivot_constants :
    25 * (3 * Real.sqrt 2 * Real.exp 1 * (9/2 : ℝ) ^ ((1:ℝ)/6)) < 375 ∧
    5 * (8 * Real.sqrt (Real.exp 1) * (2:ℝ) ^ (-(1:ℝ)/8)) < 61 := by
  constructor
  · have := C3_lt; linarith
  · have := C2_lt; linarith

/-- Lemma 5.4: L_0 = 2 + 2 log 19 < 8. -/
theorem L0_lt : 2 + 2 * Real.log 19 < 8 := by
  have h : Real.log 19 < 3 := by
    rw [Real.log_lt_iff_lt_exp (by norm_num)]
    have he : (2.7182818283:ℝ)^3 < Real.exp 1 ^ 3 := by gcongr; exact exp_one_gt_d9
    have : Real.exp 3 = Real.exp 1 ^ 3 := by rw [← Real.exp_nat_mul]; norm_num
    rw [this]; nlinarith [he]
  linarith

/-- Lemma 5.5: (1 + sqrt(1+d))(1 + sqrt(1-d)) <= 4 for 0 <= d <= 1. -/
theorem kernel_product_le (d : ℝ) (hd0 : 0 ≤ d) (hd1 : d ≤ 1) :
    (1 + Real.sqrt (1+d)) * (1 + Real.sqrt (1-d)) ≤ 4 := by
  have ha : 0 ≤ Real.sqrt (1+d) := Real.sqrt_nonneg _
  have hb : 0 ≤ Real.sqrt (1-d) := Real.sqrt_nonneg _
  have ha2 : Real.sqrt (1+d) ^ 2 = 1+d := Real.sq_sqrt (by linarith)
  have hb2 : Real.sqrt (1-d) ^ 2 = 1-d := Real.sq_sqrt (by linarith)
  have hprod : Real.sqrt (1+d) * Real.sqrt (1-d) ≤ 1 := by
    nlinarith [sq_nonneg (Real.sqrt (1+d) - Real.sqrt (1-d))]
  have hsum : Real.sqrt (1+d) + Real.sqrt (1-d) ≤ 2 := by
    nlinarith [sq_nonneg (Real.sqrt (1+d) - Real.sqrt (1-d)),
      sq_nonneg (Real.sqrt (1+d) + Real.sqrt (1-d) - 2)]
  have e : (1 + Real.sqrt (1+d)) * (1 + Real.sqrt (1-d))
      = 1 + (Real.sqrt (1+d) + Real.sqrt (1-d)) + Real.sqrt (1+d) * Real.sqrt (1-d) := by ring
  rw [e]
  linarith

/-- Lemma 5.5: for 0 < d <= 1, 2 log((1 + sqrt(1+d))(1 + sqrt(1-d))) <= 4 log 2. -/
theorem kernel_log_bound (d : ℝ) (hd0 : 0 < d) (hd1 : d ≤ 1) :
    2 * Real.log ((1 + Real.sqrt (1+d)) * (1 + Real.sqrt (1-d))) ≤ 4 * Real.log 2 := by
  have hpos : 0 < (1 + Real.sqrt (1+d)) * (1 + Real.sqrt (1-d)) := by positivity
  have h := Real.log_le_log hpos (kernel_product_le d hd0.le hd1)
  have h4 : Real.log 4 = 2 * Real.log 2 := by
    rw [show (4:ℝ) = 2^2 by norm_num, Real.log_pow]; norm_num
  linarith

/-- Lemma 5.5: J(1) = pi + 2 log(1 + sqrt 2) < pi + 4 log 2. -/
theorem kernel_at_one : 2 * Real.log (1 + Real.sqrt 2) < 4 * Real.log 2 := by
  have hs : Real.sqrt 2 < 2 := by rw [Real.sqrt_lt' (by norm_num)]; norm_num
  have h : 1 + Real.sqrt 2 < 4 := by linarith
  have h4 : Real.log 4 = 2 * Real.log 2 := by
    rw [show (4:ℝ) = 2^2 by norm_num, Real.log_pow]; norm_num
  have := Real.log_lt_log (by positivity) h
  linarith

/-- Lemma 5.6, (5.10): a density bounded by M > 0 has half potential sqrt(2M) + 2M/sqrt(2M) = 2 sqrt(2M). -/
theorem bounded_half_value (M : ℝ) (hM : 0 < M) :
    Real.sqrt (2*M) + 2*M / Real.sqrt (2*M) = 2 * Real.sqrt (2*M) := by
  have hs : 0 < Real.sqrt (2*M) := Real.sqrt_pos.mpr (by positivity)
  have h2 : Real.sqrt (2*M) * Real.sqrt (2*M) = 2*M := Real.mul_self_sqrt (by positivity)
  have e : 2*M / Real.sqrt (2*M) = Real.sqrt (2*M) := by
    rw [div_eq_iff hs.ne']; exact h2.symm
  rw [e]; ring

/-- Lemma 5.6, definite case: 2 sqrt(2 pi) < 6. -/
theorem definite_pair_half : 2 * Real.sqrt (2 * π) < 6 := by
  have h : Real.sqrt (2 * π) < 3 := by
    rw [Real.sqrt_lt' (by norm_num)]
    have := pi_lt_d2
    nlinarith
  linarith

/-- Lemma 5.6, indefinite case: 4 sqrt(1/64) (8 + log(16/(1/64))) = 4 + 5 log 2, and 8 + 4 + 5 log 2 < 16. -/
theorem pair_half_constants :
    4 * Real.sqrt (1/64) * (8 + Real.log (16 / (1/64))) = 4 + 5 * Real.log 2 ∧
    (8:ℝ) + (4 + 5 * Real.log 2) < 16 := by
  have hs : Real.sqrt (1/64 : ℝ) = 1/8 := by
    rw [show (1/64 : ℝ) = (1/8)^2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  have hl : Real.log (16 / (1/64) : ℝ) = 10 * Real.log 2 := by
    rw [show (16 / (1/64) : ℝ) = 2^10 by norm_num, Real.log_pow]; norm_num
  refine ⟨?_, ?_⟩
  · rw [hs, hl]; ring
  · have := log_two_lt_d9; norm_num at this; linarith

/-- Proposition 7.2: 16 zeta^{-1/4} = 16 sqrt 20 < 72, eta^{-1/2}(pi + 4 log 2 + 2 L_0) < 81, and
81 + 1 = 82 dominates the no-pivot value 61 and the pair value 72. -/
theorem halfpotential_constants :
    16 * Real.sqrt 20 < 72 ∧
    Real.sqrt (40/3) * (π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19)) < 81 ∧
    (81:ℝ) + 1 = 82 ∧ (61:ℝ) ≤ 82 ∧ (72:ℝ) ≤ 82 := by
  obtain ⟨-, h40, -, -, h20⟩ := pivot_scales
  refine ⟨by linarith, ?_, by norm_num, by norm_num, by norm_num⟩
  have hpi := pi_lt_d2
  have hl := log_two_lt_d9
  have hL := L0_lt
  have hs0 : 0 ≤ Real.sqrt (40/3 : ℝ) := Real.sqrt_nonneg _
  have hsum : π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19) < 21.93 := by
    norm_num at hl; linarith
  have hsum0 : 0 ≤ π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19) := by
    have := Real.pi_pos
    have h2 := Real.log_nonneg (show (1:ℝ) ≤ 2 by norm_num)
    have h19 := Real.log_nonneg (show (1:ℝ) ≤ 19 by norm_num)
    linarith
  nlinarith [mul_le_mul_of_nonneg_right h40.le hsum0]

/-- Theorem 1.1: the diagonal pivot sqrt(40/3) 82 < 300, the definite pair 20 pi < 63, the indefinite pair
20(6 + log 16 + L_0) + 1/e < 337, and all of these and the no-pivot value are below 375 <= 400. -/
theorem main_constants :
    Real.sqrt (40/3) * 82 < 300 ∧ 20 * π < 63 ∧
    20 * (6 + Real.log 16 + (2 + 2 * Real.log 19)) + 1 / Real.exp 1 < 337 ∧
    (300:ℝ) < 375 ∧ (63:ℝ) < 375 ∧ (337:ℝ) < 375 ∧ (375:ℝ) ≤ 400 := by
  obtain ⟨-, h40, -, -, -⟩ := pivot_scales
  refine ⟨by linarith, by have := pi_lt_d4; linarith, ?_, by norm_num, by norm_num, by norm_num, by norm_num⟩
  have h16 : Real.log 16 = 4 * Real.log 2 := by
    rw [show (16:ℝ) = 2^4 by norm_num, Real.log_pow]; norm_num
  have hl := log_two_lt_d9
  have h19 : Real.log 19 < 3 := by have := L0_lt; linarith
  have he := exp_one_gt_d9
  have hinv : 1 / Real.exp 1 < 1 := by rw [div_lt_one (Real.exp_pos 1)]; linarith
  rw [one_div] at hinv
  rw [h16]
  norm_num at hl ⊢
  linarith

end QformNine
