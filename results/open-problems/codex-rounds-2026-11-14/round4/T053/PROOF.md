# The stationary law of the environment seen from a Poisson billiard

Let d >= 2, r > 0 and lambda > 0. Let P be the law of a homogeneous Poisson process omega of intensity lambda in R^d. Define

\[
O_\omega=\bigcup_{z\in\omega}\overline B(z,r),\qquad
V_\omega=\mathbb R^d\setminus O_\omega.
\]

Let V_infinity(omega) be the union of the unbounded connected components of V_omega, and set

\[
H=\{\omega:0\in V_\infty(\omega)\},\qquad
\theta=P(H)>0,\qquad Q=P(\,\cdot\mid H).
\]

No uniqueness of the unbounded component is assumed. The event H and the set {(omega,x):x in V_infinity(omega)} are measurable: an open-set component is unbounded exactly when, for every integer n, it contains a point outside the ball of radius n reachable from x by a finite polygonal path in the vacant set. The internal vertices and the final point can be chosen rational, by openness and compactness of each finite path. This gives a countable test, and vacancy of each compact segment is measurable from the locally finite obstacle configuration. Let sigma be probability surface measure on S^(d-1). Write tau_x omega = {z-x:z in omega}. Thus V_(tau_x omega) = V_omega-x. A regular collision occurs at a boundary point belonging to exactly one obstacle sphere, with nonzero normal velocity. If n points from that ball into the vacant set, specular reflection is

\[
v^+=v^- - 2(v^-\cdot n)n.                                      \tag{1}
\]

The speed is one. At a collision time the velocity is taken to be the outgoing velocity.

## The result

For Q-almost every omega and sigma-almost every initial velocity v, the billiard starting at (0,v) has a unique two-sided trajectory with finitely many collisions on every bounded time interval. All its collisions are regular. At every interior time it stays in the unbounded vacant component of its starting point.

Let X_t and V_t be its position and velocity, and define

\[
\eta_t=\tau_{X_t}\omega.
\]

For every bounded measurable function f of an environment and a unit velocity, and every real t,

\[
\boxed{\quad
\mathbb E_{Q\otimes\sigma} f(\eta_t,V_t)
       =\mathbb E_{Q\otimes\sigma} f(\omega,v).
\quad}                                                        \tag{2}
\]

In particular, the shifted environment and current velocity have the product law Q tensor sigma at each deterministic time. This is an annealed invariance statement. It assumes neither ergodicity nor mixing. The arguments below also work with any measurable translation-covariant union of vacant components in place of V_infinity, provided its volume fraction is positive.

## 1. Boundary geometry and the local flow

Almost surely omega is locally finite and has distinct centers, with no pair of centers at distance 2r. Indeed, in any bounded box the centers, conditional on their finite number, have an absolutely continuous joint distribution. Equality of two centers or the equation |z-z'|=2r is a Lebesgue-null constraint. Take the countable union over pairs and integer boxes.

Fix such a configuration. Only finitely many obstacle spheres meet a bounded set. The part Gamma of the boundary belonging to exactly one sphere is a countable union of smooth open sphere patches. The remaining boundary Sigma is contained in the union of pairwise sphere intersections. Each nonempty such intersection is a smooth (d-2)-sphere; in d=2 it consists of two points. Consequently Sigma has zero (d-1)-dimensional surface measure and is locally covered by finitely many smooth sets of dimension at most d-2. No assertion about transverse intersections of three or more spheres is needed. For every bounded set K,

\[
S(K):=\mathcal H^{d-1}(\Gamma\cap K)<\infty.                  \tag{3}
\]

For example, it is bounded by the number of centers within distance r of K times d kappa_d r^(d-1), where kappa_j is the volume of the unit ball in R^j.

Starting at x in V_omega with velocity v, follow the line until its first boundary contact. If that contact is regular, apply (1) and repeat. Stop at a singular contact or a finite accumulation of collisions. This construction uses a finite list of nearby centers on each bounded time interval before stopping, so it gives measurable collision times, locations and velocities. A measurable enumeration of the locally finite point set can be obtained by integer boxes and lexicographic order within each box. All maps below are therefore measurable.

We use the phase measure

\[
m(dx,dv)=dx\,\sigma(dv)
\]

on V_omega times S^(d-1). On each branch with a prescribed finite sequence of regular sphere hits, the local billiard flow preserves this measure. Here is a direct verification.

