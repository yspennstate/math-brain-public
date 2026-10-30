from pathlib import Path
import json,hashlib,datetime,copy
R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parent.parent
P=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8'));fields=protocol['required_per_run']
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(name,obj):
    (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def statement_sha(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
checks={key:read(R/f'out/{key}.json') for key in ['MAIN','SCALAR','CALIBRATION']}
assert all(v['status']=='PASS' for v in checks.values())
assert checks['MAIN']['helper_sha256']==sha(R/'code/check.py')
assert checks['SCALAR']['helper_sha256']==sha(R/'code/scalar.py')
assert checks['CALIBRATION']['helper_sha256']==sha(R/'code/calibration.py')
total=sum(x['assertions'] for x in checks.values());assert total==659213
formal=read(R/'out/LEAN_RECEIPT.json') if (R/'out/LEAN_RECEIPT.json').exists() else {'status':'PENDING_NOT_CLAIMED'}
peer_paths={
 'A094':ROOT/'agents/A094/runs/20261026T232939Z-fleet04-A094-proof-chain-challenger',
 'A050':ROOT/'agents/A050/runs/20261027T005654Z-fleet04-A050-repair-with-scope',
 'A096':ROOT/'agents/A096/runs/20261023T140303Z-fleet03-A096-live-gap-ledger',
 'A097':ROOT/'agents/A097/runs/20261023T143952Z-fleet03-A097-cross-route-transfer'}
peer_claims={k:read(v/'CLAIMS.json') for k,v in peer_paths.items()}
gap=copy.deepcopy(next(c for c in peer_claims['A094'] if 'A011' in c['claim_id']))
assert statement_sha(gap['exact_statement'])==gap['statement_sha256']
gap.setdefault('review_records',[]).append({'reviewer':'A011','verdict':'HOLDS_UNCHANGED_SCOPED_OBJECTION','scope':'Exact original named statement; physical contraction telescope and allowed b>=12 witness, not a refutation of v5 numerical reserve. No repair to this objection supplied.','source':str(R/'DERIVATION.md')+' sections1--3','evidence':str(R/'out/WITNESSES.json')})
gap['status']='INDEPENDENTLY_RECONSTRUCTED_LOCALLY_A011; ORIGINAL_REVIEW_RECORDS_RETAINED; FULL_FEI_OPEN'
dep050=next(c for c in peer_claims['A050'] if c['claim_id']=='A050-VACUUM-CALIBRATED-HEREDITARY-REFERENCE')
dep096=next(c for c in peer_claims['A096'] if c['claim_id']=='A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT')
old=read(A/'runs/20261023T134844Z-fleet03-A011-representation-existence/CLAIMS.json')[0]
statement='For every nonconstant uniform Boolean g on a>=1 bits with supplied complete covering subprobability reference c=CE(Pg,R)<=C0 I(g), C0>=0, fixed b>=12, and any finite sequence of actual point edits with arbitrary nonempty fresh control blocks, retain the v5 ACTUAL ROOT floors6rho/8rho/later4(1+4j(j+1))rho and true control kernels. Let R_M be that root reference, D_j=a+b+sum r_i, rho_j=2^-D_j, S=sum(1+j(j+1))rho_j D_j. For EVERY finite adaptive physical query policy with no repeated coordinate along a branch, prescribe inherited complete descendant models, optionally followed after EVERY query by calibration of their NORMALIZED vacuum shape while preserving scalar mass. All such calibration charges are nonpositive. The actual complete signed transaction bill Braw=CE_root+sum reached actual reset charges=H(F_M)+Qloss+E D_full_terminal is <=135c/92+320S. At the SAME original K=4C0+15 and full old0<=U<=(C0+37/8)I(g), K I(F_M)-Braw-U >=[(35751/23552)C0+18111/4096]I(g)+K sum G_j>0, G_j=2rho_j(D_j-d_previous_actual). Every old scalar mass and all full terminals remain. For mass1 the calibration is A050 actual-vacuum compatibility; at mass<1 it is only normalized-shape compatibility with the full mass penalty retained. The root reference admits A096 moving occupied/ghost witness representation with at most2^N original labels plus one reusable empty slot; no O(I) witness price is inferred. V5 numerical terminal-functional scope is retained separately, but its identification with root CE plus actual resets is WITHDRAWN: for locally rebuilt v5 floors Braw=Lterminal+Qloss, and all-policy payment remains unproved. No original source is renewed; full FEI remains OPEN.'
deps=[{'claim_id':old['claim_id'],'version':5,'statement_sha256':old['statement_sha256'],'scope':'ROOT envelope only, rederived in current proof; no adoption of erroneous transaction identification.'}]
for dep in [gap,dep050,dep096]:
    deps.append({'claim_id':dep['claim_id'],'version':dep['version'],'statement_sha256':dep['statement_sha256'],'scope':'Scoped correction or compatible inherited-interface specialization; current proof derives the portion used.'})
claim=dict(claim_id='A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK',version=6,exact_statement=statement,
 hypotheses=['Finite uniform Boolean cubes, base2 CE/KL, finite covering subprobability source0<s<=1, nonconstant source and supplied c<=C0 I(g).','Fixed b>=12; arbitrary finite actual signs/points; globally nonempty fresh control blocks.','Actual root references as in v5; descendants inherited without new local floors, with optional mandatory normalized-vacuum calibration and scalar mass retained.','Every finite adaptive physical policy with no repeated coordinate on a branch; full physical reaches, complete terminals and all old U retained.','This reference class is NOT claimed to meet fixed nonempty floors, fixed alpha or essential-mask requirements.'],
 statement_sha256=statement_sha(statement),contributors=['A011','A094 (accounting correction)','A086 (accounting objection)','A050 (vacuum-calibrated interface)','A096 (ghost-complete hereditary interface)'],
 proof_source=[str(R/'DERIVATION.md'),str(R/'code/check.py'),str(R/'code/calibration.py'),str(R/'code/scalar.py')],proof_dependencies=deps,review_records=[],status='AUTHOR_PROOF_EXACT_FINITE_CHECKS; INDEPENDENT_V6_REVIEW_PENDING; CONDITIONAL_INITIAL_SOURCE; FULL_FEI_OPEN',
 supersedes=[{'claim_id':old['claim_id'],'version':5,'scope':'Withdraws its full-transaction interpretation and replaces descendant policy by inherited/vacuum-calibrated models. Numerical v5 terminal bound retained at that scope only.'}],refutes=[],
 first_unproved_line='No independent acceptance of version6 yet. For prescribed v5 LOCAL floors, accumulated Qloss is not paid by their terminal-functional inequality alone. For full FEI the original arbitrary-core O(I) source or required compatible admission remains unpaid.',next_consumers=['B03 lead','A085','A090','A094','A086','A050','A096','A099','A100','B20'])
for c in [claim,gap]:assert set(c)==set(fields['claim_fields'])
write('CLAIMS.json',[claim,gap])
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B03',packet_id='A011',gap_id='C020-ORIGINAL-SOURCE-C024-QUERY-KL-ACCOUNT',attempt_id='A011-stage22-repair-v5-query-ledger',method='Consume A094/A100 objection; finite divergence conservation; inherited-reference repair; consume A050/A096 compatible calibration; exact Boolean/rational verification.',mathematical_delta='A094 unchanged objection accepted. V5 full-transaction reading withdrawn. V6 ALL physical policies pay actual root+resets at SAME K/full old U for inherited or vacuum-calibrated references, residual[(35751/23552)C0+18111/4096]Ig+KsumG. Fixed-local-floor Qloss and original source remain unpaid.',deliverable_status='COMPLETE_LOCAL_ARTIFACTS_REVIEW_PENDING',mathematical_status='CONDITIONAL_AUTHOR_PROOF;659213_EXACT_ASSERTIONS_PASS;FULL_FEI_OPEN',claim_versions_used=deps,claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':6},{'claim_id':gap['claim_id'],'version':gap['version'],'change':'Local unchanged-statement independent A011 reconstruction'}],source_artifacts=['DERIVATION.md','out/SOURCE_RECEIPTS.json','out/DEPENDENCY_RECEIPTS.json','out/MAIN.json','out/SCALAR.json','out/CALIBRATION.json','out/WITNESSES.json','out/LEAN_RECEIPT.json'],next_consumers=claim['next_consumers'],next_action='A085/A090 independently audit v6 and exact mass<1 calibration scope. In the hereditary moving-witness interface, price one ORIGINAL arbitrary-core source from unused original influence; if fixed nonempty floors are required, charge their actual conversion plus Qloss rather than inheriting v5 equation6.',stagnant_substantive_attempts=0,blockers=['Original arbitrary-core O(I) source remains unpaid.','All-policy transaction price for the locally rebuilt v5 floors remains open.','Independent v6 reconstruction and supervisor publication unverified.','Checklist working update failed: checklist lock held too long.'],packet_ids=['A011'])
assert set(progress)==set(x.split(' (')[0] for x in fields['progress_fields'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
write('out/DEPENDENCY_DISPOSITIONS.json',{'old_claim_id':old['claim_id'],'version':5,'statement_sha256':old['statement_sha256'],'withdrawn':'Identification in DERIVATION equation6 of Hroot+E Dterminal with raw root CE plus actual signed resets; missing accumulated nonnegative Qloss.','retained':'Numerical terminal-functional bound and root-envelope scope not refuted.','substitute_version':6,'local_floor_transaction_status':'UNPAID_QLOSS_GAP','independent_review_consumed':gap['claim_id'],'universal_FEI':'OPEN'})
receipt=[]
for agent,d in peer_paths.items():
    for name in ['CLAIMS.json','REPORT.md']:
        p=d/name;raw=p.read_bytes();raw.decode('utf-8-sig');receipt.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'use':'Detailed exact claim read; context report accessed; no blanket adoption.'})
