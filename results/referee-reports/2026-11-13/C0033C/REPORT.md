PARTIAL

# Determinantal entropy on three points and along rank-two directions

Let \(P_Q\) be the determinantal measure with Hermitian marginal kernel \(0\le Q\le I\), and let \(H(Q)=-\sum_S P_Q(S)\log P_Q(S)\), with natural logarithms.

The following results are proved.

**Theorem A (the singular three-point certificate).** Let \(0<Q<I\) have order three, and let \(R_Q\) be the matrix in C0033B, equation (12). Then \(R_Q\) is singular if and only if the graph with edges \(ij\) for \(Q_{ij}\ne0\) is disconnected. On this stratum the entropy Hessian is negative semidefinite in every ambient Hermitian direction. The possible ranks of \(R_Q\) are zero, one and three: rank zero corresponds to diagonal kernels, rank one to a nontrivial two-point block and an isolated coordinate, and rank three to connected kernels.

**Theorem B (a coordinate direction and a rank-one update).** Fix any Hermitian matrix \(Q_0\), a coordinate vector \(e_i\), and a vector \(b\). The function
\[
(s,t)\longmapsto H(Q_0+s e_i e_i^*+tbb^*)
\]
is jointly concave on its feasible set of positive contractions. This holds in every finite dimension. Consequently, entropy is concave along every Hermitian rank-two direction whose range contains a coordinate vector, including positive and negative semidefinite directions. The directions supported on one row and column are also included, by C0033B.

For \(A=\alpha e_i e_i^*+bb^*\), \(\alpha\ge0\), the proof gives the quantitative interior estimate
\[
D^2H(Q)[A,A]\le-4\alpha^2. 
\tag{1}
\]

These statements do **not** prove inequality (17) of C0033B on the connected strict three-point domain. General positive semidefinite rank-two directions on three points, and general rank-two directions in higher dimensions, remain unresolved. No entropy counterexample is established. In particular, a theorem asserting full three-point concavity is not claimed.

The two-point concavity theorem, conditional lifting, and the block/product-kernel Hessian theorem are taken from [C0033A/REPORT.md](../C0033A/REPORT.md). Joint concavity in one row and column, the positive matrix \(R_Q\), indefinite rank-two concavity on three points, and the scalar criterion (17) are taken from [C0033B/REPORT.md](../C0033B/REPORT.md). Their proofs are not repeated. The files [dpp.py](dpp.py) and [dpp.cpp](dpp.cpp) are verbatim copies from C0033B. The new assertions are Theorems A and B, their proofs below, and the conditional rank-two formula in Proposition C.

## 1. The singular stratum of \(R_Q\)

Use the notation of C0033B. For \(\{i,j,k\}=\{1,2,3\}\), write
\[
\ell_{ij}^0=\log\frac{p_i p_j}{p_0p_{ij}},\qquad
\ell_{ij}^1=\log\frac{p_{ik}p_{jk}}{p_kp_{123}},\qquad
\gamma=\ell_{ij}^0-\ell_{ij}^1.
\]
All atoms are positive at a strict contraction, and the two conditional log odds are nonnegative. Set
\[
D_0=\operatorname{diag}(\ell_{23}^0,\ell_{13}^0,\ell_{12}^0),\qquad
D_1=\operatorname{diag}(\ell_{23}^1,\ell_{13}^1,\ell_{12}^1).
\]
C0033B proves
\[
R_Q=D_0-\gamma Q=D_1+\gamma(I-Q)\succeq0,
\tag{2}
\]
and the identity
\[
D^2H(Q)[A,A]=-\sum_S\frac{Dp_S[A]^2}{p_S}
             +2\operatorname{tr}(\operatorname{adj}(A)R_Q).
\tag{3}
\]

**Proof of Theorem A.** If \(\gamma<0\), the representation \(R_Q=D_0+|\gamma|Q\) makes \(R_Q\) positive definite. If \(\gamma>0\), use \(R_Q=D_1+\gamma(I-Q)\) instead. Therefore singularity requires \(\gamma=0\). In that case \(R_Q=D_0\); singularity means that \(\ell_{ij}^0=0\) for at least one pair. Since \(\gamma=0\), also \(\ell_{ij}^1=0\).

