PARTIAL

# The three-point determinantal entropy inequality in seven parameters

Write $H(Q)=-\sum_{S\subseteq\{1,2,3\}}p_S\log p_S$, with natural logarithms.
The full three-point concavity assertion is not proved here, and no counterexample
is obtained. The following statements are proved.

**Theorem 1 (seven-parameter scalar criterion).** Every connected strict
three-point kernel is represented, up to diagonal unitary conjugation,
permutation, and complex conjugation, by
\[
Q=\begin{pmatrix}a&x&y\\x&b&r e^{i\phi}\\y&r e^{-i\phi}&c\end{pmatrix},
\qquad (a,b,c,x,y,r,\phi)\in(0,1)^3\times[0,1/2]^3\times[0,\pi].
\tag{1}
\]
There are seven continuous parameters on the stratum with three nonzero edges.
The feasibility conditions and the matrices $M\in\mathbb R^{7\times7}$,
$b_*\in\mathbb R^7$ defined in Section 1 are explicit functions of these
parameters. On the connected strict domain, $M>0$, and inequality (21) of
C0033C is exactly
\[
\boxed{\quad b_*^{\mathsf T}M^{-1}b_*\ge2.\quad}
\tag{2}
\]
Its margin is $m(Q)=b_*^{\mathsf T}M^{-1}b_*-2=1-\theta(Q)$.
This reduction retains all nine ambient Hermitian directions.

**Theorem 2 (a family with a strict ambient Hessian sign).** Put
\[
Q_r=\begin{pmatrix}1/2&ir&-ir\\-ir&1/2&ir\\ir&-ir&1/2\end{pmatrix},
\qquad 0<r<1/(2\sqrt3).
\tag{3}
\]
The full nine-dimensional entropy Hessian at $Q_r$ is negative definite.
If
\[
k=\frac{1+4r^2}{1-12r^2},\qquad L=\log k,
\]
then the exact margin is given by (12) below. In particular,
\[
\theta(Q_r)=12r^2+O(r^4)\quad(r\downarrow0),\qquad
m(Q_r)=\frac4{L+4}+O(Le^{-L})\quad(L\to\infty).
\tag{4}
\]
The eigenvalues approach $0,1/2,1$ in the second limit. Consequently there is
no strictly positive uniform margin on the connected strict domain.

**Theorem 3 (two boundary expansions).** Let
$D=\operatorname{diag}(q_1,q_2,q_3)$, $0<q_i<1$, and let $W=W^*$
have zero diagonal and all three off-diagonal entries nonzero. Set
$v_i=q_i(1-q_i)$. Then
\[
\theta(D+tW)=t^2\sum_{i=1}^3
 \frac{|W_{ij}|^2|W_{ik}|^2}{v_i|W_{jk}|^2}+O(t^3),
\qquad \{i,j,k\}=\{1,2,3\}.
\tag{5}
\]
Let $K>0$ have all three off-diagonal entries nonzero, and put
\[
\lambda_i=\log\frac{K_{jj}K_{kk}}{K_{jj}K_{kk}-|K_{jk}|^2}>0,
\qquad d_0=\lambda_1\lambda_2\lambda_3.
\]
For $t\downarrow0$,
\[
\theta(tK)=t d_0\sum_i\frac{K_{ii}}{\lambda_i^2}+O(t^2),
\qquad \theta(I-tK)=\theta(tK).
\tag{6}
\]
The remainders are uniform on compact sets of the stated data that keep the
specified positive quantities away from zero. These expansions do not include
arbitrary simultaneous approaches to a disconnected graph and a spectral face.

**Theorem 4 (a sufficient inequality and a certified box).** Set
\[
V=\operatorname{tr}(Q-Q^2),\quad d=\det R_Q,\quad
S(Q)=(\operatorname{tr}R_Q)^2-2\operatorname{tr}(R_Q^2)-2dV.
\tag{7}
\]
At a connected strict kernel,
\[
m(Q)\ge\frac{S(Q)}{\operatorname{tr}(R_Q^2)+dV}.
\tag{8}
\]
In particular $S(Q)>0$ implies a negative definite full entropy Hessian.
The checkpointed interval cover in Section 5 proves $m(Q)>0.02478$ on the
entire seven-dimensional box
\[
\begin{gathered}
a,b,c\in[49/100,51/100],\qquad x,y\in[99/1000,101/1000],\\
\Re Q_{23}\in[-1/1000,1/1000],\qquad
\Im Q_{23}\in[99/1000,101/1000],\qquad Q_{12}=x, Q_{13}=y.
\end{gathered}
\tag{9}
\]
This is a local cover, not a cover of the full connected strict domain.

The two-point theorem, conditional lifting, and the product-kernel variation
formulas are credited to [C0033A](../C0033A/REPORT.md). The positive matrix
$R_Q$, full Hessian identity, and scalar criterion are credited to
[C0033B](../C0033B/REPORT.md). The characterization of singular $R_Q$ and the
ambient Hessian sign there are credited to [C0033C, Theorem A](../C0033C/REPORT.md).
Those results are used below without re-proving them. [dpp.py](dpp.py) and
[dpp.cpp](dpp.cpp) are verbatim copies from C0033C, also identical to the
corresponding C0033B and C0033A files. The new reductions, boundary statements,
and certificates are specified below.

## 1. Explicit seven-parameter inequality

