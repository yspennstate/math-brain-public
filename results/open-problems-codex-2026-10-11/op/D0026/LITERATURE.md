# D0026 literature verification

Research date: 2026-10-11 (session date). Searches use Python urllib only.

## Source confirmed

Fabio Martinelli, Assaf Shapira, Cristina Toninelli,
*Long time behaviour of one facilitated kinetically constrained models:
results and open problems*, arXiv:2510.20461v1 [math.PR], 23 October 2025.
URL: https://arxiv.org/pdf/2510.20461 . Saved as source.pdf and source.txt.

Conjecture 1, Section 1.1, PDF page 2, verbatim (mathematical typography
normalized):

> For any q ∈ (0, 1) and any function f depending on the state of finitely
> many vertices lim_{t→∞} |E_ν(f(η(t))) − π(f)| = 0, (1.1)
> provided that ν(∃ an infected vertex) = 1.

Page 3 specifies spins: infected=0 and pi is Bernoulli(p), p=1-q,
on the spin variables. Page 4 gives the precise FA-1f constraint (1.7).
Page 2 states that tools to prove Conjectures 1 and 2 are unavailable
for arbitrary q, and notes results only above thresholds. This is a
statement about the source date, not a proof of current open status.

Corollary 2.9, PDF page 7, verbatim:

> Let µ be a stationary measure for the one-dimensional FA-1f. Then µ =
> λπ + (1−λ)δ_1 for some λ ∈ [0, 1]. The same holds for the BABP and for
> the δ-West process, δ ∈ (0, 1].

This classifies stationary measures; it does not establish convergence.

## Searches and local history

All external queries and full URLs are in search_literature.py; raw
responses and request errors are recorded in search_log.json. The service
list is arXiv, OpenAlex (including attempted citing-work lookup), Crossref,
Semantic Scholar (including citing-work lookup), and GitHub.
Results are pending interpretation; no SOLVED_IN_LITERATURE verdict.

Read-only brain searches: math_recall.py "Fredrickson Andersen facilitated
convergence equilibrium"; brain.py recall "FA-1f kinetically constrained
convergence equilibrium mistakes". Returned cards are mostly unrelated;
none supplies a verified FA-1f theorem.

Local intake search for D0026 found D0026-A001, dated 2026-09-08, in
probability_1000_intake_D_20260908/attempts.jsonl. Its unproved assertions
are audited in ATTEMPT.md. The neighboring D0027-A001 is not a proof of a
valid infinite-volume reduction: boundary influence must be controlled.

## Relevant literature and scope

* Oriane Blondel, Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto,
  Cristina Toninelli, *Fredrickson-Andersen one spin facilitated model out
  of equilibrium*, Markov Processes and Related Fields 19(3), 383–406
  (2013); arXiv:1205.4584. Source reference [3]. The 2018 front paper,
  PDF page 2, describes its infection-spacing and q>1/2 hypotheses,
  which are stronger than Conjecture 1's hypotheses.
* Oriane Blondel, Aurelia Deshayes, Cristina Toninelli, *Front evolution of
  the Fredrickson-Andersen one spin facilitated model*, arXiv:1803.08761v2,
  29 October 2018. Fetched as front_pdf.pdf and front_pdf.txt. Theorems 2.1
  and 2.2, PDF page 5, require q above a contact-process threshold and
  concern the process seen from the front and front LLN/CLT. PDF page 4
  explicitly states that FA-1f's extinction time is always infinite
  because a single zero cannot disappear. This confirms the correction
  to the intake attempt, but does not prove the all-q conjecture.
* Anatole Ertul, *Cutoff for the Fredrickson-Andersen one spin facilitated
  model*, ALEA 19(1), 511–536 (2022); arXiv:2103.00019v2. Source reference
  [8]: finite-volume cutoff for q not too small, not Conjecture 1.
* Ivailo Hartarsky, Fabio Lucio Toninelli, *Kinetically constrained models
  out of equilibrium*, Probability and Mathematical Physics 5(2), 461–489
  (2024); arXiv:2212.08437v2. Source reference [10]: high-q convergence
  for more general KCMs; not the all-q conclusion.
* Laure Marêche, *Exponential convergence to equilibrium in supercritical
  kinetically constrained models at high temperature*, Markov Processes
  and Related Fields 26(5), 861–884 (2020). Source reference [17]; high
  temperature is a substantive restriction.
* Ivailo Hartarsky, Cristina Toninelli, *Kinetically Constrained Models*,
  SpringerBriefs in Mathematical Physics 53, Springer Cham (2025);
  arXiv:2412.13634. Source reference [9], especially Chapter 7 for
  nonstationary questions. Background, not a verified later solution.

### Papers submitted after the source

