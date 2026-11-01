from pathlib import Path
from fractions import Fraction as F
import time,json
R=Path(__file__).resolve().parents[1]
start=time.perf_counter(); count=0
def ck(b):
    global count
    assert b
    count+=1
    if time.perf_counter()-start>55:raise RuntimeError('frozen cap')
def parity(x):return x.bit_count()%2
def direct(a):
    return [sum(v*(-1)**parity(s&x) for x,v in enumerate(a)) for s in range(len(a))]
def edgeI(a):
    return F(sum(a[x]!=a[x^(1<<j)] for x in range(len(a)) for j in range(len(a).bit_length()-1)),len(a))
def rank(vs):
    span={0}
    for v in vs:span|={x^v for x in list(span)}
    return span.bit_count() if False else (len(span).bit_length()-1)
fixtures=[]
for source in [[1,1,1,-1],[1,-1]]:
    # Evaluate physical exponent afresh; source is stored above the four gadget bits.
    root=[]
    for x in range(16*len(source)*4):
        a,b,c,z=[(x>>j)&1 for j in range(4)]
        controls=x//(16*len(source))
        root.append(source[(x>>4)%len(source)]*(-1)**(a*b+a*c+b*c+z*a) if controls==0 else 1)
    children=[];reset=[]
    for branch in range(4):
        a,b=branch%2,branch//2
        ch=[root[(y<<2)|branch] for y in range(len(root)//4)]
        sh=[]
        for y in range(len(ch)):
            c,z=y%2,(y>>1)%2
            oldc=c^z if branch==1 else c
            oldy=(y&~3)|oldc|(z<<1)
            sh.append(ch[oldy])
        ck(sorted(v*v for v in direct(ch))==sorted(v*v for v in direct(sh)))
        ck(edgeI(ch)-edgeI(sh)==(F(1,4) if branch==1 else 0))
        children.append(ch);reset.append(sh)
    ck(edgeI(root)-sum((edgeI(x) for x in children),F(0))/4==F(1,4))
    ck(sum((edgeI(a)-edgeI(b) for a,b in zip(children,reset)),F(0))/4==F(1,16))
    fixtures.append({'source':source,'root_I':str(edgeI(root))})
# Independent guard: even-parity spectral law gives only ONE zero-cost parity.
guards=[]
for d in [3,5]:
    table=[]
    for x in range(1<<d):
        last=(x>>(d-1))&1
        exponent=sum((((x>>(2*j))&1)^last)*(((x>>(2*j+1))&1)^last) for j in range((d-1)//2))
        table.append((-1)**exponent)
    w=direct(table);den=len(table)**2
    support=[s for s,c in enumerate(w) if c]
    ck(support==[s for s in range(1<<d) if parity(s)==0])
    ck(all(c*c==2**(d+1) for c in w if c))
    costs={v:min(F(sum(c*c for s,c in enumerate(w) if parity(v&s)),den),1-F(sum(c*c for s,c in enumerate(w) if parity(v&s)),den)) for v in range(1,1<<d)}
    ck([v for v,c in costs.items() if c==0]==[(1<<d)-1])
    ck(rank(v for v,c in costs.items() if c==0)==1)
    ck(all(c==F(1,2) for v,c in costs.items() if v!=(1<<d)-1))
    ck(F(d,2)-F(d-1,2)==F(1,2))
    guards.append({'d':d,'actual_release':'1/2','false_dependent_swap_sum':str(F(d,2))})
# Rational logarithm enclosures by atanh; normalize the argument into[1,2].
def lnunit(x,N=40):
    y=(x-1)/(x+1)
    s=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    tail=2*y**(2*N+1)/(F(2*N+1)*(1-y*y))
    return s,s+tail
ln2=lnunit(F(2))
ck(ln2[0]>F(2,3))
def log2interval(x):
    shift=0
    while x<1:x*=2;shift-=1
    while x>2:x/=2;shift+=1
    lo,hi=lnunit(x)
    return F(shift)+lo/ln2[1],F(shift)+hi/ln2[0]
def hhinterval(x):
    lo,hi=log2interval(x*x)
    return -x*x*hi,-x*x*lo
mu=F(127,128);small=F(1,128)
a=hhinterval(mu);b=hhinterval(small)
sourceH=(a[0]+255*b[0],a[1]+255*b[1])
K=F(15,4);q=F(1,16)
ck(sourceH[0]>K*q+F(1,256))
t=100000000;k=10000
ck(k*k==t)
# Bernoulli proves mu^t<=1/(1+t/128); no huge exponent is evaluated.
mean_bound=F(128,128+t)
Lerror=F(13+6*k)*mean_bound
eta=5*K/4-4
ck(Lerror<eta)
terminal_lower=F(t,256)-K*(1+2*k)-10*k-20
ck(terminal_lower>0)
result={'status':'PASS','assertions':count,'runtime_seconds':time.perf_counter()-start,'direct_fixtures':fixtures,'rank_guards':guards,'point8_scalar_certificate':{'t':t,'k':k,'K':str(K),'source_deficit_lower':'1/256','L_over_p_error_upper':str(Lerror),'payment_margin_over_p_lower':str(eta-Lerror),'all_four_reset_terminal_deficits_over_p_lower':str(terminal_lower),'truth_table_constructed':False,'large_power_evaluated':False}}
(R/'out/INDEPENDENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
