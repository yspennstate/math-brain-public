PARTIAL

# Entropy concavity for determinantal measures: three points and rank two

Let $H(Q)=\operatorname{Ent}(P_Q)$, with natural logarithms. All matrices below are complex Hermitian; the assertions therefore include real symmetric matrices.

The following statements are proved.

1. **One row and column in any dimension.** Fix a principal submatrix $C$ of order $n-1$. On its entire feasible domain, the function
   \[
   (a,v)\longmapsto H\!\begin{pmatrix}a&v^*\\v&C\end{pmatrix}
   \tag{1}
   \]
   is jointly concave. Thus concavity holds along every direction supported on one row and its matching column, including changes connecting that coordinate to arbitrarily many others. These directions have rank at most two.
2. **Indefinite rank two on three points.** If $n=3$ and $A=aa^*-bb^*$, then $t\mapsto H(Q+tA)$ is concave on every interval where $0\le Q+tA\le I$. In particular, all indefinite rank-two directions are covered. The result also holds in any dimension for such a direction supported on three coordinate indices.
3. **Three-point Hessian reduction.** At every strict three-point contraction, the Hessian is a negative Fisher quadratic form plus $2\operatorname{tr}(\operatorname{adj}(A)R_Q)$, with an explicit $R_Q\succeq0$. It has at most one positive eigenvalue. When $R_Q>0$, its negative semidefiniteness is equivalent to the scalar inequality (17) below.
4. **A local interval certificate.** Outward-rounded interval arithmetic certifies strict concavity on the full nine-dimensional box specified in Section 6, containing kernels with nonreal entries. This is a local certificate, not a cover of the three-point domain.

No entropy counterexample was found. Full concavity on three points, arbitrary rank-two directions in higher dimensions, rank-two semidefinite directions, and arbitrary commuting segments remain unresolved in this report. In particular, a matrix of rank two need not have the form $aa^*-bb^*$: a positive semidefinite matrix of rank two is excluded from that form.

The previous attempt [C0033A/REPORT.md](../C0033A/REPORT.md) proves the full two-point theorem, conditional lifting for changes on a fixed coordinate block, and the Hessian and fourth variation at product kernels. Those results are used with attribution, not counted as new results here. Numerical enumeration and Hessian routines were copied from [C0033A/dpp.py](../C0033A/dpp.py) and [C0033A/dpp.cpp](../C0033A/dpp.cpp) into [dpp.py](dpp.py) and [dpp.cpp](dpp.cpp).

## 1. Identities and standard facts

