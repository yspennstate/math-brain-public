# E0024 — attempt and referee audit

Date: 2026-10-12. Result: PARTIAL. There is no proof or counterexample here for the unrestricted question. Results below are proved reductions/special cases, explicitly conditional on the stated extra hypotheses. No novelty is claimed for familiar stability arguments.

## 1. Exact question and conventions

Let X_1 on R^n and X_2 on R^m be independent Lévy processes, n,m≥1. If each satisfies Hunt’s hypothesis (H), must Z=(X_1,X_2) satisfy (H)? Equivalently the projections onto a nonempty proper subspace and its orthogonal complement are independent and satisfy (H). If ?nonempty? permits the zero subspace, that extra case is tautological. Exact source quotations and references are in LITERATURE.md.

For a set D, T_D=inf{t>0:X_t∈D}. A thin set is contained in a nearly Borel C with P^x(T_C=0)=0 for every x. A semipolar set is contained in a countable union of thin sets. A polar set is contained in a nearly Borel C with P^x(T_C<∞)=0 for every x. (H) says that every semipolar set is polar. We use processes with their full families of translated starting laws.

Exponents use E exp(i<z,X_t>)=exp(-tψ(z)); r=Re ψ≥0. For finite positive measures ν, define

E_X^λ(ν)=∫ (λ+r(z))/((λ+r(z))²+(Im ψ(z))²) |ν̂(z)|² dz.

The same Fourier expression may be used for finite complex measures; (H) criteria themselves quantify over positive measures. Independence gives ψ_Z(x,y)=ψ_1(x)+ψ_2(y).

Imported results used below, with all relevant hypotheses:

1. Survey Theorem 4.2, PDF p.20: if X has resolvent densities with respect to Lebesgue measure, (H) is equivalent to E_X^λ(ν)→0 for every finite positive measure ν of finite 1-energy.
2. Survey Theorem 2.3, PDF p.4 (Rao): a process with resolvent densities satisfies (H) if |1+ψ|≤A f(A), A=1+Re ψ, with positive increasing f and ∫_N^∞dλ/(λ f(λ))=∞.
3. Survey Proposition 4.8, PDF p.21: assuming X,Y,Z have resolvent densities, X satisfies (H), Y has |Im ψ_Y|≤c(1+Re ψ_Y), and ν=η⊗ξ is positive, compactly supported and of finite product energy, its product energy tends to zero.
4. Domination of positive-measure energy used by the survey on p.23, citing Kanda [28, Corollary of Lemma 2.1]: for positive compact measures η≤ξ, E_X^λ(η)≤E_X^λ(ξ). We use this only in the optional measure-class extension in Section 6, not in the sharp comparison or Rao theorem.

## 2. Product closure is equivalent to independent-sum closure

This is an equivalence of universal assertions over all finite dimensions. It does not say a fixed-dimensional sum theorem would settle every product dimension.

### Lemma 2.1: inert coordinates preserve (H), in both directions

For a Lévy process X on R^n, the R^{n+m}-valued process W=(X,0) satisfies (H) if and only if X does.

Proof. Started at (x,v), W_t=(x+X_t,v). For a nearly Borel set C in the product, write C_v={u:(u,v)∈C}. Then T_C for W started at (x,v) equals T_{C_v} for X started at x, pathwise. Sections are nearly Borel for the corresponding process. This follows directly from the defining Borel lower/upper envelopes of a nearly Borel set: take their sections, and transfer the zero probability of ever entering the envelope difference by the same pathwise identity. Cylinders over nearly Borel sets are nearly Borel for W by the converse envelope construction.

Suppose X satisfies (H), and D is semipolar for W. Choose nearly Borel thin witnesses C_j such that D⊂C=∪_j C_j. For each v, C_{j,v} is thin for X by the hitting-time identity. Thus C_v is semipolar and, by (H) for X, polar. Since C_v itself is nearly Borel and is contained in a polar witness, P^x(T_{C_v}<∞)=0 for every x. Therefore P^{(x,v)}(T_C<∞)=0 for every (x,v). C is a nearly Borel polar witness for D; hence W satisfies (H).

Conversely, if W satisfies (H), a semipolar set D for X has nearly Borel thin witnesses C_j. The cylinders C_j×R^m are thin for W. Their union is semipolar, so W cannot hit it from any (x,v). The hitting-time identity says X cannot hit ∪C_j from any x. That union is a polar witness for D. Hence X satisfies (H). ∎

### Lemma 2.2: a surjective linear image preserves (H)

