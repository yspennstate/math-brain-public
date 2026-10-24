# F0137 mathematical attempt

Date: 2026-10-11. Proved statements below are auxiliary results, not a solution of the open conjecture.

## Exact target

Let d≥2 and let independent Dirichlet(alpha_1,...,alpha_{2d}) outgoing environments be assigned to sites of Z^d, all alpha_i>0, e_{i+d}=-e_i. Set A=sum_i alpha_i, d_alpha=sum_i alpha_i e_i and κ=2A-max_{1≤j≤d}(alpha_j+alpha_{j+d}). For every direction ℓ with d_alpha·ℓ>0, seek the source's (T′), namely finite E0 exp(c_gamma R^gamma) for each 0<gamma<1, where R=sup_{0≤n≤τ1}|X_n|. The weaker intake asks for (T)gamma; a proof for some gamma would already imply the conjectured positive moments s<κ by the source's Theorem 6. The source itself says (T′), as verified in LITERATURE.md. The universal direction phrasing follows the surrounding renewal discussion; the sentence on p.19 does not explicitly specify a direction. No stronger direction quantifier is attributed to the sentence alone.

## 1. Exact annealed path weights

For a finite nearest-neighbor path x_0=0,...,x_N, let n_{x,i} be its number of departures from x in direction e_i, and N_x=sum_i n_{x,i}. With (z)_m=z(z+1)...(z+m-1) and (z)_0=1,

    P0(X_0=x_0,...,X_N=x_N)
      = product_x [ product_i (alpha_i)_{n_{x,i}} / (A)_{N_x} ].       (1)

Proof. Its quenched probability is product_{x,i} omega(x,x+e_i)^{n_{x,i}}. Independence separates the expectation over x. The Dirichlet density normalizing integral gives E product_i omega_i^{m_i} = Γ(A)/Γ(A+sum_i m_i) product_i Γ(alpha_i+m_i)/Γ(alpha_i), which is the displayed rising-factorial expression. This calculation only integrates finitely many sites and requires no limit interchange.

Conditioned on any finite walk history, the outgoing vector at x has Dirichlet parameters alpha_i+n_{x,i}, by multiplying its original density by its likelihood. Consequently the next-step predictive probability is

    (alpha_i+n_{x,i})/(A+N_x).                                    (2)

## 2. Exponential wrong-exit bound for paths with no repeated departure site

This is a proved restriction on an event, not (T) for the whole walk. Fix a unit ℓ with μ=d_alpha·ℓ/A>0. For b,L>0 define T as the first time X_n·ℓ≥L or X_n·ℓ≤-bL. Let S mean T<∞ and X_0,...,X_{T-1} are distinct. Then there is λ>0, depending only on alpha and ℓ, such that

    P0(S and X_T·ℓ≤-bL) ≤ exp(-λ bL).                            (3)

The same λ works for ℓ in a sufficiently small neighborhood of the fixed ℓ.

Proof. On a path with distinct departure sites, every N_x in (1) is either zero or one. Its annealed probability is exactly product_{k=0}^{N-1} alpha_{i_k}/A, which is the path probability of a homogeneous walk Y with independent increments e_i of probabilities p_i=alpha_i/A. Countably many finite first-exit path cylinders are pairwise disjoint. Summing their equal probabilities gives the RWDE restricted wrong-exit probability equal to the homogeneous restricted probability, and therefore at most the homogeneous probability ever to hit Y_n·ℓ≤-bL.

Set m(λ,ℓ)=sum_i p_i exp(-λ e_i·ℓ). This differentiable finite sum has m(0,ℓ)=1 and partial derivative at λ=0 equal to -μ<0. Choose λ>0 with m(λ,ℓ)<1. Continuity gives the same strict inequality in an open neighborhood of ℓ. Thus M_n=exp(-λ Y_n·ℓ) is a nonnegative supermartingale with M_0=1. For H=inf{n:Y_n·ℓ≤-bL}, bounded optional stopping yields E M_{H∧n}≤1 and hence exp(λbL) P(H≤n)≤1, since M_H≥exp(λbL) on H≤n. Taking the increasing limit of P(H≤n) proves (3). This uses no integrability of unbounded stopping times. Overshoot strengthens the displayed inequality. The terminal site need not be new, since there is no departure from it in its cylinder likelihood. QED.

## 3. Necessary regeneration-time moment threshold without (T)

Use the usual first strictly positive regeneration time τ1 in direction ℓ: a regeneration point is a strict record in projection and the path never subsequently has a smaller projection. Any stricter standard record construction has the same obstruction below. Assume τ1 exists a.s., as for directionally transient RWDE. Choose j maximizing alpha_j+alpha_{j+d}, put a=alpha_j, b=alpha_{j+d}, and choose either orientation z=±e_j. For n≥1 let C_n be the cylinder path

    0,z,0,z,...,0  (n complete two-step loops).