Put $u=x^2, v=y^2, w=r^2, \rho=2xyr\cos\phi$, and
\[
\Delta=abc-aw-bv-cu+\rho,
\quad
\overline\Delta=(1-a)(1-b)(1-c)-(1-a)w-(1-b)v-(1-c)u-\rho.
\]
Strict feasibility is precisely positivity of $a,b,c,1-a,1-b,1-c$, of
\[
ab-u, ac-v, bc-w,\quad
(1-a)(1-b)-u, (1-a)(1-c)-v, (1-b)(1-c)-w,
\]
and of $\Delta,\overline\Delta$. These are all principal minors of $Q$
and $I-Q$. The graph is connected exactly when at least two of $x,y,r$
are positive. The eight probabilities, inherited from C0033A, are
\[
\begin{aligned}
p_{123}&=\Delta,&p_{12}&=ab-u-\Delta,&p_{13}&=ac-v-\Delta,&p_{23}&=bc-w-\Delta,\\
p_1&=a-ab-ac+u+v+\Delta,\\
p_2&=b-ab-bc+u+w+\Delta,\\
p_3&=c-ac-bc+v+w+\Delta,\\
p_0&=\overline\Delta.
\end{aligned}
\]
For $\{i,j,k\}=\{1,2,3\}$, define
\[
\ell_{ij}^0=\log\frac{p_i p_j}{p_0p_{ij}},\quad
\ell_{ij}^1=\log\frac{p_{ik}p_{jk}}{p_kp_{123}},\quad
\gamma=\log\frac{p_{123}p_1p_2p_3}{p_0p_{12}p_{13}p_{23}},
\quad R=\operatorname{diag}(\ell_{23}^0,\ell_{13}^0,\ell_{12}^0)-\gamma Q.
\]
The inherited results give $R>0$ exactly on the connected strict stratum.

Here is a formula for all matrices in (2), with no unspecified differentiation.
For $s\subseteq\{1,2,3\}$, put
\[
A_s=a-\mathbf1_{1\notin s},\quad B_s=b-\mathbf1_{2\notin s},\quad
C_s^{\rm diag}=c-\mathbf1_{3\notin s},\quad \sigma_s=(-1)^{3-|s|}.
\]
To avoid confusing a matrix with its third diagonal variable, write
$h_s=C_s^{\rm diag}$. The Hermitian gradient matrix $G_s$ is
\[
G_s=\sigma_s\begin{pmatrix}
B_sh_s-r^2&yr e^{-i\phi}-xh_s&xr e^{i\phi}-yB_s\\
yr e^{i\phi}-xh_s&A_sh_s-y^2&xy-A_s r e^{i\phi}\\
xr e^{-i\phi}-yB_s&xy-A_s r e^{-i\phi}&A_sB_s-x^2
\end{pmatrix}.
\]
Thus $Dp_s[T]=\operatorname{tr}(G_sT)$. Index the seven nonempty subsets
in the order $1,2,12,3,13,23,123$, and let $p$ now denote the column of
their probabilities. Set
\[
\begin{aligned}
\Sigma&=\operatorname{diag}(p)-pp^{\mathsf T},&d&=\det R,\\
(b_*)_s&=\operatorname{tr}(RG_s),&
K_{st}&=\operatorname{tr}(RG_sRG_t),\qquad M=K+d\Sigma.
\end{aligned}
\tag{10}
\]
The traces are real. Equations (1), (10), and (2) are the requested explicit
inequality in seven real parameters. An inverse-free version is
$b_*^{\mathsf T}\operatorname{adj}(M)b_*-2\det M\ge0$, since $M>0$.

**Proof of Theorem 1.** A diagonal unitary can make two edges of a triangle
positive real. Their remaining phase is the argument of
$Q_{12}Q_{23}Q_{31}$. Complex conjugation reverses that phase and preserves
every atom, allowing $0\le\phi\le\pi$. If an edge vanishes, phases can
instead be fixed on a spanning tree. A connected path has only five continuous
parameters: three diagonal entries and two moduli. The phase disappears on that
stratum. Permutations are a finite symmetry and do not reduce the generic
continuous count. The upper bound $1/2$ on each modulus follows from
$Q^2\le Q$. The principal-minor conditions above characterize strict
feasibility.

Choose a Frobenius-orthonormal real basis $E_\alpha$ of all Hermitian
matrices of order three, and set
\[
U_{s\alpha}=\operatorname{tr}(G_sR^{1/2}E_\alpha R^{1/2}),\qquad
\tau_\alpha=\operatorname{tr}E_\alpha.
\]
Normalization gives $G_0=-\sum_{s\ne0}G_s$. Therefore the Fisher matrix
in these congruent coordinates is $U^{\mathsf T}WU$, where
\[
W=\operatorname{diag}(p_s^{-1})+p_0^{-1}\mathbf1\mathbf1^{\mathsf T},
\qquad W^{-1}=\Sigma.
\]
The last identity follows by direct multiplication, using
$p_0+\sum_{s\ne0}p_s=1$. Moreover,
\[
UU^{\mathsf T}=K,\quad U\tau=b_*,\quad \tau^{\mathsf T}\tau=3.
\]
C0033C (22), which is equivalent to its (21), and Woodbury's identity now give
\[
\theta=\tau^{\mathsf T}(I+d^{-1}U^{\mathsf T}WU)^{-1}\tau
       =3-b_*^{\mathsf T}(d\Sigma+K)^{-1}b_*.
\]
For nonzero $z\in\mathbb R^7$, Cauchy–Schwarz gives
\[
z^{\mathsf T}\Sigma z
=\sum_s p_sz_s^2-(\sum_s p_sz_s)^2
\ge p_0\sum_s p_sz_s^2>0.
\]
Also $K=UU^{\mathsf T}\succeq0$ and $d>0$, proving $M>0$.
This establishes (2) without discarding any ambient direction. $\square$

