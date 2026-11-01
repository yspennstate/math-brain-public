from pathlib import Path
import json, xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent
lit='''# Literature and status check — 2026-10-12

No exact solution in print was identified in the accessible bounded search.
This is not an exhaustive assertion of current open status. API restrictions,
search ranking and indexing coverage limit this check. No theorem is designated
SOLVED_IN_LITERATURE.

## Verified source and correction to intake locator

Roland Bauerschmidt, Hugo Duminil-Copin, Jesse Goodman and Gordon Slade,
Lectures on Self-Avoiding Walks, arXiv:1206.2092v1, 11 June 2012.
https://arxiv.org/pdf/1206.2092 (HTTP 200; source.pdf and source.txt).
The relevant section is **1.4, 1/d expansion**, printed/PDF pp. 4-5,
equation (1.19), not Section 1.5. The hypothesis is nearest-neighbour strictly
self-avoiding walk on Z^d, d an integer tending to infinity. Its expansion
exists to every fixed order, has integer coefficients indexed from -1,
and has an error constant allowed to depend on the truncation order.

Exact source sentence, across pp. 4-5:
> It is expected, though not proved, that the asymptotic series in (1.19) has radius of convergence 0, so that the right-hand side of (1.19) diverges for each fixed d.

This is an open assertion, not a theorem proving the requested conclusion.

## Relevant papers checked

* T. Hara and G. Slade, The self-avoiding-walk and percolation critical points
  in high dimensions, Combinatorics, Probability and Computing 4 (1995),
  197-215. Source reference [35]. Establishes the all-orders asymptotic expansion
  according to the fetched lectures. Not a proof of zero radius; original paper
  was not independently fetched in this session.
* N. Clisby, R. Liang and G. Slade, Self-avoiding walk enumeration via the lace
  expansion, Journal of Physics A: Mathematical and Theoretical 40 (2007),
  10973-11017. Source reference [21]. Computed finite coefficients. Exact title
  arXiv API query returned no entries. No factorial LOWER bound is established
  by the finite data, and the paper itself was not fetched.
* B. T. Graham, Borel-type bounds for the self-avoiding walk connective constant,
  Journal of Physics A: Mathematical and Theoretical 43 (2010), 235001,
  doi:10.1088/1751-8113/43/23/235001; arXiv:0911.5163v1.
  https://arxiv.org/pdf/0911.5163 (HTTP 200; graham.pdf, graham.txt).
  Theorem 1.1, p. 2, proves factorial remainder UPPER bounds, and Lemma 4.1,
  p. 5, proves |alpha_n| <= C_2^n n!. Neither proves divergence. Equation (3.2)
  and Lemma 3.3, pp. 4-5, give the signed formal recursion and finite-memory
  stabilization used in ATTEMPT.md. Page 3 notes alpha_12 and alpha_13 are
  negative, although alpha_1 through alpha_11 are positive. Thus a positivity
  assumption for the full reciprocal coefficient sequence is already false.
* Gordon Slade, Self-avoiding walk on the hypercube, arXiv:2108.03682v2,
  13 May 2022. https://arxiv.org/pdf/2108.03682 (HTTP 200; hypercube.pdf,
  hypercube.txt). The hypercube itself is a different object. The discussion
  on p. 6 explicitly includes the Z^d series preceding it:
  > We believe that these series and also the series for the hypercube in Theorem 1.3 have radius of convergence zero but are Borel summable; to prove any of these statements is an open problem.
  This is later support for open status as of that version, not a solution.
* P. R. Gerber and M. E. Fisher, Critical temperatures of classical n-vector
  models on hypercubic lattices, Physical Review B 10 (1974), 4697-4703.
  Graham and Slade cite divergence for the spherical model. Different model;
  recorded as a lead, not an answer for SAW. Original paper not fetched.
* T. Hara, G. Slade and A. D. Sokal, New lower bounds on the self-avoiding-walk
  connective constant, Journal of Statistical Physics 72 (1993), 479-517,
  arXiv:hep-lat/9302003 (author metadata in arxiv.response); Crossref DOI
  10.1007/BF01048021. Loop-erasure bounds matching finitely many 1/d terms are
  a possible comparison lead; no all-orders signed coefficient bound follows.

## Earlier work and brain, read-only

Read the intake C0097-A001 (2026-09-07): factorial-counting heuristics stalled
on signed cancellation. Read origin/master:probability_campaigns/codex_pool_2026-10-10/team_O/w330/reports/C0097_finite_coefficients.md
with git show. It proves a finite-prefix information obstruction; it does not
solve the expansion problem. The repository working tree was not changed.
Ran math_recall.py with "connective constant expansion Graham" and brain.py
recall with "connective constant expansion mistakes". Relevant returned hints
were checked against the source. Unrelated memories were not used. No remember
or explicit store mutation command was issued.

## Every web search and fetch

The following exact URLs and outcomes supplement the raw .response files.
All requests used Python requests from the shell. No built-in web search.
The initial eight searches were repeated once when followup.py imported
search.py; this is a duplicate execution, not additional coverage.
'''
for f in ['search_log.json','followup_log.json','citing_search_log.json']:
 for q in json.loads((P/f).read_text(encoding='utf-8')):
  lit+='\n* 2026-10-12 '+q['service']+': '+q.get('url','(URL unavailable)')+'; HTTP '+str(q.get('status','not recorded'))
  if 'params' in q:lit+='; query parameters '+json.dumps(q['params'])
  if 'error' in q:lit+='; '+q['error']
  lit+='.'
