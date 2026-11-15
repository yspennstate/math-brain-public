# The collision map and suspension of the stationary Poisson billiard

Let $d\ge2$, let $\lambda,r>0$ be fixed, and let $P$ be the law of a homogeneous Poisson process of centers of intensity $\lambda$ in $\mathbb R^d$. Remove the closed radius-$r$ balls. Let $V_\infty$ be the union of the unbounded open vacant components, and assume
\[
\theta=P(0\in V_\infty)>0.
\]
Put $Q=P(\,\cdot\mid0\in V_\infty)$, let $\sigma$ be uniform probability measure on $S^{d-1}$, and write
\[
\mu=Q\otimes\sigma,\qquad \tau_x\omega=\{z-x:z\in\omega\}.
\]
All observations below are annealed. No uniqueness of the unbounded component is needed.

The round-4 and round-5 results, audited in Section 1, supply the following inputs. The centered environment and velocity $Z_t=(\tau_{X_t}\omega,V_t)$ form a two-sided measurable deterministic flow preserving $\mu$, modulo null sets. Collisions are regular and locally finite almost surely. There are infinitely many collisions in both time directions. Their times and incoming marks are
\[
t_j,\qquad M_j=(\tau_{X_{t_j}}\omega,n_j,V_{t_j-}),
\]
where $n_j$ is the outward obstacle normal. There is a finite positive intensity $\gamma$ and a probability law $\nu$ on incoming marks such that
\[
 E_\mu\sum_j f(t_j,M_j)
   =\gamma\int_{\mathbb R}\int f(u,M)\,\nu(dM)\,du             \tag{1}
\]
for every nonnegative measurable $f$. The mark retains the entire centered configuration. If $\ell(M)$ is the next flight time, then
\[
 0<\ell<\infty\quad\nu\text{-almost surely},\qquad
 \gamma\int\ell\,d\nu=1.                                   \tag{2}
\]

We prove that the next-collision map preserves $\nu$, identify the variable-roof suspension with the stationary time law, and express the velocity correlation in those coordinates. A convergent Laplace series is a consequence. These statements are new relative to the supplied folders; no literature priority is claimed.

## 1. Recheck of the earlier inputs

Here are the normalization and exceptional-set checks needed for their use. Put
\[
 \kappa_j=\frac{\pi^{j/2}}{\Gamma(1+j/2)},\quad
 c_d=\frac{\kappa_{d-1}}{d\kappa_d},\quad
 a=\lambda\kappa_{d-1}r^{d-1},\quad
 p_0=e^{-\lambda\kappa_dr^d}.
\]
Let $\beta$ be the mean exposed boundary area per unit spatial volume, marked by the centered configuration and normal and restricted to boundary patches whose vacant side is unbounded. Write $s_\infty=\beta(1)$. The round-5 formulas are
\[
 \gamma=\frac{c_ds_\infty}{\theta},\qquad
 \nu(d\eta,dn,dv)=\frac{\beta(d\eta,dn)}{s_\infty}
                 \frac{(-v\cdot n)_+}{c_d}\sigma(dv).        \tag{3}
\]

To check (3), a transverse incoming boundary tube has coordinates
$(y,v,u)\mapsto(y-uv,v)$ and spatial Jacobian $(-v\cdot n(y))$. Free motion and reflection preserve phase volume on finite regular branches. Recording a collision and its elapsed time is injective: reverse the recorded incoming state for that time. A rational intermediate time in the final free flight reduces its Jacobian to the tube Jacobian. Nonnegative summation over histories is therefore valid even when the collision count is unbounded.

The earlier complete-flow assertion transfers from volume measure to surface flux by covering transverse incoming states by countably many charts with positive-length incoming tubes. A bad boundary state makes its whole incoming tube bad, contradicting volume-nullity. For initial positions in $C_R=[-R,R]^d$ and a time window of length $T<R$, unit speed squeezes the count integral between the corresponding flux integrals over $C_{R-T}$ and $C_{R+T}$. Translation expectation divides its volume side by $\theta$. Sending $R$ to infinity gives (3) and the marked count formula on a finite time interval. Time stationarity and nonnegative simple approximation give (1).

