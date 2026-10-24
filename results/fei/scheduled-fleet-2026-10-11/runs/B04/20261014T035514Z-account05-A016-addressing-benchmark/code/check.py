from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time,sys
RUN=Path(__file__).resolve().parents[1];spec=json.loads((RUN/'FROZEN_SPEC.json').read_text())
start=time.perf_counter();checks=0
def ck(b,label):
    global checks
    if not b:raise AssertionError(label)
    checks+=1
    if time.perf_counter()-start>60:raise RuntimeError('Frozen60-second limit exceeded')
def fwht(v):
    v=list(v);step=1
    while step<len(v):
        for k in range(0,len(v),step*2):
            for j in range(k,k+step):
                x,y=v[j],v[j+step];v[j]=x+y;v[j+step]=x-y
        step*=2
    return v
def coreln(q):
    z=(q-1)/(q+1);p=z;out=F(0)
    for k in range(36):out+=2*p/(2*k+1);p*=z*z
    return out,out+2*p/(73*(1-z*z))
ln2lo,ln2hi=coreln(F(2));cache={}
def lg(q):
    if q in cache:return cache[q]
    original=q;k=0
    while q>=2:q/=2;k+=1
    lo,hi=coreln(q);D=1<<90
    out=F(((k+lo/ln2hi)*D).__floor__(),D),F(((k+hi/ln2lo)*D).__ceil__(),D)
    cache[original]=out;return out
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y,x[1]*y
def ent(ws):
    den=len(ws)**2;out=(F(0),F(0))
    for mass,count in Counter(v*v for v in ws).items():
        if mass:out=add(out,mul(lg(F(den,mass)),F(mass*count,den)))
    return out
def B(ws,i):
    out=(F(0),F(0));den=len(ws)**2;bit=1<<i
    rows=Counter((ws[s]**2,ws[s|bit]**2) for s in range(len(ws)) if not s&bit)
    for (p,q),count in rows.items():
        if p and q:
            out=add(out,mul(lg(F(p+q,p)),F(count*p,den)))
            out=add(out,mul(lg(F(p+q,q)),F(count*q,den)))
    return out
