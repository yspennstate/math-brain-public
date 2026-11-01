from pathlib import Path
import json,hashlib,datetime

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
statement=('For every Boolean F=g(f_1,...,f_k) on disjoint uniform physical blocks and fair singleton restriction x in block j, set delta Z=Z-(Z+ +Z-)/2, m_i=E f_i, beta=(m_j+ -m_j-)/2, d=Inf_x(f_j), t=E(D_j g)^2, b=E D_j g and M=E F. With Eplus_mu(g)=sum_{S nonempty} P_mu(S)log2(product_{i in S}(1-m_i^2)/P_mu(S)), D=I-Var and e(u)=u log2(1/u), delta Eplus(F)=delta Eplus_mu(g)+t delta Eplus(f_j), delta I(F)=td, delta D_mu(g)=beta^2(t-b^2), and delta H(F)=t delta H(f_j)+T where T=delta Eplus_mu(g)+delta e(M^2)-t delta e(m_j^2). Writing F=A+B f_j, AB=0, A^2+B^2=1, L(a,c)=e(a^2)+e(c^2)-e(a^2+c^2), one has B_x(F)=t B_x(f_j)+R, R=sum_Z L(Ahat_Z+m_j Bhat_Z,beta Bhat_Z)-t L(m_j,beta), and T=R+JS_x(F)-t JS_x(f_j). All identities extend after deterministic contraction. T=0 if beta=0 or the outer gate is a signed dictator. The existing inner magnitude-mismatch/KL bound transports by t only with the signed remainder T retained; vanishing inner mismatch does not force T=0. No universal stopping-tree payment is asserted.')
claim={
 'claim_id':'A024-BIASED-CHILD-TRANSPORT','version':1,'exact_statement':statement,
 'hypotheses':['finite Boolean signs','independent uniform physical inputs','mutually disjoint inner blocks','fair physical singleton query','actual induced product output laws at each child','bits; corrected entropy has no output-variance numerator','deterministic output coordinates contracted before normalized basis or zero-deficit division'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['fleet05/A024'],
 'proof_source':{'path':str(RUN/'BIAS_TRANSPORT.tex'),'other_artifacts':['REPORT.md','BOUNDARY_CREDITS.md','code/check.py','out/VALIDATION.json'],'locators':'equations (1)-(6); exact negative empty-sector subtraction; endpoint section'},
 'proof_dependencies':[{'claim_id':'A056-DISJOINT-COMPOSITION','version':1,'status':'observed A091 independent acceptance; coefficient proof reconstructed in this report'},{'source':'ISOSPECTRAL_SPLICING_CURATED.md','version':'source fe94de760ee2b47545419a7447b492816bd16045; blob 3421c0cbfd22031554befb962ec92cd0c8bb45b9','locator':'Corollary 3.4, equation (3.8)','use':'existing magnitude-mismatch/KL upper bound only'}],
 'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A021','A023','A029','A039','A041','A042','A056','A057','A064','A087','A094','B05','B20']}
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B05','packet_id':'A024',
 'gap_id':'FEI-B05-A024-INITIAL','attempt_id':'A024-01-exact-normalization-transfer',
 'method':'Source-bound repair/application of accepted disjoint composition; exact corrected/full surplus cocycle, negative empty-sector erasure credit, fixed-slice endpoint analysis and exhaustive small Boolean validation',
 'mathematical_delta':'Completed arbitrary-mean erasure subtraction left open in A057; exact signed T links corrected outer drift to full physical restriction; stationary means/dictator outer give T=0; near-dictator inner isospectral pair has T->2 bits; true log(1/mean) crossover and affordable beta-log bank separated from unpaid outer rarity and inner KL charges.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; INDEPENDENT_REVIEW_AND_MIRROR_PENDING',
 'mathematical_status':'PACKET_INTERFACE_RESOLVED_LOCALLY; UNIVERSAL_C019_PAYMENT_AND_FULL_FEI_OPEN',
 'claim_versions_used':['A056-DISJOINT-COMPOSITION@1 (A091 acceptance observed; reconstructed)','source ISOSPECTRAL_SPLICING Corollary 3.4 (source hash receipt pinned)'],
 'claims_created_or_changed':['A024-BIASED-CHILD-TRANSPORT@1'],
 'source_artifacts':['BIAS_TRANSPORT.tex','BOUNDARY_CREDITS.md','REPORT.md','out/SOURCE_RECEIPTS.json','out/SOURCE_EXCERPTS.txt','FROZEN_SPEC.json','FROZEN_SPEC_V2.json','code/check.py','out/PILOT.json','out/VALIDATION.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A057/A029 apply signed erasure residual to A023 overlapping controls at bad nodes, separating betaalog bank from t-rarity and terminal costs; A087/A094 independently reconstruct the empty-sector and slack cocycles.',
 'stagnant_substantive_attempts':0,
 'blockers':['No mathematical access blocker; universal signed residual/inner KL-log stopping payment remains unproved; review, supervisor copies and mirror verification pending.'],
 'packet_ids':['A024']}