* Vanja Marić, Juan P. Garrahan, Lenart Zadnik, *Hierarchy of time scales
  in kinetically constrained models via stochastic-generator expansion*,
  arXiv:2609.18882v1, submitted 16 September 2026. Fetched and inspected
  as recent_hierarchy.pdf / .txt. It studies perturbative low-temperature
  time scales for quenches in East and FA models, not convergence from
  every nonempty initial law for all q.
* Ruifeng Liu, Jianwen Zhou, Yejia Chen, Jiahang Chen, Hai-Jun Zhou,
  *Thermodynamic phase transitions in lattice spin systems with severe
  kinetic constraints: Numerical simulation results*, arXiv:2607.06205v1,
  submitted 7 July 2026. Fetched and inspected as recent_thermodynamic.pdf
  / .txt. Its K=1 rule requires ALL neighbors empty, and it studies
  square/cubic lattices and numerical phase transitions. Its constraint
  and dimension differ from one-dimensional FA-1f.
* Paul Chleboun, *Linear time mixing and pre-cutoff for oriented kinetically
  constrained models*, arXiv:2609.30585v1, submitted 24 September 2026.
  Abstract inspected in arxiv_mathpr_recent.response. Its scope is oriented
  constraints on finite boxes with uniformly positive gaps; FA-1f is
  unoriented. A methodological lead, not a solution to Conjecture 1.
* Assaf Shapira, *Universality in dimension 1 of kinetically constrained
  lattice gases*, arXiv:2608.13208v1, submitted 13 August 2026. Abstract
  inspected in arxiv_mathpr_recent.response. It classifies conservative
  lattice gases, not the nonconservative FA-1f spin system.

GitHub's Fredrickson-Andersen search returned FTurci/fredrickson-andersen
(Python simulation) and AustenLamacraft/FA-front (Julia simulation).
Neither result supplies a theorem deciding the conjecture. The bare
FA-1f query chiefly returned unrelated profile repositories.

## Search limitations and conclusion

OpenAlex search and source-ID discovery repeatedly returned HTTP 429.
An OpenAlex source work ID was not obtained, so its citing-work list
could not be retrieved. Semantic Scholar's search, source lookup and
direct ARXIV:2510.20461 citation endpoint also returned HTTP 429. These
failures are not counted as negative results. Crossref title searches did
not return the source among the bounded results. The arXiv title search
confirms v1 for the source. The broad math.PR query returned 100 of 101
records, chiefly unrelated kinetic-PDE papers; a narrower exact-phrase
follow-up was issued to address this limit.

No paper proving the exact conjecture has been verified. The status is
**not SOLVED_IN_LITERATURE**. The bounded search supports only 'no verified
resolution found', with the stated unavailable citation-search channels.

Additional read-only history: `git show origin/master:` was used for
operations/claims/D0027.md and the R7-04 D0027 handoff
research7_2026-09-17/R7-04/handoffs/2026-09-17T194200Z__D0027_sixrun_handoff.md.
That handoff reports PARTIAL and contains the neighbor-refresh duality.
Its algebra was independently verified in ATTEMPT.md, Proposition 6.
No instructions or unverified mathematical conclusions from it were adopted.

Source Section 6, Theorem 6.2, PDF page 25, gives almost-sure linear
growth bounds for the infection range Y(t) and diameter D(t) from a
finite nonempty infection set for any q>0. This is already an all-q
growth result, so it would be wrong to describe all-q survival or all-q
diameter growth as wholly unknown. It does not ensure that every fixed
site locally equilibrates or exclude escape of infection from that site.

The final exact-phrase arXiv query returned all 6 matching entries,
including the source. Besides Chleboun and Shapira's papers above, it
returned Balázs Pozsgay's *Anomalous current fluctuations in the stochastic
XNOR hopping model* (arXiv:2608.10536v2), Laurent Bartholdi, Ivailo
Hartarsky and Ivan Mitrofanov's *Super-Arrhenius relaxation of the triangular
plaquette model in any dimension* (arXiv:2606.16259v1), and Assaf
Shapira's *A Thomson-type variational principle for diffusion coefficients*
(arXiv:2606.04636v2). Their inspected abstracts concern a conservative
hopping model, a plaquette model, and conservative-system diffusion,
respectively; none states the target FA-1f convergence theorem.

The further brain query during the attempt was math_recall.py
"spectral theorem reversible Markov semigroup convergence invariant measures".
It returned generic semigroup/Poincare/hypercontractivity material, not a
verified answer to this conjecture. The proof here checks its own
stationary-kernel and L1 arguments directly.

## Additional attempt: direct gap recall and neighboring theorem (2026-10-11)

Brain questions, read only:

