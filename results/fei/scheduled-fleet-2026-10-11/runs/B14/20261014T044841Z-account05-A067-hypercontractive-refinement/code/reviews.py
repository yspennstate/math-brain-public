import itertools,json,time
from fractions import Fraction as Q
import check as h
START=time.perf_counter();COUNT=0
def ck(b):
    global COUNT
    COUNT+=1;assert b;assert time.perf_counter()-START<60
def log_form(x):
    return h.combine((h.ns['factors'](x.numerator),Q(1)),(h.ns['factors'](x.denominator),Q(-1)))
def lost(v,core,controls,keep_dummy=False):
    a=h.fwht(v);den=len(v)**2;out=[]
    for i in range(controls):
        bit=1<<(core+i);e=h.physical(v,[core+i])
        if not e:continue
        rows={}
        for s in range(len(a)):
            if s&bit:continue
            mu=Q(a[s|bit]**2,den)/e;ref=Q(a[s]**2+a[s|bit]**2,den)
            key=(s>>core, (s&1) if keep_dummy else 0)
            rows.setdefault(key,[]).append((mu,ref))
        loss={}
        for key,row in rows.items():
            pm=sum(t[0] for t in row);pr=sum(t[1] for t in row)
            if not pm:continue
            for mu,ref in row:
                if mu:loss=h.combine((loss,Q(1)),(log_form((mu/pm)/(ref/pr)),e*mu))
        lo,hi=h.interval(loss);delta=Q(1,1<<core)
        # First exposed child: old remaining-bent density=2delta and theta=1/2.
        bound=Q(256,9)*delta*e*(Q(1,4) if keep_dummy else 1)
        ck(hi*h.ns['LN2'][1]<=bound or not loss)
        ck(lo>=0 or not loss)
        out.append((e,loss))
    return out
gatecases=0
for r in [1,2,3]:
    for truth in range(1<<(1<<r)):
        gate=[1 if truth>>z&1 else -1 for z in range(1<<r)]
        bent=[(-1)**(((y&1)*((y>>1)&1))+(((y>>2)&1)*((y>>3)&1))) for y in range(16)]
        F=[bent[y]+(gate[z]-1 if y==0 else 0) for z in range(1<<r) for y in range(16)]
        G=[bent[y>>1]+(gate[z]-1 if y==0 else 0) for z in range(1<<r) for y in range(32)]
        lost(F,4,r);lost(G,5,r,True);gatecases+=2
        ah=Q(sum(gate),len(gate));ck(h.physical(F,range(4))==2+4*Q(1,16)*(1-ah))

# A068 direct signed identification and inherited-reference witness.
v=[1 if (x&1)==0 and (x&2)!=0 else -1 for x in range(4)]
coeff=h.fwht(v);ck([Q(c,4) for c in coeff]==[-Q(1,2),Q(1,2),-Q(1,2),-Q(1,2)])
G=[v[0],v[3]];ck(G==[-1,-1]);ck(h.physical(G,[0])==0)
reference=[Q(1,4),Q(2,5),Q(1,10),Q(1,4)];push=[reference[0]+reference[3],reference[1]+reference[2]];ck(push==[Q(1,2),Q(1,2)])

# A070 exposed-family influence/code guard and the final common-reference rescue.
fixtures=[]
def internal(bits):
    if len(bits)<=1:return []
    k=len(bits)//2
    return [sum(1<<i for i in bits)]+internal(bits[:k])+internal(bits[k:])
for t in [4,5,6]:
    n=2+2*t;N=1<<n;delta=Q(1,1<<t);vmask=((1<<t)-1)<<2;ymask=((1<<t)-1)<<(t+2)
    q1=[-1 if x&3==0 else 1 for x in range(N)]
    q2=[-1 if not(x&1) and not(x&vmask) else 1 for x in range(N)]
    core=[-1 if not(x&ymask) else 1 for x in range(N)]
    source=[a*b for a,b in zip(q1,core)];mask=[a*b for a,b in zip(q1,q2)];final=[a*b for a,b in zip(q2,core)]
    Ig=h.physical(source,range(n));Iq=h.physical(mask,range(n));If=h.physical(final,range(n))
    ck((Ig,Iq,If)==(1+2*t*delta,1+t*delta,(3*t+1)*delta))
    Y=list(range(t+2,n));V=list(range(2,t+2));control=(1<<(t+2))-1
    cells=[N-1,control,control^1]+internal(Y)+internal(V)
    a=h.fwht(source);gamma=Q(sum(c*c*(1+2*sum(bool(s&C) for C in cells)) for s,c in enumerate(a)),N*N)
    ck(gamma<=7*Ig)
    if t>=5:ck(7*Ig+12*Iq>26*If)
    fixtures.append({'t':t,'I_source':str(Ig),'I_mask':str(Iq),'I_final':str(If),'Gamma_source':str(gamma),'ancestral_bill_over_final_I':str((7*Ig+12*Iq)/If)})
ck(Q(5,4)>Q(5,6))
out={'assertions':COUNT,'A066_physical_cases':gatecases,'A068_push_reference':[str(p) for p in push],'A070_exposed_fixtures':fixtures,'runtime_seconds':time.perf_counter()-START}
(h.ROOT/'out/REVIEWS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
