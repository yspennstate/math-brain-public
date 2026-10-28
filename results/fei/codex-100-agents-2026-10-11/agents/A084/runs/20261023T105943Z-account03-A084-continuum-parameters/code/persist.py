"""Source-bound protocol persistence and local receipts, inside A084 only."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
R=Path(__file__).resolve().parents[1];BASE=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=read(protocol_path)
v=read(R/'out/VALIDATION.json');extension=read(R/'out/RATE_EXTENSION.json')
audits=[read(R/'out'/f'AUDIT_d{i}.json') for i in range(3)]
assert v['main']=='PASS' and extension['status']=='PASS' and all(z['direct_physical_audit']=='PASS' for z in audits)
total=v['assertions']+sum(z['assertions'] for z in audits)+extension['exact_assertions']
assert total==241331
source={'claim_id':'A072-LOCAL-HULL-ADMISSION-DAMAGE-UNBOUNDED','version':1,'statement_sha256':'794f189e73fe133d5fc29f5b18d26f19a6e0a929999f900f76ccf9cf24875f3b'}
seed={'claim_id':'A084-SAME-CREDIT-TWO-CORE-CONTINUATION','version':1,'statement_sha256':'55c7c1651b72ecb1d203f529f289ad9c72fe6fe3a29b6d166c3bc665129dc203'}
review=dict(source,verdict='HOLDS_GENERIC_CAPITAL_SUBSTATEMENT',reviewer='A084',independent_reconstruction=True,
 scope='The exact max-arrival-path/current-local-hull capital recurrence and its distinction from the expected stopping hull. Reconstructed by induction and audited on6 small guard/parity cases. The source all-d rate1 family and all<=3-bit all-rate theorem were read but not independently replayed here.',
 evidence=['PROOF.md sections3,5','code/audit.py','out/AUDIT_d0.json','out/AUDIT_d1.json','out/AUDIT_d2.json'],repair_supplied=False)
put(R/'out/REVIEW_A072.json',review)
statement=(
 'For every fixed real K>0, let R_K(f) be the full physical stopping hull with payoff '
 '(H(f)-K I(f))_+, and let T_K(f) be the least initially supplied credit solvent at '
 'every future admission/query/stop arrival when initial admitted set is empty, '
 'admissions preserve actual credit, and every physical query uses the CURRENT '
 'admitted-set hull allocation a_b=a+rho_M(child_b)-mean rho_M(children). '
 'There is a finite dimension-independent L>=0 with T_K(f)<=L R_K(f) for all '
 'uniform Boolean f if and only if H(f)<=K I(f) for all uniform Boolean f. '
 'Explicitly, any finite seed f on n bits with A_K=H(f)-K I(f)>0 gives actual '
 'Boolean G_d(s,x,z)=chi_r(z)*[f(x) if s=0^d else+1], with r an integer satisfying '
 'K r>=n+3, for which T_K(G_d)>=A_K while 0<R_K(G_d)<=4*2^(-d)*(n+2d+2) '
 'for every integer d>=3. In particular, use the24-bit f=J(-1,+1,g,g,g,g), '
 'g negative on{0,1,2}, h negative on{0,1,2,4,8,16,32,6,17,40}, '
 'J(x)=-h(x xor1), bit1 meaning sign-1, all four g blocks disjoint. With r=7, '
 'uniformly for EVERY real K in the closed interval[4,33/8], '
 'T_K(G_d)>1/256 and 0<R_K(G_d)<=4*2^(-d)*(26+2d) for d>=3. '
 'At d=20 this is an actual51-bit accounting witness. The auxiliary activation '
 'entropy profile is analytically bounded on all real delta in[0,1/4], with '
 'zero limit at delta=0; actual physical guards have delta=2^(-d). The rare '
 'positive-arrival capital bound does not extend to the zero-reach face, where '
 'the function is parity and both capitals are0. This does not disprove FEI: '
 'H(G_d)/I(G_d) tends0.'
 )
hypotheses=[
 'Uniform finite cubes, mutually disjoint seed/selector/parity coordinates, Boolean +/-1 truth tables, entropy in bits and total physical influence.',
 'The prescribed allocator uses the exact CURRENT admitted-set stopping hull. Stop, singleton admissions and all physical queries are allowed; no fresh credit is added on admissions.',
 'Solvency is required at every positive-reach arrival, keeping actual inherited credit. Credit owners are nonnegative and old debit labels may be signed with nonnegative total.',
 'The generic equivalence assumes K>0; the explicit constant lower bound assumes K in[4,33/8]. K=0 and zero-reach branches are not silently included.',
 'All credits discussed are already supplied/booked; the theorem does not produce an unused influence-funded donor or change old terminal bills.'
]
digest=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hypotheses},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
claim={
 'claim_id':'A084-RATE-CONTINUUM-LOCAL-ADMISSION-OBSTRUCTION','version':1,
 'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':digest,
 'contributors':['A084'],
 'proof_source':['PROOF.md','code/certify.py','code/audit.py','code/extend.py','out/SEED_CERTIFICATE.json','out/RATE_EXTENSION.json','out/EXPLICIT_WITNESS.json'],
 'proof_dependencies':[dict(source,acceptance='GENERIC_SUBSTATEMENT_INDEPENDENTLY_RECONSTRUCTED',scope=review['scope']),dict(seed,acceptance='SEED_H_AND_I_INDEPENDENTLY_RECONSTRUCTED',scope='Only the complete actual seed Fourier entropy/influence, recomputed with literal coefficient groups and matched to centered-sector computation; no dependency on its pending two-core financial acceptance.')],
 'review_records':[],
 'status':'AUTHOR_PROOF_AND_EXACT_CONTROLS_INDEPENDENT_REVIEW_PENDING',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'None within the stated accounting obstruction and equivalence. FEI itself and an influence-paid coherent full-universe envelope at a suitable absolute rate remain open.',
 'next_consumers':['A072','A071','A075','A080','A089','A074','A092','B17','B20']
}
put(R/'CLAIMS.json',[claim])
next_action=('A072/A074/A092 independently reconstruct the all-K Boolean guard reduction and rate4 endpoint. A071/A075/A089 must replace root-hull top-ups by a coherent envelope whose INITIAL price is paid from the actual unused original influence account, retaining old owners and both complete terminals.')
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B17','packet_id':'A084',
 'gap_id':'A084-INHERITED-PHYSICAL-CORE-PAYMENT','attempt_id':'stage8-rate4-continuum-admission-obstruction',
 'method':'Exact factored Boolean Walsh reconstruction; rare physical activation and disjoint parity; finite max-arrival capital induction; analytic compact-rate and zero-reach reductions.',
 'mathematical_delta':'Root-hull constant-factor admission shortcut fails uniformly on ALL real K in[4,33/8]; actual51-bit witness and all-d family. For each K>0, bounded local-admission amplification is equivalent to fixed-rate full FEI. A072 generic capital substatement independently reconstructed; original four-core fixture remains closed.',
 'deliverable_status':'COMPLETE_LOCAL',
 'mathematical_status':'SCOPED_ACCOUNTING_OBSTRUCTION_AND_EQUIVALENCE_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':[source,seed],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':digest}],
 'source_artifacts':['REPORT.md','PROOF.md','FROZEN_SPEC.json','EXTENSION_SPEC.json','out/SOURCE_PINS.json','out/REVIEW_A072.json','out/SEED_CERTIFICATE.json','out/VALIDATION.json','out/RATE_EXTENSION.json','out/BIAS_FACES.json','out/AUDIT_d0.json','out/AUDIT_d1.json','out/AUDIT_d2.json','out/MANIFEST.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Independent external reconstruction of the new all-d/all-rate obstruction remains pending.','Universal FEI and the noncircular influence price of a coherent full-universe envelope remain unproved; local-hull top-up reduction cannot bypass them.','Supervisor GitHub/brain mirror unverified; personal-model/state/dream context remains stale and unused as evidence.'],
 'packet_ids':['A084']
}
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in required['progress_fields']}
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
report=f'''# A084: a compact rate region with an actual admission obstruction

## exact target, quantifiers, hypotheses and units

Uniform Boolean functions; Fourier entropy in bits. Close the all-real rate domain, not a rate grid, for a precise failure of the CURRENT-local-hull allocator. For every K in the CLOSED REAL interval[4,33/8], actual G_d on d+31 physical bits has robust sequential-admission capital T_K(G_d)>1/256 while its global stopping hull satisfies0<R_K(G_d)<=4*2^-d*(26+2d)->0. At d=20 an explicit51-bit witness already has global reserve below1/256. The exact truth definition and whole seed are in PROOF.md. Full FEI remains OPEN: this family's ordinary H/I tends0, not infinity.

The stronger generic result holds at EVERY real K>0: existence of a dimension-independent finite L with T_K<=L R_K for all Boolean functions is EQUIVALENT to full FEI with that SAME rate K. No arbitrary admission allocator is ruled out; the specified current-local-hull rule and actual old credit are essential hypotheses.

## sources actually read, revisions and theorem locators

Read current BOARD.md, unchanged B17 lead v2, own STATUS/LEARNED and stage7 proof/engine/certificate; A08020261023T043938Z REPORT/PROOF (all four cores closed), A07220261023T060838Z REPORT/PROOF/CLAIMS (rate1 local-admission damage), A075/A089 current STATUS and board entries, machine-wide AGENTS and execution protocol {protocol['revision']}. Source bytes are pinned in out/SOURCE_PINS.json. Earlier campaign/paper intake is background, not a new theorem premise. One paired read-only math recall returned weak nearby cards, none used. B17's original AND sign-map task was closed earlier; protocol dispatch instead consumes A072's useful new obstruction and A080's closure, avoiding duplicate third-core work.

Brain wake completed for this session but self-care is degraded: owner-model97.4h, state notes82.0h and last dream32.7h stale at intake. Their personal-context reliability is affected; they are excluded from mathematical premises.

## complete derivation or exact first unsupported line

PROOF.md supplies the complete guard/parity truth-table construction and exact character inverse/Parseval identity, independent physical edges, full entropy formula, all-real auxiliary bias bounds with delta=0 treated separately, and the compact rate endpoint reduction. A parity block keeps EVERY selector-only restriction solvent, hence every original local-hull allocation increment is0. On the rare positive-reach selector path a later admission exposes the same negative seed deficit. Initial actual credit cannot be retroactively reallocated or drawn again from the donor. The global hull is at most Fourier entropy, which tends0 under rare activation. This proves the all-d obstruction. Applying it to any hypothetical seed with H>KI proves the generic fixed-K equivalence; if FEI holds at K then all local payoffs/hulls/capitals are0.

All rates in[4,33/8] are covered by the affine seed deficit and a strict exact endpoint sign. The first conservative domain[4,4097/1024] used I<=24. It was widened only after independent reconstruction gave exact I=98637/524288, allowing the stronger endpoint; EXTENSION_SPEC and RATE_EXTENSION preserve the reason and check. No change of seed or accounting convention occurred. The auxiliary entropy profile is controlled for ALL real delta in[0,1/4], but only dyadic deltas are asserted to be uniform Boolean guards. At delta=0 the rare branch disappears and T=R=0: there is no false extension of the positive-reach lower bound to that face.

First unsupported universal line: construct and initially pay a coherent full-universe envelope at a suitable absolute rate from actual unused influence resources, retaining old owners and full terminal functions. The reduction identifies a circular shortcut rather than proving FEI.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC and EXTENSION_SPEC preceded their respective computations. Commands from this run: python -B -X utf8 code/certify.py --pilot; certify.py; audit.py0, audit.py1, audit.py2 (with a space before the integer argument); extend.py; persist.py. The pilot passed239957 assertion calls in28.86896s. Main seed/family run passed240100 recorded calls in41.31691s:50,625 literal coefficient groups cover all16,777,216 actual Fourier atoms, exactly matching the different centered occupied-sector engine for complete H and I. It checks51 fixed width/rate controls and four bias faces. These finite controls do not establish the all-d or continuum theorem; the analytic proof does.

The separate direct-character/physical-edge augmented-DAG audit covers d=0,1,2, rates1 and3/2, at most6 physical bits. It passed163,356,709 assertion calls in0.01032,0.30755,0.31059s. Every selector-only arrival has zero local hull, original credit stays unchanged, and the complete seed deficit survives both parity revelations. The widened endpoint passed3 exact checks in0.05998s. Total nonpilot RECORDED assertion calls: {total}; these are not distinct functions. Arithmetic uses Fraction/integer profiles, exact prime-log cancellation and outward192-bit80-term atanh log bounds with a proved tail. No floating sign decides any claim. Memory estimates<=120MB; all jobs finish below55s, no >300MB job, GPU, remote compute, detached worker, automatic dimension escalation or process shedding. No Lean check was attempted or claimed for this analytic proof.

## proof dependencies and changed downstream conclusions

A072-LOCAL-HULL-ADMISSION-DAMAGE-UNBOUNDED@1, hash {source['statement_sha256']}, independently HOLDS at the GENERIC capital-recurrence substatement only (out/REVIEW_A072.json). Its source rate1 all-d family was read, not independently replayed. The complete seed H/I from A084-SAME-CREDIT-TWO-CORE-CONTINUATION@1, hash {seed['statement_sha256']}, is independently recomputed and matched; no assumption of pending two-core financial acceptance is used. The new result supplies a rate4-and-above ACTUAL Boolean obstruction and all-positive-rate reduction. It does not reopen or refute A080/A071's separately certified four-core fixture, which checked the actual admission accounts rather than inferring them from root equality. Old labels, actual reaches, both complete terminals and already spent donor accounting remain explicit. This is a narrow source-bound reconstruction/obstruction, not a new proposed universal proof candidate.

New claim {claim['claim_id']}@1, statement hash {digest}: source-complete author proof and exact controls; independent external acceptance pending.

## one next mathematical action and independent reviewer

{next_action} The review should attack the selector-only uniform solvency bound, the seed endpoint sign, full entropy superharmonicity, actual parity revelation, and the distinction between a tiny expected reserve and every positive-reach arrival.

## actual persistence receipts or precise save blocker

All research outputs are local to this A084 run. The four protocol files have exact required fields and byte-identical progress/delta content; out/MANIFEST.json records SHA256/size checks. STATUS has two lines and WORKLOG/LEARNED append this stage. Required session wake/checklist receipts are handled by their supplied system helpers; no shared research index, peer folder, brain store or repository was edited. No git, mail or peer message was sent. Supervisor mirroring and independent acceptance remain unverified. out/FINAL_PERSISTENCE_CHECK.json records the final local audit and completion receipt; it and the manifest itself are excluded from circular manifest hashing. Every mathematical command completed and no worker was left running.

## Universal bridge

C019 stopping-tree payment and C024 history transfer advance by an explicit all-dimensional Boolean obstruction UNIFORM over the compact REAL rate interval[4,33/8], not a grid: global reserve tends0 while actual current-local-hull admission needs more than1/256 bit. The generic guard reduction further proves that bounded root-hull-to-local amplification at any fixed K>0 is already EQUIVALENT to FEI at that same K. No universal constant or influence-paid initial bank is obtained. The unpaid step is a coherently allocated full-universe envelope whose initial price comes from the original unused influence account. NEXT addresses that exact noncircular supplier with old owners and full terminals retained, rather than repeating the closed four-core fixture or another isolated function-class estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
for field in required['report_fields']:assert '## '+field in report
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
(BASE/'STATUS.md').write_text('STATE: Stage8 saved: actual all-d local-admission damage unbounded uniformly K in[4,33/8]; bounded amplification iff fixed-rate FEI;241331 recorded exact checks; review pending; FEI OPEN.\nNEXT: A072/A074/A092 review guard reduction and endpoint; pay coherent full-universe INITIAL envelope from SAME unused influence account with old labels/full terminals.\n',encoding='utf-8')
with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23 10:59 UTC stage (20261023T105943Z): A080/A071 already close the four-core fixture; consumed A072 new rate1 admission obstruction rather than duplicate the saved third-core NEXT. Proved generic guard-and-parity reduction for every K>0: bounded local-admission amplification iff same-rate full FEI. Recomputed24-bit seed via50625 literal coefficient groups covering2^24 atoms and matched centered-sector H/I. Actual G_d with7 parity bits gives uniform capital>1/256 but vanishing global hull at ALL real K in[4,33/8]. Initial conservative[4,4097/1024] enlarged using exact I=98637/524288, not a changed seed. Explicit51-bit witness; zero-reach face treated separately;241331 nonpilot recorded exact assertions. Source generic A072 capital substatement independently HOLDS; new result external review pending. Local saves verified; mirror unverified; no formal verification, git or workers.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23: For ANY real K>0 and any Boolean seed f with H(f)>K I(f), rare physical activation U_d followed by disjoint parity chi_r, K r>=n+3, forces current-local-hull sequential admission capital>=H(f)-K I(f), while full stopping hull<=H(U_d)<=4*2^-d*(n+2d+2)->0. Hence finite dimension-free T_K/R_K bound for all Boolean functions is equivalent to FULL FEI at SAME K; a fixed-factor top-up is a circular shortcut. With actual24-bit Fplus seed, exact I=98637/524288 and r=7 certify ALL REAL K in[4,33/8] at capital>1/256. At d20 this is a51-bit accounting witness, NOT an FEI counterexample (ordinary H/I tends0). At literal zero-reach delta0 both capitals0; do not extend positive-arrival bound to that face. Proof/certificate: runs/20261023T105943Z-account03-A084-continuum-parameters. Independent review pending.\n')
manifest={'protocol_revision':protocol['revision'],'schema_checks':'PASS','claim_statement_sha256':digest,'statement_hash_convention':'SHA256 compact sorted utf8 JSON of exact_statement and hypotheses','nonpilot_recorded_assertions':total,'independent_review':'PENDING','mirror_verified':False,'files':[]}
for p in sorted(R.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in ['MANIFEST.json','FINAL_PERSISTENCE_CHECK.json']:continue
 assert p.stat().st_size<20*1024*1024,p
 manifest['files'].append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
put(R/'out/MANIFEST.json',manifest)
print(json.dumps({'claim':claim['claim_id']+'@1','statement_sha256':digest,'files':len(manifest['files']),'schema':'PASS','recorded_assertions':total}))
