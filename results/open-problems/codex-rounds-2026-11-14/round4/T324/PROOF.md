# Two groups of nonzero width

Consider normalized self-attention on the circle, with identity query, key and value matrices and with self-attention included. In real angular coordinates its velocity is

\[
 V_\mu(\theta)=\frac{\int e^{\beta\cos(\phi-\theta)}\sin(\phi-\theta)\,d\mu(\phi)}
 {Z_\mu(\theta)},\qquad
 Z_\mu(\theta)=\int e^{\beta\cos(\phi-\theta)}\,d\mu(\phi).             \tag{1}
\]

The measure is transported by \(\dot\theta=V_{\mu_t}(\theta)\). Weighted finite token systems are included: take \(\mu_t=\sum_i m_i\delta_{\theta_i(t)}\), with positive weights summing to one. All assertions below are deterministic.

Fix

\[
 p,q>0,\quad p+q=1,\quad 0<\delta<x<\pi.
\]

For each beta, decompose the initial measure into two labelled measures
\(\mu_0=\mu_{A,0}+\mu_{B,0}\), of masses p and q. Their supports lie in disjoint ordered compact intervals on a real lift of the circle, with group A to the left of group B. Transport each label by the common velocity (1). Write

\[
 a(t)=p^{-1}\int\theta\,d\mu_{A,t},\quad
 b(t)=q^{-1}\int\theta\,d\mu_{B,t},\quad s(t)=b(t)-a(t),
\]

and let \(W_A(t),W_B(t)\) be the diameters of their lifted supports. Suppose

\[
 s(0)=x,\qquad W_A(0),W_B(0)\le w_\beta\le\frac1{4\sqrt\beta}.
                                                                    \tag{2}
\]

Let \(\tau_\beta=\inf\{t\ge0:s(t)\le\delta\}\). Constants in the proof may depend on p,q,delta,x, but not on the number of tokens, their individual weights, or the distributions inside the groups.

## Theorem

For all sufficiently large beta, \(\tau_\beta<\infty\), and

\[
 W_A(t),W_B(t)\le w_\beta e^{-t/2}
 \quad(0\le t\le\tau_\beta).                                      \tag{3}
\]

The first group-center merging time satisfies

\[
 \lim_{\beta\to\infty}\frac{\log\tau_\beta}{\beta}=1-\cos x.          \tag{4}
\]

If, in addition,

\[
 \beta^2 w_\beta^3\longrightarrow0,                               \tag{5}
\]

then the full two-atom prefactor is preserved:

\[
 \tau_\beta\sim
 \frac{\exp\{\beta(1-\cos x)\}}
 {(p/q+q/p)\,\beta\sin^2x}.                                      \tag{6}
\]

Condition (5) holds, for example, for \(w_\beta=O(\beta^{-1})\), or more generally for \(w_\beta=o(\beta^{-2/3})\). The theorem concerns two groups already present at time zero. It does not determine their formation from uniform initialization or the number of groups.

## 1. Characteristics and interval geometry

The equations have global characteristic solutions. For completeness, on the compact initial support K write a configuration as a continuous map \(\Theta:K\to\mathbb R\), and integrate (1) against the fixed initial measure using \(\phi=\Theta(z)\), \(\theta=\Theta(y)\). The denominator is at least \(e^{-\beta}\). The first derivatives of numerator and denominator are bounded for fixed beta, so this defines a Lipschitz map on \(C(K)\) in the supremum norm. Picard's theorem gives a unique solution, and \(|V|\le1\) prevents finite-time escape. Atoms give the ordinary finite system. The same argument applies separately to the two labelled restrictions of the initial measure.

Initially the total support span is at most

\[
 L_\beta=x+2w_\beta<\pi.                                         \tag{7}
\]

An interval of length less than pi containing all tokens is invariant: its left endpoint has nonnegative velocity because all angular differences lie in \([0,\pi)\), and its right endpoint has nonpositive velocity. This endpoint statement also holds for compact supports, using the upper and lower Dini derivatives of their extrema. Thus the original containing interval remains invariant. In particular all pairwise lifted distances stay at most \(L_\beta\). Since the velocity is spatially Lipschitz, characteristics preserve their order (the difference of two characteristics is bounded below by its initial difference times a positive exponential on every finite interval). The two labels therefore stay ordered.

Work until \(s=\delta\), and temporarily assume both diameters are at most \(w_\beta\). Any point of a group lies within its diameter of that group's mean. Thus, for theta in either group's convex hull and phi in the other group,

\[
 \delta-2w_\beta\le |\phi-\theta|\le L_\beta.
\]