For a two-point determinantal law with kernel \(K\), its four atom probabilities \(w,x,y,z\) satisfy \(xy-wz=|K_{ij}|^2\). Consequently zero conditional log odds are equivalent to a zero conditional off-diagonal kernel entry. The two conditional entries in the present setting are
\[
Q_{ij}+\frac{Q_{ik}Q_{kj}}{1-Q_{kk}},\qquad
Q_{ij}-\frac{Q_{ik}Q_{kj}}{Q_{kk}}.
\tag{4}
\]
Both vanish. Subtracting them, and using \(0<Q_{kk}<1\), gives \(Q_{ik}Q_{kj}=0\), and then \(Q_{ij}=0\). At least two edges are absent, so the three-point graph is disconnected.

Conversely, if the graph is disconnected, a coordinate permutation writes \(Q=C\oplus(c)\), with \(C\) of order two. The corresponding law is the product of its two block laws. The log odds between the isolated coordinate and either other coordinate are zero, and the log odds inside \(C\) do not depend on the isolated coordinate's occupation. Thus \(\gamma=0\), and \(R_Q\) has only one potentially nonzero diagonal entry. That entry is positive exactly when the off-diagonal entry of \(C\) is nonzero. This proves the classification of the ranks and the equivalence in the statement.

Finally, C0033A, Proposition 4.1, gives, for every ambient Hermitian direction \(A\),
\[
D^2H(C\oplus(c))[A,A]
 =D^2H(C)[A_{\{1,2\},\{1,2\}},A_{\{1,2\},\{1,2\}}]
  -\frac{A_{33}^2}{c(1-c)}\le0.
\tag{5}
\]
The inequality uses its two-point theorem. Off-block entries of \(A\) do not contribute to this second variation. This proves the required Hessian sign on the entire singular stratum. \(\square\)

Here singularity refers to \(R_Q\) while \(Q\) remains a strict contraction. At a boundary kernel, some logarithms used to define \(R_Q\) can be undefined. Boundary endpoints for the directional theorems below are handled by regularization, not by assigning finite values to these logarithms.

## 2. Joint concavity with a coordinate rank-one direction

The following elementary inequality controls the positive mixed term.

**Lemma 2.1.** For \(0<r<1\),
\[
\frac1{r(1-r)}-\log^2\frac{1-r}{r}\ge4.
\tag{6}
\]

**Proof.** Put \(u=\log((1-r)/r)\). The left side is \(2+2\cosh u-u^2\), which is at least four because \(\cosh u\ge1+u^2/2\). \(\square\)

**Proof of Theorem B.** First work at a strict contraction, and permute the distinguished coordinate to index zero. Write
\[
Q=\begin{pmatrix}a&v^*\\v&C\end{pmatrix},\qquad
b=\begin{pmatrix}b_0\\b_F\end{pmatrix},\qquad
A=\alpha e_0e_0^*+bb^*.
\]
For each exact pattern \(T\subseteq F\), use the quantities from the one-row theorem of C0033B:
\[
M_T=C-D_{F\setminus T},\qquad
\pi_T=P_C(T),\qquad
r_T=a-v^*M_T^{-1}v.
\tag{7}
\]
Thus \(\pi_T>0\), \(0<r_T<1\), and the two joint atoms over \(T\) are \(\pi_T r_T\) and \(\pi_T(1-r_T)\). Set
\[
k_T=b_F^*M_T^{-1}b_F,\qquad
\rho_T=|b_0-v^*M_T^{-1}b_F|^2,\qquad
u_T=\log\frac{1-r_T}{r_T}.
\tag{8}
\]
Differentiation along \(bb^*\), using the determinant formula for \(\pi_T\) and the conditional kernel formula for \(r_T\), gives
\[
\pi'_T=\pi_T k_T,\qquad r'_T[bb^*]=\rho_T\ge0.
\tag{9}
\]
The latter equality also follows directly by differentiating the Schur complement in (7). Hence along \(A\),
\[
\pi'_T=\pi_T k_T,\qquad r'_T=\alpha+\rho_T.
\]
The Fisher quadratic form splits into a marginal and a conditional part:
\[
\mathcal F_Q(A):=\sum_S\frac{Dp_S[A]^2}{p_S}
 =\sum_T\pi_T\left\{k_T^2+
       \frac{(\alpha+\rho_T)^2}{r_T(1-r_T)}\right\}.
\tag{10}
\]
Indeed, substitution of the derivatives of \(\pi_T r_T\) and \(\pi_T(1-r_T)\) cancels their two cross terms.

