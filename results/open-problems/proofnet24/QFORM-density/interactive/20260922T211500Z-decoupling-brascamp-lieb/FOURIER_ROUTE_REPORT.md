# Bounded density of quadratic forms: the Fourier route (agent A report)

Conventions. X_1, ..., X_n independent (identical distribution is never used), each with a density
<= 1; Q(x) = x^T A x + b^T x + c with arbitrary b, c; phi(t) = E e^{itQ(X)}; psi_i, f_i the ch.f. and
density of X_i; "leverage" of coordinate i in a frame R (orthonormal columns) is |r(i)|^2, r(i) the i-th row.
PROVED means a complete proof is written here (or the step is a cited theorem whose statement I checked);
HEURISTIC and NUMERICAL are marked as such.

## 0. Summary

**Audit of the lead's Theorem D (Section 1): correct**, including the constant 6 sqrt(e) Z^{-1/6}. The
determinant step must be written through the "diagonal + PSD" expansion when some β_j = 1 (the route through
det D · det(I + N^T N) needs every e_j > 0); the conclusion is unchanged. Marginal formula and the Gaussian
determinant bound confirmed numerically to machine precision. Heavy coordinates belong on the J side.

**Extensions of Theorem D (PROVED):**
* D' (Jensen): the I-marginal threshold 1/2 can be any h < 3/4, constant 6 sqrt(e)(2h)^{-1/2}(3-4h)^{-1}.
* D_5: a decoupled block with 5-volume Z_5 gives ||p_Q||_∞ <= 5 sqrt(2e) Z_5^{-1/10} ≈ 11.66 Z_5^{-1/10}
  with **no marginal condition at all** (general D_k formula in 1.2).

**Task 1 (Section 2): S1-S3 verified.** Decoupling and the L^p lemma (int|psi|^p <= 4π/sqrt p, p >= 2) are
right as stated. S3 gives ||p_Q||_∞ <= 6 κ^{1/3} (σ_1σ_2σ_3)^{-1/3} for an exact rank-3 block A_IJ
(κ^{1/3} = sqrt 2, or 1 when |J| = 3), under leverage <= 1/2 *within I*; LPP (Israel J. Math. 2016, Thm 1.1,
checked) gives the density 2^{3/2} det(G_J)^{-1/2} of c = R_J^T W without orthonormality.

**New tools for the complement of Theorem D (Section 3-4, PROVED):**
* **Theorem F (Fresnel-Brascamp-Lieb):** for A = (any diagonal) + R Λ R^T with rank-r part of coordinate
  weights <= 1/2, |phi(t)| <= (4π)^{r/2} |t|^{-r/2} prod|λ_k|^{-1/2}. No decoupling, so no squaring and no
  partition; diagonal and linear terms are harmless (they are twists, and twisted ch.f.s obey the same L^p
  bounds). **Every rank-3 form in which each coordinate has leverage sum_k r_k(i)^2 <= 1/2 in the
  eigenspace has density <= 12 |λ_1λ_2λ_3|^{-1/3} <= 12** (Gaussian benchmark 4.24; empirical worst in 27
  edge cases 3.77).
* **Theorem MF (mixed Fresnel):** coordinates of leverage up to 1 that couple linearly to spread
  directions are integrated against their densities and each gains a full |t|^{-1}; e.g.
  2X_1<g,X> + <r_2,X>^2 (outside Theorem D: every 3-volume vanishes) has density <= 7.57.
* **Proposition H:** three independent blocks, Hölder in t with uniform L^3 bounds (table in 3.3);
  2(X_1X_2 + X_3X_4 + X_5X_6) <= 3.
* **Peels (Section 4):** square peel D(Q) <= |a|^{-1/2} H_{1/2}(Schur complement); coordinate-hyperbola peel
  D(Q) <= 2^{3/4}κ|μ|^{-3/4} H_{1/4}(...); fractional potentials H_α controlled by int|t|^{α-1}|phi|.
  Consequences: diagonal + spread rank 2 with the third eigenvalue on a coupled coordinate
  (8 sqrt 2 |a|^{-1/2}|λ_1λ_2|^{-1/4}); the n = 3 zero-diagonal core 2(X_1X_2 + X_2X_3 + X_1X_3) (<= 4.55);
  A = I - 2rr^T on R^3 (bounded, by two peels).

**Task 2 (Section 5):** with Theorem F the leverage condition is removed down to a clean dichotomy
(Prop. 5.1, PROVED): for δ ≤ 1/2, either ||p_Q||_∞ <= 12 |λ_1λ_2λ_3|^{-1/3}/(2δ), or a unit vector of the
eigenspace carries >= 1 - 2δ of its mass on fewer than 3/δ coordinates. The fully localized alternative
reduces the rank-3 (+ diagonal) conjecture to the bounded-dimensional problem BD(m); hybrid alternatives
are covered in the sub-cases listed in 5.2, not in general.

**Task 3 (Section 6.1):** the "three singular directions" lemma holds in Theorem D's volume-sampling
form (extra directions only increase Z); my projection-based version needed exact rank and fails under
small dense noise, which Theorem D absorbs.

**Task 4, what remains (6.3):** R1 the glue (a structural theorem sending every A into a proved class
with universal parameters; perturbations of *localized* low-rank structure are not handled);
R2 BD(m) in general, reduced here to a density bound for products of two general linear forms of a
2-dimensional product density (proved in the coordinate case, Lemma 4.3, and in the non-degenerate pivot
case); R3 phase-sensitive estimates for few-coordinate forms such as I - 2rr^T, where every
absolute-value Fourier bound here stalls at |t|^{-1}. **The conjecture itself is not proved.**

Numerics (Section 7): six scripts, no bound violated, no unbounded-looking density.

## 1. Audit of the lead's Theorem D (volume-sampling Brascamp-Lieb)

**Verdict: correct as stated, constants included.** One step (the determinant bound) needs a
different formulation when some β_j = 1, and one remark about where heavy coordinates belong.
Numerical checks are in Section 7 (N2).

Notation. After conditioning on X_K (free, see 2.1), Q is a quadratic polynomial in X_I, X_J
(I, J disjoint). M = A_IJ, rows a_i (i in I). psi_i = ch.f. of X_i, h_i(s) = |psi_i(2ts)|,
g_j = density of W_j = X_j - X_j' (g_j <= 1, int g_j = 1, W has independent coordinates).
Decoupling (2.2) gives |phi(t)|^2 <= E_W prod_i h_i((MW)_i) = int_{R^J} prod_i h_i(<a_i,w>) prod_j g_j(w_j) dw.

