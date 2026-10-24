from pathlib import Path
from fractions import Fraction as Q
import json,sys,time,hashlib,math
import a060_math as m

ROOT=Path(__file__).resolve().parents[1]
check=m.check
K=m.add({2:Q(12)},{3:-Q(9,2)})
def eta(x): return m.entropy([x])
def P(z): return m.add(eta((1-z)**2),eta(z*z),m.scale(eta((1-2*z)**2),-Q(1,2)))
def G(z): return m.add({2:4-4*z},m.scale(P(z),1/z))
def integer_sign(vec):
    den=1
    for c in vec.values(): den=math.lcm(den,c.denominator)
    pos=neg=1
    for prime,c in vec.items():
        n=int(c*den)
        if n>=0: pos*=prime**n
        else: neg*=prime**(-n)
    return (pos>neg)-(pos<neg),{'denominator_clearer':den,'positive_bits':pos.bit_length(),'negative_bits':neg.bit_length(),'positive_sha256':hashlib.sha256(pos.to_bytes((pos.bit_length()+7)//8,'big')).hexdigest(),'negative_sha256':hashlib.sha256(neg.to_bytes((neg.bit_length()+7)//8,'big')).hexdigest(),'exponents':{str(p):int(c*den) for p,c in vec.items()}}

def restrict(vals,i,bit):
    n=len(vals).bit_length()-1
    return [vals[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(1<<(n-1))]
def point_case(r,mask,transform=m.fwht):
    core=[-1 if (mask>>x)&1 else 1 for x in range(4)]; q=Q(1,1<<r)
    mean=Q(sum(core),4); a=1-mean; V=1-mean*mean; z=q*a
    vals=[core[x>>r] if x% (1<<r)==0 else 1 for x in range(1<<(r+2))]
    spec=transform(vals); check(sum(c*c for c in spec)==1)
    inf=m.influences(vals); hc=m.H(core,transform)
    check(inf==[z]*r+[q*d for d in m.influences(core)])
    for i in range(r):
        c0,c1=restrict(vals,i,0),restrict(vals,i,1)
        decrement=m.add(m.H(vals,transform),m.scale(m.add(m.H(c0,transform),m.H(c1,transform)),-Q(1,2)))
        exact=m.add({2:2*q*V+2*(q-2*q*q)*a*a},P(z))
        check(decrement==exact)
        residual=m.add(decrement,{2:-q*V})
        check(residual==m.add({2:2*z+z*a-4*z*z},P(z)))
        check(integer_sign(m.add(m.scale(K,z),m.scale(residual,-1)))[0]>=0)
        check(integer_sign(residual)[0]>=0)
        check(sum(inf)==inf[i]+(sum(m.influences(c0))+sum(m.influences(c1)))/2)
        if r==3 and mask==15: check(residual==m.scale(K,z))
    return 1

def fine_case(transform=m.fwht):
    core=[-1 if x<7 else 1 for x in range(32)]
    vals=[core[x>>1] if x%2==0 else 1 for x in range(64)]
    z=Q(7,32); V=Q(175,256); q=Q(1,2)
    terminal=m.scale(m.H(core,transform),Q(1,2))
    D=m.add(m.H(vals,transform),m.scale(terminal,-1))
    check(m.influences(vals)[0]==z)
    check(D==m.scale(G(z),z))
    sign,cert=integer_sign(m.add(G(z),m.scale(K,-1))); check(sign>0)
    coarse=m.add(D,{2:-q*V})
    check(m.add(m.scale(D,1/z),m.scale(coarse,-1/z))=={2:Q(25,16)})
    check(integer_sign(m.add(m.scale(K,z),m.scale(coarse,-1)))[0]>0)
    check(sum(m.influences(vals))==z+sum(m.influences(core))/2)
    return {'dimension':6,'outer_influence':str(z),'coarse_release':str(q*V),'fine_release':0,'fine_ratio_minus_K_integer_certificate':cert,'root_entropy_prime_logs':{str(p):str(c) for p,c in m.H(vals,transform).items()},'terminal_entropy_prime_logs':{str(p):str(c) for p,c in terminal.items()}}

LN2=m.lnat(Q(2),80)
def plus(*ivs): return sum((x[0] for x in ivs),Q(0)),sum((x[1] for x in ivs),Q(0))
def mult(iv,c): return (iv[0]*c,iv[1]*c) if c>=0 else (iv[1]*c,iv[0]*c)
def ln(x): return m.lnat(x,80)
def pnat(z):
    return plus(mult(ln(1-z),-2*(1-z)**2),mult(ln(z),-2*z*z),mult(ln(1-2*z),(1-2*z)**2))
def pprime(z):
    return plus(mult(ln(1-z),4*(1-z)),mult(ln(z),-4*z),mult(ln(1-2*z),-4*(1-2*z)))
def divln2(iv):
    a,b=iv; combos=[a/LN2[0],a/LN2[1],b/LN2[0],b/LN2[1]]
    return min(combos),max(combos)
def gprime(z):
    x=divln2(mult(plus(mult(pprime(z),z),mult(pnat(z),-1)),1/(z*z)))
    return x[0]-4,x[1]-4
def giv(z):
    x=divln2(mult(pnat(z),1/z)); return x[0]+4-4*z,x[1]+4-4*z
def continuum():
    lo,hi=Q(1,8),Q(1,4)
    check(gprime(lo)[0]>0); check(gprime(hi)[1]<0)
    rows=[]
    for i in range(40):
        mid=(lo+hi)/2; iv=gprime(mid)
        if iv[0]>0: lo=mid; sign=1
        elif iv[1]<0: hi=mid; sign=-1
        else: raise AssertionError('Derivative sign unresolved; no silent precision escalation')
        check(lo<hi); rows.append({'step':i,'mid':str(mid),'derivative_sign':sign,'derivative_interval':m.dyadic(iv)})
    low=giv(lo); derivative=gprime(lo)
    gamma=(low[0],low[1]+derivative[1]*(hi-lo))
    check(derivative[0]>0); check(gprime(hi)[1]<0)
    check(gamma[0]>Q(487,100)); check(gamma[1]<Q(49,10))
    result={'maximizer_bracket':[str(lo),str(hi)],'maximum_interval':m.dyadic(gamma),'bisections':rows,'arithmetic':'80-term rational atanh intervals and analytic strict concavity/tangent upper bound'}
    (ROOT/'out/CONTINUUM_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return {k:v for k,v in result.items() if k!='bisections'}

def scalar_certificates():
    check(7**126>3**60*2**256)
    check(7**49>2**80*3**36)
    check(3**5<2**8); check(3**3<2**5)
    return {'Gprime_one_eighth':'7^126>3^60*2^256','G_one_eighth_less_G_one_quarter':'7^49>2^80*3^36','Gprime_one_quarter_negative':'3^30<2^48 follows from 3^5<2^8','K_greater_9_over_2':'3^3<2^5'}

mode=sys.argv[1] if len(sys.argv)>1 else 'main'; start=time.perf_counter()
rs=[1,2,3] if mode in ['pilot','reproduce'] else [1,2,3,4,5]
transform=m.direct if mode=='reproduce' else m.fwht
count=sum(point_case(r,mask,transform) for r in rs for mask in range(16))
fine=fine_case(transform); scalars=scalar_certificates()
cv=continuum() if mode=='main' else None
check(time.perf_counter()-start<55)
result={'status':'PASS','mode':mode,'cases':count,'assertions':m.CHECKS,'seconds':time.perf_counter()-start,'fine_witness':fine,'scalar_certificates':scalars,'continuum':cv}
(ROOT/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['fine_witness','scalar_certificates','continuum']}))
