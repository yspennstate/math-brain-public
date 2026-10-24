import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];BASE=AGENT.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,v):(ROOT/p).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
sources=[BASE/'BOARD.md',BASE/'claude/B11/STREAM_NOTES.md',
 Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),
 AGENT.parent/'A051/runs/20261014T012634Z-account05-A051-near-extremizer-definition/REPORT.md',
 AGENT.parent/'A051/runs/20261014T012634Z-account05-A051-near-extremizer-definition/TWO_BIT_RESERVE.md',
 AGENT.parent/'A051/runs/20261014T012634Z-account05-A051-near-extremizer-definition/CLAIMS.json',
 AGENT.parent/'A055/runs/20261014T004129Z-account05-A055-extremal-obstruction-referee/REPORT.md',
 AGENT.parent/'A055/runs/20261014T004129Z-account05-A055-extremal-obstruction-referee/PROOF.md',
 AGENT.parent/'A055/runs/20261014T004129Z-account05-A055-extremal-obstruction-referee/CLAIMS.json',
 AGENT/'runs/20261013T221539Z-account05-A052-critical-source-structure/CRITICAL_PHASE_PROOF.md',
 AGENT/'runs/20261013T221539Z-account05-A052-critical-source-structure/code/check_phase.py',
 AGENT/'runs/20261013T221539Z-account05-A052-critical-source-structure/code/exact_library.py']
put('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
a51=json.loads(sources[5].read_text())[0];a55=json.loads(sources[8].read_text())[0]
reviews=[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],
          'reviewer':'A052','verdict':'HOLDS_AT_COMPLETE_ANALYTIC_SCOPE_WITH_INDEPENDENT_FINITE_REPLAY',
          'review_source':str(ROOT/'DEPENDENCY_REVIEW.md'),'review_sha256':sha(ROOT/'DEPENDENCY_REVIEW.md'),
          'contributor_conflict':False,'registry_adoption':'PENDING'} for c in (a51,a55)]
put('out/REVIEW_RECORDS.json',reviews)
statement='For every finite uniform-cube Boolean sign f and distinct physical coordinates i,j, let C_i,C_j,C_ij be the weighted squared-density row collisions and O_k=Inf_k-beta_k the singleton excess orientation energies. For Fourier quartets (alpha,beta,gamma,delta), q=sum amplitudes squared, define P_ij=sum_t 4(alpha delta+beta gamma)^2/q, M_i=sum_t[4alpha^2 beta^2/(alpha^2+beta^2)+4gamma^2 delta^2/(gamma^2+delta^2)-4(alpha beta+gamma delta)^2/q], and M_j analogously interchanging beta,gamma. Zero-mass fractions are zero. Then M_i,M_j>=0 and C_ij=C_i+C_j+P_ij-M_i-M_j exactly; P_ij<=2(Inf_i+Inf_j), and C_ij<=2(C_i+C_j)+2(O_i+O_j). On a least-essential-dimension FEI(K) violating witness, K>0, deficit D>0 and actual singleton child reserves S_i,S_j>=0, the reviewed scalar bound r_K=log2(1+2^(2/ln2-K)) yields C_ij<=2(C_i+C_j)+(2/K)(2r_K-2D-S_i-S_j). The unconditional singleton-only bound is still false on the exact three-bit parity guard. The orientation coefficient2 is sharp for arbitrary real quartets, not claimed sharp for Boolean functions. For K>=4, the displayed bound can substitute into the reviewed two-bit phase-bank upper bound by monotonicity, but supplies no pair-selection theorem or universal FEI constant.'
hyp=['Uniform finite Boolean signs and physical singleton/pair cuts; entropy bits; zero Fourier row masses omitted',
     'Algebra/refund inequalities hold without criticality and also for arbitrary real quartets',
     'Reserve substitution requires K>0 and least essential dimension among all Boolean K-violators; child deficits are actual physical deficits',
     'The two-bit phase-bank corollary requires K>=4 and a proper queried pair',
     'No claimed sharp Boolean coefficient, global optimizer, selected affordable pair or full FEI resolution']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A052-SIGNED-PAIR-ORIENTATION-REFUND','version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':digest,'contributors':['account05/A052'],
       'proof_source':{'path':str(ROOT/'SIGNED_PAIR_PROOF.md'),'sha256':sha(ROOT/'SIGNED_PAIR_PROOF.md'),'locator':'Sections1--4'},
       'proof_dependencies':reviews,'review_records':[],'status':'AUTHOR_PROVED_SCOPED_APPLICATION_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':[],'first_unproved_line':None,
       'next_consumers':['claude/B11','A051','A053','A055','A090','A094','B20']}