Line-by-line.

(a) **BL form and scaling.** Write h_i = (h_i^{1/α_i})^{α_i}, g_j = (g_j^{1/(1-β_j)})^{1-β_j}.
Since sum_i α_i = E|S| = 3 and sum_j β_j = E|T| = 3, the exponents satisfy
sum_i α_i + sum_j (1-β_j) = |J| = dim R^J, which is the scaling condition. Rows with α_i = 0 never
occur in a non-zero minor; drop them (h_i <= 1). Columns with β_j = 1: drop g_j using g_j <= 1.
Rows kept have a_i != 0 (a zero row kills every minor), so every map is surjective (Lieb needs this).

(b) **Lieb normalisation.** For data (B_k, c_k) with 1-dimensional targets,
BL = sup_{λ_k>0} ( prod λ_k^{c_k} / det(sum_k c_k λ_k B_k^T B_k) )^{1/2}; checked on the trivial
cases (identity: 1; B = 2: 1/2; geometric data: 1). With d_i = α_i p_i, e_j = (1-β_j) q_j the
ratio becomes prod(d_i/α_i)^{α_i} prod(e_j/(1-β_j))^{1-β_j} / det(D + M^T D_I M). Correct.

(c) **Determinant bound.** The lead's route det(D) det(I + N^T N), N = D_I^{1/2} M D^{-1/2}, needs
every e_j > 0, i.e. no β_j = 1. The version that always works is the expansion of a determinant of
"diagonal + PSD" together with Cauchy-Binet:

  det(D + M^T D_I M) = sum_{T ⊂ J} prod_{j ∉ T} e_j · det((M^T D_I M)_{TT})
                     = sum_T sum_{|S|=|T|} det(M_ST)^2 prod_{i∈S} d_i prod_{j∉T} e_j
                     >= sum_{|S|=|T|=3} det(M_ST)^2 prod_S d_i prod_{j∉T} e_j.

Weighted AM-GM with w_ST = det(M_ST)^2 / Z gives >= Z prod d_i^{α_i} prod_j e_j^{1-β_j}; an index j
with β_j = 1 lies in every T of positive weight, so e_j never appears (consistent with dropping g_j).
All Gaussian parameters cancel: BL <= Z^{-1/2} prod α_i^{-α_i/2} prod (1-β_j)^{-(1-β_j)/2}. Correct.
(Tested: over 60 000 random Gaussian parameter sets on 30 random matrices, the ratio never exceeded 1/Z.)

(d) **L^p lemma.** ||h_i||_{1/α_i} = ((2|t|)^{-1} int|psi_i|^{1/α_i})^{α_i} <= (4π sqrt(α_i)/(2|t|))^{α_i}
needs 1/α_i >= 2, i.e. α_i <= 1/2. The bound int|psi|^p <= 4π/sqrt(p) (real p >= 2) is proved in 2.3.
The factors α_i^{α_i/2} cancel exactly; sum α_i = 3 gives (4π)^3 (2|t|)^{-3}.

(e) **The e^{3/2}.** -x log x <= 1 - x on [0,1], so prod(1-β_j)^{-(1-β_j)/2} <= exp(sum β_j / 2) = e^{3/2}.

(f) **Assembly.** |phi|^2 <= e^{3/2} (2π)^3 |t|^{-3} Z^{-1/2}; with |phi| <= 1,
int min(1, B|t|^{-3/2}) dt = 6 B^{2/3}, B = (2π)^{3/2} e^{3/4} Z^{-1/4}, so
||p_Q||_∞ <= (3/π) B^{2/3} = 6 sqrt(e) Z^{-1/6}. Correct.

(g) **Marginal formula** α_i = sum_m p_m u_m(i)^2, p_m = s_m^2 e_2(s^2_{-m}) / e_3(s^2): confirmed by
brute-force enumeration of all 3x3 minors on 30 random matrices (max error 1.5e-14), together with
Z = e_3(s^2) and sum α = sum β = 3. For exact rank 3, p_m = 1 and α_i is the leverage score, so
Theorem D contains the sketch S3 (constant 6 sqrt(e) ≈ 9.89 against 6 sqrt(2) ≈ 8.49 from the
projection route of Section 2; the projection route needs exact rank 3, Theorem D does not).

(h) **KL version** (any weight w with row marginals <= 1/2, extra factor exp(KL(w||w_vol)/2)): correct,
same AM-GM with x_ST/w_ST.

(i) **Where the heavy coordinates go.** Only the I-side marginals are constrained; the J side enters
only through Z and the harmless e^{3/2}. Coordinates of large leverage should therefore always be put
in J. The obstruction is only that I must "see" all three directions through rows of small marginal.

### 1.1 Extension D' (Jensen): the marginal threshold 1/2 can be raised to any h < 3/4

Since h_i <= 1, E_W F <= (E_W F^q)^{1/q} for q >= 1 (F = prod h_i). Apply the same BL argument to
F^q = prod |psi_i(2t .)|^q: the L^p lemma now needs q/α_i >= 2. One gets

  E_W F^q <= e^{3/2} (2π)^3 q^{-3/2} |t|^{-3} Z^{-1/2},   |phi(t)|^2 <= [e^{3/2}(2π)^3 q^{-3/2} Z^{-1/2}]^{1/q} |t|^{-3/q}.

For max_i α_i <= h with 1/2 <= h < 3/4 take q = 2h (then 3/(2q) > 1):

  **||p_Q||_∞ <= 6 sqrt(e) (2h)^{-1/2} (3 - 4h)^{-1} Z^{-1/6}.**

### 1.2 Extension D_k: higher volumes; for k >= 5 there is no marginal condition at all

Run the same argument with k x k minors, Z_k = e_k(M^T M), marginals α_i^{(k)} (sum = k):
E_W F^q <= e^{k/2} (2π/|t|)^k q^{-k/2} Z_k^{-1/2} whenever max α_i^{(k)} <= q/2, hence
|phi| <= B |t|^{-k/(2q)} and, for a = k/(2q) > 1,

  ||p_Q||_∞ <= 2 sqrt(e) · a/(a-1) · q^{-1/2} · Z_k^{-1/(2k)}.

Marginals never exceed 1, so q = 2 is always admissible; for k = 5:
**||p_Q||_∞ <= 5 sqrt(2e) Z_5^{-1/10} ≈ 11.66 Z_5^{-1/10}, for any disjoint I, J, no condition.**
(k = 4 needs max α^{(4)} < 1; k = 3 needs max α^{(3)} < 3/4.) Consequently a matrix that escapes
Theorem D and its extensions has, for every disjoint I, J, small 5-volume in A_IJ and 3-volume that
is either small or carried by rows of marginal >= 3/4.

