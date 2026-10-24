from pathlib import Path
import json, xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
logs=[]
for f in ['search_log.json','search_more_log.json']:
 logs+=json.loads(Path(f).read_text())
entries=[]
for f in ['arxiv_recent.txt','arxiv_queue.txt','arxiv_spatial.txt','arxiv_horizon.txt']:
 if Path(f).exists():entries+=E.fromstring(Path(f).read_text()).findall('a:entry',ns)
ids=['2504.00765','1810.10650','2309.11865','2508.04666','2203.13242','2306.09584','2211.04651','2310.09284','2403.01341','cond-mat/9809193']
out=['# Literature and status check — 12 October 2026', '',
'No paper checked here proves the full canonical growing-ring covariance question with its density regimes and finite-size corrections. The verdict is not SOLVED_IN_LITERATURE. Searches are bounded and some services were rate-limited; this is not a proof that no solution exists.', '',
'## Source', '',
'Leonid Petrov and Axel Saenz (organizers), Evan Sorensen (moderator), Hieu Trung Vu (scribe), *AIM Workshop: All roads to KPZ Universality Open Problems*, March 19, 2025, Section 5, PDF p.3. Downloaded from https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ.pdf into source.pdf; full extraction source.txt. Exact question quoted in ATTEMPT.md. The statement supplies no asymmetry parameter or quantitative limiting regime.','',
'## API searches (raw responses retained)', '']
for l in logs:
 out+=['- '+l['date']+'; '+l['service']+'; query URL: '+l['url']+'. Result: '+(str(l['status'])+'; '+l['file'] if 'status' in l else l['error'])]
out+=['', 'OpenAlex source discovery and retry both returned HTTP 429. No indexed work ID for the workshop source could be obtained, so its citing-works endpoint could not be addressed. This citation-following branch remains incomplete. Semantic Scholar search and the known-paper citation endpoint also returned HTTP 429. GitHub returned zero repositories. Crossref broad search mostly returned irrelevant items; focused search and arXiv identified the leads below.', '', '## Relevant records and classification', '']
for id in ids:
 e=next((e for e in entries if id in e.findtext('a:id',namespaces=ns)),None)
 if e is None:continue
 authors=', '.join(a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns))
 title=' '.join(e.findtext('a:title',namespaces=ns).split())
 out+=['- '+authors+'. *'+title+'*. '+e.findtext('a:id',namespaces=ns)+'; first submitted '+e.findtext('a:published',namespaces=ns)+', last update '+e.findtext('a:updated',namespaces=ns)+'.']
out+=['',
'Martin: James B. Martin, *Stationary distributions of the multi-type ASEP*, Electronic Journal of Probability **25** (2020), paper 36, 1–41, DOI 10.1214/20-EJP421, arXiv:1810.10650v3. Downloaded and read the relevant sections in martin.pdf/martin_clean.txt. Theorem 3.1 (arXiv PDF p.19) is the infinite-line stationary queue construction; Theorem 3.3 (p.22) is its canonical-ring counterpart. These are reductions, not a covariance asymptotic theorem.', '',
'Ferrari–Gernholt: arXiv:2504.00765v3, 20 July 2026 (first submitted 1 April 2025). Downloaded decoupling.pdf and inspected main results plus Sections 3 and 5.3. Its abstract and introduction explicitly study large-time mixed space-time correlations on Z. Theorem 1.3 and Corollary 1.9 give time-scaled distributional decay of off-diagonal normal-mode two-point functions. They do not state the equal-time, canonical finite-ring asymptotic asked here. The queue drift/return-time estimates in Section 5.3.2 are relevant leads, and overlap the qualitative infinite-line exponential-mixing methods. They are NOT a solution in print to this question.', '',
'Stationary-horizon/speed-process papers: relevant to convergence of cumulative height fields in closing-density-gap regimes. Height-field convergence alone does not give pointwise occupation covariance asymptotics or canonical ring corrections; those require additional estimates. No theorem from these records is asserted to solve P0286.', '',
'Karimipour, cond-mat/9809193: the abstract advertises exact periodic correlations for a generalized overtaking model. Treat as a lead only: its model identification with the common-rate priority ASEP has not been verified here. Other arXiv recent hits include type-D ASEP, modified colloidal exclusion, open ASEP, and q-TAZRP: different models or time/geometry regimes.', '',
'## Read-only research brain and earlier work', '',
'Ran brain.py recall on “two species ASEP covariance mistakes” and on “Stationary two color ASEP covariance decay on a large ring”. The returned memories were mostly off-topic; none was used as mathematical authority. The recall helper reported an attempted detached index refresh which failed; no remember/write command was issued.', '',
'Ran math_recall.py on “Ferrari Martin queue two species stationary correlations”, and walked card claim_cbc6339431b41ebf26b756f6ded4a38087e5458884d5c62f68aff575b286e430. That prior attempt proves conservation/uniform-baseline identities but explicitly leaves asymmetric decay unresolved. Those identities were re-proved here.', '',
'Searched P0286 in the intake area and codex_pool_2026_10_10 with rg. A literal wildcard path failed on Windows; a follow-up Python glob search of probability_1000_intake_* JSONL files returned no matching records. The broader rg found the October 10 open-problems list entry, reproducing the supplied statement. A read-only git ls-tree of origin/master and a targeted Python path filter found no P0286-named answer path. No checkout file or repository state was changed. Raw path/ledger outputs are in previous_paths.txt and previous_ledger.txt.', '',
'## Search limitation', '',
'Only Martin and Ferrari–Gernholt full papers and the workshop PDF were downloaded/read. Other listed papers were screened from API metadata/abstracts. No theorem with the required identical ring objects, hypotheses and quantifiers was found and checked, so no word-for-word solution theorem or line-by-line solution mapping is claimed.']
Path('LITERATURE.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('LITERATURE.md saved')
