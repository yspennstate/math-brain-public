"""Exact lower return iterations for the copied C33 block model.

Floors are computed by integer division and always round downward. A crossing
is an algebraic witness pending the probabilistic interpretation in C34.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json

BASE=Path(__file__).resolve().parent
SCALE=10**12

def parameters(record):
    classes=record['classes'];episodes=record['episodes']
    a=F(episodes['bulk_top']['exit_means']['up'])
    b={e:F(episodes['bulk_top']['exit_means'][e]) for e in classes}
    ac={c:F(episodes['bulk_bottom_'+c]['exit_means']['up']) for c in classes}
    bc={c:{e:F(episodes['bulk_bottom_'+c]['exit_means'][e]) for e in classes} for c in classes}
    root={c:{e:F(episodes['root_bottom_'+c]['exit_means'][e]) for e in classes} for c in classes}
    assert classes and all(a>=0 for a in [a,*b.values(),*ac.values()])
    for c in classes:
        assert F(episodes['root_bottom_'+c]['exit_means']['up'])==0
        assert sum(root[c].values())>=1
    return classes,a,b,ac,bc,root

def iterate(data,limit=200):
    classes,a,b,ac,bc,root=data
    min_root=min(sum(row.values()) for row in root.values())
    x=F(0);y={c:F(0) for c in classes};history=[]
    def lower_floor(value):
        scaled=value*SCALE
        return F(scaled.numerator//scaled.denominator,SCALE)
    for n in range(1,limit+1):
        new_x=lower_floor(a+sum(b[e]*x*y[e] for e in classes))
        new_y={c:lower_floor(ac[c]+sum(bc[c][e]*x*y[e] for e in classes)) for c in classes}
        assert new_x>=x and all(new_y[c]>=y[c] for c in classes)
        x,y=new_x,new_y
        history.append({'n':n,'x_lower':str(x),'y_lower':{c:str(v) for c,v in y.items()},'root_mean_factor_lower':str(x*min_root)})
        if x*min_root>=1:break
    return {'iterations':len(history),'witness':x*min_root>=1,'x_lower':str(x),
            'minimum_root_local_offspring_mean':str(min_root),'root_mean_factor_lower':str(x*min_root),
            'rounding':'every coordinate floored to 10^-12 by exact integer division',
            'history':history}

def main():
    gate=BASE/'C34_FRONTIER_CHECK.txt';assert gate.exists() and gate.stat().st_size>0
    source_digest=hashlib.sha256((BASE/'exact_site_block_upper.py').read_bytes()).hexdigest()
    # Independent one-site ordinary-T4 calculation, not an extracted C33 row.
    analytic=(['one'],F(2,5),{'one':F(8,5)},{'one':F(1,5)},
              {'one':{'one':F(4,5)}},{'one':{'one':F(1)}})
    analytic_result=iterate(analytic)
    assert analytic_result['witness'],'Known noncontracting one-site control did not fire'
    cases=[];seen=set()
    for path in sorted((BASE/'computations').glob('c33_site_*/final.json')):
        record=json.loads(path.read_text(encoding='utf-8'))
        if record['source_sha256']!=source_digest:continue
        params=record['parameters'];key=(params['d'],params['expanded'],params['root_only'])
        if key not in [(4,0,False),(4,1,False),(6,0,True)]:continue
        data=parameters(record);result=iterate(data)
        if key==(6,0,True):
            classes,a,b,ac,bc,root=data;assert classes==['root']
            assert a+b['root']*F(1,2)*F(1,4)==F(1,2)
            assert ac['root']+bc['root']['root']*F(1,2)*F(1,4)==F(1,4)
            assert not result['witness'] and F(result['x_lower'])<=F(1,2)
        cases.append({'parameters':params,'coefficient_file':str(path.relative_to(BASE)),
                      'coefficient_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                      'source_sha256':source_digest,'sites':record['sites'],**result})
        seen.add(key)
    assert seen=={(4,0,False),(4,1,False),(6,0,True)},'Missing live scope; an empty read cannot pass'
    output={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'C33 copied site-block upper process; not the ordinary frog model',
            'status':'exact algebraic witnesses; probabilistic route-failure proof unaudited',
            'live_cases_read':len(cases),'analytic_T4_one_site_control':analytic_result,
            'known_T6_finite_control':'F(1/2,1/4)=(1/2,1/4); no crossing',
            'scale':SCALE,'cases':cases}
    path=BASE/'C34_RETURN_LOWER_RESULTS.json';part=path.with_suffix('.json.part')
    part.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8');part.replace(path)
    for row in cases:print(json.dumps({k:row[k] for k in ['parameters','sites','iterations','witness','x_lower','minimum_root_local_offspring_mean','root_mean_factor_lower']}),flush=True)

if __name__=='__main__':main()
