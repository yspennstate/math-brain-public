from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=json.loads((R/'out/EXACT_CHECKS.json').read_text(encoding='utf-8'))
bank=json.loads((R/'out/BANK_CHECKS.json').read_text(encoding='utf-8'))
assert checks['helper']=='A041-unbounded-jump-v1' and checks['assertions']==3059
assert [checks[k] for k in ('full_count_cases','top_formula_cases','direct_cases','admission_proper_cases','admission_endpoint_cases')]==[6,12,10,276,8]
assert bank['status']=='PASS' and bank['cases']==768 and bank['assertions']==3840
shared=Path('~/brain_workers/FEI100_20261011')
review=shared/'agents/A045/runs/20261022T232557Z-fleet03-A045-biased-realizability-referee'
sources=[shared/'BOARD.md',shared/'claude/B09/STREAM_NOTES.md',review/'REPORT.md',review/'PROOF.md',review/'REVIEW_A041.md',review/'CLAIMS.json',shared/'context/threshold_paper_38pp.txt',A/'runs/20261021T190738Z-fleet03-A041-weighted-threshold-fei/CLAIMS.json',A/'runs/20261014T083216Z-fleet05-A041-weighted-threshold-fei/code/check_stage.py',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
receipts=[]
for p in sources:
 b=p.read_bytes()
 try:t=b.decode('utf-8');enc='utf-8'
 except UnicodeDecodeError:t=b.decode('cp1252');enc='cp1252 source fallback'
 receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'decoding':enc})
