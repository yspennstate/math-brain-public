from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];TEAM=AGENT.parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
SOURCE=TEAM/'agents'/'A050'/'runs'/'20261014T033613Z-fleet05-A050-repair-with-scope'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):(ROOT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def chash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
c=next(x for x in json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8-sig')) if x['claim_id']=='A050-COMMON-CONDITIONAL-KERNEL-REPAIR')
original=dict(c);originalhash=c['statement_sha256']
variants=[chash(c),hashlib.sha256(c['exact_statement'].encode()).hexdigest(),hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()]
assert originalhash in variants
c['statement_sha256']=chash(c)
c['proof_source']={'original_run':str(SOURCE),'source_claims_sha256':sha(SOURCE/'CLAIMS.json'),'source_statement_sha256':originalhash,
 'independent_review_run':ROOT.name,'independent_proof':'PROOF.md section 1','independent_code':'code/check.py; code/controller.py; code/targeted.py','original_source_statement_and_hypotheses_unchanged':True}
c['review_records']=c['review_records']+[{'reviewer':'fleet05/A092','verdict':'ACCEPT_AT_STATED_SCOPE','substantive_repair_supplied':False,
 'method':'Independent normalized conditional-kernel and KL-chain reconstruction; same physical full-reference transport and quotient marginals; exact original truth-table/physical-edge checks, matched controller/data examples and explicit nonmatching boundary',
 'scope':'Original A050 theorem unchanged; quotient requires its own certificate; terminal spectator debt retained once; arbitrary nonmatching reference/core payment remains open',
 'source':'PROOF.md; REPORT.md; out/RESULT.json; out/CONTROLLER_RESULT.json; out/FOUR_BIT_CERTIFICATE.json'}]
c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE'
assert c['exact_statement']==original['exact_statement'] and c['hypotheses']==original['hypotheses'] and c['contributors']==original['contributors']
save('CLAIMS.json',[c])
results=[json.loads((ROOT/'out'/n).read_text()) for n in ['RESULT.json','TARGETED_RESULT.json','CONTROLLER_RESULT.json']]
assert all(x['status']=='PASS' and x['runtime_seconds']<120 for x in results)
assert [x['cases'] for x in results]==[262,257,2]
assert [x['primary_assertions'] for x in results]==[13408,13006,123]
assert [x['entropy_helper_assertions'] for x in results]==[72,27,6]
total=sum(x['primary_assertions']+x['entropy_helper_assertions'] for x in results);assert total==26642
pilot=json.loads((ROOT/'out'/'PILOT.json').read_text());assert pilot['status']=='PASS' and pilot['cases']==20 and pilot['runtime_seconds']<60
fixture=json.loads((ROOT/'out'/'FOUR_BIT_CERTIFICATE.json').read_text())
assert fixture['entropy_drift_sign']==-1 and fixture['conditional_reset_sign']==1
assert not fixture['sufficient_retained_likelihood'] and not fixture['spectator_marginal_JS']
assert fixture['joint_conditional_debit']==fixture['entropy_drift']
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B19','packet_id':'A092','gap_id':'G-R-MISMATCH',
 'attempt_id':'A092-stage5-conditional-entropy-KL-signed-account',
 'method':'Independent A050 conditional-kernel review; original Boolean product-reference transport; exact minimal refutation of entropy-only reset credit; signed conditional product-KL reconstruction',
 'mathematical_delta':'A050 common-kernel v1 accepted unchanged. Four-bit H=3,I=3/2 gate has negative spectator entropy drift and positive conditional reset, integer-certified; all n<=3 splits exclude this particular violation. Retained joint product-reference conditional account satisfies C_child-C_root=DeltaL-Gamma_Z and positive net increase<=2 Inf/ln2; source conditional erasure pays fixture children once. Initial source/quotient budgets and arbitrary canonical occupancy transfer remain open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'A050_INDEPENDENT_REVIEW_ACCEPTED; ENTROPY_ONLY_RESET_PAYMENT_REFUTED; JOINT_CONDITIONAL_PRODUCT_REPAIR_CHECKED; FULL_FEI_OPEN',
 'claim_versions_used':['A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1 (independently reconstructed and accepted)','A038-OWNED-RELEASE-RESET-OCCUPANCY-CERTIFICATE@1 (actual exposure provenance, formulas reconstructed)','A039 stage4 occupancy continuation (scope/context only, not assumed universal)','A047 stage5 graph/support boundary (new next dependency, not independently accepted)'],
 'claims_created_or_changed':['A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1 independent A092 acceptance'],
 'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','code/check.py','code/targeted.py','code/controller.py','code/entropy_tools.py','out/FROZEN_SPEC.json','out/TARGETED_SPEC.json','out/CONTROLLER_SPEC.json','out/JOINT_SPEC.json','out/RESULT.json','out/TARGETED_RESULT.json','out/CONTROLLER_RESULT.json','out/FOUR_BIT_CERTIFICATE.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':['A050','A038','A039','A047','A048','A064','A091','A087','B19','B20'],
 'next_action':'Carry the certified conditional erasure/likelihood statistic into the prescribed canonical occupancy reference at this actual query; use A047 support boundary, explicitly retain reference-only rows, initial source/quotient banks and both full terminal debts on one influence account.',
 'stagnant_substantive_attempts':0,'blockers':['Initial conditional source/quotient banks and canonical occupancy likelihood correction are not universally funded; new audit certificate independent review and supervisor/remote adoption remain unverified.'],
 'packet_ids':['A092']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude'/'B19'/'STREAM_NOTES.md']
sources.extend(SOURCE/n for n in ['REPORT.md','PROOF.md','CLAIMS.json'])
for a,run,names in [
 ('A038','20261014T022516Z-fleet05-A038-occupancy-term-audit',['REPORT.md','PROOF.md','CLAIMS.json']),
 ('A039','20261014T025407Z-fleet05-A039-projection-under-restrictions',['REPORT.md']),
 ('A083','20261014T023633Z-fleet05-A083-formal-core',['REPORT.md','PROOF.md']),
 ('A047','20261014T044331Z-fleet05-A047-boundary-search',['REPORT.md'])]:
 sources.extend(TEAM/'agents'/a/'runs'/run/n for n in names)
sources.append(AGENT/'runs'/'20261014T020903Z-fleet05-A092-counterexample-referee'/'code'/'entropy_tools.py')
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A092 stage 5 complete: A050 common-kernel scoped theorem independently accepted; minimal four-bit entropy-only conditional-reset payment refuted; signed product-KL net increase<=2 Inf/ln2; 521 cases/26,642 exact assertions PASS; FEI OPEN.\nNEXT: Carry exact conditional erasure/likelihood into canonical occupancy reference, using A047 support boundary and one source/quotient budget with both terminal debts; A048/A087 review certificate.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} | {ROOT.name}: Read board/lead/status/protocol and new A038/A039/A083/A050 sources; consumed late A047 support handoff. Independently accepted A050 common-kernel v1 unchanged. Three-bit one/two-spectator censuses found no entropy<=0/reset>0 case; planned actual four-bit opposite-priority gate has DeltaL<0,rho_cond>0, verified via direct character sums and integer powers. H=3,I=3/2, terminal H=4-9/8 log2(3), terminal I=1. Initial standalone-reset obstruction then repaired jointly: C_child-C_root=DeltaL-Gamma_Z, positive net debit<=2Inf/ln2, exact conditional erasure pays actual child conditional debts once. Added frozen identity checks on unchanged domains; final 521 cases/{total} assertions PASS, no failed checker. Original source/quotient bank and arbitrary occupancy correction remain unpaid. All required local files saved, no remote adoption claimed.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage5: A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1 accepted unchanged: hereditary shared conditional spectral kernel with matched references transports quotient prices exactly and retains spectator entropy once; first-data positive entropy drift<=2Inf/ln2 and sufficient retained-frequency likelihood matching hold. Conditional entropy drift alone is NOT signed conditional reset credit. Effective four-bit F(x,a,b,y)=(-1)^a if x=0, else v(y) if b=1, else1, v=2y-1, querying a: DeltaL=-1/2+9/8log2(3)-5/8log2(5)<0, rho_cond=-2+9/8log2(3)+1/8log2(5)>0. Integer certificates 3^9<2^4*5^5 and 3^9*5>2^16. H=3,I=3/2; n<=3 all splits exclude this fixed product-reference violation. Repair uses joint signed conditional product-KL: C= sum_Z h2(Inf)-H(S_Z|T), E C_child-C_root=DeltaL-Gamma_Z, positive net increase<=2Inf/ln2. At the fixture branch release alone misses reset by5/8log2(27/25); original conditional erasure restores balance, leaving -DeltaL>0 after both fresh child conditional debts. Initial C_root and quotient/core/occupancy bills are not newly supplied influence credit.\n')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
assert set(c)==set(protocol['required_per_run']['claim_fields']) and c['statement_sha256']==chash(c)
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for x in protocol['required_per_run']['report_fields']:assert '# '+x in report
assert report.strip().splitlines()[-1].startswith('Universal bridge:')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
for p in ROOT.rglob('*'):
 if p.is_file():assert p.stat().st_size<20_000_000
save('out/VALIDATION.json',{'status':'PASS','at_utc':now,'claim_fields_exact':True,'source_statement_hypotheses_contributors_unchanged':True,'progress_fields_exact':True,'canonical_claim_hash':True,'progress_copies_identical':True,'required_report_fields':True,'all_files_under_20MB':True,'final_cases':521,'final_assertions':total,'new_broad_claims_queued':0,'mirror_status':'UNVERIFIED'})
save('out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json'])
print(json.dumps({'status':'PASS','independent_review':'A050 common-kernel v1 unchanged','cases':521,'assertions':total,'run':str(ROOT)}))
