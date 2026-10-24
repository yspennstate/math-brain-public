# Literature audit — 2026-10-12

## Exact source verified

Antal A. Járai, *Sandpile models*, Probability Surveys 15 (2018), 243–306, DOI 10.1214/14-PS228; arXiv:1401.0354v3, dated September 13, 2018. Downloaded https://arxiv.org/pdf/1401.0354 to jarai.pdf; text in jarai.txt and Unicode-normalized text in jarai_normalized.txt.

PDF page 61 (printed page 61), Section 6.2, verbatim statement with mathematical glyphs transcribed:

> Open Question 6.7. Consider Z². Is it true that for ν-a.e. η the configuration η + 1₀ can be stabilized with finitely many topplings? Note that for all x ∈ Z² we have Eν[n(o,x;·)] = limₙ→∞ Eνₙ[n(o,x;·)] = limₙ→∞ Gₙ(o,x) = ∞.

The following sentence says the first equality is not immediate and cites reference [5]. Infinite expectation is not a statement of almost sure infinite toppling.

Theorem 6.6 (PDF p. 60):

> [40, Theorem 3.11] Assume the hypotheses of Theorem 6.4. If in addition G is transient, then for ν-a.e. η and all x ∈ V, the configuration η + 1ₓ can be stabilized with finitely many topplings.

Theorem 6.4 (PDF p. 59) assumes that WSF-almost surely each tree has one end and proves ν_n⇒ν for every exhaustion. Thus the missing hypothesis for applying 6.6 on Z² is transience, despite its one-ended WSF.

Z² is recurrent, so this theorem does not apply. The source uses stable heights 0,…,deg(x)−1; on Z² these are 0,1,2,3. ν is the weak limit of uniform recurrent configurations on finite wired domains. The question asks for finite TOTAL topplings, not merely sitewise finiteness.

## Search record

Every HTTP request, URL (including exact encoded query), date, result size or error is saved in search_log.jsonl. Raw successful responses are retained. All searches use Python urllib; no built-in web search.

Initial services/queries on 2026-10-12:

- arXiv API: `all:sandpile AND all:avalanche`, newest 50; response arxiv.json (Atom XML).
- arXiv API: `all:sandpile AND (all:infinite OR all:two-dimensional)`, newest 80; response arxiv_target.json.
- OpenAlex works search: `sandpile avalanche finiteness`; HTTP 429.
- OpenAlex works search: `Sandpile models Jarai`; HTTP 429.
- OpenAlex retry: `sandpile models`; HTTP 429.
- Crossref works: `sandpile avalanches infinite volume`, 30 results; crossref.json.
- Semantic Scholar paper search: `sandpile avalanche finiteness`; HTTP 429.
- Semantic Scholar source record/citations: ARXIV:1401.0354; HTTP 429.
- GitHub repository search: `sandpile avalanche`; github.json. Repository hits cannot establish a published theorem.

Further source-title, finiteness and citation searches are being recorded in the same log.

## Earlier research (read-only)

Intake F0033-A001, 2026-09-08, in probability_1000_intake_F_20260908/attempts.jsonl: proposes reducing to number of waves, claiming individual waves are UST bushes. Treat this as unverified: the survey's bijection concerns the ensemble of all waves and two-root forests, and its argument explicitly uses transience. A numbered wave under ν is not automatically an unconditioned UST past.

Math recall for `sandpile avalanche finiteness recurrent Járai` and memory recalls for `sandpile avalanches mistakes` and `stationary sandpile Z2 finiteness` produced no reliable solution. Unrelated recall hits were discarded.

## Status

No exact solution has been verified. This is a bounded search with API failures, not a certification that no solution exists.

## Relevant papers checked in full text

1. Sandeep Bhupatiraju, Jack Hanson, Antal A. Járai, *Inequalities for critical exponents in d-dimensional sandpiles*, Electronic Journal of Probability 22 (2017), paper 85, 1–51, DOI 10.1214/17-EJP111; arXiv:1602.06475v2. Downloaded PDF in bhj.json (binary PDF despite suffix), extracted text in bhj.txt. PDF p. 5 explicitly states: “We do not have an upper bound on ν(R ≥ r) in d = 2, and it is an open problem whether ν(R < ∞) = 1.” Theorem 1.7, PDF pp. 7–8, controls the last k waves and the waves conditioned on N=k. Theorem 1.8 supplies ν(R≥r,N≤k)≤C_k r^(−α_k). Theorem 1.9, PDF p. 8: “Suppose d = 2. Then EνN = ∞.” These give a conditional reduction and rule out a uniform geometric stopping argument; none proves ν(N<∞)=1.

2. Robin Kaiser, Ecaterina Sava-Huss, Julia Überbacher, *Limit shape, avalanches, and stabilisation of abelian sandpiles on comb lattices*, arXiv:2609.21359v1, September 21, 2026. comb.json is the downloaded PDF, comb.txt its text. PDF p. 2: “In particular, it remains open whether on Z² the configuration η + δₒ can be stabilized in finitely many topplings.” Theorem 1.1, pp. 2–3, is about the comb lattice obtained by deleting all horizontal edges off the axis. It is not Z² and is not a solution to F0033. This is particularly recent explicit status evidence.

