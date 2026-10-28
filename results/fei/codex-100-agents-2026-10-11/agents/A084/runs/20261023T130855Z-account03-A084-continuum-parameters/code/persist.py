"""Persist exact protocol fields, source-bound review and local save receipts."""
from pathlib import Path
import hashlib,json,copy
R=Path(__file__).resolve().parents[1];BASE=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def claims(doc):return doc['claims'] if isinstance(doc,dict) else doc
def statement_hash(c):return hashlib.sha256(json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json');protocol=read(protocol_path)
root=read(R/'out/CRITICAL_POINT.json');audit=read(R/'out/SCALAR_AUDIT.json');physical=read(R/'out/PHYSICAL.json')
assert all(z['status']=='PASS' for z in [root,audit,physical])
assert root['certified_rational_upper']=='39/8' and physical['core_tables']==257
total=root['assertions']+audit['assertions']+physical['recorded_assertions'];assert total==25154
source_root=BASE.parent/'A080/runs/20261023T112507Z-account03-A080-universal-counterexample-standard'
source=next(c for c in claims(read(source_root/'CLAIMS.json')) if c['claim_id']=='A080-PIVOTAL-TRANSPORT-FRESH-GUARD-HULL')
source_ref={k:source[k] for k in ['claim_id','version','statement_sha256']}
assert source_ref['statement_sha256']=='5cb347b67915c35284ac65b35e547bc38f4bf7bf1c52a09bd4a872c1b0c2ff5f'
review=dict(source_ref,reviewer='A084',verdict='HOLDS_FRESH_COORDINATE_SUBSTATEMENT_UNCHANGED',
 scope='PROOF sections6-7: whole fresh-AND correction formula, the source variance-bound derivative proof and source K>=8 full-hull contraction/owner mechanism. These are independently reconstructed in the present proof; the source general pivotal theorem, point-family raw-correction obstruction and separate financial application are NOT independently accepted here.',
 method='Direct complete Fourier coefficient factorization, derivative check, distinct physical influence p, finite envelope induction and literal full-spectrum/edge controls.',
 evidence=['PROOF.md sections1-5','out/PHYSICAL.json','out/SCALAR_AUDIT.json'],source_repaired=False)
put(R/'out/REVIEW_A080.json',review)
old_path=BASE/'runs/20261023T105943Z-account03-A084-continuum-parameters/CLAIMS.json'
old=copy.deepcopy(claims(read(old_path))[0])
accept_path=BASE.parent/'A075/runs/20261023T112446Z-account03-A075-search-to-theorem-bridge/CLAIMS.json'
accepted=next(c for c in claims(read(accept_path)) if c['claim_id']==old['claim_id'])
assert old['exact_statement']==accepted['exact_statement'] and old['hypotheses']==accepted['hypotheses']
assert statement_hash(old)==old['statement_sha256']==accepted['statement_sha256']
old['review_records'].append({'reviewer':'A075','independent_reviewer':True,'verdict':'HOLDS','scope':'Whole existing exact_statement and hypotheses, unchanged and without repair','source':str(accept_path),'source_sha256':sha(accept_path),'source_statement_sha256':old['statement_sha256']})
old['status']='ONE_INDEPENDENT_EXTERNAL_REVIEW_HOLDS_RECORDED'
old['proof_source']=[str((old_path.parent/Path(p)).resolve()) if not Path(p).is_absolute() else p for p in old['proof_source']]
assert all(Path(p).exists() for p in old['proof_source'])
put(R/'out/ACCEPTED_PRIOR_REVIEW.json',{'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256'],'reviewer':'A075','verdict':'HOLDS_UNCHANGED','old_immutable_run_modified':False,'source_review_sha256':sha(accept_path)})
statement=(
 'Let c(p)=2*h2(p)-h2((1-2*p)^2)/2 for real p in[0,1]. There is exactly one '
 'p_star in(0,1/2) solving p*c_prime(p)-c(p)=0, and '
 'lambda_star=c(p_star)/p_star is the LEAST constant with c(p)<=lambda_star*p '
 'for every real p in[0,1], equivalently for every bias realizable by finite '
 'uniform Boolean cores. It satisfies487/100<lambda_star<39/8, with the '
 'exact192-bit root and price enclosures in out/CRITICAL_POINT.json. '
 'For every finite uniform Boolean g, a distinct independent balanced '
 'physical bit y, and EACH FIXED real K>=lambda_star, the full stopping '
 'deficit hull satisfies R_K(AND_minus(g,y))=R_K(g)/2. In particular every '
 'real K>=39/8 suffices, improving the source sufficient K>=8. For every '
 'integer m>=0 fresh balanced AND guards, R_K(F_m)=2^(-m)*R_K(g), including '
 'all adaptive physical reveal/stopping histories. The complete correction is '
 'paid by the ORIGINAL distinct guard influence owners: each guard in the '
 'final F_m has influence2^(-(m-1))*Pr(g=-1), and total correction is at most '
 'lambda_star*m*2^(-(m-1))*Pr(g=-1). All real supplied surpluses above this '
 'coherent hull bank are covered by affine credit shifts with old owner/debit '
 'labels and full outcomes retained. The scalar bound is sharp; no optimality '
 'of lambda_star as a full-hull-contraction threshold is asserted. Initial '
 'influence pricing of an arbitrary R_K(g), general active-core composition '
 'and full FEI remain open.'
 )
