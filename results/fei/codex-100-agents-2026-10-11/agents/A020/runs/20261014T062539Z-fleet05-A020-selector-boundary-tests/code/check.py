from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,argparse,sys,importlib.util
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('arith',R.parent/'20261014T002716Z-fleet05-A020-selector-boundary-tests/code/check.py');a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
def law(v):return [Q(w*w,len(v)**2) for w in a.walsh(v)]
def formadd(out,other,c=Q(1)):
    for p,w in other.items():
        out[p]=out.get(p,Q(0))+c*w
        if not out[p]:del out[p]
    return out
@lru_cache(None)
def factors(n):
    out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d=3 if d==2 else d+2
    if n>1:out[n]=out.get(n,0)+1
    return out
def logterm(q,w):
    out={}
    for p,e in factors(q.numerator).items():out[p]=w*e
    for p,e in factors(q.denominator).items():out[p]=out.get(p,Q(0))-w*e
    return {p:v for p,v in out.items() if v}
def ce(P,Qref):
    out={}
    for p,q in zip(P,Qref):
        if p:
            assert q>0;formadd(out,logterm(q,-p))
    return out
def entropy(P):return ce(P,P)
def kl(P,Qref):return formadd(ce(P,Qref),entropy(P),-1)
def interval(f):
    lo=hi=Q(0)
    for p,w in f.items():
        l,h=a.lograt(p)
        if w>=0:lo+=w*l;hi+=w*h
        else:lo+=w*h;hi+=w*l
    return lo,hi
def jsonform(f):return {str(p):str(w) for p,w in f.items()}
def activation(g,Qg):
    # s on two independent bits, one point negative and mean1/2.
    s=[-1,1,1,1];ps=law(s);N=len(g);G=[g[y]*s[z] for z in range(4) for y in range(N)]
    PG=law(G);QG=[q*p for p in ps for q in Qg]
    # x is low bit, private G bits following it.
    F=[1 if not(t&1) else G[t>>1] for t in range(2*len(G))];PF=law(F);QF=[]
    for T in range(len(G)):
        row=PF[2*T]+PF[2*T+1];qrow=(QG[T]+int(T==0))/2
        if row:QF.extend([qrow*PF[2*T]/row,qrow*PF[2*T+1]/row])
        else:QF.extend([qrow,Q(0)])
    assert sum(QF)==1
    refund=formadd(kl(PG,QG),kl(PF,QF),-2)
    refund={p:w/2 for p,w in refund.items()}
    return dict(PF=PF,QF=QF,CE=ce(PF,QF),D=refund,F=F)
