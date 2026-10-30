from pathlib import Path
from fractions import Fraction as Q
import json,time
from collections import Counter
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
    global checks
    assert v;checks+=1
def lnunit(z):
    u=(z-1)/(z+1);ck(0<=u<=Q(1,3));s=sum((2*u**(2*j+1)/Q(2*j+1)for j in range(64)),Q(0));tail=2*u**129/(129*(1-u*u));return s,s+tail
LN=lnunit(Q(2))
from functools import lru_cache
@lru_cache(None)
def lg(z):
    k=0
    while z<1:z*=2;k-=1
    while z>=2:z/=2;k+=1
    a,b=lnunit(z);cs=[a/LN[0],a/LN[1],b/LN[0],b/LN[1]];return k+min(cs),k+max(cs)
def L(z):
    if not z:return Q(0),Q(0)
    a,b=lg(z);return -z*b,-z*a
def phiupper(A,B):return L(A)[1]+L(B)[1]-L(A+B)[0]
data=json.loads((R/'out/ALL_PROFILES.json').read_text());target=Counter({(v['m'],tuple(tuple(map(Q,p))for p in v['pairs'])):n for v,n in zip(data['profiles'],data['counts'])})
actual=Counter()
sign=[[(-1)**((s&t).bit_count())for s in range(8)]for t in range(8)]
for mask in range(256):
    c=[1 if mask>>s&1 else -1 for s in range(8)];a=[Q(sum(c[s]*sign[t][s]for s in range(8)),8)for t in range(8)]
    for W in range(256):
        b=[Q(sum(c[s]*sign[t][s]for s in range(8)if W>>s&1),8)for t in range(8)]
        p=tuple(sorted((x,y)if y>0 or(y==0 and x>=0)else(-x,-y)for x,y in zip(a,b)));actual[W.bit_count(),p]+=1
ck(actual==target);ck(sum(actual.values())==65536)
def df(t,m):return min(m*t/8,1-m*t/8)
def RR(t,m):return 4*df(t,m)-m*t/4+m*t*t/4
coverage={i:[]for i in range(46)};count=0;minimum=None
for job in range(6):
    v=json.loads((R/f'out/CONTINUUM_{job}.json').read_text());ck(v['status']=='PASS')
    for cert in v['certificates']:
        j=cert['profile'];lo=Q(cert['lo']);hi=Q(cert['hi']);m=data['profiles'][j]['m'];p=[tuple(map(Q,x))for x in data['profiles'][j]['pairs']]
        upper=sum((phiupper(max((a-lo*b)**2,(a-hi*b)**2),max((lo*b)**2,(hi*b)**2))for a,b in p),Q(0));lower=min(RR(lo,m),RR(hi,m))-upper
        ck(lower>=Q(cert['lower'])>0);coverage[j].append((lo,hi));count+=1;minimum=Q(cert['lower'])if minimum is None else min(minimum,Q(cert['lower']))
    for cert in v['pruned']:
        j=cert['profile'];lo=Q(cert['lo']);hi=Q(cert['hi']);m=data['profiles'][j]['m'];mn=min(df(lo,m),df(hi,m));mx=max(df(lo,m),df(hi,m))
        if m and lo<=Q(4,m)<=hi:mx=Q(1,2)
        ck((cert['reason']=='zero'and m==0)or(cert['reason']=='rare'and mx<=Q(1,32))or(cert['reason']=='moderate'and mn>=Q(1,6)));coverage[j].append((lo,hi))
for j,rows in coverage.items():
    rows.sort();ck(rows[0][0]==0 and rows[-1][1]==1)
    for (a,b),(c,d)in zip(rows,rows[1:]):ck(a<b==c<d)
ck(lg(Q(5,4))[1]<Q(1,3))
result={'status':'PASS','profiles':46,'classified_pairs':65536,'positive_certificates':count,'coverage_intervals':sum(map(len,coverage.values())),'minimum_positive_gap':str(minimum),'assertions':checks,'elapsed':time.perf_counter()-start}
(R/'out/VERIFY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
