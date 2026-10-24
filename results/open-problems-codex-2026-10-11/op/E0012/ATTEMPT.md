# E0012 research attempt — 2026-10-12

## Exact source and scope

Rick Durrett, *Coexistence in stochastic spatial models*, Annals of Applied Probability 19(2) (2009), 477–496, DOI 10.1214/08-AAP590, arXiv:0906.2293. Problem 6, PDF p.14 (printed article p.489): “Show that coexistence is not possible in the colicin model when β1 < β2 and δ1 = δ2 = 1.”

Example 2.3, PDF p.13, specifies rates 0→1: β1 f1; 0→2: β2 f2; 1→0: δ1; 2→0: δ2+γ f1. Here fi is the local fraction of neighbors in state i. We write a=β1, b=β2, g=γ≥0. The survey uses Z^d, usually d=2. Problem 6 gives no explicit large-range or stirring assumption, and no lower bound on g. Its coexistence notion (PDF p.4) is an invariant distribution concentrated on configurations with infinitely many individuals of each type. A convex mixture of two single-species laws is therefore not coexistence.

The proofs below specify their neighborhoods explicitly. They do not settle arbitrary a<b and g≥0.

## Proposition 1: attractiveness (proved)

For any common finite neighborhood with nonnegative normalized weights, the process is attractive in the order 2<0<1.

Proof. Construct independent baseline death clocks of rate 1 at each site, resetting its state to 0. For each directed neighbor edge y→x of weight p(y,x), use type-1 birth arrows at rate a p(y,x), type-2 birth arrows at rate b p(y,x), and toxin arrows at rate g p(y,x). A type-i birth arrow changes a vacant target to i if its source is i; other cases do nothing. A toxin arrow changes a type-2 target to 0 if its source is 1. These give exactly the stated rates.

Each update is an increasing map of its inputs. The reset-to-0 map is constant. For a type-1 arrow, increasing the source can only enable a birth of 1; increasing the target from 2 to 0 can only enable an upward change and increasing it from 0 to 1 leaves the output 1. For a type-2 arrow, increasing the source can only disable a downward birth; the target outputs at 2,0,1 are respectively 2, either 2 or 0, and 1. For a toxin arrow, increasing the source can only enable 2→0; target outputs at 2,0,1 are either 2 or 0, then 0, then 1. Thus every update preserves the coordinatewise order. Sharing the clocks preserves ordered configurations for all times. The infinite-volume construction follows by the usual finite backward dependency exploration, whose size is bounded by a continuous-time branching process with finite rates on any finite time interval. ∎

Audit: the September intake attempt asserted non-attractiveness. That assertion is false for these rates. Its proposed scalar traveling-wave integral is also unjustified: equation (9) is a two-component system, and a scalar bistable-wave identity does not apply without a proved scalar reduction. Its assertion that type 1 always wins is stronger than Problem 6 and is false at g=0 in the usual supercritical competing contact process.

## Proposition 2: an explicit local extinction range (proved)

For nearest-neighbor interactions on Z^d, d≥1, with D=2d neighbors and fi(x)=D^{-1}∑_{y∼x}1{ξ(y)=i}, if 0≤a≤D/(D−1), then for every initial law and every site x,

    lim_{t→∞} P(ξ_t(x)=1)=0.

In particular every invariant law has no type 1 anywhere, and coexistence is impossible. This includes a≤4/3 on Z², for every b and every finite g≥0. It is a special case, not a resolution of E0012.

Proof. First couple the type-1 set with a one-type contact process η of birth parameter a and death parameter 1, started fully occupied. Use the same type-1 arrows and death clocks. Colicin births require a vacant target, whereas the contact process accepts any target lacking η-occupation. Baseline deaths remove a type 1 and the corresponding η-occupation; toxin events and type-2 births cannot create type 1. Induction on local graphical events gives {ξ_t=1}⊆{η_t=1}. Thus it suffices to prove local extinction of this contact process.

The laws μ_t of η started from all occupied sites decrease in stochastic order: the all-occupied initial state dominates its law at time s, and attractiveness then gives μ_{t+s}≤μ_t. On the compact product space {0,1}^{Z^d}, the probabilities of finite all-occupied events decrease to limits; inclusion-exclusion gives convergence of every cylinder probability. These cylinder limits define a probability law μ, and compactness gives weak convergence. The finite-range graphical construction makes the semigroup Feller: a local observable at time s can, with arbitrarily high probability, be determined from a finite set of initial sites, by the nonexplosion of its backward dependency exploration. Consequently μP_s=lim μ_tP_s=lim μ_{t+s}=μ, so μ is invariant. It inherits translation and lattice symmetries from μ_t.

