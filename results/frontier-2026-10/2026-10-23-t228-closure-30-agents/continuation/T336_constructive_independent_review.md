# T336 constructive route: independent mathematical and quantifier review

Agent 27, 23 October 2026. Internal research review, not external peer review or formal proof-assistant certification. No frozen campaign file was edited.

**Disposition: accepted at the scope stated below.** I found no remaining fatal mathematical, architecture, or quantifier gap in the pinned compiler and statistical argument. The result establishes exact all-real-label representation for a specified finite-rank polynomial GP in the explicitly defined architecture, and a separate prior-averaged KL guarantee for non-singleton structured ERM. It does **not** establish uniform-all-label KL convergence of the learned predictors. The latter distinction is necessary, not cosmetic.

## 1. Exact inputs and accepted scope

These are the final snapshots read for this acceptance. Future edits are not silently covered.

| File | SHA-256 |
|---|---|
| `a02/T336_REGISTRY.json` | `a62961f2c1f30287356a73e9609430d437e93ba42a85aaad85908fdbd2d5f7d6` |
| `followup/T336_architecture_compiler.md` | `8dbb67bbc8609cb86b0a1fb888f61c64abf36b07c8ebfc0464b0d0e5a4adf175` |
| `followup/T336_scope_and_obstruction.md` | `5c1ea4e7c3691c4eef8814b25ede5ebb9997b476c524fbf674cfed55b9bb75d0` |
| `followup/T336_barrier_literature.md` | `9fb9458e535615c2311485d7e819a949f0fb06311b923fa2172e5bf65eaf27b1` |
| `followup/T336_unbounded_label_independent.md` | `82ebfbbee8cca6d7f8ac1a797b5f605e7e25507bdffdd6d3b51f9a3a25ef4f44` |
| `followup/check_exact_gp_normalization.py` | `fe97bce47992876b0ac3dc74a23e433d10fb21df45066a2014b0026ca473b4de` |
| `followup/check_exact_gp_normalization.json` | `83fb1167ed5143dad392bb9606dc026719f55c56a4a3de80a5d4b263c6e93b26` |
| `followup/check_T336_architecture_compiler.py` | `583d017c0fbc0c5f6251ca66c24f0c108c119083b59a97521b06d020d3a6ea6a` |
| `followup/check_T336_architecture_compiler.json` | `1017cfadb92d420fc7c6f307ade62baa99ae6b6f79e9117db685bf16e170dfb6` |

The registry asks for transformer size, pretraining sample complexity, and convergence to Bayes, for a given prior, with posterior approximation uniform over datasets. Its wording does not resolve every architectural or learning-metric convention. The accepted concrete theorem is:

> Fix a known finite-rank polynomial feature map on a compact raw-input domain, a Gaussian coefficient prior, positive fixed Gaussian observation-noise variance, a finite maximum context length, and one noisy query. The costed bidirectional residual ReLU-attention architecture, augmented by one controlled ordinary full-token pre-LayerNorm FFN and a final unnormalized raw-label attention readout, exactly represents the posterior predictive for every permitted design and every real context-label vector. A larger non-singleton compact parameter box with the stated fixed structural constraints admits the explicit approximate-ERM prior-average forward-KL bound, for independent tasks and exogenous designs.

The feature-input variant is also valid for supplied bounded finite-dimensional features. Exact arbitrary raw-input feature computation is not free. The raw polynomial variant supplies and costs that computation.

The mathematical conclusions are narrower than claims about arbitrary GP kernels, RBF kernels with arbitrary real labels, all priors, stock softmax Transformers, or a network with every residual branch pre-normalized. The construction uses arbitrary real constants and exact real arithmetic. It is not a finite-bit or numerical-stability result. The statistical conclusion concerns approximate full-box ERM, not SGD or another unproved optimizer. Multiquery algebra is described in the compiler, but the displayed complete counts and the ERM theorem audited here are for one query.

I derived the identities and inequalities below directly. Other agents' agreement or review verdicts were not used as mathematical evidence.

## 2. Posterior algebra and the positive determinant identity