For $S\subseteq E$, put $D_{S^c}=\operatorname{diag}(\mathbf1_{i\notin S})$, $B_S=Q-D_{S^c}$, and
\[
p_S=(-1)^{n-|S|}\det B_S.
\tag{2}
\]
If $0<Q<I$, every $p_S$ is positive. For example, with $L=Q(I-Q)^{-1}>0$,
\[
p_S=\det L_{S,S}/\det(I+L)>0.
\]
For a fixed Hermitian direction $A$, all derivatives in this report are derivatives along $Q+tA$. Jacobi's formula and normalization give
\[
H''=-\sum_S\frac{(p'_S)^2}{p_S}-\sum_Sp''_S\log p_S.
\tag{3}
\]
In particular, the first term is nonpositive. For rank-one $A$, each determinant in (2) is affine, so $p''_S=0$. This is the mechanism of Gu's Theorem 7.

Two standard finite DPP facts will be used, with their precise roles stated here.

**Conditioning.** Given an exact pattern $T\subseteq C$, the conditional kernel on $B=E\setminus C$ is
\[
Q_{BB}-Q_{BC}(Q_{CC}-D_{C\setminus T})^{-1}Q_{CB}.
\tag{4}
\]
This follows by taking the Schur complement in the inclusion-and-exclusion determinant for the joint event. It is a positive contraction because its principal minors and those of its complement are conditional inclusion and avoidance probabilities. In the strict case it is a strict contraction: its determinant and its complementary determinant are positive conditional atom probabilities. Consequently, after arbitrary coordinate conditioning, two remaining occupation indicators have covariance $-|K_{ij}|^2\le0$.

**Stochastic domination.** If $0\le C_0\le C_1\le I$, then $P_{C_0}\preceq P_{C_1}$: the expectation of each increasing function on subsets increases. The version without a commutation assumption is [Borcea–Brändén–Liggett, Theorem 4.13](https://arxiv.org/pdf/0707.2340). The distinction matters: Lyons's original Theorem 8.1 stated a commuting assumption. His [errata](https://rdlyons.pages.iu.edu/errata/bases.pdf) also explain its removal by a simultaneous projection dilation. Explicitly, the isometry
\[
x\longmapsto(C_0^{1/2}x,(C_1-C_0)^{1/2}x,(I-C_1)^{1/2}x)
\]
dilates $C_0,C_1$ to two nested projections; projection stochastic domination and restriction give the stated finite result. No entropy concavity assumption enters this fact.

## 2. Concavity when one row and column vary

**Theorem 2.1.** For fixed $C$, (1) is concave on
\[
\mathcal D_C=\{(a,v):0\le\begin{pmatrix}a&v^*\\v&C\end{pmatrix}\le I\}.
\]

**Proof.** First suppose the full kernel is a strict contraction. Write $F=E\setminus\{0\}$. For $T\subseteq F$, define
\[
M_T=C-D_{F\setminus T},\quad
\pi_T=P_C[X=T],\quad
r_T=a-v^*M_T^{-1}v.
\tag{5}
\]
All $M_T$ are invertible, $\pi_T>0$, and $0<r_T<1$. Formula (4) identifies $r_T$ with the conditional probability that coordinate $0$ is occupied. With $h(r)=-r\log r-(1-r)\log(1-r)$, the entropy chain rule gives
\[
H(Q)=H(C)+\sum_{T\subseteq F}\pi_T h(r_T).
\tag{6}
\]

The function $T\mapsto r_T$ is decreasing. To verify one Boolean-lattice edge, fix all coordinates of $F\setminus\{j\}$. The conditional process on $\{0,j\}$ has a strict kernel
\[
K=\begin{pmatrix}\alpha&z\\\overline z&\beta\end{pmatrix}.
\]
Its two conditional probabilities for coordinate $0$ are
\[
P(0\in X\mid j\in X)=\alpha-|z|^2/\beta,
\quad
P(0\in X\mid j\notin X)=\alpha+|z|^2/(1-\beta).
\]
The second minus the first is $|z|^2/[\beta(1-\beta)]\ge0$. All comparable subsets are connected by such edges. Since $h'(r)=\log((1-r)/r)$ is decreasing, the function
\[
f(T)=h'(r_T)
\]
is increasing.

For an arbitrary $w\in\mathbb C^F$, $C+sww^*$ is a positive contraction for sufficiently small $s\ge0$. Stochastic domination, applied to the fixed function $f$, implies
\[
0\le\left.\frac{d}{ds}\right|_{s=0+}E_{P_{C+sww^*}}f
 =\sum_T\pi_T h'(r_T)w^*M_T^{-1}w.
\tag{7}
\]
The derivative equality follows directly from (2). Thus the Hermitian matrix
\[
G_Q:=\sum_T\pi_T h'(r_T)M_T^{-1}
\tag{8}
\]
is positive semidefinite. The argument does not differentiate $f$; it holds $f$ at the original kernel while differentiating the complement law.

Along $a(t)=a+t\alpha, v(t)=v+tw$, the coefficients $\pi_T$ are constant and
\[
r'_T=\alpha-2\operatorname{Re}(w^*M_T^{-1}v),\qquad
r''_T=-2w^*M_T^{-1}w.
\]
Twice differentiating (6) yields the certificate
\[
\boxed{
H''=-\sum_T\pi_T\frac{[\alpha-2\operatorname{Re}(w^*M_T^{-1}v)]^2}{r_T(1-r_T)}-2w^*G_Qw\le0.}
\tag{9}
\]
The strict feasible domain is convex, so this proves its concavity.

For arbitrary boundary endpoints, apply the result to $Q_j^\varepsilon=(1-2\varepsilon)Q_j+\varepsilon I$, $0<\varepsilon<1/2$. Their complementary blocks are still equal. Every atom is polynomial in the kernel entries, and $-p\log p$ is continuous at zero. Letting $\varepsilon\downarrow0$ proves the assertion on the closed domain. $\square$

A direction in this theorem has the form
\[
A=\begin{pmatrix}\alpha&w^*\\w&0\end{pmatrix}.
\]
When $w\ne0$, its two nonzero eigenvalues are
\[
\frac{\alpha\pm\sqrt{\alpha^2+4\|w\|^2}}2,
\]
so it is an indefinite rank-two direction. Its support may involve every coordinate. The theorem therefore extends beyond changes confined to a two-coordinate principal block.

## 3. A positive matrix certificate on three points

For $n=3$, abbreviate exact atom probabilities by $p_0,p_1,p_2,p_3,p_{12},p_{13},p_{23},p_{123}$, with $p_0=p_\varnothing$. For $\{i,j,k\}=\{1,2,3\}$, set
\[
\ell_{ij}^{0}=\log\frac{p_i p_j}{p_0p_{ij}},\qquad
\ell_{ij}^{1}=\log\frac{p_{ik}p_{jk}}{p_kp_{123}}.
\tag{10}
\]
These are nonnegative. Indeed, the two-point conditional law given $X_k=0$, or given $X_k=1$, is determinantal. For any two-point determinantal law with empty, singleton and double probabilities $w,x,y,z$, respectively, $xy-wz=|K_{ij}|^2\ge0$. Normalizing a conditional law cancels from the ratios in (10).

The quantity
\[
\gamma=\log\frac{p_{123}p_1p_2p_3}{p_0p_{12}p_{13}p_{23}}
       =\ell_{ij}^{0}-\ell_{ij}^{1}
\tag{11}
\]
does not depend on the chosen pair. Define
\[
D_0=\operatorname{diag}(\ell_{23}^{0},\ell_{13}^{0},\ell_{12}^{0}),\qquad
R_Q=D_0-\gamma Q.
\tag{12}
\]

**Lemma 3.1.** For every strict three-point contraction, $R_Q\succeq0$.

**Proof.** If $\gamma\le0$, then $R_Q=D_0+(-\gamma)Q\succeq0$. If $\gamma\ge0$, let $D_1=\operatorname{diag}(\ell_{23}^{1},\ell_{13}^{1},\ell_{12}^{1})$. Equations (10)–(11) give
\[
R_Q=D_1+\gamma(I-Q)\succeq0.
\]
These two cases exhaust the possibilities. $\square$

**Proposition 3.2.** For every Hermitian $3\times3$ direction $A$,
\[
\boxed{D^2H(Q)[A,A]=-\sum_S\frac{(p'_S)^2}{p_S}
                   +2\operatorname{tr}(\operatorname{adj}(A)R_Q).}
\tag{13}
\]
Here $\operatorname{adj}(A)$ is the classical adjugate, defined also for singular matrices.

**Proof.** Freeze the values $f(S)=\log p_S$ at the base kernel. Expand the set function in its unique Boolean Möbius expansion
\[
f(S)=f(\varnothing)+\sum_i m_i\mathbf1_{i\in S}
 +\sum_{i<j}m_{ij}\mathbf1_{\{i,j\}\subseteq S}
 +\gamma\mathbf1_{\{1,2,3\}\subseteq S}.
\]
The pair coefficients are $m_{ij}=-\ell_{ij}^{0}$, and the triple coefficient is (11). Consequently, for an arbitrary kernel $K$,
\[
E_{P_K}f=f(\varnothing)+\sum_i m_iK_{ii}
 +\sum_{i<j}m_{ij}\det K_{ij,ij}+\gamma\det K.
\tag{14}
\]
For $K=Q+tA$, the second derivative of a pair determinant is $2\det A_{ij,ij}$. The coefficient of $t^2$ in the three-point determinant is $\operatorname{tr}(Q\operatorname{adj}(A))$, by the cubic determinant expansion. Moreover, the diagonal entries of $\operatorname{adj}(A)$ are the complementary pair determinants. Differentiating (14) twice gives
\[
\sum_Sp''_S\log p_S
 =2\operatorname{tr}\!\left(\operatorname{adj}(A)
       [-D_0+\gamma Q]\right)
 =-2\operatorname{tr}(\operatorname{adj}(A)R_Q).
\tag{15}
\]
Substitution in (3) proves (13). No change of the coordinate basis of the DPP has been made. $\square$

**Theorem 3.3.** If $A=aa^*-bb^*$ has order three, then $H(Q+tA)$ is concave on its full feasible interval.

**Proof.** If $A$ has rank at most one, its adjugate is zero, so (13) proves the claim in the interior. Otherwise, $A$ has one positive and one negative eigenvalue and a zero eigenvalue. Its adjugate has eigenvalues $0,0,\lambda_+\lambda_-$, and is therefore negative semidefinite. Lemma 3.1 implies
\[
\operatorname{tr}(\operatorname{adj}(A)R_Q)\le0.
\]
Both terms in (13) are nonpositive. Integrating the Hessian inequality along an interior segment proves concavity there; the common regularization used in Theorem 2.1 proves the boundary cases. $\square$

**Corollary 3.4.** In any dimension, concavity holds along an indefinite rank-two direction supported on three coordinate indices.

**Proof.** Let $B$ consist of those three indices and $C=E\setminus B$. Along the segment, $Q_{CC}$ and $Q_{BC}$ are fixed. Each complement-pattern probability $\pi_T$ is fixed, and (4) is an affine three-point kernel with the same direction $A_{BB}$. Thus
\[
H(Q(t))=H(Q_{CC})+\sum_T\pi_TH(K_T(t))
\]
is concave by Theorem 3.3. Regularization handles the boundary. This is the conditional lifting argument of C0033A, applied to the new directional theorem. $\square$

At a real symmetric three-point kernel, the Hessian splits into its real symmetric and purely imaginary Hermitian subspaces: conjugation changes the sign of the latter variables and fixes the former. A purely imaginary Hermitian $3\times3$ matrix is $i$ times a real skew-symmetric matrix and has eigenvalues $0,\lambda,-\lambda$. Theorem 3.3 therefore proves the entire imaginary block is negative semidefinite. It does not settle the remaining real block or mixed directions at a nonreal kernel.

## 4. What remains in the three-point Hessian

**Proposition 4.1.** The three-point entropy Hessian has at most one positive eigenvalue. Suppose $R_Q>0$, let $d=\det R_Q$, and let $E_1,\ldots,E_9$ be a Frobenius-orthonormal real basis of Hermitian matrices. Define
\[
\begin{aligned}
F_{\alpha\beta}&=\sum_S\frac{Dp_S[E_\alpha]Dp_S[E_\beta]}{p_S},\\
J_{\alpha\beta}&=F_{\alpha\beta}
 +d\operatorname{tr}(R_Q^{-1}E_\alpha R_Q^{-1}E_\beta),\\
z_\alpha&=\operatorname{tr}(R_Q^{-1}E_\alpha).
\end{aligned}
\tag{16}
\]
Then $J>0$, and full concavity at $Q$ is equivalent to
\[
\boxed{d\,z^{\mathsf T}J^{-1}z\le1.}
\tag{17}
\]

**Proof.** Write $A=R_Q^{1/2}XR_Q^{1/2}$. The adjugate congruence identity gives
\[
2\operatorname{tr}(\operatorname{adj}(A)R_Q)
 =d\{(\operatorname{tr}X)^2-\operatorname{tr}(X^2)\}.
\tag{18}
\]
For invertible $X$ this follows from the inverse formula for the adjugate, and polynomial continuity proves the singular case. The form in braces has one positive direction, the scalar matrices, and is negative definite on traceless Hermitian matrices. Subtracting the nonnegative Fisher form cannot increase its positive index. If $R_Q$ is singular, approximate it by $R_Q+\varepsilon I$ in (13); the bound of one on the positive index passes to the limit.

For $R_Q>0$, the second term defining $J$ is positive definite. Equations (13), (16) and (18) give the Hessian matrix $dzz^{\mathsf T}-J$. Congruence by $J^{-1/2}$ shows it is negative semidefinite exactly when $d\|J^{-1/2}z\|^2\le1$, proving (17). $\square$

The scalar inequality (17) has not been proved globally. It must also be supplemented by an analysis of the singular $R_Q$ strata. Merely knowing the correction matrix $R_Q\succeq0$ does not prove (17), because $\operatorname{adj}(A)$ can have positive eigenvalues.

For completeness, there is a useful monotonicity identity in the invariant coordinates from C0033A. Write
\[
Q=\begin{pmatrix}a&x&y\\\overline x&b&z\\\overline y&\overline z&c\end{pmatrix},
\quad u=|x|^2,\ v=|y|^2,\ w=|z|^2,
\quad\rho=2\operatorname{Re}(xz\overline y).
\]
At fixed $a,b,c$, all atom probabilities are affine in $u,v,w,\rho$, so entropy is concave as a function of these four formal variables wherever the atoms are positive. At a realizable strict kernel,
\[
\frac{\partial H}{\partial u}
 =-(1-c)\ell_{12}^{0}-c\ell_{12}^{1}\le0,
\qquad \frac{\partial H}{\partial\rho}=-\gamma,
\tag{19}
\]
with analogous formulas for $v,w$. To verify (19), differentiate the inclusion determinants in (14): $\partial_u\det Q_{12}=-1$, $\partial_u\det Q=-c$, and $\partial_\rho\det Q=1$. This yields $\partial_uH=m_{12}+c\gamma$ and $\partial_\rho H=-\gamma$, which are the displayed expressions. The cubic triangle term prevents direct use of ordinary concave composition to settle the full kernel problem.

## 5. General rank two and commuting kernels

Let $wedge^2 M$ denote the second compound matrix in the coordinate-pair basis. For a strict kernel of arbitrary order define the Hermitian matrix
\[
\mathcal R_Q=-\sum_Sp_S\log p_S\;\wedge^2(B_S^{-1}).
\tag{20}
\]
The trace identity $2\operatorname{tr}(\wedge^2 M)=(\operatorname{tr}M)^2-\operatorname{tr}(M^2)$, and multiplicativity of compound matrices, give the exact general formula
\[
D^2H(Q)[A,A]=-\sum_S\frac{(p'_S)^2}{p_S}
       +2\operatorname{tr}(\mathcal R_Q\wedge^2 A).
\tag{21}
\]
If $A$ has eigenvalues $\lambda_+>0>\lambda_-$ and otherwise zero, then $wedge^2 A=-\kappa uu^*$, where $\kappa=-\lambda_+\lambda_->0$ and $u$ is a unit decomposable bivector. Thus nonnegativity of $\langle u,\mathcal R_Qu\rangle$ on all decomposable bivectors would suffice to prove all indefinite rank-two directions. It is sufficient, not asserted necessary: the Fisher term in (21) can compensate a negative value.

The stronger assertion $\mathcal R_Q\succeq0$ is false. Section 7 gives strict kernels of orders five, six and eight and 110/160-digit negative Rayleigh quotients. Their testing vectors are not decomposable. An additional outward-rounded interval proof at order five is given by [wedge_interval.py](wedge_interval.py) and [data/wedge_interval_n5.json](data/wedge_interval_n5.json): interval LDL certifies both $Q>0$ and $I-Q>0$, all 32 atoms have positive lower bounds, and the exterior Rayleigh quotient has a strictly negative upper bound. A nonzero interval Plücker relation certifies that the vector is not decomposable. These are counterexamples to that proposed matrix certificate, not counterexamples to entropy concavity. No extension of Gu's rank-one proof to every general rank-two direction is claimed.

There is also an exact simplification for commuting three-point kernels.

**Proposition 5.1.** Fix a $3\times3$ unitary $U$. There is a probability distribution $c_\pi$ on coordinate permutations, depending only on $U$, such that for every $\lambda\in[0,1]^3$,
\[
P_{U\operatorname{diag}(\lambda)U^*}
 =\sum_{\pi\in S_3}c_\pi\;\pi_*P_{\operatorname{diag}(\lambda)}.
\tag{22}
\]

**Proof.** Choose the eigenmodes independently with occupation parameters $\lambda_j$. Conditional on the chosen set $J$, the process is the projection DPP onto the columns $U_J$; it has probability $|\det U_{S,J}|^2$ at a set $S$ of size (|J|). This spectral mixture identity follows from Cauchy–Binet applied to the inclusion determinants.

The matrix $W_{ij}=|U_{ij}|^2$ is doubly stochastic. Write $W=\sum_\pi c_\pi P_\pi$ by the Birkhoff–von Neumann theorem. The transition on singleton subsets is $W$. On two-element subsets, the cofactor identity for a unitary matrix gives
\[
|\det U_{S,J}|^2=|U_{S^c,J^c}|^2,
\]
so the same convex combination of permutations gives that transition. On the empty and full subsets both transitions are the identity. Hence the entire spectral-subset-to-coordinate-subset channel is the same fixed mixture of coordinate permutations. Applying it to the independent spectral subset proves (22). $\square$

Although the weights in (22) are fixed along a commuting segment, its input product law is not affine in $\lambda$. Ordinary entropy concavity in a probability vector therefore does not establish concavity of its composition with this channel. This reduction leaves a precise classical three-variable question; it is not a proof of the commuting assertion. Commuting segments covered here include Gu's rank-one case, the indefinite rank-two cases of Theorem 3.3 and Corollary 3.4, and the coordinate block cases proved in C0033A. Arbitrary commuting segments remain open.

## 6. Compact parametrization and a validated local box

Diagonal unitary conjugation and permutation preserve every atom and act linearly on the full Hermitian space. A three-point kernel can therefore be represented with $a\le b\le c$, $Q_{12}=x\ge0$, $Q_{13}=y\ge0$, and $Q_{23}=z+it$. Complex conjugation additionally allows $t\ge0$. Zero edges cause no difficulty: choose the phases on the nonzero edges; if an edge used for normalization vanishes its phase is unrestricted.

A compact containing box is
\[
(a,b,c)\in[0,1]^3,\quad x,y\in[0,1/2],
\quad z\in[-1/2,1/2],\quad t\in[0,1/2].
\]
The off-diagonal bound follows from $Q^2\le Q$: $|Q_{ij}|^2\le Q_{ii}(1-Q_{ii})\le1/4$. The feasible set in this box is given exactly by nonnegativity of all principal minors of $Q$ and (I-Q). Their order-three inequalities are
\[
abc-a(z^2+t^2)-by^2-cx^2+2xyz\ge0
\]
and
\[
(1-a)(1-b)(1-c)-(1-a)(z^2+t^2)-(1-b)y^2-(1-c)x^2-2xyz\ge0.
\]
Together with the order-one and order-two principal inequalities, these characterize the full compact domain. The full Hessian still has nine real variables: discarding the two phase directions from a seven-variable chart does not certify ambient concavity.

The executable interval certificate [interval3.py](interval3.py) uses those nine variables, in the order
\[
(q_{11},q_{22},q_{33},\Re q_{12},\Im q_{12},\Re q_{13},\Im q_{13},\Re q_{23},\Im q_{23}).
\]
The center is
\[
(2/5,1/2,3/5,1/16,0,1/20,0,1/24,1/32).
\tag{23}
\]
The radius and rational outward bounds for all pivots are recorded below and in [data/interval3.json](data/interval3.json). Interval Gershgorin bounds verify $0<Q<I$ throughout the box. Each probability and each first and second derivative is evaluated as an explicit polynomial. The negative Hessian is then evaluated by
\[
(-\nabla^2H)_{ij}=\sum_S\left(\frac{\partial_i p_S\partial_jp_S}{p_S}
                         +\log(p_S)\partial_{ij}p_S\right).
\tag{24}
\]
An interval $LDL^{\mathsf T}$ elimination produces strictly positive lower bounds for every pivot. Induction on the elimination steps proves that the negative Hessian is positive definite at every point of the box. All interval operations, including logarithms, use 60-decimal-place `mpmath.iv` outward rounding. Saved endpoint bounds are rounded outward to rational multiples of $10^{-20}$. The executable assertions and rational input data specify the certificate completely. No assertion is made that these boxes cover the remaining compact domain or its singular boundary.

## 7. Reproducible numerical evidence

To rebuild the library and rerun the validated certificates and high-precision audits, run:

```sh
python3 reproduce.py audit
```

To regenerate all search data first, run `python3 reproduce.py searches`, followed by the audit command. `python3 sources_manifest.py` fetches the five source PDFs. The scripts require NumPy, SciPy, SymPy and mpmath; exact versions and artifact hashes are saved in [artifact_manifest.json](artifact_manifest.json). All commands run sequentially.

The following tables are generated from the saved JSON by [make_tables.py](make_tables.py). Every entropy and derivative enumerates all $2^n$ atoms. This is exhaustive enumeration of subsets, not a search over all kernels. Search arithmetic is binary floating point; the reported high-precision checks evaluate the decimal-entry matrices saved in the witness files.

All computations use one numerical process at a time, one BLAS thread, and no model helpers or worker pools. HiGHS is explicitly configured for one thread in the final LP runs. Process priority was inherited as nice 10. Peak resident memory is recorded in the tables and is far below 4 GB.

The three-point search [explore3.py](explore3.py), seed 330033, includes uniform, near-projection and extreme spectra, and diluted off-diagonal entries. It also maximizes the largest Hessian eigenvalue divided by the squared off-diagonal Frobenius norm, to reduce attraction to product kernels. Four saved near-zero witnesses are checked at 110 and 160 digits by [verify_mp.py](verify_mp.py). An independent permutation expansion computes polynomial coefficients of inclusion determinants, converts them to atom coefficients by Möbius inversion, and evaluates (3) without inverses or Jacobi's identity. The final decoder symmetrizes its output exactly in binary arithmetic; an earlier decoder had conjugate entries differing by roundoff, discovered by the independent audit and corrected before the final run.

[verify_certificates.py](verify_certificates.py), seed 33350, independently compares (9) and (13) with the inherited curvature implementation, verifies the conditional entropy chain rule, evaluates negative exterior Rayleigh quotients at 110 and 160 digits, and checks optimized commuting witnesses at both precisions. The latter witnesses commute to binary precision; the stated decimal-entry high-precision tests certify their curvature but do not upgrade that approximate commutation to an exact mathematical identity.

[ranktwo_probe.py](ranktwo_probe.py), seed 33320, tests 4,000 indefinite rank-two directions and records the nonlinear logarithmic term separately. [commuting_search.py](commuting_search.py), seed 33330, computes the entire Hessian on each fixed simultaneous eigenbasis, rather than sampling just one spectral direction; its optimization includes Haar real, Haar complex and Fourier eigenbases. [wedge_probe.py](wedge_probe.py), seed 33340, computes the full matrix (20). [decomposable_search.py](decomposable_search.py), seed 33341, optimizes its Rayleigh quotient on decomposable bivectors at the three failed-PSD witnesses. These last optimizations are local and do not certify a global minimum.

[submodular_probe.py](submodular_probe.py), seed 33321, and [submod_boundary.py](submod_boundary.py), seed 33322, test a stronger possible route: whether the determinantal expectation of every submodular set function has the appropriate mixed derivative sign in two positive rank-one directions. The LP imposes every elementary submodularity inequality and bounds function values by one in absolute value. No violation was found in these finite tests, including projection boundary tests through order eight. This is an unproved auxiliary statement, not an ingredient of any theorem above.

<!-- TABLES_START -->

Three-point full Hessians and normalized optimization ([data/explore3.json](data/explore3.json)):


| Family | Kernels / restarts | Optimization evaluations | Largest score |
| --- | --- | --- | --- |
| three_False | 6000 | — | 5.650908e-16 |
| three_True | 6000 | — | -5.158521e-16 |
| normalized_three_False | 8 | 3523 | 3.750925e-13 |
| normalized_three_True | 8 | 7769 | 1.949277e-13 |


For the normalized rows, the score is the largest Hessian eigenvalue divided by the squared off-diagonal norm. Tiny positive binary scores are not counterexamples.


Saved three-point directions, independent high-precision audit ([data/three_point_mp.json](data/three_point_mp.json)):


| Witness | 160-digit curvature | Independent absolute discrepancy |
| --- | --- | --- |
| three_False | -7.57259283945e-16 | 5.334621e-161 |
| three_True | -4.42822449502e-16 | 3.556414e-161 |
| normalized_three_False | -1.45069258494e-15 | 1.778207e-161 |
| normalized_three_True | -1.6204883367e-16 | 1.4225656e-160 |


General indefinite rank-two tests ([data/ranktwo_probe.json](data/ranktwo_probe.json)). The logarithmic term is \(\sum_Sp_S^{\prime\prime}\log p_S\):


| n | Trials | Smallest logarithmic term | Largest entropy curvature |
| --- | --- | --- | --- |
| 3 | 1000 | 3.531397e-05 | -0.1569934 |
| 4 | 1000 | 0.0001285909 | -0.3117102 |
| 5 | 1000 | 0.001736617 | -0.3925273 |
| 6 | 1000 | 0.005318704 | -0.2430517 |


Commuting Hessians ([data/commuting_search.json](data/commuting_search.json)):


| n | Field / family | Kernels / evaluations | Largest curvature |
| --- | --- | --- | --- |
| 3 | real | 600 | -0.0005014125 |
| 3 | complex | 600 | -5.805286e-05 |
| 4 | real | 600 | -4.985301e-05 |
| 4 | complex | 600 | -3.441433e-05 |
| 5 | real | 600 | -8.217443e-08 |
| 5 | complex | 600 | -1.81179e-05 |
| 6 | real | 600 | -2.671547e-06 |
| 6 | complex | 600 | -1.429689e-06 |
| 8 | real | 150 | -9.028411e-05 |
| 8 | complex | 150 | -1.107301e-06 |
| 3 | mixed / optimized | 825 | 1.809207e-15 |
| 4 | mixed / optimized | 1323 | 2.211803e-15 |
| 6 | mixed / optimized | 4035 | 8.179528e-15 |


Optimized commuting directions, high-precision check ([data/certificate_audit.json](data/certificate_audit.json)):


| n | Binary commutator norm | 160-digit curvature |
| --- | --- | --- |
| 3 | 8.606302e-18 | -1.71849641528e-16 |
| 4 | 8.673617e-19 | -5.56272422133e-16 |
| 6 | 3.079703e-17 | -3.77037933099e-16 |


The exterior matrix (20): negative eigenvalues disprove its proposed global PSD extension, not entropy concavity ([data/wedge_probe.json](data/wedge_probe.json)):


| n | Kernels | Smallest observed eigenvalue |
| --- | --- | --- |
| 3 | 1000 | 0.000362314 |
| 4 | 1000 | 2.224348e-05 |
| 5 | 1000 | -0.02581933 |
| 6 | 1000 | -0.02853182 |
| 8 | 200 | -0.01874926 |


High-precision negative Rayleigh quotients, each using the saved vector with its exact decimal entries. A nonzero Plücker relation certifies that it is not decomposable:


| n | 110-digit evaluation | 160-digit evaluation | Absolute Plücker relation |
| --- | --- | --- | --- |
| 5 | -0.02581933223143933 | -0.02581933223143933 | 0.19490736 |
| 6 | -0.02853182004080286 | -0.02853182004080286 | 0.037872591 |
| 8 | -0.01874926039474629 | -0.01874926039474629 | 0.025384087 |


Local decomposable-vector optimization at those same kernels ([data/decomposable_search.json](data/decomposable_search.json)):


| n | Starts | Smallest located decomposable value | Corresponding entropy curvature |
| --- | --- | --- | --- |
| 5 | 15 | 0.2319244 | -3986.01 |
| 6 | 15 | 0.2077937 | -1847.618 |
| 8 | 15 | 0.1197574 | -90977.11 |


Interval certificate: radius **1/10000 in each of the nine coordinates** about (23). The pivot bounds below are shortened outward to six decimal places; full rational bounds are saved in [data/interval3.json](data/interval3.json).


| LDL pivot | Lower bound | Upper bound |
| --- | --- | --- |
| 1 | 4.150446 | 4.186617 |
| 2 | 3.983769 | 4.019237 |
| 3 | 4.146870 | 4.188446 |
| 4 | 0.365172 | 0.420211 |
| 5 | 0.107138 | 0.156440 |
| 6 | 0.232842 | 0.292472 |
| 7 | 0.061598 | 0.116145 |
| 8 | 0.177864 | 0.239660 |
| 9 | 0.062327 | 0.164771 |


Independent identity checks:


| Identity | Cases | Maximum absolute error |
| --- | --- | --- |
| Three-point formula (13) | 300 | 1.705303e-13 |
| One-row formula (9), n=3 | 100 | 5.684342e-14 |
| One-row formula (9), n=4 | 100 | 3.907985e-14 |
| One-row formula (9), n=5 | 100 | 5.684342e-14 |
| One-row formula (9), n=6 | 100 | 5.684342e-14 |


The largest recorded peak RSS among these principal runs was **127.94 MiB**. The interval run uses only 8 atom polynomials and a 9 by 9 interval matrix. Auxiliary LP data are [data/submodular_probe.json](data/submodular_probe.json) and [data/submod_boundary.json](data/submod_boundary.json); no violations exceeded the binary numerical scale (about \(10^{-14}\)).

<!-- TABLES_END -->

## 8. Sources and remaining questions

The requested papers were fetched anew and saved with extracted text and SHA-256 hashes in [sources/manifest.json](sources/manifest.json).

- [Lyons, *Determinantal probability measures* (2003)](https://www.numdam.org/item/10.1007/s10240-003-0016-0.pdf): the finite entropy conjecture is Conjecture 9.2, in Section 9. Section 5 concerns measures on bases. The entropy-rate Conjecture 5.3 appears in the [2014 survey](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf).
- [Gu, *Entropy of Determinantal Point Processes*](https://sevenkplus.com/data/dpp.pdf): Theorem 7 proves rank-one concavity; Corollary 6 proves $H(tQ)\ge tH(Q)$. The latter endpoint inequality does not, by itself, prove full concavity on a ray. The report is an unrefereed course project.
- [Borcea–Brändén–Liggett, *Negative dependence and the geometry of polynomials* (2009)](https://arxiv.org/pdf/0707.2340), Theorem 4.13, and [Lyons's errata](https://rdlyons.pages.iu.edu/errata/bases.pdf): stochastic domination in Loewner order without a commuting assumption. This known theorem is used in Theorem 2.1.

What remains open in this attempt is explicit:

1. The full three-point conjecture, for real symmetric and complex Hermitian kernels. The positive matrix (12), the scalar criterion (17), and the compact chart do not establish a global Hessian sign.
2. General indefinite rank-two directions in arbitrary dimension, beyond one-row changes and directions supported on three coordinates. The exterior matrix need not be positive semidefinite; positivity on decomposable bivectors, or a sufficient Fisher compensation inequality in (21), has not been proved.
3. Rank-two positive or negative semidefinite directions beyond the inherited coordinate-supported cases. These are not included in $aa^*-bb^*$ with two nonzero eigenvalues.
4. Arbitrary commuting kernels, including general simultaneous eigenvalue changes already on three points. Formula (22) supplies a classical reduction, not a concavity theorem for that nonlinear input family.

No statement here resolves stationary entropy-rate concavity.

Task: “Open problem C0033: concavity of the entropy of determinantal measures in the kernel” — received 13 November 2026, approximately 02:13, Asia/Tbilisi.
