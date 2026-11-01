from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];AG=R.parents[1];ROOT=AG.parents[1]
OLD=AG/'runs/20261023T105559Z-fleet03-A029-child-deficit-transport'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
names=['pilot','main','logit_pilot','logit_main','independent','relative_independent']
results={n:read(R/'out'/f'{n}.json') for n in names}
assert all(d['status']=='PASS' for d in results.values())
main=results['main'];rel=results['logit_main'];ind=results['independent'];ri=results['relative_independent']
consumers=['A028','A026','A030','A056','A094','A096','A097']
old=read(OLD/'CLAIMS.json');own=[c for c in old if c['claim_id']=='A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT'][-1]
own['version']=4
own['exact_statement']+=' Version4 retains prior scoped clauses and adds these supplied-reference theorems. For arbitrary finite uniform independent controller/data blocks and fully shared Boolean sources, supply one original controller and two source spectral references positive on their true supports, inherited through their OWN actual phase channels and normalizers. Set T=W+gamma Da, S=Z+gamma Cvac, eta=Var(a)*Pr(G!=H). Keep inherited row marginal and nonempty shape. At each occupied row and every adaptive history choose any real lambda in[1/2,2], and target ell=lambda*k/[1+(lambda-1)*k]. Its exact extra KL C=sum q D_Ber(k||ell) satisfies C<=eta/2. The quantity eta is a physical supermartingale, eta<=I_controls(F), and Trel=T+eta/2, Srel=S+eta/2-C>=0 give Dtarget=Trel-Srel. For EVERY finite adaptive mixed stopping tree, full entropy-decrement path plus ALL complete terminal CE equals Hroot+Trel_root-sum reach*(Trel_parent-E Trel_child)-E Srel_leaf, hence costs at most Hroot+Troot+eta_root/2. Raw reconstruction from the CURRENT target reference equals the signed target KL increment plus BOTH actual output refunds. No descendant allowance is renewed. Exact actual-child compensation is d0+d1<=2(R+A), d_i=C_i-S_i, R=U-b-H-T. A separate fixed-mixture class epsilon in[0,1/16] admits the same telescope with one ORIGINAL constant1/8 allowance. That constant is not universally influence-priced: with a=y,G=1,H negative only at0^n, exact source/controller references give T=S=0, I(F)=(n+1)2^-n and fixed-mixture cost C_n>1/1024 for all n>=4, although H(F)<4I(F). On the literal retained A029@3 family and prefix, the first odds target is a relative-odds target (lambda7/9 on the9/10 row, lambda1 elsewhere). Every subsequent finite adaptive mixed relative-odds history is paid by the SAME original4I(F_m) and old debit1/8, retaining the first profile cost exactly once, with reserve>3m-263/128>=121/128. The separate fixed-mixture envelope has reserve>3m-497/256>=271/256. Signed round trips give unbounded positive variation at fixed influence, refuting positive-part accounting. Exact-reference relative targets with alpha=rho,k1/2,ell2/3 lie outside A028@9 posterior-channel image and require the real eta/2 allowance. Universal initial H+T suppliers and necessity of bounded-relative-odds targets remain open; no full FEI theorem is asserted.'
own['statement_sha256']=hashlib.sha256(own['exact_statement'].encode('utf-8')).hexdigest()
own['hypotheses']+=[
 'New v4 general mixed-tree target theorem: normalized originally supplied source/controller references inherited through OWN physical channels and actual normalizers, all off-true reference mass retained',
 'For each occupied row relative factor may vary arbitrarily by row and history in real[1/2,2]; zero/one odds are fixed, zero-true rows unchanged; no nonempty profile means no nonempty target mass',
 'Original admission must genuinely cover Hroot+Troot+eta_root/2 (or Hroot+Troot+1/8 for the separate fixed-mixture class); original old debit b is not dropped',
 'All actual children, current output references and both erasure/outcome refunds retained; signed reset increments are not clipped',
 'Integrated rate4 corollaries are only the stated common-character family m>=1 with literal DATA x0 and CONTROL y0 prefix and first shape/odds target retained; no universal unused-credit assertion'
]
own['contributors']=['A029','A028 (supplied canonical T/S core and separate posterior-channel admissibility)','A030 (generic signed-reset interface)','A026 (carried-profile precursor)']
own['proof_source']={'retained_v3':str(OLD/'DERIVATION.md'),'new_derivation':'DERIVATION.md sections1-10','source_reviews':'REVIEW.md','constant_main':'out/main.json','relative_main':'out/logit_main.json','separate_implementations':['out/independent.json','out/relative_independent.json'],'frozen_specs':['out/FROZEN_SPEC.json','out/LOGIT_FROZEN_SPEC.json','out/VERIFY_SPEC.json','out/VERIFY_RELATIVE_SPEC.json']}
own['proof_dependencies']=[{'claim':'A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@3','scope':'retained literal paid prefix and actual current odds reference'},{'claim':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@9','scope':'supplied canonical T/S transport and comparison with posterior-channel image; old universal supplier/surcharge clauses excluded'},{'claim':'A030 version5','scope':'generic signed-reset and physical likelihood-account interface only'},{'claim':'A026 version5','scope':'two-sided structural-completion comparison only; different zero-pair channel not substituted into checks'},'New scalar KL estimate, eta supermartingale and influence bound proved in DERIVATION sections6-8; no external universal supplier used']
own['review_records']=[]
own['status']='AUTHOR_PROOF_EXACT_CHECKED_EXTERNAL_REVIEW_PENDING_NOT_LEAN_CERTIFIED'
own['supersedes']=[{'claim_id':own['claim_id'],'version':3,'reason':'Retains scope; adds all finite mixed relative-odds histories and influence-scaled original allowance, plus fixed-mixture obstruction'}]
own['refutes']+=[{'statement':'Fixed epsilon1/16 row-odds mixture has extra liability <=K I(F) universally for some finite K','witness':'Relevant point-defect family: I=(n+1)2^-n ->0, C_n>1/1024 for all n>=4; FEI still holds H<4I'},{'statement':'Positive parts of all relative-odds target transactions fit one eta/2 bank','witness':'a=y with k dummy controls, G=z1,H=z2 and exact refs: signed charge C=(1/2)log2(9/8), positive sum kC at fixed I=3/2 and eta=1/2'}]
gap='Universal original influence-priced Hroot+Troot source/controller allowance, and a proof that a NECESSARY target has bounded relative odds or another source-owned price. Arbitrary prescribed fixed-strength mixtures cannot satisfy a universal influence price.'
own['first_unproved_line']=gap;own['next_consumers']=consumers
claims=[]
source_specs=[('A028','20261023T122923Z-fleet03-A028-stopping-tree-payment',9,'HOLDS_NEW_POSTERIOR_CHANNEL_AND_MIXED_TREE_CORE_ONLY'),('A026','20261023T113002Z-fleet03-A026-good-coordinate-erasure',5,'HOLDS_TWO_SIDED_STRUCTURAL_COMPLETION_ONLY'),('A030','20261023T110419Z-fleet03-A030-restriction-plateau-tests',5,'HOLDS_GENERIC_SIGNED_RESET_AND_LIKELIHOOD_INTERFACE_ONLY')]
for agent,run,version,verdict in source_specs:
 p=ROOT/'agents'/agent/'runs'/run/'CLAIMS.json';cs=read(p)
 if isinstance(cs,dict):cs=cs.get('claims',[cs])
 c=[x for x in cs if x['version']==version][-1]
 assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
 c['review_records'].append({'reviewer':'A029/fleet03','reviewed_version':version,'verdict':verdict,'scope':'Exactly the named new scope in REVIEW.md; other bundled claims remain unreviewed; no repair supplied','source':str(R/'REVIEW.md'),'source_sha256':sha(R/'REVIEW.md')})
 claims.append(c)
claims.append(own);save(R/'CLAIMS.json',claims)
p=read(OLD/'PROGRESS.json');p.update(run_id=R.name,attempt_id='A029-stage9-influence-priced-relative-odds-transport',method='Consume new A028@9/A026@5/A030@5; analytic actual-child deficit condition, eta supermartingale and scalar KL; exact mixed-tree census and separate direct-character checks',mathematical_delta='All finite mixed relative-odds histories paid by ONE original eta/2<=I_controls/2; literal old prefix at same4I and old1/8 retains reserve>121/128. Fixed-strength mixture universal influence price refuted by actual relevant point-defect family, not FEI.',deliverable_status='COMPLETE_LOCAL_REVIEW_HANDOFF',mathematical_status='SCOPED_ANALYTIC_AUTHOR_PROOF_EXACT_CHECKED; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN; NO_LEAN_CLAIM',claim_versions_used=['A029@3 literal prefix','A028@9 supplied T/S and posterior-channel image scoped review','A026@5 two-sided completion scoped review','A030@5 signed-reset interface scoped review'],claims_created_or_changed=[own['claim_id']+'@4']+[a+'@'+str(v)+' scoped review record' for a,_,v,_ in source_specs],source_artifacts=['DERIVATION.md','REVIEW.md','out/main.json','out/logit_main.json','out/independent.json','out/relative_independent.json','out/SOURCE_RECEIPTS.json','out/ARTIFACTS.json'],next_consumers=consumers,next_action='Independently review eta/2 transport and consume it in the original source/controller supplier chain; test the first NECESSARY target outside bounded relative odds, retaining all old liabilities. Do not repeat histories already covered by the theorem.',stagnant_substantive_attempts=0,blockers=[gap,'Independent peer review of A029@4 pending; separate implementation is not peer acceptance','Supervisor mirroring/adoption unverified','Brain self-care degraded/unverified: stale owner model/state-of-mind/dream records; not used as proof evidence'],packet_ids=['A029'])
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
counts={n:sum(results[n].get(k,0) for k in ['assertions','source_assertions','previous_mixed_assertions','prior_adapter_assertions']) for n in names}
save(R/'out/VALIDATION_SUMMARY.json',{'status':'PASS','counts_by_run':counts,'implementations_are_not_external_peer_review':True,'full_fei':'OPEN','no_jobs_intended_to_remain_running':True})
report=f'''# A029 stage9: child deficits through all mixed relative-odds histories

## exact target, quantifiers, hypotheses and units

Bits, uniform finite cubes, disjoint controller/data blocks and arbitrary fully shared Boolean sources. Supplied original source/controller references and their OWN physical channels are hypotheses. For every finite adaptive mixed stopping tree and any rowwise real odds factors in[1/2,2], the actual extra target KL is at most eta/2, eta=Var(a)Pr(G!=H)<=I_controls(F). ONE original allowance pays the entire signed history. The exact two-child compensation condition is d0+d1<=2(R+A), d_i=C_i-S_i; both actual deficits are retained. Full FEI OPEN; universal initial suppliers are not claimed.

## sources actually read, revisions and theorem locators

BOARD, B06 STREAM_NOTES, own status and earlier stages; campaign execution-v2 required context was read during this continuing packet. This stage consumes A028@9 DERIVATION sections2-5 (posterior-channel core), A026@5 sections1,6 (two-sided completion) and A030@5 PROOF sections1,2,5 (signed-reset/likelihood interface). Byte receipts: out/SOURCE_RECEIPTS.json. Scoped independent source reviews: REVIEW.md. Their other bundled clauses are not accepted. A028@9 pays its admissible posterior-channel image from source slack; our exact-reference lambda2 guard lies outside that image and uses a real additional original allowance.

## complete derivation or exact first unsupported line

DERIVATION.md sections1-10 proves the scalar KL bound, physical eta supermartingale, original Trel/Srel stopping identity, raw CURRENT-reference resets and both refunds. No child bank is renewed. The literal A029@3 first shape, controller query and first odds target are retained exactly. SAME original4I and old debit1/8 pay all later mixed relative-odds histories with reserve>3m-263/128>=121/128. The separate constant1/8 mixture envelope leaves>271/256. A relevant point-defect family has I=(n+1)2^-n but fixed-mixture cost>1/1024, proving that constant envelope is not universally influence-priced; these functions satisfy H<4I. Signed round trips refute clipping positive resets. First unsupported universal line: {gap}

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede their jobs in out/. Exact Fractions, prime-log linear identities and rational logarithm enclosures; direct character/edge reconstruction in the separate implementation. No float search is a proof. All planned memory <=180MB, below the300MB memok threshold; pilot caps55s and main caps240s, no domain escalation. Fresh memory was checked in this stage; the stale shared governor was not restarted or altered.

Commands: python -X utf8 code/check.py pilot|full; python -X utf8 code/logit_check.py pilot|full; python -X utf8 code/independent.py; python -X utf8 code/relative_independent.py. PASS outputs: out/pilot.json, main.json, logit_pilot.json, logit_main.json, independent.json and relative_independent.json.

Constant full:256 roots, {main['edge_rows']} edge cases ({main['edge_rows']-6912} history/guard edges beyond6912 census), {counts['main']} exact predicates across its modules, {main['seconds']}s. Relative full:256 roots, {rel['edge_rows']} edges, {counts['logit_main']} predicates, {rel['seconds']}s. Pilots separately: {counts['pilot']} and {counts['logit_pilot']} predicates. Direct-character constant verifier:{ind['assertions']} predicates, {ind['seconds']}s. Relative verifier:{ri['assertions']} predicates, {ri['seconds']}s;3 literal m1..3 prefixes,15 scalar cases,5 compressed rare cases and4 truth-table rare cases. Counts are separate executions, not independent peer acceptance; no prior-stage counts are included. All-real/all-width claims use the displayed analytic proof, rather than extrapolation from the census. No Lean certification claimed.

## proof dependencies and changed downstream conclusions

A029@4 extends the same candidate, retaining @3. A028@9, A026@5 and A030@5 reviews are narrowly scoped in CLAIMS.json and REVIEW.md. Repeated reconstruction from the actual odds-changed law is now closed for bounded relative odds through arbitrary mixed histories, including the next shared DATA query. The new row-odds liability has an explicit original influence price <=I_controls/2. Initial source/controller eligibility and necessity of this target class remain open. No universal FEI result, coordinate selector or arbitrary-target payment follows.

## one next mathematical action and independent reviewer

Consume eta/2 in the complete original source/controller supplier chain and locate its first NECESSARY target outside[1/2,2]; test whether source slack or a different physical supermartingale pays it. A028/A030 should independently reconstruct the allowance and current-reference telescope; A026/A056/A094/A096/A097 can audit the unchanged-rate prefix. Peer acceptance is pending. Another finite history inside the closed target class is unnecessary.

## actual persistence receipts or precise save blocker

Four protocol files, proofs, specs, code and exact outputs are saved in this run. STATUS.md has two lines; dated WORKLOG.md and LEARNED.md record the result. out/ARTIFACTS.json records file sizes/hashes; code/finalize.py checks schemas, statement hashes and identical PACKET_DELTA/PROGRESS. No own arithmetic job is intended to remain running. Supervisor mirroring is unverified; no git command or shared research mutation was made. Brain self-care remains degraded/unverified because owner-model, state-of-mind and dream records are stale; those records were not mathematical evidence. Shared lifecycle closure is tracked separately in local receipts.

**Universal bridge**: C019 stopping-tree payment and C024 history transfer advance from one paid odds reset to EVERY finite adaptive mixed relative-odds history, with one proved row-odds allowance <=I_controls/2; the literal old prefix still fits original4I minus old1/8 with reserve>121/128. Fixed-strength mixing has no universal influence price, by an actual relevant Boolean family that itself satisfies FEI. The universal original H+T supplier and necessity of bounded relative odds remain open. Consuming this influence-priced component in the full supplier chain and attacking its first necessary out-of-class target is the shortest next route to full FEI; another admitted-family sweep would not close that missing universal line.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(AG/'STATUS.md').write_text('STATE: Stage9 saved: A029@4 author proof/exact checks; all mixed relative-odds transport costs ONE eta/2<=I_controls/2, same old4I prefix reserve>121/128; fixed-mixture universal price obstructed; FEI OPEN, peer review pending.\nNEXT: A028/A030/A026/A056/A094/A096/A097 review eta account and consume it in universal original source/controller supplier chain; attack first NECESSARY target outside bounded relative odds; no descendant bank renewal.\n',encoding='utf-8',newline='\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,text in [('WORKLOG.md',f'{stamp} stage9: read new BOARD/B06 and A028@9/A026@5/A030@5; derived exact two-child deficit condition, constant envelope, fixed-mixture rare-activation obstruction and relative-odds eta/2 repair. Constant and relative pilots/main PASS, two separate direct-character verifiers PASS; current-run counts {counts}. Same old4I/old1/8 literal prefix reserve>121/128 for all mixed bounded-relative-odds histories. Saved source scoped reviews, no universal supplier/FEI claim; independent peer review/mirror pending. Brain wake degraded; stale records not used as proof. All searches bounded, no job left intentionally running.'),('LEARNED.md','Stage9 durable: ell=lambda*k/(1+(lambda-1)k), lambda in[1/2,2], costs at most k/2 per row; eta=Var(a)Pr(G!=H) is supermartingale with control release gamma*ahat(singleton)^2 and DATA release0, eta<=I_controls. T+eta/2 and S+eta/2-C pay all signed mixed histories from ONE original allowance. Exact compensation is d0+d1<=2(R+A), not positive-part charges. Fixed epsilon1/16 mixing is not universally influence-priced: relevant point defect I=(n+1)2^-n, C>1/1024 for n>=4 while H<4I. A028@9 image pays C<=Z but cannot change odds when actual/reference label posteriors coincide; relative targets can be outside it and need real original allowance. Literal old family/prefix same4I minus1/8 keeps>121/128; full FEI supplier/necessary-target bridge remains open.')]:
 existing=(AG/name).read_text(encoding='utf-8') if (AG/name).exists() else ''
 marker='stage9: read new BOARD/B06' if name=='WORKLOG.md' else 'Stage9 durable:'
 if marker not in existing:
  with (AG/name).open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+text+'\n')
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
def fields(v):
 if isinstance(v,list):return set((x if isinstance(x,str) else x['name']).split(' (')[0] for x in v)
 return set(v)
def locate(d,key):
 if isinstance(d,dict):
  if key in d:return d[key]
  for v in d.values():
   found=locate(v,key)
   if found is not None:return found
 if isinstance(d,list):
  for v in d:
   found=locate(v,key)
   if found is not None:return found
 return None
assert set(p)==fields(locate(protocol,'progress_fields'))
assert all(set(c)==fields(locate(protocol,'claim_fields')) for c in claims)
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert len((AG/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
manifest=[]
for f in sorted(R.rglob('*')):
 if f.is_file() and '__pycache__' not in str(f) and f.name!='ARTIFACTS.json':
  assert f.stat().st_size<20*1024*1024
  manifest.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
save(R/'out/ARTIFACTS.json',manifest)
print(json.dumps({'status':'SAVED_AND_VALIDATED','claim':own['claim_id']+'@4','counts_by_run':counts,'files':len(manifest)}))
