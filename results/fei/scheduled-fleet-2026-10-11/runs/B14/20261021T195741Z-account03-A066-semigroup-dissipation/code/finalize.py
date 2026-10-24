from pathlib import Path
import json, hashlib, datetime

run=Path(__file__).resolve().parents[1]
agent=run.parent.parent
root=Path('~')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

protocol_path=root/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
result=json.loads((run/'out/CHECK_FULL.json').read_text(encoding='utf-8'))
assert result['status']=='PASS' and result['cases']==5 and result['exact_checks']==32861
pilot=json.loads((run/'out/CHECK_PILOT.json').read_text(encoding='utf-8'))
old=agent/'runs/20261014T090057Z-account05-A066-semigroup-dissipation'
oldclaims=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8'))
if isinstance(oldclaims,dict): oldclaims=oldclaims.get('claims',[oldclaims])
oldref=[{'claim_id':x['claim_id'],'version':x['version'],'use':'incoming accounts reconstructed locally, no external acceptance inferred'} for x in oldclaims]

sources=[protocol_path,root/'AGENTS.md',root/'brain_workers/FEI100_20261011/BOARD.md',root/'brain_workers/FEI100_20261011/claude/B14/STREAM_NOTES.md',old/'REPORT.md',old/'DERIVATION.md',old/'CLAIMS.json',root/'<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md']
for name in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    sources.append(root/'mop_fei100/reports/fei-2026-10-11'/name)
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    sources.append(root/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'/name)
sources.extend((root/'brain_workers/FEI100_20261011/context').glob('*.txt'))
for ag,pattern in [('A094','20261021T155244Z*'),('A096','20261014T094929Z*'),('A097','20261014T050248Z*')]:
    for d in (root/'brain_workers/FEI100_20261011/agents'/ag/'runs').glob(pattern): sources.append(d/'REPORT.md')
dump('out/SOURCE_MANIFEST.json',{'as_of':stamp,'scope':'Local primary evidence and coordination; paper excerpts read at abstracts and threshold Proposition8.6, not a fresh paper audit. No external lookup or novelty assertion.','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources if p.exists()]})
census=[]
for d in sorted(run.parent.iterdir()):
    if d==run: continue
    rec={'run':d.name,'report_present':(d/'REPORT.md').exists(),'files':[p.name for p in d.iterdir() if p.is_file()]}
    if (d/'.final').exists():rec['final_marker']=(d/'.final').read_text(encoding='utf-8')
    census.append(rec)
dump('out/PRIOR_RUN_CENSUS.json',census)

leanfiles=list((run/'out/lean').glob('*/RESULT.json'))
lean_status='Not certified: see saved compiler attempt/source; only width arithmetic was submitted.'
if (run/'out/LEAN_RECEIPT.json').exists():
    ob=json.loads((run/'out/LEAN_RECEIPT.json').read_text(encoding='utf-8'))
    lean_status=f"The core-only width-growth submission returned {ob.get('result',{}).get('status','UNVERIFIED')} after {ob.get('seconds','unknown')} seconds, with no verified target or axiom receipt. No Lean certification is claimed, even for width arithmetic. The entropy curvature remains an analytic proof pending review."

statement=('For every integer m>=2, let b(x)=(-1)^sum_(k=1)^m x_(2k-1)x_(2k), delta=2^(-2m), c(x,j)=b(x)-2*1_(x=0,j=1), q(z)=(-1)^z, and F=c+1_(x=0,j=0)(q-1). '
 'For the DATA j query with both complete physical children, e=Inf_j(F)=delta/2, the incoming A066 accounts satisfy Gdrop=0 and D_R=e, while m+3<=DeltaH/e<=3m+3. '
 'Thus DeltaH<=D_R+K e fails for every dimension-independent K. Nevertheless the SINGLE actual terminal surplus B=4 E I_child-E H_child is at least2m; after booking R=(m+1/2)delta once, L=max(DeltaH-4e-D_R,0) satisfies B-R-L>=(59m+1)/32. '
 'The complete data debit is paid by4e+D_R+L while both complete terminal entropy bills and E R_child=m delta are retained. The exact signed heat boundary is negative and remains in 2DeltaK=ln2 DeltaH-Delta b_empty. '
 'This is a scoped first-query source payment, with no assertion that B is unused after arbitrary earlier histories or on arbitrary cores.')
claim={'claim_id':'A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT','version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite binary cube, Boolean sign output; bit entropy; physical query j','Integer m>=2; specified bent tensor core, one marked edit, one-bit character gate','Bank B has no prior debit and retains both complete actual terminal entropy bills; R is booked once'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A066'],
 'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':[],
 'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_CHECKS_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':['Universal DATA completion DeltaH<=D_R+K Inf_j for a fixed K without a separate source bank'],
 'first_unproved_line':'Arbitrary inherited core/reference: pay the selected positive data/reset profile from the SAME unused original source after all old debits, retaining both terminal bills; universally paid initial references remain absent.',
 'next_consumers':['A070','A088','A094','A096','A097']}
dump('CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A066',
 'gap_id':'C019-C024-INHERITED-DATA-AND-TERMINAL-PAYMENT','attempt_id':'A066-stage7-nonflat-data-single-source-v1',
 'method':'Exact complete spectra, bounded scalar midpoint curvature, actual two-terminal surplus and one carried reserve',
 'mathematical_delta':'Exposes all-width DATA residual >=(m+2)Inf after the release, then pays the specified nonflat query at rate4 with one certified actual-child bank and both full terminals. No universal constant improvement.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_INDEPENDENT_REVIEW_PENDING','mathematical_status':'SCOPED_ANALYTIC_PROOF_FULL_FEI_OPEN',
 'claim_versions_used':oldref,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['DERIVATION.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/FROZEN_BANK_AMENDMENT.json','code/check_data.py','out/CHECK_FULL.json'],
 'next_consumers':['A070','A088','A094','A096','A097'],
 'next_action':'Replace the bent coefficient-count bound by an influence-priced signed profile for one selected DATA query on an arbitrary inherited core, charging only unused original source surplus and retaining full terminal references.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review pending','No arbitrary-core source-bank admission or old-debit hereditary payment','No verified formal certificate for the analytic curvature step','Supervisor copy, canonical adoption and mirrors unverified'],
 'packet_ids':['A066']}
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)

report=f'''# A066 stage 7: one nonflat data query paid from one actual source

## exact target, quantifiers, hypotheses and units

Continue stage6's first unpaid DATA step with the SAME G,R, retaining both whole physical terminal functions. DERIVATION.md specifies an actual Boolean family for every m>=2: a 2m-bit quadratic bent tensor, a rare two-bit AND sign at its marked point, and a nonflat incoming core c. Entropy is in bits; K is noise-semigroup area in nats. The selected data coordinate has e=delta/2, delta=2^(-2m). No universal FEI result or novelty for bad-coordinate examples is claimed.

## sources actually read, revisions and theorem locators

Full execution protocol 2026-10-11-execution-v2; current BOARD and B14 lead v2 (11Oct23:25UTC); own stage6 REPORT/DERIVATION/CLAIMS and rolling files. Read the campaign indices, plan A066 acceptance contract, supplementary campaign/claim/obstruction seeds and mapping; threshold38pp Proposition8.6 gives the background complete shared-selector identity. Both percolation and both threshold abstract/version contexts were inspected; no percolation theorem is used here. A094's latest same-source signed-profile REPORT, A096's complete-terminal transport REPORT and A097's source-bank REPORT provide coordination only, not new accepted dependencies. Source sizes/hashes are in out/SOURCE_MANIFEST.json. Math-brain recall identified earlier bent bad-coordinate warnings; the local obstruction is an account-specific specialization, not a claimed new general phenomenon. No source claim is accepted solely on a recall card.

The prior-run census finds six substantive reports and ten later marker-only run directories, preserving their exact markers in out/PRIOR_RUN_CENSUS.json. This stage resumes the last actual derivation rather than treating all sixteen stage labels as new mathematics. Your current23Oct14:49UTC campaign endpoint supersedes the older21Oct endpoint in static campaign files; no schedule is changed.

## complete derivation or exact first unsupported line

Write h(u)=-u^2 log2(u^2), E(v)=sum_T h(hat b(T)-v). Complete root and child spectra give DeltaH=E(3delta/2)-[E(delta)+E(2delta)]/2+delta(m+3/2). All coefficients in this scalar interval are nonzero. The explicit bound |E''|<=4m/delta and the midpoint integral remainder give m+3<=DeltaH/e<=3m+3 for EVERY m>=2. The SAME incoming reserve releases only D_R=e and Gdrop=0, so (DeltaH-D_R)/e>=m+2. Paying data solely by this release and a universal coordinate charge is impossible; this does not refute choosing another coordinate or FEI.

The actual source B=4 E I_child-E H_child is computed AFTER reserving both complete terminal entropy bills. Maximum entropy on the N actual core atoms proves B>=2m. Book R=(m+1/2)delta ONCE. The residual L=max(DeltaH-4e-D_R,0) obeys L<=delta(3m/2-1) and B-R-L>=(59m+1)/32. Thus4e, released D_R, and at most L from the unused B-R pay this specific data step, leaving the SAME child reserve m delta and the complementary source bank. This supplies the requested nonflat one-query payment, with zero old debit and an explicitly proved bank; it is not an arbitrary-history closure.

For q_t(S)=hat g(S)^2 exp(-2t|S|), J_g=sum_(S nonempty)|S|q_t(S)ln(1/p_S), 2K=H_nat-b_empty exactly. The finite sum is bounded at zero and <=e^(-2t)J_g(0) at infinity. The corrected raw entropy has derivative-2J, and b_empty<=I pays the scalar boundary. A universal2K<=A I would imply FEI at(A+1)/ln2. For this SAME physical query the signed boundary Delta b_empty is negative; it is retained in2DeltaK=ln2 DeltaH-Delta b_empty. The data obstruction survives that boundary. The positive entropy payment is not promoted to a separate absolute-boundary influence payment.

Rung: analytic author proof with exact finite certificates, pending independent reconstruction. {lean_status}

FIRST UNSUPPORTED UNIVERSAL LINE: obtain the analogous selected signed-profile and complete reference/reset payment for an arbitrary inherited nonflat core from the SAME genuinely unused source after old debits, while retaining both complete terminals. The bent atom-count source certificate is not available for arbitrary cores. Initial universally influence-priced complete references remain unpaid. Full FEI is OPEN.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json predates the search: pilot m=2; full m=2..6, five actual functions, no symmetry reduction, no automatic dimension escalation, maximum dimension14. Integer Walsh transforms are checked against the analytic coefficients atom by atom; separately enumerated physical edges verify influence. Both actual terminal spectra, their entropy, the zero G drop, carried R release, signed heat boundary and source-bank ownership are checked. Logs have rigorous32-term range-reduced atanh enclosures with explicit geometric tail, then saved intervals round outward to2^-70.

Commands from A066: python -X utf8 runs/{run.name}/code/check_data.py pilot, and the same helper with full. Pilot PASS:116 checks in{pilot['elapsed_seconds']:.6f}s. Original full PASS:32836 checks in1.956205s. After deriving the bank certificate, out/FROZEN_BANK_AMENDMENT.json adds25 ownership checks on the SAME five cases without changing dimension or precision. Final full PASS:{result['exact_checks']} checks in{result['elapsed_seconds']:.6f}s. These totals are successive versions, not additive samples. Full output, original pre-bank output and pilot are saved. The all-m theorem follows from the written curvature/source proof; five exact cases alone do not prove it.

Memory estimate80MB, actual peak unmeasured;55s helper runtime cap; no heavy/GPU/background job. Fresh memok before the core-only formal attempt returned physical12.9GB and commit19.0GB free. Full Mathlib is excluded by the1.5GB cap (wrapper documents about4GB); the source submitted only the natural-width consequence and cannot certify the entropy bound.

## proof dependencies and changed downstream conclusions

New joint claim is self-contained: tensor Walsh spectrum, scalar derivatives, midpoint integral remainder, finite-alphabet entropy maximum and direct physical edge counts. Incoming stage6 accounts are reconstructed, not silently renewed. Earlier bad-coordinate work is acknowledged; no universal good-coordinate premise is refuted. No prior theorem is superseded and no new independent acceptance is claimed. This is a narrow continuation of the existing pending ledger, not another broad FEI candidate. Consumers can now reject release-only DATA completion and use the explicitly certified two-child bank on this exact fixture. Universal FEI constant improvement: zero.

## one next mathematical action and independent reviewer

Replace the bent coefficient-count estimate by an influence-controlled signed profile on an arbitrary inherited core through one selected DATA query, keeping both complete terminal references and every previous bank debit. A070 or A088 should independently reconstruct the complete spectra, midpoint sign and one-bank allocation; A094 should challenge the source/terminal ownership. A096/A097 are downstream consumers. These are artifact handoffs, not messages sent or reviews received.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, DERIVATION.md, frozen specs, checker, outputs, source/census records and local formal-attempt evidence are saved in this assigned run. STATUS has two lines; WORKLOG and LEARNED are updated. code/finalize.py checks exact protocol field sets, statement hash, delta equality and20MB ceilings, and writes byte/SHA256 receipts. Local durability only; supervisor copy, remote mirror, canonical adoption and independent review are unverified. Only own research outputs are mutated; no git, mail, trading access, brain-memory write or other-agent-folder write. The mandated wake/checklist infrastructure runs are separate from research-output ownership.

## Universal bridge

C019 stopping payment and C024 history transfer advance by one actual nonflat DATA query: its released reserve is proved insufficient at every fixed local rate, but the entire debit is paid at physical rate4 from one explicitly certified original two-child surplus, retaining BOTH full terminals and the same unspent reserve. The universal improvement is zero. Arbitrary inherited-core signed-profile payment, admission after old debits and cheap universal source references remain open. NEXT attacks exactly that missing owner and avoids repeating automatic no-reset transfer or another isolated root entropy bound.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(agent/'STATUS.md').write_text('STATE: A066 stage7 saved: all-width nonflat DATA debit/release obstruction and same actual-child-bank rate4 payment;32861 exact checks PASS; independent review pending;FEI OPEN.\nNEXT: A070/A088/A094 review; pay selected arbitrary-core signed DATA/reference profile from SAME unused original source after old debits, retaining both full terminal references.\n',encoding='utf-8',newline='\n')
lesson='A066 stage7: For quadratic bent b on2m bits, c=b-2*1_(x=0,j=1), F=c+1_(x=0,j=0)((-1)^z-1), m>=2, actual DATA j has e=delta/2 and same Gdrop0,D_R=e. Complete physical entropy debit satisfies m+3<=DeltaH/e<=3m+3 by |E_second|<=4m/delta and midpoint remainder. Hence release-only plus constant-query completion fails, not FEI or selected-coordinate existence. The actual full-terminal surplus B=4 E Ichild-E Hchild>=2m books R=(m+1/2)delta once and pays L=max(DeltaH-5e,0), with B-R-L>=(59m+1)/32. Both terminal entropies and inherited Rchild=m delta remain; no prior debit is allowed in this supplied source. Delta empty-boundary<0, so true heat decrement also keeps the obstruction. Arbitrary-core/old-debit source admission remains open; no generic novelty for bent bad-coordinate examples.'
with (agent/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+stamp+' '+lesson+'\n')
with (agent/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+stamp+' stage7: Resumed stage6 after confirming ten later marker-only runs. Derived complete nonflat DATA fixture, all-m curvature and one original two-terminal-bank payment. Pilot116 and final32861 exact predicates PASS; five widths, 2.294235s final. Added25 bank checks to same frozen cases, preserved pre-bank output. Full FEI remains OPEN; new narrow proof pending review. No shared research writes or jobs left intentionally running.\n')

req=protocol['required_per_run']
assert set(claim)==set(req['claim_fields'])
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
expected={x.split(' (')[0] for x in req['progress_fields']}
assert set(progress)==expected,(set(progress)^expected)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
for heading in req['report_fields']: assert '## '+heading in report
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert sha(run/'DERIVATION.md')
assert all(p.stat().st_size<20_000_000 for p in run.rglob('*') if p.is_file())
dump('out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_field_count':len(claim),'progress_field_count':len(progress),'report_fields':len(req['report_fields']),'compatibility_equal':True,'claim_statement_hash_verified':True,'full_fei':'OPEN'})
paths=[p for p in run.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[agent/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
dump('out/PERSISTENCE_RECEIPTS.json',{'created_at':stamp,'scope':'Local only; no mirror or independent-review assertion','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths]})
print(json.dumps({'status':'PASS','files':len(paths),'checks':result['exact_checks'],'claim':claim['claim_id'],'full_fei':'OPEN'}))
