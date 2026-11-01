# G0001 literature audit — 2026-10-11

## Status and exact source

Continuation audit (2026-10-11): fetched the proof sources at exact commit cd090736b8f5984d49926e80363910e7c6441a4f, its Git commit and actual tree object 2a3d2c7bf05adf43607606504ab0911937d394ae, audit workflows, acceptance checker and public verification receipts. Initial 13 audit files match their pinned Git blob hashes. The comparator API reports its mathematical comparison step run and successful. Its logs artifact download returned HTTP 401 without credentials; release list is empty. Every exact URL, date, response size/hash or error is in pinned_request_log.jsonl, which is part of this literature log. See CERTIFICATE_AUDIT.md and MODEL_CORRESPONDENCE.md. Full local kernel replay is not claimed.

Later-discovered primary lead: a public critical-SITE extinction development at nitromannitol/percolation-after-anthropic was fetched and its statement definitions inspected. GitHub reports CI and comparator success at revision cd090736b8f5984d49926e80363910e7c6441a4f (2026-10-09). This is substantive evidence for a resolution claim, with independent full-certificate validation pending. It is not dismissed as bond-only. See the later status-lead section, ATTEMPT.md section 7, and CHECK_RECEIPTS.md. No current-openness assertion is inferred from older intake records.

No paper stating and proving the complete question with the same site model, theta(p)>0 hypothesis, and all p in (0,1) was verified. Therefore SOLVED_IN_LITERATURE is NOT assigned. This is a bounded search with incomplete OpenAlex access, not a guarantee that no solution exists.

Raphaël Cerf, *theta(pc,Z^d)=0?*, dated August 22, 2026; arXiv:2608.23661v1, submitted August 24, 2026, 708 PDF pages. PDF successfully fetched (93,839,721 bytes), saved as cerf_pdf.pdf and extracted as cerf_source.txt. IMPORTANT: the available arXiv HTML contains only part of the introduction and a shortened reference list; the PDF is the authority for the numbered statements here.

PDF page 1: “We consider the Bernoulli site percolation model on Zd with d ≥3. Each site is declared open with probability p and closed with probability 1 −p, and the sites are independent.”

Conjecture 1.4, PDF page 3, verbatim text with the mathematical layout normalized:

> Conjecture 1.4. Let d ≥ 3. For any p ∈ ]0,1[, we have the implication
> theta(p,Z^d) > 0 => lim inf_{n→∞} (1/ln n) ln ln (1/P_p(n ≤ |C(0)| < +∞)) > 0.

Theorem 1.2, PDF page 2, same normalization:

> Theorem 1.2. Let d ≥ 3 and let pc be the critical point for the Bernoulli site percolation in Zd. Denoting by C(0) the cluster of the origin, we have either theta(pc,Zd) = 0 or
> lim inf_{n→∞} (1/ln n) ln ln (1/P_pc(n ≤ |C(0)| < +∞)) = 0. (1.1)

Equation (1.5), PDF page 2, states for every p>pc the actual limit is 1-1/d. This is a strict-supercritical result; it does not include a hypothetical percolating critical point. It supports the reduction in ATTEMPT.md section 1, not a SOLVED_IN_LITERATURE verdict.

## Relevant references and disposition

1. Harry Kesten and Yu Zhang, *The Probability of a Large Finite Cluster in Supercritical Bernoulli Percolation*, Annals of Probability 18(2) (1990), 537–555. DOI: 10.1214/aop/1176990844. Cerf reference [84], PDF page 705. The source cites it for (1.5) initially above the slab threshold. This is a strict-supercritical input, not the theta>0 endpoint statement.
2. G. R. Grimmett and J. M. Marstrand, *The supercritical phase of percolation is well behaved*, Proceedings of the Royal Society of London A 430(1879) (1990), 439–457. Cerf reference [62], PDF page 703. The source invokes equality of slab and full critical parameters for (1.5). Primary complete proofs were not independently re-audited here; the reduction explicitly depends on the equation stated in the site source.
3. Geoffrey Grimmett, *Percolation*, 2nd ed., Grundlehren der mathematischen Wissenschaften 321, Springer-Verlag, Berlin, 1999. Cerf reference [63], PDF page 703. Background; no full endpoint solution verified.
4. Yacine Aoun and Kamil Khettabi, *Non-perturbative finite connectivities in supercritical Bernoulli percolation on Z^d with d≥3*, arXiv:2610.08682v1, submitted October 6, 2026. Abstract and full HTML fetched. Section 1.2 explicitly says “nearest-neighbour Bernoulli bond percolation” and “From now on, we consider p ∈ (pc,1).” Theorem 1.1 bounds a volume-conditioned two-point probability; Theorem 1.2 gives Ornstein–Zernike asymptotics for finite two-point connections. Model and parameter hypotheses both differ. Section 1.6 already assumes the Kesten–Zhang stretched-exponential volume bound. It is NOT a solution of G0001.
5. Tho Tran and Tan M. Nguyen, *Locality of Bernoulli Site Percolation on Transitive Graphs*, arXiv:2609.07026v1, September 2026. Abstract fetched; claims locality of the critical probability. That claim alone says nothing about theta(pc)=0 or the required conditional tail, so it is a lead only.
6. Joel Bassil, *Counterexamples to the site-percolation analogues of the Easo-Severo-Tassion cutset theorems*, arXiv:2608.29940v1, August 2026, 5 pp. Abstract fetched. Counterexamples involve modified rooted binary trees and gadgets. They do not counterexample G0001 on Z^d; they caution against transferring general edge-cutset theorems to site cutsets without checking geometry.
7. Sahar Diskin, Philip Easo, Ritvik Ramanan Radhakrishnan, Benny Sudakov and Vincent Tassion, *Supercritical sharpness of percolation*, arXiv:2603.03257v1, March 2026. Abstract fetched; claims finite-cluster decay exponentially in the isoperimetric profile for supercritical parameters. It predates Cerf and does not by its abstract settle the critical theta>0 endpoint. Full HTML inspection is recorded in the subsequent audit notes.

Semantic Scholar returned the source paper with no indexed citations. GitHub exact-id repository search returned total_count=0. Crossref recent search produced no matching full-scope mathematical theorem; it also returned future-dated records, which were not treated as papers available by the audit date. OpenAlex repeatedly returned HTTP 429 for search and DOI lookup. Resolving the source's OpenAlex work id and following its cited_by_api_url was therefore blocked. A DOI-based citing-filter attempt was made and returned 429 too; it is not a successful citing-works search and no conclusions are drawn from it.

## Read-only brain, ledger, and repository audit

Before/during the attempt: math_recall.py query “Cerf slab site percolation finite cluster tail”; brain.py recall “site percolation finite cluster tail criticality mistakes”; brain.py node prob1000_intake_g_fifteen_rows_2026_09_10. These are hints only. The memory and G0001-A001 intake attempt claim an equivalence with critical extinction; this work checks that equivalence against the SITE source and does not merge it with bond rows C0023/C0094.

Searched the probability intake ledgers with rg for G0001; earlier attempt G0001-A001 (September 10) says p>pc is known and leaves pc. Read origin/master:operations/claims/G0001.md with git show; it identifies the source and an earlier research slot but supplies no proof. No repository or brain store was written.

## Complete web query log

All requests use Python urllib from the shell (no built-in web search). Queries and responses follow, including failures.

- Date: 2026-10-11; service/request: cerf_pdf
  URL: https://arxiv.org/pdf/2608.23661
  Response: {"status": 200, "bytes": 93839721, "file": "cerf_pdf.pdf"}

- Date: 2026-10-11; service/request: cerf_abs
  URL: https://arxiv.org/abs/2608.23661
  Response: {"status": 200, "bytes": 37620, "file": "cerf_abs.txt"}

- Date: 2026-10-11; service/request: arxiv
  URL: https://export.arxiv.org/api/query?search_query=all%3A%22percolation%22+AND+%28all%3A%22finite+cluster%22+OR+all%3A%22Cerf%22%29&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending
  Response: {"status": 200, "bytes": 54973, "file": "arxiv.txt"}

- Date: 2026-10-11; service/request: openalex
  URL: https://api.openalex.org/works?search=Cerf+theta+percolation+critical&per-page=20
  Response: {"error": "HTTP Error 429: Too Many Requests"}

- Date: 2026-10-11; service/request: crossref
  URL: https://api.crossref.org/works?query=Cerf+percolation+finite+cluster+stretched+exponential&rows=20
  Response: {"status": 200, "bytes": 153614, "file": "crossref.txt"}

- Date: 2026-10-11; service/request: semantic
  URL: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.23661?fields=title,authors,year,citations.title,citations.year,citations.externalIds
  Response: {"status": 200, "bytes": 189, "file": "semantic.txt"}

- Date: 2026-10-11; service/request: github
  URL: https://api.github.com/search/repositories?q=percolation+criticality&per_page=20
  Response: {"status": 200, "bytes": 120329, "file": "github.txt"}

- Date: 2026-10-11; service/request: cerf_html
  URL: https://arxiv.org/html/2608.23661v1
  Response: {"result": "Saved cerf_html.txt, 47651 bytes"}

- Date: 2026-10-11; service/request: new_abs
  URL: https://arxiv.org/abs/2610.08682
  Response: {"result": "Saved new_abs.txt, 40541 bytes"}

- Date: 2026-10-11; service/request: new_html
  URL: https://arxiv.org/html/2610.08682v1
  Response: {"result": "Saved new_html.txt, 537474 bytes"}

- Date: 2026-10-11; service/request: openalex_exact
  URL: https://api.openalex.org/works?filter=doi%3Ahttps%3A%2F%2Fdoi.org%2F10.48550%2FarXiv.2608.23661&per-page=5
  Response: {"result": "HTTP 429 (OpenAlex)"}

- Date: 2026-10-11; service/request: openalex_tail
  URL: https://api.openalex.org/works?search=site+percolation+finite+cluster+tail&filter=from_publication_date%3A2026-08-24&per-page=30
  Response: {"result": "HTTP 429 (OpenAlex)"}

- Date: 2026-10-11; service/request: arxiv_exact
  URL: http://export.arxiv.org/api/query?search_query=all%3A%222608.23661%22+OR+%28all%3A%22site+percolation%22+AND+all%3A%22critical%22%29&max_results=20&sortBy=submittedDate&sortOrder=descending
  Response: {"result": "Saved arxiv_exact.txt, 40969 bytes"}

- Date: 2026-10-11; service/request: github_exact
  URL: https://api.github.com/search/repositories?q=%222608.23661%22&per_page=10
  Response: {"result": "Saved github_exact.txt, 55 bytes"}

- Date: 2026-10-11; service/request: openalex_citing
  URL: https://api.openalex.org/works?filter=cites%3Adoi%3A10.48550%2FarXiv.2608.23661&per-page=20
  Response: {"error": "HTTP Error 429: Too Many Requests"}

- Date: 2026-10-11; service/request: site_counter_abs
  URL: https://arxiv.org/abs/2608.29940
  Response: {"bytes": 39978}

- Date: 2026-10-11; service/request: site_locality_abs
  URL: https://arxiv.org/abs/2609.07026
  Response: {"bytes": 38681}

- Date: 2026-10-11; service/request: openalex_source_direct
  URL: https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2608.23661
  Response: {"error": "HTTP Error 429: Too Many Requests"}

- Date: 2026-10-11; service/request: supercritical_abs
  URL: https://arxiv.org/abs/2603.03257
  Response: {"bytes": 38224}

- Date: 2026-10-11; service/request: crossref_recent
  URL: https://api.crossref.org/works?query=site+percolation+critical+finite+cluster+Cerf&filter=from-pub-date%3A2026-08-24&rows=20
  Response: {"bytes": 199318}

- Date: 2026-10-11; service/request: supercritical_html
  URL: https://arxiv.org/html/2603.03257v1
  Response: {"bytes": 623960}

- Date: 2026-10-11; service/request: site_locality_html
  URL: https://arxiv.org/html/2609.07026v1
  Response: {"bytes": 3414438}



## Later primary-source status lead: critical SITE extinction

The historical reconciliation report at origin/master:research7_2026-09-17/R7-06/screens/2026-09-18T200200Z__G0001_external_formal_resolution_reconciliation.md claims a public September 5 resolution. We fetched the cited homepage, companion page, repository metadata, README, Hypergraph/FinalCriticality.lean, VERIFICATION.md, recursive source tree, comparator challenge/solution, workflow metadata, and docs/kn-results.pdf/tex. Files and complete requests are saved locally.

Ahmed Bou-Rabee, *Percolation after Anthropic*, public formal Lean development, https://github.com/nitromannitol/percolation-after-anthropic ; companion page https://nitromannitol.github.io/site-percolation-7d3f2/ . The formal declaration KNAll.Site.site_no_percolation_at_critical states thetaSite d (criticalProbSiteI d)=0 for d>=3 with only d and the numerical lower-bound binder. It applies its ExactCommonQAssembly theorem. The independent comparator's product site measure, graph and cluster definitions were inspected and match the intended model at statement level. Authors' verification claims are retained, but the full dependency chain has not been independently rebuilt here.

This is a SITE resolution claim, so it must not be discarded as a bond-only result. It would imply G0001 by the complete argument in ATTEMPT.md sections 1 and 7 if verified. It does not satisfy this task's strict SOLVED_IN_LITERATURE rule: the numbered theorem with the full finite-tail implication has not been found. The downloaded 28-page finite-inequality manuscript does not state that theorem. Accordingly record it as a substantive lead with certification pending, and do not assert current openness from the older intake label.

Also read and rechecked the earlier boundary-score/local-uniqueness artifact at origin/master:research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T191000Z__G0001_boundary_score_local_uniqueness_reduction.md. Its exact parameter comparison is proved in ATTEMPT.md section 8; it leaves the high-boundary sector.

Full HTML of Tran–Nguyen confirms Theorem 1.1 is convergence of critical SITE parameters under local graph convergence. Diskin et al.'s proof explicitly selects q in (pc,p) and further smaller supercritical parameters; that mechanism cannot be applied at pc from theta(pc)>0 alone. Neither source gives the complete target statement.

Additional query log entries (including all later fetches):

- {"date": "2026-10-11", "service": "openalex_citing", "url": "https://api.openalex.org/works?filter=cites%3Adoi%3A10.48550%2FarXiv.2608.23661&per-page=20", "error": "HTTP Error 429: Too Many Requests"}
- {"date": "2026-10-11", "service": "site_counter_abs", "url": "https://arxiv.org/abs/2608.29940", "bytes": 39978}
- {"date": "2026-10-11", "service": "site_locality_abs", "url": "https://arxiv.org/abs/2609.07026", "bytes": 38681}
- {"date": "2026-10-11", "service": "openalex_source_direct", "url": "https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2608.23661", "error": "HTTP Error 429: Too Many Requests"}
- {"date": "2026-10-11", "service": "supercritical_abs", "url": "https://arxiv.org/abs/2603.03257", "bytes": 38224}
- {"date": "2026-10-11", "service": "crossref_recent", "url": "https://api.crossref.org/works?query=site+percolation+critical+finite+cluster+Cerf&filter=from-pub-date%3A2026-08-24&rows=20", "bytes": 199318}
- {"date": "2026-10-11", "service": "supercritical_html", "url": "https://arxiv.org/html/2603.03257v1", "bytes": 623960}
- {"date": "2026-10-11", "service": "site_locality_html", "url": "https://arxiv.org/html/2609.07026v1", "bytes": 3414438}
- {"date": "2026-10-11", "service": "bourabee_home", "url": "https://nitromannitol.github.io/", "bytes": 15905}
- {"date": "2026-10-11", "service": "site_proof_repo", "url": "https://api.github.com/repos/nitromannitol/percolation-after-anthropic", "bytes": 6328}
- {"date": "2026-10-11", "service": "site_proof_readme", "url": "https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/README.md", "bytes": 17486}
- {"date": "2026-10-11", "service": "site_proof_page", "url": "https://nitromannitol.github.io/site-percolation-7d3f2/", "bytes": 43701}
- {"date": "2026-10-11", "service": "site_proof_final", "url": "https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/Hypergraph/FinalCriticality.lean", "bytes": 10577}
- {"date": "2026-10-11", "service": "site_proof_verify", "url": "https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/VERIFICATION.md", "bytes": 6548}
- {"date": "2026-10-11", "service": "site_proof_tree", "url": "https://api.github.com/repos/nitromannitol/percolation-after-anthropic/git/trees/main?recursive=1", "bytes": 73551}
- {"date": "2026-10-11", "service": "site_manuscript_tex", "url": "https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/docs/kn-results.tex", "bytes": 110215}
- {"date": "2026-10-11", "service": "site_comparator_challenge", "url": "https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/PercolationAudit/SiteCriticality/Challenge.lean", "bytes": 5687}
- {"date": "2026-10-11", "service": "site_comparator_solution", "url": "https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/PercolationAudit/SiteCriticality/Solution.lean", "bytes": 1856}
- {"date": "2026-10-11", "service": "site_repo_actions", "url": "https://api.github.com/repos/nitromannitol/percolation-after-anthropic/actions/runs?per_page=5", "bytes": 72342}
- {"date": "2026-10-11", "service": "site_manuscript_pdf", "url": "https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/docs/kn-results.pdf", "bytes": 416395, "pages": 28}
