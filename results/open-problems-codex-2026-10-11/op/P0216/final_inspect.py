import pathlib,json,xml.etree.ElementTree as ET
R=pathlib.Path(__file__).resolve().parent
ns={'a':'http://www.w3.org/2005/Atom'}
p=R/'arxiv_aldous.raw';root=ET.fromstring(p.read_bytes())
entries=[]
for e in root.findall('a:entry',ns):
 entries.append({'title':' '.join(e.findtext('a:title',namespaces=ns).split()),'id':e.findtext('a:id',namespaces=ns),'authors':[a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)],'summary':' '.join(e.findtext('a:summary',namespaces=ns).split())})
(R/'arxiv_aldous_summary.json').write_text(json.dumps(entries,indent=2,ensure_ascii=False),encoding='utf8')
for e in entries:print(json.dumps(e,ensure_ascii=False))
claims=[]
for line in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines():
 x=json.loads(line)
 x['remaining_gap']=x['remaining_gap'].replace('Exact identification with source hypotheses pending PDF check; ','').replace('; exact source-model verification pending','').replace('exact source-model verification pending; ','')
 if 'Exact identification' in x['remaining_gap']:x['remaining_gap']='This is a lower bound only; optimal limit remains unresolved.'
 if 'Exact' in x['remaining_gap'] or 'pending' in x['remaining_gap']:print('CLAIM NEEDS REVIEW',x)
 claims.append(x)
claims[0]['remaining_gap']='This is a lower bound only; optimal limit remains unresolved.'
claims[0]['checks']='Source hypotheses verified. Exhaustive m=2,n=3 check: all 4096 equally likely cell-pair outcomes; exact isolated mean 507/1024.'
claims[2]['remaining_gap']='Does not prove existence or evaluation of the optimal limit; source already outlines a stronger 0.728 lower bound. No novelty claim.'
claims[2]['checks']='Full waiting-time proof in ATTEMPT.md. Exact 4096-outcome recurrence check; 300 simulations at each m=20,100,500,2000, lambda=2, agree with the 2/3 accepted fraction. Lean comparison check separately scoped.'
claims.append({'problem_id':'P0216','claim':'For all n in the independent same-label random-point model, Var(C_n)<=E C_n. Assuming E C_n=O(n^(1/3)), existence of a mean limit is equivalent to convergence in probability to the same constant.','status':'proved','proof_location':'ATTEMPT.md section 3','remaining_gap':'Neither establishes the mean limit nor evaluates its constant. The order upper bound is quoted from the source rather than reproved here.','checks':'Full conditional-expectation variance proof and pointwise deletion certificate; exact enumeration verifies certificate for every pair of rank-induced posets on n=1,2,3,4.'})
claims.append({'problem_id':'P0216','claim':'Exact distributions of C_n for n=1,2,3,4 are recorded in exact_posets.json.','status':'numerical_evidence','proof_location':'exact_posets.py and exact_posets.json','remaining_gap':'Small cases do not control the asymptotic constant.','checks':'Enumerated all pairs of rank-induced posets weighted by their representation multiplicities; totals (n!)^4; independently checked the n=2 formula.'})
(R/'CLAIMS.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in claims)+'\n',encoding='utf8')
print('validated claims',len(claims))
