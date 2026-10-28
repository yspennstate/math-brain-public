from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];BASE=AGENT.parents[1]
def rd(p):return p.read_text(encoding='utf-8-sig')
def js(p):return json.loads(rd(p))
def wr(p,t):p.write_text(t,encoding='utf-8')
def dump(p,x):wr(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
v=js(ROOT/'out/validation.json');j=js(ROOT/'out/js_validation.json');pilot=js(ROOT/'out/pilot.json')
assert v['status']==j['status']==pilot['status']=='PASS'
assert (v['seed_queries'],v['transactions'],v['full_terminal_references'])==(88,704,1408)
assert (j['eligible_zero_singleton_seeds'],j['controller_sign_cases'])==(78,468)
assert v['helper_sha256']==sha(ROOT/'code/check.py') and j['helper_sha256']==sha(ROOT/'code/review_js.py')
assert pilot['helper_sha256']==sha(ROOT/'code/check_v1.py')
src97=BASE/'agents/A097/runs/20261023T062140Z-account03-A097-cross-route-transfer'
src93=BASE/'agents/A093/runs/20261023T070224Z-account03-A093-literature-and-priority'
ids=['A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER','A093-ZERO-SINGLETON-JS-REFUND-REFINEMENT']
claims=[];anchors=[]
for src,cid,proof in ((src97,ids[0],'REVIEW_A097.md'),(src93,ids[1],'REVIEW_A093.md')):
 c=next(x for x in js(src/'CLAIMS.json') if x['claim_id']==cid)
 declared=c['statement_sha256'];computed=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
 anchors.append({'claim_id':cid,'source':str(src/'CLAIMS.json'),'source_file_sha256':sha(src/'CLAIMS.json'),'source_declared_statement_sha256':declared,'printed_statement_utf8_sha256':computed,'match':declared==computed})
 if declared!=computed:
  assert cid==ids[1] and computed=='f3d5c4417721b4ddfcd9f5140bbf4c0c01969bc2d7958a8d000a21167f2b02b4'
  c['statement_sha256']=computed
 c['review_records'].append({'reviewer':'A033','run_id':ROOT.name,'verdict':'HOLDS_AT_STATED_SUPPLIED_CURRENT_SOURCE_SCOPE','method':'Independent analytic reconstruction of full support/calibration/occupancy/refund/mixture chain; own exact character and FWHT certificates; no source helper imported; no substantive repair','evidence':[str(ROOT/proof),str(ROOT/'out/validation.json'),str(ROOT/'out/js_validation.json')],'scope':'Unchanged original theorem only; no arbitrary-core initial influence price or necessary zero-energy conversion supplied'})
 c['status']='INDEPENDENT_REVIEW_HOLDS_AT_STATED_SUPPLIED_SOURCE_SCOPE'
 if declared!=computed:
  c['review_records'][-1]['source_declared_statement_sha256']=declared
  c['review_records'][-1]['binding']='Unchanged printed statement at computed SHA256; source hash mismatch corrected in local copy ONLY; no mathematical repair; source author reconciliation pending'
  c['status']='INDEPENDENT_REVIEW_HOLDS_PRINTED_STATEMENT_SOURCE_HASH_CORRECTED_LOCALLY'
 claims.append(c)
dump(ROOT/'out/SOURCE_HASH_AUDIT.json',{'status':'SOURCE_METADATA_MISMATCH_EXPLICITLY_BOUND','anchors':anchors,'source_author_action':'A093 reconcile declared hashes with exact printed statement; shared files unchanged'})
dump(ROOT/'CLAIMS.json',claims)
nxt='A093 reconcile its declared statement hash with the printed source (local review binds computed f3d5c441...); consume A003/A004 current-source discrepancy certificates only at their exact hypotheses; identify a NECESSARY EXACT-MATCHED isospectral conversion at actual completion or prove it avoidable, and pay any unavoidable complete liability from SAME unused original ancestor influence, retaining arbitrary-core initial CE, old debits and BOTH terminals. A097/A093/A032/A079/A094 review the handoff.'
p={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B07','packet_id':'A033','gap_id':'G-BOOLEANITY','attempt_id':'A033-INDEPENDENT-PHASE-BIN-JS-REVIEW-1','method':'Consume fresh A097 and A093 dependencies; independent complete-reference analytic reconstruction; exact direct-character/Fraction panel and independent FWHT prime-log fixture','mathematical_delta':'A097 phase-bin theorem and A093 stronger zero-singleton JS refund independently HOLD without repair. The positive-sector energy improves by128/7 for fixed A079 controller: epsilon7/519 becomes1/5 in the full actual Boolean witness. Full terminal increment exactly(3/8)log2(5/8)<0. Isospectral nullspace and arbitrary-core initial source remain unpaid; full FEI OPEN. No new broad candidate opened.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'TWO_UNCHANGED_SCOPED_DEPENDENCIES_INDEPENDENTLY_REVIEWED; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'use':'Independent review, no theorem statement change or upstream universal source assumption'} for c in claims],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'A033 independent acceptance without repair; no new candidate'} for c in claims],'source_artifacts':['REVIEW_A097.md','REVIEW_A093.md','FROZEN_SPEC.json','PANEL_FROZEN_SPEC.json','JS_FROZEN_SPEC.json','code/check_v1.py','code/check.py','code/review_js.py','out/pilot.json','out/full_attempt.json','out/validation.json','out/js_validation.json'],'next_consumers':['A097','A093','A096','A003','A004','A032','A079','A094','B07','B20'],'next_action':nxt,'stagnant_substantive_attempts':0,'blockers':['No universal influence-priced arbitrary-core initial reference','No necessity/selection theorem paying exact-matched isospectral conversion from same unused ancestor account','Separate original cyclic atom-cap-prefix construction/checker still absent locally; do not invent full import','Source registry adoption and supervisor remote publication unverified','Original full2208-transaction attempt timed out at frozen55s; only explicit smaller panel and separate all-zero-singleton audit completed'],'packet_ids':['A033']}
p['mathematical_delta']+=' SAVE AUDIT: A093 declared4a115d... does not match its unchanged printed statement, computed f3d5c441...; local review uses computed hash and records both. No mathematical repair; source-author metadata reconciliation pending.'
p['source_artifacts'].append('out/SOURCE_HASH_AUDIT.json')
p['blockers'].append('A093 source-declared hash mismatch; corrected only in local review copy, source-author reconciliation pending')
dump(ROOT/'PROGRESS.json',p);wr(ROOT/'PACKET_DELTA.json',rd(ROOT/'PROGRESS.json'))
dump(ROOT/'out/formal_status.json',{'status':'NOT_LAUNCHED','reason':'No formal certificate claimed; proof reviewed analytically and exact finite certificates checked by Python. Each job estimated70MB, so no >300MB job or memok admission was needed.'})
report=f'''# exact target, quantifiers, hypotheses and units

Independently review A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER@1 and consume the fresh A093-ZERO-SINGLETON-JS-REFUND-REFINEMENT@1 at their EXACT stated hypotheses: every finite actual Boolean seed, complementary independent physical controller, full CURRENT coherent finite-CE supplied source, both outcomes and all old debits retained. Entropy/CE/KL are bits. Verdicts HOLDS WITHOUT REPAIR at supplied-source scope. No universal initial rate, new broad A033 candidate or FEI theorem is asserted. Full FEI OPEN.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2 (full read); machine AGENTS.md; current BOARD relevant B07/A093/A003/A004 rows; B07 STREAM_NOTES v2 Oct11; own prior STATUS and 06:50 proof/check/finalizer/progress artifacts; crash-restoration common guidance; A097 run20261023T062140Z DERIVATION sections1-4 and original CLAIMS; A093 run20261023T070224Z DERIVATION sections1,3,4 and original CLAIMS. Exact statement hashes and source paths in CLAIMS.json and out/SOURCE_MANIFEST.json. A093 literature paragraph was read for context; no external literature priority claim or unchecked paper theorem is used, so no web search was needed. Prior packet source baseline remains inherited; not represented as freshly reread.

# complete derivation or exact first unsupported line

REVIEW_A097.md reconstructs normalization, actual restriction spectra, support propagation, per-bin calibration, SAME inherited comparison law, Pinsker/parallelogram, Gram minimum, full mixture liability, exact occupancy chain and finite-tree telescope. All-positive/all-negative bin merging proves optimality of two sign bins. REVIEW_A093.md independently derives the exact common-reference JS decomposition and controller factor cancellation BEFORE Pinsker: at d=0, refund>=beta*V^2/(2ln2). Thus y=beta*V^2/4 pays epsilon=y/(t+y), retaining y/ln2 after the mixture. For fixed controller, y/x=128/7 wherever energy is positive; the Boolean witness changes epsilon7/519 to1/5. Exact full signed increment is(3/8)log2(5/8)<0, with both complete children and strictly positive reset liability.

At d=0,V=0, all u_T*v_T vanish; actual occupancy fibers are points and erasure is0. At exact current source all calibration refunds are0, while mismatched sources MAY release prepaid KL. This retains the corrected scope of the majority/product-block obstruction. The first unsupported universal line is an influence-priced initial reference for an arbitrary Boolean core, or proof that a specific isospectral conversion is NECESSARY and payable from SAME unused original ancestor influence. Neither accepted theorem proves it. No generic divergence identity is advertised as a new Booleanity admission inequality. Complete signed convolution at every shift/restriction remains the hierarchy; fixed prefixes, dyadic coefficients and small defects are not reused as admission criteria. Original cyclic atom-cap-prefix source/checker still absent locally.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede all checks. Pilot command: python -B -X utf8 code/check_v1.py --pilot (originally code/check.py); all20 n<=2 truth tables,160 transactions,320 full terminals,{pilot['exact_assertions']} exact assertions PASS in{pilot['runtime_seconds']:.6f}s. Original full276-seed/2208-transaction main hit its frozen55s cap; out/full_attempt.json records INCOMPLETE_TIMEOUT with NO completed exhaustive count. No mathematical assertion failed; no exhaustive n=3 transaction pass is inferred.

Separately frozen panel command: python -B -X utf8 code/check.py --panel. All20 n<=2 truth tables plus68 specified n=3 tables;88 seed queries,704 transactions,1408 full terminal references,{v['exact_assertions']} exact assertions PASS in{v['runtime_seconds']:.6f}s. Both signs, actual/uniform calibrated sources and single/sign partitions checked; direct integer characters and Fraction certify full laws, support, normalization, calibration multipliers, exact common-reference parallelogram and mixture floors. Transcendental inequalities are proved analytically rather than inferred from floats.

Separately frozen JS command: python -B -X utf8 code/review_js.py. ALL78 zero-singleton truth tables n<=3, three controllers including beta0/beta1, both signs:468 cases,{j['exact_assertions']} assertions PASS in{j['runtime_seconds']:.6f}s. Independent integer FWHT verifies the four full physical fixture terminals. Complete entropy/CE cancellation is an exact rational combination of prime logarithms; sign follows from5<8. No float sign, automatic dimension escalation, GPU, new worker or >300MB job. Formal compiler not launched; no formal acceptance claimed.

# proof dependencies and changed downstream conclusions

The two original exact statements/hypotheses/contributor lists/hashes are preserved, with A033 independent review records appended. A097 was already independently reviewed by A093; this stage reconstructs it separately and additionally accepts A093's then-pending stronger certificate. No substantive repair, cycle in proof dependencies or new universal source premise. Consumers should use the stronger JS energy in the zero-singleton NONISOSPECTRAL sector, retaining current-reference support and all full terminal CEs. That finite positive-sector gain does not alter the exact nullspace or initial arbitrary-core liability. Prior fixed-strength obstruction remains valid.

# one next mathematical action and independent reviewer

{nxt}
Saved source-bound handoff only; no external message or claimed downstream adoption.

# actual persistence receipts or precise save blocker

Four protocol files, both reviews, all frozen specs, preserved original helper, exact outputs and source manifest are saved locally. out/PERSISTENCE_RECEIPT.json checks exact field sets, original statement hashes, source/helper/output hashes, size caps, identical progress/delta and two-line STATUS. WORKLOG and LEARNED are appended with dated results. The07:06 invocation was unstarted before the10:53 replacement; no mathematical result is assigned to it. Crash recovery found no own research job needing restart; only explicitly frozen new bounded checks were run. Remote copying/publication belongs to the supervisor and is UNVERIFIED. Research stayed inside A033; shared inputs read-only; no git, mail, brain writes, trading access, worker creation or stopping others. Brain self-care remains degraded/unverified (latest owner-model97h and state-of-mind81.6h stale); personal context freshness is affected, and those notes were not used as mathematical authority.

REPORT: Done: two unchanged scoped proofs independently accepted; exact completed domains stated above.
REPORT: Stopped: only own full attempt at its frozen55s cap; no completed certificate inferred.
REPORT: Left running: none owned; universal FEI/source-payment gap remains open.

# Universal bridge

This stage moves C024 history transfer by independently accepting both the supplied-source phase-bin transaction and its stronger zero-singleton JS refinement: fixed-controller positive-sector energy improves by128/7 and the complete Boolean fixture permits epsilon1/5 rather than7/519, with every old debit and terminal retained. It gains ZERO universal initial influence price; C018/C019 remain open. NEXT addresses necessity/selection and SAME unused original ancestor payment at an exact-matched isospectral/completion frontier, or the original arbitrary-core source itself. That is the shortest universal route exposed by the accepted mechanisms: increasing finite Booleanity prefixes or repeating prescribed off-image resets cannot supply the missing price.
'''
report=report.replace('Exact statement hashes and source paths in CLAIMS.json and out/SOURCE_MANIFEST.json.','Exact PRINTED-statement hashes and source paths in CLAIMS.json, out/SOURCE_HASH_AUDIT.json and out/SOURCE_MANIFEST.json. SAVE AUDIT FOUND: A093 source declares4a115d... but its unchanged printed statement hashes f3d5c441...; local review binds the computed hash and records the declared one. A097 declared/computed hash matches. No source was edited; A093 reconciliation pending.')
report=report.replace('The two original exact statements/hypotheses/contributor lists/hashes are preserved,','The two original exact statements/hypotheses/contributor lists are preserved; A097 hash matches and A093 hash is explicitly corrected only in the local copy to match its unchanged printed text,')
report=report.replace('original statement hashes, source/helper/output hashes','computed printed-statement hashes, explicit original-hash mismatch, source/helper/output hashes')
report=report.replace('before writing CLAIMS','before writing CLAIMS')
report=report.replace('Research stayed inside A033;','An initial save failed on the A093 source-hash mismatch, and premature readback found no receipt; those failures are retained in out/SAVE_AUDIT_FAILURES.md. Research stayed inside A033;')
wr(ROOT/'REPORT.md',report)
wr(AGENT/'STATUS.md',f'STATE: A097 and A093 printed JS theorem independently HOLD;704 transactions+468 zero-singleton cases PASS;A093 declared hash MISMATCH, local review binds computed f3d5c441...;FEI OPEN.\nNEXT: A093 reconcile source hash; NECESSARY exact-matched isospectral/completion conversion or arbitrary-core initial source, paid SAME unused ancestor influence; A003/A004 scope, old debits/BOTH terminals retained.\n')
entry=f'\n{now} - {ROOT.name}: Independently accepted A097 phase-bin@1 and fresh A093 JS-refund@1 without repair, preserving original statement hashes/contributors. Positive-sector y=beta*TV^2/4 improves fixed-controller energy by128/7; actual full Boolean fixture epsilon1/5, complete increment(3/8)log2(5/8)<0 checked as exact prime-log coefficients. Pilot{pilot["exact_assertions"]} checks; full2208 attempt timed frozen55s (incomplete, no successful exhaustive claim); new frozen704-transaction panel{v["exact_assertions"]} checks and separate ALL78 zero-singleton seeds/468 controller-sign cases{j["exact_assertions"]} checks PASS. beta0/beta1 endpoints retained. Isospectral d=0,V=0 has point occupancy and zero erasure; ALL refund zero asserted only for exact incoming source, not mismatched references. Universal initial arbitrary-core source price and necessity/global ancestor-payment gap remain OPEN. No new broad candidate; older07:06 invocation unstarted, latest10:53 stage owns these results.\n'
entry=entry.replace('preserving original statement hashes/contributors','preserving exact printed statements/contributors; A097 hash verified, A093 declared4a115d... mismatches printed computed f3d5c441..., local copy corrected with both anchors recorded and source-author reconciliation pending')
for name in ('WORKLOG.md','LEARNED.md'):
 old=rd(AGENT/name)
 if ROOT.name not in old:wr(AGENT/name,old+entry)
sources=[BASE/'BOARD.md',BASE/'claude/B07/STREAM_NOTES.md',src97/'DERIVATION.md',src97/'CLAIMS.json',src93/'DERIVATION.md',src93/'CLAIMS.json',AGENT/'runs/20261023T065015Z-account03-A033-derivative-hierarchy/PROGRESS.json',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
dump(ROOT/'out/SOURCE_MANIFEST.json',[{'path':str(x),'sha256':sha(x),'role':'actually read; hash at final save; mutable board may update'} for x in sources])
fields=set('protocol_revision run_id stream packet_id gap_id attempt_id method mathematical_delta deliverable_status mathematical_status claim_versions_used claims_created_or_changed source_artifacts next_consumers next_action stagnant_substantive_attempts blockers packet_ids'.split())
cf=set('claim_id version exact_statement hypotheses statement_sha256 contributors proof_source proof_dependencies review_records status supersedes refutes first_unproved_line next_consumers'.split())
assert set(p)==fields
for c in js(ROOT/'CLAIMS.json'):assert set(c)==cf and hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len(rd(AGENT/'STATUS.md').splitlines())==2
for heading in js(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']['report_fields']:assert '# '+heading in report
assert report.rfind('# Universal bridge')>report.rfind('REPORT:')
files=[x for x in ROOT.rglob('*') if x.is_file() and x.name!='PERSISTENCE_RECEIPT.json'];assert all(x.stat().st_size<20*1024*1024 for x in files)
dump(ROOT/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS','at':now,'field_sets_exact':True,'printed_statement_hashes_verified':True,'A093_source_declared_hash_mismatch_recorded':True,'progress_delta_identical':True,'rolling_status_two_lines':True,'file_count':len(files),'files':[{'path':str(x.relative_to(ROOT)),'bytes':x.stat().st_size,'sha256':sha(x)} for x in files]})
print(json.dumps({'status':'PASS','run':ROOT.name,'panel_assertions':v['exact_assertions'],'JS_assertions':j['exact_assertions'],'reviews':ids,'full_FEI':'OPEN'}))
