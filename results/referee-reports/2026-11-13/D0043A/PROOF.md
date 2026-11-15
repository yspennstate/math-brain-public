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
