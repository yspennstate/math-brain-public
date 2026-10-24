"""Research test of an iterated electrical-response H3 candidate.

NOT a proof: compares full forest coefficients with a putative wedge energy
of harmonic boundary cycle responses after H0,H1,H2 vanish.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from general_H2_mirror_stress_heat import forest_R,mm,inv_det


def candidate(n,unmarked,e,f,r=2,ce=F(1),cf=F(1)):
    edges=unmarked+[(e[0],e[1],ce),(f[0],f[1],cf)]
    L=[[F(0)for _ in range(n)]for _ in range(n)]
    for x,y,c in edges:
        L[x][x]+=c;L[y][y]+=c;L[x][y]-=c;L[y][x]-=c
    N=[x for x in range(n)if x!=r]
    K,tau=inv_det([[L[x][y]for y in N]for x in N])
    G=[[F(0)for _ in range(n)]for _ in range(n)]
    for i,x in enumerate(N):
        for j,y in enumerate(N):G[x][y]=K[i][j]
    v=[G[x][e[0]]-G[x][e[1]]for x in range(n)]
    w=[G[x][f[0]]-G[x][f[1]]for x in range(n)]
    assert v[f[0]]==v[f[1]]==w[e[0]]==w[e[1]]==0
    assert all(not(v[x]and w[x])for x in range(n))
    S=[x for x in range(n)if not v[x]and not w[x]];assert r in S
    B=[x for x in S if x!=r];U=[x for x in range(n)if x not in S]
    C,_=inv_det([[L[x][y]for y in U]for x in U])
    Pi=mm(C,[[-L[x][y]for y in B]for x in U])
    p=[[F(0)for _ in B]for x in range(n)]
    for i,x in enumerate(B):p[x][i]=1
    for i,x in enumerate(U):p[x]=Pi[i]
    T=[[G[x][y]for y in B]for x in B]
    def responses(z,pair):
        pi=p[pair[0]];assert pi==p[pair[1]]
        ans=[]
        for x,y,c in edges:
            eta=[z[x]*p[y][i]-z[y]*p[x][i]-(z[x]-z[y])*pi[i]for i in range(len(B))]
            if any(eta):
                zz=[sum((p[x][i]*T[i][j]*eta[j]for i in range(len(B))for j in range(len(B))),F(0))for x in range(n)]
                ans.append((c,eta,zz))
        return ans
    E=responses(v,e);Ff=responses(w,f)
    h2=F(0);h3=F(0)
    for a,eta,va in E:
        for b,theta,wb in Ff:
            ip=sum((eta[i]*T[i][j]*theta[j]for i in range(len(B))for j in range(len(B))),F(0))
            h2+=a*b*ip*ip
            # Suggested special constants: response potentials vanish on the
            # original opposite marked endpoints when all transfer terms zero.
            assert va[f[0]]==va[f[1]] and wb[e[0]]==wb[e[1]]
            va0=[x-va[f[0]]for x in va];wb0=[x-wb[e[0]]for x in wb]
            for x,y,c in edges:h3+=a*b*c*(va0[x]*wb0[y]-va0[y]*wb0[x])**2
    return tau*tau*h2,tau*tau*h3,tau


def chain(m):
    E={tuple(sorted((a,b)))for i in range(m-1)for a in [2*i,2*i+1,2*i+2,2*i+3]for b in [2*i,2*i+1,2*i+2,2*i+3]if a<b}
    e=(0,1);f=(2*m-2,2*m-1)
    return [(x,y,F(1))for x,y in sorted(E)if (x,y)not in[e,f]],e,f


def main():
    out=[]
    cases=[]
    for m in [4,5]:
        edges,e,f=chain(m);cases.append(('K4_chain_'+str(m),2*m,edges,e,f))
    for scales in [(1,1,1,1),(2,3,4,5),(F(1,2),F(2,3),F(3,4),F(4,5))]:
        alpha,beta,gamma,delta=map(F,scales)
        A=[2,3];C=[4,5];a=[F(1),F(4)];b=[F(2),F(3)]
        u=[F(2),F(3)];z=[F(1),F(5)]
        edges=[(0,x,alpha*q)for x,q in zip(A,a)]+[(1,x,beta*q)for x,q in zip(A,a)]
        edges +=[(6,x,gamma*q)for x,q in zip(C,b)]+[(7,x,delta*q)for x,q in zip(C,b)]
        edges +=[(x,y,u[i]*z[j])for i,x in enumerate(A)for j,y in enumerate(C)]
        edges +=[(2,3,F(7)),(4,5,F(11))]
        cases.append(('rank_one_four_boundary_'+str(scales),8,edges,(0,1),(6,7)))
    # Three vertices on one response interface; arbitrary internal core edges.
    A=[2,3,4];C=[5,6];a=[F(1),F(2),F(4)];b=[F(3),F(5)]
    u=[F(2),F(3),F(7)];z=[F(1),F(5)]
    edges=[(x,y,q)for x in [0,1]for y,q in zip(A,a)]
    edges +=[(x,y,q)for x in [7,8]for y,q in zip(C,b)]
    edges +=[(x,y,u[i]*z[j])for i,x in enumerate(A)for j,y in enumerate(C)]
    edges +=[(2,3,F(5)),(3,4,F(7)),(5,6,F(2))]
    cases.append(('rank_one_five_boundary',9,edges,(0,1),(7,8)))
    # Non-twin active support on e: two mirrored path interiors before A.
    A=[4,5];C=[6,7]
    edges=[(0,2,F(2)),(1,3,F(2)),(2,4,F(1)),(2,5,F(4)),(3,4,F(1)),(3,5,F(4)),
           (8,6,F(2)),(8,7,F(3)),(9,6,F(2)),(9,7,F(3)),
           (4,6,F(2)),(4,7,F(10)),(5,6,F(3)),(5,7,F(15)),(4,5,F(7)),(6,7,F(11))]
    cases.append(('non_twin_rank_one_core',10,edges,(0,1),(8,9)))
    for name,n,edges,e,f in cases:
        R=forest_R(n,edges,e,f);h2,h3,tau=candidate(n,edges,e,f,r=4 if name=='non_twin_rank_one_core'else 2)
        actual=R.get(2*n-7,F(0))
        item={'name':name,'n':n,'H2_candidate':str(h2),'H3_candidate':str(h3),'H3_actual':str(actual),'tau':str(tau),'match':h2==0 and h3==actual,
              'unmarked_edges':[(x,y,str(c))for x,y,c in edges],'marked_edges':[e,f],
              'R_coefficients':{str(k):str(c)for k,c in R.items()}}
        out.append(item);print(item,flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'unproved research candidate','cases':out},indent=2))


if __name__=='__main__':main()
