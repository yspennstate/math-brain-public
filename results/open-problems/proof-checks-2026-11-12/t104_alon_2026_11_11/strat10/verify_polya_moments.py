"""PROVED: exact coefficient-matrix replay of eight new frame inequalities.

No numerical solver, eigenvalue tolerance, or stored Gram matrix is used.
"""
import json
from fractions import Fraction as F
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


def main():
    rr,*g=ring('z0,z1,z2,z3,x0,x1,x2',QQ)
    z,x=g[:4],g[4:]
    U=[sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)]
    delta=U[0]-U[4]
    W=[sum((U[4]-U[j+1])*x[j] for j in range(3))]
    W += [delta*x[j] for j in range(3)]
    W += [sum((U[j+1]-U[0])*x[j] for j in range(3))]
    assert sum(U)==sum(W)==sum(a*b for a,b in zip(U,W))==0
    t,n=sum(v*v for v in U),sum(v*v for v in W)
    A,C=sum(v**4 for v in U),sum(a*a*b*b for a,b in zip(U,W))
    total=0
    for filename,sign in [('polya_upper_bounds.json',-1),('polya_lower_bounds.json',1)]:
        for rec in json.load(open(filename)):
            k,bound=F(rec['k']),F(rec['bound'])
            exponent=rec['power']
            assert k>=0 and bound>0 and isinstance(exponent,int) and exponent>=0
            poly=QQ(bound.numerator,bound.denominator)*t*t*n
            poly-=QQ(k.numerator,k.denominator)*A*n
            poly+=sign*t*C
            poly*=sum(z)**exponent
            matrices={}
            for mon,c in poly.terms():
                assert sum(mon[:4])==6+exponent and sum(mon[4:])==2
                mat=matrices.setdefault(mon[:4],[[F(0)]*3 for _ in range(3)])
                ids=[i for i in range(3) for _ in range(mon[4+i])]
                i,j=ids
                value=F(int(c.numerator),int(c.denominator))
                mat[i][j]+=value*(2 if i==j else 1)
                if i!=j:
                    mat[j][i]+=value
            for mat in matrices.values():
                a,b,c=mat[0]
                _,d,e=mat[1]
                _,_,f=mat[2]
                minors=(a,d,f,a*d-b*b,a*f-c*c,d*f-e*e,
                        a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
                assert min(minors)>=0
            total+=len(matrices)
            print('PROVED:',str(k)+' A '+('+' if sign<0 else '-')+' C <= '+str(bound),
                  'and its u/w swap; power',exponent,'PSD matrices',len(matrices))
    print('PROVED:',total,'coefficient matrices and all seven principal minors checked exactly.')


if __name__=='__main__':
    main()
