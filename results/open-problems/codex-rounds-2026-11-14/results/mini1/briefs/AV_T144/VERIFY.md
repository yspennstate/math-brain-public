# Verification of T144

Checked 14 November 2026 (Asia/Tbilisi). **Recommendation: keep T144 open.** The three supplied main statements do not claim GOE statistics for periodic boxes of the Anderson model on Z^3. This is a comparison of statements and a record of follow-ups, not an endorsement or rejection of their proofs.

## 1. Absolutely continuous spectrum: same lattice, different conclusion

**OpenAI, *Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three*, September 23, 2026.** Opened [build/paper.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/paper.tex) and [build/01-introduction.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex), not merely the catalogue description. Local copies: [title page](sources/AC-paper.tex), [introduction](sources/AC-introduction.tex). The source defines the operator by negative nearest-neighbor hopping plus lambda V, with V_x independent uniform on [-1,1]. A graph-Laplacian convention for -Delta adds a constant and translates the energy interval.

Theorem 1.1, copied exactly from the LaTeX source, including its labels:

```latex
\begin{theorem}\label{thm:main}
There is a fixed sufficiently small number $e_2\in(0,1/100)$ such that,
for every fixed integer $d\ge3$, there is a number $\lambda_d>0$
with the following property. Set
\begin{equation}\label{eq:energy-windows}
 I_d=
 \begin{cases}
   (-6+e_2/2,-6+e_2),&d=3,\\
   -2d+(1/200,1/100),&d\ge4.
 \end{cases}
\end{equation}
Then
for every fixed $0<\lambda<\lambda_d$, almost surely
\[
 I_d\subset\sigma(H_{\lambda,\omega}),\qquad
 \chi_{I_d}(H_{\lambda,\omega})\ell^2(\ZZ^d)
       \subset\mathcal H_{\mathrm{ac}}(H_{\lambda,\omega}).
\]
In particular, the spectral restriction to $I_d$ is purely absolutely
continuous and $\chi_{I_d}(H_{\lambda,\omega})\ne0$.
For $d\ge4$, one may take $\lambda_d=\sqrt3\,2^{-n_*(d)}$, where the finite-matrix
specification of $n_*(d)$ is given in Definition~\ref{def:threshold}.
For $d=3$, the proof supplies an existential positive threshold.
\end{theorem}
```

Here ZZ, CC and the other macros have their meanings in the saved paper.tex. The theorem asserts an almost-sure spectral-type property of the infinite-volume operator, not just a finite-scale bound, but the quantity is different from T144.

## 2. Pure-point spectrum: different dimension and regime

**OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026.** Opened [build/paper.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/paper.tex) and [build/sections/introduction.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/introduction.tex). Local copies: [title page](sources/PP-paper.tex), [introduction](sources/PP-introduction.tex). The model is positive nearest-neighbor hopping on Z^2 with independent v_x uniform on [-h,h]; thus h plays the role of lambda for the uniform example in T144.

Theorem 1.1, copied exactly:

```latex
\begin{theorem}\label{main:theorem}
For each fixed $h>0$, almost surely $H_v$ has pure-point spectral type,
admits a complete orthonormal eigenbasis, and has spectrum
\[
 \sigma(H_v)=[-4-h,4+h].
\]
Its eigenvalues are dense in this interval. The probability-one event
in this statement is allowed to depend on $h$.
\end{theorem}
```

The surrounding text expressly does not assert exponential eigenfunction decay or dynamical localization. Nor does this statement assert Poisson eigenvalue statistics: pure-point spectral type alone is not such a statistics theorem.

## 3. GOE universality: matching observable, different graph ensemble

**OpenAI, *Fixed-energy universality for weak Anderson disorder on random regular graphs*, October 5, 2026.** Opened [build/paper.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/paper.tex) and [build/sections/01-introduction.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex). Local copies: [title page](sources/RRG-paper.tex), [introduction](sources/RRG-introduction.tex).

The model defined immediately before the theorem is H_{n,d,w} = A_{n,d} + w diag(omega_1,...,omega_n), where A_{n,d} is the ordinary adjacency matrix of a uniformly random simple labelled d-regular graph and the omega_v are independent uniforms on [-1,1], independent of the graph. Here d is vertex degree, not spatial dimension. The measure nu_{d,w} is the expected root spectral measure of the corresponding infinite d-regular tree. The reference Xi_n^{GOE} is sum_i delta_{(n/pi) mu_i}, with mu_i the eigenvalues of normalized GOE (off-diagonal variance 1/n and diagonal variance 2/n).

