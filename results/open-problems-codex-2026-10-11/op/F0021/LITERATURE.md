# Literature search

Search date: 2026-10-12 (machine date).
- source: `https://arxiv.org/pdf/2401.01757`
- arxiv: `https://export.arxiv.org/api/query?search_query=all:heavy-tailed+AND+all:polymer&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending`
- openalex: `https://api.openalex.org/works?search=heavy%20tailed%20directed%20polymer&per-page=30`
- crossref: `https://api.crossref.org/works?query=heavy%20tailed%20directed%20polymer&rows=20`
- semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2401.01757?fields=title,year,citations.title,citations.year,citations.externalIds`
- github: `https://api.github.com/search/repositories?q=heavy+tailed+directed+polymer`
- arxiv_kpz: `https://export.arxiv.org/api/query?search_query=all%3A%22directed+polymer%22+AND+%28all%3Auniversality+OR+all%3Aheavy%29+AND+submittedDate%3A%5B20240101+TO+20261012%5D&max_results=70&sortBy=submittedDate&sortOrder=descending` (2026-10-12).
- arxiv_fixed: `https://export.arxiv.org/api/query?search_query=all%3A%22polymer%22+AND+all%3A%22fixed+temperature%22&max_results=30` (2026-10-12).
- openalex_retry: `https://api.openalex.org/works?search=directed%20polymer%20heavy%20tail&per_page=20` (2026-10-12).
- openalex_source: `https://api.openalex.org/works?filter=title.search:Directed%20polymers%20in%20a%20random%20environment&per_page=10` (2026-10-12).
- semantic_retry: `https://api.semanticscholar.org/graph/v1/paper/search?query=heavy%20tailed%20directed%20polymer&limit=20&fields=title,year,externalIds` (2026-10-12).
- crossref_kpz: `https://api.crossref.org/works?query.bibliographic=directed%20polymer%20KPZ%20universality&filter=from-pub-date:2024-01-01&rows=25` (2026-10-12).
- newchaos: `https://arxiv.org/pdf/2602.04429` (2026-10-12).
- physics: `https://arxiv.org/pdf/1411.1242` (2026-10-12).
- improved: `https://arxiv.org/pdf/2509.21453` (2026-10-12).
- lindeberg: `https://arxiv.org/pdf/2304.04871` (2026-10-12).
- crossref_source: `https://api.crossref.org/works?query.title=Directed%20polymers%20in%20a%20random%20environment%20a%20review%20of%20the%20phase%20transitions&rows=3` (2026-10-12).
- semantic_citations: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2401.01757/citations?fields=title,year,externalIds&limit=100` (2026-10-12).
- openalex_citations: `https://api.openalex.org/works?filter=cites:https%3A%2F%2Farxiv.org%2Fabs%2F2401.01757&per_page=100` (2026-10-12).
- finite_moments: `https://arxiv.org/pdf/2609.08308` (2026-10-12).
- high_temp: `https://arxiv.org/pdf/2503.20192` (2026-10-12).
- openalex_doi: `https://api.openalex.org/works/https://doi.org/10.1016/j.spa.2024.104431` (2026-10-12).

## Verified source and hypothesis corrections

Nikos Zygouras, *Directed polymers in a random environment: A review of the phase transitions*, Stochastic Processes and their Applications **177** (2024), article 104431, DOI 10.1016/j.spa.2024.104431; arXiv:2401.01757v4, 12 September 2024. Downloaded PDF has 49 pages and title-page date September 13, 2024.

Question 5, PDF p. 42, transcribed with mathematical typography normalized:
> Derive the limiting behaviours in the rest of the phase diagram. Do Airy and KPZ asymptotics extend when γ = 0 and α > 5 ?

Assumption 3, PDF p. 37: the right tail is x^{-α}L(x), α>0, L slowly varying. For α>2 the disorder has mean zero and variance one. The left-tail domination assumption is imposed only for α≤2. The field is iid, and the walk is the d=1 simple symmetric walk from the review's general definition. Section 5.1 uses the unnormalized exponential-weight partition function. Section 5.2 uses a different product-weight model and does not give an answer here. The phrase “domain of attraction of an α-stable law” in the intake is misleading for α>2; the actual assumption in this question is regular variation of the right tail. The Gaussian result is Theorem 5.2(ii), not 5.3(ii).

## Search outcomes and coverage limitations

