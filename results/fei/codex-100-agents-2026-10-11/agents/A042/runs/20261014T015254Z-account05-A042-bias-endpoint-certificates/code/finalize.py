from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1];agent=root.parents[1]
team=agent.parents[1]
source=team/'agents/A043/runs/20261013T233947Z-account05-A043-prime-gate-decomposition'
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def save(name,x): (root/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sc=json.loads((source/'CLAIMS.json').read_text())[0]
assert sc['statement_sha256']=='020b97a3820a338acb78f02d9b22287302d18dfc754cb34eabc90fcc455b0e86'
review={'reviewer':'A042/account05','source_claim_id':sc['claim_id'],'version':1,'statement_sha256':sc['statement_sha256'],'decision':'HOLDS_AT_SCOPED_PORTIONS','accepted_scope':['universal signed singleton reserve','all-equal, exactly-one, mask25 continuum upper bounds and sharp paths','mask33152 prime status and exact companion obstruction'],'excluded_scope':['independent ternary catalogue review','mux dependency','majority bundle','whole read-once closure'],'independence':'own centered-moment implementation, physical signed derivatives, all ten prime row tests; written reconstruction in PROOF.md','repair_supplied':False,'evidence':['PROOF.md','code/check.py','out/CHECK_OUTPUT.json']}
save('out/SCOPED_REVIEW.json',review)
statement=('For every Boolean sign gate under any interior independent Bernoulli law, the exact unused singleton reserve is '
 '4D-2R-E_single=sum_i v_i[2(d_i-t_i)+2t_i(1-t_i)-t_i^2 ln(1/t_i^2)], '
 'where D=I-Var, R=sum_{|S|>=3}(|S|-2)P(S), d_i=E D_i^2, t_i=|E D_i|, and D_i is the half-difference derivative. '
 'Each displayed local contribution is nonnegative, and d_i-t_i=2min(P(D_i=1),P(D_i=-1)). '
 'For the four-input prime positive exactly at assignments 7,8,15 (mask33152), with first three input probabilities 1/2 and fourth probability z in [0,1], '
 'D=(5+14z-7z^2)/16 and E=4h((1-z)/4)+3h((1+z)/4)+(z(1-z)/2)ln64, h(t)=t^2ln(1/t^2). '
 'Its full natural corrected entropy margin satisfies (4+ln4)D-E >= (10-9ln2)/8 >47/100, with equality in the first inequality at z=0. '
 'At z=0, E=(7/4)ln2+[(5/2)ln2+1/8]z+O(z^2) and Hplus/D tends to 28/5. '
 'At s=1-z=0, E=(3/2)ln2+[3/4+(3/2)ln2]s+(1/2)s^2ln(1/s)+O(s^2), and Hplus/D tends to 2. '
 'The general four-bias prime inequality and all-dimensional FEI remain open.')
hyp=['finite Boolean sign table and normalized product Fourier basis','E=(ln2)Hplus, D spectral influence minus variance, v_i=4p_i(1-p_i)','universal reserve identity assumes interior input biases; h(0)=0 by continuity','selector-line theorem fixes the first three probabilities exactly at 1/2','deterministic selector endpoints interpreted by contraction or continuous formulas','endpoint big-O constants are for this fixed one-parameter family']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A042-RETAINED-SINGLETON-RESERVE-SELECTOR-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A042/account05'],'proof_source':{'run_id':root.name,'paths':['PROOF.md','out/CHECK_OUTPUT.json','code/check.py']},'proof_dependencies':['Parseval for product Fourier basis','actual mask33152 truth table','elementary logarithm inequality ln(x)<=x-1 and Taylor theorem'],'review_records':[],'status':'SOURCE_COMPLETE_NARROW_REPAIR_AND_EXACT_CHECKS_PENDING_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A043','A041','A045','A090','A091','B09']}
save('CLAIMS.json',[claim])
checks=json.loads((root/'out/CHECK_OUTPUT.json').read_text())
p={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A042','gap_id':'C025-G-BIASED-LTF-RETAINED-SINGLETON-SLACK','attempt_id':'A042-stage4-scoped-review-and-selector-repair','method':'independent analytic reconstruction and exact rational spectra; retained local slack identity; continuum selector margin','mathematical_delta':'Scoped independent HOLDS of A043 new three orbit bounds, signed reserve and prime obstruction. Exact universal nonnegative singleton-slack decomposition. Entire mask33152 fair-data selector line has sharp absolute natural margin >=(10-9ln2)/8>0.47, with symbolic endpoint expansions.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'RESTRICTED_RESULTS_PROVED; GENERAL_PRIME_PAYMENT_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':sc['claim_id'],'version':1,'statement_sha256':sc['statement_sha256'],'scope':'scoped portions explicitly reviewed in out/SCOPED_REVIEW.json'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':digest}],'source_artifacts':['PROOF.md','out/SCOPED_REVIEW.json','out/FROZEN_SPEC.json','code/check.py','out/CHECK_OUTPUT.json'],'next_consumers':['A043','A041','A045','A090','A091','B09','B20'],'next_action':'Use exact local singleton slack to test a cofactor-sensitive payment for mask33152 with unequal first-three biases; first isolate a rigorous collar around each zero-deficit face.','stagnant_substantive_attempts':0,'blockers':['No proven all-bias higher-degree payment by the retained local slack; full FEI open.'],'packet_ids':['A042']}
save('PROGRESS.json',p);(root/'PACKET_DELTA.json').write_bytes((root/'PROGRESS.json').read_bytes())
report=f'''# A042 stage 4: retained singleton slack and a prime selector certificate

## exact target, quantifiers, hypotheses and units

Review A043's new ternary mechanisms and obstruction; repair the endpoint analysis at that obstruction using the actual singleton slack. E is corrected entropy in natural units, Hplus=E/ln2, and D=I-Var uses spectral influence. The universal slack identity applies to every finite Boolean gate at interior product biases. The continuum certificate concerns precisely mask33152 at (1/2,1/2,1/2,z), 0<=z<=1. It is not an all-bias or all-arity theorem. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-14 01:51 UTC, B09 STREAM_NOTES.md v2 (2026-10-11 23:33), own STATUS.md and prior binary/majority checker interfaces, and EXECUTION_PROTOCOL.json in full (2026-10-11-execution-v2). Read A043 stage3 REPORT.md, CORE_PROOF.md and CLAIMS.json, claim {sc['claim_id']}@1, hash {sc['statement_sha256']}. Source portions used are the signed reserve, three new orbit arguments and explicit prime obstruction. No new paper theorem, brain result or floating-point search is a premise. A041/A044 latest board summaries informed dispatch but their proofs are not consumed here.

## complete derivation or exact first unsupported line

PROOF.md gives the complete reconstruction and new derivations. The exact unused singleton reserve is a sum of nonnegative local signed-cancellation and logarithm-slack terms. Independently reconstructed A043's all-equal, exactly-one and mask25 inequalities and sharp paths, and verified the prime obstruction. The review is scoped: no independent ternary census, mux dependency, majority bundle or whole formula-closure acceptance is claimed. No substantive repair to those accepted source portions was needed.

For the obstruction prime the complete fair-data selector continuum satisfies (4+ln4)D-E >= (10-9ln2)/8 >47/100; the lower margin is attained at the contracted AND3 endpoint z=0. At the other endpoint the vanishing normalized coefficients produce +(1/2)s^2 ln(1/s), explicitly separated from the selector variance. Endpoint ratios are 28/5 and 2. This pays the total entropy even where the previously proposed higher-degree companion is false.

First unsupported universal line: E_ge2-ln4 D-2R <= the actual retained singleton slack for arbitrary higher-arity primes. The exact identity relating those quantities merely rewrites the target and does not prove that line. For mask33152, allowing all four biases to vary is still unresolved.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json preceded execution. Command: `python -X utf8 code/check.py`. Final output: {checks['assertions_passed']:,} exact assertions; 375 ternary cases (125 in each of masks126,22,25), 64 selector cases including z=1/1024, and all ten proper block row tests. Each prime row count is three. Independent centered moments agree with mixed-difference formulas; physical signed derivatives verify Parseval reserve terms. Rational atanh-series log intervals use 24 terms after power-of-two range reduction, with positive tail <=2t^49/[49(1-t^2)]. Runtime {checks['runtime_seconds']:.3f} seconds. Estimated memory 60 MB, not measured; no job above the 300 MB trigger and no heavy search. The checker was rerun once after adding the explicit rational ln2<52/75 check needed for the stated decimal-free 47/100 margin. The analytic proof establishes continuum closure; the grid is not a continuum certificate.

## proof dependencies and changed downstream conclusions

Local results depend on the actual truth table, Parseval and elementary scalar inequalities, not an unreviewed broad claim. out/SCOPED_REVIEW.json pins A043's exact statement hash and separates accepted/excluded scopes. The source's false companion obstruction survives independent implementation. The new line certificate shows that obstruction does not signal any failure of the full corrected inequality along that entire selector segment. Retaining exact unused singleton slack is now available to A041/A043/A045; treating it as a separately reusable mass budget remains unjustified.

## one next mathematical action and independent reviewer

NEXT: carry the retained signed-cancellation and scalar slack through unequal data biases for mask33152, first treating zero-deficit-face collars with the existing exact endpoint expansion rather than a new unstructured grid. A043 should consume the scoped review and reconstruct the selector proof; A090/A091 should review the new identity and its endpoint logarithm coefficient. No independent reviewer is marked accepted for the new local claim.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, PROOF.md, frozen specification, scoped review, checker and output saved inside this run. Rolling STATUS.md has two lines; WORKLOG.md and LEARNED.md are appended. out/PERSISTENCE.json records local file sizes and hashes; out/VALIDATION.json checks schemas and statement hash. Supervisor copying, remote mirrors, registry adoption and independent review of this new claim are pending; no remote save is asserted. No save blocker exists.

**Universal bridge:** This stage advances the lead's C025/G-BIASED-LTF prime payment by independently reviewing three newly closed ternary orbits and replacing a failed higher-degree-only interpretation with an exact local singleton-slack identity. For the first obstructing quaternary prime it certifies the full selector-bias continuum with sharp absolute natural entropy margin (10-9ln2)/8, and resolves both selector endpoints including the logarithmic correction. Arbitrary data biases and a dimension-independent cofactor payment remain open. NEXT targets those same retained local terms at the first unresolved prime and its degenerate faces; this tests a reusable payment mechanism for the universal bridge rather than accumulating unrelated gate classes.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A042 stage 4 saved: scoped A043 ternary/reserve/obstruction HOLDS; exact singleton slack and full mask33152 selector-line margin >0.47; 8,062 exact checks; FEI OPEN.\nNEXT: A043/A090 review slack and selector endpoints; extend retained cofactor payment to unequal data biases, starting at zero-deficit faces.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
if 'stage4: independently reconstructed A043' not in (agent/'WORKLOG.md').read_text(encoding='utf-8'):
 with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} stage4: independently reconstructed A043 three new orbit proofs and prime obstruction. Derived exact retained singleton slack; proved entire fair-data mask33152 selector line with sharp margin (10-9ln2)/8 and both endpoint expansions. 8062 exact checks, no heavy computation. All-bias payment remains open.\n')
if 'Stage4: exact slack S=' not in (agent/'LEARNED.md').read_text(encoding='utf-8'):
 with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage4: exact slack S=4D-2R-E_single=sum_i v_i[2(d_i-|c_i|)+2|c_i|(1-|c_i|)-h(|c_i|)]. Here d_i=E Di^2 and d_i-|c_i|=2min(P(Di=1),P(Di=-1)). For prime mask33152 with first-three fair biases, D=(5+14z-7z^2)/16 and E=4h((1-z)/4)+3h((1+z)/4)+(z(1-z)/2)ln64. Full margin >=(10-9ln2)/8>0.47, sharp at z=0, despite false higher-degree companion. Endpoint ratios 28/5 and 2; z=1 expansion has +(1/2)(1-z)^2ln(1/(1-z)). General unequal-data payment remains unproved. A043 stage3 three new orbit bounds/signed reserve/prime obstruction independently HOLDS at scoped portions; census/mux/formula bundle excluded.\n')
inputs=[protocol,source/'REPORT.md',source/'CORE_PROOF.md',source/'CLAIMS.json',team/'BOARD.md',team/'claude/B09/STREAM_NOTES.md']
save('out/SOURCE_RECEIPTS.json',[{'path':str(x),'sha256':sha(x)} for x in inputs])
pr=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(pr['claim_fields'])
assert set(p)=={s.split(' (')[0] for s in pr['progress_fields']}
assert (root/'PACKET_DELTA.json').read_bytes()==(root/'PROGRESS.json').read_bytes()
assert len((agent/'STATUS.md').read_text().splitlines())==2
assert all('## '+h in report for h in pr['report_fields'])
assert checks['assertions_passed']==8062
save('out/VALIDATION.json',{'schemas':'PASS','statement_hash':digest,'compatibility_bytes':'PASS','rolling_status_lines':2,'assertions':checks['assertions_passed'],'full_fei':'OPEN'})
save('out/PERSISTENCE.json',[{'path':str(x.relative_to(root)),'bytes':x.stat().st_size,'sha256':sha(x)} for x in sorted(root.rglob('*')) if x.is_file() and x.name!='PERSISTENCE.json'])
print(json.dumps({'saved':str(root),'statement_sha256':digest,'assertions':checks['assertions_passed'],'schema_validation':'PASS'}))
