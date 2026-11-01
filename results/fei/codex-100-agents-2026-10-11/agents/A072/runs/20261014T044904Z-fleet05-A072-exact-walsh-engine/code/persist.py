import json,hashlib,copy
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1]
SOURCE=TEAM/'agents/A080/runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard'
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
now=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
validation=read(R/'out/validation.json');boundary=read(R/'out/boundary_validation.json')
assert validation['passed'] and boundary['passed'] and boundary['queries']==8
source=next(c for c in read(SOURCE/'CLAIMS.json')['claims'] if c['claim_id']=='A080-REPEATED-ESCAPE-RETURN-NOGROWTH')
assert sha(source['exact_statement'].encode())==source['statement_sha256']
review={'reviewer':'A072','reviewed_at':now,'verdict':'HOLDS','scope':'Exact unchanged source theorem, common-policy steps plus complete rare one-flip episodes and terminal prefixes only','kind':'Independent direct centered interpolation, Hamming-weight edge polynomial reconstruction, two-interval rational Bernstein certificate and analytic episode/event ownership proof','contributor_conflict':'No substantive repair supplied; source proof is valid unchanged. A072 prior one-flip work is acknowledged source context, not an independent acceptance of its own erasure theorem.','artifacts':['INDEPENDENT_PROOF.md','out/continuum_certificate.json','out/validation.json'],'not_accepted':['All arbitrary mixed sign words or shared-data substitutions','Absolute starting-core H/I or C018/C019 bound','Later A075/A071 absolute-variation claims']}
claim=copy.deepcopy(source);claim['review_records'].append(review);claim['status']='INDEPENDENTLY_ACCEPTED'
for field in ('claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies'):
    assert claim[field]==source[field]
save('CLAIMS.json',[claim]);save('out/REVIEW.json',{'source_run':str(SOURCE),'source_claim_id':source['claim_id'],'source_version':source['version'],'source_statement_sha256':source['statement_sha256'],'review':review})
positive=[];query_excess=[]
for p in sorted((R/'out').glob('boundary_case_*.json')):
    x=read(p)
    if x['delta_C_sign']=='POSITIVE':positive.append({'gate':x['gate'],'block':x['block'],'inner_coordinate':x['inner_coordinate'],'delta_C_bounds':x['delta_C_bounds'],'normalized_curvature_bounds':x['normalized_curvature_delta_C_over_Inf']})
    from fractions import Fraction
    assert Fraction(x['full_query_excess_at_K4'][0])>0
    query_excess.append({'gate':x['gate'],'block':x['block'],'inner_coordinate':x['inner_coordinate'],'Delta_H_minus_4Inf_bounds':x['full_query_excess_at_K4'],'sign':'STRICTLY_POSITIVE'})
