from pathlib import Path
from fractions import Fraction as F
import json, hashlib, time, copy

BASE=Path(__file__).resolve().parent
if BASE.name=='code': BASE=BASE.parents[2]
RUNID='20261023T144436Z-fleet03-A033-derivative-hierarchy'
RUN=BASE/'runs'/RUNID
SRC=BASE.parent/'A031'/'runs'/'20261023T135224Z-fleet03-A031-convolution-identity'
SRC35=BASE.parent/'A035'/'runs'/'20261023T132111Z-fleet03-A035-signed-cancellation-countersearch'
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return p.read_text(encoding='utf-8-sig')
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def js(p,o): write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
RUN.mkdir(parents=True,exist_ok=True)
for d in ['code','out']: (RUN/d).mkdir(exist_ok=True)
write(RUN/'code'/'review.py',read(Path(__file__)))
spec={'helper_version':'A033-final-review-v1','helper_sha256':sha((RUN/'code'/'review.py').read_bytes()),'actual_Boolean_family':'Three explicitly supplied 3-bit truth tables: x*pointdefect2, selector(pointdefect2,character), dummy*pointdefect2','parameter_domain':'fixed labelled tables; sharpness s=1/16,1/8,1/4; one singly occupied generic ghost fixture','case_count':'3 truth tables,3 sharpness parameters,1 generic ghost fixture; no search','symmetry':'none','arithmetic':'exact integer Walsh/direct characters, Fraction, symbolic prime logarithms, analytic integral bounds; no floats used for signs','memory_estimate_MB':40,'maximum_runtime_seconds':55,'purpose':'Independent bounded certificate review, not a new campaign search'}
js(RUN/'FROZEN_SPEC.json',spec)
t0=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x
def spectrum(v):
 n=len(v); a=list(v);step=1
 while step<n:
  for i in range(0,n,2*step):
   for j in range(i,i+step): a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
  step*=2
 direct=[sum(v[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(n)) for s in range(n)]
 ck(a==direct)
 for u in range(n): ck(sum(a[s]*a[s^u] for s in range(n))==(n*n if u==0 else 0))
 return [F(z,n) for z in a]
def logs(q):
 out={}
 for v,sgn in [(q.numerator,1),(q.denominator,-1)]:
  k=2
  while k*k<=v:
   while v%k==0:out[k]=out.get(k,0)+sgn;v//=k
   k+=1
  if v>1:out[v]=out.get(v,0)+sgn
 return {k:F(v) for k,v in out.items() if v}
def add(*terms):
 out={}
 for c,d in terms:
  for k,v in d.items():out[k]=out.get(k,F(0))+c*v
 return {k:v for k,v in out.items() if v}
def kl(p,q):
 return add(*[(a,logs(a/b)) for a,b in zip(p,q) if a])
def phi(pp,pm,m,blocks,rp,rm):
 total=F(0)
 for z,b in enumerate(blocks):
  ap=sum(pp[i] for i in b);am=sum(pm[i] for i in b)
  if ap and am:
   e=sum(abs(rp[z]*pp[i]/ap+rm[z]*pm[i]/am-2*m[i]) for i in b)
   total+=e*e/(4*(rp[z]**2/ap+rm[z]**2/am))
  elif ap or am:
   p,a,r=(pp,ap,rp[z]) if ap else (pm,am,rm[z])
   o=sum(max(F(0),r*p[i]/a-2*m[i]) for i in b)
   total+=a*o*o/(r*r)
 return total

g=[-1,1,1,1]; ch=[1,-1,1,-1]
parents=[[(-1 if x&1 else 1)*g[x>>1] for x in range(8)], [g[x>>1] if x%2==0 else ch[x>>1] for x in range(8)], [g[x>>1] for x in range(8)]]
for v in parents:
 full=spectrum(v); plus=spectrum(v[::2]);minus=spectrum(v[1::2])
 for i in range(4):
  ck(full[2*i]==(plus[i]+minus[i])/2)
  ck(full[2*i+1]==(plus[i]-minus[i])/2)
  ck(full[2*i]**2+full[2*i+1]**2==(plus[i]**2+minus[i]**2)/2)
 ck(sum(full[2*i+1]**2 for i in range(4))==F(sum(v[2*i]!=v[2*i+1] for i in range(4)),4))
 ck(all(a*a==F(1,4) for a in spectrum(g)))
p=[F(1,4)]*4
for s in [F(1,16),F(1,8),F(1,4)]:
 m=[(1+2*s)/4]*2+[(1-2*s)/4]*2
 ck(sum(m)==1 and min(m)>0)
 ck(phi(p,p,m,[list(range(4))],[F(1)],[F(1)])==2*s*s)
 # Exact prime-log derivation of M=-log2(1-4s^2)/2.
 ck(kl(p,m)==add((F(-1,2),logs(1-4*s*s))))
 # Parent query is deterministic in Fourier occupancy; carried references unchanged.
 ck(add((1,kl(p,m)),(-1,kl(p,m)))=={})
 # Integral sharpness bracket: 1 <= (M ln2)/Phi <= 1/(1-4s^2).
 ck(0<4*s*s<1 and 1/(1-4*s*s)>1)
pp=[F(1),F(0),F(0)];pm=[F(0),F(0),F(1)]
m=[F(1,8),F(3,8),F(1,2)];r=[F(1,2)]*2
ck(phi(pp,pm,m,[[0,1],[2]],r,r)==F(1,4))
rp=[F(1,4),F(1,4),F(1,2)];rm=[F(0),F(1,2),F(1,2)]
ck(sum(rp)==sum(rm)==1)
ck(all((x+y)/2==z for x,y,z in zip(rp,rm,m)))
ck(add((F(1,2),kl(pp,rp)),(F(1,2),kl(pm,rm)))=={2:F(3,2)})
# Optimality: occupied plus reference at atom0 <=2m0=1/4; minus atom2 fixed1/2.
ck(rp[0]==2*m[0] and rp[2]==rm[2]==F(1,2))
ck(F(1,2)*F(1,2)==F(1,4)) # gap ln2/2 >=1/4 from integral ln2>=1/2

# Independent exact KKT reconstruction of A035's positive apparent/negative full debit.
pp=[F(1,4)]*4;pm=[F(0),F(1),F(0),F(0)]
rp=[F(5,12),F(1,12),F(1,4),F(1,4)]
rm=[F(1,12),F(5,12),F(1,4),F(1,4)]
ck([(-a/b+c/d) for a,b,c,d in zip(pp,rp,pm,rm)]==[F(-3,5),F(-3,5),F(-1),F(-1)])
M=add((F(1,2),kl(pp,rp)),(F(1,2),kl(pm,rm)))
ck(M==add((F(1,8),logs(F(186624,3125)))))
ck(186624>16*3125 and 186624<256*3125 and 729>256)
elapsed=time.perf_counter()-t0
ck(elapsed<55)
js(RUN/'out'/'validation.json',{'verdict':'PASS','exact_assertions':checks,'runtime_seconds':elapsed,'domain':spec['case_count'],'formal_compiler':'NOT_LAUNCHED','scope':'Independent fixtures and analytic proof reconstruction; no exhaustive-domain claim'})

derivation='''# Independent final review: quantitative compatible-reference tariff

Verdict: A031-QUANTITATIVE-FINE-COMPATIBILITY-TARIFF@1 HOLDS at its stated generic, supplied-source scope, without repair. A035-MISMATCHED-MEAN-FINE-ATTAINABILITY@1 likewise HOLDS; it already supplies the arbitrary-mean extension contemplated by A033. No duplicate theorem is opened. A031 independently accepted A033's previous actual-midpoint criterion unchanged; that incoming review is preserved separately.

## Independent proof reconstruction
Write d_tau=R_tau/r_tau-kappa_tau in an occupied block. Subtracting coarse KL leaves exactly (1/2)sum a_tau D(kappa_tau||kappa_tau+d_tau). In natural units binary log-sum and the curvature 1/[x(1-x)]>=4 give at least (1/4)sum a_tau ||d_tau||_1^2. Let E_tau=r_tau*d_tau. In a doubly occupied block compatibility forces E_++E_-=-e. Minimize the quadratic lower bound under the scalar relaxation x_++x_->=||e||_1, x_tau=||E_tau||_1. Its exact reciprocal-weight minimum is ||e||_1^2/(4W), W=sum r_tau^2/a_tau. This independently reconstructs the tariff by a two-variable quadratic minimization. In a singly occupied block compatibility forces R_tau<=2m. The excess ideal mass o must move out of violating atoms. Since E_tau has zero block total, its L1 norm is at least2o, giving a_tau*o^2/r_tau^2. Empty actual blocks cost zero. Positive denominators follow from finite coarse KL. Summing proves the stated Phi bound for every feasible pair and hence its finite minimum.

Phi vanishes precisely when the doubly occupied pointwise equality and singly occupied domination tests hold. Equality in conditional Gibbs fixes the entire occupied conditional, including actual-zero atoms. The free sibling is its componentwise residual in singly occupied blocks; wholly empty blocks can be allocated proportionally to m. This gives A035 necessity and sufficiency. The proportional-m candidate is finite; compactness and lower semicontinuity make a failed equality test a strictly positive minimum gap.

For sharpness let p uniform4 and f=x*pointdefect2. Both actual child spectra equal p and physical influence is1. With one block, r_tau=1 and m=((1+2s)/4 twice,(1-2s)/4 twice), Jensen gives the optimizer R_+=R_-=m. Exact M ln2=-ln(1-4s^2)/2 and Phi=2s^2. Put z=4s^2. Integrating 1/(1-t) on[0,z] gives z<=-ln(1-z)<=z/(1-z); thus the ratio is squeezed between1 and1/(1-z), tending to1. No larger uniform multiplier is possible. This is an analytic continuum argument, not an extrapolation from finite samples.

The parent spectrum is wholly on queried-bit-present labels. Set full Q there equal to m and zero elsewhere. Its conditional occupancy matches the actual deterministic occupancy; B=JS=rho=0. Old full KL equals M, so the full transaction M-JS-Dold-rho is exactly ZERO. A positive fine minimum here prices existing mismatch, not a new debit.

For the additional singly occupied fixture p+=(1,0,0),p-=(0,0,1), m=(1/8,3/8,1/2), blocks{0,1}|{2}, both declared profiles(1/2,1/2), Phi=1/4 nats. The exact optimum R+=(1/4,1/4,1/2),R-=(0,1/2,1/2) has M=3/2 bits,L=1 bit. Feasibility bounds its sole occupied first-block atom by1/4, proving optimality directly. The bound gap*ln2>=1/4 follows from ln2>=1/2 by integrating1/t on[1,2]. This checks the reference-only-atom and singly occupied branch independently.

For every physical node H(P)=B+mean H(p_tau)+JS. Therefore the full increment is M-JS-D(P||Q), with D(P||Q)=D(actual marginal||m)+rho. Multiplying by actual reach and summing telescopes complete CE and erasure costs, retaining all negative terms and old U. This proves A031's necessary tree test from a genuinely original margin; it does not assert a universal need for that declared class. When r_+=r_-=pi(m), unchanged R_tau=m is feasible, so the minimum net increment is <=-rho. This free-continuation guard remains decisive.

## Exact hierarchy and imported obstructions
Complete Booleanity means sum_S fhat(S)fhat(S xor U)=1{U=empty} for EVERY shift U, at EVERY physical restriction; equivalently every restricted truth table squares to1. The full derivative D_T has values in 2^(1-|T|)Z intersect[-1,1], with all the corresponding full convolution identities. Finite derivative/order prefixes and a dyadic grid alone are not admission. The previously source-audited fixed-order dyadic real controls have I=w+3/4 and B/I growing as log K/(4w+3), while all square-spectrum shifts of degrees1 through2w-1 vanish. Small norm/square-defect variants were already ruled out. The separate cyclic atom-cap-prefix original family/checker remains missing locally; no exact parameterization is invented. This stage adds no new Booleanity admission inequality: the tariff is valid for generic normalized laws and fails the lead's requirement for a specifically Booleanity-derived bound.

## First unsupported universal line
A universal construction must identify a mathematically required compatible reference class and pay its full reached minimum, less actual JS, old mismatch and occupancy, from the SAME unused influence-priced original owner after old debits and both full terminals. Alternatively it must construct an O(I(core)) initial complete reference for arbitrary Boolean cores without circular FEI admission. No such step is proved here. Fixed-prefix, optional-conversion and zero-refund-depth loops remain retired. Full FEI OPEN.
'''
write(RUN/'DERIVATION.md',derivation)
sourceclaims=json.loads(read(SRC/'CLAIMS.json'))
selected=[]
for cid in ['A031-QUANTITATIVE-FINE-COMPATIBILITY-TARIFF','A035-MISMATCHED-MEAN-FINE-ATTAINABILITY','A033-NONISOSPECTRAL-COMPATIBILITY-ATTAINMENT']:
 c=copy.deepcopy(next(c for c in sourceclaims if c['claim_id']==cid))
 assert sha(c['exact_statement'].encode('utf-8'))==c['statement_sha256']
 if cid.startswith('A031'): assert sha((SRC/'DERIVATION.md').read_bytes())==c['proof_source']['sha256']
 if cid.startswith('A035'): assert sha((SRC35/'DERIVATION.md').read_bytes())==c['proof_source']['sha256']
 if not cid.startswith('A033'):
  c['review_records'].append({'reviewer':'A033','run_id':RUNID,'verdict':'HOLDS_NO_REPAIR_AT_STATED_SCOPE','method':'Independent quadratic minimization/conditional equality proof; exact signed Boolean and rational boundary certificates','artifacts':['DERIVATION.md','code/review.py','out/validation.json'],'scope':'Generic supplied-reference geometry only; no initial source or class necessity'})
  c['status']='INDEPENDENT_SCOPED_REVIEW_HOLDS_NO_REPAIR'
 selected.append(c)
js(RUN/'CLAIMS.json',selected)
proto=json.loads(read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')))
progress={'protocol_revision':proto['revision'],'run_id':RUNID,'stream':'B07','packet_id':'A033','gap_id':'REQUIRED-COMPATIBLE-CLASS-OR-ORIGINAL-CORE-SOURCE','attempt_id':'final-quantitative-tariff-independent-review','method':'Consume useful new peer dependencies; exact finite certificates and complete proof reconstruction; no new broad candidate','mathematical_delta':'A031 optimal quantitative fine tariff and A035 arbitrary inherited-mean criterion independently HOLD; A031 incoming acceptance of A033 criterion preserved; complete old-KL cancellation retained','deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_THEOREMS_REVIEWED_FULL_FEI_OPEN','claim_versions_used':[c['claim_id']+'@'+str(c['version']) for c in selected],'claims_created_or_changed':['Independent review records only; original statements and contributors unchanged'],'source_artifacts':[str(SRC/'DERIVATION.md'),str(SRC/'CLAIMS.json'),str(SRC35/'DERIVATION.md')],'next_consumers':['A031','A035','A096','A097','A094','B07','B20'],'next_action':'Specify a truly REQUIRED compatible arbitrary-core class and pay its full signed minimum from SAME unused original owner, or construct a noncircular influence-priced original core source.','stagnant_substantive_attempts':0,'blockers':['Universal required class and original supplier absent','Original cyclic atom-cap-prefix family/checker still absent locally','Remote supervisor adoption unverified','Brain self-care degraded: attachment lock failure; owner model101.2h/state85.8h/dream36.5h stale'],'packet_ids':['A033']}
js(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',read(RUN/'PROGRESS.json'))
report=''
parts=[
('exact target, quantifiers, hypotheses and units','Independently review A031 quantitative compatibility tariff for arbitrary finite complete child laws and supplied full inherited mean, plus A035 attainability criterion. Full fine-mean compatibility and prescribed profiles are explicit extra obligations. KL/CE bits, Phi nats. Full FEI remains OPEN.'),
('sources actually read, revisions and theorem locators','BOARD dated2026-10-23 14:50 UTC; B07 STREAM_NOTES v2; own STATUS; EXECUTION_PROTOCOL v2 read completely; machine AGENTS; A031 20261023T135224Z DERIVATION sections1-4 and CLAIMS; A035 20261023T132111Z DERIVATION sections1-4; own prior12:30 DERIVATION/CLAIMS. See SOURCE_MANIFEST for exact hashes. Previous-stage imports are identified as such, not freshly reread papers. Wake disclosed attachment integrity failure and stale personal context; those notes are not proof premises.'),
('complete derivation or exact first unsupported line',derivation+'\nNo new Booleanity-specific consequence is claimed. Independent proofs required no repair; source contributors unchanged.'),
('executed validation with domain, arithmetic, commands and outputs','Frozen FROZEN_SPEC written before certificate checks. Command: python -B -X utf8 final_stage_144436.py; reproducible as python -B -X utf8 runs/'+RUNID+'/code/review.py (script locates A033 root). Exact actual truth tables, full all-shift signed convolution, independent direct Walsh sums, physical influence, symbolic prime-log KL and rational KKT. See out/validation.json for actual assertion count/runtime. No broad search, floating sign, heavy job or Lean claim. Estimated40MB, so300MB memok trigger not reached. Initial broad source output was truncated; A031/A035 proofs and exact claims were subsequently retrieved in full. Initial PowerShell source intake omitted explicit encoding; mathematical sources were reread explicitly UTF8 before source binding.'),
('proof dependencies and changed downstream conclusions','Three exact original statements retained with SHA checks; A031/A035 receive independent A033 no-repair reviews; A033 incoming no-repair peer acceptance retained. Sharpness multiplier1 is optimal for arbitrary supplied means, including positive-influence actual Boolean children, but its complete transaction is zero. Positive gap alone cannot charge a new account. No universal source or FEI closure follows.'),
('one next mathematical action and independent reviewer',progress['next_action']+' Consumers/reviewers A096/A097 specify required class and original payer; A094 audits full owner ledger. A031/A035 consume this review. The campaign deadline14:49UTC had already passed at source intake; this is a bounded final review/handoff, not a restarted campaign.'),
('actual persistence receipts or precise save blocker','All research writes remain inside A033. out/PERSISTENCE_RECEIPT.json records schemas, statement hashes and every saved-file SHA; it is reread and checked after creation. Supervisor publication/mirror adoption UNVERIFIED. No git or brain write, mail, remote compute, workers or detached work. Brain context degraded as disclosed.\n\nREPORT done: bounded independent tariff/attainability review and exact certificates.\nREPORT stopped: no broad search launched; full FEI open.\nREPORT left running: none.')]
for i,(h,b) in enumerate(parts,1):report+=f'# {i}. {h}\n\n{b}\n\n'
report+='# Universal bridge\n\nThis stage moves the C019 stopping-tree/C024 history-transfer accounting interface by independently accepting an explicit sharp lower tariff for a declared full-compatible class and the exact arbitrary-mean attainment test; it adds zero to a universal FEI constant and no initial source bound. Actual JS, inherited mismatch, occupancy, negative terms, old bookings and both complete terminals remain. The shortest remaining route is a required arbitrary-core class with an actually unused original influence payer, or a noncircular initial source; another optional reset, deeper prefix or granularity relaxation cannot bridge that gap.\n'
write(RUN/'REPORT.md',report)
write(BASE/'STATUS.md','STATE: Final stage saved: A031 sharp fine tariff/A035 arbitrary-mean criterion independently HOLD; A031 accepted A033 criterion unchanged; exact certificates PASS; full FEI OPEN.\nNEXT: A096/A097 specify REQUIRED compatible arbitrary-core class and SAME unused original payer, or noncircular O(I(core)) initial reference; A094 audits old KL/JS/occupancy/full terminals.\n')
for name,line in [('WORKLOG.md',f'\n2026-10-23 final14:44 stage: consumed fresh14:50 board; avoided duplicating A035 generalization. Independently reconstructed A031 optimal quantitative tariff and A035 criterion without repair; exact bounded certificates PASS. Incoming A031 acceptance of prior A033 theorem preserved. Campaign deadline passed before source intake; saved final scoped handoff, no new broad search. Full FEI OPEN. Brain wake degraded and disclosed. Run{RUNID}.\n'),('LEARNED.md','\n2026-10-23 final: A031 quantitative bound (M-L)ln2>=sum_double ||r+kappa+ +r-kappa- -2m||1^2/[4 sum r_tau^2/a_tau]+sum_single a_tau*(sum(r_tau*kappa_tau-2m)_+)^2/r_tau^2 independently reconstructed. Universal multiplier1 sharp even actual Boolean f=x*pointdefect2, but sharpness full transaction0 after old KL. A035 already proves arbitrary-mean equality criterion. If both prescribed profiles equal inherited coarse mean, unchanged full references are feasible, so min net<=-actual occupancy KL. A positive fine gap cannot alone be a new required debit.\n')]:
 with (BASE/name).open('a',encoding='utf-8') as f:f.write(line)
sourcepaths=[SRC/'DERIVATION.md',SRC/'CLAIMS.json',SRC35/'DERIVATION.md',BASE/'runs'/'20261023T123045Z-fleet03-A033-derivative-hierarchy'/'CLAIMS.json',Path(r'BOARD.md'),Path(r'claude\B07\STREAM_NOTES.md')]
js(RUN/'out'/'SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p.read_bytes())} for p in sourcepaths])
assert set(progress)==set(x.split(' (')[0] for x in proto['required_per_run']['progress_fields'])
for c in selected:assert set(c)==set(proto['required_per_run']['claim_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len(read(BASE/'STATUS.md').splitlines())==2
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'verdict':'PASS','files':{str(p.relative_to(RUN)):sha(p.read_bytes()) for p in files},'statement_hashes':'PASS','schemas':'PASS','progress_delta_identical':True,'status_two_lines':True,'full_FEI':'OPEN','remote_adoption':'UNVERIFIED','jobs_left_running':0}
js(RUN/'out'/'PERSISTENCE_RECEIPT.json',receipt)
saved=json.loads(read(RUN/'out'/'PERSISTENCE_RECEIPT.json'))
for p,h in saved['files'].items():assert sha((RUN/p).read_bytes())==h
print(json.dumps({'saved_readback':'PASS','files':len(files),'exact_assertions':checks,'runtime_seconds':elapsed,'new_broad_claims':0,'independent_reviews':2,'full_FEI':'OPEN','jobs_left_running':0}))
