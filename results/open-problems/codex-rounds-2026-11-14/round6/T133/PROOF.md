# Completion of the candidate curve at Delta = 1/sqrt(2)

These are deterministic statements about the candidate formulas. No
convergence theorem for the six-vertex measure is asserted.

## Definitions and result

Fix
\[
\gamma=\pi/4,\qquad \delta=3\pi/4,\qquad h=4/3,
\qquad 0<u<\delta,\qquad T=\delta-u.
\]
For \(|\theta|<T\), set
\[
\begin{split}
a(\theta)&=\frac{\sin\gamma}{2\pi(\cos(\theta-u)+\cos\gamma)},\\
b(\theta)&=\frac{\sin\gamma}{2\pi(\cos(\theta+u)+\cos\gamma)},\\
e(\theta)&=\frac1{2\pi}\left[
 \frac{\sin T}{\cos\theta-\cos T}
 -\frac{h\sin(hT)}{\cos(h\theta)-\cos(hT)}\right],\\
W&=ab'-a'b,\\
\Gamma_u(\theta)=(x_u,y_u)&=
\left(\frac{eb'-e'b}{W},\frac{ae'-a'e}{W}\right).
\end{split}                                                     \tag{1}
\]
For \(\Gamma_T\), exchange \(u,T\) in this definition. Define four
arcs by taking the closures of
\[
\Gamma_{\rm SW}=\Gamma_u,\quad
\Gamma_{\rm SE}=(1-x_T,y_T),\quad
\Gamma_{\rm NE}=(1-x_u,1-y_u),\quad
\Gamma_{\rm NW}=(x_T,1-y_T).                                    \tag{2}
\]
The formulas are those of Alexey Bufetov,
[*Limit shape for domain-wall six-vertex model*, arXiv:2609.20576v1](https://arxiv.org/html/2609.20576v1),
(4.3), (4.4), (4.6), here defined outside the parameter range of its
announced disordered theorem.

The vertex-weight ratio is \(\sin T/\sin u=\sin\delta\cot u-\cos\delta\).
Its derivative is \(-\sin\delta\csc^2u<0\), and its endpoint limits
are infinity and zero. Thus varying \(u\) covers every positive weight
ratio at this value of \(\Delta\).

**Theorem.** The union in (2) is a regular \(C^2\) simple closed curve
in the unit square. It has strictly positive geometric curvature
everywhere and bounds a strictly convex set. Its only contacts with the
square are
\[
W_0=(0,k),\quad S_0=(k,0),\quad
E_0=(1,1-k),\quad N_0=(1-k,1),                                \tag{3}
\]
where
\[
k=k(u)=\frac{\sin u\sin T}{\sin\delta}
           [\cot T-h\cot(hT)],\qquad 0<k<1.                   \tag{4}
\]
It has an injective inward normal collar of positive uniform width for
each fixed \(u\). At equal weights \(u=T=\delta/2\), the curve is
not \(C^3\) at the four contacts.

The collar in this theorem uses Euclidean normal distance. It does not
assert extension of the Fredholm critical-parameter coordinates across
the contacts.

## The open-arc input and its exact recheck

The round 5 result proves
\[
W>0,\quad C=x_ua''+y_ub''-e''>0,\qquad
\Gamma_u'=\frac C W(b,-a),\quad
\frac{d^2y_u}{dx_u^2}=\frac{W^2}{Cb^3}>0                      \tag{5}
\]
throughout the open parameter domain. Both \(a,b\) are positive.
The same holds with \(u,T\) exchanged. Thus each open arc is a
regular embedded graph with strictly monotone coordinates.

For specificity, this input was rechecked with the exact integer
certificate included here, not inferred from numerical samples.
Its rational reduction uses
\[
z=\tan((T+\theta)/6),\quad w=\tan((T-\theta)/6),
\qquad z,w>0,\quad z+w+zw<1,
\]
and
\[
A(z)=\frac{(1+z^2)^3}{2z(1-z)(3-z^2)(z^2+4z+1)},\qquad
f(z)=\frac{z(z^4+7)}{6(1-z)(1+z)(3-z^2)}.                    \tag{6}
\]
Then \(2\pi a=A(z)\), \(2\pi b=A(w)\),
\(2\pi e=f(z)+f(w)\), and differentiation in \(\theta\) is
\([(1+z^2)\partial_z-(1+w^2)\partial_w]/6\).
The numerator determining \(C\) factors into positive elementary
factors times the polynomial \(Q\) specified by
[certificate.json](certificate.json). The positive factors and the full
integer numerator identity are verified by
[audit_certificate.py](audit_certificate.py). Under
\[
z=r/(1+r),\qquad w=s/((1+s)(1+2r)),
\]
which maps \(r,s>0\) bijectively onto this domain, the polynomial
\((1+r)^{12}(1+s)^{12}(1+2r)^{12}Q(z,w)\) has zero constant term
and all 324 remaining coefficients positive, including coefficients 63
of \(r\) and \(s\). The same verifier checks every coefficient of
this substitution. This is the earlier computer-assisted sign proof;
the endpoint argument below adds no assumption about its missing boundary.

The identities for the tangent and graph curvature in (5) also follow
directly by differentiating \(ax_u+by_u=e\) and
\(a'x_u+b'y_u=e'\). In particular
\(ax_u'+by_u'=0\) and \(a'x_u'+b'y_u'=-C\), giving (5).

## Contact limits by cancellation of the poles

Define the odd function
\[
H_0(s)=\tfrac12[\cot(s/2)-h\cot(hs/2)].
\]
Its apparent singularity at zero is removable, with
\[
H_0(0)=0,\qquad H_0'(0)=(h^2-1)/12.
\]
The cotangent addition identity gives
\[
e(\theta)=\frac{H_0(T+\theta)+H_0(T-\theta)}{2\pi}.             \tag{7}
\]
Thus \(e\) is analytic at \(\theta=T\), and there
\[
e_0=\frac{\cot T-h\cot(hT)}{4\pi},\qquad
e_1=\frac{h^2\csc^2(hT)-\csc^2T-(h^2-1)/3}{8\pi}.            \tag{8}
\]
Write \(q=\theta-T\). Since \(T+u=\delta\), expansion of the
denominator of \(b\) gives
\[
b(T+q)=-\frac1{2\pi q}+\frac{\cot\delta}{4\pi}+O(q).
\]
Consequently its reciprocal \(\beta=1/b\) extends analytically with
\[
\beta(T)=0,\quad \beta'(T)=-2\pi,\quad
\beta''(T)=-2\pi\cot\delta.                                  \tag{9}
\]
Meanwhile \(a\) is analytic at \(T\), and
\[
a_0=a(T)=\frac{\sin\delta}{4\pi\sin u\sin T}>0,
\qquad
\frac{a_1}{a_0}=\frac{\cot u-\cot T}{2}.                      \tag{10}
\]
Indeed \(\cos(T-u)-\cos\delta=2\sin u\sin T\); the second
identity follows by differentiating the original denominator.

Put \(\alpha=a\beta\) and \(\eta=e\beta\). After dividing
the tangent equation by \(b\), its envelope is
\[
x_u=\frac{\eta'}{\alpha'},\qquad
y_u=\eta-\alpha\frac{\eta'}{\alpha'}.                         \tag{11}
\]
To justify this normalization, differentiate
\(\alpha x+y=\eta\) while holding \(x,y\) fixed, and use the
original two envelope equations. Since
\(\alpha'(T)=-2\pi a_0\ne0\), (11) gives analytic continuation
of the parametrized arc to a neighborhood of \(T\). In particular
\[
\Gamma_u(T)=(e_0/a_0,0)=(k(u),0).                            \tag{12}
\]
Reflection of (1) gives
\(\Gamma_u(-\theta)=(y_u(\theta),x_u(\theta))\), proving the
other endpoint is \((0,k(u))\).

Since \(h(u+T)=\pi\),
\(\cot(hu)+\cot(hT)=0\). Therefore
\[
k(u)+k(T)=\frac{\sin u\sin T}{\sin\delta}
                   (\cot T+\cot u)=1.                       \tag{13}
\]
Both summands are positive. To see this without assuming the curve lies
in the square, \(t\cot t\) is strictly decreasing on \((0,\pi)\):
its derivative has numerator \(\sin t\cos t-t<0\), since
\((t-\sin t\cos t)'=2\sin^2t\) and the value at zero is zero.
Apply this with \(0<T<hT<\pi\) to obtain
\(\cot T-h\cot(hT)>0\). The same argument applies to \(u\).
This proves \(0<k(u)<1\) and all contact identities in (3).

## Nonzero endpoint speed

Set
\[
d(u)=e_1-k(u)a_1.
\]
Differentiating (11), using (9), gives
\[
x_u'(T)=\frac{2d(u)}{a_0}=:v(u),\qquad y_u'(T)=0,\qquad
y_u''(T)=2\pi a_0v(u).                                       \tag{14}
\]
For example \(\eta''-k\alpha''=-4\pi d(u)\), proving the
first identity. The last follows by differentiating
\(y_u'=-\alpha x_u'\) at \(T\).

Here is an exact sign proof at the endpoint. Let
\(z=\tan(T/3)\in(0,1)\), and use \(A,f\) from (6). In the
limit \(\theta=T\), the second rational coordinate is zero.
With \(L=(1+z^2)d/dz\) and \(f'(0)=7/18\), (6) gives
\[
a_0=A(z)/(2\pi),\quad e_0=f(z)/(2\pi),\quad
a_1=LA(z)/(12\pi),\quad e_1=[Lf(z)-7/18]/(12\pi).
\]
Thus substitution in (14) gives
\[
v(u)=\frac{Lf(z)-7/18-f(z)LA(z)/A(z)}{3A(z)}
=\frac{z(1-z)H(z)}{27(1+z)^2(1+z^2)^3},                      \tag{15}
\]
where
\[
H(z)=21+189z+280z^2+105z^3-122z^4-93z^5-32z^6-9z^7-3z^8.
\]
The polynomial identity in (15) can be checked without trigonometric
limits: insert the two rational expressions (6), differentiate, and
clear their denominators. The resulting integer identity is checked
coefficient by coefficient in [verify_joins.py](verify_joins.py).

For every \(r>0\), direct binomial expansion gives
\[
\begin{split}
(1+r)^8H(r/(1+r))={}&21+357r+2191r^2+6930r^3+12688r^4\\
 &+13860r^5+8764r^6+2856r^7+336r^8>0.                       \tag{16}
\end{split}
\]
The substitution maps \(r>0\) bijectively onto \(0<z<1\), so
\(H(z)>0\) there. Every other factor in (15) is positive. Hence
\(v(u)>0\) and \(d(u)>0\) for every allowed \(u\). By symmetry
the tangent at the western endpoint is \((0,-v(u))\). Thus neither
endpoint is a cusp or a stationary parametrized point.

## Matching the second derivatives as graphs

The geometric curvature at the southern endpoint, where the tangent is
horizontal, follows from (14):
\[
K(u)=\frac{y_u''(T)}{x_u'(T)^2}
     =\frac{\pi a_0^2}{d(u)}>0.                              \tag{17}
\]
It agrees with \(K(T)\). Here is a derivation that does not rely on
the rational computation. Put
\[
M(s)=\cot s-h\cot(hs).
\]
Using (8), (10), and \(k a_1=e_0a_1/a_0\), expansion gives
\[
8\pi d(u)=\tfrac23(h^2-1)-M(T)M(u).                          \tag{18}
\]
Explicitly, set \(A_*=\cot T\), \(B_*=\cot u\),
\(J=h\cot(hT)=-h\cot(hu)\). The right side obtained from
(8) is
\[
h^2\csc^2(hT)-\csc^2T-(h^2-1)/3
 -(A_*-J)(B_*-A_*)
=\tfrac23(h^2-1)+J^2+J(B_*-A_*)-A_*B_*,
\]
which equals (18), since
\(M(T)M(u)=(A_*-J)(B_*+J)\). This proves the identity.
Both (18) and \(a_0\) in (10) are invariant under \(u\leftrightarrow T\).
Therefore \(K(u)=K(T)\), and also \(v(u)=v(T)\).

Near \(S_0\), each adjacent arc is an analytic graph over \(x\),
by its nonzero horizontal speed. Their values at the contact agree by
(13), their first derivatives are zero, and their second derivatives
are \(K(u)\) and \(K(T)\). Reflection in a vertical line preserves
the second graph derivative. The two graph pieces consequently form a
\(C^2\) graph with positive second derivative at the join.
Reflection and interchange of the coordinate axes give the same argument
at the other three contacts. This establishes regular \(C^2\) gluing
and positive curvature at all joins. Positive curvature on the open arcs
is already (5).

## Nonintersection and strict convexity

Write \(k=k(u)\) and \(l=k(T)=1-k\). From (5), (12), and
reflection, the southwest arc is a strictly convex decreasing graph
from \((0,k)\) to \((k,0)\). Every interior point satisfies
\[
0<x<k,\quad 0<y<k,\quad x+y<k.                              \tag{19}
\]
For the last inequality, a strictly convex graph lies strictly below
the chord joining its endpoints. This follows, for example, from the
strict increase of its first derivative in (5).

The southeast arc has \(k<x<1\) in its interior, whereas the southwest
arc has \(x<k\); they meet only at \(S_0\). The northwest arc has
\(k<y<1\), so it meets the southwest arc only at \(W_0\).
The corresponding bounds separate southeast from northeast and northwest
from northeast. The opposite arcs are also disjoint: southwest has
\(x+y<k\), northeast has \(x+y>2-k\), and \(k<1\).
For the other opposite pair, reflecting (19) for parameter \(T\)
gives \(x-y>k\) on southeast and \(x-y<-k\) on northwest.
The four contacts are distinct because \(0<k<1\). Thus the arcs
make a simple closed curve and have no further contacts with the square.

Traverse the southwest arc from west to south, then southeast to east,
northeast to north, and northwest to west. The southwest tangent angle
increases strictly from \(-\pi/2\) to zero, by (5) and the endpoint
tangents in (14). The reflections and orientations make the other three
successive angle ranges \((0,\pi/2)\), \((\pi/2,\pi)\), and
\((\pi,3\pi/2)\). Hence the tangent turns exactly \(2\pi\),
strictly monotonically. All these assertions remain true across the joins
by the established regularity and positive curvature.

For completeness, this implies strict convexity as follows. Parametrize
the curve by arclength \(s\) of period \(L\), and fix \(s_0\).
Let \(n_0\) be its left unit normal and
\(g(s)=(\Gamma(s)-\Gamma(s_0))\cdot n_0\). Its derivative is
the sine of the difference of tangent angles. During one traversal it
is positive up to the unique angle difference \(\pi\), and negative
thereafter until the difference reaches \(2\pi\). Because
\(g(s_0)=g(s_0+L)=0\), it follows that \(g(s)>0\) at every
other point. Thus every tangent is a supporting line touching the curve
at exactly one point. Every normal direction occurs. In the compact
convex hull of the curve, the support face in each direction is therefore
this single point of the curve. Every point on the boundary of a compact
convex set has a supporting line, so the convex hull boundary equals the
curve. The support faces contain no nontrivial segment, proving strict
convexity. Its convex hull lies in the unit square by (19) and its reflected
bounds.

## A geometric collar

The regular \(C^2\) curve has a periodic arclength parametrization with
\(C^1\) inward unit normal \(n(s)\) and continuous positive curvature
\(K(s)\). Consider
\[
\Psi(s,t)=\Gamma(s)+t n(s).
\]
With positively oriented unit tangent \(T(s)\),
\(n'=-KT\), so \(\Psi_s=(1-tK)T\) and \(\Psi_t=n\).
At \(t=0\) the Jacobian is nonzero. The inverse function theorem
gives a local \(C^1\) diffeomorphism around every point of the circle
\(t=0\).

There is a common positive width on which this map is injective. If
not, there would be distinct colliding pairs with \(|t|,|t'|\to0\).
Compactness gives limiting arclength parameters. Their curve points
coincide; simplicity makes the limits identical modulo \(L\). Both
pairs then lie in one inverse-function neighborhood, a contradiction.
Choose the width also smaller than \(1/\max K\), which is positive
by continuity and compactness. Positive \(t\) lies inside the curve:
locally the inward normal points into the convex region, and this side
is consistent around the connected closed curve. This proves the inward
normal collar assertion. No Fredholm parametrization was used here.

## The C2 conclusion is sharp at equal weights

Let \(u=T=3\pi/8\), and put \(r=\sqrt2-1\). Then
\[
k=1/2,\quad a_0=r/(2\pi),\quad a_1=0,\quad
v=\frac{41-13\sqrt2}{54}>0,\quad \cot\delta=-1.               \tag{20}
\]
The speed follows from (18) and (14), since
\(M(T)=r\), \(h^2-1=7/9\), and \(r^2=1-2r\).
Moreover, differentiating (7) twice and (1) twice at \(T\) gives
\[
e_2=\frac{\csc^2T\cot T}{8\pi},\qquad
\frac{a_2}{a_0}=2-\sqrt2,\qquad e_2=\tfrac12a_2.
\]
The last equality follows from
\(\cot T=r\) and \(\csc^2T=1+r^2=2(2-\sqrt2)\).

To calculate the third graph derivative, retain the notation
\(\alpha=a/b\), \(\eta=e/b\). At this symmetric endpoint,
\(\alpha'=-2\pi a_0\), \(\alpha''=-2\pi a_0\cot\delta\).
Differentiating \(\eta'=x\alpha'\) twice gives
\[
x''=3(e_2-ka_2)/a_0-v\cot\delta/2=v/2.
\]
For clarity, the first equality follows by writing
\(\eta'''-k\alpha'''=-6\pi(e_2-ka_2)-6\pi d\cot\delta\)
using (9), and then subtracting \(2v\alpha''\) and dividing by
\(\alpha'\). As \(y'=-\alpha x'\), at the endpoint
\[
\frac{d^3y}{dx^3}
=-\frac{\alpha''}{v^2}+\frac{\alpha'x''}{v^3}
=-\frac{3r}{2v^2}
=-\frac{4168422\sqrt2+494262}{1803649}<0.                     \tag{21}
\]
At equal weights the southeast arc is its reflection across \(x=1/2\).
Its one-sided third graph derivative has the opposite sign. Thus the
curve is not \(C^3\) at \(S_0\). The other contacts follow by
the square symmetries. This also rules out analytic gluing in general.

## Reproduction and scope

Run the exact earlier-certificate audit, the symbolic endpoint derivation,
and the independent endpoint audit as listed in [LOG.md](LOG.md).
The new audit checks (15) as a full integer polynomial identity and (16)
by independent binomial sums. Fraction-series computations reconstruct
the endpoint jets without symbolic differentiation. Direct derivatives
of the original trigonometric formulas independently test their limits.

The allowed collar width can depend on \(u\). No positive uniform width
is claimed as \(u\to0\) or \(u\to\delta\). Nothing here proves
that the Fredholm branch extends uniformly through the contacts, rules
out distant critical points, extends the curvature sign to other values
of \(\Delta\), or identifies the candidate with a probabilistic liquid
region. No antiferroelectric result is obtained.
