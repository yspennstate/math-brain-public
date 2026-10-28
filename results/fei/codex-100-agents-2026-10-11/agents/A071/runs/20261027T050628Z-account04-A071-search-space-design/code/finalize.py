from pathlib import Path
import datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
main=read(R/'out/RESULT.json'); audit=read(R/'out/AUDIT.json'); pilot=read(R/'out/PILOT.json')
assert main['status']==audit['status']==pilot['status']=='PASS'
assert main['counts']['functions']==552 and main['counts']['blocks']==21348
receipt=read(R/'out/LEAN_RECEIPT.json')
source=Path(r'agents\A080\runs\20261027T015619Z-account04-A080-universal-counterexample-standard')
c=read(source/'CLAIMS.json')['claims'][0]
review=read(R/'out/REVIEW.json')
# Raw UTF8 statement convention is used by this producer (A080), as checked here.
assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
review['verified_hash_convention']='sha256(raw UTF8 exact_statement)'
review.pop('canonical_hash_reconstruction',None)
write(R/'out/REVIEW.json',review)
c['review_records'].append(dict(reviewer='A071',verdict='HOLDS_UNCHANGED',source=str(R/'PROOF.md'),antecedent_disclosure='A071 supplied the prior row criterion; no repair of the A080 version was made'))
c['status']='INDEPENDENT_RECONSTRUCTION_HOLDS_UNCHANGED'
statement='For every Boolean sign seed g on n>=1 uniform bits and k>=2 fresh bits, F(x,z)=g(x)(-1)^[wt(x,z)<=1] has exactly three distinct residual rows on the entire fresh block. Its minimum sum of total physical influences over all valid TWO-Boolean-output summaries of that block is exactly k^2*2^(1-k), attained by the signs of 1[wt(z)>=1] and 1[wt(z)>=2]. The separate indicators u=1[z=0],v=1[wt(z)=1] give an exact correlated three-state representation, with I(1-2u)+I(1-2v)=k(k+1)*2^(1-k); their activity-weighted bill exceeds actual fresh physical influence k(n+k-1)*2^(1-n-k) by exactly2k*2^(1-n-k). For every delta>0, the supremum of H(F)/I(F) over these composition-prime constructions with H(1-2u)+H(1-2v)+I(1-2u)+I(1-2v)+H_input(u,v)<delta is exactly C_FEI in the extended reals. No universal initial payment or divergent seed family is supplied.'
new=dict(claim_id='A071-PRIME-CHEAP-TWO-OUTPUT-SUMMARY',version=1,exact_statement=statement,hypotheses=['uniform physical cube; actual Boolean signs; all coordinates retained','n>=1,k>=2; complete squared Fourier entropy in bits','summary outputs are arbitrary functions of the fresh block only and reconstruct F with outside coordinates raw','nonconstant seed for ratio approximation; delta>0; C_FEI is unrestricted extended-real H/I supremum'],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A071; A080 and concurrently A075 arbitrary-seed prime perturbation are credited antecedents'],proof_source=str(R/'PROOF.md'),proof_dependencies=['A080-COMPOSITION-PRIME-APPROXIMATION@1; independently reconstructed unchanged here','elementary residual-row criterion, physical edge counting and finite entropy support bound'],review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['Proposed strategy-level extension: scalar composition-primality rules out proper two-output compression (not attributed to A080)'],first_unproved_line=None,next_consumers=['A075','A080','A084','A089','A092','B20'])
write(R/'CLAIMS.json',dict(claims=[c,new]))
prog=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B15',packet_id='A071',gap_id='B15-ORIGINAL-ARBITRARY-CORE-INITIAL-SOURCE',attempt_id='stage22-three-state-summary',method='Independent row/coupling reconstruction and exact bounded Boolean falsification domain; sharp two-output boundary cost',mathematical_delta='A080@1 HOLDS unchanged; cheap optimal TWO-output summary costs k^2*2^(1-k) yet retains full FEI supremum. Exact120 encodings/40 entropy controls supplement552 constructions/21348 blocks. No O(I) source supplied.',deliverable_status='COMPLETE_LOCAL',mathematical_status='ANALYTIC_REDUCTION_AND_SHARP_SUMMARY_COST; FULL_FEI_OPEN; NEW_CLAIM_REVIEW_PENDING',claim_versions_used=['A080-COMPOSITION-PRIME-APPROXIMATION@1','A071-PRIME-BALL-PROPER-PARTITION-OBSTRUCTION@1 (antecedent only)'],claims_created_or_changed=['A080-COMPOSITION-PRIME-APPROXIMATION@1 review only','A071-PRIME-CHEAP-TWO-OUTPUT-SUMMARY@1'],source_artifacts=['PROOF.md','out/REVIEW.json','out/SOURCE_INTAKE.json','FROZEN_SPEC.json','AUDIT_SPEC.json','out/RESULT.json','out/AUDIT.json','out/LEAN_RECEIPT.json'],next_consumers=['A075','A080','A084','A089','A092','B20'],next_action='Require a noncircular ORIGINAL source for the arbitrary retained OUTER seed on this correlated three-state interface; retain old debits and BOTH full terminals. A080/A092 review sharp output-boundary cost.',stagnant_substantive_attempts=0,blockers=['Universal initial O(I) source remains unpaid','New corollary independent review pending','Supervisor/private mirrors unverified'],packet_ids=['A071'])
write(R/'PROGRESS.json',prog);write(R/'PACKET_DELTA.json',prog)
stamp=dt.datetime.now(dt.timezone.utc).isoformat()
formal_status=receipt.get('result',{}).get('status',receipt.get('status','UNVERIFIED'))
report=f'''# A071 stage22: cheap multiple-output summaries retain the arbitrary seed

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. Independently audit A080-COMPOSITION-PRIME-APPROXIMATION@1 and define a bounded actual Boolean family testing its row obstruction and a multiple-output escape. For every n>=1,k>=2, F=g times the radius-one ball sign has exactly three fresh-block residual rows. The optimal sum of physical influences of TWO summary outputs is k^2 2^(1-k). Even requiring arbitrarily small summary entropy/influence retains the full FEI supremum. H means complete squared Fourier entropy in bits; input Shannon entropy is explicitly distinguished.

## sources actually read, revisions and theorem locators

Read machine AGENTS, execution protocol v2 in full, campaign README/status/registries/packet/stream/plan, supplemental campaign/claims/counterexamples/seed/native files and sources, earlier campaign report runs, all four supplied paper text versions, current BOARD, B15 v2 lead notes, own STATUS/LEARNED/WORKLOG and previous REPORT. Intake pins are in out/SOURCE_INTAKE.json. The board is newer than the original registries and identifies the actual current target; the stale n5 dispatch is already closed. Specific proof dependency: A080 latest PROOF, CLAIMS, REPORT, digest {c['statement_sha256']}; PROOF section1 reconstructs the entire row/continuity/bank chain. A075 latest REPORT independently gives the same reduction with three fresh bits; A080 already improves it to two. No new claim to that reduction is made here. Threshold composition/activation and percolation singularity locators are background only. One three-wording math recall returned neighboring Booleanity/FEI cards, no answering row-summary proof, and no card is a premise.

## complete derivation or exact first unsupported line

PROOF section1 independently reconstructs the three exhaustive cuts, checks the N=8(n+m+2) approximation schedule, positive denominators, nonnegative-numerator case, finite coupling entropy and exact singleton bank consequence. A080's statement HOLDS unchanged; A071's earlier row-criterion authorship is disclosed. Section2 gives the exact three-state factorization and negative covariance. A physical boundary lower bound proves the optimal two-output cost even for non-row-constant encodings. The simple u,v representation costs k(k+1)2^(1-k); the optimal chain encoding costs k^2 2^(1-k). The difference is a change of encoding, not number drift. The weighted u,v bill overcounts actual fresh physical influence by exactly2k2^(1-N), because two outputs flip and cancel at x=0. Section3 proves the arbitrarily cheap-summary supremum remains C_FEI by fixed-seed approximation. The first unsupported full-FEI line is a noncircular ORIGINAL influence-priced source for the retained arbitrary OUTER seed, including the correlated state, old debits and both full terminals. No universal source is obtained.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC and helper preceded the pilot. All labelled n1..3 seeds, k2/3, constants/dummies/complements retained; no symmetry quotient. Pilot20 constructions/172 blocks/{pilot['counts']['assertions']} predicates in {pilot['seconds']:.6f}s. Main552 constructions/21348 proper blocks/25440 direct Fourier atoms/{main['counts']['assertions']} exact assertions in {main['seconds']:.6f}s. Direct character sums independently match integer FWHT; direct physical edges match every spectral influence. Two missing-fresh-bit witnesses have two rows and are preserved as hypothesis controls. Separate AUDIT_SPEC preceded all120 injective row encodings on k2..6 and40 actual entropy/TV cases: {audit['assertions']} assertions PASS in {audit['seconds']:.6f}s. Exact Fraction logarithms use a40-term positive atanh series with explicit geometric remainder and power-two reduction; no floating sign decision. The analytic boundary lower bound covers arbitrary summaries beyond the finite row-constant encoding census. Commands: python -B -X utf8 code/verify.py --pilot; code/verify.py; code/audit.py; code/intake.py; code/finalize.py.

The finite Lean theorem encodes the four-row sign alternative only. Receipt status: {formal_status}; see out/LEAN_RECEIPT.json for exact target/compiler/axioms or admission failure. The whole analytic theorem is not represented as Lean-checked. Fresh memok returned0 before the formal attempt; compiler memory cap1024MB,45s; every exact Python check estimated80MB with55s cap. No heavy search, GPU, dimension escalation, remote or detached work. A first read-only intake attempt incorrectly tried cp1252 for UTF8 source files and failed on byte0x9d; the corrected intake tries strict UTF8 first and cp1252 only on actual failure. No source corruption was inferred. A hook initially blocked the explicit-UTF8 receipt command for an acknowledgment; the same command was acknowledged and reissued. Both are setup/provenance events, not mathematical failures.

## proof dependencies and changed downstream conclusions

A080@1 is independently reconstructed unchanged; its own source excludes multiple-output summaries. New A071-PRIME-CHEAP-TWO-OUTPUT-SUMMARY@1 is a narrow analytic corollary with exact controls, independent review pending. The n1,k2 family refutes the proposed stronger strategy statement that scalar primality forbids two-output compression; that statement is NOT attributed to another agent. The stronger useful conclusion is that compression of the huge fresh block and arbitrarily cheap summary outputs still leave unrestricted FEI in the outside seed. Product-bias composition is unavailable because the outputs have a three-point correlated law. No bank coherence, debit-sign repair, scalar reserve or FEI theorem is refuted.

## one next mathematical action and independent reviewer

A080/A092 review the exact minimal influence encoding and arbitrary-summary lower bound; A075/A084/A089 test an ORIGINAL outer-source payment on this three-state interface. A theorem must pay the retained arbitrary seed rather than just the tiny fresh summary. Consumers are named in saved artifacts; no message delivery or adoption is claimed.

## actual persistence receipts or precise save blocker

Saved locally at {stamp}. REPORT, CLAIMS, PROGRESS, PACKET_DELTA, complete proof, frozen specs, code, outputs and source pins are inside the designated A071 run; out/PERSISTENCE.json checks exact protocol fields, raw statement hashes, source stability, equal progress/delta bytes, file sizes and two-line STATUS. Rolling WORKLOG/LEARNED append this result. Supervisor mirroring and downstream use remain unverified. No git, email, peer message, shared ledger/brain/index write, trading access, deletion or process shedding. The required wake reported stale personal model/state/dream notes; alert was delivered, and they are excluded from premises. Compute snapshot was ok but disk8.7GB free; this stage adds only small artifacts. No own research job remains after finalization.

## Universal bridge

This stage advances the C019/C024 initialization obstruction by accepting A080's arbitrary-seed prime reduction and sharply pricing a MULTIPLE-output escape: two outputs suffice, their optimal total influence is k^2 2^(1-k), and their complete entropy and input-state entropy can all tend to zero while the ordinary FEI supremum stays exactly unrestricted C_FEI. The fresh-block compression is real; the missing ORIGINAL O(I) source for the arbitrary retained outer seed is still unpaid. NEXT targets that source with the correlated three-state law and exact cancellation retained, because merely introducing more summaries or optimizing their influence cannot remove the full-FEI seed already present at state(0,0).
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(A/'STATUS.md').write_text('STATE: A071 stage22 saved: A080 prime approximation HOLDS; optimal TWO-output fresh summary I=k^2*2^(1-k), cheap summaries retain full FEI supremum;81070 main/audit exact assertions PASS;FEI OPEN.\nNEXT: A080/A092 review sharp encoding;A075/A084/A089 fund ORIGINAL arbitrary OUTER seed on correlated three-state interface,old debits/BOTH full terminals;no scalar-partition or cheap-summary reset.\n',encoding='utf-8',newline='\n')
entry=f'\n{stamp} stage22 {R.name}: A080 arbitrary-seed row/coupling/bank theorem reconstructed unchanged; antecedent authorship disclosed. New exact optimal TWO-output summary influence k^2*2^(1-k); simple u,v bill k(k+1)*2^(1-k), excess physical activity bill2k2^(1-N). All552 constructions/21348blocks/80865 assertions and120 encodings/40 entropy cases/205 assertions PASS. Arbitrarily cheap summaries retain exact full FEI supremum; retained outer seed unpaid. Formal status {formal_status}; no full Lean certification claim. Brain stale alert delivered; research writes only A071, mirrors unverified.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(entry)
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write(entry+'For the radius-one prime perturbation, the whole fresh block has exactly3 rows. Codes00,10,11 attain the lower bound from k zero-to-one plus k(k-1) one-to-two edges, even against arbitrary non-row-constant two-output summaries. Correlated state support is3, not a product law. Tiny summary cost does not pay the arbitrary outside seed.\n')
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
expected=set(protocol['progress_fields']); expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(prog)==expected
for claim in [c,new]:assert set(claim)==set(protocol['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for item in read(R/'out/SOURCE_INTAKE.json'):assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256']
manifest=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        manifest.append(dict(path=str(p.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
write(R/'out/PERSISTENCE.json',dict(saved_at=stamp,status='PASS',protocol_keys='exact',sources_stable=True,progress_delta_identical=True,files=manifest,remote_mirror='UNVERIFIED'))
print(json.dumps(dict(status='PASS',files=len(manifest),formal_status=formal_status,main_assertions=80865,audit_assertions=205)))
