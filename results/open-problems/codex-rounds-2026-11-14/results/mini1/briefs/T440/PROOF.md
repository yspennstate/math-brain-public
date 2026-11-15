# An explicit lower bound on the first-click time

Fix \(0<\lambda<\alpha\). Let \(X\) be the diffusion in the question, started at the Poisson distribution of mean \(\lambda/\alpha\), and put
\[
 x_0=e^{-\lambda/\alpha},\qquad
 d=\alpha-\lambda,\qquad r=\lambda/\alpha,\qquad q=1-r.
\]
The solution is understood in the usual probability-valued state space with the moment and local integrability properties needed for its stated drift. The Poisson initial state satisfies the moment assumptions.

## Proposition

For every \(\nu>0\), define
\[
 F(y)=2\alpha y+2\lambda\log(1-y),\quad 0\le y<1,
\]
\[
 u_\nu(x)=2\nu\int_0^x e^{-\nu F(z)}
       \left(\int_z^1\frac{e^{\nu F(y)}}{y(1-y)}\,dy\right)dz.
 \tag{1}
\]
Then
\[
 \mathbb E\tau_\nu\ \ge\ u_\nu(x_0).
 \tag{2}
\]
Moreover, for fixed \(\alpha,\lambda\) in the range above,
\[
 u_\nu(x_0)\sim
 \frac{\alpha\sqrt\pi}
 {\sqrt\lambda(\alpha-\lambda)^2\sqrt\nu}
 \exp\!\left\{2\nu\left[\alpha-\lambda+
                  \lambda\log(\lambda/\alpha)\right]\right\}.
 \tag{3}
\]
Consequently, with
\[
 V=2[\alpha-\lambda+\lambda\log(\lambda/\alpha)],\qquad
 C=\frac{\alpha\sqrt\pi}{\sqrt\lambda(\alpha-\lambda)^2},
\]
\[
 \liminf_{\nu\to\infty}
 \frac{\mathbb E\tau_\nu}{C\nu^{-1/2}e^{\nu V}}\ge1,
 \qquad
 \liminf_{\nu\to\infty}\nu^{-1}\log\mathbb E\tau_\nu\ge V>0.
 \tag{4}
\]
These assertions are lower bounds for the specified diffusion. They do not identify its sharp exponential rate or prefactor.

## 1. The scalar lifetime function

Write \(a(y)=y(1-y)\), \(b(y)=y[d-\alpha y]\), and consider the scalar diffusion on \([0,1]\) with generator
\[
 L_\nu f=b f'+\frac{a}{2\nu}f''.
 \tag{5}
\]
The boundary 0 is absorbing; at 1 the diffusion coefficient vanishes and the drift is \(-\lambda\), directed into the interval. The coefficients give the usual unique Wright--Fisher diffusion. No artificial killing or absorbing condition is imposed at 1.

A direct calculation gives
\[
 F'(y)=\frac{2b(y)}{a(y)}=2\alpha-\frac{2\lambda}{1-y}.
 \tag{6}
\]
For \(0<x<1\), differentiation in (1) gives
\[
 v_\nu(x):=u_\nu'(x)
 =2\nu e^{-\nu F(x)}\int_x^1\frac{e^{\nu F(y)}}{a(y)}\,dy>0,
\]
\[
 v_\nu'(x)=-\nu F'(x)v_\nu(x)-\frac{2\nu}{a(x)}.
\]
Equations (5)--(6) therefore give \(L_\nu u_\nu=-1\) on \((0,1)\).

For fixed \(\nu\), as \(x\downarrow0\), the inner integral is
\(\log(1/x)+O(1)\). This follows by subtracting \(1/y\) from its integrand on any fixed small interval near zero. Since \(e^{-\nu F(x)}=1+O(x)\),
\[
 v_\nu(x)=2\nu\log(1/x)+O(1).
\]
Thus \(u_\nu\) extends continuously to 0 with value 0.

