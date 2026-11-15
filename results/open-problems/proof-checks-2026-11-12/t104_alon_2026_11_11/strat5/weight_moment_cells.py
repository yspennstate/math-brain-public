"""Rational rectangle certificates from two nonnegative edge sums.

Numerical linear programs choose multipliers. Every retained rectangle is
subsequently checked using exact rational quadratic minimization.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import contextlib,json,itertools
with open('moment_region.out','a') as log, contextlib.redirect_stdout(log):
    import moment_region as mr
import numpy as np
import sympy as s
from scipy.optimize import linprog
aa,rr=s.symbols('a r')
verts=mr.vertices

def expr(v,theta_n,theta_j,tangent):
    A,B,C=v
    fm=A+rr*B+(1+rr)*C
    kk=A+B+2*C
    lam=(2+aa*(1+rr))/4
    l,h=mr.lh(v,False)
    base=l.subs(mr.r,rr)+aa*h.subs(mr.r,rr)
    zn=aa*(2*tangent*fm-(1+rr)*tangent*tangent)-lam*(2-kk)/5
    zj=aa*(2*tangent*fm-(1+rr)*tangent*tangent)-lam*(4-kk)/5
    return s.Poly(s.expand(base+theta_n*zn+theta_j*zj),aa,rr)

def choose(a0,r0,rlo=None):
    rlo=r0 if rlo is None else rlo
    best=None
    for tangent in [s.Rational(k,80) for k in range(24,61)]:
        rows=[]
        rhs=[]
        for ax in (float(s.Rational(4,11)),float(a0)):
            for v in verts:
                A,B,C=map(float,v)
                rx,tx=float(r0),float(tangent)
                fm=A+rx*B+(1+rx)*C
                kk=A+B+2*C
                f=fm-(1+rx)/5
                z=14/9*f+ax*(2*(1+rx)*f/9+4/3*(1+rx*rx)-14/3*(A+rx*rx*B)-4*(1+rx*rx+rx/3)*C)
                common=ax*(2*tx*fm-(1+rx)*tx*tx)
                lam=(2+ax*(1+rx))/4
                zn=common-lam*(2-kk)/5
                zj=common-lam*(4-kk)/5
                rows.append([-zn,-zj,1])
                rhs.append(z)
        sol=linprog([0.,0.,-1.],A_ub=rows,b_ub=rhs,
                    bounds=[(0,max(0.,5*float(rlo)/3-1)),(0,1+float(rlo)),(None,None)],method='highs',options={'threads':1})
        if sol.success and (best is None or sol.x[2]>best[0]):
            tn=s.Rational(max(0,int(np.floor(sol.x[0]*1000000))),1000000)
            tj=s.Rational(max(0,int(np.floor(sol.x[1]*1000000))),1000000)
            best=(sol.x[2],tn,tj,tangent)
    return best

def exact_min(poly,alo,ahi,rlo,rhi):
    values=[]
    assert poly.degree(aa)<=1 and poly.degree(rr)<=2
    for ax in (alo,ahi):
        pp=s.Poly(poly.as_expr().subs(aa,ax),rr)
        values.extend([pp.eval(rlo),pp.eval(rhi)])
        if pp.degree()==2 and pp.nth(2)>0:
            crit=-pp.nth(1)/(2*pp.nth(2))
            if rlo<=crit<=rhi:values.append(pp.eval(crit))
    return min(values)

if __name__=='__main__':
    for r0 in [s.Rational(3,5),s.Rational(7,10),s.Rational(4,5),s.Rational(9,10),1]:
        for a0 in [s.Rational(1,2),s.Rational(13,25),s.Rational(27,50)]:
            found=choose(a0,r0)
            print('NUMERICAL: point',a0,r0,'best supporting bound',found,flush=True)
    cells=[]
    # Adjacent ratio cells; certify from a=0 to each largest tested scale.
    for j in range(60,100):
        rlo,rhi=s.Rational(j,100),s.Rational(j+1,100)
        winner=None
        low,high=88,111
        while low+1<high:
            k=(low+high)//2
            ahi=s.Rational(k,200)
            chosen=choose(ahi,(rlo+rhi)/2,rlo)
            _,tn,tj,tan=chosen
            assert 0<=tn<=5*rlo/3-1 and 0<=tj<=1+rlo
            margin=min(exact_min(expr(v,tn,tj,tan),s.Rational(4,11),ahi,rlo,rhi) for v in verts)
            if margin>=0:
                winner=dict(rlo=str(rlo),rhi=str(rhi),alo='4/11',ahi=str(ahi),theta_n=str(tn),theta_j=str(tj),tangent=str(tan),margin=str(margin))
                low=k
            else:high=k
        if winner:
            cells.append(winner)
            print('PROVED: cell',winner,flush=True)
    with open('weight_moment_cells.json','w') as out:json.dump(cells,out,indent=2)
