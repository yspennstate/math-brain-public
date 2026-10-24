from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
r=Path(__file__).resolve().parents[1]; agent=r.parents[1]
root=Path(r'~\brain_workers\FEI100_20261011')
protofile=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def dump(p,z):p.write_text(json.dumps(z,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
proto=json.loads(protofile.read_text(encoding='utf-8'))
checks=json.loads((r/'out/checks.json').read_text(encoding='utf-8'))
assert (checks['selector_cases'],checks['priority_cases'],checks['A057_review_trees'])==(4096,4096,1088)
assert checks['exact_assertions']=='ALL PASS' and checks['runtime_seconds']<180
source57=root/'agents/A057/runs/20261012T003930Z-account05-A057-coherent-restriction-remainder'
sources=[protofile,root/'BOARD.md',root/'claude/B12/STREAM_NOTES.md',
 source57/'REPORT.md',source57/'PROOF.md',source57/'CLAIMS.json',
 root/'agents/A028/runs/20261012T011208Z-account05-A028-stopping-tree-payment/REPORT.md',
 root/'agents/A023/runs/20261012T010933Z-account05-A023-amortized-rarity-budget/REPORT.md',
 root/'agents/A059/runs/20261011T224320Z-account05-A059-decomposition-depth/REPORT.md',
 agent/'runs/20261011T233147Z-account05-A056-balanced-composition/REPORT.md']
manifest=[]
for p in sources:
 b=p.read_bytes(); manifest.append({'path':str(p),'bytes':len(b),'sha256':sha(b)})
dump(r/'out/source_manifest.json',manifest)
consumers=['A057','A058','A059','A060','A028','A095','A094','A091','A090','B20']
statement='For every Boolean indicator c on a uniform physical controller block and Boolean signs u,v on mutually disjoint uniform data blocks disjoint from c, put a=1-2c,p=E c,Va=Var(a),m=E u,n=E v,d=(1-mn)/2 and C0=2+2/ln2+1/(sqrt(e)ln2)<6. The full cost of any controller-only physical tree determining c is Pi_H=H(cu+(1-c)v)-pH(u)-(1-p)H(v)<=d Hplus(a)+C0 d Va, where Hplus is raw nonempty squared-spectrum entropy in bits. Its queried influence is d I(a); terminal influence p I(u)+(1-p)I(v). Hence strong controller certificate Hplus(a)<=T[I(a)-Va] gives Pi_H<=max(T,C0)d I(a). For priority events E1={s=+,A=1},E2={s=+,B=1} sharing one fair bit s, with disjoint private controls and disjoint cores u,v, reveal s,A then B only if A=0. The shared influence is Qs=p delta_u+(1-p)q delta_v, private accounts QA=(1/2)(delta_u+q delta_v-2delta_u q delta_v)I(1-2A), QB=(1/2)(1-p)delta_v I(1-2B), terminal entropy (p/2)H(u)+((1-p)q/2)H(v). Shared Qs is spent once; strong private-controller certificates give complete path price max(C0,TA,TB)(Qs+QA+QB), with both arbitrary terminal entropies retained. No shared nonempty-data collision or arbitrary-terminal FEI bound is asserted.'
claim={'claim_id':'A056-TWO-BRANCH-COMMON-CONTROL-TRANSPORT','version':1,'exact_statement':statement,
 'hypotheses':['Finite independent uniform physical signs','Controller independent of data','Two data branch blocks mutually disjoint','Priority private controls and both core blocks mutually disjoint, shared bit independent','Boolean sign values for branches and controller sign','Entropy in bits; raw nonempty Hplus; actual controller-only physical stopping trees'],
 'statement_sha256':sha(statement.encode()),'contributors':['account05/A056'],
 'proof_source':{'path':str(r/'PROOF.md'),'locators':'(S), (E)-(I), (C)-(B), (O)-(T)'},
 'proof_dependencies':[],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
cap=next(z for z in json.loads((source57/'CLAIMS.json').read_text(encoding='utf-8')) if z['claim_id']=='A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK')
source_declared_digest=cap['statement_sha256']
actual_digest=sha(cap['exact_statement'].encode())
dump(r/'out/source_digest_note.json',{'source':str(source57/'CLAIMS.json'),'claim_id':cap['claim_id'],'version':1,'declared_statement_sha256':source_declared_digest,'actual_utf8_statement_sha256':actual_digest,'match':source_declared_digest==actual_digest,'action':'Preserve author source unchanged; local transcription uses recomputed UTF8 digest and records original digest in review provenance; source file bytes pinned separately'})
cap['statement_sha256']=actual_digest
cap['review_records'].append({'reviewer':'A056','verdict':'HOLDS_SOURCE_PRICE_RECONSTRUCTION; INDEPENDENT_FULL_CHAIN_ACCEPTANCE_DEFERRED','source':str(r/'REVIEW_A057.md'),'method':'Separate integer FWHT/actual physical-tree check plus analytic pricing reconstruction','independence_limitation':'A056 authored upstream biased-interface premise; do not count as independent full-chain acceptance','source_declared_statement_sha256':source_declared_digest,'source_actual_utf8_statement_sha256':actual_digest,'digest_correction_scope':'Local transcription only; author file unchanged','next_reviewer':['A091','A090']})
cap['status']='PRICE_VERIFIED_LOCALLY_FULL_CHAIN_INDEPENDENT_REVIEW_PENDING'
dump(r/'CLAIMS.json',[claim,cap])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':r.name,'stream':'B12','packet_id':'A056',
 'gap_id':'FEI-B12-COMMON-CONTROL-TERMINAL-TRANSPORT','attempt_id':'A056-stage3-two-core-ownership-1',
 'method':'Complete two-branch Fourier path reconstruction; semiconvex mean correction; common-bit priority physical account; verification of productive A057 cap before focused extension',
 'mathematical_delta':'Two disjoint biased branches preserve one-core scalar C0<6; pays distinct-core/shared-bit priority full control path with one shared debit and both terminal entropies retained. Nonempty shared-data collision and universal terminal cost remain open.',
 'deliverable_status':'COMPLETE_LOCAL; supervisor mirror pending','mathematical_status':'SCOPED_C019_PATH_PAYMENT_PROVED_LOCAL_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A056-DISJOINT-COMPOSITION','version':2,'role':'consumed prior interface and A057 source acceptance, not used as unpaid universal premise'},{'claim_id':cap['claim_id'],'version':1,'role':'source-price verification only; upstream authorship link prevents independent full-chain acceptance; not premise of new theorem'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1},{'claim_id':cap['claim_id'],'version':1,'local_change':'source-bound verification record; author source unchanged'}],
 'source_artifacts':['REPORT.md','PROOF.md','REVIEW_A057.md','out/FROZEN_SPEC.json','code/check.py','out/pilot.json','out/checks.json','out/source_manifest.json'],
 'next_consumers':consumers,'next_action':'Remove only u/v data disjointness in paid selector, derive nonempty paired collision correction and test controller plus one terminal reserve on cancellation/bent splice; A091/A090 review new proof and cap full chain.',
 'stagnant_substantive_attempts':0,'blockers':['Nonempty shared-data collision and arbitrary core terminal H/I remain unproved','New interface pending review; A057 cap full-chain acceptance deferred to reviewer without upstream authorship link'],
 'packet_ids':['A056']}
