from pathlib import Path
from fractions import Fraction as F
import json,math,time,sys
import arithmetic as a
R=Path(__file__).resolve().parents[1]
J=[-a.TABLE[z^1] for z in range(64)]
C=a.mobius(J)
check=a.check
add,sub,mul,phi,entropy=a.add,a.sub,a.mul,a.phi,a.entropy
def save(name,x):
    (R/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,tuple):return {'exact':[str(z) for z in x],'display':[float(z) for z in x]}
    if isinstance(x,list):return [encode(z) for z in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x
def overlap(x,y):return max(x[0],y[0])<=min(x[1],y[1])
def spectral(table):
    # Characters represented by sets of inputs where they are negative.
    N=len(table);n=(N-1).bit_length();neg=sum(1<<x for x,y in enumerate(table) if y<0);M=neg.bit_count()
    planes=[sum(1<<x for x in range(N) if x>>i&1) for i in range(n)]
    chars=[0]*N;w=[F(N-2*M,N)]
    for s in range(1,N):
        bit=s&-s;i=bit.bit_length()-1
        chars[s]=chars[s^bit]^planes[i]
        w.append(F(-2*(M-2*(neg&chars[s]).bit_count()),N))
    mu=[v*v for v in w];check(sum(mu)==1)
    inf=[];B=[]
    for i in range(n):
        d=F(sum(table[x]!=table[x^(1<<i)] for x in range(N)),N)
        check(d==sum(mu[s] for s in range(N) if s>>i&1));inf.append(d)
        b=(F(0),F(0))
        for s in range(N):
            if not s>>i&1:b=add(b,phi(mu[s],mu[s|(1<<i)]))
        B.append(b)
    return w,mu,inf,B,entropy(mu)
def outer(p):
    b=a.centered(C,p);law=a.masses(C,p);v=4*p*(1-p);m=1-2*p
    check(sum(law)==1)
    sigma=(1-b[0])/2
    check(sigma==4*p-10*p*p+18*p**3-19*p**4+10*p**5-2*p**6)
    qs=[]
    for j in range(6):
        physical=F(0)
        for z in range(64):
            if not z>>j&1:
                # Other five bits only; own coordinate irrelevant to pivotal event.
                physical+=(J[z]!=J[z|(1<<j)])*p**z.bit_count()*(1-p)**(5-z.bit_count())
        spectral=sum(law[s] for s in range(64) if s>>j&1)/v
        check(physical==spectral);check(0<physical<=1);qs.append(physical)
    Q=sum(qs);Cp=sub(entropy(law),mul(entropy([v,1-v]),Q))
    check(sum(s.bit_count()*law[s] for s in range(64))==v*Q)
    return b,law,qs,Q,Cp,sigma
def reserve(law,j,t,p,q):
    v=4*p*(1-p);m=1-2*p;out=(F(0),F(0))
    for s in range(64):
        if not s>>j&1:out=add(out,phi(law[s],t*law[s|(1<<j)]/v))
    return sub(out,mul(phi(m*m,t),q))
def direct(mask):
    g=[-1 if mask>>x&1 else 1 for x in range(4)]
    w,mu,ds,B,H=spectral(g);p=F(mask.bit_count(),4)
    b,law,qs,Q,Cp,sigma=outer(p)
    table=[]
    for x in range(4096):
        z=sum((g[(x>>(2*j))&3]<0)<<j for j in range(6));table.append(J[z])
    fw,fmu,fd,fB,fH=spectral(table)
    for S in range(4096):
        pattern=0;coef=F(1)
        for j in range(6):
            inner=(S>>(2*j))&3
            if inner:pattern|=1<<j;coef*= -w[inner]/2
        check(fw[S]==b[pattern]*coef)
    check(F(sum(y<0 for y in table),4096)==sigma)
    for j in range(6):
        for i in range(2):
            check(fd[2*j+i]==qs[j]*ds[i])
            res=reserve(law,j,w[1<<i]**2,p,qs[j])
            check(overlap(fB[2*j+i],add(mul(B[i],qs[j]),res)))
            if ds[i]==0:check(fd[2*j+i]==0);check(fB[2*j+i]==(0,0))
    check(overlap(fH,add(mul(H,Q),Cp)))
    check(sum(fd)==Q*sum(ds))
    return encode({'core_mask':mask,'p':p,'child_bits':12,'direct_coefficients':4096,'physical_directions':12,'Q':Q,'Cp':Cp,'direct_child_H':fH,'direct_child_I':sum(fd),'sigma':sigma,'status':'PASS'})
def rare(r):
    p=F(1,1<<r);g=[-1]+[1]*((1<<r)-1)
    w,mu,ds,B,H=spectral(g);b,law,qs,Q,Cp,sigma=outer(p)
    check(3*p<sigma<4*p);check(Q>=F(11,4))
    invln2=(F(a.SCALE,a.LN2[1]),F(a.SCALE,a.LN2[0]))
    # log2(e/(5p)) = log2(e)-log2(5p).
    price=mul(sub(invln2,a.log2_bounds(5*p)),120*p*p)
    check(Cp[1]<price[0])
    normalization=mul(Cp,1/(Q*sum(ds)))
    check(normalization[1]<F(240,11)*p)
    loss=mul(sub(invln2,a.log2_bounds(4*p*p)),2*p)
    blocks=[]
    for j in range(6):
        q=qs[j];t=w[1]**2;res=reserve(law,j,t,p,q)
        change=mul(res,1/(q*ds[0]))
        check(change[0]>-loss[0])
        check(min(q,1-q)<=5*p)
        blocks.append({'block':j,'q':q,'reserve':res,'E_change':change})
    return encode({'r':r,'p':p,'child_bits':6*r,'sigma':sigma,'Q':Q,'Cp':Cp,'Cp_normalized':normalization,'loss_bound':loss,'all6_blocks':blocks,'status':'PASS'})
def polynomial_audit():
    counts=[sum(J[z]<0 and z.bit_count()==k for z in range(64)) for k in range(7)]
    check(counts==[0,4,10,18,15,6,1])
    poly=[F(0)]*7
    for k,c in enumerate(counts):
        for j in range(7-k):poly[k+j]+=c*math.comb(6-k,j)*(-1)**j
    check(poly==list(map(F,[0,4,-10,18,-19,10,-2])))
    piv=[j for j in range(6) if J[0]!=J[1<<j]];check(piv==[1,2,3,5])
    low=4-F(10,16)-F(19,16**3)-F(2,16**5);check(low>3)
    high=-10+F(18,16)+F(10,16**3);check(high<0)
    # Rigorous universal entropy-price sums, independent of finite samples.
    check(F(3,16)*(F(31,4)+F(3,2))==F(111,64));check(3**4<2**7)
    check(a.LN2[0]>F(2,3)*a.SCALE)
    check(F(240,11)*F(3,32)==F(45,22))
    return encode({'negative_weight_counts':counts,'sigma_coefficients':poly,'dominant_pivotal_directions':piv,'sigma_over_p_lower_bound':low,'negative_upper_correction':high,'geometric_sum_p_bound':F(3,32),'entropy_price_bound':F(45,22),'erasure_price_strict_bound':F(111,64)})
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    analytic=polynomial_audit();children=[];probes=[]
    for mask in ([1] if pilot else [1,14,6,10]):
        children.append(direct(mask));save('PILOT_PARTIAL.json' if pilot else 'DIRECT_PARTIAL.json',children)
    for r in ([4] if pilot else range(4,9)):
        probes.append(rare(r));save('PILOT_RARE_PARTIAL.json' if pilot else 'RARE_PARTIAL.json',probes)
    result={'status':'PASS','pilot':pilot,'helper':'A074-oneflip-direct-character-v5','checks':a.CHECKS,'runtime_seconds':time.perf_counter()-start,'analytic_gate_certificate':analytic,'direct_children':children,'rare_probes':probes,'independence':'No A072 code or outputs loaded; own direct bitset characters versus binary Moebius occupied-pattern coefficient expansion; own previous interval helper reused'}
    save('PILOT.json' if pilot else 'VALIDATION.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ['analytic_gate_certificate','direct_children','rare_probes']}))
if __name__=='__main__':main()