1. math_recall.py "neighbor refresh dual finite infection local occupation
   convergence biased annihilating branching Neuhauser Sudbury". No verified
   FA-1f resolution was returned. A generic weighted-tail criterion was
   relevant as a caution, not a solution.
2. math_recall.py "sigma finite reversible measure spectral gap heat kernel
   finite particle sector Nash inequality". Returned generic Poincare,
   Nash and heat-kernel material, not the needed model-specific gap theorem.
3. Walked card claim_186d6a667014e34cb8b64365830391915950601674d6bb2f0bfcbb56d28276ff
   (Weighted tail criterion for convergence of occupation sums). Its
   insistence on a genuine weighted-tail bound was checked against the
   infinite mass of the occupation test in FRESH_ATTEMPT.md.

Additional shell/Python web fetches (all 2026-10-11):

* https://arxiv.org/pdf/2412.13634 -> kcm_book.pdf / kcm_book.txt, 125 PDF
  pages, 1,878,067 bytes. Reference: Ivailo Hartarsky and Cristina
  Toninelli, *Kinetically Constrained Models*, SpringerBriefs in Mathematical
  Physics 53 (2025), arXiv:2412.13634. Independently inspected Theorem 4.8,
  printed page 39 / PDF page 49, and the definition immediately preceding it.
  The theorem says (verbatim with normalized mathematical typography):

  > Theorem 4.8 (General KCM upper bound) There exists C > 0 depending only
  > on R such that for every q ∈ (0, 1),
  > T_rel ≤ (2/q)^{C log min(|Λ|, 2/q)}.

  Its setup explicitly restricts to an arbitrary irreducible component C
  with stationary law mu=pi(.|C). This supplies the nonempty finite-interval
  gap used in the fresh proof. The interval-to-cycle comparison and every
  hypothesis match are written in FRESH_ATTEMPT.md. It does NOT itself
  prove the conjecture; finite-volume relaxation and fixed-site long-time
  convergence from singular starts are different statements.
* https://arxiv.org/pdf/2103.00019 -> cutoff.pdf / cutoff.txt, 648,070 bytes.
  Anatole Ertul, *Cutoff for the Fredrickson-Andersen one spin facilitated
  model*, arXiv:2103.00019v2, 20 November 2021. Its finite interval has
  infected exterior and its relaxation theorem requires q above a threshold.
  It was checked for boundary/model distinctions; not used to infer the
  all-q nonempty-cycle gap or solve the conjecture.
* https://arxiv.org/pdf/2005.13327 -> spectral_note.pdf / spectral_note.txt,
  197,291 bytes, 17 PDF pages. Assaf Shapira, *A note on the Fredrickson-
  Andersen one spin facilitated model in stationarity*, arXiv:2005.13327v2,
  18 June 2020. Published as *A note on the spectral gap of the Fredrickson-
  Andersen one spin facilitated model*, J. Stat. Phys. 181(6), 2346–2352
  (2020). Theorem 1.3 concerns an UPPER bound for finite graphs with
  |V|=c/q, under product law conditioned on at least one vacancy. It is
  not a uniform lower-gap bound and is not used as such.

Source page 27's explicit assertion about uniformly positive nonempty-
cycle gaps is consistent with the independent book theorem. Source page
26's shorter discussion of healthy-boundary chains should not be read as
a positive gap for the unconditioned chain containing the empty absorbing
class. The fresh proof bypasses that ambiguity.

The book attributes Theorem 4.8 to Ivailo Hartarsky, *Bisection for
kinetically constrained models revisited*, Electronic Communications in
Probability 26 (2021), Paper No. 60, 10 pages (book reference [110]).
The input used here is the independently inspected book statement and
setup; the original 2021 paper was not separately fetched. None of these
references is being labeled a solution in print to Conjecture 1.


