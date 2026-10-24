# T384: stopped actual-GD law in a negative-correlation outer cone

**Status: internally proved; independent audit in reviews/j03_review.md.** This identifies the actual simultaneous-GD training output, and optionally any fixed finite collection of test outputs, through the first return of a cumulative supporting clock. It does **not** select the dynamics after that return. The required initialization, finite-grid transfer and uniform-horizon compactness/cutoff estimates are the proved results in `../20261023T232238Z/{BOUNDARY_GRID,MACRO_COMPACTNESS}.md`; the frozen entrance classifier and exact one-gate invariant are in `../20261024T032106Z/NEGATIVE_RHO_NEXT.md`. No pre-step tangent-Gram convergence is claimed.

## Model and statement

Fix two linearly independent unit training inputs, with $G=XX^T=\begin{psmallmatrix}1&-a\\-a&1\end{psmallmatrix}$, $0<a<1$, the shallow original-coordinate iid symmetric $\alpha$-stable initialization, $0<\alpha<2$, and fixed critical multiplier $\gamma>0$. Use $A_m=m^{1/\alpha}$, $L_m=(\log m)^{1/\alpha}$, $h_m=\gamma/L_m$, $v_{i,n}=XU_{i,n}$, $z_{i,n}=W_{i,n}/A_m$, $r_{m,n}=y-f_{m,n}$. The exact simultaneous update is

\[
v_{i,n+1}=v_{i,n}+\gamma z_{i,n}G D(v_{i,n})r_{m,n},\qquad
W_{i,n+1}=W_{i,n}+(\gamma/A_m)r_{m,n}^{T}(v_{i,n})_+ . \tag{1}
\]

Let $(F,C,N)$ be the joint primitive of `BOUNDARY_GRID.md`, $R=y-F$, and condition on the **strict outer event**

\[
E=\{R_1>0,\ R_2>0,\ R_1<aR_2\}. \tag{2}
\]

For an original Poisson mark $u$, write $V=Xu=(V_1,V_2)$. Define disjoint selectors and their square masses by

\[
\chi_1(z,u)=\mathbf1_{\{z>0,V_1>0,V_2\le0\}},\quad
\chi_2(z,u)=\mathbf1_{\{z>0,V_2>0\}},\qquad
P_j=\int z^2\chi_j(z,u)N(dz,du). \tag{3}
\]

The $\chi_2$ class includes the initially double-active $V_1,V_2>0$ rows: in the outer cone they exit gate 1 in a finite frozen-grid history. All negative-$z$ rows ultimately die, and positive-$z$ rows initially inactive on both coordinates are already dead. Put

\[
Q=C+\operatorname{diag}(P_1,P_2),\quad r^0(t)=e^{-Qt}R,\quad
I^0(t)=\int_0^t r^0(s)ds=Q^{-1}(I-e^{-Qt})R, \tag{4}
\]

and let $\tau$ be the first $t>0$ at which either $I^0_1(t)$ or $I^0_2(t)$ returns to zero, with $\tau=\infty$ if neither returns. Both clocks are positive just after zero. On every compact $0\le t<\tau$, the conditional joint macroscopic limit of the **actual GD** residual and marked endpoints is

\[
r(t)=r^0(t),\qquad
q_{z,u}(t)=
\begin{cases}
z(I^0_1(t),-aI^0_1(t)),&\chi_1(z,u)=1,\\
z(-aI^0_2(t),I^0_2(t)),&\chi_2(z,u)=1,\\
0,&\chi_1=\chi_2=0.
\end{cases} \tag{5}
\]

These endpoint identities extend by continuity **to** $\tau$ when it is finite. In particular, for any deterministic $T$, conditional on $E\cap\{\tau>T\}$, the polygonal residual and training output converge jointly with the initial primitives in $C([0,T])$ to $r^0$ and $y-r^0$. There is no atom at $\tau=T$; see below. The convergence also has a precise stopped formulation using a candidate finite-width stopping time, given after the proof.

