# E0093 literature record — 2026-10-12

## Status

No exact arbitrary-finite-group solution was located in this bounded search.
This is **not** a proof of openness. Verdict: PARTIAL, not
SOLVED_IN_LITERATURE. All primary texts used are saved here as *.raw PDFs
and extracted *.txt files. The source is verified directly, not from an
intake paraphrase.

## Source, verbatim (PDF page 9, Question 2)

> The same set of problems can be considered for any group G. If a generating
> set S is chosen at random, what is the typical rate of convergence? This is
> the topic of random random walks. Hildebrand [37] gives a survey. Babai,
> Beals, and Seress [4] give the best bounds on the diameter of such random
> Cayley graphs. These may be turned into (perhaps crude) rates of convergence
> via bounds in [26]. I cannot resist adding mention of one of my old
> conjectures. For the alternating group A_n, it is known that a randomly
> chosen pair of elements generate A_n with probability approaching 1. I
> conjecture that the random walk based on any generating pair gets random
> in at most n^3 log n steps.

Mathematical subscripts and superscripts rendered in plain text; wording
preserved. The preceding Wilson theorem assumes an ergodic chain and concerns
uniform choice from N sampled binary vectors. The broad question supplies no
fixed generator-count regime, no group sequence, and no explicit laziness or
symmetrization convention. The embedded worst-case A_n conjecture has a
different quantifier from a typical-random-generating-set assertion.

Reference: Persi Diaconis, “Some things we've learned (about Markov chain
Monte Carlo),” Bernoulli 19(4) (2013), 1294–1305.
DOI: 10.3150/12-BEJSP09. arXiv:1309.7754.

## Every online query and fetch

All requests used Python urllib from the shell. No built-in web search.
URLs encode the exact query, ordering, limits, and fields.