Then

    P0(C_n) = (a)_n(b)_n/(A)_n^2
      ~ [Γ(A)^2/(Γ(a)Γ(b))] n^{-κ}.                              (4)

Moreover C_n⊂{τ1>2n}. Therefore for some c>0 and all sufficiently large real t,

    P0(τ1>t) ≥ c t^{-κ},
    E0[τ1^s]=∞ for every s≥κ.                                    (5)

Proof of inclusion. All times at 0 after time zero fail to be strict records. If z·ℓ≤0, the visits to z are not strict records either. If z·ℓ>0, the first visit to z is followed by a return to 0 of smaller projection, so it is not a regeneration; all later visits to z also have subsequent returns to 0, and in addition are not new strict records. Thus no time 1,...,2n is a regeneration. This argument also covers perpendicular strongest traps.

Proof of probability. Only 0 and z have departures, n each, and all use their common edge in opposite directions. Formula (1) gives (4). Positivity alpha_i>0 implies A>a,b and κ=(A-a)+(A-b)>0. For fixed real u, Stirling's formula and log(n+u)=log n+u/n+O(n^{-2}) give log Γ(n+u)=(n+u-1/2)log n-n+(1/2)log(2π)+O(n^{-1}). Subtracting the expressions for u and v gives log[Γ(n+u)/Γ(n+v)]=(u-v)log n+O(n^{-1}). Exponentiating proves Γ(n+u)/Γ(n+v)~n^{u-v}, and applying this twice yields the stated positive constant.

For large t choose n=ceil(t/2); then {τ1>2n}⊂{τ1>t}, and (4) gives the tail lower bound with a changed constant. For s>0 the layer-cake identity, valid also when infinite, is E τ1^s=s∫_0^∞ t^{s-1}P(τ1>t)dt. For s≥κ its integrand is bounded below by cs t^{s-1-κ}, whose integral diverges, logarithmically at s=κ. QED.

This proves only the divergent-moment half of the proposed sharp threshold. During C_n the entire path is in {0,z}; it gives no lower bound on large R and no counterexample to (T)gamma.

For completeness, the **exit time of the pair itself** has the full sharp threshold. Let H=inf{k≥0:X_k∉{0,z}} for a walk started at 0. Since the only internal edge is the common edge, {H>2n}=C_n. Thus P(H>2n) is exactly (4) (with exponent κ_j=2A-alpha_j-alpha_{j+d} for an arbitrary pair). Monotonicity sandwiches the tail at any real t between its adjacent even-integer tails. It is therefore bounded above and below by positive constants times t^{-κ_j} for large t. Applying the same tail integral proves E H^s<∞ exactly when 0<s<κ_j. This proves a finite-trap special case of the proposed moment statement, not the corresponding upper bound for τ1.

## 4. Deterministic finite-trap cut minimization in every dimension

For a finite S⊂Z^d define the directed outgoing alpha-boundary B(S)=sum_{x∈S,i:x+e_i∉S} alpha_i. For every |S|≥2,

    B(S)≥κ,                                                     (6)

and equality is attained by S={0,e_j} when j maximizes alpha_j+alpha_{j+d}. No connectedness hypothesis is needed for the bound.

Proof. Let c_i=alpha_i+alpha_{i+d}. Let q_i(S) be the number of occupied lattice lines parallel to e_i. Each occupied finite line has at least one outgoing +e_i edge at its largest coordinate and one -e_i edge at its smallest coordinate. Hence B(S)≥sum_i c_i q_i(S). Select distinct x,y∈S. Their projections orthogonal to e_i coincide exactly when y-x is a multiple of e_i. This can occur for at most one index i. If it occurs for index j, then q_j≥1 and all other q_i≥2, giving B(S)≥c_j+2sum_{i≠j}c_i=2A-c_j≥κ. If it occurs for no index, every q_i≥2 and B(S)≥2A≥κ. A nearest-neighbor pair in direction j has exactly 2A-c_j outgoing weight, since its two internal directed edges remove alpha_j+alpha_{j+d} from 2A. QED.

For a w-by-h filled rectangle in d=2, B=hP+wQ with P=alpha_1+alpha_3 and Q=alpha_2+alpha_4. Any integer w,h≥1 with wh≥2 has w≥2 or h≥2, so B≥min(P+2Q,2P+Q)=κ. Algebra.lean checks this rectangle inequality, the exponent identity and positivity, and the negative-posterior-drift calculation below. It does not formalize the geometric or probabilistic arguments.

