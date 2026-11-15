# A close pair with two antipodal additional observations

Let \(\sigma(t)=\max(t,0)\). In \(\mathbb R^d\), \(d\ge2\), consider
\[
 f(x)=\sum_{j=1}^m c_j\sigma(w_j\cdot x),\qquad
 Q(c,w)=\frac12\sum_j(c_j^2+\|w_j\|^2).
\]
There are no biases, skips, or output intercepts. Width is unrestricted or
fixed at any \(m\ge4\). Test inputs are uniform on \(S^{d-1}\), with
normalized surface measure, and \(R(f)=\mathbb E f(X)^2\). The reference
regression function is zero.

Fix orthonormal \(e_1,e_2\), and write
\[
 0<\theta<\pi,\qquad a=\cos(\theta/2),\quad b=\sin(\theta/2),
 \quad s=2ab=\sin\theta.
\]
The four observations are
\[
 x_1=ae_1+be_2,\quad x_2=ae_1-be_2,\quad x_3=e_2,\quad x_4=-e_2,
 \qquad y=(1,-1,A,B).
\]

## Theorem

Suppose
\[
 A\le\frac1{2b},\qquad B\ge-\frac1{2b}.                 \tag{1}
\]
Define the unit directions
\[
 u=be_1+ae_2,\qquad v=-be_1+ae_2.
\]
Every minimum-\(Q\) interpolant induces the same function, namely
\[
 \begin{split}
 f_\theta(x)
 &=\frac1s\sigma(u\cdot x)
   +\left(\frac A a-\frac1s\right)\sigma(v\cdot x)
   -\frac1s\sigma((-v)\cdot x)
   +\left(\frac B a+\frac1s\right)\sigma((-u)\cdot x)\\
 &=f_{0,\theta}(x)+\frac A a\sigma(v\cdot x)
                         +\frac B a\sigma((-u)\cdot x),
 \qquad
 f_{0,\theta}(x)=\frac{|u\cdot x|-|v\cdot x|}{s}.
 \end{split}                                           \tag{2}
\]
The minimum parameter cost is exactly
\[
 Q_{\min}=\frac4s+\frac{B-A}{a}.                         \tag{3}
\]
In particular, for any fixed \(H<\infty\), condition (1) holds for every
\(|A|,|B|\le H\) once \(\theta\) is sufficiently small. Uniformly over
these labels and all minimizers,
\[
 \theta Q_{\min}\longrightarrow4,\qquad
 \sup_{\|x\|\le1}|\theta f_\theta(x)|\longrightarrow0,
 \qquad
 R(f_\theta)\longrightarrow\frac{1+(A^2+B^2)/2}{d}.       \tag{4}
\]
The meaning of uniformity in the last assertion is that the difference
between the two sides tends to zero uniformly over the bounded labels.
Thus the conditional risk has a finite, strictly positive limit, although
the minimum parameter cost diverges. For zero additional labels the limit
is \(1/d\); for \(A,B\in\{-1,1\}\) it is \(2/d\).

Here are exact finite-angle risks. Put \(c=\cos\theta\) and
\[
 R_0(\theta)=\frac{2\pi-4s-(2\pi-4\theta)c}
                    {\pi d s^2}.
\]
Then
\[
 R(f_\theta)
 =\bigl(1+b(B-A)\bigr)R_0(\theta)
   +\frac{A^2+B^2}{2d a^2}
   +\frac{AB(s-\theta c)}{\pi d a^2}.                   \tag{5}
\]
The deterministic antipodal geometry here has probability zero for iid
continuous inputs. These statements do not classify the random-design
large-sample limit.

## 1. Atomic normalization and a dual lower bound

For \(w_j\ne0\), let \(r_j=w_j/\|w_j\|\) and
\(\gamma_j=c_j\|w_j\|\). Discard zero units. Homogeneity and
\((c_j^2+\|w_j\|^2)/2\ge |c_j|\|w_j\|\) give
\[
 f(x)=\sum_j\gamma_j\sigma(r_j\cdot x),\quad \|r_j\|=1,
 \qquad T=\sum_j|\gamma_j|\le Q.                        \tag{6}
\]
Conversely a coefficient \(\gamma\) at a unit direction \(r\) is realized
at cost \(|\gamma|\) by
\(c=\operatorname{sign}(\gamma)\sqrt{|\gamma|}\) and
\(w=\sqrt{|\gamma|}r\).

If multipliers \(\lambda_i\) satisfy
\[
 \left|g(r)\right|\le1\quad(\|r\|=1),\qquad
 g(r)=\sum_{i=1}^4\lambda_i\sigma(r\cdot x_i),
\]
then every interpolant satisfies
\[
 Q\ge T\ge\sum_j\gamma_jg(r_j)=\lambda\cdot y.           \tag{7}
\]
Indeed \(\gamma_jg(r_j)\le|\gamma_j|\) term by term. If (7) is attained,
every nonzero coefficient must satisfy
\(g(r_j)=\operatorname{sign}(\gamma_j)\).

