COUNTEREXAMPLE

# C0101: a counterexample for literal Loewner maximality

**Scope of the result.** If “maximal element” has its usual meaning for the Loewner order, there are irrational, non-isolated maximal elements in every dimension $d\ge3$. An explicit example and its proof follow. There is a terminology problem in the question: the statement that all two-dimensional maximal elements correspond to packing circles omits residual maximal elements of the closed set. The counterexample uses precisely those residual elements. It does **not** disprove rationality or isolation of the more restrictive circle-type **cone peaks** apparently intended by the survey. No resolution of that stronger question was found in the literature search or established here.

The result below is an elementary consequence of the corrected LPS characterization together with a zero-coordinate reduction proved here. No novelty claim is made. The calculations are exact; decimals are included only to identify the example.

## 1. Definitions, sources, and the distinction that matters

Use
\[
\Delta g(x)=\sum_{i=1}^d[g(x+e_i)+g(x-e_i)-2g(x)],\qquad q_A(x)=\tfrac12x^TAx.
\]
Write $\Gamma_1^d$ for the closed obstacle class: a symmetric real matrix $A$ belongs when there is an integer-valued $g$ with
\[
\Delta g\le1,\qquad g(x)\ge q_A(x)+b\cdot x+c
\]
for some real $b,c$. The contact/compactness argument below shows this class is closed. The asymptotic definition in LPS, $g=q_A+o(|x|^2)$, gives the same two-dimensional class; an asymptotic representative also supplies obstacles for $A-\eta I$, hence an obstacle representative for $A$ by closure. Every computed certificate satisfies the stronger affine-periodic condition
\[
g(x)=q_A(x)+b\cdot x+p(x),\qquad p\text{ bounded and periodic}.
\]
Periodicity is a sufficient certificate, not part of the general definition.

The survey defines allowed Hessians through local stabilization with stable heights at most (2d-1). This is the corresponding obstacle class with $\Delta g\le2d-1$, after closure. Integer quadratics translate between thresholds. In dimension three, set
\[
S=\operatorname{diag}(2,1,1),\qquad
p_S(x)=2\binom{x_1}{2}+\binom{x_2}{2}+\binom{x_3}{2}.
\]
Then $\Delta p_S=4$, so the survey's set is $S+\Gamma_1^3$. Translation preserves maximality, isolation, and rationality. Add $S$ to the example below to express it in that convention. Affine obstacle terms cause no problem: for any $\eta>0$, they are absorbed into the lower obstacle $q_{A-\eta I}$ by changing its constant.

For the rest of the report, maximal means
\[
A\in\Gamma_1^d,\quad B\in\Gamma_1^d,\ B-A\succeq0\ \Longrightarrow\ B=A.
\]
An element is isolated if a neighborhood contains no other maximal elements. A cone peak is a stronger notion; this report does not identify the two.

The core sources are:

