# P0003: maximal collar control for critical SAW

Draft proof packet, 2026-10-10, w396. The full P0003 target is **not proved**. The finite lemmas below have written proofs but are not independently checked. No novelty claim is made for conditional expectation, restriction identities, or Doob's inequality.

## Exact catalog target and explicitly separate working specialization

The original catalog target is Geoffrey Grimmett, *Selected problems in probability theory*, arXiv:2205.07318v1, Question 2.2, printed p.3: uniform n-step self-avoiding walks starting at the origin of the infinite honeycomb lattice, with n tending to infinity, and suitable spatial rescaling, are asked to converge weakly to SLE(8/3). The phrase "when suitably rescaled" leaves the scale constant, continuum endpoint convention, stopping/natural-time convention, and curve topology unspecified in that question. Those are not filled in by silently changing ensembles. Present openness is UNKNOWN.

Write Sigma_n(0) for all n-edge honeycomb walks starting at 0 with no repeated vertex, and P_n for the uniform probability on this finite set. Every such walk lies in the graph-distance-n ball, so it is a finite model even though the lattice is infinite. A precise operational fixed-length version would first choose a spatial normalization s_n, interpolate gamma_n(t)=s_n omega(floor(nt)) linearly for t in [0,1], choose a continuum SLE(8/3) variant and stopping convention matching this finite, free-endpoint whole-plane curve, and specify a curve topology. The predicted exponent s_n proportional to n^{-3/4}, and a whole-plane curve stopped at prescribed natural length, are additional conjectural specifications, not exact assertions supplied by Question 2.2.

The precise missing lemma attempted in this lane is **H_disk**, stated below: a scale-uniform power bound on the fixed-length weight of paths that avoid one prescribed disk but enter its shrinking collar. L1 reduces control at *all* exploration times to this one static estimate. A further identification input **H_len** would require conformally covariant asymptotics of the positive, length-resolved continuation kernels C_{n-k}(G_eta;tip), sufficiently uniformly over realized prefixes to identify the continuum curve law. Neither is proved. Replacing these kernels by an all-length partition function discards a hypothesis. Tightness, normalization/continuum conventions, and transfer to the chordal model are separately unresolved.

Bauerschmidt, Duminil-Copin, Goodman and Slade, *Lectures on self-avoiding walks*, arXiv:1206.2092, Conjecture 1.5 and Section 3.3, formulate the related critical boundary-to-boundary scaling conjecture and explicitly restate it on the honeycomb lattice. In a simply connected domain D with two distinct marked boundary points a,b, use a finite honeycomb approximation D_delta of mesh delta and compatible endpoint approximations. Sum over all finite self-avoiding walks between the endpoints, with critical activity per visited honeycomb vertex, and normalize the total weight. The conjectured random-curve limit is chordal SLE(8/3) from a to b in D. This is an all-length critical ensemble, not the uniform fixed-length catalog ensemble. The source's vertex endpoint convention and the boundary-mid-edge convention must also be recorded separately; neither ensemble transfer nor endpoint-convention equivalence is proved here.

The concrete formulation worked on here takes D bounded Jordan and analytic near a,b, takes a_delta,b_delta to be boundary mid-edges, and sets x_c=(2+sqrt(2))^{-1/2}. A walk gamma has weight x_c^{ell(gamma)}, where ell(gamma) is the number of honeycomb vertices it visits. Duminil-Copin--Smirnov, arXiv:1007.0575v2, Theorem 1 establishes this critical activity; its Section 4 does not establish the scaling limit. Let Z_delta(D;a,b)>0 be the finite partition sum. Embed the paths as polygonal curves. The working convergence assertion uses weak convergence in the uniform metric modulo increasing reparametrization, as specified in Lawler--Schramm--Werner, arXiv:math/0204277v2, Section 3.4.1. Passing from this analytic-boundary working specialization to all admissible source domains is a separate extension.

Present openness is UNKNOWN: targeted literature/source checks recovered the historical conjecture and the exact critical constant, but did not certify an up-to-date resolution or exhaust the owner's solved/retired corpus. Recent public pointers mention honeycomb exponent results; those titles are not a proof of this chordal limit. They are not used as inputs below.

