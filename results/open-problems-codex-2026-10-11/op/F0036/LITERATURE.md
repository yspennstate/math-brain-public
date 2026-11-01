# Literature and searches — F0036

Checked 2026-10-12. Source downloaded from https://arxiv.org/pdf/1506.00724 into source.pdf; current version dated 2017-01-09, 80 PDF pages.

Exact source quote, printed/PDF page 72:
> Conjecture 8.3 (Potential most recent common ancestors) If we replace W({0} × R) in (8.3) by N({0} × R), then the set M is a locally finite subset of R × (0, ∞).

Equation (8.3) requires t>0, two paths started at time zero, equality at t, and strict ordering throughout (0,t). The conjecture is interpreted almost surely for the standard Brownian net of the survey. No change to random starting times or to short bubble excursions is permitted.

Reference: Emmanuel Schertzer, Rongfeng Sun, Jan M. Swart, The Brownian Web, the Brownian Net, and their Universality, in Advances in Disordered Systems, Random Processes and Some Applications (2016), DOI 10.1017/9781316403877.007; arXiv:1506.00724.

All API queries and failures are saved in search_log.json, with raw responses alongside it. Searches are bounded, not a certification that the conjecture remains open. No exact solving theorem has yet been identified.

Read-only brain consultations: math_recall “Brownian net relevant separation points meeting points local finiteness”; brain recall “Brownian net mistakes” and “Brownian net”. Results were unrelated and supply no relevant theorem. Intake F0036-A001 contains an explicitly unverified sketch; its inward-extremal identification is being audited.

## Search ledger (all executed 2026-10-12)

- arxiv: `https://export.arxiv.org/api/query`. Query: `{"search_query": "all:\"Brownian net\"", "max_results": 100, "sortBy": "submittedDate", "sortOrder": "descending"}`. Result: HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=45).
- openalex: `https://api.openalex.org/works?search=Brownian+net&per-page=100`. Query: `{"search": ["Brownian net"], "per-page": ["100"]}`. Result: 200.
- openalex_source: `https://api.openalex.org/works?search=The+Brownian+web+the+Brownian+net+and+their+universality&per-page=5`. Query: `{"search": ["The Brownian web the Brownian net and their universality"], "per-page": ["5"]}`. Result: 200.
- crossref: `https://api.crossref.org/works?query=Brownian+net+most+recent+common+ancestors&rows=40`. Query: `{"query": ["Brownian net most recent common ancestors"], "rows": ["40"]}`. Result: 200.
- semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1506.00724?fields=title%2Cyear%2CcitationCount%2Ccitations.title%2Ccitations.year%2Ccitations.externalIds`. Query: `{"fields": ["title,year,citationCount,citations.title,citations.year,citations.externalIds"]}`. Result: 429.
- github: `https://api.github.com/search/repositories?q=%22Brownian+net%22&per_page=30`. Query: `{"q": ["\"Brownian net\""], "per_page": ["30"]}`. Result: 200.
- arxiv_exact: `http://export.arxiv.org/api/query`. Query: `{"search_query": "all:\"potential most recent common ancestors\"", "max_results": 20}`. Result: HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=45).
- citing_published: `https://api.openalex.org/works?filter=cites%3AW2121110727&per-page=200`. Query: `{"filter": ["cites:W2121110727"], "per-page": ["200"]}`. Result: 200.
- citing_arxiv: `https://api.openalex.org/works?filter=cites%3AW4300525659&per-page=200`. Query: `{"filter": ["cites:W4300525659"], "per-page": ["200"]}`. Result: 200.
- crossref_net: `https://api.crossref.org/works?query.title=Brownian+net&rows=50`. Query: `{"query.title": ["Brownian net"], "rows": ["50"]}`. Result: 200.
- semantic_search: `https://api.semanticscholar.org/graph/v1/paper/search?query=Brownian+net&limit=100&fields=title%2Cyear%2CexternalIds%2Cabstract`. Query: `{"query": ["Brownian net"], "limit": ["100"], "fields": ["title,year,externalIds,abstract"]}`. Result: 429.
- openalex_exact: `https://api.openalex.org/works?search=%22potential+most+recent+common+ancestors%22&per-page=50`. Query: `{"search": ["\"potential most recent common ancestors\""], "per-page": ["50"]}`. Result: 200.
- arxiv_retry: `https://export.arxiv.org/api/query`. Query: `{"search_query": "ti:\"Brownian net\"", "max_results": 50}`. Result: HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=50).
- special_times: `https://arxiv.org/pdf/2512.10761`. Query: `{}`. Result: 200.
- universality: `https://arxiv.org/pdf/2401.09370`. Query: `{}`. Result: 200.
- special_points: `https://arxiv.org/pdf/0806.2326`. Query: `{}`. Result: 200.

