# C0119: Gaussian disorder chaos — complete argument

Date: 2026-10-12. This note uses two explicitly cited, downloaded variance theorems. It proves the remaining chaos implication and a low-temperature baseline estimate in full. It does not assert novelty, and does not classify a variance theorem as an exact printed chaos theorem.

## 1. Statement and scope

**Source model.** Fix lattice dimension k≥3. Let P_n be all paths p=(v_0,…,v_{n−1}) in Z_+^k, with v_0=0 and v_{i+1}−v_i one of e_1,…,e_k. Give vertices iid N(0,1) weights X_v. Set H_p(X)=Σ_{v∈p}X_v and M_n=max_p H_p. Let P_n(X) be the unique maximizing path (a.s.). Couple X^t=e^{−t}X+sqrt(1−e^{−2t})Y, where Y is an independent copy. We prove

    E|P_n(X) ∩ P_n(X^t)| / n ≤ C_k / ((1−e^{−t}) log n),  n≥3, t>0.      (1)

Thus for *every* positive sequence t_n→0 with t_n log n→∞, the left side tends to zero. In particular t_n=(log n)^{−1/2} works. Each coordinate perturbation has mean square 2(1−e^{−t_n})→0. This answers the exact question in Chatterjee Section 12(2), interpreted through its Section 8 model and overlap definition. It also holds for k=2; k=1 fails.

**Conventional finite-temperature model.** Fix spatial dimension d≥1 (in particular d≥3) and fixed β>0. Paths s=(s_0,…,s_{n−1}) start at 0 in Z^d and take nearest-neighbor steps. Disorder is iid standard Gaussian on time-sites (i,x). Set H_s=Σ_{i=0}^{n−1}X_{i,s_i}, Z_n=Σ_s exp(βH_s), and μ_{n,X}(s)=exp(βH_s)/Z_n. Conditional on environments, sample s and s' independently from μ_{n,X} and μ_{n,X^t}. Define

    R_n(s,s') = Σ_{i=0}^{n−1} 1{s_i=s'_i},
    Q_n(t) = E[(μ_{n,X}⊗μ_{n,X^t})(R_n)].

We prove, with C=C(d,β),

    Q_n(t)/n ≤ C / ((1−e^{−t}) log n),                              (2)
    Q_n(0)/n ≥ 1 − sqrt(2 log(2d))/β.                               (3)

In particular at each fixed β>sqrt(2 log(2d)), original replicas have a positive uniform mean overlap fraction, whereas replicas from arbitrarily slightly perturbed environments have vanishing mean overlap fraction along every t_n as above. This is disorder chaos at low temperature in the usual lattice Gaussian polymer. Bound (2) actually holds at every fixed positive β; the low-temperature condition distinguishes chaos from already-small overlap. We do not claim that the numerical temperature threshold is sharp.

**Scope distinction.** The source specifies Gaussian disorder and a zero-temperature measure concentrated on a ground state; its literal open question does not specify a finite β or a general disorder law. We prove that question, plus the conventional finite-temperature Gaussian formulation above. We do not claim finite-temperature results for all disorder distributions, temperature perturbations, continuum polymers, constrained endpoints, or finite-temperature positive-coordinate paths in every dimension. Those are different additional statements. The all-dimensional nearest-neighbor space-time ground-state version also follows from Graham's second variance bound by the same proof.

## 2. Finite-dimensional Gaussian identity

Only finitely many vertices can be used at fixed n. Let J denote their union, m=|J|, γ_m standard Gaussian measure, and X,Y independent γ_m vectors. For a smooth f:R^m→R whose gradient is bounded and whose higher derivatives have at most polynomial growth, define the OU operator

    (T_t f)(x)=E_Y f(e^{−t}x+sqrt(1−e^{−2t})Y).

This operator preserves γ_m: the argument is again standard Gaussian if x is. The semigroup law T_a T_b=T_{a+b} follows by combining independent Gaussian vectors and their variances. It is self-adjoint in L²(γ_m), since the joint Gaussian law of (X,X^t) is invariant under interchanging the two components. Jensen plus invariance gives ||T_t h||_2≤||h||_2 for h∈L². Also

    ∂_j T_t f=e^{−t} T_t(∂_j f).                                  (4)

