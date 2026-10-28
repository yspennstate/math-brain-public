from pathlib import Path
import json,hashlib,copy
root=Path(__file__).resolve().parents[1];agent=root.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=read(root/'out/CHECK.json');ind=read(root/'out/INDEPENDENT.json')
assert main['status']==ind['status']=='PASS'
assert main['helper_sha256']==sha(root/'code/check_stage.py')
assert ind['runner_sha256']==sha(root/'code/check_independent.py')
assert ind['base_sha256']==sha(root/'code/independent_base.py')
statement=('Let F be any finite genuine disjoint formula of Boolean gates with literal leaves, under any interior independent physical product law, with all gates evaluated at actual induced child laws and constants contracted. Let omega be the usual influence/child-variance weights, Delta=I-Var, R_tree=sum_v omega_v R(g_v), and E_1 the corrected singleton entropy in natural units. At each node define the actual singleton scale import T=T_out+T_in as in A043, and its imported mantissa refund V by replacing each singleton dyadic charge j ln4 in those two imports by ln(1/u^2), where 1/2<u=2^j|c|<=1. Then T,V>=0 and T+V+E_1(parent)=E_1(gate)+sum_i a_i E_1(child_i) exactly. Thus T_tot+V_tot+E_1(F)+S_tree=4Delta(F)-2R_tree, where S_tree=sum_v omega_v[4Delta(g_v)-2R(g_v)-E_1(g_v)]>=0. In particular the TOTAL singleton import satisfies T_tot<=4Delta(F)-2R_tree-E_1(F), uniformly in depth, fan-in and biases. This coefficient is not claimed sharp. Separately ln4 C_hi,tot+L_hi(F)=sum_v omega_v L_hi(g_v)+V_tot. With complete singleton-preserving paid-sector references and ordinary full KL, the signed flat/tree conversion is K_flat-K_tree=ln4 C_hi,tot-V_tot+n_F-sum_v omega_v n_v, retaining both full terminal laws and final singleton masses. No reference normalizer or imported refund is renewed. The universal arbitrary-prime high-degree scale J_hi remains unproved; the conditional composition FEI+ constant K+4+ln4 is unchanged.')
hyp=['Finite actual Boolean functions; independent physical product law; deterministic coordinates and constant children contracted; natural entropy units',
 'Genuine disjoint physical composition, with actual independent induced child-output laws; literal leaves; omega_root=1 and omega_child=omega_parent I_i(g)/Var(child_i)',
 'Physical normalized coefficients; dyadic upper-boundary convention 1/2<2^j|c|<=1; zero-mass terms omitted',
 'Complete paid-sector references preserve all actual empty and singleton masses and retain every occupied high atom; ordinary KL replaced with its reference',
 'Original singleton and mantissa banks counted once; R_tree is a weighted gate sum, not asserted equal to final R_F; universal prime scale is not assumed paid']
canonical=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'))
claim={'claim_id':'A044-ALL-DEPTH-SINGLETON-IMPORT-OWNER','version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(canonical.encode()).hexdigest(),'contributors':['A044/account03'],
 'proof_source':{'path':'PROOF.md','sha256':sha(root/'PROOF.md')},
 'proof_dependencies':[{'claim_id':'A043-SINGLETON-IMPORT-BOUNDARY-AND-DEPTH','version':1,'statement_sha256':'0f4a98356a94028224020188918ef2d3caef8cc3aff708df442d04cf3814f2f6','scope':'Actual import definitions and exact high-scale partition; independently reconstructed and reviewed'},
 {'claim_id':'A041-PAID-SECTOR-ADAPTIVE-CARRY','version':1,'scope':'Comparison with its paid-sector joint telescope only; new two-account split derived directly here'},
 'Direct coefficient factorization, exact entropy/KL identities and weighted finite telescoping; Boolean physical singleton derivative bound'],
 'review_records':[],'status':'AUTHOR_ANALYTIC_PROOF_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':'Pay actual arbitrary-prime J_hi at every induced product law from SAME genuinely unused original capacity; singleton import closure and refunds do not establish that payment.',
 'next_consumers':['A041','A042','A043','A045','A091','B09 lead']}
