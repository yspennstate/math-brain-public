# G0008 research record ? 2026-10-11

## Exact target and current status
For iid nearest-neighbour Bernoulli bond percolation on Z^d, d>=2, define tau_n(p)=P_p(0 <-> n e_1), n>=0. The requested claim is tau_{n+1}(p)<=tau_n(p), for every n and every 0<p<1. The axis statement is weaker than the source's separately defined comparison between arbitrary vertices of different graph distances. We work on the axis statement.

The downloaded source is Campos?de Lima, arXiv:2601.00291v1, 1 January 2026. Its abstract explicitly calls the axis statement open; p.2 specifies independent bond percolation. The transitive-graph and Pipe-Dust examples do not settle it. Bounded follow-up searches have found no solution; OpenAlex and Semantic Scholar returned HTTP 429, so the literature search is incomplete. Further searches and exact partial checks are ongoing.

## Read-only prior research audit
Read the intake G0008-A001/A002 and the origin/master G0008 admissions, mathematical artifacts and terminal handoff from 18 September 2026; copies of the latter are preserved locally as prior_*.md. Brain topic/mistake recall returned largely unrelated hints.

1. The withdrawn crude-path-count argument does not prove small-p monotonicity uniformly in n. The actual uniform small-p theorem is de Lima?Procacci?Sanchis (2015), Theorem 1(i), proved using uniform Ornstein?Zernike and polymer estimates. It is a literature result, not our proof.
2. The 2015 high-p result, Theorem 1(ii), concerns tau^f_n=P(0 <-> n e_1, |C(0)|<infinity). It must not be silently identified with tau_n-theta(p)^2. The exact decomposition is tau_n=tau^f_n+P(0 and n e_1 both in the infinite cluster), by uniqueness. The second summand depends on n. Therefore eventual monotonicity of tau^f alone does NOT establish eventual monotonicity of the full supercritical tau. The intake's corresponding inference is unsupported.
3. A subcritical OZ asymptotic tau_n=A n^{-a} exp(-xi n)(1+o(1)), xi>0, DOES imply eventual strict decrease: tau_{n+1}/tau_n -> exp(-xi)<1. For polynomial decay alone the analogous ratio limit is 1 and is insufficient.
4. Finite-width eventual monotonicity (K?nig?Richthammer) has a width-dependent onset, so does not pass to arbitrary fixed n in the plane.
5. The earlier critical first-step punctured-star certificate is being independently audited and strengthened. Full parameter or distance coverage is not claimed.

## Elementary special cases
At p=0, tau_0=1 and tau_n=0 for n>=1. At p=1, all tau_n=1. On Z, the only simple path from 0 to n has n edges, so tau_n=p^n; this proves monotonicity in dimension one. In any dimension tau_1<tau_0 for p<1, because closing all 2d edges at the origin has probability (1-p)^{2d}>0.

More detailed proofs, exact finite computations and the remaining gap will be added below.

## A checked critical first-step theorem

**Theorem (restricted to d=2, p=1/2, n=1).**

    tau_1(1/2) - tau_2(1/2) >= 9/2048 > 0.

This strengthens the earlier record's 13/4096 bound. It does not settle all n or all p. No novelty claim is made.

### Proof: geometry and the exact six-orbit reduction

Translate the three vertices so that y=(0,0), x=(-1,0), z=(1,0), u=(0,1), v=(0,-1). Delete the four edges incident to y. The graph K has isolated y; discard y. Observe the equivalence relation of open connectivity on the cyclically ordered terminals (x,u,z,v).

There are 15 equivalence relations on four labelled points. Exactly one, {x,z}|{u,v}, cannot occur: if its two disjoint clusters existed, choose finite simple paths for the two opposite connections. The four terminals lie in cyclic order on the boundary of the single face left by removing the star. Two disjoint paths joining alternate boundary points of a planar face are impossible by the Jordan curve theorem (equivalently, put this face on the outside by a sphere homeomorphism and apply the disk version). Thus there are 14 possible noncrossing partitions. This argument uses finite connection witnesses, not any assumption that clusters are finite.

The iid law on K is invariant under the dihedral symmetries of the square. Write s,a,b,g,d,e for the probabilities of ONE SPECIFIED partition in the following six orbits:

|Orbit variable|Block sizes and geometry|Orbit size|
|---|---|---:|
|s|four singletons|1|
|a|one adjacent pair, two singletons|4|
|b|one opposite pair, two singletons|2|
|g|two adjacent pairs|2|
|d|one triple, one singleton|4|
|e|one block of size four|1|

All six numbers are nonnegative and

    s+4a+2b+2g+4d+e=1.                                      (N)

Restore the four star edges independently with parameter p and put q=1-p. Conditional on a terminal partition pi and a star-edge subset S, connections are obtained by merging exactly those blocks that have a member incident to S, together with y. The conditional contribution is

    sum_{S subset {x,u,z,v}} p^{|S|} q^{4-|S|}
        [1{x connected to y after merging} - 1{x connected to z after merging}].

Summing this expression over all specified partitions in each orbit gives the following orbit totals, after dividing by q:

|Orbit|Coefficient of its per-partition probability in B_p|
|---|---|
|s|p|
|a|2p(3-2p)|
|b|2p-1|
|g|2pq(2-p)|
|d|2p^3-7p^2+8p-2|
|e|-q^3|

Consequently tau_1(p)-tau_2(p)=q B_p. This table is a complete finite reduction: the displayed sum specifies all 14*16 cases, and `check_partitions.py` independently generates the set partitions and unions the open star edges to verify every coefficient as a rational polynomial. In particular, at p=1/2,

    B = s/2 + 2a + 3g/4 + d/2 - e/8,
    tau_1(1/2)-tau_2(1/2)=B/2.                            (B)

### Proof: the critical self-dual relation

Let f be the removed edge xy, and consider the graph with f deleted but all other edges present. At p=1/2 let D be the probability of an open detour from x to y avoiding f. Its dual edge f* has dual endpoints x*,y*. Under the usual coupling dual edges are open exactly when the corresponding primal edges are closed; delete f* in the dual graph as well. Let D* be the dual detour probability between x*,y* avoiding f*.

Exactly one of these two detours exists almost surely. Here are both directions. If the primal detour exists, choose a simple such path and add f as a geometric segment. This is a simple polygonal cycle, with the endpoints of f* on its opposite sides. A dual path avoiding f* must cross another edge of that cycle; all those other edges are primal-open, hence dual-closed, so the dual detour is impossible. If the primal detour does not exist, the x-cluster is finite almost surely at criticality (the standard Harris--Kesten absence of a critical infinite cluster, preserved by deleting one edge). Its edge boundary consists of closed edges, including f. In the dual graph those boundary edges form a finite graph of even degrees. Every edge of such a graph lies on a cycle, so there is a dual cycle containing f*. Removing f* from this cycle gives the required dual detour. Thus D+D*=1. At p=1/2 the deleted-edge dual lattice is isomorphic to the deleted-edge primal lattice, with the same independent edge probabilities; D*=D. Hence D=1/2.

Condition now on the K partition and restore the three star edges other than xy. If m is the number of terminals among {u,z,v} in the K-cluster of x, x fails to connect to y precisely when all m corresponding star edges are closed, with probability 2^{-m}. (A terminal outside the x-block cannot reach x through y without at least one open star edge into the x-block.) Summing this failure probability over each orbit gives, respectively,

    1, 3, 3/2, 1, 7/4, 1/8.

For example, in the adjacent-pair orbit x belongs to the pair in two of the four partitions: total 2*(1/2)+2*1=3. In the triple orbit x is in the triple in three partitions: total 3*(1/4)+1=7/4. The other entries follow by the same direct count. Since the unconditional failure probability is 1-D=1/2, this table and (N) imply

    4s+8a+4b-2d-3e=0.                                    (SD)

### Proof: FKG and a stronger algebraic bound

Let A={x connected to z in K}, C={u connected to v in K}. Both are increasing, with common probability

    T=b+2d+e.

Their intersection is exactly the all-four-connected event: two opposite connections in different clusters would be the forbidden crossing partition. Harris's product-measure association therefore gives

    e >= T^2.                                            (FKG)

For completeness, this infinite-edge application follows by approximating A,C by finite-box connection events. Finite product association follows inductively on the number of edges: for one Bernoulli variable the covariance of increasing functions is p(1-p)(f(1)-f(0))(g(1)-g(0))>=0; conditioning on the last coordinate and applying the covariance decomposition proves the induction. Passing to increasing finite-box approximations gives the displayed bound.

Eliminating s and b from (N),(SD) gives

    2a+(3/4)e+T+(5/2)d+2g=1.                             (E)

In particular T+(3/4)T^2<=1. Since T>=0, this implies T<=2/3: the polynomial factors as

    T+(3/4)T^2-1 = (3/4)(T-2/3)(T+2).

Put h=2/3-T>=0. Equation (E) and (FKG) yield

    (5/2)d+2g <= 1-T-(3/4)T^2
                 = 2h-(3/4)h^2 <= 2h,

so h >= (5/4)d+g. A second elimination gives

    8B=4+3e-8T+4d-2g.

Using (E) to bound the -2g term, equivalently using a>=0, yields

    8B >= 3+(15/4)e-7T+(13/2)d
        >= Q(T)+(13/2)d,
    Q(T)=3+(15/4)T^2-7T
         = 2h+(15/4)h^2 >= 2h.

Combining these inequalities proves the stronger conditional implication

    8B >= 9d+2g,
    B >= (9/8)d+(1/4)g.                                 (ALG)

This is the key real algebra statement in `CriticalFirstStep.lean`; its hypotheses are precisely nonnegativity, (N), (SD), and (FKG). Only this implication is formalized, not the stochastic or planar arguments.

### Proof: explicit strictness

Force the four edges along the path

    x--(-1,1)--u--(1,1)--z

to be open, and force the three K-edges incident to v to be closed:

    v--(-1,-1), v--(1,-1), v--(0,-2).