## 2. The antipodal dual certificate and its equality cases

Take
\[
 \lambda=\left(\frac1{ab},-\frac1{ab},-\frac1a,\frac1a\right).
                                                               \tag{8}
\]
For an ambient unit vector \(r\), write \(p=r\cdot e_1\) and
\(q=r\cdot e_2\), so \(p^2+q^2\le1\). Since
\(\sigma(q)-\sigma(-q)=q\), the dual price is
\[
 g(r)=\frac{D(p,q)}{ab},\qquad
 D(p,q)=\sigma(ap+bq)-\sigma(ap-bq)-bq.                  \tag{9}
\]
For \(q>0\), the three possible activation regions give
\[
 D(p,q)=
 \begin{cases}
  -bq,&ap\le-bq,\\
  ap,&-bq\le ap\le bq,\\
  bq,&ap\ge bq.
 \end{cases}                                           \tag{10}
\]
For \(q<0\), direct interchange of the two ReLUs gives
\(D(p,q)=-D(p,-q)\), and for \(q=0\) the value is zero. Therefore
\[
 |D(p,q)|=\min\{a|p|,b|q|\}.                           \tag{11}
\]
This minimum is at most \(ab\). Otherwise \(|p|>b\) and \(|q|>a\),
contradicting \(p^2+q^2\le1=a^2+b^2\). Thus (8) is dual feasible
for every ambient direction, including directions outside the sample plane.

Equality in (11) with \(|D|=ab\) requires \(|p|\ge b\) and
\(|q|\ge a\). The same sum-of-squares inequality then forces
\(|p|=b\), \(|q|=a\), and zero component outside the plane.
At these four directions, (10) shows that the price has the sign of \(pq\).
Consequently the complete list of signed equality atoms is
\[
 +u,\qquad -v,\qquad -(-v),\qquad +(-u),                \tag{12}
\]
where the sign preceding an atom means its coefficient sign. This also
proves that off-plane atoms cannot occur with nonzero coefficients in a
minimum that attains (7).

## 3. Interpolation, exact optimality, and uniqueness as a function

In the order \(u,v,-v,-u\), the four unit-atom response columns are
\[
 \begin{array}{c|rrrr}
       &u&v&-v&-u\\\hline
 x_1   &s&0&0&0\\
 x_2   &0&0&s&0\\
 e_2   &a&a&0&0\\
 -e_2  &0&0&a&a
 \end{array}.                                          \tag{13}
\]
For example \(u\cdot x_1=2ab=s\), \(u\cdot x_2=0\),
\(v\cdot x_1=0\), and \(v\cdot x_2=-s\); the remaining entries
follow by negation and by the second coordinates.

The interpolation equations have the unique coefficient totals
\[
 \gamma_u=\frac1s,\quad
 \gamma_v=\frac A a-\frac1s,\quad
 \gamma_{-v}=-\frac1s,\quad
 \gamma_{-u}=\frac B a+\frac1s.                          \tag{14}
\]
Condition (1) is exactly the requirement that these have the coefficient
signs permitted by (12), with zeros allowed. Their absolute sum is
\[
 \frac1s+\left(\frac1s-\frac A a\right)+\frac1s
                 +\left(\frac B a+\frac1s\right)
 =\frac4s+\frac{B-A}{a}
 =\lambda\cdot(1,-1,A,B).                               \tag{15}
\]
Balancing realizes these at parameter cost (15) using at most four units.
Together with (7), this proves (3) and existence in both width conventions.

Every minimum has equality throughout (7). Its nonzero normalized atoms
must therefore be the signed atoms (12), and (13) fixes their total
coefficients to (14). Splitting an atom into repeated units does not change
the resulting function. This proves uniqueness as a function, including at
the non-strict label boundaries in (1).

Finally \(-v=be_1-ae_2\), and
\(\sigma(t)+\sigma(-t)=|t|\) groups the terms independent of \(A,B\)
in (2) into \((|u\cdot x|-|v\cdot x|)/s\), as claimed.

## 4. Cancellation, bounded functions, and the limiting risk

