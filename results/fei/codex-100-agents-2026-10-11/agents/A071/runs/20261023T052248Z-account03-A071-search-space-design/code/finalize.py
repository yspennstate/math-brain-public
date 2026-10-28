from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];AG=R.parents[1];BASE=AG.parents[1]
SRC=AG.parent/'A075'/'runs'/'20261023T043917Z-account03-A075-search-to-theorem-bridge'
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(s,h):return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
stamp=datetime.now(timezone.utc).isoformat();validation=read(R/'out/VALIDATION.json');review=read(R/'out/SOURCE_REVIEW.json')
audit=read(R/'out/AUDIT.json') if (R/'out/AUDIT.json').exists() else None
complete=audit is not None;assert not validation['admission_threshold'];assert review['states_reconstructed']==3456
statement='For uniform physical bits and base2 Fourier entropy, let g be six-bit negative on{0,1,2}, h negative on{0,1,2,4,8,16,32,6,17,40}, J(x)=-h(x xor1), Fplus=J(-1,+1,g,g,g,g), S=4I-H and A=-S(Fplus)>0. For every already supplied real net debit D>=0, incoming root credit A+D pays every adaptive physical reveal/stopping policy on ALL FOUR remaining cores, using the exact stopping-hull allocator a_b=rho_M(child_b)+a-mean rho_M(children) for each currently admitted subset M. A first core may be chosen at the root and each later core may be chosen after observations; every admission retains the credit ACTUALLY allocated by all preceding one-, two- and three-core phases. The full hull has root rho_all4=A exactly. All8784 labelled admission cuts, including6912 fourth-core cuts, have sharp extra initial-credit threshold0. Every old signed debit and nonnegative credit-owner label is conserved in conditional mean; all other complete stopped terminals and the original donor spending remain fixed; no new outside flow is drawn. This closes this fixed24-bit retained-terminal restriction domain, with all-real supplied-debit parameter, and asserts neither arbitrary past allocators nor an all-dimensional Boolean theorem.'
hyp=['specified actual disjoint six-bit inner cores and literal outer gate, uniform physical bits, entropy in bits, rate4',
'A+D is already supplied by the retained original donor account; original spending, stopped terminals and owner labels remain unchanged',
'each admitted subset uses its exact finite stopping-hull allocator; incoming credit is not reset when another core is admitted',
'incoming nonnegative credit-owner labels sum to supplied credit; signed old debit labels sum to the nonnegative actual total debit',
'only the four remaining fixed cores are queried; dummy queries may be inserted with identical children and unchanged account']
own={'claim_id':'A071-SAME-CREDIT-FOUR-CORE-CONTINUATION','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(statement,hyp),'contributors':['A071'],
'proof_source':['PROOF.md','code/fourth.py','code/audit.py','out/ADMISSION_RESULT.json','out/VALIDATION.json','out/FULL_*.json','out/CUTS_MASK_*.json']+(['out/AUDIT.json'] if complete else []),
'proof_dependencies':['A075-SAME-CREDIT-THREE-CORE-CONTINUATION@1 independently reconstructed unchanged in out/SOURCE_REVIEW.json','character orthogonality, finite Shannon chain rule and finite Bellman induction reconstructed in PROOF.md','A084/A075 prime-log utilities and A071 directed-log primitive copied with SOURCE_PINS attribution'],
'review_records':[{'reviewer':'A071','independent_reviewer':False,'verdict':'AUTHOR_PRIMARY_CERTIFICATE_AND_REVERSE_PREDECESSOR_AUDIT_PASS' if complete else 'AUTHOR_PRIMARY_CERTIFICATE_PASS_SECOND_AUDIT_RUNNING','scope':'fixed24-bit Boolean family; all mask admissions under specified original exact-hull allocator; external acceptance pending'}],
'status':'AUTHOR_EXACT_FINITE_CERTIFICATE_REVIEW_PENDING' if complete else 'AUTHOR_CERTIFICATE_SECOND_AUDIT_PENDING','supersedes':[],'refutes':[],
'first_unproved_line':'Construct a dimension-independent signed-component superharmonic envelope with initial credit funded from influence for arbitrary Boolean outer spectra and restrictions. The starting bank here is already subsidized.',
'next_consumers':['A072','A074','A075','A080','A084','A089','A092','B15','B20']}
peer=read(SRC/'CLAIMS.json')[0]
assert peer['statement_sha256']==digest(peer['exact_statement'],peer['hypotheses'])
peer['proof_source']=[str(SRC/'PROOF.md'),str(SRC/'REPORT.md'),'out/SOURCE_REVIEW.json','PROOF.md']
peer['review_records']=peer['review_records']+[{'reviewer':'A071','independent_reviewer':True,'verdict':'HOLDS_UNCHANGED_SCOPE','scope':'all3456 triple S/rho state instances and864 actual original one-then-two phase paths; finite Bellman and affine supplied-credit proof reconstructed','method':'new direct Walsh-subset spectra, own named-profile Bellman and original physical-coordinate replay; logarithm primitive shared and attributed','evidence':'out/SOURCE_REVIEW.json'}]
peer['status']='INDEPENDENTLY_RECONSTRUCTED_UNCHANGED_SCOPE'
save(R/'CLAIMS.json',[own,peer])
next_action='A074/A092 independently reconstruct the full6084-orbit/8784-cut certificate. A072/A075/A089 extract a signed-component superharmonic envelope paid from influence, preserving actual owner-labelled credit across arbitrary-core admission; all four cores of this retained Fplus domain are now closed, so do not repeat that finite search or increase dimension by default.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B15','packet_id':'A071','gap_id':'B15-ARBITRARY-CORE-BIASED-ADMISSION','attempt_id':'A071-stage19-fourth-core-actual-credit','method':'New direct Walsh-subset spectra; complete product restriction DAG; all sequential admission minima; independent source reconstruction; reverse-predecessor and physical-path author audit.',
'mathematical_delta':'Zero extra credit for every admission of all FOUR remaining cores under actual exact-hull allocations;6084 full profile orbits,8784 admission cuts; source three-core claim accepted unchanged.',
'deliverable_status':'COMPLETE_LOCAL; external review and supervisor adoption pending' if complete else 'PRIMARY_AND_SOURCE_REVIEW_SAVED; second audit running',
'mathematical_status':'FINITE_FULL_RETAINED_DOMAIN_CLOSED; SOURCE_ACCEPTED_UNCHANGED; FULL_FEI_OPEN',
'claim_versions_used':['A075-SAME-CREDIT-THREE-CORE-CONTINUATION@1 '+peer['statement_sha256']],
'claims_created_or_changed':[own['claim_id']+'@1',peer['claim_id']+'@1 independent acceptance unchanged'],
'source_artifacts':['FROZEN_SPEC.json','AUDIT_SPEC.json','AUDIT_V2_SPEC.json','PROOF.md','out/SOURCE_PINS.json','out/SOURCE_REVIEW.json','out/VALIDATION.json','out/ADMISSION_RESULT.json','out/FULL_*.json','out/CUTS_MASK_*.json']+(['out/AUDIT.json'] if complete else []),
'next_consumers':own['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
'blockers':['Universal influence-funded initial envelope remains unproved.','External acceptance and supervisor GitHub/brain mirroring unverified.']+([] if complete else ['Second author audit remains running.']),
'packet_ids':['A071']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
audittext=(f"The second implementation passed {audit['actual_admission_cuts']} reverse-predecessor cut checks, {audit['path_steps']} unique saved-path steps and {audit['financial_rows']} financial rows, with {audit['checks']} predicates in {audit['seconds']:.3f}s. Its deliberately altered live root and carried-credit positive controls were rejected." if complete else 'The second implementation is still running; no completed second-audit receipt is asserted.')
report=f'''# A071 stage19: all four remaining cores paid from the actual bank

## exact target, quantifiers, hypotheses and units

Full FEI is OPEN. In the actual retained Fplus=J(-1,+1,g,g,g,g), with the specified six-bit Boolean cores, entropy bits and S=4I-H, the SAME already supplied A=-S(Fplus) pays every adaptive reveal/stopping policy on all FOUR remaining cores. Each phase uses its exact stopping-hull allocator. Core admissions may depend on previous observations and preserve actual carried credit, all old labels and the already spent original donor. Every real already supplied old debit D>=0 is covered by incoming A+D. Arbitrary alternative past allocators are outside scope. The bounded family is complete for all20736 labelled product restrictions on these24 fixed bits.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2, BOARD at stage intake05:15UTC with header refreshed05:35, unchanged B15 lead v2, own stage18 STATUS/PROGRESS/helpers, A075 latest043917 REPORT, PROOF sections1-6, CLAIMS and third_core/profile_engine/bank_audit/finalize code; source certificate triples and stronger phase cuts consumed in the review. Earlier campaign/registry and paper intake is reused background; no new literature premise is claimed. SOURCE_PINS records copied source helpers and source report/proof/claim hashes. Critical spectra are newly reconstructed by direct Walsh-subset expansion. Brain self-care is degraded/unverified: stale owner-model and state-of-mind sources affect personal-context reliability; they are unused as mathematical premises.

## complete derivation or exact first unsupported line

PROOF gives occupied-mask Shannon/influence identities, exact least-superharmonic stopping hull, affine child credit allocation, zero-credit/debit owner-label cases and actual-history admission minima. The full four-core root hull equals A exactly. Every8784 labelled admission cut has exact extra-credit threshold0, including6912 actual three-core->four-core cuts. The primary propagates actual minima forward; the second checker uses all reverse predecessors. Adding supplied D shifts every descendant arrival by D, so the all-real statement is algebraic, not a numerical grid. No history is reassigned to a fresh optimum. The first unsupported universal line is an arbitrary-dimensional signed-component envelope whose INITIAL credit is paid from influence. The finite starting terminal here is already subsidized; its closure does not supply a universal bank.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC precedes pilot/search. All729 physical inner restrictions and1458 query rows establish the twelve-profile reduction. Literal block swaps checked on16 outer inputs reduce20736 full profiles to6084 spectrum orbits and all15 admitted masks to8280 hull orbits. Pilot144 spectra agree with the separate centered engine, completing in8.238s. Primary passes74227 predicates and8784 cuts in{validation['seconds']:.3f}s, private peak{validation['private_peak_bytes']}bytes. All decisions use Fraction prime-log forms, exact cancellation and directed192-bit logarithm intervals with proved remainder. No float sign, automatic dimension increase, GPU, detached job or job estimated above300MB was used.

Independent source reconstruction passes3456 triple state instances and864 original physical-prefix paths in{review['seconds']:.3f}s with{review['checks']} checks. {audittext}

The first pilot failed only at a Windows process-handle type in the resource monitor; explicit64-bit typing repaired it and the full pilot rerun passed. FIRST_FAILURE preserves the error. First author audit exceeded its300s checkpoint budget without reporting a mathematical mismatch; AUDIT_V1_FAILURE preserves this limitation. AUDIT_V2_SPEC freezes the unchanged domain with shared-prefix memoization, a1200s bound and periodic280MB/time stops. No other workload was killed or throttled. Shared compute read status was ok with approximately2.8GB available RAM and high aggregate CPU; last intake disk free was approximately9.1GB, so outputs stay small. Commands relative to run: python -B -X utf8 code/setup.py; code/fourth.py --pilot; code/fourth.py; code/fourth.py --review; code/audit.py; code/finalize.py. No Lean run is asserted.

## proof dependencies and changed downstream conclusions

A075-SAME-CREDIT-THREE-CORE-CONTINUATION@1 receives independent acceptance unchanged: statement and canonical statement+hypotheses digest retained; critical spectrum representation, Bellman and physical history replay are independently implemented. Shared bounded-log arithmetic is attributed, not presented as a new independent primitive. New A071-SAME-CREDIT-FOUR-CORE-CONTINUATION@1 closes the fourth-core frontier for this exact allocator and complete retained domain. Its external acceptance remains pending. Earlier negative-full-terminal obstructions and the need for nonflat actual credit remain valid; no blanket full-child positivity or arbitrary sufficient past allocator is inferred.

## one next mathematical action and independent reviewer

{next_action} This is the universal C019/C024 history-transfer obstruction to attack next, rather than a new isolated finite-family census.

## actual persistence receipts or precise save blocker

All four required protocol files, PROOF, frozen specs, code and exact bounded outputs are saved inside A071 only. PERSISTENCE records protocol field checks, canonical hashes, progress/delta identity, file sizes/hashes and rolling-file hashes. No file exceeds20MB. STATUS has exactly two lines; WORKLOG and LEARNED are dated. New external review and supervisor GitHub/brain mirroring remain unverified. Shared checklist entries including T-20261023-230 remain unmodified under the user's explicit A071-only write rule; no shared index, brain, checklist, other-agent folder, message or git was written. {'No certificate job remains running.' if complete else 'The second author audit is still running; this is a provisional saved report.'}

## Universal bridge

This stage moves C019 stopping-tree payment and C024 history transfer from three to ALL FOUR remaining cores at unchanged rate4 and ZERO extra outside credit:6084 full spectrum orbits,8280 hull orbits and8784 exact labelled admission cuts include6912 fourth-core cuts at the actual diminished bank. It independently accepts the A0753456-state/864-path source. This closes the entire fixed retained Fplus restriction domain, while full FEI stays OPEN. What remains is a dimension-independent signed-component superharmonic envelope funded from influence at its initial account. NEXT extracts and challenges that envelope under owner-preserving arbitrary-core admission, because repeating this now-complete finite domain cannot close the universal initial-payment gap.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
state='all8784 reverse cuts and financial paths audited' if complete else 'second author audit running'
(AG/'STATUS.md').write_text('STATE: A071 stage19: SAME credit pays ALL FOUR remaining cores;6084 spectra/8280 hull orbits/8784 admissions;A075 source accepted3456states/864paths;'+state+';FEI OPEN, external review pending.\nNEXT: A074/A092 independently review four-core certificate;A072/A075/A089 derive a dimension-independent influence-paid signed envelope preserving actual owner-labelled credit;do not repeat this closed domain.\n',encoding='utf-8')
marker=R.name+(' FINAL' if complete else ' PRIMARY')
for name,text in [('WORKLOG.md',f'{stamp} {marker}: new Walsh-subset spectra close all four retained cores with same credit;8784 admission cuts zero; A0753456states/864paths accepted; {state}. Pilot resource-monitor type fixed; first audit300s budget exceeded, unchanged-domain1200s/memoized rerun frozen. Full FEI open.'),('LEARNED.md',f'{stamp} {marker}: For fixed Fplus=J(-1,+1,g6^4), g6 negative{{0,1,2}}, the exact all-four stopping hull equals original A=-S(Fplus); the actual single->pair->triple->all-four exact-hull account requires zero additional outside credit at all8784 labelled cuts. Twelve literal profiles/core and two block swaps give6084 complete full orbits. Continuum parameter is already supplied debit D>=0, not dimension. Source A075 three-core theorem independently reproduced unchanged. Universal influence-funded initial envelope remains unpaid.')]:
    p=AG/name;existing=p.read_text(encoding='utf-8') if p.exists() else ''
    if marker not in existing:
        with p.open('a',encoding='utf-8',newline='') as f:f.write('\n'+text+'\n')
fields=read(PROTO)['required_per_run']
expected_progress={x.split(' (')[0] for x in fields['progress_fields']}
assert set(progress)==expected_progress
for c in [own,peer]:assert set(c)==set(fields['claim_fields']) and c['statement_sha256']==digest(c['exact_statement'],c['hypotheses'])
for heading in fields['report_fields']:assert '## '+heading in report
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((AG/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipt={'saved_at':stamp,'protocol_fields':'PASS','canonical_statement_and_hypotheses_hashes':'PASS','progress_delta_identity':'PASS','files':[],'rolling_files':[],'external_review':'PENDING','remote_mirror':'UNVERIFIED','certificate_job_state':'NONE' if complete else 'AUDIT_RUNNING','full_fei':'OPEN'}
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        assert p.stat().st_size<20*1024**2
        receipt['files'].append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for n in ['STATUS.md','WORKLOG.md','LEARNED.md']:receipt['rolling_files'].append({'path':str(AG/n),'sha256':sha(AG/n)})
save(R/'out/PERSISTENCE.json',receipt)
print(json.dumps({'run':R.name,'files':len(receipt['files']),'schema':'PASS','four_core_threshold':'0','source_acceptance':'UNCHANGED','second_audit':'PASS' if complete else 'RUNNING','new_claim_hash':own['statement_sha256'],'full_fei':'OPEN'}))
