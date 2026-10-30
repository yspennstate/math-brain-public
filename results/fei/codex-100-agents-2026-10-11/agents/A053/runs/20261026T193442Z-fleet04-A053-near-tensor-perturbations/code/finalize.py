from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
main=read(R/'out/CHECKS.json'); independent=read(R/'out/INDEPENDENT.json')
assert main['status']==independent['status']=='PASS'
total=main['checks']+independent['checks']
proper_core_fibres=sum(f['certified_core_fibres'] for f in main['families'])
assert proper_core_fibres==208
lean=read(R/'out/LEAN_ATTEMPT.json') if (R/'out/LEAN_ATTEMPT.json').exists() else {'stdout':'not completed','exit_code':None}
lean_text=lean['stdout'].strip()
lean_status='HELD_NO_CERTIFICATE' if 'SETUP_UNVERIFIED' in lean_text else 'SEE_EXACT_RECEIPT_NO_BLANKET_CERTIFICATION'
sources=[Path('~/AGENTS.md'),Path('BOARD.md'),
Path('claude/B11/STREAM_NOTES.md'),
A/'runs/20261023T123501Z-fleet03-A053-near-tensor-perturbations/REPORT.md',
A/'runs/20261023T123501Z-fleet03-A053-near-tensor-perturbations/LINEAR_RADIUS_PROOF.md']
base=Path('math-open-problems/reports/fei-2026-10-11')
sources += [base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
sources +=[supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
ctx=Path('context')
sources +=list(ctx.glob('*.txt'))
other=Path('agents')
sources +=[other/'A054/runs/20261023T130129Z-fleet03-A054-connectedness-alternatives/PAIR_RANK_INTERFACE.md',
other/'A054/runs/20261023T130129Z-fleet03-A054-connectedness-alternatives/REPORT.md',
other/'A055/runs/20261023T132836Z-fleet03-A055-extremal-obstruction-referee/REPORT.md',
other/'A052/runs/20261023T142511Z-fleet03-A052-critical-source-structure/REPORT.md']
save('out/SOURCE_RECEIPTS.json',{'note':'Observed local bytes, not immutable commit or evidence of fresh full-paper audit; papers earlier baseline retained, current threshold Prop8.6 and percolation Thm1.1 excerpted only.',
 'files':[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in sources if p.exists()]})
state=read(Path('~/.claude/compute/compute_state.json'))
save('out/COMPUTE_OBSERVATION.json',dict(observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 snapshot_ts=state.get('ts'),status=state.get('status'),note='Stale telemetry not live admission; no governor or existing process changed; mathematical jobs estimated60--70MB only.',
 cpu_pct=state.get('cpu_pct'),mem_avail_mb=state.get('mem_avail_mb'),disk_free_gb=state.get('disk_free_gb')))
statement='For K>=0 and a coordinate product F=product_j h_j on n bits, let G differ from F on R vertices. For any nonempty proper factor subproduct h_J on m bits let r be its exact vertex distance to the class H<=KI. If all complete original m-bit cofactors of G are K-certified, then R>=2^(n-m)r. More generally at least max(0,2^(n-m)-floor(R/r)) cofactors violate K when r>0. With rho=r/2^m and mu=min_{dist(g,h_J)<r}(H(g)-KI(g))>0, the full signed terminal deficit is at least mu-(mu+Km)min(1,delta/rho), delta=R/2^n. A genuine least-essential-dimension positive K-witness on its n essential coordinates therefore has delta>=max_J rho_K(h_J) for every comparison product. For the three-bit point defect at K2 rho=1/8, sharp for the original one-factor-terminal criterion via the XOR edit family; repaired factor fibres do not imply all proper descendants are certified.'
claim={
 'claim_id':'A053-TENSOR-CRITICAL-REPAIR-DENSITY','version':1,'exact_statement':statement,
 'hypotheses':['Uniform Boolean signs; normalized Walsh entropy in bits; physical influence','At least two nonempty disjoint factor blocks; retained J nonempty and proper','Critical corollary uses least ESSENTIAL dimension and a root represented on exactly its essential coordinates','For r>0 only: finite positive mu, all original physical terminal fibres retained'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A053'],
 'proof_source':'PROOF.md Sections1--3; out/CHECKS.json; out/INDEPENDENT.json',
 'proof_dependencies':['Finite disjoint physical-fibre counting; sign invariance; elementary H>=0,I<=m; tensor additivity only for stated optional corollary'],
 'review_records':[{'reviewer':'A053','kind':'author proof, separate exact arithmetic implementations and sharp scope counterguard','outcome':f'{total} exact assertions PASS; independent-agent acceptance pending; {lean_status}'}],
 'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW','supersedes':[], 'refutes':[],
 'first_unproved_line':'No gap claimed in finite repair-density statement. No universal critical-source proximity theorem or high-K original-block funding including Pi is proved.',
 'next_consumers':['A051','A052','A054','A055','A090','A094','B11','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B11',packet_id='A053',
 gap_id='G-R-SELECT',attempt_id='A053-stage21-critical-fibre-repair',method='Exact finite fibre-distance obstruction; complete signed-terminal reserve; scoped independent phase-bank reconstruction',
 mathematical_delta='Every genuine critical tensor perturbation has density at least each violating subproduct repair radius; sharp1/8 original-core-fibre guard, larger-terminal obstruction retained. A054 Pi identity holds at scoped analytic level. Universal constant gain0.',
 deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_AUTHOR_PROOF; REVIEW_A054_ANALYTIC_HOLDS; FULL_FEI_OPEN',
 claim_versions_used=['A054 stage20 PAIR_RANK_INTERFACE equations1--6 (scoped independently reconstructed; no source census)', 'Elementary finite Boolean identities; prior A053 stage20 is context only'],
 claims_created_or_changed=['A053-TENSOR-CRITICAL-REPAIR-DENSITY@1'],
 source_artifacts=['PROOF.md','out/SOURCE_RECEIPTS.json','out/CHECKS.json','out/INDEPENDENT.json','out/LEAN_ATTEMPT.json'],
 next_consumers=['A051','A052','A054','A055','A090','A094','B11','B20'],
 next_action='Exploit ALL proper-subproduct repair constraints and exact nonnegative full-child reserves to select one ORIGINAL high-K block beyond these neighborhoods, paying Pi and every old debit.',
 stagnant_substantive_attempts=0,blockers=['Universal critical block selection remains open','Independent-agent review, supervisor copying, registry adoption and mirrors unverified',lean_status],packet_ids=['A053'])
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
save('PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# A053 stage21: critical tensors need positive repair density

## exact target, quantifiers, hypotheses and units

For every uniform Boolean product seed F and an R-vertex edit G, quantify how genuine smaller-child criticality forces repair of EVERY parallel physical fibre containing a violating factor or proper factor subproduct. Entropy bits, physical influence, K>=0, delta=R/2^n. The critical corollary represents the root on exactly its n essential coordinates. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD26October19:33UTC, B11 STREAM_NOTESv2 and own stage20 STATUS/LEARNED and report/proof read. Current protocol2026-10-11-execution-v2 read whole. Campaign README/status, B11 routing, registry/plan excerpts and supplemental seed/counterexample material refreshed. Four manuscript baseline reads from earlier stages are retained, not called new full audits; threshold38pp Proposition8.6 equations75--79 and percolation30pp Theorem1.1 read as current excerpts. No percolation or threshold theorem is a premise. Fresh A054 stage20 REPORT and complete PAIR_RANK_INTERFACE, A052 stage11 REPORT, and A055 stage10 REPORT consumed. Actual local byte receipts are in out/SOURCE_RECEIPTS.json. The recalled math-store search supplied no theorem used here. Latest direct continuation request governs the older expired campaign dates; no schedule was extended.

Session wake completed with required stale-owner-model/state/dream warning; owner was told before reliance. These notes are not mathematical premises. Compute telemetry was stale, not used as live capacity evidence; no governor/process changes were made.

## complete derivation or exact first unsupported line

PROOF Sections1--2 gives the complete argument. Let r_K(h) be the vertex distance of an m-bit core to the finite nonempty class H<=KI. Every complementary fibre of the product seed is +/-h. Edit counts sum to the SAME original R, so eligibility of every full terminal forces R>=2^(n-m)r_K(h), hence delta>=rho_K(h). The constraint holds simultaneously for every nonempty proper factor subproduct, without a spectral support or stationarity hypothesis. More quantitatively at least max(0,2^(n-m)-floor(R/r)) terminals violate. With mu the minimum positive deficit below repair radius, the COMPLETE signed bank obeys E D_K(child)>=mu-(mu+Km)min(1,delta/rho); negative siblings remain. Averaged eligibility and individual criticality are explicitly different.

The three-bit point defect at K2 has exact r1 and rho1/8. Editing xor(block labels)=0 reaches density1/8 and repairs EVERY original one-factor fibre for every tensor power. Finite exact n6/n9 certificates show the larger-terminal obstruction survives: G2 violates K2, and G3 has actual proper child -G2. This proves sharpness only for the named fibre test; no critical high-K counterexample or FEI disproof is asserted.

PROOF Section4 independently reconstructs A054's partition-preserving basis minimum, phase stationarity inequality and complete signed bank equations1--6 without repair. The explicit genuine K2 critical guard has J1,R1/2, paid new row, and Pi=D2(h)>0. Dropping Pi remains invalid. Source large census/local flux/global selection claims are outside this acceptance.

FIRST UNSUPPORTED UNIVERSAL LINE: arbitrary genuine high-K critical sources must possess a paid ORIGINAL block including Pi and old debits. The theorem does not supply a nearby product containing a violating factor; certified-factor products have repair radius0 and give no positive exclusion. No inherited bank is reset.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/SPEC.json precedes python -B -X utf8 code/check_fibres.py. PASS {main['checks']} assertions: all256 labelled3bit signs, all8 point repairs, XOR-edit roots n3,6,9, all{proper_core_fibres} proper original-core fibres, and A054 physical n3 guard with three old-debit values. The frozen prose case count24+192 had an arithmetic typo: the unchanged explicit domain has16+192=208 fibres, verified from actual outputs; no case was omitted. Integer Walsh was compared with direct characters; FEI2 signs use exact integer products. Larger entropy signs use Fraction atanh28 with explicit positive remainder, cached only by exact argument. Runtime {main['seconds']:.6f}s, estimated70MB, peak unmeasured.

Separate out/SPEC_INDEPENDENT.json precedes code/independent.py. No primary helper imported: direct characters, independent physical edges, prime-log vectors a+b log2(3), integer-power signs. ALL2081 six-bit edit sets of size0,1,2;4162 complete banks;33296 complete fibres;{independent['checks']} assertions PASS. Its recorded seconds field is CPU time {independent['seconds']}; wall time was not instrumented by this script. A metadata-only timer edit was reverted to the executed implementation; mathematical predicates did not change. This is a separate implementation by A053, not independent-agent acceptance.

New exact-stage total {total}, excluding all previous stage counts. It differs from stage20's91721 because domain and predicates changed. No dimension escalation, GPU, heavy job, detached search or float sign. Small/boundary checks include R0, certified r0 exclusion from division, all one-point repair locations, equality delta=rho, constant/character tables, negative siblings, and a missing-larger-terminal counterguard. Core Lean finite-sum attempt: {lean_status}; exact output in out/LEAN_ATTEMPT.json. An admission hold is not a failed theorem or a Lean certificate. Research rung: author proof with exact finite validation, independent acceptance pending.

## proof dependencies and changed downstream conclusions

The new result is a narrow quantitative consequence of genuine complete-child eligibility, not another proposed universal FEI inequality. It strengthens the earlier clean-copy observation from one untouched fibre to an exact positive-density obstruction and a signed reserve lower bound. Previous linear37R/4 Fourier-code result is unchanged and not a premise. A054 analytic bank scope independently HOLDS unchanged. No registered result refuted; universal constant gain0.

## one next mathematical action and independent reviewer

A051/A052/A054/A055 combine ALL proper-subproduct repair constraints with genuinely nonnegative smaller-child reserves to select an ORIGINAL high-K block outside these neighborhoods, keeping phase price Pi and old debit. A090/A094 review the finite-distance quantifiers, essential-dimension condition and sharp terminal scope. No message or new worker was sent.

## actual persistence receipts or precise save blocker

All four exact-schema protocol files, PROOF, frozen specs, scripts, complete outputs and source receipts saved only inside this A053 run. Finalizer checks claim hash/field sets, progress field sets, byte-identical compatibility file, required report headings,20MB cap and two-line STATUS; it hashes and reads back all artifacts. Rolling WORKLOG/LEARNED are updated. Independent review, shared adoption, supervisor repository copying, brain ingestion and remote mirrors remain unverified. No git, mail, deletion, brain-content mutation, trading access or other-agent research mutation. Administrative checklist working command returned exit0 without text; closure receipt saved separately. All mathematical jobs finished; existing work untouched.

## Universal bridge

C019 stopping-tree payment gains an exact criticality-dependent repair-density obstruction for ALL original proper tensor-subproduct partitions, plus a signed full-terminal reserve bound and a sharp1/8 guard showing why one-factor eligibility cannot replace larger-child eligibility. Universal constant gain is zero. General critical sources may lie outside all useful violating-factor neighborhoods, and Pi remains unpaid there. NEXT uses genuinely eligible full terminals to select one original block on that residual class, the missing universal implication rather than another primitivity or phase-normalization test.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text(f'STATE: Stage21 saved: critical tensor repair-density theorem;sharp1/8 original-fibre guard;A054 full Pi bank independently reconstructed;{total} exact checks PASS;FEI OPEN.\nNEXT: Use ALL proper-subproduct repair constraints and exact nonnegative smaller-child reserves to select ORIGINAL high-K block beyond these neighborhoods;retain Pi/old debit;A090/A094 review.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n2026-10-26 stage21 ({R.name}): derived critical full-fibre repair density and signed-bank lower bound; sharp1/8 XOR guard repairs factor fibres but exposes larger violating terminal. A054 analytic Pi ledger independently holds. {total} exact assertions PASS on two implementations. {lean_status}; FEI open; universal original-block supplier remains unpaid.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage21: If G is a genuine least-essential-dimensional positive K-witness and differs by density delta from a coordinate product, every proper factor subproduct h forces delta>=rho_K(h), its exact distance to H<=KI. Full fibres are disjoint: at least q-floor(R/r) violate. With mu=min deficit below r and m retained bits, E D>=mu-(mu+Km)min(1,delta/rho), retaining negative siblings. Three-bit point-defect K2 radius1 gives sharp1/8 for original factor fibres; XOR-edit tensor family repairs them all yet G3 exposes violating proper child -G2. Thus eligibility of only factor fibres is insufficient; r0 gives no obstruction. A054 phase bank requires Pi even when the rematched row is paid.\n')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']: assert '## '+field in report
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipts=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in files+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]
save('out/PERSISTENCE_RECEIPT.json',dict(protocol_fields_verified=True,compatibility_byte_identical=True,total_exact_checks=total,files=receipts))
for x in receipts: assert sha(Path(x['path']))==x['sha256']
print(json.dumps(dict(status='COMPLETE_LOCAL',exact_checks=total,run=str(R),lean=lean_status,receipt_files=len(receipts))))
