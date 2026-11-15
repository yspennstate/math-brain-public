# Merging of two atoms with unequal masses

Let the state space be the unit circle, with identity query, key and value matrices and normalized attention including self-attention. For beta positive, fix

\[
0<\delta<x<\pi,\qquad p_\beta\in(0,1),\qquad q_\beta=1-p_\beta.
\]

The masses are constant in time for each beta. For the measure
\(p_\beta\delta_{v_1}+q_\beta\delta_{v_2}\), the angular equations, with an optional stochastic perturbation, are

\[
\begin{aligned}
d\theta_1&=\frac{q_\beta e^{\beta\cos D}\sin D}
 {p_\beta e^\beta+q_\beta e^{\beta\cos D}}\,dt+\sqrt{2\nu_\beta}\,dW_1,\\
d\theta_2&=-\frac{p_\beta e^{\beta\cos D}\sin D}
 {q_\beta e^\beta+p_\beta e^{\beta\cos D}}\,dt+\sqrt{2\nu_\beta}\,dW_2,
\qquad D=\theta_2-\theta_1.
\end{aligned}                                                    \tag{1}
\]

Here \(W_1,W_2\) are independent standard Brownian motions; the noise acts on the two atoms themselves. The case \(\nu_\beta=0\) is the exact two-atom solution of the deterministic mean-field equation. It also describes two coincident groups of tokens when their sizes have ratio \(p_\beta:q_\beta\). Independent noises on individual tokens of a group do not preserve coincidence, and (1) does not assert a reduction of that model.

Put

\[
a(s)=1-\cos s,\qquad
\rho_\beta=\min\{p_\beta/q_\beta,q_\beta/p_\beta\},\qquad
L_\beta=-\log\rho_\beta\geq0.
\]

Let \(X\) be the shorter angular distance, with \(X_0=x\), and let
\(\tau_\delta=\inf\{t\geq0:X_t\leq\delta\}\).

## Theorem

Suppose \(L_\beta/\beta\to\kappa\in[0,\infty)\), and define
\(A(s)=(a(s)-\kappa)_+\), where \(t_+=\max\{t,0\}\).

1. In the deterministic case, the time \(T_\beta\) to reach delta satisfies

   \[
   \lim_{\beta\to\infty}\frac{\log T_\beta}{\beta}=A(x).       \tag{2}
   \]

   Write \(C_\beta=p_\beta/q_\beta+q_\beta/p_\beta\) and define

   \[
   B=\int_\delta^x\frac{ds}{\sin s}
    =\log\frac{\tan(x/2)}{\tan(\delta/2)},\qquad
   J_\beta=\int_\delta^x\frac{e^{\beta a(s)}}{\sin s}\,ds.
   \]

   For every beta and every pair of positive masses there is the uniform estimate

   \[
   \max\{B,J_\beta/C_\beta\}\leq T_\beta
      \leq B+J_\beta/C_\beta.                               \tag{3a}
   \]

   More precisely, uniformly in the masses,

   \[
   0\leq\frac{J_\beta}{C_\beta}
       +\left(1-\frac2{C_\beta^2}\right)B-T_\beta
   \leq\frac{B}{C_\beta e^{\beta a(\delta)}}.               \tag{3b}
   \]

   Whenever \(e^{\beta a(x)}/(C_\beta\beta)\to\infty\), in particular whenever \(\kappa<a(x)\), the sharper asymptotic is

   \[
   T_\beta\sim
   \frac{e^{\beta a(x)}}
        {C_\beta\,\beta\sin^2x}.                           \tag{3}
   \]

   For fixed masses this has \(C_\beta=p/q+q/p\).

   At the finer critical scale
   \(L_\beta=\beta a(x)-\log\beta+b+o(1)\), with fixed real b,

   \[
   T_\beta\longrightarrow B+\frac{e^{-b}}{\sin^2x}.        \tag{3c}
   \]

   If \(\kappa>a(x)\), then

   \[
   T_\beta\longrightarrow
   \log\frac{\tan(x/2)}{\tan(\delta/2)}.                      \tag{4}
   \]

