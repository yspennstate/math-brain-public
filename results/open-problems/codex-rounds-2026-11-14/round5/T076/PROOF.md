# Noncommuting quadratic errors: temporal variation and a logarithmic loss

Let \(M\geq3\), let \(B=(I+\mathrm{adjacency})/5\) on
\((\mathbb Z/M\mathbb Z)^2\), and put
\[
P_{xy}=M^{-2},\qquad Q=I-P,\qquad A=I-B,\qquad
G_u=(I-uB)^{-1},\qquad H_u=G_uQ.
\tag{1}
\]
The eigenvalues of \(B\) and \(A\) at frequency \(k\) are
\[
b_k=\frac{1+2\cos(2\pi k_1/M)+2\cos(2\pi k_2/M)}5,
\qquad a_k=1-b_k,
\qquad g_u(k)=1-ub_k=1-u+ua_k.
\tag{2}
\]
Here \(-3/5\leq b_k\leq1\), and \(a_k>0\) except at the constant
mode. All inverses at \(u=1\), if used, are restricted to \(Q\).

For a real symmetric centered error \(D(u)=QD(u)Q\), define
\[
U_{u,t}=(I-uB)G_t,\qquad
\mathcal J_t[D]=W^2\int_0^t U_{u,t}D(u)BD(u)U_{u,t}\,du,
\qquad 0\leq t<1.
\tag{3}
\]
The preceding round proved a bound for translation-invariant errors
under the envelope
\[
-\frac{\delta u}{W^2}AG_u^2Q\preceq D(u)
\preceq\frac{\delta u}{W^2}AG_u^2Q.
\tag{4}
\]
The conclusions below concern the same envelope without translation
invariance. The order \(\preceq\) is the order on real symmetric matrices.

## Statements

Suppose \(E(u)=QE(u)Q\) is real symmetric, \(\|E(u)\|\leq1\), and
\[
D(u)=\frac{\delta u}{W^2}A^{1/2}G_uE(u)G_uA^{1/2}.
\tag{5}
\]
Then (4) holds. Conversely, for \(u>0\), \(\delta>0\), every centered
real symmetric \(D(u)\) satisfying (4) has this representation with a
unique contraction on \(Q\). This follows by conjugating (4) with the
inverse of \(A^{1/2}G_u\) on \(Q\).

First, if \(E\) has total variation \(V\) in operator norm on
\([0,t]\), meaning
\[
V=\sup_{0=s_0<\cdots<s_n=t}
       \sum_{j=1}^n\|E(s_j)-E(s_{j-1})\|,
\]
then
\[
-\frac{\delta^2t}{W^2}(1+2V)H_t
\preceq\mathcal J_t[D]
\preceq\frac{\delta^2t}{W^2}(1+2V)H_t.
\tag{6}
\]
Consequently,
\[
|\mathcal J_t[D]_{xy}|
\leq\frac{\delta^2t}{W^2}(1+2V)r_M(t),
\qquad r_M(t)=(H_t)_{00}.
\tag{7}
\]
The earlier return-kernel estimate is
\[
r_M(t)=\frac5{4\pi}\log\frac1{1-t+M^{-2}}+O(1)
\quad(1/2\leq t<1),
\qquad \sup_{t<1}r_M(t)\leq C(1+\log M).
\tag{8}
\]
Thus a bound on \(V\) independent of \(M\) retains a single logarithm.
In particular, (6) has the preceding round's constant for every
time-independent contraction \(E\), whether or not it commutes with \(B\).

Second, without a variation bound, every measurable contraction path
still satisfies
\[
|\mathcal J_t[D]_{xy}|
\leq\frac{C\delta^2}{W^2}(1+\log M)^2,
\qquad 0\leq t<1.
\tag{9}
\]
This order cannot be improved under (4) alone. For each integer
\(R\geq1\), set
\[
M=8^{R+2},\qquad t_M=1-M^{-4}.
\]
There is a continuous, piecewise continuously differentiable real
symmetric path (5), with \(D(0)=0\), for which
\[
\mathcal J_{t_M}[D]_{00}
\geq \frac{\delta^2}{W^2}
       \frac{\log8}{720000}R(R+1).
\tag{10}
\]
Its contraction path has variation \(V=2R\). Since
\(\log M=(R+2)\log8\), (10) has order
\(\delta^2(\log M)^2/W^2\). In particular, the single-logarithm
entry bound does not follow from the noncommuting pointwise envelope.
Moreover, for fixed \(\delta>0\), the same examples with
\(W=\lceil R^{3/4}\rceil\) have all error entries tending uniformly
to zero, while \(\mathcal J_{t_M}[D]_{00}\) tends to positive infinity.

