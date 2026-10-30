import json,time
from fractions import Fraction as Q
import check as h
START=time.perf_counter(); assertions=0
def ck(b):
    global assertions
    assertions+=1
    assert b
    assert time.perf_counter()-START<60
def logbits(x):return h.log(x)
def c_bits(a,b):
    q=a*a+b*b; lo=hi=Q(0)
    for t in [a+b,a-b]:
        if not t:continue
        l,u=logbits(t*t/q);lo+=t*t*l/2;hi+=t*t*u/2
    return lo,hi
records=[]
for m in range(2,6):
    N=1<<(2*m);d=Q(1,N);A=Q(1,1<<m)
    bent=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m)) for x in range(N)]
    # z is the last bit: z=+ leaves g, z=- flips the zero vertex.
    F=bent+[-bent[0]]+bent[1:];coeff=h.fwht(F)
    ck(h.physical(F,[2*m])==d);ck(Q(coeff[N],2*N)==d)
    ck(h.physical(F,range(2*m+1))==m+(2*m+1)*d)
    core=h.fwht(bent);ck(all(abs(a)==1<<m for a in core))
    nplus=sum(a>0 for a in core);ck(nplus==(N+(1<<m))//2)
    low=high=Q(0)
    for s in range(1,N):
        aa=Q(coeff[s],2*N);bb=Q(coeff[s+N],2*N)
        ck(bb==d);l,u=c_bits(aa,bb);low+=l;high+=u
    l,u=logbits(1/(d*d));low+=d*d*l;high+=d*d*u
    # Convert base-2 row charges to natural logs with proved rational ln2 bounds.
    lower=low*h.ns['LN2'][0]/d;upper=high*h.ns['LN2'][1]/d
    ck(lower>2)
    if m==2:ck(lower>Q(217,100))
    records.append({'m':m,'rate_lower':str(lower),'rate_upper':str(upper)})

# New direct paired-input reconstruction, independent of source code.
q=[1 if x&1 else (-1)**(((x>>1)&1)+((x>>2)&1)) for x in range(16)]
y=[(-1)**((x>>3)&1) for x in range(16)];g=[a*b for a,b in zip(q,y)]
cells=[15,7,6]
def gamma(v):
    a=h.fwht(v)
    return Q(sum(c*c*(1+2*sum(bool(s&C) for C in cells)) for s,c in enumerate(a)),256)
rt=Q(0)
for C in cells:
    choices=[t for t in range(16) if not(t&~C)]
    both=sum(g[x]!=g[(x&~C)|t] and q[x]!=q[(x&~C)|t] for x in range(16) for t in choices)
    rt+=8*Q(both,16*len(choices))
ri=2*Q(sum(g[x]!=g[x^(1<<i)] and q[x]!=q[x^(1<<i)] for i in range(4) for x in range(16)),16)
Ig=h.physical(g,range(4));Iq=h.physical(q,range(4));If=h.physical(y,range(4))
ck((Iq,Ig,If)==(Q(3,2),Q(5,2),Q(1)))
ck((gamma(q)-1,gamma(g),gamma(y),rt,ri)==(Q(4),Q(11,2),Q(3),Q(13,2),Q(3)))
banks=[12*Ig-gamma(g),12*Iq-(gamma(q)-1),rt-12*ri]
ck(banks==[Q(49,2),Q(14),-Q(59,2)]);ck(sum(banks)==12*If-gamma(y)==9)
ck(Q(28800,42961)>Q(100,169));ck(28800*169-100*42961==571100)
out={'assertions':assertions,'runtime_seconds':time.perf_counter()-START,'A066_exact_rows':records,'A070_refund':str(rt),'A070_physical_refund':str(ri),'A070_banks':[str(a) for a in banks],'A070_real_gap':571100}
(h.ROOT/'out/REVIEWS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='A066_exact_rows'}))
