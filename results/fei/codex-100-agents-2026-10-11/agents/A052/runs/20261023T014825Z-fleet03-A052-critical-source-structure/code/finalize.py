from pathlib import Path
import json,hashlib,datetime,subprocess,sys
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
B=Path(r'~\brain_workers\FEI100_20261011')
P=Path(r'math-open-problems/reports\fei-2026-10-11')
def put(p,t): p.write_text(t,encoding='utf-8',newline='')
def js(p,d): put(p,json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
main=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
ind=json.loads((R/'out/INDEPENDENT.json').read_text(encoding='utf-8'))
assert main['status']==ind['status']=='PASS'
assert main['checks']==3677 and ind['checks']==718
total=main['checks']+ind['checks']; stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
proof=(R/'RANK_PAIR_PROOF.md').read_text(encoding='utf-8')
needle='This includes the exceptional empty coefficient. All sums are finite.\n'
if 'Summing their h-values' not in proof:
    assert proof.count(needle)==1
    proof=proof.replace(needle,needle+'''Indeed, at every nonzero data label s all control labels carry amplitude
p*Ghat(s); at data label zero the nonempty control amplitudes are
-p(1-mu), and the empty one is1-p(1-mu). Summing their h-values gives
the displayed formula: the nonzero data terms contribute
p[H-h(mu)]+2kp(1-mu^2), and the nonempty control-only terms contribute
p(1-p)h(1-mu)+2kp(1-p)(1-mu)^2.
''')
needle='line is unavailable; the previous A052/A055 path families have negative\nphysical child banks.'
if 'Physical ratio criticality alone does not license' not in proof:
    assert needle in proof
    proof=proof.replace(needle,needle+''' Physical ratio criticality alone does not license
the transformed children: it gives S_A>=0, while S_E,A=S_A-K*rho_E,A
may be negative. The stronger least-dimensional fixed-K selector is
used precisely to license these smaller Boolean affine images.''')
needle='time elsewhere. This is a local theorem, not FEI(15/4).'
if 'physical-only query is strictly unpaid' not in proof:
    assert needle in proof
    proof=proof.replace(needle,needle+''' In fact the
physical-only query is strictly unpaid at15/4: (5) has L_A>(15/4)p,
because h(3/4)>0, p(1-p)>0 and Delta>=0. The actual non-character
refund changes this SAME original pair from unpaid to paid.''')
put(R/'RANK_PAIR_PROOF.md',proof)
review='''# Scoped independent reconstruction of A051 reset accounting

Source A051/runs/20261023T002518Z-fleet03-A051-near-extremizer-definition/RESET_BUDGET.md, A051-FULL-AFFINE-CHILD-RELEASE-BUDGET@1, hash458cfc425aa95401d3f2f68a63f1805f406f31044ab52da1575729b20f09e91d. Reviewer A052. HOLDS without repair for Section2 equation(3), its exact smaller-function eligibility, and Section3 finite adaptive telescope. This does not independently accept the new all-k upper budget or local perturbation bound; those are read context, not premises of the new result.

For each physical branch, the finite affine orbit contains the identity and preserves the entire entropy. Thus a(g)<=I(g), every branch release is nonnegative, and its average rho has exactly S_A-S_Astar=K rho. Averaging the original influence split I=I_A+E I(g) gives D+S_Astar=L_A-K(I_A+rho). No branch is removed and no optimizer over dimensions is invoked. All affine images of a proper child still have dimension at most n-|A|. Only nonviolation of ALL smaller Boolean functions makes S_Astar nonnegative; physical ratio criticality alone does not. The original path-code negative bank remains an essential guard.

At each current chart I(g)=I_A+reset_release+E I(next), while H(g)=L_A+E H(next), because the reset preserves H on that branch. Multiply by original node reaches and sum over the finite tree; each interior term cancels exactly. This proves both telescopes and the final signed-bank identity. No common global chart is assumed. A reset booked at its parent cannot be counted again at a descendant. These are exact finite sums, so there is no unjustified independence or limit exchange.

The current independent physical tensor checker tests the actual input shear and original reaches rather than reading recorded reset amounts. It verifies all four complete terminal entropies, the measured influence release, and the whole signed bank at15/4, retaining three independent cores. This is new targeted validation, not adoption of A051's census count. The prior minimum-basis characterization remains accepted at its preceding A052 review scope.
'''
put(R/'REVIEW_A051.md',review)
dep={'claim_id':'A051-FULL-AFFINE-CHILD-RELEASE-BUDGET','version':1,'statement_sha256':'458cfc425aa95401d3f2f68a63f1805f406f31044ab52da1575729b20f09e91d','acceptance':'A052 independent scoped HOLDS: Section2 equation3 and eligibility; Section3 telescope only'}
stmt='For any finite d-bit Boolean sign g, let E contain all coordinate parity vectors, m(v)=min(P(v dot S=1),1-P(v dot S=1)), r_E(t)=rank_F2{v in E:m(v)<=t}, N(t)=#{j:m(e_j)<=t}, and chi=sum_j(2Inf_j(g)-1)_+. Its minimum influence a_E over parity bases from E and translations equals integral_0^(1/2)(d-r_E(t))dt, and the actual affine release equals chi+integral_0^(1/2)(r_E(t)-N(t))dt. This supplies a full-release lower bound and spends overlapping parity gains only once. For every integer k>=2,p=2^-k, Q=(-1)^(ab+ac+bc+za), F_k=1-A_k+A_k Q, the original proper pair(a,b) has I_A=p, exact full affine child release rho_A=p/4 and zero character-only child release. Its complete decrement L_A satisfies (15/4)p<L_A<(595/128)p, so after the explicit one-branch parity reset it is paid at SAME K=15/4 with margin>5p/128. The same query/reset/payment holds after tensoring ANY disjoint Boolean core left untouched in every terminal. The three nonconstant optimized terminals violate K=15/4 for k>=16, so no terminal nonviolation or full FEI follows.'
claim={'claim_id':'A052-RANK-RELEASE-ORIGINAL-PAIR-PAYMENT','version':1,'exact_statement':stmt,'hypotheses':['Uniform finite Boolean signs; entropy bits and normalized real Fourier coefficients','E is a finite set of nonzero parity vectors containing every coordinate vector; d0 allowed','Activation depth k integer>=2; original pair(a,b), all four original reaches1/4','Arbitrary tensor core disjoint from displayed variables and retained untouched','Nonnegative optimized-child banks require all smaller Boolean functions nonviolating, stronger than physical ratio criticality'],'statement_sha256':hashlib.sha256(stmt.encode('utf-8')).hexdigest(),'contributors':['A052'],'proof_source':['RANK_PAIR_PROOF.md','code/check_rank_pair.py','code/independent_tensor.py','out/CHECK.json','out/INDEPENDENT.json'],'proof_dependencies':[dep,'A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1; previously independently accepted; rank formula rederived here'],'review_records':[{'reviewer':'A052','scope':'author analytic audit, independent direct-character and physical shear representation','verdict':'PASS; independent-agent acceptance pending'}],'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[{'claim_id':'EXPLORATORY-SUM-OF-OVERLAPPING-AFFINE-SWAPS','version':0,'exact_false_statement':'Sum all individually beneficial row exchanges as unused child influence release.','witness':'odd-d even-parity spectral hyperplane: true rho=1/2, proposed sum=d/2; actual Boolean realization in proof Section1'}],'first_unproved_line':None,'next_consumers':['A051','A055','A090','A094','B11','B20']}
js(R/'CLAIMS.json',[claim])
next_action='Find one original proper pair on a genuine least-dimensional high-K witness whose quotient-rank increments fund its signed bill from SAME unused S_E,A, retaining mixed T and every terminal; do not sum dependent parity swaps.'
prog={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B11','packet_id':'A052','gap_id':'G-R-SELECT','attempt_id':'stage8-rank-lower-funding-original-pair','method':'Exact rank-layer formula for affine release, independent reset-account review, actual original-pair lower funding with four complete terminals and arbitrary tensor core.','mathematical_delta':'Rank increments give lower funding without overlapping-swap double count. A rare activated bent core has an original pair unpaid physically at15/4 but paid after exact rho=p/4 with margin>5p/128, all k>=2; arbitrary retained core and negative-terminal guard explicit.','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'SCOPED_AUTHOR_PROOF_EXACT_CERTIFICATE; INDEPENDENT_REVIEW_PENDING; UNIVERSAL_SELECTION_AND_FULL_FEI_OPEN','claim_versions_used':[dep],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'new lower-funding interface and original-pair payment fragment'},{'claim_id':dep['claim_id'],'version':1,'change':'independent scoped local-bank/telescope acceptance without repair'}],'source_artifacts':['RANK_PAIR_PROOF.md','REVIEW_A051.md','out/FROZEN_SPEC.json','out/FROZEN_REVIEW.json','out/PILOT.json','out/PILOT_CORRECTION.json','out/CHECK.json','out/INDEPENDENT.json','out/LEAN.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['No universal proper-pair lower rank funding/selection theorem.','Lean scalar endpoint run RUNTIME_UNVERIFIED; no formal certificate.'],'packet_ids':['A052']}
js(R/'PROGRESS.json',prog); js(R/'PACKET_DELTA.json',prog)
report='''# exact target, quantifiers, hypotheses and units

A052/B11 stage8 targets LOWER funding of full affine child release on an ORIGINAL physical pair, beyond affine/weak-source admission. Finite uniform Boolean signs, Fourier entropy bits, all original terminal reaches retained. RANK_PAIR_PROOF Sections1--5 prove an exact rank formula for usable affine release, an actual all-k original-pair payment at SAME15/4, and an arbitrary-core terminal preservation theorem. Full FEI remains OPEN. Current owner deadline23October2026 14:49UTC governs over the older protocol clock.

# sources actually read, revisions and theorem locators

BOARD current B11 rows, unchanged B11 STREAM_NOTESv2 and own STATUS read at stage start. Execution protocol2026-10-11-execution-v2 retained from the preceding complete read; current schema/dispatch/compute fields refreshed. New sources read in full: A05123October00:25UTC REPORT/RESET_BUDGET and A05522October23:36UTC REPORT/PROOF; A051 current CLAIMS read. Own previous path proof and exact-library source revisited. Prior campaign and four manuscript baseline reads are not a fresh paper audit. No new external literature or novelty claim is used. Source paths/hashes are in out/SOURCE_RECEIPTS.json. Wake degraded: owner-model/state notes stale; current instructions govern. The lead's old composition task was completed earlier; consuming new child-budget dependencies follows protocol dispatch.

# complete derivation or exact first unsupported line

RANK_PAIR_PROOF gives the complete derivation. Greedy independent-vector growth saturates rank at every parity-cost threshold. Integrating the finite rank deficit computes a restricted affine minimum exactly. Subtracting centered coordinate cost gives actual release as character refund plus a nonnegative rank increment. Using only a subset of parities yields a concrete executable LOWER bound on full release. Actual Boolean even-hyperplane guards show naive summation of overlapping exchanges overcharges by an arbitrary factor d; quotient rank is the essential ownership test.

For F_k=1-A_k+A_k*(-1)^(ab+ac+bc+za), k>=2,p=2^-k, query original(a,b). Four unactivated terminals are constant, two single characters and one weight-two character. One actual parity shear reduces that last activated terminal's influence by p, at reach1/4: rho=p/4, while all character-only refunds vanish. Its signed physical decrement is exactly (15/4)p+p(1-p)h(3/4)+(3/8)kp^2+Delta(p). Curvature on[1-p,1] bounds the full Delta, not a discarded mixed remainder. The certified inequalities h(3/4)<1/2, ln2>2/3, kp<=1/2 yield (15/4)p<L<(595/128)p. The physical-only pair is unpaid at15/4; the SAME query plus reset is paid with margin>5p/128.

Every complete terminal remains, including ANY disjoint tensor core h untouched in all four branches. This is a paid local fragment in a family retaining arbitrary FEI difficulty, not an FEI bound on h. For k>=16 each nonconstant optimized terminal violates15/4, so terminal nonviolation is not supplied. On a least-dimensional fixed-K witness, only nonviolation of ALL smaller Boolean functions licenses the affine-image terminals. Physical ratio criticality alone grants no such reset eligibility. Historical component-pruning failures stay excluded: no virtual component indicator replaces an actual child; all signs, reaches and whole-core entropy persist.

FIRST UNSUPPORTED LINE: force an adequate quotient-rank increment at some original proper pair of every genuine high-K critical witness, paying its signed bill with SAME unused S_E,A, mixed T and complete terminals. The rank formula and displayed all-k paid fragment are proved; universal selection is not.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede each job. From A052 run python -B -X utf8 followed by this run's code/check_rank_pair.py --pilot, then without --pilot; run code/independent_tensor.py. Final pilot246 predicates PASS on22 tables in0.086s. Main3677 predicates PASS in0.820s: all278 labelled tables n0..3, every independent parity basis through3bits, independent physical directional influences, rank/character decomposition, actual even-hyperplane controls d3,5,7, three explicit activated roots k2..4 and their12 physical terminals, and exact analytic profiles k2..20. No floating sign decision or symmetry quotient.

Independent direct-character/physical-shear replay718 counted coefficient comparisons and assertions PASS in0.199s: three actual tensors (literal, point2, bent2), all12 original terminals and12 reset terminals, whole entropy multisets, separately counted physical edges, measured p/4 release and exact signed account. Combined4395 final checks; pilot excluded. This new targeted count is separate from the prior stage's84247 checks. The literal core deliberately lacks affine minimality, showing that its preservation is unnecessary for this explicit tensor payment; it receives no centering credit.

The first pilot caught a packed branch-label error: the weight-two character is branch integer1=a+2b, not integer2 from lexicographic(a,b) ordering. out/PILOT_CORRECTION records the old helper hash, actual branch influences/releases and correction. The mathematics was unchanged; v2 spec and pilot were refreshed before the adopted full run. Independent input shear subsequently verified the branch directly.

Arithmetic is integer Walsh and separate direct character sums, Fraction, exact prime-log identities and32-term rational atanh tails with outward96-bit rounding for inequalities. The all-k step is the analytic curvature/monotonicity proof, not extrapolation from k<=20. Constants, rank0, zero marginals, tied costs and all branch reaches are covered. Zero-log terms are explicit; p>0,k>=2 and positive logarithm arguments are checked where used. No job expected above300MB: Python estimates70--90MB,55s caps; core Lean estimate150MB. No GPU, automatic dimension increase, detached work or other running work changed. Lean core scalar-endpoint attempt RUNTIME_UNVERIFIED after39.2s (wrapper41.15s); no Lean certification, whole-Fourier or scalar, is claimed. Rung: author-checked proof plus exact finite validation, independent review pending.

# proof dependencies and changed downstream conclusions

REVIEW_A051 independently accepts current A051 local optimized-child bank/eligibility and adaptive reset telescope (Section2 equation3 and Section3), unchanged and without repair. The new all-k upper-budget and perturbation claims are read context only, not newly independently accepted. Earlier minimum-basis reduction remains accepted at its prior scope; the rank formula is rederived directly. A055's new SAME-K weak hidden-pair guard is consumed, not independently accepted anew. The new result supplies a genuine non-character LOWER release and shows why dependent swap proposals cannot be separate budgets. No universal constant improves and no source theorem is refuted.

# one next mathematical action and independent reviewer

NEXT_PLACEHOLDER

A051/A055 consume the rank lower-funding interface; A090 reconstructs the greedy rank ownership and physical shear; A094 challenges the all-k curvature bound, sign of every terminal and arbitrary-core account. Handoffs are source-bound local artifacts; no messages were sent.

# actual persistence receipts or precise save blocker

All four protocol files, proof, scoped independent review, frozen specs, correction evidence, code, exact outputs and source hashes saved under A052 only. Finalizer verifies schema field sets, compatibility-copy bytes, required headings, statement hash,20MB cap, two-line STATUS and saved file hashes. WORKLOG and LEARNED updated with this stage. out/PERSISTENCE_RECEIPT.json records actual local paths/sizes/hashes and rolling receipts. Supervisor copies, registry adoption, brain ingestion, remote mirrors and new independent review remain unverified. No local save blocker. No git or shared-source mutation was performed.

## Universal bridge

C019 stopping-tree payment through B11 critical selection gains an exact LOWER funding interface: conditional cheap-parity ranks measure executable affine release without double-spending dependent directions. It also gains one ORIGINAL physical pair that changes from unpaid to paid at SAME15/4 through a non-character refund, for every activation depth and with an arbitrary core retained in all terminals. Universal constant gain is zero, because terminal debts and general selection remain open. NEXT forces a sufficient quotient-rank increment relative to SAME unused S_E,A on a genuine high-K witness; this is the shortest missing implication after the demonstrated payment and ownership, whereas another affine/weak-root class or upper budget cannot fund it.
'''.replace('NEXT_PLACEHOLDER',next_action)
put(R/'REPORT.md',report)
source_paths=[P/'EXECUTION_PROTOCOL.json',B/'BOARD.md',B/'claude/B11/STREAM_NOTES.md',A/'runs/20261021T222218Z-fleet03-A052-critical-source-structure/PATH_CODE_PROOF.md',A/'runs/20261014T124751Z-fleet05-A052-critical-source-structure/code/exact_library.py']
for who,run,names in [('A051','20261023T002518Z-fleet03-A051-near-extremizer-definition',['REPORT.md','RESET_BUDGET.md','CLAIMS.json']),('A055','20261022T233657Z-fleet03-A055-extremal-obstruction-referee',['REPORT.md','PROOF.md','CLAIMS.json'])]:
    source_paths += [B/'agents'/who/'runs'/run/name for name in names]
js(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in source_paths])
put(A/'STATUS.md','STATE: Stage8 saved: exact rank lower-funding formula; original pair paid at SAME15/4 via non-character p/4 refund, arbitrary core/full terminals retained;4395 checks PASS; FEI OPEN.\nNEXT: '+next_action+'\n')
for name,marker,text in [('WORKLOG.md','Stage8 rank lower funding',f'\n{stamp} Stage8 rank lower funding: reviewed A051 local bank/telescope; derived rank-integral executable release and Boolean d-fold overlapping-swap guard. Original(a,b) pair of rare activated quadratic changes from unpaid to paid at15/4 with rho=p/4, margin>5p/128, allk>=2; arbitrary tensor core retained.3677+718=4395 checks PASS; packed branch error fixed before full adoption; Lean runtime unverified. Full FEI/selection OPEN.\n'),('LEARNED.md','Stage8 durable rank refund','\nStage8 durable rank refund: rho_E=chi+integral(rank cheap parities - count cheap coordinates), an actual affine lower release when E contains coordinates. Never sum dependent row-swap savings: odd-d even-hyperplane Boolean spectra give rho1/2 but naive sumd/2. For activated Q=(-1)^(ab+ac+bc+za), query original(a,b), k>=2,p=2^-k: rho=p/4, Ip=p, (15/4)p<L<(595/128)p, paid after reset at15/4 with margin>5p/128. All four terminals and any disjoint core remain. Nonconstant optimized terminals violate15/4 for k>=16. Local payment is not terminal nonviolation; transformed-child eligibility requires the fixed-K least-dimension selector, stronger than physical ratio criticality.\n')]:
    if marker not in (A/name).read_text(encoding='utf-8'):
        with (A/name).open('a',encoding='utf-8',newline='') as f: f.write(text)
put(R/'CHECKPOINT.md','Stage8 complete locally: rank lower-funding formula and original pair all-k SAME15/4 payment,4395 checks PASS; arbitrary core/all terminals retained; universal selection and FEI OPEN.\nNEXT: '+next_action+'\n')
assert set(prog)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for heading in protocol['required_per_run']['report_fields']: assert '# '+heading in report
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'checked_at_utc':stamp,'schema_checks':'PASS','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'remote_save':'UNVERIFIED'}
js(R/'out/PERSISTENCE_RECEIPT.json',receipt)
for e in receipt['files']: assert sha(R/e['path'])==e['sha256']
print(json.dumps({'status':'SAVED_SCHEMA_AND_HASH_VERIFIED','checks':total,'files':len(files),'claim':claim['claim_id']}))