2. For \(\nu_\beta>0\), if
   \(-\log\nu_\beta/\beta\to r\in[0,\infty)\), then

   \[
   \lim_{\beta\to\infty}
   \frac{\log\mathbb E_x\tau_\delta}{\beta}
   =\min\{(1-\cos x-\kappa)_+,r\}.                          \tag{5}
   \]

The statements concern first entrance into a fixed merging neighborhood. They do not assert permanent merging or count clusters formed from general initial measures.

## 1. Scalar equation and exact formulas

Set \(E_\beta(s)=e^{\beta a(s)}\). Subtracting (1) gives

\[
dD=-h_\beta(D)\,dt+\sqrt{4\nu_\beta}\,dB,
\]

where \(B=(W_2-W_1)/\sqrt2\) is standard Brownian motion and, for \(0\leq s\leq\pi\),

\[
\begin{aligned}
h_\beta(s)
 &=\sin s\left\{\frac{q_\beta}{p_\beta E_\beta(s)+q_\beta}
              +\frac{p_\beta}{q_\beta E_\beta(s)+p_\beta}\right\}\\
 &=\sin s\left\{\frac{1}{1+\rho_\beta E_\beta(s)}
              +\frac{\rho_\beta}{E_\beta(s)+\rho_\beta}\right\}.
\end{aligned}                                                    \tag{6}
\]

The second equality follows by interchanging labels if necessary so that \(p_\beta\leq q_\beta\). The drift on the difference circle is the odd periodic extension of (6). Since it depends only on \(\cos D\) and \(\sin D\), folding the circle gives the distance generator

\[
\mathcal L_\beta f=2\nu_\beta f''-h_\beta f'
\quad\text{on }(\delta,\pi),\qquad f'(\pi)=0.                \tag{7}
\]

Indeed, smooth functions of the shorter distance lift to functions even about pi; their derivative at pi is zero. The endpoint delta is absorbing for this first entrance problem. The factor \(2\nu_\beta\) also follows by applying
\(\nu_\beta(\partial_{\theta_1}^2+\partial_{\theta_2}^2)\)
to a function of \(\theta_2-\theta_1\).

For zero noise, \(h_\beta>0\) on \((0,\pi)\), so separation of variables gives

\[
T_\beta=\int_\delta^x\frac{ds}{h_\beta(s)}.                 \tag{8}
\]

For positive noise, the exact mean is

\[
u_\beta(x):=\mathbb E_x\tau_\delta
 =\frac1{2\nu_\beta}\int_\delta^x\int_y^\pi
 \exp\left\{-\frac1{2\nu_\beta}\int_y^z h_\beta(s)\,ds\right\}
 dz\,dy.                                                     \tag{9}
\]

To verify (9), let \(v(y)\) be its inner integral including the factor \(1/(2\nu_\beta)\), and let \(u(s)=\int_\delta^s v(y)\,dy\). Differentiation gives

\[
v'(y)=-\frac1{2\nu_\beta}
       +\frac{h_\beta(y)}{2\nu_\beta}v(y),\qquad v(\pi)=0.
\]

