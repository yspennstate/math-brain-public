import datetime,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1];AGENT=HERE.parents[1]
OLD=AGENT/'runs/20261012T033113Z-account05-A029-child-deficit-transport'
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
TEAM=AGENT.parents[1];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def baseclaim(cid,statement,hyp,source,deps,refutes):
    payload=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()
    return {'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,
      'statement_sha256':hashlib.sha256(payload).hexdigest(),'contributors':['account05/A029'],
      'proof_source':source,'proof_dependencies':deps,'review_records':[],
      'status':'AUTHOR_PROVED_SOURCE_COMPLETE_PENDING_INDEPENDENT_REVIEW','supersedes':[],
      'refutes':refutes,'first_unproved_line':None,'next_consumers':['A028','A030','A064','A087','A094','B06 lead','B20']}
baseline={'claim_id':'B06-R2','version':'STREAM_NOTES v2, 2026-10-11 23:26Z','status':'BASELINE_USED_NOT_RECLAIMED'}
hyp=['Actual Boolean signs; independent fair physical bits; entropy in bits; ordinary physical influence',
 'Tree ratios retain actual physical terminal entropy and influence; constants have no divided ratio',
 'Depth-two versus arbitrary-tree domains are explicitly distinct']
refute={'exact_statement':'For every Boolean f, best single-coordinate ratio minus best unrestricted physical stopping-tree ratio is at most 2',
 'source':'B06 STREAM_NOTES v2 A029 target; unrestricted reading of parenthetical all-bent gain exactly2',
 'surviving_scope':'Prior n<=4 depth-two theorem, all paired-carrier depth-two equality, and quadratic bent unrestricted equality remain valid',
 'not_refuted':'Full FEI; or the dimension-unrestricted depth-two gain bound for every Boolean function'}
c2=baseclaim('A029-DEPTH-SENSITIVE-BENT-GAIN',
 'For every m>=1 and Boolean m-bit seed g, F_g(x,y)=(-1)^(x dot y)g(y) has r1=4 and best depth-at-most-two stopping ratio2. Quadratic bent roots have best unrestricted stopping ratio2. For m=3 and g=-1 only at000, the explicit tree revealing x, stopping at x=0 and completing y elsewhere has ratio (352+9log2(3))/186<916/465; hence unrestricted gain>944/465>2.03. Its terminal deficit D2(g)/8 is the exact negative of its query credit, and disjoint tensors inherit this helper violation while retaining H/I=2.',
 hyp,['REPORT.md','DERIVATION.md','code/check.py','code/verify.py','out/checks.json','out/independent.json'],[baseline],[refute])
c3=baseclaim('A029-PRIORITY-TERMINAL-DEFICIT-TRANSPORT',
 'For every m>=1, Boolean m-bit seed g, p=2^-m, and real K, the paired carrier F_g has the priority physical tree querying x to its first1 at i, then y1..yi, or stopping at g if all x=0. Its costs are Pi_I=2-p(2+I(g)) and Pi_H=4-p(4+H(g)); terminal expected D_K=(K-2)(m-2+2p)+pD_K(g), and query account KPi_I-Pi_H=2(K-2)-p[2(K-2)+D_K(g)], summing to D_K(F)=(K-2)m. For the six-variable three-bit-point-defect carrier, the declared seven-node depth-four tree has ratio (184+9log2(3))/102<496/255, giving gain>524/255>2.05. Minimum expected terminal D2 cut is zero at depth3 and -5/16+(9/64)log2(3) at depth4; therefore4 is the least maximum tree depth giving gain>2 for this specific root.',
 hyp+['Priority transport applies to arbitrary seed, without an assumed seed FEI certificate',
      'The compact-tree ratio is attained; no global optimal ratio or all-function minimal-dimension assertion'],
 ['REPORT.md','DERIVATION.md','code/check.py','code/verify.py','out/compact.json','out/independent.json'],
 [baseline,{'claim_id':c2['claim_id'],'version':1,'status':'LOCAL_PROOF_USED_ONLY_FOR_SURVIVING_DEPTH_TWO_SCOPE'}],[refute])