Take a small smooth boundary patch with normal n(y). Coordinates for a straight tube approaching it are

\[
(y,w,s)\longmapsto (y-sw,w),\qquad w\cdot n(y)<0.
\]

The Jacobian for the spatial coordinates is |w dot n(y)|: the d-1 tangential columns span the boundary surface element, and the s column is -w. Hence

\[
dx\,\sigma(dw)=|w\cdot n(y)|\,dA(y)\,\sigma(dw)\,ds.        \tag{4}
\]

Free translation preserves dx sigma(dv). Between two transverse sections of the same straight tube, (4) shows that the boundary measure |w dot n| dA sigma(dw) is preserved. Reflection fixes y and acts on w by an orthogonal map R_y. In local coordinates its derivative in (y,w) has block triangular form, with identity on y and an isometry on the velocity tangent space. It preserves dA sigma(dw), and |R_y w dot n|=|w dot n|. It thus preserves the boundary measure in (4). For a fixed-time map with exactly one collision, its incoming coordinates are (y,w,s), where s is the time to collision. Its outgoing coordinates are (y,R_y w,t-s). The reflection preserves the boundary flux factor and the last time coordinate has derivative -1 in s, so the map preserves m by (4). For finitely many collisions, choose intermediate times between the successive collisions and work in a neighborhood where the same regular sequence persists; composing these one-collision maps proves preservation of m. A countable rational choice of intermediate times and local charts covers all finite regular branches. The branches admit countable chart covers. Time reversal supplies their inverses, so these are genuine local changes of variables, without any assertion yet about global existence.

## 2. Finite singular encounters have zero phase measure

First consider a singular encounter reached by one straight flight in a bounded region and bounded time. For an edge hit, write the initial point as x=y-sw with y in Sigma, w in S^(d-1), and 0<=s<=T. On compact charts this is a smooth or Lipschitz image of a space of dimension at most

\[
(d-2)+(d-1)+1=2d-2,
\]

whereas phase space has dimension 2d-1. It therefore has zero m-measure. For a tangency to a smooth patch, impose w dot n(y)=0. The dimensions are (d-1)+(d-2)+1=2d-2, giving the same conclusion. Countable compact chart covers and integer bounds on position and time cover all direct singular flights.

Now suppose a singular contact is preceded by finitely many regular collisions. There is a rational time q strictly between the last regular collision and that singular contact. Up to q the trajectory lies on a finite regular branch. At time q its phase point belongs to the direct-singular-flight null set just described. The inverse branch preserves m by (4), so its preimage is null. Countably many rational q, finite collision words, and charts cover all these possibilities. Thus phase points reaching a singular contact after finitely many regular collisions form an m-null set. Initial boundary states are also m-null.

## 3. A collision-flux bound excludes accumulation almost everywhere

Let A be a bounded measurable set of initial positions, and T>0. Every collision before time T of a trajectory started in A lies in

\[
K=A+\overline B(0,T).
\]

Let N_T(x,v) count its regular collisions by time T before a possible stopping time, with value infinity if they accumulate by T. Define

\[
c_d=\int_{w\cdot n<0}|w\cdot n|\,\sigma(dw)
    =\frac{\kappa_{d-1}}{d\kappa_d}.                          \tag{5}
\]

This does not depend on the unit vector n. To see the second equality, project the incoming hemisphere onto the unit (d-1)-ball. The Jacobian of the projection is |w dot n|, so the unnormalized flux is kappa_(d-1). Divide by the sphere area d kappa_d.

For every individual collision of a finite regular history, record its time s in (0,T], location y in Gamma intersect K and incoming velocity w. On each branch the change of variables from the initial phase point to (y,w,s) has measure (4), by the finite-branch calculation in Section 1. The images of distinct histories and collision indices are disjoint, up to chart overlaps which can be partitioned away: given (y,w,s), reverse the incoming flight and the preceding regular reflections for time s. If a finite regular history exists it is unique. In particular two different collision indices cannot give different regular initial histories with the same recorded triple.

Summing (4) over these disjoint images and then over all finite collision indices gives, by monotone convergence,

\[
\begin{split}
\int_{(A\cap V_\omega)\times S^{d-1}}N_T(x,v)\,dx\,\sigma(dv)
&\le\int_0^T\int_{\Gamma\cap K}\int_{w\cdot n(y)<0}
              |w\cdot n(y)|\,\sigma(dw)\,dA(y)\,ds\\
&=T c_d S(K)<\infty.                                        \tag{6}
\end{split}
\]

