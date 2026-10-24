# F0137 literature and fidelity log

Research date: 2026-10-11. All online access is through Python urllib from the shell; raw responses and URLs are retained in this folder and fetch_log.jsonl. A failed API request is not evidence of absence of a paper.

## Verified primary source and intake corrections

Christophe Sabot and Laurent Tournier, *Random walks in Dirichlet environment: an overview*, arXiv:1601.08219v1 (2016), https://arxiv.org/pdf/1601.08219. Downloaded as source.pdf, 35 PDF pages. Text in source.txt.

**The intake is not verbatim.** PDF page 19, immediately after Corollary 2, actually reads (line wrapping removed):

> It is expected that this condition is not optimal, and we conjecture that at least (T)′ is satisfied when dα ≠ 0, hence that renewal times have finite s-moments for s < κ when the RWDE is directionally transient, i.e. when dα ≠ 0.

The glyph is a prime, not gamma. PDF page 18, Definition 5: (T)γ, γ∈(0,1), means directional transience and existence of c>0 such that E0[exp(c sup_{0≤n≤τ1}|Xn|^γ)]<∞. The same definition states: “We say that (T)′ is satisfied if (T)γ is satisfied for all γ < 1.” The regeneration-range definition is the source's precise definition; a slab-exit formulation needs its neighborhood-of-directions quantifiers and any equivalence hypotheses, and is not substituted silently here.

Also, condition (6.1), PDF page 18, is exactly

    sum_{i=1}^d |alpha_i-alpha_{i+d}| > 1.

It is not the half-space-weight condition described in the intake. It appears in Theorem 7, attributed to Enriquez–Sabot and Tournier, and implies Kalikow's condition, hence (T)1, in a direction. Bouchet–Ramírez–Sabot and Fribergh–Kious enter the renewal integrability discussion.

PDF page 18, Theorem 6, reads (mathematical typography transcribed):

> Consider the RWDE with parameters (αi)i=1,...,2d in dimension d ≥ 2. Assume that there exist ℓ such that dα·ℓ > 0. Consider the renewal times (τk)k≥1 in the direction ℓ. Assume that (T)γ is satisfied for some γ∈(0,1). Then E0^(α)[(τ1)^s] < ∞ if and only if s < κ.

Thus a single gamma suffices for the moment consequence; the source's spatial conjecture quantifies over every gamma. Moment assertions here concern s>0. No source theorem in this overview proves the conjecture without an extra hypothesis.

## Search register (2026-10-11)

1. arXiv export API: `all:"Dirichlet environment"`, submittedDate descending, max_results=60. Success; arxiv.xml. Returned relevant 2024 and 2025 papers, plus older sources.
2. OpenAlex works search: `random walk Dirichlet environment ballisticity`, per-page=60. HTTP 429.
3. Crossref works search: `random walk Dirichlet environment ballisticity`, rows=40. Success; crossref.json. No exact resolution identified among those results.
4. Semantic Scholar paper search: same query, limit=50, fields title/year/authors/abstract/url/externalIds. HTTP 429.
5. GitHub repository search: `Dirichlet random walk`, per_page=30. Success; github.json. Repository search is supplementary, not a theorem database.
6. OpenAlex targeted source search: `Random walks in Dirichlet environment an overview`, per-page=5. Follow-up requested; outcome appended below when available. This is to obtain the work identifier and then search citing works.
7. OpenAlex targeted newer-work search: `Dirichlet environment`, per-page=30, filter from_publication_date:2016-01-01. Follow-up requested.
8. Semantic Scholar citation API for ARXIV:1601.08219, limit=100, fields title/year/authors/externalIds. Follow-up requested.
9. arXiv export API: `all:Dirichlet AND (all:ballisticity OR all:Sznitman OR all:regeneration)`, max_results=60, submittedDate descending. Follow-up requested.

## Read-only research brain and ledger

Executed math_recall.py with `Dirichlet environment Sznitman renewal Sabot Tournier`; results chiefly general RWRE and unrelated definitions. Executed brain.py recall with `Dirichlet random walk mistakes` and `Sznitman Dirichlet renewal`. No hint is treated as a verified theorem. The recall utility itself reported a failed automatic refresh spawn; no remember/write command was issued.

