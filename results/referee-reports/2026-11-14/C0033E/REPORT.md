PARTIAL

# Three-point determinantal entropy at a mixed spectral and graph boundary

Let $H(Q)=-\sum_Sp_S(Q)\log p_S(Q)$, with natural logarithms. On the connected strict three-point domain, write $m(Q)=1-\theta(Q)$, using C0033C (21), equivalently C0033D (2). Define
\[
\Lambda(Q)=-\log\min_Sp_S(Q).
\]
The full three-point concavity assertion remains unresolved. No negative margin was found. The results established here are an independent exact calculation on the cyclic family, a uniform estimate on a restricted mixed collar, and an obstruction to the constant in a possible global atom-logarithmic bound.

**Theorem 1 (independent cyclic formula and explicit remainder).** For C0033D's family
\[
Q_r=\begin{pmatrix}1/2&ir&-ir\\-ir&1/2&ir\\ir&-ir&1/2\end{pmatrix},
\quad 0<r<1/(2\sqrt3),\qquad
k=\frac{1+4r^2}{1-12r^2},\quad L=\log k,
\]
put
\[
\begin{aligned}
A(k,L)&=9k^3-15k^2+3k+3+(6k^2+6k-4)L-(3k^2+k)L^2,\\
B(k,L)&=36k^3-60k^2+12k+12
 +(9k^3+33k^2-21k+11)L+(6k^2+2k)L^2.
\end{aligned}
\]
Then
\[
 m(Q_r)=\frac{4A(k,L)}{B(k,L)}. \tag{1}
\]
This agrees identically with C0033D (12), and gives both expansions in C0033D (4). For $L\ge4$, the following explicit bounds hold:
\[
 m(Q_r)\ge\frac2{L+2},\qquad
 \left|m(Q_r)-\frac4{L+4}\right|\le\frac{10}{3}Le^{-L}. \tag{2}
\]
The derivation of (1) below uses the full nine-direction atom Hessian and a determinant ratio, rather than the two-dimensional inverse calculation in C0033D.

**Theorem 2 (a uniform restricted mixed collar).** Suppose $0<a<1$, $0<h\le1/4$, and define
\[
 b_0=h(1-h),\quad b_1=\tfrac12-b_0,\quad
 \nu=a(1-a)b_0,\quad k=b_1/b_0,\quad K=2\log k.
\]
For $e>0$, set
\[
 Q(a,h,e)=\begin{pmatrix}
 a&e&e\\ e&1/2&h-1/2\\ e&h-1/2&1/2
 \end{pmatrix},\qquad x=e^2,
\]
and assume
\[
 0<x\le\frac{\nu^8}{8\cdot10^{13}(K+1)}. \tag{3}
\]
Then $0<Q<I$, its graph is connected, and its full ambient entropy Hessian is negative definite. More precisely, let
\[
 f=\frac1{b_0}-\frac1{2b_1},\qquad
 g=\frac1{2b_1},\qquad v=\frac1{b_0}-3,
\]
and set
\[
 m_0(h)=\frac{f^2-(g-K)^2}{f^2-g^2+fK(v+v^{-1})+K^2}. \tag{4}
\]
For every $0<x\le\nu^5/(2\cdot10^9)$, the extension from $x>0$ satisfies the explicit uniform remainder estimate
\[
 |m(Q(a,h,e))-m_0(h)|\le4\cdot10^{13}\frac{x}{\nu^8}. \tag{5}
\]
Moreover,
\[
 m_0(h)\ge\frac1{K+1};\qquad
 0\le m_0(h)-\frac1{K+1}\le\frac3{k(K+1)}\quad(k\ge2). \tag{6}
\]
Consequently (3) implies
\[
 m(Q(a,h,e))\ge\frac1{2(K+1)}\ge\frac1{4\Lambda(Q)+2}. \tag{7}
\]
All constants in (3), (5), and (7) are independent of $a,h,e$ in the stated ranges. In particular, $a$ may approach either endpoint at an arbitrary rate. The restriction to equal real connections and a balanced two-point block is part of the theorem.

