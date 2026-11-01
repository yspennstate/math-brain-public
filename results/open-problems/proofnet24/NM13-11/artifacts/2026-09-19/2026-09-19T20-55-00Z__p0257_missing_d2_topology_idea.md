# P0257 research idea — missing directed-2NN sink topology

Before writing a checker, test a route that is structurally different from the preceding capsule refinement.

The current lower-bound package already charges several vertex-disjoint sink strongly connected components (SCCs) of the directed two-nearest-neighbor graph D2. The immediately preceding non-C4 four-point class has normalized nearest-two topology

`((1,2),(0,2),(1,3),(1,2))`,

while the older bidirected-C4 class has topology

`((1,3),(0,2),(1,3),(0,2))`.

Try to realize a third, non-isomorphic D2 sink topology on a positive-measure, deliberately asymmetric four-point family and add its Hamiltonian boundary surcharge rather than improve another guard constant on an already-counted family.

Normalize

`p1=(0,0), p2=(1,0)`,

`p3=(x,y)` with `11/25 <= x <= 49/100`, `-51/50 <= y <= -47/50`,

`p4=(z,w)` with `9/10 <= z <= 49/50`, `-8/25 <= w <= -11/50`.

The target nearest-two sets are

`N2(p1)={p2,p4}, N2(p2)={p1,p4}, N2(p3)={p1,p4}, N2(p4)={p2,p3}`,

which is strongly connected and not isomorphic to either previously charged four-point topology. The inequalities to certify are deliberately low-dimensional: `x<1/2`, `d13>1`, `d13>d14`, `z>1/2`, and `d14>d34`.

If those inequalities have uniform rational slack, take a common internal second-neighbor bound `U`, an external guard radius `H>U`, and use the existing topology-independent sink-SCC boundary mechanism: every non-endpoint sink SCC forces at least two Hamiltonian path boundary crossings, each paying at least `(H-U)s` over the degree-two nearest-neighbor floor. Count accepted ordered quadruples, divide by `4!`, and transfer through the exact finite binomial model before integrating the full scale variable.

Actual Section-B routes being tested in this run:

- #3 PROVE SOMETHING STRONGER: formulate the surcharge at the level of any guarded D2 sink SCC, independent of its internal topology.
- #15 BREAK THE SYMMETRY ON PURPOSE: seek an asymmetric topology absent from the C4/chain classes.
- #25 COUNT THE SAME THING TWICE: count the same accepted object both as an ordered geometric quadruple (for expectation) and as a unique sink SCC (for no-overlap charging).

No success, metric movement, or finite certificate is claimed by this idea note. The next step is exact arithmetic only if the proposed topology survives all uniform inequalities.