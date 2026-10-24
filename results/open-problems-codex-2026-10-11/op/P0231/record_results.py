from pathlib import Path
import json, xml.etree.ElementTree as E
R=Path(__file__).resolve().parent
out=['# P0231 literature audit — 2026-10-12','',
'No retrieved paper states and proves determinism of the Hausdorff dimension for the original two-seed Euclidean Poisson-coloring frontier. This is a bounded negative search result, not an exhaustive current-open certification. SOLVED_IN_LITERATURE is not claimed.','',
'## Primary source and exact remaining question','',
'Anne-Laure Basdevant, Guillaume Blanc, Nicolas Curien, Arvind Singh, “Fractal properties of the frontier in Poissonian coloring,” ALEA, Latin American Journal of Probability and Mathematical Statistics 20 (2023), 1565–1586. DOI: 10.30757/ALEA.v20-59. arXiv:2302.07254v2, updated 2023-11-27. Source URL: https://alea.impa.br/articles/v20/20-59.pdf. Download saved as source.pdf; all pages extracted into source_text.txt.','',
'Verbatim question-containing paragraph, PDF page 3 / printed page 1567:','',
'> “Although our results show the convergence in a strong sense of the colored regions and establish the fractal nature of the frontier, many questions remain open, such as the existence of a zero–one law for the Hausdorff dimension of F∞. We focus here on the planar case d = 2, which concentrates the most interesting topological questions.”','',
'This is a prose question, not Open Question 1.2 (which concerns curves). The model on PDF pages 1–2 has fixed distinct seeds in [0,1]^d and independent uniform arrivals, with Euclidean nearest-neighbor inheritance. F∞ is the intersection of closures of both color-site sets. The strict bounds in Theorem 1.1 (PDF page 2) are already proved and are not the task. Proposition 3.8 (PDF pages 20–21) explicitly assumes d>=2 for the lower bound. The immediately following topological questions specialize to d=2. No theorem giving deterministic dimension was found in the source.','',
'## Every network search / fetch','',
'Raw service responses are retained locally. Entries report failures honestly. OpenAlex citation retrieval was attempted but rate-limited; the DOI-form cites filter in the attempted request is not validated and is not a completed citation traversal. A correct OpenAlex work-ID traversal requires first resolving the source work, which also returned HTTP 429. Semantic Scholar citation traversal did succeed.','']
for fn in ['search_log.json','search_followup_log.json','citations_log.json','citing_fetch_log.json']:
 for x in json.loads((R/fn).read_text(encoding='utf8')):
  out.extend([f"- {x['date']} | {x['service']} | {x['status']} | query/URL: `{x['url']}`"])
out.extend(['','## Search results and relevance',''])
ns={'a':'http://www.w3.org/2005/Atom'}
for filename in ['arxiv.txt','arxiv_broad.txt']:
 root=E.parse(R/filename)
 out.extend([f'### {filename}',''])
 for e in root.findall('a:entry',ns):
  title=' '.join(e.find('a:title',ns).text.split()); aid=e.find('a:id',ns).text
  out.append(f'- {title}; {aid}; updated {e.find("a:updated",ns).text}.')
out.extend(['','The exact phrase arXiv search returned only the source and Aldous (2018). The broadened search returned 60 entries, including newer papers, but their titles/abstracts did not supply a matching Euclidean-frontier zero-one theorem. This query is noisy and truncated at 60; it is not exhaustive.','',
'Crossref broad title query returned the source and Aldous among mostly unrelated works. The dimension/zero-one query produced no matching paper. GitHub exact and broader repository searches each returned total_count=0. Semantic Scholar relevance search returned the source, Aldous, a duplicate Aldous submission, and unrelated results.','',
'## Papers citing the source',''])
cites=json.loads((R/'semantic_citations.txt').read_text(encoding='utf8'))
for item in cites['data']:
 p=item['citingPaper'];out.append(f"- {p['title']} ({p['year']}); identifiers: {json.dumps(p['externalIds'],ensure_ascii=False)}.")
