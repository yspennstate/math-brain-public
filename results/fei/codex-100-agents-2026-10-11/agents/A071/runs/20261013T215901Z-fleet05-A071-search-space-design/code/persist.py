import hashlib,json
from datetime import datetime,timezone
from pathlib import Path

RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
statement=('For h negative exactly on {0,1,2,4,8,16,32,6,17,40}, let g be the six-bit sign negative only at zero. '
 'With B_i the spectral conditional entropy in bits and E=min relevant B_i/Inf_i, E(g)>9/4 whereas '
 'E(h(g^6))<9/4 and E(h((-g)^6))<9/4, using disjoint identical copies. '
 'All 36 physical coordinates in each composition are equal by actual permutation symmetry. '
 'Thus neither a universal nonnegative signed admission reserve nor an arbitrary-K threshold transfer, even with a choice of output sign, holds for this gate. '
 'Separately 323/100<E(h(h^6))<324/100. '
 'The 559 achievable six-bit bias/singleton-square signatures have 440 positive,31 zero,88 negative signed reserves; '
 'the 288 signatures with p<=1/2 have 233 positive,16 zero,39 negative reserves. '
 'These are scoped finite statements and do not refute admission restricted to E(g)>=K6 or prove/disprove FEI.')
claim_id='A071-F6-BIASED-ADMISSION-OBSTRUCTION'
claim={'claim_id':claim_id,'version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean signs on independent uniform physical blocks; entropy in bits',
  'h is the specified matched-pair six-bit truth table; no arbitrary gate quantifier',
  'Core g is the actual six-bit one-point defect; its output complement included',
  'Signature completeness concerns the signed scalar reserve only, not all E minima',
  'Interval arithmetic proof and transitivity establish strict rational comparisons; external review pending'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A071'],
 'proof_source':str(RUN/'REPORT.md'),
 'proof_dependencies':['Exact Walsh Parseval, coordinate-pair erasure, and physical edge counts, reconstructed locally',
  'A056 biased recentered B_i interface equations (3)-(6), independently specialized and checked against actual18-bit table; no reliance on signed-correction positivity'],
 'review_records':[],'status':'LOCAL_EXACT_CERTIFICATE_AND_PROOF_REVIEW_PENDING',
 'supersedes':[],
 'refutes':['A071 test hypothesis: for all actual cores R_p(beta_i^2)>=0',
  'A071 test repair: minority orientation always makes that reserve nonnegative',
  'A071 test repair: for every g,K with E(g)>K some sign epsilon has E(h((epsilon*g)^6))>K'],
 'first_unproved_line':None,'next_consumers':['A075','A089','A085','A092','A082','B15','B20']}
write(RUN/'CLAIMS.json',[claim])
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',
 BASE/'agents/A075/runs/20261013T212622Z-fleet05-A075-search-to-theorem-bridge/REPORT.md',
 BASE/'agents/A075/runs/20261013T212622Z-fleet05-A075-search-to-theorem-bridge/CLAIMS.json',
 BASE/'agents/A056/runs/20261011T233147Z-fleet05-A056-balanced-composition/REPORT.md',
 BASE/'agents/A085/runs/20261013T213517Z-fleet05-A085-certificate-adversary/REPORT.md',
 BASE/'agents/A098/runs/20261012T024601Z-fleet05-A098-resource-reallocation/REPORT.md',
 BASE/'agents/A089/runs/20261012T044049Z-fleet05-A089-repair-specialist/REPORT.md',
 AGENT/'runs/20261011T233808Z-fleet05-A071-search-space-design/REPORT.md',
 AGENT/'runs/20261011T233808Z-fleet05-A071-search-space-design/code/sparse_search.py']
