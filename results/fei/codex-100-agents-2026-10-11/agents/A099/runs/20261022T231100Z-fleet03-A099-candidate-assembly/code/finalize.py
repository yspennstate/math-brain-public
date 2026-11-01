from pathlib import Path
import json,hashlib,datetime,re
R=Path(__file__).resolve().parents[1];O=R.parents[1]
B=O/'runs/20261021T155354Z-fleet03-A099-candidate-assembly'
TEAM=O.parents[1]
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
full=rd(R/'out/EXACT_EXIT_RESET.json');pilot=rd(R/'out/PILOT.json')
assert full['status']==pilot['status']=='PASS'
assert full['roots']==18 and pilot['roots']==3 and full['seconds']<55
assert full['positive_spent_nonconstant_exit_resets']>0
from fractions import Fraction as F
w=full['positive_witness'];assert F(w['signed_reset_lower'])>0 and F(w['prior_debit_lower'])>0
save(R/'out/POSITIVE_RESET_CERTIFICATE.json',{'arithmetic':'rational interval, strictly positive lower endpoints','witness':w,
 'scope':'Both physical children nonconstant; booked erasure before reset >0; current off exit unqueried; all other full terminal costs retained in complete check'})
save(R/'out/COMPUTE_ADMISSION.json',{'memok_exit_code':1,'message':'physical free3.0GB<4.0GB; commit23.9GB>8.0GB',
 'large_job_launched':False,'Lean':'NOT_LAUNCHED','PDF':'NOT_BUILT_THIS_STAGE','small_checker_estimate_MB':100,
 'observed_check_seconds':full['seconds'],'memory_peak':'UNMEASURED'})

# Correct a descriptive policy-count typo without changing the frozen family/domain.
spec=rd(R/'out/FROZEN_SPEC.json')
save(R/'out/FROZEN_METADATA_CORRECTION.json',{'old':spec['case_count'],
 'corrected':'18 root/reference pairs; all eligible type words/stopping cuts; TWO fixed exit policies plus every single-exit replacement',
 'reason':'Checker has keep-all and convert-all fixed policies; each single-exit policy is additional. No domain/result changed.'})

claims=rd(R/'CLAIMS.json');old=rd(B/'CLAIMS.json');assert claims[:len(old)]==old
roots={'A096-CANONICAL-ACTIVE-RESET-SAME-ANCESTOR':TEAM/'agents/A096/runs/20261021T210221Z-fleet03-A096-live-gap-ledger',
 'A097-MIXED-ACTIVE-CONTROL-RESET-SAME-ANCESTOR':TEAM/'agents/A097/runs/20261021T232544Z-fleet03-A097-cross-route-transfer',
 'A073-DUMMY-DATA-RESET-SAME-ANCESTOR':TEAM/'agents/A073/runs/20261022T211534Z-fleet03-A073-certified-logarithms'}
hashes=[]
for c in claims[len(old):]:
 if c['claim_id'] in roots:
  original=next(x for x in rd(roots[c['claim_id']]/'CLAIMS.json') if x['claim_id']==c['claim_id'])
  assert all(c[k]==original[k] for k in ['claim_id','version','exact_statement','hypotheses','statement_sha256'])
  c['review_records'][-1].update(verdict='HOLDS_AT_EXACT_ORIGINAL_SCOPE',timestamp=stamp,
   validation=str(R/'out/EXACT_EXIT_RESET.json'),
   guard='A099 independently reconstructs exact full scoped chain; no universal or integrated-chain acceptance')
  c['status']='SCOPED_A099_INDEPENDENT_RECONSTRUCTION_INTEGRATED_AUDITS_OPEN'
 else:
  assert c['claim_id']=='A099-PRESCRIBED-EXIT-SOURCE-RESET'
  c['status']='ANALYTIC_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW'
 text=c['exact_statement'];hyp=c['hypotheses']
 choices=[('raw',text)]
 for k in ['statement','exact_statement']:
  for asc in [True,False]:
   for sep in [None,(',',':')]:choices.append((str((k,asc,sep)),json.dumps({k:text,'hypotheses':hyp},sort_keys=True,ensure_ascii=asc,separators=sep)))
 matches=[name for name,value in choices if hashlib.sha256(value.encode('utf-8')).hexdigest()==c['statement_sha256']]
 assert matches,c['claim_id']
 hashes.append({'claim_id':c['claim_id'],'statement_sha256':c['statement_sha256'],'conventions':matches})
