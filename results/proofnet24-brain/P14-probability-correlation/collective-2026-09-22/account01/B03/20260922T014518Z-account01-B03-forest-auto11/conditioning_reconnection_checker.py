from fractions import Fraction
from itertools import combinations

def forest(n, es):
    p=list(range(n))
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for a,b in es:
        a,b=f(a),f(b)
        if a==b: return False
        p[a]=b
    return True

def fmasks(n, E):
    return [m for m in range(1<<len(E))
            if forest(n,[E[i] for i in range(len(E)) if (m>>i)&1])]

triples=identity_fail=cov_extension_fail=pos_Xg=pos_Yg=neg_D1=pos_XY=0
witness=None
for n in range(2,6):
    K=list(combinations(range(n),2))
    for gm in range(1<<len(K)):
        E=[K[i] for i in range(len(K)) if (gm>>i)&1]
        if len(E)<2: continue
        for ei,fi in combinations(range(len(E)),2):
            e,f=E[ei],E[fi]
            B=[h for j,h in enumerate(E) if j not in (ei,fi)]
            M=fmasks(n,B); N=len(M)
            vals=[]
            for m in M:
                H=[B[i] for i in range(len(B)) if (m>>i)&1]
                X=forest(n,H+[e]); Y=forest(n,H+[f])
                S=forest(n,H+[e,f]); Q=X and Y and not S
                vals.append((m,X,Y,S,Q))
            x=Fraction(sum(v[1] for v in vals),N)
            y=Fraction(sum(v[2] for v in vals),N)
            r=Fraction(sum(v[3] for v in vals),N)
            q=Fraction(sum(v[4] for v in vals),N)
            exy=Fraction(sum(v[1] and v[2] for v in vals),N)
            c=exy-x*y; D=x*y-r
            if D != q-c: identity_fail+=1
            if c>0:
                pos_XY+=1
                if witness is None:
                    witness=(n,E,e,f,N,x,y,r,q,c,D)
            for gi,g in enumerate(E):
                if gi in (ei,fi): continue
                triples+=1
                k=B.index(g)
                R0=[v for v in vals if not ((v[0]>>k)&1)]
                R1=[v for v in vals if ((v[0]>>k)&1)]
                def st(R):
                    z=len(R)
                    xx=Fraction(sum(v[1] for v in R),z)
                    yy=Fraction(sum(v[2] for v in R),z)
                    rr=Fraction(sum(v[3] for v in R),z)
                    return xx,yy,rr,xx*yy-rr
                x0,y0,r0,D0=st(R0); x1,y1,r1,D1=st(R1)
                p=Fraction(len(R1),N)
                if D != (1-p)*D0+p*D1-p*(1-p)*(x1-x0)*(y1-y0):
                    identity_fail+=1
                if D1<0: neg_D1+=1
                t=p
                xt=Fraction(sum(v[1]*((v[0]>>k)&1) for v in vals),N)-x*t
                yt=Fraction(sum(v[2]*((v[0]>>k)&1) for v in vals),N)-y*t
                if xt>0: pos_Xg+=1
                if yt>0: pos_Yg+=1

                Ef=[h for j,h in enumerate(E) if j!=fi]
                MF=fmasks(n,Ef); Z=len(MF)
                ie,ig=Ef.index(e),Ef.index(g)
                pe=Fraction(sum((m>>ie)&1 for m in MF),Z)
                pg=Fraction(sum((m>>ig)&1 for m in MF),Z)
                peg=Fraction(sum(((m>>ie)&1)*((m>>ig)&1) for m in MF),Z)
                if peg-pe*pg != xt/(1+x)**2:
                    cov_extension_fail+=1

assert triples==46563
assert identity_fail==cov_extension_fail==pos_Xg==pos_Yg==neg_D1==0
print("triple_instances",triples)
print("identity_failures",identity_fail)
print("extension_identity_failures",cov_extension_fail)
print("positive_Cov_X_g",pos_Xg)
print("positive_Cov_Y_g",pos_Yg)
print("negative_D1",neg_D1)
print("positive_Cov_X_Y_cases",pos_XY)
print("first_overlap_witness",witness)