origin=agent.parent/'A043/runs/20261023T123418Z-account03-A043-prime-gate-decomposition'
reviewed=copy.deepcopy(read(origin/'CLAIMS.json')[0])
ps=reviewed['proof_source']
if isinstance(ps,list):reviewed['proof_source']=[str((origin/p).resolve()) if isinstance(p,str) else p for p in ps]
elif isinstance(ps,dict):ps['path']=str((origin/ps['path']).resolve())
elif isinstance(ps,str):reviewed['proof_source']=str((origin/ps).resolve())
reviewed['review_records'].append({'reviewer':'A044/account03','outcome':'HOLDS','scope':'Original mathematical import partition, one-boundary bound with refunds, sharp outer-import control and all-depth majority-tower obstruction. Source checker counts and global registry adoption excluded.',
 'source_statement_sha256':reviewed['statement_sha256'],'source_proof_sha256':sha(origin/'PROOF.md'),
 'review_source':str((root/'REVIEW_A043.md').resolve()),'independent_validation':'out/CHECK.json; out/INDEPENDENT.json; out/TOWERS.json','source_mutation':'none'})
claims=[claim,reviewed];dump(root/'CLAIMS.json',claims)
next_action='Pay actual arbitrary-prime J_hi from genuinely unused original capacity AFTER the singleton import/carry debits, retaining the same complete reference, ordinary KL, both full terminal laws and explicit V/S refunds; A043/A041/A045 independently review the new split first.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A044',
 'gap_id':'A044-SIGNED-PROFILE-BOUNDED-CONGESTION','attempt_id':'substantive9-all-depth-singleton-import-owner',
 'method':'Consume A043 boundary/tower dependency and independently review it; derive lost-singleton entropy identity, exact import/refund split, two all-depth original-owner telescopes and signed complete-reference conversion; rational-log-vector pilot and separate direct-cofactor/log-interval pilot.',
 'mathematical_delta':'TOTAL singleton import T_tot paid <=4Delta-2R_tree-E_1(F), without depth or fan-in dependence, with exact V_tot/S_tree refunds. High carries use local high mantissas plus V_tot once; signed flat/tree KL conversion explicit. Universal prime J_hi remains unpaid; no universal FEI constant improved.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW_OF_NEW_CLAIM','mathematical_status':'UNIVERSAL_FEI_OPEN; ALL_DEPTH_IMPORT_OWNER_AUTHOR_PROOF',
 'claim_versions_used':['A043-SINGLETON-IMPORT-BOUNDARY-AND-DEPTH@1','A041-PAID-SECTOR-ADAPTIVE-CARRY@1 (joint-telescope comparison only)','A042-PAID-SECTOR-ACTIVATION-CARRY-OWNER@1 (read control, not needed as proof premise)'],
 'claims_created_or_changed':['A044-ALL-DEPTH-SINGLETON-IMPORT-OWNER@1','A043-SINGLETON-IMPORT-BOUNDARY-AND-DEPTH@1 local independent HOLDS review'],
 'source_artifacts':['PROOF.md','REVIEW_A043.md','out/FROZEN_SPEC.json','out/FROZEN_INDEPENDENT.json','out/CHECK.json','out/INDEPENDENT.json','out/TOWERS.json','out/SOURCE_RECEIPTS.json','out/PERSISTENCE.json'],
 'next_consumers':['A041','A042','A043','A045','A091','B09 lead'],'next_action':next_action,
 'stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-prime J_hi payment remains unproved.','Independent review of new A044 split and supervisor registry/mirror adoption not observed.','Brain self-care degraded/unverified; owner/state/dream notes stale; no mathematical reliance.','Compute-state timestamp unchanged across separated reads; stale snapshot not used as current admission. No heavy job or governor intervention.'],
 'packet_ids':['A044']}
