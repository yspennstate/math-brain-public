import json,time,math
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
SRC=Path('~/brain_workers/FEI100_20261011/agents/A032/runs/20261011T234647Z-fleet05-A032-boolean-phase-realizability/out/mixed_slices_m4.json')
start=time.monotonic(); assertions=0
def ck(v):
    global assertions
    assertions+=1
    assert v
    if time.monotonic()-start>55: raise RuntimeError('frozen55-second cap')
def fw(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return a
def factors(n):
    d=2;out=Counter()
    while d*d<=n:
        while n%d==0:out[d]+=1;n//=d
        d+=1
    if n>1:out[n]+=1
    return out
def odd(n):
    if n==0:return 1
    while n%2==0:n//=2
    return n
def nu(n):return sum(factors(odd(n)).values())
def permissible(n):return all(p%4==1 for p in factors(odd(n)))

def ln_interval(x):
    x=F(x);e=0
    while x>=2:x/=2;e+=1
    while x<1:x*=2;e-=1
    z=(x-1)/(x+1);n=32
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    hi=lo+2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    if e:
        a,b=ln_interval(F(2)) if False else LN2
        lo,hi=(lo+e*a,hi+e*b) if e>0 else (lo+e*b,hi+e*a)
    return lo,hi
z=F(1,3);LN2=(2*sum((z**(2*j+1)/F(2*j+1) for j in range(32)),F(0)),F(0))
LN2=(LN2[0],LN2[0]+2*z**65/(F(65)*(1-z*z)))
def log2i(n):
    a,b=ln_interval(n);return a/LN2[1],b/LN2[0]
LOG={n:log2i(n) for n in range(1,65)}
def entropy(norms,den):
    base=den.bit_length()-1;lo=hi=F(base)
    for s in norms:
        if s:
            a,b=LOG[s];lo-=F(s,den)*b;hi-=F(s,den)*a
    return lo,hi

# Necessary norm configurations: no reliance on catalogue completeness.
eligible=0;raw=0;worst=None;min_margin=None
records=[]
for mu in range(17):
    t=16-mu
    for e0 in range(t+1):
        for e1 in range(t-e0+1):
            for e2 in range(t-e0-e1+1):
                e3=t-e0-e1-e2
                ss=[mu+4*e for e in [e0,e1,e2,e3]];raw+=1
                if not all(permissible(s) for s in ss):continue
                eligible+=1
                upperL=sum((F(s,64)*nu(s) for s in ss),F(0))
                ix=F(ss[1]+ss[2]+2*ss[3],64)
                hlo,hhi=entropy(ss,64);dlo,dhi=hlo+ix,hhi+ix
                if upperL==0:continue
                ck(dlo>0)
                margin=F(5,2)*dlo-upperL;ck(margin>0)
                if min_margin is None or margin<min_margin:min_margin=margin
                ratio_hi=upperL/dlo
                if worst is None or ratio_hi>worst[0]:worst=(ratio_hi,ss,upperL,dlo,dhi,mu)
                records.append({'norms':ss,'mu':mu,'L_upper':str(upperL),'D_interval':[str(dlo),str(dhi)],'margin_lower':str(margin)})
ck(raw==4845)
(ROOT/'out/norm_certificate.json').write_text(json.dumps({'raw_configurations':raw,'eligible_configurations':eligible,'nonzero_records':len(records),'target':'5/2','records':records},indent=2)+'\n',encoding='utf-8')

# Exact component check in different representation from A032 template search.
data=json.loads(SRC.read_text());rows=data['records'];ck(len(rows)==45088)
stats=Counter();normN={};nonfair=0
for row in rows:
    vals=row['truth_h'];ck(set(vals)<={-2,-1,0,1,2})
    w=fw(vals);sq=[z*z for z in w];total=sum(sq)
    sn=sum(z*z for z in vals);ck(total==16*sn)
    ck(sn==row['norm_integer'])
    marg=[sum(z for s,z in enumerate(sq) if (s>>i)&1) for i in range(4)]
    N=sum(0<a<total and 2*a!=total for a in marg)
    ck(permissible(sn) and N<=nu(sn))
    # Integer product identity, zero-safe and exact.
    for s,z in enumerate(sq):
        ck(z*total**3==math.prod(marg[i] if (s>>i)&1 else total-marg[i] for i in range(4)))
    mask=sum(1<<i for i,z in enumerate(vals) if abs(z)==1)
    ck(mask==row['mixed_mask'])
    ck((sn-mask.bit_count())%4==0)
    stats[N]+=1;normN[sn]=max(normN.get(sn,0),N);nonfair+=N>0

# Actual point-defect family: r X addresses, ONE data bit; product condition vacuous.
direct=[];compressed=[]
for r in range(1,41):
    p=F(1,1<<r);w0=(1-p)**2+p*p;eta=1-w0
    ix=r*p
    # H(w) <= eta log2(e/eta) + eta*r; bound ln2>1/2,
    # eta>=p and eta<=2p imply H(w)+I_X<=(5r+4)p.
    Dupper=(5*r+4)*p
    lower=w0/Dupper
    if r>=2:ck(w0>F(1,2))
    compressed.append({'r':r,'w0':str(w0),'N_empty':int(r>=2),'I_X':str(ix),'D_upper':str(Dupper),'ratio_lower':str(lower) if r>=2 else None})
    if r>10:continue
    vals=[-1]+[1]*((1<<(r+1))-1);w=fw(vals);den=1<<(2*(r+1))
    ww=[F(w[j]**2+w[j+(1<<r)]**2,den) for j in range(1<<r)]
    ck(ww[0]==w0 and all(z==2*p*p for z in ww[1:]))
    ixx=F(sum((s&((1<<r)-1)).bit_count()*z*z for s,z in enumerate(w)),den)
    iyy=F(sum(((s>>r)&1)*z*z for s,z in enumerate(w)),den)
    ck(ixx==ix and iyy==p)
    ne=0
    for j,a in enumerate(ww):
        q=F(w[j+(1<<r)]**2,den)/a
        if q not in [0,F(1,2),1]:ne+=a
    ck(ne==(w0 if r>=2 else 0))
    physical=F(sum(vals[s]!=vals[s^(1<<i)] for s in range(len(vals)) for i in range(r)),len(vals))
    ck(physical==ix)
    direct.append({'r':r,'L':str(ne),'I_X':str(ix),'I_Y':str(iyy),'one_data_bit':True})

# Norm-only fixed-two-address candidate at m=5 passes primitive norm and parity.
# Dominant h row would need three nonfair 1:3 ratios and two fair ones.
P=32;amag=[3**((s&7).bit_count()) for s in range(P)]
ck(sum(z*z for z in amag)==P*125)
ck(all(z%2==1 for z in amag))
ck(max(amag)<=2*P)
gauge_divisor=3**3
# Shift all five coordinates pairs every magnitude to complement: product27.
ck(all(amag[s]*amag[s^31]==gauge_divisor for s in range(P)))
ck((-3*P)%gauge_divisor!=0)
norm_warning={'m':5,'norms':[125,1,1,1],'magnitude_template':'three1:3 and two1:1 coordinates','square_norm':sum(z*z for z in amag),'all_odd':True,'max_coefficient':max(amag),'required_autocorrelation':-3*P,'divisor':gauge_divisor,'remainder':(-3*P)%gauge_divisor,'verdict':'NO common physical phases for concentrated single-point mixed mask'}

out={'status':'PASS','assertions':assertions,'seconds':time.monotonic()-start,'norm_raw':raw,'norm_eligible':eligible,'nonzero_norm_records':len(records),'norm_worst':{'ratio_upper':str(worst[0]),'norms':worst[1],'L_upper':str(worst[2]),'D_interval':[str(worst[3]),str(worst[4])],'mu':worst[5]},'catalogue_rows':len(rows),'N_distribution':dict(stats),'norm_max_N':normN,'nonfair_rows':nonfair,'direct_point_defects':direct,'compressed_point_defects':compressed,'norm_only_warning':norm_warning}
(ROOT/'out/validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['direct_point_defects','compressed_point_defects','norm_max_N','norm_worst']},indent=2))
print('worst norm tuple',worst[1],'ratio upper approximate',float(worst[0]))
