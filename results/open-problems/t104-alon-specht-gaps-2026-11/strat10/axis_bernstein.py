"""PROVED: exact one-coordinate Bernstein bounds with rational replay.

Convert the normalized centered variable in one coordinate from [-1,1]
to a Bernstein basis on [0,1]. Each control remains a polynomial in five
variables. Bound those five variables by exact signed monomial ranges.
"""
from fractions import Fraction as F
from math import comb,lcm
from functools import lru_cache
from centered_bounds import translate


@lru_cache(None)
def conversion(n):
    scale=lcm(*(comb(n,j)for j in range(n+1)))
    coeff=[]
    for k in range(n+1):
        row=[]
        for i in range(n+1):
            val=sum(F(comb(k,j)*2**j*(-1)**(k-j)*comb(i,j),comb(n,j))for j in range(min(i,k)+1))
            assert (val*scale).denominator==1
            row.append(int(val*scale))
        coeff.append(row)
    return scale,coeff


def analysis(poly,box):
    centers=[(F(l)+F(h))/2 for l,h in box]
    widths=[(F(h)-F(l))/2 for l,h in box]
    scale=lcm(*(x.denominator for x in centers+widths))
    tr,d=translate(poly,[int(x*scale)for x in centers],scale)
    powers=[[int(x*scale)**k for k in range(9)]for x in widths]
    normal={}
    for mon,a in tr.items():
        val=a
        for i,m in enumerate(mon):val*=powers[i][m]
        if val:normal[mon]=val
    impacts=[sum(abs(a)*mon[i]for mon,a in normal.items())for i in range(6)]
    return normal,scale**d,impacts


def bound_normal(normal,denominator,axis):
    n=max(mon[axis]for mon in normal)
    scale,conv=conversion(n)
    groups={}
    for mon,a in normal.items():
        key=mon[:axis]+mon[axis+1:]
        if key not in groups:groups[key]=[0]*(n+1)
        groups[key][mon[axis]]=a
    lowers=[0]*(n+1)
    for mon,coeff in groups.items():
        constants=not any(mon);odd=any(m%2 for m in mon)
        for i in range(n+1):
            val=sum(a*conv[k][i]for k,a in enumerate(coeff)if a)
            if constants:lowers[i]+=val
            elif odd:lowers[i]-=abs(val)
            elif val<0:lowers[i]+=val
    controls=[F(x,scale*denominator)for x in lowers]
    return min(controls),controls


def box_bound(poly,box,axis):
    normal,denominator,impact=analysis(poly,box)
    return bound_normal(normal,denominator,axis)


def replay_conversion():
    """Exact identity certificate for every conversion degree used here."""
    import sympy as s
    z=s.symbols('z')
    for n in range(7):
        scale,matrix=conversion(n)
        for k in range(n+1):
            recon=sum(s.Rational(matrix[k][i],scale)*comb(n,i)*z**i*(1-z)**(n-i)for i in range(n+1))
            assert s.expand(recon-(2*z-1)**k)==0
    print('PROVED: all 28 monomial-to-Bernstein conversion identities through degree six replayed.')

if __name__=='__main__':replay_conversion()
