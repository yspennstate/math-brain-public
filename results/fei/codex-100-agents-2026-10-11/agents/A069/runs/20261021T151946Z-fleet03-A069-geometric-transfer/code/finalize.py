from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];HOME=RUN.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):
 p=RUN/name;p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol_path=Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
cert=json.loads((RUN/'out/CERTIFICATE.json').read_text(encoding='utf-8'))
assert cert['status']=='PASS' and cert['exact_assertions']==1150
lean=json.loads((RUN/'out/LEAN_RESULT.json').read_text(encoding='utf-8'))
assert lean['result']['status']=='RUNTIME_UNVERIFIED'
statement=(
 'For every integer m>=1, on a finite uniform cube with disjoint c,u, m-bit Z and three-bit Y, '
 'let q2=-1 exactly on c=0,Z=0 and let G have ordered Boolean cores '
 '(Maj3,y0,-y0,-Maj3) indexed by c+2u. Start with common frequency reference '
 'R=(8/13,2/13,1/26,1/26,1/26,1/26,1/26,1/26). Use the stage5 five-cell control law '
 'with weights (1/4,1/4,1/16,7/20,7/80), uniform inside each cell, and the actual control-occupancy '
 'prior. Through every physical core query carry R by frequency marginalization to the SAME '
 'reference for both children and all four cores. For every core-only adaptive restriction history '
 'with no repeated coordinate on a path, complete each path to three core queries. Every node '
 'has signed excess e=max(0,Delta C_Q-4 Inf_i)<=1/4. Every complete actual terminal has '
 '4I-C_Q>1 and remains nonconstant. Allocate each node excess to its final descendants with '
 'their physical conditional probabilities: the cumulative debit on any final terminal is <=3/4 '
 'from its ONE inherited complete terminal surplus, leaving >1/4. The exact signed telescope '
 'therefore proves H(F)<=C_Q(F)<4I(F)-1/4 for F=q2G, all m. At m=1, after Y1=0, the relevant '
 'query Y2 has 1/100<Delta C_Q-4 Inf_Y2<1/40, and both actual child core pairs are nonconstant. '
 'No arbitrary-core, control-query, depth-independent or universal FEI assertion is made.'
)
claim={
 'claim_id':'A069-SAME-REFERENCE-ADAPTIVE-CORE-TERMINAL-BANK','version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform finite Boolean cube; entropy and reference cross entropy in bits.',
 'Exactly the paired majority/literal cores and positive normalized core reference specified.',
 'm>=1, event c=0,Z=0; fixed cell weights and actual flag prior retained.',
 'Only physical Y queries, distinct along each branch; all actual terminal costs retained.',
 'All negative query prices allocated cumulatively against one original complete terminal reserve; no reset.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['fleet03/A069'],
 'proof_source':{'path':str(RUN/'DERIVATION.md'),'sha256':sha(RUN/'DERIVATION.md'),'locators':'equations (1)-(5), thinning argument and terminal allocation'},
 'proof_dependencies':[],
 'review_records':[],
 'status':'AUTHOR_PROOF_WITH_EXACT_FINITE_CERTIFICATES_INDEPENDENT_REVIEW_PENDING',
 'supersedes':[], 'refutes':[], 'first_unproved_line':None,
 'next_consumers':['A070','A088','A094','A067','A096','B14','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
write('CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B14','packet_id':'A069',
 'gap_id':'G-R-SELECT','attempt_id':'A069-geometric-transfer-stage6-same-terminal-bank',
 'method':'Complete inherited five-cell reference; Bernoulli thinning; exact core certificate; cumulative terminal allocation',
 'mathematical_delta':'Replaced stage5 unpaid physical core-query price by an explicit one-terminal-bank payment for every adaptive history of the three core coordinates, all private widths; rate4 and a relevant negative-price second query.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW_AND_SUPERVISOR_COPY',
 'mathematical_status':'SCOPED_AUTHOR_PROOF_WITH_EXACT_CERTIFICATES; FULL_FEI_OPEN; LEAN_RUNTIME_UNVERIFIED',
 'claim_versions_used':[{'claim_id':'A069-EXPOSED-CANCELLATION-COMMON-REFERENCE-HISTORY','version':1,'scope':'Reference construction and exact signed ledger; specialized derivation independently reproduced here; prior independent review still pending.'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','FROZEN_CERTIFICATE_SPEC.json','FROZEN_LEAN_SPEC.json','code/certificate.py','out/CERTIFICATE.json','out/LEAN_RESULT.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A070/A088 audit the stage5/6 references and cumulative allocation. Then replace the depth-three per-query allowance by telescoped flag information and cumulative core-reference excess on one longer actual non-flat history with the same unused terminal owner.',
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI: no dimension-free cumulative excess/terminal-bank existence theorem for arbitrary cores.',
 'Independent reviews and registry/mirror adoption unverified.',
 'Lean named allocation target returned RUNTIME_UNVERIFIED after timeout; no formal certification.'],
 'packet_ids':['A069']}
fields=[v.split(' (')[0] for v in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
sources=[protocol_path,HOME/'STATUS.md',HOME/'LEARNED.md',
 Path(r'~/AGENTS.md'),
 Path(r'BOARD.md'),
 Path(r'claude/B14/STREAM_NOTES.md')]
root=Path(r'math-open-problems/reports/fei-2026-10-11')
sources += [root/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
root=Path(r'math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
sources += [root/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/ERASURE_REDUCTION.md','sources/GAMMA_ENDPOINT_LEDGER.md','sources/ONE_BIT_ENDPOINT.md','sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']]
ctx=Path(r'context')
sources += list(ctx.glob('*.txt'))
sources += list((HOME/'runs/20261014T060600Z-fleet05-A069-geometric-transfer').glob('*.md'))
sources += list((HOME/'runs/20261014T060600Z-fleet05-A069-geometric-transfer').glob('CLAIMS.json'))
sources += list(Path(r'agents/A070/runs/20261014T034205Z-fleet05-A070-analytic-route-referee').glob('CLAIMS.json'))
sources += list(Path(r'agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee').glob('CLAIMS.json'))
write('out/SOURCE_MANIFEST.json',{'note':'Local bytes read; hashes are source pins, not independent proof review. Legacy manuscript text files explicitly decoded cp1252 after UTF-8 decoding failed. STATUS/LEARNED entries hash pre-update content.','sources':[{'path':str(p),'sha256':sha(p)} for p in sources]})
report='''# A069 stage6: one terminal bank through an adaptive core history

## exact target, quantifiers, hypotheses and units

For every private width m>=1, take F=q2G with q2 negative exactly at c=0,Z=0, and the fixed paired cores (Maj3,y0,-y0,-Maj3) indexed by c+2u on three Y bits. Preserve the stage5 common core reference R=(8/13,2/13,1/26,...,1/26), the same five-cell control law, and all complete actual terminal costs through ANY adaptive physical Y-query history. Entropy and reference cost are bits; influence is ordinary pivotal influence. Each node's positive excess (Delta C-4Inf)+ is <=1/4; each fully restricted terminal has unused surplus 4I-C>1. At most three path charges spend <=3/4 from that SAME terminal bank, leaving >1/4. Thus H(F)<=C_Q(F)<4I(F)-1/4. This is a scoped author proof with exact finite certificates, awaiting independent review. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL revision2026-10-11-execution-v2; requested README/status/registries/plan and supplement campaign/claim/counterexample/seed/crosswalk files; current BOARD dated2026-10-21 15:30 UTC; B14 STREAM_NOTES v2 remains the old initial directive, already completed in earlier A069 stages. The productive saved stage5 NEXT therefore governs. Actual source-complete A069 reports stop at20261014T060600Z; later fleet05 directories contain only failure markers or no reports, not fifteen additional verified mathematical stages. Stage5 DERIVATION Sections2,3,6 fixes the reference and signed ledger. A070's20261014T034205Z whole stage4 review and private-source obstruction, and A088's20261014T053751Z conditional-flag obstruction, were read at source. Neither is represented as acceptance of the new claim.

Percolation30pp Section2/Lemma2.1 and its proof distinguish deterministic child-mask decoding from the geometric arm estimate that pays occupancy. The earlier31pp version has the same abstract interface. Threshold38pp Proposition8.6(75)-(79) retains shared-core marginals and actual influence; earlier29pp reviewed for baseline differences. Supplement source notes on erasure, block restrictions, endpoint and Gamma were inspected. SOURCE_MANIFEST pins the bytes read. No paper download, publication or scheduler change occurred. The family already has the stage5 structured FEI certificate; no claim that its FEI membership is new. This stage improves its explicit reference budget and continuation mechanism, not the class-priority record.

## complete derivation or exact first unsupported line

DERIVATION.md gives the proof. For each partial assignment, let a=restricted Maj3,b=restricted y0,d=Pr(a!=b),A=(I(a)+I(b))/2,rho=2^-m,beta=2rho(1-rho), and B the mean cross entropy under the inherited common core reference. The paired signs give sum of cores zero pointwise. Exactly

    C=B+h2(d rho^2)+2+2(1-2d)rho
       +beta[m+log2(1-rho)+log2(20/7)],
    I=A+1+(m+1-2d)rho.

These are complete reference costs, not entropy-only bounds. On a core query all nonflag control terms average unchanged. The decrement is Delta B plus the Jensen-Shannon flag refund. Independent Bernoulli thinning bounds that refund by rho^2<=1/4. All27 core query types certify Delta B<=4Inf at relevant queries; irrelevant queries have zero flag refund and Delta B<1/4. Therefore signed excess never exceeds1/4, including irrelevant exposure.

After all Y bits are fixed, both possible d=0,1 terminals have surplus>1: exact certificates cover m=1,2, while m>=3 gives surplus>=1+rho(2m+2-4d-16/5)>=1+4rho/5. They remain nonconstant since I_cu>=1-rho>0. Complete any adaptive stopping tree to three distinct Y queries. Allocate each query excess to its final descendants according to the true physical conditional probabilities. Each leaf receives <=3/4 total debit against ONE >1 unused complete terminal surplus. This is a single allocation over the whole tree; it does not recertify fresh child slack. The exact influence/reference telescope includes all node prices and all final reference bills, yielding root surplus>1/4. Partial stopped terminal bills are retained by expanding their own exact continuation identities.

The first unsupported universal line is existence, for arbitrary Boolean cores, of a common reference and an actual tree whose cumulative signed query excess is paid by one unused complete terminal bank. Here the depth3 bound and the finite majority/literal certificate supply it. No arbitrary-core, Z-dependent source, control-query or dimension-free history conclusion is inferred. In particular the A088 conditional-flag local-price obstruction is not bypassed by declaring a refund to be income.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC recorded the81-query pilot before execution. Its first invocation reached the final output write but failed because out/ had not been created; this was an artifact setup failure, not a mathematical counterexample. The directory creation was added. The spec was clarified before the completed rerun to identify floating logs as discovery only; the original planned exact-log implementation was not claimed to have run in the pilot. Completed pilot81 queries in0.135665s found16 negative K4 prices, including4 relevant negative-price queries at m=1. Its numbers are evidence only.

FROZEN_CERTIFICATE_SPEC separately fixes27 core patterns,27 core queries,81 full Boolean nodes and81 full queries at m1..3, and4 terminal boundary types at m1,2. code/certificate.py PASS:1150 exact assertions in0.370316s. Integer Walsh and independent pivotal counts agree on every checked influence. Prime-log coefficient maps certify the exact whole-reference formulas and physical ledger. Fraction atanh intervals use24 terms after power-of-two reduction; the omitted positive remainder is bounded by2z^49/[49(1-z^2)], with z<=1/3. No floating sign decides a certificate. The relevant second query Y2 after Y1=0 at m=1 has exact excess strictly between1/100 and1/40; both actual restricted core pairs have positive core influence. The all-m extension is the analytic thinning/terminal argument, not finite enumeration extrapolation.

Commands from A069:

    python -X utf8 runs/20261021T151946Z-fleet03-A069-geometric-transfer/code/pilot.py
    python -X utf8 runs/20261021T151946Z-fleet03-A069-geometric-transfer/code/certificate.py
    python -X utf8 tools/memok.py
    python -B -X utf8 runs/20261021T151946Z-fleet03-A069-geometric-transfer/code/lean_run.py
    python -X utf8 runs/20261021T151946Z-fleet03-A069-geometric-transfer/code/finalize.py

Mathematical failure checks: arbitrary unequal cores need not sum to zero (four equal literal cores give alpha=2rho-rho^2, not the specialized paired-core formula); arbitrary common references can have arbitrarily large irrelevant-query cost. Thus both hypotheses are used. d=0,1, alpha=1, constants in restricted cores, and irrelevant queries are covered exactly. rho and1-rho are positive for every allowed m; no endpoint denominator is canceled at m=0. Finite histories justify all telescoping sums without limits. Queries may depend on prior physical outcomes, but never on the Fourier sample.

The discrete allocation sublemma was submitted to the installed Lean helper with --core, named target quarter_bank, exact reviewed-source SHA, allowed-axiom auditing, local receipt directory and timeout55s. memok passed (physical20.3GB,commit30.5GB free). Lean returned RUNTIME_UNVERIFIED after60.399s including wrapper/poll overhead, exceeding the requested55s cap; no compiler/target certificate or axiom result was obtained. The formal rung remains unresolved. The Nat statement represents three quarter-unit upper charges leaving one of four units, not the Fourier/information proof. No Lean-checked theorem is claimed. No retry or larger compiler job was launched. Noncompiler jobs estimated32/64MB and finished under one second of script execution; no GPU, detached job or dimension escalation.

## proof dependencies and changed downstream conclusions

The stage5 reference definition is retained exactly and specialized formulas are independently rederived and verified against full Boolean truth tables here. Standard Parseval, Gibbs, physical influence restriction and mutual-information data processing are used explicitly. No unreviewed external campaign inequality is required as a proof premise. The new claim has no campaign proof dependencies; stage5 remains a source/provenance version in PROGRESS, not a false independent acceptance receipt. All earlier accepted class theorems remain in scope. Stage5's next question is answered for this fixed nonfactorizing core: even a relevant bad second query is funded from the original complete terminal bank. General private dependence and full FEI remain unresolved.

## one next mathematical action and independent reviewer

A070 should reconstruct the actual reference formulas and cumulative descendant allocation; A088/A094 should audit the thinning information bound and compatibility with the conditional-flag obstruction. There are now two source-complete pending scoped A069 candidates (stages5/6), so review or repair precedes another broad candidate. The next mathematical target is to replace the depth3 per-node allowance by telescoped flag information and cumulative signed core-reference excess on one longer actual unequal-amplitude history, preserving the SAME supplied reference, both full terminals and one unused owner. A larger finite-core census alone would leave the universal bridge unchanged.

## actual persistence receipts or precise save blocker

All four protocol files, derivation, frozen specifications, scripts and outputs are local to the requested run. finalize.py validates exact protocol field sets, statement/source hashes, identical PROGRESS/PACKET_DELTA, seven required report headings, final Universal bridge paragraph, and size limits, then writes out/RECEIPTS.json. STATUS has exactly two lines; WORKLOG is appended and LEARNED records durable scope. Local completion requires reading the finalizer PASS receipt; independent review, B20 registry adoption, supervisor copy, mirrors and public release are not asserted. No save blocker. Wake reported stale owner-model/state-of-mind notes and the owner was alerted before relying on them. Compute telemetry showed low disk and high picture-publisher IO; existing work was left running, no cleanup or brain write was performed.

## Universal bridge

This stage moves C024 from an exact signed identity to an actual paid adaptive history under one unchanged reference: every path's at most three signed query excesses consumes<=3/4 of its ONE >1 complete terminal surplus, including a relevant bad second query with both core children nonconstant. C019 gains an explicit physical allocation for this fixed core; the root reference is paid at4I with>1/4 remaining. What remains universal is a dimension-independent cumulative excess bound and a justified common terminal reserve for arbitrary cores, plus nonflat private-source rows. NEXT removes the depth-based payment through telescoped flag information and a cumulative signed core-reference account; that attacks the precise missing universal owner inequality rather than adding another isolated class certificate.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A069 stage6 complete locally: SAME-reference adaptive three-core-query history paid once from >1 terminal bank; H<=C<4I-1/4 all private widths;1150 exact checks PASS; Lean unverified; FEI OPEN.\nNEXT: A070/A088/A094 review stage5/6; replace depth3 quarter charges by telescoped flag information and cumulative signed core-reference excess with SAME unused terminal owner.\n'
(HOME/'STATUS.md').write_text(status,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' stage6 fleet03: Resumed last source-complete stage5 (later fleet05 slots lack reports). Paired majority/literal common reference gives exact all-m cost/influence formulas.27 core query types+81 full nodes/queries,1150 exact assertions PASS. Bernoulli thinning prices flag refund<=rho^2;3 physical core queries debit<=3/4 from one >1 actual terminal surplus, H<=C<4I-1/4. Relevant bad second-query excess lies(1/100,1/40), both core pairs nonconstant. Lean core allocation timed out RUNTIME_UNVERIFIED; no certification. Review/mirror pending; full FEI OPEN.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage6: For paired cores(a,b,-b,-a) indexed c+2u, d=Pr(a!=b),rho=2^-m, I_cu=1+(1-2d)rho, I_Z=m rho, alpha=1-d rho^2. Exact fixed-five-cell CE=B+h2(d rho^2)+2I_cu+2rho(1-rho)log2[(1-rho)20/(7rho)]. Core-query flag refund is Bernoulli-thinning information<=rho^2; irrelevant queries have zero flag refund but can release positive inherited core-reference cost. For Maj3/literal and R=(8/13,2/13,1/26 six times), all27 core query types give excess<=1/4 at K4; every all-Y-restricted actual terminal has surplus>1 allm. A single terminal owns <=3/4 cumulative ancestor charges for any adaptive three-query history; no child bank reset. Scoped H<=C<4I-1/4; new family priority not claimed. Full FEI needs a depth-independent cumulative excess/available terminal owner, not the same exact telescope renamed. Lean check timed out; no Lean-checked result.\n')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
receipts=[]
for p in RUN.rglob('*'):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20*1024*1024
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/RECEIPTS.json',{'status':'PASS','at':stamp,'scope':'local persistence and schema checks; not independent mathematical review','artifacts':receipts,'rolling':[{'path':str(HOME/n),'sha256':sha(HOME/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS','claim':claim['claim_id'],'artifacts':len(receipts),'assertions':cert['exact_assertions'],'lean':lean['result']['status'],'full_fei':'OPEN','run':str(RUN)}))