- 2026-10-12 `diaconis_pdf`: https://arxiv.org/pdf/1309.7754 — HTTP 200, 242879 bytes.
- 2026-10-12 `arxiv`: http://export.arxiv.org/api/query?search_query=all%3A%22random%20Cayley%22%20AND%20all%3Amixing&start=0&max_results=40 — HTTP 200, 9301 bytes.
- 2026-10-12 `arxiv_https`: https://export.arxiv.org/api/query?search_query=all%3A%22random%20Cayley%22%20AND%20all%3Amixing&start=0&max_results=40 — HTTP 200, 9301 bytes.
- 2026-10-12 `openalex`: https://api.openalex.org/works?search=random%20Cayley%20graphs%20mixing&per-page=40 — HTTP Error 429: Too Many Requests.
- 2026-10-12 `openalex_source`: https://api.openalex.org/works?search=Some%20things%20we%20have%20learned%20about%20Markov%20chain%20Monte%20Carlo&per-page=5 — HTTP Error 429: Too Many Requests.
- 2026-10-12 `crossref`: https://api.crossref.org/works?query=random%20Cayley%20graphs%20mixing&rows=30 — HTTP 200, 159193 bytes.
- 2026-10-12 `semantic`: https://api.semanticscholar.org/graph/v1/paper/search?query=random%20Cayley%20graphs%20mixing&limit=30&fields=title,authors,year,externalIds,url,abstract — HTTP Error 429: .
- 2026-10-12 `github`: https://api.github.com/search/repositories?q=random%20Cayley%20mixing&per_page=20 — HTTP 200, 55 bytes.
- 2026-10-12 `arxiv_general`: https://export.arxiv.org/api/query?search_query=all%3A%22random%20Cayley%22&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending — HTTP 200, 82675 bytes.
- 2026-10-12 `arxiv_hildebrand`: https://export.arxiv.org/api/query?search_query=ti%3A%22survey%22%20AND%20au%3AHildebrand&max_results=10 — HTTP 200, 1957 bytes.
- 2026-10-12 `openalex_source_retry`: https://api.openalex.org/works/https://doi.org/10.3150/12-BEJSP09 — HTTP Error 429: Too Many Requests.
- 2026-10-12 `openalex_citing`: https://api.openalex.org/works?filter=cites:doi:10.3150/12-BEJSP09&per-page=50 — HTTP Error 429: Too Many Requests.
- 2026-10-12 `semantic_source`: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1309.7754?fields=title,year,citations.title,citations.year,citations.externalIds — HTTP Error 429: .
- 2026-10-12 `crossref_specific`: https://api.crossref.org/works?query.title=mixing%20random%20Cayley%20graphs&rows=25 — HTTP 200, 120428 bytes.
- 2026-10-12 `nilpotent_pdf`: https://arxiv.org/pdf/2403.12355 — HTTP 200, 619202 bytes.
- 2026-10-12 `abelian_pdf`: https://arxiv.org/pdf/2102.02809 — HTTP 200, 883313 bytes.
- 2026-10-12 `dihedral_pdf`: https://arxiv.org/pdf/2510.19942 — HTTP 200, 407166 bytes.
- 2026-10-12 `discussion_pdf`: https://arxiv.org/pdf/1911.02975 — HTTP 200, 541838 bytes.
- 2026-10-12 `hildebrand_pdf`: https://arxiv.org/pdf/math/0401189 — HTTP 200, 322419 bytes.
- 2026-10-12 `uppertriangular_pdf`: https://arxiv.org/pdf/1911.02974 — HTTP 200, 834988 bytes.
- 2026-10-12 `diameter2026_pdf`: https://arxiv.org/pdf/2605.29457 — HTTP 200, 453060 bytes.
- 2026-10-12 `lie_pdf`: https://arxiv.org/pdf/1309.1975 — HTTP 200, 866290 bytes.
- 2026-10-12 `openalex_doi_final`: https://api.openalex.org/works/doi:10.3150/12-BEJSP09 — HTTP 200, 15163 bytes.
- 2026-10-12 `crossref_abelian`: https://api.crossref.org/works/10.4171/JEMS/1743 — HTTP 200, 8899 bytes.
- 2026-10-12 `semantic_bulk`: https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22random%20Cayley%22%20mixing&fields=title,year,authors,externalIds — HTTP 200, 1331 bytes.
- 2026-10-12 `openalex_valid_citations`: https://api.openalex.org/works?filter=cites:W2073769344&per-page=100 — HTTP Error 429: Too Many Requests.

- 2026-10-12 additional OpenAlex retry: https://api.openalex.org/works?filter=cites:W2073769344&per-page=100 — HTTP 429.
- 2026-10-12 additional OpenAlex retry: https://api.openalex.org/works?search=random%20Cayley%20graphs%20mixing&per-page=40 — HTTP 429.

OpenAlex eventually returned the source as W2073769344, with 32 citing works
in its metadata. The correctly formed citing-works requests remained rate
limited. The earlier cites:doi filter was not a valid resolved-ID citation
query; it too received 429 and supplied no citation evidence. Citation
coverage is therefore incomplete. Semantic Scholar's ordinary search and
source-citation lookup returned 429, but its bulk search succeeded with four
results: Hermon–Thomas (2018), Hermon–Olesker-Taylor (2021), Hermon–Huang
(2024), Huang–Rao (2025). GitHub returned zero repositories. arXiv's general
query returned 48 entries through October 2026; abstracts were inspected,
with primary PDFs fetched for the most relevant results. Crossref's two
keyword searches were noisy; title, author, DOI and publication metadata
were inspected, and the Abelian paper's precise publication was fetched by DOI.

## Relevant references and why they do not resolve the full question

1. Martin Hildebrand, “A survey of results on random random walks on finite
   groups,” Probability Surveys 2 (2005), 33–63; arXiv:math/0401189.
   Direct PDF fetched. Foundational survey covering distinct models and regimes.