Write \(t=x\cdot e_1\) and \(z=x\cdot e_2\). The elementary identity
\[
 |P+Q|-|P-Q|=2\operatorname{sign}(PQ)\min\{|P|,|Q|\}
\]
holds by considering the signs of \(P,Q\) and whether \(|P|\ge|Q|\).
With \(P=bt\), \(Q=az\), it yields
\[
 f_{0,\theta}(x)
 =\operatorname{sign}(tz)\min\left\{\frac{|t|}{a},
                                          \frac{|z|}{b}\right\},
 \qquad |f_{0,\theta}(x)|\le\frac{|t|}{a}.               \tag{16}
\]
The value is zero when \(tz=0\). In particular, on the unit ball,
\[
 |f_\theta(x)|\le\frac{1+|A|+|B|}{a}.                   \tag{17}
\]
Thus for bounded labels the functions remain uniformly bounded as
\(\theta\downarrow0\). This proves the uniform scaled-function limit
in (4), directly, without passing through a risk estimate. Equation (3)
also gives \(\theta Q_{\min}\to4\).

For \(z\ne0\), (16) gives
\(f_{0,\theta}(x)\to t\operatorname{sign}(z)\), while
\(v\to e_2\) and \(-u\to-e_2\). Hence outside the equator the pointwise
limit of (2) is
\[
 F_{A,B}(x)=t\operatorname{sign}(z)+A\sigma(z)+B\sigma(-z).
                                                               \tag{18}
\]
The equator has zero surface measure. Bound (17) and dominated convergence
give convergence in every finite \(L_p\), including the squared-risk limit.
This passage is uniform over bounded labels: the base term in (16) is
independent of the labels, and the difference between each correction atom
in (2) and its limit is uniformly small by the ReLU Lipschitz bound.

For uniform \(X\in S^{d-1}\), coordinate symmetry gives
\(\mathbb E X_1^2=1/d\), and reflection of the second coordinate gives
\(\mathbb E\sigma(\pm X_2)^2=1/(2d)\). The two ReLUs in (18) have
disjoint positive supports. The cross terms involving
\(X_1\operatorname{sign}(X_2)\) have expectation zero by reflection
of \(X_1\). Consequently
\[
 \mathbb E F_{A,B}(X)^2
 =\frac1d+\frac{A^2+B^2}{2d},                            \tag{19}
\]
which proves the last assertion of (4).

There is a separate check on the cancellation of the large odd component.
For any normalized atomic representation, the odd part is
\(\tfrac12(\sum_j\gamma_j r_j)\cdot x\). Substitution of (14) cancels
all terms proportional to \(1/s\), leaving
\[
 \sum_j\gamma_j r_j
 =-\frac{b(A+B)}a e_1+(A-B)e_2.
\]
Thus the odd-part risk is exactly
\[
 R_{\rm odd}=\frac1{4d}\left[\frac{b^2(A+B)^2}{a^2}
                                      +(A-B)^2\right].
\]
Its limit is \((A-B)^2/(4d)\). The even part of (18) is
\(X_1\operatorname{sign}(X_2)+(A+B)|X_2|/2\), with squared norm
\(1/d+(A+B)^2/(4d)\). Adding the two orthogonal parts recovers (19).

The unscaled convergence is not uniform in \(x\). Already for \(A=B=0\),
the limit takes opposite values near the two sides of the equator where
\(t\ne0\), while every \(f_{0,\theta}\) is continuous and zero at \(z=0\).
The uniform convergence asserted in (4) concerns \(\theta f_\theta\).

## 5. Exact risk, and a separate derivation of its limit

For unit vectors \(r,t\) at angle \(\beta\in[0,\pi]\), define
\(K_d(\beta)=\mathbb E\sigma(r\cdot X)\sigma(t\cdot X)\).
To obtain its normalization, write a standard Gaussian vector as \(G=\rho X\).
Direction and radius are independent, and \(\mathbb E\rho^2=d\).
In the plane of \(r,t\), the Gaussian polar angle is uniform and the squared
planar radius has mean two. The interval on which both projections are
positive can be taken as \([\beta-\pi/2,\pi/2]\). Thus
\[
 d K_d(\beta)=\frac1\pi\int_{\beta-\pi/2}^{\pi/2}
                      \cos\phi\cos(\phi-\beta)\,d\phi
 =\frac{\sin\beta+(\pi-\beta)\cos\beta}{2\pi}.           \tag{20}
\]
The last equality is product-to-sum integration. By continuity it includes
the parallel and antiparallel endpoints.

Since \(|r\cdot X|=\sigma(r\cdot X)+\sigma(-r\cdot X)\), summing
four terms from (20) gives
\[
 M_d(\beta):=\mathbb E|r\cdot X||t\cdot X|
 =2K_d(\beta)+2K_d(\pi-\beta)
 =\frac{2\sin\beta+(\pi-2\beta)\cos\beta}{\pi d}.        \tag{21}
\]
The angle between \(u\) and \(v\) is \(\theta\). Squaring the base term
in (2) and using \(\mathbb E(u\cdot X)^2=1/d\) gives
\[
 R_0(\theta)=\frac{2/d-2M_d(\theta)}{s^2},               \tag{22}
\]
which is the formula preceding (5).

