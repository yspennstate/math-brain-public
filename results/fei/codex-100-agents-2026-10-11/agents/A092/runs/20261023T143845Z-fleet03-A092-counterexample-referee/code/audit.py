from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,hashlib,time,sys,copy

R=Path(__file__).resolve().parents[1];HOME=R.parents[1];FLEET=HOME.parents[1]
OLD=HOME/'runs/20261023T121344Z-fleet03-A092-counterexample-referee/code'
for name in ['arithmetic.py','review.py']:(R/'code'/name).write_bytes((OLD/name).read_bytes())
import review as rv
def js(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(b):rv.ck(b)
def ge(a,b):return rv.integer_sign(rv.sub(a,b))[0]>=0
@lru_cache(None)
def stats(v):return rv.stats(list(v))
@lru_cache(None)
def hull(v,K):
 s=stats(v);best=rv.sub(s['H'],{1:K*s['I']})
 if not ge(best,{}):best={}
 for j in range(len(v).bit_length()-1):
  t=rv.scale(F(1,2),rv.add(hull(tuple(rv.child(list(v),j,0)),K),hull(tuple(rv.child(list(v),j,1)),K)))
  if ge(t,best):best=t
 return best
SRC=FLEET/'agents/A080/runs/20261023T133708Z-fleet03-A080-universal-counterexample-standard'
spec={'helper_version':'A092-stage21-v1','sha256':sha(Path(__file__)),'family':'ALL16 labelled two-bit Boolean factors; all256 ordered tensor pairs; all16 two-bit outer gates and16 first cores, fixed second negative-point core','rates':[0,1,2,3],'pilot_tensor_pairs':4,'primary_tensor_rows':1024,'primary_bank_rows':1024,'max_dimension':4,'symmetry':'none; dummies/constants retained','arithmetic':'direct characters plus butterfly and physical edges; exact rational prime-log forms; integer comparisons; complete physical Bellman recursion','memory_estimate_MB':100,'pilot_max_seconds':55,'primary_max_seconds':55,'automatic_escalation':False}
js(R/'out/FROZEN_SPEC.json',spec)
tables=[tuple(1 if (t>>x)&1 else -1 for x in range(4)) for t in range(16)]
rates=[F(0),F(1),F(2),F(3)]
def validate(pilot):
 rv.checks=0;start=time.perf_counter();pairs=[(0,0),(1,6),(6,1),(6,6)] if pilot else [(i,j) for i in range(16) for j in range(16)]
 for i,j in pairs:
  a,b=tables[i],tables[j];v=tuple(a[x&3]*b[x>>2] for x in range(16));s=stats(v)
  ck(s['H']==rv.add(stats(a)['H'],stats(b)['H']));ck(s['I']==stats(a)['I']+stats(b)['I'])
  for K in rates:
   rr=hull(v,K);ck(rr==rv.add(hull(a,K),hull(b,K)))
   saved=rv.sub(s['H'],rr);ck(ge(saved,{}));ck(ge({1:K*s['I']},saved))
 for gate in (range(2) if pilot else range(16)):
  for core in (range(2) if pilot else range(16)):
   a,b=tables[core],rv.point(2);g=tables[gate]
   v=tuple(g[(0 if a[x&3]==1 else 1)+2*(0 if b[x>>2]==1 else 1)] for x in range(16));s=stats(v)
   qa=sum(F(g[0+2*(z==-1)]!=g[1+2*(z==-1)],4) for z in b)
   qb=sum(F(g[(z==-1)]!=g[(z==-1)+2],4) for z in a)
   W=rv.add(rv.scale(qa,stats(a)['H']),rv.scale(qb,stats(tuple(b))['H']));C=rv.sub(s['H'],W)
   ck(s['I']==qa*stats(a)['I']+qb*stats(tuple(b))['I'])
   for K in rates:
    inner=rv.add(rv.scale(qa,hull(a,K)),rv.scale(qb,hull(tuple(b),K)))
    A=rv.add(rv.add(C,{1:6*s['I']}),inner)
    ck(ge(A,rv.add(s['H'],{1:(6-K)*s['I']})));ck(ge(rv.add(s['H'],{1:6*s['I']}),A))
    clip=rv.add(rv.add(C if ge(C,{}) else {},{1:6*s['I']}),inner)
    if s['I']:
     choices=[rv.scale(1/s['I'],s['H'])]
     for q,vv in [(qa,a),(qb,tuple(b))]:
      ss=stats(vv)
      if q*ss['I']>0:choices.append(rv.scale(1/ss['I'],ss['H']))
     best={}
     for e in choices:
      if ge(e,best):best=e
     ck(ge(best,rv.sub(rv.scale(1/s['I'],clip),{1:6})))
    else:ck(not A and not clip)
   if time.perf_counter()-start>55:raise RuntimeError('55s cap exceeded')
 out={'status':'PASS','pilot':pilot,'tensor_rows':len(pairs)*4,'bank_rows':16 if pilot else 1024,'exact_assertions':rv.checks,'seconds':time.perf_counter()-start,'max_dimension':4}
 js(R/'out'/('PILOT.json' if pilot else 'VALIDATION.json'),out)
 return out
p=validate(True);v=validate(False)
source=json.loads((SRC/'CLAIMS.json').read_text(encoding='utf-8-sig'))
old=next(c for c in source['claims'] if c['claim_id']=='A080-EXACT-HULL-TENSOR-FAITHFUL-BANK');c=copy.deepcopy(old)
c['review_records'].append({'reviewer':'A092','independent_reviewer':True,'verdict':'INDEPENDENTLY_ACCEPTED_UNCHANGED_STATEMENT','run_id':R.name,'scope':'Full tensor/hull/sandwich/extraction statement only. A089 owner proof and separate bank coherence are NOT accepted by this review.','proof':'REPORT.md complete reconstruction; code/audit.py independent full Bellman recursion from original truth tables; out/VALIDATION.json','repair_supplied':False})
c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE'
assert all(c[k]==old[k] for k in ['exact_statement','hypotheses','statement_sha256','version','proof_dependencies'])
proto=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(c)==set(proto['required_per_run']['claim_fields']);js(R/'CLAIMS.json',[c])
paths=[SRC/n for n in ['CLAIMS.json','REPORT.md','PROOF.md','SOURCE_REVIEW.md']]+[FLEET/'BOARD.md',FLEET/'claude/B19/STREAM_NOTES.md']
js(R/'out/SOURCES.json',[{'path':str(x),'sha256':sha(x)} for x in paths])
next_action='A072/A075/A089 price INITIAL coherent bank on indecomposable arbitrary Boolean cores from SAME unused original total-influence owner; A074/A092 audit actual root ratios. Do not search more local drift or tensor amplification. A089 owner-proof sign erratum remains separate.'
d={'protocol_revision':proto['revision'],'run_id':R.name,'stream':'B19','packet_id':'A092','gap_id':'C019-INITIAL-FAITHFUL-BANK-PRICE','attempt_id':'A092-stage21-tensor-extraction-review','method':'Independent stopping-policy proof and direct truth-table Bellman/prime-log exact verification.','mathematical_delta':'A080 full-hull tensorization and faithful signed/clipped root-bank extraction independently accepted unchanged;1024 tensor rows and1024 bank/extraction rows checked exactly. Local coherence is no longer the active gap; initial O(I) payment remains FEI-equivalent.','deliverable_status':'COMPLETED_LOCALLY','mathematical_status':'SCOPED_SOURCE_CLAIM_INDEPENDENTLY_ACCEPTED;FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':1,'statement_sha256':c['statement_sha256']}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1,'change':'Independent acceptance, no statement or hypothesis changes'}],'source_artifacts':[str(x) for x in paths]+['out/FROZEN_SPEC.json','code/audit.py','out/VALIDATION.json'],'next_consumers':['A071','A072','A074','A075','A080','A089','B19','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal initial influence-price remains unpaid; no unbounded actual Boolean ratio family supplied.','A089 owner-proof sign correction not reviewed here; supervisor copy unverified.'],'packet_ids':['A092']}
assert set(d)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']};js(R/'PROGRESS.json',d);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# A092 stage21: faithful Boolean counterexample extraction referee