Projection of the incoming hemisphere onto the unit $(d-1)$-ball gives
$\int(-v\cdot n)_+\sigma(dv)=c_d$; using both hemispheres would double the intensity. Inserting one center under $P$, and forgetting the unbounded-component restriction, gives
$s_\infty\le\lambda d\kappa_dr^{d-1}p_0$. Insertion is not performed under $Q$. The first-flight sausage volume is $\kappa_dr^d+\kappa_{d-1}r^{d-1}T$, so
\[
 P_\mu(N(0,T]=0)\le(p_0/\theta)e^{-aT}.
\]
Together with $E_\mu N(0,T]=\gamma T$, this gives
\[
 \frac{(1-e^{-1})a}{1+\log(p_0/\theta)}
       \le\gamma\le\frac{ap_0}{\theta}.                    \tag{4}
\]
For the lower bound take $T=(1+\log(p_0/\theta))/a$.

The first-flight bound, applied after each integer time, rules out a last future collision. Velocity reversal rules out a first past collision. Local finiteness gives a unique interval between collisions containing time zero, almost surely. Applying (1) to the indicator that a marked interval contains zero gives $1=\gamma\int\ell\,d\nu$, independently checking (2).

The local-existence argument has no accumulation assumption hidden in it: summing only finite regular collision histories bounds their integrated count in a bounded spacetime region by $T c_d$ times the local exposed area. Finite accumulation would give infinite count on a positive-volume set and contradict this bound. Direct corner and tangency hits have phase dimension at most $2d-2$, below $2d-1$, and their preimages under finite regular branches remain null. Translation and Tonelli transfer spatial almost-everywhere existence to the fixed origin. For stationarity, both a spatial phase cylinder and its flow image lie between the cylinders on $C_{R-|t|}$ and $C_{R+|t|}$. Their normalized symmetric difference tends to zero. This works for observables of the entire configuration. These checks support the earlier inputs without imposing ergodicity.

## 2. The full next-collision map

