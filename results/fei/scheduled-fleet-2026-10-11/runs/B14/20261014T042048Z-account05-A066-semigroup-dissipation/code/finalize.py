from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
run=Path(__file__).resolve().parents[1]; agent=run.parent.parent; root=agent.parent.parent
upstream=root/'agents/A100/runs/20261014T034838Z-account05-A100-release-and-continuation-ledger'
original073=root/'agents/A073/runs/20261014T023508Z-account05-A073-certified-logarithms'
source096=root/'agents/A096/runs/20261014T013836Z-account05-A096-live-gap-ledger'
protocolpath=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
original=next(c for c in json.loads((upstream/'CLAIMS.json').read_text()) if c['claim_id']=='A100-BINARY-REMAINDER-JENSEN-BOUND')
review=copy.deepcopy(original)
review['review_records'].append({'reviewer':'A066/account05','verdict':'ACCEPT_AT_FULL_STATED_SCOPE_NO_REPAIR','contributor_conflict':False,'material_repair_to_reviewed_version':False,
 'proof_source':str(run/'DERIVATION.md'),'locator':'Section 4 independent specialization/Jensen reconstruction','validation_source':str(run/'out/CHECK_FULL.json'),
 'independent_method':'Direct truth tables/physical edges, own exact prime-log complete row and quotient identities, all labeled 2-bit independent spectators; analytic monotonicity and integer margin.',
 'scope':'Entire original explicit-family Jensen theorem and spectator/debit guards; no acceptance of arbitrary-core payment.',
 'source_claims_sha256':hashlib.sha256((upstream/'CLAIMS.json').read_bytes()).hexdigest()})
review['status']='INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A066'
for k in ['exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies']:assert review[k]==original[k]
statement='For any r>=1 Boolean control gate q, any even quadratic bent core dimension d>=4, delta=2^-d and F(z,y)=b_d(y)+1_{y=0}(q(z)-1), write a=qhat(empty), alpha=1-a, beta_i=qhat({i}), e_i=Inf_i(q). For a relevant control i, Inf_i(F)=delta e_i. In its complete normalized Fourier residual/derivative laws r_i and mu_i, retain every residual control subset U and discard only core T. The only nonzero conditional KL loss cell is U=empty. Put c_sigma=1-2alpha sigma sqrt(delta)+delta(alpha^2+beta_i^2), R_i=1+delta(a^2+beta_i^2-1), D0_i=sum_sigma(1+sigma sqrt(delta))/2 ln(R_i/c_sigma). Then lost weighted KL L_i=delta beta_i^2 D0_i, sum_i L_i<=(256/9)delta^2 W1(q)<=(256/9)delta I_controls(F). Actual full quotient row price is M_i^C=delta sum_(U nonempty)qhat(U+i)^2 ln((qhat(U)^2+qhat(U+i)^2)/qhat(U+i)^2)+delta beta_i^2 ln(R_i/(delta beta_i^2))=M_i(F)+L_i. Every finite adaptive control-only singleton stopping tree obeys sum_v w_v L_i(F_v)<=(256/9)delta[I(F_root)-E I(F_leaf)], retaining all leaf entropy. For one first paired-core query in original d>=6, the edited child G=b_(d-2)(Y)+1_{w=0,Y=0}(q-1) has delta0=2^(-(d-2)), theta=1/2 and point mass delta_p=theta delta0. Retaining residual U and the dummy w Fourier occupancy W gives sum_i L_i(G)<=(256/9)theta^2 delta_p I_controls(G), also hereditary under control-only stopping. For negative-AND q, deleting W as well adds exact binary conditional KL with extra local rate at least ln(7/(4delta0))/4, unbounded as d grows. These are narrow lost-refund payments only; complete retained row prices, informative flag costs and actual core/gate leaf entropy are not declared paid, and no arbitrary non-flat-core or universal FEI bound is asserted.'
own={'claim_id':'A066-ARBITRARY-GATE-CONDITIONAL-REFUND-DEBIT','version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform actual Boolean q, any control arity; quadratic bent base at specified all-zero point','Natural-log lost KL; complete reference marginalized, never conditioned on derivative support','Base d>=4; first paired-core exposure original d>=6; no arbitrary data-query heredity asserted','Stopping trees query only controls after the specified possible first exposure; actual terminal functions and costs retained'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A066; prior two-bit boundary family credited to A073; consumed A100 Jensen interface'],
 'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':[],
 'review_records':[],'status':'NARROW_CONDITIONAL_INTERFACE_AUTHOR_PROVED_PENDING_REVIEW','supersedes':[],
 'refutes':['The same core-discarding quotient retains a uniformly small local loss after an arbitrary first physical core query, without keeping new informative occupancy'],
 'first_unproved_line':None,'next_consumers':['A067','A070','A073','A096','A100','A001','A085','A094','B14','B20']}