The Hessian of $H(Q(a,b,c,x,y,r,\phi))$ in a nonlinear chart would contain
chart-curvature terms. It is not a substitute for the calculation above.

## 2. An exact family reaching a mixed spectral boundary

**Proof of Theorem 2.** The eigenvalues of (3) are
$1/2, 1/2\pm\sqrt3r$. Put $u=r^2$. The empty and full atoms have the
common value $A=(1-12u)/8$; the other six atoms have common value
$B=(1+4u)/8$. Consequently $\gamma=0$ and $R=LI$, with $L=\log(B/A)>0$.

The Fisher form and the trace metric are invariant under the cyclic coordinate
permutation. They also separate real symmetric and purely imaginary Hermitian
directions. Indeed $Q_r=I-\overline{Q_r}$; particle complementation and
conjugation permute the atoms and send a direction $T$ to
$-\overline T$. The Fisher form is invariant under this map. The linear
functional $T\mapsto\operatorname{tr}T$ is cyclically invariant and belongs
to the real symmetric part. Thus the inverse in the inherited scalar criterion,
applied to this trace functional, lies in the two-dimensional space
\[
T=\alpha I+\beta(J_3-I),\qquad \alpha,\beta\in\mathbb R,
\]
where $J_3$ is the all-ones matrix. This is a restriction of the inverse solve
to its invariant subspace, not a restriction of the directions being tested.

Write $c_0=3/4-3u$ and $\delta=c_0\alpha-6u\beta$.
The full atom derivative is $\delta$, the empty atom derivative is
$-\delta$, the three singleton derivatives are $\delta-\alpha$, and
the three pair derivatives are $\alpha-\delta$. Hence the Fisher form is
\[
F(T)=\frac{2\delta^2}{A}+\frac{6(\delta-\alpha)^2}{B}.
\]
In the coordinates $\alpha,\beta$, let its matrix entries be
$f_{11},f_{12},f_{22}$. Substituting
$u=(k-1)/(4(3k+1))$ gives
\[
\begin{aligned}
f_{11}&=\frac{3(3k^3+15k^2-3k+1)}{k(3k+1)},\\
f_{12}&=-\frac{9(k-1)^3}{k(3k+1)},\\
f_{22}&=\frac{9(k-1)^2(k+3)}{k(3k+1)}.
\end{aligned}
\tag{11}
\]
Since $\operatorname{tr}(T^2)=3\alpha^2+6\beta^2$, the matrix of the
positive form $J$ in the inherited original-coordinate criterion is
$F+\operatorname{diag}(3L,6L)$. The scalar criterion therefore becomes
\[
\theta=\frac{9L}{9L+s},\qquad
m=\frac{s}{9L+s},\qquad
s=\frac{D}{f_{22}+6L},
\tag{12}
\]
where direct expansion yields
\[
\begin{aligned}
D&=(f_{11}-6L)(f_{22}+6L)-f_{12}^2\\
 &=36\left\{-L^2+
 \frac{6k^2+6k-4}{k(3k+1)}L+3\frac{(k-1)^2}{k}\right\}.
\end{aligned}
\tag{13}
\]
Here $k>1$, $L>0$, and the coefficient of $L$ is positive. Furthermore
\[
\frac{(k-1)^2}{k}=2(\cosh L-1)\ge L^2.
\]
Thus $D>0$, whence $s>0$ and $\theta<1$. The inherited criterion now
proves negative definiteness of the full ambient Hessian.

As $r\downarrow0$, $L=16r^2+O(r^4)$, $f_{11}=12+O(r^2)$, and
$f_{12}=O(r^6)$. The scalar formula before elimination gives
$\theta=12r^2+O(r^4)$. As $k\to\infty$, (11)–(13) give
$s=36+O(L^2/k)$. Substitution in (12) proves (4).
The exact strict feasibility for every finite $k>1$, and the positive margins
tending to zero, prove the last assertion of the theorem. $\square$

The determinant identity (13) has an exact zero symbolic remainder in
[family.py](family.py). The generic seven-parameter chart for this family is
$(1/2,1/2,1/2,r,r,r,\pi/2)$, up to conjugation. In particular, the degenerating
margin is not confined to small off-diagonal moduli or to phase endpoints.

## 3. Boundary expansions and the remaining obstruction

**Proof of Theorem 3.** Use the inherited original-coordinate formula
\[
J=F+d\mathcal T_{R^{-1}},\quad
\mathcal T_{R^{-1}}(A,B)=\operatorname{tr}(R^{-1}AR^{-1}B),\quad
z(A)=\operatorname{tr}(R^{-1}A),\quad \theta=d z^{\mathsf T}J^{-1}z.
\]
Split coordinates into three diagonal and six off-diagonal directions.