## Exact conjugation of the quadratic term

Put \(C_t=A^{1/2}G_tQ\). All deterministic functions of \(B\)
commute with one another; no commutation with \(E(u)\) is used. From (5),
\[
U_{u,t}D(u)=\frac{\delta u}{W^2}C_tE(u)G_uA^{1/2},
\qquad
D(u)U_{u,t}=\frac{\delta u}{W^2}A^{1/2}G_uE(u)C_t.
\]
Therefore
\[
\mathcal J_t[D]
=\frac{\delta^2}{W^2}C_t
 \left[\int_0^t u^2E(u)ABG_u^2E(u)\,du\right]C_t.
\tag{11}
\]
Define the positive primitive on \(Q\)
\[
F_v=\int_0^v u^2A|B|G_u^2Q\,du.
\tag{12}
\]
Here \(|B|\) has eigenvalues \(|b_k|\). Its use is necessary:
\(B\) itself has negative eigenvalues. The eigenvalue of (12) at
a nonzero mode is
\[
f_v(k)=a_k|b_k|\int_0^v\frac{u^2}{g_u(k)^2}\,du
\leq a_kv^2\int_0^v\frac{du}{(1-ub_k)^2}
=\frac{a_kv^3}{g_v(k)}\leq v^2.
\tag{13}
\]
The integral identity follows by differentiating \(u/(1-ub_k)\);
it holds also when \(b_k=0\) or \(b_k<0\). The last inequality uses
\(g_v(k)\geq va_k\). Hence
\[
0\preceq F_v\preceq v^2Q.
\tag{14}
\]
Conjugating \(-A|B|G_u^2\preceq ABG_u^2\preceq A|B|G_u^2\)
by \(E(u)\) and integrating shows that the bracket in (11) lies
between \(-K_t\) and \(K_t\), where
\[
K_t=\int_0^t E(u)F'_uE(u)\,du\succeq0.
\tag{15}
\]

## Bounded variation estimate and an independent derivation

First suppose \(E\) is absolutely continuous. The product rule gives
\[
K_t=E(t)F_tE(t)
-\int_0^t \bigl[E'(u)F_uE(u)+E(u)F_uE'(u)\bigr]du,
\tag{16}
\]
since \(F_0=0\). By (14) and \(\|E(u)\|\leq1\),
\[
\|K_t\|\leq t^2+2\int_0^t u^2\|E'(u)\|du
\leq t^2(1+2V).
\tag{17}
\]

The same coefficient follows without a differential product rule.
For a step path with values \(E_j\) on successive intervals with
endpoints \(0=s_0<\cdots<s_n=t\), (15) is exactly
\[
K_t=E_nF_tE_n+
 \sum_{j=1}^{n-1}\bigl[E_jF_{s_j}E_j-E_{j+1}F_{s_j}E_{j+1}\bigr].
\tag{18}
\]
For any two contractions \(E,\widetilde E\),
\[
EF_vE-\widetilde EF_v\widetilde E
=(E-\widetilde E)F_vE+\widetilde EF_v(E-\widetilde E),
\]
whose norm is at most \(2t^2\|E-\widetilde E\|\).
Taking norms in (18) yields (17). This checks the endpoint coefficient
one and the variation coefficient two independently of (16).