def persist_run(run,claim,num,delta,method,nextact,artifacts):
    ck=run.resolve().is_relative_to(AGENT.resolve());assert ck
    dump(run/'CLAIMS.json',[claim])
    progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B06','packet_id':'A029',
     'gap_id':'G-R-MISMATCH','attempt_id':f'A029-child-deficit-transport-{num:02}',
     'method':method,'mathematical_delta':delta,'deliverable_status':'COMPLETE_LOCAL_SAVED_PENDING_REVIEW',
     'mathematical_status':'GAIN_HELPER_REFUTED_SCOPED_TRANSPORT_PROVED_FULL_FEI_OPEN',
     'claim_versions_used':claim['proof_dependencies'],
     'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
     'source_artifacts':artifacts,'next_consumers':claim['next_consumers'],'next_action':nextact,
     'stagnant_substantive_attempts':0,
     'blockers':['Universal terminal-inclusive arbitrary-root payment unproved','Independent agent review and supervisor mirror verification pending'],
     'packet_ids':['A029']}
    dump(run/'PROGRESS.json',progress);dump(run/'PACKET_DELTA.json',progress)
    protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))['required_per_run']
    assert set(claim)==set(protocol['claim_fields'])
    assert set(progress)==set(f.split(' (')[0] for f in protocol['progress_fields'])
    report=(run/'REPORT.md').read_text(encoding='utf-8')
    assert all(f'## {f}' in report for f in protocol['report_fields'])
    assert report.strip().split('\n\n')[-1].startswith('**Universal bridge:**')
    assert json.loads((run/'PROGRESS.json').read_text())==json.loads((run/'PACKET_DELTA.json').read_text())
    return progress
p2=persist_run(OLD,c2,2,'All-seed paired depth2 gain2; six-variable unrestricted gain>2.03; exact negative terminal cancellation; 593232 checks and second implementation561 checks',
 'Paired signed Fourier law, frozen 256-seed restriction census, exact prime-log explicit stopping certificate',
 'Finish compact depth4 witness and derive arbitrary-seed priority cleanup transport with its single terminal deficit retained',
 ['REPORT.md','DERIVATION.md','SPEC.json','VERIFY_SPEC.json','out/checks.json','out/independent.json','out/witness.json'])
p3=persist_run(HERE,c3,3,'Arbitrary-seed priority signed accounts at every K; compact depth4 gain>2.05, minimum depth4 certified; 276 priority trees, 14495 assertions; direct checker3381 assertions',
 'Exact arbitrary-seed priority transport, seven-node physical countertree, independent exact prime-log cut DP',
 'Apply certified signed terminal-core slack to a two-branch shared-control selector ledger, pricing coherent query correction from one owned reserve; retire further gain searches',
 ['REPORT.md','DERIVATION.md','SPEC.json','VERIFY_SPEC.json','code/check.py','code/verify.py','out/checks.json','out/compact.json','out/independent.json'])
dump(HERE/'REFUTED_STATEMENT.json',dict(refute,actual_witness='F(x,y)=(-1)^(x dot y)g(y), g=-1 iff y=000',
 checked_tree='Seven internal nodes, maximum depth4; complete physical leaf list out/compact.json',
 exact_ratio='(184+9log2(3))/102',strict_gain_lower='524/255',
 first_false_inference='Using a queried-tree ratio while treating the actual negative terminal D_K as zero',
 original_finite_claim_unchanged='A029-CHILD-DEFICIT-BENCHMARKS v1 n<=4 scope'))