write('out/DEPENDENCY_RECEIPTS.json',receipt)
write('out/VALIDATION_SUMMARY.json',{'status':'PASS_FINITE_CHECKS','total_main_assertions':total,'jobs':checks,'pilot_not_added':read(R/'out/PILOT.json'),'scalar_first_attempt':'INCOMPLETE_RUNTIME; replaced same frozen domain by incremental exact helper','formal':formal,'rung':'Author proof with exact finite checks; full theorem NOT Lean-certified; independent review pending.'})
formal_status=formal.get('status', 'See raw helper receipt; no blanket Lean claim.')
report=f'''# A011 stage22: correct the query ledger and pay inherited compatible policies

## exact target, quantifiers, hypotheses and units

The v5 full-transaction reading is withdrawn. Its equation(6) omits accumulated physical-query KL contraction Qloss. A094's unchanged objection is independently reconstructed. Full FEI remains OPEN. Version6 instead pays the actual complete transaction bill for EVERY finite adaptive physical policy with inherited descendants, including mandatory normalized-vacuum calibration, at SAME original K=4C0+15 and FULL old U<=(C0+37/8)Ig. Source: any nonconstant Boolean g with supplied complete c<=C0Ig; fixed b>=12; arbitrary finite actual point edits with nonempty fresh controls. Bits throughout. New bound Braw<=135c/92+320S and residual>= [(35751/23552)C0+18111/4096]Ig+KsumG>0. At subprobability mass<1 calibration constrains normalized shape only and retains the entire scalar mass penalty.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2, current BOARD and B03 STREAM_NOTES v2, own STATUS/rolling files and stage21 DERIVATION/CLAIMS were read. Canonical README/current status/claim-obstruction-packet registries/stream actions/campaign plan, supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING/sources and all FOUR context paper texts were intake-accessed with selected passages inspected; no new full-paper audit is claimed. Detailed mathematics: A09420261026T232939Z DERIVATION1--2 and exact objection; A10020261027T023227Z REPORT unchanged independent confirmation; A08620261023T140222Z accounting objection; A09620261023T140303Z ghost-complete exact claim and A05020261027T005654Z vacuum-calibrated exact claim. A097 exact signed-floor claim was inspected for what the inherited interface does not preserve. Source hashes, bytes and decoding in out/SOURCE_RECEIPTS and DEPENDENCY_RECEIPTS. Brain wake warned of stale owner-context sources; brain recalls produced no adopted replacement premise. Current instructions and source mathematics govern.

## complete derivation or exact first unsupported line

DERIVATION1--3 proves the exact finite identity Braw=Hroot+E Dterminal+Qloss, including both complete children, ghost reference fibers, masses and actual normalizers. A dictator with b>=12 and one allowed fresh-control edit has Zclean*Zedit<1, so the omitted term is strictly positive. This does not refute the old numerical reserve. DERIVATION4--5 constructs v6: inherit the final paid ROOT model down any physical tree, with no new local floors; optional normalized-vacuum calibration costs exactly minus Bernoulli KL. Therefore total actual reset charges are nonpositive and even a bank that declines negative refunds can pay root CE. The root envelope and geometric/influence sums are rederived without v5 equation6. Actual full transaction residual is the displayed rational bound. Moving ghost labels are inherited and at most one reusable empty label is needed for calibration, consuming A050/A096 rather than another optional edit history. No dimension-independent witness-count claim follows.

First unpaid line for locally rebuilt v5 floors: bound the accumulated Qloss from the SAME unused original account. First universal line: supply an original arbitrary-core O(I) complete reference in a useful hereditary interface, or pay a required stricter admission including its actual query losses. Neither line is declared closed.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede pilot/main/scalar and calibration jobs. python -B -X utf8 code/check.py pilot passed4494 assertions on22 sources/66 trees in0.092s. Main passed267528 assertions on ALL278 labelled Boolean sources n0..3,2412 first queries,1668 complete trees/23796 nodes in12.686s. Three references P,P/2,(P+U)/6 exercise scalar masses, signed resets and source-zero ghost fibers. code/calibration.py passed261186 assertions on834 complete trees/11898 nodes,11064 calibrations and876 observed positive ghost slots in17.952s. Every original label is reconstructed after physical erasure and calibration, including the one reusable empty slot. code/scalar.py passed130499 assertions on43344 exact scalar tuples and21 actual in-family b12..32 normalizer witnesses in0.633s. Total main assertions659213; overlapping fixtures are counted per execution, pilot excluded. The first scalar helper exceeded its55s cap and is recorded INCOMPLETE; unchanged domain was completed with an incremental exact partial sum after the frozen amendment. No failed runtime is evidence for or against a mathematical claim.

Arithmetic: integer Walsh transforms, Fraction spectra/masses/normalizers/witness coefficients, exact rational per-atom ratio checks and geometric identities; independent24-term atanh log intervals with proved tail and outward96-bit grid. Interval overlap only diagnoses identities, whose equality is proved by exact finite algebra. Strict witness signs use rational factorizations. Main domain is not every n3 policy; the universal tree quantifier is analytic. Estimated60--120MB/checker, no dimension escalation, one checker at a time. Lean admission was explicitly checked before the possible >300MB compiler. Formal result is preserved in out/LEAN_RECEIPT.json (current wrapper status: {formal_status}); no complete theorem or entropy translation is claimed Lean-certified. The requested formal statement covers node ledger algebra only.

## proof dependencies and changed downstream conclusions

Version6 is a repair of the SAME candidate. V5 root/numerical terminal scope is separated from its erroneous transaction identification. Its all-local-floor transaction interpretation must remain CONDITIONAL until Qloss is paid. New inherited-reference theorem and normalized-vacuum specialization are author proofs awaiting independent reconstruction. A094 objection is adopted unchanged, with A011 review recorded locally; A094/A086 receive contribution credit for the correction and A050/A096 for the compatible interface. No contributor is manufactured into an independent reviewer of v6. No shared index, another agent's file, old immutable run, git state or brain store was changed. out/DEPENDENCY_DISPOSITIONS.json gives source-bound downstream correction for A099/A100/B20.

## one next mathematical action and independent reviewer

A085/A090 independently reconstruct version6, especially full scalar mass at constant leaves and the root envelope. Then price ONE original arbitrary-core complete source in the hereditary moving-witness/vacuum interface from UNUSED original influence. If a downstream argument requires fixed nonempty floors instead, specify them and pay actual signed admission plus accumulated Qloss; equation6 cannot supply a free conversion. This targets the universal admission/source line, not another history census.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA with packet_ids[A011], proof, frozen specs, helpers and exact outputs are saved only in A011. Protocol key sets, statement hashes, output-helper hashes and local file receipts are checked by code/finalize.py. Rolling STATUS has two lines, WORKLOG and LEARNED record the correction. Supervisor mirror/downstream adoption are unverified. Checklist working update failed with checklist lock held too long; closure receipt is saved separately when attempted. No mail, git, trading path, detached job, remote compute, GPU or deletion used. Other workers were untouched; finite checkers completed or hit their own declared cap. Brain owner-model/state-of-mind/dream freshness warnings are recorded as context health, not mathematical evidence.

Universal bridge: C024 history transfer and C019 stopping-tree payment advance by repairing the full transaction ledger and paying ALL physical policies for inherited/vacuum-calibrated descendants at unchanged original K and old U, with explicit residual[(35751/23552)C0+18111/4096]Ig+KsumG. C020 original whole-set source existence remains unpaid. The old locally rebuilt floor theorem has a precise extra Qloss obligation. NEXT prices an original arbitrary-core source in the now concrete hereditary interface, or a truly required stricter conversion, so it attacks the all-dimensional FEI bottleneck rather than extending another isolated class. Full FEI remains OPEN.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
tag='2026-10-27 A011 stage22'
lesson='V5 equation6 omitted Qloss: raw root CE+signed resets=Hroot+E Dterminal+sum reached query KL. A094/A100 objection holds; old numerical terminal inequality is not refuted. Inherited root references, optionally normalized-vacuum calibrated with scalar mass retained, give nonpositive reset charges and actual Braw<=135c/92+320S; SAME K/full U residual[(35751/23552)C0+18111/4096]Ig+KsumG. All-local-floor Qloss and ORIGINAL arbitrary-core source remain unpaid. Exact659213 assertions PASS; first scalar runtime incomplete and optimized same-domain retry PASS; independent v6 review pending.'
for name,head in [('WORKLOG.md',''),('LEARNED.md','')]:
    p=A/name;t=p.read_text(encoding='utf-8') if p.exists() else ''
    if tag not in t:p.write_text(t+'\n\n## '+tag+'\n'+lesson+'\n',encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A011 stage22 COMPLETE_LOCAL: A094 query-KL objection HOLDS; v5 transaction reading withdrawn; v6 inherited/vacuum-calibrated ALL-policy SAME-owner bill paid;659213 exact assertions PASS; review pending; FEI OPEN.\nNEXT: A085/A090 audit v6 mass-retaining calibration/root payment; supply ORIGINAL arbitrary-core O(I) source in hereditary moving-witness interface, or pay required local floors INCLUDING accumulated query KL.\n',encoding='utf-8')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/PERSISTENCE_RECEIPT.json',{'status':'LOCAL_SCHEMA_HASH_SIZE_CHECKS_PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol':protocol['revision'],'claims':len([claim,gap]),'assertions':total,'files':receipts,'external_mirror':'UNVERIFIED','full_FEI':'OPEN'})
print(json.dumps({'status':'COMPLETE_LOCAL','assertions':total,'claim6_sha256':claim['statement_sha256'],'files':len(receipts),'formal_status':formal_status,'report':str(R/'REPORT.md')}))
