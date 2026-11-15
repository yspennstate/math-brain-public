MINOR

The finite-mixture branching theorem and the regeneration lemma are correct under their written assumptions. I found no wrong Perron normalization, missing factor of two, invalid finite-type theorem application, or failure of exact-size admissibility. Independent calculations reproduce the nonconstant example's constant. An independently written conditioned sampler also agrees with the predicted CRT scaling for a genuinely type-dependent offspring law.

This is a valid partial result about an explicitly specified branching model. It does not prove Conjecture 7.2 for the interacting diffusions, or for general continuous kernels. Its mathematical novelty is limited: the main CRT conclusion is an elementary latent-type reduction followed by an existing finite-type theorem. The useful contributions are the careful variance correction and the quantitative regeneration calculations. The submission already discloses most of these limitations; they are not reasons to label its theorem false. Minor corrections to scope, the example, the literature discussion and the supplied archive are needed.

The following list distinguishes submission issues from defects in the underlying conjecture's formulation. Locations refer to the supplied, unchanged `claim_files/REPORT.md`; its complete file inventory and SHA-256 hashes are pinned in [independent_data/artifact_audit.json](independent_data/artifact_audit.json).

1. **The model identification is conditional, not established.** Locations: report lines 19–49, 286–325, 384, 483–487; source Section 4 and standing conventions. Theorem A specifies a common independent potential-child count, independent slots, child-side thinning by p(y), and a root strength law μ_i or a mixture. The source's preceding prose uses parent-side thinning p(x), while Definition 4.1 displays child-side thinning p(y). A mean kernel alone does not determine the offspring point process or sibling dependence. Neither an SDE realization of the mixture nor the original cascade's root law is supplied. The report correctly warns about the diffusion-to-branching transfer, but its description as a continuous-type subclass must remain attached to this chosen branching interpretation. Fix: describe Theorem A as a corollary for finite-mixture independent-slot branching trees; to claim a genuine special case of the diffusion conjecture, identify the full offspring/root laws and prove the conditional reduction. A comparison of mean operators is insufficient.

2. **The displayed nonconstant example reverses the source's response direction.** Locations: report lines 376–384; source Definition 4.1. With q_1=N(-0.8,1), q_2=N(0.8,1) and w_1(x)=0.5+0.2 tanh(x), its conditional mean strength is E[Y|x]=-0.32 tanh(x), strictly decreasing. The source describes forcing increasing with parent strength. The example satisfies the stated smoothness, tail and Wasserstein conditions, but it does not demonstrate that physical response property. Fix: retain it explicitly as an abstract analytic example, or reverse the sign of the weight and recompute all constants. Changing this sign alone would still not derive a diffusion realization. This issue does not affect Theorem A.

3. **The source archive cited by the submission is absent from the supplied package.** Locations: report lines 11, 55, 481; `claim_files/data/final_verification.json`; the manifest loop in `claim_files/code/verify_artifacts.py`. There is no `claim_files/sources/` directory, although the report and final verification describe 19 archived source texts. The verification loop silently skips missing files before its later directory check. This may be a transfer omission; I cannot infer that the earlier run never had those files. Fix: supply the referenced archive and make absence of any required source a verification failure. I independently recovered the central sources into this review's `sources/`; nine downloaded PDF/text hashes match the submitted manifest.

4. **The submitted experiments do not test its nonconstant finite-mixture theorem.** Locations: report lines 409–477 and `claim_files/code/simulate_ou_conditioned.py`. Constant transmission makes the shape an ordinary Poisson(1) or Binomial(2,1/2) GW tree; OU marks are added afterward. The nonzero-correlation OU kernel used there is not a finite mixture of fixed component laws. These are valid exact conditioned single-type experiments, as the report explicitly says, but they cannot validate the latent-type variance formula in a reproduction-dependent example. Fix: keep that limitation attached to the experimental claim, or add such an experiment. This review supplies one independently, below. The two submitted 100,000-vertex examples and all reported means/standard errors check out.

