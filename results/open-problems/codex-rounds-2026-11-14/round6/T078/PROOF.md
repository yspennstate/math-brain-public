# Sparse injections with isolated removed sites

All distances below are the maximum norm on the cubic lattice. Edges have conductance one, and each undirected edge is counted once in the energy. A current is antisymmetric: J(v,w)=-J(w,v). Write

    div J(v)=sum_{w~v} J(v,w),
    E(J)=sum_{unordered edges {v,w}} J(v,w)^2.

For a vertex set U, only edges with both endpoints in U belong to its graph. Its Dirichlet energy is

    D_U(f)=sum_{{v,w} subset U, v~w} (f(v)-f(w))^2.

Functions in a finite Dirichlet problem are extended by zero to the rest of U. Edges to removed vertices contribute nothing.

## 1. Statement

Let Z be any subset of Z^3 such that

    |z-z'|>=3 whenever z,z' in Z are distinct,             (1)

and put U=Z^3\Z. The set Z may be infinite. There is a fixed linear operator T, depending only on Z, from full-lattice currents with zero divergence on Z to currents on U such that

    div_U(TJ)(v)=div J(v) for v in U,
    E_U(TJ)<=7 E(J).                                    (2)

No optimality of the constant 7 is asserted.

Here is its consequence for the sparse injections of round 5. Let I be finite, m=|I|, and let x_i in Z^3 be labels, with repetitions allowed. Suppose L>=0, 0<=alpha<1 and

    #{i: |x_i-x|<=r}<=L(1+r)^alpha                      (3)

for every x in Z^3 and real r>=0. Let mu_i be finitely supported nonnegative measures on U with total mass at most one, supported within distance R>=0 of x_i. Set g=sum_i mu_i. Then there are unit currents J^a on U, one for each a in the support of g, whose aggregate K=sum_a g(a)J^a satisfies

    div_U K=g,
    E_U(K)<=[7000 L/(1-alpha)](1+R)^alpha m.             (4)

The same upper bound holds for the energy of the solution of the killed Dirichlet problem in every finite Omega subset U containing the support of g. Labels need not belong to U. The assertion concerns the positions of injected mass, which do belong to U.

For a nonempty finite S subset U satisfying (3) as distinct labels, define

    cap_U(S)=inf{D_U(f): f finitely supported on U,
                         f>=1 on S}.

Then

    cap_U(S)>=[(1-alpha)/(7000 L)] |S|.                 (5)

## 2. Independent verification of the full-lattice input

This section rechecks the estimate in [round 5 PROOF.md](~/codex_op_1114r5/briefs/T078/PROOF.md). Let A be the full-lattice Laplacian, Af(v)=sum_{w~v}(f(v)-f(w)). The continuous-time walk with generator -A jumps along each edge at rate one. Denote its transition kernel by p_t and put G(x)=integral_0^infinity p_t(x)dt.

The bounds needed from its explicit heat-kernel argument are

    G(x)<=3,             G(x)<=432/|x| if |x|>0.         (6)

Here are the constants checked directly. Independent coordinate Poisson walks and one-dimensional Fourier inversion give

    sup_x p_t(x)<=min(1,t^(-3/2)).

Indeed 1-cos(theta)>=2theta^2/pi^2 on [-pi,pi], so the one-dimensional kernel is at most sqrt(pi)/(4sqrt(t)); multiply three such bounds. Integration in time gives G(x)<=3 for every x. The coordinate moment generating function is exp[2t(cosh(lambda)-1)], and cosh(lambda)-1<=lambda^2 for 0<=lambda<=1. Chernoff with lambda=min(a/(4t),1), followed by the union bound over three coordinates, yields

    P(|X_t|>=a)<=6 exp[-min(a^2/(8t),a/2)].

In p_t(x)=sum_w p_{t/2}(w)p_{t/2}(x-w), one of |w| and |x-w| is at least |x|/2. Thus, with r=|x|>=1,

    p_t(x)<=12 min(1,(t/2)^(-3/2))
                  exp[-min(r^2/(16t),r/4)].

Integrating on t<=r/4 gives 3r exp(-r/4)<=48/r: the maximum of r^2 exp(-r/4) is 64 exp(-2), and e>2. On t>=r/4 use the second power in the minimum prefactor and enlarge the interval to (0,infinity). Since

    integral_0^infinity t^(-3/2)exp[-r^2/(16t)]dt
       =4sqrt(pi)/r,

this contribution is at most 96sqrt(2pi)/r<384/r. This proves (6). The first part of (6), which is stronger near the origin, was not used in round 5's final rounding. For r<=144 use 3(1+r)<=435; for r>=144 use 432(1+r)/r<=435. Consequently

    G(x)<=435/(1+|x|) for every x.                      (7)