A finite-variation matrix path has one-sided limits. Changing values
at its countably many discontinuities does not change (15). Take its
right-continuous representative and approximate it uniformly, except
possibly at the terminal point, by step paths sampled in time order.
For completeness, such finite partitions exist because failure of a
uniform oscillation bound \(\varepsilon\) on arbitrarily many successive
intervals would force variation at least \(n\varepsilon\) for every
\(n\). The sampled step paths remain contractions and their variations
are at most \(V\). For fixed finite \(M\), \(F'_u\) is continuous on
\([0,t]\). The bound
\[
\|E_nF'_uE_n-EF'_uE\|
\leq2\|E_n-E\|\,\|F'_u\|
\]
shows convergence of the integrals. Thus (17) holds for every
finite-variation path, including paths with jumps.

Equations (11), (15) and (17) give
\[
-\frac{\delta^2t^2}{W^2}(1+2V)C_t^2
\preceq\mathcal J_t[D]
\preceq\frac{\delta^2t^2}{W^2}(1+2V)C_t^2.
\]
For \(t>0\), mode by mode,
\[
C_t^2=AG_t^2Q\preceq t^{-1}H_t
\tag{19}
\]
because \(ta_k\leq g_t(k)\). This proves (6); \(t=0\) is immediate.
If \(-cH_t\preceq J\preceq cH_t\) and \(J=QJQ\), then
\(J=cH_t^{1/2}TH_t^{1/2}\) for a symmetric contraction \(T\) on
\(Q\). Cauchy–Schwarz gives
\[
|J_{xy}|\leq c\sqrt{(H_t)_{xx}(H_t)_{yy}}=c r_M(t).
\]
This proves (7), even though \(J\) need not be translation invariant.

## A general upper bound without temporal control

Let
\[
a_* =\min_{k\ne0}a_k=\frac45\sin^2(\pi/M)
\geq\frac{16}{5M^2}.
\tag{20}
\]
The equality follows by minimizing the two nonnegative sine-square
terms in \(a_k\); the inequality uses \(\sin(\pi/M)\geq2/M\).
For \(u\leq1/2\), \(g_u(k)\geq1/2\), so
\(\|F'_u\|\leq32u^2/5\). For \(u\geq1/2\), write \(s=1-u\).
Then \(g_u(k)\geq(s+a_k)/2\), and
\[
u^2\frac{a_k|b_k|}{g_u(k)^2}
\leq\frac{4a_k}{(s+a_k)^2}
\leq\frac4{s+a_*}.
\]
Consequently
\[
\int_0^1\|F'_u\|du
\leq\frac{16}{5}+4\log\left(1+\frac1{2a_*}\right)
\leq C(1+\log M).
\tag{21}
\]
The first constant is a harmless upper bound on the early-time
integral. Since \(E\) is a contraction, (15) and (21) imply
\(K_t\preceq C(1+\log M)Q\). For \(t\geq1/2\), use (19),
then the entry argument above and (8), to obtain (9).
For \(t\leq1/2\), use instead
\(K_t\preceq(32/15)t^3Q\) and
\(C_t^2\preceq(32/5)Q\), since \(a_k\leq8/5\) and
\(g_t(k)\geq1/2\). This gives an absolute entry bound
\(C\delta^2/W^2\) and completes the proof of (9).

## Explicit continuous family attaining two logarithms

Fix \(R\geq1\), \(M=8^{R+2}\), and, for \(1\leq r\leq R\), set
\[
n_r=8^r,\qquad s_r=n_r^2/M^2,
\qquad
\mathcal K_r=\{(k_1,k_2):1\leq k_1,k_2\leq n_r\}.
\tag{22}
\]
For \(k\in\mathcal K_r\), pair it with
\(j_r(k)=(k_1+3n_r,k_2)\). Thus
\(3n_r+1\leq j_1\leq4n_r\) and \(1\leq j_2\leq n_r\).
The two sets are disjoint and have equal size \(n_r^2\).

For all distinct frequencies used here, take real cosine eigenvectors
\[
e_k(x)=\frac{\sqrt2}{M}\cos(2\pi k\cdot x/M).
\tag{23}
\]
These vectors are centered and orthonormal. Indeed the exponential sum
over the torus vanishes at every nonzero frequency. Products of cosines
give the frequencies \(k-l\) and \(k+l\); in the present positive
quadrant, all coordinates are less than \(M/2\), so the latter cannot
be zero modulo \(M\), and the former vanishes only for \(k=l\).
The same calculation gives squared norm \(M^2/2\) before the
normalization in (23). Repeated frequencies across different scales
mean the same vector. They cause no difficulty below.

Let \(T_r\) interchange each pair \(e_k,e_{j_r(k)}\), and vanish
on their orthogonal complement. It is a real symmetric contraction
of norm one, supported on \(Q\). Define a scalar cutoff in the variable
\(v=1-u\): it vanishes outside \([s_r,2s_r]\), is one on
\([5s_r/4,7s_r/4]\), and is linear on the two intervening intervals.
Explicitly,
\[
\chi_r(u)=
\begin{cases}
4(v/s_r-1),&s_r\leq v\leq5s_r/4,\\
1,&5s_r/4\leq v\leq7s_r/4,\\
4(2-v/s_r),&7s_r/4\leq v\leq2s_r,\\
0,&\text{otherwise}.
\end{cases}
\tag{24}
\]
Since \(s_{r+1}=64s_r\), these supports are disjoint. Put
\[
E(u)=\sum_{r=1}^R\chi_r(u)T_r
\tag{25}
\]
and define \(D\) by (5). At most one summand is active, so
\(E\) is a continuous symmetric contraction path. Each excursion
from zero to \(T_r\) and back has variation two; the supports are
separated by zero intervals. Thus \(V=2R\). The path is zero near
\(u=0\), so \(D(0)=0\), and (4) holds at every time.

We give lower bounds with deliberately loose constants. For nonzero integer
frequencies with coordinate magnitudes at most \(M/2\), sine bounds
give
\[
\frac{16}{5}\frac{|k|^2}{M^2}
\leq a_k\leq\frac{4\pi^2}{5}\frac{|k|^2}{M^2}
<8\frac{|k|^2}{M^2}.
\tag{26}
\]
For a paired input \(j=j_r(k)\),
\(9n_r^2\leq|j|^2\leq17n_r^2\), so
\[
28s_r\leq a_j\leq136s_r.
\tag{27}
\]
As \(n_r\leq M/64\), \(s_r\leq1/4096\), and
\(a_j\leq136/4096<1/16\). Hence \(b_j>1/2\).
On the support of \(\chi_r\), \(u\geq1/2\), and
\[
g_u(j)=v+ua_j\leq2s_r+136s_r=138s_r.
\]
It follows that throughout the plateau,
\[
u^2\frac{a_jb_j}{g_u(j)^2}
\geq\frac{28}{8\cdot138^2s_r}
\geq\frac1{10000s_r}.
\tag{28}
\]
The final inequality is checked by
\(28\cdot10000>8\cdot138^2=152352\).
The plateau has length \(s_r/2\), so
\[
\int \chi_r(u)^2u^2\frac{a_jb_j}{g_u(j)^2}\,du
\geq\frac1{20000}.
\tag{29}
\]

Take \(t=t_M=1-\mu\), \(\mu=M^{-4}\). All cutoff supports lie
in \([0,t]\), because \(\mu<s_1=64/M^2\). Every nonzero frequency
has \(a_k\geq a_*\), and (20) implies
\(\mu/a_k\leq5/(16M^2)<1/2\). Therefore
\[
g_t(k)\leq a_k+\mu\leq3a_k/2,
\qquad \frac{a_k}{g_t(k)^2}\geq\frac4{9a_k}.
\tag{30}
\]

Extend the cosine vectors to a real orthonormal eigenbasis of \(B\).
For each active scale, \(T_rABG_u^2T_r\) is diagonal in that basis:
it interchanges the two corresponding diagonal coefficients on each
pair and annihilates all other vectors. All these coefficients are
nonnegative, since every involved frequency has \(b_k>0\), also for
the output frequencies by (26). Thus the bracket in (11), and then
\(\mathcal J_t\), are diagonal and positive semidefinite in this
fixed basis. Its origin diagonal is the sum of its mode coefficients
times \(e_k(0)^2=2/M^2\). There are no cross terms or cancellations.
Keeping only the output frequencies \(k\in\mathcal K_r\), equations
(29)–(30) give
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2}{W^2}
\sum_{r=1}^R\frac1{20000}\frac49\frac2{M^2}
                 \sum_{k\in\mathcal K_r}\frac1{a_k}.
\tag{31}
\]

