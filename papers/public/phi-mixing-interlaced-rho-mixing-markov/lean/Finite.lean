/-
Machine-checked finite components of

  "Phi-mixing implies interlaced rho-mixing for Markov chains" (Bradley's Question 5).

Contents.
  * Section 6 (the six-state chain): the kernel of equation (6.2) is stochastic and nonnegative for
    0 < eps < 1/2, pi is invariant, K^2 = Pi (every row of K^2 equals pi), every row of K is at
    total-variation distance exactly eps from pi (so the row diameter is 2 eps and it is attained),
    the posterior-mean identity of the edge law, the second moment E B^2 = 2 eps, and the posterior
    variance identity 2 eps (1 - m^2).
  * Section 8 (the two-state chain): the posterior variance identity behind
    rho^2 = r^2 (1 - m^2) / (1 - r^2 m^2) and the bound rho^2 <= r^2.
  * Section 4 (the path matrix): the elementary norm bound behind Remark 4.3, in the form of a
    Cauchy-Schwarz estimate for the two-diagonal bilinear form and a quadratic-form bound for the
    path adjacency matrix, together with the sine eigenvector identity.
  * Lemma 2.1 (finite case): the Dobrushin oscillation contraction osc(M h) <= delta(M) osc(h),
    the consequence that a nonconstant eigenvector of a stochastic matrix has eigenvalue at most the
    row diameter, and the total-variation contraction under postprocessing (delta(KR) <= delta(K)).

Total variation of two rows is written as (1/2) sum_y |row(y) - row'(y)|, the normalisation of the
paper.  Everything is over the reals; the state spaces are Fin n.
-/
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Finset.Max
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open Finset

namespace BradleyQ5

/-! ### Section 6: the six-state chain -/
section SixState

/-- Sign coordinate `u` of the six states `(u, v)`, listed as
`(-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1)`. -/
def uu : Fin 6 → ℝ := fun i => if (i : ℕ) < 3 then -1 else 1

/-- Second coordinate `v` of the six states. -/
def vv : Fin 6 → ℝ := fun i => if (i : ℕ) % 3 = 0 then -1 else if (i : ℕ) % 3 = 1 then 0 else 1

/-- The weights `nu(v)` with `nu(-1) = nu(1) = eps`, `nu(0) = 1 - 2 eps`, listed per state. -/
noncomputable def nu (ε : ℝ) : Fin 6 → ℝ := fun i => if (i : ℕ) % 3 = 1 then 1 - 2 * ε else ε

/-- The product law `pi = mu ⊗ nu` with `mu` uniform on the sign. -/
noncomputable def piw (ε : ℝ) : Fin 6 → ℝ := fun i => nu ε i / 2

/-- The kernel of equation (6.2): `K((u,v),(u',v')) = pi(u',v') (1 + u v')`. -/
noncomputable def K (ε : ℝ) : Fin 6 → Fin 6 → ℝ := fun i j => piw ε j * (1 + uu i * vv j)

theorem piw_nonneg (ε : ℝ) (h0 : 0 ≤ ε) (h1 : ε ≤ 1 / 2) (i : Fin 6) : 0 ≤ piw ε i := by
  fin_cases i <;> simp [piw, nu] <;> linarith

theorem piw_sum (ε : ℝ) : ∑ i, piw ε i = 1 := by
  simp [Fin.sum_univ_six, piw, nu]
  ring

/-- Rows of `K` sum to one. -/
theorem K_row_sum (ε : ℝ) (i : Fin 6) : ∑ j, K ε i j = 1 := by
  fin_cases i <;> simp [Fin.sum_univ_six, K, piw, nu, uu, vv] <;> ring

/-- `K` is nonnegative when `0 <= eps <= 1/2`. -/
theorem K_nonneg (ε : ℝ) (h0 : 0 ≤ ε) (h1 : ε ≤ 1 / 2) (i j : Fin 6) : 0 ≤ K ε i j := by
  fin_cases i <;> fin_cases j <;> simp [K, piw, nu, uu, vv] <;> linarith

/-- `pi` is invariant for `K`. -/
theorem piw_invariant (ε : ℝ) (j : Fin 6) : ∑ i, piw ε i * K ε i j = piw ε j := by
  fin_cases j <;> simp [Fin.sum_univ_six, K, piw, nu, uu, vv] <;> ring

/-- `K^2 = Pi`: every row of `K^2` is `pi`. -/
theorem K_sq (ε : ℝ) (i j : Fin 6) : ∑ k, K ε i k * K ε k j = piw ε j := by
  fin_cases i <;> fin_cases j <;> simp [Fin.sum_univ_six, K, piw, nu, uu, vv] <;> ring

/-- The signed row difference from `pi` has density `u v'` with respect to `pi`. -/
theorem K_sub_piw (ε : ℝ) (i j : Fin 6) : K ε i j - piw ε j = piw ε j * (uu i * vv j) := by
  unfold K; ring

theorem uu_abs (i : Fin 6) : |uu i| = 1 := by
  fin_cases i <;> simp [uu]

theorem sum_piw_abs_vv (ε : ℝ) : ∑ j, piw ε j * |vv j| = 2 * ε := by
  simp [Fin.sum_univ_six, piw, nu, vv]
  ring

/-- Equation (6.5): `sum_j |K(x, j) - pi(j)| = 2 eps`, i.e. every row is at total-variation
distance `eps` from `pi`. -/
theorem row_tv (ε : ℝ) (h0 : 0 ≤ ε) (h1 : ε ≤ 1 / 2) (i : Fin 6) :
    ∑ j, |K ε i j - piw ε j| = 2 * ε := by
  have h : ∀ j, |K ε i j - piw ε j| = piw ε j * |vv j| := by
    intro j
    rw [K_sub_piw, abs_mul, abs_of_nonneg (piw_nonneg ε h0 h1 j), abs_mul, uu_abs, one_mul]
  simp_rw [h]
  exact sum_piw_abs_vv ε

theorem row_diff (ε : ℝ) (i i' j : Fin 6) :
    K ε i j - K ε i' j = piw ε j * ((uu i - uu i') * vv j) := by
  unfold K; ring

