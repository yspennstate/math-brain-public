# Literature and source verification — initial and final log

Date: 2026-10-11. No published solution is asserted. Initial shell requests repeatedly timed out before execution; source and search requests were subsequently launched using research.py. Raw API responses and errors are retained in this folder with the names below. Until those results are inspected, literature status is unresolved.

Searches launched (exact URLs and outcomes are saved by research.py in search_log.json):

- Source: https://arxiv.org/pdf/1406.0763 ; Five remarks about random walks on groups, Problem 4, reported PDF page 25.
- arXiv export API: all:"conjugation-invariant" AND all:"random walk", maximum 20.
- OpenAlex works: "conjugation invariant random walk drift", 20 records.
- OpenAlex source identification: "Five remarks about random walks on groups", 5 records. Citing-work query is pending source identification.
- Crossref works: "conjugation invariant random walk drift", 20 records.
- Semantic Scholar graph API: "conjugation invariant random walk drift", 20 records with title, authors, year, URL and abstract.
- GitHub repositories: "conjugation invariant random walk".

Brain requests launched, read-only: brain.py recall "conjugation invariant metric drift mistakes"; math_recall.py "cancellation norm spelling length random walks". Their responses await inspection. Prior intake ledgers were searched for E0072, also pending tool output.

Mathematical lead: the cancellation/spelling norm of a free group, defined by planar inverse-letter matchings, gives the elementary counterexample proved in ATTEMPT.md. This terminology should be searched separately. The proof does not rely on finding this construction in print.

## Final verified results (supersedes the pending notes above)

Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, 7 July 2014. Source fetched successfully; saved PDF and complete text. Problem 4, PDF page 25, reads (spacing normalized and subscript typeset):

> Let (G, µ) be a symmetric measured group and suppose there exists a bi-invariant (conjugation-invariant) and µ-integrable (semi-)metric d on G. Is ℓ_d(µ) = 0?
>
> For instance, as a first test case, one could focus on the commutator subgroup G of the free group on two generators and the stable commutator length on G.

Page 1 defines measured groups as countable groups with semigroup-generating measure support, symmetry as µ(g)=µ(g^-1), and drift as the expected-distance limit. No properness or finite-ball condition appears. Every hypothesis is met by our F_32 counterexample. No paper found has been certified to state and prove the entire question as posed. Verdict is SOLVED by independent proof, not SOLVED_IN_LITERATURE. The bounded search establishes no novelty claim.

### Search outcomes and additional searches, all on 2026-10-11

Exact URLs and outcomes are retained in search_log.json, followup_search_log.json, and extra_search_log.json. research.py was run directly and then replayed by followup.py's import, so the initial seven requests were issued twice. Raw successful replies are saved under their query names.

1. Initial arXiv query above succeeded, returning three entries on matrix walks, holonomy fields and Kac's walk; no exact solution. Metadata/abstracts: arxiv_summary.json.
2. Both initial OpenAlex queries returned HTTP 429.
3. Initial Crossref query succeeded; broad mostly irrelevant results, no exact solution identified (crossref.txt).
4. Initial Semantic Scholar search returned HTTP 429.
5. GitHub search succeeded with zero repositories (github.txt).
6. arXiv query `all:"cancellation norm" OR all:"spelling length" OR (all:"bi-invariant" AND all:"random walks")`, max_results=30: successful, producing norm/spelling-length leads below; arxiv_cancellation.txt and arxiv_cancellation_summary.json.
7. OpenAlex lookup by `https://doi.org/10.48550/arXiv.1406.0763`: HTTP 429, preventing recovery of a canonical work ID.
8. OpenAlex citing-work fallback filter `cites:https://doi.org/10.48550/arXiv.1406.0763`, per-page=100: HTTP 429. The fallback could not be validated or resolved; an ID-based citing-work search was blocked by source lookup rate limits. No citing-work list obtained.
9. Semantic Scholar `paper/ARXIV:1406.0763/citations`, limit=100, fields=title,authors,year,url: successful, returning an empty data list (semantic_citations.txt). This database result does not establish absence of citations.
10. arXiv query `(all:"cancelation" OR all:"cancellation" OR all:"conjugation-invariant") AND (all:"drift" OR all:"random")`, max_results=40: successful, broad and capped, mostly small-cancellation groups, random permutations and unrelated applications; raw reply arxiv_cancelation_random.txt. No exact resolution certified.
11. Crossref title query `cancelation norm random walks biinvariant metrics`, rows=15: successful; crossref_norm.txt retained. Results included compact-hypergroup norm convergence and Hamiltonian diffeomorphism metrics, plus mostly irrelevant random-walk references; no exact drift theorem certified. The relevant cancelation-norm paper below was found through arXiv.
12. Direct fetch https://arxiv.org/pdf/1310.2921: successful, saved as cancelation_norm.pdf with full extraction cancelation_norm_text.txt. No occurrence of "random" found in its text; it is background, not a solution-in-print claim.

### Relevant references

Michael Brandenbursky, Światosław R. Gal, Jarek Kędra, Michał Marcinkowski, *The cancelation norm and the geometry of biinvariant word metrics*, arXiv:1310.2921v3, 2 April 2023 (initial preprint 2013), https://arxiv.org/abs/1310.2921. Proposition 2.A, PDF page 7, identifies cancelation norm with the biinvariant word norm. Theorem 1.C, PDF page 3, gives an O(n^3)-time/O(n^2)-memory algorithm on a free group. These are background for our construction, not drift theorems. The v3 text flags the older proof of Proposition 2.E as incomplete and supplies an erratum in Section 6. Our adjacent-inverse matching surgery is independently proved and does not rely on that old proof. The positive-drift counting argument is our deduction, so it is not labeled a solution in print.

Timothy Riley, *Computing area in presentations of the trivial group*, arXiv:1606.08833v4, https://arxiv.org/abs/1606.08833. The abstract establishes polynomial-time area/spelling-length algorithms and relates them to RNA folding. Metadata and abstract inspected; computational background only.

A. Majumdar, J. M. Robbins, M. Zyskin, *Tangent unit-vector fields: nonabelian homotopy invariants and the Dirichlet energy*, arXiv:0907.0478v1, https://arxiv.org/abs/0907.0478. Spelling length in free fundamental groups; metadata and abstract inspected, background predating the question.

Bence Borda, *Equidistribution of random walks on compact groups II. The Wasserstein metric*, arXiv:2004.14089v2, https://arxiv.org/abs/2004.14089. Compact groups with bi-invariant metrics and ergodic sum limit theorems; different setting and claims. Metadata and abstract inspected; not a solution of this question.

### Brain and prior attempts

Topic/mistakes recall `conjugation invariant metric drift mistakes` returned off-topic memories. math_recall.py queries `cancellation norm spelling length random walks` and `Brandenbursky Gal Kedra Marcinkowski cancelation` likewise returned off-topic cards, no relevant theorem. An initial topic recall did not execute because of tool-host timeout. No verdict inferred from brain results.

rg over permitted intake ledgers found E0072 and E0072-A001 in probability_1000_intake_E_20260908, dated 2026-09-08, attempted_unsolved. That attempt discussed homogeneous quasimorphisms and the scl supremum/limit obstruction. Its unsupported assertions of general monotonicity and quasimorphism-type structure were not used. Read-only git ls-tree of origin/master in math-open-problems found no path containing E0072 or five_remarks. No repository was modified.
