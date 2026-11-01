"""Exact symbolic verification of the seven-polynomial analytic certificate.

The identity holds as an equality of polynomials in x,y,z,u,v. It does not
test only numerical values. All displayed coefficient polynomials are
checked against their explicitly specified integer numerators.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json

N=5
def C(value):return {(0,)*N:F(value)} if value else {}
def V(index):
    key=[0]*N;key[index]=1
    return {tuple(key):F(1)}
def add(*polys):
    result=defaultdict(F)
    for poly in polys:
        for key,value in poly.items():result[key]+=value
    return {key:value for key,value in result.items() if value}
def scale(poly,value):return {key:c*value for key,c in poly.items() if c*value}
def mul(*polys):
    result=C(1)
    for poly in polys:
        out=defaultdict(F)
        for key,value in result.items():
            for other,coefficient in poly.items():out[tuple(a+b for a,b in zip(key,other))]+=value*coefficient
        result={key:value for key,value in out.items() if value}
    return result
def pow(poly,n):return mul(*([poly]*n))
x,y,z,u,v=map(V,range(N));s=add(x,z);t=mul(x,z)
M=scale(u,F(1,2));J=scale(mul(u,v),F(1,18));one=C(1)


# The key is (s-degree,t-degree,y-degree), followed by positive numerator.
NUMERATORS={
 '00':(1,{(0,0,0):1,(1,0,0):1,(0,1,0):1}),
 '10':(4,{(0,0,0):2,(1,0,0):3,(2,0,0):2,(1,1,0):2,
           (0,0,1):2,(1,0,1):2,(0,1,1):2}),
 '11':(72,{(0,0,0):36,(1,0,0):51,(2,0,0):34,(1,1,0):30,(3,0,0):2,(2,1,0):2,
            (0,0,1):30,(1,0,1):34,(2,0,1):4,(0,1,1):30,(1,1,1):4,
            (1,0,2):2,(0,1,2):2}),
 '12':(18,{(0,0,0):9,(1,0,0):12,(2,0,0):8,(1,1,0):6,(3,0,0):1,(2,1,0):1,
            (0,0,1):6,(1,0,1):8,(2,0,1):2,(0,1,1):6,(1,1,1):2,
            (1,0,2):1,(0,1,2):1}),
 '20':(4,{(1,0,0):2,(2,0,0):2,(3,0,0):1,(2,1,0):1,
           (0,0,1):4,(1,0,1):4,(2,0,1):2,(1,1,1):2,
           (0,0,2):2,(1,0,2):1,(0,1,2):1}),
 '21':(72,{(1,0,0):30,(2,0,0):32,(3,0,0):17,(4,0,0):2,(2,1,0):12,(3,1,0):2,
            (0,0,1):60,(1,0,1):68,(2,0,1):38,(3,0,1):6,(1,1,1):24,(2,1,1):6,
            (0,0,2):36,(1,0,2):25,(2,0,2):6,(0,1,2):12,(1,1,2):6,
            (0,0,3):4,(1,0,3):2,(0,1,3):2}),
 '22':(324,{(1,0,0):108,(2,0,0):126,(3,0,0):72,(4,0,0):15,(5,0,0):1,
             (2,1,0):36,(3,1,0):12,(4,1,0):1,
             (0,0,1):216,(1,0,1):288,(2,0,1):180,(3,0,1):48,(4,0,1):4,
             (1,1,1):72,(2,1,1):36,(3,1,1):4,
             (0,0,2):162,(1,0,2):144,(2,0,2):54,(3,0,2):6,
             (0,1,2):36,(1,1,2):36,(2,1,2):6,
             (0,0,3):36,(1,0,3):24,(2,0,3):4,(0,1,3):12,(1,1,3):4,
             (0,0,4):3,(1,0,4):1,(0,1,4):1}),
}


def clusters(groups):
    ds=[add(one,a) for a in groups]
    answer=mul(*ds)
    for i,a in enumerate(groups):
        rest=[ds[j] for j in range(len(groups)) if j!=i]
        answer=add(answer,mul(M,a,a,*rest),mul(J,a,a,a,*rest))
        for j in range(i):
            rest=[ds[k] for k in range(len(groups)) if k not in (i,j)]
            answer=add(answer,scale(mul(J,a,a,groups[j],groups[j],*rest),2))
    return answer
def bernstein(poly):
    complement=add(one,scale(poly,-1))
    return [pow(complement,2),scale(mul(poly,complement),2),pow(poly,2)]
def main():
    Q={}
    for label,(denominator,coefficients) in NUMERATORS.items():
        assert denominator>0 and all(value>0 for value in coefficients.values())
        Q[label]=add(*(scale(mul(pow(s,i),pow(t,j),pow(y,k)),F(value,denominator))
                       for (i,j,k),value in coefficients.items()))
    Q['01']=Q['02']=Q['00']
    A=clusters([x,y,z]);E=clusters([add(x,y),z]);Ff=clusters([x,add(y,z)]);EF=clusters([add(x,y,z)])
    exact=add(mul(E,Ff),scale(mul(A,EF),-1))
    bu,bv=bernstein(u),bernstein(v)
    positive=mul(x,z,add(*(mul(bu[i],bv[j],Q[str(i)+str(j)])for i in range(3)for j in range(3))))
    assert exact==positive
    results={'arithmetic':'exact Fraction polynomial identity in x,y,z,u,v',
             'identity_nonzero_monomials':len(exact),'seven_positive_polynomials':{
                 label:{'denominator':den,'positive_terms':len(coeffs),'minimum_numerator':min(coeffs.values())}
                 for label,(den,coeffs) in NUMERATORS.items()},
             'coefficientwise_identity_exact':True,'strictness_source':'(1-u)^2 Q00; Q00=1+s+t>0'}
    Path(__file__).with_name('forest_adjacent_terminal_core3_bernstein_exact_results.json').write_text(json.dumps(results,indent=2)+'\n')
    print('Exact seven-polynomial Bernstein identity PASS.',flush=True)
if __name__=='__main__':main()