**Corollary 3 (the coefficient of a possible global bound).** Put
\[
 Q_h=Q(1/2,h,h^6),\qquad 0<h\le10^{-6}.
\]
Then (3) holds, and
\[
 \lim_{h\downarrow0}\Lambda(Q_h)m(Q_h)=\frac12. \tag{8}
\]
Therefore a universal inequality $m(Q)\ge c/(\Lambda(Q)+C)$, with fixed finite $C$, can hold only if $c\le1/2$. Along the cyclic family the corresponding limit is (4). The atom logarithm remains a plausible scale; its optimal global coefficient is not proved here.

## 1. Inherited results and the ambient criterion

The two-point theorem, conditional lifting, and block/product variations are credited to [C0033A](../C0033A/REPORT.md). The positive matrix $R_Q$, atom Hessian identity, and scalar criterion are credited to [C0033B](../C0033B/REPORT.md). The singular-$R_Q$ classification and its ambient Hessian sign are credited to [C0033C](../C0033C/REPORT.md). The seven-atom matrix formulation, cyclic family, and completed local interval cover are credited to [C0033D](../C0033D/REPORT.md). These results are used without re-proving them.

For reference, with $\{i,j,k\}=\{1,2,3\}$,
\[
 \ell_{ij}^0=\log\frac{p_ip_j}{p_0p_{ij}},\quad
 \gamma=\log\frac{p_{123}p_1p_2p_3}{p_0p_{12}p_{13}p_{23}},\quad
 R=\operatorname{diag}(\ell_{23}^0,\ell_{13}^0,\ell_{12}^0)-\gamma Q.
\]
On the connected strict domain, $R>0$. In any real basis $E_i$ of all Hermitian directions, put
\[
 F_{ij}=\sum_S\frac{Dp_S[E_i]Dp_S[E_j]}{p_S},\quad
 d=\det R,\quad z_i=\operatorname{tr}(R^{-1}E_i),\quad
 J_{ij}=F_{ij}+d\operatorname{tr}(R^{-1}E_iR^{-1}E_j).
\]
The inherited identity is
\[
 -D^2H=J-dzz^{\mathsf T},\qquad
 \theta=d z^{\mathsf T}J^{-1}z,\qquad J>0. \tag{9}
\]
This formula is basis invariant. In particular, no Hessian in a nonlinear seven-parameter chart is substituted for the nine-dimensional Hessian.

The requested files [dpp.py](dpp.py), [dpp.cpp](dpp.cpp), [reduced.py](reduced.py), [boundary.py](boundary.py), [interval_core.py](interval_core.py), and [bnb.py](bnb.py) are verbatim copies from C0033D. Their sources and hashes are recorded in [data/inherited_manifest.json](data/inherited_manifest.json). New computations are in the other scripts named below.

## 2. Proof of Theorem 1

Use the unnormalized coordinate basis in the order
\[
 (q_{11},q_{22},q_{33},\Re q_{12},\Im q_{12},\Re q_{13},\Im q_{13},\Re q_{23},\Im q_{23}).
\]
Write $u=r^2$, $p_0=p_{123}=A_0=(1-12u)/8$, and $p_S=B_0=(1+4u)/8$ for the other six atoms. All derivatives below are derivatives of the signed determinant polynomials $p_S=(-1)^{3-|S|}\det(Q-D_{S^c})$. Let $G$ be their eight by nine gradient matrix, $F=G^{\mathsf T}\operatorname{diag}(p_S^{-1})G$,
\[
 D=\operatorname{diag}(1,1,1,2,2,2,2,2,2),\qquad
 t=(1,1,1,0,0,0,0,0,0)^{\mathsf T}.
\]
Direct differentiation gives
\[
 \sum_{S\ne\varnothing,123}D^2p_S=D-tt^{\mathsf T}.
\]
The common $\log A_0$ term cancels because $\sum_SD^2p_S=0$. The negative Hessian computed from the atom formula alone is therefore
\[
 N=F+L(D-tt^{\mathsf T}),\qquad J=N+Ltt^{\mathsf T}=F+LD.
\]
Here $R=LI$, so (9) and the matrix determinant lemma give
\[
 m=1-Lt^{\mathsf T}J^{-1}t=\frac{\det N}{\det J}. \tag{10}
\]

