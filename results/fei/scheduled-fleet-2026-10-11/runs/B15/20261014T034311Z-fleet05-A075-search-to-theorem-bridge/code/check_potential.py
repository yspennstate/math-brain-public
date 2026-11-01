from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time
from arithmetic import *
import arithmetic as ar
ROOT=Path(__file__).resolve().parents[1];started=time.perf_counter()
def dump(name,x):(ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def pa(a,b):
    r=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]+=x
    for i,x in enumerate(b):r[i]+=x
    while len(r)>1 and not r[-1]:r.pop()
    return r
def scale_poly(a,c):return [x*c for x in a]
def prob_poly(counts,n):
    r=[Q(0)]*(n+1)
    for k,count in enumerate(counts):
        for j in range(n-k+1):r[k+j]+=count*comb(n-k,j)*(-1)**j
    return r
def ev(a,p):
    r=Q(0)
    for x in reversed(a):r=r*p+x
    return r
def bernstein_range(poly,a,b):
    n=len(poly)-1;c=[]
    for j in range(n+1):c.append((b-a)**j*sum((poly[k]*comb(k,j)*a**(k-j) for k in range(j,n+1)),Q(0)))
    B=[sum((c[k]*Q(comb(j,k),comb(n,k)) for k in range(j+1)),Q(0)) for j in range(n+1)]
    return min(B),max(B)
def logq(x):
    ck(x>0);return add(logform(x.numerator),logform(x.denominator),Q(-1))
def hm(x):return scale(logq(x),-x) if x else {}
def h2expr(p):return add(hm(p),hm(1-p))
def h2bounds(p):return enclose(h2expr(p))
def h2range(a,b):
    ck(0<=a<=b<=1)
    z=[h2bounds(a),h2bounds(b)]
    return min(x[0] for x in z),(Q(1) if a<=Q(1,2)<=b else max(x[1] for x in z))
def ibprod(a,b):
    z=[x*y for x in a for y in b];return min(z),max(z)
def bounds(expr):
    l,u=enclose(expr);return {'lower':str(l),'upper':str(u),'display':[float(l),float(u)]}
def gate_data(truth):
    counts=[0]*7
    for x,y in enumerate(truth):
        if y<0:counts[x.bit_count()]+=1
    prob=prob_poly(counts,6);piv=[]
    for j in range(6):
        c=[0]*6
        for x in range(64):
            if not(x>>j&1) and truth[x]!=truth[x|(1<<j)]:c[x.bit_count()]+=1
        piv.append(prob_poly(c,5))
    total=[Q(0)]
    for q in piv:total=pa(total,q)
    return {'prob':prob,'piv':piv,'Q':total,'truth':truth,'walsh':fwht(truth),'counts':counts}
NEG={0,1,2,4,8,16,32,6,17,40}
h=[-1 if x in NEG else 1 for x in range(64)];J=[-h[x^1] for x in range(64)]
gates={'h':gate_data(h),'J':gate_data(J)}
tau=[Q(0),Q(0),Q(12),Q(-28),Q(27),Q(-12),Q(2)]
ck(gates['h']['prob']==pa([Q(1)],scale_poly(tau,Q(-1))))
ck(gates['J']['prob']==[Q(0),Q(4),Q(-10),Q(18),Q(-19),Q(10),Q(-2)])
ck(gates['J']['counts']==[0,4,10,18,15,6,1])
ck(all(q==gates['h']['piv'][0] for q in gates['h']['piv']))
ck(gates['h']['Q']==[Q(0),Q(24),Q(-84),Q(108),Q(-60),Q(12)])
assertions=[]
# Independent source review A089: exact threshold and reciprocal-I constants.
delta=Q(1,16);c=Q(7,32)
ck(ev(gates['h']['Q'],delta)==Q(313875,262144)>Q(19,16))
ck(2-10*c+5*c*c==Q(53,1024))
ck(Q(65536,35625)<2)
ck(ev(gates['h']['Q'],1-c)==Q(1003275,8388608)>Q(1,9))
ck(ev(tau,c)<Q(3,8))
ck(Q(3,8)**4*(3-2*Q(3,8)**2)==Q(7047,131072)<delta)
ck(Q(1,2)**4*(3-2*Q(1,2)**2)==Q(5,32)<c)
ck(Q(360)*Q(4,105)<14)
ck(Q(38,3)+4==Q(50,3));ck(Q(76,3)+32==Q(172,3))
ck(Q(172,3)+Q(76,5)==Q(1088,15));ck(Q(50,3)+Q(24,5)==Q(322,15))
dump('GATE_POLYNOMIALS.json',{name:{'probability_poly':[str(x) for x in data['prob']],'pivotal_polys':[[str(x) for x in q] for q in data['piv']],'total_pivotal_poly':[str(x) for x in data['Q']],'negative_weight_counts':data['counts']} for name,data in gates.items()})

cert=[];data=gates['h']
for left,right in [(delta,c),(Q(1,2),1-c)]:
    for j in range(128):
        a=left+(right-left)*Q(j,128);b=left+(right-left)*Q(j+1,128)
        qs=bernstein_range(data['Q'],a,b);ps=bernstein_range(data['prob'],a,b)
        hp=h2range(a,b);ho=h2range(*ps)
        D=(qs[0]*hp[0]-ho[1],qs[1]*hp[1]-ho[0]);ck(D[0]>0)
        vr=bernstein_range([Q(0),Q(4),Q(-4)],a,b)
        hb=h2range(vr[0],vr[1]);hq=h2range(qs[0]/6,qs[1]/6)
        upperC=6*vr[1]*hq[1];negativeC=qs[1]*hb[1]
        ck(max(upperC,negativeC)<=64*D[0])
        cert.append({'input_bias_box':[str(a),str(b)],'D_interval':[str(z) for z in D],'C_upper':str(upperC),'minus_C_upper':str(negativeC),'abs_C_over_D_upper':str(max(upperC,negativeC)/D[0])})
