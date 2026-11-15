# Initial residual motion for the nonlinear sine model

Let \(\gamma=N(0,1)\), \(\pi=\gamma\otimes\gamma\), and
\[
 f_\rho(x)=\int a\sin(vx)\,d\rho(a,v),\qquad
 R(\rho)=\frac12\int(f_\rho(x)-\sin x)^2\,d\gamma(x).
 \tag{1}
\]
The parameter prior is fixed. Time is the physical gradient-flow time
for \(F_\lambda=R+\lambda\operatorname{KL}(\cdot\Vert\pi)\).
Define
\[
 \begin{split}
 K(v,w)&=\int\sin(vx)\sin(wx)\,d\gamma(x)
       =e^{-(v^2+w^2)/2}\sinh(vw),\\
 G_t(w)&=\int(\sin x-f_{\rho_t}(x))\sin(wx)\,d\gamma(x),\\
 g(w)&=G_0(w)=e^{-(1+w^2)/2}\sinh w.
 \end{split}
 \tag{2}
\]
Here and below \(\rho_0=\pi\).

The MFLD equation has weak generator
\[
 L_t\phi=\lambda(\phi_{aa}+\phi_{vv})
 +(G_t(v)-\lambda a)\phi_a
 +(a\partial_vG_t(v)-\lambda v)\phi_v.
 \tag{3}
\]
This follows from \(\delta R/\delta\rho=-aG_t(v)\) and the
standard Gaussian logarithmic gradient \(-(a,v)\).

## 1. Statement and solution class

Fix \(0<\lambda\leq1\) and \(T>0\). Let \(\rho_t\), \(0\leq t\leq T\),
be a \(W_2\)-continuous weak solution of (3), with locally bounded fourth
moments, that obeys
\[
 F_\lambda(\rho_t)\leq F_\lambda(\pi)=R(\pi).
 \tag{4}
\]
The results below hold for every solution in this class; they do not
assert a general existence or uniqueness theorem for unbounded
two-layer parameterizations.

Put
\[
 \begin{split}
 H(x)&=\frac1{\sqrt2}e^{-(1+x^2)/4}\sin(x/2),\\
 h(w)&=\frac1{\sqrt3}e^{-(1+w^2)/3}\sinh(w/3),\\
 U(x)&=\frac1{\sqrt2}e^{-(1+x^2)/4}
       \left[(1+x^2/2)\sin(x/2)+(x/2)\cos(x/2)\right],\\
 D(w)&=\frac{e^{-(1+w^2)/3}}{9\sqrt3}
       \left[(10-2w^2)\sinh(w/3)+5w\cosh(w/3)\right].
 \end{split}
 \tag{5}
\]

**Theorem.** In input \(L^2(\gamma)\), and pointwise for the residual,
\[
 \left.\frac{d}{dt}f_{\rho_t}\right|_{t=0}=U,
 \qquad \dot G_0(w)=-D(w).
 \tag{6}
\]
Neither derivative depends on \(\lambda\). The function \(D\) has
exactly one positive zero \(b\), with \(3<b<5\). It is positive on
\((0,b)\), negative on \((b,\infty)\), and
\[
 D(w)\sim-\frac{w^2}{9\sqrt3}e^{-(w^2-w+1)/3},\qquad
 \frac{\dot G_0(w)}{g(w)}\longrightarrow+\infty
 \quad(w\longrightarrow\infty).
 \tag{7}
\]
In particular, at each fixed \(w>b\), the actual residual initially
increases: \(G_t(w)>g(w)\) for all sufficiently small positive t,
where the allowed time can depend on w.

There is also a uniform upper bound
\[
 D(w)\leq C_*g(w)\quad(w>0),\qquad C_*:=\frac{25e}{9\sqrt3}.
 \tag{8}
\]
For an explicit positive-time statement set
\[
 M_T=13e^{20T},\qquad C_T=15000M_T^2.
 \tag{9}
\]
Uniformly in \(0<\lambda\leq1\), \(0\leq t\leq T\), and \(w\in\mathbb R\),
\[
 |G_t(w)-g(w)+tD(w)|\leq C_Tt^2\min(|w|,1).
 \tag{10}
\]
Consequently, if \(t\leq\min(T,1/(2C_*))\) and
\[
 L(t)^2:=4\log(1/t)-1-2\log(4C_T)>0,
 \tag{11}
\]
then
\[
 G_t(w)\geq\frac14g(w)>0\qquad(0<w\leq L(t)).
 \tag{12}
\]
In particular, for each fixed \(0<\kappa<2\), the residual is positive
on \(0<w\leq\kappa\sqrt{\log(1/t)}\) for all sufficiently small t.
The constants in (9) are deliberately loose.