Theorem 1.1, copied exactly:

```latex
\begin{theorem}[Fixed-energy universality]\label{thm:main}
For every $d\ge3$ and every $0<\kappa<2\sqrt{d-1}$, there is
$w_0=w_0(d,\kappa)>0$ with the following property.  For each fixed
$0<w<w_0$, the restriction of $\nu_{d,w}$ to an open neighborhood of
\[
 I_{d,\kappa}=[-2\sqrt{d-1}+\kappa,\,2\sqrt{d-1}-\kappa]
\]
has a continuous density $\rho_{d,w}$, strictly positive on
$I_{d,\kappa}$.  For every fixed $E\in I_{d,\kappa}$, set
\[
 \Xi_{n,E}=\sum_{i=1}^n
       \delta_{n\rho_{d,w}(E)(\lambda_i-E)}.
\]
Then, for every nonnegative $f\in C_c(\RR)$,
\begin{equation}\label{eq:main-laplace}
 \left|
 \EE\exp\left(-\int f\,d\Xi_{n,E}\right)
 -\EE\exp\left(-\int f\,d\Xi_n^{\GOE}\right)
 \right|\longrightarrow0
\end{equation}
as $n\to\infty$ through all sizes $n>d$ with $nd$ even.
\end{theorem}
```

This is a claim of the full microscopic point-process law at each fixed energy, expressed by convergence of Laplace functionals for every nonnegative continuous compactly supported test function. It is stronger than a spacing bound or energy-averaged statistic. The obstacle to matching T144 is the model and single-site-law scope, not the strength of this statistical conclusion.

## 4. Clause-by-clause comparison with our row

| Clause in T144 | Absolutely continuous spectrum paper | Two-dimensional pure-point paper | Random-regular-graph paper |
|---|---|---|---|
| H = -Delta + lambda V on Z^3 | Same nearest-neighbor infinite lattice model for the uniform example, up to the Laplacian convention | Z^2 instead of Z^3; positive-hopping convention on the infinite lattice | Random adjacency matrix plus diagonal disorder; graph edges are random as well |
| V_x iid with a bounded density, e.g. uniform [-1,1] | Uniform [-1,1] only; no theorem for all bounded densities | Uniform [-h,h] only; not all bounded densities | Uniform [-1,1] only; not all bounded densities |
| Small fixed lambda > 0 | Every fixed 0 < lambda < lambda_d | Every fixed h > 0, including small h | Every fixed 0 < w < w_0(d,kappa) |
| Dimension three | Included in every fixed d >= 3 | Excluded: dimension exactly two | No Euclidean dimension; d >= 3 denotes degree |
| Box [-L,L]^3 with periodic boundary conditions | Periodic finite lattices are intermediate proof objects; main conclusion is infinite-volume spectral purity | Finite tori appear in the proof plan; main conclusion is infinite-volume pure-point spectral type | Uniform random simple regular graphs with n vertices, with no lattice-box geometry or boundary condition |
| E in the bulk where states are extended | Only the displayed I_3 just above -6 (negative-adjacency convention); no result for arbitrary bulk extended energies | Whole spectral interval, with a pure-point conclusion | Any fixed E in the displayed compact interior of the clean tree band, once w is small enough |
| Rescaling by integrated density of states | No unfolded eigenvalue process | No unfolded eigenvalue process | Scaling n rho_{d,w}(E) using the infinite-tree DOS, not the Z^3 DOS |
| L tends to infinity at fixed disorder | No microscopic eigenvalue-statistics limit | No microscopic eigenvalue-statistics limit | n tends to infinity at fixed w, along nd even |
| Full GOE bulk point-process convergence | Not asserted, even for uniform potentials and E in I_3 | Not asserted | Asserted, but for the different ensemble above |

Taking degree d = 6 in the graph theorem does not produce the cubic lattice. Random 6-regular graphs have locally tree-like neighborhoods; the cubic lattice has short square cycles. Matching the number of neighbors does not match either the operator ensemble or its infinite-volume density of states.

There is also a wording issue in our target: the GOE bulk limit is the beta = 1 process, often called Sine_1. The scalar determinantal sine-kernel process is the beta = 2/GUE limit. The target should say “the GOE bulk point process” to avoid conflating them; the graph preprint specifies GOE directly through its finite-matrix reference. This terminological correction does not change the NOT-THIS verdict.

