# F0073 - research record (2026-10-12)

## Exact target and normalization
Velenik, *Localization and delocalization of random interfaces*, Probability Surveys 3 (2006), 112-169, DOI 10.1214/154957806000000050, arXiv:math/0509695v3, PDF p.23 (printed p.134), asks: "Open Problem 6. Extend (21) (when d = 2) to the case of uniformly strictly convex interactions V." The preceding paragraph includes existence of the positive infinite-volume field pinned at 0 and a mean comparable to log |i|.

Section 1.1, PDF p.5, assumes V even, convex, V(0)=0, V in C^2, and 0<c_- <= V'' <= c_+ < infinity. We study the real-valued nearest-neighbor field with edges counted once and H=sum_e V(phi_x-phi_y). Fixed positive inverse temperature and the uniform nearest-neighbor normalization can be incorporated into V and its curvature constants. More general edge weights are not part of the unit-edge normalization; the weighted modification of the local inequality is described below. Heights are real, not integer-valued. Logarithmic comparisons concern large |i|; log(2+|i|) avoids zero at neighbors.

For Lambda_N=[-N,N]^2 intersect Z^2 set phi_0=0, phi=0 outside Lambda_N, and impose phi_x>=0 at every free vertex. Let mu_N^+ be the density proportional to exp(-H) on this orthant. The source paragraph does not spell out the infinite-volume construction. Here the precise construction is the increasing zero-boundary finite-volume exhaustion, consistent with its domain notation. No uniqueness assertion for every possible pinned positive DLR measure is made. The target includes a proper limit and constants 0<c<C<infinity such that c log|i| <= E phi_i <= C log|i| for large |i|.

## Prior attempt audit
The intake F0073-A001 (2026-09-08) claims an upper bound by domination by a wall field without the pin in Lambda_(2|i|), followed by a monotone limit. This does not prove the upper bound. Domain enlargement with nonnegative boundary values increases the wall field. A bound in a single small box cannot upper-bound the increasing infinite-volume limit. Comparison in Lambda_N instead gives C log N, which diverges as N tends to infinity at fixed i. The local comparison supplies a lower bound.

## Completed components
1. A full finite-volume proof of monotonicity in nonnegative boundary data and in domain, via FKG boundary interpolation.
2. Local-box lower comparison, giving a logarithmic lower bound using the existing zero-boundary box entropic-repulsion theorem.
3. A self-contained energy identity on the orthant, and finite-volume resistance upper bound, explicitly not volume uniform.
4. Determine precisely the missing uniform upper bound and tightness issue.


## Proposition 1: finite-volume boundary and domain monotonicity

All finite graphs below have a nonempty grounded set meeting every component. The free coordinates are in [0,∞). Nonnegative boundary heights are allowed. Densities are integrable and have all moments: V(t)≥c_-t²/2 and the grounded Dirichlet Laplacian is positive definite; linear boundary terms do not destroy coercivity.

For two different free coordinates x,y, the mixed derivative of log density is V''(φ_x−φ_y)≥0 when they are adjacent, and zero otherwise. Consequently the density satisfies the lattice condition f(a∨b)f(a∧b)≥f(a)f(b). Here is a direct edge check: for a<=b and c<=d,
    V(a-d)+V(b-c)-V(a-c)-V(b-d)
      = integral_a^b [V'(t-c)-V'(t-d)] dt >= 0,
since V' is increasing. On each edge, taking coordinatewise minimum and maximum either preserves the two original endpoint pairs or replaces crossed pairs by ordered pairs. The displayed inequality decreases the total edge energy. Single-coordinate boundary terms preserve their sum exactly. Hence H(a meet b)+H(a join b)<=H(a)+H(b), which proves the lattice condition, including the boundary by continuity. The orthant is closed under coordinate minimum and maximum. The continuous FKG association theorem therefore applies: Cov(F,G)≥0 for bounded increasing F,G. This use of the standard FKG theorem is an explicit external theorem, not a newly proved theorem.