lit+='''

The follow-up arXiv responses were valid Atom XML (saved before the script
incorrectly attempted JSON parsing); inspected with ElementTree afterwards.
The recent query returned 48 entries, including Graham but no later direct
solution. The exact Clisby title query returned zero entries. The primary
query returned 17 entries. Full returned metadata is retained in the XML files.
Counts are checked below rather than inferred from requested page sizes.

The Semantic Scholar search endpoint returned HTTP 429, but the separate
ARXIV:1206.2092/citations endpoint returned HTTP 200 and 96 citation records,
with next=null. All returned titles were screened, and available abstracts
were screened for Borel, 1/d, expansion, divergence and connective-constant
terms; citation_titles.txt and semantic_citing.response retain the records.
No direct solution was identified in those metadata. Not every citing full
text was fetched.

OpenAlex returned HTTP 429 throughout, including the requested works-citing
query. Its assumed DOI locator 10.1090/cmp/015/03 could not be resolved and
is NOT asserted here as the source's verified DOI; no usable OpenAlex citation
search was completed. The Crossref source-title query returned irrelevant
items and did not verify that DOI. The general Crossref query also ranked
mostly irrelevant works; the targeted query returned Graham and other
connective-constant bounds, with no exact solution identified.

Direct PDF fetches: https://arxiv.org/pdf/1206.2092,
https://arxiv.org/pdf/0911.5163, https://arxiv.org/pdf/2108.03682; each HTTP 200.
'''
ns={'a':'http://www.w3.org/2005/Atom'}
lit+='\nVerified Atom entry counts:\n'
for f in ['arxiv.response','arxiv_recent.response','arxiv_clisby.response']:
 r=ET.fromstring((P/f).read_text(encoding='utf-8'));lit+='* '+f+': '+str(len(r.findall('a:entry',ns)))+' entries.\n'
(P/'LITERATURE.md').write_text(lit,encoding='utf-8')
claims=[
 {'claim':'For every fixed finite memory tau, the normalized connective constant mu_tau(d)/(2d) agrees for large integer d with a complex analytic germ at x=1/(2d)=0.','status':'proved_special_case','proof_location':'ATTEMPT.md Proposition 1','remaining_gap':'No uniform radius in tau, and no implication of divergence for infinite memory.','checks':'Exact canonical state reset for tau=1..6; characteristic polynomials for tau=1..4; independent d=4,tau=4,n=6 concrete count.'},
 {'claim':'Zero radius of the SAW connective-constant Laurent tail is equivalent to zero radius of its formal reciprocal critical-point series.','status':'proved','proof_location':'ATTEMPT.md Proposition 2','remaining_gap':'Neither zero-radius statement is proved.','checks':'Analytic reciprocal in both directions with nonzero constant term; shifts by x handled explicitly.'},
 {'claim':'Graham\'s equation gives h_n=S_n+R_n, with R_n depending only on earlier coefficients; coefficients through h_n stabilize once tau>=2n.','status':'proved','proof_location':'ATTEMPT.md Proposition 2 (using cited Graham equation and stabilization)','remaining_gap':'No superexponential lower bound for the signed aggregate.','checks':'Coefficient extraction and induction; checked against Graham equation (3.2) and Lemma 3.3, pp.4-5.'},
 {'claim':'The paired-axis return coefficient at order five is -195, although its diagonal contribution is +945.','status':'proved_special_case','proof_location':'ATTEMPT.md auxiliary return counts; FiniteChecks.lean','remaining_gap':'This is an auxiliary random-walk class, not SAW connective-constant coefficients.','checks':'Exact symbolic expansion through order20; independent counting formula and finite algebra identity.'},
 {'claim':'The infinite-memory SAW connective-constant expansion has zero radius of convergence.','status':'conjecture','proof_location':'LITERATURE.md verified source; ATTEMPT.md Remaining gap','remaining_gap':'A lower bound forcing limsup |h_n|^(1/n)=infinity remains missing.','checks':'Bounded literature check found no exact solution; factorial upper bounds and finite computations do not prove the claim.'}
]
with (P/'CLAIMS.jsonl').open('w',encoding='utf-8') as f:
 for c in claims:c={'problem_id':'C0097',**c};f.write(json.dumps(c,ensure_ascii=False)+'\n')
print('Saved literature and',len(claims),'claims')