Now compute interactions between labels, instead of estimating the potential at an arbitrary displaced endpoint. If a is in the support of mu_i and b in that of mu_j, the triangle inequality gives

    |a-b|>=(|x_i-x_j|-2R)_+.

The mass bound therefore implies

    Q(g):=sum_{a,b}g(a)G(a-b)g(b)
       <=435 sum_{i,j} [1+(|x_i-x_j|-2R)_+]^(-1).       (8)

For fixed i, the elementary identity

    [1+(d-2R)_+]^(-1)
       =integral_{2R}^infinity 1_{d<=s}/(1+s-2R)^2 ds

and (3), centered at x_i, bound the inner sum in (8) by

    L integral_0^infinity (1+2R+t)^alpha/(1+t)^2 dt
       <= L(1+2R)^alpha/(1-alpha).

The last inequality follows from 1+2R+t<=(1+2R)(1+t) and integration of (1+t)^(alpha-2). Since 2^alpha<=2,

    Q(g)<=870 L(1+R)^alpha m/(1-alpha)
         <=1000 L(1+R)^alpha m/(1-alpha)=:C_g.          (9)

This independently recovers the earlier reported bound, even with a smaller coefficient. It includes alpha=0 and repeated labels.

For clarity, Q(g) supplies actual currents. In a finite full-lattice box B containing the support of g, the killed matrix A_B has diagonal 6. Grouping the two endpoint terms of each edge gives

    <f,A_B f>=D_{Z^3}(f).

It is positive definite because a finite-support function of zero energy must be constant on the connected infinite lattice, hence zero. The inverse is the time integral of the killed walk kernel, and is entrywise bounded by G. For u_B=A_B^(-1)g this proves

    D_{Z^3}(u_B)=<g,u_B><=Q(g).

On an increasing exhaustion, the killed kernels increase to G: every finite-time walk has finitely many jumps. Hence u_B converges pointwise to u(x)=sum_a G(x-a)g(a). Its gradient J(v,w)=u(v)-u(w) has div J=g by passage through the finite six-term sum at each fixed vertex, and E(J)<=Q(g) by Fatou. Applying this construction to delta_a gives unit currents whose finite weighted sum is precisely J. This proves all the full-lattice input needed in (4).

The coefficient in the energy identity can be checked without the walk: for B={0}, A_B=[6], D(delta_0)=6 and the unit-source solution has energy 1/6. The initial holding time of the rate-one-per-edge walk also has mean 1/6.

## 3. Explicit bypasses around one removed site

First take the hole at 0. Let e_1,e_2,e_3 be the coordinate unit vectors and choose a=e_1 as a hub. For each other neighbor v of 0 choose the following directed path from v to a:

    P_{-e_1}: -e_1, -e_1+e_2, e_2, e_1+e_2, e_1;
    P_{ e_2}:  e_2,  e_1+e_2, e_1;
    P_{-e_2}: -e_2,  e_1-e_2, e_1;
    P_{ e_3}:  e_3,  e_1+e_3, e_1;
    P_{-e_3}: -e_3,  e_1-e_3, e_1.

Every step is a nearest-neighbor step. All vertices lie in the radius-one cube B_1(0) and avoid 0. Only the first two paths share edges, namely their last two edges, in the same direction. The first two edges of P_{-e_1} occur nowhere else. The other three paths have disjoint edge sets, also disjoint from the first two.

For a directed path P, let I_P be its current, equal to +1 along each directed step, -1 in reverse, and zero elsewhere. At each internal vertex its incoming and outgoing contributions cancel, so div I_P=delta_start-delta_end.

Suppose div J(0)=0, and put s(v)=J(v,0) for the six neighbors. Antisymmetry implies sum_v s(v)=0. Define

    Delta=sum_{v~0,v!=a} s(v) I_{P_v}.

At each neighbor v!=a, its divergence is s(v), and at a it is -sum_{v!=a}s(v)=s(a). It vanishes elsewhere. Thus Delta replaces exactly the divergence at neighbors lost by deleting the star through 0.

Write b=s(-e_1), c=s(e_2), d=s(-e_2), e=s(e_3), f=s(-e_3). The stated edge overlaps give the exact identity

    E(Delta)=2b^2+2(b+c)^2+2(d^2+e^2+f^2)
       <=6b^2+4c^2+2(d^2+e^2+f^2)
       <=6 sum_{v~0}s(v)^2.                            (10)

The first inequality is (b+c)^2<=2b^2+2c^2. The omitted hub square is nonnegative. Cancellation or negative values of the s(v) cause no problem.