Let b_z be a boundary height. For a bounded increasing function F of the free coordinates, differentiating its expectation gives
    d E_b F / d b_z = Cov_b(F, S_z),
    S_z(φ)=Σ_{x free, x~z} V'(φ_x−b_z).
Indeed −∂_{b_z}H=S_z. S_z is increasing in every free coordinate. FKG gives a nonnegative derivative. Although S_z is unbounded, it has linear growth, and truncation to [−K,K], followed by dominated convergence using Gaussian tails, justifies association. Differentiation is also justified by Gaussian-tail domination uniformly on compact boundary-height intervals. Integrating one boundary coordinate at a time proves stochastic monotonicity under b≤b'. The argument extends to increasing coordinates by bounded truncation and monotone convergence.

If D⊂D' are two domains with the same pin at 0, condition the D' wall field on the coordinates outside D. Its conditional law inside D is exactly the wall Gibbs specification with nonnegative boundary heights and the same pin if the pin is in D. It stochastically dominates the zero-boundary specification in D. Average over the outside coordinates. If fields are extended by zero outside their domains, the extra coordinates in D' are already ≥0; apply the same conditional argument to any bounded increasing function of all coordinates. Hence μ_D^+≤st μ_D'^+.

The same argument holds when D avoids the pin altogether: the conditional law in D dominates an ordinary zero-boundary wall field with no pin. No conditioning on the probability-zero event φ_0=0 is used; 0 is a fixed grounded vertex throughout.

## Proposition 2: logarithmic lower bound from the existing box theorem

External input B (already stated explicitly by Velenik, PDF p.22, printed p.133, citing Deuschel–Giacomin [40]): for even uniformly strictly convex V in two dimensions, the expected center height in an ordinary zero-boundary square of radius r, constrained nonnegative throughout that square, is at least a(V) log r for all sufficiently large r. The same source states the corresponding upper bound. This is a box theorem. It does not assert the desired pinned infinite-volume upper bound. The reduction here depends on B; the original paper's full proof is not reproduced, and no exact theorem-number quotation from it is claimed.

Fix i≠0 and let r=floor(||i||_∞/3). For sufficiently large ||i||_∞, r≥1. The translated square D=i+[−r,r]² misses 0, since its distance from 0 is at least ||i||_∞−r>0. If N≥2||i||_∞, D and its nearest-neighbor boundary lie in Λ_N. By Proposition 1, conditional on the field outside D, the expected height at i is at least the expected center height in the ordinary zero-boundary wall field on D. Translation invariance and B give
    E_{μ_N^+} φ_i ≥ a(V) log r ≥ c(V) log ||i||_∞
for all sufficiently large ||i||_∞, uniformly over these N. The last inequality follows from r≥||i||_∞/4 for ||i||_∞≥12 and log(r)≥(1/2)log||i||_∞ for ||i||_∞≥16. Enlarging the threshold if necessary covers both conditions.

Thus every proper weak limit satisfies E φ_i≥c log||i||_∞. To justify this without an incorrect exchange of means and weak limits, retain the full stochastic domination by the fixed ordinary wall field on D. For every K, E_{μ_N^+} min(φ_i,K)≥E_{wall,D} min(φ_i,K). Pass to weak limits at fixed K and then let K→∞; the right side tends to the box mean. This does not establish the existence of a proper limit.

## Proposition 3: a volume-dependent energy upper bound (self-contained)

Let n=|Λ_N\{0}| be the number of free coordinates and let L be the unit-conductance grounded Dirichlet Laplacian. Write Q(φ)=φᵀLφ=Σ_e(φ_x−φ_y)², including edges incident to the pin or outer zero boundary once.

For every free vertex v integrate ∂_{φ_v}(φ_v exp(−H)) over the orthant. The boundary term at φ_v=0 is zero because of the factor φ_v; the boundary at infinity is zero by coercivity. Fubini and differentiation are legitimate because H has at least a positive quadratic lower bound and its derivatives have at most linear growth. Dividing by the partition function gives E[φ_v ∂_v H]=1. Summing over v, each free-free edge contributes
    φ_x V'(φ_x−φ_y) + φ_y V'(φ_y−φ_x)
    = (φ_x−φ_y)V'(φ_x−φ_y),
