# Bistability caused by skew query–key coupling

Let

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
Q=I_2,\quad K=\kappa J,\quad V=aI_2-\omega J,
\qquad a,\omega,\kappa,\beta>0.
\]

Consider the normalized, unmasked system, including self-interaction,

\[
\dot x_i=(I-x_ix_i^T)\sum_{j=1}^n p_{ij}Vx_j,
\qquad
p_{ij}=\frac{\exp(\beta x_i^TQ^TKx_j)}
{\sum_{k=1}^n\exp(\beta x_i^TQ^TKx_k)}.                 \tag{1}
\]

All statements below concern this continuous-time equation. Set
\(q=\beta\kappa\) and \(B=\omega q\).

## Theorem

For every even \(n\ge2\), if \(B>a\), system (1) has both of the following
attracting families, each with an open basin in \((S^1)^n\):

1. Rotating consensus: for some phase \(s_\infty\),
   \(x_i(t)-e^{(s_\infty-\omega t)J}e_1\to0\) for every \(i\).
2. Stationary balanced antipodal pairs: for any fixed assignment
   \(\sigma_i\in\{1,-1\}\) with \(\sum_i\sigma_i=0\),
   \(x_i(t)\to\sigma_i e^{s_\infty J}e_1\).

The transverse linear decay rates are respectively \(a\), and
\(B-a\) together with \(B\) (the latter has multiplicity \(n-2\)).
In sufficiently small neighborhoods, nonlinear convergence holds at any
strictly smaller positive rate than the smallest transverse rate.

For \(n=2\), the complete classification by unsigned separation
\(\delta_0\in[0,\pi]\) is as follows.

- If \(B\le a\), every \(\delta_0<\pi\) approaches rotating consensus.
  The exactly antipodal pair is stationary.
- If \(B>a\), there is a unique \(\delta_*\in(0,\pi)\) satisfying
  \[
  \tan(\delta_*/2)\tanh\!\left(\frac q2\sin\delta_*\right)
       =\frac a\omega.                                      \tag{2}
  \]
  Separations below \(\delta_*\) approach rotating consensus, and those
  above it approach a stationary antipodal pair. At \(\delta_*\) the
  pair rotates with constant separation and is transversely unstable.

Thus an almost-everywhere single-cluster theorem for arbitrary matrices
cannot follow just from positive definiteness of the symmetric part of
\(V\), or from positivity of all real parts of its eigenvalues.

## 1. Angular equation

Write \(x_i=(\cos\theta_i,\sin\theta_i)\). Its unit tangent is \(Jx_i\),
so projection in (1) gives the scalar angular velocity
\(\dot\theta_i=(Jx_i)^T\sum_jp_{ij}Vx_j\).
For \(\Delta_{ij}=\theta_j-\theta_i\), direct inner products give

\[
x_i^TJx_j=-\sin\Delta_{ij},\qquad
(Jx_i)^TVx_j=a\sin\Delta_{ij}-\omega\cos\Delta_{ij}.
\]

Consequently

\[
F_i(\theta):=\dot\theta_i
=\sum_j\frac{e^{-q\sin(\theta_j-\theta_i)}}
{\sum_k e^{-q\sin(\theta_k-\theta_i)}}
\{a\sin(\theta_j-\theta_i)-\omega\cos(\theta_j-\theta_i)\}.
                                                               \tag{3}
\]

This is a smooth vector field on the compact torus, hence has unique
solutions for all time. It is invariant under adding a common angle.

## 2. Linearization at balanced antipodal configurations

Fix \(\theta_i^*=0\) when \(\sigma_i=1\), and \(\theta_i^*=\pi\)
when \(\sigma_i=-1\). All scores are zero and all weights are \(1/n\).
Also \(\sum_jx_j=0\), so every such configuration is stationary.

For a perturbation \(\theta_i=\theta_i^*+\varepsilon\eta_i\), put
\(\bar\eta=n^{-1}\sum_i\eta_i\) and
\(r=n^{-1}\sum_i\sigma_i\eta_i\). At the base configuration,
\(\cos(\theta_j^*-\theta_i^*)=\sigma_i\sigma_j\) and the sine is zero.
Differentiating the logit \(-q\sin(\theta_j-\theta_i)\) gives

\[
\ell'_{ij}=q\sigma_i\sigma_j(\eta_i-\eta_j),\qquad
p'_{ij}=\frac1n\left(\ell'_{ij}-\frac1n\sum_k\ell'_{ik}\right).
                                                               \tag{4}
\]