write(RUN/'out/source_manifest.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources])
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B15','packet_id':'A071',
 'gap_id':'B15-ARBITRARY-CORE-BIASED-ADMISSION','attempt_id':'A071-stage3-f6-signed-reserve',
 'method':'Freeze actual small/edited cores, then exhaust all achievable six-bit (bias,singleton-square) signatures; exact rational Walsh/centered coefficients and rigorous logarithms; independent actual18-bit physical reconstruction and signed conditional-section certificates.',
 'mathematical_delta':'Both output orientations of a six-bit one-point defect defeat unguarded fixed-K admission at K=9/4. 559 projected signatures exactly classified. Actual36-bit h(h^6) has E>3.23. Threshold-guarded high-E admission and FEI remain open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; independent review and supervisor copying pending',
 'mathematical_status':'BOUNDED_ADMISSION_HELPERS_REFUTED_EXACTLY; HIGH_E_ADMISSION_OPEN; FULL_FEI_OPEN',
 'claim_versions_used':['A056 biased-child physical erasure split, REPORT equations (3)-(6); independently reconstructed, no universal payment assumed',
  'A075-SPARSE-MATCHING-HEREDITARY-CLOSURE@1 consumed for dispatch only, pending review',
  'A082/A085 independent n=5 reconstruction/coverage audit consumed to retire prior census'],
 'claims_created_or_changed':[claim_id+'@1'],
 'source_artifacts':[str(p) for p in sources]+[str(RUN/'out/orientation_certificate.json'),str(RUN/'out/verification.json'),str(RUN/'out/signatures.json')],
 'next_consumers':['A075','A089','A085','A092','A082','B15','B20'],
 'next_action':'State threshold-guarded admission at E(g)>=K6 using the exact signed reserve; target realizability of negative-reserve signature sectors in actual high-E cores, preserving every physical coordinate and terminal H(g). Independent A085/A092 reconstruction of the two orientation certificates.',
 'stagnant_substantive_attempts':0,'blockers':[], 'packet_ids':['A071']}
write(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',progress)
now=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A071 stage3 complete locally: both orientations of a six-bit point defect refute unguarded f6 admission at K=9/4; 559 exact signatures; 36-bit h(h^6) E>3.23; review pending; FEI OPEN.\nNEXT: A075/A089 formulate high-E guarded admission using signed reserves and terminal H(g); target bad signature sectors; A085/A092 independently reconstruct orientation certificates.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | Stage 20261013T215901Z: read updated board/lead/status and consumed A075 matching closure. Frozen408 actual cores:1526 relevant coordinate types,414 negative reserves,73 decreasing E. Projected six-bit signatures complete559:88 negative,39 minority-negative; four paired signatures negative in both signs. Certified one-point core E=2.292244938>9/4 and both36-bit compositions E=2.152706173,2.000800963<9/4. Certified h(h^6) E=3.230266469>323/100. Independent full18-bit Walsh/edge/pair reconstruction passed all18 coordinates. Corrected verifier diagnostic threshold for -h from5/2 to8/3 after an assertion; console truncation caused nonzero pipeline exit only after full search saved. No high-E admission theorem or FEI resolution claimed. Artifacts '+str(RUN)+'.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | f6 arbitrary-core interface: B_i(h(g^6))=q B_i(g)+R_p(beta_i^2), Inf_i=q Inf_i(g), q=2p(1-p)^3(2-p). Output sign matters before this gate despite preserving core E,H,I. One-point six-bit g (p1/64,beta=-1/32) has E=[62+962log2(962)-961log2(961)]/32>9/4; BOTH gate compositions with g or -g have E<9/4, so minority/either-sign unguarded admission fails. This does not refute a guarded E>=K6 version. Projected signatures (M,d) with M1..63,0<=d<=min(M,64-M),d=M mod2 are exactly complete for this reserve on six-bit cores;559 cases,88 negative;39/288 minority-negative. Actual h(h^6),36 bits, has every coordinate E=3.230266468892202...>323/100, all physical influences17419455/268435456. Finite erasure lower obstruction is not FEI disproof or an H/I lower bound of that size. See stage3 exact rational packets and certificates.\n')
# Validate exact schema fields; packet_ids is the protocol's compatibility field.
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['required_per_run']['report_fields']:assert '\n## '+heading+'\n' in report
assert report.rsplit('\n## ',1)[-1].startswith('Universal bridge\n')
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
write(RUN/'out/schema_validation.json',{'claim_fields_exact':True,'progress_fields_exact':True,'report_fields_present':True,'packet_delta_identical':True,'statement_sha256_valid':True,'full_fei':'OPEN'})
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='receipts.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(RUN)),'sha256':digest(p),'bytes':p.stat().st_size})
write(RUN/'out/receipts.json',{'created_at_utc':now,'files':receipts,'all_files_under20MB':True,'independent_review':'PENDING','supervisor_copy':'PENDING','mirror_verification':'PENDING'})
print(json.dumps({'run':str(RUN),'artifact_count':len(receipts)+1,'schema':'PASS','rolling_files':'updated','full_fei':'OPEN'}))