5. **The literature account needs a small extension and a restrained novelty claim.** Location: report Section 2. It omits the especially relevant Haas–Stephenson (2021), Theorem 4.1, as well as the Abraham–Delmas–Guo local-limit result and an explicit check of Lehéricy's recent work requested in the task. These do not resolve the general exact-size conjecture. Fix: add their actual type spaces and conditioning, and describe Theorem A's CRT conclusion as a corollary of established finite-type theory. I found no verified prior occurrence of this exact collection of regeneration identities, but this search does not certify their novelty.

6. **The source's spectral conclusions cannot be used as quantitative regeneration hypotheses.** Locations: source Theorem 5.1 and proof; submitted report lines 177–188 and 194–202. An L² spectral gap does not imply uniform total-variation ergodicity. For the stationary OU transition P(x,·)=N(rx,1-r²), 0<r<1, the Hermite eigenvalues are r^k and the operator is Hilbert–Schmidt, yet sup_x ||P^k(x,·)-N(0,1)||_TV=1 at every finite k. Also, for a Lebesgue density γ and reference density v, the Hilbert–Schmidt integral uses γ(x,y)²/v(y), integrated against ϖ(dx)dy; the source's displayed integral instead weights by v(y). Fix: prove the correct density integrability and a separate minorisation/drift estimate. The submission does this under stronger assumptions and does not rely on the invalid implication.

7. **The source's critical L² assertion is false if read literally.** Locations: source Theorem 6.1(3); submitted report line 188. For a critical ordinary GW process with positive offspring variance s², h=1 and E[Z_k²]=1+ks². Finite second moments do not give L² boundedness. If item (3) inherits supercriticality from item (2), it is not a critical input for Conjecture 7.2. Fix: specify that regime and independently formulate the critical assumptions. The submitted partial proof does not use the false critical assertion.

8. **The source's ordinary spine-averaged variance and i.i.d. count reduction are wrong in general.** Locations: source Corollary 6.2; submitted report lines 133–175 and equation (8). Spectral criticality does not make the ordinary count averaged under the spine law have mean one, and inherited types do not give independent type-blind offspring counts. For M=((1/2,1),(1/4,1/2)) with independent Poisson offspring counts by type, a=(1/3,2/3), b=(3/2,3/4), the spine distribution is (1/2,1/2). Its ordinary offspring mean is 9/8 and mixed variance 81/64; the correct Perron factorial variance is 9/8. I verified these values in rational arithmetic. Fix: use the weighted factorial variance, not ordinary counts in a scalar Otter–Dwass argument. The submission's correction is right.

9. **Regeneration alone leaves an exact-size conditioning gap.** Locations: report lines 278–280; source Programme 7.3. The block skeleton has i.i.d. offspring/decorations before conditioning, but conditioning the original tree means conditioning ΣC=n, with block mass C correlated with skeleton offspring B and path lengths. It does not mean fixing skeleton size. A joint lattice local limit, a conditioned path-length comparison and convergence of the vertex mass measure remain necessary. This is expressly acknowledged by the submission, not a hidden false proof step. Fix: preserve that limitation; do not advertise the regeneration lemma as a CRT theorem for all minorised kernels. The finite-mixture theorem bypasses this gap by using an exact finite-type genealogy.

