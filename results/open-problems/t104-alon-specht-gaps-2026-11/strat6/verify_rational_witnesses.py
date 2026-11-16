"""PROVED: independent finite replay of new zero-edge endpoint witnesses."""
import json
from fractions import Fraction as F
from moment_bounds import value,vertices
from rational_rays import frame_data,cell_bound

data=json.load(open('rational_ray_witnesses.json'))
cells=json.load(open('strong_moment_cells.json'))
prior=json.load(open('STRAT5/weight_moment_cells.json'))
oldverts=vertices()
for rec in data['witnesses']:
    r=F(rec['r'])
    info=frame_data(rec['U'],rec['W'],r)
    a,lam=info['a'],info['lam']
    assert a==F(rec['a']) and info['T']==F(rec['T'])
    assert 0<r<=1 and r>F(3,25) and lam>a and a>F(443,1000)
    assert min(info['weights'])==0 and sum(info['weights'])==1
    # Independent original trace calculation, without radial coefficients.
    U,W=rec['U'],rec['W']
    uu,ww=sum(x*x for x in U),sum(x*x for x in W)
    Q=[[F(U[i]*U[j],uu)+F(W[i]*W[j],ww)for j in range(5)]for i in range(5)]
    gap=[[a*F(U[i]*U[j],uu)+a*r*F(W[i]*W[j],ww)for j in range(5)]for i in range(5)]
    Pi=[[F(int(i==j))-F(1,5)-Q[i][j]for j in range(5)]for i in range(5)]
    x1=2*(lam*a*(1+r)-a*a*(1+r*r))
    x2=F(10,3)*sum(Pi[i][j]*gap[i][j]**2 for i in range(5)for j in range(5))
    x3=(1-lam)/3*(2*a*(1+r)-F(10,3)*sum(Pi[i][i]*gap[i][i]for i in range(5)))
    twice_s5=2*sum((lam/5+gap[i][j])*(Pi[i][i]+Pi[j][j]-2*Pi[i][j])
                       *(gap[i][i]+gap[j][j]-2*gap[i][j])for i in range(5)for j in range(i+1,5))
    assert x1+x2+x3-twice_s5==info['T']
    assert not any(F(c['rlo'])<=r<=F(c['rhi']) and a<=F(c['ahi'])for c in prior)
    if r==1:
        assert a>F(11,20)
        # The old equal-gap endpoint is less than 11/20.
        assert (F(476)*F(11,20)-209)**2>9*305
    A,B,C=info['moments']
    cr=max(F(0),1-7*r)*(9+r)/24
    old=value((A,B,C),a,r,0,0,0,0,0)-a*cr*C
    assert old==F(rec['old_moment'])<0
    limits=[]
    for p in oldverts:
        L=value(p,F(0),r,0,0,0,0,0)
        H=value(p,F(1),r,0,0,0,0,0)-L-cr*p[2]
        if H<0:
            limits.append(-L/H)
    assert a>min(limits)
    oldD=34+52*r-22*r*r+max(F(0),1-7*r)*(9+r)/2
    assert a>14*(1+r)/oldD
    if r>=F(3,5):
        k=A+B+2*C
        fm=A+r*B+(1+r)*C
        zn=a*fm*fm/(1+r)-lam*(2-k)/5
        zj=a*fm*fm/(1+r)-lam*(4-k)/5
        oldw=value((A,B,C),a,r,0,0,0,0,0)
        oldw+=(5*r/3-1)*max(F(0),zn)+(1+r)*max(F(0),zj)
        assert oldw==F(rec['old_weight'])<0
    cell=cells[rec['cell']]
    assert F(cell['rlo'])<=r<=F(cell['rhi'])
    bound=cell_bound(cell,info['moments'],a,r)
    assert info['T']/a>=bound==F(rec['bound'])>=0
print('PROVED:',len(data['witnesses']),'exact connected zero-edge endpoints satisfy all old remaining conditions and the new bound.')