Write the context feature matrix as \(\Phi\in\mathbb R^{n\times r}\), the query feature as \(q\in\mathbb R^r\), and the observation-noise variance as \(s>0\). With \(G\sim N(0,I_r)\) and \(y=\Phi G+\xi\), define

\[
H=sI_r+\Phi^T\Phi,\qquad \Delta=\det H.
\]

Completing the Gaussian square gives posterior coefficient mean \(H^{-1}\Phi^Ty\) and covariance \(sH^{-1}\). Therefore the noisy query predictive is

\[
N(a^Ty,v),\qquad a=\Phi H^{-1}q,\qquad
v=s+s q^TH^{-1}q.
\]

These formulas remain valid for repeated inputs, padded zero rows, and rank-deficient \(\Phi\), since \(H\succeq sI_r\). There is no nonsingularity assumption on the unregularized Gram matrix.

Apply Cauchy–Binet to the \((n+r)\)-by-\(r\) matrix obtained by stacking \(\Phi\) and \(\sqrt{s}I_r\). In a selected set of \(r\) rows, let \(k\) be the number drawn from \(\Phi\). Expansion along the \(r-k\) selected identity rows leaves a \(k\)-by-\(k\) minor of \(\Phi\), with squared factor \(s^{r-k}\). Each row/column minor occurs once. Hence

\[
\Delta=s^r+\sum_{k=1}^{\min(n,r)}
\sum_{|I|=|J|=k}s^{r-k}(\det\Phi_{I,J})^2
=s^r+\sum_{\ell=1}^{M-1}u_\ell^2,
\quad M=\binom{n+r}{r}.
\]

The weighted minors \(u_\ell=s^{(r-k)/2}\det\Phi_{I,J}\) require only fixed real constants, additions, and products. No data-dependent square root or division is hidden here. The identity for \(M\) is Vandermonde's identity. The empty minor supplies the strictly positive constant necessary for the normalization trick.

I checked the standard Gaussian posterior formulas against the primary GPML Chapter 2 text, and the all-minors Cauchy–Binet identity against Knill's primary paper, arXiv:1306.0062v3, Theorem 7 and its corollaries. The identities above are also proved directly, so acceptance does not rest on a quotation or another review's interpretation. The local Knill PDF checked had SHA-256 `0a10d76bf619c39c911333e47f003f1efb1504c09a0bc648489488f6ee137e5a`.

## 3. Full-token LayerNorm really computes the reciprocal

The final compiler supersedes the intermediate projected-normalization presentation with an ordinary full-token LayerNorm. This distinction was checked against the actual register inventory.

There are \(N=n+2\) tokens: contexts, query, and scratch. Each has immutable local design, raw label, positional one-hot vector, and balance coordinate \(-p\), where \(p\) is the scratch-position indicator. Scratch local design and label are zero. There is **no additional constant-one register**. On scratch, \(p=1\) supplies all constants; on sources, \(p=0\).

Immediately before normalization, the fixed preparation layer clears all copied design and arithmetic registers and writes the paired weighted minors and special pair. Thus the complete nonzero scratch inventory is

\[
(\lambda u_1,-\lambda u_1,\ldots,
\lambda u_{M-1},-\lambda u_{M-1},1,-1,1,-1).
\]

The last pair is the immutable position/balance pair. The vector has mean zero and squared norm \(2\lambda^2\sum u_\ell^2+4\). With the **actual full embedding width** \(D\) and fixed normalization floor \(\epsilon>0\), set

\[
\lambda^2=\frac{4+D\epsilon}{2s^r}.
\]

Then the full-token normalization denominator satisfies

\[
\operatorname{den}^2
=D^{-1}\|h_\star\|^2+\epsilon
=\frac{2\lambda^2}{D}\Delta.
\]

A fixed two-unit residual FFN selects the difference of the normalized special coordinates, using \(\operatorname{ReLU}(t)-\operatorname{ReLU}(-t)=t\), and writes it to a fresh zero register. On scratch this yields \(z=2/\operatorname{den}\). Two arithmetic gates then give

\[
\rho=\frac{\lambda^2}{2D}z^2=\frac1\Delta.
\]

