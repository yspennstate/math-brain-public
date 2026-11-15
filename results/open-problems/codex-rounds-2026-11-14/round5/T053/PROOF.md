# Collision law for the stationary Poisson billiard

Let $d\ge2$, $\lambda,r>0$, and let $P$ be the law of a homogeneous Poisson process of intensity $\lambda$ in $\mathbb R^d$. Put
\[
 O_\omega=\bigcup_{z\in\omega}\overline B(z,r),\qquad
 V_\omega=\mathbb R^d\setminus O_\omega.
\]
Let $V_\infty(\omega)$ be the union of all unbounded connected components of $V_\omega$, and assume
\[
 H=\{0\in V_\infty\},\qquad \theta=P(H)>0.
\]
Write $Q=P(\cdot\mid H)$, let $\sigma$ be probability surface measure on $S^{d-1}$, and set
\[
 \tau_x\omega=\{z-x:z\in\omega\},\quad
 \kappa_j=\frac{\pi^{j/2}}{\Gamma(1+j/2)},\quad
 c_d=\frac{\kappa_{d-1}}{d\kappa_d},\quad
 a=\lambda\kappa_{d-1}r^{d-1},\quad
 p_0=e^{-\lambda\kappa_dr^d}.
\]
The billiard has unit speed. At a regular collision with outward obstacle normal $n$, the incoming velocity $v$, with $v\cdot n<0$, becomes
\[
 R_nv=v-2(v\cdot n)n.                                      \tag{1}
\]

The round-4 result supplies a two-sided regular billiard with locally finite collisions for $Q\otimes\sigma$-almost every initial state, and invariance of this initial law under the environment seen from the particle. Its proof is rechecked in Section 8 below. No uniqueness of the unbounded component or dynamical ergodicity is assumed.

## 1. The boundary measure

Let $\Gamma_\infty(\omega)$ consist of boundary points $y$ that belong to exactly one obstacle sphere and whose local vacant side belongs to an unbounded vacant component. At such a point, the normal $n(y)$ points from that obstacle into vacancy. If its center is $z$, then $n(y)=(y-z)/r$.

Almost surely the obstacle family is locally finite, with distinct centers and no pair of tangent spheres. Only finitely many spheres meet a bounded set. The regular boundary is a countable union of smooth patches; the omitted multiple-sphere intersections have zero surface area. Near a regular point there is a positive margin from every other ball, and the local vacant side is connected. The unbounded-component indicator is constant on sufficiently small patches of this kind. It is measurable: unbounded connectivity from a small outward normal displacement is tested by countably many rational polygonal paths reaching outside arbitrarily large balls. Thus all the surface integrals below are measurable. Write $dA= d\mathcal H^{d-1}$.

For nonnegative bounded measurable $h$ of a centered configuration and a normal, define the measure $\beta$ by
\[
 \beta(h)=E_P\int_{\Gamma_\infty\cap[0,1)^d}
                 h(\tau_y\omega,n(y))\,dA(y),\qquad
 s_\infty=\beta(1).                                       \tag{2}
\]
For every bounded Borel set $B$,
\[
 E_P\int_{\Gamma_\infty\cap B}h(\tau_y\omega,n(y))\,dA(y)
       =|B|\beta(h).                                      \tag{3}
\]
Indeed the expected weighted surface measure on the left is translation invariant. It is locally finite: surface area in $B$ is bounded by $d\kappa_dr^{d-1}$ times the number of centers at distance at most $r$ from $B$. A locally finite translation invariant measure is a constant times Lebesgue measure. One can see this first by tiling boxes with rational side lengths, then approximating open sets by rational boxes and Borel sets by measure regularity. The constant is its mass on the unit cube, namely (2). For each set of marks this defines a finite measure; countable additivity follows from Tonelli. Formula (3) extends to all nonnegative $h$ by monotone convergence.