As an algebraic check of the coefficient six, the matrix for the b,c part is [[4,2],[2,2]]. Its characteristic polynomial is lambda^2-6lambda+4, with roots 3+sqrt(5) and 3-sqrt(5). Both are at most six. The other three diagonal coefficients are two, giving the same upper bound independently of the inequality used in (10).

## 4. All holes and the energy bound

Translate the preceding construction to every z in Z, with hub a_z=z+e_1. The cubes B_1(z) are vertex-disjoint by (1): a common vertex would give |z-z'|<=2. Each cube contains no other hole. In particular all bypass paths are in U and their edge sets for different holes are disjoint.

Let J_0 be J restricted to the edges of U and let Delta_z be its translated correction, formed using the original star values J(v,z). Define

    TJ=J_0+sum_{z in Z} Delta_z.

This defines a current even for infinite Z: each edge belongs to at most one bypass cube. The construction is linear. At a surviving vertex x, only finitely many edges are incident. Deleting hole edges removes divergence sum_{z~x,z in Z}J(x,z), and the corrections add that same quantity by Section 3. Hence div_U(TJ)(x)=div J(x).

Let E_*=sum_{z in Z}sum_{v~z}J(v,z)^2. No edge joins two holes, so these stars count each deleted edge exactly once, and

    E(J)=E_U(J_0)+E_*.

The disjoint bypass supports and (10) give E_U(sum_z Delta_z)<=6E_*. The triangle inequality in the edge square-summable space, followed by the two-dimensional Cauchy-Schwarz inequality, now gives

    E_U(TJ)
       <=(sqrt(E_U(J_0))+sqrt(6E_*))^2
       <=(1+6)(E_U(J_0)+E_*)=7E(J).                    (11)

The final inequality also checks by subtraction: its right side minus the preceding squared expression is (sqrt(6E_U(J_0))-sqrt(E_*))^2>=0.

For infinite sums, these inequalities follow first for partial sums of corrections and then by convergence in the square-summable edge space, since their disjoint energies have finite total. If E(J)=infinity the asserted bound is vacuous; the finite-energy case establishes (2).

Apply T to each full-lattice unit current at an injection site a in U. Its divergence at every hole is zero. Linearity and (9)-(11) yield the aggregate in (4), including collisions of injection endpoints. No factor m is lost by summing the individual current energies: the energy estimate is applied to the aggregate full-lattice current itself.

## 5. Independent dual check of the factor seven

There is a matching extension inequality for test functions. Given a finite-support real f on U, define F on the full lattice by

    F(v)=f(v) for v in U,       F(z)=f(a_z) for z in Z.

The hubs a_z are distinct, so F has finite support. Each star term at z, except for its zero hub term, is (f(v)-f(a_z))^2. Telescoping along P_v and applying Cauchy-Schwarz bound this term by the length of P_v times the sum of squared differences along that path.

The length of P_{-e_1} is 4 and each other length is 2. Its first two edges have coefficient 4, the two edges shared with P_{e_2} have coefficient 4+2=6, and all other bypass edges have coefficient 2. Therefore

    sum_{v~z}(F(v)-F(z))^2
       <=6 sum_{edges in the bypass cube at z}(df)^2.

The bypass cube edge sets are disjoint between holes. Adding the surviving-edge energy proves

    D_{Z^3}(F)<=7D_U(f).                               (12)

This checks the factor seven using path lengths and test functions, without calculating correction-current squares. It also yields the same source-energy comparison directly. For the full-lattice aggregate current J of Section 2, finite summation by parts gives

    sum_x g(x)f(x)=sum_x g(x)F(x)
       =sum_{full-lattice edges} J(v,w)(F(v)-F(w)).

Only finitely many terms on the right are nonzero. Cauchy-Schwarz, (9) and (12) imply

    (sum_x g(x)f(x))^2<=7C_g D_U(f).                   (13)

There is thus a second proof of the bound on finite-volume source energy below.

## 6. Finite volumes and capacity

The graph on U is connected and infinite. To see connectedness, take any finite full-lattice path between surviving vertices. Whenever it uses a two-edge segment v,z,w through a hole, replace that segment by P_v followed by the reverse of P_w, using a length-zero path if a neighbor is the hub. The replacement lies in U. No two holes are adjacent, and each bypass cube contains no other hole, so this gives a finite walk in U between the endpoints. There are infinitely many surviving vertices: already the neighbors z+e_1 of distinct holes are distinct surviving vertices if Z is infinite, while finite Z removes only finitely many lattice sites.

For finite Omega subset U define

    (A_{Omega,U}f)(v)=sum_{w~v,w in U}(f(v)-f(w)),

with f=0 on U\Omega. Its diagonal is the degree of v in U, not necessarily six. Grouping endpoint terms gives <f,A_{Omega,U}f>=D_U(f). If this is zero, f is constant along every edge of U; connectivity and its finite support force f=0. Thus A_{Omega,U} is positive definite and invertible.