## exact target, quantifiers, hypotheses and units

Independently accept A080-EXACT-HULL-TENSOR-FAITHFUL-BANK@1, unchanged statement/hash. All finite disjoint uniform Boolean factors, K>=0; H in bits, total physical influence I; all finite adaptive stopping policies and both full outcomes. Exact tensorization, rate stability, signed-bank sandwich and clipped whole/core extraction are reviewed. This does NOT accept A089's written owner proof or independently establish the separate coherent-bank theorem. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD14:39UTC; B19 leadv2; own stage20 STATUS. Fresh A080 source run {SRC.name}, CLAIMS, REPORT, complete PROOF sections1--6 and SOURCE_REVIEW. The board supersedes the prior nonempty-drift NEXT: A072 coherence is now reported independently reviewed, while initial bank price remains unpaid. Prior protocol/paper context carries forward, without new literature assertion. Current protocol revision {proto['revision']} governs exact fields. Sources and hashes saved. No peer executable imported or executed; only own previously checked direct-character/symbolic-log helpers reused.

## complete derivation or exact first unsupported line

Let R_K(v)=max((H(v)-KI(v))_+, max_j mean R_K(v_j)), constants0. A physical query has child spectral laws (a+b)^2,(a-b)^2 averaging to the parent frequency marginal. Concavity plus Shannon erasure gives mean H_child<=H_parent. Thus H is a nonnegative superharmonic majorant and0<=R_K<=H, while R_K>=H-KI; hence0<=H-R_K<=KI.

