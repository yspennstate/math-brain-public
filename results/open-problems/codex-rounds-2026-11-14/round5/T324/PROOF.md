# Two narrow groups with independent token noise

Let \(A,B\) partition \(N=n_A+n_B\) tokens, with \(n_A,n_B\geq1\). All token weights are \(1/N\). Write \(p=n_A/N\), \(q=n_B/N\). The normalized identity-matrix attention dynamics on a real lift of the circle is

\[
 d\theta_i=V_{\mu_t}(\theta_i)\,dt+\sqrt{2\nu}\,dW_i,\qquad
 \mu_t=N^{-1}\sum_{j=1}^N\delta_{\theta_j(t)},                       \tag{1}
\]

where the \(W_i\) are independent standard Brownian motions, \(\nu>0\), and

\[
 V_\mu(\theta)=\frac{\int e^{\beta\cos(\phi-\theta)}
                 \sin(\phi-\theta)\,d\mu(\phi)}
                 {Z_\mu(\theta)},\qquad
 Z_\mu(\theta)=\int e^{\beta\cos(\phi-\theta)}\,d\mu(\phi).          \tag{2}
\]

Self-attention is included. For fixed \(\beta\), the drift of the finite system is smooth, periodic and globally Lipschitz, since its denominators are bounded below by \(e^{-\beta}\). Thus (1) has a global strong solution with continuous real lifts.

Define the labelled arithmetic means, their gap, and the maximum group diameter by

\[
 a=\frac1{n_A}\sum_{i\in A}\theta_i,\quad
 b=\frac1{n_B}\sum_{i\in B}\theta_i,\quad S=b-a,\quad
 W=\max\{\max_A\theta_i-\min_A\theta_i,
          \max_B\theta_i-\min_B\theta_i\}.                       \tag{3}
\]

Fix \(0<\delta<x<\pi\), with \(S(0)=x\), and put

\[
 \tau_\delta=\inf\{t\geq0:S(t)\leq\delta\},\qquad A_x=1-\cos x.
\]

The stopping event uses the lifted means. The asymptotic estimates below ensure, with probability tending to one, that the groups remain ordered in an arc shorter than \(\pi\) before this event. No permanent-merging assertion is made.

## 1. Statements

The exact two-atom inward drift at masses \(p,q\) is

\[
 h_\beta(s)=\sin s\left\{\frac{q}{p e^{\beta(1-\cos s)}+q}
                       +\frac{p}{q e^{\beta(1-\cos s)}+p}\right\},
 \quad 0<s<\pi.                                                 \tag{4}
\]

### Stopped concentration and center equation

Choose \(x<L<\pi\), \(\beta\geq1\), and \(0<\bar w\leq1\), with

\[
 \beta\bar w^2\leq\tfrac18,\qquad
 \delta-2\bar w\geq\delta/2,\qquad L+2\bar w<\pi.
\]

Let

\[
 R_*=\max(p/q,q/p),\qquad
 \epsilon_\beta=R_*e^{-\beta(\cos\bar w-\cos(\delta/2))},
\]

and assume the explicit sufficient condition

\[
 -1+(\beta+\tfrac12)\bar w^2+(\beta+2)\epsilon_\beta
 \leq-\tfrac12.                                                 \tag{5}
\]

Let \(W(0)\leq w_0<\bar w\), and define

\[
 \sigma=\inf\{t\geq0:S(t)\notin(\delta,L)\text{ or }W(t)\geq\bar w\},
 \quad M=\binom{n_A}{2}+\binom{n_B}{2},\quad
 K=2+\frac2{1-e^{-1/2}}.                                        \tag{6}
\]

For \(T>0\) and \(u>0\) satisfying \(w_0+Ku<\bar w\),

\[
 \mathbb P\left\{\exists t\leq T\wedge\sigma:
    W(t)>w_0e^{-t/2}+Ku\right\}
 \leq4M\lceil T\rceil\exp\left(-\frac{u^2}{8\nu}\right).           \tag{7}
\]

On the event supplied by this estimate, exit through \(W=\bar w\) before time \(T\) is impossible. If \(M=0\), both groups are singletons and their diameters vanish identically.

There is a standard Brownian motion \(B^c\), defined in Section 4, such that the exact center-gap equation is

\[
 dS=(-h_\beta(S)+\mathcal R_t)\,dt
        +\sqrt{2\nu\chi}\,dB^c_t,\qquad
 \chi=\frac1{n_A}+\frac1{n_B}.                                  \tag{8}
\]

