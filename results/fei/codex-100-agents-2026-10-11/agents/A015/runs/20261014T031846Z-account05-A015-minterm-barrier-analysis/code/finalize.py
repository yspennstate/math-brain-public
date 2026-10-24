from pathlib import Path
import json,hashlib,datetime
BASE=Path(__file__).resolve().parents[1]; AGENT=BASE.parents[1]; ROOT=AGENT.parents[1]
A7=ROOT/'agents/A007/runs/20261014T014217Z-account05-A007-root-normalization'
OLD7=ROOT/'agents/A007/runs/20261013T220854Z-account05-A007-root-normalization/LIFT.md'
OLD15=AGENT/'runs/20261014T001450Z-account05-A015-minterm-barrier-analysis/code/check.py'
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(BASE/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
proto=json.loads(PROTO.read_text(encoding='utf-8-sig'))
original=next(x for x in json.loads((A7/'CLAIMS.json').read_text(encoding='utf-8')) if x['claim_id']=='A007-DISTRIBUTED-CORE-COMPONENT-LIFT')
claim=json.loads(json.dumps(original))
claim['review_records'].append({'reviewer':'A015','verdict':'HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR','proof_source':str(BASE/'REVIEW_A007.md'),'validation':str(BASE/'out/EXACT_CHECK.json'),'method':'Independent gate-level component attachments and chronological BFS/deletion inverse; reconstruct all mass/rank/normalization and equal-width clauses analytically','reviewer_supplied_substantive_repair':False,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
claim['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING'
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':proto['revision'],'run_id':BASE.name,'stream':'B03','packet_id':'A015','gap_id':'G-J-COST','attempt_id':'A015-stage4-retained-posterior-occupation',
 'method':'Whole unchanged-scope A007 review; exact sharp occupation envelope and original-posterior owned-size law with nonconstant core residual retained',
 'mathematical_delta':'A007 distributed lift v1 independently HOLDS. At maximal overlap Z>=2^(-u H(ownership)/5), coefficient sharp with explicit error; exact full-cell posterior size weights derived and certified. Psi_dist <=pr/10 sum P_g E_eta H, with inherited pR_g retained. Uniform posterior entropy and universal base cost OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS',
 'mathematical_status':'DEPENDENCY_INDEPENDENTLY_ACCEPTED_NARROW_DIAGNOSTIC_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':['A007-DISTRIBUTED-CORE-COMPONENT-LIFT@1','A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS@1'],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'Added local independent unchanged-scope acceptance; no new broad candidate'}],
 'source_artifacts':[str(BASE/'REVIEW_A007.md'),str(BASE/'OCCUPATION_ENVELOPE.md'),str(BASE/'out/EXACT_CHECK.json'),str(BASE/'out/FULLSUPPORT_CHECK.json')],
 'next_consumers':['A007','A008','A086','A094','B03','B20'],
 'next_action':'Prove or refute a uniform ownership-entropy tail under exact W law, retaining finite-N depletion, factorial moments, signed normalizer and complete inherited core residual.',
 'stagnant_substantive_attempts':0,
 'blockers':['Uniform posterior ownership-entropy bound unproved','Universal physical-location/rank base payment and general overlapping-table Psi_dist unproved','Diagnostic independent review and supervisor adoption unobserved'],
 'packet_ids':['A015']}
save('PROGRESS.json',progress);(BASE/'PACKET_DELTA.json').write_bytes((BASE/'PROGRESS.json').read_bytes())
sources=[(ROOT/'BOARD.md','Entire supervisor snapshot via follow-up chunks, 2026-10-14 03:14 UTC'),(ROOT/'claude/B03/STREAM_NOTES.md','Complete v2'),(AGENT/'STATUS.md','Inherited stage-3 status before update'),(PROTO,'Complete v2'),(A7/'REPORT.md','Complete'),(A7/'DISTRIBUTED_LIFT.md','Complete mathematical proof'),(A7/'CLAIMS.json','Complete original statement/version/hash'),(OLD7,'Complete earlier lift proof and paid constants'),(OLD15,'Own immutable source read/compiled without writes; independent chronological moment helper')]
save('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'scope':scope} for p,scope in sources])
full=json.loads((BASE/'out/EXACT_CHECK.json').read_text(encoding='utf-8'))
pilot=json.loads((BASE/'out/PILOT.json').read_text(encoding='utf-8'))
size=json.loads((BASE/'out/FULLSUPPORT_CHECK.json').read_text(encoding='utf-8'))
assert full['status']==pilot['status']==size['status']=='PASS'
assert full['occupation_cases']==648 and pilot['occupation_cases']==60 and size['assignments']==91
assert (full['assertions'],pilot['assertions'],size['assertions'])==(11016,2415,438)
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
assert all(claim[k]==original[k] for k in ['version','exact_statement','hypotheses','statement_sha256'])
report=(BASE/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in proto['required_per_run']['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
(AGENT/'STATUS.md').write_text('STATE: A015 stage 4 complete: A007 distributed lift v1 independently HOLDS; sharp 1/5 occupation envelope and exact retained-posterior size law proved; 13,869 exact checks PASS; FEI OPEN.\nNEXT: A007/A008/A086 review; prove or refute uniform ownership-entropy tail under exact W law, keeping finite-N labels, factorial moments, signed normalizer and inherited core cost.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 stage 4 ('+BASE.name+'): consumed A007 distributed lift and independently accepted whole unchanged v1 without repair. Derived maximal-overlap occupation envelope Z>=2^(-u H(a)/5), sharp equal-size limit with error gamma*u^2/(L ln2). Retained SAME base posterior and pR_g; isolated Psi_dist<=pr/10 sum P_g E_eta H. Derived exact full-cell owned-size law with binom(N,k) N^-k (s)_(k-1) multinomial and congestion; independent BFS verifies91 assignments. Finalpilot2415+full11016+size438=13869 exact assertions PASS; initial weaker pilot2352 preserved/excluded. No broad universal candidate; next is exact-law posterior entropy concentration or falsifier.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nA007-DISTRIBUTED-CORE-COMPONENT-LIFT@1 independently reconstructed by A015 unchanged scope/no repair: delete fresh-coordinate edges and replay old BFS; component root may be above its core owner; multiplicity u_a(u+1)...(u+c-2), c1 separately one. Signed log[D\'/pD] and full inherited residual must stay.\nMaximal selected overlap kappa_l=s: distributed ownership Z_tau(u)>=2^(-(gamma-1)u H(s_l/s)), gamma6/5. Variational product-owner law plus convex xlogx proves it; it does not replace eta_T. Equal owned sizesL give k^(-u/5)<=Z<=k^(-u/5) exp((6/5)u^2/L), exact analytic sharpness on parity prime assignments. Fixed-assignment loss is not a lower bound on optimized whole cost.\nFull-support common-order table, lambda1/N,beta1: original-posterior Psi_dist<=pr/10 sum_T P_g E_eta H(ownership). Exact conditional sizes weights proportional to binom(N,k)N^-k(s)_(k-1) [s!/prod s_l!] prod(s_l/s)^((6/5)s_l). Rising factorial counts chronological forests; finite-N depletion and rank-independent conditional cancellation must be retained. Uniform E_eta H<=C would pay this correction by C/5 I_core, but that bound and universal inherited physical-location/rank cost remain unproved. Full cells need not be prime: extension to legal AND covers is directly justified and does not enlarge A007\'s reviewed prime statement.\n')
files=[p for p in BASE.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[AGENT/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
save('out/RECEIPTS.json',{'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'schema_fields':'PASS','progress_packet_identical':(BASE/'PROGRESS.json').read_bytes()==(BASE/'PACKET_DELTA.json').read_bytes(),'source_statement_preserved':True,'diagnostic_independent_review':'PENDING','mirror':'UNVERIFIED'})
assert all(sha(Path(x['path']))==x['sha256'] for x in json.loads((BASE/'out/RECEIPTS.json').read_text(encoding='utf-8'))['files'])
print(json.dumps({'persistence':'PASS','files':len(files),'assertions':full['assertions']+pilot['assertions']+size['assertions'],'run':str(BASE)}))
