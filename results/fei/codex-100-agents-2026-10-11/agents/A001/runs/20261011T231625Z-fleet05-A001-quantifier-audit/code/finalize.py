from pathlib import Path
import hashlib, json, re

RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[1]
TEAM=ROOT.parents[1]
SHARED=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPPLEMENT=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
A089=TEAM/'agents'/'A089'/'runs'/'20261011T224857Z-fleet05-A089-repair-specialist'
protocol=json.loads((SHARED/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
required=protocol['required_per_run']
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
headings=re.findall(r'^# (.+)$',report,re.M)
assert headings==required['report_fields']
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
walsh=json.loads((RUN/'out'/'WALSH_CHECK.json').read_text(encoding='utf-8'))
order=json.loads((RUN/'out'/'ORDER_CERTIFICATES.json').read_text(encoding='utf-8'))
tail=json.loads((RUN/'out'/'TAIL_ANCHORS.json').read_text(encoding='utf-8'))
assert walsh['assertions']==90 and order['assertions']==66 and tail['assertions']==10
assert all(x['failures']==0 for x in [walsh,order,tail])
assert len(order['rows'])==12

sources=[
    (SHARED/'EXECUTION_PROTOCOL.json','revision 2026-10-11-execution-v2'),
    (TEAM/'BOARD.md','snapshot 2026-10-11 23:09 UTC'),
    (TEAM/'claude'/'B01'/'STREAM_NOTES.md','v1 22:40Z; A001 next target'),
    (SHARED/'source_material'/'reductions'/'paper'/'restrictions.tex','prop:bentsplice, prop:splitexact'),
    (SHARED/'runs'/'B05'/'20261011T193057Z-fleet01-B05-rare-restrictions'/'REPORT.md','sections 2-6'),
    (SUPPLEMENT/'sources'/'ERASURE_REDUCTION.md','sections 1-4'),
    (A089/'REPORT.md','sections 2-4; B05 erasure subclaim'),
    (A089/'CLAIMS.json','A089-EXACT-EXISTENTIAL-ERASURE-REPAIR@1'),
    (ROOT/'runs'/'20261011T210330Z-fleet05-A001-quantifier-audit'/'REPORT.md','prior A001 packet continuity')]
manifest=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,locator=loc) for p,loc in sources]
save(RUN/'out'/'SOURCE_MANIFEST.json',manifest)

statement='For the canonical quadratic bent splice X009 on m+1 physical bits, every even m>=4 has its relevant-coordinate minima B_i/I_i and Delta_iH/I_i attained exactly by data coordinates, with closed forms (7) in REPORT.md, sharp family suprema 2 and 4 respectively. For the canonical B05 activation of that splice with even k>=4 and r=2k controls, the B_i/I_i minimum is data at k=4 and control at k>=6, while the Delta_iH/I_i minimum is data at k=4,6,8,10,12 and control at every even k>=14. Formula (19) gives both exact minima. Their limits are 2 and 4; a uniformly bounded decrement coordinate exists with ratio less than 4+41/512. The selector never minimizes either ratio.'
hypotheses=['Actual Boolean signs on uniform physical cubes; entropy in bits','Canonical quadratic bent sign and one origin-point flip selected by y, as defined in REPORT.md section 2','B05 uses a point activation on exactly r=2k fresh control bits','Minima are over relevant coordinates; no hereditary restriction-closure assertion']
claim=dict(claim_id='A001-LOCAL-ERASURE-AND-DECREMENT-ARGMIN',version=1,exact_statement=statement,hypotheses=hypotheses,
    statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hypotheses),sort_keys=True,separators=(',',':')).encode()).hexdigest(),
    contributors=['A001; B05 erasure ordering credited to A089'],
    proof_source={'path':'REPORT.md','sections':'1-6','finite_certificate':'out/ORDER_CERTIFICATES.json','tail_anchors':'out/TAIL_ANCHORS.json'},
    proof_dependencies=[{'source':'Exact Fourier split and scalar entropy inequalities','locator':'REPORT.md section 1; original C005 prop:splitexact'},{'source':'Integer Walsh/direct-edge verification','path':'out/WALSH_CHECK.json'},{'source':'Finite rational ordering certificate','path':'out/ORDER_CERTIFICATES.json'},{'source':'Self-contained all-parameter ordering proof','locator':'REPORT.md sections 3,5,6'}],
    review_records=[],status='ANALYTIC_AND_EXACT_CERTIFICATE_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,
    next_consumers=['A003','A005','A026','A064','A087','A089','A094','B01','B18','B20'])
