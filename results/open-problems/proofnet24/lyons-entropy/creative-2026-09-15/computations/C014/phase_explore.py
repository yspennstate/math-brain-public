import math, random, json

def jacobi(mat):
    a=[r[:] for r in mat]; n=len(a)
    for _ in range(n*n*60):
        v,p,q=max((abs(a[p][q]),p,q) for p in range(n) for q in range(p+1,n))
        if v<1e-12: break
        tau=(a[q][q]-a[p][p])/(2*a[p][q]); t=math.copysign(1,tau)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+t*t); s=t*c
        app=a[p][p]; aqq=a[q][q]; apq=a[p][q]
        a[p][p]=app-t*apq; a[q][q]=aqq+t*apq; a[p][q]=a[q][p]=0
        for k in range(n):
            if k not in (p,q):
                akp=a[k][p]; akq=a[k][q]
                a[k][p]=a[p][k]=c*akp-s*akq
                a[k][q]=a[q][k]=s*akp+c*akq
    return sorted(a[i][i] for i in range(n))

def atoms(diag,edges):
    out=[]
    for mask in range(8):
        d=[diag[i]-(not(mask>>i&1)) for i in range(3)]
        p=d[0]*d[1]*d[2]-sum(d[i]*abs(edges[i])**2 for i in range(3))+2*(edges[0]*edges[1]*edges[2]).real
        g=[0.]*9; h=[[0.]*9 for _ in range(9)]
        for i in range(3):
            j,k=[a for a in range(3) if a!=i]
            g[i]=d[j]*d[k]-abs(edges[i])**2
            h[i][j]=h[j][i]=d[k]
            h[i][k]=h[k][i]=d[j]
            for a,z in enumerate((1,1j)):
                ia=3+2*i+a
                g[ia]=-2*d[i]*(edges[i].conjugate()*z).real+2*(z*edges[j]*edges[k]).real
                h[ia][ia]=-2*d[i]
                h[i][ia]=h[ia][i]=-2*(edges[i].conjugate()*z).real
                for b,w in enumerate((1,1j)):
                    jb=3+2*j+b
                    h[ia][jb]=h[jb][ia]=2*(z*w*edges[k]).real
                    kb=3+2*k+b
                    h[ia][kb]=h[kb][ia]=2*(z*w*edges[j]).real
        sign=(-1)**(3-mask.bit_count())
        out.append((sign*p,[sign*x for x in g],[[sign*x for x in r] for r in h]))
    return out

def hessian(diag,edges):
    aa=atoms(diag,edges)
    if min(p for p,_,_ in aa)<=0: return None
    hh=[[0.]*9 for _ in range(9)]
    scale=[1.]*3+[1/math.sqrt(2)]*6
    for p,g,h in aa:
        for i in range(9):
            for j in range(9):hh[i][j]+=(-g[i]*g[j]/p-h[i][j]*math.log(p))*scale[i]*scale[j]
    return hh

def profile(d,r,n=25):
    res=[]
    for i in range(n):
        c=-1+2*i/(n-1); e=[r[0],r[1],r[2]*complex(c,math.sqrt(max(0,1-c*c)))]
        hh=hessian(d,e)
        if hh is not None:res.append((c,jacobi(hh)[-1]))
    return res

def run():
    rng=random.Random(14014)
    records=[]
    for idx in range(300):
        d=[rng.uniform(.12,.88) for _ in range(3)]
        r=[rng.uniform(.01,.2) for _ in range(3)]
        pf=profile(d,r,17)
        if len(pf)<17:continue
        # full phase endpoints and quadrature center
        anchors=max(pf[0][1],pf[8][1],pf[-1][1]); best=max(pf,key=lambda t:t[1])
        if best[1]>anchors+1e-7:
            rec={'d':d,'r':r,'profile':pf,'gap':best[1]-anchors}
            records.append(rec)
            print(json.dumps(rec),flush=True)
            if len(records)>=8:break
    print('COUNT',len(records))

if __name__=='__main__':run()

def solve(a,b):
    n=len(b); a=[list(row)+[b[i]] for i,row in enumerate(a)]
    for i in range(n):
        piv=max(range(i,n),key=lambda j:abs(a[j][i]))
        a[i],a[piv]=a[piv],a[i]
        f=a[i][i]
        if abs(f)<1e-18: raise ZeroDivisionError()
        for k in range(i,n+1):a[i][k]/=f
        for j in range(n):
            if i!=j:
                f=a[j][i]
                for k in range(i,n+1):a[j][k]-=f*a[i][k]
    return [row[-1] for row in a]

def danger(diag,edges):
    aa=atoms(diag,edges)
    if min(p for p,_,_ in aa)<=0:return None
    f=[-math.log(p) for p,_,_ in aa]
    tau=sum((-1)**(3-mask.bit_count())*f[mask] for mask in range(8))
    cs=[f[(7^(1<<i))]-sum(f[1<<j] for j in range(3) if i!=j)+f[0] for i in range(3)]
    mm=[cs[i]+tau*diag[i] for i in range(3)]
    detm,gm,hm=atoms(mm,[tau*e for e in edges])[7]
    scale=[1.]*3+[1/math.sqrt(2)]*6
    gm=[gm[i]*scale[i] for i in range(9)]
    hm=[[hm[i][j]*scale[i]*scale[j] for j in range(9)] for i in range(9)]
    fi=[[sum(g[i]*g[j]/p for p,g,h in aa)*scale[i]*scale[j] for j in range(9)] for i in range(9)]
    nn=[[fi[i][j]+gm[i]*gm[j]/detm-hm[i][j] for j in range(9)] for i in range(9)]
    zz=solve(nn,gm)
    return sum(g*z for g,z in zip(gm,zz))/detm
