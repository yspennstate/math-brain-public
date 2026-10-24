import sys,json,time,math,importlib.util
from pathlib import Path
from fractions import Fraction as F
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261014T020611Z-account05-A072-exact-walsh-engine/code/verify.py'
spec=importlib.util.spec_from_file_location('own_stage4',old);a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
B=a.B;checks=0
H=tuple(-1 if x in (0,1,2,4,8,16,32,6,17,40) else 1 for x in range(64))
J=tuple(-H[x^1] for x in range(64))
def ck(v):
    global checks
    if not v:raise AssertionError('check '+str(checks+1))
    checks+=1
def dump(name,o):
    (R/'out'/name).write_text(json.dumps(o,indent=2,default=str)+'\n',encoding='utf-8')
def trim(z):
    z=list(map(F,z))
    while len(z)>1 and not z[-1]:z.pop()
    return z
def add(*polys):
    z=[F(0)]*max(map(len,polys))
    for p in polys:
        for i,x in enumerate(p):z[i]+=x
    return trim(z)
def scale(p,c):return trim([c*x for x in p])
def mul(p,q):
    z=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):z[i+j]+=x*y
    return trim(z)
def ev(poly,x):
    z=F(0)
    for c in reversed(poly):z=z*x+c
    return z
def countpoly(counts,n):
    z=[F(0)]*(n+1)
    for k,c in enumerate(counts):
        for l in range(n-k+1):z[k+l]+=c*math.comb(n-k,l)*(-1)**l
    return trim(z)
def bernstein(poly,lo,hi):
    d=len(poly)-1
    powers=[sum((poly[i]*math.comb(i,j)*lo**(i-j)*(hi-lo)**j for i in range(j,d+1)),F(0)) for j in range(d+1)]
    return [sum((powers[j]*F(math.comb(k,j),math.comb(d,j)) for j in range(k+1)),F(0)) for k in range(d+1)]
def symbolic():
    records={}
    for name,t in [('h',H),('J',J)]:
        uniform=B.uniform_certificate(t)
        counts=[sum(t[x]<0 and x.bit_count()==k for x in range(64)) for k in range(7)]
        probability=countpoly(counts,6);pivs=[]
        for j in range(6):
            edges=[sum(not x>>j&1 and x.bit_count()==k and t[x]!=t[x|(1<<j)] for x in range(64)) for k in range(6)]
            pivs.append(countpoly(edges,5))
        records[name]={'probability_polynomial':probability,'pivotal_polynomials':pivs,'negative_weight_counts':counts,'uniform_certificate':uniform}
    q=[0,4,-14,18,-10,2]
    ck(all(z==q for z in records['h']['pivotal_polynomials']))
    alpha=mul([1,-4,6,-4,1],[1,4,-2]);ck(records['h']['probability_polynomial']==alpha)
    ck(records['J']['probability_polynomial']==[0,4,-10,18,-19,10,-2])
    v=[0,4,-4];Q=scale(q,6);w=scale(mul(alpha,add([1],scale(alpha,-1))),4)
    P=[4,-28,109,-152,100,-32,4]
    prefactor=mul([0,0,12],[1,-4,6,-4,1])
    ck(add(scale(mul(Q,v),2),scale(w,-3))==mul(prefactor,P))
    boxes=[]
    for lo,hi in [(F(0),F(1,2)),(F(1,2),F(1))]:
        coeff=bernstein(P,lo,hi);ck(all(c>0 for c in coeff))
        # Independent polynomial equality at all degree+1 integer abscissae.
        for t in range(7):
            ck(ev(P,lo+(hi-lo)*t)==sum((coeff[k]*math.comb(6,k)*t**k*(1-t)**(6-k) for k in range(7)),F(0)))
        boxes.append({'lo':lo,'hi':hi,'bernstein_coefficients':coeff})
    # Endpoint envelopes used by the all-dimensional proof, exact rational checks.
    ck(2*F(15,16)**3*F(31,16)>3)
    ck(ev(Q,F(1,16))==F(313875,262144)>F(19,16))
    ck(ev(Q,F(25,32))==F(1003275,8388608)>F(1,9))
    ck(2-10*F(7,32)+5*F(7,32)**2>0)
    ck(63*F(3,48)<4 and 54*3<256)
    ck(F(1731,44)==3*(8+F(225,44))<40)
    dump('polynomials.json',records);dump('continuum_certificate.json',{'P':P,'positive_boxes':boxes,'covered_interval':[0,1],'minimum_Bernstein_coefficient':min(x for b in boxes for x in b['bernstein_coefficients'])})
    return records