3. Nico Heizmann, Robin Kaiser, Ecaterina Sava-Huss, *Sandpiles on the Vicsek fractal explode with probability 1/4*, arXiv:2312.13647v2 (August 2024); published DOI 10.3150/24-BEJ1814. vicsek.json / vicsek.txt. Abstract p. 1 states stabilization with probability 3/4 and explosion with probability 1/4 on the infinite Vicsek fractal. Different graph: a warning against assuming recurrence alone forces a positive answer on Z².

4. Nikita Kalinin, Vladislav Khramov, *Sandpile group of infinite graphs*, arXiv:2305.05346v4 (June 9, 2025). group.json / group.txt. Its abstract specifies a C-net of sinks S⊂Z². With these sinks relaxation is well defined. This is a dissipative modification, not the sink-free infinite-volume addition in F0033.

## Citation and expanded search audit

Crossref exact bibliographic query `Sandpile models Antal Jarai Probability Surveys` correctly identifies DOI 10.1214/14-PS228 and pp. 243–306. An earlier author/title parameter query returned irrelevant items; they were not treated as evidence.

Semantic Scholar source DOI citation endpoint succeeded: `paper/DOI:10.1214/14-PS228/citations?fields=title,year,externalIds&limit=100`. It returned 57 citations and no next cursor. All title/model screens are preserved in citing_screen.md, with identifiers. The 2026 comb paper is the closest exact status lead. Recent hits on divisible sandpiles, stochastic one-dimensional models, Sierpiński identities and UST correlations concern different objects or observables. Two additional leads, exploding sandpile shape theorems and height-zero probability scaling, were fetched for abstract checks.

Further arXiv queries: `all:sandpile AND (all:finiteness OR all:stabilizability)` (50 results), and `all:sandpile AND (all:finite OR all:infinite)` (100 newest results). Responses arxiv_finite.json and arxiv_finite2.json are Atom XML. No exact solution was identified from the screened results.

OpenAlex retries by exact DOI, DOI filter, and quoted title were mostly rate-limited. A guessed DOI 10.1214/17-PS293 resolved successfully to a DIFFERENT paper, *Topics in loop measures and the loop-erased walk*, and was discarded. Similarly an initial citation request with unverified ID W2144458972 failed with 429 and is NOT a verified source-citation lookup. The corrected DOI-based source/citation requests are in search_log.jsonl. No successful OpenAlex citation list should be inferred from these failed requests. This audit explicitly keeps that coverage limitation.

Conclusion of status search: NOT SOLVED_IN_LITERATURE. Source question verified; September 2026 literature still explicitly calls it open; incomplete OpenAlex coverage acknowledged.

Final OpenAlex retry succeeded in identifying the exact source: `https://api.openalex.org/works/doi:10.1214/14-ps228` returned *Sandpile models*, ID W4230642927, saved in openalex_source_lower.json. Both subsequent VERIFIED source citation queries `filter=cites:W4230642927` (one sorted newest first) returned HTTP 429. Thus source identity is resolved, but the citing works could not be retrieved from this service. Semantic Scholar's successful 57-item citation list provides the citation screen used above.

Additional abstracts checked: Ahmed Bou-Rabee, *A shape theorem for exploding sandpiles*, arXiv:2102.04422, published DOI 10.1214/23-AAP1976: exploding backgrounds and growth shape, not the wired stationary ν assertion. Miles W. Elvidge and Antal A. Járai, *Scaling and partial universality of the height zero probability in the 2D Abelian sandpile*, arXiv:2607.26169v1 (July 30, 2026): one-site height scaling and conformal covariance, not avalanche finiteness. Full downloads and extracted texts are retained.

## Second-attempt neighbouring theorem check, 2026-10-12

Anne Fey, Lionel Levine, Yuval Peres, *Growth Rates and Explosions in Sandpiles*, Journal of Statistical Physics 138 (2010), 143–159, DOI 10.1007/s10955-009-9899-6; arXiv:0901.3805v2 (December 2009). Downloaded via Python at https://arxiv.org/pdf/0901.3805, retained as flp_growth.json (PDF), with normalized flp_growth.txt. Crossref query `Growth rates explosions sandpiles Fey Levine Peres` verified title, DOI, volume and pages; response flp_crossref.json. These requests are logged in search_log.jsonl.

Theorem 1.1, PDF p. 3, bounds growth on constant backgrounds d≤h≤2d−2. Theorem 1.2, PDF p. 4, gives robust periodic backgrounds with many saturated sites. Proposition 1.3, PDF p. 5, gives explosive sparse lattice perturbations, and Proposition 1.4 on the same page gives almost-sure explosiveness of background 2d−2 plus independent Bernoulli extra grains. In that paper “explosive” means there exists a finite number of added particles producing the explosive behaviour; it does NOT assert the F0033 single-grain statement for ν. Its sitewise notion of a finite toppling procedure must also be distinguished from finite TOTAL topplings. These results support the need to control geometry rather than density, but are not a solution to the stationary question.

The explicit periodic one-grain ladder and the fractional/integer barrier separation in SECOND_ATTEMPT.md are proved directly; no originality beyond this attempt is asserted. The survey's Section 5.5.1, PDF p. 35, explicitly discusses the rigorous proofs of stationary mean height 17/8 (Kenyon–Wilson, Poghosyan–Priezzhev–Ruelle and Kassel–Wilson), so that comparison is not based solely on a conjectured numerical density.

Brain gap queries and the rounding-mistake card actually consulted are recorded in BRAIN_SECOND.md. No useful stationary-tail theorem was retrieved. The second attempt does not upgrade the literature status to SOLVED_IN_LITERATURE.