## 2. Task 1: the sketch S1-S3, verified with explicit constants

### 2.1 (S1) Inversion and conditioning — PROVED
If phi ∈ L^1 then Q(X) has a continuous density with ||p_Q||_∞ <= (1/2π) ||phi||_1. For any set K,
P(Q ∈ B) = E[P(Q(x_K, X_L) ∈ B)|_{x_K = X_K}], so ||p_Q||_∞ <= sup_{x_K} ||p_{Q(x_K, X_L)}||_∞.
Given X_K = x_K, Q is x_L^T A_LL x_L + b(x_K)^T x_L + c(x_K): the quadratic part is the principal
block, linear and constant terms appear. Every bound below is uniform in b and c.

### 2.2 (S2) Decoupling — PROVED as stated
For disjoint I, J ⊂ L (rest conditioned): |phi(t)| <= E_{X_I} |E_{X_J} e^{itQ}|, Cauchy-Schwarz,
expand the square with an independent copy X_J', integrate X_I first:
|phi(t)|^2 <= E_{X_J, X_J'} | prod_{i∈I} psi_i(2t (A_IJ W)_i) |, W = X_J - X_J'.
A_II, A_JJ, b and c drop out. W_j = X_j - X_j' are independent with densities
g_j(w) = int f_j(w+x) f_j(x) dx <= sup f_j <= 1. Nothing to correct.

### 2.3 The L^p lemma — PROVED, constant as claimed
Let psi be the ch.f. of a density f <= 1. For p = 2m (m >= 1): |psi|^{2m} is the ch.f. of a sum of 2m
independent variables with densities f and f(-.), integrable (it is <= |psi|^2 ∈ L^1), so
int |psi|^{2m} = 2π · (density of that sum at 0) <= 2π · sup of the density of U_1 + ... + U_{2m}
(Rogozin 1987; U_k uniform on [-1/2,1/2]) = 2π int (sin πx/πx)^{2m} dx <= 2π (2/(2m))^{1/2}
(Ball's integral inequality). So **int|psi|^{2m} <= 2 sqrt(2) π / sqrt(2m)**; for p = 2 exactly
int|psi|^2 = 2π int f^2 <= 2π. For real p ∈ [2m, 2m+2], log-convexity of p -> int|psi|^p and
p/(2m) <= 2 give **int|psi|^p <= 4π / sqrt(p) for every real p >= 2**. (Numerically, N1: for the
uniform law and three lattice-like laws the sharper 2 sqrt(2) π / sqrt(p) holds at every p tested,
including non-even p; I only claim 4π/sqrt(p) for non-even p.)

The same proof gives the bound for **twisted** transforms g(s, τ) = E e^{i s X^2 + i τ X} in the
variable τ, uniformly in s: g(s, .) is the Fourier transform of h = e^{isx^2} f with |h| = f, and
|(h * h~)^{*m}(0)| <= (f * f~)^{*m}(0). Hence **int |g(s,τ)|^p dτ <= 4π/sqrt(p) for all s, p >= 2.**
This is the lemma behind Section 3.

### 2.4 Projection densities — citation checked
Livshyts-Paouris-Pivovarov, "On sharp bounds for marginal densities of product measures",
Israel J. Math. 216 (2016) 877-889, Theorem 1.1 (read in the arXiv source): if f = prod f_i with
||f_i||_∞ <= 1, the marginal of f on any k-dimensional subspace E ⊂ R^n (k < n) has density at most
min((n/(n-k))^{(n-k)/2}, 2^{k/2}). Rudelson-Vershynin (IMRN 2015, Thm 1.1) is the (CK)^k version with an
unspecified absolute C; LPP is the citable sharp form. For k = n the product density itself is <= 1.

### 2.5 (S3) the rank-3 decoupled block — PROVED, with three corrections
**Proposition 2.5.** Let I, J be disjoint and suppose A_IJ has rank exactly 3 with non-zero singular
values σ_1 >= σ_2 >= σ_3, and let U_0 (|I| x 3, orthonormal columns) span its column space. If every
row u_i of U_0 has |u_i|^2 <= 1/2, then

  |phi(t)|^2 <= 8 π^3 κ_J / (σ_1 σ_2 σ_3 |t|^3)   and   ||p_Q||_∞ <= 6 κ_J^{1/3} (σ_1 σ_2 σ_3)^{-1/3},

κ_J = 1 if |J| = 3 and κ_J = 2^{3/2} if |J| >= 4.

Proof. A_IJ = U_0 N S P V_0^T with V_0 orthonormal (|J| x 3) and N S P invertible; c = V_0^T W has
density <= 2^{3/2} (LPP; <= 1 if |J| = 3). E_W F(A_IJ W) <= ||ρ_c||_∞ int_{R^3} F(U_0 N S P c) dc;
substitute z = 2t N S P c (dc = dz / (8|t|^3 σ_1σ_2σ_3)); the rows u_i satisfy sum u_i u_i^T = I_3,
so geometric BL with c_i = |u_i|^2, f_i(s) = |psi_i(|u_i| s)|^{1/|u_i|^2} gives
int prod_i |psi_i(<u_i,z>)| dz <= prod (|u_i|^{-1} · 4π|u_i|)^{|u_i|^2} = (4π)^3. Integrate
min(1, B|t|^{-3/2}) (= 6B^{2/3}) and divide by 2π. ∎

Corrections to the sketch: (i) the conditions and the constant depend only on the column space and
the singular values of A_IJ; for A = RΛR^T this is |λ_1λ_2λ_3| det(G_I)^{1/2} det(G_J)^{1/2} with
G_I = R_I^T R_I, and the leverage condition is on the rows of R_I G_I^{-1/2} (leverage within I, not
in the full frame); (ii) the density of c needs no orthonormality of R_J: LPP gives
2^{3/2} det(G_J)^{-1/2} for any R_J of rank 3; (iii) the small-|t| region is handled by |phi| <= 1 and
the optimal cut T = B^{2/3}; the claimed exponent |t|^{-3} for |phi|^2 is right.
For a balanced random split of a spread rank-3 frame (G_I ≈ G_J ≈ I/2) this gives
||p_Q||_∞ <= 12 sqrt(2) |λ_1λ_2λ_3|^{-1/3} ≈ 17.0 |λ_1λ_2λ_3|^{-1/3}. Section 3 improves this to 12
without any partition.

Proposition 2.5 applies verbatim to A = RΛR^T + (any diagonal), since decoupling only sees
off-diagonal blocks. It is subsumed, up to the constant, by Theorem D (Section 1), which also
covers blocks of any rank. With Jensen (1.1) the threshold 1/2 becomes any h < 3/4.

## 3. New Fourier tools for the complement of Theorem D (PROVED)

The lead asked for "Fresnel on the rank-2 part with the diagonal as a product twist". Carried out,
the Fresnel linearisation gives more than that: it needs **no decoupling at all**, so it does not
square |phi|, keeps diagonal and linear terms, and works for any rank. Everything rests on the
twisted L^p lemma of 2.3: for g(s,τ) = E e^{isX^2 + iτX}, int |g(s,τ)|^p dτ <= 4π/sqrt(p) (p >= 2),
uniformly in s.

### 3.1 Theorem F (Fresnel-Brascamp-Lieb)
Let A = D + sum_{k=1}^r λ_k r_k r_k^T, D diagonal (arbitrary), r_k orthonormal, R = [r_1..r_r] with
rows r(i) ∈ R^r, and Q(x) = x^T A x + b^T x + c (b, c arbitrary). If max_i |r(i)|^2 <= 1/2, then

  |phi(t)| <= (4π)^{r/2} |t|^{-r/2} prod_k |λ_k|^{-1/2},   and for r >= 3
  **||p_Q||_∞ <= (4r/(r-2)) (prod_k |λ_k|)^{-1/r};   r = 3:  ||p_Q||_∞ <= 12 |λ_1 λ_2 λ_3|^{-1/3}.**

Proof. (1) Regularised Fresnel: for a ≠ 0, ε > 0,
int e^{(ia-ε)ξ^2 + iξy} dξ = (π/(ε-ia))^{1/2} e^{-y^2/(4(ε-ia))}; so h_ε(y) := e^{-y^2/(4(ε-ia))} has
|h_ε| <= 1 and h_ε(y) -> e^{-iy^2/(4a)}. With a_k = -1/(4tλ_k) the limit is e^{itλ_k y^2}.
(2) By dominated convergence phi(t) = lim_ε E[e^{it(sum d_i X_i^2 + b^T X + c)} prod_k h_{k,ε}(<r_k,X>)].
(3) For ε > 0 the ξ-integrals converge absolutely, Fubini applies, and independence gives
E[...] = e^{itc} prod_k ((ε-ia_k)/π)^{1/2} int_{R^r} prod_k e^{(ia_k-ε)ξ_k^2} prod_i g_i(t d_i, t b_i + <r(i), ξ>) dξ.
(4) Take moduli. The rows satisfy sum_i r(i) r(i)^T = I_r, so geometric BL with c_i = |r(i)|^2 and
f_i(σ) = |g_i(t d_i, t b_i + |r(i)|σ)|^{1/c_i} applies; int f_i = |r(i)|^{-1} int |g_i(t d_i, τ)|^{1/c_i} dτ
<= 4π by the twisted lemma (1/c_i >= 2; translation in τ is harmless). Hence the ξ-integral is <= (4π)^r.
(5) Let ε -> 0: |phi(t)| <= prod_k (|a_k|/π)^{1/2} (4π)^r = prod_k (4π|tλ_k|)^{-1/2} (4π)^r.
The density bound is (1/π) (a/(a-1)) B^{1/a} with a = r/2, B = (4π)^{r/2} prod|λ_k|^{-1/2}. ∎

Consequences.
* **Rank-3 forms, spread case: C = 12.** If rank A = 3 and every coordinate has leverage <= 1/2
  (needs n >= 6), then ||p_Q||_∞ <= 12 |λ_1λ_2λ_3|^{-1/3} <= 12, for every n, every law, every b, c.
  No partition is needed (compare 12 sqrt 2 from S3). Gaussian-limit benchmark: 3 sqrt 2 ≈ 4.24.
* The same for "diagonal + spread rank 3" with an arbitrary diagonal, which decoupling cannot see.
* **Per-direction decay, made rigorous.** r = 1: |E e^{itλ<u,X>^2 + diagonal + linear}| <= (4π/|tλ|)^{1/2}
  whenever max u_i^2 <= 1/2. For u = (e_1+e_2)/sqrt 2 Cauchy-Schwarz gives the sharper
  |E e^{is(X_1+X_2)^2}| <= (π/|s|)^{1/2}. This is consistent with (F2): the bound is false for a single
  coordinate and true as soon as the direction is split over coordinates of weight <= 1/2.
* **Heavy coordinates conditioned.** For any K (L = complement) with G_L = R_L^T R_L invertible,
  condition on X_K and apply Theorem F to A_LL = R_L Λ R_L^T (frame R_L G_L^{-1/2}, middle matrix
  G_L^{1/2} Λ G_L^{1/2} with |det| = |λ_1λ_2λ_3| det G_L): if max_{i∈L} r(i)^T G_L^{-1} r(i) <= 1/2 then
  ||p_Q||_∞ <= 12 |λ_1λ_2λ_3|^{-1/3} det(G_L)^{-1/3}. At most 5 coordinates have leverage > 1/2.

### 3.2 Theorem MF (mixed Fresnel: heavy coordinates integrated against their densities)
Let H ⊂ [n], L = complement, and write A_LL = D_L + S Λ S^T (D_L diagonal, S ∈ R^{L x r} orthonormal
columns, r >= 0). Put C = A_LH, w_l = (C_{l,.}, s(l)) ∈ R^{|H|+r} and Γ = sum_l w_l w_l^T =
[[C^T C, C^T S], [S^T C, I_r]]. If Γ is invertible and max_l w_l^T Γ^{-1} w_l <= 1/2 then, with no
condition on A_HH, D_L, b, c,

  |phi(t)| <= (4π)^{|H| + r/2} 2^{-|H|} |t|^{-(|H| + r/2)} prod_k |λ_k|^{-1/2} det(Γ)^{-1/2}.

Proof. Condition on nothing: phi = E_{X_H}[e^{it(...X_H only...)} E_{X_L}[...]]. For fixed x_H the inner
expectation is the situation of Theorem F on L with linear coefficients t b_l + 2t (C x_H)_l; steps
(1)-(3) bound it by prod_k (4π|tλ_k|)^{-1/2} int_{R^r} prod_l |g_l(t d_l, t b_l + 2t(Cx_H)_l + <s(l),ξ>)| dξ.
Integrate over x_H against prod f_h <= 1, substitute y = 2t x_H (factor (2|t|)^{-|H|}), and apply BL to
the rows w_l after the change of variables z = Γ^{-1/2} y' (geometric rows Γ^{-1/2} w_l, factor
det Γ^{-1/2}, leverages w_l^T Γ^{-1} w_l <= 1/2, twisted lemma). ∎

This is decoupling without squaring: each heavy coordinate coupled through a well-conditioned column
gains a full |t|^{-1} (decoupling gains |t|^{-1/2} per rank). Theorem F is the case H = ∅.
Examples: Q = 2 X_1 <g, X_L> + <r_2, X_L>^2 (g ⟂ r_2 unit, spread): H = {1}, r = 1, Γ = I_2,
|phi| <= (4π)^{3/2}/(2|t|^{3/2}), **||p_Q||_∞ <= 7.57**. This form has a leverage-1 coordinate and
e_3(A_IJ^T A_IJ) = 0 for every disjoint I, J (so it is outside Theorem D). Two heavy coordinates coupled to
orthonormal spread g_1, g_2 (four eigenvalues ±1): |phi| <= 4π^2/t^2, ||p_Q||_∞ <= 4.

### 3.3 Proposition H (independent blocks, Hölder in t)
If Q = sum_k Q_k(X_{B_k}) over disjoint coordinate blocks then phi = prod phi_k and
||p_Q||_∞ <= (1/2π) ||phi_1||_3 ||phi_2||_3 ||phi_3||_3 for any three of the blocks. Uniform L^3 bounds:

| block Q_k (plus any linear term) | bound used | ||phi_k||_3^3 <= |
|---|---|---|
| λ X^2 | Hausdorff-Young, int g^{3/2} <= 4 for the density g of X^2 | 32π / |λ| |
| 2μ X_1 X_2 (hyperbolic pair) | |phi_k| <= (π/(|μ||t|))^{1/2} (Cauchy-Schwarz) | 6π / |μ| |
| λ<u,X>^2 + diagonal, max u_i^2 <= 1/2 | Theorem F, r = 1 | 24π / |λ| |
| any block with density <= D_k | ||phi_k||_3^3 <= ||phi_k||_2^2 = 2π int p_k^2 | 2π D_k |

Example: Q = 2(X_1X_2 + X_3X_4 + X_5X_6) (all 3-volumes carried by rows of marginal 1): ||p_Q||_∞ <= 3.
Hölder also mixes with Theorem F: Q = aX_0^2 + (independent spread rank-2 part) gives
||p_Q||_∞ <= (1/2π)(32π/|a|)^{1/3} (6B)^{2/3}, B = 4π|λ_1λ_2|^{-1/2}.

## 4. Peeling: a bridge between localized coordinates and Fourier bounds (PROVED)

Decoupling and Fresnel both lose the oscillation of a quadratic term carried by one or two
coordinates. For those, peel the coordinate(s) geometrically and pass the rest to a *fractional
potential*, which Fourier bounds control with less decay than a density needs. Write
H_α(Z) := sup_s E|Z - s|^{-α} (0 < α < 1) and D(Z) := ||p_Z||_∞.

**Lemma 4.1 (potentials from Fourier).** For 0 < α < 1, any real Z and s,
E|Z - s|^{-α} <= c_α int |t|^{α-1} |phi_Z(t)| dt, c_α = 2^{1-α} Γ((1-α)/2) / (2 sqrt(π) Γ(α/2));
c_{1/2} = (2π)^{-1/2}, c_{1/4} ≈ 0.1493 (Section 7). If |phi_Z| <= min(1, B|t|^{-b}) with b > α, then
H_α(Z) <= c_α · 2 b B^{α/b} / (α(b - α)); in particular H_{1/2} <= 8 B^{1/2}/sqrt(2π) when b = 1, and
H_{1/4} <= 16 c_{1/4} B^{1/2} when b = 1/2.
Proof. |x|^{-α} = Γ(α/2)^{-1} int_0^∞ u^{α/2-1} e^{-ux^2} du and e^{-ux^2} = (4πu)^{-1/2} int e^{-τ^2/4u} e^{iτx} dτ.
Everything is absolutely integrable after taking |phi_Z|; Tonelli in u gives the kernel
(4π)^{-1/2} Γ((1-α)/2) Γ(α/2)^{-1} (|τ|/2)^{α-1}. ∎ (A density needs b > 1; H_{1/2} needs b > 1/2;
H_{1/4} needs b > 1/4. This is where "half a power per eigenvalue" becomes exact bookkeeping.)

**Lemma 4.2 (square peel).** If A_ii = a ≠ 0, completing the square in x_i gives
Q = a (X_i + ℓ(X_{-i}))^2 + S(X_{-i}), S the Schur-complement form (with its linear and constant terms),
and D(Q) <= |a|^{-1/2} H_{1/2}(S). Moreover H_α(Q) <= M_α |a|^{-α} for α < 1/2, whatever S is,
where M_α = sup_c sup_f int |y^2 - c|^{-α} f(y) dy over densities f <= 1; M_{1/4} <= 4.
Proof. Given X_{-i}, V = X_i + ℓ has density <= 1 and aV^2 has density <= (|a||u|)^{-1/2} at u. For M_{1/4}:
for y >= 0, |y^2 - c| >= (y - sqrt c)^2 when c > 0 (and >= y^2 when c <= 0); the bathtub principle over
sets of measure 1 around the two roots gives <= 2 int_{-1/4}^{1/4} |v|^{-1/2} dv = 4. ∎

**Lemma 4.3 (coordinate hyperbola).** (a) If Y_1, Y_2 are independent with densities <= 1, then
Y_1 Y_2 has density <= 4 log(1 + 1/(2 sqrt|u|)) at u ≠ 0. (b) If A_ii = A_jj = 0 ≠ A_ij = μ then
Q = 2μ (X_i + β_j)(X_j + β_i) + S with S the Schur complement of the 2x2 block, and
D(Q) <= 2^{3/4} κ |μ|^{-3/4} H_{1/4}(S), κ = sup_{y>0} log(1+y)/sqrt(y) = 0.8047.
Proof. (a) p(u) = int f_1(y) f_2(u/y) |y|^{-1} dy; split at |y| = sqrt|u| and substitute y -> u/y in the
inner part; each half is <= sup{ int_{|y|>=a} h/|y| : 0 <= h <= 1, int h = 1 } = 2 log(1 + 1/(2a)),
a = sqrt|u| (bathtub). (b) Complete the product: 2μx_ix_j + 2x_iℓ_i + 2x_jℓ_j = 2μ(x_i + ℓ_j/μ)(x_j + ℓ_i/μ)
- 2ℓ_iℓ_j/μ; given the rest the two factors are independent with densities <= 1; use (a) and
log(1+y) <= κ sqrt(y). ∎

**Corollary 4.4 (what the peels prove).**
(i) *Square peel + Fresnel rank 2.* If A_ii = a ≠ 0 and the Schur complement is D' + λ_1uu^T + λ_2vv^T
with u, v orthonormal of leverage <= 1/2, then D(Q) <= 8 sqrt(2) |a|^{-1/2} |λ_1λ_2|^{-1/4}
(Theorem F with r = 2 gives B = 4π|λ_1λ_2|^{-1/2}, b = 1). This covers "diagonal + spread rank 2" whose
third large eigenvalue sits on a coordinate coupled to the frame, the case the lead singled out.
(ii) *Hyperbolic pair + one spread direction.* If A_ii = A_jj = 0 ≠ A_ij = μ and the Schur complement is
D' + λuu^T with leverage <= 1/2: D(Q) <= 2^{3/4} κ |μ|^{-3/4} · 16 c_{1/4} (4π/|λ|)^{1/4} ≈ 6.1 |μ|^{-3/4}|λ|^{-1/4}.
(iii) *Bounded dimension, zero diagonal.* Q = 2(X_1X_2 + X_2X_3 + X_1X_3) (eigenvalues 2, -1, -1; every
2x2 principal block indefinite; n = 3, so decoupling, Theorem D and Theorem F are all unavailable):
S = -2X_3^2, H_{1/4}(S) <= 2^{-1/4} M_{1/4}, so **D(Q) <= 4 sqrt(2) κ ≈ 4.55** (empirical max 2.05).
(iv) *Two square peels.* If the first Schur complement has a non-zero pivot a' as well, then
H_{1/2}(a'(V')^2 + S'') <= |a'|^{-1/2} (8 + 2 E log_+(|a'|/(4|s - S''|))) (from
int |y^2 - c|^{-1/2} f <= 2(4 + log_+(1/(4|c|))) for c > 0, and a log bound for c <= 0), and the log term is
finite as soon as S'' has any H_α, α > 0. Example: A = I - 2rr^T, r = (1,1,1)/sqrt 3 (n = 3, pivots
1/3 and -3, Schur complements -(Y_1^2 + 4Y_1Y_2 + Y_2^2) and then 3Y_2^2): bounded. Constants degrade like
|a|^{-1/2} as a pivot tends to 0; there the hyperbolic pivot (iii) takes over only when the diagonal is
exactly zero. A robust interpolation (a density bound for products of two general linear forms of a
2-dimensional product density, uniform in the forms up to the determinant) is not proved here; see 6.3.