For \(t<\sigma\) with \(\beta W(t)\leq1\),

\[
 |\mathcal R_t|\leq C\{\beta W(t)^3
                 +(\beta+1)W(t)h_\beta(S(t))\},                 \tag{9}
\]

where \(C\) depends only on \(p,q,\delta,L\). The coefficient multiplying \(f''(S)\) in Itô's formula is \(\nu\chi\), rather than the two-atom coefficient \(2\nu\) unless \(n_A=n_B=1\). Equation (8) is not a closed scalar Markov equation: its remainder depends on the full configuration.

### Weak-noise merging theorem

Keep \(n_A,n_B,\delta,x\) fixed. Let \(\beta\to\infty\), let \(\nu=\nu_\beta>0\), and suppose

\[
 W(0)\leq w_\beta\leq\frac1{4\sqrt\beta},\qquad
 \liminf_{\beta\to\infty}\frac{-\log\nu_\beta}{\beta}>A_x.         \tag{10}
\]

Then

\[
 \frac{\log\tau_\delta}{\beta}\longrightarrow A_x
 \quad\hbox{in probability}.                                   \tag{11}
\]

If also \(\beta^2w_\beta^3\to0\), then

\[
 \frac{\tau_\delta}
 {e^{\beta A_x}/[(p/q+q/p)\beta\sin^2x]}
 \longrightarrow1\quad\hbox{in probability}.                    \tag{12}
\]

These statements concern two groups already present at time zero. They do not determine their formation, generic cluster count, successive mergers, a mean entrance-time asymptotic, or the regime where the noise exponent is at most \(A_x\).

## 2. Contraction in the stopped tube

For fixed \(\mu\), write \(\mathbb E_\theta\) for expectation under its attention row. Differentiation gives

\[
 V_\mu'(\theta)=-\mathbb E_\theta\cos(\phi-\theta)
        +\beta\operatorname{Var}_\theta(\sin(\phi-\theta)).        \tag{13}
\]

The derivative of \(e^{\beta\cos(\phi-\theta)}\) is \(\beta\sin(\phi-\theta)e^{\beta\cos(\phi-\theta)}\), and the derivative of its sine factor is minus the cosine. The quotient rule subtracts \(\beta(\mathbb E_\theta\sin)^2\), leaving the variance.

At a time before \(\sigma\), write \(w=W(t)\), \(s=S(t)\). A point in either group's convex hull is at distance at most \(w\) from that group's mean. Cross-group distances lie between \(s-2w\) and \(s+2w\), within \([\delta/2,L+2\bar w]\subset(0,\pi)\). In a row evaluated in the A hull, the own-group row mass is at least \(p e^{\beta\cos\bar w}\), and the cross mass is at most \(q e^{\beta\cos(\delta/2)}\). Hence the cross-attention probability is at most \(\epsilon_\beta\). The B estimate interchanges \(p,q\).

Own-group sine magnitudes are at most \(w\), so

\[
 \mathbb E_\theta\cos\geq(1-\epsilon_\beta)\cos w-\epsilon_\beta,
 \qquad \operatorname{Var}_\theta(\sin)\leq w^2+\epsilon_\beta.
\]

Since \(\cos w\geq1-w^2/2\), (13) and (5) imply

\[
 V_\mu'(\theta)\leq-1+(\beta+1/2)\bar w^2
                           +(\beta+2)\epsilon_\beta\leq-1/2.     \tag{14}
\]

For labels \(i,j\) in one group, set \(D_{ij}=\theta_i-\theta_j\), without imposing any order on their positions. The fundamental theorem of calculus gives

\[
 dD_{ij}=c_{ij}(t)D_{ij}\,dt+dM_{ij},\quad
 c_{ij}(t)=\int_0^1 V_{\mu_t}'(\theta_j+vD_{ij})\,dv\leq-1/2,
 \quad M_{ij}=\sqrt{2\nu}(W_i-W_j).                              \tag{15}
\]

The segment in (15) remains in the group's convex hull. Formula (13) also gives \(V'\geq-1\), so these coefficients are bounded. All crossings inside a group are permitted.

## 3. Brownian maxima on unit intervals

Consider \(dD=c_tD\,dt+dM\) on \([k,k+1]\cap[0,\sigma]\), with \(c_t\leq-1/2\). Set \(\Phi(t,v)=\exp(\int_v^t c_z\,dz)\). Variation of constants and integration by parts give

