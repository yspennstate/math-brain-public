import math, random, json

def inv(a):
    n=len(a); z=[list(a[i])+[float(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(z[i][k])); z[k],z[p]=z[p],z[k]
        d=z[k][k]
        if abs(d)<1e-25: raise ValueError('singular')
        z[k]=[x/d for x in z[k]]
        for i in range(n):
            if i!=k:
                d=z[i][k]; z[i]=[x-d*y for x,y in zip(z[i],z[k])]
    return [r[n:] for r in z]

def eig(a):
    n=len(a); a=[r[:] for r in a]
    for _ in range(300):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-12: break
        theta=.5*math.atan2(2*a[p][q],a[q][q]-a[p][p]); c=math.cos(theta); s=math.sin(theta)
        pp,qq,pq=a[p][p],a[q][q],a[p][q]
        for k in range(n):
            if k not in (p,q):
                kp,kq=a[k][p],a[k][q]; a[k][p]=a[p][k]=c*kp-s*kq; a[k][q]=a[q][k]=s*kp+c*kq
        a[p][p]=c*c*pp+s*s*qq-2*c*s*pq; a[q][q]=s*s*pp+c*c*qq+2*c*s*pq; a[p][q]=a[q][p]=0
    return sorted(a[i][i] for i in range(n))

def state(rhos,diag):
    x,y,z=rhos
    co=(x*y+x*z+y*z-x*y*z)/(2*math.sqrt(x*y*z))
    if co>1: return None
    phase=complex(co,math.sqrt(max(0,1-co*co)))
    L=[[0j]*3 for _ in range(3)]
    for i in range(3): L[i][i]=diag[i]
    for (i,j),r,v in zip([(0,1),(1,2),(2,0)],rhos,[1,1,phase]):
        L[i][j]=math.sqrt(r*diag[i]*diag[j])*v; L[j][i]=L[i][j].conjugate()
    J=inv([[L[i][j]+float(i==j) for j in range(3)] for i in range(3)])
    K=[[float(i==j)-J[i][j] for j in range(3)] for i in range(3)]
    cov=[[K[i][i].real*(1-K[i][i].real) if i==j else -abs(K[i][j])**2 for j in range(3)] for i in range(3)]
    C=inv(cov)
    for (i,j),r in zip([(0,1),(1,2),(2,0)],rhos): C[i][j]+=math.log1p(-r); C[j][i]+=math.log1p(-r)
    return eig(C),K,C

def main():
    rng=random.Random(130013); minimum=(float('inf'),None); fail=None; accepted=0
    for _ in range(30000):
        rhos=[1-math.exp(-10**rng.uniform(-3,2)) for i in range(3)]
        if min(rhos)<=0 or max(rhos)>=1:continue
        diag=[10**rng.uniform(-5,5) for i in range(3)]
        try: s=state(rhos,diag)
        except (ValueError,ZeroDivisionError): continue
        if s is None: continue
        accepted+=1
        if s[0][0]<minimum[0]:minimum=(s[0][0],{'rhos':rhos,'diag':diag,'eig':s[0]})
        if s[0][0]<-1e-6:fail=minimum;break
    print(json.dumps({'accepted':accepted,'minimum':minimum,'failure':fail},indent=2))

if __name__=='__main__':main()