Thus \(\mathcal L_\beta u=-1\), \(u(\delta)=0\), \(u'(\pi)=0\), and \(u\) is bounded and nonnegative. Ito's formula stopped at \(t\wedge\tau_\delta\) yields

\[
\mathbb E(t\wedge\tau_\delta)
 =u(x)-\mathbb E u(X_{t\wedge\tau_\delta})\leq u(x).
\]

The reflecting term is zero by the Neumann condition, and the stopped stochastic integral has mean zero because \(u'\) is bounded. Monotone convergence implies finite mean entrance time. Continuity at delta and bounded convergence then show that the last expectation tends to zero, proving (9).

There is also an explicit drift integral. For

\[
F_\beta(v)=\log(1+e^{L_\beta-\beta v})
             +\log(1+e^{-L_\beta-\beta v}),
\]

one has

\[
\int_y^z h_\beta(s)\,ds
 =\frac{F_\beta(a(y))-F_\beta(a(z))}{\beta}.                 \tag{10}
\]

In fact \(-F_\beta'(v)/\beta\) is the sum of the two summands in braces in (6) after setting \(E=e^{\beta v}\), and \(a'(s)=\sin s\). This proves (10), including its nonnegative sign.

## 2. Bounds uniform in the masses

For \(\rho\leq1\), \(E\geq1\),

\[
0\leq\frac{\rho}{E+\rho}\leq\frac1{1+\rho E}.
\]

The second inequality is equivalent to
\(\rho+\rho^2E\leq E+\rho\), hence to \(\rho^2\leq1\).
Consequently

\[
\frac{\sin s}{1+\rho_\beta e^{\beta a(s)}}
\leq h_\beta(s)\leq
\frac{2\sin s}{1+\rho_\beta e^{\beta a(s)}}.                 \tag{11}
\]

For every fixed \(v\geq0\),

\[
\frac1\beta\log(1+e^{\beta v-L_\beta})
 \longrightarrow(v-\kappa)_+.                             \tag{12}
\]

This follows from
\(\max\{0,t\}\leq\log(1+e^t)\leq\max\{0,t\}+\log2\)
with \(t=\beta v-L_\beta\).

## 3. Deterministic exponent and uniform mass comparison

Inverting (11) and using (8) gives

\[
\frac12\int_\delta^x
 \frac{1+\rho_\beta e^{\beta a(s)}}{\sin s}\,ds
\leq T_\beta\leq
\int_\delta^x
 \frac{1+\rho_\beta e^{\beta a(s)}}{\sin s}\,ds.             \tag{13}
\]

The upper bound is at most
\(C(1+\rho_\beta e^{\beta a(x)})\), with
\(C=\int_\delta^x ds/\sin s\) finite and positive. For any fixed
\(0<\eta<x-\delta\), the lower bound is at least
\(\eta(1+\rho_\beta e^{\beta a(x-\eta)})/2\), since \(\sin s\leq1\) and \(a\) increases. Equation (12) gives

\[
A(x-\eta)\leq\liminf\frac{\log T_\beta}{\beta}
\leq\limsup\frac{\log T_\beta}{\beta}\leq A(x).
\]

Continuity as \(\eta\downarrow0\) proves (2).

For arbitrary masses, write \(C_\beta=p_\beta/q_\beta+q_\beta/p_\beta\geq2\). Direct algebra in (6) gives

\[
\frac{h_\beta(s)}{\sin s}
  =\frac{C_\beta E_\beta(s)+2}
         {E_\beta(s)^2+C_\beta E_\beta(s)+1}.             \tag{14}
\]

For \(C\geq2\), \(E\geq1\), subtraction gives

\[
\frac{E^2+CE+1}{CE+2}-\frac EC
 =\frac{(C-2/C)E+1}{CE+2}\in[0,1].
\]

The numerator is positive since \(C-2/C>0\), and it is at most the denominator since their difference is \(2E/C+1>0\). Moreover \((E^2+CE+1)/(CE+2)\geq1\), because \(E^2\geq1\). Multiply these inequalities by \(1/\sin s\) and integrate. They prove (3a), without any asymptotic hypothesis on the masses.

A second division gives the exact identity

\[
\frac{E^2+CE+1}{CE+2}
 =\frac EC+1-\frac2{C^2}-\frac{1-4/C^2}{CE+2}.
\]

The last numerator is in \([0,1]\) for \(C\geq2\), and
\(CE_\beta(s)+2\geq C e^{\beta a(\delta)}\) on the integration interval. Integrating this identity proves (3b).

To evaluate \(J_\beta\), set
\(v=a(s)\), \(dv=\sin s\,ds\), and
\(g(v)=1/[v(2-v)]\). Then

\[
\int_\delta^x\frac{e^{\beta a(s)}}{\sin s}\,ds
 =\frac{e^{\beta a(x)}}{\beta}
 \int_0^{\beta(a(x)-a(\delta))}
 e^{-w}g(a(x)-w/\beta)\,dw.
\]

On the fixed interval \([a(\delta),a(x)]\), \(g\) is bounded and continuous. Extend the integrand by zero beyond its upper limit. Dominated convergence gives the limit \(g(a(x))=1/\sin^2x\) for the last integral. Thus
\(J_\beta\sim e^{\beta a(x)}/(\beta\sin^2x)\). If \(e^{\beta a(x)}/(C_\beta\beta)\to\infty\), the bounded additive error in (3a) is negligible, proving (3). Since \(C_\beta=e^{L_\beta}+e^{-L_\beta}\), that divergence holds whenever \(\kappa<a(x)\). When \(p=q=1/2\), \(C_\beta=2\), recovering the earlier prefactor.

Conversely, if \(e^{\beta a(x)}/(C_\beta\beta)\to0\), (3a) gives \(T_\beta\to B\). This condition can hold even at \(\kappa=a(x)\), and it holds whenever \(\kappa>a(x)\).

If \(L_\beta=\beta a(x)-\log\beta+b+o(1)\), then \(L_\beta\to\infty\) and
\(C_\beta\sim e^{L_\beta}\sim e^{\beta a(x)}e^b/\beta\).
The asymptotic for \(J_\beta\) gives
\(J_\beta/C_\beta\to e^{-b}/\sin^2x\). In (3b) the coefficient of B tends to one and the error tends to zero. This proves (3c).

If \(\kappa>a(x)\), then
\(\rho_\beta e^{\beta a(s)}\to0\) uniformly on \([\delta,x]\), while \(\rho_\beta\to0\). Formula (6) therefore gives \(h_\beta(s)/\sin s\to1\) uniformly. Integrating \(1/\sin s\) in (8) proves (4).

## 4. Noisy exponent: lower bound

Fix \(\eta>0\) so that \(x-\eta>\delta\) and \(x+\eta<\pi\). If
\(y\in[x-\eta,x]\), \(z\in[y,y+\eta]\), and \(s\in[y,z]\), (11) implies

\[
h_\beta(s)\leq
M_\beta:=\frac{2}{1+\rho_\beta e^{\beta a(x-\eta)}}.
\]

Restrict the two integrals in (9) to this rectangle with moving upper edge. Exact integration of \(e^{-M_\beta(z-y)/(2\nu_\beta)}\) gives

\[
u_\beta(x)\geq
\frac{\eta}{M_\beta}
\left(1-e^{-M_\beta\eta/(2\nu_\beta)}\right)
\geq (1-e^{-1})\eta
\min\left\{\frac\eta{2\nu_\beta},\frac1{M_\beta}\right\}.  \tag{15}
\]

The last inequality follows from
\(1-e^{-t}\geq(1-e^{-1})\min\{t,1\}\): on \([0,1]\) use concavity, and on \([1,\infty)\) use monotonicity. Equation (12) shows
\(\log(1/M_\beta)/\beta\to A(x-\eta)\). Taking logarithms in (15) and then letting eta decrease to zero proves

\[
\liminf_{\beta\to\infty}\frac{\log u_\beta(x)}{\beta}
 \geq\min\{r,A(x)\}.                                     \tag{16}
\]

This argument includes \(r=0\), \(\kappa=a(x)\), and \(\kappa>a(x)\).

## 5. Noisy exponent: upper bound and outward excursions

First, (9) and \(h_\beta\geq0\) imply

\[
u_\beta(x)\leq\frac{(x-\delta)(\pi-\delta)}{2\nu_\beta}.   \tag{17}
\]

This proves the upper exponent \(r\) when \(r\leq A(x)\).

Suppose \(r>A(x)\). By continuity, choose fixed \(\eta>0\) with
\(x+\eta<\pi\) and \(A(x+\eta)<r\). Put

\[
m_\eta=\min_{s\in[\delta,x+\eta]}\sin s>0,
\qquad b_\beta=
\frac{m_\eta}{1+\rho_\beta e^{\beta a(x+\eta)}}.
\]

For \(y\in[\delta,x]\) and \(z\in[y,y+\eta]\), (11) gives
\(h_\beta(s)\geq b_\beta\) throughout \([y,z]\). For \(z\geq y+\eta\), nonnegativity of the drift gives
\(\int_y^z h_\beta\geq\eta b_\beta\). Splitting the inner integral in (9) at \(y+\eta\) yields

\[
u_\beta(x)\leq(x-\delta)
\left\{\frac1{b_\beta}
 +\frac\pi{2\nu_\beta}
       e^{-\eta b_\beta/(2\nu_\beta)}\right\}.             \tag{18}
\]

This estimate does not require monotonicity of the unequal-mass drift. By (12),

\[
\frac{\log(1/b_\beta)}\beta\to A(x+\eta),\qquad
\frac{\log(b_\beta/\nu_\beta)}\beta\to r-A(x+\eta)>0.
\]

Thus \(b_\beta/\nu_\beta\) grows exponentially. In the second term in braces in (18), the logarithm divided by beta equals

\[
\frac{\log(\pi/2)-\log\nu_\beta}{\beta}
-\frac{\eta b_\beta}{2\beta\nu_\beta}\longrightarrow-\infty.
\]

It follows that the upper exponent is at most \(A(x+\eta)\). The same reasoning applies to arbitrarily small such eta. Letting \(\eta\downarrow0\) and combining with (16) proves (5).

## 6. Independent checks and scope

In vector coordinates, write \(c=v_1\cdot v_2\) and let
\(w_1=q/(p e^{\beta(1-c)}+q)\),
\(w_2=p/(q e^{\beta(1-c)}+p)\). The projected equations are
\(\dot v_1=w_1(v_2-cv_1)\),
\(\dot v_2=w_2(v_1-cv_2)\). Direct differentiation gives

\[
\dot c=(w_1+w_2)(1-c^2).
\]

Consequently an independent exact coordinate formula is

\[
T_\beta=\int_{\cos x}^{\cos\delta}
\frac{dc}{(w_1(c)+w_2(c))(1-c^2)}.                         \tag{19}
\]

For fixed masses, \(w_1+w_2\sim (p/q+q/p)e^{-\beta(1-c)}\) uniformly on this interval. Applying the same endpoint substitution to (19) again gives (3). Under noise, applying the angular generator to \(\cos D\) gives the cosine drift
\((w_1+w_2)(1-c^2)-2\nu_\beta c\), checking the diffusion factor independently.

Formula (3) requires its stated divergence condition when the masses vary. For example, take \(p_\beta/q_\beta=e^{-\kappa\beta}\) with \(\kappa>a(x)\). Applying (3) outside that condition would incorrectly predict a time tending to zero, contradicting (4). The correct logarithmic law has a positive part. At \(\kappa=a(x)\), a zero exponent alone does not imply a bounded merging time: take \(L_\beta=\beta a(x)-\sqrt\beta\). The divergence condition in (3) then holds, giving \(T_\beta\sim e^{\sqrt\beta}/(\beta\sin^2x)\to\infty\). In contrast, \(L_\beta=\beta a(x)+\sqrt\beta\) gives \(T_\beta\to B\) by (3a). Both sequences have the same kappa.

For rational fixed masses, the deterministic result applies exactly to two coincident token groups of the corresponding sizes. Exponentially small mass ratios require a growing number of tokens in that interpretation. The theorem does not provide a width estimate for approximately coincident groups, nor a noisy independent-token reduction. Exactly antipodal deterministic atoms remain stationary, and exact deterministic coincidence takes infinite time; neither endpoint is included in the fixed-gap assumptions. No transition-time distribution or full cluster-count theorem is claimed.