For clarity, the logarithmic second-variation term can be computed while holding the logarithms fixed. If \(f\) is any fixed set function and \(\Phi_f(K)=E_{P_K}f\), variation of the single diagonal entry gives
\[
D_{e_0e_0^*}\Phi_f(Q)
 =\sum_T\pi_T\{f(T\cup\{0\})-f(T)\}.
\tag{11}
\]
Differentiating (11) in direction \(bb^*\) and then taking \(f(S)=\log p_S\) at the base kernel yields
\[
D_{bb^*}D_{e_0e_0^*}\Phi_f(Q)
 =\sum_T\pi_T k_T\log\frac{r_T}{1-r_T}
 =-g_Q(b),
\qquad
 g_Q(b):=\sum_T\pi_T k_T\nu_T.
\tag{12}
\]
Every atom is affine along either of the two rank-one directions separately. Therefore its second derivative along their sum consists only of the mixed term, and the entropy second derivative is exactly
\[
D^2H(Q)[A,A]=-\mathcal F_Q(A)+2\alpha g_Q(b).
\tag{13}
\]
C0033B, equation (8) and its positive semidefiniteness proof, give
\[
g_Q(b)=b_F^*\left(\sum_T\pi_T\nu_T M_T^{-1}\right)b_F\ge0.
\tag{14}
\]
This is an invocation of the predecessor's one-row result.

If \(\alpha\le0\), (13) and (14) prove nonpositive curvature. If \(\alpha\ge0\), substitute (10) into (13) and complete the square:
\[
\begin{aligned}
\mathcal F_Q(A)-2\alpha g_Q(b)
=\sum_T\pi_T\bigg\{&(k_T-\alpha\nu_T)^2
 +\alpha^2\left[\frac1{r_T(1-r_T)}-\nu_T^2\right]\\
 &+\frac{2\alpha\rho_T+\rho_T^2}{r_T(1-r_T)}\bigg\}
\ge4\alpha^2.
\end{aligned}
\tag{15}
\]
The last step uses Lemma 2.1, \(\rho_T\ge0\), and \(\sum_T\pi_T=1\). This proves both nonpositive curvature and (1).

An arbitrary direction in the two-dimensional affine family in Theorem B is \(\alpha e_0e_0^*+\beta bb^*\). For \(\beta>0\), absorb \(\sqrt\beta\) into \(b\). For \(\beta<0\), reverse the direction, which does not change a second variation, and then absorb \(\sqrt{-\beta}\). For \(\beta=0\), use rank-one concavity. Thus the Hessian restricted to the family is negative semidefinite throughout its strict feasible set. This set is convex, so the restriction is concave there.

For arbitrary feasible endpoints \(Q_1,Q_2\) in this family, use
\[
Q_j^\varepsilon=(1-2\varepsilon)Q_j+\varepsilon I,
\qquad 0<\varepsilon<1/2.
\]
Their difference remains in the span of the same two directions. The interior argument applies, and continuity of the finite entropy sum as \(\varepsilon\downarrow0\) proves the assertion on the closed feasible set.

It remains to establish the stated consequence for a rank-two matrix \(A\) whose range contains \(e_0\). Its range is spanned by \(e_0\) and a vector \((0,w)\), where \(w\ne0\). Thus
\[
A=\begin{pmatrix}a&\overline\eta w^*\\\eta w&\delta ww^*\end{pmatrix},
\qquad a,\delta\in\mathbb R.
\tag{16}
\]
If \(\delta=0\), this is a one-row-and-column direction, covered by C0033B. Otherwise reverse its sign if needed to arrange \(\delta>0\). Completing the square gives
\[
A=\left(a-\frac{|\eta|^2}{\delta}\right)e_0e_0^*+bb^*,
\qquad
b=\begin{pmatrix}\overline\eta/\sqrt\delta\\\sqrt\delta\,w\end{pmatrix}.
\tag{17}
\]
This is precisely the direction treated above. Both possible signs of its first coefficient have been proved. \(\square\)

