from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pilot=read(R/'out/pilot.json');main=read(R/'out/full.json');carrier=read(R/'out/CARRIER.json')
assert all(x['status']=='PASS' for x in (pilot,main,carrier))
assert main['representations']==4096 and main['physical_splits']==16384 and carrier['carriers']==44
old=read(A/'runs/20261023T135203Z-fleet03-A026-good-coordinate-erasure/CLAIMS.json')[0]
peer=Path(r'agents\A029\runs\20261026T213208Z-fleet04-A029-child-deficit-transport')
pc=read(peer/'CLAIMS.json')[0]
statement=('Scoped independent reconstruction of A029@5: for every supplied-reference Boolean mux on independent controller/DATA cubes, '
 'the true-occupancy calibrated odds target ell=(1-epsilon)k+epsilon eta, real epsilon in[0,1/16], has excess C<=31eta/160<=eta/2; '
 'all eta0/1 and zero-controller-variance endpoints are retained. The supplied allowance theorem holds for entropy-path plus full-terminal CE, '
 'equivalently initial CE plus signed resets MINUS explicit physical-query KL refunds. The unrefunded raw bill has the additional sum w L, '
 'which is not asserted paid here. A026@6 code already subtracts that term and is not refuted. '
 'For a single dictator controller and exact source references, EVERY covering odds target preserving true DATA row marginal loses its ENTIRE divergence C on the controller query, with both inherited children exact and true outcome normalizers. '
 'An admissible AND2 relative-odds target gives L=(1/4)log2(9/8)>0; an admissible calibrated three-bit point target has '
 '16L=log2(2^80*3^6/(5^10*7*11^3*19^9*31^3))>0. '
 'For every Boolean h and integer m>=1, F=AND2 times m disjoint h copies has H=2+mH(h), I=1+mI(h), '
 'all occupied controller odds k=eta=1/2, zero calibrated conversion cost and a ROOT coordinate with B_i/I_i=2. '
 'Each gate erasure is1 before the first gate query and0 afterward; the first gate entropy decrement is2=1 erasure+1 JS. '
 'The restriction closure contains arbitrary h at m1, and every adaptive mixed restriction tree splits exactly into gate and core entropy/influence telescopes. '
 'Thus this root good-coordinate class is full-FEI-hard and gives no hereditary selection theorem. Full FEI and an ORIGINAL arbitrary-core O(I) source remain OPEN.')
claim={
 'claim_id':'A026-CALIBRATED-FLOOR-ROOT-SELECTION-AUDIT','version':1,'exact_statement':statement,
 'hypotheses':['finite uniform Boolean cubes','base2 entropy','supplied covering references with actual inherited phase channels and declared ghost completion',
  'true-weighted calibration, not reference-weighted calibration','all original source and terminal entropy retained','disjoint blocks in carrier reduction'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A026 independent reconstruction; carrier extension','A029 original calibrated-floor and carrier theorem','A094 original general query-KL accounting distinction'],
 'proof_source':str(R/'DERIVATION.md'),'proof_dependencies':[
  {'claim_id':pc['claim_id'],'version':pc['version'],'statement_sha256':pc['statement_sha256'],'scope':'reviewed calibrated scalar and endpoint account; exact carrier baseline'},
  {'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256'],'scope':'own exact refund convention, checked against source code'}],
 'review_records':[{'reviewer':'A026','source_claim_id':pc['claim_id'],'source_version':pc['version'],'verdict':'HOLDS_AT_EXPLICIT_ENDPOINT_FUNCTIONAL_SCOPE','source':str(R/'DERIVATION.md'),'independence':'convex endpoint reconstruction; different exact checker; no substantive repair to source theorem'}],
 'status':'AUTHOR_PROOF_AND_EXACT_FINITE_CHECKS; NEW_CONSEQUENCES_REVIEW_PENDING; FULL_FEI_OPEN',
 'supersedes':[],'refutes':[],'first_unproved_line':'An ORIGINAL influence-priced arbitrary-core source and hereditary stopping policy; unrefunded raw payment additionally requires sum w L paid from SAME actual unused owner.',
 'next_consumers':['A028','A029','A030','A087','A094','A096','A097','A099','B20']}