## Prior-attempt digest and division of work

The 2026-09-07 ranking labels P0003 `attempted_un`. It supplies no theorem. The requested H and I attempt directories gave no exact P0003 record in the targeted ID search. The supplied Lean directory's relevant hit is the annotated ranking; no formal theorem receipt for P0003 was recovered. The Claude intake's C0096 dedup note relates its n=0 critical case to P0003 and points to the lectures' Conjecture 1.5; that dedup note does not prove equivalence of fixed-length and chordal ensembles. Its C0095 attempt treats convergence of the complex observable as conjectural. Neither is imported here as a checked mathematical result. w397 identified the original Grimmett Question 2.2, and I verified its primary text; this packet corrects the initial ensemble mismatch explicitly.

Team O assigns C0095 observable convergence to w334 and O(n) interfaces to w335. w399's saved status takes the basic obstacle partition identities. This packet uses those identities as elementary background and claims the narrower maximal collar-error and weak-conditioning bridge. STATEMENT_FOR_ADVERSARY.md was sent to w397 before this proof packet (mesh message msg-168e5faa4e); w398 is the assigned mathematical referee. Team membership was absent, so the existing mesh's direct-message command was used; no team was created.

The required scar `perceptron_proof_open_gaps_fleet_2026_07_12` warns that a completed computation need not close the hardest proof gap. This packet records the gap explicitly and keeps numerical checks separate from proof.

## Finite setup and exact background identity (L0)

Let G=(V,E) be finite, a!=b in V, and assign every edge e a weight q_e>0. Let Omega_G be the simple paths from a to b, stopped on first reaching b. For omega in Omega_G put w(omega)=product of q_e along omega, Z_G=sum w(omega), and assume Z_G>0. For A subset V\{a,b}, E_A means that omega visits no vertex of A. Every subgraph retains the original edge weights.

Deleting A gives exactly the paths in E_A, so r_G(A):=P_G(E_A)=Z_{G\A}/Z_G. If r_G(A)>0, the conditional path law given E_A is P_{G\A}. This is a finite counting identity.

For geometric obstacles one instead deletes every edge whose embedded segment intersects the closed obstacle. The same argument works with forbidden edge sets and makes avoidance of the compact trace literal. Removing just obstacle vertices while leaving crossing edges would be a different discretization.

Let N=|V|-1. F_k records the prefix of min(k,length(omega)) edges, including terminal information. After completion it keeps the same complete path. At a realized unfinished prefix eta=(v_0,...,v_k), put G_eta=G\{v_0,...,v_{k-1}} and retain v_k. The bijection between completions and simple v_k-to-b paths in G_eta, together with cancellation of the prefix's product weight, gives

    M_k^A := P_G(E_A | F_k)
       = 1_{eta avoids A} Z_{G_eta\A}(v_k,b)/Z_{G_eta}(v_k,b).

Every realized unfinished prefix has positive denominator. Impossible prefixes are never divided by; they may be assigned arbitrary values off the probability space. At completed prefixes use M_k^A=1_{E_A}, including the case when b was reached before k. Consequently M^A is a [0,1]-valued martingale and M_N^A=1_{E_A}.

The honeycomb mid-edge model is covered by subdividing the honeycomb edges and weighting each half-edge x_c^{1/2}; a path with ell visited original vertices has 2ell half-edges and hence the intended weight x_c^ell. Self-avoidance in the subdivided graph is exactly the usual walk self-avoidance. A deleted geometric edge is deleted in this subdivided graph. These are finite identities, not an equivalence theorem for endpoint conventions in the continuum.

## Length-preserving version for the actual catalog ensemble (L0')

For a finite weighted graph define C_m(G;v) as the sum of inherited product weights over all simple m-edge paths starting at v, with their terminal vertex free. Put C_0(G;v)=1 when v is present and C_m(G;v)=0 when v is deleted or no such path exists. Define C_m(G;v,b) similarly if a terminal vertex b is prescribed, retaining the exact remaining length m. For the uniform n-step honeycomb model all edge weights are one and G is the graph-distance-n ball about 0.