If W on R^d satisfies (H) and L:R^d→R^k is surjective linear, then LW satisfies (H).

Proof. Let D be semipolar for LW and C_j nearly Borel thin witnesses. Their inverse images under L are nearly Borel for W: pull back Borel envelopes, and transfer the probability-zero entrance condition by T_{L^{-1}C_j}(W)=T_{C_j}(LW). They are thin by the same identity. Their union is semipolar for W, so it is polar. Consequently P^x(T_{L^{-1}(∪C_j)}<∞)=0 for every x. For every y choose x with Lx=y; the identity gives P^y(T_{∪C_j}<∞)=0 for LW. Thus D is polar. ∎

### Theorem 2.3: equivalence

(P) For every n,m, independent (H) Lévy factors have an (H) product.

(Sum) For every d, the sum of two independent (H) Lévy processes on R^d satisfies (H).

Then (P)⇔(Sum).

Proof. Assume (P). For independent X,Y on R^d satisfying (H), (X,Y) satisfies (H). Apply Lemma 2.2 to L(u,v)=u+v. This gives (Sum), the implication noted in survey Remark 5.1(ii).

Assume (Sum). Given the factors in the product question, form U=(X_1,0_m) and V=(0_n,X_2), both on R^{n+m}. Lemma 2.1 gives (H) for U; the coordinate-permuted version gives (H) for V. U,V are independent because they are deterministic functions of the independent original processes. Their sum is (X_1,X_2), so (Sum) yields (P). ∎

This reduction removes no difficult quantifier: general independent-sum closure is also open in the searched source/literature.

## 3. A rigorously scoped Rao special case

### Theorem 3.1

Assume both factors have absolutely continuous transition laws for every t>0. Suppose there is ONE positive nondecreasing f:[1,∞)→(0,∞), with ∫_1^∞ds/(s f(s))=∞, such that

|Im ψ_i(z)|≤(1+Re ψ_i(z)) f(1+Re ψ_i(z)), i=1,2.

Then their independent product satisfies (H).

Proof. Put r_i=Re ψ_i, A_i=1+r_i, A=1+r_1+r_2. Since A_i≤A and A_1+A_2=A+1≤2A,

|Im ψ_Z|≤A_1 f(A_1)+A_2 f(A_2)≤2A f(A).

Thus |1+ψ_Z|≤A+|Im ψ_Z|≤A F(A), where F(s)=1+2f(s). F is positive and nondecreasing. Since f(s)≥f(1)>0,

F(s)≤(2+1/f(1)) f(s),

so the required integral for F diverges.

If p_{i,t} are transition densities, independence gives product transition density p_{1,t}(u)p_{2,t}(v). Tonelli shows u_α(u,v)=∫_0^∞e^{-αt}p_{1,t}(u)p_{2,t}(v)dt is a resolvent density: it is nonnegative measurable and integrates to 1/α. Rao’s theorem applies to Z and F. ∎

The proof also works if product resolvent densities are separately assumed, instead of deriving them from transition densities. Having each factor satisfy (H) alone does not supply f. Having two different divergent-integral control functions does not automatically supply a common one: domination by max(f_1,f_2) needs its own divergence check.

Boundary cases: the identically zero process and driftless compound Poisson processes have no nonempty thin sets, since every starting point is held for a positive time. If one factor is compound Poisson and the other is any (H) factor, source Proposition 3.9 already proves the product case without densities. If both satisfy condition (S), source Proposition 3.10 already proves it. Nonzero deterministic drift fails (H): a singleton is thin (no positive-time return near zero) but is hit from a suitable earlier point. It cannot serve as an admissible factor in a counterexample to this problem.

## 4. Sharp imaginary-perturbation comparison and reduction

Let c≥0 and define

K(c)=1+c²/2+(c/2)√(c²+4).

For a>0, b,d real with |d|≤c a,

K(c)^{-1}(a²+b²) ≤ a²+(b+d)² ≤ K(c)(a²+b²).  (4.1)

### Complete proof, including optimality

If c=0 then d=0 and K=1, so equality holds. If c>0, k=K(c)>1 and (k−1)²=k c²; this follows by expansion of the displayed expression and (√(c²+4))²=c²+4. Also d²≤c²a². The identity

(k−1)[k(a²+b²)−(a²+(b+d)²)]
 = ((k−1)b−d)²+k(c²a²−d²)

has nonnegative right side. Divide by k−1>0 to obtain the upper bound. Apply that same upper bound to (a,b+d,−d), which still satisfies its assumption. This gives a²+b²≤k(a²+(b+d)²), the lower bound. For a=1,d=c,b=c/(k−1), the square and remainder in the identity both vanish, so the upper ratio equals k. No smaller universal constant works. The lower bound is sharp by reversing this substitution. ∎

