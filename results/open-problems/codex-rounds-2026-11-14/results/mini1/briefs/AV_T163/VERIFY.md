# Verification of T163

Checked 14 November 2026. Verdict: NOT-THIS. The two October manuscripts make GFF claims for integer Lipschitz surfaces, not for uniformly random lozenge tilings. The September master source identifies the same Lipschitz model, but its included main theorem has not yet been recovered; the October theorem must not be passed off as a verbatim September quotation.

## Candidate 1: two-arc heights, 6 October 2026

OpenAI, *The Gaussian free field limit of integer Lipschitz heights with two-arc boundary data*, October 6, 2026. Opened the original build/paper.tex and the actual 64-page manuscript PDF at the community mirror. The following is Theorem 1.1, printed page 3; mathematical typesetting is transcribed into LaTeX, with prose retained exactly.

> Let $D$ be a bounded smooth simply connected planar domain with two distinct marked boundary points. Let $D_\delta$ be simply connected triangular-lattice polygonal approximations with uniformly converging marked boundary parametrizations and edge-midpoint marks, and let $h_\delta$ have the uniform odd-height law (1.1). There is a constant $\sigma>0$, depending only on the unit triangular-lattice model, such that
> $$h_\delta\Longrightarrow\bar g+\sigma\Phi_D\qquad\text{in }\mathcal D'(D).$$
> For every $f\in C_c^\infty(D)$, $\mathbb E h_\delta(f)\to\int_D\bar g f$. Consequently
> $$\frac{h_\delta-\mathbb E h_\delta}{\sigma}\Longrightarrow\Phi_D\qquad\text{in }\mathcal D'(D).\tag{1.3}$$
> All finite vectors of test-function integrals converge jointly to the corresponding Gaussian vectors, and all their mixed moments converge. The constant is specified by the absolutely convergent finite-volume series in Proposition 6.1; in the spectral convention below, $\sigma=4\pi\sqrt{c_*}$.

The law (1.1), printed page 2, is uniform over odd integer functions on triangular-lattice vertices, equal to $+1$ and $-1$ on the two boundary arcs and satisfying $|h_\delta(x)-h_\delta(y)|\in\{0,2\}$ on every edge. The field is interpolated affinely on triangles and tested by Euclidean area integrals. The covariance in (1.2) is $G_D=(-\Delta_D)^{-1}$; $\bar g$ is the bounded harmonic extension of the two-arc data. The paper itself says this addresses the field part of Schramm's Problem 2.2 (p. 3), and distinguishes its interface question.

Sources: [original master source](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/build/paper.tex), [manuscript PDF actually read](https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/paper.pdf), [original PDF location](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/paper.pdf).

## Candidate 2: two-arc heights, 25 September 2026

