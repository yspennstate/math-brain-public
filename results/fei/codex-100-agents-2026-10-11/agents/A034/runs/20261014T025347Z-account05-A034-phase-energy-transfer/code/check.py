from pathlib import Path
from fractions import Fraction as F
from math import gcd, prod
import json, time
root=Path(__file__).resolve().parents[1]
(root/'out').mkdir(exist_ok=True)
start=time.perf_counter(); assertions=0
def ck(x):
    global assertions
    assert x
    assertions+=1
def fw(v):
    a=list(v); k=1
    while k<len(a):
        for j in range(0,len(a),2*k):
            for i in range(j,j+k):
                u,v=a[i],a[i+k];a[i],a[i+k]=u+v,u-v
        k*=2
    return a
def product_law(w,m):
    z=sum(x*x for x in w)
    marg=[sum(x*x for s,x in enumerate(w) if s>>i&1) for i in range(m)]
    if not m:return True
    return all(w[s]**2*z**(m-1)==prod(marg[i] if s>>i&1 else z-marg[i] for i in range(m)) for s in range(len(w)))
counts=[]
for m in range(5):
    P=1<<m; tested=admitted=0; examples=[]
    masks=(M for M in range(1<<P) if M.bit_count()%2) if m<4 else [1]
    for M in masks:
        signs=range(1<<P) if m<4 else range(1<<(P-1))
        for z in signs:
            if m==4:z<<=1
            h=[(-1 if z>>y&1 else 1)*(1 if M>>y&1 else 2) for y in range(P)]
            w=fw(h);tested+=1
            if not product_law(w,m):continue
            admitted+=1
            # Complete every admitted row to an actual Boolean sign.
            for y in range(P):
                rows=[h[y],1,1,-h[y]] if M>>y&1 else [h[y],0,0,0]
                ck(all(abs(v)==2 for v in fw(rows)))
            if not m:continue
            ck(all(x%2 for x in w))
            a=[];b=[]
            for i in range(m):
                ratio=F(abs(w[1<<i]),abs(w[0]));a.append(ratio.denominator);b.append(ratio.numerator)
            ck(abs(w[0])==prod(a))
            ck(all(abs(w[s])==prod(b[i] if s>>i&1 else a[i] for i in range(m)) for s in range(P)))
            D=prod(x*y for x,y in zip(a,b));mu=M.bit_count()
            t=sum((-1)**y.bit_count() for y in range(P) if M>>y&1)
            N=sum(x!=y for x,y in zip(a,b))
            ck(prod((x*x+y*y)//2 for x,y in zip(a,b))==4*P-3*mu)
            ck(sum(w[s]*w[s^(P-1)] for s in range(P))==-3*P*t)
            ck((3*t)%D==0);ck(3**N<=D<=3*abs(t))
            ck(8*P<=9*t*t+6*mu+1<=(3*mu+1)**2)
            ck(abs(t)<=min(mu,P-mu))
            if len(examples)<4:examples.append({'M':M,'h':h,'N':N,'D':D,'t':t})
        if time.perf_counter()-start>55:raise RuntimeError('Frozen runtime exceeded')
    counts.append({'m':m,'tested':tested,'admitted_product_rows':admitted,'examples':examples})
ck(sum(x['tested'] for x in counts)==65674)
phantom=[3**(s&7).bit_count() for s in range(32)]
ck(sum(x*x for x in phantom)==4000);ck(product_law(phantom,5));ck(96%27!=0)
point=[]
for r in range(1,11):
    P=1<<(r+1);truth=[1]*P;truth[0]=-1;w=fw(truth)
    ck(w[0]==P-2 and all(v==-2 for v in w[1:]))
    mass=[F(w[2*j]**2+w[2*j+1]**2,P*P) for j in range(1<<r)]
    p=F(1,1<<r);ck(mass[0]==(1-p)**2+p*p)
    ck(sum(mass[j]*j.bit_count() for j in range(len(mass)))==r*p)
    ck(sum(F(w[2*j+1]**2,P*P) for j in range(len(mass)))==p)
    Q=sum(mass[j] for j in range(len(mass)) if 2*w[2*j+1]**2!=w[2*j]**2+w[2*j+1]**2)
    ck(Q==(0 if r==1 else mass[0]))
for r in range(2,41):
    p=F(1,1<<r);w0=(1-p)**2+p*p
    bound=w0/((5*r+4)*p)
    point.append({'r':r,'Q':str(w0),'rigorous_ratio_lower_bound':str(bound)})
    ck(w0>F(1,2))
for m in range(1,9):
    ck((F(9,25)+F(16,25))**m==1)
    ck(F(16,25) not in [0,F(1,2),1]);ck(F(7,5)**m>1)
result={'helper_version':'A034-odd-mask-v1','counts':counts,'assertions':assertions,'phantom':{'P':32,'mu':1,'norm':4000,'D':27,'required_signed_sum_absolute':96,'remainder':96%27},'point_defect_ratio_certificates':point,'runtime_seconds':time.perf_counter()-start,'status':'PASS'}
(root/'out'/'validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','counts':counts,'assertions':assertions,'runtime_seconds':result['runtime_seconds']},indent=2))