The main claims are
\[
 0<s_\infty\le \lambda d\kappa_dr^{d-1}p_0,\qquad
 \gamma=\frac{c_ds_\infty}{\theta}\in(0,\infty),             \tag{4}
\]
and the following marked collision identity. If $t_j$ are the collision times, $n_j$ their normals, and $V_{t_j-}$ their incoming velocities, then for every nonnegative measurable $g$ and $T>0$,
\[
 E_{Q\otimes\sigma}\sum_{0<t_j\le T}
  g(\tau_{X_{t_j}}\omega,n_j,V_{t_j-})
 =\frac T\theta\int\beta(d\eta,dn)\int_{S^{d-1}}
             (-v\cdot n)_+g(\eta,n,v)\,\sigma(dv).          \tag{5}
\]
In particular $E N(0,T]=\gamma T$. The collision Palm probability law, meaning the normalized expected distribution of a mark at collision times, is
\[
 \boxed{\quad
 \nu(d\eta,dn,dv)=\frac{\beta(d\eta,dn)}{s_\infty}
                  \frac{(-v\cdot n)_+}{c_d}\,\sigma(dv).
 \quad}                                                   \tag{6}
\]
Thus the conditional incoming velocity law given the boundary environment and normal is the cosine law. The configuration in (6) has a ball tangent to the origin. Its distribution differs from the volume-conditioned configuration law $Q$.

## 2. Specific exposed area and the Poisson formula

For clarity the Poisson insertion identity needed here follows directly by conditioning on the number of points in a bounded region $D$. Conditional on $m$ points, their locations are independent uniform points in $D$. For a nonnegative function $F(z,\omega)$, condition also on the configuration outside $D$, expand the sum over its $m$ interior points, and distinguish one of them. The coefficient changes according to
\[
 e^{-\lambda|D|}\frac{(\lambda|D|)^m}{m!}\frac m{|D|}
 =\lambda e^{-\lambda|D|}\frac{(\lambda|D|)^{m-1}}{(m-1)!}.
\]
Integrating the distinguished point and the remaining uniform points gives
\[
 E_P\sum_{z\in\omega\cap D} F(z,\omega)
       =\lambda\int_D E_P F(z,\omega\cup\{z\})\,dz.        \tag{7}
\]
Nonnegative approximation allows arbitrary measurable $F$, including dependence on the whole outside configuration. Increasing $D$ gives the same identity on all of $\mathbb R^d$.

Parametrize a sphere point as $y=z+rn$, with ordinary, unnormalized unit-sphere area measure $dS(n)$; its area element is $r^{d-1}dS(n)$. In the inserted configuration $\omega\cup\{-rn\}$, let $J_\infty(\omega,n)$ indicate that 0 belongs only to the inserted sphere and its outward vacant side is unbounded. Applying (7), changing variables $y=z+rn$, and using translation invariance yields the exact formula
\[
 \beta(h)=\lambda r^{d-1}\int_{S^{d-1}}
 E_P\left[J_\infty(\omega,n)
       h(\omega\cup\{-rn\},n)\right]dS(n).                 \tag{8}
\]
For example, before dividing by the volume of a spatial set $B$, the integrand contains $1_B(z+rn)$; the substitution $y=z+rn$ integrates this to $|B|$, which gives (8) by (3). No insertion is performed under the conditioned law $Q$.

Forgetting the unbounded-component condition leaves the event that no original center lies in $\overline B(0,r)$. It has probability $p_0$, independently of $n$; deterministic boundaries have zero Poisson mass. Hence
\[
 s_\infty\le \lambda r^{d-1}|S^{d-1}|p_0
             =\lambda d\kappa_dr^{d-1}p_0<\infty.           \tag{9}
\]
If all vacant components are retained, the corresponding specific exposed area is exactly the right side of (9). The inequality in (9) need not be an equality for unbounded vacancy.

## 3. Flux coordinates and complete boundary trajectories

For a smooth boundary patch, an incoming direction $v\cdot n(y)<0$, and a sufficiently short $u>0$, the point $y-uv$ lies in its vacant side. The map
\[
 (y,v,u)\longmapsto (y-uv,v)
\]
has the measure identity
\[
 dx\,\sigma(dv)=(-v\cdot n(y))\,dA(y)\,\sigma(dv)\,du.    \tag{10}
\]
To compute the spatial Jacobian, choose an orthonormal tangent frame on the patch. The tangential columns span its area element, and the last column is $-v$; the absolute determinant is $|v\cdot n|$. Dependence of $x$ on $v$ does not alter this factor because the full phase derivative has the identity in its velocity block.

Reflection (1) preserves spherical velocity measure and $|v\cdot n|$. Together with free translation, (10) proves measure preservation for each finite regular billiard branch, both for volume and for section flux. These are local changes of variables with inverses given by reversing the trajectory.