def Inf(ws,i):return F(sum(v*v for s,v in enumerate(ws) if s&(1<<i)),len(ws)**2)
def I(ws):return F(sum(v*v*s.bit_count() for s,v in enumerate(ws)),len(ws)**2)
def connected(truth):
    n=len(truth).bit_length()-1;poly=[(1-x)//2 for x in truth]
    for i in range(n):
        for s in range(len(poly)):
            if s&(1<<i):poly[s]^=poly[s^(1<<i)]
    parent=list(range(n))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    for s,v in enumerate(poly):
        if v and s:
            first=(s&-s).bit_length()-1
            for i in range(first+1,n):
                if s&(1<<i):parent[find(i)]=find(first)
    return len(set(find(i) for i in range(n)))==1
def restrict(truth,fixed):
    n=len(truth).bit_length()-1;rem=[i for i in range(n) if i not in fixed]
    out=[];base=sum(v<<i for i,v in fixed.items())
    for r in range(1<<len(rem)):
        s=base+sum(((r>>j)&1)<<i for j,i in enumerate(rem));out.append(truth[s])
    return out,rem
def splice_value(word,a,m):
    value=1
    for j in range(a):
        block=(word>>(j*(m+1)))&((1<<(m+1))-1);x=block&1;t=block>>1;e=0
        for k in range(0,m,2):e^=((t>>k)&1)*((t>>(k+1))&1)
        value*=1-2*e-2*x*int(t==0)
    return value
records=[];pilot='--pilot' in sys.argv
for a,m,M in (spec['pilot_domain'] if pilot else spec['domain']):
    D=a*(m+1);n=1+M+D;delta=F(1,1<<m);Ns=1<<D
    s=[splice_value(r,a,m) for r in range(Ns)];sw=fwht(s)
    Is=a*(F(m,2)+(m+1)*delta);ck(I(sw)==Is,'mask influence')
    truth=[1 if not r&1 else (-1 if ((r>>1)&((1<<M)-1)).bit_count()%2 else 1)*s[r>>(M+1)] for r in range(1<<n)]
    ws=fwht(truth);den=len(ws)**2;expectedI=(M+Is+1)/2
    ck(I(ws)==expectedI,'root I');ck(connected(truth),'root finest factor connected')
    for i in range(n):
        direct=F(sum(truth[r]!=truth[r^(1<<i)] for r in range(len(truth))),len(truth))
        ck(direct==Inf(ws,i),'physical root influence')
    hmask=((1<<M)-1)<<1;active_mass=F(0)
    for r,v in enumerate(ws):
        hp=r&hmask;sr=r>>(M+1)
        if hp==hmask:
            ck(v==((-1 if r&1 else 1)*(1<<M)*sw[sr]),'fixed active coefficients')
            active_mass+=F(v*v,den)
        elif hp==0 and sr==0:ck(v==len(ws)//2,'constant coefficients')
        else:ck(v==0,'no unsupported reference rows')
    ck(active_mass==F(1,2),'active true mass')
    Qmass=F(2,4)+F(2*Ns,4*Ns);ck(Qmass==1,'complete reference normalization')
    CE=2+F(D,2);ck(CE<=4*expectedI,'complete cost paid')
    hs=ent(sw);hr=ent(ws);formulaH=add((F(2),F(2)),mul(hs,F(1,2)))
    ck(hr[0]<=formulaH[1] and formulaH[0]<=hr[1],'entropy spectral split')
    rootgateB=B(ws,0);ck(Inf(ws,0)==F(1,2),'private gate influence')
    ck(rootgateB[1]<=1,'private gate K2 good')
    # Check both actual gate-first terminals and the full influence telescope.
    zero,rz=restrict(truth,{0:0});one,ro=restrict(truth,{0:1});zw=fwht(zero);ow=fwht(one)
    ck(all(v==1 for v in zero) and I(zw)==0,'constant terminal')
    ck(I(ow)==M+Is,'active terminal I')
    ck(expectedI==F(1,2)+(I(zw)+I(ow))/2,'gate-first physical telescope')
    ck(F(D,2)<=4*(I(zw)+I(ow))/2,'both terminal costs paid')
    total=F(0);corebill=F(0);localized=F(0);nodes=[]
    for j in range(a):
        for prefix in range(1<<j):
            fixed={1+M+k*(m+1):(prefix>>k)&1 for k in range(j)}
            node,rem=restrict(truth,fixed);nw=fwht(node);qi=rem.index(1+M+j*(m+1));inf=Inf(nw,qi);er=B(nw,qi)
            ck(inf==delta/2,'selector influence at actual descendant')
            ck(connected(node),'finest factor connected at descendant')
            if m>=6:ck(er[0]>=inf*(m-1),'exact all-descendant bad lower bound')
            ck(er[0]>4*inf,'actual K4 bad')
            bill=F(2*sum(v*v*(s.bit_count()-1) for s,v in enumerate(nw) if s&(1<<qi)),len(nw)**2)
            # Sum only h-coordinate spectral derivative energy; independent of mask spectators.
            hinds=[rem.index(i) for i in range(1,M+1)]
            cb=F(2*sum(v*v*sum(bool(s&(1<<i)) for i in hinds) for s,v in enumerate(nw) if s&(1<<qi)),len(nw)**2)
            ck(cb==M*delta,'same private core exact charge')
            total+=bill/F(1<<j);corebill+=cb/F(1<<j);localized+=bill/F(1<<j)
            nodes.append({'depth':j,'prefix':prefix,'Inf':str(inf),'B_lower':str(er[0]),'B_upper':str(er[1]),'B_over_Inf_lower':str(er[0]/inf),'2I_D':str(bill),'private_h_charge':str(cb),'bad_K4':True,'connected':True})
    raw=a*(M+F(1,2))*delta+F(a*a*m,2)*delta+F(a*(a-1)*(2*m+1),2)*delta**2
    ck(total==raw==localized,'full localized bill formula');ck(corebill==a*M*delta,'repeated core exact total')
    selector_terminal_cost=2+F(a*m,2)
    for prefix in range(1<<a):
        fixed={1+M+k*(m+1):(prefix>>k)&1 for k in range(a)}
        leaf,rem=restrict(truth,fixed);lw=fwht(leaf)
        branchI=F(a*m,2)+2*m*delta*prefix.bit_count()
        ck(I(lw)==(M+branchI+1)/2,'selector-first actual terminal influence')
        ck(selector_terminal_cost<=4*I(lw),'selector-first complete terminal code paid')
        ck(F(2,4)+F(2*(1<<(a*m)),4*(1<<(a*m)))==1,'selector-first leaf reference normalized')
    rec={'a':a,'m':m,'M':M,'n':n,'I_mask':str(Is),'I':str(expectedI),'raw_and_localized_K4_bill':str(total),'core_only_bill':str(corebill),'localized_bill_over_I':str(total/expectedI),'core_bill_over_I':str(corebill/expectedI),'complete_Q_mass':str(Qmass),'complete_CE':str(CE),'complete_CE_over_I':str(CE/expectedI),'gate_first_bad_bill':'0','gate_first_B_lower':str(rootgateB[0]),'gate_first_B_upper':str(rootgateB[1]),'terminal_average_CE':str(F(D,2)),'selector_first_terminal_average_CE':str(selector_terminal_cost),'nodes':nodes}
    records.append(rec);(RUN/'out'/('PILOT_PARTIAL.json' if pilot else 'PARTIAL.json')).write_text(json.dumps({'records':records},indent=2)+'\n')
result={'helper_version':spec['helper_version'],'pilot':pilot,'cases':len(records),'assertions':checks,'failures':0,'elapsed_seconds':time.perf_counter()-start,'records':records,'full_FEI':'OPEN'}
(RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['helper_version','pilot','cases','assertions','failures','elapsed_seconds']}))
