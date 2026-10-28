from pathlib import Path
from fractions import Fraction as F
import sys, json, importlib.util, time
sys.dont_write_bytecode = True
R = Path(__file__).resolve().parents[1]
sp = importlib.util.spec_from_file_location('prior', R.parent/'20261023T025703Z-account03-A083-formal-core/code/balanced_core.py')
B = importlib.util.module_from_spec(sp); sp.loader.exec_module(B)
P, E = B.P, B.E
START = time.perf_counter(); CHECKS = 0
def ck(x):
    global CHECKS
    CHECKS += 1
    if not x: raise AssertionError(CHECKS)
    if time.perf_counter()-START > 60: raise TimeoutError('frozen60s')
def add(*v): return E.add(*v)
def mul(v,c): return E.mul(v,c)
def iv(v):
    lo=hi=F(0)
    for p,c in v.items():
        a,b=E.scale(E.log2_interval(F(p)),c);lo+=a;hi+=b
    return lo,hi
def spike(t, alpha=F(1,6)):
    p=P.spectral(t)
    if sum(bool(a) for a in p)==1: return list(p)
    full=len(p)-1
    return [p[0]]+[(1-alpha)*p[s]+(alpha*(1-p[0]) if s==full else 0) for s in range(1,len(p))]
g=(1,-1,-1,1,-1,1,1,1)
h=tuple((-1)**(s&1)*g[s>>1] for s in range(16))
pg=P.spectral(g); qg=spike(g)
qh=[F(0)]*16
for s,a in enumerate(qg):qh[1+2*s]=a
t=B.gate(h);p=P.spectral(t);Q=B.lift(P.spectral(h),qh)
# Flip only the y frequency of a fraction eta of the declared INITIAL law.
eta=F(1,5);Q=[(1-eta)*Q[s]+eta*Q[s^64] for s in range(128)]
ck(p==B.direct(t));ck(B.inf(g)==F(9,4));ck(B.inf(h)==F(13,4));ck(B.inf(t)==F(21,8))
Hg=B.ent(pg);CEg=add(Hg,P.kl(pg,qg));C=mul(P.vec_log(F(5,4)),F(1,2))
A0=P.kl(p,Q);ck(A0==add(mul(P.kl(pg,qg),F(1,2)),C))
H0=B.ent(p);ck(add(H0,A0)==add({2:F(3)},mul(CEg,F(1,2)),C))
nodes=[(t,Q,F(1),['x','z','a','u','v','b','y'],{})]
releases={}; rows=[]; booking=None
for name in ['b','y','x','a']:
    new=[]; release={}
    for tt,qq,w,labels,path in nodes:
        if name=='a' and path['x']==1:
            new.append((tt,qq,w,labels,path));continue
        i=labels.index(name)
        # Z labels the y fiber at b; otherwise the complete remaining set.
        Z=(1<<(labels.index('y')-1)) if name=='b' else (1<<(len(labels)-1))-1
        row,d=P.query(tt,i,Z,qq,'fair');rows.append({'query':name,'reach':str(w),'path':path,'reference_outcomes':[str(sum(a)) for a in d[5]],'ghost_mass':row['reference_only_erased_mass']})
        if name=='b':
            ck(row['conditional_child_KL']==P.serial(C));booking=row['conditional_child_KL']
        childrefs=[[a/sum(d[5][j]) for a in d[5][j]] for j in (0,1)]
        dc=mul(add(*(P.kl(d[3][j],childrefs[j]) for j in (0,1))),F(1,2))
        release=add(release,mul(add(P.kl(P.spectral(tt),qq),mul(dc,-1)),w))
        if name=='a': ck(list(qq)==qh)
        for j in (0,1):
            child=P.child(tt,i,j);ql=childrefs[j]
            if name=='a':
                # Remaining z is a forced Fourier character, not part of the spike block.
                gc=tuple(child[2*k] for k in range(len(child)//2));qgc=spike(gc)
                fresh=[F(0)]*len(child)
                for s,a in enumerate(qgc):fresh[1+2*s]=a
                # Independent literal inherited profile: parity exact, point alpha/(2-alpha)=1/11.
                if j==0: ck(ql==fresh)
                else:
                    inherited=[F(1,4),F(5,22),F(5,22),F(13,44)]
                    ck([ql[1+2*s] for s in range(4)]==inherited)
                new.append((child,fresh,w/2,[z for z in labels if z!=name],dict(path,**{name:j})))
            else:new.append((child,ql,w/2,[z for z in labels if z!=name],dict(path,**{name:j})))
    releases[name]=release;nodes=new
    if name=='y':ck(release==C)
sigma=mul(P.vec_log(F(1404,1331)),F(1,16))
Df={};HL={};IL=F(0)
for tt,qq,w,labels,path in nodes:
    ck(P.spectral(tt)==B.direct(tt))
    Df=add(Df,mul(P.kl(P.spectral(tt),qq),w))
    HL=add(HL,mul(B.ent(P.spectral(tt)),w));IL+=w*B.inf(tt)
ck(len(nodes)==12 and sum(z[2] for z in nodes)==1)
ck(add(A0,sigma)==add(*(releases.values()),Df))
ck(HL=={2:F(1,2)} and IL==F(5,4))
S=add({2:4*IL},mul(HL,-1));ck(S=={2:F(9,2)})
edge=add(H0,mul(HL,-1),{2:-4*(B.inf(t)-IL)})
ck(edge==add({2:F(-3)},mul(Hg,F(1,2))))
bill=add(A0,edge,sigma);ck(iv(bill)[1]<0)
ck(iv(sigma)[0]>0);ck(iv(CEg)[1]<F(53,16))
ck(6**3<2*5**3 and 5**3<2*4**3 and 1404<2*1331)
tensor=[]
for m in range(1,65):
    # Entire infinite family is proved in PROOF.md, these are exact formula checks only.
    original=add({2:3+F(9,2)*m},mul(CEg,-F(m,2)),mul(C,-1))
    price=mul(sigma,m);terminal=2+F(5,2)*m
    ck(iv(add(original,mul(price,-1),{2:-terminal}))[0]>0)
    tensor.append({'m':m,'terminal_S4':str(terminal),'after_old_quarter':str(terminal-F(1,4))})
result={'status':'PASS','physical_histories':1,'physical_leaves':len(nodes),'tensor_formula_cases':64,'checks':CHECKS,'helper_checks':P.CHECKS,'seconds':time.perf_counter()-START,'g':list(g),'pg':list(map(str,pg)),'qg':list(map(str,qg)),'old_y_conditional_booking':booking,'initial_KL':P.serial(A0),'query_releases':{k:P.serial(v) for k,v in releases.items()},'positive_actual_reset':P.serial(sigma),'complete_final_KL':P.serial(Df),'signed_edge':P.serial(edge),'signed_bill_interval':E.outward(iv(bill)),'terminal_S4':'9/2','after_old_quarter':'17/4','rows':rows,'tensor_cases':tensor,'full_FEI':'OPEN','formal_check':'Not requested: exact rational identity certificate; no compiler admission used'}
(R/'out/RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','physical_histories','physical_leaves','tensor_formula_cases','checks','helper_checks','seconds','after_old_quarter']}))