These seven distinct edge prescriptions have probability 2^{-7}. Regardless of all other edges, they connect x,u,z and isolate v, so they force exactly the specified triple-plus-singleton partition. Thus d>=1/128. By (B),(ALG),

    tau_1(1/2)-tau_2(1/2)=B/2 >= (9/16)d >= 9/2048.

This completes the restricted theorem, conditional only on the standard absence of a critical infinite cluster for square-lattice bond percolation.

## Exact finite-box experiments

`exact_boxes.py` uses a frontier connectivity transfer calculation with exact integer coefficients. For the induced free-boundary square B_R=[-R,R]^2 and source (0,0), write

    P_{B_R,p}(0 connected to (n,0))
      = sum_{k=0}^{m} c_{R,n,k} p^k (1-p)^{m-k},

where m=4R(2R+1) and c counts configurations with k open edges. Initially the source and target are retained as two marked singleton components. Process edges by columns, add an endpoint at its first appearance, branch to open (merge components) or closed (no merge), and remove every unmarked vertex after its last incident edge. At each step the state records exactly the partition of active vertices induced by all processed open edges; this invariant is preserved by the two branches and forgetting. Polynomial coefficient updates count closed branches at the same k and open branches at k+1. At the end sum counts over states in which the two marks agree. This proves the recurrence produces the exact coefficients.

Checks: at each completed graph, the total coefficients over all terminal states equal binomial(m,k); an independent exhaustive 2^12-edge-configurations check on R=1 passed. `exact_boxes.json` preserves all coefficient arrays. Computed R=1,2,3, with m=12,40,84; peak state count 6571; total measured calculation time 4.30 seconds, well below the job bounds.

For R=2 all coefficients c_{2,1,k}-c_{2,2,k} are nonnegative. For R=3 all coefficients of both differences (n=1 versus 2 and n=2 versus 3) are nonnegative. These finite-box comparisons therefore hold for EVERY p in [0,1], not just sampled p. They are special cases on different finite graphs; as evidence about G0008 they remain finite-volume evidence. No passage to the infinite lattice follows from a finite list of boxes. At p=1/2 these arrays also permit exact comparison against the critical theorem, without replacing the infinite-volume proof.

## Hostile-referee audit and precise remaining gap

- Translation sends the original distance-one/distance-two comparison to x-y versus x-z with middle y at the puncture; D4 symmetry applies to K, not to the source-target ordered triple.
- Orbit variables denote per-specified-partition probabilities, so normalization uses multiplicities. The independent star enumeration checks that no orbit multiplicity was lost.
- Opposite terminal connections may intersect; FKG uses their ordinary intersection, not disjoint occurrence. Planarity proves that this intersection is exactly the all-connected event.
- The primal/dual identity is justified here at criticality using finite clusters. It is not extrapolated to a free/wired partition identity away from criticality.
- Critical detour probability is conditional on deleting the direct edge; it is not the full nearest-neighbour probability. Indeed tau_1(1/2)=1/2+(1/2)*(1/2)=3/4, a useful sanity check.
- The strictness cylinder forces only seven edges and holds independently of the exterior. No finite-box truncation is used in that bound.
- Lean checks the real algebra implication, not the whole percolation theorem; no theorem beyond that formal scope is described as machine-checked.
- The standard critical no-infinite-cluster theorem and Jordan curve topology are established background results, explicitly identified above. No new proof of those background theorems is claimed.
- The finite-box experiments cannot establish tau_{n+1}<=tau_n in the plane. Free and wired boundary effects cannot be cancelled without a separate comparison theorem.

The remaining gap is exact: prove tau_{n+1}(p)<=tau_n(p) for every integer n>=1 and every 0<p<1 on the infinite nearest-neighbour Z^2 lattice, or exhibit and certify a violation. This work proves only the critical first comparison, alongside elementary cases and finite-box evidence. The all-d axis version remains unresolved too. A possible next route is a width-uniform transfer invariant forcing the signed coefficient comparison, but no such invariant has been proved.


## New infinite-volume first-step intervals from exact boundary bounds

**Theorem (d=2, n=1, explicit parameter intervals).** For

    0<p<=2/5   or   23/25<=p<1,

one has

    tau_1(p)-tau_2(p) >= (3/10) p(1-p)^6 > 0.

This is an infinite-lattice theorem, not just the same-boundary finite-box observation. It remains a first-distance special case.

### Complete comparison proof

Let B=[-3,3]^2, with origin (0,0) and targets (1,0),(2,0). Let F(p) be its free-boundary probability of connection to (1,0), and W(p) its probability of connection to (2,0) when all boundary vertices are deterministically identified (wired). Then

    tau_1(p)>=F(p),   tau_2(p)<=W(p).

The first inequality follows because every path in B is a path in the lattice. For the second, take any finite lattice path from 0 to (2,0). Its parts outside B can be replaced by the deterministic identification of the exit and entrance boundary vertices. All its remaining edges in B are open, so it implies connection in the wired B. This is a pointwise coupling argument, valid for every exterior realization, not a claimed cancellation of boundary errors. Therefore

    tau_1(p)-tau_2(p) >= F(p)-W(p).