These statements follow directly from the definition, differentiating under the expectation in (4). Write L=Δ−x·∇. Gaussian integration by parts, obtained by integrating each coordinate against density (2π)^{−1/2}exp(−x_j²/2), gives

    ∫ u L v dγ_m = −∫ ∇u·∇v dγ_m.                                (5)

The boundary terms vanish by the Gaussian density and the growth assumptions. Differentiating the Gaussian integral defining T_t and integrating by parts in Y gives ∂_t T_t f=L T_t f for t>0. For clarity, if a=e^{−t}, b=sqrt(1−a²), direct differentiation gives −a x·E∇f(ax+bY)+(a²/b)E[Y·∇f(ax+bY)]; integration by parts in Y replaces the second term with a² EΔf(ax+bY), exactly L_x T_t f.

Let C_f(t)=E[f(X)f(X^t)]−(Ef(X))²=∫ f T_t f dγ_m−(Ef)². Equations (4)–(5) give

    C_f'(t)=−e^{−t}Σ_j E[∂_j f(X) ∂_j f(X^t)].                    (6)

Because f is Lipschitz, f(X^t)→f(Y) in L² as t→∞ (bound its difference by its Lipschitz constant times ||X^t−Y|| and take second moments). Hence C_f(∞)=0 and C_f(0)=Var(f). Integrating (6) yields

    Var(f)=∫_0^∞ e^{−t} A_f(t) dt,
    A_f(t):=Σ_j ⟨∂_j f,T_t ∂_j f⟩_2.                            (7)

By self-adjointness and the semigroup property,

    A_f(t)=Σ_j ||T_{t/2} ∂_j f||²_2.

It is nonnegative and nonincreasing: for u≥t, T_{u/2}=T_{(u−t)/2}T_{t/2} and use contraction. Therefore for each t>0,

    Var(f) ≥ ∫_0^t e^{−s}A_f(t) ds = (1−e^{−t})A_f(t).            (8)

Nothing here uses spatial dimension or strong disorder.

## 3. Application to Gibbs measures and to the maximum

For any finite family of n-vertex time-directed paths, write a_{p,j}=1 if p visits time-site j, and 0 otherwise. Each path visits n distinct coordinates, so Σ_j a_{p,j}=n. Allow deterministic positive prior weights w_p; they cancel in the gradient formulas. Set

    G_β(X)=β^{−1}log Σ_p w_p exp(β Σ_j a_{p,j}X_j).

It is smooth. Its derivatives are Gibbs cumulants of finitely many bounded indicators, so the smoothness/growth hypotheses in Section 2 hold. Direct differentiation gives

    ∂_j G_β(X)=p_j(X):=Σ_p μ_X(p)a_{p,j} ∈[0,1],
    Σ_j p_j(X)=n.

In particular ||∇G_β||²≤n, so G_β is sqrt(n)-Lipschitz. Conditional independence of the two replicas gives

    (μ_X⊗μ_{X^t})(R)=Σ_j p_j(X)p_j(X^t).

Thus A_{G_β}(t)=Q(t), and (7)–(8) become

    Var(G_β)=∫_0^∞ e^{−t}Q(t)dt,
    Q(t)≤Var(G_β)/(1−e^{−t}).                                    (9)

Equivalently Var(log Z)=β²∫ e^{−t}Q(t)dt. Q is nonincreasing, 0≤Q≤n. No assumption about endpoint overlap is needed.

For the maximum use w_p=1 and let β→∞ at fixed n. If K is the finite number of paths, the elementary log-sum-exp estimate is

    M(X) ≤ G_β(X) ≤ M(X)+(log K)/β.                               (10)

Hence G_β→M in L², and their variances converge. Distinct directed paths have distinct coordinate incidence vectors, so H_p−H_q is a nondegenerate centered Gaussian when p≠q. Its probability of being zero is zero. A finite union proves a unique maximizing path a.s. Consequently p_j(X)→a_{P(X),j} a.s.; also this holds for X^t, whose marginal is standard Gaussian. Bounded convergence applies to the finite sum over J. In (9) pass to β→∞ to obtain

    Q_∞(t):=E|P(X)∩P(X^t)| ≤ Var(M)/(1−e^{−t}).                  (11)

One can also pass under the integral in (9), dominated by n e^{−t}, to retain the exact variance identity. No differentiation of a nonsmooth maximum was assumed.