dump(root/'PROGRESS.json',progress);(root/'PACKET_DELTA.json').write_bytes((root/'PROGRESS.json').read_bytes())
report=f'''# A044/B09 stage20 — one all-depth owner for singleton import

## exact target, quantifiers, hypotheses and units

Consume the current B09 singleton-import boundary obstruction and pay the TOTAL import at all depths from its original source. Scope: every finite genuine disjoint formula of actual Boolean gates, every interior independent physical law and actual induced child laws, literal leaves, contracted constants. Natural entropy units. Full FEI remains OPEN; no new universal constant is claimed.

## sources actually read, revisions and theorem locators

Read current BOARD.md B09 section, lead STREAM_NOTES.md v2 and own STATUS.md at stage start. Read A041 run20261023T113320Z PROOF.md sections1-6, especially exact singleton/high joint bank (10); A042 run20261023T120324Z PROOF.md sections1-5, especially fair-selector majority obstruction; A043 run20261023T123418Z entire PROOF.md and CLAIMS.json, especially import equations(1)-(5) and tower(6)-(7). Source claim metadata and hashes saved in out/SOURCE_RECEIPTS.json. Protocol schema is checked directly at persistence. Historical campaign/paper sources were read in earlier stages and are not new mathematical premises. The lead's older address-class target was already completed; this stage follows the current dependency and review bottleneck. B09 review cap is respected by consuming and independently reviewing A043 before the new narrow refinement.

## complete derivation or exact first unsupported line

PROOF.md derives E_1(g)+sum a_i E_1(child)-E_1(F)=T+V from the actual label partition. T is exactly A043 scale import; V>=0 is its imported singleton mantissa refund. Weighted finite telescoping gives T_tot+V_tot+E_1(F)+S_tree=4Delta(F)-2R_tree, with S_tree>=0. Thus total singleton import is paid by <=4Delta with explicit degree and terminal refunds, at any depth/fan-in. This is a DIFFERENT quantity from A043's ln4 one-boundary bound; 4 is not claimed sharp. Separately ln4 C_hi,tot+L_hi(F)=sum omega L_hi(g)+V_tot. Complete reference conversion is K_flat-K_tree=ln4 C_hi,tot-V_tot+n_F-sum omega n_g. All refunds, ordinary KL and both full terminals remain attached, and no paid term is renewed. First unsupported universal line: arbitrary-prime J_hi payment from genuinely unused original capacity after those debits. Conditional universal composition constant K+4+ln4 is unchanged.

## executed validation with domain, arithmetic, commands and outputs

Both frozen specs preceded execution. Main command: python -X utf8 code/check_stage.py from the run (or its run-relative path from A044). Domain: all16 labeled binary roots, children drawn from masks1,6,8 in both positions, two fixed rational physical laws:288 compositions. Added12 predeclared compressed Maj3 tower depths1 through12; no truth-table dimension escalation. Exact Fraction arithmetic and rational prime-exponent vectors for logarithmic identities, plus pointwise coefficient/reference/support checks. PASS {main['exact_assertions']} assertions, {main['positive_import_cases']} positive-import, {main['positive_import_refund_cases']} positive-refund and {main['positive_high_carry_cases']} positive-high-carry cases; runtime {main['runtime_seconds']:.3f}s. Independent command: python -X utf8 code/check_independent.py, 12 fixed compositions; direct alternating cofactor sums and rigorous32-term range-reduced atanh intervals with proved tail. PASS {ind['exact_assertions']} assertions, runtime {ind['runtime_seconds']:.3f}s. Total {main['exact_assertions']+ind['exact_assertions']} exact assertions. Jobs sequential, estimated80 MB each and below55-second frozen runtime caps; no >300-MB job or memok admission needed. No pilot failed. The tower bound uses the stated analytic ln4<2 when comparing rational coefficients. No Lean/formal certification is claimed. The independent base helper is a local copy of the direct-cofactor/log-interval definitions from our preceding run, with its old case loop excluded; its hash is saved.

## proof dependencies and changed downstream conclusions

REVIEW_A043.md independently accepts A043-SINGLETON-IMPORT-BOUNDARY-AND-DEPTH@1 at its original mathematical scope, including the all-depth majority obstruction, without repairing or changing its statement. Source certificate counts are not adopted. The new proof splits A041's existing joint bank into singleton import and high-mantissa accounts; it adds no capacity. Downstream A041/A042/A043 can now use one explicit all-depth import payment with V_tot refunded exactly once into high carry, rather than renewing the false ln4 Delta boundary allowance. Prime scale remains the unresolved supplier. Local copied claim records append review only; no shared registry status is changed.

## one next mathematical action and independent reviewer

{next_action} This is the remaining universal supplier; another selector, singleton normalizer or isolated gate estimate does not fund it.

## actual persistence receipts or precise save blocker

All four protocol files, PROOF.md, review, frozen specs, code and exact outputs are saved inside this run. PROGRESS.json and PACKET_DELTA.json are identical with packet_ids=[A044]. STATUS.md has exactly two lines and WORKLOG/LEARNED append this stage once. out/PERSISTENCE.json records hashes checked by rereading every saved artifact and rolling file, and all pinned shared source hashes remain unchanged. No shared tree, other agent folder, brain store, external message or trading path was modified; no git command or remote publication was used. Supervisor mirroring and new independent review remain unobserved. At wake brain self-care was degraded/unverified (owner-model99.4h, state-of-mind84.0h, dream34.7h stale), affecting personal-context recall, not mathematical premises. The compute-state timestamp remained unchanged across separated reads and governor log was inspected; no blind restart or service intervention was attempted, and no stale memory figure authorized a heavy job. No computation remains running after completed pilots.

**Universal bridge:** This stage moves C020 whole-set witness cost by closing the TOTAL singleton-import debit at every depth from the original singleton bank, with bound4Delta-2R_tree-E_1(F) and exact V/S refunds, and by attaching its separate high-carry and signed complete-reference KL ledgers. It consumes a pending A043 review and prevents repeated boundary payments demonstrated false by the actual majority tower. It changes no universal FEI constant: arbitrary-prime J_hi is still unpaid. The shortest NEXT is that supplier payment from genuinely unused original capacity with these committed refunds/debits retained; another isolated gate class or normalizer cannot fill the named gap.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A044 substantive9 saved: all-depth singleton import T_tot<=4Delta-2R_tree-E1 with exact V/S refunds; separate high-carry/signed KL ledger; 22006+221 checks PASS; A043 import/tower HOLDS; FEI OPEN.\nNEXT: A041/A043/A045 review split; pay arbitrary-prime J_hi from SAME unused original capacity after import/carry debits, retaining V/S refunds, ordinary KL and both full terminals.\n',encoding='utf-8')
marker='2026-10-23 substantive9 / 20261023T125747Z'
for name,text in {
 'WORKLOG.md':'Consumed A041 paid-sector telescope, A042 fair-selector majority obstruction and A043 boundary/tower theorem. Independently accepted A043 original mathematical scope. Derived exact lost-singleton entropy T+V+E1(parent)=E1(gate)+sum a E1(child), hence all-depth T_tot+V_tot+E1(F)+S_tree=4Delta-2R_tree. Separated carry refund ledger and signed complete-reference KL conversion. Main22006 exact checks PASS (1.933s), independent221 PASS (0.587s), no failed pilot/heavy/formal job. Universal prime J_hi remains open. Brain self-care degraded, compute-state stale; neither used as mathematics or heavy-job admission.',
 'LEARNED.md':'At an actual disjoint boundary, root singleton entropy leaves E1 precisely when its child label is high, and child singleton entropy leaves E1 precisely when its outer label is high. Splitting each lost entropy into j ln4 plus mantissa gives exact T+V transport. Thus total all-depth import <=4Delta-2R_tree-E1(F), with V_tot and S_tree retained; 4 not sharp and distinct from ln4 one-boundary constant. High carries obey ln4 C_hi,tot+Lhi(F)=sum omega Lhi(g)+V_tot. Signed full-reference conversion is ln4 C_hi,tot-V_tot+n_F-sum omega n_g. V_tot is the same remaining original singleton refund, not fresh credit. Arbitrary prime J_hi still needs payment.'}.items():
    p=agent/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
    if marker not in old:
        with p.open('a',encoding='utf-8',newline='') as stream:stream.write('\n## '+marker+'\n'+text+'\n')
protocol=read(Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
assert all(set(c)==set(protocol['claim_fields']) for c in claims)
fields=['packet_ids' if x.startswith('packet_ids (') else x for x in protocol['progress_fields']]
assert set(progress)==set(fields)
assert all('## '+s in report for s in protocol['report_fields'])
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for item in read(root/'out/SOURCE_RECEIPTS.json'):assert sha(Path(item['path']))==item['sha256']
files=[p for p in root.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']+[agent/x for x in ('STATUS.md','WORKLOG.md','LEARNED.md')]
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'status':'SAVED_AND_REHASHED','files':[{'path':str(p.resolve()),'sha256':sha(p),'bytes':p.stat().st_size} for p in files],'schemas':'exact protocol fields checked','shared_sources':'pinned hashes unchanged','full_FEI':'OPEN','remote_publication':'not performed; supervisor mirrors finished run'}
dump(root/'out/PERSISTENCE.json',receipt)
for item in read(root/'out/PERSISTENCE.json')['files']:assert sha(Path(item['path']))==item['sha256']
print(json.dumps({'status':'SAVED_AND_REHASHED','hashed_files':len(files),'claim_records':len(claims),'new_claim_statement_sha256':claim['statement_sha256'],'exact_assertions':main['exact_assertions']+ind['exact_assertions'],'full_FEI':'OPEN'}))
