PARTIAL

# D0040: nested beta ensembles

Task: “Open problem D0040.” Received 2026-11-13 09:52 +04 (Asia/Tbilisi).

## Statement and scope of the result

There is a nested tridiagonal model for every beta-Laguerre family with a fixed hard-edge exponent. This follows by a reversal and transpose from Dumitriu–Edelman's finite-size theorem; it is not a new finite-size matrix model. A second positive example is the antisymmetric Gaussian beta ensemble. The requested general classification, including arbitrary dependent Jacobi models for fixed beta-Jacobi weights and general one-cut potentials, is not established here, and the literature located does not settle that stronger question. Thus the status is PARTIAL, not RESOLVED_IN_LITERATURE.

Several distinctions are essential:

* One matrix for each size is weaker than one infinite matrix whose actual leading blocks have the required laws.
* An interlacing array with specified one-level laws is weaker than a matrix representation of that array with a fixed bandwidth.
* Virág's nested Hermite construction and the full beta-Hermite corners process have different joint laws, despite having the same one-level marginals and the same adjacent two-level laws.
* A parameter that measures a Wishart matrix's number of columns is different from the hard-edge exponent. Parameters must be tracked when taking minors.

The statements proved below include the Laguerre construction, a dimension obstruction for full corners processes, parameter shifts under Dixon–Anderson links, two restricted Gaussian characterizations, failure of a reversed Jacobi candidate, and an obstruction for ordinary unitary principal minors. None of the restricted obstructions is presented as a classification of all possible random Jacobi matrices.

## Exact source and meaning of the question

