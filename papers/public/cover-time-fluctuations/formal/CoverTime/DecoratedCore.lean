/-
Machine-checked finite steps from
"Cover-time fluctuations beyond the maximal hitting-time scale".

Part 2: fixed cores with many leaves (Sections 7-11).

Checked here: the coefficient identities behind the spectral perturbation of Lemma 8.1
(`λ'(0) = 0`, `q λ''(0) = 2 fᵀ L⁺ f` in the form `q λ''(0)/2 = fᵀ r'(0)`), the explicit
eigenvalue of the two-vertex core, the two threshold tail bounds of Lemma 8.2, the
elimination of the leaf states and the linearity of the Dirichlet problem in
Proposition 9.1, the value of the pendant-target vertex, the hitting times on the
double star (10.1) and on the decorated three-vertex path, the two-vertex pseudoinverse,
the two-vertex limit variable of Section 9.1 with its mean and variance, the variance
bound for stars in Proposition 10.2 (with `H^{(2)} ≤ π²/6` from Mathlib), the constants
of Theorem 10.1, and the variance identity of Proposition 11.1.
-/
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Real.Sqrt
import Mathlib.NumberTheory.ZetaValues
import Mathlib.Data.Fin.VecNotation

open Finset

namespace CoverTime.DecoratedCore

/-! ### Lemma 8.1: the perturbation coefficients -/

/-- Column sums of a Laplacian vanish, so `∑ᵢ (L v)ᵢ = 0` for every `v`. -/
theorem sum_mulVec_eq_zero {n : Type*} [Fintype n] (L : Matrix n n ℝ)
    (hL : ∀ j, ∑ i, L i j = 0) (v : n → ℝ) : ∑ i, (L.mulVec v) i = 0 := by
  simp only [Matrix.mulVec, dotProduct]
  rw [Finset.sum_comm]
  apply Finset.sum_eq_zero
  intro j _
  rw [← Finset.sum_mul, hL j, zero_mul]

