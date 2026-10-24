from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy

run=Path(__file__).resolve().parents[1]
agent=run.parent.parent; root=agent.parent.parent
last=run.parent/'20261013T215841Z-account05-A066-semigroup-dissipation'
source=root/'agents/A096/runs/20261013T220343Z-account05-A096-live-gap-ledger'
referee=root/'agents/A088/runs/20261013T234248Z-account05-A088-booleanity-referee'
protocolpath=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
def dump(p,x): p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
reviewed=next(c for c in json.loads((source/'CLAIMS.json').read_text()) if c['claim_id']=='A096-TERMINAL-KL-REFUND-AUDIT')
original=copy.deepcopy(reviewed)
reviewed['review_records'].append({'reviewer':'account05/A066','verdict':'ACCEPT_AT_FULL_STATED_SCOPE','reviewer_contributed_repair':False,
 'proof_source':str(run/'AUDIT_A096.md'),'validation_source':str(run/'out/REFUND_FULL.json'),
 'independent_method':'Direct physical Boolean truth tables, new FWHT/prime-log code, complete normalized row and joint likelihood checks; analytic tensor/activation/cutoff reconstruction.',
 'scope':'Finite transport formulas and all fixed ell/sublinear-cutoff supremum equality, constants included analytically; no universal finite payment accepted.',
 'source_claims_file_sha256':hashlib.sha256((source/'CLAIMS.json').read_bytes()).hexdigest()})