claimfields=set(protocol['required_per_run']['claim_fields'])
progressfields=set('packet_ids' if s.startswith('packet_ids ') else s for s in protocol['required_per_run']['progress_fields'])
assert set(claim)==claimfields,(set(claim)^claimfields)
assert set(progress)==progressfields,(set(progress)^progressfields)
for name,data in [('CLAIMS.json',[claim]),('PROGRESS.json',progress),('PACKET_DELTA.json',progress)]:
    (RUN/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
status='STATE: A024 interface complete locally: exact biased-child entropy/slack and negative empty-sector credits; 110,789 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: A087/A094 review; A057/A029 apply signed outer residual at bad nodes of overlapping-control trees, keeping inner KL rebates and terminal entropy.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
log=(f'\n{now} — Completed A024 source-bound normalization interface. Read protocol/board and newly available B05 lead notes; consumed accepted A056 baseline and repaired A057 biased empty-sector gap. Pilot 6,004 assertions (0.119405 s); full 110,789 assertions, 4,096 compositions/8,192 physical splits and seven near-dictator cases (5.469279 s). Exact arithmetic only. Signed T and R remain unpaid universally; no FEI solution, independent review, mirror or downstream use claimed.\n')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(log)
learned='''# Durable A024 facts

Fair physical restrictions preserve uniform untouched inputs; biased outer laws arise only from actual independent child outputs in disjoint composition.

Corrected FEI+ Eplus=sum_nonempty P log2(product coordinate variances/P) has no output-variance numerator. On physical uniform inputs H=Eplus+e(mean^2); Eplus=v H(nonempty spectrum)+v log2(1/v). Always contract deterministic child outputs before normalization or division by deficit.

For F=g(f_i), a_i=E(D_i g)^2 stays bounded at v_i=0; physical influence factors by a_i. A fair query inside j changes a_i affinely in m_j for i!=j, so averaging coefficients cancels all unchanged-child costs.

Exact transport: delta H(F)=t delta H(f_j)+T, T=delta Eplus_outer+delta e(M^2)-t delta e(m_j^2); delta I(F)=t d. The full surplus drift is t times inner surplus drift minus T.

Exact biased erasure repair: B_x(F)=t B_x(f_j)+sum L(Ahat+m Bhat,beta Bhat)-t L(m,beta), AB=0, A^2+B^2=1. Keep the negative empty-sector subtraction. T=R+JS_F-t JS_inner.

At fixed nonzero m, leading beta^2 log(1/beta^2) coefficient in R is nonpositive; at m=0 it is kappa<=t. Iterated beta=o(|m|), m->0 yields kappa beta^2 log(1/m^2), with nonuniform crossover. The betaalog component fits [2/(e ln2)]t d using |beta|<=d. Outer t-rarity, complete signed residual and inner mismatch/KL charges are separate unpaid obligations.

T=0 exactly for stationary child means beta=0 and for a signed dictator outer gate. Inner isospectral children alone do not force composed T=0: x-times-point-defect inner with AND outer has delta H_inner=0, delta I_F=1/2, T->2 bits. It is a calibration, not a bad-node divergence.

All 4,096 two-bit disjoint compositions and 8,192 first-block splits verified by exact rational prime-log identities (110,789 assertions with endpoint cases). Human/agent independent acceptance remains pending. Do not repeat this interface after acceptance without a changed hypothesis or a downstream signed-cost application.
'''
(AGENT/'LEARNED.md').write_text(learned,encoding='utf-8')
for name in ['CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']:
    json.loads((RUN/name).read_text(encoding='utf-8'))
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+f in report for f in protocol['required_per_run']['report_fields'])
rows=[]
for p in sorted(RUN.rglob('*')):
    if not p.is_file() or p.name=='PERSISTENCE_RECEIPT.json': continue
    raw=p.read_bytes(); assert len(raw)<20*1024*1024
    rows.append({'path':str(p.relative_to(RUN)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']:
    raw=p.read_bytes(); rows.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
receipt={'saved_at':now,'schema_checks':'PASS; exact protocol claim/progress fields, required report headings; compatibility copy identical; STATUS exactly two lines','artifacts':rows,'independent_review':'PENDING','supervisor_mirror':'NOT_PERFORMED','downstream_use':'NOT_CLAIMED'}
(RUN/'out/PERSISTENCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'saved':len(rows),'schemas':'PASS','claim':claim['claim_id'],'run':str(RUN)}))
