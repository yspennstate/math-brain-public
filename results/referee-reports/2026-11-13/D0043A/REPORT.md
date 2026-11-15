COUNTEREXAMPLE

# D0043: the displayed exotic-edge operator is already disproved

The conjecture fails for k=1, β=2. This is a known result: Jnaneshwar Baslingker, *Stochastic domination in beta ensembles*, J. Math. Phys. 66, 053303 (2025), DOI [10.1063/5.0254593](https://doi.org/10.1063/5.0254593), **Theorem 4 in [arXiv:2304.09236v2](https://arxiv.org/abs/2304.09236v2), PDF p. 7**, with proof on pp. 10–12. The theorem number and pages here are verified against the saved arXiv text; the journal abstract confirms the result, but the journal PDF was inaccessible. No new resolution is claimed.

The obstruction is in the right tail. The displayed Gaussian operator gives P(−λ₀>s)≥exp(−Cs^(7/6)), while the critical unitary quartic kernel forces any largest-eigenvalue limit to have P(X>s)≤Cexp(−cs^(7/2)). Fixed positive rescaling cannot reconcile these powers. We give complete proofs of the operator construction and contradiction, explain what survives the formal scaling argument, and prove convergence of an artificial independent-chi model to this operator. Numerical comparisons are evidence only.

## Exact statement and meaning

Virág, *Operator limits of random matrices*, [arXiv:1804.06953](https://arxiv.org/abs/1804.06953), PDF p.14, states exactly:

> **Conjecture 5.** After scaling, T_n converges to the random operator
>
> $S_{\beta,k}=-\partial_t^2+t^{1/(2k+1)}+\frac{2}{\sqrt\beta}t^{-k/(2k+1)}b'_t.$

Here T_n is the KRV random Jacobi matrix of a polynomial-potential β-ensemble with independent Dirichlet spectral weights. KRV's more precise formulation is Conjecture45 in the saved arXiv version, PDF p.57 (published numbering13.1). It stipulates the half-line, Dirichlet boundary and Theorem9(i) convergence: the ordered low eigenvalues and embedded eigenvectors of the scaled EI−T_n converge jointly. This entails convergence of the scaled largest matrix eigenvalue to −λ₀ of the proposed operator. The explicit counterexample below uses the confining quartic U with V=U/2 in KRV's convention; it has one-cut equilibrium density vanishing to order5/2 at its right edge.

The status is COUNTEREXAMPLE rather than RESOLVED_IN_LITERATURE because the stipulated positive-theorem early-stop condition is not met: the printed theorem disproves the proposed limit. The correct general critical-edge random operator is not identified here. The certified negative scope is k=1,β=2; no classification for all k or β is claimed.



# Counterexample audit: the proposed Gaussian operator has the wrong tail

The arguments here concern the literal half-line Dirichlet operator in Virág's Conjecture 5. They do not construct the correct critical-edge random operator. All page numbers refer to the saved arXiv text versions.

**Prior literature.** This counterexample was already proved by Jnaneshwar Baslingker, *Stochastic domination in beta ensembles*, Journal of Mathematical Physics **66**, 053303 (2025), DOI 10.1063/5.0254593; arXiv:2304.09236v2 (22 December 2024), **Theorem 4, PDF p. 7**, proof in Section 3, PDF pp. 10–12. In particular equation (22), PDF p. 12, is precisely the exponent in Theorem 2 below. The derivation below was written during this audit before that paper was located; it is a verification and exposition of a known obstruction, not a claim of a new refutation. Our local expected-count argument spells out why compact kernel convergence alone suffices.

## 1. Construction of the proposed operator

Fix an integer k≥0 and β>0. Put p=1/(2k+1), a=k/(2k+1), σ=2/√β, and

W(t)=σ∫₀ᵗu^(−a)dB(u).

Since 2a<1, this is a continuous Gaussian martingale on [0,∞), with variance σ²t^p/p. Its distributional derivative is exactly σt^(−a)B′(t), not the derivative of t^(−a)B(t).

Let D be the real or complex functions f∈H¹₀(0,∞) with ∫t^p|f|²<∞. On compactly supported members of D define

q(f)=∫(|f′|²+t^p|f|²)dt−∫W(t)(|f(t)|²)′dt.

Here H¹₀ means zero trace at 0; no additional condition is imposed at infinity.

**Lemma 1.** Almost surely, for every ε>0 there is a finite Cε such that

|−∫W(|f|²)′| ≤ ε∫(|f′|²+t^p|f|²)+Cε∫|f|².

**Proof.** For integer j≥1, let Mj be the oscillation of W on [j,j+1]. The quadratic variation of this increment process is at most σ²j^(−2a). The exponential martingale inequality gives

P(Mj>r)≤4 exp(−c r²j^(2a)),

with a deterministic c>0; the unimportant factor 4 also covers oscillation rather than deviation from the left endpoint. Borel–Cantelli, with r=Cj^(−a)√log(j+2) and a sufficiently large deterministic C, implies Mj=O(j^(−a)√log(j+2)) almost surely. M0 is finite by continuity.

Let A interpolate W linearly at the nonnegative integers and put R=W−A. On [j,j+1], |A′|≤Mj and |R|≤2Mj, and R vanishes at both endpoints. Integration by parts block by block gives

−∫W(|f|²)′=∫A′|f|²−∫R(|f|²)′.

Its absolute value is at most ∫m|f|²+4∫m|f||f′|, where m(t)=Mj on block j. Young's inequality bounds this by

δ∫|f′|²+∫(m+4m²/δ)|f|².

For every δ>0, m+4m²/δ=o(t^p) as t→∞: for a=0 it is O(log t), and for a>0 it even tends to zero. On bounded intervals it is bounded. Choose δ and then the tail cutoff to give the asserted ε inequality. This also proves that the block expression extends continuously to all f∈D. Polarization gives the associated sesquilinear form. ∎

**Theorem 1.** q defines, almost surely, a canonical self-adjoint Dirichlet operator Sβ,k, bounded below, with compact resolvent and simple discrete eigenvalues tending to +∞.

**Proof.** The deterministic form q0(f)=∫(|f′|²+t^p|f|²) is closed on D, which is complete in q0+‖·‖². Smooth compactly supported functions in (0,∞) form a core: first cut off at large t and near 0, and then mollify; the standard H¹₀ approximation and locally bounded weight give convergence in this norm. Lemma 1 makes the noise an infinitesimally q0-bounded symmetric form. The closed-form perturbation theorem gives closedness, semiboundedness and a unique associated self-adjoint operator. Equivalently, choosing ε<1/2 in Lemma 1 shows directly that q+C‖·‖² is an equivalent positive complete form norm.

The embedding D→L² is compact. A bounded sequence in D has, on each finite interval, an L²-convergent subsequence by the one-dimensional Rellich theorem, and its mass beyond R is at most R^(−p) times its bounded weighted norm. A diagonal subsequence is therefore Cauchy in L² on the whole half-line. The resolvent maps bounded L² sets into bounded form-norm sets, so it is compact. The spectral theorem yields the stated discrete spectrum; the space is infinite dimensional, hence infinitely many eigenvalues.

For simplicity one may use the quasi-derivative g=f′−Wf. The distributional eigenvalue equation is equivalent locally to

f′=Wf+g,    g′=(t^p−λ−W²)f−Wg.

These coefficients are continuous, including at 0. Solutions are determined by (f(0),g(0)). A weak eigenfunction has this regularity: the distributional derivative of f′−Wf equals the locally integrable expression above, hence that quasi-derivative is absolutely continuous. Since f(0)=0, the space of such solutions for fixed λ is at most one dimensional. Self-adjointness excludes higher algebraic multiplicity. ∎

For deterministic f the noise form is the ordinary Gaussian stochastic integral σ∫t^(−a)|f|²dB, by integration by parts, first for smooth functions and then by approximation.

## 2. A lower bound on the upper-eigenvalue tail

**Theorem 2.** For every fixed k≥0, β>0 there are C,s₀∈(0,∞) such that, for all s≥s₀,

P(−λ₀(Sβ,k)>s) ≥ exp(−C s^r),    r=3/2−a=(4k+3)/(4k+2).

**Proof.** Set g(x)=√30 x(1−x) on [0,1] and zero elsewhere. This belongs to H¹₀ and has norm one. Define

f_s(t)=s^(1/4)g(√s t).

Then ‖f_s‖₂=1, ∫|f_s′|²=As with A=10, and ∫t^p|f_s|²=Ds^(−p/2), where D=∫₀¹x^pg²dx>0. The Gaussian part of q(f_s) has variance

σ²∫t^(−2a)f_s⁴dt = σ²C_a s^((1+2a)/2),

where C_a=∫₀¹x^(−2a)g⁴dx=900 B(5−2a,5)>0. Thus

P(q(f_s)<−s)=Φ(−z_s),

z_s=((1+A)s+Ds^(−p/2))/(σ√C_a s^((1+2a)/4)).

For s≥1, 0<z_s≤C₁s^((3−2a)/4). The Gaussian Mills lower bound, or integration of the Gaussian density over [z_s,z_s+1/z_s] once z_s≥1, implies Φ(−z_s)≥exp(−C₂s^((3−2a)/2)) for sufficiently large s. By the variational principle λ₀≤q(f_s), proving the claim. ∎

An independent weaker check avoids the singular endpoint completely. Center a unit-norm bump of width s^(−1/2) at t=1. Its kinetic energy is O(s), its deterministic potential energy O(1), and its Gaussian variance is comparable to s^(1/2). This already gives P(−λ₀>s)≥exp(−Cs^(3/2)). Even that weaker bound contradicts the critical unitary tail below. The singular-endpoint calculation sharpens it to 7/6 for k=1.

## 3. The critical quartic ensemble and a printed theorem

Use the unitary convention with eigenvalue density proportional to

exp(−nΣU(λ_i)) ∏_{i<j}(λ_i−λ_j)²,

where

U(x)=x⁴/20−4x³/15+x²/5+8x/5.

Its equilibrium measure is supported on [−2,2], with

ρ(x)=(x+2)^(1/2)(2−x)^(5/2)/(10π).

This is Claeys–Vanlessen, arXiv:math-ph/0607043, Example 1.2, PDF p. 5, equations (1.28)–(1.29), and CIK Example 1.2, PDF p. 2. The local KRV potential for this ensemble is V=U/2, because KRV uses exp(−nβΣV).

For completeness the equilibrium formula can be checked without assuming it: its mass is one; its Stieltjes transform is

G(z)=½[U′(z)−(z−2)²√(z²−4)/5],

with √(z²−4)∼z at infinity. It has G(z)=1/z+O(z^(−2)) and the asserted jump. The derivative of the effective potential U−2∫log|x−y|ρ(y)dy outside [−2,2] is (x−2)²√(x²−4)/5, using that branch. It is nonnegative to the right and nonpositive to the left. On the interval its derivative vanishes. Consequently the equilibrium variational equalities and inequalities hold. The leading coefficient of U is positive, ensuring confinement.

Claeys–Vanlessen **Theorem 1.7**, PDF pp. 6–7, equations (1.30)–(1.34), gives, at deformation parameters s=t=0,

(c n^(2/7))^(−1) K_n(2+u/(c n^(2/7)),2+v/(c n^(2/7))) → K_crit(u,v),

uniformly for u,v in compact subsets of R. Here c=6^(2/7)>0, from h₀(x)=(x−2)²/5 in their equation (1.24). Their Assumptions 1.1 hold by their Example 1.2; set both deformation parameters identically zero.

For this kernel there are c₀,C₀,s₀>0 with

∫_s^∞K_crit(u,u)du ≤ C₀ exp(−c₀s^(7/2)),    s≥s₀.       (T)

There are two ways to verify (T). CIK equations (1.23)–(1.24), PDF p. 5, give the kernel and Fredholm right-tail bounds for the same critical kernel, up to a fixed positive rescaling. Alternatively stay entirely in Claeys–Vanlessen's normalization: equation (1.20), PDF p. 4, and the RH expansion in Section 3.6 give Φ₁(u)=O(u^(−1/4)e^(−θ(u))), Φ₂(u)=O(u^(1/4)e^(−θ(u))), with θ(u)=u^(7/2)/105 at s=t=0. Their Lax equation (1.15) and polynomial matrix (1.16)–(1.17) bound the derivatives by a fixed polynomial times e^(−θ). Taking the diagonal limit in their kernel formula (1.34) therefore bounds |K_crit(u,u)| by C(1+u)^M exp(−2u^(7/2)/105). Integration and absorption of the polynomial give (T). The real-axis boundary version follows from the sectorially uniform RH expansion; CIK (1.23) states the real-variable kernel bound explicitly. Nonnegativity of the diagonal also follows from local uniform convergence of the nonnegative finite-n diagonals.

## 4. Contradiction without any Fredholm-convergence assumption

**Theorem 3.** For this quartic ensemble, no fixed positive edge-scaling constant can make its largest eigenvalue converge in distribution to −λ₀(S₂,₁). In particular the operator convergence in Virág's Conjecture 5 and KRV's Conjecture 45 is false for k=1, β=2, with the displayed Gaussian operator and the stipulated Dirichlet boundary.

**Proof.** First use the Claeys–Vanlessen scale and write X_n=c n^(2/7)(λ_max(T_n)−2). Suppose X_n converges to a finite random variable X. For any finite interval (s,R),

P(X_n∈(s,R)) ≤ E[# {i: c n^(2/7)(λ_i(T_n)−2)∈(s,R)}].

The right-hand side is the integral over (s,R) of the rescaled diagonal kernel, and converges by Theorem 1.7 to ∫_s^R K_crit(u,u)du. The portmanteau inequality for the open interval gives

P(X∈(s,R)) ≤ liminf P(X_n∈(s,R)) ≤ ∫_s^R K_crit(u,u)du.

Let R→∞. Since X is finite almost surely, (T) implies P(X>s)≤C₀exp(−c₀s^(7/2)). No convergence of Fredholm determinants, tightness of the full point process, or exchange of n→∞ with an unbounded integral has been assumed.

If a different fixed positive scaling γn^(2/7) gave limit −λ₀(S₂,₁), then in the scale above X would have law −(c/γ)λ₀(S₂,₁). Theorem 2 gives its upper tail at least exp(−C s^(7/6)), whereas the preceding inequality gives at most C₀exp(−c₀s^(7/2)). These inequalities are incompatible as s→∞. Norm-resolvent convergence in the intended ordered-eigenvalue sense would imply this excluded largest-eigenvalue convergence. ∎

Fixed deterministic additive shifts also cannot remove the mismatch. Replacing 2/√β by any nonzero constant cannot remove it. More generally, a nonzero additive Gaussian potential on any fixed interior interval already has the s^(3/2) lower-tail obstruction described above. Merely adjusting the displayed power or constant in the noise does not repair the conjecture in this Gaussian Schrödinger class.

The theorem above establishes a counterexample for k=1, β=2 only. Theorem 2 holds for all k,β, and yields the same contradiction at any higher k for which the corresponding unitary local kernel convergence and exp(−c s^((4k+3)/2)) bound are established. No such extra literature assumption is needed for the explicit k=1 counterexample.


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


# Numerical evidence and checks

The proof is independent of these computations. Random seeds and numerical settings are in the code; individual eigenvalues and diagnostics are in data/. All calculations ran at inherited nice10 with one numerical thread, below4GB. The largest recorded RSS among the experiment processes was204MB; the spectral/HMC runs used at most142MB. No dense n×n matrix was used for n=10000 or100000. Tridiagonal bisection computes the first three eigenvalues in linear storage; a sparse shift-invert calculation independently checked an artificial sample.

## Independent critical profile and operator discretization

The artificial matrices in SCALING.md use standardized centered χ₁ diagonal noise and exact integrated variance in each cell. There are96 independent samples at each β,n. The operator discretization uses Gaussian increments with that same exact cell variance, not a singular point evaluation at t=0. Meshes h=.025 and.0125 span length128. Entries below are sample means of −λ₀, followed by sample standard deviations in parentheses. These are Monte Carlo summaries, not exact limiting means.

| β | χ profile n=10000 | χ profile n=100000 | Gaussian h=.025 | Gaussian h=.0125 |
|---|---:|---:|---:|---:|
| 1 | -0.6915 (0.6420) | -0.4965 (0.7312) | -0.5651 (0.7902) | -0.5148 (0.8400) |
| 2 | -1.1701 (0.3919) | -1.0988 (0.4735) | -0.9884 (0.5454) | -1.0869 (0.5377) |
| 4 | -1.2763 (0.3196) | -1.3215 (0.3518) | -1.3124 (0.3418) | -1.3197 (0.3670) |

A separate96-sample coupled-Brownian refinement check aggregates pairs of fine increments to build the coarse mesh. The root-mean-square changes in the ground eigenvalue from h=.025 to.0125 were β=1: 0.01342, β=2: 0.01649, β=4: 0.00443. Restricting the same paths from length128 to64 changed the first three eigenvalues by at most 4.9e-12. This last number is an observed finite-sample boundary check at numerical precision, not a uniform probabilistic bound. The deterministic mesh/boundary check is also saved.

## Genuine critical quartic

The target is exactly the KRV entry density with V=U/2, U=x⁴/20−4x³/15+x²/5+8x/5. In q_i=log b_i coordinates its negative log density is nβ trU(T)/2−βΣ(n−i)q_i; the Jacobian is included. Metropolis-corrected HMC updates all2n−1 entry variables. A fixed pentadiagonal Hessian mass at the finite-n mode accounts for the coefficient correlations. Cholesky factors and triangular solves use linear storage. The mass matrix is fixed throughout a chain; its use does not approximate the target. At each n=256,1000,10000 and β=1,2,4, two chains used300 warm-up trajectories, then400 retained draws per chain, thinning2. Step-size adaptation ends before retained sampling. Last sampled a,b vectors are saved in NPZ files.

An earlier diagonal-preconditioned run failed mixing diagnostics (split R-hat as high as2.60 and ESS below20); its raw data and diagnostics are retained but excluded from the summaries below. The banded run had split R-hat0.9995–1.0323 and within-chain autocorrelation ESS118–601 per800 draws. These basic diagnostics support exploratory comparisons but are not proof of stationarity, independence or rare-tail accuracy. There were no recorded divergent trajectories, and no Hessian diagonal shift was needed.

| n | β | mean c n^(2/7)(λmax−2) | sample SD | split R-hat | estimated ESS |
|---:|---:|---:|---:|---:|---:|
| 256 | 1 | -1.5632 | 2.4196 | 1.0322 | 144.8 |
| 256 | 2 | -4.0600 | 1.4343 | 1.0117 | 118.2 |
| 256 | 4 | -4.8499 | 0.6253 | 1.0015 | 601.3 |
| 1000 | 1 | -1.5554 | 2.6018 | 1.0080 | 175.9 |
| 1000 | 2 | -4.0241 | 1.3778 | 1.0158 | 137.3 |
| 1000 | 4 | -4.8024 | 0.5925 | 0.9995 | 598.9 |
| 10000 | 1 | -1.4670 | 2.6488 | 1.0111 | 163.1 |
| 10000 | 2 | -3.9641 | 1.4459 | 1.0052 | 161.0 |
| 10000 | 4 | -4.8749 | 0.6236 | 1.0024 | 579.0 |

Here c=6^(2/7) is the Claeys–Vanlessen kernel normalization. To compare with the displayed operator using the *formal deterministic drift* calculation, multiply these scaled eigenvalues by γ/c, where γ=2^(−6/7). This constant is derived algebraically in SCALING.md and is not fitted. For n=10000:

| β | quartic formal-scale mean | approximate MC SE | Gaussian operator mean | independent-sample SE |
|---|---:|---:|---:|---:|
| 1 | -0.4854 | 0.0686 | -0.5148 | 0.0857 |
| 2 | -1.3116 | 0.0377 | -1.0869 | 0.0549 |
| 4 | -1.6129 | 0.0086 | -1.3197 | 0.0375 |

The mismatch of sample means under this formal normalization is evidence only. It cannot exclude another constant normalization; the rigorous tail argument excludes every fixed positive normalization.

## Independent β=2 finite-n check and limiting-law computation

For n=256, a separate quadrature projection-kernel computation approximated the largest-eigenvalue CDF of the genuine unitary quartic ensemble. It used fully reorthogonalized weighted polynomials on [−3.5,6], with4096 and8192 Gauss–Legendre nodes. The maximum CDF change on45 comparison points was 0.00612; the orthogonality residual was below 3.1e-15. The800 HMC draws differed from the finer-grid CDF by at most 0.03616 on this grid. This is a quadrature consistency and sampler check, not an independent-sample goodness-of-fit test. Domain truncation and quadrature error are not certified.

An initial quadrature attempt formed exp(−n(U−minU)) before taking its square root; this underflowed near the edge and was rejected. The corrected code exponentiates half the exponent before normalizing. The final projection is checked for finiteness and orthogonality. This matters even at n=256.

The limiting higher-order TW₂ Fredholm determinant itself was not evaluated. Claeys–Olver1111.3527 describes numerical RH/Fredholm evaluation, but a verified implementation was not available in this workspace. The finite-n determinantal CDF above is explicitly distinguished from that limiting law. The rigorous comparison uses the published critical-kernel right-tail estimate, not an ordinary TW₂ approximation.

## Algebra, solver and tail checks

- Direct trace-vs-dense-eigenvalue action error: 1.78e-15.
- Exact quartic gradient vs centered finite differences: maximum error 6e-10.
- The banded analytic Hessian vs independently differenced gradients: maximum error 1.82e-09.
- Tridiagonal eigenvalue solver vs sparse shift-invert, n=10000: maximum error 1.89e-14.
- SymPy rederived the edge powers, the local quartic equations, x=D³/8+O(D⁴), c=2, and γ=2^(−6/7). Direct integration of the equilibrium density gives total mass0.9999999999916908; its Stieltjes transform independently has leading term1/z.
- Exact Gaussian log probabilities of the trial-function events are tabulated for k=0,1,2, β=1,2,4 and s=1,…,4096 in rayleigh_tail.csv. These are probabilities of a variational *sufficient event*, hence rigorous-formula lower bounds on an operator tail, not sampled eigenvalue-tail probabilities or estimates of its exact exponent.

Original plots: `data/eigenvalue_comparison.png`, `data/unitary_cdf_check.png`, and `data/trial_tail_powers.png`. No paper images or scans are present.

The final integrity audit (`code/audit.py`, results in `data/audit.json`) checks source-text hashes, PDF absence, report control characters, all saved row counts and sampled-matrix dimensions, numerical summary consistency, and the Gaussian trial-event power calculations. Mathematical proof steps were audited separately and matched to Baslingker's theorem.

## Reproduction

From this directory, with nice≥10 and one numerical thread:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/check_algebra.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/verify_models.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py artificial --draws 96
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py quartic --ns 256 1000 10000 --banded --burn 300 --draws 400 --thin 2
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/coupled_mesh.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/finite_unitary.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py tail
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/build_report.py
```

If the shell is not already at nice10, prefix the Python command with `nice -n 10`; the scripts check inherited priority. Sources can be regenerated with code/acquire.py and the URLs in sources/manifest.json. Versions and resource metadata are saved in data/environment.json.


# Literature search and exact locators

Search date: 13 November 2026. Primary sources were consulted throughout. Secondary search snippets were used only to discover primary papers, notably Baslingker; conclusions below are based on the primary texts. PDFs were converted in memory and discarded; only text is retained. The source manifest records URLs, byte hashes of the unretained PDF streams, text hashes and page counts. Page numbers below count PDF pages, not guessed journal pagination. Several arXiv PDFs have a regenerated date on their title page; the URL and hash identify the text actually inspected.

## Decisive result

Jnaneshwar Baslingker, *Stochastic domination in beta ensembles*, [arXiv:2304.09236v2](https://arxiv.org/abs/2304.09236v2), 22 December 2024 (first submitted 18 April 2023), **Theorem 4, PDF p. 7**: the KRV conjecture fails for β=2, k=1. The definition and precise connection to the conjectured operator are on pp.6–7; the proof is Section3, pp.10–12. Equation(22), p.12, gives the Gaussian variational lower-tail exponent (4k+3)/(4k+2). Equation(16), p.11, records the incompatible critical-unitary right-tail bound at k=1.

Published as *Journal of Mathematical Physics* **66**, 053303 (2025), [DOI10.1063/5.0254593](https://doi.org/10.1063/5.0254593). The [publisher page](https://pubs.aip.org/aip/jmp/article/66/5/053303/3346682/Stochastic-domination-in-beta-ensembles) explicitly confirms the negative result and is dated12May2025. Its readable abstract/reference page is saved as `baslingker_published_web.txt`. The journal PDF returned403, so the theorem number and exact pages cited here refer explicitly to arXiv v2. We do not claim to have checked the journal's internal pagination or theorem renumbering.

This is a negative literature resolution, so REPORT.md begins COUNTEREXAMPLE. The user's early-stop instruction for a theorem *proving* the conjecture for k≥1 is not triggered. There is no claim of a new refutation.

## Other primary sources checked

| Source | Exact location checked | Scope and implication |
|---|---|---|
| Virág, [1804.06953](https://arxiv.org/abs/1804.06953) | Conjecture5, p.14; Theorems5.1 p.6 and8.1 in Section8 | Exact requested statement; half-line Airy limit and context of polynomial-potential tridiagonal matrices. |
| Krishnapur–Rider–Virág, [1306.4832](https://arxiv.org/abs/1306.4832), CPAM69(2016),145–199 | Theorem1 p.3; entry density eq.(8) p.8; local minimizers eqs.(10)–(14) p.9; Assumptions1–2 and Theorem9 pp.13–15; Proposition41 eq.(68) p.49; Section13 pp.55–57, Conjecture45 p.57 | Proves uniformly convex regular potentials, not critical k≥1. Conjecture45 is the arXiv numbering; Baslingker refers to the published numbering Conjecture13.1. |
| Ramírez–Rider–Virág, [math/0607331](https://arxiv.org/abs/math/0607331) | Theorem5.1 p.21; Assumptions1–2 pp.20–21 | General tridiagonal convergence criterion. The saved preprint uses this numbering; do not substitute a theorem number from a different printing. |
| Bloemendal–Virág, [1011.1877](https://arxiv.org/abs/1011.1877) | Theorem2.10, p.19; Remark2.11 same page | Boundary-condition extension used by KRV; spikes concern regular Airy limits. [1109.3704](https://arxiv.org/abs/1109.3704) abstract also checked: matrix-valued spiked regular-edge limits, not the critical-density operator. |
| Claeys–Vanlessen, [math-ph/0607043](https://arxiv.org/abs/math-ph/0607043) | Example1.2 p.5; Theorem1.7 pp.6–7; Lax pair eqs.(1.15)–(1.21) p.4; Theorem1.11 p.8 | Rigorous β=2, k=1 critical kernel convergence, locally uniform including the diagonal. Theorem1.11 concerns deterministic orthogonal-polynomial recurrence coefficients, not random KRV coefficient convergence. |
| Claeys–Its–Krasovsky, [0901.2473](https://arxiv.org/abs/0901.2473) | Example1.2 p.2; discussion of eqs.(1.13)–(1.15) p.3; RH eqs.(1.19)–(1.21) p.4; right-tail eqs.(1.23)–(1.24) p.5; Theorem1.5 p.6; Theorem1.12 p.9 | Critical kernels/Fredholm determinants and hierarchy formulas. The p.3 paragraph expressly says their goal is not to prove general kernel or largest-eigenvalue convergence. Theorem1.5 is a left-tail asymptotic theorem, not an operator-convergence theorem and not the positive-tail bound used here. |
| Claeys–Kuijlaars, [math-ph/0501074](https://arxiv.org/abs/math-ph/0501074) | Theorem2.1 p.6, introduction | Quadratic *interior* zero, PainlevéII double scaling. Not a5/2 right edge. |
| Bleher–Its, [math-ph/0201003](https://arxiv.org/abs/math-ph/0201003) | Introduction; Theorem1.2 p.16 | Symmetric critical quartic/interior double scaling and orthogonal-polynomial asymptotics, not the proposed random edge operator. |
| Dumaz–Labbé, [2212.04862](https://arxiv.org/abs/2212.04862) | Theorem1 p.2 | Whole-line white-noise Anderson localization. Does not prove the critical β-ensemble limit. Their large-temperature Airy and localization-crossover work was also searched by title/abstract. |
| Dumaz–Li–Valkó, [2003.02779](https://arxiv.org/abs/2003.02779) | Theorem3 p.4 | Operator-level hard-to-soft Bessel→ordinary Airy transition, not k≥1. |
| Li–Valkó–Xu, [2607.08536](https://arxiv.org/abs/2607.08536) | Theorem1 p.2; introduction and operator-convergence discussion | 2026 lower Laguerre edge transition to ordinary Airy for diverging parameters, not a higher-order vanishing edge. |
| Gorin–Kleptsyn, [2009.02006](https://arxiv.org/abs/2009.02006) | Theorem1.1 p.4 and introduction | β→∞ multilevel Gaussian/Airy objects, not finite-β critical-density universality. |
| Lambert–Paquette, [2009.05003](https://arxiv.org/abs/2009.05003) | Theorem1.5 p.5 and introduction | Gaussian regular-edge characteristic polynomials and stochastic Airy function. |
| Edelman–Sutton, [math-ph/0607038](https://arxiv.org/abs/math-ph/0607038) | Abstract and Airy/Bessel operator sections | Classical finite-difference stochastic operators; no critical polynomial-potential limit theorem. |
| Forrester–Rahman–Shen, [2611.10990](https://arxiv.org/abs/2611.10990) | Abstract | November2026 hard-edge review/results. Hard-edge gap/correction results do not establish the proposed k≥1 soft edge. Earlier Forrester edge/Coulomb-gas work was searched by name and subject; no positive resolution was found. |
| Cafasso–da Silva Pinheiro, [2504.20721](https://arxiv.org/abs/2504.20721) | Theorem1.5 p.4 and Theorem1.10 p.6 | Critical5/2 unitary determinantal statistics governed by KdV. “Operator” here includes integral/RH structures, not convergence to the displayed Gaussian Schrödinger operator. |
| Dai–Long–Xu–Yao–Zhang, [2501.12679](https://arxiv.org/abs/2501.12679) | Theorem1.1 p.6 | Multiplicative constant in higher-order Fredholm large-gap asymptotics; no KRV stochastic-operator limit. |
| Claeys–Olver, [1111.3527](https://arxiv.org/abs/1111.3527) | Abstract and numerical RH/Fredholm method | A method for numerical higher-order TW distributions; no certified implementation/data was available in this workspace. We do not replace this law by ordinary TW₂. |

## Search record and limits

Queries included the exact source title and arXiv identifier; “exotic edge operators”; “Universality of the stochastic Airy operator”; “higher order stochastic Airy operator”; “critical edge beta stochastic operator2024 2025 2026”; “higher order edge beta ensembles”; “beta ensemble critical point operator”; “stochastic operator higher order Tracy-Widom”; every author group named in the task; and follow-ups through the cited references and recent author publication pages.

The decisive follow-up was “stochastic higher order Tracy-Widom operator conjecture”, which surfaced Baslingker's title. The initial search by “Conjecture5” or “Conjecture45” missed the published numbering13.1. Searching the operator description rather than only the conjecture label found the negative result.

The search is not a proof that no additional literature exists. It *is* enough to establish that this problem, as stated with the displayed operator, already has a printed counterexample at k=1,β=2. No higher-k or β≠2 classification is asserted.



Task: “Open problem D0043” — 13 November2026, approximately10:40 Asia/Tbilisi (first recorded session time).
