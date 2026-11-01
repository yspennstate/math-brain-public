from pathlib import Path
import json, hashlib

agent=Path(__file__).resolve().parents[3]
run=Path(__file__).resolve().parents[1]
root=agent.parents[1]
def write(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sources=[root/'BOARD.md',root/'claude/B14/STREAM_NOTES.md',
    root/'agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger/DERIVATION.md',
    root/'agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee/REPORT.md',
    agent/'STATUS.md',agent/'runs/20261014T042048Z-fleet05-A066-semigroup-dissipation/DERIVATION.md',
    Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
write('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources])
statement=('For every Boolean core b on d>=0 data coordinates, every Boolean gate q on disjoint control coordinates, '
 'and F=b+1_zero(q-b(0)), let any finite adaptive physical mixed stopping tree carry G_v=2^(-d_v) H_bits(q_v) '
 'and R_v=2^(-d_v)d_v Var(q_v), preserving q on live-point data children and using the actual marked-point '
 'constant sign on clean children. Let P_C=sum_control w_v Inf_i(F_v) and D_R=sum_data w_v 2^(-d_v)Var(q_v). '
 'Then sum_control w_v M_i(F_v)<=G_root-E G_leaf+R_root-E R_leaf-D_R+[2/(e ln2)]P_C, '
 'and sum_control w_v Delta H_bits(F_v)<=G_root-E G_leaf+R_root-E R_leaf-D_R+[(3+2/e)/ln2]P_C. '
 'Here M_i=sum_T p_(T+i) log2[(p_T+p_(T+i))/p_(T+i)] uses the complete normalized physical row reference. '
 'The heat version retains its exact signed constant-Fourier boundary: 2 sum_control w_v Delta K '
 '=ln2 sum_control w_v Delta H_bits-B_C. No root account is claimed automatically paid or available, '
 'and actual data entropy drops and complete physical terminal entropy remain explicit.')
cid='A066-MIXED-HISTORY-COMPLETE-CONTROL-ACCOUNT'
gap=('Admission of G_root and payment of actual data-node entropy/heat/reference debit plus full physical '
     'terminal debt from the named data release D_R and genuinely unused certified child/source surplus.')
claim={'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform Boolean cubes; physical restrictions and their actual reach weights',
 'Bits for G,R,H,M; K and its signed constant-Fourier boundary use nats',
 'Point attachment at the surviving marked point; no gate or reserve renewal at live descendants',
 'Complete reference including derivative-free atoms; zero terms interpreted continuously',
 'No admission of a root reserve without a separately certified unused source account'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A066/fleet05'],
 'proof_source':{'path':str(run/'DERIVATION.md'),'locator':'Sections 1-2, equations (1)-(6); scalar and heat preliminaries',
                 'checker':str(run/'code/check_accounts.py'),'output':str(run/'out/CHECK_FULL.json')},
 'proof_dependencies':[],'review_records':[],
 'status':'NARROW_HISTORY_INTERFACE_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A069','A070','A085','A096','B14','B20']}
write('CLAIMS.json',[claim])
full=json.loads((run/'out/CHECK_FULL.json').read_text(encoding='utf-8'))
pilot=json.loads((run/'out/CHECK_PILOT.json').read_text(encoding='utf-8'))
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B14','packet_id':'A066',
 'gap_id':'G-A066-HEAT-INTEGRAL','attempt_id':'A066-mixed-complete-control-account-06',
 'method':'Complete physical control-row price; carried gate entropy and variance reserve; exact mixed-history telescopes',
 'mathematical_delta':{'new_narrow_result':statement,'universal_FEI_bound_improvement':0,
 'mechanism_change':'From lost conditional KL on flat/control-only prefixes to complete control price on arbitrary cores and mixed adaptive histories',
 'availability_objection_consumed':'A096 nonflat rate-four actual-child-surplus obstruction prevents automatic root-capacity admission',
 'finite_validation':full,'remaining_gap':gap},
 'deliverable_status':'COMPLETE_SAVED_LOCALLY','mathematical_status':'CONTROL_HISTORY_INTERFACE_PROVED_BY_AUTHOR; FULL_FEI_OPEN; REVIEW_PENDING',
 'claim_versions_used':[], 'claims_created_or_changed':[{'claim_id':cid,'version':1}],
 'source_artifacts':[str(p) for p in sources]+[str(run/'DERIVATION.md'),str(run/'out/CHECK_FULL.json')],
 'next_consumers':claim['next_consumers'],
 'next_action':'Expose one actual nonflat data query with these same G,R and full inherited terminal functions; compare its debit with D_R and actual unused certified surplus without resetting either account.',
 'stagnant_substantive_attempts':0,'blockers':[gap,'Independent review of the narrow mixed-history lemma remains pending'],
 'packet_ids':['A066']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# A066 stage 6: complete control payment through mixed semigroup histories

## exact target, quantifiers, hypotheses and units

For every finite Boolean point attachment F=b+1_zero(q-b(0)), with arbitrary nonflat core and arbitrary gate, bound the complete control-query entropy price along any finite adaptive mixed stopping tree. G=delta H_bits(q) is a retained gate account and R=delta d Var(q) is one carried variance reserve. Influences are ordinary physical influences. Entropy and oriented row prices use bits; the heat area K and constant-Fourier boundary use nats. This is a narrow repair of the existing history-payment mechanism, not a new broad FEI candidate or a claim that its root accounts are free.

## sources actually read, revisions and theorem locators

Read the 2026-10-14 08:52 UTC BOARD snapshot, B14 STREAM_NOTES v2 (2026-10-11 23:25 UTC), own incoming STATUS, and the full execution protocol revision 2026-10-11-execution-v2. Consumed A096 stage5 DERIVATION (20261014T042803Z, nonflat actual-child-bank obstruction) and A088 stage5 REPORT (20261014T053751Z, conditional flags after core exposure). The board records A082's acceptance of the A096 obstruction; this stage does not claim a fresh independent review of it. Own stage5 complete-reference and informative-flag result supplies context, not an unproved dependency of the new ledger. Exact paths and read-time SHA256 receipts are in out/SOURCE_MANIFEST.json. Earlier baseline sources remain as recorded in prior runs; no new external literature or novelty claim is used.

## complete derivation or exact first unsupported line

DERIVATION.md reconstructs the complete quotient row on arbitrary cores, not only flat spectra. Its exceptional atom costs at most delta d beta_i^2+(2/(e ln2))Inf_i(F). Control queries decrease G by at least delta M_i(q) and decrease R by exactly delta d beta_i^2. Data queries decrease G by zero and release exactly delta Var(q) from R. Weighted telescoping gives the complete control bill bound, with data release D_R subtracted so it cannot be spent again. The entropy version adds the rigorously bounded row and channel terms; the heat version retains the exact signed boundary. Finite-cube heat integrability holds at zero and infinity, without a universal pointwise dissipation envelope.

The result applies to mixed adaptive queries and both nonconstant core children because its accounts follow actual restrictions. G_root remains potentially unpaid and R_root must be admitted from actual unused certified surplus. A096's example has R_root=d delta but rate-four actual-child surplus at most 5delta, forbidding automatic admission for d>5. FIRST UNSUPPORTED LINE: {gap} No payment of the whole entropy or full FEI is inferred from the control-only left side.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json was frozen before the search. Every labeled core truth table on d=1,2 and gate truth table on r=1,2 was used, with no root symmetry reduction. All fixed coordinate permutations and all prefix stopping depths were checked; arbitrary adaptivity is proved analytically by nodewise identities and weighted telescoping, not claimed to be exhaustively enumerated. The pilot checked {pilot['root_pairs']} root pairs and {pilot['stopping_prefixes']} prefixes in {pilot['elapsed_seconds']:.6f} seconds. The full run checked {full['root_pairs']} root pairs, {full['orders']} orders, {full['stopping_prefixes']} prefixes, {full['cached_physical_states']} cached physical states and {full['assertions']} predicates in {full['elapsed_seconds']:.6f} seconds.

Commands, from the A066 folder: `python -X utf8 runs\\{run.name}\\code\\check_accounts.py pilot` and the same command with `full`. Both exited zero. Integer Walsh transforms, Fraction influences/means, exact prime-log identities and rational logarithm enclosures certify the checks. The finite scalar guard uses the proved 2/e<3/4; the analytic theorem keeps the sharper 2/e. Full entropy splits into control drops, data drops and actual leaf entropy exactly; the signed heat boundary and unspent data reserve are checked explicitly. Estimated memory was 100 MB; no job over 300 MB or heavy job was started. Outputs are CHECK_PILOT.json and CHECK_FULL.json.

## proof dependencies and changed downstream conclusions

The claimed inequality is self-contained in DERIVATION.md: Parseval, KL data processing, physical entropy restriction and scalar log inequalities are reconstructed there. The A096 availability obstruction is source-bound context for the next obligation, not a premise of the new inequality. No old claim is superseded or refuted. Downstream consumers may replace the earlier flat/control-prefix lost-KL payment by this complete control-price ledger, provided G and R are carried once and actual data/terminal debts remain. Root influence capacity is not certified unused child surplus. Quantitative improvement to the universal FEI constant is zero.

## one next mathematical action and independent reviewer

Expose one actual nonflat DATA query with the same G,R and full inherited terminal functions, and test whether its actual entropy/reference debit fits D_R plus an already certified unused source surplus. A070 or A085 should independently reconstruct the complete reference and history telescope; A096 can inspect the bank-availability guard. These are requested handoffs in the artifacts, not messages sent to other agents. Independent acceptance is pending.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, DERIVATION.md, SPEC.json, code and out are saved in this run. STATUS.md is current and WORKLOG.md/LEARNED.md are appended. out/PERSISTENCE_RECEIPTS.json records byte sizes and SHA256 for all other run files and the rolling files. The saver validates exact protocol field sets and compatibility-copy equality. Local durability is established; supervisor copying, mirror verification and downstream mathematical use are not asserted. No save blocker.

**Universal bridge:** This stage moves C019 stopping-tree payment and C024 history transfer by paying the complete control bill from actual decreases of one gate account and one variance reserve through arbitrary-core mixed histories, with the data release withheld explicitly. It removes flat-core and control-only restrictions from that payment interface; it does not improve a universal FEI bound. What remains is admission of the gate/root reserve and payment of actual data and terminal debt from genuinely available sources. NEXT examines exactly the next unpaid physical data split under the same accounts, so it tests the universal ownership bridge rather than collecting another isolated class bound.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A066 stage6 saved: arbitrary-core complete control bill paid by carried G,R through mixed histories; 101715 exact predicates PASS; independent review pending; FEI OPEN.\nNEXT: Expose one nonflat DATA query with same G,R and full terminal functions; pay actual debit from D_R and certified unused child/source surplus, with no bank renewal.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as fp:
    fp.write('\n2026-10-14T09:00:57Z stage6: Read updated board/B14/incoming status and A096/A088 new objections. Changed from lost-KL-only to complete control price for any core. Derived G,R telescopes through mixed physical histories, withholding data releases. Frozen pilot/full checks passed: 400 roots, 6944 orders, 26944 prefixes, 101715 exact predicates. Root G admission and actual data/terminal payment remain open. Source-bound A096 bank obstruction retained; no fresh acceptance claimed. Saved narrow lemma v1 and all protocol files.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as fp:
    fp.write('\n2026-10-14 stage6: For any core b and F=b+1_zero(q-b(0)), complete control price M_i(F)<=delta M_i(q)+delta d beta_i^2+(2/(e ln2))Inf_i(F). Carry G=delta H_bits(q), R=delta d Var(q): control drops G>=delta M_i(q), R=delta d beta_i^2; data drops G=0, R=delta Var(q). Thus mixed-history control bill<=Gdrop+Rdrop-D_R+kappa P_C, complete control entropy adds 3/ln2 P_C. Actual leaf/data entropy and signed heat boundary must remain. G is unpaid gate account; R is not automatically available source surplus. A096 shows rate-four actual surplus may be <R for nonflat point cores. This ledger changes ownership mechanism without settling the universal data/terminal payment.\n')
protocol=json.loads(sources[-1].read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
expected=set(protocol['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert all(s in report for s in protocol['report_fields'])
assert len((agent/'STATUS.md').read_text().splitlines())==2
files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json')
files += [agent/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
write('out/PERSISTENCE_RECEIPTS.json',{'run_id':run.name,'protocol_field_validation':'PASS',
 'compatibility_copy':'BYTE_IDENTICAL','mirror_status':'NOT_CHECKED',
 'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files]})
print(json.dumps({'saved':run.name,'protocol':'PASS','checks':full['assertions'],'receipt_files':len(files)}))