The selectors use the original-coordinate stable mark law, not a Gram-only angular surrogate. With $c_\alpha=\Gamma(\alpha)\sin(\pi\alpha/2)/\pi$, $\beta=\alpha/2$, and $\pi_1=\Pr\{(XU)_1>0,(XU)_2<0\}\in(0,1/2)$, the independent masses $P_1,P_2$, also independent of $(F,C)$, obey

\[
\mathbb E e^{-sP_j}=\exp[-\pi_j c_\alpha\Gamma(1-\beta)s^\beta],\quad
\pi_2=\Pr\{(XU)_2>0\}=1/2. \tag{6}
\]

Here $P_1,P_2\in(0,\infty)$ almost surely. The two thinning classes in (3) are disjoint, which proves their independence; no independence of $F$ and $C$ is needed for (5).

## Finite certificates and persistence without a residual-ratio assumption

Freeze $R=(p,q)$ with $0<p<aq$. The strict-grid classifier in `NEGATIVE_RHO_NEXT.md` gives a finite, generic terminal certificate for each atom: $\chi_1=1$ ends at strict single-1, $\chi_2=1$ ends at strict single-2, and every other atom ends at strict dead. For $z>0$, a row initially single-1 stays there; a row initially single-2 stays there; and a $++$ row has increments $\gamma z(p-aq,q-ap)$, so its first coordinate reaches $\le0$ in finitely many steps while its second grows, then it remains single-2. For $z<0$, the proved lower-coordinate barriers and strictly decreasing coordinate sum force finite death despite gate reactivation. Every finite grid threshold equality has zero original-mark probability. The strict outer inequality, finite history and terminal strict signs therefore give a locally stable certificate at each generic marked atom.

Take any joint macro subsequence supplied by `MACRO_COMPACTNESS.md` and couple its limit to the fixed-grid endpoint limits of `BOUNDARY_GRID.md`. The latter can be appended for all finite $K$ by diagonal extraction; the macro theorem already carries the same $(F,C,N)$. Fix a finite marked cutoff $\varepsilon<|z|<M,\|u\|<B$, away from its null boundaries. It contains finitely many matched atoms. Their random maximum certificate index is finite almost surely. First restrict it to $K\le K_0$, transfer the strict certificates with the fixed-$K_0$ boundary-grid theorem, and then let $K_0\uparrow\infty$. This is the only use of frozen-grid convergence; it is never run for $O(L_m)$ steps.

Continuity of the limiting residual and $R>0$ give a small $\delta>0$ on which both limiting residual coordinates remain positive. Uniform actual-residual convergence makes both actual coordinates positive at every grid step through $\delta$, eventually under the joint coupling. Retained $z_{i,n}$ retain their original sign uniformly on fixed horizons by the macro row-displacement bound. Hence after their transferred finite certificate, each live positive-$z$ row stays in its certified **single** gate through $\delta$: in single-1 its increments are $\gamma z_{i,n}r_{m,n,1}(1,-a)$; in single-2 they are $\gamma z_{i,n}r_{m,n,2}(-a,1)$. Positivity of the corresponding residual makes the active coordinate increase and the inactive one decrease. A dead row stays exactly dead. This argument needs no later restriction on the ratio $r_{m,1}/r_{m,2}$.

Now write $J_j(t)=\int_0^t r_j(s)ds$ for the cumulative clocks of the **unselected** macro subsequential residual. On any fixed interval $[0,T]$ on which both $J_j(t)>0$ for every $t\in(0,T]$, the preceding single-gate certificates persist through $T$, even if a residual coordinate becomes negative. To prove this rather than assume it, take a retained live atom and suppose its certified gate fails at a first actual grid time $t_n\in[\delta,T]$. All preceding steps had that gate, so the exact telescoped update, with $d_1=(1,-a)^T,d_2=(-a,1)^T$, is

\[
\frac{v_{i,n}}{L_m}
=\frac{v_{i,K}}{L_m}
+d_j\frac{\gamma}{L_m}\sum_{\ell=K}^{n-1}z_{i,\ell}r_{m,\ell,j}
=z d_jJ_j(t_n)+o(1) \tag{7}
\]

