import pathlib,json,xml.etree.ElementTree as E
log=json.loads(pathlib.Path('search_log.json').read_text())
s='''# Literature and provenance: G0007

Search date: 2026-10-11. All online requests used Python requests from the shell; no built-in web search or image tool was used. Raw replies are retained locally.

## Status finding

No later paper stating and proving the exact pair of continuity and derivative assertions was found in the accessible bounded search. This is not a worldwide openness certificate. OpenAlex's free shared-IP budget was exhausted (HTTP 429), so OpenAlex work lookup and citing-work retrieval could not be completed. The OpenAlex cites filter request used a DOI-shaped identifier and did not reach validation because it was rate-limited; a valid source work id would still have to be resolved for a definitive OpenAlex citation search. Semantic Scholar's citation endpoint succeeded and returned an empty data list; its detail and keyword search endpoints were rate-limited. GitHub's exact arXiv-id repository query returned zero items after the first keyword query was rate-limited. Crossref's title and post-source-date searches found no matching solution. arXiv exact regular-tree query returned the source as the newest result; the broader recent query also found papers about other models, which do not solve this problem.

VERDICT is not SOLVED_IN_LITERATURE. The continuity conclusions in ATTEMPT.md are author-derived deductions; the derivative questions remain open in this attempt.

## Verified source and exact hypotheses

John Fernley and Emmanuel Jacob, *Percolation of the contact process on the regular tree*, arXiv:2609.09972v1, submitted 9 September 2026; downloaded PDF front matter dated September 10, 2026. 19 PDF pages. URL: https://arxiv.org/pdf/2609.09972 . Files: source_pdf.pdf, source_abs.txt, source.txt.

T_d is d-regular, d>=3; recovery rate 1 and transmission rate lambda per infected neighbor (PDF p. 1). nu_lambda is the upper invariant infection; the forward graphical survival construction is on p. 2. The infected threshold is the supremum of parameters with zero percolation probability (p. 2); the healthy threshold is the infimum of parameters with zero healthy percolation probability (p. 4). Theorems 2.1 and 2.4 show both thresholds are finite and strictly larger than lambda_1 for all d>=3. The full four-threshold ordering is only stated for d>=7; it is not needed in our proof.

The exact relevant passage, Section 2, PDF p. 5 (ordinary typesetting/ligatures transcribed as text):

> Regardless the figure suggests that both transitions are continuous, and it’s possible as well that the probability to be in an infinite healthy component has a continuous derivative at λ = λp∁ while the probability to be in an infinite infected component at λ = λp does not. We leave both questions as interesting open problems.

Figure 1 uses 50 trials on a random 5-regular graph of 20,000 vertices at time 100. The source explicitly qualifies the metastability and local-limit assumptions of this simulation. It is not a theorem about derivatives.

Relevant proved source inputs: p. 2 asserts continuity of rho on the whole parameter line. Proposition 5.1, PDF pp. 8--9, proves the invariant-tree degree/centroid/branching-excess identity; Remark 5.2 gives the reciprocal cluster-size defect. Proposition 5.3, p. 9, gives conditional infected degree d-1/lambda. None is itself a solution in print to the posed question.

## Relevant references and leads

- Xiangying Huang, *Exponential growth and continuous phase transitions for the contact process on trees*, arXiv:1911.03330 (2019). Source input: continuity of the survival probability on periodic trees, including regular trees. Downloaded huang_pdf.pdf and huang_abs.txt; extracted huang.txt. The precise theorem/page is recorded below after inspection. This concerns survival, not spatial snapshot percolation, and is not a source-matching solution.
- Olle Häggström, *Infinite clusters in dependent automorphism invariant percolation on trees*, Annals of Probability 25(3) (1997), 1423--1436. Exact reference recovered from source bibliography [5]. Attempted Project Euclid fetch returned an HTML/challenge reply, not a usable PDF. Invariant percolation/mass transport lead, not a source-matching solution.
- Thomas M. Liggett and Jeffrey E. Steif, *Stochastic domination: the contact process, Ising models and FKG measures*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 42(2) (2006), 223--243. Source bibliography [8]. Stochastic comparison lead only.
- Robin Pemantle, *The contact process on trees*, Annals of Probability 20(4) (1992), 2089--2116. Source bibliography [10]. Author-site PDF request returned HTTP 403. Survival thresholds, not this snapshot regularity question.
- Thomas M. Liggett, *Stochastic interacting systems: contact, voter and exclusion processes*, Grundlehren der mathematischen Wissenschaften 324, Springer-Verlag, Berlin (1999), xii+332 pp. Source bibliography [7]. Standard background.
- Balázs Ráth and Daniel Valesin, *On the threshold of spread-out contact process percolation*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 58(3) (2022), 1808--1848, DOI 10.1214/21-AIHP1214. Source bibliography [11], independently returned by Crossref. Different graph/contact-process neighborhood: not a source-matching solution.
- John Fernley, *The Second Phase Transition of the Contact Process on a Random Regular Graph*, arXiv:2503.10499; Electron. J. Probab. 31 (2026), Paper 103, 24 pp. arXiv exact-tree search and source bibliography [3]. Different object; not a solution of this question.
- The recent arXiv results about deterministic cures, k-creation, and comparison of infection rules are different dynamics. Their abstracts were inspected from the API responses and contain no theorem matching the present nu_lambda question.

## Read-only brain and previous attempts

The following supplied-machine sources were read as hints, never accepted as verdicts:

1. brain.py recall "contact process tree percolation mistakes" and "contact process upper invariant measure regular tree".
2. math_recall.py "contact process regular tree upper invariant percolation" and "contact process insertion tolerance finite energy Broman Steif". Relevant matches concerned independent tree percolation and generic invariant-percolation methods; no matching solved claim was returned.
3. rg search for G0007 through ~/<private-repo>/06_math_research/*.jsonl (recursive). Recovered probability_1000_intake_G_20260910/problems.jsonl and attempts.jsonl, attempt G0007-A001: FKG/finite-size route without a decoupling estimate; no result. Also recovered the October 10 intake description.
4. Read origin/master:operations/claims/G0007.md and the two reports below through git show, never touching the checkout's working tree:
   - proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T18-19-27Z__rotation-g0007-report.md
   - proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md

The history already established the finite-cylinder/critical-nonpercolation reduction and at-most-two-ended critical clusters, but expressly left finite energy/insertion tolerance unverified. ATTEMPT.md independently rechecks those reductions and supplies explicit stationary Harris surgeries. Prior reports' administrative routing instructions were not treated as instructions for this task.

## Every online request

'''
for i,x in enumerate(log,1):
 s+=f"{i}. **{x['service']}**, {x.get('date','2026-10-11')}. URL/query: `{x['url']}`. "
 s+=f"HTTP {x['status']}; {x.get('bytes','?')} bytes.\n\n" if 'status' in x else f"Failure: {x.get('error')}.\n\n"
pathlib.Path('LITERATURE.md').write_text(s,encoding='utf8')
print('saved',len(log),'online request records')