For sufficiently large beta the lower bound exceeds \(\delta/2\). Set

\[
 R=\max\{p/q,q/p\},\qquad
 \varepsilon_\beta
 =R\exp\{-\beta(\cos w_\beta-\cos(\delta/2))\}.                    \tag{8}
\]

For theta in the A hull, its own-group contribution to Z is at least \(p e^{\beta\cos w_\beta}\); the other contribution is at most \(q e^{\beta\cos(\delta/2)}\). The cross-attention probability is consequently at most epsilon_beta. The same bound holds in B. Since

\[
 \beta(1-\cos w_\beta)\le\tfrac12\beta w_\beta^2\le1/32,
\]

we have

\[
 \varepsilon_\beta\le R e^{1/32}e^{-\beta(1-\cos(\delta/2))}.        \tag{9}
\]

In particular \(\beta^k\varepsilon_\beta\to0\) for every fixed k.

## 2. Contraction inside each group

Let \(\mathbb E_\theta\) denote expectation under the attention probability proportional to \(e^{\beta\cos(\phi-\theta)}d\mu_t(\phi)\). Differentiating numerator and denominator in (1), while holding \(\mu_t\) fixed, gives the exact identity

\[
 \partial_\theta V_{\mu_t}(\theta)
 =-\mathbb E_\theta\cos(\phi-\theta)
   +\beta\operatorname{Var}_\theta(\sin(\phi-\theta)).              \tag{10}
\]

Indeed \(\partial_\theta e^{\beta\cos(\phi-\theta)}
=\beta\sin(\phi-\theta)e^{\beta\cos(\phi-\theta)}\), and the derivative of the sine is minus the cosine. On the own-group hull, own-group angular distances are at most \(w=w(t)=\max(W_A(t),W_B(t))\). The cross-attention bound gives

\[
 \mathbb E_\theta\cos(\phi-\theta)
 \ge (1-\varepsilon_\beta)\cos w-\varepsilon_\beta,
 \qquad
 \operatorname{Var}_\theta(\sin(\phi-\theta))
 \le w^2+\varepsilon_\beta.
\]

For large beta, \(\cos w>0\). Substitution in (10) yields

\[
 \partial_\theta V_{\mu_t}(\theta)
 \le-1+(\beta+1/2)w^2+(\beta+2)\varepsilon_\beta\le-1/2.           \tag{11}
\]

The last inequality follows from \(\beta w_\beta^2\le1/16\) and (9). The mean value theorem applied between the two extremes of a group now gives \(D^+W_A\le-W_A/2\), and the same for B. Equivalently, apply (11) to any pair in the same group and take the supremum. No diameter can cross upward through its initial bound. A first-exit argument therefore removes the temporary diameter assumption and proves (3) throughout the interval before \(s=\delta\). If \(w_\beta=0\), coincidence is invariant and the rest of the argument is the exact two-atom calculation.

## 3. Internal motion of a group mean

