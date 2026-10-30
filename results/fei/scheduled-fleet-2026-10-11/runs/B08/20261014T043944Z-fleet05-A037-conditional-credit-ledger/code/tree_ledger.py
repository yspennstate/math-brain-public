from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import math,json,time
BASE=Path(__file__).resolve().parent.parent
START=time.monotonic(); ASSERTIONS=0
def check(x):
    global ASSERTIONS
    ASSERTIONS+=1
    assert x,ASSERTIONS
    assert time.monotonic()-START<60
def factor(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
class Log:
    def __init__(self,terms=None):self.v={p:F(c) for p,c in (terms or {}).items() if c}
    def __add__(self,o):
        t=defaultdict(F,self.v)
        for p,c in o.v.items():t[p]+=c
        return Log(t)
    def __sub__(self,o):return self+o.scale(-1)
    def scale(self,c):return Log({p:v*c for p,v in self.v.items()})
    def __eq__(self,o):return self.v==o.v
    def display(self):return sum(float(c)*math.log2(p) for p,c in self.v.items())
    def data(self):return {'prime_log_coefficients':{str(p):str(c) for p,c in sorted(self.v.items())},'display_only':self.display()}
def log(q):
    q=F(q);check(q>0); t=defaultdict(F)
    for p,c in factor(q.numerator).items():t[p]+=c
    for p,c in factor(q.denominator).items():t[p]-=c
    return Log(t)
def entropy(p):
    z=Log()
    for q in p:
        if q:z=z-log(q).scale(q)
    return z
def h(d):return entropy([d,1-d])
def total(xs):
    z=Log()
    for x in xs:z=z+x
    return z
def walsh(tab):
    a=list(tab); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for t in range(step):u,v=a[j+t],a[j+t+step];a[j+t],a[j+t+step]=u+v,u-v
        step*=2
    return [F(x,len(tab)) for x in a]
def stats(tab):
    a=walsh(tab);p=[x*x for x in a];n=(len(tab)-1).bit_length()
    d=[sum(q for s,q in enumerate(p) if s>>j&1) for j in range(n)]
    H=entropy(p);M=total(h(x) for x in d)
    check(sum(p)==1)
    return dict(a=a,p=p,d=d,H=H,M=M,TC=M-H,I=sum(d))
def child(tab,i,y):
    return [tab[(t&((1<<i)-1))|(y<<i)|((t>>i)<<(i+1))] for t in range(len(tab)//2)]
def family(r):
    tab=[]
    for t in range(1<<(r+3)):
        x=t&3; active=((t>>2)&((1<<r)-1))==0;y=t>>(r+2)&1
        b=-1 if x==3 else 1
        if y and x==0:b=-b
        tab.append(b if active else 1)
    return tab
METRICS=['D','MI','Gamma','JS','B','Dout','reset']
def tree(tab,coords,order):
    nodes=[];leaves=[];sums={m:Log() for m in METRICS};massI=F(0)
    def visit(t,c,remaining,path,w):
        nonlocal massI
        st=stats(t)
        if not remaining or all(v==t[0] for v in t):
            leaves.append({'path':path,'weight':str(w),'coords':c,'H':st['H'].data(),'TC':st['TC'].data(),'I':str(st['I'])})
            return st['H'].scale(w),st['TC'].scale(w),st['I']*w
        i=c.index(remaining[0]); cnew=[j for j in c if j!=c[i]]
        children=[child(t,i,y) for y in (0,1)];ss=[stats(z) for z in children]
        q=[(ss[0]['p'][T]+ss[1]['p'][T])/2 for T in range(len(t)//2)]
        B=st['H']-entropy(q);D=h(st['d'][i]);MI=D-B
        JS=entropy(q)-(ss[0]['H']+ss[1]['H']).scale(F(1,2))
        Gamma=total(h((u+v)/2)-(h(u)+h(v)).scale(F(1,2)) for u,v in zip(ss[0]['d'],ss[1]['d']))
        check(st['TC']==MI-JS+Gamma+(ss[0]['TC']+ss[1]['TC']).scale(F(1,2)))
        check(st['I']==st['d'][i]+F(1,2)*(ss[0]['I']+ss[1]['I']))
        # Transport parent residual product via the same function-specific channel.
        dres=[st['d'][j] for j in range(len(c)) if j!=i]
        Q=[math.prod(d if T>>j&1 else 1-d for j,d in enumerate(dres)) for T in range(len(q))]
        kernels=[[ss[y]['p'][T]/(2*q[T]) if q[T] else F(1,2) for T in range(len(q))] for y in (0,1)]
        qY=[sum(Q[T]*kernels[y][T] for T in range(len(q))) for y in (0,1)]
        Dout=total(log(F(1,2)/qy).scale(F(1,2)) for qy in qY)
        reset=Log()
        for y in (0,1):
            dc=ss[y]['d']
            for T,pc in enumerate(ss[y]['p']):
                if not pc:continue
                predicted=Q[T]*kernels[y][T]/qY[y]
                projected=math.prod(d if T>>j&1 else 1-d for j,d in enumerate(dc))
                check(predicted>0 and projected>0)
                reset=reset+log(predicted/projected).scale(pc/2)
        check(reset==Dout+JS-Gamma)
        values=dict(D=D,MI=MI,Gamma=Gamma,JS=JS,B=B,Dout=Dout,reset=reset)
        cls='control' if 2<=c[i]<=5 else ('selector' if c[i]==6 else 'data')
        nodes.append({'path':path,'weight':str(w),'queried_global_coordinate':c[i],'node_class':cls,'Inf':str(st['d'][i]),'H':st['H'].data(),'TC':st['TC'].data(),**{m:v.data() for m,v in values.items()}})
        for m,v in values.items():sums[m]=sums[m]+v.scale(w)
        massI+=w*st['d'][i]
        vals=[visit(children[y],cnew,remaining[1:],path+str(y),w/2) for y in (0,1)]
        return vals[0][0]+vals[1][0],vals[0][1]+vals[1][1],vals[0][2]+vals[1][2]
    root=stats(tab);LH,LTC,LI=visit(tab,coords,order,'',F(1))
    check(sums['MI']+sums['Gamma']+LTC==root['TC']+sums['JS'])
    check(sums['B']+sums['JS']+LH==root['H'])
    check(sums['D']-sums['MI']+LH==root['H']-sums['JS'])
    check(massI+LI==root['I'])
    classes={}
    for cls in ['control','selector','data']:
        rows=[row for row in nodes if row['node_class']==cls]
        classes[cls]={}
        for m in METRICS:
            v=Log()
            for row in rows:v=v+Log({int(p):F(c) for p,c in row[m]['prime_log_coefficients'].items()}).scale(F(row['weight']))
            classes[cls][m]=v.data()
    return dict(nodes=nodes,leaves=leaves,sums={m:v.data() for m,v in sums.items()},classes=classes,leaf_H=LH.data(),leaf_TC=LTC.data(),leaf_I=str(LI),spent_I=str(massI),net_erasure_with_terminal=(sums['B']+LH).data())

orders={'CF-core':[2,3,4,5],'CF-split':[2,3,4,5,6],'SF-split':[6,2,3,4,5],'CF-full':[2,3,4,5,6,0,1],'SF-full':[6,2,3,4,5,0,1]}
tab=family(4);root=stats(tab);results={name:tree(tab,list(range(7)),order) for name,order in orders.items()}
core=stats(family(0));check(core['I']==F(7,4));check(core['a'][0]==F(1,4));check(root['I']==F(19,64))
for r in range(1,5):
    st=stats(family(r));p=F(1,2**r)
    check(st['I']==p*(F(7,4)+F(3,4)*r))
    check(st['M']==h(p*F(3,4)).scale(r)+h(p*F(3,4)).scale(2)+h(p*F(1,4)))
formula=[]
for r in range(1,13):
    p=F(1,2**r);c=F(3,4)
    debt=total(h(c/F(2**m)).scale(F(2**m)) for m in range(1,r+1)).scale(p)
    # Closed entropy from root empty atom and repeated nonempty core/control atoms.
    H=entropy([(1-p*c)**2]) + entropy([p*p*c*c]).scale(F(2**r-1))
    H=H+entropy([p*p*a*a for a in core['a'][1:]]).scale(F(2**r))
    M=h(p*c).scale(r+2)+h(p*F(1,4));TC=M-H
    # Sum Gamma exactly from Bernoulli resets on the live control chain.
    Gamma=Log()
    for m in range(1,r+1):
        pm=F(1,2**m)
        phi=lambda t:h(t)-h(2*t).scale(F(1,2))
        gm=phi(pm*c).scale(m-1)+total(phi(pm*d) for d in core['d'])
        Gamma=Gamma+gm.scale(p/pm)
    check(debt+Gamma+core['M'].scale(p)==M)
    formula.append({'r':r,'p':str(p),'I':str(p*(F(7,4)+r*c)),'control_marginal_debt':debt.data(),'control_Gamma':Gamma.data(),'H':H.data(),'TC':TC.data()})
for row in formula:
    if row['r']==4:
        check(Log({int(p):F(c) for p,c in row['control_marginal_debt']['prime_log_coefficients'].items()})==Log({int(p):F(c) for p,c in results['CF-core']['sums']['D']['prime_log_coefficients'].items()}))
        check(Log({int(p):F(c) for p,c in row['H']['prime_log_coefficients'].items()})==root['H'])

# Rigorous rational prime-log bounds. Range reduction ensures |z|<=1/3.
def ln_interval(q):
    q=F(q);e=0
    while q>=2:q/=2;e+=1
    while q<1:q*=2;e-=1
    def series(x):
        z=(x-1)/(x+1);s=F(0);power=z
        for j in range(96):s+=power/F(2*j+1);power*=z*z
        tail=2*power/(F(193)*(1-z*z))
        return 2*s,2*s+tail
    a,b=series(q);u,v=series(F(2))
    return (a+e*u,b+e*v) if e>=0 else (a+e*v,b+e*u)
L2,U2=ln_interval(F(2))
def bounds(v):
    lo=F(0);hi=F(0)
    for p,c in v.v.items():
        a,b=ln_interval(F(p));a,b=a/U2,b/L2
        if c>=0:lo+=c*a;hi+=c*b
        else:lo+=c*b;hi+=c*a
    return lo,hi
certs={}
for name,res in results.items():
    net=Log({int(p):F(c) for p,c in res['net_erasure_with_terminal']['prime_log_coefficients'].items()})
    lo,hi=bounds(net)
    check(hi < 8*root['I'])
    certs[name]={'net_lower':str(lo),'net_upper':str(hi),'net_over_I_display':float((lo+hi)/2/root['I']),'upper_below_8I':True}
def restored(d):return Log({int(p):F(c) for p,c in d['prime_log_coefficients'].items()})
gap=restored(results['SF-split']['net_erasure_with_terminal'])-restored(results['CF-split']['net_erasure_with_terminal'])
gl,gu=bounds(gap);check(gl>F(26,10000) and gu<F(27,10000))
certs['SF_minus_CF_split']={'lower':str(gl),'upper':str(gu),'between_26_and_27_over_10000':True}
for name in ['CF-core','CF-split','SF-split']:
    v=restored(results[name]['sums']['reset']);lo,hi=bounds(v);check(hi<0)
    certs[name]['total_reset_negative']=True
summary={'status':'PASS','assertions':ASSERTIONS,'runtime_seconds':time.monotonic()-START,'root':{'H':root['H'].data(),'TC':root['TC'].data(),'I':str(root['I'])},'trees':results,'formula_summaries':formula,'interval_certificates':certs}
(BASE/'out/EXACT_LEDGER.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':ASSERTIONS,'runtime_seconds':summary['runtime_seconds'],'root_I':str(root['I']),'root_H_display':root['H'].display(),'root_TC_display':root['TC'].display(),'trees':{name:{'sums':{m:r['sums'][m]['display_only'] for m in METRICS},'leaf_H':r['leaf_H']['display_only'],'leaf_TC':r['leaf_TC']['display_only'],'net':r['net_erasure_with_terminal']['display_only'],'nodes':len(r['nodes']),'leaves':len(r['leaves'])} for name,r in results.items()}},indent=2))