2. László Babai, Robert Beals and Ákos Seress, “On the diameter of the symmetric
   group: polynomial bounds,” Proceedings of the Fifteenth Annual ACM–SIAM
   Symposium on Discrete Algorithms (2004), 1108–1112. Exact source reference
   [4], not itself a theorem of sharp general-group mixing.
3. Noga Alon and Yuval Roichman, “Random Cayley graphs and expanders,” Random
   Structures & Algorithms 5(2) (1994), 271–284; DOI 10.1002/rsa.3240050203.
   Crossref verified title/authors/DOI. Logarithmic-generator expansion is
   classical, preceding the source, and does not specify sharp mixing or cutoff
   for all generator regimes. Theorem 1 in ATTEMPT.md is an elementary,
   nonoptimal-constant proof of this phenomenon, not a new full resolution.
4. Demetres Christofides and Klas Markström, “Expansion properties of random
   Cayley graphs and vertex transitive graphs via matrix martingales,” Random
   Structures & Algorithms (2008); DOI 10.1002/rsa.20177 (online 2007).
   Matrix concentration improves expansion estimates; keyword metadata
   located through Crossref, not a full-resolution theorem read in this run.
5. Emmanuel Breuillard, Ben Green, Robert Guralnick and Terence Tao,
   “Expansion in finite simple groups of Lie type,” arXiv:1309.1975.
   Direct PDF, Theorem 1.2, PDF page 3: random pairs are expanding with
   probability at least 1-C|G|^(-delta), with constants depending only on rank.
   Provides logarithmic mixing for bounded-rank Lie-type simple groups;
   does not cover all finite groups, unbounded rank, or alternating groups.
6. Jonathan Hermon and Sam Olesker-Taylor, “Cutoff for almost all random walks
   on Abelian groups,” Journal of the European Mathematical Society 28(5)
   (2026), 1913–1977; DOI 10.4171/JEMS/1743; arXiv:2102.02809v2.
   Publication metadata verified via Crossref. Direct PDF, Theorem A,
   PDF page 4: Abelian G, 1<<k≲log|G| and k-d(G)>>1 imply cutoff at
   an entropic time tau_*; under further conditions that time depends
   only on k and |G|. Continuous-time model (page 3), with directed and
   undirected versions. The phrase “affirmative answer” in the text is
   explicitly **for Abelian groups**, not arbitrary groups.
7. Jonathan Hermon and Sam Olesker-Taylor, “Cutoff for random walks on upper
   triangular matrices,” arXiv:1911.02974v2 (2019, revised).
   Direct PDF. Structured nilpotent matrix families and Heisenberg groups.
   Abstract explains that k and |G| alone need not determine the cutoff time;
   the abelianization also matters. This refutes a group-independent-time
   universality strengthening in some regimes, not the broad question.
8. Jonathan Hermon and Sam Olesker-Taylor, “Further results and discussions
   on random Cayley graphs,” arXiv:1911.02975v2. Direct PDF.
   Supplements the Abelian and matrix-group results, including generation
   criteria and absence of cutoff at bounded degree. A lead, not a general
   solution.
9. Jonathan Hermon and Xiangying Huang, “Cutoff for random Cayley graphs of
   nilpotent groups,” arXiv:2403.12355v1 (19 March 2024).
   Direct PDF. Theorem 1, PDF page 6, assumes nilpotent G with bounded
   rank and nilpotency class and 1<<log k<<log|G|, and gives cutoff at
   max{t_0(k,|G_ab|), log_k|G|}. Theorem 2, PDF page 7, reduces some
   sparse deterministic-generator walks to abelianization. Continuous time,
   explicitly defined on page 5. Nilpotence and bounded structural
   parameters exclude arbitrary finite groups.