reviewed['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A066'
for key in ['exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies']:
    assert reviewed[key]==original[key]
statement='For every m>=2, take the actual Boolean sign F_m(z,x)=(-1)^(sum_j x_(2j-1)x_(2j))-(1-z)1_{x=0} on 2m+1 uniform bits. Set A=2^-m, d=A^2, N=2^(2m), n_plus=(N+2^m)/2, n_minus=(N-2^m)/2 and c(a,b)=((a+b)^2 ln((a+b)^2/(a^2+b^2))+(a-b)^2 ln((a-b)^2/(a^2+b^2)))/2. Then Inf_z=hat F({z})=d, I(F)=m+(2m+1)d, C_z^+=(n_plus-1)c(A-d,d)+n_minus c(A+d,d), ell_z=d^2 ln(1/d^2). Its joint paid rate obeys 2+2d[ln(1/d)-2/(1-A)]<=(C_z^++ell_z)/d<=2-2d+2d ln(1/d), is strictly greater than 2, and tends to 2 from above. At m=2 it exceeds 217/100 by a rigorous rational-log certificate. Its nonempty-row oriented erasure obeys |M_z^+/d-2m ln2|<=8*2^-m; the expensive selected query is not a universal good-coordinate obstruction. H_bits(F)/I(F)<=2+1/m, and total oriented M/I<=(1+2d)ln2; this is not an unbounded FEI-ratio family. This is a narrow stress test of the pending joint singleton budget, not a universal residual payment.'
own={'claim_id':'A066-JOINT-SINGLETON-COEFFICIENT-TWO-OBSTRUCTION','version':1,'exact_statement':statement,
 'hypotheses':['Actual uniform Boolean F_m; m>=2','Natural-log row charges; physical singleton z; empty residual row excluded from C_z^+','Zero log masses vanish; no upper bound on arbitrary terminal-core entropy asserted'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A066'],
 'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':[],
 'review_records':[],'status':'NARROW_PAID_FRAGMENT_VERIFICATION_PROVED_PENDING_REVIEW','supersedes':[],
 'refutes':['Proposed universal joint singleton channel-plus-level coefficient 2 (never claimed proved in prior stages)','Selecting a query solely by |hat f({i})|=Inf_i guarantees bounded selected oriented erasure rate'],
 'first_unproved_line':None,'next_consumers':['A067','A070','A088','A094','A096','B14','B20']}
claims=[reviewed,own]
for c in claims: assert set(c)==set(protocol['required_per_run']['claim_fields'])
dump(run/'CLAIMS.json',claims)
dump(run/'out/REVIEWED_ORIGINAL.json',original)
sources=[protocolpath,root/'BOARD.md',root/'claude/B14/STREAM_NOTES.md',agent/'STATUS.md',agent/'LEARNED.md',last/'DERIVATION.md',last/'CLAIMS.json',source/'REPORT.md',source/'DERIVATION.md',source/'CLAIMS.json',referee/'REPORT.md',run.parent/'20261011T233317Z-account05-A066-semigroup-dissipation/code/check_restrictions.py']
dump(run/'out/SOURCES.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sources])
b=json.loads((run/'out/BENT_CHECK.json').read_text()); r=json.loads((run/'out/REFUND_FULL.json').read_text())
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A066','gap_id':'G-A066-HEAT-INTEGRAL','attempt_id':'A066-bent-paid-fragment-reference-audit-04',
 'method':'Verify pending joint-budget strengthening on actual bent edits; independently reconstruct normalized A096 terminal refund and sublinear admission',
 'mathematical_delta':'Narrow actual five-bit witness forces any joint paid-fragment constant above 2.17; all-m selected erasure remains logarithmic although weighted global bill is bounded. Independently accept A096 terminal-KL refund v1 at full stated scope, without repair; universal payment improvement zero.',
 'deliverable_status':'COMPLETE_LOCAL; NARROW_DIAGNOSTIC_PENDING_REVIEW; SOURCE_BOUND_A096_ACCEPTANCE_SAVED',
 'mathematical_status':'PAID_FRAGMENT_COEFFICIENT_TWO_REFUTED; A096_REFUND_AUDIT_HOLDS; UNIVERSAL_C018_C019_AND_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A066-POSITIVE-RESTRICTION-HEAT-LEDGER','version':2,'proof_source':str(last/'DERIVATION.md'),'acceptance_scope':'Singleton-only paid-fragment scope; still pending independent review, no new acceptance asserted.'},{'claim_id':'A096-TERMINAL-KL-REFUND-AUDIT','version':1,'proof_source':str(source/'DERIVATION.md'),'acceptance_scope':'Independently reconstructed and accepted this stage, full stated transport/cutoff scope only.'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Source-preserving independent review' if j==0 else 'Narrow pending-paid-fragment stress test, no broad candidate'} for j,c in enumerate(claims)],
 'source_artifacts':['REPORT.md','DERIVATION.md','AUDIT_A096.md','SPEC.json','code/check_bent.py','code/check_refund_independent.py','code/finalize.py','out/BENT_CHECK.json','out/REFUND_PILOT.json','out/REFUND_FULL.json','out/EXECUTION_NOTE.md','out/SOURCES.json','out/PERSISTENCE.json'],
 'next_consumers':['A001','A067','A070','A073','A088','A094','A096','A099','B14','B20'],
 'next_action':'Seek an influence-weighted signed-Boolean lower bound for the complete terminal-core KL, or a child-certified query policy with one physical reserve. Test on bent-edit selected-query failure and the exact admitted arbitrary seeds; retain all terminals. A070/A094 review narrow diagnostic; A001/A073 consume A096 independent acceptance.',
 'stagnant_substantive_attempts':0,'blockers':['Actual arbitrary terminal-core divergence or retained global erasure is still unpaid; no finite universal constant known.','Previous A066 v2 and signed-transfer claims remain pending independent review; no new broad candidate opened.'],'packet_ids':['A066']}
assert set(progress)=={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
for name in ['PROGRESS.json','PACKET_DELTA.json']: dump(run/name,progress)
report=f'''# A066 B14: paid-fragment stress test and terminal-refund audit

## exact target, quantifiers, hypotheses and units

Verify the pending singleton heat price and the actual unpaid normalized-reference mechanism for every finite uniform Boolean seed. Natural logarithms for this derivation; reviewed A096 statements retain their original bits. Previous K=(H_nat-b_empty)/2=integral J and finite small-/large-time integrability remain unchanged. This stage tests whether the proved paid coefficient beta=2+2/e^2 can be reduced to 2, then independently audits the retained terminal-core KL under tensor/parity/point activation. No universal entropy integral or residual payment is proved.

## sources actually read, revisions and theorem locators

Read BOARD snapshot 2026-10-14 01:20 UTC, B14 STREAM_NOTES v2 (2026-10-11 23:25 UTC), own STATUS/LEARNED and previous v2 derivation/claims, and execution protocol revision 2026-10-11-execution-v2 in full. B14's original block/majority/addressing target was completed earlier. A088 stage3 REPORT (20261013T234248Z) records actual A067 downstream use of the singleton-only correction, without independent acceptance of our new v2. A096 stage3 (20261013T220343Z) REPORT, DERIVATION equations (1)-(6), full cutoff proof and original claim record supply the useful new dependency. Scoped text search in A067/A070/A079/A088 prevented repeating their bent/padding/channel work; none is a premise of the new elementary diagnostic. Source paths and byte hashes are in out/SOURCES.json.

## complete derivation or exact first unsupported line

DERIVATION.md constructs F_m from a quadratic bent sign on 2m bits by flipping one vertex in exactly one child of a fresh singleton query. Its actual pair histogram gives C_z^+ and ell_z, omitting exactly the empty residual row. A lower bound g(r)>=r^2/2 proves the joint paid rate is greater than 2 for every m>=2 and tends to 2 from above. The five-bit m=2 certificate exceeds 217/100=2.17. Thus the proved paid upper price cannot simply be replaced by 2; no contradiction to beta=2+2/e^2 occurs. Its selected nonempty oriented erasure rate differs from 2m ln2 by at most 8*2^-m. The root weighted bill is nevertheless bounded by M/I<=(1+2d)ln2, and H_bits/I<=2+1/m. An expensive selected coordinate is not a FEI counterexample or a failure of existential good-coordinate payment.

AUDIT_A096.md independently reconstructs the full normalized row/joint likelihoods, source's finite tensor/activation formulas including constants analytically, and all fixed-tail/sublinear-cutoff supremum equality. Verdict HOLDS at full stated scope; no repair contributed. The activation bill M_ge2=qmM(seed)+kq(1-kq) in bits retains the arbitrary seed cost. The first unsupported universal line is still D_f>=sum_i(e_i/I)ln(1/e_i)-K for one finite K, or its global retained-erasure/child-certified stopping-tree equivalent. A coordinate-wise version is too strong; a future claim must price the actual influence-weighted global bill and all terminal costs.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json precedes all jobs. Commands, from the agent folder:

    python -X utf8 runs/{run.name}/code/check_bent.py
    python -X utf8 runs/{run.name}/code/check_refund_independent.py pilot
    python -X utf8 runs/{run.name}/code/check_refund_independent.py full

Bent checks: 64 compressed m=1..64 cases, four direct m=1..4 truth tables, {b['assertions']} predicates in {b['elapsed_seconds']:.4f}s. Exact Fractions and rational log intervals certify the five-bit witness, direct histogram, physical influence and erasure error bound. All-m proof is analytic; finite checks are not extrapolated. The first bent invocation could not certify a shrinking positive difference using unreduced 24-term log enclosures at large m; out/EXECUTION_NOTE.md preserves this limitation. Revised checker uses the same precision and domain, exact logarithms for m<=8 and the proved rational analytic row bound for larger m. New proof/physical-influence checks justify the final bounded replay; only final predicates are counted.

Independent refund pilot: 16 actual functions, 1219 predicates in 0.0363s. Full: 240 actual labeled functions, {r['assertions']} predicates in {r['elapsed_seconds']:.4f}s. Seeds are all nonconstant n=1,2 tables plus four specified n=3 masks; m=1,2, ell=2,3, k=1,2,3; maximum ambient dimension 12. New integer FWHT and direct physical flips check every complete derivative/residual/joint normalizer and refund formula through exact prime-log cancellation, with no author A096 code or floating sign tests. Frozen per-job limit 60s; both full jobs obeyed it. Estimated memory <=100MB, so no >300MB memok trigger. No symmetry quotient, automatic dimension growth, GPU or background worker.

## proof dependencies and changed downstream conclusions

The narrow bent diagnostic is self-contained finite Fourier algebra and scalar convexity; it opens no new broad-payment candidate while prior A066 v2/transfer await review. CLAIMS.json preserves A096-TERMINAL-KL-REFUND-AUDIT v1's exact statement, hypotheses, contributors and recorded hash, appending an independent A066 acceptance. out/REVIEWED_ORIGINAL.json preserves the source record. A096 supplied no repair to our diagnostic and A066 supplied no repair to its audited theorem.

A001/A073/A096/A099/B20 may consume this source-bound independent refund acceptance; activation rarity does not eliminate terminal seed divergence. B14/A067/A070 should reject coefficient-two joint-paid substitutions and per-coordinate refund extrapolations. The existing beta upper bound and exact signed block transfer remain unchanged and not newly independently accepted. A067's already saved singleton-only substitution is observed downstream correction use; central adoption and mirroring are not asserted.

## one next mathematical action and independent reviewer

Derive one influence-weighted signed-Boolean lower bound for the complete terminal-core KL, or a child-certified policy allocating the same global reserve, admitting arbitrary seeds and retaining every leaf. The bent-edit diagnostic must not be used to demand uniform payment at every possible query. A070/A094 independently reconstruct the narrow witness and row bound; A001/A073 consume the independent A096 review. This changes the next attack from reducing already paid constants to actual global residual payment.

## actual persistence receipts or precise save blocker

All four exact-schema protocol files, derivation, independent audit, frozen specification, scripts and certificate outputs are saved locally in this run. STATUS.md has two current lines; WORKLOG.md and LEARNED.md are appended. out/PERSISTENCE.json records reread SHA256/byte checks and JSON/schema verification. Files are below 20MB. No files outside A066 were written. Local persistence is verified; supervisor mirrors, central adoption and independent review of our narrow witness are unverified.

**Universal bridge:** This stage moves C019's paid-fragment audit by forcing its universal joint singleton coefficient above 2.17, and moves C018's terminal-reference chain by independently accepting A096's exact normalized KL/refund transport at full scope. The reduction in the unknown universal residual bound is zero: the actual seed KL lower bound or globally paid retained erasure, with terminal costs, remains missing. NEXT seeks influence-weighted signed-Boolean payment or certified query selection on that same complete reference; this directly attacks the universal unpaid account, whereas further isolated bent or point-edit bounds cannot pay arbitrary terminal cores.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
stamp='2026-10-14T01:29:49Z stage'
(agent/'STATUS.md').write_text('STATE: A066 stage4 saved: joint singleton coefficient 2 refuted (>2.17 at five bits); A096 terminal KL refund v1 independently HOLDS; 667+17389 exact predicates PASS; FEI OPEN.\nNEXT: Price influence-weighted actual terminal-core KL or certified query residual with one physical reserve; retain arbitrary cores/leaves; A070/A094 review narrow witness; prior v2/transfer review pending.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+': Read updated board/lead and A088 downstream correction. Verified pending paid-fragment on bent single-child edits: coefficient 2 false, m2 rate>217/100; all-m tends to2 above, selected oriented erasure~2m ln2 but weighted root bill bounded. Recorded large-m direct-log precision limitation, used proved same-domain analytic bounds. Independently reconstructed and accepted A096-TERMINAL-KL-REFUND-AUDIT v1, no repair; 240 actual functions,17389 exact predicates,52.1717s. Bent final667 predicates,.4573s. Saved files, no universal residual payment.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+': Actual bent single-child point edit F=g-(1-z)1_0 has query d=2^-2m, I=m+(2m+1)d and paid rate>2 for allm>=2 (>2.17 at m2), tending to2 above. Selected M_z^+/d is within8*2^-m of2m ln2, while global M/I<=(1+2d)ln2. A bad selected query is not a global-reference/good-coordinate counterexample. A096 exact terminal refund v1 independently accepted in full scope; activation leaves arbitrary seed divergence and tail bill unpaid. Fixed-precision log differences lose shrinking signs at large dimensions: use analytic row bounds, not unjustified float or automatic precision growth. Next must price global influence-weighted KL or a certified query policy, rather than set paid coefficient2 or demand coordinate-wise refund.\n')
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
for field in protocol['required_per_run']['report_fields']: assert '## '+field in report
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        data=p.read_bytes(); assert len(data)<20*1024*1024
        if p.suffix=='.json': json.loads(data)
        receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=agent/name; data=p.read_bytes(); assert len(data)<20*1024*1024
    receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
assert len((agent/'STATUS.md').read_text().splitlines())==2
dump(run/'out/PERSISTENCE.json',{'verified_at_utc':datetime.now(timezone.utc).isoformat(),'local_saved':True,'mirror_verified':False,'schema_checks':'Exact claim/progress keys; identical packet delta; source-reviewed protected fields preserved; seven report headings/final bridge; JSON parse; STATUS two lines; sizes <20MB','files':receipts})
print(json.dumps({'saved':True,'review':'A096-TERMINAL-KL-REFUND-AUDIT@1 HOLDS, no repair','bent_predicates':b['assertions'],'refund_predicates':r['assertions'],'receipted_files':len(receipts)}))