The volume-almost-everywhere complete-flow statement also holds for flux-almost every incoming boundary state. Here is the required transfer. Cover the transverse boundary states by countably many relatively compact charts with $-v\cdot n>\delta>0$, on each of which an incoming free tube of some positive length is available. Such charts cover because each regular transverse state has a positive local clearance. A bad boundary state, meaning its regular two-sided extension fails, makes every interior phase point in that incoming tube bad as well. On each chart (10) would then turn any positive flux measure of bad boundary states into positive bad phase volume. This contradicts the volume-null exceptional set. Countable covers prove that bad boundary states have zero flux measure. The pairs consisting of a boundary state and an elapsed time $s$ for which the reverse phase point is itself a collision have zero product flux-time measure: for each complete boundary trajectory there are only countably many such $s$, and Tonelli applies. Only integrations in $s$ will be used.

Restriction to $\Gamma_\infty$ ensures that a regular continuation stays in the same unbounded component at interior times. Across one contact a small detour on the connected vacant side joins its incoming and outgoing interior points; apply this at the finitely many contacts in each finite interval.

## 4. Exact collision counting and spatial averaging

Fix a configuration outside the null set, a bounded initial position set $A$, and $T>0$. For a complete incoming boundary state $(y,v)$, denote by $x_{-s}(y,v)$ the position obtained by following its incoming history backward for time $s$. The collision at $y$ is time 0 in this notation. For nonnegative bounded $g$, set
\[
 b_g=\int\beta(d\eta,dn)\int(-v\cdot n)_+
                                  g(\eta,n,v)\,\sigma(dv).
\]
The finite-branch change of variables (10) gives
\[
\begin{split}
 &\int_{A\cap V_\infty}dx\int\sigma(dw)
        \sum_{0<t_j\le T}g(\tau_{X_{t_j}}\omega,n_j,V_{t_j-})\\
 &=\int_0^T ds\int_{\Gamma_\infty}dA(y)\int\sigma(dv)
       (-v\cdot n(y))_+ g(\tau_y\omega,n(y),v)
                    1_{\{x_{-s}(y,v)\in A\}}.             \tag{11}
\end{split}
\]
On the first line the trajectory starts at $(x,w)$; its positions are absolute spatial positions. To justify the sum, restrict first to any finite regular collision history and the index of its final recorded collision. To verify its Jacobian explicitly, choose a fixed rational elapsed time $q$ strictly between the preceding collision (or initial time) and the recorded one. In a neighborhood of this history, the map to time $q$ preserves phase volume by the finite-branch calculation. From time $q$ to the recorded collision use the direct tube coordinates $(y,v,s-q)$ of (10). Since $d(s-q)=ds$, the composite has exactly the Jacobian (10). Countably many rational $q$ and charts cover the histories. Given $(y,v,s)$, time reversal uniquely reconstructs the initial state and the preceding regular history; different histories and indices have disjoint images after chart overlaps are partitioned away. All but a flux-null set have complete histories by Section 3. Summing the branch identities by Tonelli proves (11), including arbitrarily many collisions. This gives an equality, not merely the finite-history upper bound used to prove existence.

Take $A=C_R=[-R,R]^d$ and $R>T$. Unit speed gives
\[
 |x_{-s}(y,v)-y|\le s\le T.
\]
Thus all $y\in C_{R-T}$ contribute to the right side of (11), whereas only $y\in C_{R+T}$ can contribute. Take $P$-expectations and apply (3). Translation covariance of the trajectories and stationarity of $P$ turn the first line into
\[
 |C_R|\theta\ E_{Q\otimes\sigma}
             \sum_{0<t_j\le T}g(\tau_{X_{t_j}}\omega,n_j,V_{t_j-}).
\]
Consequently
\[
 T|C_{R-T}|b_g\ \le\ |C_R|\theta\ E_Q\sum_{0<t_j\le T}g_j
                      \ \le\ T|C_{R+T}|b_g.                \tag{12}
\]
The omitted velocity law in $E_Q$ here is still $\sigma$. By (9), $b_g<\infty$ for bounded $g$. Divide by $|C_R|$, let $R\to\infty$, and use $|C_{R\pm T}|/|C_R|=(1\pm T/R)^d\to1$. This proves (5) for bounded nonnegative $g$. Truncation and monotone convergence prove it for every nonnegative measurable $g$.

