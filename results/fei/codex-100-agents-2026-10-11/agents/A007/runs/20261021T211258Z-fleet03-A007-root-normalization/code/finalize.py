from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
def rd(p): return Path(p).read_text(encoding='utf-8-sig')
def save(p,t): Path(p).write_text(t,encoding='utf-8')
def js(p,d): save(p,json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
protocol=json.loads(rd(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
results={n:json.loads(rd(ROOT/'out'/n)) for n in ['pilot.json','checks.json','scale_checks.json','payment_checks.json']}
assert all(x['status']=='PASS' for x in results.values())
lean=json.loads(rd(ROOT/'out/lean_attempt.json'))
try: lean_status=json.loads(lean.get('stdout','')).get('result',{}).get('status','UNVERIFIED')
except json.JSONDecodeError: lean_status='UNVERIFIED'
total=sum(x['assertions'] for n,x in results.items() if n!='pilot.json')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
statement=('For every integer m>=2, let g_m=2[(OR_m x) AND (OR_m y)]-1 and F_m=2z[(OR_m x) AND (OR_m y)]-1 on independent uniform bits, '
 'where z is one fresh satisfied-bit indicator. With the exact pair prime table, fixed lambda_ij=1/m, beta=1/m and the source complete forest surrogate, '
 'the accepted distributed transfer and reconstructed one-control inequality give R_F <29 I_core(F), including inherited R_g, all nonempty-data sectors, ranks and control-only residual. '
 'The same-reference correction satisfies Psi/I(g_m)=(1/4)log2(m)+1/20+o(1), uniformly over permitted original posteriors. '
 'For any finite positive record system w_rho(t)=t^k_rho w_rho and scale-independent positive lift multipliers, the mass portion pR_t+Psi_t,beta '
 'depends only on alpha=t beta, provided both references are feasible and positive and all 2^r control subsets are retained. '
 'The entropy/reference overhead outside R and full FEI remain separate; no actual queue probability or optimal-cost lower bound is asserted.')
claim_id='A007-COMBINED-LEAFLESS-PAYMENT-AND-SCALE-CANCELLATION'
claim={
 'claim_id':claim_id,'version':1,'exact_statement':statement,
 'hypotheses':['uniform physical cube; sign outputs; log2 units; m>=2',
 'same exact monotone pair prime table and globally fixed lambda=1/m,beta=1/m',
 'source surrogate residual and accepted distributed transfer, not actual queue probabilities',
 'conditional algebra identity requires finite positive raw records homogeneous once per used gate, positive masses, same multipliers and feasible old/final references'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A007'],
 'proof_source':['KMM_PAYMENT.md','SCALE_CANCELLATION.md','LEAFLESS_ASYMPTOTIC.md','REVIEW_A015.md'],
 'proof_dependencies':['A007 actual-data-witness distributed lift, stage3 LIFT.md and stage4 DISTRIBUTED_LIFT.md',
 'A007-EXACT-ROOT-TILTED-OCCUPATION@1, stage6',
 'A015 stage6 ONE_CONTROL.md, independently reconstructed here; review excludes upstream self-authored A007 results'],
 'review_records':[],'status':'AUTHOR_PROOF_EXACT_FINITE_CHECKS_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'A dimension-independent bound for the same combined final-reference cost on arbitrary shared/leafless incidences with arbitrarily small output mass b, retaining all external overhead.',
 'next_consumers':['A015','A008','A006','A086','A094']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
js(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B02','packet_id':'A007',
 'gap_id':'G-J-COST','attempt_id':'A007-substantive-stage7-combined-control-bank',
 'method':'Independent A015 reconstruction; exact normalized-mass cancellation; full-sector controller-influence payment; sharp all-m asymptotic; integer Walsh and rational certificates',
 'mathematical_delta':'Same leafless K_m,m obstruction paid completely at R_F<29 I_core using inherited residual and original control influence; Psi/I_g=log2(m)/4+1/20+o(1); intermediate common scale cannot improve combined mass at fixed final reference.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW_AND_SUPERVISOR_COPY',
 'mathematical_status':'SCOPED_SOURCE_CONDITIONAL_PROOF; FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[claim_id+'@1'],
 'source_artifacts':['KMM_PAYMENT.md','SCALE_CANCELLATION.md','LEAFLESS_ASYMPTOTIC.md','REVIEW_A015.md','out/checks.json','out/scale_checks.json','out/payment_checks.json','out/lean_attempt.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Pay the SAME combined final-reference bill for B=1_{|x|>=m-1}1_{|y|>=m-1}, whose m^2 primes omit one variable per block and have no common literal; b=(m+1)^2/4^m tends to zero. Retain original raw masses, all sectors and actual controller influence 2rp b; no intermediate scale refactoring.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review and supervisor mirror copying are unobserved','Full FEI all-dimensional combined payment remains open','Core Lean attempt status: '+lean_status],
 'packet_ids':['A007']}
expected=set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert set(progress)==expected
js(ROOT/'PROGRESS.json',progress); js(ROOT/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A007/B02 substantive stage7, C020 / G-J-COST, continued from the last substantive stage6. The account's scheduled-stage counter is not a count of new proofs. All functions use uniform physical bits and sign outputs; all costs are bits. For EVERY integer m>=2, pay the complete inherited distributed surrogate residual for the SAME activated leafless K_m,m prime table at lambda=1/m,beta=1/m. Also determine the exact leading loss of its signed correction and test whether an intermediate common scale can repair the combined bill. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read full EXECUTION_PROTOCOL.json revision {protocol['revision']}, machine AGENTS, BOARD snapshot 2026-10-21 21:14 UTC, B02 STREAM_NOTES v2 and own STATUS/LEARNED. Campaign README/CURRENT_STATUS, registry/packet JSON and stream matrix were inspected; their 11 October snapshots and old endpoint are not the current live frontier. The user endpoint 2026-10-23 14:49 UTC controls; no schedule is changed. Supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING, source inventory and plan A007 acceptance contract were inspected. Four paper text files were scanned for normalization locators; their prior mathematical baseline is inherited, not newly independently reconstructed. No external literature theorem is needed here.

The substantive new source is A015 runs/20261021T162002Z-fleet03-A015-minterm-barrier-analysis: ONE_CONTROL.md, LEAFLESS_SCALE.md, REPORT.md and REVIEW_A007.md. Own stage3 LIFT.md, stage4 DISTRIBUTED_LIFT.md and stage6 JOINT_OCCUPATION.md were read for exact raw weights, rank envelopes and complete signed ledger. Their locators are explicit in the proof files. The old lead instruction to review A009 and handle activated tribes was already completed; its review-first direction is followed by reconstructing the new A015 result. Board results on private leaves and full-support tails are neither repeated nor assumed universally. One read-only math recall returned generic/irrelevant cards, no payment theorem; no recalled claim is imported.

# complete derivation or exact first unsupported line

REVIEW_A015.md independently reconstructs both new A015 results without repair. It accepts the centered one-control bound Psi<=[log(1/beta)/2+3log(e)/5+1/20]M, M<=I_g-v, and its complete fixed-reference leafless obstruction at their stated scopes. A007 authored the upstream occupation interface, so no second independent acceptance of that upstream result is claimed.

KMM_PAYMENT.md closes the SAME leafless obstruction with the original total physical influence, including inherited R_g. An explicit old record gives R_g<=v log D+(log m+22/5)I_g. Combining the accepted full distributed transfer, all its rank/control-only payments and the independently reconstructed Psi bound gives R_F/I_core<10199/360<29 for EVERY m>=2. The all-m estimates are ma<=1/2, m^2 a<=9/8, log m<=m and I_core=(1-a)^2>=9/16. No sector or old reference cost is reset. The entropy interface, if used, yields H(F)<(K_ref+31)I(F) with unchanged source K_ref. This is a source-dependent residual closure, not a new universal FEI proof.

SCALE_CANCELLATION.md proves an exact finite identity: S_t J_t,beta,U=sum_rho(t beta)^k w_rho H_rho,U. After retaining the old normalizer and every U subset, pR_t+Psi_t,beta depends only on the FINAL scale alpha=t beta. The normalizer cancels with inherited R_t, and the posterior denominator cancels because p^2*2^r=p. This correctly allows eta_t to change with t. Refactoring the same final weights between old and lifted references cannot fix that combined bill. Positivity, finite support and homogeneity once per used gate are explicit hypotheses, not assumptions about arbitrary changed codebooks.

LEAFLESS_ASYMPTOTIC.md sharpens A015's SAME signed correction to Psi/I_g=(1/4)log2 m+1/20+o(1), uniformly over the old posteriors. Exact within-side L0,J1 and binomial factorial expectation determine the leading term. A TWO-SIDED cross bound |cross|/I_g<=a(1-a)log2(9m) removes unknown compensation. The negative normalizer tends to -log2(e)/4 in units of I_g; dropping it would give the wrong constant. The earlier 15/64 coefficient was a weakened lower bound; 1/4 is the computed asymptotic coefficient, not inconsistent data.

The first unpaid universal line is the combined final-reference payment for arbitrary shared/leafless incidence with output mass b tending to zero. Here the actual controller influence supplies a bank bounded below; in general 2rp b may vanish. A correct extension must retain that mass, inherited core/reference cost and all sectors. No fixed-reference obstruction is advertised as a variational or FEI disproof.

# executed validation with domain, arithmetic, commands and outputs

Three frozen specifications preceded their respective jobs. code/check.py uses independent integer Walsh transforms and physical flip counting on m=2,...,7 (21,840 physical entries), checking every coefficient including both cross and within-side sectors, mean/variance/Parseval and influence. Compressed exact Fraction checks run through m=40. Formal fifth powers certify edge occupation bounds and exact root/factorial coefficients without floating signs. Pilot: {results['pilot.json']['assertions']} assertions in {results['pilot.json']['seconds']:.3f}s. Full: {results['checks.json']['assertions']} assertions in {results['checks.json']['seconds']:.3f}s. Decimal values are labeled diagnostics and do not certify the all-m proof.

code/scale_check.py checks {results['scale_checks.json']['assertions']} exact Fraction predicates over six rational scale factorizations and all control subsets r=1,...,4, retaining changing posterior denominators and nonconstant record counts. These are finite algebra fixtures, not invented Boolean counterexamples. code/payment_check.py checks {results['payment_checks.json']['assertions']} predicates, all {results['payment_checks.json']['selected_forests']} nonempty selected sets on m=2,3,4 using independently constructed source-SCC-rooted actual forests, and the rational payment inequalities through m=40. Nonpilot total: {total} exact assertions; the {results['pilot.json']['assertions']} overlapping pilot assertions are separate. All all-dimensional conclusions come from the written arguments, not extrapolation.

Commands from A007: python -X utf8 runs/{ROOT.name}/code/check.py --pilot; same command without --pilot; python -X utf8 runs/{ROOT.name}/code/scale_check.py; python -X utf8 runs/{ROOT.name}/code/payment_check.py; python -X utf8 runs/{ROOT.name}/code/finalize.py. Jobs are sequential, fixed n/domain, no GPU, window or detached process. Frozen memory estimates 80--100 MB are estimates, not measured peaks; no >300 MB compute job was started. The read compute snapshot reported ok and no recent interventions.

Checks that could fail were run or separately proved: root chronology/factorial, singleton s=1, missing cross compensation, denominator positivity, variable posterior under scaling, exactly 2^r subsets, complete control-only sector in the transfer, and inherited residual cost. The Core Lean attempt for the termwise Nat scale-product law returned {lean_status} (exit {lean.get('exit_code')}); out/lean_attempt.json retains the exact source hash, output and command. It does not certify real logarithms or the full proof. Proof rung: analytic source-dependent proof plus independent exact finite checks; independent review of the new result is pending. No Lean certification beyond the actual receipt is claimed.

# proof dependencies and changed downstream conclusions

The new payment uses the previously accepted A007 distributed lift and A015 one-control estimate reconstructed here, with unchanged original posterior and weights. The scale identity is finite algebra under an explicit source homogeneity hypothesis. The sharp asymptotic uses only the exact one-control coefficient and elementary integral/variance bounds. No general graph cost theorem or full-FEI premise is assumed. The inherited source entropy overhead K_ref stays explicit. New claim {claim_id}@1 is narrow author proof/exact checks pending A008/A086/A094 review. Full FEI and the universal constant are unchanged.

Downstream change: the K_m,m scale obstruction is paid by its actual controller influence WITH inherited cost; it no longer blocks this named complete activated residual. Independently refactoring common scales is ruled out as a repair at unchanged final weights. A vanishing-output-mass leafless family is the next relevant stress test, rather than another positive-controller calibration.

# one next mathematical action and independent reviewer

{progress['next_action']} A015/A008 should reconstruct (2)--(7) of KMM_PAYMENT and the posterior-denominator cancellation; A086/A094 should audit the source-residual versus actual-queue distinction and all retained terminal/overhead terms. No messages were sent and no other agent files changed.

# actual persistence receipts or precise save blocker

The four protocol files, four complete mathematical notes, three frozen specifications, own code, exact outputs, Lean attempt and source/file hashes are saved only under A007. code/finalize.py checks exact claim/progress fields, PROGRESS=PACKET_DELTA, output status and 20 MB caps, and writes out/RECEIPTS.json. STATUS has two lines; WORKLOG/LEARNED are updated. Local completion is distinct from independent review, shared registry adoption, supervisor copying and mirror verification, which remain unobserved.

# Universal bridge

C020 whole-set witness cost moves by paying the SAME previously obstructing leafless activated prime family at complete residual R_F<29 I_core, including inherited old reference, empty/nonempty controls and control-only rank/root terms. The negative normalization also has its exact limiting refund, and an exact combined-scale identity prevents moving that bill between intermediate references from being mistaken for progress. No universal constant changes: arbitrary shared incidence with vanishing true-output mass can lose the positive controller bank and remains unpaid. NEXT keeps that exact combined cost and actual 2rp b owner on a vanishing-mass leafless family, which attacks the missing universal payment rather than adding another unrelated class bound.
'''
save(ROOT/'REPORT.md',report)
save(AGENT/'STATUS.md',f'STATE: A007 stage7 locally complete: SAME leafless full residual <29 I_core; exact scale cancellation and Psi/I_g=log(m)/4+1/20+o(1);{total} exact checks PASS; review pending; FEI OPEN.\nNEXT: Pay SAME combined final-reference cost on leafless/shared incidence with b tending to zero, all core sectors and inherited cost retained; A015/A008/A086/A094 review.\n')
for name,text in [('WORKLOG.md',f'\n## {stamp} — A007 substantive stage7\nIndependently reconstructed A015 stage6. Closed the SAME K_m,m complete activated residual at <29 I_core using inherited R_g and actual controller budget. Derived exact intermediate-scale cancellation and sharp signed Psi/I_g asymptotic log(m)/4+1/20. {total} nonpilot exact assertions PASS; pilot {results["pilot.json"]["assertions"]} separate. Core Lean {lean_status}; no full formal certification. FEI OPEN. NEXT: vanishing-b shared/leafless combined payment.\n'),
 ('LEARNED.md','\n## Stage7 durable facts — use the actual controller bank\n- For the SAME activated K_m,m table lambda=1/m,beta=1/m, the full source residual including inherited cost satisfies R_F/I_core<10199/360<29, m>=2. The source entropy overhead stays K_ref; h2<=1<2I_core.\n- Its signed nonempty-data correction nevertheless has Psi/I_g=log2(m)/4+1/20+o(1), uniformly over old posteriors. Negative normalizer/I_g tends to -log2(e)/4; two-sided cross contribution is <=2^-m(1-2^-m)log2(9m). Divergence relative to tiny data influence does not obstruct payment from original total influence.\n- For finite positive homogeneous raw weights t^k w, S_t E_eta_t[beta^k H]=sum(t beta)^k wH. Keeping ALL 2^r control sectors and inherited pR_t cancels old D_t and S_t exactly. At fixed final scale alpha=t beta, the combined selected-mass cost cannot improve by refactoring an intermediate scale, even though the old posterior changes.\n- Remaining C020 gap: control influence is 2rp b and can vanish when true-output mass b tends to zero. Positive-bank calibration must not be promoted to a universal payment. New stage7 results await independent review; A015 new one-control/leafless proof reconstructed without repair, excluding upstream self-authored A007 dependencies.\n')]:
    with (AGENT/name).open('a',encoding='utf-8') as f: f.write(text)
assert len(rd(AGENT/'STATUS.md').splitlines())==2
assert json.loads(rd(ROOT/'PROGRESS.json'))==json.loads(rd(ROOT/'PACKET_DELTA.json'))
sources=[]
for agent,run,names in [('A007','20261013T220854Z-fleet05-A007-root-normalization',['LIFT.md']),('A007','20261014T014217Z-fleet05-A007-root-normalization',['DISTRIBUTED_LIFT.md']),('A007','20261014T100124Z-fleet05-A007-root-normalization',['JOINT_OCCUPATION.md']),('A015','20261021T162002Z-fleet03-A015-minterm-barrier-analysis',['ONE_CONTROL.md','LEAFLESS_SCALE.md','REPORT.md','REVIEW_A007.md'])]:
    for n in names:
        p=AGENT.parent/agent/'runs'/run/n
        sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
js(ROOT/'out/SOURCES.json',sources)
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size})
js(ROOT/'out/RECEIPTS.json',{'saved_at':stamp,'files':receipts,'protocol_fields':'PASS','local_save':'COMPLETE','independent_review':'PENDING','supervisor_mirror':'UNOBSERVED'})
print(json.dumps({'status':'PASS','nonpilot_assertions':total,'lean_status':lean_status,'local_files':len(receipts),'run':str(ROOT)}))