On three points, the range condition is equivalent to the null vector of a rank-two direction having at least one zero coordinate. A generic rank-two positive semidefinite direction has a null vector with no zero coordinates. Such directions are not covered by this theorem. All indefinite rank-two directions on three points were already covered by C0033B, Theorem 3.3.

## 3. Conditioning an arbitrary rank-two update

The following formula records what conditioning does to a general update. It also identifies the terms that prevent an immediate application of conditional lifting or one-row concavity.

**Proposition C.** Let \(Q(t)=Q+tUDU^*\), where \(U\) has two columns and \(D\) is an invertible Hermitian matrix of order two. Partition the coordinates as \(B\sqcup C\), fix an exact pattern \(T\subseteq C\), and put
\[
M=Q_{CC}-D_{C\setminus T},\quad
G=U_C^*M^{-1}U_C,\quad
W=U_B-Q_{BC}M^{-1}U_C.
\]
Near \(t=0\) at a strict contraction, the pattern weight and conditional kernel satisfy
\[
\begin{aligned}
\pi_T(t)&=\pi_T(0)\det(I_2+tDG),\\
K_T(t)&=K_T(0)+tW(D^{-1}+tG)^{-1}W^*.
\end{aligned}
\tag{18}
\]
In particular,
\[
K'_T(0)=WDW^*,\qquad K''_T(0)=-2WDGDW^*.
\tag{19}
\]

**Proof.** Apply the matrix determinant lemma to \(M+tU_CDU_C^*\) to obtain the first identity. In the Schur complement defining \(K_T(t)\), substitute
\[
(M+tU_CDU_C^*)^{-1}
=M^{-1}-tM^{-1}U_C(D^{-1}+tG)^{-1}U_C^*M^{-1}.
\]
Expansion and collection of the terms containing \(U_B-Q_{BC}M^{-1}U_C\) give the second identity. Differentiation at zero gives (19). All inverses exist in a neighborhood of zero; no assertion at a pole is required. \(\square\)

Even conditioning on one coordinate need not produce an affine conditional kernel. For an exact rational example, let
\[
Q=I_4/2,\quad a=(1,1,1,1)^{\mathsf T}/4,\quad
b=(1,2,-1,-2)^{\mathsf T}/4,\quad A=aa^*+bb^*.
\]
Condition on coordinate four being occupied, and put
\(c=A_{\{1,2,3\},4}=(-1,-3,3)^{\mathsf T}/16\). Then
\[
\pi_1(t)=\frac12+\frac5{16}t,
\qquad
K_1(t)=\frac12 I_3+tA_{\{1,2,3\},\{1,2,3\}}
       -\frac{t^2cc^*}{1/2+(5/16)t},
\qquad K_1''(0)=-4cc^*\ne0.
\tag{20}
\]
These identities are verified symbolically in [structural_audit.py](structural_audit.py), with output [data/structural_audit.json](data/structural_audit.json). The example is not a counterexample to entropy concavity. It shows that, for a general rank-two update, the conditional entropy chain rule has changing weights and nonlinear conditional kernels. Concavity on affine one-row families does not supply the missing signs for these additional terms. If \(U_C=0\), (18) reduces to the fixed-weight affine setting of the conditional lifting theorem in C0033A.

## 4. Inequality (17) on the connected domain

