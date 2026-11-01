# Same-sign positive residuals: stopped full-gate law and inherited reflection

**Status.** Internally proved and independently reviewed proof for the $R_1,R_2>0$, $0<\rho<1$ sector of T384, conditional on the already proved `BOUNDARY_GRID.md`, `MACRO_COMPACTNESS.md`, and the monotone relay facts of run 012528. Independent review: reviews/i03_same_sign_review.md; assembly review: reviews/i03_all_initial_review.md. It makes no claim about negative initial residuals, negative correlation, deep networks, test inputs, external priority, or convergence of pre-step tangent Grams in $L^1/J_1$.

Use exactly the two-unit-input shallow stable initialization and actual simultaneous GD of `BOUNDARY_GRID.md`: $G=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)$, $a=m^{1/\alpha}$, $L=(\log m)^{1/\alpha}$, physical step $h=\gamma/L$, $F,C,N$ the joint initialization primitives, and $R=y-F$. Condition on $E_{++}=\{R_1>0,R_2>0\}$. The boundary-grid endpoint associated with $(z,u)$ is

\[
v_0=Xu,\qquad v_{n+1}=v_n+\gamma zG D(v_n)R. \tag{1}
\]

Define the original-mark selector and finite square mass

\[
\chi(z,u)=\mathbf1_{\{z>0,\ \max((Xu)_1,(Xu)_2)>0\}},\qquad
P=\int z^2\chi(z,u)N(dz,du). \tag{2}
\]

Put $Q=C+PG$, $r^0(t)=e^{-Qt}R$, $I^0(t)=\int_0^t r^0(s)ds$, and let $\tau=\inf\{t>0:\min_j r^0_j(t)=0\}$, with $\tau=\infty$ if there is no finite zero. If $\tau<\infty$, exactly one coordinate $b$ vanishes; call the other $p$. For $I(t)=\int_0^t r(s)ds$, let

\[
\mathcal S(w)(t)=w(t)-\min\bigl(0,\min_{0\le s\le t}w(s)\bigr),\qquad
V_b(t)=\mathcal S(I_b+\rho I_p)(t),\quad
V_p(t)=\rho V_b(t)+(1-\rho^2)I_p(t). \tag{3}
\]

**Claim.** On every fixed physical horizon, the actual polygonal GD residuals and initial primitives $(r_m,f_{m,0},C_{m,0},N_m)$, conditionally on the finite-width initial event $R_{m,1}>0,R_{m,2}>0$, converge jointly in law to $(r,F,C,N)$. The limiting residual is specified as follows. If $\tau=\infty$, $r=r^0$ on every finite horizon. If $\tau<\infty$, $r=r^0$ through $\tau$ and globally satisfies

\[
r(t)=R-CI(t)-P V(t), \tag{4}
\]

with the coordinate order $(b,p)$ in (3). Every selected atom has limiting endpoint $q_{z,u}=zV$; every other atom has endpoint zero. The limiting output is $y-r$. In particular the law is independent of the fixed critical multiplier $\gamma>0$. This is a statement about actual GD output paths, **not** about $L^1/J_1$ convergence of the binary pre-step Gram.

## A. Frozen entrance is finite, strict, and independent of gamma

For $R_1,R_2>0$, the four velocities in (1), divided by $z$, are $0,(R_1,\rho R_1),(\rho R_2,R_2),GR$ in sectors $--,+-,-+,++$, respectively. If $z>0$, both projections are nondecreasing. An initially $--$ atom is exactly stationary. If either gate is initially on, that coordinate remains on and drives the other projection upward by at least $\gamma\rho z\min(R_1,R_2)>0$ per step until it activates. Hence the row reaches strict $++$ in finitely many steps and stays there under frozen $R$. If $z<0$, both projections are nonincreasing, and every positive projection decreases at least $\gamma|z|\min(R_1,R_2)$ per step while active. It therefore reaches $--$ in finitely many steps, after which the row is exactly stationary. Initially dead $z<0$ rows already stay dead. The original mark has a density and the finite-grid hyperplane argument of `BOUNDARY_GRID.md` removes axis equalities at every fixed integer step, simultaneously for the countable PPP atoms. The finite certificates are consequently strict almost surely.

