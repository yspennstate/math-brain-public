# Literature audit — C0159, 2026-10-11

## Status and source verification

No paper retrieved states and proves the full question under arbitrary transitivity. This is NOT SOLVED_IN_LITERATURE. Search coverage has explicit limitations: OpenAlex was HTTP 429 throughout; the Semantic Scholar source-citation request succeeded but keyword search and the Bell citation request were rate-limited. Negative search results are not a proof of absence.

Olle Häggström and Johan Jonasson, “Uniqueness and non-uniqueness in percolation theory”, Probability Surveys 3 (2006), 289–344, DOI 10.1214/154957806000000096; arXiv:math/0612812v1, 28 December 2006. The Project Euclid endpoint returned HTTP 200 with an Incapsula HTML block (1165 bytes), not a PDF. The full paper was retrieved instead from https://arxiv.org/pdf/math/0612812 and its title page confirms the journal and DOI. Local copy: source_arxiv.txt (PDF bytes) and source_arxiv_extracted.txt.

The correct locator is the END OF SECTION 5, printed pp.308–309, PDF pp.20–21, immediately before Section 6. The quoted passage is:

> “Suppose for some p in the non-uniqueness regime of a transitive nonamenable graph G that we can find two infinite clusters C1 and C2 that come within distance 1 from each other in infinitely many places. Call two such infinite clusters strongly neighboring.”

> “If this is the case for any p, then G is said to exhibit cluster repulsion. Häggström et al. [57] conjectured that cluster repulsion holds for any transitive graph, and supplemented their conjecture with a non-transitive counterexample. Very recently, Timár [101] proved the conjecture under the additional assumption of unimodularity, by means of an ingenious mass-transport argument. The nonunimodular case remains open.”

These quotations normalize PDF ligatures and diacritics, and concatenate the text split across pp.308–309. The source discussion is iid bond percolation, with transitive, connected finite-degree graphs. It defines contact at distance ONE, not an arbitrary bounded radius. ATTEMPT.md explicitly proves an all-finite-radius continuity reduction, and retains the intake's stronger target without claiming the definitions equivalent. No simultaneous-in-p almost-sure assertion is inferred.

## Relevant exact references and scope

1. Ádám Timár, “Neighboring clusters in Bernoulli percolation”, Annals of Probability 34(6) (2006), 2332–2343, DOI 10.1214/009117906000000485, arXiv:math/0702873v1 (28 February 2007). Full text retrieved. Theorem 1.1, printed p.2332, PDF p.1:

> “Let G be a quasi-transitive unimodular graph and consider Bernoulli(p) edge percolation on it. Then any two infinite clusters touch each other in only finitely many vertices almost surely.”

The introduction specifies local finiteness and touching at distance 1. The theorem requires unimodularity, so it does not solve C0159. The 2006 journal year and 2007 arXiv posting are different dates, not a bibliographic error.

2. Sasha Bell, Tasmin Chu, Owen Rodgers, Grigory Terlov, and Anush Tserunyan, “Heavy repulsion of clusters in Bernoulli percolation”, arXiv:2509.10631v1 (2025). Full text retrieved (19 PDF pages). Theorem 1.2, printed/PDF p.3, verbatim apart from math typography:

> “Suppose G is a connected locally finite quasi-transitive nonunimodular graph. Then any two heavy clusters come within unit distance of each other only in a light set of vertices P_p-almost surely.”

The preceding definitions fix Bernoulli(p) bond percolation and light = finite total Haar-stabilizer weight. Question 1.1 on p.2 asks repulsion at any p; p.3 explicitly says “Question 1.1 still remains open.” Line-by-line scope comparison: transitive graphs are quasi-transitive, but only HEAVY clusters are covered; unit distance is R=1; LIGHT is not FINITE; and no all-finite-radius conclusion is asserted. This is a lead and the input theorem for Section 1 of ATTEMPT.md, not a published solution. Pages 2–3 also recall continuity of two-point connectivity as sufficient, leaving only countably many exceptional p. The final proof in ATTEMPT.md supplies the detailed sprinkling argument for every finite radius.

