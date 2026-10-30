from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];FLEET=A.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):(R/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
base=Path('math-open-problems/reports/fei-2026-10-11')
P=read(base/'EXECUTION_PROTOCOL.json')
main=read(R/'out/EXACT_CHECK.json');four=read(R/'out/N4_CHECK.json');ind=read(R/'out/INDEPENDENT_CHECK.json');pilot=read(R/'out/PILOT.json')
assert all(o['status']=='PASS' for o in [main,four,ind,pilot])
total=sum(o['assertions'] for o in [main,four,ind])
prior=A/'runs/20261023T033823Z-fleet03-A054-connectedness-alternatives'
src52=FLEET/'agents/A052/runs/20261023T055856Z-fleet03-A052-critical-source-structure'
sources=[base/'EXECUTION_PROTOCOL.json',FLEET/'BOARD.md',FLEET/'claude/B11/STREAM_NOTES.md',src52/'REPORT.md',src52/'PRECONDITIONING_PROOF.md',src52/'CLAIMS.json',prior/'RESET_COMPONENT_INTERFACE.md',prior/'CLAIMS.json',A/'runs/20261014T055856Z-fleet05-A054-connectedness-alternatives/code/mathcore.py']
write('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'observed local bytes, read-only; proof scopes specified in REPORT/REVIEW; baseline helper was read, not imported by this stage checkers'} for p in sources])
c52=read(src52/'CLAIMS.json')[0]
write('out/REVIEW_RECEIPT.json',{'reviewer':'fleet03/A054','source_claim_id':c52['claim_id'],'version':c52['version'],'source_statement_sha256':c52['statement_sha256'],'source_proof_sha256':sha(src52/'PRECONDITIONING_PROOF.md'),'verdict':'SCOPED_HOLDS_WITHOUT_REPAIR','scope':'Sections1--3 and5 compensated bank, transported quotient ranks, genuine critical child eligibility and changed-partition guard; not entire family/census acceptance','review_path':'REVIEW_A052.md'})
stmt=('For every n>=2, nonempty Boolean negative support U of mass p, and partition into labels with no cross-labelled physical cube edge, set w(v)=P[f(X)!=f(X+v)], gamma(v)=P[X,X+v in U with distinct labels], ell=w+2gamma, I0=I(f). Let M0 be minimum ordinary-cost vector-basis sum and lambda0(v)=min{t:v in span{z:w(z)<=t}}. Then min over input bases B and marked v in B with ell(v)>=p of [sum_B w+2gamma(v)] equals M0+tau0, tau0=min_{ell(v)>=p}[ell(v)-lambda0(v)], with empty minimum infinity. Thus a reset and singleton meeting W>=p/2 and2gamma(v)<=rho-u exist iff M0+tau0<=I0-u, for any retained old debit u>=0. They pay L<=C(w(v)+rho-u), C=4+2/ln2+4/(e ln2), retaining all actual terminal entropies. This is an exact frontier for the stated sufficient interface mechanism, not for entropy-payment necessity. The all-crossing-labelled analogue has minimum M+tau, tau=min_{ell(v)>=p}(ell(v)-lambda(v)), and M0+tau0<=M+tau, strictly for actual Boolean support{1,2} in three bits with nonzero L=2 and old debit1/2. Genuine least-essential-dimensional positive K-witnesses at K>=C cannot satisfy the criterion with u=0. Original coordinate restrictions retain admissible inherited labels. Output characters, universal critical-source selection and full FEI are not asserted.')
cid='A054-RESET-COMPONENT-CROSSING-INTERFACE'
cons=['A051','A052','A053','A055','A090','A094','claude/B11','B20']
claims=[dict(claim_id=cid,version=2,exact_statement=stmt,hypotheses=['Finite uniform cube n>=2; entropy bits; nonempty sign support, and inherited labels have no cross-labelled physical edge before reset','Invertible INPUT affine changes only; no output-character multiplication','Old debit u is retained; both complete actual restriction terminals and all earlier siblings remain in their signed ledger','Critical exclusion uses genuine least-essential-dimensional positive K-violation, K>=C; it is not inferred from weak ratio criticality'],statement_sha256=hashlib.sha256(stmt.encode()).hexdigest(),contributors=['fleet03/A054'],proof_source={'path':str(R/'FORCED_DIRECTION_PROOF.md'),'sha256':sha(R/'FORCED_DIRECTION_PROOF.md'),'locator':'Sections1--4, especially equations7--8 and the strict actual Boolean example'},proof_dependencies=[{'claim_id':cid,'version':1,'acceptance':'AUTHOR_PROOF_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW','used_scope':'universal raw/sign row bound; explicit8gamma singleton interface; complete signed terminal identity; prior proof pinned in source receipts'}],review_records=[],status='AUTHOR_PROOF_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW',supersedes=[cid+'@1 (extension; no retraction)'],refutes=[],first_unproved_line=None,next_consumers=cons)]
write('CLAIMS.json',claims)
next_action='Force sharp M0+tau0<=I0-u AFTER an actual ORIGINAL proper restriction of a genuine high-K source, paying the original full signed bill and every sibling from SAME unused reserve; A090/A094 review basis exchange and marked-singleton frontier.'
prog=dict(protocol_revision=P['revision'],run_id=R.name,stream='B11',packet_id='A054',gap_id='B11-SIGNED-CRITICAL-QUERY-RESET-SELECT',attempt_id='A054-stage19-forced-query-direction',method='Exact forced-element basis exchange, mixed ordinary/queried-label costs, scoped independent source review and exact Boolean/certificate replay.',mathematical_delta='Replace a release optimizer followed by an unproved next-query selection with an exact marked-direction cost M0+tau0; only queried crossing flux is paid. Strict actual nonzero-L example retains an already booked full release. Universal selection remains open.',deliverable_status='COMPLETE_LOCAL',mathematical_status='AUTHOR_PROOF_EXACT_VALIDATION_PASS_FULL_FEI_OPEN',claim_versions_used=[cid+'@1'],claims_created_or_changed=[cid+'@2'],source_artifacts=['FORCED_DIRECTION_PROOF.md','REVIEW_A052.md','out/FROZEN_SPEC.json','out/FROZEN_N4.json','out/FROZEN_V3.json','out/EXACT_CHECK.json','out/N4_CHECK.json','out/INDEPENDENT_CHECK.json','out/REVIEW_RECEIPT.json','out/SOURCE_RECEIPTS.json'],next_consumers=cons,next_action=next_action,stagnant_substantive_attempts=0,blockers=['Genuine critical-source forcing of the sharp criterion after an ORIGINAL restriction remains open.','Original query full signed bill, all siblings and old debit cannot be paid twice.','Output-character support-label transfer excluded.','New claim independent review, shared registry adoption and supervisor mirror verification pending.','Brain personal-model/state/dream freshness degraded; current mathematical sources govern.'],packet_ids=['A054'])
write('PROGRESS.json',prog);write('PACKET_DELTA.json',prog)
examples={}
for filename in ['EXAMPLES.json','N4_EXAMPLES.json']:
 for key,e in read(R/'out'/filename).items():examples[filename+':'+key]={k:e[k] for k in ['n','source','mass_count','normalizer','I0','M','tau','M0','tau0','best_singleton']}
write('out/CASE_SUMMARY.json',examples)
report=f'''# exact target, quantifiers, hypotheses and units

A054/B11 stage19 strengthens the controlled component interface theorem
by selecting an actual reset basis AND a qualifying next singleton inside
the SAME unused bank. Uniform finite cubes; Fourier entropy bits; n>=2;
p>0. Labels have no physical cross-label edge before reset; actual
components and their inherited original-coordinate restrictions qualify.
Input changes only. Full FEI OPEN. The owner deadline23October14:49UTC
supersedes the older protocol clock.

# sources actually read, revisions and theorem locators

BOARD snapshot10:53UTC, unchanged B11 STREAM_NOTESv2 and own stage18 STATUS
read at start. Protocol2026-10-11-execution-v2 read and schema reloaded.
A052 latest REPORT and PRECONDITIONING_PROOF Sections1--5 read; scoped
independent reconstruction in REVIEW_A052 accepts Sections1--3 and5
without repair. Earlier A054 raw/sign helper, prior reset proof and its
claim consumed. Campaign registries, plan, supplement and four manuscript
baseline reads are retained, not claimed fresh audits. Source receipts
pin observed local bytes, not immutable commits. One two-wording read-only
math recall returned WEAK MATCH and no answering forced-basis/interface
card; it supplies no premise. Brain self-care degraded/unverified:
personal-model97.4h, state-of-mind82.0h, latest dream32.7h stale at wake;
the user was told, and current orders/proof sources govern.

# complete derivation or exact first unsupported line

FORCED_DIRECTION_PROOF Sections1--4 supplies the derivation. Forced-element
basis exchange gives minimum cost M+c(v)-lambda(v), including ties.
Applied to labelled costs ell=w+2gamma this jointly funds all crossing
and one qualifying query at cost M+tau. More sharply, the query only
needs its OWN crossing charge. Pricing the remaining basis by ordinary
influence gives the exact marked-direction cost M0+tau0, equation7.
Thus the sufficient singleton hypotheses are achievable iff
M0+tau0<=I0-u, with the old debit retained. Equation5 pays the explicit
8gamma queried interface from SAME remaining rho-u; equation6 retains
both complete actual child entropies and their signed reserves.

The sharper class is strictly larger: U={{1,2}} on three bits has I0=3/2,
all-labelled cost3/2, sharp cost1, and reset columns(1,3,4). Query first:
rho=1/2, gamma_query=0, w_query=1/2, actual L=2. Old debit u=1/2 leaves
zero release, but no queried crossing payment is needed. The unrelated
crossing direction is not charged to this singleton. The paid critical
class excludes genuine least-dimensional K-witnesses for K>=C at u=0,
C=4+2/ln2+4/(e ln2)<37/4, without terminal pruning. This does not show
that failing the criterion makes the actual entropy bill unpaid.

FIRST UNSUPPORTED UNIVERSAL LINE: after an actual ORIGINAL proper
restriction, force the sharp marked-direction cost below I0-u while
paying the original complete signed query bill and ALL siblings from the
same unused child reserve. Criticality licenses smaller-child reserves;
it does not supply this rank/forcing-cost inequality. A052's invariant
prevents obtaining new credit by merely preconditioning the same partition.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC, FROZEN_N4 and FROZEN_V3 precede their respective checks.
Final pilot n<=2: {pilot['assertions']} assertions PASS. Final v3 main:
{main['assertions']} checks,273 roots n1..3 plus1488 inherited nonempty
original-singleton children,20457 old-debit half-grid tests, PASS in
{main['seconds']:.6f}s. Fixed n4 sample (not exhaustive):64 labelled masks
(1103515245*j+12345) mod65536, j0..63, and512 inherited children;
{four['assertions']} checks,16544 old-debit tests, PASS in{four['seconds']:.6f}s.
All unordered independent bases enumerated, counts1,3,28,840 by dimension;
only basis permutations removed. The sample has12 positive all-labelled
surcharge paid cases and1 unpaid-by-that-criterion case. CASE_SUMMARY
and full exact EXAMPLES preserve provenance, costs and marked bases.

Independent replay imports no helper: direct character sums, set-span
enumeration, exact prime-log entropy vectors and integer-product sign
certificates. {ind['assertions']} checks PASS in{ind['seconds']:.6f}s, on
{ind['representatives']} saved representatives, {ind['actual_signed_identity_and_payment_tests']}
actual complete-terminal payment checks, k2,3,4 fixed bent directional
profiles, the A052 changed-partition adversary and the explicit nonzero-L
strict-improvement example. This is an independent implementation by
A054, not independent-agent acceptance. Final NEW-stage total{total};
pilot and earlier checker versions excluded. No floating sign decision,
no exhaustive n4 claim, no dimension extrapolation and no Lean certificate.

Commands: python -X utf8 code/check_forced_basis.py --pilot;
python -X utf8 code/run_checks.py (sequential full n<=3, fixed n4,
independent); final python -X utf8 code/independent.py adds the explicit
strict example and replaces its count. Estimated peak<=120MB, unmeasured;
each search55s cap, observed seconds above. No job expected>300MB, so no
heavy-job admission needed. All work synchronous and finished.

# proof dependencies and changed downstream conclusions

This is version2 of the existing component crossing candidate, not a
third broad unreviewed claim. Version1's raw/sign row bound and terminal
identity remain dependencies, with author-proof status pending independent
review. Vector-basis exchange and exact mixed-cost optimization are proved
here. Scoped A052 invariance review supplies no new mathematical premise
for exchange; it closes the free-preprocessing funding interpretation.
The cheap-rank release alone is insufficient for next-query selection.
The new scalar frontier prices that selection, and avoids charging every
other inherited-label crossing to one marked query. Universal constant
gain0; no source theorem refuted, no FEI or actual entropy failure claimed.

# one next mathematical action and independent reviewer

{next_action} A051/A052/A053/A055 consume the sharp singleton-only budget
and keep input-only scope; A090/A094 reconstruct the full dependency chain.
No external messages sent.

# actual persistence receipts or precise save blocker

The four exact-schema protocol files, proof, scoped review, frozen specs,
code and exact outputs are saved only under A054. Finalizer validates
claim statement hash, exact keys, report headings, byte-identical progress
copies,20MB cap and two-line STATUS. out/PERSISTENCE_RECEIPT pins saved
bytes and rolling files; a subsequent readback is required. Shared indices,
GitHub copies, brain ingestion and independent review remain unverified.
No git, mail, brain writes, other-agent mutation, deletion, GPU or detached
work. Nothing left running by this stage.

## Universal bridge

C019 stopping-tree payment gains an exact mixed-cost interface frontier:
M0+tau0 is the least actual reset-basis cost plus the marked query's
crossing charge, and M0+tau0<=I0-u pays its complete signed continuation
without renewing old debit. The strict Boolean L=2 example removes a
real overcharge, while A052 review rules out free credit from a fixed
query's chart change. Universal constant gain is zero. The remaining
bridge is to force this inequality after an ORIGINAL critical restriction
while funding that original full bill and all siblings. NEXT attacks
precisely that independent-rank/forcing-cost inequality, rather than
another isolated truth-table class, because it is the unpaid selection
step needed to telescope to full FEI.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
status=f'STATE: A054 stage19 saved: exact marked-query cost M0+tau0 pays ONLY queried crossing from SAME old-debit bank; strict actual L=2 example; {total} exact checks PASS; FEI OPEN, review pending.\nNEXT: Force M0+tau0<=I0-u after ORIGINAL critical restriction with original full signed bill and ALL siblings; A090/A094 review; A052 no-free-preconditioning scoped HOLDS.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
entry=f'\n2026-10-23 stage19 ({R.name}): forced-element basis exchange gives exact all-labelled M+tau and sharper ordinary/marked-crossing M0+tau0. Old debit retained; strict actual n3 U={{1,2}}, L=2, u=1/2 paid without charging another direction\'s gamma. Scoped A052 compensated invariant/quotient rank review HOLDS without repair. {total} final exact checks PASS; no Lean certificate; independent review/full FEI OPEN. Nothing running.\n'
for name in ['WORKLOG.md','LEARNED.md']:
 with (A/name).open('a',encoding='utf-8',newline='') as f:f.write(entry if name=='WORKLOG.md' else '\n2026-10-23: For any directional weights c, min basis containing v costs M+c(v)-lambda(v), lambda the first threshold span containing v. For labels without physical cross-edges, ell=w+2gamma; exact cost to select a W>=p/2 singleton AND pay only its crossing is M0+min_{ell(v)>=p}(ell(v)-lambda0(v)), not the all-labelled M+tau. Compare to I0-u with old debit retained. Actual U={1,2} on3bits gives sharp1 vs all-labelled3/2, old debit1/2, complete L=2 paid. Failing the test does not prove unpaid entropy. Output characters excluded; critical-source forcing remains OPEN.\n')
assert set(prog)==set('packet_ids' if k.startswith('packet_ids ') else k for k in P['required_per_run']['progress_fields'])
assert all(set(c)==set(P['required_per_run']['claim_fields']) for c in claims)
assert all('# '+h in report for h in P['required_per_run']['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
write('out/PERSISTENCE_RECEIPT.json',{'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in files+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'full_fei':'OPEN','remote_mirror':'UNVERIFIED','independent_review':'PENDING'})
print(json.dumps({'status':'SAVED_SCHEMA_PASS','assertions':total,'claim':cid+'@2','files':len(files),'full_fei':'OPEN'}))
