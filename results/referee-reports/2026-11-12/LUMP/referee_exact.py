"""Exact comb, four-state witness, and occupation-flow certificates."""
import json
from fractions import Fraction as F
from referee_core import exact_chain, exact_hit, lump, comb, display

out = {'method': 'grounded Laplacian plus exact occupation LP certificates', 'comb': []}
for n in [1,2,4,8]:
    for t in ([4,16,256,4096] if n in [2,4] else [256]):
        w, labels = comb(n,t,t,1+t**3)
        a = exact_chain(w)
        b = exact_chain(lump(w,labels))
        h, alpha, r = F(t), F(t), F(1+t**3)
        delta = (2+alpha+alpha*h)/(r-1)
        m = h+(n+1)*(1+delta)
        bound = h+(n+2)*(1+delta)
        rho = sum(w[-1])/r**n
        low = n*h*alpha/(1+alpha)
        hit = max(row[-1] for row in a['H'])
        assert hit <= m and a['tmix'] <= max(bound,m+bound-rho)
        assert rho >= m and a['tmix'] <= bound
        assert b['H'][0][-1] >= low and b['tmix'] >= a['pi'][-1]*low
        out['comb'].append(dict(N=n,t=t,tmix=display(a['tmix']),
             lumped=display(b['tmix']),ratio=display(b['tmix']/a['tmix']),
             hit_ratio=display(b['H'][0][-1]/hit)))
for n,h,alpha,r,ell in [(1,1,1,2,0),(2,3,F(1,2),2,0),
                        (3,7,11,3,5),(4,F(5,2),F(7,3),F(13,4),100)]:
    w, labels = comb(n,h,alpha,r,ell=ell)
    a,b = exact_chain(w),exact_chain(lump(w,labels))
    delta = (2+F(alpha)+F(alpha)*h)/(F(r)-1)
    m = h+(n+1)*(1+delta)
    bound = h+(n+2)*(1+delta)
    rho = sum(w[-1])/F(r)**n
    low = n*F(h)*alpha/(1+F(alpha))
    assert max(row[-1] for row in a['H']) <= m
    assert a['tmix'] <= max(bound,m+bound-rho)
    assert b['H'][0][-1] >= low and b['tmix'] >= a['pi'][-1]*low
out['off_diagonal_parameter_cases'] = 4
w = [[F(0)]*4 for _ in range(4)]
for i,j,x in [(0,2,1),(1,2,1),(1,3,109),(2,3,54)]:
    w[i][j]=w[j][i]=F(x)
w[1][1],w[3][3] = F(117),F(10000)
a,b = exact_chain(w),exact_chain(lump(w,[0,1,2,2]))
out['four_state'] = dict(tmix=display(a['tmix']),lumped=display(b['tmix']),
                       ratio=display(b['tmix']/a['tmix']),
                       starts=list(map(str,a['starts'])),lumped_starts=list(map(str,b['starts'])))
assert a['tmix'] == F(149731115,63193903)
assert b['tmix'] == F(346900,114917)
# Explicit negative-eigenvalue and complete-graph equality checks.
out['equalities'] = []
for size in range(2,7):
    w = [[F(i!=j) for j in range(size)] for i in range(size)]
    a=exact_chain(w)
    assert a['tmix'] == F(size-1,size)
    out['equalities'].append([size,str(a['tmix'])])
for p,q in [(F(1),F(1)),(F(1,3),F(2,5)),(F(4,5),F(9,10))]:
    w = [[(1-p)/p,F(1)],[F(1),(1-q)/q]]
    assert exact_chain(w)['tmix'] == 1/(p+q)
out['all_exact_certificates_passed']=True
with open('referee_exact.json','w') as f:
    json.dump(out,f,indent=2)
print('All exact occupation LP certificates and comb inequalities passed.')
for row in out['comb']:
    print('N=%d t=%d tmix=%.12g lumped=%.12g ratio=%.12g hit_ratio=%.12g' %
          (row['N'],row['t'],row['tmix']['decimal'],row['lumped']['decimal'],row['ratio']['decimal'],row['hit_ratio']['decimal']))
print('FOUR STATE',out['four_state'])