This argument only counts finite regular histories. It does not assume a flow through a potential accumulation. Each trajectory accumulating by T contributes arbitrarily many finite histories and therefore N_T=infinity. Equation (6) proves that such initial phase points have zero m-measure. Taking integer boxes A and integer T excludes every finite-time accumulation almost everywhere. Apply the same argument after reversing v to obtain the backward assertion. A finite-speed path cannot escape to infinity in finite time. If it has only finitely many collisions before a finite terminal time, the next obstruction is a singular contact, already excluded in Section 2; otherwise the regular construction continues. Thus the billiard exists uniquely for all positive and negative times for m-almost every initial phase point.

For each fixed t the image of this full-measure set is full measure: backward trajectories give inverses and the finite regular branches preserve m. The set mapped to a collision exactly at t has measure zero, as also follows by setting s=t in (4). Consequently the complete billiard maps Phi_t preserve m, with the usual interpretation modulo null sets at boundary times.

Every finite trajectory portion has finitely many regular contacts. Near each contact the boundary is a single sphere patch with a connected vacant side. Replace a sufficiently short portion containing the contact by a small detour within that side. These finitely many detours give a path in the open vacant set joining the original interior endpoints. Those endpoints are therefore in the same connected component. It follows that Phi_t preserves the restriction

\[
m_\infty(dx,dv)=1_{\{x\in V_\infty(\omega)\}}dx\,\sigma(dv). \tag{7}
\]

## 4. From almost every position to the fixed origin

Let b(omega,x,v) be the indicator that the two-sided regular construction at (x,v) fails, restricting x to V_omega. Sections 1--3 show that its integral over any bounded spatial box and the velocity sphere is zero for every configuration in the probability-one set above. The construction is translation covariant:

\[
b(\omega,x,v)=b(\tau_x\omega,0,v).
\]

For a box C of positive finite volume, Tonelli and stationarity of P give

\[
\begin{split}
0&=\mathbb E_P\int_C\int
  1_{\{x\in V_\infty(\omega)\}}b(\omega,x,v)\,\sigma(dv)\,dx\\
 &=|C|\,\mathbb E_P\left[1_H(\omega)
                   \int b(\omega,0,v)\,\sigma(dv)\right].    \tag{8}
\end{split}
\]

Divide by |C| theta. A final application of Fubini yields the asserted regular two-sided trajectory for Q-almost every environment and sigma-almost every direction. This step is necessary: a deterministic almost-everywhere assertion in x alone would not justify starting at the fixed origin.

## 5. Spatial averaging proves invariance

Fix t in R, put h=|t| and let C_R=[-R,R]^d with R>h. For a fixed configuration write

\[
F_\omega(x,v)=f(\tau_x\omega,v),\qquad
I_R(\omega)=\int_{C_R\cap V_\infty}\int
      F_\omega(\Phi_t(x,v))\,\sigma(dv)\,dx,
\]

and

\[
J_R(\omega)=\int_{C_R\cap V_\infty}\int
      F_\omega(x,v)\,\sigma(dv)\,dx.
\]

Here F_omega(Phi_t(x,v)) means F_omega evaluated at the final position and velocity. By the measure preservation in (7), I_R is the integral of F_omega over the image of the initial cylinder (C_R intersect V_infinity) times S^(d-1). Finite speed and the inverse flow give, modulo null sets,

\[
(C_{R-h}\cap V_\infty)\times S^{d-1}
\ \subset\ \Phi_t((C_R\cap V_\infty)\times S^{d-1})
\ \subset\ (C_{R+h}\cap V_\infty)\times S^{d-1}.             \tag{9}
\]

The middle image and the original cylinder can therefore differ only in the outer-minus-inner shell. For bounded, possibly signed f,

\[
|I_R-J_R|\le\|f\|_\infty
 \big[(2(R+h))^d-(2(R-h))^d\big].                            \tag{10}
\]

This estimate uses no locality of f: it holds for every bounded measurable observable of the whole environment and velocity.

Translation covariance identifies the trajectory starting at x in omega with the trajectory starting at 0 in tau_x omega, after subtracting x from its positions. Since tau_y(tau_x omega)=tau_(x+y) omega, the shifted environment at the final point agrees in the two descriptions. Thus stationarity of P and Fubini give exactly

