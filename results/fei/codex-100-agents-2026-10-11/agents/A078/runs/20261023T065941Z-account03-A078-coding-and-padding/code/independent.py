from direct import F,product,Path,json,time,hashlib,plus,gg,prime,spectrum,entropy,positive,child,influence
R=Path(__file__).resolve().parents[1];O=R/'out'
spec={'version':'direct-majority-third-1','family':'actual odd majority with arbitrary correlated two-bit edited profiles, all first-two answers and ALL remaining nonseparator third queries','domain':{'d':[5,7],'explicit_profiles':8,'answers':4},'case_count':1536,'symmetry':'only first two nonseparator coordinates canonicalized by permutation; all remaining third coordinates checked','arithmetic':'direct Walsh character sums, Fraction edges and prime-log vectors, outward24-term atanh','memory_estimate_MB':80,'max_runtime_seconds':55}
(O/'FROZEN_INDEPENDENT.json').write_text(json.dumps(spec,indent=2),encoding='utf-8');start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks;assert time.monotonic()-start<55
def massg(q):
 if not q:return {}
 return plus(*[(-q*s,{p:F(v) for p,v in prime(n).items()}) for n,s in [(q.numerator,1),(q.denominator,-1)]])
def erase(a,i):return plus(*[(1,plus((1,gg(a[t])),(1,gg(a[t|(1<<i)])),(-1,massg(a[t]**2+a[t|(1<<i)]**2)))) for t in range(len(a)) if not(t>>i)&1])
profiles=[(1,1,1,1),(-1,-1,-1,-1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1),(-1,1,1,1),(1,-1,-1,-1),(1,1,1,-1)]
cases=means=0
for d in [5,7]:
 for b1,b2 in product([0,1],repeat=2):
  fixed={1:b1,2:b2};vertices=[s for s in range(2**d) if all((s>>i)&1==b for i,b in fixed.items())];r=d-2;p=F(1,2**r)
  for v in profiles:
   for w in profiles:
    f=tuple(v[z] if s==0 else w[z] if s==1 else 1 if s.bit_count()<=d//2 else -1 for z in range(4) for s in vertices)
    H=entropy(f);a=spectrum(f)
    meansector=tuple(F(sum(f[z*len(vertices)+s] for z in range(4)),4) for s in range(len(vertices)));ma=spectrum(meansector)
    rel=p*(2-F(sum(v),4)**2-F(sum(w),4)**2) if b1==b2==0 else F(0)
    for i in range(1,r):
     cases+=1;cc=[child(f,i,b) for b in [0,1]];j=influence(f,i)
     delta=plus((1,H),(-F(1,2),entropy(cc[0])),(-F(1,2),entropy(cc[1])))
     B=erase(ma,i)
     ck(positive(plus((1,{2:35*j}),(-1,B))))
     ck(positive(plus((1,{2:rel+38*j}),(-1,delta))))
     ck(sum(z*z for z in a)==1)
     if b1==b2==0:means+=int(sum(v)!=0 and sum(w)!=0)
ck(cases==1536)
# Original donor, all12 physical inputs; direct edges, no compressed spectral law.
truth=[]
for x in range(4096):
 s=x%32;z=(x>>5)%16;pad=(x>>9)%4;y=1-2*((x>>11)&1)
 b=(-1)**((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))
 truth.append(y*b if s==0 else y*(1-2*(z==0 and pad==0)) if s==1 else 1 if s.bit_count()<=2 else -1)
truth=tuple(truth);infs=[influence(truth,i) for i in range(12)]
expected=[F(409,1024)]+[F(7,16)]*4+[F(17,1024)]*4+[F(1,1024)]*2+[F(1,16)]
ck(infs==expected);ck(sum(infs)==F(2335,1024))
result={'status':'PASS','exact_assertions':checks,'third_queries':cases,'active_both_nonzero_means':means,'original_donor_coordinate_influences':[str(v) for v in infs],'original_donor_total_influence':str(sum(infs)),'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'INDEPENDENT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
