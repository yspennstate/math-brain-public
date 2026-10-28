from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
def write(name,s):
    (R/name).write_text(s,encoding='utf-8',newline='')
def js(name,obj):write(name,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def digest(b):return hashlib.sha256(b).hexdigest()
main=json.loads((R/'out/EXACT_RESULTS.json').read_text(encoding='utf-8'))
audit=json.loads((R/'out/AUDIT_RESULTS.json').read_text(encoding='utf-8'))
assert main['status']==audit['status']=='PASS'
checks=main['checks']+audit['checks']
statement=('For actual balanced Boolean f_k=(1-A_k)z+A_k y b_m with k>=2 and m=2(2^k-k), '
'I=2, Var=1, H<=4. For normalized positive-support power references R_q=P^q/Z_q and '
'arbitrary q_k in [0,1], sup_k CE(P_k,R_qk)<infinity iff sup_k[(1-q_k)2^(k+1)-k]<infinity. '
'Thus exponent selection from only mean/variance/influence fails when its value at (0,1,2) is <1. '
'The disjoint fresh selector has I=5/2, two full balanced I=2 children, and SAME-q inherited '
'CEroot=2+average CEchildren. A three-stratum normalized original reference instead costs <=7/2 '
'on f_k and <=11/2 on the selector. This does not disprove FEI or provide arbitrary-core sources.')
hyp=['Uniform independent physical coordinates; sign-valued Boolean functions.',
'b_m is the explicit disjoint quadratic bent function; y,z and k guard bits are separate.',
'All information in bits; positive-support power reference, q in [0,1]; q is held fixed during the selector query.',
'The exponent policy may use mean, variance and total influence only for the stated policy obstruction.',
'Both entire terminal cross-entropies are retained; no inherited reference is replaced for free.']
claim={'claim_id':'A056-FIXED-INFLUENCE-POWER-SOURCE-OBSTRUCTION','version':1,
'exact_statement':statement,'hypotheses':hyp,
'statement_sha256':digest(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()),
'contributors':['A056'],'proof_source':['DERIVATION.md sections 1-6','code/certify.py','code/audit.py'],
'proof_dependencies':[],'review_records':[{'reviewer':'A056','kind':'author adversarial reconstruction with independent direct Walsh arithmetic','status':'PASS; not independent external review'}],
'status':'AUTHOR_PROOF_SCOPED_OBSTRUCTION; EXACT_FINITE_CERTIFICATES; INDEPENDENT_REVIEW_PENDING',
'supersedes':[],'refutes':['CE(P,P^q/Z_q)<=K I universally for any fixed q<1, or exponent selected only from mean/variance/influence with value <1 at the exhibited invariants'],
'first_unproved_line':'An influence-priced ORIGINAL structural mixture/reference for every Boolean function, with its complete mixture normalizer and full terminal costs.',
'next_consumers':['A091','A090','A006','A015','A058','A059','A094','B20']}
js('CLAIMS.json',[claim])
next_action=('Test a structural ORIGINAL whole-set mixture beyond scalar power priors: prove its complete mixing normalizer is paid by unused original influence. '
'A091/A090 reconstruct the fixed-I threshold and both physical inherited children; do not reprice v9 transport.')
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B12','packet_id':'A056',
'gap_id':'FEI-B12-INITIAL-ORIGINAL-SPECTRUM-SOURCE','attempt_id':'A056-stage22-fixed-influence-original-power-source-test',
'method':'Actual balanced rare bent activation, exact constant-influence tuning, complete power normalizer, two-full-child physical selector, contrasting three-stratum original reference',
'mathematical_delta':'Fixed I=2 and mean=0 obstruction to power sources chosen only from scalar invariants; sharp variable-exponent threshold sup((1-q)2^(k+1)-k)<infinity; explicit original macro source<=7/2; full physical selector SAME-source ledger retained.',
'deliverable_status':'COMPLETE_LOCAL; source-bound review handoff; supervisor mirror unobserved',
'mathematical_status':'AUTHOR_PROOF_SCOPED_SOURCE_OBSTRUCTION_AND_EXACT_CERTIFICATES; UNIVERSAL_INITIAL_SOURCE_OPEN; FULL_FEI_OPEN; LEAN_NOT_RUN_MEMORY_ADMISSION_FAILED',
'claim_versions_used':[{'claim_id':'A056-TWO-BRANCH-COMMON-CONTROL-TRANSPORT','version':9,'role':'retained conditional context only; no load-bearing dependency in new source proof'}],
'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
'source_artifacts':['REPORT.md','DERIVATION.md','CLAIMS.json','FROZEN_SPEC.json','FROZEN_AUDIT.json','code/certify.py','code/audit.py','code/SourceThreshold.lean','code/finalize.py','out/EXACT_RESULTS.json','out/AUDIT_RESULTS.json','out/RESOURCE_AND_OPERATIONS.json','out/SOURCE_RECEIPTS.json','out/PERSISTENCE.json'],
'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
'blockers':['Full FEI and universal original source unpaid.','Independent external reconstruction pending.','Lean admission refused: physical free2.7GB<4; commit free3.1GB<8. No retry or heavy job.','Checklist working update failed with checklist lock held too long.'],'packet_ids':['A056']}
js('PROGRESS.json',progress);write('PACKET_DELTA.json',(R/'PROGRESS.json').read_text(encoding='utf-8'))
js('out/RESOURCE_AND_OPERATIONS.json',{'small_jobs_memory_estimate_MB':80,'main_seconds':main['seconds'],'audit_seconds':audit['seconds'],
'lean':'NOT RUN: memok printed WAIT physical2.7GB need4, commit3.1GB need8; Lean source is uncompiled and unverified.',
'checklist_working':'FAILED: RuntimeError checklist lock held too long; no lock broken.',
'wake':'WARN required owner-model/state/dream sources stale; owner informed before mathematical use.',
'processes':'No workers launched, no process stopped, no background mathematical computation.',
'source_encoding':'Bundled PDF-to-text files are cp1252, not UTF8; initial strict UTF8 read rejected, then explicitly decoded cp1252 without altering originals.'})
report=f'''# exact target, quantifiers, hypotheses and units

Test ORIGINAL source funding for every k>=2 on an actual balanced Boolean family with I=2. All costs are true-law cross-entropy in bits. Specify exactly when normalized power references fail, including adaptive exponents chosen only from scalar invariants, and retain both full children at a physical selector. Full FEI remains OPEN. This extends the known fixed-Renyi obstruction with fixed invariants and a sharp variable-exponent threshold; it is not advertised as a new generic Renyi no-go.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json, revision2026-10-11-execution-v2, read in full; current BOARD.md intake with B12 and A011/A090/A091/A094 lines; B12 STREAM_NOTES.md v2 (2026-10-11); own STATUS/LEARNED and prior stage21 REPORT/PROGRESS. Current targeted intake also covers README/CURRENT_STATUS, registry and packet B12 entries, campaign plan A056/C020/C024/convolution paragraphs, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING sections. Bundled 38pp threshold paper Proposition7.1 and8.9 and corresponding earlier abstract, plus both percolation-version composition references were inspected. The bundled text is cp1252, explicitly decoded after strict UTF8 rejected. Earlier complete baseline intake belongs to previous stages, not a fresh whole-library audit. One math-brain multiwording search supplied no dependency or proof of this refinement. The proof here is self-contained; source hashes and scopes appear in out/SOURCE_RECEIPTS.json.

# complete derivation or exact first unsupported line

DERIVATION.md sections1-6 gives the complete analytic author proof. Equation1 freezes I=2 and balance; equation2 bounds H<=4. Equations3-6 prove bounded original power-source cost iff sup[(1-q_k)2^(k+1)-k] is finite. Thus no exponent selected only from mean/variance/influence works if it is strictly below one at the exhibited invariants. Equations7-8 preserve both FULL physical children at Iroot=5/2 and exactly transported SAME-q references. Equation9 gives the constructive three-stratum original reference CE<=7/2, or <=11/2 at the selector root. This is a falsification and repair of a source proposal, not a universal positive supplier. The first unpaid universal line is constructing an ORIGINAL structural mixture/reference for arbitrary Boolean f with its whole mixing normalizer paid by unused O(I). Existing v9 transport remains conditional and unchanged.

# executed validation with domain, arithmetic, commands and outputs

PASS: {checks} exact checks ({main['checks']} main + {audit['checks']} separate representation audit). Main code performs complete 256-row Boolean truth-table/FWHT/edge-influence verification at k=2,m=4,n=8, checks all256 signed-convolution shifts, and explicitly forms272 nonzero selector Fourier amplitudes on17 inputs. Both actual selector children are balanced I=2; root I=5/2. Compressed exact rational tests cover19 k values2..20, five rational exponent controls, and209 remaining-guard cases. The second implementation uses a direct256x256 Walsh matrix, exact physical pair kernels for q=1/2 and macro references, and the integer inequality product(1/Q)^(256P)<=2^896. It does not import the first checker. These are distinct author implementations, not external independent review. Timings: {main['seconds']:.3f}s and {audit['seconds']:.3f}s inside Python. Frozen specifications precede each job; estimated80MB each, no dimension escalation or heavy job. Commands: `python -X utf8 code/certify.py`, `python -X utf8 code/audit.py`. No numerical logarithm sign is used. Lean algebraic source is saved, but NOT RUN: required memok admission returned WAIT (physical2.7GB<4; commit3.1GB<8). No Lean-checked theorem is claimed. Rung: analytic author proof plus exact finite certificates; external review pending.

# proof dependencies and changed downstream conclusions

New source obstruction is self-contained. It uses actual Boolean functions satisfying all signed convolution equations, so full Booleanity alone does not license this specific power normalization estimate. The already known fixed-q Renyi failure is retained as baseline. The new fixed-invariant policy test and exact q_k threshold narrow what an original supplier must use. The explicit structural source shows FEI is not contradicted. No balanced-composition or v9 history-transfer theorem is reopened; no original owner bank, old debit, full terminal, or reset charge is discarded. This scoped source audit is not a new broad positive candidate added around the stream review cap.

# one next mathematical action and independent reviewer

{next_action} A091 is the proposed independent reviewer, A090 alternate. Review requests here are source-bound handoffs for the supervisor, not messages sent or acceptance claimed.

# actual persistence receipts or precise save blocker

Required REPORT/CLAIMS/PROGRESS/PACKET_DELTA, proof, frozen specs, scripts, exact results and rolling files are saved within A056. out/PERSISTENCE.json hashes every run artifact except itself and checks protocol fields and byte-identical progress compatibility. Nothing was written in campaign source trees or another agent folder. No git, mail, trading access, new worker, detached process or brain write was performed. Required developer checklist working attempt hit a shared lock; no lock was broken. Supervisor mirroring and independent acceptance are unobserved. Brain wake flagged stale owner-model/state/dream context and the owner was informed. Initial and later resource snapshots differ; admission uses the later memok result, not the earlier permissive snapshot.

# Universal bridge

C020 whole-set source cost, feeding C024 history transfer and C019 stopping-tree payment: this stage removes a specific original-source proposal even at EXACT fixed balance and influence, with both full physical terminal costs retained, and proves the precise exponent threshold required to evade the obstruction. An explicit three-stratum source pays this actual family from original O(I), explaining why the source proposal fails without implying an FEI counterexample. The unpaid universal bridge is a structurally selected whole-set mixture whose complete original normalization cost is O(I); v9 already handles conditional transport and does not supply that source. NEXT tests that original structural supplier because repeating transport identities or increasing finite dimensions cannot pay the missing universal invoice.
'''
write('REPORT.md',report)
# Read-only source receipt: hash current observed bytes, distinguish excerpts from full intake.
sources=[]
paths=[Path(r'math-open-problems/reports\fei-2026-10-11')/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
B=A.parents[1]
paths += [B/'BOARD.md',B/'claude/B12/STREAM_NOTES.md']
paths += list((B/'context').glob('*.txt'))
S=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
paths += [S/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
for p in paths:
    raw=p.read_bytes();sources.append({'path':str(p),'bytes':len(raw),'sha256':digest(raw),'scope':'full protocol' if p.name=='EXECUTION_PROTOCOL.json' else 'targeted current excerpts; previous complete intake not repeated'})
js('out/SOURCE_RECEIPTS.json',sources)
state=f'STATE: Stage22 fixed-I=2 balanced power-source obstruction proved; sharp adaptive-q threshold; macro source<=7/2; {checks} exact main/audit checks PASS; independent review pending; full FEI OPEN.\nNEXT: Price ORIGINAL structural whole-set mixing normalizer beyond scalar power priors; retain v9 transport and both full terminals; A091/A090 review fixed-invariant threshold/source audit.\n'
(A/'STATUS.md').write_text(state,encoding='utf-8',newline='')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n2026-10-27 stage22 {R.name}: tuned rare balanced bent activation to EXACT I=2; power-source cost bounded iff sup((1-q)2^(k+1)-k)<infinity. Both physical selector children and SAME inherited refs retained. Explicit macro source<=7/2. {checks} exact checks PASS; Lean NOT RUN after memok WAIT; checklist working failed lock. Universal source/full FEI OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\n2026-10-27 stage22: f=(1-A_k)z+A_k y bent_m, m=2(2^k-k), is balanced essential with I=2, H=eta((1-delta)^2)+2+2kdelta(1-delta)<=4. For q in[0,1], power reference has log-normalizer high term E=(1-q)2^(k+1)-k; uniformly bounded CE iff sup E finite. Hence ANY scalar-invariant-only exponent policy below1 at (mean0,Var1,I2) fails; q=1 is actual-spectrum/FEI-equivalent. A fresh selector of two disjoint copies has I5/2 and exact SAME-q CEroot=2+avg FULL childCE; inherited children require no reset. Three-stratum prior masses1/2,1/4,1/4 has CE<=7/2; root<=11/2. This isolates global power normalization, not FEI. A structural original mixture must retain its complete normalizer; never infer child source renewal from a root CE bound.\n')
protocol=json.loads(paths[0].read_text(encoding='utf-8'))
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        raw=p.read_bytes();assert len(raw)<20_000_000
        manifest.append({'path':p.relative_to(R).as_posix(),'bytes':len(raw),'sha256':digest(raw)})
js('out/PERSISTENCE.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'files':manifest,'protocol_fields':'PASS','progress_compatibility_bytes':'IDENTICAL','review':'pending','remote_mirror':'unobserved'})
print(json.dumps({'status':'SAVED','exact_checks':checks,'files':len(manifest),'run':str(R),'schema':'PASS'}))
