from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, subprocess
RUN=Path(__file__).resolve().parents[1]; ROOT=RUN.parent.parent; TEAM=ROOT.parent.parent
OLD=ROOT/'runs/20261014T031358Z-account05-A099-candidate-assembly'
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p): return p.read_text(encoding='utf-8-sig')
def obj(p): return json.loads(read(p))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v): (RUN/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def ar(a,r): return TEAM/'agents'/a/'runs'/r
def cs(p): return {c['claim_id']:c for c in obj(p/'CLAIMS.json')}
a97=ar('A097','20261014T050248Z-account05-A097-cross-route-transfer')
a98=ar('A098','20261014T054007Z-account05-A098-resource-reallocation')
a96=ar('A096','20261014T042803Z-account05-A096-live-gap-ledger')
a100=ar('A100','20261014T034838Z-account05-A100-release-and-continuation-ledger')
stamp=datetime.now(timezone.utc).isoformat(); protocol=obj(BASE/'EXECUTION_PROTOCOL.json')
claims=cs(OLD); sources=[]
for r,names in [(a97,['DERIVATION.md','CLAIMS.json']),(a98,['DERIVATION.md','CLAIMS.json']),(a96,['DERIVATION.md','CLAIMS.json']),(a100,['REVIEW.md','REPORT.md','CLAIMS.json']),(OLD,['CANDIDATE_MANUSCRIPT.tex','CLAIMS.json','out/PROOF_DEPENDENCIES.json','out/SOURCE_RECEIPTS.json'])]:
    for n in names:
        p=r/n; sources.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'usage':'Complete source derivation or scoped review; retained baseline'})
for p in [BASE/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B20/STREAM_NOTES.md',ROOT/'STATUS.md']:
    sources.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'usage':'Stage intake'})
save('out/SOURCE_RECEIPTS.json',{'sources':sources,'retained_manifest':str(OLD/'out/SOURCE_RECEIPTS.json'),'acceptance_by_receipt':False})
(RUN/'out/BOARD_SNAPSHOT.md').write_text(read(TEAM/'BOARD.md'),encoding='utf-8')
floor=cs(a97)['A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK']; reviewed=cs(a98)[floor['claim_id']]
assert floor['exact_statement']==reviewed['exact_statement'] and floor['hypotheses']==reviewed['hypotheses']
assert floor['statement_sha256']==reviewed['statement_sha256']
floor['review_records']=reviewed['review_records']
def audit(c,locator,method,validation):
    c['review_records'].append({'reviewer':'A099','timestamp':stamp,'verdict':'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR','scope':c['exact_statement'],'proof_source':str(RUN/'CANDIDATE_MANUSCRIPT.tex'),'locator':locator,'method':method,'validation_source':str(RUN/validation),'source_statement_sha256':c['statement_sha256'],'reviewer_contributed_repair':False})
assert obj(RUN/'out/EXACT_FLOOR.json')['status']=='PASS'
audit(floor,'thm:floor','Independent all-parameter complete-reference and one-bank proof, direct signed-character/physical-edge Fraction reconstruction and prime-log identities; product-terminal clause analytically reconstructed','out/EXACT_FLOOR.json')
floor['status']='TWO_INDEPENDENT_FULL_SCOPED_ACCEPTANCES_A098_A099_HEREDITARY_TRANSPORT_OPEN'
claims[floor['claim_id']]=floor
newids=[floor['claim_id']]
for cid in ['A096-NONFLAT-POINT-QUOTIENT-REMAINDER','A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION']:
    claims[cid]=cs(a96)[cid]; newids.append(cid)
binary=claims['A073-NONZERO-ERASURE-BINARY-REMAINDER']; br=cs(a100)[binary['claim_id']]
assert binary['exact_statement']==br['exact_statement'] and binary['hypotheses']==br['hypotheses']
for rr in br['review_records']:
    if rr.get('reviewer')=='A100':
        rr['original_source_statement_sha256']=binary['statement_sha256']; rr['review_copy_statement_sha256']=br['statement_sha256']
        if not any(r.get('reviewer')=='A100' for r in binary['review_records']): binary['review_records'].append(rr)