OpenAI, *The Gaussian free field limit of integer Lipschitz heights with two-arc boundary data*, September 25, 2026. The original [README](https://raw.githubusercontent.com/openai/math/main/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-September-25-2026/README.md) and build/paper.tex were opened: it gives this author, title and date, and an abstract specifying uniform odd integer heights with neighboring differences zero or two and two boundary arcs with values $+1,-1$. It includes its introduction through `sections/01-introduction`.

**Candidate-level access result: UNREADABLE for the exact main theorem; model identified from the primary abstract.** The PDF wrapper opened, but the raw PDF was rejected by the web reader as `application/octet-stream`. The included introduction source, alternative raw URLs and September mirror could not be fetched. No claim is made that the September and October theorem statements are word-for-word identical. The readable primary abstract is enough to identify a different model from lozenge tilings, but not enough to certify all September theorem hypotheses.

Sources: [September master source actually read](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-September-25-2026/build/paper.tex), [PDF wrapper opened](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-September-25-2026/paper.pdf). See LOG.md for failed direct-source/PDF attempts.

## Candidate 3: weighted heights, 6 October 2026

OpenAI, *Gaussian free-field limits of weighted integer Lipschitz heights*, October 6, 2026. Opened the actual 85-page manuscript PDF at the community mirror and the original README. The following is Theorem 1.2, printed page 3; prose is retained exactly and mathematical typesetting is transcribed into LaTeX.

> For every fixed $x\in[1/\sqrt2,1]$ there exists $\sigma(x)\in(0,\infty)$, independent of $D$ and of the inside approximation in Definition 1.1, such that
> $$\frac{h_\delta}{\sigma(x)}\Longrightarrow\Phi_D\qquad\text{in }\mathcal D'(D).$$
> In particular, the fields are tight as random distributions and, for every $k\ge1$ and $f_1,\ldots,f_k\in C_c^\infty(D)$, the vector $(h_\delta(f_i)/\sigma(x))_{i=1}^k$ converges to $(\Phi_D(f_i))_{i=1}^k$. All mixed moments of these vectors converge.

Definition 1.1 (pp. 2–3) requires a bounded simply connected domain with $C^2$ Jordan boundary and inside approximations bounded by simple hexagonal-lattice cycles: $D_\delta\subset D$, eventual containment of every compact subset, and uniform convergence of homeomorphic boundary parametrizations. Heights live on enclosed hexagonal faces (identified with triangular-lattice centers), are zero on the boundary face layer and satisfy $|h(u)-h(v)|\le1$. Their law is $\mathbb P_{\delta,x}(h)=x^{N_\delta(h)}/Z_{\delta,x}$, counting unequal adjacent face heights. Thus $x=1$ is the uniform Lipschitz model. Reflection makes its expectation zero. Equation (1.3) expressly uses the Euclidean Laplacian, with Green singularity $(2\pi)^{-1}\log(1/|z-w|)$.

The paragraph after the theorem explicitly leaves $\sigma(x)$ implicit and does not assert that it is independent of $x$. The exact loop representation is loop $O(2)$, with weight $2^{\#\mathrm{loops}}x^{\#\mathrm{occupied\ edges}}$ (p. 3). This is not the honeycomb perfect-matching measure of lozenge tilings.

Sources: [manuscript PDF actually read](https://mathcommunity.github.io/oai-math-revised/papers/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/paper.pdf), [original PDF location](https://github.com/openai/math/blob/main/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/paper.pdf), [original version note](https://github.com/openai/math/blob/main/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/README.md).

The manuscript quotations are attributed to OpenAI and reproduced from the repository's [Apache-2.0 licensed material](https://github.com/openai/math/blob/main/LICENSE).

## Comparison with our statement, clause by clause

| Clause in T163 | Two-arc October theorem | Weighted October theorem | Consequence |
|---|---|---|---|
| Uniform lozenge tilings of tileable triangular-lattice domains | Uniform odd integer Lipschitz functions, edge increments $0,\pm2$ | Integer Lipschitz functions, increments $0,\pm1$, weight $x$ per changed edge | Different probability spaces and local constraints. Uniform at $x=1$ does not mean uniform lozenge tilings. |
| Planar dimension | Planar | Planar | Same dimension alone supplies no implication. |
| Bounded simply connected $D$, arbitrary admissible boundary height profile | Smooth $D$ with two marked boundary points and fixed $\pm1$ data | $C^2$ Jordan $D$ and zero boundary layer | Neither covers arbitrary $h$. Fixed microscopic boundary values also rescale to zero, rather than arbitrary macroscopic slope data. |
| General tileable approximating sequences and convergent rescaled boundary heights | Uniform convergence of marked boundary parametrizations, edge-midpoint marks | Inside simple-cycle approximations with the full conditions of Definition 1.1 | Restricted geometric approximation assumptions, in another model. |
| Limit shape and its liquid region $L$ | Field on all of $D$ | Field on all of $D$ | No theorem on the liquid region of a lozenge limit shape, frozen facets, disconnected liquid regions or forced sets. |
| Centered height fluctuations | Centered field converges after division by $\sigma$; uncentered limit includes harmonic mean | Already mean zero, divided by $\sigma(x)$ | Same kind of observable, for different random surfaces. |
| $\pi^{-1/2}$ times GFF | Model constant $\sigma=4\pi\sqrt{c_*}$ | Unspecified $\sigma(x)>0$ | Neither identifies the lozenge normalization. |
| Kenyon–Okounkov complex structure, map $\phi:L\to\mathbb C_+$ | Ordinary Dirichlet Green kernel on $D$ | Explicit Euclidean Green kernel on $D$ | Neither constructs or identifies the shape-dependent complex structure in T163. |
| Full GFF scaling limit | Distributional convergence, joint test integrals and all their mixed moments | Same strength | These are full field-limit claims, not merely logarithmic variance bounds, but do not transfer to lozenges. |

For September the readable primary abstract confirms the model/boundary mismatch; exact theorem-level geometric and convergence claims remain unverified. No part of the general lozenge theorem is established by the candidate claims merely because both use triangular lattices and Gaussian free fields. In particular, a Lipschitz contour configuration has degree zero or two at interior honeycomb vertices, whereas a perfect matching has degree one; no measure-preserving identification with lozenge tilings is supplied.

The GFF is a random distribution, not a field with ordinary pointwise values: the requested convergence should itself be understood after testing/averaging, or with an explicitly specified distinct-point moment interpretation. This does not repair the model mismatch.

## Follow-ups and verification records opened

- [Repository README](https://github.com/openai/math): says manuscripts are raw research data, that some unformalized results could have issues, and that revisions preserve earlier versions. This is a claim-status notice, not independent validation.
- [Repository history](https://github.com/openai/math/blob/main/history.md), including the October 7 update, and both October original README version notes. The weighted revision supplies an annulus circuit proof; the two-arc revision derives conditional cut and loop estimates from the weighted annulus circuit theorem at $x=1$. These are author revisions, not referee acceptance.
- [Lean README](https://github.com/openai/math/blob/main/lean/README.md) and [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml) opened. Searching the catalogue for the candidate title fragments found no corresponding formalisation. The lean/ directory listing itself returned cache miss. No Lean proof was run.
- [math20 family 232](https://math20.org/f/232/) opened: lists these as Schramm Lipschitz-model results and lists no Lean formalization. Its proposed exposition is still in preparation.
- [Plectis Atlas family 232](https://wcook04.github.io/plectis-atlas/families/232.html) opened: lists no Lean statement, no corresponding Comparator run or outside-group comparison, and reproduces the October two-arc theorem. This is a catalogue, not an expert endorsement.
- Community pages for [two-arc October](https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/) and [weighted October](https://mathcommunity.github.io/oai-math-revised/papers/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/) opened. Both say there are no contributor notes yet; their automatically collected prior-literature suggestions are explicitly unreviewed. Existing-issues links could not be fetched. Their mirrored PDFs, rather than abstracts alone, supplied the October theorem quotations above.
- Exact-title web searches combined with `arxiv`, `error`, `refutation` and `review`, plus `site:arxiv.org` searches, found no later arXiv version, identifiable refutation, referee report or named expert verification of these candidate claims. Search results included further reading-guide pages (DiscoverIA and slatinwine); attempts to open them failed, so they are not cited as evidence.

This is a bounded search as of 14 November 2026; absence of a located comment does not prove none exists. The earlier lozenge-tiling references supplied in the task have not been independently re-audited here and are not being newly certified.

## Recommended new “where it stands” sentence

The general lozenge-tiling statement remains open on the evidence checked here, with the previously recorded special cases unchanged. OpenAI's *The Gaussian free field limit of integer Lipschitz heights with two-arc boundary data* (25 September and 6 October 2026) and *Gaussian free-field limits of weighted integer Lipschitz heights* (6 October 2026) concern different random-surface models and do not claim the Kenyon–Okounkov statement for general lozenge domains. No independent verification or Lean formalisation of these Lipschitz claims was found.

## Spot check

Selected the central spectral-classification lemma, **Lemma 5.8** of OpenAI's October 6 two-arc manuscript (printed pp. 28–29). It asserts that every vague subsequential limit of the rescaled plane spectral measures is $M(dp)=c\,dp/|p|^2$, with $0\le c<\infty$. This is a load-bearing step: it identifies the shape of the GFF covariance; the subsequent Proposition 5.9 must still make the coefficient unique and Theorem 5.10 must make it positive.

Read its full proof and the stated inputs (5.5), (5.8), (5.9), Lemma 5.7, and the angular identity preceding them in the [October PDF](https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/paper.pdf). The following check is conditional on those earlier inputs, not a verification of the whole preprint.

1. On any rescaled band $a\le|k|/\delta\le b$, (5.9) bounds the mixing mass. The nonnegative integrable defect $D(k,s)=((|k|-s)/(|k|+s))^2$ has integral tending to zero on the shrinking original band, by (5.8). Away from $s/\delta=|k|/\delta$, it has a positive lower bound, including at zero and infinity. Thus limiting mixing measures concentrate on that graph. This deduction is valid if the quoted band bounds and defect integrability hold.
2. The Cauchy kernel on that graph gives $M(dk,dl)=|k|\eta(dk)dl/[\pi(k^2+l^2)]$ on $k\ne0$. Multiplying by $|p|^2$ gives $|k|\eta(dk)dl/\pi$, whose distributional derivative in the vertical direction vanishes. This does not require assuming that $\eta$ has a density.
3. At any nonzero point, at least two of the three rotated tangential coordinates are nonzero. Their normal directions are independent. The two vanishing directional derivatives therefore imply a locally constant distribution. Local smoothing gives the same conclusion directly, and connectedness of the punctured plane makes the constant global. Thus the last identification in the lemma does not mistakenly infer continuous rotation invariance from sixfold symmetry alone.
4. The alias argument concerns shrinking neighborhoods of nonzero reciprocal preimages, with the preimages themselves excluded on the horizontal band. A finite measure gives these punctured neighborhoods vanishing mass even if it has an atom at the center. This part is sound under the paper's local finiteness premise. Lemma 5.7 also excludes mass on the axes; its stated $O(\varepsilon/r)$ bound is the ingredient needed there.

As a check on the algebra feeding this argument, with $a=|k|>0$, the analytic function $((a+iz)/(a-iz))^2$ is bounded in the upper half-plane and its boundary real part is $1-8a^2l^2/(a^2+l^2)^2$. Its value at $z=is$ is $((a-s)/(a+s))^2$, confirming the sign and square in Lemma 5.5. Independently, $\int_{\mathbb R}8a^2l^2/(a^2+l^2)^2\,dl=4\pi a$ (substitute $l=a\tan t$); the six rotated fourth harmonics sum to zero by a finite geometric series. These are consistency checks of the displayed calculation, not evidence for the upstream reflection representation.

No error was identified in this conditional spectral-classification argument. The existence and properties of the plane measure, positive normal transfer, annulus estimate, boundary comparisons and Gaussian moment identification remain unaudited. The spot check supplies no conclusion about correctness of either main theorem and does not affect the model-mismatch verdict.