The initial risk slope is
\[
 \dot R(\rho_0)
 =-\frac{13e^{-1/3}-3e^{-1}}{18\sqrt3}<0.
 \tag{13}
\]
No assertion about the sign of \(G_t\) on the whole positive half-line
at a fixed positive time follows from these statements.

## 2. The two contributions to the initial predictor derivative

The generator applied to the feature \(\phi_x(a,v)=a\sin(vx)\) is
\[
 L_t\phi_x=G_t(v)\sin(vx)
 +a^2\partial_vG_t(v)x\cos(vx)
 -\lambda a\left[(1+x^2)\sin(vx)+vx\cos(vx)\right].
 \tag{14}
\]
At \(t=0\), the output weight A is centered, independent of V, and
\(\mathbb E A^2=1\). The last term in (14) integrates to zero. Thus
\[
 \dot f_0(x)=\mathbb E[g(V)\sin(Vx)]
            +x\mathbb E[g'(V)\cos(Vx)].
 \tag{15}
\]
The second term is the contribution of hidden-weight motion.

Gaussian integration gives
\[
 \mathbb E[g(V)\sin(Vx)]=H(x).
 \tag{16}
\]
For detail, insert \(g(V)=e^{-1/2-V^2/2}\sinh V\), expand the
hyperbolic sine and sine as exponentials, and use
\(\mathbb E e^{-V^2/2+zV}=2^{-1/2}e^{z^2/4}\).
The imaginary part is exactly (16). Gaussian decay justifies the
complex exponential integration.

Gaussian integration by parts in V, applied to \(g(V)\cos(Vx)\), gives
\[
 \mathbb E[g'(V)\cos(Vx)]
 =\mathbb E[Vg(V)\cos(Vx)]+x\mathbb E[g(V)\sin(Vx)]
 =H'(x)+xH(x).
 \tag{17}
\]
Equations (15)–(17) yield
\[
 \dot f_0(x)=(1+x^2)H(x)+xH'(x)=U(x).
 \tag{18}
\]
Differentiating H gives the expression for U in (5).

These derivatives also hold in input \(L^2\). Indeed (14), the bounded
residual derivatives proved below, and the local moment bounds give an
integrable polynomial envelope in x, uniformly for short times. The
weak equation with parameter cutoffs and dominated convergence therefore
gives the integral of (14), and its value tends to (15) as t decreases
to zero. Continuity follows from \(W_2\) continuity and the moment
bounds. All Gaussian input polynomial moments are finite.

More explicitly, for a coupling of \((A,V)\sim\rho_t\) and
\((\widetilde A,\widetilde V)\sim\rho_s\),
\[
 \|f_{\rho_t}-f_{\rho_s}\|_{L^2(\gamma)}
 \leq(\mathbb E|A-\widetilde A|^2)^{1/2}
 +(\mathbb E|\widetilde A|^2)^{1/2}
  (\mathbb E|V-\widetilde V|^2)^{1/2}.
\]
This uses \(|\sin(vx)-\sin(ux)|\leq|v-u||x|\) and
\(\|X\|_{L^2}=1\). An optimal \(W_2\) coupling proves input
continuity. The same Cauchy–Schwarz bound applied to the input
correlations proves uniform continuity of the residual frequency
derivatives needed below. The terms in (14) have at most quadratic
parameter growth, so their expectations are continuous by this
continuity and uniform integrability from the fourth moments.

## 3. Residual derivative and its signs

The sine transform of H is
\[
 \int H(x)\sin(wx)\,d\gamma(x)=h(w).
 \tag{19}
\]
This follows by product-to-sum and
\(\mathbb E e^{-X^2/4}\cos(zX)=\sqrt{2/3}e^{-z^2/3}\).

Using (18), first note
\[
 h'(w)=\mathbb E[XH(X)\cos(wX)],\qquad
 h''(w)=-\mathbb E[X^2H(X)\sin(wX)].
 \tag{20}
\]
Integration by parts in X gives
\[
 \mathbb E[XH'(X)\sin(wX)]
 =\mathbb E[(X^2-1)H(X)\sin(wX)]-wh'(w).
 \tag{21}
\]
Adding the transform of \((1+X^2)H\) to (21) yields
\[
 \mathbb E[U(X)\sin(wX)]=-2h''(w)-wh'(w)=D(w).
 \tag{22}
\]
Direct differentiation of (19) gives exactly the formula for D in (5).
Equation (2) then proves \(\dot G_0=-D\).

For \(w>0\), h is positive. Write
\[
 \frac{D(w)}{h(w)}=P(w)
 :=\frac{10-2w^2+5w\coth(w/3)}9.
 \tag{23}
\]
Its continuous value at zero is \(25/9\). To prove strict decrease,
put \(z=w/3>0\). The inequality \(\tanh z<z\), obtained by
integrating \((\tanh z)'=\operatorname{sech}^2z<1\), implies
\(z\coth z>1\). Consequently
\[
 \coth z-z\operatorname{csch}^2z
 =z+\coth z(1-z\coth z)<z.
 \tag{24}
\]
Differentiating (23) now gives
\[
 P'(w)=\frac{-4w+5[\coth z-z\operatorname{csch}^2z]}9
 <-\frac{7w}{27}<0.
 \tag{25}
\]
At w=3, its numerator is \(-8+15\coth1>7\). At w=5, use
\(\coth z=1+2/(e^{2z}-1)<1+1/z\), a consequence of
\(e^{2z}>1+2z\). Its numerator is then less than
\(10-50+25(1+3/5)=0\). Continuity and strict decrease prove the
unique root and all stated signs.

As w tends to infinity, \(\coth(w/3)\to1\),
\(P(w)\sim-2w^2/9\), and
\(h(w)\sim e^{-(w^2-w+1)/3}/(2\sqrt3)\). This proves (7)'s
first relation. Also
\[
 \frac{h(w)}{g(w)}
 =\frac{e^{(1+w^2)/6}}{\sqrt3[1+2\cosh(2w/3)]}
 \sim\frac1{\sqrt3}e^{(w^2-4w+1)/6}\longrightarrow\infty.
 \tag{26}
\]
Combining (23) and (26) proves \(-D/g\to+\infty\).
The assertion at each fixed \(w>b\) follows directly from the
definition of its strictly positive time derivative.

## 4. A uniform bound for the tangent residual

Denote the ratio in (26) by Q(w). Its logarithmic derivative has the
sign of
\[
 N(w)=w[1+2\cosh(2w/3)]-4\sinh(2w/3).
 \tag{27}
\]
Here
\[
 N(0)=0,\quad N'(0)=1/3,\quad
 N''(w)=\tfrac89\sinh(2w/3)+\tfrac{8w}9\cosh(2w/3)>0.
 \tag{28}
\]
Thus Q is increasing on the positive half-line. For \(0<w<5\),
\[
 Q(w)\leq Q(5)
 =\frac{e^{13/3}}{\sqrt3[1+2\cosh(10/3)]}
 \leq\frac e{\sqrt3},\qquad P(w)\leq25/9.
 \tag{29}
\]
The last denominator bound uses \(1+2\cosh y\geq e^y\).
On the region where P is positive, (29) bounds \(D/g=PQ\) by
\(C_*\). Where P is nonpositive the same upper bound holds because
Q is positive. This proves (8). In particular,
\[
 g(w)-tD(w)\geq\tfrac12g(w)\quad
 (w>0,\ 0\leq t\leq1/(2C_*)).
 \tag{30}
\]
This is a statement about the exact tangent in predictor space, not
about a proposed probability law obtained by linearizing its density.

## 5. Moment and derivative bounds for the Taylor remainder

The energy inequality (4) implies
\[
 \|\sin-f_{\rho_t}\|_{L^2(\gamma)}^2=2R(\rho_t)
 \leq2R(\pi)=\mathbb E\sin^2X<1.
 \tag{31}
\]
Differentiating the correlation in its frequency variable and applying
Cauchy–Schwarz yields
\[
 \|\partial_v^jG_t\|_\infty
 \leq(\mathbb E X^{2j})^{1/2}\leq4\quad(0\leq j\leq3).
 \tag{32}
\]
For j=0 and j=1 the bounds are at most one.

Let \(r^2=a^2+v^2\), \(V_4=(1+r^2)^2\), and let the drift in
(3) be B. From the sharper j=0,1 bounds,
\[
 (a,v)\cdot B=aG_t(v)+av\partial_vG_t(v)-\lambda r^2
 \leq|a|+|av|\leq\tfrac12+r^2.
 \tag{33}
\]
Since \(\nabla V_4=4(1+r^2)(a,v)\) and
\(\Delta V_4=8+16r^2\),
\[
 L_tV_4\leq4(1+r^2)(\tfrac12+r^2)+8+16r^2
 \leq20(1+r^2)^2.
 \tag{34}
\]
The usual stopped weak equation followed by Gronwall and localization
gives
\[
 \mathbb E_{\rho_t}V_4\leq\mathbb E_\pi V_4\,e^{20t}
 =13e^{20t}\leq M_T.
 \tag{35}
\]
The value 13 uses \(\mathbb E_\pi r^2=2\) and
\(\mathbb E_\pi r^4=3+2+3=8\). The locally bounded fourth-moment
assumption justifies localization; (35) gives an explicit bound.

Here is a full bound on the second time derivative in (10). Fix w and
put \(\delta=\min(|w|,1)\), \(k(v)=K(v,w)\), and
\(q=1+|a|+|v|\). For \(0\leq j\leq4\),
\[
 |k^{(j)}(v)|\leq8\delta.
 \tag{36}
\]
Indeed for \(|w|\leq1\) use \(|\sin(wX)|\leq|wX|\), and for
\(|w|\geq1\) use its bound by one. The needed absolute moments up
to order five are less than eight: Gaussian integration by parts gives
\(\mathbb E|X|^{p+2}=(p+1)\mathbb E|X|^p\), starting from
\(\mathbb E|X|<1\) and \(\mathbb E X^2=1\).

Write \(G=G_t\), with primes denoting v derivatives, and define
\[
 B_1=G'k',\quad Q_1=k''-k-vk',\quad
 \Psi_t=L_t(ak)=Gk+a^2B_1+\lambda aQ_1.
 \tag{37}
\]
The following pointwise bounds follow from (32) and (36):
\[
 \begin{array}{c|ccc}
 &\text{function}&\text{first derivative in }v&\text{second derivative in }v\\ \hline
 B_1&32\delta&64\delta&128\delta\\
 Gk&32\delta&64\delta&128\delta\\
 Q_1&16q\delta&24q\delta&32q\delta.
 \end{array}
 \tag{38}
\]
For the last row,
\(Q_1'=k'''-2k'-vk''\) and
\(Q_1''=k''''-3k''-vk'''\), which proves the displayed constants.
In particular \(|\Psi_t|\leq48q^2\delta\).

To bound the time derivatives of G and G', apply the weak equation
to \(ak\) and to \(a\partial_wK(v,w)\). For the latter kernel,
its first two v derivatives are bounded by eight, uniformly in w,
using absolute input moments through order three. The same calculation
as (37) therefore gives
\[
 \|\dot G_t\|_\infty\leq48\mathbb E q^2,
 \qquad \|\partial_v\dot G_t\|_\infty\leq48\mathbb E q^2.
 \tag{39}
\]
These are separate bounds, not a bound on their sum. Since
\(q^2\leq3(1+r^2)\) and \(M_T\geq1\), each is at most
\(144\sqrt{M_T}\leq144M_T\).

For constant temperature, the explicit time derivative of (37) is
\(\partial_t\Psi_t=\dot G_tk+a^2\partial_v\dot G_tk'\).
Consequently
\[
 \mathbb E|\partial_t\Psi_t|
 \leq1152M_T\delta\,\mathbb E q^2
 \leq3456M_T^2\delta.
 \tag{40}
\]
Here \(\mathbb E q^2\leq3\sqrt{M_T}\leq3M_T\).

Expanding the generator once more gives
\[
 \begin{split}
 L_t\Psi_t={}&\lambda[2B_1+(Gk)''+a^2B_1''+\lambda aQ_1'']\\
 &+(G-\lambda a)(2aB_1+\lambda Q_1)\\
 &+(aG'-\lambda v)[(Gk)'+a^2B_1'+\lambda aQ_1'].
 \end{split}
 \tag{41}
\]
The three lines in absolute value are bounded, respectively, by
\(352q^2\delta\), \(320q^2\delta\), and \(608q^3\delta\).
For example \(|G-\lambda a|\leq4q\),
\(|aG'-\lambda v|\leq4q\), and the last bracket is at most
\(152q^2\delta\). Since q is at least one, the sum is at most
\(1280q^4\delta\). Also \(q^4\leq9V_4\). Hence
\[
 \mathbb E|L_t\Psi_t|\leq11520M_T\delta.
 \tag{42}
\]

The weak equation applied to the time-dependent test \(\Psi_t\)
now gives, for almost every time,
\[
 |\ddot G_t(w)|
 \leq\mathbb E|(\partial_t+L_t)\Psi_t|
 \leq(11520M_T+3456M_T^2)\delta
 \leq14976M_T^2\delta.
 \tag{43}
\]
All tests above have the polynomial envelopes exhibited in (38)–(42).
Parameter cutoffs, the fourth-moment bound, and dominated convergence
justify their weak equations. Equation (39) supplies the time regularity
needed in (40); equivalently use its integrated identity and approximate
in time. Thus \(\dot G_t(w)\) is absolutely continuous with the stated
bound. The bounds hold for each w with constants independent of w, so
Taylor's integral remainder yields
\[
 |G_t(w)-g(w)+tD(w)|
 \leq7488M_T^2t^2\delta\leq C_Tt^2\delta.
 \tag{44}
\]
This proves (10), including w=0, where all terms vanish.

## 6. Positivity window and initial risk

For every \(w>0\), \(\sinh w\geq w\) gives the elementary lower bound
\[
 g(w)\geq e^{-(1+w^2)/2}\min(w,1).
 \tag{45}
\]
Combining (30) and (44) yields
\[
 G_t(w)\geq\tfrac12g(w)-C_Tt^2\min(w,1).
 \tag{46}
\]
For w at most L(t), (11) is exactly the condition
\(C_Tt^2\leq\tfrac14e^{-(1+L(t)^2)/2}\).
Equation (45) then makes the second term in (46) at most g(w)/4.
This proves (12). Since \(L(t)^2=4\log(1/t)-O_T(1)\), the assertion
for every \(\kappa<2\) follows.

Finally (6) and \(f_0=0\) give
\(\dot R(\rho_0)=-\langle\sin,U\rangle=-D(1)\).
Substituting w=1 into (5), and expanding sinh and cosh, gives
\[
 D(1)=\frac{e^{-2/3}}{9\sqrt3}
       [8\sinh(1/3)+5\cosh(1/3)]
 =\frac{13e^{-1/3}-3e^{-1}}{18\sqrt3}>0.
 \tag{47}
\]
This proves (13).

## 7. Relation to the earlier shear obstruction

For the explicit shears \(\operatorname{Law}(A+t g(V),V)\), the
residual is exactly \(g-th\). Since h/g diverges at infinity, that
residual has a negative far tail at every t>0. The full nonlinear
trajectory instead has tangent \(g-tD\), which stays positive on the
entire positive half-line for small t by (30). Its far-tail initial
derivative is positive, not negative. Hidden-weight motion is responsible
for the difference.

The error estimate (10) is absolute after division by \(\min(|w|,1)\).
It is not relative to g, which decays as a Gaussian in frequency.
It therefore gives no sign beyond the window (11). A remote negative
lobe at positive times, a later lobe, or a small prediction-relevant
proximal gap along the trajectory remains possible. No polynomial
learning-time guarantee or exponential learning-time lower bound is
proved here. The initial derivative calculation also applies to a
bounded temperature schedule continuous at zero, because the initial
OU expectation vanishes; the quantitative remainder here was proved
only for constant temperature.