out.extend(['',
'Fetched and examined newer close leads:',
'',
'1. Anne-Laure Basdevant and Arvind Singh, “Random sequential nearest-neighbor coloring on trees,” arXiv:2606.24793v1, posted 2026-06-23 (PDF dated June 24, 2026), 39 pages. Full PDF and text retained as tree_paper.txt (PDF bytes) and tree_paper_text.txt. Its abstract and introduction explicitly distinguish regular-tree geometry from Euclidean coloring. Its theorems concern genealogical forests and local limits on trees; this is a different object, not a solution to P0231.',
'2. Augusto Teixeira and Daniel Ungaretti, “Holder continuity of interfaces for scale-invariant Poisson stick soup,” arXiv:2601.19546v1, posted 2026-01-27 (PDF dated January 28, 2026), 34 pages. Full PDF/text retained as stick_paper.txt and stick_paper_text.txt. The object is the covered/vacant interface of a planar Poisson stick soup; the paper proves tightness and Holder continuity, not this coloring-frontier zero-one theorem.',
])
s=json.loads((R/'survey_metadata.txt').read_text(encoding='utf8'))['message']
authors=', '.join(a.get('given','')+' '+a.get('family','') for a in s.get('author',[]))
out.extend([f"3. {authors}, {s.get('title')}, {s.get('container-title')}, volume {s.get('volume')}, article {s.get('article-number')}, DOI {s.get('DOI')}; publication metadata {s.get('published')}. Crossref metadata retrieved, full text not reviewed. Survey lead only.",'',
'Other relevant references from the primary source:',
'',
'- David Aldous, “Random partitions of the plane via Poissonian coloring and a self-similar process of coalescing planar partitions,” Annals of Probability 46(4) (2018), 2000–2037; DOI 10.1214/17-AOP1218; arXiv:1701.00131. Predecessor, not a later solution.',
'- John Preater, “A species of voter model driven by immigration,” Statistics & Probability Letters 79(20) (2009), 2131–2137. The source attributes zero Lebesgue measure to its Theorem 2, and island creation to Theorem 3. Neither is dimension determinism.',
'- Lyuben Lichev and Dieter Mitsche, “New results for the random nearest neighbor tree,” arXiv:2108.13014; DOI 10.1007/s00440-024-01268-2. Genealogical/combinatorial lead; no matching theorem identified.',
'- Michael Aizenman and Almut Burchard, “Hölder regularity and dimension bounds for random curves,” Duke Mathematical Journal 99(3) (1999), 419–453. Used for source dimension bounds; does not settle this model-specific question.',
'- Edwin Hewitt and Leonard J. Savage, “Symmetric measures on Cartesian products,” Transactions of the American Mathematical Society 80 (1955), 470–501. Standard finite-permutation zero-one law used for the envelope reduction; no claim of applicability directly to the original coloring.',
'',
'## Brain and prior-work searches (read-only)',
'',
'- math_recall.py query “Poissonian coloring frontier dimension”: returned source_f99341d044db78ac6ec222b5d6a69595c260bf605fb2be6e055a242a9bb37cc1, original-question card claim_fb1674b634c48ffddc2f64fc48ad9fca6751ac3ee46a6528f9ced76aee43343b, and whole prior attempt card claim_a3f5a8e2ffcc02ceb1350467c3f66117c3179f68d3e9d89b894151251ebc2519. Prior attempt warns that early changes affect infinitely many descendant colors, and proposes regeneration as a missing ingredient. Rechecked rather than assumed.',
'- brain.py recall “Poisson coloring frontier” and “Poisson coloring frontier mistakes”: returned mostly off-topic memories; no proof imported.',
'- rg P0231 against intake and codex_pool_2026_10_10: direct wildcard path failed in PowerShell; retried by enumerating matching intake directories and searching JSONL files. No matching output in the accessible matching directories. A follow-up directory listing was requested.',
'- Read-only git ls-tree origin/master on ~/math-open-problems, followed by filename filtering for 0231 / poisson-color / frontier: no exact P0231 filename located. Broad frontier matches were unrelated. No repository content was changed.','',
'Search conclusions are limited by service coverage, relevance ranking, API rate limits, and the fact that metadata alone cannot rule out an unadvertised theorem. No solved-in-literature verdict is warranted.'])
(R/'LITERATURE.md').write_text('\n'.join(out)+'\n',encoding='utf8')
claims=[
 {'claim':'The supremum of Hausdorff dimensions over all finite-prefix binary recolorings with fixed uncolored future genealogy is almost surely deterministic.','status':'proved','proof_location':'ATTEMPT.md Section 2','remaining_gap':'This enlarged envelope need not equal the original red-blue frontier dimension; no equality is proved.','checks':['Full measurability, refinement, and finite-permutation proof','finite_checks.json: 100 finite genealogy trials passed','FrontierAlgebra.lean: finite set identity only; compilation status in lean_check.txt']},
 {'claim':'The original frontier dimension is at most the deterministic finite-recoloring envelope.','status':'proved','proof_location':'ATTEMPT.md Sections 2.2 and 2.4','remaining_gap':'The opposite inequality and constancy of the original dimension remain unproved.','checks':['Exact grouping identity and inclusion']},
 {'claim':'For d=1 and two distinct fixed seeds, the limiting frontier is a singleton almost surely and has Hausdorff dimension zero.','status':'proved_special_case','proof_location':'ATTEMPT.md Section 3','remaining_gap':'Does not settle d>=2, the source fractal setting.','checks':['Complete order and density proof','finite_checks.json: 20 one-dimensional order trials passed']},
 {'claim':'A finite permutation of arrivals can change infinitely many later colors and the limiting frontier with positive probability, even in d=1.','status':'proved_special_case','proof_location':'ATTEMPT.md Section 4, positive-probability control','remaining_gap':'The dimensions in this example are both zero. It is not a dimension counterexample.','checks':['Strict inequalities on open intervals (.39,.41) and (.67,.69)','Probability .0004','One-dimensional singleton theorem']},
 {'claim':'The original Euclidean two-seed frontier attains the deterministic finite-recoloring envelope almost surely.','status':'conjecture','proof_location':'ATTEMPT.md Sections 4 and 6','remaining_gap':'No regeneration or transplantation theorem is proved; this sufficient target could be too strong.','checks':['Explicitly not used as a proved assertion']},
]
with (R/'CLAIMS.jsonl').open('w',encoding='utf8') as out:
 for x in claims: out.write(json.dumps({'problem_id':'P0231',**x},ensure_ascii=False)+'\n')
print('Recorded LITERATURE.md and CLAIMS.jsonl')