assert len(positive)==2
save('out/BOUNDARY_HANDOFF.json',{'actual_core_negative_support':[0,1,2],'core_dimension':6,'parent_dimension':36,'physical_queries':8,'positive_curvature_cases':positive,'full_query_excess_at_rate4':query_excess,'scope_warning':'True entropy decrement, not B_i. Only these8 tagged queries checked; no assertion about all physical queries.','equation':'Delta H(F)-K Inf_F = q_j(Delta H(g_j)-K Inf_g_j)+C_parent-average C_child','payment_status':'OPEN; positive curvature cannot be dropped and all8 tagged full-query excesses are positive at rate4. No arbitrary unused child surplus certified.','next_consumers':['A075','A089','A074','A092']})
positive_text='; '.join(f"{x['gate']} block{x['block']} inner-coordinate{x['inner_coordinate']}" for x in positive)
next_action='A075/A089 use NEXT_INTERFACE.md equation(B) to fund positive terminal curvature after one actual non-flat core query from one certified unused child surplus, retaining both complete child bills; A074/A092 audit the two-box source review and constant-child endpoint cases.'
progress=dict(protocol_revision=read(PROTO)['revision'],run_id=R.name,stream='B15',packet_id='A072',gap_id='G-R-SELECT',attempt_id='A072-COMPOSITION-5',method='Independent reconstruction of A080 repeated-cycle theorem; exact first-physical-core-query terminal interface and endpoint-aware non-flat fixtures',mathematical_delta='A080 repeated-escape/return upper correction (1731/44)Var(seed)/I(seed) independently HOLDS at unchanged scope; replaces stage4 repeated-cycle warning for this strategy. Positive terminal correction after a physical core query remains:8 exact non-flat cases yield2 positive,6 negative curvatures. Complete initial and child entropy retained.',deliverable_status='COMPLETE_LOCAL_SAVED_SOURCE_REVIEW_HOLDS',mathematical_status='NAMED_CYCLE_MECHANISM_INDEPENDENTLY_CLOSED_TERMINAL_CORE_AND_FEI_OPEN',claim_versions_used=[source['claim_id']+'@1'],claims_created_or_changed=[source['claim_id']+'@1 (local independent review)'],source_artifacts=['SPEC.json','BOUNDARY_SPEC.json','INDEPENDENT_PROOF.md','NEXT_INTERFACE.md','out/REVIEW.json','out/continuum_certificate.json','out/validation.json','out/boundary_validation.json','out/BOUNDARY_HANDOFF.json','out/source_receipts.json','out/manifest.json'],next_consumers=['A080','A075','A089','A074','A092','A071','B15','B20'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['No noncircular absolute bound for the retained arbitrary starting entropy/erasure ratio.','Positive physical-query terminal curvature has no universal certified child-surplus owner.','Shared registry adoption, supervisor mirroring and downstream use are not verified.'],packet_ids=['A072'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Independently reconstruct A080-REPEATED-ESCAPE-RETURN-NOGROWTH@1 for EVERY actual finite uniform Boolean seed, all finite sequences of the specified common-sign h policy and complete rare-triggered J escape episodes (a terminal prefix is allowed). Copies are identical and disjoint. Entropy is in bits. Verdict: HOLDS at its unchanged scope, without repair. The complete starting H/I is retained, and the upper increase is at most(1731/44)Var(seed)/I(seed)<40. This is not a universal FEI bound.

A second, explicitly frozen finite application checks the next physical-query boundary: actual36-bit h/J compositions of six copies of the non-flat six-bit core negative on{{0,1,2}}. Eight tagged queries certify the complete terminal correction with constant children allowed;2 curvatures are positive and6 negative. All8 tagged queries have true entropy decrement strictly above4 times physical influence, including the negative-curvature cases. This is not an erasure B_i claim or an assertion about every physical query. No arbitrary child-surplus payment is asserted.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2 was read in full. BOARD.md supervisor snapshot2026-10-14 04:40 UTC and B15 STREAM_NOTES.md v2 unchanged2026-10-11 23:25 were read; own stage4 STATUS, helper and proof supplied retained context. The original lead packet is complete, so protocol dispatch consumes A080's explicit review request rather than repeating its baseline Walsh witnesses. No disagreement with the lead's mathematical statements.

Source A080 run20261014T034416Z: complete REPORT, PROOF, CLAIMS; symbolic.py was read, and persist.py hash-convention lines were read. Source exact statement SHA256 is {source['statement_sha256']}, preserved verbatim. A075 run20261014T034311Z and A071 run20261014T042108Z REPORT material was read as current dispatch context, including their retained-core warning; their stronger legal-word/signed-variation theorems are not independently accepted here. No other agent's code was imported or run. Own earlier FWHT and rigorous logarithm definitions are the only reused executable helpers. out/source_receipts.json binds all current source artifacts and own helper dependencies actually used; literature and campaign context from earlier stages are not represented as a new audit.

# complete derivation or exact first unsupported line

INDEPENDENT_PROOF.md reconstructs the full source theorem: the exact signed entropy ledger H(F)=QH(g)+C, physical influence I(F)=QI(g), C=H_p(k)-Qh2(Var(g)); spectral Poincare monotonicity of mu=Var/I; common-step contraction mu_next<=2mu/3 on the entire bias interval; common price<=8mu; full one-flip episode price<=(225/44)mu_start; and one episode per common-step count. Two separately summed geometric series give(1731/44)mu_seed for arbitrarily many eligible cycles. The initial H/I survives every telescope. Exact Bernstein positivity on just two closed half-intervals replaces the source's16-box representation; minimum coefficient23/20. No finite sample is promoted to a continuum claim.

NEXT_INTERFACE.md gives the concrete physical continuation. If coordinate i of core block j is actually queried, q_j stays fixed, the other q_l average affinely, and Delta H(F)=q_j Delta H(g_j)+Delta C, with Delta C=C_parent-average C_child. Thus the rate-K excess is q_j(Delta H(g_j)-K Inf_i(g_j))+Delta C. Complete other-core entropy and both queried-core children remain in this identity. Positive frozen cases are: {positive_text}. The exact outward intervals, physical edge sums and full terminal data are saved, including the p_child=0 endpoint.

First unsupported universal line: certify a genuinely unused actual child surplus paying that positive Delta C together with the inherited queried-core excess, or otherwise pay the arbitrary initial core bill. Merely invoking I-h2(p)>=0 or the composition mu budget does not establish this physical payment. No arbitrary mixed-sign, shared-data, C018 total-erasure or C019 stopping-tree bound follows.

# executed validation with domain, arithmetic, commands and outputs

SPEC.json was frozen before the main pilot. From A072, commands were `python -X utf8 runs/{R.name}/code/audit.py --pilot` and the same without `--pilot`. Pilot passed {read(R/'out/pilot.json')['assertions']} assertions in {read(R/'out/pilot.json')['runtime_seconds']:.6f}s. Full passed {validation['assertions']} assertions in {validation['runtime_seconds']:.6f}s:9 rational profiles, all12 directional pivotal polynomials,2 full-interval Bernstein boxes,8 actual12-bit parents,32768 exact signed coefficient matches and96 independent physical coordinate edge counts. The structural coefficient/inverse/edge checks precede entropy estimates. Parent entropy identities enclosed around zero are diagnostics; the exact coefficient factorization and analytic chain rule establish the identities. Generic h/J parent cases outside a gate's policy domain test structure only and do not extend its entropy-price theorem.

BOUNDARY_SPEC.json was frozen before the second pilot. Commands were the same prefix with `code/boundary.py --pilot` and then without `--pilot`. Pilot passed {read(R/'out/boundary_pilot.json')['assertions']} assertions in {read(R/'out/boundary_pilot.json')['runtime_seconds']:.6f}s. Full passed {boundary['assertions']} assertions in {boundary['runtime_seconds']:.6f}s, within its frozen120s cap. It checks8 compressed actual36-bit physical queries and16 child states without a full36-bit table. The core and children pass direct integer Walsh/Parseval/sign inverse/edge checks. Every outer rational expansion, including endpoint p=0, passes Parseval, inverse at all64 sign-valued truth points and spectral-vs-weighted-edge influence. Each selected physical edge is separately summed over32 core fibers and32 other-outer assignments.2 strict positive and6 strict negative Delta C signs use outward intervals, not floating displays.

All arithmetic for decisions is arbitrary integer/Fraction with own48-term positive atanh-series logarithm enclosure, explicit tail and96-bit outward log2 rounding. Estimated memory100MB per job, peak unmeasured; no expected>300MB job and no memok invocation required. All pilots were below60s; jobs were serial, with no automatic dimension increase, GPU, detached process or outside write. Completed cases were checkpointed immediately. The two full validations total {validation['assertions']+boundary['assertions']} exact/interval assertions; no failing mathematical assertion occurred.

# proof dependencies and changed downstream conclusions

The local claim copy preserves A080's exact statement, hypotheses, hash, contributors and source proof, adding only an independent review/status. The proof reconstructs the entire dependency chain from actual gate counting, orthogonality, Shannon chain rule, proved scalar inequalities, two rational polynomial boxes and geometric event ownership. No substantive repair was supplied and no new broad claim is opened. The review does not certify A072's own prior erasure-loss theorem or A075/A071's larger legal-word theorems.

Downstream change: A072 stage4's unpriced repeated-escape entropy warning is retired for the EXACT A080 strategy. Its unknown starting core H/I remains; named-cycle depth growth from a fixed seed is no longer an unbounded-ratio route. The physical-boundary cases replace a vague terminal warning with a signed Delta C that has actual positive witnesses. They do not refute FEI, a paid policy or source A080's composition theorem.

# one next mathematical action and independent reviewer

{next_action} In particular use the non-flat constant-child endpoint with all original child weights; demonstrate the reserve owner rather than postulating H<=K(I-h2(p)). This is the shortest next step toward a universal payment because the legal repeated-cycle mechanism is already paid and independently reconstructed.

# actual persistence receipts or precise save blocker

All four protocol files, two frozen specs, independent proof, boundary interface, exact code and checkpointed outputs are saved locally in this run. CLAIMS preserves the source version/hash; PROGRESS and PACKET_DELTA are byte-identical with packet_ids=[A072]. Rolling STATUS is two lines; WORKLOG and LEARNED are updated. out/manifest.json binds sizes/SHA256 (excluding itself); every artifact is below20MB. out/schema_validation.json records protocol field/hash checks. Local independent review is complete; shared registry adoption, supervisor copying, remote mirrors and downstream use remain unverified. All writes were inside A072; no messages were sent.

## Universal bridge

This stage moves B15's retained-terminal signed-composition bridge adjacent to C018/C019 by independently closing A080's arbitrarily repeated named escape/return entropy-growth route at additive(1731/44)Var(seed)/I(seed), with the complete starting H/I retained. It also isolates the first physical-query correction Delta C on8 actual non-flat boundary cases,2 positive and6 negative. No universal FEI constant, total-erasure C018 inequality or C019 physical-tree payment is obtained. The exact remaining bridge is payment of the arbitrary retained core and positive terminal curvature from an exclusively owned actual child surplus. NEXT targets that signed physical transfer because another fixed-seed cycle/depth search lies inside an already proved bounded mechanism and cannot remove the unpaid universal starting bill.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A072 stage5 saved: A080 global-cycle theorem independently HOLDS unchanged; two-box contraction certificate;8 non-flat physical queries give2 positive/6 negative terminal curvatures; FEI OPEN.\nNEXT: A075/A089 pay Delta C after an actual non-flat core query from one unused child surplus, retaining full terminals; A074/A092 audit INDEPENDENT_PROOF.md and endpoint fixtures.\n',encoding='utf-8')
entry=f'\n2026-10-14 stage5 ({R.name}): Independently accepted A080 repeated escape/return theorem unchanged; exact2-box continuum certificate min23/20,32768 signed physical coefficients and96 edge counts. Non-flat first-query extension:8 actual compressed36-bit queries,2 positive/6 negative terminal curvatures, constant children retained. Full jobs passed {validation["assertions"]+boundary["assertions"]} assertions. Retired stage4 cycle entropy warning at named scope; arbitrary starting-core payment and physical Delta C ownership remain open.\n'
if R.name not in (A/'WORKLOG.md').read_text(encoding='utf-8'):
    with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
learn='\n2026-10-14 stage5: A080-REPEATED-ESCAPE-RETURN-NOGROWTH@1 independently HOLDS: mu=Var/I contracts<=2/3 at common h, never increases at J;8mu per common step and225/44 mu per full escape sum to1731/44 mu_seed for all eligible cycles. Initial H/I remains. The P polynomial has positive Bernstein coefficients on just[0,1/2],[1/2,1], min23/20. At a physical query in block j, q_j stays fixed and other q_l average affinely, so Delta H(F)=q_j Delta H(g_j)+C_parent-average C_child, including constant children. Actual rare non-flat core negative on{0,1,2} produces strictly positive terminal curvature in2 of8 frozen h/J queries; this correction cannot be discarded or paid by merely naming I-h2(p). No generic child owner or FEI theorem follows.\n'
if '2026-10-14 stage5:' not in (A/'LEARNED.md').read_text(encoding='utf-8'):
    with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(learn)
followup='\n2026-10-14 stage5 boundary sign audit: All8 frozen physical queries have Delta H(F)>4 Inf(F), even the6 with negative Delta C. Positive Delta C occurs only in J block0 (i=0 and2). These are true-decrement diagnostics, not erasure B_i or all-coordinate assertions; inherited core decrement must be retained along with terminal curvature. Exact bounds are in out/BOUNDARY_HANDOFF.json of '+R.name+'.\n'
for filename in ['WORKLOG.md','LEARNED.md']:
    if '2026-10-14 stage5 boundary sign audit:' not in (A/filename).read_text(encoding='utf-8'):
        with (A/filename).open('a',encoding='utf-8') as f:f.write(followup)
sources=[PROTO,TEAM/'BOARD.md',TEAM/'claude/B15/STREAM_NOTES.md']+[SOURCE/x for x in ['REPORT.md','CLAIMS.json','PROOF.md','code/symbolic.py','code/persist.py']]
sources += [TEAM/'agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge/REPORT.md',TEAM/'agents/A071/runs/20261014T042108Z-fleet05-A071-search-space-design/REPORT.md']
sources += [A/'runs/20261014T020611Z-fleet05-A072-exact-walsh-engine/code/verify.py',A/'runs/20261013T222130Z-fleet05-A072-exact-walsh-engine/code/check.py',A/'runs/20261012T004036Z-fleet05-A072-exact-walsh-engine/EXACT_WALSH_INTERFACE.py',A/'runs/20261011T220909Z-fleet05-A072-exact-walsh-engine/EXACT_WALSH_INTERFACE.py']
assert all(p.exists() for p in sources)
save('out/source_receipts.json',{'captured_at':now,'note':'Board/notes are dispatch context; source claim and proof audited at exact scope. Source executable code was read only, never imported or executed. Own imported helper chain is bound here.','sources':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sources]})
protocol=read(PROTO)['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert set(claim)==set(protocol['claim_fields'])
assert all('# '+field in report for field in protocol['report_fields'])
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
save('out/schema_validation.json',{'passed':True,'protocol_fields':'exact sets','source_statement_and_hash_preserved':True,'progress_delta_byte_equal':True,'rolling_status_lines':2,'full_validations_pass':True,'independent_review_verdict':'HOLDS_UNCHANGED_SOURCE_SCOPE'})
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='manifest.json':
        b=p.read_bytes();assert len(b)<20_000_000
        manifest.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':sha(b)})
save('out/manifest.json',{'saved_at':now,'files':manifest,'rolling_files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'regenerate':['python -X utf8 code/audit.py --pilot','python -X utf8 code/audit.py','python -X utf8 code/boundary.py --pilot','python -X utf8 code/boundary.py','python -X utf8 code/persist.py'],'remote_adoption':'NOT_VERIFIED'})
print(json.dumps({'saved_artifacts':len(manifest)+1,'reviewed_claim':source['claim_id']+'@1','verdict':'HOLDS','positive_boundary_cases':positive_text,'schema':'PASS'}))
