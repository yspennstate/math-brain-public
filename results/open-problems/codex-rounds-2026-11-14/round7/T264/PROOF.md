# Finite risk moments below the projective collision threshold

Let \(\sigma(t)=\max(t,0)\). For \(d\ge2\), consider homogeneous
two-layer ReLU networks
\[
 f(x)=\sum_{j=1}^m a_j\sigma(w_j\cdot x),\qquad
 Q(a,w)=\frac12\sum_{j=1}^m(a_j^2+\|w_j\|^2).
\]
There are no biases, skips or output intercepts. Width is unrestricted, or
fixed at any \(m\ge n\), where \(n\ge2\) is the sample size. A minimum
means a global minimum of \(Q\) subject to interpolation. Surface measure
on \(S^{d-1}\) is normalized to mass one, and
\[
 R(f)=\mathbb E_{X\sim\mathrm{Unif}(S^{d-1})} f(X)^2.
\]
The reference regression function is zero.

## Theorem

Let \(x_1,\ldots,x_n\in S^{d-1}\) be pairwise nonparallel, and let
\(|y_i|\le H<\infty\). Define
\[
 s_{ij}=\sqrt{1-(x_i\cdot x_j)^2},\qquad
 \delta=\min_{i<j}s_{ij}>0,
\]
\[
 K_{n,d}=n\bigl[2+32(n-1)\sqrt{d-1}\bigr].                 \tag{1}
\]
A minimum exists in both width conventions above, and every minimum
satisfies
\[
 Q_{\min}\le\frac{H K_{n,d}}\delta,
 \qquad
 R(f)\le\frac{H^2K_{n,d}^2}{2d\delta^2}.                 \tag{2}
\]

Now let the training inputs be iid uniform on \(S^{d-1}\), and let the
labels obey \(|Y_i|\le H\) almost surely. For any measurable selection of
minima and every \(0<r<(d-1)/2\),
\[
 \mathbb E R(f_n)^r
 \le\left(\frac{H^2K_{n,d}^2}{2d}\right)^r
 {n\choose2}
 \frac{B((d-1-2r)/2,\,1/2)}{B((d-1)/2,\,1/2)}
 <\infty.                                               \tag{3}
\]
In particular, for \(d\ge4\),
\[
 \boxed{\mathbb E R(f_n)
 \le\frac{H^2K_{n,d}^2}{2d}{n\choose2}\frac{d-2}{d-3}
 <\infty.}                                              \tag{4}
\]
For independent Rademacher labels, this expectation is strictly positive.
The constants in (1)--(4) are not uniform in \(n\).

Combined with the round-5 lower-moment theorem, the Rademacher model has
the exact moment threshold, for every fixed \(n\ge3\) and \(d\ge2\),
\[
 \boxed{\mathbb E R(f_n)^r<\infty
 \quad\Longleftrightarrow\quad 0<r<(d-1)/2.}              \tag{5}
\]
The lower bound in that theorem also gives, together with (2),
\[
 \mathbb P(R(f_n)>t)=\Theta_{n,d}(t^{-(d-1)/2})
 \quad(t\to\infty).                                    \tag{6}
\]
The two constants in (6) need not agree. This is not an exact tail
asymptotic.

## 1. Atomic cost and risk

For each unit with \(w_j\ne0\), set
\(u_j=w_j/\|w_j\|\) and \(\gamma_j=a_j\|w_j\|\).
Discard zero units. Homogeneity gives
\[
 f(x)=\sum_j\gamma_j\sigma(u_j\cdot x),\qquad \|u_j\|=1,
 \qquad T:=\sum_j|\gamma_j|\le Q,                        \tag{7}
\]
because \((a_j^2+\|w_j\|^2)/2\ge |a_j|\|w_j\|\).
Conversely, an atomic coefficient \(\gamma\) at a unit direction \(u\)
is realized at parameter cost \(|\gamma|\) by
\[
 a=\operatorname{sign}(\gamma)\sqrt{|\gamma|},\qquad
 w=\sqrt{|\gamma|}\,u.
\]
For an unnormalized direction \(v\), the term
\(c\sigma(v\cdot x)\) therefore has a realization with cost
\(|c|\|v\|\).

For a unit \(u\), reflection symmetry and rotational invariance give
\[
 \|\sigma(u\cdot X)\|_{L_2}^2
 =\tfrac12\mathbb E(u\cdot X)^2=\frac1{2d}.
\]
The triangle inequality in \(L_2\), applied to (7), yields
\[
 R(f)^{1/2}\le\frac{T}{\sqrt{2d}}\le\frac Q{\sqrt{2d}}.
                                                               \tag{8}
\]
This bound applies to every parameter representation.

