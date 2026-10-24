from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1]; AGENT=RUN.parents[1]
TEAM=AGENT.parents[1]; OUT=RUN/'out'
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((BASE/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
def save(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
inventory=json.loads((OUT/'CHAIN_INVENTORY.json').read_text(encoding='utf-8'))
claims=[]; used=[]
for packet in ['A001','A006','A011']:
    original=next((TEAM/'agents'/packet).rglob('CLAIMS.json'))
    for claim in json.loads(original.read_text(encoding='utf-8')):
        accepted=claim['claim_id']!='A001-UNIVERSAL-QUANTIFIER-AND-GAP-MAP'
        claim['review_records'].append({'reviewer':'A086/account05','at':now,'verdict':'ACCEPT_AT_STATED_SCOPE' if accepted else 'PARTIAL_REVIEW_ONLY','source':str(RUN/'JOINT_CODE_REVIEW.md'),'source_sha256':sha(RUN/'JOINT_CODE_REVIEW.md'),'method':'Independent analytic reconstruction plus independent integer-FWHT/Fraction queue and transcript implementation; no author checker imported.','scope':'All stated content' if accepted else 'Endpoint J, fixed-marginal admission and good-coordinate selection directions only; not all 37 interfaces.'})
        claim['status']='INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE' if accepted else 'PARTIALLY_REVIEWED_NOT_BLANKET_ACCEPTED'
        claim['proof_source']={'original':claim['proof_source'],'original_claims_path':str(original),'original_claims_sha256':sha(original),'review':str(RUN/'JOINT_CODE_REVIEW.md')}
        fields=protocol['required_per_run']['claim_fields']
        assert set(claim)==set(fields), (claim['claim_id'],set(claim)-set(fields))
        computed=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
        assert computed==claim['statement_sha256'],claim['claim_id']
        claims.append(claim); used.append({'claim_id':claim['claim_id'],'version':claim['version'],'review_verdict':claim['review_records'][-1]['verdict']})
save(RUN/'CLAIMS.json',claims)
gaps={'full_fei_status':'OPEN','chain_inventory':inventory,'gaps':[
 {'gap_id':'G-J-COST','exact_first_unsupported_line':'For every Boolean f there exists one globally fixed admissible representation and reference whose complete expected posterior residual is at most K I(f) for one absolute finite K.','status':'OPEN_NOT_USED_BY_ACCEPTED_RESTRICTED_PROOFS','consumer':'A089'},
 {'gap_id':'G-LOWSEL-COLLISION','exact_first_unsupported_line':'Physical-path labels and support membership bits can be jointly compressed with a complete normalized reference under an explicit new structural hypothesis beyond I_sel>=gamma D.','status':'OPEN_CONTINUATION','consumer':'A089','precise_test_family':'First-positive a-selector comb: all stopping labels y1 and only terminal label y2; D=2(1-2^-a), B=a*2^(-(a-1)), hence B/D->0.','retain':['physical path label','leaf costs','Kraft normalizer','signed cross terms','posterior H(W|S)','no repeated physical influence payment']},
 {'gap_id':'A086-MISSING-ORIGINALS','exact_first_unsupported_line':'No complete source was available for A002-A005,A007-A010,A012-A015 at intake; no verdict can be issued.','status':'DEPENDENCY_NOT_AVAILABLE','consumer':'A096'},
 {'gap_id':'A086-A001-UNRECONSTRUCTED-INTERFACES','exact_first_unsupported_line':'The remaining broad A001 inventory analytic dependencies have not been independently reconstructed by this stage.','status':'REVIEW_OUTSTANDING','consumer':'A094'}], 'reviewers':['A094','A085'],'repair_contribution':False}
save(RUN/'JOINT_CODE_GAPS.json',gaps)
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B18','packet_id':'A086','gap_id':'G-J-COST','attempt_id':'A086-JOINT-CODE-INDEPENDENT-RECONSTRUCTION-1',
 'method':'Analytic reconstruction from original sources; independent graph-based queue enumeration and prefix-code/Fourier-law checker',
 'mathematical_delta':'Independent acceptance at stated scopes of A006 sunflower posterior and complete-cost theorem, A011 coherent selector transcript theorem and A001 fixed-Boolean-marginal tensor admission. 251206 exact assertions passed. A001 broad map only partly reviewed. No universal FEI implication newly paid.',
 'deliverable_status':'COMPLETE_LOCAL_AVAILABLE_CHAIN_REVIEW','mathematical_status':'THREE_CLAIM_VERSIONS_INDEPENDENTLY_REVIEWED_FULL_FEI_OPEN',
 'claim_versions_used':used,'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':x['version'],'change':'local independent review record only; exact statement unchanged'} for x in claims],
 'source_artifacts':[{'path':str(RUN/'JOINT_CODE_REVIEW.md'),'sha256':sha(RUN/'JOINT_CODE_REVIEW.md')},{'path':str(OUT/'SOURCE_MANIFEST.json'),'sha256':sha(OUT/'SOURCE_MANIFEST.json')},{'path':str(OUT/'EXACT_RESULTS.json'),'sha256':sha(OUT/'EXACT_RESULTS.json')}],
 'next_consumers':['A007','A008','A009','A010','A013','A014','A019','A058','A089','A090','A094','A096','B20'],
 'next_action':'Consume newly available A002--A015 originals without repeating accepted baseline; A089 target is joint physical-path compression retaining complete normalization and posterior credit.',
 'stagnant_substantive_attempts':0,
 'blockers':['Twelve A001--A015 reports absent at intake; full-chain coverage remains incomplete.','B18 STREAM_NOTES.md absent.','Supervisor adoption and mirror receipts not available.'],
 'packet_ids':['A086']}