Let ρ=μ(η(0)=1), and q=μ(η(0)=η(e)=1), for a fixed unit neighbor e. Symmetry makes q the same for each neighbor. Stationarity applied to η(0) gives

    ρ=a(ρ−q).                                      (1)

Indeed, deaths contribute −ρ, and births contribute (a/D)∑_{y∼0}μ(η(0)=0,η(y)=1)=a(ρ−q).

Stationarity applied to η(0)η(e) gives

    2q=(a/D)[2(ρ−q)+R],                          (2)

where

    R=∑_{z∼0,z≠e} μ(η(0)=0,η(e)=1,η(z)=1)
      +∑_{z∼e,z≠0} μ(η(e)=0,η(0)=1,η(z)=1).

These are the birth terms at the two endpoints; a death at either occupied endpoint contributes −q. All probabilities in R are nonnegative.

Suppose ρ>0. Equation (1) rules out a=0. We show R>0 rather than merely R≥0, which is needed at the boundary. Choose any neighbor z≠e of 0 (there is one because D≥2). Starting from any configuration with η(e)=1, prescribe during a unit time interval these local graphical events: in the first quarter have deaths at 0 and z and no incoming birth arrows to those sites; in the second quarter have an arrow e→0 and no deaths at 0; in the third quarter have an arrow 0→z and no deaths at 0 or z; in the final quarter have a death at 0, with no arrows into 0. Throughout the interval forbid deaths at e, and after the first quarter forbid deaths at z. Unspecified arrows can all be forbidden at these three targets, except the two prescribed birth arrows. In the first quarter ensure at least one death at each of 0,z; in the indicated birth subintervals ensure at least one prescribed arrow and no other incoming arrows. The final death occurs only in its indicated subinterval. There are finitely many incident clocks, all with finite rates; the prescribed birth clocks have positive rates. These conditions therefore have a fixed probability c>0 independent of the exterior and of the initial states at 0,z. They guarantee η(0)=0,η(e)=η(z)=1 at time 1. Stationarity now implies μ(η(0)=0,η(e)=η(z)=1)≥cρ>0. Hence R>0.

Equations (1),(2) imply q> (a/D)(ρ−q)=ρ/D. Also (1) implies q=(1−1/a)ρ. Dividing by ρ>0 gives 1−1/a>1/D, or a>D/(D−1). This contradicts the assumed range. Thus ρ=0, and the all-occupied contact-process marginal tends to zero. The coupling proves the claimed limit for every initial law. For any invariant colicin law, its one-site type-1 probability must equal its limit and is zero; countable union over sites shows that no type 1 is present anywhere almost surely. ∎

Referee checks: (i) only the dominating contact-process invariant law needs lattice symmetries, not the colicin initial law; (ii) all generator observables are bounded cylinder functions with bounded rates; (iii) R>0 is explicitly established, so equality at D/(D−1) is covered; (iv) no type-2 death-rate inequality is used; (v) this argument does not say anything about supercritical a beyond this explicit bound.

### Quantitative corollary: explicit exponential extinction below the bound (proved)

For 0≤a<D/(D−1), the same domination actually gives, for every initial law and every site,

    P(ξ_t(x)=1) ≤ exp(−κt),
    κ=[D−(D−1)a]/(D+a)>0.                         (5)

Proof. For the dominating contact process started fully occupied, let ρ(t)=P(η_t(0)=1), q(t)=P(η_t(0)=η_t(e)=1). Its translation and nearest-neighbor symmetries hold at all times. The time-dependent generator identities, obtained exactly as above, imply

    ρ'=(a−1)ρ−aq,
    q'≥−2q+(2a/D)(ρ−q).

Set c=aD/[2(D+a)] and F=ρ−cq. In this parameter range 0≤c<1/2 (at the endpoint c=1/2), so (1−c)ρ≤F≤ρ, since 0≤q≤ρ. Because c≥0,

    F'≤(a−1−2ca/D)ρ+[−a+2c(1+a/D)]q
       =−κρ≤−κF.

The equality is direct substitution of c and κ. Gronwall's inequality, or differentiating e^{κt}F(t), gives F(t)≤F(0)e^{−κt}. Full occupation gives ρ(0)=q(0)=1 and F(0)=1−c. Hence ρ(t)≤e^{−κt}. Coupling proves (5). Bounded cylinder observables have differentiable expectations under these bounded finite-range rates, justifying the generator identities at every t. ∎

This avoids taking a stationary limit below the endpoint and supplies a checkable rate. The endpoint a=D/(D−1) still requires the strict stationary argument in Proposition 2.

### Extension to every uniform finite symmetric neighborhood (proved)