For a checkable determinant expansion, order the real directions as $1,2,3,4,6,8$ and the imaginary directions as $5,7,9$. Both matrices have zero cross blocks. Set
\[
\begin{aligned}
 P_+={}&(48u^2+8u-1)L^2+(4608u^3-192u^2-4)L-1536u^2,\\
 P_-={}&(48u^2+8u-1)L^2+(2304u^3-480u^2+2)L+768u^2,\\
 C_0={}&\frac{8L^2((4u+1)L+4)^2}{(4u+1)^3(12u-1)}.
\end{aligned}
\]
Expansion of the six by six blocks yields
\[
 \det J_{\mathrm{real}}=C_0P_+,\qquad
 \det N_{\mathrm{real}}=-2C_0P_-.
\]
The common three by three imaginary-block determinant is
\[
 \frac{8((4u+1)L+32u)^2((48u^2+8u-1)L-32u)}{(4u+1)^3(12u-1)}.
\]
These identities can be verified by forming the eight signed cubic determinants and their first and second derivatives; the complete gradient matrix and factorizations are in [data/exact_cyclic.json](data/exact_cyclic.json), generated by [exact_cyclic.py](exact_cyclic.py). Thus (10) is $-2P_-/P_+$. Substitution of $u=(k-1)/(4(3k+1))$ gives (1).

For comparison with C0033D (12), define
\[
 f_{22}=\frac{9(k-1)^2(k+3)}{k(3k+1)},\quad
 D_0=36\left[-L^2+\frac{6k^2+6k-4}{k(3k+1)}L+3\frac{(k-1)^2}{k}\right].
\]
Rational simplification of (1) gives
\[
 m=\frac{s}{9L+s},\qquad s=\frac{D_0}{f_{22}+6L}. \tag{11}
\]
The symbolic difference is zero, establishing agreement with the exact formula in C0033D. Expanding (1) with $L=\log((1+4u)/(1-12u))$ at $u=0$ gives $1-m=12u+O(u^2)$.

For the explicit large-$L$ remainder, let $k=e^L$, $L\ge4$. Then
\[
 3k\le f_{22}\le3k+2,\qquad
 2\le\frac{6k^2+6k-4}{k(3k+1)}\le6.
\]
Consequently
\[
 0<36-s\le12e^{-L}(L^2+4L+8). \tag{12}
\]
Indeed, subtract $f_{22}+6L$ from $D_0/36$; the difference is negative, with absolute value at most $L^2+4L+8$, and divide by $f_{22}+6L\ge3k$. The right side of (12) decreases for $L\ge4$ and is less than (18) at $L=4$. Thus $s\ge18$, proving the first inequality in (2). Finally,
\[
 \left|\frac{s}{9L+s}-\frac{36}{9L+36}\right|
 \le\frac{|s-36|}{9L}
 \le\frac43 e^{-L}(L+4+8/L)
 \le\frac{10}{3}Le^{-L}.
\]
This proves (2), the second expansion in C0033D (4), and Theorem 1. $\square$

## 3. The mixed limit and proof of Theorem 2

Apply the fixed orthogonal change from coordinates $2,3$ to their symmetric and antisymmetric modes. In that basis,
\[
 Q=\begin{pmatrix}a&\sqrt2e&0\\\sqrt2e&h&0\\0&0&1-h\end{pmatrix}.
\]
This change is used to express directions and $R$, not to change the ground set of the determinantal law. The atom probabilities in the original ground set, in order $0,1,2,12,3,13,23,123$, are affine in $x=e^2$:

| Atom | Constant $p_S(0)$ | Coefficient of $x$ |
| --- | --- | --- |
| (0) | $(1-a)b_0$ | (-2h) |
| (1) | $ab_0$ | (2h) |
| $2,3$ | $(1-a)b_1$ | (2h-1) |
| $12,13$ | $ab_1$ | (1-2h) |
| (23) | $(1-a)b_0$ | (2(1-h)) |
| (123) | $ab_0$ | (-2(1-h)) |

