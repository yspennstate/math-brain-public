# Literature audit

Search date: 2026-10-12. Results below distinguish exact resolutions from related results.

- 2026-10-12 | source | `https://arxiv.org/pdf/math/0509695` | OK 722547

- 2026-10-12 | arxiv | `https://export.arxiv.org/api/query?search_query=all%3A%22entropic+repulsion%22+AND+%28all%3A%22convex%22+OR+all%3A%22pinned%22%29&max_results=40` | OK 21903

- 2026-10-12 | openalex | `https://api.openalex.org/works?search=entropic+repulsion+convex+pinned&per-page=30` | OK 523915

- 2026-10-12 | source_openalex | `https://api.openalex.org/works/https://doi.org/10.1214/154957806000000050` | OK 14785

- 2026-10-12 | crossref | `https://api.crossref.org/works?query=entropic+repulsion+pinned+convex+interface&rows=25` | OK 212384

- 2026-10-12 | semantic | `https://api.semanticscholar.org/graph/v1/paper/search?query=entropic+repulsion+convex+pinned&limit=30&fields=title%2Cauthors%2Cyear%2CexternalIds%2Cabstract%2Curl` | <HTTPError 429: ''>

- 2026-10-12 | github | `https://api.github.com/search/repositories?q=entropic+repulsion+convex` | <HTTPError 403: 'rate limit exceeded'>

- 2026-10-12 | arxiv2 | `https://export.arxiv.org/api/query?search_query=all%3A%22convex%22+AND+%28all%3A%22maximum%22+OR+all%3A%22extrema%22%29+AND+all%3A%22Ginzburg%22&max_results=30` | OK 7215

- 2026-10-12 | crossref2 | `https://api.crossref.org/works?query=pinned+harmonic+crystal+positive+origin&rows=15` | OK 57908

- 2026-10-12 | oa_convex | `https://api.openalex.org/works?search=entropic+repulsion+non+Gaussian+gradient+field&per-page=40` | OK 707093

- 2026-10-12 | citing | `https://api.openalex.org/works?filter=cites:W2172014396&per-page=100` | OK 1597187

## Brain and prior work (read only)
2026-10-12: brain.py recall queries: `pinned positive convex interface entropic repulsion`; `convex interface entropic repulsion mistakes`. Returned no useful on-target verified memory. math_recall.py query: `Velenik pinned origin entropic repulsion convex`; returned contextual cards, no exact resolution. Read intake probability_1000_intake_F_20260908/problems.jsonl and attempts.jsonl F0073 records. Attempt A001 contains an unproved upper-bound limiting step (see ATTEMPT.md). Read-only git ls-tree origin/master found no paths containing F0073.

## Verified source
Yvan Velenik, Localization and delocalization of random interfaces, Probability Surveys 3 (2006), 112?169. DOI: 10.1214/154957806000000050. arXiv:math/0509695v3. Exact open-problem quote and source hypotheses recorded in ATTEMPT.md. PDF p.22 (printed 133) explicitly states logarithmic average height at distance L from the boundary for uniformly strictly convex interactions with a full-box wall, citing [40].

## Existing box result
Jean-Dominique Deuschel and Giambattista Giacomin, Entropic repulsion for massless fields, Stochastic Processes and their Applications 89(2) (2000), 333?354. DOI: 10.1016/S0304-4149(00)00030-2. Source [40]; box result, not the origin-pinned positive infinite-volume question.

- 2026-10-12 | wetting | `https://arxiv.org/pdf/math/0604175` | OK 171159

- 2026-10-12 | bl_crossref | `https://api.crossref.org/works?query.title=On+stochastic+domination+in+the+Brascamp+Lieb+framework&rows=3` | OK 20617

- 2026-10-12 | dg_oa | `https://api.openalex.org/works/https://doi.org/10.1016/S0304-4149(00)00030-2` | OK 14252

- 2026-10-12 | dg_author | `https://www.lpsm.paris/pageperso/giacomin/` | OK 24372

- 2026-10-12 | maximum2016 | `https://arxiv.org/pdf/1610.04195` | OK 419663

- 2026-10-12 | maximum2024 | `https://arxiv.org/pdf/2403.11500` | OK 758845

- 2026-10-12 | dg_publisher | `https://www.sciencedirect.com/science/article/pii/S0304414900000302` | <HTTPError 403: 'Forbidden'>

- 2026-10-12 | bl_pdf | `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0305004102006552/S0305004102006552a.pdf/on-stochastic-domination-in-the-brascamp-lieb-framework.pdf` | <HTTPError 404: 'Not Found'>

- 2026-10-12 | dg_lpsmraw | `https://www.lpsm.paris/_export/raw/pageperso/giacomin/index` | OK 24372

- 2026-10-12 | arxiv_wetting_query | `https://export.arxiv.org/api/query?search_query=ti%3A%22Wetting+of+gradient+fields%22&max_results=5` | OK 2235

- 2026-10-12 | wetting_metadata | `https://api.openalex.org/works/W1970562499` | OK 12163

- 2026-10-12 | crossref_max | `https://api.crossref.org/works?query.title=Maximum+of+the+Ginzburg+Landau+fields&rows=3` | OK 42852