### 4a. A sharp bound at fixed connected-set diameter

There is also a stronger bound for large **connected** sets, which corrects a misleading possible interpretation of the earlier ledger. Put m=A-max_i c_i>0, where positivity uses d≥2. For nonempty finite nearest-neighbor-connected S let D=max_j(max_{x∈S}x_j-min_{x∈S}x_j), its diameter in the infinity norm. Then

    B(S)≥A+mD.                                                   (9)

For each integer D≥0 equality is attainable by a straight segment of D+1 vertices in a direction j maximizing c_j. In particular the minimum outgoing weight of a connected set of diameter D is exactly A+mD.

Proof. Choose a coordinate j whose range equals D. A nearest-neighbor path in S connecting sites with minimum and maximum j coordinates must attain every integer between them. For every i≠j, sites with different j coordinates lie on different lines parallel to e_i. Thus q_i(S)≥D+1 for i≠j; also q_j(S)≥1. The line argument used in (6) yields B(S)≥c_j+(D+1)sum_{i≠j}c_i=A+D(A-c_j)≥A+Dm. For a straight segment along j, the two endpoint outward axial edges have total c_j, while every one of its D+1 vertices has all transverse outward edges, total (D+1)(A-c_j). This is equality. The singleton D=0 has B=A, also consistent. QED.

This concerns outgoing alpha-weight of S, not the integrability exponent of the exit time from S: the latter can still be governed by an internal pair. One must not replace a minimum over trapping subsets by B(S).

There is an exact fixed-set environmental interpretation. For a connected S with at least two vertices, write r_x=sum_{i:x+e_i∉S}alpha_i and u_x=A-r_x. Connectedness implies u_x>0. For r_x>0, the total outgoing boundary probability at x has Beta(r_x,u_x) law by grouping Dirichlet coordinates. Its probability of being at most ε is

    [1/Beta(r_x,u_x)]∫_0^ε t^{r_x-1}(1-t)^{u_x-1}dt
       ~ ε^{r_x}/[r_x Beta(r_x,u_x)] as ε↓0,

because the continuous factor (1-t)^{u_x-1} tends uniformly to 1 on [0,ε]. For r_x=0 the boundary probability is identically zero. Independence of sites gives

    P(all site boundary probabilities in S are ≤ε)
       ~ C_S ε^{B(S)},                                           (10)

with explicit C_S=product_{x:r_x>0}[r_x Beta(r_x,u_x)]^{-1}>0. Formula (9) says these fixed-set exponents grow linearly in diameter. Formula (10) is a limit for a fixed S, not a bound on all mechanisms of backward travel.

In fact, a **uniform single-shape upper bound** can be extracted without taking a limit. Let r_min=min_i alpha_i>0. For each nonempty proper set J of outgoing directions, put r_J=sum_{i∈J}alpha_i, u_J=A-r_J, and

    K=max(1, max_J 2^{max(1-u_J,0)}/[r_J Beta(r_J,u_J)]),
    C=K^{1/r_min}.

Both are finite constants depending only on the fixed alpha-vector: there are finitely many J, and r_J,u_J>0. For 0<ε≤1/2 and 0≤t≤ε, (1-t)^{u_J-1}≤2^{max(1-u_J,0)}. Integrating the beta density therefore gives P(Beta(r_J,u_J)≤ε)≤K ε^{r_J}. If N_b is the number of boundary sites of S, independence gives P(E_S(ε))≤K^{N_b} ε^{B(S)}. Since B(S)≥r_min N_b and K≥1, K^{N_b}≤K^{B(S)/r_min}. Consequently, for every finite connected S of size≥2,

    P(E_S(ε))≤(Cε)^{B(S)}.

When Cε<1, equation (9) further gives the shape-uniform estimate

    P(E_S(ε))≤(Cε)^{A+mD}.                                      (11)

All constants in (11) are independent of S. The unsolved step is not the existence of a constant for this one event: it is a justified union bound over relevant shapes, and, more fundamentally, a proof that the full wrong-exit event reduces to such low-boundary-probability regions. A walk can backtrack without every boundary site's entire outward probability being small. Equation (11) therefore still does not prove (T).

## 5. A concrete failure of the mean-drift supermartingale method

Suppose d_alpha·e_1=alpha_1-alpha_{1+d}=p-q>0. Condition on n complete loops 0,-e_1,0. At time 2n the outgoing posterior at 0 has backward weight q+n, forward weight p, and unchanged transverse weights. Therefore

    E[(X_{2n+1}-X_{2n})·e_1 | this history]
       = (p-q-n)/(A+n)<0 whenever n>p-q.                        (7)

