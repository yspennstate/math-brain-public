from pathlib import Path
import json, hashlib, datetime

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
OWNER=Path(r'~')
SRC=OWNER/'brain_workers/FEI100_20261011/agents/A069/runs/20261026T224025Z-fleet04-A069-geometric-transfer'
P=OWNER/'mop_fei100/reports/fei-2026-10-11'
def read(p):
    return p.read_text(encoding='utf-8-sig')
def save(p,v):
    p.write_text(v,encoding='utf-8',newline='\n')
def js(p,v):
    save(p,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def statement_hash(c,key='statement'):
    canonical=json.dumps({key:c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    return hashlib.sha256(canonical).hexdigest()

res=json.loads(read(R/'out/results.json'))
assert res['status']=='PASS' and res['script_sha256']==sha(R/'code/check.py')
protocol=json.loads(read(P/'EXECUTION_PROTOCOL.json'))
source_claims=json.loads(read(SRC/'CLAIMS.json'))
review=source_claims[1]
assert statement_hash(review)==review['statement_sha256']
assert sha(SRC/'DERIVATION.md')==review['proof_source']['sha256']
assert review['claim_id']=='A069-UNIFORM-NEAR-BOOLEAN-SOURCE-OBSTRUCTION'
review['review_records'].append({'reviewer':'fleet04/A070','verdict':'HOLDS_AT_FULL_STATED_SCOPE','independent':True,'substantive_repair':False,'reviewer_conflict':False,'review_source':str(R/'DERIVATION.md'),'review_sha256':sha(R/'DERIVATION.md'),'locators':'Sections 1 and 4; independent integer-product/Walsh certificate in out/results.json','method':'Reconstruct finite Gaussian-product masses, entropy-to-energy bound, uniform defects and homogeneous full-terminal telescope without importing author code; exact product values and independent Walsh/convolution calculations. No repair.'})
review['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A070_PENDING_B20'
prior=source_claims[0]
own_prior=json.loads(read(A/'runs/20261023T133455Z-fleet03-A070-analytic-route-referee/CLAIMS.json'))
old=next(c for c in own_prior if c['claim_id']==prior['claim_id'])
assert old['statement_sha256']==prior['statement_sha256']
assert statement_hash(prior,'exact_statement')==prior['statement_sha256']
assert old['exact_statement']==prior['exact_statement'] and old['hypotheses']==prior['hypotheses']
js(R/'out/CONSUMED_REVIEW.json',{'claim_id':prior['claim_id'],'version':prior['version'],'statement_sha256':prior['statement_sha256'],'external_review':prior['review_records'],'source_path':str(SRC/'CLAIMS.json'),'source_sha256':sha(SRC/'CLAIMS.json'),'disposition':'Consumed independent A069 receipt; no self-review or shared registry mutation.'})

statement=('There are normalized REAL functions G_k, k>=2, on finite uniform cubes, uniformly within 1/k+1/(2k^2) of an actual Boolean parity, with sup|G_k^2-1|<=2/k+1/k^2, whose signed Boolean convolution equations hold EXACTLY for every nonempty U with |U|<2k and whose squared norms are EXACTLY one at EVERY physical restriction fixing fewer than 2k coordinates. Nonetheless H(G_k)/J(G_k)>2k/(3(1+1/k^2)) tends to infinity. Explicitly parity-lift every coordinate of A069 Gaussian-product g=(x0+h/k)/sqrt(1+A/k^2) to a disjoint block of k bits, with n=2^(2k^4), m=2^(k^4), h=Im product_j(m+i y_j)/sqrt(n+1), A=E h^2. The first nonzero convolution and a nonunit restriction occur at degree/depth 2k. Every normalized dominating original reference and every adaptive stopping tree, keeping inherited frequency marginals, homogeneous masses and full terminal cross-entropy, has positive rate4 invoice plus expected terminal CE >=H(G_k)-4J(G_k). For trees of depth at most 2k-1 the analogous reference-free entropy invoice plus expected full terminal entropy has the same lower bound, with all node/child spectra normalized. J is squared derivative energy; these are real relaxation guards, not Boolean FEI counterexamples. The rounded Boolean family is a parity with H=0 and influence k.')
new={
 'claim_id':'A070-EXACT-SHALLOW-NORMALIZATION-SOURCE-OBSTRUCTION','version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite physical cubes, REAL functions and base-two entropy; squared derivative energy J, never real change-indicator influence.','k>=2; all parity blocks disjoint, of width k; all infinite-family parameters symbolic and no huge cubes allocated.','Exact restriction-normalization and convolution claims have strict depth/degree cutoff 2k; failure at 2k explicitly exhibited.','For the source invoice: one normalized original support-dominating reference, inherited by frequency marginalization only, all physical reach weights, both full outcomes and all terminal costs retained.','Independent original random seeds allowed; no refreshed source, forgotten debit or free terminal.','No full FEI solution or novelty priority assertion.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['fleet04/A070'],
 'proof_source':{'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md'),'locators':'Sections 2-4; reviewed prerequisite Section 1; exact certificate out/results.json'},
 'proof_dependencies':[{'claim_id':review['claim_id'],'version':1,'statement_sha256':review['statement_sha256'],'acceptance':'Independent unchanged full-scope reconstruction in this run; direct self-contained proof included.'}],
 'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unregistered relaxed source principle: any finite or growing finite prefix of exact Boolean convolution and exact shallow physical child normalization, together with uniform approximate Booleanity, supplies a dimension-independent influence-energy source payment.'],
 'first_unproved_line':None,'next_consumers':['A069','A031','A033','A088','A094','B14','B20']}
new['statement_sha256']=statement_hash(new)
claims=[review,new]
required=set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==required for c in claims)
js(R/'CLAIMS.json',claims)

formal=json.loads(read(R/'out/FORMAL_RECEIPT.json')) if (R/'out/FORMAL_RECEIPT.json').exists() else {'status':'NOT_ATTEMPTED'}
formal_status=formal['status']
next_action='A031/A033/A069 use a genuinely FULL Boolean consequence, excluding the exact shallow-normalization family, to price one necessary original-source update from SAME unused influence; retain old debits and both full terminals. A088/A094 independently review this parity lift and stopped-terminal extension.'
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A070','gap_id':'G-A070-STABLE-COMPLETE-ANALYTIC-CODE','attempt_id':'A070-stage10-uniform-near-Boolean-review-and-exact-shallow-boundary',
 'method':'Independent Gaussian-integer physical-value/Walsh reconstruction; disjoint parity-block lift; exact convolution and all shallow restrictions; terminal-inclusive adaptive telescope.',
 'mathematical_delta':'A069 uniform near-Boolean obstruction independently HOLDS unchanged. Exact convolution through degree2k-1 and exact norm at EVERY depth<2k restriction coexist with uniform proximity to a parity and H/J growing at least linearly in k. Source/entropy full-terminal lower bound applies to stopped trees. Full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_PENDING_SUPERVISOR_COPY','mathematical_status':'SOURCE_REVIEW_HOLDS_NEW_REAL_ROUTE_OBSTRUCTION_PROOF_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':review['claim_id'],'version':1,'statement_sha256':review['statement_sha256']},{'claim_id':prior['claim_id'],'version':1,'statement_sha256':prior['statement_sha256'],'scope':'External independent-review receipt consumed, not a circular proof dependency.'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'status':c['status']} for c in claims],
 'source_artifacts':['REPORT.md','DERIVATION.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','code/formal_attempt.py','code/finalize.py','out/pilot.json','out/results.json','out/FORMAL_RECEIPT.json','out/CONSUMED_REVIEW.json','out/SOURCE_MANIFEST.json','out/RECEIPTS.json'],
 'next_consumers':['A031','A033','A069','A088','A094','B14','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':[{'scope':'Full FEI','reason':'Original arbitrary-Boolean-core influence-priced source/payment remains unproved. This stage rejects a relaxation, not the actual Boolean target.'},{'scope':'Review/persistence','reason':'New parity/stopping result awaits independent review; supervisor private copy, B20 adoption and brain ingestion unverified.'},{'scope':'Formal check','reason':formal_status},{'scope':'Wake','reason':'Owner-model184h/state-of-mind169h/latest-dream41h stale; owner alerted before affected notes used; current instructions and source evidence govern.'}],
 'packet_ids':['A070']}
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
js(R/'PROGRESS.json',progress); js(R/'PACKET_DELTA.json',progress)

