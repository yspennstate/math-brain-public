# D0040 — research record, 2026-10-12

## Exact question and interpretation

Virág, *Operator limits of random matrices*, arXiv:1804.06953, PDF p. 6:
“Question 2 (Nested models). Can any other Dyson β-ensembles be coupled this way? How about other natural random matrix models?”
The preceding context, parameter conventions, and search results are recorded in LITERATURE.md. The source asks a broad question, not a classification theorem with specified auxiliary spectral weights. Here a strict nesting coupling means one random real symmetric tridiagonal array J whose leading n by n block has the specified eigenvalue law for every n. No self-adjoint infinite-operator assertion is needed. Dependence between entries is allowed.

## Proved special case: beta-Laguerre with fixed rectangularity

Fix β>0 and a>−1. Let all random variables below be independent, and set

    d_i = χ_{β(a+i)} / sqrt(β),   c_i = χ_{β i} / sqrt(β),  i≥1.

Here χ_r is defined for every real r>0 by χ_r² having gamma shape r/2 and scale 2. Define a lower bidiagonal infinite array B by B_{ii}=d_i and B_{i+1,i}=c_i. Define its symmetric tridiagonal Gram array J entrywise:

    J_{ii}=d_i²+c_{i−1}²,  c_0=0;
    J_{i,i+1}=J_{i+1,i}=d_i c_i.

**Theorem.** For each n≥1 the eigenvalues of the leading block J_n have density, on 0<λ_1<⋯<λ_n,

    Z_n^{-1} ∏_{i<j}(λ_j−λ_i)^β
       ∏_{i=1}^n λ_i^{β(a+1)/2−1} exp(−β λ_i/2).

All n use the same β, a and weight. These are strict tridiagonal leading minors. Their spectra strictly interlace almost surely.

**Proof.** Countably many independent chi variables exist on their product probability space. Every shape is positive, including β(a+1), so each d_i,c_i is finite and strictly positive almost surely, simultaneously. Because each row i of B has support only in columns i−1,i, the leading block of J equals B_n B_n^T exactly, with B_n the leading bidiagonal block. In particular no c_n² contaminates its final diagonal.

Let R_n be the reversal permutation matrix, and put L_n=R_n B_n^T R_n. Its diagonal entry i is d_{n+1−i}, with shape β(a+n+1−i); its subdiagonal entry (i+1,i) is c_{n−i}, with shape β(n−i). These entries are independent. With m=n+a, this is exactly the Dumitriu–Edelman Laguerre lower-bidiagonal factor, scaled by 1/sqrt(β): diagonal χ_{β(m−i+1)} and subdiagonal χ_{β(n−i)}. Their Laguerre spectral-density theorem applies because m>n−1, equivalently a>−1. Its exponent is β(m−n+1)/2−1=β(a+1)/2−1 and scaling divides eigenvalues by β, producing exp(−βλ/2).

Finally L_n L_n^T=R_n B_n^T B_n R_n. This has the same eigenvalues as B_n B_n^T: B_n is invertible and B_n^{-1}(B_n B_n^T)B_n=B_n^T B_n. Thus the quoted finite-size density is exactly the law of J_n. This proves the nesting claim for all n on the single product space.

For completeness strict interlacing follows from elementary characteristic-polynomial recurrence. Write p_k(x)=det(xI−J_k), p_0=1. Expansion of the last row gives p_{k+1}(x)=(x−J_{k+1,k+1})p_k(x)−J_{k,k+1}²p_{k−1}(x). At a root of p_k, p_{k+1} is the negative positive multiple of p_{k−1}. Starting with the one simple root of p_1, let r_1<⋯<r_k be the roots of p_k, and suppose p_{k−1} interlaces them. Since p_{k−1} is monic and has k−i roots above r_i, its sign at r_i is (−1)^{k−i}. Thus the sign of p_{k+1}(r_i) is (−1)^{k−i+1}, alternating across the r_i. There is one root of p_{k+1} between each consecutive pair. At r_1 its sign is (−1)^k, opposite the sign (−1)^{k+1} at negative infinity; at r_k it is negative, opposite its positive sign at positive infinity. Hence there is a further root on each exterior side. These k+1 distinct roots exhaust its degree. No common root can occur since the recurrence would force p_0=0. This proves strict interlacing. Positive definiteness follows from invertibility of B_n. ∎