For any λ>0 the conditional factor for exp(-λX·e_1) is

    [p exp(-λ)+(q+n)exp(λ)+A-p-q]/(A+n),                       (8)

which tends to exp(λ)>1 as n→∞. These histories have strictly positive probability by (4). Thus no constant λ>0 makes exp(-λX_n·e_1) an annealed supermartingale for all walk histories, even when the original drift is positive. This is a counterexample to a proof method, not to F0137. The path probabilities are history-dependent and cannot be replaced by homogeneous probabilities after loop erasure: summing loop histories changes both denominators and outgoing edge weights.

## Remaining gap

### Prior-attempt benchmark, independently checked

Two read-only origin/master reports found during the repository review already identify the source correction and the continued (T′) assumption in 2024–2025. The report dated 2026-09-19 proposes the ray alpha_1=1+δ and every other alpha_i=1, 0<δ≤1. Its formulas check directly: A=2d+δ, d_alpha=δe_1, max_j c_j=2+δ, κ=4d-2+δ, and sum_j|alpha_j-alpha_{j+d}|=δ≤1. Thus even arbitrarily large κ need not imply the source's sufficient condition.

For this ray the homogeneous comparison in section 2 has an explicit exponential parameter: λ=log(1+δ). Indeed

    m(λ,e_1)=[(1+δ)e^{-λ}+e^{λ}+2d-2]/(2d+δ)=1.

The bounded-stopping proof therefore gives the restricted bound (1+δ)^{-bL}. Choosing any strictly smaller positive λ gives m<1 and the neighborhood-of-directions version. This confirms the benchmark is controlled for paths without repeated departure sites. It does not control the full walk. Moreover after n backward two-site loops its conditional e_1 drift is (δ-n)/(2d+δ+n), negative already when n>δ. The high trap exponent does not rescue the naive pointwise conditional drift argument.

The previous report's beta/log-odds diagnostic is local to a site and cannot turn the transverse-moving projected walk into an independent one-dimensional beta RWRE. No such projection reduction is used here.

Equation (3) leaves every wrong-exit trajectory with repeated departure sites uncontrolled. Equations (4)-(11) control the exact time cost, alpha-boundary, or uniformly small boundary probabilities of finite traps, but do not control the probability that a reinforced, many-times-visited path traverses a large distance against d_alpha. There is no estimate here on that full probability uniform in L, nor on E exp(c R^gamma). In particular, a bound on a single shape's trapping probability is not a bound on the total entropy or dependence of visited regions, and a low-boundary-probability event need not occur on every wrong-exit trajectory.

The source's known condition sum_i|alpha_i-alpha_{i+d}|>1 covers a special parameter regime, but the sought nonzero-drift regime includes arbitrary small overall weights and arbitrarily weak drift. The computations and formal checks are auxiliary checks and cannot close that gap. No full proof or counterexample is claimed.

## Final verification and disposition

Seven parameter vectors passed the exact finite checks in experiments.py. The shared `lake env lean` check of Algebra.lean completed with exit code 0; its four algebraic lemmas are kernel-checked, and no `sorry` or `native_decide` was used. The finite boundary enumeration and rational loop checks agree with the written proofs. The hostile-referee audit is in CHECKS.md. These are auxiliary results, some already standard in the Dirichlet-trap literature; no novelty or resolution of the full conjecture is asserted.

Verdict: **PARTIAL**. This bounded attempt is complete. The actual source's (T′) conjecture and the weaker all-parameter (T)gamma question both remain unproved here. No source-matching solution in print was verified.

## User-requested second serious attempt

See SECOND_ATTEMPT.md for two new approaches: Green-function-weighted auxiliary drift and exact annealed path reversal. The first was pursued through exact summation of all two-site revisits and a proposed whole-pair exit-jump repair. Explicit nonzero-drift Dirichlet families with kappa>1 make both required local drift signs negative; the strongest example also has A>1 and works in every d≥2. This blocks these proposed universal reductions without refuting (T′). The reversal route gives a proved finite identity, but heavily traversed paths lose a uniform individual-path exponential bias. AuxiliaryAlgebra.lean and auxiliary_results.json contain the finite checks; their final execution status is recorded in the second-attempt audit.

Second-attempt final status: **DONE / PARTIAL**. Five new auxiliary claims, exact computations, and nine Lean algebraic lemmas are recorded in SECOND_ATTEMPT.md, CLAIMS.jsonl, auxiliary_results.json, and auxiliary_lean_expanded_result.json. The global repeated-visit spatial estimate remains unproved.