write(R/'CLAIMS.json',[claim])
total=main['assertions']+carrier['assertions']
next_action='A028/A029/A087/A094 review the explicit refund/endpoint distinction and root-K2 carrier restriction ledger; supply a DATA-sensitive hereditary arbitrary-core stopping rule and ORIGINAL O(I) reference, or price its raw query-KL term from SAME unused owner.'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B06','packet_id':'A026','gap_id':'A026-SAME-SOURCE-HISTORY-PAYMENT',
 'attempt_id':'stage22-calibrated-floor-review-root-versus-hereditary-selection','method':'Independent calibrated-KL endpoint reconstruction; exact full physical-channel ledger; arbitrary-core carrier erasure and adaptive component telescopes',
 'mathematical_delta':'A029@5 scoped HOLDS. Explicit positive admissible query-KL witnesses; A026@6 already subtracts refunds. Full-FEI-hard calibrated class has root good-coordinate K2 but exposes arbitrary cores under restriction. No universal constant gain.',
 'deliverable_status':'COMPLETE_LOCAL; SUPERVISOR_MIRROR_UNVERIFIED','mathematical_status':'PROOF_WITH_EXACT_FINITE_VALIDATION; NEW_CONSEQUENCES_EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':[str(R/'out/SOURCE_RECEIPTS.json'),str(R/'out/SOURCE_EXCERPTS.json'),str(R/'DERIVATION.md')],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal ORIGINAL arbitrary-core source unpaid','Root good-coordinate class is not restriction closed','Raw transaction query-KL term not automatically paid','Lean and administrative receipts retain their actual recorded status','External review and supervisor mirror unverified'],
 'packet_ids':['A026']}
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
sections=[
 ('exact target, quantifiers, hypotheses and units','Review A029@5 for all finite uniform Boolean muxes with once-supplied covering references and real epsilon in[0,1/16]. Distinguish entropy-path/full-terminal payment from an unrefunded physical transaction bill. Extend the arbitrary-core AND2 carrier reduction to exact B_i, entropy decrement and arbitrary adaptive mixed restriction trees. All units bits; no all-coordinate bound, hereditary universal selection, original-source supplier or full FEI theorem is claimed.'),
 ('sources actually read, revisions and theorem locators','Fresh BOARD, B06 v2 notes, own rolling state and stage21 proof/checker; full execution protocol2026-10-11-execution-v2; campaign and supplemental intake with focused registry/source passages; four supplied paper texts at relevant composition/restriction locators. Detailed mathematical sources: A02920261026T213208Z DERIVATION1-6 and CLAIMS, A09420261026T232939Z DERIVATION1-2. All read source hashes and decoding choices appear in out/SOURCE_RECEIPTS.json and locators in SOURCE_EXCERPTS. No fresh paper audit or internet attribution is claimed. Required brain wake flagged stale personalization/dream sources; those notes are not mathematical premises.'),
 ('complete derivation or exact first unsupported line','DERIVATION1 reconstructs calibrated C<=31eta/160 and the inherited eta allowance, retaining endpoints. Sections2-3 prove the physical-ledger identity with sum w L and two exact admissible strict-loss witnesses. Own stage21 checker lines67-74 already subtracts that refund, so its endpoint theorem is NOT refuted. Section4 proves root B_i/I_i=2 on the AND2 carrier class while its restriction closure contains every Boolean core, and decomposes all adaptive mixed entropy/influence paths without renewing gate surplus. First unpaid line: an ORIGINAL O(I) source and genuinely hereditary DATA-sensitive stopping rule. No numerical quota failure is inferred from a positive refund.'),
 ('executed validation with domain, arithmetic, commands and outputs',f'Frozen out/FROZEN_SPEC*.json and CARRIER_SPEC precede jobs. Commands: python -X utf8 code/check.py pilot; code/check.py full; code/carrier.py; code/intake.py; code/finalize.py, each with python -X utf8. Final pilot {pilot["representations"]} representations/{pilot["assertions"]} assertions in{pilot["seconds"]:.3f}s, separate from totals. Main ALL4096 labelled two-bit controller/source-pair representations,16384 actual physical splits,{main["assertions"]} exact assertions in{main["seconds"]:.3f}s. No symmetry reduction. Exact rational Walsh, full reference normalization and prime-log identities; scalar signs use24-term rational atanh bounds with proved remainder. Two strict witness signs have integer certificates. Independent direct-character/edge carrier checker imports no main code:44 carriers from all h on0..2 bits and m1,2;1294 adaptive nodes;{carrier["assertions"]} assertions in{carrier["seconds"]:.3f}s. Total final main+carrier={total}; failed or repeated checks are not added. First full helper timed out at55s without a failed mathematical predicate; cache-only V3 amendment retained domain and cap. Timeout receipt is preserved. Estimated140MB main/80MB alternate, observed peak unmeasured; no job>300MB research search, GPU, dimension escalation or detached process. Lean receipt is separate and certifies at most its real-algebra statement.'),
 ('proof dependencies and changed downstream conclusions','A029@5 scalar/endpoint/calibrated-carrier clauses independently reconstruct unchanged. A026@6 remains at its explicitly refunded endpoint scope; no correction of its proved inequality is needed. A094 query-KL distinction is independently exhibited inside the actual A026 and A029 target classes, rather than transferring an unrelated counterexample. The carrier extension proves a concrete root K2 selection theorem on a full-FEI-hard nonhereditary class. This does not improve a universal FEI constant. New audit consequences await A028/A029/A087/A094 review.'),
 ('one next mathematical action and independent reviewer',next_action+' Further floor-only parameter sweeps and root-only carrier selections do not address this gap.'),
 ('actual persistence receipts or precise save blocker','All four exact-schema protocol files, complete derivation, code, frozen specifications, source hashes, exact outputs and timeout receipt are local in the assigned A026 run. This finalizer checks schemas, statement hash, compatibility equality and<20MB sizes, and saves out/PERSISTENCE_RECEIPT.json. STATUS has two lines; dated WORKLOG and LEARNED updates persist. Supervisor upload, canonical adoption and independent review remain unverified. No git, mail, messages, brain research writes, other-agent changes, deletions, trading actions or remote compute. No own research calculation is intentionally left running. Administrative/Lean receipts state actual outcomes; no automatic green status is inferred.')]
