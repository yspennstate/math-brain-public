from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];TEAM=AGENT.parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):(ROOT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def chash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude'/'B19'/'STREAM_NOTES.md']
claims=[]
targets=[('A083','20261013T234228Z-account05-A083-formal-core','A083-COHERENT-ROW-CORE-AND-RESET-OBSTRUCTION',
          ['REPORT.md','CLAIMS.json','code/CoherentTransport.lean','out/LEAN_CHECK.txt']),
         ('A050','20261014T004109Z-account05-A050-repair-with-scope','A050-ACTIVE-LABEL-SCHEDULE-REPAIR',
          ['REPORT.md','PROOF.md','CLAIMS.json','code/targeted.py'])]
for agent,run,cid,files in targets:
    p=TEAM/'agents'/agent/'runs'/run
    c=next(c for c in json.loads((p/'CLAIMS.json').read_text(encoding='utf-8-sig')) if c['claim_id']==cid)
    originalhash=c['statement_sha256']
    allowed=[chash(c),hashlib.sha256(c['exact_statement'].encode()).hexdigest(),hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()]
    assert originalhash in allowed
    c['statement_sha256']=chash(c)
    c['proof_source']={'original_run':str(p),'original_claims_sha256':sha(p/'CLAIMS.json'),'source_statement_sha256':originalhash,
                       'source_hash_convention':'preserved source digest; export uses compact JSON statement+hypotheses',
                       'independent_review_run':ROOT.name,'independent_proof':'PROOF.md','independent_certificate':'code/check.py; out/RESULT.json'}
    c['review_records'].append({'reviewer':'account05/A092','verdict':'ACCEPT_AT_STATED_SCOPE','substantive_repair_supplied':False,
                               'scope':'Original statement unchanged; no universal bank supply or FEI asserted; Lean not rerun',
                               'method':'Independent algebra, tensor/entropy and normalized-reference reconstruction; integer Walsh truth-table spectra and physical edge influence; exact coherent joints and retained terminal bills',
                               'source':'PROOF.md; REPORT.md; out/RESULT.json'})
    c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE'
    claims.append(c);sources.extend(p/f for f in files)
sources.append(TEAM/'agents'/'A039'/'runs'/'20261013T235428Z-account05-A039-projection-under-restrictions'/'CLAIMS.json')
sources.append(AGENT/'runs'/'20261013T222550Z-account05-A092-counterexample-referee'/'code'/'audit.py')
save('CLAIMS.json',claims)
result=json.loads((ROOT/'out'/'RESULT.json').read_text());pilot=json.loads((ROOT/'out'/'PILOT.json').read_text())
assert result['status']=='PASS' and result['cases']==11 and result['assertions']==15793 and result['entropy_helper_assertions']==86
assert pilot['status']=='PASS' and pilot['cases']==3 and pilot['runtime_seconds']<60
assert result['runtime_seconds']<120
fixture=json.loads((ROOT/'out'/'PRIORITY_m6.json').read_text());assert fixture['rigorous_violation']=='H(Pi|W)>16 R'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B19','packet_id':'A092','gap_id':'G-R-MISMATCH',
 'attempt_id':'A092-stage4-prescribed-witness-bank-audit',
 'method':'Independent source claim reviews; exact original truth-table coherent lifts; one normalized physical transcript reference; all-m signed-bank obstruction',
 'mathematical_delta':'A083@1 and A050@1 accepted unchanged. Shared controller-complete priority tree has zero injection, exact H(Pi|W)=2-H(W), R=2^-m(5m/8+3/4), terminal H=2^(-m-1). Separate conditional-bank influence funding fails all finite constants; m6 rigorously exceeds 16R. Own family H<4I, full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'TWO_INDEPENDENT_REVIEWS_ACCEPTED; PRESCRIBED_BANK_ROUTE_REFUTED; JOINT_SIGNED_PAYMENT_AND_FULL_FEI_OPEN',
 'claim_versions_used':['A083-COHERENT-ROW-CORE-AND-RESET-OBSTRUCTION@1 (independently reconstructed)','A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1 (independently reconstructed)','A092-UNIFORM-SIGNED-TRANSCRIPT-BANK-CONVERSION@1 (prior own scoped interface, independently rederived here)'],
 'claims_created_or_changed':['A083-COHERENT-ROW-CORE-AND-RESET-OBSTRUCTION@1 independent A092 review','A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1 independent A092 review'],
 'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','code/check.py','code/entropy_tools.py','code/finalize.py','out/FROZEN_SPEC.json','out/PILOT.json','out/RESULT.json','out/PRIORITY_m6.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':['A083','A050','A048','A039','A038','A091','A087','B19','B20'],
 'next_action':'Change from separate-bank payment to one signed Bayes/occupancy reference after nonconstant shared-core data exposure, matching A038 owned reserve and A039 adaptive descendant order while retaining terminal core bills.',
 'stagnant_substantive_attempts':0,'blockers':['Universal joint signed residual/core payment open; audit family obstruction not independently reviewed; supervisor adoption and remote mirrors unverified.'],
 'packet_ids':['A092']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A092 stage 4 complete: A083/A050 scoped claims independently accepted; prescribed zero-injection shared-control bank has unbounded bank/I ratio despite H<4I; 15,879 exact main assertions PASS; FEI OPEN.\nNEXT: Preserve signed cancellation in one Bayes/occupancy reference after shared-core data exposure, matching A038 owned reserve and A039 descendant query order; A087/A039 review audit certificate.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | {ROOT.name}: Read board, B19 notes, own status and full protocol. Independently accepted A083 retained-root reset obstruction and A050 active-label repair unchanged. Fresh integer Walsh/joint checker passed 11 frozen cases, {result["assertions"]}+{result["entropy_helper_assertions"]} assertions in {result["runtime_seconds"]:.6f}s. Named actual W and one physical-transcript reference on shared-control priority F_m: B=2-H(W), R=2^-m(5m/8+3/4), terminal H=2^(-m-1), injection zero. Exact m6 certificate B>16R; all-m B/I unbounded but H<4I. This refutes separate bank funding, preserves signed cancellation and changes next mechanism. All local files saved; no remote persistence claimed.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage4: A083@1 accepted: retained root-to-terminal bank loses r bits on disjoint AND signs, H=2r,I=r; local Lean scope is rational row transport only. A050@1 accepted: e=H(S intersect Q|S)<=I_A h2(R/I_A), with exact normalized deletion reference and KL rebate; terminal independence of A implies e=0. Zero injection does not fund history. On F_m selected by shared AND_m plus two private arms, same parity/AND data cores, actual W=fixed data projection; rho(pi|w)=physical transcript law is normalized, H(Pi|W)=2-H(1-11t/16,t/16,t/16,9t/16), t=2^-m. R=t(5m/8+3/4), I=t(5m/8+2), terminal H=t/2. Bank/I diverges while H<4I. Half-bank tends1 and signed residual tends1: preserving their cancellation is necessary. Never substitute separate O(I) bank funding for the joint signed ledger.\n')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields']) and c['statement_sha256']==chash(c)
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for x in protocol['required_per_run']['report_fields']:assert '# '+x in report
assert report.strip().splitlines()[-1].startswith('Universal bridge:')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
for p in ROOT.rglob('*'):
    if p.is_file():assert p.stat().st_size<20_000_000
save('out/VALIDATION.json',{'status':'PASS','at_utc':now,'claim_fields_exact':True,'progress_fields_exact':True,'claim_hashes_canonical':True,'progress_copies_identical':True,'required_report_fields':True,'all_files_under_20MB':True,'source_reviews':'ACCEPT_UNCHANGED_AT_SCOPE','new_broad_claims_queued':0,'result':result,'mirror_status':'UNVERIFIED'})
save('out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json'])
print(json.dumps({'status':'PASS','independent_reviews':2,'cases':11,'assertions':result['assertions']+result['entropy_helper_assertions'],'run':str(ROOT)}))