The finite-size distribution theorem used here is a known theorem, not an asserted new proof of that theorem. This argument derives a nesting consequence from it. It is not a post-source paper explicitly solving Virág's question and is not SOLVED_IN_LITERATURE.

### The source's random-measure formulation also holds

The source's immediate context is Theorem 4.1, which asks for one random measure whose degree-n orthogonal polynomial zeros have the n-point ensemble law. The construction above satisfies this stronger formulation as well.

**Proof.** Let X have chi-square law with r degrees of freedom. Its moment generating function at 1/4 is 2^{r/2}, so Markov's inequality gives P(X>4r)≤exp(−r)2^{r/2}. For r=β(a+i) and r=βi these bounds are summable in i. Borel–Cantelli therefore implies, almost surely, that eventually d_i²≤4(a+i) and c_i²≤4i. In particular the Jacobi offdiagonal t_i=d_i c_i satisfies t_i≤C i for all sufficiently large i, with a finite constant C depending on a. Thus ∑_{i≥1}1/t_i=∞.

The standard Carleman criterion for Jacobi operators states that positive offdiagonals with this divergent reciprocal sum make the symmetric operator on finitely supported vectors essentially self-adjoint. Apply it pathwise to J. Its quadratic form on finitely supported x is ∑_{i≥1}(d_i x_i+c_i x_{i+1})²≥0, so its self-adjoint closure is nonnegative. Let μ be its spectral measure at e_1; it is a probability measure on [0,∞). Every J^k e_1 has finite support, hence belongs to the domain of J and has finite norm. The spectral theorem gives ∫x^{2k}dμ=||J^k e_1||²<∞. Positive offdiagonals imply that the span of e_1,J e_1,…,J^{k}e_1 equals the span of e_1,…,e_{k+1}, by induction on the nonzero coefficient ∏_{i=1}^{k}t_i at e_{k+1}. Therefore these polynomial vectors are linearly independent, and μ has infinite support.

The determinant recurrence above, with normalization by ∏_{i=1}^{n}t_i, constructs orthonormal polynomials P_n such that P_n(J)e_1=e_{n+1}. Their inner products under μ are exactly the inner products of e_{n+1}. Their zeros are those of det(xI−J_n). The finite-size theorem already proved identifies their laws as the fixed-weight beta-Laguerre laws. This proves the random-measure version. ∎

The resulting measure is measurable in the random entries. Indeed extend J_n to J_n⊕0 on the infinite Hilbert space. These bounded self-adjoint operators agree with J on every fixed finitely supported vector for all sufficiently large n. Finitely supported vectors are a core of the essentially self-adjoint closure, so the standard core criterion for strong resolvent convergence gives J_n⊕0→J. Their e_1 spectral measures, which are measurable functions of finite random matrices, converge weakly to μ by the spectral theorem for strong resolvent convergence. Thus μ is a random measure.

Carleman's operator criterion, the spectral theorem and its core convergence criterion are standard external results used with their hypotheses explicitly checked; they are not Lean-verified here.

### Boundary and scaling checks

For n=1, J_1=χ²_{β(a+1)}/β, exactly the claimed gamma density. For n=2,

    det(xI−J_2)=x²−(d_1²+d_2²+c_1²)x+d_1²d_2².

Hence det J_n=∏d_i², and E tr J_n=n(a+n). The latter follows by adding E d_i²=a+i and E c_i²=i. Its variance is 2n(a+n)/β because every square is independent. These are useful checks against the tempting incorrect Gram orientation. The limiting parameter a=−1 is excluded: d_1 would have zero shape and a zero eigenvalue, and the displayed density is nonintegrable at zero. Fixed m, rather than fixed m−n=a, is a different family and is not covered.

## Proved obstruction for the canonical quartic model only