At a realized prefix eta of k edges, completions are precisely the simple (n-k)-edge paths from its tip in G_eta. Thus the correct fixed-length martingale is

    M_k^A = 1_{eta avoids A}
             C_{n-k}(G_eta\A;tip)/C_{n-k}(G_eta;tip),
    M_n^A = 1_{E_A}.

The denominator is positive at every realized prefix. The root probability is C_n(G\A;0)/C_n(G;0), not Z_{G\A}/Z_G. The same conditional-expectation proof gives L1 with horizon n and these root ratios; L2 likewise applies unchanged to the nested events. This length-preserving statement applies directly to P0003's finite uniform laws without assuming any ensemble transfer. It still supplies no asymptotic for its root or random-tip ratios.

## Maximal collar-error lemma (L1)

If A subset B subset V\{a,b}, put D_k=M_k^A-M_k^B. Since E_B subset E_A, D_k=E[X | F_k], where X=1_{E_A\E_B}. Thus D is a nonnegative bounded martingale, D_0=r_G(A)-r_G(B), and D_N=X. For every lambda>0,

    P_G(max_{0<=k<=N} D_k >= lambda)
        <= min(1,(r_G(A)-r_G(B))/lambda).                 (L1)

Proof. Stop at the first k with D_k>=lambda if such a k exists, and otherwise stop at N. This is a bounded stopping time tau. Finite martingale stopping, obtained directly by summing E[(D_{k+1}-D_k)1_{tau>k}]=0, gives E[D_tau]=D_0. On the crossing event D_tau>=lambda, while off it D_tau>=0. Therefore lambda P(crossing)<=D_0. No independence is assumed. This also covers arbitrary stopping rules, because D_sigma<=max_k D_k for every sigma in {0,...,N}. The argument is unchanged for nested forbidden edge sets.

The constant is sharp. On the equal-weight diamond with paths (a,c,b) and (a,d,b), choose A empty, B={c}, lambda=1. D_0=1/2 and D is 1 after choosing c, 0 after choosing d. The crossing probability is exactly 1/2.

## Conditioning costs only the initial ratio deficit (L2)

For A subset B and 0<r_G(B)<=r_G(A), with total variation defined as sup_C |P(C)-Q(C)|,

    TV(P_G(.|E_A), P_G(.|E_B)) = 1-r_G(B)/r_G(A).      (L2)

Proof. Set p=r_G(B)/r_G(A). The law conditioned on E_A is p times the law conditioned on E_B plus (1-p) times the law conditioned on E_A\E_B. The two components have disjoint support. Testing E_B attains 1-p, and the mixture identity bounds every other event by 1-p. If p=1 the laws coincide and no conditioning on the null difference event is needed. Any measurable prefix or stopped-prefix map contracts total variation, so the same expression is an upper bound for its two induced laws.

## A rigorous weak-limit conditioning bridge (L3)

Let K_n be random nonempty compact traces in a fixed compact metric space, converging in law for Hausdorff distance to K. Let A be nonempty and closed and define d_n=dist(K_n,A), d=dist(K,A). Suppose

    P(d_n>0)->r,
    P(d_n>epsilon_j)->r_j for a sequence epsilon_j decreasing to 0,
    r_j->r>0.                                         (C)

Then P(K avoids A)=r and the conditional laws of K_n given d_n>0 converge weakly to the law of K given d>0. No assumption that K has zero probability of touching the boundary of A is needed.

Proof of the probability statement. The clearance functional is continuous, so d_n converges in law to d. Portmanteau applied to the open interval (0,infinity) gives P(d>0)<=r. For each j, P(d_n>epsilon_j)<=P(d_n>=epsilon_j), and Portmanteau for the latter closed interval yields r_j<=P(d>=epsilon_j)<=P(d>0). Let j tend to infinity. This proves equality.

Proof of conditional convergence. On a Skorohod coupling in the compact-trace space, K_n converges to K almost surely, hence d_n->d. On {d>0}, eventually d_n>0. The false-negative probabilities therefore tend to zero. Since P(d_n>0)->P(d>0), the false-positive probabilities tend to zero as well. Thus 1_{d_n>0}->1_{d>0} in L1. For every bounded continuous F on trace space, F(K_n) converges almost surely to F(K); the product with the avoidance indicators converges in L1. Divide its expectations by P(d_n>0)->r. This proves conditional weak convergence.