The HTTP arXiv API endpoint redirected to HTTPS and timed out. The HTTPS broad search and a narrower retry also timed out. Successful direct arXiv PDF downloads supplemented these failed API searches; the API failures are not negative search results. Semantic Scholar returned HTTP 429 for the source-citation query and broad search. OpenAlex retrieved 52 works citing the published source and zero citing its separately indexed arXiv record. All 52 titles/metadata were screened; no title or metadata identified an exact solving theorem. These were not all read in full. Crossref's first broad ancestor query was noisy, so a title-focused Brownian-net search was added. GitHub returned two unrelated mobile geometric network repositories (jalt-online/brownian-networks; jalt-research/brownian-networks-2).

## Relevant papers and checked scope

1. E. Schertzer, R. Sun, J. M. Swart, The Brownian Web, the Brownian Net, and their Universality (source above). Checked equation (8.3) and Conjecture 8.3 on p.72; Proposition 2.7 (coalescing point-set density), Corollary 2.8, Theorem 2.11 (web special points), Theorem 3.2 (left/right marginals), Theorem 3.9 (wedge characterization), Proposition 3.14 (containment), Proposition 3.18 (deterministic-time density), Remark 3.21 (exceptional random times), Theorem 3.24 (net special points), Proposition 4.7 (relevant separation points), and Proposition 4.9 (finite graph). The relevant-separation theorem concerns dual time reversal, not reversal of the incoming forward paths in the PMRCA definition. It is a lead, not a solution of the conjecture.
2. E. Schertzer, R. Sun, J. M. Swart, Special points of the Brownian net, Electronic Journal of Probability 14 (2009), Paper 30, 805–864. DOI 10.1214/EJP.v14-641; arXiv:0806.2326. Downloaded special_points.pdf. Theorem 1.12 (structure of special points), printed PDF p.13, extends incoming/outgoing equivalence to full net paths. Conjecture 1.13 (three-connected points), printed PDF p.15, is a related unproved local-finiteness assertion. Our conditional three-arm reduction is in ATTEMPT.md Section 5; it is not a solution in print.
3. R. Sun, J. M. Swart, The Brownian net, Annals of Probability 36 (2008), 1153–1208. DOI 10.1214/07-AOP357. Results used through their statements in the checked survey; the original PDF was not fetched in this attempt.
4. R. Kou, Special times for the point set process of the Brownian Net, arXiv:2512.10761v1 (11 December 2025). Downloaded special_times.pdf. Theorem 1, PDF p.2: the set of times at which Xi_t has cluster points has Hausdorff dimension 1/2 almost surely. This concerns time slices rather than first meetings. It does not settle Conjecture 8.3 and does not justify local finiteness at a random first-contact time. Title/abstract/main theorem and text searches checked.
5. R. Sun, J. M. Swart, J. Yu, Universality of the Brownian net, arXiv:2401.09370v2 (15 September 2026). Downloaded universality.pdf. The main result concerns scaling limits of weakly branching/coalescing random walks with crossing paths and finite (3+epsilon)-moment increments. Title/abstract and full-text searches for ancestors, PMRCA, meeting points and conjecture references did not identify an exact theorem about M. Related scaling-limit work, not a printed solution.
6. E. Schertzer, R. Sun, J. M. Swart, Stochastic flows in the Brownian web and net, Memoirs of the AMS 227 (2014), no.1065; DOI 10.1090/S0065-9266-2013-00687-9. Proposition 6.5 is the origin of the finite graph result cited in survey Proposition 4.9. Consulted via the survey; not fetched in full.

The metadata references for all OpenAlex citation candidates are saved in citation_candidates.md. No source inspected states and proves the exact F0036 question. Literature status is “no exact solution identified in this bounded search”; no assertion of certified current openness is made.

## Earlier local research consulted read-only

- Intake ledger probability_1000_intake_F_20260908, F0036-A001: an explicitly unverified inward-extremal identification. Only the earliest-time inequality follows from containment.
- `git show origin/master:prob1000_lean_20260908/ultracode_20260909/F0036/memo.md` in ~/math-open-problems: a 2026-09-09 partial memo, not an accepted proof. Its claim that same-source witnesses contribute exactly one point also does not follow merely from a lower bound on first meeting time; we do not use it. Its recursive “equivalence” after random meeting times has not been proved and is not accepted here.
- The same repository's bruteforce_check.py was read as a method hint. We wrote an independent script in this folder with its own initial-time treatment and fresh exact checks.
- A filtered `git ls-tree` search for F0036 / Brownian-net / PMRCA paths identified the above files. A first unfiltered listing was unnecessarily large; no working-tree changes were made.
- During the attempt, a second math-store query, “Schertzer Sun Swart Brownian net three connected points”, was issued; any returned cards remain hints requiring source checks.