/-- Matching the coefficients of `z` and `z²` in `(-L + z D_f) r(z) = λ(z) r(z)` with
`r(0) = 1`, `λ(0) = 0`, `r'(0) = r1`, `r''(0)/2 = r2`, `λ'(0) = l1`, `λ''(0)/2 = l2`:
the `z` coefficient reads `-L r1 + f = l1 · 1`, the `z²` coefficient reads
`-L r2 + f ∘ r1 = l2 · 1 + l1 r1`. Summing over the vertices with `1ᵀ L = 0` and `1ᵀ f = 0`
gives `λ'(0) = 0` and `q λ''(0)/2 = fᵀ r'(0)`; with `r'(0) = L⁺ f` this is
`λ''(0) = (2/q) fᵀ L⁺ f`. -/
theorem perturbation_coefficients {n : Type*} [Fintype n] (L : Matrix n n ℝ)
    (hL : ∀ j, ∑ i, L i j = 0) (f r1 r2 : n → ℝ) (l1 l2 : ℝ)
    (h1 : ∀ i, -(L.mulVec r1) i + f i = l1)
    (h2 : ∀ i, -(L.mulVec r2) i + f i * r1 i = l2 + l1 * r1 i)
    (hf : ∑ i, f i = 0) (hq : 0 < Fintype.card n) :
    l1 = 0 ∧ (Fintype.card n : ℝ) * l2 = ∑ i, f i * r1 i := by
  have s1 : ∑ i, (-(L.mulVec r1) i + f i) = ∑ _i : n, l1 :=
    Finset.sum_congr rfl fun i _ => h1 i
  rw [Finset.sum_add_distrib, Finset.sum_neg_distrib, sum_mulVec_eq_zero L hL, hf,
    Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at s1
  have hq' : (Fintype.card n : ℝ) ≠ 0 := by exact_mod_cast hq.ne'
  have hl1 : l1 = 0 := by
    have : (Fintype.card n : ℝ) * l1 = 0 := by linarith
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h hq'
    · exact h
  refine ⟨hl1, ?_⟩
  have s2 : ∑ i, (-(L.mulVec r2) i + f i * r1 i) = ∑ i, (l2 + l1 * r1 i) :=
    Finset.sum_congr rfl fun i _ => h2 i
  rw [Finset.sum_add_distrib, Finset.sum_neg_distrib, sum_mulVec_eq_zero L hL,
    Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul, hl1] at s2
  simp only [zero_mul, Finset.sum_const_zero, add_zero, neg_zero, zero_add] at s2
  exact s2.symm

/-- For the single edge with `f = (a, -a)`: `λ(z) = -1 + √(1 + a²z²)` satisfies the
characteristic equation `λ² + 2λ - a²z² = 0` of `-L + z diag(a, -a)`, it is at least `-1`
(the other root is at most `-1`), and `a²z²/2 - a⁴z⁴/8 ≤ λ(z) ≤ a²z²/2`, so that
`λ(0) = 0`, `λ'(0) = 0` and `λ''(0) = a² = (2/q) fᵀ L⁺ f` with `q = 2`,
`L⁺ = (1/4) [[1,-1],[-1,1]]`. -/
theorem two_vertex_eigenvalue (a z : ℝ) :
    (-1 + Real.sqrt (1 + a ^ 2 * z ^ 2)) ^ 2 + 2 * (-1 + Real.sqrt (1 + a ^ 2 * z ^ 2))
        - a ^ 2 * z ^ 2 = 0 ∧
    -1 ≤ -1 + Real.sqrt (1 + a ^ 2 * z ^ 2) ∧
    a ^ 2 * z ^ 2 / 2 - a ^ 4 * z ^ 4 / 8 ≤ -1 + Real.sqrt (1 + a ^ 2 * z ^ 2) ∧
    -1 + Real.sqrt (1 + a ^ 2 * z ^ 2) ≤ a ^ 2 * z ^ 2 / 2 := by
  have h0 : 0 ≤ 1 + a ^ 2 * z ^ 2 := by positivity
  have hs := Real.sq_sqrt h0
  have hs0 := Real.sqrt_nonneg (1 + a ^ 2 * z ^ 2)
  have hx : 0 ≤ a ^ 2 * z ^ 2 := by positivity
  refine ⟨by linear_combination hs, by linarith, ?_, ?_⟩
  · -- `1 + x/2 - x²/8 ≤ √(1 + x)` with `x = a²z²`
    have hx4 : a ^ 4 * z ^ 4 = (a ^ 2 * z ^ 2) ^ 2 := by ring
    rw [hx4]
    rcases le_or_gt (1 + a ^ 2 * z ^ 2 / 2 - (a ^ 2 * z ^ 2) ^ 2 / 8) 0 with hy | hy
    · linarith
    · have hle : 1 + a ^ 2 * z ^ 2 / 2 - (a ^ 2 * z ^ 2) ^ 2 / 8
          ≤ Real.sqrt (1 + a ^ 2 * z ^ 2) := by
        rw [Real.le_sqrt hy.le h0]
        nlinarith [sq_nonneg (a ^ 2 * z ^ 2), mul_nonneg hx (sq_nonneg (a ^ 2 * z ^ 2))]
      linarith
  · have : Real.sqrt (1 + a ^ 2 * z ^ 2) ≤ 1 + a ^ 2 * z ^ 2 / 2 := by
      rw [Real.sqrt_le_left (by positivity)]
      nlinarith [sq_nonneg (a ^ 2 * z ^ 2)]
    linarith

/-! ### Lemma 8.2: the threshold tails -/

/-- `P(B_{v,k} > log k + u) = 1 - (1 - e^{-u}/k)^k ≤ e^{-u}` for `u ≥ 0`, by Bernoulli's
inequality. -/
theorem threshold_upper_tail (k : ℕ) (hk : 1 ≤ k) (u : ℝ) (hu : 0 ≤ u) :
    1 - (1 - Real.exp (-(Real.log k + u))) ^ k ≤ Real.exp (-u) := by
  have hk0 : (0 : ℝ) < k := by exact_mod_cast hk
  have hx : Real.exp (-(Real.log k + u)) = Real.exp (-u) / k := by
    rw [neg_add, Real.exp_add, Real.exp_neg (Real.log k), Real.exp_log hk0]; ring
  have hb := one_add_mul_le_pow (show (-2 : ℝ) ≤ -(Real.exp (-u) / k) by
    have h1 : Real.exp (-u) ≤ 1 := Real.exp_le_one_iff.mpr (by linarith)
    have h2 : Real.exp (-u) / k ≤ 1 := by
      rw [div_le_one hk0]
      have : (1 : ℝ) ≤ k := by exact_mod_cast hk
      linarith
    linarith) k
  have hb' : 1 - (k : ℝ) * (Real.exp (-u) / k) ≤ (1 - Real.exp (-u) / k) ^ k := by
    simpa [sub_eq_add_neg, mul_neg] using hb
  have hc : (k : ℝ) * (Real.exp (-u) / k) = Real.exp (-u) := by
    field_simp
  rw [hx]
  linarith

/-- `P(B_{v,k} < log k - u) = (1 - e^{u}/k)^k ≤ e^{-e^u}` for `u ≤ log k`. -/
theorem threshold_lower_tail (k : ℕ) (hk : 1 ≤ k) (u : ℝ) (hu' : u ≤ Real.log k) :
    (1 - Real.exp (-(Real.log k - u))) ^ k ≤ Real.exp (-(Real.exp u)) := by
  have hk0 : (0 : ℝ) < k := by exact_mod_cast hk
  have hy : Real.exp (-(Real.log k - u)) = Real.exp u / k := by
    rw [neg_sub, Real.exp_sub, Real.exp_log hk0]
  have hy1 : Real.exp u / k ≤ 1 := by
    rw [div_le_one hk0]
    calc Real.exp u ≤ Real.exp (Real.log k) := Real.exp_le_exp.mpr hu'
      _ = k := Real.exp_log hk0
  have hb : 1 - Real.exp u / k ≤ Real.exp (-(Real.exp u / k)) := by
    have := Real.add_one_le_exp (-(Real.exp u / k))
    linarith
  rw [hy]
  calc (1 - Real.exp u / k) ^ k ≤ Real.exp (-(Real.exp u / k)) ^ k :=
        pow_le_pow_left₀ (by linarith) hb k
    _ = Real.exp (-(Real.exp u)) := by
        rw [← Real.exp_nat_mul]
        congr 1
        field_simp

/-! ### Proposition 9.1: the Dirichlet problems of a decorated core -/

/-- Eliminating the leaf states at a core vertex `u` of core degree `d` carrying `k` leaves:
each leaf satisfies `h_leaf = 1 + h_u`, and the first-step equation
`(d + k) h_u = (d + k) + S + k h_leaf`, with `S` the sum over the core neighbours, becomes
`d h_u - S = 2k + d`, i.e. `(L h)_u = 2k + d_u`. -/
theorem leaf_elimination (d k h S hl : ℚ) (hleaf : hl = 1 + h)
    (hstep : (d + k) * h = (d + k) + S + k * hl) : d * h - S = 2 * k + d := by
  subst hleaf
  linear_combination hstep

/-- At the core vertex `v` of a pendant target there are `k - 1` non-target leaves and the
target is hit in one step: `(d + k) h_v = (d + k) + S + (k - 1)(1 + h_v)` gives
`(L h)_v + h_v = 2k + d_v - 1`. -/
theorem leaf_elimination_target (d k h S : ℚ)
    (hstep : (d + k) * h = (d + k) + S + (k - 1) * (1 + h)) :
    d * h - S + h = 2 * k + d - 1 := by
  linear_combination hstep

/-- Linearity and uniqueness of the Dirichlet problem, (9.2): if the reduced Laplacian `M`
(the target's row and column removed) is invertible and `M h = 2k · 1 + d`, `M T = 1`,
`M H = d`, then `h = 2k T + H`. -/
theorem dirichlet_linearity {n : Type*} [Fintype n] [DecidableEq n]
    (M : Matrix n n ℚ) (hM : IsUnit M) (h T H : n → ℚ) (k : ℚ) (d : n → ℚ)
    (hh : M.mulVec h = fun u => 2 * k + d u)
    (hT : M.mulVec T = fun _ => 1) (hH : M.mulVec H = d) :
    h = (2 * k) • T + H := by
  apply Matrix.mulVec_injective_iff_isUnit.mpr hM
  rw [Matrix.mulVec_add, Matrix.mulVec_smul, hT, hH, hh]
  ext u
  simp

/-- The value at the pendant target's core vertex, (9.1): summing `(L h)_u = 2k + d_u` over
`u ≠ v` and `(L h)_v + h_v = 2k + d_v - 1`, and using `1ᵀ L = 0`, gives
`h_v = 2qk + Σ_u d_u - 1 = 2qk + 2e - 1`. -/
theorem pendant_value {n : Type*} [Fintype n] [DecidableEq n]
    (L : Matrix n n ℚ) (hL : ∀ j, ∑ i, L i j = 0) (h d : n → ℚ) (k : ℚ) (v : n)
    (hu : ∀ u, u ≠ v → (L.mulVec h) u = 2 * k + d u)
    (hv : (L.mulVec h) v + h v = 2 * k + d v - 1) :
    h v = 2 * (Fintype.card n : ℚ) * k + (∑ u, d u) - 1 := by
  have key : ∑ i, (L.mulVec h) i = 0 := by
    simp only [Matrix.mulVec, dotProduct]
    rw [Finset.sum_comm]
    apply Finset.sum_eq_zero
    intro j _
    rw [← Finset.sum_mul, hL j, zero_mul]
  have split : ∑ i ∈ Finset.univ.erase v, (L.mulVec h) i + (L.mulVec h) v
      = ∑ i, (L.mulVec h) i :=
    Finset.sum_erase_add _ _ (Finset.mem_univ v)
  have hsum : ∑ i ∈ Finset.univ.erase v, (L.mulVec h) i
      = ∑ i ∈ Finset.univ.erase v, (2 * k + d i) :=
    Finset.sum_congr rfl fun i hi => hu i (Finset.ne_of_mem_erase hi)
  have hd : ∑ i ∈ Finset.univ.erase v, (2 * k + d i) + (2 * k + d v) = ∑ i, (2 * k + d i) :=
    Finset.sum_erase_add _ _ (Finset.mem_univ v)
  have hall : ∑ i, (2 * k + d i) = 2 * (Fintype.card n : ℚ) * k + ∑ u, d u := by
    rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    ring
  linarith

/-! ### Theorem 10.1: the double star -/

/-- First-step equations on `D_k`: `X = H(c₁,c₂)` satisfies `(k+1)X = (k+1) + k(1+X)`
(a leaf excursion costs two steps), and `Y = H(c₂,a₂)` for a leaf `a₂` of `c₂` satisfies
`(k+1)Y = (k+1) + (k-1)(1+Y) + (X + Y)`. Then `X = 2k + 1`, `Y = 4k + 1`, and the value from
a leaf of `c₁` to a leaf of `c₂` is `1 + X + Y = 6k + 3`, which is (10.1). -/
theorem double_star_hitting (k X Y : ℚ)
    (hX : (k + 1) * X = (k + 1) + k * (1 + X))
    (hY : (k + 1) * Y = (k + 1) + (k - 1) * (1 + Y) + (X + Y)) :
    X = 2 * k + 1 ∧ Y = 4 * k + 1 ∧ 1 + X + Y = 6 * k + 3 :=
  ⟨by linear_combination hX, by linear_combination hX + hY,
   by linear_combination 2 * hX + hY⟩

/-- The other leaf-to-leaf value on `D_k` (both leaves at one centre) is `1 + (4k + 1)`,
which is smaller, and the core-to-leaf values are smaller still. -/
theorem double_star_max (k : ℚ) (hk : 1 ≤ k) :
    1 + (4 * k + 1) ≤ 6 * k + 3 ∧ 4 * k + 1 ≤ 6 * k + 3 ∧
      2 * k + 1 + (4 * k + 1) ≤ 6 * k + 3 :=
  ⟨by linarith, by linarith, by linarith⟩

/-- (9.3) for the single-edge core, `q = 2`, `e = 1`, `T_F = H_F = 1`: `4k + 2 + 2k + 1 = 6k + 3`. -/
theorem double_star_from_formula (k : ℚ) :
    2 * 2 * k + 2 * 1 + (2 * k * 1 + 1) = 6 * k + 3 := by ring

/-- The decorated three-vertex path `a - b - c` with `k` leaves at each vertex, target `c`:
the first-step equations give `H(a,c) = 6k + 4` and `H(b,c) = 4k + 3`, which is (9.2) with
`T_F(a,c) = 3`, `H_F(a,c) = 4`, `T_F(b,c) = 2`, `H_F(b,c) = 3`. -/
theorem path3_core_hitting (k ha hb : ℚ)
    (h1 : (1 + k) * ha = (1 + k) + hb + k * (1 + ha))
    (h2 : (2 + k) * hb = (2 + k) + ha + k * (1 + hb)) :
    ha = 6 * k + 4 ∧ hb = 4 * k + 3 :=
  ⟨by linear_combination 2 * h1 + h2, by linear_combination h1 + h2⟩

/-- The two-vertex Laplacian and its Moore-Penrose inverse: with `L = [[1,-1],[-1,1]]` and
`L⁺ = (1/4) L`, the four Penrose equations hold, `L⁺ 1 = 0`, and `L⁺ (1,-1) = (1/2, -1/2)`. -/
theorem two_vertex_pseudoinverse :
    let L : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of ![![1, -1], ![-1, 1]]
    let Lp : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of ![![1 / 4, -1 / 4], ![-1 / 4, 1 / 4]]
    L * Lp * L = L ∧ Lp * L * Lp = Lp ∧ (L * Lp).transpose = L * Lp ∧
      (Lp * L).transpose = Lp * L ∧ Lp.mulVec (fun _ => 1) = 0 ∧
      Lp.mulVec ![1, -1] = ![1 / 2, -1 / 2] := by
  intro L Lp
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [L, Lp, Matrix.mul_apply, Fin.sum_univ_two] <;> norm_num
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [L, Lp, Matrix.mul_apply, Fin.sum_univ_two] <;> norm_num
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [L, Lp, Matrix.mul_apply, Fin.sum_univ_two, Matrix.transpose_apply] <;> norm_num
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [L, Lp, Matrix.mul_apply, Fin.sum_univ_two, Matrix.transpose_apply] <;> norm_num
  · ext i
    fin_cases i <;> simp [Lp, Matrix.mulVec, dotProduct, Fin.sum_univ_two] <;> norm_num
  · ext i
    fin_cases i <;> simp [Lp, Matrix.mulVec, dotProduct, Fin.sum_univ_two] <;> norm_num

/-! ### Section 9.1: the two-vertex unequal decoration -/

/-- With `X_F = (s z/2, -s z/2)`, `s = √2` (so `s z/2 = z/√2`), the limit variable (9.7)
`a X₁ + b X₂ - (a + b) min(X₁, X₂)` equals `√2 (a Z₊ + b (-Z)₊)`. -/
theorem two_vertex_G (a b z s : ℝ) (hs : 0 < s) :
    a * (s * z / 2) + b * (-(s * z / 2)) - (a + b) * min (s * z / 2) (-(s * z / 2))
      = s * (a * max z 0 + b * max (-z) 0) := by
  rcases le_or_gt 0 z with hz | hz
  · rw [max_eq_left hz, max_eq_right (by linarith : -z ≤ 0),
      min_eq_right (by nlinarith [mul_nonneg hs.le hz])]
    ring
  · rw [max_eq_right hz.le, max_eq_left (by linarith : (0 : ℝ) ≤ -z),
      min_eq_left (by nlinarith [mul_nonneg hs.le (by linarith : (0 : ℝ) ≤ -z)])]
    ring

/-- Its mean and variance, with `m = E Z₊`, `m² = 1/(2π)`, `E Z₊² = 1/2`, `s² = 2`:
`(E G)² = (a + b)²/π` and `Var G = a² + b² - (a + b)²/π`. -/
theorem two_vertex_G_moments (a b s m : ℝ) (hs : s ^ 2 = 2) (hm : m ^ 2 = 1 / (2 * Real.pi)) :
    (s * (a + b) * m) ^ 2 = (a + b) ^ 2 / Real.pi ∧
    s ^ 2 * (a ^ 2 * (1 / 2) + b ^ 2 * (1 / 2)) - (s * (a + b) * m) ^ 2
      = a ^ 2 + b ^ 2 - (a + b) ^ 2 / Real.pi := by
  have hpi : Real.pi ≠ 0 := Real.pi_ne_zero
  constructor
  · rw [mul_pow, mul_pow, hs, hm]; field_simp
  · rw [mul_pow, mul_pow, hs, hm]; field_simp

/-! ### Proposition 10.2: stars -/

/-- `H_r^{(2)} = ∑_{j=1}^r 1/j² ≤ π²/6`. -/
theorem harmonic2_le (r : ℕ) : ∑ j ∈ Icc 1 r, (1 : ℝ) / (j : ℝ) ^ 2 ≤ Real.pi ^ 2 / 6 :=
  sum_le_hasSum (Icc 1 r) (fun j _ => by positivity) hasSum_zeta_two

/-- The star with `k` leaves: `H(centre, leaf) = 2k - 1` from `k h = k + (k-1)(1 + h)`, so the
leaf-to-leaf hitting time is `2k`. -/
theorem star_hitting (k h : ℚ) (hstep : k * h = k + (k - 1) * (1 + h)) :
    h = 2 * k - 1 ∧ 1 + h = 2 * k :=
  ⟨by linear_combination hstep, by linear_combination hstep⟩

/-- `Var_s(τ_cov) = 4(k² H_k^{(2)} - k H_k) ≤ 2π²k²/3`, and with `t_hit = 2k` the ratio
`Var/t_hit² ≤ π²/6`, i.e. `SD/t_hit ≤ π/√6`. -/
theorem star_variance_bound (k : ℕ) (hk : 2 ≤ k) :
    4 * ((k : ℝ) ^ 2 * (∑ j ∈ Icc 1 k, (1 : ℝ) / (j : ℝ) ^ 2)
        - k * (∑ j ∈ Icc 1 k, (1 : ℝ) / j))
      ≤ 2 * Real.pi ^ 2 / 3 * (k : ℝ) ^ 2 ∧
    (4 * ((k : ℝ) ^ 2 * (∑ j ∈ Icc 1 k, (1 : ℝ) / (j : ℝ) ^ 2)
        - k * (∑ j ∈ Icc 1 k, (1 : ℝ) / j))) / (2 * (k : ℝ)) ^ 2 ≤ Real.pi ^ 2 / 6 := by
  have h2 := harmonic2_le k
  have h1 : 0 ≤ ∑ j ∈ Icc 1 k, (1 : ℝ) / j := sum_nonneg fun j _ => by positivity
  have hk0 : (0 : ℝ) < k := by exact_mod_cast (by omega : 0 < k)
  have hA := mul_le_mul_of_nonneg_left h2 (sq_nonneg (k : ℝ))
  have hB := mul_nonneg hk0.le h1
  constructor
  · nlinarith
  · rw [div_le_iff₀ (by positivity)]
    nlinarith

/-! ### Theorem 10.1 from Theorem 7.1: the constants -/

/-- With `q = 2` and `M_F = |Z|/√2`: the scale `2qk√ℓ · (1/√2) = 2√2 k√ℓ` of (10.2); the mean
coefficient `4 · E|Z|/√2 = 4 · (√2/√π)/√2 = 4/√π` of (10.3); the variance coefficient
`4q² · Var|Z|/2 = 8(1 - 2/π)` of (10.4); and the squared constants of (10.5),
`(2√2)²/(2√6)² = 1/3` and `8(1 - 2/π)/36 = (2/9)(1 - 2/π)`. Written with `s = √2`,
`p = √π`, `r = √6`. -/
theorem double_star_constants (s p r : ℝ) (hs : s ^ 2 = 2) (hp : p ^ 2 = Real.pi)
    (hr : r ^ 2 = 6) (hs0 : 0 < s) (hp0 : 0 < p) (hr0 : 0 < r) :
    2 * 2 * (1 / s) = 2 * s ∧
    4 * ((s / p) / s) = 4 / p ∧
    4 * 2 ^ 2 * ((1 - 2 / Real.pi) / 2) = 8 * (1 - 2 / Real.pi) ∧
    (2 * s) ^ 2 / (2 * r) ^ 2 = 1 / 3 ∧
    8 * (1 - 2 / Real.pi) / 6 ^ 2 = 2 / 9 * (1 - 2 / Real.pi) := by
  have hs' : s ≠ 0 := hs0.ne'
  have hp' : p ≠ 0 := hp0.ne'
  have hr' : r ≠ 0 := hr0.ne'
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · field_simp
    nlinarith [hs]
  · field_simp
  · ring
  · rw [mul_pow, mul_pow, hs, hr]
    norm_num
  · ring

/-! ### Corollary 9.2: the geometric-mean ratio -/

/-- From (7.4), (9.4) and (7.3): `4q²k²ℓ Var(M_F) / (2k(q + T_*) · 2qkℓ) = q Var(M_F)/(q + T_*)`. -/
theorem geometric_mean_ratio (q T k ℓ V : ℝ) (hq : 0 < q) (hT : 0 < T) (hk : 0 < k)
    (hℓ : 0 < ℓ) :
    4 * q ^ 2 * k ^ 2 * ℓ * V / ((2 * k * (q + T)) * (2 * q * k * ℓ)) = q * V / (q + T) := by
  have hqT : q + T ≠ 0 := (by linarith : 0 < q + T).ne'
  have hq' : q ≠ 0 := hq.ne'
  have hk' : k ≠ 0 := hk.ne'
  have hℓ' : ℓ ≠ 0 := hℓ.ne'
  field_simp
  ring

/-! ### Proposition 11.1: independent holding times -/

/-- Law of total variance for the random sum: if `E[τ̃ | τ] = mτ` and `Var(τ̃ | τ) = vτ`, so
that `E τ̃ = m Eτ` and `E τ̃² = v Eτ + m² Eτ²`, then `Var τ̃ = m² Var τ + v Eτ`, which is (11.1). -/
theorem holding_time_variance (m v Eτ Eτ2 : ℝ) :
    (v * Eτ + m ^ 2 * Eτ2) - (m * Eτ) ^ 2 = m ^ 2 * (Eτ2 - Eτ ^ 2) + v * Eτ := by
  ring

end CoverTime.DecoratedCore
