from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent

def step(state,is_mirror):
    x,y,axis=state
    if is_mirror(x,y):
        axis=1-axis
    if axis==0:
        x+=1 if y%2==0 else -1
    else:
        y+=1 if x%2==0 else -1
    return x,y,axis

def period(state,is_mirror,limit):
    initial=state; orbit=[]
    for _ in range(limit):
        orbit.append(state)
        state=step(state,is_mirror)
        if state==initial:
            return orbit
    return None

def main():
    start=time.perf_counter()
    mirrors={(-3,0),(0,0),(-3,3),(0,3)}
    initial=(0,0,0)
    orbit=period(initial,lambda x,y:(x,y) in mirrors,20)
    assert orbit is not None and len(orbit)==12
    added=mirrors|{(0,1)}
    route=[initial]
    state=initial
    for _ in range(6):
        state=step(state,lambda x,y:(x,y) in added)
        route.append(state)
    assert route[1]==(0,1,1)
    assert route[2]==(-1,1,0)
    assert state==(-5,1,0)
    assert not any(y==1 and x<0 for x,y in added)
    # Every future vertex is (-5-k,1): empty, horizontal, and directed west.
    for k in range(12):
        assert step((-5-k,1,0),lambda x,y:(x,y) in added)==(-6-k,1,0)
    dense=[]
    for x in (0,1):
        for y in (0,1):
            for axis in (0,1):
                cycle=period((x,y,axis),lambda x,y:True,8)
                assert cycle is not None and len(cycle)==4
                dense.append({'state':[x,y,axis],'period':4})
    empty=step(initial,lambda x,y:False)
    assert empty==(1,0,0)
    result={'command':'python -X utf8 p0009_check.py','period_before_added_mirror':12,
            'after_added_mirror':'certified empty westward ray; unbounded',
            'orbit':orbit,'added_mirror_route':route,'q_one_parity_axis_cases':dense,
            'q_zero':'straight eastward ray; unbounded','elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'p0009.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('orbit','added_mirror_route','q_one_parity_axis_cases')},indent=2))

if __name__=='__main__':
    main()