\[
 D(t)=\Phi(t,k)D(k)+(M(t)-M(k))
       +\int_k^t c_v\Phi(t,v)(M(v)-M(k))\,dv.                   \tag{16}
\]

Alternatively subtract \(M(t)-M(k)\) first and solve the resulting ordinary integral equation. Thus (16) does not treat a kernel depending on future coefficients as a martingale integrand. Since \(c_v\leq0\),

\[
 \int_k^t |c_v|\Phi(t,v)\,dv=1-\Phi(t,k)\leq1.
\]

If \(\sup_{0\leq v\leq1}|M(k+v)-M(k)|\leq u\), it follows that

\[
 |D(k+v)|\leq e^{-v/2}|D(k)|+2u                               \tag{17}
\]

up to the stopping time. Iterating at integer endpoints and then within the last block yields

\[
 |D(t)|\leq e^{-t/2}|D(0)|+\frac{2u}{1-e^{-1/2}}+2u.
\]

The endpoint errors form the geometric sum \(2u\sum_{j\geq0}e^{-j/2}\), and the final partial block adds at most \(2u\).

Each \(M_{ij}\) is Brownian motion of variance rate \(4\nu\). Reflection and the Gaussian Chernoff bound give

\[
 \mathbb P\{\sup_{0\leq v\leq1}|M_{ij}(k+v)-M_{ij}(k)|>u\}
 \leq4e^{-u^2/(8\nu)}.                                         \tag{18}
\]

Indeed reflection bounds a one-sided maximum by twice a Gaussian tail, that tail is at most \(e^{-z^2/2}\), and the two sides give the factor 4. A union bound over the \(M\) unordered pairs and \(\lceil T\rceil\) blocks proves (7). Pair noises are correlated; independence is not needed. Continuity at \(\sigma\), together with \(w_0+Ku<\bar w\), excludes width exit on this event.

If \(\nu_\beta\leq e^{-r_0\beta}\), \(u_\beta=e^{-\kappa\beta}\), \(2\kappa<r_0\), and \(T_\beta=e^{H\beta}\), the bound is at most

\[
 4M(e^{H\beta}+1)\exp[-e^{(r_0-2\kappa)\beta}/8].
\]

For fixed \(M,H\), this tends to zero faster than \(e^{-c\beta}\) for every fixed \(c>0\).

## 4. Exact center variance and the drift remainder

Average (1) over each group. Define

\[
 B_A=n_A^{-1/2}\sum_{i\in A}W_i,\qquad
 B_B=n_B^{-1/2}\sum_{i\in B}W_i.
\]

These are independent standard Brownian motions, and

\[
 B^c=\frac{B_B/\sqrt{n_B}-B_A/\sqrt{n_A}}{\sqrt\chi}
\]

is standard Brownian motion in the original filtration. Thus the martingale part of \(S\) has quadratic variation \(2\nu\chi t\), proving (8)'s noise factor. Independently, applying the original noise generator \(\nu\sum_i\partial_{\theta_i}^2\) to \(f(S)\) gives \(\nu\chi f''(S)\). The within-group centered Brownian increments \(dW_i-n_G^{-1}\sum_{j\in G}dW_j\) are orthogonal to \(dB_G\), as follows by taking covariance. The drift remains coupled, so no independence of the nonlinear center and width processes is asserted.

Let \(I_A,I_B\) be the internal contributions to the mean velocities. Use measures of mass \(p,q\), the kernel \(K_{ij}=e^{\beta\cos(\theta_j-\theta_i)}\), and row sums \(Z_i\). Kernel symmetry and sine antisymmetry give exactly

\[
 I_A=\frac1{2p}\iint_{A\times A}K_{ij}\sin(\theta_j-\theta_i)
                      (Z_i^{-1}-Z_j^{-1})\,d\mu_A(i)d\mu_A(j).   \tag{19}
\]

The factor \(1/p\) arises from taking the conditional mean. With token weights \(1/N\), this is precisely \(1/n_A\) times the sum of token velocities. For \(\theta\) in the A hull, put \(d=s-2w>0\). Since all cross distances are below \(\pi\),

\[
 |Z'(\theta)|\leq\beta\{p e^\beta w+q e^{\beta\cos d}\},\qquad
 Z(\theta)\geq p e^{\beta\cos w}.
\]