put('CLAIMS.json',[claim])
check=json.loads((ROOT/'out/CHECK.json').read_text());total=sum(check[k] for k in ['assertions_new_checker','assertions_phase_library','assertions_log_library'])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A052','gap_id':'G-R-SELECT',
 'attempt_id':'A052-signed-pair-orientation-4','method':'Exact signed fourth-moment/merging identity; Cauchy--Schwarz; critical singleton reserve insertion; independent direct-character/rational replay',
 'mathematical_delta':f'Proved C_ij=C_i+C_j+P_ij-M_i-M_j with nonnegative merging refunds and C_ij<=2(C_i+C_j)+2(O_i+O_j). Critical orientation is bounded by actual child reserves and the reviewed exponential singleton bank. Independently accepts A051 two-bit and A055 singleton claims. {total:,} exact assertions PASS.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SIGNED_PARITY_TERM_COMPARISON_RESOLVED_WITH_ADDITIVE_RESERVE; UNIVERSAL_SELECTION_AND_FULL_FEI_OPEN',
 'claim_versions_used':reviews,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'NEW_SCOPED_SIGNED_PAIR_COMPARISON'},*reviews],
 'source_artifacts':['SIGNED_PAIR_PROOF.md','DEPENDENCY_REVIEW.md','code/check_signed_pair.py','code/phase_library.py','code/exact_library.py','out/FROZEN_SPEC.json','out/CHECK.json','out/SOURCE_MANIFEST.json','out/REVIEW_RECORDS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Use the exact signed merging refunds to select a critical-witness pair with residual cost below its full D+S_pair+phase margin, or diagnose a multirow obstruction; retain singleton collisions and the additive orientation correction rather than repeat the false unconditional comparison.',
 'stagnant_substantive_attempts':0,'blockers':['No dimension-independent control of remaining singleton collisions relative to positive root/child reserve; exponentially small orientation upper bounds do not give a positive deficit lower bound','New scoped correction awaits independent review; shared adoption and mirror persistence unverified'],
 'packet_ids':['A052']}
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A052/B11, stage {ROOT.name}. Target the signed alpha*delta+beta*gamma pair-row term identified by A051, retaining actual singleton orientation and physical child reserves. All cubes finite and uniform, f Boolean signs, entropies bits. Unconditional pair identities require no criticality; guarded bounds require a least-essential-dimension FEI(K) violator and K>0. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read own STATUS, updated BOARD and B11 STREAM_NOTES v2 (still2026-10-11 23:3xZ), and the full protocol revision2026-10-11-execution-v2. New A051 stage4 REPORT, CLAIMS and TWO_BIT_RESERVE sections1--6 and A055 stage3 REPORT, CLAIMS and PROOF were read. The source-bound A055 analytic review of the prior A052 phase theorem is consumed. A053 status was consulted for scope; its newer proof was not audited or used. Earlier campaign/paper reads are not represented as refreshed. Exact source hashes are in out/SOURCE_MANIFEST.json. The lead's original beta-composition target is already complete; this stage follows the useful live reserve dependency.

# complete derivation or exact first unsupported line

