from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parent.parent
def put(p,t):p.write_text(t,encoding='utf-8',newline='\n')
def dump(p,x):put(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
oldrun=A/'runs/20261023T124913Z-fleet03-A014-overlap-beyond-worst-case-read'
oldprogress=json.loads((oldrun/'PROGRESS.json').read_text(encoding='utf-8-sig'))
results={n:json.loads((R/'out'/n).read_text(encoding='utf-8-sig')) for n in ['pilot.json','check.json','local_pilot.json','local_check.json']}
nonpilot=results['check.json']['assertions']+results['local_check.json']['assertions']
assert nonpilot==3685
for result in results.values():assert result['elapsed_seconds']<55
statement=('For every integer r>=12 let m=r^2 and G=K_r disjoint union m edges, C its independent-set indicator, f=1-2C, s=EC and I the actual total influence. Use the ORIGINAL complete edge-occupation source with fixed clique edge activities 1/(r-1), isolated-edge activities 0<lambda_j<=1, all root/attachment factors and full normalization, and actual empty/nonempty calibration. Define kappa_dil=sum_j Pr_{fhat^2}(S meets isolated edge j) log2(1/lambda_j)/I=s sum_j log2(1/lambda_j)/I. Then the ENTIRE reference cross-entropy is at most (259/32+kappa_dil) I. Local activities lambda_j=1 give kappa_dil=0 and CE<=259I/32<9I despite indispensable positive-DNF maximum read r-1 tending to infinity. In contrast the globally feasible uniform scale lambda_e=1/Delta=1/(r-1) gives complete CE/I>=(2/3)log2(r-1), which diverges on the SAME actual all-relevant Boolean family. Full H(f)/I<6, so this refutes universal payment of the globally uniform occupation source, not FEI. The exact influence is s[(4/3)r^2+2r(r-1)/(r+1)]. Both normalizers, all label/root/attachment costs and the empty wrapper are retained. For m disjoint edges alone the exact full nonempty-cost ratio is (3/4)log2(1/lambda)+(1/2)log2(32)+(1/4)log2(48)+3[1-(3/4)^m]log2[(1+lambda/12)^m-1]/m; its lambda dependence cancels at m=1. The repaired root, with general projected/calibrated references, retains all actual full-CE decrease bookings and both full terminals on every finite stopping tree. No refreshed history budget or arbitrary-query fee payment is asserted. Arbitrary connected overlaps and full FEI remain open.')
gap=oldprogress.get('gap_id','C020-ORIGINAL-INTRINSIC-UNPADDED-WHOLESET')
next_action='A006/A015 construct and pay a locally weighted original whole-set source on connected physically overlapping gates, retaining full normalizer, actual influence and old terminal/debit ledger; A086/A094 independently reconstruct v9. Use the global-scale counterfamily and A007 arbitrary-core embedding as mandatory controls.'
claim={
 'claim_id':'A014-INTERFERENCE-COMPLETE-CRITERION-AND-PP-GUARD','version':9,
 'exact_statement':statement,'hypotheses':['Uniform finite cube; sign Boolean output; base-two entropy and ideal complete reference cross-entropy','Integers r>=12,m=r^2; all actual clique-plus-matching coordinates relevant; positive activities fixed before sampling','Clique edge activities 1/(r-1); each isolated-edge activity in (0,1]; vertex incident activity sums at most one','Original maximal-matching/root/attachment occupation factors including J; F(empty)=1; entire nonempty normalizer and actual variance wrapper','Stopping statements use actual full-CE decreases only, not arbitrary query invoices'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A014'],
 'proof_source':{'path':str(R/'DERIVATION.md'),'locators':['sections 1-2: exact factorization and global feasible source obstruction','section 3: matching identity and m=1 cancellation','sections 4 and 4a: same-construction local repair and explicit spectral congestion theorem'],'certificates':[str(R/'out/check.json'),str(R/'out/local_check.json')]},
 'proof_dependencies':[{'claim_id':'A014-INTERFERENCE-COMPLETE-CRITERION-AND-PP-GUARD','version':6,'scope_used':'General original-reference projection/calibration and full-CE stopping identity ONLY; not needed for root inequalities.'}],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[{'claim_id':'A014-INTERFERENCE-COMPLETE-CRITERION-AND-PP-GUARD','version':8,'scope':'New source-payment stage; previous v8 results retained in their immutable original run, not retracted.'}],
 'refutes':[{'statement':'The fixed globally uniform feasible activity lambda=1/Delta always makes the complete original occupation reference cost <=K I for some absolute finite K on all graph edge unions','witness':'K_r disjoint union r^2 isolated edges, r>=12; all relevant; read r-1; CE/I >=(2/3)log2(r-1), while H/I<6','scope':'Global uniform occupation source only, not locally weighted sources, actual FEI or prior dense/padded theorems'}],
 'first_unproved_line':'Existence and ORIGINAL influence payment of an intrinsic locally weighted whole-set source for arbitrary connected physical overlaps; arbitrary signed-core source pricing is FEI-equivalent.',
 'next_consumers':['A006','A007','A015','A086','A094','B03','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B03','packet_id':'A014','gap_id':gap,
 'attempt_id':'A014-stage21-global-dilution-to-local-spectral-weights',
 'method':'Exact occupation factorization; actual physical product Fourier moments; adversarial global-source family; local activity repair with signed normalizer; bounded exact certificates',
 'mathematical_delta':'Globally feasible uniform 1/Delta source is NOT universally influence-paid: actual growing-read family CE/I >=(2/3)log(r-1) but H/I<6. SAME occupation construction with local weights has CE<9I. More generally CE<=(259/32+kappa_dil)I with explicit activation-weighted spectral congestion, zero locally.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':6,'scope':'stopping extension only'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':9}],
 'source_artifacts':[str(R/'DERIVATION.md'),str(R/'out/SOURCES.json'),str(R/'out/check.json'),str(R/'out/local_check.json'),str(R/'out/ATTEMPTS.md')],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI OPEN; arbitrary connected whole-set source unpaid','Independent review pending','Lean admission held under 5500MB free: no compiler launched; not Lean-checked','Supervisor mirroring unverified; personal-context wake sources stale and not used as mathematical evidence'],
 'packet_ids':['A014']}
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report='''# A014 stage21: a global feasible scale fails; local spectral weights repair it

## exact target, quantifiers, hypotheses and units

For EVERY integer r>=12 set m=r^2 and take the actual graph G=K_r disjoint union m edges. Its edge-union sign has all coordinates relevant and indispensable positive-DNF maximum read r-1. Entropy is in bits on the uniform cube. Keep the ORIGINAL complete occupation construction and actual empty/nonempty wrapper. Clique weights are 1/(r-1), and each isolated-edge weight lambda_j may be ANY fixed number in (0,1]. The explicit spectral dilution congestion is kappa_dil=sum_j Pr_p(S meets edge j)log(1/lambda_j)/I. The ENTIRE cost obeys CE<=(259/32+kappa_dil)I. Component-local weights give kappa_dil=0 and CE<=259I/32<9I despite growing read. In contrast, the globally feasible scale 1/Delta on the SAME graph gives CE/I>=(2/3)log(r-1), while actual H/I<6. This is a reference obstruction, not an FEI counterfamily or a new claim of FEI for read-once functions.

## sources actually read, revisions and theorem locators

Read machine AGENTS, EXECUTION_PROTOCOL 2026-10-11-execution-v2, the campaign navigation/registries/plan, supplement and sources, four supplied paper text versions, BOARD, B03 STREAM_NOTES v2, own prior run reports/claims and current rolling files. Full-text source hashes and explicit source encodings are in out/SOURCES.json. A015 CORE_FUSION sections on signed costs and its uniform-core barrier, A006's shared-core report and A007's arbitrary-core universality report guide the unresolved scope; no peer claim is imported as a new proved premise. Source factor definitions and original clique coefficients are reconstructed from A014 v6-v8, with the normalizer argument repeated explicitly. No threshold or percolation paper theorem is needed for the new proof. One read-only math recall returned Boolean-realizability and coordinate-entropy guards; no recalled card is a proof dependency. The wake reported stale personal-context files and a partial dream; the owner was alerted, and these notes are not mathematical evidence.

## complete derivation or exact first unsupported line

DERIVATION sections 1-4a are the all-dimensional proof. Occupation matching choices factor exactly over components, giving full normalizer (1+Z_K)product_j(1+lambda_j/12)-1. Actual product indicator spectra give Pr_p(S meets edge j)=s and I=s[(4/3)m+2r(r-1)/(r+1)]. For global weights the full normalizer cancels the potentially negative clique cost, rather than being omitted, and leaves the growing spectral dilution bill. For local weights, normalize each FULL component law and condition their product nonempty ONCE. Its signed conditioning refund is retained. Clique atom lengths <=21r/4 and exact edge-state lengths pay the entire reference, producing 259/32+kappa_dil. The same proof allows unequal isolated-edge activities. The exact one-edge boundary cancels all activity dependence, ruling out a false raw-mass-only obstruction.

The proof also bounds actual H/I<6 and keeps all auxiliary physical variables in I. Every old actual full-CE decrease and BOTH complete projected/calibrated terminal references telescope from the repaired root using v6; no arbitrary query fee or new history budget is asserted. First unsupported universal line: find and influence-pay an intrinsic local whole-set source for arbitrary CONNECTED physically overlapping gates, including its full normalizer and inherited terminal ledger. Component-local correction does not price connected interactions or arbitrary signed cores. Full FEI is OPEN.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC and FROZEN_LOCAL_VALIDATION precede execution. Run python -X utf8 code/check.py --pilot, code/check.py, code/local_check.py --pilot, and code/local_check.py from the run directory. Main base: all 168 fixed (r,m) pairs r=3..16,m=1..12; all 480 physical subsets of four actual graphs at (r,m)=(3,1),(3,2),(4,1),(4,2); direct integer Walsh and physical edge flips; 245 scalar r values through256. A separate recursive enumeration of every maximal matching and attachment agrees with the closed component masses. Main base passes3089 assertions in0.906207s. Mixed-weight main repeats the independent occupation enumeration on480 atoms and checks four large exact profiles r=12,16,24,32 with m=r^2, full global/local normalizers, complete CE intervals and actual H intervals:596 assertions in23.243806s. Total3685 nonpilot exact assertions. Successful final pilots have1372 and52 assertions, separately (overlap excluded), in0.045133s and0.323144s.

Arithmetic is integer/Fraction with exact outward log enclosures from the positive atanh series and its explicit tail, followed by dyadic rounding. All signs are certified; floats record runtime only. The initial local pilot was INCONCLUSIVE at the CE upper comparison because fixed absolute log rounding overwhelmed exponentially small influence. out/ATTEMPTS.md preserves this failed assertion; FROZEN_PRECISION_REPAIR precedes relative precision near1 and the successful repaired runs. No failure is silently counted as a certificate. The source-reader initially met non-UTF8 text; it now records the explicitly selected decoding and hashes without modifying the source.

No search exceeded its55s cap or60MB estimate, no GPU, remote compute, automatic dimension escalation, detached process or window was used. A conservative memok check returned OK (4.5GB physical and10.6GB commit free), then the formal checker independently HELD at its5500MB admission floor, launching no compiler. out/lean_attempt.json is a SETUP_UNVERIFIED message, not a proof receipt. LocalEdge.lean formalizes scalar constants and component algebra only, and is NOT claimed checked. The mathematical rung is an author proof with exact finite certificates, pending independent reconstruction.

## proof dependencies and changed downstream conclusions

Bundled source-payment claim advances v8->v9; previous restricted theorems remain preserved, with no retraction. New root inequalities are self-contained; v6 is used only for the optional stopping-tree extension. The proposed universal global 1/Delta source is now REFUTED, not an open sufficient lemma. Dense-graph and padded-core bounds retain their explicit hypotheses. A015 uniform-core and A007 arbitrary-core barriers remain applicable: arbitrary source existence cannot be renamed an easy leaf. No peer acceptance, external priority or novelty is claimed.

## one next mathematical action and independent reviewer

A006/A015: construct a feasible locally weighted source for CONNECTED physical overlap and pay its complete original expected cost from actual unused influence. Keep the full signed normalization, both terminals and old bookings; test against this global-scale family and A007's arbitrary-core embedding. A086/A094 independently reconstruct the v9 lower bound, local repair and general-activity congestion theorem. This is a source-bound review request in the artifacts; no message or review acceptance is asserted.

## actual persistence receipts or precise save blocker

Four protocol files, complete derivation, frozen specifications, scripts, exact outputs and failed-attempt record are saved only inside A014. STATUS has exactly two lines; WORKLOG is dated and appended; LEARNED records the exact new theorem and failed precision guard. out/RECEIPTS.json records local SHA256/sizes and verifies schema, statement and delta equality. Every file is below20MB. Supervisor copying, shared adoption, remote mirror and independent review are UNVERIFIED. No git, email, brain-store write, other-agent mutation, trading access or process intervention was performed. Shared task/checklist writes were not made under the explicit A014-only output restriction.

## Universal bridge

C020 whole-set payment gains an exact source-level obstruction and repair: even globally feasible1/Delta activities can produce CE/I growing logarithmically on an actual all-relevant unbounded-read family with H/I<6, while intrinsic local weights yield the SAME complete occupation construction with CE<=259I/32. The explicit activation-weighted kappa_dil replaces read in the sufficient bound and is identically zero locally; normalization and C019-style full terminal/debit conservation remain paid once. The universal gap is connected physical interaction under a locally weighted original source, not component multiplication or auxiliary-influence removal. NEXT isolates and prices one connected overlap because another dense/padded family or uniform reference would leave precisely this newly exposed source defect unpaid. Full FEI remains OPEN.
'''
put(R/'REPORT.md',report)
put(A/'STATUS.md','STATE: A014 stage21 saved: global feasible1/Delta source FALSE; actual growing-read family CE/I>=2log(r-1)/3 but H/I<6; SAME local occupation CE<9I, explicit kappa_dil;3685 exact checks PASS;review pending;FEI OPEN.\nNEXT: A086/A094 review v9; A006/A015 price locally weighted ORIGINAL source for CONNECTED physical overlap, full normalizer/both terminals/old bookings; no global thinning or free auxiliary-influence removal.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
    f.write('\n'+now+' stage21: Read board/lead and prior stage. Proved and exactly checked global feasible activity dilution obstruction on K_r plus r^2 edges and same-source local repair with explicit spectral kappa.3685 nonpilot checks pass. Failed absolute-rounding pilot preserved and repaired; Lean admission HELD, no compiler. Connected whole-set source remains unpaid; FEI OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
    f.write('\nStage21 (2026-10-26): On K_r disjoint union r^2 edges,r>=12, original uniform feasible lambda1/(r-1) has FULL CE/I>=2log(r-1)/3 despite actual H/I<6 and every variable relevant. Thus global1/Delta source payment is FALSE. Disjoint occupation F factors exactly INCLUDING F(empty)=1; nonempty Z=(1+Z_K)product(1+lambda_j/12)-1. Local clique weight1/(r-1), isolated-edge weight1 gives SAME occupation CE<=259I/32<9I, maximum read r-1. More generally kappa_dil=sum_j Pr_p(S meets edge j)log(1/lambda_j)/I=s sum_jlog(1/lambda_j)/I yields CE<=(259/32+kappa_dil)I. Reference choice is fixed before target. Exact isolated-edge masses1,lambda/32,lambda/32,lambda/48; m=1 activity dependence cancels after normalizing. Never drop signed normalizers. Relative precision near1 is essential when v and I are exponentially small: absolute2^-40 log rounding can overwhelm the whole claim. Full FEI and connected local-source payment remain OPEN.\n')
# Source receipts may still be writing; final external validation checks them.
records=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        data=p.read_bytes();assert len(data)<20_000_000
        records.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
rolling=[]
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=A/name;rolling.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert field in report
dump(R/'out/RECEIPTS.json',{'saved_at':now,'files':records,'rolling':rolling,'schema_check':'PASS','statement_hash_check':'PASS','delta_equality':'PASS','nonpilot_assertions':nonpilot,'formal_status':'SETUP_UNVERIFIED_HELD','mirror_status':'UNVERIFIED'})
print(json.dumps({'protocol_files_written':4,'run':str(R),'nonpilot_assertions':nonpilot,'recorded_files':len(records),'full_fei':'OPEN'}))