3. Ádám Timár, “Percolation on nonunimodular transitive graphs”, Annals of Probability 34(6) (2006), 2344–2364, DOI 10.1214/009117906000000494; arXiv:math/0702875v1. Full text retrieved. It treats critical percolation, heavy clusters and nonunimodular examples, not a solution of cluster repulsion. Its grandmother graph is the grandparent graph used in this attempt.

4. Tom Hutchcroft, “Nonuniqueness and mean-field criticality for percolation on nonunimodular transitive graphs”, arXiv:1711.02590; Journal of the American Mathematical Society, DOI 10.1090/jams/953. Abstract retrieved through arXiv search and Semantic Scholar citation metadata. Establishes p_c<p_h<=p_u, not cluster repulsion. Full text not fetched in this attempt.

5. Pengfei Tang, “Heavy Bernoulli-percolation clusters are indistinguishable”, arXiv:1809.01284. Abstract retrieved via arXiv search. Heavy indistinguishability does not give unweighted repulsion.

6. Grigory Terlov and Ádám Timár, “Weighted-amenability and percolation”, arXiv:2502.02560v2 (2025). Abstract retrieved via arXiv search. Weighted amenability and heavy phase thresholds are adjacent topics; no repulsion solution is stated in the retrieved abstract.

7. Shirshendu Chatterjee, Yang Chen, and Grigory Terlov, “β-Skewed Maximal Spanning Forests”, arXiv:2609.11845v1 (2026). Full text retrieved. Its forest equalities and counterexample concern a different question. Example 2.3 confirms the grandparent weight ratios k,k^2,1/k,1/k^2. No cluster-repulsion theorem was found in the retrieved text.

8. Martin P. W. Zerner, “Infinite light rays and infinite clusters with infinitely many pivots”, arXiv:2610.12460, submitted 8 October 2026 according to the retrieved abstract page, retrieved following the source's Semantic Scholar citation list. Full text retrieved. This is about Lorentz mirror trajectories and bundled random one-ended trees with variable parallel-edge multiplicities, not two distinct Bernoulli clusters on a fixed transitive graph. The title's “light rays” refers to trajectories, not modular-weight light clusters. No inference of a transitive counterexample is justified.

9. Gábor Pete, “A note on percolation on Z^d: isoperimetric profile via exponential cluster repulsion”, Electronic Communications in Probability 13 (2008), DOI 10.1214/ECP.v13-1390; arXiv:math/0702474. Crossref and arXiv abstract retrieved. Finite versus infinite cluster estimates on Z^d do not resolve the question.

## Searches and fetches (all performed 2026-10-11)

Every HTTP request made in this attempt is listed below with the exact encoded query URL and the result. Raw responses are saved beside this file; search_log.jsonl is the machine-readable ledger. An OpenAlex citing-source filter request was attempted but rate-limited before any result could be validated; its DOI filter spelling was not validated as an OpenAlex works-ID lookup.