For every unit $n$, projection of its incoming hemisphere onto the unit $(d-1)$-ball gives
\[
 \int(-v\cdot n)_+\sigma(dv)=\frac{\kappa_{d-1}}{d\kappa_d}
                            =c_d.                         \tag{13}
\]
This is a single hemisphere; integrating $|v\cdot n|$ over the whole sphere would incorrectly double the collision rate. Equations (5), (9) and (13) prove finite mean collision intensity $\gamma=c_ds_\infty/\theta$ and
\[
 \gamma\le \frac{a p_0}{\theta}.                           \tag{14}
\]

## 5. Positivity and Palm normalization

A regular trajectory with no collision in $(0,T]$ traces the vacant straight segment $[0,Tv]$. For a deterministic $v$, the set of forbidden Poisson centers is its closed radius-$r$ sausage. Its volume is
\[
 \kappa_dr^d+\kappa_{d-1}r^{d-1}T:
\]
the cylindrical part contributes the second term, and the two hemispherical end caps together contribute the first. Therefore the probability of vacancy of this segment under $P$ is $p_0e^{-aT}$. Discarding the restriction $H$ in a numerator gives
\[
 P_{Q\otimes\sigma}\{N(0,T]=0\}
       \le \frac{p_0}{\theta}e^{-aT}.                      \tag{15}
\]
Since $N\ge1_{\{N\ge1\}}$, equation (5) implies
\[
 \gamma\ge \frac{1-(p_0/\theta)e^{-aT}}{T}.                \tag{16}
\]
Here $\theta\le p_0$, because unbounded vacancy implies vacancy at the origin. Taking $T=[1+\log(p_0/\theta)]/a$ proves the explicit positive lower bound
\[
 \boxed{\quad
 \frac{(1-e^{-1})a}{1+\log(p_0/\theta)}
       \le\gamma\le\frac{a p_0}{\theta}.
 \quad}                                                   \tag{17}
\]
In particular $s_\infty>0$. Integration of (6), using (13), now gives total mass one. Formula (5) becomes $E\sum_{0<t_j\le T}g_j=T\gamma\nu(g)$. This identifies the collision Palm law without a sample-frequency or ergodic assertion. Reflection pushes the incoming conditional law in (6) to $(v\cdot n)_+\sigma(dv)/c_d$ for outgoing velocity. The environment and normal marginal is $\beta/s_\infty$.

Rotational covariance of (2) makes the normal marginal of $\beta/s_\infty$ uniform. Integrating (6) over normals therefore gives uniform incoming velocity marginal, since $\int(-v\cdot n)_+\sigma(dn)=c_d$. This marginal uniformity does not make velocity independent of the boundary environment.

## 6. Mean time between collisions

There are infinitely many collisions in both time directions almost surely under the stationary volume law. Indeed (15) tends to zero as $T\to\infty$, so there is a future collision almost surely. By stationarity the same holds after each integer time. A trajectory with a last forward collision would have no collision after some integer, a countable union of null events. The backward statement follows from reversal of the initial velocity, whose conditional law remains uniform, and the same straight-segment void bound. Local finiteness then gives a sequence of collision times unbounded in both directions.

For an incoming boundary mark $M=(\eta,n,v)$, let $\ell(M)$ be the time from that collision, after reflection, to the next collision. Define it arbitrarily on exceptional boundary states. Formula (5) transfers null properties of actual collision marks to $\nu$; in particular $0<\ell<\infty$ holds $\nu$-almost surely. Measurability follows by the successive-flight construction.

The collision process, including these marks, is stationary in time because the volume initial law is invariant. Thus (5) holds with $(0,T]$ replaced by any bounded time interval, with its length on the right. First for indicator rectangles in time and marks, then by nonnegative simple approximation, it yields
\[
 E\sum_j f(t_j,M_j)=\gamma\int_{\mathbb R}\nu(f(s,\cdot))\,ds
                                                               \tag{18}
\]
for every nonnegative measurable $f$. No independence of the marks or of successive times is asserted.

At time 0 there is almost surely exactly one last collision before 0 and one next collision after 0. A collision exactly at 0 has zero probability: (18) applied to the time singleton gives zero expected count. Hence
\[
 1=\sum_j 1_{\{t_j\le0<t_j+\ell(M_j)\}}.
\]
Take expectations, use (18), and then Tonelli:
\[
 1=\gamma\int_{-\infty}^0\nu(\ell>-s)\,ds
   =\gamma\int_0^\infty\nu(\ell>u)\,du
   =\gamma\nu(\ell).
\]
Thus the Palm mean flight time, also the mean flight length at unit speed, is
\[
 \boxed{\qquad \nu(\ell)=\frac1\gamma
                    =\frac{\theta}{c_ds_\infty}.\qquad}   \tag{19}
\]
The forward waiting time under the volume law need not have this mean; it is a different sampling law.

