import exact as e
from exact import Q,ck,cutoff,save,logint
import sys,json,time
job=int(sys.argv[1]);data=json.loads((e.ROOT/'out/ALL_PROFILES.json').read_text());certs=[];pruned=[];visited=0
def upperphi(A,B):
    if not A or not B:return Q(0)
    return A*logint(1+B/A)[1]+B*logint(1+A/B)[1]
def df(t,m):
    d=m*t/8;return min(d,1-d)
def R(t,m):return 4*df(t,m)-m*t/4+m*t*t/4
def walk(j,m,p,lo,hi,depth):
    global visited
    cutoff();visited+=1
    mn=min(df(lo,m),df(hi,m));mx=max(df(lo,m),df(hi,m))
    if m and lo<=Q(4,m)<=hi:mx=Q(1,2)
    reason='zero' if not m else 'rare' if mx<=Q(1,32) else 'moderate' if mn>=Q(1,6) else None
    if reason:pruned.append({'profile':j,'lo':str(lo),'hi':str(hi),'reason':reason});return
    upper=sum((upperphi(max((a-lo*b)**2,(a-hi*b)**2),max((lo*b)**2,(hi*b)**2)) for a,b in p),Q(0))
    lower=min(R(lo,m),R(hi,m))-upper
    if lower>0:
        v=lower*(1<<48);rounded=Q(v.numerator//v.denominator,1<<48);ck(rounded>0)
        certs.append({'profile':j,'lo':str(lo),'hi':str(hi),'lower':str(rounded)});return
    ck(depth<6);mid=(lo+hi)/2;walk(j,m,p,lo,mid,depth+1);walk(j,m,p,mid,hi,depth+1)
for j in range(8*job,min(8*job+8,len(data['profiles']))):
    v=data['profiles'][j];m=v['m'];p=[tuple(map(Q,row))for row in v['pairs']]
    for i in range(128):walk(j,m,p,Q(i,128),Q(i+1,128),0)
    save(f'CONTINUUM_{job}_PARTIAL.json',{'completed_through':j,'certificates':certs,'pruned':pruned})
result={'status':'PASS','job':job,'certificates':certs,'pruned':pruned,'visited':visited,'assertions':e.checks,'elapsed':time.perf_counter()-e.start}
save(f'CONTINUUM_{job}.json',result);print({k:v for k,v in result.items()if k not in('certificates','pruned')},'certificates',len(certs))