For \(R=R_Q>0\), let \(d=\det R\), let \(E_\alpha\) be a Frobenius-orthonormal real basis of Hermitian matrices, and set
\[
F_{\alpha\beta}=\sum_S\frac{Dp_S[E_\alpha]Dp_S[E_\beta]}{p_S},\quad
J_{\alpha\beta}=F_{\alpha\beta}
+d\operatorname{tr}(R^{-1}E_\alpha R^{-1}E_\beta),\quad
z_\alpha=\operatorname{tr}(R^{-1}E_\alpha).
\]
C0033B proves that full Hessian nonpositivity is equivalent to
\[
\theta(Q):=d z^{\mathsf T}J^{-1}z\le1.
\tag{21}
\]
Theorem A treats exactly the strict kernels at which this expression is not defined. It does not establish (21) for connected kernels.

For numerical conditioning, [probe_scalar.py](probe_scalar.py) uses the congruent form
\[
T_\alpha=R^{1/2}E_\alpha R^{1/2},\quad
\widetilde F_{\alpha\beta}=\frac1d\sum_S
 \frac{Dp_S[T_\alpha]Dp_S[T_\beta]}{p_S},\quad
\theta(Q)=\tau^{\mathsf T}(I+\widetilde F)^{-1}\tau,
\qquad \tau_\alpha=\operatorname{tr}E_\alpha.
\tag{22}
\]
This is a change of variables in the inherited scalar criterion. It avoids forming \(R^{-1}\) in the search. The original-coordinate expression (21) and (22) are compared independently at 100 kernels in [structural_audit.py](structural_audit.py).

A rounded rational version of the largest located score is certified by [interval_audit.py](interval_audit.py). Its exact nine coordinates are in [data/scalar_witness_rational.json](data/scalar_witness_rational.json). Exact rational leading principal minors prove \(Q>0\) and \(I-Q>0\). The script evaluates integer atom polynomials and their derivatives using 100-decimal-place outward-rounded `mpmath.iv` arithmetic. Interval leading minors certify \(R>0\). Interval \(LDL^{\mathsf T}\) factorizations certify positive definiteness of \(J\) and of the negative full nine-dimensional Hessian. A triangular interval solve bounds (21). The basis in this certificate is the unnormalized coordinate basis; the scalar expression is invariant under an invertible basis change.

<!-- TABLES_START -->

Scalar search ([probe_scalar.py](probe_scalar.py), [data/scalar_search.json](data/scalar_search.json)):

| Family | Kernels | Largest score (21) |
| --- | ---: | ---: |
| uniform | 1500 | 0.7599495134 |
| extreme | 1500 | 0.9271546014 |
| projection | 1500 | 0.8842327818 |

| Optimization start | Evaluations | Largest score |
| --- | ---: | ---: |
| 0 | 1600 | 0.955829264 |
| 1 | 1600 | 0.9556245527 |
| 2 | 1600 | 0.9339534781 |
| 3 | 1600 | 0.9555522144 |
| 4 | 1600 | 0.95509399 |
| 5 | 1600 | 0.9180572499 |
| 6 | 1600 | 0.9446432502 |
| 7 | 1600 | 0.9549322737 |

Rational point certificate ([interval_audit.py](interval_audit.py), [data/interval_audit.json](data/interval_audit.json)). This point is rounded from the floating search witness, so its score differs slightly. Bounds below are shortened outwards.

| Quantity | Certified interval |
| --- | --- |
| Score (21) | [0.955828326323, 0.955828326324] |
| One minus score | [0.044171673676, 0.044171673677] |

| Negative full Hessian LDL pivot | Certified interval |
| --- | --- |
| 1 | [100000.94286388, 100000.94286389] |
| 2 | [50009.23897079, 50009.23897080] |
| 3 | [78.25935206, 78.25935207] |
| 4 | [0.11459612, 0.11459613] |
| 5 | [0.07157312, 0.07157313] |
| 6 | [0.00000405, 0.00000406] |
| 7 | [0.00000352, 0.00000353] |
| 8 | [136.60823528, 136.60823529] |
| 9 | [38271.72291617, 38271.72291618] |

General rank-two searches ([ranktwo_search.py](ranktwo_search.py), [data/ranktwo_search.json](data/ranktwo_search.json)):

