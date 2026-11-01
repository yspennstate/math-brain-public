import json,pathlib,xml.etree.ElementTree as E
P=pathlib.Path(__file__).parent
out=['# Literature record — P0287 — 2026-10-12','',
'## Status and exact source',
'Leonid Petrov and Axel Saenz Rodriguez (organizers), *All roads to the KPZ universality class*, AIM Workshop Summary (workshop 2025), PDF p.5, section “ASEP on graphs or trees,” system S2. https://aimath.org/pastworkshops/roadtokpzrep.pdf. Saved as aim_https.pdf, with extracted text source.txt.',
'',
'> S2 TASEP on the full line with a particle removal mechanism at site 0 (where particles disappear from the system at a fixed rate).',
'',
'> We then focused on studying the invariant measure of the second system using the matrix product ansatz.',
'',
'> A key challenge in applying the matrix ansatz to our system lies in identifying the appropriate telescoping structure.',
'',
'> We agreed to continue working on this problem after the workshop. However, there has been no progress since then.',
'',
'The report names Zongrui Yang as contact. It specifies full-line TASEP and fixed-rate removal at 0, but does not state the rate normalization, positivity explicitly, tail densities, extremality, or an all-measures quantifier. This attempt uses unit jump rate and kappa>0, as in the supplied problem; “characterize invariant measures” is the research objective inferred from the report, not a separately numbered theorem. The fetched workshop page identifies the event as 2025; the PDF itself is a follow-up summary rather than a journal article.',
'',
'No paper proving the full classification was identified. This is NOT a verified assertion that no such paper exists. OpenAlex and Semantic Scholar requests were rate-limited; no exact source record was obtained from OpenAlex, so its citing-works query could not be performed with a verified work ID. These search gaps preclude an exhaustive status claim. No SOLVED_IN_LITERATURE verdict is assigned.',
'',
'## Search log',
'All requests below were made on 2026-10-12 using Python urllib, never built-in web search. Exact URLs contain the exact queries and parameters. Response bodies and machine logs are retained in this folder.',
'',
'- Initial source fetch with the default urllib user-agent: https://aimath.org/pastworkshops/roadtokpzrep.pdf — HTTP 403; retried successfully with a browser user-agent.',
]
for fn in ['search_log.json','followup_log.json']:
 for x in json.loads((P/fn).read_text(encoding='utf8')):
  out+=['- **'+x['service']+'**: '+x['url']+' — '+(x.get('error') or str(x.get('status'))+'; saved '+x.get('file',''))]
out+=['',
'### Read-only brain and earlier-record searches',
'- math_recall.py: “TASEP invariant measures killing defect”; returned the previous local-current/product-obstruction attempt and its dependencies.',
'- brain.py recall: “TASEP invariant measures mistakes”; no useful mathematical result. The helper reported its own automatic index refresh; no remember/write command was requested. No further brain.py commands were used.',
'- math_recall.py: “Liggett half line exclusion stationary measures boundary”; results mostly off topic, not used as premises.',
'- rg for P0287 in intake problems.jsonl, attempts.jsonl and sources.jsonl, and codex_pool_2026_10_10: no matching earlier files found in these targeted paths; two intake directories lacked attempts/sources files. An initial broader jsonl search found the 2026-10-10 problem-list record with the supplied statement and caveat.',
'- Read-only git ls-tree origin/master filtered for P0287/p0287 in ~/math-open-problems: no matching path. No repository was changed.',
'',
'## Relevant leads, with scope differences',
'- B. Derrida, M. R. Evans, V. Hakim, V. Pasquier, “Exact solution of a 1D asymmetric exclusion model using a matrix formulation,” *Journal of Physics A: Mathematical and General* 26 (1993), 1493–1517. Explicitly cited by the workshop source. Finite open ASEP matrix ansatz, not full-line single-site killing; no inference of a printed solution.',
'- Riddhipratim Basu, Sourav Sarkar, Allan Sly, “Invariant Measures for TASEP with a Slow Bond,” arXiv:1704.07799 (2017). Read the returned abstract. A conservative slow hopping bond is a different generator: no death and no current loss at the defect. Its invariant-measure theorem cannot answer this question.',
'- Tomohiro Sasamoto, Lauren Williams, “Combinatorics of the asymmetric exclusion process on a semi-infinite lattice,” arXiv:1204.1114v1 (2012). Full PDF fetched from https://arxiv.org/pdf/1204.1114 to halfline.pdf, text halfline.txt. Directly relevant to the reduction in ATTEMPT Section 5, but treats a semi-infinite boundary and supplies formulas under a semi-infinite matrix ansatz; no full-line killing classification claimed here.',
'- Zongrui Yang, “Limits of open ASEP stationary measures near a boundary,” arXiv:2402.13675v2 (submitted 2024). Returned abstract concerns limits of finite open stationary measures and convergence near a boundary. A useful half-line lead, not the killing-site model.',
'- Yuliy Baryshnikov, Alexander Stolyar, “Multi-floor generalization of TASEP,” arXiv:2603.13610v2 (submitted 2026-03-13). This is a post-workshop hit, but the model has multiple occupancy, back-pressure movement, and boundary input/output. Its standard-TASEP c=1 case is still boundary-driven and has no interior killing; not a solution.',
'- Sourav Pal, Abhik Basu, “Stationary densities in a weakly nonconserving asymmetric exclusion processes with finite resources,” arXiv:2602.08405v1 (2026). Post-workshop hit. Langmuir kinetics and a finite-resource reservoir differ from single-site full-line killing; abstract describes density/phase diagrams, not the requested classification.',
'- ExclusionProcess-tools/TASEPy and Francesco-Cerutti/TASEP-inhomogeneities-approximations, GitHub repositories returned by “TASEP stationary”. Numerical/approximation packages for inhomogeneous TASEP, not proof of this classification. Query “TASEP killing” returned zero repositories.',
'',
'## All arXiv records returned (for audit)',
]
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['arxiv_https.txt','arxiv_removal.txt','arxiv_halfline.txt']:
 out+=['','### '+fn]
 for e in E.parse(P/fn).findall('a:entry',ns):
  title=' '.join(e.find('a:title',ns).text.split());authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns));url=e.find('a:id',ns).text;date=e.find('a:published',ns).text
  out+=['- '+authors+'. '+title+'. '+url+'; submitted '+date+'.']
out+=['','## Crossref returned records','Broad queries were noisy; irrelevant matches are listed to make the search reproducible. No exact killing-site theorem was identified in these records.']
for fn in ['crossref.json','crossref_target.json']:
 out+=['','### '+fn]
 for x in json.loads((P/fn).read_text(encoding='utf8'))['message']['items']:
  title='; '.join(x.get('title',[])) or '(no title)';authors=', '.join((a.get('given','')+' '+a.get('family','')).strip() for a in x.get('author',[]));date=x.get('published',x.get('issued',{})).get('date-parts',[])
  out+=['- '+authors+'. '+title+'. DOI '+x.get('DOI','')+'; publication date '+str(date)+'.']
(P/'LITERATURE.md').write_text('\n'.join(out)+'\n',encoding='utf8')
print('Wrote LITERATURE.md with all API URLs, returned references and limitations.')
