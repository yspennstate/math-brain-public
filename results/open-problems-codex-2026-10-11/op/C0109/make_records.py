import json, pathlib, xml.etree.ElementTree as E
R=pathlib.Path(__file__).parent
if (R/'DIRECT_UPPER.md').exists():
 raise SystemExit('First-pass recorder retained for provenance; use update_second_records.py to preserve second-pass claims.')
logs=[]
for file in ['search_log.json','search_log_extra.json','search_log_third.json','search_log_fourth.json','search_log_fifth.json']:
 logs+=json.loads((R/file).read_text())
header='''# C0109 literature status — 2026-10-11

No exact solution in print was verified. This is a bounded search, not a
proof of absence. OpenAlex and Semantic Scholar returned HTTP 429 on all
attempts, limiting citation coverage. No SOLVED_IN_LITERATURE verdict.

## Exact source

Terence Tao and Van Vu, “From the Littlewood-Offord problem to the
Circular Law: Universality of the spectral distribution of random matrices,”
Bulletin of the AMS 46 (2009), 377–396, DOI
10.1090/S0273-0979-09-01252-X; arXiv:0810.2994v3 (1 January 2009).
Section 6, PDF/printed p.22:

> Circular Law. A natural question here is to investigate the rate of convergence. In [54], we observed that under the extra assumption that the (2 + ε)-moment of the entries are bounded, we can have rate of convergence of order n−δ, for some positive constant δ depending on ε. The exact dependence between ε and δ is not clear.

The surrounding model (pp.1–3) is iid entries with one fixed law, mean
zero, unit variance, normalized by n^(-1/2). No bounded density is assumed.
The intake's “optimal rate” phrase is a paraphrase, not a verbatim quote.

[54] Terence Tao and Van Vu, “Random matrices: The circular law,”
Communications in Contemporary Mathematics 10 (2008), 261–307,
DOI 10.1142/S0219199708002788, arXiv:0708.2895v5. Its p.4 states:

> One can obtain some quantitative estimates on the rate of convergence as well. For example, under the (2 + η)th moment assumption, we can show that almost surely, the distance sup_{s,t} |μ_n(s, t) − μ_∞(s, t)| between μ_n and the limiting distribution μ_∞ in the uniform metric is at most n^{−η′} for some constant η′ > 0 and all sufficiently large n.

Subscripts/superscripts are transcribed into readable notation from the PDF.
This identifies random-ESD almost-sure eventual rectangle discrepancy.
Sections 13–14 discuss refinements, not a sharp dependence.

## Relevant later papers and scope

1. Friedrich Götze and Jonas Jalowy, “Rate of convergence to the Circular
   Law via smoothing inequalities for log-potentials,” Random Matrices:
   Theory and Applications 10 (2021), 2150026,
   DOI 10.1142/S201032632150026X; arXiv:1807.00489v3, 9 April 2021.
   Definition 2(A), p.4: centered variance-one independent entries, all
   absolute moments finite. Theorems 6 and 7, p.6: ball and rectangle
   discrepancy <=n^(-1/2+eta) with failure <=n^(-Q), for every eta,Q>0
   and sufficiently large n. These are inputs for EACH FIXED finite-past
   law in ATTEMPT.md. They do not assert this under only (2+eps)-moments.
   Theorem 8 excludes the edge and uses 4+delta moments: different scope.

2. Jonas Jalowy, “The Wasserstein distance to the circular law,” Annales
   de l'Institut Henri Poincaré, Probabilités et Statistiques 59 (2023),
   2285–2307, DOI 10.1214/22-AIHP1317; arXiv:2111.03595v3,
   28 October 2022. Theorem 1, p.2 gives W_1 <=n^(-1/2+eta) with failure
   <=n^(-Q) under ALL moments. Theorem 3, p.3 gives expected Ginibre
   W_1 <=4/sqrt(n). Lemma 5, p.4 is a geometric quantization bound.
   Stronger-moment/Gaussian cases do not answer the weak-moment question.

3. Friedrich Götze and Alexander Tikhomirov, “The circular law for random
   matrices,” Annals of Probability 38 (2010), 1444–1491,
   DOI 10.1214/09-AOP522; arXiv:0709.3995v4. Fetched PDF.
   Finite moments above two; circular-law convergence, not a verified
   theorem giving the optimal eps-dependent rate. Lead, not a solution.

4. Friedrich Götze, Alexey Naumov, Alexander Tikhomirov, “On local laws
   for non-Hermitian random matrices and their products,” Random Matrices:
   Theory and Applications 9 (2020), 2050004; arXiv:1708.06950v2.
   API abstract explicitly assumes finite (4+delta)-moment. Local law on
   optimal scale with logarithmic factors. Abstract-level lead only.

5. Elizabeth S. Meckes and Mark W. Meckes, “A rate of convergence for the
   circular law for the complex Ginibre ensemble,” Annales de la Faculté
   des Sciences de Toulouse 24 (2015), 93–117,
   DOI 10.5802/afst.1443; arXiv:1406.1396v3. Ginibre Wasserstein rates;
   Gaussian special case; API/Crossref lead only.

6. Terence Tao and Van Vu (appendix by Manjunath Krishnapur), “Random
   matrices: Universality of ESDs and the circular law,” Annals of
   Probability 38 (2010), 2023–2065, DOI 10.1214/10-AOP534.
   Qualitative finite-second-moment universality differs from a sharp
   polynomial rate. Brain bibliographic lead, not newly fetched.

Recent arXiv rate-query results were inspected: band matrices,
spectral-radius results, and a 2026 spectral-properties thesis concern
other models/statistics or local laws. No matching theorem was verified.
GitHub yielded rkw0k/Random-Matrix-Theory, an examples repository.

## Search receipts (Python urllib from shell)

'''
for x in logs:
 header+=f"- Date {x['date']}; service `{x['service']}`; query/URL `{x['url']}`; result: {x['status']}"+(f"; {x['bytes']} bytes saved." if 'bytes' in x else '.')+'\n\n'
