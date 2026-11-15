# A centered quadratic drift and the suppression of low modes

Let \(M\geq3\), \(\mathbb T_M=(\mathbb Z/M\mathbb Z)^2\), and
\[
B_{ab}=\frac15(\mathbf1_{a=b}+\mathbf1_{a\sim b}).
\]
Let \(P_{ab}=M^{-2}\), \(Q=I-P\), \(A=I-B\), and, for \(0\leq u<1\),
\[
G_u=(I-uB)^{-1},\qquad H_u=G_uQ,\qquad
U_{u,t}=(I-uB)G_t\quad(0\leq u\leq t<1).
\tag{1}
\]
All these matrices commute. The eigenvalues of \(B\), indexed by
\(\Lambda_M=\{-\lfloor M/2\rfloor,\ldots,\lceil M/2\rceil-1\}^2\), are
\[
b_k=\frac{1+2\cos(2\pi k_1/M)+2\cos(2\pi k_2/M)}5,
\qquad a_k=1-b_k.
\tag{2}
\]
Thus \(-3/5\leq b_k\leq1\), and \(a_k=0\) precisely for \(k=0\).
Write \(g_u(k)=1-ub_k=1-u+ua_k>0\).
For a measurable matrix family \(D(u)\), define the quadratic Duhamel term
\[
\mathcal J_t[D]=W^2\int_0^t
 U_{u,t}D(u)BD(u)U_{u,t}\,du,
\tag{3}
\]
whenever the entries are integrable. Here \(W\geq1\).

The centered return diagonal from the preceding work is
\[
r_M(t)=(H_t)_{00}=\frac1{M^2}\sum_{k\ne0}\frac1{g_t(k)}.
\tag{4}
\]
For \(1/2\leq t<1\), that work gives, uniformly,
\[
r_M(t)=\frac5{4\pi}\log\frac1{1-t+M^{-2}}+O(1),
\qquad r_M(1)=\frac5{2\pi}\log M+O(1).
\tag{5}
\]
At \(t=1\), all matrices in this text are restricted to \(Q\) before
taking their finite-dimensional limits. The proof below uses (5) only
to express its bounds in logarithmic form.

## A sufficient condition without an additional logarithm

Suppose that \(D(u)\) is real symmetric and translation invariant, so its
Fourier eigenvalues \(d_u(k)\) are real. Fix \(\delta\geq0\). Suppose, for
almost every \(u\in[0,t]\), that
\[
d_u(0)=0,\qquad
|d_u(k)|\leq\frac{\delta u}{W^2}
                    \frac{a_k}{g_u(k)^2}\quad(k\ne0).
\tag{6}
\]
Equivalently, in the order on real symmetric matrices,
\[
-\frac{\delta u}{W^2}AG_u^2Q
\preceq D(u)\preceq\frac{\delta u}{W^2}AG_u^2Q.
\]
Translation invariance is part of the hypothesis; this assertion is not
made for arbitrary matrices satisfying just these order inequalities.

Then the integral (3) exists and
\[
-\frac{\delta^2t}{W^2}H_t
\preceq\mathcal J_t[D]\preceq\frac{\delta^2t}{W^2}H_t.
\tag{7}
\]
In particular, for every pair of vertices,
\[
|\mathcal J_t[D]_{ab}|
\leq\frac{\delta^2t}{W^2}r_M(t)
\leq\frac{C\delta^2}{W^2}(1+\log M).
\tag{8}
\]
For \(t\geq1/2\), the first bound and (5) give the more precise bound
\[
|\mathcal J_t[D]_{ab}|\leq\frac{\delta^2t}{W^2}
 \left[\frac5{4\pi}\log\frac1{1-t+M^{-2}}+C\right].
\tag{9}
\]

### Proof