def centered(t,p):
    # Direct biased interpolation. No uniform-Walsh-to-biased conversion.
    c=list(map(F,t))
    for j in range(6):
        for s in range(64):
            if not s>>j&1:
                u,z=c[s],c[s|(1<<j)]
                c[s]=(1-p)*u+p*z;c[s|(1<<j)]=z-u
    s=[c[T]**2*(p*(1-p))**T.bit_count() for T in range(64)]
    ck(sum(s)==1)
    for x in range(64):
        ck(sum((c[T]*math.prod(F((x>>j)&1)-p for j in range(6) if T>>j&1) for T in range(64)),F(0))==t[x])
    q=[];v=4*p*(1-p)
    for j in range(6):
        edges=sum((p**x.bit_count()*(1-p)**(5-x.bit_count()) for x in range(64) if not x>>j&1 and t[x]!=t[x|(1<<j)]),F(0))
        ck(v*edges==sum((s[T] for T in range(64) if T>>j&1),F(0)));q.append(edges)
    return c,s,q
def profile(name,p,records):
    t=H if name=='h' else J;c,s,qs=centered(t,p);Q=sum(qs);v=4*p*(1-p);w=1-s[0]
    ck(w<=Q*v)
    ck(all(q==ev(poly,p) for q,poly in zip(qs,records[name]['pivotal_polynomials'])))
    ck((1-c[0])/2==ev(records[name]['probability_polynomial'],p))
    if name=='h':ck(3*w<=2*Q*v)
    C=a.e.subtract(a.ent(s),tuple(Q*z for z in a.ent((1-v,v))))
    if name=='h':
        ck(C[1]<8*Q*v)
        if p<=F(1,16):ck(C[1]<342*p*p)
    else:
        ck(min(qs)>0 and sum(qs)>=F(11,4))
        ck(all(min(q,1-q)<=5*p for q in qs))
        ck(3*p<(1-c[0])/2<4*p)
        cap=F(120,11)*p*(F(3,2)-a.log(5*p)[0])
        ck(C[1]/(Q*v)<cap)
    dump('profile_'+name+'_'+str(p.numerator)+'_'+str(p.denominator)+'.json',{'gate':name,'p':p,'masses':s,'q_j':qs,'Q':Q,'v':v,'w':w,'mu_multiplier':w/(Q*v),'C_interval':C,'C_over_Qv_interval':[z/(Q*v) for z in C]})
def physical(name,mask):
    t=H if name=='h' else J;g=tuple(1-2*((mask>>x)&1) for x in range(4));core=B.uniform_certificate(g)
    p=F(sum(z<0 for z in g),4);c,s,qs=centered(t,p)
    table=tuple(t[sum((g[(x>>(2*j))&3]<0)<<j for j in range(6))] for x in range(4096))
    W,inf,edges=a.fast(table)
    for S in range(4096):
        occupied=0;product=F(1)
        for j in range(6):
            u=(S>>(2*j))&3
            if u:occupied|=1<<j;product*=F(-core['walsh'][u],8)
        ck(F(W[S],4096)==c[occupied]*product)
    for j in range(6):
        for i in range(2):ck(inf[2*j+i]==qs[j]*core['influences'][i])
    # Entire entropy identity, as independent interval diagnostic after exact coefficients/edges.
    Q=sum(qs);v=4*p*(1-p)
    parentH=a.ent([F(w*w,4096**2) for w in W]);coreH=a.ent(core['spectrum'])
    C=a.e.subtract(a.ent(s),tuple(Q*z for z in a.ent((1-v,v))))
    diagnostic=a.e.subtract(parentH,(Q*coreH[0]+C[0],Q*coreH[1]+C[1]))
    ck(diagnostic[0]<=0<=diagnostic[1])
    dump('parent_'+name+'_'+str(mask)+'.json',{'core_mask':mask,'gate':name,'p':p,'legal_J_price_domain':name!='J' or p<=F(1,16),'integer_walsh':W,'undirected_edges':edges,'influences':inf,'coefficient_matches':4096,'entropy_identity_interval_diagnostic':diagnostic})
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv;cap=55 if pilot else 120
    records=symbolic()
    for name,grid in [('h',[F(1,16)] if pilot else [F(1,256),F(1,64),F(1,16),F(7,32),F(1,2),F(25,32)]),('J',[F(1,16)] if pilot else [F(1,256),F(1,64),F(1,16)])]:
        for p in grid:profile(name,p,records);ck(time.perf_counter()-start<cap)
    for name in ['h','J']:
        for mask in ([1] if pilot else [1,3,6,7]):physical(name,mask);ck(time.perf_counter()-start<cap)
    result={'passed':True,'assertions':checks,'profiles':2 if pilot else 9,'polynomial_boxes':2,'actual_parents':2 if pilot else 8,'exact_coefficient_matches':8192 if pilot else 32768,'coordinate_edge_counts':24 if pilot else 96,'runtime_seconds':time.perf_counter()-start}
    dump('pilot.json' if pilot else 'validation.json',result);print(json.dumps(result))
if __name__=='__main__':main()