## 2. One tangent direction separates finitely many projections

Let \(V\) be a Euclidean space of dimension \(k\ge1\), and let
\(v_1,\ldots,v_N\) be unit vectors in \(V\), with \(N\ge1\).
There exists a unit \(z\in V\) such that
\[
 |z\cdot v_j|\ge\frac1{8N\sqrt{k}}
 \quad(1\le j\le N).                                    \tag{9}
\]

To see this, let \(G\) be a standard Gaussian in \(V\) and put
\(\varepsilon=1/(4N)\). Each \(G\cdot v_j\) is a standard scalar
Gaussian, so its density is bounded by \(1/\sqrt{2\pi}\). Hence
\[
 \mathbb P(|G\cdot v_j|<\varepsilon)
 \le\sqrt{2/\pi}\,\varepsilon<\varepsilon.
\]
The union bound gives probability less than \(1/4\) that any of these
inequalities fails. Also \(\mathbb E\|G\|^2=k\), so Markov's inequality
gives
\[
 \mathbb P(\|G\|>2\sqrt{k})\le\tfrac14.
\]
Thus there is a nonzero \(G\) with \(\|G\|\le2\sqrt{k}\) and
\(|G\cdot v_j|\ge\varepsilon\) for every \(j\). Setting
\(z=G/\|G\|\) proves (9). No independence among these scalar Gaussian
projections is required.

Fix an index \(i\), and put \(e=x_i\) and
\(V=e^\perp\), of dimension \(k=d-1\). For \(j\ne i\), the vectors
\[
 v_j=\frac{x_j-(e\cdot x_j)e}{s_{ij}}
\]
are well-defined unit vectors in \(V\). Apply (9) with \(N=n-1\).
There is a unit \(z_i\perp x_i\) such that
\[
 |z_i\cdot x_j|=s_{ij}|z_i\cdot v_j|
 \ge\frac{s_{ij}}{C},\qquad
 C=8(n-1)\sqrt{d-1}.                                    \tag{10}
\]
This includes \(d=2\), where \(V\) is a line.

There is a second derivation of (9) using a uniform direction directly.
For \(k=1\), either unit direction has absolute projection one. For
\(k\ge2\), the coordinate \(Z\) of a uniform point on \(S^{k-1}\)
has density
\[
 c_k(1-t^2)^{(k-3)/2},\quad -1<t<1,\qquad
 c_k=\frac{\Gamma(k/2)}{\sqrt\pi\Gamma((k-1)/2)}.
\]
This follows by writing the polar angle density as
\(\sin^{k-2}\theta/J_{k-2}\), then changing variables
\(t=\cos\theta\); (18) supplies the normalizer.
For \(k\ge3\) this density is at most \(c_k\le\sqrt{k}\).
For the last inequality, put \(x=(k-1)/2>0\) and apply Cauchy--Schwarz
to the gamma integral to obtain
\[
 \Gamma(x+1/2)^2
 \le\Gamma(x)\Gamma(x+1)=x\Gamma(x)^2,
 \qquad c_k\le\sqrt{x/\pi}<\sqrt{k}.
\]
For \(k=2\) and \(|t|\le1/2\), the density is at most
\(2/(\pi\sqrt3)<1<\sqrt{k}\). Thus for every \(k\ge2\) and
\(0<\eta\le1/2\),
\(\mathbb P(|Z|<\eta)\le2\sqrt{k}\eta\).
Take \(\eta=1/(8N\sqrt{k})\) and use a union bound over the \(N\)
vectors: the forbidden probability is at most \(1/4\). This gives
(9) again without a Gaussian length truncation.

## 3. Three-ReLU interpolation tents

For real numbers \(s,t\),
\[
 \sigma(s+t)+\sigma(s-t)-2\sigma(s)
 =\bigl(|t|-|s|\bigr)_+.                               \tag{11}
\]
Indeed \(\sigma(v)=(v+|v|)/2\) makes the left side
\((|s+t|+|s-t|-2|s|)/2\). If \(|s|\ge|t|\), then
\(|s+t|+|s-t|=2|s|\); otherwise it equals \(2|t|\).
These two cases prove (11), including equality at the boundary.