The base term is centrally even. Its products with the odd parts of either
correction atom integrate to zero. Therefore, putting \(M=M_d(\theta)\),
\[
 \mathbb E[f_{0,\theta}(X)\sigma(v\cdot X)]
       =\frac{M-1/d}{2s},\qquad
 \mathbb E[f_{0,\theta}(X)\sigma((-u)\cdot X)]
       =\frac{1/d-M}{2s}.                               \tag{23}
\]
Twice the cross product with the corrections in (2) is consequently
\[
 \frac{B-A}{as}(1/d-M)=b(B-A)R_0(\theta),                \tag{24}
\]
where (22) and \(s=2ab\) were used. The angle between \(v\) and \(-u\)
is \(\pi-\theta\), so the squared norm of the correction is
\[
 \frac{A^2+B^2}{2d a^2}
       +\frac{2AB}{a^2}K_d(\pi-\theta)
 =\frac{A^2+B^2}{2d a^2}
       +\frac{AB(s-\theta\cos\theta)}{\pi d a^2}.         \tag{25}
\]
Equations (22), (24), and (25) prove (5).

For an independent evaluation, (16) makes the squared base function on
the circle equal to \(\min\{\cos^2\phi/a^2,\sin^2\phi/b^2\}\).
In the first quadrant the switch is at \(h=\theta/2\). Symmetry and
elementary antiderivatives yield, in dimension two,
\[
 R_{0,2}=\frac2\pi\left[
    \frac1{b^2}\int_0^h\sin^2\phi\,d\phi
   +\frac1{a^2}\int_h^{\pi/2}\cos^2\phi\,d\phi\right]
 =\frac1\pi\left[\frac{h-ab}{b^2}
                 +\frac{\pi/2-h-ab}{a^2}\right].         \tag{26}
\]
For a homogeneous function depending on just the first two coordinates,
the spherical angle is uniform and independent of the planar radius; the
mean squared planar radius is \(2/d\). Thus its risk is \(2/d\) times
its circle risk. Applying this fact to (26) gives a second exact expression
for (22) in every \(d\ge2\). To check their equality directly, put (26)
over the denominator \(a^2b^2\), use \(h=\theta/2\),
\(a^2-b^2=\cos\theta\), and \(2ab=s\).

One convenient equivalent form is
\[
 R_0(\theta)=\frac1{d a^2}
       -\frac{4(s-\theta\cos\theta)}{\pi d s^2}.         \tag{27}
\]
Since
\[
 s-\theta\cos\theta=\int_0^\theta t\sin t\,dt
                   =\frac{\theta^3}{3}+O(\theta^5),
\]
(27) gives \(R_0\to1/d\). Substitution into (5) independently recovers
(19). It also gives, uniformly over \(|A|,|B|\le H\),
\[
 R(f_\theta)=\frac{1+(A^2+B^2)/2}{d}
       +\frac\theta d\left(\frac{B-A}{2}-\frac4{3\pi}\right)
       +O_{H,d}(\theta^2).                              \tag{28}
\]

## 6. Scope and the role of the additional observations

The one-hemisphere theorem has leading cost \(2/\sin\theta+O(1)\)
and risk asymptotic to \(2/(d\theta^2)\). Here the antipodal fourth
constraint changes the leading cost to \(4/\sin\theta+O(1)\), and forces
cancellation of the leading function. Equations (16)--(19) show that
the risk remains bounded even though interpolation forces the local slope
between the close pair to diverge. In particular, such a slope alone is
not a lower bound of order \(\theta^{-2}\) on population risk.

Condition (1) is substantive for the exact optimizer formula. If it fails,
(14) still interpolates, but its coefficient signs no longer attain (7);
no minimum or risk formula is claimed there. For bounded labels, all
sufficiently small angles satisfy (1).

For \(0<\theta<\pi/2\), at the boundary \(A=1/(2b)\), \(B=-1/(2b)\),
the coefficients of \(v\)
and \(-u\) in (14) vanish. The function reduces to the original two-point
minimum \([\sigma(u\cdot x)-\sigma((-v)\cdot x)]/s\), and (3) reduces
to \(2/s\). Its risk is
\([\pi-s+\theta\cos\theta]/(\pi d s^2)\), as also follows from (5).
These angle-dependent additional labels are unbounded as \(\theta\downarrow0\);
their risk again grows as \(1/(d\theta^2)\). Boundedness of the labels in
(4) is therefore necessary.

All four sample points lie in a plane, but the optimization allows arbitrary
ambient weights; the equality analysis in Section 2 forces every minimizing
nonzero direction into that plane. Biases, skips, GD selection, nonantipodal
opposite-hemisphere extras, and random-design large-sample risk are outside
this theorem. The finite limiting risk in this deterministic family is
compatible with the predecessor's infinite training-averaged risks.
