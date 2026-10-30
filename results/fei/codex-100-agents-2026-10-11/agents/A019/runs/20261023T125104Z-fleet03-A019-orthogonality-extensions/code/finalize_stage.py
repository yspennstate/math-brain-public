import json,hashlib,copy
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];BASE=R.parents[1]
OUT=R/'out';now=datetime.now(timezone.utc).isoformat()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
checks=json.loads((OUT/'CHECKS.json').read_text(encoding='utf-8'));pilot=json.loads((OUT/'PILOT.json').read_text(encoding='utf-8'))
assert checks['status']==pilot['status']=='PASS'
assert len(checks['cases'])==3 and len(checks['review_cases'])==3
sources={
 'A018':Path(r'agents\A018\runs\20261023T121958Z-fleet03-A018-shared-data-collision-law'),
 'A020':Path(r'agents\A020\runs\20261023T110208Z-fleet03-A020-selector-boundary-tests'),
 'A016':Path(r'agents\A016\runs\20261023T112921Z-fleet03-A016-addressing-benchmark'),
 'A019-prior':R.parent/'20261023T105439Z-fleet03-A019-orthogonality-extensions'}
receipts=[]
for who,p in sources.items():
 for name in ['REPORT.md','CLAIMS.json']:
  f=p/name
  receipts.append({'source':who,'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'use':'Read report/claims' if who in ['A018','A020'] else 'Claim statements and prior source proof interface'})
dump(OUT/'SOURCE_RECEIPTS.json',receipts)
statement=("For every k>=8,m>=2 put rho=2^-k, G=product of m disjoint three-bit signs g3 (negative only at000), A=point_k*(1-G)/2, h0=u,h1=(1-A)u+A, and use the original contaminated-core/actual-selector/complete-activation reference hierarchy of the hypotheses. Query q; on q1 leave seed0 and padding live and short-circuit each other seed at its first1 or after000, without querying its remaining irrelevant bits. Keep q0 and ALL q1 physical outcomes, with ORIGINAL marginal codes and actual gate conditionals. Write C_frontier for complete averaged CE, I_frontier for averaged remaining physical influence, p=rho*(1-(3/4)^m)/2, lambda=(log2(8/5))/2+(log2(4/3))/4>3/8. Exactly 4I_frontier=6+3rho/8+(2k-3)*p/2; C_frontier>21rho*(m-1)/1024. The active-seed sector contributes exactly (7rho/128)*(m-1)*lambda to the averaged ghost-cleanup CE release, and the full release is at least that amount. For ANY old U>=0, 4I_frontier-C_frontier-U<6+(14k-15)*rho/16-21rho*(m-1)/1024. The initial cores/root are genuinely rate4 eligible with original B>3/4 and root surplus>B+5/8. In particular m=2^(k+9)+1 gives whole-frontier reserve<-4 for every k>=8 while disagreement p tends to0; m=2^(2k+1)+1 gives reserve tending to minus infinity as p tends to0. This refutes every-prefix averaged eligibility for this original source without mandatory cleanup, not FEI or cleanup-complete payment.")
statement=statement.replace('while disagreement p tends to0','while neighboring disagreement p/2 tends to0')
statement += ' Moreover for m>=4, putting Dghost=(7rho/128)*(m-1)*lambda, the exact active-sector CE is (7rho/128)*(2k+11+(m-1)*lambda), and 0<=C_frontier-Dghost<(7rho/128)*(2k+11)+k+8. Averaged true entropy is at most k+7; hence full reference KL has the same exact linear-in-m leading coefficient at fixed k.'
statement += ' Here J=I(1-2A), c1=CE(P_h1,Q1), and B=7/4-p+J/2-c1/4; all these belong to the original unsplit source.'
hyp=[
 'Independent uniform physical bits; Fourier entropy/cross-entropy in bits; Qb=(P_hb+delta_empty)/2 and parent core reference is the actual q-frequency conditional lift of average Qb.',
 'Exact two-bit point-defect mask s has mean1/2 and flat squared spectrum; F=1 at fresh gate0 and h*s at gate1. Each complete activation reference has data marginal (Qcore tensor P_s+delta_empty)/2 and actual gate-frequency conditionals.',
 'Every descendant core code is the exact frequency marginal of ORIGINAL Q1, with no reset, support restriction, renormalization or renewed influence. The original old U is retained at global reach.',
 'A finite adaptive physical partition: q0 untouched; q1 short-circuits seeds1 throughm-1, retains ALL outcomes including000,001,01 and first1, and never queries seed0,padding,u,gate or mask. Cleanup statement subsequently marginalizes all remaining ghost bits and retains their identical physical children.'
]
cid='A019-AVERAGED-ADAPTIVE-GHOST-PREFIX-OBSTRUCTION'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A019/fleet03'],'proof_source':{'path':str(R/'REPORT.md'),'derivation':'out/DERIVATION.md','certificates':['out/CHECKS.json','out/PILOT.json']},'proof_dependencies':['A019-NO-NEW-INFLUENCE-TENSOR-OBSTRUCTION@1: original tensor Fourier/source eligibility identities, with all-k remainder extension displayed','Elementary Fourier marginalization, finite log-sum/KL and exact physical influence conservation'],'review_records':[{'reviewer':'A019/fleet03','independent':False,'verdict':'AUTHOR_ANALYTIC_PROOF_EXACT_CHECKED','assertions':checks['assertions'],'formal_status':'NOT_FORMALIZED'}],'status':'AUTHOR_PROOF_EXACT_CHECKED_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':['Unregistered EVERY-prefix averaged signed eligibility for the original one-balanced tensor source without obligatory ghost cleanup'],'first_unproved_line':None,'next_consumers':['A018','A020','A016','B04-lead','A094']}
original=json.loads((sources['A018']/'CLAIMS.json').read_text(encoding='utf-8'))[-1]
review=copy.deepcopy(original)
review['review_records'].append({'reviewer':'A019/fleet03','independent':True,'verdict':'PARTIAL_SCOPE_HOLDS_OWNERSHIP_IDENTITY_AND_COMPLETE_PHYSICAL_ENDPOINT','scope':'Independently reconstruct W=B+Omega and complete endpoint >2; finite tests check Omega<85/64 and Tq<1/4 only diagnostically. The uniform Tq estimate and whole combined source claim do NOT receive full independent acceptance in this record.','substantive_repair':False,'source':str(R/'REPORT.md'),'checked_at':now})
review['status']='PARTIAL_A019_REVIEW_ONLY_FULL_SOURCE_ACCEPTANCE_PENDING'
dump(R/'CLAIMS.json',[claim,review])
der=(OUT/'DERIVATION.md').read_text(encoding='utf-8')
der=der.replace('For every nonempty frequency of the live seed, each padding/u row','For every nonempty frequency of the live seed, on supported ghost-empty rows, each padding/u row')
(OUT/'DERIVATION.md').write_text(der,encoding='utf-8')
reviewtext='''# Independent source review: deliberately restricted scope

A018-DENSITY-ONLY-SOURCE-OWNERSHIP@1 is copied unchanged, at its original statement/hypotheses hash. Independently reconstructing complete actual spectra gives parent-core CE=(1+c1)/2+Delta-D. Applying the complete activation identity gives Croot=5/4+c1/4+Delta/2-D/2+Psi(p/4)-Aref(p^2/16,(2+p^2)/32). Subtracting B from physical4I-Croot leaves exactly the original Omega. Hence no dimension-growing J/2 owner remains outside B.

For the physical endpoint, ALL event bits, including reference ghosts, are queried. Original Q1 then has only empty/u masses(1+p)/2,(1-p)/2. The u core cost log2(2/(1-p))<3/2 for p<=1/4; its full activation cost<15/4 using Psi(0)=2 and nonnegative Aref. A constant core costs at most1; Psi(1/2)<5/4 gives full activation cost<11/4. Untouched q0 costs<7/2. Physical endpoint influence is6-3p/2, so after U<=1/8 the reserve is strictly greater than19/8-p-U>=2. The scalar Psi bound follows directly by substitution in its displayed logarithmic expression; integer certificates from A018 and our independently evaluated endpoint formulas support it. CE release has positive sign and the original J/2 is retired once.

The checker constructs complete small Boolean spectra/references from truth tables, not A018 output rows. It tests exact ownership cancellation and exact physical endpoint telescoping on singleton events in2,3 bits and a two-point event in3 bits. It independently forces ALL event coordinates, unlike a stopped determination tree. Omega and Tq upper bounds on those cases are diagnostics. This stage does not issue full HOLDS for the uniform Tq calculus bound or the combined A018 claim. No new repair or contributor attribution to that source is made. Its source statement/hash stay unchanged; acceptance is limited to ownership identity and endpoint.
'''
(OUT/'SOURCE_REVIEW.md').write_text(reviewtext,encoding='utf-8')
report=f'''# A019 stage20: an averaged adaptive prefix obstruction with exact ghost debt

## exact target, quantifiers, hypotheses and units

Prove or refute averaged physical prefix eligibility after genuinely interacting seed queries with padding live in the SAME original one-balanced hierarchy. The displayed theorem covers every k>=8,m>=2, every physical outcome of a prescribed short-circuit policy, and all old U>=0. Reference costs are complete and in bits; original influence is retired once. Full FEI remains OPEN. This is a Boolean inherited-reference obstruction, not a Boolean FEI counterfamily.

## sources actually read, revisions and theorem locators

Read current BOARD (12:47UTC), full B04 STREAM_NOTES v2, own STATUS/LEARNED and prior stage19 source. Read A018 stage20 REPORT and claim statements in full, A020 all-adaptive cleanup REPORT, and A016 recent claim statements including fixed-subset averaged payment and mixed-padding repair. Protocol field schemas were reread at execution-v2; campaign/paper conventions are carried from prior stages, with no new external theorem. Machine AGENTS and session wake were consumed before substantive work. Source byte hashes are in out/SOURCE_RECEIPTS.json. The already established disagreement closure max{{2/c,C}} and bent-splice falsifier remain imported standing constraints; no constant-correlation corollary is relabeled new. This stage changes from root-owner search, now closed by A018, to adaptive averaged prefixes, not a duplicate of A020's rare local history.

## complete derivation or exact first unsupported line

{der}

The independent source review is in out/SOURCE_REVIEW.md. It accepts A018's ownership identity and correctly signed complete endpoint only; it does not claim full independent acceptance of its uniform first-query bound. A018 independently accepted both stage19 A019 claims at their unchanged full scopes; its source records are preserved read-only.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the pilot. The first pilot failed because the checker applied a supported-row ratio assertion also to zero-true-mass/reference-positive ghost rows. Those rows must remain in the code; corrected the assertion to positive TRUE mass and retained out/PILOT_CORRECTION.md. No mathematical hypothesis or family was changed. Corrected pilot: `python -B -X utf8 code/check_prefix.py --pilot`, PASS {pilot['assertions']} assertions, four q1 leaves, {pilot['seconds']:.6f}s. Main without --pilot: PASS {checks['assertions']} exact assertions, three fixed fixtures,24 q1 physical leaves, three independent source-review fixtures, {checks['seconds']:.6f}s. Pilot counts are excluded from main counts. Each job is capped60seconds with estimated120MB; no >300MB job, GPU, compiler, detached work or window. Process startup was slow under the stale shared compute heartbeat; no shared repair was attempted.

The checker recomputes integer Walsh spectra, exact Fraction original marginals, physical edge influences, actual complete activation CE, short-circuit reach sums, active-sector masses/ratios and exact expected ghost debt. Both cleanup children are checked identical before their common value is used to average them; cleanup is zero-influence and all outcomes remain represented. Prime-log vectors and proved rational outward intervals establish signs. Integer75^2<2^13 proves lambda>3/8. Finite tests validate formulas outside the k>=8 theorem range; the all-dimensional proof is the displayed algebra, not finite enumeration. No floating-point sign or Lean proof is claimed.

## proof dependencies and changed downstream conclusions

The source tensor eligibility is inherited from stage19, with the explicit all-k remainder extension. New work proves a COMPLETE averaged-prefix obstruction: unlike a distinguished exponentially rare history, it includes every adaptive leaf and the untouched q0 sibling. A016 fixed-subset averaged payment survives because this is an adaptive, outcome-dependent erased set. A020 cleanup-complete payment and A018 all-coordinate endpoint survive because this prefix deliberately retains reference ghosts. This isolates an operation the eventual C019 stopping rule must bundle or charge. No universal supplier is obtained. One new scoped author claim is submitted; source review is explicitly partial. No global stream queue admission or novelty priority is asserted.

## one next mathematical action and independent reviewer

A018/A020/A016 independently reconstruct the short-circuit physical partition and its mean ghost debt. Then test whether mandatory reference cleanup can be bundled at admission with a monotone averaged potential under genuinely overlapping seeds, retaining original Q,U,all siblings and once-retired influence. This is the next unresolved operation; repeating fixed-subset or complete-endpoint estimates cannot repair this counterexample. No peer messages were sent.

## actual persistence receipts or precise save blocker

The four required protocol files, frozen spec, derivation, code and exact outputs are local to this A019 run. Rolling STATUS is two lines, WORKLOG/LEARNED append dated entries. out/PERSISTENCE_RECEIPTS.json checks schemas, statement hashes, identical PROGRESS/PACKET_DELTA, required headings and local file sizes/hashes. Supervisor copying and remote adoption remain unverified; worker git and brain writes were not used. Brain self-care remains degraded/unverified: owner-model,state-of-mind,dream notes are stale, affecting personal-context reliability; none is a mathematical premise. The compute heartbeat is stale and was not repaired. No background research work remains and nothing was stopped.

## Universal bridge

This stage moves C024 history transfer toward C019 stopping-tree payment by closing the averaged-prefix question negatively on an explicit unbounded Boolean tensor family: at disagreement tending to0 the SAME eligible initial source reaches a complete adaptive frontier with reserve<-4, and a faster diagonal tends to minus infinity. Its exact active-sector ghost debt is(7rho/128)(m-1)lambda, so averaging all siblings cannot erase it; it must be paid or obligatorily cleaned. The universal bridge still needs a source-priced stopping policy with cleanup and an influence-priced initial reference supplier. The shortest NEXT is to bundle cleanup before admission and test that bundle on overlapping sources, since this is the precise unpaid operation between the now-understood initial owner, adaptive failure and complete paid endpoint.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B04','packet_id':'A019','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A019-stage20-adaptive-averaged-ghost-debt','method':'Exact physical short-circuit partition, original spectral marginals, prime-log certificates and all-dimensional tensor algebra','mathematical_delta':'Complete averaged prefix reserve <-4 at p->0, unbounded negative on faster diagonal; exact active-sector expected ghost debt; partial independent source ownership/endpoint review','deliverable_status':'COMPLETE_LOCAL_CHECKED','mathematical_status':'SCOPED_OBSTRUCTION_PROVED; FULL_FEI_OPEN; INDEPENDENT_NEW_REVIEW_PENDING','claim_versions_used':['A019-NO-NEW-INFLUENCE-TENSOR-OBSTRUCTION@1','A018-DENSITY-ONLY-SOURCE-OWNERSHIP@1','A020-ALL-ADAPTIVE-TENSOR-CLEANUP@1'],'claims_created_or_changed':[cid+'@1','A018-DENSITY-ONLY-SOURCE-OWNERSHIP@1 partial review only'],'source_artifacts':[str(z) for z in sources.values()],'next_consumers':['A018','A020','A016','B04-lead','A094'],'next_action':'Review adaptive complete partition; bundle mandatory reference cleanup before stopping/admission on overlapping sources from same original Q/U/influence','stagnant_substantive_attempts':0,'blockers':['No universal original supplier or overlapping-source cleanup payment','Independent new claim review and supervisor mirror pending','Brain self-care/compute heartbeat stale; personal context not relied on'],'packet_ids':['A019']}
dump(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
(BASE/'STATUS.md').write_text(f'STATE: Stage20 saved: ALL-outcome adaptive prefix reserve<-4 at p->0; exact ghost debt; {checks["assertions"]} exact checks PASS; A018 ownership/endpoint partial review; FEI OPEN.\nNEXT: A018/A020/A016 review physical partition; bundle obligatory reference cleanup before admission on overlapping sources with SAME Q/U, all siblings and once-retired influence.\n',encoding='utf-8')
entry=f'\n\n[{now}] Stage20: short-circuit m-1 seeds while one seed and padding stay live. Complete averaged physical frontier, not rare history, has reserve<-4 at m=2^(k+9)+1,k>=8; exact active-sector ghost debt7rho(m-1)lambda/128. Initial pilot row-support assertion corrected (reference-only rows retained); corrected pilot and main PASS, main {checks["assertions"]} exact checks. Partial A018 ownership/endpoint review; no full Tq acceptance. FEI OPEN; local persistence, external copying pending.\n'
if R.name not in (BASE/'WORKLOG.md').read_text(encoding='utf-8'):
 with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\nRun '+R.name+entry)
learn=f'\n\n[{now}] Adaptive averaged prefixes require reference cleanup. Short-circuit each of m-1 g3 seeds at first1/000 and leave one g3 live. Ghost empty masses5/8,3/4,1,1 occur with probabilities1/2,1/4,1/8,1/8. Mean log debt lambda=2-log2(75)/4>3/8. Complete active-sector debt at original global reach is7rho(m-1)lambda/128; 4I_frontier=6+3rho/8+(2k-3)p/2. Thus W-U<6+(14k-15)rho/16-21rho(m-1)/1024, <-4 for k>=8,m=2^(k+9)+1. This retains q0 and all leaves, disproving every-prefix averaged eligibility while preserving fixed-subset and cleanup-complete results. Supported-row assertions must not demand equality on true-zero/reference-positive ghosts. Universal initial supplier and cleanup payment for overlapping sources remain open.\n'
if R.name not in (BASE/'LEARNED.md').read_text(encoding='utf-8'):
 with (BASE/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nRun '+R.name+learn)
expected_claim={'claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers'}
assert set(claim)==set(review)==expected_claim
canonical=json.dumps({'statement':review['exact_statement'],'hypotheses':review['hypotheses']},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
assert hashlib.sha256(canonical).hexdigest()==review['statement_sha256']
assert len((BASE/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert set(progress)=={'protocol_revision','run_id','stream','packet_id','gap_id','attempt_id','method','mathematical_delta','deliverable_status','mathematical_status','claim_versions_used','claims_created_or_changed','source_artifacts','next_consumers','next_action','stagnant_substantive_attempts','blockers','packet_ids'}
saved=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
assert hashlib.sha256(saved[0]['exact_statement'].encode('utf-8')).hexdigest()==saved[0]['statement_sha256']
headings=['exact target, quantifiers, hypotheses and units','sources actually read, revisions and theorem locators','complete derivation or exact first unsupported line','executed validation with domain, arithmetic, commands and outputs','proof dependencies and changed downstream conclusions','one next mathematical action and independent reviewer','actual persistence receipts or precise save blocker','Universal bridge']
assert all('\n## '+x+'\n' in report for x in headings)
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000
  if p.suffix=='.json':json.loads(b.decode('utf-8'))
  files.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump(OUT/'PERSISTENCE_RECEIPTS.json',{'checked_at':now,'schema_validation':'PASS','statement_hash_conventions':{'A019':'UTF8 exact statement only','A018':'canonical sorted compact statement+hypotheses JSON'},'progress_delta_identical':True,'status_two_lines':True,'required_report_headings':True,'full_FEI':'OPEN','remote_copy':'UNVERIFIED_SUPERVISOR_PENDING','files':files})
for item in json.loads((OUT/'PERSISTENCE_RECEIPTS.json').read_text(encoding='utf-8'))['files']:
 assert hashlib.sha256((R/item['path']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'status':'PASS','files':len(files)+1,'assertions':checks['assertions'],'new_claim_sha256':claim['statement_sha256'],'full_FEI':'OPEN'}))
