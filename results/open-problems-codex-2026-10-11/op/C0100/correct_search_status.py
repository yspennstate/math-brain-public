from pathlib import Path
import json
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8');s=s.replace("Semantic Scholar's direct ARXIV:1611.00411/citations endpoint also returned 429.","Semantic Scholar's direct ARXIV:1611.00411/citations endpoint subsequently succeeded with HTTP 200 (32 records, no next-page field), although the earlier search and source requests returned 429. The citing records were screened by title and selected leads were fetched from arXiv.")
s=s.replace('with the cited quota limitations','with OpenAlex quota limitations and the earlier Semantic Scholar search failures')
s+='\n## Semantic Scholar citation retrieval and GitHub screening\n\nThe final Semantic Scholar direct citation request succeeded; semantic_citations.json is retained. Titles of all 32 returned records (not a guarantee of exhaustive citation coverage):\n'
for row in json.loads(Path('semantic_citations.json').read_text())['data']:
 x=row['citingPaper'];s+=f"- {x['year']}: {x['title']}; external IDs {json.dumps(x.get('externalIds',{}),ensure_ascii=False)}.\n"
s+='\nPotential leads requiring abstract comparison: arXiv:1911.01762 (high-dimensional height distribution), arXiv:2009.05968 (dynamic dimensional reduction), and arXiv:2609.21359 (comb lattices). Other citation titles concern distinct graphs, random growth, divisible/leaky sandpiles, or algebraic models.\n\nThe identity GitHub query returned these repositories; these are code/experimental leads, not paper proofs:\n'
for x in json.loads(Path('github_identity.json').read_text())['items']:s+=f"- {x['full_name']}: {x['html_url']}; {x['description']}.\n"
p.write_text(s,encoding='utf8')
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8').replace('Semantic Scholar search and citations returned 429.','Semantic Scholar search requests returned 429, but its final direct source-citations request succeeded with 32 records; these were screened and selected leads were fetched.');p.write_text(s,encoding='utf8')
