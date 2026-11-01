from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

run=Path(__file__).resolve().parents[1]; root=run.parents[1]; team=root.parents[1]
proto=Path(r'~\mop_fei100\reports\fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(proto.read_text(encoding='utf-8'))
check=json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))
ind=json.loads((run/'out/INDEPENDENT.json').read_text(encoding='utf-8'))
assert check['status']==ind['status']=='PASS' and not check['pilot']
assert check['counts']['labelled_seeds']==278 and check['counts']['blocks']==2138
assert check['counts']['actual_children']==7106 and ind['seeds']==22
assert ind['singleton_child_pairs']==36
stamp=datetime.now(timezone.utc).isoformat()
def write(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
source=team/'agents/A051/runs/20261023T002518Z-fleet03-A051-near-extremizer-definition'
source_claims=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))
if isinstance(source_claims,dict):source_claims=source_claims.get('claims',[source_claims])
ids=[str(c['claim_id'])+'@'+str(c['version']) for c in source_claims]
write('out/SCOPED_A051_REVIEW.json',{'reviewer':'A002','source':str(source/'RESET_BUDGET.md'),'claim_versions':ids,'verdict':'HOLDS_SCOPED_WITHOUT_REPAIR','accepted_scope':'Section2 equation3 and Section3 original-owner finite adaptive telescope only; reconstructed in RESET_LEDGER Section5','excluded_scope':'directional upper/tolerance bounds, channel log-Sobolev premise, all-k critical budgets, original source census, and universal selected-pair funding','independence':'independent analytic expansion of conserved physical influence and complete child entropy; source bounds not assumed'})
statement=('For every finite uniform Boolean sign h and integer k>=2, let p=2^-k and F=1+1[z=0^k](h-1). '
'Let ell be minimum influence under invertible linear input changes and a minimum under those changes plus character multiplication. '
'Then a(F)=ell(F)=p[ell(h)+k(1-Eh)]. For every original physical DATA block A, with every child h_b retained, '
'rho_A(F)=p rho_A(h)-p E[ell(h_b)-a(h_b)], where rho is expected full-affine child influence release. '
'Writing R_k(mu)=H(F)-pH(h), the complete original bank satisfies '
'D_K(F)+S_Astar(F)=p[D_K(h)+S_Astar(h)]+R_k(mu)-E R_k(mu_b)+Kp E[ell(h_b)-a(h_b)]. '
'After branchwise linear data minimization, querying all SAME activation controls redeems exactly p E[ell(h_b)-a(h_b)] once; '
'queried influence, both reset releases and full final leaf influence telescope to I(F). '
'For bent2 source and any k>=2, source singleton rho=1/2 but activated rho=0; at k2 source K2 query/reset bill0 lifts to positive '
'(120+18log2(3)-49log2(7))/32, certified by 2^120*3^18>7^49. Neither this root nor the tensor-bent examples is claimed genuinely high-K critical.')
claim=dict(claim_id='A002-ACTIVATED-FULL-AFFINE-RESET-LEDGER',version=1,exact_statement=statement,
hypotheses=['finite uniform Boolean signs; normalized real Walsh spectrum; entropy in bits','integer k>=2; all activation controls remain unresolved at the DATA frontier','A is a block of ORIGINAL data coordinates, with every physical branch included','K arbitrary real for bank algebra; K>=0 for the payment interpretation','linear data-only minimum is chosen for the delayed-credit continuation; this achieves full affine activated-child optimum'],
statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A002'],proof_source='RESET_LEDGER.md Sections1--5',
proof_dependencies=['A002-AFFINE-MINIMAL-RARE-ADMISSION@1 activation directional ledger, rederived here','A051 affine parity-basis characterization, elementary finite rank-count proof repeated here']+['SCOPED '+i+': only original-bank/telescope identities, independently rederived' for i in ids],
review_records=[{'reviewer':'A002','scope':'author analytic proof; exact integer/Fraction full finite checker; independent physical/exhaustive-basis implementation by same author','result':'PASS; independent-agent acceptance pending; Lean held before compiler by failed memok'}],
status='PROVED_LOCAL_REVIEW_PENDING',supersedes=[],refutes=['Unregistered transfer rho_A(activation(h))=p rho_A(h) with controls unresolved','Unregistered source-paid-query transport by rarity scaling alone'],first_unproved_line='At a genuine critical witness, select an original proper pair funded by SAME unused S_Astar with mixed refund and every terminal; no lower funding bound follows from this ledger.',next_consumers=['A005','A051','A052','A055','A090','A094'])
write('CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=run.name,stream='B01',packet_id='A002',gap_id='G-R-SELECT',attempt_id='A002-stage8-activated-affine-reset',method='Exact activated parity-basis optimization; all physical data-block child ledgers; source credit-loss guard and deferred same-control redemption.',mathematical_delta='Full-affine activated optimization equals scaled LINEAR seed optimum. Exact lost-translation and mean-profile corrections identify the original child bank; delayed credit is redeemed only after actual controls resolve. No universal FEI constant improves.',deliverable_status='COMPLETE_LOCAL',mathematical_status='AUTHOR_CHECKED_PROOF_AND_EXACT_FINITE_CERTIFICATES; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',claim_versions_used=['A002-AFFINE-MINIMAL-RARE-ADMISSION@1']+ids,claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=['RESET_LEDGER.md','out/CHECK.json','out/INDEPENDENT.json','out/LEAN_ADMISSION.json','out/SCOPED_A051_REVIEW.json','out/SOURCE_RECEIPTS.json'],next_consumers=claim['next_consumers'],next_action='A051/A052 derive one genuine critical proper-pair lower funding/selection inequality from SAME unused S_Astar; any activated source comparison must retain BOTH corrections and the delayed-control asset without new credit; A090/A094 review ledger.',stagnant_substantive_attempts=0,blockers=['Universal critical lower funding/selected-pair step remains open','Source full-affine child credit is unavailable before controls resolve; scalar mean-profile term has no proved sign','Fresh memok failed: compiler and all >300MB jobs held','Independent agent review, registry adoption, supervisor copying and remote mirror not verified'],packet_ids=['A002'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
total=check['counts']['assertions']+ind['assertions']
report=f'''# exact target, quantifiers, hypotheses and units

A002/B01 stage8: determine exactly which FULL affine physical-child reset credit survives rare activation, and whether a source-paid query lifts while controls remain unresolved. Every seed is an actual Boolean sign on a finite uniform cube; entropy and all child bills are in bits. k>=2; every original physical DATA block is covered, with every branch retained. The complete theorem and scalar profile are in RESET_LEDGER. Full FEI remains OPEN. Current owner endpoint23October2026 14:49UTC governs over the older protocol clock.

# sources actually read, revisions and theorem locators

Current BOARD header23October01:01UTC, unchanged B01 STREAM_NOTESv1, own STATUS and preceding stage7 were consumed. Protocol2026-10-11-execution-v2 schema/compute/dispatch rules were retained from their full prior read and loaded for exact validation; earlier baseline campaign and four-manuscript reads are not fresh audits. New substantive sources actually read: A051 current REPORT and RESET_BUDGET Sections1--5; current A005/A052/A055 REPORTs, including A005 zero character release and A055 hidden-pair child exclusion. Source receipts record exact observed bytes. B01's old ledgers and near-erasure admission are already retired; dispatch consumes the new affine reset interface. A read-only two-wording math recall returned background and no matching reset theorem. No internet premise, novelty or external literature claim is used. Wake flagged owner-model/state notes87.5/72.1hours stale; current instructions and source proofs govern.

# complete derivation or exact first unsupported line

RESET_LEDGER proves a(F)=ell(F)=p[ell(h)+k(1-mu)] by exact directional costs and finite basis rank thresholds, including mixed data/control bases. Pointwise Booleanity gives w_h(u)<=1-mu; k>=2 makes every activated parity cost<=1/2, so affine majority centering cannot help. Applying the identity to EVERY physical child yields rho_A(F)=p rho_A(h)-p E(ell-a)(child), and the complete signed bank has the additional scalar mean-profile correction. An explicit prescribed continuation redeems the deferred translation asset only after querying the SAME controls; query influence, both releases and final source terminals telescope exactly once to original I(F).

The bent2 canonical seed loses ALL its scaled singleton reset credit at the activated data frontier. At k2, source query/reset is paid at K2 equality, but the actual activated bill is positive by integer2^120*3^18>7^49. Its full affine-minimal/full-span parent and both actual child entropies are retained. For t>=2 tensor-bent cores, half the scaled source credit survives: rho_i(F)=p/4 rather than p/2; the proof handles the affine-coset character endpoint separately. The example is not a genuine high-K critical witness.

FIRST UNSUPPORTED UNIVERSAL LINE: select a proper ORIGINAL physical pair at an actual finite maximal-deficit minimal witness, lower-funding L_A-K I_A from the SAME unused full-affine child bank, mixed refund and complete terminals. This stage supplies exact transport/corrections and a delayed asset, not that selection theorem.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede jobs. From A002 run python -X utf8 runs/{run.name}/code/check.py --pilot, then without --pilot, and code/independent.py in that run. Final v2 pilot:22 labelled seeds/74 blocks/158 children,1386 assertions PASS in0.1412s. Final v2 full:{check['counts']['labelled_seeds']} labelled seeds n0..3,282 activated fixtures (including four bent2 k2..5 guards),{check['counts']['blocks']} data blocks including empty/full,{check['counts']['actual_children']} actual complementary children, plus fixed tensor-bent t2,t3 guards: {check['counts']['assertions']} assertions PASS in{check['seconds']:.4f}s. Source dimensions and named guards were frozen; no automatic dimension escalation or symmetry quotient. The initial v1 passed32228 assertions; v2 adds the SAME-control delayed-redemption telescope on the unchanged domain, so only the final v2 total is counted.

Arithmetic is integer FWHT, exact Fraction parity costs, exact prime-log entropy vectors and exhaustive source basis checks through3bits. Every activated directional cost, root/child optimum, full coefficient-entropy profile and signed K0/K2/K8 bank is checked. Independent replay uses physical disagreement counts, separate direct characters and EVERY independent parity basis through4bits:22 roots/36 singleton child pairs/{ind['assertions']} assertions PASS in{ind['seconds']:.4f}s. It also certifies the strict guard by integer powers. This is a different implementation by A002, not independent-agent acceptance. Combined final full assertions: {total}; pilot and earlier v1 excluded. Constants, both mean endpoints, zero rank/coefficients, ties, empty/full data blocks and k1 negative-constant failure are covered.

All jobs have55s caps and estimated50--70MB RAM, observed peak unmeasured. Initial compute snapshot:2.4GB free RAM, CPU97.6percent; a later fresh memok failed at1.2GB physical free versus4.0GB required (commit15GB versus8GB required). This changed memory window is why Lean and every>300MB job were held before launch. Bank.lean represents only the cleared-denominator scalar loss identity and is uncompiled. No Lean/kernel certification is claimed. No GPU, detached process, changed running work or heavy search. Proof rung: author-checked analytic proof plus exact finite certificates, independent review pending.

# proof dependencies and changed downstream conclusions

Previous A002 activation directions and affine parity-basis characterization are rederived. A051 RESET_BUDGET Section2 equation3 and Section3 original-owner telescope receive independent scoped HOLDS reconstruction without repair; its channel bound, near-extremal upper bounds and all-k critical budget are not independently accepted here. No unsupported FEI inequality is used. Root full-affine optimality does not imply source full-affine child credit transports unchanged. The correction is a deferred same-owner asset, not a replenished bank; scalar profile and every terminal remain. No registered source theorem is refuted and no universal constant improves.

# one next mathematical action and independent reviewer

A051/A052 should derive the actual critical proper-pair lower funding/selection step with SAME unused S_Astar, mixed refund and complete terminals. Any activation-based comparison must carry BOTH terms in equation5 and redeem equation7 only at the actual control frontier. A005/A055 consume that exact guard; A090/A094 independently reconstruct the mixed-basis proof and two-stage same-owner telescope. Handoff remains local and source-bound; no messages sent.

# actual persistence receipts or precise save blocker

The four protocol files, complete proof, scoped review, frozen specs, helpers and exact outputs are saved only under A002. Finalizer checks exact field sets, statement hash, byte-identical compatibility files, required headings, two-line STATUS and20MB cap. out/PERSISTENCE_RECEIPT hashes run artifacts and the three rolling files. Local save is verified; independent-agent review, registry adoption, supervisor repository copying and brain ingestion remain unverified. Git and brain writes were not run under the standing ownership rules.

## Universal bridge

C019 stopping-tree payment through the full-affine critical-child interface: this stage closes the all-dimensional rare-activation reset ledger, identifies an exact lost-translation and signed mean-profile correction, and proves that the deferred credit is redeemed once only after its original controls resolve. A canonical exact guard disproves source-paid-query transport by rarity scaling alone; no universal entropy is newly paid and no FEI constant improves. The remaining step is lower-funding an actual critical original pair from the SAME unused complete child bank. NEXT targets that funding direction with the now-correct account; another root symmetry or small-influence admission cannot remove the unpaid terminals.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(root/'STATUS.md').write_text('STATE: A002 stage8 saved: exact activated full-affine optimum/ALL data-block bank; deferred credit redeemed once at SAME controls; '+str(total)+' exact checks PASS; FEI OPEN, review pending.\nNEXT: A051/A052 fund actual critical ORIGINAL pair from SAME S_Astar with both mean/translation corrections and full terminals; A090/A094 review ledger; no source-credit scaling shortcut.\n',encoding='utf-8')
tag='stage8 activated full-affine reset ledger'
entries={'WORKLOG.md':stamp+' '+tag+': a(F)=p[ell(h)+k(1-mu)], rhoF=p rhoh-p E(ell-a)children; exact scalar-profile bank and delayed SAME-control redemption proved. '+str(total)+' final full checks PASS; v2 adds two-stage same-owner telescope, superseding v1 count32228. Bent2 sourceK2 paid query becomes positive bill; integer certificate saved. Fresh memok1 held Lean/large jobs; FEI OPEN.','LEARNED.md':'Stage8 durable: rare activation k>=2 converts FULL affine optimum into scaled LINEAR seed optimum plus control energy. DATA-frontier full-affine credit loses p E(ell-a)children; after linear child reset and actual SAME-control query that exact amount is redeemable once, with pk(1-mu) queried energy and complete final source terminals. The exact bank also retains R_k(mu)-E R_k(mu_child), of unasserted sign. Canonical bent2 activation has zero DATA release despite source1/2; tensor-bent t>=2 keeps p/4 versus scaledp/2. Root affine/full-span/weak hypotheses do not pay this bill; genuine critical child eligibility still required.'}
for name,entry in entries.items():
    f=root/name;old=f.read_text(encoding='utf-8')
    if entry not in old:
        with f.open('a',encoding='utf-8') as out:out.write('\n'+entry+'\n')
paths=[proto,team/'BOARD.md',team/'claude/B01/STREAM_NOTES.md',source/'RESET_BUDGET.md',source/'CLAIMS.json',team/'agents/A005/runs/20261022T231421Z-fleet03-A005-noncircular-endpoint-referee/REPORT.md',team/'agents/A052/runs/20261021T222218Z-fleet03-A052-critical-source-structure/REPORT.md',team/'agents/A055/runs/20261022T233657Z-fleet03-A055-extremal-obstruction-referee/REPORT.md',root/'runs/20261021T210845Z-fleet03-A002-hardness-preserving-transformations/ADMISSION_PROOF.md']
write('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'observed_at':stamp,'mutable_observation_not_revision':p.name in ['BOARD.md','STREAM_NOTES.md']} for p in paths])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert all('# '+h in report for h in protocol['required_per_run']['report_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((root/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
        b=p.read_bytes();assert len(b)<20_000_000;receipts.append({'path':str(p.relative_to(run)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
rolling=[{'path':str(root/n),'sha256':hashlib.sha256((root/n).read_bytes()).hexdigest()} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
write('out/PERSISTENCE_RECEIPT.json',{'status':'PASS','utc':stamp,'validation':'exact schemas, statement hash, required headings, identical compatibility copy, two-line STATUS,20MB cap','local_only':True,'artifacts':receipts,'rolling_files':rolling})
print(json.dumps({'status':'PASS','run':str(run),'assertions':total,'artifacts':len(receipts),'full_fei':'OPEN','review':'PENDING','Lean':'HELD_NO_COMPUTE_ADMISSION'}))
