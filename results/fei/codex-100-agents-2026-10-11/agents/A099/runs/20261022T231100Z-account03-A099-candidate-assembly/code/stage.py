"""A099 source assembly and independent prescribed-exit certificate. No background work."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,hashlib,datetime,time,sys,importlib.util

RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1]
BASE=OWN/'runs/20261021T155354Z-account03-A099-candidate-assembly'
TEAM=OWN.parents[1];REPO=Path('~/mop_fei100')
SOURCES={
 'active':TEAM/'agents/A096/runs/20261021T210221Z-account03-A096-live-gap-ledger',
 'control':TEAM/'agents/A097/runs/20261021T232544Z-account03-A097-cross-route-transfer',
 'dummy':TEAM/'agents/A073/runs/20261022T211534Z-account03-A073-certified-logarithms',
 'dummy_review':TEAM/'agents/A098/runs/20261022T220656Z-account03-A098-resource-reallocation',
 'active_review':TEAM/'agents/A082/runs/20261021T230321Z-account03-A082-finite-inequalities',
 'obstruction':TEAM/'agents/A085/runs/20261021T174013Z-account03-A085-certificate-adversary'}

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def initialize():
 for d in ['out','code']:(RUN/d).mkdir(exist_ok=True)
 spec={'helper_version':'A099-exit-source-direct-character-v1',
 'family':'F=1-2 A_a+2 A_(a+b+r), all eligible live type words; pure source continuation on exits',
 'domain':'a in {1,2}, b in {0,1}, r in {1,2}, b+r>=2; matching, increasing, reference-only-spiked source models',
 'case_count':'18 root/reference pairs; all eligible A,D,C type words and stopping cuts; three fixed exit policies plus each single-exit replacement',
 'symmetry':'No label symmetry claim; least remaining label of each type only; all-label quantifiers analytic',
 'arithmetic':'Fraction distributions/direct character sums; 12-term rational atanh log intervals with proved remainder',
 'memory_estimate_MB':100,'max_runtime_seconds':55,'pilot':'a=2,b=1,r=2 with three models',
 'sign_checks':'Full terminals, local source prices, original quota, positive signed spent-history exit reset; reference-only mass and a1 endpoints',
 'no_dimension_escalation':True,'saved_at':now()}
 save(RUN/'out/FROZEN_SPEC.json',spec)
 paths=[TEAM/'BOARD.md',TEAM/'claude/B20/STREAM_NOTES.md',OWN/'STATUS.md',Path('~/AGENTS.md')]
 paths += [REPO/'reports/fei-2026-10-11'/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
 supp=REPO/'research_pushes/2026-10-11-full-fei-100-agents'
 paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
 paths += list((supp/'sources').glob('*.md'))+list((TEAM/'context').glob('*.txt'))
 paths += [BASE/n for n in ['CANDIDATE_MANUSCRIPT.tex','CLAIMS.json','PROGRESS.json','out/PROOF_DEPENDENCIES.json']]
 for directory in SOURCES.values():
  paths += [directory/n for n in ['REPORT.md','CLAIMS.json','DERIVATION.md','REVIEW.md','PROOF.md'] if (directory/n).exists()]
 pins=[]
 for p in paths:
  raw=p.read_bytes()
  try:raw.decode('utf-8');enc='utf-8'
  except UnicodeDecodeError:raw.decode('cp1252');enc='cp1252 explicitly decoded legacy export'
  pins.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc})
 save(RUN/'out/SOURCE_RECEIPTS.json',pins)
 (RUN/'out/BOARD_SNAPSHOT.md').write_bytes((TEAM/'BOARD.md').read_bytes())
 manuscript=(BASE/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8')
 manuscript=manuscript.replace('21 October 2026; assembly version 6','23 October 2026; assembly version 7')
 manuscript=manuscript.replace('\\section{Dependencies, review and sources}',(RUN/'STAGE7_ADDITIONS.tex').read_text(encoding='utf-8')+'\n\\section{Dependencies, review and sources}')
 manuscript=manuscript.replace('Prescribed\nfresh-reference resets remain a separate signed account.',
  'Active, dummy and eligible control resets, and prescribed source resets\nat unqueried exits, are paid on the specified point-source family.\nUniversal fresh-reference payment remains a separate open account.')
 (RUN/'CANDIDATE_MANUSCRIPT.tex').write_text(manuscript,encoding='utf-8')
 claims=rd(BASE/'CLAIMS.json')
 imported=[]
 for name,identity in [('active','A096-CANONICAL-ACTIVE-RESET-SAME-ANCESTOR'),('control','A097-MIXED-ACTIVE-CONTROL-RESET-SAME-ANCESTOR'),('dummy','A073-DUMMY-DATA-RESET-SAME-ANCESTOR')]:
  c=next(x for x in rd(SOURCES[name]/'CLAIMS.json') if x['claim_id']==identity)
  if name=='active':
   for reviewer in ['control','active_review']:
    source=next(x for x in rd(SOURCES[reviewer]/'CLAIMS.json') if x['claim_id']==identity)
    c['review_records']+=source['review_records']
  c['review_records'].append({'reviewer':'A099','verdict':'RECONSTRUCTED_VALIDATION_PENDING','source':str(RUN/'STAGE7_ADDITIONS.tex'),
    'scope':'Exact original full statement reconstructed; author and independent review status remain separate'})
  imported.append(c)
 statement='For the exact A073 negative-cell family with a>=1,b>=0,r>=1,d=b+r>=2, finite normalized source reference cost c_raw<=C0 I(g), and the specified canonical live-branch active/dummy/control histories, any non-active exit may be retained unqueried and then reset once to its current original source reference (control exit), or its dummy marginal calibrated at the unchanged source vacuum (dummy exit), with point spectral controls. Its complete source cost is <=c reserved at its creating parent. Any finite pure-source continuation using marginalization/calibration and explicit constant point references costs at most that c. All executed live-branch debits and every other full terminal remain. Each converted non-active exit costs at most W+2e locally, each inherited exit at most W+8e; therefore every such mixed policy is paid by the SAME original (2C0+10)I(F)-12e_root, or leaves18e_root when all non-active exits convert. A signed reset may be positive and is not assumed free. No further query may have been executed inside an exit before its conversion; arbitrary post-query exit resets, unrelated new source references, non-point sources and extra channel/code bills are excluded. Structural source uses unchanged rate18; universal FEI remains open.'
 hypotheses=['Uniform finite Boolean negative-cell point-source family; bits and ordinary physical influence',
 'Original supplied complete source and canonical floor, d>=2; eligible controls r_current>=2',
 'Exit root has no previously executed query inside it; old live-branch debits and all complementary terminals retained',
 'Only the stated original source/marginal-calibrated exit references and pure-source continuations; no bank renewal']
 new={'claim_id':'A099-PRESCRIBED-EXIT-SOURCE-RESET','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hypotheses},sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
 'contributors':['A099'],'proof_source':str(RUN/'STAGE7_ADDITIONS.tex'),
 'proof_dependencies':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in imported],
 'review_records':[],'status':'ANALYTIC_PROOF_VALIDATION_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A096','A097','A073','A085','A094','A098','B20']}
 claims+=imported+[new];save(RUN/'CLAIMS.json',claims)
 dag=rd(BASE/'out/PROOF_DEPENDENCIES.json')
 for c in imported+[new]:
  deps=[x['claim_id'] for x in c['proof_dependencies']]
  # Full source dependencies are pinned in claims; assembly graph uses present nodes.
  dag['nodes'].append({'claim_id':c['claim_id'],'version':c['version'],'proof_dependencies':deps,
    'statement_sha256':c['statement_sha256'],'tex_label':'sec:mixedexits'})
 save(RUN/'out/PROOF_DEPENDENCIES.json',dag)
 p=rd(BASE/'PROGRESS.json');p.update(run_id=RUN.name,attempt_id='A099-assembly-v7',
  method='Source-complete mixed-reset reconstruction and original-source exit-reference transaction',
  mathematical_delta='Active/dummy/control substitutions assembled; specified exit-root source reset and full pure-source continuation fit same original bank; positive signed reset sought, universal initial pricing remains OPEN.',
  deliverable_status='CHECKPOINT_SAVED_VALIDATION_PENDING',mathematical_status='SCOPED_EXIT_SOURCE_PROOF_PENDING_VALIDATION_FULL_FEI_OPEN',
  claims_created_or_changed=[{'claim_id':c['claim_id'],'version':c['version']} for c in imported+[new]],
  source_artifacts=[str(RUN/'CANDIDATE_MANUSCRIPT.tex'),str(RUN/'STAGE7_ADDITIONS.tex'),str(RUN/'out/SOURCE_RECEIPTS.json')],
  next_consumers=new['next_consumers'],next_action='A097/A094 audit prescribed exit-source transaction, then price a prescribed reset AFTER an actual exit query with the SAME old debits and other complete terminals; no fresh source.',
  stagnant_substantive_attempts=0,blockers=['Universal influence-priced source/reference construction open','Post-query exit reset not covered','Two integrated-chain audits pending'],packet_ids=['A099'])
 p['claim_versions_used'] += [{'claim_id':c['claim_id'],'version':c['version']} for c in imported]
 save(RUN/'PROGRESS.json',p);save(RUN/'PACKET_DELTA.json',p)
 report='''# A099 version 7 checkpoint

## exact target, quantifiers, hypotheses and units

Assemble the full supported chain and advance its prescribed reset boundary. Uniform finite Boolean signs, bits, ordinary physical influence. The new scoped target is a reset at an unqueried retained non-active exit to its original source reference (or specified marginal/calibration), retaining all old live-branch debits and other full terminals. This is not an arbitrary incoming-profile or universal cheap-reference theorem. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Entire execution-v2 protocol and current board (2026-10-22 23:09 UTC), B20 notes v2, own v6 source/status consumed. Mandatory campaign ledgers, plan, supplemental sources and four explicitly decoded local paper exports are pinned in out/SOURCE_RECEIPTS.json; paper claims are context, not new premises. Critical originals are A09620261021T210221Z DERIVATION1--4, A09720261021T232544Z DERIVATION1--7, A07320261022T211534Z DERIVATION1--5. A097 and A082 exact scoped active-reset reviews are consumed. A098 accepts only the local dummy substitution and conditional global algebra; it is not counted as a full upstream review. A085 absolute-TV obstruction is respected. Stale lead's original assembly chain is retained, with this source-complete new dependency. Wake self-care is degraded: attachment lock timeout, owner model85.6h and state-of-mind70.2h stale; user alerted, affected notes not mathematical premises.

## complete derivation or exact first unsupported line

STAGE7_ADDITIONS.tex reconstructs all active/control/dummy local substitutions. Proper active steps release e from the virtual envelope W=c+10eL; final active step uses an explicit point spectrum. Each non-active step with inherited off-reference costs <W+8e. Original reserve at d=b+r>=2 is >=5a*2^d e_root; reach*e is invariant, so at most d-1 non-active charges leave>=12e_root at unchanged rate2C0+10 (18 structurally).

New transaction: a retained non-active exit, before any query inside it, may reset to the ORIGINAL source reference with vacuum controls, or its specified dummy marginal/calibration. Its full cost is <=c, already reserved at its creating parent. Any finite pure-source marginal/calibrated continuation (explicit constant points) has full erasure/terminal ledger<=c. Replacing the inherited off-bill by this WHOLE source-tree bill lowers its conservative surcharge to<2e; when all non-active exits convert, reserve>=18e_root. Previously executed live-branch erasures and all other full terminal costs remain. A delayed exit-root reset is permitted while it stays unqueried; no source budget is renewed. A positive reset is paid, not assumed nonpositive.

First unsupported universal line: pay a newly prescribed reset after queries already executed INSIDE an exit, while its sibling keeps its original inherited terminal; or construct a cheap complete source reference for arbitrary non-point Boolean functions. Extra channels/codes are outside this erasure/CE mechanism. Four universal conjectures and both independent integrated audits stay open.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes search. Planned independent direct-character/Fraction checker uses rational12-term atanh enclosures; pilot a2,b1,r2 with three references, then frozen18 roots, all eligible type words/stopping cuts, old debits, both full terminals, a1 and reference-only mass. Fixed policies keep all exits, convert all exits, and convert each one individually with a pure-source physical query. Positive signed spent-history conversion is an explicit falsifiable coverage requirement. Status: validation pending. Estimate100MB, cap55s, no heavy/GPU/detached work or dimension escalation. No Mathlib/Lean job is launched on the low-memory box; the former timed-out bookkeeping check is not rerun or promoted to certification.

## proof dependencies and changed downstream conclusions

v6 original statements are preserved; new source versions are pinned unchanged. A096 active reset has two external scoped reviews; A097 mixed-control and A073 full mixed-history chains receive independent A099 reconstruction only after validation. A098 local-only acceptance is not widened. The new A099 exit-source theorem is author proved and pending independent review. It extends a reference mechanism on a known point-source/read-once family, not universal FEI. No universal constant improves, and historical C024 is not identified with this finite-tree interface.

## one next mathematical action and independent reviewer

A097/A094 (alternate A085) independently audit the exact exit-source reset, then exercise one prescribed fresh reference AFTER a physical query inside a converted or inherited exit, using the SAME old debit and both complete terminals. A085/A094 remain named integrated-chain reviewers; fragment acceptance does not close either full audit.

## actual persistence receipts or precise save blocker

Four protocol files, single-source TeX, new full proof, frozen spec, code and source pins saved in this assigned run. Rolling STATUS two lines, WORKLOG append and LEARNED final update maintained. Supervisor copy/canonical adoption/mirrors unverified; no git, shared-tree, other-agent or brain-content write. Mandatory wake/checklist hooks are exceptions. Mathematical validation and final artifact receipts pending at this checkpoint.

## Universal bridge

C024 finite history transfer and C019 stopping payment advance from no-reset v6 to source-complete active/dummy/control substitutions and a specified retained exit-root source reset, always using one original quota. The extra exit transaction costs<2e locally and permits complete pure-source continuations, with>=18e_root spare when all exits convert; inherited-exit policies retain>=12e_root. Universal FEI improvement is zero: arbitrary initial source pricing, post-query exit resets and both integrated audits remain unpaid. NEXT is the reset after an actual exit query with old debit and the other terminal retained, because that is the first source-reference change not paid by this same-envelope substitution.
'''
 (RUN/'REPORT.md').write_text(report,encoding='utf-8')
 (OWN/'STATUS.md').write_text('STATE: A099 v7 checkpoint saved: mixed-reset chain and prescribed exit-source reset proof; exact validation pending; FEI OPEN.\nNEXT: Validate positive signed spent-history exit reset; A097/A094 audit, then pay reset after an actual exit query from SAME old bank and both terminals.\n',encoding='utf-8')
 with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now()+': v7 checkpoint; complete mixed-reset sources consumed; derived prescribed unqueried exit-source reset/full source continuation at same original quota, with old live debits retained. Validation pending.\n')
 print(json.dumps({'checkpoint':'SAVED','sources':len(pins),'claims':len(claims)}))

# Standalone interval arithmetic; all values and every tail bound are rational.
COUNT=0;START=0
def ck(x):
 global COUNT
 COUNT+=1
 assert x,COUNT
 assert time.monotonic()-START<55,'frozen runtime exceeded'
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def times(a,x):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def minus(x,y):return plus(x,times(F(-1),y))
def outward(x):
 D=1<<72
 return F(x[0].numerator*D//x[0].denominator,D), F(-((-x[1].numerator*D)//x[1].denominator),D)
@lru_cache(None)
def lnunit(q):
 z=(q-1)/(q+1);N=12
 s=2*sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
 rem=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
 return s,s+rem
@lru_cache(None)
def log2(q):
 assert q>0
 k=0
 while q>=2:q/=2;k+=1
 while q<1:q*=2;k-=1
 lo,hi=lnunit(q);a,b=lnunit(F(2))
 return outward((F(k)+lo/b,F(k)+hi/a))
@lru_cache(None)
def ce(p,q):
 ans=(F(0),F(0))
 for a,b in zip(p,q):
  if a:
   assert b>0
   ans=plus(ans,times(-a,log2(b)))
 return outward(ans)
@lru_cache(None)
def spectrum(f):
 N=len(f)
 return tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)),N)**2 for s in range(N))
def insert(x,j,b):return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)
def restrict(f,j,b):return tuple(f[insert(x,j,b)] for x in range(len(f)//2))
def marginal(q,j):return tuple(q[insert(t,j,0)]+q[insert(t,j,1)] for t in range(len(q)//2))
def calibration(q,mass):
 ck(q[0]<1 and mass<1)
 return (mass,)+tuple(x*(1-mass)/(1-q[0]) for x in q[1:])
def influence(f):
 N=len(f);n=N.bit_length()-1
 return F(sum(f[x]!=f[x^(1<<j)] for x in range(N) for j in range(n)),N)
def model(a,b,r,R):
 n=a+b;N=1<<n;L=n+r;s=F(1,1<<a);t=F(1,N);e=F(2,1<<L);mu=1-2*s
 f=tuple(1-2*int((x&((1<<a)-1))==0)+2*int(x==0) for x in range(1<<L))
 g=tuple(1-2*int((x&((1<<a)-1))==0) for x in range(N));pg=spectrum(g);p=spectrum(f)
 M=tuple(sum(p[T+U*N] for U in range(1<<r)) for T in range(N))
 Re=tuple((1-e/s)*R[T]+(e/s)*mu*int(T==0)+2*e*t for T in range(N))
 Q=tuple(Re[x%N]*p[x]/M[x%N] for x in range(len(p)))
 ck(all(v>0 for v in M) and sum(Q)==1 and sum(Re)==1)
 ck(influence(f)==2*a*s+e*(b+r-a))
 c=ce(pg,R);W=plus(c,(10*e*L,10*e*L));rootce=ce(p,Q)
 ck(rootce[1]<=W[0])
 return f,g,pg,Q,c,W,e
def source_reference(a,b,kind):
 n=a+b;N=1<<n;s=F(1,1<<a);mu=1-2*s
 g=tuple(1-2*int((x&((1<<a)-1))==0) for x in range(N))
 if kind=='matching':return spectrum(g)
 weights=[F(x+1) for x in range(1,N)]
 if kind=='spiked':weights=[F(1)]*(N-1);weights[-1]=F(4096)
 den=sum(weights)
 return (mu*mu,)+tuple((1-mu*mu)*w/den for w in weights)
@lru_cache(None)
def exact_helper():
 helper=BASE/'code/check_transport.py'
 module_spec=importlib.util.spec_from_file_location('a099_v6_exact_log',helper)
 exact=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(exact)
 return exact

def source_tree_cost(f,q):
 # One actual pure-source query; both resulting full references retained.
 if len(f)==1:return ce(spectrum(f),q)
 p=spectrum(f);j=0;v=marginal(q,j);m=marginal(p,j)
 B=minus(ce(p,p),ce(m,m));children=[spectrum(restrict(f,j,b)) for b in range(2)]
 costs=times(F(1,2),plus(ce(children[0],v),ce(children[1],v)))
 result=plus(B,costs)
 # Prove a sign by separated rational bounds, or an exact prime-log equality.
 gap=minus(ce(p,q),result)
 if gap[0]>=0:ck(True)
 else:
  exact=exact_helper()
  bv=exact.add(exact.entropy(p),exact.scale(F(-1),exact.entropy(m)))
  tv=exact.scale(F(1,2),exact.add(*(exact.ce(child,v) for child in children)))
  ck(exact.add(exact.ce(p,q),exact.scale(F(-1),bv),exact.scale(F(-1),tv))=={})
 return result
def words(a,b,r,prefix=''):
 yield prefix
 if a>=2:yield from words(a-1,b,r,prefix+'A')
 if a==1:yield prefix+'A'
 if b:yield from words(a,b-1,r,prefix+'D')
 if r>=2:yield from words(a,b,r-1,prefix+'C')

def certify(pilot=False):
 global START,COUNT
 START=time.monotonic();COUNT=0;roots=histories=local=0;positive=[];nonactive=0
 params=[(2,1,2)] if pilot else [(a,b,r) for a in [1,2] for b in [0,1] for r in [1,2] if b+r>=2]
 for a0,b0,r0 in params:
  for kind in ['matching','increasing','spiked']:
   R0=source_reference(a0,b0,kind);root=model(a0,b0,r0,R0);f0,g0,pg0,q0,c0,W0,e0=root
   Ig=influence(g0);C0=F(4 if kind=='matching' else 32);K=2*C0+10;quota=K*influence(f0)
   ck(c0[1]<=C0*Ig)
   roots+=1
   for word in words(a0,b0,r0):
    histories+=1;a,b,r=a0,b0,r0;R=R0;rho=F(1);debit=(F(0),F(0));exits=[];converted=[];live=root
    for depth,letter in enumerate(word):
     f,g,pg,Q,c,W,e=live;n=a+b
     j=0 if letter=='A' else (a if letter=='D' else n)
     p=spectrum(f);m=marginal(p,j);v=marginal(Q,j)
     B=minus(ce(p,p),ce(m,m));debit=plus(debit,times(rho,B))
     off=restrict(f,j,1);on=restrict(f,j,0);poff=spectrum(off);oldoff=ce(poff,v)
     ck(sum(v)==1 and all(not x or y>0 for x,y in zip(poff,v)))
     if letter=='A':
      target=(F(1),)+tuple(F(0) for _ in range(len(off)-1));sourcecost=ce(poff,target)
      ck(sourcecost==(F(0),F(0)))
     else:
      nonactive+=1
      sourceR=R if letter=='C' else calibration(marginal(R,j),pg[0])
      newn=n if letter=='C' else n-1;remainingcontrols=r-1 if letter=='C' else r
      target=tuple(sourceR[x] if x<(1<<newn) else F(0) for x in range(len(off)))
      sourcecost=source_tree_cost(off,target)
      reset=minus(ce(poff,target),oldoff)
      if reset[0]>0 and depth>=1 and influence(off)>0 and influence(on)>0:
       positive.append({'root':[a0,b0,r0,kind],'history':word[:depth+1],
        'signed_reset_lower':str(reset[0]),'signed_reset_upper':str(reset[1]),'prior_debit_lower':str(debit[0]-rho*B[0]),
        'old_off_CE_upper':str(oldoff[1]),'target_root_CE_lower':str(ce(poff,target)[0])})
     exits.append(times(rho/2,oldoff));converted.append(times(rho/2,sourcecost))
     local+=1
     if letter=='A' and a==1:
      poin=spectrum(on);livecost=ce(poin,poin);rho/=2;a=0
      break
     if letter=='A':a-=1;R=calibration(marginal(R,j),(1-F(2,1<<a))**2)
     if letter=='D':b-=1;R=calibration(marginal(R,j),(1-F(2,1<<a))**2)
     if letter=='C':r-=1
     nextlive=model(a,b,r,R)
     ck(nextlive[0]==on and nextlive[6]==2*e)
     offCE=sourcecost if letter!='A' else oldoff
     ck(plus(B,times(F(1,2),plus(offCE,nextlive[5])))[1] < W[0]+(2 if letter!='A' else 0)*e if letter!='A' else plus(B,times(F(1,2),plus(offCE,nextlive[5])))[1]<=W[0])
     live=nextlive;rho/=2;livecost=ce(spectrum(live[0]),live[3])
    if not word:livecost=ce(spectrum(f0),q0)
    retained=plus(debit,times(rho,livecost));allold=retained;allnew=retained
    for x in exits:allold=plus(allold,x)
    for x in converted:allnew=plus(allnew,x)
    ck(allold[1] <= quota-12*e0)
    ck(allnew[1] <= quota-18*e0)
    ck(allold[1] <= W0[0]+8*(b0+r0-1)*e0)
    ck(allnew[1] <= W0[0]+2*(b0+r0-1)*e0)
    for i in range(len(exits)):
     single=retained
     for j,x in enumerate(exits):single=plus(single,converted[j] if j==i else x)
     ck(single[1]<=quota-12*e0)
    # Actual prior debit is included in every variant, never canceled or renewed.
 ck(bool(positive))
 result={'status':'PASS','pilot':pilot,'roots':roots,'histories':histories,'local_queries':local,'nonactive_queries':nonactive,
  'exact_assertions':COUNT,'positive_spent_nonconstant_exit_resets':len(positive),'positive_witness':positive[0],
  'seconds':time.monotonic()-START,'arithmetic':'Fraction/direct character sums and rigorous rational log enclosures',
  'scope':'Frozen fixed-label finite cases verify implementation; full quantifiers follow analytic proof, not extrapolation'}
 save(RUN/('out/PILOT.json' if pilot else 'out/EXACT_EXIT_RESET.json'),result)
 print(json.dumps({k:v for k,v in result.items() if k!='positive_witness'}))

if __name__=='__main__':
 if sys.argv[1]=='init':initialize()
 elif sys.argv[1]=='pilot':certify(True)
 elif sys.argv[1]=='main':certify(False)