`wired_bounds.py` calculates W using the same exact frontier recurrence, now retaining a third marked component and merging each boundary vertex into it on introduction. This exactly implements boundary identification; internal edges remain independent. The free and wired graphs both have 84 independent lattice edges. If f_k,w_k are their exact configuration counts, the signed polynomial is

    F(p)-W(p)=sum_{k=0}^{84}(f_k-w_k)p^k(1-p)^{84-k}
              =p(1-p)^6 H(p),

where H has degree 77. The equality is checked by exact integer polynomial expansion and division, with zero remainder. All f_k,w_k and all coefficients of H are preserved in `exact_boxes.json`, `wired_box.json`, `free_wired_counts.json`, `free_wired_polynomial.txt` and `interval_certificates.json`; they are fully reproducible from the saved programs.

### Complete algebraic certificate proof

Let c_j be the integer power coefficients of H, 0<=j<=77. On a rational interval [a,b], substitute p=a+(b-a)t. Its power coefficients are exactly

    h_i=sum_{j=i}^{77} c_j binomial(j,i) a^{j-i}(b-a)^i.

Its normalized Bernstein coefficients of degree 77 are exactly

    B_k=sum_{i=0}^{k} h_i binomial(k,i)/binomial(77,i).

To justify this conversion, expand each t^i by multiplying by
(t+(1-t))^{77-i}=1. The coefficient identity
binomial(77,i)binomial(77-i,k-i)=binomial(77,k)binomial(k,i)
gives

    t^i=sum_{k=i}^{77}[binomial(k,i)/binomial(77,i)]
                      binomial(77,k)t^k(1-t)^{77-k}.

Thus

    H(a+(b-a)t)=sum_{k=0}^{77} B_k binomial(77,k)t^k(1-t)^{77-k}.

For 0<=t<=1 these basis weights are nonnegative and sum to one by the binomial theorem. `certify_intervals.py` evaluates every B_k with exact Fraction arithmetic. For [a,b]=[0,2/5] and [23/25,1], every one of the 78 coefficients is strictly greater than 3/10. The smallest coefficients, reported only for readability as decimal approximations, are respectively about 0.3157583728 and 0.3033134711; the certificate file retains exact rational values and verification compares them as rational numbers. Therefore H(p)>=3/10 throughout both closed intervals. Combining the factorization and boundary comparison proves the displayed infinite-volume bound, completing the proof.

### Scope and failure of extension

This particular free/wired polynomial is negative at p=1/2: its exact rational value is recorded in the final verification file (approximately -0.06263). Thus this fixed box does not prove the middle parameter range; the critical proof above is independent and supplies a positive result there. Negative free-minus-wired bounds are not counterexamples to lattice monotonicity. The all-distance question remains open after both restricted theorems.


## Final verification receipt (2026-10-11)

- `check_partitions.py`: ALL_EXACT_CHECKS_PASS (all 14 noncrossing partitions, all 16 restored-star states, polynomial orbit coefficients and dual failure weights).
- `CriticalFirstStep.lean`: checked by `lake env lean` from the specified lean_verify project, exit 0. Only Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith imported; no sorry, no native_decide. Lean reports only the usual propext, Classical.choice, Quot.sound axioms. The algebra proof is kernel-checked; the complete probabilistic theorem is written above.
- `box_verification.json`: independent enumeration of all 4096 configurations of the 3 by 3 free square agrees coefficientwise with the transfer recurrence; all stated same-boundary finite-box signed counts are nonnegative.
- `verify_final.py`: free and wired 7 by 7 counts agree with recalculation in REVERSED edge order; wired 3 by 3 target-on-boundary counts equal the exact star formula 1-(1-p)^4; wired counts dominate free counts coefficientwise; the signed degree-84 polynomial factorization is exact; every stored rational Bernstein coefficient is recomputed and exceeds 3/10 on the certified intervals. All checks passed, recorded in final_verification.json.
- The free-minus-wired comparison at p=1/2 is exactly -302861607514102889507865/4835703278458516698824704, so this attempted global certificate fails there. This failure is correctly recorded as an obstruction, not a counterexample to G0008.
- Literature follow-up: Semantic Scholar's source citations endpoint eventually succeeded and returned zero indexed citations. OpenAlex remained rate-limited; literature status is a bounded negative search, not a certified exhaustive novelty assessment.

Final disposition: DONE / PARTIAL. The research pass is complete with two proved infinite-lattice first-step restrictions, exact finite-box comparisons and an explicit unresolved all-parameter/all-distance gap. No complete proof or counterexample to G0008 is claimed.


## Additional serious attempt: two previously untried approaches

Reopened on 2026-10-11 at the user's request. Exact remaining gap: uniform sign of the infinite-lattice axial differences, already unresolved for n=1 in the middle parameter range apart from p=1/2.

