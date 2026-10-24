from pathlib import Path
from fractions import Fraction as F
import json,math,time
R=Path(__file__).resolve().parents[1];O=R/'out';ts=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1;assert x,checks;assert time.perf_counter()-ts<45
def direct(v):return [sum(z*(-1 if (i&j).bit_count()%2 else 1) for i,z in enumerate(v)) for j in range(len(v))]
def p(v):return [F(z*z,len(v)**2) for z in direct(v)]
def log(q):
    d={}
    for n,s in [(q.numerator,1),(q.denominator,-1)]:
        k=2
        while n>1:
            if k*k>n:k=n
            e=0
            while n%k==0:n//=k;e+=1
            if e:d[k]=d.get(k,F(0))+s*e
            k+=1
    return {k:v for k,v in d.items() if v}
def add(*x):
    d={}
    for c,v in x:
        for k,z in v.items():d[k]=d.get(k,F(0))+c*z
    return {k:z for k,z in d.items() if z}
def ce(v,q):
    ck(all(a==0 or b>0 for a,b in zip(v,q)))
    return add(*[(-a,log(b)) for a,b in zip(v,q) if a])
def ent(v):return ce(v,v)
def sign(d):
    D=math.lcm(*(v.denominator for v in d.values())) if d else 1
    up=down=1
    for k,v in d.items():
        e=int(D*v)
        if e>0:up*=k**e
        else:down*=k**(-e)
    return (up>down)-(up<down)
def vec(v):return [F(x) for x in v]
def enc(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
    if isinstance(v,list):return [enc(x) for x in v]
    return v
validation=json.loads((O/'validation.json').read_text(encoding='utf-8'));ck(validation['PASS'])
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-x*x for x in a]
A=[F(x,16) for x in direct(a)];B=[F(x,16) for x in direct(b)]
fixtures=json.loads((O/'fixed_resets.json').read_text(encoding='utf-8'));ck(len(fixtures)==2)
answers=[]
for f in fixtures:
    h=f['seed'];ph=p(h);m=F(sum(h),len(h));r=m*m;ref=vec(f['reference']);target=vec(f['target_tail'])
    parent=[x+y for x,y in zip(f['actual_children'][0],f['actual_children'][1])] # not used as a fictitious Boolean table
    par=[x*x*(1 if j==0 else 0) for j in range(len(h)) for x in A]+[y*y*z for z in ph for y in B]
    qr=[x*x*(1 if j==0 else 0) for j in range(len(h)) for x in A]+[y*y*z for z in ref for y in B]
    children=[]
    for k,sig in enumerate([1,-1]):
        truth=[x+sig*y*z for z in h for x,y in zip(a,b)]
        ck(truth==f['actual_children'][k]);ck(all(x in [-1,1] for x in truth))
        pp=p(truth);ck(pp==vec(f['child_spectra'][k]));children.append(pp)
        mixed=[F(7,8)*x/(1-ref[0])+F(1,8)*y for x,y in zip(ref[1:],target)]
        qq=[(x+sig*m*y)**2 for x,y in zip(A,B)]+[y*y*(1-r)*z for z in mixed for y in B]
        ck(qq==vec(f['fresh_references'][k]));ck(sum(qq)==1)
    qbar=[(x+y)/2 for x,y in zip(*children)]
    erasure=add((1,ent(par)),(-1,ent(qbar)))
    inc=add((1,erasure),(F(1,2),ce(children[0],vec(f['fresh_references'][0]))),(F(1,2),ce(children[1],vec(f['fresh_references'][1]))),(-1,ce(par,qr)))
    ck(inc=={int(k):F(v) for k,v in f['increment'].items()})
    ck(sign(add((1,inc),(1,{2:F(1,64)})))<0)
    answers.append({'reference':ref,'increment':inc,'strict_below_minus_1_over_64':True})
w=json.loads((O/'support_obstruction.json').read_text(encoding='utf-8'))
truth=w['child_truth_table'];W=direct(truth);ck(W==w['child_Walsh']);ck(all(z in [-1,1] for z in truth))
ck(F(W[0]**2,len(truth)**2)==F(1,256));q=vec(w['naive_normalized_reference']);ck(sum(q)==1);ck(q[0]==0)
ck(21**18>2**79);ck(21**3>2**13)
out={'PASS':True,'checks':checks,'seconds':time.perf_counter()-ts,'fixtures':len(fixtures),'support_obstruction':True,'method':'direct character sums and integer-power signs','results':answers}
(O/'independent.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