- **source**: `https://projecteuclid.org/journals/probability-surveys/volume-3/issue-none/Uniqueness-and-non-uniqueness-in-percolation-theory/10.1214/154957806000000096.pdf` — 200; 1165 bytes
- **bell_abs**: `https://arxiv.org/abs/2509.10631` — 200; 41014 bytes
- **openalex**: `https://api.openalex.org/works?search=cluster+repulsion+nonunimodular&per-page=30` — HTTP Error 429: Too Many Requests
- **openalex_source**: `https://api.openalex.org/works/https://doi.org/10.1214/154957806000000096` — HTTP Error 429: Too Many Requests
- **arxiv**: `http://export.arxiv.org/api/query?search_query=all%3A%22cluster+repulsion%22&max_results=30` — 200; 17793 bytes
- **semantic**: `https://api.semanticscholar.org/graph/v1/paper/search?query=cluster+repulsion&limit=30&fields=title%2Cyear%2Cauthors%2Curl%2Cabstract` — HTTP Error 429: 
- **github**: `https://api.github.com/search/repositories?q=cluster+repulsion+percolation` — 200; 55 bytes
- **bell_pdf**: `https://arxiv.org/pdf/2509.10631` — 200; 521691 bytes
- **crossref**: `https://api.crossref.org/works?query=cluster+repulsion+percolation&rows=30` — 200; 216334 bytes
- **openalex_citing**: `https://api.openalex.org/works?filter=cites%3Adoi%3A10.1214%2F154957806000000096&per-page=100` — HTTP Error 429: Too Many Requests
- **arxiv_nonunimodular**: `https://export.arxiv.org/api/query?search_query=all%3Anonunimodular+AND+%28all%3Arepulsion+OR+all%3Aclusters%29&max_results=40&sortBy=submittedDate&sortOrder=descending` — 200; 14695 bytes
- **openalex_retry**: `https://api.openalex.org/works?search=Neighboring+clusters+Bernoulli&per-page=10` — HTTP Error 429: Too Many Requests
- **semantic_source**: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/154957806000000096?fields=title,year,citations.title,citations.year,citations.externalIds` — 200; 22525 bytes
- **crossref_source**: `https://api.crossref.org/works/10.1214/154957806000000096` — 200; 1765 bytes
- **arxiv_source**: `https://export.arxiv.org/api/query?search_query=ti%3A%22Uniqueness+and+non-uniqueness+in+percolation+theory%22&max_results=5` — 200; 2869 bytes
- **timar_pdf**: `https://arxiv.org/pdf/math/0702873` — 200; 172079 bytes
- **source_arxiv**: `https://arxiv.org/pdf/math/0612812` — 200; 649606 bytes
- **light_rays_abs**: `https://arxiv.org/abs/2610.12460` — 200; 41169 bytes
- **light_rays_pdf**: `https://arxiv.org/pdf/2610.12460` — 200; 532652 bytes
- **bell_citing**: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2509.10631?fields=title,year,citations.title,citations.year,citations.externalIds` — HTTP Error 429: 
- **recent_forest**: `https://arxiv.org/pdf/2609.11845` — 200; 416048 bytes
- **nonunimodular_timar**: `https://arxiv.org/pdf/math/0702875` — 200; 266071 bytes

## Read-only research brain and earlier records

The second math-store recall returned Michael Aizenman, Harry Kesten, and Charles M. Newman, “Uniqueness of the infinite cluster and continuity of connectivity functions for short and long range percolation” (1987), DOI 10.1007/BF01219071, as source card source_db0bd4fe5f8c95bb56d302b5a91d32963791018848265459875802796ed42435. This is a potentially relevant continuity lead, not a fetched or checked theorem for the nonuniqueness regime, and no inference from it was used.

Ran math_recall.py with “percolation cluster repulsion Timar heavy clusters” and later “Haggstrom Schonmann connectivity function continuity repulsion”. Ran brain.py recall with “nonunimodular percolation cluster repulsion” and “nonunimodular percolation mistakes”. No relevant checked theorem was identified in the initial results. Read-only rg search for C0159 under 06_math_research located the intake and C0159-A001. That attempt left a tilted-mass-transport gap and suggested upward parallel clusters on the grandparent graph; Propositions 3.1–3.2 and Theorem 6.1 give a checked mathematical response to that lead. The ledger's statement that a counterexample needs contacts in one modular class was not accepted as a theorem. The present superlevel bound shows why summably decreasing weights are instead an unresolved possibility in general.

Ran git ls-tree -r --name-only origin/master with C0159/cluster-repulsion path patterns in ~/math-open-problems; no matching path was returned. No repository working tree was touched. No brain/store write command was invoked.

## Conclusion

Bounded searches found no full published answer, and the 2025 paper expressly retains the open question. The correct research verdict is PARTIAL: the written attempt proves the grandparent-graph special case and a general continuity reduction, while the arbitrary nonunimodular case remains unproved. No novelty claim is made for these special-case arguments.

## Second-attempt follow-up, 2026-10-11

The gap itself was queried in the math store, read-only, with these exact questions:

* `percolation connectivity right continuity nonuniqueness cluster repulsion Hutchcroft Tang`
* `Hutchcroft L2 boundedness percolation tilted susceptibility p_t p_h`