**Approach A (selected): couple the signed comparison through a common exterior.** Rather than lower-bound tau_1 and upper-bound tau_2 separately, remove the central star and expose an interior square once. Keep the free partition of its four terminals AND which of those clusters reach the square boundary. Any exterior induces a coarsening only among boundary-reaching blocks. Average the restored-star signed functional over D4, then minimize this same signed functional over the possible intermediate noncrossing partitions. The expected minimum is a rigorous lower bound using the common interior configuration. This can have much smaller boundary error than the old independent free-minus-wired bound, because the exterior can alter terminal connectivity only if at least two distinct terminal clusters reach the boundary. Goal: an all-p first-step certificate or new explicit middle-parameter intervals.

**Approach B (not selected for main work): transfer ferromagnetic reflection inequalities through q down to 1.** The q-state Potts/random-cluster correspondence might suggest importing axial correlation monotonicity from the Ising/Potts reflection-positivity literature and analytically continuing the connectivity inequality to q=1. This is different from the earlier ordinary Toeplitz positive-definiteness reduction. A hostile check must first test positivity of the random-cluster boundary join matrices for noninteger q between 1 and 2; loss of that positivity would invalidate the proposed continuation. A finite exact matrix test will be recorded alongside the main attempt.

Brain query already run: math_recall.py "percolation axial connectivity monotonicity width uniform transfer Bernstein wired boundary Koenig Richthammer". It returned mostly unrelated cards, with a relevant Aizenman--Kesten--Newman continuity reference and wired-boundary arm hints. None was used as a theorem establishing the gap. A second named-result query follows for Approach B.

### Approach A: first exact results saved

Implemented joint_boundary.py, tracking the free terminal partition and boundary-hit flags for each active component in the punctured square. At p=1/2 the signed common-exterior lower bound is exactly 946031639/68719476736 > 0.01376657 already for radius 2 (36 random interior edges). For radius 3 (80 edges) it is 222467545577872491640397/4835703278458516698824704 > 0.04600521. These outperform the earlier critical 9/2048 bound if the new coupling and finite calculation pass the independent audit.

Exact radius-two evaluation at all nineteen rational parameters k/20, 1<=k<=19, is positive. These samples are not an all-parameter proof. The next concrete step is an exact piecewise Bernstein certificate for the radius-two lower-envelope function, with independent checks of the boundary-flag transfer recurrence and D4 averaging.

State budgets: radius-two peak 2326, radius-three peak 277787; scalar integer-count jobs use a hard 350000-state cap and 160-second cap. Radius-three run took 27.78 seconds. Files joint_R1.json, joint_R2.json, joint_R3.json and joint_R2_grid.json preserve the results.

### New all-parameter candidate (saved before audit)

The coefficientwise lower-envelope construction has produced a single global [0,1] Bernstein certificate of degree 40 with every coefficient nonnegative and at least one positive. This suggests a proof of tau_1(p)>tau_2(p) for EVERY 0<p<1 on the infinite square lattice, using only a radius-two common-interior calculation and D4 averaging. It is not yet admitted as proved: the averaging identity, allowed-coarsening characterization, boundary flags and certificate will be checked by independent brute force at radius one, reversed-edge radius-two transfer, direct orbit enumeration and an integer-convolution recomputation. Files joint_interval_certificates.json and joint_signed_integer_certificate.json preserve the exact candidate.


## Proved: the first axial comparison for every parameter

**Computer-assisted theorem.** In iid nearest-neighbour bond percolation on the infinite square lattice,

    tau_1(p)-tau_2(p) >= p(1-p)^6 > 0  for every 0<p<1.       (NEW)

This settles the first comparison uniformly in p, but is still PARTIAL for G0008, which asks every n. The proof is finite and uses symmetry and planarity; it does not use critical self-duality, the no-infinite-cluster theorem, or an infinite-volume approximation limit. Publication novelty remains unverified.

### 1. Exact averaged signed observable

As before, center the middle vertex y at (0,0), and write its cyclically ordered neighbours as x=(-1,0), u=(0,1), z=(1,0), v=(0,-1). Delete the four star edges at y; call the remaining graph K. Let Pi be the partition of these four terminals by K-open connectivity. For a specified partition pi, define Phi_p(pi) to be the conditional probability difference P(x connected to y)-P(x connected to z) after independently restoring the four star edges with parameter p. Then

    tau_1(p)-tau_2(p)=E[Phi_p(Pi)].

Let G=D4 act on the four terminal labels. The law of Pi is G-invariant because K and the iid edge law are invariant under all these rotations/reflections. Define

    barPhi_p(pi)=(1/8) sum_{g in G} Phi_p(g pi).

For each fixed g, invariance gives E[Phi_p(g Pi)]=E[Phi_p(Pi)]. Averaging proves

    tau_1(p)-tau_2(p)=E[barPhi_p(Pi)].                       (S)

This is an expectation identity. It does NOT assert Phi_p(pi)=barPhi_p(pi) for each pi, and no conditional symmetry after revealing the interior is assumed.

The only impossible terminal partition is the crossing pair xz|uv, by the planar face/Jordan argument already proved above. Thus pi belongs to the same 14 noncrossing partitions and six D4 orbits. Directly restoring all 16 subsets of star edges and averaging all 8 dihedral permutations yields

    4 barPhi_p(pi) = sum_{j=0}^4 C_{o(pi),j} p^j(1-p)^{4-j},