Set
\[
 \delta_i=\min_{j\ne i}s_{ij},\qquad L_i=C/\delta_i,
\]
and define
\[
 \begin{split}
 h_i(x)
 &=\sigma((L_i z_i+x_i)\cdot x)
   +\sigma((L_i z_i-x_i)\cdot x)
   -2\sigma(L_i z_i\cdot x)\\
 &=\bigl(|x_i\cdot x|-L_i|z_i\cdot x|\bigr)_+.
 \end{split}                                            \tag{12}
\]
At \(x_i\), orthogonality gives \(h_i(x_i)=1\).
For \(j\ne i\), (10) gives
\[
 L_i|z_i\cdot x_j|\ge s_{ij}/\delta_i\ge1
 \ge |x_i\cdot x_j|,
\]
so \(h_i(x_j)=0\). Thus
\[
 F(x)=\sum_{i=1}^n y_i h_i(x)                            \tag{13}
\]
interpolates all labels, using at most \(3n\) ReLU units.

Since \(z_i\perp x_i\), the two outer weight vectors in (12) have
norm \(\sqrt{1+L_i^2}\). Section 1 gives atomic cost
\[
 T(h_i)\le2\sqrt{1+L_i^2}+2L_i
 \le2+4L_i
 \le\frac{2+4C}{\delta_i}.                              \tag{14}
\]
The middle inequality uses \(\sqrt{1+L^2}\le1+L\) for \(L\ge0\),
and the last uses \(0<\delta_i\le1\). Therefore (13) has cost at most
\[
 \sum_i|y_i|\frac{2+4C}{\delta_i}
 \le\frac{Hn(2+4C)}\delta
 =\frac{HK_{n,d}}\delta.                                \tag{15}
\]
The tents are even functions. This imposes no restriction on the prescribed
values because no two observed points are parallel. The construction is
allowed to assign the same value at the unobserved antipode of a sample.

## 4. Reduction to n units and existence

For the given observations write
\[
 A(u)=(\sigma(u\cdot x_1),\ldots,\sigma(u\cdot x_n))
 \in\mathbb R^n.
\]
Any finite atomic interpolant gives a representation
\[
 y=\sum_{j=1}^M\beta_j a_j,
 \qquad \beta_j>0,\quad a_j\in\{A(u),-A(u):\|u\|=1\},  \tag{16}
\]
with cost \(\sum_j\beta_j\). Zero coefficients have been removed.