Let N⊂Z^d\{0} be finite, symmetric under sign reversal, and have D=|N|≥2; put fi(x)=D^{-1}∑_{e∈N}1{ξ(x+e)=i}. Proposition 2 and its exponential corollary remain true with this D, even when the neighbors belong to distinct rotation orbits.

Proof. Domination and existence of the contact-process upper invariant law are unchanged. For either its stationary law or its law at time t from full occupation, define qe=P(η(0)=η(e)=1), and q̄=D^{-1}∑_{e∈N}qe. Translation invariance gives P(η(e)=0,η(0)=1)=ρ−qe; reversing edges is permitted because N=−N. Thus the one-site identity uses q̄:

    ρ'=a(ρ−q̄)−ρ.

For each e∈N, its pair-generator identity is

    qe'=−2qe+(a/D)[2(ρ−qe)+Re],

where Re is the sum of the remaining nonnegative triple probabilities for births into the two endpoints, exactly as in (2) but with the neighborhood N. Averaging gives

    q̄'=−2q̄+(2a/D)(ρ−q̄)+(a/D²)∑_{e∈N}Re.

If the stationary ρ>0 and a>0, choose e,z∈N with z≠e and prescribe the same births e→0→z and final death at 0. Symmetry ensures both arrows are present. That finite event proves Re>0, hence the averaged stationarity equation gives q̄>ρ/D. The one-site equation gives q̄=(1−1/a)ρ, again forcing a>D/(D−1). This proves extinction up to the boundary. In the transient case the nonnegative triple sum gives precisely the lower bound on q̄' used in the quantitative proof; replacing q by q̄ throughout yields the same κ and c and hence the same exponential estimate. No rotational symmetry is required. ∎

This covers the uniform finite Euclidean-ball neighborhood of Lanchier–Mercer, although the explicit bound approaches 1 as its degree grows.

## Proposition 3: interior mean-field equilibrium is a saddle (proved algebraically)

The mean-field equations are x'=x[a(1−x−y)−1], y'=y[b(1−x−y)−1−gx]. For 0<a<b and g>0, an interior equilibrium must have

    x*=(b−a)/(ag),  y*=(a−1)/a−(b−a)/(ag).

It exists exactly when a>1 and g>(b−a)/(a−1). To see this, the first equilibrium equation gives 1−x−y=1/a, and the second then gives gx=b/a−1. The displayed formulas follow; x*>0 automatically, and y*>0 is exactly g(a−1)>b−a, which also forces a>1. Conversely these inequalities give x*,y*>0 and x*+y*=1−1/a<1, and substitution verifies both equations. If g=0, the two equations would require a=b, so there is no interior equilibrium in the question's range.

At an interior equilibrium the Jacobian is

    J=[−ax, −ax; −(b+g)y, −by],

with determinant −agxy<0. Its characteristic polynomial has discriminant tr(J)^2−4 det(J)>0, hence two real roots whose product is negative. Thus one eigenvalue is positive and one negative. This confirms instability but is not a spatial noncoexistence proof.

## Proposition 4: a stationary interface reduction (proved)

Suppose a,b>0 and g<∞, and μ is a translation-invariant stationary law for the nearest-neighbor model. Put ρi=μ(ξ(0)=i), qii=Eμ[1{ξ(0)=i}fi(0)], and h=Eμ[1{ξ(0)=1}f2(0)]. Translation invariance and symmetry of the neighborhood imply h=Eμ[1{ξ(0)=2}f1(0)], by reversing and translating each directed edge. The same argument gives Eμ[1{ξ(0)=0}fi(0)]=Eμ[1{ξ(0)=i}f0(0)]=ρi−qii−h for i=1,2. The one-site generator identities therefore give exactly

    q11+h=(1−1/a)ρ1,
    q22+(1+g/b)h=(1−1/b)ρ2.                 (3)

All qii are nonnegative, so

    0≤h≤min{(a−1)ρ1/a, (b−1)ρ2/(b+g)}.     (4)

Moreover, if μ gives positive probability to configurations containing at least one individual of each type, then h>0. Proof: the joint-presence event is the countable union of events ξ(x)=1,ξ(y)=2 with x≠y. One such event has positive μ-probability. Choose a simple nearest-neighbor path from x to y. In a finite time interval, prescribe baseline deaths at its internal vertices, forbid their other incoming birth arrows, preserve the endpoint types, then prescribe successive type-1 birth arrows along the path up to the neighbor of y. Forbid baseline deaths on the growing occupied path and forbid all toxin arrows into y. All relevant clocks are finite in number and have finite rates; prescribed type-1 arrows have positive rates. The event has a uniform positive probability conditional on the initial joint-presence event, and results in an adjacent 1,2 pair. Stationarity gives positive probability for that pair. Translating it to an edge incident to 0 implies h>0. If x,y were already adjacent, simply preserve them over the interval. This proves the assertion. Consequently proving h=0 for every such μ would exclude coexistence (and would exclude all simultaneous presence), even though positive ρ1 and ρ2 alone could also arise from a mixture of single-species laws. ∎

