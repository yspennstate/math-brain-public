from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
assert A==Path(r'agents\A067')
OLD=A/'runs/20261023T015109Z-fleet03-A067-hypercontractive-refinement'
REVIEW=Path(r'agents\A088\runs\20261023T025955Z-fleet03-A088-booleanity-referee')
def write(name,value):
 p=R/name;assert p.resolve().is_relative_to(A.resolve());p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n' if not isinstance(value,str) else value,encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
protocolpath=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
# Read-only source refresh; paper/context hashes do not imply a new theorem was used.
paths=[Path(x['path']) for x in json.loads((OLD/'out/SOURCES.json').read_text(encoding='utf-8'))]
paths += [REVIEW/'PROOF.md',REVIEW/'CLAIMS.json',protocolpath]
sources=[]
for p in dict.fromkeys(paths):
 if p.is_file():
  data=p.read_bytes();encoding='utf-8-sig'
  try: data.decode(encoding)
  except UnicodeDecodeError:encoding='binary'
  sources.append({'path':str(p),'sha256':sha(data),'bytes':len(data),'encoding':encoding,'role':'Read-only source refresh; primary mathematical reliance stated in REPORT.md'})
write('out/SOURCES.json',sources)
pilot=json.loads((R/'out/PILOT.json').read_text());main=json.loads((R/'out/CHECK.json').read_text());audit=json.loads((R/'out/INDEPENDENT_AUDIT.json').read_text())
assert all(x['status']=='PASS' for x in [pilot,main,audit])
oldclaims=json.loads((OLD/'CLAIMS.json').read_text())
transfer=oldclaims[1]
assert transfer['statement_sha256']==sha(transfer['exact_statement'].encode())
transfer['review_records'].append({'reviewer':'fleet03/A088','verdict':'HOLDS_AT_EXACT_CANONICAL_SELECTED_HISTORY_SCOPE','independent':True,'substantive_repair':False,'source':str(REVIEW/'PROOF.md'),'locator':'section 1; unchanged author statement; sections 2-6 supply positive-partner obstruction and scope guards'})
transfer['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
statement=('For every integer m>=2 take canonical b_m(Y)=(-1)^(sum_j Y_(2j-1)Y_(2j)), c_m=b_m-2*1{w=0,Y=0}, G_m with z terminals b_m,c_m, A=2^-m, d=A^2. On c_m query a=Y1, stop a=1 and query exposed partner b=Y2 on a=0; retain all three c leaves with original G reaches 1/4,1/8,1/8 and the unchanged b_m terminal. Every reference is only the corresponding marginal of the original full spectrum of c_m. For the complete two-child CE drops L0,L1, L0<=1 and L1<1+3d/(1+d). With the single rate3 chosen at the original source, the root-weighted CE debit E_Q(3)<-9d/4. The full weighted terminal KL K_F<9/16, hence actual entropy debit E_H(3)=E_Q(3)+K_F<9/16-9d/4. The original additional reserve I_X=(I(b_m)+I(c_m))/2=m+(2m+1)d/2 pays this bill after unchanged old D, with r3-E_H(3)>m-9/16. Old rate2 invoices are retained by E_Q(2)-E_Q(3)=E_H(2)-E_H(3)=1/4+d, and E_H(2)<13/16-5d/4. Full signed frontier identities S_Q=S3+E_Q(3), S_H=S_Q+K_F, S_H-(D+E_H(3))=r+I_X hold. For fixed real C, E_Q(C)->(3-C)/4, so3 is the sharp threshold for nonpositive CE debit of this exact block. No iteration, nonpositive actual entropy debit at rate3, arbitrary-core payment or full FEI is asserted.')
claim={'claim_id':'A067-FIRST-EXPOSED-PARTNER-PAIRED-RATE3','version':1,'exact_statement':statement,
 'hypotheses':['Uniform Boolean canonical quadratic phase with marked all-zero jet and dummy w; m>=2','Only the specified first intact-plus-partner stopping block, with every physical child and full Fourier label retained','A single original rate choice3 supplies exactly the original increment I_X; original D and old rate2 invoices explicitly retained','No reference reset, clipping, renewed child bank or repeated supply of I_X'],
 'statement_sha256':sha(statement.encode()),'contributors':['fleet03/A067; A088 supplied independently reconstructed positive-partner obstruction and scope guard'],
 'proof_source':str(R/'PROOF.md'),'proof_dependencies':['A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK@1','A067-EDITED-INTACT-PAIR-CONDITIONAL-SOURCE-TRANSFER@1','A088 20261023T025955Z PROOF sections 2-3 for exact partner formulas and asymptotic sharpness'],
 'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CHECKED_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A088','A070','A094','A066','A096','B14','B20']}
