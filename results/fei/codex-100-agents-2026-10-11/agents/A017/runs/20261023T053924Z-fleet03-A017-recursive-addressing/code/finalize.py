"""Save protocol records, exact evidence receipts and rolling handoff."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R.parent.parent
PREV=A/'runs/20261023T012331Z-fleet03-A017-recursive-addressing'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_bytes((json.dumps(v,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
proto=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
main=read(R/'out/certificate.json');ind=read(R/'out/independent_certificate.json');bad=read(R/'out/bad_intermediate_query.json')
assert main['status']==ind['status']==bad['status']=='PASS'
assert main['parents']==2432 and main['adaptive_prefix_rows']==533248 and main['assertions']==1136256
assert ind['parents']==273 and ind['activation_identities']==16
for code,spec in [('verify.py','spec.json'),('verify.py','witness_spec.json'),('independent.py','independent_spec.json')]:
    assert sha(R/'code'/code)==read(R/'out'/spec)['helper_sha256']
sources=[Path('BOARD.md'),
 Path('claude/B04/STREAM_NOTES.md'),
 Path('claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt/CLAIMS.json'),
 PREV/'PROOF.md',PREV/'CLAIMS.json',A/'runs/20261021T213328Z-fleet03-A017-recursive-addressing/out/boolean_counterexample.json']
save(R/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
(R/'INHERITED_STAGE18_PROOF.md').write_bytes((PREV/'PROOF.md').read_bytes())
(R/'out/inherited_stage18_claims.json').write_bytes((PREV/'CLAIMS.json').read_bytes())
(R/'out/inherited_block_baseline_claims.json').write_bytes(sources[2].read_bytes())
consumers=['A018','A020','A024','A030','A090','A091','B04','C019']
statement=('The prior all-dimensional twelve coherent same-fiber edit theorem remains at K=4+2/ln(2). '
 'For any quadratic q on n uniform original physical bits with polar matrix Q, Q_i nonzero, '
 'P={partial_i q=1}, g=(-1)^q*(1-2*1_E), and |E intersect P^c|<=2^n/32, let J exclude i '
 'and satisfy Q_ij=0 and Q_j not in span_F2(Q_i) for each j in J. There is NO pairwise '
 'noninteraction hypothesis. With I_J=sum_j Inf_j(g), H(g)-average_a H(g|J=a)<=K I_J and '
 'I(g)=I_J+average_a I(g|J=a). For every adaptive prefix T querying only unused J coordinates, '
 'retain all full conditional leaves, let D_T be its actual weighted entropy debit, R_T its '
 'full remaining-J completion debit and A_T its actual weighted queried influence. Then '
 'D_T+R_T=H(g)-average_a H(g|J=a), A_T+sum_v w_v I_Jv(g_v)=I_J, and '
 'K I_J-D_T-R_T>=0, with the same original I_J account. Neither local K4 goodness in '
 'descendants nor D_T<=K A_T is asserted. An exact tagged ten-bit parent has a reached '
 'physical query with B_k>4 Inf_k despite the paid whole block. Arbitrary tagged half-cube '
 'leaves A_h have H(A_h)=2+H(h)/2 and I(A_h)=1+I(h)/2; uniformly paying all such leaves '
 'at a dimension-independent rate would imply full FEI by tensor amplification.')
deps=[{'claim_id':'A017-FOUR-EDGE-COMPATIBILITY','version':2,
 'status':'AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW','used_for':'Unchanged twelve-edit theorem and previous tangent context; new block extension proved in PROOF.md.'},
 {'claim_id':'B04-SEL-LOG-SHARP','version':1,'status':'PROVED_AUTHOR_INDEPENDENT_REVIEW_PENDING;M_BOUND_PARTIALLY_RECONSTRUCTED_BY_A018',
 'used_for':'Established uniform physical selector block split and M_J<=2 I_J/ln(2). No new generic multiplexer bound claimed.'}]
claim=dict(claim_id='A017-FOUR-EDGE-COMPATIBILITY',version=3,exact_statement=statement,
 hypotheses=['Uniform physical cube, Boolean signs, base-two spectral entropy; Q alternating over F2.',
 'Inside edits arbitrary; outside edit density at most1/32 of the whole cube.',
 'Commit to one original physical J; each prefix queries only unused J coordinates and retains full completion leaves.',
 'Remaining committed J influence is reserved, never charged again as a full child FEI budget.',
 'External composition is conditional on supplied eligible blocks; arbitrary terminal payment and universal selection are unproved.'],
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A017'],
 proof_source=['PROOF.md','INHERITED_STAGE18_PROOF.md','out/inherited_block_baseline_claims.json','code/verify.py','code/independent.py','out/'],
 proof_dependencies=deps,review_records=[],status='AUTHOR_CHECKED_PROOF_AND_EXACT_CERTIFICATES_PENDING_REVIEW',
 supersedes=['A017-FOUR-EDGE-COMPATIBILITY@2'],refutes=[],first_unproved_line=None,next_consumers=consumers)
next_action=('Pay the first residual-core query or a reference change AFTER committed interacting J, '
 'using only original influence outside J; preserve both full leaves and every old debit. '
 'Rank-two inherited quadratics have no eligible independent tangent, so iteration of the old predicate is insufficient. '
 'Use the exact tagged-half identities to reject any free-terminal shortcut. A090/A091 review the account independently.')
progress=dict(protocol_revision=proto['revision'],run_id=R.name,stream='B04',packet_id='A017',
 gap_id='C019-LOCALIZED-BAD-NODE-BOUNDARY-OWNERSHIP',attempt_id='A017-stage19-interacting-committed-block-transfer',
 method='Apply established block entropy to physical tangent lower bounds; exact adaptive-prefix escrow telescope; actual tagged bad-child fixture and direct-character reproduction.',
 mathematical_delta='Removed pairwise noninteraction and allowed outside density<=1/32 at SAME K; all committed-block adaptive prefixes retain ONE original account. Exact bad intermediate K4 query shows why local heredity fails. Tagged arbitrary half-cube terminals are FEI-equivalent, not free.',
 deliverable_status='LOCAL_COMPLETE_REVIEW_AND_SUPERVISOR_TRANSFER_PENDING',
 mathematical_status='AUTHOR_CHECKED_RESTRICTED_HISTORY_TRANSFER;FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':d['claim_id'],'version':d['version']} for d in deps],
 claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':3}],
 source_artifacts=['REPORT.md','PROOF.md','CLAIMS.json','INHERITED_STAGE18_PROOF.md','code/','out/'],
 next_consumers=consumers,next_action=next_action,stagnant_substantive_attempts=0,
 blockers=['Independent proof review pending, including inherited dependencies.',
 'Universal useful-block selection and full retained-leaf entropy payment remain open.',
 'Supervisor adoption/remote mirror verification pending; no git or shared-tree writes performed.'],packet_ids=['A017'])
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in proto['required_per_run']['progress_fields']}
save(R/'CLAIMS.json',[claim]);save(R/'PROGRESS.json',progress)
(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
sections=[
'''At K=4+2/ln(2), extend the stage18 physical tangent-block payment to interacting original coordinates, with arbitrary inside edits and outside density at most1/32. All dimensions are quantified in PROOF.md sections1-3; finite tests are validation of a proved formula, not a finite-to-infinite inference. The previous twelve-edit theorem is inherited unchanged. Every prefix retains both full children and uses one committed original influence allocation; a full child FEI budget cannot spend the reserved part again. Full FEI remains OPEN.''',
'''Read at stage start: machine AGENTS.md, BOARD.md (including the current B04/A017-A020 entries), B04 STREAM_NOTES v2, own STATUS and stage18 PROOF; full execution protocol was re-read. The lead's B04-SEL-LOG-SHARP@1 exact claim was read and copied for its established selector split and M_J bound; these baseline inequalities are not claimed as new. The stage17 actual Boolean witness was read and hash-bound. Read-only math recall returned draft warnings about every-coordinate induction and retained budgets; none was promoted to a proof dependency. Source hashes are in out/source_receipts.json. Earlier threshold/percolation readings belong to previous stages; no new reading of the papers is claimed here. The current campaign deadline is the owner's 2026-10-23 14:49 UTC instruction.''',
'''PROOF.md gives the complete scoped derivation. Eligible original physical tangents satisfy Inf_j>=1/4-2 e_out/2^n regardless of interactions or inside edits. The established full-block identity bounds the erasure by sum_j h2(Inf_j), at most4 I_J when e_out<=2^n/32. This pays the whole J block at the unchanged K. Every adaptive J-prefix has exact entropy debit plus full completion debit equal to the SAME root block debit; its spent influence plus weighted remaining-J influence equals the SAME original I_J. The excess K I_J minus both debits is invariant through all such prefixes. This is a committed-block result, not a claim that every prefix is paid by its already queried influence alone.

The exact ten-bit parent in section4 is a useful falsifier: both root tangents are eligible, yet after j=0, B_k>4 Inf_k. Its original I_J=9/16 still funds the full block. The tag separates the bad six-bit phase from the vacuum and gives exact half-scaling of selected erasure and influence. Shared address-data labels remain fully retained with weighted influence ONE after the address is fixed; no level gets a new allowance for the same label.

First unpaid universal line: choose another useful block or pay every final leaf using only the unallocated physical influence. The precise obstruction is H(A_h)=2+H(h)/2, I(A_h)=1+I(h)/2 for arbitrary h. A uniform FEI bound for all these half-cube leaves already implies full FEI by tensor powers. Moreover, the inherited quadratic after the interacting block can have rank two, and every rank-two alternating matrix lacks eligible independent tangents: independent row coefficient pairs have determinant Q_ij=1. Thus merely iterating the old tangent predicate does not terminate on arbitrary retained cores. No terminal bound, paid reference change or universal selection is proved here.''',
f'''All frozen specs are under out/. The first pilot failed on a real verifier bug: unnormalized Walsh entropy requires 2n log(2), while v1 used n log(2). out/pilot_failure_v1.json and the original spec are retained; v2 corrected it before the successful pilot/full run. The corrected pilot passed28 parents,3072 prefix rows,6660 assertions in0.130 s.

The full specified domain consists of ALL256 inside-half masks at n4 with no outside edits, plus128 explicitly frozen n5 masks and ALL17 zero/single-outside-edit choices. It is2432 actual parents, not an exhaustive n5 Boolean census. Every adaptive J-prefix policy is included:9 per n4 parent,244 per n5 parent. The result is533248 prefix rows and1136256 exact assertions, PASS, runtime {main['elapsed_seconds']:.3f} s. Integer Walsh/prime-log coefficient vectors certify the entropy and influence telescopes exactly. Rational 48-term atanh-series bounds with explicit tail certify every tested sign; floating point appears only in runtime metadata. The actual ten-bit bad-child witness passed exact integer products and direct edge counts.

The separate reproduction uses direct XOR/popcount character sums, positive-integer erasure products and rational edge counts: ALL256 four-bit parents, the actual ten-bit parent/nine-bit child and16 tagged-activation identities,273 fixtures total; {ind['assertions']} assertions, PASS, runtime {ind['elapsed_seconds']:.3f} s. This is a distinct representation by A017, not independent-agent acceptance. Commands: python -X utf8 code/verify.py --freeze; --pilot; full without flags; --witness; code/independent.py --freeze; then no flags. Specs were frozen before each job. Estimated memory80/40 MB, no job over300 MB, no heavy admission needed; peak RAM not measured. No GPU, automatic dimension increase, detached process or Lean run.''',
'''A017-FOUR-EDGE-COMPATIBILITY@3 evolves the current pending candidate rather than opening another broad review candidate. Version2 supplies the unchanged twelve-edit theorem; B04-SEL-LOG-SHARP@1 supplies the established block identity/M_J bound with its recorded partial reconstruction. The new scope removes the pairwise Q_jk=0 condition from the WHOLE-BLOCK conclusion, not from the false descendant singleton assertion. Old five/six-control and twelve-edit certificates are not rerun or relabeled as new evidence. No earlier actual counterexample is withdrawn. External review of the new application and inherited chain remains pending.''',
next_action+''' This moves the unpaid terminal/selection issue directly; another fixed edit-count census would not resolve it. Handoff consumers are A018/A020/A024/A030 and A090/A091 through the saved run, without external messaging.''',
'''The four required protocol files, proof, code, frozen specs and certificates are saved under the specified A017 run directory, each below20 MB. PACKET_DELTA is byte-identical to PROGRESS and has packet_ids=["A017"]. out/PERSISTENCE_RECEIPTS.json binds every other run file and the rolling notes to bytes/SHA256; schema fields and source/helper hashes are checked. STATUS.md, WORKLOG.md and LEARNED.md carry the result and next unpaid step. Remote transfer remains the campaign supervisor's job and has no receipt here. Brain self-care is degraded/unverified (owner-model91.3h stale, state-of-mind75.9h stale); personalization based on them is unverified and neither was used as a mathematical premise. No work was stopped or left running.'''
]
report='# A017 stage19: interacting committed blocks and the retained-leaf barrier\n\n'
report+='\n\n'.join('## '+h+'\n\n'+s for h,s in zip(proto['required_per_run']['report_fields'],sections))
report+='''\n\n## Universal bridge

This stage moves C019 stopping-tree payment and C024 history transfer by removing pairwise polar noninteraction from the physical block payment at SAME K, allowing outside density<=1/32, and proving a nonrenewing original-account identity through every adaptive prefix of a committed block. An actual bad intermediate query confirms that local K4 heredity is unnecessary for this aggregate payment. What remains is useful-block selection and full retained-leaf payment from the original influence outside the committed block; the tagged-half identity shows why declaring those leaves free would assume full FEI. NEXT therefore targets the first such residual payment/selection rather than another isolated class census; the universal bridge remains open.
'''
(R/'REPORT.md').write_bytes(report.encode('utf-8'))
status=('STATE: A017 stage19 saved: interacting physical tangent blocks incl outside density<=1/32 paid SAME K; all533248 prefixes retain ONE account; actual bad child K4 verified; FEI OPEN, review pending.\n'
 'NEXT: Pay one residual-core query or reference change after committed J using ONLY unallocated original influence; rank2 has no eligible tangent and arbitrary tagged-half terminals are FEI-equivalent. A090/A091 review v3.\n')
(A/'STATUS.md').write_bytes(status.encode('utf-8'))
marker='2026-10-23 stage19 (20261023T053924Z)'
for name,note in [('WORKLOG.md','Removed pairwise noninteraction using established full-block entropy bound and original physical influence>=3/16; all committed adaptive prefixes retain exact SAME original account. Main2432 parents/533248 rows/1136256 assertions PASS; separate273 fixtures PASS. Saved actual10-bit bad intermediate K4 witness. Corrected pilot normalization bug, preserving v1 evidence. Proved tagged-half H=2+H(h)/2,I=1+I(h)/2 universal-terminal barrier. Independent review and full FEI remain open.'),
 ('LEARNED.md','A committed physical tangent block J can interact: if Q_i!=0, Q_ij=0,Q_j not in span(Q_i), and outside edit density<=1/32, established block entropy gives D_J<=K I_J, K=4+2/ln2. For every adaptive J-prefix, D_T+R_T=D_J and A_T+E I_remainingJ=I_J; K I_J-D_T-R_T stays fixed. This reserves the entire original J allocation once; it does NOT imply local descendant K4 or D_T<=K A_T. Exact tagged bad-child fixture disproves heredity. Arbitrary tagged-half terminals A_h have H=2+Hh/2,I=1+Ih/2; paying all of them implies FEI by tensor amplification. For raw Walsh entropy remember log(N^2)=2n log2, not n.')]:
    p=A/name;b=p.read_bytes() if p.exists() else b''
    if marker.encode('utf-8') not in b:p.write_bytes(b+('\n\n'+marker+': '+note+'\n').encode('utf-8'))
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json':continue
    assert p.stat().st_size<20*1024*1024
    if p.suffix=='.json':read(p)
    files.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='LOCAL_FILES_VALIDATED',claim='A017-FOUR-EDGE-COMPATIBILITY@3',
 full_fei='OPEN',review='PENDING',remote='SUPERVISOR_PENDING',files=files,
 rolling=[{'path':n,'sha256':sha(A/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]))
print(json.dumps({'status':'LOCAL_FILES_VALIDATED','run_files':len(files),'full_fei':'OPEN','independent_review':'PENDING'}))