The symmetry interchanging $2,3$, and complex conjugation, preserve $J$ and the source $z$ in (9). Hence the inverse solve for that source belongs to the four-dimensional real fixed space. A basis of this space, in the displayed mode basis, is
\[
 E_{00},\ E_{11},\ E_{22},\ x^{-1/2}(E_{01}+E_{10}). \tag{13}
\]
Using this invariant space computes the full ambient scalar criterion. It does not restrict which Hessian directions are tested by that criterion.

### 3.1 The removable singularity at zero connection

Let
\[
 \ell=\log\frac{p_1p_3}{p_0p_{13}},\qquad
 \ell_B=\log\frac{p_2p_3}{p_0p_{23}}.
\]
In the mode basis, write
\[
 R=S\overline R S,\qquad S=\operatorname{diag}(1,\sqrt x,\sqrt x),
\]
where
\[
 \overline R=
 \begin{pmatrix}
 \ell_B-a\gamma&-\sqrt2\gamma&0\\
 -\sqrt2\gamma&(\ell-h\gamma)/x&0\\
 0&0&(\ell-(1-h)\gamma)/x
 \end{pmatrix}. \tag{14}
\]
All entries have analytic extensions in $x$ at zero. Differentiating the atom table gives
\[
 \gamma'(0)=\frac{2h-1}{a(1-a)b_0b_1},\quad
 P:=\left.\frac{\ell-h\gamma}{x}\right|_{0}=\frac1{a(1-a)b_1},\quad
 T:=\left.\frac{\ell-(1-h)\gamma}{x}\right|_{0}
 =\frac{1-3b_0}{a(1-a)b_0b_1}.
\]
Thus $\overline R(0)=\operatorname{diag}(K,P,T)$, with $T/P=v$. The identities are also checked as exact rational identities in [mixed_limit.py](mixed_limit.py).

Put $B=\overline R^{-1}$, $\overline d=\det\overline R$, and
\[
 Y_0=xE_{00},\quad Y_1=E_{11},\quad Y_2=E_{22},\quad Y_3=E_{01}+E_{10},\qquad
 \overline z_i=\operatorname{tr}(BY_i).
\]
In the basis (13), the matrix in (9) is exactly
\[
 J_{ij}(x)=F_{ij}(x)+\overline d\operatorname{tr}(BY_iBY_j),\qquad
 \theta(x)=\overline d\,\overline z^{\mathsf T}J(x)^{-1}\overline z. \tag{15}
\]
The Fisher matrix $F(x)$ is analytic: the first three atom derivatives are polynomials in $x$, while the fourth is $\sqrt2$ times the coefficient in the last column of the atom table. Thus (15) removes the singular factors $x^{-1}$ from the criterion.

At zero, the Fisher score of the fourth direction is orthogonal to every marginal score: both the one-point marginal on coordinate (1) and the two-point marginal on coordinates $2,3$ are unchanged by a connection. Independence at $x=0$ also makes their marginal Fisher cross block zero. Therefore the (0) and (3) coordinates decouple at zero. On coordinates $1,2$, the matrix and source in (15) reduce to
\[
 \begin{pmatrix}f+Kv&g\\g&f+K/v\end{pmatrix},\qquad
 \sqrt{\overline d}\,\overline z=
 \begin{pmatrix}\sqrt{Kv}\\\sqrt{K/v}\end{pmatrix}.
\]
A two by two determinant calculation now gives (4). In particular, this limit is independent of $a$, although its uniform remainder depends on $\nu$.

To prove (6), write
\[
 f=2k+1-k^{-1},\quad g=1+k^{-1},\quad v=2k-1,
\]
and denote the numerator and denominator of (4) by $N,D$. Direct algebra gives
\[
 (K+1)N-D=K\{4(k-k^{-1})+2K/k-K^2\}. \tag{16}
\]
For $t=\log k\ge0$,
\[
 k-k^{-1}=2\sinh t\ge2t+t^3/3\ge t^2,
\]
because $t^2/3-t+2>0$. Since $K=2t$, (16) is nonnegative. Also $D>0$, as it is the determinant of a positive definite matrix. This proves the first inequality in (6). For $k\ge2$,
\[
 D\ge2(K+1)k^2,\qquad K+1\le k^2.
\]
Dropping the negative terms in the braces of (16) gives
\[
 0\le\frac ND-\frac1{K+1}
 \le\frac{2}{k(K+1)}+\frac1{k^3}
 \le\frac3{k(K+1)},
\]
which proves the remaining assertion.