The mean value theorem for \(1/Z\), followed by (19), gives

\[
 |I_A|\leq\frac\beta2 e^{2\beta(1-\cos w)}w^2
             \{w+(q/p)e^{-\beta(1-\cos d)}\}.
\]

Here the pair mass is \(p^2\), the sine is at most the pair distance, and the reciprocal difference supplies a second pair distance. The powers of \(p\) cancel to the coefficient displayed. Introduce the current-separation cross bound

\[
 \epsilon(s,w)=R_*e^{-\beta(\cos w-\cos(s-2w))}.
\]

Since \(2\beta(1-\cos w)\leq\beta w^2\leq1/8\), adding the B estimate gives

\[
 |I_B-I_A|\leq e^{1/8}\beta\{w^3+\epsilon(s,w)w^2\}.             \tag{20}
\]

The same bound with the coarser \(\epsilon_\beta\) holds throughout the tube. If \(C_A\geq0\) is the cross contribution to \(a'\), and \(-C_B\leq0\) that to \(b'\), both \(C_A,C_B\leq\epsilon_\beta\). Thus the finite-variation part of the gap also obeys

\[
 |\operatorname{drift}(S)|\leq e^{1/8}\beta(w^3+\epsilon_\beta w^2)
                                      +2\epsilon_\beta.         \tag{21}
\]

The signs use only instantaneous tube geometry, not deterministic preservation of token order.

For the sharper comparison put \(m=\min_{[\delta,L]}\sin s>0\). The denominator inequalities \(pE+q\leq E\), \(qE+p\leq E\), for \(E=e^{\beta(1-\cos s)}\geq1\), show

\[
 h_\beta(s)\geq\sin s\,e^{-\beta(1-\cos s)}.                     \tag{22}
\]

When \(\beta w\leq1\),

\[
 \frac{\epsilon(s,w)}{h_\beta(s)}
 \leq\frac{R_*}{m}
 e^{\beta(1-\cos w)+\beta(\cos(s-2w)-\cos s)}
 \leq\frac{R_*}{m}e^{5/2}.                                    \tag{23}
\]

The last step uses \(1-\cos w\leq w^2/2\), the Lipschitz constant 1 of cosine, \(w\leq1\), and \(\beta w\leq1\).

For a row in A, its cross numerator relative to \(q e^{\beta\cos s}\sin s\) lies between \(e^{-2\beta w}(1-2w/m)\) and \(e^{2\beta w}(1+2w/m)\). If \(1-2w/m<0\), the lower bound is simply trivial by positivity. Its full denominator relative to \(p e^\beta+q e^{\beta\cos s}\) lies between \(e^{-2\beta w}\) and \(e^{2\beta w}\). For its internal part this uses \(e^{-\beta w^2/2}\geq e^{-2\beta w}\), and for the cross part it uses \(|\cos(\phi-\theta)-\cos s|\leq2w\). The same estimates hold in B.

It follows that \((C_A+C_B)/h_\beta(s)\) lies between \(e^{-4\beta w}(1-2w/m)\) and \(e^{4\beta w}(1+2w/m)\). For the possibly negative lower factor the claim remains true by positivity. Moreover

\[
 \begin{split}
 e^{4\beta w}(1+2w/m)-1&\leq e^4(4\beta+2/m)w,\\
 1-e^{-4\beta w}(1-2w/m)&\leq(4\beta+2/m)w.
 \end{split}
\]

Therefore

\[
 |C_A+C_B-h_\beta(s)|\leq C_1(\beta+1)w h_\beta(s).              \tag{24}
\]

Finally \(\operatorname{drift}(S)=-(C_A+C_B)+(I_B-I_A)\). Combining (20), (23), (24), and \(w^2\leq w\) proves (9).

## 5. Width and center control on an exponential horizon

Choose \(r_0\) with

\[
 A_x<r_0<\liminf_{\beta\to\infty}(-\log\nu_\beta)/\beta.
\]

Then \(\nu_\beta\leq e^{-r_0\beta}\) for large \(\beta\). Choose fixed \(L\in(x,\pi)\) close enough to \(x\) that \(a_L=1-\cos L<r_0\). Since \(a_L<2\), choose

\[
 \frac{a_L}{3}<\kappa<\min\{r_0/2,1\},\qquad
 A_x<H<r_0,\qquad 0<2\gamma<r_0-H.                             \tag{25}
\]