uniformly up to $T$, as long as the gate has not failed. Here $K$ is its finite certificate index; its state is $O(1)$, the initial mark is bounded on the cutoff, and $z_{i,\ell}\to z$ uniformly by the macro row bound. On $[\delta,T]$, $\min J_j>0$. Because $z>0$, (7) places the first coordinate of a single-1 row strictly positive and its second strictly negative, or the corresponding opposite signs for a single-2 row, at the purported first failure. This is a contradiction. The first-failure test is at a **pre-step state**, so it respects the strict zero-gate convention. This proves persistent actual-grid gates per retained atom from cumulative positivity, without circular use of the candidate residual or a uniform margin across the Poisson population.

It follows from (7), on every positive time, that the subsequential endpoints have the forms in (5) with $I^0$ replaced by $J$, and dead atoms have zero endpoint. The exact macro output decomposition, finite-cutoff convergence, and its uniform small-$|z|$ square-mass bound remove the cutoff. The output sum is absolutely uniform because $\int z^2N<\infty$, and for $J_j>0$ its two contributions are exactly $P_1e_1J_1+P_2e_2J_2$. Thus the actual-GD subsequential residual satisfies

\[
r(t)=R-CJ(t)-\operatorname{diag}(P_1,P_2)J(t)=R-QJ(t). \tag{8}
\]

This is an identification of **output increments**. It neither replaces a ReLU secant by a pre-step tangent Gram nor asserts convergence of the latter.

Define $\sigma=\inf\{t>0:J_1(t)J_2(t)=0\}$, taking infinity if the set is empty. Since $r(0)=R>0$, both $J_j$ are strictly positive for small positive time. Apply the preceding argument on every rational compact interval below $\sigma$, then take their countable union. Equation (8) and $J'=r$ give $r=e^{-Qt}R=r^0$, $J=I^0$, until $\sigma$. Continuity forces $\sigma=\tau$: if one were earlier, its clock would contradict strict positivity of the other trajectory; if one were later, it would pass through the other's zero. When $\tau=\infty$, this identifies every fixed horizon. At finite $\tau$, uniform Lipschitz bounds and endpoint continuity extend (5) and $r=r^0$ to the stopping time from the left. Since every macro subsequence has the same identified stopped limit, the corresponding joint convergence in law follows.

## Return geometry and a realizable strict example

The matrix $C$ is positive definite and $C_{12}\ge0$ because it is a sum of nonnegative ReLU-ray outer products. Hence $Q\succ0$, $Q_{12}=c\ge0$. If $c=0$, both clocks stay positive forever. If $c>0$, a residual coordinate can cross from positive to negative only while the other is positive: at $r_1=0<r_2$, $r'_1=-cr_2<0$, and likewise with coordinates exchanged. The resulting mixed sign cone is forward invariant (at its two axes the vector field points inward). Thus at most one residual coordinate crosses, the other stays positive, and the crossed coordinate stays negative. Its clock first increases and then decreases. Consequently a finite cumulative return occurs exactly when one component of $Q^{-1}R=I^0(\infty)$ is negative. Both components cannot be negative, since $Q^{-1}R<0$ componentwise would require $Q_{11}Q_{22}<c^2$, contrary to positive definiteness. Equality gives only asymptotic approach to zero. At finite $\tau$ the returning clock is transverse: $I_j^0(\tau)=0$, $r_j^0(\tau)<0$, while $I_k^0(\tau)>0$, $r_k^0(\tau)>0$.

This return has positive probability in the stipulated model. Take $a=1/2$,

\[
x_1=(1/2,-\sqrt3/2),\quad x_2=(1/2,\sqrt3/2),\quad
C=\begin{pmatrix}2&1\\1&3\end{pmatrix},\quad
P_1=P_2=1,\quad R=(1,10). \tag{9}
\]

The input Gram has correlation $-1/2$, and $R_1<aR_2$. The three nonzero signed-coordinate ReLU rays are common $(1/2,1/2)$, first-only $(\sqrt3/2,0)$, and second-only $(0,\sqrt3/2)$; their square masses $4,4/3,8/3$ give exactly the displayed $C$. Then