For the exact geometric-edge deletion convention, P(d_n>epsilon_j) is the partition ratio after deleting the epsilon_j neighborhood of A. To use a family of smooth simply connected collars rather than literal neighborhoods, one must supply inclusions between inner and outer neighborhoods and squeeze their ratios; that geometric compatibility is a hypothesis, not a result of L3. The trace lemma also applies to any available convergence in the stronger uniform curve metric, because taking the trace is continuous. Trace convergence itself does not establish the ordered-curve tightness required by P0003.

## What these lemmas reduce, and what they do not

Suppose H_5/8 below is supplied both for A and for shrinking admissible collars B_epsilon containing A, with their conformal derivative products converging to the product for A. By L1, for every lambda>0,

    lim_{epsilon->0} limsup_{delta->0}
       P(max_k |M_k^A-M_k^{B_epsilon}|>=lambda) = 0.

The order of limits is stated; no uniform convergence in arbitrary delta-dependent collars has been proved. L2 also makes full-path conditional laws uniformly insensitive to the collar. Under the neighborhood-ratio version of the same input and an existing subsequential curve limit, L3 transfers the exact discrete restriction conditioning to the continuum. Thus a separate conditional-independence argument and a blanket boundary-touch continuity assumption are unnecessary for this step.

If a subsequential limit is an interior simple a-to-b curve and its avoidance probabilities for all admissible boundary-attached obstacles have the H_5/8 values, the uniqueness/identification theorem of Lawler--Schramm--Werner, arXiv:math/0209343, Section 3 and Theorem 6.1, identifies its trace law with chordal SLE(8/3). Simplicity gives the unique oriented a-to-b curve associated with that trace, up to increasing reparametrization. This conditional reduction does not establish curve tightness or simplicity.

## Substantive attack on the hardest input

H_5/8 asks, for D analytic near a,b and A a compact boundary-attached obstacle away from them with D\A simply connected and unchanged near the endpoints,

    r_delta(A) = Z_delta(D\A;a,b)/Z_delta(D;a,b)
         -> rho_D(A) = (|f_A'(a)| |f_A'(b)|)^{5/8},

where f_A:D\A -> D fixes a,b. Graph deletion defines the numerator in the same lattice and with the same endpoint normalization. The endpoint derivative product is invariant under postcomposition by endpoint-fixing automorphisms of D. In the half-plane normalization a=0,b=infinity this is Phi_A'(0)^{5/8}. Derivatives at infinity use the usual hydrodynamic normalization, not a finite boundary derivative formula.

Attempt 1: use the exact exploration martingale to identify this value. L0 supplies M_0=r_delta(A), not a value for M_0. Optional stopping only returns that same unknown ratio. L1 transfers errors between nested obstacles but has no conformal map in it. Therefore using optional stopping to assert rho_D(A) would be circular.

An exact obstruction to that inference is the graph with paths (a,b) and (a,c,b), direct-edge weight u>0 and the two other edge weights v,w>0. Deleting c has ratio u/(u+vw). Varying u/(vw) gives any value in (0,1) while the graph, embedding, restriction identity and every martingale statement stay valid. This is a counterexample to deriving a geometric power law from those general identities, not a counterexample to critical honeycomb H_5/8.

Attempt 2: bring in the honeycomb complex observable. The source establishes a local linear relation at each degree-three vertex and the spin parameter 5/8. It does not provide a positive comparison or convergence theorem identifying the unweighted two-boundary partition ratio in a slit domain. Equality of this spin with the predicted boundary exponent does not close H_5/8. The absent step is a uniform, domain-sensitive estimate for the positive partition sums (or a proved analytic substitute implying it). This route has not produced that estimate here and does not duplicate Team O's observable-convergence computations.

A valid exact collar estimate is r_delta(A)-r_delta(B)=Z_delta(E_A\E_B)/Z_delta(D). The numerator is precisely the weight of walks avoiding A but entering the collar. Bounding it by a conformal modulus tending to zero would close the collar portion of H_5/8; L1 would then handle all random exploration prefixes automatically. No proved bound with the required modulus is available in this packet. A union bound over vertices of the collar gives no scale-uniform control and is not substituted for one.