with the following complete INTEGER table:

|Orbit|C_0|C_1|C_2|C_3|C_4|
|---|---:|---:|---:|---:|---:|
|s (four singletons)|0|4|8|4|0|
|a (one adjacent pair)|0|6|8|2|0|
|b (one opposite pair)|-2|-2|2|2|0|
|g (two adjacent pairs)|0|8|4|0|0|
|d (triple plus singleton)|-2|2|3|1|0|
|e (all four together)|-4|0|0|0|0|

These are UNNORMALIZED Bernstein coefficients; no binomial factors are implicit in the displayed expansion. The table also follows from the earlier orbit formulas by dividing each orbit coefficient by its orbit size and multiplying by 4. An independent verifier reconstructs it from scratch using 8*16 DSU calculations for each of the 14 partitions.

### 2. Reveal one common finite interior

Let B=[-2,2]^2 and let E_B be its lattice edges, except the four removed star edges. There are 40-4=36 such edges. Expose their states once. Write pi_f for the resulting free partition of the terminals, and mark each block by whether its interior open component meets the vertex boundary of B. This complete visible state is h=(pi_f,hit).

Define A(h) to contain every noncrossing terminal partition r with the following two properties:

1. r coarsens pi_f: vertices in the same interior block remain connected;
2. whenever r merges two distinct pi_f blocks, BOTH blocks are boundary-reaching.

The actual full-K terminal partition Pi belongs to A(h). Indeed, an interior connection cannot be destroyed by adding exterior edges. Conversely an interior terminal cluster that never reaches the boundary cannot use an exterior edge: any path from it to outside B would first reach a boundary vertex, contradicting its definition. Thus such a block cannot merge with any other block. Connections among boundary-reaching blocks may use intermediate exterior or interior components not containing terminals; A(h) allows all such coarsenings, even if some are not realizable. That enlargement only weakens a lower bound. A(h) is nonempty because it contains pi_f. The true Pi is noncrossing by the global planarity argument.

For each h and j, put

    l_{h,j}=min_{r in A(h)} C_{o(r),j}.

Since p^j(1-p)^{4-j} is nonnegative,

    4 barPhi_p(Pi) >= sum_{j=0}^4 l_{h,j} p^j(1-p)^{4-j}.  (L)

The minimum is taken COEFFICIENTWISE, not by selecting a partition that depends on p. This makes (L) valid simultaneously for every p. It is deliberately conservative, and remains valid even if different coefficients attain their minima at different partitions. There is no independence assumption between Pi and h in (L).

### 3. Exact counting of the visible states

Let c_{h,k} count configurations of E_B with k open edges and visible state h. Since these 36 edges are iid,

    P_p(h)=sum_{k=0}^{36} c_{h,k}p^k(1-p)^{36-k}.

There are exactly 80 visible states with nonzero counts. All 80 coefficient arrays appear in joint_R2.json. The finite transfer recurrence that calculates them has the following invariant: at every step, active vertices carry their exact processed-edge connectivity partition and each component carries an OR flag recording whether it has touched a boundary vertex. Keep all four terminal marks forever, introducing every other vertex at its first incident edge and removing it immediately after its last incident edge. A vertex on the boundary begins with hit flag 1; other introduced vertices begin with flag 0. In the open branch, merge the two endpoint components and OR their hit flags. In the closed branch, do not merge. Then restrict the partition to the retained vertices and canonically relabel its components, retaining their flags. A component forgotten completely can never reconnect later, so discarding it is safe. This proves the invariant by induction over the edges. Counting closed branches in degree k and open branches in degree k+1 proves the recurrence counts each configuration exactly once with its correct state and open-edge count.

Explicit edge ordering: scan x=-2,...,2 and y=-2,...,2, skip y's central vertex (0,0), and append the horizontal edge from (x-1,y) when present and the vertical edge from (x,y-1) when present, omitting all four central-star edges. The code independently checks sum_h c_{h,k}=binomial(36,k) for every k. Reversing the entire edge ordering yields the SAME 80 arrays, coefficient for coefficient. Exhaustive enumeration of all 256 rim-edge configurations in the analogous radius-one punctured square checks both partition and hit flags against the transfer implementation.

Taking expectations in (L), using (S), and convolving the two finite expansions gives

    4[tau_1(p)-tau_2(p)] >= sum_{t=0}^{40} d_t p^t(1-p)^{40-t},
    d_t=sum_{h} sum_{k+j=t} c_{h,k} l_{h,j}.                (C)

Every quantity on the right is a finite integer. This is where the independence/product-measure realizability information missing from earlier abstract partition inequalities enters: the 80-state law is the law of an actual 36-edge patch, not an arbitrary associated terminal-partition distribution.

### 4. The exact integer certificate and conclusion

The full coefficient vector d_0,...,d_40 is:

    [0, 4, 148, 2640, 30160, 247338, 1547512, 7667748, 30845208, 102524812, 285288204, 671510680, 1348925352, 2332160230, 3501939952, 4616183220, 5410569388, 5718734248, 5518012068, 4888609184, 3959929024, 2894507102, 1876414204, 1061430556, 517519260, 215651364, 76294772, 22754084, 5664400, 1159528, 190720, 24300, 2256, 136, 4, 0, 0, 0, 0, 0, 0]

