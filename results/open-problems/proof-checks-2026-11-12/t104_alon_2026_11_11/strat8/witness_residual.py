"""PROVED: the exact witnesses satisfy every STRAT6 residual filter.
The inherited bounds are used only to locate witnesses, not prove positivity.
"""
import json
from fractions import Fraction as F
from moment_bounds import vertices,value
from rational_rays import frame_data


def replay():
    witnesses=json.load(open('exact_witnesses.json'))['witnesses']
    cells=json.load(open('strong_moment_cells.json'))+json.load(open('enhanced_moment_cells.json'))+json.load(open('directional_moment_cells.json'))
    wcells=json.load(open('prior_weight_moment_cells.json'))
    vv=[vertices(False),vertices(True)]
    print('PROVED: exact residual threshold vertex counts',list(map(len,vv)),flush=True)
    for row in witnesses:
        r=F(row['r']); data=frame_data(row['U'],row['W'],r);a=data['a']
        cr=max(F(0),1-7*r)*(9+r)/24
        A0=14*(1+r)/(34+52*r-22*r*r+12*cr)
        thresholds=[A0,F(103,200)]
        for verts in vv:
            ratios=[]
            for p in verts:
                ell=value(p,F(0),r,0,0,0,0,0)
                hh=value(p,F(1),r,0,0,0,0,0)-ell-cr*p[2]
                if hh<0:ratios.append(ell/(-hh))
            assert ratios
            thresholds.append(min(ratios))
        thresholds.extend(F(c['ahi'])for c in cells+wcells if F(c['rlo'])<=r<=F(c['rhi']))
        assert a>max(thresholds)and a<F(2)/(3-r)
        assert min(data['weights'])<(data['lam']-a)/5
        assert value(data['moments'],a,r,0,0,0,0,0)-a*cr*data['moments'][2]<0
        assert F(row['max_moment_lower'])<0 and row['outside_prior_boxes']
        assert r<F(3,5)or F(row['nonlinear_lower'])<0
        assert row['chart_certificate']is not None
    print('PROVED:',len(witnesses),'exact endpoints satisfy every residual filter in STRAT6 (a=a_end).')

if __name__=='__main__':replay()