Finally, even exact avoidance of A before taking a limit is insufficient: deterministic traces at distance 1/n from A avoid it for every n but their limit can hit it. Their fixed positive collars eventually have avoidance probability zero, so condition (C) fails. This shows exactly why the collar ratio input is present.

## Precise fixed-length missing lemma and its attempted bound

Fix z in C and r>0 with |z|>r, and choose the operational, conjectured normalization s_n=n^{-3/4}. Let A be the closed disk of radius r about z and B_epsilon the concentric disk of radius (1+epsilon)r; take epsilon small enough that 0 is outside B_epsilon. In the graph-distance-n honeycomb ball G_n, delete every edge whose segment, after multiplying coordinates by s_n, intersects the respective disk. Denote the resulting forbidden edge sets A_n and B_{n,epsilon}. All counts below retain **exact length n** and a free terminal vertex. Set

    Delta_n(epsilon)
      = [C_n(G_n\A_n;0)-C_n(G_n\B_{n,epsilon};0)]/c_n(H).

The exact missing estimate H_disk is: there exist alpha>0 and C=C(z,r)<infinity such that

    limsup_{n->infinity} Delta_n(epsilon) <= C epsilon^alpha

for all sufficiently small epsilon>0. Its scale convention is explicitly a chosen version of the source's unspecified rescaling. This estimate is conjectural; even its modulus-to-zero version is not proved here. If supplied, L1 gives limsup_n P(max_k |M_k^{A_n}-M_k^{B_{n,epsilon}}|>=lambda)<=C epsilon^alpha/lambda for every lambda>0, with no n factor.

Proof attempt by first collar entrance. Let c_k^{B}(0,v) count k-edge simple paths from 0 to v in G_n\B_{n,epsilon}; let C_m^{A}(w) count m-edge simple paths from w with free endpoint in G_n\A_n. A path counted by the numerator has a unique first forbidden B edge (v,w), traversed after k edges; it is not an A edge. Splitting there is an injection into a prefix, the oriented edge and a suffix. Dropping the mutual self-avoidance constraint between prefix and suffix gives the rigorous counting upper bound

    c_n(H) Delta_n(epsilon)
      <= sum_{k=0}^{n-1}
           sum_{(v,w) oriented in B_{n,epsilon}\A_n}
             c_k^{B}(0,v) C_{n-k-1}^{A}(w).            (U)

This is multiplication of cardinalities in a counting injection, not multiplication of conditional probabilities. The empty prefix/suffix cases use C_0=1. At unit edge weights no extra edge factor is needed. For positive general weights one includes q_(v,w).

The gap is explicit: no scale-uniform estimate of the mutually avoiding prefix/suffix mass, or a sufficiently strong bound on (U), has been proved here. The product bound discards mutual avoidance and may be too large even if H_disk is true. Bounds using only the connective constant have exponential/subexponential losses and do not yield the required epsilon modulus; no such losses are hidden as constants. The partition identity, Doob bound and known observable spin supply no estimate of these length-resolved counts. Thus this attack ends at a specific positive counting estimate, not at an asserted SLE limit.

## Single hardest attempted gap and full-target prerequisites

**H_disk is the single hardest concrete estimate attempted in this packet:** prove the stated fixed-length collar-count bound, retaining mutual avoidance and length n. It remains unproved. Closing it would close the collar-control step, not the full catalog problem. The further H_len identification input and ordered-curve tightness, interior simplicity/Loewner regularity, and scale/continuum conventions are also unproved. **H_5/8 remains unproved** for the distinct all-length chordal route, which would still require a fixed-length transfer theorem and endpoint/domain extensions. L0--L3 and L0' do not imply these prerequisites. Current claim: a finite maximal-error lemma valid for both ensembles, a conditional weak-limit bridge, and an exact first-entrance counting reduction, not a solution of P0003.

NEXT: Have w398 audit L0', L1--L3 and (U); then control mutually avoiding prefix/suffix counts for H_disk without replacing C_n by an all-length Z.