| n | Signature | Trials | Largest curvature | Smallest midpoint gap |
| --- | --- | ---: | ---: | ---: |
| 3 | positive | 800 | -1.641359761 | 1.363242852e-12 |
| 3 | indefinite | 800 | -0.2208121031 | 2.675915045e-13 |
| 4 | positive | 800 | -1.440411589 | 3.335109966e-13 |
| 4 | indefinite | 800 | -0.2383670169 | 1.727507026e-13 |
| 6 | positive | 300 | -1.03382519 | 1.154631946e-13 |
| 6 | indefinite | 300 | -0.5427186248 | 4.047873148e-13 |
| 8 | positive | 300 | -0.9327713172 | 6.616929227e-14 |
| 8 | indefinite | 300 | -0.5387333285 | 3.108624469e-14 |

Positive rank-two optimizations on three points (same code and data):

| Start | Evaluations | Curvature | Smaller positive direction eigenvalue |
| --- | ---: | ---: | ---: |
| 0 | 2500 | -1.338188941 | 0.001049463237 |
| 1 | 2500 | -1.3368421 | 0.000122596347 |
| 2 | 2500 | -1.335222907 | 3.269964189e-05 |
| 3 | 2500 | -1.33483237 | 0.0001139423543 |
| 4 | 2500 | -1.335233232 | 6.319099427e-05 |
| 5 | 2500 | -1.358163867 | 0.002395213514 |
| 6 | 2500 | -1.334543163 | 0.0003013040187 |
| 7 | 2500 | -1.335086624 | 0.0003368199576 |

Exact rank-two certificates ([certify_ranktwo.py](certify_ranktwo.py), [data/ranktwo_certificates.json](data/ranktwo_certificates.json)). The inputs are the adjacent `*_rational.json` files; all ranks and kernel leading minors are checked exactly. Curvatures are for unit Frobenius norm and intervals are shortened outwards.

| Witness | Certified curvature interval |
| --- | --- |
| psd_optimized_0 | [-1.338188942, -1.338188941] |
| psd_optimized_1 | [-1.336842101, -1.336842100] |
| psd_optimized_2 | [-1.335222908, -1.335222907] |
| psd_optimized_3 | [-1.334832371, -1.334832370] |
| psd_optimized_4 | [-1.335233232, -1.335233231] |
| psd_optimized_5 | [-1.358163868, -1.358163867] |
| psd_optimized_6 | [-1.334543164, -1.334543163] |
| psd_optimized_7 | [-1.335086625, -1.335086624] |
| ranktwo_n3_sign1 | [-1.641359762, -1.641359761] |
| ranktwo_n3_sign-1 | [-0.220812104, -0.220812103] |
| ranktwo_n4_sign1 | [-1.440411590, -1.440411589] |
| ranktwo_n4_sign-1 | [-0.238367017, -0.238367016] |

Independent structural checks ([structural_audit.py](structural_audit.py) and [ranktwo_search.py](ranktwo_search.py)):

| Identity | Cases | Largest absolute error |
| --- | ---: | ---: |
| Original criterion (21) versus congruent criterion (22) | 100 | 9.436895709e-16 |
| Theorem B formula (13) versus inherited C++ curvature | 400 | 2.131628207e-14 |
| Conditional rank-two formula (18), rational example | 1 | exact zero |

The smallest observed scalar form in (14) was 9.246200774e-06.

| Run | Seconds | Peak RSS, MiB |
| --- | ---: | ---: |
| scalar search | 1.653492292 | 73.15625 |
| rank-two search | 3.5396735 | 77.3125 |
| scalar interval audit | 0.04633566701 | 68.75 |
| rank-two exact/interval certificates | 11.42927629 | 84.515625 |
| structural audit | 0.093436792 | 104.578125 |

<!-- TABLES_END -->

These point certificates do not cover the connected domain. The numerical extrema are attained search values, not certified suprema. No assertion that \(\theta(Q)<1\) holds globally follows from them.

## 5. Computation and reproducibility

All calculations enumerate every atom. The searches use binary floating point and fixed seeds 33361 and 33362. No worker pool, subagent, or additional language-model process was started; numerical libraries use one thread. Search processes inherit the session's priority. Their measured peak resident memory is reported in the generated tables and is far below 4 GB.