- arXiv heavy-tail search: returned 22 entries; later broad polymer/universality search returned 17 entries. Raw Atom responses are saved. Screened titles and abstracts, and downloaded the most relevant later PDFs.
- Crossref: initial heavy-tail query returned 20 ranked results; post-2024 polymer/KPZ query returned 25 ranked results; source query returned 3. Raw responses are saved. These are bounded ranked searches, not exhaustive bibliographies.
- GitHub repository search: HTTP success, `total_count=0` for the recorded query; this cannot rule out papers or code with other terminology.
- Semantic Scholar source/citation lookup and general search initially returned HTTP 429. The direct citations endpoint then succeeded, returning 30 citing records and no next page. Full response is in semantic_citations.json; all records are listed below.
- OpenAlex general searches, source-title lookup, and source DOI lookup returned HTTP 429. An attempted citing-works request using the arXiv source URL also returned HTTP 429; that form was not validated. A resolved OpenAlex source ID could not be obtained, so an actual OpenAlex citing-works list could not be retrieved. This is a coverage gap, not a negative search result.
- The exact source URL and every external query/fetch URL are recorded above. No built-in web search was used.

## Relevant references and why they do not close Question 5

1. Partha S. Dey and Nikos Zygouras, *High temperature limits for (1+1)-dimensional directed polymer with heavy-tailed disorder*, Annals of Probability **44**(6) (2016), 4006–4048, DOI 10.1214/15-AOP1067; arXiv:1503.01054. This is the review's source for neighbouring high-temperature regimes, not the fixed-temperature α>5 KPZ assertion.
2. Quentin Berger and Niccolò Torri, *Directed polymers in heavy-tail random environment*, Annals of Probability (2019), DOI 10.1214/19-AOP1353; arXiv:1802.03355. Also *Entropy-controlled Last-Passage Percolation*, arXiv:1805.11989. These are the nearby energy/entropy-driven regimes cited by the source, not a proof for α>5 at fixed temperature. This classification follows the review's statements; no new complete reading of these two PDFs is claimed.
3. Antonio Auffinger and Oren Louidor, *Directed polymers in random environment with heavy tails*, arXiv:1001.1028 (2010). Source for the α<2 ballistic variational regime, as stated in the review's Theorem 5.5. Not a result for α>5.
4. Thomas Gueudré, Pierre Le Doussal, Jean-Philippe Bouchaud and Alberto Rosso, *Ground-state statistics of directed polymers with heavy-tailed disorder*, Physical Review E **91** (2015), 062110, DOI 10.1103/PhysRevE.91.062110; arXiv:1411.1242, PDF title *Revisiting Directed Polymers with heavy-tailed disorder*. Downloaded PDF describes a “mostly numerical study” of ground states. It supports the fifth-moment threshold in a zero-temperature setting but is not a theorem about the fixed-positive-temperature polymer in Assumption 3.
5. Julian Ransford, *Universality of directed polymers in the intermediate disorder regime*, Annals of Probability **53**(3) (2025), 1019–1048, DOI 10.1214/24-AOP1724; arXiv:2304.04871v2. Downloaded PDF establishes an intermediate-disorder universality range 1/5<temperature exponent<1/4. The parameter tending to zero excludes γ=0; it does not prove this question.
6. Pranay Agarwal, *Improved universality bounds for directed polymers in the intermediate disorder regime*, Electronic Communications in Probability **31** (2026), 1–12, DOI 10.1214/26-ECP752; arXiv:2509.21453v1. Downloaded arXiv PDF, Theorem 1.2 and Theorem 1.3, p. 3: the inverse temperature is n^{-a}, a in (2/(3K+11),1/4) for the comparison theorem, and a in (2/17,1/4) for its general-disorder consequence, improved to (1/10,1/4) with vanishing third moment. Theorem 1.3 requires a moment generating function finite near zero. Both fixed temperature and regularly varying positive tails fall outside those hypotheses. Here a is a temperature exponent, not this problem's tail exponent α. This is a lead, not a solution in print.
7. Gaspard Gomez, *Disordered systems and (subcritical) polynomial chaos with heavy-tail disorder*, arXiv:2602.04429v1 (4 February 2026). Downloaded PDF p. 1 fixes heavy-tail exponent in (1,2) and intermediate-disorder scaling, with Lévy-chaos limits. It addresses a different tail range and regime.
8. Dang-Zheng Liu, Fangzhou Luo, Tian Wu and Yuxuan Zong, *Subcritical limits of a 1D KPZ growth surface with finite moments*, arXiv:2609.08308v1 (8 September 2026). Downloaded PDF Theorem 1.3 and 1.4, p. 2: subcritical noise scale N^{-1/4-ε}, ε>0, bounded eighth moments (or stronger moment condition), additive SHE limit. Example 1.2 includes a polymer recursion, but its effective inverse temperature tends to zero. This is not fixed-temperature KPZ/Airy universality, and α>5 does not imply eight moments.
9. Makoto Nakashima, *A note on the asymptotics of the free energy of 1+1 dimensional directed polymers in random environment at high temperature*, arXiv:2503.20192v1 (26 March 2025). Downloaded PDF Theorem 1.1, p. 3 gives lim_{β→0} F(β)/β^4=-1/6 under exponential-moment hypotheses stated on p. 2. This concerns the deterministic free-energy density at high temperature, not n^{1/3} fluctuations at fixed β with heavy tails.