Searched the read-only research ledgers for F0137. The F_20260908 intake attempts.jsonl entry F0137-A001 is attempted_unsolved and flags repeated-visit reinforcement. Its claim that repetition “only ever increases” a previous-step probability is too broad: reinforcing one outgoing edge decreases probabilities of other outgoing edges. Its description of a zero-lower-bound slab is also not the usual (T) slab. The F0136 attempt's alleged equivalence of invariant measure and nonzero velocity, and its boundary-fraction explanation, are not used without proof.

## Leads requiring primary-paper inspection

- arXiv:2404.06502v1 (2024), *Limit theorem for subdiffusive random walk in Dirichlet random environment in dimension d ≥ 3*. Abstract explicitly assumes Sznitman's (T) for a stable fluctuation theorem with κ∈(1,2). Does not prove F0137 merely by giving a limit theorem.
- arXiv:2501.06767v1 (2025), *Invariant measure for the process viewed from the particle for 2D random walks in Dirichlet environment*. Abstract explicitly assumes directional transience **and (T′)** for the invariant-measure existence result. Does not establish the missing (T′) hypothesis.
- arXiv:1909.03866 (2019), *Limit Theorem for sub-ballistic random walks in Dirichlet environment in dimension d≥3*. Stable displacement theorem is not a regeneration-range stretched-exponential bound.
- Bouchet–Ramírez–Sabot, *Sharp ellipticity conditions for ballistic behavior of random walks in random environment*, and Fribergh–Kious, *Local trapping for elliptic random walks in random environments*. Pre-source sufficient conditions and moment implications are not resolutions of the post-source conjecture.

Current conclusion: no verified SOLVED_IN_LITERATURE theorem. This is a bounded search, not a proof that none exists.

## Completed follow-up review

The overview's journal reference is independently returned by Crossref: C. Sabot and L. Tournier, *Annales de la Faculté des sciences de Toulouse: Mathématiques* 26(2) (2017), 463–509, DOI **10.5802/afst.1542**. The p.18/p.19 locators above refer to the actual 2016 arXiv PDF fetched here; the journal version uses different pagination and theorem numbering. No incorrect journal-page attribution is made.

**Adrien Perrel and Christophe Sabot**, *Invariant measure for the process viewed from the particle for 2D random walks in Dirichlet environment*, arXiv:2501.06767v1, 12 January 2025; downloaded as 2d.pdf and extracted to 2d.txt. PDF p.2 says:

> If dα ≠ 0, the RWDE is directional transient and it is widely conjectured that in that case Sznitman’s condition (T′) is true (it is known in particular if |α1−α3|+|α2−α4| > 1).

PDF p.8, Theorem 2.3, explicitly starts:

> Under the hypothesis that the random walk in Dirichlet environment P on Z2 satisfies the condition (T′) (and in particular that dα ≠ 0), and that κ > 1, there exists an invariant probability measure Q from the point of view of the particle which is absolutely continuous with respect to P.

The next sentence gives an Lp density for p<κ. This is not F0137: (a) d=2 only; (b) it assumes (T′), the target; (c) κ>1 excludes the sub-ballistic regime; (d) its conclusion is an invariant measure, not an unconditional regeneration-range bound. PDF pp.7–8 explicitly repeat that (T′) for all nonzero Dirichlet drift is expected. Note an apparent `min`/`max` typo in the introductory κ formula on p.2; it is not used for our mathematics.

**Adrien Perrel**, *Limit theorem for subdiffusive random walk in Dirichlet random environment in dimension d≥3*, arXiv:2404.06502v1, 9 April 2024; downloaded as perrel.pdf and perrel.txt. PDF p.7, section 1.3, says “In this paper, we constantly assume condition (T)” and then defines it by exponential control of the range before regeneration. It also states:

> In fact, it is conjectured (but this conjecture is far from being proved) that (T) is equivalent to the directional transience of the walk; in that case, assuming condition (T) would not be a restriction of generality in our paper.

This is positive author evidence of an unresolved stronger bridge as of that version, not a theorem resolving the weaker all-gamma conjecture.

**Élodie Bouchet, Alejandro F. Ramírez and Christophe Sabot**, *Sharp ellipticity conditions for ballistic behavior of random walks in random environment*, *Bernoulli* 22(2) (2016), 969–994, DOI **10.3150/14-BEJ683**, arXiv:1310.6281v3 (5 February 2016). Downloaded brs.pdf / brs.txt. PDF p.8, Theorem 5 states:

> Let β1,β2,...,βd,βd+2,...,β2d be fixed positive numbers. Then, there exists an ε∈(0,1) depending on these numbers such that if β1+d is chosen so that β1+d≤ε, the Random Walk in Dirichlet Environment with parameters (β1,...,β2d) satisfies condition (P)M|e1 for M≥15d+5.

Remark 5, PDF p.6, explains the (P)M/(T′) equivalence under the ellipticity moment condition. The theorem requires one parameter sufficiently small with the others fixed; it is not universal in all positive parameters. PDF p.8 explicitly conjectures (T′) iff max_i|β_i−β_{i+d}|>0. Theorem 1, PDF p.4, assumes (P)M and an ellipticity condition before proving a regeneration-tail exponent. It cannot be used to establish its own spatial hypothesis.

**Alexander Fribergh and Daniel Kious**, *Local trapping for elliptic random walks in random environments in Zd*, arXiv:1404.2060, downloaded fk.pdf / fk.txt. Proposition 4.4, PDF p.24 of the fetched version, constructs a directionally transient zero-speed environment with no prolonged localization on a single edge, using the specially constructed law Q_ex. It is a general elliptic RWRE, not the independent Dirichlet outgoing-vector family. Zero speed also does not contradict (T′) in Dirichlet environments with κ≤1, as the overview explicitly emphasizes. This is not a F0137 counterexample. Its criteria likewise use a separate polynomial spatial condition.

## Follow-up service outcomes and search limits

- OpenAlex source search and newer-work retry both returned HTTP 429.
- Semantic Scholar citations of ARXIV:1601.08219 succeeded: semantic_citations.json contains 30 entries, including the 2025 Perrel–Sabot and 2024 Perrel papers. No continuation offset is present in that response. This is one service's citation coverage, not complete worldwide coverage.
- Additional Semantic Scholar source-metadata request `ARXIV:1601.08219?fields=title,authors,year,externalIds,citationCount`: HTTP 429.
- Crossref exact-title search `Random walks in Dirichlet environment an overview`, rows=3: succeeded and identified the source DOI.
- OpenAlex direct DOI lookup `works/https://doi.org/10.5802/afst.1542`: HTTP 429.
- OpenAlex citing-works attempt `filter=cites:https://doi.org/10.5802/afst.1542`, per-page=100, publication_date descending: HTTP 429. Because the canonical OpenAlex id lookup was blocked, this last request used a DOI-form filter; a successful/valid OpenAlex citation traversal is **not** claimed. The Semantic Scholar citation traversal is the successful alternative.
- arXiv follow-up query succeeded; most additional results were PDEs, dynamic or one-dimensional models, or pre-source papers. No exact post-source resolution found.
- GitHub's four repositories concern Monte Carlo PDE Dirichlet boundary problems, not RWDE ballisticity; they are off-target.
- Downloaded and reviewed 1310.6281 and 1404.2060 as pre-source leads, not post-source resolutions.

Exact request URLs, outcomes, timestamps (date), and raw files are in fetch_log.jsonl. Requests were bounded; blocked searches are identified rather than counted as negative evidence.

## Earlier recorded answers checked read-only

Used `git -C ~/math-open-problems show origin/master:<path>` for:

- `runs/R20/2026-09-18T09-05-00Z_successor_admission_f0137_dirichlet_status_81c4e2.md`: status-only screening, no proof; correctly highlights extra (T)/(T′) assumptions in 2024–2025.
- `research7_2026-09-17/R7-01/admission/2026-09-19T231700Z__F0137_clean_test_ray_and_current_gate.md`: already corrects source prime/condition wording and proposes alpha=(1+δ,1,...,1), 0<δ≤1, as a benchmark. Its A, drift and κ formulas were independently checked and used only as a diagnostic in ATTEMPT.md. It contains no global spatial bound.

The extra math-store query `Kalikow Dirichlet integration parts drift` again predominantly returned Dirichlet-form (not Dirichlet-environment) cards. Stored output is brain_during.txt; no irrelevant card is used as mathematical input. These older records support the bounded status finding but are not independent proofs of global openness.


## Exact bibliographic metadata from the broad arXiv results