The attention velocity splits into an internal and a cross contribution. Let \(I_A\) be the contribution of internal A interactions to \(a'\). At a fixed time write \(Z_i=Z_{\mu_t}(\theta_i)\) and \(K_{ij}=e^{\beta\cos(\theta_j-\theta_i)}\); integral notation with i,j as variables includes atomic measures. Symmetry of K and antisymmetry of the sine give

\[
 I_A=\frac1{2p}\iint_{A\times A}K_{ij}\sin(\theta_j-\theta_i)
             (Z_i^{-1}-Z_j^{-1})\,d\mu_A(i)d\mu_A(j).             \tag{12}
\]

This cancellation is needed to control the initial displacement of the group centers.

For theta in the A hull, differentiation under the integral and the separation bounds imply

\[
 |Z'(\theta)|\le\beta\{p e^\beta w+q e^{\beta\cos(\delta/2)}\},
 \qquad Z(\theta)\ge p e^{\beta\cos w}.
\]

Thus

\[
 |Z_i^{-1}-Z_j^{-1}|
 \le\frac{\beta\{p e^\beta w+q e^{\beta\cos(\delta/2)}\}}
 {p^2 e^{2\beta\cos w}}\,|\theta_i-\theta_j|.
\]

Use \(K_{ij}\le e^\beta\), \(|\sin(\theta_j-\theta_i)|\le|\theta_j-\theta_i|\le w\), and total pair mass \(p^2\) in (12). The result is

\[
 |I_A|\le\frac\beta2 e^{2\beta(1-\cos w)}w^2
       \{w+(q/p)e^{-\beta(1-\cos(\delta/2))}\}.
\]

Since \(2\beta(1-\cos w)\le\beta w^2\le1/16\), and since the second summand in braces is at most epsilon_beta, the same calculation for B proves

\[
 |I_B-I_A|\le C_0\beta(w^3+\varepsilon_\beta w^2),
 \qquad C_0=e^{1/16}.                                          \tag{13}
\]

These estimates do not require equal weights within either group.

Each cross contribution to a group mean has absolute value at most epsilon_beta. Hence

\[
 |s'|\le C_0\beta(w^3+\varepsilon_\beta w^2)+2\varepsilon_\beta.
                                                                    \tag{14}
\]

Integrate (14), using (3). For any \(t\le\tau_\beta\),

\[
 |s(t)-x|\le C_0\beta\{\tfrac23 w_\beta^3
                   +\varepsilon_\beta w_\beta^2\}
                    +2t\varepsilon_\beta.                       \tag{15}
\]

Take \(t_0=4\beta\). The right side of (15) tends to zero uniformly for \(t\le t_0\), since \(\beta w_\beta^3=O(\beta^{-1/2})\). If \(\tau_\beta\le t_0\), (15) at that time would contradict \(s(\tau_\beta)=\delta<x\) for large beta. Thus \(\tau_\beta>t_0\), and

\[
 s_0:=s(t_0)=x+O(\beta w_\beta^3+\beta\varepsilon_\beta),\qquad
 w(t_0)\le w_\beta e^{-2\beta}.                                 \tag{16}
\]

Under (5), (16) also gives \(\beta|s_0-x|\to0\).

## 4. Reduction after the initial contraction

Define the exact two-atom inward gap drift

\[
 h_\beta(s)=\sin s\left\{\frac{q}{p e^{\beta(1-\cos s)}+q}
                       +\frac{p}{q e^{\beta(1-\cos s)}+p}\right\}.
                                                                    \tag{17}
\]

Choose \(L_*=(x+\pi)/2<\pi\). For large beta, (7) implies \(s(t)\le L_\beta\le L_*\). Set

\[
 m=\min_{[\delta,L_*]}\sin s>0.
\]

For \(s\in[\delta,L_*]\), (17) gives a useful uniform lower bound

\[
 h_\beta(s)\ge \sin s\,e^{-\beta(1-\cos s)}\ge m e^{-2\beta}.       \tag{18}
\]

To see the first inequality, put \(E=e^{\beta(1-\cos s)}\ge1\). Then \(pE+q\le E\) and \(qE+p\le E\), so the two coefficients in braces sum to at least \((p+q)/E=1/E\).

Let \(C_A\ge0\) be the cross contribution to \(a'\), and \(C_B\ge0\) the magnitude of the cross contribution to \(b'\). Both signs follow because the groups are ordered in a common interval of length less than pi. We next compare their sum to h_beta.

For theta in A and phi in B,

\[
 |(\phi-\theta)-s|\le2w,\qquad
 |\cos(\phi-\theta)-\cos s|\le2w,\qquad
 |\sin(\phi-\theta)-\sin s|\le2w.
\]

Consequently the cross numerator at a point of A, divided by
\(q e^{\beta\cos s}\sin s\), lies between
\(e^{-2\beta w}(1-2w/m)\) and \(e^{2\beta w}(1+2w/m)\).
The internal part of its denominator, divided by \(p e^\beta\), lies between \(e^{-\beta w^2/2}\) and 1. Its cross part, divided by \(q e^{\beta\cos s}\), lies between \(e^{-2\beta w}\) and \(e^{2\beta w}\). Since \(w\le1\), the complete denominator divided by \(p e^\beta+q e^{\beta\cos s}\) lies between \(e^{-2\beta w}\) and \(e^{2\beta w}\). The same estimates hold after averaging over A and for B with p,q interchanged. Therefore, whenever \(\beta w\) is sufficiently small,

\[
 |C_A+C_B-h_\beta(s)|\le C_1(\beta+1)w\,h_\beta(s),                \tag{19}
\]

where \(C_1\) depends only on m. This follows explicitly from the two multiplicative bounds \(e^{\pm4\beta w}(1\pm2w/m)\), by the mean value theorem for the exponential on a fixed bounded interval.

Since \(s'=-(C_A+C_B)+(I_B-I_A)\), equations (13), (18), (19), and (3) imply that, for all \(t\in[t_0,\tau_\beta)\),

\[
 |s'+h_\beta(s)|\le\eta_\beta h_\beta(s),\qquad \eta_\beta\to0,    \tag{20}
\]

uniformly over the permitted initial measures. For clarity, one admissible bound is

\[
 \eta_\beta=C_1(\beta+1)w_\beta e^{-2\beta}
 +\frac{C_0}{m}\beta e^{2\beta}
    (w_\beta^3e^{-6\beta}+\varepsilon_\beta w_\beta^2e^{-4\beta}).
                                                                    \tag{21}
\]

Every term tends to zero under (2). For large beta, eta_beta<1/2, so (18),(20) imply \(s'\le-(m/2)e^{-2\beta}<0\). This proves finite hitting, rather than assuming it in the reduction.

Put

\[
 T_\beta(z,\delta)=\int_\delta^z\frac{du}{h_\beta(u)}.
\]

Along the trajectory after t_0, its derivative is \(s'/h_\beta(s)\), which lies between \(-(1+\eta_\beta)\) and \(-(1-\eta_\beta)\). Integrating to first hitting gives the concrete sandwich

\[
 t_0+\frac{T_\beta(s_0,\delta)}{1+\eta_\beta}
 \le\tau_\beta\le
 t_0+\frac{T_\beta(s_0,\delta)}{1-\eta_\beta}.                    \tag{22}
\]

## 5. Scalar asymptotics and sensitivity to the initial center gap

The scalar result needed here can be verified without a reduction theorem. Set \(E=e^{\beta(1-\cos u)}\) and \(C=p/q+q/p\). Adding the two coefficients in (17) and dividing polynomials gives

\[
 \frac{h_\beta(u)}{\sin u}=\frac{CE+2}{E^2+CE+1},\qquad
 \frac{E^2+CE+1}{CE+2}
 =\frac EC+1-\frac2{C^2}-\frac{1-4/C^2}{CE+2}.                   \tag{23}
\]

For fixed masses and fixed \(z\in(\delta,\pi)\), it follows that

\[
 T_\beta(z,\delta)=\frac1C\int_\delta^z
                 \frac{e^{\beta(1-\cos u)}}{\sin u}\,du+O(1).
\]

The bounded error is uniform on compact sets of z in \((\delta,\pi)\). Substitute \(v=1-\cos u\). The exponential integral becomes

\[
 \int_{1-\cos\delta}^{1-\cos z}\frac{e^{\beta v}}{v(2-v)}\,dv
 \sim\frac{e^{\beta(1-\cos z)}}{\beta\sin^2 z}.                  \tag{24}
\]

Indeed, after setting \(r=\beta(1-\cos z-v)\), division by
\(e^{\beta(1-\cos z)}/\beta\) leaves an integrand converging to
\(e^{-r}/\sin^2z\), bounded by a constant times \(e^{-r}\) on the fixed compact v interval. Dominated convergence proves (24).

Since \(s_0\to x\), for every sufficiently small fixed \(d>0\), monotonicity gives

\[
 T_\beta(x-d,\delta)\le T_\beta(s_0,\delta)
                     \le T_\beta(x+d,\delta).
\]

Apply (24), take logarithms, divide by beta, and let \(d\downarrow0\). The result is logarithmic rate \(1-\cos x>0\) for \(T_\beta(s_0,\delta)\). Thus \(t_0=4\beta\) is negligible, and (22) proves (4).

Under (5), set \(d_\beta=|s_0-x|=o(1/\beta)\). On a fixed neighborhood of x, (23) gives

\[
 |T_\beta(s_0,\delta)-T_\beta(x,\delta)|
 \le K d_\beta e^{\beta(1-\cos x+d_\beta)},                      \tag{25}
\]

for a constant K: the reciprocal sine is bounded there and
\(|\cos u-\cos x|\le|u-x|\). Division by (24) at x bounds the relative error in (25) by a constant times
\(\beta d_\beta e^{\beta d_\beta}\to0\). Hence
\(T_\beta(s_0,\delta)\sim T_\beta(x,\delta)\). Equations (22)--(24) give (6).

## 6. Scope

At all times before the stopping threshold, each labelled group has exponentially contracting diameter and the groups stay separated by at least \(\delta-2w_\beta\). This is a concentration estimate over the exponentially long waiting interval, uniform in token count and valid for compactly supported mean-field groups as well as finite weighted systems. The precise event used in the theorem is first entrance of the arithmetic group-center gap into delta.

The hypotheses exclude antipodal groups, exponentially vanishing group masses, wide initial groups, general attention matrices, and independently noisy tokens. Adding independent token noise invalidates the deterministic diameter inequality (3). A noisy extension needs a probability bound for within-group widths on the waiting interval and a derivation of the group-center diffusion; neither is supplied by this theorem.
