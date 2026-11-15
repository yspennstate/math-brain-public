# A summed stationary-phase bound for the passage coefficients

Write \(\mathbb T=\mathbb R/\mathbb Z\) with normalized length measure,
and \(e(x)=\exp(2\pi i x)\). All constants below depend on the fixed
packet data. No uniformity over changing coordinate charts is claimed.

## Statement

Let \(V\in C^\infty(\mathbb T;\mathbb R)\), let \(I\) be an open arc
on which \(V'>0\), and let \(m\in\mathbb Z\setminus\{0\}\).
Let \(A\in C^\infty(\mathbb T^2;\mathbb C)\) have support compactly
contained in \(I\times\mathbb T\). Fix a real lift of \(I\).
For each positive integer \(N\), suppose

\[
 |\Delta_N|\le N^{-1},\qquad
 H_N'=N(V+\Delta_N),\qquad H_N(u+1)-H_N(u)\in\mathbb Z.       \tag{1}
\]

Here \(H_N\) is a smooth real lift, so \(e(mH_N)\) is periodic.
Define

\[
 C_{N,j}(a)=\int_{\mathbb T}A(u,a)e(mH_N(u)-ju)\,du.          \tag{2}
\]

If \(u_*\in I\) solves \(mV(u_*)=j/N-m\Delta_N\), put

\[
 \ell_{N,j}(a)=
 \frac{A(u_*,a)}{\sqrt{N|m|V'(u_*)}}
 e\left(mH_N(u_*)-ju_*+\frac{\operatorname{sgn}(m)}8\right).
                                                                    \tag{3}
\]

Set this to zero if there is no solution or its amplitude is zero.
There is a constant \(C_\eta<\infty\), independent of \(N,j,a\) and
the permitted choices of \(\Delta_N,H_N\), such that

\[
 \boxed{\quad
 \eta_N^2:=\sum_{j\in\mathbb Z}\int_{\mathbb T}
           |C_{N,j}(a)-\ell_{N,j}(a)|^2\,da
       \le \frac{C_\eta^2}{N^2}.
 \quad}                                                           \tag{4}
\]

In particular this proves the array convergence left conditional in
round 5. Both signs of \(m\), all integer indices, and stationary points
crossing the amplitude support are included.

## Extending the phase without changing the integral

Choose a closed interval \(K\) strictly inside the lifted arc \(I\)
whose interior contains the projection of \(\operatorname{supp}A\).
Choose a smooth cutoff \(\rho\) compactly supported in \(I\), equal
to one on an open interval containing \(K\), with \(0\le\rho\le1\).
For any \(v_0>0\), set on \(\mathbb R\)

\[
 w(u)=\rho(u)V'(u)+(1-\rho(u))v_0.                              \tag{5}
\]

The product with \(V'\) is extended by zero outside \(I\).
There are constants \(0<\kappa\le M<\infty\) with
\(\kappa\le w\le M\): on the compact support of \(\rho\),
\(V'\) has a positive minimum; elsewhere \(w=v_0\).
Integrate \(w\), choosing the integration constant to give a function
\(\widetilde V\) agreeing with \(V\) on the interval where \(\rho=1\).
It is a proper increasing diffeomorphism \(\mathbb R\to\mathbb R\).
All its derivatives of positive order are bounded.

Let \(Q'=\widetilde V\). On a neighborhood of \(K\) there is a
constant \(h_N\) such that

\[
 H_N(u)=NQ(u)+N\Delta_Nu+h_N.                                   \tag{6}
\]

Extend \(A\) by zero to \(\mathbb R\times\mathbb T\). It is smooth
and compactly supported in \(u\). Equation (2) becomes exactly

\[
 C_{N,j}(a)=e(mh_N)\int_{\mathbb R}A(u,a)e(N\Phi_t(u))\,du,
 \quad \Phi_t(u)=mQ(u)-tu,\quad t=j/N-m\Delta_N.                 \tag{7}
\]

Write \(\epsilon=\operatorname{sgn}(m)\), \(k=|m|\kappa\), and
\(K_1=|m|M\). Then

\[
             k\le\epsilon\Phi_t''(u)\le K_1.                  \tag{8}
\]

There is a unique critical point \(r(t)\), determined by
\(m\widetilde V(r(t))=t\). It depends smoothly on \(t\).
Where it lies on the original amplitude support, it is exactly the
point in (3). Where it does not, the amplitude is zero. Strict
monotonicity ensures that the extension cannot introduce a nonzero
leading term absent from (3).

## A quadratic coordinate uniform at support edges

Set

\[
 y=y_t(u)=\operatorname{sgn}(u-r(t))
 \sqrt{2\epsilon(\Phi_t(u)-\Phi_t(r(t)))}.                       \tag{9}
\]

Taylor's formula with integral remainder writes this as

\[
 y=(u-r(t))\sqrt{\,2\int_0^1(1-v)
            \epsilon\Phi_t''(r(t)+v(u-r(t)))\,dv\,}.           \tag{10}
\]

Thus it is smooth at \(u=r(t)\), and
\(\sqrt{k}|u-r(t)|\le |y|\le\sqrt{K_1}|u-r(t)|\).
Away from the critical point,

\[
 \partial_u y=\frac{\epsilon\Phi_t'(u)}{y}>0,
 \qquad \frac{k}{\sqrt{K_1}}\le\partial_u y
                   \le\frac{K_1}{\sqrt{k}}.                    \tag{11}
\]

The inequalities follow by integrating (8) from \(r(t)\) to \(u\)
and using the preceding bounds on \(y\). They extend to \(u=r(t)\)
by continuity. Hence \(y_t\) is a global smooth increasing
diffeomorphism of \(\mathbb R\); its range is all of \(\mathbb R\)
by the lower bound on \(|y|\). Write its inverse as \(u_t(y)\) and put

\[
 b_{t,a}(y)=A(u_t(y),a)\,\partial_yu_t(y).                       \tag{12}
\]

For \(t\) in any fixed compact interval these functions have support
in one fixed compact \(y\) interval, and their first four derivatives
in \(y\) are uniformly bounded. Indeed, \(r(t)\) ranges over a
compact interval, \(u\) ranges over the fixed support of \(A\), and
(10)--(11) and the implicit function theorem give smooth inverse
derivatives on the resulting compact set. The zero extension of \(A\)
is smooth, including its support boundary. No assertion that the
amplitude is nonzero at the critical point is needed. Moreover

\[
 \begin{split}
 \int A(u,a)e(N\Phi_t(u))\,du
 &=e(N\Phi_t(r(t)))
       \int b_{t,a}(y)e(\epsilon Ny^2/2)\,dy,\\
 b_{t,a}(0)&=\frac{A(r(t),a)}{\sqrt{|m|\widetilde V'(r(t))}}.
 \end{split}                                                    \tag{13}
\]

## Quadratic integral with a finite remainder bound

For \(b\in C_c^\infty(\mathbb R)\), use the Fourier transform
\(\widehat b(\xi)=\int b(y)e(-\xi y)\,dy\).
Fourier inversion of the quadratic exponential gives

\[
 \int b(y)e(\epsilon Ny^2/2)\,dy
 =\frac{e(\epsilon/8)}{\sqrt N}
       \int\widehat b(\xi)e(-\epsilon\xi^2/(2N))\,d\xi.         \tag{14}
\]

Here is a justification including convergence. Insert the factor
\(e^{-\pi\tau y^2}\), \(\tau>0\), in the left side and insert the
absolutely convergent Fourier inversion of \(b\). Fubini is valid
because \(\widehat b\in L^1\) and the Gaussian is integrable.
The inner integral is

\[
 \int e^{-\pi(\tau-i\epsilon N)y^2+2\pi i\xi y}\,dy
 =(\tau-i\epsilon N)^{-1/2}
          \exp\left(-\frac{\pi\xi^2}{\tau-i\epsilon N}\right). \tag{15}
\]

For positive real quadratic coefficient this is the usual Gaussian
transform, obtained by differentiating in \(\xi\), integrating by
parts and using its value at zero. That value follows from the real
Gaussian integral, whose square is evaluated in polar coordinates.
More explicitly, for coefficient \(z>0\), if the integral is \(F(\xi)\),
integration of the \(y\) derivative gives
\(F'(\xi)=-2\pi\xi F(\xi)/z\), and
\(F(0)=z^{-1/2}\). The normalization is
\((\int e^{-\pi y^2}dy)^2=2\pi\int_0^\infty re^{-\pi r^2}dr=1\).
Both sides are analytic in the quadratic coefficient in the right
half-plane, with differentiation under the integral justified on its
compact subsets; the identity theorem gives (15) there. Choose the
square root positive on the positive real axis. The modulus of (15)
is at most \(N^{-1/2}\). Dominated convergence against
\(|\widehat b|\) as \(\tau\downarrow0\) proves (14), including
the phase \(e(\epsilon/8)\).

Since \(|e^{-ix}-1|\le |x|\), (14) implies

\[
 \left|\int b(y)e(\epsilon Ny^2/2)\,dy
             -\frac{e(\epsilon/8)}{\sqrt N}b(0)\right|
 \le\frac\pi{N^{3/2}}
                  \int\xi^2|\widehat b(\xi)|\,d\xi.            \tag{16}
\]

The moment is finite with the explicit bound

\[
 \int\xi^2|\widehat b(\xi)|\,d\xi
 \le \frac23\|b\|_1+\frac{1}{8\pi^4}\|b^{(4)}\|_1.            \tag{17}
\]

On \(|\xi|\le1\), use \(|\widehat b|\le\|b\|_1\) and
\(\int_{-1}^1\xi^2d\xi=2/3\). Outside this interval, four
integrations by parts give
\(|\widehat b(\xi)|\le(2\pi|\xi|)^{-4}\|b^{(4)}\|_1\).
Since \(\int_{|\xi|>1}\xi^{-2}d\xi=2\), this gives (17).

## The bounded frequency range

Choose a positive integer

\[
                 R>2|m|(\|V\|_\infty+1).                      \tag{18}
\]

For \(|j|\le RN\), the parameter in (7) has
\(|t|\le R+|m|\). Define the finite constant

\[
 B=\pi\sup_{|t|\le R+|m|,\ a\in\mathbb T}
       \left(\frac23\|b_{t,a}\|_1
                         +\frac{\|\partial_y^4 b_{t,a}\|_1}{8\pi^4}\right).
                                                                    \tag{19}
\]

Its finiteness was proved after (12). Equations (7), (13) and (16)
give, uniformly on this range,

\[
                    |C_{N,j}(a)-\ell_{N,j}(a)|\le BN^{-3/2}.   \tag{20}
\]

If the extended critical point lies outside the amplitude support,
\(b_{t,a}(0)=0\) and the same estimate applies. If it lies on the
boundary of that support, the same smooth family applies. This is the
required uniformity when a stationary point enters or leaves support.

## The infinite tail

For \(|j|>RN\), set
\(D(u)=mH_N'(u)-j=Nm(V(u)+\Delta_N)-j\).
By (18) and (1), \(|D(u)|\ge |j|/2\) on the support of the amplitude.
There is no leading term on this range: a nonzero one would require
\(j/N=m(V(u_*)+\Delta_N)\) at a point of that support, contrary
to (18).

Twice use \((e(mH_N-ju))'=2\pi iD e(mH_N-ju)\). Boundary
terms vanish because the amplitude is compactly supported in the lift.
This gives

\[
 C_{N,j}(a)=\frac1{(2\pi i)^2}
 \int e(mH_N-ju)
 \left(\frac{A''}{D^2}-\frac{3A'D'}{D^3}
              -\frac{AD''}{D^3}+\frac{3A(D')^2}{D^4}\right)du. \tag{21}
\]

Primes here denote \(u\) derivatives. The denominators can be defined
on a neighborhood of the support, which suffices for the integrations.
Put \(v_1=\|V'\|_\infty\), \(v_2=\|V''\|_\infty\), and
\(A_r=\sup_a\|\partial_u^r A(\cdot,a)\|_{L^1(\mathbb R)}\).
Since \(N<|j|/R\), (21) implies

\[
 \begin{split}
 |C_{N,j}(a)|&\le D_0|j|^{-2},\\
 D_0&=\frac1{(2\pi)^2}
 \left(4A_2+\frac{24|m|v_1A_1}{R}
             +\frac{8|m|v_2A_0}{R}
             +\frac{48m^2v_1^2A_0}{R^2}\right).                \tag{22}
 \end{split}
\]

There are \(2RN+1\) indices in (20). Since \(RN\) is an integer,
monotonicity of \(x^{-4}\) gives

\[
 \sum_{|j|>RN}|j|^{-4}
       \le2\int_{RN}^\infty x^{-4}\,dx
       =\frac2{3R^3N^3}.                                      \tag{23}
\]

Integrating in \(a\), whose total measure is one, proves

\[
 \eta_N^2\le\frac{(2R+1)B^2}{N^2}
                  +\frac{2D_0^2}{3R^3N^3}.
 \quad\text{One may take}\quad
 C_\eta^2=(2R+1)B^2+\frac{2D_0^2}{3R^3}.                       \tag{24}
\]

This proves (4).

## Retained cutoffs and coefficient intensities

Assume now that \(mV\) is bounded away from zero on the projection
of \(\operatorname{supp}A\). In the passage this is arranged by the
integer addition in \(V=c+\phi\). Define, with zero extension off the
branch \(s=mV(u)\),

\[
 W(s,a)=\frac{|A(u,a)|^2}{|m|V'(u)},\qquad
 E=\{(mV(u),a):(u,a)\in\operatorname{supp}A\}.                 \tag{25}
\]

The zero extension is smooth and compactly supported. To see this,
the inverse of \(mV\) is smooth on its branch and the amplitude is
zero on a neighborhood of the branch endpoints. Also \(W\) vanishes
for \(|s|<s_0\) for some \(s_0>0\). Set

\[
 d_N=m\Delta_N,\quad
 M(s)=\int_{\mathbb T}W(s,a)\,da,\quad
 \mathcal M=\int M(s)\,ds,\quad U=\int|M'(s)|\,ds.
                                                                    \tag{26}
\]

Change of variables and (3) give

\[
 |\ell_{N,j}(a)|^2=N^{-1}W(j/N-d_N,a),\qquad
 \mathcal M=\int_{\mathbb T^2}|A|^2.
                                                                    \tag{27}
\]

Choose a fixed smooth \(0\le\chi(s,a)\le1\), compactly supported
in \(s\), equal to one on an open neighborhood of \(E\), and
supported away from \(s=0\). Compactness gives \(\delta_\chi>0\)
such that \(\chi=1\) on the closed \(\delta_\chi\) neighborhood
of \(E\). For all sufficiently large \(N\),
\(|d_N|<\min(\delta_\chi,s_0)\). Then

\[
 \chi(j/N,a)\ell_{N,j}(a)=\ell_{N,j}(a),\qquad
 \ell_{N,0}=0.                                                   \tag{28}
\]

Indeed, the support of the leading array lies in
\(E+(d_N,0)\). Consequently

\[
 \sum_j\int_{\mathbb T}
       |(1-\chi(j/N,a))C_{N,j}(a)|^2\,da
 \le\eta_N^2\le C_\eta^2/N^2.                                  \tag{29}
\]

This follows by replacing \(C\) inside \((1-\chi)C\) by
\(C-\ell\) using (28). It includes the deleted zero mode.
The actual removed intensity satisfies the same bound:

\[
 \sum_j\int_{\mathbb T}(1-\chi(j/N,a)^2)|C_{N,j}(a)|^2\,da
                  \le\eta_N^2.
\]

Indeed, wherever \(\chi<1\), (28) forces \(\ell=0\), and
\(1-\chi^2\le1\). This also holds after multiplication by \(\psi^2\).
For any measurable \(0\le\psi\le1\), Parseval in \(u\) therefore
gives the reconstruction estimate

\[
 \left\|\sum_j\psi(a)\chi(j/N,a)C_{N,j}(a)e(ju)
                   -\psi(a)A(u,a)e(mH_N(u))\right\|_2
 \le C_\eta/N.                                                   \tag{30}
\]

Only finitely many retained indices occur. Multiplication by
\(e(m\theta-mH_N(u))\) preserves this norm and gives the corresponding
packet transport estimate in the passage coordinates.

For the intensity discrepancy take \(\psi\in C_c^\infty((0,1))\)
in a lifted spare-coordinate arc, \(0\le\psi\le1\), and put

\[
 \begin{split}
 q_j(a)&=\psi(a)^2\chi(j/N,a)^2|C_{N,j}(a)|^2,\\
 E_N&=\sum_j\int_0^1
       |q_j(a)-N^{-1}W(j/N,a)\psi(a)^2|\,da.
 \end{split}                                                     \tag{31}
\]

The definition gives \(q_0=0\) since \(\chi\) is supported away
from zero. Choose \([a_-,a_+]\) containing the \(s\) support of
\(W\), and put \(d=a_+-a_-\) and

\[
 \Omega=\int_0^1\psi(a)^2\sup_s|\partial_sW(s,a)|\,da.
                                                                    \tag{32}
\]

Then for all sufficiently large \(N\),

\[
 \begin{split}
 E_N&\le\frac{C_\eta}{N}
        \left(\sqrt{\mathcal M}
                   +\sqrt{\mathcal M+U/(2N)}\right)
       +\frac{|m|}{N}\left(d+\frac{2|m|+1}{N}\right)\Omega\\
     &\le C_E/N,\\
 C_E&=C_\eta\left(\sqrt{\mathcal M}
                       +\sqrt{\mathcal M+U/2}\right)
                         +|m|(d+2|m|+1)\Omega.                  \tag{33}
 \end{split}
\]

For completeness, (28) gives pointwise

\[
 |\chi^2|C|^2-|\ell|^2|
       \le |C-\ell|(|C|+|\ell|).                               \tag{34}
\]

If \(\ell\ne0\), this is the squared-modulus inequality with
\(\chi=1\); if \(\ell=0\), it follows from \(\chi\le1\).
Multiplication by \(\psi^2\), summation and Cauchy--Schwarz give
\(\eta_N(\sqrt{\mathcal M}+\sqrt{B_N})\), where Parseval gives
the exact mass \(\sum_j\int|C_{N,j}|^2=\mathcal M\) and

\[
 B_N=N^{-1}\sum_j M(j/N-d_N)
                   \le\mathcal M+U/(2N).                       \tag{35}
\]

To verify (35), partition the real line into cells of length \(1/N\)
centered on \(j/N-d_N\), compare the center value of \(M\) with
its value at each point of the cell, and integrate \(M'\) between
them. After interchanging the integrations the weight on \(|M'|\)
is at most \(1/(2N)\). This proves (35).

Finally the fundamental theorem of calculus bounds the integrated
change from \(W(j/N-d_N,a)\) to \(W(j/N,a)\) by
\(|d_N|\Omega\). It is zero unless
\(j/N\in[a_--|d_N|,a_++|d_N|]\), an interval containing at
most \(N(d+2|d_N|)+1\) lattice indices. Multiplying by \(1/N\)
and using \(|d_N|\le |m|/N\) proves (33).

Thus the retained coefficient discrepancy in round 5 is now
\(O(N^{-1})\), rather than an unproved input, for these fixed smooth
packets and fixed support neighborhoods.

## Consequence for the round 5 residue bound

Use a linear jitter \(J(a)=La+\beta\) on the support of \(\psi\),
with \(L>0\). Push each \(q_j(a)da\), \(j\ne0\), under
\(t=j/N+jJ(a)/N^2\), group by \(j\equiv h\pmod P\), and fold
modulo one. Denote the resulting densities by \(p_{N,h}\).
Let \(p(z)=\sum_{l\in\mathbb Z}M(z+l)\), and set

\[
 \begin{split}
 f(s,a)&=W(s,a)\psi(a)^2,\\
 H&=\int\frac{1}{|s|}\int|\partial_a f(s,a)|\,da\,ds,\\
 C_{\rm cut}&=\int\!\int W(s,a)(1-\psi(a)^2)\,da\,ds,\\
 K(s,y)&=\frac{1}{|s|L}
                 f\left(s,\frac{y/s-\beta}{L}\right),\\
 J_1&=\int |y|\sup_s|\partial_sK(s,y)|\,dy,\\
 J_2&=\int(2y^2+|y|)\sup_s|\partial_sK(s,y)|\,dy.
 \end{split}                                                      \tag{36}
\]

Set \(K=0\) near \(s=0\), and extend \(f\) by zero outside its
spare-coordinate arc. These are finite fixed-data quantities. Applying
the independently rechecked round 5 inequality with (33) gives

\[
 \boxed{\quad
 \sum_{h=0}^{P-1}\|p_{N,h}-p/P\|_1
 \le\frac{C_E+dJ_1}{N}+\frac{J_2}{N^2}
                       +\frac{PH}{2L}+C_{\rm cut}.
 \quad}                                                          \tag{37}
\]

There is no divisibility condition between \(P\) and \(N\).
The coefficient and sampling errors tend to zero after all other
data are fixed. Equation (37) does not say that the last two terms
vanish for a fixed cutoff and jitter. They must be made small by
the separate choices already described in round 5.

## Independent checks

The quadratic normalization can be checked without the Fourier
inversion step. For the Schwartz amplitude \(b(y)=e^{-\pi y^2}\),
direct Gaussian evaluation gives

\[
 \int e^{-\pi y^2}e(\epsilon Ny^2/2)\,dy
 =(1-i\epsilon N)^{-1/2}
 =\frac{e(\epsilon/8)}{\sqrt N}
       \left(1-\frac{i\epsilon}{2N}+O(N^{-2})\right).          \tag{38}
\]

This independently checks the sign \(\epsilon/8\), the leading
\(N^{-1/2}\) factor and the \(N^{-3/2}\) remainder scale. In
(14), \(\widehat b(\xi)=e^{-\pi\xi^2}\) gives the same first
correction, since integration by parts gives
\(\int\xi^2e^{-\pi\xi^2}d\xi=1/(2\pi)\). This example checks
the quadratic kernel; the compact-support theorem was proved above.

There is also a direct check of the intensity error, independent of
the array Cauchy--Schwarz step. Put

\[
 L_0=\sup_{|t|\le R+|m|,\ a\in\mathbb T}|b_{t,a}(0)|
       \le\frac{\|A\|_\infty}{\sqrt{|m|\kappa}}.
\]

On the bounded frequency range, write \(C=\ell+r\) and use (20).
Then, pointwise in \(a\),

\[
 \big||C|^2-|\ell|^2\big|
       \le2L_0B/N^2+B^2/N^3.
\]

The same bound holds after the cutoff \(\chi^2\), since the retained
leading term is unchanged and its remainder is \(\chi r\).
On the exterior range \(\ell=0\) and the summed intensity
is at most \(2D_0^2/(3R^3N^3)\). Thus, even before integration in
\(a\), the sum of retained intensity errors against the rounded
leading intensities is at most

\[
 (2RN+1)(2L_0B/N^2+B^2/N^3)
                       +2D_0^2/(3R^3N^3)=O(N^{-1}).           \tag{39}
\]

After multiplication by \(\psi^2\), integration, and the separate
rounding bound, this reproduces \(E_N=O(N^{-1})\) without Parseval
or a bound on the leading array's total mass.

For another check on (21)--(22), divide the phase by \(N\) and put
\(p(u)=m(V(u)+\Delta_N)-j/N\). Two integrations by parts give
the same bracket as (21) with \(D\) replaced by \(p\) and an
exterior factor \(N^{-2}\). The four bracket terms have coefficients
\(1,-3,-1,3\); \(|p|\ge |j|/(2N)\) gives respectively
\(4,24,8,48\) in (22) after using \(N<|j|/R\) in the last
three terms. Differentiating \((A'/D^2-AD'/D^3)\) directly also
reproduces the bracket, including its signs.

The Fourier moment constant in (17) is independently read as
\(\int_{-1}^1\xi^2d\xi=2/3\) and
\(2/(2\pi)^4=1/(8\pi^4)\). The array rate has the correct
dimension: \(O(N)\) entries of squared error \(O(N^{-3})\)
give \(O(N^{-2})\), while the squared exterior tail is
\(O(N^{-3})\). Its square root is \(O(N^{-1})\), as in (24).

## Scope and relation to the source

The exact coefficients and leading array are those in the passage
section of **OpenAI**, *A smooth three-torus diffeomorphism with simple
Lebesgue spectrum*, September 23, 2026. The
[citation README](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/README.md)
and [passage section](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/02-passages.tex)
were opened. No arXiv identifier was located. The source already states
qualitative convergence of the summed array. The result here supplies
a full fixed-data proof with a rate and cutoff consequences; no
historical novelty is claimed for stationary phase.

For a finite list of packets, apply (4), (29), (30) and (33) to each
packet and add the finitely many bounds. There is no dependence on
future choices in this assertion. The coefficient result itself does
not require the gap around zero; the retained nonzero-index and residue
statements do. If \(A=0\), all arrays and errors vanish directly.

This result does not audit physical smooth closeness together with
support tracking for a sequence of passages, index-signal transmission,
or the limiting cyclic-basis construction. It does not prove the
existence of a probability-preserving transformation with simple
Lebesgue spectrum.