For $Q=D+tW$, independence at $D$ and determinant expansion give
\[
p_s(Q)=p_s(D)-t^2\sum_{i<j}|W_{ij}|^2\partial_{q_iq_j}p_s(D)+O(t^3).
\]
At this order the logarithm of an atom contains only one-coordinate and
two-coordinate terms. Thus its Boolean triple coefficient satisfies
$\gamma=O(t^3)$. The conditional log odds give
\[
R_{ii}=t^2 h_i+O(t^3),\quad
h_i=\frac{|W_{jk}|^2}{v_jv_k}>0,\qquad
R_{ij}=O(t^4)\quad(i\ne j).
\]
Consequently
\[
d=t^6h_1h_2h_3+O(t^7),\quad
z_D=t^{-2}(h_i^{-1})_i+O(t^{-1}),\quad z_O=O(1).
\]
The diagonal Fisher block is
$F_{DD}=\operatorname{diag}(v_i^{-1})+O(t^2)$, while
$F_{OO}=O(t^2)$. Also $F_{DO}=O(t^2)$: the apparent order-$t$
term is the inner product of a centered one-coordinate Bernoulli score with a
centered two-coordinate score, which is zero by independence. The metric term
therefore gives
\[
J_{DD}=\operatorname{diag}(v_i^{-1})+O(t^2),\quad
J_{DO}=O(t^2),\quad J_{OO}=t^2B+O(t^3),\quad B>0.
\]
Positivity of $B$ follows already from the leading metric term; the Fisher
contribution is positive semidefinite. Block elimination in $J$ shows that the
leading term of $z^{\mathsf T}J^{-1}z$ is
$t^{-4}\sum_i v_i/h_i^2$, with error $O(t^{-3})$.
Multiplication by $d$ proves (5), since
$h_1h_2h_3v_i/h_i^2=|W_{ij}|^2|W_{ik}|^2/(v_i|W_{jk}|^2)$.

For $Q=tK$, inclusion-exclusion gives
$p_s=t^{|s|}\det K_{s,s}+O(t^{|s|+1})$ for nonempty $s$.
The conditional log odds consequently yield
$R=\operatorname{diag}(\lambda_i)+O(t)$, with off-diagonal entries $O(t)$.
Here $d=d_0+O(t)$, $z_D=(\lambda_i^{-1})_i+O(t)$, and $z_O=O(t)$.
The singleton atoms give
\[
J_{DD}=t^{-1}\operatorname{diag}(K_{ii}^{-1})+O(1),\qquad
J_{DO}=O(1),\qquad J_{OO}=B_0+O(t),\quad B_0>0.
\]
Again the metric term ensures $B_0>0$. Block elimination gives (6).
Particle complementation leaves the Fisher form unchanged, interchanges the
two conditional log odds, negates $\gamma$, and leaves $R$ unchanged.
It therefore leaves $\theta$ unchanged. The uniformity assertions follow
from the displayed expansions and uniform positive lower bounds for their
leading blocks on the stated compact sets. $\square$

These estimates prove positive margins sufficiently far along each fixed
approach in (5) or (6). Their constants deteriorate when edge moduli or positive
principal minors of the fixed data vanish. They do not provide uniform collars
around all intersections of boundary faces.

For clarity, the other boundary mechanisms can be described precisely.

**Proposition 3.1 (one simple spectral face).** Suppose $Q_0$ has eigenvalues
$\lambda_1,\lambda_2,0$, with $0<\lambda_i<1$, and all its atoms except
$p_{123}$ are positive. Put $Q_\varepsilon=Q_0+\varepsilon I$, and express
a direction $A$ in this eigenbasis. Then
\[
\begin{aligned}
-D^2H(Q_\varepsilon)[A,A]
={}&\frac{\lambda_1\lambda_2}{\varepsilon}A_{33}^2\\
&+2\log\varepsilon\{
\lambda_1(A_{22}A_{33}-|A_{23}|^2)
+\lambda_2(A_{11}A_{33}-|A_{13}|^2)\}
+O(\|A\|_F^2).
\end{aligned}
\tag{14}
\]
The remainder bound is uniform in $A$ for a fixed $Q_0$.

**Proof.** All other atom contributions to the negative entropy Hessian remain
bounded. The eigenbasis is used to expand the exceptional determinant; the other
atoms retain their original ground-set coordinates. In the exceptional atom,
\[
p_{123}=\lambda_1\lambda_2\varepsilon+O(\varepsilon^2),\quad
Dp_{123}[A]=\lambda_1\lambda_2 A_{33}+O(\varepsilon\|A\|_F),
\]
and direct determinant expansion gives
\[
D^2p_{123}[A,A]=2\{\lambda_1(A_{22}A_{33}-|A_{23}|^2)
+\lambda_2(A_{11}A_{33}-|A_{13}|^2)\}+O(\varepsilon\|A\|_F^2).
\]
Insert these in $(Dp)^2/p+(\log p)D^2p$. The remaining errors are bounded
quadratic forms because $\varepsilon|\log\varepsilon|\to0$. $\square$

When $A_{33}=0$, the logarithmically divergent term is nonnegative. If also
$A_{13}=A_{23}=0$, both displayed singular terms vanish. The finite Hessian
on this residual tangent space is not controlled by (14). Complementation gives
the same obstruction at a simple eigenvalue-one face. At simultaneous spectral
faces, more atoms can vanish; (3) handles one such family, not all of them.