The precise algebraic step with k>1 and (k−1)²=k c² is formalized in SharpComparison.lean, importing only Mathlib.Data.Real.Basic and the Linarith/Ring tactics. The c=0 case, radical formula, division to kernels, integration, and potential-theoretic application are proved here, not claimed to be formalized.

### Theorem 4.2: invariance under a sector-bounded imaginary perturbation

Let Z,Z′ be Lévy processes on the SAME R^d, BOTH with resolvent densities. Assume their exponents have equal real part r and

|Im ψ_Z−Im ψ_Z′|≤c(1+r).

Then Z satisfies (H) if and only if Z′ does; their finite positive measures of finite 1-energy are exactly the same. For every λ≥1 and every finite positive ν,

K(c)^{-1} E_{Z′}^λ(ν) ≤ E_Z^λ(ν) ≤ K(c) E_{Z′}^λ(ν).  (4.2)

Proof. Put a=λ+r>0, b=Im ψ_Z′, d=Im ψ_Z−Im ψ_Z′. The assumption gives |d|≤ca. Invert the strictly positive denominators in (4.1) and multiply by a, obtaining the same two-sided comparison of the two real resolvent kernels. Multiply by |ν̂|²≥0 and integrate; Tonelli/order gives (4.2), also as an extended-value inequality. At λ=1 it identifies the finite-energy measures. For each of those measures (4.2) transfers convergence to zero in either direction. Apply Theorem 4.2 of the survey to both processes, whose resolvent densities are explicitly assumed. ∎

### Corollary 4.3: reduction to a symmetric partner

Let X,Y be independent. Suppose |Im ψ_Y|≤c(1+Re ψ_Y). Let Y^s have exponent Re ψ_Y (realize its law as Y_{t/2}−Y′_{t/2}, with an independent copy Y′). Assume Z=(X,Y) and Z^s=(X,Y^s) both have resolvent densities. Then Z satisfies (H) iff Z^s does.

Proof. Equal real parts follow from additivity. The imaginary difference is Im ψ_Y(y), bounded by c(1+Re ψ_Y(y))≤c(1+Re ψ_X(x)+Re ψ_Y(y)). Apply Theorem 4.2 above. If X and Y have transition densities for all t>0, Y^s has the convolution density of p_{Y,t/2} and its reflection; both products have transition, hence resolvent, densities. ∎

The earlier September memo already had this reduction with the nonoptimal constant 2(1+c²). The new algebraic constant here is sharp. Neither version proves that pairing an arbitrary (H) X with a symmetric Y preserves (H).

## 5. Exact obstructions to two tempting transfers

### 5.1 Resolvent densities do not automatically tensorize

Let X_t=t on R and let Y_t=t be another deterministic process. They are independent, since their path laws are point masses. Each has resolvent density e^{-αu}1_{u>0}, translated appropriately at other starting points. The product resolvent starting at the origin is supported on the diagonal {(t,t):t>0}, a Lebesgue-null subset of R², and has total mass 1/α. It therefore has NO Lebesgue density. This disproves the blanket assertion that individual resolvent densities pass to independent products. These factors fail (H), so it does NOT disprove such an assertion with additional (H)/Rao hypotheses, nor does it answer E0024. We did not use that unproved stronger assertion.

### 5.2 Genuine (H) factors can have arbitrarily large cancellation amplification

Take reflected, maximally skewed 1-stable processes on R with exponents

ψ_+(u)=|u|+iκu log|u|,   ψ_−(u)=|u|−iκu log|u|, κ=2/π,

with u log|u| interpreted as 0 at 0. These are the usual 1-stable Lévy exponents with opposite skew parameters and zero location in this convention. Both have transition densities, and both satisfy (H) by Rao’s criterion: if A=1+|u|, then

|1+ψ_±(u)|≤A+κ|u||log|u||≤A(2+κ log A).

For |u|≥1 use |u|log|u|≤A log A; for |u|≤1 use |u||log|u||≤1/e and κ/e<1. The function f(A)=2+κ log A has divergent ∫dA/(Af(A)). Thus their product also satisfies (H) by Section 3.

Nevertheless, at x=y=T>1 the joint imaginary parts cancel. Its 1-energy kernel is 1/(1+2T); either factor’s kernel at T is

(1+T)/((1+T)²+κ²T²(log T)²).

The ratio joint/single is