The selector (2) is thus exact for the frozen grid, not an assumed zero-start choice. It is locally constant at each generic finite certificate. Its mass is finite because $\int z^2N<\infty$ almost surely. More explicitly, $P$ is a positive $\alpha/2$-stable variable, independent of $(F,C,R)$, with Laplace transform

\[
\mathbb E e^{-sP}=\exp\{-\pi_X c\Gamma(1-\alpha/2)s^{\alpha/2}\},\qquad
\pi_X=\mathbb P\{\max((XU)_1,(XU)_2)>0\}\in(1/2,1), \tag{5}
\]

where $c=\Gamma(\alpha)\sin(\pi\alpha/2)/\pi$. This marginal law is optional for the matching proof; only (2) and $P<\infty$ are used below.

## B. Strict positive off-diagonal action

The initialization formula $C=\sum_{\ell,\pm}S_\ell^\pm q_\ell^\pm(q_\ell^\pm)^T$, with $q_\ell=Xe_\ell$ and $q_\ell^\pm=(\pm q_\ell)_+$, gives $C_{12}\ge0$. Since $\rho=x_1\cdot x_2=\sum_\ell x_{1\ell}x_{2\ell}>0$, some coordinate has $x_{1\ell}x_{2\ell}>0$. Choose its common-sign ReLU ray. Both ray components are strictly positive, and its stable square weight $S_\ell^\pm$ is strictly positive almost surely: its Laplace transform tends to zero as its argument tends to infinity, so it has no atom at zero. Hence

\[
C_{12}>0,\qquad Q_{12}=C_{12}+\rho P>0\quad\text{a.s.} \tag{6}
\]

The prior initialization theorem also gives $C\succ0$, so $Q\succ0$. At a finite first zero of $r^0$, both coordinates cannot be zero because $e^{-Q\tau}$ is invertible and $R\ne0$. If $r^0_b(\tau)=0<r^0_p(\tau)$, then

\[
(r^0_b)'(\tau)=-Q_{12}r^0_p(\tau)<0. \tag{7}
\]

Thus the $Q$ trajectory crosses transversally into the mixed quadrant. The no-exit case is included pathwise. In fact, since $Q$ is symmetric with positive off-diagonal, its fast eigenvector has two positive coordinates and its slow eigenvector has opposite signs. A positive $R$ has no finite exit exactly when it lies on the fast eigenray. Independence and the density of $R$ make this exceptional case probability zero, but the proof below does not discard it.

## C. Identify the stopped law from actual GD, without using its proposed continuation

Take an arbitrary joint subsequential limit supplied by `MACRO_COMPACTNESS.md`, represented with residual $r$, marked endpoint paths $q_{z,u}$, gate fractions, and its effective action

\[
r'=-Q_{\rm eff}(t)r,\qquad
Q_{\rm eff}=C+\int z^2D(\theta)GD(\theta)N. \tag{8}
\]

Work pathwise after localization to bounded initial energy and residual and to a finite physical horizon $T$. The theorem gives uniform actual-residual convergence, uniform row-weight-sign retention for each fixed nonzero $z$, bounded endpoint path slopes, and the exact output identity with uniform removal of small $|z|$ square mass. Augment the joint representation by the countable fixed-grid endpoint coordinates; `BOUNDARY_GRID.md` and diagonal extraction allow this without changing the macro conclusion.

Let $\sigma=\inf\{t>0:\min_j r_j(t)=0\}$, with infinity if no zero. For any rational $t<\sigma$, continuity makes both limiting residual coordinates uniformly positive on $[0,t]$. Under the joint coupling, actual residuals are then positive at every grid step through $t$, eventually. Fix a finite marked cutoff $\varepsilon<|z|<M,\ \|u\|<B$. Each retained atom has a finite random strict certificate from A. Restrict first to the event that the maximum certificate step is at most a deterministic $K$; the fixed-$K$ boundary-grid theorem transfers every certificate to actual GD. Then let $K\uparrow\infty$. No uniform certificate time over the entire infinite PPP is asserted.