claims=[review,own]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
dump(run/'CLAIMS.json',claims);dump(run/'out/REVIEWED_ORIGINAL.json',original)
inputs=[protocolpath,root/'BOARD.md',root/'claude/B14/STREAM_NOTES.md',agent/'STATUS.md',run.parent/'20261014T012949Z-account05-A066-semigroup-dissipation/DERIVATION.md',source096/'DERIVATION.md',original073/'REPORT.md',original073/'DERIVATION.md',upstream/'REPORT.md',upstream/'REVIEW.md',upstream/'CLAIMS.json']
dump(run/'out/SOURCES.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs])
main=json.loads((run/'out/CHECK_FULL.json').read_text());tree=json.loads((run/'out/TREE_FULL.json').read_text());exposure=json.loads((run/'out/EXPOSURE_CHECK.json').read_text())
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A066','gap_id':'G-A066-HEAT-INTEGRAL','attempt_id':'A066-conditional-refund-control-exposure-05',
 'method':'Consume positive-erasure Jensen interface by independent review; exact arbitrary-gate conditional partition, single control-influence debit and first-data informative flag correction',
 'mathematical_delta':'Extend two-bit conditional remainder to any Boolean control gate with sum lost KL <=(256/9)delta I_controls, hereditary control-only stopping. First core query remains paid only if newly informative dummy occupancy is retained; deleting it adds unbounded local binary KL. Independently accept A100 Jensen v1; no universal FEI constant improvement.',
 'deliverable_status':'COMPLETE_LOCAL; NARROW_EXTENSION_PENDING_REVIEW; SOURCE_BOUND_A100_ACCEPTANCE_SAVED','mathematical_status':'CONDITIONAL_REMAINDER_AND_FIRST_EXPOSURE_AUTHOR_PROVED; A100_JENSEN_HOLDS; UNIVERSAL_RETAINED_ROWS_AND_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A100-BINARY-REMAINDER-JENSEN-BOUND','version':1,'proof_source':str(upstream/'REVIEW.md'),'acceptance_scope':'Full original scope independently reconstructed this stage, no repair.'},{'claim_id':'A066-POSITIVE-RESTRICTION-HEAT-LEDGER','version':2,'proof_source':str(run.parent/'20261013T215841Z-account05-A066-semigroup-dissipation/DERIVATION.md'),'acceptance_scope':'Existing singleton-only stopping identity contextual application, pending independent review; no new acceptance claimed.'}],
 'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':1,'change':'Source-preserving independent acceptance'},{'claim_id':own['claim_id'],'version':1,'change':'Narrow conditional quotient/history extension, no new broad payment candidate'}],
 'source_artifacts':['REPORT.md','CLAIMS.json','DERIVATION.md','SPEC.json','TREE_SPEC.json','EXPOSURE_SPEC.json','code/check_quotient.py','code/check_tree.py','code/check_exposure.py','code/finalize.py','out/CHECK_PILOT.json','out/CHECK_FULL.json','out/TREE_PILOT.json','out/TREE_FULL.json','out/EXPOSURE_CHECK.json','out/SOURCES.json','out/PERSISTENCE.json'],
 'next_consumers':own['next_consumers'],'next_action':'A070/A085 review arbitrary-gate debit and first-exposure flag. Preserve the same complete terminal reference after the next non-flat/core or overlapping-data split; pay both retained price and exact conditional loss once from available certified child slack, not alphabet size or reused control influence.',
 'stagnant_substantive_attempts':0,'blockers':['No universal payment for complete retained gate/core rows and actual terminal entropy.','Flat-core proof does not imply arbitrary-data heredity; new informative flags must be retained or paid.'],'packet_ids':['A066']}
