from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import time,json,sys
import entropy_tools as E
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNT=0
def ck(ok):
    global COUNT
    COUNT+=1
    if not ok: raise AssertionError(COUNT)
def save(name,v): (ROOT/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def ent(law): return E.H(tuple(x for x in law if x))
def serial(v): return {str(p):str(c) for p,c in v.items()}
def marginal(joint,positions):
    ans=defaultdict(F)
    for key,p in joint.items(): ans[tuple(key[i] for i in positions)]+=p
    return ans
@lru_cache(None)
def spectrum(t,labels):
    vals=list(t);N=len(t);step=1
    while step<N:
        for s in range(0,N,2*step):
            for j in range(step):
                a,b=vals[s+j],vals[s+j+step]
                vals[s+j],vals[s+j+step]=a+b,a-b
        step*=2
    law={sum(1<<labels[i] for i in range(len(labels)) if s>>i&1):F(c*c,N*N) for s,c in enumerate(vals) if c}
    ck(sum(law.values())==1)
    return law
def restrict(t,i,b):
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def influences(t,labels):
    return {a:F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i,a in enumerate(labels)}
def audit(t,chooser,A,name):
    labels=tuple(range(len(t).bit_length()-1));root=spectrum(t,labels)
    inf=influences(t,labels);a=sum(inf[i] for i in A);nodes={};leaves={}
    sums={'M':{},'J':{},'leafH':{}};R=F(0);terminalI=F(0)
    def walk(tt,ll,path,w):
        nonlocal R,terminalI
        law=spectrum(tt,ll);infl=influences(tt,ll);query=chooser(path,ll,tt)
        if query is None:
            leaves[path]=(w,law,tt,ll);terminalI+=w*sum(infl.values())
            sums['leafH']=E.add(sums['leafH'],E.mul(ent(law.values()),w));return
        ck(query in ll and infl[query]>0)
        i=ll.index(query);rest=ll[:i]+ll[i+1:]
        ts=[restrict(tt,i,b) for b in [0,1]];cs=[spectrum(c,rest) for c in ts]
        row=defaultdict(F)
        for s,p in law.items(): row[s&~(1<<query)]+=p
        ck(all(row[s]==(cs[0].get(s,F(0))+cs[1].get(s,F(0)))/2 for s in set(row)|set(cs[0])|set(cs[1])))
        M=E.sub(ent(law.values()),ent(row.values()))
        J=E.sub(ent(row.values()),E.mul(E.add(*(ent(c.values()) for c in cs)),F(1,2)))
        for k,v in [('M',M),('J',J)]:sums[k]=E.add(sums[k],E.mul(v,w))
        R+=w*infl[query];nodes[path]=(query,row,cs)
        for b in [0,1]:walk(ts[b],rest,path+((query,b),),w/2)
    walk(t,labels,(),F(1))
    ck(R==sum(inf.values())-terminalI)
    joint=defaultdict(F)
    for s,mass in root.items():
        def lift(path,w):
            if path not in nodes:
                Q=sum(1<<i for i,b in path);joint[(s,path,s&~Q)]+=w;return
            query,row,cs=nodes[path];Q=sum(1<<i for i,b in path)|(1<<query);T=s&~Q
            ck(row[T]>0)
            for b in [0,1]:
                p=cs[b].get(T,F(0))/(2*row[T])
                if p:lift(path+((query,b),),w*p)
        lift((),mass)
    ck(sum(joint.values())==1)
    for path,(w,law,tt,ll) in leaves.items():
        ck(sum(p for (s,h,v),p in joint.items() if h==path)==w)
        for v in set(law)|{v for s,h,v in joint if h==path}:
            ck(sum(p for (s,h,q),p in joint.items() if h==path and q==v)==w*law.get(v,F(0)))
    Hs=ent(root.values());Hp=ent(w for w,law,tt,ll in leaves.values())
    Hsp=ent(marginal(joint,(0,1)).values());Hw=ent(marginal(joint,(2,)).values())
    Hwp=ent(marginal(joint,(2,1)).values());Hsw=ent(marginal(joint,(0,2)).values())
    bank=E.sub(Hwp,Hw);rootbank=E.sub(Hsp,Hs);j=E.sub(Hp,rootbank)
    jw=E.sub(Hp,bank);inj=E.sub(Hsw,Hs);reset=E.sub(bank,rootbank)
    ck(j==sums['J']);ck(Hs==E.add(sums['M'],sums['J'],sums['leafH']))
    ck(Hwp==E.add(Hp,sums['leafH']));ck(reset==E.sub(j,jw))
    # Verify schedule reference capacity and true expected deletion size.
    deleted=sum(p*(s&~w).bit_count() for (s,path,w),p in joint.items())
    ck(deleted==R and R<=a)
    if a and R!=a and R:
        cap=E.mul(E.hb(R/a),a);slack=E.sub(cap,inj)
        if slack:ck(E.interval(slack)[0]>=0)
    else:ck(not inj)
    # Physical transcript reference is one normalized law, independent of W.
    ck(sum(w for w,law,tt,ll in leaves.values())==1)
    ck(bank==E.sub(Hp,jw))
    residual=E.add(E.mul(Hp,F(1,2)),sums['M'],E.mul(j,-1))
    ck(Hs==E.add(sums['leafH'],E.mul(sums['M'],2),E.mul(bank,F(1,2)),E.mul(jw,F(1,2)),E.mul(residual,-1)))
    if not inj:
        # W fixed projection in controller-complete examples: no hidden reset injection.
        ck(all(w==s&~sum(1<<i for i in A) for s,path,w in joint))
        if reset:ck(E.interval(reset)[0]>=0)
    row={'name':name,'n':len(labels),'truth_table':list(t),'I':str(sum(inf.values())),'R':str(R),'a':str(a),'terminal_I':str(terminalI),
         'H_root':serial(Hs),'H_transcript':serial(Hp),'H_W':serial(Hw),'H_transcript_given_W':serial(bank),
         'H_transcript_given_root':serial(rootbank),'reset_price':serial(reset),'injection':serial(inj),
         'J':serial(j),'M':serial(sums['M']),'terminal_H':serial(sums['leafH']),'signed_residual':serial(residual),
         'bank_interval':E.outward(E.interval(bank),64),'joint_entries':len(joint),
         'root_spectrum':{str(k):str(v) for k,v in root.items()},
         'physical_transcripts':[{'path':list(path),'probability':str(w)} for path,(w,law,tt,ll) in leaves.items()]}
    save(name+'.json',row)
    return row,(Hs,Hp,Hw,bank,rootbank,inj,sums,reset)
def main():
    pilot='--pilot' in sys.argv;cases=0
    # Independently validate zero-row arithmetic without invoking Lean.
    for a in [F(0),F(1,4),F(1)]:
        for b in [F(0),F(1,8),F(2)]:
            k=a/(a+b) if a+b else F(1,2);kb=b/(a+b) if a+b else F(1,2)
            ck(k+kb==1 and (a+b)*k/2==a/2)
    for r in ([1] if pilot else [1,2,3]):
        t=tuple((-1)**sum((x>>(2*j)&3)==3 for j in range(r)) for x in range(1<<(2*r)))
        def choose(path,ll,tt):
            d=dict(path)
            for j in range(r):
                if 2*j not in d:return 2*j
                if d[2*j] and 2*j+1 not in d:return 2*j+1
            return None
        row,v=audit(t,choose,set(range(2*r)),'AND_r'+str(r));cases+=1
        Hs,Hp,Hw,bank,rb,inj,sums,reset=v
        ck(Hs=={2:F(2*r)} and Hp=={2:F(3*r,2)} and not Hw)
        ck(rb=={2:F(r,2)} and reset=={2:F(r)} and row['I']==str(F(r)))
    for m in ([1] if pilot else range(1,7)):
        n=m+4;t=[]
        for x in range(1<<n):
            z=x&((1<<m)-1);a=x>>m&1;b=x>>(m+1)&1;y=x>>(m+2)
            g=1-2*(6>>y&1);h=1-2*(8>>y&1)
            t.append(g if z==(1<<m)-1 and a else h if z==(1<<m)-1 and b else 1)
        def choose(path,ll,tt):
            d=dict(path)
            for i in range(m):
                if i not in d:return i
                if d[i]==0:return None
            if m not in d:return m
            if d[m]:return None
            if m+1 not in d:return m+1
            return None
        row,v=audit(tuple(t),choose,set(range(m+2)),'PRIORITY_m'+str(m));cases+=1
        Hs,Hp,Hw,bank,rb,inj,sums,reset=v;tau=F(1,1<<m)
        expectedW=ent((1-11*tau/16,tau/16,tau/16,9*tau/16))
        ck(Hw==expectedW and bank==E.sub({2:F(2)},Hw))
        ck(Hp=={2:2-tau/2} and sums['leafH']=={2:tau/2} and not inj)
        ck(F(row['R'])==tau*(F(5*m,8)+F(3,4)))
        ck(F(row['I'])==tau*(F(5*m,8)+2) and F(row['terminal_I'])==5*tau/4)
        if m==6:
            ck(E.interval(bank)[0]>16*F(row['R']))
            row['rigorous_violation']='H(Pi|W)>16 R'
            save('PRIORITY_m6.json',row)
    t=tuple((-1)**x.bit_count() for x in range(8))
    def adaptive(path,ll,tt):
        if not path:return 0
        if len(path)==1:return 1 if path[0][1]==0 else 2
        return None
    row,v=audit(t,adaptive,set(range(3)),'ADAPTIVE_PARITY');cases+=1
    ck(v[5]=={2:F(1)} and F(row['R'])==2)
    if not pilot:
        r,k=2,3;n=r*k+(1<<r);t=[]
        for x in range(1<<n):
            sign=(-1)**(x>>(r*k)).bit_count()
            for j in range(r):
                if (x>>(j*k))&((1<<k)-1)==(1<<k)-1:sign=-sign
            t.append(sign)
        def indexed(path,ll,tt):
            d=dict(path)
            for j in range(r):
                if j*k not in d:return j*k
            idx=r*k+sum(d[j*k]<<j for j in range(r))
            return idx if idx not in d else None
        A=set(range(0,r*k,k))|set(range(r*k,n))
        row,v=audit(tuple(t),indexed,A,'INDEXED_r2_k3');cases+=1
        p=F(1,2**(k-1));q=4*p*(1-p)
        jk=E.sub(E.hb(q/2),E.mul(E.hb(q),F(1,2)))
        ck(v[5]==E.sub({2:F(r)},E.mul(jk,r)) and v[6]['leafH']=={2:F(2)})
    ck(cases==(3 if pilot else 11));ck(time.perf_counter()-START<(60 if pilot else 120))
    result={'status':'PASS','cases':cases,'assertions':COUNT,'entropy_helper_assertions':E.ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'pilot':pilot,'float_used':False}
    save('PILOT.json' if pilot else 'RESULT.json',result);print(json.dumps(result))
if __name__=='__main__':main()