If \(M>n\), take a nonzero real dependence
\(\sum_j t_j a_j=0\). Replace \(t\) by \(-t\) if needed so that
\(\sum_j t_j\ge0\) and some \(t_j>0\). Such a sign always exists:
when the sum is positive there must be a positive entry, and when it is
zero a nonzero vector has entries of both signs. Put
\[
 \lambda=\min_{j:t_j>0}\frac{\beta_j}{t_j}>0,
 \qquad \beta'_j=\beta_j-\lambda t_j.
\]
All \(\beta'_j\) are nonnegative and at least one is zero. The represented
label vector is unchanged, while
\[
 \sum_j\beta'_j=\sum_j\beta_j-\lambda\sum_jt_j
 \le\sum_j\beta_j.
\]
Remove the zero coefficients and repeat. This reduces (16) to at most
\(n\) atoms without increasing cost. Balancing these atoms gives at most
\(n\) parameter units with the same or lower cost. The represented
function outside the sample need not be preserved.

Apply this reduction to (13). A competitor of width at most \(n\)
satisfies (15), and zero units pad it to any \(m\ge n\).
At fixed width \(m\), interpolation constraints are closed and every
bounded \(Q\) sublevel is compact in the finite-dimensional parameter
space. A minimizing sequence in the sublevel supplied by (15) therefore
has a feasible convergent subsequence and attains its minimum.

Every finite-width feasible network can likewise be compressed to width
at most \(n\) with no increase in parameter cost, by (7) and the reduction
above. Hence the infimum over all finite widths equals the minimum at
width \(n\), and is attained there. This proves unrestricted-width
existence as well. Bound (15) now holds for the minimum in either width
convention; (8) proves (2) for every minimizer.

## 5. Integrating the bound

Pairwise nonparallelism holds almost surely for iid uniform spherical
inputs: for a fixed point its two parallel directions have surface
measure zero when \(d\ge2\), and there are finitely many pairs.

The angle \(\Theta\in(0,\pi)\) between an independent spherical pair has
density
\[
 \frac{\sin^{d-2}\theta}{J_{d-2}},\qquad
 J_p=\int_0^\pi\sin^p\theta\,d\theta.                   \tag{17}
\]
Spherical polar coordinates about the first point give the sine power
and its normalization. For \(p>-1\), symmetry about \(\pi/2\) and the
substitution \(t=\sin^2\theta\) give
\[
 J_p=\int_0^1 t^{(p-1)/2}(1-t)^{-1/2}\,dt
 =B((p+1)/2,1/2).                                      \tag{18}
\]
The integral is finite exactly when \(p>-1\), as follows by comparing
\(\sin\theta\) to \(\theta\) near zero and to \(\pi-\theta\) near
\(\pi\).

For \(r>0\),
\[
 \delta^{-2r}=\max_{i<j}s_{ij}^{-2r}
 \le\sum_{i<j}s_{ij}^{-2r}.
\]
No independence between these pair variables is needed. Using (17)--(18),
\[
 \mathbb E\delta^{-2r}
 \le {n\choose2}\frac{J_{d-2-2r}}{J_{d-2}}
 ={n\choose2}
 \frac{B((d-1-2r)/2,1/2)}{B((d-1)/2,1/2)}<\infty
                                                               \tag{19}
\]
when \(2r<d-1\). Combining (2) and (19) proves (3).

For \(r=1\) and \(d>3\), integration by parts gives
\[
 J_m=(m-1)(J_{m-2}-J_m),\qquad
 J_m=\frac{m-1}{m}J_{m-2}\quad(m>1).
\]
For the first identity integrate \(\sin^{m-1}\theta\sin\theta\),
differentiating the first factor and integrating the last; the boundary
term vanishes. Taking \(m=d-2\) gives
\[
 \mathbb E(\sin\Theta)^{-2}
 =\frac{J_{d-4}}{J_{d-2}}=\frac{d-2}{d-3}.               \tag{20}
\]
Equations (2) and (19)--(20) prove (4). Independently, (18) and
\(\Gamma(z+1)=z\Gamma(z)\) give the same ratio in (20).

If a continuous interpolant has any nonzero label, it is nonzero on a
relatively open neighborhood of that sample on the sphere. This neighborhood
has positive surface measure, so \(R(f)>0\). Rademacher labels are nonzero;
therefore the finite expectation in (4) is strictly positive.

## 6. Matching the existing lower threshold

The lower bound used here is Theorem 2 in
`~/codex_op_1114r5/briefs/T264/PROOF.md`.
For the same homogeneous model, width allowance, iid uniform spherical
inputs, independent Rademacher labels and every measurable minimizing
selection, it proves for fixed \(n\ge3\)
\[
 \liminf_{t\to\infty}t^\alpha\mathbb P(R(f_n)>t)
 \ge c_{n,d}>0,
 \quad \alpha=(d-1)/2,
\]
\[
 c_{n,d}=\frac{2^{2-n}C_d}{d-1}(2/d)^\alpha,
 \qquad C_d=1/J_{d-2}.                                 \tag{21}
\]
Its event is an opposite-label close pair with all remaining points in
one separation hemisphere; its joint sign probability is \(2^{2-n}\).
The cited theorem supplies the lower bound, rather than an inference
from the deterministic antipodal configuration.

For completeness, (2) supplies a matching upper power. Let
\(A=H^2K_{n,d}^2/(2d)>0\). For \(t\ge4A\), put
\(u=\sqrt{A/t}\le1/2\). Then
\[
 \{R(f_n)>t\}\subseteq\{\delta<u\}.
\]
For one pair, \(\sin\Theta<u\) consists of the two angular caps at
zero and \(\pi\). Thus a union bound and (17) give
\[
 \begin{split}
 \mathbb P(R(f_n)>t)
 &\le {n\choose2}\,2C_d
       \int_0^{\arcsin u}\sin^{d-2}\theta\,d\theta\\
 &\le {n\choose2}\frac{2C_d}{d-1}(2u)^{d-1}.
 \end{split}                                            \tag{22}
\]
Here \(\sin\theta\le\theta\) and
\(\arcsin u=\int_0^u(1-v^2)^{-1/2}\,dv\le2u\) for \(u\le1/2\).
For Rademacher labels take \(H=1\). Combining (21)--(22) proves (6).

Finally, Tonelli's theorem applied to
\(R^r=\int_0^R rt^{r-1}\,dt\) yields
\[
 \mathbb E R^r=r\int_0^\infty t^{r-1}\mathbb P(R>t)\,dt.
\]
The positive lower bound (21) makes this infinite for \(r\ge\alpha\),
including the logarithmic endpoint \(r=\alpha\). Bound (3) proves the
other direction, giving (5). For \(n=2\), the same threshold follows
by combining (3) with the exact two-point theorem in the first predecessor.

## Scope

For every fixed \(n\), the mean risk is finite in \(d\ge4\), while the
previous lower theorem makes it infinite in \(d=2,3\) with Rademacher
labels. Finiteness at each \(n\) does not imply boundedness of the sequence
of mean risks as \(n\to\infty\). The bound (4) grows with \(n\), so it
does not determine that limit or classify convergence in probability.
No conclusion is drawn about GD, narrower fixed widths, penalized biases,
free affine components, or other input distributions.