hypotheses=[
 'All physical cubes are uniform and finite, outputs +/-1, entropy in bits, ordinary total physical influence; h2 and eta use continuous zero conventions.',
 'AND_minus(g,y)=(1+g+y-g*y)/2; fresh guards are independent balanced original coordinates, all distinct from the arbitrary seed core.',
 'The rate K is FIXED throughout a history. All fresh influence owners are initially unused; core hull credit and any old booked obligations are already supplied.',
 'No changes to the original decomposition or retroactive insertion into an already paid tree are assumed; both full query outcomes and all stopped siblings are retained.',
 'Supplied initial credit is at least the stated full hull bank; every EXTRA real surplus D>=0 is allowed, without asserting that mere current solvency funds every future history.',
 'lambda_star is an optimal universal scalar correction price, not a proved optimal threshold for the actual deficit-hull identity and not a universal FEI constant.'
]
new={
 'claim_id':'A084-SHARP-FRESH-OWNER-CONTINUUM','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':'',
 'contributors':['A084'],
 'proof_source':['PROOF.md','code/critical.py','code/scalar_audit.py','code/physical.py','out/CRITICAL_POINT.json','out/SCALAR_AUDIT.json','out/PHYSICAL.json','out/COUNTERCONTROLS.json'],
 'proof_dependencies':[dict(source_ref,acceptance='FRESH_COORDINATE_SUBSTATEMENT_INDEPENDENTLY_RECONSTRUCTED',scope=review['scope'])],
 'review_records':[],'status':'AUTHOR_ANALYTIC_PROOF_EXACT_CERTIFICATES_EXTERNAL_REVIEW_PENDING',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'None within the scalar optimum and supplied-bank fresh-guard theorem. Initial influence payment for arbitrary inner hull and general active-core correction allocation remain open.',
 'next_consumers':['A080','A071','A072','A075','A089','A074','A092','B17','B20']
}
new['statement_sha256']=statement_hash(new)
put(R/'CLAIMS.json',[new,old])
next_action=('A080/A074/A092 independently reconstruct the single-critical-point price and whole-function hull induction. A071/A072/A089 must allocate the TWO-arbitrary-active-core/general-gate correction to genuinely unused ORIGINAL influence owners; this sharp fresh-owner boundary and all old labels/full terminals must remain valid. Arbitrary initial inner pricing is still unpaid.')
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B17','packet_id':'A084',
 'gap_id':'A084-INHERITED-PHYSICAL-CORE-PAYMENT','attempt_id':'stage9-sharp-fresh-owner-continuum',
 'method':'Exact full entropy correction; derivative/unique-root analytic reduction of ALL real biases; strict192-bit root certificate with independent rational48-term audit; distinct original physical-influence payment and full-DAG hull induction.',
 'mathematical_delta':'Sharp scalar fresh-owner price lambda_star in(4.8723210717795,4.8723210717892); K>=39/8 replaces source K>=8 for arbitrary-core exact all-policy fresh-guard hull contraction. All real biases[0,1] and rate/surplus boundaries covered analytically. A075 external HOLDS of prior all-K guard obstruction recorded unchanged.',
 'deliverable_status':'COMPLETE_LOCAL',
 'mathematical_status':'SCOPED_DISTINCT_OWNER_PRICE_PROOF_CERTIFIED_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':[source_ref,{k:old[k] for k in ['claim_id','version','statement_sha256']}],
 'claims_created_or_changed':[{k:c[k] for k in ['claim_id','version','statement_sha256']} for c in [new,old]],
 'source_artifacts':['PROOF.md','REPORT.md','FROZEN_SPEC.json','out/SOURCE_PINS.json','out/CRITICAL_POINT.json','out/SCALAR_AUDIT.json','out/PHYSICAL.json','out/COUNTERCONTROLS.json','out/REVIEW_A080.json','out/ACCEPTED_PRIOR_REVIEW.json','out/MANIFEST.json'],
 'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['General-gate/two-active-core distinct original-owner allocation and arbitrary inner-hull initial influence payment remain unproved.','New sharp-price theorem external review and supervisor mirror remain unverified.','Compute telemetry unchanged at13:57:59 across >30s; no fresh heavy-job assurance was inferred. Brain personal-model/state/dream context remains stale and unused as evidence.'],
 'packet_ids':['A084']
}
required=protocol['required_per_run']
assert all(set(c)==set(required['claim_fields']) for c in [new,old])
assert set(progress)=={x.split(' (')[0] for x in required['progress_fields']}
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
put(R/'out/COMPUTE_NOTE.json',{'governor_log_read':True,'state_ts_first':'2026-10-23 13:57:59','state_ts_second':'2026-10-23 13:57:59','read_separation_over_30_seconds':True,'fresh_telemetry_claimed':False,'other_work_stopped_or_restarted':False,'own_job_estimated_max_MB':100,'heavy_job_started':False})
put(R/'out/INTAKE_NOTE.json',{'source':str(source_root/'CLAIMS.json'),'initial_read_only_error':'TypeError: string indices must be integers; source has a run_id/stream/claims wrapper, not a top-level array','resolution':'Read the claims member; preserve source bytes and exact claim digest. No mathematical check or proof failed.'})
report=f'''# A084: the sharp fresh-coordinate price covers all real biases

## exact target, quantifiers, hypotheses and units

For EVERY uniform Boolean core g, with p=Pr(g=-1), retain the complete F=AND_minus(g,y) and a distinct independent balanced physical bit y. Its exact outer entropy correction is c(p)=H(F)-H(g)/2. Certify its sharp scalar price over ALL REAL p in[0,1], including0,1/2,1, then pay it from the ORIGINAL fresh-coordinate influence p. Entropy is in bits. The sharp scalar price lambda_star lies strictly between4.8723210717795 and4.8723210717892, so the rational K=39/8=4.875 suffices. For EVERY fixed real K>=lambda_star, R_K(F)=R_K(g)/2; all m fresh guards contract exactly by2^-m under all adaptive histories. No universal FEI constant is asserted and arbitrary initial inner hull pricing remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD, B17 STREAM_NOTES v2, own STATUS/previous-stage proof and arithmetic; A071113913 REPORT (failed proposed positive correction), A072120900 PROOF (signed drift<=6 times physical influence but initial bank unpaid), A080112507 REPORT and PROOF sections6-7 (fresh-coordinate K>=8), A075112446 REPORT/CLAIMS (full independent HOLDS of A084's previous guard obstruction), execution protocol {protocol['revision']}, and read-only governor log/state. Earlier campaign/paper intake is retained background; no new literature claim is assumed. out/SOURCE_PINS.json pins source bytes. The old AND sign-map target was already closed; current protocol dispatch consumes the new distinct-owner payment rather than repeat the fixed four-core fixture or the accepted obstruction.

Brain wake completed, but self-care is degraded: owner-model99.6h, state84.2h and dream34.9h stale at intake. Their personal-context reliability remains affected; none is mathematical evidence. Compute state remained timestamp13:57:59 across reads separated by more than30s, and was not treated as current memory availability. No governor or other running work was stopped/restarted. Own jobs stayed small. A read-only intake initially assumed an array in A080 CLAIMS; its actual run wrapper was then decoded correctly (INTAKE_NOTE); no mathematics changed.

## complete derivation or exact first unsupported line

PROOF.md derives every coefficient of the complete fresh-AND composition, retaining EMPTY and y-only masses, and the exact H/I identities. Its negative-third-derivative proof shows the second derivative crosses0 exactly once. The ratio derivative numerator N=p*c_prime-c then has exactly one interior zero, so strict signs at two rational root endpoints cover the entire real bias interval. Symmetry handles p>1/2; direct formulas handle0,1/2,1. The exact critical point/price enclosure is in CRITICAL_POINT; the two endpoints are1009093403773/4398046511104 and504546701887/2199023255552. An independent exact Fraction logarithm implementation confirms the decisive signs and rational bound487/100<lambda_star<39/8.

The source's rate8 came from c<=2Var(g)<=8p. Direct maximization of c/p replaces that bound with lambda_star<39/8 for the SAME complete function and the SAME original fresh influence owner. This explains the changed constant. The full-hull proof uses W=R_K(g)/2 before y is revealed and R_K(g) or0 on the two full y-fixed outcomes. It majorizes the deficit by the pointwise fresh-owner payment, and is superharmonic under every physical query; y-first supplies the matching lower bound. All real surplus credits above this supplied bank shift affinely, with old labels and full terminals retained. Each guard's contribution is scaled to its influence in the FINAL original full function, so repeated guards do not recharge old core influence.

The scalar price is sharp by dyadic density and literal Boolean realizability. This does NOT identify the smallest possible full-hull-contraction rate; a scalar-payment failure need not be an actual hull deficit. First unpaid universal line: allocate general-gate or two-active-core correction from distinct STILL-unused original influence owners, and price arbitrary initial inner hulls. Raising K or assuming the entropy-containing initial bank is influence-paid would not establish that line.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded computation. From this run: python -B -X utf8 code/critical.py --pilot; physical.py --pilot; critical.py; scalar_audit.py; physical.py; persist.py. Root pilot:8 steps/10 predicates,0.00608s. Physical pilot:all16 two-bit cores,960 recorded assertions,0.07382s. Main root:40 fixed bisections/60 predicates,0.87623s. Both certified root signs and a unique-maximum proof, not a rate/bias grid, support the all-real result.

Independent scalar audit:48-term EXACT Fraction atanh series with explicit remainder,23 predicates in0.31739s; root signs and bounds agree with the separate fixed-grid192-bit80-term producer. Two altered-sign/underpriced controls reject. Physical main:all256 three-bit cores plus one fixed5-bit core negative on0..6,543 complete core/full/restriction functions checked,25071 recorded assertions in0.80732s. Integer FWHT vs direct characters, inverses, Parseval, full physical edges, all fresh/core query outcomes, exact prime-log correction equality and hull equality are checked. A nonzero supplied entropy envelope audits coherence beyond zero deficit cases. The fixed p=7/32 control rejects scalar price487/100; a rate1 point-defect control rejects unconditional hull contraction BELOW the theorem hypothesis. Neither is called an FEI counterfamily or an optimal-contraction threshold counterexample.

Total NONPILOT recorded assertion calls:{total}; these are not counts of distinct Boolean functions. All job estimates<=100MB, pilots/jobs<55s; no expected>300MB job, memory-gated heavy job, dimension escalation, GPU, remote compute, detached worker or process shedding. No floating sign decides any claim; decimal root displays are auxiliary. No Lean verification was attempted or claimed.

## proof dependencies and changed downstream conclusions

Source A080-PIVOTAL-TRANSPORT-FRESH-GUARD-HULL@1, hash {source_ref['statement_sha256']}, independently HOLDS at the fresh-coordinate substatement of sections6-7, unchanged and without repair; other source claims are outside this review (REVIEW_A080). New claim {new['claim_id']}@1, hash {new['statement_sha256']}, has a complete author proof and exact certificates; external review is pending. It sharpens an existing scoped payment theorem, not another proposed universal candidate.

A075 independently accepts the WHOLE prior A084-RATE-CONTINUUM-LOCAL-ADMISSION-OBSTRUCTION@1 unchanged, hash {old['statement_sha256']}. This run checks its exact statement/hypotheses/digest match and records that external review in CLAIMS/ACCEPTED_PRIOR_REVIEW; the old immutable run and its mathematics are not modified. A072's signed C+6I envelope remains conditional on initial supply. For this fresh-owner boundary the new theorem pays the correction directly, without importing its additional full-influence bank. General initial pricing remains unpaid.

## one next mathematical action and independent reviewer

{next_action} The review should attack the constant/empty masses, the derivative signs and all endpoint faces, actual fresh influence pricing, distinct guard-owner scaling, and whether the sharp scalar constant has been wrongly called a sharp full-hull rate.

## actual persistence receipts or precise save blocker

All research files are saved only in the specified A084 run; four protocol files have exact required fields and byte-identical progress/delta. out/MANIFEST.json pins hashes/sizes, canonical statement digests and schema checks; FINAL_PERSISTENCE_CHECK gives the closing verification. STATUS has two lines; WORKLOG and LEARNED append this stage. No peer research folder, shared index, brain store or repository was written; no git/mail/message/deletion/trading action occurred. Required wake used the supplied session helper. Supervisor mirroring, public release and independent review of the NEW theorem remain unverified. No certificate command or own worker remains running at closure.

## Universal bridge

C019 stopping-tree payment advances by a sharp SCALAR initial correction price on the ENTIRE compact real bias region[0,1]: lambda_star<39/8 replaces the source rate8 for exact all-policy fresh-guard contraction of an ARBITRARY Boolean core. Arbitrary guard counts use the sum of DISTINCT original physical-influence owners, retaining scaled old core bills and both full outcomes. This moves a genuine source-funded boundary rather than a finite grid or another fixed fixture, but does not pay arbitrary initial inner hulls or general two-active-core correction. NEXT uses this sharp fresh-owner limit to test the general original-owner allocation while preserving old labels and full terminals; that is the remaining noncircular supplier route toward full FEI.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
assert all('## '+x in report for x in required['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
(BASE/'STATUS.md').write_text('STATE: Stage9 saved: sharp scalar fresh-owner price4.87232107178; exact all-guard hull contraction for real K>=39/8 (was8), all real biases;25154 checks; A075 prior-theorem HOLDS recorded; FEI OPEN.\nNEXT: A080/A074/A092 review root/owner proof; allocate TWO-active-core/general-gate correction from DISTINCT unused original owners, retaining old labels/full terminals; inner initial price unpaid.\n',encoding='utf-8')
with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23 13:08 UTC stage (20261023T130855Z): Recorded A075 independent HOLDS of prior all-K guard obstruction unchanged. A072 universal signed-drift bank still lacks initial price; consumed A080 fresh-AND source instead of duplicate fixed-core work. Proved unique global maximum of full c(p)/p for ALL real p in[0,1], isolated40-step root with independent48-term rational audit:4.8723210717795<lambda_star<4.8723210717892<39/8. Thus arbitrary-core exact fresh-guard hull contraction holds for every real K>=39/8, improving old8 via direct correction/fresh-influence ratio. All distinct original guard owners scaled explicitly for arbitrary m. Main recorded25154 exact checks; no floating verdict or Lean claim. New theorem review and supervisor mirror pending; arbitrary inner initial price/general two-core allocation remain unpaid. Intake wrapper TypeError fixed read-only; no math mismatch. Compute telemetry stale, no governor/work changed.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23: For ANY uniform Boolean g and fresh balanced bit y, H(AND_minus(g,y))=H(g)/2+c(p), I=I(g)/2+p, c(p)=2h2(p)-h2((1-2p)^2)/2. c/p has one global maximum: N=p*c_prime-c, N_prime=p*c_second, c_third=-4/[ln2*p*(1-p)*(1-2p)]<0 on(0,1/2). Exact isolated lambda_star in(4.8723210717795,4.8723210717892), so distinct unused original fresh influence pays correction at real K>=39/8. Exact full hull contracts1/2, or2^-m for arbitrary fresh guards/all interleavings; final guard influence is2^{-(m-1)}p, so owner costs do not recharge old core I. This scalar constant is sharp but NOT proved optimal full-hull rate. Initial arbitrary inner hull pricing and general two-core source allocation remain OPEN. A075 independently HOLDS prior all-K admission equivalence unchanged. Proof/certificates: runs/20261023T130855Z-account03-A084-continuum-parameters; new theorem external review pending.\n')
manifest={'protocol_revision':protocol['revision'],'schema_checks':'PASS','nonpilot_recorded_assertions':total,'new_claim_statement_sha256':new['statement_sha256'],'accepted_prior_statement_sha256':old['statement_sha256'],'statement_digest_convention':'SHA256 sorted compact UTF8 JSON of exact_statement and hypotheses','new_theorem_independent_review':'PENDING','mirror_verified':False,'files':[]}
for p in sorted(R.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in ['MANIFEST.json','FINAL_PERSISTENCE_CHECK.json']:continue
 assert p.stat().st_size<20*1024*1024,p
 manifest['files'].append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
put(R/'out/MANIFEST.json',manifest)
print(json.dumps({'claim':new['claim_id']+'@1','statement_sha256':new['statement_sha256'],'recorded_assertions':total,'files':len(manifest['files']),'schema':'PASS','prior_external_review':'A075 HOLDS unchanged'}))
