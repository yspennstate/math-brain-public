# T384 nonorthogonal pair: frozen-residual endpoint selection

**Scope and status.** The deterministic, frozen-residual, normalized two-input endpoint problem is solved below for generic interior marks using the Filippov inclusion. This is a local building block, not a finite-width network limit or a residual-coupled theorem. It exposes an actual existence obstruction for the binary gate ODE and proves that the collapsed scaled initial condition does not select the boundary trajectory. No full T384 or novelty claim is made.

Let

\[
G=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad 0<|\rho|<1,
\qquad a=zr_1,\quad b=zr_2,
\]

where \(z\ne0\) and the residual \(r\) is constant. Boundary time is \(s=L_mt\). The endpoint projected mark \(v(s)\in\mathbb R^2\), initialized at \(v(0)=u=(U\cdot x_1,U\cdot x_2)\), has the four open-sector velocities

| Sector of \(v\) | Velocity \(F(v)\) |
| --- | --- |
| \(--\) | \((0,0)\) |
| \(+-\) | \(a(1,\rho)\) |
| \(-+\) | \(b(\rho,1)\) |
| \(++\) | \((a+\rho b,\rho a+b)\) |

This is exactly \(F=G(a1_{v_1>0},b1_{v_2>0})^T\) off the axes. At an axis, use the essential convex hull of the adjacent velocities. Equivalently, a Filippov solution is absolutely continuous and satisfies

\[
\dot v=G(a\theta_1,b\theta_2)^T\quad\text{a.e.},\qquad
\theta_j=1\ (v_j>0),\quad\theta_j=0\ (v_j<0),\quad
\theta_j\in[0,1]\ (v_j=0). \tag{1}
\]

At the origin the four-sector convex hull is precisely the parallelogram described by the two independent fractions in (1).

## Generic-mark theorem and event rule

Assume

\[
ab\rho(a+\rho b)(b+\rho a)\ne0. \tag{2}
\]

Take an initial mark with \(u_1u_2\ne0\), excluding the at most three rays on which the straight trajectory in its initial nonzero sector reaches the origin exactly. Then (1) has one forward solution. After finitely many sector/face events it is either stationary, a constant-velocity ray in an open sector, or a constant-velocity ray on an attracting positive half-axis. Consequently there is a \(p=p(a,b,\rho,u)\) and finite \(C\) such that

\[
\sup_{0\le t\le T}\left\|\frac{v(Lt)}L-tp\right\|\le \frac C L
\quad\text{for every }L\ge1,\ T>0. \tag{3}
\]

The event rule computes \(p\) without integrating a discontinuous ODE. In an open sector, move along its constant velocity until the first axis hit, if any. A simultaneous hit of both axes is excluded by the mark condition. At \(v_1=0,v_2>0\), the inactive-side and active-side normal speeds are

\[
n_-=\rho b,\qquad n_+=a+\rho b. \tag{4}
\]

If both have the same sign, cross in that direction. If \(n_->0>n_+\), slide, with the **forced** fraction and tangential speed

\[
\theta_1^*=-\frac{\rho b}{a}\in(0,1),\qquad
\dot v=(0,(1-\rho^2)b). \tag{5}
\]

The reverse, repelling configuration \(n_-<0<n_+\), cannot be reached forward from either open neighboring sector. At \(v_2=0,v_1>0\), interchange indices: \(n_-=\rho a\), \(n_+=b+\rho a\), and an attracting slide has \(\theta_2^*=-\rho a/b\), \(\dot v=((1-\rho^2)a,0)\). At a negative half-axis, the only reachable case is an active coordinate driven toward zero; it sticks there with zero velocity. A slide in (5) directed toward the origin occurs only when \(a,b<0\) and \(\rho<0\). It reaches the origin and stays there.

**Proof.** In each open sector the ODE is constant and unique. The nonzero factors in (2) make every positive-face normal speed strictly nonzero on either side. Same-sign normals force a unique crossing. Opposed normals pointing inward force a path starting at the face to stay on it: an excursion into either open side would have derivative directed back toward the face and cannot start at zero. The zero-normal convex combination is unique and gives (5). Outward opposed normals cannot be hit from either side. At a negative half-axis the inactive field is zero and the active normal points toward the face in the only reachable case; the same excursion argument gives sticking. A positive half-axis can be crossed at most once, because its adjacent normal signs are fixed. A negative half-axis terminates motion. Thus there are finitely many events, except possibly a positive-face slide that runs to the origin. As noted above, inward sliding implies \(a,b<0\). In that case \(\Phi(v)=a(v_1)_++b(v_2)_+\) is concave, (1) is \(\dot v\in G\partial\Phi(v)\), and the subgradient anti-monotonicity gives

\[
\frac12\frac d{ds}\|v-\tilde v\|_{G^{-1}}^2
= (v-\tilde v)^T(g-\tilde g)\le0.
\]

Hence the solution from the origin is uniquely the constant zero path. The excluded initial rays are precisely where an open-sector line hits the origin without an intervening face event; in the mixed-sign case a continuation from that origin need not be unique. Every remaining trajectory eventually has the form \(v(s)=ps+c\), or becomes constant. Bounding \(v(s)-ps\) over the finite transient proves (3). The possible nonzero velocities are the three open-sector vectors above and the two sliding vectors; \(p=0\) in the stationary case.

