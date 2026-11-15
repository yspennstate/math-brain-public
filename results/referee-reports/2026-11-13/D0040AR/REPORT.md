MINOR

The main claim survives. For every fixed β>0 and a>−1, the proposed single infinite Jacobi matrix has, simultaneously for all n, the unscaled β-Laguerre eigenvalue density with hard-edge power β(a+1)/2−1. Neither the primitive chi laws nor any retained matrix entry depends on the terminal size. The Dumitriu–Edelman shape parameter and effective Wishart column count do depend on n; the submitted report states that dependence correctly. The antisymmetric example and the stated restricted obstructions also survive. I found a parameter issue in the supporting circular/Hua–Pickrell literature discussion, missing later literature, and an archival gap, rather than a counterexample to either construction.

This is a correct elementary consequence of published matrix models, with useful distinctions between several meanings of coupling. It is not a new finite-size ensemble or an unrestricted classification. I would accept the mathematical partial result after the following corrections. Line references below are to claim_files/REPORT.md, as supplied; that file was not modified.

1. At lines 419 and 57, the assertion about all-β circular couplings via the cited Hua–Pickrell family needs its parameter convention stated. Equation (28) of the cited arXiv:1905.08684v2 actually has factors (1+ix)^(−s−Nθ)(1−ix)^(−s̄−Nθ), θ=β/2. Its nearby assertion that s=0 gives the circular β ensemble by Cayley transform is incorrect as printed when θ≠1. The transform leaves a one-body factor |1−z|^(2(θ−1)) at s=0. Indeed, for N=1, θ=1/4, s=0, the displayed real-line density is not even integrable. Fix: use the real-line CβE density Δ(x)^(2θ)∏(1+x_j²)^(−1−θ(N−1)), or reparameterize that preprint's s as 1−θ for CβE, with the corresponding correct integrability condition Re(s)+θ>1/2. More generally its real s corresponds to circular exponent 2(s+θ−1). Equation (29) has an analogous convention issue: inversion of its x^(−τ−2θN) weight gives Laguerre power τ+2θ−2, requiring τ>1−2θ, rather than its printed τ>−1 for all θ. This is a defect in the cited version and a qualification missing from the report, not a defect in the Laguerre proof. I confirmed the expressions in the original TeX as well as the PDF extraction. I could not access the journal PDF and do not assert that the journal retains the error. The qualitative existence of coherent circular eigenvalue arrays remains valid with the corrected convention.

2. The literature list at lines 44–63 omits directly relevant later work by Virág. Add Valkó–Virág, *The Sineβ operator* (2017), especially Proposition 20 and Theorem 21; Valkó–Virág, *Operator limit of the circular beta ensemble* (2020), Theorem 1; and Krishnapur–Rider–Virág, *Universality of the Stochastic Airy Operator* (2016), Proposition 2 and Theorem 1. These are finite/operator-limit representations and couplings, not all-size leading-block theorems. Their inclusion changes the coverage, not the verdict. Sources and exact distinctions are given below.

3. The archival assertions at lines 22 and 499 cannot be checked from the delivered claim package: claim_files/sources/ is absent, including the cited source inventory and search log. This could be an omission in packaging rather than in the originating run. Fix: provide those texts and metadata. This audit independently obtained the papers into sources/ as page-marked plain text, with retrieval URLs and hashes. Line 28 accurately paraphrases Theorem 4.1 but does not transcribe it; the exact statement requested for this audit is supplied below.

4. At lines 9 and 65, “the requested general classification” describes a stronger objective than the quoted Question 2 itself. That question asks for other examples; the verified Laguerre construction answers that existential question positively. Fix: distinguish a positive answer for these families from a classification of all fixed-weight potentials. The report's bounded wording about what its literature search found is appropriate; neither this audit nor that search proves global nonexistence of an overlooked paper or certifies that every remaining case is open.

I found no additional mathematical error in the displayed Laguerre proof, antisymmetric corollary, dimension argument, parameter-shift proposition, Gaussian characterizations, reversed-Jacobi counterexample, or unitary block calculation. The Gaussian and unitary results must retain their stated hypotheses. The symmetric Jacobi candidate can also be excluded, as shown below, but the report correctly says that its mean argument alone does not do so.

