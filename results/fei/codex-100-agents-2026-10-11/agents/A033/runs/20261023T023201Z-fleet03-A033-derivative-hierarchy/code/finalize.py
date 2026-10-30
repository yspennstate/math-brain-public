from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
BASE=AGENT.parents[1]; RUN=ROOT.name
now=datetime.now(timezone.utc).isoformat()
def read(p):return Path(p).read_text(encoding='utf-8-sig')
def js(p):return json.loads(read(p))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):Path(p).write_text(v,encoding='utf-8')
def dump(p,v):write(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
v=js(ROOT/'out/targeted.json'); f=js(ROOT/'out/biased_continuation.json')
assert v['status']==f['status']=='PASS'
assert v['parent_query_profiles']==656 and v['targeted']
assert v['helper_sha256']==sha(ROOT/'code/check.py')
assert f['helper_sha256']==sha(ROOT/'code/biased.py')
source_run=BASE/'agents/A032/runs/20261023T013017Z-fleet03-A032-boolean-phase-realizability'
source_claims=js(source_run/'CLAIMS.json')
old=next(c for c in source_claims if c['claim_id']=='A032-SIGNED-TAG-VACUUM-TAIL-RESET')
assert hashlib.sha256(old['exact_statement'].encode()).hexdigest()==old['statement_sha256']
review=dict(old)
review['review_records']=list(old['review_records'])+[{'reviewer':'A033','at':now,'verdict':'HOLDS_AT_STATED_SCOPE','method':'Independent complete signed Fourier/reference factorization, exact prime-log identities and direct-character boundary fixture; no author code or repair','source':str(ROOT/'REVIEW_A032.md'),'formal_verification':'NOT_CLAIMED'}]
review['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A033_LOCAL_ADOPTION_UNVERIFIED'
statement=('Let A,B on a uniform controller cube satisfy AB=0 and A^2+B^2=1 pointwise, h be any independent Boolean seed, and G_sigma=A+sigma B h the BOTH actual physical tag children. Given the finite-CE normalized CURRENT signed-vacuum reference Q_sigma(U,empty)=(Ahat(U)+sigma E(h) Bhat(U))^2, Q_sigma(U,T)=Bhat(U)^2(1-E(h)^2)M(T) for nonempty T, query one physical seed bit i. Keep its actual inherited marginal Qbar_sigma, old debits and all reference-only atoms. With m1=M({i}), w=(1-E(h)^2)(1-m1), L(V)=[M(V)+M(V+i)]/(1-m1) on nonempty residual V, and nu_tau=E(h|i=tau), the exact coarse refund R_sigma,tau is KL between ((Ahat+sigma nu_tau Bhat)^2 at EACH controller vacuum atom, beta(1-nu_tau^2)) and ((Ahat+sigma E(h)Bhat)^2+Bhat^2(1-E(h)^2)m1 at EACH vacuum atom, beta*w). For fresh tail N=(1-epsilon)L+epsilon S, 0<=epsilon<1, matching each actual vacuum atom and total actual tail gives reset increment -R_sigma,tau+beta(1-nu_tau^2)[D(p_tau_tail||N)-D(p_tau_tail||L)]. The complete physical erasure-plus-mean-child-CE increment is minus current conditional occupancy KL rho_sigma, minus mean R_sigma,tau, plus the displayed mean tail change. Hence a mean likelihood-floor bill <=rho_sigma+mean R_sigma,tau funds the prescribed reset from the SAME incoming terminal, retaining BOTH seed children, BOTH tag children and every prior debit. Zero sectors are handled without division. The refund includes a controller-vacuum-profile KL in addition to scalar occupancy KL; the actual Boolean balanced seed x_i*[-1,1,1,1] with A=(1+c)/2,B=(1-c)/2 has scalar refund zero but profile refund (9/8)log2(3)-(5/8)log2(5)>1/4 at all four terminals. For the fixed A079 mask and seed [1,1,1,-1,1,1,1,-1], use incoming source R0=1/2,Rtail=p_tail and A032 actual paid first epsilon1/8 uniform tag mixture. The next bit-weight-one query and a prescribed SECOND epsilon1/8 mixture with ANY residual nonempty target have full increment<-1/10 at EACH tag child, since inherited vacuum mass=361/448 and 448^40*7^15>2^8*361^40*8^15. Old mixture/debits and four full terminals remain. This is conditional source-history transfer in bits, not a universal initial source price, new Booleanity admission inequality or full FEI proof.')
claim={
 'claim_id':'A033-POST-TAG-SEED-VACUUM-REFUND','version':1,
 'exact_statement':statement,
 'hypotheses':['Actual independent uniform physical controller/seed coordinates; complementary disjoint A,B; actual signed means and Fourier coefficients','Finite-CE normalized CURRENT reference of the displayed form, including any already paid earlier mixture','Prescribed fresh target is normalized and epsilon<1; zero sectors use explicit PROOF.md endpoints','History application requires the incoming source account already paid; old debits/full terminal costs retained; no automatic influence bound on erasure','Entropy, CE and KL in bits; original physical influences; the packet Booleanity-specific universal target remains open'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A033'],
 'proof_source':{'path':str(ROOT/'PROOF.md'),'sha256':sha(ROOT/'PROOF.md'),'validation':['out/targeted.json','out/phase_fixture.json','out/biased_continuation.json'],'formal_verification':'NOT_LAUNCHED_MEMORY_GATE'},
 'proof_dependencies':[], 'review_records':[],
 'status':'AUTHOR_PROOF_WITH_EXACT_CERTIFICATES_INDEPENDENT_REVIEW_PENDING',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A032','A079','A088','A094','A096','A097','B07','B20']}
dump(ROOT/'CLAIMS.json',[review,claim])
next_action='At an arbitrary-core post-tag reset, use the FULL current rho+controller-vacuum refund as the source-facing eligibility condition; derive a dimension-independent lower bound from SAME unused original physical-influence reserve, or refute that proposed lower bound by actual Boolean seeds. A032/A079/A088/A094 review first; no return to fixed prefixes or fixed controller all-history banks.'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B07','packet_id':'A033','gap_id':'G-BOOLEANITY','attempt_id':'A033-POST-TAG-SEED-VACUUM-REFUND-1',
 'method':'Independently consume A032 signed tag reset; exact current-reference occupancy/coarse-KL decomposition after next active seed query; retain signed vacuum profile and both full terminals; strict exact second-mixture witness',
 'mathematical_delta':'A032 signed-tag reset independently HOLDS at unchanged conditional scope. New exact post-tag active-seed-query/reset identity retains full controller-vacuum KL, which can be positive at zero scalar refund. Actual A079 biased first1/8-mixture continuation funds a SECOND prescribed1/8 mixture with >1/10-bit release at EACH tag child from SAME source owner. Universal influence price and sought extra Booleanity-specific inequality gained: none; both remain open.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'CONDITIONAL_HISTORY_TRANSFER_AUTHOR_PROOF_EXACT_CERTIFICATES; A032_INDEPENDENT_REVIEW_HOLDS; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256'],'use':'Independently accepted unchanged; supplied paid first-reset interface/application only. New identity self-contained.'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1},{'claim_id':old['claim_id'],'version':old['version'],'change':'Independent A033 review only; statement unchanged'}],
 'source_artifacts':['PROOF.md','REVIEW_A032.md','NO_GO_IMPORT.md','FROZEN_SPEC.json','FROZEN_REPLAY.json','FROZEN_TARGETED.json','FROZEN_BIASED.json','code/check.py','code/biased.py','out/targeted.json','out/phase_fixture.json','out/biased_continuation.json','out/formal_status.json','out/attempt1_timeout.json','out/attempt2_timeout.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['No universal initially influence-priced source or dimension-free Booleanity-specific lower bound on required unused refunds','Distinct cyclic atom-cap no-go original construction/checker still absent locally; import remains audited summary only','Compiler not launched: memok exit1, physical free1.7GB below4GB; no formal certificate','New A033 extension external review and supervisor publication are unverified'],
 'packet_ids':['A033']}
dump(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',read(ROOT/'PROGRESS.json'))
report=f'''# exact target, quantifiers, hypotheses and units

Continue beyond A032's already paid physical tag reset, using its CURRENT
signed-vacuum reference on BOTH tag children of A+zBh. Query ONE active
physical seed bit, retain both full seed children, and price a prescribed
new tail mixture from the SAME incoming terminal and unused original owner.
PROOF.md equations (6)--(8) are exact for every displayed finite-CE reference,
all complementary A,B and Boolean seed h, including zero sectors. An actual
A079 biased example retains the paid first1/8 mixture and funds a SECOND
prescribed1/8 mixture with more than1/10 bit release at EACH tag child.
Bits throughout; original uniform-cube coordinates and influences.
Full FEI and the packet's sought extra Booleanity inequality remain OPEN.

# sources actually read, revisions and theorem locators

At entry read BOARD written2026-10-23 02:33UTC, B07 STREAM_NOTES v2 and own
STATUS; machine-wide AGENTS and full EXECUTION_PROTOCOL v2 were reread.
Current owner endpoint23October14:49UTC supersedes historical protocol dates.
A032 run20261023T013017Z REPORT, PROOF sections1--5 and exact CLAIMS scope;
A079 run20261022T225318Z REPORT and PROOF sections1--4; own previous stage
PROGRESS and exact helper were inspected. REVIEW_A032.md independently
reconstructs the NEW A032 tag-reset lemma without author code or repair.
ROUTE_MAP_CURATED section3 and own LEARNED were reread for the fixed-order
no-go import; precise scope and the missing atom-cap source are recorded
in NO_GO_IMPORT.md. Earlier campaign/paper baseline stays background, not
a fresh audit or a new paper dependency. Source hashes are saved locally.
Personal-context wake notes are not proof or authorization premises.

# complete derivation or exact first unsupported line

After the seed query, the inherited vacuum reference is
(ahat+sigma*mu*bhat)^2+bhat^2(1-mu^2)M({{i}}), while the TRUE child vacuum
is (ahat+sigma*nu_tau*bhat)^2. Replacing one by the other is a reset.
Keep every controller-vacuum atom and coarsen only the nonempty seed tail.
Their coarse KL is the exact refund R for recalibrating vacuum and total
tail mass. The current conditional tail is carried into the prescribed
mixture. Complete erasure-plus-terminal cost equals -rho-mean R plus the
actual tail likelihood change; rho is the CURRENT conditional occupancy
KL. Equations(6)--(8) prove this directly, with finite-support/endpoints.
It is never called a free arbitrary reset or a new influence bank.

The refund contains controller-profile KL beyond scalar occupancy. An
actual balanced Boolean example has scalar refund0 but profile refund
(9/8)log2(3)-(5/8)log2(5)>1/4, certified by3^9>4*5^5; a genuinely changed
1/8 tail mixture then leaves>5/32 release. The concrete A079 biased
continuation keeps its FIRST actual1/8 uniform target mixture, with
M({{i}})=13/42, current L=(26/29,3/58,3/58). The next query's inherited
vacuum mass361/448 and constant-child refund bound give a SECOND arbitrary
1/8-target mixture cost<-1/10 at EACH tag child. The exact certificate is
448^40*7^15>2^8*361^40*8^15. All four final terminal spectra remain.

The exact first unsupported universal line is an initially influence-priced
reference for arbitrary h, or a dimension-free Booleanity-specific lower
bound paying required future resets and erasures from unused ORIGINAL
influence. Generic KL does not supply it. These identities also apply
beyond Booleanity and are explicitly NOT the lead's missing inequality
excluding normalized nonBoolean controls. ALL signed-convolution identities
and all physical split identities, not a fixed prefix or dyadic grid, are
stated in PROOF.md. No fixed-bank all-history shortcut is retried.

# executed validation with domain, arithmetic, commands and outputs

Specs precede each search. Initial pilot passed2444 exact assertions on40
parent query/profiles; two broad2048-case attempts reached their180s limit
and are INCOMPLETE, recorded separately. They contribute no completed-domain
certificate. Bounded caching improved the pilot; after the second timeout
the validation mechanism changed to a separate frozen boundary panel.
No dimension was increased. Completed targeted certificate: all16 signed
one-controller masks/all16 two-bit seeds/every seed query plus fixed A079
mask/24 explicitly frozen three-bit seeds/every seed query/two references.
This is {v['parent_query_profiles']} parent-query profiles, {v['actual_terminals']}
actual terminals, {v['fresh_resets']} fresh resets and {v['exact_assertions']}
exact assertions in {v['runtime_seconds']:.6f}s. Constant parents are explicit
stops. Integer FWHT, Fraction probabilities and exact prime-log expressions
verify the complete current CE/refund identities, A032's antecedent and
normalizations/supports. No float determines a mathematical sign.

Independent direct character sums and integer powers certify the biased
continuation: {f['exact_assertions']} exact assertions in {f['runtime_seconds']:.6f}s,
all four terminal spectra and references saved. Commands from A033:
python -B -X utf8 runs/{RUN}/code/check.py --targeted
and python -B -X utf8 runs/{RUN}/code/biased.py.
Outputs: out/targeted.json, phase_fixture.json, biased_continuation.json.
The universal quantifiers follow from the written algebra, not extrapolation.
Fresh memok exited1 (physical free1.7GB below4GB; commit18.6GB). No compiler
was launched; intended arithmetic guard is code/Core.lean. Formal status:
NOT_LAUNCHED_MEMORY_GATE. The standard-library jobs were estimated below140MB;
no >300MB job, GPU, new worker or detached producer was launched.

# proof dependencies and changed downstream conclusions

A032-SIGNED-TAG-VACUUM-TAIL-RESET@1 independently HOLDS locally, unchanged
statement hash a8eaef0443d2816feeef2b939d7fd28498792dd1561d0bd3da7168a2e134885e.
It supplies the already-paid first tag reset only. The new post-tag identity
is derived self-containedly. A033's previous fixed-controller no-go remains;
full source entropy and remaining reference debt are retained. New A033
external review, shared-registry adoption, supervisor copying and remote
persistence are unverified. No universal C018 inequality or full FEI closes.

# one next mathematical action and independent reviewer

{next_action}
This is a saved handoff, not a sent message or claimed downstream adoption.

# actual persistence receipts or precise save blocker

Four protocol files, full derivation/review/import notes, frozen specs,
scripts and exact outputs are saved here. out/PERSISTENCE_RECEIPT.json
checks exact protocol keys, statement/helper hashes, completed certificates,
file sizes, two-line STATUS and byte-identical progress/delta. All files
are below20MB. STATUS/WORKLOG/LEARNED are current. Local persistence only;
supervisor publication remains outside this agent's authorized write scope.
No git, mail, brain write, other-agent mutation, trading-project access or
stop of existing work occurred. Brain self-care remains degraded/unverified:
owner model89h and state-of-mind73.6h were stale at wake. This affects
personal-context freshness; those notes did not authorize work or prove math.

# Universal bridge

This stage moves C024 history transfer and C019 stopping-tree payment by
one ACTUAL active seed query and SECOND prescribed tail reset after A032's
paid tag reset, keeping its old1/8 component, old debit, SAME original
account and all four terminals, with>1/10-bit new release per tag child.
It identifies the complete signed controller-vacuum KL refund that scalar
occupancy can miss. The remaining bridge is a universal initially
influence-priced source, or a Booleanity-specific bound on required
unused refunds; neither is supplied. NEXT tests that precise arbitrary-core
source-facing eligibility condition against original influence, so it
addresses the universal missing payment rather than extending another
finite class or increasing a fixed derivative/convolution prefix.
'''
write(ROOT/'REPORT.md',report)
write(AGENT/'STATUS.md','STATE: Post-tag active seed/reset identity; actual prior1/8 mixture funds SECOND prescribed1/8 reset with >1/10-bit release per tag child; exact certificates PASS; A032 independently HOLDS; FEI OPEN.\nNEXT: A032/A079/A088/A094 review full signed-vacuum refund; bound arbitrary-core rho+profile refund from SAME unused original influence, both terminals/old debits retained; no fixed-bank shortcut.\n')
entry=f'\n{now} - {RUN}: Independently reconstructed A032 signed-tag reset unchanged. Derived exact next seed-query/current-reference reset cost -rho-mean full vacuum/tail coarse KL plus actual tail likelihood change; scalar occupancy can miss strictly positive signed controller-profile refund. Actual A079 biased first1/8-mixture continuation funds SECOND arbitrary1/8 target mixture with>1/10-bit release at each tag child, old account/debits/full four terminals retained. Two2048-case runs timed out honestly; changed to frozen656-case boundary panel, {v["exact_assertions"]} exact assertions PASS; independent biased direct-character47 checks PASS. Compiler not launched: memok1. Universal initial source/Booleanity inequality remains OPEN.\n'
for filename in ('WORKLOG.md','LEARNED.md'):
 oldtext=read(AGENT/filename)
 if RUN not in oldtext:write(AGENT/filename,oldtext+entry)
sources=[source_run/'PROOF.md',source_run/'CLAIMS.json',BASE/'agents/A079/runs/20261022T225318Z-fleet03-A079-correlated-auxiliaries/PROOF.md',BASE/'claude/B07/STREAM_NOTES.md',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents/sources/ROUTE_MAP_CURATED.md')]
dump(ROOT/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'role':'source actually read; final local hash'} for p in sources])
claimfields=set('claim_id version exact_statement hypotheses statement_sha256 contributors proof_source proof_dependencies review_records status supersedes refutes first_unproved_line next_consumers'.split())
progressfields=set('protocol_revision run_id stream packet_id gap_id attempt_id method mathematical_delta deliverable_status mathematical_status claim_versions_used claims_created_or_changed source_artifacts next_consumers next_action stagnant_substantive_attempts blockers packet_ids'.split())
assert set(progress)==progressfields
for c in js(ROOT/'CLAIMS.json'):
 assert set(c)==claimfields
 assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len(read(AGENT/'STATUS.md').splitlines())==2
assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C024')
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'status':'PASS','at':now,'run':str(ROOT),'full_fei':'OPEN','new_independent_review':'PENDING','formal':'NOT_LAUNCHED_MEMORY_GATE','remote_persistence':'UNVERIFIED_SUPERVISOR_OWNED','file_count_excluding_receipt':len(files),'exact_protocol_keys':True,'progress_delta_identical':True,'rolling_status_two_lines':True,'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
dump(ROOT/'out/PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))