**Equivalence useful for auditing.** For either observable, if Var(G_n)=o(n), choose a_n=max(Var(G_n)/n,1/n), t_n=sqrt(a_n). Then t_n→0 and (9) implies Q_n(t_n)/n→0, since 1−e^{−t_n}≥t_n/2 for sufficiently large n. Conversely, if t_n→0 and Q_n(t_n)=o(n), monotonicity and Q≤n yield

    Var(G_n) ≤ n(1−e^{−t_n})+e^{−t_n}Q_n(t_n)=o(n).

The variance conclusion is not a consequence merely of a positive same-environment overlap; it is equivalent to the existence of noise chaos in this precise normalized-overlap sense.

## 4. Ground-state source model: use of Graham's theorem

Graham Theorem 6.1 (graham.pdf, p. 14; quoted in LITERATURE.md) applies to iid standard Gaussian weights on Z^k, k≥2. Extend the source's weights on Z_+^k to all of Z^k with independent Gaussian coordinates. This does not change any path from 0 with positive steps. With N=n−1, all such paths end in S_N and Graham's convention excludes the origin. Therefore exactly

    M_n(X)=X_0+T(0,S_{n−1}).

The second term does not depend on X_0. Independence gives

    Var(M_n)=1+Var(T(0,S_{n−1}))≤C_k n/log n, n≥3,               (12)

after increasing C_k to handle finitely many small n. Combining (11)–(12) proves (1). Since 1−e^{−t}≥t/2 for 0<t≤1, every t_n→0 with t_n log n→∞ proves vanishing overlap. A Markov bound gives P(|P_n∩P_n^{t_n}|>εn)→0 for each fixed ε>0. Ground-state measures are delta masses, and the unperturbed overlap is exactly n. Thus this is a nontrivial change of the polymer configuration, not a high-temperature absence of overlap.

In fact P(P_n(X)=P_n(X^{t_n}))≤E|P_n(X)∩P_n(X^{t_n})|/n→0, since equality of paths forces overlap n. With total variation defined as sup_A|μ(A)−ν(A)|, the total variation between the two ground-state delta measures tends to 1 in probability and in mean. This explicitly gives sensitivity of the measure itself.

The same bookkeeping applies to Graham's hat graph: N transitions, N weighted vertices after excluding the origin, free endpoint. Add the independent origin coordinate and use the second estimate in Theorem 6.1. It covers every spatial dimension at least one, including d≥3.

## 5. Finite temperature: variance input and exact indexing

Chatterjee's Theorem 2.4(3), surface_growth.pdf, p. 9, gives Var(f(n,0))≤C n/log n for every fixed spatial d≥1 and fixed β>0. In its Section 2.4, f(n,0) has the same law as β^{−1}log Z_n in the nearest-neighbor Gaussian polymer.

There is a minor indexing convention to check explicitly. That paper sums over paths (p_0,…,p_n) with n transitions, but assigns energy only to p_0,…,p_{n−1}. For each path in our definition there are exactly 2d possible final unweighted steps. Thus its Z_n=(2d)Z_n^{ours}; normalized laws on the first n weighted vertices coincide. Adding β^{−1}log(2d) to G_β is deterministic and does not change variance, gradients, or overlaps. The paper's time-reversal representation uses n independent time layers, so its equality in law requires no assumption about reversibility of a quenched polymer measure. Variance is a single-environment law and equality in law suffices.

Standard Gaussian disorder is the identity Lipschitz image required by that theorem. Therefore

    Var(G_{n,β})≤C(d,β)n/log n.                                  (13)

Substitution in (9) proves (2), with fixed β. We do not send β to infinity in this theorem; its constants may depend on β. The zero-temperature assertion was proved separately using Graham.

## 6. An elementary low-temperature baseline bound

This proof works for any finite n-vertex family with K≤D^n paths and iid standard Gaussian weights, each path visiting n distinct coordinates. For the nearest-neighbor model D=2d, since K=(2d)^{n−1}. Define U_β(X)=Σ_p μ_X(p)H_p(X). Then

    U_β(X)=Σ_j X_j p_j(X).

Differentiating a Gibbs average gives

    ∂_j p_j(X)=β(Σ_p μ_X(p)a_{p,j}²−p_j(X)²)
               =β(p_j(X)−p_j(X)²),

