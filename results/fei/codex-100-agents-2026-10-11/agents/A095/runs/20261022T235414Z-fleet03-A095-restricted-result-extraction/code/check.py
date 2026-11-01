from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]
P=R.parents[0]/'20261021T180853Z-fleet03-A095-restricted-result-extraction/code/check.py'
spec=importlib.util.spec_from_file_location('own_previous_arithmetic',P);A=importlib.util.module_from_spec(spec);spec.loader.exec_module(A)
def add(*xs):return tuple(sum(x[i] for x in xs) for i in (0,1))
def scale(x,v):return (x[0]*v,x[1]*v) if v>=0 else (x[1]*v,x[0]*v)
def sub(x,y):return add(x,scale(y,-1))
def overlap(x):A.ck(x[0]<=0<=x[1])
def cost(v,Q):return A.ce([a*a for a in A.walsh(v)],Q)
def rounded(x):
    D=2**80
    return [str(F((x[0]*D).__floor__(),D)),str(F((x[1]*D).__ceil__(),D))]
def model(g,m):
    k=len(g).bit_length()-1;n=k+m;e=F(1,2**n);ac=A.walsh(g);p=[x*x for x in ac];s=sum(x!=0 for x in p)
    gg=[g[x%len(g)] for x in range(2**n)];v=gg+gg;v[2**n]*=-1
    W=2*e-s*e*e
    Q=[(1-W)*p[x] if x<len(p) and p[x] else e*e for x in range(len(v))]
    A.ck(sum(Q)==1);vv=A.walsh(v)
    for x,a in enumerate(vv):
        A.ck(a==ac[x]-g[0]*e if x<len(p) and p[x] else abs(a)==e)
        if a:A.ck(Q[x]>0)
    return v,Q
def source(t,b):
    if b==0:return [-(1-2*(x==0)) for x in range(2**t)]
    return [(1-2*((x%2**t)==0))*(1-2*((x>>t)==0)) for x in range(2**(t+b))]
def tensorcheck(v,Q):
    p=[x*x for x in A.walsh(v)];r=[F(1,3),F(2,3)];p2=p+[F(0)]*len(p);q2=[q*a for a in r for q in Q]
    z=cost(v,Q);term=A.ce([F(1),F(0)],r)
    overlap(sub(A.ce(p2,q2),add(z,term)));A.ck(sum(q2[len(p):])==F(2,3))