Thus the AC paper is relevant to the extended-state background (our T009), but does not claim any portion of T144's eigenvalue-statistics conclusion. The graph paper claims the analogous statistics on a different ensemble; it is not a special case of T144. The 2D paper concerns a separate localization problem. These are not grounds for marking T144 PARTIAL-CLAIMED.

## 5. Follow-ups actually opened

### A mathematical follow-up to the AC paper

Opened the [arXiv abstract](https://arxiv.org/abs/2610.11611) and [full HTML, including Appendix B](https://arxiv.org/html/2610.11611v1) of **Vojkan Jaksic and Yoram Last, *Extended States on the Bethe Lattice Revisited***, submitted October 8, 2026. These are the author spellings on the arXiv page. Appendix B, dated October 7, takes the OpenAI paper's positive-probability boundary-imaginary-part estimate as input and gives a shorter route from that input to spectral purity. Its final paragraph explicitly leaves the preceding finite-volume analysis unchanged. It is neither a proof audit of that input nor a lattice GOE theorem. The reference there uses the October 6 public-release date; the supplied manuscript's title-page date is September 23.

Opened the [arXiv page](https://arxiv.org/abs/2609.06987) of **Vojkan Jaksic, Yoram Last, Simone Warzel, *A Note on Extended States on the Bethe Lattice***, submitted September 7, 2026. It predates the supplied papers and is not a post-release follow-up. Its abstract concerns tree AC spectrum and an analogous conditional lattice criterion, not lattice eigenvalue statistics. Only its abstract page, not its full proof, was inspected.

Opened the [arXiv page](https://arxiv.org/abs/2611.08087) of **Jonathan P. Keating and Henrik Ueberschaer, *Multifractal scaling of quantum eigenfunctions in the thermodynamic limit***, submitted November 5, 2026. This search lead concerns point-like bump potentials in dimension at least five and eigenfunction multifractality; its abstract does not state T144. No claim about its full proof is made.

### Lean: distinguish the release from later third-party work

Opened the release's [lean/README.md](https://raw.githubusercontent.com/openai/math/main/lean/README.md), [formalization.yaml](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml), [family 261 scope note](https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md), and [PlanarAndersonSpectrum.lean challenge](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/PlanarAndersonSpectrum.lean). The scope note explicitly limits this formalization to existence/self-adjointness of the Z^2 operator and the almost-sure spectral set [-4-h,4+h]. The challenge agrees: it contains no pure-point, absolutely-continuous, or GOE conclusion. The challenge's sorry is its placeholder; it is not the separate solution proof. The family 219 scope-note URL returned 404, the catalogue provides no Lean link for family 219, and neither candidate title occurs in the formalization catalogue. No release formalization of these GOE or AC headline claims was identified.

A later, separate project does claim to formalize the lattice AC theorem: **Yao Xu, [anderson-ac-lean4](https://github.com/cadamcat/anderson-ac-lean4)**. Opened its [README](https://raw.githubusercontent.com/cadamcat/anderson-ac-lean4/main/README.md), [actual Challenge.lean](https://raw.githubusercontent.com/cadamcat/anderson-ac-lean4/main/AndersonAC/Challenge.lean), and [verification record](https://raw.githubusercontent.com/cadamcat/anderson-ac-lean4/main/docs/verification.md). The displayed target quantifies d >= 3, small uniform-distribution width, and an open interval carrying purely AC spectral measures with nonzero weight; it has no finite-volume eigenvalue-statistics clause. The author reports kernel replay and Comparator acceptance for v1.0.0, with only the three standard axioms; those checks were not rerun here and their proof dependencies were not audited here. The [MathDB submission](https://mathdb.com/p/389103/extended-states-in-the-anderson-model-in-dimension-3) records public release on October 14. This updates the AC background's formalization record, not the T144 verdict.

### Expositions, review scope, and negative findings

Opened the [arXiv page](https://arxiv.org/abs/2609.24426) and [v4 HTML introduction](https://arxiv.org/html/2609.24426v4) of **Xujie Lai and Fan Yang, *Localization Lengths for Two-Dimensional Random Band Matrices: Exponential Lower Bounds***, revised November 8, 2026. Its introduction calls the OpenAI 2D pure-point and d >= 3 AC results claims and discusses a qualitative localization consequence of the 2D paper's fractional-moment theorem, while noting a missing quantitative weak-disorder localization-length bound. This is relevant mathematical commentary, not a referee report or a lattice GOE claim. The October 18 v3 HTML, also opened under its earlier “Stretched-Exponential Lower Bounds” title, did not contain the OpenAI discussion.

Opened **Yao Xu, [*Extended states in the Anderson model: an exposition*](https://github.com/cadamcat/anderson-exposition)**, both its [README](https://raw.githubusercontent.com/cadamcat/anderson-exposition/main/README.md) and [article source](https://raw.githubusercontent.com/cadamcat/anderson-exposition/main/article/exposition.md). MathDB records v1.0.2 on November 6. It explains the AC claim and the later Lean project and states that the manuscript is not independently refereed. It supplies no lattice level-statistics result. MathDB also lists expositions by Halina Y.J Han and Jhon Supelano Rojas; their submission descriptions were opened, but their attached essays were not inspected, so they are not used as proof evidence.

Opened **Tejpal Virk (MathVet), [EXPLAINER.md](https://github.com/mathvet/mathvet/blob/main/EXPLAINER.md)**. Its review explicitly flags the release's spectral-set-only scope for family 261. It calls itself pre-referee and model-assisted; it is not an expert certification of the unformalized AC or graph proofs. Opened the [Plectis Atlas PlanarAndersonSpectrum page](https://wcook04.github.io/plectis-atlas/statements/PlanarAndersonSpectrum.html) as a cross-reference, then checked the primary scope note and challenge directly.

Opened the [fortnow/AI-Papers README](https://github.com/fortnow/AI-Papers/blob/main/README.md) and [kusasyu36/openai-math-audit README](https://github.com/kusasyu36/openai-math-audit). The former's named expositions concern complexity results; the latter had no Anderson-specific entry. Neither supplies evidence settling T144.

Opened the release's [README](https://raw.githubusercontent.com/openai/math/main/README.md), [CONTENTS.md](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md), [history.md](https://raw.githubusercontent.com/openai/math/main/history.md), and each candidate's README. The history through October 29 and the three candidate READMEs contain no Anderson correction or withdrawal notice. The repository itself describes its outputs as research data at different verification stages. Read-only issue searches for Anderson and the candidate titles in openai/math returned no issues. No same-title arXiv version, relevant refutation/error report, referee acceptance, or expert comment establishing lattice GOE statistics was found in the searches recorded in LOG.md. This is a search result, not a claim that no such item exists anywhere.

## 6. Recommended “where it stands” (three sentences)

> Wigner–Dyson/GOE bulk statistics for the weak-disorder Anderson model on Z^3 remain open; none of the three matched OpenAI preprints claims this lattice result. OpenAI's unrefereed *Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three* (September 23, 2026) claims purely absolutely continuous spectrum on a restricted interval for uniform potentials, and a later third-party Lean project claims to formalize that spectral-type theorem. OpenAI's *Fixed-energy universality for weak Anderson disorder on random regular graphs* (October 5, 2026) claims full fixed-energy GOE statistics for random regular graphs, while *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder* (September 23, 2026) concerns localization in two dimensions.

This replacement addresses the release-related status change. The older Poisson-statistics references in the supplied row were not independently rechecked in this verification.

## Attribution and source copies

All three preprints name **OpenAI** as author. The exact theorem excerpts above are reproduced from the opened LaTeX under the repository's Apache License 2.0; a copy is saved at [sources/LICENSE-openai-math](sources/LICENSE-openai-math). The excerpts are unchanged; comparison text is separate. Source snapshots and LOG.md preserve the evidence used here. No Lean build, numerical simulation, git command, or write outside this folder was performed.

## Spot check

Selected the **spectral-readout proposition**, label `prop:certificate-readout`, in the AC preprint's [build/09-spectral.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/09-spectral.tex), saved in [sources/AC-spectral.tex](sources/AC-spectral.tex). This is the load-bearing transfer from the adaptive finite-volume certificate to a statement about the actual Anderson resolvent. The following checks its finite-dimensional bridge carefully; it does not check the construction of the certificate in Sections 3–8.

Fix a true finite matrix H, energy E, height eta > 0, and any qualifying certificate (A,r). Let S be the real Schur complement after eliminating A^c, and write
\[
 \widehat G=(S-\eta R)^{-1},\qquad G_A=(S-i\eta)^{-1}.
\]
The assumption Im r >= p_- > 0 gives the norm bound
\[
 \|\widehat G\|\le(\eta p_-)^{-1}.
\]
Indeed, the imaginary part of the quadratic form of S-eta R has magnitude at least eta p_- times the squared norm. The identity
\[
 \widehat G-G_A=\widehat G\,\eta(R-i)G_A
\]
therefore gives \(\|\widehat G e_i\|\le C_R\|G_Ae_i\|\), with
\(C_R=1+(B+1)/p_-\). The Ward identity has the sign and ordering
\[
 \Im\widehat G=\eta\widehat G^*(\Im R)\widehat G.
\]
Consequently the certificate's lower diagonal bound implies
\[
 \eta\|G_Ae_i\|^2\ge c_*:=q_*/(p_+C_R^2).
\]
This confirms the first nontrivial comparison; it does not assume that damping only A equals damping the whole matrix.

For the more delicate compression step, put T=(H-E)^{-1}, \(B_A=P_ATP_A\), and
\(Q=\mathbf1_{[E-\epsilon\eta,E+\epsilon\eta]}(H)\). With
\(T_c=T(1-Q)\), \(B_c=P_AT_cP_A\), and \(f_\eta(u)=u/(1-i\eta u)\),
block inversion gives \(G_A=f_\eta(B_A)\). The noncommutative identity
\[
 f_\eta(B)-f_\eta(C)
 =(1-i\eta B)^{-1}(B-C)(1-i\eta C)^{-1}
\]
follows by multiplying on its two sides; it does not require B and C to commute. Thus \(D=f_\eta(B_A)-f_\eta(B_c)\) has rank at most rank Q, norm at most 2/eta, and squared Hilbert–Schmidt norm at most \(4\,\mathrm{rank}(Q)/\eta^2\).

The far-spectrum comparison also holds:
\[
 \eta\|f_\eta(B_c)e_i\|^2
 \le\eta\|B_ce_i\|^2
 \le\eta\|T_ce_i\|^2
 \le (1+\epsilon^{-2})q_i(E+i\eta).
\]
The first inequality is the scalar spectral calculus for the self-adjoint compressed matrix B_c; the second is projection contraction; the third follows from the scalar weight comparison outside the cut. No projection is commuted through Q, and no operator monotonicity is invoked. This matters because such shortcuts would not be justified for an adaptively chosen A.

Writing \(M_\epsilon=1+\epsilon^{-2}\) and
\(\Phi(u)=\min\{2M_\epsilon u,c_*\}\), the squared triangle inequality gives
\[
 \Phi(q_i)\ge c_*-2\eta\|De_i\|^2 \quad (i\in A).
\]
If the right side is negative this is automatic; otherwise both entries in the minimum exceed that right side. Summing confirms the paper's constant:
\[
 \frac1N\sum_i\Phi(q_i)\ge \frac{c_*}{2}
       -\frac{8\,\mathrm{rank}(Q)}{\eta N}
\]
on the certificate event.

A second derivation of the final scale is through direct counting: the spectral window has length 2 epsilon eta and each true diagonal variable has density \(1/(2\lambda)\). Own-site averaging therefore bounds
\(\mathbb E\mathrm{rank}(Q)\le N\epsilon\eta/\lambda\). With certificate probability at least 1/2,
\[
 \mathbb E\,N^{-1}\sum_i\Phi(q_i)
 \ge c_*/4-8\epsilon/\lambda\ge c_*/8
\]
when \(0<\epsilon\le\min\{1,c_*\lambda/64\}\). The factors of eta and N cancel as claimed. This expectation is under the original product law, without conditioning that law on certificate success. Thus the adaptive selection of A does not invalidate this use of own-site averaging.

The stated torus-to-lattice error also vanishes at the specified scales: \(L_m=4^{20m}\), \(\eta_m\asymp4^{-m}\), so \(\eta_mL_m\asymp4^{19m}\), whereas the logarithm of \(L_m^{d-1}\eta_m^{-2}\) is only of order m for fixed d. This supports the passage of the bounded Lipschitz observable to infinite volume.

**Finding:** no algebraic or conditioning error was found in this bridge. Its conclusion is positivity of a bounded function of the scalar boundary resolvent, followed in the paper by spectral purity. It gives neither a joint eigenvalue law nor a microscopic spacing estimate. The difficult existence/probability estimates for the certificate, the rest of the full proof, and the third-party Lean build remain outside this spot check; the verdict does not certify their correctness.