binary['status']='TWO_INDEPENDENT_FULL_SCOPED_ACCEPTANCES_A098_A100_REMAINDER_ONLY'
jensen=cs(a100)['A100-BINARY-REMAINDER-JENSEN-BOUND']
cert={'PASS':77**4<2*65**4,'left':77**4,'right':2*65**4,'R_at_quarter':'77/65','derivative_numerator_lower':'31/64','symbolic_gap':'(1+x)(1+x^2/4)-(1+x-3x^2/4)=x^2+x^3/4','scope':'Scalar certificate plus complete Jensen proof in sec:jensen, no floating-point search'}
assert cert['PASS']; save('out/JENSEN_CERTIFICATE.json',cert)
audit(jensen,'sec:jensen','Independent weighted Jensen algebra, all-parameter derivative and logarithm inequalities, exact integer certificate and product-factor cancellation','out/JENSEN_CERTIFICATE.json')
jensen['status']='ONE_INDEPENDENT_FULL_SCOPED_ACCEPTANCE_A099_SECOND_PENDING'; claims[jensen['claim_id']]=jensen; newids.append(jensen['claim_id'])
hashes=[]
for c in claims.values():
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    raw=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    canonical=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    envelope=hashlib.sha256(json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    assert c['statement_sha256'] in [raw,canonical,envelope],c['claim_id']
    hashes.append({'claim_id':c['claim_id'],'version':c['version'],'recorded':c['statement_sha256'],'raw':raw,'canonical':canonical,'envelope':envelope})
save('CLAIMS.json',list(claims.values()));save('out/HASH_CONVENTIONS.json',hashes)
dag=obj(OLD/'out/PROOF_DEPENDENCIES.json')
labels=['thm:floor','sec:childbank','sec:childbank','sec:jensen']
for cid,label in zip(newids,labels):
    c=claims[cid]
    deps=['COMPLETE'] if cid==floor['claim_id'] else ['A073-NONZERO-ERASURE-BINARY-REMAINDER'] if cid==jensen['claim_id'] else ['NORMALIZED-DERIVATIVE-REFERENCE']
    dag['nodes'].append({'claim_id':cid,'version':c['version'],'proof_dependencies':deps,'tex_label':label,'statement_sha256':c['statement_sha256'],'scope':c['status']})
dag['floor_boundary']='Actual descendant reference/normalizer and reset funded from same remaining bank; Boolean family closure alone is insufficient'
save('out/PROOF_DEPENDENCIES.json',dag)
save('out/CONSUMED_REVIEWS.json',{'reviews':[{ 'claim_id':c['claim_id'],'version':c['version'],'status':c['status'],'review_records':c['review_records']} for c in claims.values()],'integrated_manuscript_audits':'BOTH_PENDING','source_A086_broad_subprobability_theorem':'NOT_IMPORTED; required special mixture proof reconstructed locally'})
tex=read(OLD/'CANDIDATE_MANUSCRIPT.tex').replace('14 October 2026; assembly version 4','14 October 2026; assembly version 5')
marker='\\section{Dependencies, review and sources}'
assert marker in tex;tex=tex.replace(marker,read(RUN/'STAGE5_ADDITIONS.tex')+'\n'+marker)
tex=tex.replace('acceptance. The fixed-degree obstruction is retained at author scope.','acceptances by A098 and A100. The fixed-degree obstruction is retained at author scope.')
refs=r'''
\bibitem{A097e} A097, \emph{Negative-cell floor with an actual source bank},
run \path{20261014T050248Z-account05-A097-cross-route-transfer}, DERIVATION Sections 1--5; original version 1.
\bibitem{A098e} A098, \emph{Independent full reconstruction of the negative-cell floor},
run \path{20261014T054007Z-account05-A098-resource-reallocation}, DERIVATION and CLAIMS; no repair.
\bibitem{A096e} A096, \emph{Non-flat quotient remainder and sharp loss-only child-bank threshold},
run \path{20261014T042803Z-account05-A096-live-gap-ledger}, DERIVATION; two original version-1 claims at author scope.
\bibitem{A100e} A100, \emph{Binary remainder and Jensen sharpening},
run \path{20261014T034838Z-account05-A100-release-and-continuation-ledger}, REVIEW: full original A073 acceptance and separate version-1 refinement.
'''
tex=tex.replace('\\end{thebibliography}',refs+'\\end{thebibliography}')
(RUN/'CANDIDATE_MANUSCRIPT.tex').write_text(tex,encoding='utf-8')
intake=read(RUN/'out/INTAKE.md')+'\nSubsequently read A100 actual REVIEW.md in full, REPORT math and CLAIMS in full. Adopted its scoped A073 acceptance with original digest preserved, and independently reconstructed its separate Jensen refinement. Missing DERIVATION.md is not a proof input.\n'
(RUN/'out/INTAKE.md').write_text(intake,encoding='utf-8')
p=obj(OLD/'PROGRESS.json');p.update(run_id=RUN.name,attempt_id='A099-assembly-v5',method='Source-complete assembly and independent supplied-reference floor/Jensen reconstruction; preserve actual child-bank obstruction',mathematical_delta='Negative-cell floor pays full reference change and erased edges from one supplied source bank, CE<=c+10(C+E+J), K=2C0+10; two scoped audits A098/A099. Jensen gives each binary quotient remainder <e/8 and summed loss <delta^2/(2 ln2). A096 distinguishes root quotas from actual child surplus with sharp loss-only threshold five. Universal descendant reference transport remains open.',claim_versions_used=[{'claim_id':x['claim_id'],'version':x['version']} for x in dag['nodes']],claims_created_or_changed=[{'claim_id':cid,'version':claims[cid]['version'],'change':'Original statement preserved; assembled complete proof and explicit scoped review status'} for cid in newids+[binary['claim_id']]],source_artifacts=['CANDIDATE_MANUSCRIPT.tex','STAGE5_ADDITIONS.tex','FROZEN_SPEC.json','out/EXACT_FLOOR.json','out/PILOT.json','out/JENSEN_CERTIFICATE.json','out/SOURCE_RECEIPTS.json','out/CONSUMED_REVIEWS.json','out/PROOF_DEPENDENCIES.json'],next_consumers=['B20','A097','A096','A073','A100','A094','A085','A098'],next_action='A097/A096 construct descendant incoming reference after an actual active-bit restriction, charging normalizer/reset and terminal row to the same remaining bank; A094/A085 independently audit full assembly.',blockers=['Hereditary incoming-reference transport from same remaining bank open','Universal normalized terminal seed KL/collision payment open','Both integrated-chain audits pending'],mathematical_status='TWO_SCOPED_FLOOR_AUDITS_UNIVERSAL_HEREDITARY_PAYMENT_OPEN')
save('PROGRESS.json',p);save('PACKET_DELTA.json',p)
build=[]
exe=Path(r'~\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.EXE')
for i in range(2):
    try:
        z=subprocess.run([str(exe),'--disable-installer','-interaction=nonstopmode','-halt-on-error','-output-directory=out','CANDIDATE_MANUSCRIPT.tex'],cwd=RUN,capture_output=True,text=True,timeout=45)
        (RUN/f'out/BUILD_PASS_{i+1}.txt').write_text(z.stdout+z.stderr,encoding='utf-8')
        build.append({'pass':i+1,'returncode':z.returncode})
        if z.returncode: break
    except subprocess.TimeoutExpired:
        build.append({'pass':i+1,'timeout_seconds':45});break
log=read(RUN/'out/CANDIDATE_MANUSCRIPT.log') if (RUN/'out/CANDIDATE_MANUSCRIPT.log').exists() else ''
save('out/VALIDATION.json',{'build':build,'overfull_boxes':log.count('Overfull'),'exact_floor':obj(RUN/'out/EXACT_FLOOR.json'),'jensen':cert,'integrated_audits':'PENDING'})
print(json.dumps({'claims':len(claims),'DAG_nodes':len(dag['nodes']),'open_leaves':len(dag['open_leaves']),'build':build,'overfull_boxes':log.count('Overfull')}))