SIGNED_PAIR_PROOF.md proves the exact joint/singleton collision identity with signed parity cost P and nonnegative merging refunds M_i,M_j. Weighted Cauchy--Schwarz pays P by twice the pair influence. The exact minority/orientation split and C_k>=2beta_k then give C_ij<=2(C_i+C_j)+2(O_i+O_j). On a genuine minimal K-witness, A055's singleton bank bounds the orientation correction by (2/K)(2r_K-2D-S_i-S_j); all root and child reserves remain present. Inserting this into the reviewed A051 two-bit bank is valid by monotonicity. The three-bit zero-singleton parity guard passes with its missing cost explicitly in orientation, not discarded. A rational real-row limit shows why an orientation correction is necessary and why its coefficient2 is sharp for general real rows; no sharp Boolean conclusion follows.

First unsupported line: a dimension-independent K and proper pair/larger-block selection with collision and phase cost below the retained root/child reserve. The correction is positive and neither the singleton collision masses nor the root deficit are uniformly separated. Exponentially small upper bounds and dimension-dependent Fourier granularity cannot settle D>0. No component or Boolean phase is silently granted physical-descendant status.

# executed validation with domain, arithmetic, commands and outputs

The frozen specification preceded the only job; memory estimate70MB, runtime cap55 seconds, no >300MB job requiring memok, no GPU or background process. Executed from A052:

    python -X utf8 runs\\{ROOT.name}\\code\\check_signed_pair.py

PASS: {total:,} exact assertions, comprising {check['assertions_new_checker']:,} new comparisons and {check['assertions_phase_library']:,} phase/channel validation assertions, helper runtime {check['runtime_seconds']:.6f} seconds. Domain: all276 Boolean tables n<=3, 804 labelled singleton cuts and784 pair cuts (full pairs at n2 only for identities), fixed NAND6 with15 pairs, fixed parity guard with3 pairs, all625 rational real quartets in{{-2,-1,0,1,2}}^4, and8 frozen rational orientation-limit rows. No symmetry quotient or dimension escalation. Real quartets test algebra only, not FEI realizability. The48 pair cuts of16 genuine n3 K=2 minimal violations retain nonnegative singleton child reserves. No computed K>=4 violating root is claimed.

Direct character sums and physical edge boundaries supply spectra/influence independently of source helpers. Exact Fraction verifies signed identity, squared merging formulas, orientation/mass accounting and parity guard; prime-log expressions with proved40-term atanh tails and outward96-bit bounds certify entropy signs. A055's finite bank replay uses the proved relaxation 2/ln2<3 at K2,4,8; its sharp exponent is analytic. A051's actual row-class bank is checked at K4,8 with its exact rational log argument, retaining arbitrary roots' signed S. Logs are inherited from the earlier A052 checked library, not a new independent logarithm implementation. CHECK.json persists all named pair quantities and exact orientation-limit values. Runtimes are descriptive decimals, not proof decisions.

# proof dependencies and changed downstream conclusions

DEPENDENCY_REVIEW.md and out/REVIEW_RECORDS.json independently accept A051-TWO-BIT-CRITICAL-PHASE-RESERVE@1 and A055-SINGLETON-CRITICAL-RESERVE@1 at complete analytic scope, with independent finite replay and no substantive repair. Their original finite assertion totals are not adopted. Exact source statement hashes are in the reviews. Live source-complete interfaces are reviewed before recording this narrowly scoped application; no new broad FEI candidate or unreviewed universal assertion is opened. Source-bound A055 acceptance of A052's previous phase exclusion is consumed without changing its original run or a shared registry.

Changed conclusion: the signed degree-two term is no longer an unspecified barrier to guarded pair-versus-singleton comparison. Its exact cost and refunds are explicit, and its orientation remainder is quantitatively paid by the existing singleton reserve. This is a comparison theorem with a positive residual, not the missing selection theorem. It does not revive raw-component pruning: every Fourier row belongs to the actual Boolean parent, and reserve signs are used only for genuine smaller-dimensional physical children.