\[
Q=\begin{pmatrix}3&1\\1&4\end{pmatrix},\qquad
Q^{-1}R=(-6/11,29/11), \tag{10}
\]

so the first clock returns at a finite positive time, after a residual-axis crossing. The independent positive-stable ray masses and the independently thinned $P_1,P_2$ have full support on $(0,\infty)$, and the primitive $R$ has full support; the strict inequalities in (2) and (10) persist in a neighborhood. Thus a neighborhood of (9), not the exact point, has positive probability. This upgrades the earlier algebraic candidate to a realized **stopped actual-network** example, without saying anything about the phase at or after the return.

## Concrete finite-width stopping and finite test outputs

For an entirely finite-width stopping rule, form the original-mark masses

\[
P_{1,m}=A_m^{-2}\sum_i W_{i,0}^{2}\mathbf1_{\{W_{i,0}>0,v_{i,0,1}>0,v_{i,0,2}\le0\}},\quad
P_{2,m}=A_m^{-2}\sum_i W_{i,0}^{2}\mathbf1_{\{W_{i,0}>0,v_{i,0,2}>0\}}. \tag{11}
\]

Set $Q_m=C_{m,0}+\operatorname{diag}(P_{1,m},P_{2,m})$, $R_m=y-f_{m,0}$, and let $\tau_m^0$ be the first positive return to zero of a component of $\int_0^t e^{-Q_ms}R_mds$ (infinity if none), on the finite-width strict event corresponding to (2). The marked-PPP convergence, null selector boundaries and the same small-square-mass estimate give joint $P_{j,m}\Rightarrow P_j$ with $(F,C,N)$. The candidate return map is continuous at every strict finite transversal return and on each compact horizon with no return; $\Pr(\tau=T\mid E)=0$ for a fixed $T>0$, since conditional on $Q$ the equation $I_j^0(T)=0$ is a proper linear hyperplane in the continuously distributed $R$. Hence $\tau_m^0\to\tau$ under joint subsequence representation, locally in the extended-time topology. The uniform actual-output Lipschitz bound in `MACRO_COMPACTNESS.md` fills the vanishing interval between $\tau-\epsilon$ and $\tau_m^0$. In particular, for each fixed $T$, the polygonal **actual** residual stopped at $\tau_m^0$ converges jointly to $r^0(t\wedge\tau)$ on $[0,T]$, conditional on (2); the same is true for the training output. Stopping at the candidate clock is only a reporting device, not an assertion that every finite-width gate fails at that exact time.

For any fixed finite deterministic test matrix $Z\in\mathbb R^{q\times d}$, the rank-free stacked signed-ray initialization gives correlated $F_*\in\mathbb R^q$ and rectangular $C_*\in\mathbb R^{q\times2}$ as in `../20261024T032106Z/TEST_PREDICTIONS.md`. Its projection identity and integration-by-parts/cutoff proof use no sign of $\rho$, so along this stopped branch the actual test outputs converge jointly to

\[
f_*(t)=F_*+C_*I^0(t)
+P_1 I^0_1(t)(Zx_1)_+
+P_2 I^0_2(t)(Zx_2)_+,\qquad 0\le t\le\tau. \tag{12}
\]

Indeed $K=ZX^TG^{-1}$, $Kd_j=Zx_j$, and the retained endpoint contribution is $z(Kq_{z,u})_+=z^2I_j^0(Zx_j)_+$ while $I_j^0>0$. The exact rectangular cross-time Gram freeze supplies $C_*I^0$; the test small-$|z|$ bound is the same square-mass bound with $\|Z\|\|X\|$ in place of $\|G\|$. Equation (12) also holds at $\tau$ by continuity and with the finite-width candidate stopping $\tau_m^0$. Setting $Z=X$ recovers $F+CI^0+\operatorname{diag}(P_1,P_2)I^0=y-r^0$.

At $\tau<\infty$, the returning selected population has $q_{z,u}(\tau)=0$ after division by $L_m$, whereas its unscaled original-mark offset and fractional last-step overshoot can select distinct subsequent gates. Equation (12) and the training stopped law deliberately make **no** post-return claim, no moving-return phase law and no threshold-null assertion.