The first returned the already identified Aizenman–Kesten–Newman continuity reference, but no theorem resolving the nonunique phase. The second returned draft card claim_a66fd0813e6c88c86b2d79faff1ff2561984be25f8a01527e1ac5e03aa9db9bc (“Draft uniqueness obstruction to operator boundedness”). It was read in full with `math_recall.py --id` and its assertion was independently proved in SECOND_ATTEMPT.md instead of accepting its provisional label as evidence.

Two additional full-text requests were made with Python urllib and logged to search_log.jsonl:

* https://arxiv.org/pdf/1711.02590 — HTTP 200, 1,126,550 bytes; saved as hutchcroft_nonunimodular_full.txt (PDF bytes) and hutchcroft_nonunimodular_full_extracted.txt. Retrieved version is arXiv:1711.02590v3, 25 February 2020; title page dated 26 February 2020. Exact reference: Tom Hutchcroft, “Non-uniqueness and mean-field criticality for percolation on nonunimodular transitive graphs”, DOI 10.1090/jams/953. Its Theorem 1.8, PDF/printed p.9, reads, with mathematical glyphs normalized:

  > “Let G be a connected, locally finite graph and suppose that Γ ⊆ Aut(G) is transitive and nonunimodular. Then p_c(G) < p_c(G, Γ, λ) ≤ p_t(G, Γ) for every λ ∈ (0, 1).”

  The definitions on p.8 identify p_t=p_c(1/2), with p_c(λ) the supremum of parameters of finite tilted susceptibility. They also state p_t≤p_h and expressly note that both equality and strict inequality occur. Its Remark 7.2 records boundedness of T_p for p<p_t. The theorem supplies a nonempty initial interval, not every p or every light-cluster parameter. SECOND_ATTEMPT.md gives the independent Schur calculation and the additional sprinkling implication; this is a literature-assisted reduction, not SOLVED_IN_LITERATURE.

* https://arxiv.org/pdf/1904.05804 — HTTP 200, 373,520 bytes; saved as hutchcroft_L2_full.txt (PDF bytes) and hutchcroft_L2_full_extracted.txt. Exact reference: Tom Hutchcroft, “The L² boundedness condition in nonamenable percolation”, arXiv:1904.05804v2, 23 September 2020 (title-page date 24 September 2020); Electronic Journal of Probability, DOI 10.1214/20-EJP525. Definitions on p.3 give p_(q→q). Page 4 recalls p_c<p_(2→2) for graphs admitting a quasi-transitive nonunimodular group and the uniqueness obstruction to boundedness. Theorem 2.2, p.6, concerns exponential two-point decay, not the full cluster-repulsion conjecture. The retrieved paper is a relevant neighbouring-area source, not a full answer to C0159.

No new broad status search is presented as having eliminated the open gap. This follow-up was targeted at the two new approaches requested by the user. Its result remains PARTIAL: bounded-operator parameters, a quantitative contact tail, and a verified nonempty interval above p_c on every nonunimodular transitive graph. At high nonunique parameters the new sufficient hypothesis may fail, as the grandparent example proves. The finite-interface partition approach remains unproved. No novelty claim is made.

The half-tilt normalization was checked against the modular-function definition on PDF p.12 of arXiv:1711.02590v3: in the transitive case Delta(u,v)=|Gamma_v u|/|Gamma_u v|, equal to the stabilizer Haar-measure ratio used in this attempt. Its reference [2] also confirms the full Aizenman–Kesten–Newman citation: Communications in Mathematical Physics 111(4) (1987), 505–531, DOI 10.1007/BF01219071. The AKN paper itself was not fetched or used as an unverified theorem.

During the referee audit the operator hypothesis was weakened further by a direct BK argument: finite two-point column square sums suffice for a finite expected contact count. This is written out in SECOND_ATTEMPT.md Theorem D.2. It is an independently derived sufficient criterion, not a theorem claimed to solve the entire question in a retrieved paper. The new remaining gap was also queried in the math store with `percolation bubble diagram cluster repulsion BK touching`; any returned cards are hints rather than a proof of finite bubbles in the nonunique regime. GP(2), p=3/4 explicitly has infinite bubble diagram, so a universal finite-bubble claim would be false.
