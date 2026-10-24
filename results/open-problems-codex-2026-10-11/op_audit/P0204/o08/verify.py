from fractions import Fraction as F
import json
import numpy as np

def upsets(n):
    if n==0:return [0,1]
    prev=upsets(n-1);s=1<<(n-1)
    return [a|(b<<s) for a in prev for b in prev if a&~b==0]

def solve(A,b):
    k=len(b);M=[list(A[i])+[b[i]] for i in range(k)]
    for i in range(k):
        j=next(j for j in range(i,k) if M[j][i]);M[i],M[j]=M[j],M[i]
        v=M[i][i];M[i]=[x/v for x in M[i]]
        for j in range(k):
            if j!=i:
                v=M[j][i]
                M[j]=[x-v*y for x,y in zip(M[j],M[i])]
    return [r[-1] for r in M]

out=[]
for n in range(2,6):
    rows={'n':n,'sets':0,'min_average_degree':None,'max_mixing_P':0,'max_mixing_Q':0,'exact_hitting_tests':0,'largest_mass_ratio':0.,'min_gap_difference':1.,'max_residual':0.}
    for mask in upsets(n):
        V=[x for x in range(1<<n) if mask>>x&1];m=len(V)
        if m<(1<<(n-1)):continue
        rows['sets']+=1
        adj=[[int((x^y).bit_count()==1) for y in V] for x in V]
        deg=[sum(r) for r in adj];D=sum(deg)
        assert D==2*sum(n-x.bit_count() for x in V)
        assert 2*D>=n*m
        av=F(D,m)
        rows['min_average_degree']=str(min(av,F(rows['min_average_degree']))) if rows['min_average_degree'] else str(av)
        pi=np.array(deg)/D;mu=np.ones(m)/m
        P=np.eye(m)*.5+np.array(adj)/(2*np.array(deg)[:,None]);Q=np.eye(m)-np.diag(deg)/(2*n)+np.array(adj)/(2*n)
        rows['largest_mass_ratio']=max(rows['largest_mass_ratio'],float(max(pi/mu)))
        residual=max(abs(pi@P-pi).max(),abs(mu@Q-mu).max(),abs(P.sum(axis=1)-1).max(),abs(Q.sum(axis=1)-1).max())
        rows['max_residual']=max(rows['max_residual'],float(residual))
        S=np.sqrt(pi)[:,None]*P/np.sqrt(pi)[None,:]
        gapP=1-np.linalg.eigvalsh(S)[-2];gapQ=1-np.linalg.eigvalsh(Q)[-2]
        assert gapP>=gapQ-1e-12
        rows['min_gap_difference']=min(rows['min_gap_difference'],float(gapP-gapQ))
        for K,stat,label in [(P,pi,'P'),(Q,mu,'Q')]:
            M=np.eye(m);t=0
            while np.abs(M-stat).sum(axis=1).max()/2>.25+1e-13:
                M=M@K;t+=1
                assert t<1000
            rows['max_mixing_'+label]=max(rows['max_mixing_'+label],t)
        if n<=3:
            for target in range(1,1<<m):
                U=[i for i in range(m) if not (target>>i&1)]
                if not U:continue
                AP=[[F(int(i==j),2)-F(adj[i][j],2*deg[i]) for j in U] for i in U]
                AQ=[[F(deg[i],2*n)*int(i==j)-F(adj[i][j],2*n) for j in U] for i in U]
                h=solve(AP,[F(1)]*len(U));g=solve(AQ,[F(1)]*len(U))
                assert all(x<=y for x,y in zip(h,g))
                rows['exact_hitting_tests']+=len(U)
    out.append(rows)
print(json.dumps(out,indent=2))
open('verification_results.json','w',encoding='utf8').write(json.dumps(out,indent=2))
