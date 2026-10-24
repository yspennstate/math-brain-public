# A local attracting-face selection lemma for frozen endpoint dynamics

Status: PROVED (internal), independently audited in reviews/e04_face_review.md. This pays a local boundary-selection step for the nonorthogonal T384 route. It is not the self-consistent stochastic training theorem. The convex-flow mechanism and Schur complement are standard mathematical mechanisms; no novelty is claimed for them.

## Definitions and local hypotheses

Let X have k linearly independent rows x_j, with G=XX^T. Freeze a nonzero endpoint weight z and residual r in R^k. The endpoint hidden-state field off activation boundaries is

u'=z sum_j r_j 1{x_j·u>0}x_j.                       (1)

Choose disjoint index sets P,B,N partitioning {1,...,k}. Work near a face where x_j·u>0 for j in P, x_j·u=0 for j in B, and x_j·u<0 for j in N. Suppose B is nonempty and z r_j<0 for each j in B. Define

q_B^*=-G_BB^(-1)G_BP r_P,
theta_j^*=q_j^*/r_j, j in B,                       (2)

and assume 0<theta_j^*<1 for every j in B. These are explicit strict attraction/feasibility hypotheses. They fail at repelling or degenerate faces; no claim covers those cases.

Let Pi_T be orthogonal projection onto ker X_B and Pi_N=I-Pi_T. Set

a_P=z sum_(j in P)r_j x_j,
c_j=-z r_j>0,
delta=min_(j in B)c_j min(theta_j^*,1-theta_j^*)>0.

G_BB is positive definite by the row independence assumption. Equation (2) says

Pi_N a_P=sum_(j in B)c_j theta_j^* x_j.              (3)

All statements below are restricted to the interval before a P or N projection changes sign. The local model treats those signs as fixed. For data starting sufficiently close to the relative interior of the face, this interval includes the short capture interval described below, since velocities are bounded and strict P,N margins persist for a sufficiently short time.

## Inclusion, existence, uniqueness, and finite-time capture

With the P,N signs fixed, define the convex globally Lipschitz polyhedral function

phi(u)=sum_(j in B)c_j(x_j·u)_+ - a_P·u.             (4)

The Filippov set of (1) in this neighborhood is exactly -partial phi(u). Indeed all 2^|B| sign choices of the B projections are locally realizable because X_B has independent rows; convexifying their limiting vectors permits independent theta_j in [0,1] at zero, while theta_j is 0 or 1 at negative or positive projections. These are precisely the convex subgradients in (4). This equality uses the frozen residual and endpoint weight; it is not an assertion about arbitrary nonsmooth neural-network losses.

The inclusion u' in -partial phi(u) has a unique global absolutely continuous solution in the frozen-sign model. Here is a self-contained argument. Every subgradient has norm at most M=||a_P||+sum_j c_j||x_j||. Explicit Euler polygons, selecting any subgradient at each node, are uniformly M-Lipschitz on finite intervals, hence have uniformly convergent subsequences. Their selected subgradients have weak-star convergent subsequences in L-infinity. The convex inequality phi(v)>=phi(u_node)+g_node·(v-u_node), integrated on arbitrary measurable time sets, passes to the limit because phi is Lipschitz and the node-to-polygon distance is at most Mh. First use countably many rational v, then continuity in v, to obtain g(t) in partial phi(u(t)) a.e. Passing through the integral update gives u'=-g. For two such solutions, convex-subgradient monotonicity gives

d/dt (||u-v||^2/2)=-(u-v)·(g_u-g_v)<=0.

Equal initial values therefore give uniqueness. Compactness and uniqueness show every sequence of Euler polygons with h->0 converges uniformly to that solution. This proves existence and vanishing-step selection in the local frozen-sign model without invoking an unproved nonsmooth-flow theorem.

Set w=Pi_N u; then X_Bu=X_Bw. The tangential velocity is constant, Pi_T u'=Pi_T a_P. Using (3), and any allowed theta_j at zero,

w'=-sum_(j in B)c_j(theta_j-theta_j^*)x_j,
(1/2)d||w||^2/dt
 =-sum_j c_j(theta_j-theta_j^*)(x_j·w)
 <=-delta sum_j |x_j·w|
 <=-delta sigma_min(X_B)||w||.                     (5)

Here sigma_min(X_B)>0 denotes the smallest positive singular value; w lies in the row space of X_B, where ||X_B w||_2>=sigma_min(X_B)||w||. For ||w||>0 the chain rule gives d||w||/dt<=-delta sigma_min(X_B). Thus capture occurs by

tau <= ||Pi_N u(0)||/[delta sigma_min(X_B)],         (6)

provided no P,N sign change occurs first. Once captured, w=0 persists: equation (2) supplies a zero normal velocity, and uniqueness makes this the continuation. This proves strict attraction, not merely feasibility of a chosen tangent vector.

## The selected velocity and its output action

On the captured face, independence of the B rows makes the unique tangent choice theta_B=theta_B^*. In projected coordinates V=Xu,

V_B'=0,
V_P'=z [G_PP-G_PB G_BB^(-1)G_BP]r_P,
V_N'=z [G_NP-G_NB G_BB^(-1)G_BP]r_P.              (7)

The last line matters: inactive projections can approach zero, causing a new event. They are not absorbed forever. Put S=G_PP-G_PB G_BB^(-1)G_BP. It is positive definite if P is nonempty, as the principal Schur complement of the SPD principal block on B union P; if P is empty, the output action below is zero.

The endpoint contribution to the vector output is z(V)_+. On a time interval entirely on this face its derivative is therefore

d[z(V)_+]/dt = z^2 E_P S E_P^T r.                  (8)

E_P embeds the P coordinates into R^k. This symmetric PSD *output-action representative* is convenient because the B and N output coordinates have zero derivative. It should not be identified with an averaged binary tangent Gram matrix. The chosen fractional tangent Gram z^2 D(theta)G D(theta) also has the same action on this particular residual, because its B normal components vanish and D_N=0, but generally it is a different matrix from the representative in (8). Attracting feasibility itself depends on r through theta^*; these are local identities, not a global residual-independent kernel theorem.

For two unit inputs with correlation rho, B={1}, P={2}, the hypotheses are z r_1<0 and 0< -rho r_2/r_1<1. Then theta_1^*=-rho r_2/r_1, V_2'=z(1-rho^2)r_2, and the output derivative is (0,z^2(1-rho^2)r_2). The familiar example rho=1/2,z=1,r=(-1,1) gives theta_1^*=1/2 and derivative (0,3/4).

## Limits of this result

This lemma proves one local frozen-residual mechanism, including capture and vanishing-step selection under strict face assumptions. It does not prove that every endpoint reaches such a face, that repelling intersections are harmless, or that the residual stays frozen on macroscopic time. In the network, different endpoints couple through r(t), and width, time-step, and long-boundary-time limits require new uniform estimates. The finite-grid theorem in BOUNDARY_GRID.md avoids this limit interchange. The explicit discrete chatter in agents/e03_discrete.md explains why replacing actual output increments by the average pre-step tangent Gram is incorrect.