- Levine–Peres, *Laplacian growth, sandpiles and scaling limits*, Bull. AMS 54 (2017), 355–382, [arXiv:1611.00411](https://arxiv.org/abs/1611.00411), §6 and open problem (4), preprint p.27.
- Levine–Pegden–Smart, *The Apollonian structure of integer superharmonic matrices*, Annals of Mathematics 186 (2017), 1–67, [arXiv:1309.3267v4](https://arxiv.org/abs/1309.3267v4), Theorems 1.1–1.2 and Lemma 3.4. **Use the corrected v4 formula:** in the $\Delta\le1$ normalization the additional half-space is $\operatorname{tr}A\le0$. The publisher PDF still prints 2 in Theorem 1.1, inconsistent with its own normalization and the universal trace bound. Both versions have been saved as text.
- Levine–Pegden–Smart, *Apollonian structure in the Abelian sandpile*, GAFA 26 (2016), 306–336, [arXiv:1208.4839](https://arxiv.org/abs/1208.4839). The supplied identifier 1608.00064 belongs to a neuroscience paper; 1208.4839 is the intended sandpile source.

The corrected LPS theorem says
\[
\Gamma_1^2=\{A:\operatorname{tr}A\le0\}\ \cup\ \bigcup_{C\in\mathcal B}\{A:A\preceq A_C\},
\qquad
A_C=\tfrac12\begin{pmatrix}r_C+a_C&b_C\\b_C&r_C-a_C\end{pmatrix}.
\tag{1}
\]
Here proper circles of the band packing have rational centers and radii. The paragraph after Theorem 1.1 explicitly retains residual trace-zero points outside the circle downsets. Such a point is Loewner maximal: any nonzero positive semidefinite improvement has positive trace and, by (1), would be below a circle matrix, contradicting the residual point's exclusion from every such downset. Thus the survey's identification of all maximal elements with circles requires a qualification even in dimension two.

These matrices matter because they specify the admissible Hessians in the fully nonlinear obstacle problem governing the sandpile scaling limit. They retain lattice information that the ordinary Laplacian loses. The survey's §6 gives the viscosity interpretation; the GAFA paper constructs fractal PDE solutions using the two-dimensional circle structure. A periodic certificate describes a microscopic periodic Laplacian pattern, rather than a complete single-source scaling-limit solution.

## 2. Exact counterexample

Let
\[
t=\sqrt{\sqrt5-2},\qquad a=1-t,\qquad b=t^3+4t-1=\sqrt{\sqrt5+2}-1.
\]
Define
\[
A_*=
\frac12\begin{pmatrix}
1-t&t^3+4t-1&0\\
t^3+4t-1&t-1&0\\
0&0&0
\end{pmatrix}.
\tag{2}
\]
The point $(a,b)$ is approximately
\[
(0.5141317282433543218171361241,\ 1.0581710272714922503219810476).
\]

**Theorem.** $A_*$ is an irrational, non-isolated Loewner-maximal element of $\Gamma_1^3$. Its zero extension is likewise maximal and non-isolated in every larger dimension. Its translate $S+A_*$ has the same properties in the survey's three-dimensional normalization.

### 2.1 An exact sequence of packing circles

Use curvature-center coordinates $(c,u,v)$, meaning center $(u/c,v/c)$ and radius $1/c$. Start with the three mutually tangent proper circles
\[
C_1=(1,1,0),\qquad C_2=(1,1,2),\qquad C_3=(4,1,4),
\]
and their other Soddy circle, the oriented line $E=(0,-1,0)$. At each step form
\[
D=2(C_1+C_2+C_3)-E,
\]
replace $C_j$ by $D$, replace $E$ by the old $C_j$, and cycle $j=1,2,3,1,2,3,\ldots$. This inserts the inner Soddy circle in a nested packing gap. The curvatures strictly increase, so all inserted circles are distinct members of the band packing.

Over a complete three-step cycle, each coordinate column is multiplied by
\[
T=\begin{pmatrix}
2&2&2&-1\\3&6&6&-2\\10&15&18&-6\\0&0&1&0
\end{pmatrix},
\qquad
p(z)=\det(zI-T)=z^4-26z^3+46z^2-26z+1.
\tag{3}
\]
Since $p(z)/z^2=(z+z^{-1})^2-26(z+z^{-1})+44$, there is a unique dominant eigenvalue $\lambda>1$: the other roots are $\lambda^{-1}$ and two roots of modulus one. In the field $\mathbb Q(t)$,
\[
\lambda=(11t^3+5t^2+47t+23)/2\in(24,25).
\]
A left eigenvector, with variable $z$ evaluated at $\lambda$, is
\[
w(z)=(z^3-24z^2+24z-6,\ 2z^2-6z-3,\ 2z^2-z+2,\ -z^2+8z-6).
\]
Its products with the initial curvature, horizontal-center, and vertical-center columns are
\[
\begin{aligned}
d(z)&=z^3-14z^2+14z-1,\\
n_x(z)&=z^3-19z^2+9z-1,\\
n_y(z)&=12z^2-16z+2.
\end{aligned}
\]
The nonzero dominant projection therefore gives limiting centers
\[
\lim (u_n/c_n,v_n/c_n)
=(n_x(\lambda)/d(\lambda),n_y(\lambda)/d(\lambda))=(a,b),
\qquad 1/c_n\longrightarrow0.
\tag{4}
\]
The identities in (3)–(4) are checked by polynomial reduction modulo $t^4+4t^2-1$, not by numerical fitting. The dominant projection of the curvature column is nonzero since $d(\lambda)>0$.

Every fixed proper packing circle is disjoint from all but possibly one circle of this sequence. Consequently its center $q$ and radius $r$ satisfy $|(a,b)-q|\ge r$ by taking limits of the external-disjointness inequalities.

### 2.2 The limit lies on no rational circle

The polynomial $t^4+4t^2-1$ is irreducible over $\mathbb Q$. One direct proof: $t^2=\sqrt5-2$ generates $\mathbb Q(\sqrt5)$, and this element has norm (-1), so it cannot be a square in that real quadratic field. Hence $1,t,t^2,t^3$ are linearly independent over $\mathbb Q$.

Reduction modulo that polynomial gives
\[
a^2+b^2=6-10t+2t^2-2t^3.
\]
The four elements $1,a,b,a^2+b^2$ are linearly independent: the last has a nonzero $t^2$ coefficient, while the first three do not; the first three themselves are independent. Their coefficient matrix has determinant 2. A rational circle equation would be a nonzero relation
\[
a^2+b^2+u a+v b+w=0,\qquad u,v,w\in\mathbb Q,
\]
which is impossible. Thus all the preceding circle-distance inequalities are strict: ((a,b)) is outside every closed proper packing disk. Both $a$ and $b$ are irrational.

Set $C_*=\frac12\left(\begin{smallmatrix}a&b\\b&-a\end{smallmatrix}\right)$. It has trace zero and belongs to $\Gamma_1^2$ by (1). The PSD criterion $C_*\preceq A_C$ is exactly $|(a,b)-(a_C,b_C)|\le r_C$, which has just been excluded. The observation after (1) proves that $C_*$ is maximal.

### 2.3 Why zero extension preserves this maximality

The necessary reduction lemma is proved in §3. It says that if $C$ is maximal and
\[
\sum_i\lceil C_{ii}\rceil=1,
\tag{5}
\]
then $C\oplus0$ is maximal in every larger dimension. Here (0<a<1), so
$\lceil a/2\rceil+\lceil-a/2\rceil=1$; the lemma applies to $C_*$.

Each proper LPS circle matrix has positive trace and ceiling sum one, so its zero extension is also maximal. The rational matrices from the sequence in §2.1 converge to (2), by (4). They are distinct, of positive trace, while $A_*$ has trace zero. This proves non-isolation. It also explains why this example is a residual maximal point rather than a circle-type peak.

## 3. Structural lemmas and their proofs

### 3.1 Contact normalization and closure

Suppose an integer $H$ has a lower quadratic obstacle $q_D+b_0\cdot x+c$. Choose $x_0$ within $\varepsilon$ of the infimum of $H-q_D-b_0\cdot x$. Translate $x_0$ to zero, subtract $H(x_0)$, and subtract an integer linear function. The resulting integer function $h$ satisfies
\[
h(0)=0,\qquad h(x)\ge q_D(x)+b\cdot x-\varepsilon,
\qquad |b_i|\le1/2.
\tag{6}
\]
Its Laplacian bound is unchanged.

For a convergent sequence of obstacle matrices, (6) gives uniform lower bounds on every finite set. The inequality $\Delta h\le K$ gives an upper bound at a neighbor from an upper bound at the current point and lower bounds at its other neighbors. Starting at $h(0)=0$, this bounds every fixed finite ball above as well. Integer-valuedness, a diagonal subsequence, and compactness of the slopes give an integer pointwise limit with the limiting obstacle and Laplacian inequality. This proves closure in every dimension and justifies the contact limits below. No periodicity is assumed.

### 3.2 The ceiling bound and complete diagonal slice

For every $A\in\Gamma_1^d$,
\[
\boxed{\sum_i\lceil A_{ii}\rceil\le1.}
\tag{7}
\]
To prove this, put $k_i=\lceil A_{ii}\rceil$, $K=\operatorname{diag}(k_i)$, and $s=\sum k_i$. Subtract the integer quadratic $p_K=\sum k_i\binom{x_i}{2}$. If $s\ge2$, the residual satisfies $\Delta H\le1-s<0$, and the diagonal entries of its lower-obstacle Hessian $D=A-K$ lie in ((-1,0]). Normalize a contact as in (6). For sufficiently small $\varepsilon$, the lower obstacle at every $\pm e_i$ is strictly greater than (-1), because $|b_i|\le1/2$ and $D_{ii}>-1$. All these integer neighbor values are therefore nonnegative. With $h(0)=0$, this contradicts $\Delta h(0)<0$.

For diagonal matrices (7) is sufficient as well. For real $a_i$, put $k_i=\lceil a_i\rceil$ and $p_i=k_i-a_i\ge0$. If (p>0), the integer convex function
\[
F_p(n)=\sup_{m\in\mathbb Z}\{mn-\lceil m^2/(2p)\rceil\}
\]
satisfies
\[
pn^2/2-1-1/(8p)\le F_p(n)\le pn^2/2.
\]
The lower bound follows by choosing an integer $m$ within (1/2) of (pn). Set $F_0=0$. Then
\[
g(x)=\sum_i[k_i\binom{x_i}{2}-F_{p_i}(x_i)]
\]
is integer, has $\Delta g\le\sum k_i$, and has quadratic growth $\operatorname{diag}(a_i)$, with a bounded error after an affine term. Thus
\[
\boxed{\operatorname{diag}(a_1,\ldots,a_d)\in\Gamma_1^d
\iff \sum_i\lceil a_i\rceil\le1.}
\tag{8}
\]
Its maximal diagonal matrices are exactly the integer diagonal matrices of trace one. Each is also maximal in the full matrix space.

### 3.3 Zero-coordinate reduction

If a $k\times k$ matrix $C$ has ceiling sum one, then
\[
C\oplus0_{d-k}\in\Gamma_1^d\quad\Longleftrightarrow\quad C\in\Gamma_1^k.
\tag{9}
\]
The reverse implication is constant extension of a representative.

For the forward implication, subtract $p_K$, where $K=\operatorname{diag}(\lceil C_{11}\rceil,\ldots,\lceil C_{kk}\rceil,0,\ldots,0)$. Its Laplacian is one, so the residual is integer superharmonic with bound zero. At normalized contacts, the neighbor argument in §3.2 now forces all neighbor values to zero. In each added zero direction, (6) consequently gives $|b_j|\le\varepsilon$. Let $\varepsilon\downarrow0$ and use §3.1. The limit (h(x,z)) satisfies
\[
\Delta h\le0,\qquad h(x,z)\ge q_{C-K}(x)+b\cdot x,
\]
with no affine term in the added variables $z$.

For each $x$, the integer minimum $H(x)=\min_{z\in\mathbb Z^{d-k}}h(x,z)$ is finite and attained. At a minimizing $z$, $\Delta_z h\ge0$, while neighboring minima give $\Delta_x H\le\Delta_x h$. Hence $\Delta H\le0$. Add back the $k$-dimensional integer quadratic to obtain a representative for $C$.

Now suppose $C$ is maximal and has ceiling sum one. If $B\succeq C\oplus0$ is admissible, any positive added diagonal entry would raise the ceiling sum to at least two, contrary to (7). All added diagonal entries of the PSD difference therefore vanish. Its corresponding rows and columns vanish as well, so $B=C'\oplus0$ with $C'\succeq C$. Monotonicity of ceilings and (7) give ceiling sum exactly one for (C'). By (9), $C'\in\Gamma_1^k$, and maximality gives $C'=C$. This proves the lifting assertion used in §2.

### 3.4 A rational isolated family

Every integer symmetric matrix $M$ of trace one is maximal, with integer representative
\[
p_M(x)=\sum_i M_{ii}\binom{x_i}{2}+\sum_{i<j}M_{ij}x_ix_j,
\qquad\Delta p_M=1.
\]
Every admissible matrix has trace at most one. For an obstacle representative, subtract $q_A+b\cdot x+c$ and use simple random walk: if $\operatorname{tr}A>1$, its bounded-below difference has a uniformly negative Laplacian, whose expectation would decrease without bound. This is impossible. A nonzero PSD improvement of $M$ would increase trace, proving maximality.

In fact $M$ is the only maximal element in the operator-norm ball of radius (1/(10d)) about $M$. Here is a quantitative proof. Suppose integer $H$ satisfies $\Delta H\le0$ and has a lower obstacle of Hessian $D$, with $\delta=\|D\|_{op}<1/(10d)$. Normalize (6). All neighbor values are nonnegative and hence zero, so $|b_i|\le\varepsilon-D_{ii}/2\le\varepsilon+\delta/2$.

If $Dv=\lambda v$ with $\lambda>0$, choose the sign of the unit vector $v$ so $b\cdot v\ge0$. Follow the ray (tv), $t\ge0$, by a nearest-neighbor lattice path, ordering simultaneous coordinate crossings arbitrarily. Path vertices are within $\sqrt d/2$ of the ray; they and their neighbors are within $2\sqrt d$. For $x=tv+e$, $|e|\le2\sqrt d$, completing the square gives
\[
q_D(x)+b\cdot x-\varepsilon
\ge-5d\delta-(2d+1)\varepsilon>-1
\]
when $\varepsilon$ is sufficiently small. Thus $h\ge0$ on the path and all its neighbors. Starting from $h(0)=0$, the superharmonic inequality forces successive path values to be zero. But its lower quadratic obstacle grows to infinity along that positive eigendirection, a contradiction. Therefore $D\preceq0$.

Apply this to $H=g_B-p_M$. Any admissible $B$ sufficiently close to $M$ satisfies $B\preceq M$, proving the isolation statement. In dimension three the explicit radius is (1/30). This radius is not claimed optimal.

## 4. Algorithms, validation, and exploration

### Periodic membership search

For rational $A$, choose $N$ and $b$ with
\[
NA\text{ integral},\qquad N^2A_{ii}/2+Nb_i\in\mathbb Z.
\]
Then $f_0=\lceil q_A+b\cdot x\rceil$ has a periodic Laplacian. Search for integer $N$-periodic $u$ with $\Delta(f_0+u)\le1$, by legal parallel topplings on the torus. This is finite-volume least action. If every vertex has toppled, no periodic stabilizer exists for that period and affine phase: otherwise normalize a stabilizer to have minimum zero, and least action would prevent its zero vertex from toppling.

Affine phases are essential. They are reduced modulo integer slopes and translations using HNF of the lattice generated by $[NA\mid NI]$. A failed search at one period, even with all phases exhausted, does not exclude a nonperiodic representative or a larger period.

The independent verifier uses Python integers and rational arithmetic at every torus site, checks quasi-periodic integrality, and checks that the mean Laplacian equals the trace. Positive certificates contain $A,N,b,u$. There are no floating acceptance tolerances.

A full-rank affine-periodic integer representative necessarily has rational $A$: for a lattice basis $V$, integer-valued affine increments force (AV) integral. Thus such searches cannot certify an irrational representative. At trace one the periodic Laplacian must be identically one, and its periodic harmonic correction is constant; integer second and mixed differences then force $A$ itself integral.

### Saved results

| Experiment | Result |
|---|---:|
| Generated 2D packing circles, curvature at most 100 in the recorded window | 501 |
| Selected known rational maximal circle points, curvature at most 25 | 24/24 certified |
| Trace-(1/4), $9\times9$ validation grid | all 38 LPS members certified; no false positives |
| 3D diagonal grid modulo permutations | 165 tests; all agree with (8) |
| All 3D slice and rank-one tests | 317 |
| Exact 3D positive certificates | 165 |
| Initial fixed-period exclusions | 101 |
| Initial trace exclusions | 51 |

The 3D tests used diagonal matrices, $tI+s(e_1e_2^T+e_2e_1^T)$, and
\[
\begin{pmatrix}1/4+\delta&1/2&0\\1/2&\delta&0\\0&0&c\end{pmatrix},
\]
plus 26 positive rank-one perturbations of the lifted Ford point. The periodic exclusions are labeled separately from global obstructions. The ceiling bound independently excludes 146 of the 317 samples. In particular, every negative diagonal sample is now a genuine nonmember by (8). The identity-plus-shear slice has the exact answer $t\le0$: necessity follows from (7); sufficiency follows by lifting the trace-nonpositive 2D block from (1) and adding a concave integer one-dimensional representative.

One explicit rational maximal member is the lifted Ford matrix
\[
F=\begin{pmatrix}1/4&1/2&0\\1/2&0&0\\0&0&0\end{pmatrix},
\qquad
g(x,y,z)=\left\lceil x^2/8+xy/2+y/2\right\rceil+\mathbf1_{x\text{ even}}.
\]
An exact period-eight certificate and direct translated checks are saved. Its maximality follows from LPS and §3.3, rather than the failed perturbation searches.

The algebraic counterexample program checked 120 exact Descartes steps, pairwise tangency identities, the characteristic polynomial, irreducibility, eigenvector ratios, and the rational-circle exclusion. Eighty-digit values were computed after these exact checks. All 190 saved periodic certificates (24 validation, 165 exploration, one explicit Ford certificate) were independently reverified. The integer-quadratic Laplacian was also checked symbolically.

The 3D search and independent verification took about 24.2 seconds with one compute thread, maximum period 16 and 4096 sites. Reported peak RSS was 62,111,744 bytes. Processes inherited nice 15, satisfying the nice-at-least-10 requirement. No subagents, pushes, publications, or writes outside this directory were used.

## 5. Literature outcome and remaining problem

The 2016–2026 search did not locate a printed higher-dimensional classification or a theorem settling rationality/isolation of cone peaks on the nearest-neighbor cubic lattice. Search details and scope limitations are in [sources/LITERATURE.md](sources/LITERATURE.md). In particular:

- Pegden–Smart, *Stability of patterns in the Abelian sandpile*, Ann. Henri Poincare 21 (2020), 1383–1399, [arXiv:1708.09432](https://arxiv.org/abs/1708.09432), proves pattern stability/convergence using the two-dimensional theory.
- Bou-Rabee, *Convergence of the random Abelian sandpile*, Ann. Probab. 49 (2021), 3168–3196, [arXiv:1909.07849](https://arxiv.org/abs/1909.07849), develops scaling limits with an implicit effective operator. *Dynamic dimensional reduction in the Abelian sandpile*, CMP 390 (2022), 933–958, [arXiv:2009.05968](https://arxiv.org/abs/2009.05968), concerns specified hypercube initial conditions.
- Bou-Rabee, *Integer superharmonic matrices on the F-lattice*, Adv. Math. 436 (2024), 109400, [arXiv:2110.07556](https://arxiv.org/abs/2110.07556), classifies a different directed planar graph. Its irrational boundary points are not automatically maximal.
- Kalinin, *Sandpile solitons in higher dimensions*, Arnold Math. J. 9 (2023), 435–454, treats piecewise affine huskings/solitons; its introduction notes the missing higher-dimensional quadratic-pattern classification.
- Kalinin–Shkolnikov, *Tropical curves in sandpile models*, Adv. Math. 502 A (October 2026), 111127, [arXiv:1502.06284](https://arxiv.org/abs/1502.06284), treats small perturbations on the square lattice.

A general description of the genuinely higher-dimensional cone peaks remains unproved here. The counterexample above answers the literal Loewner-order formulation; it should not be presented as resolving a strengthened peak formulation without first specifying that definition.

## 6. Reproduction and files

Python packages: numpy, sympy, matplotlib, pypdf. From this directory, with one thread:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
python3 code/validate_2d.py
python3 code/explore_3d.py
python3 code/algebraic_counterexample.py
python3 code/figures_and_audit.py
```

Retain inherited nice priority if already at least 10; otherwise launch these commands at nice 10. Source retrieval is separately reproducible with `python3 code/fetch_sources.py`; PDFs are read into memory and only extracted text and hashes are retained.

Key artifacts: [algebraic certificate]$data/algebraic_counterexample.json$, [audit summary]$data/audit_summary.json$, [explicit Ford certificate]$data/explicit_ford_certificate.json$, [3D classified samples]$data/exploration_3d_classified.json$, [Apollonian validation]$data/apollonian_validation.svg$, [3D slices]$data/slices_3d.svg$, [counterexample convergence]$data/counterexample_convergence.svg$, and [research log](LOG.md).

Task: “Open problem C0101” — received 2026-11-13 06:13 +04.