since V' is odd. Each free-ground edge contributes the same expression with the grounded height zero. Hence the exact identity is
    E Σ_e (φ_x−φ_y)V'(φ_x−φ_y)=n.
Evenness gives V'(0)=0. Integrating c_-≤V''≤c_+ from 0 to t, with the orientation of the integral respected for t<0, gives
    c_-t²≤t V'(t)≤c_+t².
Therefore n/c_+≤E Q(φ)≤n/c_-.

Let R_N(i)=(L^{-1})_{ii}, the resistance from i to the grounded set. For any deterministic vector φ,
    φ_i=e_iᵀφ=(L^{-1/2}e_i)ᵀ(L^{1/2}φ),
so Cauchy–Schwarz gives φ_i²≤R_N(i)Q(φ). Consequently
    E φ_i≤sqrt(E φ_i²)≤sqrt(n R_N(i)/c_-).
This is a proved finite-volume bound; n grows like N² and it DOES NOT give a bound uniform in N. For a still more elementary estimate, a nearest-neighbor path of length ℓ=||i||_1 from 0 to i and Cauchy–Schwarz give R_N(i)≤ℓ whenever that path lies inside the box.

The cancellation and resistance inequality on the three-vertex path are formalized in FiniteChecks.lean. This finite algebra check is not a formalization of the probabilistic proof.

## Proposition 4: local mean inequality (self-contained)

Fix a free vertex v and condition on every other coordinate. Its four neighbors have fixed heights b_1,...,b_4≥0, including grounded heights if any. Its conditional density on s≥0 is proportional to exp(−U(s)), where U(s)=Σ_{j=1}^4 V(s−b_j). For every s,b≥0,
    V'(s−b)=V'(s)−∫_{s−b}^s V''(t)dt
            ≤c_+s−c_-b.
This uses V'(0)=0 and V'(s)≤c_+s. Thus
    U'(s)≤4c_+s−c_-Σ_j b_j.
Let k=4c_+, m=(c_-/(4c_+))Σ_j b_j and Q_m(s)=k(s−m)²/2. Then U'(s)≤Q_m'(s), so the density ratio exp(Q_m(s)−U(s)) is nondecreasing on [0,∞).

Here is the elementary likelihood-ratio comparison in full. If ν is the normalized density exp(−Q_m) on [0,∞) and r is the density ratio before normalization, r is positive increasing and ∫r dν<∞. For bounded increasing f,
    Cov_ν(f,r)= (1/2)∫∫(f(s)−f(t))(r(s)−r(t))ν(ds)ν(dt)≥0.
It follows that E_ν[fr]/E_ν[r]≥E_ν f. Taking f(s)=min(s,M) and passing M→∞ proves that the conditional mean under exp(−U) is at least the mean under ν. Finally
    ∫_0^∞(s−m)exp(−k(s−m)²/2)ds
       = exp(−km²/2)/k>0,
so E_ν s≥m. This proves
    E[φ_v | other coordinates] ≥ α Σ_{w~v} φ_w,
    α=c_-/(4c_+)>0.
Averaging gives m_N(v)≥α Σ_{w~v}m_N(w), and in particular m_N(v)≥α m_N(w) for each adjacent free w. All expectations are finite by coercivity. On a graph of degree d the identical proof uses α=c_-/(dc_+).

## Proposition 5: existence reduces to a single neighboring mean bound

