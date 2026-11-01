import exact as e
from exact import Q,ck,cutoff,save,fwht,inf,entropy,cross,add,Lv
import json,time,sys
job=int(sys.argv[1]);data=json.loads((e.ROOT/'out/ALL_PROFILES.json').read_text());cases=0
def Phi(a,b):return add((1,Lv(a)),(1,Lv(b)),(-1,Lv(a+b)))
for j in range(8*job,min(8*job+8,46)):
    mask,W=data['representatives'][j];m=W.bit_count();c=[1 if mask>>s&1 else -1 for s in range(8)];b=fwht([c[s]if W>>s&1 else 0 for s in range(8)]);a=fwht(c)
    for ev in range(16):
        cutoff();E=[bool(ev>>v&1)for v in range(4)];theta=Q(ev.bit_count(),4);kappa=[1-2*x for x in E];kh=fwht(kappa);Pk={v:x*x for v,x in enumerate(kh)};Rk={0:kh[0]**2,**{v:(1-kh[0]**2)/3 for v in range(1,4)}}
        G=[c[x&7]for x in range(32)];H=[c[x&7]*(1-2*bool(W>>(x&7)&1)*E[x>>3])for x in range(32)];F=G+H
        gh=fwht(G);hh=fwht(H);fh=fwht(F);PG={t:x*x for t,x in enumerate(gh)};PH={t:x*x for t,x in enumerate(hh)};PF={t:x*x for t,x in enumerate(fh)}
        d=m*theta/8;delta=m*theta*theta/8
        ck(sum(inf(F))==(sum(inf(G))+sum(inf(H)))/2+d);ck(inf(F)[5]==d)
        for t in range(8):ck(hh[t]==a[t]-2*theta*b[t]);ck(fh[t]==a[t]-theta*b[t]);ck(fh[t+32]==theta*b[t])
        for v in range(1,4):
            for t in range(8):ck(hh[t+8*v]==b[t]*kh[v])
        B=add(*[(1,Phi(PF[t],PF[t+32]))for t in range(32)])
        expected=add((1,{2:2*(d-delta)}),*[(1,Phi((a[t]-theta*b[t])**2,(theta*b[t])**2))for t in range(8)])
        ck(B=={p:x for p,x in expected.items()if x})
        RH={t:PH[t]if t<8 else b[t&7]**2*Rk[t>>3]for t in range(32)}
        RF={t:PF[t]if(t&31)<8 else RH[t&31]/4 for t in range(64)}
        ck(sum(RH.values())==1);ck(sum(RF.values())==1)
        Hk=entropy(Pk.values());Ck=cross(Pk,Rk);Dh=add((1,cross(PH,RH)),(-1,entropy(PH.values())));Df=add((1,cross(PF,RF)),(-1,entropy(PF.values())))
        ck(Dh==add((Q(m,8),Ck),(-Q(m,8),Hk)));ck(Df==add((Q(1,2),Dh)))
        Delta=add((1,entropy(PF.values())),(-Q(1,2),entropy(PG.values())),(-Q(1,2),entropy(PH.values())))
        ck(cross(PF,RF)==add((Q(1,2),entropy(PG.values())),(Q(1,2),cross(PH,RH)),(1,Delta)))
        cases+=1
save(f'FIXTURES_{job}.json',{'status':'PASS','cases':cases,'assertions':e.checks,'elapsed':time.perf_counter()-e.start});print(job,cases,e.checks,time.perf_counter()-e.start)