The precise source statement and its definitions were checked against independently obtained text, not against the submitted paraphrase. The full nine-page paper is [sources/kumar_duddala_2608.21125v1.txt](sources/kumar_duddala_2608.21125v1.txt); the original TeX is [sources/kumar_duddala_original_tex.txt](sources/kumar_duddala_original_tex.txt). The unchanged relevant source environments, including the exact Conjecture 7.2, are collected in [sources/exact_definitions_and_conjecture.txt](sources/exact_definitions_and_conjecture.txt). This provides the literal statement, formulas and inherited assumptions without silently repairing its ambiguities. The source is [Kumar–Duddala, arXiv:2608.21125v1](https://arxiv.org/abs/2608.21125v1), submitted 21 August 2026.

Conjecture 7.2, on PDF page 8, assumes Theorem 6.1's hypotheses at ρ(K)=1 and an additional offspring exponential moment. It conditions the critical cluster on {|S|=n}, multiplies graph distance by Σ_c/√n, and asserts convergence to Aldous' CRT in Gromov–Hausdorff–Prokhorov topology, with an explicit positive constant built from σ²_off and ϖ_*. It supplies no formula for that constant. The following is the exact mathematical content of the definitions it invokes, together with what the paper leaves unspecified:

- The strength type is A∈ℝ, the failure overshoot. The standing convention (R2) and Programme 7.3 also allow (d,a)∈𝒟×ℝ, with a finite hazard-domain set 𝒟. The source does not give a general arbitrary-Polish-space theorem; ℝ and this finite product are its relevant Polish spaces.
- Γ(a,dA′) is the law of the child's strength given a transmitting parent of strength a. Definition 4.1 describes an OU stationary-plus-forced Gaussian response to forcing increasing in a. The displayed operator is exactly

  \[
  (Kf)(a):=\bar\nu\int_{\mathbb R}p(A')f(A')\Gamma(a,dA'),
  \qquad f\in L^2(\mathbb R,\varpi),\qquad
  \bar\nu=m_*=g''(1)/g'(1).
  \]

  Here ϖ is the Gaussian OU stationary reference law; criticality is exactly ρ(K)=1. The function p is the transmission probability, with the parent/child inconsistency described in item 1. No full continuous-type offspring point-process formula resolving that inconsistency is given.
- Theorem 5.1 assumes a jointly smooth Gaussian-type strength density with sub-Gaussian tails, p(a)∈[p_min,1], and Wasserstein-2 Lipschitz dependence of Γ(a,·) on a. It concludes compactness, a positive simple Perron eigenfunction h, a strict spectral gap, and uniform ergodicity of

  \[
  P=\rho(K)^{-1}h^{-1}K(h\,\cdot).
  \]

  The invariant probability it calls ϖ_* is the spine stationary law. A separate Harris, Doeblin or drift condition is not an assumption of that theorem. Its proof adds a bounded-mean description not stated quantitatively in the theorem.
- Theorem 6.1 defines Z_k=Σ_{|v|=k}δ_{A_v} and W_k=ρ(K)^{-k}⟨h,Z_k⟩. It asserts the martingale property; under ρ(K)>1 and E[⟨h,Z_1⟩log_+⟨h,Z_1⟩]<∞, a.s./L¹ convergence with positivity on survival; and, with an additional second moment, L² and weighted empirical-law convergence. The latter assertion has the regime problem in item 7. The conjecture uses the hypotheses of this theorem, not a valid already-proved critical invariance principle.
- Corollary 6.2 defines σ²_off exactly as Var_{ϖ_*}(number of failed children)∈(0,∞). It is an ordinary mixed count variance, not the weighted factorial variance. These quantities differ, including in the smooth submitted example.
- S is the failed cluster of the initially failed root; |S| counts vertices, including that root, not a generation size or survival time. The companion [arXiv:2608.15987v1](https://arxiv.org/abs/2608.15987v1), Section 2.1, gives the root potential-degree law g and the other vertices' size-biased forward-degree law. Theorem A replaces this with its explicitly stated root and common potential-child laws. No identification of those root conventions is proved.
- For the measure and CRT convention, the companion's Section 6.1 and Theorem 6.4 specify uniform probability on the cluster vertices and the tree coded by a normalized Brownian excursion e. Thus μ_n=n^{-1}Σ_{v∈S}δ_v, d_gr counts edges, and d_e(s,t)=e(s)+e(t)-2min_{[s∧t,s∨t]}e; μ_e is the pushforward of Lebesgue measure. The root is the class of 0. This fixes the e versus 2e ambiguity and makes the expected scale σ/2. The displayed formulation of Conjecture 7.2 itself abbreviates these conventions rather than redefining them.
- GHP means distributional convergence of the compact measured trees modulo isometry. Its rooted version additionally matches the distinguished roots. One may define rooted GHP by taking the infimum over common isometric embeddings of the maximum of root distance, Hausdorff distance between the spaces, and Prokhorov distance between their probability measures. Theorem A proves this stronger rooted version after discarding strength marks; no marked-tree convergence is asserted.
- Exact conditioning must be restricted to integers with P(|S|=n)>0. The conjecture does not separately state aperiodicity. Theorem A does better: all positive integers are admissible. The original source does not specify a continuous root-strength law, a quantitative offspring exponential-moment bound uniform in strength, a numerical Σ_c, or a fully unambiguous offspring law. An exact definition of these missing data cannot be extracted from it.

The same-conditioning/same-scaling check therefore has a qualified answer. For the independent-slot branching interpretation using the displayed child-side kernel, Theorem A is a genuine finite-mixture special case: the same vertices, total-size event, distances and uniform measure survive forgetting the latent labels. There is no discretisation error. Its scale is compatible with the source's excursion convention and is correctly derived, but equality to a specific source formula cannot be checked because none is supplied. It has not been established as a specialization of the original interacting SDE with its physical kernel and root law. The submitted report already warns that a finite-graph diffusion approximation would need control after rare-event conditioning; its quoted subcritical comparison bound is singular at criticality.

I audited the proof in the order of its actual dependencies. The following table covers the mathematical steps of Sections 3 and 4 rather than attributing the total-size theorem to a citation with different conditioning.

| Submission location | Independent check | Result |
|---|---|---|
| Lines 133–161, left/right eigenobjects and equation (1) | Integrate Pf=h^{-1}K(hf) against hℓ; expand Var_x(Σh(Y)). The Kh² and h² terms cancel under ℓK=ℓ. | Correct with ℓ(1)=ℓ(h)=1 and the stated integrability. |
| Lines 194–223, block killing and height | Remove the split kernel εζ from the spine and conjugate by h. K_0^k1=hP_0^k(1/h)≤(h_+/h_-)(1-ε)^k. | Correct; controls all interior descendants, not merely a single spine path. |
| Lines 225–239, exponential block moment | Apply the proposed supersolution e^{th(x)} to the recursion for e^{θ(C+B)}. Common exponential moments of D uniformly bound the quadratic remainder. The stated choice of θ leaves a positive linear slack. | Correct. Monotone iteration can start at 1; the block is a.s. finite by the height estimate. |
| Lines 241–258, regeneration type and critical skeleton | A terminal-success slot has measure (εh(x)/ν)ζ(dy)/h(y). Conditional terminal types are i.i.d. η, independent of the unrevealed block data. Solve the terminal-count resolvent. | Correct for independent slots and root η. This would fail as a blanket deduction for correlated offspring having the same mean kernel. |
| Lines 260–276, normalization and variance | Use π_*=εζΣP_0^k; conjugate to obtain ηΣK_0^k=(a_0/ε)ℓ. Solve the factorial second-moment recursion. | E_ηC=a_0/ε and Var_ηB=σ²/(εa_0), both correct. |
| Lines 286–303, theorem assumptions and latent sampling | Accepted class j has slot probability r_j(x)=c_jw_j(x), and conditional strength law μ_j=pq_j/c_j, independent of its parent's type. | Correct full offspring-law reduction, stronger than finite rank of a mean operator alone. |
| Lines 329–333, finite GW branching and hypotheses | Integrating each fresh strength under μ_i produces a fixed offspring-word law for class i. M_ij=νμ_i(r_j)>0; ρ(M)=1 by assumption; accepted count≤D. | Independence, irreducibility, criticality and common exponential moments all hold. |
| Line 333, leaves, nondegeneracy and exact-size support | Since p_+<1 and P(D≥2)>0, leaf, exactly-one-child and at-least-two-child events have positive probability for every class. Chains give every size. | Extinction possibility and nondegeneracy hold. Matrix primitivity and total-size span one are separate facts; both are checked. |
| Lines 335–347, variance | For distinct slots Q^{(i)}_{jk}=βμ_i(r_jr_k), including the diagonal factorial moment. | Gives precisely σ²=Σa_ib_jb_kQ^{(i)}_{jk}=(β/ν²)ℓ(h²). No ordinary count variance substituted. |
| Line 349, theorem and metric transfer | Apply Addario-Berry et al. Theorem 1.3 with λ=(1,…,1). Forgetting labels changes neither size nor the metric-measure space. | Correct rooted GHP conclusion. No unjustified upgrade from type-count conditioning. |
| Lines 353–370, eigenfunctions and Doeblin bound | Write K=CG, M=GC; calculate Gh=b, Kh=h, ℓK=ℓ and ℓh=1. Lower-bound P by a fixed hμ_j/b_j component. | Correct spectral identification, uniform h bounds, and explicit minorisation. The L² density condition supplies boundedness where an L² operator is discussed. |
| Line 349 and theorem height bound | Theorem 1.4 initially gives Ce^{-cx²/n}+Ce^{-cx}; total-size conditioning has H≤n. For x≤n, x≥x²/n; for x>n the probability is zero. | The stated sub-Gaussian simplification is valid. |
| Lines 386–394, Wasserstein regularity | Differentiate Gaussian-mixture quantiles. Uniformly positive component weights bound the integral of (F_1-F_2)²/f_s; the Gaussian tails make it integrable. | The W₂-Lipschitz argument is valid; it does not establish SDE realizability or increasing inheritance. |

The Perron/variance calculation can also be summarized without the latent construction. Normalize ℓK=ℓ, Kh=h and ℓ(1)=ℓ(h)=1. Then

\[
\pi_*(dx)=h(x)\ell(dx),\qquad
\sigma^2=\int\ell(dx)\,\mathbb E_x\sum_{u\ne v}h(Y_u)h(Y_v)
=\int\ell(dx)\operatorname{Var}_x\!\left(\sum_u h(Y_u)\right).
\]

The CRT distance scale for the excursion-coded tree is σ/2. In the common-D independent-slot model, β=E[D(D-1)] and the factorial integrand is βh(x)²/ν². These identities agree with the finite-type theorem's factorial moment tensor, not merely with a dimensional heuristic.

For regeneration, put a_0=η(h)=1/ζ(1/h). The independently rederived identities are

\[
\eta(dy)=\frac{\zeta(dy)/h(y)}{\zeta(1/h)},\quad
\mathbb E_x B=h(x)/a_0,\quad
\mathbb E_\eta B=1,\quad
\mathbb E_\eta C=a_0/\varepsilon,\quad
\operatorname{Var}_\eta B=\sigma^2/(\varepsilon a_0).
\]

In particular, ε√(Var(B) E C)/2=σ/2. This is a useful consistency check, not a substitute for the missing conditioned block theorem. The factorization requires withholding terminal strengths until their next blocks start. With that convention, the claimed i.i.d. decorations and skeleton are legitimate.

The independent numerical work is in [independent_simulation.py](independent_simulation.py); it imports no submitted code. [independent_data/results.json](independent_data/results.json) contains every parameter and check, and [independent_data/trees.csv](independent_data/trees.csv) contains every sample. The continuous strengths are integrated analytically into latent offspring probabilities; they are not replaced by a finite partition.

I used the submitted Gaussian components and nonconstant mixture weights, but took exactly two potential children and

\[
p(y)=\tau(0.55+0.15\tanh y),\qquad
\tau=0.91435266547724\ldots .
\]

This makes the mean matrix critical and equal, to numerical precision, to the matrix in the submitted Poisson example. Reproduction depends on the inherited strength: its mean is 2Σ_jc_jw_j(x), which varies with x, and both latent-class offspring laws differ. The root law is μ_1, as allowed by Theorem A. This is another example of the abstract branching theorem, subject to the same physical-model qualification in items 1–2.

Gauss–Legendre integration on [-12,12] with 480 nodes, checked against 320 nodes on [-11,11], gives

\[
\begin{aligned}
a&=(0.460856594943035,\ 0.539143405056965),\\
b&=(1.020372240050881,\ 0.982585929655916),\\
\sigma^2&=0.500436532807369,\qquad
\Sigma_c=0.353707694575397.
\end{aligned}
\]

The two quadratures differ in scale by 1.1×10^{-16}. This agreement is a numerical check, not a certified error enclosure. Left/right eigenvector residuals are at most 1.2×10^{-16}; the factorial and continuous variance formulas differ by 1.1×10^{-16}. For the original submitted Poisson-D example the same independent calculation gives ν=1.82870533095448, σ²=1.000873065614738 and Σ_c=0.500218218784247. The last value agrees with the claim to its reported precision; ν agrees within 1.2×10^{-14}. Its ordinary spine count mean 1.001027942204660 and variance 1.002246313432325 also reproduce, confirming that the raw-count and correct constants are different.

The sampler uses exact-total-size probability recurrences. Write L_i for the probability of no children, U_ij for the probability of the single-child word j, and V_ijk for the probability of the ordered two-child word (j,k). If r_0=1-r_1-r_2, these are μ_i(r_0²), 2μ_i(r_0r_j), μ_i(r_jr_k), respectively. With t_i(n)=P_i(|T|=n),

\[
t_i(1)=L_i,\qquad
t_i(n)=\sum_jU_{ij}t_j(n-1)
+\sum_{j,k}V_{ijk}\sum_{s=1}^{n-2}t_j(s)t_k(n-1-s).
\]

At each vertex of a prescribed remaining size, the sampler chooses its offspring word and child subtree sizes with probabilities proportional to the corresponding terms of this recurrence, then recurses. The conditional probabilities telescope to the original typed-tree probability divided by t_i(n). Consequently it samples exact conditioning, apart from floating-point quadrature/arithmetic; it uses no size window, MCMC, rejection threshold or approximate bridge. Every output has exactly n vertices. Exhaustive enumeration of every typed plane unary/binary tree through n=6 checks both this telescoping identity and the recurrence probabilities, with errors below 10^{-13}. Parent/depth/degree identities are checked for every sampled tree.

For H_n the maximum height and D_n the average vertex depth, the predictions are

\[
\frac{\Sigma_c H_n}{\sqrt n}\Rightarrow\max e,
\qquad
\frac{\Sigma_c D_n}{\sqrt n}\Rightarrow\int_0^1 e(t)dt.
\]

Their means are √(π/2)=1.2533141373 and √(π/8)=0.6266570687, respectively. The first CDF was evaluated from the Brownian-excursion maximum theta series; the second mean also follows by integrating the mean of a three-dimensional Bessel bridge, E[e(t)]=2√(2/π)√(t(1-t)). These give independent height and integrated-height normalizations.

| n | Samples | Scaled maximum height, mean ± SE | Scaled average depth, mean ± SE | Height KS distance to max e |
|---:|---:|---:|---:|---:|
| 500 | 600 | 1.13517 ± 0.00991 | 0.57680 ± 0.00558 | 0.1887 |
| 2,000 | 600 | 1.17755 ± 0.01051 | 0.59437 ± 0.00589 | 0.1251 |
| 10,000 | 600 | 1.22695 ± 0.01070 | 0.61336 ± 0.00604 | 0.0553 |

There is visible finite-size downward bias. At n=10,000 the height and average-depth means are about 2.46 and 2.20 Monte Carlo standard errors below the limiting means. This is not claimed to be an exact finite-n CRT fit or a statistical proof of convergence. As an additional normalization check, the recurrence's probabilities t_1(n), divided by b_1 n^{-3/2}/√(2πσ²), give ratios 0.997712, 0.999427 and 0.999885 at these sizes. No seeds or batches were discarded.

Reproduce with `python3 independent_simulation.py`. The fixed seed is 1515202611130917. The run took 28.70 seconds at nice 10, with one numerical thread and peak RSS 51,200,000 bytes on macOS. Thus it is well below the requested four-thread/4-GB bounds. It saves one full 10,000-vertex latent tree in [independent_data/example_tree.csv](independent_data/example_tree.csv). It does not claim a new 100,000-vertex reproduction-dependent experiment.

Separately, [audit_artifacts.py](audit_artifacts.py) independently recomputes all ten submitted sample-group means and standard errors from CSV, and reconstructs both submitted 100,000-vertex trees by breadth-first traversal. The binomial example has height 1,145 and width 222; the Poisson example has height 656 and width 494. Degrees, depths, parents and saved profiles are consistent. The submission contains 3,050 samples, including 450 at size 100,000. These checks validate its numerical records and exact-size constructions; historical runtime/resource reports cannot be independently reconstructed from the CSVs. None of the submitted programs was used to generate this review's trees.

The literature result is bounded but clear: I found no printed theorem, or retrieved preprint theorem, establishing the full general continuous/Polish-type exact-total-size GHP conclusion under precisely the source's assumptions. This is a search result, not a proof of nonexistence. The finite-mixture conclusion is already covered by finite-type theory after the exact latent reduction. The following are the relevant primary-source checks, through 13 November 2026:

| Work and location | What is actually proved | Applicability here |
|---|---|---|
| [Miermont (2008)](https://www.numdam.org/item/AIHPB_2008__44_6_1128_0/), (H), p. 1130; Theorem 2, pp. 1133–1134 | Finitely many types; critical, irreducible, nondegenerate offspring with finite second moments, plus small exponential moments for the conditioned height theorem. Conditioning fixes one type population. | Correct variance reference, but not literally the total-size theorem required here. Periodicity is handled by admissible subsequences. |
| [de Raphélis (2017), arXiv:1405.3916v3](https://arxiv.org/abs/1405.3916v3), Section 1.2, pp. 6–8; Theorem 2, p. 8 | Countable types, positive summable eigenvectors (HM), finite weighted factorial variance (HQ), and quantitative root-type return-height conditions (HR); an unconditioned forest-height invariance principle. | Neither a non-atomic type space nor exact-total-size-conditioned GHP. A continuous kernel does not return to a fixed strength singleton. |
| [Haas–Miermont (2012), arXiv:1003.3632](https://arxiv.org/abs/1003.3632), Theorems 5–8 | Markov-branching scaling principles and conditioned monotype GW applications. | Integrating hidden inherited types does not automatically give the size-only splitting law and asymptotics needed for application. |
| [Haas–Stephenson (2021)](https://doi.org/10.1007/s00440-021-01064-2), Theorem 4.1, printed p. 753 | Finite-type critical irreducible GW CRT convergence with finite second moments, conditioned on n vertices of type 1, with uniform mass on those vertices. | A relevant improvement over Miermont omitted by the submission; still finite types and a specified type count. It is not a general Polish-type exact-size result. |
| [Stephenson (2018), arXiv:1412.6911](https://arxiv.org/abs/1412.6911), Theorem 3.1 | Local convergence of finite-type trees conditioned to be large to an infinite Kesten tree. | Different topology and limit from compact rescaled CRT convergence. |
| [Abraham–Delmas–Guo (2018), arXiv:1511.01721](https://arxiv.org/abs/1511.01721), Theorem 3.1 | Local limit under large type-population conditioning, with primitive mean matrix and lattice hypotheses. | Does not imply the global CRT conclusion. GHP metric foundations in Abraham–Delmas–Hoscheit are likewise not a branching invariance principle for arbitrary type marks. |
| [Kortchemski (2013), arXiv:1109.4138](https://arxiv.org/abs/1109.4138), main conditioned contour theorem | Exact progeny conditioning for a monotype GW law in a stable domain of attraction, using a local absolute-continuity argument. | Illustrates precisely why exact-mass conditioning needs local control. It is not a general inherited-type theorem; no such conclusion was found in the requested 2015–2026 search either. |
| [Lehéricy (2025), arXiv:2510.12034](https://arxiv.org/abs/2510.12034), Section 2.2 and 2.4, pp. 5–8 | Critical centered BRW displacement tails and total-weight limits under a large maximum-displacement/decorations event; the multitype application explicitly restricts to finitely many types. | Different conditioning. It does not supply exact vertex-count conditioning for the cascade. |
| [Foutel-Rodier, arXiv:2412.16035v1](https://arxiv.org/abs/2412.16035v1), Assumptions 1–2; Theorems 1.1–1.2; Corollary 1.3 | Genuine discrete-time Polish-type theory: bounded continuous positive h, normalized left eigenmeasure, uniform mean convergence, uniform moments of all orders and continuous count second moment; a uniform Kolmogorov estimate upgrades excursion convergence to marked GHP, with survival-conditioned and forest consequences. | Highly relevant, but no theorem conditioning on a single exact total mass. The source's L² gap does not establish its uniform hypotheses. |
| [Horton–Powell, arXiv:2601.05906v2](https://arxiv.org/abs/2601.05906v2), Assumption 1, pp. 2–4; Theorem 2, p. 5 | Continuous-time branching Markov genealogy under survival to time n, with occupation/lifetime mass, in Gromov–Hausdorff–weak topology. Assumptions include bounded branching/second moments, uniform Perron mixing, extinction, a pair-offspring lower bound and a generator-domain condition. | Different time model, conditioning and mass. The following paragraph explicitly treats discrete time as an expected extension. |
| [Addario-Berry–Beltran–Stufler–Thévenin, arXiv:2507.23241v2](https://arxiv.org/abs/2507.23241v2), Theorems 1.3–1.4 and equation (1.3), pp. 5–6 | Finite-type irreducible critical trees with exponential moments, extinction possibility and nondegeneracy, conditioned on a nonnegative integer linear combination of type populations. Rooted GHP CRT and height tails. | This directly proves Theorem A's conclusion with λ=(1,…,1). Normalizations are a·1=a·b=1 and c_scal=(σ/2)√(λ·a), hence σ/2 for total size. |

The first nine central texts and four additional relevant texts are archived only as plain text, with retrieval URLs and hashes in [source_manifest.json](source_manifest.json) and [additional_source_manifest.json](additional_source_manifest.json). The extra manifest also records an explicitly rejected wrong-identifier retrieval; its unrelated text was removed and was never used. No PDF, paper image or scan was retained. Public availability of a preprint is not represented here as proof of journal publication.

What is proved is exactly this: for the specified common-D independent-slot branching model, a finite uniformly positive mixture of fixed child-strength laws, bounded nontrivial thinning, critical finite latent mean matrix, exponential potential-child moment and an allowed mixture root law imply an unmarked rooted GHP CRT limit under exact total vertex count, with scale (1/2)√((β/ν²)ℓ(h²)). Under bounded positive h and a global spine minorisation, the separate lemma proves exponential block-height/mass/offspring estimates and the stated regeneration identities. The latter estimates do not themselves prove a general exact-size CRT theorem. The main finite-mixture limit is correct and follows from existing finite-type results; the original diffusion conjecture and its general continuous-type exact-size version remain unproved by this submission.

Task: “You are an independent referee … open problem G0015 … Break it if it is wrong” — received 2026-11-13, 11:17 +04 (Asia/Tbilisi).