On a source, both special input coordinates are zero. Their normalized values are identical, even though their common mean and denominator can depend on an arbitrarily large source label. Their difference is exactly zero. The entire source token is unchanged by this FFN because it writes only that difference into its fresh register.

This cancellation requires the fixed unit LayerNorm gains, zero biases, and fixed difference selector specified in the compiler. It would not follow for independently trainable gains or selectors. The final trainable class keeps those entries fixed, so the cancellation is an identity for every parameter value, not only at the comparator. All calculations remain defined because \(\epsilon>0\).

The actual width is chosen first and then fixes \(\lambda\). This is not a circular complexity definition: changing a fixed coefficient after allocating the registers adds no gate or register.

## 4. Attention compilation and source-label isolation

I checked the primitives using the displayed attention update, including its fixed \(1/N\) factor.

* Gathering position \(j\) uses query \(p_i\), key \((e_k)_j\), and value \(Nd_k\). Exactly the scratch-to-\(j\) edge has score one. All source work registers remain zero.
* An affine gate uses the scratch self-edge with both query and key \(p\), and value \(N(\alpha a+\beta b+cp)\). The offset is scratch-local; it does not introduce a constant on source tokens.
* A multiplication gate uses two signed heads with queries \(\pm a\), key \(b\), and values \(\pm Np\). Their sum is \(ab\) on scratch and zero elsewhere, for arbitrary signs and magnitudes.
* Preparation can simultaneously subtract old work coordinates and route their linear combinations, since attention values are evaluated on the pre-update state. It therefore clears registers without destroying the minors before they are copied into the normalization pairs.
* A second fixed gather reloads immutable source design after normalization. Cleared raw feature calculations are recomputed; no necessary intermediate is assumed to survive erasure.

The post-normalization arithmetic forms

\[
C=\operatorname{adj}(H),\quad t=\rho Cq,
\quad a=\Phi t,\quad v=s+s q^Tt.
\]

The final two heads use queries \(\pm a_i\), context-position keys, and values \(\pm Ny_j\). At scratch their signed scores produce \(a_jy_j\), including when either factor is negative. Non-context keys and all non-scratch coefficient queries are zero. A fresh mean coordinate therefore receives exactly \(a^Ty\). The readout selects the mean and variance directly; it does not supply a hidden rational Gaussian decoder.

For the larger trainable class, all allowed arithmetic/feature entries can vary while their scratch-working read/write supports remain architectural constraints. Input placement, immutable labels and design, gathers, preparation, normalization selector, output clips, and final label readout remain fixed. Source work registers are zero by induction for every parameter vector. Consequently no earlier branch can read a raw label, and the coefficient and variance branches are design-only throughout the box.

Freeing the signed-head coefficients need not preserve their ideal arithmetic identities away from the comparator. That is harmless: the statistical proof needs a bounded design-only branch with finite parameter sensitivities, and an exact comparator inside the class. It does **not** assume every parameter setting computes a correct determinant or product circuit. The final statistical text appropriately propagates sensitivities through the scalar expansion of the actual trainable attention matrices.

## 5. Counts, raw features, and a genuinely non-singleton class

I independently recounted the displayed circuit. Define

\[
G_{\min}=\sum_{k=1}^{\min(n,r)}\binom nk\binom rk
\big[k!(k-1)+1\big],
\quad
G_{\rm adj}=r^2\big[(r-1)!\max(r-2,0)+1\big].
\]

The minor term counts each Leibniz product and one affine sum. The adjugate term covers every cofactor and correctly includes the rank-one constant adjugate. The total

\[
S=nr^2+2r^2+nr+n+3r+3+G_{\min}+G_{\rm adj}
\]

equals: \(nr^2+r^2\) for \(H\), both determinant/adjugate terms, two reciprocal gates, \(r^2+r\) for \(Cq\), \(r\) for multiplication by \(\rho\), \(nr+n\) for \(a\), and \(r+1\) for \(v\). Only the minor circuit runs before erasure; \(H\) is computed afterward.

The width

\[
D=N(F+1)+S+2M+4
\]