using a_{p,j}²=a_{p,j}. Gaussian integration by parts is legitimate because p_j is bounded and its derivative is bounded by β. Hence

    EU_β=Σ_j E∂_j p_j = β(n−Q(0)).                              (14)

Pointwise U_β≤M:=max_p H_p. For every λ>0, e^{λM}≤Σ_p e^{λH_p}; each H_p is N(0,n), regardless of correlations among paths. Jensen and the normal moment-generating function give

    λ EM ≤ log E e^{λM} ≤ log K+λ²n/2.

For K>1 choose λ=sqrt(2 log K/n), obtaining EM≤sqrt(2n log K)≤n sqrt(2 log D). If K=1, EM=0 directly. Combining with (14) gives

    Q(0)/n ≥ 1−sqrt(2 log D)/β.                                 (15)

For β>sqrt(2 log D), c=1−sqrt(2 log D)/β>0 is independent of n. Equations (2) and (15) imply Q_n(t_n)/Q_n(0)→0. They also imply annealed high-overlap probability for same-environment replicas is bounded away from zero: since R/n∈[0,1] and ER/n≥c,

    P(R/n>c/2)≥c/(2−c).

Indeed ER/n≤c/2+(1−c/2)P(R/n>c/2). In perturbed environments this probability tends to zero by Markov. For the quenched quantity A_n(X,Y)=(μ_X⊗μ_{X^{t_n}})(R/n>ε), EA_n≤Q_n(t_n)/(εn)→0, so A_n→0 in probability as a function of the environment. We assert this precise sense of chaos, rather than unspecified total-variation convergence of random measures.

There is also a direct finite-temperature measure-sensitivity conclusion. For each fixed X define f_X(s')=Σ_s μ_X(s)R(s,s')/n, so 0≤f_X≤1. For probability measures on the finite path space, |∫f_X dμ_X−∫f_X dμ_{X^t}|≤TV(μ_X,μ_{X^t}). To verify this inequality directly, write δ(s)=μ_X(s)−μ_{X^t}(s); Σ_sδ(s)=0 and Σ_{δ>0}δ=TV. Since 0≤f_X≤1, both the positive and negative parts of Σ_s f_X(s)δ(s) are at most TV. Taking expectations therefore gives

    E TV(μ_X,μ_{X^t}) ≥ (Q_n(0)−Q_n(t))/n.                     (16)

At every fixed β>sqrt(2 log(2d)), along the noise sequences in Section 1,

    liminf_n E TV(μ_{n,X},μ_{n,X^{t_n}}) ≥ 1−sqrt(2 log(2d))/β>0.

This is a quantitative change of the measure under a coordinatewise vanishing perturbation. It does not assert TV→1 at fixed finite β. The lower bound approaches 1 in the iterated limit of n→∞ followed by β→∞.

## 7. Boundary case and a failed earlier inference

For k=1 positive-coordinate paths there is only one path. Its Gibbs law is the same for every β and environment. M_n=Σ_{i=0}^{n−1}X_i, Var(M_n)=n and Q_n(t)=n for every t≥0. There is no chaos. The variance identity is exactly n=∫_0^∞e^{−t}n dt. This disproves the abstract inference "positive path overlap implies a BKS logarithmic variance gain." In general a strongly localized deterministic path has maximal overlap and linear variance. Geometry or another independent variance input is essential.

This boundary counterexample is not a counterexample to the d≥3 problem. In the actual models above the necessary geometry is supplied by the published variance results.

## 8. Referee checklist and verification