After that transferred certificate, a selected $z>0$ actual row stays fully active as long as both actual residual coordinates are positive: the exact projected increments have both coordinates positive and the actual output weight retains sign. Dead rows remain exactly stationary for all later residuals. The finite entrance time is $O(1)$ boundary steps, hence physical time $O(1/L)$, and its $O(1)$ endpoint state vanishes after division by $L$. Summing the exact projected updates and using uniform residual and weight convergence gives, for each selected atom and $t<\sigma$,

\[
q_{z,u}(t)=zG\int_0^t r(s)ds;\qquad
q_{z,u}(t)=0\quad\text{for every unselected atom}. \tag{9}
\]

The finite-cutoff output identity and the prior uniform small $|z|$ square-mass bound then imply $r=R-(C+PG)\int_0^t r$ on $[0,\sigma)$. Large $|z|$ and original-mark cutoffs are removed by finite-intensity tightness. Therefore $r(t)=r^0(t)$ until its own first residual-axis exit. By continuity, its first exit equals $\tau$: an earlier exit would occur while $r^0$ is strictly positive, and a later one would pass through the zero of $r^0$. If $\tau=\infty$, (9) and $r=r^0$ hold on every finite horizon, completing that branch.

At a finite $\tau$, (9) extends to the endpoint by continuity. Since $r_j>0$ on $[0,\tau)$, both $I_j(\tau)>0$, so for each selected $z>0$

\[
q_{z,u}(\tau)=zGI(\tau)\in(0,\infty)^2,\qquad
\eta_{z,u}(\tau):=q_p(\tau)-\rho q_b(\tau)
=z(1-\rho^2)I_p(\tau)>0. \tag{10}
\]

These are the **inherited nonzero endpoint data** at the crossing. Resetting endpoints to zero here would change the dynamics.

## D. The crossing and mixed signs require no atom-selection assumption

The action in (8) is bounded on each fixed horizon by $M_*:=\|C\|+\|G\|\int z^2N$. Every off-diagonal contribution is nonnegative because $\rho>0$ and $0\le\theta_j\le1$, so $Q_{{\rm eff},12}(t)\ge C_{12}>0$. At $\tau$, $r_b=0<r_p$. By continuity, choose a short right interval on which $r_p\ge r_p(\tau)/2$ and $M_*|r_b|\le C_{12}r_p(\tau)/4$. For almost every time there,

\[
r_b'=-Q_{{\rm eff},bb}r_b-Q_{{\rm eff},bp}r_p
\le -C_{12}r_p(\tau)/4<0. \tag{11}
\]

It follows by integration that $r_b(t)<0<r_p(t)$ immediately after $\tau$. Once strictly mixed, $s=(-r_b,r_p)$ solves a bounded time-dependent Metzler system: its off-diagonal entries are $Q_{{\rm eff},bp}\ge0$, and each $s_j'\ge-M_*s_j$. Consequently $s_j(t)\ge s_j(t_0)e^{-M_*(t-t_0)}>0$ on every later finite horizon. This proves global mixed-sign persistence for **any** actual-GD subsequential limit before identifying its post-exit atoms. It also makes the first-crossing argument noncircular. A separate convergence theorem for finite-width random crossing times is unnecessary.

## E. Inherited reflection and preservation of every selected support

Fix one selected atom in the subsequential limit. Starting from (10), suppose its support coordinate $q_p$ has a first zero after $\tau$. On the preceding interval $q_p>0$, so its support gate fraction is one and its normal equation is

\[
q_b'=a(t)\theta_b+c(t),\quad
a(t)=zr_b(t)\le0,\quad c(t)=\rho z r_p(t)>0,\quad
\theta_b\in H(q_b). \tag{12}
\]

The negative part of $q_b$ cannot grow from zero: wherever $q_b<0$, $\theta_b=0$ and $q_b'=c>0$; the absolutely continuous chain rule gives $(q_b)_-=0$ throughout that interval. Also the exact tangential cancellation gives

\[
(q_p-\rho q_b)'=z(1-\rho^2)r_p>0. \tag{13}
\]

