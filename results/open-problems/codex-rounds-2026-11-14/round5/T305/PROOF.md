# Energy error for a compact perturbation of a Gaussian

Let \(R>0\), \(0\le a<1\), \(M\ge0\), and \(T_*>0\) be fixed.
In every dimension \(d\ge1\), suppose \(U\in C^2(\mathbb R^d)\) satisfies
\[
 U(x)=0\quad (|x|\ge R),\qquad
 \|\nabla^2U(x)\|_{\rm op}\le a,\qquad
 \|\nabla^2U(x)-\nabla^2U(y)\|_{\rm op}\le M|x-y|.
 \tag{1}
\]
Set
\[
 V(x)=|x|^2/2+U(x),\quad H(x,p)=V(x)+|p|^2/2,
 \quad \rho=\pi\otimes N(0,I_d),\quad \pi\propto e^{-V}.
\]
Let \(S=\Psi_h^n\) be kick–drift–kick leapfrog, where
\(0<h\le1\), \(n\ge1\), and \(nh\le T_*\), and write
\[
 \Delta(z)=H(Sz)-H(z).
\]
These are the errors of the proposals before a Metropolis decision.

There are constants \(C,C_t,K\), depending only on \(R,a,M,T_*\), such that
\[
 E_\rho\Delta^2\le C\{dh^4+(dh^4)^2\}.
 \tag{2}
\]
Consequently, whenever \(dh^4\le1\),
\[
 0\le D_{\rm KL}(S_\#\rho\|\rho)=E_\rho\Delta\le Cdh^4.
 \tag{3}
\]
For every \(M_0\)-warm position law \(\nu\le M_0\pi\), independently
refreshed standard Gaussian momentum, and \(0<\delta<1\), put
\[
 s=\log(KM_0/\delta).
\]
Then
\[
 \Pr_{\nu\otimes N(0,I)}\left\{
 |\Delta|>\frac{dh^4}{24}
              +C_t h^2\bigl(\sqrt{ds}+s^{3/2}\bigr)\right\}
 \le\delta.
 \tag{4}
\]
In particular, a fixed small average rejection is obtained with a
reciprocal step size of order
\[
 d^{1/4}s^{1/4}+s^{3/4}.
 \tag{5}
\]
This statement controls one proposal. It is not a mixing theorem.

## 1. Density comparison and a deterministic error bound

For \(|x|<R\), choose a point \(y\) on the boundary of the ball on the
ray through \(x\). At \(x=0\), any ray suffices. Then \(|x-y|\le R\),
and \(U(y)=0\), \(\nabla U(y)=0\), by (1) and continuity. Taylor's
formula with an integral remainder gives
\[
 |\nabla U(x)|\le aR,\qquad |U(x)|\le aR^2/2=:B.
 \tag{6}
\]
These bounds hold outside the ball as well. If \(\gamma_d=N(0,I_d)\)
and \(\Gamma=\gamma_d\otimes\gamma_d\), then
\[
 e^{-2B}\le\frac{d\pi}{d\gamma_d}\le e^{2B},\qquad
 \rho\le e^{2B}\Gamma.
 \tag{7}
\]
Also \( (1-a)I\preceq\nabla^2V\preceq(1+a)I\). Put
\[
 G=1+aR,\quad L=1+a,\quad c_v=1+G/2,
 \quad W(x,p)=\sqrt{1+|x|^2+|p|^2}.
\]
Thus \(|\nabla V(x)|\le |x|+aR\le G\sqrt{1+|x|^2}\).

For one step, write \(g=\nabla V\) and
\[
 v=p-hg(x)/2,\qquad q=x+hv,\qquad p'=v-hg(q)/2.
\]
Expanding the kinetic energies proves the exact identity
\[
 \begin{split}
 H(q,p')-H(x,p)
 &=V(q)-V(x)-\tfrac12(q-x)\cdot(g(q)+g(x))\\
 &\quad+\tfrac{h^2}{8}(|g(q)|^2-|g(x)|^2).
 \end{split}
 \tag{8}
\]
For \(r=q-x\), \(f(t)=V(x+tr)\), integration by parts twice gives
\[
 \begin{split}
 f(1)-f(0)-\tfrac12(f'(1)+f'(0))
 &=\int_0^1(1/2-t)f''(t)\,dt\\
 &=-\tfrac12\int_0^1t(1-t)f'''(t)\,dt.
 \end{split}
 \tag{9}
\]
Here (f'') is Lipschitz, hence absolutely continuous, and its derivative
exists almost everywhere with absolute value at most \(M|r|^3\).
Since \(\int_0^1t(1-t)dt=1/6\), the defect in (9) is at most
\(M|r|^3/12\). No fourth derivative is used.

For \(h\le1\),
\[
 |v|\le c_vW,\quad
 \sqrt{1+|q|^2}\le(1+c_v)W,\quad
 |g(q)|+|g(x)|\le G(2+c_v)W.
\]
Using \(|g(q)-g(x)|\le Lh|v|\) in (8), and \(W\ge1\), proves
\[
 |H(q,p')-H(x,p)|\le b h^3W^3,
 \quad b=\frac{Mc_v^3}{12}+\frac{LGc_v(2+c_v)}8.
 \tag{10}
\]
A half kick increases the norm \(W\) by at most a factor \(1+hG/2\);
a drift increases it by at most \(1+h\). This follows by viewing
((1,x,p)) as an augmented Euclidean vector and applying the triangle
inequality. At every mesh point \(jh\le T_*\), therefore,
\[
 W_j\le e^{(G+1)T_*}W_0.
\]
Sum (10) over \(n\) steps to obtain the global deterministic estimate
\[
 |\Delta(z)|\le D h^2 W(z)^3,
 \qquad D=T_* b e^{3(G+1)T_*}.
 \tag{11}
\]
Its constants are independent of \(d\).

## 2. A Gaussian path avoids the perturbation except on a small event

Let \(S_G\) denote leapfrog for the unperturbed Hamiltonian
\(H_G(x,p)=(|x|^2+|p|^2)/2\). Put
\[
 \alpha=h^2/4,\quad r_h=\sqrt{1-\alpha},
 \quad\theta=2\arcsin(h/2).
\]
Direct multiplication of the two half kicks and the drift, followed by
the angle addition identities, gives
\[
 x_j^G=\cos(j\theta)x+\frac{\sin(j\theta)}{r_h}p,
 \quad
 p_j^G=-r_h\sin(j\theta)x+\cos(j\theta)p.
 \tag{12}
\]
Let \(Z=[x\ p]\) be the \(d\)-by-\(2\) matrix with these columns, and
let \(\sigma_{\min}(Z)=\inf_{|u|=1}|Zu|\). The coefficient vector in
the formula for \(x_j^G\) has squared norm
\[
 \cos^2(j\theta)+\sin^2(j\theta)/r_h^2\ge1.
\]
Consequently,
\[
 |x_j^G|\ge\sigma_{\min}(Z)\quad\hbox{for every integer }j.
 \tag{13}
\]
For \(d=1\), this minimum singular value is zero; the statement remains
valid. Define
\[
 \mathcal E=\{\sigma_{\min}([x\ p])\le R\}.
\]
On \(\mathcal E^c\), all Gaussian mesh positions lie outside the ball.
Induction over the leapfrog steps shows that the perturbed and Gaussian
positions and momenta are identical: at every force evaluation
\(\nabla U=0\). Also \(U=0\) at both initial and final positions. Hence
\[
 \Delta(z)=\Delta_G(z):=H_G(S_Gz)-H_G(z)
 \quad\hbox{on }\mathcal E^c.
 \tag{14}
\]
Nothing is asserted about the line segments between mesh positions.
Only endpoint force evaluations enter leapfrog. In particular, this
comparison has no union factor \(n\).

Here is an elementary probability bound under \(\Gamma\). The Gram
matrix \(Z^TZ\) satisfies
\[
 \lambda_{\min}(Z^TZ)
 \ge\min(|x|^2,|p|^2)-|x\cdot p|.
 \tag{15}
\]
This follows by evaluating its quadratic form and using
\(2|u_1u_2|\le u_1^2+u_2^2\). If \(|x|^2,|p|^2\ge d/2\) and
\(|x\cdot p|\le d/4\), its smallest eigenvalue is at least \(d/4\).

For \(X\sim\gamma_d\), Gaussian integration gives
\(E e^{-|X|^2/2}=2^{-d/2}\). Markov's inequality implies
\[
 \Pr\{|X|^2<d/2\}\le
 \exp\{-c_0d\},\qquad c_0=\tfrac12\log2-\tfrac14.
 \tag{16}
\]
For independent \(X,P\sim\gamma_d\), condition on \(X\) to get
\[
 E e^{tX\cdot P}=E e^{t^2|X|^2/2}=(1-t^2)^{-d/2},\quad |t|<1.
\]
Using \(t=1/4\) for each sign gives
\[
 \Pr\{|X\cdot P|>d/4\}\le2e^{-cd},
 \quad c=\frac1{16}+\frac12\log(15/16)>0.
 \tag{17}
\]
In fact \(c<c_0\). Positivity follows, for example, from
\(\log(1-u)\ge-u/(1-u)\) with \(u=1/16\), which gives
\(c\ge1/16-1/30>0\).

Let
\[
 d_0=1+\lceil4R^2\rceil,\qquad K_R=4e^{cd_0}.
 \tag{18}
\]
If \(d\ge d_0\), (15)–(17) give
\(\Gamma(\mathcal E)\le4e^{-cd}\). For \(d<d_0\), use the bound
one. Together these prove, for all \(d\ge1\),
\[
 \Gamma(\mathcal E)\le \min(1,K_R e^{-cd}).
 \tag{19}
\]

## 3. Gaussian energy-error moments

The matrix in (12) preserves \(r_h^2x^2+p^2\) coordinatewise. Thus
\[
 \Delta_G^{(i)}=\frac\alpha2\{(x_n^{G,i})^2-x_i^2\}.
 \tag{20}
\]
For \(\phi=n\theta\), each coordinate pair under \(\Gamma\) consists
of independent standard normals, so
\[
 \mu_1:=E_\Gamma\Delta_G^{(i)}
 =\frac{\alpha^2\sin^2\phi}{2(1-\alpha)}
 \le h^4/24.
 \tag{21}
\]
For completeness, write \(v=(\cos\phi,\sin\phi/r_h)^T\) and
\[
 E_1=\frac\alpha2(vv^T-e_1e_1^T).
\]
Then \(\Delta_G^{(i)}=u_i^TE_1u_i\) and
\(\operatorname{tr}E_1=\mu_1\). The determinant formula for the
difference of these two rank-one matrices gives
\[
 \det E_1=-\frac{\alpha^2\sin^2\phi}{4(1-\alpha)}
 =-\mu_1/2.
\]
Wick's fourth-moment formula therefore gives
\[
 \operatorname{Var}(\Delta_G^{(i)})
 =2\operatorname{tr}(E_1^2)
 =2\{(\operatorname{tr}E_1)^2-2\det E_1\}
 =2\mu_1+2\mu_1^2.
 \tag{22}
\]
The coordinate pairs are independent under \(\Gamma\). It follows that
\[
 E_\Gamma\Delta_G^2
 =2d\mu_1+(d^2+2d)\mu_1^2
 \le\frac{dh^4}{12}+\frac{d^2h^8}{192}.
 \tag{23}
\]

## 4. The exceptional set contributes only \(O(dh^4)\)

Under \(\Gamma\), \(W^2=1+Y\), where \(Y\) has a chi-squared law with
(2d) degrees of freedom. Its integer moments are
\(E Y^k=2^k(d)_k\), where \((d)_k=d(d+1)\cdots(d+k-1)\) and
\((d)_0=1\). Expanding \(W^{12}=(1+Y)^6\) gives
\[
 E_\Gamma W^{12}
 =\sum_{k=0}^6\binom6k2^k(d)_k
 \le(2d+11)^6.
 \tag{24}
\]
Indeed \((d)_k\le(d+5)^k\) for \(0\le k\le6\). By Cauchy–Schwarz,
(19), and (24),
\[
 E_\Gamma[W^6\mathbf1_{\mathcal E}]
 \le(2d+11)^3\sqrt{K_R}\,e^{-cd/2}
 \le A_R d,
 \tag{25}
\]
where one possible finite constant is
\[
 A_R=13^3\sqrt{K_R}\,\frac{16}{c^2e^2}.
 \tag{26}
\]
For the last inequality, use \(2d+11\le13d\) and maximize
\(u^2e^{-cu/2}\) over \(u\ge0\); its maximum is
\(16/(c^2e^2)\), attained at \(u=4/c\).

Split the error at \(\mathcal E\). Equations (7), (11), (14), (23),
and (25) give
\[
 \begin{split}
 E_\rho\Delta^2
 &\le e^{2B}\left\{E_\Gamma\Delta_G^2
                  +D^2h^4E_\Gamma[W^6\mathbf1_{\mathcal E}]\right\}\\
 &\le e^{2B}\left\{(1/12+D^2A_R)dh^4+d^2h^8/192\right\}.
 \end{split}
 \tag{27}
\]
This proves (2) with explicit dimension-independent constants. They are
conservative and may be large.

To obtain (3), let \(J(x,p)=(x,-p)\). Leapfrog is a global
volume-preserving diffeomorphism, \(JSJ=S^{-1}\), and \(H\circ J=H\).
Thus \(F=JS\) is a volume-preserving involution and
\(\Delta(Fz)=-\Delta(z)\). A change of variables proves
\[
 E_\rho f(\Delta)=E_\rho[e^{-\Delta}f(-\Delta)]
 \tag{28}
\]
for nonnegative measurable \(f\). Polynomial moments of \(\Delta\) are
finite by (11). Applying (28) to absolute powers also justifies the
signed identities used next. Since
\[
 t(1-e^{-t})\le\tfrac12 t^2(1+e^{-t}),
\]
which is equivalent to \(|\tanh(t/2)|\le|t|/2\), (28) yields
\[
 E_\rho\Delta
 =\tfrac12 E_\rho[\Delta(1-e^{-\Delta})]
 \le\tfrac12 E_\rho\Delta^2.
 \tag{29}
\]
Finally, volume preservation implies
\[
 D_{\rm KL}(S_\#\rho\|\rho)
 =E_\rho\log\frac{e^{-H(Z)}}{e^{-H(SZ)}}=E_\rho\Delta\ge0.
 \tag{30}
\]
Combine (27)–(30) and \(dh^4\le1\).

## 5. Warm tails, including warm starts concentrated in the ball

Let \(E_G\) be the block diagonal matrix with the \(d\) blocks \(E_1\).
Since \(|v|^2\le4/3\) and \(\alpha=h^2/4\),
\[
 \|E_G\|_{\rm op}\le\frac{7h^2}{24}\le\frac{h^2}3,
 \quad \|E_G\|_F^2\le\frac{2dh^4}9.
\]
If \(Q=u^TE_Gu\) for a standard Gaussian \(u\in\mathbb R^{2d}\),
diagonalization and one-dimensional Gaussian integration give
\[
 \log E e^{t(Q-EQ)}
 =\sum_i\{-\tfrac12\log(1-2t\lambda_i)-t\lambda_i\}
 \le\frac{t^2\|E_G\|_F^2}{1-2|t|\|E_G\|_{\rm op}}.
\]
The bound follows by expanding the logarithm and summing absolute values
of its terms of order at least two. For \(s>0\), substitute
\[
 t=\frac{\sqrt s}{\|E_G\|_F+2\|E_G\|_{\rm op}\sqrt s}
\]
in Chernoff's inequality, for both signs. The resulting exponent is
exactly \(s\) at the threshold
\(2\|E_G\|_F\sqrt s+2\|E_G\|_{\rm op}s\). If \(E_G=0\), the result
is immediate without this substitution. Thus, since \(2\sqrt2/3<1\),
\[
 \Gamma\{|\Delta_G-d\mu_1|>h^2(\sqrt{ds}+s)\}\le2e^{-s}.
 \tag{31}
\]
Also \(E_\Gamma e^{Y/4}=2^d\), and Markov's inequality gives
\[
 \Gamma\{Y>4(d+s)\}\le e^{-(1-\log2)d-s}\le e^{-s}.
\]
On the complementary event,
\[
 W^2\le1+4(d+s)\le5(d+s),\qquad d\ge1.
 \tag{32}
\]

The warm phase-space law \(\lambda=\nu\otimes\gamma_d\) obeys
\(\lambda\le M_0 e^{2B}\Gamma\). Choose
\[
 K=3K_R e^{2B},\qquad s=\log(KM_0/\delta)>1.
 \tag{33}
\]
If \(s<cd\), then
\[
 \lambda(\mathcal E)\le M_0e^{2B}K_Re^{-cd}
 =\frac\delta3 e^{s-cd}\le\delta/3.
\]
Outside \(\mathcal E\), use (14) and (31). Its additional exceptional
probability under \(\lambda\) is at most
\(2M_0e^{2B}e^{-s}=2\delta/(3K_R)\). Hence, with failure probability
less than \(\delta\),
\[
 |\Delta|\le dh^4/24+h^2(\sqrt{ds}+s)
 \le dh^4/24+h^2(\sqrt{ds}+s^{3/2}).
 \tag{34}
\]
If \(s\ge cd\), then \(d\le s/c\). Use (11) and (32), with failure
probability at most \(M_0e^{2B}e^{-s}=\delta/(3K_R)\), to get
\[
 |\Delta|\le D h^2[5(1+1/c)s]^{3/2}.
 \tag{35}
\]
This second case is necessary: an arbitrarily warm start can concentrate
inside the perturbation ball, so its exceptional probability cannot
always be discarded. Equations (34)–(35) prove (4), for example with
\[
 C_t=\max\{1,D[5(1+1/c)]^{3/2}\}.
\]
The estimate is for the absolute energy error, with no change of center
to a mean under the warm law.

For fixed \(\eta>0\), it suffices to impose
\[
 h\le1,\quad
 h\le(8\eta/d)^{1/4},\quad
 h\le\left(\frac{\eta}{3C_t\sqrt{ds}}\right)^{1/2},\quad
 h\le\left(\frac{\eta}{3C_t s^{3/2}}\right)^{1/2}.
 \tag{36}
\]
The threshold in (4) is then at most \(\eta\). The conditional rejection
probability is \((1-e^{-\Delta})_+\le\min(1,\Delta_+)\), so its average
is at most \(\eta+\delta\). Since \(s>1\), (36) gives (5).
For a fixed integration time \(T\le T_*\), take \(n=\lceil T/h_*\rceil\)
and use the actual step \(h=T/n\le h_*\), where \(h_*\) is the minimum
of the four bounds. This changes the number of steps only by rounding.

## 6. An explicit family outside dimension-independent Frobenius regularity

Take \(R=1\), \(\gamma=1/24\), and, in every dimension, define
\[
 U_d(x)=\gamma(1-|x|^2)_+^3,
 \qquad V_d(x)=|x|^2/2+U_d(x).
 \tag{37}
\]
This is a radial, coupled perturbation; it is \(C^2\) with a globally
Lipschitz Hessian. For \(|x|<1\), write \(r=|x|\), \(s=r^2\). Direct
differentiation gives
\[
 \nabla^2U_d(x)=-6\gamma(1-s)^2I
                       +24\gamma(1-s)xx^T.
 \tag{38}
\]
The tangential eigenvalue is \(-6\gamma(1-s)^2\), in \([-6\gamma,0]\).
The radial eigenvalue is
\[
 \gamma(-6+36s-30s^2)
 =\gamma\{24/5-30(s-3/5)^2\},
\]
in \([-6\gamma,24\gamma/5]\) on \(0\le s\le1\). Outside the ball
the Hessian vanishes, and it tends to zero at the boundary. Thus
\[
 \|\nabla^2U_d\|_{\rm op}\le6\gamma=1/4,
 \quad \tfrac34 I\preceq\nabla^2V_d\preceq\tfrac54 I.
 \tag{39}
\]
For a unit vector \(w\), differentiation inside the ball gives
\[
 D_w\nabla^2U_d
 =24\gamma(1-r^2)\{(x\cdot w)I+wx^T+xw^T\}
       -48\gamma(x\cdot w)xx^T.
 \tag{40}
\]
Its operator norm is at most
\[
 72\gamma r(1-r^2)+48\gamma r^3
 =24\gamma(3r-r^3)\le48\gamma=2.
\]
Integrate this derivative along any line segment. The Hessian is
continuous across the sphere, and the segment has at most two boundary
crossings; the same Lipschitz bound holds globally. This proves the
operator regularity in (1) with constants independent of \(d\), despite
the jump in third derivatives at the sphere.

For \(x=te_1\), \(0<t<1\), each tangential diagonal entry of (38) is
\(-6\gamma(1-t^2)^2\). Its derivative in \(t\) is
\(24\gamma t(1-t^2)\), equal to \(9\gamma=3/8\) at \(t=1/2\).
Therefore any global Frobenius-Lipschitz constant \(M_{F,d}\) must obey
\[
 M_{F,d}\ge\|D_{e_1}\nabla^2U_d(e_1/2)\|_F
 \ge\frac38\sqrt{d-1}.
 \tag{41}
\]
Thus (2)–(4) apply to a family to which a theorem requiring a
dimension-independent Frobenius-Lipschitz constant cannot be applied
directly. The source's stronger assumption is not silently recovered.

The gap also occurs for \(C^3\) potentials, so it is not an artifact of
the jump in third derivatives in (37). Take instead
\[
 \widetilde U_d(x)=\frac1{32}(1-|x|^2)_+^4.
 \tag{42}
\]
For \(\widetilde\gamma=1/32\), its tangential and radial Hessian
eigenvalues inside the ball are, respectively,
\[
 -8\widetilde\gamma(1-s)^3,
 \qquad 8\widetilde\gamma(1-s)^2(7s-1).
\]
The latter has minimum \(-8\widetilde\gamma\) and maximum
\(256\widetilde\gamma/49\), attained at \(s=0\) and \(s=3/7\).
Thus its Hessian norm is at most \(1/4\). Differentiating its Hessian as
in (40) bounds the directional operator derivative by
\[
 144\widetilde\gamma r(1-r^2)^2
       +192\widetilde\gamma r^3(1-r^2)
 =48\widetilde\gamma r(1-r^2)(3+r^2)
 \le96\widetilde\gamma=3.
\]
Here \(r(1-r^2)\le1/2\) on ([0,1]). Its third derivatives vanish
continuously at the sphere. The derivative of each tangential Hessian
entry along \(te_1\), evaluated at \(t=1/2\), is
\(48\widetilde\gamma t(1-t^2)^2=27/64\). Therefore this \(C^3\) family
has the same spectral bounds, an operator-Lipschitz constant at most 3,
and Frobenius-Lipschitz constant at least
\((27/64)\sqrt{d-1}\). It also satisfies (2)–(4).

## 7. Scope of the conclusion

The compact support and fixed radius in (1) are essential to the
avoidance estimate. Almost all high-dimensional Gaussian trajectories
miss this ball, uniformly in the number of leapfrog steps. The proof
does not control a nonquadratic Hessian throughout the typical shell
\(|x|\asymp\sqrt d\). Its constants are not uniform if \(R\) grows with
dimension. In particular it does not establish (2) under the full
assumptions of T305.

There is no proposal-overlap or conductance argument here. An energy
tail and constant acceptance alone do not establish the total-variation
mixing bound in the question, and (37) is not a lower-bound example.