Here d_0=0 and d_35=...=d_40=0. For every j=0,...,33, exact integer comparison gives

    d_{j+1} >= 4 binomial(33,j).                            (I)

The minimal normalized reduced coefficient is exactly 4, attained at both ends. To see directly how this concludes the proof, substitute (I) into (C):

    4[tau_1-tau_2] >= 4 sum_{j=0}^{33} binomial(33,j)
                           p^{j+1}(1-p)^{39-j}
                    =4p(1-p)^6 [p+(1-p)]^{33}
                    =4p(1-p)^6.

Dividing by 4 proves (NEW), and strictness follows from 0<p<1.

### 5. Independent and formal checks of this proof

- verify_joint.py independently enumerates the 14 partitions, all 8 D4 actions and all 16 restored-star subsets. It rebuilds the integer orbit table and computes each coefficientwise minimum over A(h).
- The same verifier directly convolves each of the 80 visible-state count arrays with those integer minima. This result agrees with the independent normalized-Bernstein/grouped implementation in certify_joint.py.
- The 36-edge visible-state arrays agree under forward and reverse edge order; an exhaustive 8-edge radius-one calculation agrees with all partition/flag arrays. The radius-one lower bound is actually negative (-1/16), a useful check that the method has not assumed positivity.
- JointCertificate.lean checks the 34 integer dominance inequalities in (I) with `decide +kernel`; the theorem has NO axioms. It also checks list lengths and the sign lemma used in Approach B. No sorry and no native_decide are used. The explicit baseline integers are checked against Python math.comb; the binomial sum identity is proved above. Lean does NOT formalize the graph enumeration, symmetry argument or boundary coupling.
- All files and proof calculations remain inside the problem folder. This is a computer-assisted proof with transparent, small finite inputs, rather than a claim that the full probabilistic argument has been formalized in Lean.

### 6. What does not follow

The theorem covers exactly n=1 in d=2. The D4 orbit average works particularly well because the source is itself a neighbour of the deleted middle vertex. For a source at distance n>=2, rotations move the source to further axial vertices, and the observable involves more terminals; the same six-orbit table does not apply. Thus replacing 1 and 2 by arbitrary consecutive n is unjustified. Higher-dimensional stars also have extra neighbours and lose the single-face noncrossing restriction. No all-n or all-d result is claimed.

## Approach B: a finite obstruction, not a percolation counterexample

Let the five partitions of three boundary terminals be

    1|2|3, 12|3, 13|2, 23|1, 123.

The random-cluster boundary joining matrix M(q) has entry q^{number of blocks of pi join rho}. Directly joining these partitions gives

    M(q) = [[q^3,q^2,q^2,q^2,q],
            [q^2,q^2,q,q,q],
            [q^2,q,q^2,q,q],
            [q^2,q,q,q^2,q],
            [q,q,q,q,q]].

For v=(1,-1,-1,-1,2), multiplication yields

    v^T M(q) v = q^3-3q^2+2q = q(q-1)(q-2).

This is negative for every 1<q<2, because q>0, q-1>0 and q-2<0. At q=3/2 its exact value is -3/8. Therefore this boundary joining matrix is not positive semidefinite anywhere in (1,2). The generic reflection-positivity route cannot be justified by analytically continuing the integer-q boundary Gram matrix toward q=1. Moreover v^T M(q)v/(q-1) tends to -1 as q decreases to 1, so taking the first nontrivial derivative of the rank-one q=1 matrix does not repair that particular positivity argument. This is an obstruction to the proposed proof method, not a refutation of axial monotonicity. Symbolic matrix arithmetic is in reflection_join_obstruction.json; the real sign implication is checked in JointCertificate.lean.

This check also rejects the brain card's loose phrase suggesting the Potts representation automatically supplies reflection positivity for all real q>=1. Only the directly verified finite obstruction is used here; no broader reflection-positivity classification is asserted.


## Extension to the next distance: exact diagnostic and obstruction

To test whether the method closes the next inequality, use four collinear marks a=(0,0), d=(1,0), b=(2,0), c=(3,0). Reflection about x=3/2 swaps a with c and d with b. Translation invariance gives P(a connected to b)=P(c connected to d)=tau_2; P(a connected to c)=tau_3. Thus

    tau_2-tau_3 = E[(1{a~b}+1{c~d})/2 - 1{a~c}].

Reveal the full-edge interior rectangle [-1,4] times [-2,2], track its four-terminal partition and boundary-hit flags, and minimize this signed function over every coarsening among boundary-reaching blocks. Here no single-face noncrossing restriction on the four collinear marks is assumed; all 15 partitions are allowed. The exact counting recurrence, including hit flags, is the same validated recurrence, now with 49 random edges and the displayed half-integer signed observable. At p=1/2 this rigorous lower bound is

    -39996922331841/562949953421312 < 0
    (approximately -0.0710488065).

