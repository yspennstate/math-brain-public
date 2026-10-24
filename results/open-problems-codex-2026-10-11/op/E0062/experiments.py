import math,json,pathlib,random,time
R=pathlib.Path(__file__).resolve().parent
def cycle(a,b,c,d): return [[0,a,0,-d],[-a,0,b,0],[0,-b,0,c],[d,0,-c,0]]
cases=[('balanced4',cycle(.6,.6,.6,.6),[.1,.2,.3,.4]),
       ('unequal4',cycle(.8,.3,.7,.4),[.1,.2,.3,.4]),
       ('reverse_unequal4',cycle(.3,.8,.4,.7),[.1,.2,.3,.4]),
       ('balanced_weighted4',cycle(.8,.4,.3,.6),[.1,.2,.3,.4]),
       ('cyclic3',[[0,.6,-.6],[-.6,0,.6],[.6,-.6,0]],[.2,.3,.5]),
       ('acyclic_zeros4',[[0,.7,0,.2],[-.7,0,.4,0],[0,-.4,0,.8],[-.2,0,-.8,0]],[.1,.2,.3,.4])]
out=[]
for name,A,x0 in cases:
    t=time.monotonic(); logs=[math.log(v) for v in x0]; m=len(logs); total=[0.]*m; samples=[]
    for n in range(1,100001):
        h=max(logs); x=[math.exp(v-h) for v in logs]; s=sum(x); x=[v/s for v in x]
        for i in range(m): total[i]+=x[i]
        if n in [100,1000,10000,25000,50000,75000,100000]:
            samples.append({'n':n,'x':x,'mean':[v/n for v in total],'min_log':min(logs),'residual':max(abs(x[i]*sum(A[i][j]*x[j] for j in range(m))) for i in range(m))})
        logs=[logs[i]+math.log1p(sum(A[i][j]*x[j] for j in range(m))) for i in range(m)]
        h=max(logs); z=h+math.log(sum(math.exp(v-h) for v in logs)); logs=[v-z for v in logs]
        if time.monotonic()-t>100: break
    out.append({'case':name,'A':A,'x0':x0,'samples':samples,'steps':n,'seconds':time.monotonic()-t})
    (R/'experiments.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(name,'steps',n,'seconds',time.monotonic()-t,'last',samples[-1],flush=True)
# Exact rational enumeration checks the formula, not the limiting theorem.
from fractions import Fraction as F
for pattern in range(3**6):
    digits=[]; v=pattern
    for _ in range(6): digits.append(v%3); v//=3
    A=[[F(0) for _ in range(4)] for _ in range(4)]
    for k,(i,j) in enumerate([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):
        A[i][j]=F(digits[k],2); A[j][i]=-A[i][j]
    x=[F(1,10),F(2,10),F(3,10),F(4,10)]
    y=[x[i]*(1+sum(A[i][j]*x[j] for j in range(4))) for i in range(4)]
    assert sum(y)==1 and min(y)>=0
    for r in range(1,4):
        delta=sum(y[:r])-sum(x[:r]); cross=sum(A[i][j]*x[i]*x[j] for i in range(r) for j in range(r,4))
        assert delta==cross and delta>=0
print('Exact rational prefix checks: 729 patterns * 3 cuts; all passed.',flush=True)