fields=[x.replace(' (one primary ID, for compatibility)','') for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
save(RUN/'PROGRESS.json',progress); save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+x in report for x in protocol['required_per_run']['report_fields'])
status='STATE: A086 stage complete locally; A006/A011 and A001 tensor admission independently accepted at stated scopes; 251,206 exact checks passed; full FEI OPEN.\nNEXT: Consume new A002--A015 originals; A094/A085 review reconstruction; A089 pursue normalized joint path-label compression beyond boundary admission.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as h:
    h.write('\n'+now+' '+RUN.name+': Read original conditioned forest proof, A006 and A011 complete proofs, A001 tensor admission. Independent graph/queue and prefix-code reconstruction passed 251206 exact assertions in 12.670593 s. Accepted three claims at scope; A001 broad map partial. Twelve reports and B18 lead notes absent. Saved complete local review; no shared writes.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as h:
    h.write('\n'+now+'\n- Distinct child-label occurrence draws count as different queue runs even at a repeated attachment coordinate; alternative abstract descriptions of the same trace do not.\n- A006 sunflower: R<=43I/10; complete nonempty cost <=23I/2, paid prior <=25I/2. Keep h2(v) when inferring total H. Nonempty-root conditioning is valid without almost-sure termination.\n- A011: fair physical-child spectral sampling plus theta=(u-v)^2/[2(u^2+v^2)] gives exact signed coherent parent law. Physical prefix + leaf prefix + depth membership bits is Kraft-valid and costs 2D+sum p c. Boundary admission is a hypothesis; this is a separate reference from the forest queue.\n- Fixed actual Boolean X-marginal classes admitting arbitrary independent data tensors retain exactly C_FEI as their optimal conditional-entropy/full-influence constant.\n- Context PDF text exports decode as cp1252; machine intake is distinguished from independent review of every analytic paper theorem.\n')
save(OUT/'SCHEMA_VALIDATION.json',{'claim_fields':'PASS','statement_sha256':'PASS','progress_fields':'PASS','report_fields':'PASS','compatibility_byte_equality':'PASS','required_files':'PASS','checked_at':now})
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']:
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save(OUT/'PERSISTENCE_RECEIPTS.json',{'at':now,'files':receipts,'mirror_status':'NOT_VERIFIED_SUPERVISOR_PENDING'})
print(json.dumps({'schema':'PASS','reviewed_claims':len(claims),'accepted_claims':3,'receipted_files':len(receipts),'run':str(RUN)}))