No checked paper states and proves the precise fixed-temperature α>5 question under Assumption 3. Accordingly this run does NOT use SOLVED_IN_LITERATURE. The search does not prove global absence of a solution, especially given the OpenAlex access failures.

## Semantic Scholar works citing the review (retrieved 2026-10-12)
- Percolation Markov Decision Processes (2026); arXiv: 2609.19905; DOI: not supplied.
- Moments Comparison Inequalities for Critical 2d Stochastic Heat Flow, Polymers and GMC (2026); arXiv: 2609.12820; DOI: not supplied.
- Subcritical limits of a 1D KPZ growth surface with finite moments (2026); arXiv: 2609.08308; DOI: not supplied.
- Free energy and phase transition for 2D directed polymers with critical spatial correlations (2026); arXiv: 2608.30829; DOI: not supplied.
- Disorder Thresholds and Free Energy of Brownian Directed Polymers with Product and Radial Spatial Correlations (2026); arXiv: 2608.29501; DOI: not supplied.
- A Spectral Route to Directed-Polymer Glasses (2026); arXiv: 2608.03730; DOI: not supplied.
- Information Rate Decomposition for Noisy Nanopore Channels with Geometric Duplication (2026); arXiv: 2606.06808; DOI: 10.48550/arXiv.2606.06808.
- Sharp behavior of the free energy for the two-dimensional directed polymer model (2026); arXiv: 2605.30707; DOI: not supplied.
- On a fractional stochastic heat equation arising from the disordered pinning model (2026); arXiv: 2603.01823; DOI: not supplied.
- From Disordered Systems to the Critical 2D Stochastic Heat Flow (2025); arXiv: 2511.08479; DOI: 10.1137/25m181129x.
- Non-coincidence of critical points for directed polymers on supercritical percolation clusters (2025); arXiv: 2510.24532; DOI: not supplied.
- Non-directed polymers in random environments with range penalties: the high-dimensional case (2025); arXiv: 2509.17319; DOI: 10.30757/alea.v23-33.
- A central limit theorem for two-dimensional directed polymers with critical spatial correlation (2025); arXiv: 2509.16694; DOI: not supplied.
- The Random Walk Pinning Model I: Lower bounds on the free energy and disorder irrelevance (2025); arXiv: 2509.08789; DOI: not supplied.
- Sharp moment and upper tail asymptotics for the critical $2d$ Stochastic Heat Flow (2025); arXiv: 2507.22029; DOI: not supplied.
- Probing Phase Transitions of Finite Directed Polymers near a Corrugated Wall via Two-Replica Analysis (2025); arXiv: 2507.15332; DOI: 10.3390/e28020190.
- Enhanced noise sensitivity, 2D directed polymers and Stochastic Heat Flow (2025); arXiv: 2507.10379; DOI: not supplied.
- Singularity and regularity of the critical 2D Stochastic Heat Flow (2025); arXiv: 2504.06128; DOI: not supplied.
- A note on the asymptotics of the free energy of $1+1$ dimensional directed polymers in random environment at high temperature (2025); arXiv: 2503.20192; DOI: not supplied.
- A random polymer approach to the weak disorder phase of the vertex reinforced jump process (2025); arXiv: 2503.10209; DOI: not supplied.
- Coincidence of critical points for directed polymers for general environments and random walks (2025); arXiv: 2502.04113; DOI: 10.2140/om.2026.3.89.
- On the Moments of the Mass of Shrinking Balls Under the Critical 2d Stochastic Heat Flow (2024); arXiv: 2410.14601; DOI: 10.1007/s00220-026-05616-2.
- Equivalence of fluctuations of discretized SHE and KPZ equations in the subcritical weak disorder regime (2024); arXiv: 2410.06801; DOI: 10.2140/pmp.2025.6.819.
- Edwards–Wilkinson fluctuations in subcritical 2D stochastic heat equations (2024); arXiv: 2405.09520; DOI: 10.1214/25-ecp735.
- The Tail Distribution of the Partition Function for Directed Polymers in the Weak Disorder Phase (2024); arXiv: 2405.04335; DOI: 10.1007/s00220-025-05246-0.
- On the space-time fluctuations of the SHE and KPZ equation in the entire $L^{2}$-regime for spatial dimensions $d \geq 3$ (2024); arXiv: 2402.06874; DOI: not supplied.
- Strong disorder and very strong disorder are equivalent for directed polymers (2024); arXiv: 2402.02562; DOI: 10.24033/asens.1849.
- Local limit theorem for directed polymers beyond the $L^{2}$-phase (2023); arXiv: 2307.05097; DOI: 10.4171/jems/1650.
- Localization of the continuum directed random polymer (2022); arXiv: 2203.03607; DOI: 10.1007/s00440-024-01345-6.
- Minicourse: Semilinear stochastic heat equations in the critical dimension (None); arXiv: not supplied; DOI: not supplied.

