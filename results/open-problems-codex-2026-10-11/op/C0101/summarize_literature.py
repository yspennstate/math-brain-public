from pathlib import Path
import json,xml.etree.ElementTree as E
R=Path(__file__).parent
source=R/'source.txt';t=source.read_text(encoding='utf-8'); start=t.index('(4) As proved'); end=t.index('References',start)
ns={'a':'http://www.w3.org/2005/Atom'}
out=['\n# Literature assessment — 2026-10-12',
'No inspected paper states and proves the d≥3 maximal-element classification or the isolation/rationality questions. This is a bounded search result, not a proof that no solution exists. Verdict is PARTIAL, not SOLVED_IN_LITERATURE.',
'\n## Source and exact question',
'Lionel Levine and Yuval Peres, *Laplacian growth, sandpiles, and scaling limits*, Bulletin of the American Mathematical Society 54 (2017), 355–382. DOI: 10.1090/bull/1573; arXiv:1611.00411v1. Downloaded `source.pdf`, extracted `source.txt`; open problem 9(4), printed/PDF p.27. The set Γ is defined on printed/PDF p.21 as the Euclidean closure of matrices A for which Δceil(x^T A x/2) stabilizes locally.',
'Exact question (PDF text, with line breaks retained):\n\n```text\n'+t[start:end].strip()+'\n```',
'Hypotheses: real symmetric d-by-d matrices, standard nearest-neighbor Z^d, degree 2d, integer heights, unstable at height≥2d, d≥3. The semidefinite order used by the cited classification is A≤B iff B-A is positive semidefinite (apollonian.pdf p.2). The survey does not define a different order. Isolation is interpreted relative to the maximal set.',
'\n## Relevant papers and why they do not settle C0101',
'1. Lionel Levine, Wesley Pegden, Charles K. Smart, *The Apollonian structure of integer superharmonic matrices*, Annals of Mathematics 186(1) (2017), 1–67. DOI: 10.4007/annals.2017.186.1.1; arXiv:1309.3267v4. Downloaded and inspected pp.1–4. Theorem 1.1, p.2, classifies 2-by-2 matrices; its Laplacian threshold is 1 and its representatives have q_A+o(|x|²) growth. These differ in normalization from the survey threshold 3 in d=2. No d≥3 classification is asserted. Theorem 1.2 constructs full-rank affine-periodic representatives: a lead for rationality, not a higher-dimensional theorem.',
'2. Ahmed Bou-Rabee, *Integer superharmonic matrices on the F-lattice*, Advances in Mathematics (January 2024), article 109400. DOI: 10.1016/j.aim.2023.109400; arXiv:2110.07556v2 (5 November 2023). Downloaded on retry and inspected pp.1–6, Theorems 1.1–1.3. The F-lattice is a directed periodic planar graph on Z^2. Theorem 1.1 classifies its cone packing; Theorem 1.3 supplies affine-periodic odometers. Different graph and dimension: not a solution for nearest-neighbor Z^d, d≥3.',
'3. Nikita Kalinin, *Sandpile solitons in higher dimensions*, arXiv:2212.03717v1 (6 December 2022); DOI: 10.1007/s40598-023-00224-7. Downloaded and inspected pp.1–2. Theorem 1, p.2, classifies hyperplane-shaped movable soliton states, not quadratic Hessians. The author says on p.2: "For example, there is no classification of patterns via quadratic forms similar to [10, 8] in dimensions more than two." This is evidence for status as of that manuscript, not an exhaustive current-status theorem.',
'4. Nikita Kalinin and Mikhail Shkolnikov, *Sandpile solitons via smoothing of superharmonic functions*, arXiv:1711.04285; DOI: 10.1007/s00220-020-03828-8. The retrieved arXiv abstract concerns piecewise-linear functions on Z^2. A technique lead; no quadratic maximal-matrix classification.',
'5. Ahmed Bou-Rabee, *Dynamic Dimensional Reduction in the Abelian Sandpile*, arXiv:2009.05968; DOI: 10.1007/s00220-022-04322-z. Found in citation lists; this concerns sandpile dynamics, and no exact C0101 solution is claimed from its metadata. Do not assume arbitrary quadratic representatives separate across coordinates.',
'\n## Search results and limitations']
for name in ['arxiv_0.txt','arxiv_1.txt','arxiv_higher.json','arxiv_superharmonic_dimension.txt']:
 root=E.fromstring((R/name).read_text()); entries=root.findall('a:entry',ns)
 out.append(f'\n{name}: {len(entries)} returned entries.')
 for e in entries:out.append('- '+e.find('a:title',ns).text.replace('\n',' ')+'; '+e.find('a:id',ns).text)
for name in ['semantic_source.json','semantic_citing_lps.txt']:
 data=json.loads((R/name).read_text());out.append(f'\n{name}: {len(data.get("data",[]))} citation records; next={data.get("next")}. Titles and returned abstracts screened for this question; no matching solution identified. Raw responses retained.')
 for item in data.get('data',[]):
  p=item['citingPaper'];out.append('- '+p['title']+' ('+str(p.get('year'))+'); '+json.dumps(p.get('externalIds')))
for name in ['github_6.txt','github_7.txt']:
 d=json.loads((R/name).read_text());out.append(f'\n{name}: total_count={d.get("total_count")}; incomplete_results={d.get("incomplete_results")}.')
out+=['\nOpenAlex repeatedly returned HTTP 429: the shared anonymous IP daily budget was exhausted. The correct source DOI lookup and a citing-source filter request were attempted and logged, but source-ID resolution and the OpenAlex citing-work screen could not be completed. An earlier lookup used an incorrect DOI suffix 1553, corrected to 1573 after the successful Crossref lookup. No API keys were sought. Semantic Scholar supplied both the survey and LPS citation lists instead.',
'Semantic Scholar standard search initially returned HTTP 429; bulk search and citation endpoints succeeded. Crossref supplied the source DOI and publication metadata and found the planar and F-lattice classification papers. GitHub repository searches yielded no relevant solution.',
'\n## Read-only research brain and earlier attempts',
'Ran math_recall.py "integer superharmonic matrices" and brain.py recall "integer superharmonic matrices mistakes" and "sandpile integer superharmonic". Read the C0101 entries in the seven probability_1000_intake directories (matching entries saved in earlier_intake.txt), and the w332/w346 files under codex_pool_2026_10_10. Listed matching origin/master paths in math-open-problems and read the C0101 report through git show. No repository working tree or brain store was edited.',
'The old bound Δceil(a n²/2)≤a+1 is false (a=1/2, n=0 gives 2>3/2). The old claim of coordinate separation does not prove diagonal classification. The binomial-quadratic identity is valid but needed the closure connection and trace bound proved in ATTEMPT.md before maximality followed. Packing analogies and higher-dimensional Descartes arithmetic provide no Γ correspondence.']
with (R/'LITERATURE.md').open('a',encoding='utf-8') as f:f.write('\n\n'.join(out)+'\n')
print('Literature assessment saved')