The case \(t=0\) is immediate. Fix \(0<t<1\). The eigenvalue of
\(U_{u,t}\) at \(k\) is \(g_u(k)/g_t(k)\). Thus the eigenvalue of (3) is
\[
j_t(k)=\frac{W^2b_k}{g_t(k)^2}
                \int_0^t g_u(k)^2d_u(k)^2\,du.
\tag{10}
\]
It vanishes at \(k=0\). For \(k\ne0\), (6) gives
\[
|j_t(k)|\leq\frac{\delta^2}{W^2}
 \frac{|b_k|a_k^2}{g_t(k)^2}
 \int_0^t\frac{u^2}{g_u(k)^2}\,du.
\tag{11}
\]
For any real \(b\) with \(1-ub>0\) on this interval,
\[
\frac{d}{du}\frac{u}{1-ub}=\frac1{(1-ub)^2}.
\]
Consequently, without dividing by \(b\),
\[
\int_0^t\frac{u^2}{(1-ub)^2}\,du
\leq t^2\int_0^t\frac{du}{(1-ub)^2}
=\frac{t^3}{1-tb}.
\tag{12}
\]
This covers zero and negative eigenvalues. Since \(g_t(k)\geq ta_k\),
\[
|j_t(k)|\leq\frac{\delta^2t}{W^2g_t(k)}
 |b_k|\left(\frac{ta_k}{g_t(k)}\right)^2
\leq\frac{\delta^2t}{W^2g_t(k)}.
\tag{13}
\]
All integrals are finite for fixed \(t<1\), and (13) proves (7).
Fourier inversion, whose characters have modulus one, gives
\[
|\mathcal J_t[D]_{ab}|\leq\frac1{M^2}\sum_{k\ne0}|j_t(k)|
\leq\frac{\delta^2t}{W^2}r_M(t).
\]
For \(t\leq1/2\), \(g_t(k)\geq1/2\), hence \(r_M(t)\leq2\).
For later times apply (5), which proves (8) and (9).

The conclusion retains the one logarithm already in the return kernel.
Condition (6) includes the factor \(a_k/g_u(k)\) relative to
\(\delta uW^{-2}H_u\). If \(1-u\gg a_k\), this factor is small.

## Why the relative centered-kernel envelope alone does not suffice

Consider instead the smooth family
\[
D_\delta(u)=\frac{\delta u}{W^2}H_u,\qquad\delta>0.
\tag{14}
\]
It is real symmetric, translation invariant and positive semidefinite,
has zero row sums, and satisfies \(D_\delta(0)=0\). In particular it
satisfies the weaker relative envelope
\[
0\preceq D_\delta(u)\preceq\frac{\delta u}{W^2}H_u
\tag{15}
\]
with equality. Nevertheless its quadratic drift has the exact value
\[
\mathcal J_t[D_\delta]
=\frac{\delta^2t^3}{3W^2}BG_t^2Q.
\tag{16}
\]
Indeed \(U_{u,t}H_u=G_tQ\); insert (14) into (3), commute the
deterministic factors, and integrate \(\int_0^t u^2du=t^3/3\).
This calculation includes the propagator in both coordinates.

For \(t_M=1-M^{-4}\), its diagonal satisfies
\[
\mathcal J_{t_M}[D_\delta]_{00}
=\frac{\delta^2}{W^2}\left[c_*M^2+O(\log M)\right],
\qquad
c_*:=\frac{25}{48\pi^4}
          \sum_{k\in\mathbb Z^2\setminus\{0\}}\frac1{|k|^4}>0.
\tag{17}
\]
The implied constant is absolute. The same formula holds uniformly
for \(0<1-t\leq M^{-4}\).

### Proof of the coefficient and error in (17)

Put \(\alpha=4\pi^2/5\). The elementary cosine bounds on
\([-\pi,\pi]^2\) imply
\[
a_k\asymp |k|^2/M^2,\qquad
\left|a_k-\alpha|k|^2/M^2\right|\leq C|k|^4/M^4.
\tag{18}
\]
These estimates are uniform over the representatives in (2).
For \(v_k=\alpha|k|^2/M^2\), taking differences of reciprocal squares
gives
\[
|a_k^{-2}-v_k^{-2}|
=\frac{|a_k-v_k|(a_k+v_k)}{a_k^2v_k^2}
\leq C M^2/|k|^2.
\tag{19}
\]
Also \(a_k^{-1}\leq CM^2/|k|^2\). Since \(b_k=1-a_k\),
\[
\left|\frac{b_k}{a_k^2}-\frac{M^4}{\alpha^2|k|^4}\right|
\leq CM^2/|k|^2.
\tag{20}
\]
The shell \(\|k\|_\infty=n\) has \(8n\) points, so summing (20)
and dividing by \(M^2\) costs at most \(C(1+\log M)\).
Every integer point excluded from \(\Lambda_M\) has
\(\|k\|_\infty\geq(M-1)/2\). The same shell count yields
\[
\sum_{k\notin\Lambda_M}|k|^{-4}\leq C M^{-2}.
\tag{21}
\]
It follows that
\[
\frac1{M^2}\sum_{k\ne0}\frac{b_k}{a_k^2}
=\frac{M^2}{\alpha^2}
  \sum_{k\in\mathbb Z^2\setminus\{0\}}|k|^{-4}+O(\log M).
\tag{22}
\]
The negative Fourier eigenvalues are included in the error estimate;
no positivity of \(B\) has been assumed.