Explicit external input BL: the Brascamp–Lieb variance inequality for a smooth strongly convex density, extended to a convex support, says Var(F)≤E[∇Fᵀ(∇²H)^{-1}∇F]. In the present model ∇²H≥c_-L. To justify the orthant version, replace its indicator by exp(−Σ_v k g(−φ_v)), with g(t)=(max(t,0))^4. g is convex and C². Apply the ordinary full-space BL inequality to H+Σ k g(−φ_v); the Hessian is still ≥c_-L. Let k→∞; Gaussian domination gives convergence of normalization and first and second moments, and therefore the linear-function variance inequality passes to the orthant. Thus
    Var_{μ_N^+}(φ_i)≤R_N(i)/c_-≤||i||_1/c_-.
The last resistance bound comes from the fixed path to 0. It is independent of N once the path is included.

Let e=(1,0). Assume ONLY
    M:=sup_{N≥1} m_N(e)<∞.                       (missing estimate A)
For any fixed i≠0, choose a finite nearest-neighbor path e=v_0,...,v_ℓ=i that avoids 0. Such a path exists because Z²\{0} is connected: a path meeting 0 can replace the entering and exiting segments by a detour along the eight-vertex perimeter of [-1,1]^2 intersect Z^2, which avoids 0. For N large enough this path lies in Λ_N. Repeatedly apply Proposition 4 in the direction m_N(v_j)≥α m_N(v_{j+1}); this gives
    m_N(i)≤α^{-ℓ}m_N(e)≤α^{-ℓ}M.
Finitely many smaller N do not matter. Therefore every fixed coordinate has uniformly bounded means and, by BL, uniformly bounded second moments.

These bounds give tightness of every finite-coordinate marginal by Markov's inequality and a union bound. Tightness in the countable product follows by enumeration of vertices: choose coordinate cutoffs with probabilities summing to less than any given ε; the product of the compact coordinate intervals is compact in the product topology. Take a weakly convergent subsequence. Proposition 1 implies uniqueness of any subsequential limit: expectations of bounded continuous increasing cylinder functions are increasing in N, so all subsequential limits have the same expectations for these functions. Such functions determine finite-dimensional distributions (approximate indicators of upper orthants by bounded continuous increasing products), hence determine the product measure. Thus the whole sequence converges to a proper field with φ_0=0 and nonnegative finite heights.

The second-moment bounds give uniform integrability, so E φ_i=lim_N m_N(i). The Gibbs specifications pass to the limit as well: for a bounded continuous local F, its conditional expectation under a finite wall specification is bounded and continuous in its finitely many boundary values, by Gaussian-tail domination locally uniformly in those values. Apply the finite-volume DLR identity to products of F with bounded continuous cylinder functions outside its region and pass to weak limits. A monotone-class argument extends this identity to measurable test functions. The limit is a pinned positive Gibbs field.

Conversely, if m_N(e) is unbounded, domain monotonicity makes it tend to +∞. With B=1/c_- the BL bound and Chebyshev give, for any K and m_N(e)>K,
    μ_N^+(φ_e≤K)≤B/(m_N(e)−K)²→0.
It cannot have a proper tight marginal at e. Thus proper convergence of this exhaustion is equivalent to estimate A. This equivalence is a reduction, not a proof of A.

If estimate A fails, Proposition 4 along paths in the reverse direction implies that all fixed nonzero site means diverge. BL then makes all fixed-site marginals escape to +∞. If A holds, the path argument gives at most an exponential-in-distance upper bound; it does not give C log|i|.

## Remaining gap and verdict

No proper convex-interaction infinite-volume pinned positive field has been constructed here without assuming A. A is the volume-uniform first-moment bound at one neighbor of the pin. Even after A, the established upper bound α^{-ℓ}M is far too weak for the desired logarithmic growth; a sharper spatial bound is still required. Equivalently, a sufficient missing estimate is
    sup_{N large enough to contain i} E_{μ_N^+}φ_i≤C(V)log(2+|i|)
for every fixed i, with the SAME constant C(V). This gives A, existence and the desired upper half; Proposition 2 supplies the lower half. No proof or counterexample for this missing estimate is claimed.

The work establishes finite-volume identities and comparisons, a lower-bound reduction to the existing box theorem, and a one-site existence criterion. It is PARTIAL, not SOLVED and not SOLVED_IN_LITERATURE.


