from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
old=R.parents[0]/'20261013T222840Z-account05-A013-representation-stability/code/check.py'
helper=old.read_text().split('tables=')[0]
(R/'code/check.py').write_text(helper+'''\npatterns=[(1,0,0,0,0,0,0,0),(F(1,2),)*3+(-F(1,2),)+(0,)*4,(F(3,4),)+(F(1,4),)*4+(-F(1,4),)*3,(-F(3,4),)+(F(1,4),)*7]
def row(a,b):
 m=a*a+b*b
 return mul(H([a*a/m,b*b/m]),m) if m else {}
def packet(cs,d):
 b=mul(lv(2),2*(d-8*d*d))
 for c in cs:b=add(b,row(c-d,d))
 return b
certs=[]
for k,cs in enumerate(patterns):
 for r in [0,1]:
  d=F(1,8*(1<<r));b=packet(cs,d);gap=add(mul(lv(2),4*d),b,F(-1));nonneg(gap)
  lo,hi=iv(gap);check(lo>0)
  certs.append({'pattern':k,'r':r,'d':str(d),'gap_prime_log':{str(p):str(v) for p,v in gap.items()},'gap_interval':[str(lo),str(hi)]})
(RUN/'out/PROFILE_CERTIFICATES.json').write_text(json.dumps(certs,indent=2))
print('eight rational profile certificates PASS',flush=True)
profiles=0;pattern_counts=[0]*4
for mask in range(256):
 c=[1 if mask>>y&1 else -1 for y in range(8)];a=fwht(c)
 for w in range(8):
  cs=[a[t]*c[w]*(-1 if (t&w).bit_count()%2 else 1) for t in range(8)]
  k=next(k for k,p in enumerate(patterns) if sorted(cs)==sorted(p));pattern_counts[k]+=1
  for r in [0,1,2,3]:
   n=3+r;d=F(1,8*(1<<r))
   h=[c[x&7]*(-1 if (x&7)==w and (x>>3)==0 else 1) for x in range(1<<n)]
   ah=fwht(h);ag=[a[t] if t<8 else F(0) for t in range(1<<n)]
   for t in range(1<<n):check(ah[t]==ag[t]-2*d*c[w]*(-1 if (t&w).bit_count()%2 else 1))
   f=[c[x&7] if x<(1<<n) else h[x-(1<<n)] for x in range(1<<(n+1))]
   af=fwht(f)
   for t in range(1<<n):check(af[t]==(ag[t]+ah[t])/2);check(af[t+(1<<n)]==(ag[t]-ah[t])/2)
   check(influence(f,n+1)[n]==d)
   # Prime-log equality verifies actual spectra, not only the surrogate pattern.
   bc={}
   for t in range(8):bc=add(bc,row((ag[t]+ah[t])/2,(ag[t]-ah[t])/2))
   b=add(bc,mul(lv(2),2*(d-8*d*d)))
   check(b==packet(patterns[k],d))
   profiles+=1
 print('phase',mask,'complete',flush=True) if mask in [63,127,191,255] else None
source_cases=0
tables=[[1 if mask>>x&1 else -1 for x in range(8)] for mask in range(256)]
for gi in range(16):
 for hi in range(16):
  g=tables[gi];h=tables[17*hi]
  ag=fwht(g);ah=fwht(h)
  eg=[F(0)]*16;eh=[F(0)]*16
  for t in range(8):eg[t]=ag[t];eh[(t&3)|((t>>2)<<3)]=ah[t]
  d=(1-sum(a*b for a,b in zip(eg,eh)))/2
  if d>F(1,2):eh=[-a for a in eh];d=1-d
  delta=sum((eg[t]-eh[t])**2/4 for t in range(4));bc={};bout={}
  for t,(a,b) in enumerate(zip(eg,eh)):
   z=row((a+b)/2,(a-b)/2)
   if t<4:bc=add(bc,z)
   else:bout=add(bout,z)
  check(bout==mul(lv(2),2*(d-delta)));check(delta<=min(d,4*d*d))
  nonneg(add(mul(lv(2),4*d),add(bc,bout),F(-1)));source_cases+=1
print('source ownership/payment reconstruction PASS',flush=True)
# Exact proper-nonmember root witnesses, independently generated.
t=[1 if x.bit_count()>=2 else -1 for x in range(16)];minors=[]
for j in range(4):
 for v in [0,1]:
  for k in range(4):
   if k!=j:check(any(t[x]!=t[x^(1<<k)] for x in range(16) if (x>>j)&1==v))
for mask in range(1,15):
 if not mask&1:continue
 left=[x for x in range(16) if x&~mask==0];right=[x for x in range(16) if x&mask==0]
 witness=next((a,b,c,d) for a in left for b in left for c in right for d in right if t[a|c]*t[b|d]!=t[a|d]*t[b|c])
 minors.append({'partition':mask,'minor':witness})
(RUN/'out/NONMEMBER_RECHECK.json').write_text(json.dumps(minors,indent=2))
# Retain an arbitrary fixed terminal reference under a disjoint common factor.
tensor_cases=0
for mask in range(16):
 q=[1 if mask>>x&1 else -1 for x in range(4)];pq=[v*v for v in fwht(q)]
 for r in [0,1]:
  for cmask in [255,15,1,7]:
   c=[1 if cmask>>y&1 else -1 for y in range(8)];n=3+r
   h=[c[x&7]*(-1 if (x&7)==0 and (x>>3)==0 else 1) for x in range(1<<n)]
   f=[c[x&7] if x<(1<<n) else h[x-(1<<n)] for x in range(1<<(n+1))]
   pf=[a*a for a in fwht(f)];p=[a*b for a in pq for b in pf]
   actual=[q[x//len(f)]*f[x%len(f)] for x in range(4*len(f))]
   check([a*a for a in fwht(actual)]==p)
   for rq in refs(pq):
    ref=[a*b for a in rq for b in pf]
    check(sum(ref)==1);check(CE(p,ref)==add(CE(pq,rq),H(pf)))
    check(add(CE(p,ref),H(p),F(-1))==add(CE(pq,rq),H(pq),F(-1)))
    tensor_cases+=1
res={'status':'PASS','helper_version':'A013-three-bit-profile-v1','profiles':profiles,'classification_pairs':sum(pattern_counts),'pattern_counts':pattern_counts,'scalar_certificates':len(certs),'source_pairs':source_cases,'nonmember_partitions':len(minors),'retained_terminal_reference_cases':tensor_cases,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/'out/EXACT_RESULTS.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res),flush=True)
''',encoding='utf-8')
spec={'helper_version':'A013-three-bit-profile-v1','family':'G=c on three shared bits; H=c with one shared point flipped only when all r private controllers are zero; fresh physical selector. Independent A012 two-shared-bit ownership recheck and fixed common terminal product.','domain':{'c':'all 256 labelled signs','w':'all 8 shared points','r':[0,1,2,3],'source_review':'16 x 16 fixed labelled three-bit branch subset','terminal':'16 two-bit signs x four named phases x r=0,1 x three fixed references'},'case_counts':{'profiles':8192,'phase_point_classification':2048,'scalar_interval_certificates':8,'source_review_pairs':256,'proper_nonmember_partitions':7,'retained_terminal_reference_cases':384},'symmetry':'No truth-table symmetry reduction; four proved relative-point Walsh patterns used only for analytic scalar certificates.','arithmetic':'Integer FWHT; Fraction; exact prime-log vectors; 20-term rational atanh with geometric tail for logarithm signs.','memory_estimate_MB':70,'maximum_runtime_seconds':50,'pilot_max_seconds':60,'no_automatic_escalation':True,'helper_provenance':'Copied local stage3 elementary rational log arithmetic; new independent spectra/ownership and profile checker; no A012 or A095 code imported.'}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('checker and frozen spec saved before search')
