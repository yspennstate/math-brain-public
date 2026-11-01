from pathlib import Path
P=Path('.')
P.joinpath('ATTEMPT.md').write_text(r'''# F0087 — mathematical attempt, 2026-10-11

## 1. Exact question and explicit special-case setting
Kenyon asks for the scaling limit of exp(iαh), with constant α, and conjectures rotational invariance for uniform square-grid dimers. His h uses reference flow 1/4, so H=4h is the integer domino height. The source does not prescribe a domain, a Gibbs slope, an additive constant, a topology, or a multiplicative renormalization. These choices are mathematically significant.

Our unconditional special-case theorems concern the canonical translation-invariant, zero-slope, infinite-volume uniform square-grid dimer Gibbs measure used by Dubédat. We pin h(0)=0 at a dual face. Identify dual faces with Z², translated so the pinned face has coordinate (0,0). Choose the sign of H so that along a horizontal dual edge (x,y)→(x+1,y),

    ΔH = (-1)^(x+y)(1−4N_e),

and along a vertical edge (x,y)→(x,y+1),

    ΔH = (-1)^(x−1+y)(1−4N_e),

where N_e is the indicator of the crossed primal dimer. Reversing the height convention conjugates all observables and preserves the conclusions. Our finite rectangles use the equivalent picture in which primal vertices are checkerboard cells and dual vertices are their corners.

Embed the height electric field using cells Q_epsilon(f)=epsilon(f+[0,1)²):

    U_epsilon,alpha(z)=exp(iαh(f)),  z∈Q_epsilon(f).

All statements below about this embedding concern laws on the infinite-volume model, not arbitrary bounded-domain tilings or nonzero slope.

## 2. P1: deterministic residues and exact charge aliases
For every configuration, h(f)−r(f)∈Z, where the following table defines r modulo Z:

    (x mod 2,y mod 2):  (0,0)    (1,0)    (0,1)    (1,1)
    r(x,y):                0       1/4      −1/4       1/2.

Proof. Along any directed edge the difference between Δh and its background increment sign/4 is −sign·N_e, an integer. Therefore the residue modulo Z is deterministic along every finite path starting at 0. The displayed table has exactly the background increments modulo Z: on horizontal edges it changes by (-1)^(x+y)/4, and on vertical edges by (-1)^(x−1+y)/4. These assertions can each be checked for the four parity pairs. For instance, the horizontal change at odd x and odd y is −1/4−1/2=−3/4≡1/4. The table takes value 0 at the pinned face, so induction along a path proves h(f)≡r(f) mod Z. Actual height increments are closed because each cell has exactly one dimer; pinning fixes the integration constant. This argument uses actual height closedness, not real-valued closedness of the background increments alone. QED.

In particular, for every integer m,

    exp(i(α+2πm)h(f)) = exp(2πimr(f)) exp(iαh(f)).       (2.1)

Proof. Write h(f)=r(f)+n_f with n_f integer and use exp(2πimn_f)=1. Applying (2.1) at f and g shows that the **absolute value** of the two-point electric correlator is periodic in α with period 2π. The complex correlator need only be periodic up to a deterministic phase. The full pinned observable has exact period 8π. These distinctions rule out applying a quadratic, nonperiodic Gaussian exponent to all α without first reducing the charge and retaining the lattice phase. QED.

A kernel-checked finite algebraic part is in `HeightResidue.lean`: arbitrary oriented crossing signs s and integer occupancies n give path sum ∑s(1−4n) differing from its background sum ∑s by a multiple of 4; two paths with equal background sum consequently have the same height residue mod 4. This is the path-sum algebra, not a Lean formalization of dimer probability or scaling convergence.

## 3. P2: quantitative zero limit for nonresonant charges
Let α/(2π)=m+s with m∈Z and −1/2<s<1/2, s≠0. Set p=2s², so 0<p<1/2. For every compactly supported smooth complex test function φ,

    E |∫ φ(z) U_epsilon,alpha(z) d²z|² ≤ C_alpha,K epsilon^p ||φ||²_L²,       (3.1)

for 0<epsilon≤1 and support φ⊂K. In particular each test pairing converges to zero in mean square.

Proof, including the uniform estimate used. Proposition 23 of Dubédat, quoted in LITERATURE.md, gives for 0<s<1/2

    |E exp(2πis(h(f)−h(g)))| ∼ A_s |f−g|^(−p),   A_s=exp(2c(Λ,s))>0.

Negative s follows by complex conjugation. Equation (2.1) extends its modulus to m+s. For the fixed uniform square grid, the dimer law is invariant under all graph translations; the oriented height differences have at most finitely many starting-face parity types (a color-exchanging translation may reverse their sign). Hence the absolute correlator for all starting faces and all offsets has the bound

    |E exp(iα(h(f)−h(g)))| ≤ B_alpha (1+|f−g|)^(−p).                    (3.2)

To justify turning the asymptotic into this bound, fix one of the finitely many starting types. The asymptotic as |f−g|→∞ is in arbitrary direction, not just on one ray. It bounds the ratio by 2A_s outside some radius. Inside that radius there are finitely many offsets, and the characteristic function is bounded by 1. Increase B to handle these and the finitely many types. This relies on the printed large-distance proposition; it is not inferred from GFF convergence. Pinning does not enter any height difference.

If z∈Q_epsilon(f), w∈Q_epsilon(g), then |z−w|≤epsilon|f−g|+2sqrt(2)epsilon. Thus

    |E U_epsilon,alpha(z) overline(U_epsilon,alpha(w))|
        ≤ B'_alpha epsilon^p |z−w|^(−p)                              (3.3)

for z≠w, by increasing the constant; when z,w are in the same or neighboring cells the right hand side remains at least a fixed positive constant. On the diagonal use the bound 1.

Fubini applies because U has modulus 1 and φ is integrable. Expanding the square and applying (3.3) bounds its expectation by

    B'_alpha epsilon^p ∬ |φ(z)||φ(w)| |z−w|^(−p) d²z d²w.

Choose a disk of radius R>0 containing K. Set u=z−w and extend φ by zero. Cauchy–Schwarz gives ∫|φ(z)||φ(z−u)|d²z≤||φ||²_L². Only |u|≤2R contributes. Polar integration gives

    ∫_{|u|≤2R} |u|^(−p) d²u = 2π(2R)^(2−p)/(2−p)<∞.

This proves (3.1) with an explicit geometric factor. The diagonal has Lebesgue measure zero. QED.

### P2a: genuine distributional convergence and renormalized tightness
For every smooth compact cutoff χ and t>1,

    E ||χ U_epsilon,alpha||²_H^(−t) ≤ C_chi,alpha,t epsilon^p,          (3.4)

where a fixed enclosing square is viewed as a torus and χ is supported away from its boundary. Consequently the raw field tends to zero in probability in H^(−t)_loc, t>1.

Moreover V_epsilon,alpha=epsilon^(−s²)U_epsilon,alpha is tight locally in H^(−t) for every t>1. This is tightness only; the limit has not been identified and need not be asserted nonzero for aliased charges.

Proof. Let e_k be the normalized Fourier basis of the enclosing torus. Apply (3.1) to φ=χ overline(e_k). The support and L² norm are bounded independently of k. Therefore E|Fourier coefficient k of χU|²≤Cepsilon^p. By Tonelli,

    E||χU||²_H^(−t) ≤ Cepsilon^p ∑_{k∈Z²}(1+|k|²)^(−t).

The sum is finite for t>1: the shell n≤|k|<n+1 has O(n) lattice points, and ∑n^(1−2t) converges. This proves (3.4). Exhausting the plane by countably many cutoffs and using convergence for each proves convergence in the local Sobolev topology, for example with its standard bounded sum of cutoff seminorms.

For tightness of χV choose 1<u<t. The same computation gives a bound on E||χV||²_H^(−u) uniform in epsilon. Markov's inequality puts probability at least 1−δ in a ball of radius sqrt(C/δ) of H^(−u). Its closure in H^(−t) is compact: high Fourier modes have squared H^(−t) norm at most (1+N²)^(−(t−u)) times the squared H^(−u) norm, and the finitely many modes |k|≤N lie in a bounded finite-dimensional set. Thus balls are totally bounded and their H^(−t) closures are compact. A countable cutoff exhaustion, allocating failure probabilities δ2^(−j), proves local tightness. QED.

## 4. P3: all integer charges, deterministic special cases
For α=2πm, m∈Z, U_epsilon,alpha is deterministic. It converges distributionally to 1 if m is divisible by 4 and to 0 otherwise. This statement needs no Gibbs assumption, provided the same height sign, embedding and pinning are used.

Proof. P1 makes the field periodic on parity classes, with values

    1, i^m, (−i)^m, (−1)^m.

Its average on a 2×2 block is μ_m=(1+i^m+(−i)^m+(−1)^m)/4, equal to 1 for m≡0 mod4 and to 0 for the other three residues. If m≡0 mod4 the field is identically 1 because 4h is integer. Otherwise partition the plane into 2epsilon×2epsilon blocks. The integral of U−μ_m over every complete block is zero. In the test integral replace φ on each block by its value at one corner. The replacement error on a block is at most 2sup|U−μ_m|sqrt(2)epsilon sup|∇φ| times block area. Only blocks within O(epsilon) of the compact support can contribute; their total area is uniformly bounded for epsilon≤1. The resulting total error is O(epsilon), proving the limit. Smooth test functions extended by zero make this argument cover support-boundary blocks too. QED.

This is not a counterexample to Kenyon's question: it identifies lattice resonances that a full answer must include. Changing the additive height constant multiplies these observables by a fixed phase and changes their constant limit accordingly.

## 5. P4: exact finite determinant reduction, with full proof
Let G be a finite bipartite planar domino graph with at least one matching. Let K be a nonsingular bipartite Kasteleyn matrix for positive weights w_e, with the common determinant phase/sign furnished by Kasteleyn's enumeration theorem. For a dual path γ from f to g write

    h(g)−h(f)=D_gamma−∑_e a_e N_e,

where a_e is the algebraic signed number of path crossings of e and D_gamma=∑_e a_e/4, including the background contribution of boundary dual edges if present. Define K_alpha by replacing the entry for e by K_e exp(−iαa_e). Then exactly

    E exp(iα(h(g)−h(f))) = exp(iαD_gamma) det(K_alpha)/det(K).          (5.1)

Proof. The height increment formula summed along γ gives the displayed path identity; repeated or reversed crossings are included in a_e. In the determinant expansion, nonzero terms correspond to perfect matchings. Kasteleyn's sign condition means their coefficients are a common nonzero phase q times ∏_{e∈M}w_e. Multiplying entries by exp(−iαa_e) changes each term by exp(−iα∑_{e∈M}a_e) without changing this common phase. Hence det K_alpha=q∑_M w(M)exp(−iα∑a_e N_e), while det K=q∑_M w(M). Dividing cancels q, and multiplying by exp(iαD_gamma) proves (5.1). It holds even when det K_alpha vanishes. For different paths with the same endpoints, actual height closedness makes the expectation identical, so the phase-adjusted determinant ratio is path independent. QED.

The same determinant expansion proves the multipoint version with edge multiplier exp(−i∑_jα_j a_{j,e}). This is an exact finite reduction, not an asymptotic evaluation.

### Exhaustive finite checks
`finite_checks.py` enumerates every matching of 2×2, 2×4, 4×4, 4×6 and 6×6 rectangles: respectively 2, 5, 36, 281, 6728. It reconstructs H at every corner and checks all edge increments, closedness, configuration-independent residues mod4, determinant counts, (5.1) on two paths, and (2.1) for seven charges including α=π. The maximum determinant discrepancy was 8.972e−16; the maximum alias discrepancy was 2.221e−16. Enumeration is exact combinatorics, but exponentials and determinants are floating-point. These checks do not establish infinite-volume decay, rotational asymptotics, or a collision bound. Raw results are in `finite_checks.json`.

## 6. P5: a Gaussian collision bound proved algebraically
For distinct complex x₁,…,xₙ,y₁,…,yₙ with all x_i≠y_j, define

    F_p(x,y)= [∏_{i<j}|x_i−x_j||y_i−y_j| / ∏_{i,j}|x_i−y_j|]^p.

For 0<p≤1,

    F_p(x,y) ≤ ∑_{σ∈S_n} ∏_{i=1}^n |x_i−y_{σ(i)}|^(−p).            (6.1)

Proof of the algebraic identity used. Multiply det[(x_i−y_j)^(−1)] by Q=∏_{i,j}(x_i−y_j). Each term of the determinant expansion cancels n denominators and is a polynomial of total degree n²−n. The resulting polynomial is alternating separately in the x's and the y's, and vanishes whenever any two x's, or any two y's, agree. Each linear difference therefore divides it (polynomial division by that difference has zero remainder after substitution). These distinct linear irreducible factors are pairwise nonassociate and prime in the polynomial ring over C, so their product, the two Vandermonde polynomials, divides it. Their combined degree is n(n−1), the same as the numerator's degree, so the quotient is constant.

To determine the constant take x_i→y_i with y_i pairwise distinct. Multiplying the determinant by ∏_i(x_i−y_i) leaves limit 1: the identity permutation contributes 1 and every other permutation has at least one uncancelled vanishing diagonal factor. Q/∏_i(x_i−y_i) tends to ∏_{i≠j}(y_i−y_j)=(−1)^(n(n−1)/2)∏_{i<j}(y_j−y_i)². The product of the two Vandermonde polynomials tends to ∏_{i<j}(y_j−y_i)². Thus

    det[(x_i−y_j)^(−1)]
      = (−1)^(n(n−1)/2)∏_{i<j}(x_j−x_i)(y_j−y_i)/Q.

Taking absolute values gives F_p=|det C|^p. The determinant triangle inequality bounds |det C| by ∑_σ∏_i|x_i−y_{σ(i)}|^(−1). For nonnegative a_j, (∑a_j)^p≤∑a_j^p when 0<p≤1. For completeness, for 0<p<1 the derivative of (1+t)^p−1−t^p is p[(1+t)^(p−1)−t^(p−1)]≤0 for t>0, and its limit at zero is zero; scaling gives the two-term inequality, and induction gives the finite sum. For p=1 it is equality. This proves (6.1). Same-sign coincidences follow by continuity when cross distances are nonzero; cross coincidences can be interpreted with an infinite right hand side. QED.

The bound is locally integrable in all variables for p<2: each permutation pairs variables into disjoint two-variable factors, and ∫_{|u|≤R}|u|^(−p)d²u is finite. With test φ, integrating (6.1) against ∏|φ(x_i)φ(y_i)| yields at most n! I_phi^n, where I_phi=∬|φ(x)||φ(y)||x−y|^(−p)d²x d²y.

`cauchy_checks.py` checked the Cauchy identity in 60 exact rational cases n≤4, and (6.1) in 450 complex numerical cases n≤5 including opposite-charge distances down to 1e−8. `cauchy_checks.json` records these. This is a **Gaussian power-kernel** bound, not a bound on discrete dimer correlators.

## 7. P6: rigorous conditional reduction to a missing dimer estimate
Take a principal charge 0<|s|<1/2, α=2πs, p=2s², and a_s=exp(−c(Λ,|s|)). Let Θ be independent and uniform on [0,2π). Define

    W_epsilon(z)=e^(iΘ) a_s epsilon^(−s²) U_epsilon,alpha(z).

The independent phase is an explicit modification: it suppresses unbalanced moments. It is not automatically present in the pinned dimer field.

Here is a sufficient extra hypothesis, not proved in this attempt:

(MB) For each n and compact K there is C_n,K<∞, independent of epsilon and positions, such that for almost every x,y∈K^n,

    |E ∏_i W_epsilon(x_i) overline(W_epsilon(y_i))|
       ≤ C_n,K ∑_{σ∈S_n} ∏_i (|x_i−y_{σ(i)}|+epsilon)^(−p).          (7.1)

If (MB) holds, W_epsilon converges in law locally in H^(−t), t>1, to the phase-randomized imaginary Gaussian chaos with balanced correlation functions F_p. Thus the actual remaining dimer question is isolated in a uniform collision estimate and, for the original pinned field, control of its phase/unbalanced sector.

Complete proof of this implication. For distinct fixed macroscopic insertions, the lattice separations are epsilon^(−1) times the continuum separations plus O(1), so they are all mutually comparable. Theorem 24, exactly as printed, applies with n charges +s and n charges −s. The lattice product contributes epsilon^(2ns²), since ∑_{i<j}2s_i s_j=−∑_j s_j²=−2ns². This cancels epsilon^(−2ns²) in W, and a_s^(2n) cancels exp(2nc). Consequently the balanced correlation converges to F_p. Coinciding macroscopic configurations have measure zero.

For integrated moments, (7.1) is dominated by C_n,K times the locally integrable right hand side of (6.1), because (r+epsilon)^(−p)≤r^(−p). Dominated convergence proves convergence of every balanced mixed moment of test pairings. Unbalanced mixed moments are identically zero: integrating e^(i(k−l)Θ) gives zero when k≠l. Bounds with larger n also give uniform integrability when passing moments through subsequential laws.

The candidate exists. On a bounded support within {|z|<L}, a Gaussian field with covariance log(L/|z−w|) can be constructed as a Dirichlet GFF in that disk, in the convention Cov=log|1−z overline(w)/L²|−log(|z−w|/L), plus an independent harmonic Gaussian field with covariance −log|1−z overline(w)/L²|. The latter kernel is positive semidefinite by its series ∑_{k≥1} Re[(z overline(w)/L²)^k]/k, realized with independent sine and cosine Gaussian modes. The sum has the desired pure logarithmic covariance. On compact subsets its regular part is smooth. Junnila–Saksman–Webb Theorem 1.1 constructs μ=:exp(i sqrt(p)X): since sqrt(p)<sqrt(2). Set W=e^(iΘ)L^(−p/2)μ. The Gaussian exponential identity gives balanced moments F_p: the constant log L contributes L^(pn), canceled by L^(−pn) from this amplitude. Unbalanced moments vanish by Θ. Different sufficiently large disks give the same law on overlapping compact supports by the moment determination argument below, so this defines a consistent local field law.

For any test φ the candidate's moments satisfy E|W(φ)|^(2n)≤n! I_phi^n by (6.1). They are indeed given by integrating F_p; one may first use smooth Gaussian regularizations and pass to the limit using Gaussian-chaos moment convergence, as in the cited construction and moment results. These bounds imply an exponential moment for |W(φ)|² for sufficiently small positive parameter: expand exp(t|W(φ)|²) into its nonnegative series and use ∑t^n n! I_phi^n/n!<∞ when tI_phi<1. Therefore all real projections of this complex variable are moment-determinate. The same holds for arbitrary finite linear combinations of test pairings. Equality of their moments consequently identifies all finite-dimensional laws (or use the analytic moment-generating function near zero and uniqueness of characteristic functions).

P2a gives local tightness of W_epsilon. Any subsequential limit in H^(−t)_loc has, by the moment convergence and uniform integrability just established, the candidate's test-pairing moments. The preceding determination argument identifies its finite-dimensional test-pairing laws; a countable separating family of smooth tests generates the Borel sigma algebra of this separable local Sobolev space, and so identifies the distribution-valued law. All subsequential limits are the same, which proves convergence in law. QED, conditional on (MB).

## 8. Hostile-referee audit and remaining gaps
- **Height convention:** verified from Kenyon p.16 and Dubédat p.22. Using the integer H would replace α by 4α in every displayed range and exponent. Residue algebra was checked in Lean; finite tilings independently checked it.
- **Global additive phase:** fixed for P1–P3; phase-randomization in P6 is expressly additional. Neutral correlators alone cannot identify a pinned field's unbalanced sector.
- **Weak GFF convergence:** never used to exponentiate unsmoothed dimer heights. The Gaussian chaos theorem assumes Gaussian approximations and cannot supply the missing dimer estimate.
- **Uniformity of P2:** only requires fixed-grid two-point decay in arbitrary direction, translations with finitely many parity types, and finitely many remaining lattice offsets. It does not require higher-point coalescence estimates.
- **Coincidences:** P2 uses a two-dimensional integrable singularity with p<1/2. P6 requires (MB). The Gaussian bound P5 gives no transfer principle from a Gaussian field to dimers.
- **Endpoint:** α≡π mod2π, equivalently s=±1/2, is not covered by Proposition 23. Finite checks at α=π do not prove its infinite-volume limit. No analytic continuation or continuity in α uniform in separation has been asserted.
- **Large charges:** aliases preserve two-point moduli, not complex fields. P2a's tightness for aliased charges does not identify their renormalized limit.
- **Domain/slope:** nothing here proves bounded-domain, nonzero-slope or arbitrary Gibbs-measure statements.
- **Rotational invariance:** supplied in the two-point principal-charge range by the existing literature. The proof in this folder establishes additional distributional consequences, not a new proof of Dubédat's analytic asymptotics.
- **Formalization scope:** Lean checks only the stated integer path algebra. Imports are `Mathlib.Tactic.Ring` and `Lean.Elab.Tactic.Omega`; no `sorry` or `native_decide`. Final check exited 0, axioms only `propext` and `Quot.sound`. Initial BOM/import failures were corrected and are not called checked results.
- **Computation scope:** finite exact enumeration and Cauchy checks finish in seconds and stay well below 1 GB. Floating-point errors are verification, not exact proofs of analytic limits.

Final verdict: PARTIAL. Proved here: deterministic aliases/resonances, raw zero field limit and renormalized tightness in an explicit infinite-volume special case, the exact finite determinant formula, the Gaussian matching inequality, and the stated conditional convergence reduction. Not proved: (MB) for dimer correlators, the nontrivial renormalized law of the original pinned electric field, the half-integer charge endpoint, or a full answer for all settings left unspecified in Kenyon's question. The bounded literature search found no theorem meeting the user's exact-solution criterion.
''',encoding='utf8')