/-- Two rows are at total-variation distance `eps |u - u'|`:
`sum_j |K(x,j) - K(x',j)| = |u - u'| 2 eps`. -/
theorem row_pair_tv (ε : ℝ) (h0 : 0 ≤ ε) (h1 : ε ≤ 1 / 2) (i i' : Fin 6) :
    ∑ j, |K ε i j - K ε i' j| = |uu i - uu i'| * (2 * ε) := by
  have h : ∀ j, |K ε i j - K ε i' j| = |uu i - uu i'| * (piw ε j * |vv j|) := by
    intro j
    rw [row_diff, abs_mul, abs_of_nonneg (piw_nonneg ε h0 h1 j), abs_mul]
    ring
  simp_rw [h]
  rw [← Finset.mul_sum, sum_piw_abs_vv]

theorem uu_diff_le (i i' : Fin 6) : |uu i - uu i'| ≤ 2 := by
  fin_cases i <;> fin_cases i' <;> norm_num [uu]

theorem uu_diff_attained : |uu 0 - uu 3| = 2 := by
  have h0 : uu 0 = -1 := by simp [uu]
  have h3 : uu 3 = 1 := by simp [uu]
  rw [h0, h3]
  norm_num

/-- The row diameter is `2 eps`: no pair of rows is farther than `2 eps` and the pair
`(u,v) = (-1,-1), (1,-1)` attains it. -/
theorem diameter (ε : ℝ) (h0 : 0 ≤ ε) (h1 : ε ≤ 1 / 2) :
    (∀ i i', (∑ j, |K ε i j - K ε i' j|) / 2 ≤ 2 * ε) ∧
      (∑ j, |K ε 0 j - K ε 3 j|) / 2 = 2 * ε := by
  constructor
  · intro i i'
    rw [row_pair_tv ε h0 h1]
    have := uu_diff_le i i'
    nlinarith
  · rw [row_pair_tv ε h0 h1, uu_diff_attained]; ring

/-- Values of the second coordinate of an edge, `b ∈ {-1, 0, 1}`. -/
def bval : Fin 3 → ℝ := fun b => if (b : ℕ) = 0 then -1 else if (b : ℕ) = 1 then 0 else 1

/-- The two signs `a ∈ {-1, 1}`. -/
def aval : Fin 2 → ℝ := fun a => if (a : ℕ) = 0 then -1 else 1

noncomputable def nu3 (ε : ℝ) : Fin 3 → ℝ := fun b => if (b : ℕ) = 1 then 1 - 2 * ε else ε

/-- `E B^2 = 2 eps` for the edge law `q(a,b) = mu(a) nu(b) (1 + a b)`. -/
theorem edge_second_moment (ε : ℝ) : ∑ b, nu3 ε b * bval b ^ 2 = 2 * ε := by
  simp [Fin.sum_univ_three, nu3, bval]
  ring

/-- The conditional law of the sign given `B = b` is `(1 + a b)/2`, and its mean is `b`:
`E[A | B] = B`. -/
theorem edge_posterior_mean (b : Fin 3) :
    ∑ a, (1 + aval a * bval b) / 2 * aval a = bval b := by
  fin_cases b <;> simp [Fin.sum_univ_two, aval, bval] <;> ring

/-- The posterior-variance identity used to compute `kappa_E(K)`: for an input sign of mean `m`,
`Var(E[U | V']) = 2 eps (1 - m^2)`. -/
theorem six_state_posterior_variance (ε m : ℝ) :
    ε * (1 + m) * (1 - m) ^ 2 + ε * (1 - m) * (-1 - m) ^ 2 = 2 * ε * (1 - m ^ 2) := by
  ring

end SixState

/-! ### Section 8: the binary channel with parameter `r` and input mean `m` -/
section Binary

/-- `Var(E[U|V]) = r^2 (1-m^2)^2 / (1 - r^2 m^2)` for the binary symmetric channel with parameter
`r` and an input sign of mean `m`.  The left side is `E[(E[U|V])^2] - m^2` with the two posterior
means `(m + r)/(1 + m r)` and `(m - r)/(1 - m r)` weighted by `P(V = 1) = (1 + m r)/2` and
`P(V = -1) = (1 - m r)/2`. -/
theorem binary_posterior_variance (r m : ℝ) (h1 : 1 + m * r ≠ 0) (h2 : 1 - m * r ≠ 0) :
    ((m + r) / (1 + m * r)) ^ 2 * ((1 + m * r) / 2)
      + ((m - r) / (1 - m * r)) ^ 2 * ((1 - m * r) / 2) - m ^ 2
      = r ^ 2 * (1 - m ^ 2) ^ 2 / ((1 + m * r) * (1 - m * r)) := by
  have h12 : (1 + m * r) * (1 - m * r) ≠ 0 := mul_ne_zero h1 h2
  rw [eq_div_iff h12]
  field_simp
  ring

/-- The denominator identity `(1 + m r)(1 - m r) = 1 - r^2 m^2`. -/
theorem binary_denominator (r m : ℝ) : (1 + m * r) * (1 - m * r) = 1 - r ^ 2 * m ^ 2 := by
  ring

/-- Dividing by `Var(U) = 1 - m^2` gives `rho^2 = r^2 (1 - m^2) / (1 - r^2 m^2)`. -/
theorem binary_rho_sq (r m : ℝ) (hm : 1 - m ^ 2 ≠ 0) (h3 : 1 - r ^ 2 * m ^ 2 ≠ 0) :
    r ^ 2 * (1 - m ^ 2) ^ 2 / (1 - r ^ 2 * m ^ 2) / (1 - m ^ 2)
      = r ^ 2 * (1 - m ^ 2) / (1 - r ^ 2 * m ^ 2) := by
  rw [div_div, div_eq_div_iff (mul_ne_zero h3 hm) h3]
  ring

/-- `rho^2 <= r^2`, with equality at `m = 0`: the robust coefficient of the binary channel is `r`. -/
theorem binary_rho_sq_le (r m : ℝ) (hm : m ^ 2 < 1) (hr : r ^ 2 ≤ 1) :
    r ^ 2 * (1 - m ^ 2) / (1 - r ^ 2 * m ^ 2) ≤ r ^ 2 := by
  have hpos : 0 < 1 - r ^ 2 * m ^ 2 := by nlinarith [sq_nonneg r, sq_nonneg m]
  rw [div_le_iff₀ hpos]
  have hprod : 0 ≤ r ^ 2 * m ^ 2 * (1 - r ^ 2) :=
    mul_nonneg (mul_nonneg (sq_nonneg r) (sq_nonneg m)) (sub_nonneg.mpr hr)
  nlinarith

theorem binary_rho_sq_at_zero (r : ℝ) : r ^ 2 * (1 - 0 ^ 2) / (1 - r ^ 2 * 0 ^ 2) = r ^ 2 := by
  simp

end Binary

/-! ### Section 4: the path matrix -/
section Path

theorem abs_add_le' (a b : ℝ) : |a + b| ≤ |a| + |b| := by
  rw [abs_le]
  constructor
  · linarith [neg_abs_le a, neg_abs_le b]
  · linarith [le_abs_self a, le_abs_self b]

/-- Cauchy-Schwarz in the form used below. -/
theorem cs_sqrt (s : Finset ℕ) (f g : ℕ → ℝ) :
    |∑ i ∈ s, f i * g i| ≤ Real.sqrt (∑ i ∈ s, f i ^ 2) * Real.sqrt (∑ i ∈ s, g i ^ 2) := by
  rw [← Real.sqrt_mul (Finset.sum_nonneg (fun i _ => sq_nonneg (f i)))]
  exact Real.abs_le_sqrt (Finset.sum_mul_sq_le_sq_mul_sq s f g)

/-- The bilinear form of the bipartite path matrix (entries `kappa` at `(i,i)` and `(i+1,i)`, zero
elsewhere) is bounded by `2 kappa ||x|| ||y||`: this is the elementary bound `||E|| <= 2 kappa`
of Remark 4.3. -/
theorem path_bilinear_bound (κ : ℝ) (hκ : 0 ≤ κ) (N : ℕ) (x y : ℕ → ℝ) :
    |∑ i ∈ range N, κ * x i * y i + ∑ i ∈ range N, κ * x (i + 1) * y i|
      ≤ 2 * κ * Real.sqrt (∑ i ∈ range (N + 1), x i ^ 2) * Real.sqrt (∑ i ∈ range N, y i ^ 2) := by
  set X := Real.sqrt (∑ i ∈ range (N + 1), x i ^ 2) with hX
  set Y := Real.sqrt (∑ i ∈ range N, y i ^ 2) with hY
  have hA : |∑ i ∈ range N, x i * y i| ≤ X * Y := by
    calc |∑ i ∈ range N, x i * y i|
        ≤ Real.sqrt (∑ i ∈ range N, x i ^ 2) * Real.sqrt (∑ i ∈ range N, y i ^ 2) :=
          cs_sqrt (range N) x y
      _ ≤ X * Y := by
          apply mul_le_mul_of_nonneg_right _ (Real.sqrt_nonneg _)
          apply Real.sqrt_le_sqrt
          rw [Finset.sum_range_succ]
          linarith [sq_nonneg (x N)]
  have hB : |∑ i ∈ range N, x (i + 1) * y i| ≤ X * Y := by
    calc |∑ i ∈ range N, x (i + 1) * y i|
        ≤ Real.sqrt (∑ i ∈ range N, x (i + 1) ^ 2) * Real.sqrt (∑ i ∈ range N, y i ^ 2) :=
          cs_sqrt (range N) (fun i => x (i + 1)) y
      _ ≤ X * Y := by
          apply mul_le_mul_of_nonneg_right _ (Real.sqrt_nonneg _)
          apply Real.sqrt_le_sqrt
          rw [Finset.sum_range_succ']
          linarith [sq_nonneg (x 0)]
  have e1 : ∑ i ∈ range N, κ * x i * y i = κ * ∑ i ∈ range N, x i * y i := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intros; ring
  have e2 : ∑ i ∈ range N, κ * x (i + 1) * y i = κ * ∑ i ∈ range N, x (i + 1) * y i := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intros; ring
  rw [e1, e2, ← mul_add, abs_mul, abs_of_nonneg hκ]
  have hsum : |∑ i ∈ range N, x i * y i + ∑ i ∈ range N, x (i + 1) * y i| ≤ X * Y + X * Y :=
    le_trans (abs_add_le' _ _) (add_le_add hA hB)
  calc κ * |∑ i ∈ range N, x i * y i + ∑ i ∈ range N, x (i + 1) * y i|
      ≤ κ * (X * Y + X * Y) := mul_le_mul_of_nonneg_left hsum hκ
    _ = 2 * κ * X * Y := by ring

theorem path_quadratic_form_aux (N : ℕ) (z : ℕ → ℝ) :
    2 * ∑ k ∈ range N, z k * z (k + 1) ≤ ∑ k ∈ range N, z k ^ 2 + ∑ k ∈ range N, z (k + 1) ^ 2 := by
  induction N with
  | zero => simp
  | succ n ih =>
    simp only [Finset.sum_range_succ]
    nlinarith [sq_nonneg (z n - z (n + 1)), ih]

/-- The quadratic form of the path adjacency matrix on `N+1` vertices is at most twice the squared
norm: `2 sum_k z_k z_{k+1} <= 2 sum_k z_k^2`, i.e. the largest eigenvalue is at most `2`. -/
theorem path_quadratic_form (N : ℕ) (z : ℕ → ℝ) :
    2 * ∑ k ∈ range N, z k * z (k + 1) ≤ 2 * ∑ k ∈ range (N + 1), z k ^ 2 := by
  have h := path_quadratic_form_aux N z
  have h1 : ∑ k ∈ range N, z k ^ 2 ≤ ∑ k ∈ range (N + 1), z k ^ 2 := by
    rw [Finset.sum_range_succ]; linarith [sq_nonneg (z N)]
  have h2 : ∑ k ∈ range N, z (k + 1) ^ 2 ≤ ∑ k ∈ range (N + 1), z k ^ 2 := by
    rw [Finset.sum_range_succ']; linarith [sq_nonneg (z 0)]
  linarith

/-- The sine vector is an eigenvector of the path adjacency: for `theta = pi/(m+1)` and every
integer `k`, `sin((k-1)theta) + sin((k+1)theta) = 2 cos(theta) sin(k theta)`; at the ends
`sin(0) = 0` and `sin((m+1) theta) = sin(pi) = 0`, so the recursion closes on `k = 1, ..., m` with
eigenvalue `2 cos(pi/(m+1))`. -/
theorem path_sine_eigen (θ : ℝ) (k : ℤ) :
    Real.sin ((k - 1) * θ) + Real.sin ((k + 1) * θ) = 2 * Real.cos θ * Real.sin (k * θ) := by
  have h1 : ((k : ℝ) - 1) * θ = k * θ - θ := by ring
  have h2 : ((k : ℝ) + 1) * θ = k * θ + θ := by ring
  rw [h1, h2, Real.sin_sub, Real.sin_add]
  ring

theorem path_sine_boundary (m : ℕ) : Real.sin (((m : ℝ) + 1) * (Real.pi / ((m : ℝ) + 1))) = 0 := by
  have hm : ((m : ℝ) + 1) ≠ 0 := by positivity
  rw [mul_div_cancel₀ _ hm]
  exact Real.sin_pi

end Path

/-! ### Lemma 2.1, finite case: oscillation contraction and the eigenvalue bound -/
section Dobrushin

variable {ι : Type*} [Fintype ι]

/-- Dobrushin's oscillation contraction for one pair of rows: if `a <= h <= b` then
`(M h)(x) - (M h)(x') <= (sum_y |M x y - M x' y|) (b - a)/2`. -/
theorem dobrushin_osc (M : ι → ι → ℝ) (x x' : ι)
    (hrow : ∑ y, M x y = 1) (hrow' : ∑ y, M x' y = 1)
    (h : ι → ℝ) (a b : ℝ) (ha : ∀ y, a ≤ h y) (hb : ∀ y, h y ≤ b) :
    ∑ y, M x y * h y - ∑ y, M x' y * h y ≤ (∑ y, |M x y - M x' y|) * ((b - a) / 2) := by
  have expand : ∀ y, (M x y - M x' y) * (h y - (a + b) / 2)
      = M x y * h y - M x' y * h y - (a + b) / 2 * M x y + (a + b) / 2 * M x' y := by
    intro y; ring
  have hsum : ∑ y, M x y * h y - ∑ y, M x' y * h y
      = ∑ y, (M x y - M x' y) * (h y - (a + b) / 2) := by
    simp_rw [expand]
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_sub_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, hrow, hrow']
    ring
  rw [hsum]
  calc ∑ y, (M x y - M x' y) * (h y - (a + b) / 2)
      ≤ ∑ y, |M x y - M x' y| * ((b - a) / 2) := by
        apply Finset.sum_le_sum
        intro y _
        calc (M x y - M x' y) * (h y - (a + b) / 2)
            ≤ |(M x y - M x' y) * (h y - (a + b) / 2)| := le_abs_self _
          _ = |M x y - M x' y| * |h y - (a + b) / 2| := abs_mul _ _
          _ ≤ |M x y - M x' y| * ((b - a) / 2) := by
              apply mul_le_mul_of_nonneg_left _ (abs_nonneg _)
              rw [abs_le]
              constructor <;> linarith [ha y, hb y]
    _ = (∑ y, |M x y - M x' y|) * ((b - a) / 2) := by rw [Finset.sum_mul]

/-- A nonconstant eigenvector of a stochastic matrix has eigenvalue at most the row diameter
`delta(M) = max_{x,x'} (1/2) sum_y |M x y - M x' y|`.  This is the eigenvector step in the finite
proof of Lemma 2.1: applied to `M = K R` and the top centered eigenvalue `theta = rho^2`, it gives
`rho^2 <= delta(M)`. -/
theorem eigen_le_diameter [Nonempty ι] (M : ι → ι → ℝ) (δ θ : ℝ)
    (hrow : ∀ x, ∑ y, M x y = 1) (hδ : ∀ x x', (∑ y, |M x y - M x' y|) / 2 ≤ δ)
    (h : ι → ℝ) (heig : ∀ x, ∑ y, M x y * h y = θ * h x) (hnc : ∃ x x', h x ≠ h x') :
    θ ≤ δ := by
  obtain ⟨xmax, _, hmax⟩ := Finset.exists_max_image Finset.univ h Finset.univ_nonempty
  obtain ⟨xmin, _, hmin⟩ := Finset.exists_min_image Finset.univ h Finset.univ_nonempty
  have hpos : 0 < h xmax - h xmin := by
    obtain ⟨x, x', hne⟩ := hnc
    have h1 := hmax x (Finset.mem_univ _)
    have h2 := hmin x (Finset.mem_univ _)
    have h3 := hmax x' (Finset.mem_univ _)
    have h4 := hmin x' (Finset.mem_univ _)
    rcases lt_or_gt_of_ne hne with hlt | hgt <;> linarith
  have hosc := dobrushin_osc M xmax xmin (hrow _) (hrow _) h (h xmin) (h xmax)
    (fun y => hmin y (Finset.mem_univ _)) (fun y => hmax y (Finset.mem_univ _))
  rw [heig xmax, heig xmin] at hosc
  have hδ' := mul_le_mul_of_nonneg_right (hδ xmax xmin) hpos.le
  have hθ : θ * (h xmax - h xmin) ≤ δ * (h xmax - h xmin) := by nlinarith
  exact le_of_mul_le_mul_right hθ hpos

/-- Postprocessing by a stochastic kernel contracts total variation: for a stochastic `R`,
`sum_z |sum_y (alpha_y - beta_y) R y z| <= sum_y |alpha_y - beta_y|`.  Applied to the rows of `K`
this is `delta(K R) <= delta(K)`. -/
theorem tv_contract {κ : Type*} [Fintype κ] (R : ι → κ → ℝ) (hR : ∀ y z, 0 ≤ R y z)
    (hrow : ∀ y, ∑ z, R y z = 1) (α β : ι → ℝ) :
    ∑ z, |∑ y, (α y - β y) * R y z| ≤ ∑ y, |α y - β y| := by
  calc ∑ z, |∑ y, (α y - β y) * R y z| ≤ ∑ z, ∑ y, |α y - β y| * R y z := by
        apply Finset.sum_le_sum
        intro z _
        calc |∑ y, (α y - β y) * R y z| ≤ ∑ y, |(α y - β y) * R y z| :=
              Finset.abs_sum_le_sum_abs _ _
          _ = ∑ y, |α y - β y| * R y z := by
              apply Finset.sum_congr rfl
              intro y _
              rw [abs_mul, abs_of_nonneg (hR y z)]
    _ = ∑ y, |α y - β y| * ∑ z, R y z := by
        rw [Finset.sum_comm]
        apply Finset.sum_congr rfl
        intro y _
        rw [Finset.mul_sum]
    _ = ∑ y, |α y - β y| := by
        apply Finset.sum_congr rfl
        intro y _
        rw [hrow y, mul_one]

end Dobrushin

end BradleyQ5

#print axioms BradleyQ5.K_row_sum
#print axioms BradleyQ5.K_nonneg
#print axioms BradleyQ5.piw_invariant
#print axioms BradleyQ5.K_sq
#print axioms BradleyQ5.row_tv
#print axioms BradleyQ5.diameter
#print axioms BradleyQ5.edge_second_moment
#print axioms BradleyQ5.edge_posterior_mean
#print axioms BradleyQ5.six_state_posterior_variance
#print axioms BradleyQ5.binary_posterior_variance
#print axioms BradleyQ5.binary_denominator
#print axioms BradleyQ5.binary_rho_sq
#print axioms BradleyQ5.binary_rho_sq_le
#print axioms BradleyQ5.path_bilinear_bound
#print axioms BradleyQ5.path_quadratic_form
#print axioms BradleyQ5.path_sine_eigen
#print axioms BradleyQ5.path_sine_boundary
#print axioms BradleyQ5.dobrushin_osc
#print axioms BradleyQ5.eigen_le_diameter
#print axioms BradleyQ5.tv_contract