(AGENT/'STATUS.md').write_text('STATE: A029 stage3 saved: arbitrary-seed priority transport; depth4 bent gain>2.05 refutes unrestricted all-bent gain2; depth2/quadratic scopes survive; exact checks PASS; review pending; full FEI OPEN.\nNEXT: A087/A094 review; use one certified signed terminal-core reserve at a shared-control selector with both physical child debts retained; retire gain searches.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} Stage2 late finalization after prompt interruption: paired arbitrary-seed depth2 theorem, six-variable bent unrestricted counterexample, 186624 restrictions/593232 exact checks and561 direct checks were saved before interruption; REPORT/CLAIMS/PROGRESS/PACKET_DELTA now source-complete. No retroactive mirror or review claim.\n')
 f.write(f'\n{now} Stage3: read current board/B06 v2/status and A030/A064 lessons. Proved priority cleanup PiI=2-p(2+Ig), PiH=4-p(4+Hg) for every seed, retained signed terminal D_K at every K. Frozen276 priority trees:14495 exact checks PASS in3.256s. Compact seven-node depth4 bent tree ratio(184+9log2 3)/102, gain>524/255>2.05. Direct prime-log/physical-cut implementation3381 checks PASS in0.170s; exact minimum cut D2=0 atdepth3, negative atdepth4. Prior unrestricted bent gain2 reading refuted; depth2 and quadratic cases survive. Next coherent shared-control terminal reserve, not further gain census.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('''

## Stages 2 and 3: depth-sensitive bent terminal debt

- F_g(x,y)=(-1)^(x dot y)g(y) has Fourier coefficients2^-m g(A)(-1)^(A dot B), hence H=2m,I=m and every root split ratio4, for every actual Boolean seed.
- Under a restriction with p free pairs, U unmatched free y, ell fixed-y=1 pure x characters, H=2p+E H(u_t), I=p+ell+E I(u_t). If physical codim<=2, |U|<=2 and D2>=0. Thus all paired carriers have depth2 ratio2/gain2 in every dimension, without certifying the arbitrary seed itself.
- Quadratic bent roots have ratio2 for every unrestricted optimal stopping tree because all quadratic restrictions satisfy H<=2I. General bent roots do not: the six-bit paired three-bit point defect gives gain>2.05 atdepth4. Do not extend n=4 quadratic evidence to all bent functions.
- Compact countertree: x1=1 -> query y1, stop; x1=0 -> x2; x2=1 -> y2, stop if1, otherwise y1 then stop; x2=0 -> x3, stop if0, otherwise y3 then stop. Seven internal nodes/eight leaves. PiI=51/32, PiH=23/8+(9/64)log2 3. Ratio=(184+9log2 3)/102<496/255. Minimum allowed maximum depth for gain>2 on this particular function is4 (exact cut DP through3/4).
- Priority arbitrary-seed cleanup: query x to first1 at i, then y1..yi; all-zero x leaves g. p=2^-m. PiI=2-p(2+Ig), PiH=4-p(4+Hg); E D_K=(K-2)(m-2+2p)+pD_K(g); query account=2(K-2)-p[2(K-2)+D_K(g)]. Sum=(K-2)m. AtK2 terminal pD2(g) and query credit -pD2(g) cancel exactly.
- The gain shortcut's failure is caused by an actual negative terminal deficit, not a root FEI violation. Tensor replication preserves the helper violation with H/I=2. No finite-to-universal inference may delete or repeatedly spend that terminal account.
- Primary stage2 pilot caught original-coordinate/local-index confusion in influence vectors; corrected before full search. Physical coordinate labels must be translated to the ordered free-variable indices after restriction.
''')
paths=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B06/STREAM_NOTES.md',AGENT/'runs/20261011T223746Z-account05-A029-child-deficit-transport/REPORT.md',
 TEAM/'agents/A030/LEARNED.md',TEAM/'agents/A064/LEARNED.md',OLD/'DERIVATION.md',OLD/'out/checks.json',OLD/'out/independent.json']
sources=[]
for p in paths:
    data=p.read_bytes();sources.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'size_bytes':len(data),'receipt_time':now})
dump(HERE/'SOURCE_RECEIPTS.json',sources)
dump(OLD/'SOURCE_RECEIPTS.json',{'finalization_time':now,'note':'Current source hashes at late finalization, not a claim to recover overwritten historical BOARD snapshot',
 'sources':[s for s in sources if s['path']!=str(TEAM/'BOARD.md')]})
for run in (OLD,HERE):
    entries=[]
    for p in sorted(run.rglob('*')):
        if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
            data=p.read_bytes();assert len(data)<20*1024*1024
            entries.append({'path':str(p.relative_to(run)),'size_bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    dump(run/'ARTIFACT_RECEIPTS.json',{'persisted_utc':now,'local_only':True,'artifacts':entries,
       'stage2_late_finalization':run==OLD})
assert (AGENT/'STATUS.md').read_text().count('\n')==2
print(json.dumps({'status':'PASS','protocol_fields_exact':True,'stage2_finalized':str(OLD),'stage3_finalized':str(HERE),
 'claim_hashes':[c2['statement_sha256'],c3['statement_sha256']],'rolling_files_current':True},indent=2))