### 3.2 Explicit uniform remainder

The following bounds use the Euclidean operator norm for matrices and the Euclidean norm for vectors; complex analytic extensions are taken without complex conjugation in the bilinear products of (15). Fix $a,h$ in the theorem's ranges. Then $\nu<1/16$. On the complex disk
\[
 |x|\le\rho:=\nu/8,
\]
every constant atom is at least $\nu$, and every atom slope has modulus at most (2). Choose logarithms by continuation from $x=0$. The elementary estimate for $\log(1+w)$, $ |w|\le1/4$, yields
\[
 |\log p_S(x)-\log p_S(0)|\le3|x|/\nu.
\]
It follows that
\[
 |\gamma(x)|\le24|x|/\nu,\quad
 |\ell_B(x)-K-a\gamma(x)|\le36|x|/\nu,
\]
and the analytic functions $(\ell-h\gamma)/x$, $(\ell-(1-h)\gamma)/x$ have modulus at most $36/\nu$. Cauchy's coefficient bound, on $ |x|\le\rho/2$, consequently gives
\[
 \|\overline R(x)-\overline R(0)\|\le2000|x|/\nu^2. \tag{17}
\]
For example, either of the last two diagonal entries differs from its value at zero by at most $576|x|/\nu^2$; the off-diagonal entry has modulus at most $34|x|/\nu$, and the first diagonal difference is at most $36|x|/\nu$. These entry bounds imply (17).

Here $K>1$, $P\ge8$, and $T\ge P$. Also $K,P,T\le4/\nu$. On the smaller disk
\[
 |x|\le R_*:=\nu^2/8000,
\]
(17) is at most $1/4$, so
\[
 \|B\|<2,\quad \|\overline R\|\le5/\nu,\quad
 |\overline d|\le125/\nu^3,\quad \|\overline z\|\le12. \tag{18}
\]
Each atom derivative in the basis (13) has modulus at most $10$ on this disk. For the first three directions this follows either by differentiating the table before setting the antisymmetric eigenvalue to $1-h$, or from the cofactor bound $\|Q-D_{S^c}\|<2$; the fourth derivative was given explicitly above. Since $|p_S|\ge3\nu/4$, every Fisher entry has modulus less than $1100/\nu$. Equations (18) imply that every metric entry in (15) has modulus at most $1500/\nu^3$. Therefore
\[
 \|J(x)\|\le11000/\nu^3\quad (|x|\le R_*). \tag{19}
\]

At zero, $J_{00}=1/[a(1-a)]\ge4$. On its middle two coordinates the Fisher eigenvalues are $f+g=1/b_0$ and $f-g=1/b_0-1/b_1\ge32/15>2$. The final coordinate has metric term $2T>2$. The decoupling proved above thus gives $J(0)\succeq2I$. Applying Cauchy's coefficient bound to (19), for $ |x|\le R_*/2$, yields
\[
 \|J(x)-J(0)\|\le176000000\,|x|/\nu^5.
\]
On $ |x|\le r_*:=\nu^5/10^9$, this is less than $1/4$. Consequently $J^{-1}$ is analytic there and has norm less than $1$. From (15), (18),
\[
 |1-\theta(x)|\le18001/\nu^3\quad (|x|\le r_*).
\]
One last Cauchy estimate, on $ |x|\le r_*/2$, gives
\[
 |m(x)-m(0)|\le\frac{36002\cdot10^9}{\nu^8}|x|
 <4\cdot10^{13}|x|/\nu^8.
\]
This proves (5), with $m(0)$ denoting the analytic extension $m_0(h)$.

