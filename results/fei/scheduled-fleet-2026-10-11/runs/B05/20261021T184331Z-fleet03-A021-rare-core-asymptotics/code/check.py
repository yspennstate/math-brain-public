"""A021 partner checks. Utilities copied with provenance; new policy independently built."""
from pathlib import Path
from fractions import Fraction as Q
import json, time, hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
old=ROOT/'code/old_utilities.py'
# Import only pure definitions; do not run its job or write its outputs.
ns={'__file__':str(ROOT/'code/old_utilities.py'),'__name__':'utilities'}
exec(compile(old.read_text(encoding='utf-8').split('def run():')[0],str(old),'exec'),ns)
build,restrict,actual,bank,terminal,entropy,infs,influence,add,sub,scale=[ns[k] for k in ['build','restrict','actual','bank','terminal','entropy','infs','influence','add','sub','scale']]
checks=0
def check(ok,where):
    global checks
    checks+=1
    assert ok, (checks,where)
def save(name,x):
    (OUT/name).write_text(json.dumps(x,indent=2,default=str)+'\n',encoding='utf-8')
def avg_entropy(fs):
    ans=(Q(0),Q(0))
    for w,f in fs: ans=add(ans,scale(entropy(f),w))
    return ans
def go():
    started=time.perf_counter(); rows=[]
    for m in (4,6,8):
      for t in (0,1,2):
        delta=Q(1,2**m); p=Q(1,2**t)
        cores=build(m,t); f=actual(cores)
        xc=[[restrict(g,m,b) for g in cores] for b in (0,1)]
        yc=[[restrict(g,0,b) for g in xc[0]] for b in (0,1)]
        zc=[[[restrict(g,0,b) for g in cs] for b in (0,1)] for cs in yc]
        leaves=[(Q(1,2),xc[1])]+[(Q(1,8),cs) for pair in zc for cs in pair]
        Dx=sub(entropy(f),avg_entropy([(Q(1,2),actual(cs)) for cs in xc]))
        Ux=max(Q(0),Dx[1]-10*p*delta/2)
        Dy=sub(entropy(actual(xc[0])),avg_entropy([(Q(1,2),actual(cs)) for cs in yc]))
        check(Dy[1]<5*p*(Q(1,2)+delta),'inherited y0 bill')
        Ds=[]; ds=[]
        for a in (0,1):
            ff=actual(yc[a]); d=infs(ff)[0]
            D=sub(entropy(ff),avg_entropy([(Q(1,2),actual(cs)) for cs in zc[a]]))
            ds.append(d); Ds.append(D)
            check(d==p*(delta if a==0 else 1-delta),'partner pivot')
            check(bank(yc[a])-sum((bank(cs)/2 for cs in zc[a]),Q(0))==3*p*delta/2,'partner bank release')
        Uy=max(Q(0),Ds[0][1]-10*ds[0])/4
        check(ns['erasure'](actual(yc[0]),0)[0]>p*delta*(Q(3,2)+Q(m,4)),'obstruction row lower bound')
        check(Ux<=p*m*delta/2,'old excess')
        check(Uy<=p*m*delta/4,'new excess')
        check(Ds[1][1]<5*ds[1],'opposite sibling payment')
        IT=sum((w*terminal(cs)[0] for w,cs in leaves),Q(0))
        HT=(Q(0),Q(0))
        for w,cs in leaves: HT=add(HT,scale(terminal(cs)[1],w))
        S=(8*IT-HT[1],8*IT-HT[0])
        R=sum((w*bank(cs) for w,cs in leaves),Q(0))
        Rold=p*(3*m-1+3*t)*delta/4
        check(IT==p*(Q(m+1,2)+Q(m-2,2)*delta+t),'full terminal influence')
        check(R==p*(3*m-6+3*t)*delta/4,'full remaining bank')
        check(S[0]>p*(3*m+2+4*t),'full surplus lower bound')
        for debit,frac in [(Rold,delta/4),(Ux,delta/6),(Uy,delta/12)]:
            check(debit<=frac*S[0],'one disjoint booking')
        check(R+Ux+Uy<=delta*S[0]/2,'total bookings')
        IC=Q(0)
        for w,cs in leaves:
            ff=actual(cs); ic=sum(infs(ff)[-2:]); IC+=w*ic
            bill=(Q(0),Q(0)) if cs[0]==cs[1]==cs[2] else sub(entropy(ff),terminal(cs)[1])
            check(bill[1]<=bank(cs)+10*ic,'complete controller continuation')
        qdata=infs(f)[m]+infs(actual(xc[0]))[0]/2+(ds[0]+ds[1])/4
        check(influence(f)==qdata+IC+IT,'physical influence telescope')
        decomp=add(Dx,scale(Dy,Q(1,2)))
        decomp=add(decomp,scale(add(Ds[0],Ds[1]),Q(1,4)))
        dc=(Q(0),Q(0))
        for w,cs in leaves: dc=add(dc,scale(sub(entropy(actual(cs)),terminal(cs)[1]),w))
        total=add(add(decomp,dc),HT)
        check(total[0]<=entropy(f)[1] and total[1]>=entropy(f)[0],'entropy telescope')
        check(10*influence(f)-entropy(f)[1]>=2*IT+(1-delta/2)*S[0],'final paid history')
        rows.append({'m':m,'t':t,'R3':R,'IT3':IT,'S3_interval':S,'Ux_upper':Ux,'Uy_upper':Uy,'partner_D':Ds,'partner_d':ds})
        save('DIRECT.json',{'status':'RUNNING','rows':rows,'assertions':checks})
    for m in range(4,102,2):
      for t in (0,m,3*m+1):
        delta=Q(1,2**m); p=Q(1,2**t); S=p*(3*m+1+4*t)
        Rold=p*(3*m-1+3*t)*delta/4; R3=p*(3*m-6+3*t)*delta/4
        Ux=p*m*delta/2; Uy=p*m*delta/4
        check(Rold<=delta*S/4,'scalar bank')
        check(Ux<=delta*S/6,'scalar old')
        check(Uy<=delta*S/12,'scalar new')
        check(0<=R3<=Rold,'scalar contraction')
        check(R3+Ux+Uy<=delta*S/2,'scalar total')
        check(delta/2<=Q(1,32),'scalar fraction')
    result={'status':'PASS','direct_cases':9,'scalar_cases':147,'assertions':checks,'seconds':time.perf_counter()-started,'rows':rows,'helper_origin':str(old),'helper_origin_sha256':hashlib.sha256(old.read_bytes()).hexdigest()}
    save('DIRECT.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','helper_origin','helper_origin_sha256')}))
if __name__=='__main__': go()