Thus $q_p=\rho q_b+\eta\ge\eta(\tau)>0$, contradicting a first support zero. Hence $q_p>0$ forever and (12)--(13) hold globally. There is no uniform positive support margin across infinitely many atoms: this argument is atomwise, followed by a countable intersection.

The scalar monotone relay of run 012528 now applies with the **nonzero** initial value $q_b(\tau)>0$. Its reflected solution is

\[
q_b(t)=w(t)-\min\bigl(0,\min_{\tau\le s\le t}w(s)\bigr),\quad
w(t)=q_b(\tau)+z\int_\tau^t(r_b+\rho r_p)ds. \tag{14}
\]

The relay's uniqueness does not require $a(\tau)<0$: here $a\le0$, is strictly negative after $\tau$, and graph monotonicity yields $(q_b-\tilde q_b)(\theta_b-\tilde\theta_b)\ge0$, so the squared distance of two normal solutions cannot increase. The running-minimum construction is valid at the isolated zero $a(\tau)=0$; if $a=0,c>0$, the regulator is inactive there. Equation (13) reconstructs $q_p$ uniquely. Before $\tau$, the driver $I_b+\rho I_p$ is strictly increasing and positive, so stitching (14) to (9) is exactly $q_{z,u}=zV$ from (3). Every dead row remains zero from its finite-grid death. Thus the actual-GD inclusion itself selects the inherited reflected continuation; no choice at a newly collapsed origin is made.

There is also a direct finite-width robustness check. At any fixed time just before $\tau$, a retained selected row has $x=V_b>0$ and $\eta=V_p-\rho V_b$ both of order $L$, with positive normalized limits. On a later interval where the actual supporting residual remains positive, its exact gate recursion gives $\eta_{n+1}-\eta_n=\gamma(1-\rho^2)(W_{i,n}/a)r_{p,n}>0$ while support is active. A uniform bound $D$ on the inward normal step makes $x> -\gamma D$ forward invariant, even as the other residual changes sign. Hence $V_p=\eta+\rho x>0$ for all sufficiently large widths. This check is consistent with, but not needed in place of, the limiting first-zero argument.

## F. Closed equation, uniqueness, conditioning, and scope

Absolute uniform convergence of the Poisson output sum follows from $\sum z^2<\infty$, the bound $\|V(t)\|\le K\int_0^t\|r(s)\|ds$, and the uniform small-atom estimate already proved for actual GD. Summing $zq_{z,u}=z^2V$ over selected atoms gives $PV$ and yields (4) on all finite horizons.

The running-minimum map $\mathcal S$ is $2$-Lipschitz in the prefix sup norm. Thus the right side of (4), viewed as a map on $r$, has difference at time $t$ bounded by $K\int_0^t\sup_{s\le v}\|\Delta r(s)\|dv$, where $K<\infty$ depends on $C,P,\rho$. Picard iteration gives a local solution, the linear-growth/Gronwall bound prevents blowup, and continuation gives a unique global solution. Equivalently, uniqueness follows directly by Gronwall for any two solutions. On the pre-exit interval its reflection is inactive, so it coincides with $r^0$. After exit, the reflected endpoint action is $G r$ wherever $V_b>0$, and is $\operatorname{diag}(0,1-\rho^2)r$ in the $(b,p)$ order at almost every time where $V_b=0$. Both give a bounded PSD addition to $C$ with nonnegative off-diagonal. The same transversal crossing and Metzler comparison therefore keep the selected solution in its mixed phase, with $V_p>0$. Every subsequential actual-GD limit is the same measurable function of $(F,C,N)$, establishing convergence of the full conditional sequence in $C([0,T];\mathbb R^2)$ for every fixed $T$.

Finally $R$ has a full-dimensional continuous density, so $\mathbb P(R_1R_2=0)=0$; $E_{++}$ has positive probability and its finite-width indicator converges jointly to the limiting indicator. Standard conditioning on this continuity event gives the claimed conditional convergence. The proof handles the deterministic exceptional $\tau=\infty$ branch explicitly. Negative initial residuals require a separately checked sign-reflected classification; they are not asserted here.