def rootcase(w,m):
    _,_,_,v,Q,delta=A.root(w,m);C0=cost(v,Q);I=A.influence(v)
    A.ck(4*I-C0[1]>F(451,256));rho=F(1);G=(F(0),F(0));siblings=[];rows=[];spend=F(0)
    for d in range(w+1):
        t=w-d;C=cost(v,Q);before=add(G,scale(C,rho),*(scale(c,r) for r,c,_ in siblings));overlap(sub(before,C0))
        vs,Qs=A.transport(v,Q,t);cs=[cost(z,q) for z,q in zip(vs,Qs)]
        Gn=add(G,scale(sub(C,scale(add(*cs),F(1,2))),rho));lam1=rho/2
        a,q1=model(source(t,1),m);A.ck(a==vs[0]);Ccan=cost(a,q1)
        A.ck(Ccan[1]<4)
        if t>=4:A.ck(Ccan[1]<2)
        for eta in [F(0),F(1,4)]:
            fresh=[(1-eta)*q+eta/F(len(q1)) for q in q1];C1=cost(vs[0],fresh)
            e1=scale(sub(C1,cs[0]),lam1)
            L1=add(Gn,*(scale(c,r) for r,c,_ in siblings),scale(cs[1],lam1),scale(C1,lam1))
            overlap(sub(L1,add(C0,e1)));A.ck(lam1*C1[1]<F(5,4))
            A.ck(4*I-L1[1]>F(75,256))
            zz,rr=A.transport(vs[0],fresh,t);cc=[cost(z,r) for z,r in zip(zz,rr)]
            G2=add(Gn,scale(sub(C1,scale(add(*cc),F(1,2))),lam1));lam2=rho/4
            z,q2=model(source(t,0),m);A.ck(z==zz[0]);C2=cost(z,q2);A.ck(C2[1]<4)
            if t>=4:A.ck(C2[1]<2)
            A.ck(lam2*C2[1]<F(1,2))
            e2=scale(sub(C2,cc[0]),lam2)
            L2=add(G2,*(scale(c,r) for r,c,_ in siblings),scale(cs[1],lam1),scale(cc[1],lam2),scale(C2,lam2))
            overlap(sub(L2,add(C0,e1,e2)))
            # Both conservative bookings use the ORIGINAL root bank.
            p1=max(e1[1],F(0));p2=max(e2[1],F(0));A.ck(p1<F(5,4));A.ck(p2<F(1,2))
            A.ck(4*I-C0[1]-p1-p2>F(3,256));A.ck(4*I-L2[1]>F(3,256))
            remain=sum((r*ii for r,_,ii in siblings),F(0))+lam1*A.influence(vs[1])+lam2*(A.influence(zz[0])+A.influence(zz[1]))
            spend2=spend+rho*sum(F(v[x]!=v[x^(1<<t)],len(v)) for x in range(len(v)))+lam1*sum(F(vs[0][x]!=vs[0][x^(1<<t)],len(vs[0])) for x in range(len(vs[0])))
            A.ck(I==spend2+remain)
            if t==0 and m==0:A.ck(q2==[F(0),F(1)]);A.ck(C2==(F(0),F(0)))
            if w==4 and m==0 and d in (0,w):tensorcheck(zz[0],q2);tensorcheck(zz[1],rr[1])
            unused=4*I-L2[1];unused_conservative=4*I-C0[1]-p1-p2
            rows.append({'w':w,'m':m,'d':d,'eta':str(eta),'e1':rounded(e1),'e2':rounded(e2),'p1_upper':rounded((p1,p1))[1],'p2_upper':rounded((p2,p2))[1],'old_releases':rounded(G2),'final_ledger':rounded(L2),'unused_original_lower':rounded((unused,unused))[0],'conservative_unused_lower':rounded((unused_conservative,unused_conservative))[0],'physical_spent':str(spend2),'remaining_I':str(remain),'C2':rounded(C2),'zero_reference_boundary':t==0 and m==0})
        if d<w:
            vs,Qs=A.transport(v,Q,0);cs=[cost(z,q) for z,q in zip(vs,Qs)]
            G=add(G,scale(sub(C,scale(add(*cs),F(1,2))),rho));spend+=rho*sum(F(v[x]!=v[x^1],len(v)) for x in range(len(v)))
            siblings.append((rho/2,cs[1],A.influence(vs[1])));v,Q=vs[0],Qs[0];rho/=2
    return rows
def main():
    pilot='pilot' in sys.argv;start=time.perf_counter();domain=[(4,0)] if pilot else [(4,0),(4,1),(5,0),(5,1),(6,0)];rows=[]
    for w,m in domain:rows+=rootcase(w,m)
    # Finite diagnostics for the induction / analytic tail, not an all-dimensional certificate.
    for w in range(5,65):
        x=F(2*w+19,2**(w+2))+F(4*w+2,2**(2*w+1));A.ck(x<=F(243,1024))
    for t in range(4,65):
        for m in range(1,33):A.ck(F(4*m,F(1))+F(1,4)<=F(17,4)*2**(m-1))
    out={'status':'PASS','histories':len(rows),'roots':len(domain),'assertions':A.NCHK,'seconds':time.perf_counter()-start,'rows':rows,'positive_second':sum(F(x['e2'][0])>0 for x in rows),'negative_second':sum(F(x['e2'][1])<0 for x in rows),'own_helper_source':str(P),'own_helper_sha256':hashlib.sha256(P.read_bytes()).hexdigest()}
    (R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if pilot else 'EXACT_RESULTS.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['rows','own_helper_source']}))
if __name__=='__main__':main()
