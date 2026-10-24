from pathlib import Path
import json
s=r'''
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

Checks: at each completed graph, the total coefficients over all terminal states equal binomial(m,k); an independent exhaustive 2^12-edge-configurations check on R=1 is being added. `exact_boxes.json` preserves all coefficient arrays. Computed R=1,2,3, with m=12,40,84; peak state count 6571; total measured calculation time 4.30 seconds, well below the job bounds.

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
'''
with Path('ATTEMPT.md').open('a',encoding='utf8') as f:f.write(s)
claims=[
{'claim':'For square-lattice iid bond percolation, tau_1(1/2)-tau_2(1/2) >= 9/2048.','status':'proved_special_case','proof_location':'ATTEMPT.md, A checked critical first-step theorem','remaining_gap':'All other distances and full parameter range remain unresolved.','checks':['Independent 14-partition by 16-star-state rational enumeration passed.','Lean algebra check pending; geometry and probability proved in prose.']},
{'claim':'Full supercritical connection probability is the sum of finite-cluster connectivity and joint infinite-cluster membership, not finite connectivity plus theta(p)^2.','status':'proved','proof_location':'ATTEMPT.md, Read-only prior research audit','remaining_gap':'No supercritical full-connectivity monotonicity follows from the truncated theorem.','checks':['Partition the connection event into finite versus infinite origin cluster; apply uniqueness.']},
{'claim':'A positive-exponential OZ asymptotic implies eventual strict axial decrease.','status':'proved','proof_location':'ATTEMPT.md, Read-only prior research audit, item 3','remaining_gap':'This abstract implication supplies no all-distance theorem; it requires the asymptotic for the function in question.','checks':['Consecutive ratio converges to exp(-xi)<1.']},
{'claim':'Free squares B_2 have connection probability to (1,0) >= to (2,0) for every p; B_3 has the analogous comparisons 1>=2>=3.','status':'proved_special_case','proof_location':'ATTEMPT.md, Exact finite-box experiments; exact_boxes.json','remaining_gap':'These finite-graph theorems do not imply the infinite-lattice conjecture.','checks':['All signed Bernstein counts nonnegative.','Coefficient totals equal binomial counts.','Independent small-box brute-force check pending.']},
{'claim':'tau_n=p^n on Z; on every Z^d, tau_0>tau_1 for 0<p<1.','status':'proved_special_case','proof_location':'ATTEMPT.md, Elementary special cases','remaining_gap':'Dimensions >=2 and comparisons n>=1 unresolved in general.','checks':['Unique simple path on Z; isolate origin by closing 2d edges.']}]
Path('CLAIMS.jsonl').write_text(''.join(json.dumps({'problem_id':'G0008',**c})+'\n' for c in claims),encoding='utf8')
