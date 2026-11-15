PARTIAL

# Concavity of finite determinantal entropy

Let \(H(Q)=\operatorname{Ent}(P_Q)\), with natural logarithms. The following statements are proved below for complex Hermitian kernels and therefore also for real symmetric kernels.

1. **Two points.** \(H\) is concave on \(\{Q\in\mathbb C^{2\times2}:0\le Q\le I\}\). This theorem is already in [the author's November 2026 preprint](https://github.com/yspennstate/lyons-determinantal-entropy-two-points/blob/main/paper/main.tex). Section 2 gives an alternative proof by a cubic determinant identity.
2. **Two coordinate indices in any dimension.** If \(Q_1-Q_2\) is supported on \(B\times B\), where \(|B|\le2\), then
   \[
   H((1-t)Q_1+tQ_2)\ge(1-t)H(Q_1)+tH(Q_2),\qquad 0\le t\le1.
   \]
   No restriction is imposed on the entries connecting \(B\) to its complement. More generally, concavity in dimension \(m\) lifts to changes supported on any \(m\) coordinate indices.
3. **Local second variation in all dimensions.** At a strict block diagonal contraction, the Hessian is the sum of the Hessians on the diagonal blocks. In particular it is negative semidefinite in every direction when all blocks have size at most two. At \(Q=\operatorname{diag}(q_i)\), \(0<q_i<1\),
   \[
   D^2H(Q)[A,A]=-\sum_i\frac{A_{ii}^2}{q_i(1-q_i)}.
   \]
4. **Explicit fourth variation at product kernels.** If \(A=A^*\) has zero diagonal, then
   \[
   H(Q+tA)=\sum_i h(q_i)-\frac{t^4}{2}
   \sum_{i<j}\frac{|A_{ij}|^4}{q_i(1-q_i)q_j(1-q_j)}+O(t^5),
   \tag{1}
   \]
   where \(h(u)=-u\log u-(1-u)\log(1-u)\). For \(n\ge2\), the positive coefficient subtracted in (1) is at least
   \[
   \frac{4\|A\|_F^4}{n(n-1)}.
   \tag{2}
   \]
   For \(n\ge2\), this bound is sharp: take \(Q=I/2\) and constant \(|A_{ij}|\) for \(i\ne j\). Every fixed affine line through a strict coordinate-diagonal kernel has a neighborhood on which its entropy is concave.

No counterexample was found. The searches include exact enumeration of all atoms through \(n=14\), analytic directional derivatives, full Hessians through \(n=6\), and optimization of full and circulant-symbol Hessians. Each saved optimized witness had negative curvature at both 80 and 120 decimal digits. These computations do not settle the finite conjecture, its general rank-two or commuting restrictions, or entropy-rate concavity.

The two-point theorem and the fourth-order phenomenon at reducible kernels predate this audit. No priority claim is made for the conditional lifting or the product-kernel formulas.

## 1. Determinant and differentiation identities

For \(S\subseteq E\), put \(D_{S^c}=\operatorname{diag}(\mathbf1_{i\notin S})\) and \(B_S=Q-D_{S^c}\). Then
\[
p_S=P_Q[X=S]=(-1)^{n-|S|}\det B_S.
\tag{3}
\]
For \(0<Q<I\), all these probabilities are positive. Indeed, \(L=Q(I-Q)^{-1}>0\) and
\[
p_S=\frac{\det L_{S,S}}{\det(I+L)}.
\tag{4}
\]
To verify (4), multiply \(Q-D_{S^c}\) on the right by \(I+L\). Rows indexed by \(S\) become rows of \(L\); the other rows become rows of \(-I\). Expansion in the latter rows gives (4). In particular \(B_S\) is invertible in the interior.

For a Hermitian direction \(A\), let
\[
r_S=\operatorname{tr}(B_S^{-1}A),\qquad
u_S=\operatorname{tr}(B_S^{-1}AB_S^{-1}A).
\]
Jacobi's identity gives \(p'_S=p_Sr_S\) and \(p''_S=p_S(r_S^2-u_S)\). Differentiation of the finite entropy sum, using \(\sum_Sp''_S=0\), yields
\[
D^2H(Q)[A,A]
=-\sum_Sp_S\{r_S^2+\log p_S\,(r_S^2-u_S)\}.
\tag{5}
\]
Traces in these formulas are real, even though \(B_S^{-1}A\) need not be Hermitian. Polarization gives the full real Hessian on the real vector space of Hermitian matrices.