I independently downloaded [Virág's paper](https://arxiv.org/abs/1804.06953). The 28-page PDF is dated May 25, 2014, and was uploaded in April 2018. The retained text is [sources/virag.txt](sources/virag.txt). Counting PDF pages from one, the exact statement on page 5 is:

> Theorem 4.1 (Coupling of the β-Hermite ensembles). There exists a random measure μβ so that for all n the zeros of the orthogonal polynomial pn with respect to μβ are distributed as the eigenvalues of the n-point β-Hermite ensemble.

Here μβ and pn denote the source's subscripted μ_β and p_n; only typographic subscript rendering has been flattened. Question 2 on PDF page 6 is:

> Question 2 (Nested models). Can any other Dyson β-ensembles be coupled this way? How about other natural random matrix models?

The surrounding text makes the intended mechanism explicit. There is one random measure, so there is one sequence of three-term recurrence coefficients. Its monic degree-n polynomial is det(xI−J_n), where J_n is the actual leading n×n block of one semi-infinite Jacobi matrix. Conversely an essentially self-adjoint Jacobi matrix with positive off-diagonals supplies the measure at e₁. A different measure or a different tridiagonalization at every size does not suffice. Neither does an arbitrary interlacing array: its polynomials need not satisfy a three-term recurrence with a scalar, x-independent coefficient multiplying p_(n−2).

The scale matters. Virág's equation (1) has diagonal variance 2/(nβ) and off-diagonal χ_(β(n−i))/√(nβ). Section 4 uses √n T_n and reverses the indexing. In common units the nested Hermite matrix has independent a_i∼N(0,2/β), b_i∼χ_(βi)/√β, and density Δ(x)^β exp(−β∑x_i²/4). The normalized T_n themselves are not literal prefixes. This agrees with the claim. A global deterministic scale is harmless; applying an n-dependent scale separately to every prefix changes the question.

Here is my full verification of the main construction. Set θ=β/2. On one probability space choose all the following variables mutually independently:

\[
 d_i=\beta^{-1/2}\chi_{\beta(a+i)},\qquad
 \ell_i=\beta^{-1/2}\chi_{\beta i},\qquad i\ge1,
 \quad a>-1.
\]

Let B be lower bidiagonal, with B_(i,i)=d_i and B_(i+1,i)=ell_i. Define L entrywise by

\[
 L_{ii}=d_i^2+\ell_{i-1}^2,\quad \ell_0=0,
 \qquad L_{i,i+1}=L_{i+1,i}=d_i\ell_i.
\]

For example its leading size-three matrix is

\[
 \begin{pmatrix}
 d_1^2&d_1\ell_1&0\\
 d_1\ell_1&d_2^2+\ell_1^2&d_2\ell_2\\
 0&d_2\ell_2&d_3^2+\ell_2^2
 \end{pmatrix}.
\]

Because the first n rows of B have no entries in columns beyond n,

\[
 L_n=B_nB_n^{\mathsf T}
\]

exactly. The alternative product is genuinely different: the leading n-block of BᵀB equals B_nᵀB_n+ell_n²e_ne_nᵀ. This is the boundary error the claimed construction successfully avoids.

Let R_n reverse n coordinates and C_n=R_nB_nᵀR_n. Its diagonal, from the top, has degrees β(a+n), β(a+n−1), …, β(a+1); its sub-diagonal has degrees β(n−1), β(n−2), …, β. All entries have the common scale β^(−1/2), and all 2n−1 entries are independent. Thus √β C_n is precisely the bidiagonal matrix above [Dumitriu–Edelman Theorem 3.4](https://arxiv.org/abs/math-ph/0206043), PDF page 14, with dimension m=n and their parameter

\[
 A_n=\theta(n+a),\qquad p_n=1+\theta(n-1).
\]

The theorem gives raw squared-singular-value density

\[
 Z^{-1}\Delta(t)^\beta\prod_{j=1}^n t_j^{A_n-p_n}e^{-t_j/2},
 \quad A_n>\theta(n-1).
\]

The exponent and admissibility reduce to

\[
 A_n-p_n=\theta(a+1)-1,\qquad a>-1.
\]

Moreover C_nᵀC_n=R_nL_nR_n, and C_nC_nᵀ has the same eigenvalues. Taking t_j=βx_j proves that the actual prefix L_n has density

\[
 Z_{n,\beta,a}^{-1}\Delta(x)^\beta
 \prod_{j=1}^n x_j^{\theta(a+1)-1}e^{-\beta x_j/2},
 \qquad 0<x_1<\cdots<x_n.
 \tag{R1}
\]

This is an exact finite-n identity for every n on the same product probability space. There is no terminal-size parameter in d_i, ell_i or L_(i,j). The DE shape A_n varies with n; concealing that fact would be an error, but the report gives it explicitly. If m denotes effective Wishart columns, then m_n=n+a. Fixed columns m would instead give exponent θ(m−n+1)−1, a different family, full-rank for only finitely many integer n. For general real a, “columns” is only a formal Wishart parameter; an ordinary Gaussian rectangle requires appropriate integer dimensions. In particular −1<a<0 is allowed for the generalized density without describing an actual n×m_n Gaussian rectangle.

To prescribe any fixed hard-edge power α>−1 in (R1), choose a=2(α+1)/β−1. A weight e^(−c x), for any fixed c>0, follows from one constant rescaling of the whole L. A weight with rate proportional to n is a different nesting requirement. These facts settle the scaling and column-count ambiguities.

Every d_i,ell_i is strictly positive almost surely; hence every L_n is positive definite and irreducible. The characteristic-polynomial recurrence is

\[
 P_n(z)=(z-d_n^2-\ell_{n-1}^2)P_{n-1}(z)
       -d_{n-1}^2\ell_{n-1}^2P_{n-2}(z).
\]

The positive final coefficient rules out shared consecutive roots, since a shared root would propagate to P₀=1. Cauchy interlacing is therefore strict. This proves genuine nested matrices, not merely matching marginals.

The orthogonality-measure conclusion also holds. Chi-square exponential tails imply d_i,ell_i=O(√i) almost surely by Borel–Cantelli, so c_i=d_i ell_i=O(i) and ∑c_i^(−1)=∞. The Jacobi Carleman criterion makes the minimal operator essentially self-adjoint. Equivalently a square-summable nonreal deficiency solution would imply 1/c_n≤C|u_nu_(n+1)| eventually, contradicting that divergent sum. On finitely supported f, ⟨f,Lf⟩=‖Bᵀf‖²≥0. The closure is nonnegative, and its probability spectral measure at cyclic e₁ has the required orthogonal polynomials. Thus the construction meets the random-measure reading of Theorem 4.1, not just its finite-matrix shadow.

There is a useful independent sanity check against accidentally claiming ordinary Laguerre corners. E L₁=a+1, whereas E tr(L₂)/2=a+2. A Dirichlet(θ,θ) deletion link would give the latter as the expected scalar minor. Hence this construction has a different adjacent-level link from ordinary invariant Wishart corners. The report makes exactly this distinction.

For the antisymmetric claim, [Dumitriu–Forrester](https://arxiv.org/abs/0904.2216), equation (1.4) and Theorem 1.1, PDF pages 2–3, use tilde-χ_k²∼Gamma(k/2,scale 1). Reversing the off-diagonal sequence gives independent

\[
 r_i^2\sim\operatorname{Gamma}(i\beta/4,1),\qquad i\ge1.
\]

One infinite zero-diagonal symmetric Jacobi matrix with off-diagonals r_i has each prefix unitarily equivalent to i times their real skew matrix, up to reversal and a sign. One can choose the phase change consistently on the infinite chain. Its positive eigenvalues have density

\[
 Z^{-1}e^{-\sum_j\lambda_j^2}
 \Delta(\lambda^2)^\beta\prod_j\lambda_j^{\eta_N},
 \qquad \eta_N=
 \begin{cases}\beta/2-1,&N\text{ even},\\3\beta/2-1,&N\text{ odd}.
 \end{cases}
\]

There are floor(N/2) positive eigenvalues; negatives are their opposites, and there is one zero when N is odd. For N=2, λ²=r₁²∼Gamma(β/4,1); for N=3, λ²=r₁²+r₂²∼Gamma(3β/4,1). Both verify the parity exponents and the absence of an extra factor two. Carleman applies here too since r_i=O(√i). This is a valid other natural model; its full spectrum is constrained to symmetric pairs, so it should not be described as an ordinary unconstrained N-particle Hermite density.

I checked the obstructions and supporting identities in the following order. This also records exactly how far each proof reaches.

| Claim location | Independent check and true scope |
|---|---|
| Lemma 1, lines 74–109 | The residue formula q_i=∏(x_i−y_j)/∏_(k≠i)(x_i−x_k) is positive, sums to one and has Jacobian Δ(y)/Δ(x). Substitution in the Dirichlet density gives the displayed generalized Dixon–Anderson formula with the stated gamma constant. Finite-difference Jacobians independently agree. |
| Hermite discussion, lines 111–157 | Reversal of DE supplies Dirichlet weights at e_n independent of the eigenvalues, so the cofactor resolvent gives the ordinary DA law for each adjacent pair. Multiplying fresh DA kernels gives the report's full-corners density (7). Agreement of adjacent pairs does not imply equality of the complete arrays; the report does not make that invalid inference. |
| Lemma 2, lines 159–175 | A real symmetric tridiagonal N-matrix has 2N−1 parameters. The ordered full-minor spectrum map is locally Lipschitz, by eigenvalue perturbation inequalities; it cannot have an absolutely continuous image in N(N+1)/2 dimensions for N≥3. Dependence among entries cannot evade the bound. For fixed symmetric bandwidth w, replace the parameter count by (w+1)N−w(w+1)/2 (N>w). This excludes full absolutely continuous corners arrays, not singular arrays with the same single-level marginals. It does not exclude the positive Hermite or Laguerre examples. |
| Proposition 4, lines 269–303 | Multiplying the top density by K_n^θ leaves Δ(x)Δ(y) times the cross factors. Applying generalized DA with poles (0,y,1) and parameters (p+1,θ,…,θ,q+1) gives powers p+θ,q+θ at level n−1. The Laguerre limit gives α→α+θ at the same exponential rate. Thus full-rank all-size ordinary DA coherence would require p_n=p₁−(n−1)θ and similarly q_n, eventually nonintegrable. These are statements about that particular link. |
| Theorem 5, lines 309–349 | For the canonical size-two spectral model, the coordinate Jacobian is (λ₂−λ₁)²/(2b), and the entry density is Cb^(β−1)e^(−tr V(J₂)). Entry independence makes tr V separable. Letting b→0 and then setting the two diagonals equal gives V(a+b)+V(a−b)−2V(a)=h(b). C² regularity forces V″ constant; full-line integrability forces a positive quadratic coefficient. The converse factors at all n. The independent Dirichlet-weight assumption is indispensable; eigenvalue densities alone do not determine the entry density. This does not classify arbitrary independent-entry or dependent-entry realizations. |
| Theorem 6, lines 353–378 | At β=2, the scalar deletion density is proportional to F(y)=∫_(x<y<z)(z−x)w(x)w(z) dx dz. Writing truncated moments gives F′(y)=w(y)(m₁−ym₀). Coherence F=Cw implies (log w)′=(m₁−ym₀)/C and hence a Gaussian. The stated moment and positivity assumptions justify the differentiation. This is a same-weight ordinary-DA theorem on the whole real line at β=2, not a classification under all couplings or on arbitrary supports. |
| Proposition 7, lines 384–409 | In KN (1.11)–(1.12), let S=p+q+2, d=p−q. The three independent alpha means are d/S, d/(S+2θ), (θ−S)/(θ+S). Inserting them gives E[(b_N+2)/4]=1/2+d/[2(S+β)], whereas the desired scalar mean is 1/2+d/(2S). Correct for N≥2 and p≠q. It excludes that reversed KN model only. |
| Proposition 8, lines 413–419 | For a unitary block extension, the two upper-left unitarity identities imply vv*=ww*=0. Iterating from size one forces a diagonal sequence. Thus irreducible unitary CMV/Hessenberg prefix models are impossible. It does not by itself rule out dependent diagonal phases or nonnormal representations. The report explicitly retains this scope. |
| Arrow completion, lines 441–449 | The residues −P(y_j)/Q′(y_j) are positive under strict interlacing, and P/Q=z−a−∑v_j²/(z−y_j). The resulting arrow extension has the desired characteristic polynomial and can be conjugated in its old coordinates while preserving the old block. This realizes dense Hermitian arrays, not one Jacobi recurrence or a natural invariant law. |

For completeness, the failure of the reversed KN candidate extends to symmetric weights without a mean argument. If p=q and S=2p+2, write t=alpha_(2N−3), u=alpha_(2N−2), v=alpha_(2N−4). They are independent, the last diagonal is (1−t)u−(1+t)v, and

\[
 E u^2=\frac1{S+1},\quad E v^2=\frac1{S+2\theta+1},
 \quad E(1-t)^2=\frac{4S(S+1)}{(S+\theta)(S+\theta+1)},
 \quad E(1+t)^2=\frac{4\theta(\theta+1)}{(S+\theta)(S+\theta+1)}.
\]

Consequently the reversed scalar on (0,1) has variance 1/[4(S+β+1)], while Beta(p+1,p+1) has variance 1/[4(S+1)]. These differ for every β>0. The claim's narrower conclusion is correct, merely weaker than this calculation.

My numerical work was written independently in [code/referee_mc.py](code/referee_mc.py) and [code/referee_aux.py](code/referee_aux.py). Neither imports, executes, nor copies claim_files/code. The main experiment takes 50,000 independent samples of the primitive size-six B for each β∈{0.5,1,2,3.7}, a∈{−0.5,1.25}, and takes actual leading blocks at n=1,2,3,6 from the same L. Intermediate prefixes also check interlacing. Seed: 40002113112026. The target distributions are computed from the density, not from a second implementation of DE.

For n=1 the eigenvalue target is Gamma(θ(a+1),scale 2/β). At n=2, putting α=θ(a+1)−1 and

\[
 T=x_1+x_2,\qquad U=\left(\frac{x_2-x_1}{x_1+x_2}\right)^2
\]

in (R1), the Jacobian is T/(4√U). Thus T and U are independent with

\[
 T\sim\operatorname{Gamma}(2(\alpha+1)+\beta,2/\beta),
 \qquad U\sim\operatorname{Beta}((\beta+1)/2,\alpha+1).
\]

The code integrates this density to obtain both ordered eigenvalue CDFs and every cell of a 5×5 joint quantile grid. Explicitly the joint CDF at (x,y) is the beta-weighted integral of the gamma CDF at min{2x/(1−√u),2y/(1+√u)}. Endpoint-weighted quadrature handles negative hard-edge powers. This tests the size-two two-point law as well as its two one-point marginals. The ordered Selberg normalizer, independently checked against this change of variables, is

\[
 Z_{2}=\frac{c^{-K}}2
 \frac{\Gamma(\alpha+1)\Gamma(\alpha+1+\beta/2)\Gamma(1+\beta)}
 {\Gamma(1+\beta/2)},\qquad c=\beta/2,\quad K=2(\alpha+1)+\beta.
\]

At β=2 and n=3,6 the density has projection kernel K_n(x,y)=∑_(k=0)^(n−1)phi_k(x)phi_k(y), with

\[
 \phi_k(x)=\sqrt{\frac{k!}{\Gamma(k+\alpha+1)}}
 x^{\alpha/2}e^{-x/2}L_k^{(\alpha)}(x).
\]

Numerical integrals of rho₁=K(x,x) and rho₂=K(x,x)K(y,y)−K(x,y)² give expected counts and factorial pair counts in intervals (0,1], (1,4], (4,9], (9,∞). If M_I=(∫_I phi_i phi_j), the targets are tr M_I and tr M_I tr M_J−tr(M_I M_J), subtracting the diagonal count for I=J. Integrated orthogonality errors are at most 2.70×10⁻¹². One rare n=3 tail factorial count had zero empirical variance and expected value 1.44×10⁻⁵ per sample; the code records it as uninformative and does not apply an invalid Gaussian z-test.

Across all β and tested n, density homogeneity gives trace∼Gamma(θn(n+a),scale 2/β). Differentiating the Selberg Mellin integral gives E log det=∑_(j=0)^(n−1)psi(α+1+jθ)−n log(β/2). Integration by parts in the density gives E∑x_j²=n(n+a)(2n+a−1+2/β). I also rederived the last expression directly from independent gamma moments of the entries; the maximum discrepancy between those two calculations is 1.43×10⁻¹⁴. The size-two log normalizers agree to 2.11×10⁻¹⁵.

The final run made 175 positive tests. The smallest unadjusted p-value was 0.0128018181, and none rejected at 0.05 after Holm correction. The maximum absolute moment z-score was 2.22344. The prefix/product discrepancy was 7.11×10⁻¹⁵, reversal discrepancy 3.56×10⁻¹⁵, and maximum numerical interlacing violation 7.11×10⁻¹⁵. These are roundoff-sized identities, not substitutes for the proof. Main runtime was 3.02 seconds and peak RSS 334,921,728 bytes, with niceness 10 and one thread in each numerical library. There were no worker processes. The auxiliary 16 antisymmetric trace tests also have no Holm rejection (smallest raw p=0.00544); they are secondary checks, not complete distributional tests at larger N.

Results and quadrature probabilities are in [data/referee_summary.json](data/referee_summary.json), [data/referee_tests.csv](data/referee_tests.csv), [data/referee_moments.csv](data/referee_moments.csv), [data/density_integrals.json](data/density_integrals.json), and [data/referee_aux.json](data/referee_aux.json). The auxiliary program also recomputes the submitted data's 108-test Holm summary exactly, without running the submitted code. To reproduce the independent experiment, run `python3 code/referee_mc.py` and `python3 code/referee_aux.py` from this directory; the programs enforce one numerical thread and require or set niceness at least 10.

The literature supports the following precise conclusions. All locations are to the versions downloaded independently here, counted by PDF page; texts are linked locally and retrieval metadata is in [sources/retrieval.json.txt](sources/retrieval.json.txt).

| Primary source | What it establishes and what it does not establish |
|---|---|
| [Dumitriu–Edelman 2002](https://arxiv.org/abs/math-ph/0206043), Theorem 3.4, PDF p.14; [text](sources/dumitriu_edelman.txt) | Independent chi bidiagonal Laguerre model with the precise free shape parameter needed above. Reversal, transpose and singular-value invariance prove (a) with no additional finite-size theorem. I did not locate a separately stated all-size nesting theorem there. Calling the deduction elementary and declining novelty is justified; calling it historically first or certifying it as folklore would require evidence not obtained here. |
| [Killip–Nenciu 2004](https://arxiv.org/abs/math/0410034), Theorem 1 p.3, Theorem 2 p.4; [text](sources/killip_nenciu.txt) | Finite circular CMV and Jacobi models. Circular alpha_k∼Theta_(β(n−k−1)+1), with a terminal unit-circle alpha_(n−1). Earlier coefficients lie inside the disk and depend on n. A single irreducible infinite CMV matrix cannot have these unitary finite principal blocks. Paraorthogonal termination or changing boundary coefficients is a different construction. |
| [Edelman–Sutton 2008](https://math.mit.edu/~edelman/publications/beta-jacobi.pdf), Definitions 1.6/1.8 pp.7–8, Theorem 4.1 p.17; [text](sources/edelman_sutton.txt) | Finite β-Jacobi CS/bidiagonal-block model. Reversing the angle indexing is insufficient: the terminal sine/cosine boundary factor changes. This does not supply fixed-weight leading Jacobi blocks. |
| [Forrester–Rains 2005](https://arxiv.org/abs/math-ph/0211042), equations (4.35)–(4.38), p.26; [text](sources/forrester_rains.txt) | Random Jacobi recurrences have an x(x−1) multiplier on the earlier polynomial and parameters involving terminal n−j. They cannot simply be identified with the characteristic-polynomial recurrence of one Jacobi matrix. The Dirichlet-root/DA identity is also printed as Lemma 1.1 in the 2026 paper below, citing Forrester's book, Proposition 4.2.1. I have not audited that entire book. |
| [Dumitriu–Forrester 2010](https://arxiv.org/abs/0904.2216), (1.4), Theorem 1.1 pp.2–3, Section 6 pp.16–19; [text](sources/dumitriu_forrester.txt) | Exactly the antisymmetric finite laws used in (b), and their relation to Laguerre singular values. Reversal makes the all-size coupling immediate. This is prior published substrate, not a new ensemble. |
| [Neretin 2003](https://www.esi.ac.at/preprints/esi1262.pdf), Theorem 1.3, PDF p.9; [text](sources/neretin.txt) | Projective Rayleigh-triangle measures, including Hua–Pickrell families. This is coherent-array projectivity, not a fixed-bandwidth realization. Extraction has damaged glyphs, so I use the modern sources and independent transformations for precise parameters. |
| [Borodin–Gorin 2015](https://arxiv.org/abs/1305.3627), Definition 1.1 pp.3–4 and Section 1.5 p.8; [text](sources/borodin_gorin.txt) | β-Jacobi corners with rank min(k,M) and one-level powers θα−1 and θ(|M−k|+1)−1. The dimension obstruction to obtaining their full law from tridiagonal minors is already explained explicitly. This is neither the fixed-two-exponent family nor a negative theorem about every singular coupling. |
| [Gorin–Shkolnikov 2015](https://arxiv.org/abs/1401.5595), Definition 1.1 p.3, Theorem 1.2 p.4; [text](sources/gorin_shkolnikov.txt), and [Budway–Shkolnikov 2024](https://arxiv.org/abs/2403.10724), Theorems 1.1–1.2 pp.2–3; [text](sources/budway_shkolnikov.txt) | Multilevel Hermite dynamics and full corners. SDE constructions have the stated parameter restrictions; none is a Jacobi-prefix theorem for the other classical weights. |
| [Assiotis 2019](https://arxiv.org/abs/1609.03764), Theorem 1.1/Corollary 1.4 p.3; [text](sources/assiotis.txt) | β≥1 Laguerre/Jacobi intertwining relations with dimension-dependent parameter shifts. These support the distinction between fixed hard-edge power and ordinary deletion. |
| [Sun, 2016 preprint](https://arxiv.org/abs/1609.09096), Section 4.2 p.13 and Theorems 4.3/4.5 pp.14–16; [text](sources/sun.txt) | Generalized multilevel Wishart/Jacobi matrix laws at the specified classical β=1,2. Shared numerator/denominator Gram matrices or fixed-column chains do not turn matrix ratios into leading blocks of a single Jacobi matrix. |
| [Assiotis–Najnudel 2021](https://arxiv.org/abs/1905.08684), Theorems 1.13/1.16 pp.7–9 and Section 8 pp.36–37; [text](sources/assiotis_najnudel.txt), [TeX](sources/assiotis_najnudel_tex.txt) | Classification of coherent orbital-β arrays, plus Hua–Pickrell and inverse-Wishart examples. This is not a classification of potentials with a single tridiagonal prefix representation. Equation (28)'s Cayley convention needs correction as explained in item 1. |
| [Kawamoto–Shibukawa, ALEA 23 (2026), 255–273](https://alea.impa.br/articles/v23/23-10.pdf), Definition 1.5, equation (1.6), and Theorems 1.7–1.8; [journal text](sources/kawamoto_shibukawa_journal.txt), [preprint](https://arxiv.org/abs/2505.23139) | Fixed-parameter β≥1 Laguerre intertwining, using a composite kernel. The additional same-rank kernel has support 0<y₁<z₁<…<y_N<z_N, not ordinary codimension-one interlacing with the original top row. Already for a size-two top row x₁<x₂, one can have an intermediate z∈(x₁,x₂), then y∈(0,z) with y<x₁. Thus this kernel is not a principal-minor kernel and does not supersede (a)'s particular Jacobi realization. |
| [Bourgade–Najnudel–Nikeghbali 2013](https://arxiv.org/abs/1102.2633), Propositions 2.2/2.6 pp.8/10; [text](sources/virtual_isometries.txt) | Haar unitary virtual-isometry couplings. Projection of a block matrix is A+B(I−D)^(−1)C, where defined, rather than the principal block A. This is a positive circular coupling with a different operation. |
| [Valkó–Virág 2017](https://arxiv.org/abs/1604.04381), Proposition 20/Theorem 21 p.31; [text](sources/valko_virag_sine.txt), and [Valkó–Virág 2020](https://arxiv.org/abs/1710.06988), Theorem 1 p.2; [text](sources/valko_virag_circular.txt) | Finite circular spectra represented by Dirac operators, and a precise coupling with the limiting operator through n-dependent stopping-time arrays. Theorem 1 is convergence of inverses in Hilbert–Schmidt norm, not equality of successive finite leading blocks. |
| [Krishnapur–Rider–Virág 2016](https://arxiv.org/abs/1306.4832), Proposition 2 p.7 and Theorem 1 p.3; [text](sources/krishnapur_rider_virag.txt) | Canonical finite tridiagonal densities for polynomial potentials, with Dirichlet endpoint weights, and stochastic Airy limits under the stated regularity/convexity hypotheses. Existence of a matrix at every n and coupling for an operator limit do not imply exact prefix consistency. |
| [Nakano–Trinh–Trinh 2026](https://arxiv.org/abs/2601.13674), Theorem 1.2 p.5 and Theorems 4.3–4.4 pp.11–12; [text](sources/nakano_trinh_trinh.txt), and [Petrov–Xu 2026](https://arxiv.org/abs/2607.27810), Definition 3.4 p.11; [text](sources/petrov_xu.txt) | Respectively high-temperature spectral-measure limits with Nβ→2c, and perturbed Gaussian corners. Neither fixes β and proves fixed-weight Laguerre/Jacobi leading prefixes. |

Consequently a published theorem already implies the positive Laguerre answer, and the antisymmetric answer has equally direct published antecedents. I found no printed fixed-weight β-Jacobi Jacobi-prefix construction or unrestricted one-cut classification in the checked works. This is a bounded literature conclusion; [sources/SEARCH_LOG.txt](sources/SEARCH_LOG.txt) records scope and access limits. “Not a new finite model” is proved by identifying the exact old model. “Never printed before” and “known folklore” are historical assertions not established by these searches.

Exactly what remains unresolved by this work is whether, for prescribed β>0 and p,q>−1, there exists some possibly dependent sequence of Jacobi coefficients whose every degree-n polynomial has density Δ(x)^β∏x_i^p(1−x_i)^q on (0,1), and which other fixed full-line weights admit such a sequence when the spectral weights or interlevel links are unrestricted. The Gaussian proofs address only their canonical/ordinary-DA subclasses. Circular arrays and operator-limit couplings exist; irreducible unitary CMV principal-block nesting is excluded. These are separate conclusions, and none should be described as a complete answer for all couplings.

The statement actually proved is therefore: for every β>0 and every integrable fixed Laguerre hard-edge exponent, there is an explicit essentially self-adjoint nonnegative random Jacobi operator whose actual leading blocks have exactly those unscaled Laguerre laws at every size; there is also the explicit antisymmetric family, and the additional exclusions hold only in their stated classes. The constructions' value is an explicit positive answer and a clarification of scope, with limited novelty as a deduction from existing models. The designation PARTIAL is reasonable for the broader program, but it should not obscure that the literal request for other examples has a positive answer.

Task: “You are an independent referee … Break it if it is wrong.” — received 2026-11-13 10:12 +04 (Asia/Tbilisi).