The derivative of the braces in (3) is
\(a\sigma_i\sigma_j(\eta_j-\eta_i)\). Its weighted sum equals
\(a\sigma_i r\), because \(\sum_j\sigma_j=0\).
The braces themselves equal \(-\omega\sigma_i\sigma_j\).
Multiplying these by (4) and summing gives
\(-B(\eta_i-\bar\eta)\); the row-average term vanishes because
\(\sum_j\sigma_j=0\). Thus the Jacobian is

\[
L=-BI+\frac Bn\mathbf1\mathbf1^T+\frac an\sigma\sigma^T. \tag{5}
\]

The vectors \(\mathbf1\) and \(\sigma\) are orthogonal and both have
squared norm \(n\). Equation (5) has eigenvalue zero on
\(\mathbf1\), eigenvalue \(a-B\) on \(\sigma\), and eigenvalue
\(-B\) on their common orthogonal complement. That complement has
dimension \(n-2\). These subspaces exhaust \(\mathbb R^n\).

## 3. Linearization at rotating consensus

At a common angle all weights are \(1/n\), the braces in (3) equal
\(-\omega\), and \(F=-\omega\mathbf1\). Differentiating the weights
contributes zero because their row sums have zero derivative. The remaining
derivative is

\[
(L_c\eta)_i=a(\bar\eta-\eta_i),\qquad
L_c=-aI+\frac an\mathbf1\mathbf1^T.                     \tag{6}
\]

The common phase has eigenvalue zero and all \(n-1\) transverse directions
have eigenvalue \(-a\). This calculation holds for every \(q\).

## 4. From the Jacobians to open basins and limiting phases

The needed local stability can be proved directly. In either case write
nearby angular lifts as
\(\theta=\theta^*+s\mathbf1+z\), with \(\bar z=0\).
For consensus take \(\theta^*=0\), \(c=-\omega\), and \(L=L_c\);
for the antipodal case take the configuration above, \(c=0\), and (5).
Common-angle invariance and Taylor expansion give

\[
F(\theta^*+s\mathbf1+z)=c\mathbf1+Lz+R(z),\qquad
\|R(z)\|\le C\|z\|^2                                    \tag{7}
\]

in a fixed small neighborhood, with a finite constant \(C\). The bound
is uniform in \(s\), by the invariance. Both Jacobians are symmetric,
have zero row sums, and on \(\mathbf1^\perp\) satisfy
\(z^TLz\le-\gamma\|z\|^2\), where
\(\gamma=a\) at consensus and \(\gamma=B-a>0\) at the antipodal pair.

Taking the mean and subtracting it in (7) yields

\[
\dot s=c+\overline{R(z)},\qquad
\dot z=Lz+R(z)-\overline{R(z)}\mathbf1.
\]

For any \(0<\rho<\gamma\), choose a radius \(r_0>0\) within the Taylor
neighborhood such that \(Cr_0\le\gamma-\rho\). Then, while
\(\|z\|\le r_0\),

\[
\tfrac12\frac{d}{dt}\|z\|^2
\le-\gamma\|z\|^2+C\|z\|^3\le-\rho\|z\|^2.
\]

An initial condition strictly inside this ball therefore cannot leave it,
and \(\|z(t)\|\le\|z(0)\|e^{-\rho t}\). Moreover,
\(|\dot s-c|\le C\|z(0)\|^2e^{-2\rho t}/\sqrt n\), so
\(s(t)-ct\) has a finite limit. These are open neighborhoods in the full
configuration space; the phase is free and the other \(n-1\) coordinates
range over a ball. They have positive product surface measure.
The asserted limiting configurations and nonlinear rates follow.

## 5. Exact two-token equation

By relabeling the two tokens and choosing angular lifts, take the unsigned
initial separation in \([0,\pi]\). The endpoints will be invariant, so
this choice persists. Put \(\delta=\theta_2-\theta_1\) and
\(m=(\theta_1+\theta_2)/2\). From (3),

\[
p_{12}=\frac1{1+e^{q\sin\delta}},\qquad
p_{21}=\frac1{1+e^{-q\sin\delta}},
\quad p_{12}+p_{21}=1,\quad
p_{21}-p_{12}=T(\delta):=\tanh\left(\frac q2\sin\delta\right).
\]

Subtracting and averaging the two angular velocities gives