## Hostile referee checklist

- **Incorrect domination direction:** resolved in Proposition 1; growing the domain increases the positive field. This invalidates the old fixed-small-box upper-bound argument.
- **Undefined conditioning at the pin:** avoided by keeping φ_0 fixed in the finite-volume energy, not conditioning on an event of zero probability.
- **Infinite-volume positivity event:** never conditioned upon directly. All constraints are finite-volume; tightness is required for the limiting construction.
- **Boundary signs:** Proposition 4 needs all neighbor heights ≥0. It is applied only to the wall field. No extension to unconstrained or signed boundary heights is asserted.
- **Curvature constants and β:** fixed positive inverse temperature and source edge weights are absorbed into c_±. The proof uses unit nearest-neighbor edges. If weights are used, the local denominator becomes c_+ times the sum of incident weights, and the numerator is the weighted sum times c_-.
- **Logarithm near the origin:** lower-bound statements are only for large distances. A logarithmic upper estimate is formulated with log(2+|i|).
- **Positivity boundary integration:** multiplying by φ_v makes the integration-by-parts boundary term zero at φ_v=0. Integration by parts without that factor would have a wall term and would be invalid here.
- **Weak-limit mean passage:** weak convergence alone does not preserve means. Proposition 2 instead preserves stochastic domination of bounded truncations; Proposition 5 uses uniform second moments to establish uniform integrability.
- **Using Brascamp–Lieb with a wall:** a convex C² soft-wall approximation is given explicitly. The variance bound centers at the actual mean, and thus cannot by itself bound that mean.
- **Borrowed lower-bound theorem:** external input B is precisely the ordinary full-box wall result as stated by the verified survey. A primary-source theorem-number verification of Deuschel–Giacomin was not obtained (publisher fetch forbidden). The finite-volume comparison and its implication are proved here; the literature dependency is explicit.
- **A maximum theorem is not a conditional theorem:** the later Ginzburg–Landau maximum papers concern unconstrained fields. Conditioning on simultaneous positivity is a rare event and destroys a naive application of their tail estimates.
- **Lean scope:** only the three finite algebra lemmas are checked. No FKG, BL, box theorem, DLR construction or open-problem resolution is claimed formally verified.

## Computation (numerical evidence only)

numerics.py integrates a two-free-vertex grounded triangle 0--x--y--0 on the positive quadrant with V(t)=t²/2+ε(1−cos t). For ε=0.3, 0.7≤V''≤1.3. All integrals use product trapezoidal quadrature on [0,10]², at 401 and 801 points per axis, and no more than a few arrays of about 5 MB each. The upper endpoint cutoff and discretization are not interval-certified.

With zero boundary the Euler energy should equal n=2. At the finer grid it is 2.0000215365 (Gaussian) and 2.0000271962 (ε=0.3). The Gaussian mean benchmark is 0.7329037678543798; the finer-grid mean is 0.7328973451029526. For ε=0.3 and the boundary on the edge from y raised from 0 to 0.5 to 1, the finer-grid x means are 0.6592508487, 0.7017270366 and 0.7590288606. These checks support the sign and cancellation in the finite formulas. They test neither a growing two-dimensional box nor the missing uniform bound A. numerical_checks.json contains the complete results and model specification.


## Diagnostic proposition 6: the moment and order bounds do not force tightness

This is not a counterexample to the Gibbs model. It checks an invalid possible inference from necessary bounds.

For N>=1, put deterministic height h_N=sqrt(N/2) at every vertex of Lambda_N except 0, with height zero at 0 and outside. Let nu_N be its Dirac law. There are n_N=(2N+1)^2-1=4N(N+1) free sites. The outer boundary has 4(2N+1)=8N+4 free-ground edges, and the origin contributes four more: B_N=8(N+1) nonzero-gradient edges. Free-free gradients vanish. Therefore
    Q(h_N)=B_N h_N^2=8(N+1)(N/2)=4N(N+1)=n_N.