These peels are the bounded-dimensional counterpart of the Fourier theorems: each large eigen-direction
supplies half a power of decay when spread (Theorem F), a full |t|^{-1} per well-conditioned heavy
coordinate coupled linearly to spread directions (Theorem MF), or a geometric peel when it sits on one
or two coordinates with a usable pivot.

## 5. Task 2: removing the leverage condition for rank-3 (and diagonal + rank-3) forms

Setting: A = D + R Λ R^T, D diagonal (D = 0 is the rank-3 case), R ∈ R^{n x 3} orthonormal columns,
rows r(i), leverages ℓ_i = |r(i)|^2 (sum ℓ_i = 3). Theorem F needs max ℓ_i <= 1/2 and then gives
C = 12 with no partition. Theorem D needs the I-side leverages (within I) <= 1/2 (< 3/4 with D'),
with heavy rows free to go to J.

### 5.1 Proposition (dichotomy, PROVED)
For δ ∈ (0, 1/2] let H = {i : ℓ_i > δ} (|H| < 3/δ) and L = [n] \ H. Exactly one of:
(a) λ_min(G_L) >= 2δ. Then, conditioning on X_H and applying Theorem F on L
(within-L leverage r(i)^T G_L^{-1} r(i) <= ℓ_i/λ_min(G_L) <= 1/2, det G_L >= (2δ)^3):
**||p_Q||_∞ <= 12 |λ_1λ_2λ_3|^{-1/3} (2δ)^{-1}.**
(b) Some unit vector e ∈ span(r_1, r_2, r_3) has |e_L|^2 < 2δ: at least 1 - 2δ of its squared mass lies
on the fewer than 3/δ coordinates of H.
(Proof: λ_min(G_L) = min_{|u|=1} |(Ru)_L|^2.) With δ = 1/10: either C = 60, or a unit vector of the
eigenspace has 80% of its mass on fewer than 30 coordinates. This replaces the random-partition /
matrix-Chernoff version of the S3 route (which also works, with worse constants, e.g. 24 sqrt 2/η for
λ_min(G_L) >= η, L = {ℓ_i <= η/24}); Theorem F does not need two good sets.

### 5.2 What localization gives, and what is proved in each case
Let k ∈ {1,2,3} be the number of eigenvalues of G_L below 2δ (the dimension of the localized part).

* **k = 3 (fully localized).** G_H >= (1-2δ) I_3. Condition on X_L: the remaining polynomial lives on
  m < 3/δ coordinates and its quadratic part D_H + R_H Λ R_H^T has a rank-3 part with eigenvalues λ_k θ_k,
  θ_k ∈ [1-2δ, 1] (Ostrowski: R_H Λ R_H^T is similar to G_H^{1/2} Λ G_H^{1/2}). So the rank-3 conjecture is
  reduced, with an explicit constant in the spread alternative, to the **bounded-dimensional problem
  BD(m)**: a universal C(m) for quadratic polynomials in m variables whose quadratic part is
  (diagonal) + (rank 3 with eigenvalues >= 1 - 2δ in modulus). BD(m) is not proved here in general.
  Proved sub-cases (Section 4): a pivot sequence with non-zero pivots (iterated square peels; constants
  degrade like |pivot|^{-1/2}), zero-diagonal hyperbolic pairs (Lemma 4.3), definite 2x2 blocks (K3),
  and independent blocks (Prop. H).
* **k = 1 or 2 (hybrid: localized + spread directions).** Proved sub-cases:
  - the localized part is an independent block (e.g. e = e_1 exactly, Q = λX_1^2 + spread rank 2):
    Prop. H + Theorem F, or Cor. 4.4(i);
  - a heavy coordinate with a usable pivot whose Schur complement keeps a spread rank-2 part: Cor. 4.4(i);
  - heavy coordinates entering through linear coupling to spread directions (the localized direction is
    "hyperbolic", e.g. e ∝ e_1 ± g): Theorem MF (example 2X_1G + Y^2, C = 7.57);
  - a direction spread over >= 3 heavy coordinates of comparable weight: Theorem D (two of them in I,
    the rest in J) or Theorem F after conditioning on the others.
  Not proved: a general hybrid in which a localized direction is carried by one or two coordinates with a
  small but non-zero pivot and also couples to the spread part in a way that none of the three
  mechanisms isolates. I have no counterexample; the numerics of Section 7 show nothing unbounded.

### 5.3 Limits of the Fourier route (why a geometric input is unavoidable)
* Theorem F needs at least 6 coordinates with non-zero rows (leverage <= 1/2, sum = 3); decoupling needs
  |I| >= 5 rows of marginal < 3/4 plus 3 more columns. For n <= 5 (and for any form whose three large
  directions are carried by <= 5 coordinates) neither applies.
* For n = 3 decoupling gives rank(A_IJ) <= 1, i.e. at best |phi| <= C|t|^{-1/4}.
* (F2) shows the per-direction |t|^{-1/2} bound is false for a direction on one coordinate, and
  Theorem F shows it is true as soon as every coordinate weight is <= 1/2. So "localized" in the precise
  sense needed is: **some unit vector of the relevant eigenspace has a coordinate weight > 1/2**, or
  more quantitatively the dichotomy (b).
* Keeping the Fresnel phases would be needed for forms like A = I - 2rr^T (n = 3, "diagonal + rank 1"
  with every leverage 1/3): taking absolute values inside the Fresnel integral loses exactly the
  cancellation between the Fresnel phase and the twists and gives only |phi| <~ |t|^{-1} (computed for the
  uniform law: each twisted factor has L^3_τ norm ~ |t|^{-1/6}). This example is bounded by two square
  peels (Cor. 4.4(iv)), not by Fourier.

## 6. Tasks 3-4: general A, the complement of Theorem D, and what remains

### 6.1 The "three large singular directions" lemma (Task 3)
Answer: **true in the volume-sampling form** (Theorem D): Z = e_3(s^2) >= s_1^2 s_2^2 s_3^2 and every
additional singular direction only increases Z, so dense perturbations are harmless. The hypothesis is
not a leverage condition on the top three left singular vectors alone but on the marginals
α_i = sum_m p_m u_m(i)^2, which mix all directions with weights p_m. My own first attempt (Hölder
against the density of a projection c = V^T W) needs A_IJ to have exact rank r and pays the product
of *all* r singular values, so it breaks down for "spread rank 3 + ε noise"; the lead's BL on R^J with the
coordinate densities g_j as factors is the right object, and Section 1 confirms it. Numerically (N5):
spread rank 3 on n = 30 gives Z = 0.0094, bound 21.5 (empirical 3.8); adding 0.2·Wigner raises Z to 0.089
and lowers the bound to 14.8 (empirical 2.0).

### 6.2 The complement and which tool covers which part
A form escapes Theorem D and its extensions D', D_5 when, for every disjoint I, J, the 5-volume of A_IJ
is small and the 3-volume is small or carried by rows of marginal >= 3/4. The classes this leaves, the
example, and the tool that proves a universal bound for it:

| class | example | tool | constant |
|---|---|---|---|
| two same-sign large diagonal entries, weak coupling | diag(1,1,-1) + small | K3 (definite 2x2 principal block) | π / sqrt(det) |
| diagonal + spread rank r >= 3 | D + RΛR^T, leverages <= 1/2 | Theorem F | 4r/(r-2) · prod|λ|^{-1/r} (12 for r = 3) |
| diagonal + spread rank 2, third eigenvalue off-frame | aX_0^2 + Fresnel rank 2 | Prop. H + Theorem F | explicit (3.3) |
| diagonal + spread rank 2, third eigenvalue on a coupled coordinate | pivot a, Schur complement spread rank 2 | Cor. 4.4(i) | 8 sqrt 2 |a|^{-1/2} |λ_1λ_2|^{-1/4} |
| heavy coordinates coupled linearly to spread directions | 2X_1<g,X> + <r_2,X>^2 | Theorem MF | 7.57 |
| >= 3 heavy coordinates with well-conditioned coupling columns | star-like A_LH | Theorem D with the heavy side as J | 6 sqrt(e) Z^{-1/6} |
| >= 3 independent small blocks | 2(X_1X_2 + X_3X_4 + X_5X_6) | Prop. H | 3 |
| bounded dimension, zero-diagonal pair | 2(X_1X_2 + X_2X_3 + X_1X_3) | Lemma 4.3 | 4.55 |
| bounded dimension, non-zero pivots | I - 2rr^T on R^3 | iterated square peels, Cor. 4.4(iv) | bounded, pivot-dependent |

### 6.3 What remains open (precisely)
* **R1, the glue.** A structural theorem saying that every A with three eigenvalues >= 1 in modulus
  falls, with universal parameters, into one of the rows above. For rank-3 plus diagonal, Proposition 5.1
  supplies the first split (C = 60, or a direction 80%-localized on < 30 coordinates), but the localized
  alternative is then only covered in the sub-cases listed in 5.2. For general A I have only the heuristic
  that small decoupling capacity means "diagonal + off-diagonal part of low rank or supported on a bounded
  set of rows/columns + a perturbation", and Theorems F and MF require the low-rank part to be *exact*:
  a perturbation E of a *localized* low-rank structure is handled neither by them (e^{itX^T E X} is not a
  product twist) nor by Theorem D (the volume is localized). Perturbations of *spread* structure are fine
  (Theorem D).
* **R2, the bounded-dimensional problem BD(m).** Pivot peels give bounds that degrade like
  |pivot|^{-1/2}; Lemma 4.3 covers exactly zero diagonals. What is missing is a density bound for a product
  of two general linear forms L_1 L_2 of a 2-dimensional product density (f_1, f_2 <= 1), uniform in the forms
  up to the determinant, of the shape (C/|det|)(1 + log_+(1/|u|)) after normalisation. The square-peel
  computation gives (2/|Δ|)(C + log_+(Δ^2/(4|αγ u|))) for L_1 = αY_1 + βY_2, L_2 = γY_1 + δY_2, which blows up
  only logarithmically as αγ -> 0, and Lemma 4.3 is the endpoint αγ = βδ = 0; an interpolation between the two
  (perturbing the bathtub argument of 4.3 for nearly coordinate forms) looks routine but is not written.
  With it, BD(3) would follow from the peel calculus.
* **R3, phases.** All the Fourier bounds here take absolute values of a Fresnel-linearised or decoupled
  integrand. For "diagonal + rank 1" on few coordinates (A = I - 2rr^T) this loses the decisive cancellation
  (Section 5.3). A proof of the full conjecture along Fourier lines would need a phase-sensitive estimate
  there; the geometric peels avoid the issue.

### 6.4 What the Fourier route proves (Task 4), in one list
With X_i independent (i.i.d. is never used), densities <= 1, arbitrary linear and constant terms:
1. Theorem D and D', D_5 (Section 1): any A with a decoupled block of 3-volume Z and I-marginals <= h < 3/4:
   ||p_Q||_∞ <= 6 sqrt(e) (2h)^{-1/2} (3-4h)^{-1} Z^{-1/6} (= 6 sqrt(e) Z^{-1/6} for h <= 1/2); any A with a
   decoupled block of 5-volume Z_5: ||p_Q||_∞ <= 11.66 Z_5^{-1/10}.
2. Theorem F: A = D + RΛR^T with coordinate weights <= 1/2 of the rank-r part: 4r/(r-2) · prod|λ|^{-1/r};
   in particular **every rank-3 form in which each coordinate has leverage <= 1/2 in the eigenspace: C = 12**.
3. Theorem MF, Proposition H and the peel corollaries of Section 4, with the constants stated there.
4. For rank-3 + diagonal: the dichotomy of Proposition 5.1.
Not proved: the conjecture in general; the missing pieces are R1-R3.

## 7. Numerics (scripts in num/, each well under 10 minutes, BelowNormal priority)

All histogram densities use bin width 0.01 and 1-3 million samples; they are lower bounds for the
true sup (a histogram smooths singularities) and serve only to catch a wrong upper bound.

**N1 (n1_lp.py) L^p lemma.** int|psi|^p for the uniform law and three lattice-like laws (density 1 on
2, 10 and 20 small intervals), p ∈ {2, 2.5, 3, 4, 6, 10}. Uniform: 6.282 (= 2π) at p = 2, 5.359 at p = 2.5,
4.834 at p = 3, 2.704 at p = 10; every value lies below 2 sqrt(2) π/sqrt(p) (and far below the proved 4π/sqrt(p)).

**N2 (n2_thmD.py) Theorem D.** 30 random matrices (4-7 rows, 3-6 columns, rank >= 3, some with a heavy row):
brute-force volume-sampling marginals agree with sum_m p_m u_m(i)^2 to 1.5e-14; Z = e_3(s^2) and
sum α = sum β = 3 exactly; 60 000 random Gaussian parameter sets never push
Z · prod d^α prod e^{1-β} / det(D + M^T D_I M) above 1.

**N3 (n3_examples.py) the new classes** (MC noise on |phi| about 6e-4):

| form | law | max density | proved bound | |phi(50)| | bound at t = 50 |
|---|---|---|---|---|---|
| D + spread rank 3 (n = 40, max leverage 0.27, D ∈ [-3,3]) | uniform | 0.50 | 12 | < 1e-3 | 0.126 |
| same | lattice-like | 0.001 | 12 | < 1e-3 | 0.126 |
| 2X_1<g,X> + <r_2,X>^2 (n = 60) | uniform | 3.43 | 7.57 | 0.0289 | 0.063 |
| same, X_1 lattice-like | mixed | 1.20 | 7.57 | 0.0257 | 0.063 |
| 2(X_1X_2 + X_3X_4 + X_5X_6) | uniform | 1.45 | 3 | 4e-4 | 0.0157 |
| 2(X_1X_2 + X_2X_3 + X_1X_3) | uniform | 2.05 | 4.55 | 0.0084 | - |

For the mixed-Fresnel example |phi| falls by a factor 3.91 from t = 20 to t = 50 (t^{-3/2} predicts 3.95).

**N4 (n4_checks.py, n4c_resonance.py).** c_{1/2} = 0.398942 = (2π)^{-1/2}, c_{1/4} = 0.149270,
κ = 0.80474. Coordinate-hyperbola lemma, exact quadrature for four product laws at seven levels u: the
largest ratio density/bound is 0.995 (two shifted uniforms at u = 1e-4), so Lemma 4.3(a) is essentially
sharp and never violated. Resonance (F2): X uniform on {x ∈ [0,R]: cos(sx^2) >= 0} gives
|E e^{isX^2}| = 0.68, 0.66, 0.65, 0.64 at s = 20, 80, 320, 1280 (about 2/π, no decay), while the sum of two
independent copies gives 0.058, 0.017, 0.005, 0.0013, below the Cauchy-Schwarz/Theorem F bound
sqrt(π/s) = 0.40, 0.20, 0.10, 0.05. This is the per-direction dichotomy of Section 3.1 in numbers.

**N5 (n5_small_dense.py).** n = 3 cores, random search over 40 shifted-uniform laws: I - 2rr^T max 2.54,
J - I max 2.05, both at the centred law. Theorem D on n = 30 with a random balanced split:
orthogonal-conjugated signs (all |eig| = 1): Z = 41.0, max marginal 0.27, bound 5.33, empirical 0.65;
spread rank 3: Z = 0.0094, marginal 0.43, bound 21.5, empirical 3.80; plus 0.05·Wigner: bound 20.4,
empirical 3.15; plus 0.2·Wigner: bound 14.8, empirical 2.02.

**N6 (n6_breakF.py) trying to break Theorem F at its edge.** Rank-3 part with λ = (1,1,-1) and max
leverage 0.50 (n = 6: the pair-sum frame rotated by a random O(3); n = 8, 10: random frames with max
leverage 0.499-0.500), three diagonals (D = 0; D = -diag(RΛR^T), which makes A zero-diagonal; D random in
[-2,2]) and three laws (centred uniform, uniform on [0,1], the resonant law of N4 at s = 8): 27 cases.
Largest histogram density 3.77 against the bound 12 (ratio 0.31); largest |phi(t)| t^{3/2} / (4π)^{3/2}
over t ∈ {3, 6, 12, 24} is 0.27 (bound: 1). Making A zero-diagonal changes nothing, as the theorem predicts: the diagonal enters only as a twist.

No numerical result contradicts any bound, and no configuration produced an unbounded-looking density.

---
Files: REPORT.md (this), sec*.md (the same sections separately), num/*.py (numerics).
