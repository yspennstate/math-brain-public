# Scaling and a tractable independent-coefficient model

## The regular mechanism and the exact T_n

KRV use eigenvalue density Z^(-1)exp(−nβΣV(λ_i))|Δ(λ)|^β. Independently assign Dirichlet(β/2,…,β/2) masses to the eigenvalues and take the Jacobi matrix whose spectral measure at e₁ is that random measure. In entries A_i∈R, B_i>0 its joint density with respect to dA dB is

Z^(-1) exp(−nβ tr V(T)) ∏_{i=1}^{n−1}B_i^{β(n−i)−1}.

This is KRV Section 2, PDF pp. 6–8, especially equation (8). Apart from a quadratic V these entries are dependent. The trace path expansion gives a finite-range Markov field for polynomial V, of range controlled by deg V. Independence must not be substituted into this target.

Write W_V(a,b)=[z⁰]V(a+b(z+z^(−1))). Local constant minimizers (a†(x),b†(x)) minimize W_V(a,b)−(1−x)log b (KRV equations (10)–(14), PDF p. 9). Their local right edge is E(x)=a†(x)+2b†(x), with E=E(0), b₀=b†(0)>0. In the uniformly convex regular case these minimizers are analytic, E′(0)<0, and the finite-range chain concentrates and mixes. After deleting an initial O(log n) region, KRV prove a Gaussian approximation and a functional CLT for the integrated centered row sums. The initial region is treated by a rank-one boundary correction; this is a substantive part of the proof, not automatic deletion of coordinates.

If m_n∼n^(1/3), then, schematically,

Y_n(t)=(m_n/b₀) Σ_{j≤m_nt}(E−A_j−2B_j)

converges to t²/2+(2/√β)B(t), after constants are chosen. A/B terms at neighboring sites can be assigned to the two integrated potentials in KRV Section 4.1. Positivity/growth of their deterministic parts and uniform bounds on unit-interval oscillations of their centered parts prevent spectral mass from escaping to infinity. These conditions, with convergence of integrated potentials, are KRV Assumptions 1–2, equations (21)–(25), PDF p. 14. KRV Theorem 9(i), same page, gives joint ordered eigenvalue and embedded-eigenfunction convergence with Dirichlet boundary. It imports RRV Theorem 5.1 (saved RRV preprint PDF p. 21). The boundary extension is BV Theorem 2.10. KRV Theorem 1, PDF p. 3, applies this to uniformly convex polynomial V and obtains the SAO. Its piecewise constant embedding has mesh m_n^(−1).

## Critical exponents: what the formal argument does and does not prove

Put p=1/(2k+1), a=k/(2k+1). An edge density ρ(E−u)∼C u^(2k+1/2) places O(n δ^(2k+3/2)) particles in a δ-neighborhood. An order-one count requires δ_n∼n^(−2/(4k+3)). This is an independent derivation of the eigenvalue scale.

The local deterministic edge profile obeys E−E(x)∼c x^p in KRV equation (73), PDF p. 56. Under the extra assumption that the entries follow this profile sufficiently accurately, balancing the scaled second difference with the drift requires

(m_n²/b₀)c(m_n/n)^p∼1,

so

m_n=(b₀/c)^(1/(2+p))n^(1/(4k+3)),

H_n=(m_n²/b₀)(EI−T_n),

γ=c^(−2/(2+p))b₀^(−p/(2+p))

in H_n=γn^(2/(4k+3))(EI−T_n). Thus the mesh is n^(−1/(4k+3)), the matrix eigenvalue magnification n^(2/(4k+3)), and the limiting deterministic potential is t^p. The integrated drift is t^(p+1)/(p+1). These calculations use the coefficient b₀ of the second difference and agree with the particle-count exponent.

For the explicit quartic U in PROOF.md, use V=U/2. Its local stationarity equations are

0=(a³+6ab²−4a²−8b²+2a+8)/10,

1−x=b²(3a²+3b²−8a+2)/5.

Write the right edge as a+2b=2−D and the left edge as a−2b=−2+L. The first equation gives L=5D³/128+O(D⁴), by the implicit function theorem (its L derivative is4/5 at zero); substitution into the second gives x=D³/8+O(D⁴). Hence b₀=1, c=2, and the formal drift normalization is γ=2^(−6/7). Numerical comparisons use this explicit constant, not a fit to sampled eigenvalues. This remains a formal normalization of an excluded operator limit.

KRV's displayed γ=c^(−2/3)(E/2)^(−1/3) in Conjecture 45, PDF p. 57, uses the regular-case powers; applying the preceding balance to general p gives the powers just derived (after shifting so E/2=b₀). The counterexample is independent of this constant issue: it excludes every fixed positive γ.

Suppose additionally that the *effective long-run variance* of a row-sum fluctuation has order n^(−1)(j/n)^(−2a). This means variance per site after summing covariances, not merely the variance of an individual entry. Then

Var[(m_n/b₀)Σ_{j≤m_nt}(row-sum fluctuation)]
  ∼const · m_n³ n^(−1)(m_n/n)^(−2a) ∫₀ᵗu^(−2a)du.

Since 3−2a=2+p and 1−2a=p, the n exponent vanishes at the above m_n. The limit is a Gaussian martingale with variance density proportional to t^(−2a); its distributional derivative has weight t^(−a). This derives the conjectured powers **conditionally**. Neither that variance assumption nor Gaussianity follows from the equilibrium density.

