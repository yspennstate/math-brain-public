# P0289: faster Cox modulation can increase mean workload

Status: author-checked counterexample candidate to the universal monotonicity clause of Leskela's Problem 1 (Ross's second conjecture). Its separate request for a necessary-and-sufficient condition remains unresolved. No novelty or independent-review certificate is claimed. The construction uses a finite-state stationary ergodic CTMC as its intensity environment and deterministic unit service times.

Primary source: Lasse Leskela, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), 213-215, Problem 1 on journal page 214; institutional PDF page 3. https://acris.aalto.fi/ws/portalfiles/portal/89616571/Ross_s_second_conjecture_and_supermodular_stochastic_ordering.pdf . The source specifies mean stationary workload, not a transient or arbitrarily time-weighted average. Its complete three-page article was read. The institution's PDF has a cover page.

## A uniform second-order bound with an explicit remainder

Let $F(t)$ be any stationary nonnegative intensity environment bounded by $M$, with mean $a$. Let the arrival process be Cox with intensity $\lambda_c(t)=\epsilon F(ct)$. Customers require exactly one unit of service from a rate-one FIFO server. Assume $\rho=\epsilon M<1$. Denote stationary workload by $V_c$ and its mean by $w(c)$.

Couple the arrivals by thinning a stationary homogeneous Poisson process of rate $\rho$. Its stationary M/D/1 workload $\widehat V$ dominates $V_c$ and has finite moments. For an arrival configuration $A$, define its parallel-service shot workload at time zero by

$$
 S(A)=\sum_{T\in A\cap(-1,0]}(1+T).
$$

The single-server workload is

$$
 V(A)=\sup_{u\ge0}\{N_A(-u,0]-u\},
$$

including zero in the supremum. Put $D(A)=V(A)-S(A)$. This difference is nonnegative and is nondecreasing when arrivals are added. To check the latter, add one arrival of age $v$. If $v\ge1$, its shot contribution is zero and workload cannot decrease. If $0<v<1$, any candidate $u>v$ in the supremum gains one. A candidate $u<v$ is dominated, after the addition, by candidates at $v+\eta$ as $\eta\downarrow0$, whose limiting value is at least its old value plus $1-v$. Thus $V$ increases by at least $1-v$, exactly the new shot contribution. Apply this argument first on a finite history and then pass to increasing histories.

Consequently

$$
 0\le D(A)\le D(\widehat A),\qquad
 E D(\widehat A)=\frac{\rho^2}{2(1-\rho)}.                 \tag{1}
$$

For completeness, the identity follows from $E\widehat S=\rho/2$ by Campbell's formula and $E\widehat V=\rho/[2(1-\rho)]$. The latter can be derived directly from stationarity of $\widehat V^2$: between arrivals its derivative is $-2\widehat V$, while a unit-service arrival increases its square by $2\widehat V+1$. The stable Poisson queue has finite exponential moments, so this expectation identity is justified; alternatively one can stop and use its regenerative busy periods.

Apply the same square-workload balance to the Cox queue. The intensity is bounded, and domination supplies the required moments. It gives

$$
 w(c)=\frac{\epsilon a}{2}+E[\lambda_c(0)V_c(0)].
$$

Conditioning on the environment and using Campbell's formula for the shot term yields the exact bounded expansion

$$
 w(c)=\frac{\epsilon a}{2}
 +\epsilon^2\int_0^1(1-u)E[F(0)F(-cu)]\,du+R_c,
 \qquad
 0\le R_c\le\frac{\epsilon^3M^3}{2(1-\epsilon M)}.          \tag{2}
$$

The remainder bound uses (1) and $\lambda_c(0)\le\epsilon M$. It is uniform in $c$. In particular this is not a numerical small-traffic extrapolation or an uncontrolled formal power series.

## A finite-state Markov intensity

Take $m=1024$, $\theta=2\pi/m$, and let $X_t$ be the stationary CTMC on the cyclic group $\mathbb Z/m\mathbb Z$ with only clockwise jumps, each at rate

$$
 r=\frac1{\sin\theta}.
$$

Its stationary law is uniform; it is irreducible and mixing in continuous time. Set

$$
 F(t)=2+\cos(\theta X_t+\theta/4),\qquad
 \delta=\frac{1-\cos\theta}{\sin\theta}=\tan(\pi/m).
$$

