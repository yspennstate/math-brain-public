from pathlib import Path
import json,xml.etree.ElementTree as E
R=Path(__file__).resolve().parent
intro='''# C0020 literature and source audit — 2026-10-12

Status: NO EXACT LITERATURE SOLUTION IDENTIFIED. This is a bounded search, not a proof of absence. OpenAlex citation retrieval and Semantic Scholar keyword search were rate-limited, so the coverage is explicitly incomplete. The source and the closely relevant 2024 paper were read in full at the relevant passages.

## Source and exact statement

Christophe Garban and Jeffrey E. Steif, *Noise sensitivity of Boolean functions and percolation*, arXiv:1102.5761v3, 29 May 2012. Later book: Cambridge University Press, 2014, DOI 10.1017/CBO9781139924160.
Downloaded PDF: source_pdf.pdf; extracted text: source.txt. Page numbers below distinguish the PDF page from the printed page.

Definition VIII.2 (printed 89, PDF 91):
> Given a randomized algorithm A for a Boolean function f, let C(A) (the cost of A) be the expected number of queries that the algorithm A makes. Let C(f) (the cost of f) be the infimum of C(A) over all randomized algorithms A for f.

Theorem VIII.3 (printed 87, PDF 89):
> Let f = f_n be the indicator function for the event that critical site percolation on the triangular grid contains a left to right crossing of our n × n box. Then δ_{f_n} ≤ n^{-1/4+o(1)} as n → ∞.

Open question (printed 90, PDF 92; Unicode math transcribed from the PDF):
> Open Question: Find the smallest σ such that there are algorithms A_n for f_n with C(A_n) ≤ n^σ. (We know σ ∈ [6/4, 7/4].)

The intake locator incorrectly treats p.92 as the printed page; it is the PDF page in this version. The exact exponent range refers to triangular-site critical p=1/2 percolation, not a proved exact-exponent assertion for square-bond percolation. Algorithms stop only when all completions agree (printed 83, PDF 85). This is average input-and-seed query complexity, zero error.

## Relevant papers and what they do not establish

1. Laurin Köhler-Schindler and Jeffrey E. Steif, *A study of distributional complexity measures for Boolean functions*, arXiv:2408.12995v1, 23 August 2024 (PDF manuscript dated 26 August 2024). Section 4.2, pp.24–27, discusses percolation functions. Proposition 4.6 on p.26 gives non-sharp square-bond critical bounds; Conjecture 4.7 on p.27 lists exponents including a ≤ m^(7/4+o(1)). It explicitly says, on p.27:
> Non-rigorous arguments suggest that w(f_m, π_{1/2}) behaves like m^{1.130···} and a(f_m, π_{1/2}) behaves like m^α with α ∈ [1.5, 1.6] (see [PSSW07]). Finding the exact exponents in these two cases are well-known open problems.
This is a later status lead, not a solution. The model in this example is square-bond; the accompanying discussion distinguishes triangular-site known arm exponents. The apparent 1.5–1.6 range is expressly non-rigorous and is NOT an upper bound used here. PDF stored as 2408.12995.response; text 2408.12995.txt.

2. Yuval Peres, Oded Schramm, Scott Sheffield and David B. Wilson, *Random-turn hex and other selection games*, American Mathematical Monthly 114(5) (2007), 373–387; arXiv:math/0508580v2. This predates the source and is a lead to algorithms and simulations. No theorem determining the optimal crossing-query exponent is identified. Stored as random_turn_hex.response/.txt.

3. Oded Schramm and Jeffrey E. Steif, *Quantitative noise sensitivity and exceptional times for percolation*, Annals of Mathematics (2) 171(2) (2010), 619–672; arXiv:math/0504586. This is source reference SS10b and supplies the low-revealment interface algorithm. This is the known upper-bound source, not a later solution.

4. Ryan O'Donnell and Rocco A. Servedio, *Learning monotone decision trees in polynomial time*, SIAM Journal on Computing 37(3) (2007), 827–844. The notes' reference OS07 supplies the total-influence-square lower bound reproduced as Theorem VIII.6 (printed pp.89–90). No claim of a new optimal exponent is made.

5. Michael Damron, Jack Hanson and Philippe Sosoe, *Strict inequality for the chemical distance exponent in two-dimensional critical percolation*, Communications on Pure and Applied Mathematics 74(11) (2021), 2431–2455; arXiv:1708.03643, PDF dated 5 July 2021. Theorem 1, p.1, bounds the conditional expected shortest crossing length relative to the lowest crossing. Its triangular-site discussion yields an exponent strictly below 4/3 for shortest crossing length. That is certificate geometry; it does NOT give a query algorithm finding a certificate at that cost. Stored as 1708.03643.response/.txt.

6. Nikita Gladkov, *Percolation Inequalities and Decision Trees*, arXiv:2408.08457v2, 22 August 2024. Theorem 1.1/Theorem 6.2 bounds three-point connectivity probabilities on general graphs. Its decision-tree inequalities are related techniques, not a matching crossing query-complexity theorem. Stored as 2408.08457.response/.txt.

7. Fan Chang, Hong Liu and Miao Liu, *The sharp diagonal spectral correlation inequality on the discrete cube*, arXiv:2606.32024v1, 30 June 2026. The main theorem bounds covariance of increasing Boolean functions by degree-weighted collision of Fourier spectra. No crossing algorithm or query-cost exponent theorem is stated. Six mentions of percolation, mostly contextual/bibliographic, do not change this. Stored as 2606.32024.response/.txt. This paper is a lead only; its proof is not an assumption in ATTEMPT.md.

8. Yitzchak Shmalo, *Entropy and singularity of spectral and pivotal sets in planar percolation*, arXiv:2609.15388v1, 14 September 2026. Theorem 1.1 concerns crossing entropy; the paper also treats discrete spectral/pivotal law separation. These are different open questions. It does not state/prove the optimal query exponent posed here. Stored as 2609.15388.response/.txt. Its assertions and the brain's provisional entropy claims are not used as lemmas.

Other arXiv and citation results on Voronoi/Poisson/Gaussian/Ising models, critical speeding-up, sharp thresholds and random-cluster decision trees use different hypotheses or objectives. They were screened as leads, not accepted as a printed solution.

## Read-only local evidence searches

- math_recall.py: "percolation randomized algorithm computational complexity revealment"; intake attempt card returned, treated as unverified.
- brain.py recall: "percolation algorithms mistakes" and "percolation crossing query complexity"; no checked solution returned.
- rg for C0020 in intake ledgers and codex_pool_2026_10_10. The first wildcard directory invocation failed on Windows; it was rerun with enumerated directory paths. The relevant intake is C0020-A001 in probability_1000_intake_claude_20260907/attempts.jsonl; it claims no solution and includes unsupported Fourier-level speculation.
- Read codex_pool_2026_10_10/team_O/w336/proofs/C0020.md: fixed-order OR and prepended-site-query counterexamples refute uniform revealment from total cost. Also read the corresponding file directly with git show origin/master:probability_campaigns/codex_pool_2026-10-10/team_O/w336/proofs/C0020.md in math-open-problems, after read-only git ls-tree filtering. No repository changes.

## Every external request, including unsuccessful searches

All requests used Python urllib from the shell, with bounded timeouts. No built-in web search was used. Exact requests and responses are retained; the following ledger is generated verbatim from search_log.jsonl.

'''
lines=[intro]
for row in [json.loads(x) for x in (R/'search_log.jsonl').read_text(encoding='utf8').splitlines()]:
 lines.append(f"- {row['date']} — {row['service']} — {row['url']} — "+(f"HTTP {row['status']}, {row['bytes']} bytes" if 'status' in row else row['error'])+'\n')
lines.append('\n## Saved result inventories\n\n')
ns={'a':'http://www.w3.org/2005/Atom'}
for key in ['arxiv','arxiv_target','arxiv_chemical','arxiv_hex','arxiv_cost_exact']:
 p=R/(key+'.response')
 if p.exists():
  lines.append('\n### '+key+'\n\n')
  for e in E.parse(p).getroot().findall('a:entry',ns):
   title=' '.join(e.findtext('a:title',namespaces=ns).split())
   lines.append('- '+e.findtext('a:id',namespaces=ns)+' — '+title+'\n')
for key in ['crossref','crossref_target','crossref_source']:
 p=R/(key+'.response')
 if p.exists():
  lines.append('\n### '+key+'\n\n')
  for x in json.loads(p.read_text(encoding='utf8'))['message']['items']:
   lines.append('- '+str(x.get('title'))+' — DOI '+x['DOI']+'\n')
(R/'LITERATURE.md').write_text(''.join(lines),encoding='utf8')
print('LITERATURE saved',len(''.join(lines)))