At a strict connected path with one edge zero, $R>0$ by C0033C Theorem A, so
$\theta$ is analytic in the real and imaginary parts of the missing edge.
With that edge written $s e^{i\phi}$ in a real path gauge,
\[
m(s,\phi)=m(0)+s\cos\phi\,\partial_{\Re Q_{ij}}m(0)+O(s^2).
\]
The omitted imaginary linear term vanishes by conjugation symmetry. The sign of
$m(0)$ has not been proved for every connected path. At nonzero edges and
phase (0) or $\pi$, analyticity and conjugation give an even expansion in
the phase displacement. The constant term is the unresolved real-kernel
inequality. These regularity statements cannot replace a positivity estimate.

## 4. The sufficient inequality

**Proof of (8).** Let $N=|X|$. The elementary DPP covariance identities give
$E_QN=\operatorname{tr}Q$ and
$\operatorname{Var}_Q N=\operatorname{tr}(Q-Q^2)=V>0$.
For the score $L_s=Dp_s[A]/p_s$, normalization gives $E_QL=0$, and
\[
E_Q[(N-E_QN)L]=\operatorname{tr}A.
\]
Cauchy–Schwarz therefore bounds the Fisher form by
$F_Q(A)\ge(\operatorname{tr}A)^2/V$.
Use the congruent coordinates $A=R^{1/2}XR^{1/2}$ in C0033C (22).
If $w_\alpha=\operatorname{tr}(RE_\alpha)$, this bound reads
$\widetilde F\succeq ww^{\mathsf T}/(dV)$. The inverse reverses positive
definite matrix order, and the rank-one inverse formula yields
\[
\theta\le\tau^{\mathsf T}(I+ww^{\mathsf T}/(dV))^{-1}\tau
=3-\frac{(\operatorname{tr}R)^2}{dV+\operatorname{tr}(R^2)}.
\]
This is (8). The inherited scalar criterion gives the Hessian conclusion.
$\square$

The sufficient inequality is not necessary. On (3), it becomes
$S=L^2(3-2LV)$, where $V\to1/4$ as $L\to\infty$, so it eventually
fails although Theorem 2 proves $m>0$. Global covering must use more than this
single sufficient bound; [bnb.py](bnb.py) also implements the actual interval
Hessian test.

## 5. Certified computation and numerical evidence

All point certificates use exact rational coordinates and outward-rounded
`mpmath.iv` operations. Their atom derivatives are explicit integer polynomials.
Positive exact rational leading minors verify the kernel and its complement;
interval leading minors verify $R>0$. Interval $LDL^{\mathsf T}$ elimination
with strictly positive lower pivot bounds verifies positive definiteness of
the negative full nine-dimensional Hessian. A triangular interval solve also
evaluates both the original criterion and (2); their intervals overlap. These
checks are independent of the floating-point matrix square root used in search.
The polynomial/interval approach follows the earlier certificates in C0033B/C,
with attribution in [interval_core.py](interval_core.py).

### 5.1 The completed cover

For (9), Gershgorin gives $0.287I<Q<0.713I$, and the positive
12 and 13 edges ensure connectedness. The root is split at
$a=1/2$ and $b=1/2$,
giving four closed boxes with disjoint interiors. On every leaf, outward
interval evaluation verifies $S>0$ and (8). The complete tree has seven nodes,
four accepted leaves and no unresolved leaves. All endpoints are exact
rationals. The certificate uses 45 decimal interval digits; saved bounds are
rounded outward to rational multiples of $10^{-24}$. No positive error
tolerance is allowed in accepting a box.

| $a$ half | $b$ half | Lower bound for $S$ | Lower bound for $m$ |
| --- | --- | ---: | ---: |
| lower | lower | 0.002903877702323 | 0.02478194290787 |
| lower | upper | 0.002911076888100 | 0.02484450624885 |
| upper | lower | 0.002911076888100 | 0.02484450624885 |
| upper | upper | 0.002903877702323 | 0.02478194290787 |

Each displayed lower bound is rounded down. Thus $m>0.02478$ on the entire
box. Code: [bnb.py](bnb.py); complete leaf and endpoint data:
[data/bnb_small.json](data/bnb_small.json). This proves the box assertion of
Theorem 4. The two fixed imaginary entries in the gauge are not varied, but all
nine ambient Hessian directions are tested through (8).

The wider and truncated-domain runs are checkpointed, with every unclassified
box retained. The truncated target is exactly
\[
\mathcal D_{1/10}=\{Q\text{ in the gauge (1)}:
\tfrac1{10}I\le Q\le\tfrac9{10}I,\quad
|Q_{12}|,|Q_{13}|,|Q_{23}|\ge\tfrac1{10}\}.
\]
The rectangular root uses $a,b,c\in[.1,.9]$, $x,y\in[.1,.5]$,
$\Re Q_{23}\in[-.5,.5]$, $\Im Q_{23}\in[0,.5]$. A box is rejected only
when an outward upper bound for a necessary principal minor or modulus
constraint is negative. It is accepted only by (8) or an interval positive
definite full negative Hessian. Otherwise it is bisected at the exact rational
midpoint of its longest relative side. The saved leaves plus pending boxes
form a partition of the rectangular root, up to shared faces. None of these
unresolved cells is counted as certified.

<!-- BNB_TABLE_START -->

| Checkpoint | Nodes | Accepted | Discarded | Pending | Complete | Accepted root fraction | Pending root fraction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bnb_small | 7 | 4 | 0 | 0 | True | 1 | 0 |
| bnb_local_improved | 10000 | 4992 | 0 | 17 | False | 0.0014815331 | 0.99851847 |
| bnb_interior | 10000 | 426 | 4562 | 25 | False | 1.050271e-13 | 0.99982315 |
| bnb_interior_full | 20000 | 1408 | 8578 | 29 | False | 3.375078e-13 | 0.99982315 |