report=f'''# A070 stage10: exact shallow Boolean tests leave the source unpaid

## exact target, quantifiers, hypotheses and units

Independently referee A069-UNIFORM-NEAR-BOOLEAN-SOURCE-OBSTRUCTION@1 and test whether exact shallow norm/convolution constraints repair its relaxed source-payment failure. Units are bits. REAL functions use squared-derivative energy J; actual Boolean functions use pivotal influence I. The new explicit all-k guard has unit root norm, every restriction of depth<2k exactly normalized, all convolution identities of degree<2k exact, uniform distance to an actual Boolean parity tending to zero, and H/J>2k/(3(1+1/k^2)). The rounded Boolean family has H=0,I=k. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2, current BOARD/B14 lead notesv2, A070 STATUS/LEARNED/WORKLOG and previous source artifacts, campaign README/current status and targeted registry/plan/supplement records were consulted. Sources are pinned in out/SOURCE_MANIFEST.json. A069 run20261026T224025Z DERIVATION Sections1-5 and both full CLAIMS are the substantive source. Its new theorem is reconstructed unchanged; its independent acceptance of the previous A070 boundary is consumed rather than self-awarded. Four paper-version scope openings and relevant theorem locators were revisited; percolation30pp Lemma2.1 is an arbitrary-random-set encoding, whose occupancy payment is separate. No new threshold/percolation premise is used. Those supplied text exports decode as cp1252; the initial UTF-8-only read failed and was retried explicitly, without modifying sources. The packaged cyclic companion certificate remains unavailable; no cyclic certificate replay is claimed. One read-only math recall gives existing singleton/convolution and conditioned-entropy guards, not an accepted source-payment theorem. No novelty priority is asserted. Current user continuation governs over old campaign clocks.

## complete derivation or exact first unsupported line

DERIVATION Sections1-4 contain the complete finite Fourier derivation. The Gaussian product supplies a bounded h with A>1/3, energy<=1 and each atom<=1/(n+1). Normalization Z cancels exactly in H/J. Disjoint parity blocks preserve entropy and multiply energy by k. Since the original square has only even degrees and no nonconstant term below degree2, its lift has none below degree2k. Conditional averaging proves every shallow restriction norm exactly1; the explicit first nonunit norm occurs after fixing the dictator block and one y block. Taking n=2^(2k^4),epsilon1/k leaves H/J divergent despite the factor k. The homogeneous CE/energy telescope gives a full-terminal lower bound H-4J for EVERY stopping tree; normalized shallow trees also satisfy the reference-free entropy counterpart. The first unsupported Boolean line remains an ORIGINAL influence-priced source/update for arbitrary actual Boolean cores using a full Boolean consequence that excludes these real guards.

## executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC precedes search. Independent pilot n4,b1,epsilon1/2 passes190 exact predicates. Final frozen fixtures n4,b1,2,3,epsilon1/2,1/4 plus binomial n4,16,64 and their18 parameter combinations pass {res['checks']} exact predicates in {res['runtime_seconds']:.6f}s arithmetic time. An initial final pass has460074 predicates;72 in-domain binomial normalization/ratio checks complete the frozen18 parameter combinations. No range expansion or floating sign test occurs. Actual integer Gaussian products and direct Walsh transforms are independent of author code; every lifted physical square coefficient, all shallow restriction masks/assignments and the direct boundary average are exact. n16,64 use finite binomial formulas; the infinite k family is symbolic and never allocated. Code and outputs are in code/check.py and out/pilot.json,out/results.json. Commands: python -B -X utf8 code/check.py --pilot; the same without --pilot (run relative to this run's parent path). Resource estimate70MB, arithmetic cap55s, no heavy search, GPU, detached worker or dimension escalation.

Formal receipt: {formal_status}. code/formal_attempt.py requests fresh memok admission before any compiler and uses one windowless BelowNormal thread with1024MB job cap and45s compiler timeout. Any accepted formal result is limited to the explicitly named Gaussian-integer norm identity, not the Fourier proof or FEI. The full theorem's rung is proof with exact finite certificates, pending independent review; no full formal verification is claimed.

## proof dependencies and changed downstream conclusions

A069's source theorem independently HOLDS at full stated scope without repair. The exact statement hash is preserved in local CLAIMS; original sources remain untouched. Prior A070 homogeneous-boundary external acceptance is source/hash matched in out/CONSUMED_REVIEW.json. New parity/stopped-tree consequences depend on the reconstructed product family and direct finite Fourier identities. They reject using exact finite-depth norms or truncated convolution plus small uniform defect as a universal real source supplier. They preserve every existing Boolean theorem and require no source reset, renewed budget or omitted terminal. No independent self-acceptance occurs.

## one next mathematical action and independent reviewer

{next_action}

## actual persistence receipts or precise save blocker

The four protocol artifacts, derivation, frozen spec, code and exact outputs are saved in this requested A070 run. STATUS is exactly two lines; WORKLOG/LEARNED are current. out/RECEIPTS.json verifies exact protocol key sets, statement/proof hashes, matching packet delta, limits and local artifact hashes. Supervisor remote copy, shared-index adoption, private mirror and brain ingestion remain unverified. No git, mail, research brain write, other-agent mutation, trading access or unrelated process stop occurs. Current compute record is ok with14.2GB free when read; no resource shedding or system changes occur.

## Universal bridge

This stage advances C024/C019 by accepting A069's uniform near-Boolean source obstruction and strengthening the referee boundary: even a growing exact prefix of Boolean convolution equations and EVERY shallow physical child norm leaves H/J unbounded, with a terminal-inclusive lower bound for arbitrary stopping rules. It supplies no arbitrary-core source payment. NEXT is to extract a full Boolean cancellation that pays one necessary update from SAME unused original influence, retaining old debits and both full terminals; that targets the universal unpaid line directly, whereas another source transfer or finite-prefix normalization lemma cannot close FEI.
'''
save(R/'REPORT.md',report)

