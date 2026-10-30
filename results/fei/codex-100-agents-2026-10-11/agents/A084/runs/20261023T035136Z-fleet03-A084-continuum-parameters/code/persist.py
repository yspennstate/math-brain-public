"""Persist the scoped theorem and exact protocol fields; no shared-tree writes."""
from pathlib import Path
import hashlib
import json

RUN=Path(__file__).resolve().parents[1]
BASE=RUN.parents[1]
PROTOCOL=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(PROTOCOL)
validation=read(RUN/'out/VALIDATION.json')
prefix=read(RUN/'out/PREFIX_VALIDATION.json')
scalar=read(RUN/'out/SCALAR_VALIDATION.json')
assert validation['exact_assertions']==56646
assert prefix['exact_assertions']==5572 and prefix['global_threshold_interval']==[0,0]
assert scalar['exact_assertions']==3820

source={'claim_id':'A072-OTHER-CORE-STOPPING-CREDIT-HULL','version':1,
 'statement_sha256':'3232af6b6b8937dc62c1e50b57a212def54049aec44fe6ad145148fa912feb10'}
statement=("Let h:{-1,1}^6->{-1,1} be negative exactly on the bit masks "
 "{0,1,2,4,8,16,32,6,17,40}, J(x)=-h(x xor 1), and g be negative exactly on "
 "{0,1,2} on six physical bits; bit 1 means sign -1. Retain the complete Boolean "
 "F_plus=J(-1,+1,g,g,g,g), S=4I-H with entropy in bits, and its supplied credit "
 "A0=-S(F_plus)>0. For any chosen pair of the four remaining disjoint physical "
 "cores, the exact conserved-credit hull over every allowed adaptive physical "
 "query and stopping policy within that pair has root R=A0. Further, after "
 "ANY prefix in one core using A072's original allocation a_b=R1(child_b)+a-mean R1, "
 "its actual incoming credit already dominates R2 at every cut, even when the "
 "second core is selected using the observed prefix. Thus all such two-core "
 "continuations require zero additional outside transfer for every real supplied "
 "initial old net debit D>=0 (incoming credit A0+D). All signed old debit labels, "
 "nonnegative credit-owner labels, other complete terminals and the outside donor "
 "books are preserved. On any finite restriction DAG the underlying account "
 "theorem holds for arbitrary nonnegative normalized real conditional weights, "
 "including zero-weight faces after removing unreachable outcomes: the exact "
 "all-policy requirement is R(v)=max(0,-S(v),max_query sum_b w_b R(child_b)). "
 "The physical Boolean application here uses only weights 1/2.")
hypotheses=[
 'The specified actual Boolean family and physical disjoint blocks; the other two whole cores remain present.',
 'Original credit is already supplied and booked at the source terminal; no unused donor is asserted or newly renewed.',
 'An optional initial prefix uses the actual source one-core allocation; after admission, only the chosen two cores may be queried.',
 'All incoming credit-owner labels are nonnegative; signed old debit labels have total S+a>=0; refunds may be signed.',
 'The general weighted-DAG statement assumes finite acyclic restriction states and fixed real S values; it makes no biased-influence identity claim.'
]
sh=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
claim={
 'claim_id':'A084-SAME-CREDIT-TWO-CORE-CONTINUATION','version':1,
 'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':sh,
 'contributors':['A084'],
 'proof_source':['PROOF.md','code/joint.py','code/prefix.py','code/arithmetic.py','out/JOINT_CASES.json','out/PREFIX_CUTS.json'],
 'proof_dependencies':[dict(source,acceptance='HOLDS_SUBSTATEMENT_INDEPENDENTLY_RECONSTRUCTED',scope='Single-core S/R profiles and the actual source allocation; all24 source profiles reproduced. This does not independently review every other source financial claim.')],
 'review_records':[],
 'status':'AUTHOR_PROOF_EXACT_FINITE_CERTIFICATE_INDEPENDENT_REVIEW_PENDING',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'None within the stated finite-family/analytic-account theorem. Universal extension: enabling a third physical core after credit already allocated jointly, and arbitrary-core admission, remain unpaid.',
 'next_consumers':['A072','A089','A074','A092','A075','B17','B20']
}
write(RUN/'CLAIMS.json',[claim])
next_action=('At an actual two-core allocated leaf, compute the third-core requirement and compare it with the credit actually present, retaining both complete other terminals and the spent donor books; A074/A092/A075 independently reconstruct this certificate first or in parallel.')
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B17','packet_id':'A084',
 'gap_id':'A084-INHERITED-PHYSICAL-CORE-PAYMENT','attempt_id':'stage7-same-credit-two-core-continuation',
 'method':'Independent exact Walsh/Taylor spectra; finite all-policy Bellman hull; inherited-prefix minimum-credit DAG; analytic real-credit and weight-boundary reduction.',
 'mathematical_delta':'Same original credit admits every adaptive query/stop policy in any two of four remaining actual cores, including all72 cuts of the actual A072 prefix allocation. Exact root R=A0 and extra threshold B=0 for all three pair orbits; all real D>=0. Third/arbitrary core payment open.',
 'deliverable_status':'COMPLETE_LOCAL',
 'mathematical_status':'SCOPED_PROOF_AND_EXACT_CERTIFICATE_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':[source],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':sh}],
 'source_artifacts':['PROOF.md','REPORT.md','FROZEN_SPEC.json','FINANCIAL_SPEC.json','SCALAR_SPEC.json','out/SOURCE_PINS.json','out/VALIDATION.json','out/PREFIX_VALIDATION.json','out/SCALAR_VALIDATION.json','out/LEAN_ATTEMPT.json','out/MANIFEST.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Third/fourth-core admission and a dimension-independent arbitrary-core estimate remain unproved.','Independent acceptance pending; Lean compile held by compute admission; supervisor mirror and brain ingestion unverified.'],
 'packet_ids':['A084']
}
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in required['progress_fields']}
write(RUN/'PROGRESS.json',progress)
write(RUN/'PACKET_DELTA.json',progress)