The potential identity also holds on every Filippov path:

\[
\frac d{ds}\Phi(v(s))=\dot v(s)^TG^{-1}\dot v(s)\ge0\quad\text{a.e.} \tag{6}
\]

At a zero coordinate, its time derivative is zero almost everywhere on its zero set, so the choice of \(\theta_j\) does not affect the chain rule. Identity (6) is useful for checking the event construction; it does not select a trajectory from the collapsed origin when \(\Phi\) is nonconcave.

## Exact attracting-face example and loss of the initial mark

Set \(\rho=1/2,z=1,r=(-1,1)\), so \(a=-1,b=1\). Then

\[
F_{--}=0,\quad F_{+-}=(-1,-1/2),\quad
F_{-+}=(1/2,1),\quad F_{++}=(-1/2,1/2).
\]

Every mark in either the \(-+\) or \(++\) sector reaches \(v_1=0,v_2>0\), then slides with \(\theta_1=1/2\) and \(\dot v=(0,3/4)\). Every mark in \(+-\) reaches \(v_1=0,v_2<0\) and stops; \(--\) is stationary from the start. For example,

\[
u=(-1,1):\quad v(s)=(-1+s/2,1+s)\quad(0\le s\le2),
\quad v(s)=(0,3+3(s-2)/4)\quad(s\ge2);
\]

\[
u=(1,-1):\quad v(s)=(1-s,-1-s/2)\quad(0\le s\le1),
\quad v(s)=(0,-3/2)\quad(s\ge1).
\]

Both scaled trajectories start at \(q(0)=\lim_{L\to\infty}u/L=0\), yet their limits are respectively \(q(t)=(0,3t/4)\) and \(q(t)=0\), uniformly on compact \(t\)-intervals. Even the metric-minimal velocity in the Clarke set at the origin is zero, since the all-inactive corner is zero. Thus an unmarked ODE/inclusion initialized only at \(q(0)=0\) loses the endpoint selection.

## Binary-gate obstruction and the precise role of sliding

At the positive face in this example, the normal speed is \(+1/2\) on the inactive side and \(-1/2\) on the active side. After a trajectory arrives at the face, **no absolutely continuous Carathéodory continuation exists** if the gate at zero is fixed to either binary value 0 or 1. Indeed, any positive excursion from zero would have derivative \(-1/2\) throughout that excursion and hence cannot begin at zero; any negative excursion would have derivative \(+1/2\) and is equally impossible. The only remaining path has normal coordinate identically zero, whose derivative is zero, contrary to either binary boundary value. This applies locally while \(v_2>0\). A conventional \(1_{v_1>0}\) choice at equality therefore does not supply a finite-width flow through this event. The Filippov fraction \(1/2\) is not optional: it is forced by zero normal velocity.

For a general attracting positive face, \(G^{-1}\)-metric minimization over its Clarke velocities picks exactly the sliding fraction. At \(v_1=0,v_2>0\), write \(F_\theta=G(a\theta,b)\). Then

\[
\frac d{d\theta}\|F_\theta\|_{G^{-1}}^2
=2a(\rho b+a\theta),
\]

so the strict minimizer is \(\theta=-\rho b/a\in(0,1)\). This agrees with Filippov sliding **at the attracting face**; the global metric-minimal rule at the origin instead chooses zero and cannot recover mark dependence.

The vector selection alone does not settle the evolving-residual or NTK problem. On a viable slide at \(v_1=0,v_2>0\), the endpoint output \(p=z((v_1)_+,(v_2)_+)\) obeys the **constrained Schur-complement law**

\[
\dot p=(0,z^2(1-\rho^2)r_2)
=z^2\operatorname{diag}(0,1-\rho^2)r.
\]

In particular the first output derivative is zero, although the projected first coordinate is being pushed from both sides. Algebraically the fractional-gate matrix \(z^2D_\theta G D_\theta\) has the same product with this particular residual, because tangency imposes \(\theta r_1+\rho r_2=0\); its \((1,1)\) entry is \(z^2\theta^2\), and \(\theta\) changes with the residual. A formal time average of binary pre-step factors \(z^2DGD\) with active fraction \(\theta\) instead has \((1,1)\) entry \(z^2\theta\). In the example above that average sends \(r=(-1,1)\) to \((-1/4,3/4)\), whereas the sliding output velocity is \((0,3/4)\). Thus the averaged binary Gram is **not an output-generating kernel** for the slide. Fixed-step Euler crossings require exact ReLU secants to recover the missing first-coordinate change; the companion discrete analysis in `agents/e03_discrete.md` treats that frozen case. A network theorem needs an explicit boundary selection and a compatible residual/output law beyond this frozen endpoint result.

Finally, initially inactive gates can reactivate even without sliding: with \(\rho=1/2,a=b=1,u=(1,-1)\), the \(+-\) sector velocity is \((1,1/2)\), so \(v_2\) reaches zero at \(s=2\) and becomes positive. This directly rules out independent absorbing projected clocks for nonorthogonal inputs.
