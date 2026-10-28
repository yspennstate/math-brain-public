import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
CAMPAIGN=AGENT.parents[1]
RID=ROOT.name
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def writej(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
checks=json.loads((ROOT/'out/CHECKS.json').read_text(encoding='utf-8'))
audit=json.loads((ROOT/'out/ENTROPY_CHECKS.json').read_text(encoding='utf-8'))
assert checks['status']==audit['status']=='PASS'
assert (checks['cases'],checks['exact_assertions'])==(1024,103702)
assert (audit['cases'],audit['exact_formula_assertions'])==(192,384)

source_dir=CAMPAIGN/'agents/A044/runs/20261023T033305Z-account03-A044-non-symmetric-gate-classes'
source_claims=json.loads((source_dir/'CLAIMS.json').read_text(encoding='utf-8'))
source_claim=source_claims[0]
source_payload=json.dumps({'statement':source_claim['exact_statement'],'hypotheses':source_claim['hypotheses']},sort_keys=True,separators=(',',':'))
assert hashlib.sha256(source_payload.encode('utf-8')).hexdigest()==source_claim['statement_sha256']
assert sha(source_dir/'PROOF.md')==source_claim['proof_source']['sha256']
assert source_claim['statement_sha256']=='31700d6da9cd4b820a87ff0b8420023f970a09f56abdee380bd7ec219f41d2fc'
sources=[CAMPAIGN/'BOARD.md',CAMPAIGN/'claude/B09/STREAM_NOTES.md',source_dir/'PROOF.md',source_dir/'CLAIMS.json']
for rel in ['A041/runs/20261023T050523Z-account03-A041-weighted-threshold-fei/PROOF.md',
            'A041/runs/20261023T050523Z-account03-A041-weighted-threshold-fei/CLAIMS.json',
            'A043/runs/20261023T024327Z-account03-A043-prime-gate-decomposition/PROOF.md',
            'A045/runs/20261023T041958Z-account03-A045-biased-realizability-referee/PROOF.md',
            'A091/runs/20261023T053740Z-account03-A091-composition-referee/REPORT.md']:
    sources.append(CAMPAIGN/'agents'/rel)
writej(ROOT/'out/SOURCE_RECEIPTS.json',{'read_sources':[{'path':str(p),'sha256':sha(p)} for p in sources],
    'A044_statement_hash_reproduced':True,'A044_proof_hash_matches':True,
    'A044_hash_convention':'sha256 of sorted compact JSON {statement,hypotheses}; independently read source code/save_stage.py line43',
    'scope':'A044 complete flat identity and normalizer bound independently reconstructed; no blanket acceptance of all-depth source claim',
    'A042_stage8_review':'A044 CLAIMS.json independently reconstructs A042-SCALE-AWARE-DEFICIT-APPROXIMATION@1 at stated mathematical scope; no universal J payment accepted'})
writej(ROOT/'out/PACKAGING_CORRECTION.json',{'initial_finalizer':'FAILED at source statement-hash assertion, before protocol and rolling writes',
    'cause':'Reviewer assumed statement-only hash; source actually hashes compact sorted JSON of statement and hypotheses',
    'repair':'Read original A044 code/save_stage.py, reproduce exact documented source payload; no source or mathematical theorem changed',
    'verification':'Both exact source statement hash and raw PROOF.md hash checked by assertions'})

statement=(
 'Let g be any finite Boolean sign under an interior independent product law, mu=Eg, a=(1-mu)/2 in (0,1), V=4a(1-a), I=I(g), and let X be independent Bernoulli epsilon=2^-k, k>=1 integer. Put F=1 on X=0 and F=g on X=1. For occupied nonempty coefficients c_T choose j_T by 1/2<2^j_T|c_T|<=1, P_T=v_T*c_T^2, W_T=v_T*4^-j_T, Z_g=sum W_T, J_g=ln4 sum P_T*j_T, Delta_g=I-V. Write j_a for the cell of a, b=4^-j_a, B=V+4a^2*j_a. Then Delta_F=epsilon*Delta_g+epsilon*(1-epsilon)*V and J_F=epsilon*J_g+ln4[epsilon*(1-epsilon)*B+epsilon^2*k*V], with V<=B<=2V, zero composition carry, and sharp outer-gate bound J_outer<=3ln4*Delta_outer, equality at a=epsilon=1/2. Consequently a seed bound J_g<=KDelta_g is preserved under finite independent dyadic activations with constant max(K,3ln4). The corrected entropy obeys E_F=epsilon*E_g+epsilon*(1-epsilon)*V*ln4+2epsilon^2*V*ln(1/epsilon)+4epsilon*(1-epsilon)*a^2*ln(1/a^2), valid for any interior epsilon. For the complete flat dyadic references with actual empty mass, Z_F=epsilon*Z_g+4epsilon*(1-epsilon)*b, w=4a*epsilon*(1-a*epsilon), s=4epsilon*(1-epsilon)*a^2/w, t=4epsilon*(1-epsilon)*b/Z_F, and full ordinary KL_F=epsilon*KL_g+w*d_Bern(s||t). The full composed reference has t_outer obtained by replacing Z_g with V and retains epsilon*KL_g. With Z_outer=epsilon*V+4epsilon*(1-epsilon)*b, the positive normalizer transfer is 0<=w*ln(Z_F/Z_outer)<=epsilon*(Z_g-V); the exact signed flat/tree conversion also subtracts epsilon*V*ln(Z_g/V), replacing its KL together with the reference. Uniformly in the seed, |J_F/epsilon-J_g-ln4*B|<=ln4*epsilon*(k+2)*V. For a fixed nonconstant seed the full KL endpoint is KL_F/epsilon -> KL_g+4a*d_Bern(a||4b/(Z_g+4b)). Constants give actual constant or signed-literal zero-deficit/unit-atom laws; reflecting X covers the corresponding probability-one endpoint. These are natural-log identities and original-owner transfers; arbitrary seed J payment and full FEI remain open.'
)
gap='Pay the inherited arbitrary-seed dyadic scale charge from genuinely unused ORIGINAL degree-weighted capacity in the same complete reference; epsilon J_g is not negligible compared with epsilon I(g).'
claim={
 'claim_id':'A042-DYADIC-ACTIVATION-ENDPOINT-CERTIFICATE','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean sign on a finite independent product cube; deterministic coordinates contract first',
               'Physical normalized mixed coefficients and actual product variances; natural logarithms',
               'Independent selector; dyadic epsilon for scale/reference claims; entropy expansion alone valid at any interior epsilon',
               'Full ordinary references keep actual empty atom and all occupied nonempty labels; constants handled separately',
               'No independent Boolean reset, renewed seed reserve, second KL rebate or universal seed bound assumed'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A042/account03'], 'proof_source':{'path':'PROOF.md','sha256':sha(ROOT/'PROOF.md')},
 'proof_dependencies':['Direct physical Fourier expansion of F=1-X+Xg, independently checked by moments and Mobius transform',
                       'Complete finite-law ordinary KL chain rule, reconstructed by pointwise density factorization',
                       {'claim_id':source_claim['claim_id'],'version':1,'statement_sha256':source_claim['statement_sha256'],
                        'scope':'Only the optional downstream bound Z_g-V<=9Delta_g-6R_g; independently reconstructed in REVIEW_A044.md. Main endpoint theorem independent of this import.'}],
 'review_records':[], 'status':'AUTHOR_ANALYTIC_PROOF_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':gap,
 'next_consumers':['A044','A041','A045','A043','A091','B09 lead','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
writej(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':RID,'stream':'B09','packet_id':'A042',
 'gap_id':'B09-ORIGINAL-DYADIC-SCALE-PAYMENT','attempt_id':'A042-stage9-dyadic-activation',
 'method':'Arbitrary-seed exact physical endpoint expansion, zero-carry dyadic owner split, complete-reference KL factorization, independent prime-log audit',
 'mathematical_delta':'Sharp 3ln4 payment for every dyadic activation outer gate, all-depth conditional preservation of seed J bound, exact original-deficit split and inherited seed KL/scale endpoint; no universal J bound.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY',
 'mathematical_status':'ENDPOINT_CERTIFICATE_PROVED_AND_EXACTLY_CHECKED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':source_claim['claim_id'],'version':1,'statement_sha256':source_claim['statement_sha256'],'scope':'normalizer and complete-flat identity only, reviewed in REVIEW_A044.md'}],
 'claims_created_or_changed':['A042-DYADIC-ACTIVATION-ENDPOINT-CERTIFICATE@1'],
 'source_artifacts':['PROOF.md','REVIEW_A044.md','SPEC.json','ENTROPY_AUDIT_SPEC.json','out/CHECKS.json','out/ENTROPY_CHECKS.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A044/A045 independently review the exact activation reference split; then pay arbitrary seed J from unused original whole-set capacity, keeping the inherited KL and the signed normalizer transfer.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal arbitrary-seed scale payment remains open; normalizer/rounding control does not supply it','Independent review and supervisor mirror/downstream adoption not observed','Brain self-care degraded/unverified: stale owner-model and state-of-mind affect personal-context guidance'],
 'packet_ids':['A042']}
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
writej(ROOT/'PROGRESS.json',progress)
(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())

report=f'''# A042 stage9: arbitrary-seed dyadic activation endpoints

## exact target, quantifiers, hypotheses and units

For every finite Boolean seed g at any interior independent product law, determine the corrected entropy E=ln2 Hplus, I-Var, actual dyadic scale charge J and complete-reference ordinary KL after an independent rare selector activation F=1-X+Xg. Use epsilon=2^-k, k>=1, for exact dyadic cells; the entropy expansion itself holds at every interior epsilon. Contract deterministic inputs first, and handle constant seeds, zero deficit and unit conditional atoms explicitly. Reflecting X covers selected probabilities tending to one. All logarithms are natural. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD, B09 STREAM_NOTES v2 and own stage8 STATUS; execution protocol2026-10-11-execution-v2; A041 stage19 PROOF on adaptive references, A043 stage18 PROOF on prime56067 collar, A044 stage18 PROOF on complete dyadic reference/carry and its CLAIMS, A045 stage18 PROOF on signed reference transfer, and A091 stage19 REPORT on original-capacity stopping payments. Their exact source paths/hashes are in out/SOURCE_RECEIPTS.json. A044's statement and source-proof hashes were reproduced. The older campaign/literature intake remains prior-stage context, not a claimed fresh literature audit. Current owner deadline23Oct14:49UTC supersedes the initial protocol dates. The lead's original binary assignment is already closed; current board asks for actual scale payment with the SAME owner account.

## complete derivation or exact first unsupported line

PROOF.md gives direct mixed coefficients, exact Delta_F=epsilon Delta_g+epsilon(1-epsilon)V, and zero carry. Writing B=V+4a^2*j_a with a=(1-Eg)/2, one has V<=B<=2V and J_F=epsilon J_g+ln4[epsilon(1-epsilon)B+epsilon^2*kV]. The outer activation gate satisfies sharp J_o<=3ln4 Delta_o, equality at a=epsilon=1/2. A seed J/Delta bound therefore persists through arbitrary finite independent dyadic activations with constant max(K,3ln4). The explicit endpoint error is at most ln4 epsilon(k+2)V after division by epsilon. This pays the actual outer scale contribution, not just its rounding error.

The corrected-entropy expansion includes the exact 2epsilon^2 V ln(1/epsilon) term. Complete flat and tree laws preserve actual empty mass and all occupied labels. Their full ordinary KL splits exactly into epsilon KL_seed plus a Bernoulli sector divergence. The positive normalizer transfer is at most epsilon(Z_seed-V), charged to the inherited original seed allocation once; the exact signed flat/tree conversion also retains -epsilon n_seed. Constants produce constant/signed-literal zero-deficit laws. The zero selector mass contracts physically rather than normalizing an undefined conditional law. REVIEW_A044.md independently accepts only the flat identity and normalizer bound used in this transfer, not the entire larger all-depth source claim.

First unsupported line toward full FEI: {gap} No new unconditional bound on arbitrary J_seed is proved. Both the new exact KL limit and scale limit expose that remaining obligation explicitly.

## executed validation with domain, arithmetic, commands and outputs

Frozen SPEC and independent ENTROPY_AUDIT_SPEC preceded their jobs. Commands: python -B -X utf8 code/check.py --pilot; python -B -X utf8 code/check.py; python -B -X utf8 code/audit_entropy.py --pilot; python -B -X utf8 code/audit_entropy.py. The main pilot passed16 cases/948 assertions. Main exact moment implementation exhausts16 two-bit seeds at four product laws and k=1,2,4,10, plus256 three-bit seeds at fair law and k=1,4,10:1024 actual roots,38 constant and986 nonconstant fixtures,103702 exact Fraction assertions PASS in {checks['runtime_seconds']:.3f}s. It checks direct spectra, cells, J, Delta, sharp equality, normalizers and pointwise complete likelihood-ratio factorizations. This is not a floating KL comparison.

Independent integer Mobius polynomial transform and canonical prime-log dictionaries verify the corrected-entropy expansion and deficit exactly on192 roots, including nondyadic epsilon=1/3:384 formula assertions PASS in {audit['runtime_seconds']:.3f}s. Its16-case pilot passed32 assertions. These two data paths do not share spectral helper code. The arbitrary-dimension and continuum conclusions use the written proof rather than finite extrapolation. No formal proof, peak memory measurement or float sign certificate is claimed. Jobs were estimated80MB, stayed below55s and required no over300MB admission, GPU, compiler or detached work.

## proof dependencies and changed downstream conclusions

The new claim is an authored endpoint certificate pending independent review. Its main theorem is derived directly; A044-COMPLETE-DYADIC-REFERENCE-CARRY@1 is used only for the optional inherited normalizer bound, independently reconstructed at that scope. A044 independently accepted our stage8 scale-aware approximation at stated mathematical scope; this does not pay J universally. A041 adaptive selection and A045 signed conversion are context, not new assumptions of this theorem. No other source is repaired or refuted. Downstream, dyadic activation gates have a sharp paid scale constant and incur zero carry; the seed scale/KL obligation is carried exactly, so a rare wrapper cannot erase it or renew capacity already spent.

## one next mathematical action and independent reviewer

A044/A045 independently reconstruct equations(1),(7)-(10), then use this exact arbitrary-seed endpoint to test a proposed whole-set scale supplier from genuinely unused ORIGINAL capacity. A041/A091 should challenge any double use of epsilon(Z_seed-V) or dropped seed terminal KL. The next target is the universal inherited seed scale bill, not another isolated gate census.

## actual persistence receipts or precise save blocker

All four protocol files, proof, scoped review, frozen specs, scripts and exact outputs are saved in this designated A042 run. Finalizer checks exact schema key sets, source statement/proof hashes, PASS counts, identical compatibility-copy bytes and all artifacts under20MB, then writes local sha256 receipts. Initial packaging failed because I assumed a statement-only hash; reading A044's source finalizer showed its sorted compact statement-plus-hypotheses JSON convention. out/PACKAGING_CORRECTION.json preserves the correction; the source hash is now reproduced using its actual convention. Rolling STATUS has exactly two lines; WORKLOG and LEARNED are appended. Local persistence is the only claimed receipt: supervisor copy, remote mirror and downstream adoption remain unobserved. No shared-source mutation, git or messaging occurred. Brain self-care remains degraded/unverified: stale owner-model/state-of-mind notes affect personal-context guidance, and current research instructions and actual files govern instead. No research job is left running.

## Universal bridge

This stage advances C020 whole-set witness cost and C024 history transfer by paying the actual dyadic activation outer-gate scale bill at the sharp constant3ln4, proving zero carry and conditional all-depth preservation, and exposing the exact inherited seed scale/KL and signed normalizer conversion in one complete reference with the original deficit split. It does not prove the universal supplier: epsilon J_seed persists on the same scale as epsilon I_seed, and its original allocation cannot be renewed. The shortest next step is an original-capacity supplier for that arbitrary seed charge, tested against equations(1),(7)-(10), because the wrapper and conversion costs are now explicit and paid rather than being confused with the missing universal entropy bound.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A042 stage9 COMPLETE_LOCAL: sharp dyadic activation Jgate<=3ln4 Delta_gate; exact arbitrary-seed endpoint/KL;103702 main+384 independent formula assertions PASS; FEI OPEN.\nNEXT: A044/A045 review actual activation reference; pay inherited arbitrary-seed J from unused ORIGINAL capacity, retaining epsilon KL_seed and signed normalizer transfer.\n',encoding='utf-8')
tag='2026-10-23 stage9 20261023T055815Z'
for name,line in [
 ('WORKLOG.md',f'\n{tag}: Read current B09 and A091 developments. Derived and saved arbitrary-seed dyadic activation exact J/E/Delta, sharp3ln4 gate payment, zero carry, complete flat/tree KL and original-owner normalizer transfer. Main1024 roots/103702 assertions PASS; independent192 roots/384 symbolic entropy/deficit assertions PASS; pilots separate. Scoped A044 normalizer/flat identity HOLDS. No universal seed J payment, no formal compilation, no running research job; independent review/mirror unobserved.\n'),
 ('LEARNED.md',f'\n{tag}: For F=1-X+Xg with independent epsilon=2^-k, a=(1-Eg)/2,V=4a(1-a),B=V+4a^2*j_a in [V,2V], exact J_F=epsilon J_g+ln4[epsilon(1-epsilon)B+epsilon^2*kV], Delta_F=epsilon Delta_g+epsilon(1-epsilon)V. Outer J/Delta<=3ln4 sharp at a=epsilon=1/2; carries zero. Full ordinary flat KL_F=epsilon KL_g+w*d_Bern(s||t), with Z_F=epsilon Z_g+4epsilon(1-epsilon)4^-j_a, w=4a epsilon(1-a epsilon). Positive normalizer transfer <=epsilon(Z_g-V), and signed flat/tree conversion is that transfer minus epsilon*n_g. Retain seed terminals and original capacity: rare activation does not remove arbitrary-seed J.\n')]:
    path=AGENT/name
    old=path.read_text(encoding='utf-8') if path.exists() else ''
    if tag not in old: path.write_text(old+line,encoding='utf-8')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (ROOT/'PACKET_DELTA.json').read_bytes()==(ROOT/'PROGRESS.json').read_bytes()
assert report.rstrip().split('\n\n')[-1].startswith('This stage advances C020')
assert all(p.stat().st_size<20_000_000 for p in ROOT.rglob('*') if p.is_file())
files=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json']
writej(ROOT/'out/RECEIPTS.json',{'status':'PASS','created_at':datetime.now(timezone.utc).isoformat(),'schema_verified':True,'compatibility_copy_identical':True,'local_files':files,'rolling_files':[{'path':str(AGENT/x),'sha256':sha(AGENT/x)} for x in ['STATUS.md','WORKLOG.md','LEARNED.md']],'mirror_verification':'UNOBSERVED_SUPERVISOR_ACTION'})
print(json.dumps({'status':'PASS','files_hashed':len(files),'claim_id':claim['claim_id'],'main_assertions':checks['exact_assertions'],'independent_formula_assertions':audit['exact_formula_assertions'],'report':str(ROOT/'REPORT.md')}))