assert set(progress)=={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:dump(run/name,progress)
count=main['assertions']+tree['assertions']+exposure['assertions']
report=f'''# A066 B14: conditional refund with an owned control ledger

## exact target, quantifiers, hypotheses and units

For every Boolean control gate of every finite arity, quantify the actual conditional-edge KL lost when compressing the bent-core Fourier index; retain the complete reference, retained row and physical terminals. Nats in the new proof, bits in reviewed A100 statement. Base quadratic bent dimension d>=4; first paired-core exposure original d>=6. The previous finite heat integral K=(H_nat-b_empty)/2 and its endpoint integrability are unchanged. This is a narrow C018/C019 quotient/history extension, not full FEI.

## sources actually read, revisions and theorem locators

Read BOARD supervisor snapshot 2026-10-14 04:19 UTC, all B14 STREAM_NOTES v2 (2026-10-11 23:25 UTC), own STATUS and prior stage derivation, plus execution protocol 2026-10-11-execution-v2 in full. Current board directions shift from the completed lead block calibration to actual conditional-reference and terminal-slack transfer. Read A096 stage4 DERIVATION sections1-5, A073 stage4 REPORT/DERIVATION positive-erasure family, and A100 stage4 REPORT/REVIEW/CLAIMS Jensen result. out/SOURCES.json pins original source bytes. No external paper theorem or new Internet result is a premise.

## complete derivation or exact first unsupported line

DERIVATION.md gives the complete source-independent proof. For F=b_d+1_zero(q-1), retain residual control Fourier subset U while discarding bent-core T. Every nonempty-U cell has a conditionally common uniform core law. The only lost refund is L_i=delta beta_i^2 D0_i at U=empty. Exact unequal-sign Jensen algebra and delta<=1/16 yield sum_i L_i<=(256/9)delta^2 W1(q)<=(256/9)delta I_controls(F), uniformly in arbitrary gate arity. The actual quotient price M_i^C=M_i+L_i is explicitly displayed, including its large root log term. This prices lost KL only.

Control restrictions preserve the actual family. Every finite adaptive control-only singleton stopping prefix therefore spends at most (256/9)delta times its removed physical influence; all terminal q_leaf/core entropy and K remain. After one first paired-core query, the edited child has one physical dummy. Retaining that dummy's Fourier occupancy gives the same type of bound, with coefficient (256/9)theta^2 delta_p, theta=1/2. Discarding it adds exact conditional binary KL whose local rate is at least ln(7/(4delta0))/4 for the negative-AND gate, diverging with dimension. This is a concrete history/reference correction, not a FEI counterfamily or a free flag code.

Section4 independently reconstructs A100-BINARY-REMAINDER-JENSEN-BOUND v1 at its entire stated scope, including complete normalizers, strict1/8 bits allowance, quadratic total loss and independent spectator cancellation. Verdict HOLDS, no repair supplied. The first unsupported universal line is payment of the complete retained row/gate/core bills and actual leaf entropy from one available signed child or influence reserve. Arbitrary non-flat data exposure is not silently included.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json, TREE_SPEC.json and EXPOSURE_SPEC.json were each saved before their job. Commands from the agent folder use `python -X utf8 runs/{run.name}/code/` followed by `check_quotient.py pilot`, `check_quotient.py full`, `check_tree.py pilot`, `check_tree.py full`, and `check_exposure.py full`.

Quotient full: 552 labeled gates/core pairs, all q on r=1,2,3 controls and d=4,6, 1608 control rows including irrelevant coordinates; plus51 negative-AND/spectator cases at d=2,4,6 with all16 labeled two-bit spectators. {main['assertions']} exact predicates in {main['elapsed_seconds']:.4f}s. Pilot20 cases/422 predicates in0.0354s. Independent actual truth tables, integer Walsh, physical flips, complete row/quotient normalizers, exact prime-log conditional losses and rational atanh signs; no A073/A100 author code executed.

Stopping full: 9352 labeled fixed-order prefixes, every order and every stopping depth through r=3, both core dimensions; {tree['assertions']} predicates in {tree['elapsed_seconds']:.4f}s. Pilot68 prefixes/205 predicates. Exact restricted Boolean gates and weighted full leaf influences check the control-only telescope; all-r/adaptive proof is analytic. Exposure:40 actual edited child/gate pairs at original d=6,8 plus62 compressed even-dimensional deleted-flag guards d=6..128; {exposure['assertions']} predicates in {exposure['elapsed_seconds']:.4f}s. Total final predicates {count}; pilots/replays not added. Each job stayed under frozen60s and <=100MB estimated memory; no >300MB memok trigger, dimension escalation, GPU or background helper.

## proof dependencies and changed downstream conclusions

CLAIMS.json preserves A100 v1's source statement/hypotheses/contributors/recorded hash and appends this independent acceptance; out/REVIEWED_ORIGINAL.json preserves the original. The arbitrary-gate debit is a separate elementary author theorem, not a repair to A100 and not a broad new universal candidate while earlier heat claims await review. Its flat-core, control-only and first-exposure hypotheses are explicit. Existing singleton price2+2/e^2 and signed block transfer are unchanged.

A067/A070/A096/A073 can now consume an arbitrary-gate, one-control-ledger lost-refund interface rather than allocate the same core fraction to each quotient. At the first core query they must retain the newly informative occupancy or debit its actual binary KL. A001/A099/A100/B20 may consume the source-bound Jensen review. No retained terminal gate is declared free, no universal constant improves, and no central adoption or mirror is asserted.

## one next mathematical action and independent reviewer

Preserve the complete inherited conditional reference through the next non-flat/shared-data split, explicitly record its informative flags, and pay both retained terminal price and conditional loss once from certified unused child slack. A070/A085 independently reconstruct arbitrary-gate Jensen and first-exposure flag; A094 may audit stopping ownership. This is the first unproved generalization of the survived interface, not another flat-core entropy census.

## actual persistence receipts or precise save blocker

Four protocol files, derivation, three frozen specs, code and exact outputs are saved in this run. Rolling STATUS has two current lines; WORKLOG/LEARNED are dated append updates. out/PERSISTENCE.json records reread hashes, exact-schema/JSON checks, protected-source review fields, progress/delta equality and file sizes below20MB. Local save is verified. Supervisor mirrors, canonical adoption and independent acceptance of the new narrow extension remain unverified. Only A066 files were written.

**Universal bridge:** This stage moves C018's conditional-reference debit and C019's stopping payment from one fixed two-bit gate to every Boolean control gate, paying discarded KL by (256/9)delta times one removed-control influence ledger. It also survives the first physical core query by retaining an explicit informative Fourier flag, while exactly certifying the unbounded extra loss if that flag is erased. The universal FEI improvement is zero: complete retained gate/core row prices and actual terminal entropy still need an available signed child reserve. NEXT transports that same reference and ownership through the next non-flat/shared-data split, the shortest continuation toward the universal bridge rather than another isolated class entropy result.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
stamp='2026-10-14T04:20:48Z stage'
(agent/'STATUS.md').write_text('STATE: A066 stage5 saved: arbitrary-gate lost KL <=(256/9)delta I_controls; control-prefix telescope and first-core informative-flag correction; A100 Jensen v1 HOLDS; 51158 exact predicates PASS; FEI OPEN.\nNEXT: A070/A085 review; preserve complete conditional reference/informative flags after next non-flat/shared-data split; pay retained terminal rows and lost KL from one certified unused child reserve.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+': Consumed A100/A073 positive-erasure quotient. Independently accepted A100 Jensen v1 without repair; extended to arbitrary Boolean gate q on bent core d>=4, lost KL <=(256/9)delta I_controls, hereditary control prefixes. First core query d>=6 requires retaining new dummy Fourier occupancy; deleting it adds unbounded local binary KL. Final27260+23449+449 exact predicates, no failures; pilots separately saved. Retained gate/core rows and terminal entropy unpaid; only own files written.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+': In F=b+1_zero(q-1), arbitrary q, all nonempty residual control cells share uniform bent-core laws. Only empty-control cell loses KL, exactly delta*qhat(i)^2*D0. Jensen gives sumL <=(256/9)delta^2 W1(q)<= (256/9)delta I_controls when bent d>=4, with one debit and control-only stopping heredity. Retained M_i^C includes delta*qhat(i)^2 ln(R_i/(delta*qhat(i)^2)) and remains unpaid. A first paired-core reveal creates a physical dummy whose Fourier occupancy is informative: keep it and pay <=(256/9)theta^2 delta_p I_controls; delete it and negative-AND extra local loss >=ln(7/(4delta0))/4 grows without bound. Flat-core proof is not arbitrary-data heredity. A100 Jensen v1 independently accepted; full FEI gap is actual retained terminal/child-slack ownership.\n')
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert len((agent/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in list(sorted(run.rglob('*')))+[agent/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]:
    if p.is_file() and p.name!='PERSISTENCE.json':
        data=p.read_bytes();assert len(data)<20*1024*1024
        if p.suffix=='.json':json.loads(data)
        receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump(run/'out/PERSISTENCE.json',{'verified_at_utc':datetime.now(timezone.utc).isoformat(),'local_saved':True,'mirror_verified':False,'checks':'Exact claim/progress keys, reviewed source protected fields unchanged, identical delta, all report fields/final bridge, JSON parse, two-line STATUS, file limits','files':receipts})
print(json.dumps({'saved':True,'new_claim':own['claim_id'],'independent_review':review['claim_id']+'@1 HOLDS','final_predicates':count,'receipted_files':len(receipts)}))