This reduction does not prove h=0. The balance equations allow positive interface density. For example take a=3,b=4,g=5/2, ρ0=1/2,ρ1=ρ2=1/4 and the following symmetric one-edge probability table, with rows/columns 0,1,2:

    [31/96,  1/12,   3/32;
      1/12,  7/60,   1/20;
      3/32,  1/20,  17/160].

Every entry is positive, the marginals are exactly the chosen ρi, and (3) holds with h=1/20. This is only feasibility of the one-site balance constraints. No spatial invariant measure realizing these entries is constructed or claimed. It demonstrates a precise obstruction to a proof based solely on these two stationary first-moment equations.

## Bounded finite-torus counterexample search (numerical evidence only)

simulate.py implements the continuous-time finite-state chain on a 24×24 periodic square lattice using Gillespie sampling. A vacant site's rate is (a k1+b k2)/4, a type-1 site's rate is 1, and a type-2 site's rate is 1+g k1/4. A Fenwick tree samples a site proportionally to its rate; a vacant site's birth type is sampled in the corresponding a k1:b k2 ratio. Each change updates the neighbor counts and the five affected rates. Periodic checks compare all cached neighbor counts against the actual configuration, all population counts against direct counts, and the tree total against the sum of rates. This is the exact Gillespie algorithm implemented in floating-point arithmetic, not an approximation by time steps. Each run was capped at 55 wall seconds and 2,000,000 events, with target model time 3000; memory is well below 1 GB. Initial states were independent equal-probability types 1 and 2, with no vacancies. Each result was appended immediately to simulations.jsonl.

All four runs ended at loss of a species before the caps, at a=1.8,b=4:

| g | seed | time of loss | final (vacant, type 1, type 2) | events |
|---|---|---:|---|---:|
| 20 | 1201 | 118.253896 | (175,0,401) | 87011 |
| 20 | 1202 | 82.380673 | (164,0,412) | 56474 |
| 100 | 1203 | 15.658672 | (407,169,0) | 6259 |
| 100 | 1204 | 1.637277 | (328,248,0) | 1094 |

No finite-run counterexample lead emerged. These observations cannot prove an infinite-volume exclusion result, estimate a rigorous critical toxin value, or identify a spatial invariant law. Finite chains eventually lose both species regardless of infinite-volume coexistence. The different remaining types also reinforce why 'type 1 always wins' is not the question.

## Remaining work

Verification files: checks.py and checks_result.json contain the successful finite checks (144 monotonicity comparisons, 48 pair-generator cases, 16 rational exponential-certificate parameter pairs and exact positive-table balances). The initial Algebra.lean check failed because the narrow imports did not define ℝ, producing typeclass errors; its failed output is retained in lean_result.txt and is not a certificate. The explicit Mathlib.Data.Real.Basic import has been added. verify_lean.py now checks LocalMaps.lean (decide +kernel on the finite update maps) and the corrected Algebra.lean sequentially, each with a one-hour timeout. Only return code zero in lean_checks.json and the corresponding .lean.log can justify a Lean-checked designation. REFEREE.md records the scope and failure-point audit.

The 2023 paper arXiv:2305.17016 has now been inspected. Theorem 1 proves species 2 wins for sufficiently small g when b>a>βc. Theorem 2 proves species 1 survives for sufficiently large g, but proves species 1 wins only when d=M=1. PDF p.5 explicitly conjectures the absence of coexistence, with a possible measure-zero exceptional region. Its abstract's threshold description must not be mistaken for a complete theorem. The proposed phase diagram (9) on PDF p.6 relies on the preceding conjecture.

The published version has also now been downloaded and inspected: Lanchier–Mercer, ALEA 21 (2024), 321–343, Theorems 1.1 and 1.2 on p.324 give the same partial conclusions. Printed p.327 explicitly states: “However, the absence of a phase of coexistence in the spatial model is still an open problem.” Theorem 1.4 (p.326) additionally gives species-2 victory for sufficiently large b at fixed a,g, but does not cover all parameters. See LITERATURE.md for exact quotations and limits.

The full range a<b with a>D/(D−1) and arbitrary g is not proved by this attempt. In particular for b>a>βc in d=2, type-1 survival at large g does not imply type-2 extinction. At intermediate inhibition strengths, the relation between the two survival thresholds remains uncontrolled. Numerical or finite-box absorption evidence would not close this infinite-volume gap.
