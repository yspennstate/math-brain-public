from check import fw,bounds,enc,put
from fractions import Fraction as Q
import time,sys,json
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;n=3 if pilot else 4;N=1<<n;M=1<<N
 # H numerator over N^2, in log2(2),log2(3),log2(5),log2(7).
 primes=[2,3,5,7];fac={}
 for w in range(2,N+1,2):
  x=w;ex=[]
  for p in primes:
   e=0
   while x%p==0:e+=1;x//=p
   ex.append(e)
  assert x==1;fac[w]=ex
 hs=[];ins=[];cached={};S=1<<144;checks=0
 for m in range(M):
  v=[1 if m>>x&1 else -1 for x in range(N)];ws=fw(v);h=[2*n*N*N,0,0,0];ii=0
  for s,w in enumerate(ws):
   ii+=s.bit_count()*w*w
   if w:
    for j,e in enumerate(fac[abs(w)]):h[j]-=2*w*w*e
  h=tuple(h);hs.append(h);ins.append(ii)
  if h not in cached:
   l,u=bounds({p:Q(c,N*N) for p,c in zip(primes,h) if c});cached[h]=(l.numerator*S//l.denominator,(u.numerator*S+u.denominator-1)//u.denominator)
  # Physical edge and direct character replay for every pilot and frozen stride at n4.
  if pilot or m%257==0:
   assert ii==N*sum(v[x]!=v[x^(1<<j)] for x in range(N) for j in range(n));checks+=1
   assert ws==[sum(v[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)];checks+=1
  assert time.perf_counter()-start<55
 results=[];guards=[]
 for kn in range(17):
  # Influence and K are dyadic; their scaled product is exact.
  dlo=[cached[h][0]-kn*ii*S//(2*N*N) for h,ii in zip(hs,ins)]
  dhi=[cached[h][1]-kn*ii*S//(2*N*N) for h,ii in zip(hs,ins)]
  def cmp(a,b):
   if dlo[a]>dhi[b]:return 1
   if dhi[a]<dlo[b]:return -1
   assert hs[a][1:]==hs[b][1:] and 2*(hs[a][0]-hs[b][0])==kn*(ins[a]-ins[b]),('unresolved',n,kn,a,b)
   return 0
  sub=list(range(M));sup=list(range(M));best=0
  for m in range(M):
   if cmp(m,best)>0:best=m
  for j in range(N):
   b=1<<j
   for m in range(M):
    if m&b:
     z=m^b
     if cmp(sub[z],sub[m])>0:sub[m]=sub[z]
    else:
     z=m|b
     if cmp(sup[z],sup[m])>0:sup[m]=sup[z]
  loc=[];bad=[]
  for m in range(M):
   assert sub[m]&m==sub[m] and sup[m]&m==m;checks+=1
   if cmp(sub[m],m)==0 and cmp(sup[m],m)==0:
    loc.append(m)
    if cmp(best,m)>0:
     bad.append(m)
     if len(guards)<8:guards.append({'n':n,'K':str(Q(kn,2)),'mask':m,'better_mask':best,'H_numerator':list(hs[m]),'I_numerator':ins[m],'target_H_numerator':list(hs[best]),'target_I_numerator':ins[best],'denominator':N*N,'primes':primes})
  results.append({'K':str(Q(kn,2)),'one_sign_maxima':len(loc),'non_global':len(bad),'global_mask':best})
  put('LATTICE_CHECKPOINT.json',{'n':n,'completed_K':str(Q(kn,2)),'guards':guards,'results':results})
  assert time.perf_counter()-start<55
 out={'status':'PASS','pilot':pilot,'n':n,'tables':M,'rates':17,'validation_assertions':checks,'entropy_profiles':len(cached),'results':results,'guards':guards,'elapsed_seconds':time.perf_counter()-start}
 put('LATTICE_PILOT.json' if pilot else 'LATTICE.json',out);print(json.dumps(out))
if __name__=='__main__':main()