save(R/'CLAIMS.json',claims);save(R/'out/HASH_CONVENTIONS.json',hashes)

dag=rd(R/'out/PROOF_DEPENDENCIES.json');nodes={x['claim_id']:x for x in dag['nodes']}
assert len(nodes)==len(dag['nodes'])
vis=set();stack=set()
def walk(k):
 assert k in nodes,('MISSING_DEPENDENCY',k)
 assert k not in stack,('CYCLE',k)
 if k in vis:return
 stack.add(k)
 for d in nodes[k]['proof_dependencies']:walk(d)
 stack.remove(k);vis.add(k)
for k in nodes:walk(k)

# Rebuild the single source with the final proof bytes, retaining all prior lemmas.
tex=(B/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8').replace('21 October 2026; assembly version 6','23 October 2026; assembly version 7')
annex=(R/'STAGE7_ADDITIONS.tex').read_text(encoding='utf-8')
tex=tex.replace('\\section{Dependencies, review and sources}',annex+'\n\\section{Dependencies, review and sources}')
tex=tex.replace('Prescribed\nfresh-reference resets remain a separate signed account.',
 'Active, dummy and eligible control resets and the specified exit-source\nconversions are paid on the stated point-source family. Universal\nfresh-reference payment remains a separate open account.')
assert tex.count('\\begin{conjecture}')==4 and '\\input{' not in tex and '\\include{' not in tex
assert not re.search(r'Theorem~\\ref\{(?:lem|prop|cor):',tex)
(R/'CANDIDATE_MANUSCRIPT.tex').write_text(tex,encoding='utf-8')

report=(R/'REPORT.md').read_text(encoding='utf-8').replace('# A099 version 7 checkpoint','# A099 candidate assembly version 7')
report=report.replace('Status: validation pending.',f"Pilot: {pilot['exact_assertions']} exact checks over3 roots/81 histories PASS in{pilot['seconds']:.3f}s. Full: {full['exact_assertions']} exact checks over{full['roots']} roots/{full['histories']} histories/{full['local_queries']} query transactions PASS in{full['seconds']:.3f}s. Positive signed resets after a prior debit: {full['positive_spent_nonconstant_exit_resets']} occurrences (repeated across stopping prefixes, not distinct functions). Exact witness is out/POSITIVE_RESET_CERTIFICATE.json.")
report=report.replace('A098 accepts only the local dummy substitution and conditional global algebra; it is not counted as a full upstream review.',
 'A098 accepts only the local dummy substitution and conditional global algebra; it is not counted as a full upstream review. A099 independently reconstructs the complete exact A096/A097/A073 chains in the single-source proof, retaining all original scopes and hashes.')
report=report.replace('Mathematical validation and final artifact receipts pending at this checkpoint.',
 'Validation and schema/hash/DAG checks passed. out/PERSISTENCE_RECEIPTS.json pins actual saved bytes. memok exited1 (physical3.0GB<4GB), so no optional Lean/compiler was launched; no new PDF is claimed. Proof rung: complete analytic derivation plus exact finite certificates; new exit theorem still awaits independent review. Code inspection, not a Lean certificate, checks all-dimensional quantifiers. The v6 exact prime-log helper is reused only on exact equality endpoints; author checkers are not imported. Frozen policy-count metadata said three fixed policies; the receipt corrects it to two fixed policies plus single-exit replacements, without changing domain or observations.')
report=report.replace('## Universal bridge','## Universal bridge')
(R/'REPORT.md').write_text(report,encoding='utf-8')

# Keep the latest source pins explicit; only own status and the shared board may advance.
changes=[]
for pin in rd(R/'out/SOURCE_RECEIPTS.json'):
 p=Path(pin['path']);h=hashlib.sha256(p.read_bytes()).hexdigest()
 if h!=pin['sha256']:changes.append({'path':str(p),'before':pin['sha256'],'after':h})
assert all(x['path'].endswith('STATUS.md') or x['path'].endswith('BOARD.md') for x in changes),changes
save(R/'out/SOURCE_READBACK.json',{'changes':changes,'meaning':'Own status intentionally advances; mutable board changes are not promoted into proof premises.'})
helper=B/'code/check_transport.py'
save(R/'out/HELPER_PROVENANCE.json',{'path':str(helper),'sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),
 'usage':'Own prior exact prime-log helper only for equality endpoints; all Boolean/model/reference computation independent of author checkers.'})
p=rd(R/'PROGRESS.json');p.update(deliverable_status='COMPLETE_SINGLE_SOURCE_AND_PROTOCOL',
 mathematical_status='PRESCRIBED_EXIT_SOURCE_PROOF_REVIEW_PENDING_FULL_FEI_OPEN')
p['mathematical_delta']+=f" Frozen full{full['exact_assertions']} checks PASS; positive signed spent-history reset certified. Original rate unchanged; no universal FEI improvement."
p['source_artifacts'] += [str(R/'out/EXACT_EXIT_RESET.json'),str(R/'out/POSITIVE_RESET_CERTIFICATE.json')]
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
protocol=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
cf=set(protocol['required_per_run']['claim_fields']);pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==cf for c in claims);assert set(p)==pf
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes() and p['packet_ids']==['A099']
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rsplit('## Universal bridge',1)[1].strip()
(O/'STATUS.md').write_text(f"STATE: A099 v7 source/protocol saved: mixed active/dummy/control chains reconstructed; prescribed unqueried exit-source reset/full source continuation paid from SAME original quota; {full['exact_assertions']:,} exact checks PASS; independent review pending, FEI OPEN.\nNEXT: A097/A094/A085 review exit-source theorem; pay prescribed reset AFTER an actual exit query with SAME old debit and both full terminals; integrated audits remain pending.\n",encoding='utf-8')
with (O/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+f": v7 finalized: complete imported mixed-reset chain reconstructed without scope widening. Prescribed unqueried exit-source reset/source continuation fits original rate; all-exit-convert policy leaves18e versus12e for inherited-exit policy (different policy, same rate). Pilot{pilot['exact_assertions']}/full{full['exact_assertions']} exact checks PASS; positive signed reset after prior debit certified. New theorem pending independent review, universal FEI/two integrated audits open. memok held; no Lean/PDF/background research.\n")
with (O/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nA prescribed source reset at an unqueried non-active exit is paid by the current original envelope: control exit source R costs c; dummy exit marginal then vacuum calibration costs <=c. Its entire marginal/calibrated pure-source restriction tree costs <=c by complete-reference telescoping. Thus the creating non-active transaction costs<W+2e rather than inherited-off<W+8e, even if the signed reset itself is positive. Mixed live histories with optional conversions retain>=12e_root at original K=2C0+10; all non-active exits converted retain>=18e_root. The stronger reserve belongs to a different exit policy, not a changed universal constant. Do not extend this to a different prescribed reset AFTER a query already executed inside that exit while leaving its other sibling reference fixed.\n')
assert len((O/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
validation={'status':'PASS','claims':len(claims),'DAG_nodes':len(nodes),'open_universal_conjectures':4,
 'full_exact_checks':full['exact_assertions'],'positive_reset_occurrences':full['positive_spent_nonconstant_exit_resets'],
 'new_theorem':'PENDING_INDEPENDENT_REVIEW','full_FEI':'OPEN','integrated_audits':'BOTH_PENDING',
 'Lean':'NOT_LAUNCHED_MEMOK_HELD','remote_copy':'UNVERIFIED'}
save(R/'out/FINAL_VALIDATION.json',validation)
receipts=[]
for q in list(R.rglob('*'))+[O/'STATUS.md',O/'WORKLOG.md',O/'LEARNED.md']:
 if q.is_file() and q.name!='PERSISTENCE_RECEIPTS.json':
  raw=q.read_bytes();assert len(raw)<20_000_000
  receipts.append({'path':str(q),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(R/'out/PERSISTENCE_RECEIPTS.json',{'at':stamp,'artifacts':receipts,'supervisor_mirror':'UNVERIFIED'})
# Actual post-write byte readback, not merely a list of intended output names.
for receipt in receipts:assert hashlib.sha256(Path(receipt['path']).read_bytes()).hexdigest()==receipt['sha256']
print(json.dumps(validation))
print('PERSISTED_BYTE_READBACK',len(receipts))
