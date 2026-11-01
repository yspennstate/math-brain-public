from pathlib import Path
p=Path('ATTEMPT.md')
with p.open('a',encoding='utf8') as f:
 f.write(r'''

## Proposition 1: finite-volume boundary and domain monotonicity

All finite graphs below have a nonempty grounded set meeting every component. The free coordinates are in [0,∞). Nonnegative boundary heights are allowed. Densities are integrable and have all moments: V(t)≥c_-t²/2 and the grounded Dirichlet Laplacian is positive definite; linear boundary terms do not destroy coercivity.

For two different free coordinates x,y, the mixed derivative of log density is V''(φ_x−φ_y)≥0 when they are adjacent, and zero otherwise. Consequently the density satisfies the lattice condition f(a∨b)f(a∧b)≥f(a)f(b). To check it without assuming differentiability at the orthant boundary, integrate the mixed derivatives over rectangles in the interior and then use continuity; decompose a general pair into coordinate swaps. The orthant is closed under coordinate minimum and maximum. The continuous FKG association theorem therefore applies: Cov(F,G)≥0 for bounded increasing F,G. This use of the standard FKG theorem is an explicit external theorem, not a newly proved theorem.

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

Thus every proper weak limit satisfies E φ_i≥c log||i||_∞: apply bounded truncations min(φ_i,K), pass to weak limits, and let K→∞. Equivalently, domain monotonicity and the limit construction in Proposition 5 yield the same statement. This does not establish the existence of a proper limit.

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
For any fixed i≠0, choose a finite nearest-neighbor path e=v_0,...,v_ℓ=i that avoids 0. Such a path exists because Z²\{0} is connected: a path meeting 0 can replace the entering and exiting segments by a detour around the unit square boundary. For N large enough this path lies in Λ_N. Repeatedly apply Proposition 4 in the direction m_N(v_j)≥α m_N(v_{j+1}); this gives
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
''')
print('Proofs saved')
