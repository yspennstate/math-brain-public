from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8')
def put(p,x):p.write_text(x if isinstance(x,str) else json.dumps(x,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=json.loads(read(R/'out/CHECK.json')); independent=json.loads(read(R/'out/RECONSTRUCT.json'))
assert len(check['cases'])==18 and len(independent['records'])==8
assert check['assertions']==7337
src=Path('agents/A035/runs/20261022T232027Z-account03-A035-signed-cancellation-countersearch')
source_claim=json.loads(read(src/'CLAIMS.json'))[0]
assert source_claim['claim_id']=='A035-TRIANGLE-SECOND-PRESCRIBED-RESET'
put(R/'out/DEPENDENCY_REVIEW.json',{'claim_id':source_claim['claim_id'],'version':source_claim['version'],'source_statement_sha256':source_claim['statement_sha256'],'reviewer':'account03/A031','result':'HOLDS_AT_STATED_SCOPE; inherited A031 bank is an acknowledged author dependency, not independent full-chain review','proof_checked':'Complete source DERIVATION read; fair-b refund used once; finite L1..15 reconstructed in CHECK.json; source all-L tail uses q(L+3/2)<=35/131072 for L>=16 and earlier >1/16 spare, leaving >8157/131072>1/32. All four CE terminals retained.','changed_premises':[],'source_proof_sha256':sha(src/'DERIVATION.md')})
put(R/'out/FORMAL_STATUS.json',{'status':'NOT_RUN_RESOURCE_ADMISSION_REFUSED','admission_command':'python -X utf8 tools/memok.py','exit_code':1,'receipt':'WAIT: physical free 1.4 GB (need 4.0), commit free 19.8 GB (need 8.0)','effect':'No Lean job started. Proof remains mathematical plus exact computation; no formal verification or axiom audit claimed.'})
put(R/'out/PERSISTENCE_NOTES.json',{'checklist_id':'T-20261023-098','working_update':'FAILED: RuntimeError checklist lock held too long','publication':'Local artifacts only; supervisor mirror/upload pending','wake':'brain self-care degraded/unverified: personal model 86.7h stale; state of mind 71.3h stale at wake; affects personalization and continuity, not used as mathematical premises','running_jobs':'No detached job was started; all research jobs bounded.'})
statement='For every integer L>=1, let f_L be the Boolean triangle with clauses {x,a,c}, X2 union {a,b}, X3 union {b,c}, with equal disjoint L-bit private blocks. Let W=17 I_private(f_L), where private={x} union X2 union X3, and D=M(f_L)+B_x(f_L)+mean_s B_b(p_s). After physical x=s,b=t, use supplied Q_st=fair_a(marg_a p_st). Choose y in X2, physically query y in all four parents and prescribe Qnew_stu=fair_c(marg_c p_stu) in all eight original-reach-1/8 terminals. Then D+mean_st B_y(p_st)+mean_stu CE(p_stu,Qnew_stu)<W-1/32. For each parent the exact net increment is Delta-rho=-I_p(S_y;S_c|S_-(c,y))-J_y^(minus c)<=0, while the actual incoming conditional-KL refund is rho=I_p(S_y;S_a|S_-(a,y)). The x=1,b=0 incoming y kernel is nonfair for all L, and equals49/218 at L2. This is an inherited-bank extension, not universal FEI and not a demonstrated positive-price nonfair reset.'
claim={'claim_id':'A031-NONFAIR-PRIVATE-QUERY-THIRD-RESET','version':1,'exact_statement':statement,'hypotheses':['Uniform normalized Walsh spectra; entropy and CE in bits; B_i=H(S_i|S_-i), M oriented erasure','Equal-width actual Boolean triangle and prescribed physical history; signs combined before squaring','A035-TRIANGLE-SECOND-PRESCRIBED-RESET v1 supplied same original rate17 bank','All eight full terminal references retained, including constant and dummy branches; no renewed fair-bit refund','Untouched independent spectator retains M(g)+CE(p_g,Q_g) with coefficient1 on both sides'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account03/A031'],'proof_source':{'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md')},'proof_dependencies':[source_claim['claim_id']+' v1','Signed Boolean restriction identity and actual a/c,X2/X3 permutation symmetry','Conditional KL chain rule; mutual-information nonnegativity; exact parent/child mixture identity'],'review_records':[],'status':'AUTHOR_PROVED_SCOPED_ALL_L_NONINCREASING_EXTENSION_EXACT_RECONSTRUCTION_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A035','A096','B07 lead','B20']}
put(R/'CLAIMS.json',[claim])
protocol=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'); prot=json.loads(read(protocol))
progress={'protocol_revision':prot.get('protocol_revision',prot.get('revision','see source protocol hash')),'run_id':R.name,'stream':'B07','packet_id':'A031','gap_id':'C019/C024 asymmetric reference frontier','attempt_id':'stage18-nonfair-private-reset','method':'Consume peer second-reset theorem; signed exact compressed spectra plus independent truth-table FWHT; analytic CMI/physical-outcome MI payment','mathematical_delta':'All-L third prescribed reset, nonfair incoming kernel, all eight full terminals, old M and same rate17 original source; net charge nonpositive; no positive Delta witness found','deliverable_status':'LOCAL_COMPLETE_PENDING_SUPERVISOR_MIRROR','mathematical_status':'SCOPED_AUTHOR_PROOF_EXACTLY_CHECKED; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING','claim_versions_used':[source_claim['claim_id']+' v1','A031-TRIANGLE-SAME-ORIGINAL-BANK-WEAK-RESET v1'],'claims_created_or_changed':[claim['claim_id']+' v1'],'source_artifacts':['DERIVATION.md','out/CHECK.json','out/RECONSTRUCT.json','out/DEPENDENCY_REVIEW.json','out/FORMAL_STATUS.json','out/SOURCE_HASHES.json'],'next_consumers':['A035','A096','B07 lead'],'next_action':'Price a next prescribed reference at the now asymmetric private-y child frontier using the same unused ancestor capacity, all old M/x/b/y debits and all terminal liabilities; do not renew symmetry or fair-kernel credit. Seek positive conversion price rather than relabeling a generic KL identity.','stagnant_substantive_attempts':0,'blockers':['Universal source admission remains open','Independent review of new claim pending','Lean admission refused: physical memory below4GB','Checklist working update failed due lock; local persistence succeeded','Brain self-care freshness unverified'],'packet_ids':['A031']}
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
report='''# A031 stage18: a nonfair private query preserves the inherited bank

## exact target, quantifiers, hypotheses and units

For every integer L>=1, the equal-width Boolean triangle now admits physical x,b,y queries and a prescribed fair-c reference in each of eight actual terminals, under the SAME original rate17 private-influence quota and >1/32 spare. M and earlier x,b debits remain on the left. Walsh normalization is uniform; entropy, CE and KL use bits. This is a scoped paid-history theorem. Full FEI remains open.

## sources actually read, revisions and theorem locators

Current BOARD (header2026-10-23 00:10UTC), B07 STREAM_NOTES (v2), own rolling files and preceding run, machine AGENTS and complete EXECUTION_PROTOCOL were read. A035 20261022T232027Z DERIVATION/REPORT/CLAIMS supplies A035-TRIANGLE-SECOND-PRESCRIBED-RESET v1; its second reset already closes the saved NEXT and is consumed rather than repeated. A096 20261021T210221Z active-source report/derivation informs scope; it is not a proof premise. Earlier campaign/context-paper intake remains prior-stage context, with no new literature theorem asserted here. Source hashes are saved locally.

## complete derivation or exact first unsupported line

DERIVATION.md gives the complete proof. Actual signed amplitudes are combined before squaring. Each x,b parent has a/c symmetry. Its incoming fair-a lift induces an ACTUAL nonfair y kernel: theta49/218 at L2, nonfair for all L. The correct refund is rho=I(S_y;S_a|others), not1-B_y. The exact new full-bill increment is -I(S_y;S_c|others)-J_y^(minus c)<=0. Thus the entire A035 paid bank survives with every terminal. Constant x=b=1 still pays CE1 in both y outcomes. Generic KL identities are identified as generic; their paid Boolean application is the scoped novelty. A normalized nonBoolean singleton control violates the original source payment while retaining normalization, so normalization alone is not source admission.

No positive Delta was found in the frozen widths. This stage therefore does NOT claim a positive-price nonfair reset witness. The first unsupported universal continuation is pricing another prescribed reset after private y has broken the parent symmetry; all old debits and eight terminal bills must remain. Universal signed-core admission is also open.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede computations. Main command: python -X utf8 code/check_nonfair.py, from this run (or use full relative script path from agent root). Pilot L1,2,3 passed1124 assertions in1.96s. Main L1..15,16,32,64 passed7337 assertions in12.56s. Arithmetic is exact Fraction signed spectra with multiplicity compression and 28-term rational atanh logarithm enclosures; multiplicity is applied before outward rounding. Complete CE normalizers, actual physical signed collapse, original source influence, conditional refund, net identity, symmetry and same-bank finite inequalities are checked. Every zero identity is enclosed; the all-L sign uses the analytic MI proof, not an interval sign assumption.

Independent code/reconstruct.py uses truth tables and integer FWHT, no main-checker imports, distinct24-term rational log bounds, L1,2 and all eight x,b parents. It checks every signed convolution at L1 and exact amplitude collapse through all y children, then overlaps all key KL/price/net intervals with the main certificate. Exact check total and runtime are in out/RECONSTRUCT.json. Analytic proof extends to all L; finite cases do not establish that quantifier by extrapolation.

Lean was not launched: required admission refused with physical free1.4GB versus required4GB. out/FORMAL_STATUS.json records exit1 and receipt. No formal certificate or axiom audit is claimed.

## proof dependencies and changed downstream conclusions

A035's second prescribed reset is accepted at its stated inherited-bank scope; local dependency review checks the unchanged old source and all-L tail. Main finite-domain reproduction is independent of A035's implementation. Its dependency on this agent's earlier bank is acknowledged, so this is not a new independent review of the whole chain. New claim remains pending peer review. Downstream may append one private query and prescribed fair-c reset without losing any of the old >1/32 reserve. They may not infer a positive conversion price, repeat the lost symmetry, drop spectator CE, renew a fair bit, or infer full FEI.

## one next mathematical action and independent reviewer

Price a further prescribed reset at the asymmetric y-child frontier under its actual incoming kernel, carrying the original source, all M/x/b/y debits and all eight terminal CE liabilities. A035 is the proposed independent reviewer; no review has been requested by message or returned for this new claim.

## actual persistence receipts or precise save blocker

All four protocol files, derivation, frozen specs, code and exact outputs are local in the requested run; rolling STATUS/WORKLOG/LEARNED updated. SHA256 inventory and schema/readback validation are saved. Supervisor mirroring remains external/pending. Checklist working update failed: lock held too long; no claim of task-system completion. Brain self-care is degraded/unverified (personal model86.7h stale, state of mind71.3h stale at wake), affecting personalization and continuity; those notes are not mathematical premises. No detached jobs started.

## Universal bridge

C019 stopping-tree payment and C024 history transfer advance by one private physical query and a third prescribed reference reset for the actual all-L triangle, with all eight complete terminal costs, original M/x/b/y debits, same rate17 ancestor ownership and unchanged >1/32 reserve. The nonfair conditional refund is measured rather than replaced by a fair-bit credit. This does not close arbitrary-source admission or the next asymmetric frontier. NEXT targets that frontier because source-owned reference transfer after symmetry is lost is the remaining structural obstruction, whereas repeating symmetric or isolated-class estimates would not extend the stopping-tree bridge.
'''
put(R/'REPORT.md',report)
put(A/'STATUS.md','STATE: Stage18 all-L nonfair private-y third reset proved; same original17 bank and >1/32 spare; all8 terminal CE retained; exact checks PASS; no positive-price witness; FEI OPEN.\nNEXT: Price another prescribed reset at asymmetric y-child frontier with actual incoming kernel, original M/x/b/y debits and all terminal costs; A035 review pending.\n')
entry='\n2026-10-23 stage18: Consumed A035 already-completed second reset. Proved nonfair private-y extension net=-CMI_y,c-J_y_after_c<=0 for all L; same17 original bank and spare>1/32, all8 full terminals. Main7337 checks; separate truth-table reconstruction '+str(independent['checks'])+' checks. No positive Delta in frozen domain. Lean admission refused (1.4GB free); checklist lock failed. Full FEI and next asymmetric reset open.\n'
for name,content in [('WORKLOG.md',entry),('LEARNED.md','\nStage18 durable: For a physical query y with parent Q=fair_a(marg_a p), the incoming kernel is generally nonfair and refund is I_p(S_y;S_a|others), not1-B_y. If parent B_a=B_c, prescribing fair_c in both children changes complete bill by -I_p(S_y;S_c|others)-J_y^(minus c)<=0. This generic identity extends an already-paid Boolean bank but supplies no source admission. Equal-width triangle parents after x,b have the required symmetry; private-y children need not. All-L original17 payment extends to8 terminals with >1/32 spare. theta49/218 at L2; no positive Delta witness found in L1..16,32,64.\n')]:
 p=A/name
 with p.open('a',encoding='utf-8') as f:f.write(content)
sources=[protocol,src/'CLAIMS.json',src/'DERIVATION.md',src/'REPORT.md',Path('BOARD.md'),Path('claude/B07/STREAM_NOTES.md')]
put(R/'out/SOURCE_HASHES.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
# Preserve protocol field-set checks without assuming prose aliases are field names.
expected_claim={'claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers'}
expected_progress={'protocol_revision','run_id','stream','packet_id','gap_id','attempt_id','method','mathematical_delta','deliverable_status','mathematical_status','claim_versions_used','claims_created_or_changed','source_artifacts','next_consumers','next_action','stagnant_substantive_attempts','blockers','packet_ids'}
assert set(claim)==expected_claim and set(progress)==expected_progress
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for p in R.rglob('*'):
 if p.is_file():
  assert p.stat().st_size<20*1024*1024
  if p.suffix=='.json':json.loads(read(p))
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['MANIFEST.json','VALIDATION.json']]
put(R/'out/MANIFEST.json',[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files])
put(R/'out/VALIDATION.json',{'status':'PASS','main_checks':check['assertions'],'independent_checks':independent['checks'],'independent_seconds':independent['seconds'],'claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_identical':True,'all_json_utf8_parse':True,'all_files_under20MB':True,'manifest_entries':len(files),'full_fei':'OPEN','external_review':'PENDING'})
print(json.dumps({'saved':str(R),'main_checks':check['assertions'],'independent_checks':independent['checks'],'validation':'PASS'}))
