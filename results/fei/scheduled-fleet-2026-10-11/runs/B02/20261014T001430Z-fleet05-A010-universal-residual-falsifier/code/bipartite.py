from pathlib import Path
from fractions import Fraction as Q
import json,time,sys
OUT=Path(__file__).resolve().parents[1]/'out'

def logs(x):
    k=x.numerator.bit_length()-x.denominator.bit_length(); y=x/Q(2)**k
    if y<1: y*=2; k-=1
    assert 1<=y<2
    def ln(y):
        z=(y-1)/(y+1); term=z; s=Q(0)
        for j in range(16): s+=term/(2*j+1); term*=z*z
        return 2*s,2*s+2*term/(33*(1-z*z))
    a,b=ln(y); c,d=ln(Q(2)); return k+a/d,k+b/c

def fwht(a):
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

def case(p,q):
    n=p+q; size=1<<n; table=[1 if (x&((1<<p)-1)) and x>>p else -1 for x in range(size)]
    a=fwht(table[:]); assert sum(c*c for c in a)==size*size
    u,v=Q(1,1<<p),Q(1,1<<q); aa,bb=1-u,1-v
    il,ir=2*p*u*bb,2*q*v*aa; I=il+ir; variance=4*aa*bb*(1-aa*bb)
    sectors={'left':Q(0),'right':Q(0),'mixed':Q(0)}; degrees={k:Q(0) for k in sectors}
    for A,c in enumerate(a):
        if not A: assert Q(c,size)==2*aa*bb-1; continue
        left=A&((1<<p)-1); right=A>>p
        expected=2*u*bb if left and not right else 2*v*aa if right and not left else 2*u*v
        assert Q(abs(c),size)==expected
        key='mixed' if left and right else 'left' if left else 'right'
        prob=Q(c*c,size*size); sectors[key]+=prob; degrees[key]+=A.bit_count()*prob
    assert sectors=={'left':4*bb*bb*u*(1-u),'right':4*aa*aa*v*(1-v),'mixed':4*u*v*aa*bb}
    assert degrees=={'left':bb*il,'right':aa*ir,'mixed':v*il+u*ir}
    assert sum(degrees.values())==I and sum(sectors.values())==variance
    edge=[sum(table[x]!=table[x^(1<<j)] for x in range(size) if not(x>>j&1)) for j in range(n)]
    assert all(Q(e,1<<(n-1))==il/p for e in edge[:p])
    assert all(Q(e,1<<(n-1))==ir/q for e in edge[p:])
    d=max(p,q); T=(1+Q(1,4*d))**(p*q)-1
    upper=variance*logs(T)[1]+degrees['left']*logs(Q(4*d,q))[1]+degrees['right']*(logs(Q(4*d,p))[1]+Q(6,5))+degrees['mixed']*(logs(Q(4*d))[1]+Q(12,5))
    assert upper<Q(13,2)*I,(p,q,float(upper/I))
    scale=1<<50; dyadic=Q((upper/I*scale).__ceil__(),scale)
    return {'p':p,'q':q,'n':n,'physical_inputs':size,'I':str(I),'variance':str(variance),'degrees':{k:str(v) for k,v in degrees.items()},'T':str(T),'certified_R_over_I_upper':str(dyadic),'display':float(dyadic)}

if __name__=='__main__':
    pilot='pilot' in sys.argv; start=time.monotonic(); rows=[]; ps=range(2,4 if pilot else 9)
    for p in ps:
        for q in ps:
            assert time.monotonic()-start<(60 if pilot else 300)
            rows.append(case(p,q)); (OUT/'bipartite_checkpoint.json').write_text(json.dumps(rows,indent=2))
    for k in range(65):
        assert k*(k+2)<=2**(k+1) if k>=1 else True
    for q in range(2,65): assert (q-1)*4<=2**q and q*(q-1)*4<=3*2**q
    assert Q(91,20)+Q(4,3)/Q(56,81)<Q(13,2)
    result={'cases':len(rows),'physical_inputs':sum(r['physical_inputs'] for r in rows),'rows':rows,'elapsed_seconds':time.monotonic()-start,'analytic_bound':'R <= (91/20+4/(3 ln2)) I < (13/2) I','posterior_scope':'All-prime positive table, globally fixed weights; supplies upper bound on infimum, not exact optimum'}
    (OUT/('bipartite_pilot.json' if pilot else 'bipartite.json')).write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
