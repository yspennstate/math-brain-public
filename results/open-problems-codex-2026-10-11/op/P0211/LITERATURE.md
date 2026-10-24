# P0211 literature and source verification

Search date: 2026-10-11. No paper checked below was found to state and prove the relaxation-order question for this exact chain with the required uniform quantifiers. This is a bounded literature check, not an assertion of absence from all literature. The result in ATTEMPT.md is an original derivation.

## Primary source

David Aldous, Mixing times for coagulation-fragmentation processes, author-maintained open-problem page (first posted August 2012; page update February 2018): https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag.html . Linked notes: A special aggregation-fragmentation process, section 1 of coag_frag_mix.pdf, PDF pp. 1-4 (printed page labels 2-5). Copies and extracted text are saved here.

Exact hypotheses: integer partitions of n, pairwise constant merger rate 2/n, per-internal-link fragmentation rate beta>0; reversible mass proportional to (beta*n)^number_of_clusters/product m_j!. Proposition 1 is a fixed-beta n-to-infinity statement. The concluding remark also considers beta_n~b/n, with b>0, and suggests order sqrt(n).

Proposition 1 verbatim (mathematical symbols normalized from PDF extraction): "For the aggregation-fragmentation chain (M(t)) specified above, (1-o(1))(beta^2+4beta)^(-1/2) <= tau_2 <= beta^(-1) as n -> infinity." This is a bound, not the requested sharp order in the small-beta joint limit.

Page-4 remark verbatim: "Our arguments continue to apply in the setting where beta = beta_n ~ b/n, say, though here the upper and lower bounds on tau_2 have orders n and n^(1/2)." The subsequent sentence suggests order n^(1/2) and improved coupling.

## Relevant references and exclusions

- Nathanael Hoze; David Holcman. Stochastic coagulation-fragmentation processes with a finite number of particles and applications. The Annals of Applied Probability, volume 28, issue 3, pages 1449-1490, [[2018, 6, 1]]. DOI 10.1214/17-aap1334.
- E. Hingant; R. Yvinec. Deterministic and Stochastic Becker–Döring Equations: Past and Recent Mathematical Developments. Stochastic Processes, Multiscale Modeling, and Numerical Methods for Computational Cellular Biology, volume , issue , pages 175-204, [[2017]]. DOI 10.1007/978-3-319-62627-7_9.
- Durrett, Richard; Granovsky, Boris L.; Gueron, Shay. The Equilibrium Behavior of Reversible Coagulation-Fragmentation Processes. Journal of Theoretical Probability, 12, 447-474, 1999. DOI 10.1023/a:1021682212351. PDF downloaded via Aldous page (granovsky.pdf). Stationary distributions, reversibility and equilibrium observables; no identified relaxation-order theorem.

Hingant-Yvinec: arXiv:1609.00697 (2016 preprint), PDF downloaded. Section 3 deals with Becker-Doring monomer attachment/removal; these are different transitions. The survey references the stationary work of Durrett et al.; it provides no identified solution of the present spectral-gap order.

Hoze-Holcman: arXiv:1611.06493 (2016 preprint; later Annals of Applied Probability paper above), PDF downloaded. Stationary probabilities, moments and tagged-particle meeting/separation times are treated. Mean tagged-particle times are not spectral relaxation times; no matching relaxation-order theorem identified in the text.

Other arXiv leads: 2208.10699, Double Coset Markov Chains (Diaconis, Ram, Simper), uses permutation/double-coset coagulation-fragmentation chains, not this per-link linear-polymer chain; 1612.07036, Analytical results for a coagulation/decoagulation model on an inhomogeneous lattice, is a spatial lattice reaction model; 0811.1169 treats a deterministic Smoluchowski equation. None is an exact solution in print of P0211. The remaining returned titles and metadata remain saved in arxiv*.xml and crossref*.json; astrophysics, continuum PDE and species-sampling duality hits are off model.

GitHub repository query returned numerical PDE, species-sampling and clustering implementations (github.json); none supplied a matching proved theorem.

## Every network query / fetch

The initial source-page fetch was https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag.html on 2026-10-11, successful, saved as source.html. The following are the exact additional request URLs and outcomes:

- 2026-10-11: `https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf` — OK; payload `coag_frag_mix.pdf`.
- 2026-10-11: `https://arxiv.org/pdf/1609.00697` — OK; payload `hingant_yvinec.pdf`.
- 2026-10-11: `https://www.stat.berkeley.edu/~aldous/Research/OP/granovsky.pdf` — OK; payload `granovsky.pdf`.
- 2026-10-11: `http://export.arxiv.org/api/query?search_query=all%3A%22coagulation%20fragmentation%22%20AND%20%28all%3A%22spectral%20gap%22%20OR%20all%3A%22mixing%22%20OR%20all%3A%22relaxation%22%29&max_results=30` — OK; payload `arxiv.xml`.
- 2026-10-11: `https://api.openalex.org/works?search=coagulation%20fragmentation%20spectral%20gap&per-page=30` — HTTP Error 429: Too Many Requests; payload `openalex.json`.
- 2026-10-11: `https://api.crossref.org/works?query=coagulation%20fragmentation%20relaxation%20polymer&rows=30` — OK; payload `crossref.json`.
- 2026-10-11: `https://api.semanticscholar.org/graph/v1/paper/search?query=coagulation%20fragmentation%20spectral%20gap&limit=30&fields=title,authors,year,externalIds,url,abstract` — HTTP Error 429: ; payload `semantic.json`.
- 2026-10-11: `https://api.github.com/search/repositories?q=coagulation%20fragmentation` — OK; payload `github.json`.
- 2026-10-11: `https://export.arxiv.org/api/query?search_query=all%3A%22coagulation%22%20AND%20%28all%3A%22relaxation%22%20OR%20all%3A%22spectral%20gap%22%20OR%20all%3A%22linear%20polymers%22%29&max_results=50` — OK; payload `arxiv_target.xml`.
- 2026-10-11: `https://api.openalex.org/works?search=coagulation%20fragmentation&per_page=20` — HTTP Error 429: Too Many Requests; payload `openalex_retry.json`.
- 2026-10-11: `https://api.openalex.org/works?search=Coagulation%20fragmentation%20relaxation%20Aldous&per_page=10` — HTTP Error 429: Too Many Requests; payload `openalex_source.json`.
- 2026-10-11: `https://api.openalex.org/works/https://doi.org/10.1214/18-PS321` — HTTP Error 429: Too Many Requests; payload `openalex_hingant.json`.
- 2026-10-11: `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22coagulation%22%20%22mixing%22&fields=title,year,authors,externalIds,abstract` — HTTP Error 429: ; payload `semantic_retry.json`.
- 2026-10-11: `https://api.crossref.org/works?query=stochastic%20coagulation%20fragmentation%20spectral%20gap&rows=30` — OK; payload `crossref_target.json`.
- 2026-10-11: `http://export.arxiv.org/api/query?search_query=ti%3A%22Stochastic%20coagulation-fragmentation%20processes%22&max_results=10` — OK; payload `arxiv_finite.xml`.
- 2026-10-11: `http://export.arxiv.org/api/query?search_query=all%3A%22Aldous%22%20AND%20all%3A%22fragmentation%22%20AND%20%28all%3A%22mixing%22%20OR%20all%3A%22relaxation%22%29&max_results=30` — OK; payload `arxiv_aldous.xml`.
- 2026-10-11: `https://api.crossref.org/works?query.title=Deterministic%20and%20Stochastic%20Becker-Doring%20equations%20Past%20and%20Recent%20Mathematical%20Developments&rows=5` — OK; payload `crossref_survey.json`.
- 2026-10-11: `https://api.openalex.org/works?filter=locations.landing_page_url:https%3A//www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf&per_page=10` — HTTP Error 429: Too Many Requests; payload `openalex_citing_source.json`.
- 2026-10-11: `https://api.semanticscholar.org/graph/v1/paper/URL:https%3A//www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf?fields=title,citations.title,citations.year,citations.externalIds` — HTTP Error 404: Not Found; payload `semantic_source.json`.
- 2026-10-11: `https://arxiv.org/pdf/1611.06493` — OK; payload `hoze_holcman.pdf`.
- 2026-10-11: `https://api.crossref.org/works?query.title=The%20Equilibrium%20Behavior%20of%20Reversible%20Coagulation%20Fragmentation%20Processes&rows=5` — OK; payload `crossref_durrett.json`.

OpenAlex returned HTTP 429 for every query, including the source-URL index lookup. Therefore an OpenAlex source work ID and its citing works could not be retrieved. Semantic Scholar search attempts were rate limited (429), and the exact source URL was not indexed (404), so its citation list was unavailable. These failures are recorded rather than treated as negative search results. The initially guessed Hingant DOI in one failed OpenAlex lookup was not a verified identifier; Crossref subsequently gave the correct DOI above. No SOLVED_IN_LITERATURE verdict is warranted.

## Read-only brain and earlier-work checks

Ran math_recall.py on "Relaxation linear polymer coagulation fragmentation" and on "Boolean lattice up down operators harmonic multilinear spectral decomposition". Ran brain.py recall on "coagulation fragmentation mistakes" and "linear polymer coagulation fragmentation". The prior attempt card warns against substituting the mean into an exponential survival functional (wrong Jensen direction); the present proof avoids that step entirely. The harmonic query gave generic Boolean-function material rather than the needed decomposition; Section 3 of ATTEMPT.md proves the required algebra directly.

Searched all .jsonl and .md files under the specified probability_1000_intake_* and codex_pool_2026_10_10 folders with prior_search.py. Only the intake ranking mentioned P0211; no additional proof found in those files. Read-only git ls-tree of origin/master in math-open-problems found no path containing P0211. Neither the git working tree nor any brain/store/ledger was modified.