The scalar search contains 1,500 complex kernels of each of three spectral types: interior spectra, eigenvalues close to zero or one, and regularized projections. It also contains eight Nelder–Mead optimizations with 1,600 evaluations per start and eigenvalues restricted to \([10^{-5},1-10^{-5}]\). All eight reached their evaluation cap. The direction derived from the scalar solve is not the ordinary largest-eigenvalue Hessian direction; its curvature and the largest Hessian eigenvalue are distinct quantities.

The rank-two search uses genuine two-column factors, with positive or opposite-sign weights, in dimensions 3, 4, 6 and 8. The directions have Frobenius norm one. Each midpoint test uses endpoints \(Q\pm sA\), where \(s\) is half the spectral distance of \(Q\) from the boundary; \(\|A\|_{\mathrm{op}}\le1\) guarantees feasibility. Very small gaps in the table are evaluated in floating point and can be sensitive to cancellation. Eight additional optimizations vary a three-point kernel and a complex positive rank-two factor, with 2,500 evaluations per start and a kernel spectral margin of \(10^{-4}\). All reached the cap; several approach rank one, as their saved eigenvalues show. No optimization is claimed to find a global maximum.

The 400 checks of Theorem B compare (13) against the inherited C++ curvature routine. The matrix \(G_Q\) is not assumed positive by the code: its tested scalar quadratic form is recorded independently. These checks support implementation correctness; the proof is the argument in Section 2.

[certify_ranktwo.py](certify_ranktwo.py) rounds the saved **factors**, rather than rounding the entries of a rank-two direction. It therefore produces exact rational rank-two matrices. For each of twelve three- or four-point witnesses, exact rational arithmetic checks the rank, positivity of the kernel and its complement, positivity of every atom, and normalization of the first two atom derivatives. Interval logarithms then certify strictly negative curvature after division by the exact squared Frobenius norm. For the three-point witnesses, determinant polynomial coefficients independently verify the inverse-based derivatives. The rational inputs and interval endpoints are saved in [data/](data/). These are certificates for individual directions, not global rank-two certificates.

To reproduce all results, using Python 3, NumPy, SciPy, SymPy, mpmath and a C++17 compiler, run:

```sh
python3 reproduce.py
```

The runner builds the inherited library and executes each numerical process sequentially. [artifact_manifest.json](artifact_manifest.json) records package versions and SHA-256 hashes. Reproduction overwrites generated data with the same fixed seeds. The library filename and compiler flags in the inherited code target macOS.

## 6. Remaining questions

1. **Connected strict three-point kernels:** inequality (21), which is C0033B (17), is unproved on this domain. No point violating it has been certified. The singular \(R_Q\) case is completely covered by Theorem A.
2. **Positive semidefinite rank two on three points:** Theorem B covers directions whose null vector has a zero coordinate. Directions with all three null-vector coordinates nonzero remain unresolved. Negative semidefinite directions have the same status by reversal.
3. **Rank two in dimensions at least four:** Theorem B covers directions whose range contains a coordinate vector. C0033B covers one-row changes and indefinite rank-two changes supported on three coordinates; C0033A covers changes supported on two coordinates. General directions outside these families remain unresolved. Formula (18) alone does not close the conditioning argument.
4. **Full three-point theorem:** neither a complete concavity proof nor an entropy counterexample is obtained. A proof of (21) on the connected strict domain, combined with Theorem A and continuity under common regularization, would complete the three-point theorem. The present point certificates cannot replace that step.

For the inherited literature statements, the rank-one result is Gu's Theorem 7 in [*Entropy of Determinantal Point Processes*](https://sevenkplus.com/data/dpp.pdf). The stochastic domination fact used in C0033B's one-row proof is Theorem 4.13 of [Borcea–Brändén–Liggett, *Negative dependence and the geometry of polynomials*](https://arxiv.org/pdf/0707.2340). Neither result is used here to assert an unproved higher-dimensional conclusion.

Task: “Open problem C0033, third attempt: entropy concavity of determinantal point processes on three points and in rank two” — received 13 November 2026, approximately 02:58, Asia/Tbilisi.