accounts for \(NF\) local/copied design coordinates, \(N\) positions, \(S\) arithmetic slots, \(2M\) normalization slots, and four further coordinates for raw label, balance, normalized scalar, and mean. The exact comparator uses at most \(S+5\) stages, at most \(\max(n+1,2)\) attention heads, and a two-unit normalized FFN. Its conservative stored count

\[
3(S+4)\max(n+1,2)D^2+8D
\]

counts attention matrices, normalized FFN matrices, normalization gain/bias, and the two-output readout. It deliberately includes fixed and zero entries. Fixed input placement/position constants follow the explicitly stated register-input convention.

If raw polynomial features in \(d\) variables have at most \(T\) monomials and degree at most \(d_\phi\) per coordinate, use \(F=d+1\), including presence. The bound

\[
E_\phi=(n+1)r[T\max(d_\phi-1,0)+1]+nr
\]

counts evaluation and context masking. Replacing \(S\) by \(S+2E_\phi\) correctly accounts for evaluation both before and after erasure. Constants and zero-degree features are covered by the affine sum gate. Polynomial coefficients are fixed finite real weights. For the stated quadratic feature example, independent substitution gives

\[
S=34n+69+9\binom n2+13\binom n3,
\qquad
D=3n+10+S+2\binom{n+3}{3},
\]

agreeing with the final statistical report.

If \(\|\phi\|\le R\), then \(s\le v\le V=s+R^2\) and

\[
\|a\|_2^2=q^TH^{-1}(H-sI)H^{-1}q
\le q^TH^{-1}q\le R^2/s.
\]

Role-scaled coordinate clipping to \([-A,A]\), \(A\ge R/\sqrt{s}\), and variance clipping to \([s,V]\) preserve the exact comparator and all source zeros. The variance lower endpoint is \(sp\), not an unconditional source offset. This adds one stage and \(4D(n+1)\) dense FFN entries, giving clipped depth \(S+6\).

For \(n\ge1\), the existing coefficient affine gates can include offsets \(b_jp\), with \(b_j\in[-1/2,1/2]\). Taking \(A=1+R/\sqrt{s}\) makes these perturbations survive clipping. Thus there is a non-singleton subfamily without adding a layer or register. The actual ERM theorem is for the larger class of all permitted free arithmetic/feature coefficients, with this bias family only a witness. The free parameter dimension \(P\) and the count of all stored fixed/zero entries are correctly kept separate.

## 6. Independent check of the ERM proof and constants

Let \(Z\) be the complete exogenous design, independent of the GP/noises. Each task draws a fresh independent GP and noises; tasks are independent. Conditional on \(Z\), the padded context labels \(y\) and noisy query target \(Y\) are centered jointly Gaussian, with marginal variances at most \(V=s+K\), where \(K=\sup_x\|\phi(x)\|^2\).

For every allowed parameter,

\[
q_\theta=N(a_\theta(Z)^Ty,v_\theta(Z)),\qquad
\|a_\theta\|_2\le C,\quad s\le v_\theta\le V.
\]

The output clips enforce these bounds without clipping any label or the final mean. The exact comparator belongs to a sufficiently large finite box \([-W,W]^P\).

### Loss envelope and concentration

For the shifted negative log likelihood

\[
\ell_\theta=\tfrac12\log(v_\theta/s)
+\frac{(Y-a_\theta^Ty)^2}{2v_\theta},
\]

the conditional residual is centered Gaussian specifically because \(a_\theta\) is design-only. Its variance is at most

\[
T=V(1+\sqrt n C)^2.
\]

Set \(A_0=\log(V/s)/\log2+2T/s\). Direct Gaussian-square integration gives \(E\exp(\ell_\theta/A_0)\le2\): each of the deterministic and Gaussian factors is at most \(\sqrt2\). Thus \(E\ell^k\le2k!A_0^k\). Expanding the positive centered MGF, and using \(e^{-t}-1+t\le t^2/2\) on the negative side, yields

\[
\log E e^{\lambda(\ell-E\ell)}
\le \frac{2A_0^2\lambda^2}{1-A_0|\lambda|}.
\]

The resulting two-sided bound is exactly

\[
\Pr\!\left(\left|(P_J-P)\ell_\theta\right|>
A_0[\sqrt{8u/J}+u/J]\right)\le2e^{-u}.
\]

