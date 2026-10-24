from pathlib import Path
import json,urllib.parse
P=Path('.')
source='''# F0087 literature and status search — 2026-10-11

## Verdict
No exact solution in print was verified. This is a bounded, incomplete search, not a proof that the question remains open. OpenAlex repeatedly returned HTTP 429. Semantic Scholar citation results and two arXiv API searches were obtained; several further targeted searches were rate-limited. The strongest verified result is a **partial** answer, explicitly described as such by its author.

## Source, exact statement and normalization
Richard Kenyon, *Lectures on dimers*, IAS/Park City Mathematics Series **16** (2009), 191–230; DOI 10.1090/pcms/016/04; arXiv:0910.3129. Downloaded https://arxiv.org/pdf/0910.3129 to `kenyon_pdf.pdf`. The open problem is on PDF p.54, Section 12, item 1:

> 1. Height mod k. What can be said about the random variable e^{iαh} where α is a constant and h is the height function? This is an analog of the spin-spin correlations in the Ising model and is a more delicate quantity to measure that the height function itself. Standard Toeplitz techniques allow one to evaluate it in lattice directions, and it is conjectured to be rotationally invariant (for the uniform square grid dimers, say). See [24] for some partial results. Can one describe the scaling limit of this field?

The PDF really says “measure that”; the intake changed this to “measure than”. Square-grid uniform dimers are an example in the actual statement, not a separately imposed list of hypotheses. No range for α, domain, Gibbs slope, height pinning, renormalization, or topology is specified. Section 2.2, PDF p.16, defines the domino reference flow as 1/4, and says this height is 1/4 of the integer height in Figure 8. Thus charge conventions must be checked rather than inferred from an integer-height formula.

Reference [24]: Haru Pinson, *Rotational Invariance and Discrete Analyticity in the 2d Dimer Model*, Communications in Mathematical Physics **245** (2004), 355–382, DOI 10.1007/s00220-003-1021-3. Bibliography and DOI verified; full theorem not fetched. This is the pre-source partial result, not a later solution.

## Principal later paper: verified theorem text
Julien Dubédat, *Dimers and families of Cauchy-Riemann operators I*, Journal of the American Mathematical Society **28** (2015), 1063–1167, DOI 10.1090/jams/824, arXiv:1110.2808 (initial title *Dimers and analytic torsion I*). Downloaded current PDF (title-page date October 30, 2018), 95 pages, and source TeX. PDF: `dubedat.pdf`; extracted text: `dubedat.txt`; source: `dubedat_dimertors_arx.tex`.

The introduction, PDF p.3, says verbatim:

> The study of these families will lead to precise asymptotics for “electric” correlators of the dimer height field (Theorem 24), partially answering the Open problem 1 [39]; and for monomer correlators (Theorem 28), in fulfilment of the Fisher-Stephenson conjecture ([24], see also [11]).

Proposition 23, PDF p.75, verbatim (math transcribed from the source TeX):

> If s∈(0,1/2), there is a constant c(Λ,s) such that
> |⟨χ^{h(y)−h(x)}⟩| = exp(2c(Λ,s)) |x−y|^{−2s²}(1+o(1))
> as |x−y|→∞.

Here χ=e^{2iπs}; this is an absolute-value statement. It cannot alone identify the complex phase or a field law.

Theorem 24, PDF p.77, verbatim (math transcribed from TeX lines 3119–3120):

> For weights s₁,…,s₂ₙ∈(−1/2,1/2), s₁+s₂=⋯=s₂ₙ₋₁+s₂ₙ=0, and singularities {z₁,…,z₂ₙ} with pairwise distances of order R, we have as R goes to infinity:
> ⟨exp(2iπ ∑_{j=1}^{2n} s_j h(z_j))⟩ ∼ exp(∑_{j=1}^{2n} c(Λ,|s_j|)) ∏_{1≤i<j≤2n}|z_i−z_j|^{2s_i s_j}.

The theorem is printed without absolute-value bars; the preceding proposition and parts of its proof use absolute values. The arguments here use Proposition 23 for unconditional bounds. The conditional limit reduction uses Theorem 24 exactly as printed; it does not independently reprove that analytic theorem.

Application and limitations, one hypothesis at a time:
1. The uniform square grid is a critical isoradial example of the paper's dimer setting (critical weights all equal, up to an irrelevant constant). The angle bound (♠) is satisfied.
2. Its canonical height has increments reference-flow minus occupancy (Section 3.2, p.22); on the square grid the reference is 1/4. This matches Kenyon's normalization up to sign, which conjugates electric observables.
3. Setting s=α/(2π) gives the principal-charge range |α|<π. The endpoint s=±1/2 is expressly excluded (p.58); the overview says the restriction is sharp, at least for one pair (p.14).
4. Taking n=1 gives isotropic large-distance two-point asymptotics within that range. This verifies much more than lattice-direction asymptotics.
5. Taking charges ±s gives separated balanced multipoint correlations. This does not give estimates uniform as macroscopic points coalesce.
6. A law of a renormalized random distribution requires such collision control and a convergence argument. The theorem states neither this law nor all α. Pairing restrictions also leave general neutral charges untreated; p.75 discusses this restriction explicitly.
Therefore this paper is a lead and a theorem usable for special cases, **not SOLVED_IN_LITERATURE under the user's criterion**.

## Imaginary-chaos lead, inspected
Janne Junnila, Eero Saksman, Christian Webb, *Imaginary multiplicative chaos: Moments, regularity and connections to the Ising model*, Annals of Applied Probability **30**(5) (2020), 2099–2164; DOI 10.1214/19-AAP1553; arXiv:1806.02118. Downloaded PDF to `jsw_pdf.pdf`, extracted `jsw.txt`. Theorem 1.1 constructs the Wick exponential of a log-correlated **Gaussian** field for 0<β<√d. Its standard approximations are Gaussian; a discrete dimer height is not one of them. The XOR-Ising applications and exact bosonization involve different lattice observables/models, and are not a theorem about exp(iαh) of uniform square-grid dimers. This paper supports construction and moment determinacy of a candidate, not dimer convergence.

Other retrieved leads, not claimed as solutions:
- Dubédat, *Exact bosonization of the Ising model*, arXiv:1112.4399 (2011), found among citations; not fetched.
- Neil Wilkins and Stephen Powell, *Derivation of field theory for the classical dimer model using bosonization*, arXiv:2301.09665 (2023), abstract obtained in arXiv API. The abstract describes a constructive field-theory derivation and perturbative interactions; no exact scaling-limit theorem was verified. Authors require independent metadata verification before citation in a paper.
- Haru Pinson, *Rotational Invariance of the 2d Spin – Spin Correlation Function*, Communications in Mathematical Physics **314** (2012), 807–816, DOI 10.1007/s00220-012-1545-5. Metadata only. Not assumed to concern this dimer field.
- Citation lists also returned height GFF, t-embedding, interacting-dimer and Riemann-surface work. Their titles alone do not resolve this question.

## Read-only brain and prior-work searches
On 2026-10-11 ran math_recall.py queries “dimer electric correlators Dubedat imaginary multiplicative chaos” and “Junnila Saksman Webb imaginary multiplicative chaos”; both returned mainly generic chaos cards and no relevant verified dimer theorem. Ran brain.py recall “dimer height electric field” and “dimer height mistakes”; neither returned a useful topic-specific result. No brain writes were issued.

Ran rg for F0087 across the research ledgers and separately the codex_pool_2026_10_10 directory. The F intake, problems.jsonl row 87 and attempts.jsonl row 71, supplied the Dubédat lead but explicitly had not checked its theorem. The pool had no match. The published-answer repository was inspected read-only with git ls-tree origin/master, filtered for F0087/dimer/electric; no relevant F0087 path was found. No git working tree was changed. These are searches, not mathematical evidence.

## Complete network search/fetch log
Every shell/Python HTTP request used for this search is listed below, with its original query and outcome. Raw responses and `SEARCH_LOG.jsonl` are retained. The log includes unsuccessful requests.

Important correction: `openalex_citing` used an **unverified placeholder identifier** W2120491439. It failed with HTTP 429 and is not a valid search of papers citing Kenyon. The later DOI-resolution and DOI-based citing requests also failed; OpenAlex citation coverage was not obtained. Semantic Scholar did return two pages (200 records) of citations of ARXIV:0910.3129, plus 24 citations of the old ARXIV:1110.2808 record. The latter record appears incomplete (no newer papers after 2017). Kenyon's citation list still had a next page; coverage is bounded and incomplete.

The DOI-based OpenAlex cites filter was an attempted external-ID query; its validity was not confirmed because the server returned 429. No result from either failed citation query was used.

'''
rows=[]
for line in (P/'SEARCH_LOG.jsonl').read_text(encoding='utf8').splitlines():
 r=json.loads(line);rows.append(f"- {r['date']} — **{r['service']}**: `{r['url']}` — {r['result']}\n")
(P/'LITERATURE.md').write_text(source+''.join(rows),encoding='utf8')