[((1+T)²+κ²T²(log T)²)/((1+T)(1+2T))]
 ∼ (κ²/2)(log T)² →∞.

Thus no pointwise inequality bounding the joint kernel by a constant times the SUM of the two marginal kernels holds for this fixed pair (the sum merely introduces a factor 2). This is an obstruction to that specific domination proof, not to (H). Numerical values at log T=10,50,100 were approximately 20.76,507.11,2026.92; see numerical_checks.json. The asymptotic proof, not numerics, proves unboundedness.

## 6. Correlated measures: a sufficient class and its strict limitation

Under the hypotheses of imported Proposition 4.8, suppose a positive compact measure ν is dominated by μ=Σ_{j=1}^N η_j⊗ξ_j, with each product positive, compactly supported, and of finite 1-energy for Z. Then E_Z^λ(ν)→0.

Proof. Fourier Cauchy–Schwarz gives E_Z^λ(μ)≤NΣ_j E_Z^λ(η_j⊗ξ_j), and domination of positive-measure energy gives E_Z^λ(ν)≤E_Z^λ(μ). Proposition 4.8 makes each summand tend to zero. ∎

Even in the Brownian case this finite-product domination class does not exhaust finite-energy measures. Here is an exact boundary test.

Let the two factors be independent Brownian motions with ψ_i(u)=u². Let ν be the image of Lebesgue measure on [0,1] under u↦(u,u). It is non-atomic and carried by the diagonal D. Its Fourier transform at (x,y) is ∫_0^1 exp(i(x+y)u)du. Set s=x+y,t=x−y, with Jacobian 1/2 and x²+y²=(s²+t²)/2. Since

∫_R dt/(1+(s²+t²)/2)=2π/√(s²+2),

Tonelli gives

E_Z^1(ν)=π∫_R |∫_0^1e^{isu}du|²/√(s²+2) ds<∞.

Indeed the inner modulus squared is ≤min(1,4/s²), so the integrand is bounded near zero and O(|s|^{-3}) at infinity.

For any finite product measure η⊗ξ, Fubini gives its mass on D away from atoms of ξ as zero, since (η⊗ξ)(D)=∫ξ({u})η(du). The atoms of a finite ξ are countable. For a finite sum of products choose the countable union A of these atomic coordinates. Then that sum gives D\{(u,u):u∈A} zero mass; ν gives it mass 1. Hence ν cannot be dominated by any such finite sum. This argument allows arbitrary finite η_j,ξ_j, so in particular excludes finite-energy ones. ∎

This Brownian product itself satisfies (H). The example proves that the finite-product domination route cannot establish the unrestricted energy criterion by itself; it is not a counterexample to (H).

## 7. The exact remaining gap

Already in the symmetric-partner subcase with all required resolvent densities, write r_Y(y)≥0 for the real exponent and let ν be ANY finite positive compactly supported measure of finite product 1-energy. Define the finite complex measure on R^n

σ_y(du)=∫_{R^m} e^{i<y,v>} ν(du,dv).

Tonelli and the Fourier identity give exactly

E_Z^λ(ν)=∫_{R^m} E_X^{λ+r_Y(y)}(σ_y)dy.  (7.1)

To prove (H) for Z one needs (7.1)→0 for every such ν. X satisfying (H) controls positive finite-energy measures on R^n. It does not directly give an integrable majorant, uniform in λ, for the complex and correlated slices in (7.1).

The elementary parameter comparison gives, for λ≥1,

E_X^{λ+r_Y(y)}(σ_y)≤[(λ+r_Y(y))/(1+r_Y(y))] E_X^{1+r_Y(y)}(σ_y).  (7.2)

Proof: for a′≥a>0 and real b,

[a′/(a′²+b²)]/[a/(a²+b²)]
 =(a′/a)(a²+b²)/(a′²+b²)≤a′/a.

Apply this with a=1+r_Y+Re ψ_X, a′=λ+r_Y+Re ψ_X. The last ratio is ≤(λ+r_Y)/(1+r_Y), since Re ψ_X≥0, and integrate. ∎

On r_Y≥λ the factor in (7.2) is ≤2, so integrability at λ=1 controls that tail. On r_Y<λ it can grow as λ; it does not provide dominated convergence. Fourier kernels are not pointwise monotone in λ in general: derivative of a/(a²+b²) in a is (b²−a²)/(a²+b²)². Positivity/monotonicity results for positive measures must not be silently applied to complex σ_y. Product-form measures are handled by Proposition 4.8; Section 6 gives a limited extension, and the diagonal example proves its limitation.