Condition (3) implies $x\le r_*/2$ and makes the last error at most $1/[2(K+1)]$. It also implies $2x<ah$ and $2x<(1-a)(1-h)$. In the mode basis these are the determinant conditions for the nontrivial blocks of $Q$ and $I-Q$; hence $0<Q<I$. Its two edges equal to $e>0$ give connectedness. Combining (5) and (6) proves the first bound in (7), and then (9) proves negative definiteness in all nine directions. Finally $p_0=(1-a)b_0-2hx\le b_0$, so $K\le2\log(1/b_0)\le2\Lambda(Q)$. This proves the second bound in (7) and Theorem 2. $\square$

## 4. Proof of Corollary 3

For $a=1/2$ and $e=h^6$, $\nu=h(1-h)/4\ge3h/16$. Also $K\le2\log(1/h)$. For $0<h\le10^{-6}$,
\[
 h^4(2\log(1/h)+1)\le10^{-24}(12\log10+1)
 <\frac{(3/16)^8}{8\cdot10^{13}},
\]
which verifies (3). Formula (5) gives an error at most $4\cdot10^{13}(16/3)^8h^4$. From (6),
\[
 m(Q_h)=\frac{1+O(h)}{2\log(1/h)+1-2\log2+O(h)}+O(h^4),
\]
with uniform bounds supplied by (5), (6). The atom table gives $\min_Sp_S(Q_h)\sim h/2$, so $\Lambda(Q_h)=\log(1/h)+\log2+o(1)$. Multiplication proves (8). Multiplying any proposed global bound by $\Lambda(Q_h)$ proves $c\le1/2$. $\square$

## 5. High-precision searches and point certificates

All values in search tables are attained values, not certified minima over a continuous collar. Every evaluation enumerates all eight atoms and retains all nine ambient directions in the scalar criterion. The sweep seed is 33505; optimization seeds and stopping information are saved with the data. All arithmetic used for atoms, logarithms, and solves is mpmath arithmetic at 100 or more decimal digits. Binary numbers are used only by the outer optimizer and to select random parameters.

The sweep proposed 5,099 parameter choices: 377 did not define an ordered strict spectrum, and 243 constructed candidates were rejected. There were 4,479 accepted evaluations. The first 50 rejection diagnostics are saved. An independent replay confirms that all 243 constructed rejections fail strictness; see [audit_inputs.py](audit_inputs.py) and [data/input_audit.json](data/input_audit.json). The 870 ambient perturbations comprise both signs of each of nine coordinate directions at three radii, and 120 dense Hermitian combinations at each of five scales. Their Frobenius radii are less than the spectral gap, so feasibility is controlled before evaluation. Code: [search_mp.py](search_mp.py), [mp_core.py](mp_core.py); data: [data/search_mp.json](data/search_mp.json).

| Cyclic scale L | Cyclic margin | Smallest ambient-perturbation margin | Smallest scaled perturbation margin |
| --- | ---: | ---: | ---: |
| 20 | 0.166666620100 | 0.162840181847 | 4.29323166372 |
| 60 | 0.0625000000000 | 0.0620020796458 | 4.11144796770 |
| 150 | 0.0259740259740 | 0.0258910177158 | 4.04644620101 |
| 400 | 0.00990099009901 | 0.00988820747798 | 4.01772666186 |
| 1000 | 0.00398406374502 | 0.00398145657192 | 4.00713629204 |

Here and below a scaled margin means $m(\Lambda+4)$. A fixed additive constant does not affect the limiting coefficient.

| Scale L | Generic spectral/graph accepted | Generic smallest margin | Mixed accepted | Mixed smallest margin | Mixed smallest scaled margin |
| --- | ---: | ---: | ---: | ---: | ---: |
| 20 | 547 | 0.0289094136861 | 345 | 0.0125606513599 | 0.678275173435 |
| 60 | 555 | 0.00957025778693 | 340 | 0.00417338397791 | 0.642701132598 |
| 150 | 563 | 0.00516070366671 | 331 | 0.00166774039785 | 0.632073610786 |
| 400 | 558 | 0.00155915461879 | 365 | 0.000625150932675 | 0.627651536406 |