Let u=A_{Omega,U}^(-1)g when the support of g is contained in Omega, and put E_Omega=D_U(u)=sum g u. Substituting f=u in (13) gives

    E_Omega^2<=7C_g E_Omega.

If E_Omega=0 the upper bound is immediate; otherwise divide to obtain E_Omega<=7C_g, as asserted in (4). No assumption that Omega contains bypass cubes is required: the zero extension to U and then F is a finite-support test function on the full lattice. This handles sources arbitrarily close to the Dirichlet boundary.

Alternatively, use the rerouted current K in summation by parts on U:

    E_Omega=sum g u=sum_{edges of U}K(v,w)(u(v)-u(w)).

Cauchy-Schwarz and E_U(K)<=7C_g give the same bound. This is a third check of the finite-volume convention.

For (5), set R=0, let labels be the points of S, and use mu_i=delta_{x_i}. For f>=1 on S,

    |S|^2 <= (sum_{x in S} f(x))^2
       <=[7000 L/(1-alpha)] |S| D_U(f)

by (13). Cancel |S|>0 and take the infimum over f. Here L>=1 follows from (3) at a label and r=0. The empty-set capacity is zero and needs no division by L.

## 7. Tests and limits of the statement

For Z empty the construction is the identity. For one hole the five explicit paths verify every sign in the divergence calculation, including the hub equation. Stars with arbitrary signed currents are included. If two holes are exactly distance three apart, their radius-one cubes remain vertex-disjoint; a lattice edge joining the two cubes is unmodified and does not enter either correction. Infinite Z is allowed because the supports of corrections are disjoint and the extension of a finite-support test function adds at most one hole for each nonzero hub value.

For Omega={v} and v adjacent to one hole, the killed operator is [5]. A unit source therefore has energy 1/5. On the full lattice in the same one-site volume it has energy 1/6. This explicitly checks the deleted-edge convention and confirms that a full-lattice Green upper bound cannot simply be reused by deletion monotonicity.

The separation condition has geometric content. If arbitrary nearby holes are permitted, take

    Z={e_1,-e_1,e_2,-e_2,e_3,-e_3},       y=0.

Then y is an isolated surviving vertex, so the divergence of every current on U at y is zero. There is no unit current from y to infinity. Yet the radius-eight component of each hole has diameter two, so a uniform component-diameter bound alone holds with C=2 and nu=0. This example does not contradict the source: its additional local hypothesis is a strict count <2d, which here fails already in the radius-one ball about y (six holes in d=3). It shows why that hypothesis cannot be discarded during a generalization.

No result for clusters of neighboring removed vertices is inferred from the present construction. At distance two the bypass cubes may overlap, so the disjoint-energy proof used here no longer applies. This identifies a limitation of the construction, not a counterexample to a distance-two theorem.

## 8. Relation to the source dependencies

The read source revision is `4eaee87548250b2682affda7d05d947c05554bae`. In [RegularComponents.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/RegularComponents.lean), `Regular Z x R M nu` requires fewer than 2d removed sites in every radius-M ball centered within B_{11R}(x), and a remote radius-eight component envelope outside B_{10R}(x). The theorem `regular_component_envelope` produces the bound (16d+2)(1+|z-y|)^nu for component displacements, when |x-y|<=R.

In [FlowCongestion.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/FlowCongestion.lean), `connected_envelope` combines a locally accessible source with `routed_envelope`. The latter is in [FlowRouting.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/FlowRouting.lean), and uses the general hull routing in [HullRouting.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/HullRouting.lean). Those steps permit nontrivial components; their full assertions have not been proved here.

The present result supplies the aggregate-current role used by [RegularKernels.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/RegularKernels.lean), `regular_injection_energy`, for a different, explicitly restricted class of perforations. It keeps every 0<=alpha<1, requires no local counting hypothesis on holes beyond (1), and gives a uniform operator energy comparison. In particular it covers any source instance whose removed sites additionally satisfy (1). Its undirected energy is half the sum of squares of both antisymmetric darts; numerical constants are not equated with the source's conventions. No novelty claim is made for bounded local rerouting.

Condition (1) is a local geometric alternative, not an implication of Regular or a substitute for its radius-eight component envelope. For example, finite portions of 3Z^3 satisfy (1) but have arbitrarily large radius-eight connected components. The source permits nearby holes within controlled components, whereas (1) excludes those nearby configurations. The overlap of the two classes is covered by the theorem above.

Random removed-site regularity, the loop return estimate, the magnetization tail and the infinite-volume equilibrium argument are not established by this theorem. It does not prove spontaneous magnetization for the quantum Heisenberg ferromagnet.