header+='''The OpenAlex citation lookup could not be completed: the source DOI
lookup returned 429, preventing resolution to a work ID. A tentative
DOI-based cites-filter request also returned 429; it is NOT treated as
a successful or validated citing-works search. Semantic Scholar's source
and citations request also returned 429. No absence conclusion follows.

## Read-only brain and prior attempts

Ran math_recall.py “circular law rate truncation”; brain.py recall
“circular law mistakes” and “random matrices circular law”. Searched
intake/codex-pool ledgers for C0109 and read team_O/w335/C0109_proof.md.
These distinguish scalar tail bounds from spectral lower bounds and
warn against nonnormal rank/n perturbation arguments. The earlier
“caps delta” statement was not accepted as a proof.
Read-only origin/master listing with scoped *C0109* and *circular*
patterns returned no matching paths. No repository was changed.

## Search result inventories
'''
ns={'a':'http://www.w3.org/2005/Atom'}
for file in ['arxiv.xml','arxiv_recent.json','arxiv_weak.json']:
 header+='\n### '+file+'\n\n'
 for e in E.parse(R/file).findall('a:entry',ns):
  title=' '.join(e.find('a:title',ns).text.split())
  header+='- '+title+'; '+e.find('a:id',ns).text+'\n'
(R/'LITERATURE.md').write_text(header,encoding='utf8')
claims=[
 {'problem_id':'C0109','claim':'Under finite second moment alone there is one fixed normalized real law with no finite higher moment, whose rectangle discrepancy defeats every positive polynomial exponent almost surely along a subsequence.','status':'proved','proof_location':'ATTEMPT.md, Boundary eps=0','remaining_gap':'Boundary case only; does not satisfy any positive-eps moment assumption.','checks':'Explicit p=2 specialization of the induction; conditional Jensen proves failure of all higher moments.'},
 {'problem_id':'C0109','claim':'For every 0<eps<2/3 a single centered variance-one real law with finite (2+eps)-moment has a deterministic subsequence on which n^delta d_K diverges almost surely for every delta>2eps/(2+eps).','status':'proved','proof_location':'ATTEMPT.md, Proposition and complete construction','remaining_gap':'No matching upper bound or optimal dependence; uses published Götze–Jalowy Theorem 7. Not a full C0109 solution.','checks':'Fixed-law induction; n^2 union bound; L^p convergence; fixed rectangle; Borel–Cantelli; rational windows and numerical separation checks.'},
 {'problem_id':'C0109','claim':'The same law has analogous lower obstructions for W_1, ball discrepancy and bounded-Lipschitz discrepancy.','status':'proved','proof_location':'ATTEMPT.md, Ball discrepancy and W_1 versions','remaining_gap':'No matching weak-moment upper rates. Also uses Jalowy Theorem 1.','checks':'Fixed radial test, scaling, layer cake, simultaneous thresholds.'},
 {'problem_id':'C0109','claim':'Every measure on at most n points has W_1 distance at least 2/(3sqrt(n)) from uniform measure on the unit disk.','status':'proved','proof_location':'ATTEMPT.md, Other checked special case','remaining_gap':'Wasserstein only, not Kolmogorov.','checks':'Union-of-disks area and layer-cake integral.'},
 {'problem_id':'C0109','claim':'Complex Ginibre has optimal exponent 1/2 for expected W_1 discrepancy.','status':'proved_special_case','proof_location':'ATTEMPT.md, Other checked special case; LITERATURE.md, Jalowy Theorem 3','remaining_gap':'Gaussian special case only.','checks':'Published upper bound and deterministic geometric lower bound.'},
 {'problem_id':'C0109','claim':'Auxiliary exponent windows, rectangle separation and finite eigenvalue scaling pass the recorded checks.','status':'numerical_evidence','proof_location':'checks.py and checks.json','remaining_gap':'Does not verify infinite stochastic construction or published input.','checks':'21 rational windows; 1000 radii; 18 Gaussian matrices sizes 48,96,192; residual <1e-9.'}
]
(R/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
print('Saved LITERATURE.md and CLAIMS.jsonl')