Thus $1\le F\le3$ and $a=2$. The displayed cosine values are all distinct: equality for two different cyclic labels would require $k+l+1/2$ to be an integer multiple of $m$. Therefore $F$ itself, not merely its hidden environment, is a finite-state stationary ergodic CTMC after relabeling.

The elementary Poisson jump-count generating function gives

$$
 E[F(0)F(t)]=4+\tfrac12 e^{-\delta|t|}\cos t.              \tag{3}
$$

Indeed the first Fourier character has eigenvalue
$r(e^{i\theta}-1)=-\delta+i$, and the uniform average removes the second spatial harmonic. This does not require reversibility or stochastic monotonicity; the directed cycle has neither of those extra properties in the intensity ordering.

Define

$$
 I_\delta(c)=\int_0^1(1-u)e^{-\delta cu}\cos(cu)\,du.
$$

Equations (2)-(3) now read

$$
 w(c)=\epsilon+2\epsilon^2+\tfrac12\epsilon^2 I_\delta(c)+R_c,
 \qquad 0\le R_c\le\frac{27\epsilon^3}{2(1-3\epsilon)}.    \tag{4}
$$

## Explicit reversal of the proposed monotonicity

Choose $c_1=2\pi$, $c_2=3\pi$ and $\epsilon=10^{-4}$. Without damping,

$$
 I_0(c)=\frac{1-\cos c}{c^2},\qquad
 I_0(2\pi)=0,\quad I_0(3\pi)=\frac2{9\pi^2}.
$$

The inequality $1-e^{-x}\le x$ gives

$$
 |I_\delta(c)-I_0(c)|\le\frac{\delta c}{6}.
$$

Hence

$$
 \tfrac12[I_\delta(3\pi)-I_\delta(2\pi)]
 \ge\frac1{9\pi^2}-\frac{5\pi\delta}{12}.
$$

Since $\tan x<2x$ for $0<x<\pi/4$, here $\delta<\pi/512$. Using only $\pi^2<10$ gives the rational lower bound

$$
 \tfrac12[I_\delta(3\pi)-I_\delta(2\pi)]
 >\frac1{90}-\frac{50}{6144}=\frac{137}{46080}.
$$

At the chosen $\epsilon$ the normalized remainder bound is

$$
 \frac{27\epsilon}{2(1-3\epsilon)}=\frac{27}{19994}<\frac1{700}.
$$

Therefore (4) proves, with no simulation,

$$
 \boxed{\displaystyle
 w(3\pi)-w(2\pi)
 >\epsilon^2\left(\frac{137}{46080}-\frac1{700}\right)
 =\epsilon^2\frac{2491}{1612800}>0.}
$$

The queue is stable since its intensity is at most $3\epsilon<1$. Thus faster modulation increases mean stationary workload for this fully specified finite-state Markov environment and iid deterministic service times.

## Second derivation of the coefficient

The second-order coefficient can also be recovered by adding two arrivals to an empty queue. Put their ages at $y+d$ and $y$, where $0\le d\le1$. The interaction increment, beyond the sum of their separate workloads, is $y$ for $0\le y\le1-d$, is $1-d$ for $1-d\le y\le1$, and is $2-d-y$ for $1\le y\le2-d$. Its integral over $y$ is exactly $1-d$. The ordered pair therefore contributes

$$
 \epsilon^2\int_0^1(1-d)E[F(0)F(-cd)]\,dd,
$$

matching (2). This second calculation checks the kernel, absence of an extra factorial, and the unit-service time scale. The uniform bound in (2), rather than this formal coefficient check alone, makes the counterexample rigorous.

## Limits and further work

The universal assertion in Problem 1 is refuted if the argument survives independent review. The requested necessary-and-sufficient condition on the intensity process is not supplied. The construction does not refute the established doubly stochastically monotone case, and does not settle Problem 2 about a deterministic image of such a chain. It does not establish anything for three-state environments: the explicit choice here has1024 distinct intensity states.

Initial targeted searches found the original author note and older Ross-type literature, including Miyoshi-Rolski2004 and Heyman's older counterexample concerning nonstationary-arrival formulations. These must be compared in full before claiming originality. Mean stationary workload, arrival-Palm waiting time and a transient time average must not be conflated. For deterministic unit service the stationary workload balance also relates arrival-Palm waiting mean to $w(c)$, but the source's exact workload formulation is the target used here. No new paid service, numerical simulation or public publication was used.
