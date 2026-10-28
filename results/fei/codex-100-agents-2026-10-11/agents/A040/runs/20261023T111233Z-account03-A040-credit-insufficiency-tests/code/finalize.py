"""Persist the research handoff; no research search or shared-tree mutation."""
from pathlib import Path
import json, hashlib, datetime, copy

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
B=A.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p): return Path(p).read_text(encoding='utf-8')
def obj(p): return json.loads(read(p))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x): Path(p).write_text(x,encoding='utf-8',newline='\n')
def dump(p,x): save(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
protocol=obj(P/'EXECUTION_PROTOCOL.json')
main=obj(R/'out/CHECK.json'); audit=obj(R/'out/AUDIT.json'); pilot=obj(R/'out/PILOT.json')
assert (main['status'],main['checks'],audit['status'],audit['checks'],audit['exact_prime_log_equalities'])==('PASS',282,'PASS',1442,37)
assert len(main['physical_policies'])==4 and len(main['grouped'])==18
assert pilot['status']=='PASS' and pilot['checks']==59
a047=B/'agents/A047/runs/20261023T055836Z-account03-A047-boundary-search'
a036=B/'agents/A036/runs/20261023T050401Z-account03-A036-reference-law-divergence'
a037=B/'agents/A037/runs/20261023T055409Z-account03-A037-conditional-credit-ledger'
a050=B/'agents/A050/runs/20261023T042019Z-account03-A050-repair-with-scope'
foreign=next(c for c in obj(a047/'CLAIMS.json') if c['claim_id']=='A047-SAME-SUPPORT-BOOLEAN-REFRESH-OBSTRUCTION')
assert hashlib.sha256(foreign['exact_statement'].encode('utf-8')).hexdigest()==foreign['statement_sha256']=='c51b590eea699ca82ad2ec3cb3df74228e3e3e6ed6ecd9d9419d58ff6781c5df'
review='''# Scoped independent reconstruction of A047 v1

The unchanged statement is pinned in CLAIMS.json by its source UTF-8 digest. This review accepts ONLY the pure-core all-alpha analytic obstruction and its alpha=1/6 core/activated formulas. It does not review A047's enumeration or minimality clauses, so it is not acceptance of the entire bundled claim.

For the actual three-bit truth table (1,-1,-1,1,-1,1,1,1), direct character sums give full positive support, empty/full masses1/16,9/16 and six other masses1/16. Reconstructing the actual coherent physical query and each reference's own outcome normalization gives core sigma=log2[4(2+alpha)/((2-alpha)^3(1+2alpha))]/8. Its logarithm is positive for0<alpha<1 because numerator minus denominator equals alpha^2(18-11alpha+2alpha^2)>0. At1/6 this is log2(1404/1331)/8.

For BOTH activation signs the actual reference outcomes are101/195,94/195. The mean reset is log2(K)/32, where K=(155/156)^13*(59/60)^5*(13/12)^10 /[(4/3)^2*(1-(7/195)^2)^16]. The audit checks K>1 as an exact rational integer comparison and checks the KL formula by prime-factor coefficient vectors, without importing either A047's or the main helper's code. This independently supports the analytic obstruction; no source statement or proof was repaired. See code/audit.py and out/AUDIT.json. Its 1,442 assertions/37 identities also cover the NEW rare-query family, so these totals are not all attributed to this review.
'''
save(R/'REVIEW_A047.md',review)
new_statement=(
 'For every integer r>=3 let d=2^-r, a=e0+e1, v_r(j,z,w)=(-1)^z(1-2*1{w=0 or (j=1 and w=a)}), and G_epsilon=epsilon at x0 and v_r at x1. '
 'All entropies and divergences are in bits. Use the actual same-support balanced-core reference q_alpha=(1-alpha)p+alpha delta_full, lifted to G, and the actual coherent j-query kernel with own reference outcome normalizers; reset both children to the SAME-alpha remaining-full rule. '
 'The reference outcomes are 1/2-3alpha/20,1/2+3alpha/20. Its signed physical-mean new-minus-inherited reset bill sigma_r exceeds kappa_alpha=-log2(1-9alpha^2/100)/2. '
 'At alpha=1/6, sigma_r/Inf_j(G)>2^r/300, and sigma_r=kappa+c*4^-r+O(16^-r), c=18-5log2(10)>0. '
 'The five specified actual credits (conditional erasure KL E, child-spectral Jensen-Shannon J, posterior MI P, other-influence Bernoulli-JS sum Gamma, spectral total correlation TC) are each strictly positive for all r>=3, with respective asymptotics E~9r*4^-r, J~(1+c)*2^-r/2, P~r*2^-r/2, Gamma~(1-1.5log2(1.5))*r*2^-r, TC~1.5r^2*2^-r. '
 'Each divided by sigma_r or by H(G) tends to zero, while H(G)/I(G) tends to2. '
 'For every r>=8 the original priority root F=chi_a at x0, v_r at x=b=1, and +1 otherwise, equipped from admission with its normalized alpha0=1/8 correlated reference lift, pays the actual alpha1=1/6 first resets on BOTH a outcomes and the same-alpha rare-j second resets on BOTH children, retaining b0 and an old booking omega<=1/4. '
 'Its complete signed final margin is at least13/8; the second reset bill divided by original Inf_j(F) still exceeds2^r/300. '
 'Thus arbitrary-Boolean same-support full-spike reset cost admits no uniform bound by the current query influence or any fixed linear combination of these five credits; no arbitrary initial-source price or universal FEI theorem is asserted.'
)
cid='A040-RARE-QUERY-POSTERIOR-CREDIT-INSUFFICIENCY'
new={
 'claim_id':cid,'version':1,'exact_statement':new_statement,
 'hypotheses':['uniform Boolean cube; Walsh squared spectrum; bits','r>=3, private points have equal parity; all outcome/source atoms retained','fixed 0<alpha<1 for positivity; alpha=1/6 for explicit ratio','same support, same alpha at the rare query; own reference normalizers','full original priority-source payment only for r>=8, initial alpha0=1/8, old booking in [0,1/4]; no free source conversion'],
 'statement_sha256':hashlib.sha256(new_statement.encode('utf-8')).hexdigest(),
 'contributors':['A040'],'proof_source':str(R/'PROOF.md'),
 'proof_dependencies':['Self-contained Boolean spectra, physical edges, compensated KL factorization and convexity derived in PROOF.md; exact local reconstruction code/check.py and code/audit.py','A047-SAME-SUPPORT-BOOLEAN-REFRESH-OBSTRUCTION@1 is motivational context, not a logical premise for this self-contained family'],
 'review_records':[{'reviewer':'A040','time_utc':now,'disposition':'AUTHOR_CHECKED_WITH_SEPARATE_IMPLEMENTATION; NOT_EXTERNAL_REVIEW','method':'282 main rational-interval checks; independent direct-character/prime-log audit 1442 checks including37 identities','source':str(R/'out/AUDIT.json'),'substantive_repair':False}],
 'status':'PROVED_AUTHOR_CHECKED_EXTERNAL_REVIEW_PENDING','supersedes':[],
 'refutes':['Unregistered universal inequality sigma_i<=K_alpha Inf_i for arbitrary Boolean cores under this same-support full-spike rule','Any dimension-independent payment of this sigma by a fixed linear combination of the five explicitly defined credits'],
 'first_unproved_line':'No transferable original-source or spectral-likelihood payment bound for arbitrary Boolean cores and arbitrary repeated physical histories; full FEI remains open.',
 'next_consumers':['A048','A047','A050','A036','A037','B08','B20']}
scoped=copy.deepcopy(foreign)
scoped['review_records'].append({'reviewer':'A040','time_utc':now,'disposition':'INDEPENDENT_ANALYTIC_CLAUSES_HOLD; BUNDLED_CENSUS_NOT_REVIEWED','method':'Direct character sums, normalized complete child laws, rational prime-log identities and all-alpha polynomial sign; no source-code import','source':str(R/'REVIEW_A047.md'),'substantive_repair':False})
scoped['status']='SCOPED_REVIEW_ONLY_NOT_FULL_CLAIM_ACCEPTANCE'
dump(R/'CLAIMS.json',[scoped,new])
sources=[P/'EXECUTION_PROTOCOL.json',B/'BOARD.md',B/'claude/B08/STREAM_NOTES.md',a036/'PROOF.md',a036/'CLAIMS.json',a037/'PROOF.md',a047/'PROOF.md',a047/'CLAIMS.json',a050/'REPORT.md']
dump(R/'out/SOURCE_RECEIPTS.json',{'time_utc':now,'scope':'Pinned bytes of named read-only sources; mutable board snapshot is not a timeless claim revision. Earlier protocol/campaign/paper baseline retained from previous stages, not independently rereviewed in full this stage.','sources':[{'path':str(p),'sha256':sha(p)} for p in sources]})
next_action='Derive an amortized original-source spectral-likelihood payment inequality that can absorb the nonvanishing outcome KL at arbitrarily rare physical queries; first test one further actual rare query from this diminished owner with all old bills retained. Request A048 independent reconstruction; A047 checks the original-source ledger.'
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B08','packet_id':'A040','gap_id':'G-R-MISMATCH',
 'attempt_id':'A040-stage9-rare-physical-query-outcome-KL',
 'method':'Analytic all-r Boolean family after consuming existing finite obstruction; rational interval main check and independent direct-character prime-log reconstruction; complete original-source payment ledger',
 'mathematical_delta':new_statement,
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; external mirror and downstream receipt not verified',
 'mathematical_status':'QUANTITATIVE_LOCAL_PAYMENT_OBSTRUCTION_PROVED; SPECIAL_ORIGINAL_SOURCE_PAYMENT_PROVED; FULL_FEI_OPEN',
 'claim_versions_used':['A036-NONPOSITIVE-COHERENT-SAME-PROFILE@1 (scope boundary only)','A047-SAME-SUPPORT-BOOLEAN-REFRESH-OBSTRUCTION@1 (analytic clauses independently reconstructed; census not reviewed)'],
 'claims_created_or_changed':[cid+'@1','A047-SAME-SUPPORT-BOOLEAN-REFRESH-OBSTRUCTION@1 (scoped review record; statement unchanged)'],
 'source_artifacts':[str(p) for p in sources]+[str(R/'PROOF.md'),str(R/'REVIEW_A047.md'),str(R/'out/CHECK.json'),str(R/'out/AUDIT.json')],
 'next_consumers':['A048','A047','A050','B08','B20'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI lacks arbitrary Boolean source pricing and repeated-history amortization; this is an obstruction, not an FEI counterexample.','External independent acceptance and supervisor mirror are pending; local audit is a separate implementation by the author.','Brain self-care degraded/unverified: wake rendering/attachment integrity timed out under a shared write lock; owner-model97.6h, state-of-mind82.2h and dream32.9h stale at wake. These notes are excluded from mathematical premises.','Compute-governor advisory snapshot was unchanged on two reads more than30sec apart; stale snapshot was not treated as fresh capacity admission. Jobs were frozen100MB estimates,55sec limits.','Task checklist closure unverified; no shared lock repair or unrelated attachment recovery authorized.'],
 'packet_ids':['A040']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
sections={
 'exact target, quantifiers, hypotheses and units':
 'For every r>=3, construct an actual Boolean same-support reference transaction whose fixed-alpha reset bill is bounded away from zero while the queried influence and five positive proposed credits vanish. Logs are base2. PROOF.md gives all parameters and support hypotheses. The r>=8 original-priority transaction also pays every actual reset from its ORIGINAL admitted source, retaining both signs, all outcomes and old booking omega<=1/4. This refutes a reference-payment mechanism; H(G)/I(G)->2, so it does not disprove FEI.',
 'sources actually read, revisions and theorem locators':
 'Read current BOARD.md, own STATUS.md and B08 STREAM_NOTES.md. Consumed A036 stage20261023T050401 PROOF/CLAIMS (same-profile point theorem, v1 digest d0c8e4699f7c789d396b85a3d1249ac2dbc5ca8234b8c9f991865f6880696217), A037 stage20261023T055409 PROOF (monotone point history), A050 stage20261023T042019 REPORT (same-original-source second reset), and A047 stage20261023T055836 PROOF/CLAIMS (nonpoint same-support obstruction, digest c51b590eea699ca82ad2ec3cb3df74228e3e3e6ed6ecd9d9419d58ff6781c5df). Exact source byte receipts are in out/SOURCE_RECEIPTS.json. The existing protocol/campaign/papers baseline from prior stages is retained; no new full-paper audit is claimed. EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2 was reread. The user extension to Oct23 14:49UTC takes precedence over its legacy campaign dates.',
 'complete derivation or exact first unsupported line':
 'See PROOF.md sections1-4 for complete spectra, physical edges, normalized outcomes, convexity, asymptotic coefficients and full signed original-source accounting. At alpha=1/6 the reference outcomes are19/40,21/40; sigma>kappa=log2(400/399)/2>1/600, so sigma/Inf_j(G)>2^r/300. Writing d=2^-r,c=18-5log2(10),g=1-1.5log2(1.5), the strictly positive credits have E~9rd^2, J~(1+c)d/2, P~rd/2, Gamma~grd, TC~1.5r^2d. Their ratios to sigma and H(G)->2 all vanish. The outcome KL itself is a nonvanishing COST, explicitly retained, not silently counted as a small credit. The complete priority-source transaction has remaining margin>=13/8 for every r>=8. The first unsupported universal line is a transferable ORIGINAL-source/likelihood amortization for arbitrary Boolean cores and repeated histories; no arbitrary initial price is supplied.',
 'executed validation with domain, arithmetic, commands and outputs':
 f'Frozen specs: out/FROZEN_SPEC.json, out/PRE_MAIN_AMENDMENT.json and out/AUDIT_SPEC.json. The initial three-bit census was cancelled UNEXECUTED after reading A047 (out/RETIRED_UNEXECUTED_SPEC.json). Duplicate outer sign labels were removed BEFORE the main run: four distinct complete physical policies r=3,4,5,6, each already containing BOTH a signs and BOTH j children, maximum physical dimension11. Grouped exact formulas cover18 prescribed r values3..16,24,32,64,128. Commands from the run: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/audit.py. Final pilot59 checks passed in{pilot["runtime_seconds"]:.6f}s; main282 passed in{main["runtime_seconds"]:.6f}s; independent implementation1442 passed in{audit["runtime_seconds"]:.6f}s, with37 exact prime-log identities. Preliminary pilot was not added to totals. Main uses Fraction FWHT and36-term atanh logs with proved remainder, outward dyadic2^-120 rounding; audit imports no main or foreign helper, using direct character sums and rational prime-log vectors. Finite interval strict signs of tiny credits are asserted only through r32; positivity for r64/128 and all r is analytic, not an interval precision claim. All-r extension uses explicit grouped spectra, convexity and entropy tails, never finite-case extrapolation. No Lean/formal verification claimed. Each job frozen at100MB and55sec; all elapsed well under the cap. The >300MB gate was not triggered. No mathematical failure was hidden; pre-main label/spec corrections and cancelled work remain saved.',
 'proof dependencies and changed downstream conclusions':
 'The new proof is self-contained; source-bound A047 analytic review is separate in REVIEW_A047.md and CLAIMS.json. Its unchanged statement digest is checked, but census/minimality clauses are NOT reviewed or accepted here. A036/A037 point-factor results are not refuted. The broad arbitrary-Boolean inequality sigma_i<=K_alpha Inf_i fails even with identical support and same alpha. Any fixed linear combination of the FIVE stated credits also fails to pay the local bill. The original-source account pays this family, so a global ownership/amortization route remains viable. These author-checked proofs have not received external independent acceptance; a different implementation by the same author is not such acceptance.',
 'one next mathematical action and independent reviewer':next_action+' No message to another agent was sent; this is the source-bound handoff for supervisor collection.',
 'actual persistence receipts or precise save blocker':
 'All requested run artifacts and rolling files are saved only inside A040. code/finalize.py verifies protocol field sets, statement hashes, source/algorithm pins, output counts, compatibility equality, two-line STATUS and file-size cap; out/LOCAL_RECEIPT.json records byte hashes. No shared tree, another agent folder or brain was modified for research. External mirror/supervisor ingestion remains unverified. Brain self-care is degraded/unverified (wake attachment/write-lock timeout and stale owner/mind/dream sources); this affects confidence in those notes/attachment integrity, not the direct mathematical certificates. Task ledger closure is unverified, with no shared-lock repair. Compute advisory snapshot remained stale; it was not used as fresh resource authorization.'}
report='# A040 stage9: rare-query posterior credit insufficiency\n\n'+'\n\n'.join('## '+k+'\n\n'+sections[k] for k in protocol['required_per_run']['report_fields'])
report+='\n\nUniversal bridge: This stage advances C024 history transfer and C019 stopping-tree payment by proving that even same-support, same-alpha full-spike resets cannot be charged to the current influence or any fixed combination of the five specified posterior credits: the ratio exceeds2^r/300. It also preserves a concrete complete original-source account with margin>=13/8, so the obstruction is local payment rather than a failure of the ancestor bank. The universal FEI constant improves by zero. What remains is an arbitrary-Boolean original-source price and an amortized bound through repeated rare physical queries. The next source-likelihood payment inequality directly targets that missing universal ownership bridge, rather than another isolated class estimate.\n'
save(R/'REPORT.md',report)
save(A/'STATUS.md','STATE: Stage9 proved sigma/Inf>2^r/300; five positive posterior credits vanish; original-source margin>=13/8; main282+audit1442 PASS; FEI OPEN, external review pending.\nNEXT: Amortize nonvanishing outcome KL by ORIGINAL-source spectral likelihood across rare queries; A048 reconstructs inequality obstruction, A047 reviews full original-source payment.\n')
save(A/'WORKLOG.md',read(A/'WORKLOG.md')+f'\n{now} [{R.name}] Consumed A036/A037 point closures, A047 finite nonpoint obstruction and A050 original-source requirement; cancelled duplicate census before execution. New all-r rare-query family has sigma/Inf>2^r/300 and five strictly positive credits with exact vanishing asymptotic ratios. Full actual original1/8-to1/6 priority transaction keeps oldquarter and all branches, margin>=13/8 for r>=8. Main282 checks (4 complete policies+18 grouped regimes), separate audit1442 checks/37 prime-log identities PASS; final pilot59 not included in main+audit total1724. Scoped A047 analytic review only, no census acceptance. External review/mirror, arbitrary source pricing and repeated histories remain open. Wake/self-care degraded; no notes used as proof.\n')
save(A/'LEARNED.md',read(A/'LEARNED.md')+f'\n{now} A040 stage9: For v_r=(-1)^z(1-2*1[w=0 or(j=1,w=e0+e1)]), actual same-alpha full-spike coherent rare-j query has reference outcomes1/2+-3alpha/20 and sigma>kappa_alpha>0 despite Inf_j(G)=2^-r/2. At1/6, sigma/Inf>2^r/300. With c=18-5log2(10),g=1-1.5log2(1.5), the FIVE positive credits E,J,P,Gamma,TC are asymptotic to9r4^-r,(1+c)2^-r/2,r2^-r/2,gr2^-r,1.5r^2*2^-r. All vanish relative to sigma and H(G)->2. Outcome KL is a nonvanishing cost, not an omitted credit. Full original priority alpha0=1/8 source pays actual first1/6 and second same-profile resets with oldquarter: margin>=13/8 for allr>=8. This fails local query influence pricing while preserving ancestor payment; it does not touch A036 point theorem or disprove FEI. Need ORIGINAL-source likelihood amortization, not another local KL positivity lemma. See {R.name}/PROOF.md.\n')
# Validate exact protocol shapes and algorithm pins without rerunning successful mathematics.
fields=protocol['required_per_run']
assert set(progress)==set('packet_ids' if k.startswith('packet_ids ') else k for k in fields['progress_fields'])
for c in (scoped,new):
 assert set(c)==set(fields['claim_fields'])
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
assert all('## '+h in report for h in fields['report_fields']) and report.strip().split('\n\n')[-1].startswith('Universal bridge:')
assert sha(R/'code/audit.py')==obj(R/'out/AUDIT_SPEC.json')['helper_sha256']
files=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='LOCAL_RECEIPT.json')
assert all(p.stat().st_size<20_000_000 for p in files)
dump(R/'out/LOCAL_RECEIPT.json',{'status':'PASS','time_utc':now,'protocol_fields':'EXACT','statement_digests':'EXACT; A047 unchanged','main_checks':282,'audit_checks':1442,'audit_prime_log_equalities':37,'external_review':'PENDING','mirror':'UNVERIFIED','research_jobs':'NONE_RUNNING','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'rolling_files':[{'path':str(A/n),'sha256':sha(A/n)} for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]})
print(json.dumps({'status':'PASS','main_checks':282,'audit_checks':1442,'files':len(files)+1,'claim':cid+'@1','external_review':'PENDING','mirror':'UNVERIFIED'}))