save(A/'STATUS.md',f'STATE: A070 stage10 complete: A069 near-Boolean obstruction independently HOLDS; exact depth<2k norms/convolution guard with divergent H/J proved; {res["checks"]} exact checks PASS; FEI OPEN.\nNEXT: A031/A033/A069 use FULL Boolean cancellation for ORIGINAL source payment; A088/A094 review parity-lift/stopped-terminal proof; retain SAME owner, old debits/BOTH terminals.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n2026-10-27 stage10 final: A069 uniform near-Boolean source theorem independently reconstructed unchanged. New parity lift has EXACT convolution/norm prefix through depth2k-1, first failure2k, uniform parity proximity and H/J>2k/(3(1+1/k^2)); full terminals extend obstruction to stopped trees. Pilot190; final{res["checks"]} exact predicates PASS in{res["runtime_seconds"]:.6f}s. Formal receipt{formal_status}. All artifacts local; supervisor mirror/brain adoption and new independent review unverified. No heavy search, other-agent writes or running work stopped. Full Boolean original-source payment remains OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\n2026-10-27 stage10: Disjoint b-bit parity lift preserves spectral entropy and multiplies squared derivative energy by b. If g^2 has no nonconstant coefficients below degree2, the lift has no nonconstant coefficient below2b, so EVERY restriction fixing<2b bits has normEXACTLY1. Applying this to A069 bounded near-Boolean product with b=k,eps1/k,n=2^(2k^4) gives H/J>2k/(3(1+1/k^2)), uniform parity proximity, and EXACT growing Boolean-convolution/shallow-normalization prefixes. First failure at2k has explicit coefficient2eps*m^(n-1)/(Z*(n+1)^(n/2))>0. For ANY inherited-reference stopping tree, positive rate4 invoice+full terminalCE>=Hroot-4Jroot; the entropy analogue holds on normalized shallow trees. Exact finite-depth norms do not fund arbitrary Boolean sources. New corollary pending independent review; A069 uniform near-Boolean theorem independently accepted unchanged.\n')