10. Xiangying Huang and Renyu Rao, “Cutoff for random walks on dihedral
    groups,” arXiv:2510.19942v1 (22 October 2025). Direct PDF.
    Theorem 1.3, PDF page 3, assumes dihedral groups of order 2n with
    **prime n**, diverging k, 1<<log k<<log|G| and one of two additional
    inequalities on k. Theorem 1.4, PDF page 4, covers a sequence with
    Abelian normal subgroups of uniformly bounded index when k>>log|G|.
    Abstract shorthand is broader than the first theorem's precise
    hypotheses; neither theorem covers arbitrary finite groups.
11. Demetres Christofides, Klas Markström and Christina Savvidou,
    “Diameter thresholds of random Cayley graphs,” arXiv:2605.29457v1
    (28 May 2026). Direct PDF. Theorems 1.1 and 1.2, PDF page 2,
    are uniform over arbitrary groups but concern **Bernoulli element
    inclusion** and diameter thresholds, not sharp random-walk mixing.
    This is relevant 2026 progress. Converting diameter to mixing would
    be an implication proved separately and cannot be called a solution
    in print under the user's criterion.
12. Jonathan Hermon and Sam Thomas, “Cutoff for mixing times on random
    Abelian Cayley graphs,” arXiv:1810.05130 (2018).
    Located in Semantic Scholar bulk results. Earlier Abelian-specific
    work, followed by the papers above; no general-group claim.
13. Uri Shapira and Reut Zuck, “Asymptotic metric behavior of random Cayley
    graphs of finite abelian groups,” arXiv:1607.05022v3 (2016).
    arXiv abstract inspected: fixed generator number and lattice limit
    laws for **metric** parameters of Abelian Cayley graphs, not full
    arbitrary-group mixing.
14. Daniel El-Baz and Carlo Pagano, “Diameters of random Cayley graphs of
    finite nilpotent groups,” arXiv:2002.08870v2 (2020).
    arXiv abstract inspected: bounded-rank/bounded-class nilpotent
    diameter limit laws; different observable and restricted groups.

## Positive evidence of the remaining scope

Additional directly inspected references in Hildebrand's survey:

- C. Dou and M. Hildebrand, “Enumeration and random walks on finite groups,”
  Annals of Probability 24 (1996), 987–1000.
- M. Hildebrand, “Random lazy random walks on arbitrary finite groups,”
  Journal of Theoretical Probability 14 (2001), 1019–1034.
- M. Hildebrand, “A note on various holding probabilities for random lazy
  random walks on finite groups,” Statistics & Probability Letters 56
  (2002), 199–206.
- I. Pak, “Random walks on finite groups with few random generators,”
  Electronic Journal of Probability 4 (1999), 1–11.
- Y. Roichman, “On random random walks,” Annals of Probability 24 (1996),
  1001–1011.

Hildebrand's survey, Section 4.5, Theorems 12 and 13, already supplies
uniform upper bounds for a lazy model at logarithmically many generators.
Consequently the elementary logarithmic-generator bound in ATTEMPT.md
is not evidence of new progress on the sharp arbitrary-group question.
These are upper bounds in a specified regime, not a theorem answering
all of Question 2's generator regimes or quantifiers.

Huang–Rao (2025), PDF page 1, explicitly labels the arbitrary-group cutoff
assertion (for log|G|<<k and log k<<log|G|) as “Conjecture 1 (Aldous and
Diaconis, 1985)”. This is positive evidence that its restricted main theorems
do not settle that conjecture as of that text; it is not a claim that no
later solution can exist. The arXiv query also found 2026 diameter and
combinatorial papers, with no matching all-group mixing theorem.

## Read-only prior-work and brain queries

- `brain.py recall "random Cayley graph mixing mistakes"`.
- `brain.py recall "random random walk general finite group"`.
- `math_recall.py "Alon Roichman random Cayley mixing Hildebrand"`.
  These keyword recalls mainly returned neighboring work. Nothing was
  accepted as proof. No remember or other intentional brain-write command
  was issued. The first permitted recall command itself reported an
  automatic detached index refresh; this was an internal utility side
  effect, not a research output or a service started by this worker.