# one next mathematical action and independent reviewer

Next: use the saved exact merging refunds, rather than their nonnegative relaxation, to select a pair on a genuine critical witness whose residual collision/phase bill is below D+S_pair+(K/2-2)Wg. If all such refunds can vanish on a structurally compatible high-threshold source, extract that exact obstruction and change mechanism. A051/A055 and B11 lead are immediate consumers; A090/A094 should reconstruct the weighted row identity, zero-denominator conventions, and actual child-reserve substitution. No outbound messages were sent.

# actual persistence receipts or precise save blocker

All four protocol files, proof/review notes, frozen spec, code and exact outputs are saved in this run. PROGRESS and PACKET_DELTA are byte-identical; schema, file-size and hashes are checked in out/ARTIFACT_MANIFEST.json. STATUS, WORKLOG and LEARNED are updated only in A052. Independent review of the new correction, shared-registry adoption and external mirrors remain pending. No local save blocker.

**Universal bridge:** This stage moves C019 stopping-tree payment through B11's critical pair-selection target by closing the signed parity-cross-term comparison requested by A051/A055: C_ij is exactly singleton collision plus signed parity cost minus two merging refunds, and its excess is bounded by an explicit orientation/child reserve. The quantitative gain is the guarded coefficient2 comparison with correction (2/K)(2r_K-2D-S_i-S_j), validated by{total:,} exact assertions; no universal FEI constant improves. What remains is selecting a block with the remaining singleton collision and phase cost below its complete positive reserve. NEXT uses the exact refunds to target that selection gap, whose uniform resolution would contradict every minimal FEI violation, rather than produce another isolated class bound.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text(f'STATE: Stage4 complete: signed pair/refund identity and orientation-corrected critical comparison proved; A051/A055 independently reviewed; {total:,} exact checks PASS; FEI OPEN.\nNEXT: Use exact merging refunds to select a critical-witness pair below its full root/child/phase reserve; A090/A094 review pending.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} {ROOT.name}: consumed A051/A055 new reserve proofs and independently accepted analytic scope. Derived exact C_pair=C_i+C_j+P-M_i-M_j and bound C_pair<=2(C_i+C_j)+2(O_i+O_j), then inserted retained singleton root/child reserves. {total:,} rational/log assertions PASS in{check["runtime_seconds"]:.6f}s, below55s pilot cap. Parity guard retained; no unconditional comparison or uniform pair selection asserted.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage4: signed pair collision equals singleton collisions plus P=sum4(alpha delta+beta gamma)^2/q minus two nonnegative exact weighted-Cauchy merging refunds. P<=2 I_pair and C_k>=2 beta_k give C_pair<=2(C_i+C_j)+2(O_i+O_j). Minimal K-witness reserve yields orientation correction <=(2/K)(2r_K-2D-S_i-S_j). Parity guard has C_i=C_j=0 but O_i=O_j=1/2, so omission of orientation is false. Remaining issue is selected-pair payment relative to positive full reserve; exponential upper bounds do not provide a deficit lower bound.\n')
protocol=json.loads(sources[2].read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert all(x in report for x in protocol['required_per_run']['report_fields'])
receipts=[]
for file in ROOT.rglob('*'):
    if file.is_file() and '__pycache__' not in file.parts:
        assert file.stat().st_size<20*1024*1024
        receipts.append({'path':str(file.relative_to(ROOT)),'bytes':file.stat().st_size,'sha256':sha(file)})
put('out/ARTIFACT_MANIFEST.json',{'status':'PASS','schema_checks':'PASS','file_count':len(receipts),'files':receipts})
print(json.dumps({'status':'SAVED_PROTOCOL_AND_HASH_CHECKS_PASS','files':len(receipts),'assertions':total,'claim_sha256':digest}))