Files: [small cover](data/bnb_small.json), [wider box](data/bnb_local_improved.json), [truncated domain](data/bnb_interior.json), [truncated domain with full Hessian fallback](data/bnb_interior_full.json). The wider root is a,b,c in [0.45,0.55], x,y in [0.09,0.11], Re Q23 in [-0.02,0.02], Im Q23 in [0.09,0.11]. None of the fallback run’s accepted cells required the Hessian test; that fallback did not close the unresolved cells.

<!-- BNB_TABLE_END -->

The quoted coverage fractions refer to rectangular-root volume, not to the
unknown feasible volume. No compact remainder of the original problem has been
justified by uniform boundary estimates. In particular, even a complete cover
of $\mathcal D_{1/10}$ would not finish the three-point problem.

### 5.2 Random and local searches

[search.py](search.py), seed 33402, uses eleven random families: ordinary spectra;
spectra near endpoints; regularized rank-one and rank-two projections; all
eigenvalues near zero or near one; one small edge; two small edges; real phase
zero; real phase pi; and perturbations of real kernels. There are 132,000 random
attempts and 119,635 accepted evaluations. The phase-specific real families
discard the opposite phase, so their rejection counts are not numerical
failures. Spectral and graph tails also reject nonpositive computed atoms or
nonpositive computed $R$.

Three differential-evolution searches and 36 Nelder–Mead searches act on a
seven-entry gauge for a Hermitian logarithm followed by a spectral logistic map.
The spectral floors are $10^{-3},10^{-5},10^{-7}$. Differential evolution
uses one worker and population multiplier 12. There are 115,332 differential
evolution and 144,969 Nelder–Mead evaluations, for 392,301 total proposed
evaluations including random attempts. Fifteen local starts and one differential
evolution run meet their stopping criteria; the others reach their caps.
These are attained values, not certified extrema.

<!-- SEARCH_TABLE_START -->

| Family | Accepted | Largest binary theta | Certified margin at its rounded point |
| --- | --- | --- | --- |
| uniform | 12000 | 0.83258563316 | [0.167414366842, 0.167414366843] |
| spectral_extreme | 11983 | 0.95171502718 | [0.048268026268, 0.048268026269] |
| rank1 | 11972 | 0.94715845128 | [0.062844916356, 0.062844916357] |
| rank2 | 11977 | 0.94884489865 | [0.057575126051, 0.057575126052] |
| all_zero | 12000 | 0.60140213429 | [0.398574246058, 0.398574246059] |
| all_one | 12000 | 0.59443239934 | [0.405576852092, 0.405576852093] |
| small_edge | 12000 | 0.73738149736 | [0.262618502643, 0.262618502644] |
| disconnected_limit | 11552 | 0.95785120921 | [0.406648010137, 0.406648010138] |
| phase_zero | 6061 | 0.95175363788 | [0.048246349905, 0.048246349906] |
| phase_pi | 6092 | 0.95058889765 | [0.049411118823, 0.049411118824] |
| phase_endpoint | 11998 | 0.94666837324 | [0.053331313959, 0.053331313960] |

Data: [data/search.json](data/search.json), [data/certificates.json](data/certificates.json). The final column certifies one point per row, not every sample.

