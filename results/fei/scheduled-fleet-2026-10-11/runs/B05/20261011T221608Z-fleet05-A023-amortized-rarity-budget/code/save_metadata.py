from pathlib import Path
from fractions import Fraction as F
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
HOME_TASK=ROOT.parents[1]
BASE=Path('~/mop_fei100/reports/fei-2026-10-11')
SUP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
TEAM=Path('~/brain_workers/FEI100_20261011')
def write(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    proto=json.loads((BASE/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
    # Exact rational constants from the analytic certificates; no decimal signs.
    cc=F(81,56); ee=F(65,24)
    K=1+cc+8*cc/ee; full=K+3*cc; direct=4+2*cc*(1+1/ee)
    assert K<7 and full<12 and direct<8
    write('out/constant_certificate.json',{'ln2_lower':'56/81','e_lower':'65/24','K_upper':str(K),'full_ledger_coefficient_upper':str(full),'direct_entropy_coefficient_upper':str(direct),'strict_bounds':[7,12,8],'arithmetic':'Fraction; strict analytic lower bounds proved in REPORT.md'})
    files=[BASE/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
    files += [SUP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
    files += list((SUP/'sources').glob('*.md'))
    files += list((BASE/'runs').glob('**/REPORT.md'))
    files += list((TEAM/'context').glob('*.txt'))
    files += [TEAM/'BOARD.md']
    old=TEAM/'agents/A021/runs/20261011T214020Z-fleet05-A021-rare-core-asymptotics'
    files += [old/'REPORT.md',old/'CLAIMS.json']
    old22=TEAM/'agents/A022/runs/20261011T215800Z-fleet05-A022-one-point-surgery'
    files += [old22/'REPORT.md',old22/'POINT_SURGERY.tex']
    receipts=[]
    for p in files:
        raw=p.read_bytes()
        receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'scope':'byte-loaded provenance; passages inspected are listed in REPORT.md'})
    write('out/source_receipts.json',{'sources':receipts,'lead_notes':{'path':str(TEAM/'claude/B05/STREAM_NOTES.md'),'exists':(TEAM/'claude/B05/STREAM_NOTES.md').exists()},'note':'This receipt is not a full-paper independent audit.'})
    claims=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8'))
    for q in claims:
        assert hashlib.sha256(json.dumps({'statement':q['exact_statement'],'hypotheses':q['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()==q['statement_sha256']
        q['review_records'].append({'reviewer':'A023','verdict':'ACCEPT_AT_STATED_SCOPE','source':str(ROOT/'REVIEW_A021.md'),'method':'separate raw-truth-table FWHT/edge checker and analytic series reconstruction; no repair contributed','registry_adoption':'PENDING_SUPERVISOR'})
        q['status']='INDEPENDENTLY_REVIEWED_LOCALLY_ACCEPT_AT_STATED_SCOPE'
    statement='For every Boolean core g on a uniform cube, every r>=1 fresh point controls, p=2^-r and a=1-Eg, the finite control-first tree has exclusive queried influence rpa, terminal influence pI(g), terminal entropy pH(g), and genuine magnitude-mismatch/KL debt sum_v w_v J_v <=(1+1/ln2+8/(e ln2))rpa<7rpa. Its complete sufficient ledger sum_v w_v(J_v+3mu_v/ln2)+pH(g)<=12rpa+pH(g), and directly H(1+A_r(g-1))<=8rpa+pH(g). For any finite disjoint product of such activations with cores selecting an arbitrary even-k>=4 bent function or its one-vertex flip, the control-first J+terminal is <=7I and full sufficient ledger <=12I; selector-first J+terminal <=8I and full sufficient ledger <=13I; H<=8I. Parameters r,k,vertices,bent seeds and product count are independent. Each control event is billed once and all terminal entropy is included.'
    new={'claim_id':'A023-FIRST-REVELATION-BIASED-CONTROL-LEDGER','version':1,'exact_statement':statement,'hypotheses':['uniform physical cube and bit entropy','fresh point-control block disjoint from its core','J_v uses genuine magnitude/minority mismatch, not signed disagreement at negative-mean endpoint','unconditional terminal family: arbitrary bent seed, even k>=4, one actual vertex flip and a fresh fair selector','multi-event theorem requires disjoint physical component support'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A023'],'proof_source':str(ROOT/'REPORT.md'),'proof_dependencies':[],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A028','A029','A037','A064','A065','A087','A094','B20']}
    claims.append(new)
    write('CLAIMS.json',claims)
    progress={'protocol_revision':proto['revision'],'run_id':ROOT.name,'stream':'B05','packet_id':'A023','gap_id':'G-R-MISMATCH-FIRST-REVELATION','attempt_id':'A023-1','method':'independent A021 review; exact biased activation spectrum; minority/KL control-path summation; separate terminal bank; two query orders; disjoint product extension','mathematical_delta':'Complete arbitrary-bias control J ledger <7 queried influence, full sufficient ledger <12; unconditional bent-surgery product H<=8I; both query orders paid; negative-mean endpoint guarded. Two A021 version-1 claims independently reconstructed without repair.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'PACKET_RESOLVED_FOR_DECLARED_FAMILY; UNIVERSAL_FEI_OPEN; NEW_CLAIM_REVIEW_PENDING','claim_versions_used':[],'claims_created_or_changed':[q['claim_id']+'@'+str(q['version']) for q in claims],'source_artifacts':['REPORT.md','REVIEW_A021.md','FIRST_REVELATION_LEDGER.md','code/check.py','out/FROZEN_SPEC.json','out/validation.json','out/constant_certificate.json','out/source_receipts.json'],'next_consumers':['A028','A029','A037','A064','A065','A087','A094','B20'],'next_action':'Analyze an explicit pair of overlapping control subcubes sharing one data core, deriving the physical-coordinate ownership correction while preserving the terminal account.','stagnant_substantive_attempts':0,'blockers':['B05 lead notes absent; no universal overlapping-event account or terminal-admission theorem proved'],'packet_ids':['A023']}
    write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
    expected_progress={'packet_ids' if x.startswith('packet_ids ') else x for x in proto['required_per_run']['progress_fields']}
    assert set(progress)==expected_progress
    for q in claims: assert set(q)==set(proto['required_per_run']['claim_fields'])
    report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
    for title in proto['required_per_run']['report_fields']: assert '# '+title in report
    write('out/schema_check.json',{'progress_fields_exact':True,'claim_fields_exact':True,'report_fields_present':True,'packet_delta_equals_progress':True,'status':'PASS'})
    (HOME_TASK/'STATUS.md').write_text('STATE: A023 packet complete locally: arbitrary-bias first-revelation KL ledger and both bent-surgery tree orders paid; H<=8I on disjoint multi-event family; 44,452 exact checks; A021 independently accepted locally; full FEI OPEN.\nNEXT: A087/A094 review new claim; A029/A064 derive an ownership correction for two overlapping control events sharing a core, preserving terminal cost.\n',encoding='utf-8')
    with (HOME_TASK/'WORKLOG.md').open('a',encoding='utf-8') as h:
        h.write('\n2026-10-11/12 UTC stage '+ROOT.name+': Read protocol and start board; B05 lead notes absent. Independently reconstructed A021 both v1 claims without repair. Proved arbitrary-bias control J ledger <7rpa, full sufficient bill <12rpa plus terminal; direct entropy <8rpa plus terminal. Closed arbitrary bent one-point selector activations and their disjoint products; control-first/selector-first full ledgers <=12I/13I. Exact frozen grid passed 44,452 assertions in 3.9298s. Universal structural admission and overlapping coordinate ownership remain open. Artifacts saved locally only.\n')
    with (HOME_TASK/'LEARNED.md').open('a',encoding='utf-8') as h:
        h.write('\n- For F=1+A_r(g-1), a=1-Eg, p=2^-r: queried influence rpa; terminal pI(g), pH(g). At active node u=2^-s, signed J=ua-(ua)^2+(ua)^2 log2((1-2ua+2(ua)^2)/(ua)^2). Genuine minority differs at the last node when Eg<0; use Jminor<=L<=Jsigned+c ua.\n- Summing the retained KL debt yields Jtree<7rpa and full J+3c mu<12rpa. Direct actual-spectrum entropy gives H(F)<=pH(g)+8rpa. No arbitrary-terminal FEI is inferred.\n- A fair selector between any bent k-bit function (k>=4 even) and its one-point flip has I>=7k/16, H<=k+1, hence H/I<3. Activations and disjoint products have H<=8I with complete terminal payment. Two tree orders both work despite the bad isolated selector.\n- First event account is opened once, descendants contribute subbills but cannot reuse its exclusive control coordinates. Tensor factorization preserves node J and mu; overlapping events need a fresh ownership proof.\n- Independent A021 review found no gap in its two version-1 claims; original files and all shared indices remained read-only.\n')
    artifacts=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p.name!='persistence_receipts.json':
            assert p.stat().st_size<20_000_000
            artifacts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
    write('out/persistence_receipts.json',{'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':artifacts,'rolling_files':[{'path':str(HOME_TASK/n),'sha256':sha(HOME_TASK/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'local_save_verified':True,'supervisor_copy_verified':False,'mirror_verified':False,'new_claim_independently_reviewed':False})
    print(json.dumps({'schemas':'PASS','source_files':len(receipts),'artifact_files':len(artifacts),'claims':len(claims),'local_persistence':'verified','K_upper':str(K),'full_upper':str(full),'direct_upper':str(direct)}))
if __name__=='__main__':main()