Source: Bálint Virág, [*Operator limits of random matrices*](https://arxiv.org/abs/1804.06953), dated May 25, 2014, uploaded April 2018; ICM Seoul 2014 proceedings. The retained text is [sources/virag_2014.txt](sources/virag_2014.txt). All page numbers below refer to the explicitly identified downloaded PDF, counted from 1, unless stated otherwise.

Question 2, PDF p.6, reads:

> Can any other Dyson β-ensembles be coupled this way? How about other natural random matrix models?

“This way” refers back to Section 4, Theorem 4.1, PDF p.5: a single random orthogonality measure whose degree-n orthogonal polynomial has the beta-Hermite eigenvalue law for every n. Equivalently, its recurrence coefficients form one semi-infinite Jacobi matrix with the required leading-minor spectra. The paragraph preceding that theorem explicitly reverses the numbering in equation (1). The source does not require the full Dixon–Anderson Gibbs law on all levels. Adding that requirement would exclude even the source's own tridiagonal construction.

Use common, unscaled spectral units. For example, the Hermite law here is

\[
 H_{n,\beta}(dx)=Z^{-1}_{n,\beta}\Delta(x)^\beta
       \exp\{-\tfrac\beta4\sum_i x_i^2\}\,dx,
 \qquad x_1<\cdots<x_n.
\]

Virág removes the size-dependent normalization by considering \(\sqrt n\,T_n\). Dividing each size by its own \(\sqrt n\), or imposing the convention \(e^{-n\beta\sum V/2}\), does not preserve literal principal blocks. The same scale distinction is needed outside the Gaussian case.

## Literature first: what is established, and what it implies

The search and source acquisition preceded the proofs and simulation. LOG.md records the sequence. The table gives exact locations in the versions retained here; an arXiv page number is not silently identified with a journal page number.

| Work and retained version | Exact location | Result relevant here; limitation |
|---|---|---|
| [Virág, ICM 2014 / arXiv:1804.06953](https://arxiv.org/abs/1804.06953) | Theorem 4.1, PDF p.5; Question 2, p.6 | One random measure / infinite Jacobi matrix for the Hermite laws. |
| [Dumitriu–Edelman, 2002](https://arxiv.org/abs/math-ph/0206043), 22-page version | Theorem 2.12, PDF p.12; Theorem 3.4, p.14; bidiagonal matrix immediately above Theorem 3.4 | Hermite and Laguerre matrix models, with independent Dirichlet spectral weights at the designated endpoint. The Laguerre theorem implies the nested construction proved below after transpose and reversal. |
| [Killip–Nenciu, 2004](https://arxiv.org/abs/math/0410034), 28-page version | Theorem 1, PDF p.3; Theorem 2, pp.4–5, equations (1.11)–(1.13) | All-beta finite CMV models for the circular ensemble and finite tridiagonal models for Jacobi. The distributions and terminal boundary conditions depend on size; the theorems alone do not give an infinite principal-block coupling. The Jacobi matrix entries are functions of independent beta variables, not mutually independent entries. |
| [Edelman–Sutton, 2008, author manuscript](https://math.mit.edu/~edelman/publications/beta-jacobi.pdf), 25 pages | Definitions 1.6 and 1.8, PDF pp.7–8; Theorem 4.1, p.17 | Beta-Jacobi via a bidiagonal block orthogonal matrix and CS decomposition, for all beta>0 and a,b>−1. This is a finite-size singular-value model, not a theorem about its leading principal blocks at every size. |
| [Forrester–Rains, 2005](https://arxiv.org/abs/math-ph/0211042), 49-page version | Section 4.2, PDF pp.22–27, especially (4.35)–(4.38), p.26; Section 5.2, pp.31–32; Theorem 5, p.36 | Random recurrences and two-level interlacing laws. The Jacobi recurrence has an x(x−1) coefficient and terminal-size-dependent parameters; it is not the ordinary three-term characteristic-polynomial recurrence of one Jacobi matrix. Theorem 5 supplies a tridiagonal two-level Hermite model. |
| [Neretin, 2003](https://www.esi.ac.at/preprints/esi1262.pdf), ESI 1262, 29-page PDF including cover | Propositions 1.1–1.2, PDF pp.5–6 (printed pp.4–5); Theorem 1.3, PDF p.9 (printed p.8), Section 1.5 | Rayleigh triangles interpolate matrix minor integrals in beta; the theorem establishes projective measures, including Hua–Pickrell specializations. These are array/projectivity results, not a single tridiagonal matrix assertion. Extraction of this older PDF has damaged glyphs; the locations and statement were checked in the text. |
| [Borodin–Gorin, 2015](https://arxiv.org/abs/1305.3627), 59-page version | Definition 1.1 and equation (3), PDF pp.3–4; Proposition 2.7 and proof, pp.13–15; Section 1.5, especially p.8 | All-beta Jacobi corners with consistent laws. The single-level density has exponents θα−1 and θ(|M−k|+1)−1 and rank min(k,M); this is a specified varying-parameter family. Section 1.5 explicitly explains the singularity obstruction for tridiagonal minor arrays. |
| [Gorin–Shkolnikov, 2015](https://arxiv.org/abs/1401.5595), 38-page version | Definition 1.1, PDF p.3; Theorem 1.2 (=Theorem 4.1), p.4; Theorems 5.2–5.3, pp.31–32 | Hermite corners and multilevel dynamics. The displayed SDE existence theorem has θ>1; Theorem 5.2 has θ≥2, and Theorem 5.3 has further Gibbs assumptions. Do not infer unrestricted SDE results from the general-beta abstract. None of these is an infinite tridiagonal principal-block theorem. |
| [Gorin–Marcus, 2020](https://arxiv.org/abs/1706.07393), 24-page version | Definition 1.3, PDF p.5; Theorem 1.1, p.3; Theorem 1.6, pp.5–6 | Fixed-top-row beta-corners and crystallization. The defining law is an orbital array law, not the law of all minors of a single Jacobi matrix. |
| [Assiotis, 2019](https://arxiv.org/abs/1609.03764), 11-page version | Theorem 1.1 and Corollary 1.4, PDF p.3; Remark 1.3, pp.3–4 | Beta≥1 Laguerre/Jacobi semigroup intertwinings with explicit parameter shifts; Corollary 1.4 gives a static Jacobi consistency identity in its stated parameter range. The proposed coupled generator in Remark 1.3 is described as conjectural; the theorem must not be enlarged into a general matrix construction. |
| [Yi Sun, 2016 preprint; published 2025](https://arxiv.org/abs/1609.09096), 18-page preprint | Theorem 3.4, PDF p.11; Section 4.2, p.13; Theorem 4.3, p.14; Theorem 4.5, pp.15–16 | Generalized Wishart and Jacobi multilevel matrix laws and their Bessel/Heckman–Opdam interpretation. The matrix theorems apply at beta=1 or 2 as specified. Section 4.2's Jacobi matrices are matrix ratios built from shared Gaussian matrices, not principal blocks of one tridiagonal matrix. Exact theorem/page citations here are to the 2016 preprint. |
| [Assiotis–Najnudel, 2021](https://arxiv.org/abs/1905.08684), 40-page version | Definitions 1.1, 1.3, 1.6, PDF pp.3–5; Theorems 1.13 and 1.16, pp.7–9; Section 8, pp.36–37, equations (28)–(29) | Classification of coherent orbital-beta arrays and coherent Hua–Pickrell / inverse-Wishart families. These give other natural coherent arrays with size-dependent weights; they do not assert fixed-band matrix representations. |
| [Budway–Shkolnikov, 2024](https://arxiv.org/abs/2403.10724), 34-page version | Theorem 1.1, PDF p.2; Theorem 1.2, p.3 | Multilevel Dyson construction/uniqueness for beta>2, and convergence as beta decreases to 2. Advances the dynamic theory, not the structured-matrix nesting question. |
| [Kawamoto–Shibukawa, 2026; arXiv:2505.23139](https://arxiv.org/abs/2505.23139), 15-page preprint | Lemma 1.1, PDF p.2; Definition 1.5 and Proposition 1.6, p.3; Theorems 1.7–1.8, p.4 | Fixed-parameter Laguerre intertwinings for beta≥1 using a different composite kernel. Its extra same-rank kernel has support 0≤y1≤x1≤y2≤…≤yN≤xN; composing it with the ordinary link does not assert ordinary codimension-one Cauchy interlacing. The ALEA PDF timed out; theorem/page claims use the retained arXiv preprint. Lemma 1.1 cites Forrester's *Log-gases and random matrices*, Proposition 4.2.1, for the Dirichlet-root identity; the book itself was not directly checked. |
| [Nakano–Trinh–Trinh, 2026](https://arxiv.org/abs/2601.13674), 20-page version | Theorem 1.2, PDF p.5; Theorems 4.3–4.4, pp.11–12 | Explicit Dirichlet-process spectral measures of limiting Jacobi matrices in the regime N beta→2c. Beta changes with N in this limit; finite prefixes are not thereby fixed-beta classical ensembles. |
| [Petrov–Xu, 2026](https://arxiv.org/abs/2607.27810), 31-page version | Definition 3.4, PDF p.11; Proposition 3.7, p.14; Theorem 4.6, p.17 | Perturbed Gaussian beta-corners, modified conditional links, and crystallization. This is an array/external-source extension, not a resolution of the all-size Jacobi/one-cut tridiagonal problem. |
| [Dumitriu–Forrester, 2010](https://arxiv.org/abs/0904.2216), 22-page version | Equation (1.4), Theorem 1.1, PDF pp.2–3 | Antisymmetric Gaussian beta tridiagonal model. Reversal gives the other explicit nested example below. |
| [Bourgade–Najnudel–Nikeghbali, 2013](https://arxiv.org/abs/1102.2633), 24-page version | Propositions 2.2 and 2.6, PDF pp.8 and 10; Propositions 3.1–3.2, p.11 | Coherent Haar unitary matrices under virtual-isometry projections. Those projections are not principal truncations. |

The literature therefore supplies many corners couplings and finite structured models. It does not justify identifying those notions. The Laguerre result below is an elementary consequence of an already published theorem, and no novelty is claimed for it. No located theorem establishes the requested general structured-matrix classification. This is a bounded literature finding, not a claim that no such paper exists.

## The Dixon–Anderson law and the Gaussian consistency mechanism

Put θ=β/2 and \(\Delta(x)=\prod_{i<j}(x_j-x_i)\) for increasing coordinates. Write \(y\prec x\) for
\(x_1<y_1<x_2<\cdots<y_{n-1}<x_n\).

### Lemma 1: Dirichlet residues give the conditional law

For fixed distinct \(x_1<\cdots<x_n\), choose \(q\sim\operatorname{Dirichlet}(s_1,\ldots,s_n)\), all \(s_i>0\). The roots y of

\[
 \sum_{i=1}^n\frac{q_i}{z-x_i}=0
\]

interlace x, and their density is

\[
 \frac{\Gamma(S)}{\prod_i\Gamma(s_i)}\,
 \frac{\Delta(y)\prod_{i=1}^n\prod_{j=1}^{n-1}|x_i-y_j|^{s_i-1}}
 {\prod_{i<k}(x_k-x_i)^{s_i+s_k-1}}\,1_{y\prec x},
 \qquad S=\sum_i s_i.                                      \tag{1}
\]

In particular the ordinary beta-corners link is

\[
 K_n^\theta(x,dy)=\frac{\Gamma(n\theta)}{\Gamma(\theta)^n}
 \frac{\Delta(y)}{\Delta(x)^{2\theta-1}}
 \prod_{i,j}|x_i-y_j|^{\theta-1}1_{y\prec x}\,dy.              \tag{2}
\]

Proof. Between successive poles the rational function is strictly decreasing, with opposite infinite limits, so it has exactly one root in each gap. Conversely the residues are

\[
 q_i=\frac{\prod_j(x_i-y_j)}{\prod_{k\ne i}(x_i-x_k)}>0,
 \qquad \sum_iq_i=1.
\]

The latter identity follows by comparing coefficients at infinity. Thus y and the interior of the simplex of q are in bijection. Differentiating gives \(\partial q_i/\partial y_j=-q_i/(x_i-y_j)\) for i<n. The Cauchy determinant formula, with the displayed residue formula, gives

\[
 \left|\frac{\partial(q_1,\ldots,q_{n-1})}{\partial(y_1,\ldots,y_{n-1})}\right|
       =\frac{\Delta(y)}{\Delta(x)}.
\]

Multiplying by the Dirichlet density and collecting each gap \(x_k-x_i\) gives (1). Its integral is one because the change of variables is bijective. Setting all \(s_i=\theta\) proves (2). This also proves the generalized Dixon–Anderson integration formula used below. ∎

For a symmetric Jacobi matrix, the cofactor resolvent identity gives

\[
 \frac{\det(z-J_{n-1})}{\det(z-J_n)}
       =\langle e_n,(z-J_n)^{-1}e_n\rangle
       =\sum_i\frac{|v_i(n)|^2}{z-x_i}.                     \tag{3}
\]

Consequently (2) is the law of deleting the last coordinate whenever the endpoint spectral weights are independent Dirichlet(θ,…,θ), independently of the eigenvalues.

### Hermite: two different consistent families

Take independent

\[
 a_i\sim N(0,2/\beta),\qquad b_i\sim\chi_{\beta i}/\sqrt\beta,
 \quad J_{ii}=a_i,\quad J_{i,i+1}=J_{i+1,i}=b_i.              \tag{4}
\]

Every leading block is a reversed Dumitriu–Edelman Hermite matrix. Hence its spectrum has law \(H_{n,\beta}\), and these matrices form one infinite nested family. Its entry density is

\[
 f_n(a,b)\propto
 e^{-\frac\beta4\sum_i a_i^2-\frac\beta2\sum_i b_i^2}
 \prod_{i=1}^{n-1}b_i^{\beta i-1}
 =e^{-\frac\beta4\operatorname{tr}J_n^2}
 \prod_{i=1}^{n-1}b_i^{\beta i-1}.                          \tag{5}
\]

The exact property of the Gaussian potential is trace additivity at the boundary:

\[
 \operatorname{tr}J_n^2=\operatorname{tr}J_{n-1}^2+a_n^2+2b_{n-1}^2.
\]

There is no term coupling old entries to new ones, and the exponent βi−1 of every retained off-diagonal entry is independent of terminal size n. Integrating the last diagonal and off-diagonal therefore multiplies (5) by a constant independent of the retained block. For a quadratic plus linear potential the same statement holds after a deterministic shift and scale. For a general potential, \(\operatorname{tr}V(J_n)\) contains boundary terms involving old entries; for example \(\operatorname{tr}J_2^4\) contains \(4b^2(a^2+ac+c^2)\).

Dumitriu–Edelman Theorem 2.12 also gives independent Dirichlet weights at e_n after reversal. Equations (2)–(3) thus show

\[
 H_{n,\beta}K_n^\theta=H_{n-1,\beta}.                       \tag{6}
\]

Starting at level N with \(H_{N,\beta}\) and applying fresh kernels (2) successively gives the **full Hermite corners process**. Its density is proportional to

\[
 e^{-\frac\beta4\sum_i(x_i^{(N)})^2}\Delta(x^{(N)})
 \prod_{k=1}^{N-1}\Delta(x^{(k)})^{2-\beta}
 \prod_{k=1}^{N-1}\prod_{i=1}^{k}\prod_{j=1}^{k+1}
       |x_i^{(k)}-x_j^{(k+1)}|^{\theta-1}.                 \tag{7}
\]

Indeed multiply the top density by the links and cancel powers of the Vandermondes; (6) ensures consistency as N varies. This is Gorin–Shkolnikov Definition 1.1, PDF p.3, with their variance t=2/β.

The nested matrix (4) has the same adjacent two-level laws, but its whole array is **not** (7). No claim of a reverse Markov property for the matrix array follows from adjacent conditional distributions alone.

### Lemma 2: the full corners law cannot be all Jacobi minors

For N≥3, no random real symmetric tridiagonal N-by-N matrix, with any dependence among its entries, can have an absolutely continuous full N-level corners law such as (7).

Proof. Such a matrix has 2N−1 real parameters. The map from its entries to the ordered eigenvalues of all its leading blocks is Lipschitz: for each block this follows from the eigenvalue perturbation inequality, and concatenating finitely many blocks preserves that property. The target array has dimension D=N(N+1)/2>2N−1. Cover a bounded parameter box by O(ε^{−(2N−1)}) cubes of side ε. Their images have diameter O(ε), so their total D-dimensional volume is O(ε^{D−(2N−1)}), tending to zero. Taking a countable union of boxes shows that the image has Lebesgue measure zero. A density positive in the interior of the interlacing cone cannot be supported there. ∎

For real symmetric bandwidth w the parameter count is \((w+1)N-w(w+1)/2\); whenever this is less than D the same proof applies. Thus a fixed bandwidth cannot realize such full corners laws for all large N. This does not obstruct an interlacing singular coupling of their one-level marginals. Borodin–Gorin, Section 1.5, PDF p.8, already makes this distinction.

## A nested beta-Laguerre construction

### Theorem 3: fixed hard-edge exponent, all sizes, all beta>0

Fix β>0 and a>−1. On one probability space take mutually independent

\[
 d_i=\chi_{\beta(a+i)}/\sqrt\beta\quad(i\ge1),\qquad
 \ell_i=\chi_{\beta i}/\sqrt\beta\quad(i\ge1).
\]

Let B be the semi-infinite lower bidiagonal matrix with diagonal d_i and entry \(\ell_i\) at (i+1,i). Define the symmetric tridiagonal matrix L by

\[
 L_{ii}=d_i^2+\ell_{i-1}^2,\quad \ell_0=0,
 \qquad L_{i,i+1}=L_{i+1,i}=d_i\ell_i.                     \tag{8}
\]

Its n-by-n leading block has eigenvalue density

\[
 \mathcal L_{n,\beta,a}(x)
 =Z^{-1}\Delta(x)^\beta\prod_{i=1}^n
     x_i^{\frac\beta2(a+1)-1}e^{-\beta x_i/2},
 \qquad 0<x_1<\cdots<x_n.                                \tag{9}
\]

All these spectra are coupled by strict Cauchy interlacing, and their complete finite-level joint laws are consistent under deleting the highest levels.

Proof. Let B_n be the leading n-by-n block of B. Because B is lower triangular, its first n rows have no nonzero entries beyond column n. Thus, entry by entry,

\[
 L_n=B_nB_n^T.                                            \tag{10}
\]

This identity is exactly the boundary condition that fails if the product is taken on the other side without checking it.

Let R_n reverse the coordinate order and put \(C_n=R_nB_n^TR_n\). It is lower bidiagonal. Its diagonal and sub-diagonal entries, in order from the top, have laws

\[
 \beta^{-1/2}\chi_{\beta(a+n)},\ldots,
 \beta^{-1/2}\chi_{\beta(a+1)},
 \qquad
 \beta^{-1/2}\chi_{\beta(n-1)},\ldots,
 \beta^{-1/2}\chi_{\beta}.
\]

They are independent. Therefore \(\sqrt\beta C_n\) is precisely the matrix immediately preceding Dumitriu–Edelman Theorem 3.4, PDF p.14, with its dimension m=n and its parameter

\[
 A_n=\frac\beta2(n+a),\qquad
 p_n=1+\frac\beta2(n-1).
\]

The theorem's admissibility condition \(A_n>\beta(n-1)/2\) is exactly a>−1. Its raw eigenvalue density is
\(\Delta(t)^\beta\prod_i t_i^{A_n-p_n}e^{-t_i/2}\).
Replacing t_i by βx_i gives (9), since \(A_n-p_n=\beta(a+1)/2-1\).

Reversal and transpose preserve singular values. More explicitly,
\(C_n^TC_n=R_nB_nB_n^TR_n\), and the positive matrices \(C_nC_n^T\) and \(C_n^TC_n\) have the same eigenvalues. Hence the theorem applies to (10).

All d_i and \(\ell_i\) are positive almost surely, so L_n is positive definite and has strictly positive off-diagonal entries. Cauchy's theorem gives weak interlacing of consecutive leading blocks. If consecutive characteristic polynomials had a common root, the recurrence

\[
 P_n(z)=(z-L_{nn})P_{n-1}(z)-(d_{n-1}\ell_{n-1})^2P_{n-2}(z)
\]

would force that root successively into P_{n-2},…,P_0=1, a contradiction. Interlacing is strict. Finally, the same infinite sequence of independent entries defines every L_n, so taking a smaller prefix does not change any earlier matrix or its spectrum. This proves consistency of the actual joint laws, not only agreement of the one-level marginals. ∎

If the desired power is an arbitrary fixed α>−1, set \(a=2(\alpha+1)/\beta-1\). Thus the construction covers every integrable hard-edge power. In a Wishart notation with rectangularity m−n=a, the effective column parameter is m_n=n+a and grows with size. Holding the theorem parameter A, or the number of columns m, fixed would be a different family.

The construction also gives the random-measure interpretation in Virág's theorem. Here are the operator details. For \(X\sim\chi^2_\nu\), \(E e^{X/4}=2^{\nu/2}\). Applied to d_i² and ell_i², Markov's inequality with a sufficiently large constant gives \(P(d_i^2>Ki)+P(\ell_i^2>Ki)\le C e^{-c i}\). Borel–Cantelli therefore gives \(d_i,\ell_i\le C\sqrt i\) eventually. Thus the Jacobi off-diagonals \(c_i=d_i\ell_i\) satisfy \(\sum_i 1/c_i=\infty\).

For clarity the needed Carleman argument is short. An adjoint deficiency vector u would be a square-summable solution of Ju=zu for Im z≠0, satisfying the left endpoint recurrence. Multiplying that recurrence by the conjugate of u_k and summing through n gives

\[
 |\operatorname{Im}z|\sum_{k=1}^n|u_k|^2
       \le c_n|u_nu_{n+1}|.
\]

If u is nonzero, its partial squared norm is bounded below by a positive constant eventually. Hence \(1/c_n\le C|u_nu_{n+1}|\), whose sum is finite by Cauchy–Schwarz, a contradiction. Both deficiency spaces vanish, so the minimal Jacobi operator is essentially self-adjoint. On finitely supported vectors \(\langle f,Lf\rangle=\|B^Tf\|^2\ge0\), so its closure is nonnegative. The spectral theorem now gives a probability measure on [0,∞) at e_1. Inducting in the positive-off-diagonal recurrence shows e_1 is cyclic and that the orthonormal polynomials have monic multiples P_n. Their zeros are the eigenvalues of L_n. This proves the random-measure formulation as well as finite-prefix nesting.

The entries of L themselves are dependent: for example d_i appears in both L_ii and L_i,i+1. The independent objects are the bidiagonal entries. There is therefore no conflict with the independent-Jacobi-entry theorem below.

### Why this is not the ordinary Laguerre corners process

Already n=2 distinguishes the laws. From (8), \(E L_{11}=a+1\), whereas \(E\operatorname{tr}L_2/2=a+2\). If deleting coordinate 2 had independent Dirichlet(θ,θ) spectral weights, equation (3) would give conditional mean of its scalar minor equal to the average of the two eigenvalues, and hence unconditional mean a+2. Thus the adjacent link for this construction is not (2). Its one-level laws remain exactly (9).

## What ordinary corners do to Laguerre and Jacobi parameters

### Proposition 4: the parameter shifts are unavoidable for the standard link

Let \(\mathcal J_{n,\beta;p,q}\) have density
\(Z^{-1}\Delta(x)^{2\theta}\prod_i x_i^p(1-x_i)^q\) on (0,1), with p,q>−1. Then

\[
 \mathcal J_{n,\beta;p,q}K_n^\theta
       =\mathcal J_{n-1,\beta;p+\theta,q+\theta}.           \tag{11}
\]

For Laguerre with density \(\Delta(x)^{2\theta}\prod_i x_i^\alpha e^{-c x_i}\), α>−1 and c>0, the image is Laguerre of size n−1 with exponent α+θ and the same c.

Proof. Multiply the Jacobi density by (2). Apart from constants the joint density is

\[
 \Delta(y)\Delta(x)\prod_i x_i^p(1-x_i)^q
          \prod_{i,j}|x_i-y_j|^{\theta-1}1_{y\prec x}.
\]

To integrate x, use (1) with the n+1 fixed poles
\((0,y_1,\ldots,y_{n-1},1)\) and Dirichlet parameters
\((p+1,\theta,\ldots,\theta,q+1)\).
Since the integral of that density is one, the integral of the x-dependent product is a constant times

\[
 \Delta(y)^{2\theta-1}\prod_jy_j^{p+\theta}(1-y_j)^{q+\theta}.
\]

The remaining factor \(\Delta(y)\) yields (11); normalization then identifies the probability law.

For Laguerre, instead use poles \((0,y_1,\ldots,y_{n-1},R)\), parameters \((\alpha+1,\theta,\ldots,\theta,cR+1)\), and divide out the power of R so that the x-weight becomes \(x^\alpha(1-x/R)^{cR}\). As R→∞ this tends to \(x^\alpha e^{-cx}\). The remaining y-weights tend to \(y^{\alpha+\theta}e^{-cy}\). Passage under the integrals follows from \((1-x/R)^{cR}\le e^{-cx}\), polynomial growth at infinity, and the locally integrable interlacing singularities with θ>0 and α>−1. Equivalently one can apply this domination to the normalized joint density and use the gamma ratios in (1) to take its constant's limit. This gives the stated Laguerre image. ∎

Consequences: fixed hard-edge exponent Laguerre laws and fixed p,q Jacobi laws are not consistent under the ordinary Dixon–Anderson links. If every level n is required to be a full-rank Jacobi law under those links, its powers must satisfy
\(p_n=p_1-(n-1)\theta\), \(q_n=q_1-(n-1)\theta\).
They eventually cease to exceed −1, so no such all-size family with finite initial powers exists. The analogous Laguerre statement holds for its hard-edge power. This excludes the standard link, not the successful Laguerre construction (8), nor arbitrary other links. Finite chains with dimension-dependent powers, such as dense fixed-ambient Wishart/Jacobi corners, are fully compatible with (11).

Borodin–Gorin's Jacobi process uses its stated different level structure and backward kernels; its rank min(n,M), varying exponents, and consistency must not be replaced by a claim about fixed p,q and ordinary DA links at all n.

## Two precise Gaussian characterizations

### Theorem 5: independent entries in the canonical full-line spectral model

Let V∈C²(R), with the indicated densities normalizable, and β>0. Consider the canonical model in which the size-n eigenvalue density is
\(Z^{-1}\Delta(x)^\beta e^{-\sum_iV(x_i)}\)
and the spectral weights at the deleted endpoint are independent Dirichlet(β/2,…,β/2), independently of the eigenvalues. If the two diagonal entries and positive off-diagonal entry are independent already at n=2, then

\[
 V(x)=c x^2+d x+e,\qquad c>0.                              \tag{12}
\]

Conversely these potentials give independent entries and an all-size nested canonical model after reversal.

Proof. Write \(J_2=\begin{pmatrix}a&b\\b&c_0\end{pmatrix}\), b>0. If λ1<λ2 and q is one endpoint spectral weight, then
\(b=(\lambda_2-\lambda_1)\sqrt{q(1-q)}\).
The absolute Jacobian from (λ1,λ2,q) to (a,c_0,b) is
\((\lambda_2-\lambda_1)^2/(2b)\).
Thus the product of the eigenvalue and beta(θ,θ) densities transforms to

\[
 f(a,c_0,b)=C b^{\beta-1}e^{-\operatorname{tr}V(J_2)}.      \tag{13}
\]

Independence and positivity imply that \(\operatorname{tr}V(J_2)\) is a sum of one function of a, one of c_0, and one of b. This identity initially holds almost everywhere; continuous cross-ratio identities extend it everywhere in the open product domain. Letting b decrease to zero shows that

\[
 \operatorname{tr}V(J_2)-V(a)-V(c_0)=h(b)
\]

is independent of a,c_0. In particular, setting c_0=a gives

\[
 V(a+b)+V(a-b)-2V(a)=h(b).
\]

Divide by b² and let b↓0. Since V is C², V''(a) has the same value for every a. Hence V is quadratic or affine. Normalizability on all of R rules out zero or negative quadratic coefficient, proving (12).

Conversely,
\(\operatorname{tr}V(J_n)=c\sum_i a_i^2+2c\sum_i b_i^2+d\sum_i a_i+ne\).
The canonical reversed density is
\(C_n e^{-\operatorname{tr}V(J_n)}\prod_i b_i^{\beta i-1}\);
this factors into normalizable independent diagonal and off-diagonal densities with size-independent retained factors. It therefore defines consistent leading blocks, with the desired spectral laws by the canonical spectral-coordinate change of variables. ∎

The independent Dirichlet spectral-weight hypothesis is essential to what has been proved. Eigenvalue marginals alone do not determine eigenvector weights or the entry density (13). This theorem is not an unrestricted no-go theorem for independent-entry models specified only by their eigenvalues, and it says nothing against dependent-entry realizations.

### Theorem 6: at beta=2, same fixed weight and ordinary DA coherence force Gaussian

Let w>0 be C¹ on R, with \(m_0=\int w(x)dx<\infty\), \(\int |x|w(x)dx<\infty\), and a finite, nonzero size-2 partition function. If the beta=2 size-2 law with weight w maps under K₂¹ to the size-1 law with the same w, then w is Gaussian up to normalization, translation, and scale.

Proof. The unnormalized density of the scalar minor is

\[
 F(y)=\int_{x<y<z}(z-x)w(x)w(z)\,dx\,dz.
\]

Write \(A_j(y)=\int_{-\infty}^y x^j w(x)dx\),
\(B_j(y)=\int_y^\infty x^j w(x)dx\). Then
\(F=A_0B_1-A_1B_0\), and differentiating gives

\[
 F'(y)=w(y)(m_1-y m_0),\qquad m_1=\int xw(x)dx.
\]

Consistency means F=Cw with C>0. Therefore
\(w'/w=(m_1-y m_0)/C\), and integration yields

\[
 w(y)=C_0\exp\{-\tfrac{m_0}{2C}(y-m_1/m_0)^2\}.
\]

The converse is (6), with shift and scale. ∎

Thus a nonquadratic full-line one-cut potential cannot retain the same weight under ordinary beta=2 corners projection. This stronger statement about a specified link still does not classify other singular couplings or all Jacobi-matrix models of the same marginal laws.

## Jacobi and circular: what fails, and what remains open here

### Proposition 7: simply reversing the Killip–Nenciu Jacobi matrix fails

Fix the Jacobi weight \(x^p(1-x)^q\) on (0,1), p,q>−1 with p≠q. For any N≥2, reverse the N-by-N Killip–Nenciu matrix from Theorem 2, keeping p,q fixed, and take its scalar leading block. That scalar does not have the target size-1 law.

Proof. Use the paper's coordinates on [−2,2], so its parameters called a,b are q,p respectively. Write S=p+q+2, d=p−q, θ=β/2. Its beta distribution B(s,t) on (−1,1), with weight \((1-u)^{s-1}(1+u)^{t-1}\), has mean (t−s)/(s+t). The independent variables involved in the last diagonal entry have means

\[
 E\alpha_{2N-2}=d/S,\quad E\alpha_{2N-4}=d/(S+2\theta),
 \quad E\alpha_{2N-3}=(\theta-S)/(\theta+S).
\]

Equation (1.12) of Killip–Nenciu gives

\[
 b_N=(1-\alpha_{2N-3})\alpha_{2N-2}
       -(1+\alpha_{2N-3})\alpha_{2N-4}.
\]

Independence therefore yields \(E b_N=2d/(S+2\theta)\). On mapping to (0,1), the reversed scalar mean is

\[
 E[(b_N+2)/4]=\frac12+\frac{p-q}{2(S+\beta)}.              \tag{14}
\]

The true size-1 beta(p+1,q+1) mean is
\(\frac12+(p-q)/(2S)\), which is different. ∎

This rules out that candidate, not every possible beta-Jacobi nested model. For symmetric p=q, the means coincide and this argument gives no conclusion. The finite CS model also requires attention to its changing last boundary factor; parameter distributions that look independent of size after reversal do not by themselves make its finite blocks identical.

### Proposition 8: unitary principal-block nesting forces diagonal matrices

Suppose each U_n is unitary and is literally the leading block of U_{n+1}. Then all U_n are diagonal. In particular, no irreducible CMV or unitary Hessenberg model can have every leading block unitary with a circular beta-ensemble spectrum.

Proof. Write \(U_{n+1}=\begin{pmatrix}U_n&v\\w^*&z\end{pmatrix}\). The upper-left equations in \(U_{n+1}U_{n+1}^*=I\) and \(U_{n+1}^*U_{n+1}=I\) give vv*=0 and ww*=0. Hence v=w=0 and |z|=1. Inducting from n=1 proves diagonalization, which excludes the nonzero coordinate couplings of an irreducible structured model. ∎

Diagonalization alone does not rule out arbitrary dependent diagonal phase sequences with specified spectral marginals. The proposition therefore excludes nontrivial unitary CMV/Hessenberg principal-block models, not all eigenvalue-only circular couplings or general nonnormal Hessenberg representations.

Killip–Nenciu Theorem 1 has a terminal Verblunsky coefficient on the unit circle at each finite size; its earlier coefficients lie in the disk and their laws depend on the terminal size. Paraorthogonal boundary changes can give circular spectral couplings, but those are not literal principal unitary blocks of one irreducible CMV matrix. Virtual-isometry projections provide another notion of consistency: where the inverse exists, the projection of \(\begin{pmatrix}A&B\\C&D\end{pmatrix}\) is \(A+B(I-D)^{-1}C\), rather than A. Coherent Hua–Pickrell arrays give all-beta circular eigenvalue couplings after the Cayley transform, as discussed in Assiotis–Najnudel Section 8. These facts should not be described as a principal-block CMV construction.

## Other natural models and the role of bandwidth

The following example answers the “other natural random matrix models” part positively in a concrete class.

### Corollary 9: the antisymmetric Gaussian beta model nests

Let independent \(r_i^2\sim\operatorname{Gamma}(i\beta/4,1)\), and form the real symmetric Jacobi matrix with zero diagonal and off-diagonals r_i. Its leading N-by-N block is unitarily equivalent, up to reversal and harmless signs, to i times the antisymmetric model in Dumitriu–Forrester equation (1.4). Its eigenvalues are symmetric pairs ±λ_j, and also zero when N is odd. The joint density of its positive eigenvalues is

\[
 C^{-1}e^{-\sum_j\lambda_j^2}\Delta(\lambda_1^2,\ldots,\lambda_m^2)^\beta
 \prod_{j=1}^m\lambda_j^{\eta_N},\qquad
 m=\lfloor N/2\rfloor,
\]

where \(\eta_N=\beta/2-1\) for even N and \(\eta_N=3\beta/2-1\) for odd N.

Proof. Their notation \(\widetilde\chi_k\) means the square root of Gamma(k/2,1). Reversing their off-diagonal sequence \(\widetilde\chi_{(N-i)\beta/2}\) gives precisely r_i. Multiplication of the real skew matrix by i makes it Hermitian. A diagonal unitary change of phases makes its adjacent off-diagonal entries positive real, giving the stated Jacobi form. Reversal and the phases preserve eigenvalues, with the overall sign immaterial to a spectrum symmetric about zero. The density is exactly their Theorem 1.1, PDF pp.2–3. Since the variables r_i are one infinite independent sequence, the actual principal blocks nest; their full spectra strictly interlace by the same recurrence argument as in Theorem 3. ∎

Infinite Wigner matrices with a fixed entry law give elementary nested dense Wigner models: take one infinite array of independent entries and impose symmetry. Their leading matrices have the intended Wigner laws and interlace, though non-Gaussian Wigner eigenvalue densities generally are not classical Dyson beta densities. Ordinary fixed-column Gaussian rectangular matrices give dense Wishart principal-minor chains, with the Laguerre exponent changing as in Proposition 4 and with full rank only up to the column count. Finite-ambient Haar compressions give corresponding Jacobi chains. These statements are constructions with explicit shared entries or fixed ambient matrices, not general sparse beta analogues.

There is also a general, artificial dense matrix realization of any strictly interlacing array. To see why mere existence of a dense matrix is a weak requirement, suppose H_{n-1} has spectrum y and a desired new row x strictly interlaces y. Put

\[
 P(z)=\prod_{i=1}^n(z-x_i),\quad Q(z)=\prod_{j=1}^{n-1}(z-y_j),
 \quad a=\sum_i x_i-\sum_jy_j,
 \quad v_j^2=-P(y_j)/Q'(y_j)>0.
\]

Partial fractions give \(P(z)/Q(z)=z-a-\sum_jv_j^2/(z-y_j)\). Thus the arrow matrix with top block diag(y), last diagonal a, and last column v has characteristic polynomial P. Conjugating its first n−1 coordinates into an eigenbasis of H_{n-1} constructs H_n while preserving H_{n-1} exactly. Choosing eigenvectors by a fixed measurable sign rule makes this a random construction when the array is random. Iteration realizes any coherent full beta-corners array by dense real symmetric matrices. No invariance, entry independence, fixed bandwidth, or natural matrix law is supplied by this observation.

## Computation: evidence only

The script [code/check_models.py](code/check_models.py) is reproducible from the project root with `python3 code/check_models.py`. It ran at niceness 10 with one thread in each numerical library, one process and no workers. It used Python 3.13.2, NumPy 2.2.3 and SciPy 1.15.2. Peak RSS was 203,128,832 bytes (about 194 MiB); numerical execution took 1.63 seconds. Neither the dimension arguments nor any distributional statement above rests on these experiments.

Seed: 400020261113. Each parameter case used 30,000 independent matrices, β∈{0.5,1,2,4}, a∈{−0.25,1.5}, sizes n=1,…,4. Within a sample, the candidate leading minors were taken from the same size-4 matrix.

The target checks were derived from the density independently of the candidate truncation:

1. Homogeneity of (9), or integration in the trace variable, gives
\(T_n=\sum_i\lambda_i\sim\operatorname{Gamma}(\theta n(n+a),2/\beta)\), using shape/scale convention. This was tested by a one-sample KS test at every size.
2. For n=2 set \(U=((\lambda_2-\lambda_1)/(\lambda_1+\lambda_2))^2\). Changing variables from the ordered pair to (T,U) in (9) gives independent
\(T\sim\operatorname{Gamma}(\beta(a+2),2/\beta)\) and
\(U\sim\operatorname{Beta}((\beta+1)/2,\theta(a+1))\).
Indeed \(\lambda_{1,2}=T(1\mp\sqrt U)/2\) and the Jacobian is T/(4√U); the density separates. The U marginal was tested directly. A 5-by-5 joint histogram of the two probability-integral transforms tested their full n=2 joint density, not only separate moments.
3. At n=3,4 every ordered eigenvalue marginal was compared by two-sample KS with an independent draw from the original, decreasing-index Dumitriu–Edelman bidiagonal model at the matching dimension and parameter. This is a finite-model cross-check; the n=2 checks above directly use the target density.
4. A second analytic calculation uses \(\det L_n=\prod_{i=1}^n d_i^2\), giving
\[
 E\log\det L_n=\sum_{i=1}^n\psi(\theta(a+i))+n\log(2/\beta),\quad
 \operatorname{Var}(\log\det L_n)=\sum_{i=1}^n\psi_1(\theta(a+i)).
\]
The empirical means were checked against these formulas.
5. Direct size-1 Killip–Nenciu draws were checked against Beta(p+1,q+1). Reversed size-4 Jacobi matrices, p=0.3, q=1.1, were a separate negative control.

There were 108 positive distributional checks. None rejected at family-wise level 0.05 after Holm adjustment; the smallest unadjusted p was 0.0073086871. This is compatibility with the targets, not proof of equality. The maximum absolute log-determinant mean z-score was 1.84851. Maximum matrix nesting discrepancy was 7.11×10⁻¹⁵; maximum numerical interlacing violation was 3.99×10⁻¹⁵, at roundoff scale.

| β | Reversed Jacobi scalar mean | Exact candidate mean (14) | Target mean | KS p against target |
|---|---:|---:|---:|---:|
| 0.5 | 0.397792 | 0.397436 | 0.382353 | 2.80×10⁻⁵⁰ |
| 1 | 0.408929 | 0.409091 | 0.382353 | 1.03×10⁻¹⁵⁶ |
| 2 | 0.425991 | 0.425926 | 0.382353 | below floating-point output range |
| 4 | 0.446406 | 0.445946 | 0.382353 | below floating-point output range |

Zeros returned for the last two p-values represent numerical underflow, not a mathematical probability of zero. All rejection evidence is ancillary to the exact mean mismatch in Proposition 7.

Machine-readable results: [data/checks.json](data/checks.json), [data/positive_checks.csv](data/positive_checks.csv), [data/moments.csv](data/moments.csv), [data/negative_controls.csv](data/negative_controls.csv). Raw eigenvalue samples are retained in [data/samples.npz](data/samples.npz).

## What is still unproved

The fixed-hard-edge Laguerre coupling and antisymmetric example satisfy Virág's one-matrix interpretation. Full DA corners, finite Jacobi/CMV matrix models, virtual-isometry couplings and operator limits have different requirements, and the literature above cannot be substituted for the missing implication.

Unresolved in this report are existence or a general no-go theorem for a single random Jacobi matrix with all fixed-weight beta-Jacobi leading-minor marginals; an unrestricted classification from eigenvalue marginals and independent entries without specifying spectral weights; and classification for arbitrary one-cut potentials under other singular interlacing couplings. A nontrivial unitary CMV/Hessenberg principal-block construction is excluded; general nonnormal Hessenberg models and eigenvalue-only circular couplings are not classified here.

No publication, git push, global-memory update or change outside the task directory was performed. Only plain-text source conversions were retained; no PDFs, paper page images or scans were saved.

## Final audit and files

[code/audit.py](code/audit.py) independently checked 100 finite reversal/transpose identities, explicit arrow completions of interlacing spectra, and Dirichlet residue normalizations. Maximum errors were 2.14×10⁻¹⁴, 6.99×10⁻¹³, and 4.45×10⁻¹⁶ respectively. It also re-derived all four negative-control means using exact rational arithmetic, recomputed the Holm adjustments, verified the simulation code hash against the data, inspected all 36 retained sample arrays, checked source page-marker sequences, parsed the Python files, and verified the report's local links. Results are in [data/audit.json](data/audit.json).

The source inventory, retrieval URLs, source-byte hashes and PDF page counts are in [sources/INDEX.txt](sources/INDEX.txt); search scope and access limitations are in [sources/SEARCH_LOG.txt](sources/SEARCH_LOG.txt). Report claims were audited against the stated editions. The unitary result was narrowed to what the block calculation proves: diagonalization excludes irreducible CMV/Hessenberg models, while diagonalization alone does not disprove every dependent diagonal eigenvalue coupling.

Task: “Open problem D0040.” — 2026-11-13 09:52 +04.
