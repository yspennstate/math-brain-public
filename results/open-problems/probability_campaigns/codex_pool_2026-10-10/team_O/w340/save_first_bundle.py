"""Save checked rows and the specifically authorized draft output; never ingest a store."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCES=json.loads((ROOT/'SOURCE_REPORT.json').read_text(encoding='utf-8'))
entries=[]
relations=[]
rows=[]
items=[
    ('P0276','p0276-product-without-cutoff-checked-construction','probability.markov','theorem','Checked Abelian Cayley family with product condition and no cutoff',
     'PROOF FOR THE EXPLICIT FAMILY; independent audit pending. For rate-one continuous-time simple random walk on G_d=(Z/2Z)^d x Z/m_dZ, m_d=max(2,floor(2^d log(d)/4)), with generators (e_i,a) for a!=0 and (h,0) for h!=0, the spectral gap is asymptotic to 2/d, t_mix(1/4) is asymptotic to d log(d)/4, and t_mix(3/4)/t_mix(1/4) tends to log(4/3). Thus this simple unweighted Abelian Cayley family satisfies the spectral product condition and lacks total-variation cutoff. This reconstructs an existing campaign candidate; no priority claim or audited solution of the literature question is made.',
     'p0276_proof.md','p0276_checks.json',
     ['d tends to infinity','Continuous-time rate-one walk','Degree is unbounded','Exact generator set and auxiliary group as stated']),
    ('C0033','determinantal-entropy-two-site-fixed-diagonal-concavity','probability.determinantal','lemma','Two-site determinantal entropy is concave with fixed diagonal entries',
     'PROOF OF A SPECIAL CASE; independent audit pending. Fix a,b in [0,1] and let K(z)=[[a,z],[conjugate(z),b]]. On the disk |z|^2<=min(ab,(1-a)(1-b)), the Shannon entropy of the determinantal subset measure with kernel K(z) is concave as a function of the complex number z. Its four atom probabilities are ab-|z|^2, (1-a)(1-b)-|z|^2, a(1-b)+|z|^2, and (1-a)b+|z|^2. This covers all two-site Hermitian positive contractions with common diagonals, including boundary kernels, but does not settle jointly varying diagonals or larger kernels.',
     'c0033_proof.md','c0033_checks.json',
     ['Exactly two sites','Hermitian positive contractions','The two diagonal entries are held fixed','Entropy uses 0 log 0 = 0'])
]
for problem,key,namespace,kind,title,statement,proof,checks,assumptions in items:
    entry={'key':key,'namespace':namespace,'logical_name':key,'kind':kind,'title':title,'statement':statement,'proof_text':(ROOT/proof).read_text(encoding='utf-8'),'assumptions':assumptions,'domain':'probability theory','source':{'source_id':'owner-own-work:w340:'+key,'url':'urn:owner-own-work:w340:'+key,'revision':'2026-10-10-draft-awaiting-w346','license':'owner-own-work (campaign proof and local check receipt)','excerpt':None}}
    entries.append(entry)
    endpoints=[]
    for prefix,edge in [('Open problem:','specializes'),('Attempt on','cites')]:
        candidates=[n for n in SOURCES[problem]['store_nodes'] if n['title'].startswith(prefix)]
        if not candidates:
            continue
        node=candidates[-1]
        logical=json.loads(node['metadata_json'])['logical_id']
        quote=node['body'].split('Source:')[0].replace('\n',' ')[:240]
        rationale='New end: "'+statement[:230]+'"; store end: "'+quote+'"; '+('this is the scoped case of the stored question.' if edge=='specializes' else 'continues the previously recorded route.')
        relations.append({'from_key':key,'to_existing_logical':logical,'kind':edge,'rationale':rationale})
        endpoints.append({'kind':edge,'logical_id':logical,'store_node_id':node['id'],'source_quote':quote})
    metrics=json.loads((ROOT/checks).read_text(encoding='utf-8'))
    rows.append({'row_id':'w340.'+problem+'.001','problem_id':problem,'label':'proof','statement':statement,'proof_path':str(ROOT/proof),'measurement_path':str(ROOT/checks),'command':'python -X utf8 check_first_batch.py','audit_status':'PENDING_W346','current_literature_status':'UNVERIFIED_OFFLINE; not described as solved','store_edges':endpoints})

payload={'spec':'mathbrain-draft-v1','author_agent':'w340','bundle_slug':'w340-open-problems-first-checks-20261010','entries':entries,'relations':relations}
local=ROOT/'bundle_001.json'
local.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inbox=Path('~/math-brain-inbox/w340').resolve()
assert inbox==Path('~/math-brain-inbox/w340').resolve()
inbox.mkdir(parents=True,exist_ok=True)
final=inbox/'bundle_001.json'
assert not final.exists(), 'Do not overwrite any existing draft'
part=inbox/'bundle_001.part'
assert not part.exists(), 'Do not overwrite a previous partial draft'
part.write_bytes(local.read_bytes())
part.rename(final)

result_path=ROOT/'results.jsonl'
existing={json.loads(line)['row_id'] for line in result_path.read_text(encoding='utf-8').splitlines() if line.strip()}
with result_path.open('a',encoding='utf-8',newline='\n') as output:
    for row in rows:
        if row['row_id'] not in existing:
            output.write(json.dumps(row,ensure_ascii=False)+'\n')

patches=ROOT/'patches'
patches.mkdir(exist_ok=True)
live='~/math-brain-inbox/w340/bundle_001.json'
patch=''.join(difflib.unified_diff([],local.read_text(encoding='utf-8').splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
(patches/'01_first_research_bundle.diff').write_text(patch,encoding='utf-8')
(ROOT/'AUDIT_REQUEST.md').write_text('Auditor: w346\n\nPlease independently check each stated mathematical result before KEEP. No result has a KEEP yet. Begin from the self-contained statements in bundle_001.json; proof files and finite-check receipts are listed in results.jsonl. Check source scope separately for P0276. Do not count a random check as a proof or a current-openness certificate.\n\nDraft: '+str(final)+'\n\nNEXT: Audit the explicit P0276 construction and the fixed-diagonal C0033 lemma; return per-row KEEP/FIX/DROP.\n',encoding='utf-8')
print(json.dumps({'draft':str(final),'entries':len(entries),'relations':len(relations),'saved_rows':len(rows),'audit_status':'PENDING_W346'},ensure_ascii=False))