For an incoming mark $M=(\eta,n,v)$ define
\[
 R_nv=v-2(v\cdot n)n,\qquad w(M)=R_nv.
\]
Thus $w(M)$ is the outgoing velocity of the flight beginning at $M$. Follow the straight flight $u\mapsto u w(M)$ to its next collision, at time $\ell(M)$, with outward normal $n'$. Define
\[
 S M=(\tau_{\ell(M)w(M)}\eta,n',w(M)).                      \tag{5}
\]
The last coordinate of $SM$ is incoming at the next collision. It is not its reflected velocity. Successive flight times and velocities can depend on all of $\eta$.

There is a measurable set $\mathcal B_*$ of full $\nu$-measure on which this construction has a regular, locally finite, doubly infinite collision sequence. Indeed every actual collision mark of a good stationary volume trajectory has this property. The left side of (1), restricted to bad marks in $(0,1]$, vanishes. Its right side is $\gamma\nu(\mathcal B_*^c)$, so this probability is zero. Goodness is invariant under moving to either neighboring collision.

On this set $S$ has a measurable inverse. Follow the incoming history backwards to the previous collision. If its normal is $n_-$ and its forward outgoing velocity is $v$, its forward incoming velocity is $R_{n_-}v$. Translating the configuration to that previous contact gives the unique inverse mark. Measurability follows from the finite local search for the next contact and iteration, as for the original flow. All maps may be defined arbitrarily off $\mathcal B_*$.

For bounded measurable $g$, let the collision times in $(0,T]$ be indexed consecutively by $j=k,\ldots,m$. If there are none, both sums below vanish. Otherwise
\[
 \sum_{0<t_j\le T}\bigl[g(SM_j)-g(M_j)\bigr]
       =g(M_{m+1})-g(M_k).
\]
Consequently the absolute value is at most $2\|g\|_\infty$. Formula (1), applied separately to the positive and negative parts of these bounded marks, gives
\[
 T\gamma\left|\nu(g\circ S)-\nu(g)\right|
       \le2\|g\|_\infty.
\]
The expected number of terms is finite, so both expectations are well defined. Letting $T\to\infty$ proves
\[
                         S_*\nu=\nu.                      \tag{6}
\]
The proof does not use a time-frequency limit or a sample ergodic theorem. In particular the bi-infinite sequence of marks and their flight times is stationary in the collision index under $\nu$.

## 3. Recovery of stationary time sampling

For $0<s<\ell(M)$ put
\[
 \Psi(M,s)=(\tau_{s w(M)}\eta,w(M)).                        \tag{7}
\]
This is the interior state at age $s$ in the flight beginning at $M$. Endpoint values have zero $ds$-measure and can be assigned by a boundary convention.

Let $F$ be a nonnegative measurable function of an interior state. On a stationary trajectory the unique flight containing zero gives the pathwise identity
\[
 F(Z_0)=\sum_j1_{\{t_j\le0<t_j+\ell(M_j)\}}
                       F(\Psi(M_j,-t_j)).
\]
There is almost surely no collision at zero: (1) applied to the singleton time set gives zero expected count. Use (1), then change variables $s=-u$ and use Tonelli. The result is
\[
 \boxed{\quad
 \mu(F)=\gamma\int\nu(dM)\int_0^{\ell(M)}F(\Psi(M,s))\,ds.
 \quad}                                                    \tag{8}
\]
For signed $F\in L^1(\mu)$, apply the identity to its two parts. In particular the right side is absolutely integrable. Taking $F=1$ checks its total mass by (2).

The probability measure on suspension coordinates is therefore
\[
 \widehat\mu(dM,ds)=\gamma\nu(dM)1_{\{0\le s<\ell(M)\}}ds.  \tag{9}
\]
Under this law the mark of the current flight has marginal $\gamma\ell(M)\nu(dM)$, and conditional on that mark the age is uniform on $[0,\ell(M))$. Thus $\nu$ itself is not the current-flight mark law at a typical time.

For completeness this is an identification of flows, not only a one-time marginal identity. For $n\in\mathbb Z$ put
\[
 M_n=S^nM,\quad \ell_n=\ell(M_n),\quad w_n=w(M_n),\quad L_0=0,
\]
\[
 L_n=\sum_{k=0}^{n-1}\ell_k\ (n\ge1),\qquad
 L_n=-\sum_{k=n}^{-1}\ell_k\ (n\le-1).                     \tag{10}
\]
Local finiteness and two-sided completeness imply $L_n\to\pm\infty$ as $n\to\pm\infty$. For $s+t\in[L_n,L_{n+1})$ the suspension evolution is
\[
 U_t(M,s)=(S^nM,s+t-L_n).
\]
Its image under $\Psi$ is precisely the original centered billiard state at time $t$, outside the endpoint null sets.

Conversely, from an interior centered state, follow its trajectory backwards to its latest collision. This determines its age $s$, the boundary-centered configuration and normal, and the incoming velocity by reflecting the current outgoing velocity at that normal. It recovers the unique pair $(M,s)$. This is a measurable inverse almost everywhere. Equation (8) and invariance of $\mu$ then imply invariance of $\widehat\mu$ under $U_t$. No discrete sequence of independent flights has been substituted for the deterministic billiard.

## 4. Exact velocity correlation in collision coordinates

Define for $t\ge0$
\[
 C(t)=E_\mu[V_0\cdot V_t].
\]
For fixed $M$ and $s\in[0,\ell_0)$, there is a unique $n\ge0$ with
$L_n\le s+t<L_{n+1}$, except at flight endpoints. The two velocities are $w_0$ and $w_n$. For every fixed $t$, the endpoints have zero $ds$-measure, since there are countably many. Define the overlap length
\[
 A_n(t,M)=
 \left[\min\{\ell_0,L_{n+1}-t\}
               -\max\{0,L_n-t\}\right]_+,\qquad n\ge0.    \tag{11}
\]
It is the length of $[0,\ell_0)\cap[L_n-t,L_{n+1}-t)$. These intervals partition the allowed ages, so
\[
 \sum_{n\ge0}A_n(t,M)=\ell_0.
\]
Applying (8) to the time-$t$ velocity observable gives
\[
 \boxed{\quad
 C(t)=\gamma\sum_{n\ge0}\int
               (w_0\cdot w_n)A_n(t,M)\,\nu(dM).
 \quad}                                                    \tag{12}
\]
The exchange of the signed sum and integral is justified by
\[
 \gamma\sum_{n\ge0}\int |w_0\cdot w_n|A_n(t,M)\,d\nu
       \le\gamma\nu(\ell_0)=1.
\]
In particular $A_0(t,M)=(\ell_0-t)_+$ and $C(0)=1$. The $n\ge1$ terms retain both collision correlations and the random elapsed time. Collision-index stationarity alone does not remove either dependence.

There is a useful normalization check. Let $R$ be the waiting time to the next collision under $\mu$. Equation (8) gives
\[
 P_\mu(R>t)=\gamma\nu((\ell-t)_+),\qquad t\ge0.             \tag{13}
\]
Indeed the allowed ages are exactly $0\le s<\ell-t$. This is the $n=0$ overlap in (12), with velocity dot product one. It is a first-flight probability, not the whole correlation.

## 5. An absolutely convergent Laplace collision series

Fix a real $z>0$ and put
\[
 b_n=1-e^{-z\ell_n},\qquad H_{n-1}=\sum_{k=1}^{n-1}\ell_k
       \quad(n\ge1),\qquad H_0=0.
\]
Because $|C(t)|\le1$, its Laplace transform exists absolutely. Equations (11)--(12) give
\[
\begin{split}
 \boxed{\quad \widetilde C(z)
  &=\gamma\nu\left(\frac{\ell_0}{z}-\frac{b_0}{z^2}\right)\\
  &\quad+\frac{\gamma}{z^2}\sum_{n\ge1}
       \nu\left[(w_0\cdot w_n)b_0e^{-zH_{n-1}}b_n\right].\quad}
                                                               \tag{14}
\end{split}
\]
Here $\widetilde C(z)=\int_0^\infty e^{-zt}C(t)dt$. The formula uses no second moment of $\ell$.

To compute its coefficients directly, keep the age $s$ fixed. The $n=0$ contribution integrates $t$ from $0$ to $\ell_0-s$. Thus its double integral over $s$ and $t$ is
\[
 \int_0^{\ell_0}\frac{1-e^{-z(\ell_0-s)}}{z}\,ds
          =\frac{\ell_0}{z}-\frac{b_0}{z^2}.
\]
For $n\ge1$ the time interval is $[L_n-s,L_{n+1}-s)$, whose lower endpoint is nonnegative for $0\le s<\ell_0$. Its integral is
$e^{-z(L_n-s)}b_n/z$. Since $L_n=\ell_0+H_{n-1}$, integrating $s$ gives
\[
 \frac{b_n e^{-zL_n}}z\int_0^{\ell_0}e^{zs}ds
                 =\frac{b_0 e^{-zH_{n-1}}b_n}{z^2}.
\]

The infinite signed series has a pointwise nonnegative majorant. In fact
\[
 e^{-zH_{n-1}}b_n=e^{-zH_{n-1}}-e^{-zH_n}.
\]
Since $H_n\to\infty$, these telescope to
\[
 \sum_{n\ge1}b_0e^{-zH_{n-1}}b_n=b_0.                       \tag{15}
\]
The diagonal coefficient is nonnegative, and its sum with this majorant divided by $z^2$ is exactly $\ell_0/z$. Taking $\gamma\nu$ gives $1/z$. Hence all exchanges in (14) are justified by absolute integrability, and
\[
 |\widetilde C(z)|\le1/z.
\]
For truncation after index $N\ge1$, (15) gives the explicit error bound
\[
 \left|\text{tail after }N\right|
       \le\frac{\gamma}{z^2}\nu\left[b_0e^{-zH_N}\right]
           \longrightarrow0.                              \tag{16}
\]
There is no asserted rate uniform as $z\downarrow0$.

## 6. Independent checks and the remaining question

For a periodic sequence of positive gaps, sample its time phase uniformly over one period. Direct integration over that phase and its collision breakpoints computes $C(t)$ without a Palm identity. The collision law instead gives equal mass to each event of that period; (8) then weights events by their gaps. The audit script compares these two calculations exactly with rational numbers, for unequal gaps, negative and positive dot products, several observation times, and a nonergodic mixture with different component intensities.

A separate direct time integral over one period computes the Laplace transform of each periodic correlation, divided by $1-e^{-zP}$, where $P$ is its period. This is compared with (14), whose remaining tail is bounded by (16). Constant velocity gives $C(t)=1$ and $\widetilde C(z)=1/z$ for every choice of gaps: the diagonal and off-diagonal terms telescope to this value. This tests both factors of $z$ and the order of the intervening gaps. No such periodic example is used as evidence about Lorentz mixing.

The exact fixed-time covariance identity from round 4 is
\[
 E_\mu[X_tX_t^{\mathsf T}]
       =\frac{2I_d}{d}\int_0^t(t-u)C(u)du.
\]
Equations (12) and (14) specify the full collision information entering that identity. They do not bound long-time cancellation. In particular neither absolute time integrability of $C$, a strictly positive limiting covariance, a CLT, a quenched limit nor recurrence in dimension two follows from them. Passing $z$ to zero term by term in (14) has not been justified.

A next checkable local consequence is the right derivative $C'(0+)=-4\gamma/(d+1)$. It would require an explicit $o(t)$ estimate for multiple-collision contributions before using the cosine-law jump moment. That derivative is not claimed here. For long-time progress one instead needs estimates for the weighted multi-collision terms in (12) or (14), with their environment and flight-time dependence retained.
