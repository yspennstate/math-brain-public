"""Exact example checks, not a proof of the unresolved fifth-moment bound."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def mm(A,B):
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]

def trace5(A):
    A2=mm(A,A); A4=mm(A2,A2)
    return sum((A4[i][j]*A[j][i] for i in range(len(A)) for j in range(len(A))),F(0))

def check(W,p):
    n=len(p); assert sum(p)==1 and all(x>0 for x in p)
    assert all(W[i][j]>=0 and W[i][j]==W[j][i] for i,j in product(range(n),repeat=2))
    assert all(sum(p[j]*W[i][j] for j in range(n))==1 for i in range(n))
    C={(i,j,k):sum(p[u]*W[u][i]*W[u][j]*W[u][k] for u in range(n))
       for i,j,k in product(range(n),repeat=3)}
    Q={(i,j):sum(p[k]*C[i,j,k] for k in range(n)) for i,j in product(range(n),repeat=2)}
    assert all(Q[i,j]==sum(p[u]*W[u][i]*W[u][j] for u in range(n)) for i,j in Q)
    E=[s for s in Q if Q[s]>0]; mu={s:p[s[0]]*p[s[1]]*Q[s] for s in E}
    assert sum(mu.values())==1
    P={};T=[]
    for i,j in E:
        row=[]
        for v,k in E:
            val=p[k]*C[i,j,k] if v==j else F(0)
            P[(i,j),(v,k)]=val/Q[i,j];row.append(val)
        T.append(row)
        assert sum(P[(i,j),s] for s in E)==1
    assert all(sum(mu[s]*P[s,t] for s in E)==mu[t] for t in E)
    direct=F(0)
    for z in product(range(n),repeat=5):
        val=F(1)
        for i in range(5):val*=p[z[i]]*C[z[i],z[(i+1)%5],z[(i+2)%5]]
        direct+=val
    assert trace5(T)==direct
    return {'n':n,'active_pairs':len(E),'density':str(direct),'identities_pass':True}

def main():
    records=[]
    records.append(check([[F(0),F(3,2)],[F(3,2),F(3,4)]],[F(1,3),F(2,3)]))
    records.append(check([[F(0),F(9,5),F(6,5)],[F(9,5),F(0),F(6,5)],
                          [F(6,5),F(6,5),F(3,5)]],[F(1,3)]*3))
    records.append(check([[F(1),F(1)],[F(1),F(1)]],[F(1,4),F(3,4)]))
    triangle=[[F(i!=j,2) for j in range(3)] for i in range(3)]
    warning=trace5(triangle);assert warning==F(15,16)
    out={'status':'ALL_EXACT_CHECKS_PASS','examples':records,'triangle_fifth_trace':str(warning),
         'full_Sidorenko_proof':False,'universal_residual_fifth_moment_proved':False,
         'scope':'Rational example identities only; spectral-radius proposition has a written analytic proof.'}
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_name('checks.json').write_text(text)
    print(text,end='')
if __name__=='__main__':main()