The finite collar searches used 14,182 objective calls for the margin and 5,821 for the scaled margin, including 3,007 and 988 rejected calls respectively. Their explicitly fixed endpoint eigenvalues are exp(-L) and 1-exp(-bL), with b in [0.12,1]; the middle eigenvalue and all four unitary orientation parameters vary. The first search limits angle logits to [-0.8L,0.8L]; the scaled search uses [-4L,4L] to resolve strongly unequal couplings to the low and high modes. These different orientation ranges are part of the search specification. All four differential-evolution runs and the local runs retain their stopping status in the JSON; no global optimality is asserted. Code: [optimize_collar.py](optimize_collar.py), [refine_scaled.py](refine_scaled.py); data: [margin search](data/collar_optimization.json), [scaled search](data/scaled_optimization.json).

| Collar scale L | Smallest margin in margin search | Margin at scaled-search optimum | Smallest scaled margin |
| --- | ---: | ---: | ---: |
| 20 | 0.0252483183146 | 0.0252437884319 | 0.623348583195 |
| 60 | 0.00880248398508 | 0.00836024596562 | 0.540850622719 |
| 150 | 0.00333824435516 | 0.00333763102682 | 0.516308647666 |
| 400 | 0.00125060387653 | 0.00125060387653 | 0.506110818670 |

The smallest located margin, to the displayed precision, is approximately **0.000250024145729409772194102983447**, on the structured family
\[t=e^{-1000},\qquad Q=Q(1-t^2,t^2,t^{21/10}).\]
The four structured probes at L=1000 in [data/mixed_limit.json](data/mixed_limit.json) have margins agreeing at the displayed precision. For an unambiguous certified point, the exact rational rounding of the displayed kernel is saved under `special_mixed_min_L1000` in [data/verification.json](data/verification.json). Its interval below certifies the same displayed margin. A family parameterization and a rational rounding are distinct exact kernels; their agreement is numerical, and the interval assertion is for the saved rational kernel.

The normalization obstruction is visible before extrapolation. Code: [mixed_limit.py](mixed_limit.py), [verify_results.py](verify_results.py); data: [mixed limits](data/mixed_limit.json), [independent audit](data/verification.json).

| h=exp(-L), e=h^6, a=1/2 | Margin | Lambda times margin | In the proved collar |
| --- | ---: | ---: | --- |
| L=10 | 0.0509893512378 | 0.545238952393 | no |
| L=20 | 0.0252437884312 | 0.522373429453 | yes |
| L=60 | 0.00836024596562 | 0.507409638857 | yes |
| L=150 | 0.00333763102682 | 0.502958123559 | yes |
| L=400 | 0.00125060387653 | 0.501108403164 | yes |
| L=1000 | 0.000500096592247 | 0.500443232790 | yes |

The fixed-data check at a=0.37 and h=0.1 gives $m-m0$/e^2 approaching -0.222801675401. The atom-logarithm estimate (5) is deliberately conservative; it is a uniform estimate with explicit parameters, not a fitted error.

The eta=16 probes inside the proved collar use adaptive precision until their direct ambient scalar solves resolve the explicit remainder (5). Their final precisions and retry counts are saved in the mixed-limit data. Fixed decimal precision based only on the spectral gap can be inadequate when the connections vanish much faster. Point certificates use exact rational coordinates and outward-rounded mpmath.iv operations. Leading principal minors certify Q and I-Q; leading minors certify R; interval LDL certifies the full nine-dimensional negative Hessian and both positive solve matrices. Both the original nine-direction criterion and the seven-atom criterion are enclosed and their intervals overlap. Small interval pivots are saved with nonzero outward bounds in scientific notation. The two weakly connected sweep points needed interval precision retries from 1,976 to 3,952 digits; the special minimum needed 5,200 to 10,400 digits before the seven-atom enclosure succeeded. No failed enclosure is a sign certificate.