Fix β>0. Consider the n=1 eigenvalue density proportional to exp(−βx⁴), and the n=2 beta density proportional to (λ_2−λ_1)^β exp(−β(λ_1⁴+λ_2⁴)). Choose first-coordinate spectral weight q independently with Beta(β/2,β/2) law, as in the standard tridiagonalization. Then this standard n=2 matrix cannot have its leading diagonal distributed as the standard n=1 matrix. This statement concerns these fixed matrix laws, not all tridiagonal representatives of the two eigenvalue laws.

**Full proof.** Write Δ=λ_2−λ_1>0 and h=sqrt(q(1−q)). The associated positive-offdiagonal symmetric matrix is [[u,b],[b,v]] where

    u=λ_2−qΔ, v=λ_1+qΔ, b=Δh.

This map is a bijection from λ_1<λ_2, 0<q<1 to u,v real, b>0: the inverse uses the two distinct eigenvalues and q=(λ_2−u)/Δ. Its absolute Jacobian is Δ/(2h). To verify, use s=(λ_1+λ_2)/2, t=Δ/2, z=1−2q; then u=s+tz, v=s−tz, b=t sqrt(1−z²). The determinant from (s,t,z) to (u,v,b) has absolute value 2t/sqrt(1−z²), while the determinant from (λ_1,λ_2,q) to (s,t,z) has absolute value 1. Substituting t=Δ/2 and sqrt(1−z²)=2h gives Δ/(2h).

Dividing the density Δ^β [q(1−q)]^{β/2−1} by this Jacobian gives a constant times b^{β−1} exp(−β tr T⁴), since b=Δh. Direct multiplication gives

    tr T⁴=u⁴+v⁴+4b²(u²+uv+v²)+2b⁴.

Consequently the marginal density of u is proportional to exp(−βu⁴) F(u), with

    F(u)=∫_{R}∫_0^∞ b^{β−1}
      exp[−β(v⁴+4b²(u²+uv+v²)+2b⁴)] db dv.

For every u, 0<F(u)<∞. Indeed u²+uv+v²≥0, and the integrable dominating function is b^{β−1}exp(−βv⁴−2βb⁴). Its integrability at b=0 uses β>0; at infinity both fourth powers ensure it. For fixed b>0 and v, u²+uv+v²=(v+u/2)²+3u²/4, so the integrand tends to zero as |u|→∞. Dominated convergence gives F(u)→0. The same domination proves continuity of F. F(0)>0. Thus F is not almost everywhere constant; if it were, continuity would make it constant everywhere, contrary to the limit and F(0)>0. Equality of the marginal with the n=1 density would require exactly that constant property. This is impossible. ∎

**What this does not prove.** Spectral weights need not be independent Dirichlet weights in an arbitrary nesting coupling. A different choice depending on eigenvalues might fix the first diagonal law. Thus this calculation does not disprove quartic nesting in Virág's broad sense. Nor does nonfactorization of entries, by itself, rule out consistency. The earlier intake argument claiming independence is necessary is invalid.

## Checks and remaining gap

### A checked interpretation of the earlier Favard reduction

For any three leading-minor spectra let p_k be their monic characteristic polynomials. Expansion of a tridiagonal determinant forces p_3=(x−h_3)p_2−t_2²p_1. Interlacing alone does not impose this identity. For instance, levels (0), (−1,1), (−2,1/2,2) strictly interlace. Their polynomials are p_1=x, p_2=x²−1, and p_3=x³−x²/2−4x+2. Matching the x² coefficient forces h_3=1/2. But p_3−(x−1/2)p_2=−3x+3/2 cannot be a scalar multiple of p_1. Thus no symmetric tridiagonal matrix realizes these three levels as leading spectra. This independently verifies the counterexample in the earlier origin/master Favard report; it is an interpretation check, not a counterexample to the existence of another coupling with the same level marginals.

### Canonical quartic tail check

The obstruction can be quantified: substitute b=t/|u| in F(u). For |u|→∞,

    |u|^β F(u) → [∫_R exp(−βv⁴)dv]
                     [∫_0^∞ t^{β−1}exp(−4βt²)dt] > 0.

Indeed the transformed integrand is t^{β−1}exp[−βv⁴−4βt²(1+v/u+v²/u²)−2βt⁴/u⁴]. The coefficient in parentheses is at least 3/4, so t^{β−1}exp(−βv⁴−3βt²) dominates it and is integrable. Pointwise convergence and dominated convergence give the displayed limit. This independently confirms the extra |u|^{−β} marginal tail factor.

