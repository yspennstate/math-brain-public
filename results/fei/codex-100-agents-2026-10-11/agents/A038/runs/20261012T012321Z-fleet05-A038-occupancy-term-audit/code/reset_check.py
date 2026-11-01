from pathlib import Path
from fractions import Fraction as F
import ast,time,json

ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter()
# Reuse ONLY pure helper declarations, never execute the other checker's jobs.
source=ROOT/'code'/'tree_release.py'
tree=ast.parse(source.read_text(encoding='utf-8'))
decls=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef))]
decls += [n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['LN2','ell'] for t in n.targets)]
env={'__file__':str(source),'started':started,'checks':0}
exec(compile(ast.Module(body=decls,type_ignores=[]),str(source),'exec'),env)
check=env['check'];linear=env['linear'];h=env['h'];phi=env['phi'];lg=env['lg'];interval=env['interval'];out=env['out'];addlog=env['addlog'];clean=env['clean'];ell=env['ell']

def kl(p,q):
    z={}
    for a,b in zip(p,q):
        if a:check(b>0);addlog(z,a/b,a)
    return clean(z)
nodes={1:{'O':{},'rho':{},'Gamma':{},'JS':{}}}
for k in range(2,17):
    d=F(1,2**(k-1));q0=(1-d)**2+d*d;beta=2*d*(1-d)
    qc=(1-d)**(k-1)/(2*q0);qa=1-qc
    check(F(1,4)<=qc<=F(1,2))
    O=kl([F(1,2)]*2,[qc,qa]);Gamma=linear((k-1,phi(d)));JS=phi(beta)
    rho=linear((1,O),(1,JS),(-1,Gamma))
    if k<=7:
        size=2**(k-1)
        P0=[(1-2*d)**2]+[4*d*d]*(size-1)
        P1=[F(1)]+[F(0)]*(size-1)
        residual=[(P0[t]+P1[t])/2 for t in range(size)]
        R=[d**t.bit_count()*(1-d)**(k-1-t.bit_count()) for t in range(size)]
        Ka=[P0[t]/(2*residual[t]) for t in range(size)]
        Kc=[P1[t]/(2*residual[t]) for t in range(size)]
        check(sum(R[t]*Kc[t] for t in range(size))==qc)
        Qa=[R[t]*Ka[t]/qa for t in range(size)]
        Qc=[R[t]*Kc[t]/qc for t in range(size)]
        Ra=[(2*d)**t.bit_count()*(1-2*d)**(k-1-t.bit_count()) for t in range(size)]
        Rc=[F(1)]+[F(0)]*(size-1)
        direct={}
        for P,Q,newR in [(P0,Qa,Ra),(P1,Qc,Rc)]:
            for p,a,b in zip(P,Q,newR):
                if p:check(a>0 and b>0);addlog(direct,a/b,p/2)
        check(clean(direct)==rho)
        check(sum(Qa)==sum(Qc)==1)
    if k>=3:
        eps=1-2*qc
        check(0<=eps<=F(1,2));check(eps<=2*(k-2)*d)
        oi=interval(O)
        check(oi[0]>0)
        check(oi[1]<F(8,3)*ell[0]*(k-2)**2*d*d)
    else:check(O=={})
    nodes[k]={'O':O,'rho':rho,'Gamma':Gamma,'JS':JS}

rows=[]
for n in range(2,17):
    d=F(1,2**(n-1));I=n*d;totals={k:{} for k in ['O','rho','Gamma','JS']}
    for k in range(1,n+1):
        w=F(2**k,2**n)
        for name in totals:totals[name]=linear((1,totals[name]),(w,nodes[k][name]))
    check(totals['rho']==linear((1,totals['O']),(1,totals['JS']),(-1,totals['Gamma'])))
    oi=interval(totals['O'])
    if n>2:check(oi[0]>0)
    check(oi[1]<8*ell[0]*d)
    if n>=9:check(interval(totals['rho'])[1]<0)
    rows.append({'n':n,'I':str(I),'outcome_KL_over_I':out((oi[0]/I,oi[1]/I)),'signed_reset_over_I':out(tuple(x/I for x in interval(totals['rho'])))})
result={'status':'PASS','assertions':env['checks'],'elapsed_seconds':time.perf_counter()-started,'dimensions':15,'direct_reset_nodes':6,'rows':rows}
(ROOT/'out'/'RESET_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}));print('n16',json.dumps(rows[-1]))
