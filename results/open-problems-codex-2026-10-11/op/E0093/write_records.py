import json,pathlib
R=pathlib.Path(__file__).resolve().parent
logs=[]
for f in ['search_log.json','followup_log.json','final_fetch_log.json']:
    logs.extend(json.loads((R/f).read_text(encoding='utf-8')))
body='''# E0093 literature record — 2026-10-12

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

'''
for x in logs:
    result=('HTTP '+str(x['status'])+', '+str(x['bytes'])+' bytes') if 'status' in x else x['error']
    body+=f"- {x['date']} `{x['name']}`: {x['url']} — {result}.\n"
body+='''
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
'''
(R/'LITERATURE.md').write_text(body,encoding='utf-8')
claims=[
 {'claim':'For iid uniform k-tuples on every group of order n, the symmetric walk restricted norm obeys Pr(||A||>=a)<= (n-1)m m^(2m)/(m! k^m a^(2m)) for integers k>=m>=1; hence k>=ceil(16e ceil(2 log n)) gives O(log n) mixing with high probability.', 'status':'proved','proof_location':'ATTEMPT.md, Theorem 1','remaining_gap':'Nonoptimal bound; no sharp all-group rate or cutoff, and no sparse-generator answer.','checks':'Complete trace-moment proof; exhaustive tuple evaluation on S3 in checks.py/checks.json; no claim of full Lean formalization.'},
 {'claim':'For k iid uniform elements of F_2^d, k>=d, conditioned on spanning, the nonlazy walk has period two with probability (2^d-1)/(2^k-1).','status':'proved_special_case','proof_location':'ATTEMPT.md, Theorem 2','remaining_gap':'General finite groups and aperiodic sparse-generator mixing remain unresolved.','checks':'Exhaustive integer enumeration for d<=3, k<=5 in checks.json; finite Lean checks recorded separately after verification.'},
 {'claim':'Conditioned random bases of F_2^d give a deterministic lazy-walk TV profile with cutoff at (d/2) log d and window at most order d.','status':'proved_special_case','proof_location':'ATTEMPT.md, Theorem 3','remaining_gap':'Classical special case, not arbitrary random-generator count or arbitrary group.','checks':'Complete Fourier/Chebyshev proof; lumped TV recursion for d=16,64,256 checks both inequalities.'},
 {'claim':'A single uniform generator conditioned to generate C_n gives lazy symmetric mixing time Theta(n^2) at threshold 1/4.','status':'proved_special_case','proof_location':'ATTEMPT.md, Theorem 4','remaining_gap':'Only the cyclic one-generator boundary case; no full general-group answer.','checks':'Full character calculation and explicit upper/lower estimates; numerical cycle check to be recorded separately.'}
]
with (R/'CLAIMS.jsonl').open('w',encoding='utf-8') as f:
    for c in claims:
        c={'problem_id':'E0093',**c}
        f.write(json.dumps(c,ensure_ascii=False)+'\n')
print('Wrote LITERATURE.md and CLAIMS.jsonl')
