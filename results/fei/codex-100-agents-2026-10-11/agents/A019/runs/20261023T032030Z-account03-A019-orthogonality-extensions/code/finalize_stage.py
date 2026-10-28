import copy, hashlib, json
from pathlib import Path
from datetime import datetime, timezone

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
ROOT=A.parents[1]
OLD=A/'runs/20261022T221313Z-account03-A019-orthogonality-extensions'
REVIEW=ROOT/'agents/A018/runs/20261023T022754Z-account03-A018-shared-data-collision-law'
PROTOCOL=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p): return p.read_text(encoding='utf-8-sig')
def js(p): return json.loads(read(p))
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
protocol=js(PROTOCOL)
cert=js(R/'out/CERTIFICATE.json')
reviewcert=js(R/'out/REVIEW_CERTIFICATE.json')
direct=js(R/'out/DIRECT_CERTIFICATE.json')
lean=js(R/'out/LEAN_RESULT.json')
assert all(x['status']=='PASS' for x in (cert,reviewcert,direct))
incoming=js(REVIEW/'CLAIMS.json')
if isinstance(incoming,dict): incoming=incoming['claims']
radial=copy.deepcopy(next(c for c in incoming if c['claim_id']=='A018-UNEQUAL-MEAN-RADIAL-LEDGER'))
original_hash=radial['statement_sha256']
assert original_hash=='cb9b7679c68363fc8daaeb7f6d6bee5d07ee9a2cc5d1d41cf5bf85da4e6785ea'
radial['review_records'].append({'reviewer':'A019','verdict':'HOLDS_AT_ORIGINAL_STATED_SCOPE','independent':True,'substantive_repair':False,'source':str(R/'REPORT.md'),'certificate':'out/REVIEW_CERTIFICATE.json','method':'Independent KL-chain and radial-derivative reconstruction plus 720 actual Boolean/reference cases; no source checker imported.'})
radial['status']='INDEPENDENT_A019_HOLDS_AT_ORIGINAL_SCOPE_SHARED_ADOPTION_PENDING'
statement=('For every integer k>=2, let e=2^-k, E=1[v=0] on k private bits, h0=u, h1=(1-E)u+E, and Qb=(P_hb+delta_empty)/2. Use the exact mean-1/2 two-bit mask s with uniform squared spectrum, the original q-conditional lift of (Q0+Q1)/2, and activation references with data marginal (Qcore tensor P_s+delta_empty)/2 and actual x-frequency conditionals. Let B=(4I(h0)-c0+4I(h1)-c1)/4, cb=CE(P_hb,Qb), and let Tq be the FULL first q-query CE decrement less 4 Inf_q(F). For every old debit 0<=U<=1/8, expose any one v bit on the q1 terminal, retain q0, give both core children the SAME frequency marginal Rcore of the ORIGINAL Q1, and lift both child activation references by their own actual x-frequency conditionals over (Rcore tensor P_s+delta_empty)/2. If Tv is the FULL q1 CE decrement to these two prescribed children, including inherited-to-prescribed conditional conversion, then Tv<77/64 and B-U-max(Tq,0)-max(Tv,0)/2>3/128. All CE costs are finite and in bits; all three final terminal references and the original debits are retained. This is a scoped continuation, not a uniform FEI proof.')
claim={'claim_id':'A019-INHERITED-V-QUERY-SAME-BANK','version':1,'exact_statement':statement,'hypotheses':['Explicit actual Boolean family and prescribed inherited references in exact_statement.','Mask s is +1 except at one of its four input points, where it is -1.','A018-UNEQUAL-MEAN-RADIAL-LEDGER@1 full-query specialization; no resetting incoming reference or old bank.'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A019'],'proof_source':[str(R/'REPORT.md'),str(R/'out/DERIVATION.md')],'proof_dependencies':[{'claim_id':radial['claim_id'],'version':radial['version'],'statement_sha256':original_hash,'acceptance':'A019 independent HOLDS at original scope in this run'},{'claim_id':'A019-FORCED-BIASED-EMPTY-ROW-DEBT','version':1,'acceptance':'A018 independent HOLDS; used only original bank and family, not Lambda-only debit as full debit'}],'review_records':[{'reviewer':'A019','independent':False,'verdict':'AUTHOR_CHECKED','certificates':['out/CERTIFICATE.json','out/DIRECT_CERTIFICATE.json'],'full_entropy_lean_status':lean['status']}],'status':'AUTHOR_CHECKED_PROOF; INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'No unsupported line in the scoped theorem. Universal extension: another interacting exposure must be paid from these inherited marginal references and the already diminished bank without renewing the original KL<=1/2 assumption.','next_consumers':['A018','A020','A092','A094','B04 lead']}
claims={'claims':[radial,claim]}
claim['proof_dependencies'].append({'claim_id':'A019-OWNED-EMPTY-REFERENCE-PAYMENT','version':1,'acceptance':'A018 independent HOLDS; original half-core bank fixture only'})
save(R/'CLAIMS.json',claims)
sources=[PROTOCOL,ROOT/'BOARD.md',ROOT/'claude/B04/STREAM_NOTES.md',OLD/'REPORT.md',OLD/'CLAIMS.json',REVIEW/'REPORT.md',REVIEW/'CLAIMS.json',A/'runs/20261014T055119Z-account05-A019-orthogonality-extensions/code/check_exposure.py']
save(R/'out/SOURCE_RECEIPTS.json',{'at':now,'receipts':[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources],'reading_scope':'Board and stream notes read this stage; proof sources and exact statements read in full. Earlier campaign protocol/papers retained from preceding stage; no claim of fresh full-paper reread. Shared sources never modified.'})
next_action='Expose a second interacting data coordinate with the exact surviving common marginal references and old debits retained; derive a cumulative cost invariant rather than renew the original KL<=1/2 price.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B04','packet_id':'A019','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A019-stage18-inherited-data-query','method':'Independent radial-ledger review, all-k entropy curvature bound, exact inherited complete-reference query and same-bank continuation','mathematical_delta':'Pays one actual interacting v query after the FULL unequal-mean first query; retains all terminal references and debits and leaves >3/128 of original bank, uniformly k>=2. Independent HOLDS review of A018 radial ledger. Full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_CHECKED_PROOF; NEW_THEOREM_INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':radial['claim_id'],'version':radial['version'],'statement_sha256':original_hash,'review':'independent HOLDS in this run'},{'claim_id':'A019-FORCED-BIASED-EMPTY-ROW-DEBT','version':1,'review':'A018 independent HOLDS, read source review record'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'new scoped theorem'},{'claim_id':radial['claim_id'],'version':radial['version'],'change':'independent review only; exact statement/hash unchanged'}],'source_artifacts':['REPORT.md','CLAIMS.json','out/DERIVATION.md','out/FROZEN_SPEC.json','out/REVIEW_SPEC.json','out/DIRECT_SPEC.json','out/PILOT.json','out/CERTIFICATE.json','out/REVIEW_CERTIFICATE.json','out/DIRECT_CERTIFICATE.json','out/LEAN_RESULT.json','out/SOURCE_RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['No arbitrary-core cumulative inherited-reference bank invariant.','New theorem independent review and supervisor mirror copy pending.','Lean compiler admission held; full analytic proof not formalized.','Brain self-care degraded/unverified: stale owner-model and state-of-mind notes; personal-context inferences not used.'],'packet_ids':['A019']}
save(R/'PROGRESS.json',progress)
(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
derivation=read(R/'out/DERIVATION.md')
report=f'''# A019 stage 18: one interacting query from the same original account

## exact target, quantifiers, hypotheses and units

Prove the scoped claim A019-INHERITED-V-QUERY-SAME-BANK@1 for every integer k>=2 and every choice of the next v coordinate. Entropies, CE and KL use base-two logarithms; CE(P,Q)=-sum P log2 Q and P is the squared Fourier law of an actual Boolean function. The theorem retains the original bank, the old debit, the FULL first-query bill, both newly exposed children and the unchanged opposite terminal. The remaining bank is strictly greater than 3/128. Full FEI remains OPEN; no new neighboring-disagreement lower bound is claimed.

## sources actually read, revisions and theorem locators

Read BOARD.md (snapshot 2026-10-23 03:14 UTC), B04 STREAM_NOTES.md v2, own STATUS and preceding stage derivation/report, and A018's 20261023T022754Z report and complete CLAIMS.json. Protocol revision {protocol['revision']} governs the schema. A018-UNEQUAL-MEAN-RADIAL-LEDGER@1 has unchanged statement hash `{original_hash}`. Exact source byte receipts are in out/SOURCE_RECEIPTS.json. The previous stage's >3/4 remainder paid Lambda only; A018's >5/8 remainder pays the FULL first q query. The present result starts from the latter. Previously read campaign and paper context supplies conventions, not a new external theorem assumption. The bent-splice falsifier remains imported: small disagreement alone cannot justify a vanishing collision-debt bound. The old constant-correlation closure is not presented as new.

## complete derivation or exact first unsupported line

{derivation}

For completeness the activation profile used above is Psi(mu)=eta((1+mu)^2/4)+eta((1-mu)^2/4)+1-mu^2-eta(mu^2)/2, with phi(b)=Psi(b/2). Direct differentiation gives Psi''(mu)=log2(mu^2/(1-mu^2)); hence phi is concave throughout the required b in [0,1/2], with endpoint continuity. This supplies the curvature step for the entire infinite k range. The endpoint strict sign uses the exact prime-log interval certificate in the checker, not floating point. The rational arithmetic identity 5/8-77/128=3/128 is exact. The original v influence is e/2 in the q1 terminal; it is left unspent in this conservative bound.

Independent review of A018 at its original full scope: write p=mr, z=ta, nu=beta^2/r (nu=1 if r=0), and A(p,z)=[p log2(p/z)+(1+p)log2((1+z)/(1+p))]/2. Splitting the core-label KL into empty and remaining rows, then applying the log-sum identity to the plus activation branch, gives exactly Lambda=A(p,z)-A(nu*p,nu*z)-[(1-m)E0+Erest+Kplus]/2. Each subtracted quantity is a KL cost and nonnegative. For a(kappa)=A(kappa*p,kappa*z), w=p(1+kappa*z)/(z(1+kappa*p)), direct differentiation gives a'=[p ln(w)+(z-p)/(1+kappa*z)]/(2 ln2)=p[ln(w)+1/w-1]/(2 ln2)>=0 and a''=-(p-z)^2/[2 ln2(1+kappa*p)(1+kappa*z)^2]<=0. Thus G=a(1)-a(nu)>=0. When p<=z, integration gives G=(1-nu)/(2 ln2) integral_p^z (v-p)/[v(1+v)(1+nu*v)] dv, bounded by log2((1+z)/(1+nu*z))/2 and then by (1-nu)log2(1+z)/2. Concavity also gives G<=(1-nu)[p log2(p/z)+(z-p)/ln2]/2 for positive p,z. Continuous zero cases use finite incoming CE support; t=0 forces m=0. This reconstructs the original statement without repairs. The 720 exact actual-Boolean/reference tests independently reconstruct the full activation law as an additional check; they do not prove arbitrary dimension by enumeration.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede every search in out/FROZEN_SPEC.json, REVIEW_SPEC.json and DIRECT_SPEC.json. Pilot k=2: 701 assertions, PASS. Main k=1..8: {cert['checks']} assertions, PASS, {cert['seconds']:.3f} seconds; k=1 is diagnostic, outside the theorem. Independent A018 review: {reviewcert['cases']} actual Boolean/reference cases, {reviewcert['checks']} assertions, PASS, {reviewcert['seconds']:.3f} seconds, including zero and unit boundary parameters. Direct literal character sums for k=2,3: {direct['checks']} assertions, PASS, {direct['seconds']:.3f} seconds. Total substantive assertions {cert['checks']+reviewcert['checks']+direct['checks']} excluding the pilot. Exact Fraction coefficients and integer Walsh transforms are used; logarithmic signs have rational atanh-series bounds. No floating-point sign is accepted. Parameters were not raised automatically; estimated memory 100 MB and per-checker cap 60 seconds, so the >300 MB admission condition was not triggered.

Command: `python -B -X utf8 runs/{R.name}/code/run_checks.py`. Source arithmetic helper normalized-text SHA256 is `{cert['source_arithmetic_normalized_sha256']}`; only elementary arithmetic definitions are reused, with actual references and the reviewed law reconstructed independently. No A018 checker was imported. The direct implementation replaces the Walsh transform by literal character summation. The Lean side-check command was `python -B -X utf8 runs/{R.name}/code/check_lean.py`; its resource admission was held before compiler launch: `{lean.get('blocker','see LEAN_RESULT.json')}`. No Lean verification is claimed for the entropy proof or arithmetic side file.

## proof dependencies and changed downstream conclusions

The acyclic chain is earlier A019 bank/family facts -> A018 full radial ledger and full first query -> this new inherited-v continuation. The review of the existing A018 version supplies no substantive repair; the imported statement and hash remain unchanged. New theorem independence is pending. The exact conversion gains K_b are positive parts of the decrement: deleting them when changing the terminal conditional would undercharge the query. This is the main reusable ledger correction. The old >3/4 Lambda-only remainder must never be substituted for the >5/8 full-query remainder. No priority or literature-novelty claim is made.

## one next mathematical action and independent reviewer

{next_action} A018 is the proposed independent reviewer of the new claim; A020/A092/A094 can consume the complete inherited-reference fixture. No messages were sent and no shared registry was changed. The exact first unsupported universal line is recorded in the theorem and CLAIMS.json: iteration on arbitrary remaining children with their carried marginals has no proved cumulative payment invariant.

## actual persistence receipts or precise save blocker

All four protocol files and code/out artifacts are saved locally in this run. PROGRESS.json and PACKET_DELTA.json are byte-identical; source and local artifact hashes are recorded in out/SOURCE_RECEIPTS.json and out/PERSISTENCE_RECEIPTS.json. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated only within A019. Remote copying, independent acceptance of the new theorem and downstream adoption are not verified. Brain self-care remains degraded/unverified because owner-model and state-of-mind notes are stale; personal-context conclusions remain affected and were not mathematical premises. No background job remains, and nothing was stopped. The stale signed-contract warning affects irreversible work; this stage performs only authorized reversible local research writes.

## Universal bridge

This stage moves C024 history transfer toward C019 stopping-tree payment by carrying one genuinely interacting data query through the original complete references after the full unequal-mean first-query bill, leaving >3/128 of the same bank uniformly over an unbounded family. The whole-set or arbitrary-core cumulative invariant remains open: inherited children cannot renew the original KL<=1/2 budget. The shortest next route is a second interacting exposure with these very marginals and every old debit retained, because it tests the missing iteration mechanism needed for a universal stopping tree rather than producing another disconnected class estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Stage18 scoped inherited-v theorem author/exact checked; same-bank remainder >3/128 for all k>=2; A018 radial ledger independently HOLDS; full FEI OPEN.\nNEXT: Second interacting exposure with inherited marginals and old debits retained; A018 review of new theorem pending.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} stage18: Read current board/lead and A018 full ledger; independently reconstructed its original scope without repair. Paid one actual v query from the same original bank after FULL q cost, uniform k>=2, leaving >3/128. Exact 129718 substantive checks and 701 pilot checks passed. Positive conditional-conversion charges retained. Lean admission held; no compiler started. Next: second inherited interacting query; new theorem review pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage18 durable fact: for the one-balanced sparse point-splice fixture, original contaminated references and exact mean-1/2 mask, one v query after the complete first q payment costs less than 77/128 at original reach and leaves >3/128 of the original bank, for every k>=2. Both core children use the same folded ORIGINAL Qk. Replacing inherited activation conditionals by actual child conditionals creates a nonnegative conversion gain that INCREASES the query CE decrement; it cannot be deleted as a free rebate. The old >3/4 remainder paid Lambda only; >5/8 is the full first-query remainder. The second interacting exposure cannot reset references or renew KL<=1/2. Source: current stage REPORT and A018 radial ledger independently reconstructed.\n')
# Verify schema and all current-stage JSON; exact statement hash is preserved for imported claim.
required=protocol['required_per_run']
assert set(progress)=={('packet_ids' if x.startswith('packet_ids') else x) for x in required['progress_fields']}
for c in claims['claims']: assert set(c)==set(required['claim_fields'])
assert radial['statement_sha256']==original_hash
assert hashlib.sha256(statement.encode('utf-8')).hexdigest()==claim['statement_sha256']
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
for field in required['report_fields']: assert '## '+field in report
assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C024')
for p in R.rglob('*.json'): js(p)
for p in R.rglob('*'):
 if p.is_file(): assert p.stat().st_size<20_000_000, str(p)
receipts={'at':now,'status':'LOCAL_SCHEMA_AND_PERSISTENCE_CHECKED','remote_mirror':'UNVERIFIED','new_theorem_independent_review':'PENDING','full_fei':'OPEN','files':[{'path':str(p.relative_to(R)),'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']}
save(R/'out/PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','local_files':len(receipts['files']),'new_claim':claim['claim_id'],'new_statement_sha256':claim['statement_sha256'],'reviewed_claim':radial['claim_id'],'substantive_assertions':cert['checks']+reviewcert['checks']+direct['checks'],'full_fei':'OPEN','remote_mirror':'UNVERIFIED'}))
