from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1]
TEAM=Path(r'~\brain_workers\FEI100_20261011')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
sources=[(TEAM/'BOARD.md','stage-start board read'),(TEAM/'claude/B05/STREAM_NOTES.md','full v2 lead notes read'),
 (TEAM/'claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport/REPORT.md','full lead report inspected'),
 (TEAM/'claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport/code/b05_ledger_k6.py','four-order definitions and ledger inspected'),
 (TEAM/'agents/A025/runs/20261011T225648Z-fleet05-A025-rare-event-counterfamily/REPORT.md','report inspected for threshold-2 scope and nonduplication'),
 (AGENT/'runs/20261011T215800Z-fleet05-A022-one-point-surgery/POINT_SURGERY.tex','previous-stage own proof carried forward as context')]
source_receipts=[]
for path,scope in sources:
    data=path.read_bytes();source_receipts.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'scope':scope})
(RUN/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(source_receipts,indent=2),encoding='utf-8')
statement=('For actual Boolean children g and h=g(1-2*1_D) on m uniform bits, nonempty D of s vertices and E(D) internal unordered edges, '
'd=s*2^-m and c_D=I(gh)/2=2^-m(ms-2E(D)), and c_D+log2(e)*d-B equals '
'2^-m(s log2(s)-2E(D)) + [d+(1-d)ln(1-d)]/ln2 + I(Z;T), with Z the selector spectral bit and T the residual label. '
'For quadratic bent core b on even k>=4 and a one-point activation on r>=0 controls, actual selector surgery F has '
'I(F)=2^-r[k/2+r(1-2^(-k/2))+2^-k(A_D+r S_D+s)], with S_D=sum_D b(v) and '
'A_D=sum_(v in D,i:v^i notin D)b(v)b(v^i). For alpha=s*2^-k<1/2, c_D/I(F)<=2alpha/(1-2alpha). '
'Every fair constant-child split obeys B/d<=2+log2(e)/sqrt(e)<3, so control-first activation creates no threshold-4 bad-node credit and scales the full active core ledger by 2^-r. '
'Exact exhaustion of k=4, r in {0,2,4}, all D of sizes 1..4 and four named complete orders gives maximum Q_bad,4/I=4/29 at D={15},r=0,selector-first or control-first, '
'while control-data-selector has zero bad-node credit for every such D and every integer r>=0. '
'For D3={2,4,6} and D4={2,4,6,11}, the data-first descendant after x0=0 querying x1 is bad for every r>=1; '
'its B/d is at least [112-54log2(3)+80log2(5)-98log2(7)+26log2(13)]/8 in (4157/1000,4158/1000). '
'The full data-first bad-node ratio is at least (r+3)/(35+15r) or (r+3)/(34+14r), respectively. '
'These are scoped root/ledger claims, not a universal stopping-tree payment or an FEI disproof.')
claim={'claim_id':'A022-ODDFACE-SURGERY-GAP-LEDGER','version':1,'exact_statement':statement,
'hypotheses':['Uniform cube, actual Boolean signs, fair physical selector','Entropy in bits; badness is strict B>4d','Root bound k>=4 even and 0<alpha<1/2','Finite maxima restricted to the frozen four named orders and declared domain','All-r zero-credit extension restricted to k=4 and |D|=1..4','All-r bad-descendant lower bounds restricted to the two named vertex sets'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A022'],
'proof_source':{'run_id':RUN.name,'proof':'ODDFACE_GAP.tex','finite_certificate':'out/full_RESULTS.json','pattern_records':['out/full_r0_patterns.jsonl','out/full_r2_patterns.jsonl','out/full_r4_patterns.jsonl'],'descendant_certificate':'out/WITNESS_TRANSPORT.json','artifact_reconstruction':'out/ARTIFACT_CHECK.json'},
'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_SCOPED_CERTIFICATE_PENDING_INDEPENDENT_REVIEW',
'supersedes':[],'refutes':[],'first_unproved_line':None,
'next_consumers':['A021','A023','A025','A028','A053','A064','A077','A087','A094']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
(RUN/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B05','packet_id':'A022',
'gap_id':'G-R-MISMATCH','attempt_id':'A022-oddface-surgery-2',
'method':'Exact signed gap decomposition, geometric surgery boundary, certified four-order census, constant-child transfer and all-r descendant proof',
'mathematical_delta':'Exact odd-face slack; arbitrary-pattern root bound; 7548 flip patterns and 30192 exact tree ledgers; zero control-data-selector credit for all r in the scoped k=4 family; persistent but bounded data-first descendant debt',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'LEAD_DIRECTED_SCOPED_TARGET_RESOLVED_PENDING_REVIEW_FULL_FEI_OPEN',
'claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
'source_artifacts':['REPORT.md','ODDFACE_GAP.tex','out/FROZEN_SPEC.json','out/FOLLOWUP_SPEC.json','out/full_RESULTS.json','out/WITNESS_TRANSPORT.json','out/ARTIFACT_CHECK.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':claim['next_consumers'],
'next_action':'Prove single-use ownership for point-like mismatches created by cancellation of adjacent data slices, beginning with the x0=0,x1 witness and preserving terminal entropy on unbounded cores',
'stagnant_substantive_attempts':0,'blockers':['Independent reconstruction/adoption pending; no universal descendant ownership bound established'], 'packet_ids':['A022']}
expected={name.split(' (')[0] for name in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
for name in ['PROGRESS.json','PACKET_DELTA.json']:(RUN/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
total=0
for name,field in [('pilot_RESULTS.json','assertions_passed'),('full_RESULTS.json','assertions_passed'),('WITNESS_TRANSPORT.json','assertions'),('ARTIFACT_CHECK.json','checks_passed')]:
    total+=json.loads((RUN/'out'/name).read_text())[field]
assert total==405993
(AGENT/'STATUS.md').write_text('STATE: A022 stage 2 complete: exact odd-face gap and 30,192 tree ledgers; all-r control transfer and bounded data-first descendant debt proved; 405,993 checks; review pending; full FEI OPEN.\nNEXT: A087/A094 reconstruct; prove single-use ownership for rare mismatches created by adjacent-slice cancellation, retaining terminal entropy on unbounded cores.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as fp:fp.write('2026-10-11 23:46 UTC stage / completed 2026-10-12 local: Followed B05 v2 odd-face target. Exact three-part slack, arbitrary-pattern bent activation influence/root bound, all 7,548 k=4 patterns and 30,192 four-order ledgers certified. Worst fixed-order ratio 4/29; best of four zero throughout. D={2,4,6} and {2,4,6,11} create data-first bad descendants for all r>=1, with ratios bounded below tending to 1/15 and 1/14; no divergence. Constant-child lemma extends zero control-data-selector credit to every r in frozen k=4 pattern class. Pilot/full/witness/artifact checks total 405,993; full runtime 41.902170s. Corrected draft signed Walsh list to executed exact list before completion. Independent review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as fp:fp.write('Exact odd-face surgery slack = 2^-m[s log2(s)-2E(D)] + [d+(1-d)ln(1-d)]/ln2 + I(selector spectral bit; residual label). Point and adjacent flips have no geometric excess; separated pair has excess d. Constant-child split has B=2d(1-d)+Psi(d^2,(1-d)^2), hence B/d<=2+log2(e)/sqrt(e)<3; control-first queries of one-point activation are all good at K=4, but the entire active core ledger remains. For activated quadratic bent with flip density alpha<1/2, root odd-face credit/I<=2alpha/(1-2alpha) uniformly in controls; this cannot be charged again below the root. D3={2,4,6}, D4={2,4,6,11} on four data bits create a one-point mismatch after x0=0 querying x1: B/d>=4.157115... for all r>=1; data-first credit/I has lower limits 1/15,1/14, bounded. Control-data-selector zero credit for these k=4 sparse pattern cores extends to all r, by exact finite certificate plus control transfer.\n')
receipts=[]
for path in sorted(RUN.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPTS.json':
        data=path.read_bytes();assert len(data)<20_000_000
        receipts.append({'path':str(path.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    path=AGENT/name;data=path.read_bytes();receipts.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
text=(RUN/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '# '+field in text
assert text.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
receipt={'saved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_fields':'exact claim fields; progress fields after annotation packet_ids interpreted canonically; all report fields present',
 'checks':total,'independent_review':False,'mirror_verified':False,'files':receipts}
(RUN/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'files_saved':len(receipts),'checks':total,'protocol_field_checks':'PASS','max_file_bytes':max(v['bytes'] for v in receipts),'independent_review':'PENDING','full_fei':'OPEN'},indent=2))