For a disjoint product, H and I add after EVERY restriction. Sum of factor hulls is a superharmonic majorant of the whole positive deficit, so R(product)<=sum R(f_i). For the reverse, take optimal finite factor policies. Continue every negative-signed-deficit zero-payoff leaf until constants: this preserves its0 payoff and makes all final signed deficits nonnegative. Run these factor policies successively on independent physical blocks. The product terminal positive deficit is then exactly their sum; expected payoff=sum factor hulls. Therefore R(product)=sum R(f_i), WITHOUT a root-sign hypothesis. This explicit zero-payoff completion is the crucial lower-bound step.

For0<=K<=L each terminal payoff difference lies in[0,(L-K)I_terminal], and expected terminal I<=I_root; maximizing proves0<=R_K-R_L<=(L-K)I. Finite policies give convex piecewise-affine functions of K, whose finite maximum remains convex piecewise affine.

For actual disjoint composition F=B(g_i), I(F)=sum q_i I_i by physical pivotality. Put D_i=H_i-R_i in[0,KI_i]. Then A=C+kappa I+sum q_i R_i=H(F)+kappa I-sum q_i D_i. Thus H+(kappa-K)I<=A<=H+kappa I. Two representations at common K,kappa differ by at most KI. Fixed-kappa unbounded A/I forces ordinary H/I unbounded, even if K varies; converse requires bounded K. This comparison does not fund repeated repartitioning from an already spent owner.

For clipped A_plus=C_plus+kappa I+sum q_i R_i, let W=sum q_i H_i. Since R_i<=H_i, A_plus<=kappa I+max(H(F),W). W/I is an influence-weighted average of the active core ratios H_i/I_i; zero-influence cores have zero H. Therefore A_plus/I-kappa<=max(H(F)/I,max_active H_i/I_i). Select the actual whole function or active core attaining that finite maximum. Divergence gives an ACTUAL Boolean ordinary-ratio counterfamily, not merely a high admission capital. Clipping's failed coherence is irrelevant to this root-only extraction.

Tensorization also shows product ratios cannot amplify finite factor ratios at fixed K,kappa: H,I,R and the product-representation bank add. The literal product of t two-bit negative-point factors has H=2t,I=t,Var=1-4^-t,R=t(2-K)_+. Its H/I stays2 although H/Var and H/(I/(2t)) diverge. These are exact normalization counterexamples, not FEI counterexamples. Source coherence is separate. First unsupported full-FEI line: INITIAL dimension-independent A<=L I on arbitrary indecomposable Boolean cores, or an actual unbounded root-ratio family. Neither is supplied.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification saved BEFORE verification by code/audit.py. All16 labelled two-bit Boolean factors,256 ordered pairs, rates0,1,2,3:1024 tensor rows. All16 two-bit outer gates/16 first cores with fixed negative-point second core, same rates:1024 signed-bank/clipped-extraction rows. Maximum physical dimension4, no symmetry reduction, constants/dummies and both outcomes retained. Independent FULL Bellman recursion uses direct character sums, separate butterfly comparison, physical edges, exact Fraction prime-log forms and integer signs; no author dual or policy code imported. Rates1 and3 include negative deficit leaves, so the lower-bound hypothesis is tested outside positive-root cases.

Command: python -B -X utf8 code/audit.py. Bounded pilot: {p['exact_assertions']} exact assertions in {p['seconds']:.3f}s. Primary: {v['exact_assertions']} exact assertions in {v['seconds']:.3f}s. Pilot counts are not added. The universal extension is proved above, not extrapolated. Both runs capped55s, estimated100MB; no >300MB job, GPU, detached job or dimension escalation. No floating-point or formal-assistant proof claimed. Exact results saved immediately.

## proof dependencies and changed downstream conclusions