## 7. Checks and limits

If all vacant components are used, their volume fraction is $p_0$, the specific exposed area is exactly $\lambda d\kappa_dr^{d-1}p_0$, and (4) reduces to $\gamma=a$. Independently, conditional on vacancy of the origin, the first-flight survival probability is exactly $e^{-aT}$, so its derivative at zero has rate $a$. This derivative is the stationary collision intensity: for a simple stationary collision process of finite intensity $\rho$, the excess $E N(0,h]-P(N(0,h]\ge1)$ is at most $\rho h$ times the Palm probability that the preceding gap is at most $h$. To see this, count all hits in $(0,h]$ after its first hit; each has a preceding gap at most $h$, and the marked time-count identity bounds their expected number. That Palm probability tends to zero, since every regular gap is positive. Dividing by $h$ and letting $h\downarrow0$ proves the assertion. The two calculations check both the factor $1/\theta$ and the single-hemisphere normalization. They do not replace the component restriction in the main theorem.

The cosine law has a second description: the tangential projection of the incoming velocity onto the unit $(d-1)$-ball is uniform. If $\mu=-v\cdot n$, then $\mu^2=1-|b|^2$ in those projection coordinates, so
\[
 \nu(\mu^2\mid\eta,n)=1-\frac{d-1}{d+1}=\frac2{d+1}.
\]
Reflection then gives a mean squared velocity jump of $8/(d+1)$. These identities only concern one collision; they imply no decorrelation between successive collisions.

Equations (5)--(19) give annealed stationary intensity and Palm expectations. They do not establish a deterministic almost-sure collision frequency, an independent-flight model, mixing, an integrable velocity correlation, nonzero diffusivity, a CLT, a quenched limit, or planar recurrence. No literature priority is claimed for these flux and Palm arguments.

## 8. Independent recheck of the stationarity input

The complete-flow input can be obtained without assuming global billiard existence. For a locally finite Poisson configuration, the singular boundary is covered locally by finitely many pairwise sphere intersections of dimension at most $d-2$. Initial phase points whose next straight flight hits this set are images of $(y,v,s)$, of dimension at most $(d-2)+(d-1)+1=2d-2$, below phase dimension $2d-1$. Tangencies have the same deficit by imposing $v\cdot n=0$. Countable charts make these sets phase-null. Pulling these null sets back through finite regular volume-preserving branches excludes every singular encounter preceded by finitely many regular collisions.

For initial positions in a bounded set $A$, all collisions before $T$ lie in $A+\overline B(0,T)$. Count only finite regular histories and use their injective map to collision location, incoming velocity and time, with Jacobian (10). Their images are disjoint because reversal uniquely recovers the history. Summing gives
\[
 \int_{A\cap V_\omega}dx\int\sigma(dv)\,N_T(x,v)
 \le T c_d\mathcal H^{d-1}
       (\Gamma\cap(A+\overline B(0,T)))<\infty.
\]
A finite accumulation contributes infinitely many finite histories, so it occurs on a phase-null set. Countable spatial boxes and integer $T$, also with reversed velocity, give the two-sided complete flow almost everywhere. It preserves volume by its finite regular branches and preserves each open vacant component by the local detour described in Section 3. Translation covariance and Tonelli then transfer phase-null exceptions to the fixed-origin law $Q\otimes\sigma$.

For bounded measurable $f$, compare its integral over $(C_R\cap V_\infty)\times S^{d-1}$ with the integral after flowing for $t$. Volume preservation expresses the latter over the image cylinder. Forward and inverse unit-speed bounds sandwich that image between cylinders over $C_{R-|t|}$ and $C_{R+|t|}$. Its symmetric difference with the original cylinder has volume at most
\[
 (2(R+|t|))^d-(2(R-|t|))^d.
\]
Taking Poisson expectation and translating the starting point turn the two spatial integrals into $|C_R|\theta$ times the two fixed-origin expectations. Dividing the error by $|C_R|\theta$ makes it tend to zero. Thus the centered environment and velocity at any fixed $t$ again have law $Q\otimes\sigma$. This re-derives the precise stationarity input used above, including for observables of the entire configuration.