- Source hypothesis: iid Gaussian, ground state, free endpoint. Checked against source pp. 37–38 and exact question p. 59. The intake's finite-temperature wording is explicitly separated.
- Source vs standard space-time graph: Graham Theorem 6.1 states both, so no higher-dimensional rotation argument is used.
- Origin included vs excluded: independent origin contributes variance 1 and overlap 1; accounted for in (12).
- Distinct-path ties: their incidence vectors differ; Gaussian differences have strictly positive variance. Finite union of null events.
- OU monotonicity: follows from self-adjointness, semigroup and contraction of each gradient coordinate, not positivity of individual path covariance estimates.
- Gibbs overlap equals gradient product: conditional independence and time-site indexing verified in Section 3.
- Smooth-to-max passage: uniform bound (10), a.s. unique maximizer, bounded convergence; constants are not passed through a β-dependent theorem.
- Fixed β variance input: correct Lipschitz law, dimension and free endpoint verified; final unweighted step factor explicitly accounted for.
- Baseline estimate: (14) is a site-weight IBP, not an unjustified identification of endpoint overlap with path overlap. Maximum bound uses only path count and Gaussian mgf.
- Quantifiers: β and dimension are fixed before n→∞; noise sequences satisfy t_n log n→∞. No optimal chaos scale or temperature threshold is claimed.
- General environment: not asserted; the gradient formula for a nonlinear Lipschitz image would involve F' factors and would not directly equal site overlap.

Computational verification (checks.py, checks_results.json; seed 11920261012): all forward/backward Gibbs marginals summed to 1 to within 1e−10. Thirteen occupancy derivatives in the d=3, n=4, β=2 model were checked by central differences with step 1e−5, with maximum absolute error 2.77e−11. Three 2,500-sample finite-volume experiments used graph dynamic programming, no asymptotic approximation:

| Model | Var(G), estimated | ∫e^{−t}Q(t)dt, estimated (20-point Laguerre) | Q(0) | Q(0.1) | Q(0.5) |
|---|---:|---:|---:|---:|---:|
| Positive-coordinate ground state, k=3, n=10 | 3.37545 | 3.51834 | 10 | 5.8512 | 3.4520 |
| Nearest-neighbor finite temperature, d=3, n=7, β=4 | 2.11918 | 2.13299 | 4.85780 | 3.48599 | 2.07883 |
| One-path boundary, k=1, n=10, β=4 | 10.41725 | 10 exactly | 10 | 10 | 10 |

Sampling and quadrature error are retained; these are illustrations, not certified numerical equalities or an extrapolation in n. The finite-temperature bound (15) is 3.68722 at n=7, β=4, below the estimated Q(0)=4.85780. The initial integration-by-parts residual E[U−β(n−Σp_j²)] was estimated at 0.26850 with standard error 0.11033 (2.43 standard errors from zero). This fluctuation is explicitly recorded; an independent, predetermined 10,000-sample test is run by ibp_check.py, with no quadrature and a different seed, rather than silently treating the initial value as zero. The boundary model residual was 0.02010±0.06455 standard error. The whole original numerical job took 199.38 seconds; layer arrays and batches are far below the 1 GB memory cap.

The independent test (ibp_check_results.json, seed 11920261013, exactly 10,000 samples) gave residual −0.01161 with standard error 0.05578, or −0.208 standard errors, mean energy 8.74145 and mean Q(0)=4.81174. It took 2.92 seconds. No further sampling was performed. Both the analytic derivation and this independent test support interpreting the earlier 2.43-standard-error residual as sampling fluctuation.

OverlapAlgebra.lean formalizes only three real-algebra deductions: normalization of the overlap bound, the low-temperature baseline inequality, and the same-environment probability floor. It imports Mathlib.Data.Real.Basic, Mathlib.Tactic.Linarith, and Mathlib.Tactic.FieldSimp, uses no `sorry`, added axioms, `native_decide`, or full `import Mathlib`. The analytic covariance identity and the cited variance theorems are not Lean-formalized. The first run caught a library-name error in scalar cancellation; after replacing it by a direct contradiction proof, the final file passed `lake env lean ~/brain_workers/TRIO_1011/op/C0119/OverlapAlgebra.lean` from ~/lean_verify, **exit code 0, no diagnostics**. The shared wrapper gives each execution a 3,600-second timeout; runs were sequential. LEAN_CHECK.md records the failure, correction, queue waits and final success. These three algebraic deductions are kernel checked; the remainder is the complete written proof above using the cited prior results.

## 9. Remaining gap

For the source's Gaussian ground-state question and the conventional Gaussian finite-temperature low-temperature formulation precisely stated in Section 1, there is **no remaining mathematical gap**, conditional only on the use of the published theorems as usual prior results. The broader, unspecified phrase "random environment" is not interpreted as a theorem for every probability distribution. Extension to non-Gaussian laws, temperature chaos, sharper rates, or other path geometries is outside the posed source problem and is not proved here.