\[
\mathbb E_P I_R=|C_R|\theta\,
    \mathbb E_{Q\otimes\sigma} f(\eta_t,V_t),\qquad
\mathbb E_P J_R=|C_R|\theta\,
    \mathbb E_{Q\otimes\sigma} f(\omega,v).                   \tag{11}
\]

Divide the expectation of (10) by |C_R| theta. Its right-hand side is

\[
\frac{\|f\|_\infty}{\theta}
 \left[(1+h/R)^d-(1-h/R)^d\right]\longrightarrow0.
\]

The two expectations on the left of (11) do not depend on R. They must be equal, which proves (2). This is spatial averaging in expectation, not an application of spatial or dynamical ergodicity.

On regular trajectories the environment process has the group property

\[
T_t(\omega,v)=(\eta_t,V_t),\qquad T_sT_t=T_{s+t},
\]

modulo the fixed-time null sets. Therefore (2) implies stationarity of every finite-dimensional distribution, by applying the group property and (2) to bounded measurable functions of finitely many states.

## 6. Direct consequences and remaining obstruction

Under Q tensor sigma the velocity has mean zero and covariance I_d/d at every deterministic time. In particular

\[
\mathbb E X_t=0,\qquad
\mathbb E[V_tV_t^{\mathsf T}]=I_d/d.                         \tag{12}
\]

The mean of X_t follows from X_t=integral_0^t V_s ds and boundedness of V_s. The law P, the event H and the reflection rule are invariant under every orthogonal map. Hence, for

\[
C(s)=\mathbb E[V_0\cdot V_s],\qquad s\ge0,
\]

the matrix E[V_0 V_s^T] equals C(s) I_d/d. Indeed, coordinate sign changes force the off-diagonal entries to vanish and coordinate permutations make the diagonal entries equal; their sum is C(s). Stationarity and Fubini now give the exact finite-time identities

\[
\boxed{\quad
\mathbb E|X_t|^2=2\int_0^t(t-s)C(s)\,ds,\qquad
\mathbb E[X_tX_t^{\mathsf T}]
  =\frac{2I_d}{d}\int_0^t(t-s)C(s)\,ds\quad}                 \tag{13}
\]

for t>=0. To check the first one, expand the square of integral_0^t V_u du and split [0,t]^2 along its diagonal. For u<v, stationarity gives E[V_u dot V_v]=C(v-u); the dot product makes the two triangles equal. The diagonal has two-dimensional Lebesgue measure zero. Integration in the difference s=v-u gives (13). The covariance matrix is scalar by the same orthogonal invariance, and its trace gives the second formula.

If integral_0^infinity |C(s)| ds is finite, dominated convergence in (13) yields

\[
\lim_{t\to\infty}\frac1t\mathbb E[X_tX_t^{\mathsf T}]
   =\frac{2I_d}{d}\int_0^\infty C(s)\,ds.                    \tag{14}
\]

Under that additional hypothesis the integral is nonnegative, since the left side is a limit of covariance matrices. No integrability, strictly positive integral, central limit theorem or planar recurrence has been proved here. Even an integrable C would not by itself establish a central limit theorem.

## Relation to the earlier result and literature

The round-3 geometric bound controls the largest possible straight flight in a spatial ball, uniformly over trajectories; it does not imply stationarity or correlation decay. Equations (2) and (13) supply the invariant probability law and the finite-time correlation identity at fixed density. The finite collision estimate (6) removes the earlier almost-everywhere well-posedness caveat for the initial law used here; it does not define the billiard at every exceptional phase point.

These are elementary Liouville and spatial-averaging arguments, and no literature priority is claimed. The bounded update found no fixed-density diffusion theorem. The opened papers Karsten Matthies and Raphael Winter, *Improved geometric and recollision estimates for the invariance principle of the random Lorentz gas*, [arXiv:2506.18539v2](https://arxiv.org/abs/2506.18539v2), and Bálint Tóth, *Semi-Quenched Invariance Principle for the Random Lorentz Gas -- Beyond the Boltzmann-Grad Limit*, [arXiv:2501.00519v2](https://arxiv.org/abs/2501.00519v2), concern joint limiting regimes. Yingxin Mu and Artem Sapozhnikov, *On the maximum visibility in a ball through the vacant set of Poissonian obstacles*, [arXiv:2609.11690v1](https://arxiv.org/abs/2609.11690v1), concerns geometric visibility. None of these is used as a premise of the proof above.