report='# A026 stage22: calibrated-floor review and hereditary selection boundary\n\n'+'\n\n'.join('## '+k+'\n\n'+v for k,v in sections)
report+='\n\n## Universal bridge\n\nC018 good-coordinate erasure and C019/C024 stopping/history accounting gain an exact boundary: the calibrated full-FEI-hard AND2 carrier class has root B_i<=2I_i yet exposes arbitrary cores under restriction, while endpoint payment differs from raw transactions by the explicitly retained sum w L. A029 calibrated admission reconstructs and A026 prior refunded accounting remains valid. Universal constant gain is zero; the original arbitrary-core source and hereditary policy are unpaid. NEXT tests that required source/policy against the retained mH(h) core debt and actual query losses, which addresses the universal bridge directly instead of extending an already paid floor class.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(A/'STATUS.md').write_text(f'STATE: Stage22 saved: A029 calibrated-floor endpoint theorem HOLDS; positive admissible query-KL explicitly retained; full-FEI-hard AND2 carriers rootK2 but not hereditary;{total} exact checks;FEI OPEN.\nNEXT: A028/A029/A087/A094 review carrier/full-refund scope; fund ORIGINAL arbitrary-core source and required DATA-sensitive hereditary policy from SAME unused owner, retaining core entropy and raw queryKL if charged.\n',encoding='utf-8',newline='\n')
date=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{date} stage22 {R.name}: independently reconstructed A029@5 scalar and endpoint account; exact admissible query-KL witnesses. Prior A026 code already subtracts full refund, so no false refutation. AND2 arbitrary-core carrier has rootK2 but arbitrary-core hereditary closure; adaptive component account proved. Final main{main["assertions"]}+independent{carrier["assertions"]}={total}; initial55s timeout retained and cache-only rerun. NEXT original arbitrary-core source/hereditary DATA policy; FEI OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{date} stage22: (1) A029@5 calibrated C<=31eta/160 independently HOLDS at endpoint/full-terminal functional scope. (2) Raw initialCE+signed resets = Hroot+E Dterminal+sum queryKL; own@6 code already subtracts refunds. Positive L alone does not refute quota inequality. Exact AND2 L=log2(9/8)/4; calibrated point3 witness positive by integer product. (3) AND2*h^m has H=2+mHh,I=1+mIh,gate B=1/Inf1/2 (rootK2),first gate DeltaH2=B1+JS1; arbitrary h survives restriction. Root selection on a FEI-hard class need not be hereditary. Any adaptive mixed tree factors nodewise, gate credit counted once. Initial arbitrary-core supplier remains unpaid; no further floor-only sweeps.\n')
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert all('## '+h in report for h in protocol['report_fields'])
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  receipts.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
write(R/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS_LOCAL_ONLY','at_utc':date,'final_exact_assertions':total,'files':receipts,'rolling':[{'path':str(A/f),'sha256':sha(A/f)} for f in ['STATUS.md','WORKLOG.md','LEARNED.md']],'mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS_LOCAL_ONLY','assertions':total,'claim':claim['claim_id'],'run':str(R)}))
