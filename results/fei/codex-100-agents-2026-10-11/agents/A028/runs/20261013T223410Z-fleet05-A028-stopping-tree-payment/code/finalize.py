from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]
BASE=HOME.parents[1]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,s): Path(p).write_text(s,encoding='utf-8')
def js(p,x): write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
old=HOME/'runs'/'20261012T011208Z-fleet05-A028-stopping-tree-payment'
a12=BASE/'agents'/'A012'/'runs'/'20261013T220914Z-fleet05-A012-sparse-activation-accounting'
a91=BASE/'agents'/'A091'/'runs'/'20261013T220323Z-fleet05-A091-composition-referee'
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
sources=[protocol,BASE/'BOARD.md',BASE/'claude'/'B06'/'STREAM_NOTES.md',old/'REPORT.md',old/'CLAIMS.json',
 a12/'REPORT.md',a12/'DERIVATION.md',a12/'CLAIMS.json',a91/'REPORT.md']
sources += [BASE/'agents'/a/'LEARNED.md' for a in ['A012','A023','A027','A057','A091','A095']]
js(R/'out'/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
original=json.loads((a12/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert original['statement_sha256']==hashlib.sha256(original['exact_statement'].encode()).hexdigest()
review={'claim_id':original['claim_id'],'version':original['version'],
 'statement_sha256':original['statement_sha256'],'original_exact_statement':original['exact_statement'],
 'reviewer':'A028','verdict':'ACCEPT_AT_DISJOINT_PRIVATE_ENTROPY_MUX_SUBCLAIM_SCOPE',
 'scope':'Only r=1 actual entropy identity Pi and bound Pi<=(6+1/ln2)Inf_z; scalar proof independently reconstructed; no full admission/reference/activation blanket review',
 'evidence':[str(R/'DERIVATION.md')+' one-bit endpoint',str(R/'out'/'full_validation.json')],
 'limitations':'Point-selector reference extension proved locally here; original broad A012 candidate remains at author status outside the accepted entropy subclaim'}
js(R/'out'/'REVIEW_A012_SCOPED.json',review)
statement=('Version 3 preserves all version-2 scoped results unchanged and adds the following stopping-payment interface. '
'For any Boolean signs g,h on disjoint uniform private cubes and the point indicator A on r>=1 fresh physical bits, p=2^-r, '
'F=A g+(1-A)h, d=(1-Eg Eh)/2, Q=2rp d, the complete control-first physical stopping-tree entropy payment '
'Pi=H(F)-pH(g)-(1-p)H(h) is at most (71/8)Q. The width-dependent estimate is '
'Pi<=[4+(6log2(e)+2log2(e)/e)/r]Q, while r=1 has Pi<=(6+log2(e))Q. '
'The full influence is Q+pI(g)+(1-p)I(h). Calibrated normalized supplied core references admit one explicit complete output reference '
'with CE_F=pCE_g_cal+(1-p)CE_h_cal+Pi and debt pD_g+(1-p)D_h. '
'For two priority activation events sharing one same-orientation physical bit z, private point controllers A_r,B_s, and disjoint core cubes, '
'the tree z then A then B on A-failure has terminal weights p/2 and (1-p)q/2. Its actual full entropy payment is at most (71/8) times its exclusive control influence, '
'which equals N+pq(1-Eh)(rEg-s-1)/2, N=(r+1)p(1-Eg)/2+(s+1)q(1-Eh)/2. '
'With supplied terminal allowances Lg I(g),Lh I(h), complete expected signed path cost plus terminal allowance is at most '
'max(71/8,Lg,Lh)I(F). No positive-part path bill, overlapping private data, arbitrary-selector bound or universal FEI is claimed.')
claim={'claim_id':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT','version':3,'exact_statement':statement,
'hypotheses':['Uniform physical cube; entropy bits; normalized Fourier spectra',
'Point selector fresh; private branch data/supports disjoint',
'Priority application shares exactly its one controller bit; all remaining private controllers and data blocks disjoint',
'Physical tree queries controls only, stopping at explicitly weighted terminal cores',
'Actual signed entropy increments; no clipping or extra mismatch/transcript bill',
'Any terminal FEI/reference allowance must be supplied as a checked certificate'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A028'],
'proof_source':{'report':str(R/'REPORT.md'),'derivation':str(R/'DERIVATION.md'),'checks':str(R/'out'/'full_validation.json')},
'proof_dependencies':[{'claim':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@2','scope':'point activation actual payment <=6Q and unchanged v2 component','source':str(old/'REPORT.md'),'sha256':sha(old/'REPORT.md'),'status':'LOCAL_PROOF; A027 scoped review noted on board'},
{'claim':'A012-DISJOINT-PRIVATE-MUX-ADMISSION@1','scope':'Only one-bit entropy mux bound independently reconstructed here','source':str(a12/'DERIVATION.md'),'sha256':sha(a12/'DERIVATION.md'),'status':'ACCEPTED_AT_SUBCLAIM_SCOPE_BY_A028'},
'A091 stage3 same-orientation exclusive influence identity, independently recounted here; no cap theorem imported',
'Uniform physical-tree entropy/influence conservation; direct Fourier tensor expansion and elementary scalar inequalities'],
'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
'supersedes':[{'claim_id':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT','version':2,'reason':'Narrow interface extension; no previous component withdrawn'}],
'refutes':[],'first_unproved_line':None,'next_consumers':['A027','A057','A091','A094','A012','A095','B06','B20']}
js(R/'CLAIMS.json',[claim])
validation=json.loads((R/'out'/'full_validation.json').read_text())
report='''# A028 stage 3: rare point selectors and one-bit priority stopping payment

## exact target, quantifiers, hypotheses and units

For every point selector on r fresh uniform bits and every pair of Boolean branches on disjoint private uniform cubes, prove the complete physical control-first entropy payment with both terminal entropies retained. Entropy is bits; influence uses physical uniform coordinate flips. The bound is Pi <= (71/8)Q < 9Q for positive Q, with Q=2r 2^-r Pr(g!=h). The full influence is Q+2^-r I(g)+(1-2^-r)I(h). The actual stopping-tree bill is the expected sum of signed entropy increments, not a clipped-positive or mismatch-KL upper bill.

Apply this interface to two same-orientation priority events sharing one physical control bit. Count that bit once, use actual exclusive private-control influences, and retain terminal weights p/2 and (1-p)q/2. Given terminal allowances Lg I(g),Lh I(h), the entire path plus terminal allowance is bounded by max(71/8,Lg,Lh)I(root). Thus any explicitly certified regular, bounded-overlap or threshold-formula terminal class may be used with its actual proved allowance; no opaque terminal is admitted for free. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read current BOARD.md (supervisor 2026-10-13 22:25 UTC), B06 STREAM_NOTES v2 and own STATUS at stage start; reread complete EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. Earlier required campaign, registries, plans and paper reads retain their recorded prior-stage scope; no new paper result is a premise. Current board and LEARNED files from A012,A023,A027,A057,A091,A095 identify already closed neighboring mechanisms. Read A012 stage3 REPORT, complete DERIVATION, and claim source; read A091 stage3 REPORT through overlap interface and validations. Source receipts identify the exact bytes consumed.

A012 already pays opposite shared literals with disjoint private cores; A023 handles shared-core event unions; A057 pays exclusive-controller data-only cap prefixes; A091 already derived the priority influence correction. None is rediscovered here as new. The new object is a whole rare POINT selector between two nonconstant disjoint branches and its use to pay the same-orientation priority tree. A point selector of width >1 is outside A012's literal-selector grammar: its failed-test leaves reuse the same physical h cube, so recursive literal muxes cannot be declared disjoint-private by duplicating h. A027 owns arbitrary-controller partial-core exposure; this run does not duplicate it.

## complete derivation or exact first unsupported line

DERIVATION.md gives the complete coherent Fourier formula, including the empty data row, and all scalar inequalities. With mu=Eg,nu=Eh,t=mu-nu,d=(1-mu nu)/2 and b=log2(e), the exact overhead depends only on the two means. Semiconvexity of eta(x^2), |t|<=2d, and Vg+Vh+t^2=4d give Pi <= [4+(6b+2b/e)/r]Q. For r>=2, explicit rational lower bounds on ln2 and e give coefficient <71/8. The r=1 endpoint is independently reconstructed from A012's entropy subclaim: Pi<=(6+b)Q<67Q/9. All constant and zero-cost endpoints are included.

An optional single normalized spectral reference is also constructed for this selector block. After empty calibration, nonempty branch sectors receive the appropriate squared point-indicator coefficients, while the empty data row receives its true coherent masses. Its debt is exactly pD_g+(1-p)D_h, and its CE is pCE_g_cal+(1-p)CE_h_cal+Pi. This is an analytic extension; no arbitrary-reference finite enumeration is claimed.

For the shared-bit priority tree, factor F as an outer one-bit activation of T=A g+(1-A)H_B, where H_B=1+B(h-1). Query z, then A, then B only after A fails. These operations are disjoint at the necessary interfaces. Outer and final activation costs have rate6 from A028 v2, and the middle selector has rate71/8. The full terminal-retaining entropy identity therefore gives rate71/8 against the actual control budget. That budget equals nominal independent event accounts PLUS the signed correction pq(1-nu)(r mu-s-1)/2; the nominal accounts are not substituted for physical influence. This consumes A091's ownership identity and pays the actual entropy bill it had left unbounded, without paying its separate positive cap/reset bill.

First unsupported extension: private branches sharing an additional physical data coordinate can have colliding nonempty rows. Then disagreement is not (1-mu nu)/2, and this proof does not establish Pi<=K*2rp*Pr(g!=h). Arbitrary selector substitution also remains FEI-strength (opposite constant children recover the selector). Universal terminal admission and full FEI remain unproved.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes computation. Pilot: all labeled branch tables on dimensions 0..1, point widths1..2, plus priority pairs r=s=1: 108 cases,612 exact assertions PASS. Full: all labeled branch tables on dimensions0..2, point widths1..3 (1452 cases), plus one-bit-or-constant branches and private widths r,s=1..2 in the priority gate (144 cases): 1596 cases,9432 exact assertions PASS. Maximum dimension7, no symmetry quotient or automatic escalation.

Commands from A028: python -X utf8 runs/20261013T223410Z-fleet05-A028-stopping-tree-payment/code/setup.py; then the same directory's code/check.py pilot and code/check.py full. The first run checked the provisional rate14; after the analytic sharpening the same frozen family was rerun at rate71/8. Final pilot took 0.02345 seconds and full 0.68622 seconds. A diagnostic assertion counter initially printed zero due to an imported immutable value; it was corrected to the exact helper module's live counter and both jobs rerun. Actual assertions had executed throughout.

Integer Walsh/Fraction spectra and independent physical edge counts verify the exact entropy formula, terminal weights, ownership correction and full influence decomposition. Physical point-query trees independently verify selector entropy/influence telescopes. Prime-log dictionaries give exact symbolic entropy equalities. Rational 24-term atanh intervals, with explicit tail and outward 2^48 rounding inherited transparently in code/exact.py, prove all tested 71/8 inequalities. These finite checks corroborate the analytic all-width proof; they are not an extrapolation proof. Estimate128MB, observed subsecond jobs, pilot cap60sec/full cap600sec. No >300MB job, GPU, background process or external mutation was started.

## proof dependencies and changed downstream conclusions

Version3 extends the same stopping-payment candidate; v1 and v2 results remain unchanged at their pinned scope, and no broad new universal route is added. A012's one-bit entropy-only mux subclaim was independently reconstructed and accepted locally at exactly that scope, with original statement hash preserved in out/REVIEW_A012_SCOPED.json. No blanket acceptance of its reference/admission claim is issued. A091's ownership correction is independently reproduced by physical edges; its cap, reset, history and side-information payment conclusions remain open. A028 v2 point activation rate6 supplies the outer and final stages.

B06/A057/A091 can now use a full actual control-first entropy payment on the priority gate, with terminal weights and one physical control account. This does not close their larger positive-cap or source-history bill. Known terminal certificates imply the full root FEI bound on this structural case. More fresh activation or opposite-literal tests would repeat closed mechanisms; the missing data-overlap interface is now precise.

## one next mathematical action and independent reviewer

Take a point-selector pair g(w,a),h(w,b) sharing exactly one data coordinate w. Split the coherent spectrum by w, retain both terminal entropies, and derive or refute a single-source payment for the additional nonempty-row interference using actual selector and w influences. Start from A012's saved shared-private-coordinate NEXT and A016's separator ownership results before any new finite search. Independent reviewer A094, alternate A091; A027 should check that the signed-path bill remains distinct from its partial-core transport. These are saved handoffs, not sent messages or observed review completions.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json, DERIVATION.md, frozen spec, checkers, exact pilot/full outputs, scoped review and source receipts are saved in this run. code/finalize.py checks protocol key sets, claim hash, all report headings, file size limits and two-line STATUS, then writes out/PERSISTENCE_RECEIPTS.json with artifact and rolling-file hashes. Writes are confined to A028. Local persistence is complete after this validator passes; independent review, shared index adoption, supervisor copies and mirror receipts are unobserved.

## Universal bridge

This stage moves C019 stopping-tree payment by closing an all-width rare point-selector between disjoint nonconstant cores at rate71/8 and then paying the full same-orientation one-shared-bit priority tree against its actual exclusive control influence, with both terminal costs preserved. A normalized selector-block reference additionally retains weighted terminal KL debt, but no universal history/cap charge is claimed. What remains is one additional shared data coordinate, arbitrary selector admission and universally certified terminals. NEXT isolates the first nonempty-row collision missing from this paid interface and consumes existing separator work; it is the shortest route toward universal stopping payment, whereas another disjoint activation class would not reduce the remaining ownership gap.
'''
write(R/'REPORT.md',report)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B06','packet_id':'A028','gap_id':'C019',
'attempt_id':'A028-C019-point-selector-priority-v3','method':'Coherent disjoint-branch point-selector Fourier grouping, semiconvex mean interpolation, exact exclusive physical ownership and terminal-retaining tree composition',
'mathematical_delta':'All-width point-selector complete entropy payment <=71/8 control influence; same-orientation one-shared-bit priority tree fully paid with actual signed ownership correction and terminal weights; calibrated selector-reference debt conservation; A012 one-bit entropy subclaim reconstructed',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'POINT_SELECTOR_PRIORITY_CASE_PROVED_UNIVERSAL_FEI_OPEN',
'claim_versions_used':['A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@2-point-activation-scope','A012-DISJOINT-PRIVATE-MUX-ADMISSION@1-entropy-subclaim-only','A091-stage3-exclusive-priority-influence-identity'],
'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':3,'status':claim['status']}],
'source_artifacts':[str(R/p) for p in ['REPORT.md','DERIVATION.md','code/check.py','out/full_validation.json','out/REVIEW_A012_SCOPED.json','out/SOURCE_RECEIPTS.json']],
'next_consumers':claim['next_consumers'],
'next_action':'Derive signed nonempty-row ownership for point-selector branches sharing exactly one physical data coordinate; consume A012 shared-coordinate NEXT and A016 separator account before freezing a search',
'stagnant_substantive_attempts':0,'blockers':['Shared private data invalidates disjoint Fourier sectors and mean-only disagreement','General selectors and arbitrary terminal admission remain FEI-strength','Independent v3 review and supervisor mirror/adoption not observed'],
'packet_ids':['A028']}
js(R/'PROGRESS.json',progress); js(R/'PACKET_DELTA.json',progress)
status='STATE: A028 stage 3 saved point-selector and same-orientation shared-bit priority full entropy payment <=71/8; 1596 cases/9432 exact assertions; v3 review pending; full FEI OPEN.\nNEXT: A094/A091 review; consume A012/A016 shared-data separator work and derive one-coordinate nonempty-row ownership with both terminal entropies retained.\n'
write(HOME/'STATUS.md',status)
stamp=datetime.now(timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{stamp} — stage3 {R.name}: consumed updated board; avoided A012 opposite-literal, A023 shared-core union and A091 ownership repeats. Proved rare point-selector exact entropy formula, rate71/8, calibrated reference debt and same-orientation priority full payment against actual ownership. Pilot108/612 and full1596/9432 exact checks PASS; frozen128MB, no heavy job. Independently reconstructed only A012 one-bit entropy subclaim. Corrected diagnostic counter import and reran. v3 candidate extends prior scope; universal FEI open. NEXT one shared data coordinate.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('''\n## Stage 3: rare point selectors and priority ownership

* For fresh point A_r and disjoint arbitrary Boolean g,h, p=2^-r, d=(1-Eg Eh)/2: Pi=H(A g+(1-A)h)-pH(g)-(1-p)H(h)<=71Q/8, Q=2rp d. Full influence is Q+pIg+(1-p)Ih. For r>=2 use coefficient4+(6b+2b/e)/r; r1 is A012's independently reconstructed (6+b) entropy subclaim. Exact rational constant proof: ln2>842/1215>9/13 and e>8/3.
* Exact formula includes the interfering empty row: 2rp[Vg+(1-p)Vh+(1-p)(mu-nu)^2]+Vh eta((1-p)^2)+eta((p mu+(1-p)nu)^2)-peta(mu^2)-(1-p)eta(nu^2)+p(1-p)(mu-nu)^2log2(1/(mu-nu)^2). Semiconvexity eta(x^2)''>=-6log2(e) pays the Jensen term; |mu-nu|<=2d pays the remaining scalar entropy.
* Calibrated normalized core references extend to one point-selector output reference with exact debt pDg+(1-p)Dh and CE=pCEg_cal+(1-p)CEh_cal+Pi. This is a complete spectral reference, not physical transcript decoding or rounded prefix cost.
* For same-orientation priority events sharing z, F=activation_z(A_r g+(1-A_r)activation_Bs(h)): terminal weights p/2,(1-p)q/2. Actual control influence is nominal N plus pq(1-nu)(r mu-s-1)/2, matching A091; correction may have either sign. Query z once, then A, then B on failure. Full entropy payment <=71/8 of that actual account; terminal certificates give max(71/8,Lg,Lh) root rate.
* Rare-selector h is reused on every failed point-test branch, so duplicating it into A012 literal-mux grammar violates private-support disjointness. Whole-block payment handles this reuse honestly. Shared data remains unpaid: mean-only disagreement and separated nonempty sectors fail. Signed entropy increments are not positive-part or mismatch upper bills. Full FEI stays open. Exact validation1596 cases/9432 assertions, maxdim7.
''')
pf=json.loads(protocol.read_text(encoding='utf-8'))
def find_fields(obj,key):
 if isinstance(obj,dict):
  if key in obj:return obj[key]
  for v in obj.values():
   ans=find_fields(v,key)
   if ans is not None:return ans
 if isinstance(obj,list):
  for v in obj:
   ans=find_fields(v,key)
   if ans is not None:return ans
 return None
cf=find_fields(pf,'claim_fields'); pr=find_fields(pf,'progress_fields'); rf=find_fields(pf,'report_fields')
assert set(claim)==set(cf),(set(claim),cf)
assert set(progress)==set('packet_ids' if x.startswith('packet_ids') else x for x in pr)
for heading in rf: assert ('## '+heading) in report,heading
assert sha(R/'PROGRESS.json')==sha(R/'PACKET_DELTA.json')
assert len((HOME/'STATUS.md').read_text().splitlines())==2
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
assert validation['status']=='PASS' and validation['total_cases']==1596 and validation['assertions_passed']==9432
artifacts=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json' and '__pycache__' not in p.parts]
assert all(p.stat().st_size<20_000_000 for p in artifacts)
receipt={'run_id':R.name,'validation':'PASS','schema_checks':'exact claim/progress field sets and all report headings',
'artifacts':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in artifacts],
'rolling_files':[{'path':str(HOME/p),'sha256':sha(HOME/p)} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']],
'mirror_status':'UNOBSERVED; supervisor owns copying','write_scope':'A028 only'}
js(R/'out'/'PERSISTENCE_RECEIPTS.json',receipt)
print(json.dumps({'status':'PASS','artifact_count':len(artifacts),'claim_version':3,'cases':1596,'assertions':9432,'receipt':str(R/'out'/'PERSISTENCE_RECEIPTS.json')},indent=2))