Source exact statement/hypotheses/hash preserved with independent A092 acceptance. Dependencies are finite stopping induction, Fourier orthogonality, entropy concavity and actual pivotality. A080's A089 PRICE substatement overlap is credited; its proposed owner-proof sign erratum is NOT imported or independently accepted here. No sign repair is supplied in this review. A072 bank coherence is context, not a premise of the algebra/extraction. Prior A071 local envelope obstruction remains valid, but searching its already repaired signed drift is no longer the active universal gap.

## one next mathematical action and independent reviewer

{next_action} A dimension-independent initial bound or a literal diverging root ratio is the decisive deliverable. This is a source-bound handoff, not evidence of receipt or adoption.

## actual persistence receipts or precise save blocker

Four protocol files, exact helper/spec/results and rolling STATUS/WORKLOG/LEARNED saved inside A092. out/PERSISTENCE.json checks schemas, unchanged claim statement/hypotheses/hash, progress/delta bytes and all listed file hashes/sizes. No git, email, peer message, shared-index edit, brain-store write, trading access or process shedding. Supervisor mirroring remains unverified. Required wake completed with stale personal sources: owner101.1h,state85.7h,dream36.4h; brain self-care is degraded/unverified for personal continuity, excluded from proof premises. Governor log read; telemetry timestamp13:57:59 was stale and no governor was restarted. No research job left running.

## Universal bridge

This stage advances C019 initial stopping-bank payment and C024 representation auditing by independently proving exact arbitrary-factor hull tensorization and a counterexample-faithful signed/clipped-bank standard. It closes tensor amplification and wrong-normalization routes without falsely closing FEI. The initial O(I) bank price remains unpaid on arbitrary indecomposable cores; a one-state representation bound does not renew old credit. NEXT targets that initial SAME-owner price or a literal unbounded root ratio, the shortest route to full FEI because more tensor products or already repaired local drift cannot supply the missing universal bound. Full FEI remains OPEN.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
status=f'STATE: A092 stage21 saved: A080 exact tensorization/faithful signed+clipped extraction independently HOLDS;1024 tensor+1024 bank rows,{v["exact_assertions"]} exact checks PASS;FEI OPEN.\nNEXT: Price INITIAL coherent bank on indecomposable Boolean cores from SAME unused original total-influence owner,or give literal divergent root ratio;A072/A075/A089 act,A074/A092 audit;owner sign erratum separate.\n'
(HOME/'STATUS.md').write_text(status,encoding='utf-8',newline='\n')
for name,text in [('WORKLOG.md',f'2026-10-23 14:38 UTC stage21: Read latest board and A080 complete proof; previous NEXT superseded by reviewed signed coherence. Independently accepted exact tensorization including negative-leaf completion and faithful signed/clipped extraction, unchanged source version. Primary{v["exact_assertions"]} assertions,1024 tensor+1024 bank rows PASS. Initial arbitrary-core O(I) bank price remains full-FEI gap. A089 owner-proof sign erratum excluded. Four protocol files and rolling records saved; no research jobs remain.\n'),('LEARNED.md','2026-10-23 stage21: Full stopping hull of(H-KI)_+ tensorizes exactly for arbitrary disjoint Boolean factors and K>=0: complete negative-deficit zero-payoff terminal states to constants before combining optimal policies. R<=H and H-R<=KI imply H+(kappa-K)I<=signedBank<=H+kappa I. Clipped rootBank/I-kappa is bounded by max(actual whole H/I,active core H/I); divergence extracts actual Boolean counterfamily even though clipping is incoherent. Initial influence price remains FEI-equivalent. Tensor/variance/average-influence amplification cannot fake FEI divergence.\n')]:
 with (HOME/name).open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+text)
assert all('## '+x in report for x in proto['required_per_run']['report_fields'])
assert len(status.splitlines())==2 and (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[]
for x in sorted(R.rglob('*')):
 if x.is_file() and x.name!='PERSISTENCE.json':
  assert x.stat().st_size<20*1024*1024
  files.append({'path':str(x.relative_to(R)),'sha256':sha(x),'bytes':x.stat().st_size})
js(R/'out/PERSISTENCE.json',{'status':'PASS','files':files,'schemas_exact':True,'source_statement_hypotheses_hash_preserved':True,'progress_delta_byte_identical':True,'status_two_lines':True,'full_fei':'OPEN','remote_mirror':'UNVERIFIED','research_jobs_left_running':[]})
for x in files:assert sha(R/x['path'])==x['sha256']
print(json.dumps({'status':'PASS','primary':v,'claim':c['claim_id'],'hashed_files':len(files),'full_fei':'OPEN'}))
