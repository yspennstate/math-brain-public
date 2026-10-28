from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1];P=R.parent/'20261023T120132Z-account03-A027-block-selection'
def rd(p):return p.read_text(encoding='utf-8')
def put(p,s):p.write_text(s,encoding='utf-8',newline='')
def js(p,o):put(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads(rd(R/'out/validation.json'));i=json.loads(rd(R/'out/independent.json'));pilot=json.loads(rd(R/'out/pilot.json'))
assert m['status']==i['status']==pilot['status']=='PASS'
assert m['policies']==300 and m['scalar_points']==1625 and m['controller_output_normalizer_differences']>0
gap='No influence-priced original full-reference/source admission for arbitrary Boolean functions, or necessary terminal-class target satisfying the stated eligibility tests, is proved. Bounded relative-odds resets with inherited controller shapes are a conditional target class, not a universal supplier.'
nxt='A087/A094 audit sharp scalar envelope and same original-bank integration. Test ONE actually necessary terminal-class target against bounded relative odds and A028 posterior-channel admissibility. If outside both, identify exact excess KL and an unused ORIGINAL supplier; do not generate another optional reset example.'
new='Version10 retains every earlier scoped clause. For binary row probability k and relative-odds multiplier lambda in[1/2,2], the row KL equals log2(1+(lambda-1)k)-k log2(lambda) and is <=(log2(e)-1)k<=4k/9, with the second comparison strict for k>0. The first coefficient is sharp over unrestricted binary rows, by lambda=2,k tending to0; no aggregate Boolean optimality is asserted. For binary activation with supplied original source/controller references and inherited nonempty controller shape, eta=Pr(G!=H)Var(a) is DATA-harmonic and loses exactly Pr(G!=H)*ahat({i})^2 on CONTROL exposure. Thus replace the reconstructed A029@4 allowance eta/2 by4eta/9 once at the original root, allowing arbitrary finite adaptive mixed histories, lambda_t in[1/2,2] per data row, signed canonical reconstructions, own controller/output branch normalizers and full terminal CE. Source-deficit validity remains a hypothesis. In A027 actual D4/negative-Maj3 fixture, old1/64 core debit, rate21/4, first shape conversion theta in[0,1/8] and all siblings are retained. The selected original B_OR>1/64 pays first shape<=9/1792 plus ONE all-history weighted odds allowance1/96, leaving>1/5376. A029 eta/2 exceeds the previously certified residual FLOOR by1/896; this is not insufficiency of the actual bank. No universal FEI conclusion follows.'
claims=json.loads(rd(P/'CLAIMS.json'));c=claims[-1]
c.update(version=10,exact_statement=c['exact_statement']+' '+new,proof_source=str(R/'DERIVATION.md'),status='PROVED_LOCAL_CONDITIONAL_EXTENSION; VERSION10_EXTERNAL_REVIEW_PENDING',supersedes='A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@9; all prior scoped clauses retained',first_unproved_line=gap,proof_dependencies=['A027@9 original complete terminal surplus and first shape conversion, recomputed original-account prefix','A029@4 sections7-10 independently reconstructed eta and signed-child identity; no universal supplier imported','Elementary logarithm inequality and exact rational ln2 certificates; actual current-reference physical kernels'])
c['hypotheses']+=['Version10 new target class: every row relative-odds multiplier in[1/2,2], inherited controller shape, own physical branch normalizers, no renewed original envelope','Sharpness pertains to arbitrary scalar binary rows only; supplied original account remains required']
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
c['review_records'].append({'reviewer':'A027 author alternate direct-character implementation','verdict':'PASS_NOT_EXTERNAL_ACCEPTANCE','scope':'Scalar bound, actual fixture row debts and eta releases; main separately checks full mixed signed account and both own normalizers','evidence':['out/validation.json','out/independent.json'],'formal':'NOT_RUN'})
js(R/'CLAIMS.json',claims)
pr=json.loads(rd(P/'PROGRESS.json'))
pr.update(run_id=R.name,attempt_id='A027-G-R-SELECT-021',method='Consume A029@4 all-history relative odds; sharpen scalar envelope and integrate ONE allowance into SAME A027 original full terminal reserve',mathematical_delta=f'Sharp row coefficient log2(e)-1<4/9 replaces1/2; unchanged rate21/4, old1/64 and first shape<=9/1792; ONE original odds allowance1/96 leaves>1/5376 for arbitrary finite mixed histories. Main300 policies/{m["assertions"]} predicates and1625 scalar points; alternate{i["assertions"]} checks PASS. Universal improvement zero.',deliverable_status='COMPLETE_LOCAL_ARTIFACT; VERSION10_EXTERNAL_REVIEW_PENDING',mathematical_status='SHARP_SCALAR_ENVELOPE_AND_CONDITIONAL_SAME_BANK_ALL_HISTORY_EXTENSION; FULL_FEI_OPEN',claim_versions_used=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@9','A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@4 sections7-10 reconstructed','A028@9 posterior-channel admissibility, comparison only'],claims_created_or_changed=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@10'],source_artifacts=['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','SOURCE_READS.json','REVIEW_A029.md','code/check.py','code/independent.py','code/base.py','code/exact.py','out/pilot.json','out/validation.json','out/independent.json'],next_consumers=['A028','A029','A056','A087','A094'],next_action=nxt,stagnant_substantive_attempts=0,blockers=[gap,'External review and supervisor mirrors unobserved','Brain wake exit1: attachment lock timeout; owner-model100.7h,state-of-mind85.3h,dream36.0h stale; unused as proof premises'])
js(R/'PROGRESS.json',pr);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
sources=[(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),'execution-v2; protocol schema and stage constraints'),(Path('~/AGENTS.md'),'machine shared/math constraints'),(Path('BOARD.md'),'current B06 and review entries'),(Path('claude/B06/STREAM_NOTES.md'),'v2 stream direction'),(P/'CLAIMS.json','prior candidate all clauses retained'),(P/'DERIVATION.md','original same-bank argument and unpaid supplier'),(P/'code/check.py','only prefix before def P imported to recompute original account'),(P/'code/independent.py','direct-character helper prefix before fixture reused, no full old checker executed'),(Path('agents/A029/runs/20261023T125429Z-account03-A029-child-deficit-transport/DERIVATION.md'),'sections1-10; scope reconstructed7-10'),(Path('agents/A028/runs/20261023T122923Z-account03-A028-stopping-tree-payment/DERIVATION.md'),'sections1-5 posterior-channel admissibility; contextual comparison')]
js(R/'SOURCE_READS.json',[{'path':str(p),'sha256':sha(p),'scope':scope} for p,scope in sources])
put(R/'REVIEW_A029.md','''# Scoped reconstruction of A029@4

DERIVATION sections7-10: reconstructed row identity, eta physical supermartingale, T-S signed target debt and finite frontier telescope. The stated eta/2 row bound is valid. This stage strengthens that component to4eta/9 with sharp scalar infimum coefficient log2(e)-1. The supplied-reference hypothesis and physical reference ownership are essential. Review scope excludes blanket acceptance of earlier clauses, original universal suppliers, author claims about arbitrary terminal classes, and any full FEI implication. Scope is recorded in SOURCE_READS.json by source hash; no write or review receipt is sent to another agent.
''')
report=f'''# A027 stage21: sharper row price closes the saved-reserve admission

## exact target, quantifiers, hypotheses and units

Extend the SAME original A027 terminal account to arbitrary finite adaptive mixed DATA/CONTROL histories with a prescribed relative-odds multiplier in[1/2,2] per data row, inherited controller shape and proper own reference branch normalizers. Every original charge, original tangent t=1/16, rate21/4 and full sibling remains. General identities require supplied original source/controller references. Actual admission is the seven-bit D4/negative-Maj3 fixture from stage20, not an arbitrary Boolean supplier. Entropy and KL use bits. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD, B06 STREAM_NOTES v2, own STATUS, protocol, prior complete derivation/claims and helper prefixes were consumed. A029@4 DERIVATION sections1-10 supplies an existing all-history odds mechanism; sections7-10 were reconstructed, not repeated as a new discovery. A028@9 sections1-5 identifies a distinct posterior-channel admissibility test. SOURCE_READS.json pins paths, hashes and review scope. Earlier campaign/paper baseline was not newly re-audited. Fresh exact-session brain wake exited1 with attachment lock timeout and stale owner-model100.7h/state-of-mind85.3h/dream36.0h; self-care is degraded/unverified, including wake attachment and personal/dream context, unused mathematically.

## complete derivation or exact first unsupported line

DERIVATION.md gives the scalar identity d(k,lambda)=log2(1+(lambda-1)k)-k log2(lambda). The inequality ln(1+x)<=x bounds d/k by(lambda-1-ln lambda)/ln2. Its maximum over[1/2,2] is at2 because ln2<3/4, giving c*=1/ln2-1. At lambda2,k tending to0, d/k tends to c*, proving scalar sharpness only. Exact ln2 lower certificate842/1215>9/13 yields c*<4/9; upper certificate25/36<3/4 selects the endpoint.

The reconstructed A029 envelope T=W+gamma D(Pa||Ra), S=Z+gamma D(Bern Va||Bern beta) has Dcanonical=T-S. Relative-odds targets add row cost<=4eta/9, eta=gamma Va. The source and controller accounts are carried by their own physical channels. DATA leaves eta harmonic, CONTROL releases gamma ahat(singleton)^2, so T+4eta/9 is a single original supermartingale account. Signed target changes equal raw reconstructions minus actual outcome/pair-erasure refunds; full terminal KL is retained. The finite frontier telescope therefore pays all declared adaptive resets without renewing eta or its reference owner.

At the selected OR2 child, original reach1/4 and eta3/32 make the ONE root allowance1/96. The prior B_OR>1/64 pays first shape<=9/1792 plus this allowance, leaving>1/5376, exactly. A029's weaker half-eta allowance exceeds the previously certified FLOOR19/1792 by1/896; the actual bank is not proved insufficient. Neither rate21/4 nor old1/64 debit changes. The arbitrary finite-history statement follows analytically; no finite sweep establishes its quantifiers. First unsupported universal line: {gap}

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes searches. Pilot6 policies/{pilot['assertions']} predicates PASS in{pilot['elapsed_seconds']:.3f}s. Main300 policies/{m['assertions']} exact predicates PASS in{m['elapsed_seconds']:.3f}s, including1625 scalar points,1224 physical continuation nodes,1524 full terminal occurrences and144 different controller/output normalizer occurrences. Domain is theta0,1/8, three row rules,50 declared policies: eight orders with six stopping depths plus two adaptive rules. Selected leaf has five coordinates. No symmetry reduction or exhaustive-Boolean claim. All Walsh spectra, row laws, physical kernels, signed identities and logarithm bounds use integer/Fraction arithmetic with outward rational intervals. Eleven inherited-prefix predicates recompute the earlier original account, excluded from main count.

Separate direct-character implementation, importing no main/base/exact checker, passed{i['assertions']} predicates in{i['elapsed_seconds']:.3f}s. It checks scalar identities, actual row debts, eta DATA/CONTROL releases and exact residual; it does not independently reimplement the entire mixed-tree sweep. Both implementations share earlier primitive mathematics; this is author validation, not external acceptance. Commands: python -X utf8 code/prepare.py; python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/make_independent.py; python -X utf8 code/independent.py. Preparation initially failed because out was absent, corrected by creating out before rerun; no mathematical assertion failed. Pilot/main caps60/240s, expected180MB, peak unmeasured. No expected>300MB job, GPU or detached job was used.

## proof dependencies and changed downstream conclusions

Extend existing A027 candidate9->10; retain earlier scoped clauses. A029@4 already closes the all-history half-eta transport, and this stage contributes a sharp scalar price plus its concrete admission into A027's previously certified original reserve. No blanket external acceptance of A029 or A028 is claimed. This removes the saved-floor price obstruction for bounded relative-odds targets, including mixed continuation after the first shape change. Universal supplier and eligibility of an actually required FEI terminal target remain open.

## one next mathematical action and independent reviewer

{nxt} These are saved supervisor handoff requests, not messages sent or observed reviewer acceptance. Further optional reset examples would repeat a closed local mechanism.

## actual persistence receipts or precise save blocker

Four schema-checked protocol files, proof, frozen domain, code, validation outputs and scoped source receipts are local to A027. PACKET_DELTA is byte-identical to PROGRESS. Statement hashes, file limits and two-line STATUS are checked. out/PERSISTENCE_RECEIPT.json pins local files; final readback checks hashes. No git, mail, peer-folder edit, brain-store write, supervisor publication or remote mirror is claimed. No own mathematical job remains running when finalizer completes.

## Universal bridge

This stage moves C019/C024 from one paid shape conversion followed by no-reset continuation to arbitrary finite adaptive bounded-relative-odds reconstructions, all from the SAME original terminal reserve at unchanged21/4 with old1/64 retained. The sharp scalar price is log2(e)-1<4/9; one original allowance1/96 leaves>1/5376 after the earlier shape cost. Universal constant improvement is zero: original influence-priced source admission and eligibility of an actually necessary terminal-class target remain unproved. NEXT tests that precise eligibility gap against both existing mechanisms and isolates any excess KL, the shortest route toward general induction rather than another isolated optional-target example.
'''
put(R/'REPORT.md',report)
stamp=datetime.now(timezone.utc).isoformat()
put(A/'STATUS.md','STATE: Stage21 saved: sharp row price log2(e)-1<4/9; SAME original reserve pays all-history bounded odds, rate21/4 and old1/64 retained; residual>1/5376;300 policies/12599 exact checks PASS;v10 external review pending,FEI OPEN.\nNEXT: A087/A094 review price and original allocation; test ONE necessary terminal target against bounded odds/A028 posterior admissibility, expose excess KL and ORIGINAL supplier if outside both; no more optional-reset examples.\n')
for name,line in [('WORKLOG.md',f'Stage21 consumed A029@4/A028@9; sharpened existing half-eta envelope to sharp scalar log2(e)-1<4/9. SAME B_OR pays first shape9/1792 plus one all-history1/96, leaves>1/5376, no old debit/rate change. Main300 policies/12599 exact predicates, alternate{i["assertions"]} PASS. Preparation missing-out failure fixed before pilot. Full FEI OPEN. NEXT: {nxt}'),('LEARNED.md','A027@10: scalar binary relative-odds KL/k has sharp sup log2(e)-1 on lambda[1/2,2]; rational4/9 pays all histories through eta=gamma Var(a) supermartingale. Selected weighted eta3/128 costs1/96;1/64-9/1792-1/96=1/5376. Half-eta fails only the saved lower floor, not necessarily actual bank. This closes optional bounded-odds mechanism; next must test necessary terminal eligibility or original supplier, not more optional examples.')]:
    with (A/name).open('a',encoding='utf-8',newline='') as f:f.write('\n'+stamp+' '+line+'\n')
protocol=json.loads(rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')))
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids');assert set(pr)==expected
for claim in claims:
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
    assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert len(rd(A/'STATUS.md').splitlines())==2
files=[]
for f in sorted(R.rglob('*')):
    if not f.is_file() or '__pycache__' in f.parts or f.name=='PERSISTENCE_RECEIPT.json':continue
    assert f.stat().st_size<20_000_000
    files.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
js(R/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS','timestamp':stamp,'files':files,'full_FEI':'OPEN','external_review':'PENDING','mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','files':len(files),'assertions':m['assertions'],'independent':i['assertions'],'version':10,'full_FEI':'OPEN'}))