At the other endpoint, substitute \(x=1-h\) and \(y=1-hs\) in the formula for \(v_\nu\). It becomes
\[
 v_\nu(1-h)=2\nu\int_0^1
 \frac{e^{2\nu\alpha h(1-s)}s^{2\nu\lambda-1}}{1-hs}\,ds.
 \tag{7}
\]
For \(|h|\) small this expression and its derivatives in \(h\) are integrable uniformly in \(s\), since \(2\nu\lambda>0\). Hence \(u_\nu\) is smooth up to 1 and
\[
 u_\nu'(1)=2\nu\int_0^1s^{2\nu\lambda-1}ds=1/\lambda.
\]
In particular \(u_\nu\) is bounded on \([0,1]\), and the generator equation also holds at 1 because
\(-\lambda u_\nu'(1)=-1\).

For completeness, (1) is the exact mean time for the scalar diffusion \(Y\) to hit 0. Let \(T_\epsilon=\inf\{t:Y_t\le\epsilon\}\), with \(0<\epsilon<x\). Itô's formula, stopped at \(t\wedge T_\epsilon\), gives
\[
 \mathbb E(t\wedge T_\epsilon)
 =u_\nu(x)-\mathbb E u_\nu(Y_{t\wedge T_\epsilon})
 \le u_\nu(x).
\]
There is no upper-endpoint term, by (7). As \(\epsilon\downarrow0\), continuity of the paths gives \(T_\epsilon\uparrow T_0\), including the possibility of infinity. Monotone convergence then gives \(\mathbb E T_0\le u_\nu(x)<\infty\). In the displayed identity, let \(\epsilon\downarrow0\) and then \(t\to\infty\). Boundedness of \(u_\nu\), almost sure finiteness of \(T_0\), and \(u_\nu(0)=0\) show that the terminal expectation tends to zero. Therefore \(\mathbb E_xT_0=u_\nu(x)\).

## 2. Transfer to the infinite-dimensional diffusion

Every probability vector on the nonnegative integers satisfies
\[
 m(X):=\sum_{k\ge0}kX_k\ge\sum_{k\ge1}X_k=1-X_0.
 \tag{8}
\]
The drift and quadratic variation of \(Z=X_0\) are
\[
 dZ=(\alpha m(X)-\lambda)Z\,dt+dM,
 \qquad d\langle M\rangle_t=\nu^{-1}Z(1-Z)\,dt.
\]
For \(Z>0\), Itô's drift for \(u_\nu(Z)\) is
\[
 -1+\alpha Z\,[m(X)-(1-Z)]u_\nu'(Z)\ge-1.
 \tag{9}
\]
At \(Z=1\), the same identity holds by continuity and \(m(X)=0\).

Here is the stopping argument without a scalar closure assumption. Put
\(\tau_\epsilon=\inf\{t:Z_t\le\epsilon\}\). On \([\epsilon,1]\), \(u_\nu'\) and \(u_\nu''\) are bounded. Localize further when
\(\int_0^{s\wedge\tau_\epsilon} Z_v m(X_v)dv\) reaches an integer \(n\). This removes any integrability issue from the excess drift in (9). This integral is locally finite before \(\tau_\epsilon\), as follows from the coordinate SDE itself (or from the standard moment properties of the solution). At these stops the martingale has zero expectation and (9) gives
\[
 \mathbb E u_\nu(Z_{t\wedge\tau_\epsilon\wedge S_n})
 \ge u_\nu(x_0)-\mathbb E(t\wedge\tau_\epsilon\wedge S_n).
\]
Let \(n\to\infty\) using bounded convergence for both displayed random variables. Then let \(\epsilon\downarrow0\), again using continuity and bounded convergence for fixed \(t\), to obtain
\[
 \mathbb E(t\wedge\tau_\nu)
 \ge u_\nu(x_0)-\mathbb E u_\nu(Z_{t\wedge\tau_\nu}).
 \tag{10}
\]
If \(\mathbb E\tau_\nu=\infty\), (2) is immediate. Otherwise \(\tau_\nu<\infty\) almost surely and the last expectation in (10) tends to zero as \(t\to\infty\), by boundedness and \(u_\nu(0)=0\). Monotone convergence on the left proves (2).

## 3. Sharp evaluation of the scalar integral

The function \(F\) has a unique maximum at \(q=1-r\), with
\[
 F(0)=0,\quad F'(0)=2d,\quad F(q)=V,
 \quad F''(q)=-\frac{2\alpha^2}{\lambda}.
 \tag{11}
\]
The value \(V\) is positive: \(1-r+r\log r\) vanishes at 1 and has derivative \(\log r<0\) on \((0,1)\).
Also \(x_0=e^{-r}>1-r=q\), since \(e^{-r}>1-r\) for \(r>0\).

Choose fixed \(0<\delta<q<b<x_0\) with \(F(b)>0\), which is possible by continuity at \(q\). Let
\[
 A_\nu=\int_0^\delta e^{-\nu F(z)}dz,
 \qquad
 B_\nu=\int_\delta^1\frac{e^{\nu F(y)}}{a(y)}dy.
\]
Since \(F\) is strictly increasing on \([0,\delta]\) and \(F'(0)=2d>0\),
\[
 A_\nu\sim\frac{1}{2\nu d}.
 \tag{12}
\]
One direct justification is the change of variable \(w=\nu F(z)\). The resulting integrand is
\(\nu^{-1}e^{-w}/F'(F^{-1}(w/\nu))\), with derivative bounded away from zero on this interval; dominated convergence gives (12).

Ordinary Laplace asymptotics at the interior maximum give
\[
 B_\nu\sim\frac{e^{\nu V}}{a(q)}
                  \sqrt{\frac{\pi\lambda}{\nu\alpha^2}}.
 \tag{13}
\]
The singularity of \(1/a(y)\) at 1 does not invalidate this step. To check this, choose \(c\in(q,1)\). For \(y\ge c\), set \(\kappa_c=2[\alpha c-d]>0\). Then
\[
 -F'(y)=\frac{2[\alpha y-d]}{1-y},\qquad
 \frac1{y(1-y)}\le\frac{-F'(y)}{c\kappa_c}.
\]
Integration gives
\[
 \int_c^1\frac{e^{\nu F(y)}}{a(y)}dy
 \le\frac{e^{\nu F(c)}}{\nu c\kappa_c}.
 \tag{14}
\]
Because \(F(c)<V\), this is negligible compared with (13). On \([\delta,c]\), the amplitude is smooth. Taylor expansion
\(F(q+h)=V-\alpha^2h^2/\lambda+O(h^3)\), the substitution \(h=s/\sqrt\nu\), and a quadratic upper bound in a fixed neighborhood of \(q\) give the Gaussian integral in (13); outside this neighborhood there is a strict gap below \(V\).

It remains to show that (1) is asymptotic to \(2\nu A_\nu B_\nu\). This matters because \(F\) can be negative beyond \(q\); bounding its two factors separately over the whole integration region would be incorrect.

Split the triangle \(0\le z\le x_0,\ z\le y\le1\) into four pieces. All integrands are nonnegative.

* On \(0\le z\le\delta\le y\le1\), its contribution is exactly \(2\nu A_\nu B_\nu\).
* On \(0\le z\le y\le\delta\), the contribution is at most
  \[
  \frac{2\nu\delta}{1-\delta}e^{\nu F(\delta)}.
  \]
  Indeed, \(F(y)-F(z)\le F(\delta)\), and the length \(y\) of the inner \(z\)-interval cancels the factor \(1/y\). Since \(F(\delta)<V\), this is \(o(\nu^{-1/2}e^{\nu V})\).
* On \(\delta\le z\le b\), let \(m=\min\{F(\delta),F(b)\}>0\). The contribution is at most
  \[
  2\nu(b-\delta)e^{-\nu m}B_\nu
  =O(\sqrt\nu e^{\nu(V-m)}),
  \]
  which is again negligible.
* On \(b\le z\le x_0\), (14) with \(c=z\), or the same derivative estimate using the fixed constants \(b\) and \(\kappa_b\), gives
  \[
   \int_z^1\frac{e^{\nu F(y)}}{a(y)}dy
       \le\frac{e^{\nu F(z)}}{\nu b\kappa_b}.
  \]
  Its contribution to (1) is at most \(2(x_0-b)/(b\kappa_b)=O(1)\).

These four estimates prove
\[
 u_\nu(x_0)\sim2\nu A_\nu B_\nu
 \sim\frac{e^{\nu V}}{d\,a(q)}
              \sqrt{\frac{\pi\lambda}{\nu\alpha^2}}.
\]
Finally \(a(q)=qr=\lambda d/\alpha^2\). Substitution gives (3), and then (2) gives (4).

## Scope

The exact inequality (2) uses only the drift inequality (8) and remains valid for positive \(\alpha,\lambda\) outside \(\lambda<\alpha\); the metastable evaluation (3) requires \(q\in(0,1)\). Neither (3) nor its error control is uniform as \(\lambda/\alpha\) approaches 0 or 1. The comparison is strict in the drift whenever mass lies in classes \(k\ge2\), since
\[
 m(X)-(1-X_0)=\sum_{k\ge2}(k-1)X_k.
\]
Thus no matching upper bound follows from this argument. No claim of novelty for this scalar comparison is made.
