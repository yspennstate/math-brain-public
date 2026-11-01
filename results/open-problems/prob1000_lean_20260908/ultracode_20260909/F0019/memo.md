# F0019 - Zygouras, Question 2: is f'(beta) < 0 throughout strong disorder?

Attempt of 2026-09-09 (claude, ultracode lane). Status: partial. Nothing here settles the question;
what is new is an exact finite-n formula for the beta-derivative of the mean replica overlap, a
reduction of the Gaussian case to the monotonicity of that overlap in beta, a correction to the
earlier ledger attempt, and a Lean-certified convex-analysis step behind the large-beta bound.

## 1. The problem as the source states it

Zygouras, "Directed polymers in a random environment: a review of the phase transitions",
arXiv 2401.01757, Section 3.1, PDF page 13. Verbatim:

> Under the assumption of very strong disorder and additionally that f(β) is differentiable and
> f'(β) < 0, Bates [B19, B21] and Bates-Chatterjee [BC20] have given quantitative estimates on
> localisation in terms of overlaps and in terms of Césaro means of end-point distributions [BC20b].
> [...] The relation between the derivative of the free energy and localisation properties of the
> polymer was first observed Carmona-Hu [CH02]. In relation to the discussion above about strong
> and very strong disorder we can also pose the question:
>
> **Question 2.** Does f'(β) < 0 hold in the whole strong disorder regime ?

Here f(β) = lim n^{-1} log W_n^β (Definition 3.9, eq. (3.12)), W_n^β the normalised partition
function, strong disorder means W_∞^β = 0, i.e. β > β_c. The ledger row quotes this correctly.
Note the quantifier: f'(β) < 0 at EVERY β in the strong disorder regime. Since f + λ is convex,
f has one-sided derivatives everywhere and is differentiable off a countable set, so the question
has a one-sided reading (f'(β-) < 0 and f'(β+) < 0 for every β > β_c) and a stronger reading
(f differentiable everywhere on (β_c, ∞) with negative derivative). Bates (arXiv 1910.12012,
Remark 1.2) records the stronger form as Comets' Conjecture 6.1 (Comets, Directed polymers in
random environments, LNM 2175, 2017): "It is believed (see [12, Conj. 6.1]) that there are
actually no points of non-differentiability, and moreover that p'(β) < β for all β > β_c."
(Gaussian case, p = f + β²/2.)

## 2. Notation and the standard facts used

