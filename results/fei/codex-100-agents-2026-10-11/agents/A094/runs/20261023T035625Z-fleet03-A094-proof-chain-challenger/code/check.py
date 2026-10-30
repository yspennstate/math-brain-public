from pathlib import Path
from fractions import Fraction as F
import json,sys,time
import arithmetic as A
RUN=Path(__file__).resolve().parents[1]
def add(*xs):
    z=(F(0),F(0))
    for x in xs:z=A.add(z,x)
    return z
def zero(x):A.ck(x[0]<=0<=x[1])
def interval(x):return [str(y) for y in x]
def src(t,k):
    return [(1-2*((x&((1<<t)-1))==0))*(1-2*((x>>t)==0)) for x in range(1<<(t+k))] if k else [-(1-2*(x==0)) for x in range(1<<t)]
def model(g,m):
    k=(len(g)-1).bit_length();n=k+m;ep=F(1,1<<n)
    gg=[g[x&((1<<k)-1)] for x in range(1<<n)]
    v=gg+gg;v[1<<n]*=-1
    p=A.law(g);s=sum(bool(x) for x in p);W=2*ep-s*ep*ep
    Q=[(1-W)*p[j] if j<len(p) and p[j] else ep*ep for j in range(len(v))]
    P=A.law(v);A.ck(sum(Q)==1);A.ck(all(y>=0 and (not x or y>0) for x,y in zip(P,Q)))
    aa=A.fw(g);bb=A.fw(v)
    for j,y in enumerate(bb):
        base=aa[j] if j<len(aa) else F(0)
        A.ck(y==base-g[0]*ep*(-1 if j&(1<<n) else 1))
    if n==0:A.ck(Q==P);A.ck(A.ce(P,Q)==(0,0))
    return v,Q
def transport(v,Q,i):
    vv,qq=A.inherit(v,Q,i,True)
    C=A.ce(A.law(v),Q);cc=[A.ce(A.law(z),q) for z,q in zip(vv,qq)]
    release=A.sub(C,A.scale(add(*cc),F(1,2)))
    A.ck(release[1]>=0)
    A.ck(A.total(v)==A.inf(v,i)+(A.total(vv[0])+A.total(vv[1]))/2)
    return vv,qq,cc,release
