from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time
RUN=Path(__file__).resolve().parents[1];(RUN/'out').mkdir(exist_ok=True)
start=time.perf_counter();assertions=0
def ck(b):
    global assertions
    assert b
    assertions+=1
    if time.perf_counter()-start>60:raise RuntimeError('Frozen 60-second limit exceeded')
def fwht(v):
    v=list(v);step=1
    while step<len(v):
        for k in range(0,len(v),2*step):
            for j in range(k,k+step):
                u,w=v[j],v[j+step];v[j]=u+w;v[j+step]=u-w
        step*=2
    return v
def coreln(q):
    z=(q-1)/(q+1);power=z;tot=F(0)
    for k in range(36):tot+=2*power/F(2*k+1);power*=z*z
    return tot,tot+2*power/(F(73)*(1-z*z))
ln2lo,ln2hi=coreln(F(2));cache={}
def lg(q):
    q=F(q);assert q>=1
    if q in cache:return cache[q]
    orig=q;k=0
    while q>=2:q/=2;k+=1
    lo,hi=coreln(q);lo=k+lo/ln2hi;hi=k+hi/ln2lo
    D=1<<100;out=(F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D))
    ck(out[0]<=lo<=hi<=out[1]);cache[orig]=out;return out
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,b):return (a[0]*b,a[1]*b) if b>=0 else (a[1]*b,a[0]*b)
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def entropy_counts(counts,den):
    ans=(F(0),F(0))
    for mass,count in counts.items():
        if mass:ans=add(ans,scale(lg(F(den,mass)),F(count*mass,den)))
    return ans
def H(w):return entropy_counts(Counter(t*t for t in w),len(w)**2)
def B(w,i):
    bit=1<<i
    grouped=Counter(w[s]**2+w[s|bit]**2 for s in range(len(w)) if not s&bit)
    return sub(H(w),entropy_counts(grouped,len(w)**2))