dump('COMPACT_PAYMENT_CERTIFICATE.json',{'precision_bits':192,'atanh_terms':80,'boxes':cert,'max_certified_price':str(max(Q(x['abs_C_over_D_upper']) for x in cert)),'domain':['1/16..7/32','1/2..25/32'],'coverage':'128 adjacent equal subdivisions of each closed band'})

profiles=[]
for name,data in gates.items():
    for p in [Q(1,32),delta,Q(1,8),c,Q(1,2),1-c]:
        m=1-2*p;v=4*p*(1-p);prob=ev(data['prob'],p);Qtotal=ev(data['Q'],p)
        masses=[];raw=[]
        for T in range(64):
            z=sum((Q(w,64)*m**(Z.bit_count()-T.bit_count()) for Z,w in enumerate(data['walsh']) if Z&T==T),Q(0))
            raw.append(z);masses.append(v**T.bit_count()*z*z)
            ck(abs(z)<=1)
        ck(sum(masses)==1);ck(sum(x*T.bit_count() for T,x in enumerate(masses))==v*Qtotal)
        H={}
        for x in masses:H=add(H,hm(x))
        C=add(H,h2expr(v),-Qtotal)
        D=add(scale(h2expr(p),Qtotal),h2expr(prob),Q(-1))
        dl,du=enclose(D);ck(dl>0)
        if name=='h' and p<=delta:
            cl,cu=enclose(C);ck(cu<342*p*p)
            ck(cl>=-Qtotal*v/LN2[0])
        eligible=(name=='h' and (p<=c or Q(1,2)<=p<=1-c)) or (name=='J' and p<=delta)
        if eligible:
            ck(enclose(add(scale(D,64),C,Q(-1)))[0]>=0)
            ck(enclose(add(scale(D,64),C))[0]>=0)
        profiles.append({'gate':name,'p':str(p),'Q':str(Qtotal),'output_p':str(prob),'D':bounds(D),'C':bounds(C),'legal_step':eligible})
dump('RATIONAL_PROFILES.json',profiles)

fixtures=[]
for core in [[-1,1,1,1],[1,-1,-1,1]]:
    N=4;p=Q(sum(x<0 for x in core),N);W=fwht(core);I=Q(sum(s.bit_count()*w*w for s,w in enumerate(W)),N*N)
    for name,data in gates.items():
        truth=[]
        for x in range(4096):
            outer=sum((core[x>>(2*j)&3]<0)<<j for j in range(6));truth.append(data['truth'][outer])
        A=fwht(truth);outI=Q(sum(s.bit_count()*w*w for s,w in enumerate(A)),4096**2)
        Qtotal=ev(data['Q'],p);ck(outI==Qtotal*I)
        raw=[];m=1-2*p;v=4*p*(1-p)
        for T in range(64):raw.append(sum((Q(w,64)*m**(Z.bit_count()-T.bit_count()) for Z,w in enumerate(data['walsh']) if Z&T==T),Q(0)))
        for S,value in enumerate(A):
            occupied=0;factor=Q(1)
            for j in range(6):
                subset=S>>(2*j)&3
                if subset:occupied|=1<<j;factor*=Q(W[subset],4)
            ck(Q(value,4096)==raw[occupied]*factor)
        Hp={}
        for T,z in enumerate(raw):Hp=add(Hp,hm(v**T.bit_count()*z*z))
        C=add(Hp,h2expr(v),-Qtotal)
        difference=add(add(entropy(A),entropy(W),-Qtotal),C,Q(-1))
        lo,hi=enclose(difference);ck(lo<=0<=hi and hi-lo<Q(1,1<<140))
        probability=Q(sum(x<0 for x in truth),4096);ck(probability==ev(data['prob'],p))
        D=add(scale(h2expr(p),Qtotal),h2expr(probability),Q(-1))
        # The actual potential equality has identical exact log forms.
        potentialdrop=add(scale(h2expr(p),1/I),h2expr(probability),-1/outI)
        ck(potentialdrop==scale(D,1/outI))
        fixtures.append({'gate':name,'core':core,'p':str(p),'I':str(I),'parent_I':str(outI),'full_entropy_identity_interval':bounds(difference),'potential_drop':bounds(potentialdrop),'physical_coefficient_checks':4096,'potential_identity_exact':True})
dump('PHYSICAL_FIXTURES.json',fixtures)
dump('VALIDATION.json',{'helper_version':'A075-output-entropy-potential-v1','checks':ar.checks,'compact_boxes':len(cert),'profiles':len(profiles),'physical_fixtures':len(fixtures),'runtime_seconds':time.perf_counter()-started,'max_certified_compact_price_display':float(max(Q(x['abs_C_over_D_upper']) for x in cert)),'memory_estimate_MB':100,'full_fei':'OPEN'})
print(json.dumps({'checks':ar.checks,'runtime_seconds':time.perf_counter()-started,'compact_boxes':len(cert),'compact_price':float(max(Q(x['abs_C_over_D_upper']) for x in cert))}))