dump(R/'out/SOURCE_RECEIPTS.json',receipts)
dump(R/'out/A045_REVIEW.json',{'source_claim':'A045-RATIONAL-MEAN-CONDITIONING-ADMISSION-OBSTRUCTION@1','statement_sha256':'f1b8daa6656f1a9aab06f61363d05dcdc5fd3beda9b808b29348a41c90bad341','verdict':'HOLDS_WITH_STATED_SCOPE','reconstruction':'PROOF.md section 4: nonsquare denominator, rational mean invariant; reduced-fraction square tests in EXACT_CHECKS.json','repair_supplied':False,'scope':'finite rational product biases; empty label preserved; proper nonempty subset; irrational biases excluded','received_review':{'claim':'A041-SHARP-QUADRATIC-COHERENCE-CHARGE@1','statement_sha256':'c958945c4cc6ab13b72c1d24659df0a678cd4ec0ae40067aaa88ef81b62df150','source':str(review/'REVIEW_A041.md'),'scope':'new Cauchy, sharp two-jump, overlap and D log 2 clauses; reviewer previously authored reference dependency, so not a wholly independent full-chain review'}})
statement=('For every Boolean sign on two nonempty physical blocks under an interior product law, with beta_i the maximum opposite-block-averaged pivotal probability, D_mix >= (1/2) sum_i (1-beta_i) I_i. For the actual threshold F_m=2*1{N_A+N_B>=m+1}-1 with equal block sizes m, at every interior labelled product bias the complete top-label canonical two-direction quadratic-reference ratio equals V_m^2/sum_d w_md^2 >= sqrt(m)/4, where V_m=binom(2m-1,m-1), w_md=binom(m-1,d)binom(m,m-1-d). Thus no universal pointwise multiplier exists. For this same family at fair inputs only, the averaged positive log coherence Gamma<=8D/e<3D and full mixed cross entropy C*<(36 log(2)+8/e)D<28D.')
claim={'claim_id':'A041-UNBOUNDED-POINTWISE-COHERENCE-AVERAGED-PAYMENT','version':1,'exact_statement':statement,'hypotheses':['actual Boolean sign and normalized biased Fourier basis','canonical complete two-direction count-tail reference from prior A041 source','all bias coordinates interior for pointwise obstruction and pivotal-cap bank','fair inputs ONLY for Gamma and C* payment; natural logarithms'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A041'],'proof_source':{'path':'PROOF.md','sha256':sha(R/'PROOF.md'),'exact_checks':'out/EXACT_CHECKS.json','bank_checks':'out/BANK_CHECKS.json'},'proof_dependencies':['A041-TWO-DIRECTION-COMPLETE-QUADRATIC-REFERENCE@1','A041-SHARP-QUADRATIC-COHERENCE-CHARGE@1','threshold_paper_38pp.txt Theorem A: uniform threshold H_bits<9 I'],'review_records':[],'status':'SOURCE_COMPLETE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['arity-independent pointwise P<=c K* for the canonical two-direction quadratic reference on all actual two-weight thresholds'],'first_unproved_line':None,'next_consumers':['A045','B09 lead','B20']}
dump(R/'CLAIMS.json',[claim])
report='''# exact target, quantifiers, hypotheses and units

Close a replacement reference estimate surviving the recovered weighted-threshold controls. New scoped theorem: a general physical pivotal-cap bank; unbounded pointwise reference coherence on actual two-weight threshold representations; an arity-independent averaged payment on the fair balanced stress family. Natural logarithms throughout. Arbitrary real-weight biased FEI+ and full uniform FEI remain OPEN.

# sources actually read, revisions and theorem locators

Read the current BOARD B09/B20 updates, B09 STREAM_NOTES v2, own previous status and source-complete run, and execution protocol revision 2026-10-11-execution-v2. Consume A045's 20261022T232557Z REPORT/PROOF/CLAIMS and REVIEW_A041: exact source claims and scope are pinned in out/A045_REVIEW.json. The new A045 rational-admission theorem is independently reconstructed in PROOF section 4; its reviewer receipt for our prior result is restricted to the new clauses and is not advertised as full-chain independence. Theorem A of threshold_paper_38pp supplies the known uniform threshold H_bits<9I baseline used only for the fair averaged payment. Source byte hashes and encoding receipts are in out/SOURCE_RECEIPTS.json. Earlier source history and original conditional-input counterfamilies remain as recorded in the prior run; none is replaced.

# complete derivation or exact first unsupported line

See PROOF.md for the full elementary derivation. For every Boolean sign, D >= (1/2) sum_i(1-beta_i) I_i, with beta_i the actual opposite-block pivotal-probability cap. For strict majority on 2m bits partitioned m+m, the full-label P/K* is reciprocal hypergeometric collision probability and at least sqrt(m)/4 at every interior product bias. The three-jump example m=3 has ratio 50/23>2; the earlier sharp TWO-jump factor two remains intact. No constant pointwise multiplier can survive. At FAIR inputs the same family has D>=I/4>=sqrt(m)/4, Gamma<=8D/e<3D and complete C*<28D. This uses the known uniform threshold entropy theorem and is a payment test for the reference, not a new uniform FEI class result.

The first unpaid general line is C* - M KL(R||Q) <= K D for arbitrary actual weighted thresholds and product biases, together with extending the complete reference beyond two weight groups. Arbitrary biased pivotal caps can approach one. The proof retains the complete reference including off-support labels, terminal spectral entropy and a single D bank. Conditional-input TC is not spectral TC or good-coordinate erasure. The recovered pivotal-credit refutation remains a coefficient-one refutation.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede both jobs in out/FROZEN_SPEC.json and out/FROZEN_BANK_SPEC.json. Run python -X utf8 code/check_stage.py from this run (or its full path): exact rational count spectra at m=1,2,3,4,8,16; compressed top formulas at twelve specified m through 1024; ten labelled truth-table/product checks; 276 proper A045 retained counts plus eight endpoints. Natural-log intervals use a proved atanh remainder. This passed 3059 assertions in 23.547 seconds, with a 120 MB memory estimate. No adaptive dimension growth or heavy search. The separate check_bank.py exhausts all 256 three-variable Boolean signs at three fixed product laws, including constants and nonmonotone functions, partition 1+2. Its exact Fraction results are in out/BANK_CHECKS.json. The general conclusions come from the analytic proofs, not finite extrapolation. No full Lean verification is claimed.

# proof dependencies and changed downstream conclusions

Retain the previous complete quadratic-reference identity and Cauchy theorem as declared dependencies. A045's new rational-admission result is reviewed, not needed to prove the new coherence theorem. It prevents silently treating normalized retained spectra as Boolean laws at rational biases; such laws remain valid non-Boolean references. Replace any proposed universal pointwise multiplier by an averaged likelihood/KL calculation. The fair 28D payment survives unbounded top-label coherence but does not establish biased FEI+.

# one next mathematical action and independent reviewer

Next: bound the actual averaged profile likelihood together with KL cancellation using the coordinate-dependent pivotal reserve in (1), first on arbitrary biased two-weight thresholds including the recovered OR-heavy/AND-light controls. Do not seek another worst-case pointwise multiplier. A045 is the requested independent reviewer of the new clauses; the B09 lead must account for the existing two-candidate review cap before promoting another broad candidate. No peer message was sent.

# actual persistence receipts or precise save blocker

All four protocol artifacts, full proof, scripts, frozen specs, exact outputs and source/review receipts are saved locally in this run. out/ARTIFACT_MANIFEST.json records byte counts and SHA256 after finalization; code/save_stage.py checks exact field sets, claim statement hash and byte-identical compatibility progress. The rolling STATUS, WORKLOG and LEARNED are updated. Remote supervisor copying and independent review are pending; no git, shared-index or brain write was performed. Brain self-care is degraded: stale owner-model and state-of-mind sources leave personal-context guidance unverified; the mathematical claims rely on the cited current files and exact derivations.

**Universal bridge:** This stage advances B09's actual-gate reference payment toward C020 whole-set witness cost: it proves a universal physical derivative-reserve bank, rules out an arity-independent pointwise quadratic-reference multiplier by an actual threshold family, and pays that family's complete fair averaged cost by less than 28 times the existing mixed excess-degree bank. It leaves arbitrary-bias and arbitrary-real-weight averaged likelihood/entropy payment unpaid. Combining actual pivotal reserve with the already exact signed KL identity is the shortest next route because pointwise domination is now impossible and normalized selected spectra cannot be admitted as Boolean gates without proof.
'''
report=report.replace('Its exact Fraction results are in out/BANK_CHECKS.json.',f"It passed {bank['assertions']} assertions on {bank['cases']} cases in {bank['runtime_seconds']:.3f} seconds; exact Fraction results are in out/BANK_CHECKS.json.")
write(R/'REPORT.md',report)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B09','packet_id':'A041','gap_id':'G-BIASED-LTF-MIXED-SIGNED-CROSS-ENTROPY','attempt_id':'unbounded-jump-averaged-bank-v1','method':'exact actual-gate spectrum certificates and analytic hypergeometric collision / physical derivative reserve','mathematical_delta':'Universal physical pivotal-cap bank; no constant pointwise quadratic reference multiplier; fair balanced complete averaged cost <28D; independent source-bound A045 admission review.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_THEOREM_SOURCE_COMPLETE; GENERAL_TARGET_OPEN','claim_versions_used':claim['proof_dependencies']+['A045-RATIONAL-MEAN-CONDITIONING-ADMISSION-OBSTRUCTION@1 reviewed only'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['PROOF.md','out/EXACT_CHECKS.json','out/BANK_CHECKS.json','out/SOURCE_RECEIPTS.json','out/A045_REVIEW.json'],'next_consumers':['A045','B09 lead','B20'],'next_action':'Pay averaged profile likelihood minus the existing KL cancellation from actual pivotal reserve at arbitrary biases; retain recovered heavy/light controls.','stagnant_substantive_attempts':0,'blockers':['general arity-independent arbitrary-bias signed cross-entropy payment unproved','independent review and supervisor remote copy pending'],'packet_ids':['A041']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
write(A/'STATUS.md','STATE: Source-complete: universal pivotal-cap bank, unbounded actual-threshold pointwise coherence, fair averaged C*<28D; independent review pending; full FEI OPEN.\nNEXT: Pay arbitrary-bias averaged profile likelihood with the same pivotal reserve and KL cancellation; preserve coefficient-one credit and TC/erasure scopes.\n')
for name,text in [('WORKLOG.md',f'\n{now} Stage {R.name}: proved unbounded pointwise ratio >=sqrt(m)/4 on actual threshold controls; proved general physical pivotal-cap bank and fair complete averaged cost <28D. Exact stage: 3059 assertions; bank: {bank["assertions"]} assertions/{bank["cases"]} cases. Reviewed A045 rational-admission claim at pinned hash; no repair. General weighted/bias payment remains open; switch from pointwise to averaged mechanism.\n'),('LEARNED.md','\n'+now+' Durable: D_mix >= (1/2) sum_i(1-beta_i)I_i for arbitrary Boolean signs, beta_i opposite-block pivotal cap. Strict-majority m+m full-label quadratic-reference ratio is reciprocal hypergeometric collision, >=sqrt(m)/4 at every interior bias. No universal pointwise multiplier. Fair-only averaged Gamma<3D and complete C*<28D use beta<=1/2 and known uniform threshold FEI. This neither extends the old two-jump bound nor changes coefficient-one pivotal-credit refutation scope. Rational normalized retained AND spectra with empty retained cannot be Boolean spectra at rational product biases for proper retention.\n')]:
 with (A/name).open('a',encoding='utf-8',newline='') as f:f.write(text)
protocol=json.loads(sources[-1].read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(progress)==set('packet_ids' if s.startswith('packet_ids ') else s for s in protocol['progress_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
manifest=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='ARTIFACT_MANIFEST.json']
assert all(x['bytes']<20_000_000 for x in manifest)
dump(R/'out/ARTIFACT_MANIFEST.json',{'status':'PASS','files':manifest,'bank_cases':bank['cases'],'schema_checks':'exact protocol key sets; claim hash; compatibility byte equality; file sizes'})
print(json.dumps({'status':'PASS','files':len(manifest),'claim':claim['claim_id'],'bank':bank}))