## Full request journal
* 2026-10-11T22:03:32.512966: **arxiv**; query `all:"FA-1f"`. URL: https://export.arxiv.org/api/query?search_query=all%3A%22FA-1f%22&sortBy=submittedDate&sortOrder=descending&max_results=40. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:03:33.626956: **arxiv_title**; query `Long time behaviour of one facilitated`. URL: https://export.arxiv.org/api/query?search_query=ti%3A%22Long%20time%20behaviour%22%20AND%20all%3A%22facilitated%22&max_results=10. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:03:34.509667: **openalex**; query `FA-1f convergence equilibrium`. URL: https://api.openalex.org/works?search=FA-1f%20convergence%20equilibrium&per-page=40. Outcome: <HTTPError 429: 'Too Many Requests'>.
* 2026-10-11T22:03:34.927262: **openalex_source**; query `Long time behaviour of one facilitated kinetically constrained models`. URL: https://api.openalex.org/works?search=Long%20time%20behaviour%20of%20one%20facilitated%20kinetically%20constrained%20models&per-page=10. Outcome: <HTTPError 429: 'Too Many Requests'>.
* 2026-10-11T22:03:36.116018: **crossref**; query `FA-1f convergence equilibrium`. URL: https://api.crossref.org/works?query=FA-1f%20convergence%20equilibrium&rows=30. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:03:39.306132: **semantic**; query `FA-1f convergence equilibrium`. URL: https://api.semanticscholar.org/graph/v1/paper/search?query=FA-1f%20convergence%20equilibrium&limit=30&fields=title,authors,year,externalIds,abstract,url. Outcome: <HTTPError 429: ''>.
* 2026-10-11T22:03:39.307454: **semantic_citations**; query `ARXIV:2510.20461 citations`. URL: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461/citations?fields=title,authors,year,externalIds,abstract,url&limit=100. Outcome: <HTTPError 429: ''>.
* 2026-10-11T22:03:41.910298: **github**; query `FA-1f`. URL: https://api.github.com/search/repositories?q=FA-1f&per_page=30. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:03:42.811289: **github_fredrickson**; query `Fredrickson Andersen`. URL: https://api.github.com/search/repositories?q=Fredrickson%20Andersen&per_page=30. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:10:39.573416: **arxiv_fredrickson**; query `all:Fredrickson AND all:Andersen`. URL: https://export.arxiv.org/api/query?search_query=all%3AFredrickson%20AND%20all%3AAndersen&sortBy=submittedDate&sortOrder=descending&max_results=100. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:10:40.498439: **arxiv_facilitated**; query `all:"facilitated" AND all:"equilibrium"`. URL: https://export.arxiv.org/api/query?search_query=all%3A%22facilitated%22%20AND%20all%3A%22equilibrium%22&sortBy=submittedDate&sortOrder=descending&max_results=80. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:10:40.746538: **crossref_recent**; query `Fredrickson Andersen; published since 2025-10-23`. URL: https://api.crossref.org/works?query.title=Fredrickson%20Andersen&filter=from-pub-date:2025-10-23&rows=60. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:10:40.852737: **crossref_source**; query `Long time behaviour of one facilitated kinetically constrained models`. URL: https://api.crossref.org/works?query.title=Long%20time%20behaviour%20of%20one%20facilitated%20kinetically%20constrained%20models&rows=10. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:10:42.306104: **openalex_source_retry**; query `arxiv:2510.20461`. URL: https://api.openalex.org/works?search=2510.20461&per_page=5. Outcome: <HTTPError 429: 'Too Many Requests'>.
* 2026-10-11T22:10:42.653036: **semantic_source_retry**; query `ARXIV:2510.20461`. URL: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds. Outcome: <HTTPError 429: ''>.
* 2026-10-11T22:10:42.939491: **front_pdf**; query `1803.08761`. URL: https://arxiv.org/pdf/1803.08761. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:11:05.786314: **openalex_title_retry**; query `one facilitated kinetically constrained models`. URL: https://api.openalex.org/works?search=one%20facilitated%20kinetically%20constrained%20models&per_page=5. Outcome: <HTTPError 429: 'Too Many Requests'>.
* 2026-10-11T22:13:10.990927: **arxiv_mathpr_recent**; query `https://export.arxiv.org/api/query?search_query=cat:math.PR AND (all:facilitated OR all:kinetically) AND submittedDate:[20251023 TO 20261011]&sortBy=submittedDate&sortOrder=descending&max_results=100`. URL: https://export.arxiv.org/api/query?search_query=cat%3Amath.PR%20AND%20%28all%3Afacilitated%20OR%20all%3Akinetically%29%20AND%20submittedDate%3A%5B20251023%20TO%2020261011%5D&sortBy=submittedDate&sortOrder=descending&max_results=100. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:13:10.991765: **recent_hierarchy**; query `https://arxiv.org/pdf/2609.18882`. URL: https://arxiv.org/pdf/2609.18882. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:13:10.992263: **recent_thermodynamic**; query `https://arxiv.org/pdf/2607.06205`. URL: https://arxiv.org/pdf/2607.06205. Outcome: HTTP success / raw response saved.
* 2026-10-11T22:21:45.978395: **arxiv_exact_recent**; query `cat:math.PR AND all:"kinetically constrained" AND submittedDate:[20251023 TO 20261011]`. URL: https://export.arxiv.org/api/query?search_query=cat%3Amath.PR%20AND%20all%3A%22kinetically%20constrained%22%20AND%20submittedDate%3A%5B20251023%20TO%2020261011%5D&sortBy=submittedDate&sortOrder=descending&max_results=100. Outcome: HTTP success / raw response saved.

A shell-inline attempt at the final exact-phrase query failed before issuing a request (Python quoting SyntaxError); final_search.py reruns it correctly.