- `rg` on the specified intake ledgers found E0093-A001 (2026-09-08).
  Its assertion that expansion alone yields cutoff at the diameter, and
  its polynomial-in-log-size fixed-generator Abelian mixing description,
  are not valid general conclusions. ATTEMPT.md supplies corrected proofs.
- `git ls-tree` and `git show origin/master:research7_2026-09-17/R7-01/admission/2026-09-19T211100Z__E0093_scope_and_pair_mixing_gate.md`
  read an earlier admission screen. It already identified the broad source
  scope and the distinct alternating-group conjecture. No repository
  working tree was changed. The note is a lead, not a theorem or an instruction.

No paper is marked as solving E0093 in print. No line-by-line application of
a matching theorem is possible from the located literature.

## Second-attempt gap search and neighbouring theorem, 2026-10-12

The second attempt specifically targeted **sparse pairs**, normal subgroup
fibers, and quotient mixing, rather than repeating the logarithmic-degree
concentration proof.

- `math_recall.py "random Cayley sparse generators mixing nilpotent quotient
  abelianization Hermon Huang Hildebrand"` returned mostly off-target Ising
  cards. They supplied no usable result.
- `math_recall.py "normal subgroup quotient Cayley spectral gap"` returned
  elementary quotient/normal-subgroup cards and finite-quotient approximation
  cards, not a theorem closing the mixing gap. Full output is saved in
  brain_gap_recall.txt. The quotient-group card
  claim_c7b71f49c893bfea5d33761660ef7b69acd4b1757b42864f27f765552c2d2f8b
  reminded us of the normality hypothesis, which was checked independently.
- arXiv API: `all:"random walks" AND all:"bounded index"`, max_results=30,
  https://export.arxiv.org/api/query?search_query=all%3A%22random%20walks%22%20AND%20all%3A%22bounded%20index%22&max_results=30
  — HTTP 200, zero entries. This literal query is narrow and its absence
  of results supplies no novelty or openness evidence.
- Crossref: `random walks symmetric cyclic direct product random generators`,
  rows=15,
  https://api.crossref.org/works?query=random%20walks%20symmetric%20cyclic%20direct%20product%20random%20generators&rows=15
  — HTTP 200. Relevant lead: Pak's paper, DOI 10.1214/ejp.v4-38,
  already listed above. Also found “Random walks on the torus with several
  generators,” DOI 10.1002/rsa.20029, a neighboring Fourier/Diophantine model;
  no full-text theorem from it is used. Exact raw results and logs are saved.
  A prior shell one-liner for these queries failed at Python parsing before
  making requests; second_literature.py is the corrected executed script.
- Direct reread of the already downloaded Hermon–Huang paper:
  Lemma 3.2 and Remark 5, PDF pages 19–20, compare identity-start and
  subgroup-uniform-start laws using relative diameter. This motivated
  approach A. SECOND_ATTEMPT.md gives its own half-lazy discrete-time
  projection/Dirichlet-form proof with a sqrt(|G|-|G/N|) prefactor and a
  precise normal-subgroup assumption. It does not rely on a printed
  equality between a norm deficit and a Dirichlet form for arbitrary
  functions; the spectral argument is instead applied to eigenvectors.

The resulting S_3 x C_p random-pair theorem is an independently proved
special case, not a theorem claimed to solve E0093 in print. Fixed-generator
Abelian rates and subgroup comparison mechanisms are established themes;
no novelty claim is made for the special-case construction or its proof.

Crossref metadata gives the second-query references precisely as:

- Igor Pak, “Random walks on finite groups with few random generators,”
  Electronic Journal of Probability 4 (1999), DOI 10.1214/ejp.v4-38
  (the survey gives pages 1–11).
- Timothy Prescott and Francis Edward Su, “Random walks on the torus with
  several generators,” Random Structures & Algorithms 25(3) (2004),
  336–345, DOI 10.1002/rsa.20029.

The second theorem does not use either paper as an unverified premise.
