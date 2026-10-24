from fractions import Fraction as F
from math import ceil, log, sqrt
import json

counts={}
def count(k,n=1): counts[k]=counts.get(k,0)+n
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(A,x): return [dot(row,x) for row in A]
def mm(A,B): return [[dot(row,col) for col in zip(*B)] for row in A]
def ident(p): return [[F(i==j) for j in range(p)] for i in range(p)]
def inv(A):
    p=len(A); M=[row[:]+I for row,I in zip(A,ident(p))]
    for j in range(p):
        k=next(k for k in range(j,p) if M[k][j]); M[k],M[j]=M[j],M[k]
        q=M[j][j]; M[j]=[x/q for x in M[j]]
        for k in range(p):
            if k!=j:
                q=M[k][j]; M[k]=[x-q*y for x,y in zip(M[k],M[j])]
    return [row[p:] for row in M]
def lin(row,h): return sum(v*h[k] for k,v in row.items())
def mlp(tokens,units,D,H):
    assert len(units)<=H; count('hidden_width_checks')
    ans=[h[:] for h in tokens]
    for i,h in enumerate(tokens):
        for row,col in units:
            a=max(F(0),lin(row,h))
            for k,v in col.items(): ans[i][k]+=v*a
    assert all(len(h)==D for h in ans)
    return ans
def attn(tokens,heads,D):
    assert len(heads)<=5; count('head_count_checks')
    ans=[h[:] for h in tokens]; N=len(tokens)
    for Q,K,V in heads:
        qs=[[lin(row,h) for row in Q] for h in tokens]
        ks=[[lin(row,h) for row in K] for h in tokens]
        vs=[{k:lin(row,h) for k,row in V.items()} for h in tokens]
        for i in range(N):
            for j in range(N):
                a=max(F(0),dot(qs[i],ks[j]))/N
                for k,v in vs[j].items(): ans[i][k]+=a*v
    assert all(len(h)==D for h in ans)
    return ans
def neg(rows): return [{k:-v for k,v in r.items()} for r in rows]