The interval for \(\kappa\) is nonempty, since \(a_L/3<a_L/2<r_0/2\) and \(a_L/3<2/3<1\). Set

\[
 \bar w_\beta=\frac1{3\sqrt\beta},\quad
 u_\beta=e^{-\kappa\beta},\quad T_\beta^*=e^{H\beta},\quad
 v_\beta=e^{-\gamma\beta},\quad t_0=4\beta.
\]

The tube hypotheses and (5) hold for large \(\beta\). Here \(\beta\bar w_\beta^2=1/9\), and
\[
 \epsilon_\beta\leq R_*e^{1/18}e^{-\beta(1-\cos(\delta/2))}.
\]
Also \(w_\beta+Ku_\beta<\bar w_\beta\).

Let \(\mathcal E_\beta\) be the event that all pair block maxima in Section 3 are at most \(u_\beta\) up to \(T_\beta^*\), and that the full, unstopped center martingale \(M^c(t)=\sqrt{2\nu_\beta\chi}B^c_t\) satisfies

\[
 \sup_{t\leq T_\beta^*}|M^c(t)|\leq v_\beta.
\]

Section 3 bounds the first failure probability. The reflection estimate at time \(T_\beta^*\) bounds the second by

\[
 4\exp\left[-\frac{v_\beta^2}{4\nu_\beta\chi T_\beta^*}\right]
 \leq4\exp\left[-\frac{e^{(r_0-H-2\gamma)\beta}}{4\chi}\right].   \tag{26}
\]

Thus \(\mathbb P(\mathcal E_\beta)\to1\). Independence of the events is unnecessary. On \(\mathcal E_\beta\),

\[
 W(t)\leq w_\beta e^{-t/2}+Ku_\beta
       \quad(t\leq T_\beta^*\wedge\sigma).                       \tag{27}
\]

We first prove \(\sigma>t_0\). Width exit is already excluded. Integrate (21) up to \(t\leq t_0\wedge\sigma\). The inequalities \((a+b)^3\leq4(a^3+b^3)\), \((a+b)^2\leq2(a^2+b^2)\), and (27) give

\[
 |S(t)-x|\leq d_\beta:=v_\beta+C\beta\{
 w_\beta^3+t_0u_\beta^3
 +\epsilon_\beta(w_\beta^2+t_0u_\beta^2)\}
 +2t_0\epsilon_\beta.                                          \tag{28}
\]

The constant is independent of \(\beta\); for example the integrated cubic terms are at most \(8w_\beta^3/3+4K^3t_0u_\beta^3\). Since \(w_\beta\leq1/(4\sqrt\beta)\), \(d_\beta\to0\). A first gap exit through \(\delta\) or \(L\) before \(t_0\) would contradict (28), since their distances from \(x\) are fixed and positive. Put \(S_0=S(t_0)\). Then

\[
 |S_0-x|\leq d_\beta=o(1),
\]

and \(\beta d_\beta\to0\) if \(\beta^2w_\beta^3\to0\).

For \(t\geq t_0\), (27) and \(\kappa<1<2\) give

\[
 W(t)\leq d_\beta^w:=(K+1)e^{-\kappa\beta}
       \quad(t\leq T_\beta^*\wedge\sigma).                       \tag{29}
\]

In particular \(\beta W\leq1\). On \([\delta,L]\), (22) gives \(h_\beta\geq m e^{-\beta a_L}\). Dividing (9) by this bound yields

\[
 |\mathcal R_t|\leq\eta_\beta h_\beta(S(t)),\qquad
 \eta_\beta=C\{(\beta+1)d_\beta^w
          +\beta(d_\beta^w)^3e^{\beta a_L}/m\}\longrightarrow0.   \tag{30}
\]

The last convergence uses \(3\kappa>a_L\). This controls the drift pointwise on the whole stopped horizon.

## 6. A pathwise hitting-time sandwich

Work on \(\mathcal E_\beta\). Subtract the center noise after \(t_0\):

\[
 Y(t)=S(t)-[M^c(t)-M^c(t_0)].
\]

Then \(Y\) is absolutely continuous and \(Y(t_0)=S_0\). Put \(b_\beta=2v_\beta\), so \(|Y-S|\leq b_\beta\) throughout the horizon.

For a summand \(f(s)=q/(p e^{\beta(1-\cos s)}+q)\) in (4),