The recent finite-moment surface paper and the high-temperature free-energy paper were fetched and inspected as above. Other citing titles predominantly concern d≥2, weak disorder, pinning, correlated disorder, or different models; a title screen is not a full theorem audit of each.

## Read-only internal evidence consulted

- math_recall.py query: “directed polymer KPZ heavy tails universality”; returned general KPZ and tail cards, not a closure theorem.
- brain.py recall query: “heavy tailed directed polymer mistakes”; node codex_wave_c0120_fluctuation_exponent_directed_polymers_beyond_2026_10_10 read in full. It records no closure of that neighbouring problem and is provisional.
- `rg` of intake records found F0021-A001 (2026-09-08) in probability_1000_intake_F_20260908/attempts.jsonl. Its order-one cost for visiting the full-cone maximum is refuted in ATTEMPT.md, Lemma 3.
- `git ls-tree` on origin/master of math-open-problems, filtered by F0021 and C0120, located C0120 campaign files but no F0021 path under probability_campaigns. No working tree was changed.
- Brain/store content is used as a hint only. The actual mathematical statements in ATTEMPT.md have independent proofs.


## Additional local searches (2026-10-12)
All were read-only.
- `rg -n -m 3 F0021 ~/<private-repo>/06_math_research --glob '*.jsonl' --glob '*.md'` (intake and campaign records).
- `git -C ~/math-open-problems ls-tree -r --name-only origin/master` (initial tree enumeration, output too large; subsequent queries were filtered).
- Same tree enumeration piped to `rg 'F0021|C0120'` and limited to first 35 paths.
- Tree enumeration restricted to probability_campaigns and piped to `rg 'F0021'` (no matching paths).
- `rg -n 'Assumption 1|Zβ|\[DZ16\]|\[BT19\]|\[GL' source.txt` (source model and reference locations).
- `rg -n 'Theorem|alpha|stable|2602' newchaos.txt` (PDF-extracted text contained null bytes; searched pages were subsequently read with PyMuPDF).
- Python XML parsing of saved arXiv entries by titles and summaries; Python extraction of Crossref titles, DOI, dates and reference metadata; Python reading of the complete saved Semantic Scholar citing inventory. Scripts and raw outputs are retained in this folder.


## Additional attempt (2026-10-12)
- Read-only math_recall.py query: `directed polymer transversal confinement heavy tails Lindeberg replacement universality Ransford`; general Lindeberg and provisional C0120 gap cards, no closure.
- Two new approaches and choice recorded in SECOND_ATTEMPT.md.
- Additional fetch (2026-10-12): Berger?Torri entropy-controlled LPP, `https://arxiv.org/pdf/1805.11989`.
- Second read-only math_recall.py query: `Berger Torri entropy controlled last passage percolation quadratic entropy ordered points`; returned generic entropy/FPP cards, no relevant closure.
- Fetched and read Berger–Torri, *Entropy-controlled Last-Passage Percolation*, arXiv:1805.11989v1 (29 May 2018), Theorem 2.1 p. 3 and entropy definition (2.1) p. 2. Its application theorems use alpha<2; not a solution of F0021. The additional attempt independently proves an iid-marking chain bound with a lattice correction, rather than invoking the continuum volume bound in a lattice setting.

The additional attempt read the remaining gap, queried the math store twice as recorded above, and fetched the neighbouring entropy-controlled LPP paper. It did not find or claim a new solution in print. No additional global literature-status assertion supersedes the bounded search and OpenAlex access limitation from the first attempt. Saved computational and Lean records independently document the additional mathematical work.