write('CLAIMS.json',[transfer,claim])
nextaction='At one fixed original rate3, price a second completed-pair block or a necessary w query using the same original reference and remaining reserve after the paid first block; retain original D, legacy invoices and all terminal KL. Derive changed-profile likelihood bounds before claiming iteration. A088/A070/A094 independent review.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A067','gap_id':'G-R-MISMATCH-POSTCORE-UNUSED-CHILD-RESERVE','attempt_id':'A067-stage19-first-partner-paired-original-rate3',
 'method':'Exact occupancy-changing source cost; paired query at one fixed original rate; explicit bounded full KL invoice funded from named once-only original increment; no-reset signed audit',
 'mathematical_delta':'First positive exposed-partner profile is paid at one original rate3: E_Q(3)<-9A^2/4, full K_F<9/16, old E_H(2)<13/16; threshold3 for nonpositive CE is asymptotically sharp. A088 stage18 acceptance consumed; frozen rate2 residual-only failure retained. No universal FEI constant change.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':['A067-FIRST-EXPOSED-PARTNER-PAIRED-RATE3@1','A067-EDITED-INTACT-PAIR-CONDITIONAL-SOURCE-TRANSFER@1 independent A088 acceptance consumed'],
 'source_artifacts':['PROOF.md','REPORT.md','FROZEN_SPEC.json','FROZEN_TERMINAL_AUDIT.json','FROZEN_LEGACY_AUDIT.json','FROZEN_INDEPENDENT_AUDIT.json','code/check.py','code/audit.py','code/finish.py','out/PILOT.json','out/CHECK.json','out/INDEPENDENT_AUDIT.json','out/SOURCES.json','out/RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['New source-complete theorem awaits independent review; iteration and universal initial-source supply open','Supervisor adoption/mirrors unverified; no git authorized','Prior disclosed outside-tree placeholder remains untouched pending explicit deletion approval; not a mathematical blocker','Brain self-care degraded: stale owner model and state-of-mind material excluded from mathematical evidence'],
 'packet_ids':['A067']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

For every integer m>=2 pay the first occupancy-changing exposed-partner query on the canonical Boolean edited-bent G_m, from the SAME original source. All entropies and CE/KL bills are in bits. The history is c_m: query Y1, stop outcome1, query Y2 on outcome0; all three c leaves and unchanged clean z terminal are retained. This stage changes mechanism to a single rate3 chosen at the ORIGINAL source. The frozen rate2 residual-only extension remains false. Full FEI is OPEN.

# sources actually read, revisions and theorem locators

The current BOARD row A088 supplied the new independent review at {REVIEW / 'PROOF.md'}, section1 accepting the stage18 claim unchanged; sections2-4 give the positive partner profile, all-dimensional residual-only failure and full KL conversion. Section5 gives the normalized-real phase guard. B14 STREAM_NOTES v2 remains unchanged; its leaf-certificate direction is followed through explicit stopping-node payment. Own prior STATUS, WORKLOG, LEARNED, prior PROOF/CLAIMS and EXECUTION_PROTOCOL.json revision {protocol['revision']} were consumed. Campaign index, supplement, earlier runs and paper-context texts were refreshed read-only and byte-pinned in out/SOURCES.json; no new paper theorem is invoked. No internet theorem claim or new brain write is used. The read-only math recall returned the every-coordinate/Booleanity obstructions, consistent with retaining exact scope; it supplied no new payment theorem.

# complete derivation or exact first unsupported line

PROOF.md is the complete analytic proof. Set d=A^2, A=2^-m. Exact Boolean edges give Inf_a=1/2+d and Inf_b|a0=2d. The old intact-query result gives L0<=1. For the ACTUAL changed partner profile, the exact rational identity sum P1*(Q2/(2Q1)-1)=2d/(1+d), together with ln x<=x-1 and ln2>2/3, yields L1<1+3d/(1+d). Therefore the original-reach CE debit E_Q(3)<-9d/4. The full terminal likelihood bounds 2,4,sqrt(2) give the complete weighted KL bill K_F<9/16. Thus E_H(3)<9/16-9d/4; it is paid from the once-only original extra reserve I_X>m, leaving r3-E_H(3)>m-9/16.

All old rate2 invoices are explicit: E_Q(2)-E_Q(3)=E_H(2)-E_H(3)=J=1/4+d. In particular the unrepriced old entropy invoice is <13/16-5d/4. The exact rate3 ledger uses E_Q(3), not E_Q(2); its terminal extra influence is I_X-J. Both full children, original old D, signed inherited banks and complete KL remain. The same-source telescope is background accounting, not the payment theorem. Nonpositive actual entropy debit at rate3 is NOT claimed: the finite checked E_H(3) values are positive.

For fixed C, E_Q(C)->(3-C)/4; this block's nonpositive CE threshold3 is sharp. It is not a sharp universal FEI constant. The normalized-real untouched-pair relaxation preserves this experiment, so this is an exact Boolean-family improvement and not a new exploitation of all Boolean convolution identities. The first unsupported line is that subsequent changed-profile blocks and their full conversion costs can always be funded from the remaining ORIGINAL reserve at the same fixed rate. That line remains open.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded each initial computation and subsequent terminal/legacy audit addition. Final pilot: {pilot['checks']} exact checks, m2, {pilot['runtime_seconds']:.6f}s. Main: {main['checks']} exact checks, literal m2,3,4,5 and grouped m2..16, {main['runtime_seconds']:.6f}s. Separate implementation: {audit['checks']} exact checks on m2,3, {audit['runtime_seconds']:.6f}s; direct character sums without FFT, imported helper or logarithm routine. All PASS. The earlier preliminary pilot/main runs also passed before added checks; final receipts describe the stronger checks.

Commands, from A067: `python -X utf8 -B runs/{R.name}/code/check.py pilot`, then the same command with `full`, then `python -X utf8 -B runs/{R.name}/code/audit.py`. Integer Walsh transforms, direct physical edges, Fraction arithmetic, and 28-term atanh log intervals with proved exact rational tail establish signs; decimal output is display only. No unbounded search, automatic dimension increase, heavy-memory job, GPU or detached process was used. Memory estimates were90MB main and25MB independent; no >300MB admission was needed. No Lean certificate is claimed. The all-m proof is analytic, not extrapolated from the finite domain.

# proof dependencies and changed downstream conclusions

Stage17 original C2 bank was already independently accepted. Stage18 intact-query transfer is now independently accepted unchanged by A088; CLAIMS.json records the source-bound review. The NEW claim awaits A088/A070/A094 review. A088's residual-only refutation remains intact and motivated the named additional original source. Prior 117038-check intact-history result is not rerun or renamed as new progress. No arbitrary-core supplier, universal FEI constant, other stream claim or public theorem is changed.

# one next mathematical action and independent reviewer

{nextaction}

# actual persistence receipts or precise save blocker

REPORT.md, PROOF.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, frozen specs, code and exact outputs are saved locally inside A067. Protocol field sets, statement hashes, compatibility equality, file sizes and SHA256 receipts are checked by code/finish.py and recorded in out/RECEIPTS.json. The rolling STATUS has exactly two lines; WORKLOG and LEARNED preserve the result and gap. No git or shared-tree modification is authorized; supervisor adoption and mirrors remain unverified. The previously disclosed outside-tree placeholder remains untouched pending deletion approval. Brain self-care is degraded because owner-model/state-of-mind notes are stale; these personal-context sources are excluded from mathematical evidence. This stage's work is stopped after final checks; no computation is intentionally left running.

# Universal bridge

C019 stopping-tree payment, with C024 reference-history retention, moves past the first actual occupancy-changing partner profile: at one ORIGINAL rate3 the paired source debit is strictly negative, and the entire terminal KL invoice is explicitly funded from a named once-only original increment. This does not repair frozen-rate2 residual-only payment and does not iterate the supplier. What remains is an influence-priced bound on subsequent changed-profile costs with the original owner, diminished reserve, old debits and all full terminals preserved. Testing the next such block at the SAME rate and reference is the shortest route toward a reusable universal stopping-tree mechanism, rather than producing another isolated entropy bound.
'''
write('REPORT.md',report)
status='STATE: Stage19: first positive exposed partner PAID at ONE original rate3; E_Q<-9A^2/4, full KL<9/16;1571+262 exact checks PASS; new review pending; FEI OPEN.\nNEXT: Price second completed-pair block or w using SAME original rate3/reference, diminished reserve, old rate2 invoices/D and full terminal KL; A088/A070/A094 review.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
entry=f'''\n## 2026-10-23 stage19, fleet03 (run {R.name})
Consumed A088 independent acceptance of stage18 and all-m failure of residual-only partner payment. Changed mechanism: ONE global original rate3. New exact partner bound sum P1(Q2/(2Q1)-1)=2A^2/(1+A^2), hence source paired E_Q(3)<-9A^2/4. Full terminal KL<9/16; actual entropy debit is positive in m2..5 but funded from once-only original I_X, not reset/renewal. Old E_H(2)<13/16 and E2-E3=J=1/4+A^2 explicitly retained. Rate3 sharp for nonpositive CE block. Final main1571 plus independent direct-character262 checks PASS; pilot55. Actual entropy rate3 sign is NOT asserted negative. All-m proof analytic; no Lean certificate or universal FEI result. NEXT: second required changed profile from SAME diminished original source. Prior outside-tree placeholder untouched pending approval; personal brain self-care degraded and excluded from math.
'''
for name in ['WORKLOG.md','LEARNED.md']:
 with (A/name).open('a',encoding='utf-8') as f:f.write(entry)
# Required schema sets are checked literally; protocol uses a descriptive suffix on packet_ids.
requiredprogress={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==requiredprogress
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==set(claim) for c in [transfer,claim])
assert all('# '+h in report for h in protocol['required_per_run']['report_fields'])
assert json.loads((R/'PACKET_DELTA.json').read_text())==progress
assert len((A/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  data=p.read_bytes();assert len(data)<20_000_000
  receipts.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':sha(data)})
write('out/RECEIPTS.json',{'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_checks':'All exact field sets, hashes, compatibility and two-line STATUS pass','artifacts':receipts,'brain_selfcare':'DEGRADED_UNVERIFIED_PERSONAL_CONTEXT_EXCLUDED','mirror_status':'UNVERIFIED_SUPERVISOR_OWNED'})
print(json.dumps({'status':'PASS','run':R.name,'sources_read':len(sources),'receipt_count':len(receipts),'new_statement_sha256':claim['statement_sha256'],'main_checks':main['checks'],'independent_checks':audit['checks']}))
