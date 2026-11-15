# Positive curvature of the candidate arcs at Delta = 1/sqrt(2)

The result concerns deterministic candidate formulas. It does not prove
convergence of the six-vertex measure. The sign proof uses a finite
integer polynomial certificate, supplied in full in [certificate.json](certificate.json).

## Statement and definitions

Set
\[
\gamma=\pi/4,\qquad \delta=3\pi/4,\qquad h=4/3,
\qquad 0<u<\delta,\qquad T=\delta-u.
\]
For \(|\theta|<T\), put
\[
\begin{split}
a(\theta)&=\frac{\sin\gamma}{2\pi(\cos(\theta-u)+\cos\gamma)},\\
b(\theta)&=\frac{\sin\gamma}{2\pi(\cos(\theta+u)+\cos\gamma)},\\
e(\theta)&=\frac1{2\pi}\left[
\frac{\sin T}{\cos\theta-\cos T}
-\frac{h\sin(hT)}{\cos(h\theta)-\cos(hT)}\right].
\end{split}                                                    \tag{1}
\]
These are the disordered coefficients in Alexey Bufetov,
[*Limit shape for domain-wall six-vertex model*, arXiv:2609.20576v1](https://arxiv.org/html/2609.20576v1),
equations (4.3) and (4.6), here defined at a parameter outside the range
of its announced disordered theorem. Define
\[
W=ab'-a'b,\quad
X_0=(x_0,y_0)=\left(\frac{eb'-e'b}{W},\frac{ae'-a'e}{W}\right),
\qquad C=x_0a''+y_0b''-e'' .                                  \tag{2}
\]
The multipliers \(x_0,y_0\) are held fixed in the last expression.

**Theorem.** For every \(0<u<3\pi/4\) and \(|\theta|<3\pi/4-u\),
\(C(\theta)>0\). The entire open southwest candidate arc is an
embedded graph \(y=f(x)\), with \(f'<0\) and \(f''>0\).
The small-\(B\) critical branch defined below gives one-to-one coordinates
on the locally convex side near every point of this arc. For each fixed
\(u\) these coordinates are injective for sufficiently small positive
\(B\) along any prescribed compact subarc. The same conclusions hold on
the other three open candidate arcs after the indicated affine symmetries
and the replacement \(u\leftrightarrow T\).

No assertion is made about joining points, distant critical parameters,
or a liquid region of a random configuration.

In terms of vertex weights, the parametrization is
\((a_{\rm v},b_{\rm v},c_{\rm v})\propto
(\sin T,\sin u,\sin\delta)\). Their ratio is
\(a_{\rm v}/b_{\rm v}=\sin\delta\cot u-\cos\delta\).
Its derivative is \(-\sin\delta\csc^2u<0\); its limits at
\(u=0,\delta\) are infinity and zero. Thus the theorem covers every
positive weight ratio at \(\Delta=\cos\gamma=1/\sqrt2\).

## The envelope determinant

Both \(\theta-u\) and \(\theta+u\) lie in \((-\delta,\delta)\).
On this interval \(\cos t+\cos\gamma>0\), so \(a,b>0\).
The function
\[
g(t)=\frac{\sin t}{\cos t+\cos\gamma},\qquad
g'(t)=\frac{1+\cos\gamma\cos t}{(\cos t+\cos\gamma)^2}>0
\]
is strictly increasing. Since \(a'/a=g(\theta-u)\) and
\(b'/b=g(\theta+u)\),
\[
W=ab[g(\theta+u)-g(\theta-u)]>0.                              \tag{3}
\]
Thus (2) is well defined and is the unique solution of
\(ax_0+by_0=e\), \(a'x_0+b'y_0=e'\).

## Rational coordinates

Let
\[
p=(T+\theta)/6,\quad q=(T-\theta)/6,\quad x=\tan p,\quad y=\tan q.
\]
Here \(p,q>0\), \(p+q=T/3<\pi/4\). Consequently
\[
x>0,\qquad y>0,\qquad x+y+xy<1.                              \tag{4}
\]
Conversely, (4) implies \(x,y<1\) and
\(\arctan x+\arctan y<\pi/4\); it determines a unique allowed
\(T=3(p+q)\), \(u=\delta-T\), \(\theta=3(p-q)\).
Thus (4) parametrizes exactly the full open parameter domain.

Define the positive polynomials and rational functions
\[
\begin{split}
d(z)&=z(1-z)(3-z^2)(z^2+4z+1),\\
z_0(z)&=(1-z)(1+z)(3-z^2),\\
A(z)&=\frac{(1+z^2)^3}{2d(z)},\qquad
f_0(z)=\frac{z(z^4+7)}{6z_0(z)}.
\end{split}                                                    \tag{5}
\]
The letter \(z_0\) names a polynomial, not a coordinate. Direct
trigonometric identities give
\[
2\pi a=A(x),\qquad 2\pi b=A(y),\qquad
2\pi e=f_0(x)+f_0(y).                                         \tag{6}
\]
For completeness, \(\theta-u=6p-3\pi/4\), so
\(2\pi a=1/(\sin(6p)-\cos(6p)+1)\). The identities
\[
\sin(6p)=\frac{6x-20x^3+6x^5}{(1+x^2)^3},\qquad
\cos(6p)=\frac{1-15x^2+15x^4-x^6}{(1+x^2)^3}
\]
give \(A\) in (5). The corresponding formula for \(b\) follows by
reflection. Finally,
\[
\frac{\sin T}{\cos\theta-\cos T}
=\tfrac12\left[\cot((T+\theta)/2)+\cot((T-\theta)/2)\right],
\]
and the scaled version gives one summand
\[
\tfrac12\cot(3p)-\tfrac23\cot(4p)
=\frac{x(x^4+7)}{6(1-x)(1+x)(3-x^2)}.
\]
This uses \(\cot(3p)=(1-3x^2)/(3x-x^3)\) and
\(\cot(4p)=(1-6x^2+x^4)/(4x-4x^3)\), proving (6).

Write \(L_z=(1+z^2)d/dz\). Differentiation in \(\theta\) at fixed
\(u\) is \((L_x-L_y)/6\). For this section only, set
\[
\begin{array}{lll}
\mathsf a=A(x),&\mathsf a_1=L_x A(x),&\mathsf a_2=L_x^2 A(x),\\
\mathsf b=A(y),&\mathsf b_1=-L_y A(y),&\mathsf b_2=L_y^2 A(y),\\
E=f_0(x)+f_0(y),&E_1=L_xf_0(x)-L_yf_0(y),&
E_2=L_x^2f_0(x)+L_y^2f_0(y).
\end{array}
\]
Let \(\mathcal W=\mathsf a\mathsf b_1-\mathsf a_1\mathsf b\).
By (3), \(\mathcal W=24\pi^2W>0\). Eliminating \(x_0,y_0\) in
(2) gives
\[
72\pi C=\frac{N}{\mathcal W},                                \tag{7}
\]
where
\[
N=E(\mathsf b_1\mathsf a_2-\mathsf a_1\mathsf b_2)
 +E_1(\mathsf a\mathsf b_2-\mathsf b\mathsf a_2)
 -E_2\mathcal W.                                             \tag{8}
\]
The factor \(72\pi=36(2\pi)\) accounts for the two theta derivatives
and the common coefficient normalization.

## The integer sign certificate

The exact polynomial identity used in (8) is
\[
N=\frac{(x+y)(1+x^2)^3(1+y^2)^3(1-xy)(1-x-y-xy)^2J(x,y)Q(x,y)}
 {4d(x)^3d(y)^3(1+x)^3(1+y)^3},                              \tag{9}
\]
where
\[
J(x,y)=(1+x^2)(1+y^2)+4(x+y)(1-xy)>0.                         \tag{10}
\]
All factors in (9) other than \(Q\) are strictly positive on (4).

Here is a complete specification of \(Q=\sum_{i,j=0}^{12}q_{ij}x^iy^j\).
It is symmetric: \(q_{ij}=q_{ji}\). Row \(i\) lists
\(q_{i,i},q_{i,i+1},\ldots,q_{i,12}\), including zeros.

```text
0:  0 63 630 1386 945 -520 -1030 -358 92 89 32 12 3
1:  1260 8946 16758 8587 -8952 -11844 -2564 1925 1308 450 158 33
2:  46368 66164 9816 -59756 -45296 1192 12838 6442 2080 660 92
3:  50482 -49810 -91288 -16620 24584 14554 4626 1576 438 -2
4:  -84672 -15228 59530 29182 -3737 -5423 -1730 -780 -184
5:  81336 59440 -4984 -16520 -7712 -2340 -848 -84
6:  -16088 -27344 -5130 756 168 156 102
7:  -8608 3654 2908 840 376 66
8:  1880 467 116 48 -11
9:  -172 -46 -30 -13
10: 8 0 -2
11: 2 0
12: 0
```

The mixed signs in this table do not decide its sign on (4). Make the
additional substitution
\[
x=\frac r{1+r},\qquad y=\frac s{(1+s)(1+2r)},\qquad r,s>0.       \tag{11}
\]
It maps the positive quadrant bijectively to (4):
\(x\in(0,1)\) and \(0<y<(1-x)/(1+x)=1/(1+2r)\).
Conversely, \(r=x/(1-x)\) and
\(s=y(1+2r)/(1-y(1+2r))>0\) give the inverse.

Define
\[
R(r,s)=(1+r)^{12}(1+s)^{12}(1+2r)^{12}
 Q\left(\frac r{1+r},\frac s{(1+s)(1+2r)}\right).             \tag{12}
\]
This is a polynomial of bidegree \((24,12)\). Its coefficients
\(R_{mn}\) are determined by the following finite integer sums:
\[
R_{mn}=\sum_{i,j=0}^{12}q_{ij}\binom{12-j}{n-j}
 \sum_{\ell=0}^{12-j}2^\ell\binom{12-j}{\ell}
                    \binom{12-i}{m-i-\ell}.                  \tag{13}
\]
A binomial coefficient is zero when its lower index is outside the
usual range. The constant coefficient is zero. All 324 other
coefficients are strictly positive. For a compact record of the finite
sign check, the table gives the minimum of the nonzero entries in row
\(m\). Row zero contains 12 positive entries; every other row contains
13. The complete 25 by 13 array is in certificate.json.

| m | Minimum positive coefficient in row m |
|---|---:|
| 0 | 63 |
| 1 | 63 |
| 2 | 2835 |
| 3 | 59535 |
| 4 | 779940 |
| 5 | 7176566 |
| 6 | 49451332 |
| 7 | 265447148 |
| 8 | 1139236544 |
| 9 | 3979127464 |
| 10 | 11449114592 |
| 11 | 27356308352 |
| 12 | 54541554496 |
| 13 | 90920146304 |
| 14 | 126653120512 |
| 15 | 146970039296 |
| 16 | 141221309440 |
| 17 | 111319963648 |
| 18 | 71012016128 |
| 19 | 35951411200 |
| 20 | 14044413952 |
| 21 | 4058808320 |
| 22 | 811073536 |
| 23 | 99090432 |
| 24 | 5505024 |

In particular, \(R_{10}=R_{01}=63\), so
\[
R(r,s)\geq63(r+s)>0\qquad(r,s>0).                            \tag{14}
\]
The multiplier in (12) is positive. Thus \(Q>0\) on (4).
Equations (3), (7), (9), and (10) now prove \(C>0\).

Both finite identities have an exact verification independent of the
symbolic derivation. The following details specify the arithmetic behind
the certificate, including the denominator clearing in (9).
Set
\[
A_0(z)=(1+z^2)^3,\qquad F_0(z)=z(z^4+7).
\]
For \(i=0,1\), define polynomial recurrences
\[
\begin{split}
A_{i+1}&=(1+z^2)[dA_i'-(i+1)d'A_i],\\
F_{i+1}&=(1+z^2)[z_0F_i'-(i+1)z_0'F_i].
\end{split}                                                    \tag{15}
\]
The quotient rule gives
\(L_z^iA=A_i/(2d^{i+1})\) and
\(L_z^if_0=F_i/(6z_0^{i+1})\).
Put \(H(z)=d(z)^5(1+z)^3\), and define
\[
\begin{split}
M_i(z)&=A_i(z)d(z)^{4-i}(1+z)^3,\\
M_{ij}(z)&=A_i(z)F_j(z)d(z)^{3-i-j}(1+z)^{2-j}
                   [z(z^2+4z+1)]^{j+1}.
\end{split}                                                    \tag{16}
\]
Only pairs with \(i+j\leq3\), \(i,j\leq2\) occur, so all
exponents are nonnegative. Since
\(z_0=d(1+z)/[z(z^2+4z+1)]\), these are precisely the
numerators obtained by clearing the denominator \(H\) in a single
\(A\) derivative, or in its product with an \(f_0\) derivative.

Let the six quadruples \((\varepsilon,i,k,j)\) be
\[
(-1,2,1,0),\ (-1,1,2,0),\ (1,0,2,1),\ (-1,2,0,1),\
(1,0,1,2),\ (1,1,0,2).
\]
Expanding (8) shows that its numerator over \(24H(x)H(y)\) is
\[
\sum_{(\varepsilon,i,k,j)}\varepsilon
 [M_{ij}(x)M_k(y)+(-1)^jM_i(x)M_{kj}(y)].                     \tag{17}
\]
Multiplication of the explicit polynomials (15)–(16) gives exactly
\[
6d(x)^2d(y)^2(x+y)(1+x^2)^3(1+y^2)^3
 (1-xy)(1-x-y-xy)^2J(x,y)Q(x,y).                             \tag{18}
\]
This proves (9) after division by \(24H(x)H(y)\).

[audit_certificate.py](audit_certificate.py) verifies equality of every
integer coefficient in (17) and (18), reconstructs all entries of (12)
by (13), and checks their signs. It uses only standard-library integer
addition, multiplication and binomial coefficients. No floating point
or symbolic algebra library is used in that verification.
[derive_certificate.py](derive_certificate.py) obtains the same identities
separately by rational differentiation in SymPy. The verification is run by

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_certificate.py
```

## Geometry of the entire open arc

Differentiate the two envelope equations. Their first derivatives give
\[
ax_0'+by_0'=0,\qquad a'x_0'+b'y_0'=-C,
\qquad X_0'=\frac C W(b,-a).                                 \tag{19}
\]
Because \(a,b,C,W>0\), \(x_0'>0\) and \(y_0'<0\).
Thus the whole open arc is injective and is a graph over its
\(x\)-coordinate. Its slope and second derivative are
\[
f'(x_0)=-a/b<0,\qquad
f''(x_0)=\frac{(W/b^2)}{x_0'}=\frac{W^2}{Cb^3}>0.            \tag{20}
\]
This proves the asserted strict convexity without assuming a physical
interpretation of either side of the graph.

## The critical branch and its collar

Here is a definition and derivation of the branch needed for the last
part of the theorem. On \([-B,B]\), set
\[
(K_Bv)(s)=\int_{-B}^B\frac{v(t)}{2\pi\cosh(s-t)}\,dt,
\qquad \rho_B=(I-K_B)^{-1}1.
\]
The full-line integral of \(1/(2\pi\cosh s)\) is \(1/2\), as
the substitution \(t=e^s\) gives
\(\pi^{-1}\int_0^\infty(1+t^2)^{-1}dt=1/2\).
Hence the row-integral bound is at most \(1/2\), and the Neumann
series defines the inverse on continuous functions for every \(B>0\).
The density is real and even.

Let
\[
\begin{split}
\mathscr A(z)&=\frac{\sin\gamma}{2\pi(\cosh z+\cos\gamma)},\\
\mathscr L(z)&=\frac1{2\pi}\left[
\frac{\sin T}{\cosh z-\cos T}
-\frac{h\sin(hT)}{\cosh(hz)-\cos(hT)}\right],\\
F(s;X,\theta)&=x\mathscr A(s+i(\theta-u))
              +y\mathscr A(s+i(\theta+u))-\mathscr L(s+i\theta),\\
\Phi(B;X,\theta)&=\int_{-B}^BF(s;X,\theta)\rho_B(s)\,ds.
\end{split}                                                    \tag{21}
\]
The critical branch \(X(B,\theta)\) solves
\(\Phi_B=\Phi_\theta=0\) for fixed \(B,\theta\).

After rescaling to \([-1,1]\), the kernel is
\(B/[2\pi\cosh(B(r-t))]\), analytic near \(B=0\) with norm
\(O(|B|)\). Its Neumann series is analytic there. In particular,
the even moments satisfy
\[
M_0=\int\rho_B=2B+O(B^2),\qquad
M_2=\int s^2\rho_B=2B^3/3+O(B^4),\qquad M_4=O(B^5).
\]
Writing \(F_j=\partial_s^jF(0)\) gives
\[
\Phi=M_0F_0+\tfrac12M_2F_2+O(B^5).
\]
These expansions are analytic in \(B\), locally uniformly with parameter
derivatives. Divide the critical equations by \(M_0'\) and \(M_0\),
respectively, extending the second quotient analytically at zero.
Their coefficient matrix in \(x,y\) at \(B=0\) is
\(\left(\begin{smallmatrix}a&b\\a'&b'\end{smallmatrix}\right)\).
Its positive determinant gives a unique analytic branch through \(X_0\).
The quotients \(M_2'/(2M_0')=B^2/2+O(B^3)\) and
\(M_2/(2M_0)=B^2/6+O(B^3)\) show that the branch has no linear term:
\[
X(B,\theta)=X_0(\theta)+B^2V(\theta)+O(B^3),
\quad aV_x+bV_y=C/2,\quad a'V_x+b'V_y=D_3/6,                \tag{22}
\]
where \(D_3=x_0a'''+y_0b'''-e'''\). Indeed
\(F_2=-\partial_\theta^2F_0\), so the two normalized critical
equations give exactly (22). Compactness makes the expansions uniform
on a compact subinterval of \((-T,T)\).

Put \(t=B^2\). The map is
\[
Y(t,\theta)=X_0(\theta)+tV(\theta)+t^{3/2}R_*(\sqrt t,\theta),
\qquad t\geq0,
\]
where \(R_*\) is analytic. Extend it to \(t<0\) by
\(X_0(\theta)+tV(\theta)\). The extension is \(C^1\): the
remainder and its first derivatives tend to zero at \(t=0\).
By (19) and (22),
\[
\det[V,X_0']=-\frac C W(aV_x+bV_y)=-\frac{C^2}{2W}<0.         \tag{23}
\]
The inverse function theorem gives local one-to-one coordinates at every
point of the arc. For the graph in (20), put \(G(x,y)=y-f(x)\).
Its gradient on the arc is \((a,b)/b\), and therefore
\[
\partial_tG(Y(0,\theta))=C/(2b)>0.
\]
By continuity, positive small \(t\) maps to \(G>0\), the locally
convex side; the local diffeomorphism maps a one-sided parameter
neighborhood onto the corresponding side of its image neighborhood.

To obtain injectivity along a compact subarc, choose a slightly larger
compact parameter interval still inside \((-T,T)\). If no uniform
small positive \(t\) gave injectivity on the original interval, there
would be distinct colliding pairs with \(t,t'\to0\).
Subsequences of their theta coordinates converge. Continuity and the
injectivity of \(X_0\) in (19) force the same limit theta. Both pairs
then lie in one of the local diffeomorphism neighborhoods from (23),
a contradiction. This proves compact-subarc injectivity. Positivity of
\(G\) for small positive \(t\) is uniform there by the same compactness
argument. Since \(B\mapsto B^2\) is injective for \(B>0\), the
conclusion also holds in the original positive \(B\) parameter.

Finally, the other three candidate arcs are the images of \(X_u\) or
\(X_T\) under \((x,y)\mapsto(1-x,y)\),
\((x,y)\mapsto(1-x,1-y)\), or \((x,y)\mapsto(x,1-y)\).
The theorem applies to both \(u\) and \(T\), and these affine
isometries preserve local strict convexity and injectivity. The result
therefore covers every open arc. It gives no control at their joining
points and no exclusion of critical points outside the small-\(B\)
collars. No limit-shape or antiferroelectric theorem follows from it.