For \(\mathcal K=\{1,\ldots,n\}^2\), group its points by
\(l=\max(k_1,k_2)\). There are \(2l-1\geq l\) points and
\(|k|^2\leq2l^2\). From (26),
\[
\sum_{k\in\mathcal K}\frac1{a_k}
\geq\frac{M^2}{8}\sum_{k\in\mathcal K}\frac1{|k|^2}
\geq\frac{M^2}{16}\sum_{l=1}^n\frac1l
\geq\frac{M^2}{16}\log(n+1).
\tag{32}
\]
The last inequality follows by integrating \(1/x\) over
\([1,n+1]\). Combining (31) and (32) yields
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2}{360000W^2}
                  \sum_{r=1}^R\log(n_r+1)
\geq\frac{\delta^2\log8}{720000W^2}R(R+1).
\]
This proves (10), including its normalization.

To verify the small-entry assertion, put \(S_u=AG_u^2Q\).
For \(u\leq1/2\), its diagonal is at most \(32/5\). For
\(u\geq1/2\), \(a_k/g_u(k)^2\leq4/a_k\), so
\[
(S_u)_{00}\leq4r_M(1)\leq C(1+\log M).
\]
The centered zero-mass quantity \(r_M(1)\) is finite and satisfies
the limiting form of (8). Conjugating (4) by \(S_u^{-1/2}\) on
\(Q\), and using Cauchy–Schwarz as for (7), gives
\[
\sup_{0\leq u<1}\max_{x,y}|D(u)_{xy}|
\leq\frac{C\delta}{W^2}(1+\log M).
\tag{33}
\]
For \(M=8^{R+2}\), \(W=\lceil R^{3/4}\rceil\), the right side
is \(O(\delta R^{-1/2})\), whereas (10) is bounded below by
\(c\delta^2R^{1/2}\) for all sufficiently large \(R\).
This proves the assertion, still under the stronger pointwise envelope.

