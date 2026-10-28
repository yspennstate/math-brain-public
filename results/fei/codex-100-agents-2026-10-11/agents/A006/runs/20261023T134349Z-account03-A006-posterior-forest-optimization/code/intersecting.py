from fractions import Fraction as F
from itertools import product
from pathlib import Path
import time,json
ROOT=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0; events=0; inputs=0
def ck(test):
    global checks
    checks+=1
    assert test,checks
    assert time.perf_counter()-start<55
rows=[]
for w,r in product([1,2],[1,2]):
    x,z,y=1,2,4; pos=3; blocks=[]
    for j in range(2*r): blocks.append(((1<<w)-1)<<pos); pos+=w
    vals=[1 if ((v&x) or ((bool(v&z) or all(v&B for B in blocks[:r])) and (bool(v&y) or all(v&B for B in blocks[r:])))) else -1 for v in range(1<<pos)]
    inputs+=len(vals)
    # Direct character sum is independent of the main check's FWHT.
    coeff=F(sum(s*(-1 if (v&(z|y)).bit_count()%2 else 1) for v,s in enumerate(vals)),len(vals))
    I=F(sum(vals[v]!=vals[v^(1<<i)] for v in range(len(vals)) for i in range(pos)),len(vals))
    eps=F(1,1<<w); a=(1-eps)**r
    Is=1-a+a*r*w*eps/(1-eps); Ih=(1+a)*Is
    ck(coeff**2==(1-a)**4/16)
    ck(I==1-(1+a)**2/4+Ih/2)
    beta=eps/4; c=beta*beta/(1-beta); ee=1-beta; d=ee+c
    # Enumerate every REAL event that outputs exactly {z,y}; all other local masks are impossible.
    # A marker q(j,tuple) is obtained from the actual conditional first-anchor draw, not a multiplicity alias.
    q=F(0); posterior=[]; rho=2*r*beta
    for bits in product([0,1],repeat=2*r):
        if not any(bits[:r]) or not any(bits[r:]): continue
        for j in range(2*r):
            if not bits[j]:continue
            mass=beta/rho/F((1<<(w+2))-1)
            for i,b in enumerate(bits):
                if i!=j: mass*=c if b else ee
            q+=mass; posterior.append(mass);events+=1
    ck(q==c/beta*d**(r-1)*(d**r-ee**r))
    ck(sum(m/q for m in posterior)==1)
    ck(all((z|y)&~C for C in [x|z,x|y,x]))
    rows.append({'w':w,'r':r,'n':pos,'I':str(I),'target_mass':str(coeff**2),'Q_target':str(q),'actual_target_anchor_events':len(posterior),'posterior':'All actual anchor+mask tuples retained; not just anchor multiplicity'})
for r in range(4,129):
    a=F(3,4)**r; Is=1-a+F(r,2)*F(3,4)**(r-1); Ih=(1+a)*Is
    IF=1-(1+a)**2/4+Ih/2
    ck(a<F(1,2)); ck(IF<3); ck(IF>F(7,16)); ck((1-a)**4/16>F(1,256))
    ck(Ih/2<=IF)
    d=F(113,120); ee=F(15,16)
    ck(F(1,15)*d**(r-1)*(d**r-ee**r)<=d**(2*r-1)/15)
out={'status':'PASS','helper_version':'A006-intersecting-core-v1','assertions':checks,'truth_inputs':inputs,'actual_target_anchor_events':events,'physical_rows':rows,'scalar_r_domain':[4,128],'seconds':time.perf_counter()-start}
(ROOT/'out/INTERSECTING.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','assertions','truth_inputs','actual_target_anchor_events','seconds']}))