Numerical and Lean verification records are to be appended after their commands return. The Lean file checks only the two-by-two polynomial identity, not the probability theorem. The numerical script compares spectra of the same sample before and after reversal/transposition, tests exact leading-block equality, strict interlacing, and trace means at four β,a pairs. Samples are evidence only.

The numerical run finished: 10,000 samples at n=5 for each (β,a)=(0.3,−0.8),(1,0),(2,2),(4,0.5). Maximum spectral discrepancy was 2.85×10^{−14}. All leading-block equality assertions passed. The minimum reported interlacing gap was −7.11×10^{−15} in the small-shape case, a floating-point precision limitation, not a verified violation. Trace-mean deviations were 1.952, −0.034, 0.981 and 1.155 theoretical standard errors. Numerical evidence does not establish the full density; that follows from Theorem 3.4 and the exact transformation.

Hostile-referee checklist:

1. Wrong Hermite orientation or normalization: source reversal and √n factor explicitly checked on PDF pp. 2–5.
2. Wrong Laguerre Gram orientation: leading block equality is exact only for B_n B_n^T with B lower bidiagonal as defined. The proof compares its law through R_n B_n^T R_n, not through R_n B_n R_n.
3. Size-dependent hard-edge exponent: DE parameter substitution is explicit; exponent stays β(a+1)/2−1, whereas rectangular m=n+a changes with n.
4. Nonintegrable boundary shapes: every shape is positive precisely for β>0,a>−1; a=−1 is excluded and explained.
5. Mistaking sample agreement for density equality: the density rests on DE Theorem 3.4, not the simulation.
6. Infinite-operator ambiguity: Carleman's condition, moment finiteness, nonnegativity, cyclicity and measurable spectral-measure construction are checked.
7. Overstating the quartic obstruction: its independent Dirichlet-weight assumption is explicit; arbitrary spectral weights remain allowed in the open question.
8. Mistaking corners interlacing for nesting: the three-level recurrence counterexample is written out.
9. Independence claimed necessary: this is false. For a concrete counterexample take J_{ii}=Z for all i, with a nonconstant random Z, and J_{i,i+1}=1. Its minors nest exactly although all diagonal entries are perfectly dependent. This does not give Dyson marginal laws; it refutes only the claimed necessary mechanism.
10. Literature overclaim: rate-limited citation searches are recorded as incomplete, and no abstract or related-model theorem is called a solution.

Remaining gap: determine which other fixed-weight Dyson beta-ensemble families possess an arbitrary tridiagonal leading-minor coupling (without prescribing spectral weights), and provide a classification or a genuine impossibility theorem. The Laguerre example and the canonical quartic obstruction do not fill this gap. Generalized matrix pencils and circular CMV truncations are different objects and cannot silently be substituted for tridiagonal Hermitian minors.

Final bounded-attempt verdict: PARTIAL. No complete answer to the general question and no verified literature resolution is claimed. The Lean file contains two finite algebraic formalizations, but the shared-machine check has not returned, so neither is reported as Lean-checked. See VERIFICATION.md for its command and recoverable session.

## Renewed attempt: stronger Jacobi family result

At the user's request, two previously untried approaches were recorded and the CS-angle construction was pursued. SECOND_ATTEMPT.md now contains a full proof that every fixed-weight beta-Jacobi ensemble, for β>0 and all endpoint powers α,δ>−1, admits one bounded Jacobi operator and one common random orthogonality measure. The proof uses the complementary CS block B_22 from Edelman–Sutton Theorem 4.1 (author PDF p. 17), rather than assuming the usual B_11 Gram orientation nests. The exact identity I_n−J_n=C_n C_n^T and the full mixed determinant-moment formula provide independent checks. The uniform hard-wall Dyson ensemble is an explicit corollary.

This strengthens the previous special-case result. It still leaves arbitrary spectral-weight nesting for nonclassical full-real-line potentials, especially the quartic weight, unresolved. The verdict for broad D0040 remains PARTIAL; see SECOND_ATTEMPT.md for the complete proof, referee audit, and updated verification status.