No construction in this session supplies an admissible thin nonpolar set for a product of two (H) factors. No theorem in this session closes (7.1) for arbitrary ν. No universal density argument was proved for singular products. These are the remaining gaps, not hidden assumptions in a purported solution.

## 8. Hostile-referee checklist and checks

- Source quantifiers: checked PDF pp.15,18; no extra assumptions imported into the open question.
- Universal reduction: inert-coordinate proof uses all starting fibers, not just the origin; sum proof uses independent embedded processes; linear image is surjective so every starting point is covered.
- Perturbation: same real part and two product resolvent densities are explicit. The comparison constant is uniform in λ≥1 and in the measure. λ=1 identifies the domain before the (H) criterion is applied.
- Optimal algebra: exact sum-of-squares identity and equality case proved above; 20,000 bounded-memory random evaluations (seed 24) and six equality tests passed. These numerics are secondary to the proof.
- Rao theorem: a common f is explicit; F=1+2f preserves integral divergence by f(1)>0. Product density follows from time-specific transition densities, not from convolution of individual resolvents.
- Counterexamples to shortcuts: deterministic drift only refutes an unconditional density assertion; opposite 1-stable exponents only refute a pointwise domination inequality; Brownian diagonal measure only refutes finite-product domination. NONE is called a counterexample to E0024.
- Literature: all requested services queried and archived; failures recorded. Later citing papers’ full PDFs checked and concern different assertions. No exact printed solution was identified.
- Lean: final run exited 0. Both shear_bound and shear_comparison have only [propext, Classical.choice, Quot.sound] as reported axioms; no sorryAx. The first run failed because PowerShell wrote a UTF-8 BOM; a subsequent run caught the multiplication-order helper error. Both were corrected and the final result is recorded verbatim in lean_check.txt. Only its named algebraic lemmas are called machine-checked, and only after exit code 0. No sorry, native_decide, or full Mathlib import is used.

Research conclusion: bounded attempt exhausted with a precise gap. STATE DONE means this attempt is finished; VERDICT PARTIAL means the mathematical problem remains unresolved here.

Operational caveat: the user-prescribed brain.py recall command unexpectedly reported handing an index refresh to a detached process (pid 30276). No explicit brain-writing command was issued, and no process was killed. Subsequent work and result writes remained in this problem folder. The tool’s self-refresh is not mathematical evidence.


## 9. Renewed serious attempt at the user's request (2026-10-12)

Full new proofs and the two new approaches are in SECOND_ATTEMPT.md, which forms part of this attempt record.

1. Path-law change of measure transfers product (H) under finite-horizon absolute continuity of both coordinate laws. Under local equivalence it preserves product (H) both ways. A triplet version and an infinite-activity special case are proved (B1-B2).
2. For a Levy measure nu, put Lambda=nu+nu^- and g=dnu/dLambda. The minimum Hellinger cost over symmetric reference measures is J=(1/4)int(sqrt(g)-sqrt(1-g))^2 dLambda, attained by rho_*=(sqrt(g)+sqrt(1-g))^2 Lambda/4. A locally dominating symmetric Levy path law exists exactly when J<infinity and a+int_{|x|<1}x(nu-rho_*) is in Range(Q). Proofs include singular measures and compensated drift (B4). Skew stable (H) factors have J=infinity, blocking a general solution by this route (B3). Lean checked the elementary optimum with exit 0, no sorryAx.
3. Smoothing a correlated measure in the symmetric partner coordinate makes its energy vanish at each fixed scale. Removing smoothing is equivalent, measure by measure, to sup_{lambda>=1}E_Z^lambda(nu-nu_epsilon)->0. The imported positive-measure lemma was verified in the fetched original Kanda paper (A1-A2).
4. An explicit positive Gaussian-modulated family for a fixed skew-Cauchy/Brownian (H) product disproves a uniform bound of higher smoothing-residual energies by residual 1-energy. The ratio grows as (1/pi)log T; packet asymptotics prove this and small Gauss-Hermite computations corroborate it (A3). This defeats a shortcut, not (H).

The gap in Section 7 survives in a sharper form: establish the per-measure uniform smoothing approximation from bare factor (H), or construct an admissible counterexample, and cover products without resolvent densities. The renewed verdict remains PARTIAL.

Compactness check for the renewed obstruction: A3 addendum truncates the Gaussian inputs to explicit squares of radius sqrt(20 T log T). Gaussian-tail bounds and Plancherel show the same divergent energy ratio for compactly supported positive probability inputs. This still concerns a changing family, not a counterexample to (H).