def render(x):return {'lower':str(x[0]),'upper':str(x[1]),'display':[float(x[0]),float(x[1])]}
def phase_components(truth):
    phase=[(1-v)//2 for v in truth];n=(len(truth)).bit_length()-1
    for i in range(n):
        for s in range(len(phase)):
            if s&(1<<i):phase[s]^=phase[s^(1<<i)]
    parents=list(range(n))
    def find(i):
        while parents[i]!=i:i=parents[i]
        return i
    for mask,p in enumerate(phase):
        if p and mask:
            inds=[i for i in range(n) if mask&(1<<i)]
            for i in inds[1:]:parents[find(i)]=find(inds[0])
    groups={}
    for i in range(n):groups.setdefault(find(i),[]).append(i)
    return list(groups.values())
def truth_value(word,a,m):
    z=word&1;value=1
    for j in range(a):
        block=(word>>(1+j*m))&((1<<m)-1);x=block&1;t=block>>1
        exponent=z*(t&1)
        for k in range((m-2)//2):exponent^=((t>>(1+2*k))&1)*((t>>(2+2*k))&1)
        b=1-2*(exponent&1)
        value*=b-2*x*int(z==0 and t==0)
    return value
def restrict(truth,fixed,n):
    remaining=[i for i in range(n) if i not in fixed];out=[]
    for bits in range(1<<len(remaining)):
        word=sum(v<<i for i,v in fixed.items())
        word+=sum(((bits>>j)&1)<<i for j,i in enumerate(remaining))
        out.append(truth[word])
    return out,remaining
records=[]
for a,m in [(1,4),(2,4),(3,4),(1,6),(2,6),(1,10)]:
    n=1+a*m;truth=[truth_value(s,a,m) for s in range(1<<n)];w=fwht(truth);den=len(w)**2
    delta=F(1,1<<m);Jc=F(m-2,2)+2*(m-1)*delta;Lc=Jc+2*delta
    Iz=(1-(-2*delta)**a)/2;Iexpected=a*(F(m-1,2)+m*delta)+Iz
    I=sum((F(t*t,den)*s.bit_count() for s,t in enumerate(w)),F(0));ck(I==Iexpected)
    for i in range(n):
        influence=F(sum(truth[s]!=truth[s^(1<<i)] for s in range(len(truth))),len(truth))
        spectral=sum((F(v*v,den) for s,v in enumerate(w) if s&(1<<i)),F(0))
        ck(influence==spectral)
        expected=Iz if i==0 else (delta if (i-1)%m==0 else F(1,2)+delta)
        ck(influence==expected)
    comps=phase_components(truth);ck(len(comps)==1);ck(len(comps[0])==n)
    Traw=F(0);Tfactor=F(0);node_records=[]
    for j in range(a):
        for prefix in range(1<<j):
            fixed={1+k*m:(prefix>>k)&1 for k in range(j)}
            node,rem=restrict(truth,fixed,n);qi=rem.index(1+j*m);nw=fwht(node)
            inf=sum((F(v*v,len(nw)**2) for s,v in enumerate(nw) if s&(1<<qi)),F(0));ck(inf==delta)
            erasure=B(nw,qi);ck(erasure[0]>=delta*F(m-1,2))
            bit=1<<qi;dt=[]
            for s in range(len(node)):
                if not s&bit:dt.append((node[s]-node[s|bit])//2)
            dw=fwht(dt);drem=[i for i in range(len(rem)) if i!=qi];dden=len(dw)**2
            energies=[sum((F(v*v,dden) for s,v in enumerate(dw) if s&(1<<r)),F(0)) for r in range(len(drem))]
            ck(sum(F(v*v,dden) for v in dw)==delta)
            groups=phase_components(node);component=next(g for g in groups if qi in g)
            retained=set(component)-{qi}
            raw=sum(energies,F(0));factored=sum((e for r,e in enumerate(energies) if drem[r] in retained),F(0))
            ck(all(rem.index(1+k*m) in component for k in range(j,a)))
            zeros=j-prefix.bit_count()
            ck(raw-factored==delta*zeros*F(m-2,2))
            Traw+=2*raw/F(1<<j);Tfactor+=2*factored/F(1<<j)
            node_records.append({'selector_index':j,'prefix':prefix,'Inf':str(inf),'B_over_Inf':render(scale(erasure,1/inf)),'raw_2I_D':str(2*raw),'factor_removed_2I_D':str(2*factored),'factor_component_original_coordinates':[rem[k] for k in component]})
    raw_formula=a*m*delta+delta*a*(a-1)*(Jc+Lc)
    factor_formula=raw_formula-delta*a*(a-1)*F(m-2,4)
    ck(Traw==raw_formula);ck(Tfactor==factor_formula)
    child0,r0=restrict(truth,{0:0},n);child1,r1=restrict(truth,{0:1},n)
    w0,w1=fwht(child0),fwht(child1);cd=len(w0)**2
    I0=sum((F(v*v,cd)*s.bit_count() for s,v in enumerate(w0)),F(0))
    I1=sum((F(v*v,cd)*s.bit_count() for s,v in enumerate(w1)),F(0))
    ck(I0==a*Lc);ck(I1==F(a*m,2));ck(I==Iz+(I0+I1)/2)
    h0,h1=H(w0),H(w1);ck(h1[0]<=a*(m-2)<=h1[1]);ck(h0[1]<=4*I0)
    bz=B(w,0);ck(bz[1]<=F(8,3)*Iz);ck(Iz>=F(3,8))
    # Exact fixed root reference: Q(z-Fourier-bit,R)=(Q0(R)+Q1(R))/4.
    def support1(r):
        return all(not r&(1<<(j*m)) and r&(1<<(j*m+1)) for j in range(a))
    Qsum=F(0);alpha=F(0);CE=(F(0),F(0));totalmass=F(0)
    lbig=lg(1+4**a)
    for s,v in enumerate(w):
        r=s>>1;inside=support1(r)
        q=F(1+4**a if inside else 1,4*(1<<(a*m)))
        Qsum+=q;p=F(v*v,den);totalmass+=p
        if inside:alpha+=p
        codecost=sub((F(a*m+2),F(a*m+2)),lbig) if inside else (F(a*m+2),F(a*m+2))
        CE=add(CE,scale(codecost,p))
        ck(F(w[2*r]**2+w[2*r+1]**2,den)==F(w0[r]**2+w1[r]**2,2*cd))
    ck(Qsum==1);ck(totalmass==1);ck(alpha==(1+delta**a)/2)
    formulaCE=sub((F(a*m+2),F(a*m+2)),scale(lbig,alpha))
    ck(CE==formulaCE);ck(CE[1]<=F(8,3)*I);ck(H(w)[1]<=CE[0])
    record={'a':a,'m':m,'n':n,'rows':len(truth),'I':str(I),'I_z':str(Iz),'root_factor_components':len(comps),'raw_selector_tree_charge':str(Traw),'factor_removed_selector_tree_charge':str(Tfactor),'raw_charge_over_I':str(Traw/I),'factor_removed_charge_over_I':str(Tfactor/I),'z_first_B_over_Inf':render(scale(bz,1/Iz)),'z0_terminal_H':render(h0),'z1_terminal_H':render(h1),'z0_terminal_I':str(I0),'z1_terminal_I':str(I1),'root_reference_CE':render(CE),'root_reference_CE_over_I':render(scale(CE,1/I)),'root_reference_Q_mass':str(Qsum),'root_reference_support1_spectral_mass':str(alpha),'selector_nodes':node_records}
    records.append(record)
    (RUN/'out/PARTIAL.json').write_text(json.dumps({'records':records},indent=2)+'\n',encoding='utf8')
result={'helper_version':'A016-shared-spine-v1','assertions':assertions,'failures':0,'elapsed_seconds':time.perf_counter()-start,'records':records,'arithmetic':'integer/Fraction, exact GF(2) ANF factorization, rational outward log intervals','full_fei':'OPEN'}
(RUN/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['helper_version','assertions','failures','elapsed_seconds']}))
for r in records:print(json.dumps({k:r[k] for k in ['a','m','I','raw_charge_over_I','factor_removed_charge_over_I','root_reference_CE_over_I']}))