There is also a constant warning. In the regular case KRV Proposition 41, PDF p. 49, equation (68), identifies σ²=4b₀(−E′(0))/β before normalizing. If one formally extends the local susceptibility rule to E′(x)∼−cp x^(p−1), the normalized variance clock becomes (4/β)t^p. Its derivative gives noise coefficient (2√p/√β)t^(−a), whereas the displayed conjecture has 2/√β and variance clock (4/(βp))t^p. This extension is not a theorem at the critical point. In any event a constant correction cannot cure the tail contradiction in PROOF.md.

The correct conclusion is therefore: the scaling powers and deterministic drift survive the dimensional calculation; the proposed additive Gaussian limit does not survive the known β=2 spectral law. A critical CLT, including the boundary region, cannot be inferred by copying the k=0 proof.

## A class for which the displayed operator really is the limit

**Theorem 4 (artificial critical profile).** Fix k≥0, β>0, p=1/(2k+1), h_n=n^(−1/(4k+3)), and let ξ_j be independent standardized centered χ₁ variables,

ξ_j=(|Z_j|−√(2/π))/√(1−2/π),   Z_j∼N(0,1).

Define independent increments

ΔW_{n,j}=(2/√β)[(((jh_n)^p−((j−1)h_n)^p)/p)]^(1/2)ξ_j,

and the n×n matrix H_n with off-diagonals −h_n^(−2) and diagonal

2h_n^(−2)+(jh_n)^p+ΔW_{n,j}/h_n.

Its ordered low eigenvalues and step-function eigenvectors converge in the KRV Theorem 9(i) sense to those of Sβ,k. The same conclusion holds with independent standard Gaussian ξ_j. Equivalently the artificial Jacobi matrix T_n^art=2I−h_n²H_n has off-diagonal 1, deterministic diagonal −(j/n)^p and independent centered χ noise. This artificial model does not have the polynomial-potential β-ensemble eigenvalue density.

**Proof.** Set m_n=1/h_n, y_{n,2}=0 and

y_{n,1,j}=Σ_{ℓ≤j}[h_n(ℓh_n)^p+ΔW_{n,ℓ}].

Then H_n has exactly the form in KRV Section 4.1, PDF p. 13. We verify both assumptions, including their global requirements.

The deterministic part converges uniformly on compact intervals to ∫₀ᵗu^pdu. The centered increments have variance

v_{n,j}=(4/β)(((jh_n)^p−((j−1)h_n)^p)/p),

so their cumulative variance tends uniformly to r(t)=(4/(βp))t^p. The largest increment variance on a fixed compact interval is O(h_n^p), tending to zero. The fourth moments are bounded by a constant times v_{n,j}², and hence their sum is O(h_n^p). The Lindeberg condition follows from E[X²1{|X|>ε}]≤ε^(−2)E[X⁴]. Expansion of the characteristic functions, with the maximum variance tending to zero, shows that sums over finitely many disjoint time intervals converge jointly to independent normal variables with variances given by increments of r.

Here is a direct tightness check. A centered standardized χ₁ variable is uniformly sub-Gaussian: its moment generating function is obtained from E exp(t|Z|)=2 exp(t²/2)Φ(t), and the logarithm of its centered mgf divided by t² extends continuously at 0 and is bounded on R, using the Gaussian tail asymptotics at −∞. Thus E exp(tΔW_{n,j})≤exp(Ct²v_{n,j}). Products and the exponential supermartingale maximal inequality imply

P(maximum partial-sum deviation in a block with total variance ≤δ >u) ≤2exp(−u²/(Cδ)).

Partition a compact interval in the variance clock r into O(1/δ) consecutive blocks, each with total discrete variance at most δ+max_jv_{n,j}. The union bound for the displayed inequality tends to zero as δ↓0 for each fixed u>0, uniformly for n sufficiently large. Since r is uniformly continuous and strictly increasing, this proves tightness after composing back to t. It also controls jumps. Therefore the centered processes converge locally to W(t)=(2/√β)∫₀ᵗu^(−a)dB(u), whose covariance is r(min(s,t)). This proves KRV Assumption 1.

For Assumption 2 take η_{n,1,j}=(jh_n)^p, η_{n,2}=0, and w_{n,1,j}=Σ_{ℓ≤j}ΔW_{n,ℓ}. Write η(t)=(1+t)^p and ζ(t)=(1+t)^(p/2). The drift inequalities (23)–(24) hold with a fixed sufficiently large constant, since on a cell η_{n,1} differs from t^p by O(h_n^p), and η_{n,2}=0.

The total variance of increments whose endpoints lie in [J−1,J+2] is at most C(1+J)^(−2a) for integers J≥2, uniformly over all n (h_n≤1). It is bounded by C for J=0,1. The same maximal inequality gives for the oscillation M_{n,J} of the step process on that interval

P(M_{n,J}²>u(1+J)^(p/2)) ≤C exp(−c u(1+J)^(2a+p/2)).

The sum over J≥0 tends to zero as u→∞, because 2a+p/2>0. Consequently κ_n=1+sup_J M_{n,J}²/(1+J)^(p/2), enlarged by a fixed constant for the drift, is tight uniformly in n. Every pair x,ξ with |x−ξ|≤1 is covered by one such enlarged block, and therefore (25) holds with this κ_n and η/ζ=(1+t)^(p/2). Blocks are considered only within the finite matrix interval; the same estimate with partial end blocks applies. Thus KRV Assumption 2 holds globally. Also m_n→∞ and m_n=o(n).

KRV Theorem 9(i) now proves the claimed convergence, with Dirichlet boundary at zero and the standard √m_n step-function embedding. Gaussian increments obey the same inequalities with their exact mgf, giving the second case. ∎

This theorem validates an artificial discretization of the conjectured operator for all fixed k,β. It does not validate that operator as the limit of the genuine critical β-ensemble.