def case(k):
    delta=Q(1,1<<k);N=1<<(k+1)
    children=[]
    for q in [0,1]:children.append([(-1)**q if (y>>1)==0 else (-1)**(y&1) for y in range(N)])
    p0,p1=map(law,children);assert p0==p1
    means=[Q(sum(v),N) for v in children];assert means==[delta,-delta]
    h=[children[t&1][t>>1] for t in range(2*N)];ph=law(h)
    assert a.edges(h,0)==delta and sum(h)==0
    qchild=[(p+int(i==0))/2 for i,p in enumerate(p0)]
    qh=[]
    for U in range(N):
        row=ph[2*U]+ph[2*U+1]
        if row:qh.extend([qchild[U]*ph[2*U]/row,qchild[U]*ph[2*U+1]/row])
        else:qh.extend([qchild[U],Q(0)])
    assert sum(qh)==1 and ph[0]==qh[0]==0 and ph[1]==delta*delta
    # The true-positive empty unqueried row forces all reference mass to query-present.
    assert qh[1]==(1+delta*delta)/2
    assert a.energy(children[0])==1+(k-1)*delta and a.energy(h)==1+k*delta
    assert sorted(p for p in ph if p)==sorted(p for p in p0 if p)
    dcore=formadd(kl(p0,qchild),kl(ph,qh),-1)
    assert interval(dcore)==(0,0)
    parent=activation(h,qh);c0=activation(children[0],qchild);c1=activation(children[1],qchild)
    assert interval(parent['D'])==(0,0)
    lam={};formadd(lam,c0['D'],Q(1,2));formadd(lam,c1['D'],Q(1,2));formadd(lam,parent['D'],-1);formadd(lam,dcore,Q(-1,2))
    u=delta*delta/4;t=(1+delta*delta)/8
    expected=logterm(u/t,u/2);formadd(expected,logterm((1+t)/(1+u),(1+u)/2))
    difference=formadd(dict(lam),expected,-1)
    assert interval(difference)==(0,0)
    l,hhi=interval(lam);ln2lo,ln2hi=a.logint(2)
    assert l>ln2hi/32
    assert a.edges(parent['F'],1)==delta/2
    # Actual entropy insertion is small; the fixed positive term is reference debt.
    dce=dict(parent['CE']);formadd(dce,c0['CE'],Q(-1,2));formadd(dce,c1['CE'],Q(-1,2))
    curve=entropy(parent['PF']);formadd(curve,entropy(c0['PF']),Q(-1,2));formadd(curve,entropy(c1['PF']),Q(-1,2))
    assert interval(formadd(formadd(dict(dce),curve,-1),lam,-1))==(0,0)
    for node in [parent,c0,c1]:
        assert interval(node['CE'])[1]<=4*a.energy(node['F'])*ln2lo
    mixed=[]
    for S in range(len(parent['PF'])):
        if S&2:continue
        v,w=parent['PF'][S],parent['PF'][S|2]
        if v and w:mixed.append((v,w))
    assert mixed==[(Q(1,4),u/4)]*2
    Bq=logterm(1+u,(1+u)/2);formadd(Bq,logterm(u,-u/2))
    assert interval(Bq)[1]<(delta/2)*ln2lo
    for P,Qref,Iv in [(p0,qchild,a.energy(children[0])),(ph,qh,a.energy(h))]:
        assert interval(ce(P,Qref))[1] <= 4*Iv*ln2lo
    # Guard the balanced-child source repair under both zero-row conventions.
    balanced=[]
    for q in [0,1]:balanced.append([(-1)**(y&1)*(-1)**(q*int((y>>1)==0)) for y in range(N)])
    pbal=list(map(law,balanced));hb=[balanced[t&1][t>>1] for t in range(2*N)];pb=law(hb)
    qbchild=[[(p+int(i==0))/2 for i,p in enumerate(P)] for P in pbal]
    av=[(x+y)/2 for x,y in zip(*qbchild)]
    outcomes={}
    for absent in [True,False]:
        qr=[]
        for U in range(N):
            row=pb[2*U]+pb[2*U+1]
            if row:qr.extend([av[U]*pb[2*U]/row,av[U]*pb[2*U+1]/row])
            else:qr.extend([av[U],Q(0)] if absent else [av[U]/2]*2)
        ap=activation(hb,qr);ab=[activation(v,ref) for v,ref in zip(balanced,qbchild)]
        dc={};formadd(dc,kl(pbal[0],qbchild[0]),Q(1,2));formadd(dc,kl(pbal[1],qbchild[1]),Q(1,2));formadd(dc,kl(pb,qr),-1)
        refund={};formadd(refund,ab[0]['D'],Q(1,2));formadd(refund,ab[1]['D'],Q(1,2));formadd(refund,ap['D'],-1);formadd(refund,dc,Q(-1,2))
        target={} if absent else logterm(Q(18,17),Q(1,2))
        assert interval(formadd(dict(refund),target,-1))==(0,0)
        outcomes['absent' if absent else 'equal']=jsonform(refund)
    return dict(k=k,n_parent_core=k+2,n_F=k+5,delta=str(delta),means=[str(q) for q in means],query_essential=True,parent_core_empty_reference='0',parent_empty_unqueried_true_mass=str(delta*delta),child_core_empty_reference=str((1+delta*delta)/2),core_refund='0',parent_activation_refund='0',Lambda_nats_interval=[str(l),str(hhi)],Lambda_bits_lower_bound='1/32',Lambda_exact_form=jsonform(expected),parent_CE_form=jsonform(parent['CE']),child_CE_forms=[jsonform(c0['CE']),jsonform(c1['CE'])],rate4_core_references=True,rate4_activation_references=True,actual_query_K1_good=True,Bquery_form=jsonform(Bq),insertion_identity=True,balanced_source_guard=outcomes)
def main(pilot):
    start=time.perf_counter();rows=[]
    for k in ([3] if pilot else range(3,9)):
        rows.append(case(k));assert time.perf_counter()-start<60
        (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(dict(status='PASS',cases=len(rows),rows=rows,runtime_seconds=time.perf_counter()-start),indent=2))
    print(json.dumps(dict(status='PASS',cases=len(rows),runtime_seconds=time.perf_counter()-start)))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
