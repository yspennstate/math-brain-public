PARTIAL

# A general mixed collar for three-point determinantal entropy

All logarithms are natural. The margin is the ambient scalar margin
\(m=1-\theta\) of C0033C (21), equivalently C0033D (2), and
\(\Lambda=-\log\min_Sp_S\). Full three-point concavity remains open.
No negative margin was found.

The result below removes the equal-connection, real-phase, balanced-block,
and restricted-block-spectrum assumptions of C0033E Theorem 2. Its collar
is quantitatively thin; it does not cover all simultaneous rates of approach
to spectral and graph boundaries. The coefficient in the new bound is not
claimed optimal.

## 1. Statements

After a diagonal unitary conjugation on coordinates 2 and 3, write
\[
 C=\begin{pmatrix}b&-r\\-r&c\end{pmatrix},\qquad
 0<C<I,quad r>0.
\]
The choice of the negative sign is immaterial. Define
\[
 \begin{aligned}
 w&=(1-b)(1-c)-r^2,&p&=b(1-c)+r^2,\\
 q&=(1-b)c+r^2,&z&=bc-r^2,\\
 \pi_*&=\min(w,p,q,z),&K&=\log\frac{pq}{wz}>0.
 \end{aligned}                                                    \tag{1}
\]
Let \(v\in\mathbb C^2\), \(\|v\|=1\), and consider
\[
 Q_x=\begin{pmatrix}a&\sqrt{x}\,v^*\\ \sqrt{x}\,v&C\end{pmatrix},
 \qquad 0<a<1.                                                     \tag{2}
\]
Thus \(x=|e_{12}|^2+|e_{13}|^2\). Either connection may vanish. This
normalization of \(x\) differs by a factor of two from C0033E's equal-edge
normalization.

For \(T\subseteq\{2,3\}\), put
\[
 M_T=C-D_{\{2,3\}\setminus T},\quad
 \pi_T=P_C(T),\quad k_T=v^*M_T^{-1}v.
\]
Use the real coordinate basis
\(E_{22},E_{33},E_{23}+E_{32},i(E_{23}-E_{32})\) on Hermitian matrices
of order two. Let \(F_C\) be the Fisher matrix of the four atoms in this
basis, and let \(N_C=-D^2H(C)\) be the two-point negative Hessian in the
same basis. Define the Hermitian matrix and its coordinate covector
\[
 W=\sum_T\pi_T k_T M_T^{-1},\qquad
 \eta_j=\operatorname{tr}(WE_j).                                    \tag{3}
\]
All matrices and covectors in the statements are explicit finite sums or
four by four matrices. In particular, no limiting optimization defines a
constant.

**Theorem 1 (general leading term).** For every choice in (1)–(2),
\(W>0\), and the analytic extension of \(m(Q_x)\) to \(x=0\) is
\[
 \boxed{\displaystyle
 m_0(C,v)=\left(1+\frac{K}{\det W}\,
                  \eta^{\mathsf T}N_C^{-1}\eta\right)^{-1}.}        \tag{4}
\]
It is independent of \(a\), and satisfies the uniform bound
\[
 \boxed{\displaystyle m_0(C,v)\ge\frac1{2K+3}.}                    \tag{5}
\]
There is no assumption on the two eigenvalues of \(C\), apart from
strictness. In particular, one or both may approach an endpoint, with
arbitrary imbalance. All complex phases and connection ratios are allowed.

For an explicit error bound set
\[
 \begin{gathered}
 \alpha=a(1-a),\qquad \nu=\alpha\pi_*,\qquad
 \omega=\frac{\pi_*}{2}(1-e^{-K}),\\
 \mu=\min\left\{\frac1{100},\nu,K,\frac\omega\alpha,\frac{r^2}{4}\right\}>0.
                                                                    \tag{6}
 \end{gathered}
\]
These parameters do not depend on \(v\).

