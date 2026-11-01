"""Local packet plus the explicitly authorized, exclusively claimed inbox draft."""
import json
from pathlib import Path
import datetime as dt

ROOT=Path(__file__).resolve().parent
claims=[json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
by_id={c['id']:c for c in claims}
cards=json.loads((ROOT/'MATH_BRAIN_RETRIEVAL.json').read_text(encoding='utf-8'))['cards']
existing={c['metadata']['logical_id']:c for c in cards}
old_attempt='math:probability.percolation:attempt-c0017-conformal-invariance-of-critical-bond-percolation-on-the-square-lattic'
target='math:probability.percolation:open-problem-c0017-conformal-invariance-of-critical-bond-percolation-on-the-square-lattic'
assert old_attempt in existing and target in existing

def entry(key,name,title,statement,assumptions,kind='concept'):
    return {'key':key,'namespace':'probability.percolation','logical_name':name,'kind':kind,'title':title,'statement':statement,'proof_text':None,'assumptions':assumptions,'domain':'probability theory','source':{'source_id':f'owner-own-work:w417:C0017:{key}','url':'file:///~/brain_workers/w417/ATTEMPT.md','revision':'draft-author-checked-2026-10-10-pending-w419','license':'owner-own-work','excerpt':None}}

entries=[entry('def-cells','terminal-partition-cells-and-exterior-sensitivity','Terminal partition cells and exterior sensitivity','A finite cell exposes distinct terminals T and a state pi, a partition of T recording connectivity inside the cell. On a common deterministic skeleton a crossing event is a Boolean function f of all cell partitions. Exterior sensitivity S_i(x_-i) equals one exactly when f(x_-i,pi) is nonconstant as pi ranges over the finite allowed cell states; it depends only on the exterior.',['Finite terminal sets and state spaces','Same deterministic skeleton and event in both compared laws'],'definition')]
for cid,key,name,title in [('w417-L1','weighted-comparison','sensitivity-weighted-independent-cell-comparison','DRAFT weighted independent-cell comparison'),('w417-L2','finite-obstruction','finite-independent-bond-three-terminal-site-obstruction','DRAFT finite independent-bond obstruction'),('w417-L3','pair-counterexample','three-terminal-pair-matching-crossing-counterexample','DRAFT pair matching crossing counterexample'),('w417-C1','dependence-counterexample','equal-marginals-dependent-crossing-counterexample','DRAFT equal marginals crossing counterexample')]:
    c=by_id[cid]
    entries.append(entry(key,name,title,'DRAFT author-proved partial result; independent referee review pending. '+c['statement']+' This does not prove the C0017 square-lattice scaling limit.',c['assumptions']))
entries.extend([
entry('pair-route','refuted-pair-connectivity-only-crossing-transfer','Refuted route: pair connectivity determines every crossing','REFUTED ROUTE, retained as a draft concept: matching all three pair-connectivity probabilities of a three-terminal cell was proposed to imply equality of every crossing event on a common skeleton. This implication is false: a star with three independent edges of probability 1/sqrt(2) matches each fair-site pair probability 1/2, but a connection from terminal a to the boundary set {b,c} has probability 1-1/(2sqrt(2)) rather than 1/2.',['Three distinct terminals','Full cell connectivity, rather than only one fixed pair event, can enter a crossing']),
entry('dependence-route','refuted-marginal-tv-product-comparison-with-dependent-cells','Refuted route: dependent cells substituted as products','REFUTED ROUTE, retained as a draft concept: applying the independent-cell comparison using only coordinate marginal total-variation distances for dependent endpoint laws is false. The laws of (Z,Z) and (Z,1-Z), for Z a fair bit, have identical coordinate marginals but probabilities 1/2 and 0 for the event that both bits equal one.',['Dependent joint laws are permitted in the refuted proposal']),
entry('gap','c0017-mesoscopic-weighted-cell-transfer-gap','Unresolved C0017 comparison gap G1','UNRESOLVED RESEARCH BRIDGE. For square-bond and triangular-site crossings in one marked Jordan domain, construct a common deterministic planar cell skeleton with independent partition laws mu_delta and nu_delta, representation errors r_mu(delta), r_nu(delta), and actual exterior hybrid laws H_i=(product_{j<i} nu_j)(product_{j>i} mu_j). Prove r_mu+r_nu+sum_i TV(mu_i,nu_i) P_Hi(S_i=1) tends to zero. The weighted comparison would then transfer the known reference crossing limit. No such construction or bound is proved in this packet. Neither the exponent 5/4 on square bonds nor uniform arm bounds for arbitrary hybrids may be assumed. Interface convergence still needs tightness and identification.',['Critical square-lattice independent bonds at p=1/2','Reference critical triangular-lattice independent sites at p=1/2','Uniform marked Jordan boundary approximation','No current-open or novelty claim']),
entry('spin-correction','c0017-standard-parafermionic-spin-source-correction','DRAFT source correction: q=1 standard parafermionic spin','SOURCE CORRECTION DRAFT, pending independent review. For the standard FK edge observable F(e)=E[exp(i sigma W_gamma(e,e_b)) 1_{e in gamma}], with winding measured in radians and 0<sigma<1, the parameter convention sin(pi sigma/2)=sqrt(q)/2 gives sigma=1/3 at q=1; sigma=2/3 corresponds to q=3. The existing C0017 attempt card says q=1 has spin 2/3. This correction concerns that parameter only, not the conjectural observable limit or the remaining conformal-invariance gap. Primary reference: Duminil-Copin, Conjecture 1 Eq.(3.3), https://www.ihes.fr/~duminil/publi/divergenceFK.pdf .',['Standard stated edge-observable and winding convention','0<q<4, 0<sigma<1; specialize q=1'])
])
relations=[{'from_key':k,'to_key':'def-cells','kind':'depends_on','rationale':'The stated cell result uses the same finite terminal-partition and exterior-event framework.'} for k in ['weighted-comparison','finite-obstruction','pair-counterexample']]
relations.extend([
{'from_key':'pair-counterexample','to_key':'pair-route','kind':'refutes','rationale':'The exact star calculation matches every pair probability but separates the crossing event a connected to {b,c}.'},
{'from_key':'dependence-counterexample','to_key':'dependence-route','kind':'refutes','rationale':'Identical marginals give zero marginal distance while the explicit Boolean event differs by 1/2.'},
{'from_key':'gap','to_key':'weighted-comparison','kind':'depends_on','rationale':'The displayed unresolved total error is exactly the bound in the weighted comparison, plus the two representation errors.'},
{'from_key':'gap','to_existing_logical':target,'kind':'cites','rationale':'The source target requires square-bond Cardy limits and SLE6; this draft identifies only an unresolved crossing-transfer route.'},
{'from_key':'spin-correction','to_existing_logical':old_attempt,'kind':'refutes','rationale':'Scoped refutation of the exact sentence that q=1 has standard spin sigma=2/3. The primary parameter relation instead gives 1/3. The historical missing-limit assessment is preserved.'}
])
bundle={'spec':'mathbrain-draft-v1','author_agent':'w417','bundle_slug':'c0017-independent-cell-bridge-and-spin-correction-001','entries':entries,'relations':relations}
keys={e['key'] for e in entries}
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
assert len(keys)==len(entries)<=200
for e in entries:
    assert e['kind'] in {'concept','definition'} and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
for r in relations:
    assert r['from_key'] in keys and r['kind'] in allowed
    assert r.get('to_key') in keys or r.get('to_existing_logical') in existing
deps={k:[] for k in keys}
for r in relations:
    if r['kind']=='depends_on' and 'to_key' in r:
        deps[r['from_key']].append(r['to_key'])
def visit(k,path):
    assert k not in path,'depends_on cycle'
    for nxt in deps[k]:
        visit(nxt,path|{k})
for k in keys:
    visit(k,set())

payload=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
(ROOT/'bundle_001.json').write_text(payload,encoding='utf-8')
inbox=Path('~/math-brain-inbox/w417')
assert inbox.resolve()==Path('~/math-brain-inbox/w417').resolve()
inbox.mkdir(exist_ok=True)
destination=inbox/'bundle_001.json'
part=inbox/'bundle_001.part'
assert not destination.exists() and not part.exists(),'preserve existing inbox artifacts'
with part.open('x',encoding='utf-8') as out:
    out.write(payload)
part.rename(destination)
assert destination.read_text(encoding='utf-8')==payload

entrymap={e['key']:e for e in entries}
with (ROOT/'EDGE_EVIDENCE.jsonl').open('w',encoding='utf-8') as out:
    for i,r in enumerate(relations,1):
        target_statement=entrymap[r['to_key']]['statement'] if 'to_key' in r else existing[r['to_existing_logical']]['body']
        row={'id':f'w417-edge-{i:02}','relation':r,'from_statement_quoted':entrymap[r['from_key']]['statement'],'to_statement_quoted':target_statement,'independent_reviewer':'w419 pending','status':'draft'}
        out.write(json.dumps(row,ensure_ascii=False)+'\n')
now=dt.datetime.now(dt.timezone.utc).isoformat()
state={'submitted':{'state':True,'utc':now,'path':str(destination),'mesh_exclusive_claim':'clm-ae23fac327'},'reviewed':{'state':False,'referee':'w419','note':'w418 reports scoped KEEP on L1; complete referee verdict pending.'},'ingested':{'state':False,'note':'Worker did not invoke the live integrator.'},'retrievable':{'state':False,'note':'New nodes have not been tested in the live recall store.'},'schema_checked':True,'entries':len(entries),'relations':len(relations),'promoted_theorems':0,'promoted_lemmas':0}
(ROOT/'BUNDLE_STATE.json').write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
hook={'id':'c0017-spin-w417-01','area':'math','event':'stage-start','cue':'A proof uses the standard FK edge parafermion with q=1 and spin sigma=2/3','fire_when':'The live C0017 attempt card supplies q=1 and standard spin 2/3','silent_when':'A q=3 card uses standard spin 2/3, or another winding convention is explicitly defined','text':'For F(e)=E[exp(i sigma W)1{e in gamma}], check sin(pi sigma/2)=sqrt(q)/2 before using the card. At q=1 the standard spin is 1/3. Keep the winding convention explicit; a contour identity alone does not identify the scaling limit.','evidence':'~/brain_workers/w417/REPAIR_MEASUREMENT.json; residual in q 2.0 before, 2.22e-16 after; exact C0017 attempt logical_id in MATH_BRAIN_RETRIEVAL.json','proposer':'w417'}
assert len(hook['text'])<=300
(ROOT/'HOOK_PROPOSALS.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
(ROOT/'PROGRESS_ROW.json').write_text(json.dumps({'agent':'w417','row':'S1.C0017','event':'C0017 independent-cell bridge packet: three partial lemmas, one dependence counterexample, a measured spin correction; G1 unresolved; draft bundle submitted for review.','evidence':str(ROOT/'REVIEW_PACKET.md'),'posting_state':'Prepared locally for the authorized integration contact; not written to a shared progress file by this worker.'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(state,indent=2))