No bounded-label claim is used. Population excess loss over the exact comparator equals prior-average forward KL, with finite conditional entropy and integrable losses.

### Covering the full trainable box

Suppose the output parameter sensitivities are \(L_a,L_v\) as in the final report. Put

\[
D_0=(n+1)V,\qquad
G_0=\frac{L_a\sqrt{1+C^2}}s+
\frac{L_v(1+C^2)}{2s^2}.
\]

Differentiating along the line between two admissible output pairs gives

\[
|\ell_\theta-\ell_{\theta'}|
\le\left[\frac{L_v}{2s}+G_0(\|y\|^2+Y^2)\right]
\|\theta-\theta'\|_\infty.
\]

The coefficient ball and variance interval are convex, so the interpolation stays in their bounds. The conditional covariance trace of \((y,Y)\) is at most \(D_0\). The Gaussian-square MGF and \(\prod_i(1-u_i)\ge1-\sum_i u_i\) imply

\[
E e^{(\|y\|^2+Y^2)/(4D_0)}\le\sqrt2.
\]

Consequently the stated event

\[
P_J(\|y\|^2+Y^2)\le Q_J
=2D_0\log2+\frac{4D_0\log(2/\delta)}J
\]

has failure probability at most \(\delta/2\). A radius-\(\rho\) parameter net has at most \((2+2W/\rho)^P\) elements. Taking

\[
u=P\log(2+2W/\rho)+\log(4/\delta),
\quad C_{\rm pop}=L_v/(2s)+G_0D_0,
\quad C_{\rm emp}=L_v/(2s)+G_0Q_J,
\]

the union bound plus the preceding loss sensitivity proves the claimed full-class deviation bound. Comparing a \(\xi\)-approximate ERM to the exact comparator yields

\[
R(\widehat\theta)\le\xi+
2A_0[\sqrt{8u/J}+u/J]
+2\rho(C_{\rm pop}+C_{\rm emp}).
\]

I also checked the explicit sufficient sample size: with the report's \(\bar C\), \(\rho=\min\{1,\varepsilon/[8(\bar C+1)]\}\), and \(\xi\le\varepsilon/4\), the conditions

\[
J\ge\max\{1,512A_0^2u/\varepsilon^2,8A_0u/\varepsilon\}
\]

bound the net term, square-root term, linear concentration term, and optimization error by \(\varepsilon/4\) each. The constants are sufficient as written.

### Parameter sensitivities and existence

The affine, product, ReLU, and clip recurrences in Section 5.3 are valid. LayerNorm with positive floor has Euclidean Lipschitz constant at most \(\epsilon^{-1/2}\), obtained by differentiating the radial normalization after the orthogonal mean-subtraction projection. Its coordinates have magnitude at most \(\sqrt D\).

An essential qualification is handled correctly in the final version: source normalization inputs contain unbounded labels and cannot be assigned a compact-design register bound directly. The fixed source contribution is identically zero for every parameter. Algebraically pruning that branch leaves only the label-free scratch normalization. All remaining inputs lie in a bounded design domain, all parameter entries in a compact box, and the finite scalar expansion supplies finite computable \(L_a,L_v\).

Continuity and compactness give existence of empirical minimizers; the theorem also permits approximate minimizers. Controlled capacity growth can retain the exact comparator and choose sample sizes for the displayed bound to tend to zero. Summable failure probabilities give almost-sure risk convergence. No claim follows for uncontrolled parameter growth, adaptive designs depending on labels, dependent pretraining tasks, or an optimizer not proved to achieve the required empirical loss.

## 7. The learned-uniform-KL distinction cannot be removed

For target \(N(m,v)\) and an arbitrary positive predicted variance \(w\), minimizing over \(w\) gives

\[
\inf_{w>0}\operatorname{KL}(N(m,v)\|N(m+e,w))
=\tfrac12\log(1+e^2/v),
\]

with the minimum at \(w=v+e^2\). Thus any nonzero coefficient error on a fixed design makes worst-label KL infinite along an appropriate label ray. Even a sequence of nonzero coefficient errors tending to zero need not have any finite, let alone vanishing, all-label supremum.

The exact comparator has zero error for every label, so the representation statement is valid. The ERM guarantee integrates over genuine Gaussian labels, so it also remains valid. Neither statement upgrades the other to finite-sample or asymptotic uniform-all-label guarantees for the learned model. A reading of the registry that explicitly requires that stronger learned-uniform conclusion is **not settled** by these files.

The earlier finite-piecewise-polynomial obstruction remains valid for the no-division/no-normalization arithmetic architecture. The present construction escapes it through its explicitly used normalization primitive. It does not refute that obstruction or silently alter its assumptions.

## 8. Independent audit of Section 10: fully pre-LN obstruction

I accept the compiler's additional negative theorem under its stated assumptions. Consider fixed finite token count, depth, width, and weights, a fixed affine raw design/label embedding, compact design domain, and updates

\[
h^{\ell+1}=h^\ell+F_\ell(\operatorname{LN}_\epsilon(h^\ell)),
\]

where \(\epsilon>0\) and \(F_\ell\) is continuous on the compact closure of the bounded normalized-input range. LayerNorm has bounded image; fixed finite gains/biases preserve that property. Each residual increment is therefore uniformly bounded over all labels and designs. With finitely many stages,

\[
h^L=h^0+O(1)
\]

uniformly. An affine readout consequently has mean \(b^Ty+O(1)\), where the label slope \(b\) is independent of the design. A final LayerNorm followed by affine readout instead makes the mean bounded outright.

For the rank-one GP \(k(t,u)=tu\), one context input \(x\in[1,2]\), query one, and \(s>0\), the exact mean is

\[
a(x)y,\qquad a(x)=\frac{x}{s+x^2}.
\]

The function \(a\) cannot be constant on an interval: otherwise \(b(s+x^2)-x\) would be the zero polynomial, contradicting its linear coefficient. Choose \(x\) with \(a(x)\ne b\). The mean error grows linearly in \(|y|\), up to a uniformly bounded residual. Its noisy target variance \(s+s/(s+x^2)\) is fixed and positive. The optimized KL lower bound above forces infinite all-label worst-case KL, regardless of the predicted positive variance.

The result covers ordinary finite continuous attention/FFN blocks when every information-bearing residual increment has the displayed normalized-input form. It excludes nonlinear design-label preprocessing, unnormalized cross-token value paths, multiplicative external readouts, and other bypasses. The new constructive architecture has such an explicit unnormalized raw-label path, so there is no contradiction. No obstruction for arbitrary softmax or arbitrary LayerNorm architectures is claimed.

## 9. Supplementary checks and final disposition

The root determinant/normalization checker reports 768 exact finite algebraic checks. I read its scope and did not treat it as a proof of the final full-token wiring. I also read the separate Fraction-based compiler wiring check and independently reran its 12 combinations of labels \(0,-7/3,\pm10^{100}\) and biases \(0,\pm1/2\), without rewriting its output. All passed. The test checks actual attention sums, the cleared scratch inventory, full-width normalization difference, re-gather, final mean/variance, role-scaled clips, and exact preservation of every source token. These finite checks supplement the general derivations above; they do not establish arbitrary-parameter invariance or statistical convergence by themselves.

The reported minor typesetting typo in the clipping formula was fixed in the pinned compiler. The final versions also explicitly count feature recomputation, use existing affine offsets for the non-singleton witness, fix cancellation scaffolding throughout ERM, and prune identically-zero source-normalization contributions before parameter bounds. I have no outstanding required mathematical fix for the accepted theorem.

The result should be described as an internally checked specified-prior theorem with exact representation and prior-average ERM learning. It is not external peer review, formal verification, a novelty verdict, or an official registry solved-status decision. An unqualified closure that asserts a standard fully pre-LN architecture or learned uniform-all-label KL would overstate the accepted result.

As a final integrity check, the frozen T228 manuscript remained unchanged: TeX SHA-256 `38b9479f502a3b0658906642c1ea8fd1e9b05fee0e5434e90944042b827cf0c0`; PDF SHA-256 `85e9fe0de2c2017ec6985b97290da40bd71ede22829a776a770196827246ebb6`.