| Saved exact rational point | Interval decimal precision | Certified margin interval |
| --- | ---: | --- |
| `sweep_min` | 3952 | [0.0006251509326750882, 0.0006251509326750883] |
| `sweep_scaled_min` | 3952 | [0.0006251509326750882, 0.0006251509326750883] |
| `optimized_collar_400` | 2682 | [0.0012506038765318738, 0.0012506038765318739] |
| `optimized_scaled_400` | 2682 | [0.0012506038765318736, 0.0012506038765318737] |
| `special_mixed_min_L1000` | 10400 | [0.0002500241457294097, 0.0002500241457294098] |
| `proved_mixed_collar_L100` | 1800 | [0.0050096760480419799, 0.0050096760480419800] |

The 36 doubled-precision sweep-extremum checks agree to absolute error at most 1.1379e-103 and also agree with their saved margins within 10^(-55). The seven full cyclic determinant checks have maximum absolute discrepancy 4.4648e-102; the cyclic formula versus ambient scalar solve has maximum discrepancy 8.9296e-103. All symbolic comparison remainders are zero. The additional two optimized endpoint points were also re-evaluated at doubled precision before interval certification.

The inherited small-box interval cover was reproduced: 7 nodes, 4 accepted leaves, 0 unresolved leaves. Its domain is exactly C0033D (9), and its lower margin bound is greater than 0.02478. This is credited to C0033D, not counted as a new covered region. Data: [data/bnb_small.json](data/bnb_small.json).

| Run | Seconds | Peak RSS, MiB |
| --- | ---: | ---: |
| Exact cyclic determinant | 0.766994 | 61.6406 |
| High precision sweep | 83.4613 | 59.125 |
| Margin optimization | 174.676 | 105.297 |
| Scaled optimization | 257.835 | 104.359 |
| Mixed limit checks | 9.93060 | 63.1719 |
| Precision and interval audit | 117.733 | 113.438 |
| Inherited small cover | 0.00741621 | 57.2344 |

All runs use one numerical process at a time, one numerical thread, inherited nice 20, no worker pools and no additional language-model workers. The measured memory is far below 4 GB. Sweep and optimizer checkpoints are written atomically at intervals of 100 objective calls; the independent audit checkpoints each completed extremum or certificate. Optimizer checkpoints preserve the best point and run metadata rather than the optimizer population state.

Run `python3 reproduce.py` to regenerate the exact derivation, mixed-limit checks, precision audits, interval certificates, inherited completed cover, and tables using the saved searches. Add `--search` to regenerate the searches first. The copied C++ source is built as a macOS shared library. Python, package versions, priority and artifact hashes are saved in [artifact_manifest.json](artifact_manifest.json). The running task record is [LOG.md](LOG.md).

## 6. Coverage and the remaining problem

Theorem 1 covers exactly the cyclic family, including its spectral limit. Theorem 2 covers the entire three-parameter subset (3), in all ambient directions, with an explicit uniform remainder even when $a$ and $h$ vanish at unrelated rates. Corollary 3 gives a mixed limit with the same limiting spectrum $0,1/2,1$ as the cyclic family and a different leading scaled coefficient.

Theorem 2 does not cover unequal or complex connections, unbalanced two-point blocks, connections larger than (3), general connected paths, arbitrary real triangles, simple spectral faces with generic eigenvectors, or every intersection of spectral and graph faces. In particular, the theorem does not apply to the faster connections in C0033D (16), which are tested numerically here. It supplies no justification for removing all boundary collars.

The inherited interval box in C0033D (9), reproduced locally by [bnb.py](bnb.py), is a completed compact cover of that box alone. Point certificates in this report certify individual rounded kernels. Neither these points nor that box cover a compact remainder of the full domain. No complete interval cover is claimed, and no positive tolerance is used to classify an unresolved cell as proved.

A proof of three-point concavity still requires a scaled bound near all remaining boundary types and a certified cover of the resulting compact remainder, or a direct proof of the connected scalar inequality. A numerical value tending to zero in the families above is not a violation. No certified negative margin, positive ambient Hessian direction, or nonconcave entropy segment is produced.

Task: “Open problem C0033, fifth attempt: the mixed spectral/graph boundary of inequality (21) on three points” — received 14 November 2026, approximately 03:48, Asia/Tbilisi.