\[
\begin{split}
\dot\delta&=-a\sin\delta+\omega(1-\cos\delta)T(\delta),  \tag{8}\\
\dot m&=-\frac\omega2(1+\cos\delta)
        -\frac a2 T(\delta)\sin\delta.                  \tag{9}
\end{split}
\]

The right side of (8) vanishes at both endpoints. Smoothness and uniqueness
keep \([0,\pi]\) invariant. On its interior set

\[
H(\delta)=\tan(\delta/2)T(\delta),\qquad
\dot\delta=\sin\delta\{-a+\omega H(\delta)\}.           \tag{10}
\]

## 6. Strict monotonicity of the basin function

Let \(t=\tan(\delta/2)>0\) and \(z=qt/(1+t^2)>0\). Then
\(H=t\tanh z\), and differentiation with respect to \(t\) gives

\[
\frac{dH}{dt}=\tanh z+
z\frac{1-t^2}{1+t^2}\operatorname{sech}^2z
>\tanh z-z\operatorname{sech}^2z>0.                    \tag{11}
\]

For the last inequality, the function
\(g(z)=\tanh z-z\operatorname{sech}^2z\) has \(g(0)=0\) and
\(g'(z)=2z\operatorname{sech}^2z\tanh z>0\) for \(z>0\).
The endpoint limits are

\[
\lim_{\delta\downarrow0}H(\delta)=0,
\qquad \lim_{\delta\uparrow\pi}H(\delta)=q.             \tag{12}
\]

The second follows from \(t\to\infty\), \(z\sim q/t\), and
\(\tanh z\sim z\). Thus \(H\) maps \((0,\pi)\) strictly increasingly
onto \((0,q)\).

If \(B\le a\), (10) is strictly negative throughout \((0,\pi)\).
The separation decreases to a limit, which must be a zero of its smooth
autonomous vector field. The only possible limit is zero. This includes
the threshold \(B=a\); the antipodal endpoint does not attract from the
interior at equality.

If \(B>a\), (12) gives the unique root (2). The vector field is negative
below it and positive above it. Monotonicity and the same limit argument
give convergence to zero and \(\pi\), respectively. At the root,
the derivative of (8) is
\(\omega\sin\delta_*H'(\delta_*)>0\), proving instability.
Equation (9) is constant there, giving rigid rotation. At the endpoints,

\[
\dot\delta=-a\delta+O(\delta^3),\qquad
\dot\delta=(B-a)(\pi-\delta)+O((\pi-\delta)^3).         \tag{13}
\]

These give exponential approach to each attracting endpoint at any rate
strictly below \(a\) or \(B-a\). Equation (9) gives
\(\dot m+\omega=O(\delta^2)\) at zero and
\(\dot m=O((\pi-\delta)^2)\) at \(\pi\). Integration proves convergence
of the rotating phase or stationary phase, not just of the separation.

For independent uniform initial tokens, the unsigned separation is uniform
on \([0,\pi]\). When \(B>a\), the probabilities of the two outcomes are
therefore \(\delta_*/\pi\) and \(1-\delta_*/\pi\). The boundary has
probability zero.

## 7. Same value matrix, different query–key matrix

Keep \(V=aI-\omega J\), \(\beta>0\), and \(n=2\) fixed, but instead
take \(Q=K=I\). The cross weights are now equal:

\[
p_{12}=p_{21}=p(\delta)
=\frac1{1+e^{\beta(1-\cos\delta)}}.
\]

The same subtraction of angular velocities gives
\(\dot\delta=-2ap(\delta)\sin\delta\). It is strictly negative on
\((0,\pi)\); every initially nonantipodal pair synchronizes. Near zero
the decay rate is \(a\). The mean velocity satisfies
\(\dot m=-\omega+\omega p(\delta)(1-\cos\delta)\), so the rotating
phase also converges. The exactly antipodal separation is an invariant
exception of measure zero.

In contrast, for \(Q=I\), \(K=\kappa J\), and \(\beta\kappa\omega>a\),
an open set converges to a stationary antipodal pair. The value matrix is
identical in both systems, not merely isospectral. Its symmetric part is
\(aI\) and its eigenvalues are \(a\pm i\omega\). Hence these spectral
data alone do not decide between synchronization and stationary separation.
This conclusion concerns unrestricted real query and key matrices; it does
not assert an obstruction under a symmetric positive query–key constraint.