dump(r/'PROGRESS.json',progress);dump(r/'PACKET_DELTA.json',progress)
for z in [claim,cap]:assert set(z)==set(proto['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' ')[0] for x in proto['required_per_run']['progress_fields']}
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
report=(r/'REPORT.md').read_text(encoding='utf-8')
assert len(report.split('## Universal bridge')[1].strip().split('\n\n'))==1
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
dump(r/'out/schema_validation.json',{'claim_fields':'PASS','progress_fields':'PASS','delta_byte_equality':'PASS','claim_statement_digests':'PASS','final_universal_bridge_paragraph':'PASS','exact_cases':9280,'review_independence_flag':'UPSTREAM AUTHOR: INDEPENDENT FULL-CHAIN ACCEPTANCE DEFERRED'})
(agent/'STATUS.md').write_text('STATE: Stage3 paid distinct-core/shared-bit controller path with C0<6; 9280 exact cases PASS; new theorem review pending; C019/full FEI OPEN.\nNEXT: Price nonempty shared-data paired collision with one controller/terminal reserve; A091/A090 review new selector proof and A057 cap full chain.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} — Stage 3 consumed A057 cap and A028 scalar reserve; reconstructed cap price (upstream authorship disclosed, independent full-chain acceptance deferred). Proved two-disjoint-branch full path transport with same C0<6 and one-bit common priority reserve with both terminal costs. 4096 selector +4096 priority +1088 cap trees passed exactly in {checks["runtime_seconds"]:.6f}s. Saved new proof/claim and review-limited reconstruction; universal shared-data/terminal gap remains.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
## Stage 3: two-core common control reserve

For F=c u+(1-c)v with controller and two data blocks disjoint, m=Eu,n=Ev,d=(1-mn)/2, sign controller a=1-2c, p=Ec, full physical path H(F)-pH(u)-(1-p)H(v)<=d Hplus(a)+C0 d Var(a), C0=2+2/ln2+1/(sqrt(e)ln2)<6. Both terminal entropies remain. The crucial mean correction keeps eta((pm+(1-p)n)^2)-p eta(m^2)-(1-p)eta(n^2). With z=(m-n)^2/4<=d^2 and Vu+Vv=4(d-z), scalar price is the SAME C0 as one-core activation. Strong controller certificates price at max(T,C0), without paying arbitrary cores by assumption.

Priority events {s=+,A} and {s=+,B}, distinct disjoint cores, share one actual bit. Reveal s,A then B only on A false. Qs=p delta_u+(1-p)q delta_v occurs once; QA=dA I(sign A)/2, dA=delta_u+q delta_v-2delta_u q delta_v; QB=(1-p)delta_v I(sign B)/2. Terminal H/I weights p/2 and (1-p)q/2. Root influence is exact sum of common/private/terminal accounts. Mean-only collision and shared-control ownership are paid; nonempty shared-data collision and arbitrary core FEI are not.

Separate FWHT/Fraction/prime-log helper checked 4096 selector cases, 4096 seven-bit priority roots and 1088 core-first cap trees. A057's cap pricing reconstruction holds at source scope, but A056 authored its upstream biased-interface premise: do NOT count this as independent full-chain acceptance. A091/A090 must supply that audit. No source repair or author-file change occurred.
''')
receipts=[]
for p in sorted(r.rglob('*')):
 if p.is_file() and p.name!='receipts.json' and '__pycache__' not in p.parts:
  b=p.read_bytes();assert len(b)<20_000_000
  receipts.append({'path':str(p.relative_to(r)),'bytes':len(b),'sha256':sha(b)})
dump(r/'out/receipts.json',{'saved_at_utc':stamp,'local_only':True,'files':receipts})
for z in receipts:assert sha((r/z['path']).read_bytes())==z['sha256']
print(json.dumps({'saved':'PASS','exact_cases':9280,'local_receipted_files':len(receipts),'protocol_schema':'PASS','full_FEI':'OPEN','independent_reviews':'new theorem and cap full chain pending'},indent=2))
