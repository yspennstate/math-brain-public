import exact as e
from exact import Q,ck,cutoff,save,fwht,inf,entropy,cross,add,scalar,Lv,vint
import json,time
representatives=json.loads((e.ROOT/'out/REPRESENTATIVES.json').read_text());counts=[0,1,32,64,128,155,200,256]
cases=refs=0;fixtures=[]
for pi,item in representatives.items():
    c=item['c'];w=item['w'];ch=fwht(c);Pc={t:x*x for t,x in enumerate(ch) if x};Hc=entropy(Pc.values())
    for count in counts:
        cutoff();cases+=1;theta=Q(count,256);d=theta/8
        core=[-1 if x<count else 1 for x in range(256)];kh=fwht(core);Pk={t:x*x for t,x in enumerate(kh) if x};Hk=entropy(Pk.values());mu=kh[0]
        h=[c[x&7]*core[x>>3] if x&7==w else c[x&7] for x in range(2048)]
        hh=fwht(h);Ph={t:x*x for t,x in enumerate(hh) if x};Hh=entropy(Ph.values())
        f=[c[(x>>1)&7] if not x&1 else h[x>>1] for x in range(4096)];fh=fwht(f);Pf={t:x*x for t,x in enumerate(fh) if x};Hf=entropy(Pf.values())
        expected={}
        for t,a in enumerate(hh):
            for u in (0,1):
                v=(ch[t] if t<8 else Q(0))+(-1)**u*a
                ck(fh[(t<<1)|u]==v/2)
        actual=inf(f);ck(actual[0]==d);ck(sum(actual[1:])==(sum(inf(c))+sum(inf(h)))/2)
        B={};delta=Q(0)
        for t in range(8):
            A=(ch[t]+hh[t])**2/4;M=(ch[t]-hh[t])**2/4;delta+=M
            B=add((1,B),(1,Lv(A)),(1,Lv(M)),(-1,Lv(A+M)))
        ck(delta==8*d*d);B=add((1,B),(1,scalar(2*(d-delta))))
        slack=add((1,scalar(4*d)),(-1,B));ck(not slack or vint(slack)[0]>0)
        for kind in (0,1):
            refs+=1;Rk={0:mu*mu}
            for t in range(1,256):Rk[t]=Pk.get(t,Q(0)) if kind==0 else (1-mu*mu)/255
            Rh={t:hh[t]*hh[t] for t in range(8)}
            for t in range(1,256):
                for s in range(8):Rh[s|(t<<3)]=Rk[t]/64
            ck(sum(Rh.values())==1)
            Rf={}
            for t in range(8):
                for u in (0,1):Rf[(t<<1)|u]=(ch[t]+(-1)**u*hh[t])**2/4
            for t,mass in Rh.items():
                if t>=8:
                    for u in (0,1):Rf[(t<<1)|u]=mass/4
            ck(sum(Rf.values())==1)
            Ck=cross(Pk,Rk);Ch=cross(Ph,Rh);Cf=cross(Pf,Rf)
            ck(add((1,Ch),(-1,Hh))==add((Q(1,8),Ck),(-Q(1,8),Hk)))
            ck(add((1,Cf),(-1,Hf))==add((Q(1,16),Ck),(-Q(1,16),Hk)))
            tax=add((1,Hf),(-Q(1,2),Hc),(-Q(1,2),Hh))
            ck(Cf==add((Q(1,2),Hc),(Q(1,2),Ch),(1,tax)))
            slack7=add((1,scalar(7*d)),(-1,tax));ck(not slack7 or vint(slack7)[0]>0)
            if count==155 and kind==1:fixtures.append({'profile':pi,'count':count,'d':str(d),'B_over_d_interval':e.iv(vint(add((1/d,B)))),'controller_debt_retention':'1/16','complete_reference_mass':str(sum(Rf.values()))})
        save('FIXTURE_PARTIAL.json',{'status':'PASS_COMPLETED_CASES_ONLY','cases':cases,'references':refs,'assertions':e.checks,'fixtures':fixtures})
save('FIXTURE_RESULTS.json',{'status':'PASS','cases':cases,'references':refs,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-e.start,'max_truth_table_dimension':12,'fixtures':fixtures})
print({'status':'PASS','cases':cases,'references':refs,'assertions':e.checks,'seconds':time.perf_counter()-e.start})