for p in (1,2,3):
 for J in (1,3,5):
  for n,t in ((0,0),(1,0),(1,1),(3,1),(3,3)):
    d=2; N=n+1; S=F(2); s=F(1,2); B=F(1); eps=F(1,2)
    D=7*p+6+d+J*d+p*J; H=2*J*d+p*J+4*p+1
    zc=0; zq=p; qb=2*p; w=3*p; u=4*p; wo=5*p; uo=6*p
    yi=7*p; one=yi+1; mout=yi+2; vout=yi+3; raw=yi+4; rc=raw+d; rq=rc+1; ab=rq+1; co=ab+J*d
    centers=[[F(2)+F(a,4),F(3)+F((a*2)%5,5)] for a in range(J)]
    vals=[[F(((a+2)*(j+3))%7-3,6) for a in range(J)] for j in range(p)]
    role_indices=[j%J for j in range(t)]+[(J-1)%J]+[0]*(n-t)
    labels=[F((-1)**j,2) for j in range(t)]+[F(0)]*(N-t)
    tokens=[]
    for i,a in enumerate(role_indices):
        h=[F(0)]*D; h[raw:raw+d]=centers[a]; h[one]=1; h[vout]=s; h[yi]=labels[i]
        h[rc]=F(i<t); h[rq]=F(i==t); tokens.append(h)
    original=[h[:] for h in tokens]; layer_count=0
    units=[]
    for a in range(J):
      for r in range(d):
        units.extend([({raw+r:F(1),one:-centers[a][r]},{ab+a*d+r:F(1)}),({raw+r:F(-1),one:centers[a][r]},{ab+a*d+r:F(1)})])
    tokens=mlp(tokens,units,D,H); layer_count+=1
    units=[({ab+a*d+r:F(1)},{co+j*J+a:F(1) for j in range(p)}) for a in range(J) for r in range(d)]
    units.append(({one:F(1)},{co+j*J+a:vals[j][a] for j in range(p) for a in range(J)}))
    tokens=mlp(tokens,units,D,H); layer_count+=1
    alive=list(range(J))
    while len(alive)>1:
        units=[]; new=[]
        for k in range(0,len(alive),2):
            a=alive[k]; new.append(a)
            if k+1<len(alive):
                b=alive[k+1]
                units += [({co+j*J+a:F(1),co+j*J+b:F(-1)},{co+j*J+a:F(-1)}) for j in range(p)]
        tokens=mlp(tokens,units,D,H); layer_count+=1; alive=new
    units=[]
    for j in range(p):
      for role,out in ((rc,zc+j),(rq,zq+j)):
        units.extend([({co+j*J:F(1),role:S,one:-S},{out:F(1)}),({co+j*J:F(-1),role:S,one:-S},{out:F(-1)})])
    tokens=mlp(tokens,units,D,H); layer_count+=1
    fs=[]
    for i,a in enumerate(role_indices):
        f=[min(vals[j][b]+sum(abs(centers[a][r]-centers[b][r]) for r in range(d)) for b in range(J)) for j in range(p)]; fs.append(f)
        assert tokens[i][zc:zc+p]==[x*original[i][rc] for x in f]
        assert tokens[i][zq:zq+p]==[x*original[i][rq] for x in f]
        for k in list(range(raw,rc))+[yi,one,vout,rc,rq]: assert tokens[i][k]==original[i][k]
        count('encoder_tokens_checked')
    assert layer_count==3+ceil(log(J,2)); count('encoder_layer_count')
    const=[{one:F(1)}]
    tokens=attn(tokens,[(const,const,{qb+j:{zq+j:F(N)} for j in range(p)})],D); layer_count+=1
    q=fs[t]; A=[[s*F(i==j)+sum(fs[k][i]*fs[k][j] for k in range(t)) for j in range(p)] for i in range(p)]; f=[sum(fs[k][j]*labels[k] for k in range(t)) for j in range(p)]
    L=s+max(1,n)*S*S; c=(L+s)/2; dd=(L-s)/2; alpha=c/dd
    kappa=float(L/s); M=n*S*S*B/s; eps0=min(eps/4,F(1,16))
    delta=min(.5,float(s/(2*S*S)),sqrt(float(s*eps0))/float(1+M),float(s)*sqrt(float(eps0))/float(S*S))
    T=ceil(sqrt(kappa)*log(2/delta)/2)
    chev=[F(1),alpha]
    while len(chev)<=T: chev.append(2*alpha*chev[-1]-chev[-2])
    wd=[F(0)]*p; ud=wd[:]; wp=wd[:]; up=wd[:]
    for step in range(T):
        eta=1/c if step==0 else 2*chev[step]/(dd*chev[step+1]); beta=F(0) if step==0 else chev[step-1]/chev[step+1]
        q1=[{w+j:F(1)} for j in range(p)]+[{one:F(1)}]; k1=[{zc+j:F(-1)} for j in range(p)]+[{yi:F(1)}]
        q3=[{u+j:F(1)} for j in range(p)]; k3=[{zc+j:F(1)} for j in range(p)]
        V5={}
        for j in range(p):
            V5[w+j]={w+j:beta-eta*s,wo+j:-beta}; V5[u+j]={u+j:beta-eta*s,uo+j:-beta,qb+j:eta}
            V5[wo+j]={w+j:F(1),wo+j:F(-1)}; V5[uo+j]={u+j:F(1),uo+j:F(-1)}
        heads=[(q1,k1,{w+j:{zc+j:N*eta} for j in range(p)}),(neg(q1),k1,{w+j:{zc+j:-N*eta} for j in range(p)}),(q3,k3,{u+j:{zc+j:-N*eta} for j in range(p)}),(neg(q3),k3,{u+j:{zc+j:N*eta} for j in range(p)}),(const,const,V5)]
        tokens=attn(tokens,heads,D); layer_count+=1
        wn=[wd[j]+beta*(wd[j]-wp[j])+eta*(f[j]-mv(A,wd)[j]) for j in range(p)]; un=[ud[j]+beta*(ud[j]-up[j])+eta*(q[j]-mv(A,ud)[j]) for j in range(p)]
        wp,wd=wd,wn; up,ud=ud,un
        for h in tokens:
            assert h[w:w+p]==wd and h[u:u+p]==ud and h[wo:wo+p]==wp and h[uo:uo+p]==up and h[qb:qb+p]==q
            count('exact_attention_update_tokens')
    qr=[{qb+j:F(1)} for j in range(p)]; kw=[{w+j:F(1)} for j in range(p)]; ku=[{u+j:F(1)} for j in range(p)]
    tokens=attn(tokens,[(qr,kw,{mout:{one:F(1)}}),(neg(qr),kw,{mout:{one:F(-1)}}),(qr,ku,{vout:{one:s}}),(neg(qr),ku,{vout:{one:-s}})],D); layer_count+=1
    Ainv=inv(A); m=dot(q,mv(Ainv,f)); v=s+s*dot(q,mv(Ainv,q)); mh=dot(q,wd); vh=s+s*dot(q,ud)
    for h in tokens: assert h[mout]==mh and h[vout]==vh; count('exact_readout_tokens')
    assert vh>=s and abs(float(m-mh))<=sqrt(float(s*eps0))+1e-12 and abs(float(v-vh))<=float(s)*sqrt(float(eps0))+1e-12
    kl=.5*(log(float(vh/v))+float((v+(m-mh)**2)/vh)-1)
    assert kl<=float(eps0)+1e-12; count('posterior_error_and_KL_cases')
    assert layer_count==T+5+ceil(log(J,2)); count('total_layer_count')
    # Independently evaluate the Chebyshev matrix residual and check the full vector identity exactly.
    Z=[[(c*F(i==j)-A[i][j])/dd for j in range(p)] for i in range(p)]; C0=ident(p); C1=Z
    for j in range(1,T):
        ZC=mm(Z,C1); C0,C1=C1,[[2*ZC[a][b]-C0[a][b] for b in range(p)] for a in range(p)]
    CT=C0 if T==0 else C1
    for rhs,got in ((f,wd),(q,ud)):
        exact=mv(Ainv,rhs); residual=mv(CT,exact)
        assert all(exact[j]-got[j]==residual[j]/chev[T] for j in range(p)); count('exact_polynomial_residual')
for S in (F(1),F(7,3)):
 for f in (-S,-S/2,F(0),S/2,S):
  for r in (0,1):
    assert max(f+S*(r-1),0)-max(-f+S*(r-1),0)==r*f; count('gate_boundaries')
print(json.dumps({'status':'PASS','cases':45,'dimensions':{'p':[1,2,3],'d':2,'J':[1,3,5],'n_t':[[0,0],[1,0],[1,1],[3,1],[3,3]]},'checks':counts,'arithmetic':'Exact Fraction through all encoder/attention/residual identities; floating point only final error/KL comparisons with 1e-12 tolerance.'},indent=2))