The free-interior averaged difference is positive (about 0.10936), but cannot replace the exterior-minimized bound. This computation does not prove or disprove tau_2>=tau_3.

A wider rectangle [-2,5] times [-3,3], with 97 edges, still yields a NEGATIVE lower bound:

    -1872483440877111655750557297/79228162514264337593543950336
    (approximately -0.0236340637).

Its free-interior averaged difference is about 0.09395. The wider job took 76.22 seconds, with peak 525503 connectivity states; it checked a 650 MiB RSS guard after each edge and had a 160-second time guard, below the user's per-job bounds. An earlier 350000-state version was stopped by its explicit state cap and is recorded as an incomplete budget-limited diagnostic, not a mathematical result. No further growth beyond these minute-scale tests was attempted. Exact values and box specifications are preserved in next_distance_R2_diagnostic.json and next_distance_R3_diagnostic.json.

The obstruction is more precise than simply "need a larger box": for n=2, boundary-hit flags permit too many adversarial exterior mergers. A possible stronger continuation would retain the cyclic locations at which each cluster meets the boundary, and enforce planar noncrossing restrictions on EXTERIOR mergers. Such constraints are not supplied by a four-terminal hit bitmask. No sufficient restriction of this kind is proved here.

## Why the first-step theorem does not automatically bootstrap

Even stationarity and the positive-definiteness of a connectivity/equivalence kernel do not promote a strict first comparison to all distances. Consider a stationary random equivalence relation on Z, selected as this mixture:

- with probability 3/8, put every integer in one equivalence block;
- with probability 3/8, use the three congruence classes modulo 3;
- with probability 1/4, use the clusters of iid p=1/2 nearest-neighbour percolation on Z.

Each component law is stationary, so the mixture is stationary. Each has a positive-semidefinite equivalence kernel, hence so does the mixture (the cluster-sum-of-squares argument already proved in the read-only spectral audit). Its connection sequence is

    f_n=3/8+(3/8)1{3 divides n}+(1/4)2^{-|n|},

giving f_1=1/2, f_2=7/16, f_3=25/32. Thus f_1>f_2 but f_3>f_2. This is a precise obstruction to bootstrapping using stationarity/positive definiteness alone, not a Z^2 percolation counterexample: the congruence classes are not clusters of nearest-neighbour bond percolation on Z^2. Exact fractions are recorded in bootstrap_obstruction.json.

## Final hostile-referee audit of the continuation

1. D4 averaging is justified before revealing the finite interior, using the unconditional full-K law. It is not silently imposed on a conditioned exterior law. Independently, all 80 finite visible-state arrays were verified to transform correctly under all 8 D4 actions.
2. Boundary flags indicate that a terminal's ENTIRE interior cluster reaches the boundary, not merely that the terminal itself lies on it. They propagate by OR when components merge and survive forgetting boundary vertices. Independent exhaustive enumeration of a 12-edge radius-two rim-plus-spokes subgraph checks all 4096 configurations, including genuine hit and non-hit blocks; all 74 final arrays agree.
3. An independent generator first partitions only the boundary-reaching interior blocks, leaves every other block alone, lifts the result to terminal labels and removes crossing partitions. For every one of the 80 states this gives exactly the same allowed-coarsening set as the pairwise-condition implementation.
4. The coefficientwise minimum is a lower bound because each p^j(1-p)^{4-j} is nonnegative. Minima of individual coefficients need not come from the same partition; that only makes the bound weaker and never invalidates it.
5. The integer score table is an orbit-AVERAGED signed observable, using per-partition orbit division. Its independently enumerated D4/star result agrees with the orbit formulas; the radius-two law and final convolution do not use an abstract FKG-only partition relaxation.
6. The 36-edge arrays total binomial(36,k) in every degree and agree after reversing the edge ordering. The final 41 coefficients are independently recomputed via integer convolution, rather than inferred from point samples.
7. All 34 integer comparisons to 4*binomial(33,j) passed `decide +kernel`. Lean's finite comparison theorem has no axioms. Only these numerical inequalities, list lengths, and the reflection-join sign lemma are formally checked; the full computer-assisted percolation theorem also relies on the complete written coupling and exact transfer algorithm above.
8. The n=2 negative LOWER bounds and the q-join/mixture obstructions are not counterexamples to G0008. No claim of all-distance or higher-dimensional closure follows from the new n=1 theorem.

## Final remaining gap after this serious continuation

The first inequality tau_1(p)>tau_2(p) is now proved uniformly for 0<p<1 on Z^2, quantitatively with gap at least p(1-p)^6. Together with the elementary tau_0>tau_1, this covers exactly n=0,1. The next unresolved target in this work is

    tau_2(p) >= tau_3(p) for every 0<p<1 on the infinite Z^2 lattice,

already unresolved by the new finite common-boundary method at p=1/2. Ultimately G0008 requires every n>=2 and the analogous higher-dimensional question. No counterexample was found and no complete proof was obtained. Final disposition of this continuation is STATE: DONE, VERDICT: PARTIAL, with a strictly stronger proved special case than before.
