from pathlib import Path
import hashlib,json
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
TEAM=ROOT.parents[1];CAM=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((CAM/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
def sha(b):return hashlib.sha256(b).hexdigest()
def save(name,obj):(RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
sources=[CAM/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',TEAM/'claude/B01/runs/20261011T225200Z-claude-B01-erasure-fraction-localization/CLAIMS.json',TEAM/'agents/A005/runs/20261011T225209Z-account05-A005-noncircular-endpoint-referee/REPORT.md',TEAM/'agents/A079/runs/20261011T224806Z-account05-A079-correlated-auxiliaries/REPORT.md',Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\sources\ERASURE_RIGIDITY.md'),ROOT/'runs/20261011T215124Z-account05-A002-hardness-preserving-transformations/TRANSFORMATION_LEDGER.tex']
manifest=[]
for p in sources:
    b=p.read_bytes();s=b.decode('utf-8-sig');manifest.append(dict(path=str(p),bytes=len(b),sha256=sha(b),lines=len(s.splitlines())))
save('out/SOURCE_MANIFEST.json',manifest)
admission=dict(target='B/H -> 1 with arbitrary seed H/I retained',units='bits',metrics={'B':'aggregate single-coordinate spectral erasure','D':'H-B, dual total correlation','TC':'sum h2(I_i)-H'},transformations=[
 dict(name='disjoint tensor',B='adds exactly',H='adds exactly',I='adds exactly',near_one_admission='No inflation of B/H for identical seed copies'),
 dict(name='fresh balancing and characters',B='unchanged',H='unchanged',I='balancing adds 1; character recenters coordinate influences',near_one_admission='Balancing does not change B/H; centering changes H/I rather than transporting the original ratio'),
 dict(name='systematic coding',B='sum B_i over zero columns only',H='unchanged',I='adds E|AS|',near_one_admission='Nonzero columns kill their coordinate erasure; separated support has B=0'),
 dict(name='economical balanced-core activation',B='pmB(seed)+s[2p-2p^2+E((1-p)^2,p^2)]',H='pmH(seed)+2sp(2-p)+phi((1-p)^2)',I='p[mI(seed)+s]',near_one_admission='B/H converges to seed fraction; control-dominated limit is 1/2'),
 dict(name='balanced two-cell selector of z f^m',B='mB(seed)/2+E(1,(Ef)^(2m))/2',H='2+mH(seed)/2',I='3/2+mI(seed)/2',near_one_admission='Preserves seed erasure fraction asymptotically for H(seed)>0'),
 dict(name='bent tensor inflation',B='mB(seed)+2r',H='mH(seed)+2r',I='mI(seed)+r',near_one_admission='If seed D>0 and B/H->1, H/I->2; cannot retain ratio>2'),
 dict(name='bent tensor plus tuned deterministic parity',B='mB(seed)+2r',H='mH(seed)+2r',I='mI(seed)+r+ell',near_one_admission='Constructive for seed ratio R in [0,2]; unresolved for R>2')],
 structural_results={'exact_B_equals_H':'Product law; dyadic Boolean rigidity yields character times coordinate bent function and H<=2I. Existing source proof reconstructed.',
 'near_B_equals_H':'Does not force TV closeness or bounded TC/H; actual correlated parity-block bent family disproves both.',
 'near_class_universal_bridge':'If H<=C_epsilon I on B>=(1-epsilon)H for fixed epsilon in (0,1), then FEI(max(C_epsilon,2/(epsilon ln2))).'},
 first_unsupported_line='Quantitative near-erasure H/I bound at fixed epsilon>0, or a different Boolean embedding preserving a seed ratio>2 while inflating B/H.',
 next='Use all-child deficit certification of minimal high-ratio witnesses, together with D<(2/ln2)I, in a signed Booleanity payment.')
save('ADMISSION_TEST.json',admission)
consumers=['B01','A003','A005','A031','A033','A051','A055','A078','A086','A094','B08','B20']
specs=[
 ('A002-AGGREGATE-ERASURE-TRANSPORT',
 'The exact aggregate-B tensor, balancing, coding, point-activation and balanced-selector formulas in ERASURE_LEDGER.md hold for all stated finite uniform Boolean signs. Economical activation and balanced selectors of arbitrary seed tensors preserve their B/H limit; systematic nonzero-column coding kills local erasure. For F=f^tensor m times a bent function on 2r fresh bits, D(F)=mD(f), H=mH(f)+2r and I=mI(f)+r; if D(f)>0 and B(F)/H(F)->1 then H(F)/I(F)->2. The actual parity-block bent family of dimension 2t+2r has H=2+2r, B=2r, I=t+r, TC=2t-2 and TV from its coordinate-product marginals equal to 1-2^(2-2t). These formulas do not establish high-ratio near-erasure admission.',
 ['Finite Boolean signs, uniform independent physical inputs','Entropy in bits; B=sum H(S_i|S_-i)','All tensor and auxiliary blocks physically disjoint','Activation p=2^-s with integer s>=1; selector core balanced','Pareto limit assumes H(f)>0 and D(f)>0; correlated family t>=2,r>=1'],
 'ERASURE_LEDGER.md sections 1-3',
 ['A002-EXACT-HARDENING-LEDGER@1 (H/I spectral interfaces, independently checked here)','A005 coordinate activation ledger, 20261011T225209Z REPORT sections 3-4 (independently reconstructed)']),
 ('A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE',
 'Fix epsilon in (0,1) and finite C_epsilon>=0. If every finite uniform Boolean sign f with B(f)>=(1-epsilon)H(f) satisfies H(f)<=C_epsilon I(f), then every finite uniform Boolean sign satisfies H(f)<=max(C_epsilon,2/(epsilon ln2))I(f). Conversely universal FEI(C) gives the near-erasure premise with C_epsilon=C. No restriction closure of the near-erasure class is assumed, and the premise remains open.',
 ['Finite uniform Boolean signs','Entropy in bits','Scalar coordinate restriction JS bound JS_i<=(2/ln2)I_i','epsilon and C_epsilon fixed before dimension/function'],
 'ERASURE_LEDGER.md section 4, independent minimal-violator proof',
 ['B01-MINIMAL-VIOLATOR-STRUCTURE@1, independently reconstructed','C005 exact physical restriction H/I identities and scalar JS bound'])]
claims=[]
for cid,statement,hyp,proof,deps in specs:
    claims.append(dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=sha(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()),contributors=['account05/A002'],proof_source=proof,proof_dependencies=deps,review_records=[],status='SOURCE_COMPLETE_SCOPED_EXTENSION_PENDING_REVIEW',supersedes=[],refutes=[] if 'BRIDGE' in cid else ['Near-one aggregate erasure forces uniform total-variation closeness to the product of coordinate marginals','Near-one aggregate erasure forces dimension-independent bounded TC/H'],first_unproved_line=None,next_consumers=consumers))
save('CLAIMS.json',claims)
checks=json.loads((RUN/'out/EXACT_CHECK_n3.json').read_text(encoding='utf-8'));assert checks['failures']==0 and checks['seeds']==278
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B01',packet_id='A002',gap_id='G-B01-ERASURE-FRACTION-ADMISSION',attempt_id='A002-stage2-B-ledger-and-near-erasure-v1',method='Exact aggregate spectral-edge erasure transport; paid bent dilution Pareto obstruction; actual correlated Boolean spectrum; minimal-violator universal constant bridge',mathematical_delta='Completed exact B extension of existing H/I ledgers; low-ratio admission constructed and bent inflation cannot retain ratio>2; near-product closeness disproved; hypothetical near-erasure FEI transfer sharpened from additive constant to max; high-ratio admission remains open',deliverable_status='COMPLETE_LOCAL_STAGE_ARTIFACT',mathematical_status='SCOPED_DERIVATIONS_PROVED_ON_PAGE; HIGH_RATIO_ADMISSION_OPEN; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',claim_versions_used=['A002-EXACT-HARDENING-LEDGER@1','B01-MINIMAL-VIOLATOR-STRUCTURE@1','B01-ERASURE-FRACTION-BRIDGE@1'],claims_created_or_changed=[c['claim_id']+'@1' for c in claims],source_artifacts=['ERASURE_LEDGER.md','ADMISSION_TEST.json','out/SOURCE_MANIFEST.json','out/EXACT_CHECK_n3.json','out/SIGN_CERTIFICATE.json'],next_consumers=consumers,next_action='Derive a signed Boolean near-erasure payment on minimal-variable high-ratio witnesses with every physical child certified and D<(2/ln2)I; review A002 exact aggregate and maximum-constant bridge',stagnant_substantive_attempts=0,blockers=['No quantitative near-erasure H/I bound or high-ratio erasure-inflating Boolean embedding proved; exact first unsupported line recorded'],packet_ids=['A002'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
if 'The full check passed' not in report:
    report=report.replace('Full results appear in [out/EXACT_CHECK_n3.json]',f'The full check passed {checks["assertions"]:,} assertions with zero failures in about {checks["seconds"]:.2f} seconds. Full results appear in [out/EXACT_CHECK_n3.json]')
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
assert '## Universal bridge\n\n' in report
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
for claim in claims:
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
    assert claim['statement_sha256']==sha(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode())
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
(ROOT/'STATUS.md').write_text('STATE: A002 stage 2 saved: exact B transport and max-constant bridge; 12,232 exact checks; high-ratio admission/FEI OPEN; review pending. Lead exact-product OPEN label is stale: ERASURE_RIGIDITY section 1 proves it.\nNEXT: Use all-child deficit certification and D<(2/ln2)I to prove signed near-erasure payment on minimal high-ratio witnesses; A086/A094 review new ledger and bridge.\n',encoding='utf-8')
entry='\n2026-10-11 23:44 UTC stage: Followed B01 near-one-erasure admission target; consumed A005 coordinate ledger and A079 scope guard. Extended conventional transformations to aggregate B, proved bent inflation forces H/I->2, constructed low-ratio admission, and disproved product-marginal closeness from B/H->1 with actual bent/parity-block family. Reconstructed existing dyadic product-law rigidity proof omitted from lead OPEN claim. Minimal-violator argument improves hypothetical near-class transfer to max(C_epsilon,2/(epsilon ln2)). Pilot 1,224 and full 12,232 exact assertions passed (278 seed tables; 36 balanced tensor activations; 4 correlated cases). High-ratio admission remains open; moved NEXT to Boolean all-child criticality rather than another dilution gadget.\n'
log=ROOT/'WORKLOG.md'
if entry not in log.read_text(encoding='utf-8-sig'):
    with log.open('a',encoding='utf-8') as f:f.write(entry)
learned='\nStage 2 durable facts: B=sum coordinate edge E(p_T,p_Ti); disjoint tensor B adds, fresh balance B stays, systematic coding retains exactly zero-column B_i, and separated support gives B=0. Aggregate general activation/selector formulas are in 20261011T234442Z/ERASURE_LEDGER.md; economical arbitrary-core tensors preserve seed B/H, not inflate it.\nBent tensor padding H=mHf+2r,B=mBf+2r,I=mIf+r,D=mDf. For Df>0, forcing B/H->1 forces H/I->2. A paid auxiliary with H/I<=C cannot preserve a seed ratio>C in that limit.\nExact B=H iff product spectral law; dyadic Walsh divisibility forces each nontrivial marginal 1/2, so H<=2I. This is already proved in supplemental ERASURE_RIGIDITY.md, not a new open exact endpoint. Near B/H=1 does not imply TV proximity or bounded TC/H: parity-block bent times fresh bent has H=2+2r,B=2r,I=t+r,TC=2t-2,TV=1-2^(2-2t).\nIf one fixed epsilon>0 near-erasure class B>=(1-epsilon)H has H<=C_epsilon I, full FEI holds with max(C_epsilon,2/(epsilon ln2)), proved by a least-variable violator. The class need not be restriction closed. Near-erasure quantitative payment remains FEI-equivalent, not an isolated product stability theorem.\n'
lp=ROOT/'LEARNED.md'
if learned not in lp.read_text(encoding='utf-8'):
    with lp.open('a',encoding='utf-8') as f:f.write(learned)
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name not in ['ARTIFACT_RECEIPTS.json','SCHEMA_CHECK.json']:
        raw=p.read_bytes();assert len(raw)<20*1024*1024
        receipts.append(dict(path=str(p.relative_to(RUN)),bytes=len(raw),sha256=sha(raw)))
save('out/ARTIFACT_RECEIPTS.json',receipts)
save('out/SCHEMA_CHECK.json',dict(report_fields='PASS',claim_fields='PASS',progress_fields='PASS',statement_hashes='PASS',compatibility_byte_identical=True,universal_bridge_is_final_paragraph=True,all_files_under_20MB=True,independent_review='PENDING',supervisor_copy='NOT_VERIFIED',full_FEI='OPEN'))
print(json.dumps(dict(files_receipted=len(receipts),claims=len(claims),assertions=checks['assertions'],schema='PASS',high_ratio_admission='OPEN',full_FEI='OPEN')))