It remains to justify the positive mass cutoff. Write \(\mu=1-t\).
For \(0\leq\mu\leq M^{-4}\), \(t\geq1/2\) and
\(g_t(k)=\mu+(1-\mu)a_k\geq a_k/2\). Differentiating
\(b_k/\bigl(\mu+(1-\mu)a_k\bigr)^2\) with respect to \(\mu\)
gives \(-2b_k^2/\bigl(\mu+(1-\mu)a_k\bigr)^3\). Hence
\[
\left|\frac1{M^2}\sum_{k\ne0}
 \left[\frac{b_k}{g_t(k)^2}-\frac{b_k}{a_k^2}\right]\right|
\leq\frac{C\mu}{M^2}\sum_{k\ne0}a_k^{-3}
\leq C\mu M^4\leq C.
\tag{23}
\]
The last sum is bounded using (18) and
\(\sum_{k\ne0}|k|^{-6}<\infty\), again by square shells.
Finally \(|t^3-1|\leq3\mu\); (22) is \(O(M^2)\), so multiplication
by \(t^3\) changes it by \(O(\mu M^2)=O(1)\).
Combining (16), (22) and (23), with \(1/(3\alpha^2)=25/(48\pi^4)\),
proves (17).

For a completely explicit magnitude check, the shell
\(\|k\|_\infty=1\) contributes \(4+4/4=5\) to the series defining
\(c_*\). The remaining terms are positive and at most
\[
8\sum_{n\geq2}n^{-3}
\leq8\left(\frac18+\int_2^\infty x^{-3}dx\right)=2.
\]
Thus
\[
\frac{125}{48\pi^4}<c_*\leq\frac{175}{48\pi^4}.
\tag{24}
\]
No numerical evaluation of this constant is required.

## Independent checks and limitations

There are two checks on the quadratic calculation. First, on \(Q\),
\(\partial_t H_t=BG_t^2Q\), so (16) also reads
\[
\mathcal J_t[D_\delta]_{00}
=\frac{\delta^2t^3}{3W^2}\,\partial_t r_M(t).
\tag{25}
\]
This derivative identity follows directly from differentiating
\((I-tB)G_t=I\), independently of the Duhamel cancellation.
One cannot differentiate the \(O(1)\) remainder in (5); (22)–(23)
are needed to estimate the derivative.

Second, since \(AG_1Q=Q\),
\[
BG_1^2Q=H_1^2-H_1.
\]
Translation invariance and symmetry therefore give the real-space identity
\[
(BG_1^2Q)_{00}=\sum_x(H_1)_{0x}^2-r_M(1).
\tag{26}
\]
Parseval's identity computes the first term as
\(M^{-2}\sum_{k\ne0}a_k^{-2}\). Applying (19) and (21) gives its
coefficient \(\alpha^{-2}\sum_{\mathbb Z^2\setminus0}|k|^{-4}\)
and its \(O(\log M)\) error a second way. Subtracting (5) costs only
\(O(\log M)\). The factor \(1/3\) then comes from the separate time
integral in (16). Both calculations yield (17).

