# Summary

**Route 1 (reducing the laws to intervals): PARTIAL.** Nothing is lost by passing from unit intervals to anything obtained from them by widening, convolution and mixing (Corollary 1.2, same constant). The only laws Route 2 does not reach are uniform laws on non-interval sets. A rearrangement at a fixed level s is false: for X₁²+X₂²+X₃² at s = 0.3, a two-interval set gets 2.7014 against 2.5419 for the best unit interval, though the supremum over s is still pi and intervals attain it. At the level that matters (sup over s and linear terms), exact best-response numerics at n = 3 (14 matrices) never found a set configuration beating the best intervals. We found three mechanisms that produce non-interval optimal sets; none of them raised the supremum.

**Route 2 (unit-interval laws): PARTIAL, with one complete new case.** The new idea is that projections of a cube are log-concave, and the three-dimensional coarea inequality that RESULTS §1 shows false in general becomes true for densities with convex superlevel sets. Theorem 3.3: p_{q(Z)} ≤ 71.1·|det M₀|^{-1/3}·K^{2/3}. From it, Theorem 4.1: for X uniform on any unit cube and A of rank 3+k, ‖p_Q‖ ≤ 142.2·2.61^{k'} for all n, all signatures and all linear terms. In particular **rank three is settled for interval laws (≤ 372), including the convex side and linear terms outside the range**; for general laws only 60(n−2) is known there. The same holds for hub configurations whose remainder has bounded rank once boundedly many coordinates are removed. A hub with an interval law can be removed exactly (formula (H)). The dense-remainder hub case (star + rank one + εW) is still open and reduces to a twisted pair small-ball bound with any exponent above 1.

**The hub law.** The partial density g(x) = p_{S+2xT}(s) is the integral of the joint density of (T, S) along the lines through the single point (0, s), with x fixing the slope. g has one singular direction for each singular curve of that density through (0, s), and a spread hub set gains only by collecting several of them. We cannot prove a general reduction to intervals. Two things we can prove:
- **All hub laws are covered** under a "set-uniform" pair bound: P(|T| ≤ δ, S ∈ Γ(T)) ≤ Kδ^{1+θ} for every family of sets with |Γ(τ)| ≤ 2|τ|. This follows from weak-L^{1/(1−θ)} control of the conditional density of S given T. The rectangle version is not enough for combs.
- **The degenerate hub needs no rearrangement.** Completing the square in L gives S + 4xL = 2(L+x)² − 2x² + 2V² + D. Hence the sup over all hub laws is at most sup_β ‖p_{2(L+β)²+2V²+D}‖. For D = 0 this is ≤ pi for every law of every coordinate. With the diagonal D it becomes a bounded-density question for two equal-sign eigenvalues plus a small diagonal. Numerically (n = 40), comb hub laws only lower the density: at most 0.30, against 1.71 for an interval hub.

**Most useful next step:** prove the twisted pair small-ball bound for interval laws, P(|L| ≤ δ, |λV² + εX'ᵀWX' + ⟨γ,X'⟩ − s| ≤ δ) ≤ Kδ^{1+θ}. Through (H) it closes star + rank one + εW for interval hub laws.

The only RV-type input used anywhere is the L^p/rearrangement form; the pointwise form of Lemma 3.1 appears nowhere.

- q3tools.py, altbr3.py, mats3.py, br_test3.py
- sphere_fixed_s.py, ball_check.py, rank3_cube_check.py, hub_all_laws_check.py

---

# REPORT — Extremal laws and unit-interval laws for the bounded-density problem

## 0. Setting and results

X = (X₁,…,X_n) has independent coordinates with densities f_i ≤ 1, and Q = XᵀAX + bᵀX + c. For fixed A put D(f₁,…,f_n) = sup_{b,c}‖p_Q‖_∞ = sup_{b,c,s,ε} P(|Q−s| ≤ ε)/(2ε). The conjecture is D ≤ C when A has three eigenvalues of modulus ≥ 1. By Madiman–Melbourne–Xu (arXiv:1705.00642, Thm 1.5), extremal laws are uniform on sets of measure one.

| # | Statement | Status |
|---|---|---|
| 1.1 | D is translation invariant, convex in each f_i, non-increasing under convolution; widths r ≥ 1 are free | PROVED |
| 1.2 | Unit-interval laws ⇒ every mixture of laws U[a,a+r]∗ν (r ≥ 1), same constant; the only laws not reached are non-interval sets | PROVED |
| 2.1 | Rearrangement at a fixed level s is false (sphere, s = 0.3: 2.7014 vs 2.5419) | FALSE (exact) |
| 2.2 | At the level of sup over s and linear terms, no set beat intervals (n = 3, 14 matrices) | NUMERICAL |
| 3.3 | 3D coarea for quasi-concave densities: p_{q(Z)} ≤ 71.1·\|det M₀\|^{-1/3}K^{2/3} | PROVED |
| 4.1 | Unit cube, rank 3+k: ‖p_Q‖ ≤ 142.2·2.61^{k'}·\|λ₁λ₂λ₃\|^{-1/3} | PROVED |
| 4.2 | Unit cube, rank three: ≤ 372 (all signatures, all linear terms) | PROVED |
| 5.1 | Interval hub removed exactly; a pair bound with any θ > 0 suffices | PROVED |
| 5.3 | Hub laws: X-ray-transform description; set-uniform pair bound covers all hub laws; degenerate hub reduces to two-eigenvalue + diagonal | PROVED (reductions) |
| 5.4 | Star + rank one + εW (W dense), interval laws | OPEN, reduced to a twisted pair bound |

## 1. The extremal functional

**Proposition 1.1.** Fix A.
- (a) D(f₁(·−y₁),…,f_n(·−y_n)) = D(f₁,…,f_n).
- (b) f₁ ↦ D is convex. If f₁ = ∫f^{(θ)}dμ(θ), then D ≤ sup_θ D(f^{(θ)},f₂,…).
- (c) For every probability measure ν, D(f₁∗ν, f₂,…) ≤ D(f₁,…); note f₁∗ν ≤ 1.
- (d) If X_i = r_iX_i° with r_i ≥ 1, the matrix becomes RAR (R = diag r_i), which has at least as many eigenvalues of modulus ≥ 1 as A.

*Proof.*
- (a) Q(x+y) = xᵀAx + (b+2Ay)ᵀx + Q(y), so a translation changes only (b, c).
- (b) P(|Q−s| ≤ ε) is linear in f₁ by Fubini. So D is a supremum of linear functionals, and sup_ℓ∫ℓ(f^{(θ)})dμ ≤ ∫sup_ℓ ℓ(f^{(θ)})dμ.
- (c) f₁∗ν is a mixture of translates; apply (b) and (a).
- (d) By Ostrowski, the eigenvalues of RAR are θ_kλ_k with θ_k ∈ [min r_i², max r_i²] ⊂ [1,∞). □

Unit intervals in arbitrary positions are the same problem as i.i.d. U[−½,½] coordinates with arbitrary linear terms: X_i = c_i + U_i gives Q = UᵀAU + (2Ac+b)ᵀU + Q(c). Conditioning on coordinates keeps the remaining coordinates i.i.d. uniform, so the pivot calculus and the reduction to matrices without pivots stay inside this class.

**Corollary 1.2.** If ‖p_Q‖ ≤ C for all A in the class and all unit-interval laws, the same C holds for independent coordinates whose laws are mixtures of U[a,a+r]∗ν (r ≥ 1). *Proof:* apply (b) coordinate by coordinate, then (c), then (d). □

This class contains:
- every f(x) = G(x+½) − G(x−½) with G a distribution function;
- uniform laws of width ≥ 1;
- trapezoids with plateau length ≥ 1;
- symmetric unimodal densities that are flat on the unit interval around the mode.

It contains no uniform law on a non-interval set E. Indeed 1_E is an extreme point of the admissible densities (MMX), so every mixture component equals 1_E. A component (1/r)1_{[a,a+r]}∗ν with r > 1 is < 1 everywhere, and 1_{[a,a+1]}∗ν equals 1 only on a set of measure 1 − diam(supp ν). So ν is a point mass and E is an interval.

## 2. Rearrangement: what fails and the numerics

For linear forms the density is a Brascamp–Lieb–Luttinger integral, and rearrangement increases it. For a quadratic form, p_Q(s) = ∫f_i g_i, where g_i(t) is the density at s of a_ii t² + tL_i + R_i. The best response is the top measure-one superlevel set of g_i, and nothing forces it to be an interval.

**Example 2.1.** Q = X₁²+X₂²+X₃² with X₂, X₃ ~ U[−½,½], and W = (X₂,X₃).
- The density of |W|² at ρ² is pi for ρ ≤ ½, and pi − 4·arccos(1/(2ρ)) for ½ < ρ < 2^{−1/2}.
- At s = 0.3, g₁(t) equals pi for 0.2236 ≤ |t| ≤ 0.5477, rises from g₁(0) = 1.4595 on |t| < 0.2236, and vanishes for |t| > 0.5477.
- Every unit interval gives ≤ 2.5419. The set [−0.5477,−0.0477] ∪ [0.0477,0.5477] gives 2.7014.
- Yet the supremum over s and all laws is pi (two-coordinate definite lemma), attained by centred intervals at s = ¼.

**Flat-top mechanism (proved).** For a definite 2×2 principal block B_jk, g_i(t) ≤ pi/√det B_jk for every law. Equality holds whenever the slice ellipse lies inside the box, because a definite binary quadratic has constant density pi/√det under Lebesgue measure. So these partial densities are flat-topped and dip where the slice leaves the box. It also gives ‖p_Q‖ ≤ min over definite blocks of pi/√det B_jk for all laws.

**Numerics (n = 3).**
- *Method.* Exact partial densities by quadrature with the partition of unity (∂_u q)² + (∂_w q)² = |∇q|² (integrand capped at 1/η, which moves the value by O(η)). Validated against 2π√s and 3π − 4π√s, and against 4·10⁶-sample Monte Carlo.
- *Search.* b = 0 (for invertible A, translating the sets reproduces every linear term). Alternating exact best responses over sets, with s re-optimised. Starts: centred intervals, and random 2–4-piece sets spread over [−3, 3].
- *Values after four sweeps* (interval start / random start):

| Matrix | Interval start | Random start |
|---|---|---|
| I − 2eeᵀ | 2.57 | – |
| degenerate-block example | 2.57 | 2.55 |
| 2I − J | 1.53 | 1.49 |
| −(J − I) | 2.09 | 2.09 |
| diag(1,1,−1) | 3.15 | 3.13 |
| diag(4,1,−1) | 1.59 | 1.58 |
| diag(9,1,1) | 1.05 | 0.84 |
| six random matrices | 0.46, 1.07, 1.46, 0.64, 2.04, 0.94 | within 0.01 |

- *Exceptions.* Every run ended in intervals, or in sets whose extra pieces carry zero partial density, except two:
  - diag(9,1,1) from a random start ends in a genuine symmetric-pair local optimum ([−0.69,−0.19] ∪ [0.19,0.69]), worth 0.84 < pi/3;
  - a negative definite matrix shows holes at s = −0.39, but p ≤ pi/√det B₀₂ = 0.6475 for every law and intervals give 0.647.
- *Mechanisms seen:* a short useful window for a large diagonal (non-uniqueness), flat tops (holes at suboptimal s), and symmetric pairs (worse local optima).

## 3. Coarea inequality for quasi-concave densities

**Lemma 3.1.** Let X be uniform on the unit ball of R³ and P = xᵀMx + βᵀx + κ with det M ≠ 0. Then p_{P(X)} ≤ C_B·|det M|^{-1/3}, where C_B = (3/4π)·C_ind ≤ 9.12 and C_ind = ∫₀^∞ min(π, 8μ⁻²(6.2 + log₊16μ²))dμ ≤ 38.2.

*Proof.*
1. Rotate and complete squares: P = Σ m_k(x_k − c_k)² + κ'. Let |m₁| be the largest modulus and D = |m₂m₃| ≤ m₁².
2. Given (x₂, x₃) in the unit disc Δ, X₁ is uniform on a chord of half-length h, and (X₂, X₃) has density 3h/(2π). The density of m₁(X₁−c₁)² at y is ≤ (2h)⁻¹(|m₁||y|)^{-1/2}. The chord factor cancels:
   p_P(s) ≤ (3/4π)|m₁|^{-1/2} ∫_Δ |s − R|^{-1/2}, where R = m₂(·)² + m₃(·)² + κ'.
3. Layer cake: ∫_Δ|s−R|^{-1/2} = ∫₀^∞ |{|s−R| < λ⁻²} ∩ Δ| dλ.
4. Definite R: the annulus has area ≤ 2πu/√D, which gives 2π√2·D^{-1/4}.
5. Indefinite R: Δ ⊂ [−1,1]², and Lebesgue measure there is 4 times a product of U[−1,1] laws. The hyperbolic lemma (GEOMETRIC_ROUTE_REPORT.md, Lemma 1.4) gives area ≤ (8u/√D)(6.2 + log₊(16√D/u)). The substitution λ = D^{-1/4}μ gives C_ind·D^{-1/4}; no log D survives.
6. Hence p_P ≤ C_B|m₁|^{-1/2}D^{-1/4} = C_B|m₁m₂m₃|^{-1/3}(D/m₁²)^{1/12} ≤ C_B|det M|^{-1/3}. □

**Lemma 3.2.** For a convex body C ⊂ R³ and q with nondegenerate quadratic part M₀, the density μ_r(C) of the measure vol(C ∩ q⁻¹(·)) satisfies μ_r(C) ≤ C_K·|det M₀|^{-1/3}·vol(C)^{1/3}, with C_K = 3(4π/3)^{2/3}C_B ≤ 71.1.

*Proof.* For an ellipsoid E = c + TB, μ_r(E) = |det T|·vol(B)·p_{q(c+TX)}(r). The quadratic part of q(c+Tx) has determinant det(T)²·det M₀, so Lemma 3.1 gives the bound for E. For general C, John's theorem gives E ⊂ C ⊂ 3E, and μ_r is monotone in the set. □

**Theorem 3.3.** Let Z have density g ≤ K on R³ with convex superlevel sets (log-concave, for instance). Then for every quadratic polynomial q with nondegenerate quadratic part M₀, ‖p_{q(Z)}‖ ≤ C_K·|det M₀|^{-1/3}·K^{2/3}.

*Proof.* Write g = ∫₀^K 1_{C_t}dt with C_t convex and ∫vol(C_t)dt = 1. Then p_{q(Z)}(r) = ∫₀^K μ_r(C_t)dt ≤ C_K|det M₀|^{-1/3}∫₀^K vol(C_t)^{1/3}dt ≤ C_K|det M₀|^{-1/3}K^{2/3} by Hölder. □

*Remarks.*
- The bound is scale invariant, and the exponents are sharp (ball).
- For a thin plate tangent to the cone along a ruling, the ratio to K^{2/3} is exactly 2^{2/3}, for every thickness and length.
- Numerically (56 shapes, both signatures, off-centre), the ball-lemma quantity p·|det M|^{1/3} was at most 1.72, against the proven 9.12.
- For cubes this answers the spherical-means question of GEOMETRIC_ROUTE_REPORT.md §4: M_{y₀}(r) ≤ C/r uniformly in the centre.
- Without convexity the statement is false (thin shells).

## 4. Unit-interval laws of bounded rank

**Theorem 4.1.** Let X be uniform on ∏[a_i, a_i+1]. Let A = RΛRᵀ + R'Λ'R'ᵀ, where [R R'] has orthonormal columns, Λ = diag(λ₁,λ₂,λ₃) with |λ_k| ≥ 1, R' is n×k and Λ' is arbitrary. Write b = Rβ + R'β' + γu with u ⊥ R, R' a unit vector, and k' = k + 1_{γ≠0}. Then
‖p_Q‖ ≤ 2C_K·(√2·(2π)^{1/3})^{k'}·|λ₁λ₂λ₃|^{-1/3} ≤ 142.2·2.61^{k'}.

*Proof.* Put Y = RᵀX and Y' = (R'ᵀX, ⟨u,X⟩).
1. (Y, Y') is an orthogonal projection of the uniform measure on the cube. Its density ρ is log-concave (Prékopa–Leindler) and ρ ≤ 2^{(3+k')/2} (Livshyts–Paouris–Pivovarov, Thm 1.1).
2. Q = q(Y) + φ(Y'), where q(y) = yᵀΛy + βᵀy.
3. Given Y' = y', Y is log-concave with sup ≤ 2^{(3+k')/2}/ρ_{Y'}(y'). By Theorem 3.3, the conditional density of q(Y) is ≤ C_K|det Λ|^{-1/3}(2^{(3+k')/2}/ρ_{Y'})^{2/3}.
4. By Fubini, p_Q ≤ C_K|det Λ|^{-1/3}·2^{(3+k')/3}·∫ρ_{Y'}^{1/3}.
5. Hoeffding gives E e^{⟨θ, Y'−EY'⟩} ≤ e^{|θ|²/8}. The Gaussian trick then gives E e^{|Y'−EY'|²} ≤ 2^{k'/2}. Hölder with the weight e^{|y−m|²} gives ∫ρ^{1/3} ≤ 2^{k'/6}(2π)^{k'/3} ≤ 2.072^{k'}. □

**Corollary 4.2.** Every rank-three form (any signature, any linear term, any n) has density ≤ 372 for unit-interval laws, and for the class of Corollary 1.2.

**Corollary 4.3.** If for some coordinate set S the block A_{S^cS^c} has rank 3+k and three eigenvalues of modulus ≥ 1, then ‖p_Q‖ ≤ 142.2·2.61^{k+1}. *Proof:* condition on X_S. This covers, for example:
- hub + rank one + any remainder supported on boundedly many coordinates;
- several hubs with a nonzero hub block plus a bounded-rank part.

**Corollary 4.4 (laws of bounded variation).** Let A have rank three with eigenvalues λ₁, λ₂, λ₃ of modulus ≥ 1, and
let X₁,…,X_n be independent with densities g_i of total variation at most T. Then ‖p_Q‖ ≤ 372·(T/2)² for every n and
every linear term. Unimodal densities at most 1 have T ≤ 2, so for them ‖p_Q‖ ≤ 372, the constant of Corollary 4.2.

*Proof.*
1. By the layer-cake formula g_i = ∫₀^∞ 1{g_i > t} dt = ∫₀^∞ Σ_J |J|·(1_J/|J|) dt, the sum running over the component
   intervals J of {g_i > t}: X_i is a mixture of uniform laws on intervals J, chosen with weight |J| dt, of lengths
   ℓ_i = |J|. Then E[1/ℓ_i] = ∫₀^∞ N_i(t) dt, with N_i(t) the number of components, which is TV(g_i)/2 ≤ T/2 by the coarea
   formula.
2. Fix the intervals. Then X = a + DY with D = diag(ℓ_i) and Y uniform on the unit cube, and Q = Yᵀ(DAD)Y + (linear) +
   (constant). With A = Σ_k λ_k r_k r_kᵀ, DAD = BΛBᵀ for B = D[r₁ r₂ r₃], so its nonzero eigenvalues are those of ΛG with
   G = BᵀB = Σ_i ℓ_i² ρ_iρ_iᵀ, where ρ_i ∈ R³ is the i-th row of [r₁ r₂ r₃]. The proof of Theorem 4.1 uses |λ_k| ≥ 1 only
   in its last line, so the conditional density is ≤ 372·|det Λ·det G|^{-1/3} ≤ 372·(det G)^{-1/3} (k' ≤ 1).
3. By Cauchy–Binet, det G = Σ_{i<j<k} ℓ_i²ℓ_j²ℓ_k² d_{ijk}² with d_{ijk} = det(ρ_i, ρ_j, ρ_k), and Σ d_{ijk}² = det Σ_iρ_iρ_iᵀ = 1.
   Convexity of x^{-1/3} gives (det G)^{-1/3} ≤ Σ d_{ijk}²(ℓ_iℓ_jℓ_k)^{-2/3}.
4. The density of Q at s is the average over the intervals of the conditional density, the indices in each term are
   distinct, and E ℓ_i^{-2/3} ≤ (E ℓ_i^{-1})^{2/3} ≤ (T/2)^{2/3}. So ‖p_Q‖ ≤ 372·(T/2)². □

Corollary 1.2 needs every mixture component to have width at least 1, which forces a law with density 1 at its mode to
live in an interval of length 2 around it. Corollary 4.4 needs no lower bound on the widths, only a bound on E|I|^{-2/3}
for some representation of each law as a mixture of uniform laws on intervals I; it covers e^{-2|x|}, for instance, and
the bound is then 372·(sup_i E|I_i|^{-2/3})³. A comb with N teeth has E|I|^{-2/3} ≥ N^{2/3} in every such representation,
since its intervals lie inside teeth, so combs stay out of reach, as they do for every argument here. On eight random
rank-three forms (n = 3 to 8, eigenvalues of modulus 1 to 3, both signatures, with and without a linear term) laws with
density e^{-2|x|} give Monte Carlo densities 0.14 to 0.85, below the values 0.32 to 2.32 of unit-interval laws on the
same forms (unimodal_rank3_check.py).

*Limit of the method.* Conditioning on a non-coordinate direction costs a constant factor per direction. For a spread 3-dimensional subspace, the sections of the cube by its translates have volume of order n^{−3/2} (Shephard's formula), so full-rank matrices without pivots are out of reach of this argument alone.

## 5. Hubs

**Proposition 5.1.** Let X_h ~ U[c−½, c+½] be independent of X', L = ⟨w,X'⟩ + β, and R_c = R + 2cL. Then Q = 2X_hL + R satisfies
p_Q(s) = ½·E[|L|⁻¹·1{|s − R_c| ≤ |L|}]. (H)
If P(|L| ≤ δ, |R_c − s| ≤ δ) ≤ Kδ^{1+θ} for all s and δ ≤ 1, then ‖p_Q‖ ≤ ½ + K/(1 − 2^{−θ}).

*Proof.* Given X', Q is uniform on R_c ± |L|. Average over X', and split |L| into dyadic shells. □

- *Spread hub laws.* For a hub set made of pieces of lengths w_j, the same computation gives ½ + K(1−2^{−θ})⁻¹Σ_j w_j^θ, which grows like N^{1−θ} for N equal pieces. So the argument needs θ = 1 for arbitrary sets, but only θ > 0 for an interval.
- *Calibration.* For R = λV² + G with G independent of (L, V), the bound holds with K = 8√(2/|λ|) and θ = ½, uniformly in c.
- *Small nonzero hub diagonal a.* When |L| < |a|, the conditional density is at most (|a|·|s − R + L²/a|)^{-1/2}. This part needs θ > ½, or the change of variables of GEOM Prop. 5.4.

**Proposition 5.3 (hub laws).** Let Q = 2X_hT + S with zero hub diagonal and g(x) = p_{S+2xT}(s) = ∫ρ_{T,S}(τ, s − 2xτ)dτ. That is, g is the X-ray transform of the joint density of (T, S) along the lines through the single point (0, s).
- The supremum over hub laws equals ∫₀^∞ min(1, |{g > ℓ}|)dℓ, which is at most 2‖g‖_{L^{2,∞}}.
- *Set-uniform pair bound.* If P(|T| ≤ δ, S ∈ Γ(T)) ≤ Kδ^{1+θ} for every family of sets with |Γ(τ)| ≤ 2|τ|, then ‖p_Q‖ ≤ ½ + K/(1 − 2^{−θ}) for every hub law (take Γ(τ) = s − 2τE_h).
- *Degenerate hub.* If S = 2L² + 2V² + D and T = 2L, then S + 2xT = 2(L+x)² − 2x² + 2V² + D. Hence the supremum over all hub laws is at most sup_β‖p_{2(L+β)²+2V²+D}‖. This is ≤ pi when D = 0, for every law of every coordinate. Numerically (n = 40), spread hub laws gave at most 0.30, against 1.71 for an interval hub.

**5.4 (open).** For Q = 2X_hL + λV² + εX'ᵀWX' + (linear terms) with W dense, (H) removes the hub exactly. The case then follows from the twisted pair bound
P(|L| ≤ δ, |λV² + εX'ᵀWX' + ⟨γ,X'⟩ − s| ≤ δ) ≤ Kδ^{1+θ}.
The untwisted version holds with θ = ½. In Fourier terms, what is needed is that the twisted integral ∬|E e^{i⟨uw+zv,X'⟩ + itεX'ᵀWX'}|du dz grows at most like |t|^{1/2−θ'}. Plancherel gives only growth like |t|.

## 6. What remains

- Route 1 at the level of the supremum over s and linear terms: not proved and not refuted.
- Route 2: proved for bounded rank (after deleting boundedly many coordinates).
- Open: the full-rank no-pivot regime, in particular hubs coupled to a dense small remainder. For interval hubs it reduces to the twisted pair bound of 5.4, which is the most useful next step.