old=json.loads((A089/'CLAIMS.json').read_text(encoding='utf-8'))[0]
old['review_records']=old.get('review_records',[])+[dict(reviewer='A001/fleet05',verdict='ACCEPT_B05_R_EQUALS_2K_SUBCLAIM_ONLY',scope='B05 erasure argmin: data at k=4, control for every even k>=6, restricted to r=2k. A062 and r>2k portions not independently accepted by this review.',method='Independent directed Walsh-pair multiplicities and physical edges; rational logarithm ordering base; independent scalar-inequality tail reconstruction in REPORT.md section 5.',proof_source={'path':str(RUN/'REPORT.md'),'sections':'2,4,5','certificates':'out/ORDER_CERTIFICATES.json and out/WALSH_CHECK.json'},contributor_to_original=False)]
# Preserve the original full bundled claim as pending: acceptance is only of the recorded slice.
old['status']='AUTHOR_PROVED_PENDING_FULL_INDEPENDENT_REVIEW; B05_R_EQUALS_2K_SUBCLAIM_ACCEPTED_BY_A001'
for c in [claim,old]:
    assert set(c)==set(required['claim_fields']),set(c)^set(required['claim_fields'])
    expected=hashlib.sha256(json.dumps(dict(statement=c['exact_statement'],hypotheses=c['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert expected==c['statement_sha256']
save(RUN/'CLAIMS.json',[claim,old])
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B01',packet_id='A001',gap_id='G-R-SELECT',attempt_id='A001-LOCAL-ARGMIN-1',
    method='Consume A089 erasure dependency; derive signed-pair decrement formulas; exact core/full-table Walsh checks and rational log certificates; analytic all-parameter tail proof',
    mathematical_delta='Closed both X009 coordinate minima; independently accepted A089 B05 erasure ordering at r=2k; new decrement argmin data through k=12 and control for every even k>=14; selector excluded and all-parameter bounded root coordinate proved.',
    deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_ADOPTION',mathematical_status='LOCAL_SELECTION_THEOREM_PROVED_PENDING_REVIEW; SCOPED_DEPENDENCY_REVIEW_COMPLETE; FULL_FEI_OPEN',
    claim_versions_used=['A089-EXACT-EXISTENTIAL-ERASURE-REPAIR@1 (B05 r=2k subclaim independently reconstructed)','B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO@1 (accepted obstruction/family definition)','C005 source exact restriction identity (reconstructed pairwise)'],
    claims_created_or_changed=['A001-LOCAL-ERASURE-AND-DECREMENT-ARGMIN@1','A089-EXACT-EXISTENTIAL-ERASURE-REPAIR@1 (scoped independent review record only)'],
    source_artifacts=['out/SOURCE_MANIFEST.json','REPORT.md','code/certify.py','out/WALSH_CHECK.json','out/ORDER_CERTIFICATES.json','out/TAIL_ANCHORS.json','out/FROZEN_SPEC_v3.json'],
    next_consumers=['A003','A005','A026','A064','A087','A089','A094','B01','B18','B20'],
    next_action='Derive conditional-row/child-deficit transport after one selected data/control restriction with terminal reserve retained; test the identity on arbitrary tensor-core activations to bridge root selection to C019.',
    stagnant_substantive_attempts=0,blockers=['Universal hereditary selection and terminal payment remain unproved','Independent review of new decrement/X009 theorem pending'],packet_ids=['A001'])
assert set(progress)=={x.split(' (')[0] for x in required['progress_fields']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()

(ROOT/'STATUS.md').write_text('STATE: Stage 2 complete: X009 exact minima and B05 decrement switch at k=14 proved; 166 exact checks PASS; A089 B05 r=2k erasure subclaim independently accepted; full FEI OPEN.\nNEXT: Derive child-deficit transport after the chosen split on arbitrary-core activation, retaining terminal entropy; A087/A094 review new all-parameter argmin.\n',encoding='utf-8')
work='2026-10-11 23:16 UTC stage: Consumed updated BOARD/B01 lead and A089 original; avoided duplicating its B05 erasure result. Proved X009 data argmins and B05 decrement argmin data k<=12/control k>=14, with 90 exact Walsh/edge checks, 66 rational interval checks and 10 tail anchors. Saved pilot-scope, directed-histogram and serialization corrections before acceptance. Required run files persisted; no heavy job or shared/brain mutation. Full FEI OPEN.\n'
learn='For X009, both B_i/I_i and Delta_iH/I_i are minimized by data bits for all even m>=4; sharp family suprema are 2 and 4. For canonical B05 r=2k, the B argmin switches at k=6 but the exact decrement argmin switches at k=14. Jensen-Shannon changes the minimizing coordinate: cheapest erasure is not generally cheapest decrement. Controls satisfy Delta_i/I_i<4+41/512 uniformly. The universal unpaid edge is heredity/terminal payment after the chosen split, not root coordinate availability on these families. Directed mixed bent pairs have counts N/8 +/- sqrt(N)/4; symmetric entropy numerators do not make influence denominators symmetric. Exact outward dyadic rounding controls rational log interval denominator growth.\n'
for name,entry in [('WORKLOG.md',work),('LEARNED.md',learn)]:
    p=ROOT/name
    if entry not in p.read_text(encoding='utf-8'):
        with p.open('a',encoding='utf-8') as f:f.write(entry)
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name not in ['ARTIFACT_RECEIPTS.json','FINAL_VALIDATION.json']:
        assert p.stat().st_size<20*1024*1024
        receipts.append(dict(path=str(p.relative_to(RUN)),bytes=p.stat().st_size,sha256=sha(p)))
save(RUN/'out'/'ARTIFACT_RECEIPTS.json',receipts)
result=dict(report_fields='PASS',claim_fields='PASS',progress_fields='PASS',statement_hashes='PASS',compatibility_copy='BYTE_IDENTICAL',universal_bridge_final_paragraph='PASS',size_cap='PASS',exact_assertions=166,source_files=len(manifest),saved_artifacts=len(receipts),new_claim_independent_review='PENDING',A089_review='B05_R_EQUALS_2K_SUBCLAIM_ACCEPTED',full_fei='OPEN')
save(RUN/'out'/'FINAL_VALIDATION.json',result);print(json.dumps(result))