**Theorem 2 (uniform remainder and scaled collar).** For all the data above,
\[
 0<x\le\frac{\mu^9}{2\cdot10^{18}}quad\Longrightarrow\quad
 |m(Q_x)-m_0(C,v)|\le10^{30}\frac{x}{\mu^{15}}.                      \tag{7}
\]
Every such \(Q_x\) is a connected strict contraction. On the subcollar
\[
 0<x\le\frac{\mu^{15}}{2\cdot10^{30}(2K+3)},                         \tag{8}
\]
its full nine-dimensional entropy Hessian is negative definite, and
\[
 \boxed{\displaystyle
 m(Q_x)\ge\frac1{4K+6}\ge\frac1{8\Lambda(Q_x)+6}.}                 \tag{9}
\]
The constants in (7)–(9) are independent of \(a,C,v,x\). The dependence
on degenerating block data is displayed in \(\mu\); there is no hidden
compactness constant. The three choices of isolated coordinate give three
such collars.

If \(\Lambda_0=-\log[\min(a,1-a)\pi_*]\), then (5) also gives
\(m_0\ge1/(4\Lambda_0+3)\). For a feasible \(Q_x\), one may use
\(m_0\ge1/(4\Lambda(Q_x)+3)\). Thus the requested atom-logarithmic
scale holds throughout the general leading-term family, and throughout
the explicit subcollar for the actual margin.

**Proposition 3 (a compact scaled certificate).** On exactly the small box
C0033D (9),
\[
 m(Q)(\Lambda(Q)+6)>\frac18.                                      \tag{10}
\]
This is a scaled consequence of C0033D's existing local cover. It is not
a cover of the remainder of the connected strict domain.

C0033E Corollary 3 already proves that a global inequality
\(m\ge c/(\Lambda+C_0)\), with fixed finite \(C_0\), requires
\(c\le1/2\). That obstruction is used with attribution. The computations
below support \(1/2\) as a candidate, but neither a global bound with
that coefficient nor the unshifted inequality \(\Lambda m\ge1/2\) is
proved here.

## 2. Inherited results and notation

The two-point concavity theorem, block-product Hessian, and conditioning
identities are taken from C0033A. The positive matrix \(R_Q\), ambient
Hessian identity, and scalar criterion are taken from C0033B. The
classification of singular \(R_Q\) and ambient nonpositivity at strict
disconnected kernels are taken from C0033C. The seven-atom formulation,
cyclic family, and local interval cover are taken from C0033D. The exact
restricted mixed formula and its coefficient obstruction are taken from
C0033E. These results are not counted as new theorems.

In a real basis of all Hermitian directions, the inherited identity is
\[
 \begin{aligned}
 F_{ij}&=\sum_S\frac{Dp_S[E_i]Dp_S[E_j]}{p_S},\\
 d&=\det R,\qquad z_i=\operatorname{tr}(R^{-1}E_i),\\
 J_{ij}&=F_{ij}+d\operatorname{tr}(R^{-1}E_iR^{-1}E_j),\\
 -D^2H&=J-dzz^{\mathsf T},\qquad
 m=1-dz^{\mathsf T}J^{-1}z,\qquad J>0.                            \tag{11}
 \end{aligned}
\]
Here
\[
 R=\operatorname{diag}(\ell_{23}^0,\ell_{13}^0,\ell_{12}^0)-\gamma Q,
 \quad \ell_{ij}^0=\log\frac{p_ip_j}{p_0p_{ij}},\quad
 \gamma=\log\frac{p_{123}p_1p_2p_3}{p_0p_{12}p_{13}p_{23}}.
\]
This criterion is invariant under an invertible linear change of the
ambient direction basis. No Hessian in a nonlinear kernel chart is used.

The copied files and SHA-256 attribution are recorded in
[data/inherited_manifest.json](data/inherited_manifest.json). In particular,
[mp_core.py](mp_core.py) and [mixed_limit.py](mixed_limit.py) are copied from
C0033E, and [interval_core.py](interval_core.py), [bnb.py](bnb.py), and the
other inherited core files are copied from C0033D.

