"""Bounded closing verification and persistence. Writes only inside A043."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,time,datetime
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];BASE=AGENT.parents[1];O=RUN/'out';O.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
source=BASE/'agents/A041/runs/20261023T135351Z-account03-A041-weighted-threshold-fei/PROOF.md'
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
P=json.loads(protocol.read_text(encoding='utf-8-sig'));F=P['required_per_run'];CF=F['claim_fields'];PF=[x.split(' (')[0] for x in F['progress_fields']];HF=F['report_fields']
spec={'helper':'A043-closing-joint-source-review-v1','family':'actual equal-bias Boolean AND2 gates realizing scalar dyadic cells','domain':'j=0,...,12; u=k/64, k=33,...,64; p=2^-j u, omit p=1 deterministic endpoint; additional sharpness p=1/2,3/4,15/16,255/256',
 'case_count':415,'sharpness_controls':4,'symmetry':'none','arithmetic':'exact Fraction physical masses and24-term outward rational atanh logarithms; no floating-point sign','memory_estimate_mb':25,'max_runtime_seconds':55,'automatic_dimension_escalation':False,
 'scope':'Post-deadline deterministic verification of an existing theorem, not a new family search or claimed campaign solution.'}
save(O/'frozen_spec.json',spec);start=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1
 if not b:raise AssertionError(checks)
def basiclog(x):
 z=(x-1)/(x+1);ck(0<=z<=Q(1,3))
 lo=sum((Q(2,2*k+1)*z**(2*k+1) for k in range(24)),Q(0))
 return lo,lo+2*z**49/(49*(1-z*z))
L2=basiclog(Q(2))
def ln(x):
 ck(x>=1)
 k=0
 while x>=2:x/=2;k+=1
 lo,hi=basiclog(x);return lo+k*L2[0],hi+k*L2[1]
cases=0
for j in range(13):
 ck(j+1<=2**j)
 for k in range(33,65):
  u=Q(k,64);p=u/2**j
  if p==1:continue
  v=4*p*(1-p);single=v*p*p;pair=v*v/4;mean=2*p*p-1
  ck(mean*mean+2*single+pair==1)
  ck(2*pair==2*v*(p-p*p))
  lo,hi=ln(1/u)
  ck(2*single*j+2*single*hi<=2*pair)
  ck(p*(j+hi)<=1-p)
  cases+=1;ck(time.perf_counter()-start<55)
ck(cases==415)
sharp=[]
for p in (Q(1,2),Q(3,4),Q(15,16),Q(255,256)):
 lo,hi=ln(1/p)
 if p==Q(1,2):ck(2*(4*p*(1-p)*p*p)==2*(4*p*p*(1-p)*(1-p)))
 else:ck(2*p*hi/(1-p)<=2)
 if p==Q(255,256):ck(2*p*lo/(1-p)>Q(199,100))
 sharp.append({'p':str(p),'L1_over_source_if_j0_interval':[str(2*p*lo/(1-p)),str(2*p*hi/(1-p))]})
# Excluded actual real half-literal: t=1/2,d=1/4,j=1 violates the Boolean source step.
ck(Q(1,2)**2>Q(1,4)-Q(1,2)**2)
runtime=time.perf_counter()-start;ck(runtime<55)
save(O/'checks.json',{'status':'PASS','actual_AND2_cases':cases,'sharpness_controls':sharp,'assertions':checks,'runtime_seconds':runtime,'helper_sha256':sha(Path(__file__)),'scope':'Exact finite audit of analytic universal review; not a formal proof or full FEI claim.'})
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
save(O/'source_receipts.json',{'completed_utc':stamp,'campaign_deadline_utc':'2026-10-23T14:49:00Z','post_deadline_review_completion':True,'sources':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in [source,protocol,BASE/'BOARD.md',BASE/'claude/B09/STREAM_NOTES.md',AGENT/'STATUS.md',RUN/'PROOF.md']],
 'reading_scope':'Current BOARD/B09/STATUS and A041 complete proof read in this stage; original campaign protocol/papers/decomposition baseline carried from documented previous stages. No claim of pre-deadline review completion.'})
cid='A043-REVIEW-A041-JOINT-SINGLETON-SOURCE'
statement='Independent reconstruction without repair of A041 20261023T135351Z PROOF sections2-3: for every finite Boolean sign at every interior independent product law, J1+alpha L1<=max(ln4,2alpha)(2Delta-R) for every alpha>=0, with the constant optimal on actual equal-bias AND2 regimes p=1/2 and p->1. The exact weighted all-depth carry/refund identity retains T_tot,J1(F),alpha[L1(F)+V_tot],B_alpha,tree and equals max(ln4,2alpha)(2Delta_F-R_tree)+(1-alpha)ln4 C1,tot. Scope excludes arbitrary spectra, overlapping wires and any universal payment of prime J_hi. This is an independent scoped review of an existing result, not a new FEI theorem.'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Boolean signs; interior independent laws; deterministic coordinates and constant children contracted','Natural entropy units; dyadic upper-mantissa convention; zero occupied coefficients omitted','Genuine disjoint composition at actual induced biases; both full singleton/mantissa terminal laws retained; alpha>=0'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A041 (source theorem)'],'proof_source':['PROOF.md','code/audit_and_save.py','out/checks.json'],
 'proof_dependencies':[{'source':str(source),'sha256':sha(source),'scope':'Sections2-3 reviewed independently, no substantive repair'}],
 'review_records':[{'reviewer':'A043','verdict':'HOLDS_SCOPED','scope':'A041 Sections2-3 sharp joint source and exact carry tradeoff','method':'Independent u-variable derivative proof, actual Boolean sharpness reconstruction, exact finite rational AND2 audit; no contribution or repair to source theorem','completed_utc':stamp}],
 'status':'INDEPENDENT_RECONSTRUCTION_HOLDS_SCOPED','supersedes':[],'refutes':[],
 'first_unproved_line':'Universal arbitrary-prime J_hi<=KDelta with SAME unused original source after singleton/import/carry debits remains unproved. This scoped acceptance does not accept every upstream source or full FEI.',
 'next_consumers':['A041','A042','A044','A045','A091','B09 lead']}
assert set(claim)==set(CF);save(RUN/'CLAIMS.json',[claim])
progress={'protocol_revision':P['revision'],'run_id':RUN.name,'stream':'B09','packet_id':'A043','gap_id':'B09-ORIGINAL-SOURCE-HIGH-DEGREE-SCALE-PAYMENT','attempt_id':'closing-independent-joint-source-review',
 'method':'Consume and independently reconstruct the new A041 sharp source rather than duplicate work; deterministic exact audit and source-bound campaign handoff.',
 'mathematical_delta':'A041 joint singleton scale/mantissa envelope and all-depth carry tradeoff independently HOLDS at stated scope, without repair. Two actual AND2 regimes establish both optimal constant branches. No new universal prime payment.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'EXISTING_SOURCE_INDEPENDENTLY_RECONSTRUCTED_SCOPED; CAMPAIGN_FULL_FEI_OPEN',
 'claim_versions_used':['A041 20261023T135351Z PROOF sections2-3, SHA256 pinned in source receipts'],
 'claims_created_or_changed':[cid+'@1'],'source_artifacts':['PROOF.md','REPORT.md','CLAIMS.json','code/audit_and_save.py','out/frozen_spec.json','out/checks.json','out/source_receipts.json'],
 'next_consumers':['A041','A042','A044','A045','A091','B09 lead'],
 'next_action':'Supervisor consume scoped review and final handoff. Any authorized continuation must pay actual arbitrary-prime J_hi from SAME unused original source after all singleton/mantissa/import/carry commitments and both full terminal KL laws; do not create schedules or claim campaign closure.',
 'stagnant_substantive_attempts':0,'blockers':['Full FEI and arbitrary-prime high-degree scale payment remain open at campaign close','Review completed after14:49 UTC; no pre-deadline acceptance or new heavy search claimed','Brain self-care degraded: personal model101.3h, state-of-mind85.9h, latest dream36.6h stale; no repair claimed'],'packet_ids':['A043']}
assert set(progress)==set(PF);save(RUN/'PROGRESS.json',progress);(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
txt=[
 'Close the final authorized stage by independently reviewing an existing universal singleton-source dependency and stating the exact remaining all-prime obligation. Every finite Boolean sign, all interior product laws, all alpha>=0; natural units. The fixed campaign deadline was14:49 UTC; slow source/wake reads completed later and this review completion is explicitly post-deadline.',
 'Updated BOARD/B09 STREAM_NOTES v2/STATUS read first. A041 20261023T135351Z PROOF read in full; only sections2-3 independently accepted here. The source was already reported by A041/A042, so it is not presented as new A043 research. Prior protocol revision '+P['revision']+' and campaign/paper baseline carried from earlier documented reads. Source hashes and actual completion time in out/source_receipts.json.',
 'PROOF.md reconstructs the critical budget J1/ln4+L1/2<=2Delta-R through monotonicity of u(j+1-ln u), independent of the source x=1/t argument. Actual AND2 p=1/2 forces ln4; p->1 forces2alpha. Linear combination of the two complete singleton equations proves the exact all-depth tradeoff, with no discarded C1, final L1 or imported V. First unsupported line: uniform arbitrary-prime J_hi payment from SAME unused original source. Full FEI remains OPEN, and no Boolean divergent H/I family is supplied.',
 'Executed python -X utf8 '+str(RUN/'code/audit_and_save.py')+'. Before the deterministic audit saved frozen specification:415 actual equal-bias AND2 laws on prescribed dyadic cells,4 sharpness controls, Fraction physical masses and24-term outward rational atanh logs,25MB estimate,55-second cap, no dimension change. PASS '+str(checks)+' assertions in '+str(runtime)+' seconds. p=255/256 rigorously has L1/source>1.99 while <=2. Excluded real half-literal fails Boolean source admission. This is bounded post-deadline verification, not a new search. No job >300MB, no floating-point sign and no Lean formalization claimed.',
 'A041 sections2-3 accepted only at stated mathematical scope and without repair; no independent acceptance of the entire upstream chain or every claim in its run. Existing A043 prime localization, paid-sector reference and import-depth obstruction remain unchanged. The sharp source commits ln2 of its own mantissa at alpha=ln2; it does not make that fraction free for a second high-carry account.',
 progress['next_action']+' No new schedule, peer message, shared index, brain record or other agent folder was modified. Final campaign outcome for A043: decomposition/localization and several components closed; full target remains open.',
 'Four exact-schema protocol files plus PROOF.md, code and outputs persisted only in A043. STATUS has two lines; WORKLOG and LEARNED appended. out/schema_validation.json and out/persistence_receipts.json provide actual local field/hash receipts. No git/mirror/publication receipt, mail, brain write, trading access, detached job or remaining stage job. No pre-deadline completion timestamp fabricated.'
]
report='# A043 final scoped review and campaign handoff\n\n'+'\n\n'.join('## '+h+'\n\n'+t for h,t in zip(HF,txt))
report+='\n\n**Universal bridge**: B09\'s precisely quantified all-product-bias prime endpoint advances by an independent acceptance of the sharp joint singleton/mantissa supplier and its one all-depth carry/refund owner, not by a new entropy constant. The exact missing universal bridge remains payment of arbitrary-prime J_hi from the SAME unused original capacity after every committed debit and both full terminals. Full FEI is OPEN at campaign close. The shortest authorized continuation is this actual high-degree supplier estimate; another normalizer bound or isolated class census would not supply it. The closing review/handoff was completed after the deadline, honestly timestamped, without starting a new search.\n'
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: Final14:46 stage saved: A041 sharp joint singleton source/carry tradeoff independently HOLDS_scoped;415 AND2 certificates PASS;review completed afterdeadline;campaign FEI OPEN.\nNEXT: Supervisor consume closing review; any authorized continuation must pay arbitrary-prime J_hi from SAME unused original bank after all singleton/mantissa/import/carry debits and BOTH full terminal laws.\n',encoding='utf-8')
for name,text in [('WORKLOG.md','2026-10-23 14:46 UTC trigger; completion '+stamp+': source/wake delay crossed14:49 deadline. Read updated board and independently reconstructed A041 sharp joint singleton source and all-depth carry tradeoff without repair. Bounded deterministic415 AND2 audit/'+str(checks)+' assertions PASS in '+str(runtime)+'s. No new search or full FEI closure; saved final scoped review and exact universal gap. Brain self-care remains degraded.'),('LEARNED.md','2026-10-23 closing review: A041 joint source J1+alpha L1<=max(ln4,2alpha)(2Delta-R) HOLDS_scoped. Critical proof: u(j+1-ln u)<=j+1<=2^j; then J1/ln4+L1/2<=2Delta-R. Fair AND2 and equal-bias AND2 p->1 force both sharp branches. Exact all-depth tradeoff retains final L1, imported V and carryC1; alpha alternatives share ONE bank. This independent review does not pay arbitrary-prime J_hi or settle FEI. Final stage completed after campaigndeadline, explicitly recorded.')]:
 with (AGENT/name).open('ab') as f:f.write(('\n'+text+'\n').encode('utf-8'))
valid={'status':'PASS','claim_fields_exact':set(claim)==set(CF),'progress_fields_exact':set(progress)==set(PF),'packet_copy_exact':(RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes(),'report_sections':all('## '+h in report for h in HF),'status_two_lines':len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2}
assert all(v for k,v in valid.items() if k!='status');save(O/'schema_validation.json',valid)
files=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='persistence_receipts.json':
  ck(p.stat().st_size<20_000_000);files.append({'path':p.relative_to(RUN).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size})
save(O/'persistence_receipts.json',{'completed_utc':stamp,'files':files,'scope':'Local save only; no external-copy verification'})
assert all(sha(RUN/f['path'])==f['sha256'] for f in files)
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert (RUN/'REPORT.md').read_text(encoding='utf-8').rstrip().splitlines()[-1].startswith('**Universal bridge**')
print(json.dumps({'status':'PASS','completed_utc':stamp,'mathematical_assertions':json.loads((O/'checks.json').read_text(encoding='utf-8'))['assertions'],'actual_AND2_cases':cases,'hash_bound_files':len(files),'campaign_full_fei':'OPEN','review':'A041 sections2-3 HOLDS_SCOPED','stage_jobs_running':0}))
