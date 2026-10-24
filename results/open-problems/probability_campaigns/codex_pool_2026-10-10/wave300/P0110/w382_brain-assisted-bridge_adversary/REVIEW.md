# Independent adversary review for w381 and w383

2026-10-10. w382. Independent obstruction saved in INDEPENDENT_OBSTRUCTION.md before reading w381/ATTEMPT.md. This review concerns L1--L5 in that file, headed 'terminal-bias bridge, with a supporting sphere'. It is not a review of w383's review.

Verdict: KEEP as conditional finite-scale deductions. No counterexample to L1--L5 was found. These deductions do not solve P0110. The remaining premise for a conditional global closure is matching both global exponent pairs for one eligible nondegenerate iid law, using the theorem's exact lower-bound convention. A suitable law's weight-support admissibility and a directional upper bound do not establish that premise.

Concrete source-hypothesis boundary: SMALL_DISPLACEMENT_OBSTRUCTION.md shows that Uniform[1,2] fails the literally printed Auffinger--Damron (2.2) wandering lower bound over every nonzero displacement, since D(0,e_1)=0. The adjacent direct edge costs at most 2, every alternate path costs at least 3. Thus w381's 'eligible' candidate is eligible for the weight-support assumptions and for L1--L5, not for the complete printed global-exponent premise. Chatterjee's (A4) explicitly excludes a sufficiently large ball's interior and avoids this finite obstruction. This distinction does not change the conditional L1--L5 verdict or establish asymptotic matching. New boundary-case deduction awaits w383.

L1 and L2, separately derived: translation invariance and subadditivity give h(mx)<=m h(x), hence g(x)<=h(x). For a vertex z of a minimizing path, T(0,v)=T(0,z)+T(z,v). Substitute T(x,y)=g(y-x)+b(y-x)+X(x,y) and rearrange. The detour equals b(v)-b(z)-b(v-z)+X(0,v)-X(0,z)-X(z,v). Since both internal biases are nonnegative, only the terminal bias must be bounded from above. Signs are correct.

L3, separately derived: for projection inside the segment, S>=sqrt(L^2+4r^2), so S-L>=4r^2/(S+L)>=2r^2/S. For projection outside, the distance to the nearer endpoint is r, and the distance to the farther endpoint is at least L AND at least r. The first fact gives S-L>=r; the second gives S>=2r. Thus S-L>=2r^2/S. The farther-endpoint distance >=L is the small missing explanation in w381's prose, not a missing hypothesis or a counterexample. This handles overshoots as well as perpendicular departures.

L4, separately checked: minimizing g on the Euclidean unit sphere gives rho>0, g(x)>=rho|x| and g(u)=rho for at least one unit vector u. Since g(x)<=b||x||_1, rounding nu contributes at most bd/2 to g(v_n), and ||v_n|-n|<=sqrt(d)/2. Thus g(v_n)-rho|v_n| is between zero and K0. The bounded positive edge law gives a deterministic maximum length (b/a)||v_n||_1 for EVERY minimizing path. Their vertices satisfy S<=C|v_n|, C=(b/a)sqrt(d). Combining these facts with L3 gives the stated lower quadratic detour minus K0.

L5, separately checked: all possible vertices lie in deterministic Lambda_n. Translation invariance permits applying the same centered exponential bound to X(0,z) and X(z,v_n). Distances are <=(C+1)|v_n|, so q>=0 makes the envelope denominator valid. There are at most 2|Lambda_n|+1 terms. A union bound works despite dependence. No bound is conditioned on z being a selected geodesic vertex. L2 and L4 yield the threshold and exponent exactly as written. Zero-displacement terms vanish. If a=b the geometry proof still works, but the degenerate law is excluded as a P0110 witness. If a=0 the deterministic length argument requires a new premise and this proof does not apply.

Two concrete failed closure routes:

1. Moment estimates alone cannot imply matching uniform exponential upper and moment lower exponents. INDEPENDENT_OBSTRUCTION.md gives exact scalar endpoints (1/2,1/4,3/4,1/2). It is a counterexample to that abstract implication, not to iid FPP.
2. Existence of a supporting direction cannot be promoted to a curvature bound in every direction. In R^2 set g=||.||_1, v=(n,n), z=(n/2+r,n/2-r), 0<r<n/2. Then g(z)+g(v-z)-g(v)=0 but dist(z,[0,v])=sqrt(2)r>0. Thus no positive quadratic lower detour bound is uniform over directions merely because g is a norm. The norm example does not assert an eligible continuous iid FPP law has this shape.

Additional conditional deduction for referee w383: CONDITIONAL_EXPONENTIAL_UPGRADE.md converts the full L5 tail to a uniform exponential moment along v_n at every exponent strictly above (1+q)/2. It still supplies no global matching or lower bound. It is an original derivation in this packet and remains unreviewed.

NEXT: w383 independently check the rare-tail obstruction and exponential upgrade; if retaining the conditional route, isolate the global lower/upper matching premise rather than replace it with a variance limit.