As a finite-volume check, when \(M=3\) the nonconstant eigenvalues are
\(2/5\) and \(-1/5\), each four times. Direct substitution gives
\[
(BG_1^2Q)_{00}
=\frac49\left(\frac{2/5}{(3/5)^2}
                 -\frac{1/5}{(6/5)^2}\right)=\frac{35}{81},
\quad
\mathcal J_1[D_\delta]_{00}=\frac{35\delta^2}{243W^2}.
\tag{27}
\]
The check through (26) is
\(M^{-2}\sum a_k^{-2}=125/81\), minus \(r_3(1)=10/9\), again
giving \(35/81\). Even tori may have \(b_k=-3/5\); all the preceding
bounds retain these modes. Eigenvalues \(b_k=0\) give zero drift and
are covered by (12), which uses no inverse of \(b_k\).

The logarithmic order in (8) cannot be removed under (6) in general.
For the saturating family
\(D(u)=\delta uW^{-2}AG_u^2Q\), fix a nonzero mode with \(0<b_k<1\)
and set \(t=1\) on \(Q\). Equation (10) yields
\[
j_1(k)=\frac{\delta^2}{W^2}b_k
                         \int_0^1\frac{u^2}{(1-ub_k)^2}\,du.
\]
As \(a_k=1-b_k\downarrow0\), changing variables \(v=1-ub_k\)
shows
\[
a_k\int_0^1\frac{u^2}{(1-ub_k)^2}\,du
=\frac{a_k}{b_k^3}\left(a_k^{-1}+2\log a_k-a_k\right)\longrightarrow1.
\tag{28}
\]
Thus the estimate has the same low-frequency order as \(H_1\).
This also independently checks that the time integral in (12) loses
no logarithm at a low mode. More explicitly, for \(0<a_k\leq1/4\),
restricting the integral to \(1-a_k\leq u\leq1\) gives
\(j_1(k)\geq27\delta^2/(256W^2a_k)\).
Writing \(q_k=2\pi k/M\), modes with \(|q_k|\leq1\) have
\(a_k\leq1/5\); their sum of
\(a_k^{-1}\) has order \(M^2\log M\) by (18) and square shells.
The negative modes contribute at most \(C\delta^2/W^2\) to a diagonal:
there \(g_u(k)\geq1\), so (10) bounds each by
\(C\delta^2/W^2\). Therefore the diagonal for this family has order
\(\delta^2\log M/W^2\) as \(M\to\infty\).

By contrast, the weaker family (14) has
\[
\sup_{0\leq u<1}\max_{a,b}|D_\delta(u)_{ab}|
\leq C\delta\frac{1+\log M}{W^2}.
\tag{29}
\]
Indeed \(H_u\) is positive semidefinite, so its entries are bounded
by its common diagonal, and (5) together with the bound for \(u\leq1/2\)
controls that diagonal. Take integer \(W\to\infty\),
\(M=\lfloor e^W\rfloor\), and \(t=1-M^{-4}\). The bound in (29)
tends to zero, whereas (17) tends to positive infinity for fixed
\(\delta>0\). This failure is entirely in the nonconstant modes.

Neither family here is asserted to be a realizable random-resolvent
error. In particular, although (14) is positive semidefinite, the matrix
\(W^{-2}G_u+D_\delta(u)\) need not be entrywise nonnegative. For
distinct nonadjacent vertices its derivative at \(u=0\) is
\(-\delta/(W^2M^2)<0\), while its value at zero is zero. Such pairs
exist on every torus under consideration. Thus (14) is not a
counterexample under all positivity constraints of an actual two-loop
observable. It proves only that (15), centering, symmetry, translation
invariance, small entries, and zero initial error do not suffice.

For the same reason, (7) is a conditional deterministic statement.
No estimate of the form (6) for the random error has been established.
Random errors also need not commute with \(B\); off-diagonal Fourier
couplings would have to be controlled to apply an analogue of (7).

## Relation to the loop equation

In Xujie Lai and Fan Yang, *Localization Lengths for Two-Dimensional
Random Band Matrices: Exponential Lower Bounds*,
[arXiv:2609.24426v4](https://arxiv.org/html/2609.24426v4),
equations (2.33)–(2.39) give exactly the quadratic term and the
two-coordinate propagator in (3) for the alternating two-loop error.
The calculation above isolates that term with its constant mode removed.
It supplies a sufficient low-mode condition without an additional
logarithm and an obstruction to replacing that condition by a relative
centered-kernel bound. It yields no new eigenvector, localization-length,
or local-statistics theorem for random band matrices.
