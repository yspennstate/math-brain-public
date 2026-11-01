"""Unproved iterative-response hypothesis, exact numerical stress test.

At each stage compare the predicted even trace/odd wedge coefficient to exact
forest Rayleigh coefficients. This is research evidence, never a proof.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from general_H2_mirror_stress_heat import mm,inv_det
from forest_frontier_dp_heat import forest_R_dp
from H3_response_wedge_heat import chain


def grounded(L,r):
    n=len(L);N=[x for x in range(n)if x!=r]
    K,tau=inv_det([[L[x][y]for y in N]for x in N])
    G=[[F(0)for _ in range(n)]for _ in range(n)]
    for i,x in enumerate(N):
        for j,y in enumerate(N):G[x][y]=K[i][j]
    return G,tau


def harmonic(L,S,r):
    n=len(L);B=[x for x in S if x!=r];U=[x for x in range(n)if x not in S]
    C,_=inv_det([[L[x][y]for y in U]for x in U])
    inside=mm(C,[[-L[x][y]for y in B]for x in U])if B else [[]for x in U]
    p=[[F(0)for x in B]for y in range(n)]
    for i,x in enumerate(B):p[x][i]=1
    for i,x in enumerate(U):p[x]=inside[i]
    G,tau=grounded(L,r);T=[[G[x][y]for y in B]for x in B]
    return p,T,tau,B


def response_channels(edges,current,p,pi,weight=F(1)):
    ans=[]
    for x,y,c in edges:
        eta=[current[x]*p[y][i]-current[y]*p[x][i]-(current[x]-current[y])*pi[i]for i in range(len(pi))]
        if any(eta):ans.append((weight*c,eta))
    return ans


def port_set(edges,region):return sorted({y if x in region else x for x,y,c in edges if (x in region)!=(y in region)})


def gram(channels,size):
    B=[[F(0)for _ in range(size)]for _ in range(size)]
    for c,z in channels:
        for i in range(size):
            for j in range(size):B[i][j]+=c*z[i]*z[j]
    return B


def rank(A):
    M=[row[:]for row in A];m=len(M);n=len(M[0])if m else 0;rr=0
    for j in range(n):
        piv=next((i for i in range(rr,m)if M[i][j]),None)
        if piv is None:continue
        M[rr],M[piv]=M[piv],M[rr];z=M[rr][j];M[rr]=[v/z for v in M[rr]]
        for i in range(m):
            if i!=rr and M[i][j]:
                z=M[i][j];M[i]=[a-z*b for a,b in zip(M[i],M[rr])]
        rr+=1
    return rr


def research_iterate(n,unmarked,e,f,maxstage=5):
    edges=unmarked+[(e[0],e[1],F(1)),(f[0],f[1],F(1))]
    L=[[F(0)for _ in range(n)]for _ in range(n)]
    for x,y,c in edges:
        L[x][x]+=c;L[y][y]+=c;L[x][y]-=c;L[y][x]-=c
    # Find an original equality-compatible root; reject other cases.
    for r in range(n):
        G,tau=grounded(L,r)
        v=[G[x][e[0]]-G[x][e[1]]for x in range(n)]
        w=[G[x][f[0]]-G[x][f[1]]for x in range(n)]
        if v[f[0]]==v[f[1]]==w[e[0]]==w[e[1]]==0 and all(not(v[x]and w[x])for x in range(n)):break
    else:raise ValueError('outside original H0=H1=0 geometry')
    E={x for x in range(n)if v[x]};Ff={x for x in range(n)if w[x]}
    S=sorted(set(range(n))-E-Ff)
    p,T,tau,B=harmonic(L,S,r)
    Ce=response_channels(edges,v,p,p[e[0]])
    Cf=response_channels(edges,w,p,p[f[0]])
    out=[]
    for level in range(1,maxstage+1):
        A=port_set(edges,E);C=port_set(edges,Ff)
        Be=gram(Ce,len(B));Bf=gram(Cf,len(B))
        fullrange=(rank(Be)==len(A)-1 and rank(Bf)==len(C)-1)
        even=F(0);odd=F(0);ae=[];bf=[]
        def potentials(channels,other):
            values=[]
            for c,z in channels:
                a=[sum((p[x][i]*T[i][j]*z[j]for i in range(len(B))for j in range(len(B))),F(0))for x in range(n)]
                assert all(a[x]==a[other[0]]for x in other)
                a=[x-a[other[0]]for x in a]
                values.append((c,a))
            return values
        # Only if the even trace is zero may opposite port constants be used.
        for c,z in Ce:
            for d,zz in Cf:
                ip=sum((z[i]*T[i][j]*zz[j]for i in range(len(B))for j in range(len(B))),F(0))
                even+=c*d*ip*ip
        item={'level':level,'even_index':2*level,'even_prediction':str(tau*tau*even),
              'E':sorted(E),'F':sorted(Ff),'S':S,'ports_e':A,'ports_f':C,
              'response_rank_e':rank(Be),'response_rank_f':rank(Bf),'full_contrast_range':fullrange}
        if even:
            out.append(item);break
        if not Ce or not Cf:
            item['block_independence_prediction']=True;out.append(item);break
        ae=potentials(Ce,C);bf=potentials(Cf,A)
        for c,a in ae:
            for d,b in bf:
                for x,y,cc in edges:odd+=c*d*cc*(a[x]*b[y]-a[y]*b[x])**2
        item.update({'odd_index':2*level+1,'odd_prediction':str(tau*tau*odd)})
        out.append(item)
        if odd:break
        Enew=E|{x for c,a in ae for x in range(n)if a[x]}
        Fnew=Ff|{x for c,b in bf for x in range(n)if b[x]}
        assert not(Enew&Fnew)
        assert all(not(x in Enew and y in Fnew)and not(y in Enew and x in Fnew)for x,y,c in edges)
        Snew=sorted(set(range(n))-Enew-Fnew);rnew=Snew[0]
        pn,Tn,taun,Bn=harmonic(L,Snew,rnew);assert taun==tau
        pie=pn[A[0]];pif=pn[C[0]]
        assert all(pn[x]==pie for x in A)and all(pn[x]==pif for x in C)
        Ceen=[];Cffn=[]
        for c,a in ae:Ceen+=response_channels(edges,a,pn,pie,c)
        for c,b in bf:Cffn+=response_channels(edges,b,pn,pif,c)
        E,Ff,S,r,p,T,B,Ce,Cf=Enew,Fnew,Snew,rnew,pn,Tn,Bn,Ceen,Cffn
    return out


def main():
    result=[]
    cases=[]
    for m in [5,6,7]:
        edges,e,f=chain(m);cases.append(('K4_chain_'+str(m),2*m,edges,e,f))
    # Positive-offdiagonal E response, three-port middle interface, and
    # asymmetric rank-one layers. This tests the next Gram beyond twin sides.
    rows={0:[3,30,1],1:[2,28,2],2:[15,14,3],3:[5,2,4]}
    raw=[(0,2,4),(1,2,14)]+[(2,4+i,c)for i,c in enumerate(rows[2])]
    raw +=[(0,3,12),(1,3,2)]+[(3,4+i,c)for i,c in enumerate(rows[3])]
    raw +=[(x,4+i,c)for x in [0,1]for i,c in enumerate(rows[x])]
    raw +=[(4,5,3),(5,6,2)]
    raw +=[(4+i,7+j,a*b)for i,a in enumerate([2,3,7])for j,b in enumerate([1,4,5])]
    raw +=[(7,8,5),(8,9,2)]
    raw +=[(x,10,3)for x in [12,13]]+[(x,11,5)for x in [12,13]]
    raw +=[(7+i,10+j,a*b)for i,a in enumerate([3,2,6])for j,b in enumerate([2,3])]
    raw +=[(10,11,4)]
    cases.append(('positive_offdiag_three_port_middle',14,[(x,y,F(c))for x,y,c in raw],(0,1),(12,13)))
    for name,n,edges,e,f in cases:
        R=forest_R_dp(n,edges,e,f)
        stages=research_iterate(n,edges,e,f,maxstage=5)
        for s in stages:
            for parity in ['even','odd']:
                if parity+'_index'not in s:continue
                idx=s[parity+'_index'];actual=R.get(2*n-4-idx,F(0))
                predicted=F(s[parity+'_prediction'])
                s[parity+'_actual']=str(actual);s[parity+'_matches']=actual==predicted
        item={'name':name,'n':n,'stages':stages,'R_coefficients':{str(k):str(v)for k,v in R.items()},
              'unmarked_edges':[(x,y,str(c))for x,y,c in edges],'marked_edges':[e,f]}
        result.append(item);print(json.dumps(item,indent=2),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'unproved recursion hypothesis','cases':result},indent=2))


if __name__=='__main__':main()