def product_test(v,Q,i):
    # Nonconstant Maj3 terminal, nonmatching full-support reference, true-zero labels.
    h=[1 if x.bit_count()>=2 else -1 for x in range(8)]
    ph=A.law(h);R=[F(j+1,36) for j in range(8)]
    p=A.law(v);P=[x*y for y in ph for x in p];QR=[x*y for y in R for x in Q]
    zero(A.sub(A.ce(P,QR),add(A.ce(p,Q),A.ce(ph,R))))
    vv,qq,cc,release=transport(v,Q,i)
    r=[F(0)]*(len(p)//2)
    for j,q in enumerate(Q):r[A.drop(j,i)]+=q
    pp=[A.law(x) for x in vv];mu=[(x+y)/2 for x,y in zip(*pp)]
    raw=[[r[j]*pp[b][j]/mu[j] if mu[j] else r[j] for j in range(len(mu))] for b in [0,1]]
    Z=[sum(q) for q in raw]
    for b in [0,1]:
        # On true-zero terminal labels use SAME core likelihood, as the hypothesis requires.
        fullraw=[a*y for y in R for a in raw[b]]
        A.ck(sum(fullraw)==Z[b]); fullQ=[a/Z[b] for a in fullraw]
        A.ck(fullQ==[a*y for y in R for a in qq[b]])
        fullP=[a*y for y in ph for a in pp[b]]
        zero(A.sub(A.ce(fullP,fullQ),add(cc[b],A.ce(ph,R))))
        for j,y in enumerate(ph):
            if not y:A.ck(sum(fullQ[j*len(mu):(j+1)*len(mu)])==R[j])
    A.ck(len(set(h))==2)
def run(w,m):
    rootv,rootQ=model(src(w,2),m);I=A.total(rootv);C0=A.ce(A.law(rootv),rootQ)
    A.ck(4*I-C0[1]>F(451,256))
    v,Q=rootv,rootQ;rho=F(1);G=(F(0),F(0));sib=[];spent=F(0);rows=[]
    for d in range(w+1):
        t=w-d;C=A.ce(A.law(v),Q)
        zero(A.sub(add(G,*(A.scale(c,r) for r,c in sib),A.scale(C,rho)),C0))
        vv,qold,cold,R1=transport(v,Q,t)
        canonicalv,qcan=model(src(t,1),m);A.ck(canonicalv==vv[0])
        lam1=rho/2;lam2=rho/4
        g1=add(G,A.scale(R1,rho));fixed=add(*(A.scale(c,r) for r,c in sib),A.scale(cold[1],lam1))
        for eta in [F(0),F(1,8),F(1,4)]:
            q1=[(1-eta)*x+eta/len(qcan) for x in qcan]
            c1=A.ce(A.law(vv[0]),q1);e1=A.scale(A.sub(c1,cold[0]),lam1)
            ww,q2old,c2old,R2=transport(vv[0],q1,t)
            freshv,q2=model(src(t,0),m);A.ck(freshv==ww[0])
            c2=A.ce(A.law(ww[0]),q2);e2=A.scale(A.sub(c2,c2old[0]),lam2)
            A.ck(c2[1]<4)
            if t>=4:A.ck(c2[1]<2)
            A.ck(lam1*c1[1]<F(5,4));A.ck(lam2*c2[1]<F(1,2))
            positive_upper=max(F(0),e1[1])+max(F(0),e2[1])
            A.ck(4*I-C0[1]-positive_upper>F(3,256))
            G2=add(g1,A.scale(R2,lam1))
            total=add(G2,fixed,A.scale(add(c2,c2old[1]),lam2))
            zero(A.sub(total,add(C0,e1,e2)))
            A.ck(4*I-total[1]>F(3,256))
            row={'w':w,'m':m,'d':d,'t':t,'eta':str(eta),'e1':interval(e1),'e2':interval(e2),'conservative_margin_lower':str(4*I-C0[1]-positive_upper),'ledger_margin':interval((4*I-total[1],4*I-total[0])),'zero_atom':not all(q2)}
            if t:
                zz,q3old,c3old,R3=transport(ww[0],q2,0)
                finalv,q3=model(src(t-1,0),m);A.ck(finalv==zz[0])
                c3=A.ce(A.law(zz[0]),q3);lam3=lam2/2
                e3=A.scale(A.sub(c3,c3old[0]),lam3)
                total3=add(G2,A.scale(R3,lam2),fixed,A.scale(c2old[1],lam2),A.scale(add(c3,c3old[1]),lam3))
                zero(A.sub(total3,add(C0,e1,e2,e3)))
                row['third']={'e3':interval(e3),'positive':e3[0]>0,'negative':e3[1]<0,'conservative_margin_lower':str(4*I-C0[1]-positive_upper-max(F(0),e3[1])),'ledger_margin':interval((4*I-total3[1],4*I-total3[0]))}
            if w==4 and m==0 and d==2 and eta==F(1,8):product_test(vv[0],q1,t)
            rows.append(row)
        if d<w:
            vv,qq,cc,rel=transport(v,Q,0)
            G=add(G,A.scale(rel,rho));spent+=rho*A.inf(v,0)
            sib.append((rho/2,cc[1]));v,Q=vv[0],qq[0];rho/=2
    return rows
mode=sys.argv[1];start=time.perf_counter();domain=[(4,0)] if mode=='pilot' else [(4,0),(4,2),(5,0),(5,2),(6,0)]
rows=[]
for w,m in domain:rows+=run(w,m)
third=[r['third'] for r in rows if 'third' in r]
out={'status':'PASS','mode':mode,'roots':len(domain),'two_reset_histories':len(rows),'third_reset_histories':len(third),'assertions':A.checks,'seconds':time.perf_counter()-start,'third_positive':sum(r['positive'] for r in third),'third_negative':sum(r['negative'] for r in third),'third_min_conservative_margin':str(min(F(r['conservative_margin_lower']) for r in third)),'rows':rows}
(RUN/'out'/f'{mode.upper()}_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