Environment ω i.i.d. with λ(β) = log E e^{βω} < ∞ for all β. Z_n = E_X e^{βH_n(X)},
H_n(X) = Σ_{k≤n} ω_{k,X_k}, W_n = Z_n e^{-nλ}, p_n(β) = n^{-1} E log Z_n, p = lim p_n = f + λ.
μ_n = μ_n^{β,ω} is the length-n polymer measure. For replicas X^1, X^2, ... drawn from μ_n^{⊗m},
R_{ab} = n^{-1} Σ_{k≤n} 1{X^a_k = X^b_k} is the overlap fraction, and

    OV_n = μ_n^{⊗2}(R_12) = n^{-1} Σ_{k≤n} Σ_x μ_n(X_k = x)²          (whole-path overlap of μ_n),
    EP_n = n^{-1} Σ_{k≤n} Σ_x μ_{k-1}(X_k = x)²  = n^{-1} Σ_{k≤n} I_k   (the source's (3.9), endpoint overlaps).

Facts. (A) p_n is convex, so p is convex, f + λ is convex, f is nonincreasing (Comets-Yoshida 2006);
one-sided derivatives exist everywhere and p_n' → p' at differentiability points. (B) Gaussian
ω ~ N(0,1): Carmona-Hu 2002, Lemma 7.1, and Lacoin 2025 (arXiv 2505.13382, Theorem C, eq. (6)):
p_n'(β) = β(1 - E OV_n(β)), hence

    -f'(β+) ≤ β liminf_n E OV_n(β) ≤ β limsup_n E OV_n(β) ≤ -f'(β-).

(C) Under strong disorder, a.s. for large n, -c_1 log W_n ≤ Σ_{k≤n} I_k ≤ -c_2 log W_n (source, (3.11)).
(D) Strong disorder = very strong disorder: Junk-Lacoin 2024 (arXiv 2402.02562) for disorder bounded
above; Junk 2025 (arXiv 2502.04113, "Coincidence of critical points for directed polymers for general
environments and random walks") for general environments. So f(β) < 0 for every β > β_c.

## 3. Findings

### 3.1 Audit of the earlier ledger attempt F0019-A001: its main step is wrong

A001 argued: f'(β) = -β lim E OV_n (correct, this is (B)); Σ_{k≤n} I_k ≥ c_1 n |f| (correct, from (C)
and (D)); and then identified Σ_k E I_k with n E OV_n "up to a boundary term of order o(n) by the
usual telescoping argument", concluding f'(β) ≤ -β c_1 |f(β)| < 0 at differentiability points.
The identification is false. I_k is the overlap at time k of the LENGTH-(k-1) polymer's prediction
for X_k; the k-th term of OV_n is the overlap at time k of the LENGTH-n polymer, which reweights
the time-k marginal by the future partition functions. Both are Cesaro means of n terms of different
measures; there is no telescoping. Numerically (d = 1, Gaussian, β = 1, exact transfer matrices,
overlap_d1.py part (a)):

    n     E OV_n    E EP_n    ratio
    25    0.432     0.269     1.61
    50    0.397     0.238     1.67
    100   0.369     0.209     1.77
    200   0.359     0.193     1.86
    400   0.346     0.181     1.91

The ratio is not tending to 1; the two quantities differ at order n. So A001 proves nothing beyond
(B). Its conclusion (f' < 0 at differentiability points in the Gaussian case) remains exactly the
open question, restated as "liminf_n E OV_n(β) > 0 for all β > β_c".

### 3.2 The large-beta region (known; made explicit, convex step Lean-certified)

Let m_d := lim n^{-1} E max_X H_n(X) (exists by superadditivity; finite by the exponential-moment
union bound). Since Z_n ≤ e^{β max H}, p_n(β) ≤ β m_d for every n and β ≥ 0, hence p(β) ≤ β m_d,
p(0) = 0, p convex. A convex function on [0,∞) lying below the line β m_d has all secant slopes ≤ m_d
(this is the statement certified in U_F0019.lean, theorem secant_le_of_convexOn_le_linear), so
p'(β±) ≤ m_d for every β ≥ 0, and

    f'(β±) ≤ m_d - λ'(β)   for every β ≥ 0, any environment with all exponential moments.

Since λ' is strictly increasing with λ'(β) → ess sup ω, this gives f'(β±) < 0 for all
β > β_1 := inf{β : λ'(β) > m_d}, and β_1 < ∞ iff m_d < ess sup ω (which fails exactly when the
sites carrying the maximal value percolate along oriented paths). Gaussian case: λ' = β and
m_d = c_d ≤ sqrt(2 log 2d) (first-moment bound), so f'(β±) ≤ c_d - β < 0 for β > c_d. Bates
(1910.12012, Section 1.2) attributes the same large-β conclusion to the boundedness of p' in
Comets' notes, Prop. 2.1(iii); I am not claiming novelty, only stating the threshold. What is
open is therefore the window (β_c, β_1]; in d = 3 with Gaussian disorder, β_c ≥ β_2 ≈ 1.04 (the L²
threshold from the Z³ return probability) while c_3 ≤ 1.89, so the window is presumably nonempty.

### 3.3 f' < 0 on a set of positive measure near every point of strong disorder (trivial)

f + λ is convex, hence locally Lipschitz, so f(β) = f(β') + ∫_{β'}^{β} f'(s) ds with f' ≤ 0 a.e.
If f(β) < 0 then {s ∈ (β_c, β) : f'(s) < 0} has positive Lebesgue measure, since f = 0 on [0, β_c].
With (D), this holds for every β > β_c. This does not exclude f' vanishing on an interval inside
(β_c, ∞) or at isolated points; convexity of f + λ alone allows both.

### 3.4 Gaussian reduction: monotone mean overlap implies Question 2 (one-sided form)

Claim. Gaussian disorder. Suppose that for every n the map β ↦ E OV_n(β) is nondecreasing on
(β_c, ∞) (it suffices that β ↦ limsup_n E OV_n(β) is nondecreasing). Then f'(β-) < 0 for every
β > β_c, and f'(β) < 0 at every differentiability point of f in (β_c, ∞).

Proof. Fix β > β_c. By 3.3 there is a set of positive measure of s ∈ (β_c, β) with f'(s) < 0; at
a.e. such s, f is differentiable and (B) gives lim_n E OV_n(s) = -f'(s)/s > 0. Pick one such s.
Monotonicity gives limsup_n E OV_n(β) ≥ limsup_n E OV_n(s) > 0, and (B) gives
f'(β-) ≤ -β limsup_n E OV_n(β) < 0. At differentiability points f'(β) = f'(β-). QED.

So the Gaussian Question 2 follows from "the mean whole-path overlap is nondecreasing in the inverse
temperature", a statement of the same flavour as the Comets-Yoshida monotonicity of f itself.

### 3.5 An exact formula for d/dβ E OV_n: a signed Ghirlanda-Guerra defect

Gaussian disorder. Write ⟨·⟩ for μ_n^{⊗4} and E⟨·⟩ for its environment average. Then for every
n and β > 0,

    d/dβ E OV_n(β) = 2 β n · E⟨ R_12² + 3 R_12 R_34 - 4 R_13 R_23 ⟩.                (*)

Derivation. q := E OV_n = 1 - p_n'/β, so q' = (p_n' - β p_n'')/β², with p_n' = n^{-1} E μ_n(H) and
p_n'' = n^{-1} E Var_{μ_n}(H). Index sites by i = (k,x), write μ_i = μ_n(i ∈ X), μ_ij = μ_n(i,j ∈ X),
C_ij = μ_ij - μ_i μ_j, so that Var_μ(H) = Σ_ij ω_i ω_j C_ij. Gaussian integration by parts
(∂_{ω_i} μ(A) = β(μ(A, i ∈ X) - μ(A) μ_i)) gives E μ(H) = β Σ_i E C_ii and
E Var_μ(H) = Σ_i E C_ii + Σ_ij E ∂_i ∂_j C_ij, hence β E Var = E μ(H) + β Σ_ij E ∂_i∂_j C_ij
and q' = -(nβ)^{-1} Σ_ij E ∂_i ∂_j C_ij. Differentiating twice,

    ∂_i∂_j C_ij = β² [ μ_ij - 2μ_iμ_ij - 2μ_jμ_ij + 8μ_iμ_jμ_ij - 2μ_ij² - μ_iμ_j + 2μ_i²μ_j + 2μ_iμ_j² - 6μ_i²μ_j² ]

(for i = j this reduces to β²(m - 7m² + 12m³ - 6m⁴), m = μ_i, which agrees with a direct second
derivative of m(1-m)). Summing over all pairs of sites and using that every path has exactly n
sites: Σ μ_ij = Σ μ_iμ_j = n², Σ μ_iμ_ij = n² ⟨R_12⟩, Σ μ_iμ_jμ_ij = n² ⟨R_13R_23⟩,
Σ μ_ij² = n² ⟨R_12²⟩, Σ μ_i²μ_j = n²⟨R_12⟩, Σ μ_i²μ_j² = n² ⟨R_12R_34⟩. The ⟨R_12⟩ terms
cancel (-2-2+2+2) and the constants cancel (1-1), leaving Σ_ij ∂_i∂_j C_ij =
2β²n² ⟨4R_13R_23 - R_12² - 3R_12R_34⟩, which is (*).

Two independent checks of (*). (i) n = 1 (two sites, μ = (σ, 1-σ), σ = sigmoid(βΔ), Δ ~ N(0,2),
s = σ(1-σ)): (*) reads q' = 4β E[6s² - s]; a direct differentiation of q = 1 - 2E s and one
Gaussian integration by parts in Δ give the same. (ii) Exact enumeration of all 2^n paths in d = 1
for n = 2, 3, 4, 6, averaging over 2·10^5 (6·10^4 for n = 6) environments, central differences in
β on the same environments (gg_defect_exact_small_n.py, log in gg_defect_exact_small_n.log):

    n  β    FD dq/dβ   formula (*)   |  FD p_n'   β(1 - E OV_n)
    2  0.5  0.1897     0.1894        |  0.2540    0.2529
    2  1.0  0.1867     0.1881        |  0.4073    0.4074
    2  2.0  0.1009     0.0991        |  0.5313    0.5310
    3  0.5  0.2040     0.2034        |  0.2719    0.2719
    3  1.0  0.2040     0.2051        |  0.4353    0.4370
    3  2.0  0.1089     0.1098        |  0.5644    0.5663
    4  0.5  0.2137     0.2143        |  0.2855    0.2861
    4  1.0  0.2174     0.2172        |  0.4580    0.4585
    4  2.0  0.1152     0.1110        |  0.5912    0.5889
    6  0.5  0.2287     0.2289        |  0.3049    0.3059
    6  1.0  0.2355     0.2368        |  0.4873    0.4893
    6  2.0  0.1235     0.1195        |  0.6246    0.6231

Agreement is within Monte Carlo error at every entry (the right-hand pair is the identity (B),
also confirmed). The off-diagonal terms of (*) are exercised from n = 2 on.

Why (*) is interesting. The bracket in (*) is a Ghirlanda-Guerra combination: if the overlap
distribution satisfied the two classical identities E⟨R_12R_13⟩ = ½E⟨R_12²⟩ + ½(E⟨R_12⟩)²
and E⟨R_12R_34⟩ = ⅓E⟨R_12²⟩ + ⅔(E⟨R_12⟩)², the bracket would vanish identically. Since
d/dβ E OV_n is O(1) while the bracket carries a prefactor 2βn, the identity (*) says the
Ghirlanda-Guerra defect of the finite-n polymer is exactly O(1/n) and that its SIGN is the
monotonicity of the mean overlap. The reduction in 3.4 therefore becomes:

    Gaussian Question 2 (one-sided form) ⟸ for all n and β > β_c:
         E⟨R_12²⟩ + 3 E⟨R_12R_34⟩ ≥ 4 E⟨R_13R_23⟩   under μ_n^{⊗4}.                 (**)

I could not prove (**). Note it is not a pathwise inequality: in d = 1, n = 100, the quenched
OV_n(β) decreased somewhere along the β-grid in 44 of 300 environments (worst single step
-0.157), while the environment average increased at every step (overlap_d1.py part (c)):

    β        0.10   0.25   0.50   0.75   1.00   1.25   1.50   2.00   2.50   3.00   4.00
    E OV_n   0.108  0.130  0.199  0.286  0.374  0.449  0.514  0.613  0.679  0.726  0.790

and in d = 2 (n = 24, 60 environments) the mean also increased at every step of the grid
0.25, 0.5, 0.75, 1, 1.5, 2, 3 (0.066, 0.087, 0.123, 0.177, 0.317, 0.443, 0.597), here with no
pathwise violation. This is evidence for (**) in the regime numerics can reach; it says nothing
about d ≥ 3 just above β_c, which is where the question lives.

## 4. What is not done

- (**) is unproved; it is the whole of the Gaussian case. A proof would need to control the
  O(1/n) correction to the Ghirlanda-Guerra identities with a sign, which no existing technique
  does (the identities themselves are proved only on average over β, from concentration of μ(H)).
- Non-Gaussian environments: no overlap identity; f'(β) = lim n^{-1} E μ_n(H) - λ'(β) at
  differentiability points, and the only signed statement I have is 3.2.
- Differentiability of f at every β > β_c (the stronger form, Comets' Conj. 6.1): untouched.
- Lacoin 2025 shows f(β) = o((β - β_c)^K) for every K, so f'(β_c+) = 0 and f' is extremely small
  just above β_c; the question there is delicate and no numerics can see it.

## 5. Checks run

- overlap_d1.py: transfer-matrix d = 1 numerics for 3.1 (OV vs EP), identity (B) by central
  differences (β = 0.5, 1, 2: 0.4028/0.4035, 0.6288/0.6275, 0.7718/0.7574; the last pair is at
  the edge of the sampling error, the exact small-n test in 3.5 confirms (B) at β = 2 to 0.5%),
  and the monotonicity table in 3.5. Results in overlap_d1_results.json.
- gg_defect_check.py: a first transfer-matrix check of (*) at n = 12; the run was starved of CPU
  (machine at 100% from other sessions) and rerun at reduced size; its numbers are noisy and
  superseded by gg_defect_exact_small_n.py. Kept for the record (gg_defect_run.log).
- gg_defect_exact_small_n.py: the exact path-enumeration check of (*) and (B), table in 3.5.
- U_F0019.lean: the convex slope bound of 3.2, compiled clean with `lake env lean` in ~/erdos_fc
  on the first attempt; axioms: propext, Classical.choice, Quot.sound only.

## 6. The strongest case that this memo is wrong, and the check

The only claims here that go beyond bookkeeping are (*) and the reduction 3.4. If the site-pair
expansion behind (*) had an error in the off-diagonal terms, the formula would still be right at
n = 1 (checked by hand) and wrong for n ≥ 2. That is exactly what the enumeration test targets: at
n = 2..6 the off-diagonal sums dominate, and the finite-difference derivative matches (*) at all
twelve (n, β) pairs within Monte Carlo error. The reduction 3.4 uses only (B), 3.3 and the
hypothesis; the hypothesis is the thing not proven, and the pathwise counterexamples show it can
only hold on average, which is stated. The 3.2 bound could fail only if p_n ≤ β m_d failed, but
that is Z_n ≤ e^{β max H}, or if m_d did not exist, but E max H_n is superadditive.

## 7. Prior art

- Search phrases that found things: "directed polymer" "free energy" derivative "strong disorder"
  Bates Chatterjee; "Junk Lacoin directed polymer free energy derivative strong disorder 2024 2025";
  "Stefan Junk directed polymer 2025 2026 arXiv strong disorder"; Lacoin "localization transition"
  directed polymer "is smooth". (The session's search budget ran out after these.)
- Lacoin, The localization transition for the directed polymer in a random environment is smooth,
  arXiv 2505.13382 (May 2025): Theorem C (6) is the exact Gaussian identity between f'(β±) and the
  limiting mean overlap; Theorem 2.1 gives ν = ∞ at β_c. Does not address the sign of f' away
  from β_c.
- Junk, Coincidence of critical points for directed polymers for general environments and random
  walks, arXiv 2502.04113: strong = very strong disorder for general environments (removes A001's
  dependence on the bounded-disorder assumption of Junk-Lacoin, arXiv 2402.02562).
- Bates, Full-path localization of directed polymers, arXiv 1910.12012, Remark 1.2 and Section
  1.2: the conjecture is Comets' Conj. 6.1 (LNM 2175, 2017); large β follows from the boundedness of
  p' (Comets Prop. 2.1(iii)); identity (1.7) is Bates-Chatterjee, Localization in Gaussian
  disordered systems at low temperature, Ann. Probab. 48 (2020), Cor. 3.10.
- Carmona-Hu 2002, Lemma 7.1 (the finite-n identity); Comets-Shiga-Yoshida 2003 (eq. (3.11) of
  the source).
- Nothing found that proves f' < 0 on all of (β_c, ∞) in any dimension d ≥ 3, for any environment.
  The question is open as of this search.
