# Midpoint curvature and a local collar for the candidate boundary

These are statements about the analytic candidate formulas. They do not
prove a limit theorem for the six-vertex model.

## Definitions

Let
\[
0<\gamma<\pi/2,\qquad \delta=\pi-\gamma,\qquad
\gamma\leq u<\delta,\qquad T=\delta-u,\qquad h=\pi/\delta.
\]
In particular \(h>1\) and \(0<hT<\pi\). For \(|\theta|<T\), define
\[
\begin{split}
a(\theta)&=\frac{\sin\gamma}{2\pi(\cos(\theta-u)+\cos\gamma)},\\
b(\theta)&=\frac{\sin\gamma}{2\pi(\cos(\theta+u)+\cos\gamma)},\\
e(\theta)&=\frac{\sin T}{2\pi(\cos\theta-\cos T)}
 -\frac{h\sin(hT)}{2\pi(\cos(h\theta)-\cos(hT))}.
\end{split}                                                    \tag{1}
\]
These are the coefficients in Alexey Bufetov,
[*Limit shape for domain-wall six-vertex model*,
arXiv:2609.20576v1](https://arxiv.org/html/2609.20576v1),
equations (4.3) and (4.6), continued by definition beyond the announced
theorem's range. Set
\[
W=ab'-a'b,\qquad
X_0(\theta)=(x_0,y_0)
=\left(\frac{eb'-e'b}{W},\frac{ae'-a'e}{W}\right),
\]
\[
C(\theta)=x_0a''+y_0b''-e'',\qquad
D(\theta)=x_0a'''+y_0b'''-e'''.
                                                               \tag{2}
\]
The coordinates \(x_0,y_0\) in the last two expressions multiply the
indicated derivatives; they are not differentiated there.

Write \(\alpha=a(0)=b(0)>0\) and \(p=b'(0)=-a'(0)>0\).
The envelope equations and evenness imply
\[
X_0(0)=\left(\frac{e(0)}{2\alpha},
                   \frac{e(0)}{2\alpha}\right),\qquad
C(0)=e(0)\frac{a''(0)}{\alpha}-e''(0),\qquad D(0)=0.
                                                               \tag{3}
\]
The denominator in (1) is positive on its stated domain. Also \(W>0\):
the logarithmic derivative of \(A(it)=\sin\gamma/
[2\pi(\cos t+\cos\gamma)]\) is
\[
g(t)=\frac{\sin t}{\cos t+\cos\gamma},\qquad
g'(t)=\frac{1+\cos\gamma\cos t}{(\cos t+\cos\gamma)^2}>0,
\]
and therefore \(W=ab[g(\theta+u)-g(\theta-u)]>0\).

## The sign theorem

**Proposition.** For the parameters above, \(C(0)>0\). Consequently
\(C(\theta)>0\) on some open interval about zero. When
\(0<\gamma<\pi/3\), this includes equal weights
\(u=T=\delta/2\), and also every \(\gamma\leq u<\delta\).

**Proof.** Put
\[
z=T/2,\quad q=\frac1{1-\cos T},\quad
q_h=\frac1{1-\cos(hT)},\quad
R=\frac{a''(0)}{\alpha},\quad E=\cot z-h\cot(hz).
\]
Since \(0<z<hz<\pi/2\), all the cotangents here are positive.
Direct evaluation and twice differentiating (1) give
\[
2\pi e(0)=E,\qquad
2\pi e''(0)=\cot z\,q-h^3\cot(hz)\,q_h .
\]
Substitution in (3) gives the exact identity
\[
2\pi C(0)=E(R-q)+h\cot(hz)(h^2q_h-q).                         \tag{4}
\]

Both \(E\) and \(h^2q_h-q\) are strictly positive. Indeed,
\[
\frac{d}{dt}(t\cot t)
=\frac{\sin t\cos t-t}{\sin^2t}<0\qquad(0<t<\pi/2).
\]
The numerator is negative because
\((t-\sin t\cos t)'=2\sin^2t>0\), with value zero at \(t=0\).
Thus \(z\cot z>hz\cot(hz)\), which proves \(E>0\).
Likewise
\[
\frac{d}{dt}\frac{\sin t}{t}=\frac{t\cos t-\sin t}{t^2}<0,
\]
as \((\sin t-t\cos t)'=t\sin t>0\). It follows that
\(\sin(hz)<h\sin z\), and hence
\[
h^2q_h-q=\frac12\left(\frac{h^2}{\sin^2(hz)}
                         -\frac1{\sin^2z}\right)>0.            \tag{5}
\]

It remains to check \(R-q\geq0\). Put
\[
v=(\gamma+u)/2,\qquad w=(\gamma-u)/2.
\]
Here \(0<v<\pi/2\), \(-\pi/2<w\leq0\), and
\(T=\pi-2v\), so \(q=\tfrac12\sec^2v\).
Factoring
\(\cos t+\cos\gamma=
2\cos((t+\gamma)/2)\cos((t-\gamma)/2)\)
and differentiating its reciprocal logarithmically gives
\[
R=\frac14(\sec^2v+\sec^2w)
       +\frac14(\tan v-\tan w)^2
 =\frac12(1+\tan^2v+\tan^2w-\tan v\tan w).
\]
Therefore
\[
R-q=\frac12\tan w(\tan w-\tan v)\geq0.                        \tag{6}
\]
For \(u>\gamma\) both factors in the product are negative.
At \(u=\gamma\) its value is zero. Equations (4)–(6) prove
\[
C(0)\ \geq\
\frac{h\cot(hT/2)}{2\pi}
\left(\frac{h^2}{1-\cos(hT)}-\frac1{1-\cos T}\right)>0.         \tag{7}
\]
The functions in (1)–(2) are analytic in the strict parameter domain,
so continuity supplies an interval on which \(C(\theta)>0\).
Finally \(u=\delta/2\geq\gamma\) exactly when
\(\gamma\leq\pi/3\). This proves the assertion. \(\square\)

## The local critical branch

For precision, the branch used below is defined as follows. On
\([-B,B]\), let
\[
k(s)=\frac{\sin(2\gamma)}
 {2\pi(\cosh s-\cos(2\gamma))},\quad
(K_Bf)(s)=\int_{-B}^{B}k(s-t)f(t)\,dt,\quad
\rho_B=(I-K_B)^{-1}1.
\]
Let
\[
A(z)=\frac{\sin\gamma}{2\pi(\cosh z+\cos\gamma)},\qquad
L(z)=\frac{\sin T}{2\pi(\cosh z-\cos T)}
 -\frac{h\sin(hT)}{2\pi(\cosh(hz)-\cos(hT))},
\]
\[
F(s;x,y,\theta)=xA(s+i(\theta-u))
              +yA(s+i(\theta+u))-L(s+i\theta),\qquad
\Phi=\int_{-B}^{B}F(s;x,y,\theta)\rho_B(s)\,ds.               \tag{8}
\]
The critical branch is the solution \(X(B,\theta)=(x,y)\) of
\(\Phi_B=\Phi_\theta=0\) for fixed \(B,\theta\).
The needed local facts can be established directly. Set \(t=e^s\).
Since \(0<2\gamma<\pi\),
\[
\int_{\mathbb R}|k(s)|\,ds
=\frac{\sin(2\gamma)}{\pi}
 \int_0^\infty\frac{dt}{(t-\cos(2\gamma))^2+\sin^2(2\gamma)}
=\frac{\pi-2\gamma}{\pi}<1.
\]
For the last equality the antiderivative is
\(\arctan((t-\cos(2\gamma))/\sin(2\gamma))/\sin(2\gamma)\);
its lower-end angle is \(2\gamma-\pi/2\).
The row-integral bound and the Neumann series give invertibility.
After rescaling to \([-1,1]\), its kernel is
\(B k(B(r-t))\), analytic in \(B\) near zero with norm \(O(|B|)\).
Its Neumann series defines an even analytic density.

For \(F_j=\partial_s^jF(0;x,y,\theta)\), its moments give
\[
\Phi=M_0F_0+\tfrac12 M_2F_2+O(B^5),\qquad
M_0=2B+O(B^2),\quad M_2=2B^3/3+O(B^4).
\]
All remainders here are analytic in \(B\) and locally uniform with
parameter derivatives. The equations \(\Phi_B/M_0'=0\) and
\(\Phi_\theta/M_0=0\), with the second extended at zero, have at
\(B=0\) coefficient matrix
\(\left(\begin{smallmatrix}a&b\\a'&b'\end{smallmatrix}\right)\).
Its determinant is \(W>0\). Analytic inversion therefore gives
a unique local analytic \(X(B,\theta)\). Its linear term in \(B\)
vanishes. Since \(F_2=-\partial_\theta^2F_0\),
\[
X(B,\theta)=X_0(\theta)+B^2V(\theta)+O(B^3),\qquad
aV_x+bV_y=C/2,\quad a'V_x+b'V_y=D/6.                       \tag{9}
\]
At the midpoint (3) yields
\[
V(0)=\frac{C(0)}{4\alpha}(1,1).                            \tag{10}
\]

## Which side the branch enters

**Corollary.** Near \(X_0(0)\), the candidate envelope is a regular,
strictly convex graph. The branch (8) enters its northeast, locally
convex side. It parametrizes a neighborhood on that side one-to-one
for small \(B>0\) and small \(|\theta|\). This is uniqueness among
these local critical parameters, not among all possible critical points.

**Proof.** Differentiating the envelope equations
\(ax_0+by_0=e\) and \(a'x_0+b'y_0=e'\) gives
\[
a x_0'+b y_0'=0,\qquad a'x_0'+b'y_0'=-C.
\]
Consequently
\[
X_0'=\frac C W(b,-a),\qquad
X_0'(0)=\frac{C(0)}{2p}(1,-1).                             \tag{11}
\]
The latter vector is nonzero. Differentiating the first of these
linear equations once more gives
\[
\alpha(x_0''(0)+y_0''(0))=C(0).                            \tag{12}
\]
Use the orthogonal coordinates \(r=(x-y)/\sqrt2\) and
\(s=(x+y)/\sqrt2\). At the midpoint,
\[
r_0'=\frac{C(0)}{\sqrt2 p}>0,\quad s_0'=0,\quad
s_0''=\frac{C(0)}{\sqrt2\alpha}>0.
\]
Thus the envelope is locally \(s=f(r)\), with
\[
f'(0)=0,\qquad f''(0)=\frac{\sqrt2 p^2}{\alpha C(0)}>0,     \tag{13}
\]
where \(r_0(0)=0\). Shrinking the neighborhood makes \(f''>0\).
Its locally convex side means \(s>f(r)\); it is the northeast side
at the midpoint.

To prove both the side assertion and one-to-one parametrization,
introduce \(t=B^2\). Analyticity in (9) writes the branch as
\[
Y(t,\theta)=X_0(\theta)+tV(\theta)
                         +t^{3/2}R_*(\sqrt t,\theta)
\qquad(t\geq0),                                           \tag{14}
\]
where \(R_*\) is analytic near \(B=\theta=0\). Extend this map for
\(t<0\) by \(Y(t,\theta)=X_0(\theta)+tV(\theta)\).
This extension is \(C^1\): the remainder and its \(t,\theta\)
derivatives tend to zero at \(t=0\). Equations (9) and (11) give
\[
\det[V,X_0']=-\frac C W(aV_x+bV_y)
             =-\frac{C^2}{2W}<0                           \tag{15}
\]
at the midpoint and nearby. The inverse function theorem applies
to (14) at \((0,0)\); it is a \(C^1\) diffeomorphism between
two neighborhoods.

Let \(G(x,y)=s-f(r)\). Along the envelope its gradient is a positive
multiple of \((a,b)\): this vector is normal by (11), and its
northeast component is positive. Hence on \(t=0\)
\[
\partial_t G(Y(t,\theta))\big|_{t=0}
       =\lambda(\theta)(aV_x+bV_y)
       =\lambda(\theta)C(\theta)/2>0
\]
for some positive continuous \(\lambda\).
Continuity makes this derivative positive throughout a sufficiently
small rectangle in \((t,\theta)\). Integrating it from zero shows
\(G(Y(t,\theta))\) has the sign of \(t\).
The diffeomorphism therefore maps \(t>0\) precisely to the
\(G>0\) part of its image neighborhood. As \(B\mapsto t=B^2\)
is one-to-one for \(B>0\), the claimed uniqueness follows.
At \(\theta=0\), (10) explicitly gives the positive displacement
\[
x(B,0)=y(B,0)
 =\frac{e(0)}{2\alpha}+\frac{C(0)}{4\alpha}B^2+O(B^3).
\]
Here exact equality of the coordinates follows from symmetry:
exchanging \(x,y\) and sending \(\theta\) to \(-\theta\) preserves
the critical equations, and the local solution is unique.
\(\square\)

## Scope

The weight condition \(u\geq\gamma\) is sufficient for (6); the proof
does not decide the sign of \(C\) when \(u<\gamma\), or at arbitrary
nonzero boundary parameter. The neighborhoods depend on \(\gamma,u\).
No uniform claim is made as a pole or a regime endpoint is approached.
The convex side proved here belongs to the local candidate curve.
Identifying it with a liquid region of the random six-vertex model,
and proving convergence to the candidate boundary, remain separate
problems. The antiferroelectric regime is not considered.

A reformulation for extending the sign argument is available. Set
\(r=b/a\) and \(H=e/a\). Since \(r'=W/a^2>0\), \(r\) is a local
coordinate. The envelope equations become
\(x_0+r y_0=H\) and \(r'y_0=H'\). At a fixed envelope point,
differentiating \(a(x_0+r y_0-H)\) twice, with \(x_0,y_0\) fixed,
therefore gives
\[
C=a(r''y_0-H'')
  =-a(r')^2\frac{d^2H}{dr^2}.
\]
Strict concavity of \(H\) as a function of \(r\) is thus equivalent
to the desired sign.