## 3. A quantitative two-point Fisher lemma

Write \(C_{23}=s\ne0\) real for this section; either sign is permitted.
On the three real symmetric coordinates \((b,c,s)\), set
\[
 D=\begin{pmatrix}0&1&0\\1&0&0\\0&0&-2\end{pmatrix},\qquad
 F=F_C|_{\mathrm{real}},\qquad N=N_C|_{\mathrm{real}}=F-KD.
\]
The imaginary coordinate decouples, has zero Fisher term, and has
negative-Hessian coefficient \(2K\). Put
\[
 A=wz,\quad B=pq,\quad \delta=B-A=s^2,\quad P=w p q z,
 \quad B_0=A+\delta(p+q).
\]
C0033A (8) supplies the exact identity
\[
 \det(F-uD)=\frac2P\{2\delta+B_0u-Pu^3\}.                          \tag{12}
\]
The map from the three real coordinates to the four atoms has rank three,
so \(F>0\).

**Lemma 3.1.** Let the eigenvalues of
\(L=F^{-1/2}DF^{-1/2}\) be \(\lambda,-s_1,-s_2\), with
\(0<s_1\le s_2\). Then
\[
 \lambda=\frac{s_1s_2}{s_1+s_2},\quad
 s_1+s_2-\lambda=\frac{B_0}{2\delta},\quad
 \lambda s_1s_2=\frac P{2\delta},\quad
 K\lambda\le\frac12,\quad 2Ks_2\le K+1.                           \tag{13}
\]
Consequently \(N\succeq F/2\). For every real positive semidefinite
matrix \(A_0\) of order two, let \(W_0\) be the Fisher operator applied
to \(A_0\), defined by
\(\operatorname{tr}(W_0B_0')=F_C(A_0,B_0')\) for every real symmetric
\(B_0'\). Then
\[
 \det W_0\ge\frac{F_C(A_0,A_0)}{2s_2}.                             \tag{14}
\]

**Proof.** Sylvester's law gives the stated inertia of \(L\). The zero
quadratic coefficient, the linear coefficient, and the cubic coefficient
in (12), after division by \(\det F=4\delta/P\), give the first three
identities in (13). Since \(B/A=e^K\),
\[
 \lambda^2\le\frac P{B_0}
 \le\frac{B}{(e^K-1)(p+q)}
 \le\frac1{4(e^K-1)}.
\]
For \(u\ge0\), \(e^u-2u>0\), as follows already from
\(e^u\ge1+u+u^2/2\). Integration gives \(e^K-1\ge K^2\).
Thus \(K\lambda\le1/2\), proving \(N\succeq F/2\).
Furthermore \(\lambda\le s_1\), so
\[
 s_2\le s_1+s_2-\lambda
 =\frac1{2(e^K-1)}+\frac{p+q}{2},
 \qquad
 2Ks_2\le\frac K{e^K-1}+K(p+q)\le1+K.
\]

For (14), let \(a_0\) be the coordinate vector of \(A_0\),
\(y=F^{1/2}a_0\), and \(f=Fa_0\). The coordinate covector of
\(W_0\) is \(f\); its off-diagonal component is twice the corresponding
matrix entry. Therefore
\[
 2\det W_0=f^{\mathsf T}D^{-1}f=y^{\mathsf T}L^{-1}y,
 \qquad y^{\mathsf T}Ly=2\det A_0\ge0.
\]
In an eigenbasis of \(L\), the matrix
\[
 L^{-1}-s_2^{-1}I-\frac1{s_1\lambda}L
\]
has diagonal entries \(0,0,-2/s_2+s_2/(s_1\lambda)\). The last is
nonnegative because \(s_2(s_1+s_2)\ge2s_1^2\). It follows that
\(y^{\mathsf T}L^{-1}y\ge\|y\|^2/s_2\), proving (14). \(\square\)

**Lemma 3.2.** The matrix \(W\) in (3) satisfies
\[
 W=\sum_T\pi_T M_T^{-1}vv^*M_T^{-1}>0,
 \qquad \lambda_{\min}(W)\ge\omega.                               \tag{15}
\]
Also, in the unnormalized four-coordinate basis used above,
\[
 \lambda_{\min}(N_C)\ge\min\{r^2/4,2K\}.                           \tag{16}
\]

**Proof.** Differentiating the identity
\(\sum_T\pi_TM_T^{-1}=0\) in direction \(vv^*\) gives the equality
in (15). The matrix \(W\) is real when \(C\) is real: its first
expression depends on \(v\) only through \(\operatorname{Re}(vv^*)\).
Let \(A_0=\operatorname{Re}(vv^*)\). It is positive semidefinite with
trace one. The cardinality score identity and Cauchy–Schwarz give
\[
 F_C(A_0,A_0)\ge
 \frac{(\operatorname{tr}A_0)^2}{\operatorname{tr}(C-C^2)}\ge2.
\]
Lemma 3.1 now implies \(\det W\ge1/s_2>0\). The first expression in
(15) is positive semidefinite, so \(W>0\). Since
\(-I<M_T<I\), \(\|\operatorname{adj}M_T\|\le1\), and
\(|\det M_T|=\pi_T\). Consequently
\[
 \|W\|\le\sum_T\frac1{\pi_T}\le\frac4{\pi_*},\qquad
 \det W\ge\frac1{s_2}\ge2(1-e^{-K}).
\]
Division proves the lower bound \(\lambda_{\min}(W)\ge\omega\).

For (16), write an atom differential as
\((dw,dp,dq,dz)\). Its real coordinate differential obeys
\[
 db=dp+dz,\quad dc=dq+dz,\quad
 ds=\frac{c\,dp+b\,dq+(b+c-1)dz}{2s}.
\]
Since \(|s|\le1/2\),
\[
 db^2+dc^2+ds^2\le\frac7{4s^2}(dw^2+dp^2+dq^2+dz^2).
\]
Every atom is at most one, so \(F\succeq(4s^2/7)I\).
Lemma 3.1 gives \(N\succeq(2s^2/7)I\succeq(s^2/4)I\).
Adding the decoupled imaginary coefficient \(2K\) proves (16).
\(\square\)

## 4. Proof of the general collar formula

The conditional atom identity gives, exactly in \(x\),
\[
 p_{\{1\}\cup T}(x)=\pi_T(a-xk_T),\qquad
 p_T(x)=\pi_T(1-a+xk_T).                                          \tag{17}
\]
Both one-block marginals are fixed. Put
\[
 S=\operatorname{diag}(1,\sqrt{x},\sqrt{x}),\qquad
 R=S\overline R S.
\]
Every entry of \(\overline R\) has an analytic extension at zero.
Indeed \(\gamma(0)=0\), the two isolated-to-block log odds vanish at
zero, and every atom in (17) is affine in \(x\). In the original block
coordinates,
\[
 \boxed{\displaystyle
 \overline R(0)=\operatorname{diag}\left(K,\frac{\operatorname{adj}W}{\alpha}\right).} \tag{18}
\]
Here \(\operatorname{diag}(K,T)\) denotes a one by one block and a two
by two block.

For a direct verification of (18), use a real block entry \(s=C_{23}\)
and order the patterns as \(00,10,01,11\). Put
\(A_k=k_{00}-k_{10}-k_{01}+k_{11}\). Differentiating the triple log
odds gives \(\gamma'(0)=-A_k/\alpha\). The two isolated-pair log-odds
derivatives, multiplied by \(\alpha\), are
\[
 L_2=k_{10}-k_{00},\qquad L_3=k_{01}-k_{00}.
\]
These identities also follow by a rank-one inverse update; for example
\[
 L_2=\frac{|(1-c)v_2+s v_3|^2}{wp}.
\]
The limiting lower block of \(\overline R\), multiplied by \(\alpha\),
is \(\operatorname{diag}(L_3,L_2)+A_kC\). On the other hand, (3) and
\(\pi_TM_T^{-1}=(-1)^{2-|T|}\operatorname{adj}M_T\) give
\[
 W_{22}=L_2+cA_k,\quad W_{33}=L_3+bA_k,\quad W_{23}=-sA_k.
\]
Taking the adjugate proves (18), including complex \(v\).

Use the following basis of all nine ambient directions: the isolated
coordinate, the four block directions, and the four connection directions
divided by \(\sqrt{x}\). For a direction \(E_i\) in this basis, set
\[
 Y_i=xS^{-1}E_iS^{-1}.
\]
Thus \(Y_i=xE_{11}\) for the isolated coordinate; the four block
\(Y_i\)'s are the usual block basis; and the four connection \(Y_i\)'s
are the unscaled connection basis. If \(B=\overline R^{-1}\),
\(\bar d=\det\overline R\), and
\(\bar z_i=\operatorname{tr}(BY_i)\), (11) becomes
\[
 J_{ij}(x)=F_{ij}(x)+\bar d\operatorname{tr}(BY_iBY_j),\qquad
 m(x)=1-\bar d\bar z^{\mathsf T}J(x)^{-1}\bar z.                   \tag{19}
\]
The scaled atom gradients, and hence \(F\), are analytic in \(x\).

At zero, the isolated score, the block marginal scores, and the connection
scores are pairwise orthogonal in the Fisher form. The first two statements
use independence. The connection score is centered conditionally on the
block pattern; its cross product with the isolated score vanishes because
\(\sum_T\pi_TM_T^{-1}=0\). The metric term in (19) has the same block
decomposition. The limiting source has only block components.

Set \(T=\operatorname{adj}W/\alpha\),
\(\zeta(A)=\operatorname{tr}(T^{-1}A)\). The block part of (19) is
\[
 J_B(A,B)=F_C(A,B)+K\det T\operatorname{tr}(T^{-1}AT^{-1}B).
\]
The two by two determinant identity gives
\[
 J_B=N_C+K\det T\,\zeta\zeta^{\mathsf T}.
\]
The isolated block is \(1/\alpha\). The connection metric alone is
\(2w^*\operatorname{adj}(T)w=2w^*Ww/\alpha\), so that block is
positive definite. Thus \(J(0)>0\). A rank-one inverse formula in the
block part gives
\[
 m_0=\frac1{1+K\det T\,\zeta^{\mathsf T}N_C^{-1}\zeta}.
\]
Substituting \(T^{-1}=\alpha W/\det W\) proves (4).

For (5), continue in the real block gauge and let
\(A_0=\operatorname{Re}(vv^*)\). Its Fisher covector is \(\eta\), and
its imaginary covector component is zero. Lemma 3.1 yields
\[
 \eta^{\mathsf T}N_C^{-1}\eta
 \le2\eta^{\mathsf T}F^{-1}\eta
 =2F_C(A_0,A_0),\qquad
 \frac K{\det W}\eta^{\mathsf T}N_C^{-1}\eta
 \le4Ks_2\le2(K+1).
\]
Formula (4) proves (5). All four block and all four connection directions
were retained in (19); the reduction of the limiting source discards no
ambient Hessian direction. This proves Theorem 1. \(\square\)

## 5. Proof of the uniform remainder

All norms in this section are Euclidean operator norms or Euclidean vector
norms. Analytic extensions use the bilinear trace products in (19), without
conjugating the complex variable \(x\).

Fix \(a,C,v\). We have \(\nu\le1/16\). Every constant atom in (17)
is at least \(\nu\), and every atom slope has modulus at most one:
\[
 |\pi_Tk_T|=|v^*\operatorname{adj}(M_T)v|\le1.
\]
On the complex disk \(|x|\le\rho=\nu/8\), continue each logarithm
from zero. Then
\[
 |\log p_S(x)-\log p_S(0)|\le2|x|/\nu.
\]
Each pair log odds changes by at most \(8|x|/\nu\), and
\(|\gamma(x)|\le16|x|/\nu\). The isolated-pair odds have zero
constant term. Also \(K\le2\log(1/\pi_*)\le2/\nu\).
These bounds, applied entrywise to \(\overline R\), imply
\[
 \|\overline R(x)\|\le100/\nu\quad(|x|\le\rho),\qquad
 \|\overline R(x)-\overline R(0)\|
 \le10^4|x|/\nu^2\quad(|x|\le\rho/2).                            \tag{20}
\]
For the second estimate, Cauchy's coefficient bound gives even
\(1600|x|/\nu^2\) from the first. The lower-block diagonal quotients
are bounded by \(24/\nu\), its off-diagonal quotient by \(16/\nu\),
and the isolated off-diagonal entries by \(16|x|/\nu\); these also
verify the first estimate directly.

By (15)–(16), (18), and the limiting decomposition of (19),
\[
 \overline R(0)\succeq\mu I,\qquad J(0)\succeq\mu I.              \tag{21}
\]
For the second statement the three block lower bounds are respectively
\(1/\alpha\), \(\min(r^2/4,2K)\), and \(2\omega/\alpha\).
On
\[
 |x|\le R_*:=\mu^3/10^6,
\]
(20) is at most \(\mu/100\). Hence
\[
 \|B\|\le2/\mu,\quad |\bar d|\le10^6/\mu^3,\quad
 \|\bar z\|\le100/\mu.                                          \tag{22}
\]
Every \(Y_i\) has norm at most one. Every scaled atom derivative has
modulus at most ten: block derivatives are quadratic cofactors with
connection products proportional to \(x\), and a connection derivative
divided by \(\sqrt{x}\) is a sum of at most four products of fixed
entries of modulus at most one. These expressions remain bounded by ten
on the disk. Since \(|p_S|\ge\nu/2\), every Fisher entry is bounded
by \(1600/\mu\). The trace bound
\(|\operatorname{tr}(BY_iBY_j)|\le12/\mu^2\), together with (22),
gives the deliberately enlarged uniform estimate
\[
 \|J(x)\|\le10^{10}/\mu^5\quad(|x|\le R_*).                       \tag{23}
\]
Cauchy's coefficient bound on the half disk yields
\[
 \|J(x)-J(0)\|\le2\cdot10^{16}|x|/\mu^8.
\]
In particular, on \(|x|\le r_*:=\mu^9/10^{18}\), the perturbation
is at most \(\mu/50\), so \(\|J^{-1}\|\le2/\mu\).
Equations (19) and (22) now bound its analytic margin extension by
\[
 |m(x)|\le3\cdot10^{10}/\mu^6\quad(|x|\le r_*).
\]
A final Cauchy estimate gives, on \(|x|\le r_*/2\),
\[
 |m(x)-m(0)|\le6\cdot10^{28}|x|/\mu^{15}
 \le10^{30}|x|/\mu^{15}.
\]
This proves (7).

For real \(x\) in (7), strictness also follows directly from Schur
complements. Both \(C\) and \(I-C\) have least eigenvalue at least
\(\pi_*\). Since \(x\le\nu/8\),
\[
 x v^*C^{-1}v<a,\qquad
 x v^*(I-C)^{-1}v<1-a.
\]
The block edge is nonzero and at least one connection is nonzero, proving
connectedness. Condition (8) implies the range of (7) and makes its error
at most \(1/[2(2K+3)]\). Combining with (5) proves
\(m\ge1/(4K+6)>0\).

For each block pattern the two joint atoms sum to \(\pi_T\), so
\(\min_Sp_S(Q_x)\le\pi_*/2\). Thus
\[
 K\le2\log(1/\pi_*)\le2\Lambda(Q_x).
\]
This proves (9), and (11) proves strict negative definiteness of the full
ambient Hessian. The same elementary logarithmic bound proves the stated
\(\Lambda_0\) estimate. Theorem 2 follows. \(\square\)

## 6. Boundary strata and coverage

The boundary types are described by the multiplicities \((k_0,k_1)\) of
eigenvalues zero and one, and by the support graph. A spectral face in the
convex-geometric sense additionally fixes its zero and one eigenspaces;
\((k_0,k_1)\) describes its type. Graph strata are specified by which
edge entries vanish. Coordinate permutations identify the choices of an
isolated vertex or a missing edge.

The following table lists every realizable coarse type. A triangle has
three nonzero edges, a path has two, a block has one, and a diagonal graph
has none. Spectral type \((0,0)\) with a triangle is the interior control
stratum rather than a boundary face.

| Spectral type \((k_0,k_1)\) | Triangle | Path | Block | Diagonal |
| --- | --- | --- | --- | --- |
| (0,0) | yes | yes | yes | yes |
| (1,0), (0,1) | yes | yes | yes | yes |
| (2,0), (0,2) | yes | impossible | yes | yes |
| (1,1) | yes | yes | yes | yes |
| (2,1), (1,2) | yes | impossible | yes | yes |
| (3,0), (0,3) | impossible | impossible | impossible | yes |

For the impossible path entries, either \(Q\) or \(I-Q\) has rank one.
A rank-one Hermitian positive matrix has edges exactly between pairs of
nonzero vector coordinates. Its graph is a clique on that support, so it
cannot be a connected path. The zero matrix and the identity have no edges.
All remaining entries are realized by diagonal blocks, a rank-one factor,
or an irreducible three by three Jacobi matrix with the indicated distinct
eigenvalues. In the block column, one must additionally specify which
endpoint eigenvalues belong to the isolated scalar and which belong to the
two-point block. The numerical descriptors retain this allocation.

There can be extra vanishing atoms inside a coarse spectral/graph type.
The following exact criterion supplies the necessary refinement.

**Lemma 6.1 (zero-atom refinement).** For any positive contraction \(Q\)
and any subset \(S\),
\[
 p_S(Q)=0\quad\Longleftrightarrow\quad
 [\ker Q\cap\mathbb C^S\ne\{0\}]
 \ \text{or}\
 [\ker(I-Q)\cap\mathbb C^{S^c}\ne\{0\}].                         \tag{24}
\]

**Proof.** By the signed atom determinant, the left side means that
\((Q-D_{S^c})y=0\) for a nonzero vector \(y\). Then
\(y^*Qy=\|D_{S^c}y\|^2=\|Qy\|^2\), so
\(y\in\ker(Q-Q^2)=\ker Q\oplus\ker(I-Q)\). Write \(y=y_0+y_1\)
in those two spaces. The equation is \(D_{S^c}y=y_1\); applying the
projection \(D_{S^c}\) again shows \(D_{S^c}y_1=y_1\) and
\(D_{S^c}y_0=0\). Thus the nonzero components have the support asserted
on the right. Conversely either such component is a nonzero null vector
of \(Q-D_{S^c}\). \(\square\)

For example, a simple zero eigenvalue with a null vector having no zero
coordinates gives only the full-atom zero, unless there is also an
endpoint-one eigenspace. A null vector supported on a pair gives an
additional zero pair atom. Formula (24), together with fixed endpoint
eigenspaces and the edge-zero constraints, describes all refinements; no
claim of uniform control over these refinements follows just from a generic
spectral expansion. Phase zero and phase pi are ends of a gauge interval,
not additional boundary faces of the Hermitian contraction set.

The proved coverage is as follows. A bound in a specified collar should
not be read as a bound at every approach to the entire named face.

| Face or approach | What is proved | What remains open |
| --- | --- | --- |
| Strict disconnected graph, including diagonal kernels | Ambient Hessian is nonpositive at every such kernel (C0033C Theorem A); boundary endpoints of coordinate block families follow from C0033A continuity | The scalar margin is undefined on the disconnected face itself; this sign statement alone is not a scaled collar |
| One nontrivial strict block plus an isolated point; arbitrary complex small connections | Theorems 1–2 give (7)–(9), uniformly in connection direction, block balance, and isolated weight | Connections outside (8), including competing rates when a block spectral gap collapses faster |
| All three graph edges vanish at a fixed strict diagonal kernel | C0033D (5): positive margin along fixed all-nonzero edge ratios, uniformly over compact sets of such ratios; Theorem 2 also covers sufficiently hierarchical edge scales | A single uniform neighborhood allowing all edge ratios and simultaneous spectral degeneracy |
| One missing edge, graph still a connected path | Theorem 2 covers the path subcollars with one weak remaining edge | Arbitrary strict paths; adding a tiny missing edge does not settle the unknown constant term |
| One simple zero or one eigenvalue, connected graph | C0033D (14) gives the singular Fisher and logarithmic terms | The residual finite tangent form and a uniform scaled collar, including the refinements (24) |
| Two zero eigenvalues or two one eigenvalues, connected triangle | Numerical searches and inherited point certificates | A general scaled spectral collar |
| One zero and one one eigenvalue, connected graph | The cyclic family has an exact positive margin (C0033D/E); Theorem 2 covers its specified nearly disconnected subcollars | Generic eigenspaces and approaches, including connected paths |
| Rank-one and rank-two projection limits | Numerical searches; the preceding cyclic and mixed subfamilies where applicable | A uniform scaled collar for all orientations and all relative spectral gaps |
| Zero and identity | C0033D (6) proves \(m\to1\) along \(tK\), \(I-tK\) with fixed positive definite all-edge data, uniformly on compact such data | Arbitrarily degenerate normalized shapes and simultaneous graph limits |
| Spectral/graph intersections with a scalar endpoint or a singular two-point block | Exact coordinate block restrictions inherit the two-point theorem; Theorem 2 reaches these intersections whenever (8) holds before the limit | The other relative rates of approach; no complete intersection collar is proved |

Theorem 2 is an actual uniform collar over compact subsets of the strict
one-edge graph face, since \(\mu\) then has a positive lower bound.
It also supplies explicit neighborhoods along spectral degenerations of
the block, with their necessary shrinking width. It does not remove every
boundary approach. For example, choose a fixed generic unitary \(U\) so
that all three edges of
\(U\operatorname{diag}(0,3/10,4/5)U^*\) are nonzero, and approach it
by replacing zero with \(\varepsilon\). Every candidate connection norm
in (2) stays bounded away from zero, whereas the right side of (8) tends
to zero. This approach is neither a mixed collar in this report nor the
cyclic family. A noncompact remainder therefore remains.

A possible compact target, after suitable boundary estimates, is
\[
 \mathcal K_{\delta,\kappa}=
 \{Q:\delta I\le Q\le(1-\delta)I,
       \text{the second largest of }|Q_{12}|,|Q_{13}|,|Q_{23}|
       \text{ is at least }\kappa\}.
\]
It includes paths and is compact and connected in the graph-theoretic
sense at every point. Its complete interval cover has not been supplied.
C0033D's truncated target instead requires all three edges to be at least
\(1/10\), excludes paths, and retains pending cells. Its completed cover
is only its box (9).

For Proposition 3, the inherited four accepted leaves give
\(m>0.02478\), and normalization gives \(\Lambda\ge\log8\).
Thus \(m(\Lambda+6)>0.02478(\log8+6)>1/8\). The outward interval
implementation [scaled_cover.py](scaled_cover.py) reproduces all seven
nodes and four leaves, with no unresolved cell, on that exact box only.
The leaf bounds are in [data/scaled_cover.json](data/scaled_cover.json).
This proves (10). The inherited [bnb.py](bnb.py) tests signs, or the
cardinality lower bound; it does not by itself certify an arbitrary
prescribed scaled constant on a global remainder. The wrapper adds that
scaled test for this local box.