## Later leads inspected, not exact resolutions

- David Belius and Wei Wu, *Maximum of the Ginzburg–Landau fields*, arXiv:1610.04195v2 (18 June 2019), PDF pp.1–2, especially Theorem 1.1. It proves that the maximum of the **unconstrained zero-boundary field** divided by log N tends to 2√g in L² under even uniformly convex V. The PDF was fetched and the hypotheses and theorem read. There is no origin pin and no simultaneous positivity conditioning. It is a useful multiscale lead, not a solution of F0073.
- Florian Schweiger, Wei Wu and Ofer Zeitouni, *Tightness of the maximum of Ginzburg–Landau fields*, arXiv:2403.11500v1 (18 March 2024), PDF pp.1–3, Theorem 1.1. The potential additionally has V'' Lipschitz. The result is tightness of the centered maximum of the **unconstrained zero-boundary field**. It supplies approximate random-walk and barrier technology but does not prove this pinned-positive statement. PDF inspected.
- Giambattista Giacomin, *On stochastic domination in the Brascamp–Lieb framework*, Mathematical Proceedings of the Cambridge Philosophical Society 134(3) (2003), 507–514. DOI 10.1017/S0305004102006552. Metadata verified; attempted primary PDF fetch returned 404. No theorem from it is used or claimed to solve F0073.
- Holley/FKG association and Brascamp–Lieb variance inequality are standard theorem inputs to ATTEMPT.md. The full proofs of the new comparisons, energy identity and one-site reduction are recorded there. Velenik also cites Brascamp–Lieb and Giacomin's framework in the source.

## Search limitations and conclusion

The first OpenAlex text search returned 30 works and the second 40; these are bounded relevance searches, not exhaustive. The works-citing-source query returned all 93 indexed citing works in one page; the full response is citing.json and a title/DOI digest is citing_summary.txt. These are metadata records, not 93 full-paper reviews. arXiv searches and Crossref responses are saved alongside their queries. Semantic Scholar returned HTTP 429 and GitHub repository search HTTP 403 (rate limit); these services were attempted but their contents were not searched successfully.

One preliminary wetting download used an unverified guessed arXiv ID math/0604175, which actually is Braverman–Yampolsky on Julia sets. It is off-topic and excluded from the evidence. The exact-title arXiv query later corrects that discovery error. The D–G publisher primary-source fetch returned HTTP 403; the box input is verified at the survey level, not by an inspected theorem in that original paper.

No inspected paper states and proves F0073 with the same objects, hypotheses and quantifiers. Therefore SOLVED_IN_LITERATURE is not warranted. The bounded search does not certify that the problem remains open throughout all literature. Mathematical work continues as PARTIAL.

Journal metadata from Crossref: Belius–Wu, Annals of Probability 48(6) (2020), DOI 10.1214/19-AOP1416. Schweiger–Wu–Zeitouni, Annals of Probability (2026), DOI 10.1214/25-AOP1808; Crossref publication date 2026-09-01. Exact-title search identified Yvan Velenik, Wetting of gradient fields: pathwise estimates, arXiv:0706.1632v4, PTRF (2008), DOI 10.1007/s00440-007-0130-x.

- 2026-10-12 | corrected wetting primary PDF | `https://arxiv.org/pdf/0706.1632` | OK 163092

Velenik, Wetting of gradient fields: pathwise estimates, arXiv:0706.1632v4, PDF pp.1?3 and its height-proof discussion inspected. Its Hamiltonian has quadratic gradient interaction; its V is an external one-site potential. Its remarks allow convex-interaction extensions only where dependencies permit, and it does not state a proof of F0073. Excluded as an exact resolution.

Exact journal references: David Belius and Wei Wu, Maximum of the Ginzburg?Landau fields, Annals of Probability 48(6) (2020), 2647?2679, DOI 10.1214/19-AOP1416. Florian Schweiger, Wei Wu and Ofer Zeitouni, Tightness of the maximum of Ginzburg?Landau fields, Annals of Probability 54(5) (2026), 2436?2507, DOI 10.1214/25-AOP1808. During the attempt, math-store recall queries `Deuschel Giacomin entropic repulsion massless fields` and `Brascamp Lieb convex support variance` returned contextual or off-target cards, no exact result used.

Read the full math-store card claim_11fcc5b0b92d4300329a446dd3a28c80e7535335cb27eaecb364b7fce9c12206 (Concentric Decomposition of the 2D Gaussian Free Field) with --id on 2026-10-12. Its Gaussian-specific decomposition and coupling cautions are contextual hints; none are used as a theorem in our proofs.

2026-10-12 continuation: brain.py recall query `F0073 pinned positive convex field proof mistakes`; no memory containing F0073 and no on-target theorem found. No new literature resolution is asserted.

2026-10-12 final audit: re-read downloaded Velenik source PDF p.22 (printed 133), which explicitly states the full-box two-dimensional convex-interaction entropic-repulsion result and logarithmic average height. Exact extraction saved in verified_source_p22.txt. This confirms the dependency of our lower comparison; it is not a new literature resolution. No further web search was run during closure.