These are leads from the query, not source-matching resolutions; non-lattice and different-model items are included to make the search screening auditable.

| Authors | Title | Identifier | Submitted |
|---|---|---|---|
| Adrien Perrel; Christophe Sabot | Invariant measure for the process viewed from the particle for 2D random walks in Dirichlet environment | http://arxiv.org/abs/2501.06767v1 | 2025-01-12 |
| Dongjian Qian; Yang Xiao | Speed of Random Walks in Dirichlet Environment on a Galton-Watson Tree | http://arxiv.org/abs/2405.11845v1 | 2024-05-20 |
| Adrien Perrel | Limit theorem for subdiffusive random walk in Dirichlet random environment in dimension $d \ge 3$ | http://arxiv.org/abs/2404.06502v1 | 2024-04-09 |
| Alejandro F. Ramírez; Santiago Saglietti; Lingyun Shao | A non-oriented first passage percolation model and statistical invariance by time reversal | http://arxiv.org/abs/2310.17123v1 | 2023-10-26 |
| Daniel J. Slonim | On total weight exiting finite, strongly connected sets in shift-invariant weighted directed graphs on $\mathbb{Z}$ | http://arxiv.org/abs/2205.07414v1 | 2022-05-16 |
| Daniel J. Slonim | A zero-one law for random walks in random environments on $\mathbb{Z}^2$ with bounded jumps | http://arxiv.org/abs/2108.11424v3 | 2021-08-25 |
| Rémy Poudevigne | Random walk in random environment and their time-reversed counterpart | http://arxiv.org/abs/1911.02183v1 | 2019-11-06 |
| R. Poudevigne | Limit Theorem for sub-ballistic random walks in Dirichlet environment in dimension $d\geq 3$ | http://arxiv.org/abs/1909.03866v1 | 2019-09-09 |
| Olga Lopusanschi; Tal Orenshtein | Ballistic random walks in random environment as rough paths: convergence and area anomaly | http://arxiv.org/abs/1812.01403v3 | 2018-12-04 |
| Tal Orenshtein; Christophe Sabot | Random walks in random hypergeometric environment | http://arxiv.org/abs/1804.01406v2 | 2018-04-04 |
| Christophe Sabot; Laurent Tournier | Random walks in Dirichlet environment: an overview | http://arxiv.org/abs/1601.08219v1 | 2016-01-29 |


## Second-attempt reference and brain checks (2026-10-11)

Read ATTEMPT.md and the precise repeated-departure gap before starting. Queried the read-only math store with `Dirichlet environment repeated visits Kalikow auxiliary walk integration by parts`. It returned a relevant draft card **claim_bff936a3fb0b94d164fb9181b446f619d45c77bd0be940eb4b91887d98aa8111**, "outgoing rows are tilted by occupation", stating the inverse-escape Green weighting. This is a hint, not a theorem certification. Walked its link using `math_recall.py --id claim_517154c6c40c7215139a013c15350082820b262fac6f25901741740473197ee6`; saved the full result in brain_auxiliary_link.txt. That draft gives a two-type uniformly elliptic row-law example of negative occupation drift with positive fresh-site mean drift, not a Dirichlet family and not a directional-transience claim. The present second attempt independently derives actual Dirichlet examples and explicitly checks their transience parameter.

Fetched **Laurent Tournier**, *Integrability of exit times and ballisticity for random walks in Dirichlet environment*, arXiv:0801.2875, https://arxiv.org/pdf/0801.2875, saved as tournier.pdf/tournier.txt. DOI in the earlier Crossref results: **10.1214/ejp.v14-609**. PDF p.14 defines the auxiliary row as E[G_U(z0,z)omega(z,z+e)]/E[G_U(z0,z)] for finite U and an integrable initial Green function. This is the exact definition used in SECOND_ATTEMPT.md. The two-site domains there are finite, connected, and have finite annealed Green functions because their pair exponent exceeds 1.

Reviewed the saved BRS text around PDF p.8: it expressly distinguishes (T′) from Kalikow's condition and says that parameter characterization of the latter is open. The second attempt is not a new literature-status claim and does not treat failure of Kalikow's sufficient criterion as failure of (T′). No additional broad literature-resolution search was necessary for this focused follow-up; the new targeted source fetch is logged in fetch_log.jsonl.