For a rank-one direction the polynomial \(\det(B_S+tA)\) is affine: any term selecting two updated columns has two proportional columns. Thus the probability vector itself is affine in \(t\), and ordinary concavity of Shannon entropy proves rank-one concavity, including boundary cases. This is Gu's Theorem 7. The same argument does not extend directly to rank two because a quadratic term remains. [Gu's report](https://sevenkplus.com/data/dpp.pdf) also proves \(H(tQ)\ge tH(Q)\); that endpoint inequality by itself does not assert concavity between two arbitrary points on the ray.

## 2. Concavity on two points

**Theorem 2.1.** The function \(H\) is concave on the full set of Hermitian positive contractions of order two.

**Proof.** Write
\[
Q=\begin{pmatrix}a&c+id\\c-id&b\end{pmatrix}.
\]
First assume \(0<Q<I\), \(d=0\), and \(c>0\). Denote the probabilities of \(\varnothing,\{1\},\{2\},\{1,2\}\) by \(w,x,y,z\), respectively. They satisfy
\[
\begin{aligned}
w&=(1-a)(1-b)-c^2,&x&=a(1-b)+c^2,\\
y&=(1-a)b+c^2,&z&=ab-c^2,
\end{aligned}
\]
and hence
\[
w+x+y+z=1,\qquad xy-wz=c^2.
\tag{6}
\]
All four probabilities are positive. Put
\[
\alpha=wz,\quad\beta=xy,\quad\delta=\beta-\alpha=c^2,
\quad P=wxyz=\alpha\beta,\quad
\ell=\log(\beta/\alpha)>0.
\]
In the real coordinates \((a,b,c)\), the four probability gradients are
\[
\begin{aligned}
g_w&=(b-1,a-1,-2c)^{\mathsf T},&g_x&=(1-b,-a,2c)^{\mathsf T},\\
g_y&=(-b,1-a,2c)^{\mathsf T},&g_z&=(b,a,-2c)^{\mathsf T}.
\end{aligned}
\]
Define
\[
G=\sum_{p\in\{w,x,y,z\}}\frac{g_pg_p^{\mathsf T}}p,
\qquad M=\begin{pmatrix}0&1&0\\1&0&0\\0&0&-2\end{pmatrix}.
\]
The second derivatives of \(w,z\) equal \(M\), and those of \(x,y\) equal \(-M\). It follows that
\[
-\nabla^2H=G-\ell M.
\tag{7}
\]
The matrix \(G\) is positive definite. In fact, if a vector annihilates all four gradients, it annihilates the gradients of \(x+z=a\) and \(y+z=b\), so its first two coordinates vanish; the last then vanishes because \(c>0\).

The determinant needed for (7) is the following polynomial identity:
\[
\det(G-sM)=\frac2P\{2\delta+Bs-Ps^3\},
\qquad B=\beta-\delta(w+z)=\alpha+\delta(x+y).
\tag{8}
\]
For completeness, direct determinant expansion in \(s\), followed by (6), gives these four coefficients:

| Power of \(s\) | Coefficient of \(\det(G-sM)\) |
|---|---:|
| 0 | \(4\delta/P\) |
| 1 | \(2[\beta-\delta(w+z)]/P\) |
| 2 | \(0\) |
| 3 | \(-2\) |

The gradients displayed above specify every entry in this expansion. An executable polynomial verification, reducing modulo \(c^2-xy+wz\) and \(w+x+y+z-1\), is [audit_two_point.py](audit_two_point.py); its zero remainder is recorded in [data/two_point_symbolic.txt](data/two_point_symbolic.txt).

Let \(\phi(s)=2\delta+Bs-Ps^3\). On \([0,\ell]\) it is concave, since \(\phi''(s)=-6Ps\le0\), and \(\phi(0)=2\delta>0\). Also \(B\ge\alpha\), \(\beta=xy\le1/4\), and \(\delta=\alpha(e^\ell-1)\). Therefore
\[
\begin{aligned}
\phi(\ell)
&\ge\alpha\{2(e^\ell-1)+\ell-\beta\ell^3\}\\
&\ge\alpha\{\ell+(1/3-\beta)\ell^3\}\\
&\ge\alpha(\ell+\ell^3/12)>0.
\end{aligned}
\tag{9}
\]
The middle inequality uses the elementary bound \(e^v-1\ge v^3/6\) for \(v\ge0\). Concavity and the positive endpoint values give \(\phi(s)>0\) throughout \([0,\ell]\). Thus (8) never vanishes there. Since \(G\) is positive definite, continuity of the eigenvalues of the real symmetric matrix \(G-sM\) implies that \(G-\ell M\) is positive definite. This proves the required Hessian sign for the three real coordinates.

For a general nonzero complex off-diagonal entry, conjugation by a fixed diagonal unitary makes it positive real. This conjugation preserves all principal minors and is a linear isometry of the kernel space. At \(d=0\), mixed second derivatives involving \(d\) vanish because the entropy depends on \(c,d\) through \(c^2+d^2\). Its remaining second derivative is
\[
\frac{\partial^2 H}{\partial d^2}
=2\log\frac{wz}{xy}=-2\ell<0.
\]
Consequently the full Hermitian Hessian is negative definite when the off-diagonal entry is nonzero. At a zero off-diagonal entry, \(\ell=0\) and the same gradient formula gives a negative semidefinite Hessian; alternatively this follows by continuity within the interior.

The open set \(0<Q<I\) is convex, so the Hessian sign proves concavity there. For boundary kernels use \(Q^\varepsilon=(1-2\varepsilon)Q+\varepsilon I\), apply interior concavity, and let \(\varepsilon\downarrow0\). Each atom is polynomial in the entries and \(-p\log p\) is continuous at zero, proving the result on the closed domain. \(\square\)

## 3. Conditional lifting and coordinate-supported rank-two changes

**Lemma 3.1.** Partition the coordinates as \(E=B\sqcup C\), let \(0<Q<I\), and fix a pattern \(T\subseteq C\). Conditional on \(X\cap C=T\), the process on \(B\) is determinantal with kernel
\[
K_T=Q_{BB}-Q_{BC}(Q_{CC}-D_{C\setminus T})^{-1}Q_{CB}.
\tag{10}
\]

**Proof.** Put \(M_T=Q_{CC}-D_{C\setminus T}\). By (3) applied to the marginal on \(C\),
\[
\pi_T=P_Q[X\cap C=T]=(-1)^{|C\setminus T|}\det M_T>0.
\]
For every \(U\subseteq B\), inclusion-exclusion on the coordinates of \(C\setminus T\) gives
\[
P_Q[U\subseteq X,\ X\cap C=T]
=(-1)^{|C\setminus T|}
\det\begin{pmatrix}Q_{UU}&Q_{UC}\\Q_{CU}&M_T\end{pmatrix}.
\]
Taking the Schur complement and dividing by \(\pi_T\) gives \(\det(K_T)_{UU}\). These inclusion probabilities determine the conditional law. The matrix \(K_T\) is Hermitian. Every principal minor of \(K_T\) is nonnegative, being an inclusion probability; by inclusion-exclusion every principal minor of \(I-K_T\) is an avoidance probability and is also nonnegative. The principal-minor criterion for Hermitian positive semidefiniteness gives \(0\le K_T\le I\). \(\square\)

**Theorem 3.2.** Suppose entropy concavity holds for kernels of order \(m\). In any dimension it then holds between kernels whose difference is supported on \(B\times B\), where \(|B|=m\).

**Proof.** First assume both kernels are strict contractions. Along their segment \(Q(t)\), the matrices \(Q_{CC}\) and \(Q_{BC}\) are constant. Thus \(\pi_T\) is constant and (10) is affine in \(t\), for every \(T\). The entropy chain rule is
\[
H(Q(t))=H(P_{Q_{CC}})+\sum_{T\subseteq C}\pi_T H(K_T(t)).
\tag{11}
\]
By the assumed \(m\)-point theorem each summand is concave in \(t\), with a fixed nonnegative coefficient. This proves the assertion in the interior. The common regularization used in Theorem 2.1 preserves the support condition on the difference and proves the boundary assertion by continuity. \(\square\)

Combining Theorems 2.1 and 3.2 proves statement 2 of the report. It includes positive, negative and indefinite directions of rank two supported on two coordinate indices. It does not include every rank-two Hermitian direction: an arbitrary change of eigenbasis changes the DPP entropy. A further immediate consequence is joint concavity on any fixed coordinate block diagonal family whose blocks have size at most two, since the DPP factors across the blocks and entropies add.

## 4. Second and fourth variations at product kernels

**Proposition 4.1.** Let \(Q=\bigoplus_{j=1}^r Q_j\) be a strict coordinate block diagonal contraction. For every Hermitian \(A\),
\[
D^2H(Q)[A,A]=\sum_{j=1}^rD^2H(Q_j)[A_{jj},A_{jj}].
\tag{12}
\]

**Proof.** Let \(P_t=P_{Q+tA}\), and let \(R_t\) be the product of its block marginals \(P_{Q_j+tA_{jj}}\). At \(t=0\), \(P_0=R_0\) and every atom is positive. Expansion of each determinant in permutations shows that a term using an off-block entry must use at least two off-block entries: a permutation leaving a block must also return to it. Consequently \(P_t-R_t=O(t^2)\) atom by atom. Taylor expansion of relative entropy about a positive probability vector, with the linear terms canceled by normalization, gives \(D(P_t\Vert R_t)=O(t^4)\). The exact identity
\[
H(P_t)=\sum_j H(P_{Q_j+tA_{jj}})-D(P_t\Vert R_t)
\]
now proves (12) by differentiation. \(\square\)

For blocks of size at most two, (12) and Theorem 2.1 imply a negative semidefinite Hessian in all ambient directions. For singleton blocks, \(h''(q)=-1/[q(1-q)]\) gives the explicit second variation in statement 3. This Hessian has a large nullspace, consisting of the zero-diagonal directions.

**Theorem 4.2.** Formula (1), the sharp bound (2), and the affine-line local concavity assertion in statement 4 hold.

**Proof.** Let \(P=P_Q\) for diagonal \(Q\), and write \(v_i=q_i(1-q_i)\), \(\xi_i=\mathbf1_{i\in X}\), and \(Z_i=\xi_i-q_i\). Under \(P\), the \(Z_i\) are independent and centered, with \(E_PZ_i^2=v_i\). For zero-diagonal \(A\), determinant expansion gives, for every \(U\subseteq E\),
\[
\det(Q+tA)_{UU}
=\prod_{i\in U}q_i
-t^2\sum_{\{i,j\}\subseteq U}|A_{ij}|^2\prod_{k\in U\setminus\{i,j\}}q_k
+O(t^3).
\tag{13}
\]
By inclusion-exclusion, the coefficient \(R_S\) of \(t^2\) in the exact atom probability is
\[
R_S=-\sum_{i<j}|A_{ij}|^2\partial_{q_i}\partial_{q_j}P[S].
\]
Since \(\partial_{q_i}P[S]=P[S]Z_i(S)/v_i\), this is the explicit score identity
\[
\frac{R_S}{P[S]}=-\sum_{i<j}\frac{|A_{ij}|^2}{v_iv_j}Z_i(S)Z_j(S).
\tag{14}
\]
All one-coordinate marginals stay fixed along \(Q+tA\), and \(P\) is their product. Thus
\[
H(Q)-H(Q+tA)=D(P_{Q+tA}\Vert P).
\tag{15}
\]
Taylor expansion of \((p+u)\log((p+u)/p)\), summed over atoms, cancels the linear term. Since \(p_S(t)-P[S]=t^2R_S+O(t^3)\), (15) yields
\[
H(Q)-H(Q+tA)=\frac{t^4}{2}\sum_S\frac{R_S^2}{P[S]}+O(t^5).
\]
For distinct unordered pairs \(\{i,j\}\ne\{k,l\}\), independence and centering imply \(E_P[Z_iZ_jZ_kZ_l]=0\). Equation (14) therefore gives
\[
\sum_S\frac{R_S^2}{P[S]}=\sum_{i<j}\frac{|A_{ij}|^4}{v_iv_j},
\]
proving (1). Because \(v_i\le1/4\) and there are \(N=n(n-1)/2\) unordered pairs,
\[
\frac12\sum_{i<j}\frac{|A_{ij}|^4}{v_iv_j}
\ge8\sum_{i<j}|A_{ij}|^4
\ge\frac8N\left(\sum_{i<j}|A_{ij}|^2\right)^2
=\frac{4\|A\|_F^4}{n(n-1)}.
\]
Both inequalities are equalities when all \(q_i=1/2\) and all \(|A_{ij}|\), \(i<j\), are equal. Such a direction is admissible for sufficiently small \(|t|\).

The entropy is real analytic near a strict contraction, since all its atom probabilities are positive. If \(A\) has some nonzero diagonal entry, its second derivative at zero is negative by Proposition 4.1, and stays negative in a neighborhood. If \(A\ne0\) has zero diagonal, (1) gives \(H''(Q+tA)=-12ct^2+O(t^3)\), where \(c>0\) is its fourth-order coefficient. This is negative for sufficiently small nonzero \(t\), and zero at \(t=0\). The zero direction is constant. These cases prove affine-line local concavity. The neighborhood may depend on the direction; a common convex neighborhood for all base kernels is not asserted. \(\square\)

The product-kernel formula permits triangles and other odd cycles in the support of \(A\). It is not restricted to a bipartite off-block direction. For two fixed blocks and a purely off-block direction, a diagonal sign conjugation identifies \(Q+tA\) with \(Q-tA\). The atom probabilities are then even, and the fourth-order expansion has remainder \(O(t^6)\). This is the reducible-kernel phenomenon in the [prior preprint](https://github.com/yspennstate/lyons-determinantal-entropy-two-points/blob/main/paper/main.tex).

## 5. Commutation, three points, and stationary restrictions

Coordinate-diagonal kernels give product Bernoulli measures, so their entropy is \(\sum_i h(Q_{ii})\), a concave function. Simultaneous diagonalizability by an arbitrary unitary is a different condition. For example,
\[
Q_1=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
Q_2=I-Q_1
\]
commute, but each DPP is uniform on the two singleton subsets, and hence is not a product measure. Their entropies are \(\log2\), while the midpoint has entropy \(2\log2\). In general
\(\operatorname{Cov}(\xi_i,\xi_j)=-|Q_{ij}|^2\), so a product DPP requires a coordinate-diagonal kernel. The commuting restriction is therefore not resolved by scalar Bernoulli concavity.

For reference, a three-point kernel with diagonal \(a,b,c\), squared off-diagonal moduli \(u=|Q_{12}|^2\), \(v=|Q_{13}|^2\), \(w=|Q_{23}|^2\), and \(\rho=2\operatorname{Re}(Q_{12}Q_{23}Q_{31})\) has
\[
d=\det Q=abc-aw-bv-cu+\rho.
\]
Its eight atoms are
\[
\begin{aligned}
p_{123}&=d,&p_{12}&=ab-u-d,&p_{13}&=ac-v-d,&p_{23}&=bc-w-d,\\
p_1&=a-ab-ac+u+v+d,\\
p_2&=b-ab-bc+u+w+d,\\
p_3&=c-ac-bc+v+w+d,\\
p_\varnothing&=1-a-b-c+ab+ac+bc-u-v-w-d.
\end{aligned}
\tag{16}
\]
Thus \(-\sum_Sp_S\log p_S\) is an explicit closed form. Neither (16) nor the searches below prove its concavity on the full three-point domain. Changes confined to any two coordinates are covered by Theorem 3.2.

On \(\mathbb Z_n\), the Fourier-multiplier family is \(Q=F\operatorname{diag}(f)F^*\). Real-valued symbols \(0\le f_j\le1\) give Hermitian circulant kernels; real symmetric circulants require \(f_j=f_{n-j}\). These are commuting families in the coordinate basis where the DPP is observed. Both were searched, without a proof of general concavity. Finite restrictions of symbols on the infinite torus give Toeplitz matrices; they are not identical to finite cyclic circulants. No implication from numerical cyclic tests to the infinite entropy-rate conjecture is claimed.

## 6. Numerical evidence and verification

The tables in the next section are generated directly from the saved JSON by [make_tables.py](make_tables.py). All floating-point searches enumerate every one of the \(2^n\) atoms, with no sampling approximation to entropy. They are exhaustive over subsets, not exhaustive over the continuous matrix domain, and are not exact rational arithmetic.

The compiled implementation [dpp.cpp](dpp.cpp), called by [dpp.py](dpp.py), evaluates (3) and (5) using pivoted elimination and extended-precision summation. Full Hessians use independent batched matrix inverses in NumPy. Directions have Frobenius norm one. Spectral families include uniform interior eigenvalues, independent eigenvalues within \(10^{-7}\) to \(10^{-1}\) of zero or one, and regularized projections. Exact singular projections are approached from the interior; they are not evaluated by an inverse formula at a singular point.

[search.py](search.py) uses seed 330013. It evaluates 3,000 full Hessians, 8,060 directional/midpoint trials, and 18 full-Hessian optimizations with at most 1,000 evaluations per start. Nelder–Mead acts on a Hermitian matrix whose eigenvalues are transformed by a logistic function; spectra are restricted to \([10^{-4},1-10^{-4}]\) during optimization. The full-Hessian objective chooses the worst direction by an eigenvalue computation at each kernel. Dense, positive and indefinite rank-two, commuting, and circulant directions are included. For dense and rank-two directional rows, the accompanying general midpoint endpoints are independently drawn; the separate targeted midpoint tests impose an actual rank-two difference.

[targeted_search.py](targeted_search.py), seed 330014, optimizes the Hessian restricted to Fourier-symbol variations at \(n=3,4,6,8\), with three starts per field and size, and tests 2,000 genuine positive or indefinite rank-two midpoint differences. Those midpoint endpoints are \(Q\pm sA\), with \(s\) chosen from the spectral margin to guarantee feasibility. Symbol optimization uses the interior margin \(10^{-5}\).

The optimizer is a finite local search. Many starts stop at their evaluation cap, as recorded in [data/search.json](data/search.json). The tables give attained values, not certified maxima. Matrices and directions for the best value in every family are in [data/](data/), with names encoding the family, size, and field.

[verify.py](verify.py), seed 330015, compares signed-determinant atoms against inclusion-exclusion of principal minors at 96 independent kernels; it also compares the C++ directional curvature against the full NumPy Hessian. All 14 saved optimized witnesses are checked with mpmath at 80 and 120 decimal digits. A separate rational complex three-point kernel is differentiated directly as a determinant entropy sum at 100 digits. These are high-precision numerical checks, not interval certificates.

[verify_structural.py](verify_structural.py), seed 330016, checks the conditional-kernel identity, the entropy chain rule, and the prior sharp block-quartic inequality. [verify_product.py](verify_product.py), seed 330017, checks (1) and the entire product-kernel Hessian in 200 cases through \(n=8\), and verifies a rational complex three-point fourth derivative directly at 100 digits. Its direct derivative is
\[
H^{(4)}(0)=-0.031656845238095238095238095238095238\ldots,
\]
equal to \(-24\) times the coefficient in (1).

All runs use a single BLAS thread; no worker pools or language-model workers were started. The numerical processes inherit nice 10. Search peak resident memory is reported below and is far under 4 GB. Source PDFs, extracted text and SHA-256 hashes are in [sources/](sources/). The computation is reproducible with Python 3, NumPy 2.2.3, SciPy 1.15.2, mpmath 1.3.0, SymPy 1.13.1, a C++17 compiler, and pdftotext:

```sh
clang++ -O3 -std=c++17 -dynamiclib dpp.cpp -o libdpp.dylib
python3 download_sources.py
python3 audit_two_point.py
python3 search.py all > search_run.log 2>&1
python3 targeted_search.py > targeted_run.log 2>&1
python3 verify.py > verify_run.log 2>&1
python3 verify_structural.py > structural_run.log 2>&1
python3 verify_product.py > product_run.log 2>&1
python3 make_tables.py
```

The shared-library command is for the Mac workspace. On Linux use the corresponding \(-shared -fPIC\) compiler flags and adjust the library filename in dpp.py. Re-running a search overwrites that search's JSON and witness files.

<!-- NUMERICAL_TABLES -->

## 7. Numerical tables

All maxima and minima below are attained sample values. A positive double-precision optimized value is not a verified violation.

**Full Hessians.** Code: search.py and dpp.py; data: [data/search.json](data/search.json). Each entry is the largest eigenvalue found among 100 kernels; the basis is orthonormal for the Frobenius inner product.

| n | field | uniform spectrum | near 0/1 | regularized projection |
| --- | --- | --- | --- | --- |
| 2 | real | -3.80561e-06 | -0.00130952 | -4.44834 |
| 2 | complex | -0.000124059 | -0.000788829 | -5.77386 |
| 3 | real | -0.000107576 | -0.000716132 | -0.163308 |
| 3 | complex | -0.00054635 | -0.0765518 | -0.00364601 |
| 4 | real | -5.80339e-05 | -0.0401625 | -0.15453 |
| 4 | complex | -0.00163277 | -0.000884634 | -0.113525 |
| 5 | real | -0.000717054 | -0.017645 | -0.99872 |
| 5 | complex | -0.000251261 | -0.0108356 | -0.294401 |
| 6 | real | -0.000901197 | -0.0637874 | -1.49197 |
| 6 | complex | -0.00143463 | -0.031096 | -1.25098 |

**Directional and midpoint search.** Code: search.py and dpp.cpp; data: [data/search.json](data/search.json). Rows combine five families: dense, positive rank two, indefinite rank two, commuting, and circulant. The derivative and midpoint samples are as specified in Section 6.

| n | field | trials | largest second derivative | smallest midpoint gap |
| --- | --- | --- | --- | --- |
| 3 | real | 1000 | -0.046202 | 0.000268336 |
| 3 | complex | 1000 | -0.0576945 | 0.000650627 |
| 4 | real | 1000 | -0.00441747 | 0.0010123 |
| 4 | complex | 1000 | -0.0400624 | 0.00149906 |
| 6 | real | 1000 | -0.167975 | 0.00544162 |
| 6 | complex | 1000 | -0.225247 | 0.00721675 |
| 8 | real | 600 | -0.0403259 | 0.00384451 |
| 8 | complex | 600 | -0.154331 | 0.0122597 |
| 10 | real | 300 | -0.17989 | 0.00945036 |
| 10 | complex | 300 | -0.207584 | 0.0271946 |
| 12 | real | 100 | -0.315359 | 0.0338471 |
| 12 | complex | 100 | -0.266071 | 0.0157808 |
| 14 | real | 30 | -0.673517 | 0.0445225 |
| 14 | complex | 30 | -0.416349 | 0.0411526 |

**Optimization of full Hessians.** Three starts for each row. Code: search.py; data: [data/search.json](data/search.json). The high-precision column evaluates the saved best direction, rather than reoptimizing it.

| n | field | evaluations | converged starts / 3 | double maximum | 120-digit evaluation |
| --- | --- | --- | --- | --- | --- |
| 3 | real | 1348 | 3 | 1.57119e-12 | -3.24397e-13 |
| 3 | complex | 3000 | 0 | 2.82126e-15 | -1.08871e-15 |
| 4 | real | 2688 | 2 | 2.58876e-14 | -1.89618e-15 |
| 4 | complex | 3000 | 0 | -0.000195699 | -0.000195699 |
| 5 | real | 3000 | 0 | -2.16991e-10 | -2.16991e-10 |
| 5 | complex | 3000 | 0 | -0.0144252 | -0.0144252 |

**Optimization in circulant symbols.** Three starts for each row. Code: targeted_search.py; data: [data/targeted.json](data/targeted.json) and [data/verification.json](data/verification.json).

| n | field | evaluations | double maximum | 120-digit evaluation |
| --- | --- | --- | --- | --- |
| 3 | real | 447 | 9.16296e-15 | -1.07478e-15 |
| 3 | complex | 556 | 4.83973e-15 | -7.5599e-16 |
| 4 | real | 448 | 3.35692e-13 | -1.50026e-15 |
| 4 | complex | 1016 | 9.69991e-16 | -8.50303e-16 |
| 6 | real | 974 | 2.89051e-14 | -1.44565e-15 |
| 6 | complex | 2262 | 7.38884e-10 | -1.19961e-11 |
| 8 | real | 2000 | 1.44518e-14 | -3.64278e-14 |
| 8 | complex | 2582 | 7.10538e-12 | -6.35178e-13 |

**Genuine rank-two midpoint differences.** Minimum midpoint gaps among 100 tests of each signature. Code: targeted_search.py; data: [data/targeted.json](data/targeted.json).

| n | field | positive direction | indefinite direction |
| --- | --- | --- | --- |
| 3 | real | 0.00148952 | 0.00120196 |
| 3 | complex | 0.00183889 | 0.00185582 |
| 4 | real | 0.00205156 | 0.00074363 |
| 4 | complex | 0.00165598 | 0.000766196 |
| 6 | real | 0.00105652 | 0.000458749 |
| 6 | complex | 0.000794909 | 0.00024757 |
| 8 | real | 0.000710574 | 0.000342114 |
| 8 | complex | 0.000690889 | 0.000388924 |
| 10 | real | 0.000460203 | 0.000304269 |
| 10 | complex | 0.000491846 | 0.000264053 |

**Independent checks.** Code: audit_two_point.py, verify.py, verify_structural.py, and verify_product.py. Data: data/two_point_symbolic.txt, data/verification.json, data/structural_verification.json, and data/product_verification.json.

| check | largest absolute discrepancy |
| --- | --- |
| two-point polynomial identity | exact zero |
| atoms: signed determinants versus principal-minor inclusion-exclusion | 3.30329e-16 |
| curvature: compiled directional formula versus full Hessian | 1.24345e-14 |
| normalization of atom probabilities | 6.66134e-16 |
| normalization of first/second atom derivatives | 2.33195e-15 |
| conditioning formula | 1.11022e-15 |
| conditional entropy chain rule | 8.88178e-16 |
| product-kernel quartic coefficient | 7.10543e-15 |
| product-kernel Hessian | 1.15463e-13 |
| direct 100-digit second derivative versus Jacobi formula | 3.715e-96 |
| direct 100-digit fourth derivative versus product formula | 0.0 |

The 80- and 120-digit curvature evaluations agree to an absolute discrepancy at most 3.1996e-77. Every checked optimized direction has strictly negative high-precision curvature.

**Product-kernel sharp constants.** Twenty real and twenty complex tests per dimension. Code: verify_product.py; data: [data/product_verification.json](data/product_verification.json). The equality column uses all off-diagonal pairs.

| n | bound for unit Frobenius norm | equality example | smallest random coefficient / bound |
| --- | --- | --- | --- |
| 2 | 2 | 2 | 1.0196 |
| 3 | 0.666667 | 0.666667 | 1.28735 |
| 4 | 0.333333 | 0.333333 | 1.43463 |
| 6 | 0.133333 | 0.133333 | 1.69204 |
| 8 | 0.0714286 | 0.0714286 | 2.32207 |

Main search: 73.19 seconds, peak RSS 98.88 MiB. Targeted search: 26.41 seconds, peak RSS 89.55 MiB. Timings describe this host and exclude source downloads and high-precision verification. The searches have no rejected evaluations recorded.

## 8. Literature and attribution

The finite conjecture is [Conjecture 9.2 of Lyons (2003)](https://www.numdam.org/item/10.1007/s10240-003-0016-0.pdf), in Section 9, rather than Section 5. It is Conjecture 2.6 in his [ICM 2014 survey](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf); the stationary entropy-rate version is Conjecture 5.3 of that survey. The stationary conjecture also appears as Conjecture 9.2 in [Lyons and Steif (2003)](https://rdlyons.pages.iu.edu/pdf/dyn.pdf).

The primary sources consulted, including later work found by searches through 13 November 2026, are listed below. Search phrases and scope are recorded in [sources/literature_search.md](sources/literature_search.md). A web search cannot certify the absence of a result from the entire literature.

| Source | Relevant content and limitation |
|---|---|
| [Lyons, *Determinantal probability measures*, 2003](https://www.numdam.org/item/10.1007/s10240-003-0016-0.pdf) | Original finite concavity conjecture; Section 13 relates it to stationary entropy. |
| [Kulesza–Taskar, *Determinantal Point Processes for Machine Learning*, 2012](https://arxiv.org/abs/1207.6083) | Section 7.1 explicitly records finite kernel-entropy concavity as an open question. |
| [Lyons, *Determinantal probability: basic properties and conjectures*, 2014](https://arxiv.org/abs/1406.2707) | States both the finite and entropy-rate conjectures. |
| [Hillion–Johnson, *A proof of the Shepp–Olkin entropy concavity conjecture*, 2017](https://arxiv.org/abs/1503.01570) | Concavity of entropy of a sum of independent Bernoulli variables; this controls DPP cardinality entropy, rather than the full configuration entropy. |
| [Gu, *Entropy of Determinantal Point Processes*, undated course report](https://sevenkplus.com/data/dpp.pdf) | Theorem 1 concerns cardinality entropy, Corollary 6 gives the endpoint thinning inequality, and Theorem 7 proves rank-one concavity. The PDF is an unrefereed six-page report. |
| [Mészáros, *Limiting entropy of determinantal processes*, 2020](https://arxiv.org/abs/1905.11459) | Entropy limits under convergence and sofic entropy; its results are not a finite kernel-concavity theorem. |
| [Alishahi–Barzegar, *Paving Property for Real Stable Polynomials and Strongly Rayleigh Processes*, 2020/2021](https://arxiv.org/abs/2006.13923) | Section 4.3 gives an entropy lower bound using kernel-polynomial roots. A lower bound by a concave spectral expression does not imply concavity of the entropy itself. |
| [Hino–Yano, *An embedding structure of determinantal point process*, 2025; preprint 2024](https://doi.org/10.1007/s41884-024-00156-x) | Information geometry and marginal/\(L\)-kernel duality; not a proof of the conjectured Shannon entropy Hessian sign. |
| [Ercan, *Lorentzian entropy, subgaussian matrix concentration, and sharp functional inequalities for all matroids*, 2026 preprint](https://arxiv.org/abs/2611.00626) | Studies entropy contraction and functional inequalities for Lorentzian laws. These are different variations from affine variation of the marginal DPP kernel. No theorem settling the present conjecture was identified. |
| [the author, *Concavity of the entropy of determinantal measures on two points, and the second variation in general*, November 2026 preprint](https://github.com/yspennstate/lyons-determinantal-entropy-two-points/blob/main/paper/main.tex) | Already proves the two-point theorem and the off-block fourth-order expansion, including a sharp lower bound \(2\|A\|_F^4/[k(n-k)]\) for the subtracted quartic coefficient. Its saved source is [sources/prior_2026_prior.tex](sources/prior_2026_prior.tex), blob SHA in the adjacent metadata JSON. |

The search also covered strong Rayleigh entropy and log-concavity terminology. Neither strong Rayleigh negative dependence nor ordinary entropy concavity in the probability vector makes the polynomial map \(Q\mapsto P_Q\) affine. No general finite or stationary solution was identified in the consulted sources. The partial results above should not be described as a resolution of Lyons's conjecture.

## 9. Remaining questions

- The full three-point problem, real symmetric and complex Hermitian, remains unresolved here. Formula (16) gives an explicit starting point.
- General rank-two directions remain unresolved. The proved two-coordinate theorem cannot be transferred to them by arbitrary unitary conjugation.
- General commuting kernels remain unresolved here. Coordinate-diagonal and coordinate block diagonal families with blocks of size at most two are proved.
- General finite circulant kernels, finite Toeplitz restrictions, and entropy-rate concavity in the symbol remain unresolved.
- The local formulas give no uniform global Hessian bound: the Hessian vanishes on every zero-diagonal direction at a product kernel. A global argument must control curvature beyond this degeneracy.

Task: “Open problem C0033: concavity of the entropy of determinantal measures in the kernel” — received 13 November 2026, approximately 01:35, Asia/Tbilisi.