## Checks and scope

The exact identity (11) has a second derivation. Set
\(Y_u=(I-uB)D(u)(I-uB)\). In general,
\[
U_{u,t}D(u)BD(u)U_{u,t}
=G_tY_uBG_u^2Y_uG_t.
\]
For (5), \(Y_u=\delta uW^{-2}A^{1/2}E(u)A^{1/2}\).
Substitution recovers (11) with factor \(\delta^2/W^2\)
after the external \(W^2\) in (3). On a single swapped pair,
direct multiplication of the two-by-two matrix
\(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\)
against a diagonal matrix gives
\(\operatorname{diag}(f_j,f_k)\). This independently checks the
direction of the transfer used in (29)–(31).

The shell lower bound in (32) can also be checked by rows: in the row
\(k_2=l\), retain \(1\leq k_1\leq l\). These \(l\) points each
have \(|k|^2\leq2l^2\), giving \(1/(2l)\). Summing these disjoint
rows reproduces the same harmonic lower bound without square shells.
The constants in (31)–(32) multiply as
\((1/20000)(4/9)(2/16)=1/360000\); the sum of the integers
\(1,\ldots,R\) supplies the further factor \(1/2\) in (10).

Several potential exceptional cases are excluded by explicit bounds.
Negative and zero \(b_k\) are included in (13) and (21); the
counterexample deliberately uses only positive \(b_k\). All errors
annihilate the constant vector. The counterexample uses positive mass
\(1-t=M^{-4}\), so no endpoint singularity is involved. It is
continuous in time. Its large loss agrees with (6), because its
variation grows as \(R\), while the return diagonal grows as \(R\).
The zero path covers \(\delta=0\); arbitrary \(W\geq1\) is allowed.

The matrices in (3) are the deterministic propagator and quadratic
term isolated from equations (2.33)–(2.39) of Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices:
Exponential Lower Bounds*,
[arXiv:2609.24426v4](https://arxiv.org/html/2609.24426v4).
Equation (8) is the deterministic return estimate established in
round 3 and independently rechecked in round 4.

No claim is made that (5), its uniform envelope, or a bounded variation
condition holds for the random two-loop error. A stochastic normalized
error may have infinite total variation. The counterexample is an
error family satisfying exactly the stated deterministic conditions;
it is not asserted to arise from a random resolvent or to preserve all
entrywise positivity constraints of the full two-loop observable.
It shows that a noncommuting extension cannot use the pointwise
Loewner envelope alone, even for continuous paths. The variation bound
gives one sufficient replacement. Neither statement supplies a new
delocalization threshold, localization length, or local-statistics
theorem for T076.
