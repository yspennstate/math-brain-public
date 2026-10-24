import mpmath as mp,json,itertools
from pathlib import Path
mp.mp.dps=90
# Positive uniformization: p=e^(-nt) sum (nt)^k/k! (I+Q/n)^k delta.
def uniform(n,M,t,K=300):
 states=[tuple(reversed(s)) for s in itertools.combinations_with_replacement(range(M+1),n)];idx={s:i for i,s in enumerate(states)}
 edges=[]
 for s in states:
  dest=[];rate=0
  for i in range(n):
   if i==0 or s[i]<s[i-1]:
    rate+=1;z=list(s);z[i]+=1
    if tuple(z) in idx:dest.append(idx[tuple(z)])
  edges.append((dest,n-rate))
 v=[mp.mpf(0)]*len(states);v[idx[(0,)*n]]=mp.mpf(1);w=mp.exp(-n*t);p=[w*a for a in v]
 for k in range(1,K+1):
  nxt=[mp.mpf(0)]*len(v)
  for j,a in enumerate(v):
   if a:
    ds,stay=edges[j];nxt[j]+=a*stay/n
    for h in ds:nxt[h]+=a/n
  v=nxt;w*=mp.mpf(n)*t/k
  for j,a in enumerate(v):p[j]+=w*a
 return dict(zip(states,p))
results=[]
for n,M,t,a,b in [(2,30,2,(28,1),(30,1)),(3,16,1,(14,9,0),(16,9,0)),(3,16,2,(16,11,6),(16,13,6))]:
 p=uniform(n,M,t,140);c=tuple((x+y)//2 for x,y in zip(a,b));r={'n':n,'t':t,'a':a,'b':b,'mid':c,'ratio':str(p[c]**2/p[a]/p[b]),'pa':str(p[a]),'pb':str(p[b]),'pm':str(p[c])};results.append(r);print(r,flush=True);Path('tail_rechecks.json').write_text(json.dumps(results,indent=2))