\[
 \frac{f'(s)}{f(s)}=-\beta\sin s\,
       \frac{p e^{\beta(1-\cos s)}}{p e^{\beta(1-\cos s)}+q}.
\]

The logarithmic derivative of the sum of the two positive summands is their weighted average. Hence on a fixed compact subinterval of \((0,\pi)\),

\[
 |(\log h_\beta)'|\leq\beta+C_2.                               \tag{31}
\]

For large \(\beta\), both \(Y,S\) lie in \([\delta/2,(L+\pi)/2]\) as long as the tube conditions hold. Equations (30), (31), and \(\beta b_\beta\to0\) give a deterministic \(\zeta_\beta\to0\) such that, almost everywhere after \(t_0\) on this stopped interval,

\[
 -(1+\zeta_\beta)h_\beta(Y(t))\leq Y'(t)
                 \leq-(1-\zeta_\beta)h_\beta(Y(t)).              \tag{32}
\]

Choose \(1+\zeta_\beta\) at least \((1+\eta_\beta)e^{(\beta+C_2)b_\beta}\) and \(1-\zeta_\beta\) at most \((1-\eta_\beta)e^{-(\beta+C_2)b_\beta}\). For large \(\beta\), \(\zeta_\beta<1/2\). In particular \(Y\) decreases strictly. Therefore \(S(t)\leq S_0+b_\beta<L\), so upper gap exit is impossible. Together with the width estimate, the only remaining tube exit before the horizon is the desired event \(S=\delta\).

For \(z>d>0\), define

\[
 Q_\beta(z,d)=\int_d^z\frac{ds}{h_\beta(s)}.
\]

If \(\tau_\delta\leq T_\beta^*\), continuity gives \(|Y(\tau_\delta)-\delta|\leq b_\beta\). Integrating (32) yields

\[
 t_0+\frac{Q_\beta(S_0,\delta+b_\beta)}{1+\zeta_\beta}
 \leq\tau_\delta\leq
 t_0+\frac{Q_\beta(S_0,\delta-b_\beta)}{1-\zeta_\beta}.            \tag{33}
\]

To remove the assumed hitting within the horizon, suppose it did not occur. Then \(Y(T_\beta^*)>\delta-b_\beta\). Integration of the upper inequality in (32) would give

\[
 T_\beta^*-t_0\leq
 \frac{Q_\beta(S_0,\delta-b_\beta)}{1-\zeta_\beta}.                \tag{34}
\]

Section 7 shows that the right side has logarithmic rate \(A_x<H\), contradicting (34) for large \(\beta\). Thus hitting occurs within the horizon on \(\mathcal E_\beta\), and (33) holds there.

## 7. Scalar asymptotics and endpoint sensitivity

Put \(C_*=p/q+q/p\) and \(E=e^{\beta(1-\cos s)}\). Addition of the coefficients in (4) and polynomial division give

\[
 \frac{h_\beta(s)}{\sin s}=\frac{C_*E+2}{E^2+C_*E+1},\qquad
 \frac{E^2+C_*E+1}{C_*E+2}
 =\frac E{C_*}+1-\frac2{C_*^2}
              -\frac{1-4/C_*^2}{C_*E+2}.                        \tag{35}
\]

For fixed \(0<d<z<\pi\), this implies

\[
 Q_\beta(z,d)=\frac1{C_*}\int_d^z
                    \frac{e^{\beta(1-\cos s)}}{\sin s}\,ds+O(1).
\]

To evaluate the integral, substitute \(v=1-\cos s\). Then \(dv=\sin s\,ds\), \(\sin^2s=v(2-v)\). Setting \(r=\beta(1-\cos z-v)\), its ratio to \(e^{\beta(1-\cos z)}/\beta\) becomes

\[
 \int_0^{\beta(\cos d-\cos z)}
 \frac{e^{-r}\,dr}
 {(1-\cos z-r/\beta)(1+\cos z+r/\beta)}
 \longrightarrow\frac1{\sin^2z}.                               \tag{36}
\]

Before the last substitution, \(v\) ranges in a fixed compact subinterval of \((0,2)\), on which \(1/[v(2-v)]\) is bounded. Extend the transformed integrand by zero beyond its integration interval. Dominated convergence proves (36). Therefore

\[
 Q_\beta(z,d)\sim
     \frac{e^{\beta(1-\cos z)}}{C_*\beta\sin^2z}.                 \tag{37}
\]

For \(S_0=x+o(1)\), compare \(Q_\beta(S_0,\delta\pm b_\beta)\) between fixed-endpoint integrals with upper limits \(x\pm\varepsilon\) and lower limits \(\delta\pm\varepsilon\), for fixed small \(\varepsilon>0\). Monotonicity and (37), followed by \(\varepsilon\downarrow0\), show that both have logarithmic rate \(A_x\). This is uniform over the deterministic bound (28), and supplies the contradiction in (34). Equation (33), with \(t_0=4\beta\), proves (11) on events of probability tending to one.

For the prefactor, (28) gives \(\beta|S_0-x|\to0\). From (35), on a fixed neighborhood of \(x\),

\[
 |Q_\beta(S_0,\delta)-Q_\beta(x,\delta)|
 \leq C|S_0-x|e^{\beta(A_x+|S_0-x|)}.
\]

Relative to (37) at \(x\), this is at most \(C\beta|S_0-x|e^{\beta|S_0-x|}\to0\). Changing the lower endpoint by \(b_\beta\) costs at most

\[
 C b_\beta e^{\beta(1-\cos\delta+b_\beta)}.
\]

Its ratio to (37) tends to zero, since \(1-\cos\delta<A_x\) and \(b_\beta\to0\). Both integrals in (33) are asymptotic to \(e^{\beta A_x}/(C_*\beta\sin^2x)\). The polynomial \(t_0\) and the factors \(1\pm\zeta_\beta\) do not change that asymptotic. Since \(\mathbb P(\mathcal E_\beta)\to1\), (12) follows.

## 8. Checks on the scope

For singleton groups \(\chi=2\), recovering the gap variance rate \(4\nu\). For groups each of size \(n\), \(\chi=2/n\), giving rate \(4\nu/n\). Treating each group as one independently noisy atom with variance rate \(2\nu\) would miss this factor. Independent within-group noise also makes initially coincident tokens separate, which is why (7) replaces a deterministic diameter inequality.

Condition (10) leaves a positive exponential margin. At equality, the choice \(A_x<H<r_0\) is unavailable, and no claim is made. In the noise-dominated regime, width concentration alone does not control accumulated internal center drift or outward center excursions on the mean entrance-time scale. Even in the weak-noise regime, convergence in probability does not imply a mean-time asymptotic: rare trajectories are not bounded by (33) outside \(\mathcal E_\beta\).

The explicit finite-time bound displays its token-count factor, but the merging theorem keeps the group sizes fixed and does not assert a simultaneous \(N\to\infty\) limit. The assumptions exclude antipodal centers and exact collision.

## 9. An independent width-exit estimate

There is a second proof of exponential suppression of width exits, without the block decomposition. Under the stopped concentration theorem's hypotheses, let \(D\) be any within-group difference and set

\[
 F(D)=e^{D^2/(16\nu)}.
\]

Equation (15) and Itô's formula give the drift bound

\[
 \operatorname{drift}(F(D))
 =\left[\frac14+\left(\frac{c_t}{8}+\frac1{32}\right)
                        \frac{D^2}{\nu}\right]F(D)
 \leq\left(\frac14-\frac{D^2}{32\nu}\right)e^{D^2/(16\nu)}
 \leq\frac14.                                                   \tag{38}
\]

For the last inequality, the derivative of
\(g(z)=(1/4-z/32)e^{z/16}\), for \(z\geq0\), is
\(g'(z)=(-1/64-z/512)e^{z/16}<0\). Thus \(g(z)\leq g(0)=1/4\).
Stop at \(T\wedge\sigma\). The stopped stochastic integral has mean zero, since \(D\) is bounded by \(\bar w\) on this interval. Consequently

\[
 \mathbb E F(D(T\wedge\sigma))
       \leq e^{w_0^2/(16\nu)}+T/4.
\]

On an exit through the width boundary, at least one unordered within-group pair has magnitude exactly \(\bar w\). Applying the preceding estimate to each pair and taking a union bound gives

\[
 \mathbb P\{\sigma\leq T,\ W(\sigma)=\bar w\}
 \leq M\left\{
 e^{-(\bar w^2-w_0^2)/(16\nu)}
       +\frac T4e^{-\bar w^2/(16\nu)}\right\}.                   \tag{39}
\]

This includes simultaneous width and gap exits. The estimate does not give the transient envelope in (7), but independently confirms its long-horizon concentration scale and the role of the pair variance rate \(4\nu\).