| Local start | Spectral floor | Evaluations | Converged | Binary theta | Certified margin |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.001 | 6000 | False | 0.92539710957 | [0.074602910851, 0.074602910852] |
| 1 | 1e-05 | 553 | True | 0.95785135476 | [0.406642228667, 0.406642228668] |
| 2 | 1e-07 | 6000 | False | 0.96908219125 | [0.031485212737, 0.031485212738] |
| 3 | 0.001 | 989 | True | 0.92540374371 | [0.074602907864, 0.074602907865] |
| 4 | 1e-05 | 6000 | False | 0.95582866917 | [0.044171368497, 0.044171368498] |
| 5 | 1e-07 | 6000 | False | 0.9689204614 | [0.031493972279, 0.031493972280] |
| 6 | 0.001 | 956 | True | 0.92546572579 | [0.075403318096, 0.075403318097] |
| 7 | 1e-05 | 6000 | False | 0.95581938913 | [0.044180677308, 0.044180677309] |
| 8 | 1e-07 | 856 | True | 0.968808642 | [0.031521715567, 0.031521715568] |
| 9 | 0.001 | 592 | True | 0.92539709214 | [0.074602907875, 0.074602907876] |
| 10 | 1e-05 | 6000 | False | 0.95580357439 | [0.044196471220, 0.044196471221] |
| 11 | 1e-07 | 6000 | False | 0.96168281279 | [0.038318429126, 0.038318429127] |
| 12 | 0.001 | 1091 | True | 0.9253970912 | [0.074602910364, 0.074602910365] |
| 13 | 1e-05 | 6000 | False | 0.95582799386 | [0.044172056137, 0.044172056138] |
| 14 | 1e-07 | 6000 | False | 0.96494443251 | [0.035107290091, 0.035107290092] |
| 15 | 0.001 | 3331 | True | 0.92508438151 | [0.074915626789, 0.074915626790] |
| 16 | 1e-05 | 6000 | False | 0.95582865306 | [0.044171423896, 0.044171423897] |
| 17 | 1e-07 | 6000 | False | 0.96829573015 | [0.031966383468, 0.031966383469] |
| 18 | 0.001 | 983 | True | 0.92539709209 | [0.074602907925, 0.074602907926] |
| 19 | 1e-05 | 987 | True | 0.95582868349 | [0.044171369510, 0.044171369511] |
| 20 | 1e-07 | 6000 | False | 0.96841746718 | [0.031933247138, 0.031933247139] |
| 21 | 0.001 | 1415 | True | 0.92539709201 | [0.074602908007, 0.074602908008] |
| 22 | 1e-05 | 6000 | False | 0.95582868883 | [0.044171361422, 0.044171361423] |
| 23 | 1e-07 | 6000 | False | 0.96823418882 | [0.031935910579, 0.031935910580] |
| 24 | 0.001 | 1109 | True | 0.92539708796 | [0.074602914090, 0.074602914091] |
| 25 | 1e-05 | 6000 | False | 0.95415659477 | [0.045843434369, 0.045843434370] |
| 26 | 1e-07 | 6000 | False | 0.96704778552 | [0.032997544682, 0.032997544683] |
| 27 | 0.001 | 1286 | True | 0.92539703979 | [0.074602960226, 0.074602960227] |
| 28 | 1e-05 | 6000 | False | 0.93020995921 | [0.069790040887, 0.069790040888] |
| 29 | 1e-07 | 6000 | False | 0.95568941245 | [0.044310600048, 0.044310600049] |
| 30 | 0.001 | 1563 | True | 0.92537230752 | [0.074628952474, 0.074628952475] |
| 31 | 1e-05 | 6000 | False | 0.95568437083 | [0.044315663047, 0.044315663048] |
| 32 | 1e-07 | 1776 | True | 0.94844830931 | [0.051551694217, 0.051551694218] |
| 33 | 0.001 | 1482 | True | 0.92539691891 | [0.074603081099, 0.074603081100] |
| 34 | 1e-05 | 6000 | False | 0.88402341412 | [0.116224370239, 0.116224370240] |
| 35 | 1e-07 | 6000 | False | 0.95534214433 | [0.044657916601, 0.044657916602] |

| Differential evolution floor | Evaluations | Converged | Binary theta | Certified margin |
| --- | --- | --- | --- | --- |
| 0.001 | 14364 | True | 0.92539706258 | [0.074602937413, 0.074602937414] |
| 1e-05 | 50484 | False | 0.95582771692 | [0.044172384240, 0.044172384241] |
| 1e-07 | 50484 | False | 0.96802373395 | [0.032150200074, 0.032150200075] |

<!-- SEARCH_TABLE_END -->

The smallest binary search margin is (0.0309178087450), but its solve has
condition number about $7.1\cdot10^{13}$. At its saved rational rounding the
certified margin is
\[
0.0314852127372884<m<0.0314852127372885.
\tag{15}
\]
Its seven parameters are approximately
\[
(0.9999844481514108, 0.5002075630074504, 0.4997924369923335,
7.2281720826254\cdot10^{-7}, 7.2310008933895\cdot10^{-7},
0.4999998552633628, 3.141591898731511).
\]
The approximate spectrum is
$(1.01653\cdot10^{-7},0.999984448152456,0.999999898345668)$.
The exact object in (15) is specified by the nine numerators in
[data/certificates.json](data/certificates.json), record `best`, with common
denominator $10^{24}$. All 51 rational roundings of family, local, and global
search extrema have certified positive margins and positive definite negative
Hessians. Their rounded kernels need not coincide with the exact binary inputs.

### 5.3 Boundary probes

An additional exact rational family concentrates on phase pi, a nearly
disconnected graph, and both spectral endpoints:
\[
Q(t)=\begin{pmatrix}1-t&t^2&t^2\\t^2&1/2&-1/2+t^2\\t^2&-1/2+t^2&1/2\end{pmatrix},
\qquad t=10^{-j}.
\tag{16}
\]
The antisymmetric mode has eigenvalue $1-t^2$, and the other two modes are the
eigenvalues of
$\begin{psmallmatrix}1-t&\sqrt2t^2\\\sqrt2t^2&t^2\end{psmallmatrix}$.
For $0<t\le1/10$, the two determinant conditions
$(1-t)t^2>2t^4$ and $t(1-t^2)>2t^4$ prove $0<Q(t)<I$.
Complementation and a diagonal sign conjugation give phase-zero kernels with
the same margins. At the eight stated rational points, 220-decimal interval
arithmetic certifies the full Hessian as well as (2).

For (3), exact rational $k=10^j$ fixes
$r^2=(k-1)/(4(3k+1))$. Strict feasibility is an exact algebraic consequence
of $0<r^2<1/12$; the narrow spectral gap need not be resolved by subtracting
two nearly equal floating-point eigenvalues. Interval evaluation of the proved
formula (12) certifies its margins.

<!-- BOUNDARY_TABLE_START -->

| Family (16), j | Certified margin |
| --- | --- |
| 1 | [0.115199537471, 0.115199537472] |
| 2 | [0.055460684802, 0.055460684803] |
| 3 | [0.036704423962, 0.036704423963] |
| 4 | [0.027431029451, 0.027431029452] |
| 6 | [0.018222986269, 0.018222986270] |
| 8 | [0.013643229539, 0.013643229540] |
| 10 | [0.010903091113, 0.010903091114] |
| 12 | [0.009079535725, 0.009079535726] |