## Reopened attempt: newly checked published inputs (2026-10-12)

Direct shell/Python fetch: https://arxiv.org/pdf/math/0610625 (successful, arXiv v5 dated 13 June 2008, 58 PDF pages), saved as brownian_net_original.pdf and .txt. This is Sun–Swart, The Brownian net, Annals of Probability 36 (2008), no.3, 1153–1208, DOI 10.1214/07-AOP357. The source download is a new executed literature read, not a new all-service status search.

Checked verbatim primary assertions:

- Proposition 1.13 (Image set property), PDF p.14: “Let N be the Brownian net. Then, almost surely for all t ∈ [−∞,∞],” followed by equation (1.30), N ∩ Π_t = {π ∈ Π_t : π ⊂ ∪(N ∩ Π_t)}. Its inclusion of starting time minus infinity and quantifier over all paths are essential to the finite-segment grafting lemma in PROOF.md.
- Proposition 1.15(ii), PDF p.16: “N(∗,−∞) and −N(∗,−∞) are equal in law.” The minus sign denotes space-time rotation. PROOF.md uses (x,t)->(-x,-t), and swaps the left/right labels of the two witness curves. It does not need a separate unquoted spatial-symmetry theorem.
- Proposition 1.8 (Containment by left- and right-most paths), PDF p.10: “Let N be the Brownian net and let (Wl,Wr) be its associated left-right Brownian web. Then, almost surely, there exist no π ∈ N and l ∈ Wl such that l(s) ≤ π(s) and π(t) < l(t) for some σπ ∨ σl < s < t. An analogue statement holds for right-most paths.” This propagates local class bounds and supplies uniform spatial barriers.

Re-read Schertzer–Sun–Swart (2009), Special points of the Brownian net, arXiv:0806.2326, specifically:

- Equation (3.3), PDF p.31, in the proof of Proposition 3.6: equivalence of Law(N_T cap K) and Law(N_{-infinity} cap K) for deterministic compact K strictly later than T. The proof on pp.31–32 proves this intermediate assertion itself. This supplies the new approach's decisive null-event transfer; it was not used in the first attempt.
- Theorem 1.11(a),(b), PDF p.12, identifies extended representatives with true web representatives up to strong equivalence at separation points; Theorem 1.12(b), p.13, supplies the local sandwich for arbitrary outgoing net paths.
- The type-definition paragraph, PDF p.8, says subscript s means that incoming left-web paths belong to the left outgoing class and incoming right-web paths to the right outgoing class. This permits the canonical sandwich to use actual incoming l,r, exactly as required in Lemma 2.8.
- Proposition 2.6, PDF pp.22–23, identifies true separation points with separation points of incoming l and r.
- Lemma 2.8 and Proposition 2.9, PDF pp.24–25, give the relevant-separation definition and finite expected count for fixed time horizons. The reflected target box is strictly inside these horizons in the proof.
- Lemma 3.12, PDF p.36: “If z ∈ R² is a separation (resp. meeting) point of two paths π, π′ ∈ N, then z is of type (p, pp)_s (resp. (pp, p)).” It is applied only to paths started strictly before the fork, not merely to two paths born there.

These theorems do not individually state the exact F0036 answer. The reopened attempt's proposed full proof is a deduction from them, recorded in PROOF.md; it is not categorized as SOLVED_IN_LITERATURE. No novelty conclusion follows from these reads.

Descriptive-set-theoretic input used in the reopened proof: analytic subsets of Polish spaces are universally measurable. Standard reference: A. S. Kechris, Classical Descriptive Set Theory, Graduate Texts in Mathematics 156, Springer, 1995, section on regularity properties of analytic sets. This standard theorem is cited for completed-null-event transfer; no unverified theorem number is assigned.

Additional read-only mistake-audit query (2026-10-12): brain.py recall "local absolute continuity time reversal Brownian net mistakes". Invoked while the Lean check was queued; outcome pending at this save. Brain output is a hint, never a verdict.

Mistake-audit brain outcome: returned no Brownian-net theorem. It did return a generic warning about an invalid continuity-based path-limit inference in unrelated earlier work. The present proof does not transfer counts through weak path convergence: it constructs an analytic image event and transfers a completed null event under published local absolute continuity. The recall reported an in-memory index refresh and a failed automatic detached-refresh spawn; no brain write command was issued.

Final reopened assessment: SOLVED by the complete written deduction in PROOF.md. No exact stated solving theorem was found in the inspected literature, so SOLVED_IN_LITERATURE is not used. The auxiliary new Lean invocation remained queued and is not counted as verification.