For V(t)=t^2/2, this is exactly the Euler energy identity and both curvature energy bounds in Proposition 3. The resistance inequality holds deterministically. All variances vanish, so the centered variance upper bound holds. Every free vertex has at most four positive neighbors, so
    h_N >= (1/4) sum_(w~v) h_N(w).
This is the averaged lower inequality of Proposition 4. Domain enlargement increases nu_N stochastically, since h_N increases and newly free coordinates are positive. These configurations also satisfy a logarithmic lower bound at large distances, uniformly for N>=2||i||_infinity: h_N>=sqrt(||i||_infinity), which exceeds c log||i||_infinity for sufficiently large distances. Yet the neighboring height tends to infinity.

The nu_N are not Gibbs measures: their single-site conditionals are point masses, whereas the Gibbs conditional is a positive continuous density proportional to exp(-sum_j V(s-b_j)). Thus this example does not contradict the Gaussian result. It shows that the necessary energy, order, centered variance, and averaged local lower bounds alone cannot prove tightness. More Gibbs structure is needed.

Execution audit: an initial relative-path write placed FiniteChecks.lean in the verifier directory by mistake; it was moved into F0073. One premature verification invocation failed because the move preceded file creation; it is not counted as a successful check. The original queued tool session was unavailable on continuation and no successful completion record was found. A fresh ASCII-source verification was therefore submitted through the shared-slot lake wrapper with a 3600-second total timeout. No scheduler or verifier files were changed.


## Final referee audit and closure (2026-10-12)

The continuation repaired an actual serialization error: PowerShell had replaced mathematical characters by question marks in the Lean file, header, edge-check paragraph, and diagnostic example. Pre-repair bytes are preserved locally. The repaired formulas were read against their derivations; no inequality direction or domain condition was changed. The Lean source now uses ASCII Real and <= syntax.

Lean completed successfully with exit code 0. The exact source hash and run metadata are in lean_result.json; output is in lean_stdout.txt and lean_check.txt. The three checked lemmas are edge_euler_cancellation, grounded_path_resistance, and gaussian_edge_monge. They verify algebra over arbitrary real inputs, the resistance inequality on a two-edge grounded path, and the Gaussian edge Monge inequality. The general convex FKG argument, energy integration, variance inequality, limiting argument, and the open problem itself are not formalized.

Rechecked Proposition 1 edge-by-edge: convexity gives the ordered-pair energy inequality, FKG supplies association, and differentiating in a boundary height has the positive covariance sign stated. Domain enlargement thus gives a lower comparison, not an upper bound. Rechecked Proposition 2 directly against source PDF p.22 (text saved in verified_source_p22.txt): the full-box uniformly convex result is explicitly asserted there. Its use here is an external theorem dependency, not a proof reproduced from the primary Deuschel-Giacomin paper. The lower bound passes to any proper weak limit by comparison of bounded truncations, rather than by an unjustified passage of first moments.

Rechecked the orthant Euler identity: the phi_v factor cancels the boundary term at zero. Rechecked the local derivative bound for all s,b>=0, the likelihood-ratio covariance formula, and the positive truncated-Gaussian integral. Rechecked the soft-wall approximation: its convex penalty leaves the grounded Hessian lower bound intact, and full-space Gaussian domination passes first and second moments to the orthant. The variance is centered and alone gives no mean bound. The path argument transfers a bound at one neighbor to all fixed sites; product tightness, monotone uniqueness and second-moment uniform integrability then give a proper Gibbs limit. Conversely, unbounded monotone means plus bounded variance force escape at that neighbor. The deterministic diagnostic violates the Gibbs specification and is explicitly not a counterexample to F0073.

Final verdict: PARTIAL. No exact printed resolution was found in the recorded bounded search, and no full proof or counterexample is claimed. The remaining gap is estimate A (uniform neighboring mean bound) and a spatial upper bound C(V) log(2+|i|), uniform in the outer box size. The finite-volume lower comparison and the one-site existence reduction do not fill that gap. This closes the present attempt.