report=f'''# A084: same supplied credit for two-core continuation

## exact target, quantifiers, hypotheses and units

Retain the complete actual Boolean F_plus=J(-1,+1,g,g,g,g), rate4, entropy in bits, and S=4I-H. J=-h after flipping bit0, h is negative on masks{{0,1,2,4,8,16,32,6,17,40}}, and the six-bit core g is negative on{{0,1,2}} (bit1 means sign-1). The supplied original credit is A0=-S(F_plus)>0. For ANY pair of the remaining cores, EVERY adaptive query and stopping policy within that pair has exact minimum root credit A0. This remains true after ANY original one-core prefix with its ACTUAL source allocation and an answer-dependent choice of second core. All real already supplied old debits D>=0 are covered without new donor spending. This is a finite-family theorem; FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read this stage: BOARD.md, B17/STREAM_NOTES.md, own STATUS and recovered stage6 outputs; A072's 20261023T015130Z report, proof, exact hull code/data and claim A072-OTHER-CORE-STOPPING-CREDIT-HULL@1 (hash {source['statement_sha256']}); latest A071/A089/A075 reports as financial context. Source bytes are pinned in out/SOURCE_PINS.json. Full execution protocol revision {protocol['revision']} governs the schemas. Earlier campaign and paper intake is reused background; this theorem assumes no new literature assertion. The old lead AND direction was already closed in earlier A084 work; the productive new A072 dependency supplies this narrower C019 continuation target. Brain wake completed earlier in this session, but self-care remains degraded: stale personal model/state notes are not used as mathematical evidence.

## complete derivation or exact first unsupported line

PROOF.md gives finite Bellman induction, necessary and sufficient conserved credit, maximizing stopping-policy sharpness, complete occupied-spectrum composition with deterministic faces, and minimum actual-prefix credit propagation. The 12-state single-core restriction DAG is checked against all729 labelled restrictions and1458 query rows. Literal outer swaps yield three pair types. Each has144 states/840 query rows, with exact prime-log root equality R=A0; all72 source-prefix cuts have exact extra threshold B=0. Raising supplied initial credit by any real D>=0 shifts every descendant credit by exactly D. The account proof also covers all normalized nonnegative real branch weights; zero-weight outcomes are removed and zero-credit/debit kernels are treated explicitly. Physical applications use1/2 only. First unsupported universal step: control a third admitted core from credit actually allocated during a joint history, then arbitrary cores/dimension. No fresh donor payment or universal constant is claimed.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs: FROZEN_SPEC.json, FINANCIAL_SPEC.json, SCALAR_SPEC.json. From this run directory: python -B -X utf8 code/joint.py --pilot; python -B -X utf8 code/joint.py; python -B -X utf8 code/prefix.py; python -B -X utf8 code/scalar.py. See the exact helper argument conventions in the frozen spec and source. Pilot:21387 assertions,6.19125s. Full joint certificate:56646 assertions,11.83989s,432 state instances,2520 query rows,408 unique complete profiles. Source-prefix check:5572 assertions,1.56055s,24 independently reproduced source profiles and72 cuts. Scalar controls:3820 assertions over360 cases, including36 zero-credit and36 zero-total-debit cases. These three nonpilot runs total66038 assertions. Integer FWHT/direct characters, inverse/Parseval/edges, direct centered occupied masses, exact prime-log equalities and outward192-bit logarithmic sign bounds are checked. No floating signs decide the hull. Estimated memory120MB; no heavy search. The all-real proof is algebraic, not a grid inference. Lean helper admission returned checker exit2, SETUP_UNVERIFIED; no compiler process started. out/LEAN_ATTEMPT.json records it; no formal verification claimed.

## proof dependencies and changed downstream conclusions

Dependency: A072-OTHER-CORE-STOPPING-CREDIT-HULL@1, exactly pinned above. The one-core S/R substatement and original allocation are independently reconstructed; all24 source profiles match after prime normalization. This is not blanket acceptance of every source financial conclusion. The extension retains original donor expenditure, booked balance, other full terminals, parked2tau, old signed debit labels and nonnegative credit-owner labels. Source-prefix compatibility is proved rather than retrospectively reallocating its credit. New claim {claim['claim_id']}@1, hash {sh}, is source-complete author proof/exact certificate pending independent review. This verifies and extends a narrow existing dependency, not another broad universal candidate.

## one next mathematical action and independent reviewer

{next_action} No third-core or full FEI conclusion follows merely from the current root equalities.

## actual persistence receipts or precise save blocker

All artifacts are local to this A084 run; out/MANIFEST.json records SHA256/size receipts and protocol field checks. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. No repository, shared index, other-agent folder or brain store was written. Supervisor mirroring and independent downstream acceptance remain unverified. Final local save/checklist receipt is out/FINAL_PERSISTENCE_CHECK.json; the manifest excludes itself and that final receipt to avoid circular hashes. Formal compilation remains held by admission, not a proof failure.

## Universal bridge

C019 stopping-tree payment advances from one-core stopping policies to every two-core adaptive policy in this retained actual family at ZERO additional outside flow, even after every original source prefix allocation, for the full real half-line of supplied old debit. The exact improvement is three144-state hulls and72 inherited-prefix cuts at extra threshold0. Third/fourth-core admission and a dimension-independent arbitrary-core credit bound remain open. Testing the next admission against actual joint allocated credit, while preserving donor expenditure and complete terminals, is the shortest next route toward universal C019 payment: it directly challenges the unpaid inherited charge rather than establishing another unrelated class inequality.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(BASE/'STATUS.md').write_text('STATE: Stage7 complete locally: same supplied credit for all two-core policies and72 actual source-prefix cuts;66038 exact checks; independent review pending; full FEI OPEN.\nNEXT: Compare third-core requirement against actual joint allocated credit with all donor/terminal books retained; A074/A092/A075 reconstruct certificate.\n',encoding='utf-8')
with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23 03:51 UTC stage (20261023T035136Z): Independently reconstructed A072 one-core S/R profiles (24 matches), then certified all three two-core orbit hulls (432 states/2520 rows) at original credit A0, and all72 actual-prefix cuts at extra threshold0. Full real D>=0 and normalized-weight faces proved algebraically;66038 nonpilot exact checks. Lean admission held; no compiler. Local proof/certificates saved; independent review and mirror unverified. Next: actual-credit third-core admission.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23: For retained F_plus=J(-1,+1,g,g,g,g), h negative{0,1,2,4,8,16,32,6,17,40}, J=-h after bit0 flip, g negative{0,1,2}, rate4, all policies in any two remaining cores have sharp root credit A0=-S(F_plus). Original A072 one-core allocated credit already dominates the two-core hull at every one of72 canonical prefix cuts: no retroactive reallocation/new donor. Real supplied D>=0 shifts all credits exactly D. Generic finite-DAG hull R=max(0,-S,max_query weighted Rchild) covers normalized real weights with unreachable zero-weight outcomes removed and zero-debit kernels explicit. This does not cover third/fourth-core or arbitrary-core admission; no universal FEI estimate follows. Proof and exact certificate: runs/20261023T035136Z-fleet03-A084-continuum-parameters/PROOF.md; independent review pending.\n')
manifest={'schema_checks':'PASS','protocol_revision':protocol['revision'],
 'claim_statement_sha256':sh,'statement_digest_convention':'SHA256 utf8 compact sorted JSON of exact_statement and hypotheses',
 'files':[],'mirror_verified':False,'independent_review':'PENDING'}
for p in sorted(RUN.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in {'MANIFEST.json','FINAL_PERSISTENCE_CHECK.json'}: continue
 assert p.stat().st_size<20*1024*1024,p
 manifest['files'].append({'path':p.relative_to(RUN).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)})
write(RUN/'out/MANIFEST.json',manifest)
print(json.dumps({'claim':claim['claim_id']+'@1','sha256':sh,'files':len(manifest['files']),'schema':'PASS','nonpilot_assertions':66038}))