source_paths=[P/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=OWNER/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
source_paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
source_paths += [supp/'sources'/x for x in ['ERASURE_REDUCTION.md','ROUTE_MAP_CURATED.md']]
source_paths += list((OWNER/'brain_workers/FEI100_20261011/context').glob('*.txt'))
source_paths += [SRC/'REPORT.md',SRC/'DERIVATION.md',SRC/'CLAIMS.json',OWNER/'brain_workers/FEI100_20261011/BOARD.md',OWNER/'brain_workers/FEI100_20261011/claude/B14/STREAM_NOTES.md']
manifest=[]
for p in source_paths:
    raw=p.read_bytes()
    try: raw.decode('utf-8'); enc='utf-8'
    except UnicodeDecodeError: raw.decode('cp1252'); enc='cp1252'
    manifest.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc,'scope':'Full source theorem for A069 DERIVATION/CLAIMS and protocol; otherwise relevant baseline/registry/scope locators, not a claim to reprove every source theorem.'})
js(R/'out/SOURCE_MANIFEST.json',manifest)
assert len(read(A/'STATUS.md').splitlines())==2
assert json.loads(read(R/'PROGRESS.json'))==json.loads(read(R/'PACKET_DELTA.json'))
assert all(statement_hash(c)==c['statement_sha256'] for c in claims)
files=[p for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']
assert all(p.stat().st_size < 20_000_000 for p in files)
js(R/'out/RECEIPTS.json',{'status':'PASS','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Local save/schema/hash/readback only; remote mirror and independent new-proof acceptance unverified.','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'rolling':[{'path':str(p),'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'checks':res['checks'],'formal_status':formal_status})
print(json.dumps({'status':'PASS','run':str(R),'checks':res['checks'],'formal_status':formal_status,'files':len(files)}))
