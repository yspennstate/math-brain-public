from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];TASK=ROOT.parents[1]
TEAM=TASK.parents[1]
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,obj):(ROOT/n).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def main():
    proto=json.loads(PROTO.read_text(encoding='utf-8-sig'))
    old=TEAM/'agents/A021/runs/20261011T214020Z-account05-A021-rare-core-asymptotics'
    newer=TEAM/'agents/A021/runs/20261011T232653Z-account05-A021-rare-core-asymptotics'
    lead=TEAM/'claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport'
    prior=TASK/'runs/20261011T221608Z-account05-A023-amortized-rarity-budget'
    sources=[PROTO,TEAM/'BOARD.md',TEAM/'claude/B05/STREAM_NOTES.md',lead/'REPORT.md',newer/'CORRECTION.md',newer/'CLAIMS.json',old/'CLAIMS.json',prior/'REPORT.md',prior/'REVIEW_A021.md',TEAM/'agents/A022/runs/20261011T234607Z-account05-A022-one-point-surgery/REPORT.md',TEAM/'agents/A025/runs/20261011T225648Z-account05-A025-rare-event-counterfamily/REPORT.md']
    # Locate the A025 read report if the supervisor's timestamp differs.
    if not sources[-1].exists():sources[-1]=next((TEAM/'agents/A025/runs').glob('*/REPORT.md'))
    save('out/source_receipts.json',{'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources],'scope':'Sources actually inspected are named in REPORT.md; board is a mutable supervisor snapshot. Prior-stage sources remain unchanged.'})
    c=F(81,56);e=F(65,24)
    assert 1+c+2*c/e<4 and 4+2*c<7 and 4+3*c<9
    assert F(65,24)+F(1,100)<F(11,4)
    assert F(1,2)-c/4==F(31,224)
    save('out/constant_certificate.json',{'c_upper':str(c),'e_lower':str(e),'e_upper':str(F(65,24)+F(1,100)),'constant_child_B_over_d_upper':str(1+c+2*c/e),'entropy_control_coefficient_upper':str(4+2*c),'full_KL_control_coefficient_upper':str(4+3*c),'R_half_strict_lower':'31/224','exposure_lower':'11/32','e_over_8_strict_upper':'11/32','signs':'certified by exact Fraction and analytic series bounds in report'})
    checks=json.loads((ROOT/'out/validation.json').read_text())
    rows=json.loads((ROOT/'out/results.json').read_text())['results']
    certs=json.loads((ROOT/'out/sign_certificates.json').read_text())
    for v in certs:
        if v['classification']=='EQUALITY':assert not v['vector']
        elif v['classification']=='BAD':assert F(v['lower'])>0
        else:assert F(v['upper'])<0
    maxima={}
    for order in checks['max_bad_credit_over_I']:
        maximum=max(F(x['complete'][order]['bad_credit_over_I']) for x in rows)
        assert str(maximum)==checks['max_bad_credit_over_I'][order]
        maxima[order]={'ratio':str(maximum),'witnesses':[{z:x[z] for z in ['s','r','t','k']} for x in rows if F(x['complete'][order]['bad_credit_over_I'])==maximum]}
    for row in rows:
        assert F(row['control_I'])+F(row['stopped']['terminal_I'])==F(row['I'])
        assert row['stopped']['bad_credit']=='0'
    save('out/artifact_check.json',{'classification_endpoints_valid':True,'exact_maxima_reaggregated':maxima,'queried_terminal_partitions_valid':True,'stopped_bad_credit_zero':True,'sign_certificate_count':len(certs),'same_author_recheck':True,'status':'PASS'})
    claims=json.loads((old/'CLAIMS.json').read_text())
    for q in claims:
        q['review_records'].append({'reviewer':'A023','source':str(ROOT/'CORRECTION_A021_REVIEW.md'),'previous_review':str(prior/'REVIEW_A021.md'),'verdict':'RETRACT_V1_EXPANSION_ACCEPTANCE' if q['claim_id'].endswith('EXPANSION') else 'NARROW_REPORT_ACCEPTANCE; EXACT_CLAIM_STILL_HOLDS','independent_repaired_v2_acceptance':False})
        if q['claim_id'].endswith('EXPANSION'):
            q['status']='REFUTED_V1; A023_PRIOR_REVIEW_RETRACTED'
            q['first_unproved_line']='The assertion R(q)<=0 is false; at q=1/2, R(q)>31/224.'
        else:q['status']='EXACT_V1_STATEMENT_HOLDS; ERRONEOUS_ADDITIONAL_REPORT_SIGNS_EXCLUDED'
    statement='For every uniform Boolean core g with a=1-Eg>=11/16 and independent compatible point-control blocks of common width s>=0 and exclusive widths r,t>=1, F=1+A_s(A_r OR A_t)(g-1) has a finite control-first stopping tree with exactly zero strict threshold-4 bad-node odd-face credit before the core terminal. Every queried node has B_v<4d_v for d_v>0. With u=2^-s,p=2^-r,q=2^-t,beta=p+q-pq, I_ctrl=u a[s beta+r p(1-q)+t q(1-p)], I_leaf=u beta I(g), H_leaf=u beta H(g). Thus H(F)<7I_ctrl+H_leaf, genuine minority/KL debt plus H_leaf<=4I_ctrl+H_leaf, and its full 3mu/ln2 allowance plus H_leaf<9I_ctrl+H_leaf. A more general sufficient local condition for a fresh point event against any independent residual event of probability q is a(1-q)>e/8. If g selects any bent sign on even k>=4 bits or its one-vertex flip, H(g)/I(g)<3 and therefore H(F)<7I(F), J+terminal<=4I(F), full sufficient KL ledger<9I(F), uniformly in all widths and k. Common coordinates and the shared core are paid once.'
    hypotheses=['uniform physical cube; Boolean signs; bit entropy','compatible common control literals; disjoint exclusive and common blocks; fresh controls independent of core','stopping after the control union is resolved; no unproved terminal entropy omission','unconditional class bound uses a fair selector between a bent seed and one actual vertex flip, k>=4 even']
    q={'claim_id':'A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A023'],'proof_source':str(ROOT/'REPORT.md'),'proof_dependencies':[],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A021','A025','A028','A029','A064','A087','A094','B05','B20']}
    claims.append(q);save('CLAIMS.json',claims)
    save('out/REVIEW_CORRECTION_DELTA.json',{'erroneous_source':str(prior/'REVIEW_A021.md'),'retract_acceptance':['A021-UNIFORM-RARE-CORE-EXPANSION@1'],'narrow_report_sign_acceptance':['A021-CONTROL-FIRST-KL-LEDGER@1'],'replacement_read':'A021-UNIFORM-RARE-CORE-EXPANSION@2','A023_new_family_v1_dependency_effect':'NONE: direct formulas did not use R or G_s','exact_counterwitness':'q=1/2; R>31/224>0','consumers':['A087','A094','B05','B20'],'shared_indices_changed':False})
    progress={'protocol_revision':proto['revision'],'run_id':ROOT.name,'stream':'B05','packet_id':'A023','gap_id':'G-R-MISMATCH-FIRST-REVELATION','attempt_id':'A023-2-overlap-exposure','method':'Repair prior review; exact conditional exposure split; physical common/exclusive ownership; rational bad-node certificates in four orders','mathematical_delta':'A021 v1 erroneous remainder approval retracted; old direct A023 ledger unaffected. Two overlapping compatible control events sharing one core have zero K=4 bad control cost; exposure criterion a(1-q)>e/8; complete retained-terminal H<7I on all-dimensional bent-surgery cores. 24 roots, 96 complete orders, 24 stopping trees, 963 exact assertions.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'LEAD_DIRECTED_SCOPED_TARGET_PROVED; NEW_CLAIM_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':x['version']} for x in claims],'source_artifacts':['REPORT.md','CORRECTION_A021_REVIEW.md','OVERLAP_GOOD_NODE_PROOF.md','code/check_overlap.py','out/FROZEN_SPEC.json','out/SPEC_CERTIFICATE_UPDATE.json','out/results.json','out/sign_certificates.json','out/validation.json','out/constant_certificate.json','out/artifact_check.json','out/REVIEW_CORRECTION_DELTA.json'],'next_consumers':['A021','A025','A028','A029','A064','A087','A094','B05','B20'],'next_action':'Analyze three compatible point events sharing one core at the first node where residual union probability q violates a(1-q)>e/8; prove single-use complement/survival payment or certify growing bad-node charge while retaining terminal entropy.','stagnant_substantive_attempts':0,'blockers':['New scoped claim awaits independent reconstruction; universal residual exposure and arbitrary terminal cost are unproved'],'packet_ids':['A023']}
    save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
    expected={'packet_ids' if z.startswith('packet_ids ') else z for z in proto['required_per_run']['progress_fields']}
    assert set(progress)==expected
    assert all(set(x)==set(proto['required_per_run']['claim_fields']) for x in claims)
    report=(ROOT/'REPORT.md').read_text()
    assert all('# '+title in report for title in proto['required_per_run']['report_fields'])
    save('out/schema_check.json',{'progress_fields_exact':True,'claim_fields_exact':True,'report_fields_present':True,'packet_delta_equals_progress':True,'status':'PASS'})
    (TASK/'STATUS.md').write_text('STATE: A023 stage 2 complete: A021 v1 review sign approval retracted; direct prior ledger survives; overlapping shared-core controls have zero K=4 bad cost and H<7I on bent-surgery cores; 963 exact checks; new proof review pending; FEI OPEN.\nNEXT: A087/A094 review exposure/ownership; test three events at the first residual-union exposure failure a(1-q)<=e/8 with terminal entropy retained.\n',encoding='utf-8')
    with (TASK/'WORKLOG.md').open('a',encoding='utf-8') as h:
        h.write('\n2026-10-12 UTC stage '+ROOT.name+': Initial tool-host timeouts recovered. Read board and B05 v2 notes. Acknowledged and retracted erroneous A021 v1 negative-remainder review; exact q=1/2 rational witness R>31/224. Audited prior A023 dependency chain: direct bounds unchanged. Proved all-width two-event exposure criterion and zero bad-control cost, with one common-control and shared-core account; H<7I for bent-selector terminals. Frozen 24-root/four-order grid: 963 assertions; 323 exact node signs; max ratios 14/137,12/137,0,0, stopping cost zero. All proofs/certificates saved locally; no shared writes or messaging. Next three-event residual exposure failure.\n')
    with (TASK/'LEARNED.md').open('a',encoding='utf-8') as h:
        h.write('\n- CORRECTION superseding prior blanket A021 no-gap acceptance: -2(1-q)^2log2(1-q)=2cq-3cq^2+POSITIVE R(q); R=4c sum q^j/[j(j-1)(j-2)]. Earlier review had a multiplication sign error; q=1/2 yields R>31/224. A021 v1 expansion acceptance is retracted, exact KL-ledger statement remains valid, use expansion v2. Prior A023 direct first-revelation proof uses neither R nor G and survives.\n- Shared-core exposure: against an independent residual event of probability q, a fresh point-event node with rho=2^-j has B/d<=2(1-rho)+rho log2(e/(rho d)), d=a rho(1-q)/2. If a(1-q)>e/8, every dyadic node is strictly K=4 good. Compatible two-event union with a>=11/16 and q<=1/2 always meets it.\n- For common width s and exclusive widths r,t, terminal activation probability is u(p+q-pq), never u(p+q). Exclusive control influences have (1-q),(1-p) survival factors; common controls are paid once. Full stopping ledger retains terminal entropy and yields H<7I on arbitrary bent point-surgery selector cores, J+terminal<=4I, full mismatch allowance<9I.\n- Finite four-order zeros do not imply data-first is universally safe. For the frozen k=2,4 grid complete selector/control-first ratios max14/137,12/137; data-first/control-data-selector zero. Stopped control tree has zero bad cost in ALL widths by proof. Three-event unions can lose exposure as q approaches one; this is the next owned budget gap.\n')
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p.name!='persistence_receipts.json':
            assert p.stat().st_size<20_000_000
            files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
    save('out/persistence_receipts.json',{'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'rolling_files':[{'path':str(TASK/n),'sha256':sha(TASK/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'local_save_verified':True,'supervisor_copy_verified':False,'mirror_verified':False,'independent_acceptance_of_new_claim':False})
    print(json.dumps({'status':'PASS','artifacts':len(files),'source_receipts':len(sources),'claim_records':len(claims),'sign_certificates':len(certs),'schema':'PASS','local_persistence':'verified'}))
if __name__=='__main__':main()
