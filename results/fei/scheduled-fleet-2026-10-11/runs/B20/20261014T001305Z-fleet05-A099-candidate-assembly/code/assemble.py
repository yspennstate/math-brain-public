"""A099 v3 assembly and scoped review intake; writes only inside A099."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,subprocess
RUN=Path(__file__).resolve().parents[1]; ROOT=RUN.parent.parent; TEAM=ROOT.parent.parent
OLD=ROOT/'runs/20261012T044129Z-fleet05-A099-candidate-assembly'
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
assert ROOT.name=='A099'
def read(p):return p.read_text(encoding='utf-8-sig')
def obj(p):return json.loads(read(p))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):
    path=RUN/p;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=obj(BASE/'EXECUTION_PROTOCOL.json'); rid=RUN.name; stamp=datetime.now(timezone.utc).isoformat()
a90=TEAM/'agents/A090/runs/20261013T213537Z-fleet05-A090-independent-reconstruction'
a96=TEAM/'agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger'
a97=TEAM/'agents/A097/runs/20261013T222610Z-fleet05-A097-cross-route-transfer'
receipts=[]
def pin(p,scope):
    assert p.is_file(),str(p)
    receipts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':scope})
for p in [BASE/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B20/STREAM_NOTES.md',ROOT/'STATUS.md',ROOT/'LEARNED.md',OLD/'CANDIDATE_MANUSCRIPT.tex',OLD/'CLAIMS.json',OLD/'out/SOURCE_RECEIPTS.json',OLD/'out/PROOF_DEPENDENCIES.json',OLD/'out/CONSUMED_REVIEWS.json']:
    pin(p,'stage intake or unchanged baseline retained; not a new independent audit')
(RUN/'out/BOARD_SNAPSHOT.md').write_text(read(TEAM/'BOARD.md'),encoding='utf-8')
for p in [a90/'REPORT.md',a90/'CLAIMS.json',a90/'CHECKPOINT_CORRECTION.md',a90/'RECONSTRUCTION_COMPARISON.md',a90/'out/CHECK.json',a96/'REPORT.md',a96/'CLAIMS.json',a96/'DERIVATION.md',a96/'out/CHECK.json',a97/'REPORT.md',a97/'CLAIMS.json',a97/'DERIVATION.md',a97/'BOUNDARY.md']:
    pin(p,'original proof or scoped review consumed this stage')
save('out/SOURCE_RECEIPTS.json',{'sources':receipts,'retained_baseline_receipts':str(OLD/'out/SOURCE_RECEIPTS.json'),'warning':'Byte identity is not mathematical acceptance; mutable board snapshot preserved.'})

source90={c['claim_id']:c for c in obj(a90/'CLAIMS.json')}
source96={c['claim_id']:c for c in obj(a96/'CLAIMS.json')}
source97=obj(a97/'CLAIMS.json')[0]
low=obj(OLD/'CLAIMS.json')[0]
raw=hashlib.sha256(low['exact_statement'].encode()).hexdigest()
canon=hashlib.sha256(json.dumps({'statement':low['exact_statement'],'hypotheses':low['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert canon==low['statement_sha256'] and raw==source90[low['claim_id']]['statement_sha256']
assert low['exact_statement']==source90[low['claim_id']]['exact_statement']
reviews90=[r for r in source90[low['claim_id']]['review_records'] if r['reviewer']=='A090']
assert len(reviews90)==1 and reviews90[0]['verdict']=='HOLDS_AT_STATED_SCOPE'
low['review_records']=reviews90+[{'reviewer':'A094','verdict':'PENDING'}]
low['status']='ONE_INDEPENDENT_SCOPED_ACCEPTANCE_FULL_CHAIN_AND_SECOND_AUDIT_PENDING'
tail=source90['A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS']
assert tail['exact_statement']==source96[tail['claim_id']]['exact_statement']
review96=[r for r in source96[tail['claim_id']]['review_records'] if r['reviewer']=='A096']
assert len(review96)==1 and review96[0]['verdict']=='ACCEPT_AT_STATED_SCOPE' and not review96[0]['reviewer_contributed_repair']
def review(claim,scope):
    return {'reviewer':'A099','timestamp':stamp,'verdict':'ACCEPT_AT_STATED_SCOPE','independent_method':'Direct physical truth-table character sums, rational prime-log cancellation, and complete analytic reconstruction of occupied edge and likelihood-ratio cases','proof_source':str(RUN/'CANDIDATE_MANUSCRIPT.tex'),'validation_source':str(RUN/'out/EXACT_AUDIT.json'),'scope':scope,'reviewer_contributed_repair':False,'source_statement_sha256':claim['statement_sha256']}
tail['review_records']=review96+[review(tail,'Full all-fixed-tail and arbitrary sublinear cutoff theorem; no finite universal payment or whole assembly acceptance')]
tail['status']='TWO_INDEPENDENT_SCOPED_ACCEPTANCES_A096_A099'
refund=source96['A096-TERMINAL-KL-REFUND-AUDIT']
refund['review_records']=refund['review_records']+[review(refund,'Complete normalized row/joint formulas, oriented tail and cutoff suprema; no terminal-core lower bound')]
refund['status']='ONE_INDEPENDENT_SCOPED_ACCEPTANCE_A099_SECOND_AUDIT_PENDING'
claims=[low,tail,refund,source97]
hashes=[]
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    rawc=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    cc=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert c['statement_sha256'] in (rawc,cc)
    hashes.append({'claim_id':c['claim_id'],'version':c['version'],'recorded':c['statement_sha256'],'raw_UTF8_statement':rawc,'canonical_statement_hypotheses_JSON':cc,'recorded_convention':'canonical JSON' if c['statement_sha256']==cc else 'raw UTF8'})
save('CLAIMS.json',claims)
save('out/HASH_CONVENTIONS.json',{'claims':hashes,'A090_discrepancy_resolution':'A099 v2 uses canonical statement-plus-hypotheses JSON. A090 copied the same text and recomputed its raw UTF8 hash. Both hashes are correct under different conventions; no mathematical statement or version changed.'})
exact=obj(RUN/'out/EXACT_AUDIT.json');assert exact['status']=='PASS' and exact['cases']==96
save('out/CONSUMED_REVIEWS.json',{'low_influence_v2':low['review_records'],'tail_v1':tail['review_records'],'refund_v1':refund['review_records'],'A097_shared_v1':'Author proof assembled; independent audit pending','integrated_chain':'Both full-chain reconstructions remain pending','retained_A098_scope':'H2/T12 only'})

tex=read(OLD/'CANDIDATE_MANUSCRIPT.tex')
tex=tex.replace('12 October 2026; assembly version 2','14 October 2026; assembly version 3')
tex=tex.replace('Independent full-chain reviews by A090 and A094 have not been received.','A090 independently accepts the low-influence fragment; the fixed-tail\noptimal-constant theorem has scoped A096 and A099 reconstructions.\nThe complete integrated chain still awaits both independent audits.')
marker='\\section{C019: finite adaptive stopping trees and one influence budget}'
# Tail and refund precede trees; shared transfer follows the compatible-reference proof.
addition=read(RUN/'ADDITIONS.tex')
first,shared=addition.split('\\section{A097: one shared data bit and the boundary of selector payment}',1)
tex=tex.replace(marker,first+'\n'+marker)
marker2='\\section{Closed B05 compatible-reference calibration, A097 version 1}'
tex=tex.replace(marker2,'\\section{A097: one shared data bit and the boundary of selector payment}'+shared+'\n'+marker2)
oldreview='The integrated assembly and the strengthened low-influence version\nawait two independent complete-chain\nreconstructions, A090 and A094. B20\'s source check is not either\nindependent acceptance.'
newreview='A090 accepts Theorem~\\ref{thm:low} at its exact scope; a second\nindependent acceptance remains pending. Theorem~\\ref{thm:tail} has\nindependent A096 and A099 scoped reconstructions. Proposition~\\ref{prop:refund}\nhas an A099 reconstruction; its second review is pending. The shared-data\ntransfer in Section~\\ref{sec:shared} remains at author scope.\nBoth complete integrated-chain audits remain pending. B20\'s source check\nis not independent acceptance.'
assert oldreview in tex;tex=tex.replace(oldreview,newreview)
refs=r'''
\bibitem{A090c} A090, \emph{Independent low-influence reconstruction and higher-tail completeness},
run \path{20261013T213537Z-fleet05-A090-independent-reconstruction},
REPORT equations (1)--(14), original claim version 1; checkpoint correction retained.
\bibitem{A096c} A096, \emph{Terminal-inclusive conditional-edge refund audit},
run \path{20261013T220343Z-fleet05-A096-live-gap-ledger},
DERIVATION equations (1)--(6), claim version 1; independent acceptance of A090 tail theorem.
\bibitem{A097c} A097, \emph{One-shared-data collision reference transfer},
run \path{20261013T222610Z-fleet05-A097-cross-route-transfer},
DERIVATION Sections 1--4 and BOUNDARY; scoped version 1, independent review pending.
'''
tex=tex.replace('\\end{thebibliography}',refs+'\n\\end{thebibliography}')
(RUN/'CANDIDATE_MANUSCRIPT.tex').write_text(tex,encoding='utf-8')
labels=re.findall(r'\\label\{([^}]+)\}',tex); texrefs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',tex)
assert len(labels)==len(set(labels)) and set(texrefs)<=set(labels)
assert tex.count('\\begin{conjecture}')==4 and '\\input' not in tex
dag=obj(OLD/'out/PROOF_DEPENDENCIES.json')
dag['nodes'] += [
 {'claim_id':tail['claim_id'],'version':1,'proof_dependencies':[],'tex_label':'thm:tail','statement_sha256':tail['statement_sha256']},
 {'claim_id':'NORMALIZED-DERIVATIVE-REFERENCE','version':'retained-C018-identity','proof_dependencies':['DOWNWARD'],'tex_label':'eq:refundbaseline'},
 {'claim_id':refund['claim_id'],'version':1,'proof_dependencies':['NORMALIZED-DERIVATIVE-REFERENCE',tail['claim_id']],'tex_label':'prop:refund','statement_sha256':refund['statement_sha256']},
 {'claim_id':source97['claim_id'],'version':1,'proof_dependencies':['C005','A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER'],'tex_label':'sec:shared','statement_sha256':source97['statement_sha256'],'scope':'Needed packet lemma reconstructed; whole external A086 interface not assumed'}]
dag['open_leaves'][0]['optimal_constant']='K_E exactly, even for every fixed higher-tail/sublinear low-influence cutoff; finiteness still open'
byid={x['claim_id']:x for x in dag['nodes']};done=set();active=set()
def visit(k):
    assert k in byid and k not in active
    if k in done:return
    active.add(k)
    for d in byid[k]['proof_dependencies']:visit(d)
    active.remove(k);done.add(k)
for k in byid:visit(k)
save('out/PROOF_DEPENDENCIES.json',dag)
save('ASSEMBLY_STATUS.json',{'assembly_version':3,'run_id':rid,'full_fei_status':'OPEN','low_v2':'One independent scoped acceptance A090; second pending','tail_v1':'A096 and A099 independent scoped reconstructions, no universal payment','refund_v1':'A099 independent scoped reconstruction; second pending','shared_reference_v1':'Complete author proof included, independent review pending','integrated_independent_audits':'Both pending; no fragment review promoted','frontier':'R_ge2<=K I; equivalently normalized arbitrary seed KL lower bound; signed excess collision needs one terminal reserve','new_broad_candidates':0,'mirror':'NOT_VERIFIED'})
save('CLAIM_EQUIVALENCE_MAP.json',{'retained':obj(OLD/'CLAIM_EQUIVALENCE_MAP.json'),'stage3':['Fixed higher-tail optimal constant equals K_E, including sublinear cutoffs','A096 source M is exactly assembly downward L, not marginal entropy sum','Complete reference KL lower bound is the existing C018 leaf, not a new conjecture','Shared data bit admission differs from overlapping activation controls']})
progress={'protocol_revision':protocol['revision'],'run_id':rid,'stream':'B20','packet_id':'A099','gap_id':'G-A099-ASSEMBLY-C018-C019','attempt_id':'A099-assembly-v3','method':'Consume source-bound scoped audits; independently reconstruct tail and normalized refund with direct character arithmetic; assemble complete shared-data transfer and boundary','mathematical_delta':'A090 acceptance of loss-free low-influence v2 consumed. A090 higher-tail optimal constant equality independently reconstructed by A099, joining A096; A096 terminal KL transport independently reconstructed with seed cost retained. A097 shared-bit reference transfer and unrestricted selector-only Boolean boundary assembled. No finite universal constant gained.','deliverable_status':'COMPLETE_LOCAL_PENDING_INTEGRATED_AUDITS','mathematical_status':'SCOPED_THEOREMS_RECONSTRUCTED_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':n['claim_id'],'version':n['version']} for n in dag['nodes']],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Review/status intake only; exact statement and canonical source ID preserved'} for c in claims],'source_artifacts':['CANDIDATE_MANUSCRIPT.tex','out/CANDIDATE_MANUSCRIPT.pdf','out/EXACT_AUDIT.json','out/HASH_CONVENTIONS.json','out/SOURCE_RECEIPTS.json','out/CONSUMED_REVIEWS.json','out/PROOF_DEPENDENCIES.json'],'next_consumers':['B20','A090','A094','A096','A097','A098','A100','A001','A073'],'next_action':'Audit a signed-Boolean terminal-core KL lower bound using one normalized reference and one influence reserve; A001/A073 review refund, A094 alternate chain auditor','stagnant_substantive_attempts':0,'blockers':['Universal R_ge2 payment open','Arbitrary terminal reference payment and excess collision reserve open','Both integrated audits and second low-v2 audit unobserved'],'packet_ids':['A099']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
exe=Path(r'~\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.EXE')
build=[]
for i in (1,2):
    cmd=[str(exe),'--disable-installer','-interaction=nonstopmode','-halt-on-error','-output-directory=out','CANDIDATE_MANUSCRIPT.tex']
    try:
        p=subprocess.run(cmd,cwd=RUN,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=60)
    except subprocess.TimeoutExpired as exc:
        (RUN/f'out/BUILD_PASS_{i}.txt').write_text('TIMEOUT after 60 seconds; subprocess.run killed and reaped compiler.\n'+str(exc),encoding='utf-8')
        build.append({'pass':i,'command':cmd,'status':'TIMEOUT_60_SECONDS'})
        break
    (RUN/f'out/BUILD_PASS_{i}.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
    build.append({'pass':i,'command':cmd,'returncode':p.returncode})
    if p.returncode:break
log=read(RUN/'out/CANDIDATE_MANUSCRIPT.log') if (RUN/'out/CANDIDATE_MANUSCRIPT.log').exists() else ''
save('out/VALIDATION.json',{'exact_audit':exact,'source_files_pinned':len(receipts),'claim_field_sets':True,'progress_field_set':True,'hash_conventions_checked':hashes,'acyclic_DAG_nodes':len(byid),'four_explicit_open_leaves':True,'TeX_references_resolved':True,'single_source':True,'build':build,'overfull_boxes':log.count('Overfull'),'undefined_references':'undefined references' in log,'full_FEI':'OPEN'})
print(json.dumps({'claims':len(claims),'exact':exact,'DAG_nodes':len(byid),'build':build,'overfull':log.count('Overfull')},indent=2))