| Cyclic k | Certified margin |
| --- | --- |
| 10^1 | [0.483000930298, 0.483000930299] |
| 10^2 | [0.426498892476, 0.426498892477] |
| 10^4 | [0.301881177869, 0.301881177870] |
| 10^8 | [0.178406509318, 0.178406509319] |
| 10^16 | [0.097939927913, 0.097939927914] |
| 10^32 | [0.051491500899, 0.051491500900] |
| 10^100 | [0.017075153478, 0.017075153479] |
| 10^1000 | [0.001734165373, 0.001734165374] |

Code: [boundary.py](boundary.py); data: [data/boundary.json](data/boundary.json). Cyclic entries use the proved closed formula; entries for (16) certify the full Hessian directly.

<!-- BOUNDARY_TABLE_END -->

The smallest explicitly evaluated certified margin in this report is the
$k=10^{1000}$ cyclic value, between
(0.0017341653738028063) and (0.0017341653738028064). Its location in the
seven parameters is exactly
$(1/2,1/2,1/2,r,r,r,\pi/2)$ with the rational $r^2$ just stated.
The asymptotic in Theorem 2 gives arbitrarily smaller positive margins.
There is therefore no positive minimum asserted by this finite list of probes.

### 5.4 Independent checks and resources

<!-- AUDIT_TABLE_START -->

| Check | Cases | Largest absolute binary discrepancy |
| --- | --- | --- |
| atoms | 2000 | 2.2204e-16 |
| gradients | 2000 | 5.5511e-16 |
| theta_8 | 2000 | 5.1359e-13 |
| theta_7 | 2000 | 1.3366e-11 |
| gauge | 2000 | 1.0325e-14 |
| complement | 2000 | 2.4841e-15 |
| curvature_cpp | 2000 | 2.8422e-14 |

| Additional check | Result |
| --- | --- |
| Cyclic determinant (13), symbolic remainder | 0 |
| Cyclic closed formula vs full criterion, 5 points | 6.657e-17 |
| Diagonal expansion (5): theta/t^2 at t=0.0003 | 7.26447390408 |
| Diagonal expansion predicted coefficient | 7.26447551052 |
| Zero expansion (6): theta/t at t=0.0003 | 0.0795065522386 |
| Zero expansion predicted coefficient | 0.0794890363508 |

Code: [audit.py](audit.py), [family.py](family.py); data: [data/audit.json](data/audit.json), [data/family.json](data/family.json). Full asymptotic tables, not just the last entries, are saved in the audit data.

<!-- AUDIT_TABLE_END -->

The seven-atom floating formula is less well conditioned than the nine-direction
congruent search formula near a nearly disconnected graph. Its larger binary
comparison error is why point certificates use high-precision intervals and
why binary near-zero margins would not be treated as violations.

<!-- RESOURCE_TABLE_START -->

| Run | Seconds | Peak RSS, MiB |
| --- | --- | --- |
| Random/local search | 38.98 | 77.219 |
| 51 point certificates | 3.495 | 70.469 |
| Boundary certificates | 0.4121 | 54.641 |
| Independent numerical audit | 1.334 | 37.25 |
| bnb_small | 0.007509 | 57.312 |
| bnb_local_improved | 10.41 | 83.75 |
| bnb_interior | 7.267 | 69.156 |
| bnb_interior_full | 121.6 | 84.797 |
| Exact partition and leaf audit | 18.03 | 87.906 |

<!-- RESOURCE_TABLE_END -->

All computations use one numerical process at a time, one numerical thread,
no worker pool, and inherited nice priority 20. Peak resident memory is far
below 4 GB. Checkpoints are written atomically every 1,000 processed cells and
at termination. Unfinished runs can be resumed, for example:

```sh
python3 bnb.py --resume --file data/bnb_interior_full.json --max-nodes 20000
```

For a sequential reproduction, run `python3 reproduce.py`; add `--search` to
regenerate the floating searches and finite incomplete covering runs first.
The default reruns the exact identities, interval point certificates, boundary
certificates, completed local cover, and independent audits. It also verifies
the saved cover partitions using exact rational volumes. Package versions,
resource measurements and SHA-256 hashes are in
[artifact_manifest.json](artifact_manifest.json). The inherited shared library
is rebuilt from [dpp.cpp](dpp.cpp).

## 6. What remains open

Inequality (2), equivalently C0033C (21), remains unproved for arbitrary connected
strict kernels, including arbitrary real triangles and connected paths. The
simple spectral expansion leaves an uncontrolled finite tangent form; the
generic simultaneous spectral and graph degenerations have no uniform boundary
estimate here. The proved expansions therefore do not remove all boundary
collars and do not leave a single justified compact interior remainder.

The completed cover proves only (9). The wider and truncated-domain covers
retain unresolved cells. No complete certified cover of the required domain,
and no violating entropy segment, is provided. Thus the full three-point
concavity theorem is not claimed. If the connected inequality is established,
C0033C Theorem A supplies the remaining strict kernels, and the continuity
argument in C0033A–C supplies boundary endpoints. That missing connected
inequality is exactly the outstanding step.

Task: “Open problem C0033, fourth attempt: inequality (21) on connected strict
three-point kernels” — 14 November 2026, 01:59, Asia/Tbilisi (session start).
